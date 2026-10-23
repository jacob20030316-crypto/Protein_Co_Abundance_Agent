# Conserved co-abundance modules: heart and stem_cells

## Module 0

**Tissue pair**: heart and stem_cells  
**Genes (38)**: BZW2, ALDH3A2, BLVRA, CAPN1, CISD2, CNDP2, CTNNA1, CYRIB, DYNC1H1, EIF3L, FLNB, GSN, GET3, HK1, IQGAP1, LTA4H, MESD, SLC8A1, NES, NEXN, OLA1, PANK4, PDCD6IP, PFKP, PGM2, PSMC4, ADSL, RO60, RTCA, SEC23A, SPTBN1, FARSB, KARS1, QARS1, USP5, USO1, XPO1, XPNPEP1

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established pathway-level label from enrichment alone. Its gene content instead points to a mixed cellular program involving cytoskeletal and adhesion organization, intracellular trafficking, translation capacity, glucose metabolism, calcium handling, proteostasis, and redox or aldehyde management. The network is compatible with a structural and metabolic maintenance program in muscle-related cells, but the breadth of the annotations argues against assigning one narrowly defined biological process. Heart relevance is supported by HPA detection for most genes in heart muscle and by heart-enhanced genes such as NEXN and SLC8A1. The shared heart–stem_cells signal may therefore reflect conserved cellular machinery rather than a tissue-exclusive pathway.

**Cell composition.** The module is not predominantly plasma or secreted: only a minority of genes are secreted, and most are intracellular or membrane-associated. It is also not strongly blood-cell specific, because most genes have low immune-cell specificity, although a small subset shows immune-cell enhancement or blood-cell associations, including SLC8A1, GSN, PANK4, CYRIB, and LTA4H. HPA indicates broad rather than uniform tissue restriction, with many genes having low tissue specificity and several enhanced in heart muscle, skeletal muscle, or related tissues. The strong representation of cell-type-enhanced genes in epithelial, germ-cell, trophoblast, and muscle-related populations suggests that shared cell states or broadly conserved cellular programs may contribute to the co-abundance pattern. The module should therefore not be interpreted as a purely cardiomyocyte-specific program without cell-composition controls.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a set of already known high-confidence relationships rather than a coherent interaction system covering the whole module. Known links include the glycolytic pair HK1–PFKP, HK1–PGM2, the aminoacyl-tRNA synthetase pair KARS1–QARS1, FARSB–KARS1, and FARSB–OLA1, the actin-associated pair FLNB–GSN, the adhesion-associated pair CTNNA1–IQGAP1, the ALDH3A2–CNDP2 pair, and the trafficking-associated pair SEC23A–USO1. These relationships support real biochemical, structural, or trafficking submodules, but the limited STRING connectivity means that co-abundance should not be equated with direct physical interaction. hu.MAP independently places subsets of the genes in complexes: (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1) support a KARS1–QARS1 aminoacylation-related association; (hu.MAP huMAP3_12394.1) supports a USO1–SEC23A trafficking-related association; (hu.MAP huMAP3_14442.1) groups LTA4H, ADSL, XPNPEP1, and OLA1 in a larger complex; (hu.MAP huMAP3_08741.1) links RTCA and MESD; (hu.MAP huMAP3_14982.1) links MESD and FARSB; and (hu.MAP huMAP3_09592.1) links XPO1 and ALDH3A2. The hu.MAP evidence therefore supports several local molecular assemblies, while also showing that many module genes do not belong to one shared complex.

**STRING interactions (score >= 0.7)**: 9 of 703 gene pairs: ALDH3A2–CNDP2 (0.928); CTNNA1–IQGAP1 (0.859); FARSB–KARS1 (0.813); FARSB–OLA1 (0.702); FLNB–GSN (0.745); HK1–PFKP (0.995); HK1–PGM2 (0.945); KARS1–QARS1 (0.999); SEC23A–USO1 (0.704)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (LTA4H, ADSL, XPNPEP1, OLA1; 4/57); huMAP3_08741.1 (RTCA, MESD; 2/5); huMAP3_02637.1 (QARS1, KARS1; 2/14); huMAP3_13688.1 (QARS1, KARS1; 2/14); huMAP3_14982.1 (MESD, FARSB; 2/28); huMAP3_09592.1 (XPO1, ALDH3A2; 2/95); huMAP3_12394.1 (USO1, SEC23A; 2/98)

### Novelty

This module should not be called a wholly new molecular complex or a newly discovered pathway. Several of its relationships and functional components are already represented in STRING and hu.MAP, including translation machinery, glycolysis, actin organization, and ER-to-Golgi trafficking. Nevertheless, the conserved co-abundance of this particular combination across heart and stem_cells may still be a new systems-level observation, especially because the module combines structural, metabolic, translational, and trafficking genes without a globally significant GO/KEGG label. Absence of a complete matching interaction network in STRING or hu.MAP would not by itself establish novelty. The defensible claim is that the cross-tissue co-abundance pattern is potentially novel, whereas the individual molecular functions and several local relationships are established.

**Hypothesis.** Hypothesis: the module represents a conserved cellular maintenance state that couples cytoskeletal integrity and adhesion with energy supply, calcium homeostasis, protein synthesis, and membrane trafficking. In heart-related cells, NEXN, SLC8A1, and associated actin or membrane components could coordinate mechanical architecture and calcium-dependent contractile physiology, while HK1 and PFKP support glycolytic input, QARS1 and KARS1 support translational capacity, and USO1 with SEC23A supports ER-to-Golgi cargo movement. In stem-cell contexts, the same program could support proliferation, differentiation, cytoskeletal remodeling, and high biosynthetic demand. This is a mechanistic model rather than a demonstrated causal pathway; the co-abundance data do not establish direct regulation or physical interaction among all module members.

### Important genes

#### NEXN

- **Related proteins** (co-abundance neighbors): CISD2 (0.91), BZW2 (0.91), KARS1 (0.88), EIF3L (0.87), QARS1 (0.86), GET3 (0.86), USO1 (0.86), CTNNA1 (0.85), NES (0.85), USP5 (0.84), LTA4H (0.83), DYNC1H1 (0.83), PDCD6IP (0.83), CAPN1 (0.82), PFKP (0.82), PANK4 (0.82), BLVRA (0.81), XPNPEP1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nexilin F-actin binding protein. This gene encodes a filamentous actin-binding protein that may function in cell adhesion and migration. Mutations in this gene have been associated with dilated cardiomyopathy, also known as CMD1CC. Alternatively spliced transcript variants have been described.[provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: dilated cardiomyopathy 1CC (0.792); hypertrophic cardiomyopathy 20 (0.746); familial isolated dilated cardiomyopathy (0.667); hypertrophic cardiomyopathy (0.584); cardiomyopathy, dilated, 2M (0.565)
- **Europe PMC papers**: 1090
- **Why important**: NEXN is the strongest network hub in the supplied module and connects structural, translational, trafficking, and metabolic neighborhoods. HPA shows enhancement in heart muscle and skeletal muscle, localization at the plasma membrane and actin filaments, and detection in heart. Its established function as an F-actin-binding protein involved in adhesion, migration, and cytoskeletal organization, together with its association with dilated and hypertrophic cardiomyopathy, makes it a strong anchor for the heart-related interpretation. It also has substantial literature support.
- **Conclusion**: Established evidence supports NEXN as a muscle-relevant cytoskeletal and adhesion component with cardiomyopathy relevance and a central position in this network. It is plausible, but not proven, that NEXN helps organize the structural arm of the shared module and couples it to metabolic or biosynthetic state.

#### SLC8A1

- **Related proteins** (co-abundance neighbors): BLVRA (0.91), FARSB (0.90), GET3 (0.86), DYNC1H1 (0.85), CAPN1 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Nucleoplasm, Plasma membrane; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 8 member A1. In cardiac myocytes, Ca(2+) concentrations alternate between high levels during contraction and low levels during relaxation. The increase in Ca(2+) concentration during contraction is primarily due to release of Ca(2+) from intracellular stores. However, some Ca(2+) also enters the cell through the sarcolemma (plasma membrane). During relaxation, Ca(2+) is sequestered within the intracellular sto…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.551); hypertensive disorder (0.429); smoking initiation (0.427); essential hypertension (0.424); bone fracture (0.405)
- **Europe PMC papers**: 2125
- **Why important**: SLC8A1 is tissue-enriched in heart muscle according to HPA, is detected in heart, and is associated with cardiomyocytes. Its established role in sodium and calcium homeostasis, heart-rate regulation, and force of contraction gives the module a direct cardiac physiological connection. In the network it links calcium handling to DYNC1H1, BLVRA, FARSB, GET3, and CAPN1, connecting membrane physiology with transport, metabolism, and proteolysis. Its immune-cell annotation also makes it useful for assessing possible cell-composition effects.
- **Conclusion**: Established evidence supports SLC8A1 as a cardiac calcium-handling component and one of the most biologically informative genes in the module. The hypothesis that its co-abundance marks coordinated excitation–contraction or calcium-stress adaptation across the two tissues requires functional testing.

#### PFKP

- **Related proteins** (co-abundance neighbors): QARS1 (0.95), XPO1 (0.90), SPTBN1 (0.87), EIF3L (0.86), HK1 (0.85), DYNC1H1 (0.84), RO60 (0.82), NES (0.82), NEXN (0.82); STRING partners: HK1 (0.995)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphofructokinase, platelet. This gene encodes a member of the phosphofructokinase A protein family. The encoded enzyme is the platelet-specific isoform of phosphofructokinase and plays a key role in glycolysis regulation. This gene may play a role in metabolic reprogramming in some cancers, including clear cell renal cell carcinomas, and cancer of the bladder, breast, and lung. Alternative splicing results in multiple transc…
- **Diseases (Open Targets)**: alcohol drinking (0.443); response to water (0.426); neurodegenerative disease (0.414); Alzheimer disease (0.372); spinocerebellar ataxia, autosomal recessive 30 (0.353)
- **Europe PMC papers**: 3384
- **Why important**: PFKP encodes the platelet isoform of phosphofructokinase and is an established regulator of glycolysis. It is connected in the module to QARS1, XPO1, EIF3L, SPTBN1, HK1, DYNC1H1, RO60, and NES, and it has a high-confidence STRING relationship with HK1. Its heart detection and extensive literature support make it a strong metabolic representative, although its HPA enrichment is in retina rather than heart.
- **Conclusion**: Established evidence supports PFKP as a glycolytic component that may provide metabolic context for the module. The proposed coupling of glycolytic flux to cytoskeletal, calcium, and translation-related co-abundance is a hypothesis, not a demonstrated causal relationship.

#### QARS1

- **Related proteins** (co-abundance neighbors): PFKP (0.95), USO1 (0.93), EIF3L (0.90), DYNC1H1 (0.89), NES (0.88), XPO1 (0.88), SPTBN1 (0.87), HK1 (0.86), NEXN (0.86), GSN (0.83), CAPN1 (0.82); STRING partners: KARS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutaminyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. In metazoans, 9 aminoacyl-tRNA synthetases specific for glutamine (gln), glutamic acid (glu), and 7 other amino …
- **Diseases (Open Targets)**: diffuse cerebral and cerebellar atrophy - intractable seizures - progressive microcephaly syndrome (0.794); hereditary disease (0.415); intellectual disability, autosomal dominant 43 (0.340); microcephaly (0.298); attention deficit-hyperactivity disorder (0.111)
- **Europe PMC papers**: 253
- **Why important**: QARS1 is a network connector linking PFKP, USO1, EIF3L, DYNC1H1, NES, XPO1, SPTBN1, and HK1. Its established function is glutaminyl-tRNA aminoacylation for protein translation, and it is supported by the very strong STRING relationship with KARS1 and by hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). It is detected in heart and has meaningful disease and literature support, while its broad tissue profile is consistent with a conserved biosynthetic function.
- **Conclusion**: Established evidence supports QARS1 as part of the module's translation-capacity arm and as a bridge between biosynthetic and structural neighborhoods. It is reasonable to hypothesize that increased protein-production demand helps explain the shared co-abundance, but this cannot be inferred as a direct translational response from the module alone.

#### USO1

- **Related proteins** (co-abundance neighbors): QARS1 (0.93), KARS1 (0.86), NEXN (0.86), EIF3L (0.84), DYNC1H1 (0.82), ALDH3A2 (0.82); STRING partners: SEC23A (0.704)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: USO1 vesicle transport factor. The protein encoded by this gene is a peripheral membrane protein which recycles between the cytosol and the Golgi apparatus during interphase. It is regulated by phosphorylation: dephosphorylated protein associates with the Golgi membrane and dissociates from the membrane upon phosphorylation. Ras-associated protein 1 recruits this protein to coat protein complex II (COPII) vesicles during buddin…
- **Diseases (Open Targets)**: psoriatic arthritis (0.184); bipolar disorder (0.150); retinitis pigmentosa (0.085); cone dystrophy (0.076); cone-rod dystrophy (0.076)
- **Europe PMC papers**: 546
- **Why important**: USO1 occupies a connector position between QARS1, KARS1, NEXN, EIF3L, DYNC1H1, and ALDH3A2. It is an established ER-to-Golgi vesicle-transport factor and is localized to the Golgi. Its link to SEC23A in STRING and shared hu.MAP membership (hu.MAP huMAP3_12394.1) provide convergent support for a trafficking submodule. HPA shows skeletal-muscle enhancement and myonuclear cell-type enhancement, although it was not detected in heart by IHC.
- **Conclusion**: Established evidence supports USO1 as a vesicle-trafficking component that connects the module's biosynthetic and structural features. A possible role in coordinating cargo delivery during muscle or stem-cell remodeling is a hypothesis and should not be treated as established from co-abundance alone.

## Module 1

**Tissue pair**: heart and stem_cells  
**Genes (13)**: PRKAG1, AGK, ALDH1B1, CAVIN3, TSFM, AGL, MFN1, MMAB, NIBAN1, PARVA, PDXK, PYGB, IARS2

### Function

The module is most consistent with coordinated cellular energy metabolism, especially glycogen handling, mitochondrial maintenance, and metabolic stress adaptation. AGL and PYGB provide the clearest functional anchor: AGL is a glycogen-debranching enzyme, PYGB catalyzes the rate-determining step of glycogen degradation, and they are connected by the strongest STRING relationship in the module. PRKAG1 is an AMPK regulatory subunit that senses cellular energy status, while MFN1 supports mitochondrial fusion and TSFM supports mitochondrial protein translation. Additional genes support related metabolic processes, including mitochondrial lipid metabolism, vitamin cofactor metabolism, aldehyde catabolism, and cellular stress responses. No GO or KEGG term passed global correction, so this functional interpretation is based on the identities and network relationships of the genes rather than on globally significant pathway enrichment. The absence of a globally enriched term does not invalidate the module.

