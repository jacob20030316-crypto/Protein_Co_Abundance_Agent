# Conserved co-abundance modules: autonomic_nervous_system and cerebrospinal_fluid

## Module 0

**Tissue pair**: autonomic_nervous_system and cerebrospinal_fluid  
**Genes (12)**: GOT1, PAM, SERPINC1, ATP1B1, HSPA5, CPD, F5, PENK, CRABP1, SCG2, SIL1, GC

### Function

This module does not have any GO or KEGG term passing global correction; therefore, no pathway-level annotation can be claimed as primary enrichment. Its gene composition instead suggests a mixed secretory and extracellular-fluid-associated program, combining coagulation and plasma-protein biology through SERPINC1 and F5, vitamin-D transport through GC, neuroendocrine peptide production and secretion through PENK, SCG2 and PAM, ER protein-folding support through HSPA5 and SIL1, and cellular transport or metabolic functions through ATP1B1, GOT1, CRABP1 and CPD. The network has several relatively central genes linking these otherwise distinct biological themes. Thus, the safest interpretation is a co-abundance signature of secreted plasma proteins, neuroendocrine material and supporting cellular proteins rather than a demonstrated single molecular pathway. The absence of globally significant GO or KEGG terms does not invalidate the module.

**Cell composition.** The module is strongly compatible with extracellular-fluid or blood-related composition. Most of its genes are secreted or associated with secreted products, including SERPINC1, F5, GC, PENK, SCG2 and PAM. HPA annotations emphasize liver and hepatocyte expression for SERPINC1 and GC, liver and choroid plexus expression for F5, and brain, adrenal or neuroendocrine expression for PENK and SCG2. Several genes also show blood-cell associations, especially F5 and CPD, although other members are not detected in immune cells or have low immune-cell specificity. The hu.MAP complex containing SERPINC1 and GC is dominated by plasma, complement, coagulation and transport proteins, which supports the possibility that the shared signal reflects circulating proteins, blood exposure or sample cellular composition. The HPA summary does not provide matched autonomic-nervous-system or cerebrospinal-fluid protein-detection measurements, so direct tissue-level protein localization in these two sample groups cannot be established from this evidence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The high-confidence STRING relationships are F5 with SERPINC1, GC with SERPINC1, and HSPA5 with SIL1. The first two are biologically coherent links within plasma coagulation and transport biology, while the HSPA5-SIL1 relationship supports an established ER chaperone and nucleotide-exchange-factor partnership. The hu.MAP result (hu.MAP huMAP3_15040.1) independently places SERPINC1 and GC in a large complex enriched for plasma, coagulation, complement, apolipoprotein and extracellular proteins. Most other co-abundance edges lack corresponding high-confidence STRING or hu.MAP support. Consequently, the module contains a small core of already known molecular relationships embedded within a broader statistical co-abundance structure; its edges should not generally be interpreted as direct physical interactions.

**STRING interactions (score >= 0.7)**: 3 of 66 gene pairs: F5–SERPINC1 (0.817); GC–SERPINC1 (0.84); HSPA5–SIL1 (0.998)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINC1, GC; 2/64)

### Novelty

This may be a novel conserved co-abundance association between autonomic nervous system and cerebrospinal fluid, but it is not evidence for a newly discovered protein complex or pathway. The known STRING links and the hu.MAP association between SERPINC1 and GC show that part of the signal recapitulates established plasma and ER biology. The lack of STRING functional enrichment and the absence of broad complex support make a fully unified mechanism uncertain. Absence from STRING or hu.MAP cannot prove novelty, because those resources are incomplete and are designed mainly around physical or curated functional relationships. A defensible novelty claim is therefore limited to the cross-tissue co-abundance pattern, which would require independent cohorts, adjustment for blood and cell-type composition, and targeted validation.

**Hypothesis.** Hypothesis: the shared module reflects a circulating or cerebrospinal-fluid-accessible secretory milieu that combines liver-derived coagulation and vitamin-D transport proteins with neuroendocrine secretory products and a smaller intracellular protein-homeostasis component. SERPINC1 and GC may form part of the extracellular-fluid-associated core, while PENK, SCG2 and PAM may report neuroendocrine vesicle activity; HSPA5 and SIL1 may indicate secretory-pathway or ER proteostasis in contributing cells. This model predicts that the module will be sensitive to blood admixture, barrier permeability, tissue injury or differences in neuroendocrine and hepatic contribution, rather than representing one intracellular pathway operating uniformly in every module-containing cell.

