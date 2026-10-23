# Conserved co-abundance modules: autonomic_nervous_system and rectum

## Module 0

**Tissue pair**: autonomic_nervous_system and rectum  
**Genes (11)**: SH3BP1, MTHFD1L, CD2AP, CNOT1, CORO7, CTNND1, GAR1, EIF4E, RPP30, THOC2, TWF1

### Function

No GO or KEGG term passed global correction, and no STRING functional-enrichment term was reported; therefore the function should be inferred from the annotations and network rather than assigned from enrichment. The strongest biological theme is regulation of the actin cytoskeleton, cell adhesion, membrane trafficking, migration, and epithelial junction behavior, supported by CORO7, CTNND1, SH3BP1, TWF1, and CD2AP. A second theme involves constitutive RNA and protein-expression machinery, represented by CNOT1, THOC2, GAR1, RPP30, and EIF4E. The network is sparse and appears to contain a cytoskeletal or adhesion arm connected to an RNA-processing and translation arm, rather than a single well-established pathway. CORO7 and CTNND1 occupy comparatively central positions and may connect these functional aspects, but co-abundance does not establish physical interaction or causality.

**Cell composition.** This is not a plasma-protein or secreted-protein module: none of the genes is annotated as secreted, and all module proteins were detected in rectum tissue. Most genes have low tissue specificity and low immune-cell specificity, which is compatible with broadly expressed or housekeeping-like components, especially CNOT1, THOC2, GAR1, RPP30, and EIF4E. There is nevertheless cell-type structure in the HPA evidence. Microglia recur among enriched cell types, while SH3BP1 is tissue-enhanced in esophagus, MTHFD1L in blood vessel, and CORO7 in bone marrow. CD2AP has immune-cell enhancement in plasmacytoid dendritic cells, and CTNND1 has group enrichment across monocyte and myeloid dendritic-cell categories, but the overall module does not show a strong blood-cell signature. The shared signal may therefore reflect a mixture of ubiquitous intracellular programs and conserved epithelial, vascular, neural or glial, and possibly myeloid cell-state contributions rather than circulating plasma proteins.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only one high-confidence pair, GAR1 with RPP30. This is biologically coherent with RNA-processing machinery, but it explains only a small part of the module and does not support a densely connected physical-interaction complex. hu.MAP provides complementary evidence for SH3BP1 and CD2AP appearing together in complexes C1 and C2. In both cases they represent only a subset of the larger reported complexes, so the evidence supports participation in related cytoskeletal or membrane-associated assemblies rather than a module-specific complex. The absence of STRING partners for most genes and the absence of hu.MAP assignments for most genes indicate that the co-abundance relationships are not simply a direct protein-interaction network. They may instead reflect coordinated expression across cell states, shared regulation, or indirect coupling between cytoskeletal, adhesion, and RNA-management programs.

**STRING interactions (score >= 0.7)**: 1 of 55 gene pairs: GAR1–RPP30 (0.79)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06016.1 (SH3BP1, CD2AP; 2/9); huMAP3_12900.1 (SH3BP1, CD2AP; 2/50)

### Novelty

The conserved co-abundance pattern may be a potentially new cross-tissue observation, but the available evidence does not establish it as a new biological pathway or complex. Its novelty is limited by the sparse physical-interaction support, the presence of broadly expressed housekeeping-like genes, and the lack of globally significant GO or KEGG enrichment. The known GAR1-RPP30 relationship and the hu.MAP associations involving SH3BP1 and CD2AP show that parts of the module are already biologically recognized. Conversely, the particular combination and cross-tissue co-abundance structure is not explained by those resources. Thus the defensible claim is a possibly novel conserved expression module or cell-state signature, requiring replication in independent data and testing against cell-composition and technical-confounding models. Absence from STRING or hu.MAP alone is not evidence of novelty.

**Hypothesis.** Hypothesis: the module reflects a conserved state in which actin remodeling, epithelial or membrane-junction dynamics, intracellular trafficking, and cell motility are coordinated with RNA processing and translation capacity. In this model, CORO7, CTNND1, SH3BP1, TWF1, and CD2AP represent the structural and trafficking arm, while CNOT1, THOC2, GAR1, RPP30, and EIF4E represent RNA handling and translational support. The shared signal between autonomic nervous system and rectum could arise from related epithelial, vascular, glial or neuronal, and myeloid cell states, or from a common demand for remodeling and biosynthetic adaptation. This is a mechanistic hypothesis, not a demonstrated causal pathway; it should be tested by cell-resolved expression, perturbation of cytoskeletal or RNA-processing components, and direct measurement of junctional trafficking and protein-synthesis phenotypes.

### Important genes

#### CORO7

- **Related proteins** (co-abundance neighbors): RPP30 (0.88), SH3BP1 (0.85), CNOT1 (0.84), CTNND1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coronin 7. This gene encodes a member of the coronin protein family. However, unlike other coronin proteins, it is not an actin-binding protein but rather functions as an F-actin regulator directing anterograde Golgi to endosome transport. The encoded protein has two tandem WD-40 domain repeats and localizes to the trans-Golgi network. The protein undergoes K33-linked polyubiquitination via an E3 ligase comp…
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); hypertensive disorder (0.294); mathematical ability (0.238); type 2 diabetes mellitus (0.217); pericarditis (0.178)
- **Europe PMC papers**: 218
- **Why important**: CORO7 has the strongest network centrality in the module and connects RPP30, SH3BP1, CNOT1, and CTNND1, making it a candidate bridge between the cytoskeletal and RNA-associated portions. Its established annotation supports Golgi-to-endosome transport, actin organization, cell migration, and maintenance of Golgi morphology. HPA places it in a bone-marrow-enhanced tissue category and in several neural or glial cell categories, while its literature and disease-association record is substantial.
- **Conclusion**: Established: CORO7 regulates actin-associated intracellular transport and is centrally positioned in this co-abundance graph. Hypothesis: it may coordinate trafficking and cytoskeletal remodeling across the two tissues. The module does not demonstrate that CORO7 drives the shared signal.

#### CTNND1

