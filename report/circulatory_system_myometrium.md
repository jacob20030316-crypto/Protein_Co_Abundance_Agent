# Conserved co-abundance modules: circulatory_system and myometrium

## Module 0

**Tissue pair**: circulatory_system and myometrium  
**Genes (17)**: SERPINF2, LRG1, SERPINA3, SERPINC1, APOA4, TGFBI, CP, CFI, C2, AHSG, HPX, ITIH4, KNG1, RAB21, CLEC3B, GC, AZGP1

### Function

The strongest interpretation is a circulating extracellular plasma-protein module involved in protease regulation, coagulation and fibrinolysis, complement control, acute-phase biology, and transport of extracellular ligands. The primary evidence is the globally corrected enrichment for blood microparticles (GO:CC blood microparticle; q_global = 1.56e-05), extracellular vesicles and organelles (6 globally significant GO/KEGG terms, q_global 0.000781–0.00855; see the table), peptidase and endopeptidase inhibitor activities (5 globally significant GO/KEGG terms, q_global 0.0135–0.0325; see the table), and acute-phase response (GO:BP acute-phase response; q_global = 0.0484). The module therefore does not primarily resemble an intracellular myometrial regulatory program. It is more consistent with a coordinated extracellular protease-inhibitor and plasma-protein milieu that can influence vascular, inflammatory, and extracellular-matrix processes. The vesicle annotations should be interpreted cautiously because they are broad cellular-component terms and do not by themselves establish that the proteins are physically assembled in vesicles.

**Cell composition.** The module is overwhelmingly composed of secreted proteins, with HPA identifying nearly all members as secreted to blood and many as liver- or hepatocyte-enriched. The HPA profile is dominated by liver and hepatocyte specificity rather than by myometrial cells or immune cells. Most members are not detected as immune-cell-specific, although C2, TGFBI, and LRG1 show immune or myeloid associations and LRG1 is associated with neutrophils. HPA also reports endometrial secretory-cell enhancement for several genes, which provides a possible local reproductive-tract contribution, but the overall pattern is much more compatible with plasma exposure or blood carryover than with a module produced by myometrial smooth muscle. The lack of myometrium immunohistochemical detection for most members further supports this caution. GC is detected in myometrium and RAB21 is detected there, but these observations do not outweigh the dominant liver-secreted signature.

**GO/KEGG enrichment**: 13 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 1.56e-05 | AHSG, APOA4, CP, GC, HPX, ITIH4, KNG1, SERPINA3, SERPINC1, SERPINF2 |
| GO:CC extracellular exosome | 0.000781 | AHSG, APOA4, AZGP1, C2, CFI, CLEC3B, CP, GC, HPX, ITIH4, KNG1, LRG1, RAB21, SERPINA3, SERPINC1, SERPINF2, TGFBI |
| GO:CC extracellular organelle | 0.000819 | AHSG, APOA4, AZGP1, C2, CFI, CLEC3B, CP, GC, HPX, ITIH4, KNG1, LRG1, RAB21, SERPINA3, SERPINC1, SERPINF2, TGFBI |
| GO:CC extracellular membrane-bounded organelle | 0.000819 | AHSG, APOA4, AZGP1, C2, CFI, CLEC3B, CP, GC, HPX, ITIH4, KNG1, LRG1, RAB21, SERPINA3, SERPINC1, SERPINF2, TGFBI |
| GO:CC extracellular vesicle | 0.000819 | AHSG, APOA4, AZGP1, C2, CFI, CLEC3B, CP, GC, HPX, ITIH4, KNG1, LRG1, RAB21, SERPINA3, SERPINC1, SERPINF2, TGFBI |
| GO:CC extracellular space | 0.00313 | AHSG, APOA4, AZGP1, C2, CFI, CLEC3B, CP, GC, HPX, ITIH4, KNG1, LRG1, RAB21, SERPINA3, SERPINC1, SERPINF2, TGFBI |
| GO:CC extracellular region | 0.00855 | AHSG, APOA4, AZGP1, C2, CFI, CLEC3B, CP, GC, HPX, ITIH4, KNG1, LRG1, RAB21, SERPINA3, SERPINC1, SERPINF2, TGFBI |
| GO:MF endopeptidase inhibitor activity | 0.0135 | AHSG, ITIH4, KNG1, SERPINA3, SERPINC1, SERPINF2 |
| GO:MF peptidase inhibitor activity | 0.0135 | AHSG, ITIH4, KNG1, SERPINA3, SERPINC1, SERPINF2 |
| GO:CC vesicle | 0.0189 | AHSG, APOA4, AZGP1, C2, CFI, CLEC3B, CP, GC, HPX, ITIH4, KNG1, LRG1, RAB21, SERPINA3, SERPINC1, SERPINF2, TGFBI |
| GO:MF endopeptidase regulator activity | 0.0205 | AHSG, ITIH4, KNG1, SERPINA3, SERPINC1, SERPINF2 |
| GO:MF peptidase regulator activity | 0.0325 | AHSG, ITIH4, KNG1, SERPINA3, SERPINC1, SERPINF2 |
| GO:BP acute-phase response | 0.0484 | AHSG, ITIH4, SERPINA3, SERPINF2 |

### STRING and hu.MAP

STRING supports a coherent, already known extracellular interaction neighborhood. AHSG is linked to GC, HPX, KNG1, SERPINA3, SERPINC1, SERPINF2, AZGP1, CP, and ITIH4; SERPINC1 connects the antithrombin and kininogen-related proteins; C2 connects to CFI; and LRG1 connects to SERPINA3. These relationships are concordant with plasma protease regulation, complement regulation, heme handling, and acute-phase biology rather than being isolated co-abundance coincidences. The STRING functional results independently emphasize secreted proteins, plasma and extracellular compartments, blood microparticles, and collagen-containing extracellular matrix (15 supplementary STRING terms; within-query FDR 3.3e-11–5.6e-06), but they remain supplementary rather than globally corrected evidence. hu.MAP provides substantial prior complex-level support: C1–C13 contain overlapping sets of plasma proteins including CP, SERPINA3, KNG1, AHSG, GC, HPX, APOA4, and ITIH4, while C14–C15 connect CFI with SERPINF2 and C17–C18 connect LRG1 or SERPINF2 with other extracellular or immune-related proteins. Thus, the module recapitulates known plasma-protein communities and may represent coordinated abundance of proteins sharing source, transport, or extracellular context. These databases do not establish that all proteins form one physical complex in myometrium.

