# Conserved co-abundance modules: bone_marrow and testis

## Module 0

**Tissue pair**: bone_marrow and testis  
**Genes (42)**: A2M, SERPINA3, SERPINC1, CFB, CFH, CDK5RAP3, CKAP4, C3, C5, COG5, DRG2, EML3, AHSG, H6PD, RAP1GDS1, GHDC, GLUL, HBA1, SERPING1, IGHA1, IGHG1, IGHG2, SERPINB1, KNG1, MRE11, MYH11, NSDHL, SERPINF1, PITRM1, RCN2, SAMHD1, SCRN1, SERPINH1, SIRT5, SPARC, SYNE2, TST, TF, LTF, UGDH, VIM, GC

### Function

The module is best interpreted as an extracellular plasma-protein and innate humoral-defense module. The primary evidence is the globally corrected enrichment for blood microparticle (GO:CC blood microparticle; q_global = 2.82e-09), endopeptidase and peptidase inhibitor activities (7 globally significant GO/KEGG terms, q_global 1.56e-08–0.000283; see the table), humoral immune response (GO:BP humoral immune response; q_global = 3.02e-08), complement activation (GO:BP complement activation; q_global = 3.27e-07) (GO:BP complement activation, classical pathway; q_global = 0.000244) (GO:BP complement activation, alternative pathway; q_global = 0.00146), and the complement and coagulation cascade (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 8.05e-06). Additional primary terms support antibacterial and antimicrobial humoral defense (4 globally significant GO/KEGG terms, q_global 0.000304–0.0481; see the table), immune-effector regulation (9 globally significant GO/KEGG terms, q_global 0.00176–0.0401; see the table), and extracellular localization (GO:CC extracellular space; q_global = 0.0067) (GO:CC extracellular region; q_global = 0.00768). Thus, the most defensible function is coordinated extracellular control of complement, proteolysis, coagulation-related activity, iron or antimicrobial defense, and inflammatory protection. The module is not a coherent intracellular pathway: several genes are intracellular, structural, metabolic, or cell-type markers, so the dominant interpretation comes from the secreted and plasma-associated component rather than every member having the same biochemical role.

**Cell composition.** The module is strongly enriched for plasma and secreted proteins. HPA identifies most members as secreted, and the module contains complement proteins, serpins, kininogen, transferrin, vitamin D binding protein, alpha-2-macroglobulin, immunoglobulin heavy-chain genes, and other extracellular proteins. Blood microparticle enrichment (GO:CC blood microparticle; q_global = 2.82e-09), extracellular-region enrichment (GO:CC extracellular space; q_global = 0.0067) (GO:CC extracellular region; q_global = 0.00768), platelet alpha-granule enrichment (GO:CC platelet alpha granule lumen; q_global = 0.0167) (GO:CC platelet alpha granule; q_global = 0.0212), and STRING plasma or blood-microparticle annotations (5 supplementary STRING terms; within-query FDR 5.41e-07–1.4e-05) support a circulating-protein interpretation. HPA tissue evidence is especially liver and hepatocyte enriched, while lymphoid tissue, plasma cells, neutrophils, monocytes, and other immune-cell signals are also present. The immunoglobulin genes and HBA1 suggest contributions from plasma-cell, erythroid, or blood-derived material. The shared appearance in bone marrow and testis therefore may reflect circulating plasma, blood microparticles, vascular or stromal material, and shared immune-cell content rather than a testis-specific and bone-marrow-specific program. HPA protein detection is broader in testis than in bone marrow, but several prominent liver-derived proteins are not detected in either tissue, which further cautions against interpreting co-abundance as local production by every tissue cell.

**GO/KEGG enrichment**: 37 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 2.82e-09 | A2M, AHSG, C3, CFB, CFH, GC, HBA1, IGHA1, IGHG1, IGHG2, KNG1, SERPINA3, SERPINC1, SERPING1, TF |
| GO:MF endopeptidase inhibitor activity | 1.56e-08 | A2M, AHSG, C3, C5, KNG1, LTF, SERPINA3, SERPINB1, SERPINC1, SERPINF1, SERPING1, SERPINH1 |
| GO:MF peptidase inhibitor activity | 1.56e-08 | A2M, AHSG, C3, C5, KNG1, LTF, SERPINA3, SERPINB1, SERPINC1, SERPINF1, SERPING1, SERPINH1 |
| GO:BP humoral immune response | 3.02e-08 | A2M, C3, C5, CFB, CFH, IGHA1, IGHG1, IGHG2, LTF, SERPING1, TF |
| GO:MF endopeptidase regulator activity | 1.13e-07 | A2M, AHSG, C3, C5, KNG1, LTF, SERPINA3, SERPINB1, SERPINC1, SERPINF1, SERPING1, SERPINH1 |
| GO:BP complement activation | 3.27e-07 | A2M, C3, C5, CFB, CFH, IGHA1, IGHG1, IGHG2, SERPING1 |
| GO:MF peptidase regulator activity | 5.48e-07 | A2M, AHSG, C3, C5, KNG1, LTF, SERPINA3, SERPINB1, SERPINC1, SERPINF1, SERPING1, SERPINH1 |
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 8.05e-06 | A2M, C3, C5, CFB, CFH, KNG1, SERPINC1, SERPING1 |
| GO:MF enzyme inhibitor activity | 5.37e-05 | A2M, AHSG, C3, C5, KNG1, LTF, SERPINA3, SERPINB1, SERPINC1, SERPINF1, SERPING1, SERPINH1 |
| GO:MF serine-type endopeptidase inhibitor activity | 0.000169 | A2M, SERPINA3, SERPINB1, SERPINC1, SERPINF1, SERPING1, SERPINH1 |
| GO:BP complement activation, classical pathway | 0.000244 | C3, C5, IGHA1, IGHG1, IGHG2, SERPING1 |
| GO:MF molecular function inhibitor activity | 0.000283 | A2M, AHSG, C3, C5, KNG1, LTF, SERPINA3, SERPINB1, SERPINC1, SERPINF1, SERPING1, SERPINH1 |
| GO:BP antibacterial humoral response | 0.000304 | IGHA1, IGHG1, IGHG2, LTF, TF |
| GO:BP humoral immune response mediated by circulating immunoglobulin | 0.000767 | C3, C5, IGHA1, IGHG1, IGHG2, SERPING1 |
| GO:BP complement activation, alternative pathway | 0.00146 | C3, C5, CFB, CFH |

### STRING and hu.MAP

STRING supports a dense, biologically plausible extracellular interaction core. The strongest known relationships include C3 with CFB and CFH, C3 with C5, CFB with CFH, C3 with SERPING1, KNG1 with SERPING1, and multiple links among A2M, AHSG, SERPINA3, SERPINC1, GC, TF, KNG1, and SERPING1. These relationships are consistent with complement regulation, protease inhibition, coagulation, and plasma-protein association. STRING functional results independently point to endopeptidase inhibition, secreted and signal proteins, blood microparticles, plasma-cell or bone-marrow tissue, humoral immunity, and complement and coagulation (15 supplementary STRING terms; within-query FDR 5.02e-08–5.16e-05), but these are supplementary within-query results rather than globally corrected evidence. hu.MAP provides known complex-level support: many module proteins repeatedly co-occur in complexes containing CFB, C3, C5, CFH, SERPING1, A2M, KNG1, SERPINA3, SERPINC1, AHSG, GC, TF, and HBA1 (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1). The repeated overlap across complexes indicates that much of the module recapitulates established plasma-protein assemblies or shared biochemical neighborhoods. It does not establish that all co-abundance edges are direct physical interactions, nor that every module member belongs to one physical complex.

**STRING interactions (score >= 0.7)**: 35 of 861 gene pairs: A2M–AHSG (0.803); A2M–CFB (0.726); A2M–KNG1 (0.927); A2M–LTF (0.724); A2M–SERPINA3 (0.929); A2M–SERPINC1 (0.927); A2M–SERPINF1 (0.88); A2M–SERPING1 (0.905); A2M–TF (0.82); AHSG–C3 (0.7); AHSG–GC (0.959); AHSG–KNG1 (0.936); AHSG–LTF (0.744); AHSG–SERPINA3 (0.848); AHSG–SERPINC1 (0.838); AHSG–TF (0.866); C3–C5 (0.974); C3–CFB (0.999); C3–CFH (0.999); C3–GC (0.768); C3–KNG1 (0.804); C3–LTF (0.711); C3–SERPING1 (0.954); C5–CFB (0.774); C5–CFH (0.824); C5–KNG1 (0.701); CFB–CFH (0.961); CFB–SERPING1 (0.88); CFH–SERPING1 (0.722); GC–SERPINC1 (0.84); GC–TF (0.811); KNG1–SERPINC1 (0.758); KNG1–SERPING1 (0.964); NSDHL–UGDH (0.712); SERPINC1–SERPING1 (0.753)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Endopeptidase inhibitor activity (FDR = 5.02e-08, 12 genes); Keyword Signal (FDR = 5.41e-07, 19 genes); Keyword Secreted (FDR = 5.41e-07, 16 genes); Keyword Glycoprotein (FDR = 5.67e-07, 20 genes); Component Blood microparticle (FDR = 6.76e-07, 12 genes); COMPARTMENTS Blood microparticle (FDR = 7.07e-07, 12 genes); TISSUES Plasma cell (FDR = 1.46e-06, 11 genes); Process Negative regulation of hydrolase activity (FDR = 3.47e-06, 13 genes); KEGG Complement and coagulation cascades (FDR = 5.04e-06, 8 genes); NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization (FDR = 5.83e-06, 9 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 5.87e-06, 13 genes); TISSUES Bone marrow (FDR = 1.4e-05, 14 genes); TISSUES Cerebrospinal fluid (FDR = 2.91e-05, 7 genes); Process Humoral immune response (FDR = 4.6e-05, 8 genes); PMID (2023) Changes in the body fluids proteome as a reflection of the physiological effects of dry immersion. (FDR = 5.16e-05, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (CFB, SERPINC1, SERPINA3, A2M, C3, KNG1, AHSG, GC, TF, SERPING1, CFH, HBA1; 12/64); huMAP3_10678.1 (CFB, SERPINA3, A2M, C3, C5, KNG1, AHSG, GC, TF, SERPING1, CFH; 11/71); huMAP3_09531.1 (CFB, SERPINA3, A2M, C3, C5, KNG1, AHSG, TF, SERPING1; 9/47); huMAP3_10101.1 (CFB, SERPINA3, A2M, C3, C5, KNG1, AHSG, TF, SERPING1; 9/49); huMAP3_08395.1 (CFB, SERPINA3, A2M, C3, C5, KNG1, AHSG, TF; 8/43); huMAP3_09434.1 (SERPINA3, C3, C5, AHSG, GC, TF; 6/33); huMAP3_07265.1 (SERPINA3, A2M, KNG1, AHSG, TF; 5/20); huMAP3_08224.1 (SERPINA3, C3, C5, GC, TF; 5/21); huMAP3_02242.1 (SERPINA3, C3, AHSG, TF; 4/9); huMAP3_07432.1 (SERPINA3, C3, AHSG, TF; 4/18); huMAP3_09273.1 (CFB, A2M, KNG1, SERPING1; 4/28); huMAP3_07541.1 (A2M, C5, KNG1; 3/19); huMAP3_07701.1 (CFB, A2M, KNG1; 3/22); huMAP3_08796.1 (CFB, C5; 2/15); huMAP3_09832.1 (CFB, C5; 2/18)

### Novelty

This cannot be called a wholly new molecular module on the available evidence. Its dominant complement, coagulation, protease-inhibitor, immunoglobulin, and plasma-protein structure is already represented by STRING relationships and several hu.MAP complexes, and the enrichment profile is highly concordant with established biology. The potentially novel observation is the reproducible co-abundance of this extracellular module across bone marrow and testis, including peripheral genes that are not represented in the listed STRING or hu.MAP relationships. However, absence from those resources is not evidence of novelty, and the strong liver, plasma, blood-microparticle, immune-cell, and secreted-protein signatures provide an alternative explanation based on shared circulating material or cellular composition. A claim of novelty would require comparison with published cross-tissue co-abundance modules, independent cohorts, cell-deconvolution or matched plasma measurements, and experimental validation. The current evidence supports a conserved cross-tissue association, not a newly discovered biochemical complex.

**Hypothesis.** Hypothesis: the conserved signal is generated primarily by a circulating extracellular defense and protease-control milieu that is sampled in both tissues. Liver-derived complement and inhibitor proteins may associate with blood microparticles, immunoglobulins, platelet-granule material, and immune or stromal products in tissue samples. In bone marrow, this could be reinforced by neutrophil, plasma-cell, erythroid, and progenitor-associated material; in testis, by vascular, stromal, Leydig, Sertoli, and other local extracellular compartments. The coordinated abundance of C3, CFB, CFH, C5, SERPING1, A2M, SERPINC1, immunoglobulins, and antimicrobial proteins could reflect a regulated balance between complement activation, protease activity, coagulation, and tissue protection. The module should therefore be tested against plasma contamination, vascular abundance, cell-type composition, and local tissue expression before assigning it a tissue-intrinsic mechanism.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): CFB (0.92), KNG1 (0.89), TF (0.81); STRING partners: AHSG (0.7), C5 (0.974), CFB (0.999), CFH (0.999), GC (0.768), KNG1 (0.804), LTF (0.711), SERPING1 (0.954)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_09434.1, huMAP3_08224.1, huMAP3_02242.1, huMAP3_07432.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a central complement component and has broad primary support across complement activation, humoral immunity, immune-effector, extracellular, and antibacterial-response terms (14 globally significant GO/KEGG terms, q_global 2.82e-09–0.0481; see the table). It is connected in STRING to CFB, CFH, C5, SERPING1, KNG1, GC, AHSG, and LTF, and it recurs across many hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_07432.1). HPA places it in liver-derived extracellular biology and also reports immune-cell enrichment. Its extensive disease literature includes complement deficiency, atypical hemolytic-uremic syndrome, and complement-mediated kidney and retinal disease.
- **Conclusion**: Established evidence identifies C3 as a central driver or marker of the complement-related module, although the tissue data do not establish that it is locally produced in both tissues. Its abundance may report circulating complement or immune-associated material. A direct causal role in the cross-tissue co-abundance pattern remains a hypothesis.

#### CFH

- **Related proteins** (co-abundance neighbors): SYNE2 (0.90), IGHG1 (0.85), MYH11 (0.83), MRE11 (0.81); STRING partners: C3 (0.999), C5 (0.824), CFB (0.961), SERPING1 (0.722)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: complement factor H. This gene is a member of the Regulator of Complement Activation (RCA) gene cluster and encodes a protein with twenty short consensus repeat (SCR) domains. This protein is secreted into the bloodstream and has an essential role in the regulation of complement activation, restricting this innate defense mechanism to microbial infections. Mutations in this gene have been associated with hemolytic-ure…
- **Diseases (Open Targets)**: complement factor H deficiency (0.769); age-related macular degeneration (0.750); atypical hemolytic-uremic syndrome (0.729); age related macular degeneration 4 (0.711); Doyne honeycomb retinal dystrophy (0.688)
- **Europe PMC papers**: 9287
- **Why important**: CFH is a major regulator of complement activation, especially the alternative pathway, and is supported by primary terms for complement activation, immune defense, and complement regulation (9 globally significant GO/KEGG terms, q_global 3.02e-08–0.0401; see the table). It has strong STRING relationships with C3, CFB, C5, and SERPING1 and appears in multiple hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1). HPA identifies liver enrichment, secretion to blood, vesicular localization, and enhanced expression in several stromal, hepatic, and gonadal cell types. Its disease associations include atypical hemolytic-uremic syndrome, complement factor H deficiency, and age-related macular degeneration, supported by extensive literature.
- **Conclusion**: Established evidence supports CFH as the principal regulatory counterweight to complement activation within the module. Its detection in testis but not bone marrow by HPA is compatible with local contribution in testis, but the liver and circulating-protein evidence means that a shared plasma source remains plausible. A tissue-specific protective role is therefore a hypothesis rather than a demonstrated conclusion.

#### SERPING1

- **Related proteins** (co-abundance neighbors): EML3 (0.91), COG5 (0.84), SIRT5 (0.82); STRING partners: A2M (0.905), C3 (0.954), CFB (0.88), CFH (0.722), KNG1 (0.964), SERPINC1 (0.753)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_09273.1
- **Function (MyGene.info)**: serpin family G member 1. This gene encodes a highly glycosylated plasma protein involved in the regulation of the complement cascade. Its encoded protein, C1 inhibitor, inhibits activated C1r and C1s of the first complement component and thus regulates complement activation. It is synthesized in the liver, and its deficiency is associated with hereditary angioneurotic oedema (HANE). Alternative splicing results in multipl…
- **Diseases (Open Targets)**: hereditary angioedema with C1Inh deficiency (0.828); hereditary angioedema type 1 (0.750); hereditary angioedema (0.728); angioedema (0.616); hereditary angioedema type 2 (0.614)
- **Europe PMC papers**: 4203
- **Why important**: SERPING1 encodes a plasma complement regulator and is among the most functionally connected module members. It participates in primary terms for peptidase inhibition, humoral immunity, complement activation and regulation, extracellular localization, and immune-effector processes (26 globally significant GO/KEGG terms, q_global 2.82e-09–0.0401; see the table). STRING links it to A2M, C3, CFB, CFH, KNG1, and SERPINC1, while hu.MAP places it in repeated plasma-protein complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_09273.1). HPA shows secretion to blood, liver enhancement, and immune-cell enhancement. Its well-established association with hereditary angioedema makes it medically and mechanistically important.
- **Conclusion**: Established evidence supports SERPING1 as a central inhibitor that constrains complement and related proteolytic cascades. Its co-abundance with complement components is biologically coherent, but it does not prove coordinated activation in either tissue. The cross-tissue regulatory mechanism remains a hypothesis.

#### A2M

- **Related proteins** (co-abundance neighbors): AHSG (0.89), SERPINC1 (0.83), GC (0.83); STRING partners: AHSG (0.803), CFB (0.726), KNG1 (0.927), LTF (0.724), SERPINA3 (0.929), SERPINC1 (0.927), SERPINF1 (0.88), SERPING1 (0.905), TF (0.82)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_07265.1, huMAP3_09273.1, huMAP3_07541.1, huMAP3_07701.1
- **Function (MyGene.info)**: alpha-2-macroglobulin. The protein encoded by this gene is a protease inhibitor and cytokine transporter. It uses a bait-and-trap mechanism to inhibit a broad spectrum of proteases, including trypsin, thrombin and collagenase. It can also inhibit inflammatory cytokines, and it thus disrupts inflammatory cascades. Mutations in this gene are a cause of alpha-2-macroglobulin deficiency. This gene is implicated in Alzheimer…
- **Diseases (Open Targets)**: myopia (0.206); refractive error (0.151); primary angle-closure glaucoma (0.148); Abnormality of refraction (0.144); Aganglionic megacolon (0.118)
- **Europe PMC papers**: 5133
- **Why important**: A2M is a broad-spectrum protease inhibitor and cytokine transporter with primary support for inhibitor activity, humoral defense, complement regulation, extracellular localization, and platelet alpha-granule biology (21 globally significant GO/KEGG terms, q_global 2.82e-09–0.0401; see the table). It is highly connected to the plasma-protein core in STRING, including SERPINA3, SERPINC1, SERPING1, KNG1, AHSG, TF, and SERPINF1, and occurs in numerous hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_07701.1). HPA identifies secretion to blood and enhancement in several cell types, including hepatocytes and stromal or immune-associated populations. Its disease and literature record includes alpha-two-macroglobulin deficiency and inflammatory or neurodegenerative contexts.
- **Conclusion**: Established evidence supports A2M as a broad extracellular buffering component that can link protease inhibition, cytokine handling, and complement regulation. Its central position makes it an important integrator, but the data cannot distinguish active biochemical regulation from shared plasma abundance. A2M-mediated coordination across the two tissues is a hypothesis.

#### SERPINA3

- **Related proteins** (co-abundance neighbors): GC (0.93), TST (0.87), IGHG1 (0.86), HBA1; HBA2 (0.86), SERPINH1 (0.85), DRG2 (0.85), SERPINB1 (0.85), SCRN1 (0.84), CKAP4 (0.84), COG5 (0.83), NSDHL (0.82), RAP1GDS1 (0.81); STRING partners: A2M (0.929), AHSG (0.848)
- **HPA**: Group enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_09434.1, huMAP3_07265.1, huMAP3_08224.1, huMAP3_02242.1, huMAP3_07432.1
- **Function (MyGene.info)**: serpin family A member 3. The protein encoded by this gene is a member of the serpin family of proteins, a group of proteins that inhibit serine proteases. This gene is one in a cluster of serpin genes located on the q arm of chromosome 14. Polymorphisms in this protein appear to be tissue specific and influence protease targeting. Variations in this protein's sequence have been implicated in Alzheimer's disease, and defic…
- **Diseases (Open Targets)**: prostate carcinoma (0.359); chronic kidney disease (0.217); peripheral arterial occlusive disease 1 (0.118); central nervous system cancer (0.118); glioma (0.105)
- **Europe PMC papers**: 5458
- **Why important**: SERPINA3 has the strongest network position in the supplied module and is connected to several immunoglobulin, serpin, secretory, and extracellular markers. It is included in many primary inhibitor, extracellular, blood-microparticle, immune-defense, and platelet-granule terms (14 globally significant GO/KEGG terms, q_global 2.82e-09–0.0254; see the table). STRING links it to A2M and AHSG, and hu.MAP repeatedly places it in the same plasma-protein complex neighborhoods (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_07432.1). HPA reports secretion to blood and liver or pancreas enrichment, with detection in both tissues. Its established serpin function, inflammatory annotations, liver disease association, and substantial literature support its importance as a robust module marker.
- **Conclusion**: Established evidence supports SERPINA3 as a high-connectivity extracellular protease-inhibitor marker that may organize or report the plasma-associated module. Its network centrality does not establish physical centrality or causality. It is more safely interpreted as a prominent indicator of the shared secreted-protein environment.

#### IGHG1

- **Related proteins** (co-abundance neighbors): SERPINA3 (0.86), SERPINC1 (0.85), CFH (0.85), C5 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Immune cell enriched; location None; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: immunoglobulin heavy constant gamma 1 (G1m marker)
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 3057
- **Why important**: IGHG1 provides a distinct adaptive-humoral component within a module otherwise dominated by complement and protease regulators. It appears across primary terms for blood microparticles, humoral and immunoglobulin-mediated immunity, classical complement activation, antibacterial defense, and immune-effector regulation (24 globally significant GO/KEGG terms, q_global 2.82e-09–0.0481; see the table). HPA identifies plasma cells, memory B cells, lymphoid tissue, and immunoglobulin secretion, with detection in both tissues. It has network links to SERPINA3, SERPINC1, CFH, and C5, although STRING reports no listed direct partners and hu.MAP reports no listed complex membership. Its substantial literature volume reflects the importance of immunoglobulin biology, while its module-specific role is mainly compositional.
- **Conclusion**: Established evidence supports IGHG1 as evidence of immunoglobulin or plasma-cell material contributing to the module and potentially engaging complement through antibody-mediated defense. The co-abundance does not demonstrate antigen specificity, local antibody production, or direct physical interaction with the complement proteins. Those mechanistic interpretations remain hypotheses.

## Module 1

**Tissue pair**: bone_marrow and testis  
**Genes (45)**: AAMDC, ADK, ALDH3A2, ANXA7, APOA1, APOE, ATXN10, CACNA2D1, CIAO1, CPPED1, DDX6, DNM2, EPS15, ERAP1, EXOC5, FLII, GALM, GET3, DGLUCY, GYS1, HNRNPH1, KLC1, LRP1, MGMT, NUCB1, PALLD, PLEC, PPP1R21, PTPN23, GART, CRYZ, RSU1, SAE1, SELENBP1, PSAT1, SFXN1, SFXN3, SKIC2, SNX5, SUMF2, SYNE1, TMT1A, UMPS, VAC14, ZW10

### Function

The strongest functional interpretation is lipid handling centered on cholesterol efflux. The globally corrected GO evidence is the paired enrichment for regulation of cholesterol efflux (GO:BP regulation of cholesterol efflux; q_global = 0.0339) and positive regulation of cholesterol efflux (GO:BP positive regulation of cholesterol efflux; q_global = 0.0339), supported by APOA1, APOE, and LRP1. APOA1 is the principal HDL protein and promotes cholesterol efflux; APOE participates in lipoprotein transport and receptor-mediated uptake; and LRP1 contributes to lipid homeostasis, receptor-mediated endocytosis, and clearance of apoptotic material. The module also contains secondary signals consistent with intracellular trafficking, cytoskeletal organization, RNA metabolism, nucleotide synthesis, DNA repair, and cell-cycle control, but these are gene-level annotations rather than globally corrected module functions. No STRING functional enrichment was reported. Thus, the most defensible interpretation is a cholesterol-efflux and lipoprotein-clearance module embedded in a broader cellular trafficking and metabolic context, rather than a narrowly defined canonical complex.

**Cell composition.** This is not predominantly a plasma or secreted-protein module. APOA1 and APOE are secreted to blood, while LRP1 is an intracellular and membrane protein; the remaining genes are largely intracellular. The HPA profile suggests a mixed-composition module rather than a uniformly tissue-specific program: many genes have low tissue specificity, while other genes are enhanced in liver, skeletal muscle, brain, kidney, or reproductive cell types. Hepatocyte and liver representation is notable, and several genes show neutrophil, basophil, dendritic-cell, or other immune-cell enrichment. Protein detection is broad in both tissues, especially in testis, but several genes are absent from one tissue. Consequently, the shared signal may partly reflect common cell types, circulating lipoprotein biology, or tissue composition rather than a mechanism unique to bone marrow and testis. The presence of immune-cell and hepatocyte-associated genes also warrants caution about blood-derived or stromal contributions in bone-marrow samples.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulation of cholesterol efflux | 0.0339 | APOA1, APOE, LRP1 |
| GO:BP positive regulation of cholesterol efflux | 0.0339 | APOA1, APOE, LRP1 |

