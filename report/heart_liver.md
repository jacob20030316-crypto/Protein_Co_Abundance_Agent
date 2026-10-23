# Conserved co-abundance modules: heart and liver

## Module 0

**Tissue pair**: heart and liver  
**Genes (10)**: ACADM, ACADVL, AIFM1, ALDH2, DECR1, ETFDH, NNT, SDHA, ALDH5A1, SUCLG1

### Function

This is a conserved mitochondrial oxidative-metabolism module, with a particularly strong signature of oxidoreductase activity (GO:MF oxidoreductase activity; q_global = 0.00283) and flavin adenine dinucleotide binding (GO:MF flavin adenine dinucleotide binding; q_global = 0.00879). The genes collectively support mitochondrial electron transport, fatty-acid beta-oxidation, tricarboxylic-acid-cycle activity, aldehyde detoxification, and redox protection. The primary GO evidence is reinforced by STRING annotations for mitochondria, transit peptides, oxidoreductase activity, and FAD-related function (10 supplementary STRING terms; within-query FDR 0.00012–0.0389). The module therefore most plausibly represents coordinated mitochondrial energy production and redox homeostasis in heart and liver rather than a generic tissue-independent expression program.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, mitochondrial localization is frequent, and protein detection is broadly present in both heart and liver. Most genes have low immune-cell specificity, so a blood-cell explanation is unlikely; ALDH2 is the notable exception because it is immune-cell enhanced in classical monocytes and myeloid dendritic cells. The HPA pattern is tissue- and cell-type enriched, especially for hepatocytes, cardiomyocytes, myonuclei, and muscle-associated tissues, with liver and muscle signals recurring across the module. This supports a genuine parenchymal metabolic program, while shared hepatocyte and cardiomyocyte or muscle biology could contribute to its conservation between tissues. The two genes with low tissue specificity may provide a more broadly mitochondrial component.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF oxidoreductase activity | 0.00283 | ACADM, ACADVL, AIFM1, ALDH2, ALDH5A1, DECR1, ETFDH, NNT, SDHA |
| GO:MF flavin adenine dinucleotide binding | 0.00879 | ACADM, ACADVL, AIFM1, ETFDH, SDHA |

### STRING and hu.MAP

STRING provides a coherent but incomplete interaction framework. ACADM is connected to ACADVL, DECR1, and ETFDH, while ACADVL and ETFDH are connected; these relationships align with fatty-acid dehydrogenation and electron transfer. SDHA and SUCLG1 have a particularly strong known STRING relationship, consistent with linked respiratory-chain and tricarboxylic-acid-cycle functions. Other module genes lack recorded high-confidence STRING partners within this set, so the co-abundance structure is substantially broader than the currently documented pairwise interaction structure. hu.MAP contributes one partial complex association (hu.MAP huMAP3_12388.1), containing ACADM and NNT together with electron-transfer flavoprotein components and other proteins outside the module. Thus, some relationships are already established, but the full module should not be interpreted as one experimentally defined physical complex; it is better viewed as a coordinated mitochondrial pathway-level program.

**STRING interactions (score >= 0.7)**: 5 of 45 gene pairs: ACADM–ACADVL (0.713); ACADM–DECR1 (0.755); ACADM–ETFDH (0.766); ACADVL–ETFDH (0.817); SDHA–SUCLG1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transit peptide (FDR = 0.00012, 10 genes); Keyword Mitochondrion (FDR = 0.0013, 10 genes); Keyword Oxidoreductase (FDR = 0.0013, 8 genes); Keyword FAD (FDR = 0.0018, 5 genes); Function Oxidoreductase activity (FDR = 0.0023, 9 genes); Function Flavin adenine dinucleotide binding (FDR = 0.0035, 5 genes); Function Nucleotide binding (FDR = 0.0128, 9 genes); COMPARTMENTS Mitochondrion (FDR = 0.0164, 10 genes); Function Oxidoreductase activity, acting on the CH-CH group of donors (FDR = 0.0268, 4 genes); Component Mitochondrion (FDR = 0.0389, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12388.1 (ACADM, NNT; 2/7)

### Novelty

The module is unlikely to be a wholly unknown biological pathway: its core functions, mitochondrial localization, fatty-acid oxidation genes, respiratory-chain genes, and several pairwise relationships are already established in gene annotations, STRING, and hu.MAP. Nevertheless, the specific conserved heart–liver co-abundance organization may be a new systems-level observation. The limited overlap with known complexes and the incomplete STRING connectivity indicate that the novelty, if confirmed, lies in the cross-tissue coordination and module architecture rather than in discovery of previously unrecognized functions for the individual genes. Absence of a relationship from STRING or hu.MAP is not evidence of novelty by itself. Independent replication, preservation in additional cohorts, and testing against cellular composition and physiological covariates would be needed to establish that the module is not driven only by shared tissue or cell-type abundance.

**Hypothesis.** Hypothesis: in both heart and liver, the module coordinates mitochondrial fatty-acid entry and beta-oxidation with electron transfer, respiratory-chain flux, and protection from reactive oxygen species. ACADM and ACADVL initiate oxidation of medium-chain and long-chain or very-long-chain fatty acids, DECR1 assists processing of unsaturated intermediates, and ETFDH transfers reducing equivalents from flavin-containing dehydrogenases into the respiratory chain. SDHA and SUCLG1 connect this program to succinate oxidation and tricarboxylic-acid-cycle energy metabolism, while NNT can supply NADPH for antioxidant and biosynthetic reactions. ALDH2 and ALDH5A1 may reduce aldehyde and other toxic metabolite burden, and AIFM1 may link mitochondrial redox state to apoptosis and respiratory-chain biology. The proposed mechanism is a coordinated response that matches high energetic demand with fatty-acid oxidation and redox control; it remains a hypothesis because co-abundance does not establish biochemical interaction or causal regulation.

### Important genes

#### SDHA

- **Related proteins** (co-abundance neighbors): SUCLG1 (0.83), NNT (0.82), ALDH5A1 (0.81), AIFM1 (0.80); STRING partners: SUCLG1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate dehydrogenase complex flavoprotein subunit A. This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identi…
- **Diseases (Open Targets)**: mitochondrial complex II deficiency, nuclear type 1 (0.813); pheochromocytoma/paraganglioma syndrome 5 (0.790); dilated cardiomyopathy 1GG (0.768); neurodegeneration with ataxia and late-onset optic atrophy (0.761); gastrointestinal stromal tumor (0.743)
- **Europe PMC papers**: 12756
- **Why important**: SDHA is the strongest network hub in the module and connects the respiratory-chain component to SUCLG1, NNT, ALDH5A1, and AIFM1. It is present in both primary GO terms (GO:MF oxidoreductase activity; q_global = 0.00283) (GO:MF flavin adenine dinucleotide binding; q_global = 0.00879) and all listed STRING functional categories (10 supplementary STRING terms; within-query FDR 0.00012–0.0389). Its established role as the catalytic subunit of succinate dehydrogenase directly links the module to succinate oxidation, the tricarboxylic-acid cycle, and mitochondrial electron transport. Its disease associations include mitochondrial complex II deficiency, Leigh syndrome, cardiomyopathy, and other mitochondrial disorders, and its literature support is extensive.
- **Conclusion**: Established conclusion: SDHA is a central respiratory-chain and tricarboxylic-acid-cycle anchor of the module. Hypothesis: its network position may couple fatty-acid-derived reducing equivalents to respiratory-chain capacity and influence the shared heart–liver metabolic state.

#### ETFDH

- **Related proteins** (co-abundance neighbors): ALDH2 (0.87), ACADM (0.86), ACADVL (0.85); STRING partners: ACADM (0.766), ACADVL (0.817)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein dehydrogenase. This gene encodes a component of the electron-transfer system in mitochondria and is essential for electron transfer from a number of mitochondrial flavin-containing dehydrogenases to the main respiratory chain. Mutations in this gene are associated with glutaric acidemia. Alternatively spliced transcript variants that encode distinct isoforms have been observed. [provided by RefSeq, Aug 2013].
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.845); glutaric acidemia IIc (0.704); glutaric aciduria (0.670); hereditary disease (0.523); Abnormality of metabolism/homeostasis (0.407)
- **Europe PMC papers**: 1273
- **Why important**: ETFDH is a prominent connector among ACADM, ACADVL, and ALDH2 and is present in both primary GO terms (GO:MF oxidoreductase activity; q_global = 0.00283) (GO:MF flavin adenine dinucleotide binding; q_global = 0.00879) and nearly all supplementary mitochondrial and oxidoreductase categories (9 supplementary STRING terms; within-query FDR 0.00012–0.0389). Its established function is to transfer electrons from multiple mitochondrial flavin-containing dehydrogenases to the respiratory chain, making it a mechanistic bridge between fatty-acid oxidation and respiration. Its disease associations include multiple acyl-CoA dehydrogenase deficiency and glutaric acidemia, with substantial literature support.
- **Conclusion**: Established conclusion: ETFDH is a key electron-transfer interface that explains why fatty-acid dehydrogenases and respiratory metabolism co-occur in the module. Hypothesis: coordinated ETFDH abundance may buffer tissue energy demand by maintaining electron flow from several lipid-oxidation inputs.