- **Related proteins** (co-abundance neighbors): TWF1 (0.87), CORO7 (0.81), EIF4E (0.80), CD2AP (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin delta 1. This gene encodes a member of the Armadillo protein family, which function in adhesion between cells and signal transduction. Multiple translation initiation codons and alternative splicing result in many different isoforms being translated. Not all of the full-length natures of the described transcript variants have been determined. Read-through transcription also exists between this gene and the…
- **Diseases (Open Targets)**: blepharocheilodontic syndrome (0.724); listeriosis (0.526); cleft lip (0.510); hereditary disease (0.415); exudative vitreoretinopathy (0.376)
- **Europe PMC papers**: 3021
- **Why important**: CTNND1 is among the most connected genes and links TWF1, CORO7, EIF4E, and CD2AP. Its established functions in cadherin-mediated cell-cell adhesion, cell migration, signal transduction, and protein stabilization provide a strong interpretation for the membrane and junctional aspect of the module. It is detected in rectum, has plasma-membrane localization, shows several epithelial and microglial cell-type associations, and has the largest disease and literature footprint among the adhesion-related candidates.
- **Conclusion**: Established: CTNND1 is a cell-adhesion and signaling scaffold compatible with the module's cytoskeletal structure. Hypothesis: it may be a key organizer of the conserved tissue interface or remodeling state. The co-abundance result alone cannot distinguish epithelial junction biology from contributions by myeloid or other cell types.

#### CD2AP

- **Related proteins** (co-abundance neighbors): TWF1 (0.82), CTNND1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_06016.1, huMAP3_12900.1
- **Function (MyGene.info)**: CD2 associated protein. This gene encodes a scaffolding molecule that regulates the actin cytoskeleton. The protein directly interacts with filamentous actin and a variety of cell membrane proteins through multiple actin binding sites, SH3 domains, and a proline-rich region containing binding sites for SH3 domains. The cytoplasmic protein localizes to membrane ruffles, lipid rafts, and the leading edges of cells. It is i…
- **Diseases (Open Targets)**: familial idiopathic steroid-resistant nephrotic syndrome (0.701); focal segmental glomerulosclerosis (0.585); Alzheimer disease (0.493); dementia (0.395); Abnormality of the skeletal system (0.314)
- **Europe PMC papers**: 3461
- **Why important**: CD2AP links TWF1 and CTNND1 and is the most directly supported module member in hu.MAP, where it occurs with SH3BP1 in complexes C1 and C2. Its established functions include actin-cytoskeleton regulation, membrane trafficking, cell migration, secretion, and synapse organization. Its plasma-membrane localization, enterocyte and plasmacytoid-dendritic-cell associations, and strong disease and literature record make it informative for both epithelial and immune interpretations.
- **Conclusion**: Established: CD2AP is a membrane-associated actin scaffold and has independent complex-level support with SH3BP1. Hypothesis: CD2AP may connect junctional remodeling with cell-type-specific trafficking in the shared module. The data do not establish whether its signal is epithelial, immune, neuronal, or a mixture.

#### CNOT1

- **Related proteins** (co-abundance neighbors): GAR1 (0.85), THOC2 (0.84), CORO7 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CCR4-NOT transcription complex subunit 1. Enables armadillo repeat domain binding activity; molecular adaptor activity; and nuclear receptor binding activity. Contributes to poly(A)-specific ribonuclease activity. Involved in several processes, including negative regulation of signal transduction; positive regulation of cytoplasmic mRNA processing body assembly; and regulation of gene expression. Located in P-body and cytosol. Part of CCR…
- **Diseases (Open Targets)**: holoprosencephaly 12 with or without pancreatic agenesis (0.749); Vissers-Bodmer syndrome (0.697); hereditary disease (0.515); complex neurodevelopmental disorder (0.474); neurodegenerative disease (0.471)
- **Europe PMC papers**: 1262
- **Why important**: CNOT1 connects GAR1, THOC2, and CORO7 and is the central representative of the RNA-regulatory arm. It is an adaptor and core component of the CCR4-NOT complex, with established roles in mRNA deadenylation, gene-expression regulation, cytoplasmic RNA processing bodies, and translational control. Its broad tissue and cell-type profile supports a general intracellular program rather than a secreted or tissue-restricted signal, and its disease and literature record is substantial.
- **Conclusion**: Established: CNOT1 is a core post-transcriptional gene-regulation factor and is structurally positioned between RNA-associated genes and CORO7. Hypothesis: coordinated CNOT1 abundance may indicate altered mRNA turnover or translational state accompanying cytoskeletal remodeling. The module does not prove that CCR4-NOT activity is altered.

#### GAR1

- **Related proteins** (co-abundance neighbors): THOC2 (0.89), CNOT1 (0.85); STRING partners: RPP30 (0.79)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GAR1 ribonucleoprotein. This gene is a member of the H/ACA snoRNPs (small nucleolar ribonucleoproteins) gene family. snoRNPs are involved in various aspects of rRNA processing and modification and have been classified into two families: C/D and H/ACA. The H/ACA snoRNPs also include the DKC1, NOLA2 and NOLA3 proteins. These four H/ACA snoRNP proteins localize to the dense fibrillar components of nucleoli and to coiled (Ca…
- **Diseases (Open Targets)**: neurodegenerative disease (0.400); prostate carcinoma (0.198); Thrombocytopenia (0.048); familial primary hypomagnesemia with normocalciuria and normocalcemia (0.041); renal hypomagnesemia 2 (0.041)
- **Europe PMC papers**: 1232
- **Why important**: GAR1 links THOC2 and CNOT1 and forms the module's only high-confidence STRING pair with RPP30. Its established role in H or ACA snoRNP biology, ribosome biogenesis, rRNA pseudouridylation, and telomerase-related maintenance gives the RNA-processing arm a specific molecular anchor. It is broadly expressed, nucleolar, and supported by a substantial literature and disease-association record.
- **Conclusion**: Established: GAR1 participates in nucleolar RNA modification and processing, and its relationship with RPP30 is independently supported by STRING. Hypothesis: the GAR1-RPP30 signal may reflect coordinated ribosome or RNA-processing demand within the conserved cell state. This pair does not demonstrate that the entire module is a ribosome-biogenesis complex.

## Module 1

**Tissue pair**: autonomic_nervous_system and rectum  
**Genes (7)**: ABCF1, EXOC7, FLII, NAA25, PAPSS1, SKIC3, MIA3

### Function

No GO or KEGG term passed global correction, so the module does not support a formally established pathway assignment from enrichment. Its genes nevertheless converge on several compatible cellular themes: MIA3 and EXOC7 support vesicle trafficking, cargo handling, exocytosis and secretion; FLII supports actin remodeling and contractile cytoskeletal organization; PAPSS1 supports sulfate-donor production; ABCF1 supports translation and inflammatory-response related processes; SKIC3 supports RNA surveillance and ribosome rescue; and NAA25 supports N-terminal protein acetylation and cytoskeleton organization. The co-abundance structure therefore suggests a broad intracellular homeostasis program involving trafficking, cytoskeletal organization, protein or RNA handling and metabolic modification, rather than a specific established pathway. These interpretations are gene-based and supplementary because no GO or KEGG term achieved global significance.

**Cell composition.** The module is not composed of plasma or secreted proteins: the secretome annotation is absent for every member. Most genes have low tissue specificity, and all members are detected by immunohistochemistry in rectum, which is consistent with broadly present cellular proteins rather than a tissue-exclusive secretory signature. Several genes have cell-type-enhanced annotations, but the enriched cell types are heterogeneous and do not define one coherent lineage. Most genes have low immune-cell specificity; PAPSS1 is the exception, with group enrichment in basophils and eosinophils. Thus, a blood-cell explanation is not strongly supported, although cell-type composition or shared broadly expressed cellular programs could contribute to the conserved signal. Protein evidence for autonomic nervous system could not be assessed because the corresponding HPA tissue match was unavailable.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was observed among the module members, and no STRING functional-enrichment result was reported. No hu.MAP complex contained multiple module members. The co-abundance edges are therefore not corroborated by the supplied physical-interaction or complex resources. This suggests that the module may reflect coordinated expression or protein abundance across different cellular processes rather than a single known multiprotein complex. The strongest network position belongs to MIA3, which connects the trafficking-related and other branches, while FLII links MIA3 with EXOC7 and PAPSS1 links MIA3 with ABCF1.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared co-abundance pattern may be a new observation because the module has a specific tissue-pair context and is not represented as a known high-confidence STRING interaction set or hu.MAP complex. However, absence from those resources does not establish biological novelty: these databases primarily document physical interactions and curated complexes, whereas co-abundance can arise from coordinated regulation, cell composition, shared organelle activity or technical effects. The lack of globally significant GO or KEGG enrichment also prevents claiming discovery of a new pathway. The defensible conclusion is that the tissue-shared co-abundance relationship is potentially novel, while its molecular mechanism remains unvalidated.

**Hypothesis.** Hypothesis: the conserved module reflects coordinated abundance of a broadly expressed intracellular maintenance program in rectum and autonomic nervous system samples. MIA3-mediated cargo handling and endoplasmic-reticulum export could be coupled to EXOC7-dependent post-Golgi delivery and FLII-dependent actin remodeling, while PAPSS1 supplies sulfate donor for sulfotransferase reactions and ABCF1, SKIC3 and NAA25 support translation, RNA quality control and protein maturation. This could produce correlated abundance without requiring direct physical interaction among the proteins. The hypothesis predicts that the module should track vesicle-trafficking, cytoskeletal or epithelial secretory states across samples, but the supplied evidence does not establish causality or cell-type origin.

### Important genes

#### MIA3

- **Related proteins** (co-abundance neighbors): FLII (0.88), SKIC3 (0.85), NAA25 (0.83), PAPSS1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MIA SH3 domain ER export factor 3. Enables cargo receptor activity. Involved in several processes, including COPII-coated vesicle cargo loading; cell migration involved in sprouting angiogenesis; and regulation of leukocyte migration. Located in endoplasmic reticulum exit site and endoplasmic reticulum membrane. Is integral component of membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: coronary artery disorder (0.503); myocardial infarction (0.481); odontochondrodysplasia 2 with hearing loss and diabetes (0.471); coronary atherosclerosis (0.464); angina pectoris (0.439)
- **Europe PMC papers**: 604
- **Why important**: MIA3 is the central network connector and has the strongest weighted network position in the module. Its cargo-receptor activity, COPII-coated vesicle loading, endoplasmic-reticulum to Golgi transport, exocytosis and protein-secretion annotations provide the clearest functional anchor for the module. It also has substantial literature support and disease associations involving coronary disorders, myocardial infarction and a syndromic developmental condition.
- **Conclusion**: Established evidence supports MIA3 as a vesicle-trafficking and cargo-handling protein and as the network's principal connector. It is plausible, but unproven, that MIA3 coordinates the other module branches; the co-abundance data do not demonstrate direct molecular regulation.

#### FLII

- **Related proteins** (co-abundance neighbors): MIA3 (0.88), EXOC7 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Centriolar satellite, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FLII actin remodeling protein. This gene encodes a protein with a gelsolin-like actin binding domain and an N-terminal leucine-rich repeat-protein protein interaction domain. The protein is similar to a Drosophila protein involved in early embryogenesis and the structural organization of indirect flight muscle. The gene is located within the Smith-Magenis syndrome region on chromosome 17. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: cardiomyopathy, dilated, 2j (0.616); Abnormality of the skeletal system (0.397); dilated cardiomyopathy (0.313); neurodegenerative disease (0.287); Marfan syndrome (0.118)
- **Europe PMC papers**: 1832
- **Why important**: FLII is the only tissue-enhanced gene in the module, with skeletal-muscle enrichment, and it bridges MIA3 to EXOC7. Its actin-binding, actin-severing, barbed-end capping, myofibril and sarcomere annotations connect vesicle delivery with cytoskeletal organization. It has the largest literature volume among the module genes and disease associations involving dilated cardiomyopathy and skeletal abnormalities.
- **Conclusion**: Established evidence supports FLII as an actin-remodeling protein with roles in contractile and cytoskeletal organization. A role in coupling trafficking to cytoskeletal positioning is a reasonable hypothesis, but the module does not establish that mechanism in either tissue.

#### EXOC7

- **Related proteins** (co-abundance neighbors): FLII (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exocyst complex component 7. The protein encoded by this gene is a component of the exocyst complex. The exocyst complex plays a critical role in vesicular trafficking and the secretory pathway by targeting post-Golgi vesicles to the plasma membrane. The encoded protein is required for assembly of the exocyst complex and docking of the complex to the plasma membrane. The encoded protein may also play a role in pre-mRNA splici…
- **Diseases (Open Targets)**: neurodevelopmental disorder with seizures and brain atrophy (0.678); neurodegenerative disease (0.526); hereditary disease (0.415); microcephaly (0.261); Brain atrophy (0.255)
- **Europe PMC papers**: 420
- **Why important**: EXOC7 is a component of the exocyst, a complex that targets post-Golgi vesicles to the plasma membrane, and it is connected to FLII in the module. Its annotations include exocytosis, membrane fission and protein localization to the ciliary membrane. Its disease associations include neurodevelopmental and neurodegenerative conditions, making it relevant to the autonomic nervous system context.
- **Conclusion**: Established evidence supports EXOC7 as a vesicle-docking and secretory-pathway component. Its co-abundance with FLII and MIA3 is consistent with coordinated trafficking and cytoskeletal organization, but no direct interaction among these module members is supported by the supplied STRING or hu.MAP results.

#### PAPSS1

- **Related proteins** (co-abundance neighbors): ABCF1 (0.88), MIA3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Nucleoli rim, Mitotic chromosome; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3'-phosphoadenosine 5'-phosphosulfate synthase 1. Three-prime-phosphoadenosine 5-prime-phosphosulfate (PAPS) is the sulfate donor cosubstrate for all sulfotransferase (SULT) enzymes (Xu et al., 2000 [PubMed 10679223]). SULTs catalyze the sulfate conjugation of many endogenous and exogenous compounds, including drugs and other xenobiotics. In humans, PAPS is synthesized from adenosine 5-prime triphosphate (ATP) and inorganic sulfate by 2 isoforms,…
- **Diseases (Open Targets)**: cancer (0.545); Alzheimer disease (0.335); Parkinson disease (0.334); lysosomal storage disease (0.334); neurodegenerative disease (0.334)
- **Europe PMC papers**: 434
- **Why important**: PAPSS1 is connected to the central MIA3 branch and to ABCF1. It produces the sulfate donor used by sulfotransferases, linking the module to biochemical modification of endogenous and exogenous compounds. It also has cell-type-enhanced annotations in endometrial cells and group-enriched blood annotations in basophils and eosinophils, so it may contribute either metabolic context or cell-composition sensitivity.
- **Conclusion**: Established evidence supports PAPSS1 as a sulfate-donor biosynthetic enzyme. Its presence does not establish a shared sulfation pathway for the whole module; coordinated abundance with trafficking and translation genes is currently a hypothesis.

#### ABCF1

- **Related proteins** (co-abundance neighbors): PAPSS1 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP binding cassette subfamily F member 1. The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the GCN20 subfamily. Unlike other members of the superfamily, this protein lac…
- **Diseases (Open Targets)**: urinary bladder cancer (0.074); urinary bladder carcinoma (0.074); lung adenocarcinoma (0.048); hepatocellular carcinoma (0.036); glioblastoma (0.033)
- **Europe PMC papers**: 964
- **Why important**: ABCF1 is a translation-related ABC-family protein lacking the transmembrane domains typical of many ABC transporters. It is the terminal partner of PAPSS1 in the module and has annotations involving translation, translational initiation, ribosome biogenesis and inflammatory response. Its literature volume and disease associations provide additional biological context.
- **Conclusion**: Established evidence supports ABCF1 in translation-associated and ribosome-related processes. Its link with PAPSS1 may reflect shared cellular state or regulation rather than a known complex, and its proposed contribution to the module's maintenance program remains untested.

## Module 2

**Tissue pair**: autonomic_nervous_system and rectum  
**Genes (27)**: ACLY, ALDH2, CUX1, DRG2, EIF3F, FASN, GARS1, COLGALT1, GMPS, HSD17B10, HSPBP1, KPNA2, ORC3, JUP, PTBP1, GART, RAB8A, RSL1D1, MRPS35, SNRPA1, IARS1, TEX10, MPST, TIGAR, TRAP1, XPO5, ZNF326

### Function

No GO or KEGG term passed global correction, so the module should not be assigned a single statistically established pathway. Its structure instead suggests a mixed intracellular cellular-state module. The co-abundance network connects RNA processing and translation-related genes, mitochondrial proteins, purine biosynthesis, lipid metabolism, nuclear transport, stress regulation, and epithelial junction biology. The strongest network position is occupied by RSL1D1, which links several of these components, while smaller subnetworks connect GART with GMPS, ACLY with FASN, GARS1 with IARS1, and KPNA2 with XPO5. These observations support coordinated variation in biosynthetic capacity, RNA and protein handling, mitochondrial stress response, and epithelial-cell state, but the absence of a globally significant GO or KEGG term argues against treating this as a coherent canonical pathway.

**Cell composition.** The HPA profile is predominantly broadly expressed rather than tissue restricted: most genes have low tissue specificity and most have low immune-cell specificity. Only a small minority are secreted, and the module is not predominantly composed of plasma or extracellular proteins. Several genes show cell-type-enhanced patterns across diverse populations, including epithelial, hepatic, reproductive, cardiac, neuronal, and myeloid-associated cells, indicating cellular heterogeneity rather than a clean autonomic-nervous-system or rectal lineage signature. The repeated rectal protein detection is compatible with expression in rectal tissue, but the absence of a matching autonomic-nervous-system HPA tissue dataset limits direct comparison. Overall, the module does not strongly indicate blood contamination or a plasma-protein module; it more plausibly reflects broadly expressed housekeeping and biosynthetic programs, potentially modulated by shared cell composition.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING evidence is sparse but biologically interpretable. ACLY is linked to FASN and GART, GART is linked to GMPS, GARS1 is linked to IARS1, and KPNA2 is linked to XPO5. These relationships support known connections among fatty-acid and acetyl-CoA metabolism, purine synthesis, aminoacyl-tRNA charging, and nuclear RNA transport, but they do not establish one unified physical complex for the whole module. hu.MAP provides additional support for partial complex membership. (hu.MAP huMAP3_14442.1) contains GARS1, GMPS, and TRAP1 among a much larger complex; (hu.MAP huMAP3_01662.1), (hu.MAP huMAP3_03291.1), and (hu.MAP huMAP3_00676.1) each contain GART and FASN with additional complex members outside the module. Thus, the module contains embedded known molecular relationships, while much of its co-abundance structure is not explained by currently catalogued physical complexes.

**STRING interactions (score >= 0.7)**: 5 of 351 gene pairs: ACLY–FASN (0.994); ACLY–GART (0.711); GARS1–IARS1 (0.97); GART–GMPS (0.937); KPNA2–XPO5 (0.708)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (GARS1, GMPS, TRAP1; 3/57); huMAP3_01662.1 (GART, FASN; 2/3); huMAP3_03291.1 (GART, FASN; 2/3); huMAP3_00676.1 (GART, FASN; 2/4)

### Novelty

This module should not be called a newly discovered molecular pathway. The presence of established STRING relationships and partial hu.MAP complexes shows that several constituent associations are already known. Conversely, the absence of a globally significant GO or KEGG term, the sparse STRING connectivity, and the lack of a single coherent annotated complex mean that the particular cross-tissue co-abundance pattern may be a new systems-level observation. However, co-abundance in two tissues alone does not demonstrate mechanistic novelty. The most defensible conclusion is that the module may represent a novel combination or expression-level coordination of known cellular programs, but its biological novelty requires independent replication and testing against existing tissue, cell-composition, and disease datasets.

**Hypothesis.** Hypothesis: the shared module reflects a broadly expressed epithelial or parenchymal cellular-state program that coordinates biosynthetic demand with RNA handling, mitochondrial quality control, and stress adaptation. In this model, purine and lipid synthesis support proliferation or repair, aminoacyl-tRNA and RNA-processing proteins support increased gene-expression capacity, TRAP1 and related mitochondrial factors buffer metabolic and oxidative stress, and JUP or COLGALT1-linked biology connects the intracellular state to epithelial adhesion or extracellular-matrix maintenance. This is a hypothesis rather than an established pathway assignment. It predicts that module abundance will track cellular metabolic activity, epithelial integrity, proliferative or regenerative state, and mitochondrial stress more closely than a specific autonomic or rectal function.

### Important genes

#### RSL1D1

- **Related proteins** (co-abundance neighbors): SNRPA1 (0.91), JUP (0.88), TRAP1 (0.85), TEX10 (0.83), ALDH2 (0.81), MRPS35 (0.81), GMPS (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal L1 domain containing 1. Enables mRNA 3'-UTR binding activity and mRNA 5'-UTR binding activity. Involved in regulation of apoptotic process and regulation of cellular senescence. Acts upstream of or within regulation of protein localization. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: adolescent idiopathic scoliosis (0.219); hepatocellular carcinoma (0.099); neoplasm (0.099); colorectal carcinoma (0.096); insomnia (0.078)
- **Europe PMC papers**: 381
- **Why important**: RSL1D1 has the strongest network position and connects SNRPA1, JUP, TRAP1, TEX10, ALDH2, MRPS35, and GMPS, making it the principal bridge between RNA-related, epithelial, mitochondrial, and purine-associated parts of the module. Its nucleolar and chromosome-associated localization and reported roles in protein localization, apoptosis, and cellular senescence fit a broad cellular-state interpretation. It has substantial literature and disease associations including colorectal carcinoma and hepatocellular carcinoma.
- **Conclusion**: Established evidence supports RSL1D1 as a highly connected nucleolar and chromosome-associated regulator associated with RNA-related and cellular-stress biology. Its centrality makes it an important marker of the module, but the data do not establish that RSL1D1 drives the co-abundance pattern. A plausible hypothesis is that it coordinates the biosynthetic and stress-related state represented by the module.

#### GART

- **Related proteins** (co-abundance neighbors): TIGAR (0.88), KPNA2 (0.84); STRING partners: ACLY (0.711), GMPS (0.937)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_01662.1, huMAP3_03291.1, huMAP3_00676.1
- **Function (MyGene.info)**: phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase. The protein encoded by this gene is a trifunctional polypeptide. It has phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase activity which is required for de novo purine biosynthesis. This enzyme is highly conserved in vertebrates. Alternative splicing of this gene results in two transcript variants encoding different isoforms.…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.606); mesothelioma (0.584); malignant pleural mesothelioma (0.557); adenocarcinoma (0.486); anaplastic lung carcinoma (0.462)
- **Europe PMC papers**: 1890
- **Why important**: GART is a trifunctional enzyme in de novo purine biosynthesis and connects the module to GMPS through STRING as well as to ACLY and FASN through the broader interaction and complex evidence. It is also a member of several hu.MAP complexes with FASN, including (hu.MAP huMAP3_01662.1), (hu.MAP huMAP3_03291.1), and (hu.MAP huMAP3_00676.1). Its network position links metabolic genes with TIGAR and KPNA2, while its disease literature includes multiple cancer associations.
- **Conclusion**: Established evidence supports GART as a purine-biosynthetic enzyme embedded in known metabolic and complex relationships. Its inclusion is consistent with biosynthetic demand, but no globally significant enrichment demonstrates that purine metabolism defines the entire module. The hypothesis that GART marks increased nucleotide demand in shared tissue-cell states remains testable rather than proven.

#### FASN

- **Related proteins** (co-abundance neighbors): IARS1 (0.88); STRING partners: ACLY (0.994)
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_01662.1, huMAP3_03291.1, huMAP3_00676.1
- **Function (MyGene.info)**: fatty acid synthase. The enzyme encoded by this gene is a multifunctional protein. Its main function is to catalyze the synthesis of palmitate from acetyl-CoA and malonyl-CoA, in the presence of NADPH, into long-chain saturated fatty acids. In some cancer cell lines, this protein has been found to be fused with estrogen receptor-alpha (ER-alpha), in which the N-terminus of FAS is fused in-frame with the C-terminus of …
- **Diseases (Open Targets)**: dengue disease (0.469); autism spectrum disorder (0.333); Parkinson disease (0.295); Epileptic encephalopathy (0.211); neurodegenerative disease (0.205)
- **Europe PMC papers**: 21528
- **Why important**: FASN is a major fatty-acid synthesis enzyme and has one of the strongest known STRING relationships in the module through ACLY. It also appears with GART in several hu.MAP complexes, providing convergent support for a metabolic submodule. HPA shows tissue enhancement in adipose tissue, breast, and liver and cell-type enrichment in breast lactating cells, while its extensive literature and cancer associations make it a biologically prominent metabolic marker.
- **Conclusion**: Established evidence supports FASN as a central lipogenic enzyme with known ACLY and complex relationships. Its presence suggests that lipid biosynthetic state may contribute to the shared co-abundance signal, but the module does not establish activation of lipogenesis in either tissue. The hypothesis that FASN couples nutrient or membrane-building demand to the wider module should be tested with lipid-metabolism measurements.

#### TRAP1

- **Related proteins** (co-abundance neighbors): COLGALT1 (0.87), RSL1D1 (0.85), JUP (0.82), HSD17B10 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: TNF receptor associated protein 1. This gene encodes a mitochondrial chaperone protein that is member of the heat shock protein 90 (HSP90) family. The encoded protein has ATPase activity and interacts with tumor necrosis factor type I. This protein may function in regulating cellular stress responses. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jan 2013].
- **Diseases (Open Targets)**: congenital anomaly of kidney and urinary tract (0.643); VACTERL/vater association (0.492); atrial fibrillation (0.467); neurodegenerative disease (0.372); Blindness (0.338)
- **Europe PMC papers**: 2586
- **Why important**: TRAP1 is a mitochondrial HSP90-family chaperone with roles in protein folding, cellular stress responses, respiration, reactive oxygen species regulation, and intrinsic apoptosis. It connects RSL1D1, JUP, COLGALT1, and HSD17B10 in the network and is represented in the larger hu.MAP complex (hu.MAP huMAP3_14442.1). Its high literature volume and disease associations involving mitochondrial, cardiac, renal, and neurodegenerative conditions add biological importance.
- **Conclusion**: Established evidence supports TRAP1 as a mitochondrial stress and proteostasis regulator that links metabolic and epithelial-associated components of the module. The network is compatible with a mitochondrial adaptation program, but it does not prove that oxidative stress is the cause of co-abundance. A reasonable hypothesis is that TRAP1 buffers the energetic and proteotoxic consequences of the biosynthetic state.

#### SNRPA1

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.91), TEX10 (0.87), PTBP1 (0.85), MRPS35 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: small nuclear ribonucleoprotein polypeptide A'. Enables RNA binding activity. Involved in mRNA splicing, via spliceosome and spermatogenesis. Located in nuclear speck. Part of U2-type catalytic step 2 spliceosome and U2-type precatalytic spliceosome. Implicated in connective tissue disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.538); dengue disease (0.370); phosphorus metabolism disease (0.196); hypotensive disorder (0.196); cancer (0.087)
- **Europe PMC papers**: 520
- **Why important**: SNRPA1 is a spliceosomal RNA-binding protein and a network connector between RSL1D1, TEX10, PTBP1, and MRPS35. Its annotations support mRNA splicing and spliceosome assembly, and its cell-type-enhanced patterns across reproductive and trophoblast populations illustrate the broad cellular context of the module. Its disease and literature associations provide more support than would be expected for an incidental low-connectivity transcript.
- **Conclusion**: Established evidence supports SNRPA1 as a component of spliceosomal RNA processing, and its network position supports an RNA-handling arm of the module. It does not establish tissue-specific autonomic or rectal function. The hypothesis that coordinated RNA processing helps accommodate the module's metabolic and stress state is plausible but requires transcript-isoform or splicing data.

#### ALDH2

- **Related proteins** (co-abundance neighbors): HSD17B10 (0.82), RSL1D1 (0.81), MPST (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 2 family member. This protein belongs to the aldehyde dehydrogenase family of proteins. Aldehyde dehydrogenase is the second enzyme of the major oxidative pathway of alcohol metabolism. Two major liver isoforms of aldehyde dehydrogenase, cytosolic and mitochondrial, can be distinguished by their electrophoretic mobilities, kinetic properties, and subcellular localizations. Most Caucasians have two major isozymes, …
- **Diseases (Open Targets)**: alcohol dependence (0.654); alcohol drinking (0.549); AMED syndrome, digenic (0.503); gout (0.501); atrial fibrillation (0.469)
- **Europe PMC papers**: 7978
- **Why important**: ALDH2 is a well-characterized aldehyde-detoxifying enzyme with a strong literature base and links to HSD17B10, RSL1D1, and MPST. Its HPA profile is liver-enhanced and hepatocyte-associated, while its functions include aldehyde catabolism and cellular detoxification. The network therefore connects mitochondrial or metabolic redox handling with the module's nucleolar and stress-related components.
- **Conclusion**: Established evidence supports ALDH2 as an aldehyde-detoxification enzyme and a marker of oxidative or metabolic handling. Its presence is consistent with stress adaptation, but the module does not demonstrate aldehyde accumulation or altered ALDH2 activity. The hypothesis that ALDH2 helps protect cells during the proposed biosynthetic and mitochondrial state should be evaluated experimentally.

## Module 3

**Tissue pair**: autonomic_nervous_system and rectum  
**Genes (14)**: AHNAK, AKAP12, CALD1, CBR1, CFL2, CZIB, EHD1, FERMT2, FLNA, LTA4H, PARVA, PGM2, SYNM, TPM1

### Function

The module is most strongly associated with a contractile actin-cytoskeletal apparatus. The primary evidence is the convergence of (GO:CC myofibril; q_global = 1.07e-05) and (GO:CC contractile muscle fiber; q_global = 1.07e-05) on the myofibril and contractile muscle fiber, with further support from (GO:CC sarcomere; q_global = 0.02) for sarcomere, (GO:CC supramolecular polymer; q_global = 0.0204) and (GO:CC supramolecular fiber; q_global = 0.0204) for supramolecular contractile fibers, and (GO:CC actin cytoskeleton; q_global = 0.0432) for the actin cytoskeleton. The shared biology is therefore likely structural and mechanical: organization of actin-associated fibers, focal adhesions, cell junctions, and contractile machinery. The module does not establish a neural-specific function merely because one tissue is autonomic nervous system; the evidence instead points toward smooth-muscle, vascular, stromal, or other contractile cells present in both tissue groups.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not predominantly an immune or blood-cell module, because most genes have low immune-cell specificity, although individual genes show immune-cell enrichment or enhancement. HPA evidence instead points strongly toward smooth muscle and vascular smooth muscle cells, with additional signals from stromal, myoepithelial, muscle, intestinal, and vascular cell types. Several genes have low tissue specificity, so the shared signal may reflect broadly distributed structural machinery as well as shared contractile or stromal cell populations. Rectal protein detection supports the presence of much of the module in rectum, whereas matching autonomic-nervous-system protein evidence was unavailable.

**GO/KEGG enrichment**: 6 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC myofibril | 1.07e-05 | AHNAK, CALD1, CFL2, FERMT2, FLNA, PARVA, SYNM, TPM1 |
| GO:CC contractile muscle fiber | 1.07e-05 | AHNAK, CALD1, CFL2, FERMT2, FLNA, PARVA, SYNM, TPM1 |
| GO:CC sarcomere | 0.02 | CFL2, FERMT2, FLNA, PARVA, TPM1 |
| GO:CC supramolecular polymer | 0.0204 | AHNAK, CALD1, CFL2, FERMT2, FLNA, PARVA, SYNM, TPM1 |
| GO:CC supramolecular fiber | 0.0204 | AHNAK, CALD1, CFL2, FERMT2, FLNA, PARVA, SYNM, TPM1 |
| GO:CC actin cytoskeleton | 0.0432 | AHNAK, CALD1, CFL2, FERMT2, FLNA, PARVA, TPM1 |

### STRING and hu.MAP

STRING supports a compact set of already known relationships rather than a fully connected interaction system. The strongest directly represented relationships are CALD1 with TPM1, CFL2 with FLNA, FERMT2 with FLNA, and FERMT2 with PARVA. STRING functional annotations independently recover myofibril, actin cytoskeleton, sarcomere, I-band, actin-binding, cell-cell junction, anchoring junction, and supramolecular-fiber themes in (STRING Component Myofibril; within-query FDR = 3.14e-06) through (STRING COMPARTMENTS Sarcomere; within-query FDR = 0.0499). These known links support the biological coherence of the contractile and adhesion interpretation, while the remaining co-abundance edges should not automatically be treated as physical protein interactions. No hu.MAP complex contains multiple module members, so the data do not support assignment to a single established multiprotein complex.

**STRING interactions (score >= 0.7)**: 4 of 91 gene pairs: CALD1–TPM1 (0.869); CFL2–FLNA (0.888); FERMT2–FLNA (0.852); FERMT2–PARVA (0.893)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Myofibril (FDR = 3.14e-06, 8 genes); COMPARTMENTS Myofibril (FDR = 0.0016, 5 genes); Component Actin cytoskeleton (FDR = 0.0035, 7 genes); Component Sarcomere (FDR = 0.0035, 5 genes); Component I band (FDR = 0.0174, 4 genes); Keyword Cytoskeleton (FDR = 0.0178, 8 genes); Component Cytoskeleton (FDR = 0.021, 9 genes); PMID (2023) Integrated bioinformatics and wet-lab analysis revealed cell adhesion prominent genes CDC42, TAGLN and GSN as prognostic biomarkers in colonic-polyp lesions. (FDR = 0.0296, 6 genes); Keyword Actin-binding (FDR = 0.0435, 5 genes); Keyword Cilium biogenesis/degradation (FDR = 0.0435, 3 genes); COMPARTMENTS Cell-cell junction (FDR = 0.0456, 4 genes); COMPARTMENTS Actin cytoskeleton (FDR = 0.0456, 6 genes); COMPARTMENTS Anchoring junction (FDR = 0.0456, 6 genes); COMPARTMENTS Supramolecular fiber (FDR = 0.0456, 6 genes); COMPARTMENTS Sarcomere (FDR = 0.0499, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is best described as a potentially informative tissue-shared co-abundance module, not as a proven new molecular complex or a definitively novel pathway. The finding has convergent enrichment, coherent network organization, and cell-type support, but many component functions and some pairwise relationships are already represented in STRING and the literature. The absence of a hu.MAP complex and the absence of STRING support for some edges may indicate a new co-abundance context, tissue composition effect, or undercharacterized association, but database absence alone cannot prove novelty. A claim of novelty would require independent replication, tissue- and cell-composition controls, and comparison with previously reported co-expression modules.

**Hypothesis.** Hypothesis: the shared module reflects coordinated abundance of a smooth-muscle or contractile stromal cell program in autonomic nervous system and rectum samples. In this model, CALD1 and TPM1 help regulate actin-tropomyosin contractility; CFL2 controls actin filament turnover; FLNA, FERMT2, and PARVA couple actin to integrin-containing adhesion structures; and SYNM and AHNAK provide additional structural support. The co-abundance signal could therefore represent maintenance and remodeling of mechanically active cell junctions and focal adhesions rather than a single canonical protein complex. This remains a hypothesis because the fact sheet does not provide cell deconvolution, perturbation, or causal validation.

### Important genes

#### FERMT2

- **Related proteins** (co-abundance neighbors): CFL2 (0.92), FLNA (0.91), SYNM (0.89), PARVA (0.86), CALD1 (0.84), AHNAK (0.84), AKAP12 (0.83); STRING partners: FLNA (0.852), PARVA (0.893)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Focal adhesion sites; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FERM domain containing kindlin 2. Enables several functions, including actin binding activity; phosphatidylinositol-3,4,5-trisphosphate binding activity; and type I transforming growth factor beta receptor binding activity. Involved in several processes, including cell surface receptor signaling pathway; positive regulation of cell differentiation; and positive regulation of cellular component biogenesis. Acts upstream of or withi…
- **Diseases (Open Targets)**: open-angle glaucoma (0.501); prostate carcinoma (0.488); glaucoma (0.488); neurodegenerative disease (0.473); primary angle-closure glaucoma (0.407)
- **Europe PMC papers**: 1336
- **Why important**: FERMT2 has the strongest network centrality in the module and connects to CFL2, FLNA, SYNM, PARVA, CALD1, AHNAK, and AKAP12. It occurs in all primary enrichment terms (GO:CC myofibril; q_global = 1.07e-05) through (GO:CC actin cytoskeleton; q_global = 0.0432), is localized to focal adhesion sites, and has established roles in integrin-mediated signaling, cell adhesion, cell-matrix adhesion, and cell junction biology. Its known STRING relationships with FLNA and PARVA and its substantial literature support make it a strong integrative candidate.
- **Conclusion**: Established evidence supports FERMT2 as an adhesion and cytoskeletal hub that helps connect contractile fibers to the cell-matrix interface. It is plausible, but not demonstrated here, that FERMT2 helps organize the shared module across the two tissues.

#### FLNA

- **Related proteins** (co-abundance neighbors): FERMT2 (0.91), CFL2 (0.86), SYNM (0.85), PARVA (0.81); STRING partners: CFL2 (0.888), FERMT2 (0.852)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is a central network member linked to FERMT2, CFL2, SYNM, and PARVA. It appears in every primary term (GO:CC myofibril; q_global = 1.07e-05) through (GO:CC actin cytoskeleton; q_global = 0.0432) and every listed STRING functional annotation (STRING Component Myofibril; within-query FDR = 3.14e-06) through (STRING COMPARTMENTS Sarcomere; within-query FDR = 0.0499). Its established function as an actin crosslinker and linker between actin filaments and membrane glycoproteins directly explains the module's contractile, adhesive, and membrane-associated architecture. It also has the largest literature volume among the selected genes and is tissue enhanced in blood vessel and intestine.
- **Conclusion**: Established evidence identifies FLNA as a structural organizer of actin networks, membrane receptors, cell shape, and migration. The module supports its use as a core scaffold candidate, but does not show that FLNA causally drives the tissue-shared co-abundance pattern.

#### CALD1

- **Related proteins** (co-abundance neighbors): AKAP12 (0.85), FERMT2 (0.84), SYNM (0.83), AHNAK (0.81); STRING partners: TPM1 (0.869)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caldesmon 1. This gene encodes a calmodulin- and actin-binding protein that plays an essential role in the regulation of smooth muscle and nonmuscle contraction. The conserved domain of this protein possesses the binding activities to Ca(2+)-calmodulin, actin, tropomyosin, myosin, and phospholipids. This protein is a potent inhibitor of the actin-tropomyosin activated myosin MgATPase, and serves as a mediating…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.499); diaphragmatic hernia (0.447); glaucoma (0.405); diverticular disease (0.393); open-angle glaucoma (0.390)
- **Europe PMC papers**: 3386
- **Why important**: CALD1 is connected to FERMT2, SYNM, AHNAK, and AKAP12 and participates in the primary contractile and actin terms (GO:CC myofibril; q_global = 1.07e-05), (GO:CC contractile muscle fiber; q_global = 1.07e-05), and (GO:CC supramolecular polymer; q_global = 0.0204) through (GO:CC actin cytoskeleton; q_global = 0.0432). Its established biochemical activities include calmodulin and actin binding, interaction with tropomyosin and myosin, and calcium-dependent regulation of smooth-muscle contraction. Its HPA cell-type profile includes smooth muscle, stromal, myoepithelial, and related contractile populations.
- **Conclusion**: Established evidence makes CALD1 a compelling functional marker of smooth-muscle and nonmuscle contractile regulation in this module. Its position supports a role in coupling calcium-sensitive regulation to the shared cytoskeleton, although that tissue-specific mechanism remains a hypothesis.

#### CFL2

- **Related proteins** (co-abundance neighbors): FERMT2 (0.92), PARVA (0.89), FLNA (0.86), EHD1 (0.86); STRING partners: FLNA (0.888)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cofilin 2. This gene encodes an intracellular protein that is involved in the regulation of actin-filament dynamics. This protein is a major component of intranuclear and cytoplasmic actin rods. It can bind G- and F-actin in a 1:1 ratio of cofilin to actin, and it reversibly controls actin polymerization and depolymerization in a pH-dependent manner. Mutations in this gene cause nemaline myopathy type 7, a f…
- **Diseases (Open Targets)**: nemaline myopathy 7 (0.758); typical nemaline myopathy (0.599); atrial fibrillation (0.525); nemaline myopathy (0.376); Takayasu arteritis (0.303)
- **Europe PMC papers**: 1415
- **Why important**: CFL2 is embedded in the central portion of the network through FERMT2, PARVA, FLNA, and EHD1. It appears in all primary enrichment terms (GO:CC myofibril; q_global = 1.07e-05) through (GO:CC actin cytoskeleton; q_global = 0.0432) and in many STRING annotations, including myofibril, sarcomere, actin cytoskeleton, and actin-binding themes. Its established function is regulation of actin polymerization, depolymerization, and filament severing. HPA associates it with heart muscle, skeletal muscle, tongue, and smooth-muscle-related cell types, and disease evidence includes nemaline myopathy.
- **Conclusion**: Established evidence supports CFL2 as the actin-dynamics component of the module and links the co-abundance pattern to muscle-related cytoskeletal remodeling. It may help tune contractile fiber turnover, but the fact sheet does not establish a causal role in either tissue.

#### TPM1

- **Related proteins** (co-abundance neighbors): AHNAK (0.82); STRING partners: CALD1 (0.869)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tropomyosin 1. This gene is a member of the tropomyosin family of highly conserved, widely distributed actin-binding proteins involved in the contractile system of striated and smooth muscles and the cytoskeleton of non-muscle cells. Tropomyosin is composed of two alpha-helical chains arranged as a coiled-coil. It is polymerized end to end along the two grooves of actin filaments and provides stability to the fi…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy (0.798); left ventricular noncompaction (0.760); left ventricular noncompaction 9 (0.664); familial isolated dilated cardiomyopathy (0.639); hypertrophic cardiomyopathy 3 (0.596)
- **Europe PMC papers**: 6278
- **Why important**: TPM1 is present in every primary enrichment term (GO:CC myofibril; q_global = 1.07e-05) through (GO:CC actin cytoskeleton; q_global = 0.0432), is annotated in multiple STRING contractile and cytoskeletal terms, and has a known relationship with CALD1. Its established function is stabilization and regulation of actin filaments in striated muscle, smooth muscle, and nonmuscle cytoskeletons. HPA shows tissue enhancement in heart and skeletal muscle, while the module context and the other genes support relevance to contractile cell biology.
- **Conclusion**: Established evidence supports TPM1 as a core actin-filament stabilizer and contractile-system component. Its inclusion makes the contractile interpretation biologically credible, while any specific role in autonomic nervous system or rectal physiology requires direct validation.

## Module 4

**Tissue pair**: autonomic_nervous_system and rectum  
**Genes (24)**: AIMP2, ALDOC, MTHFD1, CLTC, CLIC1, SHMT2, H1-5, H4C1, HNRNPK, IPO4, TMPO, TMPO, MOGS, NUP50, RBM39, RPL12, RPRD1B, FARSB, MARS1, VARS1, CCT7, CCT8, TMEM33, VDAC2

### Function

No GO or KEGG term passed global correction, so the module does not support a formally significant pathway assignment from those analyses. Its gene content instead points to a mixed intracellular program involving protein folding and stabilization, translation and aminoacyl-tRNA biology, RNA processing and nuclear transport, chromatin organization, mitochondrial and endoplasmic-reticulum functions, and central metabolism. The strongest network-centered interpretation is a general proteostasis and gene-expression-support module rather than a narrowly specialized autonomic-nervous-system or rectal pathway. The STRING domain signals (STRING Pfam Glutathione S-transferase, C-terminal domain; within-query FDR = 0.0334), (STRING InterPro Glutathione S-transferase, C-terminal-like; within-query FDR = 0.0491), and (STRING InterPro Glutathione S-transferase, C-terminal domain superfamily; within-query FDR = 0.0491) provide supplementary support for a shared glutathione-S-transferase-like domain architecture among AIMP2, MARS1, VARS1, and CLIC1, but they do not establish a common biochemical pathway or global enrichment.

**Cell composition.** The module is not dominated by secreted or plasma proteins: the HPA summary reports no secreted genes. Most annotated genes have low tissue specificity, and rectal protein detection is broadly present among the tested module proteins. This favors a broadly expressed intracellular or housekeeping-like component, potentially reflecting common cellular composition or general biosynthetic demand in both tissues rather than a tissue-exclusive function. There is some cell-type structure: several genes are enhanced in erythrocyte progenitors, esophageal epithelial populations, neutrophils, or progenitor populations, while other genes are enhanced in liver, lymphoid tissue, skeletal muscle, brain, or neural cell types. The overall HPA profile does not support a simple blood-cell module because immune-cell specificity is generally low, although blood or shared cell-type contributions remain plausible and should be tested with cell deconvolution or single-cell data.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING contains a limited set of high-confidence relationships rather than a densely connected established interaction network. Known relationships include the CCT7-CCT8 chaperonin pair; the AIMP2-MARS1, MARS1-VARS1, and FARSB-VARS1 aminoacyl-tRNA-related connections; the MTHFD1-SHMT2 metabolic connection; and the H1-5-H4C1 and H4C1-IPO4 chromatin or nuclear-import connections. The STRING graph also links CCT7 with RPL12 and CCT8 with several module proteins, but these edges should not be interpreted as proof of one complex. The supplementary STRING domain results (STRING Pfam Glutathione S-transferase, C-terminal domain; within-query FDR = 0.0334), (STRING InterPro Glutathione S-transferase, C-terminal-like; within-query FDR = 0.0491), and (STRING InterPro Glutathione S-transferase, C-terminal domain superfamily; within-query FDR = 0.0491) connect AIMP2, MARS1, VARS1, and CLIC1 through glutathione-S-transferase-like domain annotations. hu.MAP independently places MARS1 with AIMP2 in aminoacyl-tRNA synthetase-associated complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), CCT7 with CCT8 in CCT-associated complexes (hu.MAP huMAP3_07938.1) and (hu.MAP huMAP3_06559.1) through (hu.MAP huMAP3_14584.1), and H4C1 with IPO4 in multiple histone-chromatin or nuclear-import complexes (hu.MAP huMAP3_05517.1), (hu.MAP huMAP3_06020.1), (hu.MAP huMAP3_08143.1), (hu.MAP huMAP3_09859.1), (hu.MAP huMAP3_10747.1), (hu.MAP huMAP3_12711.1). These are mostly partial overlaps with larger complexes, so they validate several local functional neighborhoods but not a single complete molecular complex.

**STRING interactions (score >= 0.7)**: 9 of 276 gene pairs: AIMP2–MARS1 (0.999); CCT7–CCT8 (0.999); CCT7–RPL12 (0.758); FARSB–MARS1 (0.705); FARSB–VARS1 (0.776); H1-5–H4C1 (0.777); H4C1–IPO4 (0.942); MARS1–VARS1 (0.902); MTHFD1–SHMT2 (0.996)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam Glutathione S-transferase, C-terminal domain (FDR = 0.0334, 3 genes); InterPro Glutathione S-transferase, C-terminal-like (FDR = 0.0491, 4 genes); InterPro Glutathione S-transferase, C-terminal domain superfamily (FDR = 0.0491, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05517.1 (H4C1, IPO4; 2/13); huMAP3_06020.1 (H4C1, IPO4; 2/13); huMAP3_02637.1 (MARS1, AIMP2; 2/14); huMAP3_13688.1 (MARS1, AIMP2; 2/14); huMAP3_08143.1 (H4C1, IPO4; 2/21); huMAP3_07938.1 (CCT8, CCT7; 2/23); huMAP3_09859.1 (H4C1, IPO4; 2/24); huMAP3_10747.1 (H4C1, IPO4; 2/25); huMAP3_06559.1 (CCT8, CCT7; 2/25); huMAP3_09191.1 (CCT8, CCT7; 2/32); huMAP3_12711.1 (H4C1, IPO4; 2/35); huMAP3_10656.1 (CCT8, CCT7; 2/36); huMAP3_14584.1 (CCT8, CCT7; 2/61); huMAP3_09592.1 (VDAC2, TMEM33; 2/95)

### Novelty

The module should not be described as a newly discovered molecular complex or a newly established pathway. Several of its local relationships and functional neighborhoods are already represented in STRING and hu.MAP, especially chaperonin, aminoacyl-tRNA synthetase, chromatin, and metabolic relationships. Its potentially novel aspect is the coordinated co-abundance of these established cellular systems across autonomic nervous system and rectum samples. That coordination may be biologically meaningful, but novelty cannot be inferred solely from incomplete database coverage or from the absence of some module pairs in STRING or hu.MAP. A novelty claim would require replication in independent cohorts, control for cell composition and technical effects, and comparison with previously reported cross-tissue co-abundance modules.

**Hypothesis.** Hypothesis: this conserved module reflects a shared cellular state in which proteostasis, translation, RNA processing, nuclear organization, one-carbon metabolism, and endoplasmic-reticulum stress handling are coordinately maintained across the two tissues. CCT chaperonin activity could support folding of newly synthesized proteins, aminoacyl-tRNA machinery could support translational capacity, MTHFD1-SHMT2 could supply one-carbon and glycine-related metabolic support, and nuclear transport, histone, and RNA-binding proteins could couple this biosynthetic state to gene regulation. TMEM33 and MOGS suggest a possible endoplasmic-reticulum quality-control component, while VDAC2 may connect cellular metabolism with mitochondrial membrane and stress responses. This is a testable model, not an established pathway assignment: it predicts that module activity should track cellular biosynthetic load or proteotoxic and ER stress, and that its apparent conservation should weaken after adjustment for shared cell types and sample quality.

### Important genes

#### CCT8

- **Related proteins** (co-abundance neighbors): VARS1 (0.87), TMPO (0.85), MTHFD1 (0.84), NUP50 (0.84), FARSB (0.83), RBM39 (0.83), ALDOC (0.82), TMPO (0.81), H1-5 (0.81), TMEM33 (0.81), CLIC1 (0.81), SHMT2 (0.81), RPRD1B (0.80); STRING partners: CCT7 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 has the strongest network position in the supplied module and connects to proteins spanning chaperoning, metabolism, nuclear transport, RNA-associated functions, and aminoacyl-tRNA biology. Its established annotation identifies it as a subunit of the CCT chaperonin involved in protein folding and stabilization. It also has independent STRING support through CCT7 and broad hu.MAP representation (hu.MAP huMAP3_07938.1), (hu.MAP huMAP3_06559.1), (hu.MAP huMAP3_09191.1), (hu.MAP huMAP3_10656.1), and (hu.MAP huMAP3_14584.1). Its literature is extensive, making it a well-characterized anchor rather than a speculative marker.
- **Conclusion**: Established evidence supports CCT8 as a central proteostasis-related hub in this module. The hypothesis that it organizes the wider co-abundance pattern by coupling folding demand to translation and cellular stress remains unproven.

#### RBM39

- **Related proteins** (co-abundance neighbors): HNRNPK (0.91), VDAC2 (0.89), CCT7 (0.89), MTHFD1 (0.83), CCT8 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 39. This gene encodes a member of the U2AF65 family of proteins. The encoded protein is found in the nucleus, where it co-localizes with core spliceosomal proteins. It has been shown to play a role in both steroid hormone receptor-mediated transcription and alternative splicing, and it is also a transcriptional coregulator of the viral oncoprotein v-Rel. Multiple transcript variants have been observed…
- **Diseases (Open Targets)**: neurodegenerative disease (0.401); endometrial cancer (0.220); skin neoplasm (0.217); skin cancer (0.217); actinic keratosis (0.217)
- **Europe PMC papers**: 1169
- **Why important**: RBM39 occupies a highly connected position linking HNRNPK, VDAC2, CCT7, MTHFD1, and CCT8. Its established functions include RNA processing, alternative splicing, and transcriptional coregulation, with nuclear-speckle localization and tissue enhancement in bone marrow. It has no reported STRING or hu.MAP relationship in the fact sheet, which makes its position in the co-abundance network especially informative but also more dependent on the dataset.
- **Conclusion**: Established evidence supports RBM39 as a plausible RNA-processing and transcriptional component of the module. Its apparent role as a bridge between proteostasis, metabolism, and RNA regulation is a hypothesis based on network placement, not a demonstrated physical mechanism.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): RBM39 (0.91), IPO4 (0.85), MTHFD1 (0.83), TMEM33 (0.82), VDAC2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is connected to RBM39, IPO4, MTHFD1, TMEM33, and VDAC2, placing it at an interface between nuclear RNA biology, transport, metabolism, and organelle-associated proteins. Its established annotation supports roles in pre-mRNA processing, transcriptional regulation, RNA metabolism, and signal transduction. It is broadly expressed and has substantial disease and literature representation, while the supplied STRING and hu.MAP results do not provide a corresponding known interaction for this module.
- **Conclusion**: Established evidence supports HNRNPK as a multifunctional RNA and transcription regulator that could explain part of the module's gene-expression character. A direct role in coordinating the other module neighborhoods is conjectural and requires physical interaction or perturbation evidence.

#### MTHFD1

- **Related proteins** (co-abundance neighbors): CCT8 (0.84), HNRNPK (0.83), RBM39 (0.83); STRING partners: SHMT2 (0.996)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methylenetetrahydrofolate dehydrogenase, cyclohydrolase and formyltetrahydrofolate synthetase 1. This gene encodes a protein that possesses three distinct enzymatic activities, 5,10-methylenetetrahydrofolate dehydrogenase, 5,10-methenyltetrahydrofolate cyclohydrolase and 10-formyltetrahydrofolate synthetase. Each of these activities catalyzes one of three sequential reactions in the interconversion of 1-carbon derivatives of tetrahydrofolate, which are substrates for methionine, thymidylate, …
- **Diseases (Open Targets)**: combined immunodeficiency and megaloblastic anemia with or without hyperhomocysteinemia (0.773); severe combined immunodeficiency (0.473); neural tube defects, folate-sensitive (0.414); isolated spina bifida (0.376); atrial fibrillation (0.332)
- **Europe PMC papers**: 1939
- **Why important**: MTHFD1 links the central network to one-carbon metabolism and is connected to CCT8, HNRNPK, and RBM39. Its established enzymatic functions generate and interconvert folate-derived one-carbon units used in methionine, thymidylate, and purine synthesis. The strong STRING relationship with SHMT2 [the MTHFD1-SHMT2 edge] provides a known metabolic connection, and its disease associations include folate-sensitive developmental and immune disorders.
- **Conclusion**: Established evidence supports MTHFD1 as a metabolic contributor capable of supplying biosynthetic demands. The hypothesis that its metabolic activity drives the shared tissue module or couples directly to RNA and chaperone functions remains untested.

#### TMEM33

- **Related proteins** (co-abundance neighbors): MOGS (0.85), HNRNPK (0.82), VDAC2 (0.82), CCT8 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: transmembrane protein 33. Involved in positive regulation of endoplasmic reticulum unfolded protein response; regulation of endoplasmic reticulum tubular network organization; and response to endoplasmic reticulum stress. Located in endoplasmic reticulum membrane; melanosome; and nuclear envelope. Is integral component of endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: squamous cell carcinoma (0.156); thrombophilia (0.100); neoplasm (0.089); lung adenocarcinoma (0.080); cervical squamous cell carcinoma (0.077)
- **Europe PMC papers**: 338
- **Why important**: TMEM33 connects VDAC2, HNRNPK, CCT8, and MOGS, thereby linking endoplasmic-reticulum organization and stress biology with mitochondrial and cytosolic components. Its established annotation includes regulation of ER tubular network organization and positive regulation of IRE1- and PERK-mediated unfolded-protein responses. It is represented with VDAC2 in hu.MAP complex (hu.MAP huMAP3_09592.1), although that complex contains many other membrane and organelle proteins and does not establish a specific TMEM33 mechanism here.
- **Conclusion**: Established evidence supports TMEM33 as an ER organization and stress-response marker within the module. Its proposed role as the ER-side coordinator of a broader proteostasis state is a hypothesis that needs stress-response measurements and perturbation experiments.

#### H4C1

- **Related proteins** (co-abundance neighbors): none; STRING partners: H1-5 (0.777), IPO4 (0.942)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_05517.1, huMAP3_06020.1, huMAP3_08143.1, huMAP3_09859.1, huMAP3_10747.1, huMAP3_12711.1
- **Function (MyGene.info)**: H4 clustered histone 1. Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Two molecules of each of the four core histones (H2A, H2B, H3, and H4) form an octamer, around which approximately 146 bp of DNA is wrapped in repeating units, called nucleosomes. The linker histone, H1, interacts with linker DNA between nucleosomes and functions in the com…
- **Diseases (Open Targets)**: viral infectious disease (0.503); infectious disease (0.503); Tessadori-Van Haaften neurodevelopmental syndrome 3 (0.462); breast carcinoma (0.390); cancer (0.371)
- **Europe PMC papers**: 216
- **Why important**: H4C1 is an informative chromatin component despite having no co-abundance neighbors in the supplied subgraph. Its established annotation supports nucleosome assembly, chromatin organization, telomere organization, and transcriptional repression. It has STRING relationships with H1-5 and IPO4 and appears with IPO4 across multiple hu.MAP histone and chromatin-associated complexes (hu.MAP huMAP3_05517.1), (hu.MAP huMAP3_06020.1), (hu.MAP huMAP3_08143.1), (hu.MAP huMAP3_09859.1), (hu.MAP huMAP3_10747.1), and (hu.MAP huMAP3_12711.1). Its HPA profile includes lymphoid and skeletal-muscle enhancement and enrichment in several progenitor or epithelial cell populations, so cellular composition must be considered.
- **Conclusion**: Established evidence supports H4C1 as a chromatin-related member with corroborated local database context despite weak module-network connectivity. Its inclusion as evidence for coordinated chromatin remodeling across the two tissues is plausible but not demonstrated.

## Module 5

**Tissue pair**: autonomic_nervous_system and rectum  
**Genes (5)**: AP3B1, MATR3, PLCH1, PPP6R3, PSMC2

### Function

The module does not support a single statistically established pathway-level function: no GO or KEGG term passed global correction, and no supplementary STRING functional-enrichment term was reported. Its gene-level annotations suggest a mixed intracellular program involving post-transcriptional regulation and nuclear organization through MATR3, signal-transduction regulation through PPP6R3, proteasome-mediated protein turnover through PSMC2, vesicle and organelle transport through AP3B1, and phosphoinositide signaling with calcium release through PLCH1. These annotations are functional clues rather than enrichment evidence. The network is centered on MATR3, which connects to PPP6R3, AP3B1, and PLCH1, while PPP6R3 connects to PSMC2. Because the graph is sparse and lacks pathway enrichment, the safest interpretation is a co-abundance pattern linking general intracellular regulation, trafficking, proteostasis, and signaling rather than a demonstrated canonical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of its genes is annotated as secreted. HPA reports low tissue specificity for most genes and low immune-cell specificity for nearly all of them, with PLCH1 tissue-enhanced in lymphoid tissue, retina, and testis. Four genes are cell-type enhanced, but the reported cell types are heterogeneous and include epithelial, endocrine, glial, germ-cell, and progenitor populations; no blood-cell enrichment pattern was reported. Protein detection was observed for most genes in rectum, while no matching HPA tissue was available for autonomic nervous system. Overall, the module does not resemble a coherent plasma-protein or blood-cell module. Its sharing between tissues could reflect broadly expressed intracellular proteins, mixed cellular composition, or coordinated abundance in a cell population, but the available HPA evidence does not identify one shared cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship was reported among any module-gene pair, no STRING functional-enrichment term was reported, and no hu.MAP complex contained multiple module members. Thus, the observed co-abundance edges are not independently corroborated by the supplied STRING or hu.MAP evidence. This does not disprove biological coordination: co-abundance can arise from regulation, cell composition, or shared expression without a physical interaction. It does mean that the module should not be described as a known protein complex or established interaction network. The most interpretable internal structure is the MATR3-centered pattern, with PPP6R3 providing the only connection toward PSMC2 and AP3B1 and PLCH1 appearing as separate MATR3-linked functional branches.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially interesting tissue-pair co-abundance observation, but it cannot be called a new biological pathway or a newly discovered interaction module on the supplied evidence. The absence of STRING and hu.MAP support alone does not establish novelty, and the lack of globally significant GO or KEGG enrichment prevents a strong pathway-level claim. A cautious novelty statement is that the specific shared co-abundance pattern across autonomic nervous system and rectum may not be represented as a curated complex or high-confidence interaction set in the supplied resources, while its biological novelty remains unproven. Replication in independent cohorts, preservation testing, cell-composition adjustment, and comparison with published tissue co-expression modules would be needed before claiming a new finding.

**Hypothesis.** Hypothesis: the module may represent coordinated abundance of broadly expressed intracellular machinery in a shared or similarly composed cell population across autonomic nervous system and rectum. MATR3 could provide a post-transcriptional or nuclear regulatory context; PPP6R3 could modulate phosphatase-dependent signaling; PSMC2 could reflect proteostasis demand; AP3B1 could reflect vesicle and organelle trafficking; and PLCH1 could connect signaling inputs to phosphoinositide turnover and calcium release. This is a mechanistic hypothesis generated from gene functions and the internal co-abundance topology, not an established pathway claim. It should be tested by cell-resolved expression, perturbation of MATR3 or PPP6R3, measurement of PLCH1-dependent calcium and lipid signaling, and assessment of proteasome and vesicle-trafficking outputs.

### Important genes

#### MATR3

- **Related proteins** (co-abundance neighbors): AP3B1 (0.85), PPP6R3 (0.83), PLCH1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: matrin 3. This gene encodes a nuclear matrix protein, which is proposed to stabilize certain messenger RNA species. Mutations of this gene are associated with distal myopathy 2, which often includes vocal cord and pharyngeal weakness. Alternatively spliced transcript variants, including read-through transcripts composed of the upstream small nucleolar RNA host gene 4 (non-protein coding) and matrin 3 gene s…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.735); distal myopathy with vocal cord weakness (0.569); neurodegenerative disease (0.529); distal myopathy (0.384); hereditary disease (0.193)
- **Europe PMC papers**: 1756
- **Why important**: MATR3 is the central node in the module, connecting to PPP6R3, AP3B1, and PLCH1. It encodes a nuclear matrix protein implicated in messenger RNA stabilization and post-transcriptional regulation, and its annotations include activation of innate immune response and cardiac developmental processes. It has the largest literature volume among the module genes and disease associations including distal myopathy and amyotrophic lateral sclerosis, making it the strongest candidate for organizing or interpreting the module despite the absence of global enrichment.
- **Conclusion**: Established evidence supports MATR3 as the network hub and as a nuclear/post-transcriptional regulator with disease relevance. It is plausible, but not established, that MATR3-related RNA regulation contributes to the shared co-abundance pattern or links the other module branches.

