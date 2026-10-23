# Conserved co-abundance modules: lung and myometrium

## Module 0

**Tissue pair**: lung and myometrium  
**Genes (11)**: GOT2, ATP5F1A, ATP5F1B, CS, DDOST, UQCRC1, RAB18, SSR1, SUCLG1, SUCLA2, VDAC2

### Function

This is a mitochondrial oxidative-energy module. The primary, globally corrected evidence supports aerobic respiration (GO:BP aerobic respiration; q_global = 0.00448), mitochondrial matrix localization (GO:CC mitochondrial matrix; q_global = 0.00664), cellular respiration (GO:BP cellular respiration; q_global = 0.00832), oxidation of organic compounds for energy (GO:BP energy derivation by oxidation of organic compounds; q_global = 0.0204), and generation of precursor metabolites and energy (GO:BP generation of precursor metabolites and energy; q_global = 0.0468). The recurring genes ATP5F1A, ATP5F1B, CS, SUCLA2, SUCLG1 and UQCRC1 connect ATP synthase, the tricarboxylic-acid cycle, succinate-CoA ligase, and respiratory electron transport. GOT2 and VDAC2 add links to mitochondrial amino-acid or carbon metabolism and metabolite transport. The co-abundance structure therefore most plausibly reflects coordinated mitochondrial respiratory and biosynthetic capacity rather than a narrowly tissue-specific signaling pathway. The ER-associated DDOST and SSR1 pair, together with RAB18, forms a smaller peripheral component whose relationship to the respiratory core is not established by the primary enrichment results.

**Cell composition.** The module is not dominated by plasma proteins, secreted proteins, or blood-cell markers. No genes are secreted, every gene has low immune-cell specificity, and HPA protein detection is present throughout lung and for most genes in myometrium. HPA tissue patterns emphasize metabolically active tissues, including skeletal muscle, tongue and heart muscle, while several genes have low tissue specificity. Cell-type-enhanced annotations include epithelial, trophoblast, parietal, hepatocyte and related cell types, but there is no blood-cell enrichment. Thus, the shared lung-myometrium signal is more consistent with conserved mitochondrial activity in resident metabolically active cells than with blood contamination. The three genes not detected in myometrium by HPA should be treated as a protein-detection caveat rather than evidence against the co-abundance module.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP aerobic respiration | 0.00448 | ATP5F1A, ATP5F1B, CS, SUCLA2, SUCLG1, UQCRC1 |
| GO:CC mitochondrial matrix | 0.00664 | ATP5F1A, ATP5F1B, CS, GOT2, SUCLA2, SUCLG1, VDAC2 |
| GO:BP cellular respiration | 0.00832 | ATP5F1A, ATP5F1B, CS, SUCLA2, SUCLG1, UQCRC1 |
| GO:BP energy derivation by oxidation of organic compounds | 0.0204 | ATP5F1A, ATP5F1B, CS, SUCLA2, SUCLG1, UQCRC1 |
| GO:BP generation of precursor metabolites and energy | 0.0468 | ATP5F1A, ATP5F1B, CS, SUCLA2, SUCLG1, UQCRC1 |

### STRING and hu.MAP

STRING provides strong, biologically coherent support for the respiratory core. ATP5F1A and ATP5F1B are linked to one another and to CS, UQCRC1, SUCLG1 and VDAC2; CS is linked to GOT2, SUCLA2, SUCLG1 and UQCRC1; and SUCLA2 is linked very strongly to SUCLG1. STRING supplementary enrichment independently points to the TCA cycle, respiratory electron transport, aerobic respiration, mitochondrial matrix and carbon metabolism (6 supplementary STRING terms; within-query FDR 0.00032–0.0027), (5 supplementary STRING terms; within-query FDR 0.0233–0.039). These are supplementary annotations and do not replace the globally corrected GO evidence. The DDOST–SSR1 relationship is strongly represented in STRING and corresponds to an ER oligosaccharyltransferase or translocation-associated pair, but it is separate from the main mitochondrial respiratory pattern. hu.MAP identifies ATP5F1A and ATP5F1B together in several ATP synthase-containing complexes (hu.MAP huMAP3_08750.1) (hu.MAP huMAP3_09307.1) (hu.MAP huMAP3_11095.1). The complexes include many ATP synthase subunits and associated proteins, so the hu.MAP evidence supports a known ATP synthase component while covering only part of the module. No hu.MAP complex listed here contains the broader TCA and respiratory set.

