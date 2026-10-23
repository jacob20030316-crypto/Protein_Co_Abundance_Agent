# Conserved co-abundance modules: lung and testis

## Module 0

**Tissue pair**: lung and testis  
**Genes (17)**: SERPINA1, A2M, ALB, CP, CFB, C3, FBLN1, IGKC, ITIH4, LUM, MYH11, DCN, PRELP, TNS1, TF, GC, VTN

### Function

The module is best interpreted as an extracellular blood-derived and connective-tissue interface program. The strongest primary evidence is enrichment for blood microparticles (GO:CC blood microparticle; q_global = 1.81e-05), complement and coagulation cascades (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0144), the Golgi lumen (GO:CC Golgi lumen; q_global = 0.0205), extracellular space (GO:CC extracellular space; q_global = 0.0321), and extracellular-matrix structural constituents that confer compression resistance (GO:MF extracellular matrix structural constituent conferring compression resistance; q_global = 0.0424). Together, these findings indicate coordinated abundance of circulating secreted proteins involved in complement regulation, protease control, transport, adhesion, and matrix organization. C3 and CFB provide the clearest complement-related core, while DCN, LUM, PRELP, and related matrix proteins represent a connective-tissue component. The network therefore does not point to a narrowly lung- or testis-specific intracellular pathway; it more plausibly reflects shared extracellular material, vascular or stromal biology, and/or blood contribution in the two tissue datasets.

**Cell composition.** The module is strongly dominated by secreted or extracellular proteins. HPA annotates most genes as secreted, with many secreted to blood and a smaller matrix-secreted group. Liver and hepatocyte enrichment is especially prominent, including ALB, GC, CP, TF, SERPINA1, ITIH4, C3, CFB, and VTN, whereas several matrix genes are associated with fibroblasts, stromal cells, blood vessels, or smooth muscle. There is also evidence for immune-cell-associated abundance, particularly among monocyte, basophil, and B-cell annotations, although several genes are not detected in immune cells. The blood-microparticle signal (GO:CC blood microparticle; q_global = 1.81e-05) and the broad extracellular-space signal (GO:CC extracellular space; q_global = 0.0321) therefore warrant caution: the shared lung–testis module may partly reflect plasma carryover, vascular content, stromal content, or shared sample-associated cell types rather than a common tissue-cell program. HPA protein detection is limited in both tissues, so absence of tissue detection should not be treated as evidence that the genes are biologically irrelevant.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 1.81e-05 | A2M, ALB, C3, CFB, CP, GC, ITIH4, TF, VTN |
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 0.0144 | A2M, C3, CFB, SERPINA1, VTN |
| GO:CC Golgi lumen | 0.0205 | DCN, LUM, PRELP, VTN |
| GO:CC extracellular space | 0.0321 | A2M, ALB, C3, CFB, CP, DCN, FBLN1, GC, ITIH4, LUM, MYH11, PRELP, SERPINA1, TF, VTN |
| GO:MF extracellular matrix structural constituent conferring compression resistance | 0.0424 | DCN, LUM, PRELP |

### STRING and hu.MAP

STRING supports a well-known extracellular protein network rather than an isolated set of genes. Strong relationships connect ALB, C3, SERPINA1, VTN, CP, A2M, TF, GC, CFB, and ITIH4, while DCN, LUM, FBLN1, and PRELP form a matrix-associated branch. The STRING supplementary annotations for secretion, signal peptides, glycoproteins, extracellular region, blood microparticles, and plasma-protein studies are concordant with the primary GO/KEGG interpretation, but their FDR values are not global module significance and are used only as supporting evidence. hu.MAP independently places the circulating-protein subset in several overlapping complexes containing complement, transport, protease-regulatory, and plasma proteins. The repeated presence of CP, CFB, SERPINA1, A2M, C3, ALB, GC, TF, and ITIH4 across these complexes indicates that the module recovers established biochemical and proteomic associations. In contrast, LUM, DCN, FBLN1, PRELP, MYH11, TNS1, and IGKC have little or no recorded complex support in the supplied hu.MAP or STRING relationships, so their co-abundance may reflect extracellular context, tissue composition, or dataset-specific coordination rather than a documented physical complex.

**STRING interactions (score >= 0.7)**: 31 of 136 gene pairs: A2M–ALB (0.98); A2M–CFB (0.726); A2M–CP (0.889); A2M–SERPINA1 (0.98); A2M–TF (0.82); ALB–C3 (0.959); ALB–CP (0.936); ALB–GC (0.98); ALB–ITIH4 (0.765); ALB–LUM (0.737); ALB–SERPINA1 (0.998); ALB–TF (0.9); ALB–VTN (0.988); C3–CFB (0.999); C3–CP (0.751); C3–GC (0.768); C3–ITIH4 (0.745); C3–SERPINA1 (0.859); C3–VTN (0.79); CFB–SERPINA1 (0.725); CP–SERPINA1 (0.944); CP–TF (0.835); DCN–FBLN1 (0.806); DCN–LUM (0.978); DCN–VTN (0.945); GC–SERPINA1 (0.876); GC–TF (0.811); ITIH4–VTN (0.846); LUM–PRELP (0.771); SERPINA1–TF (0.848); SERPINA1–VTN (0.718)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Secreted (FDR = 3.73e-10, 14 genes); PMID (2016) Glycoproteomic Analysis of Malignant Ovarian Cancer Ascites Fluid Identifies Unusual Glycopeptides. (FDR = 2.25e-09, 11 genes); Keyword Signal (FDR = 2.83e-08, 14 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 2.89e-08, 12 genes); Keyword Glycoprotein (FDR = 1.04e-07, 14 genes); PMID (2019) Label-Free Proteomics Revealed Oxidative Stress and Inflammation as Factors That Enhance Chemoresistance in Luminal Breast Cancer. (FDR = 1.51e-07, 9 genes); Keyword Disulfide bond (FDR = 2.74e-07, 13 genes); PMID (2022) The Implant Proteome-The Right Surgical Glue to Fix Titanium Implants In Situ. (FDR = 8.32e-07, 9 genes); PMID (2016) Erythrocyte membrane in type 2 diabetes mellitus. (FDR = 8.32e-07, 8 genes); Component Blood microparticle (FDR = 1.39e-06, 9 genes); COMPARTMENTS Blood microparticle (FDR = 1.46e-06, 9 genes); PMID (2022) Plasma proteins from several components of the immune system differentiate chronic widespread pain patients from healthy controls - an exploratory case-control study combining targeted and non-targeted protein identification. (FDR = 1.82e-06, 8 genes); PMID (2012) Assessment of two immunodepletion methods: off-target effects and variations in immunodepletion efficiency may confound plasma proteomics. (FDR = 2.15e-06, 8 genes); COMPARTMENTS Extracellular region (FDR = 2.49e-06, 14 genes); PMID (2017) Lectins: an effective tool for screening of potential cancer biomarkers. (FDR = 2.55e-06, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (CP, CFB, SERPINA1, A2M, C3, ALB, GC, TF, ITIH4; 9/64); huMAP3_10678.1 (CP, CFB, SERPINA1, A2M, C3, ALB, GC, TF, ITIH4; 9/71); huMAP3_09531.1 (CP, CFB, SERPINA1, A2M, C3, ALB, TF, ITIH4; 8/47); huMAP3_10101.1 (CP, CFB, SERPINA1, A2M, C3, ALB, TF, ITIH4; 8/49); huMAP3_08395.1 (CP, CFB, SERPINA1, A2M, C3, ALB, TF; 7/43); huMAP3_09434.1 (SERPINA1, C3, ALB, GC, TF, ITIH4; 6/33); huMAP3_07432.1 (CP, SERPINA1, C3, ALB, TF; 5/18); huMAP3_07265.1 (CP, SERPINA1, A2M, ALB, TF; 5/20); huMAP3_08700.1 (CP, SERPINA1, ALB; 3/11); huMAP3_08224.1 (C3, GC, TF; 3/21); huMAP3_09273.1 (CP, CFB, A2M; 3/28); huMAP3_02242.1 (C3, TF; 2/9); huMAP3_08796.1 (CFB, ITIH4; 2/15); huMAP3_09832.1 (CFB, ITIH4; 2/18); huMAP3_07701.1 (CFB, A2M; 2/22)

### Novelty

This is not a new discovery of the underlying biological functions or of most relationships: complement, plasma transport, acute-phase proteins, extracellular matrix proteins, and their associations are already represented in STRING and hu.MAP. The lung–testis co-abundance module itself could still be a new computational observation, but the supplied evidence cannot establish that it is novel or tissue-intrinsic. Its strong liver, plasma, blood-microparticle, and extracellular-matrix signatures make a composition-driven explanation particularly plausible. Absence of STRING or hu.MAP support for some module members does not demonstrate novelty, because co-abundance can arise from shared regulation, secretion, cell mixture, sample handling, or indirect biological coupling. A novelty claim would require comparison with prior tissue co-abundance modules and validation in independent lung and testis cohorts with control for plasma and cell-type composition.

**Hypothesis.** Hypothesis: the module represents a shared extracellular vascular–stromal milieu in lung and testis in which liver-derived plasma proteins enter or remain associated with tissue samples, while complement and protease-regulatory proteins interact with matrix and vascular components. C3 and CFB could provide complement activity, A2M and SERPINA1 could constrain proteolysis and inflammation, and VTN, DCN, LUM, FBLN1, and PRELP could organize adhesive and mechanically resilient extracellular matrix. GC and TF could contribute vitamin D and iron transport, respectively. This model predicts that module abundance will track plasma contamination or vascular/stromal content and will weaken after adjustment for circulating protein abundance and cell-type composition. It also predicts that genuine tissue-localized biology should be supported by spatial or cellular measurements showing coordinated expression in vascular, stromal, smooth-muscle, or resident secretory compartments.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): CP (0.86), CFB (0.82); STRING partners: ALB (0.959), CFB (0.999), CP (0.751), GC (0.768), ITIH4 (0.745), SERPINA1 (0.859), VTN (0.79)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_09434.1, huMAP3_07432.1, huMAP3_08224.1, huMAP3_02242.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a central network member of the complement-associated portion and is present in the primary blood-microparticle, complement/coagulation, and extracellular-space terms (GO:CC blood microparticle; q_global = 1.81e-05), (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0144), and (GO:CC extracellular space; q_global = 0.0321). It has strong STRING relationships with CFB, ALB, SERPINA1, GC, ITIH4, CP, and VTN, and it recurs across many hu.MAP complexes. Its established function is central complement activation, with processed products that participate in inflammation and antimicrobial activity. It also has substantial literature and disease associations involving complement deficiency, complement glomerulopathy, and atypical hemolytic-uremic syndromes.
- **Conclusion**: Established evidence supports C3 as a biochemical anchor of the circulating complement component. Its co-abundance here is more likely to reflect extracellular or plasma-associated complement biology than a lung–testis-specific mechanism. It is a plausible mechanistic contributor, but the module alone does not demonstrate local complement activation in either tissue.

#### A2M

- **Related proteins** (co-abundance neighbors): GC (0.81); STRING partners: ALB (0.98), CFB (0.726), CP (0.889), SERPINA1 (0.98), TF (0.82)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_07265.1, huMAP3_09273.1, huMAP3_07701.1
- **Function (MyGene.info)**: alpha-2-macroglobulin. The protein encoded by this gene is a protease inhibitor and cytokine transporter. It uses a bait-and-trap mechanism to inhibit a broad spectrum of proteases, including trypsin, thrombin and collagenase. It can also inhibit inflammatory cytokines, and it thus disrupts inflammatory cascades. Mutations in this gene are a cause of alpha-2-macroglobulin deficiency. This gene is implicated in Alzheimer…
- **Diseases (Open Targets)**: myopia (0.206); refractive error (0.151); primary angle-closure glaucoma (0.148); Abnormality of refraction (0.144); Aganglionic megacolon (0.118)
- **Europe PMC papers**: 5133
- **Why important**: A2M links the module to broad extracellular protease and inflammatory regulation. It contributes to the primary complement/coagulation and extracellular-space terms (GO:CC blood microparticle; q_global = 1.81e-05), (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0144), and (GO:CC extracellular space; q_global = 0.0321), has strong STRING links to ALB, SERPINA1, CP, TF, and CFB, and occurs in several hu.MAP complexes. HPA marks it as tissue-enhanced in lung and detects it in both tissues, while its established function includes broad protease inhibition and cytokine transport. This makes it especially informative for distinguishing a circulating regulatory signal from a purely liver-derived abundance pattern.
- **Conclusion**: Established evidence supports A2M as a plausible extracellular regulator connecting proteolysis, inflammation, and complement control. Its lung enrichment is compatible with a local contribution, but the module cannot determine whether the measured protein is produced locally or arrives through blood. A local lung–testis mechanism remains a hypothesis.

#### ALB

- **Related proteins** (co-abundance neighbors): TF (0.83); STRING partners: A2M (0.98), C3 (0.959), CP (0.936), GC (0.98), ITIH4 (0.765), LUM (0.737), SERPINA1 (0.998), TF (0.9), VTN (0.988)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_09434.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_08700.1
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB is a highly abundant liver-derived plasma protein and a prominent STRING hub connecting several circulating module members, including C3, CP, GC, SERPINA1, TF, ITIH4, and VTN. It contributes to (GO:CC blood microparticle; q_global = 1.81e-05) and (GO:CC extracellular space; q_global = 0.0321) and appears across multiple hu.MAP plasma-protein complexes. Its established roles include plasma colloid-osmotic regulation and broad transport of endogenous and exogenous molecules. Its very strong plasma character makes it biologically informative but also an important possible sample-composition indicator.
- **Conclusion**: Established evidence supports ALB as evidence for a plasma-associated module rather than as evidence of a specialized shared lung–testis pathway. ALB may help explain coordinated abundance of other circulating proteins, but it should not be interpreted as proof of physical interaction or local tissue synthesis.

#### GC

- **Related proteins** (co-abundance neighbors): CP (0.88), TF (0.88), IGKC (0.84), SERPINA1 (0.83), A2M (0.81); STRING partners: ALB (0.98), C3 (0.768), SERPINA1 (0.876), TF (0.811)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09434.1, huMAP3_08224.1
- **Function (MyGene.info)**: GC vitamin D binding protein. The protein encoded by this gene belongs to the albumin gene family. It is a multifunctional protein found in plasma, ascitic fluid, cerebrospinal fluid and on the surface of many cell types. It binds to vitamin D and its plasma metabolites and transports them to target tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq,…
- **Diseases (Open Targets)**: vitamin D deficiency (0.574); vitamin deficiency (0.552); chronic obstructive pulmonary disease (0.499); squamous cell carcinoma (0.339); central nervous system cancer (0.334)
- **Europe PMC papers**: 363974
- **Why important**: GC has the strongest weighted network position in the supplied module and connects CP, TF, SERPINA1, A2M, and an immunoglobulin-associated edge. It contributes to (GO:CC blood microparticle; q_global = 1.81e-05) and (GO:CC extracellular space; q_global = 0.0321), is present in several hu.MAP complexes, and is annotated as a liver-enriched secreted blood protein detected in both tissues. Its established function is vitamin D and vitamin D metabolite transport, with additional associations to nutrient and vitamin metabolism. Its extensive literature and disease links provide a biologically interpretable transport axis within the module.
- **Conclusion**: Established evidence supports GC as a central circulating transport marker and a strong indicator of liver/plasma contribution. A coordinated vitamin D transport mechanism in the two tissues is possible, but it is not established by the co-abundance module or by the supplied annotations.

#### LUM

- **Related proteins** (co-abundance neighbors): DCN (0.96), MYH11 (0.80), FBLN1 (0.80); STRING partners: ALB (0.737), DCN (0.978), PRELP (0.771)
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lumican. This gene encodes a member of the small leucine-rich proteoglycan (SLRP) family that includes decorin, biglycan, fibromodulin, keratocan, epiphycan, and osteoglycin. In these bifunctional molecules, the protein moiety binds collagen fibrils and the highly charged hydrophilic glycosaminoglycans regulate interfibrillar spacings. Lumican is the major keratan sulfate proteoglycan of the cornea but is …
- **Diseases (Open Targets)**: lumbar disc herniation (0.359); Dupuytren Contracture (0.357); fibroblastic disorder (0.357); Hallux valgus (0.357); preeclampsia (0.154)
- **Europe PMC papers**: 14825
- **Why important**: LUM anchors the matrix-associated branch through its strong relationship with DCN and additional links to PRELP and ALB. It contributes to the primary Golgi-lumen, extracellular-space, and compression-resistant matrix terms (GO:CC Golgi lumen; q_global = 0.0205), (GO:CC extracellular space; q_global = 0.0321), and (GO:MF extracellular matrix structural constituent conferring compression resistance; q_global = 0.0424). Its established function involves collagen-fibril organization and regulation of the spacing and properties of interstitial collagen matrices. HPA associates it with stromal cells and extracellular-matrix secretion, while its literature and disease associations support relevance to connective-tissue remodeling.
- **Conclusion**: Established evidence supports LUM as a genuine extracellular-matrix component rather than merely a plasma marker. Its co-abundance with the circulating branch suggests coupling between matrix or stromal content and extracellular fluid composition, but whether that coupling is specific to lung and testis remains unresolved.

#### TNS1

