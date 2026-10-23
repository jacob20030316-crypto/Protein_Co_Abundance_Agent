# Conserved co-abundance modules: circulatory_system and ovary

## Module 0

**Tissue pair**: circulatory_system and ovary  
**Genes (12)**: SERPINC1, APOA1, APOH, CLU, C3, ITGAV, NCSTN, NUDT19, PLG, RAB3D, F2, VTN

### Function

The module is best interpreted as a circulating extracellular protease, coagulation, fibrinolysis, complement, and hemostasis module. The strongest primary evidence is the globally corrected enrichment for complement and coagulation cascades (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 3.84e-08), blood microparticles (GO:CC blood microparticle; q_global = 4e-07), regulation of blood coagulation and hemostasis (GO:BP regulation of blood coagulation; q_global = 2.63e-05) (GO:BP regulation of hemostasis; q_global = 2.63e-05) (GO:BP regulation of coagulation; q_global = 4.4e-05), fibrinolysis and its negative regulation (GO:BP regulation of fibrinolysis; q_global = 3.12e-05) (GO:BP negative regulation of fibrinolysis; q_global = 3.12e-05) (GO:BP fibrinolysis; q_global = 0.000165), and wound-healing responses (5 globally significant GO/KEGG terms, q_global 0.000339–0.00337; see the table). The extracellular, secretory, vesicular, and lipoprotein context is supported by (14 globally significant GO/KEGG terms, q_global 0.00129–0.049; see the table). The module therefore appears to represent coordinated abundance of plasma proteins involved in protease activation and inhibition, complement-related immune surveillance, lipid-associated transport, extracellular-matrix interaction, and vascular or tissue-repair processes. The receptor-binding and receptor-regulatory enrichments (4 globally significant GO/KEGG terms, q_global 0.000813–0.0138; see the table) suggest potential signaling consequences, but they do not establish a single receptor-mediated mechanism.

**Cell composition.** The module is dominated by secreted or plasma-associated proteins, including APOA1, APOH, C3, CLU, F2, PLG, SERPINC1, and VTN. HPA identifies most of the module as tissue enriched or tissue enhanced, with liver and hepatocytes recurring prominently, and identifies eight genes as secreted. This strongly supports a liver-derived circulating-protein signature rather than an ovary-specific intracellular program. The blood microparticle, extracellular vesicle, secretory vesicle, plasma lipoprotein, and extracellular-space enrichments (13 globally significant GO/KEGG terms, q_global 4e-07–0.049; see the table) are consistent with that interpretation. The module is not simply a blood-leukocyte module: several genes are not detected in immune cells, while selected genes show immune-cell enhancement or enrichment, including C3, CLU, and RAB3D. The ovary signal may therefore reflect shared exposure to circulating proteins, vascular or extracellular material, secretory cells, or shared tissue-associated cell states. ITGAV, NCSTN, and RAB3D provide a smaller tissue or vesicle-related component, but they do not outweigh the plasma protein composition.

**GO/KEGG enrichment**: 68 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 3.84e-08 | C3, CLU, F2, PLG, SERPINC1, VTN |
| GO:CC blood microparticle | 4e-07 | APOA1, C3, CLU, F2, PLG, SERPINC1, VTN |
| GO:BP regulation of blood coagulation | 2.63e-05 | APOH, F2, PLG, SERPINC1, VTN |
| GO:BP regulation of hemostasis | 2.63e-05 | APOH, F2, PLG, SERPINC1, VTN |
| GO:BP regulation of fibrinolysis | 3.12e-05 | APOH, F2, PLG, VTN |
| GO:BP negative regulation of fibrinolysis | 3.12e-05 | APOH, F2, PLG, VTN |
| GO:BP regulation of coagulation | 4.4e-05 | APOH, F2, PLG, SERPINC1, VTN |
| GO:BP positive regulation of blood coagulation | 5.94e-05 | APOH, F2, PLG, VTN |
| GO:BP positive regulation of coagulation | 5.94e-05 | APOH, F2, PLG, VTN |
| GO:BP positive regulation of hemostasis | 5.94e-05 | APOH, F2, PLG, VTN |
| GO:BP fibrinolysis | 0.000165 | APOH, F2, PLG, VTN |
| GO:BP regulation of wound healing | 0.000339 | APOH, F2, PLG, SERPINC1, VTN |
| GO:BP regulation of response to wounding | 0.000757 | APOH, F2, PLG, SERPINC1, VTN |
| GO:MF signaling receptor binding | 0.000813 | APOA1, C3, CLU, F2, ITGAV, NCSTN, PLG, VTN |
| GO:BP negative regulation of blood coagulation | 0.000839 | APOH, F2, PLG, VTN |

### STRING and hu.MAP

STRING supports a coherent known interaction neighborhood among the major plasma proteins. Particularly strong relationships include F2 with SERPINC1, PLG with SERPINC1 and VTN, ITGAV with VTN, and APOA1 with CLU, APOH, C3, and F2. STRING enrichment independently recapitulates complement and coagulation, blood microparticles, protein-lipid complexes, circulating plasma proteins, and related proteomics observations (15 supplementary STRING terms; within-query FDR 3.08e-09–9.35e-07). These are supplementary network and literature signals, not global enrichment claims. hu.MAP shows repeated overlap of F2, PLG, C3, and APOA1 in several plasma-protein and complement-associated complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_08796.1), with additional C3-APOA1 and F2-PLG complex overlaps (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_09434.1). Thus, the module is not merely a collection of unrelated correlated genes: its central constituents participate in known biochemical neighborhoods. However, the hu.MAP complexes are larger than this module and often contain many additional plasma proteins, so complex overlap does not prove that all module proteins form one physical complex. ITGAV, NUDT19, NCSTN, and RAB3D have little or no direct STRING or hu.MAP support within the supplied evidence, suggesting that their module association may reflect co-abundance, vesicle biology, or tissue context rather than a shared stable complex.