**STRING interactions (score >= 0.7)**: 17 of 55 gene pairs: ATP5F1A–ATP5F1B (0.999); ATP5F1A–CS (0.94); ATP5F1A–SUCLA2 (0.802); ATP5F1A–SUCLG1 (0.853); ATP5F1A–UQCRC1 (0.97); ATP5F1A–VDAC2 (0.715); ATP5F1B–CS (0.917); ATP5F1B–SUCLG1 (0.733); ATP5F1B–UQCRC1 (0.969); ATP5F1B–VDAC2 (0.758); CS–GOT2 (0.952); CS–SUCLA2 (0.96); CS–SUCLG1 (0.929); CS–UQCRC1 (0.71); DDOST–SSR1 (0.972); GOT2–UQCRC1 (0.718); SUCLA2–SUCLG1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM The citric acid (TCA) cycle and respiratory electron transport (FDR = 0.00032, 6 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.00062, 7 genes); Process Aerobic respiration (FDR = 0.0014, 6 genes); Keyword Transit peptide (FDR = 0.0016, 7 genes); Component Mitochondrial matrix (FDR = 0.0018, 7 genes); Keyword Mitochondrion (FDR = 0.0027, 8 genes); TISSUES Left ventricle (FDR = 0.0109, 5 genes); COMPARTMENTS Mitochondrion (FDR = 0.0152, 8 genes); TISSUES Left atrium (FDR = 0.0198, 4 genes); TISSUES Subthalamic nucleus (FDR = 0.0198, 3 genes); NetworkNeighborAL Citrate cycle (TCA cycle), and Lactate dehydrogenase activity (FDR = 0.0233, 4 genes); Keyword Tricarboxylic acid cycle (FDR = 0.0252, 3 genes); KEGG Citrate cycle (TCA cycle) (FDR = 0.039, 3 genes); KEGG Metabolic pathways (FDR = 0.039, 8 genes); KEGG Carbon metabolism (FDR = 0.039, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08750.1 (ATP5F1B, ATP5F1A; 2/12); huMAP3_09307.1 (ATP5F1B, ATP5F1A; 2/35); huMAP3_11095.1 (ATP5F1B, ATP5F1A; 2/45)

### Novelty

The biological function is not a new discovery: the mitochondrial ATP synthase, TCA-cycle, respiratory-chain and succinate-CoA ligase relationships are established and are supported by gene descriptions, STRING, hu.MAP and the primary enrichment terms. What may be novel is the observation that these genes form a conserved co-abundance module across lung and myometrium in this particular dataset. That claim cannot be established from the fact sheet alone because no comparison with published co-abundance modules, independent cohorts, or tissue-specific network studies is provided. The absence of a hu.MAP complex for most module genes and the absence of STRING support for RAB18 do not prove novelty; they mainly indicate that the module is broader than a single curated physical complex. The most defensible conclusion is a potentially dataset-specific cross-tissue co-abundance configuration built largely from well-known mitochondrial biology.

**Hypothesis.** Hypothesis: the shared module reflects coordinated mitochondrial energy demand and oxidative capacity in metabolically active resident cells of lung and myometrium. A respiratory core involving citrate production, succinate-CoA ligase activity, electron transport and ATP synthase could be co-regulated to support ATP production and precursor-metabolite generation. VDAC2 may couple the mitochondrial respiratory compartment to outer-membrane metabolite exchange and apoptotic regulation. The DDOST–SSR1 pair and RAB18 may represent a linked membrane-trafficking or protein-processing state, but this connection is speculative because their direct relationships to the respiratory core are not established by the supplied complex evidence. This hypothesis should be tested by replication in independent samples, cell-composition adjustment, and direct measurements of mitochondrial respiration or ATP-generating capacity.

### Important genes

#### ATP5F1A

- **Related proteins** (co-abundance neighbors): ATP5F1B (0.94), CS (0.89), RAB18 (0.84), UQCRC1 (0.83); STRING partners: ATP5F1B (0.999), CS (0.94), SUCLA2 (0.802), SUCLG1 (0.853), UQCRC1 (0.97), VDAC2 (0.715)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung, myometrium
- **hu.MAP 3.0**: huMAP3_08750.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit alpha. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, using an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic po…
- **Diseases (Open Targets)**: mitochondrial complex V (ATP synthase) deficiency, nuclear type 4A (0.655); mitochondrial proton-transporting ATP synthase complex deficiency (0.648); mitochondrial complex V (ATP synthase) deficiency, nuclear type 4B (0.532); hereditary disease (0.394); Mitochondrial encephalopathy (0.371)
- **Europe PMC papers**: 822
- **Why important**: ATP5F1A is a central network hub with strong module connections to ATP5F1B, CS, RAB18 and UQCRC1. It is present in every primary enriched term (5 globally significant GO/KEGG terms, q_global 0.00448–0.0468; see the table), in the major STRING mitochondrial and respiration terms (9 supplementary STRING terms; within-query FDR 0.00032–0.0198), (STRING KEGG Metabolic pathways; within-query FDR = 0.039), and in all listed hu.MAP ATP synthase complexes (hu.MAP huMAP3_08750.1) (hu.MAP huMAP3_09307.1) (hu.MAP huMAP3_11095.1). Its established function is the alpha subunit of mitochondrial ATP synthase, which uses the proton gradient to produce ATP. It also has substantial literature support and disease links to mitochondrial complex V deficiency and mitochondrial encephalopathy.
- **Conclusion**: Established evidence identifies ATP5F1A as a core ATP-synthase component and a key connectivity point between ATP synthesis and the broader respiratory module. The module data support its importance as a marker of coordinated oxidative phosphorylation. It is not established that ATP5F1A initiates or regulates the cross-tissue co-abundance pattern; that causal interpretation remains a hypothesis.

#### CS

- **Related proteins** (co-abundance neighbors): ATP5F1A (0.89), GOT2 (0.85), ATP5F1B (0.84), SUCLG1 (0.82); STRING partners: ATP5F1A (0.94), ATP5F1B (0.917), GOT2 (0.952), SUCLA2 (0.96), SUCLG1 (0.929), UQCRC1 (0.71)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in lung, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS is one of the strongest network connectors, linking ATP synthase genes, GOT2, SUCLA2, SUCLG1 and UQCRC1. It appears in every primary enriched term (5 globally significant GO/KEGG terms, q_global 0.00448–0.0468; see the table) and across the broadest set of STRING annotations, including aerobic respiration, the TCA cycle and carbon metabolism (6 supplementary STRING terms; within-query FDR 0.00032–0.0027), (5 supplementary STRING terms; within-query FDR 0.0233–0.039). Its established enzymatic role is to generate citrate from oxaloacetate and acetyl-CoA in the mitochondrial matrix. It has extensive literature support and disease associations involving neurodegenerative and other disorders.
- **Conclusion**: Established evidence makes CS a biochemical anchor for the module, connecting entry into the TCA cycle with downstream respiratory energy production. Its high network position supports interpretation of the module as coordinated mitochondrial metabolism. The data do not show that CS activity itself changes or drives the module; co-abundance is not proof of enzyme activation.

#### UQCRC1

- **Related proteins** (co-abundance neighbors): ATP5F1A (0.83), VDAC2 (0.82), SSR1 (0.81); STRING partners: ATP5F1A (0.97), ATP5F1B (0.969), CS (0.71), GOT2 (0.718)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase core protein 1. Enables ubiquitin protein ligase binding activity. Predicted to be involved in oxidative phosphorylation. Predicted to act upstream of or within mitochondrial electron transport, ubiquinol to cytochrome c. Located in mitochondrion. Implicated in Alzheimer's disease. Biomarker of Alzheimer's disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: parkinsonism with polyneuropathy (0.642); neurodegenerative disease (0.569); Parkinson disease (0.521); Alzheimer disease (0.519); lysosomal storage disease (0.498)
- **Europe PMC papers**: 1860
- **Why important**: UQCRC1 connects ATP5F1A, ATP5F1B, CS, GOT2 and VDAC2 in STRING and occupies a prominent position in the co-abundance network. It contributes to the primary aerobic-respiration and energy-generation terms (GO:BP aerobic respiration; q_global = 0.00448), (GO:BP cellular respiration; q_global = 0.00832) (GO:BP energy derivation by oxidation of organic compounds; q_global = 0.0204) (GO:BP generation of precursor metabolites and energy; q_global = 0.0468), and to STRING respiratory-electron-transport annotations (STRING RCTM The citric acid (TCA) cycle and respiratory electron transport; within-query FDR = 0.00032), (STRING Process Aerobic respiration; within-query FDR = 0.0014), (STRING Keyword Transit peptide; within-query FDR = 0.0016), (STRING Keyword Mitochondrion; within-query FDR = 0.0027), (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0152), (STRING TISSUES Subthalamic nucleus; within-query FDR = 0.0198), (STRING KEGG Metabolic pathways; within-query FDR = 0.039). Its established function places it in mitochondrial ubiquinol-to-cytochrome-c electron transport. It has disease and biomarker associations involving Parkinson disease, Alzheimer disease and other neurodegenerative conditions.
- **Conclusion**: Established evidence supports UQCRC1 as the module's electron-transport representative and as a bridge between respiratory-chain and ATP-synthase signals. Its network placement is consistent with coordinated oxidative phosphorylation. The disease associations do not establish that this lung-myometrium module is pathological or neurodegenerative.

#### SUCLA2

- **Related proteins** (co-abundance neighbors): GOT2 (0.82); STRING partners: ATP5F1A (0.802), CS (0.96), SUCLG1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase ADP-forming subunit beta. Succinyl-CoA synthetase (SCS) is a mitochondrial matrix enzyme that acts as a heterodimer, being composed of an invariant alpha subunit and a substrate-specific beta subunit. The protein encoded by this gene is an ATP-specific SCS beta subunit that dimerizes with the SCS alpha subunit to form SCS-A, an essential component of the tricarboxylic acid cycle. SCS-A hydrolyzes ATP to convert succinate t…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome, encephalomyopathic form with methylmalonic aciduria (0.816); mitochondrial DNA depletion syndrome, encephalomyopathic form (0.581); neurodegenerative disease (0.485); mitochondrial disease (0.374); disease of peritoneum (0.372)
- **Europe PMC papers**: 1440
- **Why important**: SUCLA2 is included in every primary enriched term (5 globally significant GO/KEGG terms, q_global 0.00448–0.0468; see the table) and in the STRING TCA-cycle, mitochondrial-matrix and carbon-metabolism annotations (STRING RCTM The citric acid (TCA) cycle and respiratory electron transport; within-query FDR = 0.00032), (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.00062), (STRING Component Mitochondrial matrix; within-query FDR = 0.0018), (STRING Keyword Mitochondrion; within-query FDR = 0.0027), (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0152), (5 supplementary STRING terms; within-query FDR 0.0233–0.039). It links GOT2 to the module and has strong STRING relationships with CS, SUCLG1 and ATP5F1A. Its established role is the ATP-specific beta subunit of succinyl-CoA synthetase, an essential TCA-cycle enzyme complex. It has substantial literature support and disease associations with myopathic and encephalomyopathic mitochondrial DNA depletion syndromes.
- **Conclusion**: Established evidence identifies SUCLA2 as a strong TCA-cycle and mitochondrial energy marker that connects substrate-level metabolism with ATP-synthase-related genes. Its inclusion strengthens the interpretation of an integrated respiratory-metabolic program. The module does not establish whether SUCLA2 dysfunction explains the cross-tissue co-abundance pattern.

#### VDAC2

- **Related proteins** (co-abundance neighbors): DDOST (0.84), UQCRC1 (0.82); STRING partners: ATP5F1A (0.715), ATP5F1B (0.758)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: voltage dependent anion channel 2. This gene encodes a member of the voltage-dependent anion channel pore-forming family of proteins that are considered the main pathway for metabolite diffusion across the mitochondrial outer membrane. The encoded protein is also thought to be involved in the mitochondrial apoptotic pathway via regulation of BCL2-antagonist/killer 1 protein activity. Pseudogenes have been identified on chromosomes …
- **Diseases (Open Targets)**: neurodegenerative disease (0.345); alcohol drinking (0.204); atrial fibrillation (0.175); major depressive disorder (0.143); severe combined immunodeficiency (0.118)
- **Europe PMC papers**: 2914
- **Why important**: VDAC2 links UQCRC1 and DDOST in the module and has STRING relationships with both ATP synthase subunits (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.00062), (STRING Component Mitochondrial matrix; within-query FDR = 0.0018), (STRING Keyword Mitochondrion; within-query FDR = 0.0027), (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0152). Its established function is as a mitochondrial outer-membrane channel involved in metabolite diffusion and mitochondrial outer-membrane permeabilization, with additional evidence for apoptotic regulation. It provides a mechanistic interface between the mitochondrial interior, the cytosolic compartment and the ER-associated DDOST–SSR1 component. Its literature volume is substantial and its disease associations include neurodegenerative, cardiac and psychiatric conditions.
- **Conclusion**: Established evidence supports VDAC2 as a mitochondrial boundary and transport-related component rather than a core TCA enzyme. Its position suggests a possible interface between energy metabolism, metabolite exchange and mitochondrial stress responses. A role in coordinating the entire module is only a hypothesis because the supplied evidence does not demonstrate causal regulation or physical assembly of all these proteins.

## Module 1

**Tissue pair**: lung and myometrium  
**Genes (5)**: DDX39B, GOLGA7, HNRNPK, PTBP1, SARS1

### Function

The strongest interpretation is a conserved RNA-processing module. The primary enrichment evidence is (GO:BP RNA processing; q_global = 0.0258), in which most module genes are associated with RNA processing: DDX39B, HNRNPK, PTBP1, and SARS1. The supplementary STRING result (STRING Keyword mRNA splicing; within-query FDR = 0.0346) independently points toward mRNA splicing, but it is not global enrichment evidence. DDX39B is a spliceosome-associated RNA helicase involved in spliceosome assembly and nuclear mRNA export; HNRNPK is an RNA-binding hnRNP involved in pre-mRNA processing and RNA metabolism; PTBP1 regulates alternative splicing; and SARS1 links the module to translation and tRNA-related metabolism. The network has a coherent RNA-centered core, with HNRNPK acting as a hub-like connector to PTBP1 and DDX39B and PTBP1 connecting toward SARS1. GOLGA7 is the peripheral member and contributes a Golgi trafficking and protein palmitoylation function rather than the dominant RNA-processing signal. No additional GO or KEGG term passed global correction.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the secretome evidence identifies no secreted genes. HPA indicates low tissue specificity for every member, low immune-cell specificity for every member, and protein detection for every member in both lung and myometrium. Thus the module is more consistent with broadly expressed intracellular proteins, including housekeeping-type RNA-processing and translation machinery, than with a lung-specific or myometrium-specific program. The HPA single-cell results do not show a recurring blood-cell signal. One gene is group-enriched across several neural cell types, while GOLGA7 is cell-type enhanced in germ-cell and neutrophil-related categories, but these signals are not shared across the module. The shared co-abundance pattern could therefore reflect common intracellular machinery or shared cellular composition rather than a tissue-specific secretory or immune process.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA processing | 0.0258 | DDX39B, HNRNPK, PTBP1, SARS1 |

### STRING and hu.MAP

STRING provides established support for a connected RNA-processing core: DDX39B is linked to HNRNPK and PTBP1, and HNRNPK is strongly linked to PTBP1. These relationships are concordant with (GO:BP RNA processing; q_global = 0.0258) and (STRING Keyword mRNA splicing; within-query FDR = 0.0346), strengthening the interpretation that the central part of the module represents known RNA-binding and splicing biology rather than an arbitrary correlation pattern. STRING does not list partners for GOLGA7 or SARS1 within the reported module relationships, so their co-abundance links should not be treated as established physical interactions. No hu.MAP complex contains at least two module members. Accordingly, the module is supported by several known pairwise relationships but is not represented as a known shared hu.MAP complex.

**STRING interactions (score >= 0.7)**: 3 of 10 gene pairs: DDX39B–HNRNPK (0.808); DDX39B–PTBP1 (0.785); HNRNPK–PTBP1 (0.997)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword mRNA splicing (FDR = 0.0346, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be described as a wholly new molecular complex or as proven biological novelty. Its central relationships and functional theme are already well established through STRING, the gene annotations, and the literature on HNRNPK, PTBP1, and DDX39B. The potentially novel observation is the conserved co-abundance of this particular combination across lung and myometrium, especially the inclusion of GOLGA7 and SARS1 alongside the RNA-processing core. Because hu.MAP contains no multi-member complex for the module and STRING does not cover every co-abundance relationship, the tissue-shared network may represent a new systems-level association, but absence from those resources alone cannot establish novelty. The most defensible conclusion is that this is a biologically plausible conserved module with a potentially novel cross-tissue co-abundance configuration, not a newly discovered molecular complex.

**Hypothesis.** Hypothesis: the module reflects coordinated maintenance of gene-expression output in shared lung and myometrium cells. A core formed by DDX39B, HNRNPK, and PTBP1 could coordinate pre-mRNA processing, spliceosome-related activity, and nuclear RNA handling; SARS1 could couple this RNA program to translational capacity; and GOLGA7 could connect the intracellular expression program to Golgi-to-plasma-membrane trafficking and palmitoylation of membrane proteins. The co-abundance pattern may therefore arise because cells with high general RNA-processing and protein-production activity also require increased membrane-protein trafficking. This is a mechanistic proposal rather than an established causal pathway.

### Important genes

#### HNRNPK

- **Related proteins** (co-abundance neighbors): GOLGA7 (0.89), PTBP1 (0.88), DDX39B (0.82); STRING partners: DDX39B (0.808), PTBP1 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is the most central connector in the reported module network, linking GOLGA7, PTBP1, and DDX39B. It is included in the primary RNA-processing term (GO:BP RNA processing; q_global = 0.0258) and the supplementary splicing term (STRING Keyword mRNA splicing; within-query FDR = 0.0346). Its hnRNP biology directly supports roles in pre-mRNA processing, RNA metabolism, transcriptional regulation, and transport. It also has the largest literature volume among the listed genes and established disease associations including Au-Kline syndrome and neurodevelopmental and neurodegenerative disease categories.
- **Conclusion**: Established evidence identifies HNRNPK as the network hub-like RNA-binding component and a strong biological anchor for the module's RNA-processing interpretation. The hypothesis that it organizes the cross-tissue module is plausible from its network position but is not proven by co-abundance alone.

#### PTBP1

- **Related proteins** (co-abundance neighbors): HNRNPK (0.88), SARS1 (0.82); STRING partners: DDX39B (0.785), HNRNPK (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypyrimidine tract binding protein 1. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA-binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.505); dengue disease (0.372); open-angle glaucoma (0.330); glaucoma (0.309); neoplasm (0.116)
- **Europe PMC papers**: 4849
- **Why important**: PTBP1 is a central RNA-binding regulator connected to HNRNPK and SARS1 and is included in both (GO:BP RNA processing; q_global = 0.0258) and (STRING Keyword mRNA splicing; within-query FDR = 0.0346). Its annotations specifically support regulation of alternative splicing, mRNA processing, and RNA splicing. It has the greatest literature volume among the module members and disease associations spanning neurodevelopmental disorders, glaucoma, and neoplasm-related categories.
- **Conclusion**: Established evidence supports PTBP1 as a core alternative-splicing and RNA-processing component of the module. Its position between the HNRNPK-centered core and SARS1 makes it a plausible coupling point between RNA processing and translational capacity, but that coupling remains a hypothesis.

#### DDX39B

- **Related proteins** (co-abundance neighbors): HNRNPK (0.82); STRING partners: HNRNPK (0.808), PTBP1 (0.785)
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nuclear speckles; IHC detected in lung, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 39B. This gene encodes a member of the DEAD box family of RNA-dependent ATPases that mediate ATP hydrolysis during pre-mRNA splicing. The encoded protein is an essential splicing factor required for association of U2 small nuclear ribonucleoprotein with pre-mRNA, and it also plays an important role in mRNA export from the nucleus to the cytoplasm. This gene belongs to a cluster of genes localized in th…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); Alzheimer disease (0.522); Parkinson disease (0.503); lysosomal storage disease (0.503); neurodevelopmental disorder (0.413)
- **Europe PMC papers**: 1037
- **Why important**: DDX39B is included in (GO:BP RNA processing; q_global = 0.0258) and (STRING Keyword mRNA splicing; within-query FDR = 0.0346) and has STRING support with both HNRNPK and PTBP1. Its function as a DEAD-box RNA-dependent ATPase involved in spliceosome assembly, pre-mRNA splicing, and nuclear mRNA export gives the module a direct mechanistic entry point into RNA maturation. It also has substantial literature coverage and disease associations including neurodegenerative, neurodevelopmental, and lysosomal-storage disease categories.
- **Conclusion**: Established evidence supports DDX39B as a spliceosome and mRNA-export factor that reinforces the module's RNA-processing function. A coordinated DDX39B–HNRNPK–PTBP1 activity state is a reasonable mechanistic hypothesis, but the co-abundance data do not demonstrate direct regulation among these genes.

#### SARS1

- **Related proteins** (co-abundance neighbors): PTBP1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in lung, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: seryl-tRNA synthetase 1. This gene belongs to the class II amino-acyl tRNA family. The encoded enzyme catalyzes the transfer of L-serine to tRNA (Ser) and is related to bacterial and yeast counterparts. Multiple alternatively spliced transcript variants have been described but the biological validity of all variants is unknown. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, ataxia, and seizures (0.670); autosomal recessive non-syndromic intellectual disability (0.370); autosomal recessive primary microcephaly (0.370); arteriovenous malformations of the brain (0.340); hereditary peripheral neuropathy (0.118)
- **Europe PMC papers**: 400
- **Why important**: SARS1 is one of the genes contributing to the globally significant RNA-processing overlap (GO:BP RNA processing; q_global = 0.0258), although it is not included in the supplementary STRING splicing result. Its established function is sery l-tRNA synthetase activity, with links to cytoplasmic translation, tRNA modification, and selenocysteine-related biology. It is connected in the module to PTBP1 and has disease associations involving neurodevelopmental and neurological phenotypes. Its literature volume is lower than that of the principal RNA-binding factors, making its inclusion informative for the module's broader RNA-to-protein output interpretation.
- **Conclusion**: Established evidence places SARS1 at the translation and tRNA-processing side of the module rather than in the best-supported splicing core. Its connection to PTBP1 suggests a possible bridge between transcript processing and translation, but this is a hypothesis and is not supported by a reported STRING interaction.

#### GOLGA7

- **Related proteins** (co-abundance neighbors): HNRNPK (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: golgin A7. Involved in Golgi to plasma membrane protein transport; peptidyl-L-cysteine S-palmitoylation; and protein stabilization. Acts upstream of or within Golgi to plasma membrane transport. Located in Golgi membrane and Golgi stack. Is intrinsic component of Golgi membrane. Part of palmitoyltransferase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: COVID-19 (0.370); disorder of ear (0.312); neurodegenerative disease (0.312); body weight gain (0.223); placenta praevia (0.212)
- **Europe PMC papers**: 402
- **Why important**: GOLGA7 is the peripheral network member connected to HNRNPK and is not represented in the reported GO, STRING enrichment, or STRING interaction evidence. Its annotation supplies a distinct cellular function: Golgi-to-plasma-membrane transport, protein stabilization, and peptidyl-cysteine S-palmitoylation as part of a palmitoyltransferase complex. It is detected in both tissues and has cell-type-enhanced annotations in early primary spermatocytes, neutrophils, and oocytes. Its literature volume is smaller than that of the core RNA-processing genes, which makes it a potentially informative but less established module component.
- **Conclusion**: Established evidence supports GOLGA7 as a Golgi membrane and trafficking factor, but not as an RNA-processing factor. Its association with the module may represent coordination between general gene-expression activity and membrane-protein handling, or it may be a tissue-shared co-abundance link without direct molecular interaction; the available evidence cannot distinguish these possibilities.

## Module 2

**Tissue pair**: lung and myometrium  
**Genes (9)**: MAT2A, PSMC4, PSMC2, PSMD13, KARS1, RARS1, CCT3, CCT7, CCT8

### Function

The module most strongly represents intracellular protein homeostasis: ATP-dependent folding by the CCT chaperonin system, proteasome-mediated protein processing, and ongoing protein synthesis. The strongest primary evidence is the complete-module enrichment for intracellular protein-containing complex (GO:CC intracellular protein-containing complex; q_global = 2.54e-07), broad ATP and adenyl-nucleotide binding (10 globally significant GO/KEGG terms, q_global 0.0013–0.0482; see the table), the CCT chaperonin complex (GO:CC chaperonin-containing T-complex; q_global = 0.00241) (GO:CC protein folding chaperone complex; q_global = 0.0269) (GO:MF ATP-dependent protein folding chaperone; q_global = 0.0451), and the proteasome regulatory and accessory machinery (4 globally significant GO/KEGG terms, q_global 0.00501–0.0451; see the table). The CCT3, CCT7, and CCT8 annotations additionally connect the module to protein folding, protein stabilization, nuclear-body and Cajal-body localization, and telomerase-related processes (24 globally significant GO/KEGG terms, q_global 0.00241–0.0451; see the table). Those latter annotations are driven by the CCT trio and should not be interpreted as proof that the entire module directly regulates telomerase. KARS1 and RARS1 support aminoacyl-tRNA charging and translation, while MAT2A supports S-adenosylmethionine production. Overall, the most defensible interpretation is a conserved housekeeping-like protein quality-control and biosynthetic module, with possible links to nuclear and telomere-associated protein handling.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins: HPA identifies only KARS1 as having an intracellular and membrane secretome annotation, and the other genes are not secreted. It is not blood-cell enriched; every gene has low immune-cell specificity and no enriched blood-cell category is reported. Most genes have low tissue specificity, which supports a broadly expressed cellular program rather than a lung- or myometrium-exclusive program. Several genes show cell-type enhancement in reproductive or placental cell types, and MAT2A is enhanced in smooth muscle cells, but these patterns do not establish that such cells generate the module in the sampled tissues. Protein detection is present for much of the module in lung and for part of it in myometrium, with several genes undetected in myometrium. Thus, blood contamination is not supported by the HPA summary; shared cellular housekeeping, protein turnover, or shared cell-state composition are more plausible explanations for conservation across the tissues.

**GO/KEGG enrichment**: 45 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC intracellular protein-containing complex | 2.54e-07 | CCT3, CCT7, CCT8, KARS1, MAT2A, PSMC2, PSMC4, PSMD13, RARS1 |
| GO:MF ATP binding | 0.0013 | CCT3, CCT7, CCT8, KARS1, MAT2A, PSMC2, PSMC4, RARS1 |
| GO:MF adenyl ribonucleotide binding | 0.00135 | CCT3, CCT7, CCT8, KARS1, MAT2A, PSMC2, PSMC4, RARS1 |
| GO:CC chaperonin-containing T-complex | 0.00241 | CCT3, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 0.00241 | CCT3, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 0.00241 | CCT3, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 0.00241 | CCT3, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 0.00241 | CCT3, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 0.00241 | CCT3, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 0.00241 | CCT3, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 0.00241 | CCT3, CCT7, CCT8 |
| GO:MF adenyl nucleotide binding | 0.00462 | CCT3, CCT7, CCT8, KARS1, MAT2A, PSMC2, PSMC4, RARS1 |
| GO:CC proteasome regulatory particle | 0.00501 | PSMC2, PSMC4, PSMD13 |
| GO:BP binding of sperm to zona pellucida | 0.00501 | CCT3, CCT7, CCT8 |
| GO:CC proteasome accessory complex | 0.00501 | PSMC2, PSMC4, PSMD13 |

### STRING and hu.MAP

STRING provides strong prior support for the internal structure of the module. CCT3, CCT7, and CCT8 form a highly supported CCT/TriC subgroup, PSMC2, PSMC4, and PSMD13 form a highly supported proteasome-regulatory subgroup, and KARS1 and RARS1 form a highly supported aminoacyl-tRNA synthetase pair. The CCT and proteasome groups are connected by the CCT8-PSMC2 relationship, while RARS1 and KARS1 are linked to the broader module through the co-abundance network and their established translation function. STRING supplementary annotations independently support ATP binding, ATP hydrolysis, CCT chaperoning, proteasome regulatory particles, folding of actin, and protein metabolism (15 supplementary STRING terms; within-query FDR 0.0001–0.0068), but these are not global enrichment tests. hu.MAP independently places the CCT trio in multiple CCT-associated complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), the proteasome trio in proteasome complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1), and the KARS1-RARS1 pair in aminoacyl-tRNA synthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). These observations show that much of the module recapitulates known physical complexes. The cross-complex co-abundance arrangement is therefore more informative than treating every edge as a novel physical interaction.