#### PPP6R3

- **Related proteins** (co-abundance neighbors): PSMC2 (0.87), MATR3 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase 6 regulatory subunit 3. Protein phosphatase regulatory subunits, such as SAPS3, modulate the activity of protein phosphatase catalytic subunits by restricting substrate specificity, recruiting substrates, and determining the intracellular localization of the holoenzyme. SAPS3 is a regulatory subunit for the protein phosphatase-6 catalytic subunit (PPP6C; MIM 612725) (Stefansson and Brautigan, 2006 [PubMed 16769727]).[sup…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.383); hair color (0.341); bone fracture (0.253); Pathologic fracture (0.190); obesity disorder (0.185)
- **Europe PMC papers**: 243
- **Why important**: PPP6R3 is the second most connected node and is the bridge between MATR3 and PSMC2. It encodes a regulatory subunit of protein phosphatase six that can influence substrate specificity, recruitment, and intracellular localization, with a gene-level annotation for regulation of signal transduction. Its position makes it a candidate connector between regulatory signaling and proteostasis rather than merely a peripheral marker.
- **Conclusion**: Established evidence supports PPP6R3 as a phosphatase regulatory subunit and an internally connected module component. Its role as the mechanistic bridge between MATR3-associated regulation and PSMC2-associated proteostasis is a hypothesis requiring experimental validation.

