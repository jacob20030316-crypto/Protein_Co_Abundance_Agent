# Conserved co-abundance modules: heart and skin

## Module 0

**Tissue pair**: heart and skin  
**Genes (6)**: GOT2, ATP5F1A, IMMT, NDUFA10, NDUFS1, UQCRC2

### Function

The module is most consistent with mitochondrial energy metabolism, especially respiratory-chain electron transport, oxidative phosphorylation, proton-motive-force generation, and ATP synthesis. NDUFA10 and NDUFS1 represent complex I functions, UQCRC2 represents complex III, ATP5F1A represents the catalytic F1 component of ATP synthase, and IMMT supports inner-membrane architecture and cristae formation. GOT2 adds a mitochondrial amino-acid and tricarboxylic-acid-cycle connection. The module therefore links respiratory-chain electron flow with mitochondrial structure, intermediary metabolism, and ATP production. No GO/KEGG term passed global correction, so the functional interpretation is based on the individual gene annotations, network structure, and supplementary STRING results rather than a globally significant GO/KEGG enrichment. The STRING results support inner mitochondrial membrane organization (STRING Component Inner mitochondrial membrane protein complex; within-query FDR = 0.0116) (STRING COMPARTMENTS Inner mitochondrial membrane protein complex; within-query FDR = 0.0126), oxidative phosphorylation (STRING KEGG Oxidative phosphorylation; within-query FDR = 0.0418), and thermogenesis (STRING KEGG Thermogenesis; within-query FDR = 0.0418), but these are supplementary evidence.

**Cell composition.** The genes are intracellular mitochondrial proteins rather than plasma or secreted proteins; the HPA summary reports no secreted genes. All module proteins were detected in both heart and skin, supporting the biological presence of the module in both tissues. HPA reports low immune-cell specificity for every gene and no enriched blood-cell category, so the module is not suggestive of blood-cell contamination or a plasma-protein signal. Several genes show tissue enhancement in tongue, while some are enhanced in heart muscle or skeletal muscle, and GOT2 has group enrichment spanning metabolically active tissues. This pattern is more compatible with mitochondrial energy requirements and shared oxidative cell biology than with a secreted or blood-derived module. Cell-type enhancement is present for many genes, so contribution from shared or metabolically active cell populations remains possible.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING shows a dense set of known, high-confidence relationships among ATP5F1A, IMMT, NDUFA10, NDUFS1, and UQCRC2. The supplementary STRING annotations place most of these genes in the inner mitochondrial membrane and respiratory-chain machinery (STRING Component Inner mitochondrial membrane protein complex; within-query FDR = 0.0116) (STRING COMPARTMENTS Inner mitochondrial membrane protein complex; within-query FDR = 0.0126) (STRING KEGG Oxidative phosphorylation; within-query FDR = 0.0418) (STRING KEGG Thermogenesis; within-query FDR = 0.0418). hu.MAP independently recovers the ATP5F1A-UQCRC2 pair in one complex (hu.MAP huMAP3_07245.1) and the NDUFA10-NDUFS1 pair across several respiratory-complex assemblies (hu.MAP huMAP3_07653.1) (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1). These results indicate that much of the module reflects established physical or functional organization rather than an unexplained association. GOT2 has no listed STRING partner or hu.MAP complex in the fact sheet, although it is connected in the co-abundance network to UQCRC2 and ATP5F1A; this may represent metabolic coupling that is less well represented in those interaction resources.

