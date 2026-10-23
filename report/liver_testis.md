# Conserved co-abundance modules: liver and testis

## Module 0

**Tissue pair**: liver and testis  
**Genes (33)**: PPP2R2A, AIMP1, AIMP2, AKR1B1, AP1M1, CPD, CCAR1, DAZAP1, DNAJB1, TSFM, EIF2B4, FAM98B, GNA13, GOSR1, GCLM, DTYMK, NDUFV1, NUP155, PDHB, PCYT2, PDCD10, NUP210, PPM1G, PSMC6, PSMC4, PSMC2, PSMA1, PSMD13, PSMG1, RCC1, SUCLA2, EPRS1, UFSP2

### Function

The strongest and most coherent interpretation is conserved intracellular proteostasis centered on the proteasome. The module contains a connected proteasome regulatory and accessory subnetwork, with PSMC2, PSMC4, PSMC6, PSMD13, PSMA1, and PSMG1 supported by the globally corrected intracellular-complex and proteasome terms (5 globally significant GO/KEGG terms, q_global 0.00262–0.02; see the table). Proteasome-activating activity is also supported (GO:MF proteasome-activating activity; q_global = 0.0297). The catalytic-complex term (GO:CC catalytic complex; q_global = 0.0221) broadens the interpretation to coordinated macromolecular and metabolic functions, including aminoacylation, translation-related activity, mitochondrial metabolism, phosphatase regulation, and oxidative-stress handling. The spinocerebellar-ataxia pathway (KEGG Spinocerebellar ataxia - Homo sapiens (human); q_global = 0.0377) should be read as pathway membership rather than evidence that the module causes ataxia. Supplementary STRING terms (14 supplementary STRING terms; within-query FDR 0.00075–0.0028) suggest links to cell-cycle control, RNA metabolism, nuclear transport, stress and degradation pathways, but they do not replace the primary globally corrected evidence. Overall, this is best described as a proteasome-centered cellular quality-control module with links to translation, nuclear transport, cell-cycle regulation, and energy metabolism.

**Cell composition.** This does not appear to be a plasma-protein, secreted-protein, or blood-cell module. HPA classifies nearly all members as having low immune-cell specificity, and only AIMP1 is annotated as secreted to blood. The module is therefore unlikely to be explained primarily by plasma carryover or blood-cell contamination. Most members have low tissue specificity, while many show cell-type enhancement in spermatids or spermatocytes. Testis is the most frequent enriched tissue, and late spermatids are the most frequent enriched cell type. Protein detection is broad in both tissues, although several testis-enhanced genes are not detected in liver. These observations support a shared intracellular program that may be particularly active in germ-cell differentiation, rather than a liver-specific secretory program. The presence of broadly expressed housekeeping-like proteasome, translation, mitochondrial, nuclear-pore, and stress-response genes means that part of the shared signal could reflect common cellular machinery or shared cell-state composition.

**GO/KEGG enrichment**: 8 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC intracellular protein-containing complex | 0.00262 | AIMP1, AIMP2, EIF2B4, EPRS1, PSMA1, PSMC2, PSMC4, PSMC6, PSMD13, PSMG1, TSLIG3B |
| GO:CC proteasome regulatory particle | 0.00542 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:CC proteasome accessory complex | 0.00542 | PSMC2, PSMC4, PSMC6, PSMD13 |
| KEGG Proteasome - Homo sapiens (human) | 0.00921 | PSMA1, PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:CC proteasome complex | 0.02 | PSMA1, PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:CC catalytic complex | 0.0221 | AIMP1, AIMP2, EPRS1, GCLM, GNA13, NDUFV1, PDHB, PPP2R2A, PSMA1, PSMC2, PSMC4, PSMC6, PSMD13, SUCLA2, TSLIG3B |
| GO:MF proteasome-activating activity | 0.0297 | PSMC2, PSMC4, PSMC6 |
| KEGG Spinocerebellar ataxia - Homo sapiens (human) | 0.0377 | PSMA1, PSMC2, PSMC4, PSMC6, PSMD13 |

### STRING and hu.MAP

STRING provides strong, direct support for a proteasome core within the module: PSMA1 is connected to PSMC2, PSMC4, PSMC6, PSMD13, and PSMG1, while the ATPase subunits are mutually connected (15 supplementary STRING terms; within-query FDR 0.00036–0.0028). STRING also supports the aminoacyl-tRNA synthetase-associated group through AIMP1, AIMP2, and EPRS1, the nuclear-pore pair NUP155–NUP210, and metabolic links involving PDHB, SUCLA2, and NDUFV1. hu.MAP independently identifies several proteasome complexes containing PSMG1, PSMA1, PSMC2, PSMC4, PSMC6, and PSMD13 (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) (hu.MAP huMAP3_05064.1), an aminoacyl-tRNA synthetase-associated complex containing AIMP1, AIMP2, and EPRS1 (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), and a nuclear-pore complex containing NUP155 and NUP210 (hu.MAP huMAP3_07645.1). Additional hu.MAP complexes connect NUP155 with RCC1 and PPP2R2A with PDCD10 (hu.MAP huMAP3_12581.1) (hu.MAP huMAP3_10333.1) (hu.MAP huMAP3_13510.1). Thus, much of the module recapitulates established physical or functional complexes. The co-abundance network is not simply a de novo physical interaction map: its value is in showing coordinated abundance of several established complexes together with less well-connected metabolic, trafficking, and regulatory genes.

**STRING interactions (score >= 0.7)**: 19 of 528 gene pairs: AIMP1–AIMP2 (0.999); AIMP1–EPRS1 (0.999); AIMP2–EPRS1 (0.999); AP1M1–CPD (0.733); EPRS1–TSFM (0.879); NDUFV1–PDHB (0.738); NUP155–NUP210 (0.991); PDHB–SUCLA2 (0.921); PSMA1–PSMC2 (0.999); PSMA1–PSMC4 (0.999); PSMA1–PSMC6 (0.999); PSMA1–PSMD13 (0.999); PSMA1–PSMG1 (0.935); PSMC2–PSMC4 (0.999); PSMC2–PSMC6 (0.999); PSMC2–PSMD13 (0.999); PSMC4–PSMC6 (0.999); PSMC4–PSMD13 (0.999); PSMC6–PSMD13 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Host Interactions of HIV factors (FDR = 0.00036, 9 genes); RCTM M Phase (FDR = 0.00075, 9 genes); RCTM Mitotic G1 phase and G1/S transition (FDR = 0.0012, 6 genes); RCTM Mitotic Anaphase (FDR = 0.0012, 8 genes); RCTM Metabolism of RNA (FDR = 0.0012, 11 genes); RCTM Disorders of transmembrane transporters (FDR = 0.002, 7 genes); RCTM MAPK6/MAPK4 signaling (FDR = 0.002, 6 genes); RCTM Activation of NF-kappaB in B cells (FDR = 0.0028, 5 genes); RCTM Oxygen-dependent proline hydroxylation of Hypoxia-inducible Factor Alpha (FDR = 0.0028, 5 genes); RCTM Cross-presentation of soluble exogenous antigens (endosomes) (FDR = 0.0028, 5 genes); RCTM Autodegradation of Cdh1 by Cdh1:APC/C (FDR = 0.0028, 5 genes); RCTM SCF-beta-TrCP mediated degradation of Emi1 (FDR = 0.0028, 5 genes); RCTM APC/C:Cdc20 mediated degradation of Securin (FDR = 0.0028, 5 genes); RCTM APC/C:Cdh1 mediated degradation of Cdc20 and other APC/C:Cdh1 targeted proteins in late mitosis/early G1 (FDR = 0.0028, 5 genes); RCTM Cdc20:Phospho-APC/C mediated degradation of Cyclin A (FDR = 0.0028, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09656.1 (PSMG1, PSMA1, PSMC2, PSMC4, PSMC6, PSMD13; 6/64); huMAP3_13725.1 (PSMG1, PSMA1, PSMC2, PSMC4, PSMC6, PSMD13; 6/69); huMAP3_05064.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/31); huMAP3_02637.1 (EPRS1, AIMP1, AIMP2; 3/14); huMAP3_13688.1 (EPRS1, AIMP1, AIMP2; 3/14); huMAP3_07645.1 (NUP155, NUP210; 2/7); huMAP3_00356.1 (PSMG1, PSMA1; 2/33); huMAP3_12581.1 (NUP155, RCC1; 2/58); huMAP3_10333.1 (PPP2R2A, PDCD10; 2/63); huMAP3_13510.1 (PPP2R2A, PDCD10; 2/85)

### Novelty

The proteasome, aminoacylation-associated, and nuclear-pore portions are not novel molecular entities because they are supported by established STRING relationships and hu.MAP complexes (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1) (hu.MAP huMAP3_07645.1) (hu.MAP huMAP3_00356.1) (hu.MAP huMAP3_12581.1). The potentially novel aspect is the cross-tissue co-abundance organization that places these known complexes in one conserved liver–testis module and connects them to mitochondrial metabolism, vesicle trafficking, phosphatase regulation, and germ-cell-enriched programs. The fact that some module members lack STRING partners or hu.MAP assignments does not establish novelty, because database coverage and discovery methods are incomplete. A cautious conclusion is that this is a potentially new systems-level module configuration, not a claim of a newly discovered protein complex or pathway. Demonstrating novelty would require comparison with previously published liver–testis co-abundance modules and independent replication in separate cohorts.

**Hypothesis.** Hypothesis: in both liver and testis, a shared cellular state coordinates proteasome assembly and activity with translation, nuclear transport, mitochondrial energy production, and oxidative-stress control. In testis, this program may support the high protein-folding, remodeling, and quality-control demands of spermatid and spermatocyte development; in liver, it may represent a broadly deployed proteostasis and metabolic-maintenance program. The proteasome core could serve as the central organizing process, while AIMP1–AIMP2–EPRS1, NUP155–NUP210, PDHB–SUCLA2, and regulatory proteins such as PPP2R2A provide parallel translation, transport, energetic, and phosphorylation-control arms. This remains a mechanistic hypothesis: co-abundance and database relationships do not by themselves demonstrate physical assembly, causal regulation, or identical cell-type origins in the two tissues.

### Important genes

#### PSMC2

- **Related proteins** (co-abundance neighbors): CCAR1 (0.89), FAM98B (0.88), SUCLA2 (0.87), GOSR1 (0.85), PSMC6 (0.84), DAZAP1 (0.84), PDCD10 (0.83), NUP210 (0.82), PSMG1 (0.81); STRING partners: PSMA1 (0.999), PSMC4 (0.999), PSMC6 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in liver, testis
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1, huMAP3_05064.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is the highest weighted-degree node in the module and links several otherwise distinct module members. It is a proteasome regulatory-particle ATPase, appears in every primary enrichment term (8 globally significant GO/KEGG terms, q_global 0.00262–0.0377; see the table), has strong STRING connections to the other proteasome members, and is present in multiple hu.MAP proteasome complexes (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) (hu.MAP huMAP3_05064.1). Its disease associations include plasma-cell malignancy, lymphoma, neoplasm, HIV infection, and amyloidosis, with extensive literature support.
- **Conclusion**: Established conclusion: PSMC2 is a central and well-supported proteasome component and is the strongest candidate for the module's structural anchor. Hypothesis: variation in PSMC2 abundance may help coordinate proteasomal capacity with the neighboring metabolic, nuclear, and RNA-related processes.

#### PSMC4

- **Related proteins** (co-abundance neighbors): CCAR1 (0.89), PSMD13 (0.85), DTYMK (0.83); STRING partners: PSMA1 (0.999), PSMC2 (0.999), PSMC6 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in liver, testis
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1, huMAP3_05064.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 4. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.603); mantle cell lymphoma (0.542); neoplasm (0.519); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1065
- **Why important**: PSMC4 is a proteasome regulatory-particle ATPase with broad participation in the primary proteasome and complex terms (8 globally significant GO/KEGG terms, q_global 0.00262–0.0377; see the table). It has strong STRING support with PSMA1, PSMC2, PSMC6, and PSMD13 and occurs in multiple hu.MAP proteasome complexes (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) (hu.MAP huMAP3_05064.1). It is enhanced in several spermatid and spermatocyte populations, making it especially relevant to the testis side of the conserved module. Its disease and literature associations are substantial, including malignancy, viral infection, amyloidosis, and proteostasis-related biology.
- **Conclusion**: Established conclusion: PSMC4 is a conserved proteasome-core regulatory component whose abundance is consistent with the primary functional interpretation. Hypothesis: its germ-cell-associated abundance may reflect increased proteome remodeling or quality-control demand during spermatogenesis.

#### PSMD13

- **Related proteins** (co-abundance neighbors): PSMC4 (0.85), CCAR1 (0.82), NUP210 (0.81), PSMA1 (0.80); STRING partners: PSMA1 (0.999), PSMC2 (0.999), PSMC4 (0.999), PSMC6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1, huMAP3_05064.1
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 is a non-ATPase proteasome regulatory-particle component and is among the most connected proteasome genes in the module. It contributes to the intracellular-complex, proteasome-regulatory, proteasome-accessory, KEGG proteasome, proteasome-complex, catalytic-complex, and spinocerebellar-ataxia terms (6 globally significant GO/KEGG terms, q_global 0.00262–0.0221; see the table) and (KEGG Spinocerebellar ataxia - Homo sapiens (human); q_global = 0.0377). It has strong STRING links to PSMA1 and the PSMC ATPases and is included in the proteasome complexes (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) (hu.MAP huMAP3_05064.1). Its disease associations include plasma-cell malignancy, lymphoma, neurodegenerative disease, neoplasm, and HIV infection.
- **Conclusion**: Established conclusion: PSMD13 provides an independently annotated non-ATPase arm of the proteasome signal and strengthens the interpretation that the module reflects an assembled regulatory particle rather than isolated proteasome transcripts. Hypothesis: PSMD13 may help couple proteasome abundance to nuclear or stress-responsive processes in the shared tissue state.

#### PSMG1

