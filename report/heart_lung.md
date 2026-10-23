# Conserved co-abundance modules: heart and lung

## Module 0

**Tissue pair**: heart and lung  
**Genes (10)**: GOT2, ACADVL, ACO2, ATP5F1A, ATP5F1C, CS, ETFA, L2HGDH, SUCLG1, SUCLA2

### Function

This is a mitochondrial oxidative-energy and small-molecule metabolism module. The primary evidence is the globally corrected enrichment for mitochondrial matrix (GO:CC mitochondrial matrix; q_global = 0.00375), oxidation of organic compounds (GO:BP energy derivation by oxidation of organic compounds; q_global = 0.0107), generation of precursor metabolites and energy (GO:BP generation of precursor metabolites and energy; q_global = 0.0164), and small-molecule metabolic process (GO:BP small molecule metabolic process; q_global = 0.021). The genes collectively represent fatty-acid oxidation, the tricarboxylic-acid cycle, amino-acid transamination, succinyl-CoA metabolism, and ATP synthesis. The result is biologically coherent because the mitochondrial-matrix signal is supported by most genes, while all genes contribute to (GO:BP small molecule metabolic process; q_global = 0.021). STRING independently supports mitochondrial localization and respiratory or TCA-related functions (15 supplementary STRING terms; within-query FDR 7.76e-05–0.0149).

**Cell composition.** This is not a plasma-protein or secreted-protein module: HPA reports no secreted genes, and protein is detected for every module gene in both heart and lung. The module is also unlikely to be primarily a blood-cell signal because nearly all genes have low immune-cell specificity; only L2HGDH is immune-cell enhanced, in basophils. HPA shows tissue or cell-type enrichment for most genes, particularly in muscle, heart, liver, kidney, tongue, and several epithelial or digestive cell types. The shared heart-lung signal therefore most plausibly reflects conserved mitochondrial metabolic capacity or shared metabolically active cell populations, although the module alone cannot distinguish intrinsic regulation from cell-composition effects.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrial matrix | 0.00375 | ACADVL, ACO2, ATP5F1A, ATP5F1C, CS, ETFA, GOT2, SUCLA2, SUCLG1 |
| GO:BP energy derivation by oxidation of organic compounds | 0.0107 | ACADVL, ACO2, ATP5F1A, ATP5F1C, CS, ETFA, SUCLA2, SUCLG1 |
| GO:BP generation of precursor metabolites and energy | 0.0164 | ACADVL, ACO2, ATP5F1A, ATP5F1C, CS, ETFA, SUCLA2, SUCLG1 |
| GO:BP small molecule metabolic process | 0.021 | ACADVL, ACO2, ATP5F1A, ATP5F1C, CS, ETFA, GOT2, L2HGDH, SUCLA2, SUCLG1 |

### STRING and hu.MAP

STRING provides extensive prior support for the module. Its high-confidence relationships connect TCA-cycle, respiratory, fatty-acid-oxidation, and ATP-synthase components, with especially strong support around CS, ACO2, SUCLG1, SUCLA2, and the ATP synthase subunits. Thus, the co-abundance structure closely follows an already known mitochondrial biochemical network rather than an arbitrary gene cluster. hu.MAP provides complex-level support for ATP5F1A and ATP5F1C through (hu.MAP huMAP3_09307.1) and (hu.MAP huMAP3_11095.1). These complexes contain only a subset of the module and are broad multisubunit assemblies. The lack of hu.MAP assignments for the other genes does not contradict their biochemical relationships; it indicates only that those relationships are not represented as module-member pairs in the listed hu.MAP complexes.

**STRING interactions (score >= 0.7)**: 21 of 45 gene pairs: ACADVL–ETFA (0.877); ACO2–ATP5F1A (0.884); ACO2–CS (0.999); ACO2–GOT2 (0.753); ACO2–SUCLA2 (0.862); ACO2–SUCLG1 (0.929); ATP5F1A–ATP5F1C (0.999); ATP5F1A–CS (0.94); ATP5F1A–ETFA (0.786); ATP5F1A–SUCLA2 (0.802); ATP5F1A–SUCLG1 (0.853); ATP5F1C–CS (0.726); ATP5F1C–ETFA (0.715); ATP5F1C–SUCLA2 (0.751); ATP5F1C–SUCLG1 (0.934); CS–GOT2 (0.952); CS–L2HGDH (0.931); CS–SUCLA2 (0.96); CS–SUCLG1 (0.929); ETFA–SUCLG1 (0.956); SUCLA2–SUCLG1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transit peptide (FDR = 7.76e-05, 10 genes); RCTM The citric acid (TCA) cycle and respiratory electron transport (FDR = 0.00023, 8 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.00038, 9 genes); Component Mitochondrial matrix (FDR = 0.0011, 9 genes); Keyword Mitochondrion (FDR = 0.0015, 10 genes); Process Energy derivation by oxidation of organic compounds (FDR = 0.0024, 8 genes); RCTM Pyruvate metabolism and Citric Acid (TCA) cycle (FDR = 0.0041, 5 genes); COMPARTMENTS Mitochondrion (FDR = 0.0066, 10 genes); Process Small molecule metabolic process (FDR = 0.0092, 10 genes); Process Cellular respiration (FDR = 0.0092, 7 genes); WikiPathways TCA cycle (aka Krebs or citric acid cycle) (FDR = 0.0099, 4 genes); Keyword Tricarboxylic acid cycle (FDR = 0.0112, 4 genes); NetworkNeighborAL Citrate cycle (TCA cycle), and Lactate dehydrogenase activity (FDR = 0.0124, 5 genes); NetworkNeighborAL Tricarboxylic acid cycle (FDR = 0.0124, 4 genes); Component Mitochondrion (FDR = 0.0149, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09307.1 (ATP5F1A, ATP5F1C; 2/35); huMAP3_11095.1 (ATP5F1A, ATP5F1C; 2/45)

### Novelty

The broad biological function is not a new discovery: mitochondrial, TCA-cycle, respiratory, fatty-acid-oxidation, and ATP-synthesis relationships are already supported by STRING, hu.MAP, curated annotations, and substantial literature. The potentially novel result is the reproducible co-abundance of this particular gene combination across heart and lung, especially if this cross-tissue conservation and exact abundance pattern have not previously been reported. That claim requires comparison with published tissue coexpression modules and the source cohort. Absence from STRING or hu.MAP alone would not establish novelty; the strong prior interaction evidence instead supports a conserved known metabolic program with potentially novel tissue-level organization.

**Hypothesis.** Hypothesis: the shared heart-lung module reflects coordinated mitochondrial fuel oxidation and ATP production in energetically demanding cells. ACADVL and ETFA could couple long-chain fatty-acid oxidation to electron transfer and respiratory metabolism. CS, ACO2, GOT2, L2HGDH, SUCLG1, and SUCLA2 could maintain TCA-cycle carbon flow, anaplerosis, and succinate-related metabolism, while ATP5F1A and ATP5F1C could support conversion of the proton-motive force into ATP. The cross-tissue conservation may therefore represent a common oxidative metabolic state in heart and lung cells rather than a tissue-specific signaling pathway. This is a mechanistic hypothesis, not proof of physical assembly, causal regulation, or substrate preference.

### Important genes

#### CS

- **Related proteins** (co-abundance neighbors): ETFA (0.89), GOT2 (0.85), ATP5F1C (0.83), L2HGDH (0.82), SUCLG1 (0.82), ATP5F1A (0.82); STRING partners: ACO2 (0.999), ATP5F1A (0.94), ATP5F1C (0.726), GOT2 (0.952), L2HGDH (0.931), SUCLA2 (0.96), SUCLG1 (0.929)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS is a highly connected central node and the canonical entry enzyme of the TCA cycle. It participates in every primary enrichment term (4 globally significant GO/KEGG terms, q_global 0.00375–0.021; see the table) and in the supplementary STRING mitochondrial and TCA-related terms (15 supplementary STRING terms; within-query FDR 7.76e-05–0.0149). HPA shows tissue enhancement in skeletal muscle and tongue, with protein detected in heart and lung. It has extensive literature and established disease associations including neurodegenerative and hearing-related disorders.
- **Conclusion**: Established evidence supports CS as a biochemical anchor linking acetyl-CoA entry to the TCA cycle and as a major network hub. The module supports coordinated abundance with respiratory and ATP-producing proteins, but does not show that CS controls the module or that altered CS abundance causes the cross-tissue pattern.

#### ETFA

- **Related proteins** (co-abundance neighbors): GOT2 (0.91), CS (0.89), ACADVL (0.83), ATP5F1A (0.82), ATP5F1C (0.82), ACO2 (0.81), SUCLG1 (0.80); STRING partners: ACADVL (0.877), ATP5F1A (0.786), ATP5F1C (0.715), SUCLG1 (0.956)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein subunit alpha. ETFA participates in catalyzing the initial step of the mitochondrial fatty acid beta-oxidation. It shuttles electrons between primary flavoprotein dehydrogenases and the membrane-bound electron transfer flavoprotein ubiquinone oxidoreductase. Defects in electron-transfer-flavoprotein have been implicated in type II glutaricaciduria in which multiple acyl-CoA dehydrogenase deficiencies result in l…
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.834); glutaric aciduria (0.756); hereditary disease (0.469); multiple acyl-CoA dehydrogenase deficiency, mild type (0.370); multiple acyl-CoA dehydrogenase deficiency, severe neonatal type (0.370)
- **Europe PMC papers**: 1433
- **Why important**: ETFA has the strongest weighted network position in the supplied module and links ACADVL with TCA and ATP-synthesis components. It contributes to every primary enrichment term (4 globally significant GO/KEGG terms, q_global 0.00375–0.021; see the table) and to the mitochondrial, respiratory, and fatty-acid-oxidation STRING evidence (6 supplementary STRING terms; within-query FDR 7.76e-05–0.0024), (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0066) (STRING Process Small molecule metabolic process; within-query FDR = 0.0092) (STRING Process Cellular respiration; within-query FDR = 0.0092), and (STRING Component Mitochondrion; within-query FDR = 0.0149). Its established function is electron transfer from flavoprotein dehydrogenases toward respiratory metabolism. It is associated with multiple acyl-CoA dehydrogenase deficiency and glutaric aciduria and has substantial literature support.
- **Conclusion**: Established evidence identifies ETFA as a bridge between fatty-acid oxidation and downstream mitochondrial energy metabolism. Its network position makes it important for interpreting the module, but the co-abundance data do not demonstrate that ETFA initiates the program or that fatty-acid oxidation is the dominant substrate.

