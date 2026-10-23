# Conserved co-abundance modules: brain and liver

## Module 0

**Tissue pair**: brain and liver  
**Genes (15)**: ORM1, ORM2, SERPINA3, APOD, BDH1, SERPINA6, CP, CFB, C3, C9, IGHA1, ITIH4, NIT2, BCKDHA, PTGR1

### Function

The strongest interpretation is a circulating acute inflammatory and innate-defense module. The primary evidence is enrichment for blood microparticles (GO:CC blood microparticle; q_global = 1.18e-05), acute inflammatory response (GO:BP acute inflammatory response; q_global = 0.00179), acute-phase response (GO:BP acute-phase response; q_global = 0.0132), alternative-pathway complement activation (GO:BP complement activation, alternative pathway; q_global = 0.0165), and defense response (GO:BP defense response; q_global = 0.047). C3, CFB, and C9 support complement activity, while ORM1, ORM2, ITIH4, and SERPINA3 support an acute-phase response. The network also contains a smaller metabolic branch involving NIT2, BDH1, and PTGR1, but no GO or KEGG primary term establishes that branch as the principal module function. Because the module is co-abundance based, these findings establish coordinated abundance rather than direct biochemical interaction among every member.

**Cell composition.** This is predominantly a secreted plasma-protein module with a strong liver signature. HPA identifies many secreted genes, frequent liver enrichment, and hepatocyte enrichment, while several members are also associated with astrocytes or other brain cell types. The blood-microparticle result (GO:CC blood microparticle; q_global = 1.18e-05) and STRING tissue enrichments for bone-marrow cells, plasma cells, and blood microparticles (4 supplementary STRING terms; within-query FDR 3.87e-08–1.96e-05) make a blood-derived or blood-contamination-related explanation important. The module is not uniformly immune-cell derived: some genes are immune-cell enriched, but several are not detected in immune cells, and the HPA profile also includes hepatocyte and neural-cell associations. Thus the shared brain-liver pattern may reflect circulating proteins, vascular or blood-microparticle signal, shared secretory biology, or a mixture of these rather than a single resident brain cell program.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 1.18e-05 | C3, C9, CFB, CP, IGHA1, ITIH4, ORM1, ORM2, SERPINA3 |
| GO:BP acute inflammatory response | 0.00179 | C3, ITIH4, ORM1, ORM2, SERPINA3 |
| GO:BP acute-phase response | 0.0132 | ITIH4, ORM1, ORM2, SERPINA3 |
| GO:BP complement activation, alternative pathway | 0.0165 | C3, C9, CFB |
| GO:BP defense response | 0.047 | APOD, C3, C9, CFB, IGHA1, ITIH4, ORM1, ORM2, SERPINA3 |

### STRING and hu.MAP

STRING supports a well-known extracellular plasma-protein network. The strongest relationship is between C3 and CFB, with additional relationships linking C3 to CP, ITIH4, ORM1, and ORM2, and linking CP, ORM1, ORM2, and SERPINA3. These relationships are concordant with complement and acute-phase biology, but STRING edges can represent functional or literature-supported association and do not by themselves prove a physical complex in this module. The module is represented repeatedly in hu.MAP complexes (hu.MAP huMAP3_09531.1) through (hu.MAP huMAP3_07701.1), especially the recurring group of CP, CFB, SERPINA3, C3, ORM1, ORM2, and ITIH4. Those complexes contain many additional plasma, complement, coagulation, and transport proteins, indicating that the module captures a recognizable plasma-protein neighborhood. IGHA1, NIT2, BDH1, PTGR1, APOD, C9, and SERPINA6 have little or no direct STRING or hu.MAP support within the reported evidence, so their co-abundance should not be interpreted as an established physical interaction.

**STRING interactions (score >= 0.7)**: 11 of 105 gene pairs: C3–CFB (0.999); C3–CP (0.751); C3–ITIH4 (0.745); C3–ORM1 (0.775); C3–ORM2 (0.772); CP–ORM1 (0.923); CP–ORM2 (0.908); CP–SERPINA3 (0.822); ORM1–ORM2 (0.999); ORM1–SERPINA3 (0.918); ORM2–SERPINA3 (0.903)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Bone marrow cell (FDR = 3.87e-08, 10 genes); TISSUES Plasma cell (FDR = 4.37e-07, 9 genes); PMID (2022) Effects of Omega-3 and Antioxidant Cocktail Supplement on Prolonged Bed Rest: Results from Serum Proteome and Sphingolipids Analysis. (FDR = 6.5e-06, 9 genes); PMID (2017) Lectins: an effective tool for screening of potential cancer biomarkers. (FDR = 6.93e-06, 8 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 1.05e-05, 10 genes); PMID (2022) Proteomic analysis identifies a signature of disease severity in the plasma of COVID-19 pneumonia patients associated to neutrophil, platelet and complement activation. (FDR = 1.67e-05, 9 genes); Component Blood microparticle (FDR = 1.85e-05, 8 genes); COMPARTMENTS Blood microparticle (FDR = 1.96e-05, 8 genes); Keyword Secreted (FDR = 2.72e-05, 10 genes); PMID (2016) Proteomics reveals the effects of sustained weight loss on the human plasma proteome. (FDR = 4.35e-05, 8 genes); Keyword Glycoprotein (FDR = 6.24e-05, 11 genes); PMID (2017) Identification of candidate diagnostic serum biomarkers for Kawasaki disease using proteomic analysis. (FDR = 7.52e-05, 7 genes); TISSUES Skeletal system (FDR = 0.00014, 11 genes); Keyword Signal (FDR = 0.00014, 10 genes); PMID (2013) Serum biomarkers identification by mass spectrometry in high-mortality tumors. (FDR = 0.00038, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09531.1 (CP, CFB, SERPINA3, C3, ORM1, ORM2, ITIH4; 7/47); huMAP3_10101.1 (CP, CFB, SERPINA3, C3, ORM1, ORM2, ITIH4; 7/49); huMAP3_15040.1 (CP, CFB, SERPINA3, C3, ORM1, ORM2, ITIH4; 7/64); huMAP3_10678.1 (CP, CFB, SERPINA3, C3, ORM1, ORM2, ITIH4; 7/71); huMAP3_08395.1 (CP, CFB, SERPINA3, C3, ORM1, ORM2; 6/43); huMAP3_07432.1 (CP, SERPINA3, C3, ORM1, ORM2; 5/18); huMAP3_07265.1 (CP, SERPINA3, ORM1, ORM2; 4/20); huMAP3_09434.1 (SERPINA3, C3, ORM1, ITIH4; 4/33); huMAP3_02242.1 (SERPINA3, C3, ORM1; 3/9); huMAP3_08796.1 (CFB, SERPINA6, ITIH4; 3/15); huMAP3_09832.1 (CFB, SERPINA6, ITIH4; 3/18); huMAP3_09273.1 (CP, CFB, ORM2; 3/28); huMAP3_02236.1 (CP, ORM2; 2/7); huMAP3_08700.1 (CP, ORM1; 2/11); huMAP3_08224.1 (SERPINA3, C3; 2/21); huMAP3_07701.1 (CFB, ORM2; 2/22)

### Novelty

The module should not be claimed as a wholly new biological system. Its dominant complement, acute-phase, blood-microparticle, and plasma-protein signals are already represented in STRING, hu.MAP, and the literature-linked STRING annotations. What may be distinctive is the particular co-abundance pattern shared by brain and liver, including the combination of the established plasma neighborhood with the metabolic branch involving NIT2, BDH1, and PTGR1 and the presence of neural-cell HPA associations. That pattern is a candidate context-specific observation, not proof of novelty: absence of an interaction from STRING or hu.MAP cannot establish that it is newly discovered, and the prominent liver and blood signals provide a plausible pre-existing explanation. Demonstrating novelty would require independent cohort replication, control for blood content and cell composition, and comparison with published brain-liver proteomic or co-abundance modules.

**Hypothesis.** Hypothesis: a liver-derived acute-phase secretory program enters the circulating plasma or blood-microparticle compartment and is consequently observed in both liver and brain samples. In this model, CFB and C3 coordinate alternative-pathway complement activity, C9 represents downstream membrane-attack capacity, and ORM1, ORM2, ITIH4, and SERPINA3 provide the accompanying acute-phase and protease-regulatory environment. CP may connect metal and oxidative-stress handling to this extracellular response, while APOD and the NIT2-BDH1-PTGR1 branch may reflect lipid, ketone, and inflammatory-metabolite context. The neural HPA associations could indicate genuine local contribution in selected brain cell types, but the current evidence cannot distinguish that possibility from exposure to circulating proteins or blood microparticles.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): CFB (0.88), CP (0.85); STRING partners: CFB (0.999), CP (0.751), ITIH4 (0.745), ORM1 (0.775), ORM2 (0.772)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_08395.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_02242.1, huMAP3_08224.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a central complement component and one of the clearest functional anchors of the module. It participates in the primary defense and complement terms (GO:CC blood microparticle; q_global = 1.18e-05), (GO:BP acute inflammatory response; q_global = 0.00179), (GO:BP complement activation, alternative pathway; q_global = 0.0165), and (GO:BP defense response; q_global = 0.047), connects to CFB and CP in STRING, and recurs across many hu.MAP complexes (hu.MAP huMAP3_09531.1) through (hu.MAP huMAP3_02242.1) and (hu.MAP huMAP3_08224.1). Its strong disease and literature support includes complement deficiency, complement-mediated renal disease, and macular degeneration associations.
- **Conclusion**: Established evidence supports C3 as a core complement and inflammatory marker of the module. It is plausible, but not established here, that C3 is a functional driver of the shared brain-liver co-abundance pattern rather than a highly abundant circulating correlate.

#### CFB

- **Related proteins** (co-abundance neighbors): C3 (0.88), SERPINA6 (0.88), ITIH4 (0.85), IGHA1 (0.80); STRING partners: C3 (0.999)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_08395.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_09273.1, huMAP3_07701.1
- **Function (MyGene.info)**: complement factor B. This gene encodes complement factor B, a component of the alternative pathway of complement activation. Factor B circulates in the blood as a single chain polypeptide. Upon activation of the alternative pathway, it is cleaved by complement factor D yielding the noncatalytic chain Ba and the catalytic subunit Bb. The active subunit Bb is a serine protease which associates with C3b to form the alter…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with B factor anomaly (0.764); atypical hemolytic-uremic syndrome (0.705); Immunodeficiency due to a complement cascade protein anomaly (0.614); paroxysmal nocturnal hemoglobinuria (0.561); complement 3 glomerulopathy (0.546)
- **Europe PMC papers**: 7226
- **Why important**: CFB has the strongest network connectivity in the reported module and is linked to C3 by a very strong STRING relationship. It is present in the complement and defense terms (GO:CC blood microparticle; q_global = 1.18e-05), (GO:BP complement activation, alternative pathway; q_global = 0.0165), and (GO:BP defense response; q_global = 0.047), and appears in multiple hu.MAP complexes (hu.MAP huMAP3_09531.1) through (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_08796.1) through (hu.MAP huMAP3_09273.1), and (hu.MAP huMAP3_07701.1). Its established role as the alternative-pathway factor that forms the C3 convertase makes it a mechanistically informative hub, with extensive complement-disease literature.
- **Conclusion**: Established evidence identifies CFB as a central alternative-complement component and a major network anchor. The data support coordinated complement biology, but do not demonstrate that CFB initiates the module in either tissue.

#### ORM1

- **Related proteins** (co-abundance neighbors): APOD (0.85); STRING partners: C3 (0.775), CP (0.923), ORM2 (0.999), SERPINA3 (0.918)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_08395.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_02242.1, huMAP3_08700.1
- **Function (MyGene.info)**: orosomucoid 1. This gene encodes a key acute phase plasma protein. Because of its increase due to acute inflammation, this protein is classified as an acute-phase reactant.  The specific function of this protein has not yet been determined; however, it may be involved in aspects of immunosuppression. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.102); nephronophthisis (0.088); familial idiopathic steroid-resistant nephrotic syndrome (0.087); colorectal carcinoma (0.083); breast cancer (0.083)
- **Europe PMC papers**: 2436
- **Why important**: ORM1 is a liver-enriched secreted acute-phase protein and has strong STRING relationships with CP, ORM2, SERPINA3, and C3. It occurs in the acute inflammatory, acute-phase, blood-microparticle, and defense terms (GO:CC blood microparticle; q_global = 1.18e-05), (GO:BP acute inflammatory response; q_global = 0.00179), (GO:BP acute-phase response; q_global = 0.0132), and (GO:BP defense response; q_global = 0.047), and in numerous hu.MAP complexes (hu.MAP huMAP3_09531.1) through (hu.MAP huMAP3_02242.1) and (hu.MAP huMAP3_08700.1). It has substantial literature and disease-association support for inflammatory and hepatic contexts.
- **Conclusion**: Established evidence supports ORM1 as a liver-derived acute-phase connector within the plasma network. Its precise causal role in the brain-liver relationship remains a hypothesis; co-abundance could instead reflect shared circulation or systemic inflammation.

#### ITIH4

- **Related proteins** (co-abundance neighbors): CFB (0.85), C9 (0.84), SERPINA3 (0.81), IGHA1 (0.81); STRING partners: C3 (0.745)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_09434.1, huMAP3_08796.1, huMAP3_09832.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 4. The protein encoded by this gene is secreted into the blood, where it is cleaved by plasma kallikrein into two smaller forms. Expression of this gene has been detected only in liver, and it seems to be upregulated during surgical trauma. This gene is part of a cluster of similar genes on chromosome 3. Two transcript variants encoding different isoforms have been found for this gene. [provided by R…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.466); coronary artery disorder (0.417); type 2 diabetes mellitus (0.397); osteoarthritis (0.387); diabetes mellitus (0.363)
- **Europe PMC papers**: 1710
- **Why important**: ITIH4 combines a high network position with liver enrichment, secretion to blood, and neural-cell associations in HPA. It contributes to blood microparticle, acute inflammatory, acute-phase, and defense terms (GO:CC blood microparticle; q_global = 1.18e-05), (GO:BP acute inflammatory response; q_global = 0.00179), (GO:BP acute-phase response; q_global = 0.0132), and (GO:BP defense response; q_global = 0.047), connects in STRING to CFB, C3, and SERPINA3, and appears in several hu.MAP complexes (hu.MAP huMAP3_09531.1) through (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_09434.1), (hu.MAP huMAP3_08796.1), and (hu.MAP huMAP3_09832.1). Its annotated acute-phase and hyaluronan-related biology, together with disease links involving metabolic and skeletal conditions, gives it a plausible extracellular regulatory role.
- **Conclusion**: Established evidence supports ITIH4 as a secreted acute-phase component that bridges complement-associated and extracellular-matrix-related plasma biology. A direct role in coordinating brain and liver responses is not established by this module.

#### CP

- **Related proteins** (co-abundance neighbors): C3 (0.85), ORM2 (0.82), SERPINA6 (0.80); STRING partners: C3 (0.751), ORM1 (0.923), ORM2 (0.908), SERPINA3 (0.822)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_08395.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09273.1, huMAP3_02236.1, huMAP3_08700.1
- **Function (MyGene.info)**: ceruloplasmin. The protein encoded by this gene is a metalloprotein that binds most of the copper in plasma and is involved in the peroxidation of Fe(II)transferrin to Fe(III) transferrin. Mutations in this gene cause aceruloplasminemia, which results in iron accumulation and tissue damage, and is associated with diabetes and neurologic abnormalities. Two transcript variants, one protein-coding and the other not…
- **Diseases (Open Targets)**: aceruloplasminemia (0.827); cerebellar ataxia (0.572); Hermansky-Pudlak syndrome 3 (0.564); Hermansky-Pudlak syndrome (0.543); neurodegeneration with brain iron accumulation (0.510)
- **Europe PMC papers**: 171928
- **Why important**: CP is a liver-enriched secreted plasma protein with a prominent STRING neighborhood involving C3, ORM1, ORM2, and SERPINA3. It contributes to the blood-microparticle term (GO:CC blood microparticle; q_global = 1.18e-05) and appears across many hu.MAP complexes (hu.MAP huMAP3_09531.1) through (hu.MAP huMAP3_07265.1), (hu.MAP huMAP3_09273.1), (hu.MAP huMAP3_02236.1), and (hu.MAP huMAP3_08700.1). Its established copper and iron handling functions, oxidant-detoxification annotation, aceruloplasminemia association, and very large literature base make it especially relevant to links between inflammation, metal handling, and neurological disease.
- **Conclusion**: Established evidence supports CP as a secreted metal- and redox-related component embedded in the acute-phase plasma neighborhood. The possibility that it connects inflammatory and oxidative stress biology across brain and liver is a reasonable hypothesis, not a demonstrated mechanism.

#### SERPINA3

- **Related proteins** (co-abundance neighbors): IGHA1 (0.83), ITIH4 (0.81); STRING partners: CP (0.822), ORM1 (0.918), ORM2 (0.903)
- **HPA**: Group enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in brain, liver
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_08395.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_02242.1, huMAP3_08224.1
- **Function (MyGene.info)**: serpin family A member 3. The protein encoded by this gene is a member of the serpin family of proteins, a group of proteins that inhibit serine proteases. This gene is one in a cluster of serpin genes located on the q arm of chromosome 14. Polymorphisms in this protein appear to be tissue specific and influence protease targeting. Variations in this protein's sequence have been implicated in Alzheimer's disease, and defic…
- **Diseases (Open Targets)**: prostate carcinoma (0.359); chronic kidney disease (0.217); peripheral arterial occlusive disease 1 (0.118); central nervous system cancer (0.118); glioma (0.105)
- **Europe PMC papers**: 5458
- **Why important**: SERPINA3 is a secreted acute-phase serpin with liver and astrocyte associations in HPA. It occurs in the blood-microparticle, inflammatory, acute-phase, and defense terms (GO:CC blood microparticle; q_global = 1.18e-05), (GO:BP acute inflammatory response; q_global = 0.00179), (GO:BP acute-phase response; q_global = 0.0132), and (GO:BP defense response; q_global = 0.047), has STRING relationships with CP, ORM1, and ORM2, and is repeatedly represented in hu.MAP complexes (hu.MAP huMAP3_09531.1) through (hu.MAP huMAP3_02242.1) and (hu.MAP huMAP3_08224.1). Its serine-protease inhibitory function and reported links to Alzheimer disease and liver disease make it particularly relevant to the brain-liver interpretation.
- **Conclusion**: Established evidence supports SERPINA3 as an acute-phase protease-regulatory component shared by the plasma and neural contexts. Its association with neurodegenerative disease does not establish that this module causes neurological pathology; that is only a hypothesis requiring targeted study.

## Module 1

**Tissue pair**: brain and liver  
**Genes (22)**: ABCD3, ABCF1, CNN3, DAZAP1, EIF3L, EPB42, EPS8L2, FLNA, FLNB, G6PD, COLGALT1, NSUN2, NUP205, P4HA1, PPP4C, PPM1G, PSMG1, RCC1, SRP54, SRP68, TXLNA, XRN2

### Function

The module does not have a statistically supported GO or KEGG function: no GO/KEGG term passed global correction. Its genes nevertheless suggest a heterogeneous cellular maintenance program rather than a single canonical pathway. The strongest functional themes suggested by individual annotations are cytoskeletal organization and cell adhesion through CNN3, FLNA and FLNB; RNA modification, RNA processing and nuclear RNA handling through NSUN2 and XRN2; translation and protein targeting through EIF3L, SRP54 and SRP68; proteasome assembly through PSMG1; redox and pentose-phosphate metabolism through G6PD; and lipid handling through ABCD3. These annotations are mechanistic clues, not enrichment evidence. The co-abundance structure may therefore represent coordinated expression of broadly required cellular processes, with additional contributions from cell structure, protein synthesis, metabolism and extracellular-matrix handling.

**Cell composition.** This is not predominantly a secreted or plasma-protein module. Most genes have low tissue specificity, and protein detection is common in both brain and liver, supporting a broadly expressed cellular component rather than a tissue-exclusive program. The module is also not strongly blood-cell specific overall, although selected genes show blood or hematopoietic associations: G6PD is enhanced in eosinophils, COLGALT1 is associated with monocyte and myeloid populations, and EPB42 is enriched in erythrocyte-related cells. HPA results also point to several non-brain and non-liver cell populations, including esophageal cells, germ-cell populations, trophoblasts and stromal or vascular cells. Thus, shared abundance could partly reflect ubiquitous housekeeping functions, shared vascular or stromal components, blood contamination, or cell-composition variation. ABCD3 is liver-enhanced, while PPM1G and PSMG1 are testis-enhanced; these observations argue against interpreting the module as a uniform brain-liver-specific program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING evidence supports only two high-confidence known relationships within the module: FLNA with FLNB, and SRP54 with SRP68. These links are biologically coherent with actin-cytoskeleton organization and signal-recognition-particle function, respectively. No STRING functional-enrichment result was returned, so the STRING evidence does not establish a broader pathway. No hu.MAP complex contains multiple module members. The remaining co-abundance edges are therefore not independently supported here as physical protein interactions or membership in a known multiprotein complex. The module should be interpreted primarily as a coordinated abundance pattern, with two embedded known interaction pairs rather than as one established molecular complex.

**STRING interactions (score >= 0.7)**: 2 of 231 gene pairs: FLNA–FLNB (0.979); SRP54–SRP68 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be novel as a brain-liver co-abundance pattern, but the fact sheet does not establish a new molecular mechanism or a new physical complex. The absence of a matching hu.MAP complex and the limited STRING connectivity indicate that most relationships are not recognized here as established protein interactions. That absence alone does not prove novelty, because co-abundance can capture shared regulation, cell composition, protein turnover or indirect pathway coupling. Novelty is therefore best stated cautiously: the cross-tissue module configuration appears potentially new, whereas several of its component functions and two of its relationships are already well established. Independent replication, control for cell composition and comparison with published co-expression modules would be needed to claim a genuinely new biological discovery.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-maintenance state present in brain and liver that couples cytoskeletal and membrane organization with biosynthetic quality control. In this model, CNN3, FLNA and FLNB support actin-associated structural organization; SRP54 and SRP68 support cotranslational targeting of selected proteins to the endoplasmic reticulum; EIF3L and ABCF1 support translation-related activity; NSUN2 and XRN2 support RNA maturation and processing; PSMG1 supports proteasome assembly; G6PD supplies reducing power for protection from oxidative stress; and ABCD3 supports peroxisomal lipid handling. The observed pattern could arise from coordinated regulation in common resident cell types or from shared vascular, stromal or blood-related contributions rather than from direct physical interaction among all module members. This is a testable hypothesis, not an enriched-pathway conclusion.

### Important genes

#### CNN3

- **Related proteins** (co-abundance neighbors): PSMG1 (0.86), SRP54 (0.84), TXLNA (0.84), PPM1G (0.82), G6PD (0.82), PPP4C (0.81), NSUN2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calponin 3. This gene encodes a protein with a markedly acidic C terminus; the basic N-terminus is highly homologous to the N-terminus of a related gene, CNN1. Members of the CNN gene family all contain similar tandemly repeated motifs. This encoded protein is associated with the cytoskeleton but is not involved in contraction. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.492); pleural empyema (0.256); pneumothorax (0.256); biliary tract disorder (0.247); tooth disorder (0.196)
- **Europe PMC papers**: 1628
- **Why important**: CNN3 is the most connected hub described in the module and links genes associated with proteasome assembly, signal-recognition-particle function, cytoskeletal regulation, RNA processing, metabolism and phosphatase activity. Its annotation supports actin filament and actomyosin organization, epithelial differentiation and cell-cell adhesion. It is detected in brain and liver and has substantial literature, while its disease associations include neurodegenerative disease and several tissue-injury or structural disorders. Its central network position makes it a useful candidate for testing whether the module has a structural-cellular component.
- **Conclusion**: Established evidence supports CNN3 as a broadly detected actin-associated protein with a central position in this co-abundance network. It is plausible, but not demonstrated, that CNN3 helps organize the shared module through cytoskeletal or adhesion-related cell-state regulation.

#### NSUN2

- **Related proteins** (co-abundance neighbors): XRN2 (0.83), RCC1 (0.82), ABCF1 (0.81), CNN3 (0.80), TXLNA (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP2/Sun RNA methyltransferase 2. This gene encodes a methyltransferase that catalyzes the methylation of cytosine to 5-methylcytosine (m5C) at position 34 of intron-containing tRNA(Leu)(CAA) precursors. This modification is necessary to stabilize the anticodon-codon pairing and correctly translate the mRNA. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Mar…
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.694); hereditary disease (0.518); Intellectual disability (0.489); phenylketonuria (0.470); neurodegenerative disease (0.462)
- **Europe PMC papers**: 2458
- **Why important**: NSUN2 is a highly connected module member linking RNA processing and modification with translation-related and nuclear transport-associated genes. Its established functions include tRNA cytosine methylation, tRNA modification, rRNA processing, mRNA processing and regulation of mRNA export. It is detected in both brain and liver, has extensive literature and is associated with intellectual disability and neurodegenerative disease in the supplied evidence. It provides a strong candidate for a post-transcriptional regulatory axis within the module.
- **Conclusion**: Established evidence supports NSUN2 as an RNA-modification and RNA-processing enzyme with broad cellular relevance. Its participation in the shared module may indicate coordinated RNA and translation control, but the co-abundance data do not prove that NSUN2 regulates the other module genes.

#### G6PD

- **Related proteins** (co-abundance neighbors): SRP54 (0.84), PPM1G (0.82), CNN3 (0.82), PSMG1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glucose-6-phosphate dehydrogenase. This gene encodes glucose-6-phosphate dehydrogenase. This protein is a cytosolic enzyme encoded by a housekeeping X-linked gene whose main function is to produce NADPH, a key electron donor in the defense against oxidizing agents and in reductive biosynthetic reactions. G6PD is remarkable for its genetic diversity. Many variants of G6PD, mostly produced from missense mutations, have been described…
- **Diseases (Open Targets)**: anemia, nonspherocytic hemolytic, due to G6PD deficiency (0.851); anemia (phenotype) (0.776); G6PD deficiency (0.686); hereditary disease (0.535); infection (0.488)
- **Europe PMC papers**: 16994
- **Why important**: G6PD is centrally connected to several module members and provides a direct metabolic interpretation. Its established function is production of NADPH through the pentose-phosphate pathway, supporting antioxidant defense and reductive biosynthesis. It is detected in brain and liver, has very extensive literature, and has strong disease associations with G6PD deficiency and hemolytic anemia. Its eosinophil-enhanced HPA profile also makes blood-cell contribution a relevant alternative explanation.
- **Conclusion**: Established evidence supports G6PD as a redox and metabolic component of the module. A role for oxidative-stress buffering in the shared brain-liver signal is a reasonable hypothesis, but the module does not establish that redox metabolism is its dominant function or that G6PD drives the co-abundance pattern.

#### SRP54

- **Related proteins** (co-abundance neighbors): G6PD (0.84), CNN3 (0.84); STRING partners: SRP68 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal recognition particle 54. Enables several functions, including 7S RNA binding activity; endoplasmic reticulum signal peptide binding activity; and guanyl ribonucleotide binding activity. Contributes to GTPase activity. Involved in granulocyte differentiation and protein targeting to ER. Located in cytosol and nucleus. Part of signal recognition particle, endoplasmic reticulum targeting. Implicated in severe congenital neut…
- **Diseases (Open Targets)**: neutropenia, severe congenital, 8, autosomal dominant (0.758); neurodegenerative disease (0.536); Shwachman-Diamond syndrome 1 (0.453); Abnormality of the skeletal system (0.380); hereditary disease (0.375)
- **Europe PMC papers**: 1519
- **Why important**: SRP54 is part of the only explicitly supported signal-recognition-particle pair in the module, with a high-confidence STRING relationship to SRP68. Its established functions include signal-peptide recognition, cotranslational protein targeting to the endoplasmic reticulum, granulocyte differentiation and protein targeting. It is detected in brain and liver and is linked to severe congenital neutropenia and related hereditary disease. Its direct STRING relationship gives it stronger interaction support than most module genes.
- **Conclusion**: Established evidence supports SRP54 as an endoplasmic-reticulum targeting factor and supports its relationship with SRP68. The module may include a protein-trafficking component, but the broader network does not show enough independent interaction evidence to conclude that all module members form an SRP-centered complex.

#### ABCD3