**STRING interactions (score >= 0.7)**: 9 of 15 gene pairs: ATP5F1A–IMMT (0.809); ATP5F1A–NDUFA10 (0.759); ATP5F1A–NDUFS1 (0.961); ATP5F1A–UQCRC2 (0.986); IMMT–NDUFS1 (0.901); IMMT–UQCRC2 (0.811); NDUFA10–NDUFS1 (0.999); NDUFA10–UQCRC2 (0.986); NDUFS1–UQCRC2 (0.998)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Inner mitochondrial membrane protein complex (FDR = 0.0116, 5 genes); COMPARTMENTS Inner mitochondrial membrane protein complex (FDR = 0.0126, 5 genes); KEGG Oxidative phosphorylation (FDR = 0.0418, 4 genes); KEGG Thermogenesis (FDR = 0.0418, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07245.1 (UQCRC2, ATP5F1A; 2/4); huMAP3_07653.1 (NDUFA10, NDUFS1; 2/7); huMAP3_02819.1 (NDUFA10, NDUFS1; 2/34); huMAP3_14018.1 (NDUFA10, NDUFS1; 2/48); huMAP3_06397.1 (NDUFA10, NDUFS1; 2/49); huMAP3_09982.1 (NDUFA10, NDUFS1; 2/49); huMAP3_09567.1 (NDUFA10, NDUFS1; 2/52); huMAP3_14878.1 (NDUFA10, NDUFS1; 2/53)

### Novelty

The module should not be described as a newly discovered mitochondrial pathway or as a newly established protein complex. Its principal relationships and annotations are already supported by STRING, hu.MAP, and curated gene information. A potentially novel aspect is the conserved heart-skin co-abundance configuration, particularly the joint behavior of respiratory-chain, cristae, ATP-synthase, and amino-acid-metabolism genes across these tissues. However, the fact sheet does not provide an external replication cohort, temporal validation, perturbation experiment, or direct biochemical validation, so the module-level novelty remains provisional. Absence of a gene or edge from a particular database would not establish novelty.

**Hypothesis.** Hypothesis: this conserved heart-skin module reflects coordinated regulation of mitochondrial respiratory capacity. Variation in inner-membrane organization through IMMT may be coupled to complex I and complex III electron transfer through NDUFA10, NDUFS1, and UQCRC2, while ATP5F1A converts the resulting proton gradient into ATP. GOT2 may connect this respiratory state to amino-acid and tricarboxylic-acid-cycle flux. In heart and skin, shared metabolic demand or shared regulation of oxidative cell states could therefore produce the observed co-abundance pattern. This is a mechanistic hypothesis, not a demonstrated causal model.

### Important genes

#### NDUFS1

- **Related proteins** (co-abundance neighbors): IMMT (0.82); STRING partners: ATP5F1A (0.961), IMMT (0.901), NDUFA10 (0.999), UQCRC2 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, skin
- **hu.MAP 3.0**: huMAP3_07653.1, huMAP3_02819.1, huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S1. The protein encoded by this gene belongs to the complex I 75 kDa subunit family. Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Thi…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 5 (0.810); mitochondrial complex I deficiency (0.647); type 2 diabetes mellitus (0.608); Parkinson disease (0.603); diabetes mellitus (0.580)
- **Europe PMC papers**: 2567
- **Why important**: NDUFS1 is a central respiratory-chain gene in the module: it has strong STRING relationships with ATP5F1A, IMMT, NDUFA10, and UQCRC2 and recurs in many hu.MAP respiratory-complex assemblies (hu.MAP huMAP3_07653.1) (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1). Its annotation identifies it as the largest complex I subunit and an iron-sulfur-fragment component that transfers electrons toward ubiquinone. It is detected in both heart and skin, is enhanced in heart muscle and skeletal muscle, and has substantial literature and disease association with complex I deficiency, Parkinson disease, and diabetes.
- **Conclusion**: Established evidence supports NDUFS1 as a core complex I component and a major functional anchor of the module. It is a plausible marker of coordinated respiratory-chain abundance. Whether it drives the heart-skin module, rather than simply tracking mitochondrial content, remains a hypothesis.

#### UQCRC2

- **Related proteins** (co-abundance neighbors): GOT2 (0.84), IMMT (0.82); STRING partners: ATP5F1A (0.986), IMMT (0.811), NDUFA10 (0.986), NDUFS1 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, skin
- **hu.MAP 3.0**: huMAP3_07245.1
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase core protein 2. The protein encoded by this gene is located in the mitochondrion, where it is part of the ubiquinol-cytochrome c reductase complex (also known as complex III). This complex constitutes a part of the mitochondrial respiratory chain. Defects in this gene are a cause of mitochondrial complex III deficiency nuclear type 5. [provided by RefSeq, Jul 2015].
- **Diseases (Open Targets)**: mitochondrial complex III deficiency (0.732); neurodegenerative disease (0.423); mitochondrial disease (0.312); gastric cancer (0.085); adrenoleukodystrophy (0.075)
- **Europe PMC papers**: 3297
- **Why important**: UQCRC2 links the module to complex III and is strongly connected in STRING to ATP5F1A, IMMT, NDUFA10, and NDUFS1. It is present with ATP5F1A in a hu.MAP complex (hu.MAP huMAP3_07245.1) and is annotated for ubiquinol-to-cytochrome-c electron transfer, oxidative phosphorylation, aerobic respiration, and mitochondrial respiratory function. It is detected in both tissues and has substantial literature and disease associations involving mitochondrial complex III deficiency.
- **Conclusion**: Established evidence supports UQCRC2 as the complex III bridge within a broader respiratory-chain module. Its position makes it important for interpreting the module as coordinated electron transport rather than an isolated complex I signature. A direct role in coordinating the cross-complex co-abundance pattern is not established.

#### ATP5F1A

- **Related proteins** (co-abundance neighbors): GOT2 (0.80); STRING partners: IMMT (0.809), NDUFA10 (0.759), NDUFS1 (0.961), UQCRC2 (0.986)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, skin
- **hu.MAP 3.0**: huMAP3_07245.1
- **Function (MyGene.info)**: ATP synthase F1 subunit alpha. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, using an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic po…
- **Diseases (Open Targets)**: mitochondrial complex V (ATP synthase) deficiency, nuclear type 4A (0.655); mitochondrial proton-transporting ATP synthase complex deficiency (0.648); mitochondrial complex V (ATP synthase) deficiency, nuclear type 4B (0.532); hereditary disease (0.394); Mitochondrial encephalopathy (0.371)
- **Europe PMC papers**: 822
- **Why important**: ATP5F1A represents the catalytic alpha subunit of mitochondrial ATP synthase and connects ATP production to the respiratory-chain genes. It has STRING relationships with every other major mitochondrial member listed in the fact sheet and occurs with UQCRC2 in hu.MAP (hu.MAP huMAP3_07245.1). Its annotations include ATP biosynthesis, proton-motive-force-driven ATP synthesis, lipid metabolism, and response to muscle activity. It is detected in heart and skin and has disease associations involving mitochondrial complex V deficiency.
- **Conclusion**: Established evidence supports ATP5F1A as the module's ATP-output component and a strong functional link between respiratory electron transport and energy production. Its network role supports a coordinated oxidative-phosphorylation interpretation, but does not prove that ATP synthase activity is altered in these tissues.

#### IMMT

- **Related proteins** (co-abundance neighbors): NDUFA10 (0.83), UQCRC2 (0.82), NDUFS1 (0.82); STRING partners: ATP5F1A (0.809), NDUFS1 (0.901), UQCRC2 (0.811)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inner membrane mitochondrial protein. Enables RNA binding activity. Involved in cristae formation. Located in mitochondrial inner membrane. Part of MICOS complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); multinodular goiter (0.196); alcohol drinking (0.190); breast cancer (0.094); neoplasm (0.087)
- **Europe PMC papers**: 933
- **Why important**: IMMT is the module's structural mitochondrial gene. It is annotated as a cristae-forming inner-membrane protein and MICOS-complex component, and it connects in STRING to NDUFS1, UQCRC2, and ATP5F1A. It is detected in both heart and skin and has substantial literature, including associations with neurodegenerative disease. Its inclusion provides structural context for the respiratory-chain and ATP-synthesis genes.
- **Conclusion**: Established evidence supports IMMT as an inner-membrane and cristae-organization component that can physically contextualize respiratory machinery. The hypothesis that cristae organization modulates the observed heart-skin co-abundance pattern is biologically plausible but not demonstrated by the fact sheet.