- **Related proteins** (co-abundance neighbors): AIMP1 (0.85), GOSR1 (0.83), PSMC2 (0.81); STRING partners: PSMA1 (0.935)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1, huMAP3_00356.1
- **Function (MyGene.info)**: proteasome assembly chaperone 1. Enables molecular adaptor activity. Involved in chaperone-mediated protein complex assembly. Located in several cellular components, including Golgi apparatus; endoplasmic reticulum; and nucleoplasm. Part of chaperone complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.541); intelligence (0.326); smoking initiation (0.322); atrial fibrillation (0.312); attention deficit-hyperactivity disorder (0.240)
- **Europe PMC papers**: 358
- **Why important**: PSMG1 is a proteasome assembly chaperone, connects the proteasome neighborhood to AIMP1 and GOSR1 in the module network, and is represented in the intracellular-complex term (GO:CC intracellular protein-containing complex; q_global = 0.00262). It is supported by STRING with PSMA1 and by several hu.MAP proteasome complexes (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1), and (hu.MAP huMAP3_00356.1). HPA shows testis tissue enhancement and enhancement in early spermatids, late primary spermatocytes, and oocytes. Its disease associations include neurodegenerative disease and neurodevelopmental traits, with a meaningful but smaller literature base than the major proteasome subunits.
- **Conclusion**: Established conclusion: PSMG1 is a plausible assembly-related component of the proteasome signal and provides testis-relevant context. Hypothesis: PSMG1 may be particularly important for maintaining proteasome assembly during germ-cell differentiation, although the module does not prove that it is the tissue-specific driver.

#### AIMP1

- **Related proteins** (co-abundance neighbors): DTYMK (0.87), GOSR1 (0.85), PSMG1 (0.85), EIF2B4 (0.84), PPM1G (0.82); STRING partners: AIMP2 (0.999), EPRS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver, testis
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: aminoacyl tRNA synthetase complex interacting multifunctional protein 1. The protein encoded by this gene is a cytokine that is specifically induced by apoptosis, and it is involved in the control of angiogenesis, inflammation, and wound healing. The release of this cytokine renders the tumor-associated vasculature sensitive to tumor necrosis factor. The precursor protein is identical to the p43 subunit, which is associated with the multi-tRNA synthetase complex, and i…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 3 (0.790); Pelizaeus-Merzbacher-like disease (0.657); POLR-related leukodystrophy (0.657); leukodystrophy (0.372); autosomal recessive non-syndromic intellectual disability (0.371)
- **Europe PMC papers**: 663
- **Why important**: AIMP1 has an intermediate network position and connects to AIMP2, EPRS1, EIF2B4, and other module genes. It belongs to the globally significant intracellular-complex and catalytic-complex terms (GO:CC intracellular protein-containing complex; q_global = 0.00262) and (GO:CC catalytic complex; q_global = 0.0221), and it forms established STRING and hu.MAP relationships with AIMP2 and EPRS1 (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). Its annotated functions span the aminoacyl-tRNA synthetase complex, translation, angiogenesis, inflammation, wound healing, and cell signaling. It is the only module member annotated as secreted to blood, and it has disease associations involving leukodystrophy and related neurological disorders.
- **Conclusion**: Established conclusion: AIMP1 is an important bridge between the proteostasis module and the aminoacylation-associated complex, while its secretion annotation warrants attention to possible extracellular contributions. Hypothesis: the module may coordinate intracellular translation machinery with stress or tissue-remodeling signals involving AIMP1, but the available evidence does not show that secreted AIMP1 drives the module.

#### NUP155

- **Related proteins** (co-abundance neighbors): CPD (0.85), PDHB (0.85); STRING partners: NUP210 (0.991)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07645.1, huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 155. Nucleoporins are proteins that play an important role in the assembly and functioning of the nuclear pore complex (NPC) which regulates the movement of macromolecules across the nuclear envelope (NE). The protein encoded by this gene plays a role in the fusion of NE vesicles and formation of the double membrane NE. The protein may also be involved in cardiac physiology and may be associated with t…
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); atrial fibrillation (0.470); familial atrial fibrillation (0.390)
- **Europe PMC papers**: 944
- **Why important**: NUP155 links the module to nuclear-envelope and nucleocytoplasmic-transport biology. It forms a strong STRING relationship with NUP210 and is represented in hu.MAP nuclear-pore complexes, including the complex containing NUP155 and NUP210 (hu.MAP huMAP3_07645.1) and the complex connecting NUP155 with RCC1 (hu.MAP huMAP3_12581.1). HPA shows testis tissue enrichment and late-spermatid enhancement. Its annotated functions include nuclear-envelope organization, RNA export, protein import, and nucleocytoplasmic transport, and its disease associations include atrial fibrillation and viral infection.
- **Conclusion**: Established conclusion: NUP155 is evidence that the module extends beyond proteasomal degradation into nuclear transport and envelope organization, with particular relevance to testis. Hypothesis: coordinated abundance of NUP155 and the proteasome could support coupling between nuclear transport, RNA handling, and selective protein turnover during germ-cell maturation.

## Module 1

**Tissue pair**: liver and testis  
**Genes (25)**: SERPINA3, FDXR, C9, DRG2, GFM1, ELP1, FUS, GCLC, IGHA1, ITIH4, ME1, NSF, OPA1, PANK4, PDCD6IP, PPM1B, SEC23A, SEC24D, AARS1, SYNE2, TRIM25, UGGT1, USO1, WASHC4, WASHC5

### Function

The module does not support a single pathway assignment from GO or KEGG: no GO or KEGG term passed global correction. Its strongest interpretable structure is a mixed intracellular logistics and secretory-homeostasis program. SEC23A, SEC24D, and USO1 support COPII-dependent endoplasmic-reticulum-to-Golgi transport, while WASHC4 and WASHC5 support endosomal transport and actin-linked membrane remodeling. These relationships are reinforced by the module graph and by hu.MAP complexes (hu.MAP huMAP3_12394.1), (hu.MAP huMAP3_05454.1), and (hu.MAP huMAP3_00065.1) through (hu.MAP huMAP3_10870.1). A second component consists of liver-associated extracellular proteins, including ITIH4, SERPINA3, C9, and IGHA1, alongside intracellular redox, mitochondrial, translation, and metabolic genes such as GCLC, ME1, GFM1, FDXR, and AARS1. The module is therefore best interpreted as a shared abundance program combining vesicle and membrane trafficking with hepatic secretory output, cellular stress protection, and general biosynthetic maintenance, rather than as a validated single biochemical pathway.

**Cell composition.** This is not predominantly a plasma or secreted module, because most genes have low tissue specificity and are intracellular. Nevertheless, a conspicuous subset is secreted to blood or represents extracellular plasma-associated proteins: ITIH4, C9, and SERPINA3 are secreted, and IGHA1 is an immunoglobulin gene associated with plasma cells and B-cell populations. The HPA data also show liver enrichment for several genes and broad protein detection in both liver and testis, which is compatible with a shared housekeeping or secretory background rather than a strictly testis-specific program. Blood-cell contamination or shared immune-related material is possible for part of the signal, especially around IGHA1 and genes with immune-cell enhancement, but the HPA summary does not indicate that blood-cell-enriched genes dominate the module. The module should therefore be interpreted cautiously as a mixture of broadly expressed cellular machinery, liver-derived extracellular proteins, and tissue or cell-type contributions.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The high-confidence STRING relationships are concentrated in a few coherent pairs and bridges: SEC23A with SEC24D, USO1 with NSF, SEC23A with USO1, SEC24D with USO1, and WASHC4 with WASHC5. These are established relationships consistent with COPII transport, Golgi trafficking, vesicle fusion, and WASH-complex function. The hu.MAP evidence independently supports a SEC23A-SEC24D-containing COPII group (hu.MAP huMAP3_00065.1) through (hu.MAP huMAP3_13535.1), a WASHC4-WASHC5 group (hu.MAP huMAP3_05454.1) and (hu.MAP huMAP3_06652.1) through (hu.MAP huMAP3_10870.1), and a broader trafficking complex containing USO1, SEC23A, and SEC24D (hu.MAP huMAP3_12394.1). It also places ITIH4 and SERPINA3 together in extracellular or plasma-associated complexes (hu.MAP huMAP3_09434.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1), and (hu.MAP huMAP3_10678.1), while FDXR and GFM1 recur in mitochondrial or metabolic complexes (hu.MAP huMAP3_10525.1) and (hu.MAP huMAP3_13468.1). Thus, part of the module recapitulates known physical machinery, whereas the full module is not represented by one demonstrated complex. The sparse STRING structure and the mixture of intracellular and extracellular proteins suggest that co-abundance links extend beyond direct physical binding.

**STRING interactions (score >= 0.7)**: 5 of 300 gene pairs: NSF–USO1 (0.832); SEC23A–SEC24D (0.999); SEC23A–USO1 (0.704); SEC24D–USO1 (0.751); WASHC4–WASHC5 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12394.1 (USO1, SEC24D, SEC23A; 3/98); huMAP3_05454.1 (WASHC5, WASHC4; 2/2); huMAP3_00065.1 (SEC24D, SEC23A; 2/4); huMAP3_00707.1 (SEC24D, SEC23A; 2/4); huMAP3_07775.1 (SEC24D, SEC23A; 2/5); huMAP3_06453.1 (SEC24D, SEC23A; 2/6); huMAP3_09282.1 (SEC24D, SEC23A; 2/6); huMAP3_11128.1 (SEC24D, SEC23A; 2/8); huMAP3_11237.1 (SEC24D, SEC23A; 2/12); huMAP3_13535.1 (SEC24D, SEC23A; 2/14); huMAP3_06652.1 (WASHC5, WASHC4; 2/14); huMAP3_08077.1 (WASHC5, WASHC4; 2/16); huMAP3_10870.1 (WASHC5, WASHC4; 2/20); huMAP3_09434.1 (SERPINA3, ITIH4; 2/33); huMAP3_10525.1 (FDXR, GFM1; 2/33); huMAP3_09531.1 (SERPINA3, ITIH4; 2/47); huMAP3_10101.1 (SERPINA3, ITIH4; 2/49); huMAP3_12900.1 (WASHC5, WASHC4; 2/50); huMAP3_15040.1 (SERPINA3, ITIH4; 2/64); huMAP3_10678.1 (SERPINA3, ITIH4; 2/71); huMAP3_13468.1 (FDXR, GFM1; 2/99)

### Novelty

The module-level finding may be novel as a conserved liver-testis co-abundance pattern, but the available evidence does not establish that it is a new molecular complex or a new pathway. Several internal relationships are already well known through STRING and hu.MAP, particularly the COPII, Golgi, WASH, extracellular plasma-associated, and mitochondrial groupings. Conversely, the absence of a complete matching entry in STRING or hu.MAP cannot prove novelty, because those resources primarily capture physical interactions and curated complexes rather than tissue-pair-specific co-abundance modules. A defensible conclusion is that the module contains known biological components arranged in a potentially new cross-tissue abundance configuration. Replication in independent liver and testis cohorts, control for plasma and immune-cell contribution, and comparison with existing co-expression resources would be required before claiming a novel conserved module.

**Hypothesis.** Hypothesis: the module reflects coordinated maintenance of secretory and membrane-trafficking capacity in liver and testis, with COPII export through SEC23A and SEC24D, Golgi tethering and fusion through USO1 and NSF, and endosomal actin remodeling through WASHC4 and WASHC5. In liver, this machinery may be coupled to production or handling of extracellular proteins such as ITIH4, SERPINA3, and C9. In testis, the same trafficking and membrane-remodeling capacity may support specialized secretory or cellular remodeling demands, while broadly expressed genes such as GCLC, GFM1, and OPA1 provide redox, translational, and mitochondrial support. The apparent conservation may therefore arise from shared cellular infrastructure combined with tissue-specific secretory load, rather than from one tissue-specific signaling pathway. This is a mechanistic hypothesis and is not directly demonstrated by the supplied enrichment results.

### Important genes

#### SEC23A

- **Related proteins** (co-abundance neighbors): PDCD6IP (0.82); STRING partners: SEC24D (0.999), USO1 (0.704)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_12394.1, huMAP3_00065.1, huMAP3_00707.1, huMAP3_07775.1, huMAP3_06453.1, huMAP3_09282.1, huMAP3_11128.1, huMAP3_11237.1, huMAP3_13535.1
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A is a central mechanistic anchor for the trafficking interpretation. It connects to PDCD6IP in the module graph and has STRING support with SEC24D and USO1. It recurs across multiple hu.MAP complexes (hu.MAP huMAP3_12394.1) and (hu.MAP huMAP3_00065.1) through (hu.MAP huMAP3_13535.1), all consistent with COPII assembly or related trafficking machinery. Its established function is ER cargo loading and COPII-coated vesicle budding, and it has a disease association with craniolenticulosutural dysplasia. Its literature base is substantial enough to make it a well-established rather than speculative anchor.
- **Conclusion**: Established evidence supports SEC23A as a component of ER-to-Golgi transport and as one of the best-supported structural anchors in this module. The hypothesis that its coordinated abundance with the other module genes increases secretory throughput in both tissues remains to be tested.

#### SEC24D