### Important genes

#### SERPINC1

- **Related proteins** (co-abundance neighbors): GOT1 (0.93), HSPA5 (0.93), SCG2 (0.90), F5 (0.84), CRABP1 (0.84), PENK (0.84), ATP1B1 (0.82); STRING partners: F5 (0.817), GC (0.84)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 is the strongest network hub in the module and connects the co-abundance structure to F5, GC and several otherwise unrelated proteins. It is a secreted liver and hepatocyte product, is a plasma protease inhibitor, and has established relevance to antithrombin deficiency and venous thromboembolic disease. It also participates in the hu.MAP association (hu.MAP huMAP3_15040.1) and has high-confidence STRING links to F5 and GC. Its extensive literature makes it the clearest anchor for the extracellular coagulation interpretation.
- **Conclusion**: Established evidence supports SERPINC1 as a central secreted coagulation protein and as part of the known plasma-protein component of the module. It is plausible, but not established, that its central co-abundance reflects blood-derived material or barrier-related fluid composition in the paired tissues.

#### F5

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.84), ATP1B1 (0.83), SCG2 (0.83), GC (0.82); STRING partners: SERPINC1 (0.817)
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coagulation factor V. This gene encodes an essential cofactor of the blood coagulation cascade. This factor circulates in plasma, and is converted to the active form by the release of the activation peptide by thrombin during coagulation. This generates a heavy chain and a light chain which are held together by calcium ions. The activated protein is a cofactor that participates with activated coagulation factor X to ac…
- **Diseases (Open Targets)**: thrombophilia due to activated protein C resistance (0.796); congenital factor V deficiency (0.777); factor V deficiency (0.768); ischemic stroke (0.662); venous thromboembolism (0.603)
- **Europe PMC papers**: 25771
- **Why important**: F5 is a network connector linking SERPINC1, GC, ATP1B1 and SCG2. It is a secreted coagulation cofactor with liver, choroid plexus and placenta associations, and it has blood-cell enrichment across several myeloid and regulatory cell categories. Its STRING relationship with SERPINC1 is biologically expected, and its disease associations include factor V deficiency, activated protein C resistance, ischemic stroke and venous thromboembolism.
- **Conclusion**: Established evidence supports F5 as a circulating coagulation component and a plausible contributor to a blood or extracellular-fluid signal. Its co-abundance with neuroendocrine and cellular proteins is a hypothesis about shared sample composition, not evidence that F5 directly regulates those proteins.

#### GC

- **Related proteins** (co-abundance neighbors): ATP1B1 (0.90), CPD (0.88), F5 (0.82); STRING partners: SERPINC1 (0.84)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: GC vitamin D binding protein. The protein encoded by this gene belongs to the albumin gene family. It is a multifunctional protein found in plasma, ascitic fluid, cerebrospinal fluid and on the surface of many cell types. It binds to vitamin D and its plasma metabolites and transports them to target tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq,…
- **Diseases (Open Targets)**: vitamin D deficiency (0.574); vitamin deficiency (0.552); chronic obstructive pulmonary disease (0.499); squamous cell carcinoma (0.339); central nervous system cancer (0.334)
- **Europe PMC papers**: 363974
- **Why important**: GC is a liver-enriched secreted plasma protein that transports vitamin D and is also found in cerebrospinal fluid. It connects ATP1B1, CPD, F5 and SERPINC1 in the module, has a high-confidence STRING relationship with SERPINC1, and shares the hu.MAP complex (hu.MAP huMAP3_15040.1) with SERPINC1. Its very large literature base and disease associations involving vitamin-D deficiency make it an important bridge between the plasma-fluid interpretation and a possible cerebrospinal-fluid context.
- **Conclusion**: Established evidence supports GC as a multifunctional extracellular transport protein and a strong marker of plasma or cerebrospinal-fluid-associated composition. It is not established that vitamin-D transport is functionally enriched in this module, because no GO or KEGG term passed global correction.

#### HSPA5

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.93), ATP1B1 (0.82), PAM (0.82), PENK (0.81); STRING partners: SIL1 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is a highly connected intracellular component that links SERPINC1, ATP1B1, PAM and PENK. It is an ER HSP seventy chaperone involved in protein folding, ER homeostasis and the unfolded-protein response, and its STRING partnership with SIL1 is exceptionally well established in the supplied evidence. Its extensive literature and associations with neurodegenerative disease make it a useful indicator of secretory-pathway or proteostasis involvement.
- **Conclusion**: Established evidence supports HSPA5 as an ER proteostasis factor and supports its relationship with SIL1. The hypothesis that its co-abundance with secreted and neuroendocrine proteins reflects coordinated secretory-cell stress or protein handling remains unproven.

