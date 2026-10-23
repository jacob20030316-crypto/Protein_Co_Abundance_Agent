# Conserved co-abundance modules: cerebrospinal_fluid and heart

## Module 0

**Tissue pair**: cerebrospinal_fluid and heart  
**Genes (5)**: HSPA5, CLIC1, VCAN, FN1, LAMA4

### Function

The module is most consistent with an extracellular-matrix and vascular basement-membrane program, centered on adhesion, matrix organization, cell migration, tissue morphogenesis, and vascular or cardiac structural biology. This interpretation is based on VCAN, LAMA4, and FN1 annotations and on the direct STRING-supported links connecting FN1 with LAMA4 and VCAN. HSPA5 adds an endoplasmic-reticulum proteostasis and stress-response component, while CLIC1 is compatible with cellular transport, redox regulation, and platelet-related biology. No GO or KEGG term passed global correction, so there is no globally significant pathway annotation to report. The absence of an enriched term does not invalidate the coherent extracellular-matrix interpretation, but it makes that interpretation dependent mainly on gene-level annotations and network structure.

**Cell composition.** The module is strongly compatible with extracellular and circulating protein biology: most members are secreted, extracellular-matrix, or secreted-to-blood proteins. FN1 is a soluble plasma protein and an extracellular-matrix component, VCAN is a secreted proteoglycan, and LAMA4 is secreted to the extracellular matrix. HSPA5 is intracellular and membrane-associated, whereas CLIC1 is cytosolic. HPA evidence emphasizes blood vessels, fibroblasts, smooth muscle cells, and trophoblast-related cell types, with additional liver and placenta associations. Immune-cell specificity is generally low or absent, although VCAN is group-enriched in classical monocytes and myeloid dendritic cells and CLIC1 is associated with platelet and megakaryocyte cell types. Heart protein detection is present for most members, but cerebrospinal-fluid protein detection has no available HPA data. Thus, the shared signal could reflect vascular or stromal biology, extracellular proteins entering biofluids, or shared cellular material in the samples; it should not automatically be interpreted as a heart-specific or brain-specific mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a compact extracellular-matrix relationship: FN1 is linked to LAMA4 and VCAN with high-confidence interactions. VCAN is the principal network connector, linking to LAMA4, FN1-related extracellular-matrix biology, and the module's CLIC1 and HSPA5 associations in the co-abundance graph. No STRING functional-enrichment result was present. No hu.MAP complex contained multiple module members. Therefore, the network shows partial support for a biologically coherent matrix module rather than evidence for a complete, established physical complex. The co-abundance edges involving CLIC1 and HSPA5 are not independently supported by the supplied high-confidence STRING interaction list and should be treated as module-level associations rather than established direct binding relationships.

**STRING interactions (score >= 0.7)**: 2 of 10 gene pairs: FN1–LAMA4 (0.814); FN1–VCAN (0.866)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is not established as a wholly new molecular mechanism. The central FN1, VCAN, and LAMA4 extracellular-matrix relationships are already biologically well known, and the supplied STRING results independently support part of that organization. The potentially novel aspect is the conservation of this particular co-abundance pattern between cerebrospinal fluid and heart, especially the inclusion of CLIC1 and HSPA5 alongside matrix proteins. However, the evidence is insufficient to claim discovery of a new pathway or complex: no globally significant GO or KEGG term was detected, no multi-member hu.MAP complex was found, and absence from a database cannot establish novelty. A stronger novelty claim would require comparison with published cross-tissue co-abundance modules, disease cohorts, and independent datasets.

**Hypothesis.** Hypothesis: the conserved module reflects a vascular or stromal extracellular-matrix state shared by the heart and cerebrospinal-fluid environment. FN1, LAMA4, and VCAN may form the structural and adhesive core of a basement-membrane or matrix-remodeling program, while CLIC1 and HSPA5 may report accompanying cellular stress, membrane-trafficking, platelet-related, or secretory-proteostasis conditions. In biofluids, the signal could arise from extracellular proteins released by vascular or stromal cells, extracellular vesicles, or shared tissue injury and remodeling processes. This hypothesis requires testing by targeted protein measurements, cell-type deconvolution, extracellular-vesicle analysis, and replication in independent cerebrospinal-fluid and heart cohorts.