- **Related proteins** (co-abundance neighbors): OPA1 (0.80); STRING partners: SEC23A (0.999), USO1 (0.751)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in liver, testis
- **hu.MAP 3.0**: huMAP3_12394.1, huMAP3_00065.1, huMAP3_00707.1, huMAP3_07775.1, huMAP3_06453.1, huMAP3_09282.1, huMAP3_11128.1, huMAP3_11237.1, huMAP3_13535.1
- **Function (MyGene.info)**: SEC24 homolog D, COPII component. The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec24p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. This gene product is implicated in the shaping of the vesicle, and also in cargo selection and concentration. Mut…
- **Diseases (Open Targets)**: Cole-Carpenter syndrome (0.753); hereditary disease (0.380); osteogenesis imperfecta type 1 (0.370); Seizure (0.259); Intellectual disability (0.259)
- **Europe PMC papers**: 780
- **Why important**: SEC24D is the strongest direct partner of SEC23A in STRING and also connects to USO1. It appears repeatedly with SEC23A in hu.MAP complexes (hu.MAP huMAP3_12394.1) and (hu.MAP huMAP3_00065.1) through (hu.MAP huMAP3_13535.1). Its established role is COPII cargo selection and vesicle formation, making it more informative for module function than a generic highly connected housekeeping gene. It is associated with Cole-Carpenter syndrome and osteogenesis imperfecta type one, demonstrating biological importance beyond the network itself.
- **Conclusion**: Established evidence identifies SEC24D as a COPII cargo-selection and ER-to-Golgi transport component that is physically linked to other module members. It is plausible, but not proven, that coordinated SEC23A-SEC24D abundance contributes to the shared secretory phenotype.

#### USO1

- **Related proteins** (co-abundance neighbors): WASHC5 (0.81), AARS1 (0.81); STRING partners: NSF (0.832), SEC23A (0.704), SEC24D (0.751)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in liver, testis
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: USO1 vesicle transport factor. The protein encoded by this gene is a peripheral membrane protein which recycles between the cytosol and the Golgi apparatus during interphase. It is regulated by phosphorylation: dephosphorylated protein associates with the Golgi membrane and dissociates from the membrane upon phosphorylation. Ras-associated protein 1 recruits this protein to coat protein complex II (COPII) vesicles during buddin…
- **Diseases (Open Targets)**: psoriatic arthritis (0.184); bipolar disorder (0.150); retinitis pigmentosa (0.085); cone dystrophy (0.076); cone-rod dystrophy (0.076)
- **Europe PMC papers**: 546
- **Why important**: USO1 links several trafficking observations: it is connected in STRING to NSF, SEC23A, and SEC24D, and it is present in the broader hu.MAP trafficking complex (hu.MAP huMAP3_12394.1). Its Golgi localization and established role in ER-to-Golgi vesicle transport and vesicle fusion provide a functional bridge between COPII budding and Golgi handling. Its position connecting the COPII-related genes to the wider module makes it important even though it is not a hub for every module gene. Its disease associations are limited in the supplied evidence, but its transport function is well established.
- **Conclusion**: Established evidence supports USO1 as a Golgi-associated vesicle transport factor that reinforces the module's trafficking interpretation. The proposed role of USO1 as a tissue-shared coordination point between secretion and endosomal remodeling is a hypothesis rather than a demonstrated causal role.

#### WASHC4

- **Related proteins** (co-abundance neighbors): TRIM25 (0.85), GCLC (0.83); STRING partners: WASHC5 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, testis
- **hu.MAP 3.0**: huMAP3_05454.1, huMAP3_06652.1, huMAP3_08077.1, huMAP3_10870.1, huMAP3_12900.1
- **Function (MyGene.info)**: WASH complex subunit 4. This gene encodes a component of the WASH complex, which functions in the intracellular transport of endosomes. Mutations in this gene have been detected in individuals with autosomal recessive cognitive disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014].
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.611); Intellectual disability (0.345); mathematical ability (0.322); Abnormality of the skeletal system (0.148); corneal ulcer (0.140)
- **Europe PMC papers**: 116
- **Why important**: WASHC4 is paired with WASHC5 by a very strong STRING relationship and is present with WASHC5 across several hu.MAP complexes (hu.MAP huMAP3_05454.1) and (hu.MAP huMAP3_06652.1) through (hu.MAP huMAP3_10870.1) and (hu.MAP huMAP3_12900.1). Its established function in WASH-complex-dependent endosome organization, endosomal transport, and actin nucleation adds an endosomal and cytoskeletal dimension that is complementary to COPII transport. It connects in the module graph to TRIM25 and GCLC, potentially linking membrane remodeling with stress and redox biology. It is associated with autosomal recessive intellectual disability, although the module does not establish a disease mechanism.
- **Conclusion**: Established evidence supports WASHC4 as part of an endosomal actin-remodeling complex with WASHC5. Its co-abundance with COPII and redox genes may indicate coordinated membrane quality control, but that integrated mechanism remains hypothetical.

#### ITIH4

- **Related proteins** (co-abundance neighbors): C9 (0.84), SERPINA3 (0.83), IGHA1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09434.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 4. The protein encoded by this gene is secreted into the blood, where it is cleaved by plasma kallikrein into two smaller forms. Expression of this gene has been detected only in liver, and it seems to be upregulated during surgical trauma. This gene is part of a cluster of similar genes on chromosome 3. Two transcript variants encoding different isoforms have been found for this gene. [provided by R…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.466); coronary artery disorder (0.417); type 2 diabetes mellitus (0.397); osteoarthritis (0.387); diabetes mellitus (0.363)
- **Europe PMC papers**: 1710
- **Why important**: ITIH4 represents the extracellular and liver-associated component of the module. It is tissue enriched in liver, secreted to blood, and connected in the module graph to C9, SERPINA3, and IGHA1. It recurs with SERPINA3 in multiple hu.MAP plasma-associated complexes (hu.MAP huMAP3_09434.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1), and (hu.MAP huMAP3_10678.1). Its established functions include participation in the acute-phase response and hyaluronan metabolism, and it has disease associations involving skeletal, vascular, and metabolic disorders. Its literature volume is substantial, supporting its interpretation as a biologically meaningful extracellular marker rather than an uncharacterized passenger.
- **Conclusion**: Established evidence supports ITIH4 as a liver-derived blood protein linked to acute-phase and extracellular matrix-related biology. Its presence may reflect genuine hepatic secretory biology or plasma carryover into tissue measurements; the supplied data cannot distinguish these possibilities.

#### GCLC

- **Related proteins** (co-abundance neighbors): PPM1B (0.85), WASHC4 (0.83), ME1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in liver, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamate-cysteine ligase catalytic subunit. Glutamate-cysteine ligase, also known as gamma-glutamylcysteine synthetase is the first rate-limiting enzyme of glutathione synthesis. The enzyme consists of two subunits, a heavy catalytic subunit and a light regulatory subunit. This locus encodes the catalytic subunit, while the regulatory subunit is derived from a different gene located on chromosome 1p22-p21. Mutations at this locus have been …
- **Diseases (Open Targets)**: gamma-glutamylcysteine synthetase deficiency (0.766); cystic fibrosis (0.375); neurodegenerative disease (0.373); non-autoimmune hemolytic anemia (0.370); lung adenocarcinoma (0.331)
- **Europe PMC papers**: 8941
- **Why important**: GCLC provides a redox and metabolic anchor that is distinct from the trafficking and plasma components. It is tissue enhanced in liver, detected in both tissues, and connected in the module graph to PPM1B, WASHC4, and ME1. Its established function is the rate-limiting catalytic step in glutathione synthesis, with roles in oxidative-stress responses and nutrient responses. It has a strong disease association with gamma-glutamylcysteine synthetase deficiency and hemolytic anemia, and it is extensively studied. Its network connection to WASHC4 suggests a possible interface between endosomal activity and protection from oxidative stress.
- **Conclusion**: Established evidence supports GCLC as a glutathione-biosynthesis and oxidative-stress regulator that could help maintain cellular function in both tissues. Its proposed coordination with vesicle trafficking is a hypothesis based on co-abundance and network placement, not on a demonstrated direct interaction.

## Module 2

**Tissue pair**: liver and testis  
**Genes (32)**: ALG2, BLMH, CIAO1, CISD2, COL6A3, CYP20A1, CACYBP, FKBP3, GNA11, HNRNPH1, LMNB1, PAK2, PCNA, PNP, PRKDC, PSPC1, ADSS2, CAD, RAB10, RAB21, RAN, SNRPA1, SEC23IP, PSAT1, SNRPD1, U2SURP, SRSF7, STX7, TIMM44, TPD52L2, SNRNP200, UBE2N

### Function

The strongest biological interpretation is a broadly expressed nuclear RNA-processing and genome-maintenance module, with a particularly coherent spliceosomal component. SNRNP200, SNRPA1, SNRPD1, U2SURP, HNRNPH1 and SRSF7 are established RNA-processing or spliceosome-related proteins. The direct STRING relationships among SNRNP200, SNRPA1, SNRPD1 and U2SURP, together with their membership in hu.MAP complexes (hu.MAP huMAP3_08980.1) and (hu.MAP huMAP3_06511.1), support a genuine spliceosomal subnetwork rather than an interpretation based only on expression similarity. Additional genes connect DNA replication and repair, nucleotide metabolism, vesicle trafficking, mitochondrial protein import and signaling, including PRKDC, PCNA, UBE2N, CAD, ADSS2, RAN, RAB10, RAB21 and TIMM44. STRING supplementary functions (STRING Function Organic cyclic compound binding; within-query FDR = 0.0095) and (STRING Function Heterocyclic compound binding; within-query FDR = 0.0095) identify broad organic- and heterocyclic-compound binding, but these are supplementary and do not establish a specific pathway. No GO/KEGG term passed global correction, so there is no globally significant GO/KEGG enrichment to report. Overall, the module is best viewed as a mixed but internally connected program centered on RNA splicing, with associated genome integrity, biosynthetic and intracellular-transport functions.

**Cell composition.** The module is not predominantly plasma or secreted: only COL6A3 is annotated as secreted to extracellular matrix, and most proteins are intracellular, including many nuclear proteins. Most genes have low tissue specificity, which is compatible with broadly expressed housekeeping or core cellular machinery. The HPA summary also shows predominantly low immune-cell specificity, arguing against a simple blood-cell module, although several genes have cell-type enhancement in neutrophils, erythrocyte progenitors, megakaryocyte-related cells, trophoblasts or spermatids. Late spermatid and related germ-cell signals could contribute to the liver-testis sharing, while blood or stromal contamination cannot be excluded for individual genes such as STX7, COL6A3 and PRKDC. Protein detection is widespread in both tissues, with several genes detected in both liver and testis, but tissue detection alone does not prove that the same cell type generates the module in both tissues. Thus, the shared signal may combine ubiquitous cellular machinery with contributions from shared proliferative, germ-cell, immune-associated or stromal cell states.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides strong known relationships within the spliceosomal portion: SNRNP200 is connected to SNRPA1 and SNRPD1, SNRPA1 is connected to SNRPD1 and U2SURP, SNRPD1 is connected to U2SURP and HNRNPH1, and HNRNPH1 is connected to SRSF7 (STRING Function Organic cyclic compound binding; within-query FDR = 0.0095) (STRING Function Heterocyclic compound binding; within-query FDR = 0.0095). ADSS2-CAD and PCNA-UBE2N are also established STRING relationships. These relationships support the presence of known molecular machinery embedded in the co-abundance module, but STRING covers only a sparse subset of the possible module pairs, so most co-abundance edges are not established physical interactions. hu.MAP independently supports the spliceosomal interpretation: SNRNP200, SNRPA1 and SNRPD1 occur together in (hu.MAP huMAP3_08980.1), while SNRPA1 and SNRPD1 recur in (hu.MAP huMAP3_06511.1). PRKDC and CIAO1 occur together in (hu.MAP huMAP3_09042.1), linking DNA repair or genome maintenance with cytosolic iron-sulfur assembly. The complexes therefore validate selected mechanistic substructures, but they do not demonstrate that the entire module is one physical complex.

**STRING interactions (score >= 0.7)**: 9 of 496 gene pairs: ADSS2–CAD (0.963); HNRNPH1–SNRPD1 (0.709); HNRNPH1–SRSF7 (0.922); PCNA–UBE2N (0.776); SNRNP200–SNRPA1 (0.999); SNRNP200–SNRPD1 (0.999); SNRPA1–SNRPD1 (0.999); SNRPA1–U2SURP (0.934); SNRPD1–U2SURP (0.744)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Organic cyclic compound binding (FDR = 0.0095, 26 genes); Function Heterocyclic compound binding (FDR = 0.0095, 26 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (SNRNP200, SNRPA1, SNRPD1; 3/97); huMAP3_09042.1 (CIAO1, PRKDC; 2/26); huMAP3_06511.1 (SNRPA1, SNRPD1; 2/79)

### Novelty

This module should not be described as a wholly new molecular pathway. Several of its central relationships and complexes are already represented by STRING and hu.MAP, especially the spliceosomal relationships involving SNRNP200, SNRPA1, SNRPD1 and U2SURP. The potentially novel result is the conserved liver-testis co-abundance configuration that combines this known spliceosomal core with DNA-repair, nucleotide, trafficking, mitochondrial and signaling genes. That tissue-pair-specific organization may be a new systems-level observation, but the fact sheet does not establish independent replication, causality or a new protein interaction. The absence of a relationship from STRING or hu.MAP would not prove novelty, because databases are incomplete and the co-abundance edges may reflect regulation, cell composition or indirect biology. Novelty is therefore best stated as a candidate tissue-shared co-abundance architecture requiring validation, not as discovery of a new pathway.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in liver and testis in which active RNA processing and spliceosome assembly are coordinated with genome surveillance, nucleotide supply, protein quality control and intracellular transport. The spliceosomal core formed by SNRNP200, SNRPA1, SNRPD1 and U2SURP could support transcript processing in cells with substantial biosynthetic or developmental demands. PRKDC, PCNA and UBE2N could couple this state to DNA damage sensing, replication-associated repair and damage tolerance, while CAD, ADSS2 and PNP could support nucleotide availability. RAB10, RAB21, SEC23IP and TIMM44 could connect the state to membrane, secretory and mitochondrial logistics. A competing explanation is that the apparent conservation is driven partly by shared cell types, especially germ-cell or progenitor-like populations, or by sample admixture. Testing this hypothesis requires cell-resolved data, independent cohorts and perturbation or biochemical validation.

### Important genes

#### SNRNP200

- **Related proteins** (co-abundance neighbors): GNA11 (0.89), PRKDC (0.88), ALG2 (0.85), CIAO1 (0.85), PSPC1 (0.85), PAK2 (0.84); STRING partners: SNRPA1 (0.999), SNRPD1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is the highest-connectivity member in the supplied module ranking and is linked to several functionally distinct module regions. It is a U5 snRNP-specific RNA helicase and a core component of spliceosomal tri-snRNP assembly and spliceosome conformational change. Its STRING relationships with SNRPA1 and SNRPD1 are exceptionally strong, and it participates in hu.MAP complex (hu.MAP huMAP3_08980.1). It also has substantial literature and disease association with inherited retinal dystrophy.
- **Conclusion**: Established evidence supports SNRNP200 as a central spliceosomal scaffold or remodeling factor in this module. Its position may make it an organizing marker of the module, but the co-abundance data do not prove that SNRNP200 drives the liver-testis association or regulates the other module branches.

#### SNRPD1

- **Related proteins** (co-abundance neighbors): RAB21 (0.85), CISD2 (0.84), UBE2N (0.81); STRING partners: HNRNPH1 (0.709), SNRNP200 (0.999), SNRPA1 (0.999), U2SURP (0.744)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver, testis
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_06511.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein D1 polypeptide. This gene encodes a small nuclear ribonucleoprotein that belongs to the SNRNP core protein family. The protein may act as a charged protein scaffold to promote SNRNP assembly or strengthen SNRNP-SNRNP interactions through nonspecific electrostatic contacts with RNA. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.483); dengue disease (0.370); liver disorder (0.116); breast cancer (0.097); breast carcinoma (0.097)
- **Europe PMC papers**: 636
- **Why important**: SNRPD1 is a core snRNP protein involved in spliceosomal assembly, RNA processing and the conformational transition of the spliceosome. It occupies the intersection of several module relationships, including links to SNRNP200, SNRPA1, U2SURP, HNRNPH1, RAB21, CISD2 and UBE2N. It is present in hu.MAP complexes (hu.MAP huMAP3_08980.1) and (hu.MAP huMAP3_06511.1), and its STRING relationships with SNRNP200 and SNRPA1 directly support known spliceosomal machinery.
- **Conclusion**: Established evidence identifies SNRPD1 as a strong representative of the module's spliceosomal core. Its connections outside that core are compatible with coordination between RNA processing and cellular transport or stress systems, but those cross-functional links remain hypotheses rather than demonstrated mechanisms.

