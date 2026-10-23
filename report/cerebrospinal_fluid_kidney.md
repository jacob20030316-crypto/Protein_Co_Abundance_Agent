# Conserved co-abundance modules: cerebrospinal_fluid and kidney

## Module 0

**Tissue pair**: cerebrospinal_fluid and kidney  
**Genes (5)**: A2M, ALB, APOA1, C3, HBA1

### Function

The strongest interpretation is a circulating blood-microparticle and plasma-protein module, supported by (GO:CC blood microparticle; q_global = 0.0494), which contains every module gene. Its biology combines complement and inflammatory regulation through C3, broad protease and cytokine control through A2M, lipid transport and HDL-related function through APOA1, plasma transport and osmotic-buffering functions through ALB, and erythrocyte oxygen, carbon-dioxide, and nitric-oxide transport through HBA1. The module therefore appears to represent extracellular blood-derived material rather than a coherent intracellular pathway operating specifically in cerebrospinal fluid or kidney. The network structure supports this interpretation: C3 is the most connected member and links A2M, APOA1, and HBA1, while APOA1 links C3 and ALB. HBA1 has no STRING-supported connection within the module and may reflect erythrocyte-derived material entering the measured protein pool rather than a functional interaction with the other proteins.

**Cell composition.** The composition strongly favors secreted and plasma-associated proteins. A2M, APOA1, ALB, and C3 are secreted to blood according to HPA, while ALB is described as the most abundant protein in human blood and APOA1 as a major HDL protein. HPA also assigns several genes to liver or hepatocyte enrichment, consistent with a circulating hepatic secretome. HBA1 is associated with erythrocytes, bone marrow, and lymphoid tissue and is not detected in kidney by the supplied HPA evidence, making blood-cell carryover or microparticle-associated hemoglobin a plausible contributor. The presence of C3-associated monocyte enrichment and several immune-cell associations does not establish a resident immune-cell module. Overall, the shared cerebrospinal-fluid and kidney signal may reflect common exposure to circulating plasma proteins, blood microparticles, vascular leakage, or shared sample-related material rather than shared tissue-cell biology.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 0.0494 | A2M, ALB, APOA1, C3, HBA1 |

### STRING and hu.MAP

STRING supports established relationships among the plasma proteins: A2M is linked to ALB, APOA1, and C3; ALB is linked to APOA1 and C3; and APOA1 is linked to C3. These relationships are consistent with known extracellular association or shared plasma biology, but STRING associations do not by themselves prove that the proteins form one physical complex in cerebrospinal fluid or kidney. HBA1 has no STRING partner in this module. hu.MAP provides broader complex-context evidence. The four proteins A2M, C3, APOA1, and ALB recur together across multiple hu.MAP complexes (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_10678.1), and related complexes, while HBA1 joins one larger complex with all of those proteins (hu.MAP huMAP3_15040.1). The repeated presence of many additional plasma, complement, coagulation, apolipoprotein, and acute-phase proteins in those complexes suggests that the module is a small projection of broad circulating-protein assemblies rather than a complete, tissue-specific molecular complex. The STRING and hu.MAP evidence therefore strengthens the interpretation as a known plasma-associated network, while also limiting claims that this particular five-gene arrangement is a newly discovered complex.

