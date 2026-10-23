# Conserved co-abundance modules: circulatory_system and heart

## Module 0

**Tissue pair**: circulatory_system and heart  
**Genes (8)**: A1BG, A2M, SERPINC1, CP, C3, HPX, SERPING1, GC

### Function

This is a circulating plasma protein module centered on complement regulation, humoral immunity, protease inhibition, and the interface between complement and coagulation. The strongest primary evidence is the globally significant blood microparticle term (GO:CC blood microparticle; q_global = 4.92e-06), which contains every module gene. The globally significant terms for regulation of humoral immune response (GO:BP regulation of humoral immune response; q_global = 0.000939), regulation of complement activation (GO:BP regulation of complement activation; q_global = 0.0297), humoral immune response (GO:BP humoral immune response; q_global = 0.0321), complement and coagulation cascades (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0321), and peptidase or endopeptidase inhibitor activity (GO:MF endopeptidase inhibitor activity; q_global = 0.0399)(GO:MF peptidase inhibitor activity; q_global = 0.0399) provide a coherent functional interpretation. C3 supplies the central complement component, SERPING1 restrains complement activation, A2M broadly traps proteases and can modulate inflammatory cytokines, and SERPINC1 regulates coagulation proteases. HPX, CP, and GC support extracellular transport and blood-protein functions, while the module-wide blood microparticle signal indicates that the co-abundance pattern is principally an extracellular plasma signature.

**Cell composition.** All module genes are annotated as secreted to blood by HPA, and the HPA tissue pattern is dominated by liver enrichment, with hepatocytes the dominant enriched single-cell population. This strongly suggests that the shared circulatory-system and heart signal may reflect circulating plasma proteins or common blood exposure rather than a heart-intrinsic transcriptional program. Most genes are not detected in immune cells, although A2M has immune-cell enhancement and C3 and SERPING1 have immune-cell enrichment or enhancement in particular populations. Thus the module is not best described as a blood-cell expression module; it is more consistent with a liver-derived plasma-protein module measured in samples from both tissues. HPA protein detection in heart is limited to A2M and GC, while the other proteins are not detected there, further favoring a circulating or sample-composition explanation over broad local heart production.

**GO/KEGG enrichment**: 7 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 4.92e-06 | A1BG, A2M, C3, CP, GC, HPX, SERPINC1, SERPING1 |
| GO:BP regulation of humoral immune response | 0.000939 | A2M, C3, HPX, SERPING1 |
| GO:BP regulation of complement activation | 0.0297 | A2M, C3, SERPING1 |
| GO:BP humoral immune response | 0.0321 | A2M, C3, HPX, SERPING1 |
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 0.0321 | A2M, C3, SERPINC1, SERPING1 |
| GO:MF endopeptidase inhibitor activity | 0.0399 | A2M, C3, SERPINC1, SERPING1 |
| GO:MF peptidase inhibitor activity | 0.0399 | A2M, C3, SERPINC1, SERPING1 |

### STRING and hu.MAP

STRING supports a densely connected extracellular protein network. The strongest established relationships include A2M with SERPINC1 and SERPING1, C3 with SERPING1 and HPX, and the transport or binding associations involving HPX, CP, GC, and the other plasma proteins. These links are consistent with complement control, protease inhibition, heme and metal handling, and shared plasma abundance; they should not automatically be interpreted as direct physical binding in every case. STRING also returns blood-microparticle, secreted, glycoprotein, and plasma-proteomics evidence (STRING COMPARTMENTS Blood microparticle; within-query FDR = 4.87e-07)(STRING Component Blood microparticle; within-query FDR = 4.92e-07)(STRING PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers.; within-query FDR = 4.12e-05)(STRING Keyword Signal; within-query FDR = 5.95e-05)(STRING Keyword Secreted; within-query FDR = 5.95e-05)(STRING Keyword Glycoprotein; within-query FDR = 6.77e-05). hu.MAP independently places many module members in several recurring plasma-protein and complement or coagulation complexes (hu.MAP huMAP3_15040.1)(hu.MAP huMAP3_10678.1)(hu.MAP huMAP3_09531.1)(hu.MAP huMAP3_10101.1). The repeated membership of CP, A2M, C3, HPX, A1BG, and SERPING1 across these complexes indicates that the module overlaps known extracellular protein assemblies. A1BG has no listed STRING partner, so its module membership may represent coordinated plasma abundance rather than a well-established interaction.

**STRING interactions (score >= 0.7)**: 13 of 28 gene pairs: A2M–CP (0.889); A2M–HPX (0.824); A2M–SERPINC1 (0.927); A2M–SERPING1 (0.905); C3–CP (0.751); C3–GC (0.768); C3–HPX (0.841); C3–SERPING1 (0.954); CP–HPX (0.88); GC–HPX (0.827); GC–SERPINC1 (0.84); HPX–SERPINC1 (0.762); SERPINC1–SERPING1 (0.753)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Blood microparticle (FDR = 4.87e-07, 8 genes); Component Blood microparticle (FDR = 4.92e-07, 8 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 4.12e-05, 8 genes); PMID (2017) Lectins: an effective tool for screening of potential cancer biomarkers. (FDR = 4.12e-05, 7 genes); PMID (2012) Assessment of two immunodepletion methods: off-target effects and variations in immunodepletion efficiency may confound plasma proteomics. (FDR = 4.12e-05, 7 genes); PMID (2020) Significant correlation between plasma proteome profile and pain intensity, sensitivity, and psychological distress in women with fibromyalgia. (FDR = 4.38e-05, 7 genes); TISSUES Bone marrow cell (FDR = 4.43e-05, 7 genes); PMID (2021) Urinary Protein and Peptide Markers in Chronic Kidney Disease. (FDR = 4.66e-05, 7 genes); PMID (2020) Revelation of Proteomic Indicators for Colorectal Cancer in Initial Stages of Development. (FDR = 4.66e-05, 7 genes); PMID (2013) Urinary prognostic biomarkers and classification of IgA nephropathy by high resolution mass spectrometry coupled with liquid chromatography. (FDR = 4.66e-05, 6 genes); PMID (1991) Changes in 40 serum proteins of post-menopausal women. (FDR = 4.66e-05, 6 genes); Keyword Signal (FDR = 5.95e-05, 8 genes); Keyword Secreted (FDR = 5.95e-05, 8 genes); Keyword Glycoprotein (FDR = 6.77e-05, 8 genes); Keyword Disulfide bond (FDR = 6.77e-05, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (CP, SERPINC1, A2M, C3, GC, HPX, A1BG, SERPING1; 8/64); huMAP3_10678.1 (CP, A2M, C3, GC, HPX, A1BG, SERPING1; 7/71); huMAP3_09531.1 (CP, A2M, C3, HPX, A1BG, SERPING1; 6/47); huMAP3_10101.1 (CP, A2M, C3, HPX, A1BG, SERPING1; 6/49); huMAP3_08395.1 (CP, A2M, C3, HPX, A1BG; 5/43); huMAP3_07432.1 (CP, C3, HPX, A1BG; 4/18); huMAP3_07265.1 (CP, A2M, HPX, A1BG; 4/20); huMAP3_09273.1 (CP, A2M, HPX, SERPING1; 4/28); huMAP3_02236.1 (CP, HPX, A1BG; 3/7); huMAP3_08700.1 (CP, HPX, A1BG; 3/11); huMAP3_09434.1 (C3, GC, A1BG; 3/33); huMAP3_08224.1 (C3, GC; 2/21)

### Novelty

The biological theme is not a wholly new discovery: the principal proteins, complement and coagulation functions, blood-microparticle association, and many protein relationships are already represented in STRING and hu.MAP. The co-abundance module may still be a useful new observation in the specific circulatory-system and heart comparison, especially if this exact tissue-pair organization has not previously been reported, but the fact sheet does not establish that it is novel. Absence of a particular relationship from STRING or hu.MAP would not prove novelty, because those resources capture known interactions and complexes rather than every abundance correlation. The most defensible conclusion is that this is a biologically coherent rediscovery of a known plasma complement, coagulation, and transport program, with possible novelty at the level of tissue-pair co-abundance structure rather than molecular function.

**Hypothesis.** Hypothesis: variation in liver-derived plasma protein abundance creates a coordinated extracellular buffering module that controls complement activation, inflammatory proteases, coagulation proteases, heme or metal transport, and associated oxidative or tissue stress. In samples from both circulatory system and heart, this shared plasma signal could arise because blood-derived proteins or blood microparticles contribute substantially to the measured material. C3 may provide complement activation capacity, while SERPING1 and A2M restrain inflammatory and proteolytic amplification, SERPINC1 limits coagulation proteases, and HPX and CP help manage heme, iron, and copper-related extracellular stress. This is a mechanistic model consistent with the annotations and network, not proof that these proteins form one physical complex or that the module is produced locally by heart cells.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): HPX (0.90), SERPING1 (0.87); STRING partners: CP (0.751), GC (0.768), HPX (0.841), SERPING1 (0.954)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_08224.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is the principal complement component in the module and is present in every primary immune and inhibitor-related enrichment cluster that includes it (GO:CC blood microparticle; q_global = 4.92e-06)(GO:BP regulation of humoral immune response; q_global = 0.000939)(GO:BP regulation of complement activation; q_global = 0.0297)(GO:BP humoral immune response; q_global = 0.0321)(KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0321)(GO:MF endopeptidase inhibitor activity; q_global = 0.0399)(GO:MF peptidase inhibitor activity; q_global = 0.0399). It connects to HPX and SERPING1 in STRING and appears across multiple hu.MAP complexes (hu.MAP huMAP3_15040.1)(hu.MAP huMAP3_10678.1)(hu.MAP huMAP3_09531.1)(hu.MAP huMAP3_10101.1). Its disease associations include complement deficiency, complement glomerulopathy, atypical hemolytic-uremic syndrome, and age-related macular degeneration. It also has a very large literature base, making it the clearest functional anchor for the module.
- **Conclusion**: Established evidence identifies C3 as the module's complement-activation hub and a major candidate driver of its humoral immune signal. It is probably a core biological component, although the co-abundance data alone do not establish that C3 initiates the module.