**STRING interactions (score >= 0.7)**: 22 of 66 gene pairs: APOA1–APOH (0.985); APOA1–C3 (0.957); APOA1–CLU (0.998); APOA1–F2 (0.927); APOA1–SERPINC1 (0.708); APOA1–VTN (0.755); APOH–CLU (0.911); APOH–F2 (0.984); APOH–PLG (0.94); APOH–SERPINC1 (0.944); APOH–VTN (0.787); C3–CLU (0.803); C3–F2 (0.874); C3–PLG (0.978); C3–VTN (0.79); CLU–VTN (0.962); F2–PLG (0.826); F2–SERPINC1 (0.999); ITGAV–VTN (0.999); PLG–SERPINC1 (0.992); PLG–VTN (0.995); SERPINC1–VTN (0.949)
**STRING functional enrichment (supplementary, within-query FDR)**: PMID (2022) Circulating Proteins Associated with Response and Resistance to Neoadjuvant Chemotherapy in HER2-Positive Breast Cancer. (FDR = 3.08e-09, 8 genes); KEGG Complement and coagulation cascades (FDR = 3.21e-09, 6 genes); NetworkNeighborAL Complement and coagulation cascades, and Protein-lipid complex (FDR = 8.1e-09, 7 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 2.88e-08, 8 genes); Component Blood microparticle (FDR = 5.3e-08, 7 genes); COMPARTMENTS Blood microparticle (FDR = 5.74e-08, 7 genes); Keyword Signal (FDR = 1.78e-07, 10 genes); PMID (2019) Label-Free Proteomics Revealed Oxidative Stress and Inflammation as Factors That Enhance Chemoresistance in Luminal Breast Cancer. (FDR = 1.93e-07, 7 genes); PMID (2014) Proteomic analysis of human plasma in chronic rheumatic mitral stenosis reveals proteins involved in the complement and coagulation cascade. (FDR = 2.83e-07, 7 genes); WikiPathways Complement and coagulation cascades (FDR = 4.11e-07, 5 genes); Keyword Glycoprotein (FDR = 5.76e-07, 10 genes); PMID (2013) Transient limb ischemia alters serum protein expression in healthy volunteers: complement C3 and vitronectin may be involved in organ protection induced by remote ischemic preconditioning. (FDR = 6.75e-07, 6 genes); PMID (2024) The in vitro gastrointestinal digestion-associated protein corona of polystyrene nano- and microplastics increases their uptake by human THP-1-derived macrophages. (FDR = 9.35e-07, 6 genes); PMID (2022) MS-proteomics provides insight into the host responses towards alginate microspheres. (FDR = 9.35e-07, 6 genes); PMID (2020) Novel Associations between Related Proteins and Cellular Effects of High-Density Lipoprotein. (FDR = 9.35e-07, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (PLG, SERPINC1, C3, APOA1, APOH; 5/64); huMAP3_08395.1 (F2, PLG, C3, APOA1; 4/43); huMAP3_09531.1 (F2, PLG, C3, APOA1; 4/47); huMAP3_10101.1 (F2, PLG, C3, APOA1; 4/49); huMAP3_10678.1 (F2, PLG, C3, APOA1; 4/71); huMAP3_08796.1 (F2, PLG; 2/15); huMAP3_07432.1 (C3, APOA1; 2/18); huMAP3_09832.1 (F2, PLG; 2/18); huMAP3_08224.1 (C3, APOA1; 2/21); huMAP3_07701.1 (F2, PLG; 2/22); huMAP3_09273.1 (F2, PLG; 2/28); huMAP3_09434.1 (C3, APOA1; 2/33)

### Novelty

This should not be presented as a newly discovered coagulation or complement pathway. The core biology is already extensively established by the annotations, STRING relationships, hu.MAP overlaps, disease associations, and substantial literature for C3, F2, PLG, APOA1, and related proteins. The potentially interesting finding is the conservation of this coordinated abundance pattern across circulatory_system and ovary, together with the inclusion of less connected genes such as ITGAV, NCSTN, RAB3D, and NUDT19. That cross-tissue module organization could be novel, but the fact sheet does not provide an independent comparison against published co-abundance modules, tissue-specific proteomic studies, or prior network definitions. Absence of STRING or hu.MAP support for some peripheral genes is evidence of limited prior interaction annotation, not proof of novelty. The most defensible conclusion is that the biochemical components are established, while the particular cross-tissue co-abundance configuration remains a candidate observation requiring replication and comparison with existing datasets.

**Hypothesis.** Hypothesis: the conserved module reflects a shared circulating-protein program in which liver-derived plasma proteins enter extracellular vesicle or microparticle-associated compartments and jointly regulate vascular protease balance, complement activity, fibrinolysis, lipid transport, and tissue repair in both circulatory_system and ovary. In this model, F2 supplies procoagulant protease activity, SERPINC1 provides an inhibitory counterweight, PLG supports fibrinolytic and matrix-remodeling capacity, C3 contributes complement and inflammatory signaling, and VTN links protease and lipoprotein biology to integrin-mediated cell-matrix interactions. APOA1, APOH, and CLU may organize or stabilize the lipid-associated extracellular environment. The association of ITGAV, NCSTN, and RAB3D with the module could indicate coupling to cell adhesion, membrane processing, or regulated secretion, but this peripheral interpretation is explicitly hypothetical. A key alternative is that the module primarily reflects variable plasma contamination or vascular content in tissue samples rather than local ovarian production.

### Important genes

#### F2

- **Related proteins** (co-abundance neighbors): VTN (0.90), ITGAV (0.88), APOA1 (0.83); STRING partners: APOA1 (0.927), APOH (0.984), C3 (0.874), PLG (0.826), SERPINC1 (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07701.1, huMAP3_09273.1
- **Function (MyGene.info)**: coagulation factor II, thrombin. This gene encodes the prothrombin protein (also known as coagulation factor II). This protein is proteolytically cleaved in multiple steps to form the activated serine protease thrombin. The activated thrombin enzyme plays an important role in thrombosis and hemostasis by converting fibrinogen to fibrin during blood clot formation, by stimulating platelet aggregation, and by activating additional …
- **Diseases (Open Targets)**: congenital prothrombin deficiency (0.827); thrombophilia due to thrombin defect (0.738); venous thromboembolism (0.727); deep vein thrombosis (0.690); blood coagulation disease (0.670)
- **Europe PMC papers**: 109299
- **Why important**: F2 is a central module gene with direct links to VTN, ITGAV, and APOA1 in the module network. It is present across the core complement and coagulation, blood microparticle, coagulation, fibrinolysis, hemostasis, wound-response, and receptor-related enrichments (50 globally significant GO/KEGG terms, q_global 3.84e-08–0.049; see the table). Its encoded thrombin is an established coagulation protease that converts fibrinogen to fibrin, activates platelets and coagulation factors, and participates in repair and angiogenesis. It has extensive literature and strong disease links to prothrombotic and thrombotic disorders.
- **Conclusion**: Established conclusion: F2 is a biochemical anchor of the module and strongly supports a coagulation and tissue-repair interpretation. Hypothesis: variation in F2 abundance may help couple the circulating module to vascular or ovarian remodeling, but the co-abundance data do not demonstrate local thrombin activation.

#### C3

- **Related proteins** (co-abundance neighbors): CLU (0.90); STRING partners: APOA1 (0.957), CLU (0.803), F2 (0.874), PLG (0.978), VTN (0.79)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_08224.1, huMAP3_09434.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a central complement component with STRING links to APOA1, CLU, F2, PLG, and VTN, and it appears in multiple hu.MAP plasma and complement-associated complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_09434.1). It supports the globally corrected complement and coagulation pathway (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 3.84e-08), blood microparticle and extracellular-vesicle terms (8 globally significant GO/KEGG terms, q_global 4e-07–0.0028; see the table), humoral immune response (GO:BP humoral immune response; q_global = 0.042), and receptor-related terms (5 globally significant GO/KEGG terms, q_global 0.000813–0.0138; see the table). C3 is a central complement activator and source of inflammatory peptides, has very extensive literature, and is associated with complement deficiencies and complement-mediated disease.
- **Conclusion**: Established conclusion: C3 gives the module a clear complement and innate immune dimension in addition to coagulation. Hypothesis: C3 may connect circulating protein abundance to local inflammatory or tissue-remodeling responses in ovary, but activation state cannot be inferred from abundance alone.

#### PLG

- **Related proteins** (co-abundance neighbors): VTN (0.94); STRING partners: APOH (0.94), C3 (0.978), F2 (0.826), SERPINC1 (0.992), VTN (0.995)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07701.1, huMAP3_09273.1
- **Function (MyGene.info)**: plasminogen. The plasminogen protein encoded by this gene is a serine protease that circulates in blood plasma as an inactive zymogen and is converted to the active protease, plasmin, by several plasminogen activators such as tissue plasminogen activator (tPA), urokinase plasminogen activator (uPA), kallikrein, and factor XII (Hageman factor). The conversion of plasminogen to plasmin involves the cleavage of t…
- **Diseases (Open Targets)**: hypoplasminogenemia (0.813); hereditary angioedema (0.737); hemorrhage (0.605); dysplasminogenemia (0.598); Menorrhagia (0.579)
- **Europe PMC papers**: 17740
- **Why important**: PLG is linked in the module network to VTN and is strongly connected in STRING to APOH, C3, F2, SERPINC1, and VTN. It occurs throughout the primary fibrinolysis, coagulation, wound-healing, extracellular, and vesicle enrichments (45 globally significant GO/KEGG terms, q_global 3.84e-08–0.049; see the table). Plasminogen is a circulating zymogen that can become plasmin, enabling fibrinolysis and extracellular-matrix breakdown; its established disease associations include plasminogen deficiency, hemorrhage, dysplasminogenemia, and menorrhagia. It has extensive literature.
- **Conclusion**: Established conclusion: PLG is a principal fibrinolytic and matrix-remodeling component of the module. Hypothesis: coordinated PLG and VTN abundance could influence extracellular-matrix turnover or angiogenic remodeling near ovarian tissue, but enzymatic activity and tissue origin remain untested.

#### VTN

- **Related proteins** (co-abundance neighbors): PLG (0.94), F2 (0.90); STRING partners: APOA1 (0.755), APOH (0.787), C3 (0.79), CLU (0.962), ITGAV (0.999), PLG (0.995), SERPINC1 (0.949)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vitronectin. The protein encoded by this gene functions in part as an adhesive glycoprotein. Differential expression of this protein can promote either cell adhesion or migration as it links cells to the extracellular matrix through a variety of ligands. These ligands include integrins, plasminogen activator inhibitor-1, and urokinase plasminogen activator receptor. This secreted protein can be present in the …
- **Diseases (Open Targets)**: hypertensive disorder (0.421); dengue disease (0.376); neurodegenerative disease (0.343); temporal arteritis (0.338); age-related macular degeneration (0.313)
- **Europe PMC papers**: 3940
- **Why important**: VTN is a network bridge between PLG and F2 and has very strong STRING relationships with ITGAV, PLG, CLU, and SERPINC1. It is present in the core complement/coagulation, fibrinolysis, wound response, extracellular-vesicle, cell-surface, heparin-binding, and receptor-endocytosis enrichments (54 globally significant GO/KEGG terms, q_global 3.84e-08–0.0492; see the table). Vitronectin is a secreted adhesive glycoprotein that binds integrins and other extracellular ligands and can connect plasma protease regulation with cell-matrix adhesion and migration. Its literature is substantial and includes vascular, inflammatory, and tissue-remodeling contexts.
- **Conclusion**: Established conclusion: VTN is a plausible extracellular scaffold or interface connecting coagulation, fibrinolysis, and integrin biology. Hypothesis: VTN may mediate communication between the circulating module and ovarian or vascular cell surfaces, especially through ITGAV, but this cannot be established from the network alone.

#### APOA1

- **Related proteins** (co-abundance neighbors): CLU (0.91), SERPINC1 (0.91), F2 (0.83); STRING partners: APOH (0.985), C3 (0.957), CLU (0.998), F2 (0.927), SERPINC1 (0.708), VTN (0.755)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_08224.1, huMAP3_09434.1
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 has a prominent network position and connects to CLU, SERPINC1, and F2 within the module. It has broad STRING support with APOH, C3, CLU, F2, SERPINC1, and VTN and participates in many hu.MAP plasma-protein complex overlaps (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_09434.1). It drives the blood microparticle, lipoprotein, HDL, extracellular-vesicle, protein-lipid, receptor-binding, endocytosis, and stress-response evidence (33 globally significant GO/KEGG terms, q_global 4e-07–0.049; see the table). APOA1 is the major HDL protein, supports cholesterol efflux, and has very extensive literature and established associations with HDL disorders and apolipoprotein deficiency.
- **Conclusion**: Established conclusion: APOA1 indicates that the module includes lipid transport and plasma lipoprotein biology rather than being a pure coagulation pathway. Hypothesis: HDL-associated APOA1 may alter the extracellular presentation or transport of complement and protease regulators across tissues, but such molecular coordination is not demonstrated here.

## Module 1

**Tissue pair**: circulatory_system and ovary  
**Genes (5)**: ATXN2, PYM1, SEC16A, SURF6, UBAP2

### Function

This is a small, internally connected module with no GO/KEGG term passing global correction. Its genes point to complementary intracellular processes rather than a single established pathway: SEC16A supports endoplasmic-reticulum-to-Golgi export and vesicle formation; SURF6 is associated with nucleolar organization and ribosomal-subunit biogenesis; UBAP2 contains a ubiquitin-associated domain and is linked to regulation of gene expression; PYM1 participates in exon-junction-complex disassembly, nonsense-mediated decay and translation; and ATXN2 is involved in RNA metabolism, translation, P-body and stress-granule biology, as well as endoplasmic-reticulum and plasma-membrane functions. The network therefore suggests a possible connection between intracellular trafficking, RNA or ribosome-related regulation, and protein or RNA quality control, but this is an integrative hypothesis rather than a significantly enriched pathway. No GO/KEGG term passed global correction.

**Cell composition.** The module does not look like a plasma-protein, secreted-protein or blood-cell module. All genes are non-secreted, all have low immune-cell specificity, and all have low tissue specificity. The HPA single-cell evidence identifies cell-type enhancement for SURF6 and PYM1 in selected non-blood cell populations, while the other genes have low cell-type specificity. Ovary protein detection is mixed across the module, and there is no matching circulatory-system HPA tissue result. Overall, the shared signal is more consistent with broadly distributed intracellular genes, or with shared cellular composition, than with a circulating protein program or blood-cell contamination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No qualifying STRING interaction is reported among the module genes, and no STRING functional-enrichment result is available. No hu.MAP complex contains at least two module members. Thus, the co-abundance edges are not supported by the supplied high-confidence physical-interaction or curated-complex evidence. The absence of these relationships does not disprove coordinated regulation, but it argues against interpreting the module as a known protein complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The co-abundance pattern may be a new tissue-pair observation, because the supplied databases do not identify a shared STRING interaction, STRING enrichment signal or hu.MAP complex. However, it should not be called a newly discovered biological pathway: every gene has established individual functions, and co-abundance can arise from shared expression control, cell composition, technical structure or indirect biological coupling. The most defensible conclusion is that the cross-tissue module-level association is potentially novel, whereas its component biology is not established as a unified mechanism.

**Hypothesis.** Hypothesis: in both circulatory-system and ovary samples, a shared intracellular state may coordinate secretory-pathway capacity with RNA surveillance, translation control and stress-related RNA handling. SEC16A could represent endoplasmic-reticulum export capacity, SURF6 and PYM1 could represent nucleolar or RNA-processing activity, and UBAP2 together with ATXN2 could connect ubiquitin-related regulation, RNA metabolism and cellular stress responses. This model is provisional because there is no globally significant enrichment, no qualifying STRING interaction and no hu.MAP complex support.

### Important genes

#### SEC16A

- **Related proteins** (co-abundance neighbors): SURF6 (0.85), PYM1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC16 homolog A, endoplasmic reticulum export factor. This gene encodes a protein that forms part of the Sec16 complex. This protein has a role in protein transport from the endoplasmic reticulum (ER) to the Golgi and mediates COPII vesicle formation at the transitional ER. Alternative splicing results in multiple transcript variants that encode different protein isoforms. [provided by RefSeq, Feb 2013].
- **Diseases (Open Targets)**: squamous cell carcinoma (0.288); Crohn disease (0.277); bladder calculus (0.241); nephrolithiasis (0.235); actinic keratosis (0.215)
- **Europe PMC papers**: 595
- **Why important**: SEC16A is a central connector in the module, linking SURF6 and PYM1. Its established role in endoplasmic-reticulum organization, COPII vesicle formation and transport toward the Golgi gives the module a plausible intracellular-trafficking axis. It also has substantial literature coverage and disease-oriented associations, making it a useful anchor for interpretation.
- **Conclusion**: Established evidence supports SEC16A as an ER-export and secretory-pathway regulator with a central network position. It is a candidate driver of the shared co-abundance pattern, but the supplied evidence does not establish that it mechanistically regulates the other module genes.

#### ATXN2

- **Related proteins** (co-abundance neighbors): UBAP2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ataxin 2. This gene belongs to a group of genes that is associated with microsatellite-expansion diseases, a class of neurological and neuromuscular disorders caused by expansion of short stretches of repetitive DNA. The protein encoded by this gene has two globular domains near the N-terminus, one of which contains a clathrin-mediated trans-Golgi signal and an endoplasmic reticulum exit signal. The encoded…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 2 (0.652); amyotrophic lateral sclerosis (0.446); Parkinson disease (0.309); Abnormality of the skeletal system (0.308); coronary artery disorder (0.298)
- **Europe PMC papers**: 2892
- **Why important**: ATXN2 has the strongest network-level disease and literature context in the module and is connected to UBAP2. Its established functions include regulation of translation, RNA metabolism, P-body and stress-granule assembly, and localization involving the endoplasmic reticulum and plasma membrane. Its association with spinocerebellar ataxia type two and other neurological disorders makes it biologically important beyond this module.
- **Conclusion**: Established evidence supports ATXN2 as an RNA- and stress-regulatory cytoplasmic protein with major disease relevance. Its module relationship with UBAP2 is a co-abundance observation, not evidence that this module causes ATXN2-associated disease.

#### SURF6

- **Related proteins** (co-abundance neighbors): SEC16A (0.85), UBAP2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: surfeit 6. This gene encodes a conserved protein that is localized to the nucleolus. The encoded protein may function as a nucleolar-matrix protein with nucleic acid-binding properties. There is a pseudogene for this gene on chromosome Y. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013].
- **Diseases (Open Targets)**: neurodegenerative disease (0.513); colorectal carcinoma (0.074); edema (0.032); brain compression (0.032); neoplasm (0.030)
- **Europe PMC papers**: 376
- **Why important**: SURF6 is an internal connector between SEC16A and UBAP2. It is a conserved nucleolar protein associated with ribosomal-subunit biogenesis and shows cell-type enhancement in several non-blood populations, including neuronal and renal epithelial populations. Its ovary protein detection provides tissue-level support for its presence in one member of the tissue pair.
- **Conclusion**: Established evidence supports SURF6 as a nucleolar and ribosome-biogenesis factor. Its position may indicate coordination between biosynthetic activity and trafficking, but that cross-process interpretation remains a hypothesis.