**STRING interactions (score >= 0.7)**: 5 of 10 gene pairs: A2M–ALB (0.98); A2M–APOA1 (0.998); ALB–APOA1 (0.998); ALB–C3 (0.959); APOA1–C3 (0.957)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Blood microparticle (FDR = 0.018, 5 genes); TISSUES Right atrium (FDR = 0.0188, 4 genes); TISSUES Left atrium (FDR = 0.0201, 4 genes); Component Blood microparticle (FDR = 0.0214, 5 genes); PMID (2023) Whartons jelly mesenchymal stem cells: a concise review of their secretome and prospective clinical applications. (FDR = 0.0268, 5 genes); PMID (2022) Serum alpha-1-antitrypsin level in the severity prognosis of systemic lupus erythematosus patients: Systematic exploration of novel biomarker. (FDR = 0.0268, 5 genes); PMID (2021) Apolipoprotein Signature of HDL and LDL from Atherosclerotic Patients in Relation with Carotid Plaque Typology: A Preliminary Report. (FDR = 0.0268, 5 genes); PMID (2019) Plasma Proteome Profiling to detect and avoid sample-related biases in biomarker studies. (FDR = 0.0268, 5 genes); PMID (2016) Proteomics reveals the effects of sustained weight loss on the human plasma proteome. (FDR = 0.0268, 5 genes); PMID (2024) Plasma proteome profiling reveals the therapeutic effects of the PPAR pan-agonist chiglitazar on insulin sensitivity, lipid metabolism, and inflammation in type 2 diabetes. (FDR = 0.034, 3 genes); PMID (2023) The biomarkers discovery of hyperuricemia and gout: proteomics and metabolomics. (FDR = 0.034, 3 genes); PMID (2023) Efficacy and safety of lenalidomide in HIV-associated cryptococcal meningitis patients with persistent intracranial inflammation: an open-label, single-arm, prospective interventional study. (FDR = 0.034, 4 genes); PMID (2023) Quantitative proteomic analysis of human serum using tandem mass tags to predict cardiovascular risks in patients with psoriasis. (FDR = 0.034, 4 genes); PMID (2023) Extracellular Vesicles as Potential Biomarkers in Amyotrophic Lateral Sclerosis. (FDR = 0.034, 3 genes); PMID (2023) Machine Learning-Based Urine Peptidome Analysis to Predict and Understand Mechanisms of Progression to Kidney Failure. (FDR = 0.034, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (A2M, C3, APOA1, ALB, HBA1; 5/64); huMAP3_08395.1 (A2M, C3, APOA1, ALB; 4/43); huMAP3_09531.1 (A2M, C3, APOA1, ALB; 4/47); huMAP3_10101.1 (A2M, C3, APOA1, ALB; 4/49); huMAP3_10678.1 (A2M, C3, APOA1, ALB; 4/71); huMAP3_07432.1 (C3, APOA1, ALB; 3/18); huMAP3_07265.1 (A2M, APOA1, ALB; 3/20); huMAP3_09434.1 (C3, APOA1, ALB; 3/33); huMAP3_08224.1 (C3, APOA1; 2/21)

### Novelty

This should not be presented as a new molecular pathway or a newly established protein complex. The individual functions of the genes, the dense known relationships among A2M, ALB, APOA1, and C3, the repeated hu.MAP membership, and the blood-microparticle enrichment all indicate substantial prior biological knowledge. The potentially interesting aspect is the conservation of this co-abundance pattern across cerebrospinal fluid and kidney, but the supplied evidence cannot determine whether that conservation reflects shared physiology, vascular exposure, blood contamination, microparticles, or a technical feature of protein measurement. Absence of a complete matching module in STRING or hu.MAP would not establish novelty, especially because those resources represent curated or predicted relationships rather than every tissue-specific abundance pattern. A defensible novelty claim would require comparison with published cross-tissue co-abundance modules, matched blood-contamination controls, and orthogonal validation of tissue origin.

**Hypothesis.** Hypothesis: the conserved module reflects a circulating blood-microparticle pool that enters or is sampled from both cerebrospinal fluid and kidney-associated material. Liver-derived ALB, APOA1, A2M, and C3 may travel together through plasma or extracellular particles, where they jointly represent transport, lipid handling, protease inhibition, and complement surveillance. HBA1 may mark an erythrocyte-derived component of the same sampled material. In kidney, filtration, vascular exposure, or local handling could preserve this abundance pattern; in cerebrospinal fluid, barrier permeability or blood-derived microparticles could do the same. This hypothesis predicts that the module will track plasma abundance and blood-protein contamination markers more closely than tissue-cell-specific expression, and that its apparent conservation will weaken after rigorous adjustment for blood-derived proteins and hemolysis.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): A2M (0.89), HBA1; HBA2 (0.81), APOA1 (0.80); STRING partners: ALB (0.959), APOA1 (0.957)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_08224.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is the central network member, connecting A2M, APOA1, and HBA1, and it participates in every listed hu.MAP complex containing multiple module members. It is the sole module gene with direct complement-centered functional annotation in the fact sheet, including complement activation, complement receptor signaling, and inflammatory response. Its disease associations include complement deficiency, complement glomerulopathy, atypical hemolytic-uremic syndrome, and age-related macular degeneration. It also has the largest literature volume among the module genes, making it the strongest anchor for interpreting inflammatory and complement-related biology.
- **Conclusion**: Established evidence supports C3 as a central complement and inflammatory plasma protein and as a major network hub in this module. The module does not establish that C3 is being locally activated in kidney or cerebrospinal fluid; its abundance may instead report circulating complement or blood-derived microparticles.

#### APOA1