**Cell composition.** This does not resemble a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It also does not appear primarily to be a blood-cell module. Most genes have low immune-cell specificity, although individual genes show immune-cell associations, including NIBAN1 with neutrophils and CAVIN3 with classical monocytes and myeloid dendritic cells. The module is mixed in tissue expression: several genes are broadly expressed, while others are enhanced in heart muscle, skeletal muscle, blood vessels, liver, or brain. Many genes are cell-type enhanced, including cardiomyocytes, smooth muscle cells, hepatocytes, hepatic stellate cells, and several neural or reproductive cell types. Thus, the shared heart and stem-cell signal could reflect a conserved metabolic program or shared cellular composition rather than a heart-specific pathway. HPA detects several proteins in heart, but there is no matching HPA tissue category for stem_cells, so protein-level support in the stem-cell group cannot be assessed from this sheet.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides limited direct support. The only high-confidence STRING interaction is AGL--PYGB, which is biologically coherent because both proteins participate in glycogen degradation. No STRING functional enrichment was reported. hu.MAP repeatedly places AGL and PYGB together in glycogen-related complexes (hu.MAP huMAP3_08013.1) through (hu.MAP huMAP3_12186.1), alongside proteins such as GYG2, STBD1, PYGL, GYS2, glycogen-associated phosphatase regulators, and autophagy-related proteins. These repeated complexes strengthen the interpretation that the AGL--PYGB pair is a known glycogen-metabolism relationship, although only those two complex members belong to this module. TSFM and IARS2 co-occur in the mitochondrial complex (hu.MAP huMAP3_13468.1), supporting a mitochondrial translation component, but that complex is much broader and does not establish a unified physical complex for the entire module. The remaining co-abundance edges lack corresponding STRING or hu.MAP evidence in the supplied data; they should therefore be regarded as expression relationships rather than proven direct physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 78 gene pairs: AGL–PYGB (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08013.1 (PYGB, AGL; 2/8); huMAP3_06909.1 (PYGB, AGL; 2/9); huMAP3_01396.1 (PYGB, AGL; 2/10); huMAP3_08093.1 (PYGB, AGL; 2/12); huMAP3_10227.1 (PYGB, AGL; 2/14); huMAP3_09760.1 (PYGB, AGL; 2/15); huMAP3_13075.1 (PYGB, AGL; 2/15); huMAP3_11993.1 (PYGB, AGL; 2/20); huMAP3_12186.1 (PYGB, AGL; 2/23); huMAP3_13468.1 (TSFM, IARS2; 2/99)

### Novelty

The module may represent a previously unreported co-abundance pattern, but the supplied evidence is not sufficient to call it a new biological mechanism. Its strongest internal relationships recapitulate established biology: AGL and PYGB are linked by STRING and recur together in hu.MAP complexes, while TSFM and IARS2 occur in a mitochondrial translation complex. The broader combination of glycogen metabolism, mitochondrial dynamics, mitochondrial translation, AMPK signaling, and adhesion-related proteins is less directly established. Lack of STRING or hu.MAP support for several edges is compatible with a novel co-abundance association, but absence from those resources alone does not prove novelty. The most defensible claim is that this is a potentially novel cross-tissue expression module assembled partly from known metabolic relationships, requiring independent replication and perturbation before being considered a new mechanistic discovery.

**Hypothesis.** Hypothesis: the module coordinates fuel mobilization with mitochondrial capacity in metabolically active or differentiating cells. Under changing nutrient or energy conditions, AMPK-related signaling through PRKAG1 could be associated with glycogen breakdown by PYGB and AGL, while MFN1 and the TSFM-IARS2 mitochondrial translation axis help maintain the mitochondrial network and its protein-synthesis capacity. PARVA, CAVIN3, and related genes may connect this metabolic state to adhesion, membrane organization, or cellular context. This model predicts coordinated changes in glycogen turnover, mitochondrial morphology, and mitochondrial translation when the module is perturbed. It is a hypothesis, not an established physical pathway inferred from the current evidence.

### Important genes

#### AGL

- **Related proteins** (co-abundance neighbors): MFN1 (0.87), NIBAN1 (0.86), TSFM (0.86), MMAB (0.81); STRING partners: PYGB (0.999)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08013.1, huMAP3_06909.1, huMAP3_01396.1, huMAP3_08093.1, huMAP3_10227.1, huMAP3_09760.1, huMAP3_13075.1, huMAP3_11993.1, huMAP3_12186.1
- **Function (MyGene.info)**: amylo-alpha-1,6-glucosidase and 4-alpha-glucanotransferase. This gene encodes the glycogen debrancher enzyme which is involved in glycogen degradation. This enzyme has two independent catalytic activities which occur at different sites on the protein: a 4-alpha-glucotransferase activity and a amylo-1,6-glucosidase activity. Mutations in this gene are associated with glycogen storage disease although a wide range of enzymatic and clinical variability occurs…
- **Diseases (Open Targets)**: glycogen storage disease III (0.831); disorder of glycogen metabolism (0.768); glycogen storage disease XV (0.608); hereditary disease (0.507); Acute rhabdomyolysis (0.463)
- **Europe PMC papers**: 4441
- **Why important**: AGL is a central network connector and the clearest glycogen-metabolism anchor. It has multiple module neighbors, forms the strongest STRING relationship with PYGB, and appears with PYGB across the repeated hu.MAP complexes (hu.MAP huMAP3_08013.1) through (hu.MAP huMAP3_12186.1). Its established function is glycogen debranching during glycogen degradation, and its disease associations include glycogen storage disease. Its heart and skeletal-muscle relevance also fits the tissue-pair context. The substantial literature base makes its annotation comparatively well established.
- **Conclusion**: Established conclusion: AGL is a credible driver or marker of the module's glycogen-degradation component. Hypothesis: AGL may help couple glycogen mobilization to mitochondrial energy demand in the shared module.

#### PYGB

- **Related proteins** (co-abundance neighbors): MFN1 (0.86), PRKAG1 (0.82); STRING partners: AGL (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_08013.1, huMAP3_06909.1, huMAP3_01396.1, huMAP3_08093.1, huMAP3_10227.1, huMAP3_09760.1, huMAP3_13075.1, huMAP3_11993.1, huMAP3_12186.1
- **Function (MyGene.info)**: glycogen phosphorylase B. The protein encoded by this gene is a glycogen phosphorylase found predominantly in the brain. The encoded protein forms homodimers which can associate into homotetramers, the enzymatically active form of glycogen phosphorylase. The activity of this enzyme is positively regulated by AMP and negatively regulated by ATP, ADP, and glucose-6-phosphate. This enzyme catalyzes the rate-determining step i…
- **Diseases (Open Targets)**: neurodegenerative disease (0.419); prostate carcinoma (0.329); Short stature (0.259); neoplasm (0.102); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 901
- **Why important**: PYGB is the complementary glycogen-metabolism anchor to AGL. It is connected to AGL by STRING, recurs with AGL in the hu.MAP complexes (hu.MAP huMAP3_08013.1) through (hu.MAP huMAP3_12186.1), and is connected in the module to MFN1 and PRKAG1. PYGB catalyzes a rate-determining step in glycogen degradation and is regulated by cellular energy metabolites. It is detected in heart by HPA and has established disease and metabolism literature, although its tissue annotation is not specifically restricted to heart.
- **Conclusion**: Established conclusion: PYGB strongly supports glycogen turnover as part of the module's biology. Hypothesis: its co-abundance with PRKAG1 and MFN1 may reflect coordinated control of glycogen availability and mitochondrial energy use.

#### MFN1

- **Related proteins** (co-abundance neighbors): AGL (0.87), PYGB (0.86), AGK (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitofusin 1. The protein encoded by this gene is a mediator of mitochondrial fusion. This protein and mitofusin 2 are homologs of the Drosophila protein fuzzy onion (Fzo). They are mitochondrial membrane proteins that interact with each other to facilitate mitochondrial targeting. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.514); breast carcinoma (0.211); uterine corpus leiomyoma (0.205); lobular capilliary hemangioma (0.203); neoplasm (0.099)
- **Europe PMC papers**: 9140
- **Why important**: MFN1 occupies a strategically informative position between AGL, PYGB, and AGK in the co-abundance network. It encodes a mitochondrial membrane protein that mediates mitochondrial fusion and is linked to mitochondrial organization and membrane potential. It has broad tissue and cell-type expression, no reported STRING partner in this module, and no hu.MAP complex assignment here. Its large literature base and disease links make its core mitochondrial function well established, while its module-level connection to glycogen genes is less directly documented.
- **Conclusion**: Established conclusion: MFN1 supplies a mitochondrial-dynamics component to the module. Hypothesis: MFN1 may connect glycogen-derived fuel availability with mitochondrial network remodeling, but the current data do not demonstrate that mechanism.

#### PRKAG1

- **Related proteins** (co-abundance neighbors): PARVA (0.86), PYGB (0.82), PDXK (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase AMP-activated non-catalytic subunit gamma 1. The protein encoded by this gene is a regulatory subunit of the AMP-activated protein kinase (AMPK). AMPK is a heterotrimer consisting of an alpha catalytic subunit, and non-catalytic beta and gamma subunits. AMPK is an important energy-sensing enzyme that monitors cellular energy status. In response to cellular metabolic stresses, AMPK is activated, and thus phosphorylates and inactivates acetyl-…
- **Diseases (Open Targets)**: cardiovascular disorder (0.370); intelligence (0.323); kidney failure (0.280); Abnormality of the skeletal system (0.273); hypertensive heart disease (0.197)
- **Europe PMC papers**: 746
- **Why important**: PRKAG1 connects PYGB with PARVA and PDXK and encodes a regulatory gamma subunit of AMPK, a central cellular energy sensor. Its annotations include regulation of glycolysis and responses to nutrient levels and glucose starvation. Although it has no STRING or hu.MAP relationship reported here, its network position and established energy-sensing function provide a plausible regulatory context for the glycogen and mitochondrial genes. Its disease associations include cardiovascular and kidney phenotypes, which are relevant to metabolic tissues.
- **Conclusion**: Established conclusion: PRKAG1 is a biologically plausible energy-state regulator within the module. Hypothesis: PRKAG1-dependent AMPK signaling may coordinate glycogen mobilization with mitochondrial adaptation in the shared tissue context.

#### TSFM

- **Related proteins** (co-abundance neighbors): AGL (0.86), PARVA (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: Ts translation elongation factor, mitochondrial. This gene encodes a mitochondrial translation elongation factor. The encoded protein is an enzyme that catalyzes the exchange of guanine nucleotides on the translation elongation factor Tu during the elongation step of mitchondrial protein translation. Mutations in this gene are associated with combined oxidative phosphorylation deficiency-3 syndrome. Alternate splicing results in multiple transcr…
- **Diseases (Open Targets)**: fatal mitochondrial disease due to combined oxidative phosphorylation defect type 3 (0.795); steroid-resistant nephrotic syndrome (0.474); hereditary disease (0.414); mitochondrial disease (0.372); neurodegenerative disease (0.370)
- **Europe PMC papers**: 484
- **Why important**: TSFM links AGL and PARVA in the module and is the module member of the mitochondrial translation complex (hu.MAP huMAP3_13468.1). It encodes a mitochondrial translation elongation factor, and its cell-type annotations include cardiomyocytes. Its disease associations include combined oxidative phosphorylation deficiency and other mitochondrial disease. The hu.MAP support with IARS2 gives this mitochondrial translation interpretation more direct external support than the other TSFM-centered module edges.
- **Conclusion**: Established conclusion: TSFM contributes a mitochondrial protein-synthesis component and is especially relevant to cardiomyocyte biology. Hypothesis: TSFM may help determine whether increased glycogen mobilization can be translated into sustained respiratory capacity, but this coupling is not demonstrated by the current data.

## Module 2

**Tissue pair**: heart and stem_cells  
**Genes (35)**: GOT2, ACADVL, ACO2, ACSL1, ALDH2, COQ8A, COQ9, CRYM, DCXR, DSP, DHRS4, ENO3, ETFA, ETFDH, FHL1, FLNC, HADH, IDH2, ITGA7, NDUFA10, NDUFS1, NDUFV1, NNT, MT-ND4, MT-ND5, DBT, BCKDHB, DLAT, SLC25A12, SDHA, ALDH5A1, SUCLG1, SUCLA2, SUCLG2, ACAT1

### Function

The module is best interpreted as a mitochondrial oxidative-energy and intermediary-metabolism module. The strongest primary evidence is the global enrichment for small-molecule metabolism (GO:BP small molecule metabolic process; q_global = 3.95e-06), mitochondria (GO:CC mitochondrion; q_global = 0.00125), generation of precursor metabolites and energy (GO:BP generation of precursor metabolites and energy; q_global = 0.00139), cellular respiration (GO:BP cellular respiration; q_global = 0.00201), metabolic pathways (KEGG Metabolic pathways - Homo sapiens (human); q_global = 0.00243), and oxidation of organic compounds (GO:BP energy derivation by oxidation of organic compounds; q_global = 0.00253). The convergent enrichment for the tricarboxylic-acid cycle (GO:BP tricarboxylic acid cycle; q_global = 0.0104) (KEGG Citrate cycle (TCA cycle) - Homo sapiens (human); q_global = 0.0246), aerobic respiration (GO:BP aerobic respiration; q_global = 0.011), and the electron-transport chain (GO:BP electron transport chain; q_global = 0.0388) (GO:BP respiratory electron transport chain; q_global = 0.0388) supports coordinated mitochondrial fuel oxidation, electron transfer, redox balance, and energy production. The module also contains genes for fatty-acid oxidation, branched-chain amino-acid catabolism, pyruvate entry into the cycle, succinate metabolism, and mitochondrial amino-acid transport. Thus, it is more specific than a generic housekeeping module, although its central function is a broad mitochondrial bioenergetic program rather than a single linear pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It is also unlikely to be primarily a blood-cell module, because most genes have low immune-cell specificity and the muscle-associated signal is much stronger than the immune signal. HPA evidence instead points to heart muscle, skeletal muscle, tongue, and liver, with many genes enhanced in cardiomyocytes, myonuclei, or hepatocytes. Protein detection in heart is widespread among the tested genes, while there is no matching HPA tissue category for stem cells. The shared heart and stem-cell co-abundance signal may therefore reflect a conserved mitochondrial metabolic program, shared metabolically active cell states, or differences in muscle-like differentiation and cellular composition. The liver and hepatocyte-associated genes also warrant caution about possible tissue-composition effects.

**GO/KEGG enrichment**: 17 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP small molecule metabolic process | 3.95e-06 | ACADVL, ACAT1, ACO2, ACSL1, ALDH2, ALDH5A1, BCKDHB, COQ8A, COQ9, DBT, DCXR, DHRS4, DLAT, ENO3, ETFA, ETFDH, GOT2, HADH, IDH2, MT-ND4, MT-ND5, NDUFA10, NDUFS1, NDUFV1, NNT, SDHA, SLC25A12, SUCLA2, SUCLG1, SUCLG2 |
| GO:CC mitochondrion | 0.00125 | ACADVL, ACAT1, ACO2, ACSL1, ALDH2, ALDH5A1, BCKDHB, COQ8A, COQ9, CRYM, DBT, DCXR, DHRS4, DLAT, ETFA, ETFDH, GOT2, HADH, IDH2, MT-ND4, MT-ND5, NDUFA10, NDUFS1, NDUFV1, NNT, SDHA, SLC25A12, SUCLA2, SUCLG1, SUCLG2 |
| GO:BP generation of precursor metabolites and energy | 0.00139 | ACADVL, ACAT1, ACO2, COQ9, DLAT, ENO3, ETFA, ETFDH, IDH2, MT-ND4, MT-ND5, NDUFA10, NDUFS1, NDUFV1, NNT, SDHA, SUCLA2, SUCLG1, SUCLG2 |
| GO:BP cellular respiration | 0.00201 | ACO2, COQ9, DLAT, ENO3, ETFA, ETFDH, IDH2, MT-ND4, MT-ND5, NDUFA10, NDUFS1, NDUFV1, NNT, SDHA, SUCLA2, SUCLG1, SUCLG2 |
| KEGG Metabolic pathways - Homo sapiens (human) | 0.00243 | ACADVL, ACAT1, ACO2, ACSL1, ALDH2, ALDH5A1, BCKDHB, DBT, DCXR, DHRS4, DLAT, ENO3, GOT2, HADH, IDH2, MT-ND4, MT-ND5, NDUFA10, NDUFS1, NDUFV1, NNT, SDHA, SUCLA2, SUCLG1, SUCLG2 |
| GO:BP energy derivation by oxidation of organic compounds | 0.00253 | ACADVL, ACO2, COQ9, DLAT, ENO3, ETFA, ETFDH, IDH2, MT-ND4, MT-ND5, NDUFA10, NDUFS1, NDUFV1, NNT, SDHA, SUCLA2, SUCLG1, SUCLG2 |
| GO:BP purine-containing compound metabolic process | 0.00295 | ACAT1, ACSL1, DCXR, DLAT, ENO3, GOT2, IDH2, MT-ND4, MT-ND5, NDUFA10, NDUFS1, NDUFV1, NNT, SDHA, SLC25A12, SUCLA2, SUCLG1, SUCLG2 |
| GO:BP nucleoside phosphate metabolic process | 0.00344 | ACAT1, ACSL1, DCXR, DLAT, ENO3, GOT2, IDH2, MT-ND4, MT-ND5, NDUFA10, NDUFS1, NDUFV1, NNT, SDHA, SLC25A12, SUCLA2, SUCLG1, SUCLG2 |
| GO:BP nucleobase-containing small molecule metabolic process | 0.00614 | ACAT1, ACSL1, DCXR, DLAT, ENO3, GOT2, IDH2, MT-ND4, MT-ND5, NDUFA10, NDUFS1, NDUFV1, NNT, SDHA, SLC25A12, SUCLA2, SUCLG1, SUCLG2 |
| GO:BP tricarboxylic acid cycle | 0.0104 | ACO2, DLAT, IDH2, NNT, SDHA, SUCLA2, SUCLG1, SUCLG2 |
| GO:BP aerobic respiration | 0.011 | ACO2, COQ9, DLAT, ENO3, IDH2, MT-ND4, MT-ND5, NDUFA10, NDUFS1, NDUFV1, NNT, SDHA, SUCLA2, SUCLG1, SUCLG2 |
| GO:BP organophosphate metabolic process | 0.0154 | ACAT1, ACSL1, DCXR, DLAT, ENO3, GOT2, IDH2, MT-ND4, MT-ND5, NDUFA10, NDUFS1, NDUFV1, NNT, SDHA, SLC25A12, SUCLA2, SUCLG1, SUCLG2 |
| KEGG Citrate cycle (TCA cycle) - Homo sapiens (human) | 0.0246 | ACO2, DLAT, IDH2, SDHA, SUCLA2, SUCLG1, SUCLG2 |
| GO:CC mitochondrial matrix | 0.0315 | ACADVL, ACAT1, ACO2, ALDH2, ALDH5A1, BCKDHB, DBT, DLAT, ETFA, GOT2, HADH, IDH2, NDUFA10, NDUFS1, SDHA, SUCLA2, SUCLG1, SUCLG2 |
| GO:MF oxidoreductase activity | 0.0363 | ACADVL, ALDH2, ALDH5A1, BCKDHB, CRYM, DCXR, DHRS4, ETFA, ETFDH, HADH, IDH2, MT-ND4, NDUFS1, NDUFV1, NNT, SDHA |

### STRING and hu.MAP

STRING provides extensive prior support for the module's biochemical coherence. Known or strongly supported relationships connect the respiratory-chain genes, including the complex-I-related genes NDUFA10, NDUFS1, NDUFV1, MT-ND4, and MT-ND5, and connect them with SDHA, the tricarboxylic-acid-cycle machinery, and electron-transfer flavoprotein genes. STRING also supports relationships among ACADVL, ETFA, ETFDH, and HADH, among the succinyl-CoA ligase subunits, and among the pyruvate and branched-chain amino-acid dehydrogenase components. These relationships indicate that the co-abundance structure substantially recapitulates established mitochondrial biochemistry rather than being an arbitrary gene cluster. The STRING enrichment results (6 supplementary STRING terms; within-query FDR 2.61e-06–8.21e-05) and related metabolic and mitochondrial annotations (6 supplementary STRING terms; within-query FDR 0.0001–0.00016) are concordant supplementary evidence, but they are not treated as global enrichment evidence. hu.MAP independently identifies repeated complex-I assemblies containing NDUFA10, MT-ND4, MT-ND5, NDUFS1, and NDUFV1 (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1) (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_08132.1) (hu.MAP huMAP3_07653.1), the branched-chain dehydrogenase complex containing DBT and BCKDHB (hu.MAP huMAP3_12248.1), and an electron-transfer flavoprotein-related complex containing ETFA and NNT (hu.MAP huMAP3_12388.1). The ACADVL-DHRS4 associations (hu.MAP huMAP3_08580.1) (hu.MAP huMAP3_02431.1) (hu.MAP huMAP3_11915.1) (hu.MAP huMAP3_10506.1) are also represented. Together, STRING and hu.MAP show that much of the module is anchored in known respiratory, catabolic, and mitochondrial complexes, while several co-abundance links may still reflect shared regulation rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 79 of 595 gene pairs: ACADVL–ACSL1 (0.841); ACADVL–ETFA (0.877); ACADVL–ETFDH (0.817); ACADVL–HADH (0.882); ACAT1–DLAT (0.949); ACAT1–ETFA (0.821); ACAT1–HADH (0.935); ACAT1–SDHA (0.762); ACAT1–SUCLA2 (0.883); ACAT1–SUCLG1 (0.907); ACAT1–SUCLG2 (0.867); ACO2–ALDH2 (0.751); ACO2–DLAT (0.727); ACO2–GOT2 (0.753); ACO2–IDH2 (0.998); ACO2–NDUFA10 (0.747); ACO2–NDUFS1 (0.865); ACO2–NDUFV1 (0.944); ACO2–SDHA (0.975); ACO2–SUCLA2 (0.862); ACO2–SUCLG1 (0.929); ACO2–SUCLG2 (0.735); ALDH2–DBT (0.86); ALDH5A1–IDH2 (0.894); BCKDHB–DBT (0.999); BCKDHB–DLAT (0.968); BCKDHB–SUCLA2 (0.793); BCKDHB–SUCLG1 (0.833); BCKDHB–SUCLG2 (0.746); COQ8A–COQ9 (0.991); COQ9–ETFDH (0.801); DBT–SDHA (0.714); DBT–SUCLA2 (0.901); DBT–SUCLG1 (0.956); DBT–SUCLG2 (0.89); DLAT–IDH2 (0.775); DLAT–NDUFS1 (0.773); DLAT–SDHA (0.852); DLAT–SUCLA2 (0.982); DLAT–SUCLG1 (0.99); DLAT–SUCLG2 (0.967); ETFA–ETFDH (0.999); ETFA–HADH (0.791); ETFA–SDHA (0.706); ETFA–SUCLG1 (0.956); FLNC–ITGA7 (0.737); GOT2–IDH2 (0.96); GOT2–SDHA (0.981); IDH2–NNT (0.898); IDH2–SDHA (0.869); IDH2–SUCLA2 (0.857); IDH2–SUCLG1 (0.878); IDH2–SUCLG2 (0.798); MT-ND4–MT-ND5 (0.999); MT-ND4–NDUFA10 (0.999); MT-ND4–NDUFS1 (0.999); MT-ND4–NDUFV1 (0.999); MT-ND4–SDHA (0.922); MT-ND5–NDUFA10 (0.997); MT-ND5–NDUFS1 (0.999); MT-ND5–NDUFV1 (0.999); MT-ND5–SDHA (0.881); NDUFA10–NDUFS1 (0.999); NDUFA10–NDUFV1 (0.999); NDUFA10–SDHA (0.793); NDUFA10–SUCLG1 (0.836); NDUFS1–NDUFV1 (0.999); NDUFS1–SDHA (0.995); NDUFS1–SUCLA2 (0.777); NDUFS1–SUCLG1 (0.752); NDUFS1–SUCLG2 (0.728); NDUFV1–SDHA (0.999); NDUFV1–SUCLG1 (0.836); SDHA–SUCLA2 (0.998); SDHA–SUCLG1 (0.999); SDHA–SUCLG2 (0.997); SUCLA2–SUCLG1 (0.999); SUCLA2–SUCLG2 (0.928); SUCLG1–SUCLG2 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Process Small molecule metabolic process (FDR = 2.61e-06, 30 genes); Process Generation of precursor metabolites and energy (FDR = 4.3e-05, 21 genes); Process Cellular respiration (FDR = 5.01e-05, 17 genes); Process Energy derivation by oxidation of organic compounds (FDR = 5.52e-05, 18 genes); Keyword Mitochondrion (FDR = 8.21e-05, 27 genes); Keyword Transit peptide (FDR = 8.21e-05, 23 genes); HPO Hypotonia (FDR = 0.0001, 25 genes); HPO Abnormality of metabolism/homeostasis (FDR = 0.0001, 29 genes); HPO Lactic acidosis (FDR = 0.0001, 16 genes); HPO Abnormality of acid-base homeostasis (FDR = 0.0001, 20 genes); HPO Abnormal reflex (FDR = 0.0001, 22 genes); HPO Abnormal circulating metabolite concentration (FDR = 0.0001, 24 genes); HPO Abnormal muscle physiology (FDR = 0.00011, 28 genes); HPO Acidosis (FDR = 0.00013, 19 genes); HPO Abnormal homeostasis (FDR = 0.00016, 23 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14018.1 (NDUFA10, MT-ND4, MT-ND5, NDUFS1, NDUFV1; 5/48); huMAP3_06397.1 (NDUFA10, MT-ND4, MT-ND5, NDUFS1, NDUFV1; 5/49); huMAP3_09982.1 (NDUFA10, MT-ND4, MT-ND5, NDUFS1, NDUFV1; 5/49); huMAP3_09567.1 (NDUFA10, MT-ND4, MT-ND5, NDUFS1, NDUFV1; 5/52); huMAP3_14878.1 (NDUFA10, MT-ND4, MT-ND5, NDUFS1, NDUFV1; 5/53); huMAP3_02819.1 (NDUFA10, MT-ND5, NDUFS1, NDUFV1; 4/34); huMAP3_12248.1 (DLAT, DBT, BCKDHB; 3/22); huMAP3_08132.1 (MT-ND4, MT-ND5, NDUFV1; 3/24); huMAP3_08580.1 (ACADVL, DHRS4; 2/2); huMAP3_02431.1 (ACADVL, DHRS4; 2/3); huMAP3_11915.1 (ACADVL, DHRS4; 2/3); huMAP3_10506.1 (ACADVL, DHRS4; 2/4); huMAP3_12388.1 (ETFA, NNT; 2/7); huMAP3_07653.1 (NDUFA10, NDUFS1; 2/7)

### Novelty

The module should not be claimed as a wholly new mitochondrial pathway. Its central biology is well established by the global GO and KEGG terms, the dense STRING relationships, the hu.MAP complex memberships, and the extensive gene-specific literature. Nevertheless, the specific conserved co-abundance module shared by heart and stem cells may be a new systems-level observation. Its potential novelty lies in the cross-tissue co-regulation and in the particular combination of respiratory-chain, fuel-oxidation, redox, and muscle-structural genes. Absence of some genes from STRING or hu.MAP does not establish novelty, and the biological interpretation should remain that of a potentially novel co-abundance pattern built largely from known mitochondrial components. Replication in independent heart and stem-cell datasets, control for cell composition, and comparison with published tissue modules would be needed to establish whether the configuration itself is genuinely new.

**Hypothesis.** Mechanistic hypothesis: a conserved program that maintains mitochondrial substrate oxidation and redox capacity in metabolically demanding or differentiating cells coordinates fatty-acid and branched-chain amino-acid entry, pyruvate and tricarboxylic-acid-cycle flux, electron transfer through respiratory complexes, and NADPH-dependent protection from oxidative stress. NNT could couple respiratory proton-gradient activity to NADPH production, while SDHA, NDUFS1, NDUFA10, NDUFV1, and the mitochondrial-encoded subunits could support electron flow. In heart-like cells, DSP may connect this energetic state to structural integrity and cardiomyocyte organization. This is a hypothesis rather than proof of direct regulatory control: co-abundance can arise from shared cell state, mitochondrial content, differentiation, or tissue composition. A useful test would combine perturbation of selected metabolic genes with measurements of respiratory flux, redox state, substrate use, and cardiomyocyte or stem-cell differentiation.

### Important genes

#### SDHA

- **Related proteins** (co-abundance neighbors): COQ8A (0.89), ETFDH (0.88), ALDH2 (0.88), COQ9 (0.87), SLC25A12 (0.84), SUCLG1 (0.83), ALDH5A1 (0.83), SUCLG2 (0.82), ACO2 (0.81); STRING partners: ACAT1 (0.762), ACO2 (0.975), DBT (0.714), DLAT (0.852), ETFA (0.706), GOT2 (0.981), IDH2 (0.869), MT-ND4 (0.922), MT-ND5 (0.881), NDUFA10 (0.793), NDUFS1 (0.995), NDUFV1 (0.999), SUCLA2 (0.998), SUCLG1 (0.999), SUCLG2 (0.997)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate dehydrogenase complex flavoprotein subunit A. This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identi…
- **Diseases (Open Targets)**: mitochondrial complex II deficiency, nuclear type 1 (0.813); pheochromocytoma/paraganglioma syndrome 5 (0.790); dilated cardiomyopathy 1GG (0.768); neurodegeneration with ataxia and late-onset optic atrophy (0.761); gastrointestinal stromal tumor (0.743)
- **Europe PMC papers**: 12756
- **Why important**: SDHA is one of the most connected genes in the module and links the tricarboxylic acid cycle to respiratory-chain activity. It is present across the primary metabolic, mitochondrial, respiration, TCA-cycle, and electron-transport annotations (17 globally significant GO/KEGG terms, q_global 3.95e-06–0.0388; see the table), has extensive STRING connections to both cycle enzymes and respiratory components, and is detected in heart with heart- and skeletal-muscle enhancement in HPA. Its established role as the catalytic subunit of succinate dehydrogenase, together with associations with respiratory-chain deficiency, cardiomyopathy, and other disease, makes it a strong biochemical anchor for the module.
- **Conclusion**: Established evidence supports SDHA as a central respiratory and TCA-cycle component of this module. The co-abundance data are consistent with coordinated control of succinate oxidation and electron transport. It is not established that SDHA regulates the other module genes; that possibility remains a hypothesis.

#### NDUFS1

- **Related proteins** (co-abundance neighbors): COQ9 (0.89), COQ8A (0.88), ETFDH (0.83), ALDH5A1 (0.83); STRING partners: ACO2 (0.865), DLAT (0.773), MT-ND4 (0.999), MT-ND5 (0.999), NDUFA10 (0.999), NDUFV1 (0.999), SDHA (0.995), SUCLA2 (0.777), SUCLG1 (0.752), SUCLG2 (0.728)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1, huMAP3_02819.1, huMAP3_07653.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S1. The protein encoded by this gene belongs to the complex I 75 kDa subunit family. Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Thi…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 5 (0.810); mitochondrial complex I deficiency (0.647); type 2 diabetes mellitus (0.608); Parkinson disease (0.603); diabetes mellitus (0.580)
- **Europe PMC papers**: 2567
- **Why important**: NDUFS1 is a core complex-I subunit and one of the module genes repeatedly represented in hu.MAP complex-I assemblies (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1) (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_07653.1). It is strongly connected in STRING to MT-ND4, MT-ND5, NDUFA10, NDUFV1, SDHA, and TCA-linked genes, and it contributes to the global respiration and electron-transport evidence (17 globally significant GO/KEGG terms, q_global 3.95e-06–0.0388; see the table). HPA shows heart- and skeletal-muscle enhancement and mitochondrial localization. Its established role in NADH-to-ubiquinone electron transfer, together with complex-I deficiency and neurological disease associations, gives it high mechanistic importance.
- **Conclusion**: Established evidence identifies NDUFS1 as a respiratory-chain core component that helps explain the module's electron-transport signal and its heart relevance. The module supports coordinated abundance of complex-I machinery, but does not by itself demonstrate altered complex-I activity or a causal disease mechanism.

#### ETFDH

- **Related proteins** (co-abundance neighbors): SUCLA2 (0.89), SDHA (0.88), MT-ND4 (0.86), ALDH2 (0.85), DHRS4 (0.85), NDUFV1 (0.84), NDUFS1 (0.83), NNT (0.83), ENO3 (0.82); STRING partners: ACADVL (0.817), COQ9 (0.801), ETFA (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein dehydrogenase. This gene encodes a component of the electron-transfer system in mitochondria and is essential for electron transfer from a number of mitochondrial flavin-containing dehydrogenases to the main respiratory chain. Mutations in this gene are associated with glutaric acidemia. Alternatively spliced transcript variants that encode distinct isoforms have been observed. [provided by RefSeq, Aug 2013].
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.845); glutaric acidemia IIc (0.704); glutaric aciduria (0.670); hereditary disease (0.523); Abnormality of metabolism/homeostasis (0.407)
- **Europe PMC papers**: 1273
- **Why important**: ETFDH occupies a highly connected position between substrate oxidation and the respiratory chain. It links the module to ACADVL and ETFA, appears in the global electron-transport and respiration terms (8 globally significant GO/KEGG terms, q_global 3.95e-06–0.0388; see the table), and has extensive STRING support for metabolic and mitochondrial relationships. HPA places it in mitochondria, detects it in heart, and shows enhancement in liver and tongue with myonuclear association. Its established function is electron transfer from multiple flavin dehydrogenases to the respiratory chain, and its disease associations include multiple acyl-CoA dehydrogenase deficiency and glutaric acidemia.
- **Conclusion**: Established evidence supports ETFDH as a bridge between fatty-acid and other flavin-dependent substrate oxidation and respiratory electron transfer. Its position makes it a plausible integrator of the module, but a specific regulatory or rate-limiting role is not established by co-abundance alone.

#### NNT

- **Related proteins** (co-abundance neighbors): FLNC (0.90), ACADVL (0.88), CRYM (0.88), NDUFA10 (0.88), ALDH2 (0.87), ETFA (0.86), ETFDH (0.83), IDH2 (0.80); STRING partners: IDH2 (0.898)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_12388.1
- **Function (MyGene.info)**: nicotinamide nucleotide transhydrogenase. This gene encodes an integral protein of the inner mitochondrial membrane. The enzyme couples hydride transfer between NAD(H) and NADP(+) to proton translocation across the inner mitochondrial membrane. Under most physiological conditions, the enzyme uses energy from the mitochondrial proton gradient to produce high concentrations of NADPH. The resulting NADPH is used for biosynthesis and in free …
- **Diseases (Open Targets)**: familial glucocorticoid deficiency (0.638); neurodegenerative disease (0.497); hereditary disease (0.453); atypical hemolytic-uremic syndrome with DGKE deficiency (0.416); Abnormality of the skeletal system (0.396)
- **Europe PMC papers**: 6111
- **Why important**: NNT connects the respiratory and metabolic portions of the network and is linked to IDH2, ACADVL, ETFA, ETFDH, and respiratory components. It contributes to the global energy, respiration, metabolic, and redox-related annotations (9 globally significant GO/KEGG terms, q_global 3.95e-06–0.0363; see the table), has a hu.MAP association with the electron-transfer flavoprotein-related complex (hu.MAP huMAP3_12388.1), and is detected in heart with cardiomyocyte and muscle-associated HPA evidence. Its established function couples proton translocation to NADPH generation, with NADPH supporting biosynthesis and free-radical detoxification. This gives it a distinct redox role not captured by respiratory-chain subunits alone.
- **Conclusion**: Established evidence supports NNT as a candidate redox-balancing component that could link respiratory activity to protection from oxidative stress. The module is consistent with coordinated redox and energy metabolism, but does not establish that NNT activity is the driver of the shared heart-stem-cell state.

#### DSP

- **Related proteins** (co-abundance neighbors): COQ9 (0.93), COQ8A (0.93), ALDH5A1 (0.91), ITGA7 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cell Junctions; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: desmoplakin. This gene encodes a protein that anchors intermediate filaments to desmosomal plaques and forms an obligate component of functional desmosomes. Mutations in this gene are the cause of several cardiomyopathies and keratodermas, including skin fragility-woolly hair syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016].
- **Diseases (Open Targets)**: arrhythmogenic cardiomyopathy with wooly hair and keratoderma (0.841); arrhythmogenic right ventricular dysplasia 8 (0.812); arrhythmogenic right ventricular cardiomyopathy (0.760); lethal acantholytic epidermolysis bullosa (0.745); cardiomyopathy, dilated, with wooly hair, keratoderma, and tooth agenesis (0.741)
- **Europe PMC papers**: 17350
- **Why important**: DSP is important because it provides a non-mitochondrial, structural connection within an otherwise strongly metabolic module. It is linked in the module network to COQ9, COQ8A, ALDH5A1, and ITGA7, has supplementary disease-related STRING support (4 supplementary STRING terms; within-query FDR 0.0001–0.00016), and is detected in heart. Its established function is anchoring intermediate filaments at desmosomes, and its disease associations include several cardiomyopathies and skin-fragility disorders. Although it lacks a primary GO or KEGG term in this module, its heart disease relevance and structural role make it valuable for interpreting the heart component.
- **Conclusion**: Established evidence supports DSP as a cardiac structural gene that may explain why the metabolic module is relevant to heart tissue and cardiomyopathy. Its connection to mitochondrial genes in this co-abundance network is suggestive, not proof of a direct metabolic function or physical interaction.

## Module 3

**Tissue pair**: heart and stem_cells  
**Genes (13)**: ABLIM1, AUH, CAVIN1, CAVIN2, ECI2, EML2, DGLUCY, NDUFA6, PDHX, OPA1, PDK2, PDP1, PLEC

### Function

The module is best interpreted as a coordinated mitochondrial energy and metabolic program, with a particularly coherent pyruvate dehydrogenase component. PDHX, PDK2, and PDP1 connect the pyruvate dehydrogenase complex with its inhibitory kinase and activating phosphatase, while ECI2, AUH, and NDUFA6 support fatty-acid metabolism, amino-acid metabolism, and respiratory-chain function. OPA1 adds mitochondrial organization, and ABLIM1, PLEC, CAVIN1, and CAVIN2 provide cytoskeletal or membrane context. No GO or KEGG term passed global correction, so this functional interpretation is based on the individual gene annotations, network structure, STRING evidence, hu.MAP evidence, and tissue context rather than on significant enrichment. The absence of a globally enriched term does not invalidate the module.

**Cell composition.** The module is not dominated by secreted or plasma proteins: HPA reports no secreted genes. Most genes show low immune-cell specificity, and only a limited subset is enriched in blood-cell populations, including CAVIN2 in platelet and megakaryocyte-related profiles and selected immune-cell associations for ABLIM1 and DGLUCY. The module is therefore not best explained as a plasma-protein or broad blood-contamination module. Its composition instead favors intracellular, mitochondrial, cytoskeletal, and membrane proteins. HPA supports a heart-relevant interpretation because nearly all genes with available heart protein data are detected in heart muscle, while tissue-enhanced signals include skeletal muscle, tongue, liver, and adipose tissue. The cardiomyocyte-associated signals for ABLIM1, PDP1, and DGLUCY are compatible with a metabolically active cardiac cell program, although shared cell types and sample composition remain possible explanations for part of the co-abundance pattern. HPA has no matching stem-cell tissue for protein detection, so protein-level support in stem cells cannot be assessed from this fact sheet.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a small but biologically coherent set of high-confidence relationships. The PDHX–PDK2 and PDHX–PDP1 links directly support the pyruvate dehydrogenase regulatory interpretation, while CAVIN1–CAVIN2 supports a caveolar or plasma-membrane submodule. Most module pairs do not have high-confidence STRING links, indicating that the co-abundance structure is broader than the currently catalogued direct interaction network. hu.MAP independently places PDHX and PDK2 together in multiple complexes, with the surrounding members repeatedly including core pyruvate dehydrogenase components and regulatory PDK proteins; this is strong evidence that this part of the module reflects a known biochemical complex rather than a coincidental association. The remaining module genes have no listed hu.MAP complexes or STRING partners in the supplied evidence, so their connections to the metabolic core should be treated as co-abundance relationships rather than established physical interactions.

**STRING interactions (score >= 0.7)**: 3 of 78 gene pairs: CAVIN1–CAVIN2 (0.728); PDHX–PDK2 (0.946); PDHX–PDP1 (0.965)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04919.1 (PDHX, PDK2; 2/7); huMAP3_08216.1 (PDHX, PDK2; 2/8); huMAP3_07514.1 (PDHX, PDK2; 2/9); huMAP3_09761.1 (PDHX, PDK2; 2/10); huMAP3_10899.1 (PDHX, PDK2; 2/10); huMAP3_10412.1 (PDHX, PDK2; 2/12); huMAP3_14339.1 (PDHX, PDK2; 2/13); huMAP3_11877.1 (PDHX, PDK2; 2/14); huMAP3_14864.1 (PDHX, PDK2; 2/14); huMAP3_12248.1 (PDHX, PDK2; 2/22)

### Novelty

The module should not be called a wholly new molecular complex. The PDHX–PDK2–PDP1 relationships and the PDHX–PDK2 hu.MAP membership are established, and the CAVIN1–CAVIN2 relationship is also represented in STRING. The potentially novel aspect is the cross-context co-abundance of this established mitochondrial regulatory core with cytoskeletal, caveolar, mitochondrial-dynamics, fatty-acid, amino-acid, and respiratory-chain genes in heart and stem-cell samples. However, absence of the broader module from STRING or hu.MAP alone does not establish novelty. A defensible conclusion is that this is a potentially new tissue-pair co-abundance configuration built partly from known interactions, requiring replication in independent cohorts and comparison with existing heart, stem-cell, and metabolic co-expression studies.

**Hypothesis.** Hypothesis: the module may represent coordinated control of mitochondrial fuel selection and pyruvate oxidation together with structural adaptation of metabolically active cells. In this model, PDHX provides the pyruvate dehydrogenase scaffold, PDK2 restrains pyruvate entry into acetyl-CoA production, and PDP1 reverses that inhibition; ECI2 and AUH could reflect complementary lipid and branched-chain substrate use, while NDUFA6 and OPA1 support respiratory capacity and mitochondrial organization. ABLIM1 and PLEC could connect metabolic organelles to the cytoskeleton, and CAVIN1 with CAVIN2 could mark membrane-caveolar organization. The shared heart and stem-cell signal may therefore reflect a common requirement for flexible mitochondrial metabolism and cell architecture, rather than one fully assembled physical complex. This remains a hypothesis because the global enrichment analysis was negative and most proposed links lack direct interaction evidence.

### Important genes

#### PDHX

- **Related proteins** (co-abundance neighbors): PDK2 (0.84), EML2 (0.83), ABLIM1 (0.83), DGLUCY (0.82); STRING partners: PDK2 (0.946), PDP1 (0.965)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_04919.1, huMAP3_08216.1, huMAP3_07514.1, huMAP3_09761.1, huMAP3_10899.1, huMAP3_10412.1, huMAP3_14339.1, huMAP3_11877.1, huMAP3_14864.1, huMAP3_12248.1
- **Function (MyGene.info)**: pyruvate dehydrogenase complex component X. The pyruvate dehydrogenase (PDH) complex is located in the mitochondrial matrix and catalyzes the conversion of pyruvate to acetyl coenzyme A. The PDH complex thereby links glycolysis to Krebs cycle. The PDH complex contains three catalytic subunits, E1, E2, and E3, two regulatory subunits, E1 kinase and E1 phosphatase, and a non-catalytic subunit, E3 binding protein (E3BP). This gene encodes the …
- **Diseases (Open Targets)**: pyruvate dehydrogenase E3-binding protein deficiency (0.793); hereditary disease (0.453); mitochondrial disease (0.445); Leigh syndrome (0.371); ovarian dysfunction (0.269)
- **Europe PMC papers**: 976
- **Why important**: PDHX is a central network connector and the defining scaffold-related component of the pyruvate dehydrogenase interpretation. It has direct STRING relationships with PDK2 and PDP1 and occurs with PDK2 across the hu.MAP complex entries C1 through C10. Its annotation places it in the mitochondrial pyruvate-to-acetyl-CoA reaction, and its disease associations include pyruvate dehydrogenase E3-binding protein deficiency and mitochondrial disease. Its literature volume is substantial, supporting a well-established biological role.
- **Conclusion**: Established evidence supports PDHX as the metabolic anchor of the module and as part of a known pyruvate dehydrogenase complex context. The hypothesis that PDHX coordinates the other module branches is plausible from its network position but is not established as a direct physical mechanism.

#### PDK2

- **Related proteins** (co-abundance neighbors): PDHX (0.84), NDUFA6 (0.81); STRING partners: PDHX (0.946)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_04919.1, huMAP3_08216.1, huMAP3_07514.1, huMAP3_09761.1, huMAP3_10899.1, huMAP3_10412.1, huMAP3_14339.1, huMAP3_11877.1, huMAP3_14864.1, huMAP3_12248.1
- **Function (MyGene.info)**: pyruvate dehydrogenase kinase 2. This gene encodes a member of the pyruvate dehydrogenase kinase family. The encoded protein phosphorylates pyruvate dehydrogenase, down-regulating the activity of the mitochondrial pyruvate dehydrogenase complex. Overexpression of this gene may play a role in both cancer and diabetes. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided b…
- **Diseases (Open Targets)**: Congenital lactic acidosis (0.259); type 2 diabetes mellitus (0.136); hepatocellular carcinoma (0.109); neoplasm (0.084); Thomsen and Becker disease (0.080)
- **Europe PMC papers**: 2633
- **Why important**: PDK2 is directly connected to PDHX in STRING and repeatedly co-occurs with PDHX in hu.MAP complexes C1 through C10. It regulates pyruvate dehydrogenase by phosphorylation and thereby controls the balance between glycolytic carbon entry and mitochondrial acetyl-CoA production. HPA shows tissue enhancement in skeletal muscle and tongue and protein detection in heart, while disease associations include congenital lactic acidosis and metabolic disease. It also has the largest literature volume among the module’s central regulatory genes.
- **Conclusion**: Established evidence supports PDK2 as a key negative regulator of pyruvate oxidation within the module. Its proposed role in coordinating broader fatty-acid, cytoskeletal, or membrane signals is a hypothesis based on co-abundance and must not be treated as demonstrated interaction.

#### PDP1

- **Related proteins** (co-abundance neighbors): ABLIM1 (0.86), PLEC (0.85); STRING partners: PDHX (0.965)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyruvate dehydrogenase phosphatase catalytic subunit 1. Pyruvate dehydrogenase (E1) is one of the three components (E1, E2, and E3) of the large pyruvate dehydrogenase complex. Pyruvate dehydrogenase kinases catalyze phosphorylation of serine residues of E1 to inactivate the E1 component and inhibit the complex. Pyruvate dehydrogenase phosphatases catalyze the dephosphorylation and activation of the E1 component to reverse the effects of pyruvate dehyd…
- **Diseases (Open Targets)**: pyruvate dehydrogenase phosphatase deficiency (0.775); COVID-19 (0.305); neurodegenerative disease (0.270); alcohol drinking (0.197); multinodular goiter (0.194)
- **Europe PMC papers**: 1532
- **Why important**: PDP1 is the catalytic phosphatase that activates pyruvate dehydrogenase by reversing kinase-mediated inhibition. It has a high-confidence STRING relationship with PDHX, connects to ABLIM1 in the module graph, shows cardiomyocyte-associated HPA expression, and is detected in heart. Its disease associations include pyruvate dehydrogenase phosphatase deficiency, and it has a substantial literature base.
- **Conclusion**: Established evidence supports PDP1 as the counter-regulatory partner to PDK2 in controlling pyruvate dehydrogenase activity. The connection to ABLIM1 and the wider module is an association in this dataset, not proof that cytoskeletal organization directly regulates PDP1.

#### OPA1

- **Related proteins** (co-abundance neighbors): EML2 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OPA1 mitochondrial dynamin like GTPase. The protein encoded by this gene is a nuclear-encoded mitochondrial protein with similarity to dynamin-related GTPases. The encoded protein localizes to the inner mitochondrial membrane and helps regulate mitochondrial stability and energy output. This protein also sequesters cytochrome c. Mutations in this gene have been associated with optic atrophy type 1, which is a dominantly inherited optic …
- **Diseases (Open Targets)**: autosomal dominant optic atrophy, classic form (0.846); Behr syndrome (0.812); optic atrophy with or without deafness, ophthalmoplegia, myopathy, ataxia, and neuropathy (0.766); mitochondrial DNA depletion syndrome 14B (cardioencephalomyopathic type) (0.745); optic atrophy (0.653)
- **Europe PMC papers**: 12169
- **Why important**: OPA1 links the metabolic interpretation to mitochondrial architecture. It is annotated for inner-mitochondrial-membrane organization, mitochondrial fusion, and mitochondrial stability, and it is associated with optic atrophy and cardioencephalomyopathic mitochondrial disease. Its literature volume is very large, making its function particularly well established even though it has only one listed module edge.
- **Conclusion**: Established evidence supports OPA1 as a mitochondrial-dynamics and organelle-maintenance gene. Its placement beside EML2 in the module suggests a possible structural or organelle-organization branch, but the module does not establish a direct connection between OPA1 and pyruvate dehydrogenase regulation.

#### ABLIM1

- **Related proteins** (co-abundance neighbors): ECI2 (0.88), PDP1 (0.86), CAVIN2 (0.85), AUH (0.85), PDHX (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: actin binding LIM protein 1. This gene encodes a LIM zinc-binding domain-containing protein that binds to actin filaments and mediates interactions between actin and cytoplasmic targets. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jun 2017].
- **Diseases (Open Targets)**: atrial fibrillation (0.464); diabetic ketoacidosis (0.269); preeclampsia (0.256); tooth disorder (0.244); lacrimal apparatus disorder (0.244)
- **Europe PMC papers**: 832
- **Why important**: ABLIM1 has the strongest network position in the module and connects metabolic genes, membrane-associated genes, and cytoskeletal context through several neighbors. It binds actin filaments and is annotated for cytoskeleton organization and cell morphogenesis. HPA reports cardiomyocyte-associated expression and heart protein detection, and its disease associations include atrial fibrillation. Its literature volume is moderate to substantial relative to the less characterized module members.
- **Conclusion**: Established evidence supports ABLIM1 as a cytoskeletal organizer with heart relevance. Its central position makes it an important candidate for linking cellular architecture to metabolic co-abundance, but that bridging role is a hypothesis rather than a demonstrated biochemical function in this module.

## Module 4

**Tissue pair**: heart and stem_cells  
**Genes (42)**: ACTN1, ALDH7A1, ANXA5, ATP1A1, MTHFD1, CKAP4, VCAN, DHX9, DPYSL2, DNM2, EIF3C, EZR, FABP5, FKBP3, FLNA, GANAB, SHMT2, IDH1, EIF4A2, LANCL1, LGALS3, LMNB2, MATR3, NAGK, PLS3, PSMC2, PSMB3, PSMD13, ATIC, RNH1, RTN4, SEPTIN2, SEPTIN7, SEPTIN9, SERPINH1, SUN2, RARS1, CCT5, TGM2, VIM, WDR1, XRCC6

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent; therefore, no statistically established pathway label should be assigned. The network nevertheless suggests a mixed cellular-maintenance program involving cytoskeletal organization, membrane and nuclear architecture, protein quality control, translation, and intermediary metabolism. The clearest subnetworks are the septin group containing SEPTIN2, SEPTIN7, and SEPTIN9 (hu.MAP huMAP3_02362.1), the proteasome-related group containing PSMB3, PSMC2, and PSMD13 (hu.MAP huMAP3_09656.1)(hu.MAP huMAP3_13725.1)(hu.MAP huMAP3_05064.1), and smaller neighborhoods involving actin-associated proteins, folate and purine metabolism, translation initiation, and endoplasmic-reticulum protein folding. The evidence supports a broad structural and homeostatic interpretation rather than a single canonical process.

**Cell composition.** The module is not dominated by plasma or secreted proteins. A minority of genes are secreted, including LGALS3 and VCAN, which are secreted to blood, and TGM2, which is secreted to extracellular matrix. Most genes have low tissue specificity or broad distributions, although many are cell-type enhanced. Recurrent tissue associations include blood vessel and liver, with additional associations to brain, intestine, and smooth muscle. Immune-cell specificity is generally low, although a subset is enhanced in monocyte, dendritic-cell, basophil, platelet, or related populations. HPA detects protein for many module genes in heart, while there is no matching HPA tissue for stem cells. The pattern is therefore compatible with a broadly expressed structural and housekeeping component that may be influenced by vascular, stromal, epithelial, or shared cell populations. Blood or contaminating-cell effects cannot be excluded, particularly for LGALS3, VCAN, ACTN1, and PLS3, but the module is not primarily a blood-cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports several known molecular relationships. ATIC with MTHFD1 and SHMT2 forms a linked folate, one-carbon, and purine-metabolism neighborhood. PSMB3, PSMC2, and PSMD13 form a proteasome-related neighborhood. SEPTIN2, SEPTIN7, and SEPTIN9 form a strong septin interaction group. Additional known links connect FLNA with ACTN1, EZR, SEPTIN9, and WDR1; DHX9 with MATR3 and XRCC6; EIF3C with EIF4A2; and LGALS3 with VIM. hu.MAP independently supports the septin assembly (hu.MAP huMAP3_02362.1), proteasome assemblies (hu.MAP huMAP3_09656.1)(hu.MAP huMAP3_13725.1)(hu.MAP huMAP3_05064.1), IDH1 with PLS3 (hu.MAP huMAP3_02650.1)(hu.MAP huMAP3_10900.1), MTHFD1 with ATIC (hu.MAP huMAP3_12823.1), PLS3 with EZR (hu.MAP huMAP3_10281.1), EIF3C with EIF4A2 (hu.MAP huMAP3_13175.1)(hu.MAP huMAP3_11246.1), WDR1 with ACTN1 (hu.MAP huMAP3_09165.1), PLS3 with ATIC (hu.MAP huMAP3_14442.1), and SERPINH1 with GANAB (hu.MAP huMAP3_09327.1). These findings show that portions of the co-abundance module correspond to established complexes or biochemical neighborhoods. Many module edges lack STRING or hu.MAP support, so the co-abundance pattern is broader than a single physical complex and may reflect coordinated expression, shared cell composition, or indirect cellular coupling.

**STRING interactions (score >= 0.7)**: 17 of 861 gene pairs: ACTN1–FLNA (0.716); ATIC–MTHFD1 (0.998); ATIC–SHMT2 (0.995); DHX9–MATR3 (0.786); DHX9–XRCC6 (0.819); EIF3C–EIF4A2 (0.928); EZR–FLNA (0.761); FLNA–SEPTIN9 (0.707); FLNA–WDR1 (0.874); LGALS3–VIM (0.778); MTHFD1–SHMT2 (0.996); PSMB3–PSMC2 (0.999); PSMB3–PSMD13 (0.999); PSMC2–PSMD13 (0.999); SEPTIN2–SEPTIN7 (0.999); SEPTIN2–SEPTIN9 (0.997); SEPTIN7–SEPTIN9 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02362.1 (SEPTIN2, SEPTIN7, SEPTIN9; 3/14); huMAP3_09656.1 (PSMC2, PSMB3, PSMD13; 3/64); huMAP3_13725.1 (PSMC2, PSMB3, PSMD13; 3/69); huMAP3_02650.1 (IDH1, PLS3; 2/2); huMAP3_10900.1 (IDH1, PLS3; 2/6); huMAP3_12823.1 (MTHFD1, ATIC; 2/7); huMAP3_10281.1 (PLS3, EZR; 2/9); huMAP3_13175.1 (EIF4A2, EIF3C; 2/20); huMAP3_11246.1 (EIF4A2, EIF3C; 2/24); huMAP3_05064.1 (PSMC2, PSMD13; 2/31); huMAP3_09165.1 (WDR1, ACTN1; 2/39); huMAP3_14442.1 (PLS3, ATIC; 2/57); huMAP3_09327.1 (SERPINH1, GANAB; 2/93)

### Novelty

This is a potentially interesting conserved co-abundance pattern, but it cannot be called a new molecular complex or a newly discovered pathway. Several subnetworks are already established in STRING and hu.MAP, especially the septin, proteasome, cytoskeletal, translation-initiation, and metabolic relationships. The possible novelty lies in their coordinated co-abundance across heart and stem-cell samples and in the particular combination of structural, proteostasis, metabolic, and extracellular-matrix-associated genes. Absence of an edge from STRING or hu.MAP does not prove novelty because those resources emphasize supported physical and functional relationships rather than every tissue-level co-expression relationship. Independent replication, adjustment for cell composition, and perturbation experiments would be needed before claiming a new mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state requiring coordinated cytoskeletal remodeling, membrane and nuclear mechanics, protein folding and degradation, translation, and biosynthetic metabolism. The septin, plastin, filamin, vimentin, ezrin, and WDR1-related components could organize cell shape, adhesion, and intracellular architecture. The proteasome and endoplasmic-reticulum components could maintain protein quality, while the ATIC, MTHFD1, and SHMT2 neighborhood could support nucleotide and one-carbon metabolism during growth or remodeling. LGALS3, VCAN, and TGM2 may connect this intracellular program to extracellular matrix and vascular or stromal contexts. This model is provisional because the absence of globally significant GO or KEGG enrichment and the heterogeneous HPA cell-type pattern mean that shared cell composition or sample handling could contribute substantially.

### Important genes

#### PLS3

- **Related proteins** (co-abundance neighbors): SUN2 (0.90), WDR1 (0.87), PSMD13 (0.87), CKAP4 (0.86), SEPTIN2 (0.86), DPYSL2 (0.85), LGALS3 (0.85), ATIC (0.84), RTN4 (0.84), ANXA5 (0.82), IDH1 (0.81), XRCC6 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cytosol; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_02650.1, huMAP3_10900.1, huMAP3_10281.1, huMAP3_14442.1
- **Function (MyGene.info)**: plastin 3. Plastins are a family of actin-binding proteins that are conserved throughout eukaryote evolution and expressed in most tissues of higher eukaryotes. In humans, two ubiquitous plastin isoforms (L and T) have been identified. Plastin 1 (otherwise known as Fimbrin) is a third distinct plastin isoform which is specifically expressed at high levels in the small intestine. The L isoform is expressed on…
- **Diseases (Open Targets)**: X-linked osteoporosis with fractures (0.727); congenital diaphragmatic hernia (0.553); osteoporosis (0.477); hernia, anterior diaphragmatic (0.380); postmenopausal osteoporosis (0.341)
- **Europe PMC papers**: 1365
- **Why important**: PLS3 is the highest-connectivity hub and links cytoskeletal, septin, metabolic, proteasome-associated, and membrane-related neighborhoods. It is an actin-binding plastin involved in actin filament organization, is detected in heart, and has vascular and epithelial or immune-associated HPA patterns. It participates in multiple hu.MAP associations (hu.MAP huMAP3_02650.1)(hu.MAP huMAP3_10900.1)(hu.MAP huMAP3_10281.1)(hu.MAP huMAP3_14442.1), making it an integrator of the module. Its disease associations include skeletal and hernia-related disorders, and it has substantial literature.
- **Conclusion**: Established evidence supports PLS3 as a central actin-associated hub with broad cellular distribution and disease relevance. It is a plausible structural anchor of the module. It is not established that PLS3 drives the shared heart and stem-cell co-abundance pattern; that causal role remains a hypothesis.

#### SEPTIN2

- **Related proteins** (co-abundance neighbors): CKAP4 (0.94), DHX9 (0.91), FLNA (0.91), MATR3 (0.89), VIM (0.89), PLS3 (0.86), NAGK (0.85), EIF4A2 (0.85), SEPTIN9 (0.82), PSMD13 (0.80); STRING partners: SEPTIN7 (0.999), SEPTIN9 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Actin filaments; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_02362.1
- **Function (MyGene.info)**: septin 2. Enables identical protein binding activity. Predicted to be involved in several processes, including cilium assembly; regulation of exocytosis; and smoothened signaling pathway. Predicted to act upstream of or within regulation of L-glutamate import across plasma membrane and regulation of protein localization. Located in several cellular components, including cytoskeleton; photoreceptor connectin…
- **Diseases (Open Targets)**: hypothyroidism (0.239); squamous cell carcinoma (0.201); ischemic stroke (0.189); coronary artery disorder (0.181); skin cancer (0.181)
- **Europe PMC papers**: 281
- **Why important**: SEPTIN2 is a highly connected module member and belongs to the strongly supported septin neighborhood with SEPTIN7 and SEPTIN9 in STRING and hu.MAP (hu.MAP huMAP3_02362.1). Septins contribute to cytoskeleton organization, intracellular localization, cytokinesis, cilium assembly, and exocytosis. SEPTIN2 is broadly expressed, detected in heart, and connects within the module to cytoskeletal, nuclear, RNA-associated, and membrane-related genes.
- **Conclusion**: Established evidence supports SEPTIN2 as a structural component of a known septin assembly. Its co-abundance likely reports cytoskeletal or cellular-architecture state. A specific role in coordinating the heart and stem-cell module is plausible but not demonstrated.

#### LGALS3

- **Related proteins** (co-abundance neighbors): WDR1 (0.89), NAGK (0.88), CKAP4 (0.87), EIF4A2 (0.87), GANAB (0.85), ACTN1 (0.85), PLS3 (0.85), ALDH7A1 (0.84), LMNB2 (0.83), CCT5 (0.82); STRING partners: VIM (0.778)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm, Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galectin 3. This gene encodes a member of the galectin family of carbohydrate binding proteins. Members of this protein family have an affinity for beta-galactosides. The encoded protein is characterized by an N-terminal proline-rich tandem repeat domain and a single C-terminal carbohydrate recognition domain. This protein can self-associate through the N-terminal domain allowing it to bind to multivalent sac…
- **Diseases (Open Targets)**: melanoma (0.126); COVID-19 (0.123); neoplasm (0.120); hepatocellular carcinoma (0.117); cancer (0.117)
- **Europe PMC papers**: 13803
- **Why important**: LGALS3 is highly connected and links cytoskeletal and metabolic neighborhoods, with a STRING relationship to VIM. It encodes a beta-galactoside-binding protein with extracellular-matrix, cytoplasmic, and nuclear localization. HPA identifies it as secreted to blood, enhanced in intestine, and associated with monocyte, dendritic-cell, and regulatory T-cell populations. It has extensive literature and disease associations, making it an important biological and interpretive marker even though it is not part of a hu.MAP complex here.
- **Conclusion**: Established evidence supports LGALS3 as a multifunctional extracellular and intracellular regulator associated with matrix, immune, and stromal contexts. It could connect the module to vascular, stromal, or sample-composition effects. Its presence does not prove that inflammation or immune signaling is the primary module function.

#### VCAN

- **Related proteins** (co-abundance neighbors): EIF3C (0.90), ATP1A1 (0.85), RARS1 (0.85), SEPTIN7 (0.85), RTN4 (0.84), DNM2 (0.82), PSMB3 (0.81), PSMC2 (0.81), EIF4A2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles, Mid piece, Principal piece, End piece; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: versican. This gene is a member of the aggrecan/versican proteoglycan family. The protein encoded is a large chondroitin sulfate proteoglycan and is a major component of the extracellular matrix. This protein is involved in cell adhesion, proliferation, proliferation, migration and angiogenesis and plays a central role in tissue morphogenesis and maintenance. Mutations in this gene are the cause of Wagner s…
- **Diseases (Open Targets)**: Wagner disease (0.745); Abnormality of the skeletal system (0.581); diverticular disease (0.521); inherited retinal dystrophy (0.446); hereditary disease (0.417)
- **Europe PMC papers**: 7002
- **Why important**: VCAN is among the more connected genes and is a large extracellular-matrix proteoglycan involved in adhesion, migration, angiogenesis, and tissue morphogenesis. HPA associates it with blood vessels, fibroblast-like and stromal cell types, monocyte-related populations, and secretion to blood. It connects extracellular-matrix context with EIF3C, ATP1A1, RARS1, SEPTIN7, RTN4, DNM2, PSMB3, and PSMC2. It has substantial literature and a defined association with Wagner disease.
- **Conclusion**: Established evidence supports VCAN as an extracellular-matrix and vascular or stromal marker that may explain part of the shared tissue pattern. Its role as an organizer of the entire module is unproven, and its co-abundance may partly reflect shared cell types or extracellular material.

#### PSMD13

- **Related proteins** (co-abundance neighbors): PLS3 (0.87), WDR1 (0.86), EIF4A2 (0.85), ATIC (0.85), IDH1 (0.84), TGM2 (0.83), SEPTIN2 (0.80); STRING partners: PSMB3 (0.999), PSMC2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1, huMAP3_05064.1
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 connects the module to the proteasome-related neighborhood and has strong STRING links with PSMB3 and PSMC2. It participates in several hu.MAP proteasome assemblies (hu.MAP huMAP3_09656.1)(hu.MAP huMAP3_13725.1)(hu.MAP huMAP3_05064.1). Its established functions include proteasomal protein catabolism, oxidative-stress response, and cellular responses related to type one interferon. It is detected in heart and has disease associations involving plasma-cell malignancy, lymphoma, neurodegeneration, and infection.
- **Conclusion**: Established evidence supports PSMD13 as a proteasome component and marker of protein-quality-control capacity. Its co-abundance may indicate shared proteostasis requirements, but the module does not establish altered proteasome activity or a disease mechanism.

#### ATIC

- **Related proteins** (co-abundance neighbors): PSMD13 (0.85), PLS3 (0.84), DPYSL2 (0.83); STRING partners: MTHFD1 (0.998), SHMT2 (0.995)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_12823.1, huMAP3_14442.1
- **Function (MyGene.info)**: 5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase. This gene encodes a bifunctional protein that catalyzes the last two steps of the de novo purine biosynthetic pathway. The N-terminal domain has phosphoribosylaminoimidazolecarboxamide formyltransferase activity, and the C-terminal domain has IMP cyclohydrolase activity. A mutation in this gene results in AICA-ribosiduria. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: AICA-ribosiduria (0.708); cancer (0.571); Intellectual disability (0.463); lung adenocarcinoma (0.390); anaplastic large cell lymphoma (0.374)
- **Europe PMC papers**: 5200
- **Why important**: ATIC is a bifunctional enzyme catalyzing terminal steps of de novo purine biosynthesis. It has strong STRING support with MTHFD1 and SHMT2 and participates in hu.MAP associations (hu.MAP huMAP3_12823.1)(hu.MAP huMAP3_14442.1). Within the module it connects metabolic genes with PLS3, DPYSL2, and PSMD13. It is detected in heart, has a defined association with AICA-ribosiduria, and has substantial literature including cancer and developmental disease contexts.
- **Conclusion**: Established evidence supports ATIC as a biosynthetic enzyme embedded in a known metabolic neighborhood. It provides a plausible link between cellular growth or repair demands and structural machinery in the module. The data do not establish increased purine synthesis or a direct metabolic driver of the conserved co-abundance pattern.

## Module 5

**Tissue pair**: heart and stem_cells  
**Genes (21)**: AHNAK, AIMP2, ANXA4, ANXA6, BAG3, CAP2, CLTC, FN1, GBE1, GPD2, SLC2A1, ISOC1, ITGB1, CAMK2D, MCAM, BCKDHA, PALLD, PPP1CB, SEC22B, TLN1, TXNDC5

### Function

The most coherent interpretation is a cell adhesion, extracellular-matrix coupling, actin-cytoskeleton, and mechanotransduction module with a cardiac contractility component. The central network structure links CAP2 with ITGB1, MCAM, CAMK2D, and several cytoskeletal, membrane-trafficking, and metabolic proteins. The FN1–ITGB1–TLN1 connections support an integrin-based cell–matrix adhesion axis, while CAMK2D, AHNAK, PALLD, and CAP2 support calcium-responsive cytoskeletal and contractile regulation. GBE1, BCKDHA, GPD2, and SLC2A1 indicate that cellular energy handling may accompany this structural program. No GO or KEGG term passed global correction, so these annotations should be interpreted as convergent biological evidence rather than as a globally significant enrichment result. The module is therefore best described as a structural and signaling program associated with adhesion, force transmission, membrane organization, and energy support in heart and stem-cell samples.

**Cell composition.** This is not primarily a plasma-protein or blood-cell module. FN1 is secreted to blood, but the remainder of the module is predominantly intracellular, cytosolic, membrane-associated, or focal-adhesion associated. Most genes have low tissue specificity, with the remainder biased toward skeletal muscle, blood vessel, placenta, or related tissues. HPA single-cell annotations most often point to smooth-muscle cells and myonuclei, with additional signals in pericytes, cardiomyocytes, platelets, neutrophils, epithelial cells, and other cell types. Blood-cell specificity is generally low, although GPD2 and several other genes have immune-cell associations. Thus, the shared module may reflect a broadly expressed adhesion and contractile program, or a shared mesenchymal, vascular, smooth-muscle, or muscle-related cell population, rather than a heart-specific cardiomyocyte program. Heart protein detection supports relevance to heart tissue for many members, whereas the absence of a matching HPA stem-cell tissue category prevents a direct protein-level comparison for stem cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides strong support for a specific focal-adhesion subnetwork: FN1 is connected to ITGB1 and TLN1, ITGB1 is connected to TLN1 and MCAM, and TLN1 is connected to FN1 and ITGB1. These are established relationships and make the adhesion interpretation more credible. The co-abundance network also links CAP2 to ITGB1 and MCAM and links CAMK2D to CAP2, but those relationships are not supported by high-confidence STRING edges in the supplied results and should not be treated as established physical interactions. No STRING functional enrichment was reported. No hu.MAP complex contains multiple module members, so the module is not supported as a known multi-protein complex. Overall, STRING validates a compact adhesion core, while the broader module appears to combine known adhesion proteins with co-abundant signaling, cytoskeletal, metabolic, and trafficking proteins.

**STRING interactions (score >= 0.7)**: 4 of 210 gene pairs: FN1–ITGB1 (0.999); FN1–TLN1 (0.992); ITGB1–MCAM (0.82); ITGB1–TLN1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared heart–stem-cell co-abundance module may be a new systems-level observation, but the underlying biology is not wholly novel. Integrin–fibronectin–talin adhesion, actin organization, vascular repair, cardiac calcium signaling, glycogen metabolism, and muscle proteostasis are established biological themes. The potentially novel aspect is their joint co-abundance as a conserved module across these tissue groups, especially the connection of the CAP2-centered neighborhood with the established FN1–ITGB1–TLN1 adhesion axis and cardiac signaling genes. This claim remains provisional because the supplied evidence does not include independent replication, perturbation, cell-composition adjustment, or a direct comparison with previously published co-abundance modules. The absence of a hu.MAP complex or additional STRING relationships does not by itself establish novelty.

**Hypothesis.** Hypothesis: the module represents a conserved force-sensing and tissue-support program in which FN1 engages ITGB1, TLN1, and MCAM at adhesion sites; CAP2 and PALLD organize the associated actin cytoskeleton; and CAMK2D together with AHNAK links membrane or calcium signals to contractile and structural adaptation. GBE1, BCKDHA, GPD2, and SLC2A1 may provide metabolic support for cells experiencing contractile or adhesion-related demands, while SEC22B and CLTC may support membrane and vesicle remodeling. In heart, this could contribute to force transmission and remodeling; in stem-cell samples, it could mark a shared vascular, mesenchymal, smooth-muscle-like, or adhesion-competent state. This is a mechanistic model, not a demonstrated causal pathway.

### Important genes

#### ITGB1

- **Related proteins** (co-abundance neighbors): MCAM (0.87), TLN1 (0.86), CAP2 (0.86), SLC2A1 (0.85); STRING partners: FN1 (0.999), MCAM (0.82), TLN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is a central adhesion receptor in the module, connecting MCAM, TLN1, CAP2, and SLC2A1 in the co-abundance network. It is also the best-supported interaction hub in the STRING results because it connects to FN1, TLN1, and MCAM. Its established functions include cell adhesion, integrin signaling, angiogenesis, phagocytosis, and tissue repair. It has extensive disease and literature support, making it the strongest anchor for interpreting the module as an adhesion and mechanotransduction program.
- **Conclusion**: Established evidence supports ITGB1 as a core adhesion and signaling component. It is reasonable to hypothesize that ITGB1 organizes the module's extracellular-matrix and cytoskeletal behavior, but the co-abundance data do not prove that it regulates the other module members.

#### FN1

- **Related proteins** (co-abundance neighbors): TLN1 (0.87), CLTC (0.82); STRING partners: ITGB1 (0.999), TLN1 (0.992)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 provides the extracellular-matrix counterpart to ITGB1 and TLN1. It is connected to both proteins in STRING and is co-abundant with CLTC in the module. Its established roles include cell–matrix adhesion, cell migration, wound healing, embryogenesis, and vascular or tissue remodeling. It is the most extensively studied gene in the module and is secreted to blood, so it also raises the possibility that part of the signal reflects extracellular matrix or circulating protein exposure rather than a purely intracellular program.
- **Conclusion**: Established evidence identifies FN1 as a credible extracellular scaffold component of the module. The hypothesis that it helps transmit matrix-derived mechanical signals to the shared heart–stem-cell program is biologically plausible but not directly shown by this analysis.

#### TLN1

- **Related proteins** (co-abundance neighbors): FN1 (0.87), ITGB1 (0.86), AHNAK (0.82); STRING partners: FN1 (0.992), ITGB1 (0.999)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 is positioned between FN1 and ITGB1 in the known interaction network and is co-abundant with AHNAK. Its established functions include integrin activation, cell adhesion, actin-cytoskeleton organization, cell–cell junction assembly, and integrin-mediated signaling. Its focal-adhesion localization and associations with hypertrophic cardiomyopathy and developmental syndromes make it especially relevant to a module shared with heart tissue.
- **Conclusion**: Established evidence supports TLN1 as the intracellular linker that could couple integrin engagement to actin organization. A role as a mechanical signal integrator in the shared module is a hypothesis rather than a demonstrated causal conclusion.

#### CAMK2D

- **Related proteins** (co-abundance neighbors): CAP2 (0.90), PPP1CB (0.87), AHNAK (0.83), AIMP2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Primary cilium tip, Primary cilium transition zone, Principal piece; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium/calmodulin dependent protein kinase II delta. The product of this gene belongs to the serine/threonine protein kinase family and to the Ca(2+)/calmodulin-dependent protein kinase subfamily. Calcium signaling is crucial for several aspects of plasticity at glutamatergic synapses. In mammalian cells, the enzyme is composed of four different chains: alpha, beta, gamma, and delta. The product of this gene is a delta chain. Alternative splicing re…
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.632); atrial fibrillation (0.556); CAMK2D-related neurodevelopmental disorder and dilated cardiomyopathy (0.503); heart conduction disease (0.449); heart failure (0.438)
- **Europe PMC papers**: 2254
- **Why important**: CAMK2D connects to CAP2, PPP1CB, AHNAK, and AIMP2 and is tissue enhanced in heart muscle, with cell-type enhancement in cardiomyocytes and myonuclei. Its established functions include calcium-dependent protein phosphorylation and regulation of heart contraction and membrane depolarization. Its associations with atrial fibrillation, heart conduction disease, heart failure, and dilated cardiomyopathy provide strong disease relevance, while its literature base is substantial.
- **Conclusion**: Established evidence supports CAMK2D as the cardiac calcium-signaling component of the module. It may connect adhesion-associated mechanical inputs to contractile adaptation, but that cross-talk remains a hypothesis because the network is based on co-abundance.

#### CAP2

- **Related proteins** (co-abundance neighbors): CAMK2D (0.90), MCAM (0.87), ISOC1 (0.86), ITGB1 (0.86), SEC22B (0.84), ANXA4 (0.84), GPD2 (0.84), ANXA6 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Nucleoplasm, Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cyclase associated actin cytoskeleton regulatory protein 2. This gene was identified by its similarity to the gene for human adenylyl cyclase-associated protein. The function of the protein encoded by this gene is unknown. However, the protein appears to be able to interact with adenylyl cyclase-associated protein and actin. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: cardiomyopathy, dilated, 2I (0.639); hemorrhoid (0.403); familial isolated dilated cardiomyopathy (0.391); gastroduodenitis (0.320); pregnancy disorder (0.268)
- **Europe PMC papers**: 1667
- **Why important**: CAP2 has the strongest co-abundance connectivity in the module and links CAMK2D, MCAM, ITGB1, ISOC1, SEC22B, ANXA4, GPD2, and ANXA6. It is enhanced in skeletal muscle and myonuclei and is detected in heart. Its established annotations involve actin interaction, cytoskeleton organization, cell morphogenesis, polarity, and signal transduction. Although its functional literature is smaller than that of ITGB1 or FN1, its network position makes it a useful candidate coordinator of the module.
- **Conclusion**: Established evidence supports CAP2 as a cytoskeletal and signaling-associated protein with strong module-level connectivity. It is a compelling candidate for integrating adhesion, actin organization, and cardiac signaling, but its central regulatory role is a hypothesis requiring perturbation or independent interaction evidence.

## Module 6

**Tissue pair**: heart and stem_cells  
**Genes (8)**: ANK3, DCTN1, DHRS7, LMO7, MYL9, SVIL, TATDN1, TLN2

### Function

The module is most consistent with a coordinated cytoskeletal and membrane-organization program, with links to cell adhesion, contractility, specialized membrane domains, and intracellular transport. SVIL connects actin filaments with plasma membranes and is the most connected node in the co-abundance subgraph. TLN2 supports adhesion-related linkage between extracellular-matrix receptors and the actin cytoskeleton, while LMO7 is an actin-associated interaction scaffold enriched in heart muscle. MYL9 adds a contractile and stress-fiber component, and ANK3 supports membrane–spectrin/actin organization. DCTN1 contributes a microtubule-based transport and nuclear-positioning axis, with TATDN1 providing a nucleoplasmic DNA-metabolism association. DHRS7 contributes a possible metabolic component through its short-chain dehydrogenase/reductase annotation. No GO/KEGG term passed global correction: there are no globally significant GO/KEGG terms. There are also no supplementary STRING terms and no STRING functional-enrichment result. Thus, the functional interpretation is gene- and network-based rather than enrichment-validated.

**Cell composition.** The module is not composed of plasma or secreted proteins: the genes are intracellular or membrane-associated, and no gene is annotated as secreted. Its HPA profile is heterogeneous rather than uniformly heart-specific. Several genes show tissue enhancement in skeletal or heart muscle, blood vessel, intestine, or tongue, while others have low tissue specificity. Cell-type enhancement includes cardiomyocytes, myonuclei, smooth muscle cells, epithelial populations, and neutrophil-related populations. Immune-cell evidence is generally low or mixed, but SVIL, MYL9, and DHRS7 include neutrophil-related annotations, and MYL9 also includes eosinophil-related evidence. This pattern does not establish a blood-cell artifact, but it makes shared cell composition, vascular or smooth-muscle content, and broader cytoskeletal programs plausible contributors to the heart–stem-cell co-abundance signal. Heart protein detection is broadly supportive for most module members, whereas there is no matching HPA tissue category for stem_cells, so the stem-cell interpretation cannot be directly confirmed by the reported HPA protein evidence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship is reported among the module genes, and no hu.MAP complex contains multiple module members. Therefore, the co-abundance edges are not corroborated here as established physical interactions or as membership in a recognized multiprotein complex. The annotations nevertheless support biologically compatible neighborhoods: SVIL, TLN2, LMO7, MYL9, and ANK3 converge on actin, adhesion, contractility, and membrane organization, while DCTN1 and TATDN1 form a separate transport or nuclear-associated branch. The lack of STRING and hu.MAP support means the network should be interpreted primarily as coordinated abundance or shared cellular context, not as a demonstrated physical assembly.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a previously unreported co-abundance pattern, particularly because the module is shared between heart and stem_cells yet lacks a corresponding high-confidence STRING network or hu.MAP complex. However, absence from those resources does not demonstrate novelty: the component genes have established functions, substantial prior literature, and biologically related annotations. The defensible conclusion is that the cross-tissue co-abundance configuration is potentially novel, while the underlying cytoskeletal, adhesion, contractile, membrane, and transport biology is not new.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of structural and trafficking machinery in cells that maintain mechanically specialized membranes, actin-linked adhesion sites, and contractile or motile architecture. In heart, this could arise from cardiomyocyte, vascular, or smooth-muscle structural programs. In stem_cells, it could reflect a shared mesenchymal, contractile, adhesion-related, or differentiation-associated state, or shared cellular composition in the sampled material. SVIL, TLN2, LMO7, MYL9, and ANK3 could form a functional cytoskeletal–membrane axis, with DCTN1 linking that state to microtubule transport and nuclear positioning. This is a mechanistic proposal rather than a demonstrated interaction model and should be tested with cell-composition adjustment, independent cohorts, perturbation, and protein-level or imaging validation.

### Important genes

#### SVIL

- **Related proteins** (co-abundance neighbors): TLN2 (0.92), DHRS7 (0.91), LMO7 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: supervillin. This gene encodes a bipartite protein with distinct amino- and carboxy-terminal domains. The amino-terminus contains nuclear localization signals and the carboxy-terminus contains numerous consecutive sequences with extensive similarity to proteins in the gelsolin family of actin-binding proteins, which cap, nucleate, and/or sever actin filaments. The gene product is tightly associated with both a…
- **Diseases (Open Targets)**: myofibrillar myopathy 10 (0.634); neurodegenerative disease (0.402); aortic stenosis (0.376); sialolithiasis (0.323); biliary tract disorder (0.322)
- **Europe PMC papers**: 839
- **Why important**: SVIL is the central connector in the module and links actin filaments with plasma membranes. Its actin capping, severing, polymerization, cytokinesis, and skeletal-muscle annotations give the module a strong structural interpretation. HPA supports skeletal-muscle and tongue enrichment, heart protein detection, and localization at the plasma membrane. Its association with myofibrillar myopathy and aortic stenosis makes it relevant to cardiac and muscle biology, and its literature base is substantial.
- **Conclusion**: Established evidence supports SVIL as the best network anchor for an actin–membrane structural program. The hypothesis that it organizes the other module branches in heart or stem-cell states remains unproven because the co-abundance edges lack STRING or hu.MAP support.

#### MYL9

- **Related proteins** (co-abundance neighbors): DCTN1 (0.91), LMO7 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin light chain 9. Myosin, a structural component of muscle, consists of two heavy chains and four light chains. The protein encoded by this gene is a myosin light chain that may regulate muscle contraction by modulating the ATPase activity of myosin heads. The encoded protein binds calcium and is activated by myosin light chain kinase. Two transcript variants encoding different isoforms have been found for this gen…
- **Diseases (Open Targets)**: megacystis-microcolon-intestinal hypoperistalsis syndrome 4 (0.566); diabetic ketoacidosis (0.319); familial visceral myopathy (0.289); visceral myopathy 1 (0.288); Abnormality of the skeletal system (0.168)
- **Europe PMC papers**: 3103
- **Why important**: MYL9 connects the DCTN1 branch with LMO7 and contributes a contractile interpretation through calcium-regulated myosin activity, regulation of muscle contraction, vascular smooth-muscle contraction, myofibril assembly, stress-fiber assembly, and platelet aggregation. HPA links it to blood vessel and intestine tissues, several stromal or epithelial cell types, and eosinophil- and neutrophil-related populations. It has the strongest literature volume among the selected genes and disease associations involving visceral and skeletal abnormalities.
- **Conclusion**: Established evidence supports MYL9 as a contractile and stress-fiber component and as a possible marker of vascular, smooth-muscle, or mixed cellular content. Its position connecting contractile and transport-associated portions of the network suggests a bridging role, but a direct mechanistic connection to DCTN1 is only a hypothesis.

#### LMO7

- **Related proteins** (co-abundance neighbors): SVIL (0.86), MYL9 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LIM domain 7. This gene encodes a protein containing a calponin homology (CH) domain, a PDZ domain, and a LIM domain, and may be involved in protein-protein interactions. Several alternatively spliced transcript variants encoding different isoforms have been found for this gene, however, the full-length nature of some variants is not known. [provided by RefSeq, Jan 2009].
- **Diseases (Open Targets)**: cancer (0.473); neurodegenerative disease (0.436); open-angle glaucoma (0.395); presbycusis (0.377); glaucoma (0.362)
- **Europe PMC papers**: 1196
- **Why important**: LMO7 is directly connected to SVIL and MYL9 and is the module member with HPA tissue enhancement in heart muscle. Its calponin-homology, PDZ, and LIM domains are compatible with protein-interaction scaffolding, and its annotations include regulation of cell adhesion and signaling. Its actin-filament localization and disease associations involving cancer, neurodegeneration, glaucoma, and hearing provide additional biological relevance. The literature base is substantial.
- **Conclusion**: Established evidence supports LMO7 as a heart-associated actin-interaction scaffold that reinforces the adhesion and cytoskeletal interpretation. It is a plausible cardiac-context marker, but the module does not establish that LMO7 physically assembles with SVIL or MYL9.

#### DCTN1

- **Related proteins** (co-abundance neighbors): MYL9 (0.91), TATDN1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynactin subunit 1. This gene encodes the largest subunit of dynactin, a macromolecular complex consisting of 10 subunits ranging in size from 22 to 150 kD. Dynactin binds to both microtubules and cytoplasmic dynein. Dynactin is involved in a diverse array of cellular functions, including ER-to-Golgi transport, the centripetal movement of lysosomes and endosomes, spindle formation, chromosome movement, nuclear positi…
- **Diseases (Open Targets)**: Perry syndrome (0.798); amyotrophic lateral sclerosis (0.764); neuronopathy, distal hereditary motor, type 7B (0.743); cancer (0.547); neurodegenerative disease (0.530)
- **Europe PMC papers**: 1985
- **Why important**: DCTN1 is a prominent intracellular-transport component and connects MYL9 with TATDN1 in the module. Its established role as a dynactin subunit links cytoplasmic dynein to microtubule-based transport, organelle movement, spindle organization, nuclear positioning, and neuromuscular-junction development. HPA places it at microtubules and detects it in heart, while disease associations include Perry syndrome, amyotrophic lateral sclerosis, and hereditary neuronopathy. It has an extensive literature base.
- **Conclusion**: Established evidence supports DCTN1 as the module's microtubule-transport and positioning component. Its connection to the actin-contractile branch suggests coordinated cytoskeletal remodeling as a hypothesis, not an established molecular complex in this dataset.

#### ANK3

- **Related proteins** (co-abundance neighbors): TLN2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ankyrin 3. Ankyrins are a family of proteins that are believed to link the integral membrane proteins to the underlying spectrin-actin cytoskeleton and play key roles in activities such as cell motility, activation, proliferation, contact, and the maintenance of specialized membrane domains. Multiple isoforms of ankyrin with different affinities for various target proteins are expressed in a tissue-specific,…
- **Diseases (Open Targets)**: intellectual disability-hypotonia-spasticity-sleep disorder syndrome (0.726); bipolar disorder (0.536); hereditary disease (0.472); smoking initiation (0.411); smoking cessation (0.391)
- **Europe PMC papers**: 2941
- **Why important**: ANK3 is linked to TLN2 and encodes a membrane-organizing ankyrin that connects integral membrane proteins with the spectrin–actin cytoskeleton. Its annotations include plasma-membrane organization, cytoskeleton organization, signal transduction, axonogenesis, and neuromuscular-junction development. HPA detects the protein in heart and shows enhancement across neuronal, epithelial, and renal cell types. Its disease associations include a neurodevelopmental syndrome and bipolar disorder, and its literature base is extensive.
- **Conclusion**: Established evidence supports ANK3 as a membrane-domain organizer that broadens the module beyond contractile proteins. Its occurrence may indicate specialized membrane architecture or shared cytoskeletal state, but the module does not establish a direct TLN2–ANK3 protein complex.

## Module 7

**Tissue pair**: heart and stem_cells  
**Genes (13)**: APMAP, ASPH, BCAM, CAPN2, FLOT1, FECH, EPHX1, ILK, KANK2, MYO1C, PITRM1, SCCPDH, STOM

### Function

This is a heterogeneous membrane, adhesion, cytoskeletal, vesicle, proteolytic, mitochondrial, and metabolic module rather than a confidently defined canonical pathway. The strongest biological themes suggested by individual gene annotations are integrin-linked cell-matrix signaling through ILK, calcium-sensitive proteolysis through CAPN2, xenobiotic and arachidonate metabolism through EPHX1, membrane organization and vesicle trafficking through FLOT1 and STOM, heme synthesis through FECH, and actin-dependent membrane transport through MYO1C. No GO or KEGG term passed global correction, so these annotations should be treated as functional clues from individual genes rather than evidence of significant pathway enrichment. The network is locally structured but functionally mixed, with SCCPDH linking the FLOT1-STOM branch to APMAP and BCAM, and additional smaller branches centered on CAPN2, EPHX1, KANK2, and PITRM1.

**Cell composition.** The module contains no secreted genes and is not predominantly composed of plasma proteins. Most genes have low tissue specificity, while the remainder show tissue enhancement in liver, adipose tissue, blood vessel, kidney, or bone marrow. HPA single-cell evidence is strongly cell-type selective for many members, especially neutrophils or neutrophil progenitors, alveolar cells, smooth muscle cells, adipocytes, cytotrophoblasts, and erythroid cells. Several members have immune-cell enrichment or immune-cell associations, and FECH is associated with erythrocyte progenitors and erythrocytes. This composition raises the possibility that the shared heart and stem-cell signal partly reflects shared cell populations, vascular or blood-related material, or sample admixture rather than a heart-specific or stem-cell-specific program. Detection of several proteins in heart supports some genuine cardiac representation, but absence of a matching HPA stem-cell tissue prevents a direct protein-level comparison for stem cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship among module members is FLOT1-STOM. This supports a real membrane-organization or vesicle-associated submodule, but it does not validate the full module as one physical complex or pathway. No hu.MAP complex contains multiple module members. The remaining co-abundance edges therefore appear to be co-expression or indirect functional associations rather than relationships already established by the supplied interaction and complex resources.

**STRING interactions (score >= 0.7)**: 1 of 78 gene pairs: FLOT1–STOM (0.915)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact conserved co-abundance module is a candidate finding, but it cannot be called a definitively new biological mechanism. Its mixed functional composition, lack of a globally significant GO or KEGG term, absence of a multi-member hu.MAP complex, and limited STRING support make the biological interpretation exploratory. Conversely, absence from STRING or hu.MAP alone does not establish novelty, because those resources are incomplete and are not designed to capture every tissue-specific co-abundance relationship. The most defensible novelty claim is that this particular cross-tissue co-abundance arrangement may reveal an under-characterized association linking membrane organization, adhesion, proteolysis, and metabolic or erythroid-related processes, pending replication and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a shared cell-surface and intracellular stress-adaptation program operating in cardiac-associated cells and stem-cell-associated populations. In this model, FLOT1-STOM and MYO1C organize membrane domains and vesicle traffic; ILK, KANK2, and BCAM connect those domains to adhesion, actin architecture, and cell polarity; CAPN2 provides calcium-responsive proteolysis; and EPHX1, SCCPDH, PITRM1, and FECH support detoxification, lipid or glycolipid handling, mitochondrial protein quality control, and heme-related metabolism. The blood-cell and erythroid associations suggest an alternative or additional explanation involving vascular or hematopoietic admixture. This is a hypothesis, not an established pathway, and should be tested by cell-resolved expression, purity assessment, and perturbation of the membrane-adhesion and proteolysis components.

### Important genes

#### ILK

- **Related proteins** (co-abundance neighbors): CAPN2 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin linked kinase. This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastas…
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); familial hypertrophic cardiomyopathy (0.194); Abnormality of the cardiovascular system (0.148); Prolonged QT interval (0.118); neoplasm (0.118)
- **Europe PMC papers**: 8401
- **Why important**: ILK is a network bridge from the module's co-abundance structure to a defined cellular process: integrin-mediated signaling and cell-matrix adhesion. It is localized to focal adhesion sites, is detected in heart, and has the largest literature volume among the selected genes. Its disease associations include cardiovascular abnormalities and familial hypertrophic cardiomyopathy. These features make ILK a strong candidate for linking the module to cardiac or mechanical-cellular biology, even though it has no globally significant enrichment term and only a single supplied network neighbor.
- **Conclusion**: Established evidence supports ILK as an integrin-associated adhesion and morphogenesis regulator with cardiac relevance. The hypothesis that ILK organizes the whole module is plausible but unproven, because the supplied network directly connects it only to CAPN2.

#### CAPN2

- **Related proteins** (co-abundance neighbors): EPHX1 (0.90), ILK (0.90), PITRM1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Connecting piece, Mid piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calpain 2. The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpa…
- **Diseases (Open Targets)**: Alzheimer disease (0.389); urolithiasis (0.288); alcohol drinking (0.288); aortic stenosis (0.141); neoplasm (0.105)
- **Europe PMC papers**: 1796
- **Why important**: CAPN2 is a central connector within the branch containing EPHX1, ILK, and PITRM1. It encodes the large catalytic subunit of ubiquitous calpain, an intracellular calcium-activated protease, and its annotations include response to mechanical stimulus, hypoxia, and cardiac muscle cell apoptosis. It therefore provides a mechanistically coherent link between calcium or mechanical stress, adhesion, proteolysis, and cardiac biology. It also has substantial literature and disease associations including aortic stenosis.
- **Conclusion**: Established evidence supports CAPN2 as a calcium-regulated intracellular protease with plausible relevance to mechanically stressed cardiac cells. Its role as the module's functional proteolytic hub remains a hypothesis rather than a demonstrated property of this module.

#### FLOT1

- **Related proteins** (co-abundance neighbors): SCCPDH (0.89), MYO1C (0.84); STRING partners: STOM (0.915)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: flotillin 1. This gene encodes an protein that localizes to the caveolae, which are small domains on the inner cell membranes. This protein plays a role in vesicle trafficking and cell morphology. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016].
- **Diseases (Open Targets)**: neurodegenerative disease (0.332); gastric cancer (0.101); hepatocellular carcinoma (0.101); neoplasm (0.097); lung adenocarcinoma (0.093)
- **Europe PMC papers**: 3298
- **Why important**: FLOT1 is part of the only high-confidence STRING pair in the module, with STOM, and is connected in the co-abundance graph to SCCPDH and MYO1C. It localizes to the Golgi and is associated with caveolar membrane domains, vesicle trafficking, cell morphology, receptor internalization, and junction organization. It is detected in heart and has extensive literature, making it a strong anchor for the membrane and trafficking interpretation.
- **Conclusion**: Established evidence supports FLOT1 as a membrane-domain and vesicle-trafficking protein, with a known relationship to STOM. It is reasonable to infer a membrane organization component in the module, but not to infer a larger FLOT1-centered complex from the available evidence.