#### GOT2

- **Related proteins** (co-abundance neighbors): UQCRC2 (0.84), ATP5F1A (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in heart, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamic-oxaloacetic transaminase 2. Glutamic-oxaloacetic transaminase is a pyridoxal phosphate-dependent enzyme which exists in cytoplasmic and inner-membrane mitochondrial forms, GOT1 and GOT2, respectively. GOT plays a role in amino acid metabolism and the urea and tricarboxylic acid cycles. The two enzymes are homodimeric and show close homology. Two transcript variants encoding different isoforms have been found for this gene. […
- **Diseases (Open Targets)**: genetic developmental and epileptic encephalopathy (0.618); developmental and epileptic encephalopathy (0.393); Encephalopathy (0.370); neurodegenerative disease (0.356); lagophthalmos (0.298)
- **Europe PMC papers**: 2463
- **Why important**: GOT2 provides the clearest metabolic interface outside the canonical respiratory-chain proteins. It is a mitochondrial aminotransferase involved in amino-acid, aspartate, glutamate, and tricarboxylic-acid-cycle metabolism. In the co-abundance network it connects to UQCRC2 and ATP5F1A, despite having no listed STRING partners or hu.MAP complex. It is detected in both heart and skin and shows enrichment across several metabolically active tissues and cell types. Its literature and disease associations include developmental and epileptic encephalopathy and neurodegenerative disease.
- **Conclusion**: Established evidence supports GOT2 as a mitochondrial metabolic enzyme connected by co-abundance to respiratory and ATP-synthesis components. Its network placement suggests metabolic coupling, but the specific biochemical mechanism linking GOT2 to this module is a hypothesis rather than an established interaction.

## Module 1

**Tissue pair**: heart and skin  
**Genes (6)**: ACADVL, ACSS1, AIFM1, ETFA, NDUFS2, SUCLG2

### Function

The module is most consistent with a mitochondrial energy-metabolism program, integrating fatty-acid oxidation, electron transfer, the tricarboxylic-acid cycle, and respiratory-chain activity. ACADVL and ETFA support mitochondrial fatty-acid beta-oxidation and transfer of reducing equivalents; ACSS1 supports acetate-to-acetyl-CoA metabolism; SUCLG2 supports succinyl-CoA and tricarboxylic-acid-cycle metabolism; and NDUFS2 supports respiratory-complex-I electron transport. AIFM1 adds a mitochondrial respiratory and apoptosis-related component. This interpretation is based on the coherent annotations of the member genes and the observed network links, not on enrichment significance. No GO or KEGG term passed global correction, so there is no globally significant enrichment result to report. The absence of an enriched term does not invalidate the module.

**Cell composition.** The module does not resemble a plasma-protein, secreted-protein, or blood-cell module: HPA reports no secreted genes, uniformly low immune-cell specificity, and mitochondrial localization for the genes with localization annotations. Protein detection is broadly compatible with the two tissues, with all members detected in heart and nearly all detected in skin. The HPA pattern instead suggests a mixture of metabolically active cell contexts, including hepatocytes, muscle-related cells, cardiomyocytes, and epithelial or trophoblast-related cell types. The shared heart–skin signal could therefore reflect a conserved mitochondrial metabolic program, shared oxidative demands, or differences in cellular composition rather than a tissue-specific pathway unique to heart or skin.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known STRING relationships are ACADVL with ETFA, ACSS1 with SUCLG2, and NDUFS2 with SUCLG2. These links support biological coherence across fatty-acid oxidation, succinyl-CoA metabolism, and respiratory metabolism. The remaining module relationships are not represented by high-confidence STRING links in the supplied results, so the co-abundance edges should not be interpreted as established physical interactions. No hu.MAP complex contains multiple module members in the supplied analysis. Overall, STRING provides partial support for a connected mitochondrial metabolic theme, while the co-abundance network may also capture shared regulation, tissue composition, or coordinated mitochondrial abundance.

**STRING interactions (score >= 0.7)**: 3 of 15 gene pairs: ACADVL–ETFA (0.877); ACSS1–SUCLG2 (0.844); NDUFS2–SUCLG2 (0.8)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The individual gene functions and several pairwise relationships are established, so the biological components are not new in isolation. The module-level observation may be a potentially novel cross-tissue co-abundance pattern because the supplied STRING results provide only partial pairwise support and hu.MAP provides no multi-member complex support. However, this cannot establish that the module is a new biological discovery: absence from STRING or hu.MAP is not evidence of novelty, and co-abundance can arise from shared cell types or mitochondrial content. The appropriate conclusion is that the cross-tissue module is a candidate novel systems-level association requiring replication in independent cohorts and testing against cell-composition and mitochondrial-content covariates.

**Hypothesis.** Hypothesis: in both heart and skin, a conserved population of metabolically active cells co-regulates mitochondrial fuel use and oxidative phosphorylation. ACSS1 may supply acetyl-CoA from acetate, SUCLG2 may support succinyl-CoA-cycle flux, ACADVL and ETFA may channel long-chain fatty-acid electrons into the respiratory system, and NDUFS2 may support complex-I electron transfer. AIFM1 may couple this mitochondrial state to stress or apoptosis responses. This is a mechanistic hypothesis rather than a demonstrated pathway assembled by the co-abundance data; it should be tested with independent expression data, protein measurements, mitochondrial functional assays, and cell-type-resolved analyses.

Web sources: https://medlineplus.gov/genetics/gene/acadvl/; https://www.genecards.org/card/ACADVL; https://www.genecards.org/card/NDUFS2; https://en.wikipedia.org/wiki/NDUFS2

### Important genes

#### ACSS1

- **Related proteins** (co-abundance neighbors): SUCLG2 (0.82), ACADVL (0.81), NDUFS2 (0.81), AIFM1 (0.81); STRING partners: SUCLG2 (0.844)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in heart, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase short chain family member 1. This gene encodes a mitochondrial acetyl-CoA synthetase enzyme. A similar protein in mice plays an important role in the tricarboxylic acid cycle by catalyzing the conversion of acetate to acetyl CoA. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Nov 2011].
- **Diseases (Open Targets)**: response to antihypertensive drug (0.284); neurodegenerative disease (0.220); acute myeloid leukemia (0.061); neoplasm (0.048); hepatocellular carcinoma (0.039)
- **Europe PMC papers**: 1022
- **Why important**: ACSS1 is the highest-connectivity hub in the module and links several of its metabolic components. Its established function as a mitochondrial acetyl-CoA synthetase provides a plausible entry point connecting acetate metabolism with oxidative metabolism. HPA supports expression in heart and skin and shows tissue or cell-type enhancement in several metabolically specialized contexts. Its literature volume is substantial, and its disease or phenotype associations include neurodegenerative disease and hepatocellular carcinoma, although these associations do not establish a role in this module.
- **Conclusion**: Established evidence supports ACSS1 as a central mitochondrial acetyl-CoA metabolic enzyme and as the network hub of this module. Hypothesis: ACSS1 may coordinate carbon entry into mitochondrial metabolism and help explain the cross-tissue co-abundance pattern.

#### ACADVL

- **Related proteins** (co-abundance neighbors): ACSS1 (0.81); STRING partners: ETFA (0.877)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA dehydrogenase very long chain. The protein encoded by this gene is targeted to the inner mitochondrial membrane where it catalyzes the first step of the mitochondrial fatty acid beta-oxidation pathway. This acyl-Coenzyme A dehydrogenase is specific to long-chain and very-long-chain fatty acids. A deficiency in this gene product reduces myocardial fatty acid beta-oxidation and is associated with cardiomyopathy. Alternative splic…
- **Diseases (Open Targets)**: very long chain acyl-CoA dehydrogenase deficiency (0.865); hereditary disease (0.531); long chain acyl-CoA dehydrogenase deficiency (0.506); rhabdomyolysis (0.464); Acute rhabdomyolysis (0.436)
- **Europe PMC papers**: 3504
- **Why important**: ACADVL is a key fatty-acid oxidation enzyme and is linked in STRING to ETFA, providing direct support for a functional fatty-acid oxidation branch. Its network connection to ACSS1 places lipid oxidation near the module hub. It is detected in both heart and skin, is enhanced in cardiomyocytes and several epithelial or trophoblast-related cell types, and has a strong established disease association with very-long-chain acyl-CoA dehydrogenase deficiency and cardiomyopathy-related phenotypes. It also has the largest literature volume among the module genes.
- **Conclusion**: Established evidence identifies ACADVL as a core long-chain fatty-acid oxidation enzyme with clinically important mitochondrial disease relevance. Hypothesis: its co-abundance with ACSS1 and ETFA reflects coordinated regulation of lipid-derived energy production in shared metabolically active cells.

#### ETFA

- **Related proteins** (co-abundance neighbors): AIFM1 (0.80); STRING partners: ACADVL (0.877)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein subunit alpha. ETFA participates in catalyzing the initial step of the mitochondrial fatty acid beta-oxidation. It shuttles electrons between primary flavoprotein dehydrogenases and the membrane-bound electron transfer flavoprotein ubiquinone oxidoreductase. Defects in electron-transfer-flavoprotein have been implicated in type II glutaricaciduria in which multiple acyl-CoA dehydrogenase deficiencies result in l…
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.834); glutaric aciduria (0.756); hereditary disease (0.469); multiple acyl-CoA dehydrogenase deficiency, mild type (0.370); multiple acyl-CoA dehydrogenase deficiency, severe neonatal type (0.370)
- **Europe PMC papers**: 1433
- **Why important**: ETFA transfers electrons from several mitochondrial dehydrogenases toward the respiratory system and is directly connected to ACADVL in STRING. Its annotations therefore bridge fatty-acid oxidation with respiratory electron transport. It is detected in both tissues and shows enrichment in liver and tongue at the tissue level and in hepatocytes and platelets at the single-cell level, while retaining low immune-cell specificity. Its established association with multiple acyl-CoA dehydrogenase deficiency gives the module a clinically relevant electron-transfer component.
- **Conclusion**: Established evidence supports ETFA as an electron-transfer connector between mitochondrial substrate oxidation and respiration. Hypothesis: ETFA may be a key functional bridge explaining why fatty-acid oxidation genes and respiratory genes co-vary in this module.