- **Related proteins** (co-abundance neighbors): PRELP (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Focal adhesion sites; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tensin 1. The protein encoded by this gene localizes to focal adhesions, regions of the plasma membrane where the cell attaches to the extracellular matrix. This protein crosslinks actin filaments and contains a Src homology 2 (SH2) domain, which is often found in molecules involved in signal transduction. This protein is a substrate of calpain II. Alternative splicing results in multiple transcript variant…
- **Diseases (Open Targets)**: coronary artery disorder (0.555); chronic obstructive pulmonary disease (0.550); myocardial infarction (0.513); aortic stenosis (0.462); breast cancer (0.443)
- **Europe PMC papers**: 1434
- **Why important**: TNS1 is important because it provides a cellular structural link at the edge of the matrix branch. It is connected to PRELP in the module, is localized to focal adhesions, and is associated with cell–matrix adhesion and fibroblast migration. HPA detects it in both lung and testis and associates it with pericytes, peritubular myoid cells, alveolar cells, adipocytes, and Leydig cells. Unlike the secreted proteins, TNS1 is not a secreted factor and lacks supplied STRING or hu.MAP support, making it a useful marker of a possible tissue-cell or stromal component.
- **Conclusion**: Established evidence supports TNS1 as a focal-adhesion and cell–matrix-adhesion protein with relevant cellular distributions in both tissues. Its edge with PRELP suggests a possible structural interface, but the absence of independent complex support means that direct functional coupling within this module is only a hypothesis.

## Module 1

**Tissue pair**: lung and testis  
**Genes (8)**: AAAS, CPSF6, NUP155, NUP188, NUP205, NUP88, NUP93, SF3A1

### Function

The module is best interpreted as a nuclear pore and RNA trafficking module. The primary evidence is exceptionally coherent: globally corrected terms identify nucleic acid transport, RNA transport, RNA localization, the nuclear pore, nucleocytoplasmic transport, mRNA transport, nuclear pore structure, RNA export, nuclear export, and the nucleocytoplasmic transport KEGG pathway (GO:BP nucleic acid transport; q_global = 3.66e-07) through (GO:BP mRNA export from nucleus; q_global = 0.0312). Most of the module is composed of nucleoporins, with CPSF6 linking the pore machinery to messenger RNA three-prime-end processing and export, and SF3A1 linking it to spliceosomal RNA processing. The ALS KEGG term (KEGG Amyotrophic lateral sclerosis - Homo sapiens (human); q_global = 0.0325) should not be interpreted as evidence that the module is an ALS-specific module; it is more plausibly a consequence of shared nuclear transport biology. The network therefore represents coordinated expression of structural nuclear pore components together with RNA-processing factors.

**Cell composition.** This is not a plasma-protein, secreted-protein, or blood-cell-enriched module. HPA reports no secreted genes and low immune-cell specificity for every gene. Most genes have low tissue specificity, while NUP155 is tissue-enriched in testis. Several genes show cell-type enhancement in reproductive or developmental cell types, including late spermatids, oocytes, Sertoli cells, and cytotrophoblasts, but the pattern is not restricted to one cell type. Protein detection is broader in testis than lung, and several members are detected in both tissues. Thus, the shared signal is more consistent with conserved intracellular nuclear transport biology, possibly influenced by reproductive-cell representation in testis, than with blood contamination.

**GO/KEGG enrichment**: 22 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP nucleic acid transport | 3.66e-07 | AAAS, CPSF6, NUP155, NUP188, NUP205, NUP88, NUP93 |
| GO:BP RNA transport | 3.66e-07 | AAAS, CPSF6, NUP155, NUP188, NUP205, NUP88, NUP93 |
| GO:BP establishment of RNA localization | 3.66e-07 | AAAS, CPSF6, NUP155, NUP188, NUP205, NUP88, NUP93 |
| GO:BP nucleobase-containing compound transport | 7.42e-07 | AAAS, CPSF6, NUP155, NUP188, NUP205, NUP88, NUP93 |
| GO:BP RNA localization | 9.63e-07 | AAAS, CPSF6, NUP155, NUP188, NUP205, NUP88, NUP93 |
| GO:CC nuclear pore | 4.64e-06 | AAAS, NUP155, NUP188, NUP205, NUP88, NUP93 |
| GO:BP nucleocytoplasmic transport | 7.54e-06 | AAAS, CPSF6, NUP155, NUP188, NUP205, NUP88, NUP93 |
| GO:BP nuclear transport | 7.54e-06 | AAAS, CPSF6, NUP155, NUP188, NUP205, NUP88, NUP93 |
| GO:CC nuclear protein-containing complex | 8.21e-06 | AAAS, CPSF6, NUP155, NUP188, NUP205, NUP88, NUP93, SF3A1 |
| GO:BP mRNA transport | 9.27e-06 | AAAS, NUP155, NUP188, NUP205, NUP88, NUP93 |
| GO:MF structural constituent of nuclear pore | 1.15e-05 | NUP155, NUP188, NUP205, NUP88, NUP93 |
| KEGG Nucleocytoplasmic transport - Homo sapiens (human) | 1.96e-05 | AAAS, NUP155, NUP188, NUP205, NUP88, NUP93 |
| GO:BP RNA export from nucleus | 5.75e-05 | CPSF6, NUP155, NUP188, NUP88, NUP93 |
| GO:BP nitrogen compound transport | 6.51e-05 | AAAS, CPSF6, NUP155, NUP188, NUP205, NUP88, NUP93 |
| GO:CC nuclear pore inner ring | 0.000359 | NUP155, NUP188, NUP205 |

### STRING and hu.MAP

STRING supports a known physical and functional core consisting of AAAS, NUP155, NUP188, NUP205, NUP88, and NUP93. These nucleoporin pairs have strong STRING relationships, and the STRING enrichment for capped pre-mRNA processing, mature messenger RNA transport, ribonucleoprotein transport, antiviral nuclear trafficking, and snRNP assembly (STRING RCTM Processing of Capped Intron-Containing Pre-mRNA; within-query FDR = 6.49e-09) through (STRING RCTM snRNP Assembly; within-query FDR = 1.33e-07) is concordant supplementary evidence. SF3A1 and CPSF6 have no listed STRING interactions within this query, so their module links should be interpreted as co-abundance relationships rather than established STRING relationships. hu.MAP independently places several module members in complexes containing NUP188, NUP93, NUP205, NUP155, NUP88, and AAAS (hu.MAP huMAP3_05673.1) through (hu.MAP huMAP3_09825.1). These complexes contain additional nuclear pore, transport, export, and Ran-pathway proteins, showing that the module captures portions of larger known assemblies rather than a complete standalone complex. The network is therefore strongly anchored in established nuclear pore architecture, with RNA-processing genes forming peripheral functional links.

**STRING interactions (score >= 0.7)**: 15 of 28 gene pairs: AAAS–NUP155 (0.989); AAAS–NUP188 (0.981); AAAS–NUP205 (0.986); AAAS–NUP88 (0.994); AAAS–NUP93 (0.983); NUP155–NUP188 (0.999); NUP155–NUP205 (0.999); NUP155–NUP88 (0.995); NUP155–NUP93 (0.999); NUP188–NUP205 (0.999); NUP188–NUP88 (0.992); NUP188–NUP93 (0.999); NUP205–NUP88 (0.995); NUP205–NUP93 (0.999); NUP88–NUP93 (0.995)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Processing of Capped Intron-Containing Pre-mRNA (FDR = 6.49e-09, 8 genes); RCTM ISG15 antiviral mechanism (FDR = 1.33e-07, 6 genes); RCTM Transport of the SLBP independent Mature mRNA (FDR = 1.33e-07, 6 genes); RCTM Transport of the SLBP Dependant Mature mRNA (FDR = 1.33e-07, 6 genes); RCTM Transport of Mature mRNA Derived from an Intronless Transcript (FDR = 1.33e-07, 6 genes); RCTM Transport of Mature mRNA derived from an Intron-Containing Transcript (FDR = 1.33e-07, 6 genes); RCTM Rev-mediated nuclear export of HIV RNA (FDR = 1.33e-07, 6 genes); RCTM Transport of Ribonucleoproteins into the Host Nucleus (FDR = 1.33e-07, 6 genes); RCTM NS1 Mediated Effects on Host Pathways (FDR = 1.33e-07, 6 genes); RCTM Viral Messenger RNA Synthesis (FDR = 1.33e-07, 6 genes); RCTM NEP/NS2 Interacts with the Cellular Export Machinery (FDR = 1.33e-07, 6 genes); RCTM Regulation of Glucokinase by Glucokinase Regulatory Protein (FDR = 1.33e-07, 6 genes); RCTM Nuclear import of Rev protein (FDR = 1.33e-07, 6 genes); RCTM Vpr-mediated nuclear import of PICs (FDR = 1.33e-07, 6 genes); RCTM snRNP Assembly (FDR = 1.33e-07, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05673.1 (NUP188, NUP93, NUP205; 3/11); huMAP3_12581.1 (NUP155, NUP88, AAAS; 3/58); huMAP3_07789.1 (NUP93, NUP205; 2/7); huMAP3_07492.1 (NUP188, AAAS; 2/10); huMAP3_08489.1 (NUP188, AAAS; 2/10); huMAP3_09710.1 (NUP188, AAAS; 2/13); huMAP3_09042.1 (NUP93, NUP205; 2/26); huMAP3_09825.1 (NUP188, AAAS; 2/27)

### Novelty

The biological function is not a new molecular mechanism: the nucleoporin relationships and their roles in nuclear transport are already represented by STRING and hu.MAP, and the individual gene annotations are established. The potentially novel result is the tissue-pair co-abundance observation that this particular subset of nuclear pore and RNA-processing genes is conserved between lung and testis. That claim is limited by the supplied evidence: the fact sheet does not provide comparison against published co-abundance modules, independent cohorts, preservation statistics, or experimental validation. Therefore this should be described as a potentially interesting tissue-shared co-abundance pattern, not as a definitively new complex or pathway. Absence of SF3A1 or CPSF6 from the listed STRING and hu.MAP relationships does not establish novelty.

**Hypothesis.** Hypothesis: the module reflects coordinated maintenance of nuclear pore capacity and messenger RNA handling in cells that require sustained transcriptional output or specialized differentiation. In lung and testis, shared regulation of nucleoporin abundance could support transport through the nuclear envelope, while CPSF6 and SF3A1 couple export competence to messenger RNA three-prime-end processing and spliceosomal maturation. The reproductive-cell enrichment seen for several genes may indicate that this program is especially visible in spermatogenic or germ-cell-associated populations, but this remains a hypothesis requiring cell-resolved and perturbation-based testing.

### Important genes

#### NUP93

- **Related proteins** (co-abundance neighbors): SF3A1 (0.90), NUP155 (0.86), NUP205 (0.83), CPSF6 (0.81); STRING partners: AAAS (0.983), NUP155 (0.999), NUP188 (0.999), NUP205 (0.999), NUP88 (0.995)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_05673.1, huMAP3_07789.1, huMAP3_09042.1
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 is the strongest network hub in the module and connects SF3A1 and CPSF6 with several core nucleoporins. It appears across nearly all primary GO and KEGG terms, including nuclear pore structure, RNA transport, RNA export, and nucleocytoplasmic transport (GO:BP nucleic acid transport; q_global = 3.66e-07) through (KEGG Amyotrophic lateral sclerosis - Homo sapiens (human); q_global = 0.0325). It is represented in several hu.MAP complexes (hu.MAP huMAP3_05673.1), (hu.MAP huMAP3_07789.1), and (hu.MAP huMAP3_09042.1), has a large literature base, and has disease associations involving nephrotic syndrome and viral infection.
- **Conclusion**: Established evidence supports NUP93 as a central structural and transport component of the module. Its network position makes it a plausible coordinator of the nucleoporin and RNA-processing branches, but the co-abundance data alone do not establish that it regulates the other genes.

#### NUP155

- **Related proteins** (co-abundance neighbors): AAAS (0.87), NUP93 (0.86), NUP205 (0.84); STRING partners: AAAS (0.989), NUP188 (0.999), NUP205 (0.999), NUP88 (0.995), NUP93 (0.999)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 155. Nucleoporins are proteins that play an important role in the assembly and functioning of the nuclear pore complex (NPC) which regulates the movement of macromolecules across the nuclear envelope (NE). The protein encoded by this gene plays a role in the fusion of NE vesicles and formation of the double membrane NE. The protein may also be involved in cardiac physiology and may be associated with t…
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); atrial fibrillation (0.470); familial atrial fibrillation (0.390)
- **Europe PMC papers**: 944
- **Why important**: NUP155 has strong connectivity to the principal nucleoporin core and participates in every primary enrichment term listed for the module. It is associated with the nuclear pore inner ring (GO:CC nuclear pore inner ring; q_global = 0.000359), nuclear envelope biology, RNA export, and protein import. HPA identifies it as testis-enriched and enhanced in late spermatids, making it especially informative for interpreting the lung-testis sharing. It is also represented in hu.MAP complex C2 and has disease associations involving atrial fibrillation and nephrotic or viral disease contexts.
- **Conclusion**: Established evidence supports NUP155 as a structural nuclear-envelope and nuclear-pore component with a notable testis expression feature. Its testis enrichment may contribute to the tissue-pair pattern, but it does not by itself demonstrate a testis-specific mechanism or explain the lung signal.

#### NUP205

- **Related proteins** (co-abundance neighbors): NUP155 (0.84), NUP93 (0.83), NUP188 (0.83); STRING partners: AAAS (0.986), NUP155 (0.999), NUP188 (0.999), NUP88 (0.995), NUP93 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05673.1, huMAP3_07789.1, huMAP3_09042.1
- **Function (MyGene.info)**: nucleoporin 205. This gene encodes a nucleoporin, which is a subunit of the nuclear pore complex that functions in active transport of proteins, RNAs and ribonucleoprotein particles between the nucleus and cytoplasm. Mutations in this gene are associated with steroid-resistant nephrotic syndrome. [provided by RefSeq, Jul 2016].
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); familial idiopathic steroid-resistant nephrotic syndrome (0.528); viral infectious disease (0.527); lysosomal storage disease (0.462)
- **Europe PMC papers**: 729
- **Why important**: NUP205 is embedded in the core nucleoporin network and connects NUP155, NUP93, and NUP188. It contributes to the primary nuclear pore, nucleocytoplasmic transport, RNA transport, and inner-ring terms (GO:BP nucleic acid transport; q_global = 3.66e-07) through (KEGG Amyotrophic lateral sclerosis - Homo sapiens (human); q_global = 0.0325), and it appears in hu.MAP complexes C1, C3, and C7. HPA reports enhancement in Sertoli cells. Its established association with steroid-resistant nephrotic syndrome adds disease relevance to a gene whose primary role is nuclear transport.
- **Conclusion**: Established evidence supports NUP205 as a core nuclear pore assembly and transport component. Sertoli-cell enhancement makes it a useful candidate for testing reproductive-cell contributions, but the module does not establish that Sertoli cells generate the shared signal.

#### AAAS

- **Related proteins** (co-abundance neighbors): NUP155 (0.87); STRING partners: NUP155 (0.989), NUP188 (0.981), NUP205 (0.986), NUP88 (0.994), NUP93 (0.983)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_12581.1, huMAP3_07492.1, huMAP3_08489.1, huMAP3_09710.1, huMAP3_09825.1
- **Function (MyGene.info)**: aladin WD repeat nucleoporin. The protein encoded by this gene is a member of the WD-repeat family of regulatory proteins and may be involved in normal development of the peripheral and central nervous system. The encoded protein is part of the nuclear pore complex and is anchored there by NDC1. Defects in this gene are a cause of achalasia-addisonianism-alacrima syndrome (AAAS), also called triple-A syndrome or Allgrove syndr…
- **Diseases (Open Targets)**: triple-A syndrome (0.838); HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); hereditary disease (0.489)
- **Europe PMC papers**: 9330
- **Why important**: AAAS connects to the principal nucleoporin group in STRING and is represented in multiple hu.MAP complexes (hu.MAP huMAP3_12581.1) and (hu.MAP huMAP3_07492.1) through (hu.MAP huMAP3_09825.1). It contributes to the globally corrected transport terms (GO:BP nucleic acid transport; q_global = 3.66e-07) through (GO:BP import into nucleus; q_global = 0.0218) and has a well-established role as an aladin WD-repeat nucleoporin. Its association with triple-A syndrome gives it a strong disease anchor, while its high literature volume makes it an important interpretive gene despite its peripheral position in this particular co-abundance graph.
- **Conclusion**: Established evidence supports AAAS as a nuclear pore-associated regulator of nucleocytoplasmic transport. Its lower module connectivity than the central nucleoporins suggests that it may mark a functional sub-branch rather than control the entire module.

#### CPSF6

- **Related proteins** (co-abundance neighbors): NUP93 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cleavage and polyadenylation specific factor 6. The protein encoded by this gene is one subunit of a cleavage factor required for 3' RNA cleavage and polyadenylation processing. The interaction of the protein with the RNA is one of the earliest steps in the assembly of the 3' end processing complex and facilitates the recruitment of other processing factors. The cleavage factor complex is composed of four polypeptides. This gene encodes the 68k…
- **Diseases (Open Targets)**: cancer (0.579); neurodegenerative disease (0.463); Abnormality of the skeletal system (0.451); smoking initiation (0.424); leukemia (0.376)
- **Europe PMC papers**: 1665
- **Why important**: CPSF6 is the clearest bridge from nuclear pore biology to RNA maturation. It contributes to the primary RNA transport and RNA export terms (GO:BP nucleic acid transport; q_global = 3.66e-07) through (GO:BP RNA localization; q_global = 9.63e-07), (GO:BP nucleocytoplasmic transport; q_global = 7.54e-06) through (GO:BP mRNA transport; q_global = 9.27e-06), (GO:BP RNA export from nucleus; q_global = 5.75e-05), (GO:BP nitrogen compound transport; q_global = 6.51e-05), and (GO:BP nuclear export; q_global = 0.000374) through (GO:BP intracellular transport; q_global = 0.0202), and to the supplementary capped pre-mRNA processing term (STRING RCTM Processing of Capped Intron-Containing Pre-mRNA; within-query FDR = 6.49e-09). Its annotated role in cleavage and polyadenylation, alternative polyadenylation, and promotion of RNA export gives the module a mechanistic RNA-processing connection. It is linked to NUP93 in the module but lacks a listed STRING or hu.MAP relationship in this query.
- **Conclusion**: Established evidence supports CPSF6 as an RNA three-prime-end processing factor that functionally complements the nucleoporin core. Its module association may reflect coordinated RNA production and export, but a direct physical interaction with the listed nucleoporins is not established here.

## Module 2

**Tissue pair**: lung and testis  
**Genes (10)**: GOT2, ABHD10, TSFM, ETFA, IDH3A, L2HGDH, MAIP1, NDUFAF4, SUCLA2, TIMM50

### Function

This is a conserved mitochondrial co-abundance module. The primary evidence is (GO:CC mitochondrion; q_global = 0.00227), in which every module gene is assigned to the mitochondrion and the term passes global correction. The genes collectively cover mitochondrial matrix metabolism, the tricarboxylic acid cycle, amino-acid and fatty-acid metabolism, respiratory electron transport, complex I assembly, mitochondrial protein import, mitochondrial translation, and mitochondrial membrane or calcium-related functions. The STRING results support this interpretation through mitochondrial and transit-peptide annotations (5 supplementary STRING terms; within-query FDR 6.56e-06–0.0022), while the respiratory-chain and TCA-cycle signals are supplementary (STRING RCTM The citric acid (TCA) cycle and respiratory electron transport; within-query FDR = 0.0184), not globally corrected primary evidence. The network therefore most plausibly represents coordinated mitochondrial oxidative metabolism and mitochondrial proteostasis rather than a single narrowly defined enzyme complex.

**Cell composition.** The module is not dominated by secreted proteins, because the HPA summary reports no secreted genes. It is also not strongly blood-cell driven: most genes have low immune-cell specificity, with only isolated immune-cell enhancement for IDH3A and L2HGDH. Protein detection is present for nearly all genes in both lung and testis, supporting that the module is relevant to both tissues rather than being explained solely by missing protein measurements. The composition is a mixture of broadly expressed mitochondrial genes and genes enhanced in metabolically active or reproductive cell types. HPA links several genes to spermatids, including TIMM50, SUCLA2, and TSFM, and links others to hepatocytes, muscle, tongue, oocytes, or specialized epithelial cells. Thus, the shared signal could reflect conserved mitochondrial demand across lung and testis, with a possible contribution from germ-cell or other metabolically active cell populations. The tissue and cell-type annotations do not support a simple plasma-protein or blood-contamination explanation.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrion | 0.00227 | ABHD10, ETFA, GOT2, IDH3A, L2HGDH, MAIP1, NDUFAF4, SUCLA2, TIMM50, TSFM |

### STRING and hu.MAP

The network has a coherent mitochondrial annotation but limited prior physical-interaction support. The known high-confidence STRING relationships are GOT2-IDH3A and IDH3A-SUCLA2. These connect amino-acid and TCA-related metabolism and provide a biologically plausible core. The remaining co-abundances are not represented by high-confidence STRING partnerships in the supplied data, so they should not be treated as established direct physical interactions. No hu.MAP complex contains at least two module members. This pattern suggests that the co-abundance structure captures coordinated mitochondrial activity or shared regulation across several mitochondrial processes, rather than reproducing a known stable multiprotein complex. STRING functional enrichment is concordant with the mitochondrial interpretation (12 supplementary STRING terms; within-query FDR 6.56e-06–0.0272), but those terms remain supplementary and do not replace (GO:CC mitochondrion; q_global = 0.00227) as global enrichment evidence.

**STRING interactions (score >= 0.7)**: 2 of 45 gene pairs: GOT2–IDH3A (0.889); IDH3A–SUCLA2 (0.972)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Mitochondrion (FDR = 6.56e-06, 10 genes); Keyword Transit peptide (FDR = 6.56e-06, 9 genes); COMPARTMENTS Mitochondrion (FDR = 4.84e-05, 10 genes); Component Mitochondrion (FDR = 0.00027, 10 genes); Component Mitochondrial matrix (FDR = 0.0022, 7 genes); HPO Abnormality of acid-base homeostasis (FDR = 0.0062, 7 genes); RCTM The citric acid (TCA) cycle and respiratory electron transport (FDR = 0.0184, 5 genes); HPO Acidosis (FDR = 0.0211, 6 genes); HPO Abnormality of mitochondrial metabolism (FDR = 0.0211, 5 genes); HPO Decreased activity of mitochondrial respiratory chain (FDR = 0.0211, 4 genes); HPO Abnormal homeostasis (FDR = 0.0211, 8 genes); HPO Encephalopathy (FDR = 0.0272, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The general biological theme is not new: mitochondrial metabolism, protein import, translation, and respiratory-chain maintenance are established functions of the constituent genes. The potentially novel observation is the coordinated co-abundance of this particular gene set across lung and testis, especially the combination of metabolic enzymes, import and translation machinery, and less extensively characterized mitochondrial proteins. The absence of a matching hu.MAP complex and the sparse STRING interaction support argue against this being a previously defined canonical complex, but absence from those resources alone does not prove novelty. The most defensible conclusion is that this is a potentially novel cross-tissue co-abundance module built from largely established mitochondrial biology, requiring replication and independent functional validation before being called a new mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared mitochondrial capacity program that couples substrate oxidation and TCA-cycle flux with respiratory-chain assembly, mitochondrial protein import, mitochondrial translation, and maintenance of mitochondrial homeostasis. In testis, this program may support the high energetic and biosynthetic demands of spermatid differentiation; in lung, it may reflect metabolically active resident cell populations or conserved tissue-level mitochondrial requirements. The co-abundance of TIMM50, TSFM, NDUFAF4, and MAIP1 with metabolic enzymes suggests coordinated maintenance of mitochondrial proteome production and respiratory function, while the GOT2-IDH3A-SUCLA2 relationships provide a metabolic backbone. This is a mechanistic hypothesis, not evidence of direct interaction among all module members.

### Important genes

#### ABHD10

- **Related proteins** (co-abundance neighbors): TIMM50 (0.86), GOT2 (0.84), ETFA (0.84), NDUFAF4 (0.82), IDH3A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: abhydrolase domain containing 10, depalmitoylase. This gene encodes a mitochondrially-localized enzyme that acts in liver cells as a hydrolase. The encoded protein removes glucuronide from mycophenolic acid acyl-glucuronide. There is a pseudogene for this gene on chromosome 6. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2013].
- **Diseases (Open Targets)**: lacrimal apparatus disorder (0.110); atrial fibrillation (0.087); preeclampsia (0.081); adrenoleukodystrophy (0.067); external ear disorder (0.059)
- **Europe PMC papers**: 379
- **Why important**: ABHD10 is the strongest network hub in the module and connects multiple mitochondrial genes, including TIMM50, GOT2, ETFA, NDUFAF4, and IDH3A. It is mitochondrially localized and annotated as a depalmitoylase or hydrolase, with roles in protein depalmitoylation and metabolic processes. Its presence in the globally significant mitochondrial term (GO:CC mitochondrion; q_global = 0.00227) and several supplementary mitochondrial terms (5 supplementary STRING terms; within-query FDR 6.56e-06–0.0022) supports module membership. It has comparatively limited literature and no supplied STRING or hu.MAP relationships, making it an informative candidate for testing whether the module contains a less-characterized regulatory component.
- **Conclusion**: Established evidence supports ABHD10 as a mitochondrial, metabolically associated hub with protein-modifying activity. The hypothesis that it coordinates the other module genes or regulates mitochondrial respiratory function is plausible from its position but is not established by the supplied interaction resources.

#### IDH3A

- **Related proteins** (co-abundance neighbors): GOT2 (0.88), ABHD10 (0.81), TIMM50 (0.81), SUCLA2 (0.80); STRING partners: GOT2 (0.889), SUCLA2 (0.972)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: isocitrate dehydrogenase (NAD(+)) 3 catalytic subunit alpha. Isocitrate dehydrogenases catalyze the oxidative decarboxylation of isocitrate to 2-oxoglutarate. These enzymes belong to two distinct subclasses, one of which utilizes NAD(+) as the electron acceptor and the other NADP(+). Five isocitrate dehydrogenases have been reported: three NAD(+)-dependent isocitrate dehydrogenases, which localize to the mitochondrial matrix, and two NADP(+)-dependent isoci…
- **Diseases (Open Targets)**: retinitis pigmentosa 90 (0.791); retinitis pigmentosa (0.467); neurodegenerative disease (0.437); inherited retinal dystrophy (0.381); colorectal carcinoma (0.182)
- **Europe PMC papers**: 1497
- **Why important**: IDH3A is a central network node and participates in both supplied STRING links, connecting GOT2 and SUCLA2. It encodes the catalytic alpha subunit of mitochondrial NAD-dependent isocitrate dehydrogenase and is directly associated with the TCA-cycle and isocitrate metabolism annotations. It is included in (GO:CC mitochondrion; q_global = 0.00227) and in the mitochondrial and TCA-related supplementary evidence (5 supplementary STRING terms; within-query FDR 6.56e-06–0.0022), (STRING RCTM The citric acid (TCA) cycle and respiratory electron transport; within-query FDR = 0.0184), and (STRING HPO Abnormal homeostasis; within-query FDR = 0.0211). Its disease associations and relatively extensive literature make it a well-established metabolic anchor for interpreting the module.
- **Conclusion**: Established evidence identifies IDH3A as a mitochondrial TCA-cycle enzyme and a known interaction-supported core of the module. The cross-tissue co-abundance may indicate coordinated TCA activity, but the data do not establish that IDH3A regulates the other genes.

#### TIMM50

- **Related proteins** (co-abundance neighbors): SUCLA2 (0.88), ABHD10 (0.86), IDH3A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translocase of inner mitochondrial membrane 50. This gene encodes a subunit of the TIM23 inner mitochondrial membrane translocase complex. The encoded protein functions as the receptor subunit that recognizes the mitochondrial targeting signal, or presequence, on protein cargo that is destined for the mitochondrial inner membrane and matrix. This protein may also play a role in maintaining the membrane permeability barrier, and knockdown of thi…
- **Diseases (Open Targets)**: 3-methylglutaconic aciduria type 9 (0.773); neurodegenerative disease (0.519); Mitochondrial encephalopathy (0.425); hereditary disease (0.415); Epileptic encephalopathy (0.370)
- **Europe PMC papers**: 442
- **Why important**: TIMM50 is a network-connected mitochondrial protein-import factor and a receptor subunit of the TIM23 inner-membrane translocase. It is linked to mitochondrial matrix protein import, membrane organization, and cytochrome-c release. It is detected in both tissues, is cell-type enriched in late spermatids, and appears in (GO:CC mitochondrion; q_global = 0.00227) and the supplementary mitochondrial, transit-peptide, homeostasis, and respiratory-abnormality terms (4 supplementary STRING terms; within-query FDR 6.56e-06–0.00027) and (STRING HPO Abnormality of acid-base homeostasis; within-query FDR = 0.0062), (5 supplementary STRING terms; within-query FDR 0.0211–0.0272). Its disease associations provide functional relevance beyond metabolism alone.
- **Conclusion**: Established evidence supports TIMM50 as a mitochondrial import and membrane-homeostasis component that broadens the module beyond metabolic enzymes. Its co-abundance with respiratory and metabolic genes is consistent with coordinated mitochondrial maintenance, but a direct regulatory role in this module remains hypothetical.

#### SUCLA2

- **Related proteins** (co-abundance neighbors): TIMM50 (0.88), IDH3A (0.80); STRING partners: IDH3A (0.972)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase ADP-forming subunit beta. Succinyl-CoA synthetase (SCS) is a mitochondrial matrix enzyme that acts as a heterodimer, being composed of an invariant alpha subunit and a substrate-specific beta subunit. The protein encoded by this gene is an ATP-specific SCS beta subunit that dimerizes with the SCS alpha subunit to form SCS-A, an essential component of the tricarboxylic acid cycle. SCS-A hydrolyzes ATP to convert succinate t…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome, encephalomyopathic form with methylmalonic aciduria (0.816); mitochondrial DNA depletion syndrome, encephalomyopathic form (0.581); neurodegenerative disease (0.485); mitochondrial disease (0.374); disease of peritoneum (0.372)
- **Europe PMC papers**: 1440
- **Why important**: SUCLA2 is a mitochondrial matrix enzyme in the TCA cycle and forms the ATP-specific beta subunit of succinyl-CoA synthetase. It is one of the two STRING-supported interaction partners of IDH3A, is connected to TIMM50 in the co-abundance network, and appears across the mitochondrial, TCA, respiratory, and mitochondrial-disease supplementary signals (12 supplementary STRING terms; within-query FDR 6.56e-06–0.0272). Its established association with mitochondrial DNA depletion syndrome and substantial literature make it an important disease-linked metabolic representative.
- **Conclusion**: Established evidence supports SUCLA2 as a TCA-cycle and mitochondrial-energy component that helps define the metabolic backbone of the module. The network suggests coordination between TCA metabolism and mitochondrial maintenance, but it does not prove that SUCLA2 physically interacts with TIMM50 or the broader module.

#### NDUFAF4