- **Related proteins** (co-abundance neighbors): C3 (0.80), ALB (0.80); STRING partners: A2M (0.998), ALB (0.998), C3 (0.957)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08224.1
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is a highly connected module member linking C3 and ALB and recurring across nearly all of the listed hu.MAP complexes. It is a liver- and enterocyte-associated secreted protein, the major protein component of HDL, and a cofactor for cholesterol esterification. Its annotations connect the module to lipid transport, cholesterol efflux, immune regulation, and extracellular vesicles. It has substantial disease and literature support, including APOA1 deficiency and familial visceral amyloidosis.
- **Conclusion**: Established evidence supports APOA1 as the lipid-transport and HDL-related component of a circulating plasma module. Its presence does not demonstrate local HDL production by kidney or cerebrospinal-fluid cells; a shared blood-derived source is more consistent with the supplied HPA and network evidence.

#### ALB

- **Related proteins** (co-abundance neighbors): APOA1 (0.80); STRING partners: A2M (0.98), APOA1 (0.998), C3 (0.959)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB connects APOA1 in the module and is linked by STRING to A2M and C3. It recurs in many hu.MAP complexes and is a secreted liver-enriched protein with kidney immunohistochemical detection. Its carrier functions span hormones, fatty acids, metabolites, and drugs, while its abundance and plasma role make it a powerful marker of circulating protein content. Its disease associations include congenital analbuminemia, familial dysalbuminemic hyperthyroxinemia, hyperthyroidism, and chronic kidney disease.
- **Conclusion**: Established evidence supports ALB as a dominant circulating carrier and compositional marker rather than a specific mechanistic driver of the shared tissue module. Its kidney detection is compatible with tissue exposure or handling, but does not by itself prove kidney-specific synthesis or function in this network.

#### A2M

- **Related proteins** (co-abundance neighbors): C3 (0.89); STRING partners: ALB (0.98), APOA1 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07265.1
- **Function (MyGene.info)**: alpha-2-macroglobulin. The protein encoded by this gene is a protease inhibitor and cytokine transporter. It uses a bait-and-trap mechanism to inhibit a broad spectrum of proteases, including trypsin, thrombin and collagenase. It can also inhibit inflammatory cytokines, and it thus disrupts inflammatory cascades. Mutations in this gene are a cause of alpha-2-macroglobulin deficiency. This gene is implicated in Alzheimer…
- **Diseases (Open Targets)**: myopia (0.206); refractive error (0.151); primary angle-closure glaucoma (0.148); Abnormality of refraction (0.144); Aganglionic megacolon (0.118)
- **Europe PMC papers**: 5133
- **Why important**: A2M connects directly to the network hub C3 and has strong STRING links to ALB and APOA1. It is a secreted blood protein with protease-inhibitory and cytokine-transport functions and is annotated for negative regulation of complement activation. It occurs repeatedly in the hu.MAP complexes and provides a functional counterpoint to C3 by linking protease control, inflammatory regulation, and complement modulation. Its annotations also include a role in amyloid-beta clearance and degradation, which is relevant to cerebrospinal-fluid biology.
- **Conclusion**: Established evidence supports A2M as a circulating regulator of proteases, cytokines, and complement-related inflammation. Its cerebrospinal-fluid relevance is biologically plausible from its clearance annotation, but the supplied co-abundance evidence cannot distinguish local activity from passive delivery through blood-derived material.

#### HBA1

- **Related proteins** (co-abundance neighbors): none; STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: hemoglobin subunit alpha 1. The human alpha globin gene cluster located on chromosome 16 spans about 30 kb and includes seven loci: 5'- zeta - pseudozeta - mu - pseudoalpha-1 - alpha-2 - alpha-1 - theta - 3'. The alpha-2 (HBA2) and alpha-1 (HBA1) coding sequences are identical. These genes differ slightly over the 5' untranslated regions and the introns, but they differ significantly over the 3' untranslated regions. Two alp…
- **Diseases (Open Targets)**: alpha thalassemia spectrum (0.758); hemoglobin H disease (0.755); hemoglobin M disease (0.735); Heinz body anemia (0.698); primary familial polycythemia due to EPO receptor mutation (0.689)
- **Europe PMC papers**: 4551
- **Why important**: HBA1 is the module's erythrocyte-associated member and is the only gene without a STRING-supported partner in the supplied subgraph. It is included in (GO:CC blood microparticle; q_global = 0.0494) and in the large hu.MAP complex (hu.MAP huMAP3_15040.1), but HPA associates it primarily with erythrocytes, bone marrow, and lymphoid tissue and reports no kidney detection. Its annotated functions include oxygen, carbon-dioxide, and nitric-oxide transport, and its disease associations include alpha-thalassemia-spectrum disorders and hemoglobin variants.
- **Conclusion**: Established evidence supports HBA1 as an erythrocyte or blood-microparticle marker, not as a demonstrated interacting partner of the other module proteins. Its isolated network position makes blood-cell carryover, hemolysis, or erythrocyte-derived particles a particularly important alternative explanation for the shared module.