#### PYM1

- **Related proteins** (co-abundance neighbors): SEC16A (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PYM1 exon junction complex associated factor. Enables ribosome binding activity. Involved in exon-exon junction complex disassembly; nuclear-transcribed mRNA catabolic process, nonsense-mediated decay; and positive regulation of translation. Located in cell junction; cytosol; and nuclear lumen. Part of exon-exon junction complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Alzheimer disease (0.049); esophageal cancer (0.033); neoplasm (0.030); hypothyroidism (0.026); cancer (0.025)
- **Europe PMC papers**: 132
- **Why important**: PYM1 is a peripheral connector attached to SEC16A and contributes a distinct RNA-processing and translation axis. It is associated with exon-junction-complex disassembly, nonsense-mediated decay and positive regulation of translation. Its cell-type enhancement in esophageal epithelial populations and ovary protein detection support regulated cellular expression, although not tissue specificity across the pair.
- **Conclusion**: Established evidence supports PYM1 in mRNA surveillance and translation control. Its connection to SEC16A may reflect coordinated cellular state or indirect co-expression; no physical interaction or unified pathway is established here.

#### UBAP2

- **Related proteins** (co-abundance neighbors): SURF6 (0.81), ATXN2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin associated protein 2. The protein encoded by this gene contains a UBA (ubiquitin associated) domain, which is characteristic of proteins that function in the ubiquitination pathway. This gene may show increased expression in the adrenal gland and lymphatic tissues. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: osteoarthritis (0.294); systemic lupus erythematosus (0.275); atrial fibrillation (0.274); Hypervolemia (0.221); type 2 diabetes mellitus (0.211)
- **Europe PMC papers**: 786
- **Why important**: UBAP2 is the bridge between SURF6 and ATXN2, placing it at the junction of the nucleolar or biosynthetic side and the RNA- or stress-regulatory side of the module. Its ubiquitin-associated domain supports a role in ubiquitination-related regulation, while its reported associations include immune, cardiovascular and metabolic disease contexts. It also has broad literature coverage relative to most module members.
- **Conclusion**: Established evidence supports UBAP2 as a ubiquitin-associated regulatory protein with gene-expression relevance. Its bridging position makes it a strong candidate for follow-up, but the supplied data do not demonstrate that it physically links SURF6 and ATXN2.

## Module 2

**Tissue pair**: circulatory_system and ovary  
**Genes (7)**: ALCAM, DNAJC10, MAN2A1, MAIP1, MYOF, PPP1R9B, RRBP1

### Function

The module is a sparse, connected co-abundance structure linking several intracellular protein-handling and membrane-associated processes rather than defining a single established canonical pathway. RRBP1 and DNAJC10 support an endoplasmic-reticulum protein quality-control and secretory context; MAN2A1 supports Golgi N-glycan maturation; MAIP1 supports mitochondrial protein insertion and calcium homeostasis; MYOF supports calcium-dependent membrane fusion and membrane repair; ALCAM supports cell adhesion and migration; and PPP1R9B supports phosphatase regulation and actin organization. The module therefore most plausibly reflects coordinated secretory-pathway, membrane-remodelling, adhesion, and cellular stress biology. No GO or KEGG term passed global correction, so this interpretation is based on the individual gene annotations and the co-abundance structure, not on significant pathway enrichment. The annotations are heterogeneous, and the module should not be assigned a more specific pathway without experimental validation.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. ALCAM is annotated as secreted to blood, whereas the other genes are intracellular or membrane-associated, including endoplasmic-reticulum, Golgi, mitochondrial, vesicular, and plasma-membrane localizations. HPA evidence in ovary detects protein for most module genes, with one gene not detected; there is no matching HPA tissue result for circulatory_system. Tissue specificity is mixed, with signals involving pancreas, epididymis, brain, and parathyroid gland rather than a single dominant tissue. Cell-type enhancement is widespread and includes ovarian-related endometrial cell types, acinar cells, oocytes, monocytes, dendritic cells, and other cell types. Several genes have immune-cell enhancement, but most have low immune-cell specificity. Thus, shared cellular composition, tissue sampling, or blood-associated cellular admixture could contribute to the shared signal, but the HPA summary does not establish that the module is simply a blood-cell or plasma-protein signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The module has no qualifying STRING interactions among its member pairs and no hu.MAP complex containing multiple module members. Consequently, the co-abundance edges are not independently supported here by high-confidence STRING physical or functional associations, nor by a known hu.MAP complex. The absence of these resources' support argues against interpreting the module as a demonstrated protein complex. It does not exclude indirect regulation, tissue-specific co-expression, transient contacts, shared organelle biology, or interactions absent from the reference resources. The network itself is sparse but connected, with MAIP1 and RRBP1 occupying the main bridging positions, while MAN2A1 links RRBP1 to ALCAM.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared co-abundance module is a potentially novel systems-level observation because its specific gene combination has no qualifying STRING interaction support, no multi-member hu.MAP complex support, and no globally significant GO or KEGG enrichment. However, these absences do not prove novelty. The component genes and several of their individual functions are established and well studied, especially ALCAM, RRBP1, MYOF, MAN2A1, and DNAJC10. The defensible conclusion is that a novel shared co-abundance pattern is plausible, but a new biological mechanism or new protein interaction network has not been demonstrated. Replication in independent circulatory-system and ovary datasets, control for cell composition, and targeted validation would be needed to establish novelty.

**Hypothesis.** Hypothesis: the module represents a shared state of secretory and membrane-intensive cells in which endoplasmic-reticulum quality control and glycoprotein processing are coordinated with mitochondrial calcium handling, vesicle or membrane repair, cell adhesion, and cytoskeletal signalling. In this model, RRBP1 and DNAJC10 support handling of secretory-pathway protein load, MAN2A1 modifies the resulting glycoproteins, MAIP1 and MYOF couple calcium-dependent organelle or membrane dynamics, and ALCAM with PPP1R9B links the state to adhesion and cytoskeletal regulation. This is a mechanistic hypothesis derived from co-abundance and gene function; it is not established by the enrichment, STRING, or hu.MAP evidence.

### Important genes

#### MAIP1

- **Related proteins** (co-abundance neighbors): MYOF (0.85), RRBP1 (0.84), DNAJC10 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: matrix AAA peptidase interacting protein 1. Predicted to enable ribosome binding activity. Involved in calcium import into the mitochondrion; mitochondrial calcium ion homeostasis; and protein insertion into mitochondrial membrane. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: schizophrenia (0.251); Abnormality of the skeletal system (0.197); autism spectrum disorder (0.171); metabolic disease (0.162); bipolar disorder (0.157)
- **Europe PMC papers**: 75
- **Why important**: MAIP1 has one of the strongest network positions and connects RRBP1, MYOF, and DNAJC10, making it a central bridge between endoplasmic-reticulum quality control and membrane or mitochondrial biology. Its established annotations include mitochondrial protein insertion and mitochondrial calcium homeostasis, and HPA places it in mitochondria with oocyte cell-type enhancement. Its disease associations include neuropsychiatric and metabolic traits, while its literature is comparatively limited relative to the better studied adhesion and ER genes, making its central position especially informative.
- **Conclusion**: Established: MAIP1 is a mitochondrial protein associated with protein insertion and calcium homeostasis, and it is a network bridge in this module. Hypothesis: MAIP1 may coordinate mitochondrial calcium or membrane capacity with secretory and membrane stress in the shared tissue state. The co-abundance data do not establish that it causally controls the other genes.

#### RRBP1

- **Related proteins** (co-abundance neighbors): PPP1R9B (0.85), MAIP1 (0.84), MAN2A1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosome binding protein 1. This gene encodes a ribosome-binding protein of the endoplasmic reticulum (ER) membrane. Studies suggest that this gene plays a role in ER proliferation, secretory pathways and secretory cell differentiation, and mediation of ER-microtubule interactions. Alternative splicing has been observed and protein isoforms are characterized by regions of N-terminal decapeptide and C-terminal heptad repeats.…
- **Diseases (Open Targets)**: cancer (0.476); dengue disease (0.462); neurodegenerative disease (0.324); coronary artery disorder (0.292); placental abruption (0.279)
- **Europe PMC papers**: 1654
- **Why important**: RRBP1 is a central network connector linked to MAIP1, PPP1R9B, and MAN2A1. It is an endoplasmic-reticulum ribosome-binding protein implicated in ER proliferation, secretory pathways, secretory-cell differentiation, translation, and protein transport. HPA shows tissue enhancement in pancreas and cell-type enhancement in acinar cells and syncytiotrophoblasts, consistent with secretory biology. It has substantial literature and disease associations including cancer, dengue disease, neurodegenerative disease, and coronary artery disorder.
- **Conclusion**: Established: RRBP1 is a well-studied ER and secretory-pathway component and a major network connector here. Hypothesis: it may be a principal marker of increased secretory or ER-handling demand in the shared module. Its network position does not prove direct physical interaction with the neighboring proteins.

#### ALCAM

- **Related proteins** (co-abundance neighbors): MAN2A1 (0.90); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: activated leukocyte cell adhesion molecule. This gene encodes activated leukocyte cell adhesion molecule (ALCAM), also known as CD166 (cluster of differentiation 166), which is a member of a subfamily of immunoglobulin receptors with five immunoglobulin-like domains (VVC2C2C2) in the extracellular domain. This protein binds to T-cell differentiation antigene CD6, and is implicated in the processes of cell adhesion and migration. Multiple al…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.458); mathematical ability (0.453); open-angle glaucoma (0.396); restless legs syndrome (0.379); ovarian dysfunction (0.362)
- **Europe PMC papers**: 4212
- **Why important**: ALCAM is the terminal adhesion-associated member connected through MAN2A1 and is the only gene annotated as secreted to blood. It encodes CD166, an immunoglobulin-family cell-adhesion receptor involved in cell adhesion and migration, with HPA enrichment in parathyroid gland and enhancement across several epithelial and endometrial cell types as well as myeloid dendritic cells. It has the largest literature volume in the module and an Open Targets association with ovarian dysfunction, making it particularly relevant to the tissue pair.
- **Conclusion**: Established: ALCAM is an adhesion and migration molecule with ovarian protein detection and broad epithelial or immune cell-type signals. Hypothesis: ALCAM may connect the intracellular processing program to altered cell-cell interaction or tissue-interface biology. The module does not show that ALCAM secretion or adhesion is the cause of the shared co-abundance pattern.

