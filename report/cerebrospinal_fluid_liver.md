# Conserved co-abundance modules: cerebrospinal_fluid and liver

## Module 0

**Tissue pair**: cerebrospinal_fluid and liver  
**Genes (8)**: SLC3A2, APOA2, ATP1B1, CPD, LAMB1, MAN1A1, IGF2R, CTSA

### Function

No GO/KEGG term passed global BH correction, and STRING reported no functional-enrichment term. The gene annotations nevertheless suggest a mixed biological theme involving membrane transport and electrochemical gradients through ATP1B1, amino-acid and calcium transport through SLC3A2, Golgi glycan processing through MAN1A1, lysosomal targeting through IGF2R, proteolysis and protein processing through CTSA and CPD, extracellular-matrix biology through LAMB1, and hepatic lipoprotein biology through APOA2. The network therefore does not support a single established pathway-level function. Its most defensible interpretation is a mixed trafficking, membrane, extracellular-matrix, proteolytic, and liver-derived lipoprotein module. The lack of globally significant enrichment does not by itself invalidate the co-abundance module.

**Cell composition.** The module is not predominantly composed of secreted or plasma proteins. APOA2 is explicitly secreted to blood, and LAMB1 is secreted to the extracellular matrix; CTSA has intracellular and membrane secretome annotation. The remaining genes are mainly membrane, Golgi, cytosolic, or intracellular proteins. HPA shows a mixture of tissue-enhanced, tissue-enriched, and broadly distributed genes rather than a uniform tissue program. Liver and hepatocyte signals are present through MAN1A1 and APOA2, while CPD and IGF2R show neutrophil-associated annotations and ATP1B1 shows basophil enhancement. Thus, the shared cerebrospinal-fluid/liver signal could partly reflect liver-derived extracellular material, tissue or cell admixture, or shared secretory and trafficking biology, but the evidence does not support describing the module as simply a blood-cell module. HPA provides no matching cerebrospinal-fluid protein-detection data, so direct protein-level confirmation in that tissue is unavailable.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship within the module is CPD–IGF2R. No other listed pair has a high-confidence STRING interaction, STRING functional-enrichment term, or recorded STRING partner in the fact sheet. No hu.MAP complex contains multiple module members. These results indicate that the co-abundance structure is largely not recapitulated by currently catalogued physical interactions or complexes. The CPD–IGF2R relationship provides limited support for a proteolytic, lysosomal, or intracellular trafficking connection, but it does not establish a complete module mechanism. Co-abundance edges should therefore be treated as coordinated abundance relationships rather than validated protein-protein interactions.

**STRING interactions (score >= 0.7)**: 1 of 28 gene pairs: CPD–IGF2R (0.738)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The cross-tissue co-abundance observation may be a potentially new association, but the fact sheet is insufficient to establish a new biological mechanism. Its novelty is supported only in the limited sense that the module has little overlap with the listed STRING and hu.MAP interaction or complex evidence and lacks a previously obvious canonical enrichment signature. Absence from STRING or hu.MAP alone does not prove novelty, because those resources are incomplete and the module may reflect co-regulation, shared compartmental abundance, extracellular carryover, cell composition, or technical structure rather than direct binding. A claim of novelty would require comparison with prior co-abundance studies, independent cohorts, replication, and tests distinguishing hepatic secretion or sample admixture from coordinated biology.

**Hypothesis.** Hypothesis: the module may represent a shared liver-associated and extracellularly observable abundance program that combines hepatic lipoprotein release with intracellular glycoprotein processing, lysosomal targeting, membrane transport, and proteolysis. In cerebrospinal fluid, the signal could arise from liver-derived or circulating proteins, extracellular-matrix material, or shared secretory and barrier-associated processes; in liver, it could reflect hepatocyte abundance together with non-hepatocyte cellular contributions. The CPD–IGF2R relationship is compatible with a proteolytic and lysosomal-trafficking component, while APOA2, MAN1A1, and the membrane proteins suggest additional parallel processes rather than one proven biochemical pathway. This hypothesis requires validation with cell-type-resolved data, targeted protein measurements, and replication in independent cerebrospinal-fluid and liver samples.

### Important genes

#### IGF2R

- **Related proteins** (co-abundance neighbors): MAN1A1 (0.85), ATP1B1 (0.82), SLC3A2 (0.81); STRING partners: CPD (0.738)
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enhanced; location Golgi apparatus; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor 2 receptor. This gene encodes a receptor for both insulin-like growth factor 2 and mannose 6-phosphate. The binding sites for each ligand are located on different segments of the protein. This receptor has various functions, including in the intracellular trafficking of lysosomal enzymes, the activation of transforming growth factor beta, and the degradation of insulin-like growth factor 2. Mutation or loss o…
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.498); coronary artery disorder (0.477); Hypercholesterolemia (0.369); myocardial ischemia (0.359); coronary atherosclerosis (0.349)
- **Europe PMC papers**: 12245
- **Why important**: IGF2R is a central connector in the module, linking MAN1A1, ATP1B1, and SLC3A2, and it is the only member involved in the high-confidence STRING relationship with CPD. Established annotations assign it roles in IGF2 and mannose-6-phosphate binding, lysosomal-enzyme targeting, lysosomal transport, transforming-growth-factor-beta activation, and IGF2 degradation. It has liver localization evidence and an association with hepatocellular carcinoma, with extensive literature coverage.
- **Conclusion**: Established evidence supports IGF2R as the strongest candidate for an intracellular trafficking and lysosomal-processing component of the module. Its network position makes it a plausible coordinator, but the co-abundance data do not prove that it mechanistically regulates the other module members. The proposed role as a bridge between liver-associated processing and extracellularly observed abundance remains a hypothesis.

#### ATP1B1