#### SERPING1

- **Related proteins** (co-abundance neighbors): C3 (0.87), HPX (0.83); STRING partners: A2M (0.905), C3 (0.954), SERPINC1 (0.753)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_09273.1
- **Function (MyGene.info)**: serpin family G member 1. This gene encodes a highly glycosylated plasma protein involved in the regulation of the complement cascade. Its encoded protein, C1 inhibitor, inhibits activated C1r and C1s of the first complement component and thus regulates complement activation. It is synthesized in the liver, and its deficiency is associated with hereditary angioneurotic oedema (HANE). Alternative splicing results in multipl…
- **Diseases (Open Targets)**: hereditary angioedema with C1Inh deficiency (0.828); hereditary angioedema type 1 (0.750); hereditary angioedema (0.728); angioedema (0.616); hereditary angioedema type 2 (0.614)
- **Europe PMC papers**: 4203
- **Why important**: SERPING1 is a direct regulator of complement activation, inhibits activated C1r and C1s, and is included in all of the globally significant complement, humoral-response, and protease-inhibitor terms (GO:CC blood microparticle; q_global = 4.92e-06)(GO:BP regulation of humoral immune response; q_global = 0.000939)(GO:BP regulation of complement activation; q_global = 0.0297)(GO:BP humoral immune response; q_global = 0.0321)(KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0321)(GO:MF endopeptidase inhibitor activity; q_global = 0.0399)(GO:MF peptidase inhibitor activity; q_global = 0.0399). It has a strong STRING relationship with C3 and additional links to A2M and SERPINC1, while recurring hu.MAP membership places it in complement and plasma-protein assemblies (hu.MAP huMAP3_15040.1)(hu.MAP huMAP3_10678.1)(hu.MAP huMAP3_09531.1)(hu.MAP huMAP3_10101.1)(hu.MAP huMAP3_09273.1). Its association with hereditary angioedema gives the module direct clinical relevance, and its literature base supports a well-established role.
- **Conclusion**: Established evidence makes SERPING1 the strongest inhibitory counterpart to C3 in this module. Its coordinated abundance may represent protection against excessive complement or protease activation, but a causal buffering role in these tissue samples remains a hypothesis.

#### A2M

- **Related proteins** (co-abundance neighbors): CP (0.94), HPX (0.91); STRING partners: CP (0.889), HPX (0.824), SERPINC1 (0.927), SERPING1 (0.905)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_07265.1, huMAP3_09273.1
- **Function (MyGene.info)**: alpha-2-macroglobulin. The protein encoded by this gene is a protease inhibitor and cytokine transporter. It uses a bait-and-trap mechanism to inhibit a broad spectrum of proteases, including trypsin, thrombin and collagenase. It can also inhibit inflammatory cytokines, and it thus disrupts inflammatory cascades. Mutations in this gene are a cause of alpha-2-macroglobulin deficiency. This gene is implicated in Alzheimer…
- **Diseases (Open Targets)**: myopia (0.206); refractive error (0.151); primary angle-closure glaucoma (0.148); Abnormality of refraction (0.144); Aganglionic megacolon (0.118)
- **Europe PMC papers**: 5133
- **Why important**: A2M is annotated as a broad protease inhibitor and cytokine transporter with a bait-and-trap mechanism. It participates in every primary term involving complement regulation, humoral immunity, the complement and coagulation cascade, and peptidase inhibition (GO:CC blood microparticle; q_global = 4.92e-06)(GO:BP regulation of humoral immune response; q_global = 0.000939)(GO:BP regulation of complement activation; q_global = 0.0297)(GO:BP humoral immune response; q_global = 0.0321)(KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0321)(GO:MF endopeptidase inhibitor activity; q_global = 0.0399)(GO:MF peptidase inhibitor activity; q_global = 0.0399). Its STRING connections include SERPINC1, SERPING1, CP, and HPX, and it recurs across several hu.MAP complexes (hu.MAP huMAP3_15040.1)(hu.MAP huMAP3_10678.1)(hu.MAP huMAP3_09531.1)(hu.MAP huMAP3_10101.1)(hu.MAP huMAP3_08395.1)(hu.MAP huMAP3_07265.1)(hu.MAP huMAP3_09273.1). It is detected in heart by HPA and has associations with alpha-two-macroglobulin deficiency and Alzheimer disease, with substantial literature support.
- **Conclusion**: Established evidence supports A2M as a broad extracellular protease and inflammatory regulator that links the module's complement and coagulation themes. Its heart detection makes local contribution possible, but the liver and secreted-to-blood pattern still favors a substantial circulating component.

#### SERPINC1

- **Related proteins** (co-abundance neighbors): A1BG (0.84); STRING partners: A2M (0.927), GC (0.84), HPX (0.762), SERPING1 (0.753)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 encodes antithrombin, a plasma serpin that regulates blood coagulation and is included in the primary complement-and-coagulation and peptidase-inhibitor terms (GO:CC blood microparticle; q_global = 4.92e-06)(KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0321)(GO:MF endopeptidase inhibitor activity; q_global = 0.0399)(GO:MF peptidase inhibitor activity; q_global = 0.0399). It connects in STRING to A2M, GC, HPX, and SERPING1, thereby linking coagulation control with the rest of the extracellular network. Its disease associations include hereditary antithrombin deficiency and venous thromboembolic disorders. The gene has a substantial literature base and provides the clearest coagulation-specific anchor.
- **Conclusion**: Established evidence identifies SERPINC1 as the module's coagulation-regulatory arm and supports a complement-coagulation interface. Its coordinated abundance should not be taken as evidence of altered coagulation activity without functional or clinical measurements.

#### HPX

- **Related proteins** (co-abundance neighbors): A2M (0.91), C3 (0.90), GC (0.86), CP (0.86), A1BG (0.83), SERPING1 (0.83); STRING partners: A2M (0.824), C3 (0.841), CP (0.88), GC (0.827), SERPINC1 (0.762)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09273.1, huMAP3_02236.1, huMAP3_08700.1
- **Function (MyGene.info)**: hemopexin. This gene encodes a plasma glycoprotein that binds heme with high affinity. The encoded protein is an acute phase protein that transports heme from the plasma to the liver and may be involved in protecting cells from oxidative stress. [provided by RefSeq, Apr 2009].
- **Diseases (Open Targets)**: panniculitis (0.116); neoplasm (0.107); familial idiopathic steroid-resistant nephrotic syndrome (0.101); hepatocellular carcinoma (0.101); focal segmental glomerulosclerosis (0.097)
- **Europe PMC papers**: 6894
- **Why important**: HPX has the broadest listed module connectivity and the greatest weighted network strength, linking A2M, C3, GC, CP, A1BG, and SERPING1. It is present in the globally significant blood-microparticle and humoral-response terms (GO:CC blood microparticle; q_global = 4.92e-06)(GO:BP regulation of humoral immune response; q_global = 0.000939)(GO:BP humoral immune response; q_global = 0.0321), recurs throughout STRING and hu.MAP evidence (STRING COMPARTMENTS Blood microparticle; within-query FDR = 4.87e-07)(STRING Component Blood microparticle; within-query FDR = 4.92e-07)(hu.MAP huMAP3_15040.1)(hu.MAP huMAP3_10678.1)(hu.MAP huMAP3_09531.1)(hu.MAP huMAP3_10101.1), and encodes a secreted heme-binding acute-phase protein that transports heme to the liver. Its disease associations include panniculitis, hepatocellular carcinoma, and kidney disorders, and it has substantial literature support.
- **Conclusion**: Established evidence makes HPX a network bridge between complement-associated proteins and extracellular heme or stress handling. It is a strong candidate for organizing the co-abundance signal, but the network does not prove that HPX mechanistically coordinates the other proteins.