#### ACADM

- **Related proteins** (co-abundance neighbors): ETFDH (0.86); STRING partners: ACADVL (0.713), DECR1 (0.755), ETFDH (0.766)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, liver
- **hu.MAP 3.0**: huMAP3_12388.1
- **Function (MyGene.info)**: acyl-CoA dehydrogenase medium chain. This gene encodes the medium-chain specific (C4 to C12 straight chain) acyl-Coenzyme A dehydrogenase. The homotetramer enzyme catalyzes the initial step of the mitochondrial fatty acid beta-oxidation pathway. Defects in this gene cause medium-chain acyl-CoA dehydrogenase deficiency, a disease characterized by hepatic dysfunction, fasting hypoglycemia, and encephalopathy, which can result in infant…
- **Diseases (Open Targets)**: medium chain acyl-CoA dehydrogenase deficiency (0.854); hereditary disease (0.516); rhabdomyolysis (0.370); short chain acyl-CoA dehydrogenase deficiency (0.349); Epileptic spasm (0.333)
- **Europe PMC papers**: 4795
- **Why important**: ACADM is connected to ETFDH, ACADVL, and DECR1 in STRING and participates in both globally significant GO terms (GO:MF oxidoreductase activity; q_global = 0.00283) (GO:MF flavin adenine dinucleotide binding; q_global = 0.00879) as well as the complete set of listed STRING functional categories (10 supplementary STRING terms; within-query FDR 0.00012–0.0389). It catalyzes the first step of medium-chain fatty-acid beta-oxidation and is linked to hepatic dysfunction, fasting hypoglycemia, and encephalopathy when defective. Its HPA pattern includes liver and skeletal muscle enrichment, and it has substantial literature and disease evidence.
- **Conclusion**: Established conclusion: ACADM is a representative entry point for mitochondrial fatty-acid oxidation and a major explanation for the module's oxidoreductase and FAD signature. Hypothesis: its co-abundance with ETFDH and ACADVL reflects coordinated adjustment of lipid fuel utilization across hepatocytes and contractile muscle cells.

#### NNT

- **Related proteins** (co-abundance neighbors): SDHA (0.82), DECR1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, liver
- **hu.MAP 3.0**: huMAP3_12388.1
- **Function (MyGene.info)**: nicotinamide nucleotide transhydrogenase. This gene encodes an integral protein of the inner mitochondrial membrane. The enzyme couples hydride transfer between NAD(H) and NADP(+) to proton translocation across the inner mitochondrial membrane. Under most physiological conditions, the enzyme uses energy from the mitochondrial proton gradient to produce high concentrations of NADPH. The resulting NADPH is used for biosynthesis and in free …
- **Diseases (Open Targets)**: familial glucocorticoid deficiency (0.638); neurodegenerative disease (0.497); hereditary disease (0.453); atypical hemolytic-uremic syndrome with DGKE deficiency (0.416); Abnormality of the skeletal system (0.396)
- **Europe PMC papers**: 6111
- **Why important**: NNT links to SDHA and DECR1 in the module network and is part of the globally significant oxidoreductase term (GO:MF oxidoreductase activity; q_global = 0.00283). It is also included in the hu.MAP association (hu.MAP huMAP3_12388.1) with ACADM and electron-transfer flavoprotein components. Its established function is to use the mitochondrial proton gradient to generate NADPH, which supports biosynthesis and free-radical detoxification. HPA identifies cardiomyocytes and hepatocytes among its enhanced cell types, and its disease associations include familial glucocorticoid deficiency and broader mitochondrial or hereditary disorders.
- **Conclusion**: Established conclusion: NNT supplies a biologically plausible redox-protection function within this energy-metabolism module. Hypothesis: NNT may couple respiratory activity and fatty-acid oxidation to NADPH-dependent control of oxidative stress in both tissues.

#### ALDH2

- **Related proteins** (co-abundance neighbors): ETFDH (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 2 family member. This protein belongs to the aldehyde dehydrogenase family of proteins. Aldehyde dehydrogenase is the second enzyme of the major oxidative pathway of alcohol metabolism. Two major liver isoforms of aldehyde dehydrogenase, cytosolic and mitochondrial, can be distinguished by their electrophoretic mobilities, kinetic properties, and subcellular localizations. Most Caucasians have two major isozymes, …
- **Diseases (Open Targets)**: alcohol dependence (0.654); alcohol drinking (0.549); AMED syndrome, digenic (0.503); gout (0.501); atrial fibrillation (0.469)
- **Europe PMC papers**: 7978
- **Why important**: ALDH2 is included in the primary oxidoreductase term (GO:MF oxidoreductase activity; q_global = 0.00283) and in multiple supplementary mitochondrial and oxidoreductase categories (10 supplementary STRING terms; within-query FDR 0.00012–0.0389). It is liver enhanced and hepatocyte enriched, and its established function is aldehyde catabolism, including the mitochondrial component of alcohol metabolism. Its disease associations include alcohol-related phenotypes, gout, and atrial fibrillation. Although it is peripheral in the network and lacks a listed high-confidence STRING partner within the module, its biochemical role connects mitochondrial metabolism with detoxification of reactive aldehydes.
- **Conclusion**: Established conclusion: ALDH2 adds a liver-relevant detoxification and aldehyde-redox dimension to the module. Hypothesis: its co-abundance with ETFDH may indicate protection against aldehyde stress generated or amplified during high mitochondrial lipid and respiratory flux.

## Module 1

**Tissue pair**: heart and liver  
**Genes (8)**: ACSL1, SERPINC1, MAOA, BDH1, C3, COQ9, LDHD, DBT

### Function

This is not a canonically enriched GO or KEGG module: no GO or KEGG term passed global correction, and STRING functional enrichment was absent. The biological signal is therefore best interpreted as a mixed metabolic and liver-associated module rather than a formally established pathway. ACSL1 is the central network connector and supports long-chain fatty-acyl-CoA formation, linking lipid biosynthesis and fatty-acid degradation with COQ9-associated ubiquinone biology, LDHD-associated hydroxyacid metabolism, BDH1-associated ketone-body metabolism, and DBT-associated branched-chain amino-acid catabolism. MAOA adds mitochondrial amine oxidation, while C3 and SERPINC1 represent complement and coagulation biology. The module may thus reflect coordinated liver and heart metabolic state together with circulating liver-derived proteins, rather than one intracellular biochemical complex.

**Cell composition.** The module is tissue-associated rather than broadly housekeeping-like: HPA profiles frequently point to liver and hepatocytes, with additional signals in skeletal muscle, adipose tissue, intestine, and heart muscle. C3 and SERPINC1 are secreted to blood and have liver-enriched profiles, making plasma carryover or shared liver-secretory biology an important alternative explanation for their co-abundance. The HPA pattern does not indicate that the module is predominantly blood-cell derived. Immune-cell annotations are mixed and limited, including signals involving neutrophils, monocytes, and basophils, while several genes have low immune-cell specificity or are not detected in immune cells. Protein detection in heart and liver supports presence of much of the module in both tissues, but the lack of tissue immunohistochemical detection for the secreted proteins argues for caution when interpreting the module as a tissue-intrinsic protein complex.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, so the co-abundance structure is not corroborated by known STRING physical or functional links at the supplied threshold. hu.MAP provides more specific but partial support: ACSL1 and BDH1 co-occur in several complexes (hu.MAP huMAP3_07756.1), (hu.MAP huMAP3_09371.1), (hu.MAP huMAP3_05801.1), and (hu.MAP huMAP3_11084.1), indicating a recurring association in mitochondrial or metabolic-complex contexts, although each complex contains many proteins outside the module. C3 and SERPINC1 co-occur in a large hu.MAP complex (hu.MAP huMAP3_15040.1) that is rich in plasma, complement, coagulation, and apolipoprotein proteins; this supports a shared circulating-protein context but does not establish a direct interaction between them. Overall, the network is better viewed as a co-abundance relationship with limited support from known molecular complexes, not as a demonstrated physical complex.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07756.1 (ACSL1, BDH1; 2/4); huMAP3_09371.1 (ACSL1, BDH1; 2/12); huMAP3_05801.1 (ACSL1, BDH1; 2/13); huMAP3_11084.1 (ACSL1, BDH1; 2/27); huMAP3_15040.1 (SERPINC1, C3; 2/64)

### Novelty

The exact conserved heart–liver co-abundance module may be a new systems-level observation, because the supplied resources do not show a matching STRING interaction network or a compact hu.MAP complex containing the full module. However, it should not be described as a newly discovered molecular pathway. The constituent functions are established, ACSL1–BDH1 membership recurs in hu.MAP complexes (hu.MAP huMAP3_07756.1), (hu.MAP huMAP3_09371.1), (hu.MAP huMAP3_05801.1), and (hu.MAP huMAP3_11084.1), and the C3–SERPINC1 context overlaps a known plasma-protein complex (hu.MAP huMAP3_15040.1). Absence from STRING or partial representation in hu.MAP alone cannot prove novelty. The strongest novelty claim is therefore the conserved cross-tissue co-abundance pattern and its combination of mitochondrial metabolism with liver-derived circulating proteins, pending independent replication and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a shared heart–liver metabolic and secretory state in which fatty-acid activation through ACSL1 is coordinated with mitochondrial ketone-body, ubiquinone, branched-chain amino-acid, amine, and hydroxyacid metabolism, while hepatocyte-derived C3 and SERPINC1 enter the measured protein pool as circulating components. The apparent module could therefore arise from coordinated metabolic physiology plus blood or plasma contribution, rather than direct binding among all members. Testing this hypothesis would require separating tissue-resident protein from plasma contamination, examining cell-type-resolved data, and measuring whether the metabolic genes and secreted proteins change together under defined metabolic or inflammatory conditions.

### Important genes

#### ACSL1

- **Related proteins** (co-abundance neighbors): MAOA (0.88), COQ9 (0.83), LDHD (0.81), BDH1 (0.81), C3 (0.81), SERPINC1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in heart, liver
- **hu.MAP 3.0**: huMAP3_07756.1, huMAP3_09371.1, huMAP3_05801.1, huMAP3_11084.1
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 1. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. Several transcript variants enco…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.510); diabetes mellitus (0.501); diabetic neuropathy (0.404); neurodegenerative disease (0.368); menopause (0.334)
- **Europe PMC papers**: 4992
- **Why important**: ACSL1 is the principal network connector, linking most of the module's metabolic and circulating-protein members. Its established role is conversion of long-chain fatty acids into fatty acyl-CoA esters, and its HPA profile is enhanced in liver, adipose tissue, and skeletal muscle with detection in heart and liver. It also participates with BDH1 in several hu.MAP complexes (hu.MAP huMAP3_07756.1), (hu.MAP huMAP3_09371.1), (hu.MAP huMAP3_05801.1), and (hu.MAP huMAP3_11084.1). Its disease associations include diabetes-related conditions, and its literature volume is substantial.
- **Conclusion**: Established evidence supports ACSL1 as the module's metabolic hub and a plausible anchor for liver–heart lipid physiology. It is a hypothesis, not an established fact, that ACSL1 drives the co-abundance of the secreted proteins or explains the entire module.