### Important genes

#### VCAN

- **Related proteins** (co-abundance neighbors): CLIC1 (0.87), HSPA5 (0.84), LAMA4 (0.82); STRING partners: FN1 (0.866)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles, Mid piece, Principal piece, End piece; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: versican. This gene is a member of the aggrecan/versican proteoglycan family. The protein encoded is a large chondroitin sulfate proteoglycan and is a major component of the extracellular matrix. This protein is involved in cell adhesion, proliferation, proliferation, migration and angiogenesis and plays a central role in tissue morphogenesis and maintenance. Mutations in this gene are the cause of Wagner s…
- **Diseases (Open Targets)**: Wagner disease (0.745); Abnormality of the skeletal system (0.581); diverticular disease (0.521); inherited retinal dystrophy (0.446); hereditary disease (0.417)
- **Europe PMC papers**: 7002
- **Why important**: VCAN is the central connector in the co-abundance graph and has the strongest network position among the module members. It encodes a large extracellular-matrix proteoglycan involved in adhesion, proliferation, migration, angiogenesis, morphogenesis, and maintenance. HPA links it to blood vessels, fibroblasts, and monocyte-related cell types, and detects the protein in heart. Its secreted-to-blood annotation makes it especially relevant to interpreting a shared biofluid and heart signal. It also has substantial literature support and disease associations including Wagner syndrome.
- **Conclusion**: Established evidence supports VCAN as the leading extracellular-matrix and vascular marker of the module. The hypothesis that it is the principal biological driver of the shared cerebrospinal-fluid and heart pattern remains unproven because co-abundance does not establish causality.

#### FN1

- **Related proteins** (co-abundance neighbors): LAMA4 (0.88); STRING partners: LAMA4 (0.814), VCAN (0.866)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 is a core extracellular-matrix and plasma glycoprotein with the strongest literature volume in the module. It participates in cell adhesion, cell-matrix adhesion, migration, wound healing, coagulation, host defense, and integrin-mediated signaling. It is connected in STRING to both LAMA4 and VCAN, providing the clearest known molecular bridge among the matrix genes. HPA associates it with blood vessels, liver, placenta, fibroblasts, hepatic stellate cells, and heart, while Open Targets links it to fibronectin-deposit disease and coronary artery disorder.
- **Conclusion**: Established evidence identifies FN1 as a plausible structural and circulating component of the module and as a key anchor for the known matrix relationships. It is reasonable to hypothesize that FN1 helps explain cross-tissue co-abundance, but the module does not establish that FN1 causes the shared signal.

#### LAMA4

- **Related proteins** (co-abundance neighbors): FN1 (0.88), VCAN (0.82); STRING partners: FN1 (0.814)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit alpha 4. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins are composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respecti…
- **Diseases (Open Targets)**: dilated cardiomyopathy 1JJ (0.517); eye disorder (0.434); familial isolated dilated cardiomyopathy (0.387); retinal disorder (0.370); bacterial infectious disease (0.370)
- **Europe PMC papers**: 2561
- **Why important**: LAMA4 encodes a laminin alpha subunit, an important constituent of basement membranes and extracellular matrix. Its functions include adhesion, migration, differentiation, signaling, and vascular or developmental organization. LAMA4 is directly connected to FN1 in STRING and co-abundant with VCAN in the module. HPA places it in cell types relevant to heart and stromal biology, including cardiomyocytes, epicardial cells, adipocytes, and fibro-adipogenic progenitors. Its disease associations include dilated cardiomyopathy.
- **Conclusion**: Established evidence supports LAMA4 as the basement-membrane and cardiac-structural component of the module. Its presence makes a vascular or cardiac matrix interpretation plausible, but the lack of heart immunohistochemical detection and the absence of a multi-member hu.MAP complex argue against overinterpreting it as a demonstrated heart-specific complex member.

#### HSPA5