#### MAN2A1

- **Related proteins** (co-abundance neighbors): ALCAM (0.90), RRBP1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosidase alpha class 2A member 1. This gene encodes a glycosyl hydrolase that localizes to the Golgi and catalyzes the final hydrolytic step in the asparagine-linked oligosaccharide (N-glycan) maturation pathway. Mutations in the mouse homolog of this gene have been shown to cause a systemic autoimmune disease similar to human systemic lupus erythematosus. [provided by RefSeq, Dec 2013].
- **Diseases (Open Targets)**: alcohol drinking (0.456); schizophrenia (0.455); COVID-19 (0.370); smoking initiation (0.364); dislocation (0.344)
- **Europe PMC papers**: 663
- **Why important**: MAN2A1 links RRBP1 to ALCAM and occupies the module's glycoprotein-processing branch. It is a Golgi mannosidase that catalyzes a final step in N-glycan maturation and is annotated for carbohydrate and mannose metabolism and N-glycan processing. HPA places it in the Golgi and shows oligodendrocyte cell-type enrichment, while its disease and trait associations include systemic autoimmune relevance through the mouse homolog, schizophrenia, COVID-19, and other traits. Its literature is substantial.
- **Conclusion**: Established: MAN2A1 is a Golgi N-glycan maturation enzyme and the network link between the ER-associated RRBP1 branch and ALCAM. Hypothesis: coordinated MAN2A1 activity may modify the surface abundance or glycosylation state of adhesion and secretory proteins in the shared tissue context. This functional connection is plausible but not proven by the module.