#### PLCH1

- **Related proteins** (co-abundance neighbors): MATR3 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phospholipase C eta 1. PLCH1 is a member of the PLC-eta family of the phosphoinositide-specific phospholipase C (PLC) superfamily of enzymes that cleave phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2) to generate second messengers inositol 1,4,5-trisphosphate (IP3) and diacylglycerol (DAG) (Hwang et al., 2005 [PubMed 15702972]).[supplied by OMIM, Jun 2009].
- **Diseases (Open Targets)**: holoprosencephaly 14 (0.577); alobar holoprosencephaly (0.370); neurodegenerative disease (0.369); insomnia (0.364); adolescent idiopathic scoliosis (0.313)
- **Europe PMC papers**: 367
- **Why important**: PLCH1 is a MATR3-linked signaling gene encoding a phospholipase C eta family member. Its annotated functions include phosphoinositide metabolism, intracellular signaling, and release of sequestered calcium into the cytosol. It is tissue-enhanced in lymphoid tissue, retina, and testis and has disease associations including holoprosencephaly, neurodegenerative disease, and insomnia, providing a plausible signaling output for the module.
- **Conclusion**: Established evidence supports PLCH1 as a phosphoinositide and calcium-signaling enzyme with tissue- and disease-relevant annotations. Its connection to the module's nuclear and trafficking genes does not establish a shared signaling pathway; the proposed role as a signaling arm of the module remains hypothetical.