### STRING and hu.MAP

STRING supports a small set of high-confidence relationships rather than a densely interconnected module. The most directly relevant known interactions are APOA1–APOE and APOE–LRP1, which independently support a lipoprotein and cholesterol-handling axis. Other known STRING relationships connect DNM2 with EPS15, GART with UMPS, and PLEC with SYNE1, supporting endocytosis, purine or nucleotide metabolism, and cytoskeletal organization, respectively. No STRING functional enrichment was detected. hu.MAP provides partial complex-level support: CIAO1, UMPS, and ATXN10 occur together in (hu.MAP huMAP3_09042.1); ZW10, CIAO1, and DNM2 occur together in (hu.MAP huMAP3_11232.1); UMPS and GART occur together in (hu.MAP huMAP3_10240.1); and ALDH3A2 and ATXN10 occur together in (hu.MAP huMAP3_09592.1). These complexes contain many proteins outside the module, so they support fragments of the network rather than a single unified complex. Overall, the evidence indicates a co-abundance network assembled from several biologically recognizable substructures, with the lipoprotein interaction pair being the clearest functional core.

**STRING interactions (score >= 0.7)**: 5 of 990 gene pairs: APOA1–APOE (0.999); APOE–LRP1 (0.999); DNM2–EPS15 (0.867); GART–UMPS (0.956); PLEC–SYNE1 (0.828)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09042.1 (CIAO1, UMPS, ATXN10; 3/26); huMAP3_11232.1 (ZW10, CIAO1, DNM2; 3/78); huMAP3_10240.1 (UMPS, GART; 2/12); huMAP3_09592.1 (ALDH3A2, ATXN10; 2/95)

### Novelty

This module should not be called a newly discovered molecular complex. Its central lipoprotein relationships are already well represented in STRING, and several other relationships are supported by STRING or hu.MAP. The potentially novel aspect is the reproducible co-abundance association of these genes across bone marrow and testis, particularly the juxtaposition of a cholesterol-efflux axis with metabolic, trafficking, cytoskeletal, and reproductive-cell-associated genes. However, absence of many module edges from STRING or hu.MAP does not establish novelty, because those resources emphasize curated or experimentally supported physical and functional relationships, whereas co-abundance can arise from shared regulation, cell composition, or tissue physiology. A novelty claim therefore requires independent replication, control for cell-type composition and circulating proteins, and comparison with published cross-tissue co-expression modules.

**Hypothesis.** Hypothesis: the module reflects coordinated handling of extracellular lipids and membrane-derived material in shared stromal, myeloid, or other support-cell populations present in bone marrow and testis. APOA1 and APOE may provide or bind lipoprotein cargo, while LRP1 may mediate uptake and clearance. Endosomal and vesicle-trafficking genes such as EPS15, DNM2, EXOC5, SNX5, and PPP1R21, together with cytoskeletal genes such as PLEC, SYNE1, FLII, and PALLD, could support cargo internalization and intracellular routing. The metabolic and biosynthetic genes may reflect the energetic and nucleotide demands of these cells rather than a single pathway. This hypothesis predicts that the apparent module should weaken after adjustment for hepatocyte, myeloid, neutrophil, and plasma-protein contamination, but any residual APOA1–APOE–LRP1 coordination may represent local lipid transport or clearance biology shared by the two tissues.

### Important genes

#### APOA1

- **Related proteins** (co-abundance neighbors): ADK (0.87), ERAP1 (0.86), SUMF2 (0.83), DGLUCY (0.82), NUCB1 (0.82), CRYZ (0.80); STRING partners: APOE (0.999)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is one of the three genes in both globally corrected cholesterol-efflux terms (GO:BP regulation of cholesterol efflux; q_global = 0.0339) and (GO:BP positive regulation of cholesterol efflux; q_global = 0.0339). It is the major HDL protein, promotes cholesterol efflux, and is secreted to blood. It has a direct high-confidence STRING relationship with APOE and the largest literature volume among the selected lipid-axis genes, with established associations to apolipoprotein A-I deficiency and hypoalphalipoproteinemia. Its network degree is moderate rather than hub-like, so its importance is primarily functional and interpretive rather than topological.
- **Conclusion**: Established evidence supports APOA1 as a central marker of the module's cholesterol-efflux interpretation. Its absence from detected protein in the sampled bone marrow and testis, together with blood secretion, means that the co-abundance signal could reflect circulating or blood-derived material. A local tissue role remains a hypothesis requiring protein localization and cell-resolved validation.

#### APOE

- **Related proteins** (co-abundance neighbors): TMT1A (0.83); STRING partners: APOA1 (0.999), LRP1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein E. The protein encoded by this gene is a major apoprotein of the chylomicron. It binds to a specific liver and peripheral cell receptor, and is essential for the normal catabolism of triglyceride-rich lipoprotein constituents. This gene maps to chromosome 19 in a cluster with the related apolipoprotein C1 and C2 genes. Mutations in this gene result in familial dysbetalipoproteinemia, or type III hype…
- **Diseases (Open Targets)**: hyperlipoproteinemia type 3 (0.803); coronary artery disorder (0.782); lipoprotein glomerulopathy (0.759); Alzheimer disease (0.696); familial hypercholesterolemia (0.651)
- **Europe PMC papers**: 74272
- **Why important**: APOE is present in both globally corrected cholesterol-efflux terms (GO:BP regulation of cholesterol efflux; q_global = 0.0339) and (GO:BP positive regulation of cholesterol efflux; q_global = 0.0339). It is a secreted apoprotein involved in lipoprotein transport, triglyceride metabolism, and receptor-mediated endocytosis. It has high-confidence STRING relationships with both APOA1 and LRP1, forming the clearest known interaction bridge in the module. APOE also has an extensive literature base and established disease associations including dysbetalipoproteinemia, coronary artery disease, lipoprotein glomerulopathy, and Alzheimer disease.
- **Conclusion**: Established evidence places APOE at the center of the module's lipoprotein-handling signal and provides a plausible bridge between extracellular lipid cargo and cellular uptake. Because APOE is secreted and broadly associated with blood and liver biology, its presence does not by itself demonstrate a testis-specific or bone-marrow-specific mechanism.

#### LRP1

- **Related proteins** (co-abundance neighbors): FLII (0.85), SYNE1 (0.81); STRING partners: APOE (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LDL receptor related protein 1. This gene encodes a member of the low-density lipoprotein receptor family of proteins. The encoded preproprotein is proteolytically processed by furin to generate 515 kDa and 85 kDa subunits that form the mature receptor (PMID: 8546712). This receptor is involved in several cellular processes, including intracellular signaling, lipid homeostasis, and clearance of apoptotic cells. In addition, the …
- **Diseases (Open Targets)**: neurodegenerative disease (0.514); keratosis pilaris atrophicans (0.499); developmental dysplasia of the hip (0.466); Alzheimer disease (0.462); Parkinson disease (0.443)
- **Europe PMC papers**: 10645
- **Why important**: LRP1 is the third gene in both globally corrected cholesterol-efflux terms (GO:BP regulation of cholesterol efflux; q_global = 0.0339) and (GO:BP positive regulation of cholesterol efflux; q_global = 0.0339). It is a plasma-membrane receptor involved in lipid homeostasis, receptor-mediated endocytosis, phagocytosis, and clearance of apoptotic cells. Its high-confidence STRING relationship with APOE supports a receptor-mediated lipoprotein-clearance axis. HPA places it in adipose-associated and hepatocyte, Kupffer-cell, and fibroblast-related contexts, and it has a substantial literature base with associations to neurodegenerative, skeletal, and inflammatory disease contexts.
- **Conclusion**: Established evidence supports LRP1 as the likely cellular uptake and clearance component of the cholesterol-efflux interpretation. Its absence from detected bone-marrow protein and detection in testis argue against assuming uniform activity in both tissues. A shared role in phagocytic or stromal cells is a plausible hypothesis, not an established conclusion from this module alone.

#### GALM

- **Related proteins** (co-abundance neighbors): CIAO1 (0.94), PLEC (0.91), EPS15 (0.91), GET3 (0.90), PSAT1 (0.89), MGMT (0.88), SAE1 (0.88), VAC14 (0.88), GYS1 (0.87), CPPED1 (0.87), SKIC2 (0.86), DNM2 (0.86), ATXN10 (0.85), KLC1 (0.84), UMPS (0.83), ALDH3A2 (0.83), ZW10 (0.82), RSU1 (0.81), SFXN3 (0.81), ANXA7 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galactose mutarotase. This gene encodes an enzyme that catalyzes the epimerization of hexose sugars such as glucose and galactose. The encoded protein is expressed in the cytoplasm and has a preference for galactose. The encoded protein may be required for normal galactose metabolism by maintaining the equilibrium of alpha and beta anomers of galactose.[provided by RefSeq, Mar 2009].
- **Diseases (Open Targets)**: galactosemia 4 (0.786); hypothyroidism (0.383); Abnormality of the skeletal system (0.356); sialolithiasis (0.283); alcohol drinking (0.277)
- **Europe PMC papers**: 2116
- **Why important**: GALM is the strongest network connector in the supplied subgraph and links many otherwise separate genes, including CIAO1, PLEC, EPS15, GET3, PSAT1, MGMT, SAE1, and VAC14. It encodes a galactose mutarotase involved in hexose and galactose metabolism and is detected in both tissues. Unlike the lipoprotein genes, it has no reported STRING partner, hu.MAP membership, or globally corrected GO or KEGG term in this module. Its extensive literature and disease associations provide biological context, but not a direct link to cholesterol efflux.
- **Conclusion**: Established evidence supports GALM as a topological coordinator and a carbohydrate-metabolism marker, but not as a validated driver of the module's lipid function. Its hub-like position may reflect shared metabolic state, indirect co-regulation, or sample composition. A mechanistic connection between GALM activity and the APOA1–APOE–LRP1 axis is currently hypothetical.

#### UMPS

- **Related proteins** (co-abundance neighbors): GALM (0.83); STRING partners: GART (0.956)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09042.1, huMAP3_10240.1
- **Function (MyGene.info)**: uridine monophosphate synthetase. This gene encodes a uridine 5'-monophosphate synthase. The encoded protein is a bifunctional enzyme that catalyzes the final two steps of the de novo pyrimidine biosynthetic pathway. The first reaction is carried out by the N-terminal enzyme orotate phosphoribosyltransferase which converts orotic acid to orotidine-5'-monophosphate. The terminal reaction is carried out by the C-terminal enzyme OMP …
- **Diseases (Open Targets)**: orotic aciduria (0.773); coronary artery disorder (0.507); Intellectual disability (0.462); open-angle glaucoma (0.381); Abnormality of the skeletal system (0.374)
- **Europe PMC papers**: 965
- **Why important**: UMPS is supported by the GART–UMPS STRING relationship and occurs with CIAO1 and GART in hu.MAP complexes (hu.MAP huMAP3_09042.1) and (hu.MAP huMAP3_10240.1). It catalyzes the terminal steps of de novo pyrimidine synthesis and is therefore relevant to nucleotide supply in proliferating or metabolically active cells. It is detected in both tissues, although it is not included in the globally corrected GO terms. Its established disease association with orotic aciduria gives it a clear functional and clinical anchor.
- **Conclusion**: Established evidence supports UMPS as a nucleotide-biosynthetic component and as part of a known GART-associated substructure within the module. Its relationship to cholesterol efflux is not established. The most cautious interpretation is that UMPS marks a parallel biosynthetic or proliferative program superimposed on the lipid-handling signal.

## Module 2

**Tissue pair**: bone_marrow and testis  
**Genes (31)**: GOT2, ABCF1, AIFM1, ATXN2L, CLTC, HSD17B4, DHX9, ADAR, GXYLT1, HPRT1, HSPH1, IDH3A, MCM6, NAA15, NNT, NT5DC1, PDHB, PSMC4, ADSL, CAD, RAD50, SF3A1, SMC2, EPRS1, MARS1, TRAP1, TSPYL5, SNRNP200, EFTUD2, UGGT1, XPO1

### Function

The strongest supported interpretation is a broadly expressed nucleic-acid and RNA-handling module. (GO:MF nucleic acid binding; q_global = 0.00488) is the only GO/KEGG term that passed global correction, linking much of the module to nucleic acid binding. The module also contains a coherent spliceosomal and RNA-processing component: SF3A1, EFTUD2, SNRNP200, DHX9, ADAR and XPO1 are supported by their individual annotations and by (STRING Function Nucleic acid binding; within-query FDR = 0.0051), (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.0408) and (STRING Function RNA binding; within-query FDR = 0.041). A second component comprises translation-related factors, including EPRS1, MARS1 and ABCF1, together with nucleotide, amino-acid and mitochondrial metabolic proteins. DNA replication, chromosome organization, repair, proteostasis and mitochondrial stress functions are plausible accompanying activities because of MCM6, SMC2, RAD50, PSMC4, TRAP1, NNT, AIFM1 and related annotations. Thus, the module is best viewed as a general cellular gene-expression, RNA-processing and biosynthetic-support program rather than a narrowly tissue-specific pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a small secreted component, and most proteins are intracellular. It is also not strongly blood-cell specific. HPA assigns low immune-cell specificity to most genes, with only a small immune-enhanced component and one gene not detected in immune cells. Most genes have low tissue specificity, and protein detection is broad in both bone marrow and testis. Some genes show enrichment in late spermatids, spermatocytes, erythrocyte or megakaryocyte progenitors, neutrophils, hepatocytes, muscle, tongue or choroid plexus, but these patterns are distributed rather than forming a single dominant cell-type signature. The shared module could therefore reflect broadly expressed housekeeping and proliferative machinery present in cells from both tissues, with contributions from shared germ-cell or hematopoietic cell states. The HPA observations do not support interpreting it primarily as a blood-contamination or secreted-protein module.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleic acid binding | 0.00488 | ABCF1, ADAR, AIFM1, ATXN2L, CLTC, DHX9, EFTUD2, EPRS1, GOT2, MARS1, MCM6, NAA15, RAD50, SF3A1, SMC2, SNRNP200, TRAP1, XPO1 |

### STRING and hu.MAP

STRING supports a real, but incomplete, interaction structure. The strongest known relationships are the spliceosomal links among EFTUD2, SF3A1 and SNRNP200, the DHX9 links to ABCF1, ADAR, SNRNP200 and XPO1, and the EPRS1--MARS1 pair. STRING also supports metabolic relationships involving CAD, GOT2, IDH3A, NNT, PDHB, ADSL and HPRT1, plus the MCM6--SMC2 pair and the GXYLT1--UGGT1 pair. These relationships show that several parts of the co-abundance module correspond to established molecular systems rather than being arbitrary gene associations. hu.MAP independently identifies a spliceosomal complex containing SNRNP200, EFTUD2 and SF3A1, repeated related complexes containing SNRNP200 and EFTUD2, and aminoacyl-tRNA synthetase complexes containing EPRS1 and MARS1. It also identifies a complex containing ADSL, TRAP1 and NT5DC1. The partial overlap between the module and these complexes supports known substructures, while the many module genes without matching STRING or hu.MAP relationships indicate that co-abundance extends beyond currently catalogued physical complexes.

**STRING interactions (score >= 0.7)**: 17 of 465 gene pairs: ABCF1–DHX9 (0.921); ADAR–DHX9 (0.922); ADSL–HPRT1 (0.935); ADSL–IDH3A (0.834); CAD–GOT2 (0.931); DHX9–SNRNP200 (0.784); DHX9–XPO1 (0.791); EFTUD2–EPRS1 (0.744); EFTUD2–SF3A1 (0.999); EFTUD2–SNRNP200 (0.999); EPRS1–MARS1 (0.999); GOT2–IDH3A (0.889); GXYLT1–UGGT1 (0.915); IDH3A–NNT (0.726); IDH3A–PDHB (0.856); MCM6–SMC2 (0.75); SF3A1–SNRNP200 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Nucleic acid binding (FDR = 0.0051, 18 genes); Function Organic cyclic compound binding (FDR = 0.0207, 24 genes); Function Heterocyclic compound binding (FDR = 0.0207, 24 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 0.0408, 8 genes); Function RNA binding (FDR = 0.041, 14 genes); Function ATP hydrolysis activity (FDR = 0.0413, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (ADSL, TRAP1, NT5DC1; 3/57); huMAP3_08980.1 (SNRNP200, EFTUD2, SF3A1; 3/97); huMAP3_00960.1 (SNRNP200, EFTUD2; 2/8); huMAP3_07622.1 (SNRNP200, EFTUD2; 2/9); huMAP3_02637.1 (EPRS1, MARS1; 2/14); huMAP3_13688.1 (EPRS1, MARS1; 2/14); huMAP3_08501.1 (SNRNP200, EFTUD2; 2/47); huMAP3_09504.1 (SNRNP200, EFTUD2; 2/51); huMAP3_09945.1 (SNRNP200, EFTUD2; 2/61)

### Novelty

This is potentially a new cross-tissue co-abundance configuration, but the fact sheet does not establish that it is a wholly new biological pathway. The spliceosome, RNA helicase, aminoacyl-tRNA synthetase, nucleotide-metabolism and mitochondrial components are individually well established, and several of their pairwise relationships are already present in STRING or hu.MAP. What may be novel is their coordinated abundance pattern shared by bone marrow and testis, including the connection between a central RNA-processing core and metabolic, stress-response and genome-maintenance proteins. The absence of some relationships from STRING or hu.MAP cannot by itself demonstrate novelty, because those resources are incomplete and primarily describe physical or curated associations rather than tissue-pair co-abundance. A defensible conclusion is therefore that the module contains established biology arranged in a potentially novel tissue-shared network state, requiring replication and independent experimental validation.

**Hypothesis.** Hypothesis: cells represented in both bone marrow and testis coordinate high RNA-processing capacity with biosynthetic and metabolic support to sustain proliferation, differentiation or specialized developmental programs. The spliceosomal core may regulate transcript maturation through EFTUD2, SF3A1, SNRNP200 and DHX9, while ADAR and XPO1 could influence RNA editing and nuclear transport. EPRS1, MARS1 and ABCF1 may support translation, and CAD, HPRT1, ADSL, GOT2, IDH3A, PDHB and NNT may provide nucleotide, amino-acid, carbon-flow and redox support. MCM6, SMC2 and RAD50 could connect this state to replication, chromosome organization and DNA repair, while TRAP1 and HSPH1 could buffer mitochondrial or proteotoxic stress. This is a mechanistic model rather than a demonstrated causal pathway; it predicts coordinated changes in RNA splicing, translation, nucleotide metabolism and cellular stress responses across relevant bone-marrow and testis cell populations.

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.91), NNT (0.91), CAD (0.89), SF3A1 (0.88), ABCF1 (0.86), ATXN2L (0.83), HSD17B4 (0.83), HSPH1 (0.82), ADAR (0.82), MCM6 (0.80), SNRNP200 (0.80); STRING partners: ABCF1 (0.921), ADAR (0.922), SNRNP200 (0.784), XPO1 (0.791)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is among the most central genes in the co-abundance subgraph and connects the RNA-processing core to ABCF1, ADAR, SNRNP200 and XPO1 in STRING. It is the only selected gene with direct support across the global enrichment (GO:MF nucleic acid binding; q_global = 0.00488) and the broad STRING evidence (STRING Function Nucleic acid binding; within-query FDR = 0.0051), (STRING Function Organic cyclic compound binding; within-query FDR = 0.0207), (STRING Function Heterocyclic compound binding; within-query FDR = 0.0207), (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.0408), (STRING Function RNA binding; within-query FDR = 0.041) and (STRING Function ATP hydrolysis activity; within-query FDR = 0.0413). Its annotation supports ATP-dependent unwinding of RNA and DNA-RNA complexes, alternative splicing, transcriptional regulation and interferon-related functions. Its disease and literature record is substantial, making it a strong integrative anchor.
- **Conclusion**: Established evidence supports DHX9 as a central RNA and nucleic-acid-processing factor in this module. It is reasonable to hypothesize that DHX9 helps connect spliceosomal activity with RNA remodeling and stress or antiviral responses, but the co-abundance data do not prove that it is causally upstream.

#### SF3A1

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.95), EPRS1 (0.89), DHX9 (0.88), HSPH1 (0.87), XPO1 (0.86), ATXN2L (0.84), UGGT1 (0.81), AIFM1 (0.81); STRING partners: EFTUD2 (0.999), SNRNP200 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 is a highly connected module gene and is a defined component of the U2 small nuclear ribonucleoprotein and spliceosome. It has direct global support through (GO:MF nucleic acid binding; q_global = 0.00488), strong STRING relationships with EFTUD2 and SNRNP200, and membership in hu.MAP spliceosomal complex (hu.MAP huMAP3_08980.1). Its HPA profile is broadly expressed while also showing cell-type enhancement in late spermatids and neutrophils, fitting the shared tissue context.
- **Conclusion**: Established evidence identifies SF3A1 as a core spliceosomal component and a principal structural marker of the module's RNA-processing arm. A tissue-shared change in SF3A1 abundance could indicate altered pre-mRNA processing, but no specific transcript target or tissue-specific splicing consequence is established here.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): SF3A1 (0.95), DHX9 (0.91), SNRNP200 (0.86), HSPH1 (0.86), NNT (0.83), CAD (0.80), ATXN2L (0.80); STRING partners: EPRS1 (0.744), SF3A1 (0.999), SNRNP200 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 occupies a central position in the module and has very strong STRING links to SF3A1 and SNRNP200. It is present in multiple hu.MAP complexes (hu.MAP huMAP3_08980.1), (hu.MAP huMAP3_00960.1), (hu.MAP huMAP3_07622.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1) and (hu.MAP huMAP3_09945.1), and is supported by (GO:MF nucleic acid binding; q_global = 0.00488) and the major STRING RNA-processing terms. Its established function in spliceosomal tri-snRNP assembly and spliceosome conformational change gives the module a concrete molecular process rather than only a generic nucleic-acid label. Its association with mandibulofacial dysostosis and developmental disorders also underscores the functional importance of accurate RNA processing.
- **Conclusion**: Established evidence supports EFTUD2 as a core spliceosome-associated component and one of the most informative genes for interpreting this module. The hypothesis that it mediates a shared differentiation-related RNA-processing state remains untested by the supplied data.

#### NNT

- **Related proteins** (co-abundance neighbors): EPRS1 (0.91), DHX9 (0.91), CAD (0.90), MARS1 (0.88), HSD17B4 (0.88), ABCF1 (0.85), PSMC4 (0.85), EFTUD2 (0.83), PDHB (0.82), ADSL (0.82), CLTC (0.81); STRING partners: IDH3A (0.726)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nicotinamide nucleotide transhydrogenase. This gene encodes an integral protein of the inner mitochondrial membrane. The enzyme couples hydride transfer between NAD(H) and NADP(+) to proton translocation across the inner mitochondrial membrane. Under most physiological conditions, the enzyme uses energy from the mitochondrial proton gradient to produce high concentrations of NADPH. The resulting NADPH is used for biosynthesis and in free …
- **Diseases (Open Targets)**: familial glucocorticoid deficiency (0.638); neurodegenerative disease (0.497); hereditary disease (0.453); atypical hemolytic-uremic syndrome with DGKE deficiency (0.416); Abnormality of the skeletal system (0.396)
- **Europe PMC papers**: 6111
- **Why important**: NNT has the strongest network centrality in the supplied module structure and links RNA-associated genes to CAD, HSD17B4, PSMC4 and mitochondrial metabolism. Its annotation identifies an inner-mitochondrial-membrane enzyme that generates NADPH for biosynthesis and reactive-oxygen control. Although it is not part of (GO:MF nucleic acid binding; q_global = 0.00488) and has no hu.MAP assignment, its network position and STRING connection to IDH3A provide a bridge from the nucleic-acid-rich core to redox and energy metabolism. HPA shows tissue enhancement in skeletal muscle and tongue but low immune-cell specificity.
- **Conclusion**: Established evidence supports NNT as a mitochondrial redox and biosynthetic-support factor embedded in the module. It may help maintain redox capacity during RNA production, proliferation or differentiation, but that bridging role is a hypothesis rather than a demonstrated function of this co-abundance module.

#### CAD

- **Related proteins** (co-abundance neighbors): NNT (0.90), DHX9 (0.89), SMC2 (0.87), HSD17B4 (0.80), EFTUD2 (0.80), HPRT1 (0.80); STRING partners: GOT2 (0.931)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carbamoyl-phosphate synthetase 2, aspartate transcarbamylase, and dihydroorotase. The de novo synthesis of pyrimidine nucleotides is required for mammalian cells to proliferate. This gene encodes a trifunctional protein which is associated with the enzymatic activities of the first 3 enzymes in the 6-step pathway of pyrimidine biosynthesis: carbamoylphosphate synthetase (CPS II), aspartate transcarbamoylase, and dihydroorotase. This protein is regulated by the mitogen-activated…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 50 (0.660); congenital disorder of glycosylation type I (0.595); infantile epileptic-dyskinetic encephalopathy (0.499); type 2 diabetes mellitus (0.286); urolithiasis (0.283)
- **Europe PMC papers**: 60667
- **Why important**: CAD connects several central module genes, including NNT, DHX9, SMC2, HSD17B4, EFTUD2 and HPRT1. Its established trifunctional activity catalyzes the early steps of de novo pyrimidine biosynthesis, providing a direct link between the module and nucleotide supply. STRING supports its relationship with GOT2, and the supplementary binding terms (STRING Function Organic cyclic compound binding; within-query FDR = 0.0207) and (STRING Function Heterocyclic compound binding; within-query FDR = 0.0207) include CAD. Its literature volume is especially extensive, and its disease associations include developmental and epileptic encephalopathy.
- **Conclusion**: Established evidence supports CAD as a nucleotide-biosynthesis component that could support transcription, replication and cell growth. The proposed coupling of CAD abundance to the module's spliceosomal state is biologically plausible but not proven by the available enrichment or interaction evidence.