#### MYOF

- **Related proteins** (co-abundance neighbors): MAIP1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Plasma membrane, Centriolar satellite; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myoferlin. Mutations in dysferlin, a protein associated with the plasma membrane, can cause muscle weakness that affects both proximal and distal muscles. The protein encoded by this gene is a type II membrane protein that is structurally similar to dysferlin. It is a member of the ferlin family and associates with both plasma and nuclear membranes. The protein contains C2 domains that play a role in calcium…
- **Diseases (Open Targets)**: hereditary angioedema (0.443); neurodegenerative disease (0.413); cervical carcinoma (0.134); type 2 diabetes mellitus (0.131); neoplasm (0.112)
- **Europe PMC papers**: 1200
- **Why important**: MYOF is connected to the central MAIP1 branch and provides a membrane-dynamics component. It is a ferlin-family membrane protein with C two domains implicated in calcium-mediated membrane fusion, and its annotations include plasma-membrane repair, muscle contraction, blood circulation, and regulation of neurotransmitter secretion. HPA shows vesicular and plasma-membrane localization, endometrial and other epithelial cell-type enhancement, and immune-cell enhancement in monocytes. It also has substantial literature and disease associations including hereditary angioedema and neurodegenerative disease.
- **Conclusion**: Established: MYOF is a calcium-sensitive membrane and vesicle protein connected to MAIP1. Hypothesis: MYOF may couple mitochondrial or cellular calcium handling to membrane repair and vesicle trafficking in the shared module. The co-abundance edge does not demonstrate a direct MYOF-MAIP1 interaction.

#### DNAJC10

- **Related proteins** (co-abundance neighbors): MAIP1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DnaJ heat shock protein family (Hsp40) member C10. This gene encodes an endoplasmic reticulum co-chaperone which is part of the endoplasmic reticulum-associated degradation complex involved in recognizing and degrading misfolded proteins. The encoded protein reduces incorrect disulfide bonds in misfolded glycoproteins. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Oct 20…
- **Diseases (Open Targets)**: dengue disease (0.370); dry eye syndrome (0.321); type 2 diabetes mellitus (0.317); neurodegenerative disease (0.307); response to antihypertensive drug (0.294)
- **Europe PMC papers**: 547
- **Why important**: DNAJC10 is connected to MAIP1 and adds a defined ER quality-control function. It is an ER co-chaperone involved in recognizing misfolded proteins, reducing incorrect disulfide bonds, ER-associated degradation, ER stress responses, and the IRE1-mediated unfolded-protein response. HPA shows enhancement in epididymal principal cells and low immune-cell specificity. Its literature includes work on ER stress, diabetes, neurodegeneration, and drug response, although it is less extensively studied than ALCAM or RRBP1.
- **Conclusion**: Established: DNAJC10 is an ER proteostasis and ER-stress factor linked to MAIP1 in the module. Hypothesis: it may indicate that the shared co-abundance state includes increased demand for disulfide-bond correction or ER-associated degradation. The data do not show that the module is an unfolded-protein-response module in the absence of global enrichment.

## Module 3

**Tissue pair**: circulatory_system and ovary  
**Genes (6)**: KRT10, KRT14, KRT9, KRT2, KRT1, KRT5

### Function

This is a coherent epithelial keratin and cornified-envelope module. Every module gene contributes to the globally corrected keratin-filament, intermediate-filament, epithelial-development, and skin-development signals (7 globally significant GO/KEGG terms, q_global 2.91e-11–1.13e-07; see the table), (GO:BP skin development; q_global = 1.18e-06) (GO:BP epidermis development; q_global = 1.4e-06), (GO:BP epithelial cell differentiation; q_global = 4.39e-05), (4 globally significant GO/KEGG terms, q_global 0.000161–0.000789; see the table), and (GO:CC supramolecular polymer; q_global = 0.00107) (GO:CC supramolecular fiber; q_global = 0.00107). The module also supports keratinocyte differentiation, keratinization, cytoskeletal organization, and structural epidermal function (GO:MF structural constituent of skin epidermis; q_global = 2.36e-07), (GO:BP keratinocyte differentiation; q_global = 6.4e-06) (GO:BP epidermal cell differentiation; q_global = 2.38e-05), (GO:BP keratinization; q_global = 0.000857), (GO:BP peptide cross-linking; q_global = 0.00121), and (GO:MF structural constituent of cytoskeleton; q_global = 0.00337) (GO:BP tissue development; q_global = 0.0039) (GO:BP cytoskeleton organization; q_global = 0.01). The cadherin-signaling, Staphylococcus-aureus-infection, and estrogen-signaling annotations (KEGG Cadherin signaling - Homo sapiens (human); q_global = 2.11e-06), (KEGG Staphylococcus aureus infection - Homo sapiens (human); q_global = 0.00222), and (KEGG Estrogen signaling pathway - Homo sapiens (human); q_global = 0.0209) are consistent with epithelial junctional, barrier, or tissue-context biology, but they should not be interpreted as evidence that this module directly controls infection or estrogen signaling. The strongest interpretation is a structural and differentiation program of stratified epithelial cells.

**Cell composition.** The module is not predominantly composed of plasma proteins or secreted proteins; it consists of intracellular keratin intermediate-filament proteins, with only KRT10 annotated as secreted in other tissues. HPA evidence strongly points to skin and keratinocyte biology: most genes are tissue enriched in skin, and the dominant single-cell annotations are suprabasal or basal keratinocytes. KRT5 also has enrichment across cervix, esophagus, skin, and vagina, while KRT9 has lymphoid-tissue enrichment and several cell-type-enhanced annotations. The genes are generally absent or weakly specific in immune cells, although individual immune-cell enhancement annotations occur. Protein detection in ovary is absent for all module genes. Therefore, the shared circulatory-system and ovary signal should not be treated as evidence of an ovary or blood-cell-specific program. It more plausibly reflects epithelial material, epithelial cell admixture, tissue-interface biology, or sample composition shared across the tissue groups. The absence of matching circulatory-system HPA protein evidence further limits a direct tissue-localization interpretation.

**GO/KEGG enrichment**: 30 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC keratin filament | 2.91e-11 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament organization | 3.88e-10 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament-based process | 3.88e-09 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament cytoskeleton organization | 3.88e-09 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:CC intermediate filament | 1.54e-08 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:CC intermediate filament cytoskeleton | 1e-07 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| KEGG Cornified envelope formation - Homo sapiens (human) | 1.13e-07 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:MF structural constituent of skin epidermis | 2.36e-07 | KRT1, KRT10, KRT2, KRT5 |
| GO:BP skin development | 1.18e-06 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP epidermis development | 1.4e-06 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| KEGG Cadherin signaling - Homo sapiens (human) | 2.11e-06 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP keratinocyte differentiation | 6.4e-06 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| GO:BP epidermal cell differentiation | 2.38e-05 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| GO:BP epithelial cell differentiation | 4.39e-05 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:CC cornified envelope | 5.31e-05 | KRT1, KRT10, KRT14, KRT2 |

### STRING and hu.MAP

STRING independently supports the interpretation: all module genes are represented in keratin, keratin-filament, intermediate-filament, conserved rod-domain, and cornified-envelope annotations (8 supplementary STRING terms; within-query FDR 5.37e-12–1.66e-10). The high-confidence pairwise relationships include KRT1 with KRT10, KRT2, and KRT5; KRT10 with KRT2 and KRT5; and KRT5 with KRT14 and KRT2. These relationships are biologically expected for interacting type I and type II keratin partners and indicate that the co-abundance structure is concordant with established keratin biology rather than an arbitrary correlation pattern. KRT9 lacks a reported STRING partner within this module, despite its compatible epithelial and epidermal annotations; this absence does not negate its biological membership. STRING literature associations also connect the module to keratoderma, keratinization, wound-healing, and keratin biomaterial biology (7 supplementary STRING terms; within-query FDR 2.14e-09–3.13e-09). No hu.MAP complex contains multiple module members, so the evidence supports a filamentous structural network rather than a hu.MAP-defined multiprotein complex.

