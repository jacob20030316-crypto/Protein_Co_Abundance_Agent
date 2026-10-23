# Conserved co-abundance modules: circulatory_system and liver

## Module 0

**Tissue pair**: circulatory_system and liver  
**Genes (5)**: NT5E, F11R, LHPP, ST6GAL1, SULT1B1

### Function

This is a heterogeneous candidate co-abundance module rather than a functionally validated complex. The genes collectively suggest a possible interface between hepatic and epithelial metabolism, cell-surface nucleotide processing, glycosylation, cell adhesion, and phosphate-containing compound metabolism. SULT1B1 is the network hub and encodes a sulfotransferase involved in xenobiotic, phenol-containing compound, biogenic amine, and sulfur compound metabolism. LHPP contributes phosphate-containing compound metabolism; NT5E processes extracellular nucleotides at the plasma membrane; ST6GAL1 performs protein and lipid-associated sialylation and can occur in a soluble blood form; and F11R supports epithelial or endothelial tight-junction assembly and cell adhesion. These annotations do not define one coherent canonical pathway. No GO or KEGG term passed global correction, so there is no globally significant enrichment claim to make. The absence of an enriched term does not invalidate the co-abundance module, but it makes the functional interpretation provisional.

**Cell composition.** The module is not dominated by classical plasma proteins: only ST6GAL1 is annotated as secreted to blood, whereas NT5E is intracellular and membrane-associated and the remaining genes are not annotated as secreted. The HPA evidence instead indicates a mixed cellular composition. Hepatocyte enrichment is present for SULT1B1 and ST6GAL1, while other genes show enrichment in intestinal, epithelial, endothelial, neural, endocrine, or lymphoid cell types. Blood-cell associations include neutrophils, basophils, eosinophils, naive B cells, and naive CD8 T cells, although some genes have low immune-cell specificity. Thus, the shared signal may reflect co-occurring hepatocyte, epithelial or endothelial, and blood or immune-cell contributions in circulatory-system and liver samples rather than a single intracellular pathway. Liver protein detection supports biological presence for most members, but SULT1B1 was not detected by liver immunohistochemistry.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No pair among the module genes has a qualifying STRING interaction, and no hu.MAP complex contains multiple module members. Therefore, the abundance relationships are not supported here as established direct physical interactions or membership in a known multiprotein complex. Known biology remains gene-specific: SULT1B1 is a sulfotransferase, LHPP is a phosphatase, NT5E is an ectonucleotidase and lymphocyte differentiation marker, ST6GAL1 is a Golgi sialyltransferase with a soluble form, and F11R is a junctional adhesion protein. The network should consequently be interpreted as a co-abundance pattern, possibly driven by shared cell states, tissue composition, or coordinated regulation, not as a demonstrated physical assembly.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared co-abundance pattern could represent a novel cross-tissue association because these genes lack support from qualifying STRING interactions and shared hu.MAP complexes, while their established functions span several biological systems. However, this is not sufficient to claim a new molecular mechanism. Absence from these resources can reflect incomplete coverage, context dependence, indirect regulation, or cell-composition effects. The most defensible conclusion is that the module is a potentially novel tissue-level co-abundance signature requiring independent replication, cell-type-aware analysis, and experimental or longitudinal validation.

**Hypothesis.** Hypothesis: this module reflects coordinated abundance across liver-associated and circulating cell populations that jointly influence extracellular nucleotide turnover, glycan remodeling, epithelial or endothelial barrier properties, and xenobiotic or metabolite processing. In this model, hepatocyte-associated SULT1B1 and ST6GAL1 provide the metabolic and glycan-remodeling component, NT5E links the signal to extracellular nucleotide and immune-cell biology, F11R represents junctional or barrier state, and LHPP represents a cytosolic phosphate-metabolism component. This is a mechanistic hypothesis rather than an established pathway, because enrichment, STRING, and complex evidence do not support a unified molecular complex.

### Important genes

#### SULT1B1