#### BDH1

- **Related proteins** (co-abundance neighbors): ACSL1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, liver
- **hu.MAP 3.0**: huMAP3_07756.1, huMAP3_09371.1, huMAP3_05801.1, huMAP3_11084.1
- **Function (MyGene.info)**: 3-hydroxybutyrate dehydrogenase 1. This gene encodes a member of the short-chain dehydrogenase/reductase gene family. The encoded protein forms a homotetrameric lipid-requiring enzyme of the mitochondrial membrane and has a specific requirement for phosphatidylcholine for optimal enzymatic activity. The encoded protein catalyzes the interconversion of acetoacetate and (R)-3-hydroxybutyrate, the two major ketone bodies produced duri…
- **Diseases (Open Targets)**: anemia (phenotype) (0.201); preeclampsia (0.107); diabetic kidney disease (0.081); type 2 diabetes mellitus (0.079); lung cancer (0.078)
- **Europe PMC papers**: 1501
- **Why important**: BDH1 is directly connected to ACSL1 and recurs with ACSL1 in the hu.MAP complexes (hu.MAP huMAP3_07756.1), (hu.MAP huMAP3_09371.1), (hu.MAP huMAP3_05801.1), and (hu.MAP huMAP3_11084.1). It is a mitochondrial ketone-body enzyme, is liver-enriched, and is detected in both heart and liver. Its function provides a mechanistic bridge between fatty-acid catabolism and ketone-body production, with disease annotations involving metabolic and renal disorders.
- **Conclusion**: Established evidence supports BDH1 as a relevant mitochondrial metabolic partner within the module. Its role as a functional mediator connecting ACSL1-driven lipid handling to the circulating proteins remains a hypothesis.

#### C3

- **Related proteins** (co-abundance neighbors): ACSL1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a liver-enriched, hepatocyte-associated protein secreted to blood and is central to complement activation and inflammatory signaling. It is connected to ACSL1 in the module and appears with SERPINC1 in the plasma-rich hu.MAP complex (hu.MAP huMAP3_15040.1). C3 has extensive literature and strong associations with complement disorders and inflammatory disease, making it an important indicator of extracellular or blood-derived biology.
- **Conclusion**: Established evidence supports C3 as a circulating complement component and a likely contributor to the module's liver-secretory or plasma signal. It is not established that C3 physically interacts with ACSL1 or that complement activation causes the metabolic co-abundance pattern.

#### SERPINC1

- **Related proteins** (co-abundance neighbors): ACSL1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 is a liver-enriched hepatocyte protein secreted to blood and encodes antithrombin, an established inhibitor of thrombin and other coagulation proteases. It connects to ACSL1 in the module and joins C3 in the plasma-associated hu.MAP complex (hu.MAP huMAP3_15040.1). Its disease associations with antithrombin deficiency and venous thrombosis, together with substantial literature, make it a strong marker of coagulation and circulating-protein biology.
- **Conclusion**: Established evidence supports SERPINC1 as a liver-derived plasma coagulation regulator and a possible indicator of sample blood content. A direct mechanistic link between SERPINC1 and the mitochondrial metabolic genes is only a hypothesis.

#### MAOA