#### STOM

- **Related proteins** (co-abundance neighbors): SCCPDH (0.87); STRING partners: FLOT1 (0.915)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: stomatin. This gene encodes a member of a highly conserved family of integral membrane proteins. The encoded protein localizes to the cell membrane of red blood cells and other cell types, where it may regulate ion channels and transporters. Loss of localization of the encoded protein is associated with hereditary stomatocytosis, a form of hemolytic anemia. There is a pseudogene for this gene on chromosome …
- **Diseases (Open Targets)**: neurodegenerative disease (0.332); Finnish type amyloidosis (0.191); hereditary disease (0.190); lymphatic system disorder (0.183); vein disorder (0.183)
- **Europe PMC papers**: 1636
- **Why important**: STOM is the partner of FLOT1 in the only supplied high-confidence STRING interaction. It is a conserved membrane protein associated with ion channels and transporters, localizes to vesicles and the plasma membrane, and is enriched in several cell types including neutrophils, neutrophil progenitors, and platelets. Its red-cell biology and blood-related expression make it informative both for a membrane mechanism and for the possibility of blood-cell contribution to the shared signal.
- **Conclusion**: Established evidence supports STOM as a membrane and ion-transport regulator that physically or functionally associates with FLOT1. Its inclusion strengthens the membrane-domain interpretation, while its blood-cell associations caution against interpreting the module as exclusively intrinsic to heart or stem cells.

