# Conserved co-abundance modules: heart and myometrium

## Module 0

**Tissue pair**: heart and myometrium  
**Genes (8)**: GOT2, ATP5F1A, CS, NDUFS2, NDUFV1, NNT, SUCLG1, SUCLA2

### Function

This is a coherent mitochondrial energy-metabolism module. The primary evidence is the strong, broad enrichment for aerobic respiration (GO:BP aerobic respiration; q_global = 0.00143), cellular respiration (GO:BP cellular respiration; q_global = 0.00313), oxidation of organic compounds (GO:BP energy derivation by oxidation of organic compounds; q_global = 0.00813), generation of precursor metabolites and energy (GO:BP generation of precursor metabolites and energy; q_global = 0.0133), nucleotide and organophosphate metabolism (4 globally significant GO/KEGG terms, q_global 0.0133–0.0316; see the table), and the human metabolic pathways set (KEGG Metabolic pathways - Homo sapiens (human); q_global = 0.0452). The genes span the tricarboxylic acid cycle, respiratory complex I, mitochondrial ATP synthase, succinate-CoA ligase, amino-acid metabolism, and mitochondrial redox control. Thus, the most defensible interpretation is coordinated oxidative metabolism and ATP-supporting mitochondrial activity rather than a narrowly specialized pathway. The dense co-abundance structure reinforces this interpretation, with CS occupying the broadest network position and connecting TCA, respiratory-chain, ATP-synthesis, and redox-related genes. STRING independently supports TCA-cycle and respiratory-electron-transport organization (4 supplementary STRING terms; within-query FDR 6.66e-05–0.0323), but these STRING results are supplementary rather than globally corrected enrichment evidence.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and every gene has low immune-cell specificity. This makes a blood-cell or circulating-protein explanation unlikely. The proteins are detected in heart muscle for the whole module and in myometrium for most members, supporting relevance to the sampled tissues. HPA also reports enrichment in skeletal muscle and tongue for several genes, with additional cell-type enrichments in parietal cells, hepatocytes, and other specialized epithelial populations. Therefore, the shared heart–myometrium signal is most consistent with a broadly conserved, energy-demanding tissue or muscle-cell program, although the HPA patterns indicate that the module is not exclusive to those tissues. The absence of immune specificity argues against a shared blood-cell composition artifact, while the tissue-enhanced annotations are compatible with cellular metabolic demand.

**GO/KEGG enrichment**: 9 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP aerobic respiration | 0.00143 | ATP5F1A, CS, NDUFS2, NDUFV1, NNT, SUCLA2, SUCLG1 |
| GO:BP cellular respiration | 0.00313 | ATP5F1A, CS, NDUFS2, NDUFV1, NNT, SUCLA2, SUCLG1 |
| GO:BP energy derivation by oxidation of organic compounds | 0.00813 | ATP5F1A, CS, NDUFS2, NDUFV1, NNT, SUCLA2, SUCLG1 |
| GO:BP generation of precursor metabolites and energy | 0.0133 | ATP5F1A, CS, NDUFS2, NDUFV1, NNT, SUCLA2, SUCLG1 |
| GO:BP purine-containing compound metabolic process | 0.0133 | ATP5F1A, GOT2, NDUFS2, NDUFV1, NNT, SUCLA2, SUCLG1 |
| GO:BP nucleoside phosphate metabolic process | 0.0144 | ATP5F1A, GOT2, NDUFS2, NDUFV1, NNT, SUCLA2, SUCLG1 |
| GO:BP nucleobase-containing small molecule metabolic process | 0.0209 | ATP5F1A, GOT2, NDUFS2, NDUFV1, NNT, SUCLA2, SUCLG1 |
| GO:BP organophosphate metabolic process | 0.0316 | ATP5F1A, GOT2, NDUFS2, NDUFV1, NNT, SUCLA2, SUCLG1 |
| KEGG Metabolic pathways - Homo sapiens (human) | 0.0452 | ATP5F1A, CS, GOT2, NDUFS2, NDUFV1, NNT, SUCLA2, SUCLG1 |

### STRING and hu.MAP