#### SUCLG2

- **Related proteins** (co-abundance neighbors): ACSS1 (0.82); STRING partners: ACSS1 (0.844), NDUFS2 (0.8)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase GDP-forming subunit beta. This gene encodes a GTP-specific beta subunit of succinyl-CoA synthetase. Succinyl-CoA synthetase catalyzes the reversible reaction involving the formation of succinyl-CoA and succinate. Alternate splicing results in multiple transcript variants. Pseudogenes of this gene are found on chromosomes 5 and 12. [provided by RefSeq, Apr 2010].
- **Diseases (Open Targets)**: smoking initiation (0.377); breast disorder (0.325); vitamin B deficiency (0.318); alcohol drinking (0.314); duodenal ulcer (0.270)
- **Europe PMC papers**: 1184
- **Why important**: SUCLG2 contributes the tricarboxylic-acid-cycle and succinyl-CoA branch of the module and is linked in STRING to both ACSS1 and NDUFS2. This makes it a structural bridge between acetyl-CoA-related metabolism and respiratory-chain activity, despite having fewer co-abundance connections than ACSS1. HPA shows liver enhancement, hepatocyte and parietal-cell enhancement, mitochondrial localization, and detection in both heart and skin. Its established biochemical role is supported by disease and phenotype associations, although those associations are not specific to this module.
- **Conclusion**: Established evidence supports SUCLG2 as a mitochondrial succinyl-CoA synthetase component linking intermediary metabolism to the respiratory state. Hypothesis: SUCLG2 may help couple carbon-cycle flux to respiratory demand in the shared cell populations.