**STRING interactions (score >= 0.7)**: 8 of 36 gene pairs: CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT7–CCT8 (0.999); CCT8–PSMC2 (0.733); KARS1–RARS1 (0.999); PSMC2–PSMC4 (0.999); PSMC2–PSMD13 (0.999); PSMC4–PSMD13 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword ATP-binding (FDR = 0.0001, 8 genes); Function ATP binding (FDR = 0.00046, 8 genes); Function ATP hydrolysis activity (FDR = 0.00071, 5 genes); Pfam TCP-1/cpn60 chaperonin family (FDR = 0.0014, 3 genes); Keyword Proteasome (FDR = 0.0039, 3 genes); Function ATP-dependent protein folding chaperone (FDR = 0.0041, 3 genes); Component Chaperonin-containing T-complex (FDR = 0.0049, 3 genes); Component Proteasome regulatory particle (FDR = 0.0049, 3 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 0.0051, 3 genes); COMPARTMENTS Proteasome regulatory particle (FDR = 0.0051, 3 genes); RCTM Folding of actin by CCT/TriC (FDR = 0.0063, 3 genes); RCTM Metabolism of proteins (FDR = 0.0063, 8 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 0.0068, 3 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 0.0068, 3 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 0.0068, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT3, CCT8, CCT7; 3/23); huMAP3_06559.1 (CCT3, CCT8, CCT7; 3/25); huMAP3_05064.1 (PSMC2, PSMC4, PSMD13; 3/31); huMAP3_09191.1 (CCT3, CCT8, CCT7; 3/32); huMAP3_10656.1 (CCT3, CCT8, CCT7; 3/36); huMAP3_14584.1 (CCT3, CCT8, CCT7; 3/61); huMAP3_09656.1 (PSMC2, PSMC4, PSMD13; 3/64); huMAP3_13725.1 (PSMC2, PSMC4, PSMD13; 3/69); huMAP3_01951.1 (CCT3, CCT7; 2/8); huMAP3_02637.1 (RARS1, KARS1; 2/14); huMAP3_13688.1 (RARS1, KARS1; 2/14)