STRING provides extensive known functional connectivity within the module. CS is linked to ATP5F1A, GOT2, NDUFS2, NDUFV1, SUCLA2, and SUCLG1; ATP5F1A is linked to respiratory-chain and succinate-CoA-ligase members; and SUCLA2 and SUCLG1 show particularly strong known association. NDUFS2 and NDUFV1 are very strongly connected to one another in STRING and are repeatedly present together in hu.MAP complexes (hu.MAP huMAP3_08132.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1). Those hu.MAP entries place them within larger mitochondrial respiratory-chain complex-I assemblies, alongside many established complex-I subunits and assembly factors. The module therefore recapitulates known mitochondrial biology rather than representing an unsupported association. At the same time, hu.MAP does not place the other module members into a reported shared complex, and several co-abundance links may represent pathway-level coordination or shared regulation rather than direct physical binding. NNT has no listed STRING partner in this module, despite its strong functional fit with mitochondrial redox metabolism.

**STRING interactions (score >= 0.7)**: 16 of 28 gene pairs: ATP5F1A–CS (0.94); ATP5F1A–NDUFS2 (0.98); ATP5F1A–NDUFV1 (0.958); ATP5F1A–SUCLA2 (0.802); ATP5F1A–SUCLG1 (0.853); CS–GOT2 (0.952); CS–NDUFS2 (0.772); CS–NDUFV1 (0.724); CS–SUCLA2 (0.96); CS–SUCLG1 (0.929); GOT2–NDUFS2 (0.802); NDUFS2–NDUFV1 (0.999); NDUFS2–SUCLA2 (0.837); NDUFS2–SUCLG1 (0.916); NDUFV1–SUCLG1 (0.836); SUCLA2–SUCLG1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM The citric acid (TCA) cycle and respiratory electron transport (FDR = 6.66e-05, 7 genes); Process Aerobic respiration (FDR = 0.00022, 7 genes); Keyword Transit peptide (FDR = 0.00027, 8 genes); Keyword Mitochondrion (FDR = 0.0021, 8 genes); Keyword Primary mitochondrial disease (FDR = 0.0021, 5 genes); KEGG Metabolic pathways (FDR = 0.005, 8 genes); RCTM Citric acid cycle (TCA cycle) (FDR = 0.0145, 4 genes); Keyword Methylation (FDR = 0.0199, 5 genes); COMPARTMENTS Mitochondrion (FDR = 0.0242, 8 genes); DISEASES Mitochondrial metabolism disease (FDR = 0.0274, 5 genes); DISEASES Leigh disease (FDR = 0.0291, 4 genes); Keyword Translocase (FDR = 0.0309, 3 genes); Process Tricarboxylic acid cycle (FDR = 0.0323, 4 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.0345, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08132.1 (NDUFS2, NDUFV1; 2/24); huMAP3_14018.1 (NDUFS2, NDUFV1; 2/48); huMAP3_06397.1 (NDUFS2, NDUFV1; 2/49); huMAP3_09982.1 (NDUFS2, NDUFV1; 2/49); huMAP3_09567.1 (NDUFS2, NDUFV1; 2/52); huMAP3_14878.1 (NDUFS2, NDUFV1; 2/53)

### Novelty

This module should not be described as a wholly new mitochondrial pathway. Its central functions, including the TCA cycle, respiratory electron transport, ATP synthesis, complex-I biology, and succinate-CoA ligase activity, are well established in STRING, hu.MAP, MyGene.info, Open Targets, and the literature represented in the fact sheet. The potentially novel aspect is the reproducible co-abundance organization of these known mitochondrial components as a conserved module shared by heart and myometrium, especially the tissue-pair context and the particular combination of TCA, respiratory-chain, ATP-synthase, redox, and amino-acid-metabolism genes. Lack of hu.MAP coverage for several members and absence of a listed STRING partner for NNT do not establish novelty; they instead identify relationships that require direct experimental testing. Overall, this is best regarded as a biologically credible tissue-shared organization of established mitochondrial machinery, with contextual rather than molecular novelty.

**Hypothesis.** Hypothesis: in heart and myometrium, increased cellular energy demand coordinately raises mitochondrial oxidative capacity. CS and SUCLA2–SUCLG1 could support TCA-cycle carbon flow and substrate-level nucleotide-phosphate metabolism, NDUFS2 and NDUFV1 could support complex-I electron entry and proton-gradient generation, ATP5F1A could use that gradient for ATP production, and NNT could maintain mitochondrial NADPH for biosynthesis and reactive-oxygen control. GOT2 could connect amino-acid and aspartate/glutamate metabolism with TCA intermediates. The observed module may therefore represent a coordinated energetic and redox state of metabolically active muscle-related cells. This is a mechanistic model, not proof of physical interaction, causal regulation, or altered pathway flux.

### Important genes

#### CS

- **Related proteins** (co-abundance neighbors): GOT2 (0.86), NDUFS2 (0.86), SUCLG1 (0.86), SUCLA2 (0.85), NDUFV1 (0.82), ATP5F1A (0.82), NNT (0.81); STRING partners: ATP5F1A (0.94), GOT2 (0.952), NDUFS2 (0.772), NDUFV1 (0.724), SUCLA2 (0.96), SUCLG1 (0.929)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS has the broadest network position in the module and connects nearly all functional portions of the network, including GOT2, the complex-I genes, the succinate-CoA-ligase genes, and ATP5F1A. It is a mitochondrial citrate-synthase enzyme at the entry point of the TCA cycle and appears in the primary respiration, energy-generation, and metabolic-pathway terms (5 globally significant GO/KEGG terms, q_global 0.00143–0.0452; see the table). It also has extensive STRING support (10 supplementary STRING terms; within-query FDR 6.66e-05–0.0345) and a very large literature base.
- **Conclusion**: Established conclusion: CS is a strong network and biochemical anchor for the module and supports a TCA-linked oxidative-metabolism interpretation. Hypothesis: its central co-abundance position may reflect coordination of carbon entry into respiration with downstream electron transport and ATP production, but the data do not establish that CS controls the other genes.

#### NNT

- **Related proteins** (co-abundance neighbors): ATP5F1A (0.92), CS (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nicotinamide nucleotide transhydrogenase. This gene encodes an integral protein of the inner mitochondrial membrane. The enzyme couples hydride transfer between NAD(H) and NADP(+) to proton translocation across the inner mitochondrial membrane. Under most physiological conditions, the enzyme uses energy from the mitochondrial proton gradient to produce high concentrations of NADPH. The resulting NADPH is used for biosynthesis and in free …
- **Diseases (Open Targets)**: familial glucocorticoid deficiency (0.638); neurodegenerative disease (0.497); hereditary disease (0.453); atypical hemolytic-uremic syndrome with DGKE deficiency (0.416); Abnormality of the skeletal system (0.396)
- **Europe PMC papers**: 6111
- **Why important**: NNT contributes mitochondrial redox control by coupling proton-gradient energy to NADPH production, with roles in reactive-oxygen metabolism and proton transport according to the fact sheet. It participates in every globally significant enrichment term (9 globally significant GO/KEGG terms, q_global 0.00143–0.0452; see the table) and in multiple STRING respiratory and TCA-related supplementary terms (8 supplementary STRING terms; within-query FDR 6.66e-05–0.0323). HPA detects it in heart and myometrium and identifies cardiomyocytes and myonuclei among enriched cell types. It has no listed STRING partner in the module, making it a functionally important bridge that is not explained by the reported physical-interaction network.
- **Conclusion**: Established conclusion: NNT adds a mitochondrial NADPH and redox dimension to an otherwise strongly respiratory module. Hypothesis: it may buffer oxidative stress generated by high respiratory activity in heart and smooth muscle, but this proposed redox-buffering role is not directly demonstrated by co-abundance alone.

#### NDUFS2

- **Related proteins** (co-abundance neighbors): CS (0.86); STRING partners: ATP5F1A (0.98), CS (0.772), GOT2 (0.802), NDUFV1 (0.999), SUCLA2 (0.837), SUCLG1 (0.916)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_08132.1, huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S2. The protein encoded by this gene is a core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (complex I). Mammalian mitochondrial complex I is composed of at least 43 different subunits, 7 of which are encoded by the mitochondrial genome, and the rest are the products of nuclear genes. The iron-sulfur protein fraction of complex I is made up of 7 subunits, including this g…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.758); mitochondrial complex I deficiency, nuclear type 6 (0.665); type 2 diabetes mellitus (0.608); mitochondrial disease (0.596); Parkinson disease (0.588)
- **Europe PMC papers**: 1723
- **Why important**: NDUFS2 is a core subunit of mitochondrial respiratory complex I and is annotated for NADH-to-ubiquinone electron transfer and complex-I assembly. It participates in every primary enrichment term (9 globally significant GO/KEGG terms, q_global 0.00143–0.0452; see the table), has extensive STRING connections, and is paired with NDUFV1 in every reported hu.MAP complex (hu.MAP huMAP3_08132.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1). Its disease associations include complex-I deficiency, mitochondrial disease, and Parkinson disease, providing strong clinical relevance.
- **Conclusion**: Established conclusion: NDUFS2 is a well-supported respiratory-chain component and a principal molecular anchor of the module's complex-I interpretation. Hypothesis: its co-abundance with TCA and ATP-synthase genes may indicate coordinated assembly or activity of oxidative-phosphorylation machinery, but the module does not prove altered complex-I assembly.

#### NDUFV1

- **Related proteins** (co-abundance neighbors): CS (0.82); STRING partners: ATP5F1A (0.958), CS (0.724), NDUFS2 (0.999), SUCLG1 (0.836)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, myometrium
- **hu.MAP 3.0**: huMAP3_08132.1, huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit V1. The mitochondrial respiratory chain provides energy to cells via oxidative phosphorylation and consists of four membrane-bound electron-transporting protein complexes (I-IV) and an ATP synthase (complex V). This gene encodes a 51 kDa subunit of the NADH:ubiquinone oxidoreductase complex I; a large complex with at least 45 nuclear and mitochondrial encoded subunits that liberates electrons from NAD…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.788); mitochondrial complex I deficiency, nuclear type 4 (0.724); mitochondrial complex I deficiency, nuclear type 1 (0.685); Leigh syndrome (0.635); type 2 diabetes mellitus (0.609)
- **Europe PMC papers**: 4567
- **Why important**: NDUFV1 is the complex-I subunit carrying the NADH-binding site and participates in electron transfer, proton-motive-force-driven ATP synthesis, and mitochondrial ATP synthesis. It appears in all primary enrichment terms (9 globally significant GO/KEGG terms, q_global 0.00143–0.0452; see the table), has a very strong STRING relationship with NDUFS2, and is included with NDUFS2 in all hu.MAP complex entries (hu.MAP huMAP3_08132.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1). Its disease associations include several forms of complex-I deficiency and Leigh syndrome, while its literature volume is substantial.
- **Conclusion**: Established conclusion: NDUFV1 provides direct biochemical support for the module's electron-entry and oxidative-phosphorylation interpretation. Hypothesis: coordinated NDUFV1 and NDUFS2 abundance could reflect preservation of a functional complex-I core in both tissues, although co-abundance cannot distinguish intact-complex abundance from shared transcriptional regulation.