## Module 2

**Tissue pair**: cerebrospinal_fluid and kidney  
**Genes (8)**: SERPINC1, COL18A1, LAMA5, HSPG2, GM2A, SELENBP1, GC, VTN

### Function

The module is best interpreted as an extracellular matrix, basement-membrane, and circulating protein interface with links to vascular structure, cell adhesion, protease regulation, vitamin transport, and lipid handling. The strongest coherent substructure is the COL18A1–HSPG2–VTN axis, supported by high-confidence STRING relationships and by the extracellular-matrix annotations for COL18A1, HSPG2, and LAMA5. SERPINC1 and VTN add extracellular protease and adhesion-related functions, while GC contributes vitamin-D transport and is connected to SERPINC1 in STRING. GM2A provides a vesicular lipid-catabolism component, and SELENBP1 is less clearly integrated functionally. No GO or KEGG term passed global correction, so these functional interpretations are annotation- and network-based rather than evidence of significantly enriched GO or KEGG categories.

**Cell composition.** This is predominantly a secreted or extracellular module rather than a canonical intracellular housekeeping module. The HPA evidence indicates that most members are secreted, with several assigned to blood or extracellular matrix. Liver and hepatocyte enrichment is prominent, and vascular or basement-membrane expression is also represented. Most members were not detected as immune-cell specific, so the module is not primarily a blood-cell module, although immune-cell enhancement for COL18A1, SELENBP1, and GM2A leaves open a contribution from cellular admixture. The shared cerebrospinal-fluid and kidney signal could therefore reflect circulating plasma proteins, vascular or basement-membrane material, and shared barrier-related biology rather than a module produced uniformly by kidney and cerebrospinal-fluid cells. HPA protein detection is available for kidney but not for cerebrospinal fluid in this summary.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a connected extracellular subnetwork: COL18A1 connects with HSPG2 and VTN, HSPG2 connects with VTN, and SERPINC1 connects strongly with VTN and with GC. These are already known or database-supported relationships, so the module is not an entirely unexpected collection of proteins. The remaining co-abundance links, especially SELENBP1 and GM2A in relation to the extracellular proteins, have weaker direct functional support from the supplied STRING results. hu.MAP places SERPINC1 and GC together in complex C1, but they represent only a small part of a much larger plasma-protein-associated complex; this supports a shared circulating-protein context, not a claim that all module members form one physical complex. No hu.MAP complex was supplied for the other module members.

**STRING interactions (score >= 0.7)**: 5 of 28 gene pairs: COL18A1–HSPG2 (0.894); COL18A1–VTN (0.752); GC–SERPINC1 (0.84); HSPG2–VTN (0.797); SERPINC1–VTN (0.949)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINC1, GC; 2/64)

### Novelty

The exact conserved co-abundance module may be a new observation because the supplied evidence does not identify a previously reported cerebrospinal-fluid–kidney module containing this precise combination. However, its component biology is not new: COL18A1, HSPG2, VTN, LAMA5, SERPINC1, GC, and GM2A have established functions, disease associations, or literature support, and several pairwise relationships are already represented in STRING or hu.MAP. Consequently, the defensible claim is novelty of the cross-tissue co-abundance pattern or its particular organization, not novelty of the genes, their functions, or all of their interactions. The absence of a complete module from STRING or hu.MAP cannot by itself establish novelty.

**Hypothesis.** Hypothesis: the conserved signal reflects a blood-facing vascular and basement-membrane compartment shared by kidney and cerebrospinal-fluid samples. In this model, COL18A1, HSPG2, and LAMA5 provide matrix and barrier scaffolding; VTN coordinates matrix adhesion and migration; SERPINC1 restrains extracellular proteolysis; GC transports vitamin-D-related metabolites; and GM2A contributes vesicular lipid processing. Their coordinated abundance could arise from leakage, transport, or remodeling of vascular and extracellular-matrix material into both sample types, with liver-derived circulating proteins strengthening the shared signal. SELENBP1 may mark a linked metabolic or tissue-state component, but its mechanistic placement in the module remains uncertain. This hypothesis requires validation with cell-resolved measurements, plasma or cerebrospinal-fluid protein quantification, and orthogonal assays of vascular-barrier or matrix remodeling.

### Important genes

#### COL18A1