### Novelty

The module should not be called a wholly new molecular complex. Its dominant substructures correspond to established CCT, proteasome, and aminoacyl-tRNA synthetase machinery, as shown by STRING and hu.MAP. The potentially novel aspect is the conserved co-abundance arrangement linking these otherwise distinct protein-homeostasis and translation systems across lung and myometrium. However, the fact sheet does not compare this module against a published tissue co-abundance atlas, and absence of a relationship from STRING or hu.MAP would not establish novelty. The appropriate conclusion is that this is a potentially interesting tissue-shared regulatory or cellular-state module built around known complexes, but novelty of the complete module remains unproven.

**Hypothesis.** Hypothesis: a shared cellular state in lung and myometrium increases demand for coordinated protein synthesis, folding, quality control, and degradation. In this model, KARS1 and RARS1 support translation, MAT2A supplies methyl-donor metabolism, CCT3-CCT7-CCT8 fold newly synthesized client proteins, and PSMC2-PSMC4-PSMD13 support proteasome-dependent clearance. The observed CCT-to-proteasome connection could represent coordinated handling of newly made, damaged, or remodeling-associated proteins. The CCT-associated telomerase and nuclear-localization annotations suggest a possible nuclear proteostasis or proliferative-state component, but this remains a hypothesis requiring direct measurements of protein turnover, CCT and proteasome activity, cell composition, and telomere-related phenotypes.