#### AP3B1

- **Related proteins** (co-abundance neighbors): MATR3 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor related protein complex 3 subunit beta 1. This gene encodes a protein that may play a role in organelle biogenesis associated with melanosomes, platelet dense granules, and lysosomes. The encoded protein is part of the heterotetrameric AP-3 protein complex which interacts with the scaffolding protein clathrin. Mutations in this gene are associated with Hermansky-Pudlak syndrome type 2. Two transcript variants encoding different isoforms h…
- **Diseases (Open Targets)**: Hermansky-Pudlak syndrome 2 (0.837); Hermansky-Pudlak syndrome (0.752); cancer (0.546); Parkinson disease (0.470); neurodegenerative disease (0.452)
- **Europe PMC papers**: 1324
- **Why important**: AP3B1 is linked to the central MATR3 node and encodes a subunit of the adaptor protein complex three, which participates in vesicle-mediated transport and organelle biogenesis involving lysosomes, melanosomes, and platelet dense granules. It is associated with Hermansky-Pudlak syndrome type two and has annotations involving antigen presentation, anterograde axonal transport, and vesicle transport. Its vesicular localization provides a concrete trafficking component in an otherwise heterogeneous module.
- **Conclusion**: Established evidence supports AP3B1 as a vesicle-trafficking and organelle-biogenesis factor with a well-defined inherited disease association. Its co-abundance with MATR3 and PLCH1 may indicate coordinated trafficking or cell-state regulation, but no physical interaction or shared complex was demonstrated.