- **Related proteins** (co-abundance neighbors): LAMB1 (0.86), CPD (0.86), SLC3A2 (0.85), IGF2R (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit beta 1. The protein encoded by this gene belongs to the family of Na+/K+ and H+/K+ ATPases beta chain proteins, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a vari…
- **Diseases (Open Targets)**: cardiovascular disorder (0.634); atrial fibrillation (0.606); congestive heart failure (0.601); heart failure (0.585); cardiac arrhythmia (0.536)
- **Europe PMC papers**: 2226
- **Why important**: ATP1B1 has the most central network position and connects membrane, transport, and trafficking-associated members including LAMB1, CPD, SLC3A2, and IGF2R. Its established function is as a beta subunit of sodium and potassium ATPase complexes that maintain transmembrane electrochemical gradients and support sodium-coupled transport, osmotic regulation, and cellular excitability. It also has cardiovascular disease associations and substantial literature coverage.
- **Conclusion**: Established evidence supports ATP1B1 as a membrane-homeostasis marker within the module. Its central position makes membrane organization or transport a plausible organizing feature, but the module does not establish a direct ATP1B1 interaction with its inferred neighbors. A role in coordinating the whole cross-tissue module is therefore hypothetical.

#### CTSA

- **Related proteins** (co-abundance neighbors): SLC3A2 (0.84), APOA2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Vesicles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cathepsin A. This gene encodes a member of the peptidase S10 family of serine carboxypeptidases. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate two chains that comprise the heterodimeric active enzyme. This enzyme possesses deamidase, esterase and carboxypeptidase activities and acts as a scaffold in the …
- **Diseases (Open Targets)**: galactosialidosis (0.842); cathepsin a-related arteriopathy-strokes-leukoencephalopathy (0.464); hereditary disease (0.451); lysosomal storage disease (0.373); Lynch syndrome (0.340)
- **Europe PMC papers**: 8422
- **Why important**: CTSA connects SLC3A2 and APOA2 and has liver protein detection, vesicular localization, intracellular and membrane secretome annotation, and platelet-associated cell-type enrichment. It is an active serine carboxypeptidase with deamidase and esterase functions and a scaffold role in a lysosomal multienzyme complex. Its established disease association with galactosialidosis and related arteriopathy gives it strong mechanistic and clinical relevance, supported by extensive literature.
- **Conclusion**: Established evidence supports CTSA as a proteolytic, lysosomal, and protein-stability component that could connect intracellular processing with hepatic or extracellular protein abundance. The module does not demonstrate that CTSA enzymatic activity drives the co-abundance pattern. Its proposed bridging role between APOA2 and the trafficking-related genes is a hypothesis.

#### APOA2

- **Related proteins** (co-abundance neighbors): CTSA (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein A2. This gene encodes apolipoprotein (apo-) A-II, which is the second most abundant protein of the high density lipoprotein particles. The protein is found in plasma as a monomer, homodimer, or heterodimer with apolipoprotein D. Defects in this gene may result in apolipoprotein A-II deficiency or hypercholesterolemia. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: apolipoprotein A-II amyloidosis (0.400); amyloidosis (0.382); hypercholesterolemia, familial, 1 (0.341); pancreatic neoplasm (0.096); familial pancreatic carcinoma (0.096)
- **Europe PMC papers**: 8528
- **Why important**: APOA2 is the clearest liver-derived extracellular marker in the module: it is tissue-enriched in liver, cell-type enriched in hepatocytes, and secreted to blood. It is a major constituent of high-density lipoprotein particles and has established roles or associations involving lipid transport, triglyceride metabolism, phospholipid biology, immune signaling, hypercholesterolemia, and apolipoprotein A-II amyloidosis. It also has substantial literature coverage.
- **Conclusion**: Established evidence supports APOA2 as a hepatic lipoprotein component and a plausible contributor to a shared liver and cerebrospinal-fluid abundance signal through extracellular or circulating material. It is not evidence that the entire module is a lipid-metabolism pathway, because the other genes span membrane, Golgi, lysosomal, and extracellular-matrix functions. Any causal connection between APOA2 and CTSA or the broader module remains hypothetical.

#### MAN1A1

- **Related proteins** (co-abundance neighbors): IGF2R (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosidase alpha class 1A member 1. This gene encodes a class I mammalian Golgi 1,2-mannosidase which is a type II transmembrane protein. This protein catalyzes the hydrolysis of three terminal mannose residues from peptide-bound Man(9)-GlcNAc(2) oligosaccharides and belongs to family 47 of glycosyl hydrolases. [provided by RefSeq, Jul 2012].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.368); nervous system benign neoplasm (0.353); smoking initiation (0.311); eye disorder (0.292); hypertrophic cardiomyopathy (0.280)
- **Europe PMC papers**: 645
- **Why important**: MAN1A1 is connected to IGF2R and is tissue-enhanced in liver with liver protein detection. It encodes a Golgi alpha-mannosidase involved in N-glycan mannose trimming and glycoprotein processing, including processing associated with endoplasmic-reticulum quality control. Its annotation provides a plausible biochemical link to glycoprotein trafficking and to the mannose-6-phosphate-related biology of IGF2R, even though no hu.MAP complex is recorded.
- **Conclusion**: Established evidence supports MAN1A1 as a liver-associated Golgi glycan-processing marker and as a plausible partner process for IGF2R-mediated trafficking. The module does not prove a functional MAN1A1–IGF2R complex or coordinated glycan-processing mechanism. That connection should be regarded as a mechanistic hypothesis requiring direct validation.

## Module 1

**Tissue pair**: cerebrospinal_fluid and liver  
**Genes (8)**: LRG1, SERPINA3, SERPINA6, CFB, C5, C9, COL18A1, ITIH4

### Function

The module is most consistent with a liver-derived, circulating extracellular protein program involving complement, protease regulation, steroid transport, extracellular-matrix biology, and inflammatory or acute-phase biology. This interpretation is supported by the functions of CFB, C5, C9, ITIH4, SERPINA3, SERPINA6, LRG1, and COL18A1, as well as the liver and hepatocyte enrichment in HPA. However, no GO or KEGG term passed global multiple-testing correction, so no pathway-level enrichment can be claimed as statistically significant. The functional interpretation therefore rests on the concordant annotations, tissue distribution, network structure, and protein-complex evidence rather than on globally significant enrichment. The network has a partially connected core centered on ITIH4, with complement-related links involving CFB, C5, and C9, and additional links to SERPINA3, SERPINA6, and LRG1. Overall, this resembles a coordinated circulating innate-defense and extracellular-protein module rather than a cell-intrinsic metabolic pathway.

**Cell composition.** All module genes are annotated by HPA as secreted proteins, with most secreted to blood and COL18A1 secreted to the extracellular matrix. The module is strongly liver-associated: every gene has liver tissue enrichment or enhancement, and hepatocytes are the dominant enriched cell type. Most genes are not detected in immune cells, while LRG1 is immune-cell enriched in neutrophils and COL18A1 is immune-cell enhanced in neutrophils. This argues against interpreting the module primarily as a blood-cell transcriptional program. Because the proteins are circulating and liver-produced, the shared cerebrospinal-fluid and liver signal could reflect transport of plasma proteins into cerebrospinal fluid, vascular or blood contamination, blood–brain barrier exchange, or a shared extracellular-fluid environment. HPA protein detection in liver is present for only part of the module, so transcript-level tissue enrichment should not be treated as proof that every protein is abundant in liver tissue.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a small but biologically coherent set of high-confidence relationships: C5–C9 is particularly strong, C5–CFB is also supported, and LRG1–SERPINA3 is supported. STRING reports no functional-enrichment result for the module, so it does not independently establish a pathway. hu.MAP provides stronger evidence of recurring complex or co-complex context. CFB, C5, SERPINA6, and ITIH4 repeatedly occur together across several complexes, while CFB, C5, SERPINA3, and ITIH4 recur across another group of complexes. SERPINA3, C5, and ITIH4 also recur in additional complexes, and LRG1 with SERPINA6 appears in an immune-associated complex. These results indicate that the co-abundance module overlaps known extracellular and plasma-protein assemblies, although the complexes contain many proteins outside the module and therefore do not prove that all module members form one physical complex. The distinction between the sparse direct STRING network and the broader hu.MAP overlap suggests that the module may capture related extracellular protein contexts rather than a single compact molecular machine.

**STRING interactions (score >= 0.7)**: 3 of 28 gene pairs: C5–C9 (0.999); C5–CFB (0.774); LRG1–SERPINA3 (0.711)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08796.1 (CFB, C5, SERPINA6, ITIH4; 4/15); huMAP3_09832.1 (CFB, C5, SERPINA6, ITIH4; 4/18); huMAP3_09531.1 (CFB, SERPINA3, C5, ITIH4; 4/47); huMAP3_10101.1 (CFB, SERPINA3, C5, ITIH4; 4/49); huMAP3_10678.1 (CFB, SERPINA3, C5, ITIH4; 4/71); huMAP3_09434.1 (SERPINA3, C5, ITIH4; 3/33); huMAP3_08395.1 (CFB, SERPINA3, C5; 3/43); huMAP3_15040.1 (CFB, SERPINA3, ITIH4; 3/64); huMAP3_00178.1 (C5, SERPINA6; 2/9); huMAP3_08224.1 (SERPINA3, C5; 2/21); huMAP3_14295.1 (LRG1, SERPINA6; 2/38)

### Novelty

The module should not be described as a newly discovered molecular complex or pathway. Several of its relationships and recurring protein combinations are already represented in STRING and hu.MAP, and the individual genes have established complement, protease-inhibitor, steroid-transport, extracellular-matrix, and inflammatory functions. A potentially novel aspect is the reproducible co-abundance of this particular liver-associated secreted-protein set across cerebrospinal fluid and liver, especially the combination of a complement core with ITIH4, SERPINA6, LRG1, SERPINA3, and COL18A1. That cross-tissue co-abundance observation may be novel, but novelty cannot be established from the fact sheet alone. Absence of a particular edge from STRING or hu.MAP would not demonstrate novelty, because those resources represent physical interaction or complex evidence rather than all possible co-abundance relationships. The appropriate conclusion is that the module is a potentially novel cross-tissue co-abundance pattern built from largely established extracellular proteins.

**Hypothesis.** Hypothesis: hepatocyte-derived secreted proteins enter the circulation and contribute to a shared extracellular-fluid signature in liver and cerebrospinal fluid. Within this signature, complement components CFB, C5, and C9 may represent innate-defense capacity; ITIH4 and SERPINA3 may regulate proteolysis and inflammatory extracellular remodeling; SERPINA6 may transport corticosteroids and thereby connect the module to endocrine state; LRG1 may link the circulating protein environment to vascular, epithelial, wound-healing, or transforming-growth-factor signaling; and COL18A1 may connect it to vascular extracellular matrix and endostatin-related biology. The module could therefore reflect coordinated hepatic secretion and extracellular remodeling rather than direct co-expression in a single cell. This hypothesis requires validation with independent cohorts, adjustment for plasma contamination and vascular leakage, protein-level measurements, and experiments testing whether the proposed proteins physically or functionally influence one another.

### Important genes

#### ITIH4

- **Related proteins** (co-abundance neighbors): CFB (0.85), C9 (0.84), LRG1 (0.83), SERPINA3 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08796.1, huMAP3_09832.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_09434.1, huMAP3_15040.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 4. The protein encoded by this gene is secreted into the blood, where it is cleaved by plasma kallikrein into two smaller forms. Expression of this gene has been detected only in liver, and it seems to be upregulated during surgical trauma. This gene is part of a cluster of similar genes on chromosome 3. Two transcript variants encoding different isoforms have been found for this gene. [provided by R…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.466); coronary artery disorder (0.417); type 2 diabetes mellitus (0.397); osteoarthritis (0.387); diabetes mellitus (0.363)
- **Europe PMC papers**: 1710
- **Why important**: ITIH4 is the most connected hub in the module and links CFB, C9, LRG1, and SERPINA3. It is liver-enriched, secreted to blood, associated with acute-phase response, hyaluronan metabolism, and cytokine response, and appears repeatedly in hu.MAP complexes (hu.MAP huMAP3_08796.1), (hu.MAP huMAP3_09832.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_09434.1), and (hu.MAP huMAP3_15040.1). Its extensive literature and disease associations make it a strong integrator of extracellular inflammation and matrix-related biology.
- **Conclusion**: Established evidence supports ITIH4 as a liver-derived circulating extracellular scaffold or acute-phase-associated component with a central position in this module. It is plausible, but not established, that ITIH4 helps organize the observed complement and protease-regulatory co-abundance pattern.

#### C5

- **Related proteins** (co-abundance neighbors): SERPINA6 (0.85); STRING partners: C9 (0.999), CFB (0.774)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08796.1, huMAP3_09832.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_00178.1, huMAP3_08224.1
- **Function (MyGene.info)**: complement C5. This gene encodes a component of the complement system, a part of the innate immune system that plays an important role in inflammation, host homeostasis, and host defense against pathogens. The encoded preproprotein is proteolytically processed to generate multiple protein products, including the C5 alpha chain, C5 beta chain, C5a anaphylatoxin and C5b. The C5 protein is comprised of the C5 alpha…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.744); paroxysmal nocturnal hemoglobinuria (0.610); myasthenia gravis (0.586); atypical hemolytic-uremic syndrome (0.544); neuromyelitis optica (0.516)
- **Europe PMC papers**: 81450
- **Why important**: C5 is a central complement effector, has a direct STRING relationship with C9 and CFB, and occurs across many hu.MAP complexes including (hu.MAP huMAP3_08796.1), (hu.MAP huMAP3_09832.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_09434.1), (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_00178.1), and (hu.MAP huMAP3_08224.1). It is liver-enriched and hepatocyte-enriched, and its established role in complement activation, inflammation, chemotaxis, and membrane-attack-complex biology gives the module a clear innate-defense anchor. It also has exceptionally extensive literature and strong disease associations involving complement deficiency and immune-mediated disorders.
- **Conclusion**: Established evidence identifies C5 as a biologically important complement component that anchors the module in circulating innate immunity. The module does not establish that complement is actively being cleaved or activated in either tissue; that remains a hypothesis requiring measurements of activation fragments and functional activity.

#### CFB

- **Related proteins** (co-abundance neighbors): SERPINA6 (0.88), ITIH4 (0.85); STRING partners: C5 (0.774)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08796.1, huMAP3_09832.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_08395.1, huMAP3_15040.1
- **Function (MyGene.info)**: complement factor B. This gene encodes complement factor B, a component of the alternative pathway of complement activation. Factor B circulates in the blood as a single chain polypeptide. Upon activation of the alternative pathway, it is cleaved by complement factor D yielding the noncatalytic chain Ba and the catalytic subunit Bb. The active subunit Bb is a serine protease which associates with C3b to form the alter…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with B factor anomaly (0.764); atypical hemolytic-uremic syndrome (0.705); Immunodeficiency due to a complement cascade protein anomaly (0.614); paroxysmal nocturnal hemoglobinuria (0.561); complement 3 glomerulopathy (0.546)
- **Europe PMC papers**: 7226
- **Why important**: CFB connects directly to C5 in STRING and has strong network links to SERPINA6 and ITIH4. It recurs in numerous hu.MAP complexes, including (hu.MAP huMAP3_08796.1), (hu.MAP huMAP3_09832.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_08395.1), and (hu.MAP huMAP3_15040.1). As the catalytic precursor of the alternative-pathway C3 convertase, it provides a mechanistic bridge between hepatic secretion and complement activation. Its liver enrichment, blood-secreted annotation, extensive literature, and associations with complement disorders further strengthen its importance.
- **Conclusion**: Established evidence supports CFB as an alternative-pathway complement component embedded in the module’s extracellular immune-defense context. It is not established that the module represents active alternative-pathway signaling, because co-abundance does not demonstrate proteolytic activation.

#### SERPINA6

- **Related proteins** (co-abundance neighbors): CFB (0.88), C5 (0.85), COL18A1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08796.1, huMAP3_09832.1, huMAP3_00178.1, huMAP3_14295.1
- **Function (MyGene.info)**: serpin family A member 6. This gene encodes an alpha-globulin protein with corticosteroid-binding properties. This is the major transport protein for glucorticoids and progestins in the blood of most vertebrates. The gene localizes to a chromosomal region containing several closely related serine protease inhibitors which may have evolved by duplication events. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: corticosteroid-binding globulin deficiency (0.638); hereditary disease (0.193); plasma protein metabolism disease (0.192); femur fracture (0.172); liver disorder (0.144)
- **Europe PMC papers**: 799
- **Why important**: SERPINA6 has strong links to CFB, C5, and COL18A1 and participates in hu.MAP complexes (hu.MAP huMAP3_08796.1), (hu.MAP huMAP3_09832.1), (hu.MAP huMAP3_00178.1), and (hu.MAP huMAP3_14295.1). It is a liver-enriched blood-secreted corticosteroid-binding protein and is the module’s clearest endocrine transport component. Its position connects complement-associated proteins with steroid transport and with an extracellular or immune-associated complex context. Its established clinical association with corticosteroid-binding globulin deficiency adds disease relevance despite a more moderate literature volume than the complement genes.
- **Conclusion**: Established evidence supports SERPINA6 as a circulating steroid-transport protein that may explain why endocrine state could influence this module. Any claim that SERPINA6 regulates complement activity or drives the cross-tissue co-abundance pattern is hypothetical.

#### COL18A1

- **Related proteins** (co-abundance neighbors): SERPINA6 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type XVIII alpha 1 chain. This gene encodes the alpha chain of type XVIII collagen. This collagen is one of the multiplexins, extracellular matrix proteins that contain multiple triple-helix domains (collagenous domains) interrupted by non-collagenous domains. A long isoform of the protein has an N-terminal domain that is homologous to the extracellular part of frizzled receptors. Proteolytic processing at several endogeno…
- **Diseases (Open Targets)**: Knobloch syndrome 1 (0.778); Knobloch syndrome (0.700); hereditary glaucoma, primary closed-angle (0.593); Dupuytren Contracture (0.587); severe early-childhood-onset retinal dystrophy (0.501)
- **Europe PMC papers**: 5223
- **Why important**: COL18A1 is the module’s extracellular-matrix component and connects to SERPINA6. It is liver- and blood-vessel-enhanced, hepatocyte- and pancreatic-duct-cell-enhanced, secreted to extracellular matrix, and associated with angiogenesis, endothelial morphogenesis, and endostatin production. Its disease associations include Knobloch syndrome and ocular disease, and its substantial literature supports a role distinct from the circulating complement proteins.
- **Conclusion**: Established evidence supports COL18A1 as an extracellular-matrix and vascular-biology component that broadens the module beyond complement and plasma transport. Its inclusion may indicate vascular or matrix-related biology in the shared fluid signature, but whether it functionally interacts with SERPINA6 or the complement proteins is not established.

## Module 2

**Tissue pair**: cerebrospinal_fluid and liver  
**Genes (8)**: AFM, GLB1, C1QC, CPVL, GNS, LGALS3BP, OGN, PLOD2

### Function

The module does not have a statistically supported GO or KEGG functional enrichment: no GO/KEGG term passed global correction. Its biological interpretation therefore rests on the gene annotations and network structure rather than on enrichment. The strongest coherent signal is a mixture of lysosomal and glycoconjugate metabolism, extracellular matrix and collagen-related biology, immune or macrophage-associated biology, and liver-derived circulating proteins. GNS is the most connected node and encodes a lysosomal enzyme involved in glycosaminoglycan degradation. GLB1 is also a lysosomal glycosidase involved in glycoconjugate and ganglioside catabolism, while PLOD2 is involved in collagen maturation and organization. CPVL provides a protease-related component with prominent choroid-plexus and myeloid-cell associations. C1QC indicates complement and macrophage-related biology, and AFM indicates a liver-produced serum transport protein. Overall, this is best interpreted as a mixed tissue-fluid module reflecting coordinated lysosomal, extracellular-matrix, immune-cell, and hepatic secretory signals, rather than as evidence for one narrowly defined pathway.

**Cell composition.** All module proteins are annotated as secreted or extracellularly detectable in the supplied secretome summary, although several are described as intracellular and membrane proteins rather than classically secreted proteins. AFM, LGALS3BP, C1QC, and OGN are secreted or extracellularly associated proteins, with AFM particularly characteristic of liver-derived circulating protein. HPA evidence shows liver enrichment or liver detection for AFM and detection in liver for several other members, while CPVL is enhanced in choroid plexus and lymphoid tissue. The module also has a strong myeloid context: Kupffer cells, macrophages, monocytes, Hofbauer cells, and myeloid dendritic cells recur among the enriched cell types. This composition makes a shared blood, immune-cell, or extracellular-fluid contribution a plausible explanation for co-abundance in cerebrospinal fluid and liver. It should not automatically be interpreted as a liver-specific neuronal or cerebrospinal-fluid mechanism. The mixture is not uniformly housekeeping-like: some genes are broadly expressed, but others show liver, choroid-plexus, vascular, or myeloid enrichment.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship within the module is GLB1–GNS. This is biologically coherent because both proteins are lysosomal glycosidases involved in degradation of complex glycoconjugates. The remaining module relationships are not supported by high-confidence STRING interactions in the supplied data. No hu.MAP complex contains multiple module members. Thus, the co-abundance network is not simply a known canonical protein complex. The known GLB1–GNS relationship supports a lysosomal catabolic substructure, whereas the links involving PLOD2, CPVL, LGALS3BP, OGN, C1QC, and AFM may reflect shared cellular origin, secretion, extracellular remodeling, disease state, or coordinated abundance rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 1 of 28 gene pairs: GLB1–GNS (0.957)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a potentially interesting cross-tissue co-abundance pattern, but the supplied evidence does not establish it as a new biological mechanism. Its lack of a multi-member hu.MAP complex and its sparse STRING support indicate that most of the module is not represented as one established physical complex. However, absence from those resources does not prove novelty: co-abundance can arise from shared cell types, secretion, extracellular transport, lysosomal turnover, or indirect regulation. The GLB1–GNS connection is already supported by STRING, and the individual functions of the genes are established. A defensible novelty claim would require comparison with prior cross-tissue co-abundance studies, replication in independent cohorts, control for blood-cell and protein-leakage effects, and testing whether the non-STRING edges reproduce. On the current evidence, the appropriate conclusion is a candidate mixed lysosomal–immune–hepatic secretory module, not a demonstrated novel pathway.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of proteins contributed by liver-derived circulating material and myeloid-lineage cells or macrophage-like cells present in, or influencing, cerebrospinal fluid and liver samples. Within this mixed signal, GNS and GLB1 may represent a lysosomal glycoconjugate-catabolism axis, PLOD2 and OGN may represent extracellular-matrix remodeling, and C1QC and LGALS3BP may represent immune or extracellular communication. AFM could mark the hepatic secretory component, while CPVL could connect the signal to choroid-plexus and monocyte or macrophage-associated biology. This hypothesis predicts that the module will weaken after adjustment for blood contamination, immune-cell abundance, and hepatocyte or macrophage proportions, and that its reproducible component will be strongest in samples with matched extracellular-fluid and liver inflammatory or secretory states. These predictions are hypotheses, not established findings from the supplied data.

### Important genes

#### GNS

- **Related proteins** (co-abundance neighbors): GLB1 (0.92), CPVL (0.86), OGN (0.82), AFM (0.80); STRING partners: GLB1 (0.957)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glucosamine (N-acetyl)-6-sulfatase. The product of this gene is a lysosomal enzyme found in all cells. It is involved in the catabolism of heparin, heparan sulphate, and keratan sulphate. Deficiency of this enzyme results in the accumulation of undegraded substrate and the lysosomal storage disorder mucopolysaccharidosis type IIID (Sanfilippo D syndrome). Mucopolysaccharidosis type IIID is the least common of the four subtypes of Sa…
- **Diseases (Open Targets)**: mucopolysaccharidosis type 3D (0.811); mucopolysaccharidosis type 3 (0.610); mucopolysaccharidosis (0.372); ventricular fibrillation (0.233); preeclampsia (0.223)
- **Europe PMC papers**: 3078
- **Why important**: GNS is the most connected and strongest node in the module. It is a lysosomal enzyme involved in heparin, heparan-sulfate, and keratan-sulfate degradation, and it connects to GLB1, CPVL, OGN, and AFM in the module. Its connection to GLB1 is the only high-confidence STRING relationship, providing the clearest known molecular anchor. Its disease association with mucopolysaccharidosis type three D and substantial literature support make it an informative mechanistic representative.
- **Conclusion**: Established: GNS is a lysosomal glycosaminoglycan-catabolism enzyme and a network hub, with a supported relationship to GLB1. Hypothesis: GNS may organize the lysosomal component of the shared co-abundance signal, although the network does not establish that it regulates the other module members.

#### GLB1

- **Related proteins** (co-abundance neighbors): GNS (0.92), PLOD2 (0.92); STRING partners: GNS (0.957)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galactosidase beta 1. This gene encodes a member of the glycosyl hydrolase 35 family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature lysosomal enzyme. This enzyme catalyzes the hydrolysis of a terminal beta-linked galactose residue from ganglioside substrates and other glycoconjugates. Mutat…
- **Diseases (Open Targets)**: mucopolysaccharidosis type 4B (0.849); GM1 gangliosidosis type 1 (0.847); GM1 gangliosidosis type 3 (0.842); GM1 gangliosidosis type 2 (0.842); GM1 gangliosidosis (0.771)
- **Europe PMC papers**: 2663
- **Why important**: GLB1 is directly connected to GNS and PLOD2 in the module and participates in the only high-confidence STRING pair. It encodes a lysosomal glycosidase involved in carbohydrate, glycoprotein, ganglioside, and keratan-sulfate catabolism. Its established associations with GM1 gangliosidosis and Morquio B syndrome make it relevant to lysosomal storage biology.
- **Conclusion**: Established: GLB1 provides strong support for a lysosomal glycoconjugate-processing component and for the biological plausibility of the GLB1–GNS edge. Hypothesis: coordinated GLB1 and GNS abundance may indicate shared lysosomal turnover or cellular composition, rather than a direct physical complex involving the full module.

#### CPVL

- **Related proteins** (co-abundance neighbors): GNS (0.86), PLOD2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carboxypeptidase vitellogenic like. The protein encoded by this gene is a carboxypeptidase and bears strong sequence similarity to serine carboxypeptidases. Carboxypeptidases are a large class of proteases that act to cleave a single amino acid from the carboxy termini of proteins or peptides. The exact function of this protein, however, has not been determined. [provided by RefSeq, Jan 2017].
- **Diseases (Open Targets)**: basal cell carcinoma (0.553); skin neoplasm (0.547); skin cancer (0.534); hypothyroidism (0.510); non-melanoma skin carcinoma (0.488)
- **Europe PMC papers**: 621
- **Why important**: CPVL links GNS and PLOD2 in the co-abundance graph. It is a carboxypeptidase-like protein whose exact function remains incompletely determined, and it is associated in HPA with choroid plexus, lymphoid tissue, Kupffer cells, macrophages, monocytes, and myeloid dendritic cells. This makes CPVL particularly informative for interpreting the shared cerebrospinal-fluid and liver context and for distinguishing a cell-composition signal from a purely hepatic signal.
- **Conclusion**: Established: CPVL has a strong tissue and myeloid-cell association in the supplied HPA evidence and occupies a connecting position between the lysosomal and collagen-related portions of the module. Hypothesis: CPVL may mark a macrophage, Kupffer-cell, or choroid-plexus contribution to the shared module, but its causal role is not established.

#### C1QC

- **Related proteins** (co-abundance neighbors): LGALS3BP (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C1q C chain. This gene encodes the C-chain polypeptide of serum complement subcomponent C1q, which associates with C1r and C1s to yield the first component of the serum complement system. C1q is composed of 18 polypeptide chains which include 6 A-chains, 6 B-chains, and 6 C-chains. Each chain contains an N-terminal collagen-like region and a C-terminal C1q globular domain. C1q deficiency is associated with lup…
- **Diseases (Open Targets)**: immunodeficiency due to a classical component pathway complement deficiency (0.619); C1Q deficiency (0.597); neurodegenerative disease (0.540); complement deficiency (0.462); C1Q deficiency 1 (0.462)
- **Europe PMC papers**: 4647
- **Why important**: C1QC is connected to LGALS3BP and is enriched in lymphoid tissue and macrophage-lineage cell types, including Kupffer cells and Hofbauer cells. It encodes a component of the classical complement system and is annotated for immune response, complement activation, and synapse pruning. Its links to complement deficiency and neurodegenerative disease make it especially relevant to a module shared with cerebrospinal fluid.
- **Conclusion**: Established: C1QC is a complement-associated, macrophage-lineage protein and supports an immune or myeloid interpretation of part of the module. Hypothesis: C1QC may connect peripheral macrophage or Kupffer-cell activity with cerebrospinal-fluid immune signaling, but the co-abundance data do not prove such communication.

#### AFM

- **Related proteins** (co-abundance neighbors): GNS (0.80); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: afamin. This gene is a member of the albumin gene family, which is comprised of four genes that localize to chromosome 4 in a tandem arrangement. These four genes encode structurally-related serum transport proteins that are known to be evolutionarily related. The protein encoded by this gene is regulated developmentally, expressed in the liver and secreted into the bloodstream. [provided by RefSeq, Jul 2…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.249); prostate carcinoma (0.204); adrenal gland disorder (0.103); non-alcoholic fatty liver (0.091); metabolic syndrome (0.082)
- **Europe PMC papers**: 24965
- **Why important**: AFM is connected to GNS and is the most liver-specific member according to the supplied HPA summary, with hepatocyte-associated expression and secretion to blood. It is a serum transport protein in the albumin family and is annotated for vitamin transport, protein stabilization, and extracellular protein transport. Its very substantial literature volume and liver-secretory biology make it a useful marker of the circulating hepatic component.
- **Conclusion**: Established: AFM supports a liver-derived, blood-associated contribution to the module and is not a specific marker of a lysosomal complex. Hypothesis: AFM may be carried into cerebrospinal-fluid-related measurements through shared extracellular-fluid composition or barrier and vascular processes, but contamination or passive transport must be excluded.

## Module 3

**Tissue pair**: cerebrospinal_fluid and liver  
**Genes (5)**: AOC3, CP, C3, SERPING1, TNC

### Function

The module is most consistent with a coordinated extracellular and circulating protein program linking complement regulation, inflammatory signaling, vascular or stromal adhesion, and metal or oxidative homeostasis. C3 is a central complement component, while SERPING1 is a liver-produced inhibitor of classical and lectin pathway complement activation. AOC3 contributes amine metabolism, cell adhesion, and inflammatory biology; TNC is an extracellular-matrix protein involved in cell adhesion, tissue remodeling, wound response, and neural or axonal guidance; and CP supports copper and iron homeostasis and oxidant handling. The network therefore suggests coordinated extracellular inflammatory, vascular-stromal, and tissue-injury biology rather than a narrowly defined intracellular pathway. No GO/KEGG term passed global correction, so this interpretation is based on the gene annotations, network structure, STRING relationships, hu.MAP context, and HPA evidence rather than on globally significant enrichment.

**Cell composition.** The module is strongly biased toward secreted or extracellular proteins: TNC is secreted to the extracellular matrix, SERPING1, C3, and CP are secreted to blood, and AOC3 is associated with the cell surface despite HPA listing cytosolic localization. HPA points particularly toward liver, blood vessels, smooth muscle, adipose tissue, hepatocytes, fibroblasts, pericytes, and related stromal or secretory cell types. Most genes were not detected as immune-cell markers, although C3 is immune-cell enriched and SERPING1 is immune-cell enhanced, with associations to non-classical monocytes, neutrophils, and plasmacytoid dendritic cells. HPA protein detection provides no matching cerebrospinal-fluid data and reports no detection in liver for the listed genes, so the tissue-specific RNA evidence should not be equated with demonstrated local protein abundance. The shared module could therefore reflect circulating plasma proteins, liver secretory biology, vascular or stromal cell composition, or sample-related blood contribution; it should not be interpreted automatically as a brain-specific module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports established relationships between C3 and CP and between C3 and SERPING1. These links are biologically coherent with complement and circulating plasma-protein biology. STRING provides no reported partners for TNC or AOC3 and no supplementary STRING functional-enrichment terms. hu.MAP repeatedly places CP, C3, and SERPING1 together across multiple complexes (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1), and (hu.MAP huMAP3_10678.1), while CP and C3 recur together in additional complexes (hu.MAP huMAP3_07432.1) and (hu.MAP huMAP3_08395.1), and CP and SERPING1 recur together in (hu.MAP huMAP3_09273.1). This repeated partial overlap indicates that the C3, CP, and SERPING1 relationships are already represented in curated or inferred complex-level resources. It does not establish that all module members form one physical complex, because TNC and AOC3 are absent from the listed hu.MAP complexes and the abundance network may reflect shared secretion, tissue origin, or co-regulation.

**STRING interactions (score >= 0.7)**: 2 of 10 gene pairs: C3–CP (0.751); C3–SERPING1 (0.954)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09531.1 (CP, C3, SERPING1; 3/47); huMAP3_10101.1 (CP, C3, SERPING1; 3/49); huMAP3_15040.1 (CP, C3, SERPING1; 3/64); huMAP3_10678.1 (CP, C3, SERPING1; 3/71); huMAP3_07432.1 (CP, C3; 2/18); huMAP3_09273.1 (CP, SERPING1; 2/28); huMAP3_08395.1 (CP, C3; 2/43)

### Novelty

The module should not be called a definitively new biological complex or pathway. Its complement and plasma-protein core is supported by prior STRING and hu.MAP evidence, especially the recurring C3, CP, and SERPING1 combinations. The co-abundance configuration may still be a potentially novel observation because the supplied resources do not report an established module consisting of all the listed genes, and TNC and AOC3 are not represented in the listed complexes. However, absence from STRING or hu.MAP alone cannot demonstrate novelty. A defensible claim is that this is a potentially novel cross-tissue co-abundance pattern built partly from known extracellular and complement relationships, requiring replication and independent testing against plasma contamination, liver abundance, vascular or stromal composition, and technical covariates.

**Hypothesis.** Hypothesis: shared liver and cerebrospinal-fluid abundance reflects a circulating extracellular response in which liver-derived C3, SERPING1, and CP track complement activity, complement restraint, and metal or oxidative status, while AOC3 and TNC report vascular-stromal adhesion, extracellular-matrix remodeling, and tissue injury or repair. The observed co-abundance could arise from coordinated secretion or from a common liver, vascular, stromal, or blood-derived component rather than direct physical interaction among all members. A testable prediction is that the module will covary with independent measures of complement activation, liver secretory output, vascular or stromal signatures, and blood exposure, while orthogonal protein assays and cell-composition adjustment should determine whether the cerebrospinal-fluid signal represents local biology or transport from the circulation.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): AOC3 (0.83), TNC (0.80); STRING partners: CP (0.751), SERPING1 (0.954)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_08395.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a central network member connected to AOC3 and TNC and has established STRING links to CP and SERPING1. Its annotation places it at the core of classical and alternative complement activation, inflammatory signaling, proteolysis, and membrane-attack-complex regulation. HPA identifies liver enrichment and immune-cell enrichment, and its disease associations include complement deficiency, complement-mediated renal disease, atypical hemolytic-uremic syndrome, and age-related macular degeneration. It also has the largest literature volume among the module genes.
- **Conclusion**: Established evidence supports C3 as the principal complement anchor and a major interpretive gene for the module. It is plausible, but not established from this dataset, that variation in complement activation drives the shared co-abundance pattern.

#### SERPING1

- **Related proteins** (co-abundance neighbors): TNC (0.89), AOC3 (0.83); STRING partners: C3 (0.954)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_09273.1
- **Function (MyGene.info)**: serpin family G member 1. This gene encodes a highly glycosylated plasma protein involved in the regulation of the complement cascade. Its encoded protein, C1 inhibitor, inhibits activated C1r and C1s of the first complement component and thus regulates complement activation. It is synthesized in the liver, and its deficiency is associated with hereditary angioneurotic oedema (HANE). Alternative splicing results in multipl…
- **Diseases (Open Targets)**: hereditary angioedema with C1Inh deficiency (0.828); hereditary angioedema type 1 (0.750); hereditary angioedema (0.728); angioedema (0.616); hereditary angioedema type 2 (0.614)
- **Europe PMC papers**: 4203
- **Why important**: SERPING1 is connected to TNC and AOC3 and has a strong STRING relationship with C3. It encodes the liver-synthesized C1 inhibitor, a circulating regulator of complement activation. It is represented with C3 and CP across multiple hu.MAP complexes (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1), and (hu.MAP huMAP3_10678.1), and with CP in (hu.MAP huMAP3_09273.1). HPA supports liver and hepatocyte association and immune-cell enhancement. Its disease associations are strongly centered on hereditary angioedema and C1-inhibitor deficiency, giving it a direct mechanistic and clinical link to complement control.
- **Conclusion**: Established evidence supports SERPING1 as the clearest complement-regulatory counterpart to C3 and as a likely marker of liver-derived circulating biology. The hypothesis that altered SERPING1 balance modulates the entire module requires direct measurements of complement activation products and inhibitor activity.

#### TNC

- **Related proteins** (co-abundance neighbors): SERPING1 (0.89), CP (0.85), C3 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tenascin C. This gene encodes an extracellular matrix protein with a spatially and temporally restricted tissue distribution. This protein is homohexameric with disulfide-linked subunits, and contains multiple EGF-like and fibronectin type-III domains. It is implicated in guidance of migrating neurons as well as axons during development, synaptic plasticity, and neuronal regeneration. [provided by RefSeq, Jul…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss (0.619); deafness (0.552); osteoarthritis, hip (0.551); total hip arthroplasty (0.468); Varicose veins (0.460)
- **Europe PMC papers**: 12274
- **Why important**: TNC is the most central node in the co-abundance graph, connecting SERPING1, CP, and C3. It is a secreted extracellular-matrix protein with domains associated with adhesion and tissue remodeling, and its annotations include cell growth, epithelial morphogenesis, wound response, neuronal guidance, synaptic plasticity, and neural regeneration. HPA associates it with blood vessels, smooth muscle, and several stromal or secretory cell types, while showing no immune-cell detection. It has extensive literature and disease associations involving hearing loss, osteoarthritis, and varicose veins.
- **Conclusion**: Established evidence supports TNC as an extracellular-matrix and vascular or stromal remodeling signal that may connect the complement-rich circulating core to tissue context. Its central network position is consistent with a co-abundance role, but it does not prove that TNC physically binds the other module proteins.

#### CP

- **Related proteins** (co-abundance neighbors): TNC (0.85); STRING partners: C3 (0.751)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_09273.1, huMAP3_08395.1
- **Function (MyGene.info)**: ceruloplasmin. The protein encoded by this gene is a metalloprotein that binds most of the copper in plasma and is involved in the peroxidation of Fe(II)transferrin to Fe(III) transferrin. Mutations in this gene cause aceruloplasminemia, which results in iron accumulation and tissue damage, and is associated with diabetes and neurologic abnormalities. Two transcript variants, one protein-coding and the other not…
- **Diseases (Open Targets)**: aceruloplasminemia (0.827); cerebellar ataxia (0.572); Hermansky-Pudlak syndrome 3 (0.564); Hermansky-Pudlak syndrome (0.543); neurodegeneration with brain iron accumulation (0.510)
- **Europe PMC papers**: 171928
- **Why important**: CP is a liver-enriched secreted plasma protein connected to TNC in the co-abundance graph and to C3 in STRING. It recurs with C3 and SERPING1 across the hu.MAP complex set (hu.MAP huMAP3_09531.1) through (hu.MAP huMAP3_08395.1). Its established function in copper binding, iron oxidation, iron homeostasis, and oxidant detoxification adds a metal-handling and redox dimension to the complement interpretation. Its disease associations include aceruloplasminemia, neurodegeneration with brain iron accumulation, and cerebellar ataxia, and it has a very extensive literature base.
- **Conclusion**: Established evidence supports CP as a circulating liver-derived metal and oxidative-homeostasis component that is already linked to the complement core in interaction and complex resources. It is a plausible indicator of redox or iron-related context, but the module does not establish that metal homeostasis is its principal shared-tissue driver.

#### AOC3

- **Related proteins** (co-abundance neighbors): C3 (0.83), SERPING1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: amine oxidase copper containing 3. This gene encodes a member of the semicarbazide-sensitive amine oxidase family. Copper amine oxidases catalyze the oxidative conversion of amines to aldehydes in the presence of copper and quinone cofactor. The encoded protein is localized to the cell surface, has adhesive properties as well as monoamine oxidase activity, and may be involved in leukocyte trafficking. Alterations in levels of the e…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.265); metabolic syndrome (0.220); neoplasm (0.105); cancer (0.102); diabetes mellitus (0.089)
- **Europe PMC papers**: 1367
- **Why important**: AOC3 connects C3 and SERPING1 in the abundance network, placing it as a bridge between complement-associated proteins despite having no reported STRING partners or hu.MAP representation in the supplied evidence. Its established functions include copper-dependent amine oxidation, cell adhesion, inflammatory response, and possible leukocyte trafficking. HPA associates it with adipose tissue, blood vessels, adipocytes, hepatic stellate cells, pericytes, and other stromal cell types. Its disease associations include type two diabetes and metabolic syndrome, with a more modest literature volume than the other selected genes.
- **Conclusion**: Established evidence supports AOC3 as a vascular, stromal, adhesive, and amine-metabolism marker that may provide tissue context for the complement core. Its bridge position is biologically suggestive but less independently validated than the C3, CP, and SERPING1 relationships, so its proposed mechanistic role remains a hypothesis.

## Module 4

**Tissue pair**: cerebrospinal_fluid and liver  
**Genes (6)**: CD163, COL6A1, COL6A3, FGA, LRP1, HSPG2

### Function

The module is most consistent with an extracellular-matrix and tissue-interface program rather than a narrowly defined enzymatic pathway. HSPG2 encodes perlecan, an extracellular-matrix proteoglycan that binds and cross-links matrix and cell-surface molecules. COL6A1 and COL6A3 encode collagen VI chains, supporting a connective-tissue structural component. FGA represents a blood-clotting and cell-matrix-adhesion component, while CD163 and LRP1 support macrophage-associated clearance, endocytosis, lipid handling, and inflammatory regulation. No GO or KEGG term passed global correction, so no GO or KEGG pathway can be called significantly enriched. The absence of a globally significant term does not invalidate the module; the gene-level annotations and network structure instead support a mixed matrix, vascular, hepatic, and clearance-related interpretation.

**Cell composition.** All module proteins are annotated as secreted or extracellularly associated in the HPA summary. HSPG2, COL6A1, and COL6A3 point toward extracellular matrix and stromal biology; FGA is a blood-secreted liver product; CD163 is a monocyte and macrophage marker; and LRP1 is a membrane and intracellular clearance receptor with enrichment in adipocytes, fibroblasts, hepatocytes, and monocyte-related populations. HPA cell-type evidence repeatedly points to fibroblasts, fibro-adipogenic progenitors, hepatic stellate cells, hepatocytes, and macrophage or monocyte populations. Thus, this shared cerebrospinal-fluid and liver module may reflect extracellular or blood-derived proteins, vascular or stromal material, and shared cell-type contributions rather than a liver-specific or cerebrospinal-fluid-specific intracellular program. The HPA summary reports no matching cerebrospinal-fluid tissue protein measurements, so the cerebrospinal-fluid protein interpretation is not independently supported by that tissue-level assay. Liver protein detection is present for only part of the module, further favoring caution about assigning the whole module to hepatocytes.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known STRING relationship is between COL6A1 and COL6A3, which is biologically concordant with their role as collagen VI chains. STRING also supports a relationship between HSPG2 and LRP1, consistent with an extracellular-matrix and receptor-mediated clearance interface. The remaining co-abundance edges are not supported by high-confidence STRING relationships in the fact sheet, so co-abundance should not be interpreted as proof of direct physical interaction. No hu.MAP complex contains multiple module members. Overall, the network combines a known collagen relationship, a known matrix-receptor relationship, and additional sample-level co-abundance links that may arise from shared tissue, extracellular-fluid, vascular, or cellular composition.

**STRING interactions (score >= 0.7)**: 2 of 15 gene pairs: COL6A1–COL6A3 (0.994); HSPG2–LRP1 (0.809)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This cannot be established as a new biological pathway from the supplied evidence. The collagen VI relationship and the HSPG2-LRP1 relationship are already represented in STRING, and the individual functions of the genes are established. The potentially novel aspect is the coordinated co-abundance of this particular extracellular-matrix, coagulation, macrophage-clearance, and receptor set across cerebrospinal fluid and liver. However, absence of a corresponding hu.MAP complex or absence of other STRING links does not prove novelty. The most defensible conclusion is that the cross-tissue module may be a previously uncharacterized co-abundance pattern, while its component biology is largely established.

**Hypothesis.** Hypothesis: the module captures a shared extracellular-fluid and tissue-remodeling state linking stromal matrix production, vascular or basement-membrane organization, hepatic fibrinogen supply, and macrophage or receptor-mediated clearance. In liver, hepatic stellate, stromal, hepatocyte, and Kupffer-cell contributions could generate the coordinated signal. In cerebrospinal fluid, extracellular matrix or vascular material, blood-derived fibrinogen, and soluble or shed receptor-associated material could produce a related abundance pattern. This hypothesis predicts that the module will track sample blood or stromal content and tissue injury or remodeling more strongly than a single canonical intracellular pathway. It requires validation with cell deconvolution, matched plasma measurements, orthogonal protein assays, and perturbation or longitudinal data.

### Important genes

#### HSPG2

- **Related proteins** (co-abundance neighbors): COL6A1 (0.90), LRP1 (0.86), CD163 (0.85), COL6A3 (0.81), FGA (0.80); STRING partners: LRP1 (0.809)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 is the most connected module member in the supplied co-abundance graph and links the collagen, receptor, macrophage-associated, and fibrinogen-related portions of the module. Its perlecan product is a multidomain extracellular-matrix proteoglycan that binds matrix and cell-surface molecules. HPA places it in a blood-vessel-associated pattern and in fibro-adipogenic and hepatic-stellate-related cell contexts. It also has substantial literature and disease associations, making it a strong candidate for the module's extracellular scaffold.
- **Conclusion**: Established evidence supports HSPG2 as a central extracellular-matrix organizer and as a plausible bridge between stromal structure and receptor-mediated clearance. It is a strong network anchor. It is not established that HSPG2 causally drives the cross-tissue co-abundance pattern; that role remains a hypothesis.

#### COL6A1

- **Related proteins** (co-abundance neighbors): HSPG2 (0.90), FGA (0.83), COL6A3 (0.81); STRING partners: COL6A3 (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is a structural collagen VI chain and is connected in the module to HSPG2, COL6A3, and FGA. Its strongest STRING relationship is with COL6A3, matching the known collagen VI assembly context. HPA associates it with fibroblasts, fibro-adipogenic progenitors, and stromal cell populations. It has extensive literature and established associations with collagen-related myopathies.
- **Conclusion**: Established evidence supports COL6A1 as a marker and structural component of connective-tissue matrix, with the COL6A1-COL6A3 relationship providing a biologically interpretable part of the module. The module does not establish that collagen VI production is the initiating event or that the signal reflects active fibrosis.

#### COL6A3

- **Related proteins** (co-abundance neighbors): COL6A1 (0.81), CD163 (0.81), HSPG2 (0.81); STRING partners: COL6A1 (0.994)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 3 chain. This gene encodes the alpha-3 chain, one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The alpha-3 chain of type VI collagen is much larger than the alpha-1 and -2 chains. This difference in size is largely due to an increase in the number of subdomains, similar to von Willebrand Factor type A domains, that are found in the amino termin…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy (0.766); dystonia 27 (0.764); Bethlem myopathy (0.758); Bethlem myopathy 1C (0.747); Bethlem myopathy 1A (0.718)
- **Europe PMC papers**: 5386
- **Why important**: COL6A3 is the second collagen VI component and is connected to COL6A1, HSPG2, and CD163. HPA links it to smooth muscle, fibroblasts, fibro-adipogenic progenitors, and hepatic stellate cells. Its disease associations and substantial literature support a role in connective-tissue organization and tissue remodeling.
- **Conclusion**: Established evidence supports COL6A3 as a matrix structural protein that reinforces the collagen VI interpretation and connects that interpretation to stromal and hepatic-stellate contexts. Its association with CD163 in the co-abundance graph may indicate shared macrophage-stromal composition, but it does not prove direct collagen VI regulation by macrophages.

#### CD163

- **Related proteins** (co-abundance neighbors): HSPG2 (0.85), COL6A3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD163 molecule. The protein encoded by this gene is a member of the scavenger receptor cysteine-rich (SRCR) superfamily, and is exclusively expressed in monocytes and macrophages. It functions as an acute phase-regulated receptor involved in the clearance and endocytosis of hemoglobin/haptoglobin complexes by macrophages, and may thereby protect tissues from free hemoglobin-mediated oxidative damage. This protein…
- **Diseases (Open Targets)**: arthropathy (0.205); acute tonsillitis (0.205); adolescent idiopathic scoliosis (0.193); stroke disorder (0.191); CINCA syndrome (0.185)
- **Europe PMC papers**: 31467
- **Why important**: CD163 is the clearest immune-cell marker in the module. It is associated with monocytes, macrophages, Kupffer cells, and Hofbauer cells, and its product mediates clearance and endocytosis of hemoglobin-haptoglobin complexes and can participate in innate immune responses. In the module it connects HSPG2 and COL6A3, potentially linking matrix abundance to macrophage or Kupffer-cell content. It also has the largest literature volume among the listed genes in the fact sheet.
- **Conclusion**: Established evidence supports CD163 as a macrophage and monocyte-associated clearance receptor and as a possible indicator of immune-cell composition in the samples. The module does not establish an inflammatory mechanism, macrophage activation state, or direct interaction between CD163 and the matrix proteins.

#### FGA

- **Related proteins** (co-abundance neighbors): COL6A1 (0.83), HSPG2 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibrinogen alpha chain. This gene encodes the alpha subunit of the coagulation factor fibrinogen, which is a component of the blood clot. Following vascular injury, the encoded preproprotein is proteolytically processed by thrombin during the conversion of fibrinogen to fibrin. Mutations in this gene lead to several disorders, including dysfibrinogenemia, hypofibrinogenemia, afibrinogenemia and renal amyloidosis. Alterna…
- **Diseases (Open Targets)**: familial dysfibrinogenemia (0.789); familial visceral amyloidosis (0.765); congenital afibrinogenemia (0.757); familial hypodysfibrinogenemia (0.659); congenital fibrinogen deficiency (0.619)
- **Europe PMC papers**: 7516
- **Why important**: FGA is a liver-enriched, hepatocyte-associated secreted blood protein involved in fibrinogen formation, coagulation, platelet activation, fibrinolysis, and cell-matrix adhesion. It connects to HSPG2 and COL6A1, providing a blood or vascular component to the otherwise matrix- and cell-associated module. Its disease associations and substantial literature are consistent with an important extracellular-fluid contribution.
- **Conclusion**: Established evidence supports FGA as a hepatocyte-derived circulating coagulation component and as a plausible indicator of blood or vascular material. Its co-abundance with matrix genes does not demonstrate direct binding or a coordinated coagulation response; sample composition and tissue injury are alternative explanations.

#### LRP1

- **Related proteins** (co-abundance neighbors): HSPG2 (0.86); STRING partners: HSPG2 (0.809)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LDL receptor related protein 1. This gene encodes a member of the low-density lipoprotein receptor family of proteins. The encoded preproprotein is proteolytically processed by furin to generate 515 kDa and 85 kDa subunits that form the mature receptor (PMID: 8546712). This receptor is involved in several cellular processes, including intracellular signaling, lipid homeostasis, and clearance of apoptotic cells. In addition, the …
- **Diseases (Open Targets)**: neurodegenerative disease (0.514); keratosis pilaris atrophicans (0.499); developmental dysplasia of the hip (0.466); Alzheimer disease (0.462); Parkinson disease (0.443)
- **Europe PMC papers**: 10645
- **Why important**: LRP1 is the receptor-side component of the HSPG2-LRP1 STRING relationship and is connected to lipid homeostasis, receptor-mediated endocytosis, phagocytosis, apoptotic-cell clearance, and inflammatory regulation. HPA places it in adipocyte, fibroblast, hepatocyte, Kupffer-cell, and monocyte-related contexts. It has extensive literature and disease associations, including neurodegenerative disease associations relevant to cerebrospinal-fluid studies.
- **Conclusion**: Established evidence supports LRP1 as a multifunctional clearance and signaling receptor that could connect extracellular matrix, lipid handling, and immune-cell biology. Its position as a peripheral module member makes it a plausible interface marker, but the module does not establish that LRP1 mediates the observed cross-tissue co-abundance.
