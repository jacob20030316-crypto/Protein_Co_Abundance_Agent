# Conserved co-abundance modules: cerebrospinal_fluid and myometrium

## Module 0

**Tissue pair**: cerebrospinal_fluid and myometrium  
**Genes (5)**: SERPINA1, HP, IGHG1, IGHG2, IGHG3

### Function

The module is most consistent with a circulating humoral and acute-phase protein signal rather than a myometrium-intrinsic pathway. IGHG1, IGHG2, and IGHG3 indicate immunoglobulin constant-region abundance associated with plasma cells and B-cell populations, while HP and SERPINA1 represent secreted liver-derived proteins involved in hemoglobin handling, protease inhibition, and inflammatory or tissue-protective responses. No GO or KEGG term passed global correction, so this functional interpretation is based on the gene annotations, HPA evidence, network structure, STRING, and hu.MAP rather than significant pathway enrichment.

**Cell composition.** The module is strongly biased toward secreted or plasma-associated proteins: all genes have secretome evidence, with the immunoglobulin genes associated with plasma cells and B-cell populations and HP and SERPINA1 associated with liver or myeloid populations. HPA also links the module to lymphoid tissue, hepatocytes, monocytes, neutrophils, and related blood-cell populations. Protein detection was absent for the assessed myometrium entries, while the cerebrospinal-fluid tissue comparison had no matching HPA tissue data. The shared signal may therefore reflect circulating blood-derived proteins, plasma-cell or immune-cell contribution, or sample-fluid composition, rather than expression by myometrial smooth muscle. The immunoglobulin genes are not broadly housekeeping-type genes.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship, between HP and SERPINA1, supporting a known connection between two secreted acute-phase or protease-regulatory proteins. The remaining co-abundance relationships are not represented as high-confidence STRING interactions, so the network should not be interpreted as a fully established physical interaction complex. hu.MAP places HP and SERPINA1 together in complexes C1 through C8, but each complex contains many additional plasma, complement, coagulation, transport, and immune proteins, and the module contributes only this pair to those complexes. This supports shared membership in a broad circulating-protein context rather than a module-specific molecular complex.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: HP–SERPINA1 (0.961)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07432.1 (HP, SERPINA1; 2/18); huMAP3_07265.1 (HP, SERPINA1; 2/20); huMAP3_09434.1 (HP, SERPINA1; 2/33); huMAP3_08395.1 (HP, SERPINA1; 2/43); huMAP3_09531.1 (HP, SERPINA1; 2/47); huMAP3_10101.1 (HP, SERPINA1; 2/49); huMAP3_15040.1 (HP, SERPINA1; 2/64); huMAP3_10678.1 (HP, SERPINA1; 2/71)

### Novelty

The coordinated abundance pattern across cerebrospinal fluid and myometrium may be a new observation, because the exact cross-tissue module is not established by the supplied STRING or hu.MAP evidence and lacks a previously demonstrated complete interaction structure. However, the biology of its components is not novel: immunoglobulin constant genes, haptoglobin, and alpha-one antitrypsin are well-established circulating or immune-associated proteins. The strongest interpretation is therefore a potentially novel cross-tissue co-abundance pattern built from well-known blood, plasma-cell, liver, and inflammatory proteins. Absence from STRING or hu.MAP alone cannot establish novelty, and the possible blood or sample-composition explanation limits claims of a new tissue mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared circulating-protein or immune-fluid component present in both sample groups. Plasma-cell-derived immunoglobulin abundance may covary with liver- and myeloid-associated acute-phase proteins, including HP and SERPINA1, because of common blood contamination, vascular exposure, inflammation, or altered immune-cell representation. A secondary hypothesis is that local inflammatory conditions could increase vascular permeability or immune-cell contribution in both tissues, but the supplied data do not distinguish this from passive carryover of circulating proteins. This hypothesis should be tested with cell-deconvolution markers, blood contamination controls, independent protein measurements, and tissue-localized assays.

### Important genes

#### HP