- **Related proteins** (co-abundance neighbors): ACSL1 (0.88), DBT (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Mitochondria; IHC detected in heart, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: monoamine oxidase A. This gene is one of two neighboring gene family members that encode mitochondrial enzymes which catalyze the oxidative deamination of amines, such as dopamine, norepinephrine, and serotonin. Mutation of this gene results in Brunner syndrome. This gene has also been associated with a variety of other psychiatric disorders, including antisocial behavior. Alternatively spliced transcript variants enc…
- **Diseases (Open Targets)**: Brunner syndrome (0.788); major depressive disorder (0.613); depressive disorder (0.544); hypertensive disorder (0.464); hereditary disease (0.451)
- **Europe PMC papers**: 7415
- **Why important**: MAOA forms a bridge between ACSL1 and DBT in the co-abundance graph and encodes a mitochondrial enzyme that oxidatively deaminates biogenic amines. It is detected in heart and liver and has extensive literature and disease associations including Brunner syndrome and psychiatric disorders. Its position connects lipid-associated network structure with amine and branched-chain amino-acid metabolism, although no STRING or hu.MAP support is reported.
- **Conclusion**: Established evidence supports MAOA as a mitochondrial amine-metabolism enzyme and a structurally informative connector in this module. Its participation in a shared heart–liver metabolic program is plausible but remains a hypothesis because the relationship is based on co-abundance rather than established molecular interaction.

## Module 2

**Tissue pair**: heart and liver  
**Genes (21)**: ANXA2, BCAM, CKAP4, CLIC1, DYNC1I2, DNM2, FKBP3, GSTP1, IMPDH2, PKM, PSMC4, RPL12, RUVBL2, SEPTIN2, SEPTIN7, SERPINH1, SNX6, SRSF7, TFRC, TXNDC5, XRCC6

### Function

This is a heterogeneous cellular-state module rather than a cleanly defined pathway. Its genes span endoplasmic-reticulum protein folding and collagen chaperoning through SERPINH1 and TXNDC5, guanine-nucleotide production through IMPDH2, glycolysis and redox or xenobiotic handling through PKM and GSTP1, cytoskeletal and membrane organization through the septins, ANXA2, CLIC1, DNM2 and DYNC1I2, intracellular trafficking through SNX6 and TFRC, and nuclear maintenance through RUVBL2, XRCC6, PSMC4, RPL12 and SRSF7. No GO or KEGG term passed global correction, so no pathway-level enrichment can be claimed. The network nevertheless contains several biologically coherent functional threads, including proteostasis, membrane trafficking, cytoskeletal organization, metabolism and stress responses.

**Cell composition.** The module is not dominated by secreted or plasma proteins: only a minority are annotated as secreted, and most are intracellular or membrane-associated. It is also not strongly blood-cell restricted. HPA reports low immune-cell specificity for most genes, although a limited subset is enhanced in monocytes, basophils, platelets, dendritic cells or neutrophils. Most genes have low tissue specificity, while several show enrichment in esophageal, skeletal-muscle or tongue-related tissues and diverse specialized cell types. The presence of broadly expressed housekeeping-like components, including ribosomal, proteasomal, DNA-repair, metabolic and trafficking proteins, means that the heart–liver signal could reflect a shared general cellular state or shared cell populations rather than a liver–heart-specific biochemical pathway. HPA protein detection is broadly compatible with the module being present in both tissues, but several central genes lack tissue-level IHC detection in one or both queried tissues, so protein-level interpretation should remain cautious.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a small amount of high-confidence support within the module. The established pair ANXA2–CLIC1 is consistent with membrane-associated, vesicular and cytoskeletal biology, while SEPTIN2–SEPTIN7 is a very strong known septin relationship. STRING reports no functional enrichment for the module. hu.MAP independently supports the SEPTIN2–SEPTIN7 pairing in the septin complex (hu.MAP huMAP3_02362.1). It also places TFRC and CKAP4 in a large membrane, organelle and trafficking-associated complex (hu.MAP huMAP3_10725.1), although they represent only a small portion of that complex. Most other module edges are not supported by the supplied STRING or hu.MAP records. Thus, the network is not a single established complex; it is a co-abundance structure containing a few known physical relationships embedded among broader, potentially indirect associations.

**STRING interactions (score >= 0.7)**: 2 of 210 gene pairs: ANXA2–CLIC1 (0.713); SEPTIN2–SEPTIN7 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02362.1 (SEPTIN2, SEPTIN7; 2/14); huMAP3_10725.1 (TFRC, CKAP4; 2/59)

### Novelty

The module may be a new tissue-pair co-abundance finding, but the available evidence does not establish that it is a new molecular complex or a new biological pathway. Its strongest internal relationships are already recognized by STRING or hu.MAP, especially the septin pair and the ANXA2–CLIC1 interaction, and most individual genes have substantial prior literature. Conversely, the absence of broad STRING or hu.MAP coverage cannot prove novelty because co-abundance can arise from shared regulation, cell composition, localization, or condition-dependent biology. The defensible conclusion is that the heart–liver co-abundance pattern is potentially novel as a module-level observation, while its component functions and some relationships are established.

**Hypothesis.** Hypothesis: the module records a shared cellular adaptation in heart and liver that couples proteostasis and stress handling in the endoplasmic reticulum with cytoskeletal remodeling, vesicle or receptor trafficking, redox control, glycolytic or nucleotide metabolism, and macromolecular quality control. SERPINH1 and TXNDC5 could mark folding or secretory stress, IMPDH2 and PKM could support biosynthetic and energetic demand, GSTP1 and CLIC1 could buffer oxidative or membrane stress, and septins, ANXA2, DNM2, DYNC1I2 and SNX6 could coordinate membrane organization and transport. This is a mechanistic model, not an enrichment result; it should be tested by examining cell-type composition, perturbation responses, and protein-level co-variation within each tissue.

### Important genes

#### SERPINH1

- **Related proteins** (co-abundance neighbors): RUVBL2 (0.89), TFRC (0.84), CKAP4 (0.84), XRCC6 (0.83), IMPDH2 (0.83), CLIC1 (0.81), TXNDC5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family H member 1. This gene encodes a member of the serpin superfamily of serine proteinase inhibitors. The encoded protein is localized to the endoplasmic reticulum and plays a role in collagen biosynthesis as a collagen-specific molecular chaperone. Autoantibodies to the encoded protein have been found in patients with rheumatoid arthritis. Expression of this gene may be a marker for cancer, and nucleotide polymo…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 10 (0.714); preterm premature rupture of the membranes (0.559); coronary artery disorder (0.554); myocardial infarction (0.510); Abnormality of the skeletal system (0.474)
- **Europe PMC papers**: 2762
- **Why important**: SERPINH1 is among the most central nodes in the module and connects the proteostasis-related, nuclear-maintenance, metabolic and membrane-associated portions of the network. Its established role is an endoplasmic-reticulum collagen-specific chaperone involved in protein folding and collagen organization. It also has extensive literature and disease associations involving skeletal abnormalities, preterm membrane rupture and cardiovascular disorders.
- **Conclusion**: Established evidence supports SERPINH1 as a proteostasis and collagen-biosynthesis component with a central network position. Its co-abundance here may indicate shared folding or matrix-related cellular stress, but the module does not prove that SERPINH1 regulates the other genes.

#### IMPDH2

- **Related proteins** (co-abundance neighbors): TXNDC5 (0.85), CKAP4 (0.85), BCAM (0.84), SERPINH1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inosine monophosphate dehydrogenase 2. This gene encodes the rate-limiting enzyme in the de novo guanine nucleotide biosynthesis. It is thus involved in maintaining cellular guanine deoxy- and ribonucleotide pools needed for DNA and RNA synthesis. The encoded protein catalyzes the NAD-dependent oxidation of inosine-5'-monophosphate into xanthine-5'-monophosphate, which is then converted into guanosine-5'-monophosphate. This gene is up-…
- **Diseases (Open Targets)**: acute lymphoblastic leukemia (0.529); Crohn disease (0.447); acute myeloid leukemia (0.421); lupus nephritis (0.408); myelodysplastic syndrome (0.403)
- **Europe PMC papers**: 1438
- **Why important**: IMPDH2 links the central network to nucleotide metabolism and is connected to CKAP4, TXNDC5, BCAM and SERPINH1. It is the rate-limiting enzyme for de novo guanine-nucleotide production, supporting DNA and RNA synthesis. Its literature and disease associations include hematologic malignancy, inflammatory disease and neoplasia.
- **Conclusion**: Established evidence supports IMPDH2 as a biosynthetic and growth-associated metabolic enzyme. In this module it could report increased demand for nucleotide supply during stress or remodeling, but that interpretation remains a hypothesis because no global enrichment supports it.

#### GSTP1

- **Related proteins** (co-abundance neighbors): TFRC (0.85), SEPTIN2 (0.81), ANXA2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in heart, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutathione S-transferase pi 1. Glutathione S-transferases (GSTs) are a family of enzymes that play an important role in detoxification by catalyzing the conjugation of many hydrophobic and electrophilic compounds with reduced glutathione. Based on their biochemical, immunologic, and structural properties, the soluble GSTs are categorized into 4 main classes: alpha, mu, pi, and theta. This GST family member is a polymorphic gene…
- **Diseases (Open Targets)**: neurodegenerative disease (0.350); breast cancer (0.117); hepatocellular carcinoma (0.115); neoplasm (0.114); posterior cortical atrophy (0.113)
- **Europe PMC papers**: 12759
- **Why important**: GSTP1 occupies a bridge-like position between TFRC, SEPTIN2 and ANXA2. It is a well-studied glutathione-transferase involved in detoxification, glutathione metabolism, oxidative-stress responses and inflammatory regulation. It has very extensive literature and disease associations including liver cancer and other neoplastic or neurodegenerative conditions.
- **Conclusion**: Established evidence supports GSTP1 as a redox and xenobiotic-defense protein. Its position suggests that oxidative or electrophilic stress could connect metabolic, membrane and cytoskeletal components of the module, but the co-abundance data do not identify the causal direction.

#### SEPTIN2

- **Related proteins** (co-abundance neighbors): SEPTIN7 (0.87), GSTP1 (0.81), PSMC4 (0.81), CLIC1 (0.81); STRING partners: SEPTIN7 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Actin filaments; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_02362.1
- **Function (MyGene.info)**: septin 2. Enables identical protein binding activity. Predicted to be involved in several processes, including cilium assembly; regulation of exocytosis; and smoothened signaling pathway. Predicted to act upstream of or within regulation of L-glutamate import across plasma membrane and regulation of protein localization. Located in several cellular components, including cytoskeleton; photoreceptor connectin…
- **Diseases (Open Targets)**: hypothyroidism (0.239); squamous cell carcinoma (0.201); ischemic stroke (0.189); coronary artery disorder (0.181); skin cancer (0.181)
- **Europe PMC papers**: 281
- **Why important**: SEPTIN2 is a cytoskeletal node connected to SEPTIN7, GSTP1, PSMC4 and CLIC1. It is an established septin-complex component involved in cytoskeleton organization, intracellular localization, cilium biology and cytokinesis. Its relationship with SEPTIN7 is supported by both STRING and hu.MAP (hu.MAP huMAP3_02362.1).
- **Conclusion**: Established evidence supports SEPTIN2 as the clearest structural-complex anchor in the module. The SEPTIN2–SEPTIN7 relationship is real and known, while the wider connection of septins to redox, proteostasis and metabolism is a plausible module-level hypothesis rather than a demonstrated physical complex.

#### TFRC

- **Related proteins** (co-abundance neighbors): GSTP1 (0.85), SERPINH1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes, Lysosomes; IHC detected in heart, liver
- **hu.MAP 3.0**: huMAP3_10725.1
- **Function (MyGene.info)**: transferrin receptor. This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: TFRC-related combined immunodeficiency (0.623); type 2 diabetes mellitus (0.518); mucopolysaccharidosis type 2 (0.490); diabetes mellitus (0.471); diabetic retinopathy (0.343)
- **Europe PMC papers**: 14164
- **Why important**: TFRC connects the module to iron uptake and endosomal or lysosomal trafficking and is linked in the network to GSTP1 and SERPINH1. It is detected in both queried tissues, is secreted to blood according to HPA, and is associated with erythropoiesis, hypoxia responses, iron homeostasis and receptor-mediated endocytosis. It also has extensive literature and clinically relevant disease associations.
- **Conclusion**: Established evidence supports TFRC as an iron-uptake and trafficking receptor. Its presence may indicate metabolic or hypoxic demand, or shared vascular or blood-related material in tissue samples. The data do not distinguish those possibilities, and TFRC should not by itself be interpreted as evidence of a blood-derived module.

## Module 3

**Tissue pair**: heart and liver  
**Genes (16)**: ATP1A1, CLTC, DYNC1H1, EIF3L, FLOT1, IQGAP1, MYL9, RAB10, RO60, SPTBN1, KARS1, QARS1, CCT7, TLN1, XPO1, CSE1L

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established pathway-level annotation from GO or KEGG. Its architecture instead suggests a mixed intracellular organization module involving membrane and cytoskeletal organization, vesicle trafficking, nuclear transport, translation, and protein folding. The supplementary STRING result (STRING RCTM Signaling by Rho GTPases; within-query FDR = 0.021) is consistent with signaling by Rho GTPases and includes CCT7, IQGAP1, MYL9, DYNC1H1, SPTBN1, FLOT1, XPO1, and CLTC, but this is supportive rather than globally corrected evidence. The higher-connectivity genes ATP1A1 and XPO1 link several of these processes, while the remaining branches connect adhesion and cytoskeletal proteins, transport proteins, and translation machinery.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only one secreted gene, and most proteins are intracellular or membrane-associated. Most genes have low tissue specificity, with protein detected in both heart and liver for the majority of genes represented in the HPA protein summary. This favors a broadly expressed cellular program rather than a heart- or liver-specific function. The module is also not strongly blood-cell enriched overall, because most genes have low immune-cell specificity, although neutrophil, eosinophil, platelet, megakaryocyte, endothelial, and vascular associations occur for subsets of genes. Enrichment for spermatid-related cell types and occasional vascular or blood-cell annotations could reflect shared cell-state or cellular-composition effects in tissue samples. The module should therefore not be interpreted as a dedicated cardiomyocyte or hepatocyte program without independent cell-composition validation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides three high-confidence within-module relationships: CSE1L-XPO1, IQGAP1-TLN1, and KARS1-QARS1. The CSE1L-XPO1 pair supports a nuclear transport relationship, IQGAP1-TLN1 supports adhesion and cytoskeletal signaling, and KARS1-QARS1 supports aminoacyl-tRNA synthetase biology. The supplementary Rho GTPase term (STRING RCTM Signaling by Rho GTPases; within-query FDR = 0.021) adds contextual support for cytoskeletal and trafficking coordination, but it is not global enrichment evidence. hu.MAP independently places KARS1 and QARS1 together in complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), and places XPO1 and CSE1L together in several complexes (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_09592.1). FLOT1 and SPTBN1 co-occur in (hu.MAP huMAP3_09165.1). These repeated pairings indicate that some module edges reflect established molecular relationships, whereas the sparse overall STRING connectivity and absence of hu.MAP support for many other genes suggest that the complete module is not a single established complex.