- **Related proteins** (co-abundance neighbors): TSFM (0.82), ABHD10 (0.82), MAIP1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase complex assembly factor 4. NADH:ubiquinone oxidoreductase (complex I) catalyzes the transfer of electrons from NADH to ubiquinone (coenzyme Q) in the first step of the mitochondrial respiratory chain, resulting in the translocation of protons across the inner mitochondrial membrane. This gene encodes a complex I assembly factor. Mutations in this gene are a cause of mitochondrial complex I deficiency. [provided by RefSeq, O…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.714); type 2 diabetes mellitus (0.607); mitochondrial disease (0.597); diabetes mellitus (0.578); mitochondrial complex I deficiency, nuclear type 15 (0.568)
- **Europe PMC papers**: 378
- **Why important**: NDUFAF4 is a mitochondrial complex I assembly factor and connects in the module to TSFM, ABHD10, and MAIP1. It is included in (GO:CC mitochondrion; q_global = 0.00227) and in supplementary annotations concerning mitochondrial localization, respiratory electron transport, complex-I-related abnormalities, and mitochondrial metabolism (STRING Keyword Mitochondrion; within-query FDR = 6.56e-06), (STRING COMPARTMENTS Mitochondrion; within-query FDR = 4.84e-05), (STRING Component Mitochondrion; within-query FDR = 0.00027), and (7 supplementary STRING terms; within-query FDR 0.0062–0.0272). Its disease associations with complex I deficiency and mitochondrial disease make it a strong link between the module's metabolic genes and respiratory-chain biogenesis.
- **Conclusion**: Established evidence supports NDUFAF4 as a complex I assembly factor with disease-relevant mitochondrial function. Its position alongside mitochondrial translation and membrane-related genes supports a coordinated oxidative-phosphorylation maintenance hypothesis, but the supplied data do not establish direct physical interactions with those partners.

## Module 3

**Tissue pair**: lung and testis  
**Genes (21)**: ABCB7, ACSL3, AIFM1, HSPA5, GFM1, GARS1, GHDC, HACL2, HYOU1, ME3, PDIA4, PITRM1, SLC25A12, SDHA, SUPV3L1, DARS2, IARS2, THNSL1, TNPO1, TRAP1, UGGT1

### Function

The module is best interpreted as a conserved mitochondrial maintenance and proteostasis program with an associated endoplasmic-reticulum protein-folding arm. The primary globally corrected evidence supports mitochondrion (GO:CC mitochondrion; q_global = 0.00231), mitochondrial gene expression (GO:BP mitochondrial gene expression; q_global = 0.0202), nucleotide binding (GO:MF nucleotide binding; q_global = 0.0258), nucleoside-phosphate binding (GO:MF nucleoside phosphate binding; q_global = 0.0299), and protein folding (GO:BP protein folding; q_global = 0.04). The genes indicate coordinated mitochondrial translation, mitochondrial RNA handling, respiratory metabolism, metabolite transport, iron-sulfur and heme-related homeostasis, chaperoning, and quality control. The ER component is represented by HSPA5, HYOU1, PDIA4, and UGGT1, while TRAP1 links chaperoning with mitochondrial biology. The STRING annotations independently support mitochondrial localization and transit-peptide biology (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.00077), (STRING Keyword Mitochondrion; within-query FDR = 0.0012), and (STRING Keyword Transit peptide; within-query FDR = 0.0026), and support an ER protein-folding group (STRING NetworkNeighborAL Mixed, incl. Photodynamic therapy-induced unfolded protein response, and Protein disulfide isomerase activity; within-query FDR = 0.0491).

**Cell composition.** The module is predominantly intracellular and broadly expressed rather than a plasma-protein, secreted-protein, or blood-cell module. HPA reports low tissue specificity for most genes and low immune-cell specificity for nearly all genes. The secretome annotations are intracellular or membrane-associated rather than freely circulating. Protein detection is present in both lung and testis for nearly all genes with available data. Several genes are enhanced in specialized cell types, including spermatids, neurons, muscle-related cells, plasma cells, and other populations, so cell composition may contribute to the shared signal. However, the low immune-cell specificity argues against a predominantly blood-derived module. The most cautious interpretation is a broadly deployed mitochondrial and proteostasis program expressed by cell types represented in both tissues.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrion | 0.00231 | ABCB7, ACSL3, AIFM1, DARS2, GARS1, GFM1, HSPA5, HYOU1, IARS2, ME3, PITRM1, SDHA, SLC25A12, SUPV3L1, THNSL1, TRAP1 |
| GO:BP mitochondrial gene expression | 0.0202 | DARS2, GARS1, GFM1, IARS2, SUPV3L1 |
| GO:MF nucleotide binding | 0.0258 | ABCB7, ACSL3, AIFM1, DARS2, GARS1, GFM1, HACL2, HSPA5, HYOU1, IARS2, ME3, SDHA, SUPV3L1, TRAP1 |
| GO:MF nucleoside phosphate binding | 0.0299 | ABCB7, ACSL3, AIFM1, DARS2, GARS1, GFM1, HACL2, HSPA5, HYOU1, IARS2, ME3, SDHA, SUPV3L1, TRAP1 |
| GO:BP protein folding | 0.04 | AIFM1, HSPA5, HYOU1, PDIA4, TRAP1, UGGT1 |

### STRING and hu.MAP

STRING supports several established submodules rather than a dense physical interaction network across all genes. DARS2 connects with IARS2, and IARS2 connects with GARS1. HSPA5, HYOU1, PDIA4, and UGGT1 form a strongly supported protein-folding neighborhood, while HSPA5 also connects with TRAP1 and SDHA connects with TRAP1. These relationships support biological coherence but do not establish that every co-abundance edge is a direct physical interaction. hu.MAP supports a mitochondrial translation complex containing TRAP1, DARS2, GFM1, and IARS2 (hu.MAP huMAP3_13468.1), with DARS2, GFM1, and IARS2 recurring in another mitochondrial complex (hu.MAP huMAP3_10525.1). HSPA5 and HYOU1 occur together in a chaperone complex (hu.MAP huMAP3_07455.1). PDIA4 and HYOU1 recur in ER or protein-processing complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). ABCB7 with ACSL3 and HACL2 with ACSL3 recur in additional organelle or metabolic complexes (hu.MAP huMAP3_09592.1), (hu.MAP huMAP3_02404.1), (hu.MAP huMAP3_10153.1), and (hu.MAP huMAP3_08167.1). Thus, known complexes validate several module components, while the complete cross-compartment organization remains an inference from co-abundance.

**STRING interactions (score >= 0.7)**: 10 of 210 gene pairs: DARS2–IARS2 (0.895); GARS1–IARS2 (0.863); HSPA5–HYOU1 (0.999); HSPA5–PDIA4 (0.99); HSPA5–TRAP1 (0.787); HSPA5–UGGT1 (0.747); HYOU1–PDIA4 (0.997); HYOU1–UGGT1 (0.791); PDIA4–UGGT1 (0.84); SDHA–TRAP1 (0.78)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Mitochondrion (FDR = 0.00077, 14 genes); Keyword Mitochondrion (FDR = 0.0012, 13 genes); Keyword Transit peptide (FDR = 0.0026, 10 genes); Component Mitochondrion (FDR = 0.0066, 14 genes); NetworkNeighborAL Mixed, incl. Photodynamic therapy-induced unfolded protein response, and Protein disulfide isomerase activity (FDR = 0.0491, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (TRAP1, DARS2, GFM1, IARS2; 4/99); huMAP3_10525.1 (DARS2, GFM1, IARS2; 3/33); huMAP3_09592.1 (ABCB7, ACSL3, TNPO1; 3/95); huMAP3_02404.1 (HACL2, ACSL3; 2/4); huMAP3_07455.1 (HSPA5, HYOU1; 2/4); huMAP3_09668.1 (DARS2, IARS2; 2/8); huMAP3_10153.1 (HACL2, ACSL3; 2/10); huMAP3_08167.1 (ABCB7, ACSL3; 2/24); huMAP3_14442.1 (GARS1, TRAP1; 2/57); huMAP3_06775.1 (PDIA4, HYOU1; 2/60); huMAP3_09327.1 (PDIA4, HYOU1; 2/93)

### Novelty

This should not be presented as a wholly new molecular pathway. Mitochondrial translation, respiratory metabolism, mitochondrial RNA processing, mitochondrial chaperoning, ER protein folding, and glycoprotein quality control are established processes supported by the fact sheet. The potentially novel observation is their conserved co-abundance organization across lung and testis, especially the combination of mitochondrial maintenance genes with the HSPA5-HYOU1-PDIA4-UGGT1 proteostasis group. This is a systems-level novelty claim, not a claim that the individual interactions are newly discovered. Absence from STRING or hu.MAP does not establish novelty; poorly annotated genes and cross-group edges require experimental validation. The most defensible conclusion is a potentially novel tissue-shared co-abundance configuration assembled from largely established biological processes.

**Hypothesis.** Hypothesis: the module coordinates mitochondrial output with protein-quality control during metabolic, hypoxic, translational, or proteotoxic stress. Mitochondrial translation and RNA-processing factors may sustain synthesis and surveillance of mitochondrial proteins, while SDHA, ME3, SLC25A12, ACSL3, and ABCB7 support respiration, metabolite exchange, lipid handling, and metal or heme-related homeostasis. In parallel, HSPA5, HYOU1, PDIA4, and UGGT1 may limit accumulation of misfolded ER proteins. TRAP1 and AIFM1 may couple mitochondrial chaperoning to respiratory stress tolerance and apoptotic threshold. This hypothesis predicts coordinated responses between mitochondrial translation or respiratory perturbation and the ER chaperone arm, but it is not established by the co-abundance data alone.

### Important genes

#### IARS2

- **Related proteins** (co-abundance neighbors): PITRM1 (0.87), GFM1 (0.85), SDHA (0.84), DARS2 (0.82), TRAP1 (0.82), HYOU1 (0.81); STRING partners: DARS2 (0.895), GARS1 (0.863)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1, huMAP3_09668.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 2, mitochondrial. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Two forms of isoleucine-tRNA synthetase exist, a cytoplasmic form and a mitochondrial form. This gene encodes th…
- **Diseases (Open Targets)**: cataract-growth hormone deficiency-sensory neuropathy-sensorineural hearing loss-skeletal dysplasia syndrome (0.724); Leigh syndrome (0.563); hereditary disease (0.416); neurodegenerative disease (0.411); mitochondrial disease (0.374)
- **Europe PMC papers**: 411
- **Why important**: IARS2 is the highest-connectivity node and links PITRM1, GFM1, SDHA, DARS2, TRAP1, and HYOU1. It is a mitochondrial isoleucyl-tRNA synthetase and occurs in (GO:CC mitochondrion; q_global = 0.00231), (GO:BP mitochondrial gene expression; q_global = 0.0202), (GO:MF nucleotide binding; q_global = 0.0258), and (GO:MF nucleoside phosphate binding; q_global = 0.0299). Its relationships with DARS2 and GARS1 are supported by STRING, and it recurs in mitochondrial hu.MAP complexes (hu.MAP huMAP3_13468.1), (hu.MAP huMAP3_10525.1), and (hu.MAP huMAP3_09668.1). Its disease associations include Leigh syndrome, sensory neuropathy, hearing loss, and mitochondrial disease, with substantial literature support.
- **Conclusion**: Established conclusion: IARS2 is a central mitochondrial translation and network-integration gene. Hypothesis: its network position may couple mitochondrial translational demand to respiration and stress chaperoning.

#### HSPA5

- **Related proteins** (co-abundance neighbors): HYOU1 (0.87), ME3 (0.85), PDIA4 (0.83); STRING partners: HYOU1 (0.999), PDIA4 (0.99), TRAP1 (0.787), UGGT1 (0.747)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_07455.1
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is the principal ER chaperone node, linking HYOU1, PDIA4, ME3, and TRAP1. It occurs in (GO:CC mitochondrion; q_global = 0.00231), (GO:MF nucleotide binding; q_global = 0.0258), (GO:MF nucleoside phosphate binding; q_global = 0.0299), and (GO:BP protein folding; q_global = 0.04). Its STRING relationships with HYOU1, PDIA4, TRAP1, and UGGT1 and its hu.MAP association with HYOU1 (hu.MAP huMAP3_07455.1) support a coherent proteostasis group. HSPA5 is a master regulator of ER homeostasis and has extensive literature and disease-association support.
- **Conclusion**: Established conclusion: HSPA5 is a well-supported ER proteostasis hub and a plausible bridge to the mitochondrial arm. Hypothesis: HSPA5 abundance may transmit or report proteotoxic stress affecting both compartments.

#### TRAP1

- **Related proteins** (co-abundance neighbors): IARS2 (0.82), PITRM1 (0.82); STRING partners: HSPA5 (0.787), SDHA (0.78)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_14442.1
- **Function (MyGene.info)**: TNF receptor associated protein 1. This gene encodes a mitochondrial chaperone protein that is member of the heat shock protein 90 (HSP90) family. The encoded protein has ATPase activity and interacts with tumor necrosis factor type I. This protein may function in regulating cellular stress responses. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jan 2013].
- **Diseases (Open Targets)**: congenital anomaly of kidney and urinary tract (0.643); VACTERL/vater association (0.492); atrial fibrillation (0.467); neurodegenerative disease (0.372); Blindness (0.338)
- **Europe PMC papers**: 2586
- **Why important**: TRAP1 connects IARS2 and PITRM1 in the module and connects with HSPA5 and SDHA in STRING. It occurs in (GO:CC mitochondrion; q_global = 0.00231) and (GO:BP protein folding; q_global = 0.04), in mitochondrial STRING annotations (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.00077) through (STRING Component Mitochondrion; within-query FDR = 0.0066), and in hu.MAP complexes (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_14442.1). Its mitochondrial chaperone function, ATPase activity, respiratory regulation, oxidative-stress biology, and apoptosis-related functions make it a strong integrator. Its disease associations and literature support are substantial.
- **Conclusion**: Established conclusion: TRAP1 bridges mitochondrial translation, respiration, and protein folding. Hypothesis: TRAP1 may buffer mitochondrial proteotoxic stress while influencing respiratory activity and apoptotic susceptibility.

#### HYOU1

- **Related proteins** (co-abundance neighbors): HSPA5 (0.87), GARS1 (0.82), THNSL1 (0.81), IARS2 (0.81); STRING partners: HSPA5 (0.999), PDIA4 (0.997), UGGT1 (0.791)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07455.1, huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 links HSPA5, GARS1, THNSL1, and IARS2 and occurs in (GO:CC mitochondrion; q_global = 0.00231), (GO:MF nucleotide binding; q_global = 0.0258), (GO:MF nucleoside phosphate binding; q_global = 0.0299), and (GO:BP protein folding; q_global = 0.04). Its strong STRING relationships with HSPA5 and PDIA4, plus its link to UGGT1 (STRING NetworkNeighborAL Mixed, incl. Photodynamic therapy-induced unfolded protein response, and Protein disulfide isomerase activity; within-query FDR = 0.0491), support the ER protein-folding arm. It is a stress-inducible HSP seventy-family protein involved in ER folding, secretion, hypoxia, ischemia, and apoptosis-related biology. It is enhanced in spermatids and other specialized cell types and has broad literature and disease-association support.
- **Conclusion**: Established conclusion: HYOU1 is a strong marker of stress-adaptive proteostasis. Hypothesis: it may couple hypoxia or proteotoxic stress to the mitochondrial program, particularly in testicular germ-cell populations.

#### DARS2