#### NDUFS2

- **Related proteins** (co-abundance neighbors): ACSS1 (0.81); STRING partners: SUCLG2 (0.8)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S2. The protein encoded by this gene is a core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (complex I). Mammalian mitochondrial complex I is composed of at least 43 different subunits, 7 of which are encoded by the mitochondrial genome, and the rest are the products of nuclear genes. The iron-sulfur protein fraction of complex I is made up of 7 subunits, including this g…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.758); mitochondrial complex I deficiency, nuclear type 6 (0.665); type 2 diabetes mellitus (0.608); mitochondrial disease (0.596); Parkinson disease (0.588)
- **Europe PMC papers**: 1723
- **Why important**: NDUFS2 is a core subunit of mitochondrial respiratory complex I and provides the clearest respiratory-chain anchor in the module. Its STRING relationship with SUCLG2 connects electron transport to tricarboxylic-acid-cycle metabolism. HPA shows enhancement in skeletal muscle and tongue, low cell-type specificity, mitochondrial localization, and detection in both heart and skin. Its established associations with complex-I deficiency, mitochondrial disease, and Parkinson disease underscore the physiological importance of the process represented by the module.
- **Conclusion**: Established evidence supports NDUFS2 as a core complex-I component required for mitochondrial electron transport. Hypothesis: NDUFS2 co-abundance may report shared respiratory capacity rather than a direct physical interaction with the other module members.