- **Related proteins** (co-abundance neighbors): IGHG1 (0.90), IGHG2 (0.87), SERPINA1 (0.85); STRING partners: SERPINA1 (0.961)
- **HPA**: Tissue enriched; Cell type enriched; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: haptoglobin. This gene encodes a preproprotein, which is processed to yield both alpha and beta chains, which subsequently combine as a tetramer to produce haptoglobin. Haptoglobin functions to bind free plasma hemoglobin, which allows degradative enzymes to gain access to the hemoglobin, while at the same time preventing loss of iron through the kidneys and protecting the kidneys from damage by hemoglobin. Mu…
- **Diseases (Open Targets)**: Hypercholesterolemia (0.581); coronary artery disorder (0.572); metabolic disease (0.571); hyperlipidemia (0.567); metabolic syndrome (0.516)
- **Europe PMC papers**: 125817
- **Why important**: HP is a hub-like connector in the module and is the most strongly supported physical relationship, pairing with SERPINA1 in STRING and recurring with SERPINA1 across hu.MAP complexes C1 through C8. It is liver-enriched, secreted to blood, and annotated for hemoglobin binding, defense and inflammatory responses, and protection from oxidative injury. It also has extensive literature and disease associations involving metabolic and cardiovascular disorders, making it a strong anchor for a circulating acute-phase interpretation.
- **Conclusion**: Established evidence supports HP as a secreted liver-derived acute-phase and hemoglobin-scavenging protein that links the module to blood composition and inflammatory biology. It is plausible as a central marker of the module, but the data do not establish HP production by myometrium or a causal role in the shared co-abundance pattern.

#### SERPINA1

- **Related proteins** (co-abundance neighbors): IGHG1 (0.87), IGHG2 (0.86), HP (0.85); STRING partners: HP (0.961)
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: serpin family A member 1. The protein encoded by this gene is a serine protease inhibitor belonging to the serpin superfamily whose targets include elastase, plasmin, thrombin, trypsin, chymotrypsin, and plasminogen activator. This protein is produced in the liver, the bone marrow, by lymphocytic and monocytic cells in lymphoid tissue, and by the Paneth cells of the gut. Defects in this gene are associated with chronic obs…
- **Diseases (Open Targets)**: alpha 1-antitrypsin deficiency (0.768); chronic obstructive pulmonary disease (0.690); cirrhosis of liver (0.573); cholelithiasis (0.569); pulmonary emphysema (0.569)
- **Europe PMC papers**: 6526
- **Why important**: SERPINA1 is a hub-like connector with HP and the immunoglobulin genes, is the only other module member supported by a high-confidence STRING relationship, and occurs with HP in hu.MAP complexes C1 through C8. It is secreted to blood, associated with liver and several absorptive or myeloid cell types, and inhibits multiple serine proteases. Its extensive literature and strong disease associations, including alpha-one antitrypsin deficiency, chronic obstructive pulmonary disease, emphysema, and liver disease, make it important for interpreting protease control and inflammation.
- **Conclusion**: Established evidence supports SERPINA1 as a circulating protease inhibitor with liver, myeloid, and inflammatory relevance. It likely marks the same blood-derived or acute-phase component as HP, but the module does not demonstrate that SERPINA1 mediates a tissue-specific mechanism in either cerebrospinal fluid or myometrium.

#### IGHG1

- **Related proteins** (co-abundance neighbors): IGHG2 (0.93), HP (0.90), SERPINA1 (0.87); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: immunoglobulin heavy constant gamma 1 (G1m marker)
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 3057
- **Why important**: IGHG1 is one of the better-connected module genes and is associated by HPA with plasma cells, memory B cells, and lymphoid tissue. Its immunoglobulin secretome annotation identifies a humoral immune component that complements the acute-phase proteins. It has a substantial literature base, although the module data provide no specific antigen or immune pathway assignment.
- **Conclusion**: Established evidence supports IGHG1 as an immunoglobulin heavy constant-region gene marking antibody-producing or B-cell-related material. In this module it is more likely an indicator of plasma-cell or circulating antibody abundance than evidence for a novel IGHG1-specific function in myometrium.

#### IGHG2

- **Related proteins** (co-abundance neighbors): IGHG1 (0.93), HP (0.87), SERPINA1 (0.86), IGHG3 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: immunoglobulin heavy constant gamma 2 (G2m marker)
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 1063
- **Why important**: IGHG2 has the strongest network connectivity in the module and connects the immunoglobulin group with HP and SERPINA1. HPA associates it with plasma cells, memory B cells, naive B cells, and lymphoid tissue, while its secretome annotation supports a circulating antibody signal. Its literature is substantial and its position makes it a useful bridge between the humoral and acute-phase portions of the module.
- **Conclusion**: Established evidence supports IGHG2 as a marker of immunoglobulin-producing cell or antibody abundance. Its network position suggests coordinated variation with HP and SERPINA1, but does not show that IGHG2 physically interacts with them or drives the module.