- **Related proteins** (co-abundance neighbors): ACSL3 (0.83), IARS2 (0.82); STRING partners: IARS2 (0.895)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1, huMAP3_09668.1
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 2, mitochondrial. The protein encoded by this gene belongs to the class-II aminoacyl-tRNA synthetase family. It is a mitochondrial enzyme that specifically aminoacylates aspartyl-tRNA. Mutations in this gene are associated with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation (LBSL). [provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: leukoencephalopathy with brain stem and spinal cord involvement-high lactate syndrome (0.843); neurodegenerative disease (0.527); hereditary disease (0.518); hypertensive disorder (0.425); Cerebral cortical atrophy (0.425)
- **Europe PMC papers**: 796
- **Why important**: DARS2 is a mitochondrial aspartyl-tRNA synthetase connected to IARS2 and ACSL3. It occurs in (GO:CC mitochondrion; q_global = 0.00231), (GO:BP mitochondrial gene expression; q_global = 0.0202), (GO:MF nucleotide binding; q_global = 0.0258), and (GO:MF nucleoside phosphate binding; q_global = 0.0299) and recurs in hu.MAP mitochondrial complexes (hu.MAP huMAP3_13468.1), (hu.MAP huMAP3_10525.1), and (hu.MAP huMAP3_09668.1). Its disease associations include leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation, neurodegenerative disease, and hereditary disease.
- **Conclusion**: Established conclusion: DARS2 provides direct evidence that mitochondrial protein synthesis is central to the module. Hypothesis: mitochondrial translation capacity involving DARS2 may influence responses to lipid, respiratory, or cellular stress.

#### AIFM1

- **Related proteins** (co-abundance neighbors): SUPV3L1 (0.81), SLC25A12 (0.81), SDHA (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apoptosis inducing factor mitochondria associated 1. This gene encodes a flavoprotein essential for nuclear disassembly in apoptotic cells, and it is found in the mitochondrial intermembrane space in healthy cells. Induction of apoptosis results in the translocation of this protein to the nucleus where it affects chromosome condensation and fragmentation. In addition, this gene product induces mitochondria to release the apoptogenic proteins cytochr…
- **Diseases (Open Targets)**: severe X-linked mitochondrial encephalomyopathy (0.813); X-linked hereditary sensory and autonomic neuropathy with hearing loss (0.798); Charcot-Marie-Tooth disease X-linked recessive 4 (0.761); spondyloepimetaphyseal dysplasia, Bieganski type (0.747); combined oxidative phosphorylation deficiency (0.615)
- **Europe PMC papers**: 1952
- **Why important**: AIFM1 connects SUPV3L1, SLC25A12, and SDHA and occurs in (GO:CC mitochondrion; q_global = 0.00231), (GO:MF nucleotide binding; q_global = 0.0258), (GO:MF nucleoside phosphate binding; q_global = 0.0299), and (GO:BP protein folding; q_global = 0.04). It is a mitochondrial flavoprotein involved in apoptotic nuclear disassembly, respiratory-chain complex assembly, and responses to ischemia and toxic stress. Its disease associations include severe X-linked mitochondrial encephalomyopathy, hereditary sensory and autonomic neuropathy, Charcot-Marie-Tooth disease, skeletal dysplasia, and combined oxidative-phosphorylation deficiency.
- **Conclusion**: Established conclusion: AIFM1 represents the mitochondrial stress, respiratory-assembly, and apoptosis dimension of the module. Hypothesis: AIFM1 may help determine whether cells adapt to or undergo apoptosis during severe respiratory or proteostasis stress.

## Module 4

**Tissue pair**: lung and testis  
**Genes (11)**: RNPEP, COPB1, DPP3, PDCD6IP, ATIC, RECQL, AARS1, TRIM25, USP5, USO1, VPS35

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established single pathway assignment. Its gene-level annotations and network suggest a mixed intracellular maintenance program involving vesicle and Golgi trafficking, protein quality control and ubiquitin regulation, translation-related activity, purine biosynthesis, DNA replication and repair, and antiviral or innate immune regulation. The strongest coherent structural signal is intracellular membrane traffic: USO1 and COPB1 form the only high-confidence STRING relationship, while PDCD6IP connects several trafficking, ubiquitin-related, and endosomal components. The module therefore appears functionally heterogeneous rather than a canonical pathway module. The absence of a globally enriched term does not invalidate the co-abundance pattern.

**Cell composition.** This is predominantly a broadly expressed intracellular module. HPA assigns low tissue specificity to most genes, and every module protein is detected in both lung and testis. Most genes also have low immune-cell specificity, arguing against a straightforward blood-cell or leukocyte explanation. Two genes are annotated as secreted, but the module is not dominated by plasma or secreted proteins. Several genes show cell-type enhancement, including epithelial, germ-cell, trophoblast, muscle, and neutrophil-associated patterns, so shared cell populations or sample composition could contribute to the cross-tissue co-abundance. The skeletal-muscle and myonuclear signal for USO1 is a tissue or cell-context clue, not evidence that the entire module is muscle-specific.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence known relationship, COPB1-USO1, directly supporting Golgi and vesicle trafficking biology. No other STRING partners or supplementary STRING functional terms are reported for the module. hu.MAP provides partial, rather than complete, complex support: AARS1 and RECQL co-occur in huMAP3_10115.1 (hu.MAP huMAP3_10115.1), and AARS1 and ATIC co-occur in huMAP3_14442.1 (hu.MAP huMAP3_14442.1). Because each complex contains many additional proteins not present in the module, these observations support compatibility with known complexes but do not establish that the whole module is one physical complex. Overall, the network contains a small amount of established interaction evidence and substantial unconfirmed co-abundance structure.

**STRING interactions (score >= 0.7)**: 1 of 55 gene pairs: COPB1–USO1 (0.869)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10115.1 (RECQL, AARS1; 2/14); huMAP3_14442.1 (ATIC, AARS1; 2/57)

### Novelty

The cross-tissue co-abundance pattern may be a new systems-level observation, because most module edges are not represented by the reported high-confidence STRING relationships and the module lacks a globally significant GO/KEGG or STRING enrichment signature. However, it should not be called a newly discovered molecular complex or pathway. Existing evidence for COPB1-USO1 and the partial hu.MAP memberships shows that several component relationships are already known. Absence from STRING or hu.MAP is not proof of novelty; the appropriate claim is a potentially novel co-abundance association that integrates several established cellular functions.

**Hypothesis.** Hypothesis: in both lung and testis, the module reflects a shared demand for intracellular cargo handling and proteome maintenance, coupling ER-Golgi and endosomal trafficking with ubiquitin control, aminoacyl-tRNA charging, purine production, DNA maintenance, and innate immune regulation. PDCD6IP, USO1, and COPB1 could represent the trafficking and vesicle component, while TRIM25 and USP5 could tune ubiquitin-dependent responses, and AARS1, ATIC, and RECQL could reflect biosynthetic and genome-maintenance requirements. This hypothesis should be tested against cell-type proportions, protein abundance, and independent cohorts before assigning a direct mechanistic connection among all genes.

### Important genes

#### PDCD6IP

- **Related proteins** (co-abundance neighbors): RNPEP (0.90), TRIM25 (0.85), USP5 (0.85), VPS35 (0.83), AARS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 6 interacting protein. This gene encodes a protein that functions within the ESCRT pathway in the abscission stage of cytokinesis, in intralumenal endosomal vesicle formation, and in enveloped virus budding. Studies using mouse cells have shown that overexpression of this protein can block apoptosis. In addition, the product of this gene binds to the product of the PDCD6 gene, a protein required for apoptosis, in a calc…
- **Diseases (Open Targets)**: HIV infectious disease (0.463); anthrax infection (0.462); alcohol drinking (0.388); autosomal recessive primary microcephaly (0.386); microcephaly 29, primary, autosomal recessive (0.383)
- **Europe PMC papers**: 1668
- **Why important**: PDCD6IP is the most connected node in the module and links RNPEP, TRIM25, USP5, VPS35, and AARS1. Its established ESCRT-related roles in cytokinesis, intralumenal vesicle formation, and enveloped-virus budding make it a strong candidate organizer of the module's membrane-trafficking and cellular-stress signal. It also has extensive literature and disease-relevant associations.
- **Conclusion**: Established: PDCD6IP is a multifunctional ESCRT-associated trafficking and membrane biology protein with broad tissue distribution. Hypothesis: its central network position may help coordinate the shared co-abundance program, but the network does not prove direct physical interaction with its listed neighbors.

#### AARS1

- **Related proteins** (co-abundance neighbors): ATIC (0.88), RECQL (0.84), TRIM25 (0.81), PDCD6IP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_10115.1, huMAP3_14442.1
- **Function (MyGene.info)**: alanyl-tRNA synthetase 1. The human alanyl-tRNA synthetase (AARS) belongs to a family of tRNA synthases, of the class II enzymes.  Class II tRNA synthases evolved early in evolution and are highly conserved. This is reflected by the fact that 498 of the 968-residue polypeptide human AARS shares 41% identity witht the E.coli protein.  tRNA synthases are the enzymes that interpret the RNA code and attach specific aminoacids …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2N (0.762); developmental and epileptic encephalopathy, 29 (0.747); undetermined early-onset epileptic encephalopathy (0.678); trichothiodystrophy 8, nonphotosensitive (0.568); Charcot-Marie-Tooth disease type 2 (0.566)
- **Europe PMC papers**: 672
- **Why important**: AARS1 is highly connected and bridges ATIC, RECQL, TRIM25, and PDCD6IP. Its established role in alanyl-tRNA aminoacylation makes it a plausible marker of translational and proteostasis demand. It is also present in both hu.MAP-supported complexes (hu.MAP huMAP3_10115.1) and (hu.MAP huMAP3_14442.1), giving it more complex-level context than most module genes, and it has important neurological and inherited-disease associations.
- **Conclusion**: Established: AARS1 supports translation through tRNA charging and participates in annotated complexes. Hypothesis: it may connect biosynthetic demand to trafficking and stress-control genes in this module; a direct functional bridge remains unproven.

#### ATIC

- **Related proteins** (co-abundance neighbors): AARS1 (0.88), RNPEP (0.87), USO1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: 5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase. This gene encodes a bifunctional protein that catalyzes the last two steps of the de novo purine biosynthetic pathway. The N-terminal domain has phosphoribosylaminoimidazolecarboxamide formyltransferase activity, and the C-terminal domain has IMP cyclohydrolase activity. A mutation in this gene results in AICA-ribosiduria. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: AICA-ribosiduria (0.708); cancer (0.571); Intellectual disability (0.463); lung adenocarcinoma (0.390); anaplastic large cell lymphoma (0.374)
- **Europe PMC papers**: 5200
- **Why important**: ATIC connects AARS1, RNPEP, and USO1 and is the only module gene with a clearly defined bifunctional role in the final steps of de novo purine biosynthesis. Its membership in hu.MAP complex (hu.MAP huMAP3_14442.1) and strong disease and cancer literature make it an informative metabolic anchor despite the lack of globally significant enrichment.
- **Conclusion**: Established: ATIC catalyzes late purine-biosynthetic reactions and occurs in the reported hu.MAP complex (hu.MAP huMAP3_14442.1). Hypothesis: its co-abundance with trafficking genes may reflect coordinated nucleotide and membrane-protein production rather than a shared physical complex.

#### TRIM25

- **Related proteins** (co-abundance neighbors): PDCD6IP (0.85), AARS1 (0.81), DPP3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tripartite motif containing 25. The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein is an RNA binding protein, functions as a ubiquitin E3 ligase and is involved in multiple cellular processes, including regulation of antiviral innate immunity. [provided by RefSeq, S…
- **Diseases (Open Targets)**: dengue disease (0.463); COVID-19 (0.376); severe acute respiratory syndrome (0.372); neoplasm (0.108); hepatocellular carcinoma (0.106)
- **Europe PMC papers**: 4363
- **Why important**: TRIM25 occupies a connecting position between PDCD6IP, AARS1, and DPP3. It is an RNA-binding ubiquitin E3 ligase involved in antiviral innate immunity, ubiquitination, and autophagy regulation. Its neutrophil and monocyte cell-type signals provide an important contextual alternative in which the module could partly reflect immune or inflammatory state. It also has substantial disease literature.
- **Conclusion**: Established: TRIM25 is a regulator of ubiquitin-dependent and antiviral innate immune processes, with immune-cell enhancement in HPA. Hypothesis: it may provide a stress-responsive regulatory arm of the module, but the shared lung-testis signal cannot be attributed to immune infiltration without cell-composition analysis.

#### USO1

- **Related proteins** (co-abundance neighbors): COPB1 (0.89), ATIC (0.80); STRING partners: COPB1 (0.869)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: USO1 vesicle transport factor. The protein encoded by this gene is a peripheral membrane protein which recycles between the cytosol and the Golgi apparatus during interphase. It is regulated by phosphorylation: dephosphorylated protein associates with the Golgi membrane and dissociates from the membrane upon phosphorylation. Ras-associated protein 1 recruits this protein to coat protein complex II (COPII) vesicles during buddin…
- **Diseases (Open Targets)**: psoriatic arthritis (0.184); bipolar disorder (0.150); retinitis pigmentosa (0.085); cone dystrophy (0.076); cone-rod dystrophy (0.076)
- **Europe PMC papers**: 546
- **Why important**: USO1 is one half of the module's only high-confidence STRING pair, together with COPB1, and its annotation directly concerns ER-to-Golgi vesicle transport, Golgi recycling, and vesicle fusion. Its tissue and myonuclear enhancement makes it useful for assessing cellular-context effects. Its disease associations are more limited than those of the central regulatory genes, but its functional specificity is high.
- **Conclusion**: Established: USO1 is a Golgi-associated vesicle transport factor and has a known relationship with COPB1. Hypothesis: the USO1-COPB1 pair may represent the most mechanistically coherent core of the module, while its broader connections are co-abundance associations requiring experimental validation.

## Module 5

**Tissue pair**: lung and testis  
**Genes (11)**: AMPD2, AP3D1, ATXN2L, DYNC1I2, DYNC1H1, METAP2, NSFL1C, RBM12, UPF1, LARS1, EFTUD2

### Function

No GO/KEGG term passed global correction, so the module has no statistically established GO/KEGG enrichment. The strongest functional signal is a cytoplasmic dynein motor submodule formed by DYNC1H1 and DYNC1I2, supported by their direct high-confidence STRING relationship and repeated hu.MAP membership (hu.MAP huMAP3_02226.1) (hu.MAP huMAP3_08809.1) (hu.MAP huMAP3_09560.1) (hu.MAP huMAP3_07382.1) (hu.MAP huMAP3_08818.1) (hu.MAP huMAP3_09593.1) (hu.MAP huMAP3_15007.1) (hu.MAP huMAP3_11519.1) (hu.MAP huMAP3_09802.1) (hu.MAP huMAP3_15289.1) (hu.MAP huMAP3_12566.1). The remaining genes suggest a broader cellular-maintenance context involving RNA surveillance and splicing, translation and amino-acid metabolism, vesicle and lysosomal trafficking, protein quality control, and microtubule-dependent transport. These annotations support a cautious interpretation as a mixed intracellular transport and gene-expression homeostasis module rather than a single well-defined pathway. The absence of globally enriched terms does not invalidate the co-abundance module.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity and low immune-cell specificity, and the proteins are generally detected in lung and testis, consistent with broadly expressed intracellular machinery rather than a tissue-exclusive program. There are isolated cell-type or blood-cell associations, especially for AMPD2, and brain-enhanced expression for AMPD2 and DYNC1H1, but the module is not dominated by blood-cell markers. The shared lung–testis signal could therefore reflect common cellular housekeeping, transport, RNA-processing, or proliferative requirements rather than a specialized lung–testis biological function.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

Known physical-network support is concentrated in DYNC1H1–DYNC1I2, the sole STRING interaction reported for this module and a biologically coherent dynein relationship. hu.MAP independently places the same pair together across many dynein-related complexes (hu.MAP huMAP3_02226.1) (hu.MAP huMAP3_08809.1) (hu.MAP huMAP3_09560.1) (hu.MAP huMAP3_07382.1) (hu.MAP huMAP3_08818.1) (hu.MAP huMAP3_09593.1) (hu.MAP huMAP3_15007.1) (hu.MAP huMAP3_11519.1) (hu.MAP huMAP3_09802.1) (hu.MAP huMAP3_15289.1) (hu.MAP huMAP3_12566.1), although each complex contains many members outside this module; this supports their membership in a known cytoplasmic dynein assembly but does not establish that the whole co-abundance module is one physical complex. METAP2 and AMPD2 share a hu.MAP complex (hu.MAP huMAP3_10654.1), providing a separate, more limited connection. The other genes have no listed STRING partners or hu.MAP complexes in the fact sheet. Thus, the network contains a well-supported dynein core plus weaker co-abundance links that may represent coordinated expression rather than direct binding.

**STRING interactions (score >= 0.7)**: 1 of 55 gene pairs: DYNC1H1–DYNC1I2 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10654.1 (METAP2, AMPD2; 2/4); huMAP3_02226.1 (DYNC1I2, DYNC1H1; 2/7); huMAP3_08809.1 (DYNC1I2, DYNC1H1; 2/7); huMAP3_09560.1 (DYNC1I2, DYNC1H1; 2/8); huMAP3_07382.1 (DYNC1I2, DYNC1H1; 2/9); huMAP3_08818.1 (DYNC1I2, DYNC1H1; 2/9); huMAP3_09593.1 (DYNC1I2, DYNC1H1; 2/10); huMAP3_15007.1 (DYNC1I2, DYNC1H1; 2/12); huMAP3_11519.1 (DYNC1I2, DYNC1H1; 2/13); huMAP3_09802.1 (DYNC1I2, DYNC1H1; 2/15); huMAP3_15289.1 (DYNC1I2, DYNC1H1; 2/28); huMAP3_12566.1 (DYNC1I2, DYNC1H1; 2/51)

### Novelty

The dynein relationship and the dynein complex memberships are established biology, so the module should not be presented as a newly discovered dynein interaction or complex. A potentially novel aspect is the specific conserved co-abundance pattern shared by lung and testis, particularly its juxtaposition of dynein, RNA-processing, translation, trafficking, and nucleotide-metabolism genes. However, the sparse STRING support, the absence of globally significant GO/KEGG enrichment, and the lack of a single coherent known complex make a strong new-function claim premature. The appropriate conclusion is a potentially interesting co-expression observation requiring replication, tissue-cell deconvolution, and independent functional validation.

**Hypothesis.** Hypothesis: the module reflects coordinated demand for intracellular cargo movement and cellular quality control in cells shared between lung and testis. DYNC1H1–DYNC1I2 could provide the microtubule-based retrograde transport backbone, while AP3D1 and NSFL1C could connect vesicle or organelle trafficking and protein-remodelling processes. EFTUD2, RBM12, UPF1, and ATXN2L could couple this transport state to RNA processing, surveillance, and stress-responsive gene expression, with METAP2, LARS1, and AMPD2 supporting translation and metabolic capacity. This is a mechanistic proposal, not an enrichment result; it should be tested by cell-type-resolved expression, perturbation of the dynein pair, and measurement of cargo transport, RNA surveillance, and proteostasis.

### Important genes

#### DYNC1H1

- **Related proteins** (co-abundance neighbors): DYNC1I2 (0.83); STRING partners: DYNC1I2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_02226.1, huMAP3_08809.1, huMAP3_09560.1, huMAP3_07382.1, huMAP3_08818.1, huMAP3_09593.1, huMAP3_15007.1, huMAP3_11519.1, huMAP3_09802.1, huMAP3_15289.1, huMAP3_12566.1
- **Function (MyGene.info)**: dynein cytoplasmic 1 heavy chain 1. Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polyp…
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy without contractures (0.816); intellectual disability, autosomal dominant 13 (0.815); Charcot-Marie-Tooth disease axonal type 2O (0.799); autosomal dominant non-syndromic intellectual disability (0.634); hereditary disease (0.545)
- **Europe PMC papers**: 1731
- **Why important**: DYNC1H1 is the cytoplasmic dynein heavy chain and provides the principal motor interpretation of the module. It is directly connected to DYNC1I2 by STRING and recurs with DYNC1I2 across the hu.MAP complexes (hu.MAP huMAP3_02226.1) (hu.MAP huMAP3_08809.1) (hu.MAP huMAP3_09560.1) (hu.MAP huMAP3_07382.1) (hu.MAP huMAP3_08818.1) (hu.MAP huMAP3_09593.1) (hu.MAP huMAP3_15007.1) (hu.MAP huMAP3_11519.1) (hu.MAP huMAP3_09802.1) (hu.MAP huMAP3_15289.1) (hu.MAP huMAP3_12566.1). Its annotations include microtubule-based movement, retrograde axonal transport, organelle movement, spindle organization, and intracellular transport. It is brain-enhanced and associated with multiple inherited neurological disorders, with substantial literature support.
- **Conclusion**: Established evidence supports DYNC1H1 as the strongest mechanistic anchor and a known dynein component. Its participation in the lung–testis co-abundance pattern is supported, but a tissue-specific or novel dynein function is not established.

#### DYNC1I2

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.83), ATXN2L (0.82); STRING partners: DYNC1H1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Microtubules, Centrosome, Cytosol, Flagellar centriole, Mid piece, Principal piece; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_02226.1, huMAP3_08809.1, huMAP3_09560.1, huMAP3_07382.1, huMAP3_08818.1, huMAP3_09593.1, huMAP3_15007.1, huMAP3_11519.1, huMAP3_09802.1, huMAP3_15289.1, huMAP3_12566.1
- **Function (MyGene.info)**: dynein cytoplasmic 1 intermediate chain 2. This gene encodes a member of the dynein intermediate chain family. The encoded protein is a non-catalytic component of the cytoplasmic dynein 1 complex, which acts as a retrograde microtubule motor to transport organelles and vesicles. A pseudogene of this gene is located on chromosome 10. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly and structural brain anomalies (0.698); neurodegenerative disease (0.484); viral infectious disease (0.462); lysosomal storage disease (0.432); neurodevelopmental disorder with microcephaly, hypotonia, and variable brain anomalies (0.425)
- **Europe PMC papers**: 407
- **Why important**: DYNC1I2 is a dynein intermediate-chain component that links the module directly to the motor complex. It has the same STRING-supported relationship with DYNC1H1 and the same repeated hu.MAP complex support (hu.MAP huMAP3_02226.1) (hu.MAP huMAP3_08809.1) (hu.MAP huMAP3_09560.1) (hu.MAP huMAP3_07382.1) (hu.MAP huMAP3_08818.1) (hu.MAP huMAP3_09593.1) (hu.MAP huMAP3_15007.1) (hu.MAP huMAP3_11519.1) (hu.MAP huMAP3_09802.1) (hu.MAP huMAP3_15289.1) (hu.MAP huMAP3_12566.1). Its known functions include microtubule transport, intracellular transport, and spindle-checkpoint regulation. Its localization in microtubules, centrosomes, and testis flagellar structures makes it especially informative for a transport-centered interpretation.
- **Conclusion**: Established evidence identifies DYNC1I2 as a co-abundant dynein partner rather than a newly discovered interaction. It supports the transport-core interpretation, while the broader module-level coordination remains a hypothesis.

#### UPF1

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.84), AMPD2 (0.82), ATXN2L (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UPF1 RNA helicase and ATPase. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons.…
- **Diseases (Open Targets)**: Intellectual disability (0.437); Global developmental delay (0.426); High anterior hairline (0.425); Frontal bossing (0.425); Hypertelorism (0.425)
- **Europe PMC papers**: 4252
- **Why important**: UPF1 is a central RNA helicase and ATPase involved in mRNA export, nonsense-mediated decay, translational termination, and RNA quality control. It occupies a relatively well-connected position alongside EFTUD2, AMPD2, and ATXN2L, thereby linking the module's RNA and metabolic features. It has extensive literature and disease associations involving neurodevelopmental phenotypes.
- **Conclusion**: Established evidence supports UPF1 as an RNA-surveillance and post-transcriptional regulation component. Its connection to the dynein pair is co-abundance evidence, not proof that UPF1 physically functions within the dynein complex.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): RBM12 (0.85), UPF1 (0.84), ATXN2L (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 is a spliceosomal GTPase involved in snRNP assembly, spliceosome remodeling, and pre-mRNA splicing. It has a comparatively strong network position through RBM12, UPF1, and ATXN2L, and it has substantial literature and a well-established association with mandibulofacial dysostosis with microcephaly. It represents the module's most prominent RNA-splicing anchor.
- **Conclusion**: Established evidence supports EFTUD2 as a core RNA-processing gene represented in the module. Its coordinated abundance with transport and metabolic genes is suggestive of shared cellular demand but does not establish a direct molecular complex.

#### METAP2

- **Related proteins** (co-abundance neighbors): NSFL1C (0.86), AP3D1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_10654.1
- **Function (MyGene.info)**: methionyl aminopeptidase 2. The protein encoded by this gene is a member of the methionyl aminopeptidase family. The encoded protein functions both by protecting the alpha subunit of eukaryotic initiation factor 2 from inhibitory phosphorylation and by removing the amino-terminal methionine residue from nascent proteins. Increased expression of this gene is associated with various forms of cancer, and the anti-cancer drugs f…
- **Diseases (Open Targets)**: neurodegenerative disease (0.521); autoimmune disorder of central nervous system (0.316); obesity disorder (0.305); Prader-Willi syndrome (0.279); Polyphagia (0.259)
- **Europe PMC papers**: 828
- **Why important**: METAP2 links nascent-protein processing and translational regulation to the module. It is connected to NSFL1C and AP3D1 in the co-abundance graph and shares a hu.MAP complex with AMPD2 (hu.MAP huMAP3_10654.1). Its known functions include removal of amino-terminal methionine and regulation of translation initiation, and it has extensive cancer and pharmacology literature.
- **Conclusion**: Established evidence supports METAP2 as a protein-production and processing component with an independent hu.MAP connection to AMPD2. Its possible coordination with dynein and RNA surveillance is a module-level hypothesis rather than a demonstrated physical interaction.

#### AMPD2

- **Related proteins** (co-abundance neighbors): UPF1 (0.82), LARS1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_10654.1
- **Function (MyGene.info)**: adenosine monophosphate deaminase 2. The protein encoded by this gene is important in purine metabolism by converting AMP to IMP. The encoded protein, which acts as a homotetramer, is one of three AMP deaminases found in mammals. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: pontocerebellar hypoplasia type 9 (0.813); hereditary spastic paraplegia 63 (0.696); pontocerebellar hypoplasia (0.670); hereditary disease (0.404); Abnormality of the nervous system (0.340)
- **Europe PMC papers**: 560
- **Why important**: AMPD2 supplies the module's clearest nucleotide-energy metabolism link by converting AMP to IMP and participating in purine and ATP metabolism. It connects to UPF1 and LARS1 in the network and shares hu.MAP complex (hu.MAP huMAP3_10654.1) with METAP2. HPA identifies brain enhancement and associations with several neural and myeloid cell types, while disease annotations include pontocerebellar hypoplasia and hereditary spastic paraplegia.
- **Conclusion**: Established evidence supports AMPD2 as a metabolic component and a possible source of cell-type or tissue-composition variation. Its co-abundance with the transport and RNA-processing genes may indicate coordinated energy demand, but that mechanism remains hypothetical.

## Module 6

**Tissue pair**: lung and testis  
**Genes (23)**: APEX1, MTHFD1, CPNE3, DDX39B, FLNB, FSCN1, FUS, G6PD, GLOD4, HDGF, HNRNPH1, HNRNPF, HNRNPK, LDHB, MATR3, OLA1, PRKDC, PTBP1, SEC23A, SEPTIN9, TKT, XPO5, XRCC6

### Function

The strongest interpretation is a conserved nuclear RNA metabolism module. The primary enrichment evidence identifies RNA binding (GO:MF RNA binding; q_global = 0.00029), nucleic-acid binding (GO:MF nucleic acid binding; q_global = 0.00302), and regulation of RNA splicing (GO:BP regulation of RNA splicing; q_global = 0.0294). The splicing signal is concentrated in FUS, HNRNPF, HNRNPH1, HNRNPK, and PTBP1, while the broader RNA-binding signal includes additional nuclear and multifunctional proteins. STRING independently supports RNA binding (STRING Function RNA binding; within-query FDR = 4.8e-05), an mRNA-processing and mRNA-stability neighborhood (STRING NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex; within-query FDR = 0.00013), and RNA-recognition motifs (STRING SMART RNA recognition motif; within-query FDR = 0.0037). Thus, the core function is likely coordinated handling, processing, splicing, stabilization, and export of nuclear RNA, rather than a single metabolic pathway. DNA repair, nucleic-acid surveillance, cytoskeletal, vesicular, and metabolic proteins appear to form peripheral or context-dependent components rather than defining the primary module function.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: HPA identifies only HDGF as secreted to blood, and the proteins are mainly nucleoplasmic or cytosolic. The module is also not strongly blood-cell specific at the tissue level, because most genes have low immune-cell specificity. Nevertheless, several genes show cell-type enhancement in progenitors, megakaryocytes, neutrophil-lineage cells, myeloid cells, or epithelial populations, so sample cellular composition could contribute to the shared signal. The broad tissue distribution, detection of every module protein in both lung and testis, and abundance of ubiquitously expressed hnRNP and housekeeping-like proteins support a broadly expressed core program rather than a lung- or testis-exclusive function. HPA therefore makes blood contamination an insufficient explanation, although shared cell states or cellular mixtures remain plausible contributors.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF RNA binding | 0.00029 | APEX1, CPNE3, DDX39B, FLNB, FSCN1, FUS, HDGF, HNRNPF, HNRNPH1, HNRNPK, MATR3, PRKDC, PTBP1, XPO5, XRCC6 |
| GO:MF nucleic acid binding | 0.00302 | APEX1, CPNE3, DDX39B, FLNB, FSCN1, FUS, HDGF, HNRNPF, HNRNPH1, HNRNPK, MATR3, PRKDC, PTBP1, XPO5, XRCC6 |
| GO:BP regulation of RNA splicing | 0.0294 | FUS, HNRNPF, HNRNPH1, HNRNPK, PTBP1 |

### STRING and hu.MAP

STRING shows a strongly connected established hnRNP-centered neighborhood involving FUS, HNRNPF, HNRNPH1, HNRNPK, PTBP1, MATR3, and DDX39B. The very strong associations among the hnRNP proteins and the known PRKDC–XRCC6 pair indicate that much of the module recapitulates documented protein relationships. STRING also supports the G6PD–TKT pair and the FLNB–FSCN1 pair, linking smaller metabolic and actin-associated branches to the nuclear core. hu.MAP provides convergent complex evidence: HNRNPH1, FUS, HNRNPF, and HNRNPK co-occur in a large hnRNP complex (hu.MAP huMAP3_14523.1), HNRNPH1 and HNRNPF recur in several related complexes (hu.MAP huMAP3_07055.1) (hu.MAP huMAP3_06054.1) (hu.MAP huMAP3_11034.1) (hu.MAP huMAP3_13511.1), APEX1 and OLA1 occur together in another complex (hu.MAP huMAP3_14442.1), and MATR3 and HNRNPK occur together in a further RNA-associated complex (hu.MAP huMAP3_10625.1). The known interactions are concentrated in the RNA-processing core, whereas several co-abundance links have no listed STRING or hu.MAP support. This pattern is consistent with a real functional core plus tissue-contextual associations, not with every module edge being a direct physical interaction.

**STRING interactions (score >= 0.7)**: 23 of 253 gene pairs: DDX39B–HNRNPF (0.736); DDX39B–HNRNPH1 (0.742); DDX39B–HNRNPK (0.808); DDX39B–PTBP1 (0.785); FLNB–FSCN1 (0.788); FUS–HNRNPF (0.794); FUS–HNRNPH1 (0.941); FUS–HNRNPK (0.927); FUS–MATR3 (0.91); FUS–PTBP1 (0.852); G6PD–TKT (0.91); HNRNPF–HNRNPH1 (0.994); HNRNPF–HNRNPK (0.971); HNRNPF–MATR3 (0.766); HNRNPF–PTBP1 (0.942); HNRNPH1–HNRNPK (0.975); HNRNPH1–MATR3 (0.911); HNRNPH1–PTBP1 (0.978); HNRNPK–MATR3 (0.923); HNRNPK–PTBP1 (0.997); HNRNPK–XRCC6 (0.738); MATR3–PTBP1 (0.83); PRKDC–XRCC6 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function RNA binding (FDR = 4.8e-05, 15 genes); Keyword Ubl conjugation (FDR = 0.00012, 13 genes); NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex (FDR = 0.00013, 6 genes); NetworkNeighborAL Mixed, incl. Multisystem proteinopathy, and Zinc finger, CHHC-type (FDR = 0.00013, 5 genes); Function Organic cyclic compound binding (FDR = 0.00039, 20 genes); Function Heterocyclic compound binding (FDR = 0.00039, 20 genes); NetworkNeighborAL Mixed, incl. Zinc finger, CHHC-type, and Multisystem proteinopathy (FDR = 0.00053, 4 genes); Keyword Isopeptide bond (FDR = 0.00077, 11 genes); Keyword RNA-binding (FDR = 0.002, 8 genes); TISSUES Cervical carcinoma cell (FDR = 0.0027, 7 genes); TISSUES Blood cancer cell (FDR = 0.0027, 12 genes); TISSUES Leukemia cell (FDR = 0.0027, 11 genes); COMPARTMENTS Nucleoplasm (FDR = 0.003, 9 genes); SMART RNA recognition motif (FDR = 0.0037, 5 genes); Keyword DNA-binding (FDR = 0.0049, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14523.1 (HNRNPH1, FUS, HNRNPF, HNRNPK; 4/33); huMAP3_07055.1 (HNRNPH1, HNRNPF; 2/3); huMAP3_06054.1 (HNRNPH1, HNRNPF; 2/4); huMAP3_11034.1 (HNRNPH1, HNRNPF; 2/5); huMAP3_13511.1 (HNRNPH1, HNRNPF; 2/9); huMAP3_14442.1 (APEX1, OLA1; 2/57); huMAP3_10625.1 (MATR3, HNRNPK; 2/57)

### Novelty

The biological ingredients are not individually novel: hnRNP-mediated RNA processing, DNA repair, pentose-phosphate metabolism, actin organization, and vesicle trafficking are established functions in the supplied evidence. The potentially novel result is their conserved co-abundance configuration across lung and testis, especially the way a well-supported hnRNP core is connected to DNA-repair, metabolic, cytoskeletal, and cell-state-associated proteins. The fact sheet does not establish that this exact cross-tissue module has been previously reported, so it supports a cautious claim of a potentially new systems-level association rather than a claim of a new molecular mechanism. Lack of STRING or hu.MAP coverage for some edges cannot by itself demonstrate novelty; novelty would require comparison with published tissue co-abundance modules and independent datasets.

**Hypothesis.** Hypothesis: this module represents a shared nuclear RNA-processing state maintained across lung and testis, in which an hnRNP-centered assembly coordinates pre-mRNA splicing, RNA maturation, stabilization, and export. FUS, HNRNPF, HNRNPH1, HNRNPK, PTBP1, and DDX39B could form the principal RNA-handling layer, while XPO5 and the DNA-repair proteins could couple RNA processing to nuclear transport and genome-integrity responses. The metabolic and cytoskeletal branches may reflect the energetic, proliferative, and structural demands of the cells expressing this program, or shared cellular composition between the tissues. This is a mechanistic model generated from co-abundance and interaction evidence; it does not establish direct physical binding or causal regulation for every member.

### Important genes

#### HNRNPK

- **Related proteins** (co-abundance neighbors): PTBP1 (0.95), OLA1 (0.86), G6PD (0.85), XRCC6 (0.84), MTHFD1 (0.83), LDHB (0.83), HNRNPH1 (0.82), HNRNPF (0.82), FUS (0.82), FLNB (0.81), CPNE3 (0.80), SEC23A (0.80); STRING partners: DDX39B (0.808), FUS (0.927), HNRNPF (0.971), HNRNPH1 (0.975), MATR3 (0.923), PTBP1 (0.997), XRCC6 (0.738)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_14523.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is the most central network component in the supplied module and participates in all primary enrichment terms (GO:MF RNA binding; q_global = 0.00029) (GO:MF nucleic acid binding; q_global = 0.00302) (GO:BP regulation of RNA splicing; q_global = 0.0294). It is a ubiquitously expressed nuclear hnRNP involved in RNA processing, mRNA splicing, transport, and transcriptional regulation. Its many established STRING relationships with the other hnRNP proteins and its participation in hu.MAP complexes (hu.MAP huMAP3_14523.1) (hu.MAP huMAP3_10625.1) make it a strong organizing candidate. It also has extensive literature and disease associations including Au-Kline syndrome and neurodevelopmental and neurodegenerative disorders.
- **Conclusion**: Established evidence supports HNRNPK as a central RNA-binding and RNA-processing scaffold of the module. The hypothesis that it coordinates the peripheral DNA-repair and metabolic branches is plausible from its network position but is not directly demonstrated by the supplied data.

#### PTBP1

- **Related proteins** (co-abundance neighbors): HNRNPK (0.95), OLA1 (0.86), HNRNPF (0.84), XRCC6 (0.84), APEX1 (0.83), CPNE3 (0.81), LDHB (0.81), HDGF (0.81); STRING partners: DDX39B (0.785), FUS (0.852), HNRNPF (0.942), HNRNPH1 (0.978), HNRNPK (0.997), MATR3 (0.83)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypyrimidine tract binding protein 1. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA-binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.505); dengue disease (0.372); open-angle glaucoma (0.330); glaucoma (0.309); neoplasm (0.116)
- **Europe PMC papers**: 4849
- **Why important**: PTBP1 is a highly connected module member and belongs to every primary enrichment term (GO:MF RNA binding; q_global = 0.00029) (GO:MF nucleic acid binding; q_global = 0.00302) (GO:BP regulation of RNA splicing; q_global = 0.0294). Its established function is regulation of alternative splicing and broader mRNA processing through polypyrimidine-tract binding. It has exceptionally extensive literature, strong STRING associations with the hnRNP core, and links in the co-abundance graph to APEX1, CPNE3, HDGF, LDHB, OLA1, and XRCC6. Its disease associations include neurodevelopmental disorder, dengue disease, and glaucoma.
- **Conclusion**: Established evidence identifies PTBP1 as a major functional effector of the module's RNA-splicing program. Its association with metabolic, DNA-repair, and growth-related proteins may indicate coordinated cellular state regulation, but the direction and mechanism of those links remain hypothetical.

#### HNRNPF

- **Related proteins** (co-abundance neighbors): HNRNPH1 (0.85), PTBP1 (0.84), HNRNPK (0.82), OLA1 (0.82), DDX39B (0.81); STRING partners: DDX39B (0.736), FUS (0.794), HNRNPH1 (0.994), HNRNPK (0.971), MATR3 (0.766), PTBP1 (0.942)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_14523.1, huMAP3_07055.1, huMAP3_06054.1, huMAP3_11034.1, huMAP3_13511.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein F. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins that complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and regulate alternative splicing, polyadenylation, and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present…
- **Diseases (Open Targets)**: neurodegenerative disease (0.518); dengue disease (0.370); knee fracture (0.322); breast cancer (0.103); posterior cortical atrophy (0.083)
- **Europe PMC papers**: 971
- **Why important**: HNRNPF is a core RNA-binding hnRNP, participates in all primary enrichment terms (GO:MF RNA binding; q_global = 0.00029) (GO:MF nucleic acid binding; q_global = 0.00302) (GO:BP regulation of RNA splicing; q_global = 0.0294), and is embedded in the densest known interaction neighborhood with HNRNPH1, HNRNPK, PTBP1, FUS, MATR3, and DDX39B. It recurs across several hu.MAP complexes (hu.MAP huMAP3_14523.1) (hu.MAP huMAP3_07055.1) (hu.MAP huMAP3_06054.1) (hu.MAP huMAP3_11034.1) (hu.MAP huMAP3_13511.1), providing unusually strong complex-level support. Its established functions include alternative splicing, polyadenylation, and mRNA transport, with literature and disease associations involving neurodegenerative and other disorders.
- **Conclusion**: Established evidence supports HNRNPF as a core component of a conserved hnRNP processing assembly. Its repeated complex membership makes it a stronger mechanistic anchor than its moderate module connectivity alone would suggest; any role in linking this assembly to tissue-specific biology remains a hypothesis.

#### HNRNPH1

- **Related proteins** (co-abundance neighbors): HNRNPF (0.85), HNRNPK (0.82); STRING partners: DDX39B (0.742), FUS (0.941), HNRNPF (0.994), HNRNPK (0.975), MATR3 (0.911), PTBP1 (0.978)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_14523.1, huMAP3_07055.1, huMAP3_06054.1, huMAP3_11034.1, huMAP3_13511.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein H1. This gene encodes a member of a subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins that complex with heterogeneous nuclear RNA. These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the n…
- **Diseases (Open Targets)**: neurodevelopmental disorder with craniofacial dysmorphism and skeletal defects (0.668); dengue disease (0.462); hereditary disease (0.411); neurodevelopmental disorder (0.400); syndromic intellectual disability (0.370)
- **Europe PMC papers**: 1509
- **Why important**: HNRNPH1 participates in all primary enrichment terms (GO:MF RNA binding; q_global = 0.00029) (GO:MF nucleic acid binding; q_global = 0.00302) (GO:BP regulation of RNA splicing; q_global = 0.0294), has strong interactions with the principal hnRNP members, and recurs in multiple hu.MAP complexes (hu.MAP huMAP3_14523.1) (hu.MAP huMAP3_07055.1) (hu.MAP huMAP3_06054.1) (hu.MAP huMAP3_11034.1) (hu.MAP huMAP3_13511.1). It is an established nuclear RNA-processing factor involved in splicing and RNA metabolism. Its extensive interaction support, together with disease associations involving neurodevelopmental and hereditary disorders, makes it an important structural and functional component despite its more limited direct co-abundance degree.
- **Conclusion**: Established evidence supports HNRNPH1 as a conserved RNA-splicing complex component that helps define the module's molecular identity. The cross-tissue conservation may reflect a shared requirement for this RNA-processing machinery, but it does not prove a specialized lung-testis role.

#### FUS

- **Related proteins** (co-abundance neighbors): HNRNPK (0.82); STRING partners: HNRNPF (0.794), HNRNPH1 (0.941), HNRNPK (0.927), MATR3 (0.91), PTBP1 (0.852)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_14523.1
- **Function (MyGene.info)**: FUS RNA binding protein. This gene encodes a multifunctional protein component of the heterogeneous nuclear ribonucleoprotein (hnRNP) complex. The hnRNP complex is involved in pre-mRNA splicing and the export of fully processed mRNA to the cytoplasm. This protein belongs to the FET family of RNA-binding proteins which have been implicated in cellular processes that include regulation of gene expression, maintenance of gen…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.710); sporadic amyotrophic lateral sclerosis (0.683); frontotemporal dementia with motor neuron disease (0.667); essential tremor (0.557); juvenile amyotrophic lateral sclerosis (0.527)
- **Europe PMC papers**: 19869
- **Why important**: FUS participates in every primary enrichment term (GO:MF RNA binding; q_global = 0.00029) (GO:MF nucleic acid binding; q_global = 0.00302) (GO:BP regulation of RNA splicing; q_global = 0.0294) and connects to the hnRNP core through strong STRING relationships with HNRNPH1, HNRNPK, PTBP1, HNRNPF, and MATR3. It is a multifunctional nuclear RNA-binding protein involved in splicing, mRNA stabilization, transcriptional regulation, and maintenance of genomic integrity. FUS has very extensive literature and strong disease associations with amyotrophic lateral sclerosis, frontotemporal dementia with motor neuron disease, and related neurodegenerative conditions. It also occurs in the large hnRNP hu.MAP complex (hu.MAP huMAP3_14523.1).
- **Conclusion**: Established evidence supports FUS as a biologically important bridge between RNA processing and genome-integrity functions. Its disease biology makes it a particularly informative marker of module perturbation, while a direct causal role in the lung-testis co-abundance pattern remains unproven.

#### XRCC6

- **Related proteins** (co-abundance neighbors): MTHFD1 (0.84), HNRNPK (0.84), PTBP1 (0.84), PRKDC (0.83), OLA1 (0.81), XPO5 (0.80); STRING partners: HNRNPK (0.738), PRKDC (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: X-ray repair cross complementing 6. The p70/p80 autoantigen is a nuclear complex consisting of two subunits with molecular masses of approximately 70 and 80 kDa. The complex functions as a single-stranded DNA-dependent ATP-dependent helicase. The complex may be involved in the repair of nonhomologous DNA ends such as that required for double-strand break repair, transposition, and V(D)J recombination. High levels of autoantibodies t…
- **Diseases (Open Targets)**: HIV infectious disease (0.505); neurodegenerative disease (0.441); intelligence (0.209); breast cancer (0.175); Abnormality of the skeletal system (0.154)
- **Europe PMC papers**: 2742
- **Why important**: XRCC6 is connected in the module to HNRNPK, PTBP1, PRKDC, MTHFD1, OLA1, and XPO5, and its PRKDC interaction is strongly supported by STRING. It is a component of the Ku DNA-repair complex and participates in nonhomologous end joining, double-strand-break repair, recombinational repair, and telomere maintenance. HPA shows cell-type enhancement in early and late primary spermatocytes, which is especially relevant to the lung-testis comparison. Its extensive literature and disease associations include severe combined immunodeficiency, neurodegenerative disease, and other conditions.
- **Conclusion**: Established evidence supports XRCC6 as the principal DNA-repair and genome-stability representative in the module, and its spermatocyte-associated expression provides a plausible tissue-context clue. Its connection to the RNA-processing core may reflect coordinated nuclear stress or proliferation programs, but that coupling is a hypothesis rather than an established mechanism.

## Module 7

**Tissue pair**: lung and testis  
**Genes (18)**: ATP5F1C, CS, MT-CO2, GNA11, GNAI3, ME2, UQCRC1, UQCRC2, RAB10, RAB18, RAB21, RDH11, RTN4, SEC22B, SCCPDH, SFXN1, TAMM41, TMX1

### Function

The strongest interpretation is a conserved intracellular membrane and organelle module, with a prominent mitochondrial respiratory component and an endoplasmic-reticulum membrane-trafficking component. The primary GO evidence supports organelle membrane involvement (GO:CC organelle membrane; q_global = 0.00942) and specifically implicates the ER tubular network and its organization through RAB10, RAB18, and RTN4 (GO:CC endoplasmic reticulum tubular network; q_global = 0.0185)(GO:BP endoplasmic reticulum tubular network organization; q_global = 0.0487). The network separates into a mitochondrial metabolic and respiratory neighborhood, including CS, ME2, ATP5F1C, UQCRC1, UQCRC2, and MT-CO2, and a membrane-trafficking neighborhood containing RAB10, RAB18, RAB21, RTN4, SEC22B, TMX1, and related genes. STRING independently supports organelle and membrane localization (4 supplementary STRING terms; within-query FDR 0.0033–0.0149), ER tubular-network involvement (STRING COMPARTMENTS Endoplasmic reticulum tubular network; within-query FDR = 0.0149) (STRING Component Endoplasmic reticulum tubular network; within-query FDR = 0.0211), mitochondrial inner-membrane and respiratory functions (STRING Keyword Mitochondrion inner membrane; within-query FDR = 0.0384) (STRING RCTM The citric acid (TCA) cycle and respiratory electron transport; within-query FDR = 0.0408) (STRING Keyword Electron transport; within-query FDR = 0.0426), and intracellular transport (STRING Keyword Transport; within-query FDR = 0.0426). Thus, the module most plausibly represents coordinated organelle maintenance, oxidative metabolism, and membrane or vesicle trafficking rather than a narrowly specialized pathway.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module. The HPA annotations place many members in mitochondria or the ER, and the individual secretome annotations are predominantly intracellular or membrane-associated. The module is also not strongly immune-specific overall, although HPA identifies cell-type enhancement in neutrophils, basophils, spermatids, epithelial cells, and several digestive or reproductive cell populations. Low tissue specificity for many genes, together with enhanced expression in muscle, tongue, liver, prostate, and choroid plexus, is consistent with broadly reusable cellular machinery. The shared lung-testis signal could therefore reflect common organelle activity or shared cell states, and a contribution from differing cell composition in the tissue samples cannot be excluded. The spermatid and neutrophil signals deserve particular caution when interpreting the cross-tissue conservation.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC organelle membrane | 0.00942 | ATP5F1C, GNA11, GNAI3, MT-CO2, RAB10, RAB18, RAB21, RDH11, RTN4, SEC22B, SFXN1, TAMM41, TMX1, UQCRC1, UQCRC2 |
| GO:CC endoplasmic reticulum tubular network | 0.0185 | RAB10, RAB18, RTN4 |
| GO:BP endoplasmic reticulum tubular network organization | 0.0487 | RAB10, RAB18, RTN4 |

### STRING and hu.MAP

STRING provides a coherent but incomplete set of established relationships. The strongest evidence is concentrated among the respiratory and metabolic genes: UQCRC1 and UQCRC2 connect strongly with one another and with MT-CO2, while ATP5F1C and CS connect this respiratory neighborhood to ATP synthesis and the citric-acid cycle. CS and ME2 are also supported as a metabolic pair. The absence of STRING links for several membrane-trafficking genes means that their co-abundance relationships are not necessarily established physical interactions. hu.MAP independently places MT-CO2, UQCRC1, and UQCRC2 in respiratory-chain complexes (hu.MAP huMAP3_10623.1) (hu.MAP huMAP3_00773.1) (hu.MAP huMAP3_08546.1) (hu.MAP huMAP3_09600.1) (hu.MAP huMAP3_12621.1), and places GNAI3 with GNA11 in G-protein complexes (hu.MAP huMAP3_13105.1)(hu.MAP huMAP3_11173.1). These results support known molecular substructures embedded within the module, while the full cross-compartment co-abundance architecture is broader than the currently catalogued complexes.

**STRING interactions (score >= 0.7)**: 9 of 153 gene pairs: ATP5F1C–CS (0.726); ATP5F1C–UQCRC1 (0.955); ATP5F1C–UQCRC2 (0.98); CS–ME2 (0.975); CS–UQCRC1 (0.71); CS–UQCRC2 (0.746); MT-CO2–UQCRC1 (0.979); MT-CO2–UQCRC2 (0.999); UQCRC1–UQCRC2 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Organelle membrane (FDR = 0.0033, 15 genes); Keyword Membrane (FDR = 0.0055, 15 genes); COMPARTMENTS Organelle membrane (FDR = 0.0089, 13 genes); COMPARTMENTS Membrane (FDR = 0.0149, 15 genes); COMPARTMENTS Endoplasmic reticulum tubular network (FDR = 0.0149, 3 genes); Component Endoplasmic reticulum tubular network (FDR = 0.0211, 3 genes); Keyword Mitochondrion inner membrane (FDR = 0.0384, 6 genes); RCTM The citric acid (TCA) cycle and respiratory electron transport (FDR = 0.0408, 6 genes); Keyword Electron transport (FDR = 0.0426, 4 genes); Keyword Transport (FDR = 0.0426, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10623.1 (MT-CO2, UQCRC2, UQCRC1; 3/24); huMAP3_00773.1 (MT-CO2, UQCRC2; 2/3); huMAP3_08546.1 (UQCRC2, UQCRC1; 2/9); huMAP3_09600.1 (UQCRC2, UQCRC1; 2/9); huMAP3_12621.1 (UQCRC2, UQCRC1; 2/22); huMAP3_13105.1 (GNAI3, GNA11; 2/27); huMAP3_12457.1 (UQCRC2, UQCRC1; 2/31); huMAP3_11173.1 (GNAI3, GNA11; 2/34)

### Novelty

The module should not be claimed as a newly discovered molecular complex. Its mitochondrial respiratory relationships, ER organization genes, vesicle-trafficking genes, and G-protein components have established biological interpretations, and several member pairs or groups are already represented in STRING or hu.MAP. Nevertheless, the conserved co-abundance of these components across lung and testis may be a potentially informative systems-level observation, particularly because the module links respiratory metabolism with ER and vesicle organization. That cross-tissue co-abundance configuration could be novel, but novelty would require comparison with published tissue co-expression modules and independent replication. Absence of an interaction from STRING or hu.MAP alone is not evidence that the relationship or module is novel.

**Hypothesis.** Hypothesis: the module coordinates energetic support with membrane remodeling and intracellular trafficking in cells that require substantial organelle activity. Mitochondrial respiratory and metabolic proteins may provide the energy and membrane-lipid context needed for ER maintenance, vesicle transport, and receptor or cargo trafficking. RAB10, RAB18, RAB21, RTN4, and SEC22B could link ER shape and vesicle flow to this metabolic state, while GNA11 and GNAI3 may couple membrane signaling to the response. In testis, this program may be expressed in developing germ cells or associated epithelial populations; in lung, it may reflect epithelial or other metabolically active cells. This is a mechanistic hypothesis, not a demonstrated causal pathway, and it should be tested using cell-resolved data, perturbation of the trafficking or respiratory components, and independent lung and testis cohorts.

### Important genes

#### UQCRC1

- **Related proteins** (co-abundance neighbors): UQCRC2 (0.87), CS (0.82); STRING partners: ATP5F1C (0.955), CS (0.71), MT-CO2 (0.979), UQCRC2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_10623.1, huMAP3_08546.1, huMAP3_09600.1, huMAP3_12621.1, huMAP3_12457.1
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase core protein 1. Enables ubiquitin protein ligase binding activity. Predicted to be involved in oxidative phosphorylation. Predicted to act upstream of or within mitochondrial electron transport, ubiquinol to cytochrome c. Located in mitochondrion. Implicated in Alzheimer's disease. Biomarker of Alzheimer's disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: parkinsonism with polyneuropathy (0.642); neurodegenerative disease (0.569); Parkinson disease (0.521); Alzheimer disease (0.519); lysosomal storage disease (0.498)
- **Europe PMC papers**: 1860
- **Why important**: UQCRC1 is a central representative of the mitochondrial respiratory submodule, connects in the co-abundance network to UQCRC2 and CS, has multiple high-confidence STRING relationships with respiratory proteins, and appears in several hu.MAP respiratory complexes (hu.MAP huMAP3_10623.1)(hu.MAP huMAP3_08546.1) (hu.MAP huMAP3_09600.1) (hu.MAP huMAP3_12621.1)(hu.MAP huMAP3_12457.1). Its HPA profile is enhanced in metabolically active tissues and in several epithelial and spermatid populations. It has established links to oxidative phosphorylation and mitochondrial electron transport, disease associations involving neurodegeneration and Parkinson disease, and a substantial literature base.
- **Conclusion**: Established evidence supports UQCRC1 as a respiratory-chain and mitochondrial component that helps anchor the module's organelle-energy interpretation. Its network placement supports module membership but does not establish that it regulates the ER or trafficking branch. A possible role as an energetic coordinator is therefore a hypothesis.

#### UQCRC2

- **Related proteins** (co-abundance neighbors): UQCRC1 (0.87), MT-CO2 (0.82); STRING partners: ATP5F1C (0.98), CS (0.746), MT-CO2 (0.999), UQCRC1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_10623.1, huMAP3_00773.1, huMAP3_08546.1, huMAP3_09600.1, huMAP3_12621.1, huMAP3_12457.1
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase core protein 2. The protein encoded by this gene is located in the mitochondrion, where it is part of the ubiquinol-cytochrome c reductase complex (also known as complex III). This complex constitutes a part of the mitochondrial respiratory chain. Defects in this gene are a cause of mitochondrial complex III deficiency nuclear type 5. [provided by RefSeq, Jul 2015].
- **Diseases (Open Targets)**: mitochondrial complex III deficiency (0.732); neurodegenerative disease (0.423); mitochondrial disease (0.312); gastric cancer (0.085); adrenoleukodystrophy (0.075)
- **Europe PMC papers**: 3297
- **Why important**: UQCRC2 is tightly connected to UQCRC1 and MT-CO2 in the module and has strong STRING support with ATP5F1C, CS, MT-CO2, and UQCRC1. It recurs across multiple hu.MAP respiratory complexes (hu.MAP huMAP3_10623.1) (hu.MAP huMAP3_00773.1) (hu.MAP huMAP3_08546.1) (hu.MAP huMAP3_09600.1) (hu.MAP huMAP3_12621.1)(hu.MAP huMAP3_12457.1). Its annotation directly places it in mitochondrial complex III, and its disease associations include mitochondrial complex III deficiency and broader mitochondrial disease. It is among the more extensively studied genes in the module.
- **Conclusion**: Established evidence identifies UQCRC2 as a core respiratory-chain constituent and a strong marker of the mitochondrial branch. Its presence explains part of the module's reproducible organelle signal. Any claim that UQCRC2 drives cross-talk with ER trafficking remains a hypothesis rather than a demonstrated function.

#### RAB18

- **Related proteins** (co-abundance neighbors): TAMM41 (0.84), RAB21 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB18, member RAS oncogene family. The protein encoded by this gene is a member of a family of Ras-related small GTPases that regulate membrane trafficking in organelles and transport vesicles. Knockdown studies is zebrafish suggest that this protein may have a role in eye and brain development. Mutations in this gene are associated with Warburg micro syndrome type 3. Alternatively spliced transcript variants have been found for th…
- **Diseases (Open Targets)**: Warburg micro syndrome (0.815); neurodegenerative disease (0.496); cerebral atherosclerosis (0.275); malunion fracture (0.239); adolescent idiopathic scoliosis (0.229)
- **Europe PMC papers**: 2168
- **Why important**: RAB18 is one of the genes contributing directly to all primary ER tubular-network terms (GO:CC organelle membrane; q_global = 0.00942) (GO:CC endoplasmic reticulum tubular network; q_global = 0.0185) (GO:BP endoplasmic reticulum tubular network organization; q_global = 0.0487), and it connects the ER-related branch to TAMM41 and RAB21 in the co-abundance network. STRING independently supports its ER tubular-network association (STRING COMPARTMENTS Endoplasmic reticulum tubular network; within-query FDR = 0.0149)(STRING Component Endoplasmic reticulum tubular network; within-query FDR = 0.0211) and membrane transport context (STRING Keyword Transport; within-query FDR = 0.0426). Its established functions include organelle and vesicle trafficking, lipid-droplet organization, and sterol homeostasis, with a disease association to Warburg micro syndrome. It has a substantial literature base.
- **Conclusion**: Established evidence supports RAB18 as a key marker of the ER and intracellular-trafficking interpretation and as an important bridge between membrane organization and lipid-related organelle biology. The hypothesis that it couples the ER branch to mitochondrial lipid or energy state is plausible from the module context but is not directly demonstrated here.

#### RTN4

- **Related proteins** (co-abundance neighbors): SFXN1 (0.82), SEC22B (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: reticulon 4. This gene belongs to the family of reticulon encoding genes. Reticulons are associated with the endoplasmic reticulum, and are involved in neuroendocrine secretion or in membrane trafficking in neuroendocrine cells. The product of this gene is a potent neurite outgrowth inhibitor which may also help block the regeneration of the central nervous system in higher vertebrates. Alternatively spliced t…
- **Diseases (Open Targets)**: obesity disorder (0.382); neurodegenerative disease (0.257); skin cancer (0.231); sensorineural hearing loss disorder (0.215); hearing loss disorder (0.210)
- **Europe PMC papers**: 2070
- **Why important**: RTN4 is one of the three genes defining the primary ER tubular-network enrichments (GO:CC endoplasmic reticulum tubular network; q_global = 0.0185)(GO:BP endoplasmic reticulum tubular network organization; q_global = 0.0487), is annotated to the ER, and connects in the module to SFXN1 and SEC22B. STRING independently supports its ER tubular-network membership (STRING COMPARTMENTS Endoplasmic reticulum tubular network; within-query FDR = 0.0149)(STRING Component Endoplasmic reticulum tubular network; within-query FDR = 0.0211). Its known functions include ER organization, membrane trafficking, neuroendocrine secretion, and regulation of cell migration, while disease associations include neurodegenerative and hearing-loss disorders. The gene has a substantial literature base.
- **Conclusion**: Established evidence makes RTN4 a strong structural and functional marker of the ER branch. It supports an interpretation involving ER morphology and trafficking rather than simply generic membrane abundance. Its proposed role in coordinating ER architecture with mitochondrial respiration is a hypothesis requiring experimental validation.

#### CS

- **Related proteins** (co-abundance neighbors): ME2 (0.86), ATP5F1C (0.83), UQCRC1 (0.82), RAB21 (0.81), SCCPDH (0.80); STRING partners: ATP5F1C (0.726), ME2 (0.975), UQCRC1 (0.71), UQCRC2 (0.746)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS has the highest weighted network connectivity in the module and links ME2, ATP5F1C, UQCRC1, RAB21, and SCCPDH. STRING supports its relationships with ME2, ATP5F1C, UQCRC1, and UQCRC2, and places it in the citric-acid-cycle and respiratory context (STRING RCTM The citric acid (TCA) cycle and respiratory electron transport; within-query FDR = 0.0408). Its established function is citrate synthesis in the mitochondrial matrix, and it is broadly relevant to oxidative metabolism with a very extensive literature base and disease associations involving neurodegenerative and autoimmune disorders.
- **Conclusion**: Established evidence supports CS as a metabolic hub that may explain why mitochondrial and membrane-trafficking genes co-vary in the module. Its high network position makes it important for interpretation, but co-abundance does not show that CS controls the trafficking genes. A role for metabolic flux in shaping the membrane program remains a hypothesis.

#### ATP5F1C

- **Related proteins** (co-abundance neighbors): CS (0.83); STRING partners: CS (0.726), UQCRC1 (0.955), UQCRC2 (0.98)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP synthase F1 subunit gamma. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: late-onset Alzheimers disease (0.350); scleritis (0.189); diaphragm disorder (0.082); glioblastoma (0.044); external ear disorder (0.042)
- **Europe PMC papers**: 306
- **Why important**: ATP5F1C connects the metabolic and respiratory portions of the module through CS and has strong STRING relationships with UQCRC1 and UQCRC2. It is included in the organelle-membrane primary evidence (GO:CC organelle membrane; q_global = 0.00942) and in the supplementary mitochondrial inner-membrane, respiratory, and transport annotations (STRING Component Organelle membrane; within-query FDR = 0.0033)(STRING Keyword Mitochondrion inner membrane; within-query FDR = 0.0384)(STRING RCTM The citric acid (TCA) cycle and respiratory electron transport; within-query FDR = 0.0408)(STRING Keyword Transport; within-query FDR = 0.0426). Its established function is as a subunit of mitochondrial ATP synthase, and it has disease and neurodegenerative associations with a growing literature base.
- **Conclusion**: Established evidence supports ATP5F1C as an indicator of oxidative-phosphorylation capacity and energy production within the module. It provides a plausible energetic link to trafficking and ER maintenance, but a direct causal connection to those processes is a hypothesis.

## Module 8

**Tissue pair**: lung and testis  
**Genes (23)**: CCAR1, DDX42, DDX46, DNM1L, GMPS, HSPA8, EIF4G1, EIF5, IMPDH2, MCM2, MRE11, NASP, GART, PFAS, RBM39, SF3B3, SHTN1, SRP68, SRP72, SRRT, TARS1, TXNRD1, SNRNP200

### Function

The strongest interpretation is a conserved intracellular RNA-processing and gene-expression module. Primary evidence shows broad nucleic-acid and RNA binding (GO:MF nucleic acid binding; q_global = 0.000524)(GO:MF RNA binding; q_global = 0.00179), ribonucleoprotein organization (GO:CC ribonucleoprotein complex; q_global = 0.00713), mRNA processing and spliceosomal activity (KEGG Spliceosome - Homo sapiens (human); q_global = 0.0181)(GO:BP mRNA processing; q_global = 0.0226)(GO:BP RNA splicing, via transesterification reactions; q_global = 0.0271)(GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 0.0271)(GO:BP mRNA splicing, via spliceosome; q_global = 0.0271)(GO:CC spliceosomal complex; q_global = 0.034)(GO:BP spliceosomal complex assembly; q_global = 0.0355)(GO:CC U2-type spliceosomal complex; q_global = 0.0447), and helicase or nucleic-acid conformational activities (GO:MF helicase activity; q_global = 0.0252)(GO:MF nucleic acid conformation isomerase activity; q_global = 0.0391). DDX42, DDX46, SF3B3 and SNRNP200 form the clearest spliceosomal core, while EIF4G1, EIF5, SRP68, SRP72 and TARS1 connect RNA handling with translation and protein-targeting functions. A second coherent arm is nucleotide metabolism: GART, PFAS, IMPDH2 and GMPS support purine and GMP biosynthesis (GO:BP GMP biosynthetic process; q_global = 0.0107)(GO:BP purine ribonucleoside monophosphate biosynthetic process; q_global = 0.0274)(GO:BP purine nucleoside monophosphate biosynthetic process; q_global = 0.0355)(GO:BP GMP metabolic process; q_global = 0.0355). Thus, the module most plausibly reflects coordinated RNA maturation, translation-related RNA handling, and the nucleotide supply required for proliferating or metabolically active cells. The broad nucleobase-compound signal (GO:BP nucleobase-containing compound metabolic process; q_global = 0.0396) supports this integrated interpretation, but does not by itself establish direct biochemical coupling between every arm.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes, and most proteins are intracellular, nuclear, cytosolic or organellar. The module is broadly expressed by HPA, with many genes showing low tissue specificity and low immune-cell specificity. Therefore, it does not look primarily like a blood-contamination signature, although isolated HPA associations with erythroid, myeloid or lymphoid populations warrant attention. Several genes are enhanced in spermatogenic cell types, and some are enhanced in bone marrow or testis, which could contribute to the shared lung–testis signal through proliferative or germ-cell-like programs. Detection of most module proteins in both lung and testis is consistent with a shared cellular housekeeping program rather than a lung-specific or testis-specific secretory program. MCM2 is not detected in lung in the supplied HPA evidence, and SHTN1 is detected in testis but not lung, so the module may also contain tissue-dependent or cell-composition components.

**GO/KEGG enrichment**: 18 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleic acid binding | 0.000524 | CCAR1, DDX42, DDX46, EIF4G1, EIF5, HSPA8, IMPDH2, MCM2, MRE11, RBM39, SF3B3, SNRNP200, SRP68, SRP72, SRRT, TARS1 |
| GO:MF RNA binding | 0.00179 | CCAR1, DDX42, DDX46, EIF4G1, EIF5, HSPA8, IMPDH2, RBM39, SF3B3, SNRNP200, SRP68, SRP72, SRRT, TARS1 |
| GO:CC ribonucleoprotein complex | 0.00713 | DDX42, DDX46, HSPA8, SF3B3, SNRNP200, SRP68, SRP72, SRRT |
| GO:BP GMP biosynthetic process | 0.0107 | GART, GMPS, IMPDH2, PFAS |
| KEGG Spliceosome - Homo sapiens (human) | 0.0181 | DDX42, DDX46, HSPA8, SF3B3, SNRNP200 |
| GO:BP mRNA processing | 0.0226 | DDX42, DDX46, HSPA8, RBM39, SF3B3, SNRNP200, SRRT |
| GO:MF helicase activity | 0.0252 | DDX42, DDX46, MCM2, MRE11, SNRNP200 |
| GO:BP RNA splicing, via transesterification reactions | 0.0271 | DDX42, DDX46, HSPA8, RBM39, SF3B3, SNRNP200 |
| GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile | 0.0271 | DDX42, DDX46, HSPA8, RBM39, SF3B3, SNRNP200 |
| GO:BP mRNA splicing, via spliceosome | 0.0271 | DDX42, DDX46, HSPA8, RBM39, SF3B3, SNRNP200 |
| GO:BP purine ribonucleoside monophosphate biosynthetic process | 0.0274 | GART, GMPS, IMPDH2, PFAS |
| GO:CC spliceosomal complex | 0.034 | DDX42, DDX46, HSPA8, SF3B3, SNRNP200 |
| GO:BP spliceosomal complex assembly | 0.0355 | DDX42, DDX46, SF3B3, SNRNP200 |
| GO:BP purine nucleoside monophosphate biosynthetic process | 0.0355 | GART, GMPS, IMPDH2, PFAS |
| GO:BP GMP metabolic process | 0.0355 | GART, GMPS, IMPDH2, PFAS |

### STRING and hu.MAP

STRING supports a structured, partly known network rather than an arbitrary correlation set. Strong links connect DDX42, DDX46, SF3B3 and SNRNP200 in the spliceosomal arm; GART, PFAS, IMPDH2 and GMPS in the purine-biosynthesis arm; EIF4G1 with EIF5 and HSPA8 in translation-related functions; and SRP68 with SRP72 in the signal-recognition-particle complex. STRING functional results independently support mRNA splicing, RNA metabolism, ribonucleoprotein complexes and purine biosynthesis (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 3.75e-05)(STRING Keyword Purine biosynthesis; within-query FDR = 0.0023)(STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.0024)(STRING RCTM Metabolism of RNA; within-query FDR = 0.0029)(STRING RCTM Purine ribonucleoside monophosphate biosynthesis; within-query FDR = 0.0037)(STRING KEGG Spliceosome; within-query FDR = 0.0084). These STRING results are supplementary and do not replace the globally corrected enrichment evidence. hu.MAP provides direct complex context for the spliceosomal quartet in the large spliceosomal complex (hu.MAP huMAP3_08980.1), for the DDX42–DDX46–SF3B3 group in additional spliceosomal complexes (hu.MAP huMAP3_04549.1)(hu.MAP huMAP3_06511.1), for GART and PFAS in purine-related complexes (hu.MAP huMAP3_03291.1)(hu.MAP huMAP3_00676.1), and for NASP with MCM2 in a chromatin and histone-associated complex (hu.MAP huMAP3_10747.1). The module therefore recapitulates several established molecular assemblies, while its cross-arm co-abundance structure extends beyond any single known complex.

**STRING interactions (score >= 0.7)**: 15 of 253 gene pairs: CCAR1–RBM39 (0.875); CCAR1–SRRT (0.857); DDX42–SF3B3 (0.995); DDX46–SF3B3 (0.997); DDX46–SNRNP200 (0.874); EIF4G1–EIF5 (0.99); EIF4G1–HSPA8 (0.97); GART–GMPS (0.937); GART–IMPDH2 (0.811); GART–PFAS (0.999); GMPS–IMPDH2 (0.998); HSPA8–SRRT (0.737); RBM39–SRRT (0.936); SF3B3–SNRNP200 (0.999); SRP68–SRP72 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Ubl conjugation (FDR = 1.61e-07, 16 genes); Keyword Isopeptide bond (FDR = 1.31e-06, 14 genes); RCTM mRNA Splicing - Major Pathway (FDR = 3.75e-05, 8 genes); Function Nucleic acid binding (FDR = 0.00029, 16 genes); Function RNA binding (FDR = 0.00029, 14 genes); Function Organic cyclic compound binding (FDR = 0.00029, 21 genes); Function Heterocyclic compound binding (FDR = 0.00029, 21 genes); Keyword Phosphoprotein (FDR = 0.0022, 23 genes); Keyword Purine biosynthesis (FDR = 0.0023, 4 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 0.0024, 8 genes); RCTM Metabolism of RNA (FDR = 0.0029, 9 genes); RCTM Purine ribonucleoside monophosphate biosynthesis (FDR = 0.0037, 4 genes); Component Ribonucleoprotein complex (FDR = 0.0077, 8 genes); KEGG Spliceosome (FDR = 0.0084, 5 genes); TISSUES Leukemia cell (FDR = 0.0098, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (SNRNP200, SF3B3, DDX46, DDX42; 4/97); huMAP3_04549.1 (SF3B3, DDX46, DDX42; 3/52); huMAP3_03291.1 (PFAS, GART; 2/3); huMAP3_00676.1 (PFAS, GART; 2/4); huMAP3_10747.1 (NASP, MCM2; 2/25); huMAP3_06511.1 (SF3B3, DDX46; 2/79)

### Novelty

The individual biology is not a new discovery: spliceosomal roles of DDX42, DDX46, SF3B3 and SNRNP200, purine-biosynthetic roles of GART, PFAS, IMPDH2 and GMPS, and the relevant STRING and hu.MAP relationships are already established. The potentially novel result is the conserved co-abundance organization of these processes across lung and testis, particularly the coupling of spliceosomal RNA processing, purine production, translation-related factors, chromatin handling and mitochondrial or redox-associated components. The supplied search found no direct external result for this exact module or gene combination, but that absence is weak evidence and cannot establish novelty. A defensible claim is therefore that the cross-tissue co-abundance configuration is a candidate new systems-level observation requiring replication, comparison with published tissue coexpression resources, and validation at the protein and cell-type levels.

**Hypothesis.** Hypothesis: this module represents a shared demand-response program in cells with active RNA production, RNA maturation, translation and proliferation. Spliceosomal factors may coordinate transcript processing, while purine-pathway enzymes maintain nucleotide pools needed for transcription, replication and RNA metabolism. NASP and MCM2 may connect this program to chromatin assembly and cell-cycle activity, and EIF4G1, EIF5, SRP68 and SRP72 may couple processed transcripts to translation and protein targeting. In testis, the program could be amplified by spermatogenic differentiation; in lung, it could arise from proliferative or metabolically active epithelial and stromal cell subsets. This remains a hypothesis: co-abundance does not demonstrate physical interaction, causal regulation, or a common cell type.

### Important genes

#### DDX46

- **Related proteins** (co-abundance neighbors): DDX42 (0.86), MRE11 (0.86), NASP (0.83), SRRT (0.81), GMPS (0.80); STRING partners: SF3B3 (0.997), SNRNP200 (0.874)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_04549.1, huMAP3_06511.1
- **Function (MyGene.info)**: DEAD-box helicase 46. This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribu…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); dengue disease (0.370); Hypercholesterolemia (0.203); lung adenocarcinoma (0.074); osteosarcoma (0.053)
- **Europe PMC papers**: 592
- **Why important**: DDX46 is a central RNA-processing candidate with substantial weighted connectivity and links to DDX42, SF3B3, SNRNP200, NASP, SRRT and GMPS. It appears across the primary nucleic-acid, RNA-binding, ribonucleoprotein, spliceosome, mRNA-processing, helicase and RNA-splicing terms (GO:MF nucleic acid binding; q_global = 0.000524)(GO:MF RNA binding; q_global = 0.00179)(GO:CC ribonucleoprotein complex; q_global = 0.00713)(KEGG Spliceosome - Homo sapiens (human); q_global = 0.0181)(GO:BP mRNA processing; q_global = 0.0226)(GO:MF helicase activity; q_global = 0.0252)(GO:BP RNA splicing, via transesterification reactions; q_global = 0.0271)(GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 0.0271)(GO:BP mRNA splicing, via spliceosome; q_global = 0.0271)(GO:CC spliceosomal complex; q_global = 0.034)(GO:BP spliceosomal complex assembly; q_global = 0.0355)(GO:MF nucleic acid conformation isomerase activity; q_global = 0.0391)(GO:BP nucleobase-containing compound metabolic process; q_global = 0.0396)(GO:CC U2-type spliceosomal complex; q_global = 0.0447). It is supported by multiple hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1)(hu.MAP huMAP3_04549.1)(hu.MAP huMAP3_06511.1) and strong STRING links to SF3B3 and SNRNP200. Its literature volume is substantial, and its supplied function directly supports RNA structural remodeling and U2 prespliceosome assembly.
- **Conclusion**: Established evidence supports DDX46 as a spliceosome-associated RNA helicase and a major connector of the module. The module-level hypothesis is that DDX46 helps couple spliceosomal activity to the broader metabolic and translational state, but that coupling is not established by the supplied data.

#### SF3B3

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.84), NASP (0.82), IMPDH2 (0.81); STRING partners: DDX42 (0.995), DDX46 (0.997), SNRNP200 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Nucleoli rim; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_04549.1, huMAP3_06511.1
- **Function (MyGene.info)**: splicing factor 3b subunit 3. This gene encodes subunit 3 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); dengue disease (0.370); cervical cancer (0.189); cervical carcinoma (0.189); prostate cancer (0.111)
- **Europe PMC papers**: 965
- **Why important**: SF3B3 is a core spliceosomal scaffold with primary enrichment across RNA binding, ribonucleoprotein complexes, mRNA processing and spliceosomal terms (GO:MF nucleic acid binding; q_global = 0.000524)(GO:MF RNA binding; q_global = 0.00179)(GO:CC ribonucleoprotein complex; q_global = 0.00713)(KEGG Spliceosome - Homo sapiens (human); q_global = 0.0181)(GO:BP mRNA processing; q_global = 0.0226)(GO:BP RNA splicing, via transesterification reactions; q_global = 0.0271)(GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 0.0271)(GO:BP mRNA splicing, via spliceosome; q_global = 0.0271)(GO:CC spliceosomal complex; q_global = 0.034)(GO:BP spliceosomal complex assembly; q_global = 0.0355)(GO:BP nucleobase-containing compound metabolic process; q_global = 0.0396)(GO:CC U2-type spliceosomal complex; q_global = 0.0447). It has strong STRING relationships with DDX42, DDX46 and SNRNP200 and is present in several hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1)(hu.MAP huMAP3_04549.1)(hu.MAP huMAP3_06511.1). Its nuclear localization and extensive literature on U2 snRNP and spliceosome function make it a strong mechanistic anchor.
- **Conclusion**: Established evidence identifies SF3B3 as a core component of the RNA-splicing arm. It is plausible that its co-abundance marks coordinated spliceosome abundance or activity across the tissues, but co-abundance alone cannot establish altered splicing or direct regulation.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): SF3B3 (0.84), EIF4G1 (0.81); STRING partners: DDX46 (0.874), SF3B3 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is a U5 snRNP helicase and a high-confidence member of the spliceosomal network. It is represented in the primary nucleic-acid, RNA-binding, ribonucleoprotein, spliceosome, mRNA-processing, helicase and RNA-splicing evidence (GO:MF nucleic acid binding; q_global = 0.000524)(GO:MF RNA binding; q_global = 0.00179)(GO:CC ribonucleoprotein complex; q_global = 0.00713)(KEGG Spliceosome - Homo sapiens (human); q_global = 0.0181)(GO:BP mRNA processing; q_global = 0.0226)(GO:MF helicase activity; q_global = 0.0252)(GO:BP RNA splicing, via transesterification reactions; q_global = 0.0271)(GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 0.0271)(GO:BP mRNA splicing, via spliceosome; q_global = 0.0271)(GO:CC spliceosomal complex; q_global = 0.034)(GO:BP spliceosomal complex assembly; q_global = 0.0355)(GO:MF nucleic acid conformation isomerase activity; q_global = 0.0391)(GO:BP nucleobase-containing compound metabolic process; q_global = 0.0396)(GO:CC U2-type spliceosomal complex; q_global = 0.0447). It has a very strong STRING relationship with SF3B3, an additional relationship with DDX46, and membership in hu.MAP spliceosomal complex (hu.MAP huMAP3_08980.1). Its disease associations include retinal degeneration categories, and its literature is substantial.
- **Conclusion**: Established evidence supports SNRNP200 as a core catalytic-remodeling component of the spliceosome and an important marker of this module's RNA-processing identity. A possible tissue-shared role in maintaining transcript maturation under high cellular demand remains a hypothesis.