### Important genes

#### CCT8

- **Related proteins** (co-abundance neighbors): PSMD13 (0.89), PSMC4 (0.88), RARS1 (0.86), CCT3 (0.82); STRING partners: CCT3 (0.999), CCT7 (0.999), PSMC2 (0.733)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is the strongest network connector in the module and links the CCT subgroup to proteasome and aminoacyl-tRNA-related members. It is present in the complete-module complex enrichment (GO:CC intracellular protein-containing complex; q_global = 2.54e-07), the ATP and chaperone terms (16 globally significant GO/KEGG terms, q_global 0.0013–0.0482; see the table), and many CCT-associated STRING and hu.MAP findings (STRING Keyword ATP-binding; within-query FDR = 0.0001) (STRING Function ATP binding; within-query FDR = 0.00046) (STRING Function ATP hydrolysis activity; within-query FDR = 0.00071) (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 0.0014) (STRING Function ATP-dependent protein folding chaperone; within-query FDR = 0.0041) (STRING Component Chaperonin-containing T-complex; within-query FDR = 0.0049) (STRING COMPARTMENTS Chaperonin-containing T-complex; within-query FDR = 0.0051) (STRING RCTM Folding of actin by CCT/TriC; within-query FDR = 0.0063) (STRING RCTM Metabolism of proteins; within-query FDR = 0.0063) (STRING InterPro Chaperonin TCP-1, conserved site; within-query FDR = 0.0068) (STRING InterPro Chaperonin Cpn60/GroEL/TCP-1 family; within-query FDR = 0.0068) (STRING InterPro Chaperone tailless complex polypeptide 1 (TCP-1); within-query FDR = 0.0068) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). Its established function is as a subunit of the ATP-dependent CCT folding machine. It has extensive literature coverage and disease associations including neoplasm and lung adenocarcinoma in Open Targets.
- **Conclusion**: Established evidence supports CCT8 as a central structural and functional representative of the module's protein-folding arm. Its network position makes it a plausible coordinator between folding and proteasome-related abundance patterns. A direct role for CCT8 in the tissue-shared state or in telomerase regulation is a hypothesis, not demonstrated by this module.

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT7 (0.91), CCT8 (0.82); STRING partners: CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in lung, myometrium
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a core CCT/TriC component, forms the highly supported CCT3-CCT7-CCT8 subgroup, and is present across the broad primary enrichment for intracellular complexes, ATP-dependent folding, nuclear-body localization, and telomere-related terms (35 globally significant GO/KEGG terms, q_global 2.54e-07–0.0451; see the table). It has the largest literature volume among the CCT genes listed and has disease associations involving neurodevelopmental and neurodegenerative disorders.
- **Conclusion**: Established evidence identifies CCT3 as a core chaperonin component and a robust marker of the module's folding function. Its association with telomere and Cajal-body terms reflects the shared annotation of the CCT trio and does not establish a tissue-specific telomere mechanism. Its disease links make it biologically important, but the module alone does not identify which disease association is relevant here.