#### FECH

- **Related proteins** (co-abundance neighbors): PITRM1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location None; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ferrochelatase. The protein encoded by this gene is localized to the mitochondrion, where it catalyzes the insertion of the ferrous form of iron into protoporphyrin IX in the heme synthesis pathway. Mutations in this gene are associated with erythropoietic protoporphyria. Two transcript variants encoding different isoforms have been found for this gene. A pseudogene of this gene is found on chromosome 3.[provided…
- **Diseases (Open Targets)**: autosomal erythropoietic protoporphyria (0.845); erythropoietic protoporphyria (0.714); neurodegenerative disease (0.547); Parkinson disease (0.339); Alzheimer disease (0.337)
- **Europe PMC papers**: 1826
- **Why important**: FECH provides a distinct and biologically important metabolic branch. It is the mitochondrial ferrochelatase that inserts iron into protoporphyrin during heme biosynthesis, is tissue-enhanced in bone marrow, and is associated with erythroid progenitors and erythrocytes. It is detected in heart and has established disease links to erythropoietic protoporphyria. Its connection to PITRM1 places heme metabolism near mitochondrial protein processing in the module.
- **Conclusion**: Established evidence supports FECH as a heme-biosynthetic enzyme with strong erythroid relevance and cardiac detectability. Its presence may represent a real mitochondrial or metabolic component, but it also increases concern that blood or erythroid material contributes to the shared co-abundance signal.

## Module 8

**Tissue pair**: heart and stem_cells  
**Genes (5)**: BCS1L, HSDL2, AK1, L2HGDH, NDUFS5

### Function

The module is most consistent with coordinated mitochondrial energy metabolism and cellular nucleotide homeostasis. L2HGDH provides a link to mitochondrial organic-acid and redox metabolism, BCS1L to respiratory-chain assembly, NDUFS5 to complex I and oxidative phosphorylation, and AK1 to ATP, ADP and AMP balance. HSDL2 adds a possible oxidoreductase and lipid-metabolism component. No GO or KEGG term passed global correction, and STRING reported no supplementary functional enrichment; therefore this interpretation rests on gene annotations and network structure rather than statistically significant pathway enrichment.

**Cell composition.** No module gene is secreted, so the module is not consistent with a plasma-protein or secreted-protein signal. All genes were detected in heart muscle, while there is no matching HPA tissue for stem cells. The HPA profiles are heterogeneous: some genes are tissue enhanced and others have low tissue specificity, while every gene is cell-type enhanced. The reported enriched cell types include cardiomyocytes, adipocytes, myonuclei, neutrophils and several epithelial or specialized cell types. Most genes have low immune-cell specificity, with one gene not detected in immune cells and one immune-cell-enhanced gene. The shared signal therefore may represent a broadly distributed metabolic program, a heart-associated cellular program, or shared cell composition rather than blood contamination. AK1 is highly expressed in skeletal muscle, brain and erythrocytes, so cellular composition should be considered.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported for any gene pair, and no hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated as established physical interactions or as a known multiprotein complex. The internal structure is nevertheless biologically coherent: L2HGDH is the central connector to BCS1L, NDUFS5 and AK1, while HSDL2 connects to BCS1L. This supports coordinated mitochondrial and energy-related regulation, but does not establish direct molecular binding among the genes.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is not established as a new molecular complex or interaction network because STRING and hu.MAP provide no supporting relationships. However, database absence does not prove novelty. The pattern could reflect coordinated expression, shared cellular composition, tissue-specific regulation or incompletely catalogued biology. The cautious conclusion is that this may be a potentially novel cross-tissue co-abundance association, but novelty requires replication and independent validation.

**Hypothesis.** Hypothesis: in heart and stem-cell samples, variation in mitochondrial redox handling and respiratory capacity is coordinated with adenine-nucleotide buffering. L2HGDH may connect organic-acid metabolism with respiratory machinery involving BCS1L and NDUFS5, while AK1 may help buffer cellular energy charge. HSDL2 may provide an auxiliary oxidoreductase or lipid-related component through its association with BCS1L. This is a mechanistic hypothesis based on co-abundance and annotations, not a demonstrated causal pathway or physical complex.

### Important genes

#### L2HGDH

- **Related proteins** (co-abundance neighbors): BCS1L (0.83), NDUFS5 (0.81), AK1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: L-2-hydroxyglutarate dehydrogenase. This gene encodes L-2-hydroxyglutarate dehydrogenase, a FAD-dependent enzyme that oxidizes L-2-hydroxyglutarate to alpha-ketoglutarate in a variety of mammalian tissues. Mutations in this gene cause L-2-hydroxyglutaric aciduria, a rare autosomal recessive neurometabolic disorder resulting in moderate to severe cognitive disability. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: L-2-hydroxyglutaric aciduria (0.823); neurodegenerative disease (0.514); hereditary disease (0.452); gout (0.376); lysosomal storage disease (0.370)
- **Europe PMC papers**: 521
- **Why important**: L2HGDH has the most central position in the module, connecting to BCS1L, NDUFS5 and AK1. It encodes a mitochondrial FAD-dependent enzyme that oxidizes L-2-hydroxyglutarate to alpha-ketoglutarate and is annotated in tricarboxylic acid cycle and two-oxoglutarate metabolism. It is associated with L-2-hydroxyglutaric aciduria and has substantial literature support.
- **Conclusion**: Established evidence supports L2HGDH as the principal metabolic connector and a mitochondrial redox-related gene. Its co-abundance may track respiratory or metabolic state, but the module does not show that L2HGDH regulates the other genes.

#### BCS1L

- **Related proteins** (co-abundance neighbors): HSDL2 (0.84), L2HGDH (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BCS1 ubiquinol-cytochrome c reductase complex chaperone. This gene encodes a homolog of the S. cerevisiae bcs1 protein which is involved in the assembly of complex III of the mitochondrial respiratory chain. The encoded protein does not contain a mitochondrial targeting sequence but experimental studies confirm that it is imported into mitochondria. Mutations in this gene are associated with mitochondrial complex III deficiency and the GRACILE syndrome.…
- **Diseases (Open Targets)**: GRACILE syndrome (0.819); Bjornstad syndrome (0.819); mitochondrial complex III deficiency (0.792); mitochondrial complex III deficiency nuclear type 1 (0.719); Leigh syndrome (0.694)
- **Europe PMC papers**: 606
- **Why important**: BCS1L connects L2HGDH with HSDL2 and encodes a mitochondrial respiratory-chain complex assembly chaperone. It is associated with mitochondrial complex deficiency, GRACILE syndrome, Bjornstad syndrome and Leigh syndrome, and is detected in heart. Its cell-type annotation includes cardiomyocytes.
- **Conclusion**: Established evidence supports BCS1L as a key respiratory-chain maintenance gene and a bridge between the central metabolic signal and HSDL2. Coordinated respiratory demand is plausible, but direct interaction with the other module genes is not established.

#### NDUFS5

- **Related proteins** (co-abundance neighbors): L2HGDH (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit S5. This gene is a member of the NADH dehydrogenase (ubiquinone) iron-sulfur protein family. The encoded protein is a subunit of the NADH:ubiquinone oxidoreductase (complex I), the first enzyme complex in the electron transport chain located in the inner mitochondrial membrane. Alternative splicing results in multiple transcript variants and pseudogenes have been identified on chromosomes 1, 4 and 17.…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.608); Parkinson disease (0.605); diabetes mellitus (0.578); neurodegenerative disease (0.576); Alzheimer disease (0.536)
- **Europe PMC papers**: 800
- **Why important**: NDUFS5 connects to L2HGDH and encodes a subunit of mitochondrial complex I. Its annotations include mitochondrial electron transport, aerobic respiration, complex I assembly, proton motive force-driven ATP synthesis and proton transmembrane transport. It has substantial literature support and associations with metabolic and neurodegenerative disorders.
- **Conclusion**: Established evidence supports NDUFS5 as the complex I component anchoring the respiratory interpretation. Its co-abundance with L2HGDH is compatible with coordinated mitochondrial function, but does not demonstrate complex I assembly with the other module members.

#### AK1

- **Related proteins** (co-abundance neighbors): L2HGDH (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenylate kinase 1. This gene encodes an adenylate kinase enzyme involved in energy metabolism and homeostasis of cellular adenine nucleotide ratios in different intracellular compartments. This gene is highly expressed in skeletal muscle, brain and erythrocytes. Certain mutations in this gene resulting in a functionally inadequate enzyme are associated with a rare genetic disorder causing nonspherocytic hemolytic an…
- **Diseases (Open Targets)**: hemolytic anemia due to adenylate kinase deficiency (0.765); myeloid leukemia (0.131); acute myeloid leukemia (0.059); lung adenocarcinoma (0.051); nasopharyngeal carcinoma (0.049)
- **Europe PMC papers**: 2424
- **Why important**: AK1 connects directly to L2HGDH and encodes adenylate kinase, an enzyme involved in maintaining intracellular adenine-nucleotide ratios and in ATP, ADP and AMP metabolism. It is highly expressed in skeletal muscle, brain and erythrocytes, is detected in heart, and is associated with adenylate-kinase-deficiency hemolytic anemia. It has substantial literature support.
- **Conclusion**: Established evidence supports AK1 as the nucleotide-energy homeostasis component. Its distribution also makes shared cellular composition a possible contributor to the module. Coupling AK1 activity to mitochondrial respiratory variation remains a hypothesis.

## Module 9

**Tissue pair**: heart and stem_cells  
**Genes (5)**: CRAT, CPT2, AK4, SLC25A20, IMMT

### Function

The module is most consistent with a mitochondrial fatty-acid utilization and carnitine-shuttle program, with a possible connection to mitochondrial energy homeostasis and inner-membrane organization. CRAT, CPT2, and SLC25A20 provide the strongest functional coherence: CRAT transfers acyl groups to carnitine, SLC25A20 transports acylcarnitines into the mitochondrial matrix, and CPT2 supports long-chain fatty-acid entry into mitochondrial oxidation. AK4 adds a mitochondrial nucleotide and energy-balance component, while IMMT adds a mitochondrial cristae and inner-membrane context. No GO or KEGG term passed global correction, so this functional interpretation is based on the individual gene annotations, network structure, STRING evidence, and complex evidence rather than on globally significant GO or KEGG enrichment.

**Cell composition.** The module is not composed of secreted proteins, and its HPA profile does not support a predominantly plasma-protein or blood-cell-derived module. The genes are tissue enhanced and are especially represented in liver, with additional signals in metabolically active epithelial, muscle, and reproductive cell types. Most genes have low immune-cell specificity, although AK4 has a blood-cell group-enriched signal involving myeloid populations. All module proteins were detected in heart muscle, supporting a genuine heart-associated mitochondrial program. HPA has no matching tissue for the stem_cells category, so the stem-cell interpretation cannot be independently confirmed from the reported HPA protein-detection field. The shared signal may therefore reflect a conserved mitochondrial metabolic state or shared cellular physiology rather than contamination by circulating proteins.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known STRING relationships are CPT2 with SLC25A20 and CRAT with SLC25A20. STRING also places CRAT and CPT2 in the supplementary Choline/Carnitine O-acyltransferase Pfam signal (STRING Pfam Choline/Carnitine o-acyltransferase; within-query FDR = 0.0385), but this is supplementary enrichment and is not globally corrected across modules. The module network contains additional co-abundance relationships, including links involving CRAT, AK4, and IMMT, for which corresponding high-confidence STRING partners are not listed in the fact sheet. hu.MAP places CPT2 and CRAT together in complex evidence (hu.MAP huMAP3_13468.1), but they represent only a small portion of a much larger, functionally heterogeneous mitochondrial complex. Together, these results support a real metabolic core centered on carnitine and mitochondrial function, while indicating that the complete co-abundance module is not simply a single established protein complex.

**STRING interactions (score >= 0.7)**: 2 of 10 gene pairs: CPT2–SLC25A20 (0.996); CRAT–SLC25A20 (0.916)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam Choline/Carnitine o-acyltransferase (FDR = 0.0385, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (CPT2, CRAT; 2/99)

### Novelty

The biological processes represented by this module are established rather than novel: mitochondrial fatty-acid transport, carnitine metabolism, fatty-acid oxidation, nucleotide-energy regulation, and cristae organization are all already supported by gene annotations and disease biology. The potentially new finding is the co-abundance arrangement of these genes across heart and stem_cells, particularly the association of the CRAT-centered network with AK4 and IMMT alongside the carnitine-shuttle genes. That claim should remain provisional because absence of a matching STRING or hu.MAP relationship does not establish novelty, and the module has no globally significant GO or KEGG term. The most defensible conclusion is that this is a potentially informative cross-tissue co-abundance configuration built from largely known mitochondrial biology, not a demonstrated new pathway or complex.

**Hypothesis.** Hypothesis: the shared module marks coordinated mitochondrial adaptation in which acylcarnitine production and transport through CRAT, SLC25A20, and CPT2 are coupled to mitochondrial nucleotide-energy buffering by AK4 and to cristae organization through IMMT. In heart, this could support sustained fatty-acid oxidation and respiratory capacity; in stem_cells, it could reflect a conserved mitochondrial state associated with metabolic maturation or cellular maintenance. The co-abundance link to IMMT is compatible with structural organization of the inner membrane, but it does not establish direct physical regulation. This mechanism requires validation by protein interaction, acylcarnitine flux, mitochondrial respiration, and perturbation experiments.

### Important genes

#### CRAT

- **Related proteins** (co-abundance neighbors): IMMT (0.91), AK4 (0.84), CPT2 (0.81); STRING partners: SLC25A20 (0.916)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: carnitine O-acetyltransferase. This gene encodes carnitine O-acetyltransferase, a member of the carnitine acyltransferase family and a key metabolic pathway enzyme which plays an important role in energy homeostasis and fat metabolism. This enzyme catalyzes the reversible transfer of acyl groups from an acyl-CoA thioester to carnitine and regulates the ratio of acyl-CoA/CoA. It is found in both the mitochondria and the peroxiso…
- **Diseases (Open Targets)**: neurodegeneration with brain iron accumulation 8 (0.499); neurodegeneration with brain iron accumulation (0.341); neurodegenerative disease (0.301); Alzheimer disease (0.252); lysosomal storage disease (0.247)
- **Europe PMC papers**: 4594
- **Why important**: CRAT is the central network gene, connecting the carnitine-metabolism core to AK4, CPT2, and IMMT. Its enzyme function directly links acyl-CoA and carnitine pools and therefore provides a mechanistic bridge between fatty acid handling and mitochondrial energy homeostasis. It is supported by the supplementary STRING Pfam signal (STRING Pfam Choline/Carnitine o-acyltransferase; within-query FDR = 0.0385), appears in the hu.MAP evidence (hu.MAP huMAP3_13468.1), has extensive literature, and is detected in heart.
- **Conclusion**: Established evidence supports CRAT as the most plausible metabolic organizer of the module. The hypothesis that it coordinates the module's structural and energetic branches through co-abundance is reasonable but not established as direct regulation.

#### SLC25A20

- **Related proteins** (co-abundance neighbors): AK4 (0.83); STRING partners: CPT2 (0.996), CRAT (0.916)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 25 member 20. This gene product is one of several closely related mitochondrial-membrane carrier proteins that shuttle substrates between cytosol and the intramitochondrial matrix space. This protein mediates the transport of acylcarnitines into mitochondrial matrix for their oxidation by the mitochondrial fatty acid-oxidation pathway. Mutations in this gene are associated with carnitine-acylcarnitine transloca…
- **Diseases (Open Targets)**: carnitine-acylcarnitine translocase deficiency (0.826); hereditary disease (0.192); Pancreatic pseudocyst (0.132); Abnormality of the skeletal system (0.110); neoplasm (0.097)
- **Europe PMC papers**: 1115
- **Why important**: SLC25A20 is the mitochondrial acylcarnitine carrier and is connected in STRING to both CPT2 and CRAT. Its network position links the transport step to the two principal carnitine-related enzymes. Mutations are associated with carnitine-acylcarnitine translocase deficiency and cardiac pathology, making it especially relevant to a heart-associated module. It is also detected in heart and has substantial disease and literature support.
- **Conclusion**: Established evidence identifies SLC25A20 as a core transport component of the module and a strong candidate for functional importance in cardiac fatty-acid oxidation. Its role as the physical coordinator of the whole co-abundance module remains a hypothesis.

#### CPT2

- **Related proteins** (co-abundance neighbors): CRAT (0.81); STRING partners: SLC25A20 (0.996)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: carnitine palmitoyltransferase 2. The protein encoded by this gene is a nuclear protein which is transported to the mitochondrial inner membrane. Together with carnitine palmitoyltransferase I, the encoded protein oxidizes long-chain fatty acids in the mitochondria. Defects in this gene are associated with mitochondrial long-chain fatty-acid (LCFA) oxidation disorders. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: carnitine palmitoyl transferase II deficiency, myopathic form (0.830); carnitine palmitoyl transferase II deficiency, severe infantile form (0.800); carnitine palmitoyl transferase II deficiency, neonatal form (0.772); carnitine palmitoyltransferase II deficiency (0.710); hereditary disease (0.505)
- **Europe PMC papers**: 5133
- **Why important**: CPT2 is a core long-chain fatty-acid oxidation enzyme and forms a high-confidence STRING relationship with SLC25A20. It also shares hu.MAP complex evidence with CRAT (hu.MAP huMAP3_13468.1) and is represented in the supplementary carnitine-related STRING signal (STRING Pfam Choline/Carnitine o-acyltransferase; within-query FDR = 0.0385). CPT2 has extensive literature and strong disease associations involving myopathic, infantile, neonatal, and broader CPT2 deficiency phenotypes, including effects relevant to muscle and cardiac energy metabolism.
- **Conclusion**: Established evidence supports CPT2 as a central functional member of the fatty-acid oxidation arm. The module may report coordinated control of substrate delivery and oxidation, but the co-abundance data alone cannot determine whether CPT2 is rate-limiting.

#### AK4

- **Related proteins** (co-abundance neighbors): CRAT (0.84), SLC25A20 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenylate kinase 4. This gene encodes a member of the adenylate kinase family of enzymes. The encoded protein is localized to the mitochondrial matrix. Adenylate kinases regulate the adenine and guanine nucleotide compositions within a cell by catalyzing the reversible transfer of phosphate group among these nucleotides. Five isozymes of adenylate kinase have been identified in vertebrates. Expression of these isozym…
- **Diseases (Open Targets)**: self-injurious ideation (0.304); type 2 diabetes mellitus (0.302); diabetes mellitus (0.298); Hepatitis (0.270); schizophrenia (0.262)
- **Europe PMC papers**: 1191
- **Why important**: AK4 occupies a bridging position between CRAT and SLC25A20 in the module and contributes mitochondrial adenine-nucleotide interconversion and energy regulation. Its HPA profile is enriched in metabolically active tissues and includes a myeloid-cell group-enriched signal, while its annotations connect it to oxidative phosphorylation and nucleotide metabolism. It has a meaningful disease and literature record despite lacking the listed STRING or hu.MAP support.
- **Conclusion**: Established evidence supports AK4 as a plausible energy-state component rather than a canonical carnitine-shuttle protein. Its bridging position suggests a hypothesis that nucleotide balance couples fatty-acid utilization to mitochondrial energetic demand, but that coupling is not directly demonstrated here.

#### IMMT

- **Related proteins** (co-abundance neighbors): CRAT (0.91); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inner membrane mitochondrial protein. Enables RNA binding activity. Involved in cristae formation. Located in mitochondrial inner membrane. Part of MICOS complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); multinodular goiter (0.196); alcohol drinking (0.190); breast cancer (0.094); neoplasm (0.087)
- **Europe PMC papers**: 933
- **Why important**: IMMT connects the metabolic portion of the module to mitochondrial architecture through its role in inner-membrane organization, cristae formation, and the MICOS complex. It is linked to CRAT in the co-abundance network, is detected in heart, and has disease-oriented literature involving mitochondrial and degenerative biology. Although it lacks the listed STRING and hu.MAP relationships, its functional annotation provides an important structural context for the module.
- **Conclusion**: Established evidence supports IMMT as a mitochondrial membrane-organization gene that may contextualize the metabolic genes. Its direct participation in fatty-acid oxidation or regulation of CRAT is only a hypothesis from the co-abundance pattern.

## Module 10

**Tissue pair**: heart and stem_cells  
**Genes (10)**: CLIC1, GSTP1, HNRNPK, HNRNPL, HNRNPR, HSP90AA1, PDK1, RAN, CCT7, CCT8

### Function

The strongest functional interpretation is a conserved nuclear proteostasis and RNA-processing module. The primary evidence is the globally corrected enrichment for positive regulation of protein localization to the nucleus and regulation of protein localization to the nucleus (GO:BP positive regulation of protein localization to nucleus; q_global = 0.0346) (GO:BP regulation of protein localization to nucleus; q_global = 0.047), driven by CCT7, CCT8, HSP90AA1, and RAN. RAN provides an established nuclear transport and cell-cycle connection; CCT7 and CCT8 are chaperonin subunits involved in protein folding; HSP90AA1 is a molecular chaperone; and HNRNPK, HNRNPL, and HNRNPR are nuclear RNA-binding proteins involved in pre-mRNA processing and splicing. GSTP1, CLIC1, and PDK1 add detoxification, ion-transport or redox-related, and metabolic-stress functions, respectively, but these are not supported as globally enriched module functions. Thus, the module is best viewed as a coordinated nuclear localization, protein-folding, and RNA-maturation program rather than as a narrowly defined tissue-specific pathway.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins: the HPA summary reports no secreted genes. It is also not blood-cell enriched according to HPA, which reports low immune-cell specificity for every module gene and no enriched blood-cell category. Most genes have low tissue specificity, consistent with broadly expressed housekeeping or core cellular functions. Several genes nevertheless show cell-type-enhanced patterns, including epithelial, germ-cell, neural-glial, platelet-related, and progenitor-associated cell types. This pattern could reflect shared cellular states or broadly conserved intracellular machinery in heart and stem-cell samples rather than a heart-specific biological program. Protein detection in heart supports presence of much of the module in heart, whereas the HPA resource has no matching stem-cell tissue for protein comparison. The STRING blood-cancer and leukemia-cell annotations (STRING TISSUES Blood cancer cell; within-query FDR = 0.0123) (STRING TISSUES Leukemia cell; within-query FDR = 0.0288) should therefore be treated as contextual similarity, not evidence that the module is caused by blood contamination.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP positive regulation of protein localization to nucleus | 0.0346 | CCT7, CCT8, HSP90AA1, RAN |
| GO:BP regulation of protein localization to nucleus | 0.047 | CCT7, CCT8, HSP90AA1, RAN |

### STRING and hu.MAP

STRING supports two partially connected functional neighborhoods. CCT7 and CCT8 are very strongly linked and connect to HSP90AA1 and RAN, supporting a chaperone and nuclear-localization arm. HNRNPK, HNRNPL, and HNRNPR form a densely interconnected RNA-binding arm. GSTP1 bridges several members of the RNA-binding and localization neighborhoods in the co-abundance graph, while CLIC1 links GSTP1 with CCT8; these edges are present in the module network even when corresponding STRING partners are absent. The STRING functional annotations for nucleoplasm and ubiquitin-like conjugation (STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.0194) (STRING Keyword Ubl conjugation; within-query FDR = 0.0473) are supplementary and concordant with the nuclear and proteostasis interpretation, but they are not globally corrected module-level evidence. hu.MAP independently places HNRNPK, HNRNPL, and HNRNPR together in several heterogeneous nuclear ribonucleoprotein complexes (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_07581.1). It also places CCT7 and CCT8 in several CCT-related complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). These observations indicate that the module recapitulates established molecular assemblies while also combining members of distinct assemblies into a tissue-shared co-abundance neighborhood.

**STRING interactions (score >= 0.7)**: 8 of 45 gene pairs: CCT7–CCT8 (0.999); CCT7–HSP90AA1 (0.849); CCT7–RAN (0.726); CCT8–HSP90AA1 (0.823); CCT8–RAN (0.712); HNRNPK–HNRNPL (0.99); HNRNPK–HNRNPR (0.962); HNRNPL–HNRNPR (0.961)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Blood cancer cell (FDR = 0.0123, 8 genes); COMPARTMENTS Nucleoplasm (FDR = 0.0194, 5 genes); TISSUES Leukemia cell (FDR = 0.0288, 7 genes); Keyword Ubl conjugation (FDR = 0.0473, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10659.1 (HNRNPR, HNRNPL, HNRNPK; 3/28); huMAP3_10625.1 (HNRNPR, HNRNPL, HNRNPK; 3/57); huMAP3_07225.1 (HNRNPR, HNRNPL; 2/7); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09654.1 (HNRNPR, HNRNPL; 2/13); huMAP3_07581.1 (HNRNPR, HNRNPL; 2/21); huMAP3_07938.1 (CCT8, CCT7; 2/23); huMAP3_06559.1 (CCT8, CCT7; 2/25); huMAP3_09191.1 (CCT8, CCT7; 2/32); huMAP3_10656.1 (CCT8, CCT7; 2/36); huMAP3_14584.1 (CCT8, CCT7; 2/61)

### Novelty

The module should not be described as a newly discovered molecular complex. Several of its internal relationships are already supported by STRING, and the RNA-binding and CCT portions correspond to established hu.MAP complexes. The potentially novel aspect is the conserved co-abundance association across heart and stem-cell samples, particularly the coupling of RNA-processing proteins, chaperones, nuclear transport machinery, redox-related proteins, and metabolic regulation into one cross-tissue module. However, absence of a gene from STRING or hu.MAP does not establish novelty, and the current evidence does not demonstrate a new physical interaction or causal pathway. The defensible conclusion is that this is a potentially informative cross-tissue network-level organization of known components, requiring independent replication and perturbation experiments before being called a novel mechanism.

**Hypothesis.** Hypothesis: the module represents a shared cellular stress-adaptation state in which CCT7, CCT8, and HSP90AA1 maintain folding and stability of proteins, RAN regulates their nuclear trafficking, and the HNRNP proteins coordinate processing and transport of RNA transcripts. GSTP1 and CLIC1 may connect this nuclear proteostasis state to redox, detoxification, membrane, or signaling responses, while PDK1 may couple it to metabolic stress. In heart and stem-cell contexts, this coordinated state could help cells preserve proteome quality and RNA-processing capacity during differentiation, proliferation, or physiological stress. This is a mechanistic hypothesis derived from the network and annotations, not a demonstrated causal pathway.

### Important genes

#### RAN

- **Related proteins** (co-abundance neighbors): HNRNPK (0.90), GSTP1 (0.87), HSP90AA1 (0.81); STRING partners: CCT7 (0.726), CCT8 (0.712)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAN, member RAS oncogene family. RAN (ras-related nuclear protein) is a small GTP binding protein belonging to the RAS superfamily that is essential for the translocation of RNA and proteins through the nuclear pore complex. The RAN protein is also involved in control of DNA synthesis and cell cycle progression. Nuclear localization of RAN requires the presence of regulator of chromosome condensation 1 (RCC1). Mutations in RAN di…
- **Diseases (Open Targets)**: HIV infectious disease (0.565); Orthomyxoviridae infectious disease (0.376); pemphigus foliaceus (0.298); neurodegenerative disease (0.270); Genu valgum (0.136)
- **Europe PMC papers**: 133080
- **Why important**: RAN is a central bridge in the module network, connecting the RNA-binding and chaperone-associated neighborhoods. It is the only selected gene directly represented in both globally corrected nuclear-localization terms (GO:BP positive regulation of protein localization to nucleus; q_global = 0.0346) (GO:BP regulation of protein localization to nucleus; q_global = 0.047). Its established functions include nuclear import and export, ribosomal-subunit export, DNA synthesis, and cell-cycle control. It also has extensive literature coverage and disease-linked evidence, making it a strong biological anchor for the module.
- **Conclusion**: Established evidence supports RAN as the nuclear-transport and cell-cycle component of the module. The hypothesis that RAN coordinates the chaperone and heterogeneous nuclear ribonucleoprotein arms in this cross-tissue state is plausible from the network, but it is not proven by co-abundance.

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT7 (0.86), CLIC1 (0.83); STRING partners: CCT7 (0.999), HSP90AA1 (0.823), RAN (0.712)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is part of the tightly connected CCT7–CCT8 pair and is linked in STRING to HSP90AA1 and RAN. It contributes directly to the globally corrected nuclear-localization terms (GO:BP positive regulation of protein localization to nucleus; q_global = 0.0346) (GO:BP regulation of protein localization to nucleus; q_global = 0.047) and belongs to multiple hu.MAP CCT-related complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). Its established chaperonin function provides a mechanistic route by which the module could support folding and intracellular trafficking.
- **Conclusion**: Established evidence supports CCT8 as a protein-folding and chaperone-complex component. Its proposed role in stabilizing proteins destined for nuclear localization within this module is a hypothesis supported by the enrichment and network context, not a demonstrated substrate-specific effect.

#### CCT7

- **Related proteins** (co-abundance neighbors): CCT8 (0.86); STRING partners: CCT8 (0.999), HSP90AA1 (0.849), RAN (0.726)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is the partner of CCT8 in the module and in STRING, and it connects to HSP90AA1 and RAN. Like CCT8, it is represented in both globally corrected nuclear-localization terms (GO:BP positive regulation of protein localization to nucleus; q_global = 0.0346) (GO:BP regulation of protein localization to nucleus; q_global = 0.047) and in several hu.MAP CCT-related complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). Its established role in the CCT chaperonin gives the module a defined proteostasis component. Its disease associations include myocardial infarction among the listed Open Targets links, although that association does not establish a causal role here.
- **Conclusion**: Established evidence supports CCT7 as a core chaperonin subunit and a key member of the module’s proteostasis arm. A heart-relevant contribution to stress resilience is a hypothesis and should not be inferred solely from its presence in a heart-shared module.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): RAN (0.90), HNRNPL (0.82); STRING partners: HNRNPL (0.99), HNRNPR (0.962)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is a highly connected member of the RNA-binding neighborhood, linked to HNRNPL and HNRNPR in STRING and present in the high-confidence hu.MAP complexes (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_10625.1). Its established functions include RNA processing, pre-mRNA splicing, transcriptional regulation, and regulation of gene expression. It has substantial literature coverage and disease associations involving neurodevelopmental and hereditary disorders, supporting its importance as a regulatory rather than merely structural component.
- **Conclusion**: Established evidence supports HNRNPK as an RNA-processing and transcriptional-regulatory component embedded in known heterogeneous nuclear ribonucleoprotein assemblies. Its possible coordination with RAN and chaperone proteins in the shared module is a network-based hypothesis.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): GSTP1 (0.88), HNRNPK (0.82); STRING partners: HNRNPK (0.99), HNRNPR (0.961)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_10659.1, huMAP3_10625.1, huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_07581.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is a network connector between GSTP1 and HNRNPK and is linked strongly to HNRNPK and HNRNPR in STRING. It occurs across numerous hu.MAP heterogeneous nuclear ribonucleoprotein complexes (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_07581.1). Its established functions include RNA processing, alternative splicing, and transcriptional regulation. Its broad expression and nuclear localization make it a plausible marker of a shared intracellular program rather than a tissue-restricted factor.
- **Conclusion**: Established evidence supports HNRNPL as a core RNA-processing scaffold within known nuclear ribonucleoprotein assemblies. Its bridging position with GSTP1 suggests a possible connection between RNA handling and cellular stress responses, but that connection remains a hypothesis.