- **Related proteins** (co-abundance neighbors): VCAN (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 encodes an endoplasmic-reticulum HSP seventy chaperone that regulates protein folding, assembly, and ER homeostasis and participates in the unfolded-protein response. It is connected to VCAN in the co-abundance graph and is detected in heart by HPA. Its cell-type associations include trophoblast and plasma-cell-related populations, making it relevant to secretory and proteostasis states. Its substantial literature volume and disease associations provide broad biological context, although the supplied STRING results do not establish a direct interaction with the matrix proteins.
- **Conclusion**: Established evidence supports HSPA5 as a stress and secretory-proteostasis marker that may accompany the matrix program. Its role as a mechanistic component of this conserved module is a hypothesis rather than an established conclusion, because the available evidence does not show a known physical complex with the other members.

## Module 1

**Tissue pair**: cerebrospinal_fluid and heart  
**Genes (7)**: CFB, COL6A3, SERPING1, LGALS3BP, LUM, HSPG2, PRELP

### Function

No GO/KEGG term passed global correction, so the module should not be assigned a statistically established pathway label. Its gene composition and network structure instead support an extracellular matrix and circulating-protein interface involving complement regulation, basement-membrane organization, collagen-associated matrix architecture, and cell–matrix signaling. CFB and SERPING1 provide an established complement-related component, whereas PRELP, LUM, COL6A3, and HSPG2 provide established extracellular-matrix functions. LGALS3BP adds a secreted cell–matrix and immune-response-associated protein. This is a functional interpretation from gene annotations and network evidence, not a claim of significant GO/KEGG enrichment.

**Cell composition.** All module genes are annotated as secreted proteins, with several secreted to blood and others secreted to extracellular matrix. HPA indicates strong tissue or cell-type restriction for most genes rather than a broadly expressed housekeeping profile. The recurring tissue contexts include liver, blood vessel, smooth muscle, and stromal or fibroblast-like cell types. Several genes are absent from immune cells, while others show immune-cell enhancement or enrichment, including basophil, neutrophil, and plasmacytoid dendritic-cell contexts. This pattern is more consistent with a blood-derived and extracellular-matrix mixture than with a uniform heart-specific cellular program. The shared cerebrospinal-fluid and heart signal could therefore reflect circulating proteins, vascular or stromal material, extracellular matrix turnover, or shared sample-cellular contamination. HPA heart protein detection is present for LGALS3BP and HSPG2, while several other genes are not detected in heart tissue; cerebrospinal-fluid protein detection has no available matching HPA data.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a connected extracellular-matrix substructure: COL6A3–LUM, HSPG2–LUM, HSPG2–PRELP, and LUM–PRELP, together with CFB–SERPING1. These relationships are concordant with known collagen-associated matrix organization, proteoglycan interactions, and complement regulation. LGALS3BP has no listed STRING partner in this module, so its placement is supported by co-abundance rather than a listed high-confidence physical or functional interaction. hu.MAP independently places CFB and SERPING1 together in complexes C1 through C5. Those complexes contain many circulating, complement, coagulation, acute-phase, and transport proteins, indicating that this pair belongs to a broader plasma-protein interaction context. However, only a small subset of each hu.MAP complex is represented in the module, so the complexes do not establish that the entire module is one physical complex. Overall, the known STRING and hu.MAP relationships support a composite extracellular and plasma-associated module rather than a newly identified molecular complex.

**STRING interactions (score >= 0.7)**: 5 of 21 gene pairs: CFB–SERPING1 (0.88); COL6A3–LUM (0.853); HSPG2–LUM (0.78); HSPG2–PRELP (0.839); LUM–PRELP (0.771)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09273.1 (CFB, SERPING1; 2/28); huMAP3_09531.1 (CFB, SERPING1; 2/47); huMAP3_10101.1 (CFB, SERPING1; 2/49); huMAP3_15040.1 (CFB, SERPING1; 2/64); huMAP3_10678.1 (CFB, SERPING1; 2/71)

### Novelty

The module may be novel as a cross-tissue co-abundance pattern, but the available evidence does not establish it as a new biological pathway or complex. Several component relationships are already known in STRING, and the CFB–SERPING1 pair recurs in hu.MAP plasma-associated complexes. The coherent combination of complement regulators with basement-membrane and collagen-associated proteins across cerebrospinal fluid and heart could represent a useful systems-level observation. Nevertheless, absence of a complete matching module in STRING or hu.MAP would not by itself prove novelty, and the blood and extracellular-matrix composition provides plausible non-novel explanations such as shared circulating proteins, vascular material, or stromal content. Independent replication, control for plasma abundance and cellular composition, and comparison with existing tissue co-abundance studies would be needed before calling the module a new finding.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of circulating complement-regulatory proteins and extracellular-matrix components at a vascular or stromal interface shared by cerebrospinal fluid and heart. In this model, CFB and SERPING1 represent complement activation and inhibition, while PRELP, LUM, COL6A3, and HSPG2 organize collagen-rich basement-membrane and perivascular matrix; LGALS3BP may connect secreted immune-response-associated material with cell–matrix interactions. The co-abundance could arise from coordinated matrix remodeling and complement exposure, or could instead be driven largely by shared blood-derived protein carryover. The latter alternative must be tested experimentally rather than inferred away.

### Important genes

#### CFB

- **Related proteins** (co-abundance neighbors): PRELP (0.87), HSPG2 (0.86), LUM (0.84); STRING partners: SERPING1 (0.88)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09273.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: complement factor B. This gene encodes complement factor B, a component of the alternative pathway of complement activation. Factor B circulates in the blood as a single chain polypeptide. Upon activation of the alternative pathway, it is cleaved by complement factor D yielding the noncatalytic chain Ba and the catalytic subunit Bb. The active subunit Bb is a serine protease which associates with C3b to form the alter…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with B factor anomaly (0.764); atypical hemolytic-uremic syndrome (0.705); Immunodeficiency due to a complement cascade protein anomaly (0.614); paroxysmal nocturnal hemoglobinuria (0.561); complement 3 glomerulopathy (0.546)
- **Europe PMC papers**: 7226
- **Why important**: CFB is a high-connectivity module gene and is linked by STRING to SERPING1, PRELP, HSPG2, and LUM. Its established function is as a component of the alternative complement pathway, with a circulating blood form and a catalytic fragment that participates in the alternative-pathway C3 convertase. It is liver-enriched, secreted to blood, absent from immune cells in the HPA summary, and has extensive disease and literature support involving complement disorders.
- **Conclusion**: Established evidence supports CFB as the principal complement-related anchor of the module and as a likely marker of circulating plasma contribution. It is plausible, but unproven, that its co-abundance with matrix proteins reports complement–matrix coupling in the shared tissues.

#### SERPING1

- **Related proteins** (co-abundance neighbors): LGALS3BP (0.84), PRELP (0.81); STRING partners: CFB (0.88)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09273.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: serpin family G member 1. This gene encodes a highly glycosylated plasma protein involved in the regulation of the complement cascade. Its encoded protein, C1 inhibitor, inhibits activated C1r and C1s of the first complement component and thus regulates complement activation. It is synthesized in the liver, and its deficiency is associated with hereditary angioneurotic oedema (HANE). Alternative splicing results in multipl…
- **Diseases (Open Targets)**: hereditary angioedema with C1Inh deficiency (0.828); hereditary angioedema type 1 (0.750); hereditary angioedema (0.728); angioedema (0.616); hereditary angioedema type 2 (0.614)
- **Europe PMC papers**: 4203
- **Why important**: SERPING1 is connected to CFB in STRING and is present with CFB in every listed hu.MAP complex containing module members. It encodes the plasma C1 inhibitor, an established regulator of complement activation and a liver-synthesized secreted protein. Its strong disease associations with hereditary angioedema and complement-inhibitor deficiency make it especially informative for interpreting the module as a regulated plasma-complement signal.
- **Conclusion**: Established evidence supports SERPING1 as the complement-inhibitory counterpart to CFB. The module may therefore capture balance between complement activation and inhibition, but co-abundance alone cannot demonstrate complement activity or a causal role in either cerebrospinal fluid or heart.

#### LUM

- **Related proteins** (co-abundance neighbors): COL6A3 (0.89), CFB (0.84); STRING partners: COL6A3 (0.853), HSPG2 (0.78), PRELP (0.771)
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lumican. This gene encodes a member of the small leucine-rich proteoglycan (SLRP) family that includes decorin, biglycan, fibromodulin, keratocan, epiphycan, and osteoglycin. In these bifunctional molecules, the protein moiety binds collagen fibrils and the highly charged hydrophilic glycosaminoglycans regulate interfibrillar spacings. Lumican is the major keratan sulfate proteoglycan of the cornea but is …
- **Diseases (Open Targets)**: lumbar disc herniation (0.359); Dupuytren Contracture (0.357); fibroblastic disorder (0.357); Hallux valgus (0.357); preeclampsia (0.154)
- **Europe PMC papers**: 14825
- **Why important**: LUM is a secreted extracellular-matrix proteoglycan with a central position in the matrix subnetwork through its STRING links to COL6A3, HSPG2, PRELP, and CFB. Its established functions include collagen-fibril organization and regulation of matrix spacing, and its HPA profile points to gallbladder, placenta, and decidual-stromal contexts, with immune-cell enrichment in basophils. It also has substantial literature and disease-association support for fibroblastic and connective-tissue disorders.
- **Conclusion**: Established evidence supports LUM as a core matrix-organization gene that connects several extracellular components of the module. Its presence makes matrix remodeling a credible interpretation, although the shared tissue signal could still reflect stromal or vascular material rather than active remodeling.

#### PRELP

- **Related proteins** (co-abundance neighbors): LGALS3BP (0.89), CFB (0.87), SERPING1 (0.81); STRING partners: HSPG2 (0.839), LUM (0.771)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proline and arginine rich end leucine rich repeat protein. The protein encoded by this gene is a leucine-rich repeat protein present in connective tissue extracellular matrix. This protein functions as a molecule anchoring basement membranes to the underlying connective tissue. This protein has been shown to bind type I collagen to basement membranes and type II collagen to cartilage. It also binds the basement membrane heparan sulfate proteoglycan perlec…
- **Diseases (Open Targets)**: osteoarthritis, hip (0.299); cervical carcinoma (0.230); ovarian neoplasm (0.219); arthropathy (0.169); liver disorder (0.167)
- **Europe PMC papers**: 1236
- **Why important**: PRELP has high module connectivity and links to LGALS3BP, CFB, and SERPING1, while its known partners include LUM and HSPG2. It encodes a leucine-rich extracellular-matrix protein that anchors basement membranes to connective tissue and binds collagen and perlecan. HPA associates it with blood vessels and fibroblast-like cell types, and its connective-tissue and disease literature provides biological context for a vascular or stromal matrix component.
- **Conclusion**: Established evidence supports PRELP as a basement-membrane and connective-tissue organizer that may bridge the matrix and complement-associated portions of the module. A direct functional bridge between PRELP and complement proteins remains a hypothesis based on network co-abundance and reported interaction evidence.

#### HSPG2

- **Related proteins** (co-abundance neighbors): CFB (0.86); STRING partners: LUM (0.78), PRELP (0.839)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 encodes perlecan, a large extracellular proteoglycan that binds and cross-links basement-membrane components and cell-surface molecules. It connects in STRING to LUM and PRELP and is also linked to CFB in the module network. HPA places it in blood-vessel-associated and fibro-adipogenic or hepatic-stellate cell contexts, with protein detection in heart, making it relevant to a vascular or cardiac extracellular-matrix interpretation. Its disease associations include syndromic matrix and muscle-related disorders as well as atrial fibrillation.
- **Conclusion**: Established evidence supports HSPG2 as a structural extracellular-matrix scaffold and a plausible tissue-relevant anchor. Its link to CFB suggests a possible matrix–complement interface, but this mechanistic connection is not established by the module alone.