#### PSMC2

- **Related proteins** (co-abundance neighbors): PPP6R3 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is the terminal node connected to PPP6R3 and encodes an ATPase subunit of the proteasome regulatory particle. Its annotations include ubiquitin-dependent protein catabolism, proteasomal degradation, and response to oxidative stress, while its disease associations include plasma cell myeloma and other neoplastic or protein-aggregation-related conditions. It therefore represents the module's clearest proteostasis component.
- **Conclusion**: Established evidence supports PSMC2 as a proteasome component involved in regulated protein degradation. Its placement downstream of PPP6R3 is consistent with a possible signaling-to-proteostasis relationship, but the co-abundance data do not show that PPP6R3 regulates PSMC2 in this tissue pair.

## Module 6

**Tissue pair**: autonomic_nervous_system and rectum  
**Genes (26)**: CISD2, CIAPIN1, CTBP2, DDX21, ADAR, HADHB, ETFA, FUS, HMGCS1, HMGA1, HYOU1, LARP7, SNU13, NUP98, OCIAD1, PRKDC, PTCD3, CAD, MRPL11, MRPS31, SLC25A13, SEC24C, SF3B3, SRRT, VPS35, SLC30A7

### Function

The module does not have a single statistically established GO or KEGG function: no GO/KEGG term passed global correction. Its architecture nevertheless suggests coordinated cellular maintenance involving RNA processing and splicing, mitochondrial gene expression and translation, mitochondrial transport, protein and vesicle handling, and responses to cellular stress. The strongest network hub is SF3B3, linking several module genes to the spliceosome and RNA-processing machinery. PTCD3, MRPS31, and MRPL11 connect a mitochondrial translation branch, while SLC25A13 links mitochondrial transport and calcium-responsive aspartate–glutamate exchange to the broader network. HYOU1 provides a plausible stress and protein-folding component. These functional interpretations are supported by the individual gene annotations and network structure, not by globally significant enrichment.

**Cell composition.** This is not primarily a plasma-protein, secreted-protein, or blood-cell module. HPA identifies only one secreted gene, and all genes have low immune-cell specificity. Most genes have low tissue specificity, with a smaller set showing tissue or cell-type enhancement in liver, muscle, tongue, esophageal epithelial cells, neutrophils, germ-cell populations, and other cell types. Protein detection is broadly present in rectum, whereas autonomic-nervous-system protein matching was unavailable. The composition therefore favors a broadly expressed intracellular program rather than a blood-contamination explanation, although shared epithelial, neuronal, or other cellular composition could still contribute to co-abundance across the two tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a coherent but incomplete set of known relationships. The strongest links include the mitochondrial ribosomal and RNA-processing relationships among PTCD3, MRPS31, and MRPL11; the spliceosomal relationship between SF3B3 and SNU13; the metabolic relationship between HMGCS1 and HADHB; the fatty-acid oxidation relationship between ETFA and HADHB; and the association between DDX21 and LARP7. STRING supplementary compartment evidence places several members in a ribonucleoprotein complex (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.0351), but this is not global enrichment evidence. hu.MAP independently supports shared complex membership: PTCD3 and MRPS31 occur together in two complexes (hu.MAP huMAP3_05807.1) (hu.MAP huMAP3_05954.1), while SF3B3 and SNU13 occur together in spliceosomal complexes (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_08980.1). Because only a minority of possible module pairs are high-confidence STRING interactions and the hu.MAP complexes contain many additional proteins, the module is best viewed as a connected co-abundance program assembled from several related intracellular processes, rather than a single experimentally established complex.

**STRING interactions (score >= 0.7)**: 7 of 325 gene pairs: DDX21–LARP7 (0.866); ETFA–HADHB (0.829); HADHB–HMGCS1 (0.993); MRPL11–MRPS31 (0.889); MRPL11–PTCD3 (0.888); MRPS31–PTCD3 (0.999); SF3B3–SNU13 (0.994)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Ribonucleoprotein complex (FDR = 0.0351, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05807.1 (LARP7, MRPS31, PTCD3; 3/81); huMAP3_05954.1 (MRPS31, PTCD3; 2/28); huMAP3_06511.1 (SNU13, SF3B3; 2/79); huMAP3_08980.1 (SNU13, SF3B3; 2/97)

### Novelty

The module should not be called a newly discovered molecular complex or a proven new pathway. Several of its central relationships and complex memberships are already represented in STRING and hu.MAP, especially the mitochondrial ribosomal and spliceosomal connections (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.0351) (hu.MAP huMAP3_05807.1) (hu.MAP huMAP3_05954.1) (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_08980.1). Its potentially novel aspect is the tissue-pair-specific co-abundance pattern linking these established intracellular systems across autonomic nervous system and rectum. That pattern may reflect tissue context, shared cell composition, or coordinated physiology, but novelty cannot be established from absence of database edges alone. Independent replication, comparison with existing tissue co-expression resources, and experimental validation would be required.

**Hypothesis.** Hypothesis: the shared module reflects a general intracellular resilience and biosynthetic state in which RNA maturation and transcriptional control are coordinated with mitochondrial translation, mitochondrial metabolite exchange, lipid oxidation, and endoplasmic-reticulum stress handling. In rectum and autonomic nervous system, cells experiencing similar demands for protein synthesis, mitochondrial function, and stress adaptation may therefore co-vary in abundance of these proteins. This hypothesis predicts that module activity should track mitochondrial and RNA-processing readouts, but the current evidence does not establish directionality, cell-of-origin, or causal regulation.

### Important genes

#### SF3B3

- **Related proteins** (co-abundance neighbors): SLC30A7 (0.89), FUS (0.88), SLC25A13 (0.87), HYOU1 (0.87), PRKDC (0.85), CAD (0.85), SEC24C (0.85), SNU13 (0.83), PTCD3 (0.82), HMGA1 (0.81); STRING partners: SNU13 (0.994)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Nucleoli rim; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: splicing factor 3b subunit 3. This gene encodes subunit 3 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); dengue disease (0.370); cervical cancer (0.189); cervical carcinoma (0.189); prostate cancer (0.111)
- **Europe PMC papers**: 965
- **Why important**: SF3B3 is the highest-positioned network hub in the module and connects many otherwise separate genes. It is a core subunit of the SF3B and U2 snRNP machinery, participates in spliceosomal assembly and pre-mRNA splicing, and has direct STRING and hu.MAP support with SNU13 (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.0351) (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_08980.1). It is broadly expressed, detected in rectum, and has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports SF3B3 as a central RNA-splicing and network-integration component. It is reasonable to regard it as an important marker of the module’s RNA-processing arm. It is not established that SF3B3 drives the cross-tissue co-abundance pattern or connects the mitochondrial genes mechanistically.