#### GMPS

- **Related proteins** (co-abundance neighbors): PFAS (0.87), IMPDH2 (0.85), HSPA8 (0.81), EIF4G1 (0.80), DDX46 (0.80); STRING partners: GART (0.937), IMPDH2 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: guanosine monophosphate synthase. In the de novo synthesis of purine nucleotides, IMP is the branch point metabolite at which point the pathway diverges to the synthesis of either guanine or adenine nucleotides. In the guanine nucleotide pathway, there are 2 enzymes involved in converting IMP to GMP, namely IMP dehydrogenase (IMPD1), which catalyzes the oxidation of IMP to XMP, and GMP synthetase, which catalyzes the amination of …
- **Diseases (Open Targets)**: rheumatoid arthritis (0.277); nephrotic syndrome (0.259); lupus nephritis (0.259); rhabdomyosarcoma (0.247); hepatocellular carcinoma (0.237)
- **Europe PMC papers**: 5161
- **Why important**: GMPS is the most direct representative of the GMP-biosynthesis arm. It participates in all primary purine and GMP terms (GO:BP GMP biosynthetic process; q_global = 0.0107)(GO:BP purine ribonucleoside monophosphate biosynthetic process; q_global = 0.0274)(GO:BP purine nucleoside monophosphate biosynthetic process; q_global = 0.0355)(GO:BP GMP metabolic process; q_global = 0.0355)(GO:BP nucleobase-containing compound metabolic process; q_global = 0.0396), has strong STRING links to IMPDH2 and GART, and is connected in the module to PFAS, EIF4G1, HSPA8 and DDX46. HPA describes testis-enhanced expression and enhancement in spermatogenic cell types. Its biochemical role is well established and its literature volume is extensive, including disease-related work in inflammatory and neoplastic contexts.
- **Conclusion**: Established evidence supports GMPS as a functional purine-pathway enzyme and a bridge between the metabolic arm and the rest of the module. The idea that GMP production is coordinated with spliceosome demand in the shared tissues is a mechanistic hypothesis, not a demonstrated causal relationship.