## Module 2

**Tissue pair**: heart and skin  
**Genes (8)**: AIMP2, DHX9, H4C1, HNRNPL, HNRNPR, MATR3, NES, RPL12

### Function

The most coherent interpretation is a nuclear RNA-processing and post-transcriptional regulation module. HNRNPR, HNRNPL, DHX9, and MATR3 form the functional core: they are nucleoplasmic RNA-associated proteins, and their annotations support pre-mRNA processing, alternative splicing, RNA stabilization, RNA helicase activity, and post-transcriptional regulation. The strongest direct network support is the dense set of STRING relationships among these four proteins, together with the supplementary STRING enrichments for mRNA processing, the CRD-mediated mRNA stability complex, RNA-recognition motifs, and mRNA stabilization (STRING NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex; within-query FDR = 0.0035) (STRING SMART RNA recognition motif; within-query FDR = 0.0088) (STRING NetworkNeighborAL Mixed, incl. CRD-mediated mRNA stabilization, and Zinc finger, CHHC-type; within-query FDR = 0.0127) (STRING WikiPathways mRNA processing; within-query FDR = 0.0442). RPL12 may reflect translation-related coupling, AIMP2 may connect the module to protein-translation complex assembly, NES may mark a structural or progenitor-associated context, and H4C1 may reflect chromatin organization. No GO or KEGG term passed global correction; therefore the RNA-processing interpretation is supported by gene functions, network structure, and supplementary STRING evidence rather than by globally significant GO or KEGG enrichment.