#### IGHG3

- **Related proteins** (co-abundance neighbors): IGHG2 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: immunoglobulin heavy constant gamma 3 (G3m marker)
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 2659
- **Why important**: IGHG3 is the more peripheral immunoglobulin member, connected to IGHG2, and is associated with plasma cells, memory B cells, naive B cells, and lymphoid tissue. Its presence reinforces the interpretation that the module contains a humoral immune or antibody-abundance component rather than a generic intracellular program. It also has a substantial literature base despite lacking STRING partners or hu.MAP assignment in the supplied evidence.
- **Conclusion**: Established evidence supports IGHG3 as an immunoglobulin constant-region marker of plasma-cell or B-cell-associated material. Its peripheral position makes it supportive rather than central to the module mechanism, and no direct interaction or tissue-specific causal role is demonstrated.

## Module 1

**Tissue pair**: cerebrospinal_fluid and myometrium  
**Genes (5)**: SERPINF2, APOB, C5, SERPIND1, PON1

### Function

The module is most consistent with a circulating liver-derived plasma-protein program combining lipid transport and protection from lipid oxidation with complement, coagulation, and fibrinolysis regulation. APOB and PON1 support lipid transport, cholesterol handling, and protection against plasma lipoprotein oxidation. C5 supports innate immune complement activity, while SERPIND1 and SERPINF2 support regulation of thrombin, plasmin, fibrin turnover, and related proteolytic processes. No GO or KEGG term passed global correction, so this functional interpretation is based on the individual gene annotations, network structure, tissue expression, and protein-complex evidence rather than significant pathway enrichment.

**Cell composition.** All genes are annotated as secreted to blood, and the HPA evidence points predominantly to liver and hepatocytes rather than to myometrium or immune cells. APOB also has intestine and enterocyte enrichment, while SERPINF2 has proximal-tubule and plasmacytoid-DC associations. The module proteins were not detected by immunohistochemistry in myometrium. This strongly suggests that the shared cerebrospinal-fluid and myometrium co-abundance signal may reflect circulating plasma proteins, vascular exposure, or shared sample-associated blood components rather than expression by myometrial cells. The pattern is not that of a broadly expressed housekeeping module. The blood-cell evidence is limited because most genes were not detected as immune-cell enriched, although SERPINF2 has plasmacytoid-DC enrichment.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports one particularly strong known relationship, APOB-PON1, consistent with association between lipoprotein biology and paraoxonase activity. The absence of additional high-confidence STRING edges means that most links in the co-abundance network are not established direct physical interactions in STRING. hu.MAP provides partially overlapping complexes: C5 with SERPINF2 occurs in (hu.MAP huMAP3_07119.1) and (hu.MAP huMAP3_00178.1), while C5 with SERPIND1 occurs in (hu.MAP huMAP3_08224.1), (hu.MAP huMAP3_09434.1), and (hu.MAP huMAP3_10678.1). These complexes contain many additional plasma, complement, coagulation, and lipoprotein proteins, so they support a shared extracellular-plasma context but do not establish that all module members form one molecular complex. Overall, the network is better interpreted as coordinated abundance of related circulating proteins than as a demonstrated intracellular complex.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: APOB–PON1 (0.952)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07119.1 (C5, SERPINF2; 2/6); huMAP3_00178.1 (C5, SERPINF2; 2/9); huMAP3_08224.1 (C5, SERPIND1; 2/21); huMAP3_09434.1 (C5, SERPIND1; 2/33); huMAP3_10678.1 (C5, SERPIND1; 2/71)

### Novelty

The individual biology of these proteins is well established, and the APOB-PON1 relationship plus the hu.MAP overlaps show that the module is not composed of previously unconnected molecules. The potentially new observation is their coordinated co-abundance across cerebrospinal fluid and myometrium. However, the available evidence does not establish a new tissue-specific mechanism, and the strong liver and blood-secreted signature raises the alternative explanation of shared circulating-protein carryover or vascular exposure. Therefore this should be described as a potentially novel cross-tissue co-abundance pattern, not as a newly discovered molecular pathway. Absence of broader STRING support or a complete hu.MAP complex does not by itself prove novelty.