#### NASP

- **Related proteins** (co-abundance neighbors): MCM2 (0.87), SRRT (0.86), HSPA8 (0.85), DDX46 (0.83), SF3B3 (0.82), EIF4G1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_10747.1
- **Function (MyGene.info)**: nuclear autoantigenic sperm protein. This gene encodes a H1 histone binding protein that is involved in transporting histones into the nucleus of dividing cells. Multiple isoforms are encoded by transcript variants of this gene. The somatic form is expressed in all mitotic cells, is localized to the nucleus, and is coupled to the cell cycle. The testicular form is expressed in embryonic tissues, tumor cells, and the testis. In male g…
- **Diseases (Open Targets)**: neurodegenerative disease (0.445); Paralytic ileus (0.301); glioma (0.080); central nervous system cancer (0.080); hepatocellular carcinoma (0.076)
- **Europe PMC papers**: 1349
- **Why important**: NASP is a highly connected module gene linking MCM2, SRRT, HSPA8, DDX46, SF3B3 and EIF4G1. It contributes to the globally corrected nucleobase-compound process (GO:BP nucleobase-containing compound metabolic process; q_global = 0.0396) and to the supplementary ubiquitin-related and phosphoprotein signals (STRING Keyword Ubl conjugation; within-query FDR = 1.61e-07)(STRING Keyword Isopeptide bond; within-query FDR = 1.31e-06)(STRING Keyword Phosphoprotein; within-query FDR = 0.0022). hu.MAP places NASP with MCM2 in a chromatin and histone-associated complex (hu.MAP huMAP3_10747.1). HPA shows enhancement in differentiating spermatogonia, early primary spermatocytes and erythrocyte progenitors, while the supplied function connects it to histone transport, chromatin assembly and the cell cycle.
- **Conclusion**: Established evidence supports NASP as a histone-handling and chromatin-associated factor that may explain part of the shared proliferative or germ-cell-associated signal. Its role as a bridge between chromatin state, RNA processing and purine demand is plausible but remains unproven in this module.