#### PRKDC

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.88), ADSS2 (0.85), PSPC1 (0.84), SEC23IP (0.80), PAK2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, testis
- **hu.MAP 3.0**: huMAP3_09042.1
- **Function (MyGene.info)**: protein kinase, DNA-activated, catalytic subunit. This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to DNA-PKcs deficiency (0.752); neurodegenerative disease (0.548); severe combined immunodeficiency (0.470); combined immunodeficiency (0.464); ovarian neoplasm (0.210)
- **Europe PMC papers**: 12461
- **Why important**: PRKDC encodes the catalytic subunit of DNA-dependent protein kinase and is established in DNA double-strand-break repair and recombination. It has a prominent module position, connects to SNRNP200, ADSS2, PSPC1, SEC23IP and PAK2, and participates in hu.MAP complex (hu.MAP huMAP3_09042.1). Its disease associations include DNA-PKcs deficiency and combined immunodeficiency, and it has extensive literature.
- **Conclusion**: Established evidence supports PRKDC as the principal genome-maintenance representative of the module. Its co-abundance with spliceosomal and biosynthetic genes could indicate coordination between RNA processing and DNA repair in the shared tissue state, but this coordination is not directly established by the fact sheet.

#### PSPC1

- **Related proteins** (co-abundance neighbors): TPD52L2 (0.87), CAD (0.86), CACYBP (0.85), SNRNP200 (0.85), PRKDC (0.84), PSAT1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: paraspeckle component 1. This gene encodes a nucleolar protein that localizes to punctate subnuclear structures that occur close to splicing speckles, known as paraspeckles. These paraspeckles are composed of RNA-protein structures that include a non-coding RNA, NEAT1/Men epsilon/beta, and the Drosophila Behavior Human Splicing family of proteins, which include the product of this gene and the P54NRB/NONO and PSF/SFPQ pro…
- **Diseases (Open Targets)**: sleep apnea syndrome (0.217); nephrotic syndrome (0.201); squamous cell lung carcinoma (0.196); Hypercholesterolemia (0.148); sleep disorder (0.126)
- **Europe PMC papers**: 1076
- **Why important**: PSPC1 is a highly connected nuclear module member and a paraspeckle component involved in RNA-associated nuclear organization, transcriptional regulation and membraneless organelle assembly. It links the spliceosomal marker SNRNP200 with CAD, PSAT1, CACYBP and TPD52L2. It is detected in both liver and testis, has low tissue and cell-type specificity, and has substantial literature.
- **Conclusion**: Established evidence supports PSPC1 as a plausible bridge between RNA processing and nuclear gene-regulatory organization. Its network position suggests a coordinating role, but there is no direct evidence here that it physically connects the spliceosome to nucleotide metabolism or that it explains tissue sharing.

#### CAD

- **Related proteins** (co-abundance neighbors): PSPC1 (0.86), LMNB1 (0.83); STRING partners: ADSS2 (0.963)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carbamoyl-phosphate synthetase 2, aspartate transcarbamylase, and dihydroorotase. The de novo synthesis of pyrimidine nucleotides is required for mammalian cells to proliferate. This gene encodes a trifunctional protein which is associated with the enzymatic activities of the first 3 enzymes in the 6-step pathway of pyrimidine biosynthesis: carbamoylphosphate synthetase (CPS II), aspartate transcarbamoylase, and dihydroorotase. This protein is regulated by the mitogen-activated…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 50 (0.660); congenital disorder of glycosylation type I (0.595); infantile epileptic-dyskinetic encephalopathy (0.499); type 2 diabetes mellitus (0.286); urolithiasis (0.283)
- **Europe PMC papers**: 60667
- **Why important**: CAD is a multifunctional enzyme complex responsible for the early steps of de novo pyrimidine biosynthesis and is associated with cell proliferation and liver development annotations. It connects to PSPC1 and LMNB1 in the module and has a strong known STRING relationship with ADSS2, which participates in purine nucleotide biosynthesis. CAD also has a very large literature base and disease associations involving developmental and neurological disorders.
- **Conclusion**: Established evidence supports CAD as the nucleotide-supply component of the module and as a plausible indicator of biosynthetic demand. Its relationship with the RNA-processing core may reflect the need for nucleotide production during active transcription, replication or germ-cell development, but that interpretation remains a hypothesis.

#### GNA11

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.89), SEC23IP (0.89), PNP (0.82), TIMM44 (0.82), UBE2N (0.82), PSAT1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in liver, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein subunit alpha 11. The protein encoded by this gene belongs to the family of guanine nucleotide-binding proteins (G proteins), which function as modulators or transducers in various transmembrane signaling systems. G proteins are composed of 3 units: alpha, beta and gamma. This gene encodes one of the alpha subunits (subunit alpha-11). Mutations in this gene have been associated with hypocalciuric hypercalcemia type…
- **Diseases (Open Targets)**: familial hypoparathyroidism (0.754); familial hypocalciuric hypercalcemia 2 (0.736); autosomal dominant hypocalcemia (0.611); congenital hemangioma (0.494); uveal melanoma (0.469)
- **Europe PMC papers**: 4418
- **Why important**: GNA11 is among the most connected module members and encodes a G-protein alpha subunit involved in receptor-mediated signal transduction and phospholipase C signaling. It links SNRNP200, SEC23IP, PNP, TIMM44, UBE2N and PSAT1, thereby connecting signaling with metabolic, transport and nuclear-maintenance components. It is detected in both liver and testis and has extensive literature and well-established associations with hypocalciuric hypercalcemia and dominant hypocalcemia.
- **Conclusion**: Established evidence supports GNA11 as a signaling-associated peripheral connector of the module rather than as part of the spliceosomal core. Its co-abundance may reflect upstream cellular-state signaling or shared cell composition; a direct role in coordinating RNA processing with the other module branches is not established.

## Module 3

**Tissue pair**: liver and testis  
**Genes (32)**: ANXA2, ATXN10, BAX, CAPZA2, CPNE1, CUL4A, DCPS, DDX6, DSTN, DDX39B, EIF2B5, GALM, GET3, GMDS, GSTP1, NHLRC2, NIF3L1, OAT, PNPT1, PTPA, MRPS22, SCFD1, SEPTIN2, SEPTIN7, SFXN3, SNX5, SNX6, SUPV3L1, TMEM70, TMOD3, TMX1, ZW10

### Function

The module does not support a single statistically established GO or KEGG function: no GO/KEGG term passed global correction, and there are no supplementary STRING enrichment terms. Its gene content instead points to a distributed cellular-maintenance program involving intracellular trafficking and vesicle handling, cytoskeletal organization, mitochondrial RNA processing and energy-related functions, RNA metabolism, protein quality control, and cell-cycle or chromosome-segregation processes. The co-abundance structure is therefore more consistent with coordinated basic cell biology than with a narrowly defined pathway. The liver–testis sharing may reflect common cellular demands rather than a tissue-specific biochemical pathway.

**Cell composition.** The module is not predominantly secreted, plasma, or blood-cell enriched. HPA reports only a small secreted component, while most genes have low tissue specificity and low immune-cell specificity. Protein detection is broad across both liver and testis, supporting genuine expression in both tissues rather than an explanation based solely on absent tissue expression. Several genes show cell-type enhancement in epithelial, trophoblast, muscle, germ-cell, or Hofbauer-cell contexts, but the pattern is heterogeneous. The module could therefore partly reflect shared cell states or broadly expressed housekeeping-like functions, with limited evidence for a blood-contamination explanation. HPA also shows a liver-enhanced gene and a testis-relevant spermatocyte or spermatid signal, but these are not sufficient to define the whole module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a small set of high-confidence relationships: the PNPT1–SUPV3L1 pair supports a mitochondrial RNA-processing connection; SCFD1–ZW10 supports vesicle-trafficking or membrane-organization biology; SNX5–SNX6 supports an endosomal sorting unit; SEPTIN2–SEPTIN7 supports a septin cytoskeletal unit; and CAPZA2–TMOD3 supports actin-filament organization. These known links validate parts of the network but do not establish one unified pathway. hu.MAP provides additional complex-level support for the SNX5–SNX6 pair across several sorting-related complexes, the SEPTIN2–SEPTIN7 pair in a septin complex, GMDS–GSTP1 in a complex containing PPP1R12B, ZW10–SCFD1 in vesicle-related complexes, ZW10–EIF2B5 in a broad complex, and TMEM70–ATXN10 in a broad membrane or mitochondrial-associated complex. Because most hu.MAP complexes contain only a small fraction of module members, they support local modules or shared cellular machinery rather than a complete physical complex representing the entire co-abundance module.

**STRING interactions (score >= 0.7)**: 5 of 496 gene pairs: CAPZA2–TMOD3 (0.844); PNPT1–SUPV3L1 (0.999); SCFD1–ZW10 (0.892); SEPTIN2–SEPTIN7 (0.999); SNX5–SNX6 (0.998)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14262.1 (GMDS, GSTP1; 2/3); huMAP3_02481.1 (SNX6, SNX5; 2/6); huMAP3_05609.1 (SNX6, SNX5; 2/7); huMAP3_10879.1 (SNX6, SNX5; 2/9); huMAP3_14326.1 (SNX6, SNX5; 2/11); huMAP3_12956.1 (SNX6, SNX5; 2/12); huMAP3_13408.1 (SNX6, SNX5; 2/12); huMAP3_13548.1 (SNX6, SNX5; 2/13); huMAP3_02362.1 (SEPTIN2, SEPTIN7; 2/14); huMAP3_13808.1 (SNX6, SNX5; 2/16); huMAP3_06458.1 (ZW10, SCFD1; 2/41); huMAP3_08929.1 (ZW10, SCFD1; 2/44); huMAP3_10587.1 (ZW10, SCFD1; 2/45); huMAP3_11232.1 (ZW10, EIF2B5; 2/78); huMAP3_09592.1 (TMEM70, ATXN10; 2/95)

### Novelty

This appears to be a potentially new tissue-pair co-abundance observation, but it should not be called a newly discovered molecular pathway. The module combines several biologically coherent local relationships with many genes lacking direct STRING or hu.MAP support, and it has no globally significant GO or KEGG term. Its novelty is therefore primarily the liver–testis co-abundance pattern and the particular integration of trafficking, cytoskeletal, mitochondrial, RNA, and proteostasis genes. Absence from interaction databases is not evidence of novelty by itself, because database coverage, tissue context, cell composition, and condition dependence can all produce missing interactions. Independent replication, preservation testing, protein-level validation, and comparison with published liver–testis co-expression modules would be needed to establish novelty.

**Hypothesis.** Hypothesis: the module reflects a shared cellular homeostasis program active in liver and testis, in which endosomal and secretory trafficking, actin or septin architecture, mitochondrial RNA quality control, mitochondrial protein or ATP-synthase maintenance, and stress-responsive protein handling are coordinated. A possible mechanistic chain is that trafficking and cytoskeletal machinery regulate membrane and organelle organization, while PNPT1–SUPV3L1, TMEM70, and related mitochondrial genes maintain mitochondrial RNA processing and respiratory capacity; CUL4A, EIF2B5, DDX6, and ZW10 could connect this state to proteostasis, translation control, RNA turnover, and cell-cycle surveillance. This is a testable model, not an established annotation of the module. It predicts that module activity should track organelle quality, vesicle trafficking, cytoskeletal remodeling, and mitochondrial stress in relevant liver and testis cell populations.

### Important genes

#### ATXN10