#### PENK

- **Related proteins** (co-abundance neighbors): GOT1 (0.89), CRABP1 (0.85), SERPINC1 (0.84), HSPA5 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proenkephalin. This gene encodes a preproprotein that is proteolytically processed to generate multiple protein products. These products include the pentapeptide opioids Met-enkephalin and Leu-enkephalin, which are stored in synaptic vesicles, then released into the synapse where they bind to mu- and delta-opioid receptors to modulate the perception of pain. Other non-opioid cleavage products may function in dis…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.387); diabetes mellitus (0.258); smoking initiation (0.214); substance-related disorder (0.171); alcohol drinking (0.170)
- **Europe PMC papers**: 4620
- **Why important**: PENK is a network connector linking GOT1, CRABP1, SERPINC1 and HSPA5. It is enriched in brain and adrenal gland, is stored in vesicles, and produces opioid peptides that modulate pain signaling. Its neuroendocrine distribution and large literature base provide a biologically meaningful explanation for why a module shared with autonomic nervous system and cerebrospinal fluid could contain a neural secretory component. It also has disease associations involving diabetes and substance-related phenotypes.
- **Conclusion**: Established evidence supports PENK as a neuroendocrine precursor and secreted-vesicle protein. Its presence supports a neural or neuroendocrine contribution to the module, but does not establish opioid signaling as the module-wide function.

#### PAM

- **Related proteins** (co-abundance neighbors): HSPA5 (0.82), CRABP1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peptidylglycine alpha-amidating monooxygenase. This gene encodes a multifunctional protein. The encoded preproprotein is proteolytically processed to generate the mature enzyme. This enzyme includes two domains with distinct catalytic activities, a peptidylglycine alpha-hydroxylating monooxygenase (PHM) domain and a peptidyl-alpha-hydroxyglycine alpha-amidating lyase (PAL) domain. These catalytic domains work sequentially to catalyze the conve…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.593); diabetes mellitus (0.538); Abnormality of the skeletal system (0.517); intelligence (0.492); diabetic eye disease (0.451)
- **Europe PMC papers**: 50367
- **Why important**: PAM is a catalytic component of neuroendocrine peptide maturation and connects HSPA5 with CRABP1. It is associated with heart and neuroendocrine cell types, resides in the Golgi and cytosol, and generates amidated peptide products from neuroendocrine precursors. Its substantial literature and disease associations involving diabetes and diabetic eye disease make it a useful mechanistic candidate linking secretory processing to the PENK and SCG2 side of the module.
- **Conclusion**: Established evidence supports PAM as an enzyme required for maturation of active neuroendocrine peptides. It is plausible that PAM and PENK report coordinated secretory biology, but the supplied network does not demonstrate a direct physical interaction or prove that peptide amidation drives the entire module.

## Module 1

**Tissue pair**: autonomic_nervous_system and cerebrospinal_fluid  
**Genes (6)**: DBI, ADAM10, APOA1, HSPA13, SCG3, VTN

### Function

No GO or KEGG term passed global multiple-testing correction, so there is no globally significant pathway assignment for this module. The gene identities and network suggest a mixed secretory and extracellular biology signal: SCG3 points to neuroendocrine secretory-granule protein localization, VTN to extracellular-matrix adhesion and integrin-related signaling, APOA1 to HDL-associated lipid transport, DBI to fatty-acid and phospholipid handling, ADAM10 to membrane ectodomain proteolysis, and HSPA13 to processing of cytosolic and secretory proteins. The module therefore appears most consistent with coordinated abundance of secreted, vesicular, extracellular, lipid-associated, and proteostasis-related proteins rather than a single established pathway. These functional assignments are gene-level evidence, not enrichment claims.