- **Related proteins** (co-abundance neighbors): VTN (0.90), SERPINC1 (0.85), GM2A (0.82); STRING partners: HSPG2 (0.894), VTN (0.752)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type XVIII alpha 1 chain. This gene encodes the alpha chain of type XVIII collagen. This collagen is one of the multiplexins, extracellular matrix proteins that contain multiple triple-helix domains (collagenous domains) interrupted by non-collagenous domains. A long isoform of the protein has an N-terminal domain that is homologous to the extracellular part of frizzled receptors. Proteolytic processing at several endogeno…
- **Diseases (Open Targets)**: Knobloch syndrome 1 (0.778); Knobloch syndrome (0.700); hereditary glaucoma, primary closed-angle (0.593); Dupuytren Contracture (0.587); severe early-childhood-onset retinal dystrophy (0.501)
- **Europe PMC papers**: 5223
- **Why important**: COL18A1 has the strongest network position in the module and connects to VTN, SERPINC1, and GM2A. It is a secreted extracellular-matrix collagen with links to angiogenesis, endothelial morphogenesis, and neurodevelopment. Its kidney detection, blood-vessel enhancement, and substantial literature support make it a strong structural and vascular anchor.
- **Conclusion**: Established evidence supports COL18A1 as an extracellular-matrix and vascular-barrier component with relevance to angiogenesis and disease. Hypothesis: it may help couple the matrix subnetwork to the shared cerebrospinal-fluid and kidney signal, but the co-abundance data do not prove that it drives the module.

#### VTN

- **Related proteins** (co-abundance neighbors): COL18A1 (0.90), HSPG2 (0.88); STRING partners: COL18A1 (0.752), HSPG2 (0.797), SERPINC1 (0.949)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vitronectin. The protein encoded by this gene functions in part as an adhesive glycoprotein. Differential expression of this protein can promote either cell adhesion or migration as it links cells to the extracellular matrix through a variety of ligands. These ligands include integrins, plasminogen activator inhibitor-1, and urokinase plasminogen activator receptor. This secreted protein can be present in the …
- **Diseases (Open Targets)**: hypertensive disorder (0.421); dengue disease (0.376); neurodegenerative disease (0.343); temporal arteritis (0.338); age-related macular degeneration (0.313)
- **Europe PMC papers**: 3940
- **Why important**: VTN is a central connector of the extracellular subnetwork, linking COL18A1, HSPG2, and SERPINC1 with strong STRING support. It is a secreted liver-enriched adhesive glycoprotein involved in cell-matrix adhesion, integrin signaling, and migration, and it is detected in kidney.
- **Conclusion**: Established evidence supports VTN as a plausible extracellular organizing protein connecting adhesion, matrix, and protease-regulatory biology. Hypothesis: VTN may act as the principal bridge between the matrix and circulating-protein portions of the module.

#### HSPG2

- **Related proteins** (co-abundance neighbors): LAMA5 (0.91), VTN (0.88); STRING partners: COL18A1 (0.894), VTN (0.797)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 links VTN with LAMA5 and is a basement-membrane proteoglycan that cross-links extracellular-matrix and cell-surface molecules. Its blood-vessel enhancement and kidney detection fit a vascular or filtration-barrier interpretation, while its disease associations provide additional biological relevance.
- **Conclusion**: Established evidence supports HSPG2 as a basement-membrane scaffold with roles in adhesion, signaling, and tissue organization. Hypothesis: it could provide the matrix framework that allows the module to be shared between kidney and cerebrospinal-fluid-associated vascular interfaces.

#### SERPINC1

- **Related proteins** (co-abundance neighbors): SELENBP1 (0.96), COL18A1 (0.85); STRING partners: GC (0.84), VTN (0.949)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 is a liver-enriched secreted plasma protein with a direct role in regulating coagulation. It connects to VTN, COL18A1, SELENBP1, and GC in the supplied network evidence and also participates with GC in hu.MAP complex C1. Its disease associations connect the module to antithrombin deficiency and thrombotic disorders.
- **Conclusion**: Established evidence supports SERPINC1 as a circulating coagulation regulator and as a contributor to the plasma-protein context of the module. Hypothesis: its co-abundance may report vascular-interface exposure or barrier disturbance rather than local production by kidney or cerebrospinal-fluid cells.

#### GC