#### ATP5F1A

- **Related proteins** (co-abundance neighbors): ACO2 (0.86), GOT2 (0.82), ETFA (0.82), CS (0.82), ACADVL (0.81); STRING partners: ACO2 (0.884), ATP5F1C (0.999), CS (0.94), ETFA (0.786), SUCLA2 (0.802), SUCLG1 (0.853)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, lung
- **hu.MAP 3.0**: huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit alpha. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, using an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic po…
- **Diseases (Open Targets)**: mitochondrial complex V (ATP synthase) deficiency, nuclear type 4A (0.655); mitochondrial proton-transporting ATP synthase complex deficiency (0.648); mitochondrial complex V (ATP synthase) deficiency, nuclear type 4B (0.532); hereditary disease (0.394); Mitochondrial encephalopathy (0.371)
- **Europe PMC papers**: 822
- **Why important**: ATP5F1A is a highly connected module node and the catalytic alpha subunit of mitochondrial ATP synthase. It contributes to every primary enrichment term (4 globally significant GO/KEGG terms, q_global 0.00375–0.021; see the table), is strongly connected in STRING to TCA and respiratory genes, and participates in the hu.MAP ATP-synthase-related complexes (hu.MAP huMAP3_09307.1) and (hu.MAP huMAP3_11095.1). HPA detects its protein in heart and lung. Its established disease associations include nuclear mitochondrial complex V deficiency and mitochondrial encephalopathy.
- **Conclusion**: Established evidence supports ATP5F1A as the clearest ATP-production component and as a physical-complex-supported representative of oxidative phosphorylation. Its co-abundance with matrix enzymes is consistent with coordinated energy production, but does not establish altered ATP synthase activity or direct regulation by the matrix enzymes.

#### ACADVL

- **Related proteins** (co-abundance neighbors): ETFA (0.83), ATP5F1A (0.81); STRING partners: ETFA (0.877)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA dehydrogenase very long chain. The protein encoded by this gene is targeted to the inner mitochondrial membrane where it catalyzes the first step of the mitochondrial fatty acid beta-oxidation pathway. This acyl-Coenzyme A dehydrogenase is specific to long-chain and very-long-chain fatty acids. A deficiency in this gene product reduces myocardial fatty acid beta-oxidation and is associated with cardiomyopathy. Alternative splic…
- **Diseases (Open Targets)**: very long chain acyl-CoA dehydrogenase deficiency (0.865); hereditary disease (0.531); long chain acyl-CoA dehydrogenase deficiency (0.506); rhabdomyolysis (0.464); Acute rhabdomyolysis (0.436)
- **Europe PMC papers**: 3504
- **Why important**: ACADVL provides the clearest long-chain and very-long-chain fatty-acid oxidation connection. It contributes to every primary enrichment term (4 globally significant GO/KEGG terms, q_global 0.00375–0.021; see the table), connects to ETFA in STRING, and is enhanced in cardiomyocytes and other metabolically specialized cell types by HPA. Deficiency is associated with impaired myocardial fatty-acid oxidation, cardiomyopathy, rhabdomyolysis, and very-long-chain acyl-CoA dehydrogenase deficiency. It also has substantial literature support.
- **Conclusion**: Established evidence supports ACADVL as a fuel-entry enzyme relevant to cardiac energy metabolism and as a functional complement to ETFA. The module supports coordinated lipid-fuel utilization as a hypothesis, but does not establish that lipid oxidation rather than carbohydrate or amino-acid oxidation drives the shared signal.

#### SUCLG1