- **Related proteins** (co-abundance neighbors): LHPP (0.84), NT5E (0.83), ST6GAL1 (0.80), F11R (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sulfotransferase family 1B member 1. Sulfotransferase enzymes catalyze the sulfate conjugation of many hormones, neurotransmitters, drugs, and xenobiotic compounds. These cytosolic enzymes are different in their tissue distributions and substrate specificities. The gene structure (number and length of exons) is similar among family members. However, the total genomic length of this gene is greater than that of other SULT1 genes. [pro…
- **Diseases (Open Targets)**: uterine corpus leiomyoma (0.512); autoimmune disorder of central nervous system (0.226); central nervous system cancer (0.225); female infertility (0.176); digestive system disorder (0.138)
- **Europe PMC papers**: 558
- **Why important**: SULT1B1 is the network hub, connecting every other module member in the inferred co-abundance graph. Its established sulfotransferase activity links the module to hormone, neurotransmitter, drug, xenobiotic, flavonoid, and phenol-containing compound metabolism. HPA supports intestinal and hepatocyte-associated expression and also shows blood-cell associations. It has a substantial literature base and disease associations spanning uterine, autoimmune, nervous-system, female-reproductive, and digestive disorders.
- **Conclusion**: Established: SULT1B1 is the strongest network-level anchor and a plausible hepatic or intestinal metabolic marker. Hypothesis: its centrality may reflect coordinated tissue or cell-state regulation rather than direct biochemical interaction with the other genes.

#### NT5E

- **Related proteins** (co-abundance neighbors): SULT1B1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 5'-nucleotidase ecto. The protein encoded by this gene is a plasma membrane protein that catalyzes the conversion of extracellular nucleotides to membrane-permeable nucleosides. The encoded protein is used as a determinant of lymphocyte differentiation. Defects in this gene can lead to the calcification of joints and arteries. Two transcript variants encoding different isoforms have been found for this gene.[provided b…
- **Diseases (Open Targets)**: hereditary arterial and articular multiple calcification syndrome (0.721); autosomal recessive spinocerebellar ataxia 20 (0.556); Spinocerebellar atrophy (0.340); non-small cell lung carcinoma (0.329); placental abruption (0.289)
- **Europe PMC papers**: 4404
- **Why important**: NT5E is the module's extracellular nucleotide-processing component. It is a plasma-membrane protein that converts extracellular nucleotides to nucleosides, is associated with leukocyte cell adhesion and responses to ATP, and serves as a lymphocyte differentiation determinant. HPA links it to lymphatic endothelial and several endocrine or neural cell types, as well as naive B-cell and naive CD8 T-cell populations. It has the largest literature volume among the listed genes and established associations with arterial and articular calcification and neurological disease.
- **Conclusion**: Established: NT5E provides a credible link to extracellular nucleotide signaling, immune-cell state, and vascular or tissue-interface biology. Hypothesis: its co-abundance with SULT1B1 may mark shared cellular composition or coordinated extracellular remodeling, not a direct interaction.

#### ST6GAL1

- **Related proteins** (co-abundance neighbors): SULT1B1 (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ST6 beta-galactoside alpha-2,6-sialyltransferase 1. This gene encodes a member of glycosyltransferase family 29. The encoded protein is a type II membrane protein that catalyzes the transfer of sialic acid from CMP-sialic acid to galactose-containing substrates. The protein, which is normally found in the Golgi but can be proteolytically processed to a soluble form, is involved in the generation of the cell-surface carbohydrate determinants and dif…
- **Diseases (Open Targets)**: COVID-19 (0.568); type 2 diabetes mellitus (0.539); diabetes mellitus (0.524); neurodegenerative disease (0.491); Orthomyxoviridae infectious disease (0.432)
- **Europe PMC papers**: 2147
- **Why important**: ST6GAL1 supplies the module's glycan-remodeling function. It is a Golgi sialyltransferase involved in the generation of cell-surface carbohydrate determinants and can be proteolytically processed into a soluble blood form. HPA identifies liver and lymphoid tissue enrichment and hepatocyte, B-cell, and plasma-cell-related expression. Its disease associations include COVID-19, diabetes, neurodegenerative disease, and infectious disease, with substantial literature support.
- **Conclusion**: Established: ST6GAL1 is a biologically plausible marker of hepatic and lymphoid glycoprotein remodeling. Hypothesis: its presence may connect liver-derived glycosylation changes with circulating immune or secreted-protein states.

#### F11R

- **Related proteins** (co-abundance neighbors): SULT1B1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Microtubules; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: F11 receptor. Tight junctions represent one mode of cell-to-cell adhesion in epithelial or endothelial cell sheets, forming continuous seals around cells and serving as a physical barrier to prevent solutes and water from passing freely through the paracellular space. The protein encoded by this immunoglobulin superfamily gene member is an important regulator of tight junction assembly in epithelia. In addition…
- **Diseases (Open Targets)**: neurodegenerative disease (0.354); cellulitis (0.135); abscess (0.135); neoplasm (0.115); breast cancer (0.114)
- **Europe PMC papers**: 1583
- **Why important**: F11R represents epithelial or endothelial barrier biology. Its established role includes tight-junction assembly, regulation of cell shape, inflammatory responses, and leukocyte cell-cell adhesion; it can also act as a receptor for reovirus and a ligand for LFA1. HPA shows broad cell-type enhancement across alveolar, esophageal, placental, ocular, and pancreatic epithelial populations, with neutrophil and eosinophil associations. It has substantial literature and disease links including neurodegenerative disease, cellulitis, abscess, neoplasm, and breast cancer.
- **Conclusion**: Established: F11R is a credible indicator of barrier and adhesion state. Hypothesis: its co-abundance may indicate epithelial or endothelial contribution to the shared tissue signal and may help explain the circulatory-system association.

#### LHPP

- **Related proteins** (co-abundance neighbors): SULT1B1 (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phospholysine phosphohistidine inorganic pyrophosphate phosphatase. Enables inorganic diphosphatase activity and protein homodimerization activity. Involved in phosphate-containing compound metabolic process. Located in cytosol and nuclear speck. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: open-angle glaucoma (0.473); Abnormality of the skeletal system (0.376); spina bifida (0.349); cervical carcinoma (0.321); liver disorder (0.315)
- **Europe PMC papers**: 987
- **Why important**: LHPP is the only module member connected exclusively to the hub in the inferred graph, making it a peripheral but potentially informative metabolic branch. It encodes a phospholysine phosphohistidine inorganic pyrophosphate phosphatase involved in phosphate-containing compound metabolism and is detected in liver tissue by immunohistochemistry. HPA identifies brain-associated tissue expression and specialized cell types, while disease associations include glaucoma, skeletal abnormalities, spina bifida, cervical carcinoma, and liver disorder.
- **Conclusion**: Established: LHPP contributes a distinct cytosolic phosphate-metabolism signal and is biologically present in liver. Hypothesis: its association with SULT1B1 may reflect coordinated metabolic state rather than participation in a shared physical complex.

## Module 1

**Tissue pair**: circulatory_system and liver  
**Genes (13)**: ALDH16A1, ASMTL, CLTB, CNPY3, GGCT, IDNK, HDHD2, CHCHD3, NSF, DLAT, PDCD6IP, TSPAN9, UBA3

### Function

The module does not have a statistically supported GO or KEGG functional annotation: no GO or KEGG term passed global correction. Its genes nevertheless suggest a heterogeneous cellular program involving mitochondrial organization and energy metabolism, vesicle and membrane trafficking, protein turnover and modification, glutathione-related metabolism, and intracellular signaling. The co-abundance structure is weakly organized around IDNK, which connects to several otherwise functionally diverse genes, while the remaining relationships are mostly short branches. Therefore, the safest interpretation is a shared tissue-associated cellular state rather than a demonstrated single biochemical pathway. The annotations of DLAT, CHCHD3, NSF, CLTB, GGCT, UBA3, and PDCD6IP provide biological plausibility for mitochondrial, trafficking, metabolic, and proteostasis components, but these are gene-level annotations and not globally significant module enrichment.

**Cell composition.** This is not predominantly a plasma-protein or classically secreted module. Only PDCD6IP and CNPY3 have intracellular-and-membrane secretome annotations, and the other genes are intracellular, mitochondrial, cytosolic, vesicular, Golgi, or membrane-associated. The module is also not blood-cell enriched: HPA reports low immune-cell specificity for nearly all genes and no recurring enriched blood-cell population. Most genes show cell-type-enhanced expression, but the reported cell types are diverse and include epithelial, renal, trophoblast, neuronal, cardiac, hepatic, and other populations. Protein detection in liver is widespread, whereas the circulatory-system protein evidence is unavailable in the supplied HPA summary. Consequently, the shared signal could reflect liver-associated expression, broadly shared cellular programs, or differing cell composition rather than a blood-cell or plasma-protein program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no hu.MAP complex containing multiple module members. Thus, the observed co-abundance edges are not supported here as established physical protein interactions or as membership in a known multiprotein complex. Known biology still exists at the individual-gene level: NSF participates in vesicle trafficking and receptor recycling; CLTB is a clathrin light chain involved in coated-vesicle biology; CHCHD3 is a MICOS-related mitochondrial cristae scaffold; DLAT is a component of the pyruvate dehydrogenase complex; UBA3 participates in neddylation; and PDCD6IP participates in ESCRT-associated vesicle formation. These established functions support several plausible cellular themes, but they do not demonstrate that the genes form one physical pathway in this module.

**STRING interactions (score >= 0.7)**: 0 of 78 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a new biological pathway on the basis of the supplied evidence. The absence of STRING interactions and hu.MAP complexes means that the specific cross-tissue co-abundance pattern is not represented by those resources, but absence from those databases does not prove novelty. The genes themselves have substantial prior annotation and literature, including well-established roles for vesicle trafficking, mitochondrial metabolism, glutathione catabolism, and protein modification. A cautious novelty claim is therefore limited to a potentially previously unreported co-abundance association shared by circulatory_system and liver. That claim requires replication in independent cohorts, preservation after cell-composition adjustment, and ideally experimental or perturbational validation.

**Hypothesis.** Hypothesis: the module may represent a shared liver-associated cellular state coupling mitochondrial energy handling and cristae maintenance with vesicle trafficking, receptor or membrane turnover, and proteostasis. IDNK may act as a co-abundance hub linking metabolic genes with trafficking and vesicular genes, while DLAT and CHCHD3 reflect mitochondrial demand and NSF, CLTB, and PDCD6IP reflect intracellular membrane traffic. GGCT could connect this state to glutathione homeostasis, and UBA3 could connect it to regulated protein modification. This is a mechanistic hypothesis only; the lack of globally enriched terms, STRING support, and hu.MAP complexes means that the proposed coupling is not established by the current module evidence.

### Important genes

#### IDNK

- **Related proteins** (co-abundance neighbors): ALDH16A1 (0.92), HDHD2 (0.87), GGCT (0.87), ASMTL (0.85), PDCD6IP (0.83), NSF (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IDNK gluconokinase. Predicted to enable gluconokinase activity. Predicted to be involved in D-gluconate catabolic process. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: device complication (0.278); schizophrenia (0.218); spondylolisthesis (0.128); DNA methylation (0.100); Abnormality of refraction (0.100)
- **Europe PMC papers**: 152
- **Why important**: IDNK is the network hub, with the greatest weighted connectivity in the supplied subgraph and links to ALDH16A1, HDHD2, GGCT, ASMTL, PDCD6IP, and NSF. Its annotation describes predicted gluconokinase activity and a possible role in D-gluconate catabolism, while HPA reports liver and brain tissue enhancement and enterocyte enhancement. Its literature volume is modest relative to the best-studied genes in the module, making it a potentially informative but incompletely characterized hub.
- **Conclusion**: Established: IDNK is the central co-abundance connector and has predicted carbohydrate-metabolic function with liver-associated protein detection. Hypothesis: IDNK may coordinate the metabolic and trafficking components of the module, but its hub status does not establish biochemical control or causality.

#### NSF

- **Related proteins** (co-abundance neighbors): CLTB (0.84), IDNK (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-ethylmaleimide sensitive factor, vesicle fusing ATPase. Enables PDZ domain binding activity and ionotropic glutamate receptor binding activity. Involved in intracellular protein transport; positive regulation of protein catabolic process; and positive regulation of receptor recycling. Located in Golgi apparatus; cytosol; and plasma membrane. Implicated in developmental and epileptic encephalopathy. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy 96 (0.561); neurodegenerative disease (0.529); atrial fibrillation (0.310); Abnormality of the skeletal system (0.303); androgenetic alopecia (0.300)
- **Europe PMC papers**: 65784
- **Why important**: NSF is connected to IDNK and CLTB and has a well-established role in intracellular protein transport, exocytosis, intra-Golgi trafficking, receptor recycling, and vesicle-mediated transport. It has very large literature volume and disease associations involving developmental epileptic encephalopathy and neurodegenerative disease. Its liver protein detection and brain tissue enhancement make it a plausible marker of a conserved vesicle-handling state.
- **Conclusion**: Established: NSF is a core vesicle-fusion ATPase with strong independent biological support. Hypothesis: its position in this module may indicate coordinated membrane trafficking, although the supplied data do not show a direct physical complex with the other module members.

#### CLTB

- **Related proteins** (co-abundance neighbors): NSF (0.84), CHCHD3 (0.81), CNPY3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: clathrin light chain B. Clathrin is a large, soluble protein composed of heavy and light chains. It functions as the main structural component of the lattice-type cytoplasmic face of coated pits and vesicles which entrap specific macromolecules during receptor-mediated endocytosis. This gene encodes one of two clathrin light chain proteins which are believed to function as regulatory elements. Alternative splicing result…
- **Diseases (Open Targets)**: neurodegenerative disease (0.259); hepatocellular carcinoma (0.078); neoplasm (0.075); Alzheimer disease (0.028); cancer (0.020)
- **Europe PMC papers**: 606
- **Why important**: CLTB is connected to NSF, CHCHD3, and CNPY3 and encodes a clathrin light-chain component of coated-pit and vesicle biology. Its annotations include intracellular transport, vesicle-mediated transport, and synaptic vesicle endocytosis, and it has substantial literature volume. Its vesicular localization and liver protein detection make it a strong representative of the module's membrane-trafficking aspect.
- **Conclusion**: Established: CLTB participates in clathrin-associated vesicle trafficking and is a relatively well-studied module member. Hypothesis: CLTB may connect general vesicle formation with the liver-associated co-abundance state, but the module does not establish a specific clathrin complex.

#### CHCHD3

- **Related proteins** (co-abundance neighbors): CLTB (0.81), UBA3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coiled-coil-helix-coiled-coil-helix domain containing 3. The protein encoded by this gene is an inner mitochondrial membrane scaffold protein. Absence of the encoded protein affects the structural integrity of mitochondrial cristae and leads to reductions in ATP production, cell growth, and oxygen consumption. This protein is part of the mitochondrial contact site and cristae organizing system (MICOS). Several transcript variants encoding different isof…
- **Diseases (Open Targets)**: neurodegenerative disease (0.537); smoking initiation (0.414); intelligence (0.385); insomnia (0.362); mathematical ability (0.312)
- **Europe PMC papers**: 549
- **Why important**: CHCHD3 links CLTB to UBA3 and encodes a mitochondrial inner-membrane scaffold associated with MICOS, cristae formation, mitochondrial fusion, and respiratory integrity. Its tissue enhancement in skeletal muscle and tongue, mitochondrial localization, liver protein detection, and established cellular role make it an important mitochondrial anchor. Its literature volume is substantial enough to support a well-defined function, while its connection to a trafficking gene is notable within this otherwise heterogeneous network.
- **Conclusion**: Established: CHCHD3 supports mitochondrial cristae organization and mitochondrial structural integrity. Hypothesis: it may represent the mitochondrial arm of a coordinated energy-and-trafficking state, but no evidence demonstrates direct coupling to CLTB or UBA3 in this module.

#### DLAT

- **Related proteins** (co-abundance neighbors): TSPAN9 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dihydrolipoamide S-acetyltransferase. This gene encodes component E2 of the multi-enzyme pyruvate dehydrogenase complex (PDC). PDC resides in the inner mitochondrial membrane and catalyzes the conversion of pyruvate to acetyl coenzyme A. The protein product of this gene, dihydrolipoamide acetyltransferase, accepts acetyl groups formed by the oxidative decarboxylation of pyruvate and transfers them to coenzyme A. Dihydrolipoamide acety…
- **Diseases (Open Targets)**: pyruvate dehydrogenase E2 deficiency (0.792); pyruvate decarboxylase deficiency (0.711); dystonic disorder (0.374); hereditary disease (0.341); neurodegenerative disease (0.322)
- **Europe PMC papers**: 3481
- **Why important**: DLAT is connected to TSPAN9 and encodes the E2 component of the pyruvate dehydrogenase complex, which converts pyruvate-derived carbon toward acetyl-CoA and links glycolysis with mitochondrial oxidation. It has extensive literature, liver protein detection, mitochondrial localization, and strong disease relevance through pyruvate dehydrogenase disorders and antimitochondrial autoantibodies. It provides the clearest established metabolic interpretation among the module genes.
- **Conclusion**: Established: DLAT is a central mitochondrial carbon-metabolism enzyme within the pyruvate dehydrogenase complex. Hypothesis: its co-abundance with TSPAN9 may reflect coordination between mitochondrial metabolic demand and membrane signaling or trafficking, but this relationship is not mechanistically demonstrated.

## Module 2

**Tissue pair**: circulatory_system and liver  
**Genes (37)**: ORM1, LRG1, SERPINA3, PRKAB2, GPT, ENPEP, AOC3, APOB, APOD, TGFBI, C1R, C4BPA, SERPINA6, CP, CFB, C3, C5, C9, DUSP23, HPX, HP, SERPING1, ITIH4, MAIP1, MTHFS, NIT1, PARP9, SELENOO, SIRT5, SPTBN2, TAGLN2, TNC, TNXB, TTN, TMEM70, UBA5, USP5

### Function

The module is a liver-derived circulating innate-immune and acute-phase protein program centered on complement activation, with evidence for both classical and alternative pathways. The primary evidence is the globally corrected enrichment for blood microparticles (GO:CC blood microparticle; q_global = 0.000495), circulating-immunoglobulin-mediated humoral immunity (GO:BP humoral immune response mediated by circulating immunoglobulin; q_global = 0.000743), complement activation (GO:BP complement activation; q_global = 0.00173), classical complement activation (GO:BP complement activation, classical pathway; q_global = 0.00528), alternative complement activation (GO:BP complement activation, alternative pathway; q_global = 0.00991), and the complement-and-coagulation cascade (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0124). The broader defense-response and lymphocyte-mediated immune terms (GO:BP defense response; q_global = 0.039) and (GO:BP lymphocyte mediated immunity; q_global = 0.0425) support an immune-defense interpretation, while the pertussis pathway (KEGG Pertussis - Homo sapiens (human); q_global = 0.0473) is consistent with complement biology rather than indicating a disease-specific mechanism. The module therefore most plausibly represents coordinated abundance of circulating complement, complement regulators, acute-phase proteins, and associated extracellular proteins.

**Cell composition.** This is predominantly a secreted plasma and liver program rather than a general intracellular housekeeping module. HPA identifies many secreted-to-blood proteins, and the module is strongly liver- and hepatocyte-associated; the HPA summary also identifies a substantial secreted component and frequent liver enrichment. The blood-microparticle result (GO:CC blood microparticle; q_global = 0.000495) and STRING tissue and compartment results (STRING TISSUES Bone marrow cell; within-query FDR = 3.41e-13), (STRING TISSUES Plasma cell; within-query FDR = 1.23e-12), (STRING TISSUES Bone marrow; within-query FDR = 2.62e-10), (STRING Keyword Secreted; within-query FDR = 3.03e-08), (STRING COMPARTMENTS Extracellular region; within-query FDR = 2.44e-05), (STRING COMPARTMENTS Blood microparticle; within-query FDR = 2.44e-05), and (STRING Component Blood microparticle; within-query FDR = 2.89e-05) reinforce the interpretation that measured co-abundance may reflect circulating proteins, vesicles, plasma composition, and liver production. Some genes have immune-cell enrichment, particularly complement or neutrophil-associated signals, but many module proteins are not detected in immune cells. Thus, the shared signal should not automatically be interpreted as coordinated transcription within one immune-cell population; it may largely reflect blood carryover or shared circulating protein abundance in both tissue groups.

**GO/KEGG enrichment**: 13 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 0.000495 | C3, C4BPA, C9, CFB, CP, HP, HPX, ITIH4, ORM1, SERPINA3, SERPING1 |
| GO:BP humoral immune response mediated by circulating immunoglobulin | 0.000743 | C1R, C3, C4BPA, C5, C9, HPX, SERPING1 |
| GO:BP complement activation | 0.00173 | C1R, C3, C4BPA, C5, C9, CFB, SERPING1 |
| GO:BP immunoglobulin mediated immune response | 0.00173 | C1R, C3, C4BPA, C5, C9, HPX, SERPING1 |
| GO:BP B cell mediated immunity | 0.00224 | C1R, C3, C4BPA, C5, C9, HPX, SERPING1 |
| GO:BP complement activation, classical pathway | 0.00528 | C1R, C3, C4BPA, C5, C9, SERPING1 |
| GO:BP humoral immune response | 0.00595 | C1R, C3, C4BPA, C5, C9, CFB, HPX, SERPING1 |
| GO:BP complement activation, alternative pathway | 0.00991 | C3, C5, C9, CFB |
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 0.0124 | C1R, C3, C4BPA, C5, C9, CFB, SERPING1 |
| GO:BP defense response | 0.039 | AOC3, APOD, C1R, C3, C4BPA, C5, C9, CFB, HP, HPX, ITIH4, ORM1, PARP9, SERPINA3, SERPING1, TNC |
| GO:BP lymphocyte mediated immunity | 0.0425 | C1R, C3, C4BPA, C5, C9, HPX, SERPING1 |
| GO:BP adaptive immune response based on somatic recombination of immune receptors built from immunoglobulin superfamily domains | 0.0425 | C1R, C3, C4BPA, C5, C9, HPX, SERPING1 |
| KEGG Pertussis - Homo sapiens (human) | 0.0473 | C1R, C3, C4BPA, C5, SERPING1 |

### STRING and hu.MAP

STRING supports a biologically coherent complement and plasma-protein core. Established high-confidence relationships include C1R with SERPING1 and C3, C3 with CFB, C5, C4BPA, HP, HPX, and SERPING1, and C5 with C9. Additional links connect plasma and acute-phase proteins, including CP, HP, HPX, ORM1, SERPINA3, APOB, and APOD. The STRING functional results (STRING NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization; within-query FDR = 2.4e-05) directly recover complement and coagulation biology, while (STRING TISSUES Bone marrow cell; within-query FDR = 3.41e-13) through (STRING TISSUES Bone marrow; within-query FDR = 2.62e-10) and (STRING COMPARTMENTS Extracellular region; within-query FDR = 2.44e-05) through (STRING Component Blood microparticle; within-query FDR = 2.89e-05) support bone-marrow, plasma-cell, extracellular-region, and blood-microparticle associations. hu.MAP repeatedly places CP, HP, CFB, SERPINA3, C3, C5, ORM1, HPX, C4BPA, SERPING1, and ITIH4 together across several complexes (hu.MAP huMAP3_09531.1) through. These are known relationships and indicate that much of the module recapitulates established circulating protein assemblies or shared complex membership. The network also contains peripheral links to lipid transport, extracellular matrix, metabolism, mitochondrial biology, and cellular structural proteins; these may represent secondary abundance coupling, tissue composition, or indirect associations rather than a single physical complex.

**STRING interactions (score >= 0.7)**: 30 of 666 gene pairs: APOB–APOD (0.864); APOB–C3 (0.819); APOB–GPT (0.717); C1R–C3 (0.935); C1R–SERPING1 (0.999); C3–C4BPA (0.817); C3–C5 (0.974); C3–CFB (0.999); C3–CP (0.751); C3–HP (0.862); C3–HPX (0.841); C3–ITIH4 (0.745); C3–ORM1 (0.775); C3–SERPING1 (0.954); C5–C9 (0.999); C5–CFB (0.774); CFB–SERPING1 (0.88); CP–HP (0.947); CP–HPX (0.88); CP–ORM1 (0.923); CP–SERPINA3 (0.822); ENPEP–ITIH4 (0.884); GPT–HP (0.918); HP–HPX (0.994); HP–ORM1 (0.973); HP–SERPINA3 (0.873); HPX–ITIH4 (0.706); HPX–ORM1 (0.778); LRG1–SERPINA3 (0.711); ORM1–SERPINA3 (0.918)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Bone marrow cell (FDR = 3.41e-13, 20 genes); TISSUES Plasma cell (FDR = 1.23e-12, 19 genes); TISSUES Bone marrow (FDR = 2.62e-10, 21 genes); Keyword Secreted (FDR = 3.03e-08, 20 genes); Keyword Disulfide bond (FDR = 9.2e-08, 22 genes); TISSUES Skeletal system (FDR = 2.54e-07, 23 genes); Keyword Signal (FDR = 1.54e-06, 20 genes); Keyword Glycoprotein (FDR = 2.12e-06, 21 genes); PMID (2022) Effects of Omega-3 and Antioxidant Cocktail Supplement on Prolonged Bed Rest: Results from Serum Proteome and Sphingolipids Analysis. (FDR = 5.12e-06, 13 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 5.12e-06, 16 genes); PMID (2017) Lectins: an effective tool for screening of potential cancer biomarkers. (FDR = 1.57e-05, 11 genes); NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization (FDR = 2.4e-05, 11 genes); COMPARTMENTS Extracellular region (FDR = 2.44e-05, 23 genes); COMPARTMENTS Blood microparticle (FDR = 2.44e-05, 12 genes); Component Blood microparticle (FDR = 2.89e-05, 12 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09531.1 (CP, HP, CFB, SERPINA3, C3, C5, ORM1, HPX, C4BPA, SERPING1, ITIH4; 11/47); huMAP3_10101.1 (CP, HP, CFB, SERPINA3, C3, C5, ORM1, HPX, C4BPA, SERPING1, ITIH4; 11/49); huMAP3_10678.1 (CP, HP, CFB, SERPINA3, C3, C5, ORM1, HPX, C4BPA, SERPING1, ITIH4; 11/71); huMAP3_15040.1 (CP, HP, CFB, SERPINA3, C3, ORM1, HPX, C4BPA, SERPING1, ITIH4; 10/64); huMAP3_08395.1 (CP, HP, CFB, SERPINA3, C3, C5, ORM1, HPX, C4BPA; 9/43); huMAP3_07432.1 (CP, HP, SERPINA3, C3, ORM1, HPX; 6/18); huMAP3_09434.1 (HP, SERPINA3, C3, C5, ORM1, ITIH4; 6/33); huMAP3_08796.1 (CFB, C5, C4BPA, SERPINA6, ITIH4; 5/15); huMAP3_09832.1 (CFB, C5, C4BPA, SERPINA6, ITIH4; 5/18); huMAP3_07265.1 (CP, HP, SERPINA3, ORM1, HPX; 5/20); huMAP3_09273.1 (CP, CFB, HPX, C4BPA, SERPING1; 5/28); huMAP3_08224.1 (HP, SERPINA3, C3, C5; 4/21); huMAP3_02242.1 (SERPINA3, C3, ORM1; 3/9); huMAP3_08700.1 (CP, ORM1, HPX; 3/11); huMAP3_07376.1 (C5, C4BPA; 2/4); huMAP3_02236.1 (CP, HPX; 2/7); huMAP3_02811.1 (C5, C4BPA; 2/8); huMAP3_00178.1 (C5, SERPINA6; 2/9); huMAP3_07541.1 (C5, C4BPA; 2/19); huMAP3_07701.1 (CFB, C4BPA; 2/22); huMAP3_14295.1 (LRG1, SERPINA6; 2/38)

### Novelty

The module is unlikely to constitute a newly discovered complement mechanism: its central genes, STRING relationships, and repeated hu.MAP memberships are already well established, and the globally corrected terms describe canonical complement and humoral immunity. A potentially new aspect is the reproducible co-abundance organization of this mixture across circulatory_system and liver, especially the way a liver-secreted complement and acute-phase program is shared between the tissue groups. However, the supplied evidence does not establish that this cross-tissue module has never been reported. Absence of a particular edge from STRING or hu.MAP would not prove novelty, and the strong plasma, liver, and blood-microparticle signature provides a plausible sampling or shared-compartment explanation. The conservative conclusion is that this is a biologically credible conserved module with possible dataset-specific organization, not demonstrated discovery of a new pathway.

**Hypothesis.** Mechanistic hypothesis: hepatocyte production and secretion of complement and acute-phase proteins generates a circulating extracellular pool that is captured similarly in circulatory_system and liver measurements. Within that pool, C3 and CFB may provide alternative-pathway amplification, C1R and C4BPA may represent classical-pathway initiation and regulation, SERPING1 may restrain activated proteases, and C5 with C9 may represent downstream membrane-attack-complex capacity. Acute-phase, heme-handling, lipid-transport, and extracellular-matrix proteins may co-vary with this complement pool because they are jointly regulated by hepatic inflammatory state, plasma vesicles, or tissue and blood composition. This is a hypothesis generated from co-abundance and annotation evidence; the data do not demonstrate physical interaction, causal regulation, or pathway activation in either tissue.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): CFB (0.90), ITIH4 (0.89), CP (0.85), GPT (0.82), TNC (0.80), ENPEP (0.80); STRING partners: APOB (0.819), C1R (0.935), C4BPA (0.817), C5 (0.974), CFB (0.999), CP (0.751), HP (0.862), HPX (0.841), ITIH4 (0.745), ORM1 (0.775), SERPING1 (0.954)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_15040.1, huMAP3_08395.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_08224.1, huMAP3_02242.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is the central complement hub in the module: it has strong network connectivity, extensive STRING support with C1R, C4BPA, C5, CFB, HP, HPX, ITIH4, ORM1, and SERPING1, and broad representation across the primary enrichment terms (GO:CC blood microparticle; q_global = 0.000495) through (KEGG Pertussis - Homo sapiens (human); q_global = 0.0473). HPA places it in liver-associated secreted protein biology and also reports immune-cell enrichment. Its established function spans both classical and alternative complement activation, and its disease associations include complement deficiency, complement glomerulopathy, atypical hemolytic-uremic syndrome, and age-related macular degeneration. It is also a heavily studied gene.
- **Conclusion**: Established evidence supports C3 as the principal functional anchor of the module and as a marker of circulating complement biology. The co-abundance data support its centrality but do not show that C3 drives the other genes in this module.

#### CFB

- **Related proteins** (co-abundance neighbors): C3 (0.90), SERPINA6 (0.88), PRKAB2 (0.87), ITIH4 (0.85); STRING partners: C3 (0.999), C5 (0.774), SERPING1 (0.88)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_15040.1, huMAP3_08395.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_09273.1, huMAP3_07701.1
- **Function (MyGene.info)**: complement factor B. This gene encodes complement factor B, a component of the alternative pathway of complement activation. Factor B circulates in the blood as a single chain polypeptide. Upon activation of the alternative pathway, it is cleaved by complement factor D yielding the noncatalytic chain Ba and the catalytic subunit Bb. The active subunit Bb is a serine protease which associates with C3b to form the alter…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with B factor anomaly (0.764); atypical hemolytic-uremic syndrome (0.705); Immunodeficiency due to a complement cascade protein anomaly (0.614); paroxysmal nocturnal hemoglobinuria (0.561); complement 3 glomerulopathy (0.546)
- **Europe PMC papers**: 7226
- **Why important**: CFB is a liver-enriched secreted complement component with a direct role in the alternative pathway. It is linked to C3 and SERPING1 in STRING and is present in multiple hu.MAP complement-related complexes (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_15040.1), (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_08796.1), (hu.MAP huMAP3_09832.1), (hu.MAP huMAP3_09273.1), and (hu.MAP huMAP3_07701.1). It contributes to the globally corrected complement and alternative-pathway terms (GO:BP complement activation; q_global = 0.00173), (GO:BP complement activation, alternative pathway; q_global = 0.00991), and (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0124). Its disease associations include atypical hemolytic-uremic syndrome, complement cascade abnormalities, and complement-mediated glomerulopathy, and its literature is substantial.
- **Conclusion**: Established evidence identifies CFB as the strongest module member for alternative-pathway interpretation. Its network position is consistent with coordinated complement abundance, but the module does not establish pathway cleavage or enzymatic activation.

#### C5

- **Related proteins** (co-abundance neighbors): SERPINA6 (0.85); STRING partners: C3 (0.974), C9 (0.999), CFB (0.774)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_08395.1, huMAP3_09434.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_08224.1, huMAP3_07376.1, huMAP3_02811.1, huMAP3_00178.1, huMAP3_07541.1
- **Function (MyGene.info)**: complement C5. This gene encodes a component of the complement system, a part of the innate immune system that plays an important role in inflammation, host homeostasis, and host defense against pathogens. The encoded preproprotein is proteolytically processed to generate multiple protein products, including the C5 alpha chain, C5 beta chain, C5a anaphylatoxin and C5b. The C5 protein is comprised of the C5 alpha…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.744); paroxysmal nocturnal hemoglobinuria (0.610); myasthenia gravis (0.586); atypical hemolytic-uremic syndrome (0.544); neuromyelitis optica (0.516)
- **Europe PMC papers**: 81450
- **Why important**: C5 is a downstream complement effector associated with C3, CFB, and C9 in STRING and with numerous complement complexes in hu.MAP. It appears across nearly all primary complement and humoral-immune terms (GO:BP humoral immune response mediated by circulating immunoglobulin; q_global = 0.000743) through (KEGG Pertussis - Homo sapiens (human); q_global = 0.0473). HPA identifies liver and hepatocyte enrichment and secretion to blood. Its established products include inflammatory and membrane-attack-complex-related fragments, and its disease associations include late complement deficiency, paroxysmal nocturnal hemoglobinuria, myasthenia gravis, atypical hemolytic-uremic syndrome, and neuromyelitis optica. It has extensive literature support.
- **Conclusion**: Established evidence places C5 at the effector end of the complement interpretation and makes it important for connecting upstream complement abundance to inflammatory and lytic potential. The co-abundance pattern alone cannot determine whether C5 is proteolytically activated.

#### C9

- **Related proteins** (co-abundance neighbors): ENPEP (0.93), LRG1 (0.93), TMEM70 (0.84), ITIH4 (0.84), APOD (0.81), PRKAB2 (0.81); STRING partners: C5 (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C9. This gene encodes the final component of the complement system. It participates in the formation of the Membrane Attack Complex (MAC). The MAC assembles on bacterial membranes to form a pore, permitting disruption of bacterial membrane organization. Mutations in this gene cause component C9 deficiency. [provided by RefSeq, Feb 2009].
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.747); age-related macular degeneration (0.584); complement component 9 deficiency (0.548); macular degeneration (0.541); complement deficiency (0.463)
- **Europe PMC papers**: 28081
- **Why important**: C9 is a liver-enriched secreted protein and the terminal complement component that participates in membrane attack complex formation. It is strongly connected to C5 in STRING and occupies a prominent network position through links with ENPEP, LRG1, TMEM70, ITIH4, APOD, and PRKAB2. It appears in the blood-microparticle and complement-related primary terms (GO:CC blood microparticle; q_global = 0.000495) through (GO:BP adaptive immune response based on somatic recombination of immune receptors built from immunoglobulin superfamily domains; q_global = 0.0425). Its disease associations include C9 deficiency, late complement deficiency, and age-related macular degeneration, with extensive literature support.
- **Conclusion**: Established evidence supports C9 as a downstream complement-effector marker and a useful indicator that the module extends beyond upstream recognition and regulation. Its additional network links may reflect co-abundance or shared sample context rather than a physical C9 complex.

#### SERPING1

- **Related proteins** (co-abundance neighbors): AOC3 (0.83), TNXB (0.83), ITIH4 (0.81); STRING partners: C1R (0.999), C3 (0.954), CFB (0.88)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_15040.1, huMAP3_09273.1
- **Function (MyGene.info)**: serpin family G member 1. This gene encodes a highly glycosylated plasma protein involved in the regulation of the complement cascade. Its encoded protein, C1 inhibitor, inhibits activated C1r and C1s of the first complement component and thus regulates complement activation. It is synthesized in the liver, and its deficiency is associated with hereditary angioneurotic oedema (HANE). Alternative splicing results in multipl…
- **Diseases (Open Targets)**: hereditary angioedema with C1Inh deficiency (0.828); hereditary angioedema type 1 (0.750); hereditary angioedema (0.728); angioedema (0.616); hereditary angioedema type 2 (0.614)
- **Europe PMC papers**: 4203
- **Why important**: SERPING1 is a secreted liver-associated inhibitor of complement proteases and is represented across the major humoral and complement terms (GO:CC blood microparticle; q_global = 0.000495) through (KEGG Pertussis - Homo sapiens (human); q_global = 0.0473). It has very strong STRING relationships with C1R, C3, and CFB and appears repeatedly in hu.MAP complement complexes (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_15040.1), and (hu.MAP huMAP3_09273.1). Its established disease association with hereditary angioedema directly illustrates the importance of complement regulation, and it has substantial literature support. Its module position connects classical-pathway initiation, alternative-pathway components, and regulatory biology.
- **Conclusion**: Established evidence supports SERPING1 as the principal inhibitory counterweight within the complement core. Its co-abundance with activators is compatible with coordinated production and homeostatic balancing, but does not prove that it functionally restrains complement activity in these samples.

#### ITIH4

- **Related proteins** (co-abundance neighbors): C3 (0.89), SERPINA3 (0.86), LRG1 (0.85), CFB (0.85), C9 (0.84), APOD (0.83), PRKAB2 (0.82), SERPING1 (0.81); STRING partners: C3 (0.745), ENPEP (0.884), HPX (0.706)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_15040.1, huMAP3_09434.1, huMAP3_08796.1, huMAP3_09832.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 4. The protein encoded by this gene is secreted into the blood, where it is cleaved by plasma kallikrein into two smaller forms. Expression of this gene has been detected only in liver, and it seems to be upregulated during surgical trauma. This gene is part of a cluster of similar genes on chromosome 3. Two transcript variants encoding different isoforms have been found for this gene. [provided by R…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.466); coronary artery disorder (0.417); type 2 diabetes mellitus (0.397); osteoarthritis (0.387); diabetes mellitus (0.363)
- **Europe PMC papers**: 1710
- **Why important**: ITIH4 has the highest network connectivity and strongest weighted position in the supplied module, linking complement proteins, acute-phase proteins, LRG1, APOD, and SERPING1. It is liver-enriched, secreted to blood, and included in the blood-microparticle and defense-response terms (GO:CC blood microparticle; q_global = 0.000495) and (GO:BP defense response; q_global = 0.039). STRING and hu.MAP repeatedly place it with the plasma-protein complement assemblage (hu.MAP huMAP3_09531.1) through (hu.MAP huMAP3_09832.1) and (hu.MAP huMAP3_09273.1). Its established annotation includes acute-phase response, cytokine response, and hyaluronan-related biology; disease associations include coronary artery disorder, type two diabetes mellitus, osteoarthritis, and skeletal-system abnormality. It also has substantial literature support.
- **Conclusion**: Established evidence makes ITIH4 an important network connector and a plausible indicator of hepatic acute-phase state, even though it is not itself a canonical complement component. Its central position supports a bridge between complement and broader extracellular inflammatory biology; whether it mechanistically organizes that bridge remains a hypothesis.

## Module 3

**Tissue pair**: circulatory_system and liver  
**Genes (10)**: A1BG, APOL3, COQ8A, MCEE, MGLL, PANK4, PLGRKT, PPCS, PCTP, STARD10

### Function

This is a weakly connected metabolic and lipid-associated co-abundance module rather than a securely defined pathway module. Its gene annotations converge on lipid handling, phospholipid transfer, fatty-acid or acylglycerol metabolism, coenzyme A biosynthesis, mitochondrial energy-related processes, and inflammatory lipid signaling. The strongest functional interpretation comes from the concordance of PCTP, STARD10, APOL3, MGLL, MCEE, PPCS, PANK4, and COQ8A annotations, not from enrichment statistics. No GO/KEGG term passed global correction, so there is no globally significant GO/KEGG functional term for this module. The sparse network and absence of STRING functional enrichment make the pathway-level interpretation provisional.

**Cell composition.** The module is not predominantly composed of secreted plasma proteins. A1BG is secreted to blood and is liver-enriched, while the other genes are mainly intracellular, membrane-associated, mitochondrial, cytosolic, vesicular, or nucleolar according to HPA. Several genes show liver enrichment or liver protein detection, especially A1BG, PCTP, and STARD10, supporting a liver-related component. The blood-cell evidence is also important: several genes are immune-cell enhanced, with signals involving eosinophils, monocytes, basophils, and neutrophils. Most genes have cell-type-enhanced rather than broadly uniform single-cell profiles. Therefore, the shared circulatory-system/liver signal could reflect a combination of hepatocyte or liver-associated biology and shared blood-cell composition in the samples, rather than a universal circulating secreted-protein program. The available HPA summary does not support calling the module a housekeeping module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship among module members is the PANK4–PPCS pair. This is consistent with a possible connection to coenzyme A or pantothenate-related metabolism, but it does not establish that the entire module forms a physical complex. No module-member pair is represented in the hu.MAP complexes reported for this module. The remaining co-abundance edges are therefore largely not supported by the listed high-confidence STRING interactions or hu.MAP complexes. Overall, the network may capture coordinated abundance, tissue composition, or shared regulation more than a pre-existing multiprotein complex.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: PANK4–PPCS (0.929)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The co-abundance configuration may be a tissue-pair-specific observation, but it cannot be called a definitively new biological module from this evidence alone. The absence of a matching hu.MAP complex and the very limited STRING support suggest that the observed grouping is not simply a well-established physical complex. However, absence from STRING or hu.MAP does not prove novelty: the pattern could reflect tissue-specific regulation, shared cell composition, metabolic state, or incomplete interaction coverage. The lack of globally significant GO/KEGG enrichment and the sparse known-interaction structure further argue for cautious wording: this is a potentially novel co-abundance association requiring replication and external validation, not a proven new pathway.

**Hypothesis.** Hypothesis: the module reflects coordinated liver-linked lipid and acyl-CoA homeostasis across liver and circulating samples, with its apparent conservation partly influenced by hepatocyte-associated proteins and immune-cell composition. PCTP, STARD10, APOL3, and MGLL could represent lipid transport or lipid-processing components, while MCEE, PPCS, and PANK4 could connect the signal to mitochondrial or coenzyme A metabolism; COQ8A may indicate an energy-related mitochondrial context. A1BG may contribute a blood-borne liver signal rather than a core intracellular mechanism. This hypothesis predicts that the module should track lipid and coenzyme A metabolic states and should be tested after adjusting for blood-cell and liver-cell proportions, followed by replication in independent tissue cohorts and targeted protein or transcript measurements.

### Important genes

#### PCTP

- **Related proteins** (co-abundance neighbors): COQ8A (0.84), PPCS (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Nucleoli; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphatidylcholine transfer protein. Enables phosphatidylcholine binding activity and phosphatidylcholine transporter activity. Involved in phospholipid transport. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.408); neurodegenerative disease (0.346); bronchial disorder (0.241); response to exercise (0.187); jaw disease (0.172)
- **Europe PMC papers**: 515
- **Why important**: PCTP is a central bridge in the observed subgraph, linking PPCS with COQ8A. Its established phosphatidylcholine binding, phospholipid transport, liver-enhanced expression, hepatocyte association, and liver protein detection make it a strong anchor for the lipid and liver interpretation. Its disease and literature records indicate that it is biologically studied, while its network position connects lipid biology with the mitochondrial-associated branch.
- **Conclusion**: Established evidence supports PCTP as a liver-associated phospholipid transport gene and a structurally informative connector in this module. Hypothesis: PCTP may help couple lipid handling to the coenzyme A or mitochondrial signal, but the co-abundance data do not establish direct biochemical cooperation.

#### STARD10

- **Related proteins** (co-abundance neighbors): APOL3 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: StAR related lipid transfer domain containing 10. Predicted to enable lipid binding activity. Predicted to be involved in lipid transport. Predicted to act upstream of or within bile acid secretion and positive regulation of peroxisome proliferator activated receptor signaling pathway. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: diabetes mellitus (0.504); type 2 diabetes mellitus (0.444); gestational diabetes (0.324); mathematical ability (0.270); hypothyroidism (0.230)
- **Europe PMC papers**: 433
- **Why important**: STARD10 is liver-enhanced, is associated with hepatocytes and parietal cells, and has lipid-binding and lipid-transport annotations including a relationship to bile-acid secretion and PPAR signaling. It links directly to APOL3 in the module and has disease associations involving diabetes. These features make it relevant to a liver lipid-regulatory interpretation despite its peripheral network position.
- **Conclusion**: Established evidence supports STARD10 as a liver-associated lipid-handling gene with metabolic disease relevance. Hypothesis: its co-abundance with APOL3 may mark coordinated lipid or bile-related regulation in the shared tissue context, rather than a direct protein interaction.

#### PPCS

- **Related proteins** (co-abundance neighbors): MCEE (0.85), PCTP (0.80); STRING partners: PANK4 (0.929)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphopantothenoylcysteine synthetase. Biosynthesis of coenzyme A (CoA) from pantothenic acid (vitamin B5) is an essential universal pathway in prokaryotes and eukaryotes. PPCS (EC 6.3.2.5), one of the last enzymes in this pathway, converts phosphopantothenate to phosphopantothenoylcysteine (Daugherty et al., 2002 [PubMed 11923312]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: dilated cardiomyopathy (0.596); neurodegenerative disease (0.563); lysosomal storage disease (0.370); familial isolated dilated cardiomyopathy (0.370); cardiomyopathy, dilated, 2c (0.370)
- **Europe PMC papers**: 1174
- **Why important**: PPCS is an enzyme in coenzyme A biosynthesis and is connected in the module to MCEE and PCTP. It is the member with the listed high-confidence STRING relationship to PANK4, giving the module its clearest known interaction link. Its associations with cardiomyopathy and other disease contexts make it relevant to systemic metabolic and energy biology.
- **Conclusion**: Established evidence supports PPCS as a coenzyme A biosynthetic enzyme and as part of the only listed high-confidence STRING pair within the module. Hypothesis: PPCS may connect coenzyme A availability with lipid-processing abundance, but the module does not demonstrate a complete coenzyme A pathway.

#### MCEE

- **Related proteins** (co-abundance neighbors): PPCS (0.85), MGLL (0.82), APOL3 (0.81), PANK4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methylmalonyl-CoA epimerase. The product of this gene catalyzes the interconversion of D- and L-methylmalonyl-CoA during the degradation of branched chain amino acids. odd chain-length fatty acids, and other metabolites. Mutations in this gene result in methylmalonyl-CoA epimerase deficiency, which is presented as mild to moderate methylmalonic aciduria. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: methylmalonic acidemia due to methylmalonyl-CoA epimerase deficiency (0.754); hereditary disease (0.411); methylmalonic acidemia (0.407); rheumatoid arthritis (0.026); dyshidrosis (0.026)
- **Europe PMC papers**: 520
- **Why important**: MCEE has the highest network connectivity in the reported subgraph and links PPCS, MGLL, APOL3, and PANK4. Its established role in methylmalonyl-CoA metabolism and odd-chain or branched-chain substrate degradation provides a plausible metabolic bridge between lipid-related genes and coenzyme A biology. It also has a defined inherited metabolic disease association and substantial literature support.
- **Conclusion**: Established evidence supports MCEE as a central metabolic enzyme and the principal network connector in this module. Hypothesis: MCEE may act as a co-abundance hub because the module reflects coordinated mitochondrial or acyl-CoA metabolic state, but network centrality alone does not establish regulatory control.

#### APOL3

- **Related proteins** (co-abundance neighbors): PLGRKT (0.88), STARD10 (0.85), MCEE (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein L3. This gene is a member of the apolipoprotein L gene family, and it is present in a cluster with other family members on chromosome 22. The encoded protein is found in the cytoplasm, where it may affect the movement of lipids, including cholesterol, and/or allow the binding of lipids to organelles. In addition, expression of this gene is up-regulated by tumor necrosis factor-alpha in endothelial cel…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.522); severe acute respiratory syndrome (0.203); COVID-19 (0.203); neurofibromatosis (0.125); colorectal carcinoma (0.094)
- **Europe PMC papers**: 740
- **Why important**: APOL3 connects PLGRKT, STARD10, and MCEE and has annotations involving lipid transport, lipoprotein metabolism, inflammatory response, and NF-kappa B signaling. Its induction by inflammatory signaling in endothelial contexts and its cell-type associations involving Kupffer cells and vascular-related cells make it especially relevant to a blood-versus-liver interpretation. It also has disease and infection-related associations and meaningful literature support.
- **Conclusion**: Established evidence supports APOL3 as an intracellular or membrane-associated apolipoprotein-family member with lipid and inflammatory relevance. Hypothesis: APOL3 may be a regulatory interface between liver lipid handling and immune or endothelial composition, but the module does not prove that inflammation drives the co-abundance pattern.

#### MGLL

- **Related proteins** (co-abundance neighbors): MCEE (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: monoglyceride lipase. This gene encodes a serine hydrolase of the AB hydrolase superfamily that catalyzes the conversion of monoacylglycerides to free fatty acids and glycerol. The encoded protein plays a critical role in several physiological processes including pain and nociperception through hydrolysis of the endocannabinoid 2-arachidonoylglycerol. Expression of this gene may play a role in cancer tumorigenesis and …
- **Diseases (Open Targets)**: smoking initiation (0.348); prostate carcinoma (0.344); color vision disorder (0.278); Thrombophlebitis (0.236); phlebitis (0.236)
- **Europe PMC papers**: 3868
- **Why important**: MGLL is connected to MCEE and has a well-established role in monoacylglycerol hydrolysis, free-fatty-acid production, endocannabinoid metabolism, triglyceride catabolism, and inflammatory signaling. It has the largest listed literature presence among the selected genes and is detected in liver, while also showing association with cardiomyocytes and monocytes. These features make it an informative functional representative even though it is not a highly connected node.
- **Conclusion**: Established evidence supports MGLL as a lipid and inflammatory metabolism enzyme with liver and immune-cell relevance. Hypothesis: MGLL may contribute to the module through coordinated lipid-turnover state or sample cellular composition, but its single network connection does not establish that it is a module driver.

## Module 4

**Tissue pair**: circulatory_system and liver  
**Genes (10)**: ABCB7, ACOX3, GAMT, SLC25A22, GCLC, PHKB, NUDT16, PAPSS2, SEPSECS, DARS2

### Function

The module does not have a globally significant GO or KEGG annotation: no term passed global correction. Its gene-level biology nevertheless points to a heterogeneous metabolic and organelle-associated program. The strongest network position is occupied by SEPSECS, which connects genes involved in selenocysteine incorporation, glutathione production, RNA and nucleotide-related processes, creatine synthesis, and peroxisomal fatty-acid oxidation. Other connected components link PAPSS2 with mitochondrial transport, mitochondrial translation, glycogen regulation, and heme or iron-sulfur biology. Taken together, the most defensible interpretation is a liver-associated metabolic and cellular stress-response co-abundance pattern rather than a single established pathway. The absence of a globally enriched term does not invalidate the module; it indicates that the genes do not form a sufficiently concentrated annotated pathway under the specified correction procedure.

**Cell composition.** This is not a plasma or secreted-protein module: the fact sheet reports no secreted genes. It is also not strongly blood-cell specific overall. Most genes have low immune-cell specificity, although PAPSS2 has group-enriched myeloid annotations, GCLC is immune-cell enhanced in NK cells, and NUDT16 has broad myeloid and granulocyte annotations. The dominant tissue and cell-type pattern is instead organ-associated and heterogeneous, with liver and hepatocyte representation alongside skeletal muscle, brain, pancreas, photoreceptor, enterocyte, and other specialized cell annotations. Several genes are broadly expressed or have low tissue specificity. Therefore, the shared signal between circulatory_system and liver could partly reflect hepatocyte or other shared cellular composition, but the data do not support interpreting it as a simple blood-protein signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The module has no high-confidence STRING interaction among its gene pairs, and STRING reports no supplementary functional enrichment. No hu.MAP complex contains multiple module members. Thus the co-abundance edges are not independently supported as known physical protein interactions or a recognized multiprotein complex. The observed network should be interpreted as a coordinated expression pattern, not as a demonstrated biochemical assembly. Known biology still provides plausible functional links at the pathway level: SEPSECS supports selenocysteine incorporation, GCLC supports glutathione synthesis, PAPSS2 supports sulfate-donor production, PHKB supports glycogen breakdown regulation, ABCB7 supports mitochondrial heme and iron-sulfur handling, and the remaining genes support mitochondrial transport, RNA metabolism, creatine synthesis, or peroxisomal lipid oxidation.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel tissue-pair co-abundance association, but the evidence is insufficient to call it a newly discovered biological pathway or molecular complex. The absence of STRING and hu.MAP support increases the possibility that the particular gene combination and cross-tissue co-abundance pattern have not been characterized previously. However, absence from those resources does not prove novelty, because such databases favor experimentally studied interactions and complexes, whereas co-abundance can arise from shared regulation, cell composition, organelle content, or metabolic state. The appropriate conclusion is that the module is a potentially novel systems-level observation requiring replication, cell-composition adjustment, and experimental or independent cohort validation.

**Hypothesis.** Hypothesis: the shared module reflects coordinated metabolic adaptation in liver-related cells and matched circulatory-system samples, combining redox protection, selenium-dependent protein synthesis, mitochondrial substrate and cofactor handling, glycogen regulation, creatine production, sulfate metabolism, and peroxisomal lipid processing. SEPSECS and GCLC could mark a redox-sensitive core, while PAPSS2, ABCB7, SLC25A22, and DARS2 could reflect linked mitochondrial and biosynthetic demands. PHKB and GAMT could connect this state to carbohydrate and energy buffering. This is a mechanistic hypothesis, not an established causal model; the sparse topology, lack of STRING or hu.MAP support, and absence of globally significant enrichment require that interpretation to remain provisional.

### Important genes

#### SEPSECS

- **Related proteins** (co-abundance neighbors): ACOX3 (0.89), GCLC (0.87), NUDT16 (0.84), GAMT (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Sep (O-phosphoserine) tRNA:Sec (selenocysteine) tRNA synthase. The amino acid selenocysteine is the only amino acid that does not have its own tRNA synthetase. Instead, this amino acid is synthesized on its cognate tRNA in a three step process. The protein encoded by this gene catalyzes the third step in the process, the conversion of O-phosphoseryl-tRNA(Sec) to selenocysteinyl-tRNA(Sec).[provided by RefSeq, Mar 2011].
- **Diseases (Open Targets)**: pontocerebellar hypoplasia type 2D (0.757); progressive cerebello-cerebral atrophy (0.667); pontocerebellar hypoplasia type 2 (0.667); pontocerebellar hypoplasia (0.660); neurodegenerative disease (0.537)
- **Europe PMC papers**: 491
- **Why important**: SEPSECS has the strongest network position in the module and connects to ACOX3, GCLC, NUDT16, and GAMT. Its established function is the final step of selenocysteine-tRNA formation, making it relevant to selenium-dependent protein synthesis and cellular redox biology. HPA supports liver and hepatocyte association, while the disease evidence links it to pontocerebellar hypoplasia and related neurodegenerative phenotypes. Its literature support is substantial relative to most module members.
- **Conclusion**: Established: SEPSECS is a liver-associated, highly connected module member with a defined role in selenocysteine incorporation. Hypothesis: it may be a central marker of a redox and proteostasis-related state in this module, but the co-abundance data do not establish that it regulates the other genes.

#### GCLC

- **Related proteins** (co-abundance neighbors): SEPSECS (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamate-cysteine ligase catalytic subunit. Glutamate-cysteine ligase, also known as gamma-glutamylcysteine synthetase is the first rate-limiting enzyme of glutathione synthesis. The enzyme consists of two subunits, a heavy catalytic subunit and a light regulatory subunit. This locus encodes the catalytic subunit, while the regulatory subunit is derived from a different gene located on chromosome 1p22-p21. Mutations at this locus have been …
- **Diseases (Open Targets)**: gamma-glutamylcysteine synthetase deficiency (0.766); cystic fibrosis (0.375); neurodegenerative disease (0.373); non-autoimmune hemolytic anemia (0.370); lung adenocarcinoma (0.331)
- **Europe PMC papers**: 8941
- **Why important**: GCLC is directly connected to SEPSECS and encodes the catalytic, rate-limiting component of glutathione synthesis. It is tissue enhanced in liver, detected in liver by HPA, and has an immune-cell-enhanced annotation in NK cells. Its disease associations include gamma-glutamylcysteine synthetase deficiency and hemolytic anemia, providing a clear link to redox and blood-related physiology. It also has the largest literature volume among the module genes, supporting strong prior biological characterization.
- **Conclusion**: Established: GCLC is a biologically credible redox and liver marker with direct disease relevance. Hypothesis: its association with SEPSECS may indicate coordinated demand for antioxidant protection, although no physical interaction or enriched pathway was demonstrated.

#### PAPSS2

- **Related proteins** (co-abundance neighbors): SLC25A22 (0.85), DARS2 (0.82), PHKB (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3'-phosphoadenosine 5'-phosphosulfate synthase 2. Sulfation is a common modification of endogenous (lipids, proteins, and carbohydrates) and exogenous (xenobiotics and drugs) compounds. In mammals, the sulfate source is 3'-phosphoadenosine 5'-phosphosulfate (PAPS), created from ATP and inorganic sulfate. Two different tissue isoforms encoded by different genes synthesize PAPS. This gene encodes one of the two PAPS synthetases. Defects in this gen…
- **Diseases (Open Targets)**: spondyloepimetaphyseal dysplasia, PAPSS2 type (0.799); hereditary disease (0.471); Spondyloepiphyseal dysplasia and spondyloepimetaphyseal dysplasia (0.462); autosomal recessive brachyolmia (0.455); skeletal dysplasia (0.343)
- **Europe PMC papers**: 1005
- **Why important**: PAPSS2 occupies a connecting position between SLC25A22, DARS2, and PHKB. It produces the sulfate donor PAPS, thereby supporting sulfation of endogenous and exogenous compounds. HPA associates it with adrenal tissue and several cell types, including myeloid dendritic and monocyte populations. Its disease associations include PAPSS2-related skeletal dysplasia and other skeletal disorders, and its literature base is substantial. Its network position makes it useful for linking mitochondrial, carbohydrate, and sulfation-related signals.
- **Conclusion**: Established: PAPSS2 is a connected biosynthetic enzyme with recognized disease relevance and a role in sulfation. Hypothesis: it may reflect altered metabolic or xenobiotic-processing demand in the shared tissue state, but the module provides no evidence that sulfation is its defining function.

#### ABCB7

- **Related proteins** (co-abundance neighbors): ACOX3 (0.84), PHKB (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP binding cassette subfamily B member 7. The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily ar…
- **Diseases (Open Targets)**: X-linked sideroblastic anemia with ataxia (0.819); sideroblastic anemia (0.378); hereditary disease (0.340); spinocerebellar ataxia type 1 (0.333); mitochondrial disease (0.187)
- **Europe PMC papers**: 1100
- **Why important**: ABCB7 connects ACOX3 and PHKB and has liver protein detection in HPA. Its established functions include mitochondrial heme transport, intracellular iron handling, and iron-sulfur cluster assembly. It is associated with X-linked sideroblastic anemia and ataxia and with other sideroblastic or mitochondrial disorders. These functions provide a biologically important bridge between energy metabolism, mitochondrial cofactor handling, and circulatory phenotypes.
- **Conclusion**: Established: ABCB7 is a liver-detected mitochondrial transport factor with strong relevance to heme and iron-sulfur biology. Hypothesis: it may indicate mitochondrial cofactor demand within the module, but its edge relationships are co-abundance associations rather than proven protein interactions.

#### GAMT

- **Related proteins** (co-abundance neighbors): SEPSECS (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: guanidinoacetate N-methyltransferase. The protein encoded by this gene is a methyltransferase that converts guanidoacetate to creatine, using S-adenosylmethionine as the methyl donor. Defects in this gene have been implicated in neurologic syndromes and muscular hypotonia, probably due to creatine deficiency and accumulation of guanidinoacetate in the brain of affected individuals. Two transcript variants encoding different isoforms h…
- **Diseases (Open Targets)**: guanidinoacetate methyltransferase deficiency (0.853); cerebral creatine deficiency syndrome (0.580); hereditary disease (0.533); Intellectual disability (0.372); Seizure (0.371)
- **Europe PMC papers**: 1303
- **Why important**: GAMT is directly linked to SEPSECS and is tissue enhanced in liver, skeletal muscle, and tongue, with hepatocyte representation in HPA. It catalyzes creatine biosynthesis and is associated with guanidinoacetate methyltransferase deficiency, cerebral creatine deficiency, intellectual disability, and seizures. Its function connects the module to cellular energy buffering and muscle-relevant metabolism, while its network placement links that biology to the module's most connected gene.
- **Conclusion**: Established: GAMT is a liver- and muscle-associated creatine-biosynthesis enzyme with clear inherited-disease relevance. Hypothesis: its co-abundance with SEPSECS may mark coordinated energy and redox metabolism, but the available evidence does not establish a direct causal relationship.

## Module 5

**Tissue pair**: circulatory_system and liver  
**Genes (5)**: ACADM, ACSL1, ASL, DHRS1, PTGR1

### Function

This is a liver-centered metabolic co-abundance module, with a coherent but mixed biochemical theme rather than a formally enriched pathway. PTGR1 is the network hub and links genes involved in eicosanoid inactivation, fatty-acid activation, mitochondrial fatty-acid oxidation, hepatic nitrogen disposal, and oxidoreductase activity. The network therefore suggests coordinated hepatic handling of lipids, lipid-derived signaling molecules, and intermediary metabolism. However, no GO or KEGG term passed global correction, so this functional interpretation is based on the individual gene annotations and network structure, not on globally significant pathway enrichment. The sparse topology also argues against interpreting the module as a complete physical pathway or complex.

**Cell composition.** The module is strongly liver-associated by HPA evidence: every member has liver protein detection, and liver is the most consistently enriched tissue. Hepatocytes are a recurring cell-type association, with additional associations involving enterocytes and epithelial cell types. None of the genes is secreted, so this is not a plasma-protein or secretome module. Most genes have low immune-cell specificity, although ACSL1 is associated with neutrophils and PTGR1 with plasmacytoid dendritic cells. The shared signal in circulatory_system and liver therefore more plausibly reflects liver-derived or shared metabolic cell-type biology, especially hepatocyte biology, than a module dominated by blood cells or circulating secreted proteins.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The co-abundance graph is a sparse star-like structure centered on PTGR1. The only high-confidence STRING relationship is between ACADM and ACSL1, which provides limited prior support for a fatty-acid metabolic connection. PTGR1, ASL, and DHRS1 have no reported STRING partners in the supplied evidence, and no hu.MAP complex contains multiple module members. Thus, most co-abundance edges are not supported as established protein-protein interactions or as membership in a known multiprotein complex. STRING and hu.MAP support a small portion of the biological interpretation, but they do not establish the module as a known physical complex.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: ACADM–ACSL1 (0.728)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a previously unreported cross-tissue co-abundance pattern, because the module has a distinctive combination of a PTGR1-centered network with hepatic urea-cycle, fatty-acid, mitochondrial, and oxidoreductase genes, while the supplied STRING and hu.MAP evidence provides little prior network support. The finding should nevertheless be described as potentially novel rather than definitively new. The individual genes and several of their functions are well established, and the ACADM–ACSL1 relationship is already represented in STRING. Moreover, absence from STRING or hu.MAP alone cannot prove novelty. Independent replication, preservation in other cohorts, control for hepatocyte abundance, and testing against liver metabolic state would be needed to establish that the co-abundance pattern is a reproducible biological module rather than a consequence of shared tissue composition.

**Hypothesis.** Hypothesis: variation in hepatocyte metabolic state coordinates PTGR1-mediated inactivation of lipid-derived inflammatory mediators with fatty-acid activation by ACSL1, mitochondrial fatty-acid oxidation by ACADM, hepatic nitrogen metabolism through ASL, and an as-yet poorly defined DHRS1 oxidoreductase function. In this model, the module reflects a shared hepatic response to nutrient, lipid, and metabolic demands that can become visible in both liver tissue and circulatory-system measurements through liver-derived molecular signals or shared cell-composition effects. This is a hypothesis, not a demonstrated biochemical pathway: the absence of globally significant GO or KEGG enrichment, the sparse network, and the lack of a shared hu.MAP complex limit mechanistic certainty.

### Important genes

#### PTGR1

- **Related proteins** (co-abundance neighbors): ACSL1 (0.86), ASL (0.83), DHRS1 (0.83), ACADM (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prostaglandin reductase 1. This gene encodes an enzyme that is involved in the inactivation of the chemotactic factor, leukotriene B4. The encoded protein specifically catalyzes the NADP+ dependent conversion of leukotriene B4 to 12-oxo-leukotriene B4. A pseudogene of this gene is found on chromosome 1. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2009].
- **Diseases (Open Targets)**: poisoning (0.285); response to antibiotic (0.280); malunion fracture (0.269); Alzheimer disease (0.242); Parkinson disease (0.241)
- **Europe PMC papers**: 699
- **Why important**: PTGR1 is the network hub, connecting every other module member in the supplied co-abundance graph. Its established function is the NADP-dependent conversion of leukotriene B4 to an inactive oxo-metabolite, with additional annotations involving prostaglandin and lipoxin metabolism. It is liver and intestine enhanced, has hepatocyte associations, and has a substantial literature base. Its central network position makes it the strongest candidate for organizing the module, although centrality alone does not prove biochemical control.
- **Conclusion**: Established evidence supports PTGR1 as a hepatic lipid-mediator metabolic enzyme and as the central co-abundance correlate in this module. The hypothesis that PTGR1 regulates the other genes, or that its activity drives the module, remains unproven.

#### ACSL1

- **Related proteins** (co-abundance neighbors): PTGR1 (0.86); STRING partners: ACADM (0.728)
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 1. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. Several transcript variants enco…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.510); diabetes mellitus (0.501); diabetic neuropathy (0.404); neurodegenerative disease (0.368); menopause (0.334)
- **Europe PMC papers**: 4992
- **Why important**: ACSL1 provides the clearest link to fatty-acid entry into metabolism: it converts long-chain fatty acids into fatty acyl-CoA esters and participates in lipid biosynthesis and fatty-acid degradation. It is enhanced in liver, adipose tissue, and skeletal muscle, is associated with neutrophils, and has a large literature base including metabolic disease associations. It is also connected to ACADM by the only high-confidence STRING relationship reported for the module.
- **Conclusion**: Established evidence supports ACSL1 as a metabolically important fatty-acid activation enzyme and supports a prior relationship with ACADM. Its membership in this particular cross-tissue module may reflect coordinated hepatic lipid metabolism, but the co-abundance data do not establish direct regulation or a shared complex.

#### ACADM

- **Related proteins** (co-abundance neighbors): PTGR1 (0.81); STRING partners: ACSL1 (0.728)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA dehydrogenase medium chain. This gene encodes the medium-chain specific (C4 to C12 straight chain) acyl-Coenzyme A dehydrogenase. The homotetramer enzyme catalyzes the initial step of the mitochondrial fatty acid beta-oxidation pathway. Defects in this gene cause medium-chain acyl-CoA dehydrogenase deficiency, a disease characterized by hepatic dysfunction, fasting hypoglycemia, and encephalopathy, which can result in infant…
- **Diseases (Open Targets)**: medium chain acyl-CoA dehydrogenase deficiency (0.854); hereditary disease (0.516); rhabdomyolysis (0.370); short chain acyl-CoA dehydrogenase deficiency (0.349); Epileptic spasm (0.333)
- **Europe PMC papers**: 4795
- **Why important**: ACADM catalyzes the initial step of mitochondrial beta-oxidation for medium-chain fatty acids. It is liver enhanced, associated with hepatocytes, localized to mitochondria, and has a substantial literature base. Its disease association with medium-chain acyl-CoA dehydrogenase deficiency provides strong biological relevance to hepatic energy metabolism. The STRING relationship with ACSL1 gives the module a plausible connection between fatty-acid activation and oxidation.
- **Conclusion**: Established evidence supports ACADM as a hepatic mitochondrial fatty-acid oxidation enzyme and supports its known association with ACSL1. The proposed integration of ACADM with PTGR1, ASL, and DHRS1 is a module-level hypothesis rather than an established physical or regulatory pathway.

#### ASL

- **Related proteins** (co-abundance neighbors): PTGR1 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: argininosuccinate lyase. This gene encodes a member of the lyase 1 family. The encoded protein forms a cytosolic homotetramer and primarily catalyzes the reversible hydrolytic cleavage of argininosuccinate into arginine and fumarate, an essential step in the liver in detoxifying ammonia via the urea cycle. Mutations in this gene result in the autosomal recessive disorder argininosuccinic aciduria, or argininosuccinic acid…
- **Diseases (Open Targets)**: argininosuccinic aciduria (0.866); hereditary disease (0.508); neurodevelopmental disorder (0.436); dystonic disorder (0.370); Tremor (0.370)
- **Europe PMC papers**: 13702
- **Why important**: ASL is a liver-enriched cytosolic enzyme of the urea cycle and catalyzes argininosuccinate cleavage to arginine and fumarate. It is associated with hepatocytes, has a very large literature base, and is directly linked to argininosuccinic aciduria. Its inclusion broadens the module beyond lipid metabolism and suggests a possible connection between hepatic nitrogen disposal and broader intermediary metabolism.
- **Conclusion**: Established evidence supports ASL as a core hepatic urea-cycle enzyme with a clinically defined deficiency phenotype. Its co-abundance with the lipid and redox genes may reflect shared hepatocyte metabolic state, but no supplied evidence demonstrates a direct mechanistic interaction.

#### DHRS1

- **Related proteins** (co-abundance neighbors): PTGR1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dehydrogenase/reductase 1. This gene encodes a member of the short-chain dehydrogenases/reductases (SDR) family. The encoded enzyme contains a conserved catalytic domain and likely functions as an oxidoreductase. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Nov 2008].
- **Diseases (Open Targets)**: essential tremor (0.092); episodic kinesigenic dyskinesia 1 (0.085); hereditary geniospasm (0.083); young-onset Parkinson disease (0.080); hepatocellular carcinoma (0.080)
- **Europe PMC papers**: 208
- **Why important**: DHRS1 is the least characterized member of the module but is important because it occupies a distinct branch connected to the PTGR1 hub and is annotated as a short-chain dehydrogenase/reductase-family oxidoreductase. It is liver and esophagus enhanced, has several cell-type associations, and has a comparatively limited literature base relative to the other selected genes. Its relative lack of established partners or pathway enrichment makes it a useful candidate for testing whether the module contains a less-studied metabolic component.
- **Conclusion**: Established evidence supports DHRS1 as a liver-associated SDR-family oxidoreductase candidate, but its precise substrate and role in this module are not established by the supplied data. Its participation in coordinated hepatic lipid or redox metabolism is a testable hypothesis rather than a demonstrated function.

## Module 6

**Tissue pair**: circulatory_system and liver  
**Genes (16)**: ACBD5, AGT, PIK3AP1, CFI, C8G, ADAR, F12, L2HGDH, LCN2, BCKDHB, PDLIM2, ERC1, SCLY, SPR, STEAP3, F2

### Function

The most defensible interpretation is a liver-derived circulating protein module centered on hemostasis and innate immune regulation. F12 and F2 indicate intrinsic coagulation and thrombin-related biology, while CFI and C8G indicate complement regulation and complement-associated protein biology. AGT adds a liver-secreted blood-pressure and fluid-homeostasis component. These themes are supported by the gene annotations, the direct STRING relationships involving F2 (STRING DISEASES Kidney failure; within-query FDR = 0.0445), and the partial hu.MAP overlaps (hu.MAP huMAP3_14445.1) through (hu.MAP huMAP3_10101.1). However, no GO or KEGG term passed global correction, so this is an integrated functional interpretation rather than a globally significant enrichment result. The module also contains metabolic, RNA-processing, trafficking, cytoskeletal, and inflammatory genes, indicating that it is not a narrowly defined pathway module.

**Cell composition.** The module is strongly compatible with liver-derived circulating material and with hepatocyte biology. HPA identifies liver enrichment for F12, CFI, STEAP3, C8G, F2, AGT, SCLY, and BCKDHB, and hepatocyte enrichment for several of these genes. F12, CFI, C8G, F2, and AGT are secreted to blood, while LCN2 is secreted in other tissues. Thus, the shared circulatory_system–liver signal may partly reflect abundant plasma proteins produced by the liver rather than coordinated regulation within a single intracellular cell type. The module also contains genes associated with monocytes, dendritic cells, neutrophil-lineage cells, basophils, B cells, macrophages, and Kupffer cells. This raises a secondary possibility of shared blood or myeloid-cell contribution in tissue-derived samples. The presence of broadly expressed or intracellular genes such as ADAR, ACBD5, PDLIM2, ERC1, and metabolic enzymes argues against interpreting every member as a plasma-protein marker. HPA reports liver protein detection for part of the module and lack of detection for the remainder, consistent with a mixed secreted, hepatocyte, and cellular signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a small, concentrated set of high-confidence relationships: F2 connects with AGT, CFI, and F12, and the supplementary kidney-failure association includes F2, AGT, and LCN2 (STRING DISEASES Kidney failure; within-query FDR = 0.0445). These observations support a disease-relevant plasma-protein neighborhood but do not establish global enrichment or prove that every module edge is a physical interaction. hu.MAP independently places F12, CFI, C8G, and PDLIM2 together in two partially overlapping complexes (hu.MAP huMAP3_14445.1) and (hu.MAP huMAP3_14656.1). It also places F2, AGT, and LCN2 together in a broad protein association context (hu.MAP huMAP3_10678.1), with additional F2–AGT-containing complexes (hu.MAP huMAP3_07701.1) through (hu.MAP huMAP3_10101.1). The repeated F2–AGT overlap and the repeated F12–CFI–C8G overlap indicate that portions of the module recapitulate known protein-association neighborhoods. Most module genes have no recorded STRING partner or hu.MAP complex membership in the supplied evidence, so the full co-abundance structure is broader than the currently established physical-interaction structure.

**STRING interactions (score >= 0.7)**: 3 of 120 gene pairs: AGT–F2 (0.846); CFI–F2 (0.773); F12–F2 (0.88)
**STRING functional enrichment (supplementary, within-query FDR)**: DISEASES Kidney failure (FDR = 0.0445, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14445.1 (F12, CFI, C8G, PDLIM2; 4/18); huMAP3_14656.1 (F12, CFI, C8G, PDLIM2; 4/21); huMAP3_10678.1 (F2, AGT, LCN2; 3/71); huMAP3_07701.1 (F2, AGT; 2/22); huMAP3_09273.1 (F2, AGT; 2/28); huMAP3_08395.1 (F2, AGT; 2/43); huMAP3_09531.1 (F2, AGT; 2/47); huMAP3_10101.1 (F2, AGT; 2/49)

### Novelty

The module should not be called a newly discovered molecular complex or pathway on the present evidence. Its central coagulation, complement, and liver-secreted components overlap established biological knowledge, and several relationships are represented in STRING or hu.MAP. At the same time, the specific cross-tissue co-abundance configuration, including the links to metabolic, RNA-processing, trafficking, and cytoskeletal genes, may be a potentially useful systems-level observation. Absence of STRING or hu.MAP support for those links is not evidence of novelty; it may reflect co-expression, tissue composition, incomplete databases, or indirect regulation. A claim of new finding would require comparison with published tissue co-expression modules, independent cohorts, preservation analysis, and experimental or longitudinal validation.

**Hypothesis.** Hypothesis: the shared module reflects coordinated production and abundance of liver-derived circulating proteins that couple coagulation, complement control, vascular-fluid homeostasis, and tissue or innate-immune responses. In this model, hepatocyte-derived F12, F2, CFI, C8G, and AGT form the circulating core, while LCN2 and the myeloid-associated genes report inflammatory or blood-cell context. The intracellular metabolic and signaling genes may represent the hepatic cellular state that supports synthesis, secretion, redox balance, iron handling, and inflammatory communication. This hypothesis predicts that the module will track plasma protein abundance and liver or blood-cell composition more strongly than a single intracellular signaling pathway, and that its apparent conservation across the tissues will diminish after adjustment for plasma contamination, hepatocyte proportion, and immune-cell proportion.

### Important genes

#### F12

- **Related proteins** (co-abundance neighbors): ACBD5 (0.91), SCLY (0.87), BCKDHB (0.87), F2 (0.86), L2HGDH (0.84), C8G (0.84), ADAR (0.82), PDLIM2 (0.82); STRING partners: F2 (0.88)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14445.1, huMAP3_14656.1
- **Function (MyGene.info)**: coagulation factor XII. This gene encodes coagulation factor XII which circulates in blood as a zymogen. This single chain zymogen is converted to a two-chain serine protease with an heavy chain (alpha-factor XIIa) and a light chain. The heavy chain contains two fibronectin-type domains, two epidermal growth factor (EGF)-like domains, a kringle domain and a proline-rich domain, whereas the light chain contains only a cat…
- **Diseases (Open Targets)**: congenital factor XII deficiency (0.815); hereditary angioedema type 3 (0.777); hereditary angioedema (0.677); peptic ulcer disease (0.450); angioedema (0.407)
- **Europe PMC papers**: 100014
- **Why important**: F12 is the strongest network hub in the supplied module and connects the coagulation component to F2, the complement-associated genes CFI and C8G, and several liver or intracellular genes. Its established function is coagulation-factor XII activation, the plasma kallikrein–kinin cascade, intrinsic coagulation, proteolysis, and plasminogen activation. It is liver-enriched, secreted to blood, and has extensive literature and disease evidence involving factor XII deficiency and hereditary angioedema. Its hub position makes it a useful anchor for testing whether the module represents a circulating hemostatic program.
- **Conclusion**: Established evidence supports F12 as a central liver-derived plasma coagulation component and as an important organizing marker of the module. It is plausible, but not established, that F12 coordinates the non-coagulation genes through shared hepatic regulation or sample-level plasma abundance; the co-abundance network alone does not demonstrate such regulation.

#### F2

- **Related proteins** (co-abundance neighbors): F12 (0.86); STRING partners: AGT (0.846), CFI (0.773), F12 (0.88)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_07701.1, huMAP3_09273.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1
- **Function (MyGene.info)**: coagulation factor II, thrombin. This gene encodes the prothrombin protein (also known as coagulation factor II). This protein is proteolytically cleaved in multiple steps to form the activated serine protease thrombin. The activated thrombin enzyme plays an important role in thrombosis and hemostasis by converting fibrinogen to fibrin during blood clot formation, by stimulating platelet aggregation, and by activating additional …
- **Diseases (Open Targets)**: congenital prothrombin deficiency (0.827); thrombophilia due to thrombin defect (0.738); venous thromboembolism (0.727); deep vein thrombosis (0.690); blood coagulation disease (0.670)
- **Europe PMC papers**: 109299
- **Why important**: F2 encodes prothrombin, the precursor of thrombin, and is directly connected in STRING to F12, AGT, and CFI. It has the highest literature volume among the module genes in the supplied evidence and strong disease associations with prothrombin deficiency, thrombophilia, venous thromboembolism, and other coagulation disorders. F2 also recurs across several hu.MAP complexes (hu.MAP huMAP3_10678.1) through (hu.MAP huMAP3_10101.1), making it the clearest bridge between the known coagulation neighborhood and the broader plasma-protein association context.
- **Conclusion**: Established evidence identifies F2 as a core hemostatic and circulating-plasma component with strong network and literature support. The repeated association with AGT and CFI supports a shared plasma-protein context, but does not establish a direct functional pathway connecting coagulation to renin–angiotensin or complement regulation in this module.

#### CFI

- **Related proteins** (co-abundance neighbors): C8G (0.87), AGT (0.83), LCN2 (0.81); STRING partners: F2 (0.773)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14445.1, huMAP3_14656.1
- **Function (MyGene.info)**: complement factor I. This gene encodes a serine proteinase that is essential for regulating the complement cascade. The encoded preproprotein is cleaved to produce both heavy and light chains, which are linked by disulfide bonds to form a heterodimeric glycoprotein. This heterodimer can cleave and inactivate the complement components C4b and C3b, and it prevents the assembly of the C3 and C5 convertase enzymes. Defect…
- **Diseases (Open Targets)**: complement factor I deficiency (0.798); atypical hemolytic-uremic syndrome with I factor anomaly (0.795); age-related macular degeneration (0.782); atypical hemolytic-uremic syndrome (0.639); macular degeneration (0.571)
- **Europe PMC papers**: 14453
- **Why important**: CFI is a liver-enriched secreted regulator of complement that cleaves and inactivates C4b and C3b and limits convertase assembly. It connects in the module to C8G, AGT, and LCN2, has a high-confidence STRING relationship with F2, and recurs with F12, C8G, and PDLIM2 in hu.MAP complexes (hu.MAP huMAP3_14445.1) and (hu.MAP huMAP3_14656.1). Its disease associations include complement factor I deficiency and atypical hemolytic-uremic syndrome, and it has substantial literature support.
- **Conclusion**: Established evidence supports CFI as the principal complement-regulatory component and as a biologically meaningful link between the coagulation-centered and innate-immune portions of the module. The hypothesis that CFI is functionally coordinated with F2 and F12 in this tissue pair remains to be tested; the available data support association rather than causal cooperation.

#### AGT

- **Related proteins** (co-abundance neighbors): CFI (0.83); STRING partners: F2 (0.846)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_07701.1, huMAP3_09273.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1
- **Function (MyGene.info)**: angiotensinogen. The protein encoded by this gene, pre-angiotensinogen or angiotensinogen precursor, is expressed in the liver and is cleaved by the enzyme renin in response to lowered blood pressure. The resulting product, angiotensin I, is then cleaved by angiotensin converting enzyme (ACE) to generate the physiologically active enzyme angiotensin II. The protein is involved in maintaining blood pressure, body f…
- **Diseases (Open Targets)**: renal tubular dysgenesis (0.732); renal tubular dysgenesis of genetic origin (0.691); essential hypertension (0.633); hypertensive disorder (0.619); cardiovascular disorder (0.503)
- **Europe PMC papers**: 65392
- **Why important**: AGT is liver-enriched and secreted to blood, and it supplies the precursor for the renin–angiotensin system that regulates blood pressure, fluid balance, and aldosterone biology. It is directly associated with F2 in STRING and repeatedly co-occurs with F2 in hu.MAP complexes (hu.MAP huMAP3_10678.1) through (hu.MAP huMAP3_10101.1). AGT has extensive literature and disease evidence involving hypertension, cardiovascular disease, and renal developmental disorders, making it an important physiological and clinical marker of the module.
- **Conclusion**: Established evidence supports AGT as a liver-derived circulatory homeostasis component that broadens the module beyond coagulation and complement. Its association with F2 may reflect a shared plasma or liver-abundance program; a direct mechanistic interaction between AGT and the coagulation machinery is not established by the supplied evidence.

#### C8G

- **Related proteins** (co-abundance neighbors): CFI (0.87), F12 (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14445.1, huMAP3_14656.1
- **Function (MyGene.info)**: complement C8 gamma chain. The protein encoded by this gene belongs to the lipocalin family. It is one of the three subunits that constitutes complement component 8 (C8), which is composed of a disulfide-linked C8 alpha-gamma heterodimer and a non-covalently associated C8 beta chain. C8 participates in the formation of the membrane attack complex (MAC) on bacterial cell membranes. While subunits alpha and beta play a role i…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.370); complement deficiency (0.370); immunodeficiency disease (0.148); COVID-19 (0.012); open-angle glaucoma (0.010)
- **Europe PMC papers**: 730
- **Why important**: C8G is liver-enriched, hepatocyte-enriched, and secreted to blood. It is a subunit of complement C8 and belongs to the lipocalin family, while its module position links it to CFI and F12. It recurs with F12, CFI, and PDLIM2 in the two hu.MAP complexes (hu.MAP huMAP3_14445.1) and (hu.MAP huMAP3_14656.1). Its literature volume is smaller than that of F2, F12, or AGT, but its functional specificity and position at the complement–coagulation interface make it informative.
- **Conclusion**: Established evidence supports C8G as a complement-associated liver-secreted marker that helps define the module's circulating innate-immune component. Its network placement suggests coordinated abundance with F12 and CFI, but the data do not show that C8G directly regulates coagulation or explains the cross-tissue conservation.

## Module 7

**Tissue pair**: circulatory_system and liver  
**Genes (10)**: AMBP, AP3S1, DAZAP1, DSG2, EXOC4, LMNB2, NAA15, NID1, RECQL, UBTF

### Function

The module does not have a statistically supported GO or KEGG functional label: no GO or KEGG term passed global correction. Its structure is a sparse co-abundance network centered on AMBP, with the remaining genes forming weakly connected links to AMBP or to DSG2 and RECQL. The individual annotations suggest a mixed biological signal rather than one established pathway: AMBP is a secreted plasma glycoprotein involved in transport and inflammatory or protease-inhibitory biology; DSG2 represents epithelial cell-cell adhesion and desmosomes; NID1 represents basement-membrane and cell-matrix interactions; RECQL represents DNA repair and replication-fork maintenance; and AP3S1 and EXOC4 represent vesicle trafficking and exocytosis. LMNB2, UBTF, and NAA15 represent nuclear-envelope, ribosomal-transcription, and protein-maturation functions. Together, these annotations are compatible with a composite tissue or cellular-composition signal, but they do not establish a single molecular pathway.

**Cell composition.** The module is compositionally mixed. AMBP is a liver-enriched hepatocyte-associated protein secreted to blood, while NID1 is an extracellular-matrix protein. The other genes are predominantly intracellular and broadly distributed according to HPA, including nuclear, nucleolar, cytosolic, vesicular, and junctional proteins. Only a minority of the genes are secreted, so this is not primarily a plasma-protein module. The HPA profile does not indicate a coherent immune-cell module: most genes have low immune-cell specificity, although individual genes show associations with basophils, monocytes, myeloid dendritic cells, or other blood-cell populations. The liver protein-detection pattern and the hepatocyte annotation for AMBP support a liver contribution, but the shared circulatory-system and liver signal could also reflect blood exposure, extracellular material, epithelial or stromal components, or shared cellular composition. The heterogeneous tissue and single-cell annotations argue against interpreting the module as a uniform liver-specific cellular program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction among module gene pairs met the supplied high-confidence criterion, and no STRING functional-enrichment result was reported. No hu.MAP complex contained multiple module members. Therefore, the co-abundance relationships are not corroborated here by known high-confidence physical interactions or a shared curated complex. AMBP is the central co-abundance hub, but its network position should not be treated as proof that it physically binds the genes connected to it. The DSG2 to EXOC4 and RECQL to LMNB2 links are biologically suggestive because they connect epithelial trafficking or junctional biology and nuclear genome-maintenance biology, respectively, but the supplied resources do not establish these as module-level complexes.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a newly discovered molecular complex or pathway. The absence of high-confidence STRING links and multi-member hu.MAP complexes means that the specific co-abundance pattern is not explained by the supplied interaction catalogs, but absence from those catalogs alone does not prove biological novelty. The mixed annotations, sparse graph, lack of globally significant GO or KEGG enrichment, and strong AMBP-centered organization are more consistent with a potentially novel sample-level co-abundance pattern or a composition-related signal than with a previously characterized coherent mechanism. Demonstrating novelty would require independent replication, adjustment for cell composition and circulating-protein contamination, and validation at the protein or mechanistic level.

**Hypothesis.** Hypothesis: the shared signal may arise from coordinated representation of liver-derived circulating material together with epithelial or extracellular-matrix material and a background of broadly expressed intracellular genes. In this model, hepatocyte-associated secretion contributes AMBP, extracellular or stromal representation contributes NID1, epithelial junction and vesicle biology contributes DSG2 and EXOC4, and variation in cellular stress or proliferative state contributes genes such as RECQL, LMNB2, UBTF, and NAA15. This is a hypothesis about sample composition and coordinated tissue state, not an established pathway. It should be tested by cell-composition deconvolution, exclusion or adjustment of plasma proteins, independent cohorts, and orthogonal measurements of the relevant proteins and cell populations.

### Important genes

#### AMBP

- **Related proteins** (co-abundance neighbors): NID1 (0.89), DAZAP1 (0.88), AP3S1 (0.87), RECQL (0.82), UBTF (0.81), NAA15 (0.81), DSG2 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alpha-1-microglobulin/bikunin precursor. This gene encodes a complex glycoprotein secreted in plasma. The precursor is proteolytically processed into distinct functioning proteins: alpha-1-microglobulin, which belongs to the superfamily of lipocalin transport proteins and may play a role in the regulation of inflammatory processes, and bikunin, which is a urinary trypsin inhibitor belonging to the superfamily of Kunitz-type protease inhi…
- **Diseases (Open Targets)**: systemic lupus erythematosus (0.086); ovarian neoplasm (0.072); posterior cortical atrophy (0.064); breast carcinoma (0.060); diabetes mellitus (0.060)
- **Europe PMC papers**: 1653
- **Why important**: AMBP is the strongest network hub in the module and is the clearest biological anchor. It is liver-enriched and hepatocyte-associated by HPA, secreted to blood, and encodes a precursor yielding alpha-one-microglobulin and bikunin, linking the module to circulating transport, inflammatory regulation, and protease inhibition. Its disease associations and extensive literature make it the best-supported candidate for a liver-to-circulation component, while its many co-abundance links may also reflect abundance or sample-composition effects.
- **Conclusion**: Established evidence supports AMBP as a liver-derived secreted plasma component and as the principal co-abundance hub. It is plausible, but unproven, that AMBP helps drive the shared tissue signal; the network does not demonstrate direct molecular interactions with its neighbors.

#### DSG2

- **Related proteins** (co-abundance neighbors): EXOC4 (0.84), AMBP (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cell Junctions; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: desmoglein 2. This gene encodes a member of the desmoglein family and cadherin cell adhesion molecule superfamily of proteins. Desmogleins are calcium-binding transmembrane glycoprotein components of desmosomes, cell-cell junctions between epithelial, myocardial, and other cell types. The encoded preproprotein is proteolytically processed to generate the mature glycoprotein. This gene is present in a gene clust…
- **Diseases (Open Targets)**: arrhythmogenic right ventricular dysplasia 10 (0.812); arrhythmogenic right ventricular cardiomyopathy (0.781); dilated cardiomyopathy 1BB (0.714); familial isolated dilated cardiomyopathy (0.615); Abnormality of the cardiovascular system (0.552)
- **Europe PMC papers**: 3811
- **Why important**: DSG2 is connected to AMBP and EXOC4 and is the module's clearest epithelial-junction marker. HPA places it in cell junctions and shows tissue enhancement in intestine and parathyroid gland, with expression in several epithelial cell types. Its established desmosomal adhesion function and strong disease associations with arrhythmogenic and dilated cardiomyopathy make it important for interpreting the circulatory-system component.
- **Conclusion**: Established evidence supports DSG2 as an epithelial desmosome and cell-adhesion protein with cardiovascular disease relevance. Its presence may indicate epithelial or cardiovascular cellular composition, but a functional connection to AMBP or EXOC4 within this module remains a hypothesis.

#### NID1

- **Related proteins** (co-abundance neighbors): AMBP (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nidogen 1. This gene encodes a member of the nidogen family of basement membrane glycoproteins. The protein interacts with several other components of basement membranes, and may play a role in cell interactions with the extracellular matrix. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.425); focal epilepsy (0.259); Hemiparesis (0.259); Hydrocephalus (0.259); placental retention (0.233)
- **Europe PMC papers**: 1838
- **Why important**: NID1 is directly linked to AMBP and provides the principal extracellular-matrix interpretation. It is a basement-membrane glycoprotein involved in cell-matrix adhesion and integrin-related signaling, is secreted to extracellular matrix, and has HPA associations with placenta, fibroblasts, stromal populations, and several monocyte or dendritic-cell categories. Its substantial literature and extracellular location make it useful for distinguishing a tissue-matrix or stromal contribution from a purely hepatocyte-centered interpretation.
- **Conclusion**: Established evidence supports NID1 as a basement-membrane and cell-matrix component. Its co-abundance with AMBP could reflect shared extracellular material or tissue composition, but the module does not establish a direct NID1-AMBP mechanism.

#### RECQL

- **Related proteins** (co-abundance neighbors): LMNB2 (0.84), AMBP (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RecQ like helicase. The protein encoded by this gene is a member of the RecQ DNA helicase family. DNA helicases are enzymes involved in various types of DNA repair, including mismatch repair, nucleotide excision repair and direct repair. The encoded protein is involved in the processing of Holliday junctions, the suppression of sister chromatid exchanges, telomere maintenance, and is required for genotoxic stress res…
- **Diseases (Open Targets)**: RECON progeroid syndrome (0.595); hereditary neoplastic syndrome (0.505); obesity disorder (0.404); myofibrillar myopathy 8 (0.334); hereditary breast ovarian cancer syndrome (0.328)
- **Europe PMC papers**: 954
- **Why important**: RECQL is one of the two genes forming a distinct local edge with LMNB2 and is also linked to AMBP. It encodes a RecQ helicase involved in DNA repair, homologous recombination, replication, telomere maintenance, and genotoxic-stress resistance. Its substantial literature and cancer and progeroid-disease associations make it the most informative marker of a nuclear genome-maintenance state in an otherwise mixed module.
- **Conclusion**: Established evidence supports RECQL as a DNA-repair and genome-stability factor. The RECQL-LMNB2 connection could reflect coordinated nuclear or cellular-state variation, but it is not supported here as a curated physical complex or as a causal component of the AMBP-centered signal.

#### EXOC4

- **Related proteins** (co-abundance neighbors): DSG2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exocyst complex component 4. The protein encoded by this gene is a component of the exocyst complex, a multiple protein complex essential for targeting exocytic vesicles to specific docking sites on the plasma membrane. Though best characterized in yeast, the component proteins and functions of exocyst complex have been demonstrated to be highly conserved in higher eukaryotes. At least eight components of the exocyst complex,…
- **Diseases (Open Targets)**: alcohol drinking (0.484); intelligence (0.394); neurodegenerative disease (0.356); major depressive disorder (0.353); mathematical ability (0.322)
- **Europe PMC papers**: 582
- **Why important**: EXOC4 is connected to DSG2 and supplies a vesicle-docking and exocytosis interpretation that can bridge epithelial junction biology with extracellular release. It is a component of the conserved exocyst complex and participates in targeting secretory vesicles to the plasma membrane. Its HPA profile is broadly nonspecific, so its importance comes mainly from its local network position and established trafficking function rather than tissue restriction.
- **Conclusion**: Established evidence supports EXOC4 as an exocyst component involved in exocytosis and membrane delivery. It may help explain coordinated abundance of DSG2 and secreted or membrane-associated material, but that mechanistic interpretation remains hypothetical because no corresponding STRING or hu.MAP support is present.

## Module 8

**Tissue pair**: circulatory_system and liver  
**Genes (23)**: AMPD2, ATP2A2, DCTN1, DIAPH1, EPS15L1, FLOT1, GALNT2, GGH, HACD2, HYOU1, ITGB1, ABCB1, NEK9, PACSIN3, GART, QNG1, SEC23IP, LARS1, SARS1, YARS1, UGGT1, UMPS, UTRN

### Function

The strongest functional interpretation is a membrane-associated trafficking, adhesion, and cellular homeostasis module, with a possible link to regulation of neurotransmitter transport. (GO:BP regulation of neurotransmitter transport; q_global = 0.0455) is the only GO/KEGG term that passed global correction and implicates ATP2A2, FLOT1, and ITGB1. ATP2A2 supports calcium handling, FLOT1 supports membrane-domain organization and vesicle trafficking, and ITGB1 supports adhesion, phagocytosis, hemostasis, and cellular signaling. Additional gene annotations indicate endocytosis and endosomal transport, ER protein folding and quality control, ER-to-Golgi trafficking, glycosylation, lipid synthesis, nucleotide metabolism, and translation. These annotations suggest a cellular logistics and membrane-function program more strongly than a narrowly defined neurotransmitter pathway. The network is highly hub-and-spoke, with ABCB1 connected to many otherwise weakly connected genes, so the apparent functional unity may reflect coordinated abundance or shared cellular context rather than direct physical interaction.

**Cell composition.** The module is not dominated by secreted plasma proteins: only a minority are annotated as secreted, and most genes have low tissue specificity. Many genes are instead broadly expressed intracellular or membrane proteins, including transport, translation, nucleotide-metabolism, ER, Golgi, and cytoskeletal components. HPA nevertheless shows cell-type enhancement for most genes, with signals in neutrophils, cardiomyocytes, myonuclei, neurons, and reproductive cell types. Several genes also show enrichment in neutrophils or monocyte populations, although overall immune-cell specificity is low. Liver protein detection is common among the genes, whereas the circulatory-system comparison has no matching HPA tissue-level protein readout. Thus, the shared module could partly reflect broad housekeeping biology combined with shared cellular composition, including blood-cell or vascular-associated contributions, rather than a liver-specific secreted program.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulation of neurotransmitter transport | 0.0455 | ATP2A2, FLOT1, ITGB1 |

### STRING and hu.MAP

STRING supports a limited set of established relationships. GART–UMPS is a strong association between purine and pyrimidine biosynthetic machinery, HYOU1–UGGT1 links ER stress or folding biology with glycoprotein quality control, and LARS1, SARS1, and YARS1 form a connected aminoacyl-tRNA-synthetase group. These relationships support coherent submodules for nucleotide metabolism, ER proteostasis, and translation, but STRING reports no functional enrichment for the module as a whole. hu.MAP provides partial complex support: UMPS and GART co-occur in (hu.MAP huMAP3_10240.1), while UMPS and ATP2A2 co-occur in (hu.MAP huMAP3_07170.1). Because each complex contains only a subset of module genes, the hu.MAP evidence supports local biochemical relationships rather than one unified complex. Most co-abundance edges are not independently supported by STRING or hu.MAP, so they should be treated as network associations rather than established physical interactions.

**STRING interactions (score >= 0.7)**: 5 of 253 gene pairs: GART–UMPS (0.956); HYOU1–UGGT1 (0.791); LARS1–SARS1 (0.933); LARS1–YARS1 (0.98); SARS1–YARS1 (0.941)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10240.1 (UMPS, GART; 2/12); huMAP3_07170.1 (UMPS, ATP2A2; 2/14)

### Novelty

This module may be a novel tissue-pair co-abundance pattern, but the available evidence does not establish a new molecular pathway or complex. The globally corrected enrichment is limited to (GO:BP regulation of neurotransmitter transport; q_global = 0.0455), and the module combines several recognizable cellular programs rather than matching a single known canonical system. Some relationships are already known through STRING and hu.MAP, especially the GART–UMPS pair, the ER quality-control pair involving HYOU1 and UGGT1, the aminoacyl-tRNA-synthetase cluster, and the partial complexes in (hu.MAP huMAP3_10240.1) and (hu.MAP huMAP3_07170.1). Conversely, the broad ABCB1-centered co-abundance pattern is not explained by the available interaction resources. This makes the network configuration potentially interesting, but absence from those resources alone cannot prove biological novelty. Replication in independent cohorts, cell-composition adjustment, and experimental testing would be needed to distinguish a reproducible conserved module from a shared-expression or sample-composition effect.

**Hypothesis.** Hypothesis: the module represents a coordinated membrane and secretory-cellular homeostasis program in which ABCB1-associated membrane organization is co-regulated with calcium handling, adhesion, endocytosis, ER quality control, glycosylation, and biosynthetic capacity. In liver and circulatory-system samples, this coordination may arise from shared vascular, blood-cell, or membrane-rich cellular populations. ATP2A2, FLOT1, and ITGB1 may provide the most direct connection to the globally corrected neurotransmitter-transport term, while the nucleotide, aminoacylation, and ER-folding genes may represent supporting metabolic and proteostatic demands. This is a mechanistic model rather than an established causal pathway.

### Important genes

#### ABCB1

- **Related proteins** (co-abundance neighbors): UGGT1 (0.95), ATP2A2 (0.91), UMPS (0.91), SARS1 (0.87), GALNT2 (0.87), FLOT1 (0.86), QNG1 (0.85), GART (0.84), DIAPH1 (0.83), HYOU1 (0.83), SEC23IP (0.82), DCTN1 (0.82), YARS1 (0.81), GGH (0.81), ITGB1 (0.81), LARS1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP binding cassette subfamily B member 1. The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily ar…
- **Diseases (Open Targets)**: response to tramadol (0.547); encephalopathy, acute transient (0.416); acute myeloid leukemia (0.391); inflammatory bowel disease (0.390); portal hypertension (0.357)
- **Europe PMC papers**: 20196
- **Why important**: ABCB1 is the dominant network hub and links membrane transport with genes involved in ER, Golgi, nucleotide, translation, cytoskeletal, and adhesion biology. Its established function as an ATP-dependent drug-efflux transporter and its plasma-membrane localization make it a plausible organizer or marker of the membrane-associated component. It has extensive disease and pharmacology literature, including links to xenobiotic handling and portal hypertension.
- **Conclusion**: Established: ABCB1 is a membrane ABC transporter with broad transport and xenobiotic-related functions and is highly central in this co-abundance network. Hypothesis: its hub position may reflect coordinated membrane abundance or cellular composition rather than direct control of the other module genes.

#### ATP2A2

- **Related proteins** (co-abundance neighbors): ABCB1 (0.91), HACD2 (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07170.1
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darie…
- **Diseases (Open Targets)**: Darier disease (0.823); acrokeratosis verruciformis (0.663); neurodegenerative disease (0.507); hereditary disease (0.416); schizophrenia (0.406)
- **Europe PMC papers**: 9327
- **Why important**: ATP2A2 is one of the genes in the sole globally corrected term, (GO:BP regulation of neurotransmitter transport; q_global = 0.0455), and encodes a SERCA calcium pump involved in intracellular calcium handling and contraction-relaxation biology. It is enriched in heart muscle, skeletal muscle, and tongue, and is connected in the module to ABCB1 and HACD2. It also has substantial literature and established disease associations, including Darier disease.
- **Conclusion**: Established: ATP2A2 supports calcium transport and is part of (GO:BP regulation of neurotransmitter transport; q_global = 0.0455). Hypothesis: its co-abundance with membrane, lipid, and trafficking genes may indicate coordinated calcium-dependent membrane homeostasis, but the module does not prove that ATP2A2 regulates neurotransmitter transport in these tissues.

#### ITGB1

- **Related proteins** (co-abundance neighbors): ABCB1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is another member of (GO:BP regulation of neurotransmitter transport; q_global = 0.0455) and encodes a broadly important integrin subunit involved in cell adhesion, recognition, angiogenesis, phagocytosis, hemostasis, immune response, and tissue repair. Its plasma-membrane and focal-adhesion localization provides a functional bridge between membrane organization and tissue or blood-cell interactions. It also has extensive literature and disease links involving inflammatory and autoimmune biology.
- **Conclusion**: Established: ITGB1 is a multifunctional adhesion receptor subunit and contributes to (GO:BP regulation of neurotransmitter transport; q_global = 0.0455). Hypothesis: ITGB1 may help explain the shared module through vascular, platelet, immune-cell, or adhesion-related cellular composition, rather than through a direct neurotransmitter transport mechanism.

#### LARS1

- **Related proteins** (co-abundance neighbors): ABCB1 (0.80); STRING partners: SARS1 (0.933), YARS1 (0.98)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: leucyl-tRNA synthetase 1. This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals w…
- **Diseases (Open Targets)**: infantile liver failure syndrome 1 (0.670); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.510); Global developmental delay (0.119); sensorineural hearing loss disorder (0.119); Generalized-onset seizure (0.118)
- **Europe PMC papers**: 267
- **Why important**: LARS1 is part of the STRING-supported aminoacyl-tRNA-synthetase cluster with SARS1 and YARS1. It performs cytosolic leucine-tRNA charging, participates in a multisynthetase complex, and has an established association with infantile liver failure syndrome. Its network position connects the translation-related STRING cluster to the broader ABCB1-centered module.
- **Conclusion**: Established: LARS1 supports protein translation and has known disease relevance, while its relationships with SARS1 and YARS1 are supported by STRING. Hypothesis: the cluster may mark increased translational demand or general biosynthetic activity in the cells contributing to the shared module.

#### UMPS

- **Related proteins** (co-abundance neighbors): ABCB1 (0.91); STRING partners: GART (0.956)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10240.1, huMAP3_07170.1
- **Function (MyGene.info)**: uridine monophosphate synthetase. This gene encodes a uridine 5'-monophosphate synthase. The encoded protein is a bifunctional enzyme that catalyzes the final two steps of the de novo pyrimidine biosynthetic pathway. The first reaction is carried out by the N-terminal enzyme orotate phosphoribosyltransferase which converts orotic acid to orotidine-5'-monophosphate. The terminal reaction is carried out by the C-terminal enzyme OMP …
- **Diseases (Open Targets)**: orotic aciduria (0.773); coronary artery disorder (0.507); Intellectual disability (0.462); open-angle glaucoma (0.381); Abnormality of the skeletal system (0.374)
- **Europe PMC papers**: 965
- **Why important**: UMPS is a pyrimidine-biosynthesis enzyme and forms a strong STRING-supported relationship with GART. It also appears with GART in (hu.MAP huMAP3_10240.1) and with ATP2A2 in (hu.MAP huMAP3_07170.1), making it one of the few genes that connects independent biochemical and complex-level evidence. Its established disease association with orotic aciduria and its relevance to nucleotide production add biological and clinical importance.
- **Conclusion**: Established: UMPS catalyzes the final steps of de novo UMP synthesis and has support from STRING and hu.MAP relationships. Hypothesis: its presence may reflect nucleotide demand associated with membrane turnover, protein production, or the cellular populations represented in the samples, rather than a specific liver-circulatory pathway.

#### GART

- **Related proteins** (co-abundance neighbors): ABCB1 (0.84); STRING partners: UMPS (0.956)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_10240.1
- **Function (MyGene.info)**: phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase. The protein encoded by this gene is a trifunctional polypeptide. It has phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase activity which is required for de novo purine biosynthesis. This enzyme is highly conserved in vertebrates. Alternative splicing of this gene results in two transcript variants encoding different isoforms.…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.606); mesothelioma (0.584); malignant pleural mesothelioma (0.557); adenocarcinoma (0.486); anaplastic lung carcinoma (0.462)
- **Europe PMC papers**: 1890
- **Why important**: GART is a multifunctional enzyme in de novo purine biosynthesis and is the partner of UMPS in the strongest STRING relationship in the module. It also appears with UMPS in (hu.MAP huMAP3_10240.1). Its role in producing purine intermediates gives the module a defined biosynthetic component, and it has a substantial literature including cancer-related associations.
- **Conclusion**: Established: GART supports de novo purine production and has convergent STRING and hu.MAP support with UMPS. Hypothesis: the GART–UMPS pairing may indicate coordinated nucleotide biosynthesis within the module, but it does not demonstrate that nucleotide metabolism is the primary function of the entire network.

## Module 9

**Tissue pair**: circulatory_system and liver  
**Genes (5)**: ARSA, LRTM3, NID2, NSFL1C, TBL2

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING functional enrichment. Therefore, the module does not support a statistically established pathway-level function from enrichment analysis. Its gene-level biology is heterogeneous: LRTM3 is a plasma-membrane leucine-rich-repeat transmembrane protein, NID2 is an extracellular-matrix basement-membrane adhesion protein, TBL2 is a beta-transducin-family regulatory protein linked in the supplied annotation to endoplasmic-reticulum stress, glucose starvation, and hypoxia responses, NSFL1C is a cofactor for NSF and p97 in membrane trafficking and Golgi reassembly, and ARSA is a lysosomal or Golgi-associated sulfatase involved in sphingolipid degradation. The co-abundance pattern is therefore more consistent with a tissue- or cell-state-associated module involving membrane, matrix, trafficking, and lipid-processing biology than with a single established biochemical pathway. The absence of globally significant enrichment does not invalidate the module.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: only NID2 is annotated as secreted to the extracellular matrix, while ARSA is annotated as intracellular and membrane-associated. LRTM3 is located at the plasma membrane, TBL2 in the cytosol, and NSFL1C in the nucleoplasm. The HPA profile argues against a blood-cell-driven module because the genes have low immune-cell specificity or are not detected in immune cells, and no enriched blood-cell category is reported. Instead, the profile is unusual for a circulatory-system and liver module because several genes are enriched in reproductive tissues or germ-cell states, especially testis and spermatogenic cell types, while NID2 is enhanced in ovary and placenta and other genes show broad or cell-type-enhanced expression. Liver protein detection is reported for NSFL1C, ARSA, and NID2 is not detected in liver, whereas the circulatory-system HPA tissue has no matching protein-detection data. The shared module may therefore reflect a shared cellular program, sample composition, or coordinated expression of relatively specialized genes rather than a blood-plasma signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and no STRING functional enrichment was found. No hu.MAP complex contains multiple module members. Thus, the observed co-abundance edges are not supported by established high-confidence physical interactions or a recognized multiprotein complex in these resources. The lack of database support suggests that the module captures co-expression or co-abundance relationships rather than a demonstrated physical assembly. It also means that the network should not be interpreted as evidence that all members act in one complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported co-abundance association because none of its within-module relationships are present in the supplied STRING or hu.MAP evidence. However, that absence alone does not establish biological novelty: database incompleteness, tissue-specific regulation, indirect co-regulation, and sample-composition effects are alternative explanations. The heterogeneous annotations, reproductive-cell enrichment, absence of globally significant GO or KEGG enrichment, and lack of known physical interactions make this best described as a potentially novel tissue-pair co-abundance pattern requiring independent validation, not as a newly established pathway or mechanism.

**Hypothesis.** Hypothesis: this module reflects coordinated regulation of membrane and extracellular-interface biology together with intracellular trafficking and lipid-sulfate processing in a shared cell-state or tissue-composition component present across the circulatory-system and liver datasets. LRTM3 may mark the co-abundance state at the network level, NID2 may represent extracellular-matrix or basement-membrane context, NSFL1C may connect the pattern to membrane-trafficking capacity, TBL2 may link it to cellular stress or metabolic signaling, and ARSA may indicate altered lysosomal or sphingolipid turnover. The reproductive-tissue and germ-cell HPA pattern raises the alternative hypothesis that the module is driven by a shared specialized cell population or technical composition rather than by a liver-circulation mechanism. This hypothesis should be tested with independent cohorts, cell-type-aware analysis, and experimental assessment of whether the genes change together under relevant stress, trafficking, matrix, or lipid-metabolism conditions.

### Important genes

#### LRTM3

- **Related proteins** (co-abundance neighbors): NSFL1C (0.82), TBL2 (0.81), ARSA (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: leucine rich repeat transmembrane protein 3
- **Diseases (Open Targets)**: atrial fibrillation (0.178); ankylosing spondylitis (0.140); glomerulonephritis (0.069); chronic atrophic gastritis (0.063); hemorrhage (0.062)
- **Europe PMC papers**: 0
- **Why important**: LRTM3 is the most central node in the supplied co-abundance subgraph, connecting to NSFL1C, TBL2, and ARSA. Its plasma-membrane localization and testis and early-spermatid enrichment make it a useful marker of the module's distinctive cellular context. It has no Europe PMC papers in the fact sheet, so it is comparatively understudied. Open Targets links it to atrial fibrillation, ankylosing spondylitis, glomerulonephritis, chronic atrophic gastritis, and hemorrhage, but these associations are not mechanistic proof.
- **Conclusion**: Established evidence supports LRTM3 as the network hub and as a specialized plasma-membrane, germ-cell-enriched gene. Its centrality makes it important for validating the module, but its biological role in this module remains a hypothesis because there is no reported GO or KEGG enrichment, no STRING partner, no hu.MAP complex, and little literature.

#### TBL2

- **Related proteins** (co-abundance neighbors): NID2 (0.85), LRTM3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transducin beta like 2. This gene encodes a member of the beta-transducin protein family. Most proteins of the beta-transducin family are involved in regulatory functions. This protein is possibly involved in some intracellular signaling pathway. This gene is deleted in Williams-Beuren syndrome, a developmental disorder caused by deletion of multiple genes at 7q11.23. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: gout (0.305); physical activity (0.280); type 2 diabetes mellitus (0.257); Abnormality of the skeletal system (0.243); diabetes mellitus (0.200)
- **Europe PMC papers**: 346
- **Why important**: TBL2 is connected to NID2 and LRTM3 and has a comparatively substantial literature base. The supplied annotation places it in a beta-transducin-family regulatory group and associates it with endoplasmic-reticulum unfolded-protein response, glucose-starvation response, and hypoxia response. Its testis-enhanced and spermatogenic-cell group enrichment may help explain the unusual tissue-pair pattern. Open Targets associations include gout, physical activity, type two diabetes mellitus, skeletal-system abnormality, and diabetes mellitus.
- **Conclusion**: Established evidence supports TBL2 as a plausible stress- and metabolism-related regulator within the module, but not as the cause of the co-abundance pattern. Its connection to LRTM3 and NID2 is network evidence rather than proof of direct physical interaction. A stress-responsive or metabolic role in the module is a hypothesis requiring validation.

#### NID2

- **Related proteins** (co-abundance neighbors): TBL2 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nidogen 2. This gene encodes a member of the nidogen family of basement membrane proteins. This protein is a cell-adhesion protein that binds collagens I and IV and laminin and may be involved in maintaining the structure of the basement membrane.[provided by RefSeq, Jun 2010].
- **Diseases (Open Targets)**: hearing loss disorder (0.474); benign colon neoplasm (0.439); presbycusis (0.436); sensorineural hearing loss disorder (0.436); Tinnitus (0.360)
- **Europe PMC papers**: 1495
- **Why important**: NID2 is the module's extracellular-matrix component and is connected to TBL2. Its known annotation describes basement-membrane organization and adhesion through binding to collagens and laminin. HPA identifies tissue enhancement in ovary and placenta and cell-type enhancement in several stromal, epithelial, adipocyte, and cardiac contexts; it is annotated as secreted to the extracellular matrix. Its literature volume is substantial, and Open Targets associates it with hearing-loss-related disorders and benign colon neoplasm.
- **Conclusion**: Established evidence supports NID2 as a basement-membrane and cell-matrix marker that could report tissue architecture or stromal composition. It is not evidence for a shared liver-circulation complex, especially because no hu.MAP or STRING support is present. Its participation in a coordinated matrix-trafficking program is a hypothesis.

#### ARSA

- **Related proteins** (co-abundance neighbors): LRTM3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: arylsulfatase A. The protein encoded by this gene hydrolyzes cerebroside sulfate to cerebroside and sulfate. Defects in this gene lead to metachromatic leucodystrophy (MLD), a progressive demyelination disease which results in a variety of neurological symptoms and ultimately death. Alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Dec 2010].
- **Diseases (Open Targets)**: metachromatic leukodystrophy (0.879); metachromatic leukodystrophy, juvenile form (0.782); metachromatic leukodystrophy, adult form (0.606); metachromatic leukodystrophy, late infantile form (0.592); hereditary disease (0.522)
- **Europe PMC papers**: 4753
- **Why important**: ARSA is connected to LRTM3 and is the module member with the clearest defined catalytic function: hydrolysis of cerebroside sulfate in sphingolipid catabolism. It is detected in liver by HPA, is associated with Golgi localization and intracellular or membrane secretion status, and is enriched across several cell types including enterocytes and spermatogenic states. It has extensive literature and a strong Open Targets association with metachromatic leukodystrophy and its clinical forms.
- **Conclusion**: Established evidence supports ARSA as a lysosomal or Golgi-associated sphingolipid-processing enzyme with a well-defined disease relationship. Its inclusion may indicate lipid-processing or organelle-state biology, but the module data do not establish that ARSA activity drives the other genes or that the module represents metachromatic leukodystrophy biology.

#### NSFL1C

- **Related proteins** (co-abundance neighbors): LRTM3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NSFL1 cofactor. N-ethylmaleimide-sensitive factor (NSF) and valosin-containing protein (p97) are two ATPases known to be involved in transport vesicle/target membrane fusion and fusions between membrane compartments. A trimer of the protein encoded by this gene binds a hexamer of cytosolic p97 and is required for p97-mediated regrowth of Golgi cisternae from mitotic Golgi fragments. Alternative splicing results i…
- **Diseases (Open Targets)**: neurodegenerative disease (0.326); placenta praevia (0.045); adult T-cell leukemia/lymphoma (0.035); pneumonitis (0.027); hypertensive disorder (0.026)
- **Europe PMC papers**: 308
- **Why important**: NSFL1C is connected to LRTM3 and has a defined role as an NSF and p97 cofactor involved in membrane-compartment fusion and Golgi reassembly. It is detected in liver and has broad tissue specificity, with cell-type enhancement in esophageal apical cells and oocytes. Its annotations also include ubiquitin-dependent protein catabolism and centrosome-related processes. Open Targets lists neurodegenerative disease and several additional disease associations.
- **Conclusion**: Established evidence supports NSFL1C as a membrane-trafficking and protein-homeostasis factor that could provide an intracellular context for the module. Its role as a mechanistic bridge to LRTM3, ARSA, or TBL2 is only a hypothesis because no high-confidence STRING interaction or shared hu.MAP complex is reported.

## Module 10

**Tissue pair**: circulatory_system and liver  
**Genes (5)**: DHX9, HNRNPR, RPL12, RPL6, EFTUD2

### Function

The module is best interpreted as a conserved RNA metabolism and protein-synthesis module centered on ribonucleoprotein biology. The primary evidence is the globally significant enrichment for ribonucleoprotein complex (GO:CC ribonucleoprotein complex; q_global = 0.000968), containing every module gene, and for cytoplasmic translation (GO:BP cytoplasmic translation; q_global = 0.0409), containing DHX9, RPL12, and RPL6. The supplementary STRING results reinforce this interpretation through RNA metabolism, ribosome, mRNA processing, mRNA splicing, and polysomal-ribosome annotations (STRING RCTM Metabolism of RNA; within-query FDR = 0.0012), (STRING COMPARTMENTS Ribosome; within-query FDR = 0.0122), (STRING Keyword mRNA splicing; within-query FDR = 0.0159), (STRING WikiPathways mRNA processing; within-query FDR = 0.0221), (STRING COMPARTMENTS Polysomal ribosome; within-query FDR = 0.0267), and (STRING Component Polysomal ribosome; within-query FDR = 0.0467). The network is therefore most consistent with coordinated expression of ribosomal, RNA-binding, RNA-helicase, and spliceosomal functions rather than a tissue-specific secreted pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. All genes have low tissue specificity, and all have low immune-cell specificity, so the module does not look blood-cell enriched. Protein detection in liver is reported for every module gene, while no matching circulatory-system HPA tissue is available. The broad expression pattern and the presence of core RNA and translation machinery are more compatible with a broadly expressed housekeeping-type program, although the two genes with cell-type-enhanced HPA annotations indicate that expression can still vary among cell populations. The shared signal should therefore not automatically be attributed to a plasma-protein mixture or blood contamination.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC ribonucleoprotein complex | 0.000968 | DHX9, EFTUD2, HNRNPR, RPL12, RPL6 |
| GO:BP cytoplasmic translation | 0.0409 | DHX9, RPL12, RPL6 |

### STRING and hu.MAP

STRING provides substantial support for known relationships within the module. DHX9 is linked to HNRNPR and RPL6, EFTUD2 is linked to RPL12 and RPL6, and RPL12 is strongly linked to RPL6. The STRING functional results independently support ribonucleoprotein complexes, RNA metabolism, ribosomes, mRNA splicing, and mRNA processing (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.00022), (STRING Component Ribonucleoprotein complex; within-query FDR = 0.00042), (STRING RCTM Metabolism of RNA; within-query FDR = 0.0012), (STRING COMPARTMENTS Ribosome; within-query FDR = 0.0122), (STRING Keyword mRNA splicing; within-query FDR = 0.0159), and (STRING WikiPathways mRNA processing; within-query FDR = 0.0221). These links indicate that the co-abundance pattern is biologically coherent and partly reflects established molecular relationships. However, no hu.MAP complex contains at least two module members. Thus, the module is supported as a functional RNA-related network, but the fact sheet does not establish one previously catalogued physical complex containing all members. STRING enrichment is supplementary and does not replace the globally corrected GO evidence.

**STRING interactions (score >= 0.7)**: 5 of 10 gene pairs: DHX9–HNRNPR (0.909); DHX9–RPL6 (0.958); EFTUD2–RPL12 (0.752); EFTUD2–RPL6 (0.706); RPL12–RPL6 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Ribonucleoprotein complex (FDR = 0.00022, 5 genes); Component Ribonucleoprotein complex (FDR = 0.00042, 5 genes); RCTM Metabolism of RNA (FDR = 0.0012, 5 genes); Keyword Isopeptide bond (FDR = 0.0077, 5 genes); Keyword Ubl conjugation (FDR = 0.0097, 5 genes); COMPARTMENTS Ribosome (FDR = 0.0122, 3 genes); Keyword Ribonucleoprotein (FDR = 0.0152, 3 genes); Keyword mRNA splicing (FDR = 0.0159, 3 genes); Component Ribosome (FDR = 0.021, 3 genes); WikiPathways mRNA processing (FDR = 0.0221, 3 genes); COMPARTMENTS Cytosolic large ribosomal subunit (FDR = 0.0238, 2 genes); COMPARTMENTS Polysomal ribosome (FDR = 0.0267, 2 genes); Component Cytosolic large ribosomal subunit (FDR = 0.0467, 2 genes); Component Polysomal ribosome (FDR = 0.0467, 2 genes); Keyword Ribosomal protein (FDR = 0.047, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The biological functions represented here are not new: ribosomal proteins, DHX9, HNRNPR, and EFTUD2 are already annotated in translation, RNA metabolism, RNA binding, or splicing, and several of their pairwise relationships are supported by STRING. The absence of a matching hu.MAP complex therefore cannot establish novelty, and neither can any missing STRING edge. What may be potentially new is the observation that these genes form a conserved co-abundance module shared by circulatory_system and liver. The available evidence does not demonstrate that this tissue-pair co-abundance organization has been reported previously, so the appropriate conclusion is a potentially novel systems-level association built from largely established molecular components, requiring comparison with prior co-expression studies and independent validation.

**Hypothesis.** Hypothesis: shared expression of this module coordinates RNA maturation, RNA remodeling, and translation in liver and in the circulatory-system samples. DHX9 could couple RNA structural remodeling with RNA handling, HNRNPR and EFTUD2 could support pre-mRNA processing and spliceosomal function, and RPL12 together with RPL6 could represent the translation-facing component. The co-abundance signal may therefore reflect a common cellular demand for integrated RNA processing and protein synthesis rather than a specialized secreted or immune program. This is a mechanistic hypothesis, not proof of direct physical assembly or causal regulation among all module genes.

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): RPL12 (0.82), RPL6 (0.81), EFTUD2 (0.81); STRING partners: HNRNPR (0.909), RPL6 (0.958)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is the most connected module member in the reported subgraph and links to HNRNPR, RPL6, and EFTUD2. It is an ATP-dependent RNA helicase with nuclear and cytoplasmic localization and reported roles in RNA unwinding, transcriptional regulation, alternative splicing, and interferon-related regulation. It is present in both primary GO terms (GO:CC ribonucleoprotein complex; q_global = 0.000968) and (GO:BP cytoplasmic translation; q_global = 0.0409) and in many supplementary RNA and ribosome-related terms. Its disease associations include intellectual developmental disorder and neurodegenerative disease, and it has the largest literature volume among the module genes.
- **Conclusion**: Established evidence supports DHX9 as a central RNA-remodeling and regulatory component of the module. It is a plausible connector between RNA processing and translation. Its hub position does not by itself prove that DHX9 drives the shared tissue-pair signal; that proposed coordinating role remains a hypothesis.

#### RPL6

- **Related proteins** (co-abundance neighbors): DHX9 (0.81); STRING partners: DHX9 (0.958), EFTUD2 (0.706), RPL12 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein L6. This gene encodes a protein component of the 60S ribosomal subunit. This protein can bind specifically to domain C of the tax-responsive enhancer element of human T-cell leukemia virus type 1, and may participate in tax-mediated transactivation of transcription. As is typical for genes encoding ribosomal proteins, there are multiple processed pseudogenes of this gene dispersed throughout the genom…
- **Diseases (Open Targets)**: Duchenne muscular dystrophy (0.503); Orthomyxoviridae infectious disease (0.463); cystic fibrosis (0.388); stroke disorder (0.370); hypertensive disorder (0.344)
- **Europe PMC papers**: 1588
- **Why important**: RPL6 is a component of the cytoplasmic large ribosomal subunit and is present in both primary terms (GO:CC ribonucleoprotein complex; q_global = 0.000968) and (GO:BP cytoplasmic translation; q_global = 0.0409). It participates in the strongest reported STRING relationship involving RPL12 and is also connected to DHX9 and EFTUD2. The STRING results repeatedly place it in ribosome, polysomal ribosome, and cytoplasmic large-subunit categories (STRING COMPARTMENTS Ribosome; within-query FDR = 0.0122), (STRING Component Ribosome; within-query FDR = 0.021), (STRING COMPARTMENTS Cytosolic large ribosomal subunit; within-query FDR = 0.0238), (STRING COMPARTMENTS Polysomal ribosome; within-query FDR = 0.0267), (STRING Component Cytosolic large ribosomal subunit; within-query FDR = 0.0467), and (STRING Component Polysomal ribosome; within-query FDR = 0.0467). Its annotations include cytoplasmic translation, and its disease associations include stroke disorder and hypertensive disorder, while its literature volume is substantial.
- **Conclusion**: Established evidence supports RPL6 as the clearest translation and ribosome-facing anchor of the module. Its co-abundance with RNA-processing genes supports coordination between translation and RNA handling, but no causal link between RPL6 and the tissue-pair phenotype is established.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): DHX9 (0.81); STRING partners: RPL12 (0.752), RPL6 (0.706)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 is included in the primary ribonucleoprotein-complex term (GO:CC ribonucleoprotein complex; q_global = 0.000968) and connects in STRING to both RPL12 and RPL6. Its established function is as a GTPase-containing component of the spliceosome, with roles in spliceosomal assembly and conformational change. It also appears in supplementary mRNA-splicing and mRNA-processing categories (STRING Keyword mRNA splicing; within-query FDR = 0.0159) and (STRING WikiPathways mRNA processing; within-query FDR = 0.0221). Its disease associations include mandibulofacial dysostosis with microcephaly and global developmental delay.
- **Conclusion**: Established evidence supports EFTUD2 as the spliceosomal component that broadens the module beyond ribosome structure. Its connections to ribosomal genes are consistent with coordinated RNA maturation and translation, but the available data do not show that EFTUD2 physically bridges these processes within one complex.

#### HNRNPR

- **Related proteins** (co-abundance neighbors): RPL12 (0.80); STRING partners: DHX9 (0.909)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR is present in the primary ribonucleoprotein-complex term (GO:CC ribonucleoprotein complex; q_global = 0.000968) and is linked by STRING to DHX9. It is a heterogeneous nuclear ribonucleoprotein involved in the spliceosome C complex, pre-mRNA processing, RNA transport, and transcriptional regulation. It also appears in supplementary mRNA splicing and mRNA-processing categories (STRING Keyword Ribonucleoprotein; within-query FDR = 0.0152), (STRING Keyword mRNA splicing; within-query FDR = 0.0159), and (STRING WikiPathways mRNA processing; within-query FDR = 0.0221). Its disease associations include neurodevelopmental disorder, intellectual disability, global developmental delay, and seizure.
- **Conclusion**: Established evidence supports HNRNPR as the RNA-binding and pre-mRNA-processing representative of the module. Its connection with DHX9 makes it a plausible RNA-processing partner in the network, whereas any role in coordinating translation or explaining the shared tissue pattern remains hypothetical.

## Module 11

**Tissue pair**: circulatory_system and liver  
**Genes (7)**: DYNC1H1, EIF3C, EIF3L, UPF1, AARS1, MARS1, SNRNP200

### Function

The module is best interpreted as a broadly expressed RNA-handling and protein-production module. The strongest primary evidence is the globally corrected enrichment for RNA binding (GO:MF RNA binding; q_global = 0.00905), nucleic-acid binding (GO:MF nucleic acid binding; q_global = 0.0223), translation (GO:BP translation; q_global = 0.0301), and protein biosynthetic process (GO:BP protein biosynthetic process; q_global = 0.0301). All module genes contribute to the RNA-binding and nucleic-acid-binding signals, while the translation and protein-biosynthesis signals are driven by AARS1, MARS1, EIF3C, EIF3L, and UPF1. The gene annotations support a coordinated continuum from RNA processing and surveillance through translation initiation and tRNA aminoacylation. SNRNP200 represents pre-mRNA splicing, UPF1 represents mRNA export and nonsense-mediated decay, EIF3C and EIF3L represent translation initiation, and AARS1 and MARS1 charge tRNAs. DYNC1H1 adds intracellular transport and cytoplasmic organization. Thus, the module most plausibly reflects constitutive RNA metabolism and translational capacity rather than a specialized liver or circulatory pathway. No KEGG term is reported as having passed global correction; the primary enrichment evidence is therefore the globally corrected GO evidence (4 globally significant GO/KEGG terms, q_global 0.00905–0.0301; see the table).

**Cell composition.** The module is composed entirely of intracellular proteins, with no secreted genes. HPA indicates predominantly low tissue specificity and low immune-cell specificity, so the shared signal is not readily explained by a plasma-protein program, a blood-cell-enriched program, or a narrowly restricted tissue population. Most proteins are detected in liver, while the circulatory-system protein result has no matching HPA tissue and therefore does not provide a direct protein-detection comparison. Some genes have enhanced single-cell expression in neural or cardiac-related cell types, and DYNC1H1 is tissue-enhanced in brain, but these observations do not establish that such cells generated the shared circulatory-system and liver module. Overall, the composition is more consistent with broadly expressed cellular machinery, potentially reflecting common cellular activity or technical and compositional effects shared across the tissues, than with a secreted or blood-cell-specific module.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF RNA binding | 0.00905 | AARS1, DYNC1H1, EIF3C, EIF3L, MARS1, SNRNP200, UPF1 |
| GO:MF nucleic acid binding | 0.0223 | AARS1, DYNC1H1, EIF3C, EIF3L, MARS1, SNRNP200, UPF1 |
| GO:BP translation | 0.0301 | AARS1, EIF3C, EIF3L, MARS1, UPF1 |
| GO:BP protein biosynthetic process | 0.0301 | AARS1, EIF3C, EIF3L, MARS1, UPF1 |

### STRING and hu.MAP

STRING provides direct high-confidence support for the AARS1-MARS1 relationship and for the EIF3C-EIF3L relationship. The AARS1-MARS1 pair is biologically coherent because both are aminoacyl-tRNA synthetases involved in supplying charged tRNAs for translation. EIF3C and EIF3L are supported as members of the eukaryotic translation-initiation machinery, and hu.MAP places them together in several translation-related complexes (hu.MAP huMAP3_01276.1) (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1). The remaining module connections are not represented by high-confidence STRING links, and most module genes have no listed STRING partner within this evidence set. Accordingly, the module is not a single fully documented physical complex: it combines a known tRNA-synthetase pair, a known eIF3 pair, and co-abundance links connecting these with RNA surveillance, splicing, and transport factors. STRING functional enrichment supports RNA binding, protein biosynthesis, catalytic activity on RNA, and translation-regulator activity (4 supplementary STRING terms; within-query FDR 0.0053–0.046), while the Charcot-Marie-Tooth signals (STRING DISEASES Charcot-Marie-Tooth disease type 2; within-query FDR = 0.0113) (STRING Keyword Charcot-Marie-Tooth disease; within-query FDR = 0.0177) are supplementary and should not be treated as globally corrected enrichment.

**STRING interactions (score >= 0.7)**: 2 of 21 gene pairs: AARS1–MARS1 (0.913); EIF3C–EIF3L (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function RNA binding (FDR = 0.0053, 7 genes); DISEASES Charcot-Marie-Tooth disease type 2 (FDR = 0.0113, 3 genes); Keyword Charcot-Marie-Tooth disease (FDR = 0.0177, 3 genes); Keyword Protein biosynthesis (FDR = 0.0177, 4 genes); Function Catalytic activity, acting on RNA (FDR = 0.0294, 4 genes); Function Translation regulator activity (FDR = 0.046, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01276.1 (EIF3C, EIF3L; 2/17); huMAP3_13175.1 (EIF3C, EIF3L; 2/20); huMAP3_11246.1 (EIF3C, EIF3L; 2/24)

### Novelty

This is not a wholly novel molecular mechanism, because the core relationships involving AARS1 with MARS1 and EIF3C with EIF3L are already supported by STRING, and the EIF3C-EIF3L pair occurs in multiple hu.MAP complexes (hu.MAP huMAP3_01276.1) (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1). The biological functions of the individual proteins are also established. The potentially novel aspect is the reproducible co-abundance organization of these otherwise distinct RNA-processing, translation, surveillance, and transport components across circulatory_system and liver. That observation may represent a tissue-pair-specific systems-level association, but it cannot be called a new physical complex or a new disease mechanism from this fact sheet alone. Absence of additional STRING or hu.MAP links is evidence that the observed network extends beyond currently catalogued relationships, not proof of novelty. Independent replication, preservation across cohorts, control for cellular composition, and perturbation or interaction experiments would be needed to establish a genuinely new biological finding.

**Hypothesis.** Hypothesis: the shared module reflects coordinated maintenance of RNA quality and protein synthesis in cells present in both tissues. In this model, SNRNP200 supports pre-mRNA splicing, UPF1 monitors exported transcripts and removes defective mRNAs, EIF3C and EIF3L support translation initiation, and AARS1 with MARS1 supplies charged tRNAs. DYNC1H1 may couple this RNA and translation workload to intracellular transport and cytoplasmic organization. The co-abundance pattern could therefore arise when cells increase general RNA processing, surveillance, transport, and translational capacity together. This is a mechanistic hypothesis rather than an established causal pathway; the data do not show that any member regulates the others or that the module is specific to hepatocytes, circulating cells, or a particular disease state.

### Important genes

#### MARS1

- **Related proteins** (co-abundance neighbors): EIF3C (0.86), DYNC1H1 (0.85), UPF1 (0.82), AARS1 (0.81); STRING partners: AARS1 (0.913)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionyl-tRNA synthetase 1. This gene encodes a member of the class I family of aminoacyl-tRNA synthetases. These enzymes play a critical role in protein biosynthesis by charging tRNAs with their cognate amino acids. The encoded protein is a component of the multi-tRNA synthetase complex and catalyzes the ligation of methionine to tRNA molecules. [provided by RefSeq, Jan 2011].
- **Diseases (Open Targets)**: severe early-onset pulmonary alveolar proteinosis due to MARS deficiency (0.745); Charcot-Marie-Tooth disease axonal type 2U (0.676); autosomal recessive spastic paraplegia type 70 (0.614); trichothiodystrophy 9, nonphotosensitive (0.428); pulmonary alveolar proteinosis (0.338)
- **Europe PMC papers**: 435
- **Why important**: MARS1 is the strongest network-connected member in the supplied subgraph and links the tRNA-synthetase component to EIF3C, DYNC1H1, UPF1, and AARS1. It is a methionyl-tRNA synthetase and therefore directly supports protein biosynthesis, matching all primary GO signals (4 globally significant GO/KEGG terms, q_global 0.00905–0.0301; see the table). It forms the high-confidence STRING pair with AARS1 and contributes to the supplementary protein-biosynthesis and RNA-related signals (6 supplementary STRING terms; within-query FDR 0.0053–0.046). Its disease associations include MARS deficiency with severe early-onset pulmonary alveolar proteinosis and Charcot-Marie-Tooth disease, and it has substantial literature support.
- **Conclusion**: Established: MARS1 is a central translational enzyme and a network connector with disease relevance. Hypothesis: its connectivity may make it a coordinating marker of increased translational demand in the shared module, but the co-abundance data do not establish that MARS1 controls the other genes.

#### EIF3C

- **Related proteins** (co-abundance neighbors): MARS1 (0.86), SNRNP200 (0.80); STRING partners: EIF3L (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_01276.1, huMAP3_13175.1, huMAP3_11246.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C is a translation-initiation factor, contributes to formation of the cytoplasmic translation-initiation complex, and participates in all primary GO signals (4 globally significant GO/KEGG terms, q_global 0.00905–0.0301; see the table). It has a direct high-confidence STRING relationship with EIF3L and is present with EIF3L in several hu.MAP complexes (hu.MAP huMAP3_01276.1) (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1). Within the module it connects MARS1 and SNRNP200, linking translation machinery with aminoacyl-tRNA supply and RNA splicing. It also has extensive literature support and reported associations with neoplasm and carcinoma phenotypes.
- **Conclusion**: Established: EIF3C is the clearest translation-initiation anchor and has independent interaction and complex evidence. Hypothesis: EIF3C may help couple translational initiation to the broader RNA-processing program, although the module does not demonstrate a causal coupling.

#### UPF1

- **Related proteins** (co-abundance neighbors): MARS1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UPF1 RNA helicase and ATPase. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons.…
- **Diseases (Open Targets)**: Intellectual disability (0.437); Global developmental delay (0.426); High anterior hairline (0.425); Frontal bossing (0.425); Hypertelorism (0.425)
- **Europe PMC papers**: 4252
- **Why important**: UPF1 is a core factor in mRNA surveillance, nonsense-mediated decay, mRNA export, and regulation of translational termination. It contributes to every primary GO signal (4 globally significant GO/KEGG terms, q_global 0.00905–0.0301; see the table) and connects to MARS1 in the co-abundance graph. Its very large literature base and associations with intellectual disability and developmental-delay phenotypes make it an important biological and disease-relevant representative of RNA quality control.
- **Conclusion**: Established: UPF1 provides a strong RNA-surveillance explanation for the module alongside its translation-related enrichment. Hypothesis: the module may coordinate transcript quality control with protein production, but no direct regulatory relationship between UPF1 and the translation factors is demonstrated here.

#### DYNC1H1

- **Related proteins** (co-abundance neighbors): MARS1 (0.85), EIF3L (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 1 heavy chain 1. Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polyp…
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy without contractures (0.816); intellectual disability, autosomal dominant 13 (0.815); Charcot-Marie-Tooth disease axonal type 2O (0.799); autosomal dominant non-syndromic intellectual disability (0.634); hereditary disease (0.545)
- **Europe PMC papers**: 1731
- **Why important**: DYNC1H1 contributes to the RNA-binding and nucleic-acid-binding primary terms (GO:MF RNA binding; q_global = 0.00905) (GO:MF nucleic acid binding; q_global = 0.0223) and connects MARS1 with EIF3L in the module graph. Its established function is cytoplasmic dynein-mediated intracellular movement, including organelle transport, protein sorting, and retrograde axonal transport. It is tissue-enhanced in brain and has strong associations with motor-neuron, intellectual-disability, and Charcot-Marie-Tooth phenotypes. STRING supplementary evidence also links it to the Charcot-Marie-Tooth disease signal (STRING DISEASES Charcot-Marie-Tooth disease type 2; within-query FDR = 0.0113) (STRING Keyword Charcot-Marie-Tooth disease; within-query FDR = 0.0177).
- **Conclusion**: Established: DYNC1H1 supplies an intracellular-transport dimension and is clinically important in inherited neurological disease. Hypothesis: it may connect translational or RNA-processing activity to cytoplasmic transport, but this proposed bridge is inferred from co-abundance and function rather than demonstrated interaction.

#### AARS1

- **Related proteins** (co-abundance neighbors): MARS1 (0.81); STRING partners: MARS1 (0.913)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alanyl-tRNA synthetase 1. The human alanyl-tRNA synthetase (AARS) belongs to a family of tRNA synthases, of the class II enzymes.  Class II tRNA synthases evolved early in evolution and are highly conserved. This is reflected by the fact that 498 of the 968-residue polypeptide human AARS shares 41% identity witht the E.coli protein.  tRNA synthases are the enzymes that interpret the RNA code and attach specific aminoacids …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2N (0.762); developmental and epileptic encephalopathy, 29 (0.747); undetermined early-onset epileptic encephalopathy (0.678); trichothiodystrophy 8, nonphotosensitive (0.568); Charcot-Marie-Tooth disease type 2 (0.566)
- **Europe PMC papers**: 672
- **Why important**: AARS1 is an alanyl-tRNA synthetase that directly supports tRNA aminoacylation and protein translation. It contributes to all primary GO signals (4 globally significant GO/KEGG terms, q_global 0.00905–0.0301; see the table), forms the known STRING pair with MARS1, and participates in the supplementary RNA-binding, protein-biosynthesis, and translation-regulator signals (6 supplementary STRING terms; within-query FDR 0.0053–0.046). Its disease associations include Charcot-Marie-Tooth disease and developmental epileptic encephalopathy, and it has substantial literature support.
- **Conclusion**: Established: AARS1 is a functionally coherent translational component and a known partner of MARS1. Hypothesis: the AARS1-MARS1 pair may represent a translational supply submodule within the broader network, but the data do not show that this pair drives the tissue-shared pattern.

## Module 12

**Tissue pair**: circulatory_system and liver  
**Genes (8)**: TUFM, ERO1A, LDHA, P4HA1, EPRS1, RARS1, TARS1, TNS3

### Function

No GO or KEGG term passed global correction, so the module does not have a globally significant pathway annotation. Its most defensible interpretation is a mixed cellular protein-homeostasis and biosynthetic module centered on TNS3. The functional signal is supported mainly by the supplementary STRING keyword Protein biosynthesis term (STRING Keyword Protein biosynthesis; within-query FDR = 0.0345), which includes EPRS1, RARS1, TARS1, and TUFM, together with the known aminoacyl-tRNA synthetase relationships among EPRS1, RARS1, and TARS1. The remaining genes connect this translation-related core to focal-adhesion and signaling biology through TNS3, collagen maturation through P4HA1, endoplasmic-reticulum folding and redox biology through ERO1A, glycolytic lactate production through LDHA, and mitochondrial translation through TUFM. Because these annotations span several compartments and processes, the module should not be treated as a single established pathway.

**Cell composition.** The module is predominantly composed of broadly expressed intracellular proteins rather than a clear plasma-protein or secreted-protein program. HPA reports low tissue specificity for most genes, low immune-cell specificity for most genes, and only limited tissue or cell-type enrichment distributed across different cell types. The summary flags two secreted genes, but the gene-level records generally report no secretome annotation or an intracellular or membrane localization, so secretion does not appear to be the dominant organizing principle. TNS3 has a blood-cell group-enriched pattern involving several myeloid and B-cell populations, while other genes show enrichment in podocytes, epithelial cells, megakaryocytes, neurons, myonuclei, thymic myoid cells, late spermatids, or salivary cells. This scattered pattern argues against a module specific to one shared liver or circulatory cell type. The liver protein observations are also mixed, with some genes detected and others not detected, so the co-abundance signal may reflect general cellular abundance, sample composition, or coordinated stress and biosynthetic state rather than a tissue-specific secreted program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a compact, high-confidence known interaction core: EPRS1 interacts with RARS1, EPRS1 interacts with TARS1, and RARS1 interacts with TARS1. The supplementary STRING protein-biosynthesis term (STRING Keyword Protein biosynthesis; within-query FDR = 0.0345) is consistent with this core but is not globally corrected across modules and therefore is supportive rather than definitive. hu.MAP independently places EPRS1, RARS1, and TARS1 together in two complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), with additional aminoacyl-tRNA synthetases and associated factors outside the module. These results show that part of the module recapitulates known translation-related protein organization. In contrast, TNS3, P4HA1, ERO1A, LDHA, and TUFM lack listed STRING partners or hu.MAP complexes within this module, despite their co-abundance links to TNS3. Thus, the network combines a validated synthetase subnetwork with co-abundance associations that are not established physical interactions.

**STRING interactions (score >= 0.7)**: 3 of 28 gene pairs: EPRS1–RARS1 (0.999); EPRS1–TARS1 (0.928); RARS1–TARS1 (0.806)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Protein biosynthesis (FDR = 0.0345, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, TARS1, RARS1; 3/14); huMAP3_13688.1 (EPRS1, TARS1, RARS1; 3/14)

### Novelty

The aminoacyl-tRNA synthetase component is not a new molecular association because the EPRS1–RARS1–TARS1 relationships are supported by both STRING and hu.MAP (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). The potentially novel aspect is the cross-compartment co-abundance configuration linking that known core with TNS3, P4HA1, ERO1A, LDHA, and TUFM across circulatory system and liver. However, the fact sheet does not establish that this configuration is absent from prior co-expression or proteomic studies, and absence from STRING or hu.MAP would not prove novelty. The appropriate conclusion is that this is a potentially interesting tissue-pair co-abundance pattern, not an established new biological discovery.

**Hypothesis.** Hypothesis: the module may report a shared cellular state in which protein production and protein quality control are coordinated with focal-adhesion signaling, metabolism, and mitochondrial translation. In this model, TNS3 acts as the co-abundance hub linking the known aminoacyl-tRNA synthetase core to collagen-processing, endoplasmic-reticulum redox and folding, glycolytic, and mitochondrial translation programs. The signal could arise from coordinated biosynthetic demand or cellular stress in liver and circulatory-system samples, or from variation in contributing cell populations. This hypothesis requires experimental testing because the co-abundance edges outside the synthetase core are not demonstrated physical interactions and no GO or KEGG term achieved global significance.

### Important genes

#### TNS3

- **Related proteins** (co-abundance neighbors): P4HA1 (0.87), TARS1 (0.85), ERO1A (0.85), RARS1 (0.83), LDHA (0.82), TUFM (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tensin 3. Predicted to enable phosphatase activity. Predicted to be involved in dephosphorylation and intracellular signal transduction. Predicted to act upstream of or within cell migration; lung alveolus development; and positive regulation of cell population proliferation. Located in cytosol and focal adhesion. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: prostate carcinoma (0.540); neurodegenerative disease (0.540); basal cell carcinoma (0.496); skin neoplasm (0.483); benign colon neoplasm (0.478)
- **Europe PMC papers**: 749
- **Why important**: TNS3 is the network hub with the strongest connectivity in the module and links the synthetase-related genes to P4HA1, ERO1A, LDHA, and TUFM. Its annotations implicate phosphatase activity, intracellular signal transduction, Rac signaling, focal adhesions, cell migration, and proliferation. Its blood-cell group-enriched HPA pattern may also make it relevant to sample-composition effects. It has a substantial literature and disease associations spanning prostate carcinoma, neurodegenerative disease, basal cell carcinoma, skin neoplasm, and benign colon neoplasm.
- **Conclusion**: Established evidence supports TNS3 as the structural hub and as a signaling and adhesion-associated protein. The proposed role of TNS3 as the biological coordinator of translation, metabolism, and protein-folding signals is a hypothesis rather than an established mechanism.

#### EPRS1

- **Related proteins** (co-abundance neighbors): RARS1 (0.81); STRING partners: RARS1 (0.999), TARS1 (0.928)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is part of the strongest STRING interaction core, with a very high-confidence relationship to RARS1 and another high-confidence relationship to TARS1. It is present in both hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1) and encodes a multifunctional glutamyl-prolyl-tRNA synthetase involved in translation and tRNA aminoacylation. Its annotations also include negative regulation of translation and cellular response to insulin stimulus, while its disease associations include hypomyelinating leukodystrophy and developmental phenotypes.
- **Conclusion**: Established evidence identifies EPRS1 as a central component of a known aminoacyl-tRNA synthetase assembly and as a plausible marker of translational activity. Its specific contribution to the shared liver–circulatory co-abundance pattern beyond that established complex remains unresolved.

#### RARS1

- **Related proteins** (co-abundance neighbors): TNS3 (0.83), EPRS1 (0.81); STRING partners: EPRS1 (0.999), TARS1 (0.806)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 participates in both hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1) and forms the STRING-linked synthetase core with EPRS1 and TARS1. It encodes arginyl-tRNA synthetase, a canonical enzyme of tRNA aminoacylation and protein translation. It is detected in liver and has disease associations with hypomyelinating leukodystrophy and related hereditary phenotypes. Its lower network connectivity than TNS3 does not diminish its importance as a physically supported core component.
- **Conclusion**: Established evidence supports RARS1 as a bona fide translation-related member and a known complex component. The module does not establish a new RARS1 interaction with TNS3 or a tissue-specific RARS1 function.

#### TARS1

- **Related proteins** (co-abundance neighbors): TNS3 (0.85); STRING partners: EPRS1 (0.928), RARS1 (0.806)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: threonyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Threonyl-tRNA synthetase belongs to the class-II aminoacyl-tRNA synthetase family [provided by RefSeq, Jul 2008]…
- **Diseases (Open Targets)**: trichothiodystrophy 7, nonphotosensitive (0.520); trichothiodystrophy (0.430); actinic keratosis (0.356); dyshidrosis (0.315); placental abruption (0.307)
- **Europe PMC papers**: 147
- **Why important**: TARS1 is linked by STRING to both EPRS1 and RARS1 and occurs in both hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). It encodes threonyl-tRNA synthetase and therefore provides an independent translation-related function within the known synthetase core. It is detected in liver and has reported associations with trichothiodystrophy, actinic keratosis, dyshidrosis, and placental abruption.
- **Conclusion**: Established evidence supports TARS1 as part of a known aminoacyl-tRNA synthetase interaction module. Its connection to TNS3 is a co-abundance relationship in this dataset, not a demonstrated physical or mechanistic interaction.

#### P4HA1

- **Related proteins** (co-abundance neighbors): TNS3 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prolyl 4-hydroxylase subunit alpha 1. This gene encodes a component of prolyl 4-hydroxylase, a key enzyme in collagen synthesis composed of two identical alpha subunits and two beta subunits. The encoded protein is one of several different types of alpha subunits and provides the major part of the catalytic site of the active enzyme. In collagen and related proteins, prolyl 4-hydroxylase catalyzes the formation of 4-hydroxyproline tha…
- **Diseases (Open Targets)**: neurodegenerative disease (0.406); dengue disease (0.370); Parkinson disease (0.201); intervertebral disk degenerative disorder (0.193); neoplasm (0.115)
- **Europe PMC papers**: 1910
- **Why important**: P4HA1 connects to the TNS3 hub and encodes a catalytic component of prolyl 4-hydroxylase, an enzyme required for collagen maturation and proper procollagen folding. It is localized to the endoplasmic reticulum, is detected in liver, and has associations with neurodegenerative disease, dengue disease, Parkinson disease, intervertebral disc degeneration, and neoplasm. Its substantial literature makes it an informative bridge between the module and extracellular-matrix protein processing.
- **Conclusion**: Established evidence supports P4HA1 as an endoplasmic-reticulum collagen-processing enzyme. Its placement beside TNS3 may indicate coordinated matrix or protein-folding biology, but that interpretation is a hypothesis because the module supplies only a co-abundance link and no globally significant pathway term.

#### TUFM

- **Related proteins** (co-abundance neighbors): TNS3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Tu translation elongation factor, mitochondrial. This gene encodes a protein which participates in protein translation in mitochondria. Mutations in this gene have been associated with combined oxidative phosphorylation deficiency resulting in lactic acidosis and fatal encephalopathy. A pseudogene has been identified on chromosome 17. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 4 (0.769); neurodegenerative disease (0.502); COVID-19 (0.471); combined oxidative phosphorylation deficiency (0.370); ulcerative colitis (0.303)
- **Europe PMC papers**: 1391
- **Why important**: TUFM connects to TNS3 and is a mitochondrial translation elongation factor. It is associated with mitochondrial translational elongation, mitochondrial ribosomal assembly, combined oxidative-phosphorylation deficiency, lactic acidosis, and fatal encephalopathy. Its inclusion broadens the module beyond cytosolic translation and suggests that cellular energy production or mitochondrial protein synthesis may covary with the module state.
- **Conclusion**: Established evidence supports TUFM as a mitochondrial translation factor with clinically important oxidative-phosphorylation associations. Its relationship to the cytosolic synthetase core and to TNS3 is not established as a physical interaction; any role in a coordinated biosynthetic state is hypothetical.

## Module 13

**Tissue pair**: circulatory_system and liver  
**Genes (8)**: EML4, H1-0, ITGAV, RPS6KA3, MAN2A1, NDUFS5, PEPD, TMEM11

### Function

No GO or KEGG term passed global correction, and there were no supplementary STRING functional terms. The module therefore does not support a single statistically established pathway-level function. Its genes span Golgi N-glycan maturation through MAN2A1, cell adhesion and signaling through ITGAV, proline-containing peptide recycling through PEPD, microtubule organization through EML4, mitochondrial organization and respiration through TMEM11 and NDUFS5, chromatin organization through H1-0, and MAPK-related signaling through RPS6KA3. The co-abundance pattern is consequently more consistent with a mixed cellular-state or tissue-composition signal than with a coherent canonical pathway. The sparse subgraph also argues against interpreting every edge as a functional interaction.

**Cell composition.** All module proteins were detected in liver by HPA, whereas the circulatory-system protein result had no matching HPA tissue assessment. None of the genes is annotated as secreted, and all have low immune-cell specificity. Most genes have low tissue specificity, with only PEPD showing tissue enhancement in intestine and kidney and H1-0 showing tissue enhancement in bone marrow. Several genes have cell-type-enriched or cell-type-enhanced expression, including EML4 and RPS6KA3 in innate lymphoid cells or neutrophils, NDUFS5 in megakaryocytes or platelets, PEPD in hepatocytes, and ITGAV in podocytes or urothelial cells. Thus, this is not a plasma-protein module or a clearly blood-cell-enriched module. The shared signal may instead reflect broadly expressed intracellular proteins, liver detection, and contributions from heterogeneous cell populations or shared cellular states.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and there were no STRING functional-enrichment terms. No hu.MAP complex contained at least two module members. The co-abundance links are therefore not corroborated by the supplied known physical-interaction or curated-complex resources. This does not disprove biological coordination: co-abundance can arise from shared regulation, cell composition, organelle activity, or technical and physiological covariation. It does mean that the module should not be described as an established protein complex or a validated interaction network.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported co-abundance pattern, because the supplied resources show no high-confidence STRING relationships, no shared hu.MAP complex, and no globally significant GO or KEGG term. However, these observations do not establish novelty. The genes themselves are well studied and have established functions, including integrin-mediated adhesion, Golgi glycan processing, peptide metabolism, microtubule biology, chromatin organization, mitochondrial complex-I biology, and kinase signaling. The defensible conclusion is that the cross-tissue co-abundance configuration is potentially novel or under-characterized, while the underlying gene functions are not novel. Demonstrating genuine novelty would require comparison with prior co-expression or proteomic modules, independent cohorts, and perturbation or spatial validation.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular tissue-state program rather than one molecular pathway. In liver and circulating samples, variation in the abundance or representation of cells and cellular compartments could jointly influence proteins involved in adhesion and extracellular-matrix contact through ITGAV, Golgi glycan maturation through MAN2A1, peptide and collagen-related amino-acid recycling through PEPD, cytoskeletal organization through EML4, mitochondrial energy biology through TMEM11 and NDUFS5, chromatin packaging through H1-0, and signal-responsive transcription through RPS6KA3. A plausible model is that tissue remodeling, cellular differentiation, or sample-composition variation produces coordinated abundance changes across these functions. This is a hypothesis only; the absence of significant GO or KEGG enrichment and the lack of STRING or hu.MAP support prevent calling it an established mechanism.

### Important genes

#### ITGAV

- **Related proteins** (co-abundance neighbors): MAN2A1 (0.85), PEPD (0.85), EML4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha V. The product of this gene belongs to the integrin alpha chain family. Integrins are heterodimeric integral membrane proteins composed of an alpha subunit and a beta subunit that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha V subunit. This subunit associates with beta 1, beta 3, beta…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); myocardial infarction (0.396); angina pectoris (0.371); Recurrent thrombophlebitis (0.370); intermediate coronary syndrome (0.370)
- **Europe PMC papers**: 5475
- **Why important**: ITGAV is among the most connected genes in the module and links MAN2A1, PEPD, and EML4 in the co-abundance graph. Its established function is as an integrin alpha subunit that participates in cell adhesion and signaling with multiple beta partners, and its annotations include angiogenesis, vasculogenesis, and cell-matrix adhesion. It is also the most extensively studied gene among the selected candidates and has disease associations involving cardiovascular disease and cancer-related biology.
- **Conclusion**: Established evidence supports ITGAV as a biologically plausible marker of adhesion, matrix interaction, or tissue remodeling. It is not established that ITGAV physically interacts with the neighboring module proteins or drives the module; those interpretations remain hypotheses based on co-abundance and network position.

#### MAN2A1

- **Related proteins** (co-abundance neighbors): ITGAV (0.85), TMEM11 (0.84), H1-0 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Golgi apparatus; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosidase alpha class 2A member 1. This gene encodes a glycosyl hydrolase that localizes to the Golgi and catalyzes the final hydrolytic step in the asparagine-linked oligosaccharide (N-glycan) maturation pathway. Mutations in the mouse homolog of this gene have been shown to cause a systemic autoimmune disease similar to human systemic lupus erythematosus. [provided by RefSeq, Dec 2013].
- **Diseases (Open Targets)**: alcohol drinking (0.456); schizophrenia (0.455); COVID-19 (0.370); smoking initiation (0.364); dislocation (0.344)
- **Europe PMC papers**: 663
- **Why important**: MAN2A1 has the strongest central position in the module and connects ITGAV, TMEM11, and H1-0. It encodes a Golgi glycosyl hydrolase involved in the final hydrolytic step of N-glycan maturation and has a substantial literature base. Its functional annotation also includes carbohydrate and mannose metabolism, while the mouse homolog has been linked to a systemic autoimmune phenotype.
- **Conclusion**: Established evidence supports MAN2A1 as a marker of Golgi glycan-processing capacity. Its central co-abundance position makes it a useful candidate for testing whether glycosylation-related cellular state contributes to the module, but no supplied enrichment or interaction evidence establishes it as a regulatory hub.

#### PEPD

- **Related proteins** (co-abundance neighbors): ITGAV (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peptidase D. This gene encodes a member of the peptidase family. The protein forms a homodimer that hydrolyzes dipeptides or tripeptides with C-terminal proline or hydroxyproline residues. The enzyme serves an important role in the recycling of proline, and may be rate limiting for the production of collagen. Mutations in this gene result in prolidase deficiency, which is characterized by the excretion of larg…
- **Diseases (Open Targets)**: prolidase deficiency (0.822); type 2 diabetes mellitus (0.425); Abnormality of the skeletal system (0.411); diabetes mellitus (0.409); obesity disorder (0.354)
- **Europe PMC papers**: 1500
- **Why important**: PEPD connects directly to ITGAV and is tissue-enhanced in intestine and kidney, with cell-type evidence that includes hepatocytes. It encodes prolidase, which hydrolyzes proline- or hydroxyproline-containing peptides and contributes to proline recycling and collagen production. Its disease annotation includes prolidase deficiency, and its metabolic role provides a plausible connection to hepatic and matrix-related physiology.
- **Conclusion**: Established evidence supports PEPD as a peptide-recycling and collagen-related metabolic enzyme. Its link to ITGAV suggests a testable association between peptide metabolism and adhesion or matrix biology, but the module does not establish that such a pathway operates between these proteins.

#### EML4

- **Related proteins** (co-abundance neighbors): ITGAV (0.80), RPS6KA3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules, Primary cilium, Annulus; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EMAP like 4. This gene is a member of the echinoderm microtubule associated protein-like family. The encoded WD-repeat protein may be involved in microtubule formation. Abnormal fusion of parts of this gene with portions of the anaplastic lymphoma receptor tyrosine kinase gene, which generates EML4-ALK fusion transcripts, is one of the primary mutations associated with non-small cell lung cancer. Alternative s…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.704); cancer (0.668); Abnormality of the skeletal system (0.628); neoplasm (0.601); lung adenocarcinoma (0.453)
- **Europe PMC papers**: 7119
- **Why important**: EML4 connects ITGAV with RPS6KA3 and is enriched or enhanced in several cell types, including innate lymphoid cells and neutrophils. It is a WD-repeat microtubule-associated protein involved in microtubule formation and related processes. Its extensive literature includes the clinically important EML4-ALK fusion in non-small-cell lung cancer.
- **Conclusion**: Established evidence supports EML4 as a cytoskeletal and microtubule-related gene with major cancer relevance. Its position may indicate coordination between adhesion-related and cytoskeletal states, but the supplied data do not show that EML4 mediates the module or that the cancer-associated fusion is relevant to these tissues.

#### NDUFS5

- **Related proteins** (co-abundance neighbors): H1-0 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit S5. This gene is a member of the NADH dehydrogenase (ubiquinone) iron-sulfur protein family. The encoded protein is a subunit of the NADH:ubiquinone oxidoreductase (complex I), the first enzyme complex in the electron transport chain located in the inner mitochondrial membrane. Alternative splicing results in multiple transcript variants and pseudogenes have been identified on chromosomes 1, 4 and 17.…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.608); Parkinson disease (0.605); diabetes mellitus (0.578); neurodegenerative disease (0.576); Alzheimer disease (0.536)
- **Europe PMC papers**: 800
- **Why important**: NDUFS5 links to H1-0 and encodes a subunit of mitochondrial respiratory complex I. Its annotations include mitochondrial electron transport, respiratory-chain complex-I assembly, and proton-motive-force-linked ATP synthesis. HPA cell-type evidence includes megakaryocytes and platelets, making it relevant to interpreting shared circulatory and tissue samples, while disease associations include metabolic and neurodegenerative conditions.
- **Conclusion**: Established evidence supports NDUFS5 as a marker of mitochondrial respiratory capacity. Its module membership may reflect energetic state or cellular composition, but the single co-abundance connection and absence of curated network support do not establish a mitochondria-centered module mechanism.

## Module 14

**Tissue pair**: circulatory_system and liver  
**Genes (5)**: FKBP4, GMPS, IMPDH2, ALDH18A1, PFAS

### Function

The strongest interpretation is a conserved intracellular purine and GMP biosynthesis module. The primary evidence is the repeated global enrichment of GMP biosynthetic process, purine nucleoside monophosphate biosynthesis and metabolism, and related ribonucleoside monophosphate processes (8 globally significant GO/KEGG terms, q_global 0.00551–0.0365; see the table). GMPS, IMPDH2 and PFAS account for the shared core of these terms. The globally significant molecular-function term also supports glutamine-dependent carbon–nitrogen ligase activity through GMPS and PFAS (GO:MF carbon-nitrogen ligase activity, with glutamine as amido-N-donor; q_global = 0.0416). STRING independently supports purine biosynthesis, GMP biosynthesis, purine metabolism and glutamine amidotransferase biology (6 supplementary STRING terms; within-query FDR 0.002–0.034). Thus, the module most plausibly reflects coordinated cellular nucleotide production rather than a secreted or extracellular process. ALDH18A1 contributes a glutamine-family metabolic connection in supplementary STRING evidence (STRING Process Glutamine family amino acid metabolic process; within-query FDR = 0.0358), while FKBP4 is not supported by the listed GO or STRING functional terms.

**Cell composition.** This is not a plasma-protein or secreted-protein module: none of the genes is annotated as secreted. The HPA profile instead indicates a mixture of broadly detected intracellular proteins and cell-type-enhanced genes. Several genes have low tissue specificity, while GMPS and ALDH18A1 show tissue enhancement and the module includes cell-type associations involving spermatogenic cells, salivary acinar cells, epithelial cells and erythrocyte progenitors. PFAS has immune-cell enhancement in neutrophils, whereas the other genes have low immune-cell specificity. This pattern is more consistent with intracellular metabolic programs expressed across multiple cell types than with a blood-cell-specific module, although shared cellular composition or differing cell-type representation in circulatory-system and liver samples could contribute to the observed conservation. The liver protein evidence is compatible with several module proteins being present in liver, but it does not establish that hepatocytes alone generate the co-abundance signal.

**GO/KEGG enrichment**: 9 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP GMP biosynthetic process | 0.00551 | GMPS, IMPDH2, PFAS |
| GO:BP purine nucleoside monophosphate biosynthetic process | 0.00897 | GMPS, IMPDH2, PFAS |
| GO:BP purine ribonucleoside monophosphate biosynthetic process | 0.00897 | GMPS, IMPDH2, PFAS |
| GO:BP ribonucleoside monophosphate biosynthetic process | 0.0158 | GMPS, IMPDH2, PFAS |
| GO:BP GMP metabolic process | 0.0158 | GMPS, IMPDH2, PFAS |
| GO:BP nucleoside monophosphate biosynthetic process | 0.0186 | GMPS, IMPDH2, PFAS |
| GO:BP purine nucleoside monophosphate metabolic process | 0.0365 | GMPS, IMPDH2, PFAS |
| GO:BP purine ribonucleoside monophosphate metabolic process | 0.0365 | GMPS, IMPDH2, PFAS |
| GO:MF carbon-nitrogen ligase activity, with glutamine as amido-N-donor | 0.0416 | GMPS, PFAS |

### STRING and hu.MAP

The module contains a directly supported STRING relationship between GMPS and IMPDH2, and another between GMPS and ALDH18A1. The GMPS–IMPDH2 connection is especially concordant with the biochemical pathway because IMPDH2 produces the intermediate used by GMPS to make GMP. The observed co-abundance neighborhood also links GMPS with FKBP4 and PFAS, but those relationships are not listed as high-confidence STRING interactions here. No hu.MAP complex contains multiple module members. Therefore, the module has a validated biochemical core centered on GMPS, IMPDH2 and PFAS, plus additional co-abundance relationships that may reflect shared regulation, cellular composition, or metabolic state rather than a demonstrated physical complex.

**STRING interactions (score >= 0.7)**: 2 of 10 gene pairs: ALDH18A1–GMPS (0.909); GMPS–IMPDH2 (0.998)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Purine biosynthesis (FDR = 0.002, 3 genes); RCTM Purine ribonucleoside monophosphate biosynthesis (FDR = 0.0045, 3 genes); Keyword GMP biosynthesis (FDR = 0.011, 2 genes); Process GMP biosynthetic process (FDR = 0.0257, 3 genes); KEGG Purine metabolism (FDR = 0.0272, 3 genes); Keyword Glutamine amidotransferase (FDR = 0.034, 2 genes); Process Glutamine family amino acid metabolic process (FDR = 0.0358, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The biological pathway itself is established and is not a new discovery: GMPS, IMPDH2 and PFAS are well-known purine-biosynthetic enzymes, and the enrichment and STRING results recover that expected biology. The potentially novel aspect is the conservation of this particular co-abundance module across circulatory-system and liver, including its association with FKBP4 and ALDH18A1. Because those broader module relationships are not represented in the supplied STRING or hu.MAP evidence, they may be under-characterized, but absence from those resources does not prove novelty. A defensible conclusion is that this is a potentially informative cross-tissue co-abundance arrangement of an established metabolic program, not proof of a newly discovered pathway or protein complex.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of intracellular guanine-nucleotide supply in cells represented in both circulatory-system and liver samples. In this model, PFAS supports upstream de novo purine synthesis, IMPDH2 channels IMP toward XMP, and GMPS completes GMP production; ALDH18A1 may couple this signal to glutamine and mitochondrial amino-acid metabolism, while FKBP4 may mark a shared protein-folding or cellular state program rather than directly catalyze nucleotide synthesis. The cross-tissue signal could therefore arise from a conserved metabolic response combined with shared cell-type composition. This remains a hypothesis: the provided data establish co-abundance and pathway concordance, but do not demonstrate causal regulation, physical binding for every module edge, or a specific cellular source.

### Important genes

#### GMPS

- **Related proteins** (co-abundance neighbors): FKBP4 (0.82), ALDH18A1 (0.81), PFAS (0.80); STRING partners: ALDH18A1 (0.909), IMPDH2 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: guanosine monophosphate synthase. In the de novo synthesis of purine nucleotides, IMP is the branch point metabolite at which point the pathway diverges to the synthesis of either guanine or adenine nucleotides. In the guanine nucleotide pathway, there are 2 enzymes involved in converting IMP to GMP, namely IMP dehydrogenase (IMPD1), which catalyzes the oxidation of IMP to XMP, and GMP synthetase, which catalyzes the amination of …
- **Diseases (Open Targets)**: rheumatoid arthritis (0.277); nephrotic syndrome (0.259); lupus nephritis (0.259); rhabdomyosarcoma (0.247); hepatocellular carcinoma (0.237)
- **Europe PMC papers**: 5161
- **Why important**: GMPS is the central network hub in the module, connecting the other module members in the co-abundance graph and having STRING support with ALDH18A1 and IMPDH2. It appears in every globally significant GO term (9 globally significant GO/KEGG terms, q_global 0.00551–0.0416; see the table) and every listed STRING enrichment (7 supplementary STRING terms; within-query FDR 0.002–0.0358). Its established function is the glutamine-dependent conversion of XMP to GMP, making it the clearest biochemical anchor. It also has the largest literature volume among the module genes and disease links spanning inflammatory, renal and hepatic disease contexts.
- **Conclusion**: Established conclusion: GMPS is the most credible organizing gene for the module's purine and GMP biosynthetic interpretation. Hypothesis: its hub position may reflect coordinated control of guanine nucleotide demand across the two tissues, but the co-abundance data do not establish that GMPS drives the other genes.

#### IMPDH2

- **Related proteins** (co-abundance neighbors): FKBP4 (0.82); STRING partners: GMPS (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inosine monophosphate dehydrogenase 2. This gene encodes the rate-limiting enzyme in the de novo guanine nucleotide biosynthesis. It is thus involved in maintaining cellular guanine deoxy- and ribonucleotide pools needed for DNA and RNA synthesis. The encoded protein catalyzes the NAD-dependent oxidation of inosine-5'-monophosphate into xanthine-5'-monophosphate, which is then converted into guanosine-5'-monophosphate. This gene is up-…
- **Diseases (Open Targets)**: acute lymphoblastic leukemia (0.529); Crohn disease (0.447); acute myeloid leukemia (0.421); lupus nephritis (0.408); myelodysplastic syndrome (0.403)
- **Europe PMC papers**: 1438
- **Why important**: IMPDH2 is part of the globally significant purine and GMP biosynthesis core (8 globally significant GO/KEGG terms, q_global 0.00551–0.0365; see the table) and is supported by the corresponding STRING enrichments (5 supplementary STRING terms; within-query FDR 0.002–0.0272). It catalyzes the rate-limiting oxidation of IMP toward XMP, directly preceding GMPS in guanine nucleotide production. Its STRING relationship with GMPS is particularly strong in the supplied evidence, and its disease associations include hematologic, inflammatory and renal disorders. Its literature volume is substantial.
- **Conclusion**: Established conclusion: IMPDH2 provides a mechanistically coherent upstream partner for GMPS and strongly supports the module's guanine-nucleotide interpretation. Hypothesis: coordinated IMPDH2 and GMPS abundance could tune guanine-nucleotide availability, although pathway flux was not measured.

#### PFAS

- **Related proteins** (co-abundance neighbors): GMPS (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoribosylformylglycinamidine synthase. Purines are necessary for many cellular processes, including DNA replication, transcription, and energy metabolism. Ten enzymatic steps are required to synthesize inosine monophosphate (IMP) in the de novo pathway of purine biosynthesis. The enzyme encoded by this gene catalyzes the fourth step of IMP biosynthesis. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: dyskeratosis congenita (0.520); Coats plus syndrome (0.455); neurodegenerative disease (0.187); hereditary disease (0.174); retinal disorder (0.118)
- **Europe PMC papers**: 3393
- **Why important**: PFAS is included in every globally significant GO term (9 globally significant GO/KEGG terms, q_global 0.00551–0.0416; see the table) and most of the relevant STRING enrichments (7 supplementary STRING terms; within-query FDR 0.002–0.0358). Its established enzymatic role is an upstream step in de novo IMP synthesis, placing it before the IMPDH2–GMPS branch toward GMP. It is associated with erythrocyte progenitors and neutrophils in HPA, which makes it useful for assessing whether cellular composition contributes to the circulatory-system signal. It also has a substantial literature volume and disease associations involving genome-maintenance and retinal disorders.
- **Conclusion**: Established conclusion: PFAS completes the pathway-level chain from de novo purine synthesis to GMP production and is central to the functional interpretation. Hypothesis: its blood-related cell-type associations may partly influence the cross-tissue co-abundance pattern, but they do not demonstrate a blood-cell origin for the whole module.

#### ALDH18A1

- **Related proteins** (co-abundance neighbors): GMPS (0.81); STRING partners: GMPS (0.909)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 18 family member A1. This gene is a member of the aldehyde dehydrogenase family and encodes a bifunctional ATP- and NADPH-dependent mitochondrial enzyme with both gamma-glutamyl kinase and gamma-glutamyl phosphate reductase activities. The encoded protein catalyzes the reduction of glutamate to delta1-pyrroline-5-carboxylate, a critical step in the de novo biosynthesis of proline, ornithine and arginine. Mutations in …
- **Diseases (Open Targets)**: ALDH18A1-related de Barsy syndrome (0.832); cutis laxa, autosomal dominant 3 (0.816); autosomal recessive complex spastic paraplegia type 9B (0.814); de Barsy syndrome (0.731); autosomal dominant spastic paraplegia type 9 (0.706)
- **Europe PMC papers**: 1168
- **Why important**: ALDH18A1 is a direct co-abundance neighbor of GMPS and has a high-confidence STRING relationship with GMPS. It is not part of the globally significant GO terms, but STRING supplementary evidence places it in glutamine-family amino-acid metabolism (STRING Process Glutamine family amino acid metabolic process; within-query FDR = 0.0358). Its established function is mitochondrial production of pyrroline-carboxylate and support of proline, ornithine and arginine biosynthesis. It is tissue-enhanced in salivary gland and cell-type-enhanced in salivary acinar cells, and its disease associations include well-characterized inherited connective-tissue and neuromuscular syndromes.
- **Conclusion**: Established conclusion: ALDH18A1 supplies a plausible metabolic context for the module but is not a primary GO-enrichment driver. Hypothesis: its association with GMPS may indicate coupling between mitochondrial amino-acid metabolism and cytosolic purine production, or may reflect shared cell-type composition; this coupling requires direct metabolic testing.

#### FKBP4

- **Related proteins** (co-abundance neighbors): GMPS (0.82), IMPDH2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FKBP prolyl isomerase 4. The protein encoded by this gene is a member of the immunophilin protein family, which play a role in immunoregulation and basic cellular processes involving protein folding and trafficking. This encoded protein is a cis-trans prolyl isomerase that binds to the immunosuppressants FK506 and rapamycin. It has high structural and functional similarity to FK506-binding protein 1A (FKBP1A), but unlike …
- **Diseases (Open Targets)**: testicular disorder (0.500); hypogonadism (0.349); aging (0.326); male reproductive organ cancer (0.228); chronic atrophic gastritis (0.218)
- **Europe PMC papers**: 1413
- **Why important**: FKBP4 is the second-degree network connector linking GMPS and IMPDH2 in the module co-abundance graph, yet it has no listed globally significant GO term, STRING functional enrichment or STRING interaction. Its established function concerns immunophilin biology, protein folding and intracellular trafficking, and it is detected in liver tissue by HPA. Its cell-type enhancement across epithelial and spermatogenic contexts and its disease associations involving reproductive disorders distinguish it from the purine enzymes. Its literature volume is moderate relative to GMPS.
- **Conclusion**: Established conclusion: FKBP4 is a potentially informative module-context gene rather than an established purine-biosynthesis component. Hypothesis: FKBP4 may report a shared proteostasis, differentiation or cellular-state program that co-varies with nucleotide demand, but its role in the module is currently correlative and should not be interpreted as a direct biochemical link.

## Module 15

**Tissue pair**: circulatory_system and liver  
**Genes (5)**: KRT10, KRT9, KRT2, KRT1, KRT5

### Function

This is a coherent epithelial structural module centered on keratin intermediate filaments and epidermal differentiation. The primary GO and KEGG evidence is unusually consistent: every module gene contributes to keratin-filament or intermediate-filament organization (GO:CC keratin filament; q_global = 9.47e-08), (GO:BP intermediate filament organization; q_global = 5.66e-07), (GO:BP intermediate filament-based process; q_global = 1.48e-06), (GO:BP intermediate filament cytoskeleton organization; q_global = 1.48e-06), (GO:CC intermediate filament; q_global = 4.05e-06), (GO:CC intermediate filament cytoskeleton; q_global = 8.96e-06), cornified-envelope formation (KEGG Cornified envelope formation - Homo sapiens (human); q_global = 1.75e-05), skin and epidermis development (GO:BP skin development; q_global = 4.49e-05), (GO:BP epidermis development; q_global = 5.04e-05), and cadherin signaling (KEGG Cadherin signaling - Homo sapiens (human); q_global = 0.000118). The module also supports keratinocyte and epithelial differentiation (GO:BP keratinocyte differentiation; q_global = 0.000446), (GO:BP epidermal cell differentiation; q_global = 0.000744), (GO:BP epithelial cell differentiation; q_global = 0.000968), keratinization (GO:BP keratinization; q_global = 0.00132), and cytoskeletal organization (GO:BP cytoskeleton organization; q_global = 0.0351). Thus, its best-supported interpretation is a structural keratinization and epithelial-barrier program rather than a liver-specific metabolic or circulatory function. The shared co-abundance pattern is biologically internally consistent, but it does not by itself establish that these genes act as a novel functional unit in either tissue.

**Cell composition.** The module is strongly epithelial and skin-associated rather than plasma-protein, secreted-protein, blood-cell, or broadly expressed housekeeping composition. HPA assigns most genes to skin and suprabasal keratinocytes, with KRT5 also associated with basal and other squamous epithelial cell types. KRT9 has lymphoid-tissue enrichment in the supplied HPA summary, but its gene description identifies terminally differentiated palmoplantar epidermis as its characteristic expression context. One gene, KRT10, is reported as secreted in other tissues, but the module as a whole is not a secreted-protein module. HPA reports no liver protein detection for any module gene. The apparent conservation between circulatory_system and liver therefore may reflect epithelial material, epithelial-cell admixture, tissue-interface signal, or sample contamination rather than a resident liver or blood-cell program. The HPA blood-cell annotations are mixed and do not override the much stronger skin and keratinocyte pattern.

**GO/KEGG enrichment**: 25 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC keratin filament | 9.47e-08 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament organization | 5.66e-07 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:MF structural constituent of skin epidermis | 6.57e-07 | KRT1, KRT10, KRT2, KRT5 |
| GO:BP intermediate filament-based process | 1.48e-06 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament cytoskeleton organization | 1.48e-06 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:CC intermediate filament | 4.05e-06 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:CC intermediate filament cytoskeleton | 8.96e-06 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| KEGG Cornified envelope formation - Homo sapiens (human) | 1.75e-05 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP skin development | 4.49e-05 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP epidermis development | 5.04e-05 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| KEGG Cadherin signaling - Homo sapiens (human) | 0.000118 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP keratinocyte differentiation | 0.000446 | KRT1, KRT10, KRT2, KRT5 |
| GO:BP epidermal cell differentiation | 0.000744 | KRT1, KRT10, KRT2, KRT5 |
| GO:BP epithelial cell differentiation | 0.000968 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP keratinization | 0.00132 | KRT1, KRT2, KRT5 |

### STRING and hu.MAP

STRING independently supports the same interpretation: the module genes show high-confidence associations among the KRT1, KRT10, KRT2, and KRT5 pairs, and STRING functional annotations identify keratin filaments, intermediate-filament proteins, cornified-envelope formation, and structural constituents of skin epidermis (STRING Component Keratin filament; within-query FDR = 1.45e-08) through (STRING Function Structural constituent of skin epidermis; within-query FDR = 3.13e-06). These relationships are largely established keratin-family biology, not evidence that the co-abundance analysis discovered new physical interactions. KRT9 is connected in the module pattern to KRT1 and KRT10, but it has no reported STRING partner in the supplied interaction summary, so that part of the network is less supported by the external interaction database. No hu.MAP complex contains multiple module members. Overall, the network is consistent with a known keratin-family structural network, while the absence of a hu.MAP complex argues against interpreting it as a demonstrated multiprotein complex.

**STRING interactions (score >= 0.7)**: 6 of 10 gene pairs: KRT1–KRT10 (0.999); KRT1–KRT2 (0.956); KRT1–KRT5 (0.923); KRT10–KRT2 (0.904); KRT10–KRT5 (0.793); KRT2–KRT5 (0.871)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Keratin filament (FDR = 1.45e-08, 5 genes); COMPARTMENTS Keratin filament (FDR = 1.54e-08, 5 genes); Keyword Keratin (FDR = 1.85e-08, 5 genes); SMART Intermediate filament protein (FDR = 2.53e-08, 5 genes); Keyword Intermediate filament (FDR = 3.57e-08, 5 genes); InterPro Intermediate filament protein, conserved site (FDR = 1.51e-07, 5 genes); InterPro Intermediate filament, rod domain (FDR = 1.51e-07, 5 genes); RCTM Formation of the cornified envelope (FDR = 3.56e-07, 5 genes); DISEASES Epidermolytic hyperkeratosis (FDR = 1.37e-06, 4 genes); Function Structural constituent of skin epidermis (FDR = 3.13e-06, 4 genes); PMID (2025) Mass spectrometric detection of keratins in tear fluid. (FDR = 7.25e-06, 5 genes); PMID (2023) Key Factors in the Complex and Coordinated Network of Skin Keratinization: Their Significance and Involvement in Common Skin Conditions. (FDR = 7.25e-06, 5 genes); PMID (2022) A metatranscriptomic approach to explore longitudinal tissue specimens from non-healing diabetes related foot ulcers. (FDR = 7.25e-06, 5 genes); PMID (2022) Palmoplantar Keratoderma: A Molecular Genetic Analysis of Family Cases. (FDR = 7.25e-06, 5 genes); PMID (2021) Keratin Biomaterials in Skin Wound Healing, an Old Player in Modern Medicine: A Mini Review. (FDR = 7.25e-06, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be claimed as a new keratin mechanism. Its function, tissue specificity, disease relevance, and several pairwise relationships are already well established in the supplied annotations and in the searched literature. The co-abundance observation may still be a new dataset-specific finding because this particular shared pattern across circulatory_system and liver is not demonstrated to be a previously described module. However, that possibility requires independent replication, assessment of epithelial-cell or sample-composition effects, and comparison with published co-expression studies. Absence from hu.MAP, and absence of a STRING partner for KRT9, cannot by themselves establish novelty. The most defensible conclusion is novelty of the observed cross-tissue co-abundance context is possible, but novelty of the underlying biology is unlikely.

**Hypothesis.** Hypothesis: the conserved signal is generated by coordinated abundance of epithelial keratin material, probably from skin-like or other stratified epithelial cells or fragments represented in the sampled material, rather than by a liver-resident pathway. KRT5 may mark a basal epithelial component, while KRT1, KRT10, and KRT2 represent suprabasal differentiation and cornification, with KRT9 contributing a palmoplantar or terminal-differentiation signature. In circulatory samples, this could reflect circulating epithelial proteins or cellular material; in liver-associated samples, it could reflect epithelial admixture, tissue-interface material, or technical carryover. This hypothesis predicts that the module should track epithelial-cell markers and sample composition more strongly than hepatocyte metabolic markers, and should be tested with cell deconvolution, independent cohorts, and protein-level validation.

Web sources: https://www.proteinatlas.org/ENSG00000186081-KRT5/tissue/liver; https://www.omim.org/entry/600194; https://www.genecards.org/card/KRT1; https://pmc.ncbi.nlm.nih.gov/articles/PMC11484123/; https://link.springer.com/article/10.1186/s40246-021-00374-9

### Important genes

#### KRT1

- **Related proteins** (co-abundance neighbors): KRT9 (0.94), KRT10 (0.89), KRT2 (0.80); STRING partners: KRT10 (0.999), KRT2 (0.956), KRT5 (0.923)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 is a central, highly connected member of the module and participates in every primary enrichment theme listed for the module (GO:CC keratin filament; q_global = 9.47e-08) through (GO:BP cytoskeleton organization; q_global = 0.0351). It is skin-enriched and associated with suprabasal keratinocytes in HPA, and its supplied functional annotation places it in epithelial intermediate filaments, keratinization, and epidermal differentiation. It has extensive literature support and disease associations involving epidermolytic ichthyosis and palmoplantar keratoderma. External literature also supports its heterodimerization with KRT10 and, in palmoplantar skin, with KRT9.
- **Conclusion**: Established evidence supports KRT1 as a core structural and suprabasal epithelial marker, and as an important network hub in this module. The hypothesis that it indicates epithelial carryover in the circulatory_system and liver datasets is plausible, but the module data do not prove the source of the KRT1 signal.

#### KRT10

- **Related proteins** (co-abundance neighbors): KRT1 (0.89), KRT9 (0.85), KRT2 (0.82); STRING partners: KRT1 (0.999), KRT2 (0.904), KRT5 (0.793)
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 10. This gene encodes a member of the type I (acidic) cytokeratin family, which belongs to the superfamily of intermediate filament (IF) proteins. Keratins are heteropolymeric structural proteins which form the intermediate filament. These filaments, along with actin microfilaments and microtubules, compose the cytoskeleton of epithelial cells. Mutations in this gene are associated with epidermolytic …
- **Diseases (Open Targets)**: epidermolytic hyperkeratosis 2A, autosomal dominant (0.787); epidermolytic ichthyosis (0.772); congenital reticular ichthyosiform erythroderma (0.727); ichthyosis, annular epidermolytic 1 (0.647); annular epidermolytic ichthyosis (0.642)
- **Europe PMC papers**: 2736
- **Why important**: KRT10 is among the most connected module genes and is linked to KRT1, KRT2, and KRT5 in STRING. It is skin-enriched and associated with suprabasal keratinocytes, while its supplied annotation identifies an acidic type I cytokeratin involved in intermediate-filament organization, keratinocyte differentiation, cornification, and epidermis development. It has substantial literature support and established associations with epidermolytic hyperkeratosis and related ichthyoses. The searched literature specifically supports KRT1-KRT10 heterodimerization.
- **Conclusion**: Established evidence supports KRT10 as a major suprabasal differentiation and cornification component. Its presence in this cross-tissue module is more consistent with epithelial material or cell admixture than with a liver-specific function, although that source interpretation remains a hypothesis.

#### KRT5

- **Related proteins** (co-abundance neighbors): KRT2 (0.85); STRING partners: KRT1 (0.923), KRT10 (0.793), KRT2 (0.871)
- **HPA**: Group enriched; Group enriched; blood Immune cell enriched; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 5. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the basal layer of the epidermis with family member KRT14. Mutations in t…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 2C, localized (0.768); epidermolysis bullosa simplex 2A, generalized severe (0.761); epidermolysis bullosa simplex 2B, generalized intermediate (0.761); epidermolysis bullosa simplex 2F, with mottled pigmentation (0.729); Dowling-Degos disease 1 (0.697)
- **Europe PMC papers**: 7044
- **Why important**: KRT5 provides the basal epithelial dimension of the module. It is connected to KRT2 within the module and has established STRING associations with KRT1 and KRT10. HPA places it across skin and other squamous epithelial contexts and associates it with basal keratinocytes. Its supplied annotation links it to epidermis development, mechanical-stimulus response, keratinization, migration, and intermediate-filament polymerization. It has extensive literature support and strong disease associations with epidermolysis bullosa simplex and related disorders.
- **Conclusion**: Established evidence supports KRT5 as a basal epithelial structural marker and a biologically informative complement to the suprabasal keratins. Its participation suggests that the module spans epithelial differentiation states rather than representing a narrowly liver-specific program. Whether this reflects true biological material in the samples or admixture cannot be resolved from the module alone.

#### KRT2

- **Related proteins** (co-abundance neighbors): KRT5 (0.85), KRT10 (0.82), KRT1 (0.80); STRING partners: KRT1 (0.956), KRT10 (0.904), KRT5 (0.871)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location Intermediate filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 2. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is expressed largely in the upper spinous layer of epidermal keratinocytes and mutations in this gene …
- **Diseases (Open Targets)**: superficial epidermolytic ichthyosis (0.815); exfoliative ichthyosis (0.358); Palmoplantar hyperkeratosis (0.267); hereditary disease (0.193); Vertigo (0.145)
- **Europe PMC papers**: 7459
- **Why important**: KRT2 is highly connected within the module and contributes to the primary keratin-filament, epidermal-development, keratinocyte-differentiation, and keratinization evidence (GO:CC keratin filament; q_global = 9.47e-08) through (GO:BP cytoskeleton organization; q_global = 0.0351). HPA associates it with skin and suprabasal keratinocytes. Its supplied annotation places it in the upper spinous epidermis and links it to epidermis development, keratinization, keratinocyte activation, and proliferation. It has substantial literature support and disease associations including superficial epidermolytic ichthyosis and palmoplantar hyperkeratosis.
- **Conclusion**: Established evidence supports KRT2 as a differentiated epidermal keratin and a strong indicator of the module's epithelial maturation program. Its co-abundance with basal and suprabasal keratins supports a coordinated epithelial signature, but does not establish a new mechanistic role in liver or circulation.

#### KRT9

- **Related proteins** (co-abundance neighbors): KRT1 (0.94), KRT10 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 9. This gene encodes the type I keratin 9, an intermediate filament chain expressed only in the terminally differentiated epidermis of palms and soles. Mutations in this gene cause epidermolytic palmoplantar keratoderma. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: epidermolytic palmoplantar keratoderma, 1 (0.828); palmoplantar keratoderma, epidermolytic (0.682); Localized epidermolytic hyperkeratosis (0.511); Palmoplantar hyperkeratosis (0.456); Palmoplantar keratoderma (0.438)
- **Europe PMC papers**: 773
- **Why important**: KRT9 is the most distinctive tissue-specialized member of the module. It is connected to KRT1 and KRT10 in the module network, contributes to most of the primary keratin and epithelial terms, and is described as a type I keratin restricted to terminally differentiated palmoplantar epidermis. It has a more limited literature volume than the other selected genes but a focused disease association with epidermolytic palmoplantar keratoderma. Unlike the other prominent pairings, it has no STRING partner in the supplied summary, making it informative both biologically and as a potentially less externally supported edge component.
- **Conclusion**: Established evidence supports KRT9 as a specialized terminal-differentiation marker that strengthens the skin-like interpretation. Its appearance in a circulatory_system and liver shared module is especially compatible with an epithelial-source or admixture hypothesis, but the supplied evidence does not identify whether it reflects true sample biology, contamination, or correlated technical abundance.