**STRING interactions (score >= 0.7)**: 22 of 136 gene pairs: AHSG–AZGP1 (0.794); AHSG–CP (0.776); AHSG–GC (0.959); AHSG–HPX (0.879); AHSG–ITIH4 (0.708); AHSG–KNG1 (0.936); AHSG–SERPINA3 (0.848); AHSG–SERPINC1 (0.838); AHSG–SERPINF2 (0.768); AZGP1–GC (0.823); AZGP1–HPX (0.784); C2–CFI (0.864); CP–HPX (0.88); CP–SERPINA3 (0.822); GC–HPX (0.827); GC–SERPINC1 (0.84); HPX–ITIH4 (0.706); HPX–SERPINC1 (0.762); ITIH4–KNG1 (0.723); KNG1–SERPINC1 (0.758); LRG1–SERPINA3 (0.711); SERPINC1–SERPINF2 (0.788)
**STRING functional enrichment (supplementary, within-query FDR)**: PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 3.3e-11, 15 genes); Keyword Secreted (FDR = 1.99e-10, 16 genes); TISSUES Plasma cell (FDR = 4.49e-10, 13 genes); TISSUES Bone marrow (FDR = 5.72e-09, 14 genes); Keyword Signal (FDR = 8.15e-09, 16 genes); PMID (2022) Proteomics in Multiple Sclerosis: The Perspective of the Clinician. (FDR = 3.2e-07, 12 genes); PMID (2018) A proteomic approach of biomarker candidate discovery for alcoholic liver cirrhosis. (FDR = 3.2e-07, 9 genes); COMPARTMENTS Extracellular space (FDR = 6.78e-07, 15 genes); COMPARTMENTS Extracellular region (FDR = 1.39e-06, 16 genes); COMPARTMENTS Blood microparticle (FDR = 1.39e-06, 10 genes); Component Blood microparticle (FDR = 2.71e-06, 10 genes); PMID (2014) The plasma proteomic signature as a strategic tool for early diagnosis of acute coronary syndrome. (FDR = 2.78e-06, 9 genes); Keyword Disulfide bond (FDR = 3.03e-06, 14 genes); PMID (2020) Revelation of Proteomic Indicators for Colorectal Cancer in Initial Stages of Development. (FDR = 3.27e-06, 10 genes); Component Collagen-containing extracellular matrix (FDR = 5.6e-06, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (CP, SERPINC1, SERPINA3, KNG1, AHSG, GC, HPX, APOA4, ITIH4; 9/64); huMAP3_10678.1 (CP, SERPINA3, KNG1, AHSG, GC, HPX, APOA4, ITIH4; 8/71); huMAP3_09531.1 (CP, SERPINA3, KNG1, AHSG, HPX, APOA4, ITIH4; 7/47); huMAP3_10101.1 (CP, SERPINA3, KNG1, AHSG, HPX, APOA4, ITIH4; 7/49); huMAP3_07265.1 (CP, SERPINA3, KNG1, AHSG, HPX, APOA4; 6/20); huMAP3_08395.1 (CP, SERPINA3, KNG1, AHSG, HPX, APOA4; 6/43); huMAP3_07432.1 (CP, SERPINA3, AHSG, HPX, APOA4; 5/18); huMAP3_09434.1 (SERPINA3, AHSG, GC, APOA4, ITIH4; 5/33); huMAP3_08700.1 (CP, AHSG, HPX, APOA4; 4/11); huMAP3_02236.1 (CP, KNG1, HPX; 3/7); huMAP3_02242.1 (SERPINA3, AHSG, APOA4; 3/9); huMAP3_09273.1 (CP, KNG1, HPX; 3/28); huMAP3_00484.1 (AHSG, APOA4; 2/4); huMAP3_14445.1 (CFI, SERPINF2; 2/18); huMAP3_14656.1 (CFI, SERPINF2; 2/21); huMAP3_08224.1 (SERPINA3, GC; 2/21); huMAP3_14295.1 (LRG1, CFI; 2/38); huMAP3_11660.1 (LRG1, SERPINF2; 2/43)

### Novelty

This should not be claimed as a wholly new molecular complex or a newly discovered plasma pathway. Many of the module members and their relationships are already represented in STRING and hu.MAP, and the HPA profile closely resembles a liver-derived secreted-plasma signature. The potentially novel aspect is the observation that this particular co-abundance pattern is conserved across circulatory_system and myometrium, especially the combination of coagulation, complement, acute-phase, heme-handling, and extracellular-matrix-related proteins in the same cross-tissue module. However, the evidence cannot distinguish a true conserved biological program from shared blood content, systemic physiology, or technical/sample-composition effects. Demonstrating novelty would require independent tissue-resolved validation, adjustment for blood contamination and hepatocyte-derived protein abundance, and comparison with published cross-tissue co-abundance modules.

**Hypothesis.** Hypothesis: the shared module reflects a circulating extracellular protease-control system that is delivered to or sampled around myometrial tissue through blood and extracellular vesicle or microparticle compartments. In this model, SERPINC1 and SERPINF2 restrain coagulation and fibrinolysis, KNG1 provides a kininogen and kallikrein substrate or scaffold, C2 and CFI regulate complement activation, HPX limits heme-associated oxidative stress, and LRG1 or TGFBI may connect the plasma environment to vascular or extracellular-matrix remodeling. The observed conservation could therefore indicate exposure of both tissues to a common systemic plasma state rather than local co-transcription of all module genes. This hypothesis predicts that the module will weaken after rigorous removal of blood-derived signal and will correlate with plasma protein abundance, vascular permeability, inflammation, or extracellular-matrix remodeling in independent samples.

### Important genes

#### SERPINA3

- **Related proteins** (co-abundance neighbors): HPX (0.94), SERPINC1 (0.94), KNG1 (0.90), GC (0.87), AHSG (0.85), APOA4 (0.85), AZGP1 (0.84), TGFBI (0.82); STRING partners: AHSG (0.848), CP (0.822), LRG1 (0.711)
- **HPA**: Group enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_07265.1, huMAP3_08395.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_02242.1, huMAP3_08224.1
- **Function (MyGene.info)**: serpin family A member 3. The protein encoded by this gene is a member of the serpin family of proteins, a group of proteins that inhibit serine proteases. This gene is one in a cluster of serpin genes located on the q arm of chromosome 14. Polymorphisms in this protein appear to be tissue specific and influence protease targeting. Variations in this protein's sequence have been implicated in Alzheimer's disease, and defic…
- **Diseases (Open Targets)**: prostate carcinoma (0.359); chronic kidney disease (0.217); peripheral arterial occlusive disease 1 (0.118); central nervous system cancer (0.118); glioma (0.105)
- **Europe PMC papers**: 5458
- **Why important**: SERPINA3 is the most connected and strongest-weighted node in the module and is linked to HPX, SERPINC1, KNG1, GC, AHSG, APOA4, AZGP1, and TGFBI. It occurs in every primary enrichment category, including acute-phase response and protease-regulator terms (13 globally significant GO/KEGG terms, q_global 1.56e-05–0.0484; see the table). Its secreted-to-blood and liver-associated HPA profile, extensive literature, and links to inflammatory and liver disease make it a useful hub for interpreting the module as a systemic extracellular response.
- **Conclusion**: Established evidence supports SERPINA3 as a central secreted serpin and acute-phase-associated component of the module. It is plausible as an integrator of extracellular protease and inflammatory signals, but the data do not establish that SERPINA3 drives the co-abundance pattern or that it acts locally in myometrium.

#### SERPINC1

- **Related proteins** (co-abundance neighbors): SERPINA3 (0.94), KNG1 (0.92), HPX (0.91), SERPINF2 (0.90), AHSG (0.82); STRING partners: AHSG (0.838), GC (0.84), HPX (0.762), KNG1 (0.758), SERPINF2 (0.788)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 is a highly connected module node with strong links to SERPINA3, KNG1, HPX, SERPINF2, and AHSG, and it participates in the major hu.MAP plasma complex C1. Its established function is antithrombin-mediated inhibition of thrombin and other activated coagulation proteases. It is liver- and hepatocyte-enriched, secreted to blood, associated with venous thromboembolic disease, and present in the primary blood-microparticle and protease-inhibitor enrichments (GO:CC blood microparticle; q_global = 1.56e-05), (5 globally significant GO/KEGG terms, q_global 0.0135–0.0325; see the table).
- **Conclusion**: Established evidence identifies SERPINC1 as a strong mechanistic anchor for coagulation and protease control within the module. The module may report systemic hemostatic context around myometrium, but it does not show that SERPINC1 is locally synthesized by myometrial cells.

#### HPX

- **Related proteins** (co-abundance neighbors): SERPINA3 (0.94), SERPINC1 (0.91), KNG1 (0.86), TGFBI (0.84); STRING partners: AHSG (0.879), AZGP1 (0.784), CP (0.88), GC (0.827), ITIH4 (0.706), SERPINC1 (0.762)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_07265.1, huMAP3_08395.1, huMAP3_07432.1, huMAP3_08700.1, huMAP3_02236.1, huMAP3_09273.1
- **Function (MyGene.info)**: hemopexin. This gene encodes a plasma glycoprotein that binds heme with high affinity. The encoded protein is an acute phase protein that transports heme from the plasma to the liver and may be involved in protecting cells from oxidative stress. [provided by RefSeq, Apr 2009].
- **Diseases (Open Targets)**: panniculitis (0.116); neoplasm (0.107); familial idiopathic steroid-resistant nephrotic syndrome (0.101); hepatocellular carcinoma (0.101); focal segmental glomerulosclerosis (0.097)
- **Europe PMC papers**: 6894
- **Why important**: HPX occupies a central position among the module's liver-secreted proteins and connects to SERPINA3, SERPINC1, KNG1, and TGFBI in the co-abundance network. It is a plasma heme-binding protein with an established role in heme transport and protection from oxidative stress, and it appears across the extracellular, microparticle, and protease-related primary terms (8 globally significant GO/KEGG terms, q_global 1.56e-05–0.0135; see the table) and (GO:CC vesicle; q_global = 0.0189). Its extensive literature and liver/hepatocyte HPA profile make it important for expanding the interpretation beyond coagulation alone.
- **Conclusion**: Established evidence supports HPX as a circulating heme-handling and extracellular protective component. Its network position suggests coordination with coagulation and acute-phase proteins, but that coordination is an inference from co-abundance and known interactions rather than proof of a shared local mechanism.

#### C2

- **Related proteins** (co-abundance neighbors): AZGP1 (0.90), CLEC3B (0.84); STRING partners: CFI (0.864)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C2. Component C2 is a serum glycoprotein that functions as part of the classical pathway of the complement system. Activated C1 cleaves C2 into C2a and C2b. The serine proteinase C2a then combines with complement factor 4b to create the C3 or C5 convertase. Deficiency of C2 has been reported to associated with certain autoimmune diseases and SNPs in this gene have been associated with altered suscepti…
- **Diseases (Open Targets)**: Immunodeficiency due to a complement cascade protein anomaly (0.715); immunodeficiency due to a classical component pathway complement deficiency (0.596); systemic lupus erythematosus (0.391); complement deficiency (0.372); type 1 diabetes mellitus (0.320)
- **Europe PMC papers**: 185640
- **Why important**: C2 provides the clearest complement-system entry point in the module. It connects to CFI through STRING and to CLEC3B and AZGP1 in the module network, while hu.MAP contains overlapping plasma and complement-related complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_07432.1) and (hu.MAP huMAP3_02236.1) (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_09273.1). C2 is liver-enriched, secreted to blood, and associated with complement deficiency and autoimmune disease. Its presence broadens the module from protease inhibition and coagulation to innate immune regulation.
- **Conclusion**: Established evidence supports C2 as a circulating classical-complement component and CFI as a complementary regulator in the same module neighborhood. The module suggests coordinated systemic complement and protease biology, but it does not establish complement activation in myometrium.

#### LRG1

