# Conserved co-abundance modules: bone and testis

## Module 0

**Tissue pair**: bone and testis  
**Genes (5)**: AKR1B1, MAGEA4, MDH1, MAT2A, TWF1

### Function

No GO or KEGG term passed global correction, so the module has no statistically established pathway-level annotation. The gene set instead suggests a mixed program involving actin regulation through TWF1, cytosolic redox and intermediary metabolism through MDH1 and AKR1B1, methyl-donor production through MAT2A, and testis-associated transcriptional or germ-cell biology through MAGEA4. The co-abundance pattern is therefore more consistent with a shared cellular state or coordinated expression context than with a defined canonical pathway or protein complex. These functional interpretations are biologically plausible but remain provisional because the enrichment analysis was negative.

**Cell composition.** The module is not dominated by plasma or secreted proteins because no member is annotated as secreted. It is not blood-cell enriched: the members show low immune-cell specificity or are not detected in immune cells. Protein detection is reported for all module genes in testis, while matching HPA bone protein data are unavailable. The tissue pattern is heterogeneous, including testis, adrenal gland, heart muscle, tongue, and pancreas, and all members show some cell-type enhancement. This argues against a simple blood-contamination explanation. MDH1 and MAT2A have broadly relevant metabolic functions, but the module also contains tissue- and cell-type-associated genes, particularly MAGEA4 and AKR1B1.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and no STRING functional enrichment is available. No hu.MAP complex contains multiple module members. The co-abundance edges therefore should not be interpreted as established direct physical interactions. They may instead reflect coordinated regulation, shared cell composition, indirect metabolic relationships, or a common physiological state. The lack of STRING and hu.MAP support means that the module does not currently correspond to a known interaction complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared bone–testis co-abundance pattern appears under-characterized because the supplied resources provide no high-confidence STRING interactions, no multi-member hu.MAP complex, and no globally significant GO or KEGG enrichment. However, these absences do not prove that the module is a new biological discovery. The individual genes have established functions and disease or literature associations, and a tissue-context-specific correlation may not be represented in general interaction databases. The appropriate conclusion is potential novelty of the co-abundance association, not proven novelty of a molecular mechanism.

**Hypothesis.** Hypothesis: the module reflects a metabolically active, cytoskeleton-associated cellular state that is especially visible in testis and may recur in selected bone-associated cellular contexts. MDH1 could support cytosolic redox balancing and the malate–aspartate shuttle; AKR1B1 could contribute to aldehyde, carbohydrate, retinoid, prostaglandin, and steroid-related metabolism; MAT2A could provide methyl-donor capacity; TWF1 could connect the state to actin remodeling; and MAGEA4 could mark a testis-associated transcriptional or germ-cell component. This is a mechanistic hypothesis rather than an established pathway and requires validation with independent cohorts, cell-resolved measurements, and perturbation experiments.

### Important genes

#### TWF1