#### ATP5F1A

- **Related proteins** (co-abundance neighbors): NNT (0.92), SUCLG1 (0.88), CS (0.82); STRING partners: CS (0.94), NDUFS2 (0.98), NDUFV1 (0.958), SUCLA2 (0.802), SUCLG1 (0.853)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP synthase F1 subunit alpha. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, using an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic po…
- **Diseases (Open Targets)**: mitochondrial complex V (ATP synthase) deficiency, nuclear type 4A (0.655); mitochondrial proton-transporting ATP synthase complex deficiency (0.648); mitochondrial complex V (ATP synthase) deficiency, nuclear type 4B (0.532); hereditary disease (0.394); Mitochondrial encephalopathy (0.371)
- **Europe PMC papers**: 822
- **Why important**: ATP5F1A encodes the alpha subunit of mitochondrial ATP synthase and participates in proton-motive-force-driven ATP synthesis. It is included in every primary enrichment term (9 globally significant GO/KEGG terms, q_global 0.00143–0.0452; see the table), occupies a connected position linking NNT, SUCLG1, and CS, and is supported by STRING relationships to several respiratory and TCA-associated genes (10 supplementary STRING terms; within-query FDR 6.66e-05–0.0345). Its disease associations include mitochondrial complex-V deficiency and mitochondrial encephalopathy. HPA detects the protein in both heart and myometrium.
- **Conclusion**: Established conclusion: ATP5F1A supplies the module's clearest ATP-production endpoint and connects respiratory activity to usable cellular energy. Hypothesis: its co-abundance may indicate matched demand for proton-gradient formation and ATP synthesis, but it does not establish increased ATP flux.