#### PTCD3

- **Related proteins** (co-abundance neighbors): SLC25A13 (0.89), HYOU1 (0.88), OCIAD1 (0.87), PRKDC (0.87), CAD (0.85), HMGA1 (0.85), SF3B3 (0.82), CTBP2 (0.82); STRING partners: MRPL11 (0.888), MRPS31 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_05807.1, huMAP3_05954.1
- **Function (MyGene.info)**: pentatricopeptide repeat domain 3. Enables rRNA binding activity and ribosomal small subunit binding activity. Involved in mitochondrial translation. Located in several cellular components, including cytosol; mitochondrion; and nucleoplasm. Implicated in combined oxidative phosphorylation deficiency 51. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: combined oxidative phosphorylation deficiency 51 (0.678); mixed connective tissue disease (0.230); hereditary disease (0.193); alcohol drinking (0.110); posterior cortical atrophy (0.074)
- **Europe PMC papers**: 308
- **Why important**: PTCD3 is a high-connectivity module hub and links the RNA-processing neighborhood to a mitochondrial translation branch. It binds rRNA and mitochondrial ribosomal small-subunit components, is involved in mitochondrial translation, and has strong STRING relationships with MRPS31 and MRPL11 as well as hu.MAP membership with MRPS31 (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.0351) (hu.MAP huMAP3_05807.1) (hu.MAP huMAP3_05954.1). Its disease association with combined oxidative-phosphorylation deficiency provides biological relevance.
- **Conclusion**: Established evidence supports PTCD3 as a mitochondrial RNA and translation component and as one of the best-supported bridges within the module. A role in coordinating mitochondrial output with nuclear RNA processing is a plausible interpretation, but remains a hypothesis.

#### SLC25A13

- **Related proteins** (co-abundance neighbors): SLC30A7 (0.92), CAD (0.90), PTCD3 (0.89), LARP7 (0.87), SF3B3 (0.87), OCIAD1 (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 25 member 13. This gene is a member of the mitochondrial carrier family. The encoded protein contains four EF-hand Ca(2+) binding motifs in the N-terminal domain, and localizes to mitochondria. The protein catalyzes the exchange of aspartate for glutamate and a proton across the inner mitochondrial membrane, and is stimulated by calcium on the external side of the inner mitochondrial membrane. Mutations in this…
- **Diseases (Open Targets)**: neonatal intrahepatic cholestasis due to citrin deficiency (0.804); citrullinemia type II (0.756); citrin deficiency (0.652); citrullinemia (0.649); citrullinemia type I (0.464)
- **Europe PMC papers**: 1421
- **Why important**: SLC25A13 is a prominent network connector with links to PTCD3, SF3B3, SLC30A7, CAD, OCIAD1, and LARP7. It is a mitochondrial calcium-stimulated aspartate–glutamate transporter involved in mitochondrial transport and is tissue-enriched in liver, with disease associations involving citrin deficiency and citrullinemia. It provides a metabolic and transport axis that complements the RNA and ribosome components.
- **Conclusion**: Established evidence supports SLC25A13 as a mitochondrial metabolite-exchange component and a meaningful metabolic representative of the module. Its co-abundance with RNA-processing genes may indicate shared cellular state or metabolic support for biosynthesis, but a direct regulatory connection is not demonstrated.

#### HYOU1

- **Related proteins** (co-abundance neighbors): PTCD3 (0.88), SF3B3 (0.87), MRPS31 (0.86), CTBP2 (0.85), SNU13 (0.82), HMGCS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 occupies a highly connected position and links mitochondrial-ribosome, spliceosomal, transcriptional, and metabolic neighborhoods. It is an HSP seventy-family protein associated with endoplasmic-reticulum protein folding, secretion, hypoxia, stress responses, and reduced apoptosis. It is detected in rectum and has cell-type enhancement in several stress-relevant populations.
- **Conclusion**: Established evidence supports HYOU1 as a cellular-stress and endoplasmic-reticulum protein-homeostasis component. Its position makes it a plausible integrator of stress with mitochondrial and RNA-processing demands, but the module does not establish that HYOU1 causes the observed co-abundance.

#### PRKDC

- **Related proteins** (co-abundance neighbors): HMGA1 (0.94), SNU13 (0.89), VPS35 (0.88), PTCD3 (0.87), SF3B3 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase, DNA-activated, catalytic subunit. This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to DNA-PKcs deficiency (0.752); neurodegenerative disease (0.548); severe combined immunodeficiency (0.470); combined immunodeficiency (0.464); ovarian neoplasm (0.210)
- **Europe PMC papers**: 12461
- **Why important**: PRKDC is a central network member connected to SF3B3, PTCD3, SNU13, HMGA1, and VPS35. It encodes the catalytic subunit of DNA-dependent protein kinase, with established roles in DNA double-strand-break repair, recombination, telomere maintenance, and innate immune signaling. It has extensive literature and strong disease relevance, including immunodeficiency and neurodegenerative-disease associations.
- **Conclusion**: Established evidence supports PRKDC as a genome-maintenance and DNA-repair component that may explain the module’s link to nuclear integrity. Its co-abundance with RNA-processing and mitochondrial genes is consistent with a broad cellular-maintenance state, but does not prove a shared DNA-repair mechanism.

## Module 7

**Tissue pair**: autonomic_nervous_system and rectum  
**Genes (12)**: DCUN1D1, MKI67, MCM2, MCM4, EMG1, NSUN2, DDOST, LPCAT2, PUS1, STAT1, TM9SF4, TPD52L2

### Function

This is a heterogeneous module with its clearest biological signals in genome replication and cell proliferation, RNA modification and processing, membrane lipid remodeling, and cytokine-responsive transcription. MCM2 and MCM4 connect the module to the conserved MCM replication machinery, while NSUN2, PUS1, and EMG1 indicate RNA modification or ribosome biogenesis. MKI67 supports a proliferative-cell interpretation, LPCAT2 supports membrane and inflammatory lipid metabolism, and STAT1 supports cytokine and antiviral transcriptional responses. The module should not be assigned a single established pathway: no GO or KEGG term passed global correction, and STRING functional enrichment was absent. The network may therefore represent a shared cellular state or mixture of related cell populations rather than a sharply defined biochemical pathway.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins; only a minority of genes are annotated as secreted, and most are intracellular or membrane-associated. Many genes have low tissue specificity, consistent with broadly expressed cellular machinery. HPA patterns point toward proliferative or progenitor-like cell states, with recurring enrichment in bone marrow, lymphoid tissue, erythrocyte progenitors, megakaryocyte progenitors, monocyte progenitors, neutrophil progenitors, and trophoblast populations. LPCAT2 is immune-cell enhanced, whereas most genes have low immune-cell specificity. All module proteins were detected in rectum, while there was no matching HPA tissue result for autonomic nervous system. The shared module could consequently reflect common proliferating, progenitor-like, or stromal-associated cellular components in the sampled tissues rather than a tissue-specific autonomic–rectal program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a strong established relationship between MCM2 and MCM4 and a further relationship between NSUN2 and PUS1. These links provide direct biological anchors but leave most module edges without an established STRING counterpart. hu.MAP repeatedly places MCM2 and MCM4 together in replication-associated complexes, including complexes containing other MCM proteins, GINS components, replication-fork factors, and chromatin or DNA-repair proteins (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1). The repeated MCM2–MCM4 membership is consistent with genuine replication machinery, but the fact that the complexes contain many genes outside the module means the module captures only a fragment of those complexes. The remaining co-abundance relationships are therefore not independently validated as physical interactions by the supplied STRING or hu.MAP evidence.

**STRING interactions (score >= 0.7)**: 2 of 66 gene pairs: MCM2–MCM4 (0.999); NSUN2–PUS1 (0.766)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09860.1 (MCM4, MCM2; 2/4); huMAP3_00154.1 (MCM4, MCM2; 2/5); huMAP3_06061.1 (MCM4, MCM2; 2/5); huMAP3_05529.1 (MCM4, MCM2; 2/6); huMAP3_07113.1 (MCM4, MCM2; 2/6); huMAP3_14758.1 (MCM4, MCM2; 2/14); huMAP3_08554.1 (MCM4, MCM2; 2/15); huMAP3_11832.1 (MCM4, MCM2; 2/15); huMAP3_12180.1 (MCM4, MCM2; 2/17); huMAP3_09466.1 (MCM4, MCM2; 2/23); huMAP3_10862.1 (MCM4, MCM2; 2/33); huMAP3_14306.1 (MCM4, MCM2; 2/55)

### Novelty

The module as a whole may be a new co-abundance observation, but novelty is not established merely because most module pairs are absent from STRING or hu.MAP. The MCM2–MCM4 relationship and their shared replication-complex membership are already well supported, and the NSUN2–PUS1 relationship is also represented in STRING. A potentially novel aspect is the co-abundance combination of replication, RNA-modification, proliferation, membrane-lipid, and STAT1-associated signals across autonomic nervous system and rectum. That interpretation remains provisional because there is no globally significant GO or KEGG enrichment, no STRING functional enrichment, and no evidence here that the module is a previously unreported tissue-pair-specific biological mechanism. Direct replication in independent cohorts, cell-type deconvolution, and perturbation would be needed to claim a new mechanism.

**Hypothesis.** Hypothesis: the conserved module reflects a shared proliferative or progenitor-like cellular state present in both tissue groups, in which DNA-replication capacity is coordinated with RNA maturation, membrane remodeling, and cytokine-responsive regulation. MCM2 and MCM4 may mark replication competence; NSUN2, PUS1, and EMG1 may support the RNA-processing demands of active or differentiating cells; LPCAT2 may connect that state to membrane and inflammatory lipid metabolism; and STAT1 may reflect cytokine exposure or an interferon-related regulatory context. This is a hypothesis about coordinated cellular state, not evidence that these proteins form one physical complex or that autonomic and rectal tissues share an identical cell type.

### Important genes

#### MCM2

- **Related proteins** (co-abundance neighbors): NSUN2 (0.87), TM9SF4 (0.87), EMG1 (0.82), DDOST (0.81); STRING partners: MCM4 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_09860.1, huMAP3_00154.1, huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is among the strongest network-connected genes and is linked directly to MCM4 in STRING. It participates in the conserved MCM replication machinery and appears in every listed hu.MAP complex containing module members (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1). Its HPA profile is enhanced in bone marrow and lymphoid tissue and in several progenitor or differentiating cell types. It also has extensive literature and disease annotation, making it the strongest established anchor for a replication or proliferative interpretation.
- **Conclusion**: Established evidence supports MCM2 as a replication-initiation and replication-fork factor and as the principal bridge to the MCM complexes represented in this module. Its co-abundance here plausibly marks proliferative or progenitor-like cells. It does not by itself establish that replication is the sole function of the module.

#### MCM4

- **Related proteins** (co-abundance neighbors): TM9SF4 (0.89), STAT1 (0.83); STRING partners: MCM2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_09860.1, huMAP3_00154.1, huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 4. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication rel…
- **Diseases (Open Targets)**: primary immunodeficiency with natural-killer cell deficiency and adrenal insufficiency (0.714); X-linked adrenal hypoplasia congenita (0.185); lung adenocarcinoma (0.112); microcephaly (0.111); neoplasm (0.102)
- **Europe PMC papers**: 4082
- **Why important**: MCM4 is the module partner most directly corroborated by external interaction and complex evidence: it has a STRING relationship with MCM2 and co-occurs with MCM2 across the hu.MAP complexes (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1). Its annotations directly support DNA replication initiation, DNA metabolic activity, strand elongation, and break-induced replication. Its HPA pattern is enhanced in bone marrow and several germline or progenitor populations, and it has substantial literature and disease coverage.
- **Conclusion**: Established evidence identifies MCM4 as a component of the MCM replication machinery. Together with MCM2, it gives the module a credible replication-related core. The broader links from MCM4 to STAT1 and TM9SF4 are co-abundance relationships here and should not be interpreted as proven physical interactions.

#### NSUN2

- **Related proteins** (co-abundance neighbors): TM9SF4 (0.89), MCM2 (0.87), PUS1 (0.82); STRING partners: PUS1 (0.766)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP2/Sun RNA methyltransferase 2. This gene encodes a methyltransferase that catalyzes the methylation of cytosine to 5-methylcytosine (m5C) at position 34 of intron-containing tRNA(Leu)(CAA) precursors. This modification is necessary to stabilize the anticodon-codon pairing and correctly translate the mRNA. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Mar…
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.694); hereditary disease (0.518); Intellectual disability (0.489); phenylketonuria (0.470); neurodegenerative disease (0.462)
- **Europe PMC papers**: 2458
- **Why important**: NSUN2 occupies a relatively central position in the co-abundance subgraph and connects to PUS1, MCM2, and TM9SF4. It is an RNA methyltransferase involved in tRNA modification, rRNA processing, mRNA processing, and RNA export. Its STRING relationship with PUS1 supplies an independent connection between two RNA-modification factors. NSUN2 also has extensive literature and disease associations involving intellectual disability and neurodegenerative disease.
- **Conclusion**: Established evidence supports NSUN2 as an RNA-modification and RNA-processing enzyme, and the NSUN2–PUS1 relationship is independently represented in STRING. Its presence may indicate RNA-processing demands in the shared cellular state. A direct functional coupling between NSUN2 and the MCM or STAT1 signals remains a hypothesis.