- **Related proteins** (co-abundance neighbors): AZGP1 (0.93), ITIH4 (0.86), CP (0.86), CFI (0.85); STRING partners: SERPINA3 (0.711)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14295.1, huMAP3_11660.1
- **Function (MyGene.info)**: leucine rich alpha-2-glycoprotein 1. The leucine-rich repeat (LRR) family of proteins, including LRG1, have been shown to be involved in protein-protein interaction, signal transduction, and cell adhesion and development. LRG1 is expressed during granulocyte differentiation (O'Donnell et al., 2002 [PubMed 12223515]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: colorectal carcinoma (0.113); neoplasm (0.112); nonpapillary renal cell carcinoma (0.101); non-small cell lung carcinoma (0.099); esophageal squamous cell carcinoma (0.096)
- **Europe PMC papers**: 2461
- **Why important**: LRG1 is a network connector between AZGP1, ITIH4, CP, and CFI and is represented in hu.MAP extracellular or immune-related complexes (hu.MAP huMAP3_14295.1) and (hu.MAP huMAP3_11660.1). HPA associates it with liver, hepatocytes, secreted blood proteins, vesicles, endometrial secretory cells, and neutrophils. Its documented functions include regulation of endothelial proliferation, angiogenesis, epithelial-to-mesenchymal transition, wound healing, and TGF-beta receptor signaling, giving it a plausible bridge between a circulating plasma signature and vascular or extracellular-matrix remodeling.
- **Conclusion**: Established evidence supports LRG1 as a secreted, liver-associated protein with vascular, epithelial, and inflammatory relevance. A role in linking the circulating module to myometrial remodeling is a reasonable hypothesis, but it remains unproven and could instead reflect blood or endometrial secretory-cell contribution.

## Module 1

**Tissue pair**: circulatory_system and myometrium  
**Genes (16)**: A2M, APOB, APOD, APOH, C1QB, CFH, C3, C5, SERPIND1, HP, ITIH1, ITIH2, SERPINA4, PLG, PON1, SOD3

### Function

The module is best interpreted as an extracellular plasma-protein program centered on complement regulation, protease control, coagulation and fibrinolysis, glycosaminoglycan binding, and lipid-associated transport. The strongest primary evidence is the globally corrected enrichment for glycosaminoglycan binding (GO:MF glycosaminoglycan binding; q_global = 0.000369), endopeptidase and peptidase inhibitor activities (7 globally significant GO/KEGG terms, q_global 0.000756–0.0439; see the table), complement and coagulation cascades (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.000858), and blood microparticles (GO:CC blood microparticle; q_global = 0.00137). The extracellular region and extracellular-vesicle annotations (5 globally significant GO/KEGG terms, q_global 0.0154–0.0218; see the table) support a circulating extracellular context rather than a canonical intracellular pathway. The Staphylococcus aureus infection term (KEGG Staphylococcus aureus infection - Homo sapiens (human); q_global = 0.00602) is most plausibly a pathway-level reflection of complement and innate-defense components, not evidence that the tissue module specifically represents infection. Overall, the module appears to coordinate extracellular protease inhibition, complement activation and restraint, hemostatic regulation, extracellular-matrix or glycosaminoglycan interactions, and lipoprotein-associated biology.

**Cell composition.** This is overwhelmingly a secreted, plasma-associated module. HPA identifies every module gene as secreted to blood, and the genes are predominantly tissue-enriched or tissue-enhanced in liver and enriched in hepatocytes. HPA also supports extracellular vesicle or blood-microparticle localization for many members. Most genes are not detected in immune cells, while a smaller subset has immune-cell enrichment or enhancement, including C1QB, C3, CFH, APOD, HP and A2M. Protein detection in myometrium is absent for nearly all genes, with SOD3 as the notable detected member. Therefore, the shared circulatory-system and myometrium signal is more consistent with a blood or plasma carryover signal, shared exposure to circulating liver-derived proteins, or a vascular and stromal extracellular environment than with a myometrial cell-intrinsic transcriptional program. The HPA evidence does not support interpreting the module as a broadly expressed housekeeping module.

**GO/KEGG enrichment**: 17 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF glycosaminoglycan binding | 0.000369 | APOB, APOH, CFH, ITIH1, ITIH2, SERPIND1, SOD3 |
| GO:MF endopeptidase inhibitor activity | 0.000756 | A2M, C3, C5, ITIH1, ITIH2, SERPINA4, SERPIND1 |
| GO:MF peptidase inhibitor activity | 0.000756 | A2M, C3, C5, ITIH1, ITIH2, SERPINA4, SERPIND1 |
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 0.000858 | A2M, C1QB, C3, C5, CFH, PLG, SERPIND1 |
| GO:MF endopeptidase regulator activity | 0.00121 | A2M, C3, C5, ITIH1, ITIH2, SERPINA4, SERPIND1 |
| GO:CC blood microparticle | 0.00137 | A2M, C3, CFH, HP, ITIH1, ITIH2, PLG, PON1 |
| GO:MF peptidase regulator activity | 0.00213 | A2M, C3, C5, ITIH1, ITIH2, SERPINA4, SERPIND1 |
| KEGG Staphylococcus aureus infection - Homo sapiens (human) | 0.00602 | C1QB, C3, C5, CFH, PLG |
| GO:MF serine-type endopeptidase inhibitor activity | 0.0142 | A2M, ITIH1, ITIH2, SERPINA4, SERPIND1 |
| GO:MF heparin binding | 0.0142 | APOB, APOH, CFH, SERPIND1, SOD3 |
| GO:CC extracellular region | 0.0154 | A2M, APOB, APOD, APOH, C1QB, C3, C5, CFH, HP, ITIH1, ITIH2, PLG, PON1, SERPINA4, SERPIND1, SOD3 |
| GO:CC extracellular exosome | 0.021 | A2M, APOB, APOD, APOH, C3, C5, CFH, HP, ITIH1, ITIH2, PLG, PON1, SERPINA4, SERPIND1, SOD3 |
| GO:CC extracellular organelle | 0.0218 | A2M, APOB, APOD, APOH, C3, C5, CFH, HP, ITIH1, ITIH2, PLG, PON1, SERPINA4, SERPIND1, SOD3 |
| GO:CC extracellular membrane-bounded organelle | 0.0218 | A2M, APOB, APOD, APOH, C3, C5, CFH, HP, ITIH1, ITIH2, PLG, PON1, SERPINA4, SERPIND1, SOD3 |
| GO:CC extracellular vesicle | 0.0218 | A2M, APOB, APOD, APOH, C3, C5, CFH, HP, ITIH1, ITIH2, PLG, PON1, SERPINA4, SERPIND1, SOD3 |

### STRING and hu.MAP

STRING shows a coherent known interaction neighborhood linking complement components C3, C5 and CFH; protease and coagulation-related proteins including A2M, PLG and SERPIND1; and lipid or plasma proteins including APOB, APOH, APOD, PON1 and HP. The strongest functional STRING summaries are complement and coagulation, protein-lipid complex, positive regulation of opsonization, extracellular space, plasma-cell or bone-marrow-associated protein sets, and blood microparticles (7 supplementary STRING terms; within-query FDR 4.99e-11–9.71e-06). These are supplementary corroboration rather than global enrichment evidence. hu.MAP independently places many of the same genes, especially HP, PLG, A2M, C3, CFH, ITIH1 and ITIH2, in several plasma-protein and complement-related complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_06190.1) (hu.MAP huMAP3_02811.1) (hu.MAP huMAP3_00178.1) (hu.MAP huMAP3_07432.1). The recurrence across complexes indicates that the module overlaps extensively with established extracellular protein assemblies. It also means that the co-abundance structure is biologically plausible but not necessarily evidence for a newly discovered physical complex. Some module genes, such as SERPINA4, SOD3 and APOD, have little or no represented hu.MAP or STRING interaction support, so their co-abundance may reflect shared secretion, compartment, or physiological regulation rather than direct binding.

**STRING interactions (score >= 0.7)**: 28 of 120 gene pairs: A2M–APOH (0.752); A2M–HP (0.997); A2M–PLG (0.779); A2M–SERPIND1 (0.771); APOB–APOD (0.864); APOB–APOH (0.985); APOB–C3 (0.819); APOB–ITIH2 (0.788); APOB–PLG (0.774); APOB–PON1 (0.952); APOD–APOH (0.804); APOD–C1QB (0.795); APOH–HP (0.736); APOH–ITIH2 (0.867); APOH–PLG (0.94); APOH–PON1 (0.87); APOH–SERPIND1 (0.806); C3–C5 (0.974); C3–CFH (0.999); C3–HP (0.862); C3–PLG (0.978); C5–CFH (0.824); C5–PLG (0.725); CFH–HP (0.727); HP–PON1 (0.831); ITIH1–ITIH2 (0.835); ITIH2–SERPIND1 (0.712); PLG–SERPIND1 (0.952)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Complement and coagulation cascades, and Protein-lipid complex (FDR = 4.99e-11, 13 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 4.44e-10, 14 genes); Keyword Glycoprotein (FDR = 1.17e-09, 16 genes); Keyword Signal (FDR = 1.17e-09, 16 genes); Keyword Secreted (FDR = 1.17e-09, 15 genes); NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization (FDR = 1.21e-09, 11 genes); PMID (2022) Circulating Proteins Associated with Response and Resistance to Neoadjuvant Chemotherapy in HER2-Positive Breast Cancer. (FDR = 7.51e-08, 11 genes); COMPARTMENTS Extracellular space (FDR = 9.68e-08, 15 genes); COMPARTMENTS Extracellular region (FDR = 1.08e-07, 16 genes); TISSUES Plasma cell (FDR = 1.63e-07, 11 genes); Keyword Disulfide bond (FDR = 4.87e-07, 14 genes); TISSUES Bone marrow (FDR = 1e-06, 12 genes); PMID (2018) Salivary proteome profiling of oral squamous cell carcinoma in a Hungarian population. (FDR = 5.25e-06, 9 genes); PMID (2013) Targeting human serum fucome by an integrated liquid-phase multicolumn platform operating in cascade to facilitate comparative mass spectrometric analysis of disease-free and breast cancer sera. (FDR = 5.49e-06, 10 genes); COMPARTMENTS Blood microparticle (FDR = 9.71e-06, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (HP, PLG, A2M, C3, APOH, SERPIND1, CFH, ITIH2, ITIH1; 9/64); huMAP3_10678.1 (HP, PLG, A2M, C3, C5, SERPIND1, CFH, ITIH2, ITIH1; 9/71); huMAP3_08395.1 (HP, PLG, A2M, C3, C5, ITIH2, ITIH1; 7/43); huMAP3_09531.1 (HP, PLG, A2M, C3, C5, ITIH2, ITIH1; 7/47); huMAP3_10101.1 (HP, PLG, A2M, C3, C5, ITIH2, ITIH1; 7/49); huMAP3_07541.1 (A2M, C5, ITIH2, ITIH1; 4/19); huMAP3_08224.1 (HP, C3, C5, SERPIND1; 4/21); huMAP3_07701.1 (PLG, A2M, ITIH2, ITIH1; 4/22); huMAP3_09273.1 (PLG, A2M, ITIH2, ITIH1; 4/28); huMAP3_09434.1 (HP, C3, C5, SERPIND1; 4/33); huMAP3_08796.1 (PLG, C5, ITIH1; 3/15); huMAP3_09832.1 (PLG, C5, ITIH1; 3/18); huMAP3_07265.1 (HP, A2M, ITIH2; 3/20); huMAP3_06190.1 (PLG, ITIH1; 2/6); huMAP3_02811.1 (C5, ITIH1; 2/8); huMAP3_00178.1 (C5, ITIH1; 2/9); huMAP3_07432.1 (HP, C3; 2/18)

### Novelty

The module should not be called a new molecular complex or a wholly novel pathway. Its central biology is strongly established by the globally corrected complement, coagulation, protease-inhibitor and extracellular annotations (17 globally significant GO/KEGG terms, q_global 0.000369–0.0439; see the table), by known STRING relationships (10 supplementary STRING terms; within-query FDR 4.99e-11–9.71e-06), and by repeated hu.MAP overlap (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_06190.1) (hu.MAP huMAP3_02811.1) (hu.MAP huMAP3_00178.1) (hu.MAP huMAP3_07432.1). What may be novel is the observation that this particular combination of circulating proteins forms a conserved co-abundance module across circulatory_system and myometrium in the analyzed dataset. However, the HPA profile strongly raises the possibility that the cross-tissue conservation reflects shared blood or extracellular-fluid content rather than a previously unrecognized myometrial mechanism. Demonstrating novelty would require comparison with published co-abundance modules, tissue deconvolution, matched plasma measurements, and tests showing persistence after controlling for vascular or blood contamination. Absence from a particular STRING or hu.MAP representation would not establish novelty.

**Hypothesis.** Hypothesis: the module represents a liver-derived circulating extracellular homeostasis program that is transported through plasma and detected in both tissues. In this model, complement proteins C3, C5 and CFH provide innate-defense activity and its regulation; A2M, ITIH1, ITIH2, SERPINA4 and SERPIND1 constrain extracellular proteases and inflammatory proteolysis; PLG links the program to fibrinolysis and matrix remodeling; APOB, APOH, APOD and PON1 connect it to lipoprotein and oxidative-lipid handling; and SOD3 provides extracellular antioxidant protection. In myometrium, the module could influence vascular, stromal, extracellular-matrix, inflammatory, and hemostatic states without being produced predominantly by myometrial cells. This hypothesis is consistent with the evidence but is not established by co-abundance alone.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): C5 (0.92), PON1 (0.88), SERPIND1 (0.83), ITIH1 (0.82), APOB (0.82), ITIH2 (0.81); STRING partners: APOB (0.819), C5 (0.974), CFH (0.999), HP (0.862), PLG (0.978)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08224.1, huMAP3_09434.1, huMAP3_07432.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a highly connected module member and is linked in STRING to C5, CFH, PLG, HP and APOB. It appears across many primary enrichment terms, including peptidase regulation, complement and coagulation, blood microparticles, extracellular compartments, and innate-defense pathway annotations (14 globally significant GO/KEGG terms, q_global 0.000756–0.0439; see the table). Its HPA profile supports liver and hepatocyte origin, secretion to blood, and enhancement in several tissue-associated cell types, including decidual stromal cells. It has extensive disease and literature support, including complement deficiency, complement-mediated renal disease, hemolytic-uremic syndrome and age-related macular degeneration associations.
- **Conclusion**: Established evidence supports C3 as a central complement and inflammatory effector that anchors the module to circulating innate immunity. Its co-abundance with complement regulators and protease-related proteins is biologically coherent. It is a strong candidate for a module driver or marker, although the data do not prove that C3 expression in myometrium is locally generated.

