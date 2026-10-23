# Conserved co-abundance modules: heart and ovary

## Module 0

**Tissue pair**: heart and ovary  
**Genes (10)**: ACO2, AIFM1, ATP5F1A, CRAT, CPT2, IMMT, NDUFA10, NDUFS1, NDUFS2, UQCRC2

### Function

This is a mitochondrial energy-metabolism module. The strongest primary evidence is the highly specific enrichment for the mitochondrial inner membrane and related mitochondrial membrane compartments (GO:CC mitochondrial inner membrane; q_global = 0.000713), (GO:CC organelle inner membrane; q_global = 0.000859), (GO:CC mitochondrial membrane; q_global = 0.00435), (GO:CC mitochondrial envelope; q_global = 0.00768), and (GO:CC organelle envelope; q_global = 0.0184). The module also supports thermogenesis (KEGG Thermogenesis - Homo sapiens (human); q_global = 0.0126) and diabetic cardiomyopathy (KEGG Diabetic cardiomyopathy - Homo sapiens (human); q_global = 0.0286), although these pathway labels are broader disease or physiological interpretations of the underlying mitochondrial biology. The genes span respiratory-chain complex I, complex III, ATP synthase, mitochondrial cristae organization, the citric acid cycle, and fatty-acid oxidation. Thus, the most defensible interpretation is coordinated mitochondrial oxidative phosphorylation and fuel oxidation, with potential relevance to tissue energy demand and metabolic stress. The STRING results independently support an inner-membrane respiratory network (STRING Component Mitochondrial inner membrane; within-query FDR = 0.00016), (STRING Keyword Mitochondrion inner membrane; within-query FDR = 0.00042), (STRING Component Inner mitochondrial membrane protein complex; within-query FDR = 0.0023), (STRING KEGG Thermogenesis; within-query FDR = 0.0024), (STRING COMPARTMENTS Mitochondrial inner membrane; within-query FDR = 0.0029), (STRING COMPARTMENTS Inner mitochondrial membrane protein complex; within-query FDR = 0.0036), (STRING KEGG Oxidative phosphorylation; within-query FDR = 0.0113), and (STRING Keyword Respiratory chain; within-query FDR = 0.0214).

**Cell composition.** The module is not composed of plasma or secreted proteins: every gene has no secreted-protein annotation, and all genes show low immune-cell specificity in HPA. This argues against a blood-cell or circulating-protein explanation. HPA shows mitochondrial localization and protein detection throughout heart, while detection is more heterogeneous in ovary. Most genes have tissue-enhanced or cell-type-enhanced profiles rather than uniformly broad housekeeping expression. Enrichment is seen across tongue, skeletal muscle, heart muscle, liver, oocytes, hepatocytes, enterocytes, trophoblasts, and other specialized cell types. Therefore, the shared heart–ovary signal is most plausibly a conserved mitochondrial program, while variation in tissue or cell composition could influence its apparent abundance. The HPA profile does not support an immune or plasma contamination explanation.

**GO/KEGG enrichment**: 7 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrial inner membrane | 0.000713 | AIFM1, ATP5F1A, CPT2, CRAT, IMMT, NDUFA10, NDUFS1, NDUFS2, UQCRC2 |
| GO:CC organelle inner membrane | 0.000859 | AIFM1, ATP5F1A, CPT2, CRAT, IMMT, NDUFA10, NDUFS1, NDUFS2, UQCRC2 |
| GO:CC mitochondrial membrane | 0.00435 | AIFM1, ATP5F1A, CPT2, CRAT, IMMT, NDUFA10, NDUFS1, NDUFS2, UQCRC2 |
| GO:CC mitochondrial envelope | 0.00768 | AIFM1, ATP5F1A, CPT2, CRAT, IMMT, NDUFA10, NDUFS1, NDUFS2, UQCRC2 |
| KEGG Thermogenesis - Homo sapiens (human) | 0.0126 | ATP5F1A, CPT2, NDUFA10, NDUFS1, NDUFS2, UQCRC2 |
| GO:CC organelle envelope | 0.0184 | AIFM1, ATP5F1A, CPT2, CRAT, IMMT, NDUFA10, NDUFS1, NDUFS2, UQCRC2 |
| KEGG Diabetic cardiomyopathy - Homo sapiens (human) | 0.0286 | ATP5F1A, CPT2, NDUFA10, NDUFS1, NDUFS2, UQCRC2 |

### STRING and hu.MAP

STRING provides substantial prior support for the module's biological coherence. The strongest known relationships connect NDUFS1, NDUFS2, and NDUFA10 within complex I-associated respiratory-chain biology, while UQCRC2 connects the network to complex III and ATP5F1A connects it to ATP synthase. ACO2 links the respiratory network to the citric acid cycle, and IMMT links it to mitochondrial inner-membrane and cristae organization. STRING therefore supports both direct or functionally associated respiratory-chain relationships and a broader mitochondrial energy network; its evidence is supplementary rather than globally corrected enrichment evidence. hu.MAP independently places NDUFS1, NDUFS2, and NDUFA10 together in several complex-I-related assemblies (hu.MAP huMAP3_14018.1), (hu.MAP huMAP3_06397.1), (hu.MAP huMAP3_09982.1), (hu.MAP huMAP3_09567.1), (hu.MAP huMAP3_14878.1), (hu.MAP huMAP3_07653.1), and (hu.MAP huMAP3_02819.1). It also links UQCRC2 with ATP5F1A (hu.MAP huMAP3_07245.1) and CPT2 with CRAT in a metabolic complex (hu.MAP huMAP3_13468.1). These observations indicate that part of the module recapitulates established protein complexes, while the full co-abundance module also joins proteins from neighboring respiratory and fuel-utilization systems.