**STRING interactions (score >= 0.7)**: 3 of 120 gene pairs: CSE1L–XPO1 (0.976); IQGAP1–TLN1 (0.893); KARS1–QARS1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Signaling by Rho GTPases (FDR = 0.021, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (QARS1, KARS1; 2/14); huMAP3_13688.1 (QARS1, KARS1; 2/14); huMAP3_07170.1 (XPO1, CSE1L; 2/14); huMAP3_09042.1 (XPO1, CSE1L; 2/26); huMAP3_06791.1 (XPO1, CSE1L; 2/31); huMAP3_09165.1 (FLOT1, SPTBN1; 2/39); huMAP3_09592.1 (XPO1, CSE1L; 2/95)

### Novelty

The module is unlikely to represent a previously defined canonical complex because only selected gene pairs are supported by STRING or hu.MAP, and no GO/KEGG term passes global correction. Its potential novelty lies in the coordinated co-abundance of several otherwise distinct processes across heart and liver, especially the combination of nuclear export, membrane-cytoskeletal organization, vesicle trafficking, translation support, and chaperoning. However, absence from STRING or hu.MAP alone cannot establish novelty. The finding should be treated as a potentially new tissue-level co-abundance association that requires replication, control for cell composition, and independent validation of the cross-tissue reproducibility.

**Hypothesis.** Hypothesis: the module reflects a shared cellular logistics state in heart and liver in which membrane transport and adhesion are coordinated with cytoskeletal remodeling, intracellular cargo movement, nuclear export, and protein synthesis or folding. ATP1A1, RAB10, CLTC, SPTBN1, TLN1, IQGAP1, MYL9, and FLOT1 could represent the membrane, vesicle, and cytoskeletal arm; XPO1 and CSE1L the nuclear transport arm; and KARS1, QARS1, EIF3L, and CCT7 the translation and proteostasis arm. This may represent a common structural or vascular-associated cellular component shared by the tissues, but it could also partly arise from shared non-parenchymal cell types or sample composition. The hypothesis is not established by the enrichment analysis.

### Important genes

#### ATP1A1

- **Related proteins** (co-abundance neighbors): CLTC (0.88), XPO1 (0.86), SPTBN1 (0.85), EIF3L (0.84), RAB10 (0.82), CCT7 (0.80), CSE1L (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 is the highest-connectivity node in the module and links XPO1, SPTBN1, CLTC, EIF3L, RAB10, CCT7, and CSE1L. Its established function is maintaining sodium and potassium electrochemical gradients, which can influence membrane transport, excitability, and sodium-coupled solute handling. Its disease associations include cardiac and neurological disorders, and it has substantial literature support. HPA places it at the plasma membrane and vesicles, with tissue enhancement in parathyroid gland and cell-type enhancement in several epithelial and vascular-related cell types.
- **Conclusion**: Established evidence supports ATP1A1 as a central membrane homeostasis and transport-associated hub. Its position supports a coordinating role in the module, but the data do not establish that ATP1A1 drives the co-abundance pattern or that the module is specifically cardiac or hepatic.

#### XPO1

- **Related proteins** (co-abundance neighbors): ATP1A1 (0.86), EIF3L (0.85), RAB10 (0.84), QARS1 (0.82), CCT7 (0.81), RO60 (0.80); STRING partners: CSE1L (0.976)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_07170.1, huMAP3_09042.1, huMAP3_06791.1, huMAP3_09592.1
- **Function (MyGene.info)**: exportin 1. This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSe…
- **Diseases (Open Targets)**: plasma cell myeloma (0.642); B-cell chronic lymphocytic leukemia (0.626); diffuse large B-cell lymphoma (0.602); HIV infectious disease (0.561); neurodegenerative disease (0.522)
- **Europe PMC papers**: 5357
- **Why important**: XPO1 is a highly connected module node linking ATP1A1, EIF3L, RAB10, QARS1, CCT7, and RO60. It mediates nuclear export of proteins and RNA, and its annotations include ribosomal subunit export and messenger RNA export. XPO1 has a direct high-confidence STRING relationship with CSE1L and recurring hu.MAP support with CSE1L across several complexes (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_09592.1). It has extensive literature and disease associations involving hematologic malignancy, viral disease, and neurodegeneration.
- **Conclusion**: Established evidence supports XPO1 as a nuclear transport component and a major integrator of the module’s transport and biosynthetic branches. Its centrality makes it a strong mechanistic candidate, but the module does not demonstrate altered XPO1 activity.

#### IQGAP1

- **Related proteins** (co-abundance neighbors): TLN1 (0.82), MYL9 (0.82); STRING partners: TLN1 (0.893)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in heart, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IQ motif containing GTPase activating protein 1. This gene encodes a member of the IQGAP family. The protein contains four IQ domains, one calponin homology domain, one Ras-GAP domain and one WW domain. It interacts with components of the cytoskeleton, with cell adhesion molecules, and with several signaling molecules to regulate cell morphology and motility. Expression of the protein is upregulated by gene amplification in two gastric cancer ce…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.515); Costello syndrome (0.503); allergic rhinitis (0.474)
- **Europe PMC papers**: 3787
- **Why important**: IQGAP1 connects TLN1 and MYL9 and is included in the supplementary Rho GTPase signaling result (STRING RCTM Signaling by Rho GTPases; within-query FDR = 0.021). It is a scaffold and signaling regulator associated with cytoskeletal organization, cell adhesion, MAPK signaling, receptor signaling, and cell migration. Its relationship with TLN1 is supported by a high-confidence STRING interaction. IQGAP1 has substantial literature and disease associations involving cancer, developmental syndromes, and hypertrophic cardiomyopathy, while HPA places it at the plasma membrane and cell junctions.
- **Conclusion**: Established evidence supports IQGAP1 as a plausible cytoskeletal and adhesion signaling hub within the module. Its role as a bridge between the module and Rho-related processes is supported but supplementary; a causal role in the shared heart-liver co-abundance pattern remains hypothetical.

#### KARS1

- **Related proteins** (co-abundance neighbors): EIF3L (0.82), FLOT1 (0.80); STRING partners: QARS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, liver
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: lysyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. Lysyl-tRNA synthetase is a homodimer localized to the cytoplasm which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Alternatively spliced transcript variants encoding different…
- **Diseases (Open Targets)**: leukoencephalopathy, progressive, infantile-onset, with or without deafness (0.753); deafness, congenital, and adult-onset progressive leukoencephalopathy (0.714); autosomal recessive nonsyndromic hearing loss 89 (0.685); Charcot-Marie-Tooth disease recessive intermediate B (0.670); deafness (0.534)
- **Europe PMC papers**: 232
- **Why important**: KARS1 is linked to EIF3L and FLOT1 in the module and has a very high-confidence STRING relationship with QARS1. KARS1 encodes lysyl-tRNA synthetase and therefore supports aminoacylation and protein translation. KARS1 and QARS1 repeatedly co-occur in hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), providing independent complex-level support. KARS1 has disease associations involving neurological and hearing disorders and is detected in both heart and liver by HPA.
- **Conclusion**: Established evidence supports KARS1 as part of a translation-related aminoacyl-tRNA synthetase module, with particularly strong support for its relationship to QARS1. Its inclusion may reflect biosynthetic demand or general cellular activity rather than a tissue-specific mechanism.