#### PSMC2

- **Related proteins** (co-abundance neighbors): MAT2A (0.83), RARS1 (0.80); STRING partners: CCT8 (0.733), PSMC4 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in lung, myometrium
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is an ATPase of the proteasome regulatory particle and belongs to the proteasome enrichments (17 globally significant GO/KEGG terms, q_global 2.54e-07–0.0482; see the table). It has established STRING links to PSMC4 and PSMD13 and is also linked to CCT8, providing a bridge between the proteasome subgroup and the CCT subgroup. hu.MAP places it in multiple proteasome complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). It has substantial literature coverage and disease associations involving plasma cell myeloma, mantle cell lymphoma, neoplasm, HIV infection, and amyloidosis.
- **Conclusion**: Established evidence supports PSMC2 as a central proteasome-regulatory component and a plausible network bridge to chaperone-mediated folding. The module supports coordinated proteostasis, but it does not show that PSMC2 activity is altered or that any listed disease association drives the lung-myometrium conservation.

#### PSMD13

- **Related proteins** (co-abundance neighbors): PSMC4 (0.89), CCT8 (0.89); STRING partners: PSMC2 (0.999), PSMC4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 is a non-ATPase component of the proteasome regulatory machinery and participates in the proteasome complex, regulatory particle, and accessory complex enrichments (5 globally significant GO/KEGG terms, q_global 2.54e-07–0.0451; see the table). It has highly supported STRING relationships with PSMC2 and PSMC4 and is included in the corresponding hu.MAP proteasome complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). Its nuclear-speckle localization and disease associations involving hematologic, neurodegenerative, neoplastic, and infectious conditions broaden its relevance beyond a generic proteasome marker.
- **Conclusion**: Established evidence supports PSMD13 as a proteasome-complex anchor that reinforces the interpretation of protein degradation and quality control. Its connection to CCT8 in the co-abundance graph may indicate coordinated folding and disposal, but a direct molecular interaction or causal tissue-specific role is not established by the available evidence.