**STRING interactions (score >= 0.7)**: 7 of 15 gene pairs: KRT1–KRT10 (0.999); KRT1–KRT2 (0.956); KRT1–KRT5 (0.923); KRT10–KRT2 (0.904); KRT10–KRT5 (0.793); KRT14–KRT5 (0.999); KRT2–KRT5 (0.871)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Keratin (FDR = 5.37e-12, 6 genes); Component Keratin filament (FDR = 1.24e-11, 6 genes); COMPARTMENTS Keratin filament (FDR = 1.34e-11, 6 genes); Keyword Intermediate filament (FDR = 1.82e-11, 6 genes); SMART Intermediate filament protein (FDR = 1.83e-11, 6 genes); InterPro Intermediate filament protein, conserved site (FDR = 1.03e-10, 6 genes); InterPro Intermediate filament, rod domain (FDR = 1.03e-10, 6 genes); RCTM Formation of the cornified envelope (FDR = 1.66e-10, 6 genes); PMID (2019) Keratin 9 L164P mutation in a Chinese pedigree with epidermolytic palmoplantar keratoderma, cytokeratin analysis, and literature review. (FDR = 2.14e-09, 6 genes); PMID (2025) Mass spectrometric detection of keratins in tear fluid. (FDR = 3.13e-09, 6 genes); PMID (2023) Key Factors in the Complex and Coordinated Network of Skin Keratinization: Their Significance and Involvement in Common Skin Conditions. (FDR = 3.13e-09, 6 genes); PMID (2022) Palmoplantar Keratoderma: A Molecular Genetic Analysis of Family Cases. (FDR = 3.13e-09, 6 genes); PMID (2021) Keratin Biomaterials in Skin Wound Healing, an Old Player in Modern Medicine: A Mini Review. (FDR = 3.13e-09, 6 genes); PMID (2019) Proteome Profiling of the Exhaled Breath Condensate after Long-Term Spaceflights. (FDR = 3.13e-09, 6 genes); PMID (2015) Gene expression profiling in pachyonychia congenita skin. (FDR = 3.13e-09, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is not a new discovery of a keratin-filament or epidermal-differentiation program. The globally corrected GO and KEGG results, the established STRING relationships, the HPA localization, the known keratin pairing biology, and the extensive disease literature all identify a canonical epithelial keratin module. A potentially dataset-specific observation is its shared co-abundance across circulatory-system and ovary samples, but the supplied evidence does not establish that this cross-tissue recurrence is a novel mechanism. The lack of a hu.MAP complex, or the lack of a STRING partner for KRT9, cannot by itself support novelty. A claim of novelty would require independent replication, cellular deconvolution, and evidence that the signal persists after accounting for epithelial contamination or shared cell types.

**Hypothesis.** Hypothesis: the shared module reflects coordinated abundance of keratin proteins from stratified epithelial cells or epithelial-derived material present in both tissue datasets. KRT5 and KRT14 may represent a basal epithelial scaffold, while KRT1, KRT10, KRT2, and KRT9 represent differentiation-associated or terminally differentiated keratin states. Their co-abundance may therefore capture a continuum from basal structural support to suprabasal keratinization and barrier formation. This hypothesis predicts that the module will track epithelial-cell proportion or epithelial injury more strongly than ovary-specific or circulatory-system-specific physiology. It should be tested using matched transcriptomic or proteomic cell-type markers, epithelial deconvolution, and independent cohorts.

### Important genes

#### KRT2

- **Related proteins** (co-abundance neighbors): KRT10 (0.91), KRT1 (0.87), KRT5 (0.85), KRT14 (0.81); STRING partners: KRT1 (0.956), KRT10 (0.904), KRT5 (0.871)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location Intermediate filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 2. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is expressed largely in the upper spinous layer of epidermal keratinocytes and mutations in this gene …
- **Diseases (Open Targets)**: superficial epidermolytic ichthyosis (0.815); exfoliative ichthyosis (0.358); Palmoplantar hyperkeratosis (0.267); hereditary disease (0.193); Vertigo (0.145)
- **Europe PMC papers**: 7459
- **Why important**: KRT2 has the strongest network centrality within the module and connects the KRT1/KRT10 suprabasal keratin group with the KRT5/KRT14 basal keratin group. It participates in every major globally corrected structural and epithelial annotation represented by the module, including keratin filaments, epidermis development, keratinocyte differentiation, and keratinization (23 globally significant GO/KEGG terms, q_global 2.91e-11–0.00121; see the table), (GO:MF structural constituent of cytoskeleton; q_global = 0.00337) (GO:BP tissue development; q_global = 0.0039) (GO:BP cytoskeleton organization; q_global = 0.01), (GO:BP animal organ development; q_global = 0.0224) (GO:CC supramolecular complex; q_global = 0.0274). HPA localizes it to skin and suprabasal keratinocytes. Its established association with bullous congenital ichthyosiform erythroderma and other keratinization disorders, together with an extensive literature record, makes it a strong marker of the module's differentiated epithelial state.
- **Conclusion**: Established: KRT2 is a central suprabasal keratin component with structural epidermal functions and disease relevance. Hypothesis: its central position may make it a useful reporter of the transition from basal to differentiated epithelial material in the shared tissue signal, but causality in this co-abundance module is not demonstrated.

#### KRT1

- **Related proteins** (co-abundance neighbors): KRT10 (0.95), KRT9 (0.88), KRT2 (0.87); STRING partners: KRT10 (0.999), KRT2 (0.956), KRT5 (0.923)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 is a highly connected hub linking KRT10, KRT9, and KRT2, and it also has a strong STRING relationship with KRT5. It is present across the globally corrected keratin-filament, intermediate-filament, epidermal-development, cornified-envelope, and cytoskeletal annotations (7 globally significant GO/KEGG terms, q_global 2.91e-11–1.13e-07; see the table), (GO:BP skin development; q_global = 1.18e-06) (GO:BP epidermis development; q_global = 1.4e-06) (KEGG Cadherin signaling - Homo sapiens (human); q_global = 2.11e-06), (GO:BP epithelial cell differentiation; q_global = 4.39e-05), (4 globally significant GO/KEGG terms, q_global 0.000161–0.000789; see the table), and (10 globally significant GO/KEGG terms, q_global 0.00107–0.0274; see the table). HPA places it in skin and suprabasal keratinocytes. Its established roles in epidermal structure and keratinization, its association with several ichthyosis and palmoplantar keratoderma disorders, and its very extensive literature support make it an important structural anchor.
- **Conclusion**: Established: KRT1 is a central suprabasal intermediate-filament component and a disease-relevant epidermal structural gene. Hypothesis: KRT1 abundance may help define the differentiated epithelial component underlying the cross-tissue co-abundance signal.

#### KRT5

- **Related proteins** (co-abundance neighbors): KRT14 (0.95), KRT2 (0.85); STRING partners: KRT1 (0.923), KRT10 (0.793), KRT14 (0.999), KRT2 (0.871)
- **HPA**: Group enriched; Group enriched; blood Immune cell enriched; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 5. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the basal layer of the epidermis with family member KRT14. Mutations in t…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 2C, localized (0.768); epidermolysis bullosa simplex 2A, generalized severe (0.761); epidermolysis bullosa simplex 2B, generalized intermediate (0.761); epidermolysis bullosa simplex 2F, with mottled pigmentation (0.729); Dowling-Degos disease 1 (0.697)
- **Europe PMC papers**: 7044
- **Why important**: KRT5 links the basal KRT14 branch to the differentiated KRT1, KRT10, and KRT2 branch in the module and has a strong STRING relationship with KRT14. It contributes to the globally corrected intermediate-filament, epidermal-development, keratinocyte-differentiation, and structural-cytoskeleton evidence (7 globally significant GO/KEGG terms, q_global 2.91e-11–1.13e-07; see the table), (11 globally significant GO/KEGG terms, q_global 1.18e-06–0.000789; see the table), (GO:MF structural constituent of cytoskeleton; q_global = 0.00337) (GO:BP tissue development; q_global = 0.0039) (GO:BP cytoskeleton organization; q_global = 0.01), and (GO:BP animal organ development; q_global = 0.0224) (GO:CC supramolecular complex; q_global = 0.0274). HPA supports basal-keratinocyte and epithelial localization across skin, cervix, esophagus, and vagina. Its established basal epidermal function, role in intermediate-filament polymerization and mechanical response, and strong association with epidermolysis bullosa simplex provide both biological and clinical importance.
- **Conclusion**: Established: KRT5 is a basal epithelial scaffold and a bridge between basal and suprabasal keratin states. Hypothesis: it may indicate the epithelial source or structural integrity of the shared module more reliably than an ovary-specific biological process.

#### KRT14

- **Related proteins** (co-abundance neighbors): KRT5 (0.95), KRT2 (0.81); STRING partners: KRT5 (0.999)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 14. This gene encodes a member of the keratin family, the most diverse group of intermediate filaments. This gene product, a type I keratin, is usually found as a heterotetramer with two keratin 5 molecules, a type II keratin. Together they form the cytoskeleton of epithelial cells. Mutations in the genes for these keratins are associated with epidermolysis bullosa simplex. At least one pseudogene has…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 1A, generalized severe (0.823); epidermolysis bullosa simplex 1C, localized (0.818); epidermolysis bullosa simplex 1B, generalized intermediate (0.802); epidermolysis bullosa simplex 1D, generalized, intermediate or severe, autosomal recessive (0.759); Naegeli-Franceschetti-Jadassohn syndrome (0.759)
- **Europe PMC papers**: 6348
- **Why important**: KRT14 forms the strongest reported STRING relationship with KRT5 and occupies the basal branch of the module. It is included in the globally corrected epithelial, epidermal, intermediate-filament, and cornified-envelope annotations (7 globally significant GO/KEGG terms, q_global 2.91e-11–1.13e-07; see the table), (11 globally significant GO/KEGG terms, q_global 1.18e-06–0.000789; see the table), and (10 globally significant GO/KEGG terms, q_global 0.00107–0.0274; see the table). HPA supports basal and suprabasal keratinocyte localization and does not support immune-cell expression. Its established heterotetramerization with KRT5, role in epithelial cytoskeletal organization, and extensive association with epidermolysis bullosa simplex and related disorders make it an important lineage-defining gene.
- **Conclusion**: Established: KRT14 is a basal keratin partner of KRT5 and a well-established epithelial structural and disease gene. Hypothesis: the KRT5–KRT14 branch may represent the basal epithelial contribution that is mixed with the differentiated keratin branch in the tissue-level module.

#### KRT9

- **Related proteins** (co-abundance neighbors): KRT1 (0.88), KRT10 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 9. This gene encodes the type I keratin 9, an intermediate filament chain expressed only in the terminally differentiated epidermis of palms and soles. Mutations in this gene cause epidermolytic palmoplantar keratoderma. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: epidermolytic palmoplantar keratoderma, 1 (0.828); palmoplantar keratoderma, epidermolytic (0.682); Localized epidermolytic hyperkeratosis (0.511); Palmoplantar hyperkeratosis (0.456); Palmoplantar keratoderma (0.438)
- **Europe PMC papers**: 773
- **Why important**: KRT9 is distinctive because it is linked in the co-abundance network to KRT1 and KRT10 but has no reported STRING partner within the module. It nevertheless contributes to the globally corrected keratin-filament, epidermal-development, epithelial-differentiation, and structural annotations (7 globally significant GO/KEGG terms, q_global 2.91e-11–1.13e-07; see the table), (GO:BP skin development; q_global = 1.18e-06) (GO:BP epidermis development; q_global = 1.4e-06) (KEGG Cadherin signaling - Homo sapiens (human); q_global = 2.11e-06), (GO:BP epithelial cell differentiation; q_global = 4.39e-05), (4 globally significant GO/KEGG terms, q_global 0.000161–0.000789; see the table), and (10 globally significant GO/KEGG terms, q_global 0.00107–0.0274; see the table). Its established expression in terminally differentiated palmoplantar epidermis and association with epidermolytic palmoplantar keratoderma make it a biologically informative specialization marker. HPA gives it a more unusual lymphoid-tissue annotation and several cell-type-enhanced annotations, so it may also be sensitive to tissue context or annotation breadth.
- **Conclusion**: Established: KRT9 is a specialized differentiated keratin with a recognized palmoplantar disease connection and compatible module annotations. Hypothesis: KRT9 may mark a specialized epithelial state or context-dependent component of the module rather than serving as a core physical interaction hub.

## Module 4

**Tissue pair**: circulatory_system and ovary  
**Genes (6)**: MCM2, MCM4, MCM5, MCM6, MCM7, RRM1

### Function

This module is a DNA-replication and genome-maintenance module. The primary evidence is exceptionally coherent: the MCM2, MCM4, MCM5, MCM6, and MCM7 genes jointly support the MCM complex (GO:CC MCM complex; q_global = 5.9e-10), the CMG complex (GO:CC CMG complex; q_global = 1.74e-08), replication initiation (GO:BP regulation of DNA-templated DNA replication initiation; q_global = 3.39e-08) (GO:CC DNA replication preinitiation complex; q_global = 3.39e-08) (GO:BP DNA replication initiation; q_global = 1.87e-06), DNA helicase activities (8 globally significant GO/KEGG terms, q_global 7.27e-07–6.4e-06; see the table), and the DNA-replication pathway (GO:BP DNA-templated DNA replication; q_global = 1.4e-06) (KEGG DNA replication - Homo sapiens (human); q_global = 2.27e-06) (GO:BP DNA replication; q_global = 1.22e-05). The full module, including RRM1, also supports DNA repair, DNA-damage response, and nucleotide-dependent processes (9 globally significant GO/KEGG terms, q_global 1.22e-05–0.041; see the table). Thus, the most defensible interpretation is coordinated abundance of the MCM helicase machinery together with deoxyribonucleotide supply for genome duplication and repair. The break-induced replication and homologous-recombination annotations (5 globally significant GO/KEGG terms, q_global 2.72e-09–4.71e-05; see the table) are consistent with replication-fork maintenance and repair-associated DNA synthesis, but do not by themselves establish that the module is specifically activated by DNA breaks.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and the proteins are predominantly nuclear or cytosolic rather than extracellular. It is strongly associated with proliferative precursor cell states. HPA links the genes especially to erythrocyte progenitors and monocyte progenitors, with additional enrichment involving megakaryocyte progenitors, bone marrow, and lymphoid tissue. All module genes are cell-type enhanced, while the blood-cell annotation is low for immune-cell specificity. This pattern is compatible with a shared proliferative progenitor or cell-cycle signal in circulatory-system and ovary samples, rather than a specialized secreted ovarian or vascular program. HPA protein detection in ovary is mixed: MCM2, MCM4, MCM7, and RRM1 are detected, whereas MCM5 and MCM6 are not detected. The lack of detection for some members should not be treated as evidence that the module is absent, because transcript co-abundance and protein detection need not coincide.

**GO/KEGG enrichment**: 59 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC MCM complex | 5.9e-10 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP double-strand break repair via break-induced replication | 2.72e-09 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC CMG complex | 1.74e-08 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication initiation | 3.39e-08 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC DNA replication preinitiation complex | 3.39e-08 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication | 1.47e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF four-way junction helicase activity | 7.27e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF forked DNA-dependent helicase activity | 7.27e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF double-stranded DNA helicase activity | 9.34e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF 3'-5' DNA helicase activity | 9.34e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded 3'-5' DNA helicase activity | 9.34e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP DNA-templated DNA replication | 1.4e-06 | MCM2, MCM4, MCM5, MCM6, MCM7, RRM1 |
| GO:BP DNA replication initiation | 1.87e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| KEGG DNA replication - Homo sapiens (human) | 2.27e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded DNA helicase activity | 2.78e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |

### STRING and hu.MAP

STRING provides strong support for a real, coherent molecular module rather than an arbitrary gene grouping. Every possible pair among the module genes meets the supplied high-confidence interaction threshold, with especially dense connectivity among the MCM proteins and additional links from RRM1 to each MCM component. STRING functional annotations independently recover the MCM complex, MCM domains, CMG complex, DNA unwinding, replication, and break-induced repair (15 supplementary STRING terms; within-query FDR 1.1e-09–4.04e-08). These STRING results are supplementary rather than globally corrected GO or KEGG evidence. hu.MAP independently places MCM2, MCM4, MCM5, MCM6, and MCM7 together in several experimentally supported complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1), including complexes containing the broader replisome components MCM3, CDC45, GINS proteins, TIMELESS, TIPIN, CLSPN, and MCMBP. Additional hu.MAP complexes connect subsets of these MCM proteins to chromatin and DNA-repair-associated assemblies (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_08848.1). RRM1 has no reported hu.MAP complex in this fact sheet, but its STRING connections and its role in deoxyribonucleotide production provide a plausible functional bridge to replication and repair.