**Cell composition.** The module is strongly enriched in secreted proteins: most of its genes are annotated as secreted, including proteins secreted to blood or secreted in brain. APOA1 and VTN are liver-enriched and secreted to blood, while SCG3 is brain-, pituitary-, and retina-enriched and secreted in brain. HSPA13, ADAM10, and DBI have low tissue specificity, and the module includes cell-type enhancement in hepatocytes and corticotrophs as well as several other cell types. Blood-cell specificity is generally low or absent, although APOA1 is immune-cell enhanced in plasmacytoid dendritic cells. This composition means that the shared signal may reflect circulating or extracellular protein abundance, liver-derived material, secretory biology, or shared sample cell-type contributions, rather than a tissue-specific autonomic-nervous-system or cerebrospinal-fluid mechanism. There is no matching HPA tissue for direct protein-detection assessment in either requested tissue group.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The module has limited known interaction support in STRING. APOA1-DBI and APOA1-VTN are supported STRING relationships, so APOA1 provides the principal bridge between the lipid-associated and extracellular components. SCG3, HSPA13, and ADAM10 have no listed STRING partners within the module. No hu.MAP complex contains multiple module members. Thus, the co-abundance structure is not explained by a documented shared hu.MAP complex, and only part of the network has prior interaction support. The remaining edges may reflect co-regulation, shared secretion or sample-composition effects, indirect biology, or interactions not represented in the queried resources.

**STRING interactions (score >= 0.7)**: 2 of 15 gene pairs: APOA1–DBI (0.78); APOA1–VTN (0.755)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a definitively new biological mechanism. It is unusual in combining a brain and neuroendocrine secretory marker with liver-derived plasma proteins, lipid-associated proteins, a membrane sheddase, and a proteostasis factor, and it lacks a multi-member hu.MAP complex and broad STRING support. Those features make the specific cross-tissue co-abundance pattern potentially novel. However, absence from STRING or hu.MAP does not establish novelty, and the predominance of secreted or broadly expressed proteins creates plausible technical, circulating-protein, or shared-cell-type explanations. The appropriate conclusion is that the module is a novel candidate co-abundance pattern requiring independent replication and control for blood contamination, liver-derived proteins, cellular composition, and assay effects.

**Hypothesis.** Hypothesis: the module reflects coordinated handling and release of extracellular and secretory cargo across the autonomic-nervous-system and cerebrospinal-fluid sample context. SCG3 may mark neuroendocrine or neural secretory vesicles; ADAM10 may contribute to membrane-protein ectodomain shedding; VTN and APOA1 may represent extracellular and circulating lipid-associated cargo; DBI may connect lipid metabolism with phospholipid remodeling; and HSPA13 may support processing or quality control of secretory proteins. A competing hypothesis is that the apparent module is driven mainly by variable abundance of blood- or liver-derived proteins together with shared sample cellular composition. Testing should therefore compare the module with blood-protein contamination markers, quantify cell-type composition, and validate the co-abundance pattern in independent autonomic-nervous-system and cerebrospinal-fluid cohorts.

### Important genes

#### SCG3