## Module 1

**Tissue pair**: circulatory_system and heart  
**Genes (7)**: ACADM, CRAT, GPD1L, IMMT, NDUFA10, NNT, SUCLA2

### Function

The module is most consistent with coordinated mitochondrial energy metabolism in heart and circulatory-system samples. Its genes cover several connected processes: fatty-acid oxidation through ACADM and CRAT, the tricarboxylic-acid cycle through SUCLA2, respiratory-chain electron transfer through NDUFA10, mitochondrial NADPH and redox support through NNT, inner-membrane cristae organization through IMMT, and glycerol-phosphate and related metabolic functions through GPD1L. However, no GO or KEGG term passed global correction, so this functional interpretation is based on the individual gene annotations and the network pattern rather than statistically significant module-level enrichment. The network is compatible with a mitochondrial bioenergetics program, but it is not sufficient to establish one single pathway or direct physical complex.

**Cell composition.** The module is not composed of plasma or secreted proteins: the genes have no secreted-gene annotation. All genes have low immune-cell specificity, with no recurring blood-cell enrichment, arguing against a blood-cell-driven module. HPA indicates tissue-enhanced expression throughout the module, particularly in skeletal muscle and tongue, with additional liver enrichment for ACADM. Several genes show cell-type enhancement in muscle-related, epithelial, hepatic, reproductive, or cardiac-associated cell types, while NDUFA10 has low cell-type specificity. Protein detection in heart muscle is reported for most of the module, with mitochondrial localization especially evident for SUCLA2, NDUFA10, IMMT, NNT, and ACADM. Thus, the shared signal is more plausibly related to metabolically active muscle or other tissue composition than to circulating plasma proteins, although sample cellular composition remains an alternative explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supplies one high-confidence relationship, ACADM–SUCLA2, and reports no supplementary functional enrichment. This known connection links medium-chain fatty-acid oxidation with a tricarboxylic-acid-cycle enzyme, supporting a mitochondrial metabolism interpretation but leaving most module edges without STRING support. hu.MAP identifies complex C1, containing ACADM and NNT among the module members and additional proteins outside the module. This provides partial complex-level support, but the module members are not represented as a broad set of established partners in the available hu.MAP evidence. The remaining co-abundance edges should therefore be interpreted primarily as expression-coordination relationships rather than demonstrated physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: ACADM–SUCLA2 (0.755)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12388.1 (ACADM, NNT; 2/7)

### Novelty

The module may represent a tissue-shared co-abundance pattern that is not captured by currently catalogued physical-interaction or complex annotations, because only the ACADM–SUCLA2 relationship is supported by STRING and only the ACADM–NNT pair is represented together in the reported hu.MAP complex. Nevertheless, this does not prove that the biological module is novel: the constituent mitochondrial functions and several gene relationships are already established, and co-abundance can arise from shared tissue composition or coordinated mitochondrial abundance. The most defensible conclusion is that the specific cross-tissue co-abundance organization is potentially under-described, while its underlying biology is not new.

**Hypothesis.** Hypothesis: in heart and circulatory-system samples, a metabolically active muscle-associated cell population generates coordinated abundance of mitochondrial enzymes and structural proteins. Fatty-acid input through ACADM and CRAT may supply acetyl and related carbon flux, SUCLA2 may connect this metabolism to the tricarboxylic-acid cycle, NDUFA10 may support respiratory electron transfer, NNT may maintain mitochondrial NADPH and redox capacity, and IMMT may preserve cristae architecture. GPD1L may connect glycerol-phosphate metabolism with cardiac electrical physiology through its reported association with SCN5A. This model predicts coordinated mitochondrial abundance and redox or substrate-handling capacity, but the present data do not demonstrate causal regulation, direct protein binding, or a unique heart-specific mechanism.

### Important genes

#### GPD1L