**STRING interactions (score >= 0.7)**: 19 of 45 gene pairs: ACO2–ATP5F1A (0.884); ACO2–NDUFA10 (0.747); ACO2–NDUFS1 (0.865); ACO2–NDUFS2 (0.955); ACO2–UQCRC2 (0.879); ATP5F1A–IMMT (0.809); ATP5F1A–NDUFA10 (0.759); ATP5F1A–NDUFS1 (0.961); ATP5F1A–NDUFS2 (0.98); ATP5F1A–UQCRC2 (0.986); IMMT–NDUFS1 (0.901); IMMT–NDUFS2 (0.735); IMMT–UQCRC2 (0.811); NDUFA10–NDUFS1 (0.999); NDUFA10–NDUFS2 (0.999); NDUFA10–UQCRC2 (0.986); NDUFS1–NDUFS2 (0.999); NDUFS1–UQCRC2 (0.998); NDUFS2–UQCRC2 (0.994)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Mitochondrial inner membrane (FDR = 0.00016, 9 genes); Keyword Mitochondrion inner membrane (FDR = 0.00042, 8 genes); Component Inner mitochondrial membrane protein complex (FDR = 0.0023, 6 genes); KEGG Thermogenesis (FDR = 0.0024, 6 genes); COMPARTMENTS Mitochondrial inner membrane (FDR = 0.0029, 8 genes); Keyword Mitochondrion (FDR = 0.0029, 10 genes); Keyword Transit peptide (FDR = 0.0029, 9 genes); COMPARTMENTS Inner mitochondrial membrane protein complex (FDR = 0.0036, 6 genes); Keyword Primary mitochondrial disease (FDR = 0.0036, 6 genes); COMPARTMENTS Mitochondrion (FDR = 0.0043, 10 genes); Component Mitochondrion (FDR = 0.0074, 10 genes); KEGG Oxidative phosphorylation (FDR = 0.0113, 5 genes); Keyword Transport (FDR = 0.0178, 7 genes); Keyword Respiratory chain (FDR = 0.0214, 4 genes); Keyword 4Fe-4S (FDR = 0.0215, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14018.1 (NDUFS2, NDUFA10, NDUFS1; 3/48); huMAP3_06397.1 (NDUFS2, NDUFA10, NDUFS1; 3/49); huMAP3_09982.1 (NDUFS2, NDUFA10, NDUFS1; 3/49); huMAP3_09567.1 (NDUFS2, NDUFA10, NDUFS1; 3/52); huMAP3_14878.1 (NDUFS2, NDUFA10, NDUFS1; 3/53); huMAP3_07245.1 (UQCRC2, ATP5F1A; 2/4); huMAP3_07653.1 (NDUFA10, NDUFS1; 2/7); huMAP3_02819.1 (NDUFA10, NDUFS1; 2/34); huMAP3_13468.1 (CPT2, CRAT; 2/99)

### Novelty

The mitochondrial function itself is not a new biological finding: the annotations, STRING relationships, hu.MAP complexes, disease links, and substantial literature for several genes establish this biology independently. The potentially new aspect is the coordinated co-abundance of these genes as a conserved module across heart and ovary. However, the fact sheet does not provide an external replication cohort, comparison with previously reported tissue co-abundance modules, or a test of module preservation against existing resources. Consequently, this should be described as a potentially novel tissue-pair module rather than a proven new mechanism. The absence of hu.MAP annotation for some genes, or the absence of a particular STRING relationship, does not establish novelty. The strongest novelty claim is therefore at the level of the observed cross-tissue co-abundance configuration, not at the level of mitochondrial oxidative phosphorylation.

**Hypothesis.** Hypothesis: in heart and ovary, coordinated abundance of inner-membrane respiratory proteins, cristae machinery, ATP synthase, and lipid-fuel enzymes maintains mitochondrial energy production across cells with high or changing metabolic demand. IMMT may help organize cristae architecture, allowing complex-I-associated electron transfer, complex-III activity, and ATP synthase function to operate efficiently, while CPT2 and CRAT adjust delivery and buffering of fatty-acid-derived acyl groups. This could generate the observed association with thermogenesis and diabetic cardiomyopathy pathways (KEGG Thermogenesis - Homo sapiens (human); q_global = 0.0126), (KEGG Diabetic cardiomyopathy - Homo sapiens (human); q_global = 0.0286). The hypothesis predicts that perturbing cristae organization or fatty-acid entry should alter respiratory-chain performance and ATP production together, but the co-abundance data alone do not establish directionality, physical interaction for every pair, or causation.

### Important genes

#### IMMT

- **Related proteins** (co-abundance neighbors): AIFM1 (0.86), ACO2 (0.84), NDUFA10 (0.84), UQCRC2 (0.83); STRING partners: ATP5F1A (0.809), NDUFS1 (0.901), NDUFS2 (0.735), UQCRC2 (0.811)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inner membrane mitochondrial protein. Enables RNA binding activity. Involved in cristae formation. Located in mitochondrial inner membrane. Part of MICOS complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); multinodular goiter (0.196); alcohol drinking (0.190); breast cancer (0.094); neoplasm (0.087)
- **Europe PMC papers**: 933
- **Why important**: IMMT is a central network connector and is annotated as a mitochondrial inner-membrane and MICOS-complex protein involved in cristae formation. It participates in the primary mitochondrial compartment terms (GO:CC mitochondrial inner membrane; q_global = 0.000713), (GO:CC organelle inner membrane; q_global = 0.000859), (GO:CC mitochondrial membrane; q_global = 0.00435), (GO:CC mitochondrial envelope; q_global = 0.00768), and (GO:CC organelle envelope; q_global = 0.0184), and is supported by multiple STRING inner-membrane terms (STRING Component Mitochondrial inner membrane; within-query FDR = 0.00016), (STRING Keyword Mitochondrion inner membrane; within-query FDR = 0.00042), (STRING Component Inner mitochondrial membrane protein complex; within-query FDR = 0.0023), (STRING COMPARTMENTS Mitochondrial inner membrane; within-query FDR = 0.0029), (STRING COMPARTMENTS Inner mitochondrial membrane protein complex; within-query FDR = 0.0036). Its connections to AIFM1, ACO2, NDUFA10, and UQCRC2 bridge membrane architecture with respiratory and metabolic proteins. It also has substantial literature support and disease associations involving neurodegenerative disease.
- **Conclusion**: Established evidence supports IMMT as a structural organizer of the mitochondrial inner membrane and cristae. Its network position makes it a plausible integrator of the module. It is a strong mechanistic candidate, but the co-abundance data do not prove that IMMT drives the abundance of the other genes.

#### UQCRC2