#### CFH

- **Related proteins** (co-abundance neighbors): A2M (0.88), ITIH1 (0.86), ITIH2 (0.85), C1QB (0.83), APOB (0.82); STRING partners: C3 (0.999), C5 (0.824), HP (0.727)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: complement factor H. This gene is a member of the Regulator of Complement Activation (RCA) gene cluster and encodes a protein with twenty short consensus repeat (SCR) domains. This protein is secreted into the bloodstream and has an essential role in the regulation of complement activation, restricting this innate defense mechanism to microbial infections. Mutations in this gene have been associated with hemolytic-ure…
- **Diseases (Open Targets)**: complement factor H deficiency (0.769); age-related macular degeneration (0.750); atypical hemolytic-uremic syndrome (0.729); age related macular degeneration 4 (0.711); Doyne honeycomb retinal dystrophy (0.688)
- **Europe PMC papers**: 9287
- **Why important**: CFH occupies a highly connected position near C3, C5, A2M, ITIH1, ITIH2 and C1QB. It contributes to globally corrected glycosaminoglycan-binding, complement and coagulation, blood-microparticle, heparin-binding and extracellular annotations (10 globally significant GO/KEGG terms, q_global 0.000369–0.0218; see the table). HPA supports liver-associated and hepatocyte-associated production, secretion to blood, vesicular localization, and enhancement in fibroblast, hepatic-stellate, hepatocyte, Leydig and ovarian-stromal contexts. Its disease associations include complement factor H deficiency, atypical hemolytic-uremic syndrome and age-related macular degeneration.
- **Conclusion**: Established evidence identifies CFH as a major extracellular regulator that can restrain complement activation and help explain the module's balance between innate defense and tissue protection. Its presence supports a regulated complement-homeostasis interpretation rather than simple complement activation alone. A local myometrial regulatory role remains a hypothesis because HPA favors circulating or stromal sources and does not detect myometrial protein.

#### A2M

- **Related proteins** (co-abundance neighbors): CFH (0.88), ITIH1 (0.87), APOB (0.87), APOH (0.86); STRING partners: APOH (0.752), HP (0.997), PLG (0.779), SERPIND1 (0.771)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_07541.1, huMAP3_07701.1, huMAP3_09273.1, huMAP3_07265.1
- **Function (MyGene.info)**: alpha-2-macroglobulin. The protein encoded by this gene is a protease inhibitor and cytokine transporter. It uses a bait-and-trap mechanism to inhibit a broad spectrum of proteases, including trypsin, thrombin and collagenase. It can also inhibit inflammatory cytokines, and it thus disrupts inflammatory cascades. Mutations in this gene are a cause of alpha-2-macroglobulin deficiency. This gene is implicated in Alzheimer…
- **Diseases (Open Targets)**: myopia (0.206); refractive error (0.151); primary angle-closure glaucoma (0.148); Abnormality of refraction (0.144); Aganglionic megacolon (0.118)
- **Europe PMC papers**: 5133
- **Why important**: A2M is a connected extracellular hub linked to CFH, ITIH1, APOB and APOH and represented in numerous primary terms covering protease inhibition, complement and coagulation, blood microparticles, extracellular vesicles and inhibitor activity (13 globally significant GO/KEGG terms, q_global 0.000756–0.0439; see the table). HPA supports secretion to blood and enhancement in hepatocytes, fibroblasts, cardiomyocytes, Hofbauer cells and mast cells. The supplied functional annotation describes broad protease trapping and cytokine transport, while its disease information includes alpha-two-macroglobulin deficiency and Alzheimer disease relevance. It also recurs extensively in hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_07265.1).
- **Conclusion**: Established evidence supports A2M as a broad extracellular protease and inflammatory-cascade buffer that helps connect complement, coagulation and matrix-proteolysis signals. Its network position and complex recurrence make it an important integrator. Whether it actively shapes myometrial physiology or is principally a plasma-derived correlate cannot be resolved from this module.

#### ITIH1

- **Related proteins** (co-abundance neighbors): ITIH2 (0.96), A2M (0.87), CFH (0.86), APOB (0.84), C3 (0.82), PLG (0.82); STRING partners: ITIH2 (0.835)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_07541.1, huMAP3_07701.1, huMAP3_09273.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_06190.1, huMAP3_02811.1, huMAP3_00178.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 1. This gene encodes a member of the inter-alpha-trypsin inhibitor family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the heavy chain of the inter-alpha-trypsin inhibitor complex, which is secreted by hepatocytes into the blood. The heavy chain also interacts with hyaluronan, and…
- **Diseases (Open Targets)**: osteoarthritis, hip (0.305); osteoarthritis (0.188); schizophrenia (0.185); major depressive disorder (0.183); psychiatric disorder (0.171)
- **Europe PMC papers**: 963
- **Why important**: ITIH1 is among the most connected genes in the module and is strongly linked to ITIH2, A2M, CFH, APOB, C3 and PLG. It contributes to nearly all major primary functional themes, including glycosaminoglycan binding, peptidase regulation, complement and coagulation, blood microparticles and extracellular compartments (15 globally significant GO/KEGG terms, q_global 0.000369–0.0439; see the table). HPA identifies liver and hepatocyte enrichment and secretion to blood. The supplied annotation connects ITIH1 to hyaluronan interaction and extracellular-matrix stabilization, with additional relevance to ovulation and fertilization. ITIH1 is represented in many hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_06190.1) (hu.MAP huMAP3_02811.1) (hu.MAP huMAP3_00178.1) and has a substantial literature record.
- **Conclusion**: Established evidence supports ITIH1 as a structural and protease-regulatory bridge between circulating plasma proteins and extracellular matrix or hyaluronan biology. It is particularly informative for interpreting the module as more than a generic plasma signature. A role in myometrial matrix organization is plausible but remains a hypothesis because the available tissue-protein evidence favors secretion from liver or other sources.

#### APOB

- **Related proteins** (co-abundance neighbors): A2M (0.87), APOD (0.85), PON1 (0.85), ITIH1 (0.84), C5 (0.83), CFH (0.82), C3 (0.82); STRING partners: APOD (0.864), APOH (0.985), C3 (0.819), ITIH2 (0.788), PLG (0.774), PON1 (0.952)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Vesicles, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein B. This gene product is the main apolipoprotein of chylomicrons and low density lipoproteins (LDL), and is the ligand for the LDL receptor. It occurs in plasma as two main isoforms, apoB-48 and apoB-100: the former is synthesized exclusively in the gut and the latter in the liver. The intestinal and the hepatic forms of apoB are encoded by a single gene from a single, very long mRNA. The two isoforms…
- **Diseases (Open Targets)**: hypercholesterolemia, autosomal dominant, type B (0.814); Hypercholesterolemia (0.812); familial hypobetalipoproteinemia 1 (0.803); familial hypercholesterolemia (0.780); metabolic disease (0.729)
- **Europe PMC papers**: 28452
- **Why important**: APOB has the strongest network connectivity in the module and links lipid transport biology to A2M, APOD, PON1, ITIH1, C5, CFH and C3. It contributes to the globally corrected glycosaminoglycan-binding, heparin-binding and extracellular annotations (7 globally significant GO/KEGG terms, q_global 0.000369–0.0218; see the table). HPA supports intestine and liver enrichment, enterocyte and hepatocyte association, secretion to blood, and vesicular localization, with no myometrial immunohistochemical detection. Its supplied annotation establishes a central role in chylomicron and LDL biology, and its disease associations include familial and common hypercholesterolemia-related conditions. APOB has extensive literature support and is represented in STRING relationships with several lipid and complement-associated genes.
- **Conclusion**: Established evidence supports APOB as a plasma lipoprotein scaffold that may organize or report the lipid-associated portion of the module. Its network position suggests that lipid transport is integrated with complement, protease and extracellular-vesicle signals. The module does not establish that APOB directly regulates myometrial function; a shared circulating-lipoprotein explanation is more strongly supported.

## Module 2

**Tissue pair**: circulatory_system and myometrium  
**Genes (11)**: ACO1, C1R, C4BPA, C9, CPN2, F12, FBLN1, SERPING1, KATNAL2, KLKB1, TF

### Function

The module is best interpreted as a circulating innate-defense and protease-regulation program centered on complement, coagulation, and kallikrein–kinin biology. The primary evidence is the globally corrected complement and coagulation cascade enrichment (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.00122), together with globally corrected humoral immune response (GO:BP humoral immune response; q_global = 0.0207), classical complement activation (GO:BP complement activation, classical pathway; q_global = 0.0218), and circulating-immunoglobulin-mediated humoral response (GO:BP humoral immune response mediated by circulating immunoglobulin; q_global = 0.0294). C1R and C4BPA support regulation and initiation of classical complement activity, C9 represents the terminal membrane-attack component, and SERPING1 provides an important inhibitory checkpoint. F12 and KLKB1 connect the module to intrinsic coagulation, kallikrein activation, fibrinolysis, and inflammatory mediator generation. The STRING supplementary terms reinforce this interpretation (10 supplementary STRING terms; within-query FDR 3.88e-06–0.0028), while the secreted, glycoprotein, disulfide-bond, and EGF-like-domain annotations (5 supplementary STRING terms; within-query FDR 0.00039–0.0022) are consistent with a plasma protein system. FBLN1 adds an extracellular-matrix and platelet-adhesion dimension, whereas TF contributes iron transport and antibacterial humoral activity. ACO1 and KATNAL2 are not supported by the primary enrichment terms and may represent tissue-contextual or co-abundance-linked components rather than core pathway constituents.