#### TLN1

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.83), IQGAP1 (0.82); STRING partners: IQGAP1 (0.893)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 connects DYNC1H1 and IQGAP1 and has a high-confidence STRING interaction with IQGAP1. It is an established integrin-associated cytoskeletal protein involved in cell adhesion, integrin activation, cell-cell junction assembly, and actin organization. HPA reports vascular tissue enhancement and group enrichment in megakaryocytes and platelets. Its disease associations include hypertrophic cardiomyopathy and developmental syndromes, and it has substantial literature support.
- **Conclusion**: Established evidence supports TLN1 as an adhesion and cytoskeletal component that may connect cell-matrix organization with intracellular transport. Its vascular and platelet associations make shared non-parenchymal cell contribution plausible, but the fact sheet does not establish whether TLN1 reflects vascular biology or a broader structural program in these samples.

## Module 4

**Tissue pair**: heart and liver  
**Genes (10)**: BLVRA, DHX9, HNRNPK, HNRNPR, LMNB2, MATR3, ATIC, RAN, CCT3, TPD52L2

### Function

The strongest functional interpretation is a conserved nuclear RNA-regulatory module. The only globally corrected enrichment is (GO:BP regulatory ncRNA-mediated gene silencing; q_global = 0.0106), regulatory ncRNA-mediated gene silencing, supported by DHX9, HNRNPK, and RAN. Supplementary STRING evidence (STRING NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex; within-query FDR = 0.0097) links part of the module to mRNA processing and CRD-mediated mRNA stability, while (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0209) places several members in the nuclear lumen. The module therefore most plausibly coordinates RNA processing, RNA stability, ncRNA-mediated regulation, and nuclear RNA or protein trafficking. RAN additionally supports a role in nucleocytoplasmic transport. CCT3, ATIC, BLVRA, LMNB2, and TPD52L2 may represent supporting proteostasis, nuclear-architecture, metabolic, or vesicular components rather than defining the primary function.

**Cell composition.** The HPA profile argues against a plasma-protein, secreted-protein, or blood-cell contamination explanation. None of the module genes is secreted, all have low tissue specificity, and all have low immune-cell specificity. Protein detection in heart and liver is broadly consistent with a shared, ubiquitously expressed cellular program. Several genes show cell-type-enhanced patterns in reproductive, epithelial, neural, or stromal-related cell types, but no single blood-cell pattern dominates. The module may therefore reflect a broadly used nuclear and cytoplasmic housekeeping program that is co-abundant in the relevant cells of both tissues, rather than a heart- or liver-specific pathway.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulatory ncRNA-mediated gene silencing | 0.0106 | DHX9, HNRNPK, RAN |

### STRING and hu.MAP

STRING provides direct high-confidence support for a coherent RNA-associated core. DHX9, HNRNPK, HNRNPR, and MATR3 form a densely interconnected group, with especially strong support for the HNRNPK-HNRNPR relationship and additional links among DHX9, HNRNPK, HNRNPR, and MATR3. The STRING functional results (STRING NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex; within-query FDR = 0.0097), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0209), and (STRING NetworkNeighborAL Mixed, incl. CRD-mediated mRNA stabilization, and Zinc finger, CHHC-type; within-query FDR = 0.0259) are consistent with mRNA processing, mRNA stability, nuclear localization, and related RNA-binding functions. The lymphocyte annotation (STRING TISSUES Lymphocyte; within-query FDR = 0.0191) should be treated cautiously because the HPA profile does not support blood-cell specificity. hu.MAP independently supports known complexes containing HNRNPR, MATR3, and HNRNPK in (hu.MAP huMAP3_10625.1), (hu.MAP huMAP3_07581.1), and (hu.MAP huMAP3_10659.1). These resources show that much of the central module is already connected through established RNA-protein interactions and ribonucleoprotein complexes. The absence of STRING or hu.MAP support for peripheral members does not invalidate their co-abundance relationships.

**STRING interactions (score >= 0.7)**: 6 of 45 gene pairs: DHX9–HNRNPK (0.939); DHX9–HNRNPR (0.909); DHX9–MATR3 (0.786); HNRNPK–HNRNPR (0.962); HNRNPK–MATR3 (0.923); HNRNPR–MATR3 (0.714)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex (FDR = 0.0097, 4 genes); TISSUES Lymphocyte (FDR = 0.0191, 7 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0209, 6 genes); NetworkNeighborAL Mixed, incl. CRD-mediated mRNA stabilization, and Zinc finger, CHHC-type (FDR = 0.0259, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10625.1 (HNRNPR, MATR3, HNRNPK; 3/57); huMAP3_07581.1 (HNRNPR, MATR3; 2/21); huMAP3_10659.1 (HNRNPR, HNRNPK; 2/28)

### Novelty

The module-level observation may be novel as a conserved heart-liver co-abundance pattern, but the central biology is not new in isolation. Its core genes are established RNA-binding, RNA-processing, nuclear-transport, and mRNA-stability factors, and several of their relationships are already represented by STRING and hu.MAP. The result is therefore best described as a potentially new tissue-pair organization or co-abundance configuration of known machinery, rather than discovery of a new molecular complex or new gene function. Novelty would require independent validation across cohorts, assessment of cell composition, and testing whether the heart-liver association persists after controlling for shared cellular states and technical effects.

**Hypothesis.** Hypothesis: in shared cellular populations of heart and liver, a conserved nuclear RNA homeostasis program co-regulates transcript maturation, ncRNA-mediated silencing, mRNA stability, and nucleocytoplasmic transport. DHX9 may help remodel RNA and DNA-RNA structures, HNRNPK and HNRNPR may organize RNA-protein assemblies, MATR3 may stabilize selected nuclear transcripts, and RAN may couple the program to nuclear transport. CCT3 could support folding of participating proteins, while LMNB2 could link the program to nuclear architecture. This is a mechanistic model, not demonstrated causality; the co-abundance data do not show direct regulation, physical binding for every pair, or tissue-specific functional activity.

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): CCT3 (0.89), MATR3 (0.87), RAN (0.85), HNRNPK (0.85), HNRNPR (0.83); STRING partners: HNRNPK (0.939), HNRNPR (0.909), MATR3 (0.786)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is a central network connector and the only member directly supported by the global enrichment together with HNRNPK and RAN in (GO:BP regulatory ncRNA-mediated gene silencing; q_global = 0.0106). It is an RNA helicase with roles in RNA and DNA-RNA unwinding, transcriptional regulation, alternative splicing, and nuclear-cytoplasmic localization. It connects to HNRNPK, HNRNPR, and MATR3 in STRING and appears in all of the relevant supplementary STRING annotations (STRING NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex; within-query FDR = 0.0097), (STRING TISSUES Lymphocyte; within-query FDR = 0.0191), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0209), and (STRING NetworkNeighborAL Mixed, incl. CRD-mediated mRNA stabilization, and Zinc finger, CHHC-type; within-query FDR = 0.0259). Its substantial literature and disease-association profile make it a strong mechanistic anchor.
- **Conclusion**: Established evidence supports DHX9 as a central RNA-remodeling and RNA-processing component of the module. It is plausible that DHX9 helps coordinate the shared heart-liver RNA-regulatory state, but the co-abundance result alone does not establish that DHX9 drives the module.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): DHX9 (0.85), RAN (0.84), MATR3 (0.83); STRING partners: DHX9 (0.939), HNRNPR (0.962), MATR3 (0.923)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, liver
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_10659.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is a highly connected core member with direct STRING links to DHX9, HNRNPR, and MATR3 and membership in hu.MAP complexes (hu.MAP huMAP3_10625.1) and (hu.MAP huMAP3_10659.1). It is a broadly expressed heterogeneous nuclear ribonucleoprotein involved in pre-mRNA processing, RNA processing, transcriptional regulation, and gene-expression control. It contributes to the globally corrected silencing term (GO:BP regulatory ncRNA-mediated gene silencing; q_global = 0.0106) and to every listed supplementary STRING annotation, while also having a substantial literature and clinically relevant disease associations.
- **Conclusion**: Established evidence identifies HNRNPK as a plausible organizing RNA-binding scaffold within the module. Its central position and complex membership support a coordinating role, but whether it is functionally rate-limiting in heart or liver remains a hypothesis.