- **Related proteins** (co-abundance neighbors): SELENBP1 (0.87); STRING partners: SERPINC1 (0.84)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: GC vitamin D binding protein. The protein encoded by this gene belongs to the albumin gene family. It is a multifunctional protein found in plasma, ascitic fluid, cerebrospinal fluid and on the surface of many cell types. It binds to vitamin D and its plasma metabolites and transports them to target tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq,…
- **Diseases (Open Targets)**: vitamin D deficiency (0.574); vitamin deficiency (0.552); chronic obstructive pulmonary disease (0.499); squamous cell carcinoma (0.339); central nervous system cancer (0.334)
- **Europe PMC papers**: 363974
- **Why important**: GC is connected to SERPINC1 and is one of the two module members in hu.MAP complex C1. It is liver-enriched, detected in kidney, and encodes a multifunctional plasma and cerebrospinal-fluid protein that transports vitamin-D-related metabolites. Its exceptionally large literature base makes its biological identity especially well established.
- **Conclusion**: Established evidence supports GC as a circulating transport protein that can occur in cerebrospinal fluid and plasma and that links the module to vitamin-D biology. Hypothesis: GC may help explain conservation across the two sample types through shared extracellular transport rather than through a kidney-specific cellular program.

## Module 3

**Tissue pair**: cerebrospinal_fluid and kidney  
**Genes (11)**: ALCAM, CD44, ECE1, EGFR, FAM3C, HSPA13, ICAM1, MCAM, SIRPA, SUMF1, TFRC

### Function

The module is best interpreted as a cell-surface adhesion and receptor-signaling module with an immune-interface component. ALCAM, CD44, ICAM1, MCAM, and SIRPA support cell-cell or cell-matrix adhesion and leukocyte interaction, while EGFR provides a receptor-tyrosine-kinase signaling axis. TFRC adds receptor-mediated endocytosis and iron uptake, and ECE1 adds proteolytic processing of endothelin precursors and signaling related to vascular regulation. SUMF1 and ECE1 also point to intracellular enzyme maturation and lysosomal biology through the hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). No GO/KEGG term passed global correction, so these functional interpretations are based on the annotated genes, network structure, STRING relationships, hu.MAP evidence, and HPA context rather than on globally significant pathway enrichment.

**Cell composition.** The module is not a uniformly tissue-specific kidney or cerebrospinal-fluid program. Most members have low tissue specificity or enhancement in tissues outside kidney and cerebrospinal fluid, and several are secreted to blood or secreted in other tissues. HPA shows broad kidney protein detection for the module, but the single-cell pattern is especially notable for monocytes, neutrophils, macrophages, and related myeloid populations. Several members also have immune-cell enhancement or blood-cell enrichment, including ALCAM, ECE1, TFRC, ICAM1, SIRPA, and FAM3C. This composition makes shared blood exposure, vascular or myeloid-cell contribution, and common cell-type admixture plausible explanations for the cross-tissue module. It does not establish that the module is an artifact, because kidney cells and vascular or immune interfaces can genuinely express these proteins.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a compact adhesion and receptor-signaling subnetwork. The strongest known relationships include CD44 with EGFR and ICAM1, together with links among ALCAM, EGFR, ICAM1, and TFRC; CD44 also connects to ALCAM and MCAM. These relationships are concentrated around CD44 and EGFR and provide independent support for a biologically connected membrane-signaling neighborhood rather than random co-abundance. There was no STRING functional-enrichment result. hu.MAP contributes a different type of evidence: ECE1 and SUMF1 co-occur as module members in both (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), but each complex contains many proteins outside the module. Thus, the hu.MAP result supports a shared intracellular processing or lysosomal context for ECE1 and SUMF1, not a complete reconstruction of either complex from this module.

**STRING interactions (score >= 0.7)**: 8 of 55 gene pairs: ALCAM–CD44 (0.859); ALCAM–EGFR (0.708); ALCAM–ICAM1 (0.755); CD44–EGFR (0.998); CD44–ICAM1 (0.995); CD44–MCAM (0.7); EGFR–ICAM1 (0.877); EGFR–TFRC (0.832)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (ECE1, SUMF1; 2/60); huMAP3_09327.1 (ECE1, SUMF1; 2/93)

### Novelty

The module-level finding may be novel as a conserved co-abundance pattern across cerebrospinal fluid and kidney, but the available evidence does not justify calling it a newly discovered molecular complex or pathway. Several relationships are already represented in STRING, especially the CD44-centered adhesion and receptor network, and ECE1-SUMF1 membership is represented in hu.MAP (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). At the same time, the particular cross-tissue co-abundance organization is not directly established by those resources, and the module has no STRING enrichment and no globally significant GO/KEGG term. The cautious conclusion is that the arrangement may be a new systems-level observation built from partly known biology, requiring replication and comparison with blood-cell abundance, vascular markers, and independent proteomic cohorts.