- **Related proteins** (co-abundance neighbors): CRAT (0.84), IMMT (0.83), NDUFA10 (0.82), SUCLA2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycerol-3-phosphate dehydrogenase 1 like. The protein encoded by this gene catalyzes the conversion of sn-glycerol 3-phosphate to glycerone phosphate. The encoded protein is found in the cytoplasm, associated with the plasma membrane, where it binds the sodium channel, voltage-gated, type V, alpha subunit (SCN5A). Defects in this gene are a cause of Brugada syndrome type 2 (BRS2) as well as sudden infant death syndrome (SIDS). [provided b…
- **Diseases (Open Targets)**: Brugada syndrome (0.337); dementia (0.209); Abnormality of the cardiovascular system (0.194); Prolonged QT interval (0.149); dilated cardiomyopathy (0.119)
- **Europe PMC papers**: 1327
- **Why important**: GPD1L is the highest-positioned node in the module by weighted connectivity and links CRAT, IMMT, NDUFA10, and SUCLA2. Its annotations connect glycerol-phosphate and carbohydrate metabolism with NAD-related metabolism, heart-rate regulation, and sodium transport. It is tissue-enhanced in skeletal muscle and tongue, and its reported association with SCN5A and disease links to Brugada syndrome and sudden infant death make it particularly relevant to cardiac interpretation. Its extensive literature presence also makes it a comparatively well-characterized anchor for the module.
- **Conclusion**: Established evidence supports GPD1L as a central co-abundance connector with metabolic and cardiac-electrical relevance. It is plausible that GPD1L helps link mitochondrial metabolism to cardiac excitability, but the module does not establish that it regulates the other genes or drives the shared tissue pattern.

#### SUCLA2

- **Related proteins** (co-abundance neighbors): NNT (0.82), ACADM (0.81), GPD1L (0.80); STRING partners: ACADM (0.755)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase ADP-forming subunit beta. Succinyl-CoA synthetase (SCS) is a mitochondrial matrix enzyme that acts as a heterodimer, being composed of an invariant alpha subunit and a substrate-specific beta subunit. The protein encoded by this gene is an ATP-specific SCS beta subunit that dimerizes with the SCS alpha subunit to form SCS-A, an essential component of the tricarboxylic acid cycle. SCS-A hydrolyzes ATP to convert succinate t…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome, encephalomyopathic form with methylmalonic aciduria (0.816); mitochondrial DNA depletion syndrome, encephalomyopathic form (0.581); neurodegenerative disease (0.485); mitochondrial disease (0.374); disease of peritoneum (0.372)
- **Europe PMC papers**: 1440
- **Why important**: SUCLA2 is a highly connected module member and is directly linked to ACADM by STRING, the clearest known interaction in the module. It encodes the ATP-specific beta subunit of succinyl-CoA synthetase and therefore represents a direct tricarboxylic-acid-cycle and mitochondrial-energy component. Its heart protein detection, mitochondrial localization, and association with mitochondrial DNA depletion syndrome strengthen its relevance to cardiac bioenergetics.
- **Conclusion**: Established evidence supports SUCLA2 as a core mitochondrial metabolic gene and as one endpoint of the module's best-supported known interaction. Its co-abundance with the other genes is consistent with shared energy demand, but a direct regulatory role within this module remains a hypothesis.

#### NNT

- **Related proteins** (co-abundance neighbors): SUCLA2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_12388.1
- **Function (MyGene.info)**: nicotinamide nucleotide transhydrogenase. This gene encodes an integral protein of the inner mitochondrial membrane. The enzyme couples hydride transfer between NAD(H) and NADP(+) to proton translocation across the inner mitochondrial membrane. Under most physiological conditions, the enzyme uses energy from the mitochondrial proton gradient to produce high concentrations of NADPH. The resulting NADPH is used for biosynthesis and in free …
- **Diseases (Open Targets)**: familial glucocorticoid deficiency (0.638); neurodegenerative disease (0.497); hereditary disease (0.453); atypical hemolytic-uremic syndrome with DGKE deficiency (0.416); Abnormality of the skeletal system (0.396)
- **Europe PMC papers**: 6111
- **Why important**: NNT connects to SUCLA2 in the co-abundance network and participates in the reported hu.MAP complex containing ACADM. It is an inner-mitochondrial-membrane enzyme that generates NADPH used for biosynthesis and reactive-oxygen control. HPA shows enhancement in skeletal muscle and several cell types including cardiomyocytes, with heart protein detection. Its disease associations include familial glucocorticoid deficiency and broader mitochondrial or hereditary disease categories.
- **Conclusion**: Established evidence supports NNT as a redox-support component that could protect energy-producing tissue from oxidative stress. Its placement may indicate coupling between carbon metabolism and redox maintenance, but the available evidence does not prove that NNT coordinates the module or physically interacts with SUCLA2 in these tissues.

#### ACADM

- **Related proteins** (co-abundance neighbors): SUCLA2 (0.81); STRING partners: SUCLA2 (0.755)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_12388.1
- **Function (MyGene.info)**: acyl-CoA dehydrogenase medium chain. This gene encodes the medium-chain specific (C4 to C12 straight chain) acyl-Coenzyme A dehydrogenase. The homotetramer enzyme catalyzes the initial step of the mitochondrial fatty acid beta-oxidation pathway. Defects in this gene cause medium-chain acyl-CoA dehydrogenase deficiency, a disease characterized by hepatic dysfunction, fasting hypoglycemia, and encephalopathy, which can result in infant…
- **Diseases (Open Targets)**: medium chain acyl-CoA dehydrogenase deficiency (0.854); hereditary disease (0.516); rhabdomyolysis (0.370); short chain acyl-CoA dehydrogenase deficiency (0.349); Epileptic spasm (0.333)
- **Europe PMC papers**: 4795
- **Why important**: ACADM is the mitochondrial medium-chain fatty-acyl dehydrogenase and represents the module's clearest fatty-acid oxidation entry point. It has a known STRING relationship with SUCLA2 and shares the reported hu.MAP complex with NNT. It is enhanced in liver, skeletal muscle, and tongue, is detected in heart, and has a strong established disease association with medium-chain acyl-CoA dehydrogenase deficiency, including hepatic and fasting-energy phenotypes.
- **Conclusion**: Established evidence supports ACADM as a biologically important substrate-oxidation component and as a bridge between the module and known mitochondrial interaction resources. Its presence supports a fuel-utilization interpretation, while the co-abundance data alone cannot show that fatty-acid oxidation is the primary driver of the entire module.

#### CRAT

- **Related proteins** (co-abundance neighbors): GPD1L (0.84), NDUFA10 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carnitine O-acetyltransferase. This gene encodes carnitine O-acetyltransferase, a member of the carnitine acyltransferase family and a key metabolic pathway enzyme which plays an important role in energy homeostasis and fat metabolism. This enzyme catalyzes the reversible transfer of acyl groups from an acyl-CoA thioester to carnitine and regulates the ratio of acyl-CoA/CoA. It is found in both the mitochondria and the peroxiso…
- **Diseases (Open Targets)**: neurodegeneration with brain iron accumulation 8 (0.499); neurodegeneration with brain iron accumulation (0.341); neurodegenerative disease (0.301); Alzheimer disease (0.252); lysosomal storage disease (0.247)
- **Europe PMC papers**: 4594
- **Why important**: CRAT is connected to GPD1L and NDUFA10 and encodes carnitine O-acetyltransferase, which regulates the acyl-CoA to CoA balance and participates in fatty-acid and short-chain carbon metabolism. It is heart-detected and enriched in skeletal muscle and several metabolically active cell types. Its broad disease and literature representation makes it a useful metabolic interpreter even though it lacks STRING and hu.MAP support in this module.
- **Conclusion**: Established evidence supports CRAT as a plausible regulator of acyl-group handling and metabolic flexibility. Its network position suggests coordination with glycerol-phosphate metabolism and respiratory function, but the absence of external interaction support means that this proposed coordination should remain tentative.

#### NDUFA10

- **Related proteins** (co-abundance neighbors): CRAT (0.83), GPD1L (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit A10. The protein encoded by this gene is a component of 42 kDa complex I, the first enzyme complex in the electron transport chain of mitochondria. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. A mutation in this gene was found in an individual with Leigh syndrome. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.677); Leigh syndrome (0.674); mitochondrial complex I deficiency, nuclear type 22 (0.668); type 2 diabetes mellitus (0.620); diabetes mellitus (0.578)
- **Europe PMC papers**: 1163
- **Why important**: NDUFA10 connects CRAT and GPD1L and encodes a component of mitochondrial respiratory complex I involved in NADH-to-ubiquinone electron transfer and proton-motive-force-driven ATP production. It is heart-detected and mitochondrially localized, with a reported association with Leigh syndrome and complex-I deficiency. Its inclusion provides a direct respiratory-chain dimension to a module otherwise weighted toward substrate and intermediary metabolism.
- **Conclusion**: Established evidence supports NDUFA10 as the module's respiratory electron-transfer representative. Its co-abundance with substrate-handling genes is consistent with coordinated energy production, but the module does not demonstrate a direct physical or regulatory connection among these proteins.

## Module 2

**Tissue pair**: circulatory_system and heart  
**Genes (11)**: AMBP, CFB, FBN1, KGD4, LAMB2, LUM, NRAP, HSPG2, PLEC, F2, VTN

### Function

The module is best interpreted as a blood-facing extracellular-matrix and vascular-interface program, with a coagulation/complement component and a cardiac structural component. The strongest primary evidence is the globally corrected Golgi-lumen enrichment (GO:CC Golgi lumen; q_global = 0.00317), contributed by F2, HSPG2, LUM and VTN, and the globally corrected glial-cell-differentiation term (GO:BP glial cell differentiation; q_global = 0.0354), contributed by F2, LAMB2, PLEC and VTN. The latter should not be read as evidence that this heart module is a glial program; these genes have extracellular-matrix, adhesion, muscle and tissue-structural functions in the fact sheet. Supplementary STRING terms support a coherent secreted, glycoprotein, basement-membrane and extracellular-matrix theme (10 supplementary STRING terms; within-query FDR 0.001–0.0233), while also identifying proteolytic or complement-related features (STRING Keyword Cleavage on pair of basic residues; within-query FDR = 0.0322). Thus, the most defensible functional interpretation is coordinated extracellular matrix organization and cell-matrix signaling at a vascular or cardiac tissue interface, potentially coupled to circulating coagulation and innate immune factors.

**Cell composition.** The module is strongly biased toward secreted or extracellular-matrix proteins: eight genes are classified as secreted by HPA, including several secreted to blood and several secreted to extracellular matrix. HPA most often points to liver and hepatocytes, with additional enrichment in placenta, skeletal muscle, adipose tissue, gallbladder, hepatic stellate cells, cholangiocytes, adipocytes and fibro-adipogenic progenitors. Most genes are not detected in immune cells and only one is immune-cell enriched, arguing against a primarily blood-cell module. The presence of F2, AMBP, CFB and VTN, together with liver and hepatocyte enrichment, means that the shared circulatory-system and heart signal may partly reflect plasma proteins or blood exposure in the samples rather than expression by cardiomyocytes. At the same time, NRAP, PLEC, LAMB2 and HSPG2 have heart, muscle, vascular or structural evidence, so a genuine tissue-interface component remains plausible. HPA protein detection in heart is present for some structural genes but absent for several liver-derived or circulating proteins, reinforcing a mixed plasma-plus-tissue interpretation.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC Golgi lumen | 0.00317 | F2, HSPG2, LUM, VTN |
| GO:BP glial cell differentiation | 0.0354 | F2, LAMB2, PLEC, VTN |

### STRING and hu.MAP

STRING provides a connected extracellular network rather than independent support for every co-abundance edge. Established high-confidence relationships include AMBP with F2 and VTN, and a matrix-centered group involving FBN1, HSPG2, LUM and VTN. FBN1-LUM is especially consistent with extracellular-matrix organization, while FBN1-HSPG2 and HSPG2-VTN connect matrix scaffolding and adhesive glycoprotein biology. LAMB2, CFB, NRAP, PLEC and KGD4 have weaker or absent STRING partner coverage in the supplied network, so their co-abundance links should not be treated as established physical interactions. hu.MAP repeatedly places F2 and CFB together in broad circulating protein and complement/coagulation-associated complexes (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1). These complexes contain many plasma proteins, so they support a shared blood-protein context, but their breadth and limited module representation do not establish a compact molecular complex formed by the whole module.

**STRING interactions (score >= 0.7)**: 7 of 55 gene pairs: AMBP–F2 (0.979); AMBP–VTN (0.737); FBN1–HSPG2 (0.849); FBN1–LUM (0.972); FBN1–VTN (0.806); HSPG2–LUM (0.78); HSPG2–VTN (0.797)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Repeat (FDR = 0.00028, 10 genes); Keyword Signal (FDR = 0.001, 8 genes); Keyword Secreted (FDR = 0.001, 8 genes); Keyword Glycoprotein (FDR = 0.0016, 8 genes); Keyword Disulfide bond (FDR = 0.0016, 8 genes); Component Golgi lumen (FDR = 0.0045, 4 genes); TISSUES Plasma cell (FDR = 0.009, 6 genes); Component Collagen-containing extracellular matrix (FDR = 0.0096, 7 genes); RCTM Extracellular matrix organization (FDR = 0.0167, 6 genes); Keyword Proteoglycan (FDR = 0.0209, 3 genes); Component Basement membrane (FDR = 0.0233, 4 genes); Keyword Cleavage on pair of basic residues (FDR = 0.0322, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08796.1 (F2, CFB; 2/15); huMAP3_09832.1 (F2, CFB; 2/18); huMAP3_07701.1 (F2, CFB; 2/22); huMAP3_09273.1 (F2, CFB; 2/28); huMAP3_08395.1 (F2, CFB; 2/43); huMAP3_09531.1 (F2, CFB; 2/47); huMAP3_10101.1 (F2, CFB; 2/49); huMAP3_10678.1 (F2, CFB; 2/71)

### Novelty

The module should not be called wholly novel: several of its relationships and functional themes are already represented in STRING, and F2-CFB co-membership is repeatedly represented in hu.MAP. Its potentially new aspect is the cross-tissue co-abundance configuration that joins circulating coagulation or complement proteins with basement-membrane, matrix, adhesion and cardiac structural genes. However, the fact sheet does not provide an external replication cohort, perturbation experiment, disease comparison, or direct evidence that this exact module has not been reported. Therefore the appropriate conclusion is that this is a potentially novel tissue-pair co-abundance pattern built from substantially known biology, not a demonstrated new molecular complex or newly discovered pathway.

**Hypothesis.** Hypothesis: the shared module reflects a vascular or cardiac extracellular interface in which liver-derived circulating proteins enter the sample signal while locally expressed matrix and cytoskeletal proteins define the tissue context. F2 and CFB could provide protease and alternative-complement activity in the extracellular environment; VTN, FBN1, LUM, HSPG2 and LAMB2 could organize adhesive and basement-membrane interactions; and NRAP with PLEC could connect the extracellular context to cardiac muscle structural integrity. Coordinated abundance could therefore arise from remodeling, repair, vascular exposure, or changes in the relative contribution of plasma and matrix-rich tissue, rather than from direct physical assembly of all module members. This mechanism is a testable hypothesis, not an established causal model.

### Important genes

#### F2

- **Related proteins** (co-abundance neighbors): LAMB2 (0.91), FBN1 (0.85); STRING partners: AMBP (0.979)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08796.1, huMAP3_09832.1, huMAP3_07701.1, huMAP3_09273.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: coagulation factor II, thrombin. This gene encodes the prothrombin protein (also known as coagulation factor II). This protein is proteolytically cleaved in multiple steps to form the activated serine protease thrombin. The activated thrombin enzyme plays an important role in thrombosis and hemostasis by converting fibrinogen to fibrin during blood clot formation, by stimulating platelet aggregation, and by activating additional …
- **Diseases (Open Targets)**: congenital prothrombin deficiency (0.827); thrombophilia due to thrombin defect (0.738); venous thromboembolism (0.727); deep vein thrombosis (0.690); blood coagulation disease (0.670)
- **Europe PMC papers**: 109299
- **Why important**: F2 is central to the biological interpretation because it is a secreted-to-blood coagulation factor, has the strongest supplied literature volume, and participates in both primary terms (GO:CC Golgi lumen; q_global = 0.00317) and (GO:BP glial cell differentiation; q_global = 0.0354). It occupies the module's coagulation-facing connection to LAMB2 and FBN1 and has a very strong STRING relationship with AMBP. It is also present with CFB across the hu.MAP complexes (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) and has extensive disease associations involving prothrombin deficiency, thrombophilia and venous thromboembolism.
- **Conclusion**: Established evidence supports F2 as a circulating protease precursor linking hemostasis, extracellular signaling and the plasma context of this module. Its module membership does not establish that thrombin activity causes the co-abundance pattern; the plausible interpretation is that F2 is a major marker of the blood-facing component.

#### FBN1

- **Related proteins** (co-abundance neighbors): VTN (0.87), LAMB2 (0.86), F2 (0.85), AMBP (0.84); STRING partners: HSPG2 (0.849), LUM (0.972), VTN (0.806)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibrillin 1. This gene encodes a member of the fibrillin family of proteins. The encoded preproprotein is proteolytically processed to generate two proteins including the extracellular matrix component fibrillin-1 and the protein hormone asprosin. Fibrillin-1 is an extracellular matrix glycoprotein that serves as a structural component of calcium-binding microfibrils. These microfibrils provide force-bearing s…
- **Diseases (Open Targets)**: Marfan syndrome (0.892); ectopia lentis 1, isolated, autosomal dominant (0.811); Acromicric dysplasia (0.802); geleophysic dysplasia 2 (0.802); stiff skin syndrome (0.799)
- **Europe PMC papers**: 9216
- **Why important**: FBN1 has the strongest network position in the supplied module and connects VTN, LAMB2, F2 and AMBP. It is a structural extracellular-matrix glycoprotein forming calcium-binding microfibrils and is linked by STRING to HSPG2, LUM and VTN. Its tissue and single-cell annotations point to adipose, placenta, fibroblasts and hepatic stellate cells, and its extensive disease literature includes Marfan syndrome and related connective-tissue disorders.
- **Conclusion**: Established evidence supports FBN1 as a matrix scaffold and a key bridge between circulating proteins and matrix proteins. A role in organizing the specific shared heart-circulatory module is a reasonable hypothesis, but the co-abundance data alone do not demonstrate direct regulation or disease-specific remodeling.

#### HSPG2

- **Related proteins** (co-abundance neighbors): CFB (0.86); STRING partners: FBN1 (0.849), LUM (0.78), VTN (0.797)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 is a secreted extracellular-matrix proteoglycan with blood-vessel tissue enhancement and heart protein detection. It participates in the primary Golgi-lumen term (GO:CC Golgi lumen; q_global = 0.00317) and in numerous supplementary matrix, basement-membrane and proteoglycan terms (11 supplementary STRING terms; within-query FDR 0.00028–0.0233). Its STRING links to FBN1, LUM and VTN place it in the matrix-centered portion of the network, while its disease associations include Schwartz-Jampel syndrome, dyssegmental dysplasia and atrial fibrillation.
- **Conclusion**: Established evidence supports HSPG2 as a basement-membrane and matrix-interface component that can connect vascular or cardiac structure with adhesive extracellular proteins. Its position supports a structural interpretation, but does not prove that HSPG2 is the driver of the module or of the reported disease associations.

#### LAMB2

- **Related proteins** (co-abundance neighbors): F2 (0.91), FBN1 (0.86), CFB (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit beta 2. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: LAMB2-related infantile-onset nephrotic syndrome (0.808); Pierson syndrome (0.797); nephrotic syndrome (0.496); eye disorder (0.434); synaptic congenital myasthenic syndrome (0.381)
- **Europe PMC papers**: 2504
- **Why important**: LAMB2 is one of the module's links to basement-membrane biology and is the only selected gene besides F2, PLEC and VTN contributing to (GO:BP glial cell differentiation; q_global = 0.0354). It connects F2, FBN1 and CFB in the co-abundance network, is secreted to extracellular matrix, and has cell-type enhancement in vascular smooth muscle and lymphatic endothelial cells. Its established disease associations include Pierson syndrome and nephrotic syndrome, and its functional annotations include adhesion, basement-membrane organization and muscle differentiation.
- **Conclusion**: Established evidence supports LAMB2 as a plausible vascular and tissue-structural anchor of the module. Its connection to circulating factors suggests an interface rather than a purely intracellular cardiac program; whether this reflects matrix remodeling or sample composition requires independent tissue-resolved validation.

#### NRAP

- **Related proteins** (co-abundance neighbors): AMBP (0.89), PLEC (0.89); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Intermediate filaments; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nebulin related anchoring protein. Predicted to enable actin filament binding activity and muscle alpha-actinin binding activity. Predicted to be involved in cardiac muscle thin filament assembly. Predicted to be located in fascia adherens; muscle tendon junction; and myofibril. Predicted to be active in Z disc. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dilated cardiomyopathy (0.546); smoking initiation (0.418); atrial fibrillation (0.417); Abnormality of the cardiovascular system (0.409); smoking behavior (0.291)
- **Europe PMC papers**: 579
- **Why important**: NRAP is the most specifically cardiac-muscle-oriented selected gene in the supplied evidence. HPA places it in cardiomyocytes and myonuclei, detects it in heart, and assigns it to intermediate filaments, while the gene annotation links it to cardiac thin-filament assembly and the myofibril. It connects AMBP and PLEC, and its disease associations include dilated cardiomyopathy and atrial fibrillation.
- **Conclusion**: Established evidence supports NRAP as a cardiac structural marker that makes the module more than a generic plasma-protein signature. Its limited network connectivity and lack of STRING or hu.MAP support mean that its proposed bridge between cardiac architecture and the secreted matrix remains a hypothesis.

#### VTN

- **Related proteins** (co-abundance neighbors): FBN1 (0.87); STRING partners: AMBP (0.737), FBN1 (0.806), HSPG2 (0.797)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vitronectin. The protein encoded by this gene functions in part as an adhesive glycoprotein. Differential expression of this protein can promote either cell adhesion or migration as it links cells to the extracellular matrix through a variety of ligands. These ligands include integrins, plasminogen activator inhibitor-1, and urokinase plasminogen activator receptor. This secreted protein can be present in the …
- **Diseases (Open Targets)**: hypertensive disorder (0.421); dengue disease (0.376); neurodegenerative disease (0.343); temporal arteritis (0.338); age-related macular degeneration (0.313)
- **Europe PMC papers**: 3940
- **Why important**: VTN is a liver-enriched secreted-to-blood adhesive glycoprotein and contributes to both primary terms (GO:CC Golgi lumen; q_global = 0.00317) and (GO:BP glial cell differentiation; q_global = 0.0354). It connects to FBN1 in the module and to AMBP, FBN1 and HSPG2 in STRING. Its functions include cell adhesion, cell-matrix adhesion and integrin-mediated signaling, and its disease associations span vascular and inflammatory conditions. Its substantial literature volume makes it a well-characterized marker of the adhesive extracellular environment.
- **Conclusion**: Established evidence supports VTN as a circulating-to-matrix interface molecule that helps explain the module's shared plasma and extracellular-matrix signal. The data support its use as an interpretive anchor, but do not show that VTN-mediated adhesion drives the co-abundance module.

## Module 3

**Tissue pair**: circulatory_system and heart  
**Genes (11)**: APOB, TGFBI, COL6A3, GPS1, DSG2, F13A1, AGL, ITIH1, SVIL, TNXB, XIRP1

### Function

This module appears to combine extracellular-matrix and circulating-protein biology with striated-muscle structural and metabolic biology. The central extracellular-matrix signal is represented by TNXB, COL6A3, TGFBI, and ITIH1, which are associated with matrix organization, collagen-related biology, hyaluronan interaction, and cell adhesion. APOB and F13A1 add lipid-transport and coagulation-related biology, while XIRP1, SVIL, DSG2, and AGL represent actin organization, muscle structure, cell junctions, and glycogen metabolism. The network therefore does not support a single sharply defined pathway; it is more consistent with coordinated abundance of extracellular, vascular or circulating proteins together with cardiac and skeletal-muscle structural proteins. No GO or KEGG term passed global correction. There was also no supplementary STRING functional enrichment. The inferred function is consequently a cautious synthesis of gene annotations and network structure rather than a globally significant pathway assignment.

**Cell composition.** The module is compositionally mixed, but secreted and extracellular proteins are prominent. ITIH1, APOB, TGFBI, F13A1, TNXB, and COL6A3 are secreted to blood or extracellular matrix according to HPA, so the shared signal may reflect circulating protein abundance, extracellular matrix remodeling, vascular or stromal material, or sample composition rather than a coordinated intracellular program in cardiomyocytes. APOB is enriched in liver and intestine, and ITIH1 is liver-enriched, whereas XIRP1 and AGL are associated with heart or skeletal muscle and DSG2 and SVIL are detected in heart. HPA also shows enrichment in several stromal, hepatic, myeloid, platelet, and muscle-related cell types. Some genes have monocyte, dendritic-cell, macrophage, platelet, basophil, or neutrophil associations, but the module is not uniformly blood-cell enriched because several genes are not detected in immune cells and others have low immune-cell specificity. The shared circulatory-system and heart pattern should therefore be interpreted with particular attention to plasma carryover, vascular or stromal content, and shared muscle or connective-tissue cell types.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

At the specified STRING confidence threshold, none of the possible gene-pair relationships in this module is represented as a known STRING interaction, and STRING reports no supplementary functional enrichment. No hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not corroborated by the examined curated protein-interaction or complex resources. The strongest module structure is instead an abundance-correlation pattern: TNXB connects the extracellular-matrix and circulating-protein component, while XIRP1 connects muscle-associated structural genes including SVIL, GPS1, and AGL; DSG2 and AGL provide additional links between junctional and muscle-related biology. These edges should not be interpreted as direct physical interactions without independent validation.

**STRING interactions (score >= 0.7)**: 0 of 55 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported tissue-pair co-abundance pattern, but it cannot be claimed as a new molecular mechanism. Its apparent novelty is supported only in the limited sense that the module has no matching STRING interactions, no multi-member hu.MAP complex, and no established enrichment signature in the supplied resources. Absence from those resources alone does not prove novelty. The mixed composition, strong representation of secreted proteins, liver- and intestine-associated genes, extracellular-matrix proteins, and muscle proteins provides an alternative explanation involving sample composition or coordinated tissue abundance. The most defensible conclusion is that this is a novel candidate co-abundance association requiring replication, cell-composition adjustment, and orthogonal molecular validation.

**Hypothesis.** Hypothesis: the shared module reflects a blood-facing cardiac tissue environment in which circulating liver- and intestine-derived proteins, coagulation-related proteins, extracellular-matrix components, and cardiac or skeletal-muscle structural proteins vary together across samples. TNXB, COL6A3, and TGFBI could represent matrix remodeling or matrix-cell interaction, while ITIH1, APOB, and F13A1 could represent circulating or vascular contributions. In parallel, XIRP1, SVIL, DSG2, and AGL could reflect preservation of striated-muscle architecture, cell junctions, and glycogen handling. The observed cross-tissue co-abundance could therefore arise from a combination of extracellular-matrix remodeling and variable abundance of blood, stromal, and muscle-derived material, rather than from one unified intracellular signaling pathway. This hypothesis should be tested using cell-deconvolved expression, matched plasma measurements, protein-level validation, and independent heart and circulatory-system cohorts.

### Important genes

#### TNXB

- **Related proteins** (co-abundance neighbors): ITIH1 (0.94), TGFBI (0.90), APOB (0.89), F13A1 (0.89), COL6A3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tenascin XB. This gene encodes a member of the tenascin family of extracellular matrix glycoproteins. The tenascins have anti-adhesive effects, as opposed to fibronectin which is adhesive. This protein is thought to function in matrix maturation during wound healing, and its deficiency has been associated with the connective tissue disorder Ehlers-Danlos syndrome. This gene localizes to the major histocompatib…
- **Diseases (Open Targets)**: Ehlers-Danlos syndrome due to tenascin-X deficiency (0.795); vesicoureteral reflux 8 (0.703); Abnormality of the cardiovascular system (0.550); Ehlers-Danlos syndrome (0.522); hereditary disease (0.390)
- **Europe PMC papers**: 2382
- **Why important**: TNXB is the most connected module gene and links the principal extracellular-matrix and circulating-protein component to ITIH1, TGFBI, APOB, F13A1, and COL6A3. It encodes an extracellular-matrix glycoprotein with anti-adhesive effects and a proposed role in matrix maturation during wound healing. Its association with tenascin-X deficiency and Ehlers-Danlos syndrome makes it clinically relevant to connective-tissue and cardiovascular phenotypes. It is also one of the more extensively studied genes in the module.
- **Conclusion**: Established evidence supports TNXB as a structural extracellular-matrix hub and a plausible marker of connective-tissue biology in this module. Its network centrality supports an organizing role in the co-abundance pattern, but the lack of STRING and hu.MAP support means that a direct physical interaction network is not established. A mechanistic role for TNXB in coordinating the other module proteins remains a hypothesis.

#### APOB

- **Related proteins** (co-abundance neighbors): ITIH1 (0.94), TNXB (0.89), DSG2 (0.87); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Vesicles, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein B. This gene product is the main apolipoprotein of chylomicrons and low density lipoproteins (LDL), and is the ligand for the LDL receptor. It occurs in plasma as two main isoforms, apoB-48 and apoB-100: the former is synthesized exclusively in the gut and the latter in the liver. The intestinal and the hepatic forms of apoB are encoded by a single gene from a single, very long mRNA. The two isoforms…
- **Diseases (Open Targets)**: hypercholesterolemia, autosomal dominant, type B (0.814); Hypercholesterolemia (0.812); familial hypobetalipoproteinemia 1 (0.803); familial hypercholesterolemia (0.780); metabolic disease (0.729)
- **Europe PMC papers**: 28452
- **Why important**: APOB connects the extracellular and hepatic or intestinal component to ITIH1, TNXB, and DSG2. It is the principal apolipoprotein of chylomicrons and LDL and mediates lipid transport through the LDL receptor. Its strong disease associations with hypercholesterolemia and familial lipoprotein disorders make it an important physiological and clinical anchor. Its liver and intestine enrichment and secretion to blood also make it especially informative for assessing plasma contribution or sample-composition effects.
- **Conclusion**: Established evidence supports APOB as a circulating lipid-transport protein and a likely indicator of liver, intestine, or plasma-derived material in the module. Its co-abundance with cardiac and matrix genes does not establish a direct APOB role in cardiac structural regulation. The shared pattern may instead reflect vascular exposure or variable blood-derived protein abundance.

#### XIRP1

- **Related proteins** (co-abundance neighbors): SVIL (0.89), GPS1 (0.85), AGL (0.81); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Actin filaments; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: xin actin binding repeat containing 1. The protein encoded by this gene is a striated muscle protein and belongs to the Xin actin-binding repeat-containing protein (XIRP) family. The protein functions to protect actin filaments during depolymerization. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2017].
- **Diseases (Open Targets)**: response to stimulus (0.273); Follicular Cyst (0.270); Rare familial disorder with hypertrophic cardiomyopathy (0.094); hypertrophic cardiomyopathy (0.094); left ventricular noncompaction (0.091)
- **Europe PMC papers**: 441
- **Why important**: XIRP1 is the central gene in the muscle-associated branch, connecting SVIL, GPS1, and AGL. It is a striated-muscle protein that protects actin filaments during depolymerization and is enriched in heart and skeletal muscle, with protein detected in heart. Its annotations include actin organization and muscle regeneration, and it has disease associations with hypertrophic cardiomyopathy and left ventricular noncompaction. Its literature volume is more limited than that of APOB or the major matrix genes, which makes the module context potentially valuable.
- **Conclusion**: Established evidence supports XIRP1 as a cardiac and striated-muscle cytoskeletal component. Its position suggests that the muscle branch is biologically meaningful, although the absence of curated interaction or complex support prevents claiming a validated multi-protein complex. A coordinated relationship between XIRP1 abundance and matrix or circulating proteins is a testable hypothesis rather than an established mechanism.

#### DSG2

- **Related proteins** (co-abundance neighbors): APOB (0.87), ITIH1 (0.83), AGL (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cell Junctions; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: desmoglein 2. This gene encodes a member of the desmoglein family and cadherin cell adhesion molecule superfamily of proteins. Desmogleins are calcium-binding transmembrane glycoprotein components of desmosomes, cell-cell junctions between epithelial, myocardial, and other cell types. The encoded preproprotein is proteolytically processed to generate the mature glycoprotein. This gene is present in a gene clust…
- **Diseases (Open Targets)**: arrhythmogenic right ventricular dysplasia 10 (0.812); arrhythmogenic right ventricular cardiomyopathy (0.781); dilated cardiomyopathy 1BB (0.714); familial isolated dilated cardiomyopathy (0.615); Abnormality of the cardiovascular system (0.552)
- **Europe PMC papers**: 3811
- **Why important**: DSG2 links APOB and ITIH1 to AGL and is detected in heart. It encodes a desmosomal cadherin involved in myocardial and epithelial cell-cell junctions, desmosome assembly, and adhesion. Its disease associations include arrhythmogenic right ventricular cardiomyopathy and dilated cardiomyopathy, giving it direct relevance to cardiac tissue integrity. Its network position makes it a bridge between the circulating or epithelial-associated part of the module and the muscle or glycogen-associated part.
- **Conclusion**: Established evidence supports DSG2 as a cardiac junctional protein with important cardiomyopathy associations. Its co-abundance with muscle and extracellular or circulating genes may indicate shared tissue integrity or sample-composition effects, but no direct molecular relationship among these proteins is established in the supplied interaction resources. Its bridging role is therefore an informative network observation and a mechanistic hypothesis.

#### ITIH1

- **Related proteins** (co-abundance neighbors): APOB (0.94), TNXB (0.94), COL6A3 (0.84), DSG2 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 1. This gene encodes a member of the inter-alpha-trypsin inhibitor family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the heavy chain of the inter-alpha-trypsin inhibitor complex, which is secreted by hepatocytes into the blood. The heavy chain also interacts with hyaluronan, and…
- **Diseases (Open Targets)**: osteoarthritis, hip (0.305); osteoarthritis (0.188); schizophrenia (0.185); major depressive disorder (0.183); psychiatric disorder (0.171)
- **Europe PMC papers**: 963
- **Why important**: ITIH1 is a highly connected extracellular or circulating component that links APOB and TNXB to COL6A3 and DSG2. It is secreted by hepatocytes into blood and interacts with hyaluronan, providing a plausible connection between liver-derived plasma proteins and extracellular-matrix biology. Its liver and hepatocyte enrichment supports a circulating or hepatic contribution to the shared module. Although its disease literature is less extensive than that of APOB, TNXB, or DSG2, its position is important for interpreting the module's composition.
- **Conclusion**: Established evidence supports ITIH1 as a hepatocyte-derived blood protein associated with hyaluronan-related extracellular biology. Its module position favors an interpretation involving circulating or matrix-associated abundance rather than a cardiac-specific intracellular pathway. Any proposed role for ITIH1 in cardiac remodeling or coordination with DSG2 and muscle proteins remains hypothetical.

## Module 5

**Tissue pair**: circulatory_system and heart  
**Genes (6)**: GPD2, ILK, NEXN, PPP1CB, RSU1, XPNPEP1

### Function

No GO or KEGG term passed global correction, and there are no supplementary STRING functional-enrichment terms. The module therefore does not support a single statistically established pathway-level annotation. Its gene composition instead suggests a mixed cellular program involving cell-matrix adhesion, integrin-linked signaling, actin-cytoskeleton organization, mitochondrial glycerol-phosphate metabolism, peptide processing, and serine-threonine dephosphorylation. The network is consistent with a structural and signaling interface between adhesion machinery and cellular metabolic or regulatory state, but this interpretation remains integrative rather than enrichment-established.

**Cell composition.** The module is not composed of plasma or secreted proteins; the HPA annotation reports no secreted genes. All module proteins are detected in heart tissue, while most have low tissue specificity, arguing against a purely heart-exclusive program. HPA repeatedly identifies platelets and megakaryocytes, with additional signals in smooth muscle cells, cardiomyocytes, neutrophil progenitors, and other hematopoietic or myeloid populations. NEXN is enhanced in heart and skeletal muscle, whereas several other genes show broad tissue distribution. Thus, the shared circulatory-system and heart module may partly reflect shared blood-derived or vascular-associated cell populations in the samples, in addition to a genuine cardiac structural signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING identifies a strong known relationship between ILK and RSU1, and no other STRING interaction among the module genes is reported at the stated confidence threshold. hu.MAP independently places ILK and RSU1 together in complexes (hu.MAP huMAP3_06647.1), (hu.MAP huMAP3_04827.1), (hu.MAP huMAP3_09385.1), and (hu.MAP huMAP3_11194.1), alongside LIMS proteins, PXN, PARV family proteins, and related adhesion-complex components. This convergence supports a real integrin-associated adhesion or cytoskeletal submodule centered on ILK and RSU1. The remaining genes are connected to the co-abundance network but lack supplied STRING or hu.MAP support, so their relationships should be regarded as expression-level associations rather than established physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: ILK–RSU1 (0.991)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06647.1 (ILK, RSU1; 2/6); huMAP3_04827.1 (ILK, RSU1; 2/7); huMAP3_09385.1 (ILK, RSU1; 2/8); huMAP3_11194.1 (ILK, RSU1; 2/10)

### Novelty

The module may represent a novel co-abundance combination in the circulatory-system and heart tissue pair, but the available evidence cannot establish that it is a new biological complex or pathway. The ILK–RSU1 relationship and their shared hu.MAP assignments are already known, which argues against novelty for that core interaction. Conversely, the links involving GPD2, XPNPEP1, NEXN, and PPP1CB are not represented in the supplied STRING or hu.MAP results, but absence from those resources does not prove novelty. The most defensible conclusion is that the tissue-pair co-abundance configuration is potentially novel and hypothesis-generating, while its adhesion-core component is established.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of an integrin-linked adhesion and cytoskeletal state in cardiac, vascular, platelet, or megakaryocyte-associated cells, with ILK and RSU1 forming the best-supported signaling scaffold. NEXN may connect this scaffold to actin organization and cardiac muscle architecture, while PPP1CB may tune adhesion or contractile signaling through dephosphorylation. GPD2 could reflect mitochondrial redox and glycerol-phosphate-shuttle activity, and XPNPEP1 could reflect peptide or signaling-mediator processing. A shared abundance program across heart and circulatory-system samples could therefore arise from a mixture of cardiac structural biology and shared blood or vascular cell composition; this should be tested with cell-resolved data, perturbation experiments, and direct interaction assays.

### Important genes

#### ILK

- **Related proteins** (co-abundance neighbors): RSU1 (0.87); STRING partners: RSU1 (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_06647.1, huMAP3_04827.1, huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: integrin linked kinase. This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastas…
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); familial hypertrophic cardiomyopathy (0.194); Abnormality of the cardiovascular system (0.148); Prolonged QT interval (0.118); neoplasm (0.118)
- **Europe PMC papers**: 8401
- **Why important**: ILK is the clearest network anchor for the established adhesion signal: it connects directly to RSU1 and appears with RSU1 in every reported hu.MAP complex, while HPA places it at focal adhesion sites and in platelet, megakaryocyte, and smooth-muscle cell contexts. Its annotation supports integrin-mediated signaling and cell-matrix adhesion, and it has the largest literature footprint in the module. Its cardiovascular and disease associations make it especially relevant to interpreting a heart-associated co-abundance program.
- **Conclusion**: Established evidence supports ILK as an integrin-linked adhesion and signaling component and as part of the known ILK–RSU1 complex context. It is plausible, but not demonstrated here, that ILK organizes the broader co-abundance module or couples cardiac and blood-cell signals.

#### RSU1

- **Related proteins** (co-abundance neighbors): ILK (0.87), GPD2 (0.85); STRING partners: ILK (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_06647.1, huMAP3_04827.1, huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: Ras suppressor protein 1. This gene encodes a protein that is involved in the Ras signal transduction pathway, growth inhibition, and nerve-growth factor induced differentiation processes, as determined in mouse and human cell line studies. In mouse, the encoded protein was initially isolated based on its ability to inhibit v-Ras transformation. Multiple alternatively spliced transcript variants for this gene have been rep…
- **Diseases (Open Targets)**: alcohol drinking (0.270); placental retention (0.266); obesity disorder (0.235); neurodegenerative disease (0.213); subarachnoid hemorrhage (0.211)
- **Europe PMC papers**: 614
- **Why important**: RSU1 is a central connector in the co-abundance graph, linking ILK to GPD2, and it is the partner of ILK in STRING and in all reported hu.MAP complexes. Its documented functions include Ras signaling, growth inhibition, cell-matrix adhesion, and signal transduction. HPA associates it with megakaryocytes and platelets and detects it in heart, making it a strong candidate for linking adhesion biology with the shared tissue context.
- **Conclusion**: Established evidence supports RSU1 as a component of the ILK-associated adhesion and signaling machinery. Its connection to GPD2 is a co-abundance observation rather than a demonstrated physical or metabolic interaction, so any role in coupling adhesion to mitochondrial metabolism remains a hypothesis.

#### NEXN

- **Related proteins** (co-abundance neighbors): PPP1CB (0.82), XPNPEP1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nexilin F-actin binding protein. This gene encodes a filamentous actin-binding protein that may function in cell adhesion and migration. Mutations in this gene have been associated with dilated cardiomyopathy, also known as CMD1CC. Alternatively spliced transcript variants have been described.[provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: dilated cardiomyopathy 1CC (0.792); hypertrophic cardiomyopathy 20 (0.746); familial isolated dilated cardiomyopathy (0.667); hypertrophic cardiomyopathy (0.584); cardiomyopathy, dilated, 2M (0.565)
- **Europe PMC papers**: 1090
- **Why important**: NEXN is the most tissue-specific cardiac and muscle-oriented gene in the module, with HPA enhancement in heart muscle and skeletal muscle and localization at the plasma membrane and actin filaments. It binds filamentous actin and is annotated for cell adhesion, migration, and cytoskeleton organization. Its established association with dilated and hypertrophic cardiomyopathy gives it direct disease relevance to the heart context, while its network links connect it to PPP1CB and XPNPEP1.
- **Conclusion**: Established evidence supports NEXN as a cardiac and muscle cytoskeletal factor with cardiomyopathy relevance. It may provide the cardiac structural arm of the module, but the supplied data do not establish that its co-abundance with PPP1CB or XPNPEP1 reflects a shared physical complex.

#### GPD2

- **Related proteins** (co-abundance neighbors): RSU1 (0.85), XPNPEP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycerol-3-phosphate dehydrogenase 2. The protein encoded by this gene localizes to the inner mitochondrial membrane and catalyzes the conversion of glycerol-3-phosphate to dihydroxyacetone phosphate, using FAD as a cofactor. Along with GDP1, the encoded protein constitutes the glycerol phosphate shuttle, which reoxidizes NADH formed during glycolysis. Two transcript variants encoding the same protein have been found for this gene.[pr…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.709); diabetes mellitus (0.597); obstructive sleep apnea syndrome (0.424); polycystic ovary syndrome (0.419); obesity disorder (0.415)
- **Europe PMC papers**: 1990
- **Why important**: GPD2 introduces a distinct mitochondrial metabolic component. It is a mitochondrial inner-membrane enzyme of the glycerol-phosphate shuttle and is linked to glycerol-phosphate metabolism and redox handling. HPA associates it with neutrophil progenitors and several myeloid cell types, while disease associations include diabetes and obesity. Its graph position between RSU1 and XPNPEP1 makes it a potentially informative bridge between the adhesion-associated and metabolic portions of the module.
- **Conclusion**: Established evidence supports GPD2 as a mitochondrial glycerol-phosphate-shuttle enzyme with metabolic and blood-cell expression associations. A role in coordinating metabolic state with the ILK–RSU1 adhesion axis is a hypothesis based on network placement, not a demonstrated mechanism.

#### XPNPEP1

- **Related proteins** (co-abundance neighbors): NEXN (0.82), GPD2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: X-prolyl aminopeptidase 1. This gene encodes the cytosolic form of a metalloaminopeptidase that catalyzes the cleavage of the N-terminal amino acid adjacent to a proline residue. The gene product may play a role in degradation and maturation of tachykinins, neuropeptides, and peptide hormones. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: preeclampsia (0.281); Hypercholesterolemia (0.257); bipolar disorder (0.251); bipolar I disorder (0.240); mathematical ability (0.212)
- **Europe PMC papers**: 4691
- **Why important**: XPNPEP1 connects NEXN and GPD2 in the co-abundance graph and encodes a cytosolic proline-specific aminopeptidase involved in peptide and peptide-hormone processing, including bradykinin catabolism. HPA detects it in heart and associates it with platelets and pancreatic acinar cells. Its substantial literature presence and links to vascular or metabolic disease make it relevant to a circulatory-system interpretation, even though it lacks supplied STRING or hu.MAP support within this module.
- **Conclusion**: Established evidence supports XPNPEP1 as a cytosolic peptide-processing enzyme with potential relevance to vasoactive peptide turnover. Its placement in this module may indicate coordinated cellular state or sample composition, but a direct role in cardiac adhesion or platelet-associated signaling is not established.