#### GSTP1

- **Related proteins** (co-abundance neighbors): HNRNPL (0.88), RAN (0.87), CLIC1 (0.84), HNRNPR (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutathione S-transferase pi 1. Glutathione S-transferases (GSTs) are a family of enzymes that play an important role in detoxification by catalyzing the conjugation of many hydrophobic and electrophilic compounds with reduced glutathione. Based on their biochemical, immunologic, and structural properties, the soluble GSTs are categorized into 4 main classes: alpha, mu, pi, and theta. This GST family member is a polymorphic gene…
- **Diseases (Open Targets)**: neurodegenerative disease (0.350); breast cancer (0.117); hepatocellular carcinoma (0.115); neoplasm (0.114); posterior cortical atrophy (0.113)
- **Europe PMC papers**: 12759
- **Why important**: GSTP1 has the highest network connectivity in the module and links HNRNPL, HNRNPR, RAN, and CLIC1. Its established enzymatic role is glutathione-dependent detoxification, with annotated functions involving oxidative stress, glutathione metabolism, xenobiotic metabolism, and inflammatory regulation. It is tissue-enhanced in esophagus but has low immune-cell specificity and is detected in heart, so its presence does not by itself indicate a blood-derived signal. Its extensive literature and disease associations make it an important stress-response component.
- **Conclusion**: Established evidence supports GSTP1 as a redox and detoxification enzyme that may connect stress handling to the nuclear RNA and localization machinery. The hypothesis that GSTP1 helps organize this module through redox-sensitive regulation or co-abundance coupling is not established as a physical or causal interaction.