#### SUCLA2

- **Related proteins** (co-abundance neighbors): GOT2 (0.88), SUCLG1 (0.87), CS (0.85); STRING partners: ATP5F1A (0.802), CS (0.96), NDUFS2 (0.837), SUCLG1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase ADP-forming subunit beta. Succinyl-CoA synthetase (SCS) is a mitochondrial matrix enzyme that acts as a heterodimer, being composed of an invariant alpha subunit and a substrate-specific beta subunit. The protein encoded by this gene is an ATP-specific SCS beta subunit that dimerizes with the SCS alpha subunit to form SCS-A, an essential component of the tricarboxylic acid cycle. SCS-A hydrolyzes ATP to convert succinate t…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome, encephalomyopathic form with methylmalonic aciduria (0.816); mitochondrial DNA depletion syndrome, encephalomyopathic form (0.581); neurodegenerative disease (0.485); mitochondrial disease (0.374); disease of peritoneum (0.372)
- **Europe PMC papers**: 1440
- **Why important**: SUCLA2 is the ATP-specific beta subunit of mitochondrial succinate-CoA ligase and supports the TCA cycle and succinate metabolism. It participates in every primary enrichment term (9 globally significant GO/KEGG terms, q_global 0.00143–0.0452; see the table), has strong STRING links to CS, NDUFS2, SUCLG1, and ATP5F1A, and is included in multiple TCA, respiratory, and mitochondrial-disease supplementary terms (10 supplementary STRING terms; within-query FDR 6.66e-05–0.0345). Its disease associations include myopathic mitochondrial DNA depletion syndrome and related mitochondrial disorders.
- **Conclusion**: Established conclusion: SUCLA2 links TCA-cycle chemistry and nucleotide-phosphate metabolism to the respiratory network and is a strong biochemical connector within the module. Hypothesis: its co-abundance with SUCLG1 may reflect coordinated succinate-CoA-ligase capacity in energy-demanding cells, but the data do not establish enzyme-complex stoichiometry or pathway flux.