- **Related proteins** (co-abundance neighbors): NDUFS2 (0.85), IMMT (0.83), NDUFS1 (0.82), AIFM1 (0.80); STRING partners: ACO2 (0.879), ATP5F1A (0.986), IMMT (0.811), NDUFA10 (0.986), NDUFS1 (0.998), NDUFS2 (0.994)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, ovary
- **hu.MAP 3.0**: huMAP3_07245.1
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase core protein 2. The protein encoded by this gene is located in the mitochondrion, where it is part of the ubiquinol-cytochrome c reductase complex (also known as complex III). This complex constitutes a part of the mitochondrial respiratory chain. Defects in this gene are a cause of mitochondrial complex III deficiency nuclear type 5. [provided by RefSeq, Jul 2015].
- **Diseases (Open Targets)**: mitochondrial complex III deficiency (0.732); neurodegenerative disease (0.423); mitochondrial disease (0.312); gastric cancer (0.085); adrenoleukodystrophy (0.075)
- **Europe PMC papers**: 3297
- **Why important**: UQCRC2 is a highly connected module gene that is part of mitochondrial complex III and links to ACO2, ATP5F1A, IMMT, NDUFA10, NDUFS1, and NDUFS2 in STRING. It appears in every primary GO/KEGG term (GO:CC mitochondrial inner membrane; q_global = 0.000713) through (KEGG Diabetic cardiomyopathy - Homo sapiens (human); q_global = 0.0286) and in the hu.MAP complex linking UQCRC2 with ATP5F1A (hu.MAP huMAP3_07245.1). Its established role in ubiquinol-to-cytochrome-c electron transport directly connects the module to oxidative phosphorylation. It has strong literature support and disease associations with mitochondrial complex III deficiency and mitochondrial disease.
- **Conclusion**: Established evidence identifies UQCRC2 as a core complex-III respiratory-chain component and a major network bridge. Its inclusion strongly supports an electron-transport interpretation. Its role as a causal regulator of the shared heart–ovary module remains a hypothesis.

#### NDUFS1

- **Related proteins** (co-abundance neighbors): CRAT (0.84), UQCRC2 (0.82); STRING partners: ACO2 (0.865), ATP5F1A (0.961), IMMT (0.901), NDUFA10 (0.999), NDUFS2 (0.999), UQCRC2 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1, huMAP3_07653.1, huMAP3_02819.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S1. The protein encoded by this gene belongs to the complex I 75 kDa subunit family. Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Thi…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 5 (0.810); mitochondrial complex I deficiency (0.647); type 2 diabetes mellitus (0.608); Parkinson disease (0.603); diabetes mellitus (0.580)
- **Europe PMC papers**: 2567
- **Why important**: NDUFS1 is the largest nuclear-encoded complex-I subunit represented here and has a central position in the known respiratory network, with STRING links to ACO2, ATP5F1A, IMMT, NDUFA10, NDUFS2, and UQCRC2. It occurs in all primary GO/KEGG terms (GO:CC mitochondrial inner membrane; q_global = 0.000713) through (KEGG Diabetic cardiomyopathy - Homo sapiens (human); q_global = 0.0286), all listed STRING enrichment categories relevant to respiratory-chain biology, and many hu.MAP complex-I assemblies (hu.MAP huMAP3_14018.1), (hu.MAP huMAP3_06397.1), (hu.MAP huMAP3_09982.1), (hu.MAP huMAP3_09567.1), (hu.MAP huMAP3_14878.1), (hu.MAP huMAP3_07653.1), and (hu.MAP huMAP3_02819.1). Its annotations include NADH-to-ubiquinone electron transfer, proton-motive-force-driven ATP synthesis, and complex-I assembly. It also has substantial literature and disease associations with complex-I deficiency, diabetes, and Parkinson disease.
- **Conclusion**: Established evidence supports NDUFS1 as a core complex-I component and a major explanatory gene for the module's respiratory function. Its high connectivity to other respiratory proteins reflects known biology rather than a newly demonstrated interaction. A special regulatory role in heart–ovary coordination is not established.

#### ATP5F1A

- **Related proteins** (co-abundance neighbors): ACO2 (0.83); STRING partners: ACO2 (0.884), IMMT (0.809), NDUFA10 (0.759), NDUFS1 (0.961), NDUFS2 (0.98), UQCRC2 (0.986)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart, ovary
- **hu.MAP 3.0**: huMAP3_07245.1
- **Function (MyGene.info)**: ATP synthase F1 subunit alpha. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, using an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic po…
- **Diseases (Open Targets)**: mitochondrial complex V (ATP synthase) deficiency, nuclear type 4A (0.655); mitochondrial proton-transporting ATP synthase complex deficiency (0.648); mitochondrial complex V (ATP synthase) deficiency, nuclear type 4B (0.532); hereditary disease (0.394); Mitochondrial encephalopathy (0.371)
- **Europe PMC papers**: 822
- **Why important**: ATP5F1A represents the catalytic F1 sector of mitochondrial ATP synthase and therefore connects respiratory-chain proton-gradient generation to ATP production. It occurs in all primary GO/KEGG terms (GO:CC mitochondrial inner membrane; q_global = 0.000713) through (KEGG Diabetic cardiomyopathy - Homo sapiens (human); q_global = 0.0286), has STRING associations with ACO2, IMMT, NDUFA10, NDUFS1, NDUFS2, and UQCRC2, and participates with UQCRC2 in hu.MAP complex (hu.MAP huMAP3_07245.1). Its annotations include ATP biosynthesis, proton-motive-force-driven ATP synthesis, lipid metabolism, and response to muscle activity. It has disease associations involving mitochondrial complex-V deficiency and mitochondrial encephalopathy.
- **Conclusion**: Established evidence supports ATP5F1A as the module's clearest ATP-production component and as a functional link between electron transport and cellular energy output. The module does not establish whether ATP synthase abundance is limiting or merely co-regulated with the respiratory machinery.

#### CPT2