**Hypothesis.** Hypothesis: the module reflects a shared vascular or myeloid-associated membrane program present in both sample types. A CD44-ALCAM-ICAM1 adhesion interface may couple to EGFR signaling, while TFRC-linked endocytosis and ECE1-dependent peptide processing provide supporting receptor-trafficking and vascular-signaling functions. The ECE1-SUMF1 association may represent a parallel intracellular processing or lysosomal component. Under this hypothesis, the apparent conservation between cerebrospinal fluid and kidney is driven partly by common blood-derived or immune-cell contributions and partly by genuine expression at tissue interfaces. This remains a hypothesis because the enrichment analysis provides no globally significant GO/KEGG term, the HPA cerebrospinal-fluid protein comparison has no matching data, and co-abundance does not demonstrate physical interaction or causal regulation.

### Important genes

#### CD44

- **Related proteins** (co-abundance neighbors): ECE1 (0.93), EGFR (0.91), ALCAM (0.90), TFRC (0.86), ICAM1 (0.83), SIRPA (0.81); STRING partners: ALCAM (0.859), EGFR (0.998), ICAM1 (0.995), MCAM (0.7)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD44 molecule (IN blood group). The protein encoded by this gene is a cell-surface glycoprotein involved in cell-cell interactions, cell adhesion and migration. It is a receptor for hyaluronic acid (HA) and can also interact with other ligands, such as osteopontin, collagens, and matrix metalloproteinases (MMPs). This protein participates in a wide variety of cellular functions including lymphocyte activation, recirculation and …
- **Diseases (Open Targets)**: nephrolithiasis, calcium oxalate (0.523); calcium oxalate urolithiasis (0.521); uterine corpus leiomyoma (0.480); systemic lupus erythematosus (0.467); autoimmune disease (0.330)
- **Europe PMC papers**: 102058
- **Why important**: CD44 is a topological hub in the module and has extensive known STRING connectivity to EGFR, ICAM1, ALCAM, and MCAM. Its established functions include hyaluronan-mediated cell interaction, cell adhesion, cell-matrix adhesion, migration, inflammatory response, lymphocyte trafficking, and hematopoietic regulation. HPA places it at the plasma membrane, with enhancement in monocytes, neutrophils, and other immune-related cell types, and it is detected in kidney. It is also the most extensively studied member among the selected genes, with broad disease associations including kidney stone disease and autoimmune disease.
- **Conclusion**: Established: CD44 is the strongest candidate for the module's adhesion and immune-interface center. Hypothesis: CD44 may organize the observed cross-tissue signal by coupling extracellular matrix or hyaluronan interactions to EGFR and ICAM1 signaling, possibly with an important contribution from myeloid or blood-associated material.

#### ALCAM

- **Related proteins** (co-abundance neighbors): TFRC (0.92), CD44 (0.90), FAM3C (0.89), EGFR (0.86), ECE1 (0.84), MCAM (0.84); STRING partners: CD44 (0.859), EGFR (0.708), ICAM1 (0.755)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: activated leukocyte cell adhesion molecule. This gene encodes activated leukocyte cell adhesion molecule (ALCAM), also known as CD166 (cluster of differentiation 166), which is a member of a subfamily of immunoglobulin receptors with five immunoglobulin-like domains (VVC2C2C2) in the extracellular domain. This protein binds to T-cell differentiation antigene CD6, and is implicated in the processes of cell adhesion and migration. Multiple al…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.458); mathematical ability (0.453); open-angle glaucoma (0.396); restless legs syndrome (0.379); ovarian dysfunction (0.362)
- **Europe PMC papers**: 4212
- **Why important**: ALCAM is a topological hub with connections to TFRC, CD44, FAM3C, EGFR, ECE1, and MCAM, and it has STRING support for relationships with CD44, EGFR, and ICAM1. Its established biology concerns activated leukocyte cell adhesion, heterophilic cell-cell adhesion, migration, and neuronal projection or axon guidance. HPA identifies it as secreted to blood, enriched in parathyroid tissue, enhanced in myeloid dendritic cells, and detected in kidney. Its disease and trait associations span skeletal abnormalities, glaucoma, restless legs syndrome, and ovarian dysfunction, while its literature is substantial.
- **Conclusion**: Established: ALCAM is a plausible adhesion and intercellular-contact hub linking the module's immune, vascular, and tissue-interface signals. Hypothesis: ALCAM may help bridge CD44-centered adhesion with ECE1, EGFR, and TFRC-associated signaling in the conserved co-abundance pattern.

#### EGFR