## Module 1

**Tissue pair**: heart and myometrium  
**Genes (5)**: ANXA6, HSPA5, DNM1L, GSN, HSPA8

### Function

No GO/KEGG term passed global correction, so the module does not support a globally significant pathway assignment. The strongest interpretation is a stress, protein-homeostasis, membrane-remodeling, cytoskeletal, and organelle-dynamics module. HSPA5 and HSPA8 provide chaperone functions related to protein folding, unfolded-protein responses, and membrane-trafficking processes. ANXA6 contributes calcium-dependent membrane and phospholipid binding. GSN contributes calcium-regulated actin filament assembly and disassembly. DNM1L contributes mitochondrial and peroxisomal fission. The STRING supplementary terms for melanosome, anchoring junction, and the MreB/Mbl protein domain (STRING Component Melanosome; within-query FDR = 0.0077), (STRING Component Anchoring junction; within-query FDR = 0.0151), (STRING Pfam MreB/Mbl protein; within-query FDR = 0.0381) are supportive context only and are not globally corrected GO/KEGG evidence. The sparse network, with the strongest known relationship between HSPA5 and HSPA8, argues for a compact co-abundance signature rather than a demonstrated canonical pathway.

**Cell composition.** The proteins are predominantly intracellular and broadly distributed rather than a coherent tissue-specific secreted program. HSPA5, ANXA6, DNM1L, and HSPA8 have low tissue specificity, while GSN is tissue enhanced in heart muscle. HPA reports low immune-cell specificity for most genes, with immune-cell enhancement for GSN in eosinophils; therefore the module is not strongly indicative of blood-cell contamination, although GSN is secreted to blood and could contribute to a circulating-protein signal. Four genes show cell-type enhancement, including patterns in syncytiotrophoblasts and other specialized cell types, so shared cellular composition or common stress states in the samples remain plausible explanations. Protein detection is broadly present in both heart and myometrium, supporting measurement in the paired tissues. Overall, the module is more consistent with shared intracellular housekeeping, proteostasis, cytoskeletal, and organelle-remodeling biology than with a plasma-protein or blood-cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING pair among module genes is HSPA5-HSPA8, indicating established functional relatedness between ER-associated and constitutive HSP70 chaperone systems. The remaining co-abundance edges are not represented by high-confidence STRING links in the supplied evidence, so their module-level relationships may reflect tissue-specific co-regulation, indirect biology, or correlated abundance rather than established physical interactions. STRING supplementary associations connect HSPA5, ANXA6, GSN, HSPA8, and DNM1L to anchoring-junction or melanosome-related annotations (STRING Component Melanosome; within-query FDR = 0.0077), (STRING Component Anchoring junction; within-query FDR = 0.0151), and connect HSPA5 and HSPA8 to the MreB/Mbl protein-domain annotation (STRING Pfam MreB/Mbl protein; within-query FDR = 0.0381); these are hypothesis-generating and retain their stated supplementary status. No hu.MAP complex contains multiple module members. Thus, the module has one clearly established chaperone relationship but no demonstrated shared multiprotein complex.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: HSPA5–HSPA8 (0.983)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Melanosome (FDR = 0.0077, 4 genes); Component Anchoring junction (FDR = 0.0151, 5 genes); Pfam MreB/Mbl protein (FDR = 0.0381, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a definitively new biological pathway. HSPA5, HSPA8, ANXA6, GSN, and DNM1L are individually well characterized, and several have substantial disease and literature associations. The absence of a matching hu.MAP complex and the limited STRING connectivity suggest that this exact co-abundance configuration may be underrepresented in curated interaction resources, but absence from those resources does not establish novelty. A cautious conclusion is that the tissue-pair-specific co-abundance arrangement is potentially novel, whereas the component functions and the HSPA5-HSPA8 relationship are established. Novelty would require comparison with independent heart and myometrium cohorts, other tissue-pair modules, and published co-expression or proteomic studies.

**Hypothesis.** Hypothesis: in heart and myometrium, a shared cellular stress or remodeling state coordinately increases ER and cytosolic chaperone capacity through HSPA5 and HSPA8, while ANXA6 and GSN reorganize calcium-sensitive membranes and actin structures and DNM1L adjusts mitochondrial and peroxisomal dynamics. The observed co-abundance may therefore represent a conserved proteostasis-and-remodeling response in contractile tissues, potentially arising during mechanical, metabolic, or differentiation-related stress. This is a mechanistic hypothesis, not a conclusion from the enrichment analysis; it should be tested by independent cohorts, cell-resolved data, perturbation of the chaperone or mitochondrial-fission components, and measurement of protein-folding, calcium, actin, and organelle-dynamics phenotypes.

### Important genes

#### HSPA5

- **Related proteins** (co-abundance neighbors): ANXA6 (0.90), GSN (0.83); STRING partners: HSPA8 (0.983)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in heart, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is a high-connectivity module node linked to ANXA6 and GSN and has the strongest supplied STRING relationship to HSPA8. Its established ER chaperone role and function as a regulator of ER homeostasis make it a plausible proteostasis anchor. It is detected in both tissues, has broad tissue distribution, and has extensive disease and literature coverage, making it biologically interpretable and experimentally tractable.
- **Conclusion**: Established evidence supports HSPA5 as a central ER-proteostasis component and as the most strongly supported interaction hub through its relationship with HSPA8. It is a leading candidate driver of the module's stress-response interpretation, but the co-abundance data alone do not establish that HSPA5 regulates the other module genes.

#### HSPA8

- **Related proteins** (co-abundance neighbors): ANXA6 (0.81); STRING partners: HSPA5 (0.983)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Flagellar centriole, Annulus; IHC detected in heart, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 8. This gene encodes a member of the heat shock protein 70 family, which contains both heat-inducible and constitutively expressed members. This protein belongs to the latter group, which are also referred to as heat-shock cognate proteins. It functions as a chaperone, and binds to nascent polypeptides to facilitate correct folding. It also functions as an ATPase in the disassembly of clathrin-coated…
- **Diseases (Open Targets)**: dengue disease (0.505); systemic lupus erythematosus (0.375); smoking initiation (0.199); Lennox-Gastaut syndrome (0.118); neoplasm (0.105)
- **Europe PMC papers**: 6937
- **Why important**: HSPA8 is directly connected to ANXA6 in the module and has a very strong established STRING relationship with HSPA5. As a constitutively expressed HSP70 chaperone, it supports protein folding, unfolded-protein responses, and clathrin-coated-vesicle disassembly. Its presence in both tissues and broad tissue distribution fit a shared cellular maintenance program, while its extensive literature provides strong functional context.
- **Conclusion**: Established evidence supports HSPA8 as a constitutive chaperone and trafficking factor that reinforces the HSPA5-centered interpretation. Its module position suggests participation in a shared proteostasis state, but it is not proven to form a novel complex with the other genes.

#### GSN

- **Related proteins** (co-abundance neighbors): HSPA5 (0.83), DNM1L (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gelsolin. The protein encoded by this gene binds to the 'plus' ends of actin monomers and filaments to prevent monomer exchange. The encoded calcium-regulated protein functions in both assembly and disassembly of actin filaments. Defects in this gene are a cause of familial amyloidosis Finnish type (FAF). Multiple transcript variants encoding several different isoforms have been found for this gene. [provid…
- **Diseases (Open Targets)**: Finnish type amyloidosis (0.805); AL amyloidosis (0.463); neuropathy (0.418); cardiomyopathy (0.418); cutis laxa (0.417)
- **Europe PMC papers**: 5062
- **Why important**: GSN is a network bridge between HSPA5 and DNM1L and is the only gene with heart-muscle tissue enhancement in the supplied HPA summary. Its calcium-regulated control of actin filament assembly and disassembly provides a direct connection to cytoskeletal remodeling, while its association with Finnish-type amyloidosis, amyloidosis, neuropathy, and cardiomyopathy gives it disease relevance. It is also secreted to blood, so it may link intracellular remodeling biology with circulating protein measurements.
- **Conclusion**: Established evidence supports GSN as the module's clearest actin-remodeling and heart-associated component, with important disease associations. Its secreted status means that a blood-derived contribution cannot be excluded, although the broader HPA profile does not indicate a predominantly blood-cell module. Whether GSN couples chaperone activity to mitochondrial remodeling in this module remains a hypothesis.

#### DNM1L

- **Related proteins** (co-abundance neighbors): GSN (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in heart, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 1L. This gene encodes a member of the dynamin superfamily of GTPases. The encoded protein mediates mitochondrial and peroxisomal division, and is involved in developmentally regulated apoptosis and programmed necrosis. Dysfunction of this gene is implicated in several neurological disorders, including Alzheimer's disease. Mutations in this gene are associated with the autosomal dominant disorder, ence…
- **Diseases (Open Targets)**: encephalopathy, lethal, due to defective mitochondrial peroxisomal fission 1 (0.815); autosomal dominant optic atrophy, classic form (0.721); neurodegenerative disease (0.531); encephalopathy due to mitochondrial and peroxisomal fission defect (0.455); hereditary disease (0.451)
- **Europe PMC papers**: 3015
- **Why important**: DNM1L is the network endpoint connected to GSN and is the only module member with an explicit mitochondrial and peroxisomal fission function. Its established roles in organelle division, mitochondrial organization, and programmed cell death provide a mechanistic route from cytoskeletal remodeling to organelle adaptation. Its disease associations include lethal encephalopathy caused by defective mitochondrial and peroxisomal fission and autosomal dominant optic atrophy.
- **Conclusion**: Established evidence supports DNM1L as an organelle-dynamics component that could make the module relevant to metabolic or stress adaptation. Its peripheral network position means it is not a central connectivity hub, and the data do not prove that mitochondrial fission is the primary function of the entire module.

#### ANXA6

- **Related proteins** (co-abundance neighbors): HSPA5 (0.90), HSPA8 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A6. Annexin VI belongs to a family of calcium-dependent membrane and phospholipid binding proteins. Several members of the annexin family have been implicated in membrane-related events along exocytotic and endocytotic pathways. The annexin VI gene is approximately 60 kbp long and contains 26 exons. It encodes a protein of about 68 kDa that consists of eight 68-amino acid repeats separated by linking …
- **Diseases (Open Targets)**: systemic lupus erythematosus (0.292); asthma (0.194); poisoning (0.193); stricture (0.193); neoplasm (0.115)
- **Europe PMC papers**: 1621
- **Why important**: ANXA6 is a high-connectivity node linked to both HSPA5 and HSPA8. Its calcium-dependent membrane and phospholipid-binding activity, together with reported roles in calcium transport, mitochondrial calcium homeostasis, and apoptotic signaling, provides a plausible membrane-and-calcium interface between chaperone activity and cytoskeletal or organelle remodeling. It is detected in both tissues and has established disease literature, though less extensive than the HSP70 genes.
- **Conclusion**: Established evidence supports ANXA6 as a calcium-sensitive membrane organizer within the module. Its network position makes it a plausible connector between proteostasis and membrane remodeling, but the supplied evidence does not demonstrate a direct physical complex or a causal role in the shared heart-myometrium state.