- **Related proteins** (co-abundance neighbors): DDX6 (0.88), DSTN (0.87), TMX1 (0.87), TMOD3 (0.86), GET3 (0.85), NHLRC2 (0.85), BAX (0.82), SEPTIN7 (0.81), DDX39B (0.81), OAT (0.81), CPNE1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Plasma membrane; IHC detected in liver, testis
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: ataxin 10. This gene encodes a protein that may function in neuron survival, neuron differentiation, and neuritogenesis. These roles may be carried out via activation of the mitogen-activated protein kinase cascade. Expansion of an ATTCT repeat from 9-32 copies to 800-4500 copies in an intronic region of this locus has been associated with spinocerebellar ataxia, type 10. Alternatively spliced transcript var…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 10 (0.624); neurodegenerative disease (0.437); Dupuytren Contracture (0.265); benign endocrine neoplasm (0.215); benign neoplasm of adrenal gland (0.215)
- **Europe PMC papers**: 701
- **Why important**: ATXN10 is the most connected hub in the supplied network and links genes involved in cytoskeletal organization, membrane-protein insertion, stress or survival biology, and mitochondrial or cellular maintenance. It is broadly expressed in HPA, detected in both tissues, and has a substantial literature linking it to neuronal development and spinocerebellar ataxia type ten. Its hub position makes it a useful integrator, although the module does not establish that ATXN10 drives the shared tissue pattern.
- **Conclusion**: Established evidence supports ATXN10 as a central network correlate with broad tissue expression and disease relevance. Hypothesis: ATXN10 may coordinate several maintenance processes represented in the module, but a direct liver–testis-specific mechanism remains unproven.

#### CUL4A

- **Related proteins** (co-abundance neighbors): GET3 (0.86), SCFD1 (0.86), TMX1 (0.85), CAPZA2 (0.85), GALM (0.84), ZW10 (0.82), SFXN3 (0.82), DCPS (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cullin 4A. CUL4A is the ubiquitin ligase component of a multimeric complex involved in the degradation of DNA damage-response proteins (Liu et al., 2009 [PubMed 19481525]).[supplied by OMIM, Oct 2009].
- **Diseases (Open Targets)**: plasma cell myeloma (0.613); follicular lymphoma (0.566); myelodysplastic syndrome (0.563); mantle cell lymphoma (0.551); immune system disorder (0.503)
- **Europe PMC papers**: 2882
- **Why important**: CUL4A is a prominent network connector linking trafficking-associated genes, metabolic genes, and membrane or organelle-related genes. Its established function as a ubiquitin-ligase component involved in DNA-damage-response protein degradation, cell-cycle control, nucleotide-excision repair, and spermatogenesis gives it a plausible regulatory role in both hepatic maintenance and germ-cell biology. It also has extensive disease literature, including hematologic malignancy associations.
- **Conclusion**: Established evidence supports CUL4A as a regulator of protein turnover, genome surveillance, and spermatogenesis. Hypothesis: its co-abundance may mark a shared proteostasis or cell-cycle-surveillance state, but the network does not demonstrate direct ubiquitin-ligase action on other module proteins.

#### SNX5

- **Related proteins** (co-abundance neighbors): SUPV3L1 (0.86); STRING partners: SNX6 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in liver, testis
- **hu.MAP 3.0**: huMAP3_02481.1, huMAP3_05609.1, huMAP3_10879.1, huMAP3_14326.1, huMAP3_12956.1, huMAP3_13408.1, huMAP3_13548.1, huMAP3_13808.1
- **Function (MyGene.info)**: sorting nexin 5. This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. This protein functions in endosomal sorting, the phosphoinositide-signaling pathway, and macropinocytosis. This gene may play a role in the tumorigenesis of papillary thyroid carcinoma. Alternative spli…
- **Diseases (Open Targets)**: drug allergy (0.201); Parkinson disease (0.095); hypothyroidism (0.093); nonpapillary renal cell carcinoma (0.078); head and neck squamous cell carcinoma (0.075)
- **Europe PMC papers**: 1362
- **Why important**: SNX5 is part of the strongest local sorting relationship in STRING through SNX6 and is represented with SNX6 in numerous hu.MAP complexes. Its PX-domain sorting function, endosomal transport activity, and links to receptor trafficking provide a concrete mechanistic anchor for the trafficking component of the module. HPA places it in vesicles and cytosol and shows enhancement in Hofbauer and Kupffer cells, which also makes cell composition relevant.
- **Conclusion**: Established evidence supports SNX5 as an endosomal-sorting component with known association to SNX6. Hypothesis: the SNX5–SNX6 unit may organize receptor or cargo trafficking shared by liver and testis cells, but the co-abundance data cannot determine cargo direction or causality.

#### PNPT1

- **Related proteins** (co-abundance neighbors): GMDS (0.87), TMEM70 (0.82); STRING partners: SUPV3L1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in liver, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polyribonucleotide nucleotidyltransferase 1. The protein encoded by this gene belongs to the evolutionary conserved polynucleotide phosphorylase family comprised of phosphate dependent 3'-to-5' exoribonucleases implicated in RNA processing and degradation. This enzyme is predominantly localized in the mitochondrial intermembrane space and is involved in import of RNA to mitochondria. Mutations in this gene have been associated with combined …
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 13 (0.807); autosomal recessive nonsyndromic hearing loss 70 (0.740); spinocerebellar ataxia type 25 (0.709); deafness (0.676); hearing loss, autosomal recessive (0.634)
- **Europe PMC papers**: 839
- **Why important**: PNPT1 is connected to GMDS in the module and has a very strong known STRING relationship with SUPV3L1, forming the clearest mitochondrial RNA-processing pair. It is detected in both liver and testis, has established roles in mitochondrial RNA processing and degradation, and is associated with combined oxidative-phosphorylation deficiency, hereditary deafness, and related mitochondrial disease phenotypes.
- **Conclusion**: Established evidence supports PNPT1 as a mitochondrial RNA-processing factor and supports its partnership with SUPV3L1. Hypothesis: this pair may report mitochondrial RNA quality control within the shared module and could couple organelle state to tissue-specific energetic demands.

#### ZW10

- **Related proteins** (co-abundance neighbors): SUPV3L1 (0.85), CUL4A (0.82), GMDS (0.81); STRING partners: SCFD1 (0.892)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in liver, testis
- **hu.MAP 3.0**: huMAP3_06458.1, huMAP3_08929.1, huMAP3_10587.1, huMAP3_11232.1
- **Function (MyGene.info)**: zw10 kinetochore protein. This gene encodes a protein that is one of many involved in mechanisms to ensure proper chromosome segregation during cell division. This protein is an essential component of the mitotic checkpoint, which prevents cells from prematurely exiting mitosis. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); liver disorder (0.206); placental abruption (0.126); neuropathy (0.087); prostate carcinoma (0.086)
- **Europe PMC papers**: 999
- **Why important**: ZW10 occupies a bridging position between SUPV3L1, CUL4A, and GMDS and is the module member with a direct STRING relationship to SCFD1. Its hu.MAP memberships connect it to vesicle-related complexes and to a broad complex containing EIF2B5. Its established roles in the mitotic checkpoint, chromosome segregation, spindle orientation, and ER-to-Golgi or retrograde transport make it a plausible link between cell division and membrane traffic. HPA detects it in both tissues and shows enhancement in early primary spermatocytes.
- **Conclusion**: Established evidence supports ZW10 in chromosome-segregation surveillance and vesicle-trafficking biology. Hypothesis: ZW10 may connect proliferative or germ-cell states with organelle trafficking in the shared module, but the observed correlations do not prove a single multifunctional complex.

#### SEPTIN7

- **Related proteins** (co-abundance neighbors): ATXN10 (0.81), SEPTIN2 (0.81); STRING partners: SEPTIN2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in liver, testis
- **hu.MAP 3.0**: huMAP3_02362.1
- **Function (MyGene.info)**: septin 7. This gene encodes a protein that is highly similar to the CDC10 protein of Saccharomyces cerevisiae. The protein also shares similarity with Diff 6 of Drosophila and with H5 of mouse. Each of these similar proteins, including the yeast CDC10, contains a GTP-binding motif. The yeast CDC10 protein is a structural component of the 10 nm filament which lies inside the cytoplasmic membrane and is essen…
- **Diseases (Open Targets)**: glaucoma (0.366); bone fracture (0.264); fracture of pelvis (0.264); open-angle glaucoma (0.262); male reproductive system disorder (0.260)
- **Europe PMC papers**: 304
- **Why important**: SEPTIN7 forms a high-confidence STRING pair with SEPTIN2 and is part of a hu.MAP septin complex. Its established functions in cytoskeleton organization, cytokinesis, cilium biology, and cell shape are especially relevant to testis cells and membrane-associated architecture. It is detected in both tissues and localized to actin filaments, providing a concrete structural component of the module.
- **Conclusion**: Established evidence supports SEPTIN7 as a structural septin and supports its partnership with SEPTIN2. Hypothesis: the septin pair may contribute to shared cytoskeletal or ciliary organization in liver and testis, potentially linking cell architecture to trafficking, but this requires direct cellular validation.

## Module 4

**Tissue pair**: liver and testis  
**Genes (8)**: AP3S1, ELMOD2, EIF4A2, LANCL1, NUP107, PDXDC1, UBA3, UCHL5

### Function

This module does not support a single statistically established pathway-level function: no GO or KEGG term passed global correction, and there were no supplementary STRING enrichment terms. Its gene annotations instead suggest a mixed cellular-maintenance program involving Golgi and vesicle biology through PDXDC1 and AP3S1, proteostasis and protein modification through UCHL5 and UBA3, nucleocytoplasmic transport through NUP107, translation control through EIF4A2, and possible antiviral-response biology through ELMOD2. The co-abundance structure is therefore more consistent with coordinated expression of several broadly useful intracellular processes than with a defined biochemical complex or pathway. The strongest network-centered signal is PDXDC1, which connects most of the other module members, while the UCHL5–UBA3 pair provides a smaller proteostasis-related substructure. These interpretations are functional annotations and network-context observations, not globally significant enrichment claims.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not blood-cell enriched according to HPA, since all members have low immune-cell specificity and no enriched blood-cell category was reported. Most genes have low tissue specificity, which is compatible with broadly expressed or housekeeping-like cellular functions, although several show cell-type-enhanced patterns. The most relevant tissue-pair observations are strong protein detection in testis for most measured members, while liver detection is more limited; several genes are not detected in liver despite being co-abundant in the module. HPA cell-type signals include spermatid or spermatocyte populations, neuronal or glial populations, epithelial populations, trophoblasts, lactotrophs, and cardiomyocytes. Thus, the shared module is unlikely to be explained by circulating plasma proteins or a simple blood contamination signature. It may instead reflect broadly expressed intracellular machinery, shared cellular states, or cell-composition effects, with testis-specific cellular contributions requiring particular caution.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair met the supplied high-confidence STRING interaction threshold, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. Consequently, the co-abundance edges should not be interpreted as established direct physical interactions, and the module is not corroborated as a known multiprotein complex by these resources. The absence of STRING or hu.MAP support does not invalidate the co-abundance pattern: correlated abundance can arise from shared regulation, common cell-type composition, parallel turnover, or indirect functional coupling. The annotated UCHL5 and UBA3 functions are biologically related to protein processing and modification, but the supplied resources do not establish that they physically interact within this module.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears to be a potentially novel co-abundance association rather than a rediscovery of a documented protein complex or canonical STRING-supported pathway. The main reasons are the absence of high-confidence STRING interactions, the absence of a multi-member hu.MAP complex, and the lack of globally significant GO or KEGG enrichment. However, these observations do not prove biological novelty. The module may capture coordinated regulation, tissue or cell-state composition, or weak and context-dependent relationships that are not represented in interaction databases. Novelty should therefore be stated conservatively: the liver–testis co-abundance configuration is not explained by the supplied reference resources, but its biological originality requires independent replication and experimental validation.

**Hypothesis.** Hypothesis: the module represents a shared intracellular homeostasis program that coordinates vesicle and Golgi handling, protein quality control or modification, nuclear transport, and translational regulation in cells present in both liver and testis. PDXDC1 may act as the co-abundance hub linking otherwise distinct cellular processes; AP3S1 and EIF4A2 may connect vesicle trafficking with translation-related state changes, while UCHL5 and UBA3 may reflect coordinated control of protein stability and neddylation. NUP107 may indicate a requirement for regulated nucleocytoplasmic exchange in the same cellular state. The hypothesis also allows a cell-composition explanation, particularly because several genes show cell-type-enhanced HPA patterns and testis detection is frequent. This is a mechanistic model, not an established interaction map or enrichment result.

### Important genes

#### PDXDC1

- **Related proteins** (co-abundance neighbors): AP3S1 (0.85), LANCL1 (0.85), NUP107 (0.85), ELMOD2 (0.84), UCHL5 (0.84), UBA3 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyridoxal dependent decarboxylase domain containing 1. Enables cadherin binding activity. Predicted to be involved in carboxylic acid metabolic process. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: autoimmune disorder of central nervous system (0.325); uterine corpus leiomyoma (0.325); type 2 diabetes mellitus (0.135); obesity disorder (0.123); nerve plexus disorder (0.096)
- **Europe PMC papers**: 379
- **Why important**: PDXDC1 is the network hub, connecting most other module members with comparatively strong co-abundance links. Its supplied annotation places it in the Golgi and vesicle system and describes cadherin binding and a predicted carboxylic-acid metabolic role. HPA reports low tissue specificity but enhancement in several cell types including early and late spermatids. Its disease-association evidence spans autoimmune, metabolic, obesity-related, and nervous-system contexts, while its literature volume is more modest than that of the best-studied module genes. Its central network position makes it the most important candidate for testing whether the module is organized around a real regulatory or cellular-state signal.
- **Conclusion**: Established evidence supports PDXDC1 as the co-abundance hub and as a Golgi- or vesicle-associated protein with cell-type-enhanced expression in relevant testicular populations. It is not established that PDXDC1 directly regulates the other module genes. A reasonable hypothesis is that PDXDC1 helps coordinate the module’s vesicle and cellular-homeostasis component, but this requires perturbation or interaction experiments.

#### UCHL5