- **Related proteins** (co-abundance neighbors): CS (0.82), ETFA (0.80); STRING partners: ACO2 (0.929), ATP5F1A (0.853), ATP5F1C (0.934), CS (0.929), ETFA (0.956), SUCLA2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase GDP/ADP-forming subunit alpha. This gene encodes the alpha subunit of the heterodimeric enzyme succinate coenzyme A ligase. This enzyme is targeted to the mitochondria and catalyzes the conversion of succinyl CoA and ADP or GDP to succinate and ATP or GTP. Mutations in this gene are the cause of the metabolic disorder fatal infantile lactic acidosis and mitochondrial DNA depletion. [provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome 9 (0.811); neurodegenerative disease (0.520); mitochondrial DNA depletion syndrome (0.507); post term pregnancy (0.280); lysosomal storage disease (0.245)
- **Europe PMC papers**: 1277
- **Why important**: SUCLG1 is strongly connected to ACO2, ATP5F1A, ATP5F1C, CS, ETFA, and SUCLA2 in STRING. It contributes to every primary enrichment term (4 globally significant GO/KEGG terms, q_global 0.00375–0.021; see the table) and to the complete supplementary STRING evidence set (15 supplementary STRING terms; within-query FDR 7.76e-05–0.0149). It is the invariant alpha component of succinate-CoA ligase, with a direct role in TCA-cycle succinyl-CoA metabolism and substrate-level nucleotide-triphosphate production. It is associated with mitochondrial DNA depletion and severe metabolic disease and has substantial literature support.
- **Conclusion**: Established evidence supports SUCLG1 as a central TCA-cycle and succinyl-CoA metabolism component connecting the module's matrix enzymes. Its abundance pattern is consistent with coordinated mitochondrial metabolic capacity, but the module cannot determine whether succinate-CoA ligase activity, mitochondrial DNA maintenance, or another linked process explains the cross-tissue association.

## Module 1

**Tissue pair**: heart and lung  
**Genes (5)**: AIFM1, CRAT, IMMT, SLC25A12, SDHA

### Function

The most coherent interpretation is a mitochondrial inner-membrane and oxidative-energy module. SDHA supports respiratory-chain and succinate oxidation activity; CRAT supports carnitine-linked acyl-group transfer and fatty-acid energy metabolism; SLC25A12 supports mitochondrial amino-acid exchange and the malate-aspartate shuttle; IMMT supports cristae architecture through the MICOS complex; and AIFM1 links mitochondrial function with respiratory-chain assembly and apoptotic signaling. The shared STRING annotations for mitochondrial inner membrane are supplementary evidence only (STRING Keyword Mitochondrion inner membrane; within-query FDR = 0.0046)(STRING Component Mitochondrial inner membrane; within-query FDR = 0.03). No GO/KEGG term passed global correction, so there is no globally significant GO/KEGG enrichment to report. The biological interpretation therefore rests on convergent gene functions, mitochondrial localization, tissue evidence, and the supplementary STRING signal rather than on a formally enriched GO/KEGG term.

**Cell composition.** This does not resemble a plasma-protein, secreted-protein, or blood-cell module. None of the genes is classified as secreted, all have low immune-cell specificity, and protein detection is present in both heart and lung for every gene. The HPA profile instead points toward tissue and cell-type specialization, with repeated enrichment in skeletal muscle or tongue and a heart-muscle signal for SDHA. The genes are therefore compatible with energy-demanding contractile or metabolically specialized cells, although the cell-type annotations also include neuronal, epithelial, germ-cell, and hepatocyte populations. The shared heart-lung pattern is consequently more consistent with conserved mitochondrial biology or shared metabolically active cell populations than with blood contamination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The abundance network contains links among the module genes, but STRING reports no high-confidence pairwise interactions for any of the tested gene pairs, and hu.MAP reports no complex containing multiple module members. Thus, the co-abundance structure is not simply recapitulating a documented STRING interaction network or a hu.MAP complex. The supplementary STRING annotations (STRING Keyword Mitochondrion inner membrane; within-query FDR = 0.0046)(STRING Component Mitochondrial inner membrane; within-query FDR = 0.03) independently place all module genes in the mitochondrial inner-membrane context, but they do not establish direct physical interactions. Established molecular relationships remain gene-specific: SDHA is a respiratory-chain enzyme, IMMT is a MICOS and cristae-organization component, SLC25A12 is a mitochondrial aspartate-glutamate carrier, CRAT regulates acyl-CoA to CoA balance through carnitine chemistry, and AIFM1 participates in mitochondrial respiratory and apoptotic biology.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Mitochondrion inner membrane (FDR = 0.0046, 5 genes); Component Mitochondrial inner membrane (FDR = 0.03, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared co-abundance module may represent a previously unreported tissue-pair association because its specific network configuration is not supported by a corresponding multi-member STRING network or hu.MAP complex. However, this is not sufficient to claim a new molecular complex, pathway, or mechanism. The individual mitochondrial functions and disease links are established, and the absence of representation in STRING or hu.MAP can reflect database coverage, context dependence, tissue-specific regulation, or co-abundance relationships that are not physical interactions. The defensible conclusion is that the tissue-shared co-abundance pattern is potentially novel, while its mitochondrial biological theme is not itself novel.

**Hypothesis.** Hypothesis: in heart and lung, coordinated abundance of these genes reflects a conserved program that couples respiratory-chain capacity, inner-membrane architecture, substrate handling, and apoptotic readiness. IMMT may help maintain cristae structure, SDHA may support electron transfer and central metabolism, CRAT may buffer acyl-CoA and carnitine-linked fuel flux, and SLC25A12 may coordinate amino-acid exchange with redox metabolism; AIFM1 may connect this energetic state to stress and cell-death responses. This is a mechanistic hypothesis derived from the concordant annotations and co-abundance pattern, not a demonstrated physical pathway or causal interaction.

### Important genes

#### AIFM1

- **Related proteins** (co-abundance neighbors): SDHA (0.90), SLC25A12 (0.81), CRAT (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apoptosis inducing factor mitochondria associated 1. This gene encodes a flavoprotein essential for nuclear disassembly in apoptotic cells, and it is found in the mitochondrial intermembrane space in healthy cells. Induction of apoptosis results in the translocation of this protein to the nucleus where it affects chromosome condensation and fragmentation. In addition, this gene product induces mitochondria to release the apoptogenic proteins cytochr…
- **Diseases (Open Targets)**: severe X-linked mitochondrial encephalomyopathy (0.813); X-linked hereditary sensory and autonomic neuropathy with hearing loss (0.798); Charcot-Marie-Tooth disease X-linked recessive 4 (0.761); spondyloepimetaphyseal dysplasia, Bieganski type (0.747); combined oxidative phosphorylation deficiency (0.615)
- **Europe PMC papers**: 1952
- **Why important**: AIFM1 has the strongest network connectivity in the module and links the respiratory-associated genes with CRAT. It is a mitochondrial intermembrane-space flavoprotein involved in apoptotic nuclear disassembly, mitochondrial respiratory-chain assembly, and responses to cellular stress. Its disease associations include severe mitochondrial encephalomyopathy and other X-linked mitochondrial or neuropathic disorders, and it has substantial literature support.
- **Conclusion**: Established evidence supports AIFM1 as a mitochondrial stress, respiratory, and apoptosis-related component with major disease relevance. Its central position suggests that it may help organize the module's relationship between energy metabolism and stress signaling, but that coordinating role is a hypothesis rather than a demonstrated interaction in this module.

#### SDHA

- **Related proteins** (co-abundance neighbors): AIFM1 (0.90), SLC25A12 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate dehydrogenase complex flavoprotein subunit A. This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identi…
- **Diseases (Open Targets)**: mitochondrial complex II deficiency, nuclear type 1 (0.813); pheochromocytoma/paraganglioma syndrome 5 (0.790); dilated cardiomyopathy 1GG (0.768); neurodegeneration with ataxia and late-onset optic atrophy (0.761); gastrointestinal stromal tumor (0.743)
- **Europe PMC papers**: 12756
- **Why important**: SDHA is strongly connected within the module and is tissue-enhanced in heart and skeletal muscle, making it especially relevant to a heart-lung module with a metabolically active profile. It encodes a catalytic component of the respiratory chain and supports succinate metabolism and electron transport. Its associations include respiratory-chain deficiency, Leigh syndrome, pheochromocytoma or paraganglioma syndrome, and dilated cardiomyopathy, with extensive literature support.
- **Conclusion**: Established evidence identifies SDHA as a core respiratory and energy-metabolism gene and provides a direct rationale for the module's mitochondrial interpretation. Its inclusion is compatible with a cardiac energy-demand program, but the co-abundance data alone do not establish that SDHA drives the module.

#### CRAT

- **Related proteins** (co-abundance neighbors): IMMT (0.86), AIFM1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in heart, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carnitine O-acetyltransferase. This gene encodes carnitine O-acetyltransferase, a member of the carnitine acyltransferase family and a key metabolic pathway enzyme which plays an important role in energy homeostasis and fat metabolism. This enzyme catalyzes the reversible transfer of acyl groups from an acyl-CoA thioester to carnitine and regulates the ratio of acyl-CoA/CoA. It is found in both the mitochondria and the peroxiso…
- **Diseases (Open Targets)**: neurodegeneration with brain iron accumulation 8 (0.499); neurodegeneration with brain iron accumulation (0.341); neurodegenerative disease (0.301); Alzheimer disease (0.252); lysosomal storage disease (0.247)
- **Europe PMC papers**: 4594
- **Why important**: CRAT connects to AIFM1 and IMMT and contributes a complementary fuel-management function rather than simply duplicating respiratory-chain annotation. It catalyzes reversible acyl-group transfer to carnitine, regulates the acyl-CoA to CoA balance, and participates in fatty-acid and branched-chain substrate metabolism. Its tissue profile includes skeletal muscle and tongue, and its disease associations include neurodegenerative and lysosomal-storage conditions.
- **Conclusion**: Established evidence supports CRAT as a metabolic-flexibility and acyl-group-buffering enzyme. Its network placement suggests a possible bridge between mitochondrial architecture, respiratory activity, and substrate utilization, but that bridge remains a hypothesis because neither STRING nor hu.MAP confirms a shared complex.

#### SLC25A12

- **Related proteins** (co-abundance neighbors): SDHA (0.83), AIFM1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in heart, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 25 member 12. This gene encodes a calcium-binding mitochondrial carrier protein. The encoded protein localizes to the mitochondria and is involved in the exchange of aspartate for glutamate across the inner mitochondrial membrane. Polymorphisms in this gene may be associated with autism, and mutations in this gene may also be a cause of global cerebral hypomyelination. Alternatively spliced transcript variants …
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 39 (0.799); hereditary disease (0.416); Global developmental delay (0.370); developmental and epileptic encephalopathy, 1 (0.274); X-linked spasticity-intellectual disability-epilepsy syndrome (0.266)
- **Europe PMC papers**: 992
- **Why important**: SLC25A12 is connected to SDHA and AIFM1 and contributes a transport and redox-coupling function. It encodes a calcium-binding mitochondrial carrier involved in aspartate-glutamate exchange, the malate-aspartate shuttle, and calcium responses. It is associated with developmental and epileptic encephalopathy and global developmental delay, and its HPA profile includes skeletal muscle and myonuclei as well as neural cell types.
- **Conclusion**: Established evidence supports SLC25A12 as a carrier that can couple mitochondrial substrate exchange with redox metabolism and calcium-sensitive physiology. Its presence supports a coordinated metabolic interpretation, while any direct role in linking the other module genes is a hypothesis.

#### IMMT

- **Related proteins** (co-abundance neighbors): CRAT (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inner membrane mitochondrial protein. Enables RNA binding activity. Involved in cristae formation. Located in mitochondrial inner membrane. Part of MICOS complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); multinodular goiter (0.196); alcohol drinking (0.190); breast cancer (0.094); neoplasm (0.087)
- **Europe PMC papers**: 933
- **Why important**: IMMT is the least connected node in the co-abundance subgraph but is biologically distinctive because it encodes MICOS component MIC sixty and participates in cristae formation and inner-membrane organization. It provides structural context for the respiratory and transport genes and is detected in both heart and lung. Its disease and literature associations are less extensive than those of SDHA or AIFM1, but its architectural function is highly relevant to the inferred module.
- **Conclusion**: Established evidence supports IMMT as an inner-membrane and cristae-organization factor. Its presence suggests that the module may reflect coordinated mitochondrial structure and function rather than metabolism alone, but this structural integration is a hypothesis not validated by a hu.MAP complex or STRING interaction.

## Module 2

**Tissue pair**: heart and lung  
**Genes (9)**: HSPA5, CLIC1, GANAB, HSP90AA1, HSPA8, PKM, LDHA, RAN, XRCC6

### Function

The strongest interpretation is a conserved intracellular proteostasis and stress-response module with links to endoplasmic-reticulum protein folding, antigen processing, and cytosolic protein quality control. The primary evidence is the enrichment of melanosome and pigment-granule terms (GO:CC melanosome; q_global = 0.00902)(GO:CC pigment granule; q_global = 0.00902), MHC class II protein complex binding and MHC protein complex binding (GO:MF MHC class II protein complex binding; q_global = 0.019)(GO:MF MHC protein complex binding; q_global = 0.0386), antigen processing and presentation (KEGG Antigen processing and presentation - Homo sapiens (human); q_global = 0.019), and protein processing in the endoplasmic reticulum (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.037). These terms converge particularly on HSPA5, HSPA8, HSP90AA1, and GANAB. Cadherin binding (GO:MF cadherin binding; q_global = 0.0275) is also supported, but is less specific mechanistically because it includes the glycolytic genes LDHA and PKM and the broadly functioning genes CLIC1 and RAN. The module therefore appears to represent coordinated chaperone activity, ER quality control, stress-associated intracellular trafficking, and metabolic support rather than a narrowly specialized heart- or lung-specific pathway.

**Cell composition.** The module is dominated by broadly expressed intracellular proteins: HPA assigns low tissue specificity to most members, and all members have low immune-cell specificity. HPA does not show an enriched blood-cell category, so the module is not strongly supported as a blood-cell contamination signature. The HPA summary does identify two secreted genes, although the individual annotations mainly place the proteins in intracellular, membrane, ER, cytosolic, nucleoplasmic, or vesicular compartments rather than describing a conventional plasma-protein module. Several genes have enhanced expression in selected cell types, including trophoblast, epididymal, megakaryocyte, platelet, epithelial, and germ-cell populations. Thus, shared cellular composition or general cellular stress may contribute to the heart-lung co-abundance pattern. Protein detection in both heart and lung is especially supportive for HSPA5, HSPA8, XRCC6, CLIC1, and PKM; GANAB and LDHA are detected in lung but not heart, while HSP90AA1 is not detected in either tissue by the cited HPA IHC summary.

**GO/KEGG enrichment**: 7 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC melanosome | 0.00902 | GANAB, HSP90AA1, HSPA5, HSPA8, RAN |
| GO:CC pigment granule | 0.00902 | GANAB, HSP90AA1, HSPA5, HSPA8, RAN |
| GO:MF MHC class II protein complex binding | 0.019 | HSP90AA1, HSPA8, PKM |
| KEGG Antigen processing and presentation - Homo sapiens (human) | 0.019 | HSP90AA1, HSPA5, HSPA8 |
| GO:MF cadherin binding | 0.0275 | CLIC1, HSPA5, HSPA8, LDHA, PKM, RAN |
| KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human) | 0.037 | GANAB, HSP90AA1, HSPA5, HSPA8 |
| GO:MF MHC protein complex binding | 0.0386 | HSP90AA1, HSPA8, PKM |

### STRING and hu.MAP

STRING supports a compact, established chaperone relationship centered on HSP90AA1, HSPA5, and HSPA8, with an additional GANAB-HSPA5 relationship. It also supports the metabolic enzyme pair LDHA-PKM. These are biologically coherent known relationships and explain much of the module's functional signal. The remaining co-abundance edges do not have high-confidence STRING support in the supplied results, including relationships involving RAN, XRCC6, and CLIC1. The STRING tissue enrichments (15 supplementary STRING terms; within-query FDR 0.0002–0.00095) repeatedly point to respiratory, lymphoid, cancer-associated, reproductive, and gastrointestinal contexts, but they are supplementary and do not replace the globally corrected GO or KEGG evidence. No hu.MAP complex contains multiple module members. Consequently, the module is not equivalent to one established physical complex; it combines a known chaperone subnetwork, a known glycolytic pair, and additional co-abundance relationships that may reflect shared state or cellular context.

**STRING interactions (score >= 0.7)**: 5 of 36 gene pairs: GANAB–HSPA5 (0.846); HSP90AA1–HSPA5 (0.968); HSP90AA1–HSPA8 (0.999); HSPA5–HSPA8 (0.983); LDHA–PKM (0.997)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Cervical carcinoma cell (FDR = 0.0002, 6 genes); TISSUES Leukemia cell (FDR = 0.00021, 8 genes); TISSUES Trunk (FDR = 0.00021, 8 genes); TISSUES Internal male genital organ (FDR = 0.00028, 9 genes); TISSUES Male reproductive gland (FDR = 0.00075, 9 genes); TISSUES Lymphoblast (FDR = 0.00075, 6 genes); TISSUES Respiratory system (FDR = 0.00086, 9 genes); TISSUES Lymphocytic leukemia cell (FDR = 0.00086, 5 genes); TISSUES Testis (FDR = 0.00086, 8 genes); TISSUES Thymus (FDR = 0.00086, 5 genes); TISSUES Gastrointestinal tract (FDR = 0.0009, 9 genes); TISSUES Bone marrow cancer cell (FDR = 0.0009, 5 genes); TISSUES Melanoma cell line (FDR = 0.0009, 5 genes); TISSUES Chronic lymphocytic leukemia cell (FDR = 0.0009, 4 genes); TISSUES Ascites (FDR = 0.00095, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be claimed as wholly novel at the level of individual biology: the chaperone links among HSP90AA1, HSPA5, and HSPA8 and the glycolytic LDHA-PKM relationship are already represented in STRING, and the functions of the component genes are well established. At the same time, the specific conserved heart-lung co-abundance organization may be a new systems-level observation because no multi-member hu.MAP complex is reported and several module edges lack corresponding high-confidence STRING relationships. This is evidence for a potentially novel tissue-pair association, not proof of a new physical pathway. Demonstrating novelty would require comparison with prior heart-lung co-expression studies, independent cohorts, and experimental validation of the noncanonical edges.

**Hypothesis.** Hypothesis: the module reflects a shared cellular adaptation in heart and lung in which ER and cytosolic chaperones coordinate folding, trafficking, and stress management while glycolytic enzymes provide metabolic support. HSPA5 and GANAB could couple ER protein maturation and glycan quality control, with HSP90AA1 and HSPA8 extending proteostasis control to cytosolic client proteins. RAN and XRCC6 may connect this state to nuclear transport, DNA repair, and stress-responsive cell maintenance, while CLIC1, LDHA, and PKM may reflect redox, ion-homeostatic, and glycolytic demands. The antigen-processing and MHC-binding enrichments may indicate stress-related handling or presentation of protein products rather than a dedicated immune-cell module. This model is mechanistic and testable, but the co-abundance data alone do not establish physical interactions or causal direction.

### Important genes

#### HSPA5

- **Related proteins** (co-abundance neighbors): XRCC6 (0.82), GANAB (0.81), HSPA8 (0.81); STRING partners: GANAB (0.846), HSP90AA1 (0.968), HSPA8 (0.983)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in heart, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is the central integrator of the module's strongest functional themes: it participates in the globally supported melanosome and pigment-granule terms (GO:CC melanosome; q_global = 0.00902)(GO:CC pigment granule; q_global = 0.00902), antigen processing and presentation (KEGG Antigen processing and presentation - Homo sapiens (human); q_global = 0.019), cadherin binding (GO:MF cadherin binding; q_global = 0.0275), and ER protein processing (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.037). Its STRING links to GANAB, HSP90AA1, and HSPA8 form the clearest chaperone-centered part of the network. HPA detects it in both heart and lung, and its established ER chaperone and unfolded-protein-response functions make it biologically important despite its broad expression and substantial literature volume.
- **Conclusion**: Established evidence supports HSPA5 as a core ER proteostasis and stress-response component of the module. It is plausible, but not demonstrated, that HSPA5 coordinates the heart-lung module's antigen processing and broader stress-associated co-abundance.

#### HSP90AA1

- **Related proteins** (co-abundance neighbors): GANAB (0.84), CLIC1 (0.82); STRING partners: HSPA5 (0.968), HSPA8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein 90 alpha family class A member 1. The protein encoded by this gene is an inducible molecular chaperone that functions as a homodimer. The encoded protein aids in the proper folding of specific target proteins by use of an ATPase activity that is modulated by co-chaperones. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: cancer (0.643); plasma cell myeloma (0.404); non-small cell lung carcinoma (0.394); dengue disease (0.375); Orthomyxoviridae infectious disease (0.375)
- **Europe PMC papers**: 8215
- **Why important**: HSP90AA1 has the broadest enrichment coverage among the chaperone genes, appearing in (GO:CC melanosome; q_global = 0.00902), (GO:CC pigment granule; q_global = 0.00902), (GO:MF MHC class II protein complex binding; q_global = 0.019), (KEGG Antigen processing and presentation - Homo sapiens (human); q_global = 0.019), (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.037), and (GO:MF MHC protein complex binding; q_global = 0.0386). It has very strong STRING relationships with HSPA5 and HSPA8, and its established role as an inducible ATP-dependent molecular chaperone provides a direct functional explanation for the proteostasis and MHC-binding signals. It also has substantial disease and literature associations, including cancer, lung carcinoma, and antiviral defense contexts.
- **Conclusion**: Established evidence supports HSP90AA1 as a major chaperone hub and functional anchor of the module. Its lack of HPA IHC detection in the supplied heart and lung summary cautions against interpreting it as a simple abundance marker of the dominant tissue cells. Its specific causal role in this co-abundance module remains hypothetical.

#### HSPA8

- **Related proteins** (co-abundance neighbors): HSPA5 (0.81); STRING partners: HSP90AA1 (0.999), HSPA5 (0.983)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Flagellar centriole, Annulus; IHC detected in heart, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 8. This gene encodes a member of the heat shock protein 70 family, which contains both heat-inducible and constitutively expressed members. This protein belongs to the latter group, which are also referred to as heat-shock cognate proteins. It functions as a chaperone, and binds to nascent polypeptides to facilitate correct folding. It also functions as an ATPase in the disassembly of clathrin-coated…
- **Diseases (Open Targets)**: dengue disease (0.505); systemic lupus erythematosus (0.375); smoking initiation (0.199); Lennox-Gastaut syndrome (0.118); neoplasm (0.105)
- **Europe PMC papers**: 6937
- **Why important**: HSPA8 is the only module member represented in every globally supported enrichment term (7 globally significant GO/KEGG terms, q_global 0.00902–0.0386; see the table). It is strongly connected in STRING to HSP90AA1 and HSPA5, is detected in both heart and lung by HPA, and has established constitutive chaperone, nascent-polypeptide folding, unfolded-protein, and vesicle disassembly functions. Its broad expression and large literature base support a general cellular maintenance role rather than a tissue-restricted function.
- **Conclusion**: Established evidence supports HSPA8 as a pervasive proteostasis and intracellular trafficking component that helps unify the module's enrichment profile. It is a strong candidate for maintaining the shared cellular state, but the data do not show that it drives the module.

#### GANAB

- **Related proteins** (co-abundance neighbors): HSP90AA1 (0.84), XRCC6 (0.84), RAN (0.83), HSPA5 (0.81); STRING partners: HSPA5 (0.846)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glucosidase II alpha subunit. This gene encodes the alpha subunit of glucosidase II and a member of the glycosyl hydrolase 31 family of proteins. The heterodimeric enzyme glucosidase II plays a role in protein folding and quality control by cleaving glucose residues from immature glycoproteins in the endoplasmic reticulum. Expression of the encoded protein is elevated in lung tumor tissue and in response to UV irradiation. Mut…
- **Diseases (Open Targets)**: polycystic kidney disease 3 with or without polycystic liver disease (0.792); autosomal dominant polycystic liver disease (0.515); autosomal dominant polycystic kidney disease (0.470); Biliary tract abnormality (0.438); COVID-19 (0.370)
- **Europe PMC papers**: 1240
- **Why important**: GANAB links the module to ER glycoprotein quality control and N-glycan processing. It contributes to the melanosome and pigment-granule terms (GO:CC melanosome; q_global = 0.00902)(GO:CC pigment granule; q_global = 0.00902) and ER protein processing (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.037), has a known STRING relationship with HSPA5, and occupies a relatively connected position in the co-abundance network. Its established glucosidase II function and association with autosomal-dominant polycystic kidney and liver disease make it particularly informative for interpreting the ER and glycoprotein aspects of the module.
- **Conclusion**: Established evidence supports GANAB as an ER glycan-processing partner of the chaperone component. Its connection to heart-lung co-abundance may indicate coordinated secretory-pathway quality control, but a tissue-pair-specific role is a hypothesis.

#### LDHA

- **Related proteins** (co-abundance neighbors): RAN (0.86), PKM (0.84), CLIC1 (0.82); STRING partners: PKM (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lactate dehydrogenase A. This gene encodes the A subunit of lactate dehydrogenase enzyme which catalyzes the reversible conversion of pyruvate to lactate with the concomitant oxidation of NADH to NAD in anaerobic glycolysis. The protein is found predominantly in skeletal muscle and belongs to the lactate dehydrogenase family. Mutations in this gene have been linked to exertional myoglobinuria. The human genome contains se…
- **Diseases (Open Targets)**: glycogen storage disease due to lactate dehydrogenase M-subunit deficiency (0.755); disorder of glycogen metabolism (0.505); glycogen storage disease XV (0.505); primary hyperoxaluria (0.447); hereditary disease (0.190)
- **Europe PMC papers**: 20747
- **Why important**: LDHA provides the clearest metabolic arm of the module. It is connected to PKM in STRING and in the co-abundance network, appears in cadherin-binding enrichment (GO:MF cadherin binding; q_global = 0.0275), and has an established role in the reversible conversion of pyruvate and lactate during anaerobic glycolysis. It is broadly expressed, detected in lung, and associated with muscle metabolism and exertional myoglobinuria. Its very large literature volume makes its core biochemical function well established.
- **Conclusion**: Established evidence supports LDHA as a glycolytic component that may provide metabolic context for the module. Whether its association with the chaperone network reflects direct coordination, shared cellular stress, or cell-composition effects is unresolved.

#### PKM

- **Related proteins** (co-abundance neighbors): LDHA (0.84); STRING partners: LDHA (0.997)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyruvate kinase M1/2. This gene encodes a protein involved in glycolysis. The encoded protein is a pyruvate kinase that catalyzes the transfer of a phosphoryl group from phosphoenolpyruvate to ADP, generating ATP and pyruvate. This protein has been shown to interact with thyroid hormone and may mediate cellular metabolic effects induced by thyroid hormones. This protein has been found to bind Opa protein, a bacterial o…
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); autoimmune disorder of central nervous system (0.370); tympanic membrane perforation (0.204); neoplasm (0.121); hepatocellular carcinoma (0.120)
- **Europe PMC papers**: 8544
- **Why important**: PKM completes the supported glycolytic pair with LDHA and contributes to the globally corrected MHC class II binding terms (GO:MF MHC class II protein complex binding; q_global = 0.019)(GO:MF MHC protein complex binding; q_global = 0.0386) as well as cadherin binding (GO:MF cadherin binding; q_global = 0.0275). It is tissue-enhanced in skeletal muscle and tongue, detected in both heart and lung, and has established pyruvate-kinase and ATP-producing functions. Its position at the metabolic edge of the network and its disease and cancer associations make it useful for distinguishing a metabolic support signal from a purely chaperone-defined module.
- **Conclusion**: Established evidence supports PKM as the metabolic partner of LDHA and as a contributor to the module's MHC-binding annotation through the supplied enrichment mapping. Its proposed coupling to ER stress and antigen processing is a hypothesis rather than a demonstrated mechanism.

## Module 3

**Tissue pair**: heart and lung  
**Genes (12)**: MTHFD1, CLTC, DYNC1I2, DYNC1H1, HPRT1, PDCD6IP, PSMC4, ADSL, SEPTIN9, USP5, USO1, VPS35

### Function

The strongest interpretation is a conserved intracellular trafficking and microtubule-organizing module. (GO:BP transcytosis; q_global = 0.0137) supports transcytosis through CLTC, USO1, and VPS35, linking clathrin-coated vesicles, Golgi-associated vesicle transport, and retromer-mediated endosomal recycling. (GO:CC microtubule organizing center; q_global = 0.0238) and (GO:CC microtubule cytoskeleton; q_global = 0.0382) support a microtubule-organizing and microtubule-cytoskeletal context involving clathrin, cytoplasmic dynein, PDCD6IP, PSMC4, SEPT9, and USO1. The annotations of the individual genes are concordant: DYNC1H1 and DYNC1I2 support dynein-dependent retrograde transport, CLTC supports endocytosis and intracellular trafficking, USO1 supports endoplasmic-reticulum-to-Golgi transport, VPS35 supports retromer transport, and PDCD6IP supports ESCRT-dependent vesicle formation and cytokinetic abscission. The module therefore most plausibly represents coordinated vesicle handling, intracellular transport, and microtubule-based organization rather than a narrowly tissue-specific biochemical pathway. The purine and proteasome-related genes may reflect cellular maintenance processes, but no corresponding GO/KEGG term is globally supported for those functions in this module.

**Cell composition.** The module is not dominated by plasma proteins, secreted proteins, or blood-cell-enriched genes. HPA classifies all genes as having low immune-cell specificity, and only a single gene is secreted. Most genes have low tissue specificity, while the remaining tissue patterns are distributed across skeletal muscle, liver, brain, and tongue rather than concentrated in a single shared tissue or blood lineage. Protein detection is broad in lung and substantial in heart. Cell-type-enhanced signals occur in diverse populations, including myonuclei, cardiomyocytes, epicardial cells, retinal ganglion cells, epithelial cells, and germ-cell-related populations. This pattern argues against a simple blood-contamination explanation, although broadly expressed intracellular proteins and shared structural or trafficking requirements could contribute to conservation between heart and lung.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP transcytosis | 0.0137 | CLTC, USO1, VPS35 |
| GO:CC microtubule organizing center | 0.0238 | CLTC, DYNC1H1, DYNC1I2, PDCD6IP, PSMC4, USO1 |
| GO:CC microtubule cytoskeleton | 0.0382 | CLTC, DYNC1H1, DYNC1I2, PDCD6IP, PSMC4, SEPTIN9, USO1 |

### STRING and hu.MAP

STRING provides limited direct support for the full module. The strongest known STRING relationships are the ADSL-HPRT1 pair and the DYNC1H1-DYNC1I2 pair; the latter is especially concordant with the microtubule and dynein interpretation. The supplementary STRING cell-division signal is consistent with CLTC, DYNC1H1, PDCD6IP, and SEPT9, but it is not global enrichment evidence. hu.MAP repeatedly places DYNC1H1 and DYNC1I2 together in dynein-related complexes, supporting a known physical-complex relationship. hu.MAP also places CLTC and USO1 together in a large vesicle-trafficking complex, supporting a connection between the trafficking genes. Most other module members lack a reported STRING or hu.MAP relationship in the supplied evidence. Thus, the network contains validated dynein and vesicle-trafficking components, but the complete cross-process module is not already represented as a single well-established interaction complex.

**STRING interactions (score >= 0.7)**: 2 of 66 gene pairs: ADSL–HPRT1 (0.935); DYNC1H1–DYNC1I2 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Cell division (FDR = 0.0458, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02226.1 (DYNC1I2, DYNC1H1; 2/7); huMAP3_08809.1 (DYNC1I2, DYNC1H1; 2/7); huMAP3_09560.1 (DYNC1I2, DYNC1H1; 2/8); huMAP3_07382.1 (DYNC1I2, DYNC1H1; 2/9); huMAP3_08818.1 (DYNC1I2, DYNC1H1; 2/9); huMAP3_09593.1 (DYNC1I2, DYNC1H1; 2/10); huMAP3_15007.1 (DYNC1I2, DYNC1H1; 2/12); huMAP3_11519.1 (DYNC1I2, DYNC1H1; 2/13); huMAP3_09802.1 (DYNC1I2, DYNC1H1; 2/15); huMAP3_15289.1 (DYNC1I2, DYNC1H1; 2/28); huMAP3_12566.1 (DYNC1I2, DYNC1H1; 2/51); huMAP3_12394.1 (USO1, CLTC; 2/98)

### Novelty

This is not established as a wholly new molecular pathway: the dynein pair, the clathrin-associated trafficking context, the USO1-CLTC hu.MAP association, and the ADSL-HPRT1 relationship are already known. However, the conserved heart-lung co-abundance grouping may be a potentially novel systems-level observation because the supplied interaction resources support only selected relationships rather than the complete module. That observation should be described as a candidate novel tissue-pair co-abundance association, not as proof of a new complex or mechanism. Confirmation would require replication in independent heart and lung cohorts, assessment of cell-composition covariates, and testing whether the co-abundance structure persists after controlling for tissue, disease state, and technical effects.

**Hypothesis.** Hypothesis: in shared heart and lung cellular populations, coordinated expression of clathrin, Golgi and retromer machinery, ESCRT-associated factors, and cytoplasmic dynein may support efficient sorting and long-range movement of endosomal or secretory cargo along microtubules. PDCD6IP and CLTC could connect membrane-vesicle formation with cytoskeletal organization, while USO1 and VPS35 could help maintain Golgi-directed and endosome-to-Golgi cargo flow. The accompanying expression of proteostasis and nucleotide-metabolism genes may reflect the biosynthetic and quality-control demands of these active trafficking systems, but that connection remains hypothetical and is not directly established by the globally corrected enrichment results.

### Important genes

#### PDCD6IP

- **Related proteins** (co-abundance neighbors): CLTC (0.87), USP5 (0.85), USO1 (0.82), HPRT1 (0.82), PSMC4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 6 interacting protein. This gene encodes a protein that functions within the ESCRT pathway in the abscission stage of cytokinesis, in intralumenal endosomal vesicle formation, and in enveloped virus budding. Studies using mouse cells have shown that overexpression of this protein can block apoptosis. In addition, the product of this gene binds to the product of the PDCD6 gene, a protein required for apoptosis, in a calc…
- **Diseases (Open Targets)**: HIV infectious disease (0.463); anthrax infection (0.462); alcohol drinking (0.388); autosomal recessive primary microcephaly (0.386); microcephaly 29, primary, autosomal recessive (0.383)
- **Europe PMC papers**: 1668
- **Why important**: PDCD6IP is the strongest network hub in the supplied subgraph and connects CLTC, USP5, USO1, HPRT1, and PSMC4. It appears in (GO:CC microtubule organizing center; q_global = 0.0238), (GO:CC microtubule cytoskeleton; q_global = 0.0382), and the supplementary cell-division term (STRING Keyword Cell division; within-query FDR = 0.0458). Its established functions in ESCRT-dependent cytokinetic abscission, intralumenal vesicle formation, enveloped-virus budding, and membrane-related processes make it a plausible bridge between vesicle biology and cytoskeletal organization. It also has a large literature base and disease associations including primary microcephaly.
- **Conclusion**: Established evidence supports PDCD6IP as a central intracellular vesicle and cytokinesis-associated component of this module. Its hub position makes it a strong candidate for coordinating the module, but a specific heart-lung regulatory role remains a hypothesis.

#### CLTC

- **Related proteins** (co-abundance neighbors): PDCD6IP (0.87), DYNC1H1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in heart, lung
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: clathrin heavy chain. Clathrin is a major protein component of the cytoplasmic face of intracellular organelles, called coated vesicles and coated pits. These specialized organelles are involved in the intracellular trafficking of receptors and endocytosis of a variety of macromolecules.  The basic subunit of the clathrin coat is composed of three heavy chains and three light chains. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: intellectual disability, autosomal dominant 56 (0.787); cancer (0.576); hereditary disease (0.540); Alzheimer disease (0.466); neurodegenerative disease (0.465)
- **Europe PMC papers**: 2902
- **Why important**: CLTC is present in every primary enrichment term, (GO:BP transcytosis; q_global = 0.0137), (GO:CC microtubule organizing center; q_global = 0.0238), and (GO:CC microtubule cytoskeleton; q_global = 0.0382), and connects PDCD6IP with DYNC1H1 in the module. It is a major component of coated vesicles and coated pits, with established roles in receptor-mediated endocytosis, intracellular transport, mitotic spindle organization, and chromosome segregation. It is detected in both heart and lung and has substantial disease and literature support.
- **Conclusion**: Established evidence identifies CLTC as a core vesicle-trafficking and microtubule-associated component. Its position suggests that it could link membrane cargo capture to cytoskeletal transport, but the co-abundance data alone do not establish directionality or causal control.

#### DYNC1H1

- **Related proteins** (co-abundance neighbors): CLTC (0.80); STRING partners: DYNC1I2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, lung
- **hu.MAP 3.0**: huMAP3_02226.1, huMAP3_08809.1, huMAP3_09560.1, huMAP3_07382.1, huMAP3_08818.1, huMAP3_09593.1, huMAP3_15007.1, huMAP3_11519.1, huMAP3_09802.1, huMAP3_15289.1, huMAP3_12566.1
- **Function (MyGene.info)**: dynein cytoplasmic 1 heavy chain 1. Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polyp…
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy without contractures (0.816); intellectual disability, autosomal dominant 13 (0.815); Charcot-Marie-Tooth disease axonal type 2O (0.799); autosomal dominant non-syndromic intellectual disability (0.634); hereditary disease (0.545)
- **Europe PMC papers**: 1731
- **Why important**: DYNC1H1 is the cytoplasmic dynein heavy chain and is directly paired with DYNC1I2 by a very strong STRING relationship. Both genes occur together across the supplied hu.MAP dynein-related complexes. DYNC1H1 contributes to (GO:CC microtubule organizing center; q_global = 0.0238), (GO:CC microtubule cytoskeleton; q_global = 0.0382), and (STRING Keyword Cell division; within-query FDR = 0.0458), and its established functions include microtubule-based movement, organelle transport, retrograde transport, spindle organization, and nuclear migration. It has important associations with motor-neuron, neurodevelopmental, and peripheral-nerve disorders.
- **Conclusion**: Established evidence supports DYNC1H1 as the motor component that gives the module a microtubule-transport interpretation. Its conserved co-abundance with DYNC1I2 is stronger than the evidence for most other module relationships, while its exact cargo in heart and lung remains unknown.

#### DYNC1I2

- **Related proteins** (co-abundance neighbors): PSMC4 (0.84); STRING partners: DYNC1H1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Microtubules, Centrosome, Cytosol, Flagellar centriole, Mid piece, Principal piece; IHC detected in heart, lung
- **hu.MAP 3.0**: huMAP3_02226.1, huMAP3_08809.1, huMAP3_09560.1, huMAP3_07382.1, huMAP3_08818.1, huMAP3_09593.1, huMAP3_15007.1, huMAP3_11519.1, huMAP3_09802.1, huMAP3_15289.1, huMAP3_12566.1
- **Function (MyGene.info)**: dynein cytoplasmic 1 intermediate chain 2. This gene encodes a member of the dynein intermediate chain family. The encoded protein is a non-catalytic component of the cytoplasmic dynein 1 complex, which acts as a retrograde microtubule motor to transport organelles and vesicles. A pseudogene of this gene is located on chromosome 10. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly and structural brain anomalies (0.698); neurodegenerative disease (0.484); viral infectious disease (0.462); lysosomal storage disease (0.432); neurodevelopmental disorder with microcephaly, hypotonia, and variable brain anomalies (0.425)
- **Europe PMC papers**: 407
- **Why important**: DYNC1I2 is the dynein intermediate chain and forms the module's clearest known physical relationship with DYNC1H1 in STRING. It appears in (GO:CC microtubule organizing center; q_global = 0.0238) and (GO:CC microtubule cytoskeleton; q_global = 0.0382) and in the full set of supplied hu.MAP complexes containing the dynein pair. Its established role in the cytoplasmic dynein complex supports transport along microtubules, organelle movement, and spindle-related processes. HPA detects it in both heart and lung with low tissue and cell-type specificity.
- **Conclusion**: Established evidence supports DYNC1I2 as a structural dynein component that reinforces the module's transport identity. Its broad detection is compatible with a shared housekeeping transport program, but the module does not prove a tissue-specific dynein function.

#### USO1

- **Related proteins** (co-abundance neighbors): PDCD6IP (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: USO1 vesicle transport factor. The protein encoded by this gene is a peripheral membrane protein which recycles between the cytosol and the Golgi apparatus during interphase. It is regulated by phosphorylation: dephosphorylated protein associates with the Golgi membrane and dissociates from the membrane upon phosphorylation. Ras-associated protein 1 recruits this protein to coat protein complex II (COPII) vesicles during buddin…
- **Diseases (Open Targets)**: psoriatic arthritis (0.184); bipolar disorder (0.150); retinitis pigmentosa (0.085); cone dystrophy (0.076); cone-rod dystrophy (0.076)
- **Europe PMC papers**: 546
- **Why important**: USO1 occurs in all primary enrichment terms, (GO:BP transcytosis; q_global = 0.0137), (GO:CC microtubule organizing center; q_global = 0.0238), and (GO:CC microtubule cytoskeleton; q_global = 0.0382), and connects to PDCD6IP in the module. It is a Golgi-associated vesicle transport factor involved in COPII vesicle recruitment, endoplasmic-reticulum-to-Golgi transport, vesicle fusion, and transcytosis. It also shares a hu.MAP vesicle-trafficking complex with CLTC. Its tissue-enhanced skeletal-muscle pattern and myonuclear enhancement provide a possible connection to the muscle-rich heart context, while lung protein detection supports its presence in both tissues.
- **Conclusion**: Established evidence supports USO1 as a Golgi and secretory-trafficking component that complements the clathrin and dynein signals. A role in a conserved heart-lung cargo-trafficking program is plausible but remains hypothetical.

#### VPS35

- **Related proteins** (co-abundance neighbors): USP5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in heart, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS35 retromer complex component. This gene belongs to a group of vacuolar protein sorting (VPS) genes. The encoded protein is a component of a large multimeric complex, termed the retromer complex, involved in retrograde transport of proteins from endosomes to the trans-Golgi network. The close structural similarity between the yeast and human proteins that make up this complex suggests a similarity in function. Expression studie…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.743); neurodegenerative disease (0.553); young-onset Parkinson disease (0.503); Parkinson disease (0.482); Parkinson disease, dominant (0.370)
- **Europe PMC papers**: 3611
- **Why important**: VPS35 is one of the genes supporting (GO:BP transcytosis; q_global = 0.0137) and is connected to USP5 in the module. It is a core retromer component involved in endosome-to-Golgi retrograde transport, lysosome organization, and protein trafficking. Its detection in both heart and lung and its strong association with Parkinson disease and other neurodegenerative conditions make it biologically important for cellular cargo recycling and proteostasis, even though it has limited direct connectivity in this subgraph.
- **Conclusion**: Established evidence supports VPS35 as the retromer component of the module and strengthens the transcytosis and intracellular-sorting interpretation. Its low network degree means it is not a topological hub here, but it may represent a functionally important process component whose co-abundance is not captured by many direct edges.

## Module 4

**Tissue pair**: heart and lung  
**Genes (22)**: EIF3L, HNRNPH1, HNRNPK, HNRNPL, MATR3, OLA1, PFKP, PSMC6, PSMC2, PSMA1, PSMD13, ATIC, RUVBL2, FARSB, KARS1, QARS1, RARS1, CCT5, CCT3, CCT7, CCT8, XPO1

### Function

The module is best interpreted as a conserved intracellular proteostasis and RNA–nucleoprotein maintenance program. Its strongest primary evidence is enrichment for intracellular protein-containing complexes (GO:CC intracellular protein-containing complex; q_global = 7.29e-07), the CCT chaperonin complex (GO:CC chaperonin-containing T-complex; q_global = 0.00409), protein-folding chaperone complexes (GO:CC protein folding chaperone complex; q_global = 0.00588), ATP binding and ATP hydrolysis (GO:MF ATP binding; q_global = 0.00118) (GO:MF ATP hydrolysis activity; q_global = 0.00359), RNA localization and nuclear-body localization (12 globally significant GO/KEGG terms, q_global 0.000257–0.00486; see the table), nucleic-acid and gene-expression processes (4 globally significant GO/KEGG terms, q_global 0.00606–0.044; see the table), and ubiquitin-dependent proteasomal catabolism (5 globally significant GO/KEGG terms, q_global 0.0294–0.0322; see the table). The CCT subunits CCT3, CCT5, CCT7 and CCT8 form the clearest functional core, while the proteasome genes PSMA1, PSMC2, PSMC6 and PSMD13 provide a protein-quality-control arm. RUVBL2 connects the chaperone-centered structure to ATP-dependent nucleic-acid, chromosome and telomere-related processes (11 globally significant GO/KEGG terms, q_global 0.00102–0.0145; see the table). The telomere and Cajal-body annotations are statistically supported, but they should be interpreted as pathway-level evidence rather than proof that this module directly controls telomerase in heart or lung. The sperm-recognition and fertilization terms (4 globally significant GO/KEGG terms, q_global 0.0145–0.0337; see the table) are likely driven by the same CCT subunits and are not a compelling tissue-specific biological interpretation.

**Cell composition.** This is not predominantly a plasma-protein, secreted-protein or blood-cell module. HPA reports low immune-cell specificity for every module gene and no enriched blood-cell category, arguing against a simple blood-contamination explanation. The genes are mostly broadly expressed intracellular proteins with low tissue specificity; the heart and lung protein-detection evidence is generally strong, although several individual genes are not detected in one of the two tissues. One module gene is classified as secreted, so the module is not absolutely devoid of secretome annotation, but it is overwhelmingly composed of cytosolic or nuclear machinery rather than circulating proteins. Cell-type-enhanced annotations are frequent for germ-cell populations, microglia, ciliated cells and a few other specialized populations. These annotations may reflect shared cellular programs or annotation breadth, but they do not establish that the heart–lung module is driven by those cell types. The overall composition is most consistent with a broadly expressed housekeeping and proteostasis program that is detectable in both tissues.

**GO/KEGG enrichment**: 59 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC intracellular protein-containing complex | 7.29e-07 | CCT3, CCT5, CCT7, CCT8, KARS1, PSMA1, PSMC2, PSMC6, PSMD13, QARS1, RARS1, RUVBL2 |
| GO:BP RNA localization to Cajal body | 0.000257 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP telomerase RNA localization to Cajal body | 0.000257 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP telomerase RNA localization | 0.000257 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP RNA localization to nucleus | 0.000257 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP regulation of telomere maintenance | 0.00102 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP positive regulation of telomere maintenance | 0.00102 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:MF ATP binding | 0.00118 | CCT3, CCT5, CCT7, CCT8, FARSB, KARS1, OLA1, PFKP, PSMC2, PSMC6, QARS1, RARS1, RUVBL2 |
| GO:MF adenyl ribonucleotide binding | 0.00118 | CCT3, CCT5, CCT7, CCT8, FARSB, KARS1, OLA1, PFKP, PSMC2, PSMC6, QARS1, RARS1, RUVBL2 |
| GO:BP telomere maintenance | 0.00272 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP regulation of chromosome organization | 0.00272 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP positive regulation of chromosome organization | 0.00272 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:MF ATP hydrolysis activity | 0.00359 | CCT3, CCT5, CCT7, CCT8, OLA1, PSMC2, PSMC6, RUVBL2 |
| GO:CC chaperonin-containing T-complex | 0.00409 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 0.00409 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING supports several established physical or functional blocks. The CCT3–CCT5–CCT7–CCT8 relationships are exceptionally strong and agree with the CCT chaperonin annotation (5 supplementary STRING terms; within-query FDR 0.00029–0.0026). PSMA1, PSMC2, PSMC6 and PSMD13 form a coherent proteasome block, supported by their dense STRING relationships and the proteasomal catabolism terms (4 globally significant GO/KEGG terms, q_global 0.0294–0.0294; see the table). HNRNPH1, HNRNPK, HNRNPL and MATR3 form an RNA-binding and nuclear RNA-processing block, consistent with the RNA and gene-expression terms (6 globally significant GO/KEGG terms, q_global 0.00606–0.044; see the table). KARS1, QARS1 and RARS1 form an aminoacyl-tRNA-synthetase block, with FARSB and OLA1 providing additional links. hu.MAP independently recovers the CCT complex (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), proteasome complexes (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) (hu.MAP huMAP3_05064.1), aminoacyl-tRNA-synthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), and hnRNP or nuclear RNA complexes (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_14523.1). Thus, much of the module is a convergence of already known complexes rather than a collection of unexplained pairwise interactions. Some module edges, particularly links between these blocks, are not represented by high-confidence STRING interactions or hu.MAP complexes; they may reflect coordinated abundance, shared regulation, or indirect cellular coupling rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 32 of 231 gene pairs: ATIC–CCT7 (0.881); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT3–RUVBL2 (0.766); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT5–RUVBL2 (0.705); CCT7–CCT8 (0.999); CCT7–RUVBL2 (0.802); CCT8–PSMA1 (0.797); CCT8–PSMC2 (0.733); CCT8–RUVBL2 (0.776); FARSB–KARS1 (0.813); FARSB–OLA1 (0.702); FARSB–RARS1 (0.706); HNRNPH1–HNRNPK (0.975); HNRNPH1–HNRNPL (0.982); HNRNPH1–MATR3 (0.911); HNRNPK–HNRNPL (0.99); HNRNPK–MATR3 (0.923); HNRNPL–MATR3 (0.757); KARS1–QARS1 (0.999); KARS1–RARS1 (0.999); OLA1–RARS1 (0.747); PSMA1–PSMC2 (0.999); PSMA1–PSMC6 (0.999); PSMA1–PSMD13 (0.999); PSMC2–PSMC6 (0.999); PSMC2–PSMD13 (0.999); PSMC6–PSMD13 (0.999); QARS1–RARS1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword ATP-binding (FDR = 0.00029, 13 genes); TISSUES Lymphoblast (FDR = 0.0007, 10 genes); Function ATP binding (FDR = 0.0009, 13 genes); Function ATP hydrolysis activity (FDR = 0.0009, 8 genes); Function Organic cyclic compound binding (FDR = 0.0009, 20 genes); Function Heterocyclic compound binding (FDR = 0.0009, 20 genes); RCTM Metabolism of proteins (FDR = 0.0011, 14 genes); RCTM Metabolism of RNA (FDR = 0.0011, 8 genes); TISSUES Brain (FDR = 0.0012, 22 genes); TISSUES Lymphocyte (FDR = 0.0017, 11 genes); Function Nucleic acid binding (FDR = 0.0025, 13 genes); Function Carbohydrate derivative binding (FDR = 0.0026, 14 genes); Function RNA binding (FDR = 0.0032, 12 genes); TISSUES Testis (FDR = 0.0035, 13 genes); TISSUES Internal male genital organ (FDR = 0.0037, 14 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_09656.1 (PSMA1, PSMC2, PSMC6, PSMD13; 4/64); huMAP3_13725.1 (PSMA1, PSMC2, PSMC6, PSMD13; 4/69); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_02637.1 (QARS1, RARS1, KARS1; 3/14); huMAP3_13688.1 (QARS1, RARS1, KARS1; 3/14); huMAP3_05064.1 (PSMC2, PSMC6, PSMD13; 3/31); huMAP3_10625.1 (HNRNPL, MATR3, HNRNPK; 3/57); huMAP3_05721.1 (HNRNPL, MATR3; 2/6); huMAP3_07581.1 (HNRNPL, MATR3; 2/21); huMAP3_10659.1 (HNRNPL, HNRNPK; 2/28); huMAP3_14523.1 (HNRNPH1, HNRNPK; 2/33); huMAP3_14442.1 (ATIC, OLA1; 2/57)

### Novelty

The module is unlikely to represent a wholly new molecular complex: its central substructures are established CCT, proteasome, aminoacyl-tRNA-synthetase and hnRNP machinery, and several are independently recovered by STRING and hu.MAP. Its potentially novel aspect is the reproducible co-abundance of these otherwise distinct machinery blocks across heart and lung, especially the coupling of chaperoning, proteasomal turnover, RNA handling, translation support and RUVBL2-linked nuclear maintenance. That interpretation remains a hypothesis about cross-complex coordination, not proof of a newly discovered physical assembly. Absence of hu.MAP or STRING support for individual genes such as XPO1 or EIF3L does not establish novelty, because co-abundance can arise from shared regulation, cell composition or condition-dependent interactions. The appropriate claim is therefore a conserved cross-tissue co-abundance state built largely from known complexes, with possible novelty in its tissue-pair-level organization.

**Hypothesis.** Hypothesis: in both heart and lung, cellular demand for synthesis, folding, trafficking and removal of proteins is coordinated with nuclear RNA processing and genome-maintenance functions. The CCT chaperonin core may support folding of newly made proteins, the aminoacyl-tRNA synthetases and translation-associated genes may sustain protein production, and the proteasome components may remove damaged or surplus proteins. In parallel, hnRNP proteins and XPO1 may coordinate RNA processing and nuclear transport, while RUVBL2 may couple ATP-dependent remodeling to telomere and DNA-maintenance programs. The shared abundance pattern could therefore represent a general stress-buffering or high-throughput proteostasis state common to cardiopulmonary tissues. This should be tested by perturbing CCT or proteasome activity and measuring RNA localization, protein turnover, RUVBL2-dependent nuclear functions and tissue-specific phenotypes; the co-abundance data alone do not establish directionality or direct molecular coupling.

### Important genes

#### CCT7

- **Related proteins** (co-abundance neighbors): CCT8 (0.92), CCT3 (0.90), CCT5 (0.88), PSMD13 (0.88), RUVBL2 (0.88), ATIC (0.86), MATR3 (0.85), HNRNPH1 (0.85), RARS1 (0.84), XPO1 (0.84), PSMA1 (0.83), OLA1 (0.83); STRING partners: ATIC (0.881), CCT3 (0.999), CCT5 (0.999), CCT8 (0.999), RUVBL2 (0.802)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, lung
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is a highly central node in the module and connects the other CCT subunits with RUVBL2, ATIC, MATR3, PSMD13 and RNA-related components. It participates in the strongly supported CCT chaperonin and intracellular-complex evidence (GO:CC intracellular protein-containing complex; q_global = 7.29e-07) (GO:CC chaperonin-containing T-complex; q_global = 0.00409) (GO:CC protein folding chaperone complex; q_global = 0.00588), as well as the Cajal-body, telomerase-RNA and telomere annotations (9 globally significant GO/KEGG terms, q_global 0.000257–0.00272; see the table). MyGene.info describes its established role in ATP-dependent folding of proteins including actin and tubulin. It has substantial literature coverage and disease associations including hereditary sensory and autonomic neuropathy, neurodegenerative disease and myocardial infarction in Open Targets.
- **Conclusion**: Established evidence supports CCT7 as a core molecular-chaperone component and a major structural anchor of this module. Its centrality makes it a strong marker of the module, but the co-abundance data do not prove that CCT7 drives the heart–lung program or directly regulates telomerase. A plausible hypothesis is that CCT7 helps coordinate proteostasis with nuclear maintenance through its associations with the other module blocks.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): PSMC2 (0.88), CCT7 (0.88), CCT8 (0.87), CCT5 (0.84), EIF3L (0.82), RARS1 (0.82), CCT3 (0.81); STRING partners: CCT3 (0.766), CCT5 (0.705), CCT7 (0.802), CCT8 (0.776)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 is a central connector between the CCT group, PSMC2, EIF3L and RARS1. It contributes to the primary enrichment for telomere maintenance, chromosome organization, DNA metabolic processes, RNA localization and ATP-dependent activity (12 globally significant GO/KEGG terms, q_global 0.00102–0.0145; see the table). MyGene.info describes ATPase and DNA-helicase-related functions, DNA repair, recombination and telomere maintenance. Its cell-type annotations include respiratory ciliated cells as well as germ-cell populations, and it has substantial literature coverage and disease associations involving hypogonadotropic hypogonadism and neoplasia.
- **Conclusion**: Established evidence supports RUVBL2 as an ATP-dependent nuclear and chromatin-associated factor that broadens the module beyond generic protein folding. The module supports coordinated abundance with CCT and proteasome machinery, but not a direct RUVBL2-mediated bridge between those complexes. The respiratory-ciliated-cell annotation makes a cardiopulmonary connection plausible, yet this remains a hypothesis requiring tissue-specific validation.

#### XPO1

- **Related proteins** (co-abundance neighbors): OLA1 (0.86), HNRNPK (0.85), CCT5 (0.85), CCT8 (0.85), CCT7 (0.84), ATIC (0.83), CCT3 (0.82), PFKP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in heart, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exportin 1. This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSe…
- **Diseases (Open Targets)**: plasma cell myeloma (0.642); B-cell chronic lymphocytic leukemia (0.626); diffuse large B-cell lymphoma (0.602); HIV infectious disease (0.561); neurodegenerative disease (0.522)
- **Europe PMC papers**: 5357
- **Why important**: XPO1 is a network connector linking CCT genes, HNRNPK, OLA1, ATIC and PFKP, despite having no listed high-confidence STRING interaction and no hu.MAP complex assignment. It contributes to RNA localization, gene expression, nuclear-lumen, protein-catabolism and ribonucleoprotein evidence (13 globally significant GO/KEGG terms, q_global 0.00486–0.0446; see the table). MyGene.info identifies it as exportin one, a mediator of nuclear export of RNA and proteins. It has extensive literature coverage and disease associations spanning hematologic malignancy, HIV and neurodegenerative disease.
- **Conclusion**: Established evidence supports XPO1 as a nuclear-export factor that could functionally connect RNA handling to proteostasis, but its module membership is based on co-abundance rather than known direct interactions with the other genes. It is therefore an important candidate bridge, not evidence of a newly formed complex. A testable hypothesis is that variation in nuclear export helps synchronize the RNA-processing and protein-quality-control arms of the module.

#### PSMC2

- **Related proteins** (co-abundance neighbors): RUVBL2 (0.88), CCT5 (0.86), QARS1 (0.86), KARS1 (0.85), CCT3 (0.84), OLA1 (0.81), RARS1 (0.80); STRING partners: CCT8 (0.733), PSMA1 (0.999), PSMC6 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in heart, lung
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1, huMAP3_05064.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is part of the densely connected proteasome block with PSMA1, PSMC6 and PSMD13 and also links that block to CCT5, CCT3, RUVBL2, OLA1 and several tRNA synthetases. It contributes to intracellular complexes, ATP-dependent activity and ubiquitin-dependent proteasomal catabolism (11 globally significant GO/KEGG terms, q_global 7.29e-07–0.0446; see the table). MyGene.info describes it as an ATPase subunit of the proteasome regulatory particle, with roles in protein degradation and oxidative-stress responses. It has substantial literature coverage and disease associations including plasma-cell myeloma, mantle-cell lymphoma and amyloidosis.
- **Conclusion**: Established evidence supports PSMC2 as a core proteasomal quality-control component and a credible marker of the module's protein-clearance arm. The data support coordination with chaperoning, but do not show that PSMC2 directly regulates CCT or RNA localization. A mechanistic hypothesis is that increased folding demand and increased proteasomal disposal are coupled in the shared heart–lung state.

#### MATR3

- **Related proteins** (co-abundance neighbors): CCT5 (0.89), CCT3 (0.87), CCT7 (0.85), ATIC (0.84), CCT8 (0.82); STRING partners: HNRNPH1 (0.911), HNRNPK (0.923), HNRNPL (0.757)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, lung
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_05721.1, huMAP3_07581.1
- **Function (MyGene.info)**: matrin 3. This gene encodes a nuclear matrix protein, which is proposed to stabilize certain messenger RNA species. Mutations of this gene are associated with distal myopathy 2, which often includes vocal cord and pharyngeal weakness. Alternatively spliced transcript variants, including read-through transcripts composed of the upstream small nucleolar RNA host gene 4 (non-protein coding) and matrin 3 gene s…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.735); distal myopathy with vocal cord weakness (0.569); neurodegenerative disease (0.529); distal myopathy (0.384); hereditary disease (0.193)
- **Europe PMC papers**: 1756
- **Why important**: MATR3 links the CCT-centered portion of the network to the nuclear RNA-binding machinery and is connected in STRING to HNRNPH1, HNRNPK and HNRNPL. It contributes to broad macromolecule and gene-expression evidence (4 globally significant GO/KEGG terms, q_global 0.00858–0.0402; see the table), while hu.MAP places it in several hnRNP-related complexes (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07581.1). MyGene.info describes a nuclear-matrix protein proposed to stabilize messenger RNA, and records associations with distal myopathy and vocal-cord weakness; Open Targets also links it to amyotrophic lateral sclerosis and other neurodegenerative disease. Its literature volume is substantial.
- **Conclusion**: Established evidence supports MATR3 as a nuclear RNA-processing and RNA-stability factor that provides a biologically credible connection between chaperone abundance and RNA metabolism. Its moderate network position does not make it the module hub, but its cross-block role makes it important for interpretation. The hypothesis that MATR3-mediated RNA handling is coordinated with CCT and proteasome activity is plausible but not demonstrated by these data.