#### HNRNPR

- **Related proteins** (co-abundance neighbors): DHX9 (0.83), RAN (0.82), CCT3 (0.82), LMNB2 (0.81); STRING partners: DHX9 (0.909), HNRNPK (0.962), MATR3 (0.714)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, liver
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_07581.1, huMAP3_10659.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR is part of the densest established RNA-protein core. It connects with DHX9, HNRNPK, and MATR3 in STRING, and occurs in all three hu.MAP complexes (hu.MAP huMAP3_10625.1), (hu.MAP huMAP3_07581.1), and (hu.MAP huMAP3_10659.1). Its annotated functions in spliceosomal mRNA processing and RNA transport fit the module interpretation, and its STRING annotations (STRING NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex; within-query FDR = 0.0097), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0209), and (STRING NetworkNeighborAL Mixed, incl. CRD-mediated mRNA stabilization, and Zinc finger, CHHC-type; within-query FDR = 0.0259) independently support mRNA processing, nuclear localization, and mRNA-stability biology.
- **Conclusion**: Established evidence supports HNRNPR as a core spliceosome- and RNA-processing component. Its co-abundance with the other ribonucleoprotein factors is consistent with participation in a shared RNA-metabolism program, but does not prove a novel heart-liver-specific complex.

#### MATR3

- **Related proteins** (co-abundance neighbors): DHX9 (0.87), HNRNPK (0.83), CCT3 (0.80); STRING partners: DHX9 (0.786), HNRNPK (0.923), HNRNPR (0.714)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, liver
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_07581.1
- **Function (MyGene.info)**: matrin 3. This gene encodes a nuclear matrix protein, which is proposed to stabilize certain messenger RNA species. Mutations of this gene are associated with distal myopathy 2, which often includes vocal cord and pharyngeal weakness. Alternatively spliced transcript variants, including read-through transcripts composed of the upstream small nucleolar RNA host gene 4 (non-protein coding) and matrin 3 gene s…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.735); distal myopathy with vocal cord weakness (0.569); neurodegenerative disease (0.529); distal myopathy (0.384); hereditary disease (0.193)
- **Europe PMC papers**: 1756
- **Why important**: MATR3 is a central member of the STRING-supported RNA-processing group, connecting with DHX9, HNRNPK, and HNRNPR, and is present in hu.MAP complexes (hu.MAP huMAP3_10625.1) and (hu.MAP huMAP3_07581.1). Its known role as a nuclear matrix protein proposed to stabilize selected messenger RNAs, together with annotations involving post-transcriptional regulation and innate immune response, gives it a plausible bridge between nuclear structure and RNA fate. Its disease associations, including distal myopathy and amyotrophic lateral sclerosis, also make it biologically important for a heart-relevant interpretation.
- **Conclusion**: Established evidence supports MATR3 as a nuclear RNA-stability and structural component of the core. A connection between this module and tissue vulnerability in muscle disease is plausible, but it is not demonstrated by the present network.

#### RAN

- **Related proteins** (co-abundance neighbors): DHX9 (0.85), HNRNPK (0.84), CCT3 (0.84), HNRNPR (0.82), BLVRA (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAN, member RAS oncogene family. RAN (ras-related nuclear protein) is a small GTP binding protein belonging to the RAS superfamily that is essential for the translocation of RNA and proteins through the nuclear pore complex. The RAN protein is also involved in control of DNA synthesis and cell cycle progression. Nuclear localization of RAN requires the presence of regulator of chromosome condensation 1 (RCC1). Mutations in RAN di…
- **Diseases (Open Targets)**: HIV infectious disease (0.565); Orthomyxoviridae infectious disease (0.376); pemphigus foliaceus (0.298); neurodegenerative disease (0.270); Genu valgum (0.136)
- **Europe PMC papers**: 133080
- **Why important**: RAN is a central network connector and one of the genes supporting the global term (GO:BP regulatory ncRNA-mediated gene silencing; q_global = 0.0106). It is a nuclear transport GTPase with established roles in import and export, ribosomal subunit export, DNA metabolism, and cell-cycle processes. Its links to DHX9, HNRNPK, HNRNPR, CCT3, and BLVRA connect the RNA-regulatory core to transport and cellular logistics. Its very extensive literature and broad disease-association record make it an important interpretive anchor, while its lack of tissue specificity supports a general cellular role.
- **Conclusion**: Established evidence supports RAN as the transport-related component that could couple RNA processing and silencing to nuclear trafficking. Its presence strengthens the coherence of the proposed mechanism, but it is also broadly multifunctional and need not be specific to this module.

## Module 5

**Tissue pair**: heart and liver  
**Genes (23)**: DSTN, EIF3C, EZR, FKBP4, MACROH2A1, HNRNPH1, HNRNPL, HSP90AA1, OLA1, PDCD6IP, PSMC2, PSMA1, PSMD13, ADSL, SEC23A, SEPTIN9, RARS1, CCT5, USP5, NAE1, USO1, VPS35, WDR1

### Function

The strongest interpretation is a conserved intracellular proteostasis and organelle-organization module. The globally corrected terms support positive regulation of organelle organization (GO:BP positive regulation of organelle organization; q_global = 0.0111), regulation of organelle organization (GO:BP regulation of organelle organization; q_global = 0.0215), and protein catabolic process (GO:BP protein catabolic process; q_global = 0.0393). The genes span several connected cellular systems: chaperone-assisted folding through CCT5, HSP90AA1, and FKBP4; ubiquitin-related degradation through PSMA1, PSMC2, PSMD13, and USP5; endosomal and secretory trafficking through VPS35, SEC23A, USO1, and PDCD6IP; and actin or cytoskeletal remodeling through DSTN, WDR1, EZR, and SEPTIN9. The module therefore appears to represent coordinated maintenance, sorting, remodeling, and disposal of intracellular proteins and organelles rather than a narrowly tissue-specific pathway. The enrichment does not establish that every process operates as one physical complex, but it does support a shared cellular maintenance program.

**Cell composition.** This is predominantly an intracellular, broadly expressed module rather than a plasma-protein or blood-cell module. HPA assigns low tissue specificity to most genes, low immune-cell specificity to all genes, and identifies only one secreted gene. Protein detection is common in both heart and liver, although several individual genes show tissue-specific detection differences. The single-cell annotations are heterogeneous, including epithelial, glial, muscle, reproductive, and vascular cell types, rather than pointing to a coherent blood population. The module could therefore reflect ubiquitous housekeeping and proteostasis activity shared by cardiomyocytes and hepatocytes, with contributions from multiple cell types. The absence of blood-cell specificity argues against interpreting it primarily as blood contamination, while the broad expression means that shared cellular composition or general cellular stress should remain possible explanations.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP positive regulation of organelle organization | 0.0111 | CCT5, DSTN, HSP90AA1, MACROH2A1, PDCD6IP, SEPTIN9, VPS35, WDR1 |
| GO:BP regulation of organelle organization | 0.0215 | CCT5, DSTN, EZR, FKBP4, HSP90AA1, MACROH2A1, PDCD6IP, SEPTIN9, VPS35, WDR1 |
| GO:BP protein catabolic process | 0.0393 | EZR, HSP90AA1, PDCD6IP, PSMA1, PSMC2, PSMD13, USP5, VPS35 |

### STRING and hu.MAP

STRING provides no supplementary functional-enrichment term, so it does not add a globally corrected pathway claim. Its supported pairwise relationships nevertheless confirm several established substructures: CCT5 connects to HSP90AA1; HSP90AA1 connects strongly with EZR and FKBP4; DSTN connects with WDR1; HNRNPH1 connects with HNRNPL; PSMA1, PSMC2, and PSMD13 form a strongly supported proteasome-related interaction group; and SEC23A connects with USO1 in the secretory pathway. hu.MAP independently supports the proteasome-associated group containing PSMA1, PSMC2, and PSMD13 (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) (hu.MAP huMAP3_05064.1), the USP5–FKBP4-associated complexes (hu.MAP huMAP3_11169.1) (hu.MAP huMAP3_12466.1), the DSTN–WDR1 actin-associated complex (hu.MAP huMAP3_11076.1), the ADSL–OLA1 complex (hu.MAP huMAP3_14442.1), and the SEC23A–USO1 trafficking complex (hu.MAP huMAP3_12394.1). These results indicate that parts of the module recapitulate known molecular assemblies, while the links joining proteasome, chaperone, trafficking, RNA-processing, and cytoskeletal components may represent coordinated abundance rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 11 of 253 gene pairs: ADSL–FKBP4 (0.849); CCT5–HSP90AA1 (0.868); DSTN–WDR1 (0.794); EZR–HSP90AA1 (0.954); FKBP4–HSP90AA1 (0.999); HNRNPH1–HNRNPL (0.982); OLA1–RARS1 (0.747); PSMA1–PSMC2 (0.999); PSMA1–PSMD13 (0.999); PSMC2–PSMD13 (0.999); SEC23A–USO1 (0.704)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09656.1 (PSMA1, PSMC2, PSMD13; 3/64); huMAP3_13725.1 (PSMA1, PSMC2, PSMD13; 3/69); huMAP3_11169.1 (USP5, FKBP4; 2/4); huMAP3_12466.1 (USP5, FKBP4; 2/6); huMAP3_11076.1 (WDR1, DSTN; 2/10); huMAP3_05064.1 (PSMC2, PSMD13; 2/31); huMAP3_14442.1 (ADSL, OLA1; 2/57); huMAP3_12394.1 (USO1, SEC23A; 2/98)

### Novelty

The individual genes and several subassemblies are well established, so this should not be presented as discovery of a new proteasome, chaperone, actin, or vesicle-transport complex. The potentially new result is the conserved co-abundance relationship across heart and liver that places these established systems in one module. That systems-level arrangement is plausible but cannot be called definitively novel from the fact sheet alone. Lack of a STRING edge, hu.MAP membership, or STRING enrichment is not proof of novelty, because co-abundance can reflect shared regulation, cell-state effects, or indirect pathway coupling. Novelty would require replication in independent heart and liver cohorts, testing against cell-composition and technical confounders, and comparison with existing tissue coexpression or proteomics modules.

**Hypothesis.** Hypothesis: the module reflects a shared cellular quality-control circuit in which chaperone and folding capacity, ubiquitin-dependent proteasomal degradation, endosomal or secretory trafficking, and actin remodeling are coordinately regulated to preserve organelle integrity in heart and liver cells. VPS35 and PDCD6IP could connect intracellular sorting and vesicle biology to the broader maintenance program, while CCT5 and HSP90AA1 could support folding of vulnerable client proteins and PSMA1, PSMC2, PSMD13, and USP5 could remove damaged or improperly regulated proteins. DSTN, WDR1, and EZR may provide a cytoskeletal route through which organelle positioning and membrane remodeling are coupled to proteostasis. This is a mechanistic model, not a demonstrated physical pathway; the co-abundance data do not by themselves establish directionality or direct regulation.

### Important genes

#### VPS35

- **Related proteins** (co-abundance neighbors): USO1 (0.84), USP5 (0.84), DSTN (0.83), CCT5 (0.81), PSMA1 (0.80), PSMD13 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in heart, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS35 retromer complex component. This gene belongs to a group of vacuolar protein sorting (VPS) genes. The encoded protein is a component of a large multimeric complex, termed the retromer complex, involved in retrograde transport of proteins from endosomes to the trans-Golgi network. The close structural similarity between the yeast and human proteins that make up this complex suggests a similarity in function. Expression studie…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.743); neurodegenerative disease (0.553); young-onset Parkinson disease (0.503); Parkinson disease (0.482); Parkinson disease, dominant (0.370)
- **Europe PMC papers**: 3611
- **Why important**: VPS35 is a highly connected module member and is the only selected gene present in all globally corrected terms (GO:BP positive regulation of organelle organization; q_global = 0.0111) (GO:BP regulation of organelle organization; q_global = 0.0215) (GO:BP protein catabolic process; q_global = 0.0393). Its established role in the retromer complex and endosome-to-Golgi transport gives the module a concrete organelle-sorting component. It is detected in both heart and liver, has endosomal and lysosomal localization, and has a substantial literature linking it to Parkinson disease and broader neurodegeneration.
- **Conclusion**: Established evidence supports VPS35 as a central trafficking and organelle-organization component of the module. Its co-abundance with proteasome, cytoskeletal, and vesicle-related genes supports functional coupling, but whether VPS35 coordinates proteostasis in heart and liver is a hypothesis requiring perturbation or longitudinal evidence.