**STRING interactions (score >= 0.7)**: 15 of 15 gene pairs: MCM2–MCM4 (0.999); MCM2–MCM5 (0.999); MCM2–MCM6 (0.999); MCM2–MCM7 (0.999); MCM2–RRM1 (0.914); MCM4–MCM5 (0.999); MCM4–MCM6 (0.999); MCM4–MCM7 (0.999); MCM4–RRM1 (0.952); MCM5–MCM6 (0.999); MCM5–MCM7 (0.999); MCM5–RRM1 (0.957); MCM6–MCM7 (0.999); MCM6–RRM1 (0.953); MCM7–RRM1 (0.921)
**STRING functional enrichment (supplementary, within-query FDR)**: Component MCM complex (FDR = 1.1e-09, 5 genes); COMPARTMENTS MCM complex (FDR = 1.19e-09, 5 genes); InterPro MCM domain (FDR = 1.89e-09, 5 genes); InterPro Mini-chromosome maintenance, conserved site (FDR = 1.89e-09, 5 genes); InterPro MCM N-terminal domain (FDR = 1.89e-09, 5 genes); InterPro Mini-chromosome maintenance protein (FDR = 1.89e-09, 5 genes); InterPro MCM OB domain (FDR = 1.89e-09, 5 genes); InterPro MCM, AAA-lid domain (FDR = 1.89e-09, 5 genes); Component CMG complex (FDR = 2.8e-09, 5 genes); COMPARTMENTS CMG complex (FDR = 3.04e-09, 5 genes); RCTM Unwinding of DNA (FDR = 8.06e-09, 5 genes); Keyword DNA replication (FDR = 1.21e-08, 6 genes); Process Double-strand break repair via break-induced replication (FDR = 1.28e-08, 5 genes); Process Regulation of DNA-templated DNA replication initiation (FDR = 2.78e-08, 5 genes); Process DNA unwinding involved in DNA replication (FDR = 4.04e-08, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05529.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/6); huMAP3_14758.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/14); huMAP3_08554.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_11832.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_12180.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/17); huMAP3_06061.1 (MCM4, MCM7, MCM2, MCM6; 4/5); huMAP3_07113.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_11119.1 (MCM4, MCM5, MCM7, MCM6; 4/14); huMAP3_09860.1 (MCM4, MCM2, MCM6; 3/4); huMAP3_00154.1 (MCM4, MCM2, MCM6; 3/5); huMAP3_09466.1 (MCM4, MCM2, MCM6; 3/23); huMAP3_10862.1 (MCM4, MCM2, MCM6; 3/33); huMAP3_14306.1 (MCM4, MCM2, MCM6; 3/55); huMAP3_02602.1 (MCM4, MCM6; 2/2); huMAP3_09238.1 (MCM5, MCM7; 2/11); huMAP3_08848.1 (MCM4, MCM6; 2/15)