**Hypothesis.** Hypothesis: variation in the abundance of liver-derived plasma proteins entering or being sampled from cerebrospinal fluid and myometrium produces a coordinated module linking lipoprotein handling, oxidative protection, complement activation, and control of coagulation and fibrinolysis. PON1 and APOB may define the lipid-associated component, whereas C5, SERPIND1, and SERPINF2 may represent inflammatory and protease-regulatory components. This hypothesis predicts that the module will track circulating protein exposure or vascular permeability more strongly than local myometrial transcription. It remains a hypothesis because the fact sheet does not demonstrate local production, causal regulation, or direct physical interaction among all members.

### Important genes

#### PON1

- **Related proteins** (co-abundance neighbors): C5 (0.93), APOB (0.85), SERPINF2 (0.84), SERPIND1 (0.83); STRING partners: APOB (0.952)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: paraoxonase 1. This gene encodes a member of the paraoxonase family of enzymes and exhibits lactonase and ester hydrolase activity. Following synthesis in the kidney and liver, the enzyme is secreted into the circulation, where it binds to high density lipoprotein (HDL) particles and hydrolyzes thiolactones and xenobiotics, including paraoxon, a metabolite of the insecticide parathion. Polymorphisms in this gene…
- **Diseases (Open Targets)**: diabetic retinopathy (0.377); atopic eczema (0.354); obesity disorder (0.306); idiopathic pulmonary fibrosis (0.202); malunion fracture (0.148)
- **Europe PMC papers**: 5619
- **Why important**: PON1 has the strongest network connectivity and links the lipid-associated APOB branch with the complement and protease-regulatory genes. It is a liver- and hepatocyte-enriched secreted blood protein, and its established lactonase and ester-hydrolase activities, cholesterol-efflux association, and protection against lipoprotein oxidation make it a plausible biochemical bridge. It also has substantial literature coverage and disease associations including diabetic retinopathy, atopic eczema, obesity disorder, and idiopathic pulmonary fibrosis.
- **Conclusion**: Established evidence supports PON1 as a circulating liver-derived enzyme associated with HDL, lipid handling, and protection from lipoprotein oxidation. Its central network position makes it an important module marker. It is plausible, but not demonstrated, that PON1 coordinates the module's lipid and inflammatory dimensions.

#### C5

- **Related proteins** (co-abundance neighbors): PON1 (0.93), SERPIND1 (0.87), APOB (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07119.1, huMAP3_00178.1, huMAP3_08224.1, huMAP3_09434.1, huMAP3_10678.1
- **Function (MyGene.info)**: complement C5. This gene encodes a component of the complement system, a part of the innate immune system that plays an important role in inflammation, host homeostasis, and host defense against pathogens. The encoded preproprotein is proteolytically processed to generate multiple protein products, including the C5 alpha chain, C5 beta chain, C5a anaphylatoxin and C5b. The C5 protein is comprised of the C5 alpha…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.744); paroxysmal nocturnal hemoglobinuria (0.610); myasthenia gravis (0.586); atypical hemolytic-uremic syndrome (0.544); neuromyelitis optica (0.516)
- **Europe PMC papers**: 81450
- **Why important**: C5 is a central network member connected with PON1, APOB, and SERPIND1, and it is represented with SERPINF2 or SERPIND1 in several hu.MAP complexes. Its complement annotations and very large literature base identify it as the principal innate-inflammatory component. Its disease associations include complement deficiency, paroxysmal nocturnal hemoglobinuria, myasthenia gravis, atypical hemolytic-uremic syndrome, and neuromyelitis optica.
- **Conclusion**: Established evidence supports C5 as a major complement and inflammatory plasma protein with clinically important roles in host defense and immune-mediated disease. In this module it may indicate coordinated inflammatory or vascular-protease biology, but the co-abundance data do not prove complement activation in either tissue.

#### APOB