**Cell composition.** This is not a plasma or secreted-protein module: none of the genes is annotated as secreted. The module is also not predominantly blood-cell specific, because most genes have low immune-cell specificity and the proteins are detected in heart and, for nearly all genes, skin. At the same time, most genes show cell-type enhancement, and the enhanced cell types are diverse, including epithelial, stromal, glial, renal, progenitor, and muscle-associated contexts. Five genes have low tissue specificity, while the tissue-enhanced signals include heart muscle and skeletal muscle, with additional signals in lymphoid tissue. H4C1 has group enrichment in eosinophils and neutrophils and enhancement in erythrocyte progenitors, so a contribution from nucleated blood or progenitor cells cannot be excluded. Overall, the module is more consistent with broadly expressed nuclear and translational machinery, modulated by shared cellular composition, than with a blood-derived or secreted plasma signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a compact, internally coherent interaction core. DHX9 connects to HNRNPL, HNRNPR, and MATR3, while HNRNPL, HNRNPR, and MATR3 are mutually connected within the observed subset. The highest-confidence relationships therefore concentrate on the four RNA-processing genes rather than on the peripheral genes. The supplementary STRING terms (STRING NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex; within-query FDR = 0.0035) through (STRING WikiPathways mRNA processing; within-query FDR = 0.0442) independently point toward mRNA processing and RNA stabilization, but they are supplementary within-query results and are not global module significance. hu.MAP provides prior complex-level support: HNRNPR, HNRNPL, and MATR3 recur together in (hu.MAP huMAP3_07581.1) and (hu.MAP huMAP3_10625.1), HNRNPL and MATR3 recur in (hu.MAP huMAP3_05721.1), and HNRNPR with HNRNPL recur in (hu.MAP huMAP3_07225.1) through (hu.MAP huMAP3_10659.1). These complexes contain many additional heterogeneous nuclear ribonucleoproteins and RNA-binding factors. Thus, the module appears to recover a known RNA-processing neighborhood, while its co-abundance grouping also includes genes that are not established members of those complexes.