## Module 3

**Tissue pair**: bone_marrow and testis  
**Genes (36)**: ABCD3, AP1B1, ASCC3, CNOT1, COMMD3, COPG2, EIF2B4, EML2, GMPR, EIF4G3, KIFBP, PRPSAP2, MCCC1, MTR, NAA50, NUP107, PI4KA, PIGS, PRPS2, RALGAPB, MRPS27, RUSF1, SEC23B, SEH1L, SYMPK, TIMM29, TNPO3, USP15, USP5, UQCC1, VPS33A, VPS11, VPS41, VPS50, VPS53, CSE1L

### Function

The strongest supported function is intracellular membrane trafficking and vesicle organization. The globally corrected GO evidence identifies membrane coat and coated membrane (GO:CC membrane coat; q_global = 0.0281) (GO:CC coated membrane; q_global = 0.0281), driven by AP1B1, COPG2, SEC23B, VPS11, VPS33A, and VPS41. This points to coated-vesicle formation, cargo sorting, and trafficking between the endoplasmic reticulum, Golgi, endosomes, and lysosomes. The HOPS or CORVET interpretation is especially well supported for VPS11, VPS33A, and VPS41 by their shared hu.MAP complexes (hu.MAP huMAP3_08749.1) (hu.MAP huMAP3_13822.1) (hu.MAP huMAP3_12433.1) (hu.MAP huMAP3_12945.1) (hu.MAP huMAP3_02792.1) and their strong STRING relationships. STRING protein-transport enrichment is supplementary rather than primary evidence (STRING Keyword Protein transport; within-query FDR = 0.01). Other genes indicate additional cellular processes, including nuclear transport, translation control, nucleotide metabolism, mitochondrial function, and protein quality regulation. Thus, this is best interpreted as a membrane-trafficking-centered module with a broader background of constitutive cellular maintenance machinery, rather than as a single complete biochemical complex.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and the protein is detected in both tissues for most of the module, supporting broadly expressed intracellular biology rather than a tissue-restricted secretome. HPA reports low immune-cell specificity for most genes, with only limited immune-cell enhancement involving basophils or neutrophils. Cell-type-enhanced signals include spermatocyte and spermatid populations, erythrocyte progenitors, megakaryocytes, neutrophil-lineage cells, and several neural or epithelial cell types. Therefore, the shared signal could reflect common intracellular machinery across bone-marrow and testis cell populations, including proliferating or differentiating cells, rather than contamination by circulating plasma proteins. The testis and bone-marrow overlap should nevertheless be interpreted with cell-composition effects in mind, especially because several genes are enhanced in germ-cell or hematopoietic progenitor populations.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC membrane coat | 0.0281 | AP1B1, COPG2, SEC23B, VPS11, VPS33A, VPS41 |
| GO:CC coated membrane | 0.0281 | AP1B1, COPG2, SEC23B, VPS11, VPS33A, VPS41 |

### STRING and hu.MAP

Known physical or functional relationships are concentrated in a few components. VPS11, VPS33A, and VPS41 form a strongly supported interaction group in STRING and recur together across several hu.MAP complexes (hu.MAP huMAP3_08749.1) (hu.MAP huMAP3_13822.1) (hu.MAP huMAP3_12433.1) (hu.MAP huMAP3_12945.1) (hu.MAP huMAP3_02792.1), consistent with the HOPS or CORVET machinery. VPS53 and VPS50 form a separate known pair in STRING and recur in GARP or EARP-related hu.MAP complexes (hu.MAP huMAP3_03896.1) (hu.MAP huMAP3_13708.1). NUP107 and SEH1L form a known nucleoporin pair and recur in nuclear-pore complexes (hu.MAP huMAP3_07705.1) (hu.MAP huMAP3_07492.1) (hu.MAP huMAP3_08489.1) (hu.MAP huMAP3_09710.1) (hu.MAP huMAP3_09825.1) (hu.MAP huMAP3_12581.1). PRPS2 and PRPSAP2 form another known pair and recur in phosphoribosyl-pyrophosphate-associated complexes (hu.MAP huMAP3_10201.1) (hu.MAP huMAP3_14146.1) (hu.MAP huMAP3_10941.1) (hu.MAP huMAP3_11883.1) (hu.MAP huMAP3_13128.1) (hu.MAP huMAP3_12561.1). The module also contains known or plausible complex membership involving AP1B1 and SEC23B (hu.MAP huMAP3_12394.1), and TNPO3 with EIF2B4 in broad hu.MAP assemblies (hu.MAP huMAP3_05832.1) (hu.MAP huMAP3_10202.1) (hu.MAP huMAP3_10287.1) (hu.MAP huMAP3_11232.1). However, most within-module pairs are not supported by high-confidence STRING links. This pattern suggests that the module combines several established cellular subsystems connected by co-abundance, rather than representing one fully resolved physical complex.