#### PUS1

- **Related proteins** (co-abundance neighbors): NSUN2 (0.82), STAT1 (0.81), TPD52L2 (0.81); STRING partners: NSUN2 (0.766)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pseudouridine synthase 1. This gene encodes a pseudouridine synthase that converts uridine to pseudouridine once it has been incorporated into an RNA molecule. The encoded enzyme may play an essential role in tRNA function and in stabilizing the secondary and tertiary structure of many RNAs. A mutation in this gene has been linked to mitochondrial myopathy and sideroblastic anemia. Alternate splicing results in multiple tr…
- **Diseases (Open Targets)**: myopathy, lactic acidosis, and sideroblastic anemia (0.819); mitochondrial disease (0.400); Intellectual disability (0.370); sulfite oxidase deficiency due to molybdenum cofactor deficiency type B1 (0.340); hereditary disease (0.193)
- **Europe PMC papers**: 993
- **Why important**: PUS1 connects the NSUN2 RNA-modification signal to STAT1 and TPD52L2 in the module and is supported by a STRING relationship with NSUN2. It catalyzes pseudouridine formation in tRNA and other RNA classes and has mitochondrial as well as nuclear localization. Its disease associations with mitochondrial myopathy, lactic acidosis, and sideroblastic anemia make it biologically important beyond being a network connector.
- **Conclusion**: Established evidence supports PUS1 as an RNA pseudouridine synthase with roles in RNA stability and mitochondrial function. Its pairing with NSUN2 provides a plausible RNA-processing submodule. The proposed coordination of RNA modification with replication or cytokine signaling is not directly demonstrated by the supplied evidence.

#### STAT1

- **Related proteins** (co-abundance neighbors): MCM4 (0.83), TM9SF4 (0.82), PUS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal transducer and activator of transcription 1. The protein encoded by this gene is a member of the STAT protein family. In response to cytokines and growth factors, STAT family members are phosphorylated by the receptor associated kinases, and then form homo- or heterodimers that translocate to the cell nucleus where they act as transcription activators. The protein encoded by this gene can be activated by various ligands including interferon-…
- **Diseases (Open Targets)**: immunodeficiency 31B (0.786); chronic mucocutaneous candidiasis (0.775); autoimmune enteropathy and endocrinopathy - susceptibility to chronic infections syndrome (0.772); cancer (0.554); immunodeficiency disease (0.482)
- **Europe PMC papers**: 66602
- **Why important**: STAT1 is a network connector linking MCM4, TM9SF4, and PUS1. It is a cytokine- and growth-factor-responsive transcription factor that mediates antiviral and defense-related transcriptional responses. It has very extensive literature and strong disease associations involving immunodeficiency, chronic infection susceptibility, and autoimmune enteropathy. Its rectal detection and connection to genes involved in proliferation and cellular processing make it informative for interpreting the tissue-shared state.
- **Conclusion**: Established evidence supports STAT1 as a central cytokine-responsive transcriptional regulator with important immune and antiviral functions. Its module position is consistent with a regulatory or environmental-response component. It is not evidence that the whole module is an immune module, especially because most genes have low immune-cell specificity and no enrichment term passed global correction.

#### LPCAT2

- **Related proteins** (co-abundance neighbors): TPD52L2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lysophosphatidylcholine acyltransferase 2. This gene encodes a member of the lysophospholipid acyltransferase family. The encoded enzyme may function in two ways: to catalyze the biosynthesis of platelet-activating factor (1-O-alkyl-2-acetyl-sn-glycero-3-phosphocholine) from 1-O-alkyl-sn-glycero-3-phosphocholine, and to catalyze the synthesis of glycerophospholipid precursors from arachidonyl-CoA and lysophosphatidylcholine. The encoded pr…
- **Diseases (Open Targets)**: ocular hypotension (0.350); Torg-Winchester syndrome (0.333); multicentric osteolysis-nodulosis-arthropathy spectrum (0.333); liver disorder (0.212); alopecia areata (0.174)
- **Europe PMC papers**: 761
- **Why important**: LPCAT2 is linked to TPD52L2 and contributes a distinct membrane-lipid signal to an otherwise largely nuclear and nucleolar module. It participates in phospholipid remodeling and platelet-activating-factor biosynthesis. HPA describes enhancement in bone marrow and immune-associated cell types, including basophil and eosinophil populations, and its disease annotations include inflammatory and skeletal disorders.
- **Conclusion**: Established evidence supports LPCAT2 as a lipid-remodeling enzyme with inflammatory membrane functions. Its presence may indicate membrane or inflammatory-state biology within the module, or it may reflect a contributing cell population rather than a core pathway. A mechanistic connection between LPCAT2 and the MCM, RNA-modification, or STAT1 signals remains hypothetical.

## Module 8

**Tissue pair**: autonomic_nervous_system and rectum  
**Genes (5)**: HNRNPL, SERPINH1, SUPT16H, EFTUD2, WDR12

### Function

The module does not have a globally significant GO or KEGG enrichment term; no GO or KEGG term passed global correction. Its gene annotations nevertheless suggest a mixed nuclear gene-expression and proteostasis theme. EFTUD2 and HNRNPL are associated with spliceosomal assembly, RNA processing, and alternative splicing; SUPT16H supports chromatin remodeling and transcription elongation; WDR12 supports ribosome biogenesis; and SERPINH1 is an endoplasmic-reticulum collagen-specific chaperone involved in protein folding and collagen fibril organization. The module is therefore best interpreted as a co-abundance pattern linking RNA and chromatin processes with ribosome production and extracellular-matrix protein handling, rather than as evidence for one established pathway. These functional annotations are supportive interpretations, not globally significant enrichment results.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins, and it has low immune-cell specificity across all members. Only SERPINH1 has a secretome annotation, described as intracellular and membrane rather than simply secreted. All genes have low tissue specificity, while several show enhancement in distinct cell types, including glial, renal, stromal, adipocyte, cardiomyocyte, and erythrocyte-progenitor populations. This pattern does not support a straightforward blood-cell contamination explanation, but it does indicate that the shared module could reflect broadly distributed cellular programs or mixed cell composition. Rectal protein detection is present for most members, whereas autonomic-nervous-system protein data are unavailable in the supplied HPA summary; consequently, tissue-level protein concordance across both tissues cannot be assessed.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair reaches the supplied STRING interaction threshold, and STRING functional enrichment is absent. No hu.MAP complex contains at least two module members. Thus, the co-abundance edges are not corroborated here as known high-confidence physical interactions or as membership in a known multiprotein complex. The internal arrangement is still suggestive: EFTUD2 connects SERPINH1 and SUPT16H, while HNRNPL connects SUPT16H and WDR12. This topology may reflect coordinated expression or shared cellular-state regulation, but it should not be interpreted as a validated molecular pathway.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a tissue-pair-specific co-abundance observation, but it cannot be called a new biological discovery from these data alone. Its lack of STRING and hu.MAP support means that the observed gene combination and edges are not explained by the supplied reference interaction resources, yet database absence does not establish novelty. The absence of globally significant GO or KEGG enrichment, the small module size, the mixed functional annotations, and the broad tissue expression all argue for a cautious interpretation. Novelty would require replication in independent autonomic-nervous-system and rectal datasets, preservation of the module under alternative network constructions, and experimental or orthogonal molecular support.

**Hypothesis.** Hypothesis: the module reflects a coordinated cellular response in which transcriptional elongation, spliceosome-dependent RNA processing, ribosome biogenesis, and endoplasmic-reticulum protein folding become co-regulated across the autonomic nervous system and rectum. SERPINH1 could mark collagen-related secretory or matrix-handling activity, while EFTUD2, HNRNPL, SUPT16H, and WDR12 could represent the nuclear and ribosome-production capacity supporting that state. This is a mechanistic hypothesis, not an established pathway, and it should be tested by examining cell-type composition, transcript and protein concordance, collagen or matrix markers, and independent replication.

### Important genes

#### EFTUD2

- **Related proteins** (co-abundance neighbors): SERPINH1 (0.89), SUPT16H (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 has a central position in the supplied network, linking SERPINH1 with SUPT16H. It is a spliceosome component involved in snRNP assembly, spliceosome conformational change, and precursor-mRNA splicing. Its association with mandibulofacial dysostosis with microcephaly and its substantial literature support make it an informative anchor for the RNA-processing interpretation.
- **Conclusion**: Established evidence supports EFTUD2 as a spliceosome-related gene with developmental disease relevance. Its network connection to SERPINH1 does not establish a direct molecular interaction. A possible role as a coordinator of the module's RNA-processing component is therefore a hypothesis.

#### SUPT16H

- **Related proteins** (co-abundance neighbors): HNRNPL (0.88), EFTUD2 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SPT16 homolog, facilitates chromatin remodeling subunit. Transcription of protein-coding genes can be reconstituted on naked DNA with only the general transcription factors and RNA polymerase II. However, this minimal system cannot transcribe DNA packaged into chromatin, indicating that accessory factors may facilitate access to DNA. One such factor, FACT (facilitates chromatin transcription), interacts specifically with histones H2A/H2B to effect nucle…
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and thin corpus callosum (0.651); HIV infectious disease (0.584); Global developmental delay (0.372); Intellectual disability (0.372); Abnormal corpus callosum morphology (0.370)
- **Europe PMC papers**: 676
- **Why important**: SUPT16H is centrally positioned between HNRNPL and EFTUD2. It encodes a FACT-complex subunit involved in nucleosome assembly and disassembly, RNA polymerase II transcription, and transcription elongation-coupled chromatin remodeling. Its disease associations include neurodevelopmental and intellectual-disability-related conditions, and it has a substantial literature base.
- **Conclusion**: Established evidence supports SUPT16H as a chromatin-remodeling and transcription-elongation factor. Its position could make it a regulatory bridge between transcriptional state and RNA processing, but that bridging function within this module remains hypothetical.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): SUPT16H (0.88), WDR12 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL connects SUPT16H with WDR12 and has the largest literature volume among the module genes in the supplied sheet. It is a heterogeneous nuclear ribonucleoprotein involved in RNA processing, mRNA processing, alternative splicing, and transcriptional regulation. Its broad cell-type enhancement pattern is also relevant when considering cellular composition.
- **Conclusion**: Established evidence supports HNRNPL as a multifunctional nuclear RNA-binding and RNA-processing factor. It is a plausible expression-state hub in this small network, but the co-abundance data do not demonstrate that HNRNPL directly regulates the other module members.

#### SERPINH1

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family H member 1. This gene encodes a member of the serpin superfamily of serine proteinase inhibitors. The encoded protein is localized to the endoplasmic reticulum and plays a role in collagen biosynthesis as a collagen-specific molecular chaperone. Autoantibodies to the encoded protein have been found in patients with rheumatoid arthritis. Expression of this gene may be a marker for cancer, and nucleotide polymo…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 10 (0.714); preterm premature rupture of the membranes (0.559); coronary artery disorder (0.554); myocardial infarction (0.510); Abnormality of the skeletal system (0.474)
- **Europe PMC papers**: 2762
- **Why important**: SERPINH1 is the module's link to endoplasmic-reticulum proteostasis and collagen biology. It is a collagen-specific molecular chaperone involved in protein folding, unfolded-protein response, and collagen fibril organization. It is associated with osteogenesis imperfecta type ten and other skeletal, cardiovascular, and pregnancy-related conditions. Although it is peripheral in the network, it provides the clearest connection to extracellular-matrix handling and has substantial literature support.
- **Conclusion**: Established evidence supports SERPINH1 as an endoplasmic-reticulum collagen chaperone with disease relevance. Its co-abundance connection to EFTUD2 may reflect a shared cellular state or matrix-associated cell population; a direct functional connection between collagen handling and spliceosome activity is only a hypothesis.

#### WDR12

- **Related proteins** (co-abundance neighbors): HNRNPL (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 12. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); poisoning (0.233); non-autoimmune hemolytic anemia (0.214); coronary artery disorder (0.210); myocardial infarction (0.168)
- **Europe PMC papers**: 602
- **Why important**: WDR12 is a peripheral network member connected to HNRNPL and supplies the ribosome-biogenesis component of the interpretation. Its annotations include large-subunit rRNA maturation, rRNA processing, ribosome biogenesis, and cell-cycle regulation. Its disease associations include neurodegenerative disease, hemolytic anemia, and cardiovascular conditions, although its supplied literature volume is more modest than that of the leading RNA-processing genes.
- **Conclusion**: Established evidence supports WDR12 as a ribosome-biogenesis factor. Its presence may indicate coordinated biosynthetic capacity in the cell state represented by the module, but the data do not establish a specific role for WDR12 in the autonomic nervous system or rectum.