**STRING interactions (score >= 0.7)**: 6 of 28 gene pairs: DHX9–HNRNPL (0.901); DHX9–HNRNPR (0.909); DHX9–MATR3 (0.786); HNRNPL–HNRNPR (0.961); HNRNPL–MATR3 (0.757); HNRNPR–MATR3 (0.714)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex (FDR = 0.0035, 4 genes); SMART RNA recognition motif (FDR = 0.0088, 3 genes); NetworkNeighborAL Mixed, incl. CRD-mediated mRNA stabilization, and Zinc finger, CHHC-type (FDR = 0.0127, 3 genes); WikiPathways mRNA processing (FDR = 0.0442, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07581.1 (HNRNPR, HNRNPL, MATR3; 3/21); huMAP3_10625.1 (HNRNPR, HNRNPL, MATR3; 3/57); huMAP3_05721.1 (HNRNPL, MATR3; 2/6); huMAP3_07225.1 (HNRNPR, HNRNPL; 2/7); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09654.1 (HNRNPR, HNRNPL; 2/13); huMAP3_10659.1 (HNRNPR, HNRNPL; 2/28)

### Novelty

The protein relationships themselves are not a wholly new discovery: the central interactions are already represented in STRING, and the HNRNPR–HNRNPL–MATR3 combinations recur in hu.MAP complexes. The fact sheet therefore does not support claiming a novel molecular complex or a newly discovered physical interaction. A potentially novel aspect is the co-abundance of this RNA-processing core with NES, AIMP2, RPL12, and H4C1 across heart and skin, but novelty of that tissue-pair association cannot be established from the supplied evidence alone. In particular, absence of a peripheral gene from STRING or hu.MAP would not prove novelty. The defensible conclusion is that this is a plausible context-specific conserved co-abundance module built around established RNA-processing machinery, with unproven novelty at the tissue-network level.

**Hypothesis.** Mechanistic hypothesis: in shared heart and skin cell populations, a nucleoplasmic RNA-processing assembly centered on HNRNPR, HNRNPL, DHX9, and MATR3 coordinates splicing, RNA remodeling, and stabilization of transcripts needed for cell maintenance and tissue-specific differentiation. RPL12 and AIMP2 may couple this post-transcriptional program to translation, while NES may reflect a structural or progenitor-associated state and H4C1 may reflect chromatin or cell-composition input. This is a hypothesis rather than an established pathway: the co-abundance data and interaction resources support molecular coherence, but they do not demonstrate physical assembly in heart or skin, causal regulation, or the direction of regulation.

### Important genes

#### HNRNPR

- **Related proteins** (co-abundance neighbors): DHX9 (0.84), NES (0.82), HNRNPL (0.82), AIMP2 (0.82), H4C1; H4C2; H4C3; H4C4; H4C5; H4C6; H4C8; H4C9; H4C11; H4C12; H4C13; H4C14; H4C15; H4C16 (0.81); STRING partners: DHX9 (0.909), HNRNPL (0.961), MATR3 (0.714)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, skin
- **hu.MAP 3.0**: huMAP3_07581.1, huMAP3_10625.1, huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_10659.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR is the most connected hub in the module and participates in every listed hu.MAP complex containing the module core (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1). It has direct STRING relationships with DHX9, HNRNPL, and MATR3 and is annotated as a spliceosome-associated RNA-binding protein involved in mRNA processing and transport. Its disease associations include neurodevelopmental and intellectual-disability phenotypes, and the literature record is substantial, supporting it as a biologically credible anchor rather than a peripheral correlate.
- **Conclusion**: Established evidence supports HNRNPR as a central RNA-processing hub and a strong candidate for organizing the module's core. It is plausible, but not proven, that HNRNPR helps coordinate the conserved heart–skin co-abundance pattern.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): RPL12 (0.83), DHX9 (0.82), HNRNPR (0.82); STRING partners: DHX9 (0.901), HNRNPR (0.961), MATR3 (0.757)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, skin
- **hu.MAP 3.0**: huMAP3_07581.1, huMAP3_10625.1, huMAP3_05721.1, huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_10659.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is a central connector with relationships to DHX9, HNRNPR, MATR3, and RPL12. It appears in all of the listed hu.MAP complexes associated with the module core (hu.MAP huMAP3_07581.1) through (hu.MAP huMAP3_10659.1), and it is represented in every supplementary STRING enrichment (STRING NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex; within-query FDR = 0.0035) (STRING SMART RNA recognition motif; within-query FDR = 0.0088) (STRING NetworkNeighborAL Mixed, incl. CRD-mediated mRNA stabilization, and Zinc finger, CHHC-type; within-query FDR = 0.0127) (STRING WikiPathways mRNA processing; within-query FDR = 0.0442). Its annotation supports RNA processing, alternative splicing, and regulation of transcription, while its cell-type enhancement across several neural and renal cell types suggests broad cellular relevance. It also has a substantial literature record.
- **Conclusion**: Established evidence identifies HNRNPL as a core RNA-processing component and the clearest bridge between the central interaction cluster and the peripheral RPL12 connection. Its specific contribution to heart and skin conservation remains a hypothesis.

#### DHX9

- **Related proteins** (co-abundance neighbors): HNRNPR (0.84), HNRNPL (0.82), MATR3 (0.82); STRING partners: HNRNPL (0.901), HNRNPR (0.909), MATR3 (0.786)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is a highly connected member of the central STRING cluster and links all of HNRNPL, HNRNPR, and MATR3. It is represented in the supplementary mRNA-processing and RNA-stabilization terms (STRING NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex; within-query FDR = 0.0035) (STRING NetworkNeighborAL Mixed, incl. CRD-mediated mRNA stabilization, and Zinc finger, CHHC-type; within-query FDR = 0.0127) (STRING WikiPathways mRNA processing; within-query FDR = 0.0442). As an ATP-dependent RNA and DNA–RNA helicase with nuclear and cytoplasmic functions, it could provide RNA remodeling capacity to the module. Its disease associations span intellectual-developmental and neurodegenerative disorders, and it has an extensive literature record.
- **Conclusion**: Established evidence supports DHX9 as a catalytic RNA-remodeling component of the module core. A role in coordinating tissue-shared transcript processing is mechanistically plausible but is not demonstrated by the co-abundance result.

#### MATR3

- **Related proteins** (co-abundance neighbors): DHX9 (0.82); STRING partners: DHX9 (0.786), HNRNPL (0.757), HNRNPR (0.714)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, skin
- **hu.MAP 3.0**: huMAP3_07581.1, huMAP3_10625.1, huMAP3_05721.1
- **Function (MyGene.info)**: matrin 3. This gene encodes a nuclear matrix protein, which is proposed to stabilize certain messenger RNA species. Mutations of this gene are associated with distal myopathy 2, which often includes vocal cord and pharyngeal weakness. Alternatively spliced transcript variants, including read-through transcripts composed of the upstream small nucleolar RNA host gene 4 (non-protein coding) and matrin 3 gene s…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.735); distal myopathy with vocal cord weakness (0.569); neurodegenerative disease (0.529); distal myopathy (0.384); hereditary disease (0.193)
- **Europe PMC papers**: 1756
- **Why important**: MATR3 is directly connected to DHX9, HNRNPL, and HNRNPR in STRING and recurs with the other core proteins in hu.MAP complexes (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_05721.1). Its annotation describes a nuclear matrix protein proposed to stabilize messenger RNA, with post-transcriptional regulation among its biological processes. It has established disease associations with distal myopathy, vocal-cord weakness, and amyotrophic lateral sclerosis, linking RNA control to muscle and neurodegenerative biology. Its literature record is substantial.
- **Conclusion**: Established evidence supports MATR3 as a structural and RNA-stability component of the core, with particular relevance to muscle-related disease biology. Whether it drives the heart–skin module or merely co-varies with the RNA-processing machinery remains unresolved.