- **Related proteins** (co-abundance neighbors): EIF3L (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Peroxisomes; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP binding cassette subfamily D member 3. The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the ALD subfamily, which is involved in peroxisomal import of fatty acids and/…
- **Diseases (Open Targets)**: congenital bile acid synthesis defect 5 (0.454); oculopharyngodistal myopathy (0.380); Abnormality of the skeletal system (0.359); food allergy (0.097); colorectal carcinoma (0.097)
- **Europe PMC papers**: 1205
- **Why important**: ABCD3 is connected to EIF3L and is the clearest liver-associated metabolic member in the supplied HPA evidence. Its established function is peroxisomal import related to fatty-acid and fatty-acyl-CoA handling, including very-long-chain fatty-acid metabolism, beta-oxidation, bile-acid biosynthesis and lipid transport. It is detected in both brain and liver and has disease associations involving bile-acid synthesis and neuromuscular phenotypes. It helps connect the shared module to organelle and lipid metabolism without implying that the whole module is liver-specific.
- **Conclusion**: Established evidence supports ABCD3 as a peroxisomal lipid-handling protein with liver-enhanced expression. Its presence may indicate a metabolic contribution to the module, but it does not establish that peroxisomal lipid metabolism explains the complete brain-liver co-abundance pattern.

## Module 2

**Tissue pair**: brain and liver  
**Genes (18)**: ACLY, FLII, IQGAP1, MYG1, NUP160, RECQL, SF3B3, MARS1, QARS1, RARS1, TARS1, TLN1, VCL, WDR1, XPO1, CSE1L, XRCC6, ZW10

### Function

The module is best interpreted as a conserved intracellular maintenance program involving nucleic-acid handling, translation, nuclear transport, genome maintenance, and cytoskeletal organization. The primary GO evidence is enrichment for membraneless organelles in (GO:CC membraneless organelle; q_global = 0.0205) and (GO:CC intracellular membraneless organelle; q_global = 0.0205), together with catalytic activity acting on nucleic acid in (GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.0217). This does not identify one narrowly defined pathway; instead, the network contains several connected functional neighborhoods. QARS1, MARS1, RARS1 and TARS1 form an aminoacyl-tRNA synthetase neighborhood. XPO1, CSE1L and NUP160 represent nuclear transport. RECQL and XRCC6 represent DNA repair and genome maintenance. TLN1, VCL, IQGAP1 and WDR1 represent adhesion and actin organization. The lack of STRING functional enrichment does not invalidate the module, because the globally corrected GO evidence supports a broad cellular organization program rather than necessarily a single canonical pathway.

**Cell composition.** The module is not composed predominantly of plasma or secreted proteins: HPA reports no secreted genes. Most genes have low tissue specificity, and protein detection is broadly compatible with both brain and liver, supporting a shared intracellular program rather than a tissue-exclusive signature. HPA reports low immune-cell specificity for the module, so there is no strong evidence that it is simply a blood-cell contamination signal. Nevertheless, several genes show cell-type-enhanced or group-enriched patterns involving megakaryocytes, platelets, neutrophils, spermatogenic cells, and neural cell types. TLN1 and VCL are compatible with vascular, platelet, and adhesion-related material, whereas MYG1 and NUP160 have neural cell-type associations. Shared cellular composition, vascular material, platelet-associated material, or other cell-mixture effects could therefore contribute to the co-abundance pattern. The evidence does not support classifying this as a plasma-protein module.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC membraneless organelle | 0.0205 | ACLY, FLII, IQGAP1, MARS1, MYG1, NUP160, RARS1, RECQL, SF3B3, TLN1, VCL, WDR1, XPO1, XRCC6, ZW10 |
| GO:CC intracellular membraneless organelle | 0.0205 | ACLY, FLII, IQGAP1, MARS1, MYG1, NUP160, RARS1, RECQL, SF3B3, TLN1, VCL, WDR1, XPO1, XRCC6, ZW10 |
| GO:MF catalytic activity, acting on a nucleic acid | 0.0217 | MARS1, MYG1, QARS1, RARS1, RECQL, TARS1, XRCC6 |

### STRING and hu.MAP

STRING supports specific internal relationships rather than enrichment of one overall pathway. The aminoacyl-tRNA synthetase relationships among MARS1, QARS1, RARS1 and TARS1 are strongly supported. STRING also supports TLN1 with VCL, IQGAP1 and WDR1, RECQL with XRCC6, and XPO1 with CSE1L and NUP160. These relationships support genuine molecular subnetworks within the co-abundance module. hu.MAP independently supports the aminoacyl-tRNA synthetase group through (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), the XPO1-CSE1L association through (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1) and (hu.MAP huMAP3_09592.1), RECQL with TLN1 through (hu.MAP huMAP3_14982.1), and ZW10 with NUP160 through (hu.MAP huMAP3_11232.1). Because these complexes contain only subsets of the module, the module is better viewed as a composite of several known assemblies than as one intact complex. XRCC6, FLII, IQGAP1, VCL, WDR1, SF3B3, ACLY and MYG1 lack corresponding hu.MAP evidence in the supplied results, so their co-abundance relationships should be interpreted more cautiously.

**STRING interactions (score >= 0.7)**: 12 of 153 gene pairs: CSE1L–XPO1 (0.976); IQGAP1–TLN1 (0.893); MARS1–QARS1 (0.999); MARS1–RARS1 (0.999); MARS1–TARS1 (0.881); NUP160–XPO1 (0.708); QARS1–RARS1 (0.999); QARS1–TARS1 (0.807); RARS1–TARS1 (0.806); RECQL–XRCC6 (0.898); TLN1–VCL (0.999); TLN1–WDR1 (0.744)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (TARS1, QARS1, RARS1, MARS1; 4/14); huMAP3_13688.1 (TARS1, QARS1, RARS1, MARS1; 4/14); huMAP3_07170.1 (XPO1, CSE1L; 2/14); huMAP3_09042.1 (XPO1, CSE1L; 2/26); huMAP3_14982.1 (RECQL, TLN1; 2/28); huMAP3_06791.1 (XPO1, CSE1L; 2/31); huMAP3_11232.1 (ZW10, NUP160; 2/78); huMAP3_09592.1 (XPO1, CSE1L; 2/95)

### Novelty

The module is unlikely to represent a wholly new molecular system because several internal relationships are already documented by STRING and hu.MAP, particularly the aminoacyl-tRNA synthetase group, the XPO1-CSE1L transport relationship, the RECQL-XRCC6 repair relationship, and the TLN1-VCL cytoskeletal relationship. Its possible novelty is instead at the systems level: the conserved association of translation, nucleic-acid processing, nuclear transport, genome maintenance, and cytoskeletal organization across brain and liver. Absence from STRING or hu.MAP alone does not establish novelty. A claim of new biology would require comparison with independent tissue co-abundance datasets, prior module definitions, and experiments showing that the cross-subnetwork association is reproducible and biologically regulated rather than caused by cell composition or technical effects.

**Hypothesis.** Hypothesis: the module represents a conserved cellular maintenance state in which protein synthesis and RNA processing are coordinated with nuclear-cytoplasmic transport, DNA surveillance, and cytoskeletal remodeling. The aminoacyl-tRNA synthetase neighborhood may reflect translational demand, while XPO1, CSE1L and NUP160 may coordinate movement of RNA and proteins through the nuclear envelope. RECQL and XRCC6 may provide genome-integrity functions, and the TLN1-VCL-IQGAP1-WDR1 neighborhood may connect the intracellular state to adhesion and actin dynamics. A shared metabolic or stress-responsive state in brain and liver could generate this co-abundance pattern. This mechanistic coupling remains hypothetical, and vascular, platelet-associated, neural, or other cell-composition effects should be excluded experimentally.

### Important genes

#### QARS1

- **Related proteins** (co-abundance neighbors): TARS1 (0.85), RARS1 (0.83), MYG1 (0.83), XPO1 (0.82), FLII (0.80); STRING partners: MARS1 (0.999), RARS1 (0.999), TARS1 (0.807)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutaminyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. In metazoans, 9 aminoacyl-tRNA synthetases specific for glutamine (gln), glutamic acid (glu), and 7 other amino …
- **Diseases (Open Targets)**: diffuse cerebral and cerebellar atrophy - intractable seizures - progressive microcephaly syndrome (0.794); hereditary disease (0.415); intellectual disability, autosomal dominant 43 (0.340); microcephaly (0.298); attention deficit-hyperactivity disorder (0.111)
- **Europe PMC papers**: 253
- **Why important**: QARS1 is a highly connected module gene linking TARS1, RARS1, MYG1, XPO1 and FLII. It belongs to the aminoacyl-tRNA synthetase group supported by (GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.0217), STRING, and hu.MAP (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Its established function is glutaminyl-tRNA aminoacylation and participation in protein translation. It has a substantial literature base and disease associations involving progressive microcephaly, seizures, and cerebral or cerebellar atrophy, making it relevant to a module conserved in brain and liver.
- **Conclusion**: Established evidence supports QARS1 as a translational component and as a bridge between the aminoacyl-tRNA synthetase neighborhood and other module branches. Its possible coordination of translation with nuclear transport or cytoskeletal state is a hypothesis based on network position, not an established function of this module.

#### XPO1

- **Related proteins** (co-abundance neighbors): XRCC6 (0.84), SF3B3 (0.83), QARS1 (0.82), TARS1 (0.82), ACLY (0.80); STRING partners: CSE1L (0.976), NUP160 (0.708)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_07170.1, huMAP3_09042.1, huMAP3_06791.1, huMAP3_09592.1
- **Function (MyGene.info)**: exportin 1. This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSe…
- **Diseases (Open Targets)**: plasma cell myeloma (0.642); B-cell chronic lymphocytic leukemia (0.626); diffuse large B-cell lymphoma (0.602); HIV infectious disease (0.561); neurodegenerative disease (0.522)
- **Europe PMC papers**: 5357
- **Why important**: XPO1 is a highly connected network hub linking XRCC6, SF3B3, QARS1, TARS1 and ACLY. It is supported by (GO:CC membraneless organelle; q_global = 0.0205) and (GO:CC intracellular membraneless organelle; q_global = 0.0205), STRING relationships with CSE1L and NUP160, and hu.MAP complexes (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1) and (hu.MAP huMAP3_09592.1). Its established function is export of proteins and RNA from the nucleus, including ribosomal subunits and messenger RNA. It has a large literature base and disease associations involving hematologic malignancy, viral infection, and neurodegenerative disease.
- **Conclusion**: Established evidence identifies XPO1 as a major nuclear-transport component capable of connecting translation, RNA processing, and genome maintenance. Its role as the causal organizer of the whole module remains hypothetical because co-abundance and database interactions do not establish directionality or causation.

#### RECQL

- **Related proteins** (co-abundance neighbors): FLII (0.84), RARS1 (0.83), ZW10 (0.81); STRING partners: XRCC6 (0.898)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, liver
- **hu.MAP 3.0**: huMAP3_14982.1
- **Function (MyGene.info)**: RecQ like helicase. The protein encoded by this gene is a member of the RecQ DNA helicase family. DNA helicases are enzymes involved in various types of DNA repair, including mismatch repair, nucleotide excision repair and direct repair. The encoded protein is involved in the processing of Holliday junctions, the suppression of sister chromatid exchanges, telomere maintenance, and is required for genotoxic stress res…
- **Diseases (Open Targets)**: RECON progeroid syndrome (0.595); hereditary neoplastic syndrome (0.505); obesity disorder (0.404); myofibrillar myopathy 8 (0.334); hereditary breast ovarian cancer syndrome (0.328)
- **Europe PMC papers**: 954
- **Why important**: RECQL connects FLII, RARS1 and ZW10 in the module and contributes to all primary terms (GO:CC membraneless organelle; q_global = 0.0205), (GO:CC intracellular membraneless organelle; q_global = 0.0205) and (GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.0217). STRING supports its relationship with XRCC6, while hu.MAP supports a complex containing RECQL and TLN1 through (hu.MAP huMAP3_14982.1). Its established function is a RecQ-family helicase involved in DNA repair, replication-fork processing, recombination, and telomere maintenance. It has substantial literature and disease associations involving a progeroid syndrome and hereditary neoplastic disorders.
- **Conclusion**: Established evidence supports RECQL as the principal genome-maintenance representative in the module and as a bridge between repair-related and other neighborhoods. A coordinated response linking DNA integrity with translation and cytoskeletal remodeling is a mechanistic hypothesis rather than a demonstrated module function.

#### TLN1

- **Related proteins** (co-abundance neighbors): VCL (0.83), IQGAP1 (0.82); STRING partners: IQGAP1 (0.893), VCL (0.999), WDR1 (0.744)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: huMAP3_14982.1
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 connects VCL and IQGAP1 and is supported by (GO:CC membraneless organelle; q_global = 0.0205) and (GO:CC intracellular membraneless organelle; q_global = 0.0205), strong STRING relationships with VCL, IQGAP1 and WDR1, and hu.MAP support through (hu.MAP huMAP3_14982.1). Its established function includes integrin activation, cell adhesion, and actin-cytoskeleton organization. HPA associates it with blood vessels and with megakaryocyte or platelet groups. Its disease associations include cardiomyopathy and developmental syndromes, and it has a substantial literature base.
- **Conclusion**: Established evidence supports TLN1 as the main structural and adhesion component of the module. Its HPA pattern raises the possibility that vascular or platelet-related cellular composition contributes to the signal. A direct regulatory connection between TLN1-dependent adhesion and the nuclear or translational neighborhoods remains hypothetical.

#### MARS1

- **Related proteins** (co-abundance neighbors): MYG1 (0.83); STRING partners: QARS1 (0.999), RARS1 (0.999), TARS1 (0.881)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: methionyl-tRNA synthetase 1. This gene encodes a member of the class I family of aminoacyl-tRNA synthetases. These enzymes play a critical role in protein biosynthesis by charging tRNAs with their cognate amino acids. The encoded protein is a component of the multi-tRNA synthetase complex and catalyzes the ligation of methionine to tRNA molecules. [provided by RefSeq, Jan 2011].
- **Diseases (Open Targets)**: severe early-onset pulmonary alveolar proteinosis due to MARS deficiency (0.745); Charcot-Marie-Tooth disease axonal type 2U (0.676); autosomal recessive spastic paraplegia type 70 (0.614); trichothiodystrophy 9, nonphotosensitive (0.428); pulmonary alveolar proteinosis (0.338)
- **Europe PMC papers**: 435
- **Why important**: MARS1 belongs to the tightly supported aminoacyl-tRNA synthetase group with QARS1, RARS1 and TARS1 in STRING and hu.MAP (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). It contributes to (GO:CC membraneless organelle; q_global = 0.0205), (GO:CC intracellular membraneless organelle; q_global = 0.0205) and (GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.0217). Its established function is methionyl-tRNA aminoacylation within the multi-tRNA synthetase complex. It has disease associations involving severe early-onset pulmonary alveolar proteinosis, axonal Charcot-Marie-Tooth disease, and spastic paraplegia, together with a meaningful literature base.
- **Conclusion**: Established evidence supports MARS1 as a core translational component and marker of the protein-synthesis neighborhood. Its co-abundance with nuclear transport, genome-maintenance, and cytoskeletal genes may reflect a shared cellular demand state, but a direct MARS1-mediated mechanism is not established.

## Module 3

**Tissue pair**: brain and liver  
**Genes (5)**: ACY1, BBOX1, FAH, IVD, SUCLG2

### Function

The module is most consistent with a tissue-linked metabolic program centered on hepatic and hepatocyte-associated metabolism. Its genes encode activities in carnitine biosynthesis (BBOX1), branched-chain amino-acid and leucine catabolism (IVD), aromatic-amino-acid and tyrosine catabolism (FAH), amino-acid salvage and catabolism (ACY1), and succinyl-CoA metabolism within the tricarboxylic-acid cycle (SUCLG2). BBOX1 is the central co-abundance node and connects each of the other genes, while the remaining genes are peripheral to that hub. This network structure suggests coordinated regulation of several metabolic processes rather than a demonstrated physical complex. No GO/KEGG term passed global correction, so the pathway interpretation is based on the individual gene functions and network organization, not on statistically significant enrichment. The absence of a globally enriched term does not invalidate the module.

**Cell composition.** The module is strongly liver-oriented by HPA evidence: liver enrichment or enhancement is present for most genes, and hepatocytes are the most recurrent single-cell annotation. ACY1 also has intestine-associated expression, while BBOX1 has kidney-associated enrichment and IVD has low tissue specificity. All genes are detected in liver, and most are detected in the surveyed brain regions, which is compatible with a shared metabolic program but does not establish brain-specific biology. None of the genes is annotated as secreted, so this is not predominantly a plasma or secreted-protein module. Immune-cell specificity is generally low or absent, although FAH has an immune-cell-enhanced annotation involving basophils and several blood-related cell annotations. Overall, shared hepatocyte or broader tissue-composition effects are plausible explanations for the brain–liver co-abundance pattern and should be considered alongside a true conserved metabolic program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no supplied high-confidence STRING interactions among the module genes, no STRING functional-enrichment result, and no hu.MAP complex containing multiple module members. Thus, the co-abundance relationships are not corroborated here as established protein–protein interactions or membership in a known multigene complex. The biochemical functions of the individual proteins are established in the supplied annotations, but the coordinated relationship among them remains a transcriptomic or abundance-level observation. BBOX1 is the network hub, whereas IVD, ACY1, FAH, and SUCLG2 each connect only to BBOX1; this supports a hub-centered co-regulation model more than a densely interconnected molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a novel co-abundance association linking carnitine production, amino-acid catabolism, tyrosine degradation, and succinyl-CoA metabolism across brain and liver, because the supplied resources do not report a matching STRING interaction network or hu.MAP complex. However, absence from those resources does not prove novelty: the module could reflect known metabolic co-regulation, shared hepatocyte-related composition, or correlated abundance of independently acting enzymes. The appropriate conclusion is that the cross-tissue co-abundance pattern is potentially novel, while a novel biochemical complex or pathway cannot be claimed from these data.

**Hypothesis.** Hypothesis: a conserved abundance program involving mitochondrial and cytosolic intermediary metabolism is shared between liver and brain, with BBOX1 acting as the principal co-regulated hub and the other enzymes representing complementary handling of carnitine precursors, branched-chain amino acids, aromatic amino acids, and succinyl-CoA. In liver, this signal may be driven substantially by hepatocyte abundance or state; in brain, it may reflect metabolic activity in cells that express BBOX1 and the other detected enzymes. This hypothesis predicts coordinated changes in the corresponding metabolites and should be tested with cell-resolved expression, protein abundance, and metabolomics rather than inferred as a physical complex.

### Important genes

#### BBOX1

- **Related proteins** (co-abundance neighbors): IVD (0.89), ACY1 (0.87), FAH (0.81), SUCLG2 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gamma-butyrobetaine hydroxylase 1. This gene encodes gamma butyrobetaine hydroxylase which catalyzes the formation of L-carnitine from gamma-butyrobetaine, the last step in the L-carnitine biosynthetic pathway. Carnitine is essential for the transport of activated fatty acids across the mitochondrial membrane during mitochondrial beta-oxidation. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.495); neurodegenerative disease (0.282); Abnormality of the gastrointestinal tract (0.275); hypothyroidism (0.133); thyroid cancer (0.132)
- **Europe PMC papers**: 708
- **Why important**: BBOX1 is the central network node, connecting every other module member, and is detected in both brain and liver. Its established function is the final step of carnitine biosynthesis, linking the module to transport of activated fatty acids for mitochondrial beta-oxidation. It has broad disease and phenotype associations in the supplied Open Targets evidence and substantial literature coverage, making it the strongest candidate for interpreting the module's network organization and metabolic relevance.
- **Conclusion**: Established evidence supports BBOX1 as the module hub and as a carnitine-biosynthesis enzyme expressed in both tissues. It is plausible, but not established, that BBOX1 coordinates the abundance of the other genes or connects their pathways through fatty-acid and mitochondrial metabolism.

#### IVD

- **Related proteins** (co-abundance neighbors): BBOX1 (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: isovaleryl-CoA dehydrogenase. Isovaleryl-CoA dehydrogenase (IVD) is a mitochondrial matrix enzyme that catalyzes the third step in leucine catabolism. The genetic deficiency of IVD results in an accumulation of isovaleric acid, which is toxic to the central nervous system and leads to isovaleric acidemia. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Aug 2017].
- **Diseases (Open Targets)**: isovaleric acidemia (0.848); hereditary disease (0.514); idiopathic pulmonary fibrosis (0.252); interstitial lung disease (0.159); postinflammatory pulmonary fibrosis (0.124)
- **Europe PMC papers**: 11719
- **Why important**: IVD contributes a distinct mitochondrial metabolic function: the third step of leucine and branched-chain amino-acid catabolism. It is connected to the BBOX1 hub and is detected in both brain and liver, with hepatocyte enhancement at the single-cell level. Its deficiency causes isovaleric acidemia with central nervous system toxicity, providing a strong disease link and direct relevance to the brain–liver metabolic context. The supplied literature coverage is particularly substantial.
- **Conclusion**: Established evidence supports IVD as a mitochondrial branched-chain-amino-acid catabolic enzyme with a clinically important metabolic phenotype. Its co-abundance with BBOX1 may indicate coordinated metabolic state, but the data do not establish a direct interaction or causal regulation.

#### FAH

- **Related proteins** (co-abundance neighbors): BBOX1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fumarylacetoacetate hydrolase. This gene encodes the last enzyme in the tyrosine catabolism pathway. FAH deficiency is associated with Type 1 hereditary tyrosinemia (HT). [provided by RefSeq, Jul 2008]
- **Diseases (Open Targets)**: tyrosinemia type I (0.854); tyrosinemia (0.520); hereditary disease (0.472); cholestasis (0.463); tyrosinemia type II (0.340)
- **Europe PMC papers**: 4622
- **Why important**: FAH is a liver-enhanced enzyme that catalyzes the final step of tyrosine catabolism and is connected to the BBOX1 hub. Its deficiency is associated with hereditary tyrosinemia, and its HPA annotations include hepatocytes as well as some blood-related cell categories. FAH therefore provides a strong liver-metabolism anchor and a well-established disease connection for the module.
- **Conclusion**: Established evidence supports FAH as a hepatic aromatic-amino-acid catabolic enzyme and as a marker of clinically important tyrosine-metabolism dysfunction. Its inclusion supports a liver-centered interpretation, while its relationship to BBOX1 remains a co-abundance association rather than a demonstrated molecular interaction.

#### ACY1

- **Related proteins** (co-abundance neighbors): BBOX1 (0.87); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Low immune cell specificity; location Vesicles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aminoacylase 1. This gene encodes a cytosolic, homodimeric, zinc-binding enzyme that catalyzes the hydrolysis of acylated L-amino acids to L-amino acids and an acyl group, and has been postulated to function in the catabolism and salvage of acylated amino acids. This gene is located on chromosome 3p21.1, a region reduced to homozygosity in small-cell lung cancer (SCLC), and its expression has been reported to be …
- **Diseases (Open Targets)**: aminoacylase 1 deficiency (0.810); Intellectual disability (0.466); hereditary disease (0.452); toxic encephalopathy (0.370); inborn aminoacylase deficiency (0.266)
- **Europe PMC papers**: 719
- **Why important**: ACY1 is connected to BBOX1 and encodes a cytosolic enzyme involved in hydrolysis and salvage of acylated amino acids. It is enriched in liver, intestine, colonocytes, and enterocytes, giving it a strong digestive-organ and amino-acid-metabolism signature. Its deficiency and associations with intellectual disability and toxic encephalopathy make it relevant to both metabolic and neurological interpretation.
- **Conclusion**: Established evidence supports ACY1 as an amino-acid salvage and catabolic enzyme with liver and intestinal cellular localization and disease relevance. Its presence may extend the module beyond hepatocytes toward shared amino-acid handling, but a mechanistic connection to BBOX1 is not established.

#### SUCLG2

- **Related proteins** (co-abundance neighbors): BBOX1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase GDP-forming subunit beta. This gene encodes a GTP-specific beta subunit of succinyl-CoA synthetase. Succinyl-CoA synthetase catalyzes the reversible reaction involving the formation of succinyl-CoA and succinate. Alternate splicing results in multiple transcript variants. Pseudogenes of this gene are found on chromosomes 5 and 12. [provided by RefSeq, Apr 2010].
- **Diseases (Open Targets)**: smoking initiation (0.377); breast disorder (0.325); vitamin B deficiency (0.318); alcohol drinking (0.314); duodenal ulcer (0.270)
- **Europe PMC papers**: 1184
- **Why important**: SUCLG2 is a mitochondrial component of succinyl-CoA synthetase and participates in the tricarboxylic-acid cycle and succinyl-CoA metabolism. It is liver-enhanced, enriched in hepatocytes, detected in both brain and liver, and connected to BBOX1 in the module graph. It provides the clearest link from the amino-acid catabolic enzymes to central mitochondrial carbon and energy metabolism.
- **Conclusion**: Established evidence supports SUCLG2 as a mitochondrial tricarboxylic-acid-cycle and succinyl-CoA metabolic enzyme with a liver-associated abundance pattern. Its co-abundance with BBOX1 is consistent with coordinated mitochondrial metabolism, but it remains a hypothesis that SUCLG2 functionally mediates the module.

## Module 4

**Tissue pair**: brain and liver  
**Genes (5)**: AGRN, DCTN1, EPS15L1, MAPRE2, RABGGTA

### Function

The strongest functional interpretation is a vesicle-trafficking, cytoskeletal, and neuromuscular-junction-related module. The primary evidence is the globally corrected enrichment for regulation of neuromuscular junction development (GO:BP regulation of neuromuscular junction development; q_global = 0.0182) and positive regulation of neuromuscular junction development (GO:BP positive regulation of neuromuscular junction development; q_global = 0.0182), both contributed by AGRN and DCTN1. The other genes support a coherent cellular context: RABGGTA is involved in Rab geranylgeranylation and endoplasmic-reticulum-to-Golgi transport; EPS15L1 in endocytosis and endosomal transport; MAPRE2 in microtubule organization; and DCTN1 in dynactin-dependent transport and nervous-system development. The enrichment is therefore biologically interpretable, but it should not be taken to establish a complete neuromuscular-junction pathway for every module member. No STRING functional-enrichment term was reported, and no additional GO or KEGG term should be treated as globally significant.

**Cell composition.** This does not resemble a plasma-protein, broadly secreted, or blood-cell-enriched module. Only AGRN is annotated as secreted, specifically to the extracellular matrix, while the remaining genes are non-secreted intracellular or vesicular proteins. HPA evidence indicates low immune-cell specificity for most genes and no immune-cell detection for AGRN, with no enriched blood-cell category. Protein was detected in brain for every gene and in liver for most genes, consistent with a shared biological signal rather than an obvious blood-contamination signature. The module is nevertheless heterogeneous in cellular context: HPA highlights myonuclei for several genes and kidney epithelial or podocyte populations for AGRN, while MAPRE2 is tissue-enhanced in brain and AGRN is tissue-enhanced in several kidney-related cell types. Thus, shared cell types, general cellular transport, or tissue-specific cellular composition could contribute to the brain-liver co-abundance pattern.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulation of neuromuscular junction development | 0.0182 | AGRN, DCTN1 |
| GO:BP positive regulation of neuromuscular junction development | 0.0182 | AGRN, DCTN1 |

### STRING and hu.MAP

The co-abundance graph is connected through RABGGTA, which is linked in the module to EPS15L1, MAPRE2, DCTN1, and AGRN. These edges are module-level co-abundance relationships, not established physical interactions. No module pair met the supplied high-confidence STRING interaction criterion, STRING functional enrichment was absent, and no hu.MAP complex contained multiple module members. Consequently, the network suggests coordinated abundance without external confirmation of a known protein complex. Established biological links remain plausible at the process level: RABGGTA participates in Rab modification and membrane traffic, EPS15L1 in endocytosis, MAPRE2 in microtubule dynamics, DCTN1 in dynein-dynactin transport, and AGRN in extracellular-matrix and neuromuscular-junction biology.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module is a potentially novel cross-tissue co-abundance pattern, but it cannot be called a definitively new biological discovery. The case for novelty is that the exact module has no reported high-confidence STRING interactions and no multi-member hu.MAP complex, while its members span membrane trafficking, microtubules, dynactin, and extracellular-matrix signaling. However, absence from those resources does not prove novelty: co-abundance can reflect shared regulation, cell composition, indirect pathway coupling, or technical structure, and the individual genes have established functions and disease associations. The most defensible conclusion is that the coordinated brain-liver module is under-supported by existing interaction resources and merits independent replication and validation.

**Hypothesis.** Hypothesis: this module reflects coordinated control of membrane and cargo trafficking with cytoskeletal transport, with RABGGTA acting as a central abundance correlate connecting vesicle-related EPS15L1, microtubule-associated MAPRE2, dynactin-associated DCTN1, and extracellular-matrix neuromuscular-junction factor AGRN. In brain, this could support neuronal or synaptic cargo movement and neuromuscular-junction-related organization; in liver, the same abundance program could reflect conserved intracellular trafficking or a shared specialized cell population rather than an actual neuromuscular junction. This hypothesis predicts that the co-abundance relationships should replicate across independent brain and liver cohorts and that perturbation or localization studies should reveal coordinated effects on vesicle transport, microtubule organization, or AGRN-associated signaling.

### Important genes

#### RABGGTA

- **Related proteins** (co-abundance neighbors): EPS15L1 (0.84), MAPRE2 (0.83), DCTN1 (0.82), AGRN (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rab geranylgeranyltransferase subunit alpha. Predicted to enable small GTPase binding activity. Predicted to contribute to Rab geranylgeranyltransferase activity. Predicted to be involved in protein geranylgeranylation. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.494); autoimmune disorder of central nervous system (0.319); primary familial polycythemia due to EPO receptor mutation (0.070); autosomal dominant severe congenital neutropenia (0.068); nonimmune chronic idiopathic neutropenia of adults (0.067)
- **Europe PMC papers**: 207
- **Why important**: RABGGTA is the network hub, connected to every other module member and therefore the strongest candidate for organizing the module-level signal. Its annotation places it in Rab geranylgeranylation and endoplasmic-reticulum-to-Golgi vesicle transport, providing a plausible bridge between EPS15L1, MAPRE2, DCTN1, and AGRN. It has disease links including neurodegenerative and central-nervous-system autoimmune associations, but its literature base is smaller than that of the other leading candidates.
- **Conclusion**: Established evidence supports RABGGTA as the central co-abundance correlate and as a Rab-modification and trafficking factor. It is a strong mechanistic candidate, but the network does not establish that RABGGTA directly regulates the other proteins. Its hub role should therefore be treated as a hypothesis requiring perturbation and physical or functional validation.

#### DCTN1

- **Related proteins** (co-abundance neighbors): RABGGTA (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynactin subunit 1. This gene encodes the largest subunit of dynactin, a macromolecular complex consisting of 10 subunits ranging in size from 22 to 150 kD. Dynactin binds to both microtubules and cytoplasmic dynein. Dynactin is involved in a diverse array of cellular functions, including ER-to-Golgi transport, the centripetal movement of lysosomes and endosomes, spindle formation, chromosome movement, nuclear positi…
- **Diseases (Open Targets)**: Perry syndrome (0.798); amyotrophic lateral sclerosis (0.764); neuronopathy, distal hereditary motor, type 7B (0.743); cancer (0.547); neurodegenerative disease (0.530)
- **Europe PMC papers**: 1985
- **Why important**: DCTN1 connects the module hub to dynactin-dependent microtubule transport and has the clearest direct link to the primary enrichment, contributing to both neuromuscular-junction terms (GO:BP regulation of neuromuscular junction development; q_global = 0.0182) and (GO:BP positive regulation of neuromuscular junction development; q_global = 0.0182). It is a component of a large dynein-associated transport complex and is annotated in axonogenesis, nervous-system development, organelle transport, and spindle functions. Its disease associations include Perry syndrome, amyotrophic lateral sclerosis, and hereditary motor neuronopathy, and it has extensive literature support.
- **Conclusion**: Established evidence supports DCTN1 as a biologically important transport and neuronal-development factor and as one of the two genes driving the globally significant enrichment. The module supports coordinated abundance with RABGGTA, but does not prove a direct interaction or a specific neuromuscular-junction mechanism in liver.

#### AGRN

- **Related proteins** (co-abundance neighbors): RABGGTA (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: agrin. This gene encodes one of several proteins that are critical in the development of the neuromuscular junction (NMJ), as identified in mouse knock-out studies. The encoded protein contains several laminin G, Kazal type serine protease inhibitor, and epidermal growth factor domains. Additional post-translational modifications occur to add glycosaminoglycans and disulfide bonds. In one family with con…
- **Diseases (Open Targets)**: congenital myasthenic syndrome 8 (0.793); congenital myasthenic syndrome (0.680); presynaptic congenital myasthenic syndrome (0.652); postsynaptic congenital myasthenic syndrome (0.626); COVID-19 (0.546)
- **Europe PMC papers**: 2731
- **Why important**: AGRN is the other gene contributing to both globally corrected neuromuscular-junction terms (GO:BP regulation of neuromuscular junction development; q_global = 0.0182) and (GO:BP positive regulation of neuromuscular junction development; q_global = 0.0182). It is a secreted extracellular-matrix protein with established roles in neuromuscular-junction development and synaptic signaling, and it is strongly linked to congenital myasthenic syndromes. Its high literature volume and disease relevance make it the most functionally specific marker of the module, while its connection to RABGGTA provides an unusual extracellular-to-intracellular association.
- **Conclusion**: Established evidence supports AGRN as a neuromuscular-junction and extracellular-matrix factor with clinically relevant loss-of-function biology. The co-abundance relationship with RABGGTA may indicate coordinated tissue or cell-state regulation, but a direct molecular connection is not established by the supplied STRING or hu.MAP evidence.

#### EPS15L1

- **Related proteins** (co-abundance neighbors): RABGGTA (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: epidermal growth factor receptor pathway substrate 15 like 1. Enables cadherin binding activity. Predicted to be involved in endocytosis and endosomal transport. Located in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: split hand-foot malformation (0.370); lysosomal storage disease (0.310); neurodegenerative disease (0.310); Alzheimer disease (0.310); Parkinson disease (0.310)
- **Europe PMC papers**: 426
- **Why important**: EPS15L1 is connected to the module hub and is annotated for endocytosis, endosomal transport, synaptic vesicle endocytosis, and cadherin binding. Its vesicular localization and disease associations involving neurodegenerative disease, Alzheimer disease, and Parkinson disease make it relevant to a trafficking-centered interpretation. Its literature support is substantial, although its functional contribution is less directly represented in the primary enrichment.
- **Conclusion**: Established evidence supports EPS15L1 as an endocytic and endosomal-transport factor compatible with the module's vesicle-trafficking interpretation. Its specific contribution to the brain-liver module and any connection to AGRN or DCTN1 remain hypotheses rather than demonstrated interactions.

#### MAPRE2

- **Related proteins** (co-abundance neighbors): RABGGTA (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: microtubule associated protein RP/EB family member 2. The protein encoded by this gene shares significant homology to the adenomatous polyposis coli (APC) protein-binding EB1 gene family. This protein is a microtubule-associated protein that is necessary for spindle symmetry during mitosis. It is thought to play a role in the tumorigenesis of colorectal cancers and the proliferative control of normal cells. Alternative splicing of this gene results i…
- **Diseases (Open Targets)**: multiple benign circumferential skin creases on limbs (0.746); skin creases, congenital symmetric circumferential, 2 (0.697); neurodegenerative disease (0.464); Brugada syndrome (0.388); developmental disability (0.340)
- **Europe PMC papers**: 475
- **Why important**: MAPRE2 is connected to RABGGTA and contributes a microtubule and cell-organization dimension. It is annotated in microtubule polymerization control, microtubule localization, spindle assembly, and focal-adhesion regulation, and it is tissue-enhanced in brain. Its disease associations include developmental and neurodegenerative conditions, with substantial literature support.
- **Conclusion**: Established evidence supports MAPRE2 as a microtubule-associated regulator that could complement vesicle and dynactin transport in the module. The brain-enhanced HPA pattern is compatible with a neural contribution, but the module data do not establish that MAPRE2 mediates the neuromuscular-junction enrichment or directly interacts with RABGGTA.

## Module 5

**Tissue pair**: brain and liver  
**Genes (18)**: ALDH4A1, ALDH2, BPHL, CRYL1, DMD, ETFDH, ABAT, GPD1, GSTM1, GYS1, ALAD, ALDH6A1, DBT, PCCA, PCCB, PPM1A, SEC14L2, TKFC

### Function

The module is most strongly characterized as a mitochondrial and cellular small-molecule catabolic program, with particular emphasis on branched-chain amino-acid, propanoate, organic-acid, and carboxylic-acid degradation. This conclusion is supported by the globally corrected terms for small-molecule catabolism (GO:BP small molecule catabolic process; q_global = 0.000879), valine/leucine/isoleucine degradation (KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 0.00276), organic-acid catabolism (GO:BP organic acid catabolic process; q_global = 0.00715), carboxylic-acid catabolism (GO:BP carboxylic acid catabolic process; q_global = 0.00715), propanoate metabolism (KEGG Propanoate metabolism - Homo sapiens (human); q_global = 0.00935), and branched-chain amino-acid metabolism (GO:BP branched-chain amino acid metabolic process; q_global = 0.0474). The module therefore appears to coordinate mitochondrial disposal of carbon substrates and conversion of their products into central metabolic intermediates. ABAT also connects this program to GABA and succinic-semialdehyde metabolism, while ETFDH links it to mitochondrial electron transfer and fatty-acid oxidation. The STRING enrichments (STRING KEGG Valine, leucine and isoleucine degradation; within-query FDR = 0.00052), (STRING KEGG Propanoate metabolism; within-query FDR = 0.0019), (STRING NetworkNeighborAL Fatty acid beta-oxidation, and Valine catabolic process; within-query FDR = 0.0228), (STRING Process Small molecule catabolic process; within-query FDR = 0.0254), (STRING NetworkNeighborAL Short-chain fatty acid catabolic process, and Thymine catabolic process; within-query FDR = 0.037), (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.0434), and (STRING WikiPathways Leucine, isoleucine and valine metabolism; within-query FDR = 0.0456) are concordant supporting evidence, but they are supplementary rather than additional global enrichment claims.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not primarily a blood-cell module, because most genes have low immune-cell specificity and the blood-cell signals are scattered across distinct immune populations. Instead, the composition is strongly tissue and cell-type selective, with frequent liver enrichment and hepatocyte enrichment, together with signals in kidney, skeletal muscle, adipose, and other metabolically active cell types. Protein detection in both brain and liver is widespread. This pattern supports a shared intracellular metabolic program rather than a blood-contamination explanation, although the liver and hepatocyte bias suggests that the cross-tissue signal may be driven partly by conserved metabolic machinery in specialized parenchymal cells. The presence of ABAT and its brain enrichment is consistent with a genuine neural component as well.

**GO/KEGG enrichment**: 6 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP small molecule catabolic process | 0.000879 | ABAT, ALDH2, ALDH4A1, ALDH6A1, CRYL1, DBT, ETFDH, PCCA, PCCB, TKFC |
| KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human) | 0.00276 | ABAT, ALDH2, ALDH6A1, DBT, PCCA, PCCB |
| GO:BP organic acid catabolic process | 0.00715 | ABAT, ALDH4A1, ALDH6A1, CRYL1, DBT, ETFDH, PCCA, PCCB |
| GO:BP carboxylic acid catabolic process | 0.00715 | ABAT, ALDH4A1, ALDH6A1, CRYL1, DBT, ETFDH, PCCA, PCCB |
| KEGG Propanoate metabolism - Homo sapiens (human) | 0.00935 | ABAT, ALDH6A1, DBT, PCCA, PCCB |
| GO:BP branched-chain amino acid metabolic process | 0.0474 | ALDH6A1, DBT, PCCA, PCCB |

### STRING and hu.MAP

STRING already contains a coherent set of high-confidence relationships among the central metabolic genes. The strongest established structure links PCCA with PCCB and connects both to DBT, ALDH6A1, ALDH2, ABAT, and related catabolic enzymes. These relationships correspond to known functional coupling in branched-chain amino-acid and propionyl-CoA metabolism, rather than merely generic co-expression. STRING also supports mitochondrial-matrix localization and amino-acid metabolic-disorder associations (STRING DISEASES Amino acid metabolic disorder; within-query FDR = 0.0065) and (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.0434). hu.MAP independently identifies complexes containing PCCA and PCCB, complexes containing ALDH2 and ALDH6A1, and a larger mitochondrial complex containing PCCA, PCCB, and ALDH4A1 (hu.MAP huMAP3_13468.1) through (hu.MAP huMAP3_10458.1). Thus, part of the module reflects previously characterized physical or functional machinery. The remaining links, including the connections involving GPD1, TKFC, DMD, GSTM1, SEC14L2, and several low-connectivity genes, are less directly supported by the listed STRING and hu.MAP relationships and may represent metabolic coupling, shared regulation, or tissue-contextual co-abundance.

**STRING interactions (score >= 0.7)**: 17 of 153 gene pairs: ABAT–ALDH2 (0.945); ABAT–ALDH6A1 (0.963); ABAT–DBT (0.84); ABAT–PCCA (0.821); ABAT–PCCB (0.826); ALDH2–ALDH4A1 (0.85); ALDH2–ALDH6A1 (0.961); ALDH2–DBT (0.86); ALDH2–PCCA (0.844); ALDH2–PCCB (0.843); ALDH6A1–DBT (0.956); ALDH6A1–PCCA (0.96); ALDH6A1–PCCB (0.967); DBT–PCCA (0.961); DBT–PCCB (0.972); GPD1–TKFC (0.865); PCCA–PCCB (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Valine, leucine and isoleucine degradation (FDR = 0.00052, 6 genes); KEGG Propanoate metabolism (FDR = 0.0019, 5 genes); DISEASES Amino acid metabolic disorder (FDR = 0.0065, 7 genes); KEGG Metabolic pathways (FDR = 0.0193, 12 genes); DISEASES Gamma-amino butyric acid metabolism disorder (FDR = 0.0203, 3 genes); NetworkNeighborAL Fatty acid beta-oxidation, and Valine catabolic process (FDR = 0.0228, 5 genes); Process Small molecule catabolic process (FDR = 0.0254, 9 genes); NetworkNeighborAL Short-chain fatty acid catabolic process, and Thymine catabolic process (FDR = 0.037, 3 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.0434, 8 genes); WikiPathways Leucine, isoleucine and valine metabolism (FDR = 0.0456, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (PCCA, PCCB, ALDH4A1; 3/99); huMAP3_06207.1 (ALDH2, ALDH6A1; 2/2); huMAP3_13307.1 (ALDH2, ALDH6A1; 2/3); huMAP3_07028.1 (PCCA, PCCB; 2/4); huMAP3_10458.1 (PCCA, PCCB; 2/16)

### Novelty

The core biochemical interpretation is not a wholly new pathway discovery. The central relationships among DBT, PCCA, PCCB, ALDH6A1, ALDH2, and ABAT are already supported by STRING, hu.MAP, enzyme functions, and established metabolic disease associations. The enrichment results also reproduce well-known branched-chain amino-acid and propanoate degradation biology. A potentially novel aspect is the identification of this particular co-abundance configuration as a conserved brain-liver module, including its peripheral metabolic genes and its weaker connections to glycerol, carbohydrate, detoxification, lipid, and structural programs. However, that interpretation should be treated as a context-specific systems-level finding rather than proof of a new molecular complex or new pathway. The absence of some genes or edges from STRING or hu.MAP cannot by itself establish novelty.

**Hypothesis.** Hypothesis: the module represents a conserved mitochondrial metabolic state shared by hepatocytes and selected brain cells, in which branched-chain amino-acid and propionyl-CoA catabolism supplies respiratory metabolism while ETFDH transfers reducing equivalents into the respiratory chain. ALDH6A1, DBT, PCCA, and PCCB may form the principal catabolic backbone; ALDH2 and ABAT may broaden aldehyde and GABA-related substrate handling; and GPD1, CRYL1, TKFC, GSTM1, and SEC14L2 may couple this backbone to redox balance, glycerol or carbohydrate flux, lipid handling, and detoxification. The shared brain-liver abundance could therefore reflect coordinated adaptation to substrate availability and mitochondrial oxidative demand. This is a mechanistic model, not a demonstrated causal interaction; testing it would require perturbation or flux measurements in relevant brain and liver cell types.

### Important genes

#### ALDH6A1

- **Related proteins** (co-abundance neighbors): ALDH2 (0.86), ETFDH (0.83); STRING partners: ABAT (0.963), ALDH2 (0.961), DBT (0.956), PCCA (0.96), PCCB (0.967)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: huMAP3_06207.1, huMAP3_13307.1
- **Function (MyGene.info)**: aldehyde dehydrogenase 6 family member A1. This gene encodes a member of the aldehyde dehydrogenase protein family. The encoded protein is a mitochondrial methylmalonate semialdehyde dehydrogenase that plays a role in the valine and pyrimidine catabolic pathways. This protein catalyzes the irreversible oxidative decarboxylation of malonate and methylmalonate semialdehydes to acetyl- and propionyl-CoA. Methylmalonate semialdehyde dehydrogen…
- **Diseases (Open Targets)**: methylmalonate semialdehyde dehydrogenase deficiency (0.706); hereditary disease (0.413); alcohol drinking (0.158); atrial fibrillation (0.089); gastric cancer (0.076)
- **Europe PMC papers**: 1031
- **Why important**: ALDH6A1 is a central interpretive gene because it appears in every globally corrected enrichment category (GO:BP small molecule catabolic process; q_global = 0.000879) through (GO:BP branched-chain amino acid metabolic process; q_global = 0.0474). It encodes mitochondrial methylmalonate semialdehyde dehydrogenase involved in valine and pyrimidine catabolism, has liver and kidney enrichment, and is detected in brain and liver. It is also strongly connected in STRING to DBT, PCCA, PCCB, ALDH2, and ABAT, and is present in hu.MAP complexes (hu.MAP huMAP3_06207.1) and (hu.MAP huMAP3_13307.1). Its disease association with methylmalonate semialdehyde dehydrogenase deficiency provides a direct clinical link to disruption of this catabolic chemistry.
- **Conclusion**: Established evidence supports ALDH6A1 as a core mitochondrial catabolic enzyme and a major biochemical organizer of this module. It is plausible, but not proven, that ALDH6A1 helps define the shared brain-liver metabolic state.

#### DBT

- **Related proteins** (co-abundance neighbors): ETFDH (0.83), BPHL (0.81); STRING partners: ABAT (0.84), ALDH2 (0.86), ALDH6A1 (0.956), PCCA (0.961), PCCB (0.972)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dihydrolipoamide branched chain transacylase E2. The branched-chain alpha-keto acid dehydrogenase complex (BCKD) is an inner-mitochondrial enzyme complex involved in the breakdown of the branched-chain amino acids isoleucine, leucine, and valine. The BCKD complex is thought to be composed of a core of 24 transacylase (E2) subunits, and associated decarboxylase (E1), dehydrogenase (E3), and regulatory subunits. This gene encodes the transacylase …
- **Diseases (Open Targets)**: maple syrup urine disease (0.710); maple syrup urine disease type 1A (0.695); maple syrup urine disease type 2 (0.659); intermittent maple syrup urine disease (0.370); classic maple syrup urine disease (0.370)
- **Europe PMC papers**: 15522
- **Why important**: DBT is the transacylase component of the branched-chain alpha-keto-acid dehydrogenase complex and participates in degradation of leucine, isoleucine, and valine. It occurs in all globally corrected enrichment categories (GO:BP small molecule catabolic process; q_global = 0.000879) through (GO:BP branched-chain amino acid metabolic process; q_global = 0.0474), has extensive STRING support with the module's central enzymes, and is detected in both brain and liver. Its association with maple syrup urine disease gives the module a strong disease-relevant anchor.
- **Conclusion**: Established evidence identifies DBT as a core enzymatic component of branched-chain amino-acid breakdown. Its co-abundance with propionyl-CoA and aldehyde-processing genes is consistent with pathway coordination, although co-abundance alone does not establish direct physical coupling beyond the relationships already documented.

#### PCCA

- **Related proteins** (co-abundance neighbors): PCCB (0.82), PPM1A (0.82); STRING partners: ABAT (0.821), ALDH2 (0.844), ALDH6A1 (0.96), DBT (0.961), PCCB (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_07028.1, huMAP3_10458.1
- **Function (MyGene.info)**: propionyl-CoA carboxylase subunit alpha. The protein encoded by this gene is the alpha subunit of the heterodimeric mitochondrial enzyme Propionyl-CoA carboxylase. PCCA encodes the biotin-binding region of this enzyme. Mutations in either PCCA or PCCB (encoding the beta subunit) lead to an enzyme deficiency resulting in propionic acidemia. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by…
- **Diseases (Open Targets)**: propionic acidemia (0.853); hereditary disease (0.487); dilated cardiomyopathy (0.370); neurodegenerative disease (0.357); pontocerebellar hypoplasia type 2D (0.340)
- **Europe PMC papers**: 2633
- **Why important**: PCCA is the biotin-binding alpha subunit of propionyl-CoA carboxylase and is present in every globally corrected enrichment category (GO:BP small molecule catabolic process; q_global = 0.000879) through (GO:BP branched-chain amino acid metabolic process; q_global = 0.0474). It has strong STRING connections across the central module, forms a documented pair with PCCB, and appears in several hu.MAP complexes (hu.MAP huMAP3_13468.1), (hu.MAP huMAP3_07028.1), and (hu.MAP huMAP3_10458.1). Its propionic-acidemia association directly supports the interpretation that the module handles propionyl-CoA and short-chain carbon metabolism.
- **Conclusion**: Established evidence supports PCCA as a core enzymatic and complex-level component of the module. The brain-liver co-abundance pattern may indicate shared regulation of propionyl-CoA disposal, but this regulatory interpretation remains a hypothesis.

#### PCCB

- **Related proteins** (co-abundance neighbors): PCCA (0.82), ETFDH (0.81); STRING partners: ABAT (0.826), ALDH2 (0.843), ALDH6A1 (0.967), DBT (0.972), PCCA (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain, liver
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_07028.1, huMAP3_10458.1
- **Function (MyGene.info)**: propionyl-CoA carboxylase subunit beta. The protein encoded by this gene is a subunit of the propionyl-CoA carboxylase (PCC) enzyme, which is involved in the catabolism of propionyl-CoA. PCC is a mitochondrial enzyme that probably acts as a dodecamer of six alpha subunits and six beta subunits. This gene encodes the beta subunit of PCC. Defects in this gene are a cause of propionic acidemia type II (PA-2). Multiple transcript variants e…
- **Diseases (Open Targets)**: propionic acidemia (0.861); hereditary disease (0.517); hypertensive disorder (0.453); coronary artery disorder (0.438); coronary atherosclerosis (0.428)
- **Europe PMC papers**: 1404
- **Why important**: PCCB is the beta subunit of propionyl-CoA carboxylase, partners exceptionally closely with PCCA in STRING, and appears in the same hu.MAP complexes (hu.MAP huMAP3_13468.1), (hu.MAP huMAP3_07028.1), and (hu.MAP huMAP3_10458.1). It is included in every globally corrected enrichment category (GO:BP small molecule catabolic process; q_global = 0.000879) through (GO:BP branched-chain amino acid metabolic process; q_global = 0.0474), is liver enriched, and is detected in both tissues. Its association with propionic acidemia provides independent disease evidence for the proposed propionyl-CoA catabolic role.
- **Conclusion**: Established evidence supports PCCB as an essential partner of PCCA and a central component of the module's propionate and branched-chain amino-acid metabolism. Its importance is biochemical and structural rather than evidence of a newly discovered interaction.

#### ABAT

- **Related proteins** (co-abundance neighbors): ALDH2 (0.81); STRING partners: ALDH2 (0.945), ALDH6A1 (0.963), DBT (0.84), PCCA (0.821), PCCB (0.826)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 4-aminobutyrate aminotransferase. 4-aminobutyrate aminotransferase (ABAT) is responsible for catabolism of gamma-aminobutyric acid (GABA), an important, mostly inhibitory neurotransmitter in the central nervous system, into succinic semialdehyde. The active enzyme is a homodimer of 50-kD subunits complexed to pyridoxal-5-phosphate. The protein sequence is over 95% similar to the pig protein. GABA is estimated to be present in near…
- **Diseases (Open Targets)**: GABA aminotransaminase deficiency (0.795); infantile spasms (0.568); mitochondrial DNA depletion syndrome (0.542); epilepsy (0.468); Focal impaired awareness seizure (0.466)
- **Europe PMC papers**: 1783
- **Why important**: ABAT connects the module's dominant mitochondrial catabolic signature to GABA metabolism. It is included in the globally corrected small-molecule, branched-chain, organic-acid, carboxylic-acid, and propanoate terms (GO:BP small molecule catabolic process; q_global = 0.000879) through (KEGG Propanoate metabolism - Homo sapiens (human); q_global = 0.00935), has STRING support with several core genes, and is enriched in brain as well as liver and kidney. Its established role in GABA catabolism and associations with GABA aminotransferase deficiency, infantile spasms, and epilepsy make it especially relevant to the brain-liver interpretation.
- **Conclusion**: Established evidence supports ABAT as a bridge between neural neurotransmitter catabolism and broader mitochondrial carbon metabolism. It is reasonable to hypothesize that ABAT contributes to the brain-specific meaning of the shared module, but the module does not demonstrate altered GABA flux.

#### ETFDH

- **Related proteins** (co-abundance neighbors): DBT (0.83), ALDH6A1 (0.83), ALDH4A1 (0.82), CRYL1 (0.81), PCCB (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein dehydrogenase. This gene encodes a component of the electron-transfer system in mitochondria and is essential for electron transfer from a number of mitochondrial flavin-containing dehydrogenases to the main respiratory chain. Mutations in this gene are associated with glutaric acidemia. Alternatively spliced transcript variants that encode distinct isoforms have been observed. [provided by RefSeq, Aug 2013].
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.845); glutaric acidemia IIc (0.704); glutaric aciduria (0.670); hereditary disease (0.523); Abnormality of metabolism/homeostasis (0.407)
- **Europe PMC papers**: 1273
- **Why important**: ETFDH provides a respiratory and redox dimension to the module. It is a mitochondrial electron-transfer component required for transferring electrons from multiple flavin-containing dehydrogenases to the main respiratory chain, and it appears in the globally corrected small-molecule, organic-acid, and carboxylic-acid terms (GO:BP small molecule catabolic process; q_global = 0.000879), (GO:BP organic acid catabolic process; q_global = 0.00715), and (GO:BP carboxylic acid catabolic process; q_global = 0.00715). Its neighbors include DBT, ALDH6A1, ALDH4A1, CRYL1, and PCCB, while its disease associations include multiple acyl-CoA dehydrogenase deficiency and glutaric acidemia. It is detected in brain and liver and has liver-related tissue enrichment.
- **Conclusion**: Established evidence supports ETFDH as a plausible energetic endpoint for the module's mitochondrial catabolic reactions. Its position suggests that respiratory electron handling may coordinate the module, but the co-abundance network does not prove that ETFDH activity limits pathway flux.

## Module 6

**Tissue pair**: brain and liver  
**Genes (11)**: ALB, EPB41L5, IFIT3, IGHG1, IGHG2, IGKC, KNG1, LDHD, PEX19, PLGRKT, SYNE1

### Function

The module does not have a GO or KEGG term passing global correction. Its strongest biological interpretation is a shared blood and extracellular-protein abundance pattern rather than a single established intracellular pathway. The module combines liver-derived plasma proteins, immunoglobulin components associated with plasma and B cells, a plasminogen-related receptor, interferon-associated biology, structural membrane proteins, and metabolic or peroxisomal genes. KNG1 and ALB support a plasma coagulation, kinin, transport, and extracellular signaling context, while IGHG2, IGHG1, and IGKC support an immunoglobulin or plasma-cell component. IFIT3 is consistent with antiviral and cytokine-responsive biology. These annotations support a mixed systemic and cellular-composition signal, not a formally enriched pathway.

**Cell composition.** The module is strongly compatible with blood or shared-cell-type effects. Five genes are annotated as secreted or immunoglobulin-related, including the liver-enriched plasma proteins ALB and KNG1 and the immunoglobulin genes IGHG2, IGHG1, and IGKC. HPA also identifies hepatocytes and plasma cells as recurring enriched cell types, with memory and naive B-cell associations among the blood-cell annotations. ALB and KNG1 are detected in liver but not brain by the supplied immunohistochemistry summary, whereas several other module genes are detected in both tissues. This pattern suggests that the brain signal may partly reflect vascular, blood-derived, immune, or other shared cellular material rather than expression by the dominant brain parenchymal cell type. The module is therefore not best described as a broadly expressed housekeeping module, although several nonsecreted genes have low tissue specificity.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a single high-confidence relationship within the module, between ALB and KNG1. This is consistent with a known extracellular plasma-protein context, but it does not establish a densely connected physical interaction network. hu.MAP repeatedly places ALB and KNG1 together in several broader complexes (hu.MAP huMAP3_07265.1), (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1), and (hu.MAP huMAP3_10678.1), alongside many other plasma, complement, coagulation, transport, and immune-associated proteins. Because each listed complex contributes only these two module members, the hu.MAP evidence supports shared biochemical context or membership in broad extracellular assemblies rather than a module-specific complex. The lack of STRING partners and hu.MAP assignments for most other genes indicates that most module edges are co-abundance relationships whose molecular mechanism remains unresolved.

**STRING interactions (score >= 0.7)**: 1 of 55 gene pairs: ALB–KNG1 (0.962)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07265.1 (KNG1, ALB; 2/20); huMAP3_08395.1 (KNG1, ALB; 2/43); huMAP3_09531.1 (KNG1, ALB; 2/47); huMAP3_10101.1 (KNG1, ALB; 2/49); huMAP3_15040.1 (KNG1, ALB; 2/64); huMAP3_10678.1 (KNG1, ALB; 2/71)

### Novelty

This module should not be called a newly discovered molecular complex or pathway. Its combination of ALB, KNG1, and immunoglobulin genes is readily explained by known plasma, liver, and immune-cell biology, and the ALB-KNG1 relationship is already represented in STRING. The repeated hu.MAP overlap also connects its central extracellular proteins to established broad plasma-related assemblies. The particular cross-tissue co-abundance pattern may still be a new observation in this dataset, especially because it links liver-associated plasma proteins with immune and cell-intrinsic genes in brain and liver. However, that dataset-specific pattern requires independent validation, control for blood contamination and cell composition, and replication before it can be considered a novel biological mechanism. Absence of most module genes from STRING or hu.MAP is not evidence of novelty; it more conservatively indicates limited prior physical-interaction support.

**Hypothesis.** Hypothesis: the module reflects coordinated variation in circulating or vascular protein abundance together with immune-cell and tissue-response signals shared between brain and liver. Liver-derived ALB and KNG1 may mark the extracellular plasma component, immunoglobulin genes may report plasma-cell or B-cell material, and IFIT3 may report an accompanying antiviral or cytokine-responsive state. PLGRKT could connect the extracellular signal to plasminogen activation, while EPB41L5 and other nonsecreted genes may reflect tissue-interface or cellular-structural responses. Under this hypothesis, the apparent conserved module is driven primarily by shared blood exposure, vascular interfaces, or immune composition rather than by a single protein complex operating identically in hepatocytes and brain cells. This should be tested by cell-type deconvolution, plasma-protein adjustment, vascular and immune marker controls, and validation in tissue-matched specimens.

### Important genes

#### ALB

- **Related proteins** (co-abundance neighbors): IGKC (0.83); STRING partners: KNG1 (0.962)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07265.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB is the clearest marker of the extracellular plasma component. It is liver-enriched, hepatocyte-enriched, secreted to blood, and has the strongest supplied STRING relationship through KNG1. Its broad transport role and very extensive literature make it a central interpretive anchor, even though its network degree within this module is limited.
- **Conclusion**: Established evidence supports ALB as a liver-derived circulating protein and a likely indicator of plasma or vascular material in the shared module. It does not establish a brain-intrinsic mechanism. The hypothesis that ALB abundance drives or merely reports the cross-tissue module should be tested by adjusting for circulating-protein and vascular contributions.

#### KNG1

- **Related proteins** (co-abundance neighbors): EPB41L5 (0.83), PLGRKT (0.80); STRING partners: ALB (0.962)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_07265.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: kininogen 1. This gene uses alternative splicing to generate two different proteins- high molecular weight kininogen (HMWK) and low molecular weight kininogen (LMWK). HMWK is essential for blood coagulation and assembly of the kallikrein-kinin system. Also, bradykinin, a peptide causing numerous physiological effects, is released from HMWK. Bradykinin also functions as an antimicrobial peptide with antibacteri…
- **Diseases (Open Targets)**: congenital high-molecular-weight kininogen deficiency (0.733); venous thromboembolism (0.547); hereditary angioedema (0.458); serum lipopolysaccharide activity (0.367); ischemic stroke (0.363)
- **Europe PMC papers**: 2325
- **Why important**: KNG1 connects directly to ALB in STRING and is the other member of every reported hu.MAP overlap (hu.MAP huMAP3_07265.1), (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1), and (hu.MAP huMAP3_10678.1). It is liver-enriched, hepatocyte-associated, secreted to blood, and functionally linked to high-molecular-weight kininogen, coagulation, kallikrein-kinin signaling, bradykinin release, vasodilation, and antimicrobial activity. It also links in the co-abundance graph to PLGRKT and EPB41L5.
- **Conclusion**: Established evidence supports KNG1 as an extracellular coagulation and kinin-system protein that helps define the plasma-associated character of the module. Its graph connections suggest a possible bridge between extracellular proteolytic signaling and tissue-interface genes, but that bridge is a hypothesis rather than a demonstrated physical pathway in this module.

#### IGKC

- **Related proteins** (co-abundance neighbors): IGHG1 (0.88), ALB (0.83), IGHG2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Group enriched; location Vesicles, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: immunoglobulin kappa constant. Predicted to enable antigen binding activity and immunoglobulin receptor binding activity. Involved in retina homeostasis. Located in blood microparticle and extracellular exosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: cutaneous leishmaniasis (0.587); recurrent infections associated with rare immunoglobulin isotypes deficiency (0.572); neoplasm (0.066); Barrett esophagus (0.065); squamous cell carcinoma (0.060)
- **Europe PMC papers**: 2850
- **Why important**: IGKC is plasma-cell enriched, associated with memory and naive B-cell populations, and linked in the module to both immunoglobulin heavy-chain genes and ALB. It has substantial literature and established immunoglobulin, antigen-binding, receptor-binding, adaptive immune, and B-cell-response annotations. Its protein is associated with blood microparticles and extracellular vesicles.
- **Conclusion**: Established evidence supports IGKC as an immune-cell or immunoglobulin-abundance marker rather than a liver metabolic gene. Its co-abundance with ALB may indicate blood or extracellular-vesicle carryover and should not be interpreted as evidence of a direct ALB-IGKC complex. A contribution from B-cell or plasma-cell composition is a plausible hypothesis.

#### IFIT3

- **Related proteins** (co-abundance neighbors): IGHG2 (0.86), IGHG1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Mitochondria, Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: interferon induced protein with tetratricopeptide repeats 3. Enables identical protein binding activity. Involved in negative regulation of apoptotic process; negative regulation of cell population proliferation; and response to virus. Located in cytosol and mitochondrion. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: systemic lupus erythematosus (0.108); neoplasm (0.104); systemic sclerosis (0.090); esophageal squamous cell carcinoma (0.087); acute promyelocytic leukemia (0.084)
- **Europe PMC papers**: 6714
- **Why important**: IFIT3 has the largest supplied literature volume among the module genes and is connected to both IGHG genes. It is detected in brain and liver, is associated with several cell types including oligodendrocytes and neutrophils, and has established annotations for antiviral innate immunity, cytokine response, response to virus, and regulation of apoptosis and proliferation.
- **Conclusion**: Established evidence supports IFIT3 as a tissue-compatible antiviral and cytokine-responsive marker. Its placement beside immunoglobulin genes suggests that immune activation may accompany the plasma-cell signal, but the module does not demonstrate that IFIT3 mechanistically regulates the secreted proteins. The shared-tissue relationship may reflect a common inflammatory state or cell-composition effect.

#### IGHG2

- **Related proteins** (co-abundance neighbors): PLGRKT (0.94), SYNE1 (0.87), IFIT3 (0.86), IGKC (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Group enriched; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: immunoglobulin heavy constant gamma 2 (G2m marker)
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 1063
- **Why important**: IGHG2 has the highest weighted degree in the supplied module and links immunoglobulin-related signal to PLGRKT, SYNE1, IFIT3, and IGKC. HPA associates it with lymphoid tissue, plasma cells, and memory and naive B-cell populations, while the supplied literature indicates substantial study. Its liver detection with absence of brain detection is particularly relevant to interpreting the cross-tissue signal.
- **Conclusion**: Established evidence supports IGHG2 as an immunoglobulin and plasma-cell-associated component that may report blood or immune material. Its central network position makes it important for explaining the module, but does not prove that it forms a functional intracellular network with the neighboring genes. A blood or immune-composition explanation is more strongly supported than a brain-cell-autonomous role.

#### PLGRKT

- **Related proteins** (co-abundance neighbors): IGHG2 (0.94), KNG1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plasminogen receptor with a C-terminal lysine. Predicted to be involved in positive regulation of plasminogen activation. Predicted to be integral component of plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypothyroidism (0.514); myxedema (0.433); autoimmune thyroid disease (0.276); placenta praevia (0.214); thyroid gland disorder (0.194)
- **Europe PMC papers**: 271
- **Why important**: PLGRKT links IGHG2 to KNG1 in the module and is annotated as a plasminogen receptor with a predicted role in positive regulation of plasminogen activation. It is detected in both brain and liver, has colonocyte and enterocyte cell-type associations, and provides a plausible interface between the extracellular kinin or plasminogen context and tissue-associated cells. Its literature base is smaller than that of the principal plasma and immune genes.
- **Conclusion**: Established evidence supports PLGRKT as a candidate plasminogen-related membrane component with a distinctive bridging position in the co-abundance graph. Its connection to KNG1 and IGHG2 is compatible with the proposed extracellular and immune hypothesis, but no direct STRING or hu.MAP support is supplied. Its mechanistic role in the shared brain-liver module therefore remains provisional.

## Module 7

**Tissue pair**: brain and liver  
**Genes (40)**: ANXA1, AP3B1, CCAR1, CLIC1, CLUH, CSTF3, DDX46, DDX5, EIF3C, EIF3F, FUS, HNRNPL, IMPDH2, LBR, LMNB1, MATR3, MESD, NAA15, SNU13, NUP93, PCNA, PSMD13, GART, CTPS1, RBM39, RSL1D1, RPL3, RPL9, RPRD1B, SNRPA1, RUVBL2, SEC23IP, SF3A1, SUPT16H, SRP72, SRRT, TCEA1, ALYREF, EFTUD2, UBTF

### Function

This is a conserved nuclear gene-expression and RNA-processing module. The primary evidence is the globally corrected enrichment for nucleic-acid binding (GO:MF nucleic acid binding; q_global = 5.43e-09), RNA binding (GO:MF RNA binding; q_global = 3.79e-07), ribonucleoprotein complexes (GO:CC ribonucleoprotein complex; q_global = 1.38e-05), nuclear lumen and nucleoplasm (GO:CC nuclear lumen; q_global = 4.06e-05) (GO:CC nucleoplasm; q_global = 0.00124), gene expression (GO:BP gene expression; q_global = 6.74e-05), mRNA metabolism and processing (GO:BP mRNA metabolic process; q_global = 0.000172) (GO:BP mRNA processing; q_global = 0.000304) (GO:BP RNA processing; q_global = 0.00183), and spliceosome-mediated RNA splicing (5 globally significant GO/KEGG terms, q_global 0.000613–0.0108; see the table). The module also contains evidence for RNA biosynthesis, nucleic-acid metabolism, protein–RNA complex assembly, and nuclear speck localization (8 globally significant GO/KEGG terms, q_global 0.000879–0.0462; see the table). Together, these results support coordinated control of nuclear RNA maturation, splicing, export-related processing, transcription, ribonucleoprotein assembly, and translation-linked gene expression. The module is not a single isolated pathway: it combines a core spliceosomal program with transcriptional, ribosomal, nucleotide-biosynthetic, nuclear-envelope, and translation-initiation components.

**Cell composition.** The module is dominated by intracellular, nuclear, RNA-binding, spliceosomal, ribosomal, and general gene-expression proteins rather than plasma or secreted proteins. HPA reports secreted status for only ANXA1 and identifies MESD as intracellular and membrane-associated; the remaining annotated proteins are not secreted. Most genes have low tissue specificity, and the module proteins are broadly detected in brain and liver where measurements are available. HPA indicates low immune-cell specificity for nearly all genes, so the module does not strongly resemble a blood-cell program, although some genes show enhancement in erythrocyte progenitors, bone marrow, lymphoid tissue, or other specialized cell types. The shared brain–liver signal is therefore more consistent with a broadly expressed housekeeping-like nuclear and RNA-processing program than with a plasma-protein or blood-contamination module. Cell-composition effects cannot be excluded, particularly for genes enhanced in erythrocyte progenitors or bone marrow, but they are not the dominant interpretation from the HPA summary.

**GO/KEGG enrichment**: 28 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleic acid binding | 5.43e-09 | ALYREF, CCAR1, CLUH, CSTF3, DDX46, DDX5, EFTUD2, EIF3C, FUS, HNRNPL, IMPDH2, LBR, LMNB1, MATR3, NAA15, PCNA, RBM39, RPL3, RPL9, RSL1D1, RUVBL2, SEC23IP, SF3A1, SNRPA1, SNU13, SRP72, SRRT, SUPT16H, TCEA1, UBTF |
| GO:MF RNA binding | 3.79e-07 | ALYREF, CCAR1, CLUH, CSTF3, DDX46, DDX5, EFTUD2, EIF3C, FUS, HNRNPL, IMPDH2, LBR, MATR3, NAA15, RBM39, RPL3, RPL9, RSL1D1, SEC23IP, SF3A1, SNRPA1, SNU13, SRP72, SRRT, SUPT16H, UBTF |
| GO:CC ribonucleoprotein complex | 1.38e-05 | DDX46, DDX5, EFTUD2, EIF3C, EIF3F, HNRNPL, RPL3, RPL9, RUVBL2, SF3A1, SNRPA1, SNU13, SRP72, SRRT |
| GO:CC nuclear lumen | 4.06e-05 | ALYREF, ANXA1, CCAR1, CSTF3, DDX46, DDX5, EFTUD2, FUS, HNRNPL, LBR, LMNB1, MATR3, NAA15, NUP93, PCNA, PSMD13, RBM39, RPL3, RPRD1B, RSL1D1, RUVBL2, SF3A1, SNRPA1, SNU13, SRRT, SUPT16H, TCEA1, UBTF |
| GO:BP gene expression | 6.74e-05 | ANXA1, AP3B1, CCAR1, CSTF3, DDX46, DDX5, EFTUD2, EIF3C, EIF3F, FUS, HNRNPL, LBR, LMNB1, MATR3, MESD, NAA15, NUP93, PCNA, RBM39, RPL3, RPL9, RPRD1B, RUVBL2, SF3A1, SNRPA1, SNU13, SRRT, SUPT16H, TCEA1, UBTF |
| GO:BP mRNA metabolic process | 0.000172 | AP3B1, CSTF3, DDX46, DDX5, EFTUD2, FUS, HNRNPL, RBM39, RPRD1B, SF3A1, SNRPA1, SNU13, SRRT |
| GO:BP macromolecule biosynthetic process | 0.000275 | ANXA1, AP3B1, CCAR1, CSTF3, DDX46, DDX5, EFTUD2, EIF3C, EIF3F, FUS, HNRNPL, LBR, LMNB1, MATR3, MESD, NAA15, NUP93, PCNA, RBM39, RPL3, RPL9, RPRD1B, RUVBL2, SF3A1, SNRPA1, SNU13, SRRT, SUPT16H, TCEA1, UBTF |
| GO:BP mRNA processing | 0.000304 | CSTF3, DDX46, DDX5, EFTUD2, HNRNPL, RBM39, RPRD1B, SF3A1, SNRPA1, SNU13, SRRT |
| KEGG Spliceosome - Homo sapiens (human) | 0.000613 | ALYREF, DDX46, DDX5, EFTUD2, FUS, SF3A1, SNRPA1, SNU13 |
| GO:BP RNA biosynthetic process | 0.000879 | AP3B1, CCAR1, CSTF3, DDX46, DDX5, EFTUD2, FUS, HNRNPL, NAA15, PCNA, RBM39, RPRD1B, RUVBL2, SF3A1, SNRPA1, SNU13, SRRT, SUPT16H, TCEA1, UBTF |
| GO:CC nucleoplasm | 0.00124 | ALYREF, ANXA1, CCAR1, CSTF3, DDX46, DDX5, EFTUD2, FUS, HNRNPL, LBR, LMNB1, NAA15, PCNA, PSMD13, RBM39, RPRD1B, RUVBL2, SF3A1, SNRPA1, SNU13, SRRT, SUPT16H, TCEA1, UBTF |
| GO:BP nucleic acid biosynthetic process | 0.00145 | AP3B1, CCAR1, CSTF3, DDX46, DDX5, EFTUD2, FUS, HNRNPL, NAA15, PCNA, RBM39, RPRD1B, RUVBL2, SF3A1, SNRPA1, SNU13, SRRT, SUPT16H, TCEA1, UBTF |
| GO:BP RNA processing | 0.00183 | CSTF3, DDX46, DDX5, EFTUD2, FUS, HNRNPL, RBM39, RPRD1B, SF3A1, SNRPA1, SNU13, SRRT |
| GO:BP nucleobase-containing compound biosynthetic process | 0.00462 | AP3B1, CCAR1, CSTF3, CTPS1, DDX46, DDX5, EFTUD2, FUS, GART, HNRNPL, IMPDH2, NAA15, PCNA, RBM39, RPRD1B, RUVBL2, SF3A1, SNRPA1, SNU13, SRRT, SUPT16H, TCEA1, UBTF |
| GO:CC nuclear protein-containing complex | 0.00511 | CSTF3, DDX46, DDX5, EFTUD2, NUP93, PCNA, RUVBL2, SF3A1, SNRPA1, SNU13, SUPT16H, TCEA1 |

### STRING and hu.MAP

STRING provides established, high-confidence relationships that reinforce the biological interpretation. The strongest connected group contains spliceosomal and small nuclear ribonucleoprotein components, including SF3A1, SNRPA1, SNU13, EFTUD2, and DDX46, with additional links among ALYREF, DDX5, RBM39, FUS, HNRNPL, and SRRT. Other established relationships connect EIF3C with EIF3F, RPL3 with RPL9, RSL1D1 with ribosomal proteins, LBR with LMNB1, and CTPS1 with IMPDH2. hu.MAP independently places SNRPA1, SNU13, EFTUD2, SF3A1, and DDX46 in spliceosomal complexes (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_06511.1), supports HNRNPL–MATR3 ribonucleoprotein associations (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10625.1), EIF3C–EIF3F translation-initiation complexes (hu.MAP huMAP3_01276.1) (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1), and additional complexes involving ALYREF–SRRT, SF3A1–CCAR1, and TCEA1–MESD (hu.MAP huMAP3_13998.1) (hu.MAP huMAP3_10359.1) (hu.MAP huMAP3_14982.1) (hu.MAP huMAP3_09943.1). Thus, the network is not merely based on correlated expression: substantial portions correspond to known molecular interactions and complexes. At the same time, many module edges lack a reported STRING or hu.MAP relationship, so the co-abundance graph should not be interpreted as a physical complex map.

**STRING interactions (score >= 0.7)**: 49 of 780 gene pairs: ALYREF–DDX5 (0.929); ALYREF–EFTUD2 (0.89); ALYREF–HNRNPL (0.844); ALYREF–RBM39 (0.906); ALYREF–SRRT (0.99); CCAR1–DDX5 (0.836); CCAR1–RBM39 (0.875); CCAR1–SRRT (0.857); CTPS1–GART (0.734); CTPS1–IMPDH2 (0.927); DDX46–EFTUD2 (0.723); DDX46–SF3A1 (0.999); DDX46–SNRPA1 (0.995); DDX5–FUS (0.872); DDX5–MATR3 (0.894); DDX5–RBM39 (0.971); DDX5–SRRT (0.855); EFTUD2–RPL3 (0.837); EFTUD2–RPL9 (0.864); EFTUD2–RUVBL2 (0.793); EFTUD2–SF3A1 (0.999); EFTUD2–SNRPA1 (0.999); EFTUD2–SNU13 (0.998); EIF3C–EIF3F (0.999); EIF3F–PSMD13 (0.705); EIF3F–RPL9 (0.74); FUS–HNRNPL (0.927); FUS–MATR3 (0.91); GART–IMPDH2 (0.811); GART–RPL3 (0.805); HNRNPL–MATR3 (0.757); HNRNPL–RBM39 (0.75); HNRNPL–SRRT (0.725); LBR–LMNB1 (0.999); RBM39–SF3A1 (0.722); RBM39–SRRT (0.936); RPL3–RPL9 (0.999); RPL3–RSL1D1 (0.846); RPL3–SNU13 (0.759); RPL3–SRP72 (0.936); RPL9–RSL1D1 (0.858); RPL9–SNU13 (0.839); RPL9–SRP72 (0.878); RSL1D1–SNU13 (0.893); RUVBL2–SNU13 (0.869); SF3A1–SNRPA1 (0.999); SF3A1–SNU13 (0.994); SNRPA1–SNU13 (0.993); SUPT16H–TCEA1 (0.874)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Nucleic acid binding (FDR = 8.89e-11, 31 genes); COMPARTMENTS Nuclear lumen (FDR = 2.56e-10, 23 genes); COMPARTMENTS Nucleoplasm (FDR = 1.53e-08, 17 genes); Function RNA binding (FDR = 4.51e-08, 26 genes); RCTM Processing of Capped Intron-Containing Pre-mRNA (FDR = 1.63e-07, 14 genes); RCTM Metabolism of RNA (FDR = 1.63e-07, 17 genes); Component Ribonucleoprotein complex (FDR = 3e-07, 16 genes); COMPARTMENTS Nucleus (FDR = 3.66e-07, 30 genes); RCTM mRNA Splicing - Major Pathway (FDR = 3.99e-07, 12 genes); Process Gene expression (FDR = 4.84e-07, 24 genes); Keyword Nucleus (FDR = 1.66e-06, 27 genes); Keyword Isopeptide bond (FDR = 1.66e-06, 20 genes); Keyword Ubl conjugation (FDR = 9.96e-06, 20 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 1.13e-05, 13 genes); Process RNA metabolic process (FDR = 1.51e-05, 18 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (SNRPA1, SNU13, EFTUD2, SF3A1, DDX46; 5/97); huMAP3_06511.1 (SNRPA1, SNU13, SF3A1, DDX46; 4/79); huMAP3_05721.1 (HNRNPL, MATR3; 2/6); huMAP3_01276.1 (EIF3F, EIF3C; 2/17); huMAP3_13175.1 (EIF3F, EIF3C; 2/20); huMAP3_07581.1 (HNRNPL, MATR3; 2/21); huMAP3_13998.1 (TCEA1, MESD; 2/23); huMAP3_11246.1 (EIF3F, EIF3C; 2/24); huMAP3_10359.1 (SF3A1, CCAR1; 2/27); huMAP3_14982.1 (TCEA1, MESD; 2/28); huMAP3_04549.1 (SF3A1, DDX46; 2/52); huMAP3_10625.1 (HNRNPL, MATR3; 2/57); huMAP3_09943.1 (ALYREF, SRRT; 2/78)

### Novelty

The module-level function is not wholly novel because its central spliceosomal, ribonucleoprotein, RNA-binding, translation-initiation, and nuclear-envelope relationships are already represented in STRING and hu.MAP. The co-abundance observation may nevertheless be a new systems-level finding: the conserved brain–liver organization of these components, the particular combination of RNA processing with nucleotide synthesis and nuclear architecture, and the cross-tissue co-abundance structure are not established merely by the existence of individual database interactions. Absence of some module pairs from STRING or hu.MAP is not evidence of novelty, because those resources are incomplete and are designed around physical interaction or complex evidence rather than tissue-pair co-abundance. I would therefore describe this as a potentially novel conserved tissue-pair network organization built largely from well-established cellular machinery, rather than as discovery of a new molecular pathway.

**Hypothesis.** Hypothesis: in both brain and liver, cellular demand for sustained transcription and protein production couples chromatin-associated transcriptional activity with coordinated pre-mRNA splicing, RNA quality control, nuclear export, ribosome production, translation initiation, and nucleotide supply. In this model, the spliceosomal core comprising SF3A1, SNRPA1, SNU13, EFTUD2, and DDX46 processes nascent transcripts; DDX5, FUS, HNRNPL, RBM39, ALYREF, and SRRT help regulate RNA structure, processing, and export; SUPT16H and TCEA1 support transcription through chromatin; and IMPDH2, CTPS1, and GART help maintain nucleotide availability. The brain–liver conservation could reflect a shared requirement for high-throughput RNA and protein homeostasis rather than a tissue-specific disease mechanism. This hypothesis requires validation with cell-type-resolved data, perturbation experiments, and independent cohorts.

### Important genes

#### DDX5

- **Related proteins** (co-abundance neighbors): IMPDH2 (0.88), EIF3F (0.87), LMNB1 (0.83), RSL1D1 (0.83), FUS (0.82), PSMD13 (0.80); STRING partners: ALYREF (0.929), CCAR1 (0.836), FUS (0.872), MATR3 (0.894), RBM39 (0.971), SRRT (0.855)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 is a central connector in the module, linking IMPDH2, EIF3F, LMNB1, RSL1D1, FUS, and PSMD13 in the co-abundance graph. It appears across nearly all primary RNA-processing and spliceosome terms (11 globally significant GO/KEGG terms, q_global 5.43e-09–0.0108; see the table), and STRING links it to ALYREF, CCAR1, FUS, MATR3, RBM39, and SRRT. Its annotation supports RNA-structure remodeling, transcriptional co-regulation, splicing, and small noncoding-RNA processing. Its disease relevance includes neurodegenerative and cancer-related associations, and it has substantial literature support.
- **Conclusion**: Established evidence supports DDX5 as a multifunctional RNA helicase and a plausible organizational hub for the module's RNA-processing program. It is reasonable to hypothesize that DDX5 helps couple splicing with broader gene-expression activity here, but the co-abundance data do not establish that DDX5 controls the entire module.

#### SF3A1

- **Related proteins** (co-abundance neighbors): SUPT16H (0.82), EIF3F (0.82), RPL3 (0.80), SRRT (0.80); STRING partners: DDX46 (0.999), EFTUD2 (0.999), RBM39 (0.722), SNRPA1 (0.999), SNU13 (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in brain, liver
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_06511.1, huMAP3_10359.1, huMAP3_04549.1
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 is a core component of the U2 spliceosomal machinery and is present in the primary spliceosome, RNA-splicing, ribonucleoprotein, and nuclear terms (8 globally significant GO/KEGG terms, q_global 1.38e-05–0.0108; see the table). It has high-confidence STRING relationships with DDX46, EFTUD2, SNRPA1, and SNU13, and occurs in several hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_10359.1) (hu.MAP huMAP3_04549.1). Its network position connects the conserved spliceosomal core to SUPT16H, EIF3F, RPL3, and SRRT. Its annotation directly supports spliceosome assembly and pre-mRNA splicing, with additional disease associations involving neurodegeneration and other disorders.
- **Conclusion**: Established evidence identifies SF3A1 as a mechanistic core of the module's spliceosomal function. Its co-abundance with transcriptional and translation-associated genes supports coordinated gene expression, but does not prove that the brain–liver module contains a single stable spliceosomal complex.

#### FUS

- **Related proteins** (co-abundance neighbors): SNRPA1 (0.83), PCNA (0.83), DDX5 (0.82), IMPDH2 (0.81), NUP93 (0.80); STRING partners: DDX5 (0.872), HNRNPL (0.927), MATR3 (0.91)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FUS RNA binding protein. This gene encodes a multifunctional protein component of the heterogeneous nuclear ribonucleoprotein (hnRNP) complex. The hnRNP complex is involved in pre-mRNA splicing and the export of fully processed mRNA to the cytoplasm. This protein belongs to the FET family of RNA-binding proteins which have been implicated in cellular processes that include regulation of gene expression, maintenance of gen…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.710); sporadic amyotrophic lateral sclerosis (0.683); frontotemporal dementia with motor neuron disease (0.667); essential tremor (0.557); juvenile amyotrophic lateral sclerosis (0.527)
- **Europe PMC papers**: 19869
- **Why important**: FUS connects spliceosomal genes with PCNA, DDX5, IMPDH2, and NUP93 in the module graph. It is included in primary terms for RNA binding, gene expression, mRNA metabolism, spliceosome function, DNA binding, and nuclear localization (9 globally significant GO/KEGG terms, q_global 5.43e-09–0.00994; see the table). STRING supports relationships with DDX5, HNRNPL, and MATR3. Its established functions include RNA binding, pre-mRNA splicing, regulation of gene expression, maintenance of genomic integrity, and mRNA or microRNA processing. FUS has extensive literature and strong associations with amyotrophic lateral sclerosis and frontotemporal dementia.
- **Conclusion**: Established evidence supports FUS as a bridge between RNA processing and genome-associated nuclear functions, making it particularly relevant to a brain-containing module. The network does not show that this module is disease-associated or that FUS pathology drives the observed conservation; those would remain hypotheses.

#### IMPDH2

- **Related proteins** (co-abundance neighbors): DDX5 (0.88), EIF3F (0.86), SRP72 (0.85), SUPT16H (0.84), RSL1D1 (0.84), CTPS1 (0.83), PCNA (0.82), FUS (0.81), CCAR1 (0.80); STRING partners: CTPS1 (0.927), GART (0.811)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inosine monophosphate dehydrogenase 2. This gene encodes the rate-limiting enzyme in the de novo guanine nucleotide biosynthesis. It is thus involved in maintaining cellular guanine deoxy- and ribonucleotide pools needed for DNA and RNA synthesis. The encoded protein catalyzes the NAD-dependent oxidation of inosine-5'-monophosphate into xanthine-5'-monophosphate, which is then converted into guanosine-5'-monophosphate. This gene is up-…
- **Diseases (Open Targets)**: acute lymphoblastic leukemia (0.529); Crohn disease (0.447); acute myeloid leukemia (0.421); lupus nephritis (0.408); myelodysplastic syndrome (0.403)
- **Europe PMC papers**: 1438
- **Why important**: IMPDH2 has a relatively central network position and connects DDX5, EIF3F, SRP72, SUPT16H, RSL1D1, CTPS1, PCNA, and FUS. It contributes to primary nucleic-acid binding, RNA-binding, nucleobase biosynthesis, DNA-binding, and broader biosynthetic terms (5 globally significant GO/KEGG terms, q_global 5.43e-09–0.0167; see the table). STRING supports its relationships with CTPS1 and GART. Its established function is rate-limiting control of de novo guanine-nucleotide production, supplying nucleotide pools needed for DNA and RNA synthesis. It has substantial literature and disease associations spanning hematologic disease, inflammatory disease, and neoplasia.
- **Conclusion**: Established evidence supports IMPDH2 as the metabolic component that could meet nucleotide demand created by active transcription and RNA processing. Its placement in the module makes metabolic coupling plausible, but co-abundance alone cannot establish that nucleotide supply limits spliceosome activity in brain or liver.

#### SUPT16H

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.88), LMNB1 (0.86), RSL1D1 (0.85), IMPDH2 (0.84), ALYREF (0.83), SF3A1 (0.82), SRRT (0.82), DDX46 (0.82), HNRNPL (0.82), SNU13 (0.81), MATR3 (0.81), RPL9; RPL9P7; RPL9P8; RPL9P9 (0.80); STRING partners: TCEA1 (0.874)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SPT16 homolog, facilitates chromatin remodeling subunit. Transcription of protein-coding genes can be reconstituted on naked DNA with only the general transcription factors and RNA polymerase II. However, this minimal system cannot transcribe DNA packaged into chromatin, indicating that accessory factors may facilitate access to DNA. One such factor, FACT (facilitates chromatin transcription), interacts specifically with histones H2A/H2B to effect nucle…
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and thin corpus callosum (0.651); HIV infectious disease (0.584); Global developmental delay (0.372); Intellectual disability (0.372); Abnormal corpus callosum morphology (0.370)
- **Europe PMC papers**: 676
- **Why important**: SUPT16H has the strongest network position in the supplied module and connects EFTUD2, LMNB1, RSL1D1, IMPDH2, ALYREF, SF3A1, SRRT, and DDX46. It appears broadly across the primary nucleic-acid binding, gene-expression, RNA-metabolic, nuclear, and biosynthetic terms (14 globally significant GO/KEGG terms, q_global 5.43e-09–0.0448; see the table). STRING links it to TCEA1. Its established annotation identifies it as a FACT complex subunit involved in chromatin remodeling, nucleosome disassembly, and RNA polymerase two transcription elongation. It has substantial literature and developmental or neurological disease associations.
- **Conclusion**: Established evidence supports SUPT16H as a transcriptional and chromatin-access component that can connect nascent transcription to downstream RNA processing. Its network centrality makes it an important candidate coordinator, but causality and direction of regulation remain untested.

## Module 8

**Tissue pair**: brain and liver  
**Genes (8)**: ANXA5, GFPT1, HNRNPK, EIF4G1, IPO4, PKM, NUP85, PTBP1

### Function

This module appears to represent a connected cellular homeostasis program linking RNA processing, translation, central metabolism, nuclear transport, and membrane-associated regulation. The strongest functional interpretation comes from the individual gene annotations and the network topology rather than enrichment: GFPT1 links hexosamine-pathway flux to PKM and NUP85; PTBP1 links HNRNPK and PKM; and IPO4 links GFPT1 with EIF4G1. No GO or KEGG term passed global correction, so there is no globally significant pathway assignment. The supplementary STRING result (STRING PMID (2018) Foot-and-Mouth Disease Virus Counteracts on Internal Ribosome Entry Site Suppression by G3BP1 and Inhibits G3BP1-Mediated Stress Granule Assembly via Post-Translational Mechanisms.; within-query FDR = 0.0389) connects ANXA5, PTBP1, HNRNPK, and EIF4G1 in the context of a viral study, but this is supportive context rather than global enrichment evidence.

**Cell composition.** The module does not have the profile expected for a plasma-protein, secreted-protein, or blood-cell module. Secreted genes are absent, all genes have low immune-cell specificity, and HPA detects protein in both brain and liver for most genes with available data. Most genes have low tissue specificity, although IPO4 is tissue enhanced in testis and PKM is tissue enhanced in skeletal muscle and tongue. Several genes are cell-type enhanced in specialized cell types, but the pattern is not dominated by blood cells. The shared brain-liver signal therefore is more consistent with broadly distributed intracellular proteins, or with shared cellular processes, than with an obvious blood contamination signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports two high-confidence pairwise relationships within the module: HNRNPK with PTBP1 and PKM with PTBP1. The HNRNPK–PTBP1 relationship is especially strong, while the PKM–PTBP1 relationship is also supported. The supplementary STRING term (STRING PMID (2018) Foot-and-Mouth Disease Virus Counteracts on Internal Ribosome Entry Site Suppression by G3BP1 and Inhibits G3BP1-Mediated Stress Granule Assembly via Post-Translational Mechanisms.; within-query FDR = 0.0389) includes ANXA5, PTBP1, HNRNPK, and EIF4G1, but it comes from a virus-related study and should not be treated as proof of a module-wide biological pathway. No hu.MAP complex contains multiple module members. Thus, the network contains a small known RNA-binding interaction core but otherwise has limited support from established physical complexes.

**STRING interactions (score >= 0.7)**: 2 of 28 gene pairs: HNRNPK–PTBP1 (0.997); PKM–PTBP1 (0.88)
**STRING functional enrichment (supplementary, within-query FDR)**: PMID (2018) Foot-and-Mouth Disease Virus Counteracts on Internal Ribosome Entry Site Suppression by G3BP1 and Inhibits G3BP1-Mediated Stress Granule Assembly via Post-Translational Mechanisms. (FDR = 0.0389, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The co-abundance module may be a context-specific association, but it cannot be called a definitively new biological mechanism from these data alone. Its sparse connectivity, absence of a shared hu.MAP complex, and limited STRING support suggest that the complete brain-liver co-abundance pattern is not simply a previously catalogued protein complex. However, absence from STRING or hu.MAP does not establish novelty, because co-abundance relationships can reflect regulation, cell composition, localization, or indirect metabolic coupling. The defensible conclusion is that the module-level association is potentially novel and requires experimental and independent cohort validation.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of gene expression and cellular metabolism in shared brain and liver cell populations. PTBP1 and HNRNPK may form an RNA-processing core, EIF4G1 may connect this regulatory state to translation initiation, and GFPT1 and PKM may couple it to hexosamine-pathway and glycolytic metabolism. IPO4 and NUP85 could connect the state to nuclear import and nucleocytoplasmic transport, while ANXA5 may represent a membrane-associated regulatory arm. This model predicts coordinated changes in RNA processing, translation, and metabolic flux, but the co-abundance data do not establish direct causality or physical assembly.

### Important genes

#### GFPT1

- **Related proteins** (co-abundance neighbors): IPO4 (0.82), PKM (0.81), NUP85 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamine--fructose-6-phosphate transaminase 1. This gene encodes the first and rate-limiting enzyme of the hexosamine pathway and controls the flux of glucose into the hexosamine pathway. The product of this gene catalyzes the formation of glucosamine 6-phosphate. [provided by RefSeq, Sep 2008].
- **Diseases (Open Targets)**: congenital myasthenic syndrome (0.819); neurodegenerative disease (0.559); congenital myasthenic syndromes with glycosylation defect (0.503); spinal stenosis (0.379); congenital disorder of glycosylation type I (0.370)
- **Europe PMC papers**: 1684
- **Why important**: GFPT1 has the highest network connectivity in the module and links IPO4, PKM, and NUP85. It encodes the rate-limiting enzyme of the hexosamine pathway and is annotated for fructose six-phosphate metabolism, UDP-N-acetylglucosamine biosynthesis, and carbohydrate-derivative biosynthesis. Its disease associations include congenital myasthenic syndrome and glycosylation-related disease, and it has substantial literature coverage.
- **Conclusion**: Established evidence supports GFPT1 as the module's main metabolic connector and as a regulator of hexosamine-pathway flux. Its role as a mechanistic bridge to RNA processing or nuclear transport remains a hypothesis generated by the network, not a demonstrated interaction.

#### PTBP1

- **Related proteins** (co-abundance neighbors): HNRNPK (0.86), ANXA5 (0.83); STRING partners: HNRNPK (0.997), PKM (0.88)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypyrimidine tract binding protein 1. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA-binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.505); dengue disease (0.372); open-angle glaucoma (0.330); glaucoma (0.309); neoplasm (0.116)
- **Europe PMC papers**: 4849
- **Why important**: PTBP1 occupies a central position between HNRNPK and ANXA5 and is also connected to PKM through STRING. It is a broadly expressed nuclear RNA-binding protein involved in pre-mRNA processing and alternative splicing. It has the strongest literature volume among the RNA-processing genes in this module and disease associations including neurodevelopmental and neurological disorders. It is also included in the supplementary STRING result (STRING PMID (2018) Foot-and-Mouth Disease Virus Counteracts on Internal Ribosome Entry Site Suppression by G3BP1 and Inhibits G3BP1-Mediated Stress Granule Assembly via Post-Translational Mechanisms.; within-query FDR = 0.0389).
- **Conclusion**: Established evidence supports PTBP1 as a central RNA-processing component and as one of the best-supported interaction hubs in the module. Its apparent coordination with glycolysis and membrane-associated proteins is a plausible module-level hypothesis, but not proof that PTBP1 directly controls those proteins here.

#### PKM

- **Related proteins** (co-abundance neighbors): GFPT1 (0.81), ANXA5 (0.81); STRING partners: PTBP1 (0.88)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyruvate kinase M1/2. This gene encodes a protein involved in glycolysis. The encoded protein is a pyruvate kinase that catalyzes the transfer of a phosphoryl group from phosphoenolpyruvate to ADP, generating ATP and pyruvate. This protein has been shown to interact with thyroid hormone and may mediate cellular metabolic effects induced by thyroid hormones. This protein has been found to bind Opa protein, a bacterial o…
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); autoimmune disorder of central nervous system (0.370); tympanic membrane perforation (0.204); neoplasm (0.121); hepatocellular carcinoma (0.120)
- **Europe PMC papers**: 8544
- **Why important**: PKM connects GFPT1 and ANXA5 in the co-abundance network and has a STRING relationship with PTBP1. It encodes pyruvate kinase involved in glycolysis, ATP generation, and pyruvate production, with additional annotations involving chromatin remodeling and transcriptional regulation. It has the largest literature volume in the module and disease associations including neurodegenerative disease and hepatocellular carcinoma.
- **Conclusion**: Established evidence supports PKM as the principal glycolytic component and a plausible metabolic anchor for the module. Its connection to PTBP1 may indicate coordination between metabolism and RNA regulation, but the available evidence does not establish the direction or mechanism of that coupling.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): PTBP1 (0.86); STRING partners: PTBP1 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is directly connected to PTBP1 by the strongest STRING relationship in the module. It is a nuclear heterogeneous nuclear ribonucleoprotein involved in RNA processing, splicing, transcriptional regulation, and signal transduction. It has disease associations including Au-Kline syndrome and neurodevelopmental disorders, and it has substantial literature coverage. It is also present in the supplementary STRING result (STRING PMID (2018) Foot-and-Mouth Disease Virus Counteracts on Internal Ribosome Entry Site Suppression by G3BP1 and Inhibits G3BP1-Mediated Stress Granule Assembly via Post-Translational Mechanisms.; within-query FDR = 0.0389).
- **Conclusion**: Established evidence supports HNRNPK as part of a known RNA-processing and transcriptional regulatory relationship with PTBP1. Its role as a coordinating hub for the full module is a hypothesis based on co-abundance and network placement rather than a demonstrated multiprotein complex.

#### EIF4G1

- **Related proteins** (co-abundance neighbors): IPO4 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 is connected to IPO4 and provides the module's clearest link to cap-dependent translation initiation. It is a scaffold component of the EIF4F complex that recruits messenger RNA to the ribosome. It has disease associations including late-onset and young-onset Parkinson disease, has substantial literature coverage, and appears in the supplementary STRING result (STRING PMID (2018) Foot-and-Mouth Disease Virus Counteracts on Internal Ribosome Entry Site Suppression by G3BP1 and Inhibits G3BP1-Mediated Stress Granule Assembly via Post-Translational Mechanisms.; within-query FDR = 0.0389).
- **Conclusion**: Established evidence supports EIF4G1 as a translation-initiation scaffold and a biologically meaningful endpoint of the module. Its co-abundance with IPO4 may indicate coordination between translation and nuclear transport, but no direct module-specific mechanism is established.

## Module 9

**Tissue pair**: brain and liver  
**Genes (8)**: B2M, CFH, GMPR2, NDUFV1, NID1, SNTB1, TBC1D24, TIMM9

### Function

No GO/KEGG term passed global correction, and there was no STRING functional enrichment. The module therefore does not support a single statistically established pathway-level function. Its genes span basement-membrane and cell-matrix biology through NID1, complement regulation and innate defense through CFH, purine metabolism through GMPR2, mitochondrial respiration and protein import through NDUFV1 and TIMM9, membrane trafficking and neuronal development through TBC1D24, cytoskeletal membrane association through SNTB1, and MHC class I-associated biology through B2M. The sparse co-abundance structure is consistent with a mixed biological or cellular-composition signal rather than a coherent canonical pathway.

**Cell composition.** The module is not predominantly plasma or secreted: CFH, NID1, and B2M are secreted, while the other genes are not. It is also not predominantly blood-cell enriched, although NID1 has group-enriched monocyte and myeloid dendritic-cell evidence, CFH is immune-cell enhanced, and B2M is enhanced in several immune-related cell types. HPA shows that most genes have cell-type-enhanced expression, with recurring signals in stromal, vascular-associated, hepatic stellate, and neural cell types. Four genes have low tissue specificity, three are tissue enhanced, and one is tissue enriched; liver is the most recurrent enriched tissue. Protein detection is common in both brain and liver. These observations leave open a contribution from shared cell types, stromal or vascular compartments, or sample composition, rather than proving a shared brain-liver intracellular program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no STRING functional enrichment was reported. No hu.MAP complex contained at least two module members. Thus the observed co-abundance edges are not corroborated by the supplied reference interaction or complex resources. The absence of these relationships means the network may capture coordinated expression, indirect biology, tissue or cell-type composition, or context-specific associations; it does not by itself invalidate the module or demonstrate that the relationships are novel molecular interactions.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a new molecular complex or a newly discovered pathway. Its novelty is unresolved: the co-abundance pattern is not supported by known STRING interactions or shared hu.MAP complexes, but absence from those resources is not proof of novelty. The lack of globally significant GO/KEGG terms and the heterogeneous annotations further weaken any claim of a newly defined biological mechanism. A defensible novelty claim would require replication in independent cohorts, control for cell-type composition and blood contamination, comparison with published co-expression modules, and experimental testing of any proposed physical or regulatory relationships.

**Hypothesis.** Hypothesis: the module may reflect coordinated variation in a mixed structural, immune-extracellular, mitochondrial, and neural-cellular milieu shared by brain and liver samples. A possible biological bridge is interaction between extracellular-matrix or complement-related signals from stromal, vascular, or hepatic cells and intracellular energetic, trafficking, or neuronal-state signals from resident neural or other parenchymal cells. This is a hypothesis only; the sparse network, lack of reference interactions, lack of globally significant enrichment, and HPA cell-type patterns do not establish direct mechanistic coupling.

### Important genes

#### CFH

- **Related proteins** (co-abundance neighbors): GMPR2 (0.84), B2M (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement factor H. This gene is a member of the Regulator of Complement Activation (RCA) gene cluster and encodes a protein with twenty short consensus repeat (SCR) domains. This protein is secreted into the bloodstream and has an essential role in the regulation of complement activation, restricting this innate defense mechanism to microbial infections. Mutations in this gene have been associated with hemolytic-ure…
- **Diseases (Open Targets)**: complement factor H deficiency (0.769); age-related macular degeneration (0.750); atypical hemolytic-uremic syndrome (0.729); age related macular degeneration 4 (0.711); Doyne honeycomb retinal dystrophy (0.688)
- **Europe PMC papers**: 9287
- **Why important**: CFH is a central connector in the supplied subgraph, linked to GMPR2 and B2M. It is liver tissue enriched, secreted to blood, and annotated for complement regulation and inflammatory biology. Its disease associations include complement factor H deficiency, age-related macular degeneration, and atypical hemolytic-uremic syndrome, and it has a substantial literature base. It is important because it could represent an extracellular or circulating component of the shared signal.
- **Conclusion**: Established evidence supports CFH as a secreted complement regulator with liver enrichment and disease relevance. It is plausible, but unproven, that CFH contributes to a shared brain-liver inflammatory or extracellular-environment signal; the co-abundance edge does not establish a direct interaction.

#### B2M

- **Related proteins** (co-abundance neighbors): CFH (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Plasma membrane; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: beta-2-microglobulin. This gene encodes a serum protein found in association with the major histocompatibility complex (MHC) class I heavy chain on the surface of nearly all nucleated cells. The protein has a predominantly beta-pleated sheet structure that can form amyloid fibrils in some pathological conditions. The encoded antimicrobial protein displays antibacterial activity in amniotic fluid. A mutation in this gen…
- **Diseases (Open Targets)**: MHC class I deficiency (0.656); diffuse large B-cell lymphoma (0.595); HIV infectious disease (0.532); amyloidosis, hereditary systemic 6 (0.528); AL amyloidosis (0.468)
- **Europe PMC papers**: 25100
- **Why important**: B2M is connected to CFH and is a broadly relevant MHC class I-associated serum protein. HPA places it in multiple immune-related cell types and detects it in both tissues. It has the largest literature volume among the module genes and disease associations involving MHC class I deficiency, lymphoma, HIV infection, and amyloidosis. It is important as a potential immune or sample-composition marker.
- **Conclusion**: Established evidence supports B2M as a broadly expressed MHC class I-associated protein with immune and disease relevance. Its presence may indicate immune, inflammatory, or cellular-composition variation, but it does not demonstrate that the module is an immune pathway.

#### NID1

- **Related proteins** (co-abundance neighbors): SNTB1 (0.83), NDUFV1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nidogen 1. This gene encodes a member of the nidogen family of basement membrane glycoproteins. The protein interacts with several other components of basement membranes, and may play a role in cell interactions with the extracellular matrix. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.425); focal epilepsy (0.259); Hemiparesis (0.259); Hydrocephalus (0.259); placental retention (0.233)
- **Europe PMC papers**: 1838
- **Why important**: NID1 is connected to SNTB1 and NDUFV1 and encodes a basement-membrane glycoprotein involved in cell-matrix adhesion and basement-membrane organization. HPA shows tissue enhancement in placenta, cell-type enhancement in stromal and fibroblast populations, group enrichment in myeloid populations, and secretion to the extracellular matrix. Its disease associations include neurodegenerative disease, focal epilepsy, hemiparesis, hydrocephalus, and placental retention.
- **Conclusion**: Established evidence supports NID1 as an extracellular-matrix and basement-membrane component with stromal and vascular-relevant expression. It could help explain a shared structural or cellular-composition signal, but its connection to the mitochondrial and immune genes is not mechanistically established.

#### NDUFV1

- **Related proteins** (co-abundance neighbors): TBC1D24 (0.82), NID1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit V1. The mitochondrial respiratory chain provides energy to cells via oxidative phosphorylation and consists of four membrane-bound electron-transporting protein complexes (I-IV) and an ATP synthase (complex V). This gene encodes a 51 kDa subunit of the NADH:ubiquinone oxidoreductase complex I; a large complex with at least 45 nuclear and mitochondrial encoded subunits that liberates electrons from NAD…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.788); mitochondrial complex I deficiency, nuclear type 4 (0.724); mitochondrial complex I deficiency, nuclear type 1 (0.685); Leigh syndrome (0.635); type 2 diabetes mellitus (0.609)
- **Europe PMC papers**: 4567
- **Why important**: NDUFV1 connects NID1 and TBC1D24 and encodes a core subunit of mitochondrial respiratory complex I involved in NADH electron transfer and oxidative phosphorylation. It is detected in both brain and liver and is associated with mitochondrial complex I deficiency, Leigh syndrome, and type two diabetes mellitus. Its substantial literature base makes it an informative marker of cellular energetic state.
- **Conclusion**: Established evidence supports NDUFV1 as a mitochondrial respiration gene with disease links to complex I dysfunction. A shared energy-demand or mitochondrial-state component is a reasonable interpretation, but the network does not show that NDUFV1 functionally couples to NID1 or TBC1D24.

#### TBC1D24

- **Related proteins** (co-abundance neighbors): NDUFV1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cell Junctions; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TBC1 domain family member 24. This gene encodes a protein with a conserved domain, referred to as the TBC domain, characteristic of proteins which interact with GTPases. TBC domain proteins may serve as GTPase-activating proteins for a particular group of GTPases, the Rab (Ras-related proteins in brain) small GTPases which are involved in the regulation of membrane trafficking. Mutations in this gene are associated with famili…
- **Diseases (Open Targets)**: DOORS syndrome (0.809); familial infantile myoclonic epilepsy (0.765); rolandic epilepsy-paroxysmal exercise-induced dystonia-writer's cramp syndrome (0.765); autosomal dominant nonsyndromic hearing loss 65 (0.736); autosomal recessive nonsyndromic hearing loss 86 (0.733)
- **Europe PMC papers**: 656
- **Why important**: TBC1D24 connects to NDUFV1 and is associated with Rab-related membrane trafficking, neuronal projection development, dendrite morphogenesis, cilium assembly, and excitatory postsynaptic function. HPA detects it in brain and liver and shows enhancement in several neuronal and glial cell types. Its disease associations include DOORS syndrome, familial infantile myoclonic epilepsy, and hereditary hearing-loss syndromes.
- **Conclusion**: Established evidence supports TBC1D24 as a neuronal membrane-trafficking and developmental regulator with strong neurological disease relevance. It may mark neural-cell state or membrane-trafficking variation in the shared module, while any direct relationship to mitochondrial respiration remains a hypothesis.

#### SNTB1

- **Related proteins** (co-abundance neighbors): NID1 (0.83), TIMM9 (0.82), GMPR2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntrophin beta 1. Dystrophin is a large, rod-like cytoskeletal protein found at the inner surface of muscle fibers. Dystrophin is missing in Duchenne Muscular Dystrophy patients and is present in reduced amounts in Becker Muscular Dystrophy patients. The protein encoded by this gene is a peripheral membrane protein found associated with dystrophin and dystrophin-related proteins. This gene is a member of the syntro…
- **Diseases (Open Targets)**: prostate carcinoma (0.468); type 2 diabetes mellitus (0.454); diabetes mellitus (0.443); ovarian dysfunction (0.383); liver disorder (0.370)
- **Europe PMC papers**: 537
- **Why important**: SNTB1 has the highest connectivity in the supplied subgraph, linking NID1, TIMM9, and GMPR2. It encodes a syntrophin-family peripheral membrane protein associated with dystrophin-related complexes and is annotated with muscle contraction and eye development. HPA shows liver tissue enhancement and cell-type enhancement in several epithelial and specialized cell populations. Its literature and disease-association evidence are more limited than those of CFH or B2M, making its network position especially informative.
- **Conclusion**: Established evidence supports SNTB1 as a membrane-associated cytoskeletal adaptor with the strongest network connectivity in this module. It may act as a marker of coordinated membrane or structural state, but its apparent bridging role is inferred from co-abundance and is not supported by known STRING or hu.MAP relationships.

## Module 10

**Tissue pair**: brain and liver  
**Genes (5)**: CISD1, HIP1R, PHKB, OPLAH, WASHC5

### Function

The module does not have a globally significant GO or KEGG enrichment: no globally significant GO/KEGG term passed global correction. The genes instead point to several distinct cellular processes. HIP1R is associated with endocytosis and actin-cytoskeleton organization; WASHC5 with endosomal transport and actin nucleation; PHKB with glycogen breakdown and carbohydrate metabolism; CISD1 with mitochondrial redox regulation, iron-sulfur biology and autophagy; and OPLAH with glutathione catabolism. The co-abundance pattern therefore appears functionally heterogeneous rather than a clearly defined pathway module. A cautious interpretation is shared regulation of intracellular trafficking, energy or redox-related processes, but this remains inferential rather than enrichment-supported. The absence of an enriched term does not invalidate the module.

**Cell composition.** The module is not dominated by secreted or plasma proteins, because none of the genes is annotated as secreted. It is also not uniformly blood-cell enriched: some genes have immune-cell-enhanced annotations, whereas others have low immune-cell specificity. The HPA profile is mixed, with tissue-enhanced signals involving testis, skeletal muscle and parathyroid gland, and cell-type associations involving oligodendrocyte-lineage cells, enterocytes, gastric or parietal cells and spermatogenic cells. Three proteins are detected in both brain and liver, while the remaining genes lack protein-detection data in those tissues. Thus, the shared module is unlikely to be explained simply by a plasma-protein signal, although shared cell types, tissue composition, or sample-related cellular admixture could contribute to the co-abundance pattern.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The network itself is sparse and centered on HIP1R, which is connected in the co-abundance graph to OPLAH, PHKB and CISD1; WASHC5 connects to OPLAH. These edges are co-abundance relationships, not established physical interactions. No listed gene pair has a high-confidence STRING interaction, STRING functional enrichment is absent, and no hu.MAP complex contains multiple module members. Consequently, the module is not supported as a known protein complex or as a densely documented interaction neighborhood. The lack of STRING and hu.MAP support may indicate a novel association, indirect regulation, tissue-context dependence, or limited database coverage.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is potentially a new cross-tissue co-abundance association, because the observed module structure is not represented by high-confidence STRING interactions or a shared hu.MAP complex. However, that absence alone does not establish biological novelty. The module is small, sparse and composed of genes with heterogeneous established functions, so it could reflect coordinated tissue or cell-state variation rather than a previously unknown molecular complex. The strongest defensible claim is novelty of the observed brain-liver co-abundance pattern, not proof of a new pathway or physical interaction. Independent replication, preservation testing in additional cohorts, and perturbation or biochemical experiments would be needed to establish novelty mechanistically.

**Hypothesis.** Hypothesis: the module may capture a shared cellular state involving endosomal and actin-dependent trafficking, mitochondrial redox control, glutathione handling and glycogen-related energy management in brain and liver samples. HIP1R and WASHC5 could represent trafficking or cytoskeletal components, while CISD1, OPLAH and PHKB could reflect linked metabolic or stress-response consequences. This model is compatible with the co-abundance topology and tissue detection data, but it is not demonstrated by GO, KEGG, STRING or hu.MAP evidence. An alternative hypothesis is that the pattern reflects shared cell-type composition or a broad stress or metabolic state rather than direct pathway coordination.

### Important genes

#### HIP1R

- **Related proteins** (co-abundance neighbors): OPLAH (0.87), PHKB (0.83), CISD1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: huntingtin interacting protein 1 related. Enables several functions, including phosphatidylinositol phosphate binding activity; phosphatidylinositol-3,4-bisphosphate binding activity; and protein homodimerization activity. Involved in several processes, including positive regulation of signal transduction; protein stabilization; and regulation of organelle organization. Located in clathrin-coated vesicle; cytosol; and ruffle membrane. [pr…
- **Diseases (Open Targets)**: Parkinson disease (0.502); neurodegenerative disease (0.370); obesity disorder (0.332); atrial fibrillation (0.308); dermatitis (0.296)
- **Europe PMC papers**: 869
- **Why important**: HIP1R is the central hub of the co-abundance subgraph, connecting to OPLAH, PHKB and CISD1. Its established functions in phosphatidylinositol-phosphate binding, receptor-mediated endocytosis, actin organization and organelle organization provide the strongest candidate link between the otherwise heterogeneous genes. It is detected at the protein level in brain and liver and has substantial disease and literature associations, including neurodegenerative disease and Parkinson disease.
- **Conclusion**: Established evidence supports HIP1R as the network's main trafficking and cytoskeletal coordinator and as a plausible biological anchor for the module. It is only a hypothesis that HIP1R mechanistically drives the co-abundance of the other genes; the available interaction resources do not support direct physical relationships.

#### CISD1

- **Related proteins** (co-abundance neighbors): HIP1R (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CDGSH iron sulfur domain 1. This gene encodes a protein with a CDGSH iron-sulfur domain and has been shown to bind a redox-active [2Fe-2S] cluster. The encoded protein has been localized to the outer membrane of mitochondria and is thought to play a role in regulation of oxidation. Genes encoding similar proteins are located on chromosomes 4 and 17, and a pseudogene of this gene is located on chromosome 2. [provided by RefSe…
- **Diseases (Open Targets)**: neurodegenerative disease (0.539); Abnormality of the integument (0.348); secondary malignant neoplasm (0.306); Parkinson disease (0.296); biliary tract disorder (0.283)
- **Europe PMC papers**: 1042
- **Why important**: CISD1 is directly connected to the module hub and has a mitochondrial outer-membrane location, a redox-active iron-sulfur domain and roles related to oxidation, intracellular iron homeostasis, autophagy and protein maturation. It is detected in both brain and liver and has the largest literature presence among the module genes, together with disease associations involving neurodegeneration and Parkinson disease.
- **Conclusion**: Established evidence supports CISD1 as a mitochondrial redox and stress-response component that could explain part of the shared tissue signal. Its proposed role in coordinating the trafficking and metabolic genes is a hypothesis, not an established interaction or pathway relationship.

#### PHKB

- **Related proteins** (co-abundance neighbors): HIP1R (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphorylase kinase regulatory subunit beta. Phosphorylase kinase is a polymer of 16 subunits, four each of alpha, beta, gamma and delta. The alpha subunit includes the skeletal muscle and hepatic isoforms, encoded by two different genes. The beta subunit is the same in both the muscle and hepatic isoforms, encoded by this gene, which is a member of the phosphorylase b kinase regulatory subunit family. The gamma subunit also includes the ske…
- **Diseases (Open Targets)**: glycogen storage disease IXb (0.756); disorder of glycogen metabolism (0.590); glycogen storage disease IX (0.523); glycogen storage disease XV (0.504); mitochondrial disease (0.425)
- **Europe PMC papers**: 719
- **Why important**: PHKB connects directly to HIP1R and encodes the common beta regulatory subunit of phosphorylase kinase in muscle and hepatic isoforms. Its established relationship to glycogen catabolism and carbohydrate metabolism gives the module a clear energy-storage and energy-mobilization component. It is tissue-enhanced in skeletal muscle and is associated with glycogen storage disorders and other glycogen-metabolism disorders.
- **Conclusion**: Established evidence supports PHKB as a glycogen-regulatory gene and a plausible indicator of energy-metabolic state in the co-abundance pattern. A direct connection between glycogen regulation and the endosomal or mitochondrial genes remains hypothetical.

#### WASHC5

- **Related proteins** (co-abundance neighbors): OPLAH (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WASH complex subunit 5. This gene encodes a 134 kDa protein named strumpellin that is predicted to have multiple transmembrane domains and a spectrin-repeat-containing domain. This ubiquitously expressed gene has its highest expression in skeletal muscle. The protein is named for Strumpell disease; a form of hereditary spastic paraplegia (HSP). Spastic paraplegias are a diverse group of disorders in which the autosomal d…
- **Diseases (Open Targets)**: hereditary spastic paraplegia 8 (0.802); Ritscher-Schinzel syndrome 1 (0.727); Ritscher-Schinzel syndrome (0.711); hereditary disease (0.493); hereditary spastic paraplegia (0.350)
- **Europe PMC papers**: 238
- **Why important**: WASHC5 is connected to OPLAH and is associated with the WASH complex, endosome organization, endosomal transport, actin filament polymerization and Arp2/3-mediated actin nucleation. It is detected in brain and liver, is enhanced in oligodendrocytes, and has strong disease associations with hereditary spastic paraplegia and Ritscher-Schinzel syndrome. Its literature volume is lower than that of the most studied genes but is sufficient to support a well-established trafficking and neurobiology context.
- **Conclusion**: Established evidence supports WASHC5 as a relevant endosomal and actin-remodeling component, especially for the brain aspect of the module. Its connection to OPLAH in this module does not establish a shared complex or direct biochemical mechanism.

#### OPLAH

- **Related proteins** (co-abundance neighbors): HIP1R (0.87), WASHC5 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 5-oxoprolinase, ATP-hydrolysing. The protein encoded by this gene acts as a homodimer, using ATP hydrolysis to catalyze the conversion of 5-oxo-L-proline to L-glutamate. Defects in this gene are a cause of 5-oxoprolinase deficiency (OPLAHD). [provided by RefSeq, Jun 2012].
- **Diseases (Open Targets)**: 5-oxoprolinase deficiency (0.757); inborn errors of metabolism (0.370); autoimmune disorder of central nervous system (0.205); placenta praevia (0.152); late-onset Alzheimers disease (0.139)
- **Europe PMC papers**: 467
- **Why important**: OPLAH is an intermediate connector between HIP1R and WASHC5 in the co-abundance graph. It encodes an ATP-dependent enzyme that converts five-oxoproline to glutamate and is associated with glutathione catabolism and five-oxoprolinase deficiency. Its tissue and cell-type annotations emphasize testis and spermatogenic populations, and it also has immune-cell-enhanced annotations, making it informative for evaluating cellular-composition explanations.
- **Conclusion**: Established evidence supports OPLAH as a glutathione-related metabolic enzyme and as the graph's link between the hub and the WASHC5 branch. The hypothesis that it couples glutathione metabolism to endosomal trafficking in brain and liver is not directly established and should be tested rather than treated as a demonstrated function of the module.

## Module 11

**Tissue pair**: brain and liver  
**Genes (16)**: CKAP4, DHCR24, ERO1A, GALNT2, GAR1, GOSR1, GMPS, LAMB1, IGF2R, P3H1, ALDH18A1, PLIN3, PLOD2, PRKDC, SEC63, TXNDC5

### Function

The module does not have a GO or KEGG term that passes global correction, so its function should not be assigned from enrichment alone. Its architecture instead suggests a heterogeneous cellular homeostasis module connecting mitochondrial and cytosolic metabolism, endoplasmic-reticulum protein folding and translocation, Golgi trafficking, lipid and sterol handling, extracellular-matrix processing, and DNA repair or genome maintenance. ALDH18A1 is the most connected module member and links metabolic, trafficking, sterol, DNA-repair, and ER-associated portions of the network. The P3H1–PLOD2 relationship supports collagen maturation, while ERO1A–TXNDC5 supports ER redox-dependent protein folding. These are biologically coherent substructures, but the sparse cross-functional network and absence of globally significant GO or KEGG enrichment argue against treating the module as a single narrowly defined pathway.

**Cell composition.** The module is not predominantly composed of secreted proteins: the secreted component is a minority, represented most clearly by LAMB1, which is secreted to the extracellular matrix. HPA results indicate that most genes have low tissue specificity, and many are detected in both brain and liver, supporting a broadly expressed cellular program rather than a tissue-exclusive signature. The module is also not strongly blood-cell dominated overall, because most genes have low immune-cell specificity; nevertheless, selected members show enrichment or enhancement in neutrophils, basophils, B-cell or plasmacytoid dendritic-cell populations, and erythrocyte progenitors. Several genes are enhanced in esophageal, placental, pancreatic, adrenal, or reproductive cell types. Therefore, shared cell-type composition, sample admixture, or general cellular stress and biosynthetic activity could contribute to the cross-tissue co-abundance. The weaker liver protein detection for several genes than brain detection also warrants caution when interpreting the module as a liver-intrinsic program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a small set of high-confidence, already known relationships rather than a unified interaction network: ALDH18A1–GMPS, ERO1A–TXNDC5, GAR1–GMPS, IGF2R–PLIN3, and P3H1–PLOD2. These links support nucleotide metabolism, ER redox and folding, lipid-droplet or lysosomal trafficking, and collagen maturation as real biological connections, but STRING reports no supplementary functional enrichment for the module. hu.MAP contributes one complex, (hu.MAP huMAP3_09592.1), containing PRKDC and DHCR24 among many other proteins; this is evidence that those two proteins occur together in a large annotated complex, not evidence that the entire module is one complex. Most module edges are absent from the supplied STRING and hu.MAP evidence, so the co-abundance network adds an expression-level organization that is only partly explained by established physical interactions.

**STRING interactions (score >= 0.7)**: 5 of 120 gene pairs: ALDH18A1–GMPS (0.909); ERO1A–TXNDC5 (0.976); GAR1–GMPS (0.823); IGF2R–PLIN3 (0.986); P3H1–PLOD2 (0.744)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09592.1 (PRKDC, DHCR24; 2/95)

### Novelty

The module should not be called a wholly new biological pathway. Several of its relationships and functions are already established through STRING, hu.MAP, gene annotations, and disease literature, including ER folding, collagen processing, sterol metabolism, nucleotide synthesis, DNA repair, and vesicle trafficking. Its potentially novel aspect is the cross-tissue co-abundance arrangement that places these processes together in brain and liver. However, absence from STRING or hu.MAP does not establish novelty, and the lack of globally significant GO or KEGG enrichment, the sparse network, and the heterogeneous HPA composition make a strong novelty claim premature. Replication in independent brain and liver cohorts, control for cell-type composition, and perturbation or interaction experiments would be needed to establish that this is a reproducible conserved module rather than a mixture of broadly expressed programs.

**Hypothesis.** Hypothesis: the module reflects a coordinated proteostasis and membrane-trafficking state that couples mitochondrial and nucleotide metabolism with ER folding and redox control, sterol and lipid-droplet handling, extracellular-matrix maturation, and genome maintenance. In this model, ALDH18A1-linked metabolic activity may covary with ER and Golgi demand, while TXNDC5 and ERO1A support oxidative folding, P3H1 and PLOD2 support collagen maturation, and DHCR24 and PLIN3 support membrane or lipid homeostasis. PRKDC may represent a genome-maintenance component that is co-regulated with this cellular stress or biosynthetic state rather than being a direct biochemical member of every sub-process. This hypothesis is consistent with the annotations and known interactions but is not demonstrated by the co-abundance data alone.

### Important genes

#### ALDH18A1

- **Related proteins** (co-abundance neighbors): ERO1A (0.86), PRKDC (0.86), IGF2R (0.84), DHCR24 (0.81), GMPS (0.81), GOSR1 (0.81); STRING partners: GMPS (0.909)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 18 family member A1. This gene is a member of the aldehyde dehydrogenase family and encodes a bifunctional ATP- and NADPH-dependent mitochondrial enzyme with both gamma-glutamyl kinase and gamma-glutamyl phosphate reductase activities. The encoded protein catalyzes the reduction of glutamate to delta1-pyrroline-5-carboxylate, a critical step in the de novo biosynthesis of proline, ornithine and arginine. Mutations in …
- **Diseases (Open Targets)**: ALDH18A1-related de Barsy syndrome (0.832); cutis laxa, autosomal dominant 3 (0.816); autosomal recessive complex spastic paraplegia type 9B (0.814); de Barsy syndrome (0.731); autosomal dominant spastic paraplegia type 9 (0.706)
- **Europe PMC papers**: 1168
- **Why important**: ALDH18A1 is the central network connector and links several otherwise weakly connected parts of the module. It encodes a mitochondrial enzyme involved in glutamate-dependent proline, ornithine, and arginine biosynthesis. Its disease associations include de Barsy syndrome and spastic paraplegia-related disorders, and it has substantial literature support. Its HPA profile is tissue and salivary-acinar enhanced, with brain protein detection but not liver detection, so it may be a metabolic anchor without being liver-specific.
- **Conclusion**: Established evidence supports ALDH18A1 as a metabolic enzyme and the principal network connector. It is reasonable to regard it as an organizational candidate for the module, but whether it mechanistically drives the co-abundance pattern is a hypothesis requiring perturbation.

#### PRKDC

- **Related proteins** (co-abundance neighbors): SEC63 (0.87), ALDH18A1 (0.86), DHCR24 (0.83), GALNT2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, liver
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: protein kinase, DNA-activated, catalytic subunit. This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to DNA-PKcs deficiency (0.752); neurodegenerative disease (0.548); severe combined immunodeficiency (0.470); combined immunodeficiency (0.464); ovarian neoplasm (0.210)
- **Europe PMC papers**: 12461
- **Why important**: PRKDC is one of the more connected members and is linked in the module to SEC63, ALDH18A1, DHCR24, and GALNT2. It encodes the catalytic subunit of DNA-dependent protein kinase, with established roles in DNA double-strand-break repair, recombination, telomere maintenance, and innate immune activation. It is also a member of the hu.MAP complex represented by (hu.MAP huMAP3_09592.1), has strong disease relevance through DNA-PK deficiency and immunodeficiency, and has extensive literature support. HPA detects it in both brain and liver.
- **Conclusion**: Established evidence supports PRKDC as a genome-maintenance and DNA-repair factor that is broadly present in the two tissues. Its connection to the module's metabolic and ER components may reflect shared cellular state or co-regulation; a direct mechanistic bridge is not established.

#### DHCR24

- **Related proteins** (co-abundance neighbors): PRKDC (0.83), PLOD2 (0.82), CKAP4 (0.82), ALDH18A1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain, liver
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: 24-dehydrocholesterol reductase. This gene encodes a flavin adenine dinucleotide (FAD)-dependent oxidoreductase which catalyzes the reduction of the delta-24 double bond of sterol intermediates during cholesterol biosynthesis. The protein contains a leader sequence that directs it to the endoplasmic reticulum membrane. Missense mutations in this gene have been associated with desmosterolosis. Also, reduced expression of the gene …
- **Diseases (Open Targets)**: desmosterolosis (0.821); Non-immune hydrops fetalis (0.425); hereditary disease (0.193); digestive system disorder (0.159); schizophrenia (0.112)
- **Europe PMC papers**: 2845
- **Why important**: DHCR24 is a relatively central connector between PRKDC, PLOD2, CKAP4, and ALDH18A1 and is also the second module member in the hu.MAP relationship (hu.MAP huMAP3_09592.1). It is an ER-associated sterol-biosynthesis enzyme that reduces a sterol double bond. Its established disease association is desmosterolosis, and altered expression has been reported in Alzheimer disease temporal cortex. HPA identifies liver and adrenal tissue enhancement and detects protein in both brain and liver.
- **Conclusion**: Established evidence supports DHCR24 as a sterol and membrane-homeostasis factor with relevance to both liver biology and neurological disease. Its placement between metabolic, ER, and collagen-related members makes it a plausible integrator, but the module does not prove that it coordinates those processes.

#### PLOD2

- **Related proteins** (co-abundance neighbors): P3H1 (0.82), DHCR24 (0.82), TXNDC5 (0.82); STRING partners: P3H1 (0.744)
- **HPA**: Low tissue specificity; Cell type enriched; blood Not detected in immune cells; location Nucleoli, Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: procollagen-lysine,2-oxoglutarate 5-dioxygenase 2. The protein encoded by this gene is a membrane-bound homodimeric enzyme that is localized to the cisternae of the rough endoplasmic reticulum. The enzyme (cofactors iron and ascorbate) catalyzes the hydroxylation of lysyl residues in collagen-like peptides. The resultant hydroxylysyl groups are attachment sites for carbohydrates in collagen and thus are critical for the stability of intermolecular…
- **Diseases (Open Targets)**: Bruck syndrome (0.779); osteogenesis imperfecta (0.572); osteoarthritis (0.552); osteoarthritis, hip (0.531); osteoarthritis, knee (0.472)
- **Europe PMC papers**: 3025
- **Why important**: PLOD2 connects P3H1, DHCR24, and TXNDC5 and has a corresponding known STRING relationship with P3H1. It is an ER membrane-associated collagen lysyl hydroxylase required for hydroxylysine formation and collagen crosslink stability. Its annotations include collagen biosynthesis, collagen fibril organization, protein O-linked glycosylation, and hypoxia response, and its disease associations include Bruck syndrome and osteogenesis imperfecta. HPA detects it in both brain and liver and shows pancreatic-acinar cell enrichment.
- **Conclusion**: Established evidence supports PLOD2 as an extracellular-matrix maturation enzyme operating through ER-associated collagen processing. Its module placement suggests a possible link between matrix production, ER proteostasis, and sterol state, but that cross-process interpretation remains hypothetical.

#### TXNDC5

- **Related proteins** (co-abundance neighbors): PLOD2 (0.82), LAMB1 (0.82); STRING partners: ERO1A (0.976)
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Endoplasmic reticulum; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin domain containing 5. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal endoplasmic reticulum (ER)-signal sequence, three catalytically active thioredoxin domains and a C-terminal ER-retention sequence. Its expression is induced by hypoxia and its role ma…
- **Diseases (Open Targets)**: colorectal carcinoma (0.321); spinal stenosis (0.203); neoplasm (0.096); central nervous system cancer (0.092); glioma (0.091)
- **Europe PMC papers**: 1026
- **Why important**: TXNDC5 links PLOD2 and LAMB1 in the module and has a strong known STRING relationship with ERO1A. It is an ER protein-disulfide isomerase with multiple thioredoxin domains, an ER-retention signal, and established roles in protein folding, thiol-disulfide exchange, and protection from hypoxia-associated apoptosis. HPA places it in a group enriched for choroid-plexus epithelial cells and plasma cells and detects it in brain but not liver. Its literature volume and disease associations are moderate compared with the major network hubs.
- **Conclusion**: Established evidence supports TXNDC5 as an ER folding and redox factor that could support collagen and laminin maturation. Its position provides a plausible proteostasis explanation for part of the module, but its absence from liver protein detection and its cell-type associations mean that sample composition must be considered.

## Module 12

**Tissue pair**: brain and liver  
**Genes (6)**: COQ8A, GMDS, DLAT, PDHX, PITRM1, NAE1

### Function

The strongest interpretation is a mitochondrial metabolic module centered on pyruvate dehydrogenase activity and respiratory-chain support. DLAT and PDHX are the clearest functional anchors: both are components of the pyruvate dehydrogenase complex, and their direct high-confidence STRING relationship plus repeated hu.MAP co-membership supports a real connection to pyruvate-to-acetyl-CoA metabolism (STRING Pfam 2-oxoacid dehydrogenases acyltransferase (catalytic domain); within-query FDR = 0.0352)(STRING Pfam e3 binding domain; within-query FDR = 0.0352)(STRING Pfam Biotin-requiring enzyme; within-query FDR = 0.042)(hu.MAP huMAP3_04919.1) (hu.MAP huMAP3_08216.1) (hu.MAP huMAP3_07514.1) (hu.MAP huMAP3_09761.1) (hu.MAP huMAP3_10899.1) (hu.MAP huMAP3_10412.1) (hu.MAP huMAP3_14339.1) (hu.MAP huMAP3_11877.1) (hu.MAP huMAP3_14864.1) (hu.MAP huMAP3_12248.1). COQ8A provides a second mitochondrial axis through ubiquinone biosynthesis and an electron-transferring respiratory-chain-associated protein. PITRM1 contributes mitochondrial proteolysis and transit-peptide processing, while GMDS contributes GDP-fucose biosynthesis and NAE1 contributes protein neddylation and regulatory signaling. No GO or KEGG term passed global correction, so the pathway interpretation is based on gene functions and interaction evidence rather than significant GO/KEGG enrichment. The absence of a globally significant term does not invalidate the module.

**Cell composition.** This does not resemble a plasma-protein, secreted-protein, or blood-cell module. All module genes are non-secreted, all show low immune-cell specificity, and the protein evidence supports detection in both brain and liver for most genes. The HPA tissue patterns are heterogeneous: several genes are enhanced in skeletal muscle or tongue, GMDS is associated with gastrointestinal and salivary tissues, and the remaining genes are broadly or relatively weakly tissue-specific. Cell-type enhancement is also heterogeneous, including neural, glial, adipocyte, cardiomyocyte, and germ-cell annotations. Thus, the shared brain-liver signal is more consistent with conserved intracellular biology, especially mitochondrial metabolism, than with blood contamination or a common secreted compartment. Tissue-enhanced annotations outside brain and liver also caution against treating the module as uniquely brain-liver-specific.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

Known relationships are concentrated in the DLAT-PDHX pair. STRING reports this as a very high-confidence interaction, and the same pair is recovered together across the listed hu.MAP complexes (STRING Pfam 2-oxoacid dehydrogenases acyltransferase (catalytic domain); within-query FDR = 0.0352)(STRING Pfam e3 binding domain; within-query FDR = 0.0352)(STRING Pfam Biotin-requiring enzyme; within-query FDR = 0.042)(hu.MAP huMAP3_04919.1) (hu.MAP huMAP3_08216.1) (hu.MAP huMAP3_07514.1) (hu.MAP huMAP3_09761.1) (hu.MAP huMAP3_10899.1) (hu.MAP huMAP3_10412.1) (hu.MAP huMAP3_14339.1) (hu.MAP huMAP3_11877.1) (hu.MAP huMAP3_14864.1) (hu.MAP huMAP3_12248.1). Those complexes include other pyruvate dehydrogenase components and regulatory kinases, strengthening the interpretation that DLAT and PDHX represent a partial pyruvate dehydrogenase-complex signal. The other module relationships are not supported by STRING partners or hu.MAP complexes in the supplied evidence. Therefore, the network is not a fully documented physical complex: it contains one well-established enzymatic-complex core and additional co-abundance links, particularly involving COQ8A, PITRM1, NAE1, and GMDS, that may reflect shared mitochondrial, metabolic, cellular-state, or tissue-composition regulation rather than direct binding.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: DLAT–PDHX (0.998)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam 2-oxoacid dehydrogenases acyltransferase (catalytic domain) (FDR = 0.0352, 2 genes); Pfam e3 binding domain (FDR = 0.0352, 2 genes); Pfam Biotin-requiring enzyme (FDR = 0.042, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04919.1 (PDHX, DLAT; 2/7); huMAP3_08216.1 (PDHX, DLAT; 2/8); huMAP3_07514.1 (PDHX, DLAT; 2/9); huMAP3_09761.1 (PDHX, DLAT; 2/10); huMAP3_10899.1 (PDHX, DLAT; 2/10); huMAP3_10412.1 (PDHX, DLAT; 2/12); huMAP3_14339.1 (PDHX, DLAT; 2/13); huMAP3_11877.1 (PDHX, DLAT; 2/14); huMAP3_14864.1 (PDHX, DLAT; 2/14); huMAP3_12248.1 (PDHX, DLAT; 2/22)

### Novelty

The module should not be called a newly discovered molecular complex. The DLAT-PDHX relationship and their association with pyruvate dehydrogenase complexes are already established by STRING, hu.MAP, and gene-function evidence. A potentially novel aspect is the cross-tissue co-abundance configuration linking this known pyruvate dehydrogenase pair with COQ8A, PITRM1, NAE1, and GMDS in brain and liver. However, absence of the latter relationships from STRING or hu.MAP does not prove novelty: they may be indirect, context-dependent, or insufficiently characterized. The defensible conclusion is that the network-level co-abundance pattern may be a new observation, whereas its central biochemical anchor is established.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of mitochondrial energy metabolism and proteostasis across brain and liver, with the DLAT-PDHX pyruvate dehydrogenase core coupling glycolytic carbon to mitochondrial acetyl-CoA production, COQ8A supporting respiratory-chain ubiquinone biology, and PITRM1 supporting mitochondrial protein quality control. NAE1 and GMDS may mark broader cellular regulatory or glycosylation-related state changes that covary with this mitochondrial program. This is a mechanistic hypothesis rather than a demonstrated physical pathway for all module members; it should be tested by examining tissue- and cell-resolved expression, perturbing pyruvate dehydrogenase activity, and measuring respiratory function, ubiquinone-related phenotypes, mitochondrial proteolysis, and GDP-fucose biology.

### Important genes

#### DLAT

- **Related proteins** (co-abundance neighbors): PDHX (0.84), PITRM1 (0.80); STRING partners: PDHX (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: huMAP3_04919.1, huMAP3_08216.1, huMAP3_07514.1, huMAP3_09761.1, huMAP3_10899.1, huMAP3_10412.1, huMAP3_14339.1, huMAP3_11877.1, huMAP3_14864.1, huMAP3_12248.1
- **Function (MyGene.info)**: dihydrolipoamide S-acetyltransferase. This gene encodes component E2 of the multi-enzyme pyruvate dehydrogenase complex (PDC). PDC resides in the inner mitochondrial membrane and catalyzes the conversion of pyruvate to acetyl coenzyme A. The protein product of this gene, dihydrolipoamide acetyltransferase, accepts acetyl groups formed by the oxidative decarboxylation of pyruvate and transfers them to coenzyme A. Dihydrolipoamide acety…
- **Diseases (Open Targets)**: pyruvate dehydrogenase E2 deficiency (0.792); pyruvate decarboxylase deficiency (0.711); dystonic disorder (0.374); hereditary disease (0.341); neurodegenerative disease (0.322)
- **Europe PMC papers**: 3481
- **Why important**: DLAT is a central functional anchor because it is the E2 acetyltransferase component of the pyruvate dehydrogenase complex. It has a direct high-confidence STRING relationship with PDHX, appears with PDHX across the hu.MAP complex evidence, is detected in brain and liver, and has substantial literature and disease relevance, including pyruvate dehydrogenase E2 deficiency and neurodegenerative disease associations. Its network position links the module to a well-established mitochondrial enzymatic complex.
- **Conclusion**: Established evidence supports DLAT as a bona fide pyruvate dehydrogenase-complex component and as the strongest metabolic anchor in the module. It is plausible, but not proven, that DLAT co-abundance helps report coordinated mitochondrial carbon oxidation across brain and liver.

#### PDHX

- **Related proteins** (co-abundance neighbors): DLAT (0.84); STRING partners: DLAT (0.998)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: huMAP3_04919.1, huMAP3_08216.1, huMAP3_07514.1, huMAP3_09761.1, huMAP3_10899.1, huMAP3_10412.1, huMAP3_14339.1, huMAP3_11877.1, huMAP3_14864.1, huMAP3_12248.1
- **Function (MyGene.info)**: pyruvate dehydrogenase complex component X. The pyruvate dehydrogenase (PDH) complex is located in the mitochondrial matrix and catalyzes the conversion of pyruvate to acetyl coenzyme A. The PDH complex thereby links glycolysis to Krebs cycle. The PDH complex contains three catalytic subunits, E1, E2, and E3, two regulatory subunits, E1 kinase and E1 phosphatase, and a non-catalytic subunit, E3 binding protein (E3BP). This gene encodes the …
- **Diseases (Open Targets)**: pyruvate dehydrogenase E3-binding protein deficiency (0.793); hereditary disease (0.453); mitochondrial disease (0.445); Leigh syndrome (0.371); ovarian dysfunction (0.269)
- **Europe PMC papers**: 976
- **Why important**: PDHX is the E3-binding component of the pyruvate dehydrogenase complex and directly connects to DLAT in STRING. It recurs with DLAT in all supplied hu.MAP complex records, has a tissue pattern compatible with metabolic specialization, is detected in brain and liver, and has disease associations involving PDHX deficiency, mitochondrial disease, and Leigh syndrome. Its position identifies the known complex core despite its limited number of module links.
- **Conclusion**: Established evidence makes PDHX a strong indicator of pyruvate dehydrogenase-complex biology. The module-level association of PDHX with the other genes is a co-abundance observation; whether PDHX mechanistically regulates those links is unestablished.

#### COQ8A

- **Related proteins** (co-abundance neighbors): NAE1 (0.84), PITRM1 (0.83), GMDS (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coenzyme Q8A. This gene encodes a mitochondrial protein similar to yeast ABC1, which functions in an electron-transferring membrane protein complex in the respiratory chain. It is not related to the family of ABC transporter proteins. Expression of this gene is induced by the tumor suppressor p53 and in response to DNA damage, and inhibiting its expression partially suppresses p53-induced apoptosis. Alternative…
- **Diseases (Open Targets)**: autosomal recessive ataxia due to ubiquinone deficiency (0.841); coenzyme Q10 deficiency (0.636); coenzyme Q10 deficiency, primary, 1 (0.461); hereditary disease (0.401); Abnormality of the skeletal system (0.366)
- **Europe PMC papers**: 397
- **Why important**: COQ8A has the strongest network connectivity in the supplied module and links to NAE1, PITRM1, and GMDS. It is a mitochondrial coenzyme Q biosynthesis-associated protein involved in electron-transfer-related respiratory biology, has neural and skeletal-muscle-relevant HPA patterns, and is strongly associated with recessive ataxia and coenzyme Q deficiency. Its literature base and disease relevance make it an important bridge between the pyruvate dehydrogenase core and broader mitochondrial function.
- **Conclusion**: Established evidence supports COQ8A as a mitochondrial respiratory and ubiquinone-biology gene with important neurological disease relevance. Its bridging position suggests a coordinated mitochondrial program, but a direct functional partnership with DLAT or PDHX is not established by the supplied STRING or hu.MAP evidence.

#### PITRM1

- **Related proteins** (co-abundance neighbors): COQ8A (0.83), DLAT (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pitrilysin metallopeptidase 1. The protein encoded by this gene is an ATP-dependent metalloprotease that degrades post-cleavage mitochondrial transit peptides. The encoded protein binds zinc and can also degrade amyloid beta A4 protein, suggesting a possible role in Alzheimer's disease. [provided by RefSeq, Dec 2016].
- **Diseases (Open Targets)**: spinocerebellar ataxia, autosomal recessive 30 (0.721); mitochondrial DNA depletion syndrome 7 (hepatocerebral type) (0.333); thyroid gland disorder (0.252); skin disorder (0.244); sporadic amyotrophic lateral sclerosis (0.209)
- **Europe PMC papers**: 400
- **Why important**: PITRM1 connects to both COQ8A and DLAT and encodes an ATP-dependent mitochondrial metalloprotease involved in degradation of mitochondrial transit peptides. It is detected in brain and liver, has disease associations with recessive spinocerebellar ataxia and hepatocerebral mitochondrial DNA depletion, and has literature supporting links to amyloid-beta degradation and mitochondrial protein handling. Its network position makes it a plausible proteostasis component adjoining the metabolic genes.
- **Conclusion**: Established evidence supports PITRM1 as a mitochondrial protease with neurological and mitochondrial disease relevance. Its co-abundance with the metabolic core is consistent with coordinated mitochondrial maintenance, but the supplied data do not establish that it physically interacts with DLAT or COQ8A.

#### GMDS

- **Related proteins** (co-abundance neighbors): COQ8A (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GDP-mannose 4,6-dehydratase. GDP-mannose 4,6-dehydratase (GMD; EC 4.2.1.47) catalyzes the conversion of GDP-mannose to GDP-4-keto-6-deoxymannose, the first step in the synthesis of GDP-fucose from GDP-mannose, using NADP+ as a cofactor. The second and third steps of the pathway are catalyzed by a single enzyme, GDP-keto-6-deoxymannose 3,5-epimerase, 4-reductase, designated FX in humans (MIM 137020).[supplied by OMIM, Aug 2009…
- **Diseases (Open Targets)**: open-angle glaucoma (0.497); glaucoma (0.475); Abnormality of the skeletal system (0.474); gastroesophageal reflux disease (0.390); coronary artery disorder (0.373)
- **Europe PMC papers**: 1256
- **Why important**: GMDS is connected to COQ8A and encodes the enzyme initiating GDP-fucose biosynthesis from GDP-mannose. Its HPA profile is enriched in intestinal, salivary, and stomach-related tissues and in mucous or secretory cell types, while protein is detected in brain and liver. It has a substantial literature record and disease associations including glaucoma and skeletal-system abnormalities. It is important because it may represent a non-mitochondrial metabolic or glycosylation-related component of the co-abundance pattern.
- **Conclusion**: Established evidence supports GMDS in GDP-fucose biosynthesis and indicates a tissue pattern distinct from the pyruvate dehydrogenase genes. Its link to COQ8A may reflect shared cellular or tissue state rather than a direct biochemical partnership; any role in the proposed mitochondrial mechanism remains hypothetical.

## Module 13

**Tissue pair**: brain and liver  
**Genes (6)**: CASK, GIMAP4, OPA1, SCO1, SPTBN2, SUCLA2

### Function

This is a small, heterogeneous co-abundance module rather than a confidently assigned canonical pathway. The network is organized around CASK, which connects to SUCLA2, OPA1, SPTBN2, and GIMAP4, while SCO1 connects to GIMAP4. The genes collectively point to several biological themes: neuronal membrane scaffolding and vesicle or postsynaptic organization through CASK and SPTBN2; mitochondrial dynamics and energy metabolism through OPA1, SUCLA2, and SCO1; and immune-associated nucleotide signaling through GIMAP4. However, no GO or KEGG term passed global correction, and STRING reported no supplementary functional enrichment. Therefore, these annotations support a biologically plausible mixed interpretation, not a statistically established common function. The module may reflect coordinated abundance of cell-type or organelle-related proteins across brain and liver rather than one unified biochemical process.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of the genes is annotated as secreted, and all proteins were detected by HPA in both brain and liver. It is also not broadly characterized as a blood-cell module. Most genes have low immune-cell specificity, one gene is immune-cell enriched, and one is not detected in immune cells. HPA instead indicates diverse cell-type associations, including oligodendrocyte progenitor cells, antigen-presenting or macrophage-lineage cells, trophoblasts, spermatids, and several specialized epithelial or neural cell types. Tissue specificity is mixed, with both low-specificity and tissue-enhanced genes. Thus, the shared signal is unlikely to be explained simply by circulating plasma proteins or a uniform blood-cell contaminant, but it could reflect shared cellular composition, mixed cell states, or coordinated abundance of widely distributed mitochondrial and structural proteins.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The observed co-abundance relationships are not supported by high-confidence STRING physical or functional interactions within this module. No hu.MAP complex contains multiple module members. This means that the network should not be interpreted as a known protein complex or as a validated direct interaction map. The central position of CASK is a property of the co-abundance network, whereas the biochemical relationships of the proteins remain largely separate in the supplied interaction resources. The absence of STRING and hu.MAP support does not invalidate the co-abundance pattern; it indicates that the pattern may represent shared regulation, cell composition, organelle abundance, or context-specific coordination rather than established physical binding.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The co-abundance association appears potentially novel as a cross-tissue observation because it is not reproduced as a known STRING interaction set, a hu.MAP complex, or a globally enriched GO or KEGG pathway. Nevertheless, it cannot be called a newly discovered biological mechanism from these data alone. Lack of database support is not evidence of novelty, and the heterogeneous annotations, lack of global enrichment, and mixed HPA cell-type signals leave open explanations based on cell composition, shared expression programs, or dataset-specific measurement effects. The defensible conclusion is that this is a potentially novel module-level association requiring independent replication and experimental testing.

**Hypothesis.** Hypothesis: the module captures a shared abundance program linking neuronal or membrane-cytoskeletal scaffolding with mitochondrial capacity and a context-dependent immune or vesicular component. CASK may act as the network-level bridge between SPTBN2 and the mitochondrial genes OPA1 and SUCLA2, while GIMAP4 may mark a cell-state or vesicle-associated component that connects this structural-metabolic signal to SCO1. In brain and liver, variation in the abundance of particular cell types or in mitochondrial demand could therefore produce the observed co-abundance pattern without requiring direct protein interactions. This hypothesis is not established by the enrichment or interaction evidence and should be tested using cell-resolved expression, mitochondrial state measurements, and independent cohorts.

### Important genes

#### CASK

- **Related proteins** (co-abundance neighbors): SUCLA2 (0.87), OPA1 (0.82), SPTBN2 (0.81), GIMAP4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium/calmodulin dependent serine protein kinase. This gene encodes a calcium/calmodulin-dependent serine protein kinase. The encoded protein is a MAGUK (membrane-associated guanylate kinase) protein family member. These proteins are scaffold proteins and the encoded protein is located at synapses in the brain. Mutations in this gene are associated with FG syndrome 4, intellectual disability and microcephaly with pontine and cerebellar hypoplasia…
- **Diseases (Open Targets)**: syndromic X-linked intellectual disability Najm type (0.829); FG syndrome 4 (0.800); cask-related x-linked intellectual disability (0.667); FG syndrome (0.567); hereditary disease (0.531)
- **Europe PMC papers**: 3838
- **Why important**: CASK is the network hub, connecting to SUCLA2, OPA1, SPTBN2, and GIMAP4. Its established role as a calcium or calmodulin-dependent serine protein kinase and MAGUK scaffold places it at the interface of synaptic organization, membrane-associated signaling, intracellular localization, and protein transport. It has strong disease relevance to syndromic intellectual disability and related neurological disorders, and it has the largest literature volume among the module genes. HPA detects it in both tissues and associates it with oligodendrocyte progenitor cells, with an immune-cell association also reported.
- **Conclusion**: Established evidence supports CASK as the principal network organizer and a neuronal or membrane-scaffold gene. It is plausible, but unproven, that its central co-abundance position links structural or synaptic biology to the mitochondrial and immune-associated genes in this module.

#### OPA1

- **Related proteins** (co-abundance neighbors): CASK (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OPA1 mitochondrial dynamin like GTPase. The protein encoded by this gene is a nuclear-encoded mitochondrial protein with similarity to dynamin-related GTPases. The encoded protein localizes to the inner mitochondrial membrane and helps regulate mitochondrial stability and energy output. This protein also sequesters cytochrome c. Mutations in this gene have been associated with optic atrophy type 1, which is a dominantly inherited optic …
- **Diseases (Open Targets)**: autosomal dominant optic atrophy, classic form (0.846); Behr syndrome (0.812); optic atrophy with or without deafness, ophthalmoplegia, myopathy, ataxia, and neuropathy (0.766); mitochondrial DNA depletion syndrome 14B (cardioencephalomyopathic type) (0.745); optic atrophy (0.653)
- **Europe PMC papers**: 12169
- **Why important**: OPA1 is connected directly to CASK and encodes a mitochondrial dynamin-like GTPase involved in inner-membrane organization, mitochondrial fusion, stability, and energy output. It also sequesters cytochrome c. Its disease associations include dominant optic atrophy, Behr syndrome, and mitochondrial depletion or neurodegenerative disorders. It has the largest literature volume in the module and is detected in both brain and liver.
- **Conclusion**: Established evidence supports OPA1 as a major mitochondrial component of the module and a biologically important contributor to neuronal vulnerability. Its relationship to CASK in this co-abundance network is an association, not evidence of direct interaction or a demonstrated regulatory pathway.

#### SUCLA2

- **Related proteins** (co-abundance neighbors): CASK (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase ADP-forming subunit beta. Succinyl-CoA synthetase (SCS) is a mitochondrial matrix enzyme that acts as a heterodimer, being composed of an invariant alpha subunit and a substrate-specific beta subunit. The protein encoded by this gene is an ATP-specific SCS beta subunit that dimerizes with the SCS alpha subunit to form SCS-A, an essential component of the tricarboxylic acid cycle. SCS-A hydrolyzes ATP to convert succinate t…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome, encephalomyopathic form with methylmalonic aciduria (0.816); mitochondrial DNA depletion syndrome, encephalomyopathic form (0.581); neurodegenerative disease (0.485); mitochondrial disease (0.374); disease of peritoneum (0.372)
- **Europe PMC papers**: 1440
- **Why important**: SUCLA2 is connected to CASK and encodes the ATP-specific beta subunit of succinyl-CoA synthetase, an essential tricarboxylic-acid-cycle enzyme in the mitochondrial matrix. Its annotations directly implicate succinate, succinyl-CoA, malate, and toxic-metabolite processing. Defects cause mitochondrial DNA depletion syndromes with myopathic or encephalomyopathic disease. HPA detects the protein in both tissues and reports enhancement in skeletal muscle and tongue, with additional association with spermatids.
- **Conclusion**: Established evidence supports SUCLA2 as the module's clearest tricarboxylic-acid-cycle and mitochondrial-energy marker. It may indicate coordinated mitochondrial demand in the shared brain-liver signal, but the data do not establish that SUCLA2 functionally regulates CASK or the other module members.

#### SCO1

- **Related proteins** (co-abundance neighbors): GIMAP4 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: synthesis of cytochrome C oxidase 1. Mammalian cytochrome c oxidase (COX) catalyzes the transfer of reducing equivalents from cytochrome c to molecular oxygen and pumps protons across the inner mitochondrial membrane. In yeast, 2 related COX assembly genes, SCO1 and SCO2 (synthesis of cytochrome c oxidase), enable subunits 1 and 2 to be incorporated into the holoprotein. This gene is the human homolog to the yeast SCO1 gene. [provide…
- **Diseases (Open Targets)**: mitochondrial complex IV deficiency, nuclear type 4 (0.782); leigh syndrome due to mitochondrial complex iv deficiency (0.583); mitochondrial complex IV deficiency, nuclear-type (0.543); neurodegenerative disease (0.484); mitochondrial disease (0.372)
- **Europe PMC papers**: 1293
- **Why important**: SCO1 is connected to GIMAP4 and encodes a mitochondrial cytochrome-c-oxidase assembly factor involved in copper homeostasis and respiratory-chain complex IV assembly. Its disease associations include mitochondrial complex IV deficiency and Leigh syndrome, and it has substantial disease and literature support. HPA detects it in both tissues, although its protein location is not assigned in the supplied summary.
- **Conclusion**: Established evidence supports SCO1 as a mitochondrial respiratory-chain assembly gene. Its connection to GIMAP4 is a potentially informative co-abundance bridge, but there is no supplied STRING, hu.MAP, or functional evidence establishing a direct SCO1–GIMAP4 relationship.

#### GIMAP4

- **Related proteins** (co-abundance neighbors): SCO1 (0.82), CASK (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GTPase, IMAP family member 4. This gene encodes a protein belonging to the GTP-binding superfamily and to the immuno-associated nucleotide (IAN) subfamily of nucleotide-binding proteins. The encoded protein of this gene may be negatively regulated by T-cell acute lymphocytic leukemia 1 (TAL1). In humans, the IAN subfamily genes are located in a cluster at 7q36.1. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: metabolic syndrome (0.120); lung adenocarcinoma (0.081); non-alcoholic fatty liver (0.064); Sepsis (0.044); ischemic stroke (0.044)
- **Europe PMC papers**: 495
- **Why important**: GIMAP4 is the module's immune-associated nucleotide-binding protein and is connected to both SCO1 and the CASK hub. It belongs to the IAN family of GTP-binding proteins and is associated by HPA with dendritic, Hofbauer, Kupffer, lymphatic endothelial, and macrophage-lineage cell types, while its tissue profile is enhanced in lymphoid tissue. Its disease literature is more limited than that of the mitochondrial and neuronal genes, but reported associations include metabolic, inflammatory, infectious, and vascular conditions.
- **Conclusion**: Established evidence supports GIMAP4 as a cell-state or immune-associated component rather than as a demonstrated mitochondrial complex member. Its position may reflect shared cell composition or vesicular regulation, and any mechanistic link to SCO1 or CASK remains a hypothesis.

#### SPTBN2

- **Related proteins** (co-abundance neighbors): CASK (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: spectrin beta, non-erythrocytic 2. Spectrins are principle components of a cell's membrane-cytoskeleton and are composed of two alpha and two beta spectrin subunits. The protein encoded by this gene (SPTBN2), is called spectrin beta non-erythrocytic 2 or beta-III spectrin. It is related to, but distinct from, the beta-II spectrin gene which is also known as spectrin beta non-erythrocytic 1 (SPTBN1). SPTBN2 regulates the glutamate s…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 5 (0.799); autosomal recessive spinocerebellar ataxia 14 (0.766); hereditary disease (0.506); cerebellar ataxia (0.438); spinocerebellar ataxia type 14 (0.388)
- **Europe PMC papers**: 767
- **Why important**: SPTBN2 is connected to CASK and encodes beta-III spectrin, a membrane-cytoskeletal protein that supports glutamate-transporter localization, actin organization, vesicle-mediated transport, and postsynaptic specialization. It is enriched in brain and associated with several specialized cell types, while HPA does not detect it in immune cells. Its disease associations include spinocerebellar ataxias, and it has a substantial neurological literature.
- **Conclusion**: Established evidence supports SPTBN2 as the strongest structural and neuronal counterpart to CASK in the module. Its co-abundance with mitochondrial genes could reflect coordinated neuronal maintenance or cell composition, but a direct structural-to-mitochondrial mechanism is not established.

## Module 14

**Tissue pair**: brain and liver  
**Genes (25)**: COPS3, DYNC1I2, DSP, DHX9, FKBP4, GARS1, HSPH1, EIF5, ABCB1, OLA1, QNG1, RAD50, UPF1, PDCD11, SAE1, AARS1, KARS1, NARS2, YARS1, CCT5, CCT3, CCT7, UFD1, UFSP2, UMPS

### Function

The strongest interpretation is a conserved intracellular protein-production, RNA-processing, proteostasis, and genome-maintenance module. Primary global evidence supports ATP-dependent activity and nucleotide binding (GO:MF ATP-dependent activity; q_global = 0.000243) (GO:MF ATP binding; q_global = 0.000441) (GO:MF adenyl ribonucleotide binding; q_global = 0.000494), (8 globally significant GO/KEGG terms, q_global 0.00138–0.00798; see the table), (GO:MF nucleotide binding; q_global = 0.023), (GO:MF nucleoside phosphate binding; q_global = 0.0294), together with translation and protein biosynthesis (GO:BP translation; q_global = 0.0208), (GO:BP protein biosynthetic process; q_global = 0.0208). The module contains a coherent aminoacyl-tRNA synthetase group comprising AARS1, GARS1, KARS1, NARS2, and YARS1, plus EIF5, DHX9, UPF1, and other factors involved in translation, RNA metabolism, or RNA surveillance. A second component is the CCT chaperonin group, CCT3, CCT5, and CCT7, supported by the globally significant chaperonin and ATP-dependent protein-folding terms (GO:CC chaperonin-containing T-complex; q_global = 0.0287), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.0312). RAD50, DHX9, UPF1, and the CCT subunits also support chromosome organization, DNA metabolism, telomere maintenance, and nucleic-acid processing (GO:BP regulation of telomere maintenance; q_global = 0.000869), (GO:BP regulation of chromosome organization; q_global = 0.00591), (7 globally significant GO/KEGG terms, q_global 0.0132–0.0206; see the table), (GO:BP positive regulation of chromosome organization; q_global = 0.0221), (GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.0249), (GO:BP positive regulation of DNA metabolic process; q_global = 0.0308). Thus, the module is best viewed as a general cellular maintenance program linking translation and folding with RNA quality control and genome stability, rather than as a narrowly tissue-specific pathway. The nucleotide-binding terms are broad molecular-function annotations, so they should not by themselves be interpreted as evidence for a single biochemical pathway.

**Cell composition.** This is not predominantly a plasma or secreted-protein module. The HPA summary indicates that only a small minority of genes are secreted, while most have low tissue specificity and low immune-cell specificity. Protein detection is broadly compatible with both brain and liver, supporting a shared intracellular cellular program rather than a brain-only or liver-only specialization. The module is also not dominated by blood-cell-enriched genes: only a small minority show immune-cell enrichment or enhancement, and most are low in immune-cell specificity. Some genes have cell-type-enhanced annotations, especially in reproductive, epithelial, or specialized cell populations, but these do not define the module as a whole. ABCB1 is tissue enhanced in adrenal gland and intestine and is immune-cell enhanced in particular lymphoid populations, while DSP is tissue and epithelial enriched and was not detected in the tested brain and liver samples; these genes may represent peripheral or cellular-context contributions rather than the core conserved program. The shared brain-liver signal therefore is more consistent with broadly expressed housekeeping and stress-maintenance biology than with blood contamination, although sample composition and shared cell types should still be checked experimentally.

**GO/KEGG enrichment**: 36 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF ATP-dependent activity | 0.000243 | ABCB1, CCT3, CCT5, CCT7, DHX9, DYNC1I2, HSPH1, OLA1, RAD50, SAE1, UPF1 |
| GO:MF ATP binding | 0.000441 | AARS1, ABCB1, CCT3, CCT5, CCT7, DHX9, FKBP4, GARS1, HSPH1, KARS1, NARS2, OLA1, RAD50, UPF1, YARS1 |
| GO:MF adenyl ribonucleotide binding | 0.000494 | AARS1, ABCB1, CCT3, CCT5, CCT7, DHX9, FKBP4, GARS1, HSPH1, KARS1, NARS2, OLA1, RAD50, UPF1, YARS1 |
| GO:BP regulation of telomere maintenance | 0.000869 | CCT3, CCT5, CCT7, RAD50, UPF1 |
| GO:MF purine ribonucleoside triphosphate binding | 0.00138 | AARS1, ABCB1, CCT3, CCT5, CCT7, DHX9, EIF5, FKBP4, GARS1, HSPH1, KARS1, NARS2, OLA1, RAD50, UPF1, YARS1 |
| GO:MF purine ribonucleotide binding | 0.00143 | AARS1, ABCB1, CCT3, CCT5, CCT7, DHX9, EIF5, FKBP4, GARS1, HSPH1, KARS1, NARS2, OLA1, RAD50, UPF1, YARS1 |
| GO:MF ribonucleotide binding | 0.00163 | AARS1, ABCB1, CCT3, CCT5, CCT7, DHX9, EIF5, FKBP4, GARS1, HSPH1, KARS1, NARS2, OLA1, RAD50, UPF1, YARS1 |
| GO:MF adenyl nucleotide binding | 0.00302 | AARS1, ABCB1, CCT3, CCT5, CCT7, DHX9, FKBP4, GARS1, HSPH1, KARS1, NARS2, OLA1, RAD50, UPF1, YARS1 |
| GO:MF ATP hydrolysis activity | 0.00509 | ABCB1, CCT3, CCT5, CCT7, DHX9, OLA1, RAD50, UPF1 |
| GO:BP regulation of chromosome organization | 0.00591 | CCT3, CCT5, CCT7, RAD50, UPF1 |
| GO:MF purine nucleotide binding | 0.00667 | AARS1, ABCB1, CCT3, CCT5, CCT7, DHX9, EIF5, FKBP4, GARS1, HSPH1, KARS1, NARS2, OLA1, RAD50, UPF1, YARS1 |
| GO:MF carbohydrate derivative binding | 0.00798 | AARS1, ABCB1, CCT3, CCT5, CCT7, DHX9, EIF5, FKBP4, GARS1, HSPH1, KARS1, NARS2, OLA1, RAD50, UPF1, YARS1 |
| GO:BP telomere maintenance | 0.0132 | CCT3, CCT5, CCT7, RAD50, UPF1 |
| GO:BP RNA-templated DNA biosynthetic process | 0.0149 | CCT3, CCT5, CCT7, RAD50 |
| GO:BP telomere maintenance via telomerase | 0.0149 | CCT3, CCT5, CCT7, RAD50 |

### STRING and hu.MAP

STRING provides strong, established relationships within two conspicuous subnetworks. The aminoacyl-tRNA synthetases AARS1, GARS1, KARS1, NARS2, and YARS1 form a densely connected group, and OLA1 connects to YARS1. CCT3, CCT5, and CCT7 form a tightly connected chaperonin subnetwork. STRING functional annotations independently support ATP and purine-ribonucleotide binding, ATP-dependent activity, nucleic-acid catalysis, RNA activity, protein folding, telomere maintenance, and aminoacyl-tRNA ligase activity (15 supplementary STRING terms; within-query FDR 8.94e-05–0.0159). These STRING terms are supplementary rather than globally corrected primary evidence, but their agreement with the globally significant GO/KEGG terms strengthens the biological interpretation. hu.MAP gives direct complex-level support for the same architecture: AARS1, GARS1, YARS1, and OLA1 occur together in (hu.MAP huMAP3_14442.1), while CCT3, CCT5, and CCT7 recur together across (hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). Additional hu.MAP complexes link AARS1 or YARS1 with RNA, translation, and nuclear regulatory proteins (hu.MAP huMAP3_04783.1) (hu.MAP huMAP3_11534.1) (hu.MAP huMAP3_10302.1) (hu.MAP huMAP3_10115.1) (hu.MAP huMAP3_13998.1). The network therefore contains known molecular complexes and interaction neighborhoods, not merely arbitrary co-abundance edges. At the same time, many module edges lack STRING or hu.MAP support, so co-abundance should not be equated with direct physical interaction.

**STRING interactions (score >= 0.7)**: 14 of 300 gene pairs: AARS1–GARS1 (0.983); AARS1–KARS1 (0.992); AARS1–NARS2 (0.881); AARS1–YARS1 (0.996); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT5–CCT7 (0.999); GARS1–KARS1 (0.915); GARS1–NARS2 (0.837); GARS1–YARS1 (0.989); KARS1–NARS2 (0.852); KARS1–YARS1 (0.988); NARS2–YARS1 (0.956); OLA1–YARS1 (0.824)
**STRING functional enrichment (supplementary, within-query FDR)**: Function ATP binding (FDR = 8.94e-05, 15 genes); Function Purine ribonucleoside triphosphate binding (FDR = 8.94e-05, 16 genes); Function ATP-dependent activity (FDR = 8.94e-05, 10 genes); Function Purine ribonucleotide binding (FDR = 9.54e-05, 16 genes); Keyword ATP-binding (FDR = 0.00015, 14 genes); Keyword Nucleotide-binding (FDR = 0.00043, 15 genes); Function ATP hydrolysis activity (FDR = 0.00093, 7 genes); Function Catalytic activity, acting on a nucleic acid (FDR = 0.00093, 8 genes); Function Catalytic activity, acting on RNA (FDR = 0.0025, 7 genes); Function ATP-dependent protein folding chaperone (FDR = 0.0025, 4 genes); Process Regulation of telomere maintenance (FDR = 0.0061, 5 genes); Function aminoacyl-tRNA ligase activity (FDR = 0.0069, 5 genes); Function Pyrophosphatase activity (FDR = 0.0104, 8 genes); NetworkNeighborAL tRNA Aminoacylation, and glutamyl-tRNA(Gln) amidotransferase complex (FDR = 0.0141, 6 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 0.0159, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (GARS1, AARS1, YARS1, OLA1; 4/57); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_07938.1 (CCT5, CCT3, CCT7; 3/23); huMAP3_06559.1 (CCT5, CCT3, CCT7; 3/25); huMAP3_09191.1 (CCT5, CCT3, CCT7; 3/32); huMAP3_10656.1 (CCT5, CCT3, CCT7; 3/36); huMAP3_14584.1 (CCT5, CCT3, CCT7; 3/61); huMAP3_04783.1 (AARS1, YARS1; 2/4); huMAP3_11534.1 (GARS1, AARS1; 2/5); huMAP3_10302.1 (AARS1, YARS1; 2/9); huMAP3_10115.1 (AARS1, YARS1; 2/14); huMAP3_13998.1 (YARS1, EIF5; 2/23)

### Novelty

The module is unlikely to represent a wholly new molecular system because its central components belong to well-established aminoacyl-tRNA synthetase, CCT chaperonin, RNA surveillance, DNA-repair, and transport biology. The dense STRING and hu.MAP support for the synthetase and CCT portions indicates that substantial parts of the architecture are already known. The potentially novel aspect is the conserved brain-liver co-abundance organization that brings these established components together with ABCB1, DHX9, UPF1, RAD50, SAE1, and proteostasis factors. Novelty therefore should be claimed at the level of the tissue-pair co-abundance configuration and its possible coordination, not at the level of discovering new protein functions or new physical complexes. Absence of an interaction from STRING or hu.MAP is not evidence of novelty, particularly because those resources emphasize experimentally supported or computationally inferred physical and functional relationships rather than cross-tissue abundance coupling. A defensible novelty claim would require replication in independent brain and liver cohorts, control for cell-type composition, and comparison with published cross-tissue co-expression modules.

**Hypothesis.** Hypothesis: this module coordinates the cellular response required to sustain protein synthesis and proteome quality while protecting RNA and chromosome integrity in metabolically active brain and liver cells. Aminoacyl-tRNA synthetases and EIF5 could maintain charging and initiation capacity; CCT3, CCT5, CCT7, and HSPH1 could fold or stabilize newly made proteins; DHX9 and UPF1 could process, export, and surveil RNA; and RAD50 together with SAE1 and related factors could support DNA-damage and telomere responses. ABCB1 may add a membrane transport and xenobiotic-response component, particularly relevant to liver and the brain barrier. The co-abundance pattern may therefore reflect coordinated proteostasis and genome-maintenance demand rather than a single physical complex. This remains a mechanistic hypothesis: the fact sheet demonstrates co-abundance and convergent annotations, but does not establish that these proteins act in one unified pathway, that they regulate one another, or that the module has a causal role in either tissue.

Web sources: https://www.uniprot.org/uniprotkb/P08183/entry; https://www.mdpi.com/2218-273X/14/2/231

### Important genes

#### ABCB1

- **Related proteins** (co-abundance neighbors): UMPS (0.91), YARS1 (0.89), CCT7 (0.86), DSP (0.86), NARS2 (0.86), QNG1 (0.85), FKBP4 (0.84), KARS1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP binding cassette subfamily B member 1. The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily ar…
- **Diseases (Open Targets)**: response to tramadol (0.547); encephalopathy, acute transient (0.416); acute myeloid leukemia (0.391); inflammatory bowel disease (0.390); portal hypertension (0.357)
- **Europe PMC papers**: 20196
- **Why important**: ABCB1 has the strongest network position in the module and connects the intracellular maintenance cluster to genes including YARS1, CCT7, NARS2, KARS1, FKBP4, DSP, UMPS, and QNG1. Established evidence identifies it as an ATP-dependent membrane drug-efflux transporter involved in transmembrane transport, xenobiotic responses, and multidrug resistance. It is detected in both brain and liver, while HPA also reports tissue and cell-type enhancement in intestinal, adrenal, hematopoietic, and selected lymphoid contexts. Its large literature base and disease or therapeutic associations make it an important physiological and confounding anchor.
- **Conclusion**: Established conclusion: ABCB1 is a plausible interface between cellular energy use, membrane transport, and xenobiotic handling, and its co-abundance with the module may reflect shared stress or barrier biology. Hypothesis: ABCB1 may help couple the conserved intracellular maintenance program to tissue-specific exposure and transport demands. The co-abundance data do not establish direct interaction with the other module genes.

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT7 (0.85), DHX9 (0.83), FKBP4 (0.81), CCT3 (0.81), DYNC1I2 (0.80); STRING partners: CCT3 (0.999), CCT7 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_01951.1, huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is a central member of the CCT chaperonin cluster, with module connections to CCT7, CCT3, DHX9, FKBP4, and DYNC1I2. It is present in every globally significant CCT, ATP-dependent folding, chromosome, and telomere-related annotation represented by the CCT group (19 globally significant GO/KEGG terms, q_global 0.000243–0.0206; see the table), (GO:BP positive regulation of chromosome organization; q_global = 0.0221), (GO:MF nucleotide binding; q_global = 0.023), (12 globally significant GO/KEGG terms, q_global 0.0256–0.0312; see the table). STRING directly supports its relationships with CCT3 and CCT7, and hu.MAP repeatedly places the three subunits in CCT-related complexes (hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). Its established function is ATP-dependent folding of proteins including actin and tubulin, with additional annotations involving telomere and Cajal-body biology.
- **Conclusion**: Established conclusion: CCT5 is a strong structural and functional marker of the chaperonin/proteostasis arm of the module. Its disease associations include hereditary sensory and autonomic neuropathy and neurodegenerative disease, but the module does not show that these conditions are involved here. Hypothesis: coordinated CCT5 abundance may buffer translation-associated folding stress in both tissues and may help connect proteostasis to nuclear maintenance.

#### YARS1

- **Related proteins** (co-abundance neighbors): ABCB1 (0.89), GARS1 (0.84), PDCD11 (0.82), FKBP4 (0.82), HSPH1 (0.82), UFD1 (0.82); STRING partners: AARS1 (0.996), GARS1 (0.989), KARS1 (0.988), NARS2 (0.956), OLA1 (0.824)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in brain, liver
- **hu.MAP 3.0**: huMAP3_14442.1, huMAP3_04783.1, huMAP3_10302.1, huMAP3_10115.1, huMAP3_13998.1
- **Function (MyGene.info)**: tyrosyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Tyrosyl-tRNA synthetase belongs to the class I tRNA synthetase family. Cytokine activities have also been observ…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease dominant intermediate C (0.739); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset 2 (0.707); hereditary disease (0.509); Charcot-Marie-Tooth disease (0.418); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset (0.333)
- **Europe PMC papers**: 215
- **Why important**: YARS1 has a high network position and links the synthetase group to ABCB1, FKBP4, HSPH1, UFD1, and PDCD11. It is supported by the dense STRING synthetase relationships and by multiple hu.MAP complexes (hu.MAP huMAP3_14442.1), (hu.MAP huMAP3_04783.1), (hu.MAP huMAP3_10302.1) (hu.MAP huMAP3_10115.1) (hu.MAP huMAP3_13998.1). Its established function is tyrosyl-tRNA aminoacylation for translation, with additional reported stress and starvation responses and cytokine activity after proteolytic processing. It is detected in both brain and liver, has low tissue and immune-cell specificity, and has substantial disease literature including Charcot-Marie-Tooth and multisystem neurological disorders.
- **Conclusion**: Established conclusion: YARS1 is a plausible bridge between the translation machinery and the wider stress, RNA, and protein-quality-control neighborhoods. Its disease associations support biological importance but do not establish that this module causes those disorders. Hypothesis: YARS1 abundance may coordinate translational capacity with stress-responsive functions in the shared brain-liver program.

#### RAD50

- **Related proteins** (co-abundance neighbors): PDCD11 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAD50 double strand break repair protein. The protein encoded by this gene is highly similar to Saccharomyces cerevisiae Rad50, a protein involved in DNA double-strand break repair. This protein forms a complex with MRE11 and NBS1. The protein complex binds to DNA and displays numerous enzymatic activities that are required for nonhomologous joining of DNA ends. This protein, cooperating with its partners, is important for DNA double-stra…
- **Diseases (Open Targets)**: Nijmegen breakage syndrome-like disorder (0.780); cancer (0.593); hereditary neoplastic syndrome (0.579); hereditary breast ovarian cancer syndrome (0.539); breast carcinoma (0.490)
- **Europe PMC papers**: 13311
- **Why important**: RAD50 is the principal explicit DNA-repair and telomere-maintenance gene in the module. It participates in the module network through PDCD11 and is included across the globally significant ATP, chromosome-organization, DNA-metabolism, and telomere terms (4 globally significant GO/KEGG terms, q_global 0.000243–0.000869; see the table), (11 globally significant GO/KEGG terms, q_global 0.00509–0.0206; see the table), (GO:BP positive regulation of chromosome organization; q_global = 0.0221) (GO:MF nucleotide binding; q_global = 0.023) (GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.0249), (GO:MF nucleoside phosphate binding; q_global = 0.0294), (GO:BP positive regulation of DNA metabolic process; q_global = 0.0308). Its established function is as part of the DNA double-strand-break repair machinery with MRE11 and NBS1, including checkpoint activation, recombination, and telomere maintenance. HPA reports a group-enriched pattern in several brain cell types and detection in both brain and liver, while its disease literature includes Nijmegen breakage syndrome-like disorder and cancer-related associations.
- **Conclusion**: Established conclusion: RAD50 gives the module a credible genome-integrity component and is more specific for that interpretation than the broad nucleotide-binding annotations. Hypothesis: RAD50 may indicate that the conserved co-abundance program is engaged when high translational or metabolic activity creates a need for enhanced DNA-damage surveillance. The fact sheet does not demonstrate DNA damage or RAD50-dependent regulation in these tissues.

#### DHX9

- **Related proteins** (co-abundance neighbors): CCT3 (0.86), CCT5 (0.83), UPF1 (0.82), KARS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 occupies a connecting position between the CCT group, UPF1, and KARS1 and is included in globally significant ATP-dependent activity, nucleic-acid catalysis, DNA-metabolism, translation, and protein-metabolism terms (GO:MF ATP-dependent activity; q_global = 0.000243) (GO:MF ATP binding; q_global = 0.000441) (GO:MF adenyl ribonucleotide binding; q_global = 0.000494), (8 globally significant GO/KEGG terms, q_global 0.00138–0.00798; see the table), (7 globally significant GO/KEGG terms, q_global 0.0206–0.0256; see the table), (GO:MF nucleoside phosphate binding; q_global = 0.0294), (GO:BP positive regulation of DNA metabolic process; q_global = 0.0308). Its established function is an ATP-dependent RNA helicase that unwinds RNA and DNA-RNA complexes and contributes to transcriptional regulation, alternative splicing, and RNA export. HPA places it in the nucleoplasm and detects it in both tissues. Its disease associations include intellectual developmental disorder, neurodegenerative disease, and hereditary disease, and its literature volume is substantial.
- **Conclusion**: Established conclusion: DHX9 is a strong candidate for the RNA-processing and nucleic-acid-metabolism arm of the module. Hypothesis: DHX9 may functionally couple RNA surveillance and processing to translation and chaperone demand, helping explain why these otherwise distinct subnetworks co-abundance together. Direct coordination among these module members remains unproven.

## Module 15

**Tissue pair**: brain and liver  
**Genes (5)**: TUFM, MRPL11, MRPS22, YARS2, TIMM44

### Function

This module is strongly associated with mitochondrial gene expression and mitochondrial translation. The primary evidence is the globally corrected enrichment for mitochondrial translation (GO:BP mitochondrial translation; q_global = 0.000784), mitochondrial gene expression (GO:BP mitochondrial gene expression; q_global = 0.00173), and mitochondrial matrix localization (GO:CC mitochondrial matrix; q_global = 0.0229). All module genes are annotated as mitochondrial proteins, and the four genes in (GO:BP mitochondrial translation; q_global = 0.000784) and (GO:BP mitochondrial gene expression; q_global = 0.00173) span mitochondrial ribosomal components, a mitochondrial translation factor, and a mitochondrial tyrosyl-tRNA synthetase. The network therefore represents a coherent mitochondrial protein-expression and translation program rather than a nonspecific association. TIMM44 adds a mitochondrial matrix protein-import component, linking mitochondrial translation to delivery of proteins into the matrix.

**Cell composition.** The module is not composed of plasma proteins, secreted proteins, or blood-cell-enriched proteins. HPA reports no secreted genes and low immune-cell specificity for every gene, arguing against a blood-contamination explanation. All genes have low tissue specificity, consistent with a broadly distributed mitochondrial housekeeping-type program. Protein detection is present for every module gene in the surveyed brain regions, while liver detection is present for most genes. The cell-type annotations are scattered across several cell types rather than concentrated in a shared immune population, so the brain-liver conservation is more plausibly related to a common mitochondrial requirement than to a blood-cell signal. The liver absence of detected YARS2 protein should be treated as an assay or tissue-detection limitation rather than evidence against the module.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP mitochondrial translation | 0.000784 | MRPL11, MRPS22, TUFM, YARS2 |
| GO:BP mitochondrial gene expression | 0.00173 | MRPL11, MRPS22, TUFM, YARS2 |
| GO:CC mitochondrial matrix | 0.0229 | MRPL11, MRPS22, TIMM44, TUFM, YARS2 |

### STRING and hu.MAP

STRING supports a known mitochondrial translation core: MRPL11 is strongly connected to MRPS22 and TUFM, while MRPS22 is strongly connected to TUFM. These relationships agree with the primary GO evidence and the supplementary STRING terms for mitochondrial translation, mitochondrial matrix, translation elongation, and related mitochondrial processes (STRING Process Mitochondrial translation; within-query FDR = 0.00091) through (STRING Component Mitochondrial matrix; within-query FDR = 0.0098). The STRING graph is not complete for the module, because TIMM44 and YARS2 have no listed STRING partners and several possible gene pairs lack STRING support. hu.MAP provides repeated complex-level support for the YARS2–MRPL11 pairing across (hu.MAP huMAP3_04652.1) through (hu.MAP huMAP3_06589.1), but each complex contains many additional proteins and only a small subset of its members is in this module. Thus, the module combines a known mitochondrial ribosome and elongation subnetwork with a mitochondrial import component; it should not be interpreted as a complete physical complex.

**STRING interactions (score >= 0.7)**: 3 of 10 gene pairs: MRPL11–MRPS22 (0.948); MRPL11–TUFM (0.994); MRPS22–TUFM (0.988)
**STRING functional enrichment (supplementary, within-query FDR)**: Process Mitochondrial translation (FDR = 0.00091, 4 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.0035, 5 genes); RCTM Mitochondrial translation elongation (FDR = 0.0047, 3 genes); RCTM Translation (FDR = 0.0079, 4 genes); Component Mitochondrial matrix (FDR = 0.0098, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04652.1 (YARS2, MRPL11; 2/30); huMAP3_06550.1 (YARS2, MRPL11; 2/62); huMAP3_07939.1 (YARS2, MRPL11; 2/68); huMAP3_08458.1 (YARS2, MRPL11; 2/70); huMAP3_09113.1 (YARS2, MRPL11; 2/72); huMAP3_09483.1 (YARS2, MRPL11; 2/74); huMAP3_06589.1 (YARS2, MRPL11; 2/79)

### Novelty

The biological function is not a wholly new discovery: mitochondrial translation, mitochondrial ribosomes, TUFM-dependent elongation, YARS2 aminoacylation, and TIMM44-mediated mitochondrial protein import are established biology. The observed module may nevertheless be a new systems-level finding because it is a conserved co-abundance module shared by brain and liver and combines genes with different kinds of support in existing resources. STRING directly supports only part of the network, and hu.MAP repeatedly supports the YARS2–MRPL11 relationship within much larger complexes. However, the fact that some module edges are absent from STRING or hu.MAP does not establish novelty. The defensible conclusion is that the cross-tissue co-abundance organization may be novel, whereas the underlying mitochondrial functions and several constituent relationships are established.

**Hypothesis.** Hypothesis: the shared brain-liver co-abundance signal reflects coordinated control of mitochondrial gene expression. MRPL11 and MRPS22 may provide ribosomal scaffolding, TUFM may support elongation, and YARS2 may maintain the mitochondrial tRNA supply needed for translation. TIMM44 may couple this translation program to import of nuclear-encoded mitochondrial proteins into the matrix. In tissues with substantial and sustained mitochondrial demand, coordinated regulation of these processes could help maintain respiratory capacity. This is a mechanistic hypothesis, not a demonstrated physical interaction or causal pathway from the co-abundance data alone.

### Important genes

#### MRPS22

- **Related proteins** (co-abundance neighbors): MRPL11 (0.86), TIMM44 (0.83), YARS2 (0.82), TUFM (0.82); STRING partners: MRPL11 (0.948), TUFM (0.988)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial ribosomal protein S22. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: hypotonia with lactic acidemia and hyperammonemia (0.787); 46 XX gonadal dysgenesis (0.631); neurodegenerative disease (0.525); androgenetic alopecia (0.507); hereditary disease (0.495)
- **Europe PMC papers**: 448
- **Why important**: MRPS22 is the most connected node in the module and links MRPL11, TUFM, TIMM44, and YARS2. It occurs in every primary enrichment term (GO:BP mitochondrial translation; q_global = 0.000784), (GO:BP mitochondrial gene expression; q_global = 0.00173), and (GO:CC mitochondrial matrix; q_global = 0.0229), as well as every listed STRING enrichment term (STRING Process Mitochondrial translation; within-query FDR = 0.00091) through (STRING Component Mitochondrial matrix; within-query FDR = 0.0098). Its mitochondrial small-subunit role, strong STRING support with MRPL11 and TUFM, disease associations involving hypotonia with lactic acidemia and hyperammonemia and neurodegenerative disease, and substantial literature make it a central marker of the module.
- **Conclusion**: Established: MRPS22 is a mitochondrial ribosomal protein and a central, well-supported indicator of mitochondrial translation in this module. Hypothesis: its network position could make it an important coordinator or readout of module activity, but causality is not shown by co-abundance.

#### MRPL11

- **Related proteins** (co-abundance neighbors): MRPS22 (0.86); STRING partners: MRPS22 (0.948), TUFM (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: huMAP3_04652.1, huMAP3_06550.1, huMAP3_07939.1, huMAP3_08458.1, huMAP3_09113.1, huMAP3_09483.1, huMAP3_06589.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein L11. This nuclear gene encodes a 39S subunit component of the mitochondial ribosome. Alternative splicing results in multiple transcript variants. Pseudogenes for this gene are found on chromosomes 5 and 12. [provided by RefSeq, May 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.484); type 2 diabetes mellitus (0.300); diabetes mellitus (0.264); bipolar disorder (0.023); asthma (0.019)
- **Europe PMC papers**: 355
- **Why important**: MRPL11 is a mitochondrial large-subunit ribosomal protein and participates in every primary enrichment term (GO:BP mitochondrial translation; q_global = 0.000784), (GO:BP mitochondrial gene expression; q_global = 0.00173), and (GO:CC mitochondrial matrix; q_global = 0.0229). It connects to MRPS22 and TUFM in STRING and is the only partner paired with YARS2 in all listed hu.MAP complexes (hu.MAP huMAP3_04652.1) through (hu.MAP huMAP3_06589.1). It therefore anchors the ribosomal and complex-level interpretation, with disease associations including neurodegenerative and metabolic disease and a substantial literature.
- **Conclusion**: Established: MRPL11 provides a strong mitochondrial-ribosome interpretation and has both STRING and hu.MAP support. Hypothesis: its repeated complex membership may help couple mitochondrial translation machinery to the broader co-abundance program.

#### TUFM

- **Related proteins** (co-abundance neighbors): MRPS22 (0.82); STRING partners: MRPL11 (0.994), MRPS22 (0.988)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Tu translation elongation factor, mitochondrial. This gene encodes a protein which participates in protein translation in mitochondria. Mutations in this gene have been associated with combined oxidative phosphorylation deficiency resulting in lactic acidosis and fatal encephalopathy. A pseudogene has been identified on chromosome 17. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 4 (0.769); neurodegenerative disease (0.502); COVID-19 (0.471); combined oxidative phosphorylation deficiency (0.370); ulcerative colitis (0.303)
- **Europe PMC papers**: 1391
- **Why important**: TUFM is the mitochondrial translation elongation factor in the module and participates in all primary enrichment terms (GO:BP mitochondrial translation; q_global = 0.000784), (GO:BP mitochondrial gene expression; q_global = 0.00173), and (GO:CC mitochondrial matrix; q_global = 0.0229) and all STRING supplementary terms (STRING Process Mitochondrial translation; within-query FDR = 0.00091) through (STRING Component Mitochondrial matrix; within-query FDR = 0.0098). It has very strong STRING relationships with MRPL11 and MRPS22. Its disease associations with combined oxidative phosphorylation deficiency, lactic acidosis, fatal encephalopathy, and neurodegenerative disease give it a direct functional and clinical link to mitochondrial translation failure. It also has the largest literature volume among the module genes.
- **Conclusion**: Established: TUFM is a well-supported mitochondrial translation elongation component and a clinically relevant marker of mitochondrial respiratory dysfunction. Hypothesis: coordinated TUFM abundance may be a rate-limiting readout of translation capacity within the module.

#### YARS2

- **Related proteins** (co-abundance neighbors): TIMM44 (0.89), MRPS22 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_04652.1, huMAP3_06550.1, huMAP3_07939.1, huMAP3_08458.1, huMAP3_09113.1, huMAP3_09483.1, huMAP3_06589.1
- **Function (MyGene.info)**: tyrosyl-tRNA synthetase 2. This gene encodes a mitochondrial protein that catalyzes the attachment of tyrosine to tRNA(Tyr). Mutations in this gene are associated with myopathy with lactic acidosis and sideroblastic anemia type 2 (MLASA2). [provided by RefSeq, Jan 2011].
- **Diseases (Open Targets)**: myopathy, lactic acidosis, and sideroblastic anemia (0.794); mitochondrial disease (0.509); neurodegenerative disease (0.478); hereditary disease (0.452); pericarditis (0.214)
- **Europe PMC papers**: 430
- **Why important**: YARS2 catalyzes mitochondrial tyrosine-tRNA aminoacylation and participates in every primary enrichment term (GO:BP mitochondrial translation; q_global = 0.000784), (GO:BP mitochondrial gene expression; q_global = 0.00173), and (GO:CC mitochondrial matrix; q_global = 0.0229). It connects to MRPS22 and TIMM44 in the module and is the recurring hu.MAP partner of MRPL11 across (hu.MAP huMAP3_04652.1) through (hu.MAP huMAP3_06589.1). Its association with myopathy, lactic acidosis, and sideroblastic anemia and with mitochondrial disease provides strong disease relevance. Its absence of a listed STRING partner contrasts with its repeated hu.MAP support, making it informative for the distinction between co-abundance and established interaction evidence.
- **Conclusion**: Established: YARS2 supplies a required mitochondrial tRNA-aminoacylation function and is supported by enrichment and repeated hu.MAP complex membership. Hypothesis: its linkage to the ribosomal module may reflect coordinated supply of charged tRNA to mitochondrial translation, although a direct physical connection is not established here.

#### TIMM44

- **Related proteins** (co-abundance neighbors): YARS2 (0.89), MRPS22 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translocase of inner mitochondrial membrane 44. This gene encodes a peripheral membrane protein associated with the mitochondrial inner membrane translocase, which functions in the import of proteins across the mitochondrial inner membrane and into the mitochondrial matrix. The encoded protein mediates binding of mitochondrial heat shock protein 70 to the translocase of inner mitochondrial membrane 23 (TIM23) complex. Expression of this gene is…
- **Diseases (Open Targets)**: neurodegenerative disease (0.429); Parkinson disease (0.371); Alzheimer disease (0.370); lysosomal storage disease (0.370); metabolic disease (0.184)
- **Europe PMC papers**: 343
- **Why important**: TIMM44 is the module component that broadens the interpretation beyond translation. It is a mitochondrial inner-membrane translocase-associated protein involved in import into the matrix and appears in the globally corrected matrix term (GO:CC mitochondrial matrix; q_global = 0.0229) and the supplementary matrix terms (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.0035) and (STRING Component Mitochondrial matrix; within-query FDR = 0.0098). It connects to YARS2 and MRPS22 in the module, despite having no listed STRING partner. Its associations with neurodegenerative, Parkinson, Alzheimer, and lysosomal storage disease are relevant to tissues with high mitochondrial dependence.
- **Conclusion**: Established: TIMM44 supports mitochondrial matrix protein import and connects that process to the translation-centered module through co-abundance. Hypothesis: TIMM44 may couple import capacity with mitochondrial protein synthesis, but the data do not demonstrate a direct molecular bridge.

## Module 16

**Tissue pair**: brain and liver  
**Genes (5)**: F12, HEBP1, NUDT12, SHFL, F2

### Function

The clearest established functional signal is a coagulation and extracellular protease axis centered on F2 and F12. F2 encodes thrombin, which participates in fibrin formation, platelet activation, coagulation-factor activation, wound response, and tissue repair. F12 is an extracellular zymogen involved in the plasma kallikrein–kinin cascade, intrinsic coagulation, proteolysis, and plasminogen activation. Their direct STRING relationship and shared kringle-domain annotations (STRING SMART Kringle domain; within-query FDR = 0.0185) (STRING Keyword Kringle; within-query FDR = 0.0381) support this interpretation. NUDT12 is the most connected co-abundance hub and has intracellular nucleotide, NAD-related, RNA, and circadian annotations, while SHFL contributes an interferon-responsive antiviral function and HEBP1 contributes intracellular tetrapyrrole binding and a circadian annotation. However, no GO or KEGG term passed global correction, so the coagulation interpretation is based on the gene annotations, network structure, and supplementary STRING evidence rather than globally significant GO or KEGG enrichment. The module therefore appears functionally mixed, with a strong coagulation component and additional intracellular stress, antiviral, nucleotide, and circadian biology.

**Cell composition.** The module is substantially liver- and hepatocyte-associated according to HPA, with F2 and F12 being secreted blood proteins and both showing liver enrichment. This raises the possibility that part of the shared brain–liver signal reflects circulating plasma proteins, vascular material, or shared sample-associated components rather than a single intracellular pathway operating uniformly in both tissues. The composition is not dominated by secreted proteins: NUDT12, SHFL, and HEBP1 are not annotated as secreted. Blood-cell specificity is generally low, although F12 is immune-cell enhanced in eosinophils, so a broad blood-cell explanation is not sufficient by itself. HPA protein detection is also discordant between tissues: NUDT12 is detected in both brain and liver, SHFL and HEBP1 are detected in brain but not liver, and F2 and F12 show liver-associated or undetected patterns. These observations support caution in interpreting the module as a conserved cellular complex.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING identifies F12–F2 as the only high-confidence relationship among the module genes, and both genes share the supplementary kringle-domain and kringle-keyword signals (STRING SMART Kringle domain; within-query FDR = 0.0185) (STRING Keyword Kringle; within-query FDR = 0.0381). This is consistent with a known biochemical relationship between two circulating coagulation factors and provides a coherent anchor for the module. NUDT12, SHFL, and HEBP1 have no listed STRING partners within the module, so their co-abundance links should not be treated as established physical interactions. No hu.MAP complex contains multiple members of the module. Thus, the network is better viewed as a co-abundance association containing one known coagulation relationship plus tissue- or condition-dependent associations around NUDT12, rather than as a validated multiprotein complex.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: F12–F2 (0.88)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Kringle domain (FDR = 0.0185, 2 genes); Keyword Kringle (FDR = 0.0381, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a novel tissue-pair co-abundance pattern, particularly because it links the established F2–F12 coagulation relationship with NUDT12, SHFL, and HEBP1, which lack listed STRING or hu.MAP support in this module. Nevertheless, absence from STRING or hu.MAP does not establish novelty: the added links may reflect correlated expression, secretion, plasma carryover, shared regulation, or technical and cellular composition effects. The strongest defensible conclusion is that the specific brain–liver co-abundance configuration is not independently validated as a known complex or interaction module, while its coagulation core is clearly not novel.

**Hypothesis.** Hypothesis: the module reflects a liver-associated circulating coagulation signal superimposed on a conserved tissue-state program involving nucleotide and RNA metabolism, antiviral interferon responsiveness, and heme-related or circadian biology. In this model, liver-derived F2 and F12 provide the extracellular coagulation anchor, while NUDT12 tracks a broader intracellular metabolic state and connects the coagulation signal to SHFL and HEBP1 through coordinated regulation rather than proven physical binding. A key alternative hypothesis is that the apparent brain–liver conservation is partly caused by plasma or vascular components in the samples. Testing these alternatives would require cell-type-resolved measurements, matched plasma assessment, and independent validation of the NUDT12–F2, NUDT12–SHFL, and NUDT12–HEBP1 associations.

### Important genes

#### NUDT12

- **Related proteins** (co-abundance neighbors): SHFL (0.88), F2 (0.84), HEBP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in brain, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nudix hydrolase 12. Nucleotides are involved in numerous biochemical reactions and pathways within the cell as substrates, cofactors, and effectors. Nudix hydrolases, such as NUDT12, regulate the concentrations of individual nucleotides and of nucleotide ratios in response to changing circumstances (Abdelraheim et al., 2003 [PubMed 12790796]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.403); Back pain (0.341); crush injury (0.304); diabetes mellitus (0.295); polymyalgia rheumatica (0.290)
- **Europe PMC papers**: 302
- **Why important**: NUDT12 is the central network connector, linking F2 with SHFL and HEBP1 while also having the strongest overall network position in the module. Its annotated roles in nucleotide and NAD-related metabolism, mRNA processing, NAD-cap decapping, and circadian regulation provide a plausible intracellular bridge between otherwise different biological themes. It has moderate literature coverage and disease associations including metabolic disease, but lacks listed STRING partners and lacks a globally significant GO or KEGG assignment.
- **Conclusion**: Established evidence supports NUDT12 as the structural hub and as a nucleotide- and RNA-related enzyme. It is a strong candidate for coordinating the non-coagulation component of the module, but any mechanistic connection to F2, SHFL, or HEBP1 remains a hypothesis based on co-abundance rather than demonstrated interaction.

#### F2

- **Related proteins** (co-abundance neighbors): F12 (0.86), NUDT12 (0.84); STRING partners: F12 (0.88)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coagulation factor II, thrombin. This gene encodes the prothrombin protein (also known as coagulation factor II). This protein is proteolytically cleaved in multiple steps to form the activated serine protease thrombin. The activated thrombin enzyme plays an important role in thrombosis and hemostasis by converting fibrinogen to fibrin during blood clot formation, by stimulating platelet aggregation, and by activating additional …
- **Diseases (Open Targets)**: congenital prothrombin deficiency (0.827); thrombophilia due to thrombin defect (0.738); venous thromboembolism (0.727); deep vein thrombosis (0.690); blood coagulation disease (0.670)
- **Europe PMC papers**: 109299
- **Why important**: F2 is a central functional anchor because it is directly connected to F12 in STRING and is a liver-enriched, hepatocyte-enriched protein secreted into blood. Thrombin has extensive biological and disease literature and is established in thrombosis, hemostasis, platelet activation, tissue repair, angiogenesis, and receptor signaling. Its network position connects the known coagulation pair to NUDT12.
- **Conclusion**: Established evidence identifies F2 as the strongest functional marker of a circulating coagulation component. Its association with NUDT12 is a co-abundance observation, not evidence that thrombin directly regulates NUDT12.

#### F12

- **Related proteins** (co-abundance neighbors): F2 (0.86); STRING partners: F2 (0.88)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coagulation factor XII. This gene encodes coagulation factor XII which circulates in blood as a zymogen. This single chain zymogen is converted to a two-chain serine protease with an heavy chain (alpha-factor XIIa) and a light chain. The heavy chain contains two fibronectin-type domains, two epidermal growth factor (EGF)-like domains, a kringle domain and a proline-rich domain, whereas the light chain contains only a cat…
- **Diseases (Open Targets)**: congenital factor XII deficiency (0.815); hereditary angioedema type 3 (0.777); hereditary angioedema (0.677); peptic ulcer disease (0.450); angioedema (0.407)
- **Europe PMC papers**: 100014
- **Why important**: F12 is directly linked to F2 in STRING and shares the supplementary kringle-domain and kringle-keyword annotations (STRING SMART Kringle domain; within-query FDR = 0.0185) (STRING Keyword Kringle; within-query FDR = 0.0381). It is liver-enriched, secreted to blood, associated with hepatocytes and eosinophils, and has extensive literature on the kallikrein–kinin system, intrinsic coagulation, angioedema, and factor deficiency. It provides the clearest extracellular protease counterpart to F2.
- **Conclusion**: Established evidence supports F12 as a circulating coagulation and proteolysis component of the module. Its brain–liver co-abundance should be interpreted cautiously because its HPA protein pattern does not establish a shared brain-localized cellular role.

#### SHFL

- **Related proteins** (co-abundance neighbors): NUDT12 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: shiftless antiviral inhibitor of ribosomal frameshifting. This gene is an interferon stimulated gene (ISG) that inhibits viral replication. The encoded protein binds nucleic acids and inhibits programmed -1 ribosomal frameshifting required for translation by many RNA viruses. Viruses inhibited by the protein include Zika virus, dengue virus and the coronaviruses, SARS-CoV and SARS-CoV2. [provided by RefSeq, Aug 2021].
- **Diseases (Open Targets)**: Crigler-Najjar syndrome type 2 (0.061); neonatal intrahepatic cholestasis due to citrin deficiency (0.055); hereditary mixed polyposis syndrome (0.053); Rotor syndrome (0.051); progressive familial intrahepatic cholestasis (0.051)
- **Europe PMC papers**: 167
- **Why important**: SHFL is the liver-enhanced and hepatocyte-enhanced member connected to NUDT12, with a nucleoplasmic location and brain protein detection despite lack of liver detection by immunohistochemistry. Its established annotation as an interferon-stimulated antiviral inhibitor of programmed viral ribosomal frameshifting gives the module a plausible innate antiviral dimension. Its literature volume is limited relative to F2 and F12, making it potentially informative but less extensively validated.
- **Conclusion**: Established evidence supports SHFL as an interferon-responsive antiviral factor. Its placement beside NUDT12 may indicate shared regulation or a tissue-state association, but a direct role in the coagulation signal is not established.

#### HEBP1

- **Related proteins** (co-abundance neighbors): NUDT12 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heme binding protein 1. The full-length protein encoded by this gene is an intracellular tetrapyrrole-binding protein. This protein includes a natural chemoattractant peptide of 21 amino acids at the N-terminus, which is a natural ligand for formyl peptide receptor-like receptor 2 (FPRL2) and promotes calcium mobilization and chemotaxis in monocytes and dendritic cells. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.216); Alzheimer disease (0.082); alcohol drinking (0.053); osteonecrosis (0.045); cutaneous melanoma (0.044)
- **Europe PMC papers**: 576
- **Why important**: HEBP1 connects to the NUDT12 hub and is annotated as an intracellular tetrapyrrole-binding protein with a chemotactic peptide function and a circadian biological-process annotation. Its cell-type-enhanced pattern includes enterocytes and erythrocyte progenitors, and its protein is detected in brain but not liver. It has more literature than SHFL but far less than the coagulation factors, and its disease associations are comparatively suggestive rather than definitive.
- **Conclusion**: Established evidence supports HEBP1 as an intracellular heme- or tetrapyrrole-related factor with possible immune-cell signaling relevance. Its module association may reflect metabolic or cellular-state coupling to NUDT12, but any connection to coagulation or brain–liver conservation remains hypothetical.