- **Related proteins** (co-abundance neighbors): UBA3 (0.89), PDXDC1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in liver, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin C-terminal hydrolase L5. Enables endopeptidase inhibitor activity; proteasome binding activity; and thiol-dependent deubiquitinase. Involved in negative regulation of proteasomal ubiquitin-dependent protein catabolic process; positive regulation of smoothened signaling pathway; and protein deubiquitination. Located in cytosol; nucleolus; and nucleoplasm. Colocalizes with Ino80 complex. [provided by Alliance of Genome Reso…
- **Diseases (Open Targets)**: neurodegenerative disease (0.546); laryngeal disorder (0.247); neoplasm (0.108); glomerulonephritis (0.087); cancer (0.087)
- **Europe PMC papers**: 1195
- **Why important**: UCHL5 is a proteasome-binding deubiquitinase involved in protein deubiquitination, proteasomal regulation, chromatin-related processes, and smoothened signaling according to the supplied annotation. It connects to UBA3 and PDXDC1, placing it in the module’s proteostasis-centered substructure. HPA detects it in both liver and testis and reports cytosolic and nucleoplasmic localization. It has extensive literature coverage and disease associations involving neurodegeneration, neoplasm, cancer, and renal or laryngeal disorders, making it one of the most biologically characterized members.
- **Conclusion**: Established evidence supports UCHL5 as a broadly relevant regulator of protein processing and nuclear or cytosolic homeostasis that is detected in both tissues. The module does not establish a direct UCHL5 interaction with UBA3 or PDXDC1, despite their co-abundance links. The hypothesis that UCHL5 supplies a proteostasis axis within the module is plausible but remains indirect.

#### UBA3

- **Related proteins** (co-abundance neighbors): UCHL5 (0.89), PDXDC1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in liver, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin like modifier activating enzyme 3. The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E1 ubiquitin-activating enzyme family. The encod…
- **Diseases (Open Targets)**: dengue disease (0.370); acute myeloid leukemia (0.357); myelodysplastic syndrome (0.345); chronic myelomonocytic leukemia (0.286); neurodegenerative disease (0.208)
- **Europe PMC papers**: 878
- **Why important**: UBA3 encodes an activating enzyme for a ubiquitin-like modifier and is annotated for protein modification, proteolysis, and neddylation. It is connected to UCHL5 and PDXDC1 and is detected in both liver and testis, with low tissue and cell-type specificity. Its disease associations include hematologic disorders, dengue disease, and neurodegenerative disease, and it has substantial literature coverage. These features make UBA3 a strong representative of the module’s conserved intracellular protein-regulation component.
- **Conclusion**: Established evidence supports UBA3 as a broadly expressed protein-modification enzyme present in both tissues. The supplied network and reference resources do not demonstrate that it forms a physical complex with UCHL5 or PDXDC1 in this module. A plausible hypothesis is that coordinated abundance of UBA3 and UCHL5 reflects shared regulation of protein quality control or post-translational modification, but the precise biochemical connection is unproven.

#### NUP107

- **Related proteins** (co-abundance neighbors): PDXDC1 (0.85), LANCL1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 107. This gene encodes a member of the nucleoporin family. The protein is localized to the nuclear rim and is an essential component of the nuclear pore complex (NPC). All molecules entering or leaving the nucleus either diffuse through or are actively transported by the NPC. Alternate transcriptional splice variants of this gene have been observed but have not been thoroughly characterized. [provided …
- **Diseases (Open Targets)**: Galloway-Mowat syndrome (0.665); nephrotic syndrome, type 11 (0.622); 46 XX gonadal dysgenesis (0.577); familial idiopathic steroid-resistant nephrotic syndrome (0.554); HIV infectious disease (0.541)
- **Europe PMC papers**: 1487
- **Why important**: NUP107 is an essential nuclear-pore component involved in nucleocytoplasmic transport, nuclear-pore assembly, messenger RNA export, and nuclear import. It connects to PDXDC1 and LANCL1 in the module and shows cell-type enhancement in early primary spermatocytes. Its disease associations include Galloway–Mowat syndrome, nephrotic syndrome, and gonadal dysgenesis, and it has extensive literature coverage. NUP107 therefore adds a nuclear-transport dimension and a particularly relevant germ-cell context to the interpretation.
- **Conclusion**: Established evidence supports NUP107 as a nuclear-pore and transport protein with relevance to gonadal development and spermatocyte biology. The co-abundance module does not establish that its transport activity is mechanistically linked to PDXDC1 or LANCL1. The hypothesis that NUP107 marks a coordinated nuclear-export or germ-cell developmental state is consistent with the annotations but needs direct testing.

#### AP3S1

- **Related proteins** (co-abundance neighbors): PDXDC1 (0.85), EIF4A2 (0.82), LANCL1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor related protein complex 3 subunit sigma 1. This gene encodes a subunit of the AP3 adaptor complex. This complex functions in the formation of subcellular vesicles budded from the Golgi body. Several related pseudogenes of this gene have been found. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.565); lysosomal storage disease (0.370); alcohol drinking (0.205); frozen shoulder (0.199); spondylolisthesis (0.193)
- **Europe PMC papers**: 316
- **Why important**: AP3S1 is a subunit of the AP3 adaptor complex, which participates in Golgi-derived vesicle formation and intracellular protein transport. It occupies a bridge position between PDXDC1 and EIF4A2 and also connects to LANCL1, linking vesicle biology with the translation-related annotation of EIF4A2. HPA places it in vesicles and reports enhancement in epithelial, trophoblast, and neutrophil-progenitor cell types, while blood-cell specificity remains low. Its disease associations include neurodegenerative and lysosomal-storage disorders, and its literature coverage is substantial.
- **Conclusion**: Established evidence supports AP3S1 as a vesicle-trafficking component and as a network bridge within this module. The supplied evidence does not establish a direct AP3S1 interaction with PDXDC1, EIF4A2, or LANCL1. A reasonable hypothesis is that AP3S1 reflects a shared trafficking and secretory-organelle state, but the lack of global enrichment and physical-interaction support makes this provisional.

## Module 5

**Tissue pair**: liver and testis  
**Genes (5)**: COPG2, ADSL, RAD50, SEC24C, UNC45A

### Function

This module does not support a single established pathway. Its genes span COPII and COPI vesicle trafficking, purine nucleotide synthesis, protein chaperoning, and DNA double-strand-break repair. No GO or KEGG term passed global correction. The co-abundance structure may therefore reflect coordinated cellular maintenance, but the biological convergence remains uncertain. The sparse path-like network, linking RAD50 through ADSL and SEC24C to UNC45A and COPG2, is compatible with co-regulation without demonstrating direct physical cooperation.

**Cell composition.** All module proteins were detected in both liver and testis, and none is annotated as secreted. Most genes have low tissue specificity and all have low immune-cell specificity, with no enriched blood-cell population reported. One gene is group enriched in skeletal muscle and tongue, while the single-cell annotations are distributed across several epithelial, neural, endocrine, muscle-related, and intestinal cell types. Thus, the module does not look like a plasma-protein or blood-cell module. Its shared liver-testis signal is more consistent with broadly present intracellular proteins, although shared cell composition or general tissue cellular activity cannot be excluded.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional-enrichment result was reported. No high-confidence STRING relationship was reported for any gene pair, and no hu.MAP complex contained multiple module members. The observed co-abundance links are therefore not supported here by established protein-interaction or complex evidence. This argues against interpreting the module as a known physical complex. It does not disprove functional coordination, indirect regulation, or context-dependent interactions.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact co-abundance grouping appears unusual because it combines genes from distinct cellular processes and is not represented by a high-confidence STRING network or a hu.MAP complex. However, absence from those resources does not establish a new biological mechanism: database coverage is incomplete, co-abundance is not equivalent to physical interaction, and the lack of globally significant GO or KEGG enrichment prevents pathway-level validation. The defensible conclusion is that this is a potentially novel tissue-pair co-abundance pattern, not a demonstrated novel complex or pathway.

**Hypothesis.** Hypothesis: in liver and testis, a shared intracellular state involving membrane-protein trafficking and general cellular maintenance may coordinate vesicle-coat components with purine supply, protein-folding capacity, and genome-integrity surveillance. SEC24C and COPG2 could represent the trafficking component, ADSL could link cellular energy and nucleotide demand to the module, UNC45A could reflect proteostasis or differentiation-related chaperoning, and RAD50 could reflect DNA-damage or meiotic genome surveillance. This is a mechanistic hypothesis only; the available enrichment and interaction evidence does not establish these proteins as one pathway.

### Important genes

#### SEC24C

- **Related proteins** (co-abundance neighbors): UNC45A (0.85), ADSL (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in liver, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC24 homolog C, COPII component. The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec24p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The product of this gene may play a role in shaping the vesicle, as well as in cargo selection and concentration.…
- **Diseases (Open Targets)**: 22q11.2 deletion syndrome (0.370); neurodegenerative disease (0.369); Alzheimer disease (0.281); lysosomal storage disease (0.274); Parkinson disease (0.274)
- **Europe PMC papers**: 693
- **Why important**: SEC24C is one of the more connected internal genes in the co-abundance structure and is annotated as a COPII component involved in ER-to-Golgi transport, vesicle budding, and cargo selection. Its vesicle-trafficking function provides a plausible cellular-process anchor for the module. It has substantial literature and disease-relevant associations, although those associations do not specifically validate this module.
- **Conclusion**: Established evidence supports SEC24C as a vesicle-trafficking protein detected in both tissues and positioned centrally within this small co-abundance structure. It is a plausible module anchor, but its role as a coordinator of the other genes is a hypothesis rather than an established interaction.

#### ADSL

- **Related proteins** (co-abundance neighbors): RAD50 (0.85), SEC24C (0.84); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenylosuccinate lyase. The protein encoded by this gene belongs to the lyase 1 family. It is an essential enzyme involved in purine metabolism, and catalyzes two non-sequential reactions in the de novo purine biosynthetic pathway: the conversion of succinylaminoimidazole carboxamide ribotide (SAICAR) to aminoimidazole carboxamide ribotide (AICAR) and the conversion of adenylosuccinate (S-AMP) to adenosine monophosphate …
- **Diseases (Open Targets)**: adenylosuccinate lyase deficiency (0.852); neurodegenerative disease (0.528); hereditary disease (0.486); Intellectual disability (0.464); Epileptic encephalopathy (0.462)
- **Europe PMC papers**: 1131
- **Why important**: ADSL is also internally connected and catalyzes essential steps in de novo purine metabolism, including AMP-related synthesis. It has strong functional annotation, substantial literature, and a well-established association with adenylosuccinase deficiency and neurological disease. Its placement between RAD50 and SEC24C makes it a possible metabolic bridge in the observed network.
- **Conclusion**: Established evidence supports ADSL as a core purine-biosynthetic enzyme with important disease relevance. The module does not establish that purine metabolism mechanistically drives vesicle trafficking or DNA repair, so any bridging role remains a hypothesis.

#### RAD50

- **Related proteins** (co-abundance neighbors): ADSL (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAD50 double strand break repair protein. The protein encoded by this gene is highly similar to Saccharomyces cerevisiae Rad50, a protein involved in DNA double-strand break repair. This protein forms a complex with MRE11 and NBS1. The protein complex binds to DNA and displays numerous enzymatic activities that are required for nonhomologous joining of DNA ends. This protein, cooperating with its partners, is important for DNA double-stra…
- **Diseases (Open Targets)**: Nijmegen breakage syndrome-like disorder (0.780); cancer (0.593); hereditary neoplastic syndrome (0.579); hereditary breast ovarian cancer syndrome (0.539); breast carcinoma (0.490)
- **Europe PMC papers**: 13311
- **Why important**: RAD50 is a genome-maintenance factor that works with MRE11 and NBS1 in DNA double-strand-break repair, checkpoint activation, telomere maintenance, and meiotic recombination. It has the strongest literature presence among the module genes and important disease associations involving genome instability. Although it is terminal in the observed network, its biological importance is high.
- **Conclusion**: Established evidence supports RAD50 as a major DNA-repair and recombination protein relevant to disease and reproductive biology. Its co-abundance with ADSL does not demonstrate a direct metabolic connection; a shared stress, proliferation, or meiotic-cell state is a more cautious interpretation.

#### UNC45A

- **Related proteins** (co-abundance neighbors): SEC24C (0.85), COPG2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in liver, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: unc-45 myosin chaperone A. This gene encodes a regulatory component of the progesterone receptor/heat shock protein 90 chaperoning complex, which functions in the assembly and folding of the progesterone receptor. The encoded protein is thought to be essential for normal cell proliferation, and for the accumulation of myosin during development of muscle cells. [provided by RefSeq, Sep 2018].
- **Diseases (Open Targets)**: osteootohepatoenteric syndrome (0.723); Aagenaes syndrome (0.532); type 2 diabetes mellitus (0.199); hereditary disease (0.194); diarrheal disease (0.148)
- **Europe PMC papers**: 464
- **Why important**: UNC45A occupies an internal position linking SEC24C and COPG2. It is annotated as a myosin chaperone and as a regulatory component of a progesterone-receptor and HSP ninety chaperoning complex, with roles in protein folding, cell proliferation, and myosin accumulation during muscle development. Its tissue and cell-type annotations are not restricted to liver or testis, making it relevant to a possible general proteostasis or differentiation state.
- **Conclusion**: Established evidence supports UNC45A in chaperoning and protein-folding biology, with disease associations including osteootohepatoenteric and Aagenaes syndromes. Its position suggests a possible connection between trafficking and proteostasis, but the module provides no direct interaction evidence.

#### COPG2

- **Related proteins** (co-abundance neighbors): UNC45A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coat protein complex I subunit gamma 2. Predicted to enable structural molecule activity. Involved in intra-Golgi vesicle-mediated transport. Part of COPI vesicle coat. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.410); skin neoplasm (0.327); Alzheimer disease (0.253); alcohol drinking (0.252); stroke disorder (0.252)
- **Europe PMC papers**: 389
- **Why important**: COPG2 is the terminal trafficking-related gene connected to UNC45A and encodes a gamma subunit of the COPI coat. Its annotations support retrograde Golgi-to-ER and intra-Golgi transport, complementing the COPII role of SEC24C. It has a smaller literature base than RAD50 or ADSL but provides an independent vesicle-transport rationale for the module.
- **Conclusion**: Established evidence supports COPG2 as a COPI vesicle-coat component involved in intracellular transport. Its co-abundance with UNC45A may indicate shared secretory-pathway or cellular-state regulation, but no direct physical relationship is supported by the reported STRING or hu.MAP evidence.

## Module 6

**Tissue pair**: liver and testis  
**Genes (5)**: RAP1GDS1, GBE1, MMUT, PEPD, PGM1

### Function

The most coherent interpretation is a cytosolic and intermediary-metabolism module centered on glucose handling, glycogen metabolism, and related carbon flux. GBE1 catalyzes glycogen branching, while PGM1 transfers phosphate between glucose-phosphate forms and is linked to glycogen, glycolytic, gluconeogenic, and galactose-related metabolism. MMUT connects the module to propionyl-CoA catabolism and succinyl-CoA production, and PEPD supports amino-acid and proline recycling. RAP1GDS1 provides a regulatory and signaling component rather than a clearly defined metabolic-enzyme role. However, no GO or KEGG term passed global correction; therefore these functional themes are gene-level and network-based interpretations, not evidence of statistically significant module enrichment. The sparse graph is consistent with a metabolic neighborhood rather than a demonstrated multiprotein complex.

**Cell composition.** This is not a plasma or secreted-protein module: all module proteins are intracellular, and no member is annotated as secreted. All genes have low immune-cell specificity, with no recurrent blood-cell enrichment, arguing against a blood-cell explanation. The HPA profile instead points toward tissue and cell composition, especially hepatocytes and muscle-associated cell types, with additional intestine, kidney, and specialized cell-type signals. The shared liver–testis pattern may therefore reflect conserved metabolic programs in particular parenchymal or differentiated cell populations rather than a secreted circulating program. Protein detection in both liver and testis supports the biological presence of the module in the paired tissues, while the lack of liver detection for RAP1GDS1 should temper claims of uniform protein-level representation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, between GBE1 and PGM1. This is biologically coherent because both proteins participate in glycogen or glucose-phosphate metabolism, but it establishes only a known functional or interaction relationship for that pair, not a complete physical complex for the module. The other co-abundance links are not supported by high-confidence STRING relationships in the fact sheet. No hu.MAP complex contains multiple module members. Accordingly, the co-abundance network may capture coordinated expression or shared cellular context, with only a limited portion currently supported by prior interaction resources.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: GBE1–PGM1 (0.942)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be called a wholly new biological pathway. Its central metabolic functions and the GBE1–PGM1 relationship are already established, and the individual genes have substantial prior literature and disease annotation. What may be novel is the specific conserved co-abundance configuration across liver and testis, particularly the association linking glycogen enzymes with RAP1GDS1, PEPD, and MMUT in this tissue pair. That possibility remains provisional: absence from STRING or hu.MAP does not prove novelty, and the lack of globally significant GO or KEGG enrichment limits claims that the entire module represents a previously unrecognized functional unit. Independent replication, tissue-cell deconvolution, and experimental testing of the noncanonical edges would be needed to establish novelty.

**Hypothesis.** Hypothesis: the module reflects coordinated metabolic demand in hepatocyte- and muscle-associated cell states, with PGM1 and GBE1 organizing glucose-phosphate and glycogen flux, MMUT connecting carbon handling to propionate-derived mitochondrial metabolism, and PEPD supporting amino-acid and proline recycling. RAP1GDS1 may couple this metabolic state to intracellular signaling or organelle regulation. The liver–testis conservation could arise from shared metabolic cell programs or conserved regulation of energy and biosynthetic substrates, rather than from a stable protein complex. This hypothesis predicts that the co-abundance pattern should track metabolic cell state and substrate flux, while the RAP1GDS1, PEPD, and MMUT connections may be regulatory or context-dependent rather than direct physical interactions.

### Important genes

#### GBE1

- **Related proteins** (co-abundance neighbors): RAP1GDS1 (0.87), PGM1 (0.87); STRING partners: PGM1 (0.942)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 1,4-alpha-glucan branching enzyme 1. The protein encoded by this gene is a glycogen branching enzyme that catalyzes the transfer of alpha-1,4-linked glucosyl units from the outer end of a glycogen chain to an alpha-1,6 position on the same or a neighboring glycogen chain. Branching of the chains is essential to increase the solubility of the glycogen molecule and, consequently, in reducing the osmotic pressure within cells. Highest l…
- **Diseases (Open Targets)**: glycogen storage disease due to glycogen branching enzyme deficiency (0.848); adult polyglucosan body disease (0.801); glycogen storage disease due to glycogen branching enzyme deficiency, adult neuromuscular form (0.711); glycogen storage disease due to glycogen branching enzyme deficiency, congenital neuromuscular form (0.591); disorder of glycogen metabolism (0.573)
- **Europe PMC papers**: 1361
- **Why important**: GBE1 is a central graph node connected to RAP1GDS1 and PGM1 and has a high-confidence STRING relationship with PGM1. Its established enzyme function is glycogen branching, which increases glycogen solubility and reduces osmotic pressure. It is tissue-enhanced in skeletal muscle, detected in both liver and testis, and has well-established associations with glycogen storage disease and adult polyglucosan body disease. Its extensive literature makes it a strong biological anchor for interpreting the module.
- **Conclusion**: Established: GBE1 is a glycogen-metabolism enzyme and a network-supported anchor of the module. Hypothesis: its co-abundance with RAP1GDS1 may indicate regulation of glycogen-related metabolism by a signaling or cellular-organization program, but the fact sheet does not establish a direct GBE1–RAP1GDS1 interaction.

#### PGM1

- **Related proteins** (co-abundance neighbors): GBE1 (0.87), MMUT (0.82); STRING partners: GBE1 (0.942)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglucomutase 1. The protein encoded by this gene is an isozyme of phosphoglucomutase (PGM) and belongs to the phosphohexose mutase family. There are several PGM isozymes, which are encoded by different genes and catalyze the transfer of phosphate between the 1 and 6 positions of glucose. In most cell types, this PGM isozyme is predominant, representing about 90% of total PGM activity. In red cells, PGM2 is a majo…
- **Diseases (Open Targets)**: PGM1-congenital disorder of glycosylation (0.843); MPDU1-congenital disorder of glycosylation (0.551); developmental and epileptic encephalopathy, 36 (0.551); RFT1-congenital disorder of glycosylation (0.551); disorder of glycogen metabolism (0.506)
- **Europe PMC papers**: 3203
- **Why important**: PGM1 is a central graph node linking GBE1 and MMUT and is the other member of the high-confidence STRING pair. It is a broadly important phosphohexose mutase involved in glucose-phosphate interconversion and annotated in glycogen, glucose, gluconeogenic, glycolytic, and galactose metabolism. It is group-enriched in skeletal muscle and tongue, detected in both tissues, and is associated with PGM1-related congenital glycosylation disorders and glycogen-metabolism disorders. Its substantial literature and position between glycogen and broader carbon metabolism make it the principal metabolic connector.
- **Conclusion**: Established: PGM1 provides a strong mechanistic link between glucose-phosphate metabolism and the GBE1-supported glycogen interpretation. Hypothesis: the PGM1–MMUT co-abundance edge may reflect coordinated carbon flux rather than direct physical binding.

#### MMUT

- **Related proteins** (co-abundance neighbors): PGM1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methylmalonyl-CoA mutase. This gene encodes the mitochondrial enzyme methylmalonyl Coenzyme A mutase. In humans, the product of this gene is a vitamin B12-dependent enzyme which catalyzes the isomerization of methylmalonyl-CoA to succinyl-CoA, while in other species this enzyme may have different functions. Mutations in this gene may lead to various types of methylmalonic aciduria. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: methylmalonic aciduria due to methylmalonyl-CoA mutase deficiency (0.829); vitamin B12-unresponsive methylmalonic acidemia type mut0 (0.627); methylmalonic acidemia (0.578); vitamin B12-unresponsive methylmalonic acidemia type mut- (0.549); Methylmalonic aciduria (0.519)
- **Europe PMC papers**: 499
- **Why important**: MMUT is the module's liver-enhanced, hepatocyte-associated mitochondrial metabolic enzyme and connects directly to PGM1 in the co-abundance graph. It catalyzes the vitamin B twelve-dependent conversion of methylmalonyl-CoA to succinyl-CoA and is involved in propionyl-CoA catabolism and succinyl-CoA biosynthesis. Its disease associations with methylmalonic aciduria and methylmalonic acidemia provide strong clinical support for its metabolic importance, although its literature volume is more limited than that of PGM1.
- **Conclusion**: Established: MMUT contributes a mitochondrial organic-acid and anaplerotic dimension to an otherwise largely cytosolic metabolic module. Hypothesis: its coordinated abundance with PGM1 may mark coupling between glucose-related metabolism and mitochondrial carbon entry in hepatocyte-like cells.

#### PEPD

- **Related proteins** (co-abundance neighbors): RAP1GDS1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peptidase D. This gene encodes a member of the peptidase family. The protein forms a homodimer that hydrolyzes dipeptides or tripeptides with C-terminal proline or hydroxyproline residues. The enzyme serves an important role in the recycling of proline, and may be rate limiting for the production of collagen. Mutations in this gene result in prolidase deficiency, which is characterized by the excretion of larg…
- **Diseases (Open Targets)**: prolidase deficiency (0.822); type 2 diabetes mellitus (0.425); Abnormality of the skeletal system (0.411); diabetes mellitus (0.409); obesity disorder (0.354)
- **Europe PMC papers**: 1500
- **Why important**: PEPD is a terminal graph member connected to RAP1GDS1 and is tissue-enhanced in intestine and kidney while also being associated with hepatocytes and proximal tubule cells. Its established function is hydrolysis of proline- and hydroxyproline-containing dipeptides or tripeptides, supporting proline recycling and potentially collagen-related substrate supply. It is detected in both liver and testis and is associated with prolidase deficiency and metabolic or skeletal disease phenotypes. Its substantial literature makes it useful for distinguishing a broader substrate-recycling module from a purely glycogen-focused module.
- **Conclusion**: Established: PEPD contributes peptide and amino-acid recycling capacity and is not a secreted or blood-cell marker in this dataset. Hypothesis: its link to RAP1GDS1 may represent shared regulation of cellular metabolic state or tissue composition, but no direct molecular mechanism is established here.

#### RAP1GDS1

- **Related proteins** (co-abundance neighbors): GBE1 (0.87), PEPD (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rap1 GTPase-GDP dissociation stimulator 1. The smg GDP dissociation stimulator (smgGDS) protein is a stimulatory GDP/GTP exchange protein with GTPase activity (Riess et al., 1993 [PubMed 8262526]).[supplied by OMIM, Feb 2010].
- **Diseases (Open Targets)**: Alfadhel syndrome (0.430); carcinoma of liver and intrahepatic biliary tract (0.370); uterine carcinosarcoma (0.370); ovarian endometrioid adenocarcinoma with squamous differentiation (0.370); HER2 positive breast carcinoma (0.370)
- **Europe PMC papers**: 561
- **Why important**: RAP1GDS1 is a graph connector between GBE1 and PEPD, giving it a strategically important position despite the absence of a STRING partner or hu.MAP complex assignment. Its annotated functions include regulation of mitochondrial organization, mitochondrial calcium-related processes, myosin filament assembly, vascular smooth muscle contraction, and protein localization. It has low tissue specificity, is associated with photoreceptor cell types in HPA, and has disease or cancer associations in the supplied Open Targets evidence. Its literature volume is meaningful, but its functional connection to the metabolic enzymes is less established than the roles of GBE1, PGM1, MMUT, and PEPD.
- **Conclusion**: Established: RAP1GDS1 is a regulatory protein positioned between two otherwise distinct portions of the co-abundance graph. Hypothesis: RAP1GDS1 may coordinate cellular organization, calcium or mitochondrial signaling, and metabolic enzyme abundance; this is a testable interpretation rather than a demonstrated role in glycogen or proline metabolism.

## Module 7

**Tissue pair**: liver and testis  
**Genes (5)**: KRT10, KRT9, KRT2, KRT1, KRT5

### Function

The module is a coherent keratin intermediate-filament program. Every module gene contributes to the globally significant keratin-filament and intermediate-filament terms (GO:CC keratin filament; q_global = 2.08e-07), (GO:BP intermediate filament organization; q_global = 5.62e-07), (GO:BP intermediate filament-based process; q_global = 1.26e-06), (GO:CC intermediate filament; q_global = 5.6e-06), and (GO:CC intermediate filament cytoskeleton; q_global = 9.01e-06). The same genes also support cornified-envelope formation, skin and epidermis development, keratinocyte differentiation, keratinization, epithelial differentiation, and cytoskeletal organization (18 globally significant GO/KEGG terms, q_global 2.43e-05–0.0451; see the table). Thus, the best-supported interpretation is structural reinforcement and differentiation of stratified epithelial cells, especially keratinocytes. The cadherin-signaling enrichment (KEGG Cadherin signaling - Homo sapiens (human); q_global = 0.000142) is compatible with epithelial cell adhesion and organization, but the dominant evidence is the keratin cytoskeleton rather than a broad signaling pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module, and it is not primarily a blood-cell module. HPA assigns most genes to skin-enriched tissues and suprabasal or basal keratinocyte populations, with additional epithelial and myoepithelial associations. One gene has a secretion annotation in other tissues, but the module as a whole is clearly intracellular and structural. The immune-cell annotations are heterogeneous and do not define the module. All module proteins were not detected by HPA immunohistochemistry in liver or testis. Therefore, the shared liver–testis signal is more plausibly related to epithelial-cell admixture, tissue-boundary or surface contamination, sample composition, or a shared keratin-expressing cell population than to a liver–testis-specific protein program. The absence of detected protein in both named tissues also cautions against interpreting the module as an established resident liver or testis pathway.

**GO/KEGG enrichment**: 25 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC keratin filament | 2.08e-07 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament organization | 5.62e-07 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:MF structural constituent of skin epidermis | 1.25e-06 | KRT1, KRT10, KRT2, KRT5 |
| GO:BP intermediate filament-based process | 1.26e-06 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament cytoskeleton organization | 1.26e-06 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:CC intermediate filament | 5.6e-06 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:CC intermediate filament cytoskeleton | 9.01e-06 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| KEGG Cornified envelope formation - Homo sapiens (human) | 2.43e-05 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP skin development | 3.39e-05 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP epidermis development | 4.52e-05 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| KEGG Cadherin signaling - Homo sapiens (human) | 0.000142 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP keratinocyte differentiation | 0.00029 | KRT1, KRT10, KRT2, KRT5 |
| GO:BP epidermal cell differentiation | 0.000579 | KRT1, KRT10, KRT2, KRT5 |
| GO:BP epithelial cell differentiation | 0.00112 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP keratinization | 0.00123 | KRT1, KRT2, KRT5 |

### STRING and hu.MAP

STRING independently supports the same interpretation: the module genes are annotated to keratin filaments, intermediate filaments, cornified-envelope formation, and structural constituents of skin epidermis (10 supplementary STRING terms; within-query FDR 3.73e-08–6.15e-06). STRING also contains strong pairwise associations among KRT1, KRT10, KRT2, and KRT5, indicating that much of the co-abundance structure corresponds to established keratin relationships rather than an unexplained association. KRT9 is biologically consistent with the keratin program, although the supplied STRING partner list does not report a STRING partner for it. The literature-linked STRING annotations connect the module to epidermolytic hyperkeratosis and skin keratinization (STRING DISEASES Epidermolytic hyperkeratosis; within-query FDR = 2.59e-06), (STRING PMID (2023) Key Factors in the Complex and Coordinated Network of Skin Keratinization: Their Significance and Involvement in Common Skin Conditions.; within-query FDR = 7.76e-06), (STRING PMID (2022) Palmoplantar Keratoderma: A Molecular Genetic Analysis of Family Cases.; within-query FDR = 7.76e-06), and (STRING PMID (2021) A Scarless Healing Tale: Comparing Homeostasis and Wound Healing of Oral Mucosa With Skin and Oesophagus.; within-query FDR = 7.76e-06). No hu.MAP complex contains multiple module members. This absence does not contradict the interpretation: keratin filaments are dynamic, polymeric cytoskeletal assemblies and may not be represented as a discrete hu.MAP complex.

**STRING interactions (score >= 0.7)**: 6 of 10 gene pairs: KRT1–KRT10 (0.999); KRT1–KRT2 (0.956); KRT1–KRT5 (0.923); KRT10–KRT2 (0.904); KRT10–KRT5 (0.793); KRT2–KRT5 (0.871)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Keratin filament (FDR = 3.73e-08, 5 genes); COMPARTMENTS Keratin filament (FDR = 3.87e-08, 5 genes); Keyword Keratin (FDR = 4.88e-08, 5 genes); SMART Intermediate filament protein (FDR = 6.19e-08, 5 genes); Keyword Intermediate filament (FDR = 9.46e-08, 5 genes); InterPro Intermediate filament protein, conserved site (FDR = 3.54e-07, 5 genes); InterPro Intermediate filament, rod domain (FDR = 3.54e-07, 5 genes); RCTM Formation of the cornified envelope (FDR = 3.8e-07, 5 genes); DISEASES Epidermolytic hyperkeratosis (FDR = 2.59e-06, 4 genes); Function Structural constituent of skin epidermis (FDR = 6.15e-06, 4 genes); PMID (2025) Mass spectrometric detection of keratins in tear fluid. (FDR = 7.76e-06, 5 genes); PMID (2023) Key Factors in the Complex and Coordinated Network of Skin Keratinization: Their Significance and Involvement in Common Skin Conditions. (FDR = 7.76e-06, 5 genes); PMID (2022) A metatranscriptomic approach to explore longitudinal tissue specimens from non-healing diabetes related foot ulcers. (FDR = 7.76e-06, 5 genes); PMID (2022) Palmoplantar Keratoderma: A Molecular Genetic Analysis of Family Cases. (FDR = 7.76e-06, 5 genes); PMID (2021) A Scarless Healing Tale: Comparing Homeostasis and Wound Healing of Oral Mucosa With Skin and Oesophagus. (FDR = 7.76e-06, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be claimed as a newly discovered keratin mechanism. Its function is strongly established by the complete overlap with keratin-filament enrichment (GO:CC keratin filament; q_global = 2.08e-07), the concordant epithelial and cornification terms (8 globally significant GO/KEGG terms, q_global 2.43e-05–0.00123; see the table), the STRING relationships, the HPA keratinocyte localization, and extensive gene-specific literature. The potentially novel observation is computational and contextual: this recognizable skin-keratin program co-abounds across the liver and testis data sets despite the lack of HPA protein detection in either tissue. That observation could reflect technical or cellular composition effects, and it requires validation with sample-level expression, histology, proteomics, and independent cohorts. Absence from hu.MAP, or incomplete representation in STRING, is not evidence that the module itself is biologically novel.

**Hypothesis.** Hypothesis: the conserved liver–testis module reflects a shared abundance signal from keratin-expressing epithelial cells or epithelial material present in both tissue collections, rather than a specialized pathway operating in hepatocytes and germ cells. Within those cells, KRT5 may represent a basal epithelial state, while KRT1, KRT10, and KRT2 represent progressively differentiated suprabasal structural states; KRT9 may mark a specialized terminal keratin program. Their coordinated abundance could therefore report epithelial differentiation and mechanical-barrier architecture. This hypothesis should be tested by checking cellular deconvolution, histological localization, sample quality, and whether the module tracks epithelial-cell markers rather than liver or testis functional markers.

### Important genes

#### KRT1

- **Related proteins** (co-abundance neighbors): KRT9 (0.93), KRT10 (0.89), KRT5 (0.83), KRT2 (0.80); STRING partners: KRT10 (0.999), KRT2 (0.956), KRT5 (0.923)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 is the most central gene in the supplied module network, connecting to every other member and having the strongest weighted connectivity. It appears in every globally significant enrichment term (25 globally significant GO/KEGG terms, q_global 2.08e-07–0.0451; see the table). HPA places it in skin and suprabasal keratinocytes, while gene annotations describe a structural keratin partner expressed during epidermal differentiation. Its disease associations include epidermolytic ichthyosis and palmoplantar keratoderma, and its extensive literature makes it a well-established marker and mechanistic component of epidermal structural integrity.
- **Conclusion**: Established: KRT1 is a central structural hub of the keratin-filament program and is strongly linked to epidermal differentiation and keratinization. Hypothesis: its centrality in this cross-tissue module mainly reflects coordinated epithelial-cell composition or differentiation state rather than a liver–testis-specific role.

#### KRT10

- **Related proteins** (co-abundance neighbors): KRT1 (0.89), KRT9 (0.87), KRT2 (0.82); STRING partners: KRT1 (0.999), KRT2 (0.904), KRT5 (0.793)
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 10. This gene encodes a member of the type I (acidic) cytokeratin family, which belongs to the superfamily of intermediate filament (IF) proteins. Keratins are heteropolymeric structural proteins which form the intermediate filament. These filaments, along with actin microfilaments and microtubules, compose the cytoskeleton of epithelial cells. Mutations in this gene are associated with epidermolytic …
- **Diseases (Open Targets)**: epidermolytic hyperkeratosis 2A, autosomal dominant (0.787); epidermolytic ichthyosis (0.772); congenital reticular ichthyosiform erythroderma (0.727); ichthyosis, annular epidermolytic 1 (0.647); annular epidermolytic ichthyosis (0.642)
- **Europe PMC papers**: 2736
- **Why important**: KRT10 is a highly connected module member with strong STRING associations to KRT1, KRT2, and KRT5. It contributes to the globally significant keratin, intermediate-filament, cornification, and epithelial-differentiation terms (19 globally significant GO/KEGG terms, q_global 2.08e-07–0.00983; see the table). HPA assigns it to skin and suprabasal keratinocytes, and the gene annotation identifies roles in intermediate-filament organization, keratinocyte differentiation, epidermis development, and cornification. Its disease associations include epidermolytic hyperkeratosis and ichthyotic disorders, with a substantial literature supporting its importance.
- **Conclusion**: Established: KRT10 is a differentiated epidermal keratin that helps define the module's suprabasal and cornification-related identity. Hypothesis: coordinated KRT10 abundance may be a sensitive indicator of suprabasal epithelial material in the liver and testis samples.

#### KRT5

- **Related proteins** (co-abundance neighbors): KRT2 (0.87), KRT1 (0.83), KRT9 (0.80); STRING partners: KRT1 (0.923), KRT10 (0.793), KRT2 (0.871)
- **HPA**: Group enriched; Group enriched; blood Immune cell enriched; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 5. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the basal layer of the epidermis with family member KRT14. Mutations in t…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 2C, localized (0.768); epidermolysis bullosa simplex 2A, generalized severe (0.761); epidermolysis bullosa simplex 2B, generalized intermediate (0.761); epidermolysis bullosa simplex 2F, with mottled pigmentation (0.729); Dowling-Degos disease 1 (0.697)
- **Europe PMC papers**: 7044
- **Why important**: KRT5 is connected to the principal keratin partners in the module and is the clearest basal-epithelial component. HPA associates it with skin, cervix, esophagus, vagina, basal keratinocytes, and suprabasal keratinocytes, and locates it in intermediate filaments. It contributes to nearly all of the globally significant functional themes (16 globally significant GO/KEGG terms, q_global 2.08e-07–0.00401; see the table), (8 globally significant GO/KEGG terms, q_global 0.00745–0.0451; see the table). Its established functions include epidermis development, response to mechanical stimulus, keratinization, migration regulation, and intermediate-filament polymerization. Its disease associations include multiple forms of epidermolysis bullosa simplex and Dowling–Degos disease, supported by extensive literature.
- **Conclusion**: Established: KRT5 anchors the module in basal epithelial structure and mechanical resilience. Hypothesis: KRT5 may be particularly useful for testing whether the shared liver–testis module reflects basal or epithelial-cell admixture rather than intrinsic parenchymal biology.

#### KRT2

- **Related proteins** (co-abundance neighbors): KRT5 (0.87), KRT10 (0.82), KRT1 (0.80); STRING partners: KRT1 (0.956), KRT10 (0.904), KRT5 (0.871)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location Intermediate filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 2. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is expressed largely in the upper spinous layer of epidermal keratinocytes and mutations in this gene …
- **Diseases (Open Targets)**: superficial epidermolytic ichthyosis (0.815); exfoliative ichthyosis (0.358); Palmoplantar hyperkeratosis (0.267); hereditary disease (0.193); Vertigo (0.145)
- **Europe PMC papers**: 7459
- **Why important**: KRT2 has strong network connectivity and STRING support with KRT1, KRT10, and KRT5. It is present across the globally significant keratin and epithelial terms, including keratinocyte differentiation and keratinization (25 globally significant GO/KEGG terms, q_global 2.08e-07–0.0451; see the table). HPA places it in skin and suprabasal keratinocytes, while gene annotations describe expression in the upper spinous epidermal layer and roles in epidermis development, keratinization, keratinocyte activation, proliferation, and intermediate-filament organization. Its disease associations include superficial epidermolytic and exfoliative ichthyotic conditions, and it has extensive literature support.
- **Conclusion**: Established: KRT2 represents an upper-spinous or suprabasal differentiation component of the module and reinforces the interpretation as a stratified-epithelial structural program. Hypothesis: its co-abundance with basal and suprabasal keratins may reflect a mixed epithelial differentiation continuum in the sampled material.

#### KRT9

- **Related proteins** (co-abundance neighbors): KRT1 (0.93), KRT10 (0.87), KRT5 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 9. This gene encodes the type I keratin 9, an intermediate filament chain expressed only in the terminally differentiated epidermis of palms and soles. Mutations in this gene cause epidermolytic palmoplantar keratoderma. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: epidermolytic palmoplantar keratoderma, 1 (0.828); palmoplantar keratoderma, epidermolytic (0.682); Localized epidermolytic hyperkeratosis (0.511); Palmoplantar hyperkeratosis (0.456); Palmoplantar keratoderma (0.438)
- **Europe PMC papers**: 773
- **Why important**: KRT9 is the specialized member of the module. It connects to KRT1, KRT10, and KRT5 in the co-abundance network and participates in the core keratin-filament and epidermal-development enrichments (GO:CC keratin filament; q_global = 2.08e-07), (GO:BP intermediate filament organization; q_global = 5.62e-07), (GO:BP intermediate filament-based process; q_global = 1.26e-06), (6 globally significant GO/KEGG terms, q_global 5.6e-06–0.000142; see the table), (GO:BP epithelial cell differentiation; q_global = 0.00112), (GO:CC polymeric cytoskeletal fiber; q_global = 0.00401), (GO:BP epithelium development; q_global = 0.00745), (GO:MF structural molecule activity; q_global = 0.00983), and (5 globally significant GO/KEGG terms, q_global 0.0122–0.0451; see the table). Its annotation describes terminally differentiated palmoplantar epidermal expression and a role in epithelial morphogenesis, epidermis development, epithelial differentiation, and intermediate-filament organization. It is strongly associated with epidermolytic palmoplantar keratoderma and has a smaller but still substantial literature than the other selected genes. Its lack of a reported STRING partner in the supplied result makes it a useful distinction between database coverage and biological coherence.
- **Conclusion**: Established: KRT9 is a specialized epidermal keratin that supports the module's epithelial and terminal-differentiation interpretation. Hypothesis: its presence may indicate a particular keratinized epithelial source or contamination pattern, but the current data do not establish which cell population contributes it in liver or testis.