**Cell composition.** The module is strongly dominated by secreted or plasma-associated proteins: HPA identifies eight secreted genes, with frequent liver and hepatocyte enrichment. CPN2, C9, F12, SERPING1, KLKB1, C4BPA, and TF are especially consistent with a liver-produced circulating protein signature. This makes blood or plasma contribution, vascular exposure, or shared extracellular fluid a serious alternative explanation for the conserved signal in circulatory_system and myometrium, rather than implying that all genes are produced by myometrial cells. Most genes are not immune-cell-specific in HPA, although F12 and C4BPA show neutrophil or eosinophil-associated enhancement and SERPING1 shows neutrophil and plasmacytoid dendritic-cell enhancement. FBLN1 is the clearest local myometrial or stromal component because it is extracellular-matrix secreted and detected in myometrium, with enrichment in decidual and endometrial stromal cells. KATNAL2 is also detected in myometrium but has a cytoplasmic microtubule-related annotation rather than a complement annotation. The overall composition therefore favors a liver-derived plasma module sampled across tissues, with possible stromal or extracellular-matrix contribution in myometrium.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 0.00122 | C1R, C4BPA, C9, F12, KLKB1, SERPING1 |
| GO:BP humoral immune response | 0.0207 | C1R, C4BPA, C9, SERPING1, TF |
| GO:BP complement activation, classical pathway | 0.0218 | C1R, C4BPA, C9, SERPING1 |
| GO:BP humoral immune response mediated by circulating immunoglobulin | 0.0294 | C1R, C4BPA, C9, SERPING1 |

### STRING and hu.MAP

STRING provides high-confidence known relationships among C1R–SERPING1, F12–KLKB1, F12–SERPING1, and KLKB1–SERPING1. These interactions support a biologically coherent complement, contact-system, and inhibitory-protease core, but they are prior database relationships rather than independent proof that the co-abundance module is a physical complex. CPN2, C9, C4BPA, FBLN1, KATNAL2, ACO1, and TF have no listed STRING partners within this module, so their co-abundance links should not be treated as established molecular interactions. hu.MAP repeatedly places TF, C4BPA, and SERPING1 in broad plasma-protein complexes (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1), while C4BPA and SERPING1 also co-occur in another listed complex (hu.MAP huMAP3_09273.1) and TF and C4BPA in another (hu.MAP huMAP3_08395.1). These complexes contain many circulating complement, coagulation, apolipoprotein, and acute-phase proteins, indicating known membership in broad extracellular protein assemblies rather than a module-specific complex. Overall, STRING and hu.MAP validate the plasma-protein and complement-related core, but they do not establish the entire co-abundance module as one physical complex.

**STRING interactions (score >= 0.7)**: 4 of 55 gene pairs: C1R–SERPING1 (0.999); F12–KLKB1 (0.972); F12–SERPING1 (0.987); KLKB1–SERPING1 (0.996)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization (FDR = 3.88e-06, 8 genes); NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization (FDR = 1.64e-05, 7 genes); KEGG Complement and coagulation cascades (FDR = 0.0002, 6 genes); Keyword Secreted (FDR = 0.00039, 9 genes); Keyword Complement pathway (FDR = 0.0019, 4 genes); Keyword Glycoprotein (FDR = 0.0019, 9 genes); Keyword Signal (FDR = 0.0019, 9 genes); Keyword Disulfide bond (FDR = 0.0019, 9 genes); Keyword EGF-like domain (FDR = 0.0022, 4 genes); WikiPathways Complement and coagulation cascades (FDR = 0.0022, 5 genes); RCTM Regulation of Complement cascade (FDR = 0.0023, 5 genes); WikiPathways Complement system (FDR = 0.0023, 5 genes); WikiPathways Kinin-Kallikrein pathway (FDR = 0.0023, 3 genes); Keyword Fibrinolysis (FDR = 0.0024, 3 genes); NetworkNeighborAL Complement cascade (FDR = 0.0028, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09531.1 (TF, C4BPA, SERPING1; 3/47); huMAP3_10101.1 (TF, C4BPA, SERPING1; 3/49); huMAP3_15040.1 (TF, C4BPA, SERPING1; 3/64); huMAP3_10678.1 (TF, C4BPA, SERPING1; 3/71); huMAP3_09273.1 (C4BPA, SERPING1; 2/28); huMAP3_08395.1 (TF, C4BPA; 2/43)

### Novelty

This is unlikely to be a new discovery of complement or coagulation biology: the principal genes, pathways, disease associations, and several protein relationships are already well established in STRING, hu.MAP, and the supplied literature annotations. The potentially novel result is the conserved co-abundance pattern across circulatory_system and myometrium, particularly the combination of a liver-derived plasma signature with FBLN1 and the less-characterized co-abundance-linked genes KATNAL2 and ACO1. However, absence of STRING or hu.MAP relationships for those genes does not establish novelty; it may reflect tissue context, indirect regulation, shared sample composition, or incomplete database coverage. The most defensible conclusion is that the module-level observation may be contextually novel, while its core biological function is established and its apparent cross-tissue conservation may largely reflect circulating protein carryover or shared vascular exposure.

**Hypothesis.** Hypothesis: a liver-derived circulating protein program is co-abundant across the circulatory system and myometrium, carrying a coordinated complement and contact-system defense signal into both tissue datasets. Within this program, SERPING1 may buffer C1R-, F12-, and KLKB1-linked protease activity, C4BPA may restrain classical complement activation, and C9 may report terminal complement capacity. FBLN1 may connect the circulating signal to myometrial extracellular matrix and platelet-adhesion biology. The apparent association of KATNAL2 and ACO1 may reflect local tissue state, cellular composition, or indirect metabolic and cytoskeletal coupling rather than direct participation in complement. This hypothesis should be tested by separating plasma abundance from tissue-transcribed expression, examining cell-type-resolved RNA and protein localization, and validating the module in myometrial samples with controlled blood-content measurements.

### Important genes

#### SERPING1

- **Related proteins** (co-abundance neighbors): C9 (0.91), F12 (0.86), TF (0.85); STRING partners: C1R (0.999), F12 (0.987), KLKB1 (0.996)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_09273.1
- **Function (MyGene.info)**: serpin family G member 1. This gene encodes a highly glycosylated plasma protein involved in the regulation of the complement cascade. Its encoded protein, C1 inhibitor, inhibits activated C1r and C1s of the first complement component and thus regulates complement activation. It is synthesized in the liver, and its deficiency is associated with hereditary angioneurotic oedema (HANE). Alternative splicing results in multipl…
- **Diseases (Open Targets)**: hereditary angioedema with C1Inh deficiency (0.828); hereditary angioedema type 1 (0.750); hereditary angioedema (0.728); angioedema (0.616); hereditary angioedema type 2 (0.614)
- **Europe PMC papers**: 4203
- **Why important**: SERPING1 is a central network connector, linking C9, F12, and KLKB1, and it has a direct STRING relationship with C1R. It appears in every primary globally corrected enrichment term (4 globally significant GO/KEGG terms, q_global 0.00122–0.0294; see the table), in many supplementary STRING terms, and in all listed hu.MAP complexes. Its established function as a circulating inhibitor of activated C1R and C1S makes it a mechanistic control point between complement activation, contact-system proteases, and inflammatory signaling. Its HPA liver, hepatocyte, blood-secreted, and immune-cell-enhanced profile also makes it important for interpreting the module as a plasma-derived signal. The hereditary angioedema associations and substantial literature support indicate strong disease and research relevance.
- **Conclusion**: Established evidence supports SERPING1 as a central circulating regulator of complement and contact-system activity and as a major interpretive anchor for this module. Hypothesis: variation in its abundance could tune the balance between protective inhibition and excessive complement or kallikrein-mediated inflammation in the shared tissue context.

#### F12

- **Related proteins** (co-abundance neighbors): CPN2 (0.90), KATNAL2 (0.87), SERPING1 (0.86); STRING partners: KLKB1 (0.972), SERPING1 (0.987)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coagulation factor XII. This gene encodes coagulation factor XII which circulates in blood as a zymogen. This single chain zymogen is converted to a two-chain serine protease with an heavy chain (alpha-factor XIIa) and a light chain. The heavy chain contains two fibronectin-type domains, two epidermal growth factor (EGF)-like domains, a kringle domain and a proline-rich domain, whereas the light chain contains only a cat…
- **Diseases (Open Targets)**: congenital factor XII deficiency (0.815); hereditary angioedema type 3 (0.777); hereditary angioedema (0.677); peptic ulcer disease (0.450); angioedema (0.407)
- **Europe PMC papers**: 100014
- **Why important**: F12 is a highly connected module gene and has strong STRING relationships with KLKB1 and SERPING1. It is present in the primary complement and coagulation enrichment (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.00122) and in extensive supplementary annotations involving coagulation, kallikrein–kinin signaling, fibrinolysis, and proteolysis (13 supplementary STRING terms; within-query FDR 3.88e-06–0.0024). Its established role as a circulating zymogen that activates the intrinsic coagulation and kallikrein systems provides a direct mechanistic bridge between vascular hemostasis and inflammation. It is liver-enriched and secreted to blood, with an immune-cell enhancement signal in eosinophils, and has strong links to factor deficiency and hereditary angioedema.
- **Conclusion**: Established evidence supports F12 as a core contact-system and coagulation component whose co-abundance with SERPING1 and KLKB1 is biologically plausible. Hypothesis: F12 may be a principal driver of the module’s coordinated variation, although the data do not demonstrate enzymatic activation or causality in myometrium.

#### C9

- **Related proteins** (co-abundance neighbors): FBLN1 (0.91), SERPING1 (0.91), ACO1 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C9. This gene encodes the final component of the complement system. It participates in the formation of the Membrane Attack Complex (MAC). The MAC assembles on bacterial membranes to form a pore, permitting disruption of bacterial membrane organization. Mutations in this gene cause component C9 deficiency. [provided by RefSeq, Feb 2009].
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.747); age-related macular degeneration (0.584); complement component 9 deficiency (0.548); macular degeneration (0.541); complement deficiency (0.463)
- **Europe PMC papers**: 28081
- **Why important**: C9 has substantial network connectivity through FBLN1, SERPING1, and ACO1 and is present in all primary enrichment terms (4 globally significant GO/KEGG terms, q_global 0.00122–0.0294; see the table). It is the terminal complement component that participates in membrane-attack-complex formation, giving it a clear functional endpoint in the module’s complement interpretation. Its liver and hepatocyte enrichment and secretion to blood strongly support a circulating source. Complement C9 deficiency and immunodeficiency associations, together with extensive literature coverage, make it one of the best-established and most biologically informative genes in the module.
- **Conclusion**: Established evidence supports C9 as the terminal effector marker of the module’s complement arm and as evidence that the module is not merely a generic extracellular-protein cluster. Hypothesis: C9 abundance may reflect complement effector capacity in the sampled fluid or tissue environment, but it cannot by itself establish active membrane attack.