## Module 9

**Tissue pair**: lung and testis  
**Genes (5)**: COL1A2, COL6A1, COL6A3, FBN1, BGN

### Function

This is a conserved extracellular-matrix structural module shared by lung and testis. The primary evidence is exceptionally coherent: every module gene supports extracellular-matrix structural constituent, external encapsulating structure, and extracellular matrix annotations (GO:MF extracellular matrix structural constituent; q_global = 7.06e-05) (GO:CC external encapsulating structure; q_global = 9.29e-05) (GO:CC extracellular matrix; q_global = 9.29e-05), while all genes also support structural molecule activity (GO:MF structural molecule activity; q_global = 0.00899). COL1A2, COL6A1, and COL6A3 support tensile-strength matrix and collagen-trimer annotations (GO:MF extracellular matrix structural constituent conferring tensile strength; q_global = 0.00151) (GO:CC complex of collagen trimers; q_global = 0.00151) (GO:CC collagen trimer; q_global = 0.0066), with COL6A1 and COL6A3 supporting collagen type VI trimer and beaded-filament annotations (4 globally significant GO/KEGG terms, q_global 0.0144–0.0144; see the table). Integrin signaling and ECM-receptor interaction (KEGG Integrin signaling - Homo sapiens (human); q_global = 0.00251) (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0272) indicate that the matrix is not merely structural but can participate in cell–matrix signaling. The skeletal, bone, and lung-alveolus development terms (GO:BP skeletal system development; q_global = 0.00489) (GO:BP bone development; q_global = 0.0272) (GO:BP lung alveolus development; q_global = 0.0342) are consistent with connective-tissue organization and tissue remodeling, rather than implying that the module is specific to bone or alveolar cells. The endoplasmic-reticulum-lumen annotation (GO:CC endoplasmic reticulum lumen; q_global = 0.0408) is compatible with synthesis and processing of secreted matrix proteins.

**Cell composition.** All module genes are secreted extracellular-matrix proteins according to HPA, and all are not detected in immune cells. HPA single-cell annotations consistently implicate fibroblasts and hepatic stellate cells, with frequent support for Leydig cells, peritubular myoid cells, and fibro-adipogenic progenitors. This composition strongly favors stromal, connective-tissue, vascular-support, and gonadal somatic-cell biology rather than a blood-cell signal. The module is therefore not a plasma-protein or immune-cell module, although extracellular proteins in tissue samples can also reflect shared stromal-cell abundance or matrix deposition. HPA protein detection is concordant for some genes in lung and testis but is absent for others, so the co-abundance signal should not be interpreted as uniform protein detection across both organs. Tissue annotations include smooth muscle, blood vessel, adipose tissue, placenta, cervix, and ovary, supporting a broadly connective-tissue-associated program.

**GO/KEGG enrichment**: 19 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF extracellular matrix structural constituent | 7.06e-05 | BGN, COL1A2, COL6A1, COL6A3, FBN1 |
| GO:CC external encapsulating structure | 9.29e-05 | BGN, COL1A2, COL6A1, COL6A3, FBN1 |
| GO:CC extracellular matrix | 9.29e-05 | BGN, COL1A2, COL6A1, COL6A3, FBN1 |
| KEGG Cytoskeleton in muscle cells - Homo sapiens (human) | 0.000286 | BGN, COL1A2, COL6A1, COL6A3, FBN1 |
| GO:MF extracellular matrix structural constituent conferring tensile strength | 0.00151 | COL1A2, COL6A1, COL6A3 |
| GO:CC complex of collagen trimers | 0.00151 | COL1A2, COL6A1, COL6A3 |
| KEGG Integrin signaling - Homo sapiens (human) | 0.00251 | COL1A2, COL6A1, COL6A3, FBN1 |
| GO:BP skeletal system development | 0.00489 | BGN, COL1A2, COL6A1, FBN1 |
| KEGG Protein digestion and absorption - Homo sapiens (human) | 0.00522 | COL1A2, COL6A1, COL6A3 |
| GO:CC collagen trimer | 0.0066 | COL1A2, COL6A1, COL6A3 |
| GO:MF structural molecule activity | 0.00899 | BGN, COL1A2, COL6A1, COL6A3, FBN1 |
| GO:CC collagen type VI trimer | 0.0144 | COL6A1, COL6A3 |
| GO:CC collagen beaded filament | 0.0144 | COL6A1, COL6A3 |
| GO:CC basement membrane/interstitial matrix interface | 0.0144 | COL6A1, COL6A3 |
| GO:CC von-Willerbrand-factor-A-domain-rich collagen trimer | 0.0144 | COL6A1, COL6A3 |

### STRING and hu.MAP

STRING reports high-confidence relationships among every possible gene pair in the module. The strongest known relationships include the collagen-VI association between COL6A1 and COL6A3, links of COL1A2 to COL6A3 and FBN1, and additional links involving BGN. This dense STRING structure agrees with the primary GO/KEGG results and indicates that the module recapitulates a biologically coherent extracellular-matrix network rather than a collection of unrelated genes. The STRING functional results (15 supplementary STRING terms; within-query FDR 4.03e-06–1.94e-05) independently support extracellular-matrix organization, collagen-containing matrix, connective-tissue phenotypes, and fibroblast-associated biology, but they are supplementary and are not treated as globally corrected module-enrichment evidence. No hu.MAP complex contains at least two module members, so the evidence supports a connected matrix network and shared extracellular biology rather than a documented hu.MAP intracellular complex.

**STRING interactions (score >= 0.7)**: 10 of 10 gene pairs: BGN–COL1A2 (0.938); BGN–COL6A1 (0.86); BGN–COL6A3 (0.806); BGN–FBN1 (0.784); COL1A2–COL6A1 (0.875); COL1A2–COL6A3 (0.968); COL1A2–FBN1 (0.965); COL6A1–COL6A3 (0.994); COL6A1–FBN1 (0.743); COL6A3–FBN1 (0.786)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Extracellular matrix structural constituent (FDR = 4.03e-06, 5 genes); Keyword Extracellular matrix (FDR = 5.11e-06, 5 genes); PMID (2022) Identifying miRNAs Associated with the Progression of Keloid through mRNA-miRNA Network Analysis and Validating the Targets of miR-29a-3p in Keloid Fibroblasts. (FDR = 6.23e-06, 5 genes); PMID (2023) Case report: Two individuals with AEBP1-related classical-like EDS: Further clinical characterisation and description of novel AEBP1 variants. (FDR = 1.06e-05, 5 genes); PMID (2023) The entanglement of extracellular matrix molecules and immune checkpoint inhibitors in cancer: a systematic review of the literature. (FDR = 1.06e-05, 5 genes); PMID (2018) Subpopulations of dermal skin fibroblasts secrete distinct extracellular matrix: implications for using skin substitutes in the clinic. (FDR = 1.06e-05, 5 genes); PMID (2018) Identification of hub genes and potential molecular mechanisms in gastric cancer by integrated bioinformatics analysis. (FDR = 1.06e-05, 5 genes); PMID (2015) Connective tissue growth factor regulates cardiac function and tissue remodeling in a mouse model of dilated cardiomyopathy. (FDR = 1.06e-05, 5 genes); COMPARTMENTS External encapsulating structure (FDR = 1.6e-05, 5 genes); COMPARTMENTS Collagen-containing extracellular matrix (FDR = 1.6e-05, 5 genes); PMID (2022) Muscle fibro-adipogenic progenitors from a single-cell perspective: Focus on their virtual secretome. (FDR = 1.82e-05, 5 genes); NetworkNeighborAL Extracellular matrix organization (FDR = 1.87e-05, 5 genes); HPO Joint hypermobility (FDR = 1.94e-05, 5 genes); HPO Hyperlordosis (FDR = 1.94e-05, 5 genes); HPO Finger joint hypermobility (FDR = 1.94e-05, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be described as a newly discovered molecular function. Its genes, collagen relationships, extracellular-matrix annotations, and disease associations are already well established, and STRING strongly recapitulates the same biology. The potentially novel aspect is the conserved co-abundance pattern across lung and testis, particularly its apparent representation of a shared stromal or connective-tissue program. However, the fact sheet does not provide a comparison with previously published cross-tissue co-abundance modules, so it cannot establish that this module-level observation is new. The absence of a hu.MAP complex does not demonstrate novelty, because an extracellular matrix network need not form a hu.MAP molecular complex. Overall, this is best regarded as a biologically validated cross-tissue module with possible contextual novelty, not as a novel extracellular-matrix pathway.

**Hypothesis.** Hypothesis: the conserved module reflects coordinated abundance of matrix-producing stromal and perivascular or gonadal somatic cells in lung and testis. COL1A2 may provide fibrillar collagen scaffold, COL6A1 and COL6A3 may assemble collagen-VI beaded filaments, FBN1 may organize force-bearing microfibrils and matrix signaling context, and BGN may regulate collagen fibril assembly and matrix-cell communication. Their coordinated abundance could maintain tissue architecture and influence integrin-linked mechanotransduction, developmental remodeling, and repair. This hypothesis is consistent with the annotations and network structure, but co-abundance alone cannot distinguish coordinated secretion by the same stromal population from shared extracellular deposition or changes in cell composition.

### Important genes

#### COL6A1

- **Related proteins** (co-abundance neighbors): FBN1 (0.82), COL1A2 (0.81); STRING partners: BGN (0.86), COL1A2 (0.875), COL6A3 (0.994), FBN1 (0.743)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is among the most connected genes in the module and is linked in STRING to every other module member. It is a core collagen-VI chain, supports the collagen-VI trimer and beaded-filament annotations (4 globally significant GO/KEGG terms, q_global 0.0144–0.0144; see the table), and contributes to the collagen-containing extracellular matrix (12 globally significant GO/KEGG terms, q_global 7.06e-05–0.0408; see the table). HPA places it in fibroblast, fibro-adipogenic progenitor, and stromal-cell contexts. Its established associations with Bethlem and Ullrich congenital muscular dystrophies make it important for interpreting matrix integrity and tissue mechanics.
- **Conclusion**: Established evidence supports COL6A1 as a central structural component of the module and a collagen-VI disease gene. It is a strong candidate for the module's core scaffold. A specific lung–testis regulatory role remains a hypothesis rather than an established conclusion.

#### COL6A3

- **Related proteins** (co-abundance neighbors): BGN (0.85), COL1A2 (0.83); STRING partners: BGN (0.806), COL1A2 (0.968), COL6A1 (0.994), FBN1 (0.786)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 3 chain. This gene encodes the alpha-3 chain, one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The alpha-3 chain of type VI collagen is much larger than the alpha-1 and -2 chains. This difference in size is largely due to an increase in the number of subdomains, similar to von Willebrand Factor type A domains, that are found in the amino termin…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy (0.766); dystonia 27 (0.764); Bethlem myopathy (0.758); Bethlem myopathy 1C (0.747); Bethlem myopathy 1A (0.718)
- **Europe PMC papers**: 5386
- **Why important**: COL6A3 has strong module connectivity, including the strongest STRING relationship in the module with COL6A1, and connects the collagen-VI system with COL1A2 and BGN. It contributes to nearly all primary matrix, collagen, integrin, and ECM-receptor terms (16 globally significant GO/KEGG terms, q_global 7.06e-05–0.0408; see the table). As the large alpha chain of collagen VI, it is structurally important for the beaded-filament matrix. Its fibroblast and fibro-adipogenic progenitor annotations and established links to Bethlem myopathy, Ullrich congenital muscular dystrophy, and related disorders add functional and clinical importance.
- **Conclusion**: Established evidence supports COL6A3 as a major collagen-VI organizing component and a clinically relevant indicator of matrix integrity. Its module position makes it a plausible anchor of the shared stromal program, while any organ-specific signaling role remains hypothetical.

#### COL1A2

- **Related proteins** (co-abundance neighbors): COL6A3 (0.83), COL6A1 (0.81); STRING partners: BGN (0.938), COL6A1 (0.875), COL6A3 (0.968), FBN1 (0.965)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type I alpha 2 chain. This gene encodes the pro-alpha2 chain of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIB, recessive Ehlers-Danlos syndrome Classi…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 2 (0.845); osteogenesis imperfecta type 3 (0.830); osteogenesis imperfecta type 4 (0.820); Ehlers-Danlos syndrome, cardiac valvular type (0.777); osteogenesis imperfecta type 1 (0.770)
- **Europe PMC papers**: 67901
- **Why important**: COL1A2 is highly connected within the module and has strong STRING links to COL6A1, COL6A3, FBN1, and BGN. It encodes the alpha-two chain of type I collagen and supports collagen-trimer, tensile strength, integrin, and ECM-receptor evidence (12 globally significant GO/KEGG terms, q_global 7.06e-05–0.0408; see the table). HPA detects it in both lung and testis and associates it with stromal and fibro-adipogenic populations. Its extensive literature and disease links include osteogenesis imperfecta, Ehlers-Danlos syndromes, osteoporosis, and atypical Marfan syndrome.
- **Conclusion**: Established evidence supports COL1A2 as the fibrillar-collagen component that connects the collagen-VI and microfibril portions of the module. It is likely important for matrix strength and tissue architecture. The co-abundance data do not establish whether it drives the shared program or simply tracks matrix-producing cells.

#### FBN1

- **Related proteins** (co-abundance neighbors): COL6A1 (0.82); STRING partners: BGN (0.784), COL1A2 (0.965), COL6A1 (0.743), COL6A3 (0.786)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibrillin 1. This gene encodes a member of the fibrillin family of proteins. The encoded preproprotein is proteolytically processed to generate two proteins including the extracellular matrix component fibrillin-1 and the protein hormone asprosin. Fibrillin-1 is an extracellular matrix glycoprotein that serves as a structural component of calcium-binding microfibrils. These microfibrils provide force-bearing s…
- **Diseases (Open Targets)**: Marfan syndrome (0.892); ectopia lentis 1, isolated, autosomal dominant (0.811); Acromicric dysplasia (0.802); geleophysic dysplasia 2 (0.802); stiff skin syndrome (0.799)
- **Europe PMC papers**: 9216
- **Why important**: FBN1 is connected to the collagen genes and BGN in STRING and contributes to extracellular-matrix structural, integrin, skeletal-development, lung-alveolus, and endoplasmic-reticulum evidence (10 globally significant GO/KEGG terms, q_global 7.06e-05–0.0408; see the table). It encodes fibrillin-one, a structural component of force-bearing calcium-binding microfibrils, and also produces asprosin. HPA associates it with fibroblasts, adipocytes, fibro-adipogenic progenitors, and placental or adipose tissue. Its strong disease associations include Marfan syndrome, ectopia lentis, acromicric dysplasia, geleophysic dysplasia, and stiff-skin syndrome.
- **Conclusion**: Established evidence supports FBN1 as the microfibrillar and biomechanical component of the module, with relevance to matrix organization and developmental signaling. Its presence suggests that the module extends beyond collagen fibrils into the broader microfibril scaffold. A direct role for asprosin in this cross-tissue co-abundance pattern is not established.

#### BGN

- **Related proteins** (co-abundance neighbors): COL6A3 (0.85); STRING partners: COL1A2 (0.938), COL6A1 (0.86), COL6A3 (0.806), FBN1 (0.784)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biglycan. This gene encodes a member of the small leucine-rich proteoglycan (SLRP) family of proteins. The encoded preproprotein is proteolytically processed to generate the mature protein, which plays a role in bone growth, muscle development and regeneration, and collagen fibril assembly in multiple tissues. This protein may also regulate inflammation and innate immunity. Additionally, the encoded protein…
- **Diseases (Open Targets)**: X-linked spondyloepimetaphyseal dysplasia (0.746); Meester-Loeys syndrome (0.672); familial thoracic aortic aneurysm and aortic dissection (0.630); spondyloepimetaphyseal dysplasia, matrilin-3 type (0.383); spondyloepimetaphyseal dysplasia (0.375)
- **Europe PMC papers**: 6991
- **Why important**: BGN has the least extensive module connectivity but remains biologically important because it links the matrix network to extracellular proteoglycan biology and has STRING relationships with all other module genes. It is a small leucine-rich proteoglycan involved in collagen fibril assembly, bone growth, muscle development and regeneration, and potentially inflammatory or vascular processes. It supports the shared extracellular-matrix and skeletal-development evidence (7 globally significant GO/KEGG terms, q_global 7.06e-05–0.0272; see the table). HPA associates it with fibroblasts, Leydig cells, pericytes, hepatic stellate cells, and blood-vessel tissue, while disease associations include connective-tissue and aortic disease phenotypes.
- **Conclusion**: Established evidence supports BGN as a matrix-organizing and cell–matrix signaling modulator, rather than the principal collagen scaffold. Its vascular and gonadal stromal annotations make it particularly informative for the shared lung–testis interpretation. Any proposed inflammatory effect in this module remains a hypothesis.

## Module 10

**Tissue pair**: lung and testis  
**Genes (23)**: DCTN1, DDX5, EIF3C, EIF3L, FKBP4, RHOT1, NSF, SEC24C, SNX2, CTTN, FARSB, IARS1, KARS1, QARS1, RARS1, SARS1, VARS1, YARS1, CCT5, CCT3, CCT7, CCT8, XPO1

### Function

This is a conserved intracellular protein-biosynthesis module centered on translation quality control and proteostasis. The strongest primary evidence is the coordinated presence of aminoacyl-tRNA synthetases and aminoacyl-tRNA charging in (GO:MF aminoacyl-tRNA ligase activity; q_global = 6.88e-06) through (GO:BP tRNA metabolic process; q_global = 0.000107), including the KEGG aminoacyl-tRNA biosynthesis pathway (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 6.88e-06). The module also supports translation and protein biosynthesis through EIF3C, EIF3L, and the synthetases (GO:BP translation; q_global = 0.00182) and (GO:BP protein biosynthetic process; q_global = 0.00182). A second coherent branch is the CCT chaperonin complex, represented by CCT3, CCT5, CCT7, and CCT8, with globally corrected evidence for the chaperonin-containing T-complex (GO:CC chaperonin-containing T-complex; q_global = 0.000163) and ATP-dependent protein-folding chaperone activity (GO:MF ATP-dependent protein folding chaperone; q_global = 0.0274). Broad nucleotide-binding and RNA-related terms (GO:MF ATP binding; q_global = 0.000139), (GO:MF adenyl ribonucleotide binding; q_global = 0.000153), (GO:MF purine ribonucleoside triphosphate binding; q_global = 0.000331) through (GO:MF ribonucleotide binding; q_global = 0.000385), (GO:MF catalytic activity, acting on RNA; q_global = 0.000582), (GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.00314), (GO:MF nucleotide binding; q_global = 0.00402), (GO:MF nucleoside phosphate binding; q_global = 0.00479), (GO:MF RNA binding; q_global = 0.00996), and (GO:BP nucleic acid metabolic process; q_global = 0.0425) are consistent with these activities. Telomere and Cajal-body terms (GO:BP protein localization to nuclear body; q_global = 0.000163) through (GO:BP protein localization to nucleoplasm; q_global = 0.000163) and (GO:BP regulation of telomere maintenance via telomerase; q_global = 0.000575) through (GO:BP RNA localization to nucleus; q_global = 0.000575) are supported by the CCT submodule, but they should be interpreted as annotations associated with the chaperonin components rather than proof that telomere maintenance is the principal function of the whole module. The sperm-recognition terms (GO:BP binding of sperm to zona pellucida; q_global = 0.00133), (GO:BP sperm-egg recognition; q_global = 0.00259), (GO:BP cell-cell recognition; q_global = 0.0107), and (GO:BP cell recognition; q_global = 0.0447) likewise appear to be driven by the CCT genes and do not establish a specialized reproductive function for the entire module.

**Cell composition.** The module is not dominated by plasma proteins, secreted proteins, or blood-cell markers. HPA identifies only one secreted gene, while nearly all module proteins are detected in lung and all are detected in testis. Most genes have low tissue specificity, and most have low immune-cell specificity, arguing against a simple blood-contamination explanation. The module nevertheless has substantial cell-context structure: several genes are enhanced in spermatocytes or spermatids, and selected genes are enriched in neuronal, epithelial, or other specialized cell types. This suggests that the shared lung–testis signal is more likely to reflect broadly required intracellular machinery that is particularly abundant in certain cell populations, with germ-cell enrichment contributing in testis. The absence of widespread immune enrichment makes a shared blood-cell origin less persuasive, although cellular composition remains a possible contributor to co-abundance.

**GO/KEGG enrichment**: 65 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF aminoacyl-tRNA ligase activity | 6.88e-06 | FARSB, IARS1, KARS1, QARS1, RARS1, SARS1, VARS1, YARS1 |
| GO:BP tRNA aminoacylation for protein translation | 6.88e-06 | FARSB, IARS1, KARS1, QARS1, RARS1, SARS1, VARS1, YARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 6.88e-06 | FARSB, IARS1, KARS1, QARS1, RARS1, SARS1, VARS1, YARS1 |
| GO:BP amino acid activation | 6.88e-06 | FARSB, IARS1, KARS1, QARS1, RARS1, SARS1, VARS1, YARS1 |
| GO:BP tRNA aminoacylation | 6.88e-06 | FARSB, IARS1, KARS1, QARS1, RARS1, SARS1, VARS1, YARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 6.88e-06 | FARSB, IARS1, KARS1, QARS1, RARS1, SARS1, VARS1, YARS1 |
| GO:MF catalytic activity, acting on a tRNA | 3.56e-05 | FARSB, IARS1, KARS1, QARS1, RARS1, SARS1, VARS1, YARS1 |
| GO:BP tRNA metabolic process | 0.000107 | FARSB, IARS1, KARS1, QARS1, RARS1, SARS1, VARS1, YARS1 |
| GO:MF ATP binding | 0.000139 | CCT3, CCT5, CCT7, CCT8, DDX5, FARSB, FKBP4, IARS1, KARS1, NSF, QARS1, RARS1, SARS1, VARS1, YARS1 |
| GO:MF adenyl ribonucleotide binding | 0.000153 | CCT3, CCT5, CCT7, CCT8, DDX5, FARSB, FKBP4, IARS1, KARS1, NSF, QARS1, RARS1, SARS1, VARS1, YARS1 |
| GO:CC chaperonin-containing T-complex | 0.000163 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 0.000163 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 0.000163 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 0.000163 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 0.000163 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING provides strong independent support for two physically and functionally coherent components. The aminoacyl-tRNA synthetases form a dense, mutually connected group involving FARSB, IARS1, KARS1, QARS1, RARS1, SARS1, VARS1, and YARS1; this agrees with the primary GO and KEGG evidence and with STRING annotations for cytosolic tRNA aminoacylation (STRING RCTM Cytosolic tRNA aminoacylation; within-query FDR = 6.9e-07), aminoacyl-tRNA synthetase activity (STRING Keyword Aminoacyl-tRNA synthetase; within-query FDR = 9.26e-07) and (STRING Function aminoacyl-tRNA ligase activity; within-query FDR = 5.15e-06), and translation (STRING RCTM Translation; within-query FDR = 2.23e-06) and (STRING Process Translation; within-query FDR = 2.42e-05). The CCT proteins CCT3, CCT5, CCT7, and CCT8 form a highly connected known chaperonin group, and CCT7 also links to EIF3C. EIF3C and EIF3L form a known translation-initiation pair. hu.MAP independently identifies a synthetase-containing complex containing IARS1, QARS1, RARS1, and KARS1 (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), the CCT-containing complexes (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_01951.1), and EIF3C–EIF3L initiation complexes (hu.MAP huMAP3_01276.1) through (hu.MAP huMAP3_11246.1). Thus, much of the network is a recombination of established translation, aminoacylation, and chaperonin machinery. The remaining links involving DDX5, FKBP4, NSF, transport proteins, and cytoskeletal or trafficking proteins are less directly supported by the listed STRING and hu.MAP interactions and should not be treated as established physical complexes solely because they co-abundance with the module.

**STRING interactions (score >= 0.7)**: 34 of 253 gene pairs: CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999); CCT7–EIF3C (0.728); EIF3C–EIF3L (0.999); FARSB–IARS1 (0.914); FARSB–KARS1 (0.813); FARSB–RARS1 (0.706); FARSB–VARS1 (0.776); FARSB–YARS1 (0.946); IARS1–KARS1 (0.999); IARS1–QARS1 (0.999); IARS1–RARS1 (0.999); IARS1–SARS1 (0.908); IARS1–VARS1 (0.9); IARS1–YARS1 (0.966); KARS1–QARS1 (0.999); KARS1–RARS1 (0.999); KARS1–SARS1 (0.882); KARS1–VARS1 (0.978); KARS1–YARS1 (0.988); QARS1–RARS1 (0.999); QARS1–SARS1 (0.852); QARS1–VARS1 (0.91); QARS1–YARS1 (0.959); RARS1–SARS1 (0.933); RARS1–VARS1 (0.905); RARS1–YARS1 (0.942); SARS1–VARS1 (0.879); SARS1–YARS1 (0.941); VARS1–YARS1 (0.956)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Metabolism of proteins (FDR = 1e-07, 19 genes); Keyword Protein biosynthesis (FDR = 2.98e-07, 10 genes); RCTM Cytosolic tRNA aminoacylation (FDR = 6.9e-07, 8 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 9.26e-07, 8 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 1.28e-06, 8 genes); RCTM Translation (FDR = 2.23e-06, 10 genes); Function aminoacyl-tRNA ligase activity (FDR = 5.15e-06, 8 genes); Function ATP binding (FDR = 1.08e-05, 15 genes); Function Purine ribonucleoside triphosphate binding (FDR = 1.87e-05, 16 genes); Function Catalytic activity, acting on RNA (FDR = 2.23e-05, 9 genes); Function Purine ribonucleotide binding (FDR = 2.38e-05, 16 genes); Process Translation (FDR = 2.42e-05, 10 genes); Process tRNA aminoacylation for protein translation (FDR = 2.42e-05, 8 genes); Keyword ATP-binding (FDR = 2.75e-05, 14 genes); Process ncRNA metabolic process (FDR = 3.33e-05, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (IARS1, QARS1, RARS1, KARS1; 4/14); huMAP3_13688.1 (IARS1, QARS1, RARS1, KARS1; 4/14); huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_01276.1 (EIF3C, EIF3L; 2/17); huMAP3_13175.1 (EIF3C, EIF3L; 2/20); huMAP3_11246.1 (EIF3C, EIF3L; 2/24)

### Novelty

The module is unlikely to represent a wholly new molecular machine: its dominant subnetworks correspond to well-established aminoacyl-tRNA synthetase assemblies, the CCT chaperonin, and EIF3 translation-initiation complexes, all supported by STRING and hu.MAP. The potentially novel finding is therefore the conserved co-abundance of these established components across lung and testis, together with their particular cross-tissue network arrangement and links to trafficking, RNA processing, and cytoskeletal functions. This is a systems-level observation rather than evidence for a previously unknown complex. The lack of hu.MAP or STRING support for some individual connections may indicate context-specific co-regulation or incomplete interaction coverage, but absence from those resources alone does not establish novelty. Validation in independent lung and testis datasets, with cell-composition adjustment and experimental testing of the weaker links, would be needed before claiming a new biological mechanism.

**Hypothesis.** Hypothesis: this conserved module coordinates high-throughput protein production with folding and intracellular handling in metabolically or developmentally demanding cells. The aminoacyl-tRNA synthetase group may maintain aminoacyl-tRNA supply and translational fidelity, EIF3C and EIF3L may support translation initiation, and the CCT complex may fold newly synthesized client proteins. DDX5, XPO1, SEC24C, SNX2, NSF, DCTN1, RHOT1, and CTTN could connect this core to RNA processing, nuclear export, vesicle traffic, endosomal sorting, mitochondrial movement, and cytoskeletal organization. Germ-cell enrichment in testis and broad detection in lung are compatible with a shared demand for proteome production and quality control, rather than a lung-specific or testis-specific pathway. The telomere, Cajal-body, and sperm-recognition annotations suggest testable downstream contexts for the CCT branch, but they remain hypotheses about module-level biology rather than established functions of the complete module.

### Important genes

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT7 (0.95), CCT5 (0.93), CCT3 (0.90), KARS1 (0.90), VARS1 (0.88), DDX5 (0.86), IARS1 (0.85), RARS1 (0.85), YARS1 (0.85), NSF (0.85), CTTN (0.84), FKBP4 (0.84), QARS1 (0.83), XPO1 (0.83), DCTN1 (0.82); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is the highest-ranked network hub in the supplied module and connects strongly to the other CCT subunits as well as several synthetases and RNA-related proteins. It is a constituent of the CCT chaperonin, is supported by the chaperonin and protein-folding terms (GO:CC chaperonin-containing T-complex; q_global = 0.000163), (GO:CC protein folding chaperone complex; q_global = 0.0107), and (GO:MF ATP-dependent protein folding chaperone; q_global = 0.0274), and participates in the telomere and Cajal-body annotation cluster (GO:BP protein localization to nuclear body; q_global = 0.000163) through (GO:BP protein localization to nucleoplasm; q_global = 0.000163) and (GO:BP regulation of telomere maintenance via telomerase; q_global = 0.000575) through (GO:BP RNA localization to nucleus; q_global = 0.000575). It is detected in both tissues, has oocyte-enhanced single-cell expression, and has substantial literature support. Its disease and cancer associations further indicate broad biological relevance, although they do not by themselves explain the cross-tissue module.
- **Conclusion**: Established: CCT8 is a central chaperonin component and a major network connector in this module, consistent with protein folding and proteostasis. Hypothesis: CCT8 may help couple folding capacity to translation and germ-cell or lung-cell demands, but the module does not establish a specific telomere or reproductive mechanism.

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT3 (0.95), CCT8 (0.93), CCT7 (0.93), KARS1 (0.88), RARS1 (0.87), VARS1 (0.85), XPO1 (0.85), DDX5 (0.82), DCTN1 (0.82), CTTN (0.82), IARS1 (0.82), NSF (0.81); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is a prominent network hub within the CCT group and is supported by the same globally corrected chaperonin, folding, Cajal-body, and telomere-related terms as the other CCT subunits. It has strong STRING support with CCT3, CCT7, and CCT8 and appears in multiple hu.MAP CCT complexes (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_01951.1). HPA shows detection in both tissues and enrichment in late primary spermatocytes, while disease evidence includes hereditary sensory and autonomic neuropathy and neurodegenerative disease. Its literature volume is substantial.
- **Conclusion**: Established: CCT5 is part of a known ATP-dependent folding machine represented coherently in the module. Hypothesis: its co-abundance with synthetases may mark coordinated proteome quality control during high translational demand, especially in spermatogenic cells.

#### IARS1

- **Related proteins** (co-abundance neighbors): YARS1 (0.88), CCT8 (0.85), QARS1 (0.84), EIF3L (0.83), RARS1 (0.83), CCT5 (0.82), EIF3C (0.81), NSF (0.81), CCT7 (0.80); STRING partners: FARSB (0.914), KARS1 (0.999), QARS1 (0.999), RARS1 (0.999), SARS1 (0.908), VARS1 (0.9), YARS1 (0.966)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Isoleucine-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family and has been identified as a …
- **Diseases (Open Targets)**: growth retardation, intellectual developmental disorder, hypotonia, and hepatopathy (0.733); Abnormality of the skeletal system (0.332); microcephaly (0.289); Global developmental delay (0.289); Hallux valgus (0.184)
- **Europe PMC papers**: 184
- **Why important**: IARS1 is a central member of the dense synthetase subnetwork, with strong STRING relationships to FARSB, KARS1, QARS1, RARS1, SARS1, VARS1, and YARS1. It belongs to the hu.MAP synthetase complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1) and contributes to the primary aminoacylation and translation evidence (GO:MF aminoacyl-tRNA ligase activity; q_global = 6.88e-06) through (GO:BP tRNA metabolic process; q_global = 0.000107), (GO:BP translation; q_global = 0.00182), (GO:BP protein biosynthetic process; q_global = 0.00182), and (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.0151). It is detected in both lung and testis and has disease associations involving developmental delay, hypotonia, and hepatopathy, as well as relevance to autoimmune myositis.
- **Conclusion**: Established: IARS1 is a core aminoacyl-tRNA charging enzyme and a structural bridge within the synthetase subnetwork. Hypothesis: its position may help couple translational fidelity to chaperone capacity, but the co-abundance data do not demonstrate a direct regulatory interaction with CCT.