- **Related proteins** (co-abundance neighbors): MDH1 (0.84), AKR1B1 (0.82), MAT2A (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: twinfilin actin binding protein 1. This gene encodes twinfilin, an actin monomer-binding protein conserved from yeast to mammals. Studies of the mouse counterpart suggest that this protein may be an actin monomer-binding protein, and its localization to cortical G-actin-rich structures may be regulated by the small GTPase RAC1. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: liver disorder (0.109); complex regional pain syndrome (0.096); hepatocellular carcinoma (0.095); neoplasm (0.091); lung adenocarcinoma (0.091)
- **Europe PMC papers**: 612
- **Why important**: TWF1 is the most connected node in the module and links MDH1, AKR1B1, and MAT2A. Its established actin monomer-binding function, together with roles in actin filament depolymerization, filament capping, and lamellipodium regulation, gives the module a plausible cytoskeletal dimension. Its literature volume is lower than that of the major metabolic members, making its central network position particularly informative.
- **Conclusion**: Established evidence supports TWF1 as an actin-regulatory protein and a central co-abundance connector. It may link cellular morphology or motility to the module's metabolic state, but the co-abundance data do not establish direct biochemical coupling or causality.

#### MDH1

- **Related proteins** (co-abundance neighbors): AKR1B1 (0.84), TWF1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Centrosome, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: malate dehydrogenase 1. This gene encodes an enzyme that catalyzes the NAD/NADH-dependent, reversible oxidation of malate to oxaloacetate in many metabolic pathways, including the citric acid cycle. Two main isozymes are known to exist in eukaryotic cells: one is found in the mitochondrial matrix and the other in the cytoplasm. This gene encodes the cytosolic isozyme, which plays a key role in the malate-aspartate shuttl…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 88 (0.499); prostate carcinoma (0.455); neurodegenerative disease (0.348); asthma (0.320); Abnormality of the skeletal system (0.295)
- **Europe PMC papers**: 3198
- **Why important**: MDH1 is connected to TWF1 and AKR1B1 hu.MAP and provides the clearest metabolic anchor. Its cytosolic malate dehydrogenase activity and role in the malate–aspartate shuttle connect the module to redox balance, oxaloacetate metabolism, and intermediary metabolism. It has the largest literature volume among the module genes and disease associations involving neurological, cancer, respiratory, and skeletal-system phenotypes.
- **Conclusion**: Established evidence supports MDH1 as a cytosolic metabolic and redox enzyme. Its network position makes it a plausible metabolic anchor, but no globally corrected enrichment or physical interaction evidence shows that it drives the module.

#### MAT2A

- **Related proteins** (co-abundance neighbors): MAGEA4 (0.84), TWF1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionine adenosyltransferase 2A. The protein encoded by this gene catalyzes the production of S-adenosylmethionine (AdoMet) from methionine and ATP. AdoMet is the key methyl donor in cellular processes. [provided by RefSeq, Jun 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.545); familial thoracic aortic aneurysm and aortic dissection (0.416); autoimmune disorder of central nervous system (0.340); prostate carcinoma (0.252); Abnormality of the cardiovascular system (0.192)
- **Europe PMC papers**: 2615
- **Why important**: MAT2A connects MAGEA4 and TWF1 hu.MAP and produces S-adenosylmethionine, a key methyl donor. Its documented roles include S-adenosylmethionine biosynthesis, protein oligomerization, methionine response, and positive regulation of TORC1 signaling. Its tissue and cell-type annotations, together with substantial disease literature, make it a plausible bridge between metabolism, methylation capacity, and growth regulation.
- **Conclusion**: Established evidence supports MAT2A as a methyl-donor biosynthetic enzyme with links to cellular growth signaling. A role for methylation capacity in the testis-associated module is plausible, but it is not demonstrated by the co-abundance network.

#### AKR1B1

- **Related proteins** (co-abundance neighbors): MDH1 (0.84), TWF1 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldo-keto reductase family 1 member B. This gene encodes a member of the aldo/keto reductase superfamily, which consists of more than 40 known enzymes and proteins. This member catalyzes the reduction of a number of aldehydes, including the aldehyde form of glucose, and is thereby implicated in the development of diabetic complications by catalyzing the reduction of glucose to sorbitol. Multiple pseudogenes have been identified for thi…
- **Diseases (Open Targets)**: diabetic neuropathy (0.426); diabetes mellitus (0.406); neurodegenerative disease (0.370); diabetic cardiomyopathy (0.264); hypertensive disorder (0.179)
- **Europe PMC papers**: 2300
- **Why important**: AKR1B1 is connected to MDH1 and TWF1 hu.MAP and contributes carbohydrate, sorbitol, retinoid, prostaglandin, and C21-steroid-related metabolic functions. Its adrenal enrichment and enhancement in trophoblast and Hofbauer-cell populations suggest context-dependent metabolic activity. Its disease associations include diabetic neuropathy, diabetes mellitus, neurodegenerative disease, and diabetic cardiomyopathy.
- **Conclusion**: Established evidence supports AKR1B1 as an aldehyde and carbonyl reductase with broad metabolic effects. It may cooperate with MDH1 in a redox-sensitive cellular state, but that cooperation remains a hypothesis rather than a demonstrated interaction.

#### MAGEA4

- **Related proteins** (co-abundance neighbors): MAT2A (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Nuclear speckles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MAGE family member A4. This gene is a member of the MAGEA gene family. The members of this family encode proteins with 50 to 80% sequence identity to each other. The promoters and first exons of the MAGEA genes show considerable variability, suggesting that the existence of this gene family enables the same function to be expressed under different transcriptional controls. The MAGEA genes are clustered at chromosomal lo…
- **Diseases (Open Targets)**: synovial sarcoma (0.377); neoplasm (0.115); non-small cell lung carcinoma (0.095); melanoma (0.089); esophageal squamous cell carcinoma (0.085)
- **Europe PMC papers**: 841
- **Why important**: MAGEA4 is the testis-enriched terminal node connected to MAT2A. Its enhancement in differentiating spermatogonia and early primary spermatocytes, nuclear-speckle localization, and documented roles related to transcriptional repression, apoptosis regulation, and cell-cycle promotion make it the strongest tissue-context marker in the module. Its cancer-testis biology and disease associations add importance despite a smaller literature volume than the central metabolic genes.
- **Conclusion**: Established evidence supports MAGEA4 as a testis-associated MAGE-family protein related to transcription, apoptosis, and cell-cycle biology. It may identify the testis or germ-cell context in which the module is visible, but whether it mechanistically regulates the metabolic and cytoskeletal members is unknown.

## Module 1

**Tissue pair**: bone and testis  
**Genes (5)**: CAPZB, GMPPB, LANCL1, NUP160, TRAPPC6B

### Function

No GO/KEGG term passed global correction, so the module does not have a statistically established enriched pathway annotation. The individual gene annotations suggest a tentative convergence of intracellular membrane trafficking and glycoprotein biosynthesis, nucleocytoplasmic transport, and cytoskeletal regulation. TRAPPC6B supports ER-to-Golgi and vesicle transport, GMPPB supports GDP-mannose production and glycoprotein biosynthesis, NUP160 supports nuclear pore transport and RNA export, and CAPZB supports actin-filament regulation. LANCL1 adds possible links to peptide modification, carbohydrate metabolism, and cellular detoxification. These annotations support a broad cellular-maintenance interpretation, but not a single pathway-level conclusion.

**Cell composition.** The module is not dominated by secreted proteins and does not show blood-cell specificity in the HPA summary. Its members have low immune-cell specificity, arguing against a simple plasma or blood-cell signature. Most genes have low tissue specificity, while several show cell-type-enhanced expression across different epithelial, neural, glial, reproductive, and placental populations. Testis protein detection is present for most members, whereas comparable bone protein data are unavailable in the supplied HPA evidence. The shared bone-testis signal may therefore reflect broadly used intracellular functions, shared cellular states, or cell-composition effects rather than a bone-and-testis-specific secreted program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional-enrichment result is available, and no STRING interaction meets the supplied high-confidence criterion. No hu.MAP complex contains multiple module members. Consequently, the co-abundance links should not be interpreted as validated physical interactions or as membership in a known protein complex. The strongest observed links connect TRAPPC6B with LANCL1 and CAPZB, LANCL1 with GMPPB, and GMPPB with NUP160, but these are module co-abundance relationships whose molecular mechanism remains unconfirmed.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is not established as a new biological complex or pathway: the module has no supporting STRING interactions, no multi-member hu.MAP complex, and no globally significant GO/KEGG term. It may represent a previously unreported co-abundance pattern, particularly because the observed links are not represented by the supplied interaction or complex resources. However, absence from STRING or hu.MAP alone cannot prove novelty. A defensible novelty claim would require independent replication, comparison with published bone and testis co-expression resources, and experimental testing of the proposed relationships.

**Hypothesis.** Hypothesis: the module may reflect a shared intracellular maintenance program expressed in selected cells of bone and testis. In this model, TRAPPC6B could coordinate vesicle trafficking, GMPPB could support glycoprotein maturation through GDP-mannose supply, CAPZB could organize actin structures needed for cell architecture or transport, NUP160 could couple nuclear transport with gene-expression demands, and LANCL1 could contribute membrane-associated metabolic or peptide-modifying functions. The coordinated abundance of these proteins could arise from a common cell state or developmental program rather than direct protein-protein binding. This hypothesis is consistent with the annotations and HPA cell-type patterns but is not demonstrated by the supplied data.

### Important genes

#### TRAPPC6B

- **Related proteins** (co-abundance neighbors): LANCL1 (0.91), CAPZB (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: trafficking protein particle complex subunit 6B. TRAPPC6B is a component of TRAPP complexes, which are tethering complexes involved in vesicle transport (Kummel et al., 2005 [PubMed 16025134]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, epilepsy, and brain atrophy (0.755); hereditary disease (0.337); neurodegenerative disease (0.262); alcohol drinking (0.128); male reproductive organ cancer (0.113)
- **Europe PMC papers**: 178
- **Why important**: TRAPPC6B is among the most connected genes in the module and links LANCL1 with CAPZB. Its established role as a TRAPP-complex component in ER-to-Golgi and Golgi vesicle transport gives the module a plausible trafficking axis. It is detected in testis, has an endoplasmic-reticulum location, is associated with a neurodevelopmental disorder in Open Targets, and has a substantial literature base.
- **Conclusion**: Established evidence supports TRAPPC6B as a vesicle-trafficking component and as a central co-abundance connector. The hypothesis that it coordinates the other module members is plausible but unproven, especially because no corresponding STRING or hu.MAP relationship is present.

#### GMPPB

- **Related proteins** (co-abundance neighbors): NUP160 (0.84), LANCL1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GDP-mannose pyrophosphorylase B. This gene is thought to encode a GDP-mannose pyrophosphorylase. The encoded protein catalyzes the conversion of mannose-1-phosphate and GTP to GDP-mannose, a reaction involved in the production of N-linked oligosaccharides. Alternatively spliced transcript variants encoding distinct isoforms have been described. [provided by RefSeq, Jan 2009].
- **Diseases (Open Targets)**: autosomal recessive limb-girdle muscular dystrophy type 2T (0.833); muscular dystrophy-dystroglycanopathy (congenital with brain and eye anomalies), type A14 (0.800); muscular dystrophy-dystroglycanopathy (congenital with intellectual disability), type B14 (0.791); muscle-eye-brain disease (0.634); congenital muscular dystrophy with cerebellar involvement (0.619)
- **Europe PMC papers**: 773
- **Why important**: GMPPB connects LANCL1 with NUP160 and provides the clearest biochemical link to glycoprotein production through GDP-mannose synthesis. Its disease associations include limb-girdle muscular dystrophy and dystroglycanopathy, making it medically informative. It is detected in testis and shows cell-type enhancement in several epithelial, reproductive, placental, and plasma-cell populations.
- **Conclusion**: Established evidence supports GMPPB as a metabolic and glycoprotein-biosynthetic enzyme with important disease relevance. Its participation in a shared bone-testis intracellular program is a hypothesis derived from co-abundance, not a demonstrated tissue-specific mechanism.

#### NUP160

- **Related proteins** (co-abundance neighbors): GMPPB (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 160. NUP160 is 1 of up to 60 proteins that make up the 120-MD nuclear pore complex, which mediates nucleoplasmic transport.[supplied by OMIM, Apr 2004]
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.527); neurodegenerative disease (0.469); Alzheimer disease (0.429)
- **Europe PMC papers**: 812
- **Why important**: NUP160 is the endpoint of the GMPPB connection and represents the nuclear-transport arm of the module. As a nucleoporin, it is established in nucleocytoplasmic transport, RNA export, and related nuclear functions. Its HPA cell-type enhancement spans neural and glial populations, and its disease associations include infectious and neurodegenerative disease. It also has a strong literature presence relative to the module.
- **Conclusion**: Established evidence supports NUP160 as a nuclear-pore component required for transport and RNA handling. The module data support coordinated abundance with GMPPB, but do not establish a direct functional connection between nuclear transport and glycoprotein biosynthesis.

#### CAPZB

- **Related proteins** (co-abundance neighbors): TRAPPC6B (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: capping actin protein of muscle Z-line subunit beta. This gene encodes the beta subunit of the barbed-end actin binding protein, which belongs to the F-actin capping protein family. The capping protein is a heterodimeric actin capping protein that blocks actin filament assembly and disassembly at the fast growing (barbed) filament ends and functions in regulating actin filament dynamics as well as in stabilizing actin filament lengths in muscle and …
- **Diseases (Open Targets)**: neurodegenerative disease (0.525); hypothyroidism (0.454); nontoxic goiter (0.440); multinodular goiter (0.428); thyrotoxicosis (0.414)
- **Europe PMC papers**: 1148
- **Why important**: CAPZB is connected to TRAPPC6B and supplies an actin-cytoskeletal component to the module. Its established function is capping barbed ends of actin filaments and regulating filament dynamics in muscle and nonmuscle cells. It is enhanced in early and late spermatids and is detected in testis, making it especially relevant to the reproductive side of the tissue pair. It also has the largest literature footprint among the listed genes.
- **Conclusion**: Established evidence supports CAPZB as an actin-organization factor with relevance to spermatid cell biology. Its co-abundance with TRAPPC6B may indicate coordination of cytoskeletal structure with vesicle trafficking, but this remains a mechanistic hypothesis.

#### LANCL1

- **Related proteins** (co-abundance neighbors): TRAPPC6B (0.91), GMPPB (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Microtubules, Primary cilium, Basal body, End piece; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LanC like glutathione S-transferase 1. This gene encodes a loosely associated peripheral membrane protein related to the LanC family of bacterial membrane-associated proteins involved in the biosynthesis of antimicrobial peptides. This protein may play a role as a peptide-modifying enzyme component in eukaryotic cells. Previously considered a member of the G-protein-coupled receptor superfamily, this protein is now in the LanC family. …
- **Diseases (Open Targets)**: Pain (0.248); Abnormality of the skeletal system (0.243); contracture (0.206); placental abruption (0.206); coronary artery disorder (0.139)
- **Europe PMC papers**: 364
- **Why important**: LANCL1 is a central connector between TRAPPC6B and GMPPB. Its annotations include carbohydrate metabolism, peptide modification, G-protein-coupled receptor signaling, and cellular detoxification. It has brain tissue enhancement, cell-type enhancement in oligodendrocytes and pituitary-related cells, testis detection, disease associations involving the skeletal system and pain, and a substantial literature base.
- **Conclusion**: Established evidence supports LANCL1 as a LanC-like peripheral membrane protein with diverse metabolic and signaling annotations. Its precise role in this module is less defined than those of the trafficking, glycosylation, nuclear-pore, and actin proteins; any role as a bridge between these processes is therefore a hypothesis.

## Module 2

**Tissue pair**: bone and testis  
**Genes (7)**: DDX39B, HNRNPF, LSM6, SNRPA1, SCO1, THY1, SLC25A1

### Function

The strongest interpretation is a conserved nuclear RNA-processing and pre-mRNA-splicing module. The primary global enrichment is the spliceosomal complex (GO:CC spliceosomal complex; q_global = 0.0129), driven by DDX39B, HNRNPF, LSM6, and SNRPA1. The independent STRING annotations support the same interpretation through spliceosome, snRNP, U-six snRNP, ribonucleoprotein, RNA-binding, and major mRNA-splicing terms (10 supplementary STRING terms; within-query FDR 0.0014–0.0448). SNRPA1 is a U2 spliceosomal component, DDX39B is an RNA helicase required for U2 snRNP association and RNA export, HNRNPF regulates RNA processing and alternative splicing, and LSM6 participates in spliceosomal tri-snRNP assembly and RNA turnover. SCO1 and SLC25A1 suggest a possible mitochondrial respiration and citrate-transport connection, while THY1 may reflect cell adhesion or cellular identity rather than the core molecular function. Thus, the module is best viewed as a spliceosome-centered RNA maturation module with possible links to mitochondrial metabolic state and cell composition.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and the module has low immune-cell specificity overall, with only SLC25A1 showing immune-cell enhancement in eosinophils. The HPA data therefore do not strongly support a blood-contamination explanation. Several genes show cell-type enhancement, especially in extravillous trophoblasts, while spliceosomal genes also show testis-related or germ-cell-associated patterns. Testis protein detection is reported for most of the tested genes, whereas matched bone protein evidence is unavailable. THY1 is tissue-enhanced in brain, smooth muscle, and urinary bladder and is not detected in testis by the listed HPA evidence; SLC25A1 is tissue-enhanced in liver. These observations indicate that the shared bone-testis signal may reflect broadly distributed nuclear machinery combined with shared or correlated cell states, rather than a bone-and-testis-specific secreted program.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC spliceosomal complex | 0.0129 | DDX39B, HNRNPF, LSM6, SNRPA1 |

### STRING and hu.MAP

The network contains two high-confidence STRING relationships: the very strong LSM6-SNRPA1 connection and the DDX39B-HNRNPF connection (hu.MAP huMAP3_08980.1). These relationships are biologically coherent with the spliceosomal interpretation, but most module gene pairs are not supported by high-confidence STRING links. hu.MAP identifies SNRPA1 and LSM6 in the same large spliceosome and snRNP-related complex (hu.MAP huMAP3_08980.1). The complex contains many additional canonical splicing factors, so the hu.MAP result supports membership in a known molecular machinery rather than a module-specific interaction architecture. The sparse direct STRING connectivity means the co-abundance pattern extends beyond only previously catalogued physical interactions and may also capture coordinated regulation, shared cell states, or indirect functional coupling.

**STRING interactions (score >= 0.7)**: 2 of 21 gene pairs: DDX39B–HNRNPF (0.736); LSM6–SNRPA1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Spliceosome (FDR = 0.0014, 4 genes); COMPARTMENTS Spliceosomal complex (FDR = 0.004, 4 genes); Component Spliceosomal complex (FDR = 0.0069, 4 genes); Component Spliceosomal snRNP complex (FDR = 0.0248, 3 genes); COMPARTMENTS Spliceosomal snRNP complex (FDR = 0.0253, 3 genes); RCTM mRNA Splicing - Major Pathway (FDR = 0.0274, 4 genes); COMPARTMENTS U6 snRNP (FDR = 0.0331, 2 genes); Keyword Ribonucleoprotein (FDR = 0.0349, 3 genes); Component U6 snRNP (FDR = 0.0389, 2 genes); Keyword RNA-binding (FDR = 0.0448, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (SNRPA1, LSM6; 2/97)

### Novelty

The exact seven-gene co-abundance module appears potentially novel as a bone-testis conserved module, because the supplied evidence does not identify a prior report of this precise gene combination or tissue-pair module. However, its central biology is not novel: the spliceosomal roles of DDX39B, HNRNPF, LSM6, and SNRPA1 are established, and some relationships are already represented in STRING and hu.MAP. The absence of a complete match in those resources would not by itself establish novelty. A web search returned established gene and spermatogonial literature, including DDX39B RNA-processing information and THY1-associated human spermatogonial studies, but did not identify this exact co-abundance module. The defensible conclusion is novelty of the observed cross-tissue co-abundance arrangement, not discovery of a new spliceosome or a new molecular function.

**Hypothesis.** Hypothesis: coordinated abundance of a spliceosome-centered machinery in bone and testis supports efficient pre-mRNA processing in cells with substantial differentiation or specialized transcriptional demands. DDX39B and HNRNPF may organize or regulate RNA-processing and export, while SNRPA1 and LSM6 provide snRNP and spliceosomal structural support. SCO1 and SLC25A1 may connect this RNA-processing state to mitochondrial copper handling, respiratory-complex assembly, and citrate transport, potentially coupling transcript maturation to metabolic demand. THY1 may mark a correlated cellular or adhesion state rather than directly participate in the spliceosome. This model is mechanistic but unproven by the co-abundance data and requires validation by cell-resolved expression, perturbation, and protein-interaction experiments in bone- and testis-relevant cell types.

Web sources: https://en.wikipedia.org/wiki/DDX39B; https://en.wikipedia.org/wiki/SCO1; https://www.ncbi.nlm.nih.gov/gene?cmd=Retrieve&list_uids=6627; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9023810/

### Important genes

#### DDX39B

- **Related proteins** (co-abundance neighbors): SNRPA1 (0.85), HNRNPF (0.82); STRING partners: HNRNPF (0.736)
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nuclear speckles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 39B. This gene encodes a member of the DEAD box family of RNA-dependent ATPases that mediate ATP hydrolysis during pre-mRNA splicing. The encoded protein is an essential splicing factor required for association of U2 small nuclear ribonucleoprotein with pre-mRNA, and it also plays an important role in mRNA export from the nucleus to the cytoplasm. This gene belongs to a cluster of genes localized in th…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); Alzheimer disease (0.522); Parkinson disease (0.503); lysosomal storage disease (0.503); neurodevelopmental disorder (0.413)
- **Europe PMC papers**: 1037
- **Why important**: DDX39B is a central network connector, linking SNRPA1 and HNRNPF, and it is one of the genes in the globally significant spliceosomal-complex term (GO:CC spliceosomal complex; q_global = 0.0129). It appears across the spliceosome, snRNP, U-six snRNP, RNA-binding, and mRNA-splicing STRING annotations (10 supplementary STRING terms; within-query FDR 0.0014–0.0448). Its established function as an ATP-dependent RNA helicase required for U2 snRNP association, pre-mRNA splicing, and nuclear RNA export gives it a plausible organizing role. Its disease literature is substantial, including neurodegenerative and neurodevelopmental associations in the supplied Open Targets evidence, and the web search also returned structural studies of its RNA-processing complexes.
- **Conclusion**: Established evidence supports DDX39B as a core RNA-splicing and RNA-export component and as a strong functional anchor of this module. It is a plausible coordinator of the module, but the co-abundance data do not establish that it drives the shared bone-testis signal.

#### SNRPA1

- **Related proteins** (co-abundance neighbors): DDX39B (0.85), SCO1 (0.82); STRING partners: LSM6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein polypeptide A'. Enables RNA binding activity. Involved in mRNA splicing, via spliceosome and spermatogenesis. Located in nuclear speck. Part of U2-type catalytic step 2 spliceosome and U2-type precatalytic spliceosome. Implicated in connective tissue disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.538); dengue disease (0.370); phosphorus metabolism disease (0.196); hypotensive disorder (0.196); cancer (0.087)
- **Europe PMC papers**: 520
- **Why important**: SNRPA1 is a network connector between DDX39B and SCO1, belongs to the globally significant spliceosomal-complex overlap (GO:CC spliceosomal complex; q_global = 0.0129), and has extensive STRING functional support for spliceosome, snRNP, RNA-binding, and mRNA-splicing biology (6 supplementary STRING terms; within-query FDR 0.0014–0.0274) and (STRING Keyword Ribonucleoprotein; within-query FDR = 0.0349) (STRING Component U6 snRNP; within-query FDR = 0.0389) (STRING Keyword RNA-binding; within-query FDR = 0.0448). It is also directly paired with LSM6 by a very strong STRING relationship and shares a hu.MAP complex with LSM6 (hu.MAP huMAP3_08980.1). Its established roles include U2-type spliceosome assembly, RNA splicing, and spermatogenesis, making it especially relevant to the testis component.
- **Conclusion**: Established evidence supports SNRPA1 as a core spliceosomal and spermatogenesis-relevant gene in the module. Its connection to SCO1 is a network observation, not evidence that SNRPA1 regulates mitochondrial function.

#### LSM6

- **Related proteins** (co-abundance neighbors): THY1 (0.82); STRING partners: SNRPA1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: LSM6 homolog, U6 small nuclear RNA and mRNA degradation associated. Sm-like proteins were identified in a variety of organisms based on sequence homology with the Sm protein family (see SNRPD2; MIM 601061). Sm-like proteins contain the Sm sequence motif, which consists of 2 regions separated by a linker of variable length that folds as a loop. The Sm-like proteins are thought to form a stable heteromer present in tri-snRNP particles, which are important for pre-mR…
- **Diseases (Open Targets)**: neurodegenerative disease (0.560); Alzheimer disease (0.527); lysosomal storage disease (0.526); Parkinson disease (0.526); attention deficit-hyperactivity disorder (0.373)
- **Europe PMC papers**: 414
- **Why important**: LSM6 is part of the globally significant spliceosomal-complex overlap (GO:CC spliceosomal complex; q_global = 0.0129), has broad STRING support for spliceosomal, snRNP, U-six snRNP, RNA-binding, and RNA-catabolic biology (10 supplementary STRING terms; within-query FDR 0.0014–0.0448), and forms the strongest listed STRING pair with SNRPA1. It also shares the hu.MAP spliceosome-related complex with SNRPA1 (hu.MAP huMAP3_08980.1). Its known participation in tri-snRNP assembly, snRNP assembly, mRNA splicing, and nuclear mRNA decay makes it a strong structural and functional representative of the module core.
- **Conclusion**: Established evidence supports LSM6 as a core spliceosome and RNA-turnover component. Its HPA cell-type enhancement in differentiating spermatogonia is compatible with testis relevance, but does not prove that the module is specific to germ cells.

#### HNRNPF

- **Related proteins** (co-abundance neighbors): THY1 (0.82), DDX39B (0.82); STRING partners: DDX39B (0.736)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein F. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins that complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and regulate alternative splicing, polyadenylation, and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present…
- **Diseases (Open Targets)**: neurodegenerative disease (0.518); dengue disease (0.370); knee fracture (0.322); breast cancer (0.103); posterior cortical atrophy (0.083)
- **Europe PMC papers**: 971
- **Why important**: HNRNPF is a connector linking DDX39B and THY1 and is one of the four genes in the globally significant spliceosomal-complex overlap (GO:CC spliceosomal complex; q_global = 0.0129). It has STRING support for spliceosome, ribonucleoprotein, RNA-binding, and mRNA-splicing functions (STRING Keyword Spliceosome; within-query FDR = 0.0014) (STRING COMPARTMENTS Spliceosomal complex; within-query FDR = 0.004) (STRING Component Spliceosomal complex; within-query FDR = 0.0069), (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0274), and (STRING Keyword Ribonucleoprotein; within-query FDR = 0.0349) (STRING Component U6 snRNP; within-query FDR = 0.0389) (STRING Keyword RNA-binding; within-query FDR = 0.0448). Its established role in pre-mRNA binding, alternative splicing, polyadenylation, RNA processing, and RNA transport provides a regulatory complement to the structural snRNP genes. It also has substantial literature and disease-association evidence in the supplied records.
- **Conclusion**: Established evidence supports HNRNPF as a broadly expressed RNA-processing regulator and a core functional member of the module. Its link to THY1 may represent coordinated cell-state biology or indirect co-abundance rather than a known physical interaction.

#### SCO1

- **Related proteins** (co-abundance neighbors): SLC25A1 (0.86), SNRPA1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: synthesis of cytochrome C oxidase 1. Mammalian cytochrome c oxidase (COX) catalyzes the transfer of reducing equivalents from cytochrome c to molecular oxygen and pumps protons across the inner mitochondrial membrane. In yeast, 2 related COX assembly genes, SCO1 and SCO2 (synthesis of cytochrome c oxidase), enable subunits 1 and 2 to be incorporated into the holoprotein. This gene is the human homolog to the yeast SCO1 gene. [provide…
- **Diseases (Open Targets)**: mitochondrial complex IV deficiency, nuclear type 4 (0.782); leigh syndrome due to mitochondrial complex iv deficiency (0.583); mitochondrial complex IV deficiency, nuclear-type (0.543); neurodegenerative disease (0.484); mitochondrial disease (0.372)
- **Europe PMC papers**: 1293
- **Why important**: SCO1 has the highest listed network connectivity and links the spliceosome-associated SNRPA1 branch to SLC25A1, creating a possible metabolic edge of the module. Its established function is mitochondrial copper homeostasis and assembly of respiratory-chain complex IV. The supplied disease evidence links SCO1 to mitochondrial complex IV deficiency, Leigh syndrome, and mitochondrial disease, and its literature volume is substantial. It is not part of the primary GO term or STRING functional terms, so its importance comes from network position and biological complementarity rather than enrichment.
- **Conclusion**: Established evidence supports SCO1 as a mitochondrial respiratory-chain assembly factor that may mark a metabolic component of the module. Any coupling between SCO1 and spliceosomal activity in bone or testis remains a hypothesis generated by the network, not an established mechanism.

## Module 3

**Tissue pair**: bone and testis  
**Genes (5)**: KRT10, KRT9, KRT2, KRT1, KRT5

### Function

This is a coherent epithelial intermediate-filament and keratinization module. Every module gene contributes to the globally corrected keratin-filament and intermediate-filament terms (4 globally significant GO/KEGG terms, q_global 4.36e-08–4.92e-07; see the table), and the module also supports epidermal structural function, skin and epidermis development, epithelial differentiation, cornified-envelope formation, and cadherin-associated biology (11 globally significant GO/KEGG terms, q_global 1.11e-06–0.000869; see the table). The structural-molecule and supramolecular-fiber terms (7 globally significant GO/KEGG terms, q_global 0.00501–0.021; see the table) reinforce the interpretation that the genes encode a coordinated cytoskeletal program rather than unrelated tissue markers. The strongest interpretation is a keratin filament program spanning basal and suprabasal epithelial differentiation, with KRT5 representing a basal component and KRT1, KRT2, KRT10, and KRT9 representing more differentiated keratin states. The KEGG cornified-envelope and cadherin-signaling terms (KEGG Cornified envelope formation - Homo sapiens (human); q_global = 1.2e-05) and (KEGG Cadherin signaling - Homo sapiens (human); q_global = 0.000124) are consistent with epithelial barrier architecture and cell-cell adhesion. These conclusions rely on globally corrected terms; the STRING annotations (8 supplementary STRING terms; within-query FDR 9.89e-09–1.37e-07) are concordant supplementary evidence.

**Cell composition.** The module is entirely composed of keratins, not plasma proteins. HPA assigns tissue enrichment to skin or related epithelial tissues for all module genes, with most associated with suprabasal keratinocytes and some with basal keratinocytes. KRT5 also shows enrichment across cervix, esophagus, skin, and vagina. Thus, the shared bone-testis signal is more plausibly an epithelial or keratinized-cell composition signal than a bone-and-testis-specific molecular program. HPA reports that the proteins were not detected in testis for every module gene, while there was no matching bone tissue result. This discrepancy is an important reason to treat the apparent cross-tissue conservation cautiously. KRT10 is annotated as secreted in other tissues, but the module is not predominantly secreted. HPA also reports immune-cell enhancement or enrichment for several genes, including signals involving memory or naive CD4 T cells and plasmacytoid dendritic cells; these do not outweigh the dominant epithelial pattern, but they leave open a sample-composition or contaminating-cell explanation.

**GO/KEGG enrichment**: 24 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC keratin filament | 4.36e-08 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament organization | 9.73e-08 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament-based process | 4.92e-07 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament cytoskeleton organization | 4.92e-07 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:MF structural constituent of skin epidermis | 1.11e-06 | KRT1, KRT10, KRT2, KRT5 |
| GO:CC intermediate filament | 2.89e-06 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:CC intermediate filament cytoskeleton | 6.23e-06 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| KEGG Cornified envelope formation - Homo sapiens (human) | 1.2e-05 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP skin development | 2.97e-05 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP epidermis development | 3.97e-05 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| KEGG Cadherin signaling - Homo sapiens (human) | 0.000124 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP keratinocyte differentiation | 0.00033 | KRT1, KRT10, KRT2, KRT5 |
| GO:BP keratinization | 0.000563 | KRT1, KRT2, KRT5 |
| GO:BP epidermal cell differentiation | 0.000765 | KRT1, KRT10, KRT2, KRT5 |
| GO:BP epithelial cell differentiation | 0.000869 | KRT1, KRT10, KRT2, KRT5, KRT9 |

### STRING and hu.MAP

STRING provides concordant support for a keratin-filament module (8 supplementary STRING terms; within-query FDR 9.89e-09–1.37e-07). The high-confidence network contains known relationships among KRT1, KRT10, KRT2, and KRT5, while KRT9 is a highly connected member of the module subgraph despite having no listed STRING partners in the gene-level summary. These relationships indicate that the co-abundance pattern largely recapitulates established keratin-family biology rather than revealing an unrelated interaction system. STRING also links the genes to cornified-envelope formation and epidermolytic hyperkeratosis (STRING RCTM Formation of the cornified envelope; within-query FDR = 1.07e-07) and (STRING DISEASES Epidermolytic hyperkeratosis; within-query FDR = 1.85e-06). No hu.MAP complex contains multiple module members. Therefore, the module has strong support as a coordinated functional family, but there is no hu.MAP evidence for a discrete multi-protein complex.

**STRING interactions (score >= 0.7)**: 6 of 10 gene pairs: KRT1–KRT10 (0.999); KRT1–KRT2 (0.956); KRT1–KRT5 (0.923); KRT10–KRT2 (0.904); KRT10–KRT5 (0.793); KRT2–KRT5 (0.871)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Keratin (FDR = 9.89e-09, 5 genes); Component Keratin filament (FDR = 2.03e-08, 5 genes); COMPARTMENTS Keratin filament (FDR = 2.08e-08, 5 genes); SMART Intermediate filament protein (FDR = 2.25e-08, 5 genes); Keyword Intermediate filament (FDR = 3.86e-08, 5 genes); RCTM Formation of the cornified envelope (FDR = 1.07e-07, 5 genes); InterPro Intermediate filament protein, conserved site (FDR = 1.37e-07, 5 genes); InterPro Intermediate filament, rod domain (FDR = 1.37e-07, 5 genes); DISEASES Epidermolytic hyperkeratosis (FDR = 1.85e-06, 4 genes); PMID (2025) Mass spectrometric detection of keratins in tear fluid. (FDR = 3.45e-06, 5 genes); PMID (2023) Key Factors in the Complex and Coordinated Network of Skin Keratinization: Their Significance and Involvement in Common Skin Conditions. (FDR = 3.45e-06, 5 genes); PMID (2022) A metatranscriptomic approach to explore longitudinal tissue specimens from non-healing diabetes related foot ulcers. (FDR = 3.45e-06, 5 genes); PMID (2022) Palmoplantar Keratoderma: A Molecular Genetic Analysis of Family Cases. (FDR = 3.45e-06, 5 genes); PMID (2021) Keratin Biomaterials in Skin Wound Healing, an Old Player in Modern Medicine: A Mini Review. (FDR = 3.45e-06, 5 genes); PMID (2019) Keratin 9 L164P mutation in a Chinese pedigree with epidermolytic palmoplantar keratoderma, cytokeratin analysis, and literature review. (FDR = 3.45e-06, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The biological function itself is not a new finding: keratin filament assembly, epidermal differentiation, cornification, and related skin disease associations are already well established in the globally corrected enrichment results (24 globally significant GO/KEGG terms, q_global 4.36e-08–0.021; see the table), STRING evidence (15 supplementary STRING terms; within-query FDR 9.89e-09–3.45e-06), gene annotations, and the substantial literature associated with these keratins. The cross-tissue co-abundance observation in bone and testis may be a new dataset-specific pattern, but the fact sheet does not provide a matched prior-module analysis or literature comparison that would establish this. Absence of a hu.MAP complex is not evidence of novelty, and the presence of known STRING relationships argues against calling the molecular mechanism novel. The defensible conclusion is that this may be a novel observation of shared abundance or sample composition, but it is not a demonstrated novel keratin mechanism.

**Hypothesis.** Hypothesis: the apparent conserved bone-testis module is generated primarily by shared epithelial or keratinized-cell content, technical carryover, or tissue-adjacent epithelial material rather than by a bone-testis-specific pathway. Within such cells, KRT5 may represent a basal epithelial scaffold, while KRT1, KRT2, KRT10, and KRT9 represent differentiated keratin filament states. Their coordinated abundance could therefore reflect epithelial maturation, mechanical-barrier formation, and cornified-envelope organization. The absence of HPA protein detection in testis for all module genes makes this composition-based explanation more plausible than direct testis expression, but it remains a hypothesis requiring cell-resolved expression, histological localization, and independent validation in bone and testis samples.

### Important genes

#### KRT1

- **Related proteins** (co-abundance neighbors): KRT2 (0.96), KRT10 (0.94), KRT9 (0.93); STRING partners: KRT10 (0.999), KRT2 (0.956), KRT5 (0.923)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 is a highly connected central member of the module and is linked in STRING to KRT10, KRT2, and KRT5. It contributes to every globally corrected enrichment term (24 globally significant GO/KEGG terms, q_global 4.36e-08–0.021; see the table), is tissue-enriched in skin, and is enriched in suprabasal keratinocytes. Its annotation places it in differentiated stratified-epithelial cytoskeletal structure, while its disease associations include epidermolytic ichthyosis and palmoplantar keratoderma. Its very large literature base makes it the best-established anchor for interpreting the module.
- **Conclusion**: Established evidence supports KRT1 as a core differentiated-epithelial intermediate-filament component and a major interpretive anchor. Its network position supports module centrality, but the data do not show that KRT1 specifically drives the cross-tissue association.

#### KRT10

- **Related proteins** (co-abundance neighbors): KRT1 (0.94), KRT9 (0.92), KRT2 (0.91); STRING partners: KRT1 (0.999), KRT2 (0.904), KRT5 (0.793)
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 10. This gene encodes a member of the type I (acidic) cytokeratin family, which belongs to the superfamily of intermediate filament (IF) proteins. Keratins are heteropolymeric structural proteins which form the intermediate filament. These filaments, along with actin microfilaments and microtubules, compose the cytoskeleton of epithelial cells. Mutations in this gene are associated with epidermolytic …
- **Diseases (Open Targets)**: epidermolytic hyperkeratosis 2A, autosomal dominant (0.787); epidermolytic ichthyosis (0.772); congenital reticular ichthyosiform erythroderma (0.727); ichthyosis, annular epidermolytic 1 (0.647); annular epidermolytic ichthyosis (0.642)
- **Europe PMC papers**: 2736
- **Why important**: KRT10 is a highly connected STRING-supported partner of KRT1, KRT2, and KRT5 and participates in nearly all globally corrected module terms (4 globally significant GO/KEGG terms, q_global 4.36e-08–4.92e-07; see the table) and (19 globally significant GO/KEGG terms, q_global 2.89e-06–0.021; see the table). It is skin-enriched and associated with suprabasal keratinocytes. Its annotation identifies it as a type I intermediate-filament protein involved in keratinocyte differentiation, cornification, and epithelial development. Its disease associations include epidermolytic hyperkeratosis and several ichthyosis phenotypes, and it has a substantial literature base.
- **Conclusion**: Established evidence supports KRT10 as a differentiated suprabasal keratin that helps explain the cornification and epithelial-differentiation signal. Its HPA annotation of secretion in other tissues should not be interpreted as evidence that this module is a secreted-protein module.

#### KRT2

- **Related proteins** (co-abundance neighbors): KRT1 (0.96), KRT9 (0.94), KRT10 (0.91); STRING partners: KRT1 (0.956), KRT10 (0.904), KRT5 (0.871)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location Intermediate filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 2. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is expressed largely in the upper spinous layer of epidermal keratinocytes and mutations in this gene …
- **Diseases (Open Targets)**: superficial epidermolytic ichthyosis (0.815); exfoliative ichthyosis (0.358); Palmoplantar hyperkeratosis (0.267); hereditary disease (0.193); Vertigo (0.145)
- **Europe PMC papers**: 7459
- **Why important**: KRT2 is a highly connected module member with strong STRING relationships to KRT1, KRT10, and KRT5. It appears in the full set of globally corrected terms (24 globally significant GO/KEGG terms, q_global 4.36e-08–0.021; see the table), is skin-enriched, and is enriched in suprabasal keratinocytes. Its annotation supports roles in the upper spinous epidermis, keratinization, keratinocyte activation, and epidermal development. Its disease associations include superficial epidermolytic ichthyosis and other keratinization disorders, and it has a substantial literature base.
- **Conclusion**: Established evidence supports KRT2 as a differentiated suprabasal structural keratin and a strong contributor to the module’s epithelial phenotype. A specific role in bone-testis co-abundance remains unestablished.

#### KRT5

- **Related proteins** (co-abundance neighbors): KRT9 (0.90); STRING partners: KRT1 (0.923), KRT10 (0.793), KRT2 (0.871)
- **HPA**: Group enriched; Group enriched; blood Immune cell enriched; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 5. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the basal layer of the epidermis with family member KRT14. Mutations in t…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 2C, localized (0.768); epidermolysis bullosa simplex 2A, generalized severe (0.761); epidermolysis bullosa simplex 2B, generalized intermediate (0.761); epidermolysis bullosa simplex 2F, with mottled pigmentation (0.729); Dowling-Degos disease 1 (0.697)
- **Europe PMC papers**: 7044
- **Why important**: KRT5 is the basal-epithelial member of the module and connects to KRT9 in the module graph, with additional strong STRING relationships to KRT1, KRT10, and KRT2. It contributes to the globally corrected keratin, intermediate-filament, epithelial-development, and keratinization terms (15 globally significant GO/KEGG terms, q_global 4.36e-08–0.000869; see the table) and (8 globally significant GO/KEGG terms, q_global 0.0048–0.021; see the table). HPA places it across basal and suprabasal epithelial cell types and across several epithelial tissues. Its annotation supports basal epidermal structure, mechanical-stress response, migration, and intermediate-filament polymerization. Its disease associations include multiple forms of epidermolysis bullosa simplex and Dowling-Degos disease, and it has a substantial literature base.
- **Conclusion**: Established evidence supports KRT5 as the basal scaffold that complements the more differentiated keratins in this module. Its presence strengthens the interpretation of an epithelial maturation program, but does not establish that the module originates from bona fide bone or testis cells.

#### KRT9

- **Related proteins** (co-abundance neighbors): KRT2 (0.94), KRT1 (0.93), KRT10 (0.92), KRT5 (0.90); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 9. This gene encodes the type I keratin 9, an intermediate filament chain expressed only in the terminally differentiated epidermis of palms and soles. Mutations in this gene cause epidermolytic palmoplantar keratoderma. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: epidermolytic palmoplantar keratoderma, 1 (0.828); palmoplantar keratoderma, epidermolytic (0.682); Localized epidermolytic hyperkeratosis (0.511); Palmoplantar hyperkeratosis (0.456); Palmoplantar keratoderma (0.438)
- **Europe PMC papers**: 773
- **Why important**: KRT9 has the strongest weighted connectivity in the module subgraph and is connected to every other module gene, making it an important network-integrating member even though no STRING partners are listed for it in the gene-level summary. It contributes to the principal keratin and intermediate-filament terms (4 globally significant GO/KEGG terms, q_global 4.36e-08–4.92e-07; see the table) and (6 globally significant GO/KEGG terms, q_global 2.89e-06–0.000124; see the table), as well as the broader structural terms (GO:BP epithelial cell differentiation; q_global = 0.000869) and (8 globally significant GO/KEGG terms, q_global 0.0048–0.021; see the table). Its annotation identifies a terminally differentiated palmoplantar epidermal keratin, and its disease associations include epidermolytic palmoplantar keratoderma and related hyperkeratoses. Its literature base is smaller than that of the major keratins but still substantial.
- **Conclusion**: Established evidence supports KRT9 as a highly connected terminal-differentiation marker that reinforces the keratinized-epithelial interpretation. Its unusual network position may reflect coordinated abundance with the other keratins, but it does not by itself prove a direct physical interaction or a tissue-specific mechanism.