**STRING interactions (score >= 0.7)**: 7 of 630 gene pairs: NUP107–SEH1L (0.999); PRPS2–PRPSAP2 (0.981); TNPO3–VPS53 (0.778); VPS11–VPS33A (0.999); VPS11–VPS41 (0.999); VPS33A–VPS41 (0.999); VPS50–VPS53 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Protein transport (FDR = 0.01, 13 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08749.1 (VPS41, VPS33A, VPS11; 3/9); huMAP3_13822.1 (VPS41, VPS33A, VPS11; 3/9); huMAP3_12433.1 (VPS41, VPS33A, VPS11; 3/11); huMAP3_12945.1 (VPS41, VPS33A, VPS11; 3/12); huMAP3_02792.1 (VPS41, VPS33A; 2/5); huMAP3_03896.1 (VPS53, VPS50; 2/7); huMAP3_13708.1 (VPS53, VPS50; 2/8); huMAP3_07705.1 (NUP107, SEH1L; 2/9); huMAP3_10201.1 (PRPSAP2, PRPS2; 2/10); huMAP3_14146.1 (PRPSAP2, PRPS2; 2/10); huMAP3_07492.1 (NUP107, SEH1L; 2/10); huMAP3_08489.1 (NUP107, SEH1L; 2/10); huMAP3_10941.1 (PRPSAP2, PRPS2; 2/12); huMAP3_09710.1 (NUP107, SEH1L; 2/13); huMAP3_05832.1 (EIF2B4, TNPO3; 2/14); huMAP3_11883.1 (PRPSAP2, PRPS2; 2/15); huMAP3_13128.1 (PRPSAP2, PRPS2; 2/17); huMAP3_12561.1 (PRPSAP2, PRPS2; 2/18); huMAP3_09825.1 (NUP107, SEH1L; 2/27); huMAP3_10202.1 (EIF2B4, TNPO3; 2/52); huMAP3_10287.1 (EIF2B4, TNPO3; 2/53); huMAP3_12581.1 (NUP107, SEH1L; 2/58); huMAP3_11232.1 (EIF2B4, TNPO3; 2/78); huMAP3_12394.1 (AP1B1, SEC23B; 2/98)

### Novelty

The module should not be described as a newly discovered molecular complex. Its clearest relationships involving HOPS or CORVET, GARP or EARP, nuclear-pore components, phosphoribosyl-pyrophosphate-associated proteins, and coated-vesicle machinery are already represented by STRING or hu.MAP. The potentially novel aspect is the coordinated abundance of these genes across bone marrow and testis, particularly the way membrane-trafficking components coexist with broadly expressed metabolic, nuclear-transport, and translation machinery. That cross-tissue co-abundance pattern may be a useful observation, but novelty cannot be established from absence of a STRING or hu.MAP relationship alone. Independent replication, comparison with published tissue co-expression studies, cell-type deconvolution, and perturbation would be required before claiming a new biological mechanism.

**Hypothesis.** Hypothesis: this conserved module reflects a shared demand for intracellular cargo sorting and organelle maintenance in differentiating bone-marrow and testis cells. The HOPS or CORVET-related VPS11, VPS33A, and VPS41 machinery may coordinate late-endosomal or lysosomal trafficking, while AP1B1, COPG2, and SEC23B support coated-vesicle formation and cargo movement through the secretory pathway. VPS53 and VPS50 may extend this trafficking system through retrograde or recycling pathways. The remaining genes may represent parallel requirements for nuclear transport, translation, nucleotide supply, mitochondrial activity, and protein turnover during cell differentiation. This is a mechanistic model, not a demonstrated causal connection, and the strong association with GMPR may partly reflect a co-abundance or cell-state effect rather than direct physical coupling.

### Important genes

#### VPS41

- **Related proteins** (co-abundance neighbors): PRPSAP2 (0.89), CSE1L (0.87), TNPO3 (0.85), GMPR (0.85); STRING partners: VPS11 (0.999), VPS33A (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: huMAP3_08749.1, huMAP3_13822.1, huMAP3_12433.1, huMAP3_12945.1, huMAP3_02792.1
- **Function (MyGene.info)**: VPS41 subunit of HOPS complex. Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene encodes the human ortholog of yeast Vps41 protein which is also conserved in Drosophila, tomato, and Arabidopsis. Expression studie…
- **Diseases (Open Targets)**: neurodegenerative disease (0.561); dystonic disorder (0.525); spinocerebellar ataxia, autosomal recessive 29 (0.517); Abnormality of the skeletal system (0.466); Intellectual disability (0.463)
- **Europe PMC papers**: 865
- **Why important**: VPS41 is the most informative trafficking anchor in the module. It participates in the globally supported membrane-coat terms (GO:CC membrane coat; q_global = 0.0281) (GO:CC coated membrane; q_global = 0.0281), is a HOPS-complex subunit, connects in STRING to VPS11 and VPS33A, and recurs with those genes across several hu.MAP complexes (hu.MAP huMAP3_08749.1) (hu.MAP huMAP3_13822.1) (hu.MAP huMAP3_12433.1) (hu.MAP huMAP3_12945.1) (hu.MAP huMAP3_02792.1). Its HPA profile is broadly expressed with protein detected in both tissues, making it compatible with a shared intracellular mechanism rather than a secreted or blood-specific signal. Its disease associations include neurodegenerative and dystonic disorders, and its literature supports an established role in vesicle-mediated protein sorting.
- **Conclusion**: Established evidence supports VPS41 as a core component of the module's endosomal and lysosomal trafficking interpretation. It is a strong mechanistic representative, but the co-abundance data do not establish that VPS41 controls the entire module or that the bone-marrow and testis signal has the same cellular cause.

#### VPS33A

- **Related proteins** (co-abundance neighbors): GMPR (0.93); STRING partners: VPS11 (0.999), VPS41 (0.999)
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08749.1, huMAP3_13822.1, huMAP3_12433.1, huMAP3_12945.1, huMAP3_02792.1
- **Function (MyGene.info)**: VPS33A core subunit of CORVET and HOPS complexes. This gene encodes a tethering protein and a core subunit of the homotypic fusion and protein sorting (HOPS) complex. The HOPS complex and a second endosomal tethering complex called the class C core vacuole/endosome tethering (CORVET) complex, perform diverse functions in endocytosis including membrane tethering, RabGTPase interaction, activation and proofreading of synaptic-soluble N-ethylmaleimi…
- **Diseases (Open Targets)**: mucopolysaccharidosis-plus syndrome (0.752); neurodegenerative disease (0.496); COVID-19 (0.370); placental abruption (0.198); retinitis pigmentosa (0.097)
- **Europe PMC papers**: 912
- **Why important**: VPS33A is a core HOPS or CORVET tethering component and belongs to the globally supported membrane-coat terms (GO:CC membrane coat; q_global = 0.0281) (GO:CC coated membrane; q_global = 0.0281). It has strong STRING links to VPS11 and VPS41 and recurs with them in hu.MAP complexes (hu.MAP huMAP3_08749.1) (hu.MAP huMAP3_13822.1) (hu.MAP huMAP3_12433.1) (hu.MAP huMAP3_12945.1) (hu.MAP huMAP3_02792.1). Its established functions include intracellular transport, endosome-to-lysosome transport, lysosome localization, and membrane-fusion support. It also has disease associations involving mucopolysaccharidosis-plus syndrome and neurodegeneration, with substantial literature supporting its cellular role.
- **Conclusion**: Established evidence identifies VPS33A as a central molecular anchor for the trafficking function. Its presence supports a real vesicle-tethering signal, while the module-level data alone do not show whether VPS33A activity is altered or merely co-regulated.

#### VPS11

- **Related proteins** (co-abundance neighbors): GMPR (0.84); STRING partners: VPS33A (0.999), VPS41 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_08749.1, huMAP3_13822.1, huMAP3_12433.1, huMAP3_12945.1
- **Function (MyGene.info)**: VPS11 core subunit of CORVET and HOPS complexes. Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene encodes the human homolog of yeast class C Vps11 protein. The mammalian class C Vps proteins are predominantly associated with late…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 12 (0.723); neurodegenerative disease (0.527); POLR-related leukodystrophy (0.527); dystonia 32 (0.410); VPS11-related neurological disorder (0.370)
- **Europe PMC papers**: 849
- **Why important**: VPS11 is the third member of the tightly supported VPS trafficking group. It belongs to the primary membrane-coat terms (GO:CC membrane coat; q_global = 0.0281) (GO:CC coated membrane; q_global = 0.0281), has very strong STRING links to VPS33A and VPS41, and recurs with both in several hu.MAP complexes (hu.MAP huMAP3_08749.1) (hu.MAP huMAP3_13822.1) (hu.MAP huMAP3_12433.1) (hu.MAP huMAP3_12945.1). Its annotations include endosome organization, vacuole organization, and endosome-to-lysosome transport. HPA shows cell-type enhancement in several neural cell types and protein detection in testis, while disease associations include leukodystrophy and VPS11-related neurological disorders.
- **Conclusion**: Established evidence supports VPS11 as a structural and functional partner of VPS41 and VPS33A, strengthening the HOPS or CORVET interpretation. A specific role for this trio in the shared tissue state remains a hypothesis.

#### GMPR

- **Related proteins** (co-abundance neighbors): RUSF1 (0.94), VPS33A (0.93), ASCC3 (0.92), USP15 (0.90), CNOT1 (0.90), EIF2B4 (0.90), ABCD3 (0.89), VPS50 (0.89), COPG2 (0.87), UQCC1 (0.87), USP5 (0.86), PI4KA (0.86), AP1B1 (0.86), PIGS (0.85), VPS41 (0.85), VPS11 (0.84), NAA50 (0.84), SEC23B (0.83), MCCC1 (0.83), SYMPK (0.82), KIFBP (0.82), VPS53 (0.82), PRPS2 (0.82), EML2 (0.81), SEH1L (0.81), EIF4G3 (0.81), MRPS27 (0.80), NUP107 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: guanosine monophosphate reductase. This gene encodes an enzyme that catalyzes the irreversible and NADPH-dependent reductive deamination of GMP to IMP. The protein also functions in the re-utilization of free intracellular bases and purine nucleosides.[provided by RefSeq, Oct 2009].
- **Diseases (Open Targets)**: chronic kidney disease (0.445); hypertrophic cardiomyopathy (0.333); Alzheimer disease (0.280); Abnormal blistering of the skin (0.273); disorder of appendix (0.258)
- **Europe PMC papers**: 740
- **Why important**: GMPR is the dominant network hub by weighted degree in the supplied module graph and links to many otherwise weakly connected module members, including VPS41, VPS50, SEC23B, and several regulatory or housekeeping genes. Its established function is NADPH-dependent conversion of GMP to IMP and purine nucleotide salvage. HPA shows enhancement in skeletal muscle and tongue and cell-type enhancement in differentiating spermatogonia, erythrocyte progenitors, and megakaryocytes, with basophil enhancement also reported. It has a substantial literature and disease associations including chronic kidney disease and hypertrophic cardiomyopathy.
- **Conclusion**: Established evidence supports GMPR as a purine-metabolism enzyme and a co-abundance hub. Its central network position makes it important for interpreting module structure, but the absence of STRING partners and direct pathway enrichment means that a physical or regulatory bridge from GMPR to the trafficking machinery is not established.

#### SEC23B

- **Related proteins** (co-abundance neighbors): GMPR (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Vesicles, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: SEC23 homolog B, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The function of this gene product has been implicated in cargo selection and concentration. Multiple alternativel…
- **Diseases (Open Targets)**: congenital dyserythropoietic anemia type 2 (0.834); Cowden syndrome 7 (0.730); congenital dyserythropoietic anemia (0.438); hereditary disease (0.194); hereditary ataxia (0.118)
- **Europe PMC papers**: 847
- **Why important**: SEC23B is one of the primary membrane-coat genes in (GO:CC membrane coat; q_global = 0.0281) and (GO:CC coated membrane; q_global = 0.0281), is included in the supplementary STRING protein-transport term (STRING Keyword Protein transport; within-query FDR = 0.01), and participates in a hu.MAP assembly with AP1B1 (hu.MAP huMAP3_12394.1). Its established function is COPII-coated vesicle budding and cargo loading from the endoplasmic reticulum toward the Golgi. HPA reports enhancement in neutrophils and protein detection in testis. Its disease associations include congenital dyserythropoietic anemia and Cowden syndrome, and its literature supports a well-established secretory-pathway role.
- **Conclusion**: Established evidence supports SEC23B as the strongest early secretory-pathway representative in the module and complements the late-endosomal VPS group. The shared tissue co-abundance does not by itself demonstrate altered COPII trafficking or a direct SEC23B interaction with the VPS machinery.

## Module 4

**Tissue pair**: bone_marrow and testis  
**Genes (32)**: ABHD10, ALDH1A2, DCPH1, ACOT7, BAG2, CHKB, CRLF3, MLYCD, TSFM, HSDL1, LACTB2, LYRM7, ME2, CHCHD3, MICAL1, AMDHD2, NUDCD1, NUP88, NUP98, PHB1, PHB2, PRUNE1, RAB27A, RNASET2, SLC75A1, SCAMP4, SCFD2, SMC4, SRPK2, IARS2, KARS1, TECR

### Function

This is a heterogeneous cellular maintenance module rather than a clearly defined pathway. No GO or KEGG term passed global correction, so there is no globally significant GO/KEGG annotation supporting a single statistically established biological function. The strongest mechanistic signals are mitochondrial organization and bioenergetic maintenance through PHB1, PHB2, and CHCHD3 in the hu.MAP complexes (hu.MAP huMAP3_10725.1), (hu.MAP huMAP3_01706.1), (hu.MAP huMAP3_09671.1), and (hu.MAP huMAP3_11743.1); nucleocytoplasmic transport and RNA export through NUP98 and NUP88 in complexes (hu.MAP huMAP3_05948.1), (hu.MAP huMAP3_06369.1), (hu.MAP huMAP3_10000.1), and (hu.MAP huMAP3_12581.1); mitochondrial translation through IARS2 and TSFM in (hu.MAP huMAP3_13468.1); and lipid or acyl-CoA metabolism through ALDH1A2, ACOT7, TECR, ME2, and MLYCD. The module therefore appears to combine conserved mitochondrial, nuclear-transport, translation, lipid-metabolic, and cell-structural programs. Its co-abundance may reflect a shared cellular state or cell-type mixture rather than one unified biochemical pathway. STRING supplied no enrichment result, so the functional interpretation should remain hypothesis-generating.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only a small minority are annotated as secreted, with RNASET2 being the clearest blood-secreted example. Most genes have low tissue specificity, and most have low immune-cell specificity, arguing against a module that is simply a plasma-protein signature. However, HPA single-cell evidence shows repeated enhancement in late primary spermatocytes, early or late spermatids, and neutrophil-related populations. Several genes are also enhanced in lymphoid tissue, megakaryocytes, platelets, or progenitors. Thus, the shared bone-marrow and testis signal could partly reflect common proliferative, mitochondrial, translational, or differentiation states and could also contain contributions from shared cell types. Protein detection is broadly compatible with the module in both tissues, although some genes lack tissue-level detection. The HPA pattern is therefore more consistent with broadly expressed cellular machinery overlaid by reproductive and hematopoietic cell-state effects than with a secreted-protein module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING identifies a small set of high-confidence known relationships: ACOT7 with TECR, IARS2 with KARS1, KARS1 with TSFM, NUP88 with NUP98, and PHB1 with PHB2. These links independently support local biochemical or structural units within the co-abundance network, especially the prohibitin pair, the nucleoporin pair, and the mitochondrial translation neighborhood. hu.MAP provides stronger complex-level context. PHB1 and PHB2 recur together in several complexes, with CHCHD3 joining them in the mitochondrial membrane and cristae-related complex (hu.MAP huMAP3_10725.1). NUP98 and NUP88 recur together in several nuclear-pore or nucleocytoplasmic-transport complexes (hu.MAP huMAP3_05948.1), (hu.MAP huMAP3_06369.1), (hu.MAP huMAP3_10000.1), and (hu.MAP huMAP3_12581.1). IARS2 and TSFM occur together in the large mitochondrial metabolic and translation-associated complex (hu.MAP huMAP3_13468.1). ACOT7 and ME2 recur in (hu.MAP huMAP3_05184.1) and (hu.MAP huMAP3_08042.1), while ME2 and LACTB2 occur in (hu.MAP huMAP3_14442.1). These resources show that several module edges correspond to known molecular relationships, but most module genes lack a reported STRING or hu.MAP relationship to another module member. The network is therefore a mixture of established molecular subunits and co-abundance links that remain unexplained.

**STRING interactions (score >= 0.7)**: 5 of 496 gene pairs: ACOT7–TECR (0.904); IARS2–KARS1 (0.995); KARS1–TSFM (0.809); NUP88–NUP98 (0.999); PHB1–PHB2 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10725.1 (PHB1, PHB2, CHCHD3; 3/59); huMAP3_01706.1 (PHB1, PHB2; 2/2); huMAP3_05948.1 (NUP98, NUP88; 2/5); huMAP3_05184.1 (ACOT7, ME2; 2/9); huMAP3_09671.1 (PHB1, PHB2; 2/10); huMAP3_11743.1 (PHB1, PHB2; 2/10); huMAP3_06369.1 (NUP98, NUP88; 2/12); huMAP3_08042.1 (ACOT7, ME2; 2/13); huMAP3_10000.1 (NUP98, NUP88; 2/44); huMAP3_14442.1 (ME2, LACTB2; 2/57); huMAP3_12581.1 (NUP98, NUP88; 2/58); huMAP3_13468.1 (TSFM, IARS2; 2/99)

### Novelty

The module-level observation may be novel as a conserved co-abundance pattern across bone marrow and testis, but the available evidence does not establish a new molecular complex or pathway. Several of its most interpretable relationships are already known from STRING or hu.MAP, including PHB1–PHB2, NUP98–NUP88, IARS2–TSFM, and the prohibitin, nucleoporin, and mitochondrial translation complexes. Conversely, the sparse STRING connectivity, lack of STRING enrichment, absence of globally significant GO or KEGG terms, and many genes without complex membership make the biological coherence of the full module uncertain. Absence from STRING or hu.MAP cannot demonstrate novelty because those resources are incomplete and are not designed to capture every co-expression or tissue-context relationship. The defensible conclusion is that the cross-tissue co-abundance pattern is potentially novel, whereas most individual molecular functions and several local relationships are established rather than newly discovered.

**Hypothesis.** Hypothesis: this module represents a coordinated cellular state supporting high biosynthetic and structural demand in selected bone-marrow and testis cell populations. Mitochondrial cristae organization through PHB1, PHB2, and CHCHD3 could help maintain respiratory capacity; IARS2 and TSFM could support mitochondrial protein synthesis; NUP98 and NUP88 could support nuclear import and RNA export; and ALDH1A2, ACOT7, TECR, ME2, and MLYCD could adjust retinoid, fatty-acid, and acyl-CoA metabolism. The repeated HPA association with spermatogenic cells and selected hematopoietic populations suggests that this state may accompany differentiation or rapid cellular turnover. This is a mechanistic hypothesis, not a demonstrated pathway, because global enrichment was absent and the module contains several disconnected functional neighborhoods.

### Important genes

#### ALDH1A2

- **Related proteins** (co-abundance neighbors): SCFD2 (0.94), SCAMP4 (0.92), LYRM7 (0.88), SMC4 (0.84), ME2 (0.82), RAB27A (0.81), ACOT7 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 1 family member A2. This protein belongs to the aldehyde dehydrogenase family of proteins. The product of this gene is an enzyme that catalyzes the synthesis of retinoic acid (RA) from retinaldehyde. Retinoic acid, the active derivative of vitamin A (retinol), is a hormonal signaling molecule that functions in developing and adult tissues. The studies of a similar mouse gene suggest that this enzyme and the cytochrom…
- **Diseases (Open Targets)**: diaphragmatic hernia 4, with cardiovascular defects (0.704); osteoarthritis, hand (0.464); osteoarthritis, knee (0.462); Knee pain (0.366); alcohol drinking (0.352)
- **Europe PMC papers**: 3482
- **Why important**: ALDH1A2 is the most connected and strongest hub in the supplied module network. It catalyzes retinoic-acid synthesis, has tissue enhancement in endometrium and fallopian tube, is enhanced in several stromal and epithelial cell types, and is associated with developmental and osteoarthritis-related disease annotations. Its links to SCFD2, SCAMP4, LYRM7, SMC4, ME2, RAB27A, and ACOT7 connect retinoid biology with vesicle trafficking, mitochondrial function, chromosome biology, and lipid metabolism. Its literature volume is substantial, making its annotation more established than that of several less studied module genes.
- **Conclusion**: Established evidence supports ALDH1A2 as a retinoic-acid biosynthetic enzyme and as a central co-abundance hub. It is a plausible regulator of tissue-specific differentiation or metabolic state, but the module data do not prove that retinoic-acid signaling drives the shared bone-marrow and testis pattern.

#### PHB1

- **Related proteins** (co-abundance neighbors): PHB2 (0.82); STRING partners: PHB2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: huMAP3_10725.1, huMAP3_01706.1, huMAP3_09671.1, huMAP3_11743.1
- **Function (MyGene.info)**: prohibitin 1. This gene is evolutionarily conserved, and its product is proposed to play a role in human cellular senescence and tumor suppression. Antiproliferative activity is reported to be localized to the 3' UTR, which is proposed to function as a trans-acting regulatory RNA. Several pseudogenes of this gene have been identified. Alternative splicing results in multiple transcript variants. [provided by Re…
- **Diseases (Open Targets)**: coronary artery disorder (0.458); myocardial ischemia (0.454); hypertensive disorder (0.396); heart disorder (0.343); asthma (0.339)
- **Europe PMC papers**: 1249
- **Why important**: PHB1 is a member of the strongest local molecular unit in the module: it forms a known STRING relationship with PHB2 and occurs with PHB2 in several hu.MAP complexes (hu.MAP huMAP3_10725.1), (hu.MAP huMAP3_01706.1), (hu.MAP huMAP3_09671.1), and (hu.MAP huMAP3_11743.1). It is mitochondrial, is detected in both tissues, and is annotated in mitochondrial organization, transcriptional regulation, osteoblast differentiation, and immunoglobulin production. Its disease and literature annotations are substantial. PHB1 also provides a bridge from the module to the mitochondrial cristae scaffold represented by CHCHD3.
- **Conclusion**: Established evidence supports PHB1 as part of the prohibitin complex and as a mitochondrial and regulatory protein. Its module membership is consistent with a conserved mitochondrial maintenance program, but the data do not establish a tissue-pair-specific role or a causal effect on hematopoietic or germ-cell biology.

#### PHB2

- **Related proteins** (co-abundance neighbors): CHCHD3 (0.83), BAG2 (0.83), PHB1 (0.82); STRING partners: PHB1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: huMAP3_10725.1, huMAP3_01706.1, huMAP3_09671.1, huMAP3_11743.1
- **Function (MyGene.info)**: prohibitin 2. Enables several functions, including protein C-terminus binding activity; protein N-terminus binding activity; and protein dimerization activity. Involved in several processes, including defense response to virus; positive regulation of cell cycle phase transition; and regulation of transcription, DNA-templated. Located in several cellular components, including cell surface; mitochondrial membrane…
- **Diseases (Open Targets)**: breast cancer (0.101); breast carcinoma (0.101); neoplasm (0.100); non-small cell lung carcinoma (0.096); colorectal carcinoma (0.085)
- **Europe PMC papers**: 2714
- **Why important**: PHB2 is the partner of PHB1 in the highest-confidence STRING relationship and recurs with PHB1 across multiple hu.MAP complexes (hu.MAP huMAP3_10725.1), (hu.MAP huMAP3_01706.1), (hu.MAP huMAP3_09671.1), and (hu.MAP huMAP3_11743.1). CHCHD3 also joins the PHB pair in (hu.MAP huMAP3_10725.1), linking PHB2 to inner mitochondrial membrane organization and cristae integrity. PHB2 is detected in both tissues, has annotations involving mitophagy, mitochondrial organization, transcriptional regulation, and cell-cycle control, and has a substantial literature and disease-annotation record.
- **Conclusion**: Established evidence supports PHB2 as a prohibitin-complex component with mitochondrial structural and quality-control functions. In this module it is a stronger molecular anchor than a standalone pathway marker; its shared abundance with PHB1 and CHCHD3 supports, but does not prove, coordinated mitochondrial remodeling.

#### NUP98

- **Related proteins** (co-abundance neighbors): CHKB (0.85), HSDL1 (0.85); STRING partners: NUP88 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05948.1, huMAP3_06369.1, huMAP3_10000.1, huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 98 and 96 precursor. Nuclear pore complexes (NPCs) regulate the transport of macromolecules between the nucleus and cytoplasm, and are composed of many polypeptide subunits, many of which belong to the nucleoporin family. This gene belongs to the nucleoporin gene family and encodes a 186 kDa precursor protein that undergoes autoproteolytic cleavage to generate a 98 kDa nucleoporin and 96 kDa nucleoporin. The 98 kDa nu…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); acute myeloid leukemia (0.399); lung carcinoma (0.376)
- **Europe PMC papers**: 4839
- **Why important**: NUP98 is a nucleoporin with a known STRING relationship to NUP88 and repeated hu.MAP co-membership with NUP88 in complexes (hu.MAP huMAP3_05948.1), (hu.MAP huMAP3_06369.1), (hu.MAP huMAP3_10000.1), and (hu.MAP huMAP3_12581.1). It is annotated in nuclear-pore organization, nucleocytoplasmic transport, RNA export, and nuclear-periphery functions. HPA identifies it as cell-type enriched in neutrophils, while its disease annotations include acute myeloid leukemia and viral infection. It also has one of the largest literature records in the module, making its core function particularly well established.
- **Conclusion**: Established evidence supports NUP98 as a nuclear transport and RNA-export component, with known disease relevance. Its presence may indicate high nuclear transport or transcriptional-processing demand in selected module-containing cells, but it does not demonstrate that nuclear pore function is the principal function of the entire module.

#### IARS2

- **Related proteins** (co-abundance neighbors): AMDHD2 (0.87); STRING partners: KARS1 (0.995)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 2, mitochondrial. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Two forms of isoleucine-tRNA synthetase exist, a cytoplasmic form and a mitochondrial form. This gene encodes th…
- **Diseases (Open Targets)**: cataract-growth hormone deficiency-sensory neuropathy-sensorineural hearing loss-skeletal dysplasia syndrome (0.724); Leigh syndrome (0.563); hereditary disease (0.416); neurodegenerative disease (0.411); mitochondrial disease (0.374)
- **Europe PMC papers**: 411
- **Why important**: IARS2 is a mitochondrial isoleucine-tRNA synthetase and is part of hu.MAP complex (hu.MAP huMAP3_13468.1). It has a very strong STRING relationship with KARS1, while TSFM connects the same local neighborhood to mitochondrial translation. IARS2 is detected in both tissues, and its HPA profile is broadly expressed at the tissue level. Its disease annotations include Leigh syndrome, mitochondrial disease, and a multisystem hereditary syndrome, with a substantial literature record. It therefore provides a concrete translation-related interpretation for one branch of the module.
- **Conclusion**: Established evidence supports IARS2 in mitochondrial tRNA charging and translational fidelity. Its co-abundance with TSFM and KARS1 is compatible with mitochondrial protein-synthesis demand, but the module does not show that altered mitochondrial translation is the cause of the cross-tissue association.

## Module 5

**Tissue pair**: bone_marrow and testis  
**Genes (18)**: ACACA, ADD3, CPT2, GBP1, GCLC, HPX, RNMT, MTA2, NDUFS1, NEK9, PAPSS2, PLXNB2, PFAS, UPF1, SACM1L, TTLL12, NAE1, XRN2

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established single pathway-level function. Its genes instead span several established cellular processes, including sulfation through PAPSS2, glutathione synthesis and oxidative-stress handling through GCLC, mitochondrial respiration through NDUFS1, fatty-acid oxidation through CPT2, lipid synthesis through ACACA, purine synthesis through PFAS, RNA processing and surveillance through XRN2 and UPF1, chromatin regulation through MTA2 and TTLL12, and cell-cycle regulation through NAE1 and NEK9. The co-abundance graph has a hub-and-spoke structure centered on PAPSS2, while most other genes are peripheral. This pattern is more consistent with a coordinated cellular state or shared sample composition than with a well-defined conserved molecular complex. The sole high-confidence STRING relationship, UPF1–XRN2, provides a biologically coherent RNA-processing link but does not establish a common function for the whole module.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: HPX is the clearly secreted blood protein, while GBP1 is intracellular and membrane-associated. Most members are intracellular enzymes, nuclear proteins, mitochondrial proteins, or membrane-associated proteins. HPA shows generally low tissue specificity for many genes, with several tissue-enhanced signals distributed across liver, muscle, adrenal gland, esophagus, and other tissues rather than concentrated in bone marrow or testis. Several genes have enhanced or enriched signals in hematopoietic populations, including monocyte, dendritic-cell, neutrophil, NK-cell, and erythrocyte-related populations, but overall immune-cell specificity is usually low. Protein detection is broader in testis than in bone marrow, and HPX is not detected in either target tissue despite its liver-enriched, hepatocyte-enriched, secreted profile. Therefore, contamination or shared blood-derived material is possible, particularly for HPX and the myeloid-associated genes, but the HPA evidence does not support a purely blood-cell module. Shared broadly expressed cellular programs and common cell types remain plausible explanations.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The co-abundance links should not be interpreted as physical interactions by default. STRING supports only the UPF1–XRN2 relationship among the module genes, consistent with their shared roles in RNA surveillance, RNA catabolism, and transcription-related RNA processing. PAPSS2, the network hub, has no reported STRING partners in the supplied evidence, so its centrality is specific to the co-abundance network rather than an established interaction network. No hu.MAP complex contains multiple module members. Thus, the known molecular evidence explains a small RNA-processing submodule but does not validate the hub-and-spoke architecture as a pre-existing protein complex.

**STRING interactions (score >= 0.7)**: 1 of 153 gene pairs: UPF1–XRN2 (0.812)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported tissue-pair co-abundance pattern, because the supplied databases do not identify a shared hu.MAP complex, STRING functional enrichment, or a broad set of known physical interactions. However, it cannot be called a novel biological mechanism on this evidence alone. Most constituent genes have well-established individual functions and disease associations, and the apparent novelty is primarily the cross-tissue co-abundance relationship and its unusual combination of genes. The weak database connectivity may reflect incomplete interaction coverage, expression-driven correlation, sample composition, or a context-dependent association. Independent replication, preservation testing, and perturbation or protein-level validation would be needed before claiming a new conserved module.

**Hypothesis.** Hypothesis: the module reflects a shared cellular stress and biosynthetic state present in subsets of bone-marrow and testis samples rather than a single physical pathway. In this model, PAPSS2-centered co-abundance tracks broad metabolic and regulatory demand, while GCLC supports redox buffering, NDUFS1 and CPT2 support mitochondrial energy and lipid metabolism, and XRN2 with UPF1 supports RNA quality control. HPX may mark a liver-derived or blood-associated component rather than a local bone-marrow or testis mechanism. The association could therefore arise from a mixture of common cellular programs and variable cell or extracellular-protein composition, with the UPF1–XRN2 link representing the most directly supported mechanistic connection.

### Important genes

#### PAPSS2

- **Related proteins** (co-abundance neighbors): ADD3 (0.91), NAE1 (0.90), NDUFS1 (0.90), RNMT (0.89), NEK9 (0.89), GCLC (0.87), MTA2 (0.86), XRN2 (0.86), CPT2 (0.85), PLXNB2 (0.85), TTLL12 (0.85), UPF1 (0.84), SACM1L (0.83), PFAS (0.83), ACACA (0.81), GBP1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3'-phosphoadenosine 5'-phosphosulfate synthase 2. Sulfation is a common modification of endogenous (lipids, proteins, and carbohydrates) and exogenous (xenobiotics and drugs) compounds. In mammals, the sulfate source is 3'-phosphoadenosine 5'-phosphosulfate (PAPS), created from ATP and inorganic sulfate. Two different tissue isoforms encoded by different genes synthesize PAPS. This gene encodes one of the two PAPS synthetases. Defects in this gen…
- **Diseases (Open Targets)**: spondyloepimetaphyseal dysplasia, PAPSS2 type (0.799); hereditary disease (0.471); Spondyloepiphyseal dysplasia and spondyloepimetaphyseal dysplasia (0.462); autosomal recessive brachyolmia (0.455); skeletal dysplasia (0.343)
- **Europe PMC papers**: 1005
- **Why important**: PAPSS2 is the dominant hub of the co-abundance graph and is connected to genes spanning metabolism, RNA regulation, mitochondrial function, cell-cycle control, and cytoskeletal biology. Its established function is production of PAPS for sulfation of endogenous and exogenous compounds. It has a strong skeletal-dysplasia disease association and substantial literature, making it the most informative candidate for testing whether the module has a real biochemical center or is instead an expression-state hub.
- **Conclusion**: Established evidence supports PAPSS2 as the network hub and as a sulfation-related metabolic enzyme with skeletal-dysplasia relevance. It is not established that PAPSS2 mechanistically drives the other module genes. A coordinating role is therefore a hypothesis, not a demonstrated conclusion.

#### GCLC

- **Related proteins** (co-abundance neighbors): PAPSS2 (0.87), HPX (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamate-cysteine ligase catalytic subunit. Glutamate-cysteine ligase, also known as gamma-glutamylcysteine synthetase is the first rate-limiting enzyme of glutathione synthesis. The enzyme consists of two subunits, a heavy catalytic subunit and a light regulatory subunit. This locus encodes the catalytic subunit, while the regulatory subunit is derived from a different gene located on chromosome 1p22-p21. Mutations at this locus have been …
- **Diseases (Open Targets)**: gamma-glutamylcysteine synthetase deficiency (0.766); cystic fibrosis (0.375); neurodegenerative disease (0.373); non-autoimmune hemolytic anemia (0.370); lung adenocarcinoma (0.331)
- **Europe PMC papers**: 8941
- **Why important**: GCLC is a peripheral connector between PAPSS2 and HPX and encodes the catalytic subunit of the rate-limiting enzyme for glutathione synthesis. Its bone-marrow and testis protein detection, liver-enhanced expression, NK-cell association, oxidative-stress annotations, hemolytic-anemia relevance, and extensive literature make it a strong candidate for interpreting the module as a redox or stress-associated state.
- **Conclusion**: Established evidence supports GCLC as a central enzyme in glutathione production and oxidative-stress protection. Its placement in this module is compatible with redox coordination, but the module data do not prove that redox regulation explains the complete gene set.

#### HPX

- **Related proteins** (co-abundance neighbors): GCLC (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hemopexin. This gene encodes a plasma glycoprotein that binds heme with high affinity. The encoded protein is an acute phase protein that transports heme from the plasma to the liver and may be involved in protecting cells from oxidative stress. [provided by RefSeq, Apr 2009].
- **Diseases (Open Targets)**: panniculitis (0.116); neoplasm (0.107); familial idiopathic steroid-resistant nephrotic syndrome (0.101); hepatocellular carcinoma (0.101); focal segmental glomerulosclerosis (0.097)
- **Europe PMC papers**: 6894
- **Why important**: HPX is the clearest composition-sensitive member. It is a liver-enriched, hepatocyte-enriched plasma glycoprotein that binds heme and is secreted to blood, and it connects to GCLC in the network. Its presence can therefore report extracellular heme handling, hepatic or blood-derived material, or sample-composition effects rather than a local intracellular program in bone marrow or testis. It also has a substantial literature concerning heme transport and oxidative protection.
- **Conclusion**: Established evidence supports HPX as a secreted heme-binding protein and as a plausible marker of blood or liver-derived material. It should not be treated as evidence that the entire module is a local HPX-centered pathway in either target tissue.

#### XRN2

- **Related proteins** (co-abundance neighbors): PAPSS2 (0.86); STRING partners: UPF1 (0.812)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 5'-3' exoribonuclease 2. This gene encodes a 5'-3' exonuclease that promotes transcription termination at cotranscriptional cleavage sites. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: attention deficit-hyperactivity disorder (0.339); neurodegenerative disease (0.326); atrial fibrillation (0.305); food allergy (0.271); adolescent idiopathic scoliosis (0.221)
- **Europe PMC papers**: 1676
- **Why important**: XRN2 is linked to the hub in the co-abundance graph and is the partner of UPF1 in the only high-confidence STRING interaction reported for the module. Its established functions include RNA degradation, transcription termination, RNA processing, and spermatogenesis, while HPA detects it in both target tissues and shows neutrophil-enhanced expression. Its literature base is substantial and its annotation provides the clearest coherent functional edge within the module.
- **Conclusion**: Established evidence supports XRN2 as an RNA-processing and transcription-termination factor and supports a known relationship with UPF1. A module-wide RNA-surveillance mechanism remains unproven because most other genes lack corresponding interaction or enrichment evidence.

#### UPF1

- **Related proteins** (co-abundance neighbors): PAPSS2 (0.84); STRING partners: XRN2 (0.812)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UPF1 RNA helicase and ATPase. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons.…
- **Diseases (Open Targets)**: Intellectual disability (0.437); Global developmental delay (0.426); High anterior hairline (0.425); Frontal bossing (0.425); Hypertelorism (0.425)
- **Europe PMC papers**: 4252
- **Why important**: UPF1 is a core factor in nonsense-mediated mRNA decay, mRNA export, and RNA surveillance. It is connected to XRN2 in STRING and is detected in both bone marrow and testis, although it is not detected in immune cells in the supplied HPA summary. Its broad disease literature and direct relationship with XRN2 make it a useful anchor for evaluating whether the RNA-processing signal is reproducible rather than incidental.
- **Conclusion**: Established evidence supports UPF1 as an RNA-surveillance and mRNA-quality-control factor and supports its known relationship with XRN2. The co-abundance module does not establish that UPF1 coordinates PAPSS2 or the broader metabolic branch.

## Module 6

**Tissue pair**: bone_marrow and testis  
**Genes (46)**: ACADVL, ACO1, ACO2, ANXA6, AP2B1, ATL3, HSPA5, CALD1, CALU, CAPN2, CNOT12, CORO1C, DBNL, DCTN1, DPYSL2, EHD2, FERMT2, G6PD, GALK1, GANAB, GARS1, GSN, GFPT1, GBE1, HSPA8, ITGB1, ITIH1, MAP1B, NIBAN2, NSF, FAM114A1, PDCD6IP, PDIA4, PLS3, PYGB, SEC23A, SEPTIN9, SPTBN1, SPTAN1, CTTN, LARS1, TKT, TLN1, TOP2A, VCL, RP2

### Function

The strongest and most coherent interpretation is a conserved cell cortex and membrane–cytoskeleton organization module. Primary evidence includes cell cortex (GO:CC cell cortex; q_global = 0.00016), cadherin binding (GO:MF cadherin binding; q_global = 0.00543), cortical cytoskeleton (GO:CC cortical cytoskeleton; q_global = 0.00571), calcium ion binding (GO:MF calcium ion binding; q_global = 0.00572), cell periphery (GO:CC cell periphery; q_global = 0.0073), actin cytoskeleton (GO:CC actin cytoskeleton; q_global = 0.00848), cell adhesion molecule binding (GO:MF cell adhesion molecule binding; q_global = 0.0093), actin binding (GO:MF actin binding; q_global = 0.011), anchoring junction (GO:CC anchoring junction; q_global = 0.0114), cortical actin cytoskeleton (GO:CC cortical actin cytoskeleton; q_global = 0.0116), actin cytoskeleton organization (GO:BP actin cytoskeleton organization; q_global = 0.019), focal adhesion assembly (GO:BP focal adhesion assembly; q_global = 0.0278), cell junction (GO:CC cell junction; q_global = 0.0285), focal adhesion (GO:CC focal adhesion; q_global = 0.0353), cell-substrate junction (GO:CC cell-substrate junction; q_global = 0.0353), and supramolecular fiber organization (GO:BP supramolecular fiber organization; q_global = 0.0473). Together these support a structural and signaling program that links cortical actin and spectrin scaffolds to integrin- and cadherin-associated adhesion sites, plasma-membrane organization, vesicle traffic, and mechanically responsive cell shape. Calcium-sensitive membrane and cytoskeletal regulation is also supported by (GO:MF calcium ion binding; q_global = 0.00572). The melanosome and pigment-granule terms (GO:CC melanosome; q_global = 0.00588) and (GO:CC pigment granule; q_global = 0.00588) should be interpreted cautiously as shared vesicle and membrane-trafficking biology, not as evidence that this module specifically performs pigment production. The supplementary STRING annotations independently reinforce cell cortex, cortical actin, actin binding, cytoskeletal binding, and cell-periphery functions (STRING Component Cell cortex; within-query FDR = 7.98e-05), (STRING Component Cortical actin cytoskeleton; within-query FDR = 9.49e-05), (STRING Function Actin binding; within-query FDR = 0.00032), (STRING Component Actin cytoskeleton; within-query FDR = 0.00033), (STRING Function Cytoskeletal protein binding; within-query FDR = 0.00044), (STRING COMPARTMENTS Cell cortex; within-query FDR = 0.00047), (STRING COMPARTMENTS Actin cytoskeleton; within-query FDR = 0.00047), (STRING COMPARTMENTS Cortical actin cytoskeleton; within-query FDR = 0.00047), and (STRING COMPARTMENTS Cell periphery; within-query FDR = 0.00047).

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. Most genes have low tissue specificity, and the HPA data show broad protein detection in both bone marrow and testis. Several genes have enhanced or enriched cell-type patterns rather than a single shared tissue identity. The most prominent cellular signals include platelets, megakaryocytes, monocytes, neutrophils, myeloid dendritic cells, epithelial populations, vascular cells, adipocytes, and testicular or germ-cell populations. This makes a shared structural program plausible across different cell types, but also raises the possibility that the bone-marrow signal partly reflects blood-derived cells or platelet-lineage material and that the testis signal partly reflects specialized epithelial or germ-cell populations. Several genes are secreted or associated with blood, but the module as a whole is mainly intracellular and membrane-associated rather than a plasma-protein signature. Broad housekeeping-like components, including chaperones, metabolic enzymes, translation machinery, and vesicle-trafficking proteins, may contribute to shared sample composition rather than tissue-specific biology.

**GO/KEGG enrichment**: 24 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC cell cortex | 0.00016 | CALD1, CAPN2, CORO1C, CTTN, DBNL, DCTN1, FERMT2, GSN, SEPTIN9, SPTAN1, SPTBN1, VCL |
| GO:MF cadherin binding | 0.00543 | CALD1, CNOT12, CTTN, DBNL, HSPA5, HSPA8, ITGB1, NIBAN2, SEPTIN9, SPTAN1, SPTBN1, TLN1, VCL |
| GO:CC cortical cytoskeleton | 0.00571 | CALD1, CAPN2, CTTN, GSN, SPTAN1, SPTBN1, VCL |
| GO:MF calcium ion binding | 0.00572 | ANXA6, CALU, CAPN2, EHD2, GSN, HSPA5, ITGB1, ITIH1, PLS3, SPTAN1, TKT |
| GO:CC melanosome | 0.00588 | ANXA6, CALU, GANAB, HSPA5, HSPA8, ITGB1, PDCD6IP, PDIA4 |
| GO:CC pigment granule | 0.00588 | ANXA6, CALU, GANAB, HSPA5, HSPA8, ITGB1, PDCD6IP, PDIA4 |
| GO:CC cell periphery | 0.0073 | ANXA6, AP2B1, CALD1, CAPN2, CORO1C, CTTN, DBNL, DCTN1, DPYSL2, EHD2, FERMT2, G6PD, GSN, HSPA5, HSPA8, ITGB1, MAP1B, NIBAN2, NSF, PDCD6IP, PLS3, RP2, SEPTIN9, SPTAN1, SPTBN1, TLN1, VCL |
| GO:CC actin cytoskeleton | 0.00848 | CALD1, CAPN2, CORO1C, CTTN, DBNL, FERMT2, GSN, PDCD6IP, PLS3, SEPTIN9, SPTAN1, SPTBN1, VCL |
| GO:MF cell adhesion molecule binding | 0.0093 | CALD1, CNOT12, CTTN, DBNL, FERMT2, HSPA5, HSPA8, ITGB1, NIBAN2, SEPTIN9, SPTAN1, SPTBN1, TLN1, VCL |
| GO:MF actin binding | 0.011 | CALD1, CORO1C, DBNL, FERMT2, GSN, ITGB1, MAP1B, PLS3, SPTAN1, SPTBN1, TLN1, VCL |
| GO:CC anchoring junction | 0.0114 | ANXA6, CAPN2, CNOT12, CORO1C, CTTN, DBNL, FERMT2, GSN, HSPA5, HSPA8, ITGB1, NIBAN2, PDCD6IP, TLN1, VCL |
| GO:CC cortical actin cytoskeleton | 0.0116 | CALD1, CAPN2, GSN, SPTAN1, SPTBN1, VCL |
| GO:BP regulation of cellular component biogenesis | 0.0134 | CORO1C, CTTN, DCTN1, FERMT2, GSN, HSPA5, HSPA8, MAP1B, PDCD6IP, SEPTIN9, SPTAN1, SPTBN1, TLN1, VCL |
| GO:BP actin cytoskeleton organization | 0.019 | CALD1, CORO1C, CTTN, DBNL, EHD2, FERMT2, GSN, ITGB1, PDCD6IP, PLS3, SPTAN1, SPTBN1, TLN1 |
| GO:MF actin filament binding | 0.0223 | CORO1C, DBNL, FERMT2, GSN, PLS3, SPTAN1, SPTBN1, TLN1, VCL |

### STRING and hu.MAP

STRING contains established relationships concentrated in several coherent groups. The adhesion and cortical-actin group includes ITGB1, TLN1, VCL, FERMT2, CTTN, GSN, CAPN2, and SPTAN1. The spectrin pair SPTAN1–SPTBN1 is strongly supported, as are the metabolic pairs GBE1–PYGB, ACO1–ACO2, G6PD–TKT, and GARS1–LARS1. The endoplasmic-reticulum and chaperone group includes HSPA5, HSPA8, PDIA4, GANAB, and CALU. These known relationships show that the module is not a random collection of co-abundant genes; it contains recognizable adhesion, cytoskeletal, trafficking, quality-control, and metabolic substructures. hu.MAP provides partial complex-level support rather than a single complete complex. It connects SPTAN1 with SPTBN1, CALD1 with CTTN, G6PD with GBE1, PYGB with GBE1, PDIA4 with GANAB, AP2B1 with SEC23A, DCTN1 with CNOT12, and PLS3 with GARS1 in complexes that include additional proteins outside the module. Thus, the module appears to combine several known complex fragments and functional neighborhoods rather than represent one previously defined molecular complex.

**STRING interactions (score >= 0.7)**: 27 of 1035 gene pairs: ACO1–ACO2 (0.943); AP2B1–EHD2 (0.907); CALD1–VCL (0.771); CALU–HSPA5 (0.864); CAPN2–SPTAN1 (0.762); CAPN2–TLN1 (0.971); CORO1C–PLS3 (0.818); CTTN–GSN (0.987); CTTN–TLN1 (0.937); CTTN–VCL (0.97); DPYSL2–MAP1B (0.756); FERMT2–ITGB1 (0.796); FERMT2–TLN1 (0.705); FERMT2–VCL (0.896); G6PD–TKT (0.91); GANAB–HSPA5 (0.846); GANAB–PDIA4 (0.717); GARS1–LARS1 (0.895); GBE1–PYGB (0.997); GSN–TLN1 (0.941); GSN–VCL (0.918); HSPA5–HSPA8 (0.983); HSPA5–PDIA4 (0.99); ITGB1–TLN1 (0.999); ITGB1–VCL (0.966); SPTAN1–SPTBN1 (0.999); TLN1–VCL (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Digestive gland (FDR = 2.02e-06, 39 genes); Component Cell cortex (FDR = 7.98e-05, 12 genes); Component Cortical actin cytoskeleton (FDR = 9.49e-05, 8 genes); Component Melanosome (FDR = 0.00021, 9 genes); Component Cell periphery (FDR = 0.00022, 28 genes); Function Actin binding (FDR = 0.00032, 14 genes); Function Actin filament binding (FDR = 0.00032, 11 genes); Component Actin cytoskeleton (FDR = 0.00033, 13 genes); TISSUES Liver (FDR = 0.00033, 33 genes); Function Cytoskeletal protein binding (FDR = 0.00044, 17 genes); COMPARTMENTS Cell cortex (FDR = 0.00047, 9 genes); COMPARTMENTS Actin cytoskeleton (FDR = 0.00047, 13 genes); COMPARTMENTS Cortical actin cytoskeleton (FDR = 0.00047, 7 genes); COMPARTMENTS Cell periphery (FDR = 0.00047, 22 genes); TISSUES Viscus (FDR = 0.00084, 41 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11694.1 (G6PD, GBE1; 2/3); huMAP3_07940.1 (SPTBN1, SPTAN1; 2/5); huMAP3_05473.1 (SPTBN1, SPTAN1; 2/7); huMAP3_06395.1 (CALD1, CTTN; 2/8); huMAP3_10673.1 (CALD1, CTTN; 2/14); huMAP3_10227.1 (PYGB, GBE1; 2/14); huMAP3_09760.1 (PYGB, GBE1; 2/15); huMAP3_13075.1 (PYGB, GBE1; 2/15); huMAP3_11993.1 (PYGB, GBE1; 2/20); huMAP3_12186.1 (PYGB, GBE1; 2/23); huMAP3_09165.1 (SPTBN1, SPTAN1; 2/39); huMAP3_12900.1 (DCTN1, CNOT12; 2/50); huMAP3_14442.1 (PLS3, GARS1; 2/57); huMAP3_06775.1 (PDIA4, GANAB; 2/60); huMAP3_09327.1 (PDIA4, GANAB; 2/93); huMAP3_12394.1 (AP2B1, SEC23A; 2/98)

### Novelty

The broad biological themes are established: cortical actin, integrin-associated adhesion, spectrin scaffolding, vesicle trafficking, endoplasmic-reticulum quality control, and intermediary metabolism are all well known. Therefore the module should not be described as a wholly new pathway or complex. Its potentially novel aspect is the conserved co-abundance coupling of these components across bone marrow and testis, including poorly characterized or weakly connected genes such as FAM114A1 and NIBAN2. The partial overlap with STRING and hu.MAP supports biological plausibility, while the absence of complete coverage in those resources indicates that the co-abundance organization may add context beyond known physical complexes. However, database absence alone cannot establish novelty. A defensible conclusion is that this is a potentially novel cross-tissue co-abundance configuration built around established adhesion and cytoskeletal biology, requiring replication in independent cohorts and cell-type-resolved data.

**Hypothesis.** Hypothesis: the module represents a shared membrane-remodeling and mechanical adaptation program that operates in distinct marrow and testicular cell populations. Integrin and junctional components may couple extracellular or cell-cell contacts to talin, vinculin, kindlin, spectrin, cortactin, gelsolin, and cortical actin. Calcium-sensitive proteins and calpain may remodel these attachments, while endocytic, COPII, dynactin, and ER quality-control components may recycle membrane proteins and maintain trafficking under mechanical or secretory demand. Metabolic enzymes may provide redox and biosynthetic support rather than define the central module function. In bone marrow this could support platelet, myeloid, or progenitor cell shape and adhesion; in testis it could support epithelial, Leydig, or germ-cell junctional and trafficking requirements. This remains a hypothesis because co-abundance does not establish physical interaction, directionality, or cell-type specific causation.

### Important genes

#### FERMT2

- **Related proteins** (co-abundance neighbors): GARS1 (0.94), GBE1 (0.93), SEC23A (0.90), PDCD6IP (0.89), VCL (0.88), DCTN1 (0.87), HSPA8 (0.87), FAM114A1 (0.87), NSF (0.86), GFPT1 (0.85), ANXA6 (0.85), HSPA5 (0.84), PDIA4 (0.84), PYGB (0.84), PLS3 (0.82), EHD2 (0.81), ACO1 (0.81), CAPN2 (0.81), TKT (0.80); STRING partners: ITGB1 (0.796), TLN1 (0.705), VCL (0.896)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Focal adhesion sites; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FERM domain containing kindlin 2. Enables several functions, including actin binding activity; phosphatidylinositol-3,4,5-trisphosphate binding activity; and type I transforming growth factor beta receptor binding activity. Involved in several processes, including cell surface receptor signaling pathway; positive regulation of cell differentiation; and positive regulation of cellular component biogenesis. Acts upstream of or withi…
- **Diseases (Open Targets)**: open-angle glaucoma (0.501); prostate carcinoma (0.488); glaucoma (0.488); neurodegenerative disease (0.473); primary angle-closure glaucoma (0.407)
- **Europe PMC papers**: 1336
- **Why important**: FERMT2 is one of the strongest network-connected genes and sits at the interface of many module neighborhoods. It has extensive primary support across the cell cortex, adhesion, actin, junction, focal-adhesion, and cell-substrate terms (GO:CC cell cortex; q_global = 0.00016), (GO:CC cell periphery; q_global = 0.0073), (GO:CC actin cytoskeleton; q_global = 0.00848), (GO:MF cell adhesion molecule binding; q_global = 0.0093), (GO:MF actin binding; q_global = 0.011), (GO:CC anchoring junction; q_global = 0.0114), (GO:BP actin cytoskeleton organization; q_global = 0.019), (GO:BP focal adhesion assembly; q_global = 0.0278), (GO:CC focal adhesion; q_global = 0.0353), (GO:CC cell-substrate junction; q_global = 0.0353), and (GO:BP supramolecular fiber organization; q_global = 0.0473). Its established functions include actin binding, integrin-mediated signaling, cell-matrix adhesion, focal-adhesion localization, and receptor signaling. STRING links it to ITGB1, TLN1, and VCL, giving direct support to the adhesion core. It also has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence identifies FERMT2 as a central adhesion and integrin–cytoskeleton linker. It is a strong candidate for organizing the structural core of this module. It is not established that FERMT2 drives the shared bone-marrow–testis co-abundance pattern; that causal role is hypothetical.

#### VCL

- **Related proteins** (co-abundance neighbors): FERMT2 (0.88), CALD1 (0.85), NIBAN2 (0.81); STRING partners: CALD1 (0.771), CTTN (0.97), FERMT2 (0.896), GSN (0.918), ITGB1 (0.966), TLN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vinculin. Vinculin is a cytoskeletal protein associated with cell-cell and cell-matrix junctions, where it is thought to function as one of several interacting proteins involved in anchoring F-actin to the membrane. Defects in VCL are the cause of cardiomyopathy dilated type 1W. Dilated cardiomyopathy is a disorder characterized by ventricular dilation and impaired systolic function, resulting in congestive…
- **Diseases (Open Targets)**: dilated cardiomyopathy 1W (0.692); hypertrophic cardiomyopathy 15 (0.660); hypertrophic cardiomyopathy (0.652); familial isolated dilated cardiomyopathy (0.642); cancer (0.605)
- **Europe PMC papers**: 10760
- **Why important**: VCL is a focal-adhesion protein with a central position in the recognized adhesion neighborhood. It participates in cell cortex, cadherin binding, cortical and general actin organization, anchoring junctions, focal adhesions, and cell-substrate junctions (GO:CC cell cortex; q_global = 0.00016), (GO:MF cadherin binding; q_global = 0.00543), (GO:CC cortical cytoskeleton; q_global = 0.00571), (GO:CC cell periphery; q_global = 0.0073), (GO:CC actin cytoskeleton; q_global = 0.00848), (GO:MF cell adhesion molecule binding; q_global = 0.0093), (GO:MF actin binding; q_global = 0.011), (GO:CC anchoring junction; q_global = 0.0114), (GO:CC cortical actin cytoskeleton; q_global = 0.0116), (GO:BP focal adhesion assembly; q_global = 0.0278), (GO:CC focal adhesion; q_global = 0.0353), (GO:CC cell-substrate junction; q_global = 0.0353), and (GO:BP supramolecular fiber organization; q_global = 0.0473). STRING supports relationships with FERMT2, ITGB1, TLN1, CTTN, GSN, CALD1, and the spectrin oriented cortical network. HPA detects it in both tissues and highlights platelets, which is relevant to the marrow context. It has extensive literature and established cardiomyopathy associations.
- **Conclusion**: Established evidence makes VCL a compelling marker of the module's membrane-to-actin adhesion architecture. Its platelet and broad tissue distribution also make cell composition an important alternative explanation for part of the signal. A specific cross-tissue regulatory role remains unproven.

#### SPTAN1

- **Related proteins** (co-abundance neighbors): TLN1 (0.92), SPTBN1 (0.91), NIBAN2 (0.86); STRING partners: CAPN2 (0.762), SPTBN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Microtubules; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: huMAP3_07940.1, huMAP3_05473.1, huMAP3_09165.1
- **Function (MyGene.info)**: spectrin alpha, non-erythrocytic 1. Spectrins are a family of filamentous cytoskeletal proteins that function as essential scaffold proteins that stabilize the plasma membrane and organize intracellular organelles. Spectrins are composed of alpha and beta dimers that associate to form tetramers linked in a head-to-head arrangement. This gene encodes an alpha spectrin that is specifically expressed in nonerythrocytic cells. The encod…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 5 (0.749); developmental delay with or without epilepsy (0.681); spastic paraplegia 91, autosomal dominant, with or without cerebellar ataxia (0.681); infantile spasms (0.651); genetic developmental and epileptic encephalopathy (0.651)
- **Europe PMC papers**: 1422
- **Why important**: SPTAN1 is part of the alpha-spectrin scaffold and is strongly linked in the module to SPTBN1, with additional STRING support involving CAPN2. It appears across the primary cortical, actin, adhesion, plasma-membrane, cytoskeleton, and supramolecular-fiber terms, including (GO:CC cell cortex; q_global = 0.00016), (GO:CC cortical cytoskeleton; q_global = 0.00571), (GO:CC actin cytoskeleton; q_global = 0.00848), (GO:CC cortical actin cytoskeleton; q_global = 0.0116), (GO:BP cytoskeleton organization; q_global = 0.0223), (GO:CC plasma membrane; q_global = 0.0238), (GO:CC cytoskeleton; q_global = 0.0304), (GO:MF protein-containing complex binding; q_global = 0.0384), and (GO:BP supramolecular fiber organization; q_global = 0.0473). hu.MAP independently places SPTAN1 and SPTBN1 in several complexes containing additional membrane and cytoskeletal proteins. Its established function as a membrane-stabilizing actin scaffold and its substantial neurological and developmental disease literature make it biologically informative.
- **Conclusion**: Established evidence supports SPTAN1 as a structural scaffold that can integrate cortical actin with membrane organization and intracellular transport. It is a plausible backbone of the module, but the data do not show that it assembles a unique bone-marrow–testis complex.

#### PDCD6IP

- **Related proteins** (co-abundance neighbors): FERMT2 (0.89), FAM114A1 (0.87), TOP2A (0.84), ITIH1 (0.82), NIBAN2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 6 interacting protein. This gene encodes a protein that functions within the ESCRT pathway in the abscission stage of cytokinesis, in intralumenal endosomal vesicle formation, and in enveloped virus budding. Studies using mouse cells have shown that overexpression of this protein can block apoptosis. In addition, the product of this gene binds to the product of the PDCD6 gene, a protein required for apoptosis, in a calc…
- **Diseases (Open Targets)**: HIV infectious disease (0.463); anthrax infection (0.462); alcohol drinking (0.388); autosomal recessive primary microcephaly (0.386); microcephaly 29, primary, autosomal recessive (0.383)
- **Europe PMC papers**: 1668
- **Why important**: PDCD6IP connects vesicles and membrane organization with cytoskeletal and cell-division biology. It contributes to the plasma-membrane, actin, junction, cytoskeleton, focal-adhesion, and supramolecular-fiber evidence through (GO:CC melanosome; q_global = 0.00588), (GO:CC cell periphery; q_global = 0.0073), (GO:CC actin cytoskeleton; q_global = 0.00848), (GO:CC anchoring junction; q_global = 0.0114), (GO:BP regulation of cellular component biogenesis; q_global = 0.0134), (GO:BP actin cytoskeleton organization; q_global = 0.019), (GO:BP cytoskeleton organization; q_global = 0.0223), (GO:CC plasma membrane; q_global = 0.0238), (GO:CC cell junction; q_global = 0.0285), (GO:CC cytoskeleton; q_global = 0.0304), (GO:CC focal adhesion; q_global = 0.0353), (GO:CC cell-substrate junction; q_global = 0.0353), and (GO:BP supramolecular fiber organization; q_global = 0.0473). Its established roles in ESCRT-dependent abscission, intralumenal vesicle formation, cytokinesis, and virus budding provide a mechanistic bridge between membrane remodeling and proliferative cell populations. HPA detects it in both tissues, and it has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports PDCD6IP as a membrane-vesicle and cytokinesis component that could connect the module's adhesion architecture to cell turnover and trafficking. Its proposed role as a cross-tissue coordinator is a hypothesis rather than a demonstrated mechanism.

#### HSPA5

- **Related proteins** (co-abundance neighbors): FAM114A1 (0.91), FERMT2 (0.84); STRING partners: CALU (0.864), GANAB (0.846), HSPA8 (0.983), PDIA4 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 represents the endoplasmic-reticulum protein-folding and quality-control arm of the module. It is included in primary cadherin-binding, calcium binding, membrane, junction, protein-complex, and cytoskeletal terms such as (GO:MF cadherin binding; q_global = 0.00543), (GO:MF calcium ion binding; q_global = 0.00572), (GO:CC melanosome; q_global = 0.00588), (GO:CC cell periphery; q_global = 0.0073), (GO:MF cell adhesion molecule binding; q_global = 0.0093), (GO:CC anchoring junction; q_global = 0.0114), (GO:CC plasma membrane; q_global = 0.0238), (GO:CC cell junction; q_global = 0.0285), (GO:CC focal adhesion; q_global = 0.0353), (GO:CC cell-substrate junction; q_global = 0.0353), and (GO:MF protein-containing complex binding; q_global = 0.0384). STRING supports its relationships with HSPA8, PDIA4, GANAB, and CALU. Its established role as an ER chaperone and regulator of ER homeostasis is relevant to cells with substantial membrane-protein or secretory demands, and it has extensive literature.
- **Conclusion**: Established evidence identifies HSPA5 as a quality-control and proteostasis component associated with the module's membrane and trafficking biology. Its presence may reflect shared cellular stress or biosynthetic demand rather than a specialized adhesion function, so its mechanistic connection to the cortical core should be tested directly.

#### FAM114A1

- **Related proteins** (co-abundance neighbors): HSPA8 (0.95), CTTN (0.92), HSPA5 (0.91), CALU (0.90), ANXA6 (0.90), SEC23A (0.90), DBNL (0.89), GARS1 (0.89), GBE1 (0.87), FERMT2 (0.87), DCTN1 (0.87), PDCD6IP (0.87), PYGB (0.86), GFPT1 (0.86), DPYSL2 (0.86), PDIA4 (0.85), ACO1 (0.84), PLS3 (0.84), GSN (0.84), NSF (0.84), G6PD (0.84), TKT (0.83), CORO1C (0.83), LARS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Golgi apparatus, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: family with sequence similarity 114 member A1. The protein encoded by this gene belongs to the FAM114 family and may play a role in neuronal cell development. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2017].
- **Diseases (Open Targets)**: response to stimulus (0.454); restless legs syndrome (0.382); movement disorder (0.338); neurodegenerative disease (0.335); ocular hypotension (0.193)
- **Europe PMC papers**: 200
- **Why important**: FAM114A1 has the strongest apparent co-abundance connectivity in the supplied module network and links many otherwise distinct neighborhoods, including HSPA8, CTTN, HSPA5, CALU, ANXA6, SEC23A, DBNL, and GARS1. Unlike the better annotated structural genes, it has no listed STRING partners, no hu.MAP membership, and no primary GO or KEGG term. HPA describes broad tissue specificity, a monocyte and myeloid-cell group pattern, Golgi and cytosolic localization, and detection in testis but not bone marrow. Its annotation suggests a possible role in neuronal cell development, while its disease associations and literature are comparatively limited.
- **Conclusion**: Established evidence supports FAM114A1 as a highly connected co-abundance member but does not establish its molecular function in this module. Its combination of network centrality and sparse external annotation makes it the most interesting candidate for a genuinely new module-specific relationship. Any role in coordinating adhesion, trafficking, or cell-type composition is currently a hypothesis.

## Module 7

**Tissue pair**: bone_marrow and testis  
**Genes (16)**: ACADSB, ALG2, NAGLU, ATG5, CLYBL, CRYL1, EXOC3, FAM114A2, IDE, LRRC20, MMS19, NFS1, PPM1A, PPAT, TBCE, UFSP2

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. The gene annotations nevertheless suggest a mixed cellular-maintenance module rather than a single established pathway. Its interpretable themes include protein quality control and stress handling through UFSP2 and ATG5, glycoprotein biosynthesis through ALG2, nucleotide production through PPAT, iron-sulfur biology through NFS1 and MMS19, tubulin folding through TBCE, vesicle targeting through EXOC3, and intermediary metabolism through CLYBL, ACADSB and CRYL1. The network therefore may reflect coordinated biosynthetic, organelle-maintenance and proteostasis demands in the two tissues, but the co-abundance pattern alone does not establish a unified biochemical pathway.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the HPA summary identifies only a minority of secreted genes, while most members are intracellular enzymes, regulators or structural and trafficking proteins. The module is also not broadly blood-cell enriched: nearly all genes have low immune-cell specificity, with only EXOC3 showing immune-cell enhancement in eosinophils. HPA tissue patterns are heterogeneous, including liver, kidney, skeletal muscle, tongue and bone marrow, while single-cell patterns include late primary spermatocytes, renal epithelial populations, hepatocytes and other specialized cell types. This heterogeneity argues against interpreting the module simply as a blood-contamination signature. Its presence in both tissues could instead reflect shared cellular programs, tissue composition, or coordinated expression in particular germline and marrow-associated populations. Protein detection is more frequent in testis than bone marrow, so transcript co-abundance should not be assumed to imply equal protein-level activity in both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship within the module is MMS19--PPAT, indicating prior evidence connecting cytosolic iron-sulfur assembly biology with a purine-biosynthetic enzyme. No other within-module STRING relationships met the stated confidence threshold, and there was no STRING functional-enrichment result. No hu.MAP complex contained at least two module members. Thus, most module edges are not supported as known physical interactions by these resources. The network is better viewed as a co-abundance structure that may combine genes from several cellular systems, with MMS19--PPAT providing one previously supported molecular link rather than validating the entire module as a physical complex.

**STRING interactions (score >= 0.7)**: 1 of 120 gene pairs: MMS19–PPAT (0.82)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module appears potentially novel as a cross-tissue co-abundance observation because most of its edges lack support in STRING, no multi-member hu.MAP complex was detected, and no globally corrected GO/KEGG or STRING enrichment defined it as a recognized pathway module. However, this does not prove biological novelty: absence from interaction databases can reflect incomplete coverage, context dependence, indirect regulation, or co-regulation without physical binding. Several individual genes and functions are well established, and the MMS19--PPAT relationship is already represented in STRING. The defensible conclusion is that the particular cross-tissue combination and its coordinated expression may be novel, whereas the component biology is not.

**Hypothesis.** Hypothesis: in bone marrow and testis, this module may coordinate the demands of proliferating or differentiating cells by coupling proteostasis and organelle quality control with biosynthetic capacity. UFSP2 and ATG5 could help manage protein and organelle stress; ALG2 could support glycoprotein maturation; NFS1 and MMS19 could maintain iron-sulfur-dependent activities; PPAT could supply purine precursors; and metabolic genes such as CLYBL, ACADSB and CRYL1 could adapt carbon and amino-acid metabolism. The co-abundance signal may therefore mark a shared state of biosynthetic and cellular-maintenance demand rather than a single physical complex. This hypothesis should be tested with cell-resolved expression, perturbation of central genes, protein-level measurements, and metabolic or stress-response readouts in relevant marrow and testis populations.

### Important genes

#### CLYBL

- **Related proteins** (co-abundance neighbors): ACADSB (0.92), FAM114A2 (0.84), CRYL1 (0.83), PPAT (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citramalyl-CoA lyase. Enables (S)-citramalyl-CoA lyase activity; magnesium ion binding activity; and malate synthase activity. Involved in protein homotrimerization and regulation of cobalamin metabolic process. Predicted to be located in mitochondrion. Predicted to be integral component of membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: vitamin B deficiency (0.374); neurodegenerative disease (0.309); Proteinuria (0.305); pernicious anemia (0.296); facial morphology (0.253)
- **Europe PMC papers**: 1132
- **Why important**: CLYBL is among the more connected module members and links ACADSB, FAM114A2, CRYL1 and PPAT in the co-abundance graph. Its annotated citramalyl-CoA lyase and malate-synthase-related activities, mitochondrial prediction, cobalamin-related biology and toxic-metabolite-repair annotation make it a plausible metabolic bridge between the module's central metabolic and biosynthetic signals. It is tissue-enhanced in liver, has several specialized cell-type associations, is detected in both bone marrow and testis, and has substantial literature and disease-association coverage.
- **Conclusion**: Established: CLYBL is a connected metabolic gene with annotated cobalamin-related and toxic-metabolite-repair functions and protein detection in both tissues. Hypothesis: its network position makes it a candidate integrator of metabolic state within this module, but the data do not establish that it controls the other members.

#### UFSP2

- **Related proteins** (co-abundance neighbors): PPM1A (0.93), ALG2 (0.86), NFS1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UFM1 specific peptidase 2. This gene encodes a highly conserved cysteine protease. The protein cleaves two C-terminal residues from ubiquitin-fold modifier 1, a ubiquitin-like post-translational modifier protein. Activation of ubiquitin-fold modifier 1 by the encoded protein exposes a C-terminal glycine residue that allows interaction with other proteins and transfer to its target protein. An allelic variant of this gene ha…
- **Diseases (Open Targets)**: spondyloepimetaphyseal dysplasia, di rocco type (0.708); hip dysplasia, Beukes type (0.640); developmental and epileptic encephalopathy 106 (0.611); Intellectual disability (0.546); Seizure (0.492)
- **Europe PMC papers**: 317
- **Why important**: UFSP2 occupies a relatively central position and connects PPM1A, ALG2 and NFS1. It is a conserved cysteine protease that activates the ubiquitin-fold modifier UFM1 and is annotated for ribosome disassembly and rescue of stalled cytosolic ribosomes. Its disease associations include skeletal and neurodevelopmental disorders, and it is detected in both tissues. These features make it a strong candidate for linking translational quality control with cellular stress management.
- **Conclusion**: Established: UFSP2 activates UFM1 and has documented roles in proteolysis-related and ribosome-quality-control biology. Hypothesis: its connection to ALG2, NFS1 and PPM1A may indicate a shared stress-adaptation program in marrow and germ-cell contexts, but this network interpretation remains unproven.

#### PPM1A

- **Related proteins** (co-abundance neighbors): UFSP2 (0.93), LRRC20 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase, Mg2+/Mn2+ dependent 1A. The protein encoded by this gene is a member of the PP2C family of Ser/Thr protein phosphatases. PP2C family members are known to be negative regulators of cell stress response pathways. This phosphatase dephosphorylates, and negatively regulates the activities of, MAP kinases and MAP kinase kinases. It has been shown to inhibit the activation of p38 and JNK kinase cascades induced by environmenta…
- **Diseases (Open Targets)**: neurodegenerative disease (0.446); Hypoxemia (0.241); asphyxia (0.241); hair color (0.225); nephrotic syndrome (0.196)
- **Europe PMC papers**: 1198
- **Why important**: PPM1A is a connector between UFSP2 and LRRC20 and is tissue-enhanced in bone marrow, with detection in both bone marrow and testis. It is a magnesium- or manganese-dependent serine/threonine phosphatase that negatively regulates stress-associated MAP kinase pathways and affects transforming-growth-factor-beta and NF-kappaB signaling. Its annotations and disease associations give it a plausible regulatory role despite its limited graph connectivity.
- **Conclusion**: Established: PPM1A is a stress- and signaling-related phosphatase with documented pathway-regulatory functions. Hypothesis: its position between UFSP2 and LRRC20 may reflect coordination of proteostasis with signaling state, but the co-abundance data cannot distinguish direct regulation from shared expression control.

#### ALG2

- **Related proteins** (co-abundance neighbors): UFSP2 (0.86), ATG5 (0.83), EXOC3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ALG2 alpha-1,3/1,6-mannosyltransferase. This gene encodes a member of the glycosyltransferase 1 family. The encoded protein acts as an alpha 1,3 mannosyltransferase, mannosylating Man(2)GlcNAc(2)-dolichol diphosphate and Man(1)GlcNAc(2)-dolichol diphosphate to form Man(3)GlcNAc(2)-dolichol diphosphate. Defects in this gene have been associated with congenital disorder of glycosylation type Ih (CDG-Ii). Alternative splicing results in mu…
- **Diseases (Open Targets)**: ALG2-congenital disorder of glycosylation (0.727); congenital myasthenic syndrome (0.692); neurodegenerative disease (0.450); congenital disorder of glycosylation (0.372); congenital disorder of glycosylation type I (0.370)
- **Europe PMC papers**: 871
- **Why important**: ALG2 connects UFSP2, ATG5 and EXOC3 and is detected in both tissues. It catalyzes a step in dolichol-linked oligosaccharide synthesis and is associated with congenital disorders of glycosylation and congenital myasthenic syndrome. Its position links protein modification with autophagy-related and vesicle-trafficking genes, making it informative for interpreting the module as a cellular-maintenance program.
- **Conclusion**: Established: ALG2 participates in early protein N-linked glycosylation and defects in the gene cause glycosylation-related disease. Hypothesis: its graph connections may reflect coordinated demand for glycoprotein maturation, autophagy and exocytic trafficking in cells shared between the tissues.

#### ATG5

- **Related proteins** (co-abundance neighbors): ALG2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Primary cilium transition zone, Centrosome, Basal body; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: autophagy related 5. The protein encoded by this gene, in combination with autophagy protein 12, functions as an E1-like activating enzyme in a ubiquitin-like conjugating system. The encoded protein is involved in several cellular processes, including autophagic vesicle formation, mitochondrial quality control after oxidative damage, negative regulation of the innate antiviral immune response, lymphocyte development a…
- **Diseases (Open Targets)**: neurodegenerative disease (0.557); rheumatoid arthritis (0.366); asthma (0.353); systemic lupus erythematosus (0.328); plasma cell myeloma (0.293)
- **Europe PMC papers**: 26318
- **Why important**: ATG5 connects to ALG2 and is one of the most extensively studied genes in the module. It is central to autophagosome formation and mitophagy, and its annotations also include mitochondrial quality control, lymphocyte biology, antigen presentation and apoptosis. Its testis detection and association with plasma cells provide relevant cellular context, while its large literature base makes its functional interpretation comparatively secure.
- **Conclusion**: Established: ATG5 is an autophagy and mitochondrial-quality-control factor with broad effects on cellular survival and immune biology. Hypothesis: its co-abundance with ALG2 may mark enhanced turnover and quality control rather than a direct physical partnership, especially because no supporting complex was found.

## Module 8

**Tissue pair**: bone_marrow and testis  
**Genes (12)**: ALDOC, GPS1, AGL, GEMIN4, GLT8D1, HDAC6, IMMT, NUP93, NUP210, RAB28, STARD10, TTC27

### Function

No single module function can be assigned with confidence. No GO or KEGG term passed global correction, and STRING reported no functional enrichment. The gene annotations suggest several intracellular processes, including intracellular trafficking, nucleocytoplasmic transport, spliceosomal assembly, glycolysis and glycogen metabolism, mitochondrial cristae organization, lipid handling, and protein deacetylation or quality control. The co-abundance structure is therefore more consistent with a mixed cellular-state or compartmental signal than with a coherent pathway. RAB28 is the principal network connector, while the remaining relationships are sparse and divided among trafficking, nuclear, metabolic, mitochondrial, and cytoskeletal or proteostasis functions.

**Cell composition.** The module contains no secreted genes, so it is not a plasma-protein module. Most genes have low tissue specificity and low immune-cell specificity, arguing against a uniformly blood-cell-specific program. However, HPA cell-type annotations include late spermatids, late primary spermatocytes, early spermatids, oocytes, and megakaryocyte progenitors. Several genes are detected in both tissues, whereas others show testis-only or bone-marrow-enhanced patterns. This mixture suggests that the shared signal could reflect common intracellular biology together with cell-composition effects, especially germ-cell representation in testis and progenitor representation in bone marrow. The HPA evidence does not support interpreting the module as a secreted factor program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship is NUP210–NUP93, supporting a known nuclear-pore connection. The hu.MAP evidence identifies TTC27 and NUP93 together in complex (hu.MAP huMAP3_09042.1), but they represent only a small part of a much larger annotated complex, so this does not establish that the full module is a single complex. No other module genes have reported STRING partners or hu.MAP complexes in the fact sheet. Thus, the co-abundance edges should not be treated as physical interactions: most are not independently supported by the interaction resources. The known NUP210–NUP93 relationship provides a plausible nuclear-transport anchor, while the rest of the network may reflect correlated expression, shared cell states, or indirect biology.

**STRING interactions (score >= 0.7)**: 1 of 66 gene pairs: NUP210–NUP93 (0.993)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09042.1 (TTC27, NUP93; 2/26)

### Novelty

The module may be a newly observed co-abundance pattern, but the available evidence is insufficient to call it a new biological pathway or complex. Its sparse interaction support, absence of globally significant GO or KEGG enrichment, and mixture of unrelated functional annotations weaken a strong novelty claim. Absence from STRING or hu.MAP cannot prove novelty because those resources emphasize experimentally supported or modeled physical relationships rather than every expression relationship. A defensible conclusion is that the tissue-pair co-abundance arrangement is potentially novel, whereas its biological mechanism remains unestablished.

**Hypothesis.** Hypothesis: the module is a composite intracellular state shared by selected marrow progenitors and testicular germ cells. RAB28-associated trafficking may coordinate with nuclear-pore components to influence compartmental transport, while GEMIN4 supports RNA-processing capacity and HDAC6 supports protein quality control and intracellular transport. The metabolic and mitochondrial members may reflect the energetic and structural demands of differentiation. This model predicts that the module will track particular progenitor or germ-cell states rather than represent a constitutive pathway across all cells, and it requires validation with cell-resolved expression, perturbation, and protein-interaction experiments.

### Important genes

#### RAB28

- **Related proteins** (co-abundance neighbors): NUP210 (0.86), ALDOC (0.85), NUP93 (0.84), GEMIN4 (0.80), IMMT (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB28, member RAS oncogene family. This gene encodes a member of the Rab subfamily of Ras-related small GTPases. The encoded protein may be involved in regulating intracellular trafficking. Alternative splicing results in multiple transcript variants. Pseudogenes of this gene are found on chromosomes 9 and X. [provided by RefSeq, Apr 2009].
- **Diseases (Open Targets)**: cone-rod dystrophy (0.712); retinitis pigmentosa (0.481); inherited retinal dystrophy (0.458); osteoarthritis, hip (0.435); Abnormality of the skeletal system (0.418)
- **Europe PMC papers**: 471
- **Why important**: RAB28 has the strongest network position and connects NUP210, NUP93, ALDOC, GEMIN4, and IMMT. It is a Ras-related small GTPase implicated in intracellular trafficking, visual perception, and photoreceptor maintenance. Its disease associations include cone-rod dystrophy, retinitis pigmentosa, inherited retinal dystrophy, and skeletal-system abnormalities, and it has a substantial literature base.
- **Conclusion**: Established evidence supports RAB28 as the main co-abundance connector and as a trafficking-related protein with retinal disease relevance. Hypothesis: RAB28 may coordinate the otherwise heterogeneous nuclear, mitochondrial, and metabolic signals in this module, but the network does not establish direct regulation.

#### NUP93

- **Related proteins** (co-abundance neighbors): RAB28 (0.84); STRING partners: NUP210 (0.993)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: huMAP3_09042.1
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 is linked to RAB28 in the module and has an independently supported STRING relationship with NUP210. It is a nuclear-pore component involved in nucleocytoplasmic transport, nuclear-envelope organization, nuclear-pore assembly, and polyadenylated messenger-RNA export. It also occurs with TTC27 in hu.MAP complex (hu.MAP huMAP3_09042.1) and has disease associations including nephrotic syndrome and viral infectious disease, with a substantial literature base.
- **Conclusion**: Established evidence makes NUP93 the strongest nuclear-transport anchor and supports the NUP210–NUP93 relationship as known biology. Hypothesis: altered nuclear transport could be part of the shared cellular state, but no enrichment result or co-abundance evidence demonstrates that this is the dominant module function.

#### NUP210

- **Related proteins** (co-abundance neighbors): RAB28 (0.86); STRING partners: NUP93 (0.993)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 210. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. The protein encoded by this gene is a membrane-spanning glycoprotein that is a major component of the nuclear pore complex. M…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.536); COVID-19 (0.407); Histiocytosis (0.370)
- **Europe PMC papers**: 642
- **Why important**: NUP210 is tissue-enhanced in bone marrow and cell-type enhanced in B-cells and several marrow progenitor populations, while also being detected in testis. It is a membrane-spanning nuclear-pore glycoprotein involved in nucleocytoplasmic transport and has a very strong STRING relationship with NUP93. Its disease associations include viral infectious disease and histiocytosis, and it has a substantial literature base.
- **Conclusion**: Established evidence supports NUP210 as a biologically credible link between the marrow-associated component and the nuclear-pore signal. Hypothesis: NUP210 may mark a progenitor or differentiation-related nuclear-envelope state shared with selected testicular cells, but the fact sheet does not show that it drives the module.

#### HDAC6

- **Related proteins** (co-abundance neighbors): STARD10 (0.89), GLT8D1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Centrosome, Basal body, Cytosol; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: histone deacetylase 6. Histones play a critical role in transcriptional regulation, cell cycle progression, and developmental events. Histone acetylation/deacetylation alters chromosome structure and affects transcription factor access to DNA. The protein encoded by this gene belongs to class II of the histone deacetylase/acuc/apha family. It contains an internal duplication of two catalytic domains which appear to func…
- **Diseases (Open Targets)**: X-linked dominant chondrodysplasia, Chassaing-Lacombe type (0.592); plasma cell myeloma (0.574); primary cutaneous T-cell non-Hodgkin lymphoma (0.574); neoplasm (0.573); Duchenne muscular dystrophy (0.521)
- **Europe PMC papers**: 12885
- **Why important**: HDAC6 connects STARD10 and GLT8D1 and is annotated to protein deacetylation, protein quality control, intracellular transport, stress responses, and microtubule regulation. It is detected in both tissues and localized to centrosomal, basal-body, and cytosolic compartments. Its associations include X-linked dominant chondrodysplasia, plasma-cell myeloma, cutaneous T-cell lymphoma, neoplasm, and Duchenne muscular dystrophy, and it has the largest literature volume among the selected genes.
- **Conclusion**: Established evidence supports HDAC6 as a multifunctional regulator of proteostasis, transport, and cytoskeletal behavior. Hypothesis: HDAC6 could help couple differentiation-associated trafficking and protein-quality-control demands across marrow and testis, but this remains a mechanistic possibility rather than an inferred causal role.

#### GEMIN4

- **Related proteins** (co-abundance neighbors): STARD10 (0.89), RAB28 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gem nuclear organelle associated protein 4. The product of this gene is part of a large complex localized to the cytoplasm, nucleoli, and to discrete nuclear bodies called Gemini bodies (gems). The complex functions in spliceosomal snRNP assembly in the cytoplasm, and regenerates spliceosomes required for pre-mRNA splicing in the nucleus. The encoded protein directly interacts with a DEAD box protein and several spliceosome core proteins. A…
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, cataracts, and renal abnormalities (0.738); neurodegenerative disease (0.527); microcephaly (0.262); Global developmental delay (0.259); Developmental cataract (0.259)
- **Europe PMC papers**: 647
- **Why important**: GEMIN4 connects RAB28 and STARD10 and is annotated as a component of the gem nuclear organelle machinery involved in spliceosomal small nuclear ribonucleoprotein assembly and ribosomal-RNA processing. It is enriched across several spermatogenic cell states and is detected in both tissues. Its disease associations include a neurodevelopmental disorder with microcephaly, cataracts, and renal abnormalities, as well as neurodegenerative disease, and it has a meaningful literature base.
- **Conclusion**: Established evidence supports GEMIN4 as an RNA-processing component whose cell-type pattern is particularly compatible with germ-cell differentiation. Hypothesis: GEMIN4 may indicate increased RNA-processing demand in the shared module, potentially linking differentiation with the trafficking and nuclear-transport signals.

#### AGL

- **Related proteins** (co-abundance neighbors): GLT8D1 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: amylo-alpha-1,6-glucosidase and 4-alpha-glucanotransferase. This gene encodes the glycogen debrancher enzyme which is involved in glycogen degradation. This enzyme has two independent catalytic activities which occur at different sites on the protein: a 4-alpha-glucotransferase activity and a amylo-1,6-glucosidase activity. Mutations in this gene are associated with glycogen storage disease although a wide range of enzymatic and clinical variability occurs…
- **Diseases (Open Targets)**: glycogen storage disease III (0.831); disorder of glycogen metabolism (0.768); glycogen storage disease XV (0.608); hereditary disease (0.507); Acute rhabdomyolysis (0.463)
- **Europe PMC papers**: 4441
- **Why important**: AGL is connected to GLT8D1 and encodes the glycogen-debranching enzyme with glucan-transferase and glucosidase activities. It is group-enriched in skeletal muscle and tongue, detected in testis but not bone marrow, and is strongly associated with glycogen storage disease and disorders of glycogen metabolism. Its established enzymatic function and substantial literature base make it an informative metabolic member despite its peripheral network position.
- **Conclusion**: Established evidence supports AGL as a glycogen-metabolism marker rather than as a central interaction hub. Hypothesis: its presence may reflect energetic remodeling in differentiating testicular cells or a broader cellular-state effect, but it does not by itself support a shared glycogen pathway in both tissues.

## Module 9

**Tissue pair**: bone_marrow and testis  
**Genes (37)**: RNPEP, PRMT5, AP3B1, CAPRIN1, DDX42, DDX5, EIF3L, ENAH, FABP5, HSP90AA1, HYOU1, IMPDH2, LMNB1, LMNB2, RHOT1, PGM1, PRPF31, ATIC, RECQL, SDHA, SNTB2, SRP68, AARS1, FARSB, IARS1, NARS1, QARS1, RARS1, SARS1, WARS1, YARS1, CCT5, CCT3, CCT7, CCT8, UBA6, VASP

### Function

The strongest and most coherent interpretation is a conserved, intracellular gene-expression and proteostasis module centered on translation capacity. Primary evidence is the globally corrected enrichment for aminoacyl-tRNA ligase activity, tRNA aminoacylation, amino acid activation, and aminoacyl-tRNA biosynthesis (6 globally significant GO/KEGG terms, q_global 3.09e-05–3.09e-05; see the table), supported by the same process in STRING (STRING RCTM Cytosolic tRNA aminoacylation; within-query FDR = 8.8e-06) (STRING KEGG Aminoacyl-tRNA biosynthesis; within-query FDR = 1.19e-05) (STRING Keyword Aminoacyl-tRNA synthetase; within-query FDR = 1.68e-05) and (STRING Function aminoacyl-tRNA ligase activity; within-query FDR = 4.63e-05). The module contains a coordinated set of cytoplasmic aminoacyl-tRNA synthetases, including AARS1, FARSB, IARS1, NARS1, QARS1, RARS1, SARS1, WARS1, and YARS1. Additional globally corrected evidence supports translation and protein biosynthesis (GO:BP translation; q_global = 0.0349) (GO:BP protein biosynthetic process; q_global = 0.0349), RNA and nucleic-acid handling (GO:MF catalytic activity, acting on RNA; q_global = 0.00104), (GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.00136) (GO:MF nucleic acid binding; q_global = 0.00144), (GO:BP nucleic acid metabolic process; q_global = 0.00521), and (GO:MF RNA binding; q_global = 0.0215), ATP and nucleotide binding (GO:MF ATP binding; q_global = 0.000126) (GO:MF adenyl ribonucleotide binding; q_global = 0.000134), (GO:MF nucleotide binding; q_global = 0.000394), (GO:MF nucleoside phosphate binding; q_global = 0.000494), (GO:MF adenyl nucleotide binding; q_global = 0.000922) (GO:MF purine ribonucleoside triphosphate binding; q_global = 0.000964), (GO:MF purine ribonucleotide binding; q_global = 0.00101), (GO:MF ribonucleotide binding; q_global = 0.00115) (GO:MF heterocyclic compound binding; q_global = 0.00128), (GO:MF carbohydrate derivative binding; q_global = 0.00461) (GO:MF purine nucleotide binding; q_global = 0.005), and protein-folding chaperone activity (GO:MF ATP-dependent protein folding chaperone; q_global = 0.000654), (GO:MF protein folding chaperone; q_global = 0.0091), and (GO:MF unfolded protein binding; q_global = 0.038). A second coherent component is the CCT chaperonin machinery: CCT3, CCT5, CCT7, and CCT8 form the chaperonin-containing T-complex (GO:CC chaperonin-containing T-complex; q_global = 0.000967) and are linked to ATP-dependent protein folding (GO:MF ATP-dependent protein folding chaperone; q_global = 0.000654), (GO:MF protein folding chaperone; q_global = 0.0091), and (GO:MF unfolded protein binding; q_global = 0.038). The CCT-containing subset is also associated with telomere maintenance, telomerase RNA localization to Cajal bodies, and DNA biosynthetic processes (GO:BP regulation of telomere maintenance via telomerase; q_global = 4.48e-05) (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 4.48e-05), (GO:BP regulation of telomere maintenance via telomere lengthening; q_global = 0.000183) (GO:BP positive regulation of telomere maintenance via telomere lengthening; q_global = 0.000183) (GO:BP positive regulation of DNA biosynthetic process; q_global = 0.000183), (GO:BP regulation of DNA biosynthetic process; q_global = 0.000485), (10 globally significant GO/KEGG terms, q_global 0.000967–0.00102; see the table), (5 globally significant GO/KEGG terms, q_global 0.00191–0.00344; see the table), (GO:BP positive regulation of telomere maintenance; q_global = 0.00526), (GO:BP regulation of telomere maintenance; q_global = 0.00802), and (GO:BP DNA biosynthetic process; q_global = 0.0162) (GO:BP positive regulation of chromosome organization; q_global = 0.0162). These annotations support a role in maintaining translation, RNA processing, protein folding, and proliferative or genome-maintenance capacity, but they do not by themselves establish that the complete module directly regulates telomerase.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a small secreted-protein component, and most genes are intracellular with cytosolic, nucleoplasmic, mitochondrial, nuclear-envelope, or vesicular localizations. It is also not primarily blood-cell enriched. HPA reports low immune-cell specificity for nearly all genes, with only WARS1 showing immune-cell enhancement in monocyte populations and ENAH reported as not detected in immune cells. The overall composition is therefore consistent with broadly expressed housekeeping and cell-maintenance machinery rather than a blood-cell-specific signature. This interpretation is supported by the prevalence of low tissue specificity and the widespread protein detection in both tissues. At the same time, the single-cell data show enrichment of several genes in spermatids, spermatocytes, oocytes, and progenitor or specialized cell populations, while LMNB1 is tissue enhanced in bone marrow and lymphoid tissue and SDHA is tissue enhanced in muscle. Thus, the shared signal could reflect conserved requirements of proliferating or differentiating cells in both tissues, with possible contributions from germ-cell and hematopoietic-cell composition, rather than a secreted systemic program.

**GO/KEGG enrichment**: 64 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF aminoacyl-tRNA ligase activity | 3.09e-05 | AARS1, FARSB, IARS1, NARS1, QARS1, RARS1, SARS1, WARS1, YARS1 |
| GO:BP tRNA aminoacylation for protein translation | 3.09e-05 | AARS1, FARSB, IARS1, NARS1, QARS1, RARS1, SARS1, WARS1, YARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 3.09e-05 | AARS1, FARSB, IARS1, NARS1, QARS1, RARS1, SARS1, WARS1, YARS1 |
| GO:BP amino acid activation | 3.09e-05 | AARS1, FARSB, IARS1, NARS1, QARS1, RARS1, SARS1, WARS1, YARS1 |
| GO:BP tRNA aminoacylation | 3.09e-05 | AARS1, FARSB, IARS1, NARS1, QARS1, RARS1, SARS1, WARS1, YARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 3.09e-05 | AARS1, FARSB, IARS1, NARS1, QARS1, RARS1, SARS1, WARS1, YARS1 |
| GO:BP regulation of telomere maintenance via telomerase | 4.48e-05 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP positive regulation of telomere maintenance via telomerase | 4.48e-05 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:MF ATP binding | 0.000126 | AARS1, CAPRIN1, CCT3, CCT5, CCT7, CCT8, DDX42, DDX5, FARSB, HSP90AA1, HYOU1, IARS1, NARS1, QARS1, RARS1, RECQL, SARS1, UBA6, WARS1, YARS1 |
| GO:MF adenyl ribonucleotide binding | 0.000134 | AARS1, CAPRIN1, CCT3, CCT5, CCT7, CCT8, DDX42, DDX5, FARSB, HSP90AA1, HYOU1, IARS1, NARS1, QARS1, RARS1, RECQL, SARS1, UBA6, WARS1, YARS1 |
| GO:MF catalytic activity, acting on a tRNA | 0.000176 | AARS1, FARSB, IARS1, NARS1, QARS1, RARS1, SARS1, WARS1, YARS1 |
| GO:BP regulation of telomere maintenance via telomere lengthening | 0.000183 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP positive regulation of telomere maintenance via telomere lengthening | 0.000183 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP positive regulation of DNA biosynthetic process | 0.000183 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:MF nucleotide binding | 0.000394 | AARS1, CAPRIN1, CCT3, CCT5, CCT7, CCT8, DDX42, DDX5, FARSB, HSP90AA1, HYOU1, IARS1, IMPDH2, NARS1, PRMT5, QARS1, RARS1, RECQL, RHOT1, SARS1, SDHA, UBA6, WARS1, YARS1 |

### STRING and hu.MAP

STRING provides strong, biologically coherent known relationships rather than isolated associations. The aminoacyl-tRNA synthetases form a dense interaction group, especially around IARS1, QARS1, RARS1, YARS1, AARS1, NARS1, SARS1, and WARS1, and STRING enrichment independently recovers cytosolic tRNA aminoacylation and aminoacyl-tRNA biosynthesis (STRING RCTM Cytosolic tRNA aminoacylation; within-query FDR = 8.8e-06) (STRING KEGG Aminoacyl-tRNA biosynthesis; within-query FDR = 1.19e-05) (STRING Keyword Aminoacyl-tRNA synthetase; within-query FDR = 1.68e-05), (STRING Function aminoacyl-tRNA ligase activity; within-query FDR = 4.63e-05), and (STRING Process tRNA aminoacylation for protein translation; within-query FDR = 0.00022). The CCT genes form another tightly connected group: CCT3, CCT5, CCT7, and CCT8 have very strong pairwise STRING relationships and connect to HSP90AA1, with additional links to IMPDH2 and ATIC. The module also contains known pairs or complexes involving LMNB1-LMNB2, ENAH-VASP, and ATIC-IMPDH2. hu.MAP independently supports the CCT chaperonin complex through multiple complexes containing CCT3, CCT5, CCT7, and CCT8 (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14442.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1) and (hu.MAP huMAP3_09020.1), as well as aminoacyl-tRNA synthetase assemblies involving AARS1, NARS1, YARS1, IARS1, QARS1, and RARS1 (hu.MAP huMAP3_10115.1), (hu.MAP huMAP3_10302.1) (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1) (hu.MAP huMAP3_14982.1), and (hu.MAP huMAP3_04783.1). Additional hu.MAP evidence connects PRMT5, DDX42, and PRPF31 in spliceosomal machinery (hu.MAP huMAP3_08980.1) and supports LMNB1-LMNB2 and ENAH-VASP assemblies (hu.MAP huMAP3_03501.1) (hu.MAP huMAP3_08692.1) (hu.MAP huMAP3_00325.1) (hu.MAP huMAP3_01216.1) (hu.MAP huMAP3_06340.1) (hu.MAP huMAP3_09020.1) (hu.MAP huMAP3_13519.1). Together, these results indicate that the network captures several established molecular systems: translation capacity, chaperonin-mediated folding, RNA processing, nuclear-envelope organization, and selected cytoskeletal or metabolic interactions. The co-abundance module therefore combines biologically connected subsystems rather than representing one purified physical complex.

**STRING interactions (score >= 0.7)**: 49 of 666 gene pairs: AARS1–FARSB (0.814); AARS1–HYOU1 (0.709); AARS1–IARS1 (0.98); AARS1–NARS1 (0.947); AARS1–QARS1 (0.964); AARS1–RARS1 (0.85); AARS1–SARS1 (0.881); AARS1–WARS1 (0.906); AARS1–YARS1 (0.996); ATIC–CCT7 (0.881); ATIC–IMPDH2 (0.991); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT3–HSP90AA1 (0.767); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT5–HSP90AA1 (0.868); CCT7–CCT8 (0.999); CCT7–HSP90AA1 (0.849); CCT7–IMPDH2 (0.758); CCT8–HSP90AA1 (0.823); ENAH–VASP (0.999); FARSB–IARS1 (0.914); FARSB–RARS1 (0.706); FARSB–YARS1 (0.946); HSP90AA1–HYOU1 (0.842); IARS1–NARS1 (0.965); IARS1–QARS1 (0.999); IARS1–RARS1 (0.999); IARS1–SARS1 (0.908); IARS1–WARS1 (0.85); IARS1–YARS1 (0.966); LMNB1–LMNB2 (0.999); NARS1–QARS1 (0.887); NARS1–RARS1 (0.909); NARS1–SARS1 (0.843); NARS1–WARS1 (0.84); NARS1–YARS1 (0.966); QARS1–RARS1 (0.999); QARS1–SARS1 (0.852); QARS1–WARS1 (0.888); QARS1–YARS1 (0.959); RARS1–SARS1 (0.933); RARS1–WARS1 (0.796); RARS1–YARS1 (0.942); SARS1–WARS1 (0.899); SARS1–YARS1 (0.941); WARS1–YARS1 (0.997)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Cytosolic tRNA aminoacylation (FDR = 8.8e-06, 9 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 1.19e-05, 9 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 1.68e-05, 9 genes); Keyword ATP-binding (FDR = 2.39e-05, 19 genes); Function aminoacyl-tRNA ligase activity (FDR = 4.63e-05, 9 genes); Keyword Protein biosynthesis (FDR = 4.91e-05, 10 genes); Function ATP binding (FDR = 7.87e-05, 19 genes); Function Catalytic activity, acting on RNA (FDR = 9.23e-05, 11 genes); Function Catalytic activity, acting on a nucleic acid (FDR = 9.23e-05, 12 genes); RCTM Translation (FDR = 0.00011, 11 genes); Function Nucleic acid binding (FDR = 0.00016, 21 genes); Function Nucleotide binding (FDR = 0.0002, 23 genes); Keyword Ligase (FDR = 0.00021, 10 genes); Keyword Nucleotide-binding (FDR = 0.00021, 20 genes); Process tRNA aminoacylation for protein translation (FDR = 0.00022, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10115.1 (NARS1, RECQL, AARS1, YARS1; 4/14); huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14442.1 (UBA6, ATIC, AARS1, YARS1; 4/57); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_10302.1 (NARS1, AARS1, YARS1; 3/9); huMAP3_02637.1 (IARS1, QARS1, RARS1; 3/14); huMAP3_13688.1 (IARS1, QARS1, RARS1; 3/14); huMAP3_14982.1 (NARS1, RECQL, FARSB; 3/28); huMAP3_08980.1 (PRMT5, DDX42, PRPF31; 3/97); huMAP3_03501.1 (LMNB1, LMNB2; 2/2); huMAP3_08692.1 (VASP, ENAH; 2/3); huMAP3_00325.1 (LMNB1, LMNB2; 2/3); huMAP3_01216.1 (VASP, ENAH; 2/4); huMAP3_06340.1 (VASP, ENAH; 2/4); huMAP3_09020.1 (VASP, ENAH; 2/4); huMAP3_13519.1 (LMNB1, LMNB2; 2/4); huMAP3_04783.1 (AARS1, YARS1; 2/4); huMAP3_08368.1 (VASP, ENAH; 2/5); huMAP3_10433.1 (LMNB1, LMNB2; 2/5); huMAP3_00207.1 (VASP, ENAH; 2/6); huMAP3_07276.1 (VASP, ENAH; 2/6); huMAP3_10838.1 (VASP, ENAH; 2/7); huMAP3_05711.1 (DDX5, CAPRIN1; 2/8); huMAP3_07909.1 (DDX5, CAPRIN1; 2/8); huMAP3_09259.1 (LMNB1, LMNB2; 2/8); huMAP3_09754.1 (DDX5, CAPRIN1; 2/9); huMAP3_10492.1 (LMNB1, LMNB2; 2/9); huMAP3_10614.1 (LMNB1, LMNB2; 2/9); huMAP3_10893.1 (VASP, ENAH; 2/10); huMAP3_10088.1 (NARS1, RECQL; 2/10); huMAP3_10631.1 (DDX5, CAPRIN1; 2/28); huMAP3_11111.1 (DDX5, CAPRIN1; 2/29); huMAP3_06511.1 (PRMT5, PRPF31; 2/79)

### Novelty

This module should not be described as a newly discovered molecular pathway. Its principal components and relationships are already well established in STRING and hu.MAP, particularly the aminoacyl-tRNA synthetase group, the CCT chaperonin complex, the lamin pair, and the ENAH-VASP pair. The globally corrected enrichment confirms that these familiar systems recur together in the bone-marrow and testis co-abundance data, but enrichment and co-abundance do not prove a new physical complex or a tissue-specific mechanism. The potentially novel aspect is the cross-tissue co-abundance organization of these established systems in this particular tissue pair, including the observed coupling of translation machinery, chaperoning, RNA processing, mitochondrial transport, and genome-maintenance genes. That claim remains a hypothesis because absence or limited representation in STRING or hu.MAP cannot establish novelty. Demonstrating novelty would require comparison with existing tissue co-expression studies, independent cohorts, cell-composition controls, and experimental validation of the proposed cross-system coupling.

**Hypothesis.** Hypothesis: this shared module reflects a conserved high-protein-production and proteostasis state in cells present in both bone marrow and testis. Coordinated aminoacyl-tRNA synthetases may support accurate charging of tRNAs and sustained translation, while the CCT chaperonin and HSP90AA1 help fold newly synthesized proteins. RNA helicases and spliceosomal factors such as DDX5, DDX42, PRPF31, and PRMT5 may coordinate RNA processing with this translational demand. RECQL, LMNB1, and LMNB2 could couple the state to genome integrity and nuclear organization, while RHOT1 and SDHA could connect it to mitochondrial transport and energy metabolism. The telomere and Cajal-body annotations suggest a possible link to proliferative or germ-cell genome maintenance, but this is a mechanistic hypothesis rather than an established property of the whole module. A testable prediction is that module activity will track cells undergoing sustained protein synthesis, differentiation, or proliferation in both tissues and will decrease when cell-composition effects and general expression abundance are controlled.

### Important genes

#### IARS1

- **Related proteins** (co-abundance neighbors): RHOT1 (0.88), YARS1 (0.87), RECQL (0.86), HYOU1 (0.86), CCT7 (0.85), FARSB (0.84), QARS1 (0.84), SRP68 (0.83), RARS1 (0.83), CCT5 (0.82), EIF3L (0.81); STRING partners: AARS1 (0.98), FARSB (0.914), NARS1 (0.965), QARS1 (0.999), RARS1 (0.999), SARS1 (0.908), WARS1 (0.85), YARS1 (0.966)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Isoleucine-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family and has been identified as a …
- **Diseases (Open Targets)**: growth retardation, intellectual developmental disorder, hypotonia, and hepatopathy (0.733); Abnormality of the skeletal system (0.332); microcephaly (0.289); Global developmental delay (0.289); Hallux valgus (0.184)
- **Europe PMC papers**: 184
- **Why important**: IARS1 is a central network member with connections to RHOT1, YARS1, RECQL, HYOU1, CCT7, FARSB, QARS1, and SRP68. It is included in the core aminoacyl-tRNA evidence (6 globally significant GO/KEGG terms, q_global 3.09e-05–3.09e-05; see the table), (GO:MF catalytic activity, acting on a tRNA; q_global = 0.000176), (GO:BP tRNA metabolic process; q_global = 0.000479), (GO:MF catalytic activity, acting on RNA; q_global = 0.00104), (GO:MF ligase activity; q_global = 0.008), (GO:BP translation; q_global = 0.0349), and (GO:BP protein biosynthetic process; q_global = 0.0349), and has extensive STRING support for the synthetase group (15 supplementary STRING terms; within-query FDR 8.8e-06–0.00022). Its annotation identifies it as an isoleucyl-tRNA synthetase, and its disease associations include developmental and skeletal abnormalities. Its literature volume is substantial, supporting an established biological role.
- **Conclusion**: Established conclusion: IARS1 is a representative catalytic anchor of the module's translation and tRNA-aminoacylation program. Hypothesis: variation in IARS1 abundance may influence the translational capacity of the shared cell populations and help couple translation to chaperoning and mitochondrial organization.

#### CCT7

- **Related proteins** (co-abundance neighbors): CCT5 (0.95), CCT8 (0.94), DDX5 (0.90), CCT3 (0.90), RHOT1 (0.85), IARS1 (0.85), FARSB (0.83), CAPRIN1 (0.83), WARS1 (0.82), HYOU1 (0.81), HSP90AA1 (0.81), SDHA (0.81); STRING partners: ATIC (0.881), CCT3 (0.999), CCT5 (0.999), CCT8 (0.999), HSP90AA1 (0.849), IMPDH2 (0.758)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 has one of the strongest network positions among the module genes and connects to the other CCT subunits, DDX5, RHOT1, IARS1, FARSB, and CAPRIN1. It is part of the CCT complex in hu.MAP (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14442.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1) and has very strong STRING relationships with CCT3, CCT5, and CCT8. It contributes to the broad set of globally corrected chaperone, telomere-maintenance, Cajal-body, translation-related, and sperm-recognition annotations (58 globally significant GO/KEGG terms, q_global 4.48e-05–0.0481; see the table). Its established function is ATP-dependent folding of proteins within the CCT complex, and it has a substantial literature base.
- **Conclusion**: Established conclusion: CCT7 is a principal proteostasis component and a strong structural marker of the CCT subnetwork. Hypothesis: CCT7 may help buffer the increased folding burden associated with active translation or differentiation in the shared bone-marrow and testis cell populations.

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT5 (0.94), CCT7 (0.94), CCT3 (0.91), CAPRIN1 (0.89), SDHA (0.84), DDX5 (0.84), WARS1 (0.83), RECQL (0.82), SNTB2 (0.80), HSP90AA1 (0.80); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999), HSP90AA1 (0.823)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is a connected member of the CCT core, linked to CCT3, CCT5, CCT7, CAPRIN1, SDHA, DDX5, WARS1, and RECQL. It is supported by multiple hu.MAP CCT complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14442.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1) and (hu.MAP huMAP3_09020.1), by strong STRING relationships with the other CCT subunits, and by the same globally corrected chaperone, telomere, Cajal-body, DNA-biosynthesis, and sperm-recognition terms as the other CCT genes. HPA detects it in both tissues and shows cell-type enhancement in oocytes. Its annotated role is ATP-dependent chaperone-mediated protein folding, and its literature volume is substantial.
- **Conclusion**: Established conclusion: CCT8 is a core component of the module's protein-folding machinery and a plausible bridge between translation and proteostasis. Hypothesis: CCT8-associated folding capacity may be especially important in germ-cell or progenitor states that require rapid production and remodeling of proteins.

#### YARS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.87), DDX5 (0.84), FARSB (0.84), RECQL (0.83); STRING partners: AARS1 (0.996), FARSB (0.946), IARS1 (0.966), NARS1 (0.966), QARS1 (0.959), RARS1 (0.942), SARS1 (0.941), WARS1 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: huMAP3_10115.1, huMAP3_14442.1, huMAP3_10302.1, huMAP3_04783.1
- **Function (MyGene.info)**: tyrosyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Tyrosyl-tRNA synthetase belongs to the class I tRNA synthetase family. Cytokine activities have also been observ…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease dominant intermediate C (0.739); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset 2 (0.707); hereditary disease (0.509); Charcot-Marie-Tooth disease (0.418); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset (0.333)
- **Europe PMC papers**: 215
- **Why important**: YARS1 belongs to the dense synthetase interaction group, with STRING links to AARS1, FARSB, IARS1, NARS1, QARS1, RARS1, SARS1, and WARS1. It is present in the core aminoacyl-tRNA enrichment (6 globally significant GO/KEGG terms, q_global 3.09e-05–3.09e-05; see the table) and related translation and RNA terms, and in several hu.MAP assemblies (hu.MAP huMAP3_10115.1), (hu.MAP huMAP3_14442.1), (hu.MAP huMAP3_10302.1), and (hu.MAP huMAP3_04783.1). Its annotated function is tyrosyl-tRNA aminoacylation, with additional reported stress and apoptotic functions. It is detected in both tissues and has disease associations involving peripheral neuropathy and multisystem developmental disorders.
- **Conclusion**: Established conclusion: YARS1 is a well-connected representative of the module's tRNA-charging machinery and may provide a useful readout of its translation-related component. Hypothesis: YARS1 could contribute to coupling translational fidelity with stress adaptation in the shared cell populations, although the co-abundance data do not establish a noncanonical signaling role.

#### DDX5

- **Related proteins** (co-abundance neighbors): CCT7 (0.90), RARS1 (0.89), FARSB (0.87), RHOT1 (0.85), CCT5 (0.84), YARS1 (0.84), CCT8 (0.84), LMNB2 (0.83), IMPDH2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: huMAP3_05711.1, huMAP3_07909.1, huMAP3_09754.1, huMAP3_10631.1, huMAP3_11111.1
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 occupies a bridge-like position between CCT genes, aminoacyl-tRNA synthetases, RHOT1, and LMNB2. It is included in globally corrected ATP, nucleotide-binding, RNA-binding, nucleic-acid, gene-expression, and translation-related terms (GO:MF ATP binding; q_global = 0.000126), (GO:MF adenyl ribonucleotide binding; q_global = 0.000134), (GO:MF nucleotide binding; q_global = 0.000394), (GO:MF nucleoside phosphate binding; q_global = 0.000494), (GO:MF adenyl nucleotide binding; q_global = 0.000922), (GO:MF purine ribonucleoside triphosphate binding; q_global = 0.000964), (GO:MF purine ribonucleotide binding; q_global = 0.00101), (5 globally significant GO/KEGG terms, q_global 0.00104–0.00144; see the table), (GO:MF carbohydrate derivative binding; q_global = 0.00461) (GO:MF purine nucleotide binding; q_global = 0.005) (GO:BP nucleic acid metabolic process; q_global = 0.00521), (GO:BP nucleobase-containing compound metabolic process; q_global = 0.0173), (GO:MF RNA binding; q_global = 0.0215), and (GO:BP gene expression; q_global = 0.0267). hu.MAP places it with CAPRIN1 in multiple RNA-associated complexes (hu.MAP huMAP3_05711.1) (hu.MAP huMAP3_07909.1) (hu.MAP huMAP3_09259.1) (hu.MAP huMAP3_09754.1) and (hu.MAP huMAP3_10631.1) (hu.MAP huMAP3_11111.1). Its established function is an RNA helicase and adaptor involved in RNA structure, splicing, transcriptional regulation, and small noncoding RNA processing. It has a large literature volume and disease associations including viral disease and colorectal cancer.
- **Conclusion**: Established conclusion: DDX5 is a plausible regulatory bridge linking RNA processing and gene expression to the translation and chaperone subnetworks. Hypothesis: DDX5 may coordinate RNA maturation with the high translational and proteostatic state represented by the module, but this regulatory direction requires experimental testing.

## Module 10

**Tissue pair**: bone_marrow and testis  
**Genes (14)**: ANXA4, APEX1, ARPC1B, DDAH1, DDAH2, FDPS, GNPDA2, HEBP1, LDHB, NIT2, PRDX3, RRAS, ACAA1, UCHL1

### Function

The module does not have a statistically supported GO or KEGG functional enrichment term after global correction. Its genes nevertheless suggest a heterogeneous intracellular program spanning mitochondrial and oxidative-stress biology, nitric-oxide and methylarginine regulation, intermediary and lipid metabolism, DNA repair, ubiquitin processing, and actin-dependent cellular organization. The co-abundance network links DDAH1 and PRDX3 centrally to several metabolic or redox-related genes, while RRAS connects metabolic genes with ARPC1B and therefore with cytoskeletal and signaling biology. These patterns support a shared cellular-state signal rather than a narrowly defined pathway. The absence of a globally enriched term limits confidence in assigning one specific module function.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. Protein detection is broad in both tissues, with most genes detected in bone marrow and all genes detected in testis, but this does not establish a tissue-specific mechanism. Most genes have low immune-cell specificity, and only RRAS has a blood-cell group-enriched annotation involving intermediate and non-classical monocytes. The HPA patterns are otherwise heterogeneous, including kidney, liver, blood vessel, lymphoid tissue, heart muscle, gallbladder, pancreas, brain, and pituitary associations, together with diverse epithelial, stromal, hepatocyte, germ-cell, and progenitor cell annotations. Thus, the shared module is unlikely to be explained simply by a plasma-protein signal or a generic blood-cell program. It may instead reflect broadly distributed cellular metabolism and stress biology, or differing cellular mixtures in the two tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes, no STRING functional-enrichment result, and no hu.MAP complex containing multiple module members. The internal edges are therefore co-abundance relationships rather than independently documented protein interactions. Several genes have well-established individual functions, such as PRDX3 in mitochondrial antioxidant biology, DDAH1 and DDAH2 in methylarginine and nitric-oxide regulation, LDHB in lactate metabolism, FDPS in sterol and isoprenoid synthesis, RRAS in signaling and cell adhesion, and ARPC1B in Arp2/3-mediated actin nucleation. However, the available STRING and hu.MAP evidence does not support a pre-existing physical complex or a single known protein-interaction pathway for the module.

**STRING interactions (score >= 0.7)**: 0 of 91 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a new biological discovery solely because it is absent from STRING or hu.MAP. Those databases may omit context-specific, transient, indirect, or abundance-linked relationships. The module is potentially novel as a cross-tissue co-abundance pattern because it joins genes from several established biological systems without a matching high-confidence interaction network, complex, or globally enriched GO or KEGG term. Nevertheless, the current evidence supports novelty of the observed tissue-pair association more strongly than novelty of the individual gene functions or of a defined molecular complex. Independent replication, cell-type-aware analysis, and experimental testing would be needed before claiming a new mechanism.

**Hypothesis.** Hypothesis: the module represents a coordinated cellular adaptation that couples mitochondrial redox control and nitric-oxide availability with energy, lipid, and carbohydrate metabolism, while also influencing cytoskeletal organization and stress-responsive signaling. PRDX3, DDAH1, and DDAH2 could provide a redox and methylarginine regulatory core; LDHB, FDPS, ACAA1, NIT2, and GNPDA2 could reflect metabolic state; and RRAS with ARPC1B could connect that state to adhesion, polarity, migration, or actin remodeling. A shared cell-state or sample-composition effect across bone marrow and testis is an alternative explanation. This is a hypothesis, not a demonstrated physical pathway, because enrichment, STRING, and hu.MAP evidence do not establish it.

### Important genes

#### DDAH1

- **Related proteins** (co-abundance neighbors): HEBP1 (0.90), LDHB (0.84), NIT2 (0.83), PRDX3 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dimethylarginine dimethylaminohydrolase 1. This gene belongs to the dimethylarginine dimethylaminohydrolase (DDAH) gene family. The encoded enzyme plays a role in nitric oxide generation by regulating cellular concentrations of methylarginines, which in turn inhibit nitric oxide synthase activity. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: aortic stenosis (0.372); osteoarthritis, knee (0.272); medical procedure (0.272); Alzheimer disease (0.257); seborrheic keratosis (0.240)
- **Europe PMC papers**: 1290
- **Why important**: DDAH1 has one of the strongest and most connected positions in the module and links directly to HEBP1, LDHB, NIT2, and PRDX3. Its established function is to regulate methylarginine concentrations and thereby nitric-oxide synthase activity; the supplied annotations also connect it with arginine metabolism, vascular permeability, blood-pressure regulation, and nitric-oxide biosynthesis. Its disease-association evidence includes aortic stenosis and knee osteoarthritis, and its literature volume is substantial.
- **Conclusion**: Established conclusion: DDAH1 is a plausible regulatory anchor for nitric-oxide and arginine-related biology within the co-abundance pattern. Hypothesis: it may help couple vascular or cellular signaling to the module’s metabolic and redox genes, but the module does not prove that DDAH1 controls the other members.

#### PRDX3

- **Related proteins** (co-abundance neighbors): LDHB (0.85), FDPS (0.84), DDAH1 (0.83), DDAH2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Mitochondria; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peroxiredoxin 3. This gene encodes a mitochondrial protein with antioxidant function. The protein is similar to the C22 subunit of Salmonella typhimurium alkylhydroperoxide reductase, and it can rescue bacterial resistance to alkylhydroperoxide in E. coli that lack the C22 subunit. The human and mouse genes are highly conserved, and they map to the regions syntenic between mouse and human chromosomes. Sequence com…
- **Diseases (Open Targets)**: spinocerebellar ataxia, autosomal recessive 32 (0.653); corneal dystrophy, punctiform and polychromatic pre-descemet (0.571); autosomal recessive cerebellar ataxia (0.268); neurodegenerative disease (0.257); hereditary disease (0.191)
- **Europe PMC papers**: 2613
- **Why important**: PRDX3 is among the most connected genes and links LDHB, FDPS, DDAH1, and DDAH2. It is an established mitochondrial antioxidant protein associated with response to oxidative stress, mitochondrial organization, and myeloid-cell differentiation. HPA detects it in both tissues, and its disease associations include recessive cerebellar and neurodegenerative disorders. It also has a relatively large literature base.
- **Conclusion**: Established conclusion: PRDX3 provides the strongest direct redox and mitochondrial interpretation of the module. Hypothesis: it may coordinate oxidative-stress handling with metabolic and nitric-oxide processes in the shared cellular state.

#### RRAS

- **Related proteins** (co-abundance neighbors): ACAA1 (0.85), ARPC1B (0.82), GNPDA2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAS related. The protein encoded by this gene is a small GTPase involved in diverse processes including angiogenesis, vascular homeostasis and regeneration, cell adhesion, and neuronal axon guidance. Mutations in this gene are found in many invasive cancers. [provided by RefSeq, Jul 2015].
- **Diseases (Open Targets)**: Noonan syndrome (0.424); Noonan syndrome and Noonan-related syndrome (0.370); hypertensive disorder (0.324); neurodegenerative disease (0.288); hereditary disease (0.266)
- **Europe PMC papers**: 1607
- **Why important**: RRAS occupies a bridging position, connecting ACAA1, ARPC1B, and GNPDA2. Its established functions include Ras signaling, angiogenesis, vascular homeostasis, cell adhesion, polarity, and endothelial migration. HPA identifies blood-vessel enhancement and group enrichment in intermediate and non-classical monocytes. Its annotations also include leukocyte differentiation and cancer-related mutations, with substantial literature and disease evidence including Noonan-related syndromes and hypertensive disorder.
- **Conclusion**: Established conclusion: RRAS is the most informative candidate for linking the module to signaling, adhesion, vascular biology, and selected myeloid-cell states. Hypothesis: it may connect metabolic status to changes in cell polarity or cytoskeletal behavior across the two tissues.

#### LDHB

- **Related proteins** (co-abundance neighbors): PRDX3 (0.85), DDAH1 (0.84), ARPC1B (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lactate dehydrogenase B. This gene encodes the B subunit of lactate dehydrogenase enzyme, which catalyzes the interconversion of pyruvate and lactate with concomitant interconversion of NADH and NAD+ in a post-glycolysis process. Alternatively spliced transcript variants have been found for this gene. Recent studies have shown that a C-terminally extended isoform is produced by use of an alternative in-frame translation t…
- **Diseases (Open Targets)**: glycogen storage disease due to lactate dehydrogenase H-subunit deficiency (0.724); type 2 diabetes mellitus (0.271); adverse effect (0.184); neoplasm (0.117); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 5204
- **Why important**: LDHB is highly connected and links PRDX3, DDAH1, and ARPC1B, placing lactate and redox metabolism near both the nitric-oxide-related and cytoskeletal parts of the network. Its established enzyme function interconverts pyruvate and lactate while coupling NADH and NAD+, and its annotations include lactate and NAD+ metabolism. It has strong literature coverage and disease associations involving lactate-dehydrogenase deficiency, metabolic disease, and hepatocellular carcinoma.
- **Conclusion**: Established conclusion: LDHB is a credible marker of metabolic state within the module. Hypothesis: altered lactate and redox balance could be the metabolic context that makes the other co-abundance relationships appear across bone marrow and testis.

#### FDPS

- **Related proteins** (co-abundance neighbors): APEX1 (0.86), PRDX3 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: farnesyl diphosphate synthase. This gene encodes an enzyme that catalyzes the production of geranyl pyrophosphate and farnesyl pyrophosphate from isopentenyl pyrophosphate and dimethylallyl pyrophosphate. The resulting product, farnesyl pyrophosphate, is a key intermediate in cholesterol and sterol biosynthesis, a substrate for protein farnesylation and geranylgeranylation, and a ligand or agonist for certain hormone receptors …
- **Diseases (Open Targets)**: porokeratosis 9, multiple types (0.637); disseminated superficial actinic porokeratosis (0.619); osteoporosis (0.611); postmenopausal osteoporosis (0.601); plasma cell myeloma (0.599)
- **Europe PMC papers**: 2675
- **Why important**: FDPS connects PRDX3 to APEX1 and represents sterol and isoprenoid metabolism. Its established enzyme activity produces farnesyl and geranylgeranyl intermediates used in sterol biosynthesis, protein prenylation, and hormone or growth-receptor signaling. HPA shows liver enhancement and detection in both tissues. Its disease associations include osteoporosis, postmenopausal osteoporosis, porokeratosis, and plasma-cell myeloma, and it has a substantial literature base.
- **Conclusion**: Established conclusion: FDPS supplies a credible lipid-biosynthetic and protein-prenylation component. Hypothesis: it could influence RRAS-related signaling indirectly through prenylation-dependent regulation, but that connection is not demonstrated by the supplied network.

#### ARPC1B

- **Related proteins** (co-abundance neighbors): LDHB (0.83), RRAS (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: actin related protein 2/3 complex subunit 1B. This gene encodes one of seven subunits of the human Arp2/3 protein complex. This subunit is a member of the SOP2 family of proteins and is most similar to the protein encoded by gene ARPC1A. The similarity between these two proteins suggests that they both may function as p41 subunit of the human Arp2/3 complex that has been implicated in the control of actin polymerization in cells. It is possib…
- **Diseases (Open Targets)**: platelet abnormalities with eosinophilia and immune-mediated inflammatory disease (0.771); combined immunodeficiency (0.429); autoimmune disorder of central nervous system (0.397); cutaneous leishmaniasis (0.370); immunodeficiency disease (0.346)
- **Europe PMC papers**: 1334
- **Why important**: ARPC1B links LDHB with RRAS and is the module’s clearest actin-cytoskeleton component. It is an established subunit of the Arp2/3 complex and is annotated for cortical actin organization and Arp2/3-mediated actin nucleation. HPA associates it with lymphoid tissue and several macrophage, monocyte, megakaryocyte, and trophoblast-related cell types. Its disease evidence includes platelet abnormalities, combined immunodeficiency, and immune-mediated disorders, with a substantial literature base.
- **Conclusion**: Established conclusion: ARPC1B supports a cytoskeletal and cell-interaction interpretation and is relevant to immune and hematopoietic biology. Hypothesis: it may translate metabolic or Ras-associated signals into actin remodeling, although no hu.MAP or STRING evidence establishes a module-level complex.

## Module 11

**Tissue pair**: bone_marrow and testis  
**Genes (12)**: ARMC6, BCL2L13, CHDH, DOHH, HSPBP1, HSPA2, LZTFL1, TRIP13, PPOX, PTGR2, DARS2, UFD1

### Function

This is a heterogeneous module rather than a cleanly enriched pathway. No GO or KEGG term passed global correction, and there was no supplementary STRING functional-enrichment result. The network nevertheless contains several interpretable functional components: mitochondrial metabolism and biosynthesis through PPOX, DARS2, and CHDH; protein folding and ubiquitin-linked quality control through HSPA2 and HSPBP1; meiotic and spermatogenic biology through TRIP13 and HSPA2; and ciliary or sperm-associated biology through LZTFL1 and the HPA single-cell annotations. The sparse network and absence of globally significant enrichment mean that these functions should be treated as convergent biological signals and hypotheses, not as a single demonstrated pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low immune-cell specificity, so this is not primarily a blood-cell module. However, every gene has cell-type-enhanced expression, with recurrent annotations involving late spermatids, ciliated epithelial cells, and erythrocyte progenitors. Several genes are detected in both bone marrow and testis, whereas others are detected mainly in testis or bone marrow. The shared signal may therefore reflect shared cell states, mitochondrial or proteostasis demands, and overlapping developmental programs rather than a conventional blood-derived secreted-protein signature. Testis protein detection is broad across the module, while bone-marrow detection is more mixed.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports one high-confidence pair, HSPA2-HSPBP1, providing direct external support for a proteostasis-related connection in the module. The remaining module pairs are not supported by high-confidence STRING interactions in the supplied evidence. hu.MAP identifies PPOX, DARS2, and CHDH together in two mitochondrial or metabolic complexes (hu.MAP huMAP3_10525.1) (hu.MAP huMAP3_13468.1). HSPA2 and HSPBP1 recur together in several chaperone, stress-response, and protein-quality-control complexes (hu.MAP huMAP3_05866.1) (hu.MAP huMAP3_06506.1) (hu.MAP huMAP3_13227.1) (hu.MAP huMAP3_07919.1) (hu.MAP huMAP3_11049.1) (hu.MAP huMAP3_13774.1) (hu.MAP huMAP3_14723.1). These are partial memberships rather than evidence that the entire module is one physical complex. Overall, the external resources support two local modules or anchors: a mitochondrial metabolic group and an HSPA2-HSPBP1 proteostasis group.

**STRING interactions (score >= 0.7)**: 1 of 66 gene pairs: HSPA2–HSPBP1 (0.882)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10525.1 (PPOX, DARS2, CHDH; 3/33); huMAP3_13468.1 (PPOX, DARS2, CHDH; 3/99); huMAP3_05866.1 (HSPA2, HSPBP1; 2/12); huMAP3_06506.1 (HSPA2, HSPBP1; 2/23); huMAP3_13227.1 (HSPA2, HSPBP1; 2/24); huMAP3_07919.1 (HSPA2, HSPBP1; 2/27); huMAP3_11049.1 (HSPA2, HSPBP1; 2/30); huMAP3_13774.1 (HSPA2, HSPBP1; 2/33); huMAP3_14723.1 (HSPA2, HSPBP1; 2/52)

### Novelty

The exact co-abundance module appears potentially novel, but the evidence does not establish a newly discovered molecular complex or pathway. Its genes have established individual functions, HSPA2-HSPBP1 is already supported by STRING, and subsets recur in hu.MAP complexes. The unusual feature is their co-abundance across bone marrow and testis, together with links among mitochondrial metabolism, proteostasis, meiotic biology, and ciliary or spermatid-associated cell states. Absence of broader STRING support does not by itself prove novelty. The most defensible conclusion is provisional novelty at the level of the cross-tissue co-abundance pattern, not novelty of the component biology.

**Hypothesis.** Hypothesis: this conserved module reflects a shared cellular program needed when differentiating or highly specialized cells coordinate mitochondrial biosynthesis with protein quality control. In testis, the program could support meiotic progression, spermatid development, flagellar or ciliary functions, and the handling of newly synthesized or structurally demanding proteins. In bone marrow, the same abundance pattern could arise in metabolically active progenitors or related cell states, including erythrocyte progenitors. PPOX, DARS2, and CHDH may represent the mitochondrial metabolic arm, while HSPA2-HSPBP1 represents a chaperone and ubiquitin-dependent quality-control arm; TRIP13 and LZTFL1 may connect this state to meiotic and ciliary biology. This model is not demonstrated by enrichment and requires validation with cell-resolved expression, perturbation, and protein-level interaction experiments.

### Important genes

#### PTGR2

- **Related proteins** (co-abundance neighbors): TRIP13 (0.92), HSPBP1 (0.89), BCL2L13 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prostaglandin reductase 2. This gene encodes an enzyme involved in the metabolism of prostaglandins. The encoded protein catalyzes the NADPH-dependent conversion of 15-keto-prostaglandin E2 to 15-keto-13,14-dihydro-prostaglandin E2. This protein may also be involved in regulating activation of the peroxisome proliferator-activated receptor. Alternative splicing results in multiple transcript variants. [provided by RefSeq, A…
- **Diseases (Open Targets)**: autoimmune disorder of central nervous system (0.274); retinitis pigmentosa (0.077); cone-rod dystrophy (0.076); nonpapillary renal cell carcinoma (0.074); Leber congenital amaurosis (0.068)
- **Europe PMC papers**: 238
- **Why important**: PTGR2 is among the more connected nodes and links TRIP13, HSPBP1, and BCL2L13, placing prostaglandin metabolism near the module's proteostasis and mitochondrial branches. Its established function is NADPH-dependent prostaglandin metabolism, and it may regulate peroxisome-proliferator-activated receptor activity. It has vesicular localization and cell-type-enhanced annotations in neural cells and basophils, but no STRING or hu.MAP support in this module.
- **Conclusion**: Established: PTGR2 is a prostaglandin-metabolizing enzyme and a network bridge. Hypothesis: it may couple lipid-mediator metabolism to stress or mitochondrial state in the shared module. The co-abundance data do not establish that PTGR2 regulates the other module branches.

#### PPOX

- **Related proteins** (co-abundance neighbors): ARMC6 (0.87), CHDH (0.82), DARS2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: huMAP3_10525.1, huMAP3_13468.1
- **Function (MyGene.info)**: protoporphyrinogen oxidase. This gene encodes the penultimate enzyme of heme biosynthesis, which catalyzes the 6-electron oxidation of protoporphyrinogen IX to form protoporphyrin IX. Mutations in this gene cause variegate porphyria, an autosomal dominant disorder of heme metabolism resulting from a deficiency in protoporphyrinogen oxidase, an enzyme located on the inner mitochondrial membrane. Alternatively spliced transcri…
- **Diseases (Open Targets)**: variegate porphyria (0.855); variegate porphyria, childhood-onset (0.811); neurodegenerative disease (0.520); Abnormal blistering of the skin (0.423); hereditary disease (0.341)
- **Europe PMC papers**: 938
- **Why important**: PPOX is a central metabolic node connected to ARMC6, CHDH, and DARS2 and is present with DARS2 and CHDH in two hu.MAP complexes (hu.MAP huMAP3_10525.1) (hu.MAP huMAP3_13468.1). It catalyzes a penultimate step in heme biosynthesis, localizes to mitochondria, is detected in both tissues, and is associated with variegate porphyria. Its network position and external complex membership make it a strong candidate for the mitochondrial arm of the module.
- **Conclusion**: Established: PPOX participates in mitochondrial heme biosynthesis, has disease relevance through variegate porphyria, and occupies a supported metabolic subnetwork. Hypothesis: its coordinated abundance with the other mitochondrial genes may reflect heme or respiratory-metabolic demand in shared progenitor or germ-cell states.

#### HSPA2

- **Related proteins** (co-abundance neighbors): HSPBP1 (0.89), DARS2 (0.80); STRING partners: HSPBP1 (0.882)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Flagellar centriole, Annulus; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_05866.1, huMAP3_06506.1, huMAP3_13227.1, huMAP3_07919.1, huMAP3_11049.1, huMAP3_13774.1, huMAP3_14723.1
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 2. Enables disordered domain specific binding activity; enzyme binding activity; and unfolded protein binding activity. Involved in negative regulation of inclusion body assembly and protein refolding. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: glaucoma (0.294); open-angle glaucoma (0.278); hypothyroidism (0.122); non-small cell lung carcinoma (0.100); neoplasm (0.094)
- **Europe PMC papers**: 2107
- **Why important**: HSPA2 connects HSPBP1 and DARS2, is supported by the STRING HSPA2-HSPBP1 interaction, and recurs with HSPBP1 across several hu.MAP complexes (hu.MAP huMAP3_05866.1) (hu.MAP huMAP3_06506.1) (hu.MAP huMAP3_13227.1) (hu.MAP huMAP3_07919.1) (hu.MAP huMAP3_11049.1) (hu.MAP huMAP3_13774.1) (hu.MAP huMAP3_14723.1). It is an HSPA-family chaperone involved in protein refolding, unfolded-protein responses, spermatogenesis, and spermatid development. Its localization includes vesicles, the flagellar centriole, and the annulus, and it has a substantial literature base.
- **Conclusion**: Established: HSPA2 is a chaperone with male germ-cell relevance and a directly supported relationship to HSPBP1. Hypothesis: HSPA2 may be the principal proteostasis anchor that links the module to the demands of spermatid or ciliary protein assembly. The data do not show that it drives the cross-tissue module.

#### HSPBP1

- **Related proteins** (co-abundance neighbors): HSPA2 (0.89), PTGR2 (0.89); STRING partners: HSPA2 (0.882)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: huMAP3_05866.1, huMAP3_06506.1, huMAP3_13227.1, huMAP3_07919.1, huMAP3_11049.1, huMAP3_13774.1, huMAP3_14723.1
- **Function (MyGene.info)**: HSPA (Hsp70) binding protein 1. Enables ubiquitin protein ligase binding activity. Involved in positive regulation of proteasomal ubiquitin-dependent protein catabolic process and positive regulation of protein ubiquitination. Predicted to be active in endoplasmic reticulum. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.372); hypothyroidism (0.218); breast cancer (0.077); non-syndromic male infertility due to sperm motility disorder (0.076); breast carcinoma (0.076)
- **Europe PMC papers**: 511
- **Why important**: HSPBP1 is directly connected to HSPA2 and PTGR2 and is present with HSPA2 in multiple hu.MAP complexes (hu.MAP huMAP3_05866.1) (hu.MAP huMAP3_06506.1) (hu.MAP huMAP3_13227.1) (hu.MAP huMAP3_07919.1) (hu.MAP huMAP3_11049.1) (hu.MAP huMAP3_13774.1) (hu.MAP huMAP3_14723.1). Its established activities include HSPA binding and positive regulation of protein ubiquitination and proteasomal degradation. It is detected in both bone marrow and testis and provides an experimentally supported proteostasis link within an otherwise sparse network.
- **Conclusion**: Established: HSPBP1 participates in HSPA-associated protein quality control and ubiquitin-dependent degradation, with direct STRING support for its relationship to HSPA2. Hypothesis: it may coordinate chaperone handling and selective turnover of proteins during differentiation. Its role in this particular conserved module remains inferential.

#### TRIP13

- **Related proteins** (co-abundance neighbors): PTGR2 (0.92), LZTFL1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thyroid hormone receptor interactor 13. This gene encodes a protein that interacts with thyroid hormone receptors, also known as hormone-dependent transcription factors. The gene product interacts specifically with the ligand binding domain. This gene is one of several that may play a role in early-stage non-small cell lung cancer. [provided by RefSeq, Oct 2009].
- **Diseases (Open Targets)**: mosaic variegated aneuploidy syndrome 3 (0.699); oocyte maturation defect 9 (0.600); neurodegenerative disease (0.555); mosaic variegated aneuploidy syndrome (0.503); Wilms tumor (0.375)
- **Europe PMC papers**: 1557
- **Why important**: TRIP13 links PTGR2 and LZTFL1 and is tissue-enhanced in testis, with cell-type-enhanced annotations in differentiating spermatogonia, primary spermatocytes, and early spermatids. Its established functions include meiotic checkpoint signaling, synaptonemal-complex assembly, reciprocal meiotic recombination, and spermatogenesis. It also has a substantial literature base and disease associations involving meiotic or chromosomal abnormalities.
- **Conclusion**: Established: TRIP13 is a meiotic and genome-maintenance factor with strong testis relevance. Hypothesis: it may mark the reproductive-cell component of the module and connect meiotic progression to proteostasis and metabolic demands. The available network does not establish a direct physical interaction between TRIP13 and the other module proteins.

## Module 12

**Tissue pair**: bone_marrow and testis  
**Genes (13)**: BABAM2, DCPS, HS1BP3, IAH1, EIF4A2, AK4, MVK, MBOAT7, ALDH6A1, OPA1, MRPS22, RTCA, TBC1D23

### Function

No GO or KEGG term passed global multiple-testing correction, so the module does not have a formally established pathway-level enrichment. Its gene annotations instead suggest a heterogeneous cellular maintenance program involving RNA processing and translation, mitochondrial activity, lipid and sterol metabolism, vesicle trafficking, DNA-damage responses, and apoptosis regulation. The network is organized around HS1BP3, which connects to most other module members, while TBC1D23 forms a smaller branch linking EIF4A2, AK4, and ALDH6A1. This topology is more consistent with coordinated expression across several cellular processes than with a single confidently identified biochemical pathway. The lack of enrichment should not be interpreted as evidence that the module is biologically false.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and all module genes have HPA annotations. The module is detected in both bone marrow and testis, but its single-cell signals are mostly cell-type enhanced rather than broadly uniform. Testis-associated signals include late primary spermatocytes, early spermatids, and late spermatids, while other signals involve esophageal apical cells, hepatocytes, adrenal cortex cells, neutrophils, and myeloid or dendritic populations. Several genes show liver, kidney, or adrenal enrichment, and some show blood-cell enhancement, including eosinophils, plasmacytoid dendritic cells, monocytes, myeloid dendritic cells, basophils, and neutrophils. Thus, the shared module may reflect common cellular composition or state across the sampled tissues, especially germ-cell and hematopoietic or myeloid contributions, rather than a bone-marrow-and-testis-specific secreted program. MBOAT7 is detected in testis but not bone marrow, and IAH1 is detected in testis but not bone marrow, which further argues for possible composition or cell-state effects.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair reaches the stated high-confidence STRING interaction threshold, and STRING reports no functional enrichment. No hu.MAP complex contains at least two module members. Therefore, the co-abundance relationships are not supported here by known physical or functional interaction evidence from these resources. The strongest module edge pattern is an expression-network observation, not proof of direct binding, shared complex membership, or a single molecular mechanism. The absence of STRING and hu.MAP matches also means that the apparent HS1BP3-centered structure should be treated as a hypothesis-generating organization.

**STRING interactions (score >= 0.7)**: 0 of 78 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module is potentially novel as a cross-tissue co-abundance pattern because it combines genes from RNA metabolism, mitochondrial function, lipid remodeling, sterol synthesis, vesicle transport, DNA repair, and germ-cell or immune-cell expression without corresponding STRING or hu.MAP support. However, it cannot be called a newly discovered molecular complex or pathway. The lack of database support alone does not prove novelty: it may reflect indirect co-regulation, cell-type mixture, tissue sampling, incomplete database coverage, or a module-specific statistical structure. The most defensible novelty claim is therefore that this particular shared expression organization merits validation, not that its underlying physical biology is unprecedented.

**Hypothesis.** Hypothesis: the module represents a shared cellular adaptation program in hematopoietic and testicular samples, in which mitochondrial energy and translation capacity, lipid or sterol remodeling, RNA turnover, and vesicle trafficking are coordinated across particular cell populations. HS1BP3 may mark or help organize this co-abundance state, while OPA1 and MRPS22 reflect mitochondrial maintenance, MBOAT7 and MVK reflect membrane-lipid and sterol metabolism, DCPS and RTCA reflect RNA handling, and TBC1D23 reflects intracellular trafficking. The apparent cross-tissue conservation may therefore arise from common demands of differentiating germ cells and selected marrow immune or myeloid cells, rather than from one shared protein complex. This hypothesis requires validation with cell-resolved expression, perturbation, and independent cohorts.

### Important genes

#### HS1BP3

- **Related proteins** (co-abundance neighbors): DCPS (0.88), BABAM2 (0.87), MRPS22 (0.86), RTCA (0.85), MBOAT7 (0.84), MVK (0.84), OPA1 (0.81), IAH1 (0.81), EIF4A2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HCLS1 binding protein 3. The protein encoded by this gene shares similarity with mouse Hs1bp3, an Hcls1/Hs1-interacting protein that may be involved in lymphocyte activation. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: prolapse of female genital organ (0.300); liver disorder (0.233); Tietze syndrome (0.145); prostate carcinoma (0.090); Hypercholesterolemia (0.082)
- **Europe PMC papers**: 165
- **Why important**: HS1BP3 is the central network hub, connecting to most of the other module genes and therefore providing the strongest structural anchor for interpreting the module. Its HPA signal includes late spermatids, and its annotated function concerns regulation of apoptosis with a possible relationship to lymphocyte activation. It has a relatively focused literature compared with highly studied mitochondrial or translation genes, and its disease associations are comparatively nonspecific. That combination makes it important primarily as a module-organizing candidate rather than as an already established mechanistic driver.
- **Conclusion**: Established evidence: HS1BP3 is the module's most connected gene and is detected in both tissues, with a late-spermatid cell-type signal. Hypothesis: HS1BP3 may coordinate or mark the shared cellular state. Its role in this module remains unproven because neither STRING nor hu.MAP provides supporting interaction evidence.

#### OPA1

- **Related proteins** (co-abundance neighbors): HS1BP3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OPA1 mitochondrial dynamin like GTPase. The protein encoded by this gene is a nuclear-encoded mitochondrial protein with similarity to dynamin-related GTPases. The encoded protein localizes to the inner mitochondrial membrane and helps regulate mitochondrial stability and energy output. This protein also sequesters cytochrome c. Mutations in this gene have been associated with optic atrophy type 1, which is a dominantly inherited optic …
- **Diseases (Open Targets)**: autosomal dominant optic atrophy, classic form (0.846); Behr syndrome (0.812); optic atrophy with or without deafness, ophthalmoplegia, myopathy, ataxia, and neuropathy (0.766); mitochondrial DNA depletion syndrome 14B (cardioencephalomyopathic type) (0.745); optic atrophy (0.653)
- **Europe PMC papers**: 12169
- **Why important**: OPA1 is connected directly to the hub and has a well-established role in mitochondrial inner-membrane organization, fusion, and mitochondrial stability. It is detected in both tissues and has a substantial disease literature centered on optic atrophy and related mitochondrial disorders. Its broad tissue and cell-type distribution makes it a plausible indicator of general mitochondrial requirements rather than a tissue-specific marker.
- **Conclusion**: Established evidence: OPA1 supports mitochondrial organization and energy-related interpretation of the module and has strong disease and literature support. Hypothesis: OPA1-linked mitochondrial remodeling may be part of the shared state in marrow and testis. The module does not establish a direct interaction between OPA1 and HS1BP3.

#### MBOAT7

- **Related proteins** (co-abundance neighbors): HS1BP3 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: membrane bound acylglycerophosphatidylinositol O-acyltransferase MBOAT7. This gene encodes a member of the membrane-bound O-acyltransferases family of integral membrane proteins that have acyltransferase activity. The encoded protein is a lysophosphatidylinositol acyltransferase that has specificity for arachidonoyl-CoA as an acyl donor. This protein is involved in the reacylation of phospholipids as part of the phospholipid remodeling pathway known as the Land cycle. …
- **Diseases (Open Targets)**: intellectual disability, autosomal recessive 57 (0.754); hereditary disease (0.487); autosomal recessive non-syndromic intellectual disability (0.462); complex neurodevelopmental disorder (0.370); neurodegenerative disease (0.345)
- **Europe PMC papers**: 1344
- **Why important**: MBOAT7 links the hub to phospholipid remodeling and phosphatidylinositol acyl-chain regulation. It is tissue-enhanced in adrenal gland, shows signals in neural and neutrophil-related cell types, and is associated with intellectual disability and other neurodevelopmental conditions. Its presence broadens the module beyond RNA and mitochondrial biology and supplies a plausible membrane-composition component.
- **Conclusion**: Established evidence: MBOAT7 is a lysophosphatidylinositol acyltransferase involved in phospholipid remodeling and is co-abundant with HS1BP3 in this module. Hypothesis: membrane-lipid remodeling may help support the cellular differentiation or trafficking state represented by the module. A pathway-level role is not demonstrated because no GO or KEGG term passed global correction.

#### DCPS

- **Related proteins** (co-abundance neighbors): HS1BP3 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: decapping enzyme, scavenger. This gene encodes a member of the histidine triad family of pyrophosphatases that removes short mRNA fragments containing the 5' mRNA cap structure, which appear in the 3' -> 5' mRNA decay pathway, following deadenylation and exosome-mediated turnover. This enzyme hydrolyzes the triphosphate linkage of the cap structure (7-methylguanosine nucleoside triphosphate) to yield 7-methylguanosine monopho…
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.670); neurodegenerative disease (0.574); autoimmune disorder of central nervous system (0.428); response to statin (0.282); urinary system disorder (0.201)
- **Europe PMC papers**: 886
- **Why important**: DCPS is connected to the hub and encodes a nuclear mRNA-cap scavenger involved in deadenylation-dependent mRNA decay and RNA processing. It is tissue-enhanced in liver and has cell-type signals in plasmacytoid dendritic cells and plasma cells, including an immune-cell-enhanced blood profile. Its disease associations include intellectual disability and neurodegenerative disease, and its literature is substantial enough to support a credible RNA-metabolism interpretation.
- **Conclusion**: Established evidence: DCPS provides a specific RNA-decapping and mRNA-turnover function and links the module to selected immune-cell populations. Hypothesis: coordinated RNA decay may help tune gene expression during the shared marrow or germ-cell state. This interpretation is gene-based rather than enrichment-based, because no GO or KEGG term passed global correction.

#### TBC1D23

- **Related proteins** (co-abundance neighbors): EIF4A2 (0.83), AK4 (0.83), ALDH6A1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in bone_marrow, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TBC1 domain family member 23. Involved in brain development; retrograde transport, endosome to Golgi; and vesicle tethering to Golgi. Located in cytoplasmic vesicle and trans-Golgi network. Colocalizes with WASH complex. Implicated in pontocerebellar hypoplasia. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: pontocerebellar hypoplasia (0.740); hereditary disease (0.415); Intellectual disability (0.370); neurodegenerative disease (0.344); glaucoma (0.144)
- **Europe PMC papers**: 210
- **Why important**: TBC1D23 is the central member of the module's smaller branch, connecting EIF4A2, AK4, and ALDH6A1. Its established functions include vesicle tethering, retrograde endosome-to-Golgi transport, and association with the WASH complex. It is enhanced in neutrophils and has disease associations involving pontocerebellar hypoplasia and intellectual disability, giving it a mechanistically informative trafficking role despite its modest network connectivity.
- **Conclusion**: Established evidence: TBC1D23 contributes a vesicle-trafficking interpretation and forms a coherent local co-abundance branch with translation and mitochondrial-metabolic genes. Hypothesis: altered intracellular trafficking may coordinate delivery or recycling of components needed by differentiating or metabolically active cells. The branch does not constitute a validated protein complex because hu.MAP and STRING provide no supporting complex or interaction evidence.