- **Related proteins** (co-abundance neighbors): CD44 (0.91), ALCAM (0.86), ECE1 (0.84); STRING partners: ALCAM (0.708), CD44 (0.998), ICAM1 (0.877), TFRC (0.832)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus, Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: epidermal growth factor receptor. The protein encoded by this gene is a transmembrane glycoprotein that is a member of the protein kinase superfamily. This protein is a receptor for members of the epidermal growth factor family. EGFR is a cell surface protein that binds to epidermal growth factor, thus inducing receptor dimerization and tyrosine autophosphorylation leading to cell proliferation. Mutations in this gene are associat…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.850); lung adenocarcinoma (0.774); cancer (0.737); head and neck squamous cell carcinoma (0.725); lung cancer (0.717)
- **Europe PMC papers**: 223694
- **Why important**: EGFR is a central signaling receptor in the module and has STRING relationships with CD44, ICAM1, ALCAM, and TFRC. Its established function is ligand-induced receptor dimerization and tyrosine autophosphorylation, with downstream MAPK, phosphorylation, cell-surface receptor signaling, and cell proliferation effects. HPA shows plasma-membrane and Golgi localization, tissue enhancement in placenta, enhancement in several epithelial or progenitor cell types, and kidney detection. EGFR has a very large literature and strong disease associations with lung cancer and other carcinomas.
- **Conclusion**: Established: EGFR provides a credible signaling output for the adhesion-centered network and is supported by several known STRING relationships. Hypothesis: EGFR may convert adhesion or inflammatory contacts into growth, repair, or stress-response signaling in kidney or vascular-interface cells, although the module alone cannot establish activation.

#### ECE1

- **Related proteins** (co-abundance neighbors): CD44 (0.93), SUMF1 (0.89), ALCAM (0.84), EGFR (0.84), TFRC (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: endothelin converting enzyme 1. The protein encoded by this gene is involved in proteolytic processing of endothelin precursors to biologically active peptides. Mutations in this gene are associated with Hirschsprung disease, cardiac defects and autonomic dysfunction. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: Hirschsprung disease (0.591); neurodegenerative disease (0.362); Alzheimer disease (0.332); lysosomal storage disease (0.325); Parkinson disease (0.325)
- **Europe PMC papers**: 5314
- **Why important**: ECE1 is a connector between the adhesion-receptor portion of the network and the hu.MAP-supported intracellular component. It connects to CD44, ALCAM, EGFR, TFRC, and SUMF1 in the co-abundance graph, while its annotated function is proteolytic processing of endothelin precursors, with roles in proteolysis, endothelin-related blood-pressure regulation, receptor recycling, and axon guidance. HPA shows low tissue specificity, neutrophil enrichment, immune enhancement, and kidney detection. Its disease associations include Hirschsprung disease, cardiac defects, autonomic dysfunction, and neurodegenerative or lysosomal-storage disease contexts.
- **Conclusion**: Established: ECE1 is a biologically plausible vascular and proteolytic connector and is the module member most directly linked to SUMF1 in hu.MAP (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Hypothesis: ECE1 may connect endothelin or receptor-trafficking biology to the CD44-EGFR adhesion network, with neutrophil or vascular contributions helping explain conservation across the two sample types.

#### TFRC

- **Related proteins** (co-abundance neighbors): ALCAM (0.92), CD44 (0.86), HSPA13 (0.81), ECE1 (0.80); STRING partners: EGFR (0.832)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes, Lysosomes; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transferrin receptor. This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: TFRC-related combined immunodeficiency (0.623); type 2 diabetes mellitus (0.518); mucopolysaccharidosis type 2 (0.490); diabetes mellitus (0.471); diabetic retinopathy (0.343)
- **Europe PMC papers**: 14164
- **Why important**: TFRC occupies an intermediate network position linking ALCAM, CD44, HSPA13, and ECE1, and it has a known STRING relationship with EGFR. Its established role is transferrin-dependent iron uptake through receptor-mediated endocytosis, with functions in iron homeostasis, erythropoiesis, neurological development, cell growth, hypoxia response, and acute-phase biology. HPA places it in endosomes and lysosomes, with enhancement in erythrocyte progenitors, macrophages, monocytes, and syncytiotrophoblasts, and kidney detection. Its disease associations include combined immunodeficiency, diabetes, and mucopolysaccharidosis, and its literature is substantial.
- **Conclusion**: Established: TFRC adds an endocytic and iron-handling dimension to the otherwise adhesion and signaling-focused module and supports a blood-cell or myeloid interpretation. Hypothesis: TFRC may mark coordinated receptor internalization or cellular stress within the shared module rather than being a specific driver of the adhesion program.