### Novelty

This is unlikely to be a newly discovered molecular complex or a novel DNA-replication pathway. The central MCM relationships are already well established by STRING and hu.MAP, and the GO, KEGG, and gene-level descriptions identify canonical functions. The potentially novel result is the reproducible conservation of this coordinated abundance pattern across circulatory_system and ovary. However, the available evidence does not establish that this cross-tissue module has a new tissue-specific mechanism: the HPA pattern instead suggests that shared proliferative precursor-cell composition or cell-cycle state may contribute substantially. Absence of RRM1 from hu.MAP does not establish novelty, because its STRING links and established biochemical role already support association with the MCM-centered module. Overall, the observation is biologically credible and potentially useful as a cross-tissue co-abundance signature, but it should not be described as a newly discovered replication complex without orthogonal experiments.

**Hypothesis.** Hypothesis: the shared module reflects a common proliferative-cell program present in both tissue groups, in which an MCM-centered helicase assembly licenses and supports replication forks while RRM1 supplies deoxyribonucleotides needed for replication and repair. In circulatory-system samples, the signal may be influenced by proliferating hematopoietic progenitors; in ovary, it may reflect proliferating somatic or germline-associated cells. A testable prediction is that module abundance will track markers of cell-cycle progression and proliferative precursor abundance, and that perturbing an MCM component or RRM1 will reduce replication competence and increase replication-stress or DNA-repair signatures. This is a mechanistic interpretation, not a demonstrated tissue-specific causal pathway.

### Important genes

#### MCM6

- **Related proteins** (co-abundance neighbors): MCM7 (0.94), MCM5 (0.91), MCM4 (0.90), RRM1 (0.81); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM7 (0.999), RRM1 (0.953)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 6. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: lactose intolerance (0.246); neurodegenerative disease (0.225); obesity disorder (0.166); nervous system disorder (0.141); systemic lupus erythematosus (0.140)
- **Europe PMC papers**: 3766
- **Why important**: MCM6 is the strongest network-centered member in the supplied subgraph and connects the MCM cluster to RRM1. It occurs across the primary MCM, replication, helicase, repair, and cell-cycle evidence (56 globally significant GO/KEGG terms, q_global 5.9e-10–0.041; see the table), is present in nearly all listed hu.MAP assemblies (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_08848.1), and has an established role as a conserved component of the prereplication and replication-fork machinery. Its extensive literature and disease associations make it a well-supported anchor for interpreting the module.
- **Conclusion**: Established evidence supports MCM6 as a core MCM-complex component and a central integrator of the replication signal. The hypothesis that its network position helps couple the helicase machinery to RRM1-linked nucleotide supply is plausible from the supplied network, but direct functional coupling in these tissues remains unproven.

#### MCM5

- **Related proteins** (co-abundance neighbors): MCM6 (0.91), MCM7 (0.88), MCM2 (0.83), MCM4 (0.81); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM6 (0.999), MCM7 (0.999), RRM1 (0.957)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 5. The protein encoded by this gene is structurally very similar to the CDC46 protein from S. cerevisiae, a protein involved in the initiation of DNA replication. The encoded protein is a member of the MCM family of chromatin-binding proteins and can interact with at least two other members of this family. The encoded protein is upregulated in the transition from the G0 to G1/S phase of the cell cycl…
- **Diseases (Open Targets)**: Meier-Gorlin syndrome (0.563); neurodegenerative disease (0.397); lysosomal storage disease (0.362); kidney transplant (0.198); diabetic ketoacidosis (0.129)
- **Europe PMC papers**: 4143
- **Why important**: MCM5 is a highly connected MCM member with strong links to MCM2, MCM4, MCM6, and MCM7. It is represented throughout the primary replication, repair, helicase, and cell-cycle terms (53 globally significant GO/KEGG terms, q_global 5.9e-10–0.041; see the table), appears in multiple hu.MAP replisome assemblies (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09238.1), and has extensive literature. Its known relationship to the G zero to G one/S transition makes it particularly informative for the possibility that the module reflects proliferative state.
- **Conclusion**: Established evidence identifies MCM5 as a core replication-initiation and helicase-associated component. Its HPA association with bone marrow and proliferative precursor cell types supports a cell-composition or cell-cycle interpretation, but does not demonstrate that MCM5 specifically drives the cross-tissue conservation.

#### MCM7

- **Related proteins** (co-abundance neighbors): MCM6 (0.94), MCM5 (0.88), MCM2 (0.82); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM6 (0.999), RRM1 (0.921)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 is a highly connected member of the MCM subnetwork and participates in the MCM and CMG-related evidence (53 globally significant GO/KEGG terms, q_global 5.9e-10–0.041; see the table). It is present in several hu.MAP assemblies containing broader replisome components (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09238.1), has an extensive literature base, and is detected in ovary by HPA protein profiling. Its disease associations include developmental and replication-relevant disorders, adding biological importance beyond simple network connectivity.
- **Conclusion**: Established evidence supports MCM7 as a core component of replication licensing and fork-associated machinery. Its ovarian protein detection makes it compatible with a genuine ovarian contribution, although the shared module could still primarily reflect proliferating cells rather than an ovary-specific function.

#### MCM4

- **Related proteins** (co-abundance neighbors): MCM6 (0.90), MCM5 (0.81); STRING partners: MCM2 (0.999), MCM5 (0.999), MCM6 (0.999), MCM7 (0.999), RRM1 (0.952)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 4. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication rel…
- **Diseases (Open Targets)**: primary immunodeficiency with natural-killer cell deficiency and adrenal insufficiency (0.714); X-linked adrenal hypoplasia congenita (0.185); lung adenocarcinoma (0.112); microcephaly (0.111); neoplasm (0.102)
- **Europe PMC papers**: 4082
- **Why important**: MCM4 is a core MCM member with direct links to MCM6 and MCM5 in the supplied co-abundance graph and very strong STRING relationships to the other MCM proteins. It contributes to all of the central primary MCM, replication, helicase, repair, and cell-cycle annotations (59 globally significant GO/KEGG terms, q_global 5.9e-10–0.041; see the table), and it appears across many hu.MAP complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_08848.1). Its extensive literature and association with immunodeficiency, adrenal disease, microcephaly, and neoplasm-related annotations indicate broad clinical relevance.
- **Conclusion**: Established evidence supports MCM4 as an essential replication-machinery component and a strong marker of the module's canonical function. Its lower local connectivity than some other MCM members does not weaken the biological interpretation, because it is repeatedly recovered in independent complex and pathway evidence.

#### RRM1

- **Related proteins** (co-abundance neighbors): MCM6 (0.81); STRING partners: MCM2 (0.914), MCM4 (0.952), MCM5 (0.957), MCM6 (0.953), MCM7 (0.921)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribonucleotide reductase catalytic subunit M1. This gene encodes the large and catalytic subunit of ribonucleotide reductase, an enzyme essential for the conversion of ribonucleotides into deoxyribonucleotides. A pool of available deoxyribonucleotides is important for DNA replication during S phase of the cell cycle as well as multiple DNA repair processes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec …
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.618); B-cell chronic lymphocytic leukemia (0.595); exocrine pancreatic carcinoma (0.584); sickle cell disease (0.581); ovarian carcinoma (0.571)
- **Europe PMC papers**: 5033
- **Why important**: RRM1 is the module's distinct biochemical complement to the MCM core. It is the catalytic subunit of ribonucleotide reductase and therefore supplies deoxyribonucleotides required for DNA replication and repair. It connects directly to MCM6 in the co-abundance graph and to every MCM protein in STRING, while contributing to the globally significant DNA-replication, DNA-repair, stress-response, and nucleotide-binding terms (12 globally significant GO/KEGG terms, q_global 1.4e-06–0.041; see the table). Its extensive literature and associations with cancer, leukemia, sickle-cell disease, and ovarian carcinoma make it clinically informative.
- **Conclusion**: Established evidence supports RRM1 as a nucleotide-supply component that complements the MCM helicase machinery. The hypothesis that RRM1 abundance is coordinated with MCM abundance to match nucleotide supply to replication demand is biologically coherent, but the supplied data do not prove direct physical complex formation or causal regulation.
