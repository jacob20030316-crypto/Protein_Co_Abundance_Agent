# Conserved co-abundance modules: prostate and stem_cells

## Module 0

**Tissue pair**: prostate and stem_cells  
**Genes (29)**: GOT2, ACO2, ALDH1B1, ARPC4, ALCAM, CD276, CD44, COG2, COG5, COPS7A, DCAKD, FKBP2, GPD2, GRIPAP1, HADH, NT5DC1, NT5DC2, DDOST, POLDIP2, PON2, UQCRC2, SACM1L, SGPL1, SUCLG1, SUCLG2, DARS2, TACC2, ACAT1, TIMM9

### Function

The module does not have any GO or KEGG term that passed global correction, so its function should be inferred from its gene composition and network structure rather than from formal enrichment. The strongest coherent signal is mitochondrial intermediary metabolism: GOT2 links amino-acid metabolism with several module components, while ACO2, SUCLG1, SUCLG2, UQCRC2, ACAT1, HADH, GPD2, ALDH1B1, and DARS2 represent the tricarboxylic-acid cycle, respiratory-chain, fatty-acid oxidation, redox-shuttle, aldehyde-detoxification, and mitochondrial translation functions. The densely supported STRING relationships among ACAT1, HADH, SUCLG1, SUCLG2, ACO2, GOT2, and UQCRC2 (STRING Keyword Transit peptide; within-query FDR = 0.0081) support a mitochondrial metabolic backbone, but (STRING Keyword Transit peptide; within-query FDR = 0.0081) is supplementary and is not globally corrected enrichment evidence. A second, less connected axis involves cell-surface adhesion and immune-regulatory biology through CD44, ALCAM, and CD276, together with actin, vesicle, and Golgi-related genes. Overall, the module is best interpreted as a mixed metabolic and membrane-trafficking or cell-interface program, rather than as a single narrowly defined pathway.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only a minority of genes are annotated as secreted, and most genes are intracellular enzymes, mitochondrial proteins, Golgi proteins, or signaling and structural proteins. HPA indicates broadly distributed or tissue-enhanced expression for many genes, with frequent enhancement in liver, skeletal muscle, heart muscle, tongue, and choroid plexus rather than a prostate-specific pattern. Most genes have low immune-cell specificity, although a subset is enhanced in dendritic cells, monocytes, eosinophils, neutrophil-lineage cells, or plasma cells. CD44, ALCAM, and PON2 are secreted to blood according to HPA, while CD276 is detected in vesicles. Protein detection in prostate is widespread among the annotated genes, whereas the stem-cell comparison has no matching HPA tissue record. Thus, the shared module is unlikely to be explained simply by a plasma-protein or broad blood-cell signature, but contributions from shared cell types, stromal or epithelial interfaces, and sample composition remain plausible.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a connected mitochondrial component, including ACAT1 with HADH, SUCLG1, and SUCLG2; ACO2 with GOT2, SUCLG1, SUCLG2, and UQCRC2; and SUCLG1 with SUCLG2 and UQCRC2 (STRING Keyword Transit peptide; within-query FDR = 0.0081). It also supports the adhesion relationship between ALCAM and CD44, and the Golgi relationship between COG2 and COG5. These are established database relationships and indicate that parts of the co-abundance module recapitulate known molecular biology. hu.MAP provides partial complex support rather than a complete module-level complex: FKBP2 and POLDIP2 co-occur in (hu.MAP huMAP3_11879.1), ALCAM and CD276 recur in several complexes (hu.MAP huMAP3_02887.1) through (hu.MAP huMAP3_09336.1) and (hu.MAP huMAP3_11349.1), COG2 and COG5 occur together in (hu.MAP huMAP3_04294.1) through (hu.MAP huMAP3_09176.1), HADH and NT5DC1 occur in (hu.MAP huMAP3_14442.1), and DARS2 and NT5DC2 occur in (hu.MAP huMAP3_13468.1). The repeated ALCAM-CD276 and COG2-COG5 memberships suggest membrane-interface and Golgi-related structure, but the module members generally form only a small subset of the much larger hu.MAP complexes. Therefore, the network is partly supported by known interactions but is not equivalent to one established protein complex.