#### C4BPA

- **Related proteins** (co-abundance neighbors): CPN2 (0.94); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_09273.1, huMAP3_08395.1
- **Function (MyGene.info)**: complement component 4 binding protein alpha. This gene encodes a member of a superfamily of proteins composed predominantly of tandemly arrayed short consensus repeats of approximately 60 amino acids. Along with a single, unique beta-chain, seven identical alpha-chains encoded by this gene assemble into the predominant isoform of C4b-binding protein, a multimeric protein that controls activation of the complement cascade through the classica…
- **Diseases (Open Targets)**: venous thromboembolism (0.445); dengue disease (0.370); Thromboembolism (0.332); Alzheimer disease (0.246); Parkinson disease (0.243)
- **Europe PMC papers**: 1611
- **Why important**: C4BPA is present in every primary enrichment term (4 globally significant GO/KEGG terms, q_global 0.00122–0.0294; see the table) and participates in the listed STRING supplementary complement terms. It is a component of C4b-binding protein and negatively regulates classical complement activation. HPA supports a liver, hepatocyte, neutrophil-associated, and blood-secreted profile. C4BPA also repeatedly appears with TF and SERPING1 in hu.MAP complexes (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08395.1), making it a useful bridge between the primary complement signal and broad circulating protein assemblies. Its disease associations include thromboembolic and complement-related conditions.
- **Conclusion**: Established evidence supports C4BPA as a complement-regulatory component and as a marker of broad plasma-protein complex context. Hypothesis: coordinated C4BPA and SERPING1 abundance may represent compensatory control of complement and contact-system activation rather than simple activation alone.

#### C1R