#### RARS1

- **Related proteins** (co-abundance neighbors): CCT5 (0.87), CCT3 (0.87), DDX5 (0.86), EIF3L (0.86), CCT8 (0.85), FARSB (0.84), CCT7 (0.84), KARS1 (0.84), EIF3C (0.84), IARS1 (0.83); STRING partners: FARSB (0.706), IARS1 (0.999), KARS1 (0.999), QARS1 (0.999), SARS1 (0.933), VARS1 (0.905), YARS1 (0.942)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 has a high network position and connects the synthetase group with CCT proteins, EIF3L, and DDX5. It is part of hu.MAP synthetase complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), has broad support across the primary aminoacylation, translation, RNA-binding, and protein-biosynthesis terms, and is included in the STRING synthetase annotations (STRING RCTM Cytosolic tRNA aminoacylation; within-query FDR = 6.9e-07) through (STRING Function aminoacyl-tRNA ligase activity; within-query FDR = 5.15e-06). It is detected in testis but not lung by HPA, which makes it an informative example of a module gene whose protein abundance may differ from the shared tissue-level pattern. It has established leukodystrophy associations and a meaningful literature base.
- **Conclusion**: Established: RARS1 supplies a well-supported aminoacylation function and links the translation core to other module branches. Hypothesis: its lung non-detection in HPA may reflect cell composition, sensitivity, or tissue-specific regulation rather than contradicting the conserved co-abundance signal.

#### DDX5

- **Related proteins** (co-abundance neighbors): RARS1 (0.86), CCT8 (0.86), YARS1 (0.84), KARS1 (0.84), CCT5 (0.82), CCT3 (0.82), FARSB (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 is a highly studied RNA helicase with the largest literature volume among the listed module genes. It occupies an intermediate network position, connecting CCT proteins and multiple synthetases, and is supported by primary RNA-catalytic, RNA-binding, nucleic-acid, and gene-expression terms (GO:MF catalytic activity, acting on RNA; q_global = 0.000582), (GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.00314), (GO:MF RNA binding; q_global = 0.00996), (GO:BP gene expression; q_global = 0.0342), and (GO:BP nucleic acid metabolic process; q_global = 0.0425). Its established functions include RNA-structure remodeling, transcriptional co-regulation, splicing, and small noncoding-RNA processing. HPA detects it in both tissues, and its disease and infection associations indicate broad relevance. Unlike the core synthetases and CCT proteins, it lacks the listed STRING partners and hu.MAP complexes, so its network role is less established as a physical interaction.
- **Conclusion**: Established: DDX5 provides a plausible RNA-processing component that broadens the module beyond translation and folding. Hypothesis: DDX5 may coordinate RNA maturation with protein synthesis in this module, but its direct integration into the network requires biochemical or perturbational validation.

## Module 11

**Tissue pair**: lung and testis  
**Genes (6)**: HPRT1, HSPH1, NAA15, NAA50, PSMC4, PSMD13

### Function

The strongest supported function is protein N-terminal acetylation through the NatA complex. The globally corrected terms identify protein acetylation, N-terminal protein amino acid acetylation, and the NatA complex, all driven by NAA15 and NAA50 (GO:BP protein acetylation; q_global = 0.0468) (GO:BP N-terminal protein amino acid acetylation; q_global = 0.0468) (GO:CC NatA complex; q_global = 0.0468). NAA15 is the highest-connectivity gene in the subgraph and NAA50 is its direct partner, providing a coherent catalytic-complex signal. A second component is proteostasis: PSMC4 and PSMD13 are proteasome subunits and form a direct STRING pair, while HSPH1 supports protein-folding and stress-response biology and HPRT1 supports purine salvage. Because the co-abundance graph contains links among these functional groups but the enrichment result does not establish a single unified pathway beyond NatA, the module is best interpreted as a conserved cellular protein-homeostasis and biosynthetic program rather than as proof of one physical complex.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, low immune-cell specificity for every member, and detection of every member in both lung and testis. Most genes have low tissue specificity, which is compatible with broadly used intracellular functions and a housekeeping-like component. At the same time, most members show cell-type enhancement, including germ-cell, Sertoli, syncytiotrophoblast, ductal, monocyte, or myonuclear patterns. NAA50 is tissue-enhanced in skeletal muscle and cell-enhanced in myonuclei, whereas PSMC4, HPRT1, and PSMD13 show reproductive-cell patterns. Thus, the shared signal could reflect conserved intracellular biology, shared cellular states, or differences in cell composition; the evidence does not support interpreting it as a blood-cell module.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP protein acetylation | 0.0468 | NAA15, NAA50 |
| GO:BP N-terminal protein amino acid acetylation | 0.0468 | NAA15, NAA50 |
| GO:CC NatA complex | 0.0468 | NAA15, NAA50 |

### STRING and hu.MAP

STRING provides two high-confidence direct relationships: NAA15 with NAA50 and PSMC4 with PSMD13. These pairs independently support the NatA and proteasome interpretations, respectively. STRING reports no functional enrichment for the module, so the direct interactions should not be expanded into an unsupported pathway claim. hu.MAP places NAA15 and NAA50 together in several NatA-related complexes (hu.MAP huMAP3_01027.1) (hu.MAP huMAP3_10987.1) (hu.MAP huMAP3_13394.1), and places PSMC4 and PSMD13 together in several proteasome assemblies (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). The remaining module genes are not represented as shared members of those listed hu.MAP complexes. Consequently, known molecular complexes explain two compact parts of the module, while the remaining co-abundance links may reflect coordinated expression, indirect regulation, or shared cellular context rather than direct binding.

**STRING interactions (score >= 0.7)**: 2 of 15 gene pairs: NAA15–NAA50 (0.999); PSMC4–PSMD13 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01027.1 (NAA15, NAA50; 2/6); huMAP3_10987.1 (NAA15, NAA50; 2/8); huMAP3_13394.1 (NAA15, NAA50; 2/9); huMAP3_05064.1 (PSMC4, PSMD13; 2/31); huMAP3_09656.1 (PSMC4, PSMD13; 2/64); huMAP3_13725.1 (PSMC4, PSMD13; 2/69)

### Novelty

The molecular functions represented here are not new: NatA-mediated acetylation and proteasomal degradation are established cellular processes, and the NatA and proteasome relationships are already captured by STRING and hu.MAP. The potentially novel observation is the conservation of this particular six-gene co-abundance pattern across lung and testis, especially the way NatA, proteasome, stress, and purine-salvage genes occur in one cross-tissue module. However, the supplied evidence does not establish that this exact module is absent from prior transcriptomic or proteomic studies. Absence of a complete match in STRING or hu.MAP would not prove novelty. The defensible conclusion is therefore a potentially interesting cross-tissue network configuration, not a demonstrated new biological mechanism.

**Hypothesis.** Hypothesis: the module coordinates production and quality control of intracellular proteins in shared lung and testis cellular states. NatA, represented by NAA15 and NAA50, may establish N-terminal acetylation of newly synthesized proteins; HSPH1 may help stabilize or refold vulnerable proteins; and the PSMC4–PSMD13 proteasome pair may remove damaged or otherwise targeted proteins. HPRT1 may supply purine-salvage activity to support nucleotide economy during this biosynthetic and quality-control state. This model is consistent with the annotations and network structure, but it remains a hypothesis because co-abundance does not demonstrate causal regulation, direct interaction, or identical cellular origin in the two tissues.

### Important genes

#### NAA15

- **Related proteins** (co-abundance neighbors): HSPH1 (0.88), NAA50 (0.83), HPRT1 (0.82); STRING partners: NAA50 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_01027.1, huMAP3_10987.1, huMAP3_13394.1
- **Function (MyGene.info)**: N-alpha-acetyltransferase 15, NatA auxiliary subunit. N-alpha-acetylation is among the most common post-translational protein modifications in eukaryotic cells. This process involves the transfer of an acetyl group from acetyl-coenzyme A to the alpha-amino group on a nascent polypeptide and is essential for normal cell function. This gene encodes the auxillary subunit of the N-terminal acetyltransferase A (NatA) complex. [provided by RefSeq, Jan 2017…
- **Diseases (Open Targets)**: intellectual disability, autosomal dominant 50 (0.790); hereditary disease (0.544); Intellectual disability (0.521); neurodevelopmental disorder (0.461); neurodegenerative disease (0.451)
- **Europe PMC papers**: 505
- **Why important**: NAA15 is the strongest network hub in the module and is directly linked to NAA50. It is the auxiliary subunit of NatA and contributes to all primary enrichment terms (GO:BP protein acetylation; q_global = 0.0468) (GO:BP N-terminal protein amino acid acetylation; q_global = 0.0468) (GO:CC NatA complex; q_global = 0.0468). Its disease associations include intellectual disability and neurodevelopmental disease, and the supplied literature record is substantial.
- **Conclusion**: Established evidence supports NAA15 as the central NatA anchor and the most persuasive driver of the module's primary functional interpretation. Its hub status supports coordinated module organization, but does not by itself show that NAA15 regulates the other genes.

#### NAA50

- **Related proteins** (co-abundance neighbors): NAA15 (0.83); STRING partners: NAA15 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_01027.1, huMAP3_10987.1, huMAP3_13394.1
- **Function (MyGene.info)**: N-alpha-acetyltransferase 50, NatE catalytic subunit. Enables H4 histone acetyltransferase activity; peptide alpha-N-acetyltransferase activity; and peptidyl-lysine acetyltransferase activity. Involved in N-terminal protein amino acid acetylation; establishment of mitotic sister chromatid cohesion; and mitotic sister chromatid cohesion, centromeric. Located in cytosol and nucleus. Part of NatA complex. [provided by Alliance of Genome Resources, Apr 2…
- **Diseases (Open Targets)**: musculoskeletal system disorder (0.174); Abnormality of the skeletal system (0.147); upper respiratory tract disorder (0.066); neuroblastoma (0.059); alcohol drinking (0.035)
- **Europe PMC papers**: 308
- **Why important**: NAA50 is the catalytic NatE subunit with peptide alpha-N-acetyltransferase and peptidyl-lysine acetyltransferase activities. It forms the high-confidence STRING pair with NAA15 and appears with NAA15 in several hu.MAP NatA-related complexes (hu.MAP huMAP3_01027.1) (hu.MAP huMAP3_10987.1) (hu.MAP huMAP3_13394.1). Its skeletal-muscle and myonuclear HPA patterns may be relevant to tissue or cell-state specificity.
- **Conclusion**: Established evidence supports NAA50 as the catalytic counterpart of NAA15 and the clearest functional confirmation of the acetylation signal. Its tissue-enhanced pattern is compatible with cell-composition effects, so a lung–testis-specific role remains unproven.

#### PSMC4

- **Related proteins** (co-abundance neighbors): PSMD13 (0.85), HPRT1 (0.80); STRING partners: PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 4. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.603); mantle cell lymphoma (0.542); neoplasm (0.519); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1065
- **Why important**: PSMC4 is a proteasome ATPase and is directly paired with PSMD13 by STRING. It occurs with PSMD13 in several hu.MAP proteasome assemblies (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) and has cell-type-enhanced expression in multiple reproductive and placental cell types. Its disease associations include plasma-cell myeloma, mantle-cell lymphoma, neoplasm, HIV infection, and amyloidosis, with a large literature.
- **Conclusion**: Established evidence supports PSMC4 as a proteasome-associated arm of the module and a plausible protein-quality-control component. Its co-abundance with NatA genes may indicate coordinated proteostasis, but the data do not establish a direct NatA–proteasome mechanism.

#### PSMD13

- **Related proteins** (co-abundance neighbors): PSMC4 (0.85); STRING partners: PSMC4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in lung, testis
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 is a non-ATPase proteasome subunit and the direct partner of PSMC4 in STRING. Its repeated presence with PSMC4 in hu.MAP proteasome assemblies (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) gives it strong complex-level support despite its peripheral position in the co-abundance graph. Its disease associations include plasma-cell myeloma, mantle-cell lymphoma, neurodegenerative disease, neoplasm, and HIV infection.
- **Conclusion**: Established evidence supports PSMD13 as a genuine proteasome component that reinforces the module's protein-degradation interpretation. Its low graph connectivity means it is better viewed as a complex marker than as an inferred module-wide regulator.

#### HPRT1

- **Related proteins** (co-abundance neighbors): NAA15 (0.82), PSMC4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hypoxanthine phosphoribosyltransferase 1. The protein encoded by this gene is a transferase, which catalyzes conversion of hypoxanthine to inosine monophosphate and guanine to guanosine monophosphate via transfer of the 5-phosphoribosyl group from 5-phosphoribosyl 1-pyrophosphate. This enzyme plays a central role in the generation of purine nucleotides through the purine salvage pathway. Mutations in this gene result in Lesch-Nyhan syndro…
- **Diseases (Open Targets)**: Lesch-Nyhan syndrome (0.856); hypoxanthine guanine phosphoribosyltransferase partial deficiency (0.827); neurodegenerative disease (0.439); dystonic disorder (0.372); autoimmune disorder of central nervous system (0.370)
- **Europe PMC papers**: 15377
- **Why important**: HPRT1 is a network bridge connected to both NAA15 and PSMC4, linking the acetylation and proteasome-associated portions of the subgraph. It catalyzes hypoxanthine and guanine salvage, has cell-type enhancement in early primary spermatocytes and Sertoli cells, and is associated with Lesch–Nyhan syndrome, partial HPRT deficiency, and gout. It also has a particularly extensive literature record.
- **Conclusion**: Established evidence supports HPRT1 as a purine-salvage enzyme and a potentially informative bridge in the network. Its placement is consistent with a shared metabolic state, but the module does not demonstrate that purine salvage controls acetylation or proteasomal degradation.