- **Related proteins** (co-abundance neighbors): CRAT (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: carnitine palmitoyltransferase 2. The protein encoded by this gene is a nuclear protein which is transported to the mitochondrial inner membrane. Together with carnitine palmitoyltransferase I, the encoded protein oxidizes long-chain fatty acids in the mitochondria. Defects in this gene are associated with mitochondrial long-chain fatty-acid (LCFA) oxidation disorders. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: carnitine palmitoyl transferase II deficiency, myopathic form (0.830); carnitine palmitoyl transferase II deficiency, severe infantile form (0.800); carnitine palmitoyl transferase II deficiency, neonatal form (0.772); carnitine palmitoyltransferase II deficiency (0.710); hereditary disease (0.505)
- **Europe PMC papers**: 5133
- **Why important**: CPT2 provides the clearest link to long-chain fatty-acid utilization. It participates in all primary GO/KEGG terms (GO:CC mitochondrial inner membrane; q_global = 0.000713) through (KEGG Diabetic cardiomyopathy - Homo sapiens (human); q_global = 0.0286), in STRING terms for the inner membrane, thermogenesis, mitochondrial disease, transport, and mitochondria (STRING Component Mitochondrial inner membrane; within-query FDR = 0.00016), (STRING KEGG Thermogenesis; within-query FDR = 0.0024), (STRING COMPARTMENTS Mitochondrial inner membrane; within-query FDR = 0.0029), (STRING Keyword Mitochondrion; within-query FDR = 0.0029), (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0043), (STRING Component Mitochondrion; within-query FDR = 0.0074), (STRING Keyword Transport; within-query FDR = 0.0178), and in the CPT2–CRAT metabolic complex (hu.MAP huMAP3_13468.1). Its established functions include the carnitine shuttle and mitochondrial long-chain fatty-acid beta-oxidation, with disease associations spanning several forms of CPT2 deficiency. Its tissue and cell-type annotations include liver, trophoblasts, hepatocytes, and reproductive cell contexts, making it relevant to the cross-tissue interpretation.
- **Conclusion**: Established evidence supports CPT2 as the fuel-entry and fatty-acid-oxidation component of the module. Its co-abundance with respiratory proteins supports coordinated fuel oxidation as an interpretation, but does not demonstrate that fatty-acid flux causes the module or that the same substrate preference operates in every relevant heart or ovary cell.

## Module 1

**Tissue pair**: heart and ovary  
**Genes (11)**: APMAP, ASPH, ATP1A1, ITGB1, DDOST, RAB10, RAB18, RAB8A, RTN4, SEC22B, SCCPDH

### Function

The strongest and most coherent interpretation is an endoplasmic-reticulum and endomembrane trafficking module. The primary evidence is the globally corrected enrichment for the ER tubular network and its organization (GO:CC endoplasmic reticulum tubular network; q_global = 0.000493) (GO:BP endoplasmic reticulum tubular network organization; q_global = 0.0138), organelle subcompartments (GO:CC organelle subcompartment; q_global = 0.00689) (GO:CC endoplasmic reticulum subcompartment; q_global = 0.0446), and ER membrane (GO:CC endoplasmic reticulum membrane; q_global = 0.0446). RTN4 is associated with ER organization, while RAB10 and RAB18 regulate vesicle and intracellular transport; DDOST supports ER oligosaccharyltransferase function, and SEC22B supports ER–Golgi vesicle trafficking. The supplementary STRING terms independently point toward ER membranes, cytoplasmic vesicle membranes, vesicle trafficking, and the endomembrane system (15 supplementary STRING terms; within-query FDR 0.003–0.0235). The module therefore most plausibly represents coordinated ER morphology, cargo processing, and vesicle movement rather than a narrowly defined biochemical complex. The co-abundance structure should not be interpreted as proof that every gene physically interacts with every other gene.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, which is compatible with broadly distributed cellular machinery rather than a heart- or ovary-exclusive program. At the same time, HPA single-cell annotations are frequently cell-type enhanced, with recurring signals in neutrophils and related immune or progenitor populations, and some genes show enrichment in trophoblast populations. Blood-cell specificity is low for most genes, but immune-enhanced or immune-enriched annotations occur for RTN4, ASPH, and SCCPDH. These findings raise the possibility that part of the shared heart–ovary signal reflects common cell-type composition, vascular or immune-associated material, or broadly expressed membrane machinery. The absence of secreted proteins argues against a circulating secretome explanation. Protein detection is stronger in ovary than in heart for the module as a whole, while several key ER or trafficking genes are not detected in heart muscle by HPA; this cautions against equating transcript co-abundance with uniform protein abundance in both tissues.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC endoplasmic reticulum tubular network | 0.000493 | ASPH, RAB10, RAB18, RTN4 |
| GO:CC organelle subcompartment | 0.00689 | ASPH, DDOST, RAB10, RAB18, RAB8A, RTN4, SEC22B |
| GO:BP endoplasmic reticulum tubular network organization | 0.0138 | RAB10, RAB18, RTN4 |
| GO:CC endoplasmic reticulum membrane | 0.0446 | ASPH, DDOST, RAB10, RAB18, RTN4, SEC22B |
| GO:CC endoplasmic reticulum subcompartment | 0.0446 | ASPH, DDOST, RAB10, RAB18, RTN4, SEC22B |

### STRING and hu.MAP

STRING provides direct high-confidence support for the RAB10–RAB8A relationship. STRING functional enrichment also connects the module to the ER tubular network, ER membrane, cytoplasmic vesicle membrane, endomembrane system, and phagocytic vesicle membrane (15 supplementary STRING terms; within-query FDR 0.003–0.0235). These annotations are supplementary and are concordant with, but do not replace, the globally corrected GO evidence. hu.MAP repeatedly places RAB10 and RAB8A together in broad Rab-family trafficking complexes (hu.MAP huMAP3_07302.1) (hu.MAP huMAP3_06607.1) (hu.MAP huMAP3_01895.1) (hu.MAP huMAP3_06994.1) (hu.MAP huMAP3_08941.1) (hu.MAP huMAP3_09217.1) (hu.MAP huMAP3_11094.1) (hu.MAP huMAP3_11860.1). The repeated pair is consistent with established Rab-mediated vesicle biology, but the complexes contain many additional Rab proteins and only a small subset of their members is present in this module. Most other module genes lack a reported STRING partner or hu.MAP complex in the supplied evidence. Thus, the module combines an established Rab trafficking core with co-abundance links that are not demonstrated physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 55 gene pairs: RAB10–RAB8A (0.831)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Organelle subcompartment (FDR = 0.003, 6 genes); COMPARTMENTS Endoplasmic reticulum tubular network (FDR = 0.003, 4 genes); Component Organelle subcompartment (FDR = 0.0031, 7 genes); Component Endoplasmic reticulum tubular network (FDR = 0.0031, 4 genes); COMPARTMENTS Endoplasmic reticulum membrane (FDR = 0.0052, 5 genes); COMPARTMENTS Cytoplasmic vesicle membrane (FDR = 0.0052, 6 genes); COMPARTMENTS Endoplasmic reticulum subcompartment (FDR = 0.0052, 5 genes); Component Endoplasmic reticulum membrane (FDR = 0.0063, 6 genes); Component Cytoplasmic vesicle membrane (FDR = 0.0094, 6 genes); Component Endomembrane system (FDR = 0.0126, 10 genes); Component Phagocytic vesicle membrane (FDR = 0.0185, 3 genes); Component Integral component of membrane (FDR = 0.02, 8 genes); Component Cytoplasmic vesicle (FDR = 0.02, 8 genes); Component Bounding membrane of organelle (FDR = 0.02, 7 genes); COMPARTMENTS Endomembrane system (FDR = 0.0235, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07302.1 (RAB8A, RAB10; 2/13); huMAP3_06607.1 (RAB8A, RAB10; 2/16); huMAP3_01895.1 (RAB8A, RAB10; 2/19); huMAP3_06994.1 (RAB8A, RAB10; 2/24); huMAP3_08941.1 (RAB8A, RAB10; 2/28); huMAP3_09217.1 (RAB8A, RAB10; 2/29); huMAP3_11094.1 (RAB8A, RAB10; 2/43); huMAP3_11860.1 (RAB8A, RAB10; 2/44)

### Novelty

The tissue-shared co-abundance pattern may be a useful candidate observation, but the fact sheet does not establish a new molecular mechanism. Its central ER and vesicle interpretation is strongly supported by existing annotations (5 globally significant GO/KEGG terms, q_global 0.000493–0.0446; see the table), the known RAB10–RAB8A relationship, and repeated hu.MAP Rab complexes (hu.MAP huMAP3_07302.1) (hu.MAP huMAP3_06607.1) (hu.MAP huMAP3_01895.1) (hu.MAP huMAP3_06994.1) (hu.MAP huMAP3_08941.1) (hu.MAP huMAP3_09217.1) (hu.MAP huMAP3_11094.1) (hu.MAP huMAP3_11860.1). The limited direct STRING connectivity outside that Rab pair suggests that the particular cross-tissue co-abundance arrangement may not correspond to a previously curated physical complex. However, absence from STRING or hu.MAP cannot by itself demonstrate novelty, because co-abundance relationships can be context-dependent, tissue-composition-driven, or underrepresented in interaction databases. The appropriate novelty claim is therefore a potentially informative heart–ovary co-abundance association involving known ER and trafficking biology, not a newly discovered pathway.

**Hypothesis.** Hypothesis: shared cellular or cell-composition features in heart and ovary increase the coordinated abundance of an ER–endomembrane program. RTN4 may help maintain tubular ER architecture, DDOST may support maturation of newly synthesized glycoproteins, SEC22B may couple ER and Golgi transport, and RAB18, RAB10, and RAB8A may coordinate movement of cargo through vesicular compartments. ATP1A1 and ITGB1 may connect this trafficking state to plasma-membrane organization, ion gradients, adhesion, or cellular stress. The immune and neutrophil-associated HPA signals suggest that the observed module could also be strengthened by shared immune or vascular cell contributions rather than being intrinsic to cardiomyocytes and ovarian cells alone. This hypothesis requires validation with cell-resolved data, protein measurements, and perturbation of the trafficking components.

### Important genes

#### RTN4

- **Related proteins** (co-abundance neighbors): ITGB1 (0.91), ASPH (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: reticulon 4. This gene belongs to the family of reticulon encoding genes. Reticulons are associated with the endoplasmic reticulum, and are involved in neuroendocrine secretion or in membrane trafficking in neuroendocrine cells. The product of this gene is a potent neurite outgrowth inhibitor which may also help block the regeneration of the central nervous system in higher vertebrates. Alternatively spliced t…
- **Diseases (Open Targets)**: obesity disorder (0.382); neurodegenerative disease (0.257); skin cancer (0.231); sensorineural hearing loss disorder (0.215); hearing loss disorder (0.210)
- **Europe PMC papers**: 2070
- **Why important**: RTN4 is the clearest structural anchor for the module: it has the strongest direct ER annotation, appears in every globally significant term (5 globally significant GO/KEGG terms, q_global 0.000493–0.0446; see the table), and is linked to ER organization, membrane trafficking, and epithelial or leukocyte migration. Its module connections to ITGB1 and ASPH place it at a possible interface between ER structure and cell-surface behavior. It has a substantial literature record and disease links involving neurodegeneration, hearing disorders, and obesity-related disease.
- **Conclusion**: Established evidence supports RTN4 as an ER-associated structural and trafficking component of the module. A role as the principal organizer of the shared heart–ovary co-abundance state is a hypothesis, not demonstrated by the supplied network.

#### RAB10

- **Related proteins** (co-abundance neighbors): RAB18 (0.86); STRING partners: RAB8A (0.831)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in heart, ovary
- **hu.MAP 3.0**: huMAP3_07302.1, huMAP3_06607.1, huMAP3_01895.1, huMAP3_06994.1, huMAP3_08941.1, huMAP3_09217.1, huMAP3_11094.1, huMAP3_11860.1
- **Function (MyGene.info)**: RAB10, member RAS oncogene family. RAB10 belongs to the RAS (see HRAS; MIM 190020) superfamily of small GTPases. RAB proteins localize to exocytic and endocytic compartments and regulate intracellular vesicle trafficking (Bao et al., 1998 [PubMed 9918381]).[supplied by OMIM, Mar 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.549); digestive system disorder (0.242); cervical carcinoma (0.215); lobular capilliary hemangioma (0.165); hepatocellular carcinoma (0.109)
- **Europe PMC papers**: 2856
- **Why important**: RAB10 is a central functional marker of vesicle transport and appears in every globally significant term (5 globally significant GO/KEGG terms, q_global 0.000493–0.0446; see the table). It is directly connected to RAB18 in the co-abundance graph and has the sole high-confidence STRING interaction with RAB8A; it also occurs in every listed hu.MAP Rab complex (hu.MAP huMAP3_07302.1) (hu.MAP huMAP3_06607.1) (hu.MAP huMAP3_01895.1) (hu.MAP huMAP3_06994.1) (hu.MAP huMAP3_08941.1) (hu.MAP huMAP3_09217.1) (hu.MAP huMAP3_11094.1) (hu.MAP huMAP3_11860.1). Its annotations include exocytosis, Golgi-to-plasma-membrane transport, endosomal transport, and antigen processing. It has a substantial literature record and disease associations involving neurodegenerative and other disorders.
- **Conclusion**: Established evidence identifies RAB10 as a key trafficking component and as part of the best-supported known interaction in the module. Its position as a driver that coordinates the entire tissue-shared module remains hypothetical.

#### RAB18

- **Related proteins** (co-abundance neighbors): RAB10 (0.86), DDOST (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in heart, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB18, member RAS oncogene family. The protein encoded by this gene is a member of a family of Ras-related small GTPases that regulate membrane trafficking in organelles and transport vesicles. Knockdown studies is zebrafish suggest that this protein may have a role in eye and brain development. Mutations in this gene are associated with Warburg micro syndrome type 3. Alternatively spliced transcript variants have been found for th…
- **Diseases (Open Targets)**: Warburg micro syndrome (0.815); neurodegenerative disease (0.496); cerebral atherosclerosis (0.275); malunion fracture (0.239); adolescent idiopathic scoliosis (0.229)
- **Europe PMC papers**: 2168
- **Why important**: RAB18 appears in every globally significant term (5 globally significant GO/KEGG terms, q_global 0.000493–0.0446; see the table), is connected to RAB10 and DDOST, and is repeatedly associated with ER and vesicle compartments in STRING (10 supplementary STRING terms; within-query FDR 0.003–0.0126) and (STRING Component Cytoplasmic vesicle; within-query FDR = 0.02) (STRING Component Bounding membrane of organelle; within-query FDR = 0.02) (STRING COMPARTMENTS Endomembrane system; within-query FDR = 0.0235). Its established functions include intracellular protein transport, lipid-droplet organization, and sterol homeostasis. It has a substantial literature record and a strong disease association with Warburg micro syndrome.
- **Conclusion**: Established evidence supports RAB18 as an ER and intracellular-trafficking component that could connect membrane transport with lipid and sterol handling. A specific role in producing the shared heart–ovary signature is a hypothesis.

#### DDOST

- **Related proteins** (co-abundance neighbors): ATP1A1 (0.86), SEC22B (0.82), RAB18 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in heart, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dolichyl-diphosphooligosaccharide--protein glycosyltransferase non-catalytic subunit. This gene encodes a component of the oligosaccharyltransferase complex which catalyzes the transfer of high-mannose oligosaccharides to asparagine residues on nascent polypeptides in the lumen of the rough endoplasmic reticulum. The protein complex co-purifies with ribosomes. The product of this gene is also implicated in the processing of advanced glycation endproducts (AGEs), which form from non…
- **Diseases (Open Targets)**: DDOST-congenital disorder of glycosylation (0.734); young-onset Parkinson disease (0.561); neurodegenerative disease (0.539); dengue disease (0.505); congenital disorder of glycosylation (0.373)
- **Europe PMC papers**: 685
- **Why important**: DDOST contributes to the globally significant organelle-subcompartment and ER-membrane terms (GO:CC organelle subcompartment; q_global = 0.00689) (GO:CC endoplasmic reticulum membrane; q_global = 0.0446) (GO:CC endoplasmic reticulum subcompartment; q_global = 0.0446). It is an ER oligosaccharyltransferase-complex component involved in N-linked glycosylation and is connected in the module to ATP1A1, SEC22B, and RAB18. Its protein is detected in both heart and ovary by HPA, and it has disease associations involving congenital disorders of glycosylation and neurodegenerative disease.
- **Conclusion**: Established evidence supports DDOST as the module's strongest link to ER protein maturation and glycosylation. It may couple cargo quality or glycosylation state to vesicle trafficking, but that coupling is a mechanistic hypothesis rather than a demonstrated property of this module.

#### SEC22B

- **Related proteins** (co-abundance neighbors): ATP1A1 (0.89), DDOST (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC22 homolog B, vesicle trafficking protein. The protein encoded by this gene is a member of the SEC22 family of vesicle trafficking proteins. It seems to complex with SNARE and it is thought to play a role in the ER-Golgi protein trafficking. This protein has strong similarity to Mus musculus and Cricetulus griseus proteins.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: inflammatory bowel disease (0.285); luminal A breast carcinoma (0.271); colitis (0.238); enteritis (0.238); Crohn disease (0.233)
- **Europe PMC papers**: 1006
- **Why important**: SEC22B is present in the globally significant organelle-subcompartment and ER-membrane terms (GO:CC organelle subcompartment; q_global = 0.00689) (GO:CC endoplasmic reticulum membrane; q_global = 0.0446) (GO:CC endoplasmic reticulum subcompartment; q_global = 0.0446) and is annotated for ER-to-Golgi transport, retrograde transport, vesicle fusion, and macroautophagy. Its network links to ATP1A1 and DDOST, while STRING places it in ER, vesicle, and endomembrane annotations (STRING Component Organelle subcompartment; within-query FDR = 0.0031) (STRING COMPARTMENTS Cytoplasmic vesicle membrane; within-query FDR = 0.0052) (8 supplementary STRING terms; within-query FDR 0.0063–0.0235). It has a substantial literature record and disease associations involving inflammatory bowel and intestinal disorders.
- **Conclusion**: Established evidence supports SEC22B as a vesicle-fusion and ER–Golgi trafficking component. Its connection to the heart–ovary module may indicate coordinated cargo flow, but the tissue-specific consequence is hypothetical.

#### ATP1A1

- **Related proteins** (co-abundance neighbors): SEC22B (0.89), ITGB1 (0.86), DDOST (0.86), RAB8A (0.86), SCCPDH (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 has the strongest network connectivity in the supplied module and links SEC22B, ITGB1, DDOST, RAB8A, and SCCPDH. It provides a plasma-membrane and vesicle-associated connection to the ER–endomembrane program through maintenance of sodium and potassium gradients. It has the largest literature footprint among the selected genes and disease associations involving cardiac failure, atrial fibrillation, and neurological syndromes.
- **Conclusion**: Established evidence supports ATP1A1 as a highly connected membrane transporter with relevance to electrical excitability and cardiac physiology. Its incorporation into this ER-trafficking module may reflect membrane homeostasis or shared cellular state, but a direct mechanistic bridge to the ER is a hypothesis.

## Module 2

**Tissue pair**: heart and ovary  
**Genes (5)**: DHX9, HNRNPL, HNRNPR, RPL12, SRSF7

### Function

The module is best interpreted as a conserved nuclear RNA-processing and pre-mRNA-splicing module shared by heart and ovary. The primary evidence is the repeated global enrichment of spliceosome-associated RNA splicing and mRNA-processing terms in (GO:BP RNA splicing, via transesterification reactions; q_global = 0.000818), (GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 0.000818), (GO:BP mRNA splicing, via spliceosome; q_global = 0.000818), (GO:BP mRNA processing; q_global = 0.00171), and (GO:BP RNA splicing; q_global = 0.00171). The same genes also support mRNA binding and mRNA metabolic processes in (GO:MF mRNA binding; q_global = 0.00413) and (GO:BP mRNA metabolic process; q_global = 0.00529), regulation of mRNA processing in (GO:BP regulation of mRNA processing; q_global = 0.00932), and ribonucleoprotein-complex biology in (GO:CC ribonucleoprotein complex; q_global = 0.0121). DHX9, HNRNPL, HNRNPR, and SRSF7 account for the core splicing signal, while RPL12 contributes to the ribonucleoprotein-complex annotation. Together, the evidence supports coordinated control of pre-mRNA maturation, RNA binding, spliceosome activity, and related ribonucleoprotein assembly rather than a tissue-specific secreted or extracellular function.

**Cell composition.** The module is composed entirely of intracellular, nucleoplasm-associated or ribosome-associated proteins rather than plasma or secreted proteins. HPA reports low tissue specificity for every member, no secreted genes, low immune-cell specificity for every member, and protein detection in both heart and ovary for every member. Thus, the shared module is unlikely to be explained primarily by blood contamination or a blood-cell-enriched signal. The broadly expressed pattern is consistent with a housekeeping-like RNA-processing program, although the presence of cell-type-enhanced annotations for some members indicates that particular components may vary among cell populations. The cross-tissue conservation should therefore be interpreted as a broadly deployed gene-expression and RNA-maturation program, not as evidence that the module is unique to heart or ovary.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA splicing, via transesterification reactions | 0.000818 | DHX9, HNRNPL, HNRNPR, SRSF7 |
| GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile | 0.000818 | DHX9, HNRNPL, HNRNPR, SRSF7 |
| GO:BP mRNA splicing, via spliceosome | 0.000818 | DHX9, HNRNPL, HNRNPR, SRSF7 |
| GO:BP mRNA processing | 0.00171 | DHX9, HNRNPL, HNRNPR, SRSF7 |
| GO:BP RNA splicing | 0.00171 | DHX9, HNRNPL, HNRNPR, SRSF7 |
| GO:MF mRNA binding | 0.00413 | DHX9, HNRNPL, HNRNPR, SRSF7 |
| GO:BP mRNA metabolic process | 0.00529 | DHX9, HNRNPL, HNRNPR, SRSF7 |
| GO:BP RNA processing | 0.00825 | DHX9, HNRNPL, HNRNPR, SRSF7 |
| GO:BP regulation of mRNA processing | 0.00932 | DHX9, HNRNPL, SRSF7 |
| GO:CC ribonucleoprotein complex | 0.0121 | DHX9, HNRNPL, HNRNPR, RPL12 |
| GO:BP regulation of mRNA metabolic process | 0.0248 | DHX9, HNRNPL, SRSF7 |

### STRING and hu.MAP

The module has extensive known STRING support among its RNA-processing members. DHX9 is connected to HNRNPL, HNRNPR, and SRSF7; HNRNPL is connected to HNRNPR and SRSF7; and HNRNPR is connected to SRSF7. These relationships reinforce a coherent RNA-binding and mRNA-splicing network rather than an arbitrary co-abundance association. STRING supplementary terms independently point to RNA binding, mRNA processing, RNA metabolism, the major mRNA-splicing pathway, RNA-recognition-motif biology, and ribonucleoprotein complexes in (STRING Keyword RNA-binding; within-query FDR = 5.15e-05), (STRING WikiPathways mRNA processing; within-query FDR = 7.36e-05), (STRING RCTM Metabolism of RNA; within-query FDR = 0.00012), (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.00023), (STRING SMART RNA recognition motif; within-query FDR = 0.0017), (STRING Process mRNA processing; within-query FDR = 0.0043), and (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.005). The hu.MAP evidence is more specific but partial: HNRNPL and HNRNPR co-occur in several known hnRNP-related complexes in (hu.MAP huMAP3_07225.1), (hu.MAP huMAP3_06093.1), (hu.MAP huMAP3_09654.1), (hu.MAP huMAP3_07581.1), (hu.MAP huMAP3_10659.1), and (hu.MAP huMAP3_10625.1). The other module members are not represented in those listed hu.MAP complexes, and RPL12 lacks a listed STRING partner within the module. Therefore, the network combines a well-supported hnRNP and splicing core with peripheral or less directly documented module membership. The hu.MAP results indicate that the co-abundance module overlaps known complexes but is not itself equivalent to any single established complex.

**STRING interactions (score >= 0.7)**: 6 of 10 gene pairs: DHX9–HNRNPL (0.901); DHX9–HNRNPR (0.909); DHX9–SRSF7 (0.789); HNRNPL–HNRNPR (0.961); HNRNPL–SRSF7 (0.926); HNRNPR–SRSF7 (0.833)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword RNA-binding (FDR = 5.15e-05, 5 genes); WikiPathways mRNA processing (FDR = 7.36e-05, 4 genes); RCTM Metabolism of RNA (FDR = 0.00012, 5 genes); NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex (FDR = 0.00016, 4 genes); RCTM mRNA Splicing - Major Pathway (FDR = 0.00023, 4 genes); SMART RNA recognition motif (FDR = 0.0017, 3 genes); NetworkNeighborAL Mixed, incl. CRD-mediated mRNA stabilization, and Zinc finger, CHHC-type (FDR = 0.0019, 3 genes); Keyword Isopeptide bond (FDR = 0.0041, 5 genes); Process mRNA processing (FDR = 0.0043, 4 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 0.005, 4 genes); Keyword Ubl conjugation (FDR = 0.0055, 5 genes); InterPro RNA recognition motif domain (FDR = 0.006, 3 genes); InterPro Nucleotide-binding alpha-beta plait domain superfamily (FDR = 0.006, 3 genes); InterPro RNA-binding domain superfamily (FDR = 0.006, 3 genes); Process Gene expression (FDR = 0.0062, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07225.1 (HNRNPR, HNRNPL; 2/7); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09654.1 (HNRNPR, HNRNPL; 2/13); huMAP3_07581.1 (HNRNPR, HNRNPL; 2/21); huMAP3_10659.1 (HNRNPR, HNRNPL; 2/28); huMAP3_10625.1 (HNRNPR, HNRNPL; 2/57)

### Novelty

The biological function is not novel: the module recapitulates well-established RNA-splicing, RNA-binding, hnRNP, and ribonucleoprotein biology, with strong support from globally corrected GO evidence, STRING relationships, and hu.MAP complexes. The potentially novel aspect is the reproducible co-abundance of this particular combination across heart and ovary. However, the fact sheet does not establish whether this exact cross-tissue module has been reported previously, and absence from a listed STRING interaction or hu.MAP complex cannot demonstrate novelty. The most defensible conclusion is that this is a biologically credible conserved module with a potentially new tissue-pair-level organization, rather than a newly discovered molecular pathway.

**Hypothesis.** Hypothesis: in both heart and ovary, coordinated abundance of DHX9, HNRNPL, HNRNPR, and SRSF7 may help maintain a shared RNA-processing state by coupling RNA remodeling and transport with hnRNP assembly and spliceosome-associated regulation. RPL12 may reflect linkage of this program to ribonucleoprotein and translational machinery. This could support tissue-wide management of transcript maturation during normal cellular maintenance, while allowing tissue-specific transcripts to be selected through alternative splicing. The co-abundance data support coordination, but they do not establish direct regulation, physical assembly of all module members, causal direction, or a specific transcript target.

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): HNRNPR (0.89), SRSF7 (0.86), HNRNPL (0.81); STRING partners: HNRNPL (0.901), HNRNPR (0.909), SRSF7 (0.789)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is the most connected module member and links directly to HNRNPL, HNRNPR, and SRSF7. It is a DExH-box RNA helicase with established ATP-dependent unwinding activity for double-stranded RNA and DNA-RNA complexes, and its annotations include spliceosome-associated alternative splicing, transcriptional regulation, and RNA export. It appears in every globally significant module term from (GO:BP RNA splicing, via transesterification reactions; q_global = 0.000818) through (GO:BP regulation of mRNA metabolic process; q_global = 0.0248) and in numerous supplementary STRING terms. Its substantial literature support and disease associations make it the strongest mechanistic anchor for the module.
- **Conclusion**: Established evidence supports DHX9 as a central RNA-remodeling and RNA-processing component of the module. Its network position and annotations make it a plausible coordinator of the other RNA-binding proteins. It remains a hypothesis, not an established fact, that DHX9 drives the cross-tissue co-abundance pattern or directly organizes the complete module.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): RPL12 (0.82), DHX9 (0.81); STRING partners: DHX9 (0.901), HNRNPR (0.961), SRSF7 (0.926)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, ovary
- **hu.MAP 3.0**: huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_07581.1, huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL has strong connectivity to DHX9, HNRNPR, SRSF7, and RPL12, and it is present in every globally significant enrichment term. It is a nucleoplasmic heterogeneous nuclear ribonucleoprotein associated with formation, packaging, processing, and function of messenger RNA. HNRNPL is also the most consistently represented module member in the listed hu.MAP hnRNP complexes, where it repeatedly appears with HNRNPR. Its extensive literature base and associations with dengue disease, neuromuscular disease, and ovarian cancer add biological relevance.
- **Conclusion**: Established evidence identifies HNRNPL as a central hnRNP and mRNA-processing scaffold within the module. Its repeated hu.MAP representation supports membership in established RNA-protein assemblies. It is a plausible integration point between the core splicing proteins and RPL12, but a specific role in heart-ovary coordination remains a hypothesis.

#### HNRNPR

- **Related proteins** (co-abundance neighbors): DHX9 (0.89); STRING partners: DHX9 (0.909), HNRNPL (0.961), SRSF7 (0.833)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, ovary
- **hu.MAP 3.0**: huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_07581.1, huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR is a spliceosome C-complex-associated RNA-binding protein involved in pre-mRNA processing and transport. It is connected in STRING to DHX9, HNRNPL, and SRSF7, participates with HNRNPL in every listed hu.MAP complex, and appears across the core globally significant splicing and mRNA-processing terms. Its disease associations include neurodevelopmental and intellectual-disability phenotypes, indicating that altered RNA processing involving this gene can have organism-level consequences.
- **Conclusion**: Established evidence supports HNRNPR as a bona fide spliceosome and hnRNP component that helps define the module's biological identity. Its repeated complex overlap with HNRNPL strengthens the interpretation of a known hnRNP core. Whether HNRNPR is functionally required for the shared heart-ovary co-abundance state is not established by these data.

#### SRSF7

- **Related proteins** (co-abundance neighbors): DHX9 (0.86); STRING partners: DHX9 (0.789), HNRNPL (0.926), HNRNPR (0.833)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine and arginine rich splicing factor 7. The protein encoded by this gene is a member of the serine/arginine (SR)-rich family of pre-mRNA splicing factors, which constitute part of the spliceosome. Each of these factors contains an N-terminal RNA recognition motif (RRM) for binding RNA and a C-terminal RS domain for binding other proteins. The RS domain is rich in serine and arginine residues and facilitates interaction between different…
- **Diseases (Open Targets)**: neurodegenerative disease (0.536); dengue disease (0.370); cystitis (0.221); smoking initiation (0.107); neoplasm (0.082)
- **Europe PMC papers**: 1327
- **Why important**: SRSF7 is an SR-rich splicing factor with an RNA-recognition motif and an interaction-promoting RS domain. It connects to DHX9, HNRNPL, and HNRNPR in STRING and contributes to the globally significant spliceosome, mRNA-processing, RNA-splicing, and mRNA-regulation terms. Its established role in alternative splicing complements the hnRNP functions of the other core members. It also has a substantial literature base and disease associations involving neurodegenerative disease and other conditions.
- **Conclusion**: Established evidence supports SRSF7 as the module's canonical SR-family splicing regulator and a functional complement to the hnRNP proteins. Its network connections support coordinated RNA-binding and spliceosome biology. It is a plausible mediator of transcript-selective effects, but the fact sheet does not identify specific heart or ovary transcripts controlled by SRSF7.