- **Related proteins** (co-abundance neighbors): KLKB1 (0.97), CPN2 (0.89); STRING partners: SERPING1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C1r. This gene encodes a member of the peptidase S1 protein family. The encoded protein is a proteolytic subunit in the complement system C1 complex. The complement system acts as a mediator in the innate immune response by ultimately triggering phagocytosis, inflammation, and rupturing the bacterial cell wall. Mutations in this gene are associated with Ehlers-Danlos Syndrome. [provided by RefSeq, Dec …
- **Diseases (Open Targets)**: Ehlers-Danlos syndrome, periodontitis type (0.715); immunodeficiency due to a classical component pathway complement deficiency (0.555); coronary artery disorder (0.486); systemic lupus erythematosus (0.467); complement deficiency (0.463)
- **Europe PMC papers**: 5739
- **Why important**: C1R is present in every primary enrichment term (4 globally significant GO/KEGG terms, q_global 0.00122–0.0294; see the table), has a high-confidence STRING relationship with SERPING1, and is linked in the module graph to KLKB1 and CPN2. Its established function as a proteolytic subunit of the C1 complex places it at the initiation side of classical complement activation, complementing the terminal role of C9 and the inhibitory roles of C4BPA and SERPING1. HPA supports liver and stromal-cell enrichment, including decidual and endometrial stromal cells, while its disease associations include complement deficiency and Ehlers–Danlos syndrome.
- **Conclusion**: Established evidence supports C1R as an initiating classical-complement component and a key link between the module’s plasma and stromal interpretations. Hypothesis: C1R may help couple circulating complement regulation to local extracellular-matrix or stromal conditions in myometrium, but the co-abundance data do not establish local C1R production.

#### FBLN1

- **Related proteins** (co-abundance neighbors): C9 (0.91); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibulin 1. Fibulin 1 is a secreted glycoprotein that becomes incorporated into a fibrillar extracellular matrix. Calcium-binding is apparently required to mediate its binding to laminin and nidogen. It mediates platelet adhesion via binding fibrinogen. Four splice variants which differ in the 3' end have been identified. Each variant encodes a different isoform, but no functional distinctions have been ident…
- **Diseases (Open Targets)**: synpolydactyly type 2 (0.447); FBLN1-related developmental delay-central nervous system anomaly-syndactyly syndrome (0.377); synpolydactyly (0.371); adolescent idiopathic scoliosis (0.306); alcohol drinking (0.219)
- **Europe PMC papers**: 2655
- **Why important**: FBLN1 is connected to C9 in the module and is the clearest gene tying the circulating complement signature to tissue structure. HPA identifies it as secreted to extracellular matrix, detected in myometrium, and enriched in decidual, endometrial stromal, and choroid-plexus epithelial cell contexts. Its established function includes incorporation into fibrillar extracellular matrix, integrin-related signaling, regulation of cell adhesion, and platelet adhesion through fibrinogen binding. It has no listed STRING partner in this module and does not occur in the primary GO or KEGG terms, which makes it important precisely as a possible contextual rather than core pathway component.
- **Conclusion**: Established evidence supports FBLN1 as an extracellular-matrix and adhesion protein that can connect tissue structure with circulating protein biology. Hypothesis: FBLN1 may explain why a predominantly plasma-derived module is conserved in myometrium, either through local stromal production or through matrix-associated retention of circulating factors.

## Module 3

**Tissue pair**: circulatory_system and myometrium  
**Genes (6)**: AFM, C1S, F13A1, GSN, F2, VPS35

### Function

The module is best interpreted as a circulating extracellular hemostasis and blood-microparticle program. The primary evidence is (GO:CC blood microparticle; q_global = 0.00551), in which AFM, C1S, F13A1, F2, and GSN are jointly associated with blood microparticles. This interpretation is biologically coherent with the established functions of F2 in thrombin generation and fibrin formation, F13A1 in fibrin cross-linking, C1S in classical complement activation and proteolysis, and GSN in actin-filament remodeling. The STRING results provide supplementary support through blood-microparticle, extracellular-space, and bleeding-related annotations (5 supplementary STRING terms; within-query FDR 0.002–0.0358). VPS35 is not part of the primary enriched gene overlap and may represent a trafficking-related connection rather than a core hemostasis component. No additional GO or KEGG term passed global correction beyond (GO:CC blood microparticle; q_global = 0.00551).

**Cell composition.** The module is strongly dominated by secreted blood proteins rather than by a myometrium-specific intracellular program. AFM, C1S, F2, F13A1, and GSN are secreted to blood according to HPA, and liver or hepatocyte enrichment is especially prominent for AFM, C1S, and F2. F13A1 has associations with megakaryocytes, platelets, macrophages, and monocyte or myeloid dendritic-cell contexts, while GSN has immune-cell and vascular or stromal associations. Most module proteins were not detected in immune cells, so this is not simply a canonical leukocyte-expression module. The lack of HPA protein detection in myometrium for most genes, together with detection of GSN in myometrium, favors a circulating-protein or blood-microparticle contribution to the shared signal rather than coordinated local production by smooth muscle. The shared module may therefore reflect blood exposure, vascular or stromal material, or common extracellular protein handling in the two tissue groups.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 0.00551 | AFM, C1S, F13A1, F2, GSN |

### STRING and hu.MAP

STRING identifies a high-confidence relationship between F13A1 and F2, consistent with their participation in coagulation biology (5 supplementary STRING terms; within-query FDR 0.002–0.0358). The remaining module edges are not represented as high-confidence STRING gene-pair interactions in the supplied result, so the co-abundance edges should not be treated as established physical interactions. There are no hu.MAP complexes containing multiple module members. Thus, the network is better viewed as a coordinated abundance pattern centered on related extracellular and blood-associated proteins, with limited direct evidence for a single multiprotein complex. The link involving VPS35 and C1S is especially tentative as a module-level mechanistic connection because VPS35 is an endosomal retromer component and has no primary GO or KEGG enrichment assignment here.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: F13A1–F2 (0.954)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Blood microparticle (FDR = 0.002, 5 genes); COMPARTMENTS Blood microparticle (FDR = 0.0021, 5 genes); HPO Bruising susceptibility (FDR = 0.0083, 4 genes); COMPARTMENTS Extracellular space (FDR = 0.0145, 6 genes); HPO Gingival bleeding (FDR = 0.0358, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The underlying biology is not a wholly new functional association: coagulation, complement, extracellular proteins, blood microparticles, and actin regulation are established topics for these genes, and the F13A1–F2 relationship is already represented in STRING. The potentially new observation is the coordinated co-abundance of this particular gene set in a conserved module shared by circulatory_system and myometrium, especially the inclusion of AFM, C1S, F13A1, F2, GSN, and VPS35 in one tissue-pair network. However, the supplied evidence does not establish that this tissue-pair module is novel in the literature. Lack of a hu.MAP complex or lack of additional STRING links does not by itself demonstrate novelty. The most defensible conclusion is that the module may be a new tissue-comparative network observation built from largely known biological components.

**Hypothesis.** Hypothesis: the conserved module reflects a blood-borne extracellular compartment that couples coagulation and complement activity with microparticle-associated cytoskeletal material. In this model, hepatocyte-derived AFM, F2, and C1S enter the circulation, while F13A1 from plasma, platelets, or myeloid-associated sources contributes to fibrin stabilization and GSN contributes actin-associated microparticle or extracellular remodeling. Co-abundance in circulatory_system and myometrium could arise from shared exposure to vascular contents or extracellular vesicle and microparticle material, with VPS35 marking a possible endosomal trafficking influence on C1S-related protein handling. This is a hypothesis rather than a demonstrated physical pathway; the strongest established molecular link in the supplied network is F13A1–F2.

### Important genes

#### F2

- **Related proteins** (co-abundance neighbors): C1S (0.97), AFM (0.90); STRING partners: F13A1 (0.954)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coagulation factor II, thrombin. This gene encodes the prothrombin protein (also known as coagulation factor II). This protein is proteolytically cleaved in multiple steps to form the activated serine protease thrombin. The activated thrombin enzyme plays an important role in thrombosis and hemostasis by converting fibrinogen to fibrin during blood clot formation, by stimulating platelet aggregation, and by activating additional …
- **Diseases (Open Targets)**: congenital prothrombin deficiency (0.827); thrombophilia due to thrombin defect (0.738); venous thromboembolism (0.727); deep vein thrombosis (0.690); blood coagulation disease (0.670)
- **Europe PMC papers**: 109299
- **Why important**: F2 is a central hemostasis marker in the module, connects to C1S and F13A1 in the co-abundance graph, and is the best-supported direct STRING partner of F13A1. Its established product is thrombin, which converts fibrinogen to fibrin, activates coagulation factors, stimulates platelet aggregation, and participates in wound responses. It has extensive literature support and strong disease associations involving prothrombin deficiency, thrombophilia, and venous thromboembolism. It is also a liver- and hepatocyte-enriched secreted blood protein and contributes to (GO:CC blood microparticle; q_global = 0.00551) and (5 supplementary STRING terms; within-query FDR 0.002–0.0358).
- **Conclusion**: Established conclusion: F2 is a core circulating coagulation component and a strong anchor for the module's hemostasis interpretation. Hypothesis: its co-abundance with the other genes may indicate coordinated blood-microparticle or vascular exposure in myometrium rather than local myometrial synthesis.

#### F13A1

- **Related proteins** (co-abundance neighbors): GSN (0.87), AFM (0.85); STRING partners: F2 (0.954)
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coagulation factor XIII A chain. This gene encodes the coagulation factor XIII A subunit. Coagulation factor XIII is the last zymogen to become activated in the blood coagulation cascade. Plasma factor XIII is a heterotetramer composed of 2 A subunits and 2 B subunits. The A subunits have catalytic function, and the B subunits do not have enzymatic activity and may serve as plasma carrier molecules. Platelet factor XIII is compri…
- **Diseases (Open Targets)**: Factor XIII subunit A deficiency (0.808); factor XIII, A subunit, deficiency of (0.740); congenital factor XIII deficiency (0.527); thrombophilia due to thrombin defect (0.485); hemorrhage (0.463)
- **Europe PMC papers**: 2585
- **Why important**: F13A1 occupies a connecting position between GSN and AFM and has the strongest supplied STRING relationship to F2. It encodes the catalytically active A subunit of factor XIII, which stabilizes fibrin through peptide cross-linking. Its HPA profile links it to adipose tissue, placenta, macrophages, Hofbauer cells, megakaryocytes, platelets, and immune-cell contexts. It contributes to the globally significant blood-microparticle term (GO:CC blood microparticle; q_global = 0.00551) and all of the relevant supplementary STRING terms (5 supplementary STRING terms; within-query FDR 0.002–0.0358), with established disease associations involving factor XIII deficiency and hemorrhage.
- **Conclusion**: Established conclusion: F13A1 is a biologically important bridge between coagulation, platelet or myeloid-associated sources, and fibrin stabilization. Hypothesis: it may help define the blood-derived microparticle component shared by the two tissues.

#### C1S

- **Related proteins** (co-abundance neighbors): F2 (0.97), AFM (0.88), VPS35 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C1s. This gene encodes a serine protease, which is a major constituent of the human complement subcomponent C1. C1s associates with two other complement components C1r and C1q in order to yield the first component of the serum complement system. Defects in this gene are the cause of selective C1s deficiency. [provided by RefSeq, Mar 2009].
- **Diseases (Open Targets)**: Ehlers-Danlos syndrome, periodontal type 2 (0.683); complement component C1s deficiency (0.669); Ehlers-Danlos syndrome, periodontitis type (0.560); hereditary angioedema (0.542); coronary artery disorder (0.508)
- **Europe PMC papers**: 6512
- **Why important**: C1S has a highly connected position in the module, linking F2, AFM, and VPS35. It is a secreted liver-enriched serine protease and a major component of the classical complement system, with established roles in proteolysis, complement activation, zymogen activation, and protein maturation. It contributes to (GO:CC blood microparticle; q_global = 0.00551) and to the supplementary blood-microparticle, extracellular-space, and bleeding-related terms (5 supplementary STRING terms; within-query FDR 0.002–0.0358). Its disease associations include C1S deficiency, periodontal connective-tissue disease, hereditary angioedema, and coronary artery disorder, and it has substantial literature support.
- **Conclusion**: Established conclusion: C1S supports an extracellular proteolytic and complement-related interpretation alongside coagulation. Hypothesis: its connection to VPS35 could reflect shared extracellular or endosomal protein handling, but the supplied data do not establish a direct C1S–VPS35 mechanism.

#### GSN

- **Related proteins** (co-abundance neighbors): F13A1 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gelsolin. The protein encoded by this gene binds to the 'plus' ends of actin monomers and filaments to prevent monomer exchange. The encoded calcium-regulated protein functions in both assembly and disassembly of actin filaments. Defects in this gene are a cause of familial amyloidosis Finnish type (FAF). Multiple transcript variants encoding several different isoforms have been found for this gene. [provid…
- **Diseases (Open Targets)**: Finnish type amyloidosis (0.805); AL amyloidosis (0.463); neuropathy (0.418); cardiomyopathy (0.418); cutis laxa (0.417)
- **Europe PMC papers**: 5062
- **Why important**: GSN links to F13A1 and is the only module member reported as detected by HPA immunohistochemistry in myometrium. It is a calcium-regulated actin-binding protein involved in actin filament assembly and disassembly, phagocytic engulfment, and cytoskeletal remodeling. It is secreted to blood, has vascular endothelial, fibroblast, goblet-cell, and eosinophil-associated expression contexts, and contributes to (GO:CC blood microparticle; q_global = 0.00551) and (4 supplementary STRING terms; within-query FDR 0.002–0.0145). Its disease associations include Finnish-type amyloidosis, amyloidosis, neuropathy, cardiomyopathy, and cutis laxa.
- **Conclusion**: Established conclusion: GSN provides a plausible cytoskeletal and microparticle-associated component and is the strongest HPA-supported connection to myometrial tissue presence. Hypothesis: it may represent actin-rich extracellular or microparticle material accompanying coagulation proteins, rather than a local contractile-cell program.

#### AFM

- **Related proteins** (co-abundance neighbors): F2 (0.90), C1S (0.88), F13A1 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: afamin. This gene is a member of the albumin gene family, which is comprised of four genes that localize to chromosome 4 in a tandem arrangement. These four genes encode structurally-related serum transport proteins that are known to be evolutionarily related. The protein encoded by this gene is regulated developmentally, expressed in the liver and secreted into the bloodstream. [provided by RefSeq, Jul 2…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.249); prostate carcinoma (0.204); adrenal gland disorder (0.103); non-alcoholic fatty liver (0.091); metabolic syndrome (0.082)
- **Europe PMC papers**: 24965
- **Why important**: AFM has a highly connected position, linking F2, C1S, and F13A1. It is a liver- and hepatocyte-enriched member of the albumin-related serum transport-protein family, is secreted into blood, and has annotated roles in nutrient response, protein stabilization, vitamin transport, and extracellular protein transport. It contributes to (GO:CC blood microparticle; q_global = 0.00551), (STRING Component Blood microparticle; within-query FDR = 0.002), (STRING COMPARTMENTS Blood microparticle; within-query FDR = 0.0021), and (STRING COMPARTMENTS Extracellular space; within-query FDR = 0.0145). Its disease associations include skeletal abnormality, prostate carcinoma, adrenal-gland disorder, non-alcoholic fatty liver disease, and metabolic syndrome, with substantial literature support.
- **Conclusion**: Established conclusion: AFM is strong evidence that the module includes liver-derived circulating transport proteins rather than only locally produced coagulation factors. Hypothesis: AFM may help organize or stabilize the circulating extracellular protein context in which the hemostatic and microparticle-associated signals co-vary.

## Module 4

**Tissue pair**: circulatory_system and myometrium  
**Genes (5)**: DCD, KRT10, KRT9, KRT2, KRT1

### Function

The module is best interpreted as a keratinized epithelial intermediate-filament program. The primary evidence is highly coherent: the globally corrected terms identify keratin filaments and intermediate-filament organization (6 globally significant GO/KEGG terms, q_global 7.23e-06–0.000706; see the table), epidermal structural function and cornified-envelope formation (4 globally significant GO/KEGG terms, q_global 0.000463–0.0051; see the table), and epidermal and keratinocyte differentiation (6 globally significant GO/KEGG terms, q_global 0.00303–0.0498; see the table). Cadherin signaling (KEGG Cadherin signaling - Homo sapiens (human); q_global = 0.00655) is compatible with epithelial cell adhesion, but the dominant interpretation is structural keratinization rather than a broad signaling pathway. KRT1, KRT10, KRT2, and KRT9 account for the GO/KEGG signal; DCD has no globally corrected GO/KEGG annotation in this module. The supplementary STRING results independently reinforce keratin filament, intermediate-filament, cornified-envelope, and keratinization interpretations (9 supplementary STRING terms; within-query FDR 2.66e-06–0.00025).

**Cell composition.** This is not a plasma-protein or conventional blood-cell module. HPA indicates that all module genes have tissue annotations, predominantly skin enrichment, with cell-type enrichment mainly involving suprabasal keratinocytes. KRT1 and KRT2 have immune-cell-enhanced annotations, but the overall HPA pattern is not immune-cell dominant; KRT9 is not detected in immune cells. DCD and KRT10 are annotated as secreted in other tissues, while the keratins are intracellular structural proteins. The apparent conservation between circulatory_system and myometrium therefore needs caution: HPA protein data show no detection in myometrium for the module genes, and no matching circulatory-system tissue annotation is available. The module may reflect epithelial or skin-derived material, sample admixture, extracellular debris, or shared technical and cellular composition rather than a native myometrial program.

**GO/KEGG enrichment**: 17 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC keratin filament | 7.23e-06 | KRT1, KRT10, KRT2, KRT9 |
| GO:BP intermediate filament organization | 2.53e-05 | KRT1, KRT10, KRT2, KRT9 |
| GO:BP intermediate filament-based process | 5.88e-05 | KRT1, KRT10, KRT2, KRT9 |
| GO:BP intermediate filament cytoskeleton organization | 5.88e-05 | KRT1, KRT10, KRT2, KRT9 |
| GO:MF structural constituent of skin epidermis | 0.000463 | KRT1, KRT10, KRT2 |
| GO:CC intermediate filament | 0.000491 | KRT1, KRT10, KRT2, KRT9 |
| GO:CC intermediate filament cytoskeleton | 0.000706 | KRT1, KRT10, KRT2, KRT9 |
| KEGG Cornified envelope formation - Homo sapiens (human) | 0.00128 | KRT1, KRT10, KRT2, KRT9 |
| GO:BP skin development | 0.00303 | KRT1, KRT10, KRT2, KRT9 |
| GO:BP epidermis development | 0.00413 | KRT1, KRT10, KRT2, KRT9 |
| GO:CC cornified envelope | 0.0051 | KRT1, KRT10, KRT2 |
| GO:BP peptide cross-linking | 0.0051 | KRT1, KRT10, KRT2 |
| KEGG Cadherin signaling - Homo sapiens (human) | 0.00655 | KRT1, KRT10, KRT2, KRT9 |
| GO:BP keratinocyte differentiation | 0.0351 | KRT1, KRT10, KRT2 |
| GO:BP positive regulation of epidermis development | 0.0476 | KRT10, KRT2 |

### STRING and hu.MAP

STRING provides established high-confidence relationships among KRT1, KRT10, and KRT2, forming a recognized keratin interaction core. KRT9 and DCD have no listed high-confidence STRING partners within this module, although DCD is connected to KRT10 and KRT2 in the co-abundance network. The STRING functional results support keratin filament and cornified-envelope biology (13 supplementary STRING terms; within-query FDR 1.76e-06–0.00025), but they are supplementary evidence rather than globally corrected enrichment. No hu.MAP complex contains at least two module members, so there is no hu.MAP-supported multiprotein complex for this module. Overall, the network combines a known keratin interaction core with co-abundance links that are not all established physical interactions.

**STRING interactions (score >= 0.7)**: 3 of 10 gene pairs: KRT1–KRT10 (0.999); KRT1–KRT2 (0.956); KRT10–KRT2 (0.904)
**STRING functional enrichment (supplementary, within-query FDR)**: DISEASES Epidermolytic hyperkeratosis (FDR = 1.76e-06, 4 genes); Keyword Keratin (FDR = 2.66e-06, 4 genes); Component Keratin filament (FDR = 5.13e-06, 4 genes); COMPARTMENTS Keratin filament (FDR = 5.4e-06, 4 genes); SMART Intermediate filament protein (FDR = 6.65e-06, 4 genes); Keyword Intermediate filament (FDR = 8.62e-06, 4 genes); RCTM Formation of the cornified envelope (FDR = 1.29e-05, 4 genes); PMID (2019) Proteome Profiling of the Exhaled Breath Condensate after Long-Term Spaceflights. (FDR = 3.03e-05, 5 genes); PMID (2018) Proteomics as a new tool to study fingermark ageing in forensics. (FDR = 3.13e-05, 5 genes); InterPro Intermediate filament protein, conserved site (FDR = 3.42e-05, 4 genes); InterPro Intermediate filament, rod domain (FDR = 3.42e-05, 4 genes); DISEASES Bullous congenital ichthyosiform erythroderma (FDR = 0.00018, 3 genes); DISEASES Epidermolytic palmoplantar keratoderma (FDR = 0.00018, 3 genes); PMID (2013) Serine protease HtrA1 accumulates in corneal transforming growth factor beta induced protein (TGFBIp) amyloid deposits. (FDR = 0.00022, 5 genes); COMPARTMENTS Cornified envelope (FDR = 0.00025, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The biological theme is not novel: keratin filament organization, epidermal differentiation, cornification, and keratin-associated disease are well established for this gene set, and the STRING relationships among the principal keratins are already known. What may be novel is the observation that this keratin-associated pattern is conserved between circulatory_system and myometrium in the present co-abundance analysis. That observation should not be called a new biological mechanism without replication, cell-composition controls, and comparison with independent tissue or plasma datasets. The absence of a hu.MAP complex or of some STRING relationships does not establish novelty; it mainly indicates that the co-abundance structure is not fully explained by currently catalogued complexes or interactions.

**Hypothesis.** Hypothesis: the shared module is driven primarily by co-occurring epithelial or skin-derived material rather than by a specialized myometrial pathway. A keratinized-cell or keratin-debris component could generate coordinated abundance of KRT1, KRT10, KRT2, and KRT9 in both sample groups, while secreted DCD could covary with that material or with local epithelial-associated antimicrobial products. The lack of HPA protein detection in myometrium argues against treating this as an established resident myometrial protein program. Testing this hypothesis would require epithelial-cell and contamination markers, microscopy or cell-deconvolution analyses, and replication in independently collected samples.

### Important genes

#### KRT10

- **Related proteins** (co-abundance neighbors): KRT1 (0.95), KRT2 (0.91), DCD (0.86), KRT9 (0.85); STRING partners: KRT1 (0.999), KRT2 (0.904)
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 10. This gene encodes a member of the type I (acidic) cytokeratin family, which belongs to the superfamily of intermediate filament (IF) proteins. Keratins are heteropolymeric structural proteins which form the intermediate filament. These filaments, along with actin microfilaments and microtubules, compose the cytoskeleton of epithelial cells. Mutations in this gene are associated with epidermolytic …
- **Diseases (Open Targets)**: epidermolytic hyperkeratosis 2A, autosomal dominant (0.787); epidermolytic ichthyosis (0.772); congenital reticular ichthyosiform erythroderma (0.727); ichthyosis, annular epidermolytic 1 (0.647); annular epidermolytic ichthyosis (0.642)
- **Europe PMC papers**: 2736
- **Why important**: KRT10 is the most connected hub in the module and belongs to the core keratin interaction group with KRT1 and KRT2. It contributes to every globally corrected GO/KEGG term (17 globally significant GO/KEGG terms, q_global 7.23e-06–0.0498; see the table), is enriched in skin and suprabasal keratinocytes by HPA, and has established roles in intermediate filaments, keratinocyte differentiation, epidermal development, and cornification. Its disease associations include epidermolytic hyperkeratosis and related ichthyotic disorders, and it has extensive literature support.
- **Conclusion**: Established evidence supports KRT10 as a central structural marker of differentiated epidermal keratin biology and a major driver of the module annotation. In this cross-tissue setting, its abundance is more plausibly evidence of a keratinized epithelial component than of a myometrium-specific function. A direct mechanistic role in myometrium is not established.

#### KRT1

- **Related proteins** (co-abundance neighbors): KRT10 (0.95), KRT9 (0.94), KRT2 (0.85); STRING partners: KRT10 (0.999), KRT2 (0.956)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 is a highly connected member of the keratin core and has high-confidence STRING links to KRT10 and KRT2. It participates in nearly all globally corrected terms (15 globally significant GO/KEGG terms, q_global 7.23e-06–0.0498; see the table), is enriched in skin and suprabasal keratinocytes, and is a type II keratin that pairs with type I keratins during epithelial differentiation. It has extensive literature support and well-established associations with epidermolytic and palmoplantar keratoderma disorders.
- **Conclusion**: Established evidence identifies KRT1 as a structural partner and a strong marker of stratified epithelial differentiation. Its presence supports a keratinized epithelial interpretation of the module, but does not demonstrate that KRT1 is functionally active in myometrial cells.

#### KRT2

- **Related proteins** (co-abundance neighbors): KRT10 (0.91), DCD (0.86), KRT1 (0.85); STRING partners: KRT1 (0.956), KRT10 (0.904)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location Intermediate filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 2. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is expressed largely in the upper spinous layer of epidermal keratinocytes and mutations in this gene …
- **Diseases (Open Targets)**: superficial epidermolytic ichthyosis (0.815); exfoliative ichthyosis (0.358); Palmoplantar hyperkeratosis (0.267); hereditary disease (0.193); Vertigo (0.145)
- **Europe PMC papers**: 7459
- **Why important**: KRT2 is a highly connected keratin-core member with high-confidence STRING relationships to KRT1 and KRT10 and a co-abundance link to DCD. It contributes to all globally corrected terms (17 globally significant GO/KEGG terms, q_global 7.23e-06–0.0498; see the table), is enriched in suprabasal keratinocytes, and is associated with epidermis development, keratinization, keratinocyte activation, and proliferation. Its disease associations include epidermolytic and exfoliative ichthyotic conditions, and it has extensive literature support.
- **Conclusion**: Established evidence supports KRT2 as a differentiated epidermal structural keratin and an important bridge between the keratin core and DCD in this network. Its co-abundance with DCD may reflect shared epithelial material, but any direct functional interaction in the sampled tissues remains a hypothesis.

#### KRT9

- **Related proteins** (co-abundance neighbors): KRT1 (0.94), KRT10 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 9. This gene encodes the type I keratin 9, an intermediate filament chain expressed only in the terminally differentiated epidermis of palms and soles. Mutations in this gene cause epidermolytic palmoplantar keratoderma. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: epidermolytic palmoplantar keratoderma, 1 (0.828); palmoplantar keratoderma, epidermolytic (0.682); Localized epidermolytic hyperkeratosis (0.511); Palmoplantar hyperkeratosis (0.456); Palmoplantar keratoderma (0.438)
- **Europe PMC papers**: 773
- **Why important**: KRT9 links into the keratin network through KRT1 and KRT10 and is included in the globally corrected keratin-filament, intermediate-filament, epidermal-development, and epithelial-differentiation terms (11 globally significant GO/KEGG terms, q_global 7.23e-06–0.0489; see the table). It is a specialized type I keratin of terminally differentiated palmoplantar epidermis and is associated with epidermolytic palmoplantar keratoderma. HPA places it in a distinctive tissue and cell-type pattern and does not detect it in immune cells.
- **Conclusion**: Established evidence supports KRT9 as a specialized terminal-differentiation marker that strengthens the epidermal interpretation of the module. Its unusual tissue pattern makes it especially useful as a possible indicator of epithelial or sample-composition effects. A native role in myometrial co-abundance is not established.

#### DCD

- **Related proteins** (co-abundance neighbors): KRT10 (0.86), KRT2 (0.86); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dermcidin. This antimicrobial gene encodes a secreted protein that is subsequently processed into mature peptides of distinct biological activities. The C-terminal peptide is constitutively expressed in sweat and has antibacterial and antifungal activities. The N-terminal peptide, also known as diffusible survival evasion peptide, promotes neural cell survival under conditions of severe oxidative stress. A g…
- **Diseases (Open Targets)**: esophageal ulcer (0.276); biliary tract disorder (0.148); Dupuytren Contracture (0.140); Hypocalcemia (0.082); intracranial hemorrhage (0.082)
- **Europe PMC papers**: 3862
- **Why important**: DCD is a peripheral network member connected to KRT10 and KRT2 rather than part of the globally corrected GO/KEGG core. It encodes a secreted antimicrobial precursor with additional processed peptide activities, is skin-enriched by HPA, is enriched in smooth muscle cells at the single-cell annotation level, and has substantial literature support. STRING literature-derived associations place it in the same broader keratin-associated context (STRING PMID (2019) Proteome Profiling of the Exhaled Breath Condensate after Long-Term Spaceflights.; within-query FDR = 3.03e-05) (STRING PMID (2018) Proteomics as a new tool to study fingermark ageing in forensics.; within-query FDR = 3.13e-05) (STRING PMID (2013) Serine protease HtrA1 accumulates in corneal transforming growth factor beta induced protein (TGFBIp) amyloid deposits.; within-query FDR = 0.00022).
- **Conclusion**: Established evidence supports DCD as a secreted antimicrobial and processed-peptide gene that co-abundance links to the keratin module. Its lack of globally corrected GO/KEGG participation argues against making it a principal driver of the module function. Its relationship to the keratinized component, and its relevance to myometrium, remain hypotheses requiring direct validation.