- **Related proteins** (co-abundance neighbors): ADAM10 (0.95), VTN (0.89), DBI (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: secretogranin III. The protein encoded by this gene is a member of the chromogranin/secretogranin family of neuroendocrine secretory proteins. Granins may serve as precursors for biologically active peptides. Some granins have been shown to function as helper proteins in sorting and proteolytic processing of prohormones; however, the function of this protein is unknown. Two transcript variants encoding different iso…
- **Diseases (Open Targets)**: osteoarthritis, knee (0.403); intelligence (0.341); osteoarthritis, hip (0.317); placental abruption (0.253); total knee arthroplasty (0.212)
- **Europe PMC papers**: 797
- **Why important**: SCG3 has the most central network position in the module and connects ADAM10, VTN, and DBI. It is annotated as a neuroendocrine secretory protein involved in secretory-granule protein localization, with HPA enrichment in brain, pituitary gland, and retina and localization to vesicles. Its cell-type associations include astrocytes, Bergmann glia, brain inhibitory neurons, cone photoreceptors, and corticotrophs. It therefore provides the strongest biological link to neural and neuroendocrine secretory biology. Its literature volume is more limited than that of the other leading candidates, which makes its role important but less established.
- **Conclusion**: Established evidence supports SCG3 as a neural or neuroendocrine secretory-granule marker and as the central co-abundance connector. It is plausible, but not established, that SCG3 organizes the module around neural secretory biology; the alternative explanation of shared extracellular or sample-composition effects remains substantial.

#### APOA1

- **Related proteins** (co-abundance neighbors): HSPA13 (0.95); STRING partners: DBI (0.78), VTN (0.755)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is a liver-enriched protein secreted to blood and the major protein component of HDL. Its established functions include cholesterol efflux, lipid transport, and support of cholesteryl-ester formation. It is connected in STRING to DBI and VTN, making it the main known interaction bridge in the module, although its module connectivity is limited. It has the largest literature volume among the genes and strong disease associations involving APOA1 deficiency and familial visceral amyloidosis. Its presence is especially important for assessing whether the module represents circulating or liver-derived protein abundance.
- **Conclusion**: Established evidence supports APOA1 as a circulating lipid-transport protein and as a known interaction partner of DBI and VTN. Its presence supports an extracellular or plasma-related interpretation, but does not by itself establish a neural mechanism; it may instead indicate blood or liver-derived contribution to the samples.

#### VTN

- **Related proteins** (co-abundance neighbors): SCG3 (0.89), HSPA13 (0.83); STRING partners: APOA1 (0.755)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vitronectin. The protein encoded by this gene functions in part as an adhesive glycoprotein. Differential expression of this protein can promote either cell adhesion or migration as it links cells to the extracellular matrix through a variety of ligands. These ligands include integrins, plasminogen activator inhibitor-1, and urokinase plasminogen activator receptor. This secreted protein can be present in the …
- **Diseases (Open Targets)**: hypertensive disorder (0.421); dengue disease (0.376); neurodegenerative disease (0.343); temporal arteritis (0.338); age-related macular degeneration (0.313)
- **Europe PMC papers**: 3940
- **Why important**: VTN is a liver-enriched secreted protein found in blood and extracellular-matrix contexts. It participates in cell adhesion, cell-matrix adhesion, integrin-mediated signaling, vesicle-mediated transport, and regulation of smooth-muscle-cell migration. It connects SCG3 and HSPA13 in the module and has a STRING relationship with APOA1. Its literature volume is substantial, and its disease associations include hypertensive, neurodegenerative, vascular, and retinal conditions. VTN is therefore a useful candidate for linking secretory cargo with extracellular-matrix and adhesion biology.
- **Conclusion**: Established evidence supports VTN as a secreted extracellular and adhesion-associated protein with known association to APOA1. A role for VTN in coupling neural secretory material to extracellular-matrix signaling is a hypothesis rather than a demonstrated property of this module.

#### ADAM10

- **Related proteins** (co-abundance neighbors): SCG3 (0.95); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ADAM metallopeptidase domain 10. Members of the ADAM family are cell surface proteins with a unique structure possessing both potential adhesion and protease domains. This gene encodes and ADAM family member that cleaves many proteins including TNF-alpha and E-cadherin. Alternate splicing results in multiple transcript variants encoding different proteins that may undergo similar processing. [provided by RefSeq, Feb 2016].
- **Diseases (Open Targets)**: reticulate acropigmentation of Kitamura (0.679); Alzheimer disease 18 (0.621); Alzheimer disease (0.522); dementia (0.415); schizophrenia (0.354)
- **Europe PMC papers**: 11139
- **Why important**: ADAM10 is connected to SCG3 and is localized to vesicles and the plasma membrane. Its established functions include proteolysis, membrane-protein ectodomain cleavage, negative regulation of cell adhesion, and Notch signaling. It has a large literature volume and disease associations involving Alzheimer disease, dementia, schizophrenia, and a pigmentation disorder. It supplies a mechanistically distinctive membrane-processing function that could connect secretory-vesicle biology with extracellular protein release.
- **Conclusion**: Established evidence supports ADAM10 as a membrane-associated protease involved in ectodomain shedding and Notch-related biology. Its participation in this co-abundance module may indicate coordinated vesicle or membrane remodeling, but the module data do not demonstrate that ADAM10 regulates the other proteins.

#### DBI

- **Related proteins** (co-abundance neighbors): SCG3 (0.85); STRING partners: APOA1 (0.78)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: diazepam binding inhibitor, acyl-CoA binding protein. This gene encodes diazepam binding inhibitor, a protein that is regulated by hormones and is involved in lipid metabolism and the displacement of beta-carbolines and benzodiazepines, which modulate signal transduction at type A gamma-aminobutyric acid receptors located in brain synapses. The protein is conserved from yeast to mammals, with the most highly conserved domain consisting of seven conti…
- **Diseases (Open Targets)**: neurodegenerative disease (0.418); autoimmune disorder of central nervous system (0.192); hepatocellular carcinoma (0.082); glioblastoma (0.078); Wilson disease (0.066)
- **Europe PMC papers**: 11452
- **Why important**: DBI is connected to SCG3 and has a STRING relationship with APOA1. It binds medium- and long-chain acyl-CoA species and is annotated for fatty-acid metabolism, phosphatidylcholine acyl-chain remodeling, and positive regulation of phospholipid transport. It is broadly expressed with hepatocyte enhancement and has a substantial literature volume, including associations with neurodegenerative and central-nervous-system autoimmune disease. DBI could therefore connect lipid handling with neural signaling and secretory-membrane composition.
- **Conclusion**: Established evidence supports DBI as an acyl-CoA-binding and phospholipid-related protein with links to lipid metabolism and GABA-related signaling context. Its role as a metabolic bridge in this module is plausible, but it is not established that DBI explains the cross-tissue co-abundance pattern.

## Module 2

**Tissue pair**: autonomic_nervous_system and cerebrospinal_fluid  
**Genes (9)**: BASP1, CADM1, CD276, EGFR, EMILIN1, L1CAM, NRCAM, SELENBP1, SEZ6L2

### Function

The most coherent interpretation is a neural cell-surface adhesion and cell–matrix communication module, with links to axon guidance, neuronal development, synapse maturation, extracellular-matrix organization, and receptor-mediated signaling. L1CAM, NRCAM, CADM1, and SEZ6L2 support a neuronal adhesion and connectivity theme, while EMILIN1 provides an extracellular-matrix component and EGFR provides receptor-tyrosine-kinase signaling. CD276 and CADM1 also introduce immune-regulatory and cell-recognition features. These interpretations are based on gene annotations and network structure, not on enrichment significance: no GO/KEGG term passed global correction, and STRING functional enrichment was absent. The module may therefore represent a coordinated neural-interface or tissue-architecture signal rather than a statistically established pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only EMILIN1, EGFR, and NRCAM have secretome annotations, with EMILIN1 associated with the extracellular matrix, EGFR reported as secreted to blood, and NRCAM secreted in brain. It is also not predominantly blood-cell enriched. Most genes are not detected in immune cells, although SELENBP1, BASP1, CADM1, and NRCAM show selected immune-cell enrichment or enhancement. HPA instead shows a strong tissue- and cell-type-selective pattern, especially in brain, retina, excitatory neurons, astrocytes, and related neural cell types. Thus, the shared module is more consistent with a neural or neural–vascular interface signal than with a generic housekeeping program or simple blood contamination, while the immune-associated annotations warrant caution in interpreting cerebrospinal-fluid measurements.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module: EGFR–L1CAM. This supports a possible connection between receptor signaling and neuronal adhesion, but it is a single known interaction and does not establish the entire co-abundance module as a physical complex. hu.MAP provides one shared complex context, (hu.MAP huMAP3_11349.1), containing CD276 and SEZ6L2 among many other proteins. This supports a possible shared molecular environment or complex-related association for those genes, but the module members constitute only a small part of that large complex. The remaining co-abundance edges are not supported by the listed high-confidence STRING or hu.MAP relationships, so they should be regarded as coordinated expression relationships rather than established direct binding.

**STRING interactions (score >= 0.7)**: 1 of 36 gene pairs: EGFR–L1CAM (0.976)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11349.1 (CD276, SEZ6L2; 2/78)

### Novelty

This may be a novel tissue-pair co-abundance module, particularly because the complete pattern combines neural adhesion molecules, extracellular matrix, receptor signaling, and immune-regulatory surface proteins in autonomic nervous system and cerebrospinal fluid. However, the evidence does not justify calling it a newly discovered biological complex or pathway. The known EGFR–L1CAM interaction and the CD276–SEZ6L2 hu.MAP co-membership show that parts of the pattern have prior molecular support. Conversely, the lack of STRING or hu.MAP support for the other edges does not prove novelty, because co-abundance can reflect shared cell origin, regulated secretion, trafficking, or correlated tissue state. The most defensible claim is novelty of the integrated tissue-pair co-abundance pattern, pending replication and independent validation.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of neural adhesion and extracellular-interface proteins released from, or associated with, neural and glial populations at the autonomic nervous system–cerebrospinal fluid boundary. L1CAM, NRCAM, CADM1, and SEZ6L2 could organize cell recognition, axonal contacts, and synaptic or glial interfaces; EMILIN1 could connect this signal to extracellular matrix; and EGFR could couple the interface to growth-factor and MAPK-related signaling. CD276 may mark an immunoregulatory component of the same interface. This is a mechanistic hypothesis, not an established pathway: the observed co-abundance could instead arise from shared neural cell composition, extracellular vesicles, or selective protein release into cerebrospinal fluid.

### Important genes

#### L1CAM

- **Related proteins** (co-abundance neighbors): EMILIN1 (0.90), EGFR (0.86), CD276 (0.83); STRING partners: EGFR (0.976)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: L1 cell adhesion molecule. The protein encoded by this gene is an axonal glycoprotein belonging to the immunoglobulin supergene family. The ectodomain, consisting of several immunoglobulin-like domains and fibronectin-like repeats (type III), is linked via a single transmembrane sequence to a conserved cytoplasmic domain. This cell adhesion molecule plays an important role in nervous system development, including neuronal m…
- **Diseases (Open Targets)**: X-linked hydrocephalus with stenosis of the aqueduct of Sylvius (0.855); MASA syndrome (0.833); X-linked complicated corpus callosum dysgenesis (0.762); L1 syndrome (0.725); Spastic paraplegia (0.571)
- **Europe PMC papers**: 6523
- **Why important**: L1CAM is a central network connector, linked to EMILIN1, EGFR, and CD276, and it is the partner in the module's high-confidence STRING relationship with EGFR. Its brain-enhanced expression, neuronal cell-type associations, plasma-membrane localization, and established roles in neuronal migration, differentiation, cell adhesion, and axon guidance make it the clearest anchor for the neural interpretation. It also has an extensive literature and strong disease associations with X-linked neurological syndromes.
- **Conclusion**: Established evidence supports L1CAM as a neuronal adhesion and axon-development molecule and as a major interpretive anchor. Its role as a driver of this shared co-abundance module remains a hypothesis.

#### NRCAM

- **Related proteins** (co-abundance neighbors): CD276 (0.89), BASP1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neuronal cell adhesion molecule. Cell adhesion molecules (CAMs) are members of the immunoglobulin superfamily. This gene encodes a neuronal cell adhesion molecule with multiple immunoglobulin-like C2-type domains and fibronectin type-III domains. This ankyrin-binding protein is involved in neuron-neuron adhesion and promotes directional signaling during axonal cone growth. This gene is also expressed in non-neural tissues and may…
- **Diseases (Open Targets)**: neurodevelopmental disorder with neuromuscular and skeletal abnormalities (0.774); complex neurodevelopmental disorder (0.370); stroke disorder (0.261); alcohol drinking (0.257); ovarian neoplasm (0.255)
- **Europe PMC papers**: 2314
- **Why important**: NRCAM connects CD276 and BASP1 in the module and is tissue-enhanced in adrenal gland, brain, and retina. Its neural and glial cell-type associations, secretion in brain, and annotations for neuron migration, axonogenesis, axon guidance, axonal fasciculation, and synapse assembly strongly support a neural-interface interpretation. Its literature and disease associations provide substantial external biological context.
- **Conclusion**: Established evidence supports NRCAM as a neuronal cell-adhesion and axon-organization component. Its presence in cerebrospinal fluid or its coordination with the other module proteins may reflect release or shared cellular origin, but that mechanism is not established.

#### CADM1

- **Related proteins** (co-abundance neighbors): SEZ6L2 (0.89), SELENBP1 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell adhesion molecule 1. Enables signaling receptor binding activity. Involved in several processes, including cell recognition; positive regulation of cytokine production; and susceptibility to natural killer cell mediated cytotoxicity. Located in plasma membrane. Implicated in breast carcinoma and prostate cancer. Biomarker of cervix uteri carcinoma in situ. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypothyroidism (0.505); Abnormality of the skeletal system (0.485); obesity disorder (0.420); restless legs syndrome (0.402); autoimmune thyroid disease (0.342)
- **Europe PMC papers**: 3471
- **Why important**: CADM1 connects SEZ6L2 and SELENBP1 and is tissue-enhanced in retina, with associations to astrocytes, photoreceptors, and retinal bipolar cells. Its plasma-membrane localization and roles in cell recognition, homophilic and heterophilic adhesion, cytokine production, and natural-killer-cell-mediated cytotoxicity make it a useful bridge between neural adhesion and immune-regulatory biology. It has a substantial literature and disease-association record.
- **Conclusion**: Established evidence supports CADM1 as a cell-recognition and adhesion molecule with neural and immune relevance. Its specific functional contribution to this module, especially in cerebrospinal fluid, remains unresolved.

#### EGFR

- **Related proteins** (co-abundance neighbors): CD276 (0.94), L1CAM (0.86); STRING partners: L1CAM (0.976)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: epidermal growth factor receptor. The protein encoded by this gene is a transmembrane glycoprotein that is a member of the protein kinase superfamily. This protein is a receptor for members of the epidermal growth factor family. EGFR is a cell surface protein that binds to epidermal growth factor, thus inducing receptor dimerization and tyrosine autophosphorylation leading to cell proliferation. Mutations in this gene are associat…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.850); lung adenocarcinoma (0.774); cancer (0.737); head and neck squamous cell carcinoma (0.725); lung cancer (0.717)
- **Europe PMC papers**: 223694
- **Why important**: EGFR is directly connected to L1CAM in STRING and is connected to CD276 in the co-abundance network. It is a plasma-membrane receptor tyrosine kinase with annotations for cell-surface receptor signaling, MAPK signaling, and protein phosphorylation, and it is reported as secreted to blood. Its very extensive literature makes it a strong candidate for linking adhesion-associated proteins to growth-factor signaling, although its tissue annotation here is placenta-enhanced rather than brain-specific.
- **Conclusion**: Established evidence supports EGFR as a signaling receptor and provides direct interaction evidence with L1CAM. Its participation in a neural cerebrospinal-fluid interface is a hypothesis and could also reflect a non-neural or secreted component.