- **Related proteins** (co-abundance neighbors): PON1 (0.85), C5 (0.82); STRING partners: PON1 (0.952)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Vesicles, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein B. This gene product is the main apolipoprotein of chylomicrons and low density lipoproteins (LDL), and is the ligand for the LDL receptor. It occurs in plasma as two main isoforms, apoB-48 and apoB-100: the former is synthesized exclusively in the gut and the latter in the liver. The intestinal and the hepatic forms of apoB are encoded by a single gene from a single, very long mRNA. The two isoforms…
- **Diseases (Open Targets)**: hypercholesterolemia, autosomal dominant, type B (0.814); Hypercholesterolemia (0.812); familial hypobetalipoproteinemia 1 (0.803); familial hypercholesterolemia (0.780); metabolic disease (0.729)
- **Europe PMC papers**: 28452
- **Why important**: APOB is connected to PON1 and C5 and is the module's clearest lipoprotein transport component. Its liver and intestine group enrichment, hepatocyte and enterocyte associations, secretion to blood, and established role as the structural apolipoprotein of chylomicrons and LDL support a circulating lipid-transport interpretation. It has extensive literature coverage and strong disease associations with hypercholesterolemia, familial hypercholesterolemia, and familial hypobetalipoproteinemia.
- **Conclusion**: Established evidence supports APOB as a major carrier of circulating lipids and a marker of hepatic or intestinal lipoprotein production. Its relationship with PON1 is supported by STRING. It may anchor the module's plasma-lipoprotein component, but the data do not show that APOB directly regulates the other module proteins.

#### SERPIND1

- **Related proteins** (co-abundance neighbors): C5 (0.87), PON1 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08224.1, huMAP3_09434.1, huMAP3_10678.1
- **Function (MyGene.info)**: serpin family D member 1. This gene belongs to the serpin gene superfamily. Serpins play roles in many processes including inflammation, blood clotting, and cancer metastasis. Members of this family have highly conserved secondary structures with a reactive center loop that interacts with the protease active site to inhibit protease activity. This gene encodes a plasma serine protease that functions as a thrombin and chymo…
- **Diseases (Open Targets)**: heparin cofactor 2 deficiency (0.721); Venous thrombosis (0.670); hemorrhage (0.266); neurodegenerative disease (0.265); thrombotic disease (0.120)
- **Europe PMC papers**: 1066
- **Why important**: SERPIND1 connects with C5 and PON1 and appears with C5 across several hu.MAP complexes containing broad coagulation, complement, and plasma-protein membership. It is a liver- and hepatocyte-enriched secreted protein located in vesicles and encodes a heparin-activated thrombin and chymotrypsin inhibitor. Its disease associations include heparin cofactor deficiency, venous thrombosis, hemorrhage, and thrombotic disease.
- **Conclusion**: Established evidence supports SERPIND1 as a regulator of plasma proteases and blood coagulation. Its network placement suggests that coagulation control is part of the module's circulating-protein context. A specific role for SERPIND1 in linking coagulation to complement or lipid oxidation in these tissues remains hypothetical.

#### SERPINF2

- **Related proteins** (co-abundance neighbors): PON1 (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enriched; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07119.1, huMAP3_00178.1
- **Function (MyGene.info)**: serpin family F member 2. This gene encodes a member of the serpin family of serine protease inhibitors. The protein is a major inhibitor of plasmin, which degrades fibrin and various other proteins. Consequently, the proper function of this gene has a major role in regulating the blood clotting pathway. Mutations in this gene result in alpha-2-plasmin inhibitor deficiency, which is characterized by severe hemorrhagic diat…
- **Diseases (Open Targets)**: alpha-2-plasmin inhibitor deficiency (0.666); chronic kidney disease (0.452); Alzheimer disease (0.413); dementia (0.402); Abnormal bleeding (0.371)
- **Europe PMC papers**: 1441
- **Why important**: SERPINF2 is the terminal network member connected to PON1 and is paired with C5 in (hu.MAP huMAP3_07119.1) and (hu.MAP huMAP3_00178.1). It is secreted to blood, belongs to the serpin family, and is a major inhibitor of plasmin, giving it a direct role in fibrinolysis and regulation of fibrin turnover. Its disease associations include alpha-two-plasmin inhibitor deficiency, abnormal bleeding, chronic kidney disease, Alzheimer disease, and dementia.
- **Conclusion**: Established evidence supports SERPINF2 as a plasma inhibitor that restrains plasmin-mediated fibrinolysis. Its inclusion reinforces a coagulation and extracellular-proteolysis interpretation. The observed module does not establish whether SERPINF2 is locally relevant to cerebrospinal fluid or myometrium, or whether it is simply a shared circulating constituent.