#### PSMD13

- **Related proteins** (co-abundance neighbors): RARS1 (0.88), OLA1 (0.88), WDR1 (0.87), CCT5 (0.86), USP5 (0.82), PSMA1 (0.80), VPS35 (0.80); STRING partners: PSMA1 (0.999), PSMC2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1, huMAP3_05064.1
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 is a strongly connected proteasome-associated member and participates in the protein-catabolic term (GO:BP protein catabolic process; q_global = 0.0393). It has direct STRING support with PSMA1 and PSMC2 and occurs with them in multiple hu.MAP proteasome complexes (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) (hu.MAP huMAP3_05064.1). Its established role as a non-ATPase proteasome subunit provides a direct molecular explanation for the degradation signal. It is detected in heart and has disease associations involving malignancy, neurodegeneration, and plasma-cell disorders.
- **Conclusion**: Established evidence identifies PSMD13 as a proteasome component embedded in a known complex, making it a strong anchor for the protein-catabolic interpretation. Its position in the broader module suggests coordinated abundance with folding, trafficking, and cytoskeletal systems, but does not prove that PSMD13 regulates those systems.

#### PSMC2

- **Related proteins** (co-abundance neighbors): RARS1 (0.89), HNRNPL (0.89), CCT5 (0.86), NAE1 (0.84), PDCD6IP (0.83), OLA1 (0.83), PSMA1 (0.82), FKBP4 (0.82), DSTN (0.80); STRING partners: PSMA1 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in heart, liver
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1, huMAP3_05064.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is a highly connected ATPase subunit of the proteasome regulatory particle and is present in the globally corrected protein-catabolic term (GO:BP protein catabolic process; q_global = 0.0393). It has very strong STRING relationships with PSMA1 and PSMD13 and is represented in multiple hu.MAP proteasome complexes (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) (hu.MAP huMAP3_05064.1). It is detected in both heart and liver and has established associations with myeloma, lymphoma, neoplasm, HIV infection, and amyloidosis.
- **Conclusion**: Established evidence supports PSMC2 as a core proteasomal degradation component and a major structural anchor of the module. Its connections to CCT5, RARS1, and other non-proteasome genes are consistent with coordinated proteostasis, but the module does not establish a novel PSMC2 interaction mechanism.

#### CCT5

- **Related proteins** (co-abundance neighbors): PSMD13 (0.86), PSMC2 (0.86), RARS1 (0.84), OLA1 (0.84), EIF3C (0.83), WDR1 (0.83), HNRNPL (0.83), ADSL (0.83), HSP90AA1 (0.82), VPS35 (0.81), MACROH2A1 (0.80); STRING partners: HSP90AA1 (0.868)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 has the strongest network position in the module and contributes to both organelle-organization terms (GO:BP positive regulation of organelle organization; q_global = 0.0111) (GO:BP regulation of organelle organization; q_global = 0.0215). Its established function in the CCT chaperonin complex, including folding of actin and tubulin, links protein quality control to cytoskeletal organization. It connects within the module to proteasome-associated genes, RARS1, OLA1, WDR1, and RNA-related genes, and has a strong STRING relationship with HSP90AA1. It has a substantial literature and disease associations including hereditary neuropathy and neurodegenerative disease.
- **Conclusion**: Established evidence supports CCT5 as a chaperone and a plausible bridge between folding and cytoskeletal maintenance. Its central co-abundance position makes it an important module marker, but the fact that HPA does not detect it by IHC in heart or liver cautions against treating its module prominence as proof of abundant protein in every sampled cell.

#### HSP90AA1

- **Related proteins** (co-abundance neighbors): USO1 (0.84), EIF3C (0.83), CCT5 (0.82); STRING partners: CCT5 (0.868), EZR (0.954), FKBP4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein 90 alpha family class A member 1. The protein encoded by this gene is an inducible molecular chaperone that functions as a homodimer. The encoded protein aids in the proper folding of specific target proteins by use of an ATPase activity that is modulated by co-chaperones. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: cancer (0.643); plasma cell myeloma (0.404); non-small cell lung carcinoma (0.394); dengue disease (0.375); Orthomyxoviridae infectious disease (0.375)
- **Europe PMC papers**: 8215
- **Why important**: HSP90AA1 contributes to all globally corrected terms (GO:BP positive regulation of organelle organization; q_global = 0.0111) (GO:BP regulation of organelle organization; q_global = 0.0215) (GO:BP protein catabolic process; q_global = 0.0393) and has extensive literature. It is an inducible molecular chaperone with established roles in protein folding, stress responses, and client-protein stabilization. STRING supports relationships with CCT5, EZR, FKBP4, and USO1, linking chaperone activity to membrane-cytoskeletal and secretory-trafficking features of the module. It also has broad disease associations, particularly cancer and infection.
- **Conclusion**: Established evidence supports HSP90AA1 as a major proteostasis and stress-response component. Its network relationships make it a plausible integrator of folding, trafficking, and membrane-associated processes, but the module alone cannot determine whether stress signaling caused the shared abundance pattern.