#### EMILIN1

- **Related proteins** (co-abundance neighbors): L1CAM (0.90), CD276 (0.87), SEZ6L2 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: elastin microfibril interfacer 1. This gene encodes an extracellular matrix glycoprotein that is characterized by an N-terminal microfibril interface domain, a coiled-coiled alpha-helical domain, a collagenous domain and a C-terminal globular C1q domain. The encoded protein associates with elastic fibers at the interface between elastin and microfibrils and may play a role in the development of elastic tissues including large bloo…
- **Diseases (Open Targets)**: arterial tortuosity-bone fragility syndrome (0.629); neuronopathy, distal hereditary motor, autosomal dominant 10 (0.593); Arterial tortuosity (0.487); EMILIN-1-related connective tissue disease (0.370); hereditary disease (0.194)
- **Europe PMC papers**: 1119
- **Why important**: EMILIN1 has high network connectivity to L1CAM, CD276, and SEZ6L2 and is the module's clearest extracellular-matrix component. It is secreted to the extracellular matrix and is annotated for cell–matrix adhesion, elastic-fiber organization, vascular development, and blood-pressure regulation. Its tissue and stromal-cell associations and disease links to connective-tissue and arterial disorders make it important for a possible structural or vascular-interface interpretation, despite a smaller literature than EGFR or L1CAM.
- **Conclusion**: Established evidence supports EMILIN1 as an extracellular-matrix and cell–matrix adhesion protein. Its coordinated abundance with neural adhesion proteins may indicate a structural interface, but this proposed neural connection is not yet demonstrated.