#### MAT2A

- **Related proteins** (co-abundance neighbors): PSMC2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionine adenosyltransferase 2A. The protein encoded by this gene catalyzes the production of S-adenosylmethionine (AdoMet) from methionine and ATP. AdoMet is the key methyl donor in cellular processes. [provided by RefSeq, Jun 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.545); familial thoracic aortic aneurysm and aortic dissection (0.416); autoimmune disorder of central nervous system (0.340); prostate carcinoma (0.252); Abnormality of the cardiovascular system (0.192)
- **Europe PMC papers**: 2615
- **Why important**: MAT2A is the module's distinctive metabolic component. It catalyzes production of S-adenosylmethionine, a key methyl donor, and is annotated for S-adenosylmethionine biosynthesis, protein complex oligomerization, and TORC1-related regulation. It is ATP-binding enriched with the rest of the module (11 globally significant GO/KEGG terms, q_global 2.54e-07–0.0482; see the table), but it has no reported hu.MAP complex membership and no STRING partner in the supplied evidence. HPA reports tissue enhancement in pancreas and cell-type enhancement in smooth muscle cells, making it especially relevant to interpretation of myometrium.
- **Conclusion**: Established evidence supports MAT2A as a metabolic and methyl-donor component that may connect cellular biosynthesis with protein homeostasis. Its smooth-muscle enhancement provides a tissue-relevant clue, but its single network link and lack of STRING or hu.MAP support make it a weaker physical-complex anchor. Any proposed connection to chromatin, telomere maintenance, or the shared tissue state remains a hypothesis.

## Module 3

**Tissue pair**: lung and myometrium  
**Genes (7)**: PCNA, PFAS, SEC24C, AARS1, VARS1, XPO1, CSE1L

### Function

The module does not support a globally significant GO or KEGG functional assignment: no GO/KEGG term passed global correction. Its gene composition nevertheless suggests a mixed core-cellular program rather than a single pathway. CSE1L and XPO1 point to nucleocytoplasmic transport, PCNA to DNA replication and repair, AARS1 and VARS1 to aminoacyl-tRNA charging and translational fidelity, PFAS to de novo purine biosynthesis, and SEC24C to COPII-dependent vesicle trafficking. The co-abundance structure may therefore reflect coordinated basic biosynthetic, proliferative, and intracellular transport activity, but this interpretation remains inferential because the module lacks globally significant enrichment and STRING functional enrichment is absent.

**Cell composition.** The module is not composed of plasma proteins or secreted proteins: all members are non-secreted according to the HPA summary. Most genes have low tissue specificity and are detected in lung, while most are also detected in myometrium, consistent with broadly expressed intracellular proteins rather than a tissue-exclusive program. HPA nevertheless indicates cell-type structure: several genes are enhanced in erythrocyte progenitors, and individual genes show enrichment in bone marrow, neutrophils, germ-cell populations, cytotrophoblasts, or esophageal epithelial cells. PCNA is tissue enhanced in bone marrow, and PFAS is immune-cell enhanced in neutrophils. Thus, shared abundance could reflect broadly distributed housekeeping or proliferative activity, with a possible contribution from shared cell populations or blood-related material; the evidence does not establish blood contamination or a specific cellular origin.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a strong known relationship between AARS1 and VARS1 and a strong known relationship between CSE1L and XPO1. The other co-abundance connections are not supported by the reported high-confidence STRING interaction set, so co-abundance should not be interpreted as direct physical interaction. hu.MAP provides repeated support for CSE1L and XPO1 occurring together in large complexes (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_09592.1). However, each complex contains many additional proteins and only these two module members, so the hu.MAP evidence supports a known nuclear-transport or associated-complex relationship but does not define the whole module as one molecular complex. Together, STRING and hu.MAP indicate that part of the module recapitulates established biology, while the remaining links may represent co-regulation, shared cell-state dependence, indirect biology, or technical correlation.

**STRING interactions (score >= 0.7)**: 2 of 21 gene pairs: AARS1–VARS1 (0.938); CSE1L–XPO1 (0.976)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07170.1 (XPO1, CSE1L; 2/14); huMAP3_09042.1 (XPO1, CSE1L; 2/26); huMAP3_06791.1 (XPO1, CSE1L; 2/31); huMAP3_09592.1 (XPO1, CSE1L; 2/95)

### Novelty

The module should not be claimed as a newly discovered molecular complex or pathway. Its principal components have established functions, AARS1–VARS1 is a known STRING relationship, and CSE1L–XPO1 is represented both in STRING and in multiple hu.MAP complexes. The specific cross-tissue co-abundance arrangement may still be a potentially new observation, especially because the full module is not reproduced as a documented STRING interaction network or a single hu.MAP complex. Nevertheless, absence from those resources alone cannot prove novelty. A defensible conclusion is that the module is a new tissue-pair co-abundance finding with partly established molecular relationships, requiring replication and orthogonal validation before being considered a novel mechanism.

**Hypothesis.** Hypothesis: the shared lung–myometrium signal reflects a conserved intracellular cell-state program in which nuclear transport through the CSE1L–XPO1 axis is coordinated with DNA synthesis and repair through PCNA, translational capacity through AARS1 and VARS1, purine production through PFAS, and secretory-pathway logistics through SEC24C. This program may be strongest in broadly distributed or proliferative cells and may be influenced by shared erythroid or blood-associated material. The hypothesis is based on network structure, gene functions, HPA patterns, and known interaction resources; it is not established by GO/KEGG enrichment, STRING functional enrichment, or the co-abundance data alone.

Web sources: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8493386/; https://www.cell.com/molecular-therapy-family/oncology/fulltext/S2372-7705(21)00038-3

### Important genes

#### CSE1L