**STRING interactions (score >= 0.7)**: 11 of 406 gene pairs: ACAT1–HADH (0.935); ACAT1–SUCLG1 (0.907); ACAT1–SUCLG2 (0.867); ACO2–GOT2 (0.753); ACO2–SUCLG1 (0.929); ACO2–SUCLG2 (0.735); ACO2–UQCRC2 (0.879); ALCAM–CD44 (0.859); COG2–COG5 (0.999); SUCLG1–SUCLG2 (0.999); SUCLG1–UQCRC2 (0.866)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transit peptide (FDR = 0.0081, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11879.1 (FKBP2, POLDIP2; 2/7); huMAP3_02887.1 (ALCAM, CD276; 2/9); huMAP3_05555.1 (ALCAM, CD276; 2/9); huMAP3_04294.1 (COG2, COG5; 2/10); huMAP3_14423.1 (COG2, COG5; 2/11); huMAP3_09176.1 (COG2, COG5; 2/12); huMAP3_06308.1 (ALCAM, CD276; 2/20); huMAP3_10503.1 (ALCAM, CD276; 2/27); huMAP3_08689.1 (ALCAM, CD276; 2/37); huMAP3_10980.1 (ALCAM, CD276; 2/44); huMAP3_10848.1 (ALCAM, CD276; 2/46); huMAP3_09336.1 (ALCAM, CD276; 2/50); huMAP3_14442.1 (HADH, NT5DC1; 2/57); huMAP3_11349.1 (ALCAM, CD276; 2/78); huMAP3_13468.1 (DARS2, NT5DC2; 2/99)

### Novelty

The conserved prostate and stem-cell co-abundance pattern may represent a new tissue-shared expression relationship, but the fact sheet does not establish that it is a new molecular mechanism. Several component relationships are already known through STRING and hu.MAP, especially mitochondrial metabolism, ALCAM-CD44 adhesion, COG2-COG5 Golgi organization, and the listed partial complexes. Conversely, the absence of many genes from STRING or hu.MAP cannot demonstrate novelty, because database coverage, context dependence, interaction direction, and complex incompleteness all limit those resources. The defensible conclusion is that the module-level combination and its conservation across the tissue pair may be novel or undercharacterized, while many of its constituent biological relationships are established. Direct comparison with published prostate, stem-cell, and co-abundance studies would be required to claim a genuinely new finding.

**Hypothesis.** Hypothesis: the module reflects coordinated support for mitochondrial energy and biosynthetic metabolism together with remodeling of cell-surface adhesion, vesicle trafficking, and Golgi function in a shared prostate and stem-cell-associated cellular state. In this model, the metabolic backbone involving GOT2, ACO2, SUCLG1, SUCLG2, ACAT1, HADH, and UQCRC2 supplies intermediary metabolites and respiratory capacity, while CD44, ALCAM, and CD276 mark or participate in cell-interface signaling and COG2-COG5 support membrane-protein processing and trafficking. The co-abundance relationship could therefore arise from a common epithelial, progenitor-like, stromal, or mixed-cell state rather than from direct physical binding among all module proteins. This is a testable hypothesis, not an established conclusion; it should be assessed with cell-resolved expression, mitochondrial activity measurements, adhesion or migration assays, and perturbation of the candidate interface genes.

### Important genes

#### GOT2

- **Related proteins** (co-abundance neighbors): NT5DC2 (0.89), CD44 (0.85), DARS2 (0.84), ACAT1 (0.81), FKBP2 (0.81), DDOST (0.80), COG2 (0.80); STRING partners: ACO2 (0.753)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamic-oxaloacetic transaminase 2. Glutamic-oxaloacetic transaminase is a pyridoxal phosphate-dependent enzyme which exists in cytoplasmic and inner-membrane mitochondrial forms, GOT1 and GOT2, respectively. GOT plays a role in amino acid metabolism and the urea and tricarboxylic acid cycles. The two enzymes are homodimeric and show close homology. Two transcript variants encoding different isoforms have been found for this gene. […
- **Diseases (Open Targets)**: genetic developmental and epileptic encephalopathy (0.618); developmental and epileptic encephalopathy (0.393); Encephalopathy (0.370); neurodegenerative disease (0.356); lagophthalmos (0.298)
- **Europe PMC papers**: 2463
- **Why important**: GOT2 is the strongest network connector in the supplied module and links the mitochondrial metabolic subnetwork to genes associated with nucleotides, adhesion, translation, and Golgi biology. Its established function in amino-acid metabolism, the urea and tricarboxylic-acid cycles, prostate protein detection, and broad tissue and cell-type enhancement makes it a plausible integrator rather than a peripheral marker. It also participates in the supplementary STRING transit-peptide signal (STRING Keyword Transit peptide; within-query FDR = 0.0081) and has extensive literature and disease annotation.
- **Conclusion**: Established evidence supports GOT2 as a mitochondrial amino-acid and intermediary-metabolism enzyme that occupies a central position in this module. It is reasonable to regard GOT2 as a candidate metabolic anchor, but the co-abundance data do not prove that GOT2 drives the module or directly regulates the other genes.

#### ACO2

- **Related proteins** (co-abundance neighbors): SUCLG2 (0.91), CD276 (0.86), SUCLG1 (0.82), HADH (0.80); STRING partners: GOT2 (0.753), SUCLG1 (0.929), SUCLG2 (0.735), UQCRC2 (0.879)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aconitase 2. The protein encoded by this gene belongs to the aconitase/IPM isomerase family. It is an enzyme that catalyzes the interconversion of citrate to isocitrate via cis-aconitate in the second step of the TCA cycle. This protein is encoded in the nucleus and functions in the mitochondrion. It was found to be one of the mitochondrial matrix proteins that are preferentially degraded by the serine proteas…
- **Diseases (Open Targets)**: infantile cerebellar-retinal degeneration (0.814); optic atrophy 9 (0.693); autosomal dominant optic atrophy, classic form (0.619); optic atrophy (0.601); mitochondrial disease (0.505)
- **Europe PMC papers**: 3559
- **Why important**: ACO2 connects several mitochondrial genes in the module and has STRING support with GOT2, SUCLG1, SUCLG2, and UQCRC2. Its established role in the tricarboxylic-acid cycle and mitochondrial energy metabolism provides a mechanistic link between the module's metabolic components. It is detected in prostate and is tissue-enhanced in muscle-related tissues, consistent with a respiration-associated program. Its disease associations include mitochondrial disease and optic-atrophy-related disorders, and it has substantial literature support.
- **Conclusion**: Established evidence identifies ACO2 as a core mitochondrial metabolic enzyme and a strong candidate for defining the module's energy-metabolism component. Its role as a regulatory driver of the shared prostate and stem-cell state remains hypothetical.

#### SUCLG1

- **Related proteins** (co-abundance neighbors): SUCLG2 (0.91), ALDH1B1 (0.87), ACO2 (0.82); STRING partners: ACAT1 (0.907), ACO2 (0.929), SUCLG2 (0.999), UQCRC2 (0.866)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase GDP/ADP-forming subunit alpha. This gene encodes the alpha subunit of the heterodimeric enzyme succinate coenzyme A ligase. This enzyme is targeted to the mitochondria and catalyzes the conversion of succinyl CoA and ADP or GDP to succinate and ATP or GTP. Mutations in this gene are the cause of the metabolic disorder fatal infantile lactic acidosis and mitochondrial DNA depletion. [provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome 9 (0.811); neurodegenerative disease (0.520); mitochondrial DNA depletion syndrome (0.507); post term pregnancy (0.280); lysosomal storage disease (0.245)
- **Europe PMC papers**: 1277
- **Why important**: SUCLG1 is linked within the STRING-supported mitochondrial cluster to ACO2, SUCLG2, ACAT1, and UQCRC2 (STRING Keyword Transit peptide; within-query FDR = 0.0081). It forms the alpha subunit of succinate-CoA ligase and directly connects succinyl-CoA metabolism with nucleotide-triphosphate production in mitochondria. It is detected in prostate, has tissue and cell-type enhancement in several epithelial and stem-like digestive contexts, and has established associations with mitochondrial DNA depletion and lactic-acidosis disorders.
- **Conclusion**: Established evidence supports SUCLG1 as a functional core of the mitochondrial metabolic backbone. Its co-abundance with the other metabolic genes is biologically coherent, but it is not established that SUCLG1 explains conservation of the entire module across the two tissue groups.

#### CD44

- **Related proteins** (co-abundance neighbors): GOT2 (0.85), ALCAM (0.85), GPD2 (0.84), ARPC4 (0.83); STRING partners: ALCAM (0.859)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD44 molecule (IN blood group). The protein encoded by this gene is a cell-surface glycoprotein involved in cell-cell interactions, cell adhesion and migration. It is a receptor for hyaluronic acid (HA) and can also interact with other ligands, such as osteopontin, collagens, and matrix metalloproteinases (MMPs). This protein participates in a wide variety of cellular functions including lymphocyte activation, recirculation and …
- **Diseases (Open Targets)**: nephrolithiasis, calcium oxalate (0.523); calcium oxalate urolithiasis (0.521); uterine corpus leiomyoma (0.480); systemic lupus erythematosus (0.467); autoimmune disease (0.330)
- **Europe PMC papers**: 102058
- **Why important**: CD44 is the most prominent cell-interface candidate in the module. It is connected to ALCAM, GPD2, ARPC4, and GOT2 in the co-abundance graph, and its established functions include hyaluronan-mediated cell interaction, cell-matrix adhesion, migration, endocytosis, and inflammatory signaling. HPA places it at the plasma membrane, detects it in prostate, and identifies enhancement in several immune and epithelial cell types. CD44 has very extensive literature and broad disease associations, including autoimmune and neoplastic contexts.
- **Conclusion**: Established evidence supports CD44 as a membrane adhesion and migration molecule that could mark the cellular interface component of the module. Its connection to mitochondrial genes is an observed network association, not proof of a direct metabolic mechanism; a shared cell state or cell-composition effect is an important alternative.

#### COG2

- **Related proteins** (co-abundance neighbors): ACAT1 (0.90), GOT2 (0.80); STRING partners: COG5 (0.999)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_04294.1, huMAP3_14423.1, huMAP3_09176.1
- **Function (MyGene.info)**: component of oligomeric golgi complex 2. This gene encodes a subunit of the conserved oligomeric Golgi complex that is required for maintaining normal structure and activity of the Golgi complex. The encoded protein specifically interacts with the USO1 vesicle docking protein and may be necessary for normal Golgi ribbon formation and trafficking of Golgi enzymes. Mutations of this gene are associated with abnormal glycosylation within th…
- **Diseases (Open Targets)**: congenital disorder of glycosylation, type IIq (0.671); neurodegenerative disease (0.474); congenital disorder of glycosylation type II (0.462); spinal cord disorder (0.215); polycystic ovary syndrome (0.214)
- **Europe PMC papers**: 378
- **Why important**: COG2 connects the module to Golgi organization and vesicle recycling and is paired with COG5 in STRING and in multiple hu.MAP complexes (hu.MAP huMAP3_04294.1) through (hu.MAP huMAP3_09176.1). Its established role in the conserved oligomeric Golgi complex links the module to intra-Golgi trafficking, glycoprotein handling, and maintenance of Golgi structure. It is tissue-enhanced in parathyroid gland and has disease associations involving congenital disorders of glycosylation. Although its literature volume is more limited than that of CD44 or the central mitochondrial enzymes, its complex-level evidence is comparatively direct.
- **Conclusion**: Established evidence supports COG2 as a Golgi-trafficking component and as a representative of the module's protein-processing axis. Its inclusion supports a membrane and secretory-system interpretation, but it does not establish that Golgi dysfunction causes the observed prostate and stem-cell co-abundance pattern.

## Module 1

**Tissue pair**: prostate and stem_cells  
**Genes (7)**: ABHD14B, ASPH, ATL3, BLVRB, HSPA2, MYO1C, NNT

### Function

The module does not have a statistically supported GO or KEGG functional enrichment: no GO or KEGG term passed global correction, and there were no supplementary STRING enrichment terms. The co-abundance structure nevertheless connects proteins involved in mitochondrial NADPH production and redox control through NNT, endoplasmic-reticulum organization through ATL3 and ASPH, protein folding and stress responses through HSPA2, heme metabolism through BLVRB, transcription and hydrolase-related activity through ABHD14B, and actin-dependent transport or transcription through MYO1C. Thus, the most defensible interpretation is a heterogeneous cellular homeostasis module rather than a demonstrated single biochemical pathway. Its shared appearance in prostate and stem-cell samples may reflect coordinated metabolic, proteostasis, membrane, and lineage-associated cellular states, but this remains an interpretation rather than an established pathway assignment.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of the genes is annotated as secreted. It is also not a straightforward housekeeping module, because HPA annotations show tissue-enhanced or cell-type-enhanced patterns across several differentiated cell populations. The tissue associations include skeletal muscle, adipose tissue, bone marrow, brain, and tongue, while single-cell associations include adipocytes, cardiomyocytes, hepatocytes, germ-cell populations, erythroid populations, and other specialized cells. Several genes have low immune-cell specificity, although immune-cell-enhanced annotations occur for HSPA2, ASPH, and BLVRB. Protein detection in prostate is mixed, with detection for ABHD14B, ASPH, BLVRB, and MYO1C, lack of detection for NNT and HSPA2, and no data for ATL3. These observations argue against treating the module as a prostate-specific program. Shared cell composition, tissue admixture, or a broad cellular-state signal could contribute to the co-abundance pattern.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no hu.MAP complex contained multiple module members. Therefore, the co-abundance edges are not supported here by a known high-confidence physical interaction network or by a curated multi-member complex. The absence of such support does not disprove coordinated regulation or indirect functional coupling. The strongest network-centered relationships connect NNT with ATL3, MYO1C, and ABHD14B; ATL3 with ASPH; and HSPA2 with ABHD14B and BLVRB. These links should be viewed as module-specific co-abundance relationships rather than established molecular binding relationships.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel co-abundance association, because the module is not represented by a high-confidence STRING interaction set or a hu.MAP complex and has no globally significant GO or KEGG annotation. However, those absences do not prove biological novelty. The genes have individually established functions and disease or phenotype associations, and the module could reflect shared tissue composition, cell-state variation, indirect regulation, or technical covariance. A claim of a new biological module would require replication in independent prostate and stem-cell datasets, preservation testing, adjustment for cellular composition, and comparison with published co-expression resources.

**Hypothesis.** Hypothesis: the module marks a context-dependent cellular homeostasis state in which mitochondrial redox capacity, endoplasmic-reticulum architecture, protein folding, heme handling, calcium-linked membrane physiology, and cytoskeletal or vesicle trafficking vary together. NNT could provide reducing power for biosynthesis and antioxidant defense; ATL3 and ASPH could represent endoplasmic-reticulum and calcium-related membrane processes; HSPA2 could indicate proteostasis or lineage-associated stress handling; BLVRB could link the state to heme metabolism; and MYO1C or ABHD14B could connect it to membrane trafficking or transcriptional regulation. This model is provisional and should not be presented as a demonstrated pathway because enrichment, STRING, and complex evidence do not independently support it.

### Important genes

#### NNT

- **Related proteins** (co-abundance neighbors): ATL3 (0.89), MYO1C (0.82), ABHD14B (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nicotinamide nucleotide transhydrogenase. This gene encodes an integral protein of the inner mitochondrial membrane. The enzyme couples hydride transfer between NAD(H) and NADP(+) to proton translocation across the inner mitochondrial membrane. Under most physiological conditions, the enzyme uses energy from the mitochondrial proton gradient to produce high concentrations of NADPH. The resulting NADPH is used for biosynthesis and in free …
- **Diseases (Open Targets)**: familial glucocorticoid deficiency (0.638); neurodegenerative disease (0.497); hereditary disease (0.453); atypical hemolytic-uremic syndrome with DGKE deficiency (0.416); Abnormality of the skeletal system (0.396)
- **Europe PMC papers**: 6111
- **Why important**: NNT is the most connected hub in the module and links to ATL3, MYO1C, and ABHD14B. Its established mitochondrial function couples proton translocation to NADPH production, with roles in biosynthesis and reactive oxygen species detoxification. HPA places it in a tissue-enhanced and muscle-associated context, while the supplied disease associations include glucocorticoid deficiency, neurodegenerative disease, and other hereditary phenotypes. Its substantial literature base makes it the strongest anchor for a redox and metabolic interpretation.
- **Conclusion**: Established evidence supports NNT as a mitochondrial redox and NADPH-regeneration enzyme with disease relevance. Its central position supports a hypothesis that redox state contributes to the module, but the co-abundance data do not establish that NNT regulates the other module genes.

#### ATL3

- **Related proteins** (co-abundance neighbors): NNT (0.89), ASPH (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: atlastin GTPase 3. This gene encodes a member of a family of dynamin-like, integral membrane GTPases. The encoded protein is required for the proper formation of the network of interconnected tubules of the endoplasmic reticulum. Mutations in this gene may be associated with hereditary sensory neuropathy type IF. Alternatively spliced transcript variants that encode distinct isoforms have been described. [provided b…
- **Diseases (Open Targets)**: neuropathy, hereditary sensory, type 1F (0.718); hereditary sensory and autonomic neuropathy type 1 (0.617); hereditary disease (0.193); Familial prostate cancer (0.112); prostate cancer (0.112)
- **Europe PMC papers**: 672
- **Why important**: ATL3 occupies a bridge position between NNT and ASPH. Its established role is formation and maintenance of the interconnected endoplasmic-reticulum tubular network through membrane fusion and GTPase activity. It has a group-enriched association with spermatid populations and established links to hereditary sensory neuropathy, with a more limited literature volume than NNT or HSPA2.
- **Conclusion**: Established evidence supports ATL3 as an endoplasmic-reticulum architecture factor. Its module position makes endoplasmic-reticulum organization a plausible component of the hypothesis, but there is no direct interaction or enrichment evidence showing that ATL3 functionally organizes this module.

#### HSPA2

- **Related proteins** (co-abundance neighbors): ABHD14B (0.86), BLVRB (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Flagellar centriole, Annulus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 2. Enables disordered domain specific binding activity; enzyme binding activity; and unfolded protein binding activity. Involved in negative regulation of inclusion body assembly and protein refolding. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: glaucoma (0.294); open-angle glaucoma (0.278); hypothyroidism (0.122); non-small cell lung carcinoma (0.100); neoplasm (0.094)
- **Europe PMC papers**: 2107
- **Why important**: HSPA2 connects ABHD14B and BLVRB and contributes a proteostasis dimension to the module. It is an HSP70-family chaperone with established roles in unfolded-protein binding, refolding, stress responses, spermatogenesis, and spermatid development. HPA associates it with brain and skeletal muscle and with several reproductive or developmental cell populations. Its substantial literature base and disease annotations make it an informative indicator of cellular stress or differentiation state.
- **Conclusion**: Established evidence supports HSPA2 as a chaperone and reproductive-cell-associated protein. Its co-abundance with ABHD14B and BLVRB is consistent with a proteostasis or differentiation-state hypothesis, but it does not prove that the module is a heat-shock module.

#### ASPH

- **Related proteins** (co-abundance neighbors): ATL3 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aspartate beta-hydroxylase. This gene is thought to play an important role in calcium homeostasis. The gene is expressed from two promoters and undergoes extensive alternative splicing. The encoded set of proteins share varying amounts of overlap near their N-termini but have substantial variations in their C-terminal domains resulting in distinct functional properties. The longest isoforms (a and f) include a C-terminal Asp…
- **Diseases (Open Targets)**: facial dysmorphism-lens dislocation-anterior segment abnormalities-spontaneous filtering blebs syndrome (0.770); Abnormality of the skeletal system (0.505); malignant hyperthermia of anesthesia (0.427); exercise-induced malignant hyperthermia (0.416); alcohol drinking (0.374)
- **Europe PMC papers**: 1346
- **Why important**: ASPH is the connection between ATL3 and the adipose-associated part of the module. Its established protein function includes aspartyl or asparaginyl hydroxylation and roles related to calcium homeostasis, calcium transport, electrical coupling, sarcoplasmic-reticulum release, and cardiac muscle contraction. HPA links it to adipose tissue, adipocytes, neutrophil-lineage cells, ocular epithelial cells, and a plasmacytoid dendritic-cell annotation. It also has multiple disease and phenotype associations.
- **Conclusion**: Established evidence supports ASPH as an endoplasmic-reticulum-associated calcium and protein-modification factor. Its position suggests a possible membrane-calcium component in the module, but the network does not establish a direct calcium-signaling mechanism or a specific disease process.

#### BLVRB

- **Related proteins** (co-abundance neighbors): HSPA2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biliverdin reductase B. The final step in heme metabolism in mammals is catalyzed by the cytosolic biliverdin reductase enzymes A and B (EC 1.3.1.24).[supplied by OMIM, Jul 2009]
- **Diseases (Open Targets)**: neurodegenerative disease (0.125); hepatocellular carcinoma (0.076); cholangiocarcinoma (0.074); ischemic stroke (0.055); neonatal intrahepatic cholestasis due to citrin deficiency (0.045)
- **Europe PMC papers**: 1322
- **Why important**: BLVRB is connected to HSPA2 and adds a heme and erythroid or hematopoietic interpretation. It catalyzes the final step of a biliverdin-reduction route in heme metabolism and is annotated in relation to megakaryocyte differentiation and insulin-receptor signaling. HPA associates it with bone marrow, erythrocytes, erythroid progenitors, hepatocytes, and classical monocytes, and its supplied disease associations include liver and vascular or neurological conditions.
- **Conclusion**: Established evidence supports BLVRB as a cytosolic heme-metabolism enzyme with hematopoietic and hepatic context. Its presence could indicate red-cell or bone-marrow-related composition, or a broader oxidative-metabolic state, but the module alone cannot distinguish these possibilities.

#### MYO1C

- **Related proteins** (co-abundance neighbors): NNT (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies, Plasma membrane; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin IC. This gene encodes a member of the unconventional myosin protein family, which are actin-based molecular motors. The protein is found in the cytoplasm, and one isoform with a unique N-terminus is also found in the nucleus. The nuclear isoform associates with RNA polymerase I and II and functions in transcription initiation. The mouse ortholog of this protein also functions in intracellular vesicle …
- **Diseases (Open Targets)**: neurodegenerative disease (0.381); autosomal dominant nonsyndromic hearing loss (0.370); cutaneous leishmaniasis (0.370); Alzheimer disease (0.182); chronic kidney disease (0.179)
- **Europe PMC papers**: 1069
- **Why important**: MYO1C connects directly to NNT and supplies a cytoskeletal and membrane-trafficking component. Its established functions include actin-based movement, protein targeting to the membrane, endocytosis, intracellular vesicle transport, and roles of a nuclear isoform in transcription initiation. HPA associates it with adipocytes and alveolar cells, and it is detected in prostate. Its literature base is substantial and includes neurological, hearing, infectious, and renal disease associations.
- **Conclusion**: Established evidence supports MYO1C as an actin-associated motor involved in membrane trafficking and transcription. Its link to NNT is compatible with coordinated metabolic and membrane-state variation, but there is no evidence here that MYO1C physically connects the module into a single complex.

## Module 2

**Tissue pair**: prostate and stem_cells  
**Genes (5)**: ATP5F1A, ATP5F1B, HNRNPF, PHB1, PHB2

### Function

The module is best interpreted as a mitochondrial inner-membrane and oxidative-phosphorylation module. The primary evidence is the globally corrected enrichment for the mitochondrial prohibitin complex (GO:CC mitochondrial prohibitin complex; q_global = 0.018), mitochondrial inner membrane (GO:CC mitochondrial inner membrane; q_global = 0.0479), and cell surface (GO:CC cell surface; q_global = 0.0198). ATP5F1A and ATP5F1B additionally support mitochondrial ATP synthase activity through the globally corrected angiostatin-binding and MHC class I protein-binding terms (GO:MF angiostatin binding; q_global = 0.018) (GO:MF MHC class I protein binding; q_global = 0.0424). The coherent interpretation is a structural and energetic mitochondrial program involving the ATP synthase catalytic subunits and the prohibitin complex, with possible cell-surface or signaling-related representation. HNRNPF is not covered by any primary enriched term and may represent a regulatory or sample-context connection rather than the biochemical core.

**Cell composition.** The module does not show a blood-cell signature: every gene has low immune-cell specificity in HPA, and no blood-cell enriched type is reported. It is also not predominantly secreted; HPA reports only one secreted gene in the module, while the individual annotations place the principal genes in mitochondria, membranes, or the nucleoplasm. PHB1 and HNRNPF have low tissue specificity, consistent with broadly used cellular machinery, whereas ATP5F1A, ATP5F1B, and PHB2 show cell-type or tissue enhancement. The repeated HPA enrichment for esophageal basal cells and related epithelial or trophoblast populations suggests that shared cellular states or epithelial-like cell composition could contribute to the cross-tissue signal. All module proteins were detected in prostate, while the stem-cell tissue has no matching HPA tissue entry; therefore the HPA evidence does not establish protein detection in stem cells.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrial prohibitin complex | 0.018 | PHB1, PHB2 |
| GO:MF angiostatin binding | 0.018 | ATP5F1A, ATP5F1B |
| GO:CC cell surface | 0.0198 | ATP5F1A, ATP5F1B, PHB1, PHB2 |
| GO:MF MHC class I protein binding | 0.0424 | ATP5F1A, ATP5F1B |
| GO:CC mitochondrial inner membrane | 0.0479 | ATP5F1A, ATP5F1B, PHB1, PHB2 |

### STRING and hu.MAP

STRING supports a compact, biologically coherent core. ATP5F1A and ATP5F1B have a very strong known association, PHB1 and PHB2 have a very strong known association, and ATP5F1B connects to both prohibitin proteins with strong support. These links reproduce the mitochondrial ATP synthase and prohibitin-complex interpretation and are also reflected in the supplementary STRING terms for the inner mitochondrial membrane, ATP synthase catalytic core, and mitochondrial prohibitin complex (6 supplementary STRING terms; within-query FDR 0.0012–0.0091). The STRING tissue labels involving lymphoblasts and blood cancer cells (STRING TISSUES B-cell lymphoma cell; within-query FDR = 0.0014) (STRING TISSUES Lymphoblast; within-query FDR = 0.0037) (STRING TISSUES Blood cancer cell; within-query FDR = 0.0222) are supplementary context, not evidence of a blood-cell origin or globally significant enrichment. HNRNPF has no reported STRING partner in this module, although it appears in some supplementary tissue labels. hu.MAP independently places PHB1 and PHB2 together in a high-confidence prohibitin complex (hu.MAP huMAP3_01706.1) and in several larger membrane-associated complexes (hu.MAP huMAP3_09671.1) (hu.MAP huMAP3_11743.1) (hu.MAP huMAP3_10725.1). ATP5F1A and ATP5F1B co-occur in several hu.MAP complexes (hu.MAP huMAP3_08750.1) (hu.MAP huMAP3_09307.1) (hu.MAP huMAP3_11095.1), consistent with their membership in ATP synthase assemblies. Thus, most of the module is already supported by known physical or complex-level relationships; the network is not merely a collection of functionally unrelated genes.

**STRING interactions (score >= 0.7)**: 4 of 10 gene pairs: ATP5F1A–ATP5F1B (0.999); ATP5F1B–PHB1 (0.782); ATP5F1B–PHB2 (0.712); PHB1–PHB2 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Inner mitochondrial membrane protein complex (FDR = 0.0012, 4 genes); TISSUES B-cell lymphoma cell (FDR = 0.0014, 4 genes); COMPARTMENTS Inner mitochondrial membrane protein complex (FDR = 0.0016, 4 genes); Component Cell surface (FDR = 0.0036, 4 genes); TISSUES Lymphoblast (FDR = 0.0037, 4 genes); Keyword Mitochondrion inner membrane (FDR = 0.005, 4 genes); Component Mitochondrial proton-transporting ATP synthase, catalytic core (FDR = 0.0076, 2 genes); Component Mitochondrial prohibitin complex (FDR = 0.0076, 2 genes); COMPARTMENTS Mitochondrial proton-transporting ATP synthase, catalytic core (FDR = 0.0091, 2 genes); COMPARTMENTS Mitochondrial prohibitin complex (FDR = 0.0091, 2 genes); COMPARTMENTS Cell surface (FDR = 0.0095, 3 genes); Keyword ATP synthesis (FDR = 0.0167, 2 genes); Keyword CF(1) (FDR = 0.0167, 2 genes); Pfam ATP synthase alpha/beta family, beta-barrel domain (FDR = 0.0214, 2 genes); TISSUES Blood cancer cell (FDR = 0.0222, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01706.1 (PHB1, PHB2; 2/2); huMAP3_09671.1 (PHB1, PHB2; 2/10); huMAP3_11743.1 (PHB1, PHB2; 2/10); huMAP3_08750.1 (ATP5F1B, ATP5F1A; 2/12); huMAP3_09307.1 (ATP5F1B, ATP5F1A; 2/35); huMAP3_11095.1 (ATP5F1B, ATP5F1A; 2/45); huMAP3_10725.1 (PHB1, PHB2; 2/59)

### Novelty

The molecular composition is not a new biological interaction: the ATP5F1A--ATP5F1B pair, the PHB1--PHB2 pair, and links between the ATP synthase and prohibitin components are already represented in STRING and hu.MAP. The potentially novel aspect is the coordinated co-abundance of this compact combination across prostate and stem-cell samples, especially the inclusion of HNRNPF and the particular tissue-pair context. However, the supplied evidence does not compare this module with published co-abundance studies or prior prostate--stem-cell analyses, so the module should be described as a potentially context-specific observation rather than a definitively new discovery. Absence of a reported HNRNPF complex link in these resources is insufficient by itself to establish novelty.

**Hypothesis.** Hypothesis: a shared mitochondrial energy and membrane-organization state is active in the prostate and stem-cell samples. In this model, ATP5F1A and ATP5F1B form the ATP synthase catalytic component, while PHB1 and PHB2 organize or stabilize mitochondrial inner-membrane architecture and may couple membrane organization to cellular signaling. HNRNPF may be co-abundant because an RNA-processing program supports the same cellular state, but its connection to the mitochondrial core is presently speculative. The cell-surface and angiostatin-binding annotations could reflect signaling, membrane localization, or shared cellular composition; they should not be interpreted as proof that the entire module is extracellular. This hypothesis requires validation with protein-complex assays, compartment-resolved measurements, and independent prostate and stem-cell cohorts.

### Important genes

#### ATP5F1A

- **Related proteins** (co-abundance neighbors): PHB1 (0.85), ATP5F1B (0.84), PHB2 (0.82); STRING partners: ATP5F1B (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_08750.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit alpha. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, using an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic po…
- **Diseases (Open Targets)**: mitochondrial complex V (ATP synthase) deficiency, nuclear type 4A (0.655); mitochondrial proton-transporting ATP synthase complex deficiency (0.648); mitochondrial complex V (ATP synthase) deficiency, nuclear type 4B (0.532); hereditary disease (0.394); Mitochondrial encephalopathy (0.371)
- **Europe PMC papers**: 822
- **Why important**: ATP5F1A has the strongest network position in the module, connecting to ATP5F1B, PHB1, and PHB2. It is present in the primary mitochondrial inner-membrane, cell-surface, angiostatin-binding, and MHC class I protein-binding terms (4 globally significant GO/KEGG terms, q_global 0.018–0.0479; see the table), and in multiple hu.MAP ATP synthase complexes (hu.MAP huMAP3_08750.1) (hu.MAP huMAP3_09307.1) (hu.MAP huMAP3_11095.1). Its annotation directly links it to mitochondrial ATP synthase, oxidative phosphorylation, ATP biosynthesis, and proton-motive-force-driven ATP synthesis. It is detected in prostate and has substantial literature support.
- **Conclusion**: Established conclusion: ATP5F1A is a central energetic component and a strong anchor for the mitochondrial interpretation. Hypothesis: its co-abundance with prohibitin proteins may indicate coordinated coupling between ATP synthase function and inner-membrane organization.

#### ATP5F1B

- **Related proteins** (co-abundance neighbors): ATP5F1A (0.84), PHB2 (0.81); STRING partners: ATP5F1A (0.999), PHB1 (0.782), PHB2 (0.712)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_08750.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit beta. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: hypermetabolism due to uncoupled mitochondrial oxidative phosphorylation 2 (0.499); hypertrophic cardiomyopathy (0.212); Alzheimer disease (0.177); hypertensive disorder (0.117); response to xenobiotic stimulus (0.117)
- **Europe PMC papers**: 735
- **Why important**: ATP5F1B is a core network member connected to ATP5F1A, PHB1, and PHB2, with the strongest STRING support for the ATP synthase pair and additional support for links to both prohibitin proteins. It contributes to all primary mitochondrial and cell-surface terms involving the ATP synthase subunits (4 globally significant GO/KEGG terms, q_global 0.018–0.0479; see the table) and to the ATP synthase complexes in hu.MAP (hu.MAP huMAP3_08750.1) (hu.MAP huMAP3_09307.1) (hu.MAP huMAP3_11095.1). Its established functions include mitochondrial ATP synthesis, energy generation, and proton-motive-force-driven oxidative phosphorylation. It is detected in prostate and has substantial disease and literature annotation.
- **Conclusion**: Established conclusion: ATP5F1B is a second core energetic component and reinforces that the module contains a genuine ATP synthase signal. Hypothesis: variation in this module may mark differences in mitochondrial energy demand or respiratory capacity between shared prostate and stem-cell states.

#### PHB1

- **Related proteins** (co-abundance neighbors): ATP5F1A (0.85), HNRNPF (0.82); STRING partners: ATP5F1B (0.782), PHB2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_01706.1, huMAP3_09671.1, huMAP3_11743.1, huMAP3_10725.1
- **Function (MyGene.info)**: prohibitin 1. This gene is evolutionarily conserved, and its product is proposed to play a role in human cellular senescence and tumor suppression. Antiproliferative activity is reported to be localized to the 3' UTR, which is proposed to function as a trans-acting regulatory RNA. Several pseudogenes of this gene have been identified. Alternative splicing results in multiple transcript variants. [provided by Re…
- **Diseases (Open Targets)**: coronary artery disorder (0.458); myocardial ischemia (0.454); hypertensive disorder (0.396); heart disorder (0.343); asthma (0.339)
- **Europe PMC papers**: 1249
- **Why important**: PHB1 is one half of the globally significant mitochondrial prohibitin-complex signal (GO:CC mitochondrial prohibitin complex; q_global = 0.018) and is also included in the mitochondrial inner-membrane and cell-surface terms (GO:CC cell surface; q_global = 0.0198) (GO:CC mitochondrial inner membrane; q_global = 0.0479). It connects in the module to ATP5F1A and HNRNPF, while STRING supports its associations with ATP5F1B and PHB2. hu.MAP places it with PHB2 in a high-confidence prohibitin complex and in broader membrane-related complexes (hu.MAP huMAP3_01706.1) (hu.MAP huMAP3_09671.1) (hu.MAP huMAP3_11743.1) (hu.MAP huMAP3_10725.1). Its annotation supports roles in mitochondrion organization, transcriptional regulation, cellular senescence, and tumor suppression, and it has substantial literature support.
- **Conclusion**: Established conclusion: PHB1 is a structural and regulatory anchor of the prohibitin-centered mitochondrial component. Hypothesis: PHB1 may help connect mitochondrial organization with the cellular-state or tumor-suppressive programs represented in the prostate and stem-cell samples.

#### PHB2

- **Related proteins** (co-abundance neighbors): ATP5F1A (0.82), ATP5F1B (0.81); STRING partners: ATP5F1B (0.712), PHB1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_01706.1, huMAP3_09671.1, huMAP3_11743.1, huMAP3_10725.1
- **Function (MyGene.info)**: prohibitin 2. Enables several functions, including protein C-terminus binding activity; protein N-terminus binding activity; and protein dimerization activity. Involved in several processes, including defense response to virus; positive regulation of cell cycle phase transition; and regulation of transcription, DNA-templated. Located in several cellular components, including cell surface; mitochondrial membrane…
- **Diseases (Open Targets)**: breast cancer (0.101); breast carcinoma (0.101); neoplasm (0.100); non-small cell lung carcinoma (0.096); colorectal carcinoma (0.085)
- **Europe PMC papers**: 2714
- **Why important**: PHB2 is the other member of the globally significant prohibitin-complex term (GO:CC mitochondrial prohibitin complex; q_global = 0.018) and contributes to the primary mitochondrial inner-membrane and cell-surface terms (GO:CC cell surface; q_global = 0.0198) (GO:CC mitochondrial inner membrane; q_global = 0.0479). It connects to both ATP synthase subunits in the module, has a strong STRING association with PHB1, and occurs with PHB1 in the high-confidence hu.MAP prohibitin complex and larger membrane complexes (hu.MAP huMAP3_01706.1) (hu.MAP huMAP3_09671.1) (hu.MAP huMAP3_11743.1) (hu.MAP huMAP3_10725.1). Its established annotations include mitochondrial organization, mitophagy, protein binding, dimerization, transcriptional regulation, and cell-surface localization. It has particularly broad literature support and reported cancer associations.
- **Conclusion**: Established conclusion: PHB2 is a central prohibitin-complex component that links the module's mitochondrial structure to the ATP synthase subunits. Hypothesis: PHB2 may be especially relevant to quality control or remodeling of mitochondria in the shared cellular state.

#### HNRNPF

- **Related proteins** (co-abundance neighbors): PHB1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein F. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins that complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and regulate alternative splicing, polyadenylation, and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present…
- **Diseases (Open Targets)**: neurodegenerative disease (0.518); dengue disease (0.370); knee fracture (0.322); breast cancer (0.103); posterior cortical atrophy (0.083)
- **Europe PMC papers**: 971
- **Why important**: HNRNPF is the least connected module member, with only a PHB1 edge, no reported STRING partner, and no hu.MAP complex assignment. It does not occur in any primary GO or KEGG term, but it appears in supplementary STRING tissue labels involving lymphoblasts and blood cancer cells (STRING TISSUES B-cell lymphoma cell; within-query FDR = 0.0014) (STRING TISSUES Lymphoblast; within-query FDR = 0.0037) (STRING TISSUES Blood cancer cell; within-query FDR = 0.0222). Its established function is as a broadly expressed nuclear RNA-binding protein involved in pre-mRNA processing, splicing, polyadenylation, and RNA transport. It is detected in prostate and has substantial literature support.
- **Conclusion**: Established conclusion: HNRNPF is a plausible RNA-processing marker associated with the module but not a demonstrated member of its mitochondrial biochemical core. Hypothesis: its co-abundance with PHB1 may reflect coordinated RNA and mitochondrial remodeling, or it may be a context-specific passenger caused by shared cellular state.

## Module 3

**Tissue pair**: prostate and stem_cells  
**Genes (11)**: CPD, EGFR, GMPR2, GNAS, GNAS, MYOF, RAB21, TIGAR, UGGT1, WASHC4, WASHC5

### Function

The strongest functional interpretation is an endosomal membrane-trafficking and receptor-handling module. The sole globally corrected GO/KEGG primary result is (GO:CC early endosome membrane; q_global = 0.0392), an early endosome membrane term containing EGFR, RAB21, WASHC4 and WASHC5. This interpretation is independently supported by the supplementary STRING result (STRING Component Early endosome membrane; within-query FDR = 0.0256). The network is sparse but organized around EGFR, with links to MYOF, GNAS, CPD and WASHC4, while WASHC4 and WASHC5 form a particularly strong pair. The remaining genes plausibly connect membrane trafficking with receptor processing, protein quality control, nucleotide metabolism, cellular stress and membrane repair. No KEGG term passed global correction; the only globally significant enrichment is the GO cellular-component result (GO:CC early endosome membrane; q_global = 0.0392).

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the HPA summary identifies only a small subset as secreted, and most members are intracellular or membrane-associated. Most genes have low tissue specificity, whereas many show cell-type enhancement. Neutrophil-associated signals recur among CPD, WASHC4 and RAB21, with additional signals involving monocytes, microglia, oligodendrocytes and reproductive or epithelial cell types. Therefore the prostate association is not sufficient to claim a prostate-specific program. Shared cell populations, immune-cell admixture, or sample-composition effects could contribute, although the HPA protein evidence detects all module proteins in prostate. The stem-cell tissue comparison has no matching HPA tissue-level protein evidence, so that part of the interpretation remains limited.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC early endosome membrane | 0.0392 | EGFR, RAB21, WASHC4, WASHC5 |

### STRING and hu.MAP

STRING provides only two high-confidence pairwise relationships within the module: EGFR with GNAS (STRING Component Early endosome membrane; within-query FDR = 0.0256) and WASHC4 with WASHC5. The WASHC4-WASHC5 relationship is also supported by every reported hu.MAP complex, including a high-confidence complex in which both module members account for the complete reported complex membership (hu.MAP huMAP3_05454.1). The other hu.MAP entries place the same pair within larger complexes (hu.MAP huMAP3_06652.1), (hu.MAP huMAP3_08077.1), (hu.MAP huMAP3_10870.1) and (hu.MAP huMAP3_12900.1). Thus the WASH pair is an established physical or complex-level anchor, while the broader eleven-gene co-abundance structure is not fully reproduced by known STRING or hu.MAP relationships. The limited overlap suggests that co-abundance captures a shared cellular state or pathway context in addition to stable physical interactions.

**STRING interactions (score >= 0.7)**: 2 of 55 gene pairs: EGFR–GNAS (0.718); WASHC4–WASHC5 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Early endosome membrane (FDR = 0.0256, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05454.1 (WASHC5, WASHC4; 2/2); huMAP3_06652.1 (WASHC5, WASHC4; 2/14); huMAP3_08077.1 (WASHC5, WASHC4; 2/16); huMAP3_10870.1 (WASHC5, WASHC4; 2/20); huMAP3_12900.1 (WASHC5, WASHC4; 2/50)

### Novelty

The module appears biologically coherent but should not be called a wholly new molecular complex. The WASHC4-WASHC5 association is already represented in STRING and hu.MAP, and early-endosome functions of EGFR, RAB21 and the WASH components are established by the primary enrichment and gene annotations. A potentially novel aspect is the specific co-abundance combination linking this WASH pair with EGFR, MYOF, CPD, UGGT1, GNAS, TIGAR and GMPR2 across prostate and stem-cell samples. However, absence of most module edges from reference resources does not establish novelty: co-abundance can reflect shared regulation, cell composition, or context-dependent biology, and reference databases are incomplete. The appropriate conclusion is a potentially novel cross-tissue co-abundance signature built around a known endosomal-trafficking core.

**Hypothesis.** Hypothesis: in the shared prostate and stem-cell context, coordinated abundance of WASHC4 and WASHC5 may support WASH-complex organization of endosomal actin and membrane traffic, while RAB21 and MYOF influence trafficking, adhesion or membrane-remodeling events and EGFR supplies a regulated cell-surface receptor cargo or signaling input. CPD and UGGT1 could reflect associated protein-processing demands, whereas GNAS and TIGAR could couple receptor-linked signaling to metabolic or stress adaptation. This model predicts coordinated endosomal receptor turnover and trafficking-related cell-state regulation, but the co-abundance data alone do not establish directionality, physical interaction, or causation.

### Important genes

#### EGFR

- **Related proteins** (co-abundance neighbors): MYOF (0.89), GNAS (0.84), GNAS (0.84), CPD (0.83), WASHC4 (0.82); STRING partners: GNAS (0.718)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus, Plasma membrane; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: epidermal growth factor receptor. The protein encoded by this gene is a transmembrane glycoprotein that is a member of the protein kinase superfamily. This protein is a receptor for members of the epidermal growth factor family. EGFR is a cell surface protein that binds to epidermal growth factor, thus inducing receptor dimerization and tyrosine autophosphorylation leading to cell proliferation. Mutations in this gene are associat…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.850); lung adenocarcinoma (0.774); cancer (0.737); head and neck squamous cell carcinoma (0.725); lung cancer (0.717)
- **Europe PMC papers**: 223694
- **Why important**: EGFR has the strongest network position, connects to several module members, and is one of the four genes in the primary early-endosome membrane enrichment (GO:CC early endosome membrane; q_global = 0.0392). It is a plasma-membrane receptor tyrosine kinase involved in receptor signaling and proliferation, has a strong disease and cancer literature, and is detected in prostate. Its link to GNAS is also the only STRING-supported signaling relationship involving EGFR in this module.
- **Conclusion**: Established: EGFR is a central receptor and an evidence-backed component of the enriched early-endosome membrane context. Hypothesis: its co-abundance may mark coordinated receptor internalization or endosomal signaling in the shared module; the module does not prove that EGFR initiates the program.

#### WASHC4

- **Related proteins** (co-abundance neighbors): GMPR2 (0.87), WASHC5 (0.84), EGFR (0.82); STRING partners: WASHC5 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_05454.1, huMAP3_06652.1, huMAP3_08077.1, huMAP3_10870.1, huMAP3_12900.1
- **Function (MyGene.info)**: WASH complex subunit 4. This gene encodes a component of the WASH complex, which functions in the intracellular transport of endosomes. Mutations in this gene have been detected in individuals with autosomal recessive cognitive disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014].
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.611); Intellectual disability (0.345); mathematical ability (0.322); Abnormality of the skeletal system (0.148); corneal ulcer (0.140)
- **Europe PMC papers**: 116
- **Why important**: WASHC4 is part of the primary enrichment (GO:CC early endosome membrane; q_global = 0.0392), has a direct high-confidence STRING relationship with WASHC5, and appears with WASHC5 in all reported hu.MAP complexes (hu.MAP huMAP3_05454.1) through (hu.MAP huMAP3_12900.1). Its annotation directly concerns endosome organization, endosomal transport and Arp two-thirds complex-mediated actin nucleation. It also provides a possible immune-cell composition caveat through neutrophil and neutrophil-progenitor enhancement.
- **Conclusion**: Established: WASHC4 is a molecular anchor for the endosomal and WASH-complex interpretation. Hypothesis: its abundance may report activity or abundance of WASH-dependent endosomal actin remodeling in the shared samples, potentially mixed with neutrophil-related signal.

#### WASHC5

- **Related proteins** (co-abundance neighbors): WASHC4 (0.84); STRING partners: WASHC4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_05454.1, huMAP3_06652.1, huMAP3_08077.1, huMAP3_10870.1, huMAP3_12900.1
- **Function (MyGene.info)**: WASH complex subunit 5. This gene encodes a 134 kDa protein named strumpellin that is predicted to have multiple transmembrane domains and a spectrin-repeat-containing domain. This ubiquitously expressed gene has its highest expression in skeletal muscle. The protein is named for Strumpell disease; a form of hereditary spastic paraplegia (HSP). Spastic paraplegias are a diverse group of disorders in which the autosomal d…
- **Diseases (Open Targets)**: hereditary spastic paraplegia 8 (0.802); Ritscher-Schinzel syndrome 1 (0.727); Ritscher-Schinzel syndrome (0.711); hereditary disease (0.493); hereditary spastic paraplegia (0.350)
- **Europe PMC papers**: 238
- **Why important**: WASHC5 is the direct partner of WASHC4 in STRING and is present with it in every hu.MAP complex reported for the module, including (hu.MAP huMAP3_05454.1). Its annotation supports endosome organization, endosomal transport, actin filament polymerization and regulation of Arp two-thirds complex-mediated actin nucleation. Its disease associations with hereditary spastic paraplegia and related syndromes emphasize the functional importance of membrane and cytoskeletal trafficking.
- **Conclusion**: Established: WASHC5 is a strongly supported component of a WASH-associated trafficking unit. Hypothesis: coordinated WASHC4-WASHC5 abundance may represent assembly or activity of an endosomal actin-remodeling machinery, although co-abundance cannot distinguish complex assembly from shared regulation.

#### RAB21

- **Related proteins** (co-abundance neighbors): MYOF (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB21, member RAS oncogene family. This gene belongs to the Rab family of monomeric GTPases, which are involved in the control of cellular membrane traffic. The encoded protein plays a role in the targeted trafficking of integrins via its association with integrin alpha tails. As a consequence, the encoded protein is involved in the regulation of cell adhesion and migration. Expression of this gene is associated with a poor prognos…
- **Diseases (Open Targets)**: neurodegenerative disease (0.469); small intestine neuroendocrine neoplasm (0.095); neoplasm (0.085); posterior cortical atrophy (0.074); nonpapillary renal cell carcinoma (0.065)
- **Europe PMC papers**: 999
- **Why important**: RAB21 is one of the four genes in (GO:CC early endosome membrane; q_global = 0.0392) and (STRING Component Early endosome membrane; within-query FDR = 0.0256). Its established function as a Rab-family membrane-trafficking regulator, including receptor-mediated endocytosis and integrin trafficking, gives it a direct mechanistic bridge between the early-endosome signal and cell adhesion or migration. Its connection to MYOF adds a membrane-trafficking link within the module, while its neutrophil and spermatid cell-type signals warrant attention to sample composition.
- **Conclusion**: Established: RAB21 is a functionally appropriate endosomal-trafficking marker and part of the primary enriched set. Hypothesis: it may coordinate internalization or recycling of EGFR-related and adhesion-associated cargo in this module; the available evidence does not establish a direct RAB21-EGFR interaction here.

#### TIGAR

- **Related proteins** (co-abundance neighbors): GNAS (0.84), GNAS (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TP53 induced glycolysis regulatory phosphatase. This gene is regulated as part of the p53 tumor suppressor pathway and encodes a protein with sequence similarity to the bisphosphate domain of the glycolytic enzyme that degrades fructose-2,6-bisphosphate. The protein functions by blocking glycolysis and directing the pathway into the pentose phosphate shunt. Expression of this protein also protects cells from DNA damaging reactive oxygen species…
- **Diseases (Open Targets)**: diabetes mellitus (0.538); type 2 diabetes mellitus (0.417); diabetic eye disease (0.375); cellulitis (0.282); brain aneurysm (0.217)
- **Europe PMC papers**: 2419
- **Why important**: TIGAR links the module to cellular stress, p53-associated regulation, glycolysis control and the pentose-phosphate shunt. It is connected in the module to the GNAS entries, providing a possible metabolic or stress-response branch alongside the trafficking core. Its literature is substantial compared with several peripheral module members, and it is detected in prostate, although it has no primary enrichment or STRING annotation in this module.
- **Conclusion**: Established: TIGAR is a stress and metabolic regulator that occupies a peripheral network position rather than a proven endosomal core position. Hypothesis: it may reflect metabolic adaptation accompanying receptor trafficking or altered cellular stress in the shared samples; this link is currently inferential.

## Module 4

**Tissue pair**: prostate and stem_cells  
**Genes (22)**: CLUH, EIF3C, EPS8L2, GNPNAT1, HDGF, HMGB3, LMNB1, SLC16A1, PNP, PPP4C, RBBP4, RSL1D1, SNRPA1, SNRPB2, SF3B3, SUPT16H, TCOF1, CCT3, CCT7, ALYREF, TPD52, VKORC1L1

### Function

The module is best interpreted as a mixed core-cellular machinery module rather than a single statistically established pathway. Its strongest coherent biological themes are pre-mRNA splicing and spliceosomal assembly, represented by SF3B3, SNRPA1, and SNRPB2; cytoplasmic translation initiation, represented by EIF3C; protein folding and proteostasis, represented by CCT3 and CCT7; and coupled nuclear growth, chromatin, and metabolic functions represented by HDGF, RBBP4, TCOF1, SLC16A1, and related genes. No GO or KEGG term passed global correction, so these functional themes are annotations and network-based interpretation, not globally significant enrichment claims. The module may therefore reflect coordinated abundance of broadly required cellular processes in prostate and stem-cell samples.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: only HDGF is annotated as secreted to blood, while the remaining genes are intracellular or membrane-associated. It is also not strongly blood-cell specific according to HPA, although several genes show enhanced signals in bone marrow, lymphoid or hematopoietic cell types, and some show immune-cell enhancement. Most genes have low tissue specificity, and many are detected in prostate. The HPA pattern is compatible with broadly expressed housekeeping or proliferative cellular machinery, with possible contributions from shared progenitor or other cell states rather than evidence for a prostate-specific secreted program. The stem-cell interpretation should therefore consider shared cell composition and cellular state as alternative explanations.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a coherent spliceosomal cluster involving SF3B3, SNRPA1, and SNRPB2, and a chaperonin-associated cluster involving CCT3, CCT7, and PPP4C, with EIF3C connected to CCT7. These are established protein relationships and support that parts of the co-abundance module recover known molecular machinery. hu.MAP independently places SF3B3, SNRPA1, and SNRPB2 together in complexes (hu.MAP huMAP3_06511.1), (hu.MAP huMAP3_08980.1), and (hu.MAP huMAP3_04549.1), while CCT3 and CCT7 recur together in (hu.MAP huMAP3_01951.1), (hu.MAP huMAP3_07938.1), (hu.MAP huMAP3_06559.1), (hu.MAP huMAP3_09191.1), (hu.MAP huMAP3_10656.1), and (hu.MAP huMAP3_14584.1). The module therefore contains validated submodules rather than a uniformly novel physical complex. Most other co-abundance links lack matching STRING or hu.MAP support, which is consistent with indirect regulation, shared cell state, co-expression, or incomplete interaction databases.

**STRING interactions (score >= 0.7)**: 7 of 231 gene pairs: CCT3–CCT7 (0.999); CCT3–PPP4C (0.79); CCT7–EIF3C (0.728); CCT7–PPP4C (0.815); SF3B3–SNRPA1 (0.999); SF3B3–SNRPB2 (0.999); SNRPA1–SNRPB2 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06511.1 (SNRPB2, SNRPA1, SF3B3; 3/79); huMAP3_08980.1 (SNRPB2, SNRPA1, SF3B3; 3/97); huMAP3_01951.1 (CCT3, CCT7; 2/8); huMAP3_07938.1 (CCT3, CCT7; 2/23); huMAP3_06559.1 (CCT3, CCT7; 2/25); huMAP3_09191.1 (CCT3, CCT7; 2/32); huMAP3_10656.1 (CCT3, CCT7; 2/36); huMAP3_04549.1 (SNRPB2, SF3B3; 2/52); huMAP3_14584.1 (CCT3, CCT7; 2/61)

### Novelty

The module should not be called a newly discovered molecular complex or pathway. Its spliceosomal and chaperonin components are already represented by STRING and hu.MAP, and the individual functions of many genes are well established. A potentially novel aspect is the repeated co-abundance of these established machineries across prostate and stem-cell groups, together with the links connecting RNA processing, translation, proteostasis, chromatin, and metabolism. However, absence of some edges from STRING or hu.MAP does not prove novelty. The appropriate claim is a potentially informative cross-tissue co-abundance configuration that requires replication, cell-composition control, and experimental testing.

**Hypothesis.** Hypothesis: the module reflects a shared progenitor-like or proliferative cellular state in which efficient RNA processing supports translation, chaperonin activity stabilizes newly made proteins, and chromatin or nucleolar machinery sustains transcriptional and ribosomal capacity. SLC16A1 could couple this state to monocarboxylate metabolism, while HDGF, HMGB3, RBBP4, and TCOF1 could connect growth, chromatin, and nucleolar regulation. This is a mechanistic hypothesis, not an enrichment result; it should be tested by examining the module after adjustment for cell type, proliferation, and sample blood contamination, and by perturbing the proposed RNA-processing, chaperone, and metabolic components.

### Important genes

#### SF3B3

- **Related proteins** (co-abundance neighbors): SNRPA1 (0.89), GNPNAT1 (0.87), EIF3C (0.85), RSL1D1 (0.84), ALYREF (0.81); STRING partners: SNRPA1 (0.999), SNRPB2 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Nucleoli rim; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1, huMAP3_04549.1
- **Function (MyGene.info)**: splicing factor 3b subunit 3. This gene encodes subunit 3 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); dengue disease (0.370); cervical cancer (0.189); cervical carcinoma (0.189); prostate cancer (0.111)
- **Europe PMC papers**: 965
- **Why important**: SF3B3 is a central connector within the module and is directly supported by STRING and hu.MAP relationships with SNRPA1 and SNRPB2. It is a subunit of the SF3B complex and U2 snRNP, with established roles in spliceosome assembly and pre-mRNA splicing. Its prostate detection, nuclear localization, disease associations including prostate cancer, and substantial literature make it a strong anchor for the RNA-processing interpretation.
- **Conclusion**: Established evidence supports SF3B3 as a spliceosomal component and as part of a known interaction cluster. It is plausible, but not demonstrated here, that SF3B3 helps coordinate the module's cross-tissue co-abundance.

#### SNRPA1

- **Related proteins** (co-abundance neighbors): SF3B3 (0.89), RSL1D1 (0.83), GNPNAT1 (0.82), SLC16A1 (0.82), EIF3C (0.82); STRING partners: SF3B3 (0.999), SNRPB2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein polypeptide A'. Enables RNA binding activity. Involved in mRNA splicing, via spliceosome and spermatogenesis. Located in nuclear speck. Part of U2-type catalytic step 2 spliceosome and U2-type precatalytic spliceosome. Implicated in connective tissue disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.538); dengue disease (0.370); phosphorus metabolism disease (0.196); hypotensive disorder (0.196); cancer (0.087)
- **Europe PMC papers**: 520
- **Why important**: SNRPA1 is a highly connected module member and forms a strongly supported interaction cluster with SF3B3 and SNRPB2 in STRING and hu.MAP complexes (hu.MAP huMAP3_06511.1), (hu.MAP huMAP3_08980.1), and (hu.MAP huMAP3_04549.1). It is a U2 snRNP component involved in spliceosomal assembly, mRNA splicing, and spermatogenesis. Its nuclear localization, broad tissue profile, and established literature support make it a representative core gene rather than a peripheral association.
- **Conclusion**: Established evidence identifies SNRPA1 as part of the U2 spliceosomal machinery. The module data support coordinated abundance of this machinery, but do not establish a new SNRPA1-specific regulatory mechanism.

#### CCT7

- **Related proteins** (co-abundance neighbors): HMGB3 (0.85), RBBP4 (0.83); STRING partners: CCT3 (0.999), EIF3C (0.728), PPP4C (0.815)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_01951.1, huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 links the module to the CCT or TRiC chaperonin system and is repeatedly recovered with CCT3 across hu.MAP complexes (hu.MAP huMAP3_01951.1), (hu.MAP huMAP3_07938.1), (hu.MAP huMAP3_06559.1), (hu.MAP huMAP3_09191.1), (hu.MAP huMAP3_10656.1), and (hu.MAP huMAP3_14584.1). STRING also supports its relationships with CCT3 and PPP4C and connects it to EIF3C. Its known function in ATP-dependent folding of proteins including actin and tubulin, together with its prostate detection and broad literature, makes it important for interpreting the module as a proteostasis-linked cellular program.
- **Conclusion**: Established evidence supports CCT7 as a component of the CCT folding machinery and as part of a known interaction subnetwork. Its proposed role in coupling proteostasis to the other module processes remains a hypothesis.

#### EIF3C

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.86), CLUH (0.85), SF3B3 (0.85), GNPNAT1 (0.85), SNRPA1 (0.82), PNP (0.81); STRING partners: CCT7 (0.728)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C has prominent network connectivity and connects translation initiation to the module's spliceosomal and chaperone-associated genes. It is a subunit of eIF3 and is annotated for cytoplasmic translation initiation and positive regulation of translation. Its broad tissue profile, prostate detection, cancer associations, and substantial literature make it a useful indicator of a general biosynthetic or proliferative state.
- **Conclusion**: Established evidence supports EIF3C in translation-initiation machinery. The co-abundance pattern is consistent with coordinated RNA processing and translation, but it does not prove that EIF3C functionally drives the module.

#### HDGF

- **Related proteins** (co-abundance neighbors): TCOF1 (0.93), VKORC1L1 (0.83), SLC16A1 (0.81), SUPT16H (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparin binding growth factor. This gene encodes a member of the hepatoma-derived growth factor family. The encoded protein has mitogenic and DNA-binding activity and may play a role in cellular proliferation and differentiation. High levels of expression of this gene enhance the growth of many tumors. This gene was thought initially to be located on chromosome X; however, that location has been determined to correspond to a re…
- **Diseases (Open Targets)**: prostate carcinoma (0.394); neurodegenerative disease (0.287); hepatocellular carcinoma (0.115); neoplasm (0.112); non-small cell lung carcinoma (0.111)
- **Europe PMC papers**: 2439
- **Why important**: HDGF occupies a connecting position between TCOF1, VKORC1L1, SLC16A1, and SUPT16H and is the module's annotated secreted-to-blood protein. It has mitogenic, DNA-binding, transcriptional, chromatin-remodeling, and cell-division annotations, prostate carcinoma association, prostate detection, and extensive literature. It could therefore connect growth-related nuclear functions with the module's metabolic and biosynthetic components, while also requiring attention to possible extracellular or sample-handling effects.
- **Conclusion**: Established evidence supports HDGF as a growth- and chromatin-associated protein with blood secretion annotation. A coordinating role within this module is plausible but not established by the co-abundance data.

#### SLC16A1

- **Related proteins** (co-abundance neighbors): TPD52 (0.91), SNRPA1 (0.82), HDGF (0.81), LMNB1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cell Junctions; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 16 member 1. The protein encoded by this gene is a proton-linked monocarboxylate transporter that catalyzes the movement of many monocarboxylates, such as lactate and pyruvate, across the plasma membrane. Mutations in this gene are associated with erythrocyte lactate transporter defect. Alternatively spliced transcript variants have been found for this gene.[provided by RefSeq, Oct 2009].
- **Diseases (Open Targets)**: exercise-induced hyperinsulinism (0.720); ketoacidosis due to monocarboxylate transporter-1 deficiency (0.717); metabolic myopathy due to lactate transporter defect (0.707); neurodegenerative disease (0.509); inborn errors of metabolism (0.370)
- **Europe PMC papers**: 6642
- **Why important**: SLC16A1 provides the clearest metabolic and membrane interface in the module. It transports lactate, pyruvate, and other monocarboxylates and connects in the network to TPD52, SNRPA1, HDGF, and LMNB1. Its prostate detection, cell-type-enhanced patterns, and well-established disease associations involving lactate transport make it important for testing whether the module reflects metabolic adaptation rather than only RNA and protein machinery.
- **Conclusion**: Established evidence supports SLC16A1 as a monocarboxylate transporter with a direct metabolic role. Its connection to the RNA-processing and nuclear components is a module-level hypothesis, not a demonstrated physical mechanism.

## Module 5

**Tissue pair**: prostate and stem_cells  
**Genes (6)**: EWSR1, EXOSC6, EIF6, JPT2, PSME3IP1, CCT8

### Function

The module most plausibly represents a broadly expressed intracellular gene-expression and protein-homeostasis program. EIF6 is associated with translation initiation, ribosomal-subunit export, and ribosomal-RNA maturation; EXOSC6 is a component of the RNA exosome involved in RNA degradation and processing; EWSR1 participates in transcriptional regulation and RNA processing; CCT8 contributes to chaperonin-mediated protein folding; PSME3IP1 is associated with splicing and negative regulation of proteasomal protein catabolism; and JPT2 has annotations related to calcium-mediated signaling and endocytosis. The co-abundance structure links EIF6 with several genes and connects RNA processing, translation, and protein-folding components, but it does not establish physical interaction or a single pathway. No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The lack of a globally enriched term does not invalidate the module.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. All genes have low immune-cell specificity, and the HPA profile does not support a blood-cell-enriched module. Most genes have low tissue specificity, which is compatible with broadly expressed housekeeping-like intracellular functions. A subset shows cell-type enhancement, including spermatid-associated expression for PSME3IP1 and JPT2, oocyte enhancement for CCT8, and epithelial or progenitor-associated enhancement for EIF6. JPT2 is tissue-enhanced in brain. These observations raise the possibility that the shared prostate and stem-cell signal reflects broadly expressed cellular machinery, with a possible contribution from shared reproductive or epithelial cell states, rather than a prostate-specific secreted or immune program. HPA protein detection is present for several genes in prostate, whereas there is no matching HPA tissue assessment for stem_cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. Therefore, the co-abundance edges should be interpreted as coordinated abundance relationships rather than established physical interactions. The annotations nevertheless suggest biologically related intracellular processes: RNA maturation and degradation, translation, protein folding, transcriptional regulation, and proteasomal control. The lack of STRING and hu.MAP support means that the network is not corroborated as a known multiprotein complex or canonical interaction neighborhood.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a previously unrecognized co-abundance pattern shared by prostate and stem_cells, because the module has no reported STRING or hu.MAP support and no globally significant GO or KEGG enrichment. However, it cannot be called a definitively new biological discovery. Database absence does not prove novelty, and the genes are mostly broadly expressed intracellular factors with substantial prior literature. The most defensible conclusion is that the tissue-pair co-abundance arrangement may be novel, while the underlying gene functions are established and individually well studied to differing degrees.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in which RNA maturation and surveillance, translation, protein folding, and regulated protein turnover are coordinately maintained. EIF6 may occupy a central abundance-position linking translation-related activity with RNA-processing and regulatory components, while EXOSC6, EWSR1, and CCT8 represent complementary RNA-handling, transcriptional, and proteostasis functions. Cell-composition effects, particularly shared epithelial or reproductive cell states, could generate part of this coordinated signal. This is a mechanistic hypothesis, not a demonstrated physical pathway or causal mechanism.

### Important genes

#### EIF6

- **Related proteins** (co-abundance neighbors): PSME3IP1 (0.86), EXOSC6 (0.84), EWSR1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 6. Hemidesmosomes are structures which link the basal lamina to the intermediate filament cytoskeleton. An important functional component of hemidesmosomes is the integrin beta-4 subunit (ITGB4), a protein containing two fibronectin type III domains. The protein encoded by this gene binds to the fibronectin type III domains of ITGB4 and may help link ITGB4 to the intermediate filament cytoskeleton. T…
- **Diseases (Open Targets)**: neurodegenerative disease (0.153); urolithiasis (0.135); alcohol drinking (0.135); exstrophy-epispadias complex (0.118); freckles (0.115)
- **Europe PMC papers**: 1420
- **Why important**: EIF6 has the most connected position in the module and links PSME3IP1, EXOSC6, and EWSR1. Its established annotations connect translation initiation, ribosomal-subunit export, ribosomal-RNA maturation, and regulation of glycolytic processes. It is broadly expressed, detected in prostate, and has substantial literature, making it the strongest candidate for organizing the module's translation and RNA-related interpretation.
- **Conclusion**: Established evidence supports EIF6 as a translation- and ribosome-associated factor with a central co-abundance position. It is reasonable to hypothesize that EIF6 marks the shared intracellular program, but the network does not prove that EIF6 regulates the other module genes.

#### EXOSC6

- **Related proteins** (co-abundance neighbors): CCT8 (0.85), EIF6 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exosome component 6. This gene product constitutes one of the subunits of the multisubunit particle called exosome, which mediates mRNA degradation. The composition of human exosome is similar to its yeast counterpart. This protein is homologous to the yeast Mtr3 protein. Its exact function is not known, however, it has been shown using a cell-free RNA decay system that the exosome is required for rapid degradation of…
- **Diseases (Open Targets)**: neurodegenerative disease (0.499); osteoarthritis, hip (0.095); osteoarthritis, knee (0.092); total joint arthroplasty (0.077); refractive error (0.053)
- **Europe PMC papers**: 221
- **Why important**: EXOSC6 connects to EIF6 and CCT8 and is a defined component of the multisubunit RNA exosome. Its annotations support RNA processing, RNA catabolism, ribosomal-RNA catabolism, and small-nuclear-RNA processing. This provides a mechanistic bridge between the module's translation-related signal and RNA surveillance, despite the absence of STRING or hu.MAP support.
- **Conclusion**: Established evidence supports EXOSC6 as an RNA-exosome component involved in RNA processing and degradation. Its participation in the prostate–stem_cells co-abundance program is plausible, but whether it is functionally coordinated with EIF6 or CCT8 in this module remains hypothetical.

#### EWSR1

- **Related proteins** (co-abundance neighbors): JPT2 (0.82), EIF6 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EWS RNA binding protein 1. This gene encodes a multifunctional protein that is involved in various cellular processes, including gene expression, cell signaling, and RNA processing and transport. The protein includes an N-terminal transcriptional activation domain and a C-terminal RNA-binding domain. Chromosomal translocations between this gene and various genes encoding transcription factors result in the production of chi…
- **Diseases (Open Targets)**: neurodegenerative disease (0.467); Ewing sarcoma (0.413); desmoplastic small round cell tumor (0.383); clear cell sarcoma (0.381); extraskeletal myxoid chondrosarcoma (0.380)
- **Europe PMC papers**: 6578
- **Why important**: EWSR1 connects JPT2 with EIF6 and has extensive literature. It is a multifunctional RNA-binding and gene-regulatory protein involved in transcriptional regulation, RNA processing, and RNA transport. Its disease associations include several fusion-driven or transcriptionally defined cancers, giving it particular biological relevance when interpreting a module that may reflect proliferative or progenitor-like cellular states.
- **Conclusion**: Established evidence supports EWSR1 as a multifunctional RNA-binding and transcriptional regulator with important cancer biology. The module does not establish that EWSR1 drives the observed co-abundance pattern or that a disease-associated fusion mechanism is involved.

#### CCT8

- **Related proteins** (co-abundance neighbors): EXOSC6 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 connects EXOSC6 with the module and is a subunit of the CCT chaperonin, which supports protein folding, protein stabilization, and assembly of newly synthesized proteins. It is detected in prostate and shows cell-type enhancement in oocytes, making it relevant both to proteostasis and to the possibility of shared reproductive-cell biology. Its literature base is substantial.
- **Conclusion**: Established evidence supports CCT8 as a protein-folding and chaperonin-associated factor. Its presence is consistent with a general proteostasis component in the module, but the connection to RNA surveillance and the reproductive-cell signal is an association-based hypothesis.

#### PSME3IP1

- **Related proteins** (co-abundance neighbors): EIF6 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome activator subunit 3 interacting protein 1. Involved in negative regulation of proteasomal protein catabolic process and negative regulation of protein binding activity. Located in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.074); osteoporosis (0.060); arthritic joint disease (0.026); placenta praevia (0.022); Alzheimer disease (0.011)
- **Europe PMC papers**: 18
- **Why important**: PSME3IP1 is directly connected to EIF6 and has annotations involving mRNA splicing, negative regulation of protein binding, and negative regulation of proteasomal protein catabolism. Its enhancement in early and late spermatids is distinctive within the module and may help explain why the shared signal appears in tissues or cell populations with reproductive or progenitor features, although its literature volume is limited.
- **Conclusion**: Established evidence supports PSME3IP1 as a nuclear regulator associated with splicing and proteasomal control, and HPA supports spermatid-associated expression. Its role as a contributor to the shared module or as a marker of cell composition is plausible but not resolved by the available network evidence.