#### SEZ6L2

- **Related proteins** (co-abundance neighbors): CADM1 (0.89), EMILIN1 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11349.1
- **Function (MyGene.info)**: seizure related 6 homolog like 2. This gene encodes a seizure-related protein that is localized on the cell surface. The gene is located in a region of chromosome 16p11.2 that is thought to contain candidate genes for autism spectrum disorders (ASD), though there is no evidence directly implicating this gene in ASD. Increased expression of this gene has been found in lung cancers, and the protein is therefore considered to be a no…
- **Diseases (Open Targets)**: neurodegenerative disease (0.274); colorectal carcinoma (0.077); hepatocellular carcinoma (0.075); intrahepatic cholangiocarcinoma (0.074); neoplasm (0.065)
- **Europe PMC papers**: 559
- **Why important**: SEZ6L2 connects CADM1 and EMILIN1, is brain- and pituitary-enhanced, and is associated with excitatory and inhibitory neurons as well as several pituitary cell types. Its annotations for synapse maturation and cerebellar Purkinje-cell development give it a specific neural role. It is also one of the two module members in the hu.MAP context (hu.MAP huMAP3_11349.1), together with CD276. Its literature is smaller than that of the major adhesion and receptor genes, which makes its inclusion particularly informative but less firmly characterized.
- **Conclusion**: Established evidence supports SEZ6L2 as a neural cell-surface and synapse-associated protein with hu.MAP context. Its role as a coordinator of the broader module is a hypothesis rather than an established molecular function.