- **Related proteins** (co-abundance neighbors): PCNA (0.87), XPO1 (0.86), AARS1 (0.85); STRING partners: XPO1 (0.976)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_07170.1, huMAP3_09042.1, huMAP3_06791.1, huMAP3_09592.1
- **Function (MyGene.info)**: chromosome segregation 1 like. Proteins that carry a nuclear localization signal (NLS) are transported into the nucleus by the importin-alpha/beta heterodimer. Importin-alpha binds the NLS, while importin-beta mediates translocation through the nuclear pore complex. After translocation, RanGTP binds importin-beta and displaces importin-alpha. Importin-alpha must then be returned to the cytoplasm, leaving the NLS protein behind.…
- **Diseases (Open Targets)**: intelligence (0.293); neurodegenerative disease (0.269); Alzheimer disease (0.199); celiac disease (0.187); autism spectrum disorder (0.178)
- **Europe PMC papers**: 860
- **Why important**: CSE1L has the strongest network connectivity in the module and links PCNA, XPO1, and AARS1 in the co-abundance graph. It is the only gene paired with XPO1 across all reported hu.MAP complexes (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_09592.1), while STRING independently supports the CSE1L–XPO1 relationship. Its annotated role in recycling importin-alpha and protein export from the nucleus makes it a plausible connector between nuclear transport and the rest of the module. It also has substantial literature coverage, and the web search identified lung-cancer studies associating CSE1L silencing with reduced proliferation, invasion, and migration.
- **Conclusion**: Established evidence supports CSE1L as a central nuclear-transport-related module member and as part of a known CSE1L–XPO1 relationship. Its centrality makes it a leading candidate for coordinating the module, but a causal role in the shared lung–myometrium signal remains a hypothesis.

#### XPO1

- **Related proteins** (co-abundance neighbors): CSE1L (0.86), SEC24C (0.82); STRING partners: CSE1L (0.976)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in lung, myometrium
- **hu.MAP 3.0**: huMAP3_07170.1, huMAP3_09042.1, huMAP3_06791.1, huMAP3_09592.1
- **Function (MyGene.info)**: exportin 1. This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSe…
- **Diseases (Open Targets)**: plasma cell myeloma (0.642); B-cell chronic lymphocytic leukemia (0.626); diffuse large B-cell lymphoma (0.602); HIV infectious disease (0.561); neurodegenerative disease (0.522)
- **Europe PMC papers**: 5357
- **Why important**: XPO1 is a core nuclear export factor with direct co-abundance linkage to CSE1L and SEC24C. It has the strongest reported STRING relationship in the module through CSE1L and occurs with CSE1L in every listed hu.MAP complex (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_09592.1). Its established functions include export of RNA and proteins and regulation of several signaling and transcriptional regulators. It is detected in both lung and myometrium and has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence identifies XPO1 as the best-supported molecular anchor of the module’s nuclear-transport component. It could help couple nuclear export to cell-state and biosynthetic demands, but the co-abundance data do not show that it drives the entire module.

#### PCNA

- **Related proteins** (co-abundance neighbors): CSE1L (0.87), PFAS (0.84), AARS1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proliferating cell nuclear antigen. The protein encoded by this gene is found in the nucleus and is a cofactor of DNA polymerase delta. The encoded protein acts as a homotrimer and helps increase the processivity of leading strand synthesis during DNA replication. In response to DNA damage, this protein is ubiquitinated and is involved in the RAD6-dependent DNA repair pathway. Two transcript variants encoding the same protein have b…
- **Diseases (Open Targets)**: ataxia-telangiectasia-like disorder (0.497); neurodegenerative disease (0.188); neoplasm (0.118); diabetes mellitus (0.116); hepatocellular carcinoma (0.113)
- **Europe PMC papers**: 61820
- **Why important**: PCNA is highly connected within the co-abundance graph and connects CSE1L, PFAS, and AARS1. Its established roles in DNA replication, mismatch repair, chromatin organization, and damage responses provide a plausible explanation for coordinated abundance with purine synthesis and translation machinery. HPA places PCNA in a bone-marrow-enhanced tissue context and reports enhancement across several cell populations, including erythrocyte progenitors, while detecting it in both tissues. PCNA also has extensive literature and disease-association coverage.
- **Conclusion**: Established evidence supports PCNA as a marker and mediator of proliferative and genome-maintenance activity. In this module it may report a shared proliferative or progenitor-like cell state, but it does not establish that the module is specifically a DNA-replication module.

#### AARS1

- **Related proteins** (co-abundance neighbors): CSE1L (0.85), PCNA (0.83), PFAS (0.82); STRING partners: VARS1 (0.938)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in lung, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alanyl-tRNA synthetase 1. The human alanyl-tRNA synthetase (AARS) belongs to a family of tRNA synthases, of the class II enzymes.  Class II tRNA synthases evolved early in evolution and are highly conserved. This is reflected by the fact that 498 of the 968-residue polypeptide human AARS shares 41% identity witht the E.coli protein.  tRNA synthases are the enzymes that interpret the RNA code and attach specific aminoacids …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2N (0.762); developmental and epileptic encephalopathy, 29 (0.747); undetermined early-onset epileptic encephalopathy (0.678); trichothiodystrophy 8, nonphotosensitive (0.568); Charcot-Marie-Tooth disease type 2 (0.566)
- **Europe PMC papers**: 672
- **Why important**: AARS1 is among the most connected and strongest co-abundance nodes, linking CSE1L, PCNA, and PFAS. Its established function in alanyl-tRNA aminoacylation and translation makes it a representative of the module’s protein-production machinery. The AARS1–VARS1 relationship is supported by STRING, although the two genes are not joined by a reported hu.MAP complex here. AARS1 has documented inherited neurological disease associations and a substantial literature base.
- **Conclusion**: Established evidence supports AARS1 as a translation-fidelity and aminoacylation component that may reflect general biosynthetic demand. Its position suggests integration with the module, but there is no enrichment evidence establishing a specialized translational pathway.

#### PFAS

- **Related proteins** (co-abundance neighbors): PCNA (0.84), AARS1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoribosylformylglycinamidine synthase. Purines are necessary for many cellular processes, including DNA replication, transcription, and energy metabolism. Ten enzymatic steps are required to synthesize inosine monophosphate (IMP) in the de novo pathway of purine biosynthesis. The enzyme encoded by this gene catalyzes the fourth step of IMP biosynthesis. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: dyskeratosis congenita (0.520); Coats plus syndrome (0.455); neurodegenerative disease (0.187); hereditary disease (0.174); retinal disorder (0.118)
- **Europe PMC papers**: 3393
- **Why important**: PFAS connects PCNA and AARS1 and supplies a biochemical link between purine production, nucleotide availability, DNA replication, and translation. Its annotated function is a step in de novo IMP biosynthesis, and HPA associates it with erythrocyte progenitors and neutrophils while detecting it in lung but not myometrium. It also has disease associations involving inherited and neurodegenerative conditions and a substantial literature base.
- **Conclusion**: Established evidence supports PFAS as a purine-biosynthetic component that could support proliferative or biosynthetically active cells. Its tissue-detection asymmetry and blood-related HPA annotations make cell-composition effects particularly plausible, but they do not demonstrate that PFAS explains the shared module.
