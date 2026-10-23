# Conserved co-abundance modules: autonomic_nervous_system and kidney

## Module 0

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (34)**: MPG, AKAP8, ANP32E, ATG4B, CPSF1, EIF2B4, EIF3L, ELP1, EPS15, GAPVD1, TUBGCP3, CPOX, IRGQ, LRWD1, NR2C2AP, NUP43, ORC3, PITPNB, PPIL1, PPIL2, PUM1, UPF1, UPF2, POLR3A, SARM1, SIN3A, SUPT5H, NARS1, TIMELESS, UBE2T, UBR1, UHRF1, URGCP, YTHDC2

### Function

The module does not have a GO or KEGG term that passes global correction, so its function should be inferred cautiously rather than assigned from enrichment. Its genes collectively point toward core nuclear and cytoplasmic information-processing functions: RNA maturation and surveillance, post-transcriptional regulation, transcription, translation, DNA replication and repair, chromatin organization, protein quality control, and autophagy. The network is a sparse connected scaffold rather than a densely interconnected pathway. Its most coherent functional threads are RNA metabolism centered on YTHDC2, UPF1, UPF2, PUM1, CPSF1, and PPIL proteins; genome maintenance centered on ORC3, LRWD1, UHRF1, UBE2T, MPG, and TIMELESS; and transcriptional or translational support involving POLR3A, SUPT5H, EIF3L, and NARS1. SARM1 and ELP1 provide potentially relevant links to neuronal or autonomic biology, but the module as a whole is better interpreted as a broadly expressed cellular maintenance and gene-expression module than as a tissue-specific autonomic or kidney pathway. The absence of globally enriched terms does not invalidate the module; it indicates that the genes are functionally heterogeneous or that the module is too diffuse for pathway enrichment to resolve one dominant process.

**Cell composition.** The HPA evidence argues against a plasma or secreted-protein module: no module gene is annotated as secreted, and the proteins are predominantly intracellular, especially nuclear or cytoplasmic. Most genes have low tissue specificity and low immune-cell specificity, consistent with broadly expressed housekeeping or cell-maintenance functions. Kidney protein detection is common among the genes with available kidney data, whereas matching HPA protein data are unavailable for autonomic nervous system tissue, so this does not establish tissue-specific protein expression. Some genes show enhancement in progenitor, germline, neuronal, epithelial, or selected immune-related cell types, including UHRF1, UBE2T, TIMELESS, ANP32E, and SARM1. The repeated progenitor and germline signals could reflect proliferative or developmental cell states, while the limited immune-related signals do not by themselves support a blood-cell explanation. A shared cell-state or general cellular-composition effect remains plausible and should be tested with cell-type deconvolution and independent tissue cohorts.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING evidence supports a small set of established protein relationships within the module, including the very strong UPF1–UPF2 relationship, the ORC3–LRWD1 relationship, CPSF1–YTHDC2, PPIL1–PPIL2, UBE2T–UHRF1, and ELP1–MPG. These links provide credible local anchors for RNA surveillance, replication and chromatin control, RNA processing, ubiquitin-dependent genome maintenance, and tRNA or DNA quality-control biology. The hu.MAP evidence independently supports repeated co-membership of ORC3 and LRWD1 in origin-recognition or chromatin-associated complexes, and repeated co-membership of PUM1 and UPF1 in RNA-processing or RNA-regulatory complexes. SUPT5H and POLR3A also occur together in a transcription-related hu.MAP complex. Because most module pairs lack high-confidence STRING support and the hu.MAP complexes usually contain only a subset of module members, the evidence favors several known molecular islands connected by co-abundance rather than one fully established physical complex. The module therefore contains real known interaction structure, but its complete cross-tissue network is not demonstrated by current interaction databases.

**STRING interactions (score >= 0.7)**: 6 of 561 gene pairs: CPSF1–YTHDC2 (0.874); ELP1–MPG (0.749); LRWD1–ORC3 (0.995); PPIL1–PPIL2 (0.822); UBE2T–UHRF1 (0.709); UPF1–UPF2 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00849.1 (ORC3, LRWD1; 2/4); huMAP3_06528.1 (ORC3, LRWD1; 2/4); huMAP3_09702.1 (ORC3, LRWD1; 2/5); huMAP3_11720.1 (ORC3, LRWD1; 2/5); huMAP3_08338.1 (PUM1, UPF1; 2/5); huMAP3_09909.1 (ORC3, LRWD1; 2/6); huMAP3_12035.1 (ORC3, LRWD1; 2/6); huMAP3_10905.1 (PUM1, UPF1; 2/6); huMAP3_11726.1 (ORC3, LRWD1; 2/7); huMAP3_05758.1 (PUM1, UPF1; 2/7); huMAP3_06975.1 (PUM1, UPF1; 2/31); huMAP3_10625.1 (PUM1, UPF1; 2/57); huMAP3_11092.1 (SUPT5H, POLR3A; 2/65)

### Novelty

The module may represent a new cross-tissue co-abundance pattern, but the fact sheet does not establish it as a wholly new molecular mechanism. Its constituent relationships are partly familiar: the ORC3–LRWD1 pair, the UPF1–UPF2 pair, and the PUM1–UPF1 and POLR3A–SUPT5H complex associations have database support. Several genes are also well studied and have established roles in RNA metabolism, DNA replication, repair, translation, or autonomic biology. What may be novel is the coordinated association of these otherwise distinct cellular programs across autonomic nervous system and kidney samples. Absence of a matching STRING or hu.MAP complex would not prove novelty, and the lack of globally significant GO or KEGG enrichment likewise cannot distinguish novelty from heterogeneity. A defensible claim is that the cross-tissue co-abundance configuration is potentially novel and merits replication, not that the underlying interactions or functions are newly discovered.

**Hypothesis.** Hypothesis: the module reflects a shared cellular stress or maintenance state in which RNA quality control, transcriptional output, DNA replication and repair, chromatin regulation, translation, and autophagy are coordinated. YTHDC2, UPF1, UPF2, PUM1, and CPSF1 could couple RNA processing, surveillance, and translation; ORC3, LRWD1, UHRF1, UBE2T, MPG, and TIMELESS could preserve genome integrity and replication competence; and ELP1, SARM1, ATG4B, and GAPVD1 could connect this state to autonomic signaling, organelle quality control, and vesicle or autophagy-related processes. In kidney this may represent a general epithelial maintenance or repair state, while in autonomic nervous system it may represent neuronal stress resilience or axonal maintenance. The shared abundance pattern could also arise from common proliferative or progenitor-cell admixture, so this hypothesis requires validation by cell-resolved expression, perturbation, and replication in independent samples.

### Important genes

#### YTHDC2

- **Related proteins** (co-abundance neighbors): UPF2 (0.92), PUM1 (0.88), UPF1 (0.86), PITPNB (0.84), CPOX (0.83), CPSF1 (0.81); STRING partners: CPSF1 (0.874)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: YTH N6-methyladenosine RNA binding protein C2. This gene encodes a member of the DEAH (Asp-Glu-Ala-His) subfamily of proteins, part of the DEAD (Asp-Glu-Ala-Asp) box family of RNA helicases. The encoded protein binds to N6-methyladenosine, a common modified RNA nucleotide that is enriched in the stop codons and 3' UTRs of eukaryotic messenger RNAs. Binding of proteins to this modified nucleotide may regulate mRNA translation and stability. Thi…
- **Diseases (Open Targets)**: Hyperhidrosis (0.321); neurodegenerative disease (0.304); preeclampsia (0.277); brain compression (0.211); edema (0.211)
- **Europe PMC papers**: 3247
- **Why important**: YTHDC2 is among the most connected genes in the module and links UPF1, UPF2, PUM1, CPSF1, PITPNB, and CPOX. Its annotated RNA-helicase and modified-RNA-binding functions place it at the intersection of RNA fate, translation, and surveillance. It has substantial literature and disease-oriented attention, while its low tissue specificity and kidney detection support a broadly expressed cellular role rather than a uniquely tissue-restricted marker.
- **Conclusion**: Established evidence supports YTHDC2 as a central RNA-regulatory candidate in the module. Its position suggests that it may coordinate the RNA-processing branch, but a direct causal role in the shared autonomic nervous system and kidney co-abundance pattern remains a hypothesis.

#### UPF1

- **Related proteins** (co-abundance neighbors): YTHDC2 (0.86), EPS15 (0.81); STRING partners: UPF2 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_08338.1, huMAP3_10905.1, huMAP3_05758.1, huMAP3_06975.1, huMAP3_10625.1
- **Function (MyGene.info)**: UPF1 RNA helicase and ATPase. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons.…
- **Diseases (Open Targets)**: Intellectual disability (0.437); Global developmental delay (0.426); High anterior hairline (0.425); Frontal bossing (0.425); Hypertelorism (0.425)
- **Europe PMC papers**: 4252
- **Why important**: UPF1 is connected to YTHDC2 and EPS15 and is supported by a very strong STRING relationship with UPF2. It is a core factor in nonsense-mediated messenger-RNA decay, RNA export, translational termination, and broader RNA quality control. It also appears repeatedly with PUM1 in hu.MAP complexes and has extensive literature and developmental disease associations.
- **Conclusion**: Established evidence makes UPF1 a strong anchor for the module's RNA-surveillance interpretation. The network supports a role for RNA quality control, but does not show that altered UPF1 activity drives the tissue-pair association.

#### ORC3

- **Related proteins** (co-abundance neighbors): SARM1 (0.88); STRING partners: LRWD1 (0.995)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_00849.1, huMAP3_06528.1, huMAP3_09702.1, huMAP3_11720.1, huMAP3_09909.1, huMAP3_12035.1, huMAP3_11726.1
- **Function (MyGene.info)**: origin recognition complex subunit 3. The origin recognition complex (ORC) is a highly conserved six subunits protein complex essential for the initiation of the DNA replication in eukaryotic cells. Studies in yeast demonstrated that ORC binds specifically to origins of replication and serves as a platform for the assembly of additional initiation factors such as Cdc6 and Mcm proteins. The protein encoded by this gene is a subunit of …
- **Diseases (Open Targets)**: neurodegenerative disease (0.537); benign urinary system neoplasm (0.192); kidney failure (0.092); hypothyroidism (0.078); developmental dysplasia of the hip 4 (0.071)
- **Europe PMC papers**: 534
- **Why important**: ORC3 is paired with LRWD1 by a high-confidence STRING relationship and recurs with LRWD1 across many hu.MAP origin-recognition and chromatin-associated complexes. Its established function in replication-origin licensing gives the module a clear genome-maintenance component. Its kidney detection and broadly expressed tissue profile are compatible with a general proliferative or repair-related state.
- **Conclusion**: Established evidence supports ORC3 as a replication-initiation component and as one of the most convincing physical-complex anchors in the module. Connecting this replication machinery to RNA surveillance across both tissues is a plausible systems-level interpretation, not an established mechanism.

#### LRWD1

- **Related proteins** (co-abundance neighbors): POLR3A (0.84); STRING partners: ORC3 (0.995)
- **HPA**: Tissue enriched; Group enriched; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in none
- **hu.MAP 3.0**: huMAP3_00849.1, huMAP3_06528.1, huMAP3_09702.1, huMAP3_11720.1, huMAP3_09909.1, huMAP3_12035.1, huMAP3_11726.1
- **Function (MyGene.info)**: leucine rich repeats and WD repeat domain containing 1. The protein encoded by this gene interacts with components of the origin recognition complex (ORC) and regulates the formation of the prereplicative complex. The encoded protein stabilizes the ORC and therefore aids in DNA replication. This protein is required for the G1/S phase transition of the cell cycle. In addition, the encoded protein binds to trimethylated histone H3 in heterochromatin and …
- **Diseases (Open Targets)**: Ewing sarcoma (0.047); type 2 diabetes mellitus (0.032); testicular cancer (0.024); embryonal carcinoma (0.011); testicular embryonal carcinoma (0.009)
- **Europe PMC papers**: 205
- **Why important**: LRWD1 is the partner of ORC3 in STRING and hu.MAP and is annotated to stabilize the origin-recognition complex, regulate replication licensing, and associate with heterochromatin. Its tissue-enriched testis signal and germ-cell associations indicate that its abundance can also track specialized proliferative or developmental states, which is important when interpreting a cross-tissue module.
- **Conclusion**: Established evidence supports LRWD1 as a replication and chromatin regulator. In this module it likely marks the genome-maintenance branch, while its germline-associated expression raises the alternative possibility that cell-state composition contributes to the observed co-abundance.

#### ELP1

- **Related proteins** (co-abundance neighbors): TUBGCP3 (0.82); STRING partners: MPG (0.749)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: elongator acetyltransferase complex subunit 1. The protein encoded by this gene is a scaffold protein and a regulator for three different kinases involved in proinflammatory signaling. The encoded protein can bind NF-kappa-B-inducing kinase and I-kappa-B kinases through separate domains and assemble them into an active kinase complex. Mutations in this gene have been associated with familial dysautonomia. Alternative splicing results in multip…
- **Diseases (Open Targets)**: Riley-Day syndrome (0.807); medulloblastoma (0.721); primary dysautonomia (0.407); hereditary sensory and autonomic neuropathy (0.374); mathematical ability (0.361)
- **Europe PMC papers**: 960
- **Why important**: ELP1 connects to TUBGCP3 and has a STRING relationship with MPG. It is a scaffold associated with the elongator complex, translation-related RNA modification, and inflammatory signaling, and it has a strong established association with familial dysautonomia and other autonomic disorders. Its inclusion is especially relevant because the module spans autonomic nervous system and kidney.
- **Conclusion**: Established evidence supports ELP1 as the most direct autonomic-disease-relevant candidate among the selected genes. Its network connections could link translation and cellular stress to autonomic biology, but the module does not demonstrate that ELP1 explains the shared tissue pattern.

#### SARM1

- **Related proteins** (co-abundance neighbors): ORC3 (0.88), CPSF1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sterile alpha and TIR motif containing 1. Enables NAD+ nucleotidase, cyclic ADP-ribose generating and identical protein binding activity. Involved in NAD catabolic process; positive regulation of neuron death; and response to axon injury. Located in mitochondrion. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hereditary folate malabsorption (0.528); hereditary disease (0.404); age-related macular degeneration (0.246); COVID-19 (0.244); wet macular degeneration (0.174)
- **Europe PMC papers**: 1553
- **Why important**: SARM1 links CPSF1 and ORC3 in the module and is annotated to NAD-related catabolism, axon injury responses, programmed cell death, and dendrite morphogenesis. Its cell-type enhancement in selected neural and hepatic immune-related populations and its kidney detection provide biological relevance to both neuronal injury biology and tissue maintenance. Its literature base is substantial and its autonomic-neural relevance is stronger than that of many other module members.
- **Conclusion**: Established evidence supports SARM1 as a neuronal injury and NAD-metabolism regulator. Its position suggests a possible bridge between RNA processing and neural stress responses, but that bridge is a hypothesis rather than a demonstrated physical or causal pathway.

## Module 1

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (5)**: SLC3A2, PNPT1, RAB8A, RHOG, ZMYM3

### Function

The module does not have a statistically supported GO or KEGG functional label: no GO or KEGG term passed global correction. The gene content instead suggests a heterogeneous cellular-maintenance program involving mitochondrial RNA processing through PNPT1, membrane trafficking and exocytosis through RAB8A, actin organization and polarity signaling through RHOG, chromatin-mediated transcriptional repression through ZMYM3, and amino-acid transport and calcium regulation through SLC3A2. These annotations support biological plausibility but should be treated as gene-level interpretation rather than enrichment evidence. The sparse co-abundance structure links PNPT1 with RHOG and ZMYM3, and links RHOG with RAB8A and RAB8A with SLC3A2. Thus, the most defensible interpretation is a mixed intracellular homeostasis and membrane-trafficking module rather than a narrowly defined pathway.

**Cell composition.** The module is not composed of secreted proteins, and the HPA summary gives low immune-cell specificity for every member. Most genes have low tissue specificity, while RHOG is tissue enhanced in bone marrow and several genes show cell-type-enhanced patterns in specialized cell types. RAB8A is enhanced in megakaryocyte progenitors, megakaryocytes, and platelets; RHOG is enhanced in several myeloid or tissue macrophage-related cell types; ZMYM3 is enhanced in ependymal, granulosa, and Sertoli cells; and SLC3A2 is enhanced in breast lactating, retinal pigment epithelial, and syncytiotrophoblast cells. Kidney protein detection is present for most members where HPA kidney data are available, but there is no autonomic-nervous-system tissue match in the supplied HPA evidence. The pattern therefore does not specifically establish a blood-cell module or a secreted-plasma signal. It is more consistent with broadly distributed cellular proteins combined with cell-type-associated expression, so shared cell composition or general housekeeping biology could contribute to the cross-tissue association.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and no STRING functional-enrichment result was reported. No hu.MAP complex contained multiple module members. Therefore, the co-abundance links are not corroborated here as established physical protein interactions or a known multiprotein complex. The absence of STRING and hu.MAP support does not invalidate the co-abundance pattern; it indicates that the observed relationships may reflect coordinated expression, indirect regulation, shared cell composition, context-dependent interactions, or interactions not represented in those resources.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is potentially novel as a cross-tissue co-abundance pattern because its particular gene combination and topology are not represented by a reported STRING interaction network or a multi-member hu.MAP complex. However, that absence alone cannot establish biological novelty. The individual genes and their broad cellular functions are already well established, and the module lacks globally significant GO or KEGG enrichment, STRING support, and complex-level support. The appropriate conclusion is that this is a novel candidate co-abundance association requiring replication and experimental or independent cohort validation, not a newly discovered molecular complex or pathway.

**Hypothesis.** Hypothesis: the shared signal reflects coordinated cellular remodeling in which RAB8A-dependent membrane trafficking and RHOG-dependent actin and polarity signaling are coupled to SLC3A2-mediated nutrient and calcium handling, while PNPT1 and ZMYM3 represent mitochondrial RNA-quality control and transcriptional-state regulation that accompany this cellular state. The links may be indirect and could also arise from shared cell composition or tissue-state effects. This hypothesis should be tested by replication across cohorts, cell-type-aware analysis, perturbation of the candidate regulators, and measurement of trafficking, cytoskeletal, mitochondrial-RNA, and transporter phenotypes.

### Important genes

#### RHOG

- **Related proteins** (co-abundance neighbors): RAB8A (0.83), PNPT1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ras homolog family member G. This gene encodes a member of the Rho family of small GTPases, which cycle between inactive GDP-bound and active GTP-bound states and function as molecular switches in signal transduction cascades. Rho proteins promote reorganization of the actin cytoskeleton and regulate cell shape, attachment, and motility. The encoded protein facilitates translocation of a functional guanine nucleotide exchange…
- **Diseases (Open Targets)**: atrial fibrillation (0.428); cancer (0.373); kidney transplant (0.296); eosinophilic esophagitis (0.239); cardiac arrhythmia (0.128)
- **Europe PMC papers**: 1929
- **Why important**: RHOG is centrally positioned in the co-abundance subgraph, linking PNPT1 and RAB8A. Its established biology as a Rho-family molecular switch connects actin organization, cell polarity, cell shape, motility, and signaling to the trafficking-related part of the module. It is tissue enhanced in bone marrow and has cell-type-enhanced expression in several myeloid or macrophage-related populations. It also has substantial literature coverage and disease associations including atrial fibrillation, cancer, and kidney transplant.
- **Conclusion**: Established evidence supports RHOG as the strongest integrative signaling candidate in this module because of its network position and cytoskeletal role. The hypothesis that RHOG coordinates the other module members is plausible but unproven; the co-abundance edge is not a demonstrated physical interaction.

#### RAB8A

- **Related proteins** (co-abundance neighbors): RHOG (0.83), SLC3A2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB8A, member RAS oncogene family. The protein encoded by this gene is a member of the RAS superfamily which are small GTP/GDP-binding proteins with an average size of 200 amino acids. The RAS-related proteins of the RAB/YPT family may play a role in the transport of proteins from the endoplasmic reticulum to the Golgi and the plasma membrane. This protein shares 97%, 96%, and 51% similarity with the dog RAB8, mouse MEL, and mouse …
- **Diseases (Open Targets)**: acute respiratory distress syndrome (0.077); non-small cell lung carcinoma (0.076); esophageal cancer (0.076); congenital diarrhea 5 with tufting enteropathy (0.068); inflammatory bowel disease 30 (0.067)
- **Europe PMC papers**: 2105
- **Why important**: RAB8A is centrally positioned between RHOG and SLC3A2. Its established functions include exocytosis, Golgi organization, endocytic recycling, autophagy regulation, axonogenesis, and response to insulin. Its cell-type-enhanced pattern includes megakaryocyte progenitors, megakaryocytes, and platelets, while its tissue specificity is otherwise low. It has substantial literature coverage and provides a mechanistic bridge between cytoskeletal signaling and plasma-membrane transporter biology.
- **Conclusion**: Established evidence supports RAB8A as a trafficking hub and a key interpretive gene. It is reasonable to hypothesize that the RAB8A-centered portion of the module reflects coordinated membrane delivery or recycling, but the supplied data do not establish that RHOG regulates RAB8A or that RAB8A transports SLC3A2 in this module.

#### PNPT1

- **Related proteins** (co-abundance neighbors): ZMYM3 (0.89), RHOG (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polyribonucleotide nucleotidyltransferase 1. The protein encoded by this gene belongs to the evolutionary conserved polynucleotide phosphorylase family comprised of phosphate dependent 3'-to-5' exoribonucleases implicated in RNA processing and degradation. This enzyme is predominantly localized in the mitochondrial intermembrane space and is involved in import of RNA to mitochondria. Mutations in this gene have been associated with combined …
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 13 (0.807); autosomal recessive nonsyndromic hearing loss 70 (0.740); spinocerebellar ataxia type 25 (0.709); deafness (0.676); hearing loss, autosomal recessive (0.634)
- **Europe PMC papers**: 839
- **Why important**: PNPT1 has the highest weighted degree in the module and connects to both RHOG and ZMYM3. It is an evolutionarily conserved mitochondrial polynucleotide phosphorylase involved in mitochondrial RNA processing, degradation, and import. Its established disease associations include combined oxidative phosphorylation deficiency, autosomal recessive nonsyndromic hearing loss, and spinocerebellar ataxia. It has substantial literature coverage and is detected in kidney by HPA.
- **Conclusion**: Established evidence supports PNPT1 as a mitochondrial RNA-quality-control component that broadens the module beyond membrane trafficking. Its placement suggests a possible link between mitochondrial state and the rest of the module, but that cross-compartment mechanism is a hypothesis rather than an established relationship.

#### SLC3A2

- **Related proteins** (co-abundance neighbors): RAB8A (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 3 member 2. This gene is a member of the solute carrier family and encodes a cell surface, transmembrane protein. The protein exists as the heavy chain of a heterodimer, covalently bound through di-sulfide bonds to one of several possible light chains. The encoded transporter plays a role in regulation of intracellular calcium levels and transports L-type amino acids. Alternatively spliced transcript variants…
- **Diseases (Open Targets)**: sensorineural hearing loss disorder (0.370); neurodegenerative disease (0.324); neoplasm (0.117); breast cancer (0.113); breast carcinoma (0.110)
- **Europe PMC papers**: 6815
- **Why important**: SLC3A2 is the membrane-associated amino-acid transporter heavy chain and is connected to RAB8A in the module. Its established functions include amino-acid transport and regulation of intracellular calcium, with transport of several branched or sulfur-containing amino acids represented in the supplied annotations. It is detected in kidney, has cell-type-enhanced expression in several specialized epithelial or trophoblast-related cell types, and has the largest literature volume among the module genes.
- **Conclusion**: Established evidence supports SLC3A2 as a nutrient- and membrane-homeostasis component. Its connection with RAB8A makes coordinated trafficking a plausible explanation, but the module data do not prove a direct regulatory or physical relationship.

#### ZMYM3

- **Related proteins** (co-abundance neighbors): PNPT1 (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger MYM-type containing 3. This gene is located on the X chromosome and is subject to X inactivation. It is highly conserved in vertebrates and most abundantly expressed in the brain. The encoded protein is a component of histone deacetylase-containing multiprotein complexes that function through modifying chromatin structure to keep genes silent. A chromosomal translocation (X;13) involving this gene is associated with X-l…
- **Diseases (Open Targets)**: intellectual developmental disorder, X-linked 112 (0.630); prostate adenocarcinoma (0.562); neurodegenerative disease (0.336); medulloblastoma (0.275); B-cell chronic lymphocytic leukemia (0.247)
- **Europe PMC papers**: 504
- **Why important**: ZMYM3 is the sole neighbor of PNPT1 on a terminal branch of the module and encodes a component of histone-deacetylase-containing chromatin complexes involved in transcriptional repression. It is highly conserved, most abundantly expressed in the brain according to the supplied annotation, and is associated with X-linked intellectual developmental disorder and other disease categories. Its network position makes it potentially informative for cell-state regulation even though its literature volume is lower than that of the other selected genes.
- **Conclusion**: Established evidence supports ZMYM3 as a chromatin-regulatory gene that could mark transcriptional state. The proposed connection between chromatin repression and the mitochondrial or trafficking genes is speculative and should not be interpreted as a demonstrated pathway.

## Module 2

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (44)**: SLC1A5, ASH2L, BAG5, BAZ1A, CANX, NCAPG2, CNPY3, CRNKL1, DNMT1, EFL1, EXOC1, GCSH, GRSF1, GTF2I, HELLS, IMP4, KDM3B, MKI67, LYAR, MESD, CDC42BPA, NDUFV2, PDHB, REXO2, PALS2, PCNT, PGP, PHB1, MOB4, NUP210, UQCRC1, RIF1, MRPL4, MRPL45, MRPL55, MRPS27, RUSF1, SCARB2, SETD7, HM13, TIMM50, TMA16, UBTF, YLPM1

### Function

No GO or KEGG term passed global multiple-testing correction, so the module should not be assigned a formally enriched pathway. Its gene content nevertheless forms a coherent, multi-process cellular maintenance program. The strongest interpretation is coordinated mitochondrial protein synthesis and respiration, coupled to RNA processing, ribosome biogenesis, chromatin regulation, DNA maintenance, and protein quality control. This interpretation is supported by the mitochondrial ribosomal genes MRPL4, MRPL45, MRPL55, and MRPS27; the respiratory-chain genes NDUFV2 and UQCRC1; the pyruvate dehydrogenase component PDHB; and the RNA and ribosome factors IMP4, TMA16, EFL1, UBTF, CRNKL1, and LYAR. The network is therefore better viewed as a cellular biosynthetic and energetic state module than as evidence for a single specialized tissue pathway. The lack of globally significant GO or KEGG enrichment is an important limitation, not evidence that the module is false.

**Cell composition.** The module does not look predominantly like a plasma or secreted-protein module: the HPA summary identifies only a small secreted component, and most proteins are intracellular, with mitochondrial, nuclear, nucleolar, endoplasmic-reticulum, or membrane locations. Most genes have low tissue specificity, while a smaller subset is tissue enhanced or enriched in skeletal muscle, bone marrow, lymphoid tissue, brain, testis, or tongue. HPA detects protein for most module genes in kidney, whereas no matching autonomic-nervous-system tissue assessment is available. Blood-cell specificity is generally low, although several genes show associations with progenitor or myeloid cell states. The frequent HPA signals for erythrocyte progenitors, megakaryocyte progenitors, monocyte progenitors, and related cell states mean that shared cell composition or sample blood content could contribute to the cross-tissue co-abundance pattern. The module should therefore not be interpreted as autonomic-neural or kidney-specific without cell-resolved validation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports several established local relationships. The mitochondrial ribosomal cluster is represented by MRPL4, MRPL45, MRPL55, and MRPS27, with strong links among these proteins. NDUFV2 and UQCRC1 connect respiratory-chain components, and PDHB links to UQCRC1. IMP4 connects with LYAR and TMA16, while DNMT1 connects with SETD7 and HELLS; ASH2L also connects with SETD7. Other supported edges include CANX with PHB1 and CRNKL1 with EFL1. These relationships indicate that parts of the module recapitulate known mitochondrial, ribosome-biogenesis, chromatin, and protein-folding biology rather than being wholly unexplained associations. hu.MAP independently supports repeated mitochondrial large-ribosomal complex membership for MRPL4 and MRPL55 (hu.MAP huMAP3_00983.1), (hu.MAP huMAP3_04652.1), and related complexes (hu.MAP huMAP3_06439.1) through (hu.MAP huMAP3_06589.1). It also supports respiratory-chain complex membership for NDUFV2 and UQCRC1 (hu.MAP huMAP3_14018.1), (hu.MAP huMAP3_09982.1), and DNMT1 with MESD in broader complexes (hu.MAP huMAP3_13998.1), (hu.MAP huMAP3_14982.1). Because each complex contains only a small subset of its listed members in this module, the hu.MAP evidence validates functional neighborhoods but does not establish that the entire module is one physical complex.

**STRING interactions (score >= 0.7)**: 17 of 946 gene pairs: ASH2L–SETD7 (0.792); CANX–PHB1 (0.74); CRNKL1–EFL1 (0.779); DNMT1–HELLS (0.703); DNMT1–SETD7 (0.936); EFL1–MRPL4 (0.803); IMP4–LYAR (0.857); IMP4–TMA16 (0.817); LYAR–TMA16 (0.727); MRPL4–MRPL45 (0.988); MRPL4–MRPL55 (0.959); MRPL4–MRPS27 (0.895); MRPL45–MRPL55 (0.841); MRPL45–MRPS27 (0.927); MRPL55–MRPS27 (0.876); NDUFV2–UQCRC1 (0.996); PDHB–UQCRC1 (0.826)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00983.1 (MRPL55, MRPL4; 2/22); huMAP3_13998.1 (DNMT1, MESD; 2/23); huMAP3_14982.1 (DNMT1, MESD; 2/28); huMAP3_04652.1 (MRPL55, MRPL4; 2/30); huMAP3_14018.1 (NDUFV2, UQCRC1; 2/48); huMAP3_09982.1 (NDUFV2, UQCRC1; 2/49); huMAP3_06439.1 (MRPL55, MRPL4; 2/57); huMAP3_06550.1 (MRPL55, MRPL4; 2/62); huMAP3_07939.1 (MRPL55, MRPL4; 2/68); huMAP3_08458.1 (MRPL55, MRPL4; 2/70); huMAP3_09113.1 (MRPL55, MRPL4; 2/72); huMAP3_09483.1 (MRPL55, MRPL4; 2/74); huMAP3_06589.1 (MRPL55, MRPL4; 2/79)

### Novelty

The module should not be called a completely new biological mechanism. Several of its internal relationships and functional components are already documented by STRING and hu.MAP, especially mitochondrial ribosomes, respiratory-chain proteins, ribosome biogenesis, and chromatin regulation. The potentially novel observation is the reproducible co-abundance of these established cellular programs across autonomic nervous system and kidney samples. That cross-tissue organization may be biologically informative, but the fact sheet alone does not establish independence from cell composition, shared housekeeping demand, or sample quality. Absence of a relationship from STRING or hu.MAP would not prove novelty, and the lack of globally significant GO or KEGG enrichment further argues for cautious language. Replication in independent cohorts, adjustment for cell composition, and comparison with published cross-tissue modules are needed before claiming a new finding.

**Hypothesis.** Hypothesis: this conserved module reflects a shared cellular state in which mitochondrial translation and oxidative metabolism are coordinated with nuclear RNA production, ribosome assembly, chromatin maintenance, and protein quality control. In kidney and autonomic nervous system samples, cells with high energetic and biosynthetic demand may jointly increase these processes, producing the observed co-abundance pattern. A competing explanation is that the module partly reflects broadly expressed housekeeping programs or shared progenitor and blood-related cell content. This hypothesis predicts that module activity should track mitochondrial translation, respiratory capacity, and proliferative or repair states at single-cell or spatial resolution, while its apparent conservation should weaken after careful adjustment for cellular composition.

### Important genes

#### MRPL45

- **Related proteins** (co-abundance neighbors): REXO2 (0.90), PALS2 (0.89), PCNT (0.87), SLC1A5 (0.85), GRSF1 (0.84), MOB4 (0.84), TIMM50 (0.83), HELLS (0.82); STRING partners: MRPL4 (0.988), MRPL55 (0.841), MRPS27 (0.927)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial ribosomal protein L45. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.498); lysosomal storage disease (0.325); Alzheimer disease (0.325); Parkinson disease (0.325); prostate carcinoma (0.198)
- **Europe PMC papers**: 238
- **Why important**: MRPL45 has the strongest network position in the listed module and connects to several module genes, including the mitochondrial ribosomal proteins MRPL4, MRPL55, and MRPS27. HPA places it in mitochondria and detects it in kidney. Its annotation supports mitochondrial translation, while its disease literature includes neurodegenerative and lysosomal disorders. The STRING links and the mitochondrial complexes containing MRPL4 and MRPL55 (hu.MAP huMAP3_00983.1), (hu.MAP huMAP3_04652.1), and related complexes (hu.MAP huMAP3_06439.1) through (hu.MAP huMAP3_06589.1) provide independent support for its role as a mitochondrial translation hub.
- **Conclusion**: Established evidence supports MRPL45 as a central mitochondrial-ribosome component and a strong structural anchor of the module. It is a plausible marker of the module's mitochondrial translation component, but the co-abundance data do not show that MRPL45 causally drives the cross-tissue pattern.

#### PCNT

- **Related proteins** (co-abundance neighbors): ASH2L (0.87), MRPL45 (0.87), IMP4 (0.87), NDUFV2 (0.86), PALS2 (0.84), MRPS27 (0.83), TMA16 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Low immune cell specificity; location Centrosome; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pericentrin. The protein encoded by this gene binds to calmodulin and is expressed in the centrosome. It is an integral component of the pericentriolar material (PCM). The protein contains a series of coiled-coil domains and a highly conserved PCM targeting motif called the PACT domain near its C-terminus. The protein interacts with the microtubule nucleation component gamma-tubulin and is likely important to …
- **Diseases (Open Targets)**: microcephalic osteodysplastic primordial dwarfism type II (0.808); hereditary disease (0.526); Insulin resistance (0.469); microcephalic primordial dwarfism (0.380); microcephalic osteodysplastic primordial dwarfism (0.371)
- **Europe PMC papers**: 1285
- **Why important**: PCNT has a prominent network position and links mitochondrial, nucleolar, and other module neighborhoods. Its established function is pericentrin activity at the centrosome, including microtubule nucleation, cytoskeleton organization, cell-cycle processes, and cilium assembly. HPA reports tissue enrichment in skeletal muscle and detection in kidney. It has substantial literature and disease associations involving microcephalic primordial dwarfism and insulin resistance.
- **Conclusion**: Established evidence supports PCNT as a centrosome and cytoskeleton regulator that may connect cellular architecture to the module's metabolic and biosynthetic state. Its bridging position is suggestive, but a direct mechanistic link between PCNT and the mitochondrial or kidney-autonomic co-abundance pattern remains a hypothesis.

#### SLC1A5

- **Related proteins** (co-abundance neighbors): MRPL55 (0.88), MRPL4 (0.86), MRPL45 (0.85), HM13 (0.85), DNMT1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 1 member 5. The SLC1A5 gene encodes a sodium-dependent neutral amino acid transporter that can act as a receptor for RD114/type D retrovirus (Larriba et al., 2001 [PubMed 11781704]).[supplied by OMIM, Jan 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.463); substance abuse (0.231); attention deficit-hyperactivity disorder (0.231); autoimmune disorder of central nervous system (0.213); hypotensive disorder (0.188)
- **Europe PMC papers**: 5038
- **Why important**: SLC1A5 is a central connector in the module and links the mitochondrial-ribosomal neighborhood with HM13 and DNMT1. It is a plasma-membrane neutral amino-acid transporter with established roles in glutamine, glutamate, and serine transport. HPA shows low tissue specificity, kidney detection, and enhancement in plasmacytoid dendritic cells. Its large literature base and disease associations make it a biologically informative interface between nutrient supply, biosynthesis, and cellular state.
- **Conclusion**: Established evidence supports SLC1A5 as a nutrient-transport component that could supply substrates for mitochondrial and biosynthetic activity. The network suggests coordination with mitochondrial translation and epigenetic maintenance, but it does not establish that SLC1A5 regulates those processes in this module.

#### DNMT1

- **Related proteins** (co-abundance neighbors): SLC1A5 (0.84), SETD7 (0.82); STRING partners: HELLS (0.703), SETD7 (0.936)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13998.1, huMAP3_14982.1
- **Function (MyGene.info)**: DNA methyltransferase 1. This gene encodes an enzyme that transfers methyl groups to cytosine nucleotides of genomic DNA. This protein is the major enzyme responsible for maintaining methylation patterns following DNA replication and shows a preference for hemi-methylated DNA. Methylation of DNA is an important component of mammalian epigenetic gene regulation. Aberrant methylation patterns are found in human tumors and a…
- **Diseases (Open Targets)**: autosomal dominant cerebellar ataxia, deafness and narcolepsy (0.806); hereditary sensory neuropathy-deafness-dementia syndrome (0.777); acute myeloid leukemia (0.623); myelodysplastic syndrome (0.615); cancer (0.612)
- **Europe PMC papers**: 30754
- **Why important**: DNMT1 connects the transporter neighborhood to SETD7 and HELLS, and STRING supports its relationships with both SETD7 and HELLS. Its established function is maintenance DNA methylation and epigenetic regulation. It appears in hu.MAP complexes (hu.MAP huMAP3_13998.1) and (hu.MAP huMAP3_14982.1), although only a small subset of those complexes is represented in the module. DNMT1 has by far the largest literature volume among the selected genes and is associated with hereditary neurological disease, myeloid malignancy, and other disorders.
- **Conclusion**: Established evidence supports DNMT1 as the module's strongest epigenetic-maintenance representative. Its presence is consistent with coupling of metabolic state to chromatin maintenance, but the module does not demonstrate a direction of regulation or disease mechanism.

#### UQCRC1

- **Related proteins** (co-abundance neighbors): MRPL4 (0.81); STRING partners: NDUFV2 (0.996), PDHB (0.826)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_09982.1
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase core protein 1. Enables ubiquitin protein ligase binding activity. Predicted to be involved in oxidative phosphorylation. Predicted to act upstream of or within mitochondrial electron transport, ubiquinol to cytochrome c. Located in mitochondrion. Implicated in Alzheimer's disease. Biomarker of Alzheimer's disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: parkinsonism with polyneuropathy (0.642); neurodegenerative disease (0.569); Parkinson disease (0.521); Alzheimer disease (0.519); lysosomal storage disease (0.498)
- **Europe PMC papers**: 1860
- **Why important**: UQCRC1 represents the respiratory component of the module and connects by STRING to NDUFV2 and PDHB. It is annotated to oxidative phosphorylation and mitochondrial electron transport, is detected in kidney, and is tissue enhanced in energetically active muscle and heart-related tissues. hu.MAP supports its respiratory-chain complex neighborhood with NDUFV2 (hu.MAP huMAP3_14018.1), (hu.MAP huMAP3_09982.1). Its literature includes neurodegenerative disease and Parkinson disease.
- **Conclusion**: Established evidence supports UQCRC1 as a marker of mitochondrial electron transport within the module. Its co-occurrence with mitochondrial ribosomal proteins is compatible with coordinated respiratory capacity, but it does not prove that the module represents altered oxidative phosphorylation rather than general mitochondrial abundance.

## Module 3

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (5)**: GOT1, SERPINC1, APOA1, HBA1, S100A9

### Function

The strongest functional interpretation is a blood-associated extracellular and circulating-protein module, rather than a clearly intrinsic autonomic-nervous-system or kidney cellular program. (GO:CC blood microparticle; q_global = 0.0185) is the only GO/KEGG term passing global correction and identifies blood microparticles, represented by APOA1, HBA1, and SERPINC1. This is supported independently but only supplementally by STRING terms for blood microparticles (STRING Component Blood microparticle; within-query FDR = 0.0136) and (STRING COMPARTMENTS Blood microparticle; within-query FDR = 0.0144), together with endocytic vesicle lumen (STRING Component Endocytic vesicle lumen; within-query FDR = 0.0396). The genes also span lipid transport, coagulation control, oxygen transport, amino-acid and intermediary metabolism, and inflammatory signaling. The network therefore appears heterogeneous: a plasma and erythrocyte-associated core is accompanied by a metabolic connection through GOT1 and an inflammatory myeloid-associated signal through S100A9. Because only one GO/KEGG term passed global correction, the more specific tissue and process interpretations should remain secondary.

**Cell composition.** The module is strongly compatible with blood or plasma influence in the sampled tissues. APOA1, SERPINC1, and S100A9 are secreted to blood, while HBA1 is an erythrocyte-associated hemoglobin gene. HPA points to liver enrichment for APOA1 and SERPINC1, bone-marrow or blood-cell associations for HBA1 and S100A9, and hepatocyte enrichment for APOA1 and SERPINC1. S100A9 is associated with neutrophils and classical monocytes, and HBA1 with erythrocytes. The module is therefore not composed mainly of broadly expressed housekeeping genes; instead, much of it has plasma, erythrocyte, hepatic, or myeloid specificity. The absence of HPA protein detection in kidney for most members, including APOA1, SERPINC1, S100A9, and HBA1, together with detection of GOT1 in kidney, makes blood carryover, vascular content, or shared circulating material plausible explanations for the cross-tissue conservation. This composition argues against assuming that the module represents a resident kidney or autonomic nervous system cell program.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 0.0185 | APOA1, HBA1, SERPINC1 |

### STRING and hu.MAP

STRING provides one high-confidence pair within the module: APOA1 with SERPINC1. This relationship is biologically coherent because both are circulating plasma proteins and both participate in the globally significant blood-microparticle annotation (GO:CC blood microparticle; q_global = 0.0185). The remaining within-module relationships are not supported by STRING at the stated confidence threshold, so the co-abundance edges should not be interpreted as established physical interactions. STRING’s blood-microparticle terms (STRING Component Blood microparticle; within-query FDR = 0.0136) and (STRING COMPARTMENTS Blood microparticle; within-query FDR = 0.0144) reinforce the plasma interpretation, while left-atrial and left-ventricular tissue terms (STRING TISSUES Left atrium; within-query FDR = 0.0139) and (STRING TISSUES Left ventricle; within-query FDR = 0.0187) are supplementary associations rather than globally corrected GO/KEGG evidence. The collagen-containing extracellular-matrix term (STRING Component Collagen-containing extracellular matrix; within-query FDR = 0.0312) links APOA1, SERPINC1, and S100A9 but does not establish a direct complex. hu.MAP identifies complex C1 containing SERPINC1, APOA1, and HBA1 among many additional plasma, complement, coagulation, and transport proteins. Thus, hu.MAP supports their membership in a broad circulating-protein complex context, but the large and heterogeneous complex does not demonstrate that all module genes form one discrete molecular machine. GOT1 and S100A9 have no reported hu.MAP complex with another module member, and GOT1, S100A9, and HBA1 lack reported STRING partners within this module.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: APOA1–SERPINC1 (0.708)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Blood microparticle (FDR = 0.0136, 3 genes); TISSUES Left atrium (FDR = 0.0139, 3 genes); COMPARTMENTS Blood microparticle (FDR = 0.0144, 3 genes); TISSUES Left ventricle (FDR = 0.0187, 3 genes); Component Collagen-containing extracellular matrix (FDR = 0.0312, 3 genes); Component Endocytic vesicle lumen (FDR = 0.0396, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINC1, APOA1, HBA1; 3/64)

### Novelty

The module may be novel as a cross-tissue co-abundance pattern, but the underlying biology is not wholly novel. APOA1 and SERPINC1 have a known STRING relationship, and APOA1, SERPINC1, and HBA1 occur together in hu.MAP complex C1. The blood-microparticle interpretation is also independently represented in the enrichment resources. What may be new is the particular coordinated association of this plasma and erythrocyte signal with GOT1 and S100A9 across autonomic nervous system and kidney samples. However, absence of additional STRING or hu.MAP links cannot establish novelty, and the HPA pattern raises a competing explanation involving shared blood, vascular, hepatic, erythrocyte, or inflammatory-cell content. Accordingly, this should be described as a potentially novel tissue-pair co-abundance configuration, not as discovery of a new protein complex or previously unknown pathway.

**Hypothesis.** Hypothesis: the conserved module reflects a circulating blood-associated state sampled in both tissue groups, combining HDL-associated lipid transport through APOA1, anticoagulant and plasma-protease regulation through SERPINC1, erythrocyte oxygen and redox-related material through HBA1, inflammatory myeloid-derived material through S100A9, and metabolic coupling through GOT1. A plausible mechanism is that vascular or blood-cell content, together with systemic inflammatory or metabolic variation, produces coordinated abundance of these proteins in both tissue datasets. The network bridge involving APOA1 and GOT1, and the connection of GOT1 to S100A9, could represent a metabolic-inflammatory interface, but this is a hypothesis rather than an established physical pathway. Testing would require cell-resolved data, blood-depletion or vascular-content controls, and replication using tissue-resident markers.

### Important genes

#### APOA1

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.93), GOT1 (0.88), HBA1; HBA2 (0.86); STRING partners: SERPINC1 (0.708)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is the highest-connectivity gene in the module and links SERPINC1, GOT1, and HBA1 in the co-abundance graph. It is the major HDL protein, promotes cholesterol efflux, is secreted into blood, and is enriched in liver and hepatocytes. It participates in the primary blood-microparticle term (GO:CC blood microparticle; q_global = 0.0185) and all of the listed STRING supplementary terms (STRING Component Blood microparticle; within-query FDR = 0.0136) through (STRING Component Endocytic vesicle lumen; within-query FDR = 0.0396). Its extensive literature and disease associations with apolipoprotein deficiency and lipid-related disorders make it the clearest anchor for interpreting the module as a circulating lipid and plasma signal.
- **Conclusion**: Established: APOA1 is a plasma HDL component, a module hub, a member of (GO:CC blood microparticle; q_global = 0.0185), and part of the known STRING and hu.MAP context. Conclusion: APOA1 is the most informative representative of the module’s circulating and blood-associated character. Hypothesis: its co-abundance with GOT1 and S100A9 may report systemic metabolic or inflammatory variation rather than a direct molecular interaction.

#### SERPINC1

- **Related proteins** (co-abundance neighbors): APOA1 (0.93), HBA1; HBA2 (0.83); STRING partners: APOA1 (0.708)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 is a secreted liver-enriched plasma protein encoding antithrombin, a regulator of thrombin and other coagulation proteases. It has two module connections, including the only STRING-supported within-module relationship, with APOA1, and it occurs with APOA1 and HBA1 in hu.MAP complex C1. It is part of the globally corrected blood-microparticle term (GO:CC blood microparticle; q_global = 0.0185) and the supplementary STRING terms (STRING Component Blood microparticle; within-query FDR = 0.0136), (STRING COMPARTMENTS Blood microparticle; within-query FDR = 0.0144), and (STRING Component Collagen-containing extracellular matrix; within-query FDR = 0.0312). Its strong disease associations with hereditary antithrombin deficiency and venous thrombosis make it important for distinguishing a vascular or coagulation-related signal from a resident tissue pathway.
- **Conclusion**: Established: SERPINC1 is a liver-derived circulating anticoagulant and has known network and complex support with APOA1 and HBA1. Conclusion: it supports interpretation of the module as plasma and coagulation related. Hypothesis: coordinated SERPINC1 and APOA1 abundance may reflect shared vascular exposure or plasma composition in both tissue groups.

#### HBA1

- **Related proteins** (co-abundance neighbors): none; STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: hemoglobin subunit alpha 1. The human alpha globin gene cluster located on chromosome 16 spans about 30 kb and includes seven loci: 5'- zeta - pseudozeta - mu - pseudoalpha-1 - alpha-2 - alpha-1 - theta - 3'. The alpha-2 (HBA2) and alpha-1 (HBA1) coding sequences are identical. These genes differ slightly over the 5' untranslated regions and the introns, but they differ significantly over the 3' untranslated regions. Two alp…
- **Diseases (Open Targets)**: alpha thalassemia spectrum (0.758); hemoglobin H disease (0.755); hemoglobin M disease (0.735); Heinz body anemia (0.698); primary familial polycythemia due to EPO receptor mutation (0.689)
- **Europe PMC papers**: 4551
- **Why important**: HBA1 is an erythrocyte-associated hemoglobin gene and is part of the only globally corrected term, blood microparticle (GO:CC blood microparticle; q_global = 0.0185). It is associated by HPA with erythrocytes and bone marrow or lymphoid tissues, and it appears with APOA1 and SERPINC1 in hu.MAP complex C1. Although it has no reported STRING partner in this module and has no network edge in the supplied graph, its presence is biologically informative because it points to erythrocyte or blood-derived material rather than a conventional intracellular tissue complex. Its disease associations with alpha-thalassemia and other hemoglobin disorders provide established clinical context.
- **Conclusion**: Established: HBA1 is an erythrocyte hemoglobin component and contributes to (GO:CC blood microparticle; q_global = 0.0185) and C1. Conclusion: HBA1 is more useful as a provenance marker for blood or erythrocyte material than as a mechanistic hub. Hypothesis: its co-occurrence may indicate vascular contamination, blood retention, or blood-microparticle abundance in the tissue samples.

#### S100A9

- **Related proteins** (co-abundance neighbors): GOT1 (0.91); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Group enriched; location Plasma membrane, Intermediate filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: S100 calcium binding protein A9. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: inborn error of immunity (0.370); Sepsis (0.121); neoplasm (0.119); psoriasis (0.114); cancer (0.114)
- **Europe PMC papers**: 16393
- **Why important**: S100A9 is the module’s inflammatory and myeloid-associated component. HPA links it to bone marrow and to classical monocytes and neutrophils, while the protein is secreted to blood. It is connected to GOT1 in the module and contributes to the supplementary collagen-containing extracellular-matrix term (STRING Component Collagen-containing extracellular matrix; within-query FDR = 0.0312). Its established biology includes inflammatory response, leukocyte migration, chronic inflammation, autophagy, and cell-cell signaling, with disease associations including inborn errors of immunity, sepsis, psoriasis, and cancer. Its substantial literature makes it a strong indicator that the module may include an inflammatory-cell or systemic inflammatory contribution.
- **Conclusion**: Established: S100A9 is a blood-associated inflammatory protein with myeloid enrichment and a module connection to GOT1. Conclusion: it supports an inflammatory or myeloid-content interpretation but is not part of the globally corrected GO/KEGG term. Hypothesis: S100A9 may couple systemic inflammation to the metabolic signal represented by GOT1.

#### GOT1

- **Related proteins** (co-abundance neighbors): S100A9 (0.91), APOA1 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamic-oxaloacetic transaminase 1. Glutamic-oxaloacetic transaminase is a pyridoxal phosphate-dependent enzyme which exists in cytoplasmic and mitochondrial forms, GOT1 and GOT2, respectively.  GOT plays a role in amino acid metabolism and the urea and tricarboxylic acid cycles. The two enzymes are homodimeric and show close homology. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); Parkinson disease (0.375); Alzheimer disease (0.367); lysosomal storage disease (0.356); obesity disorder (0.172)
- **Europe PMC papers**: 3793
- **Why important**: GOT1 is the principal non-secreted metabolic member and is detected by HPA in kidney, unlike most of the other module proteins. It is tissue enhanced in heart muscle, skeletal muscle, and tongue, and its known function includes amino-acid, aspartate, oxaloacetate, gluconeogenic, and tricarboxylic-acid-related metabolism. Within the module it connects APOA1 with S100A9, giving it a potentially important bridging position between the plasma lipid signal and the inflammatory signal. It has no reported STRING or hu.MAP relationship with another module member and does not occur in a globally corrected GO/KEGG term, so its interpretation must rely on network position, kidney detection, and established metabolic biology.
- **Conclusion**: Established: GOT1 is a metabolic enzyme with kidney protein detection and two co-abundance connections, but no reported STRING or hu.MAP support within this module. Conclusion: GOT1 is the best candidate for a tissue-associated metabolic component within an otherwise blood-heavy module. Hypothesis: it may mark a genuine metabolic response shared across the tissues or may reflect coordinated metabolic state alongside blood-derived proteins; the current evidence cannot distinguish these possibilities.

## Module 4

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (47)**: AATF, ABCF1, ARMC8, ASNS, ATXN2L, CDK6, C5orf22, CIP2A, DCAF13, DDX20, DHX16, SIRAL1, GNPNAT1, GSK3B, HPRT1, HK2, IGF2BP3, EIF4G1, IMPDH1, LLPH, LEMD3, MCM2, MCM4, MCM5, MYO9B, NAA25, DR1, NRDC, NVL, OGFOD1, ORC2, ORC4, PSME3IP1, RBBP7, RRS1, SF3A1, SMC2, SMN1, SMARCAD1, SRPK2, STMN1, GTF2E1, TAF6L, DNTTIP2, UBQLN2, UTP25, WDHD1

### Function

The strongest supported function is nuclear chromosome organization linked to DNA replication initiation. The primary evidence is (GO:CC nuclear chromosome; q_global = 0.00522), which places MCM2, MCM4, MCM5, ORC2, ORC4, RBBP7, RRS1, SMARCAD1, SMC2 and WDHD1 in the nuclear chromosome compartment, and (GO:BP DNA replication initiation; q_global = 0.0468), which specifically supports DNA replication initiation through MCM2, MCM4, MCM5, ORC2 and ORC4. The module therefore most plausibly represents a replication-licensing and chromatin-maintenance program, with additional nucleolar, transcriptional and RNA-processing components. The supplementary STRING results support this interpretation through the pre-replicative and GINS-complex neighborhood (STRING NetworkNeighborAL Activation of the pre-replicative complex, and GINS complex; within-query FDR = 0.0034), nuclear-chromosome terms (STRING COMPARTMENTS Nuclear chromosome; within-query FDR = 0.0036) (STRING Component Nuclear chromosome; within-query FDR = 0.0038), and cell-cycle annotations (STRING KEGG Cell cycle; within-query FDR = 0.0096) (STRING WikiPathways Cell cycle; within-query FDR = 0.0142) (STRING WikiPathways G1 to S cell cycle control; within-query FDR = 0.0142). These supplementary terms should not be treated as globally corrected enrichment.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity and low immune-cell specificity, arguing against a module composed predominantly of blood-cell markers or tissue-restricted proteins. Nevertheless, HPA shows recurring enrichment in lymphoid tissue, bone marrow and hematopoietic progenitor populations, as well as germ-cell and spermatogenic populations. This pattern is compatible with a proliferative or progenitor-cell component and raises the possibility that shared cell composition contributes to the autonomic-nervous-system and kidney co-abundance signal. Kidney protein detection is widespread among the measured genes, whereas matching HPA tissue data are unavailable for autonomic nervous system, so the tissue-pair interpretation should not be taken as evidence of a specialized autonomic-neural protein program.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC nuclear chromosome | 0.00522 | MCM2, MCM4, MCM5, ORC2, ORC4, RBBP7, RRS1, SMARCAD1, SMC2, WDHD1 |
| GO:BP DNA replication initiation | 0.0468 | MCM2, MCM4, MCM5, ORC2, ORC4 |

### STRING and hu.MAP

STRING contains established, high-confidence relationships among the replication-licensing genes: MCM2, MCM4 and MCM5 connect strongly with one another and with ORC2, ORC4 and WDHD1; MCM4 and MCM5 also connect with SMC2. This gives the module a biologically coherent core rather than an association based only on correlated abundance. Other known relationships include DDX20 with SMN1, DHX16 with SF3A1, AATF with DCAF13 and DNTTIP2, and GNPNAT1 with HK2. hu.MAP independently identifies recurring complexes containing MCM2, MCM4 and MCM5, including assemblies related to the MCM helicase, replication-fork progression and GINS-associated machinery (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1). It also identifies spliceosomal or snRNP-related complexes containing SF3A1, SMN1 and DDX20 (hu.MAP huMAP3_04549.1) (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_08980.1), and transcription-related complexes containing DR1 and TAF6L (hu.MAP huMAP3_09561.1) (hu.MAP huMAP3_08451.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_12550.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_10385.1). Thus, part of the module recapitulates known physical complexes, while the remaining co-abundance links may reflect shared cell-cycle state, nuclear biosynthetic demand, or coordinated expression rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 29 of 1081 gene pairs: AATF–DCAF13 (0.998); AATF–DNTTIP2 (0.997); AATF–UTP25 (0.724); CDK6–MCM2 (0.796); DCAF13–DNTTIP2 (0.992); DCAF13–RRS1 (0.79); DCAF13–UTP25 (0.897); DDX20–SMN1 (0.998); DHX16–SF3A1 (0.998); DNTTIP2–RRS1 (0.84); DR1–TAF6L (0.72); GNPNAT1–HK2 (0.93); HPRT1–IMPDH1 (0.955); MCM2–MCM4 (0.999); MCM2–MCM5 (0.999); MCM2–ORC2 (0.999); MCM2–ORC4 (0.997); MCM2–WDHD1 (0.998); MCM4–MCM5 (0.999); MCM4–ORC2 (0.988); MCM4–ORC4 (0.995); MCM4–SMC2 (0.748); MCM4–WDHD1 (0.999); MCM5–ORC2 (0.999); MCM5–ORC4 (0.976); MCM5–SMC2 (0.754); MCM5–WDHD1 (0.999); ORC2–ORC4 (0.999); SMC2–WDHD1 (0.719)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Nuclear lumen (FDR = 7.8e-05, 27 genes); Keyword Nucleus (FDR = 0.00084, 35 genes); COMPARTMENTS Nucleoplasm (FDR = 0.0033, 18 genes); NetworkNeighborAL Activation of the pre-replicative complex, and GINS complex (FDR = 0.0034, 6 genes); COMPARTMENTS Nuclear chromosome (FDR = 0.0036, 10 genes); Component Nuclear chromosome (FDR = 0.0038, 10 genes); KEGG Cell cycle (FDR = 0.0096, 7 genes); COMPARTMENTS Intracellular organelle lumen (FDR = 0.0135, 29 genes); WikiPathways Cell cycle (FDR = 0.0142, 7 genes); WikiPathways G1 to S cell cycle control (FDR = 0.0142, 6 genes); COMPARTMENTS DNA replication preinitiation complex (FDR = 0.0188, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05529.1 (MCM4, MCM5, MCM2; 3/6); huMAP3_14758.1 (MCM4, MCM5, MCM2; 3/14); huMAP3_08554.1 (MCM4, MCM5, MCM2; 3/15); huMAP3_11832.1 (MCM4, MCM5, MCM2; 3/15); huMAP3_12180.1 (MCM4, MCM5, MCM2; 3/17); huMAP3_04549.1 (SF3A1, SMN1, DDX20; 3/52); huMAP3_06511.1 (SF3A1, SMN1, DDX20; 3/79); huMAP3_08980.1 (SF3A1, SMN1, DDX20; 3/97); huMAP3_09860.1 (MCM4, MCM2; 2/4); huMAP3_00154.1 (MCM4, MCM2; 2/5); huMAP3_06061.1 (MCM4, MCM2; 2/5); huMAP3_07113.1 (MCM4, MCM2; 2/6); huMAP3_11119.1 (MCM4, MCM5; 2/14); huMAP3_09561.1 (DR1, TAF6L; 2/15); huMAP3_08451.1 (DR1, TAF6L; 2/17); huMAP3_09466.1 (MCM4, MCM2; 2/23); huMAP3_12550.1 (DR1, TAF6L; 2/32); huMAP3_10862.1 (MCM4, MCM2; 2/33); huMAP3_10385.1 (DR1, TAF6L; 2/40); huMAP3_14306.1 (MCM4, MCM2; 2/55); huMAP3_05807.1 (SRPK2, DNTTIP2; 2/81)

### Novelty

The module is unlikely to represent a newly discovered replication complex: the MCM and ORC relationships are already well established in STRING and hu.MAP, and the globally corrected annotations agree with canonical replication biology. Its potentially novel aspect is the coordinated co-abundance of this replication-centered core with nucleolar, RNA-processing, metabolic and chromatin-associated genes across autonomic nervous system and kidney samples. However, the supplied evidence does not establish that this cross-tissue co-abundance pattern is new. Absence of a relationship from STRING or hu.MAP cannot demonstrate novelty, because those resources emphasize experimentally supported interactions and curated complexes rather than every tissue-specific co-abundance relationship. A novelty claim would require comparison with prior tissue co-expression modules, independent cohorts, cell-composition adjustment and replication in external datasets.

**Hypothesis.** Hypothesis: the shared module reflects a conserved nuclear growth or progenitor-state program present in both tissue groups. In this model, ORC2 and ORC4 help establish replication origins, while the MCM2-MCM4-MCM5 core represents replication-licensing machinery. WDHD1, SMC2, SMARCAD1 and RBBP7 could couple replication with chromatin organization and chromosome handling, while NVL, AATF, DCAF13, RRS1 and UTP25 support the nucleolar and biosynthetic demands of cells entering or maintaining a proliferative state. The RNA-splicing and translation-related genes may reflect the broader transcriptional and post-transcriptional workload of that state. The HPA enrichment in progenitor and germ-cell populations makes a cell-state or cell-composition explanation plausible, but this remains a hypothesis rather than a demonstrated mechanism.

### Important genes

#### MCM2

- **Related proteins** (co-abundance neighbors): DCAF13 (0.86), MCM5 (0.84), SMN1; SMN2 (0.83); STRING partners: CDK6 (0.796), MCM4 (0.999), MCM5 (0.999), ORC2 (0.999), ORC4 (0.997), WDHD1 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a member of the replication-licensing core, appears in both primary terms (GO:CC nuclear chromosome; q_global = 0.00522) (GO:BP DNA replication initiation; q_global = 0.0468), and connects in STRING with MCM4, MCM5, ORC2, ORC4, WDHD1 and CDK6. It is present in numerous hu.MAP replication-related complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1). Its disease annotations include hearing-loss and developmental associations, and it has a substantial literature base, making it both mechanistically central and clinically interpretable.
- **Conclusion**: Established evidence supports MCM2 as a replication-initiation component and a key anchor of the module. The module-level association suggests coordinated replication-related activity, but it does not establish altered MCM2 activity or a causal role in either tissue.

#### MCM4

- **Related proteins** (co-abundance neighbors): SIRAL1 (0.88), SMC2 (0.85), OGFOD1 (0.83); STRING partners: MCM2 (0.999), MCM5 (0.999), ORC2 (0.988), ORC4 (0.995), SMC2 (0.748), WDHD1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 4. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication rel…
- **Diseases (Open Targets)**: primary immunodeficiency with natural-killer cell deficiency and adrenal insufficiency (0.714); X-linked adrenal hypoplasia congenita (0.185); lung adenocarcinoma (0.112); microcephaly (0.111); neoplasm (0.102)
- **Europe PMC papers**: 4082
- **Why important**: MCM4 is included in both globally corrected terms (GO:CC nuclear chromosome; q_global = 0.00522) (GO:BP DNA replication initiation; q_global = 0.0468), has strong STRING connections to MCM2, MCM5, ORC2, ORC4 and WDHD1, and recurs across many hu.MAP assemblies (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1). Its established role in the MCM helicase and replication-fork biology gives the module a direct mechanistic link to DNA replication. Its disease associations include primary immunodeficiency, adrenal hypoplasia and developmental phenotypes, with extensive literature support.
- **Conclusion**: Established evidence identifies MCM4 as a core replication factor and one of the most reliable functional representatives of this module. It is reasonable to infer replication licensing or replication-associated cell state, but not to infer a tissue-specific MCM4 defect from co-abundance alone.

#### MCM5

- **Related proteins** (co-abundance neighbors): NVL (0.91), SRPK2 (0.90), DCAF13 (0.87), MCM2 (0.84), IMPDH1 (0.83); STRING partners: MCM2 (0.999), MCM4 (0.999), ORC2 (0.999), ORC4 (0.976), SMC2 (0.754), WDHD1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_11119.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 5. The protein encoded by this gene is structurally very similar to the CDC46 protein from S. cerevisiae, a protein involved in the initiation of DNA replication. The encoded protein is a member of the MCM family of chromatin-binding proteins and can interact with at least two other members of this family. The encoded protein is upregulated in the transition from the G0 to G1/S phase of the cell cycl…
- **Diseases (Open Targets)**: Meier-Gorlin syndrome (0.563); neurodegenerative disease (0.397); lysosomal storage disease (0.362); kidney transplant (0.198); diabetic ketoacidosis (0.129)
- **Europe PMC papers**: 4143
- **Why important**: MCM5 is among the most connected members of the established replication core and is present in both primary terms (GO:CC nuclear chromosome; q_global = 0.00522) (GO:BP DNA replication initiation; q_global = 0.0468). STRING links it strongly to MCM2, MCM4, ORC2, ORC4, WDHD1 and SMC2, while hu.MAP repeatedly places it with MCM2 and MCM4 in replication complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_11119.1). Its HPA pattern includes bone marrow and hematopoietic progenitor enhancement, which is relevant to the possibility of a proliferative-cell contribution. It has extensive literature and disease links including Meier-Gorlin syndrome.
- **Conclusion**: Established evidence supports MCM5 as a central replication-licensing marker and a plausible indicator of proliferative cell content. The progenitor-associated HPA pattern supports, but does not prove, a cell-composition explanation for the shared module.

#### ORC2

- **Related proteins** (co-abundance neighbors): SMARCAD1 (0.87); STRING partners: MCM2 (0.999), MCM4 (0.988), MCM5 (0.999), ORC4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: origin recognition complex subunit 2. The origin recognition complex (ORC) is a highly conserved six subunits protein complex essential for the initiation of the DNA replication in eukaryotic cells. Studies in yeast demonstrated that ORC binds specifically to origins of replication and serves as a platform for the assembly of additional initiation factors such as Cdc6 and Mcm proteins. The protein encoded by this gene is a subunit of …
- **Diseases (Open Targets)**: neurodegenerative disease (0.183); tooth disorder (0.124); cholelithiasis (0.102); basal cell carcinoma (0.054); skin disorder (0.045)
- **Europe PMC papers**: 1776
- **Why important**: ORC2 is present in both primary terms (GO:CC nuclear chromosome; q_global = 0.00522) (GO:BP DNA replication initiation; q_global = 0.0468) and connects strongly to MCM2, MCM4, MCM5 and ORC4 in STRING. It represents the origin-recognition side of the replication-initiation machinery, complementing the MCM helicase components. Its hu.MAP coverage is less direct than that of the MCM genes, but its canonical function, disease annotations and substantial literature make it an important mechanistic marker.
- **Conclusion**: Established evidence supports ORC2 as an origin-recognition component that reinforces the replication-initiation interpretation. Its presence does not show that replication is actively occurring; it may instead reflect replication licensing or the abundance of proliferative cells.

#### NVL

- **Related proteins** (co-abundance neighbors): DNTTIP2 (0.92), MCM5 (0.91), ASNS (0.89), IGF2BP3 (0.88), DCAF13 (0.88), ATXN2L (0.84), AATF (0.84), UBQLN2 (0.84), IMPDH1 (0.84), RRS1 (0.82), DDX20 (0.82), PSME3IP1 (0.80), HK2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nuclear VCP like. This gene encodes a member of the AAA (ATPases associated with diverse cellular activities) superfamily. Multiple transcript variants encoding different isoforms have been found for this gene. Two encoded proteins, described as major and minor isoforms, have been localized to distinct regions of the nucleus. The largest encoded protein (major isoform) has been localized to the nucleolus and shown …
- **Diseases (Open Targets)**: neurodegenerative disease (0.459); Parkinson disease (0.370); lysosomal storage disease (0.370); Alzheimer disease (0.370); glioblastoma (0.263)
- **Europe PMC papers**: 717
- **Why important**: NVL is the strongest network hub described in the module and links the replication-associated genes with nucleolar, RNA-processing, metabolic and stress-related members. HPA places it in the nucleoli and reports kidney detection, while the supplied annotation supports roles in ribosome biogenesis and nucleolar organization. It has no listed STRING partner or hu.MAP complex in this module, which makes it useful as a candidate bridge between the well-established replication core and the broader co-abundance program. It also has substantial literature and disease associations involving neurodegenerative disorders.
- **Conclusion**: Established evidence supports NVL as a nucleolar AAA ATPase involved in ribosome biogenesis and as a prominent co-abundance hub. The hypothesis that NVL coordinates nucleolar biosynthetic demand with replication-state genes is plausible from the network, but direct molecular coupling is not established here.

## Module 5

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (41)**: ABHD10, GLA, ATAD3A, ATRX, CPSF7, CWC22, DIAPH2, LIG3, POLA1, TUFM, AGL, GTPBP10, KIF11, KIF23, LARP7, LMNB1, LRRC40, MDN1, MORC3, NELFE, EMG1, NUP98, OSBPL11, CAD, UPF3B, RFC3, MRPL48, ELAC2, POLR1A, POLR2A, MRPS18B, MRPS33, SRCAP, SUPV3L1, XAB2, GTF3C5, TFAM, TRIM24, TOP2A, TRRAP, ZNF326

### Function

The strongest interpretation is a conserved intracellular gene-expression and organelle-maintenance module. The globally corrected cellular-component terms place almost the entire module in membrane-enclosed, organelle, and intracellular organelle lumina (GO:CC membrane-enclosed lumen; q_global = 6.55e-05)(GO:CC organelle lumen; q_global = 6.55e-05)(GO:CC intracellular organelle lumen; q_global = 6.55e-05). More informative biological-process evidence points to mitochondrial gene expression (GO:BP mitochondrial gene expression; q_global = 0.00222) and mitochondrial nucleoid organization (GO:CC nucleoid; q_global = 0.0356)(GO:CC mitochondrial nucleoid; q_global = 0.0356), with a complementary DNA-binding signal (GO:MF DNA binding; q_global = 0.035). The gene set combines mitochondrial RNA processing, mitochondrial translation, mitochondrial DNA maintenance, nuclear transcription, RNA splicing and surveillance, chromatin regulation, DNA replication and repair, and ribosome biogenesis. Thus, the module is better viewed as coordinated nucleocytoplasmic and mitochondrial information processing than as a narrowly tissue-specific pathway. The cellular-component terms are broad, so the mitochondrial gene-expression and nucleoid terms provide the more specific functional interpretation.

**Cell composition.** This does not resemble a plasma-protein or broadly secreted-protein module: the HPA summary identifies only one secreted gene, and most proteins are intracellular. Most genes have low tissue specificity, consistent with broadly expressed cellular machinery rather than a specialized autonomic-nervous-system or kidney marker. There are nevertheless signals compatible with shared cellular composition or proliferative state. HPA tissue enrichment is frequent in lymphoid tissue and bone marrow, while single-cell enrichment is frequent in erythrocyte progenitors, neutrophils, neutrophil progenitors, late spermatids, and choroid-plexus epithelial cells. Overall blood-cell specificity is low, so the module is not convincingly a blood-cell module, but the progenitor and lymphoid annotations warrant checking for sample composition, cell-cycle activity, and technical covariates. Kidney protein detection is common among the assessed genes, whereas autonomic-nervous-system protein evidence is unavailable in the HPA comparison, so the apparent sharing should not be interpreted as tissue-specific protein localization.

**GO/KEGG enrichment**: 7 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC membrane-enclosed lumen | 6.55e-05 | ABHD10, AGL, ATAD3A, ATRX, CAD, CPSF7, CWC22, DIAPH2, ELAC2, EMG1, GLA, GTF3C5, GTPBP10, KIF23, LARP7, LIG3, LMNB1, MDN1, MORC3, MRPL48, MRPS18B, MRPS33, NELFE, NUP98, OSBPL11, POLA1, POLR1A, POLR2A, RFC3, SRCAP, SUPV3L1, TFAM, TOP2A, TRIM24, TRRAP, TUFM, UPF3B, XAB2, ZNF326 |
| GO:CC organelle lumen | 6.55e-05 | ABHD10, AGL, ATAD3A, ATRX, CAD, CPSF7, CWC22, DIAPH2, ELAC2, EMG1, GLA, GTF3C5, GTPBP10, KIF23, LARP7, LIG3, LMNB1, MDN1, MORC3, MRPL48, MRPS18B, MRPS33, NELFE, NUP98, OSBPL11, POLA1, POLR1A, POLR2A, RFC3, SRCAP, SUPV3L1, TFAM, TOP2A, TRIM24, TRRAP, TUFM, UPF3B, XAB2, ZNF326 |
| GO:CC intracellular organelle lumen | 6.55e-05 | ABHD10, AGL, ATAD3A, ATRX, CAD, CPSF7, CWC22, DIAPH2, ELAC2, EMG1, GLA, GTF3C5, GTPBP10, KIF23, LARP7, LIG3, LMNB1, MDN1, MORC3, MRPL48, MRPS18B, MRPS33, NELFE, NUP98, OSBPL11, POLA1, POLR1A, POLR2A, RFC3, SRCAP, SUPV3L1, TFAM, TOP2A, TRIM24, TRRAP, TUFM, UPF3B, XAB2, ZNF326 |
| GO:BP mitochondrial gene expression | 0.00222 | ELAC2, MRPL48, MRPS18B, MRPS33, POLR1A, POLR2A, SUPV3L1, TFAM, TUFM |
| GO:MF DNA binding | 0.035 | ATRX, GTF3C5, LIG3, LMNB1, MORC3, POLA1, POLR1A, POLR2A, RFC3, SRCAP, SUPV3L1, TFAM, TOP2A, TRIM24, ZNF326 |
| GO:CC nucleoid | 0.0356 | ATAD3A, ELAC2, SUPV3L1, TFAM, TUFM |
| GO:CC mitochondrial nucleoid | 0.0356 | ATAD3A, ELAC2, SUPV3L1, TFAM, TUFM |

### STRING and hu.MAP

STRING supports several coherent established relationships rather than a single complete physical complex. The mitochondrial branch includes ELAC2 with SUPV3L1, and a mitoribosomal cluster involving MRPL48, MRPS18B, MRPS33, and TUFM (STRING Component Mitochondrial nucleoid; within-query FDR = 0.0179)(STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.0335). The nuclear RNA-processing branch includes CWC22 with UPF3B and XAB2, and POLR2A with NELFE and XAB2. Replication and chromosome-segregation relationships include POLA1 with RFC3, RFC3 with TOP2A, and the KIF11, KIF23, and TOP2A connections. The chromatin-regulatory pair SRCAP and TRRAP is also supported. hu.MAP provides partial support for complexes containing LMNB1 and ATAD3A, SRCAP and TRRAP, POLR1A and POLR2A, LARP7 and MRPS18B, and SUPV3L1 and MRPL48 (hu.MAP huMAP3_10473.1)(hu.MAP huMAP3_09291.1)(hu.MAP huMAP3_08487.1)(hu.MAP huMAP3_06426.1)(hu.MAP huMAP3_10481.1)(hu.MAP huMAP3_14306.1)(hu.MAP huMAP3_14318.1)(hu.MAP huMAP3_11092.1)(hu.MAP huMAP3_05807.1)(hu.MAP huMAP3_06589.1). However, each hu.MAP overlap is only a subset of a much larger complex, and many co-abundance edges lack a corresponding STRING or hu.MAP relationship. The network therefore appears to combine several known molecular subsystems that are coordinated in abundance, not to represent one experimentally established multiprotein complex.

**STRING interactions (score >= 0.7)**: 21 of 820 gene pairs: CWC22–UPF3B (0.906); CWC22–XAB2 (0.999); ELAC2–SUPV3L1 (0.864); KIF11–KIF23 (0.994); KIF11–TOP2A (0.975); KIF23–LIG3 (0.747); KIF23–TOP2A (0.927); LIG3–POLR2A (0.752); MORC3–TRIM24 (0.719); MRPL48–MRPS18B (0.933); MRPL48–MRPS33 (0.938); MRPL48–TUFM (0.913); MRPS18B–MRPS33 (0.998); MRPS18B–TUFM (0.917); MRPS33–TUFM (0.913); NELFE–POLR2A (0.955); POLA1–RFC3 (0.851); POLR1A–TUFM (0.808); POLR2A–XAB2 (0.761); RFC3–TOP2A (0.757); SRCAP–TRRAP (0.93)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Intracellular organelle lumen (FDR = 6.68e-06, 39 genes); COMPARTMENTS Intracellular organelle lumen (FDR = 0.0079, 28 genes); Component Nuclear lumen (FDR = 0.0179, 30 genes); Component Mitochondrial nucleoid (FDR = 0.0179, 5 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 0.0335, 12 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10473.1 (LMNB1, ATAD3A; 2/24); huMAP3_09291.1 (SRCAP, TRRAP; 2/27); huMAP3_08487.1 (POLR1A, POLR2A; 2/37); huMAP3_06426.1 (POLR1A, POLR2A; 2/38); huMAP3_10481.1 (SRCAP, TRRAP; 2/40); huMAP3_14306.1 (SRCAP, TRRAP; 2/55); huMAP3_14318.1 (POLR1A, POLR2A; 2/58); huMAP3_11092.1 (POLR1A, POLR2A; 2/65); huMAP3_05807.1 (LARP7, MRPS18B; 2/81); huMAP3_06589.1 (SUPV3L1, MRPL48; 2/79)

### Novelty

The module may be a new cross-tissue co-abundance observation, but the fact sheet does not establish that it is a new biological mechanism. Its component processes and several gene relationships are already well established by STRING, hu.MAP, gene annotations, and disease literature. The potentially novel aspect is the coordinated association of mitochondrial gene-expression machinery with nuclear transcription, RNA surveillance, chromatin, and DNA-maintenance genes across autonomic nervous system and kidney samples. That interpretation remains provisional because broad housekeeping expression, progenitor-associated signals, and possible sample-composition effects could produce such sharing. Absence of a STRING or hu.MAP relationship for many edges is not evidence of novelty. Independent replication, adjustment for cell composition and proliferation, and perturbational or protein-level validation would be needed before claiming a new mechanism.

**Hypothesis.** Hypothesis: the shared module reflects a coordinated cellular stress or biosynthetic state in which mitochondrial genome expression and translation are coupled to nuclear transcription, RNA quality control, chromatin regulation, and DNA maintenance. TFAM, ELAC2, SUPV3L1, MRPL48, MRPS18B, MRPS33, and TUFM could represent a mitochondrial information-processing arm, while POLR2A, POLR1A, UPF3B, CWC22, XAB2, SRCAP, TRRAP, and LMNB1 could represent the nuclear transcription and RNA-processing arm. The co-abundance pattern may therefore arise when cells coordinate mitochondrial output with nuclear gene expression and genome maintenance, potentially during altered metabolic demand, differentiation, or proliferation. This is a mechanistic hypothesis rather than a demonstrated causal pathway; the current evidence does not show that any selected gene regulates the abundance of the others.

### Important genes

#### POLR2A

- **Related proteins** (co-abundance neighbors): POLR1A (0.92), UPF3B (0.89), POLA1 (0.84), ATAD3A (0.84), TRIM24 (0.84), NUP98 (0.83), ATRX (0.81); STRING partners: LIG3 (0.752), NELFE (0.955), XAB2 (0.761)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08487.1, huMAP3_06426.1, huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase II subunit A. This gene encodes the largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene contains a carboxy terminal domain composed of heptapeptide repeats that are essential for polymerase activity. These repeats contain serine and threonine residues that are phosphorylated in actively transcribing RNA polymerase. In addition, …
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and variable intellectual and behavioral abnormalities (0.738); HIV infectious disease (0.600); hereditary disease (0.479); syndromic intellectual disability (0.462); Orthomyxoviridae infectious disease (0.374)
- **Europe PMC papers**: 4546
- **Why important**: POLR2A is a high-connectivity hub linking POLR1A, UPF3B, POLA1, ATAD3A, TRIM24, NUP98, and ATRX. It is the catalytic subunit of RNA polymerase II and appears in the globally corrected organelle-lumen, mitochondrial-gene-expression, and DNA-binding terms (GO:CC membrane-enclosed lumen; q_global = 6.55e-05)(GO:CC organelle lumen; q_global = 6.55e-05)(GO:CC intracellular organelle lumen; q_global = 6.55e-05)(GO:BP mitochondrial gene expression; q_global = 0.00222)(GO:MF DNA binding; q_global = 0.035). STRING supports relationships with NELFE, XAB2, and LIG3, while hu.MAP places it with POLR1A in polymerase-related complexes. It has extensive literature and disease evidence involving neurodevelopmental and hereditary disorders.
- **Conclusion**: Established evidence supports POLR2A as a central transcriptional integrator and a plausible structural anchor of the module. The hypothesis that its abundance couples nuclear transcription to mitochondrial or tissue-specific stress is reasonable but not established by this co-abundance network.

#### TFAM

- **Related proteins** (co-abundance neighbors): MRPL48 (0.86), OSBPL11 (0.85), AGL (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transcription factor A, mitochondrial. This gene encodes a key mitochondrial transcription factor containing two high mobility group motifs. The encoded protein also functions in mitochondrial DNA replication and repair. Sequence polymorphisms in this gene are associated with Alzheimer's and Parkinson's diseases. There are pseudogenes for this gene on chromosomes 6, 7, and 11. Alternative splicing results in multiple transcript variant…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome 15 (hepatocerebral type) (0.689); neurodegenerative disease (0.550); stroke disorder (0.191); alcohol drinking (0.189); musculoskeletal system disorder (0.132)
- **Europe PMC papers**: 14423
- **Why important**: TFAM is directly represented in every globally corrected mitochondrial and mitochondrial-nucleoid term (GO:BP mitochondrial gene expression; q_global = 0.00222)(GO:CC nucleoid; q_global = 0.0356)(GO:CC mitochondrial nucleoid; q_global = 0.0356). It is a mitochondrial transcription factor involved in mitochondrial DNA replication and repair, and it connects in the module to MRPL48, OSBPL11, and AGL. Its disease associations include mitochondrial DNA depletion and neurodegenerative disease, and it has a substantial literature.
- **Conclusion**: Established evidence makes TFAM a strong marker of the mitochondrial genome-maintenance arm. It is plausible that TFAM helps couple mitochondrial transcription to cellular metabolic state, but the module does not demonstrate that TFAM drives the co-abundance pattern.

#### ELAC2

- **Related proteins** (co-abundance neighbors): ZNF326 (0.85); STRING partners: SUPV3L1 (0.864)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: elaC ribonuclease Z 2. The protein encoded by this gene has a C-terminal domain with tRNA 3' processing endoribonuclease activity, which catalyzes the removal of the 3' trailer from precursor tRNAs. The protein also interacts with activated Smad family member 2 (Smad2) and its nuclear partner forkhead box H1 (also known as FAST-1), and reduced expression can suppress transforming growth factor-beta induced growth arrest…
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 17 (0.812); prostate cancer, hereditary, 2 (0.732); hereditary disease (0.496); Intellectual disability (0.426); mitochondrial disease (0.372)
- **Europe PMC papers**: 926
- **Why important**: ELAC2 is present in the organelle-lumen, mitochondrial-gene-expression, and mitochondrial-nucleoid terms (GO:CC membrane-enclosed lumen; q_global = 6.55e-05)(GO:CC organelle lumen; q_global = 6.55e-05)(GO:CC intracellular organelle lumen; q_global = 6.55e-05)(GO:BP mitochondrial gene expression; q_global = 0.00222)(GO:CC nucleoid; q_global = 0.0356)(GO:CC mitochondrial nucleoid; q_global = 0.0356). Its annotated function in mitochondrial tRNA processing and its STRING relationship with SUPV3L1 connect RNA maturation to the mitochondrial RNA-processing branch (STRING Component Mitochondrial nucleoid; within-query FDR = 0.0179). It is linked to combined oxidative-phosphorylation defects, mitochondrial disease, and hereditary prostate cancer, with meaningful literature support.
- **Conclusion**: Established evidence supports ELAC2 as a functional representative of mitochondrial RNA maturation within the module. A possible interpretation is that mitochondrial RNA processing is coordinated with mitochondrial transcription and translation here, but this remains a hypothesis from network context rather than a demonstrated regulatory interaction.

#### UPF3B

- **Related proteins** (co-abundance neighbors): MDN1 (0.94), POLR2A (0.89), POLR1A (0.88), TOP2A (0.88), OSBPL11 (0.86), KIF23 (0.84), ZNF326 (0.83), CPSF7 (0.82), EMG1 (0.82); STRING partners: CWC22 (0.906)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UPF3B regulator of nonsense mediated mRNA decay. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. The encoded protein is one of two functional homologs to yeast Upf3p. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction…
- **Diseases (Open Targets)**: X-linked intellectual disability with marfanoid habitus (0.714); hereditary disease (0.493); non-syndromic X-linked intellectual disability (0.370); X-linked complex neurodevelopmental disorder (0.370); neurodevelopmental disorder (0.315)
- **Europe PMC papers**: 794
- **Why important**: UPF3B has the strongest network centrality in the supplied ranking and connects nuclear RNA surveillance with POLR2A, POLR1A, TOP2A, OSBPL11, KIF23, ZNF326, CPSF7, and MDN1. It is a component of nonsense-mediated mRNA decay and mRNA export, and it appears in the broad organelle-lumen terms (GO:CC membrane-enclosed lumen; q_global = 6.55e-05)(GO:CC organelle lumen; q_global = 6.55e-05)(GO:CC intracellular organelle lumen; q_global = 6.55e-05). Its STRING relationship with CWC22 supports a connection between splicing and mRNA surveillance. It has established associations with X-linked intellectual disability and a substantial literature.
- **Conclusion**: Established evidence supports UPF3B as a bridge between RNA processing and the broader nuclear machinery represented by the module. The idea that it coordinates RNA quality control with mitochondrial output is a useful hypothesis, but no causal link is shown.

#### LMNB1

- **Related proteins** (co-abundance neighbors): CAD (0.87), LARP7 (0.81), POLR1A (0.81), NUP98 (0.81), CWC22 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_10473.1
- **Function (MyGene.info)**: lamin B1. This gene encodes one of the two B-type lamin proteins and is a component of the nuclear lamina. A duplication of this gene is associated with autosomal dominant adult-onset leukodystrophy (ADLD). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: microcephaly 26, primary, autosomal dominant (0.723); autosomal dominant primary microcephaly (0.675); adult-onset autosomal dominant demyelinating leukodystrophy (0.670); hereditary disease (0.488); Syndrome with microcephaly as major feature (0.487)
- **Europe PMC papers**: 3851
- **Why important**: LMNB1 links the nuclear membrane and nuclear organization to CAD, LARP7, POLR1A, NUP98, and CWC22. It is represented in the organelle-lumen and DNA-binding terms (GO:CC membrane-enclosed lumen; q_global = 6.55e-05)(GO:CC organelle lumen; q_global = 6.55e-05)(GO:CC intracellular organelle lumen; q_global = 6.55e-05)(GO:MF DNA binding; q_global = 0.035), and hu.MAP places it with ATAD3A in a complex containing membrane and mitochondrial-associated proteins (hu.MAP huMAP3_10473.1). HPA enrichment in bone marrow and lymphoid tissue, together with erythrocyte and progenitor-associated single-cell annotations, makes it relevant to the possibility of shared cellular composition. Its associations with adult-onset demyelinating leukodystrophy and microcephaly are well established and it has extensive literature.
- **Conclusion**: Established evidence supports LMNB1 as a nuclear-envelope and chromatin-context gene that may connect cellular architecture with transcriptional state. Its progenitor-associated HPA pattern raises a composition-related alternative explanation, so a tissue-specific mechanistic role should not be inferred without cell-composition analysis.

## Module 6

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (15)**: ABRACL, BRIX1, GAR1, HDAC1, METAP1, NAA10, PDCD4, RAN, RPL3, POLR1C, FARSB, VARS1, TUBB8, CCT5, WDR3

### Function

The module is most consistent with a broadly expressed intracellular gene-expression and protein-production program centered on ribosome biogenesis, translation, RNA handling, protein maturation, and proteostasis. This interpretation is supported by the functions of RPL3, WDR3, BRIX1, GAR1, POLR1C, FARSB, VARS1, NAA10, METAP1, CCT5, and RAN, together with the dense STRING support linking ribosomal, nucleolar, tRNA-synthetase, chaperone, and nuclear-transport components. PDCD4 adds a regulatory layer involving translation initiation, transcriptional regulation, apoptosis, and inflammatory signaling. No GO or KEGG term passed global correction, so the functional interpretation is based on the concordant gene annotations and network structure rather than significant enrichment. The pattern is compatible with shared cellular biosynthetic activity in autonomic nervous system and kidney samples, but it does not establish a tissue-specific pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly intracellular, with nucleolar, nuclear, cytosolic, ribosomal, or microtubule locations. Most genes have low tissue specificity and low immune-cell specificity, arguing against a module driven primarily by blood contamination or a blood-cell population. Several genes show cell-type-enhanced or cell-type-enriched patterns in reproductive, epithelial, trophoblast, or other specialized cell types, so shared cellular composition or general proliferative and biosynthetic state could contribute to the co-abundance pattern. Kidney protein detection is present for many members, whereas matching autonomic-nervous-system protein data were unavailable; therefore the protein-detection evidence does not demonstrate equivalent protein abundance in both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a coherent, partly known interaction framework. RPL3 connects to CCT5, ABRACL, FARSB, RAN, and TUBB8 in the co-abundance graph and has STRING links to BRIX1, CCT5, METAP1, and POLR1C. BRIX1, POLR1C, and WDR3 form a particularly informative known-interaction neighborhood involving ribosome production and nucleolar function. FARSB and VARS1 are linked as aminoacyl-tRNA synthetase components, while CCT5 and RAN have a known STRING relationship involving chaperoning and nuclear transport or cell-cycle biology. STRING functional enrichment itself was absent, so these interactions are supportive context rather than a globally corrected enrichment result. hu.MAP provides two partially overlapping complexes, C1 and C2, both containing PDCD4 and FARSB. Because each complex contributes only a subset of its members to this module, the hu.MAP evidence supports known molecular context but does not define the entire module as one established complex. The mixture of confirmed physical or functional relationships and unlinked module edges suggests a connected co-abundance program assembled from several related cellular processes rather than a single canonical complex.

**STRING interactions (score >= 0.7)**: 11 of 105 gene pairs: BRIX1–POLR1C (0.868); BRIX1–RPL3 (0.871); BRIX1–WDR3 (0.889); CCT5–RAN (0.825); CCT5–RPL3 (0.731); FARSB–VARS1 (0.776); GAR1–WDR3 (0.774); METAP1–RPL3 (0.705); POLR1C–RPL3 (0.866); POLR1C–VARS1 (0.859); POLR1C–WDR3 (0.702)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05184.1 (PDCD4, FARSB; 2/9); huMAP3_08042.1 (PDCD4, FARSB; 2/13)

### Novelty

The underlying biology is not wholly new: ribosomal production, translation, tRNA charging, chaperoning, nuclear transport, and transcriptional regulation are established processes, and several module relationships are already represented in STRING or hu.MAP. The potentially new observation is the coordinated abundance of these genes across autonomic nervous system and kidney samples as a conserved module. That tissue-pair association may be a new systems-level finding, but the fact sheet does not provide an independent replication set, comparison with previously published co-abundance modules, or evidence that the tissue-pair association is absent from other datasets. Therefore the appropriate conclusion is that the module may be novel as a cross-tissue co-abundance pattern, while its component mechanisms are largely established. Absence from hu.MAP or STRING for some edges is not evidence of novelty.

**Hypothesis.** Hypothesis: the module reflects a shared demand for maintaining nucleolar activity, ribosome production, accurate translation, nascent-protein maturation, and nuclear transport in a common cellular population or physiological state present in both tissues. In this model, BRIX1, WDR3, GAR1, and POLR1C support ribosome and nucleolar functions; RPL3, FARSB, and VARS1 support translation and aminoacylation; CCT5 and NAA10 support protein folding and maturation; RAN supports nuclear transport; and PDCD4 and HDAC1 provide regulatory control over translation, transcription, and stress-responsive cell-state programs. This remains a mechanistic hypothesis because no globally significant GO or KEGG term, perturbation experiment, or tissue-specific causal evidence is available.

### Important genes

#### RPL3

- **Related proteins** (co-abundance neighbors): CCT5 (0.90), ABRACL (0.82), FARSB (0.82), RAN (0.82), TUBB8 (0.81); STRING partners: BRIX1 (0.871), CCT5 (0.731), METAP1 (0.705), POLR1C (0.866)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein L3. Ribosomes, the complexes that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L3P family of ribosomal proteins and it is located in the cytoplasm. The p…
- **Diseases (Open Targets)**: Duchenne muscular dystrophy (0.506); Orthomyxoviridae infectious disease (0.463); cystic fibrosis (0.389); neuromuscular disease caused by qualitative or quantitative defects of dystrophin (0.323); inflammatory bowel disease (0.308)
- **Europe PMC papers**: 2316
- **Why important**: RPL3 is the strongest topological hub in the module, connecting translation-related, chaperone-related, nuclear-transport, cytoskeletal, and aminoacylation-associated neighbors. Its established role as a large-subunit ribosomal protein and its STRING links to BRIX1, CCT5, METAP1, and POLR1C make it a useful anchor for the module's protein-production interpretation. Its broad tissue profile and kidney protein detection also fit a general cellular-maintenance program rather than a secreted or immune-specific signal.
- **Conclusion**: Established evidence supports RPL3 as a central ribosomal component and a network anchor. The hypothesis that RPL3 abundance helps couple ribosome output to the other module processes is plausible but is not demonstrated causally by this dataset.

#### PDCD4

- **Related proteins** (co-abundance neighbors): WDR3 (0.86), METAP1 (0.83), CCT5 (0.81), HDAC1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_05184.1, huMAP3_08042.1
- **Function (MyGene.info)**: programmed cell death 4. This gene is a tumor suppressor and encodes a protein that binds to the eukaryotic translation initiation factor 4A1 and inhibits its function by preventing RNA binding. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2010].
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.440); systemic lupus erythematosus (0.224); Tietze syndrome (0.211); atrial fibrillation (0.148); neoplasm (0.118)
- **Europe PMC papers**: 8828
- **Why important**: PDCD4 has a prominent network position and connects to WDR3, METAP1, CCT5, and HDAC1. It is the most literature-rich regulatory candidate among the module members and has established links to translation initiation, transcriptional regulation, apoptosis, inflammatory signaling, and epithelial-to-mesenchymal biology. Its participation in both hu.MAP contexts, C1 and C2, gives it additional complex-level support.
- **Conclusion**: Established evidence supports PDCD4 as a translational and regulatory modulator with disease relevance. A possible role as the module's state-sensitive control point is a hypothesis, not a demonstrated explanation for the cross-tissue co-abundance.

#### WDR3

- **Related proteins** (co-abundance neighbors): PDCD4 (0.86), NAA10 (0.81), POLR1C (0.81); STRING partners: BRIX1 (0.889), GAR1 (0.774), POLR1C (0.702)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 3. This gene encodes a nuclear protein containing 10 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, which usually include a trp-asp at the C-terminal end. Proteins belonging to the WD repeat family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. [provid…
- **Diseases (Open Targets)**: presbycusis (0.335); respiratory tract infectious disorder (0.184); neurodegenerative disease (0.143); preeclampsia (0.120); alcohol drinking (0.098)
- **Europe PMC papers**: 280
- **Why important**: WDR3 occupies a bridge position between PDCD4, NAA10, and POLR1C and has STRING links to BRIX1, GAR1, and POLR1C. Its established association with small-subunit ribosome biogenesis and nucleolar localization directly connects the module's regulatory and translation-related components.
- **Conclusion**: Established evidence supports WDR3 as a nucleolar ribosome-biogenesis factor and network bridge. It may help coordinate nucleolar activity with translation-related abundance, but the module does not establish that coordination mechanistically.

#### POLR1C

- **Related proteins** (co-abundance neighbors): WDR3 (0.81); STRING partners: BRIX1 (0.868), RPL3 (0.866), VARS1 (0.859), WDR3 (0.702)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase I and III subunit C. The protein encoded by this gene is a subunit of both RNA polymerase I and RNA polymerase III complexes. The encoded protein is part of the Pol core element. Mutations in this gene have been associated with Treacher Collins syndrome (TCS) and hypomyelinating leukodystrophy 11. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016].
- **Diseases (Open Targets)**: POLR-related leukodystrophy (0.748); leukodystrophy, hypomyelinating, 11 (0.740); Treacher Collins syndrome 3 (0.721); Treacher-Collins syndrome (0.693); hypomyelination-hypogonadotropic hypogonadism-hypodontia syndrome (0.607)
- **Europe PMC papers**: 667
- **Why important**: POLR1C links the co-abundance network to RNA polymerase function and has multiple STRING relationships with BRIX1, RPL3, VARS1, and WDR3. Its role in both RNA polymerase I and RNA polymerase III complexes provides a plausible connection between ribosomal RNA production, transcription, and the translation machinery. It also has well-established disease associations involving craniofacial development and leukodystrophy.
- **Conclusion**: Established evidence supports POLR1C as a transcriptional core component relevant to ribosome-related gene expression. Its position suggests a possible upstream transcriptional contribution to the module, but this regulatory direction is a hypothesis.

#### GAR1

- **Related proteins** (co-abundance neighbors): NAA10 (0.86), RAN (0.83); STRING partners: WDR3 (0.774)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GAR1 ribonucleoprotein. This gene is a member of the H/ACA snoRNPs (small nucleolar ribonucleoproteins) gene family. snoRNPs are involved in various aspects of rRNA processing and modification and have been classified into two families: C/D and H/ACA. The H/ACA snoRNPs also include the DKC1, NOLA2 and NOLA3 proteins. These four H/ACA snoRNP proteins localize to the dense fibrillar components of nucleoli and to coiled (Ca…
- **Diseases (Open Targets)**: neurodegenerative disease (0.400); prostate carcinoma (0.198); Thrombocytopenia (0.048); familial primary hypomagnesemia with normocalciuria and normocalcemia (0.041); renal hypomagnesemia 2 (0.041)
- **Europe PMC papers**: 1232
- **Why important**: GAR1 is a nucleolar and Cajal-body H or ACA snoRNP component involved in ribosomal RNA pseudouridylation, ribosome biogenesis, and telomerase-related biology. It connects RAN and NAA10 in the module and has STRING support with WDR3, placing it at the intersection of RNA processing, nuclear organization, and protein maturation. Its disease associations include neurodegenerative and renal-related conditions, which are relevant to the tissue pair without proving tissue specificity.
- **Conclusion**: Established evidence supports GAR1 as an RNA-modification and nucleolar-processing factor. Its co-abundance may indicate coordinated RNA maturation capacity, but that interpretation remains a hypothesis because no enrichment or perturbation evidence establishes a causal role.

## Module 7

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (46)**: ACIN1, ARFIP2, ASCC3, COPS7B, DDX46, DHX36, DIAPH1, POLA2, POLE, DRG2, EXOSC3, FANCD2, FKBP5, GMPS, MACROH2A1, HDHD5, HEATR1, HMGB3, PRKCI, MDC1, MLH1, NELFCD, ORC5, PARG, PPP4C, PSME4, PTDSS1, PPAT, ADSS2, QSOX2, RAVER1, RBBP5, POLR2B, PDCD11, SNRPA1, SETDB1, SMCHD1, SNRNP40, U2SURP, SRRT, STAG2, SYMPK, QARS1, TCERG1, TFIP11, USP28

### Function

The module is best interpreted as a conserved nuclear gene-expression and genome-maintenance program. Primary GO evidence supports nucleoplasm, nuclear lumen, and nuclear-body localization (GO:CC nucleoplasm; q_global = 0.000311)(GO:CC nuclear lumen; q_global = 0.00083)(GO:CC nuclear body; q_global = 0.00162), together with DNA metabolism, nucleic-acid metabolism, and DNA repair (GO:BP DNA metabolic process; q_global = 0.00246)(GO:BP nucleic acid metabolic process; q_global = 0.00434)(GO:BP nucleobase-containing compound metabolic process; q_global = 0.00698)(GO:BP DNA repair; q_global = 0.0435). The genes collectively span pre-mRNA splicing and RNA processing, transcriptional regulation, ribosome and rRNA maturation, DNA replication, chromatin organization, checkpoint signaling, mismatch repair, and double-strand-break repair. The network therefore appears to combine coordinated RNA maturation with genome surveillance and repair, rather than representing a narrowly specialized tissue pathway. The STRING results independently support nuclear localization and DNA-damage-related functions (STRING Keyword Nucleus; within-query FDR = 5.78e-06)(STRING COMPARTMENTS Nuclear lumen; within-query FDR = 7.8e-05)(STRING Component Nucleoplasm; within-query FDR = 0.00034)(STRING COMPARTMENTS Nucleus; within-query FDR = 0.00036)(STRING Process DNA metabolic process; within-query FDR = 0.0049)(STRING Keyword DNA damage; within-query FDR = 0.0103)(STRING Keyword DNA repair; within-query FDR = 0.0272), while also highlighting nucleic-acid metabolism (STRING Process Nucleobase-containing compound metabolic process; within-query FDR = 0.0017)(STRING Process Nucleic acid metabolic process; within-query FDR = 0.0017). The strongest network-connected RNA-processing components include SNRNP40, SNRPA1, DDX46, TCERG1, TFIP11, and U2SURP; the DNA-maintenance arm includes FANCD2, MDC1, MLH1, POLE, ASCC3, PARG, SMCHD1, PPP4C, and USP28.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary identifies only a single secreted gene, and the genes are predominantly intracellular and nuclear. The HPA profile is broadly expressed for most genes, with many showing low tissue specificity and low immune-cell specificity. Kidney protein detection is widespread among the assayed genes, whereas matching autonomic-nervous-system protein data are unavailable, so the protein evidence does not establish tissue-specific expression in the autonomic nervous system. Several genes are enhanced in reproductive, progenitor, skeletal-muscle, or selected epithelial and neural cell populations, but the overall profile does not resemble a blood-cell-enriched module. The module could therefore reflect a shared requirement for nuclear RNA handling, replication, and repair in resident cells of both tissues, with some contribution from cellular composition or proliferative state. It should not be interpreted as a secreted factor program or, on the available HPA evidence, as a simple blood-contamination signature.

**GO/KEGG enrichment**: 7 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC nucleoplasm | 0.000311 | ACIN1, ASCC3, COPS7B, DDX46, DHX36, DRG2, EXOSC3, FANCD2, FKBP5, HEATR1, MACROH2A1, MDC1, MLH1, NELFCD, ORC5, PARG, PDCD11, POLA2, POLE, POLR2B, PPP4C, PRKCI, PSME4, QSOX2, RBBP5, SETDB1, SMCHD1, SNRNP40, SNRPA1, SRRT, STAG2, SYMPK, TCERG1, TFIP11, U2SURP, USP28 |
| GO:CC nuclear lumen | 0.00083 | ACIN1, ARFIP2, ASCC3, COPS7B, DDX46, DHX36, DRG2, EXOSC3, FANCD2, FKBP5, HEATR1, MACROH2A1, MDC1, MLH1, NELFCD, ORC5, PARG, PDCD11, POLA2, POLE, POLR2B, PPP4C, PRKCI, PSME4, QSOX2, RBBP5, SETDB1, SMCHD1, SNRNP40, SNRPA1, SRRT, STAG2, SYMPK, TCERG1, TFIP11, U2SURP, USP28 |
| GO:CC nuclear body | 0.00162 | ACIN1, ASCC3, DDX46, DHX36, FANCD2, MDC1, PARG, PSME4, SMCHD1, SNRNP40, SNRPA1, SRRT, SYMPK, TCERG1, TFIP11, USP28 |
| GO:BP DNA metabolic process | 0.00246 | ASCC3, DHX36, EXOSC3, FANCD2, HMGB3, MACROH2A1, MDC1, MLH1, ORC5, PARG, POLA2, POLE, PPP4C, PSME4, SMCHD1, TFIP11, USP28 |
| GO:BP nucleic acid metabolic process | 0.00434 | ACIN1, ASCC3, DDX46, DHX36, EXOSC3, FANCD2, FKBP5, HEATR1, HMGB3, MACROH2A1, MDC1, MLH1, NELFCD, ORC5, PARG, PDCD11, POLA2, POLE, POLR2B, PPP4C, PSME4, QARS1, RBBP5, SMCHD1, SNRNP40, SNRPA1, SRRT, SYMPK, TCERG1, TFIP11, U2SURP, USP28 |
| GO:BP nucleobase-containing compound metabolic process | 0.00698 | ACIN1, ADSS2, ASCC3, DDX46, DHX36, EXOSC3, FANCD2, FKBP5, GMPS, HEATR1, HMGB3, MACROH2A1, MDC1, MLH1, NELFCD, ORC5, PARG, PDCD11, POLA2, POLE, POLR2B, PPAT, PPP4C, PSME4, QARS1, RBBP5, SMCHD1, SNRNP40, SNRPA1, SRRT, SYMPK, TCERG1, TFIP11, U2SURP, USP28 |
| GO:BP DNA repair | 0.0435 | ASCC3, FANCD2, MACROH2A1, MDC1, MLH1, PARG, POLE, PPP4C, PSME4, SMCHD1, TFIP11, USP28 |

### STRING and hu.MAP

STRING contains a coherent spliceosomal subnetwork: DDX46 connects strongly with SNRPA1, TCERG1, and U2SURP; SNRPA1 connects with SNRNP40, TCERG1, TFIP11, and U2SURP; and SNRNP40 connects with SNRPA1, TCERG1, and TFIP11. A separate DNA-repair subnetwork links FANCD2 with MDC1 and MLH1, and MLH1 with POLE; replication-related links include ORC5 with POLA2 and POLE, while POLA2 and POLE are tightly connected. The nucleolar and RNA-maturation portion is supported by HEATR1 with PDCD11, EXOSC3 with HEATR1 and PDCD11, and PDCD11 with POLR2B. These are known molecular relationships and show that part of the co-abundance structure recapitulates established physical or functional biology. hu.MAP independently places SNRPA1, DDX46, SNRNP40, and TFIP11 in a spliceosomal complex (hu.MAP huMAP3_08980.1), with related spliceosome and splicing-complex assignments (hu.MAP huMAP3_06511.1)(hu.MAP huMAP3_06726.1)(hu.MAP huMAP3_08501.1)(hu.MAP huMAP3_09504.1)(hu.MAP huMAP3_09945.1). SRRT and ACIN1 occur together in several RNA-processing and exon-junction-related complexes (hu.MAP huMAP3_10564.1)(hu.MAP huMAP3_09621.1)(hu.MAP huMAP3_11073.1)(hu.MAP huMAP3_09943.1). FANCD2 and HEATR1 also occur together in hu.MAP complexes (hu.MAP huMAP3_06247.1)(hu.MAP huMAP3_09592.1). Thus the module is not composed of wholly unknown interactions: known spliceosomal, DNA-repair, replication, and nucleolar relationships provide biological anchors. The co-abundance module nevertheless integrates these subsystems more broadly than any single listed complex.

**STRING interactions (score >= 0.7)**: 27 of 1035 gene pairs: ADSS2–GMPS (0.834); ADSS2–PPAT (0.814); ASCC3–MLH1 (0.734); DDX46–SNRPA1 (0.995); DDX46–TCERG1 (0.927); DDX46–U2SURP (0.918); EXOSC3–HEATR1 (0.76); EXOSC3–PDCD11 (0.731); FANCD2–MDC1 (0.936); FANCD2–MLH1 (0.971); GMPS–POLR2B (0.712); GMPS–PPAT (0.886); HEATR1–PDCD11 (0.999); MLH1–POLE (0.879); NELFCD–POLR2B (0.931); ORC5–POLA2 (0.766); ORC5–POLE (0.724); PDCD11–POLR2B (0.919); POLA2–POLE (0.993); SNRNP40–SNRPA1 (0.997); SNRNP40–TCERG1 (0.973); SNRNP40–TFIP11 (0.79); SNRPA1–TCERG1 (0.989); SNRPA1–TFIP11 (0.979); SNRPA1–U2SURP (0.934); SRRT–TCERG1 (0.839); TCERG1–U2SURP (0.741)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Nucleus (FDR = 5.78e-06, 38 genes); COMPARTMENTS Nuclear lumen (FDR = 7.8e-05, 27 genes); Component Nucleoplasm (FDR = 0.00034, 35 genes); COMPARTMENTS Nucleus (FDR = 0.00036, 37 genes); Component Nuclear lumen (FDR = 0.0005, 36 genes); Process Nucleobase-containing compound metabolic process (FDR = 0.0017, 31 genes); Process Nucleic acid metabolic process (FDR = 0.0017, 28 genes); COMPARTMENTS Nucleoplasm (FDR = 0.0022, 18 genes); Process DNA metabolic process (FDR = 0.0049, 15 genes); Component Nuclear body (FDR = 0.0054, 14 genes); Keyword DNA damage (FDR = 0.0103, 9 genes); Process Cellular nitrogen compound metabolic process (FDR = 0.0109, 32 genes); COMPARTMENTS Nuclear body (FDR = 0.0206, 10 genes); Keyword DNA repair (FDR = 0.0272, 8 genes); Component Nucleus (FDR = 0.0341, 39 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (SNRPA1, DDX46, SNRNP40, TFIP11; 4/97); huMAP3_06247.1 (PTDSS1, FANCD2, HEATR1; 3/65); huMAP3_06511.1 (SNRPA1, DDX46, TFIP11; 3/79); huMAP3_09592.1 (QSOX2, FANCD2, HEATR1; 3/95); huMAP3_10564.1 (SRRT, ACIN1; 2/37); huMAP3_06726.1 (SNRNP40, TFIP11; 2/37); huMAP3_08501.1 (SNRNP40, TFIP11; 2/47); huMAP3_09504.1 (SNRNP40, TFIP11; 2/51); huMAP3_09621.1 (SRRT, ACIN1; 2/56); huMAP3_09945.1 (SNRNP40, TFIP11; 2/61); huMAP3_11073.1 (SRRT, ACIN1; 2/67); huMAP3_09943.1 (SRRT, ACIN1; 2/78)

### Novelty

The constituent functions and many constituent relationships are established, so this should not be claimed as discovery of a new spliceosome, DNA-repair pathway, or nucleolar complex. The potentially novel observation is the conserved co-abundance of these RNA-processing, replication, chromatin, and DNA-repair genes across autonomic nervous system and kidney. That cross-tissue organization is not demonstrated by the STRING or hu.MAP annotations alone, because those resources describe molecular relationships rather than this specific tissue-pair co-abundance pattern. The finding is therefore best described as a new systems-level association that generates a testable hypothesis, not as proof of a new molecular interaction or pathway. Its interpretation should remain cautious because broadly expressed nuclear genes can co-vary with cell cycle, transcriptional activity, RNA-processing demand, or sample composition.

**Hypothesis.** Hypothesis: the shared module represents a conserved nuclear stress-and-maintenance state in which transcription and RNA maturation are coordinated with replication surveillance and DNA repair. In this model, the spliceosomal and RNA-processing group centered on SNRNP40, SNRPA1, DDX46, TCERG1, and TFIP11 supports accurate transcript maturation, while FANCD2, MDC1, MLH1, POLE, PARG, PPP4C, SMCHD1, and USP28 maintain genome integrity. Nucleolar components such as HEATR1, PDCD11, and EXOSC3 could couple ribosome biogenesis to the general nuclear workload. The shared signal in kidney and autonomic nervous system may consequently reflect common sensitivity of these tissues to transcriptional demand, replication-associated damage, or repair requirements. This is a hypothesis rather than a demonstrated causal mechanism; validation would require cell-resolved expression, perturbation, and direct measurement of RNA-processing and DNA-damage phenotypes in both tissues.

### Important genes

#### SNRNP40

- **Related proteins** (co-abundance neighbors): PARG (0.85), EXOSC3 (0.84), QARS1 (0.84), ASCC3 (0.83), SNRPA1 (0.83), COPS7B (0.83), PPAT (0.83), ADSS2 (0.81), ACIN1 (0.81), ARFIP2 (0.80), DHX36 (0.80), GMPS (0.80); STRING partners: SNRPA1 (0.997), TCERG1 (0.973), TFIP11 (0.79)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_06726.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 40. This gene encodes a component of the U5 small nuclear ribonucleoprotein (snRNP) particle. The U5 snRNP is part of the spliceosome, a multiprotein complex that catalyzes the removal of introns from pre-messenger RNAs. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.530); dengue disease (0.377); X-linked lymphoproliferative syndrome (0.058); autoimmune lymphoproliferative syndrome (0.055); Familial hemophagocytic lymphohistiocytosis (0.053)
- **Europe PMC papers**: 235
- **Why important**: SNRNP40 is the leading network hub by weighted connectivity in the module and occupies a central position among the spliceosomal genes. It is present in the primary nuclear and nucleic-acid terms (GO:CC nucleoplasm; q_global = 0.000311)(GO:CC nuclear lumen; q_global = 0.00083)(GO:CC nuclear body; q_global = 0.00162)(GO:BP nucleic acid metabolic process; q_global = 0.00434)(GO:BP nucleobase-containing compound metabolic process; q_global = 0.00698), has strong STRING links to SNRPA1, TCERG1, and TFIP11, and appears in several hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1)(hu.MAP huMAP3_06726.1)(hu.MAP huMAP3_08501.1)(hu.MAP huMAP3_09504.1)(hu.MAP huMAP3_09945.1). Its established function as a U5 snRNP and spliceosome component provides a direct mechanistic anchor for the RNA-processing arm. It also has substantial literature support and reported disease associations, although those associations do not establish a role in this tissue-pair module.
- **Conclusion**: Established: SNRNP40 is a central, kidney-detected nuclear spliceosomal component whose known molecular partners and annotations support RNA processing. Conclusion: it is a strong marker and plausible coordinator of the module's RNA-processing arm. Hypothesis: variation in SNRNP40 abundance could couple spliceosome capacity to the broader genome-maintenance state.

#### DDX46

- **Related proteins** (co-abundance neighbors): STAG2 (0.84), HMGB3 (0.83), QARS1 (0.83), PDCD11 (0.81), ASCC3 (0.80); STRING partners: SNRPA1 (0.995), TCERG1 (0.927), U2SURP (0.918)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_06511.1
- **Function (MyGene.info)**: DEAD-box helicase 46. This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribu…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); dengue disease (0.370); Hypercholesterolemia (0.203); lung adenocarcinoma (0.074); osteosarcoma (0.053)
- **Europe PMC papers**: 592
- **Why important**: DDX46 is a network connector between several module members and the spliceosomal subnetwork. It is included in the primary nuclear and nucleic-acid terms (GO:CC nucleoplasm; q_global = 0.000311)(GO:CC nuclear lumen; q_global = 0.00083)(GO:CC nuclear body; q_global = 0.00162)(GO:BP nucleic acid metabolic process; q_global = 0.00434)(GO:BP nucleobase-containing compound metabolic process; q_global = 0.00698), has strong STRING relationships with SNRPA1, TCERG1, and U2SURP, and occurs in hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1)(hu.MAP huMAP3_06511.1). Its established DEAD-box helicase function in pre-spliceosome assembly gives functional specificity beyond generic nuclear localization. Its disease and literature records support biological importance, while its kidney detection is consistent with the module being present in kidney cells.
- **Conclusion**: Established: DDX46 is a nuclear RNA helicase involved in spliceosome assembly and is embedded in known spliceosomal relationships. Conclusion: it is an important bridge within the RNA-processing component. Hypothesis: DDX46 may help couple transcript processing demand to the DNA-metabolism signals observed in the same module.

#### FANCD2

- **Related proteins** (co-abundance neighbors): ASCC3 (0.83); STRING partners: MDC1 (0.936), MLH1 (0.971)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_06247.1, huMAP3_09592.1
- **Function (MyGene.info)**: FA complementation group D2. The Fanconi anemia complementation group (FANC) currently includes FANCA, FANCB, FANCC, FANCD1 (also called BRCA2), FANCD2, FANCE, FANCF, FANCG, FANCI, FANCJ (also called BRIP1), FANCL, FANCM and FANCN (also called PALB2). The previously defined group FANCH is the same as FANCA. Fanconi anemia is a genetically heterogeneous recessive disorder characterized by cytogenetic instability, hypersensitiv…
- **Diseases (Open Targets)**: Fanconi anemia complementation group D2 (0.830); Fanconi anemia (0.814); acute myeloid leukemia (0.642); hereditary disease (0.497); leukemia (0.475)
- **Europe PMC papers**: 6528
- **Why important**: FANCD2 is a core genome-integrity gene and is present in every primary GO category from nuclear localization through DNA repair (GO:CC nucleoplasm; q_global = 0.000311)(GO:CC nuclear lumen; q_global = 0.00083)(GO:CC nuclear body; q_global = 0.00162)(GO:BP DNA metabolic process; q_global = 0.00246)(GO:BP nucleic acid metabolic process; q_global = 0.00434)(GO:BP nucleobase-containing compound metabolic process; q_global = 0.00698)(GO:BP DNA repair; q_global = 0.0435). It has a strong STRING relationship with MDC1 and MLH1 and appears with HEATR1 in hu.MAP complexes (hu.MAP huMAP3_06247.1)(hu.MAP huMAP3_09592.1). Its established role in interstrand-crosslink repair, double-strand-break repair, checkpoint signaling, and meiotic repair makes it one of the clearest functional anchors of the module. Its strong disease literature connects it to Fanconi anemia and leukemia-related biology.
- **Conclusion**: Established: FANCD2 is a DNA-repair and checkpoint factor with direct network support from MDC1 and MLH1. Conclusion: it is a principal representative of the module's genome-maintenance arm. Hypothesis: coordinated FANCD2 abundance may indicate elevated or sustained repair demand in the shared tissue state.

#### MDC1

- **Related proteins** (co-abundance neighbors): PDCD11 (0.87), HMGB3 (0.84), MLH1 (0.81); STRING partners: FANCD2 (0.936)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm, Nuclear bodies; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mediator of DNA damage checkpoint 1. The protein encoded by this gene contains an N-terminal forkhead domain, two BRCA1 C-terminal (BRCT) motifs and a central domain with 13 repetitions of an approximately 41-amino acid sequence. The encoded protein is required to activate the intra-S phase and G2/M phase cell cycle checkpoints in response to DNA damage. This nuclear protein interacts with phosphorylated histone H2AX near sites of DN…
- **Diseases (Open Targets)**: oligoasthenoteratozoospermia (0.465); neurodegenerative disease (0.332); nasopharyngeal carcinoma (0.102); neoplasm (0.100); breast cancer (0.091)
- **Europe PMC papers**: 3963
- **Why important**: MDC1 links DNA-damage signaling to the module's nuclear network. It appears in all primary GO evidence categories, including DNA repair (GO:CC nucleoplasm; q_global = 0.000311)(GO:CC nuclear lumen; q_global = 0.00083)(GO:CC nuclear body; q_global = 0.00162)(GO:BP DNA metabolic process; q_global = 0.00246)(GO:BP nucleic acid metabolic process; q_global = 0.00434)(GO:BP nucleobase-containing compound metabolic process; q_global = 0.00698)(GO:BP DNA repair; q_global = 0.0435), connects strongly to FANCD2 in STRING, and is connected in the co-abundance graph to PDCD11, HMGB3, and MLH1. Its established function in recruiting and organizing the response to double-strand breaks gives a mechanistic explanation for the DNA-repair signal. Its cell-type annotations include neural and kidney-relevant epithelial populations, while its disease literature includes cancer and reproductive associations.
- **Conclusion**: Established: MDC1 is a DNA-damage-response scaffold represented across the module's primary functional evidence. Conclusion: it is a strong candidate for coordinating repair signaling within the module. Hypothesis: MDC1 may connect transcriptional or replication-associated lesions to the broader RNA-processing program.

#### POLE

- **Related proteins** (co-abundance neighbors): HEATR1 (0.89), PPAT (0.84), SYMPK (0.84); STRING partners: MLH1 (0.879), ORC5 (0.724), POLA2 (0.993)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA polymerase epsilon, catalytic subunit. This gene encodes the catalytic subunit of DNA polymerase epsilon. The enzyme is involved in DNA repair and chromosomal DNA replication. Mutations in this gene have been associated with colorectal cancer 12 and facial dysmorphism, immunodeficiency, livedo, and short stature. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal cancer, susceptibility to, 12 (0.739); intrauterine growth retardation, metaphyseal dysplasia, adrenal hypoplasia congenita, genital anomalies, and immunodeficiency (0.735); facial dysmorphism-immunodeficiency-livedo-short stature syndrome (0.732); non-small cell lung carcinoma (0.668); B-cell chronic lymphocytic leukemia (0.660)
- **Europe PMC papers**: 71098
- **Why important**: POLE provides the replication and repair synthesis component of the module. It is present in the primary DNA-metabolism and DNA-repair terms (GO:CC nucleoplasm; q_global = 0.000311)(GO:CC nuclear lumen; q_global = 0.00083)(GO:BP DNA metabolic process; q_global = 0.00246)(GO:BP nucleic acid metabolic process; q_global = 0.00434)(GO:BP nucleobase-containing compound metabolic process; q_global = 0.00698)(GO:BP DNA repair; q_global = 0.0435), has strong STRING relationships with MLH1, ORC5, and POLA2, and is connected in the module to HEATR1, PPAT, and SYMPK. Its established catalytic role in leading-strand DNA replication and repair makes it a functional link between replication activity and genome surveillance. It has extensive literature and well-established associations with colorectal cancer and inherited syndromic disease.
- **Conclusion**: Established: POLE is a replication and DNA-repair polymerase supported by coherent network relationships with mismatch-repair and replication factors. Conclusion: it is a key indicator that the module is not merely an RNA-processing signature. Hypothesis: POLE abundance may reflect coordinated control of replication-associated repair in the shared tissue state.

#### STAG2

- **Related proteins** (co-abundance neighbors): QARS1 (0.85), DDX46 (0.84), HMGB3 (0.82), DIAPH1 (0.80), RAVER1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Nucleoli fibrillar center; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: STAG2 cohesin complex component. The protein encoded by this gene is a subunit of the cohesin complex, which regulates the separation of sister chromatids during cell division. Targeted inactivation of this gene results in chromatid cohesion defects and aneuploidy, suggesting that genetic disruption of cohesin is a cause of aneuploidy in human cancer. Alternatively spliced transcript variants encoding different isoforms have been…
- **Diseases (Open Targets)**: Mullegama-Klein-Martinez syndrome (0.766); alobar holoprosencephaly (0.733); neurodegenerative disease (0.541); urinary bladder cancer (0.541); Ewing sarcoma (0.523)
- **Europe PMC papers**: 3936
- **Why important**: STAG2 contributes chromosome-structure and cell-division biology to a module otherwise dominated by RNA and DNA metabolism. It is present in the primary nuclear terms (GO:CC nucleoplasm; q_global = 0.000311)(GO:CC nuclear lumen; q_global = 0.00083), connects in the module to QARS1, DDX46, HMGB3, DIAPH1, and RAVER1, and is associated with neutrophil progenitor and neutrophil cell states in HPA. Its established role as a cohesin-complex component links chromosome cohesion, chromatin organization, and genome stability. It has a large literature base and disease associations including cohesin-related developmental syndromes and cancer.
- **Conclusion**: Established: STAG2 is a cohesin component with relevance to chromosome maintenance and cell division, and it occupies a bridge position in the module. Conclusion: it broadens the interpretation from DNA repair alone to chromosome organization and nuclear integrity. Hypothesis: STAG2 may mark a shared requirement for preserving chromosome structure while RNA processing and genome maintenance are active.

## Module 8

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (5)**: ACLY, FASN, MOGS, RPL6, IARS1

### Function

The most coherent functional interpretation is a metabolic and cellular-maintenance module centered on cytosolic acetyl-CoA and fatty-acid synthesis, with additional links to translation and endoplasmic-reticulum glycoprotein processing. ACLY supplies cytosolic acetyl-CoA and FASN uses acetyl-CoA and malonyl-CoA to synthesize long-chain fatty acids. IARS1 supports translational fidelity, RPL6 represents the ribosomal component, and MOGS supports early N-linked glycosylation and protein folding. The network therefore appears biologically mixed rather than a clean canonical pathway. No GO/KEGG term passed global correction; consequently, the functional interpretation is based on individual gene functions and network structure rather than statistically significant pathway enrichment. The absence of an enriched term does not by itself invalidate the module.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not blood-cell enriched; the genes have low immune-cell specificity overall, with one reported as not detected in immune cells. Most genes have low tissue specificity, while FASN is tissue enhanced in adipose tissue, breast, and liver. Cell-type patterns are heterogeneous, including pancreatic islet, breast lactating, late spermatid, decidual stromal, and esophageal suprabasal annotations. Kidney protein detection is reported for most genes, whereas FASN is not detected there; there is no matching HPA tissue for the autonomic nervous system. Thus, the module is more consistent with broadly expressed cellular metabolism and biosynthetic activity than with a blood or secretome artifact, although shared cellular composition and tissue-specific abundance remain plausible explanations for cross-tissue co-abundance.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The reported high-confidence STRING evidence consists of the ACLY–FASN relationship. This is biologically concordant because ACLY produces acetyl-CoA and FASN consumes acetyl-CoA during fatty-acid synthesis. No STRING functional-enrichment result was reported, and the other module genes have no reported STRING partners in the fact sheet. No hu.MAP complex contains multiple module members. Therefore, the module has limited support from previously catalogued physical interaction or complex maps: the ACLY–FASN connection is established, while the remaining co-abundance edges should not be interpreted as demonstrated protein-protein interactions.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: ACLY–FASN (0.994)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The underlying biochemical functions of the genes, especially ACLY and FASN, are well established and heavily represented in the literature, so the module is not a new discovery of those individual functions. The cross-tissue co-abundance pattern may represent a potentially novel observation, particularly because most of its relationships are not captured by STRING or hu.MAP. However, database absence alone cannot establish novelty. The lack of globally significant GO/KEGG enrichment and the broad-expression HPA profile also make a strong claim of a newly defined pathway unwarranted. The most defensible conclusion is that this is a potentially interesting shared expression module whose novelty lies in its tissue-pair co-abundance context, not in a newly discovered molecular function.

**Hypothesis.** Hypothesis: the shared module reflects coordinated biosynthetic demand in cells present in both tissue groups. ACLY and FASN may form the metabolic core, coupling citrate-derived acetyl-CoA to fatty-acid production, while IARS1 and RPL6 reflect accompanying protein-synthesis demand and MOGS reflects endoplasmic-reticulum glycoprotein processing. The observed co-abundance could therefore arise from a common cellular state involving lipid anabolism, translation, and secretory-pathway or protein-folding activity. This is a hypothesis rather than a demonstrated physical complex or pathway, and it should be tested with cell-type-resolved expression, perturbation of ACLY or FASN, and measurements of lipid synthesis, translation, and glycoprotein maturation.

### Important genes

#### ACLY

- **Related proteins** (co-abundance neighbors): FASN (0.88), MOGS (0.86), IARS1 (0.84); STRING partners: FASN (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP citrate lyase. ATP citrate lyase is the primary enzyme responsible for the synthesis of cytosolic acetyl-CoA in many tissues. The enzyme is a tetramer (relative molecular weight approximately 440,000) of apparently identical subunits. It catalyzes the formation of acetyl-CoA and oxaloacetate from citrate and CoA with a concomitant hydrolysis of ATP to ADP and phosphate. The product, acetyl-CoA, serves several im…
- **Diseases (Open Targets)**: familial hypercholesterolemia (0.532); Hypercholesterolemia (0.532); atherosclerosis (0.470); inherited lipid metabolism disorder (0.467); cardiovascular disorder (0.449)
- **Europe PMC papers**: 7957
- **Why important**: ACLY has the strongest network connectivity in the module and connects directly to FASN, IARS1, and MOGS. Its established function as the primary source of cytosolic acetyl-CoA provides the clearest metabolic anchor for the module. It is detected in kidney, has broad tissue expression, is enhanced in pancreatic islet cells, and has extensive literature and disease associations involving hypercholesterolemia, atherosclerosis, and inherited lipid metabolism disorders.
- **Conclusion**: Established evidence supports ACLY as the central metabolic candidate and as a plausible driver of the ACLY–FASN relationship. It is not established that ACLY organizes the entire module or explains the autonomic nervous system–kidney sharing; that broader organizing role remains a hypothesis.

#### FASN

- **Related proteins** (co-abundance neighbors): ACLY (0.88), IARS1 (0.82); STRING partners: ACLY (0.994)
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fatty acid synthase. The enzyme encoded by this gene is a multifunctional protein. Its main function is to catalyze the synthesis of palmitate from acetyl-CoA and malonyl-CoA, in the presence of NADPH, into long-chain saturated fatty acids. In some cancer cell lines, this protein has been found to be fused with estrogen receptor-alpha (ER-alpha), in which the N-terminus of FAS is fused in-frame with the C-terminus of …
- **Diseases (Open Targets)**: dengue disease (0.469); autism spectrum disorder (0.333); Parkinson disease (0.295); Epileptic encephalopathy (0.211); neurodegenerative disease (0.205)
- **Europe PMC papers**: 21528
- **Why important**: FASN is the direct biochemical partner of ACLY in the reported STRING network supplementary STRING and catalyzes palmitate synthesis from acetyl-CoA and malonyl-CoA. Its tissue-enhanced HPA profile in adipose tissue, breast, and liver makes it the most tissue-specialized metabolic member. It has very extensive literature and disease associations spanning metabolic, neurological, and cancer-related contexts, although the fact sheet does not establish a specific disease mechanism for this module.
- **Conclusion**: Established evidence supports FASN as the principal lipid-anabolic counterpart of ACLY. Its tissue-enhanced profile also raises the possibility that variation in cellular composition or lipid-anabolic state contributes to the module. A direct functional role for FASN in the shared autonomic nervous system–kidney module remains unproven.

#### IARS1

- **Related proteins** (co-abundance neighbors): RPL6 (0.88), ACLY (0.84), FASN (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Isoleucine-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family and has been identified as a …
- **Diseases (Open Targets)**: growth retardation, intellectual developmental disorder, hypotonia, and hepatopathy (0.733); Abnormality of the skeletal system (0.332); microcephaly (0.289); Global developmental delay (0.289); Hallux valgus (0.184)
- **Europe PMC papers**: 184
- **Why important**: IARS1 is highly connected within the co-abundance graph, linking RPL6, ACLY, and FASN. Its established role in isoleucyl-tRNA aminoacylation and translational fidelity provides a plausible connection between metabolic activity and protein-production demand. It is broadly expressed, detected in kidney, and associated with developmental phenotypes and autoimmune recognition in the supplied annotations, while its literature volume is smaller than that of ACLY or FASN.
- **Conclusion**: Established evidence supports IARS1 as a translation-related component that may report cellular biosynthetic demand. Its connection to the lipid enzymes is a co-abundance observation rather than proof of a shared biochemical complex, so its proposed bridging role is hypothetical.

#### MOGS

- **Related proteins** (co-abundance neighbors): ACLY (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosyl-oligosaccharide glucosidase. This gene encodes the first enzyme in the N-linked oligosaccharide processing pathway. The enzyme cleaves the distal alpha-1,2-linked glucose residue from the Glc(3)-Man(9)-GlcNAc(2) oligosaccharide precursor. This protein is located in the lumen of the endoplasmic reticulum. Defects in this gene are a cause of type IIb congenital disorder of glycosylation (CDGIIb). Two transcript variants encodin…
- **Diseases (Open Targets)**: MOGS-congenital disorder of glycosylation (0.818); congenital disorder of glycosylation (0.374); congenital disorder of glycosylation type II (0.370); severe acute respiratory syndrome (0.370); SRD5A3-congenital disorder of glycosylation (0.370)
- **Europe PMC papers**: 987
- **Why important**: MOGS connects to ACLY in the module and is the only member whose supplied function directly places it in the endoplasmic reticulum, where it initiates processing of N-linked oligosaccharides. It is detected in kidney, has low tissue specificity, and has established disease associations with congenital disorders of glycosylation. Its literature volume is intermediate relative to the major lipid enzymes.
- **Conclusion**: Established evidence supports MOGS as an ER glycoprotein-processing enzyme and a relevant kidney-detected module member. The ACLY–MOGS co-abundance edge does not establish a direct mechanistic interaction; linking glycoprotein processing to lipid synthesis is a testable hypothesis.

## Module 9

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (15)**: ACSL3, CDH2, CKAP4, EGFR, GOLIM4, GPD2, ITGAV, ITGB1, L1CAM, MPP2, NCEH1, RAB18, SEC22B, SORT1, VAPB

### Function

The module is best interpreted as a membrane- and organelle-trafficking program coupled to cell adhesion and receptor signaling. The primary evidence is the globally corrected enrichment for cell adhesion molecule interaction (KEGG Cell adhesion molecule (CAM) interaction - Homo sapiens (human); q_global = 0.00136), signaling receptor and molecular transducer activity (GO:MF signaling receptor activity; q_global = 0.00186)(GO:MF molecular transducer activity; q_global = 0.00186), cell-surface and plasma-membrane localization (GO:CC cell surface; q_global = 0.00526)(GO:CC plasma membrane; q_global = 0.00644), endoplasmic-reticulum and vesicle-membrane compartments (GO:CC organelle subcompartment; q_global = 0.00813)(GO:CC endoplasmic reticulum membrane; q_global = 0.0132)(GO:CC endoplasmic reticulum subcompartment; q_global = 0.0132)(GO:CC cytoplasmic vesicle membrane; q_global = 0.0142)(GO:CC nuclear outer membrane-endoplasmic reticulum membrane network; q_global = 0.0142)(GO:CC vesicle membrane; q_global = 0.0154)(GO:CC organelle membrane; q_global = 0.0287), homophilic cell-cell adhesion (GO:BP homophilic cell-cell adhesion; q_global = 0.0176), and growth-factor binding (GO:MF growth factor binding; q_global = 0.0272). CDH2, ITGAV, ITGB1, and L1CAM form the clearest adhesion-receptor axis, while EGFR and SORT1 support receptor and cargo-trafficking functions. SEC22B, GOLIM4, VAPB, CKAP4, RAB18, and related genes indicate ER-to-Golgi, vesicle, and organelle-membrane handling. Thus, this is not a narrowly defined single biochemical pathway; it is a coordinated cell-surface adhesion, signaling, and membrane-trafficking module.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: the HPA summary identifies only a single secreted gene, and most members are intracellular or membrane-associated. It is also not uniformly blood-cell enriched. HPA shows generally low tissue specificity for much of the module, while all members have some cell-type enhancement and subsets are associated with neutrophils, monocyte populations, basophils, eosinophils, podocytes, neurons, cardiomyocytes, and epithelial populations. This broad and mixed cellular pattern cautions against assigning the module exclusively to autonomic nervous tissue or kidney parenchyma. Shared cellular composition, vascular or immune admixture, or a common membrane-trafficking state could contribute to its conservation. Kidney protein detection is widespread across the module, whereas there is no matching HPA tissue-protein assessment for autonomic nervous system, so the tissue-level comparison should be interpreted cautiously.

**GO/KEGG enrichment**: 15 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Cell adhesion molecule (CAM) interaction - Homo sapiens (human) | 0.00136 | CDH2, ITGAV, ITGB1, L1CAM |
| GO:MF signaling receptor activity | 0.00186 | EGFR, ITGAV, ITGB1, L1CAM, SORT1 |
| GO:MF molecular transducer activity | 0.00186 | EGFR, ITGAV, ITGB1, L1CAM, SORT1 |
| GO:CC cell surface | 0.00526 | CDH2, EGFR, ITGAV, ITGB1, L1CAM, SORT1 |
| GO:CC plasma membrane | 0.00644 | ACSL3, CDH2, CKAP4, EGFR, ITGAV, ITGB1, L1CAM, MPP2, NCEH1, RAB18, SORT1, VAPB |
| GO:CC organelle subcompartment | 0.00813 | ACSL3, CKAP4, EGFR, GOLIM4, NCEH1, RAB18, SEC22B, SORT1, VAPB |
| GO:CC cell periphery | 0.0112 | ACSL3, CDH2, CKAP4, EGFR, ITGAV, ITGB1, L1CAM, MPP2, NCEH1, RAB18, SORT1, VAPB |
| GO:CC endoplasmic reticulum membrane | 0.0132 | ACSL3, CKAP4, EGFR, NCEH1, RAB18, SEC22B, SORT1, VAPB |
| GO:CC endoplasmic reticulum subcompartment | 0.0132 | ACSL3, CKAP4, EGFR, NCEH1, RAB18, SEC22B, SORT1, VAPB |
| GO:CC cytoplasmic vesicle membrane | 0.0142 | CKAP4, EGFR, GOLIM4, ITGAV, ITGB1, RAB18, SEC22B, SORT1 |
| GO:CC nuclear outer membrane-endoplasmic reticulum membrane network | 0.0142 | ACSL3, CKAP4, EGFR, NCEH1, RAB18, SEC22B, SORT1, VAPB |
| GO:CC vesicle membrane | 0.0154 | CKAP4, EGFR, GOLIM4, ITGAV, ITGB1, RAB18, SEC22B, SORT1 |
| GO:BP homophilic cell-cell adhesion | 0.0176 | CDH2, ITGB1, L1CAM |
| GO:MF growth factor binding | 0.0272 | EGFR, ITGAV, SORT1 |
| GO:CC organelle membrane | 0.0287 | ACSL3, CKAP4, EGFR, GOLIM4, GPD2, ITGAV, ITGB1, NCEH1, RAB18, SEC22B, SORT1, VAPB |

### STRING and hu.MAP

STRING supports a known adhesion and receptor-interaction core: ITGAV–ITGB1, EGFR–ITGB1, EGFR–L1CAM, ITGB1–L1CAM, CDH2–ITGB1, and CDH2–EGFR are high-confidence relationships. These interactions make the adhesion and receptor-signaling interpretation biologically coherent rather than being based only on co-abundance. STRING supplementary enrichment also supports membrane, cell-surface, transmembrane, ER-membrane, vesicle-membrane, and cell-adhesion themes (15 supplementary STRING terms; within-query FDR 3.48e-07–0.0011), but these are supplementary evidence rather than globally corrected module significance. hu.MAP identifies a shared complex context for GOLIM4, VAPB, and CKAP4 (hu.MAP huMAP3_10725.1), and a second complex context for GOLIM4 and CKAP4 (hu.MAP huMAP3_09822.1). The absence of hu.MAP assignments for the adhesion-receptor genes and the absence of STRING partners for several trafficking genes indicate that the module combines a well-established adhesion core with a less directly connected trafficking and organelle-associated branch.

**STRING interactions (score >= 0.7)**: 6 of 105 gene pairs: CDH2–EGFR (0.78); CDH2–ITGB1 (0.818); EGFR–ITGB1 (0.966); EGFR–L1CAM (0.976); ITGAV–ITGB1 (0.999); ITGB1–L1CAM (0.909)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transmembrane (FDR = 3.48e-07, 12 genes); Component Intrinsic component of membrane (FDR = 2.88e-06, 13 genes); Keyword Transmembrane helix (FDR = 3.43e-06, 11 genes); Keyword Membrane (FDR = 1.77e-05, 14 genes); Component Integral component of membrane (FDR = 2.72e-05, 12 genes); COMPARTMENTS Cell surface (FDR = 0.00025, 6 genes); COMPARTMENTS Membrane (FDR = 0.00025, 14 genes); KEGG Cell adhesion molecules (FDR = 0.00039, 4 genes); Keyword Glycoprotein (FDR = 0.0006, 8 genes); Component Plasma membrane (FDR = 0.00065, 12 genes); Component Cell surface (FDR = 0.00065, 6 genes); Component Organelle subcompartment (FDR = 0.00065, 9 genes); Component Endoplasmic reticulum membrane (FDR = 0.00088, 8 genes); Component Cytoplasmic vesicle membrane (FDR = 0.00088, 8 genes); Component Organelle membrane (FDR = 0.0011, 12 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10725.1 (GOLIM4, VAPB, CKAP4; 3/59); huMAP3_09822.1 (GOLIM4, CKAP4; 2/28)

### Novelty

The module should be regarded as a potentially new tissue-pair co-abundance observation, not as a newly established molecular complex or mechanism. The adhesion-receptor relationships are already known from STRING, and the GOLIM4–VAPB–CKAP4 and GOLIM4–CKAP4 contexts are represented in hu.MAP. What may be novel is their coordinated abundance across autonomic nervous system and kidney, together with the accompanying ER, Golgi, vesicle, lipid, and mitochondrial genes. However, the fact sheet does not establish replication, directionality, cell-type specificity, or independence from tissue composition. Therefore, absence of a complete matching structure in STRING or hu.MAP is not sufficient to claim discovery; validation in independent cohorts and cell-resolved data is required.

**Hypothesis.** Hypothesis: the conserved module reflects a shared cellular state in which adhesion receptors and growth-factor signaling are coupled to membrane biosynthesis and vesicle trafficking. An ITGAV–ITGB1, CDH2, and L1CAM surface-adhesion network may organize contacts with neighboring cells or extracellular matrix, while EGFR provides growth-factor-responsive signaling. SORT1, SEC22B, GOLIM4, CKAP4, VAPB, RAB18, and lipid-associated genes may support receptor sorting, ER-to-Golgi transport, membrane remodeling, and delivery of adhesion components. In kidney this could involve epithelial or podocyte membrane organization; in autonomic nervous system it could involve neuronal or glial adhesion and trafficking. The same abundance pattern could also arise partly from shared vascular or immune-cell admixture, so this mechanistic interpretation remains a testable hypothesis rather than an established causal model.

### Important genes

#### ITGB1

- **Related proteins** (co-abundance neighbors): EGFR (0.83), L1CAM (0.82), GOLIM4 (0.82), ACSL3 (0.81); STRING partners: CDH2 (0.818), EGFR (0.966), ITGAV (0.999), L1CAM (0.909)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is the strongest network-centered gene in the module and connects the adhesion-receptor core to EGFR, L1CAM, GOLIM4, and ACSL3. It occurs across the primary cell-adhesion, receptor-activity, cell-surface, plasma-membrane, and homophilic-adhesion terms (KEGG Cell adhesion molecule (CAM) interaction - Homo sapiens (human); q_global = 0.00136)(GO:MF signaling receptor activity; q_global = 0.00186)(GO:CC cell surface; q_global = 0.00526)(GO:CC plasma membrane; q_global = 0.00644)(GO:CC cell periphery; q_global = 0.0112)(GO:CC cytoplasmic vesicle membrane; q_global = 0.0142)(GO:CC vesicle membrane; q_global = 0.0154)(GO:BP homophilic cell-cell adhesion; q_global = 0.0176)(GO:CC organelle membrane; q_global = 0.0287). Its established integrin function links cell adhesion, recognition, tissue repair, immune responses, angiogenesis, and phagocytosis. It has extensive literature and disease associations involving inflammation, Crohn disease, and type one diabetes. HPA places it at the plasma membrane and focal adhesions and detects it in kidney.
- **Conclusion**: Established evidence supports ITGB1 as the principal adhesion and signaling integrator of the module. It is a strong candidate for organizing the shared co-abundance state, but the data do not prove that ITGB1 causally drives the module or that its interaction partners are present in the same cell in both tissues.

#### EGFR

- **Related proteins** (co-abundance neighbors): ITGB1 (0.83); STRING partners: CDH2 (0.78), ITGB1 (0.966), L1CAM (0.976)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus, Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: epidermal growth factor receptor. The protein encoded by this gene is a transmembrane glycoprotein that is a member of the protein kinase superfamily. This protein is a receptor for members of the epidermal growth factor family. EGFR is a cell surface protein that binds to epidermal growth factor, thus inducing receptor dimerization and tyrosine autophosphorylation leading to cell proliferation. Mutations in this gene are associat…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.850); lung adenocarcinoma (0.774); cancer (0.737); head and neck squamous cell carcinoma (0.725); lung cancer (0.717)
- **Europe PMC papers**: 223694
- **Why important**: EGFR is a receptor tyrosine kinase with extensive literature and strong disease relevance, especially for lung cancer and other cancers. It occupies the receptor-activity, molecular-transducer, cell-surface, organelle, vesicle, and growth-factor-binding annotations (GO:MF signaling receptor activity; q_global = 0.00186)(GO:MF molecular transducer activity; q_global = 0.00186)(GO:CC cell surface; q_global = 0.00526)(GO:CC organelle subcompartment; q_global = 0.00813)(GO:CC cytoplasmic vesicle membrane; q_global = 0.0142)(GO:CC vesicle membrane; q_global = 0.0154)(GO:MF growth factor binding; q_global = 0.0272)(GO:CC organelle membrane; q_global = 0.0287). Its high-confidence STRING relationships with ITGB1, L1CAM, and CDH2 connect growth-factor signaling to the adhesion core. HPA detects EGFR in kidney and places it at the Golgi and plasma membrane; it is also reported as secreted to blood.
- **Conclusion**: Established evidence supports EGFR as the signaling component that could couple adhesion and trafficking to growth-factor responses. Its reported blood secretion and broad disease literature make it biologically important, but they also mean that abundance may reflect general epithelial, vascular, or systemic biology rather than a tissue-pair-specific mechanism.

#### CDH2

- **Related proteins** (co-abundance neighbors): SEC22B (0.88), ITGAV (0.83), RAB18 (0.81); STRING partners: EGFR (0.78), ITGB1 (0.818)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cadherin 2. This gene encodes a classical cadherin and member of the cadherin superfamily. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein is proteolytically processed to generate a calcium-dependent cell adhesion molecule and glycoprotein. This protein plays a role in the establishment of left-right asymmetry, development of the nervous system and t…
- **Diseases (Open Targets)**: agenesis of corpus callosum, cardiac, ocular, and genital syndrome (0.809); arrhythmogenic right ventricular dysplasia, familial, 14 (0.583); Agenesis of corpus callosum (0.515); attention deficit-hyperactivity disorder 8 (0.505); aortic stenosis (0.481)
- **Europe PMC papers**: 35205
- **Why important**: CDH2 is a classical calcium-dependent cell-adhesion molecule with extensive literature. It is annotated for cell-cell junction assembly, homophilic adhesion, synapse assembly, nervous-system development, and morphogenesis, and it contributes to the primary adhesion and cell-surface evidence (KEGG Cell adhesion molecule (CAM) interaction - Homo sapiens (human); q_global = 0.00136)(GO:CC cell surface; q_global = 0.00526)(GO:CC plasma membrane; q_global = 0.00644)(GO:CC cell periphery; q_global = 0.0112)(GO:BP homophilic cell-cell adhesion; q_global = 0.0176). Its network links include SEC22B, ITGAV, and RAB18, while STRING supports relationships with EGFR and ITGB1. HPA shows heart-muscle and neuronal cell-type associations, as well as kidney detection, making it relevant to both neural and epithelial interpretations.
- **Conclusion**: Established evidence supports CDH2 as a structural cell-contact component and a plausible bridge between adhesion and membrane trafficking. Its neural and epithelial relevance fits the tissue pair, but blood-cell group enrichment and broad cellular expression leave open the possibility that composition contributes to its apparent conservation.

#### L1CAM

- **Related proteins** (co-abundance neighbors): CKAP4 (0.84), ITGB1 (0.82), GPD2 (0.81); STRING partners: EGFR (0.976), ITGB1 (0.909)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm, Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: L1 cell adhesion molecule. The protein encoded by this gene is an axonal glycoprotein belonging to the immunoglobulin supergene family. The ectodomain, consisting of several immunoglobulin-like domains and fibronectin-like repeats (type III), is linked via a single transmembrane sequence to a conserved cytoplasmic domain. This cell adhesion molecule plays an important role in nervous system development, including neuronal m…
- **Diseases (Open Targets)**: X-linked hydrocephalus with stenosis of the aqueduct of Sylvius (0.855); MASA syndrome (0.833); X-linked complicated corpus callosum dysgenesis (0.762); L1 syndrome (0.725); Spastic paraplegia (0.571)
- **Europe PMC papers**: 6523
- **Why important**: L1CAM is a neuronal cell-adhesion glycoprotein involved in neuronal migration, differentiation, axon guidance, and nervous-system development. It contributes to the cell-adhesion, receptor-activity, cell-surface, plasma-membrane, and homophilic-adhesion evidence (KEGG Cell adhesion molecule (CAM) interaction - Homo sapiens (human); q_global = 0.00136)(GO:MF signaling receptor activity; q_global = 0.00186)(GO:CC cell surface; q_global = 0.00526)(GO:CC plasma membrane; q_global = 0.00644)(GO:CC cell periphery; q_global = 0.0112)(GO:BP homophilic cell-cell adhesion; q_global = 0.0176). It is connected in the module to CKAP4, ITGB1, and GPD2, and has high-confidence STRING relationships with EGFR and ITGB1. HPA shows enrichment in brain and intestinal tissue and in multiple neuronal cell types, with kidney protein detection. Its disease associations include L1 syndrome, hydrocephalus, and corpus-callosum dysgenesis, supported by substantial literature.
- **Conclusion**: Established evidence supports L1CAM as the strongest neural-adhesion marker among the selected genes and as a plausible link between the autonomic nervous system context and the shared adhesion network. Its presence does not establish neuronal origin for the whole module, because the module also contains broadly expressed and non-neural trafficking genes.

#### SEC22B

- **Related proteins** (co-abundance neighbors): CDH2 (0.88), MPP2 (0.87), SORT1 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC22 homolog B, vesicle trafficking protein. The protein encoded by this gene is a member of the SEC22 family of vesicle trafficking proteins. It seems to complex with SNARE and it is thought to play a role in the ER-Golgi protein trafficking. This protein has strong similarity to Mus musculus and Cricetulus griseus proteins.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: inflammatory bowel disease (0.285); luminal A breast carcinoma (0.271); colitis (0.238); enteritis (0.238); Crohn disease (0.233)
- **Europe PMC papers**: 1006
- **Why important**: SEC22B is a vesicle-trafficking protein involved in ER-to-Golgi transport, retrograde Golgi-to-ER transport, vesicle fusion, autophagy, and vesicle-mediated transport. It has relatively central network placement, connecting CDH2, MPP2, and SORT1, and contributes broadly to the primary ER, vesicle, organelle, and membrane annotations (GO:CC organelle subcompartment; q_global = 0.00813)(GO:CC endoplasmic reticulum membrane; q_global = 0.0132)(GO:CC endoplasmic reticulum subcompartment; q_global = 0.0132)(GO:CC cytoplasmic vesicle membrane; q_global = 0.0142)(GO:CC nuclear outer membrane-endoplasmic reticulum membrane network; q_global = 0.0142)(GO:CC vesicle membrane; q_global = 0.0154)(GO:CC organelle membrane; q_global = 0.0287). Although STRING lists no partners for it in this module and hu.MAP provides no overlapping complex, the gene has established trafficking biology and a substantial disease literature involving inflammatory bowel disease and colitis. HPA associates it with neutrophils and reports low tissue specificity.
- **Conclusion**: Established evidence supports SEC22B as a trafficking-side component that could explain how the adhesion and receptor proteins are processed or transported. Its lack of direct STRING or hu.MAP support within this module makes the proposed bridge provisional, and its immune-cell association strengthens the need to test whether cell composition contributes to the pattern.

## Module 10

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (32)**: ADD3, CCAR1, CCNH, COPB1, CPSF3, DDX24, DDX6, DYNC1H1, EIF2A, EIF3C, FLII, FLNB, GARS1, LNPK, NCKAP1, NUP107, NUP62, NUP93, LPCAT2, PDCD6IP, PFAS, RBM34, RFC2, MRPL50, SCFD1, SRP72, MARS2, THOP1, TPX2, WDR11, RP2, ZW10

### Function

No GO/KEGG term passed global correction, so the module should not be assigned a formally enriched pathway. Its genes instead suggest a coherent but broad cellular-machinery program involving RNA handling and translation, nucleocytoplasmic transport, ER and Golgi trafficking, vesicle biology, cytoskeletal organization, and cell-cycle-related processes. The strongest internal structure is formed by DDX6, EIF3C, COPB1, and neighboring RNA-processing, translation, and trafficking genes. A second recognizable unit contains NUP93, NUP107, and NUP62, which are nucleoporins and are linked by strong STRING relationships. Other edges connect cell division, microtubule, actin, mitochondrial translation, and membrane-lipid functions. Thus, the most cautious interpretation is a shared abundance program of general intracellular logistics and biosynthetic capacity, with contributions from several specialized cellular processes rather than a single narrowly defined pathway.

**Cell composition.** The module is predominantly composed of broadly expressed intracellular proteins: most genes have low tissue specificity and low immune-cell specificity in HPA. Nearly all genes have kidney protein detection, whereas the autonomic nervous system has no matching HPA tissue evidence in the supplied summary. Only a small part of the module is secreted, so this is not primarily a plasma-protein or secreted-protein module. The HPA single-cell annotations nevertheless show recurring enhancement in neutrophil progenitors, neutrophils, and several reproductive cell types, with additional isolated brain, muscle, epithelial, and hematopoietic signals. This pattern is compatible mainly with a housekeeping or ubiquitous intracellular program, but shared cell-type composition or blood-cell carryover cannot be excluded, especially for genes such as RP2, ADD3, LPCAT2, PFAS, TPX2, and DDX24. The module should therefore not be interpreted as autonomic-neural or kidney-specific solely from its tissue-pair label.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a set of established relationships rather than a uniformly connected pathway. The strongest supported subnetwork is the nucleoporin group NUP107, NUP62, and NUP93. Additional STRING-supported pairs are DDX24 with RBM34, GARS1 with MARS2, and the trafficking-related relationships COPB1 with SCFD1 and ZW10 and SCFD1 with ZW10. The hu.MAP evidence independently places ZW10 and SCFD1 together in three related trafficking complexes (hu.MAP huMAP3_06458.1), (hu.MAP huMAP3_08929.1), and (hu.MAP huMAP3_10587.1), and places NUP62 with NUP107 in a nuclear-pore-related complex (hu.MAP huMAP3_12581.1). These records show that several local edges reflect known molecular machinery. However, each hu.MAP complex contributes only a small subset of its members to the module, and STRING contains no global functional enrichment result. The observed network is therefore best viewed as a co-abundance assembly containing several known molecular substructures, not as proof that all module genes form one physical complex.

**STRING interactions (score >= 0.7)**: 8 of 496 gene pairs: COPB1–SCFD1 (0.729); COPB1–ZW10 (0.763); DDX24–RBM34 (0.921); GARS1–MARS2 (0.824); NUP107–NUP62 (0.997); NUP107–NUP93 (0.999); NUP62–NUP93 (0.999); SCFD1–ZW10 (0.892)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06458.1 (ZW10, SCFD1; 2/41); huMAP3_08929.1 (ZW10, SCFD1; 2/44); huMAP3_10587.1 (ZW10, SCFD1; 2/45); huMAP3_12581.1 (NUP62, NUP107; 2/58)

### Novelty

The cross-tissue co-abundance module may be a dataset-specific observation, but the module cannot be called a wholly new biological pathway on the supplied evidence. Several of its relationships are already represented in STRING or hu.MAP, especially the nucleoporin relationships and the ZW10-SCFD1 trafficking association. Most genes also have established cellular functions and substantial literature support. At the same time, the precise co-abundance combination across autonomic nervous system and kidney, including the links between its RNA, transport, trafficking, cytoskeletal, and cell-cycle components, is not directly established by the listed databases. A defensible novelty claim is therefore limited: the module may be a new integrative co-abundance pattern or tissue-pair-specific association, but it is not evidence for a newly discovered molecular complex or pathway.

**Hypothesis.** Hypothesis: this module reflects coordinated maintenance of intracellular proteostasis and macromolecule traffic in shared or compositionally similar cells from the two tissue groups. DDX6, EIF3C, and related RNA-processing factors could coordinate transcript turnover and translation, while NUP93, NUP107, and NUP62 regulate exchange between nucleus and cytoplasm. COPB1, SCFD1, and ZW10 could connect this program to ER-Golgi and vesicle trafficking, with RP2, ADD3, FLII, and NCKAP1 providing context-dependent cytoskeletal or membrane organization. Cell-cycle and biosynthetic genes may indicate proliferative or metabolically active subpopulations rather than a universal function of every module member. This model predicts that the co-abundance signal will weaken after careful adjustment for cell composition and will be strongest in cells experiencing high RNA turnover, protein trafficking, or proliferative demand; it requires experimental validation.

### Important genes

#### DDX6

- **Related proteins** (co-abundance neighbors): SRP72 (0.86), CPSF3 (0.85), EIF3C (0.85), ZW10 (0.85), COPB1 (0.84), LNPK (0.84), NUP62 (0.83), RP2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytoplasmic bodies; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 6. This gene encodes a member of the DEAD box protein family. The protein is an RNA helicase found in P-bodies and stress granules, and functions in translation suppression and mRNA degradation. It is required for microRNA-induced gene silencing. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: intellectual developmental disorder with impaired language and dysmorphic facies (0.650); Intellectual disability (0.555); neurodegenerative disease (0.459); lung carcinoma (0.371); Global developmental delay (0.371)
- **Europe PMC papers**: 3002
- **Why important**: DDX6 has the strongest network connectivity in the supplied subgraph and links RNA turnover and translation control to ZW10, COPB1, NUP62, SRP72, CPSF3, EIF3C, LNPK, and RP2. Its established P-body and stress-granule functions, role in mRNA decay and microRNA-mediated silencing, kidney detection, developmental and neurodegenerative disease associations, and extensive literature make it a strong integrative marker.
- **Conclusion**: Established evidence supports DDX6 as an RNA-metabolism and post-transcriptional-control component that may anchor the module's biosynthetic arm. It is plausible, but not established, that DDX6 drives the cross-tissue co-abundance pattern or couples RNA decay to trafficking and nuclear transport.

#### NUP93

- **Related proteins** (co-abundance neighbors): DDX24 (0.87), ZW10 (0.84), GARS1 (0.82); STRING partners: NUP107 (0.999), NUP62 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 occupies a bridge position between DDX24, ZW10, and GARS1 and belongs to the nucleoporin subnetwork supported by very strong STRING relationships with NUP107 and NUP62. It has established roles in nuclear pore assembly and nucleocytoplasmic transport, is detected in kidney, and has disease associations involving nephrotic syndromes and viral infection.
- **Conclusion**: Established evidence supports NUP93 as a nuclear-pore component and a biologically meaningful connection between transport and the rest of the module. Its placement in this co-abundance module is consistent with coordinated nuclear-cytoplasmic logistics, but does not establish a kidney disease mechanism.

#### COPB1

- **Related proteins** (co-abundance neighbors): EIF3C (0.90), DDX6 (0.84), ZW10 (0.83), EIF2A (0.83), PDCD6IP (0.81); STRING partners: SCFD1 (0.729), ZW10 (0.763)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus, Vesicles, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coat protein complex I subunit beta 1. This gene encodes a protein subunit of the coatomer complex associated with non-clathrin coated vesicles. The coatomer complex, also known as the coat protein complex 1, forms in the cytoplasm and is recruited to the Golgi by activated guanosine triphosphatases. Once at the Golgi membrane, the coatomer complex may assist in the movement of protein and lipid components back to the endoplasmic retic…
- **Diseases (Open Targets)**: Baralle-Macken syndrome (0.598); Alzheimer disease (0.463); Parkinson disease (0.462); neurodegenerative disease (0.462); lysosomal storage disease (0.462)
- **Europe PMC papers**: 565
- **Why important**: COPB1 is a comparatively central connector between EIF3C, DDX6, ZW10, EIF2A, and PDCD6IP. Its coatomer function in ER-Golgi and retrograde Golgi trafficking is directly relevant to the module's vesicle and protein-handling theme. The COPB1 relationships with SCFD1 and ZW10 are supported by STRING, while its disease associations include Baralle-Macken syndrome and neurodegenerative conditions.
- **Conclusion**: Established evidence supports COPB1 as a trafficking component that links the RNA and vesicle-related portions of the module. The hypothesis that altered COPB1 abundance coordinates the whole module remains unproven.

#### SCFD1

- **Related proteins** (co-abundance neighbors): RBM34 (0.88), EIF3C (0.84), PDCD6IP (0.82); STRING partners: COPB1 (0.729), ZW10 (0.892)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_06458.1, huMAP3_08929.1, huMAP3_10587.1
- **Function (MyGene.info)**: sec1 family domain containing 1. Predicted to enable syntaxin binding activity. Involved in negative regulation of autophagosome assembly; regulation of protein transport; and response to toxic substance. Located in cis-Golgi network. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); bronchial disorder (0.270); placental retention (0.240); bladder calculus (0.205); amyotrophic lateral sclerosis (0.195)
- **Europe PMC papers**: 391
- **Why important**: SCFD1 is a direct bridge to the established trafficking relationships involving COPB1 and ZW10 and is present in the related hu.MAP complexes (hu.MAP huMAP3_06458.1), (hu.MAP huMAP3_08929.1), and (hu.MAP huMAP3_10587.1). Its cis-Golgi localization, syntaxin-binding function, role in protein transport, and association with neurodegenerative disease make it a useful mechanistic representative of the membrane-trafficking arm.
- **Conclusion**: Established evidence supports SCFD1 as a vesicle and Golgi-trafficking factor with corroborating database relationships. Its centrality to the tissue-pair module is a reasonable interpretation of the network, but a causal role in shared autonomic nervous system and kidney biology is only a hypothesis.

#### RP2

- **Related proteins** (co-abundance neighbors): DDX6 (0.82), ADD3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Mid piece, Principal piece, End piece; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RP2 activator of ARL3 GTPase. The RP2 locus has been implicated as one cause of X-linked retinitis pigmentosa. The predicted gene product shows homology with human cofactor C, a protein involved in the ultimate step of beta-tubulin folding. Progressive retinal degeneration may therefore be due to the accumulation of incorrectly-folded photoreceptor or neuron-specific tubulin isoforms followed by progressive cell death [provide…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.818); retinitis pigmentosa 2 (0.698); inherited retinal dystrophy (0.570); retinitis pigmentosa 3 (0.481); Leber congenital amaurosis (0.467)
- **Europe PMC papers**: 3952
- **Why important**: RP2 links DDX6 to ADD3 and has distinctive disease relevance through retinitis pigmentosa and inherited retinal disorders. Its functions in ARL3 regulation, cilium assembly, protein folding, and post-Golgi transport provide a possible connection between intracellular trafficking and specialized cellular architecture. HPA places it in bone marrow-enriched and monocyte or neutrophil-associated cell contexts, which also makes it informative for evaluating cell-composition effects.
- **Conclusion**: Established evidence supports RP2 as a trafficking, ciliary, and protein-folding factor with strong disease relevance. Its presence may indicate a specialized cell-state contribution or a trafficking-related bridge, but the module does not establish that RP2 has a direct role in kidney or autonomic nervous system co-regulation.

## Module 11

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (5)**: MAOA, ASS1, ECHS1, PCK2, CRYZ

### Function

The module is best interpreted as a tissue-associated metabolic program rather than as a conclusively defined pathway. Its genes span mitochondrial and cytosolic metabolism: MAOA supports oxidative deamination of biogenic amines; PCK2 supports mitochondrial oxaloacetate-to-phosphoenolpyruvate conversion and gluconeogenic responses; ECHS1 supports mitochondrial fatty-acid and branched-chain amino-acid catabolism; ASS1 supports arginine biosynthesis and the urea cycle; and CRYZ provides NADPH-dependent quinone-reductase activity. The co-abundance graph is connected through MAOA and CRYZ, with MAOA linking PCK2 and ECHS1 and CRYZ linking ASS1. However, no GO or KEGG term passed global correction, so these annotations support biological interpretation but do not establish significant pathway enrichment. The absence of a globally significant term does not invalidate the module.

**Cell composition.** The module is composed entirely of intracellular enzymes, with no secreted genes. HPA evidence indicates tissue-enhanced or group-enriched expression concentrated especially in liver, kidney, and intestine, and single-cell enrichment in hepatocytes, enterocytes, proximal-tubule-related cells, and other epithelial or metabolically specialized cell types. All module proteins were detected by kidney immunohistochemistry, whereas no matching HPA tissue was available for autonomic nervous system. Most genes have low immune-cell specificity, one is not detected in immune cells, and ASS1 is immune-cell enriched in plasmacytoid dendritic cells. Thus, the module does not resemble a plasma-protein or broad blood-cell contamination signature; it more plausibly reflects shared epithelial or metabolically active cell populations, particularly kidney-related cells, although sample cellular composition remains a possible contributor.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction or supplementary STRING enrichment was reported for the module. Therefore, STRING does not independently support a known physical interaction network among these genes. hu.MAP provides a more limited structural connection: CRYZ and PCK2 co-occur in several complexes (hu.MAP huMAP3_07052.1), (hu.MAP huMAP3_00213.1), and (hu.MAP huMAP3_10334.1), including a recurring group that also contains IARS2, with a broader mitochondrial/metabolic complex represented by (hu.MAP huMAP3_13468.1). These complexes support a possible shared mitochondrial or metabolic context for CRYZ and PCK2, but they do not demonstrate that all module members form one complex. The remaining genes have no reported hu.MAP membership in the supplied evidence.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07052.1 (CRYZ, PCK2; 2/3); huMAP3_00213.1 (CRYZ, PCK2; 2/4); huMAP3_10334.1 (CRYZ, PCK2; 2/6); huMAP3_13468.1 (CRYZ, PCK2; 2/99)

### Novelty

This appears to be a potentially novel co-abundance association rather than a newly established molecular complex or pathway. The lack of STRING support and the partial hu.MAP overlap mean that the complete five-gene combination is not already explained by a documented interaction assembly in the supplied databases. Nevertheless, absence from STRING or hu.MAP alone cannot prove novelty: the genes have well-established individual metabolic functions, and CRYZ-PCK2 has recurring hu.MAP support. The strongest novelty claim is therefore that their coordinated abundance across autonomic nervous system and kidney is a new or insufficiently characterized tissue-pair observation, requiring replication and independent validation.

**Hypothesis.** Hypothesis: the module reflects coordinated metabolic adaptation in shared metabolically active epithelial or parenchymal cell populations across kidney and autonomic-nervous-system-associated samples. A possible mechanism is coupling mitochondrial fuel handling and redox metabolism through PCK2 and ECHS1, quinone reduction through CRYZ, nitrogen and arginine handling through ASS1, and local biogenic-amine degradation through MAOA. In kidney, this could represent a metabolic state associated with tubular or related specialized cells. The hypothesis is consistent with the HPA tissue and cell-type patterns and with the partial CRYZ-PCK2 complex evidence, but it is not established by GO/KEGG enrichment or STRING interactions and should be tested using cell-resolved proteomics, metabolic measurements, and replication in independent cohorts.

### Important genes

#### MAOA

- **Related proteins** (co-abundance neighbors): PCK2 (0.92), CRYZ (0.91), ECHS1 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: monoamine oxidase A. This gene is one of two neighboring gene family members that encode mitochondrial enzymes which catalyze the oxidative deamination of amines, such as dopamine, norepinephrine, and serotonin. Mutation of this gene results in Brunner syndrome. This gene has also been associated with a variety of other psychiatric disorders, including antisocial behavior. Alternatively spliced transcript variants enc…
- **Diseases (Open Targets)**: Brunner syndrome (0.788); major depressive disorder (0.613); depressive disorder (0.544); hypertensive disorder (0.464); hereditary disease (0.451)
- **Europe PMC papers**: 7415
- **Why important**: MAOA has the strongest network position, linking PCK2, CRYZ, and ECHS1. It is a mitochondrial enzyme that catabolizes dopamine, norepinephrine, serotonin, and other amines, giving it a plausible connection to autonomic biology while also linking the module to mitochondrial metabolism. It has extensive literature and disease associations including Brunner syndrome and mood-related disorders.
- **Conclusion**: Established evidence supports MAOA as the principal network bridge and as an amine-catabolic mitochondrial enzyme. Its position makes it a useful candidate for coordinating the module, but the supplied data do not establish that MAOA regulates the other genes. Any autonomic-neural interpretation beyond its known enzymatic role remains a hypothesis.

#### CRYZ

- **Related proteins** (co-abundance neighbors): MAOA (0.91), ASS1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_07052.1, huMAP3_00213.1, huMAP3_10334.1, huMAP3_13468.1
- **Function (MyGene.info)**: crystallin zeta. Crystallins are separated into two classes: taxon-specific, or enzyme, and ubiquitous. The latter class constitutes the major proteins of vertebrate eye lens and maintains the transparency and refractive index of the lens. The former class is also called phylogenetically-restricted crystallins. This gene encodes a taxon-specific crystallin protein which has NADPH-dependent quinone reductase activi…
- **Diseases (Open Targets)**: response to paracetamol (0.249); amyotrophic lateral sclerosis (0.220); adolescent idiopathic scoliosis (0.205); ovarian neoplasm (0.170); Wheezing (0.125)
- **Europe PMC papers**: 864
- **Why important**: CRYZ is a network bridge between MAOA and ASS1 and is the only module member recurring with PCK2 across the supplied hu.MAP complexes (hu.MAP huMAP3_07052.1), (hu.MAP huMAP3_00213.1), (hu.MAP huMAP3_10334.1), and (hu.MAP huMAP3_13468.1). It encodes a cytosolic NADPH-dependent quinone reductase and is enriched in kidney and liver, with hepatocyte and epididymal-cell signals. Its placement connects redox or xenobiotic handling with nitrogen metabolism.
- **Conclusion**: Established evidence supports CRYZ as a kidney- and liver-associated quinone reductase and as the module's main non-MAOA connector to ASS1 and PCK2. The hu.MAP overlap supports shared complex context with PCK2, but does not prove a direct functional partnership or a role in the complete module.

#### PCK2

- **Related proteins** (co-abundance neighbors): MAOA (0.92); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_07052.1, huMAP3_00213.1, huMAP3_10334.1, huMAP3_13468.1
- **Function (MyGene.info)**: phosphoenolpyruvate carboxykinase 2, mitochondrial. This gene encodes a mitochondrial enzyme that catalyzes the conversion of oxaloacetate to phosphoenolpyruvate in the presence of guanosine triphosphate (GTP). A cytosolic form of this protein is encoded by a different gene and is the key enzyme of gluconeogenesis in the liver. Alternatively spliced transcript variants have been described. [provided by RefSeq, Apr 2014].
- **Diseases (Open Targets)**: phosphoenolpyruvate carboxykinase deficiency, mitochondrial (0.511); phosphoenolpyruvate carboxykinase deficiency (0.443); neuropathy (0.187); Gait disturbance (0.185); retinitis pigmentosa (0.148)
- **Europe PMC papers**: 2644
- **Why important**: PCK2 is connected to MAOA and repeatedly co-occurs with CRYZ in hu.MAP complexes (hu.MAP huMAP3_07052.1), (hu.MAP huMAP3_00213.1), (hu.MAP huMAP3_10334.1), and (hu.MAP huMAP3_13468.1). It is a mitochondrial enzyme involved in oxaloacetate metabolism and gluconeogenesis, with expression enriched in intestine, kidney, and liver and in hepatocyte- and enterocyte-related cell types. Its disease associations include mitochondrial PCK2 deficiency.
- **Conclusion**: Established evidence supports PCK2 as a mitochondrial metabolic enzyme and as the strongest complex-supported partner of CRYZ in this module. Its module association is compatible with coordinated carbon metabolism, but the data do not show that PCK2 drives the co-abundance pattern or that the module performs gluconeogenesis as a unified pathway.

#### ECHS1

- **Related proteins** (co-abundance neighbors): MAOA (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: enoyl-CoA hydratase, short chain 1. The protein encoded by this gene functions in the second step of the mitochondrial fatty acid beta-oxidation pathway. It catalyzes the hydration of 2-trans-enoyl-coenzyme A (CoA) intermediates to L-3-hydroxyacyl-CoAs. The gene product is a member of the hydratase/isomerase superfamily. It localizes to the mitochondrial matrix. Transcript variants utilizing alternative transcription initiation site…
- **Diseases (Open Targets)**: mitochondrial short-chain Enoyl-Coa hydratase 1 deficiency (0.848); Leigh syndrome (0.759); hereditary disease (0.509); neurodegenerative disease (0.371); colorectal carcinoma (0.095)
- **Europe PMC papers**: 1714
- **Why important**: ECHS1 is directly connected to the high-centrality MAOA node and contributes a distinct mitochondrial fuel-oxidation function. It catalyzes a step in fatty-acid beta-oxidation and also participates in branched-chain amino-acid and lysine catabolism. It is liver-enriched, detected in kidney, and has substantial disease literature including ECHS1 deficiency and Leigh syndrome.
- **Conclusion**: Established evidence supports ECHS1 as a mitochondrial matrix enzyme in oxidative fuel catabolism and as a biologically important disease gene. Its single network connection makes it a peripheral module member rather than a structural hub. Its inclusion supports a broad mitochondrial-metabolic interpretation, but not a specific shared substrate pathway.

#### ASS1

- **Related proteins** (co-abundance neighbors): CRYZ (0.85); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: argininosuccinate synthase 1. The protein encoded by this gene catalyzes the penultimate step of the arginine biosynthetic pathway. There are approximately 10 to 14 copies of this gene including the pseudogenes scattered across the human genome, among which the one located on chromosome 9 appears to be the only functional gene for argininosuccinate synthetase. Mutations in the chromosome 9 copy of this gene cause citrullinemia…
- **Diseases (Open Targets)**: citrullinemia type I (0.857); citrullinemia (0.749); hereditary disease (0.472); acute neonatal citrullinemia type I (0.372); Intellectual disability (0.371)
- **Europe PMC papers**: 3704
- **Why important**: ASS1 is connected to CRYZ and contributes a complementary nitrogen-handling function through the urea cycle and arginine biosynthesis. It is enriched in kidney and liver and in several epithelial or hepatocyte-related cell types, while also showing immune-cell enrichment in plasmacytoid dendritic cells. It has extensive literature and a strong association with citrullinemia type one.
- **Conclusion**: Established evidence supports ASS1 as a kidney- and liver-associated urea-cycle enzyme with major clinical relevance in citrullinemia. Its CRYZ connection suggests possible coupling of redox and nitrogen metabolism, but this is a mechanistic hypothesis rather than a demonstrated interaction. The immune-cell signal also warrants attention when interpreting heterogeneous samples.

## Module 12

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (45)**: AP3D1, DBNL, EDC4, EFHD2, EPS15L1, EWSR1, FAM120A, FKBP4, GEMIN4, GNE, GNL1, HDAC2, HDGFL2, HMGN1, HNRNPF, HSPH1, EIF6, IMPDH2, KIFBP, LIMA1, LRRFIP2, METAP2, NAMPT, NDE1, NPM3, PAPSS1, PDLIM1, PPM1G, PSMC4, SAE1, SEC23A, SNX6, CTTN, SRP54, AARS1, KARS1, RARS1, TCEA1, CCT3, TPD52L2, TSG101, SNRNP200, UMPS, XPNPEP1, XRN2

### Function

The module does not have a GO or KEGG term that passed global correction, so its function should be inferred cautiously rather than assigned from enrichment. Its genes collectively point to a broadly expressed intracellular maintenance program involving protein synthesis and folding, RNA processing and transcription, nucleotide metabolism, proteostasis, vesicle trafficking, and cytoskeletal organization. The co-abundance structure is therefore more consistent with a general cellular state or shared cell-composition signal than with a narrowly specialized autonomic-nervous-system or kidney pathway. The strongest biological themes are supported by individual gene annotations and by the STRING links among aminoacyl-tRNA synthetases, translation-associated proteins, transcriptional machinery, and RNA-processing factors. These observations support a hypothesis of coordinated biosynthetic, proteostatic, and trafficking activity, but they do not establish a single pathway.

**Cell composition.** The module is dominated by broadly expressed, intracellular proteins: HPA classifies nearly all genes as having low tissue specificity, and most have low immune-cell specificity. This argues against interpreting the module as a tissue-exclusive kidney or autonomic-nervous-system signature. The STRING tissue signals for blood, hematopoietic system, leukocyte, lymphocyte, and related compartments (STRING TISSUES Blood; within-query FDR = 0.0014), (STRING TISSUES Hematopoietic system; within-query FDR = 0.0014), (STRING TISSUES Leukocyte; within-query FDR = 0.0232), (STRING TISSUES Lymphocyte; within-query FDR = 0.0235), (STRING TISSUES T-lymphocyte; within-query FDR = 0.0235), (STRING TISSUES Lymphoid tissue; within-query FDR = 0.0258) are compatible with shared blood or immune-cell content, but they are supplementary evidence and do not establish that the module is blood-derived. HPA identifies only a small secreted component, including NAMPT, so this is not primarily a plasma or secreted-protein module. Several genes show cell-type-enhanced or immune-cell-associated expression, including neutrophil-associated signals, but the overall HPA profile remains broadly expressed. Kidney protein detection is widespread among the module genes, whereas matching autonomic-nervous-system protein data are unavailable; this asymmetry limits tissue-specific interpretation. The shared module may therefore reflect common intracellular programs, shared cell types, or sample-composition effects rather than a specialized cross-tissue mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a small set of high-confidence relationships, concentrated around the aminoacyl-tRNA synthetase pair AARS1–KARS1 and the related RARS1–KARS1 and AARS1–RARS1 links, as well as EIF6–GNL1, EIF6–HMGN1, EIF6–SRP54, GNL1–PAPSS1, HMGN1–SRP54, and HMGN1–TCEA1. These relationships indicate that part of the co-abundance module overlaps known translation, RNA, and nucleolar or transcription-associated biology, but the sparse physical-interaction support means the entire co-abundance module is not a single established protein complex. hu.MAP supplies additional partial complex support: AARS1 and EFHD2 recur with cytoskeletal or actin-associated partners across several complexes (hu.MAP huMAP3_14442.1), (hu.MAP huMAP3_03533.1), (hu.MAP huMAP3_07456.1), (hu.MAP huMAP3_10281.1); AARS1 and TCEA1 occur in transcription- or RNA-associated complexes (hu.MAP huMAP3_09323.1), (hu.MAP huMAP3_10302.1); RARS1 and KARS1 occur in aminoacyl-tRNA synthetase complexes (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1); CTTN and EFHD2 occur in cytoskeletal complexes (hu.MAP huMAP3_06395.1), (hu.MAP huMAP3_10673.1); HMGN1 and TCEA1 occur together in a larger nuclear complex (hu.MAP huMAP3_14982.1); and UMPS with NAMPT, SNRNP200 with GEMIN4, LIMA1 with LRRFIP2, and SEC23A with EPS15L1 provide additional partial associations (hu.MAP huMAP3_12841.1), (hu.MAP huMAP3_08980.1), (hu.MAP huMAP3_09542.1), (hu.MAP huMAP3_12394.1). Most hu.MAP overlaps involve only a subset of module members, so they support modular substructure rather than a unified molecular complex.

**STRING interactions (score >= 0.7)**: 9 of 990 gene pairs: AARS1–KARS1 (0.992); AARS1–RARS1 (0.85); EIF6–GNL1 (0.875); EIF6–HMGN1 (0.8); EIF6–SRP54 (0.702); GNL1–PAPSS1 (0.783); HMGN1–SRP54 (0.707); HMGN1–TCEA1 (0.975); KARS1–RARS1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Blood (FDR = 0.0014, 23 genes); TISSUES Hematopoietic system (FDR = 0.0014, 27 genes); TISSUES Embryonic structure (FDR = 0.0016, 26 genes); TISSUES Placenta (FDR = 0.0076, 17 genes); Keyword Acetylation (FDR = 0.0222, 37 genes); TISSUES Leukocyte (FDR = 0.0232, 13 genes); TISSUES Lymphocyte (FDR = 0.0235, 12 genes); TISSUES T-lymphocyte (FDR = 0.0235, 7 genes); TISSUES Lymphoid tissue (FDR = 0.0258, 16 genes); TISSUES Digestive gland (FDR = 0.0266, 28 genes); TISSUES Viscus (FDR = 0.0267, 35 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (PDLIM1, AARS1, EFHD2, XPNPEP1; 4/57); huMAP3_03533.1 (AARS1, EFHD2; 2/4); huMAP3_09323.1 (TCEA1, AARS1; 2/4); huMAP3_07456.1 (AARS1, EFHD2; 2/5); huMAP3_06395.1 (CTTN, EFHD2; 2/8); huMAP3_10281.1 (AARS1, EFHD2; 2/9); huMAP3_10302.1 (TCEA1, AARS1; 2/9); huMAP3_12841.1 (UMPS, NAMPT; 2/10); huMAP3_10673.1 (CTTN, EFHD2; 2/14); huMAP3_02637.1 (RARS1, KARS1; 2/14); huMAP3_13688.1 (RARS1, KARS1; 2/14); huMAP3_14982.1 (HMGN1, TCEA1; 2/28); huMAP3_09542.1 (LIMA1, LRRFIP2; 2/38); huMAP3_08980.1 (SNRNP200, GEMIN4; 2/97); huMAP3_12394.1 (SEC23A, EPS15L1; 2/98)

### Novelty

The module should be regarded as a potentially novel cross-tissue co-abundance pattern, not as a newly discovered molecular complex or pathway. Its novelty is supported by the fact that the module-level GO and KEGG analysis yields no globally significant term and that STRING and hu.MAP explain only portions of the network through previously known relationships. However, absence of a complete representation in STRING or hu.MAP cannot prove biological novelty, because those resources emphasize experimentally reported or computationally supported physical and functional relationships rather than tissue-pair co-abundance patterns. The defensible claim is that the shared autonomic-nervous-system and kidney co-abundance organization appears not to map cleanly onto an established canonical pathway or complex, while its component biology is largely familiar and housekeeping-like. Independent replication, adjustment for cell composition, and comparison with existing tissue coexpression resources would be needed before calling it a new biological mechanism.

**Hypothesis.** Hypothesis: variation in the abundance of a broadly expressed intracellular maintenance program coordinates translation capacity, RNA maturation and turnover, proteostasis, nucleotide supply, membrane trafficking, and cytoskeletal organization in both autonomic-nervous-system and kidney samples. A shared abundance state could arise from common metabolic or stress conditions, similar cellular composition, or blood-cell contribution, with FAM120A and associated trafficking or RNA-linked genes acting as co-abundance hubs rather than as a single causal driver. This hypothesis predicts that the module will weaken after adjustment for cell composition and general expression intensity, but that residual activity may track cellular stress, biosynthetic demand, or tissue injury. It is not established by the current enrichment or interaction evidence.

### Important genes

#### FAM120A

- **Related proteins** (co-abundance neighbors): RARS1 (0.91), AP3D1 (0.90), XRN2 (0.88), PAPSS1 (0.87), EPS15L1 (0.87), DBNL (0.85), PSMC4 (0.85), IMPDH2 (0.85), PDLIM1 (0.82), TCEA1 (0.82), TSG101 (0.82), KARS1 (0.81), LIMA1 (0.81), CTTN (0.81), PPM1G (0.81), NAMPT (0.80), EFHD2 (0.80), SNX6 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: family with sequence similarity 120 member A. Enables RNA binding activity. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.325); major depressive disorder (0.304); neurodegenerative disease (0.273); neurotic disorder (0.216); irritable bowel syndrome (0.214)
- **Europe PMC papers**: 467
- **Why important**: FAM120A has the strongest network position in the supplied module and connects genes spanning RNA-associated, trafficking, metabolic, and cytoskeletal neighborhoods. It is included in several supplementary STRING tissue terms (STRING TISSUES Embryonic structure; within-query FDR = 0.0016), (STRING TISSUES Placenta; within-query FDR = 0.0076), (STRING Keyword Acetylation; within-query FDR = 0.0222), (STRING TISSUES Digestive gland; within-query FDR = 0.0266), while having no listed STRING partner or hu.MAP complex assignment. Its annotated RNA-binding activity, reported roles in RNA splicing and lipid biosynthesis, and possible regulation of NLRP3 inflammasome assembly make it a plausible integrator of the module's diverse signals. Its disease and literature associations are broader than those of many peripheral genes, supporting prioritization while also emphasizing that it is not a proven module-specific regulator.
- **Conclusion**: Established evidence supports FAM120A as a central co-abundance hub with broad intracellular annotation and kidney detection. It is plausible, but unproven, that FAM120A helps couple RNA handling, metabolism, and inflammatory or trafficking states in this module.

#### AARS1

- **Related proteins** (co-abundance neighbors): GNL1 (0.90), KARS1 (0.85), SNRNP200 (0.83), AP3D1 (0.83), XPNPEP1 (0.83), HSPH1 (0.81); STRING partners: KARS1 (0.992), RARS1 (0.85)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_14442.1, huMAP3_03533.1, huMAP3_09323.1, huMAP3_07456.1, huMAP3_10281.1, huMAP3_10302.1
- **Function (MyGene.info)**: alanyl-tRNA synthetase 1. The human alanyl-tRNA synthetase (AARS) belongs to a family of tRNA synthases, of the class II enzymes.  Class II tRNA synthases evolved early in evolution and are highly conserved. This is reflected by the fact that 498 of the 968-residue polypeptide human AARS shares 41% identity witht the E.coli protein.  tRNA synthases are the enzymes that interpret the RNA code and attach specific aminoacids …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2N (0.762); developmental and epileptic encephalopathy, 29 (0.747); undetermined early-onset epileptic encephalopathy (0.678); trichothiodystrophy 8, nonphotosensitive (0.568); Charcot-Marie-Tooth disease type 2 (0.566)
- **Europe PMC papers**: 672
- **Why important**: AARS1 occupies an important bridge position in the network and has direct STRING relationships with KARS1 and RARS1. It appears in multiple hu.MAP complexes, including complexes shared with EFHD2 and TCEA1 (hu.MAP huMAP3_14442.1), (hu.MAP huMAP3_03533.1), (hu.MAP huMAP3_09323.1), (hu.MAP huMAP3_07456.1), (hu.MAP huMAP3_10281.1), (hu.MAP huMAP3_10302.1). Its established role in alanyl-tRNA aminoacylation provides a concrete translation-related anchor, while its disease associations include axonal Charcot-Marie-Tooth disease and developmental epileptic encephalopathy, relevant to the autonomic-nervous-system context. Its literature support is substantial, but the module data do not show that AARS1 drives the co-abundance pattern.
- **Conclusion**: Established evidence identifies AARS1 as a translation enzyme and a connector between known aminoacylation and partial cytoskeletal or transcription-associated complexes. Its participation supports a biosynthetic interpretation, whereas any role in coordinating the shared tissue module remains a hypothesis.

#### KARS1

- **Related proteins** (co-abundance neighbors): XPNPEP1 (0.89), AARS1 (0.85), GNL1 (0.84), EDC4 (0.83), SNRNP200 (0.83), PSMC4 (0.82), AP3D1 (0.82), SRP54 (0.82), FAM120A (0.81), TPD52L2 (0.81); STRING partners: AARS1 (0.992), RARS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: lysyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. Lysyl-tRNA synthetase is a homodimer localized to the cytoplasm which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Alternatively spliced transcript variants encoding different…
- **Diseases (Open Targets)**: leukoencephalopathy, progressive, infantile-onset, with or without deafness (0.753); deafness, congenital, and adult-onset progressive leukoencephalopathy (0.714); autosomal recessive nonsyndromic hearing loss 89 (0.685); Charcot-Marie-Tooth disease recessive intermediate B (0.670); deafness (0.534)
- **Europe PMC papers**: 232
- **Why important**: KARS1 is a network connector linked to AARS1 and RARS1 by high-confidence STRING evidence and appears in aminoacyl-tRNA synthetase complexes (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1). Its lysyl-tRNA aminoacylation function gives the module a second independent translation anchor. The gene has established associations with progressive leukodystrophy, deafness, and Charcot-Marie-Tooth disease, making it biologically relevant to neural and systemic phenotypes. HPA shows broad tissue expression with cell-type enhancement in cardiomyocytes and germ-cell populations, so it is not a tissue-specific marker.
- **Conclusion**: Established evidence supports KARS1 as a core translation enzyme and as part of a known synthetase interaction neighborhood. Its co-abundance with other translation-related genes is consistent with shared biosynthetic demand, but does not demonstrate a disease mechanism in either tissue.

#### AP3D1

- **Related proteins** (co-abundance neighbors): FAM120A (0.90), IMPDH2 (0.87), SNRNP200 (0.86), EWSR1 (0.86), GNL1 (0.86), METAP2 (0.83), AARS1 (0.83), CCT3 (0.82), KARS1 (0.82), PSMC4 (0.82), RARS1 (0.82), FKBP4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor related protein complex 3 subunit delta 1. The protein encoded by this gene is a subunit of the AP3 adaptor-like complex, which is not clathrin-associated, but is associated with the golgi region, as well as more peripheral structures. The AP-3 complex facilitates the budding of vesicles from the golgi membrane, and may be directly involved in trafficking to lysosomes. This subunit is implicated in intracellular biogenesis and trafficking …
- **Diseases (Open Targets)**: Hermansky-Pudlak syndrome 10 (0.584); Hermansky-Pudlak syndrome 2 (0.455); Hermansky-Pudlak syndrome (0.432); Alzheimer disease (0.421); lysosomal storage disease (0.417)
- **Europe PMC papers**: 637
- **Why important**: AP3D1 has a high network position and connects FAM120A, IMPDH2, SNRNP200, EWSR1, GNL1, METAP2, AARS1, and CCT3 in the co-abundance graph. Its established function in the AP-3 adaptor complex links Golgi-derived vesicle budding with lysosomal, pigment-granule, platelet-dense-granule, and neurotransmitter-vesicle trafficking. Its disease associations include Hermansky-Pudlak syndromes and lysosomal storage disease, which are relevant to vesicle biology. It has broad HPA expression and no listed STRING partner or hu.MAP complex in this fact sheet, so its network centrality is co-abundance-based rather than confirmed physical connectivity.
- **Conclusion**: Established evidence supports AP3D1 as a vesicle-trafficking and lysosomal-biogenesis component with disease relevance. It may connect the module to intracellular trafficking, but the current data do not establish that this trafficking function explains the cross-tissue conservation.

#### SRP54

- **Related proteins** (co-abundance neighbors): PSMC4 (0.89), EDC4 (0.88), EWSR1 (0.82), GNL1 (0.82), KARS1 (0.82), IMPDH2 (0.81); STRING partners: EIF6 (0.702), HMGN1 (0.707)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal recognition particle 54. Enables several functions, including 7S RNA binding activity; endoplasmic reticulum signal peptide binding activity; and guanyl ribonucleotide binding activity. Contributes to GTPase activity. Involved in granulocyte differentiation and protein targeting to ER. Located in cytosol and nucleus. Part of signal recognition particle, endoplasmic reticulum targeting. Implicated in severe congenital neut…
- **Diseases (Open Targets)**: neutropenia, severe congenital, 8, autosomal dominant (0.758); neurodegenerative disease (0.536); Shwachman-Diamond syndrome 1 (0.453); Abnormality of the skeletal system (0.380); hereditary disease (0.375)
- **Europe PMC papers**: 1519
- **Why important**: SRP54 links several central module genes, including PSMC4, EDC4, EWSR1, GNL1, KARS1, and IMPDH2. STRING supports relationships with EIF6 and HMGN1, and its annotation directly connects it to signal-sequence recognition, cotranslational targeting to the endoplasmic reticulum, granulocyte differentiation, and neutrophil biology. Its established association with severe congenital neutropenia is especially relevant to the supplementary blood and leukocyte signals (STRING TISSUES Blood; within-query FDR = 0.0014), (STRING TISSUES Hematopoietic system; within-query FDR = 0.0014), (STRING TISSUES Leukocyte; within-query FDR = 0.0232), (STRING TISSUES Lymphocyte; within-query FDR = 0.0235), (STRING TISSUES T-lymphocyte; within-query FDR = 0.0235), (STRING TISSUES Lymphoid tissue; within-query FDR = 0.0258). HPA reports broad tissue specificity with late-spermatid enhancement, so the gene is not specific to either target tissue.
- **Conclusion**: Established evidence supports SRP54 as a protein-targeting factor with granulocyte and neutrophil relevance. It strengthens a hypothesis involving biosynthetic load and possible cell-composition effects, but cannot distinguish intrinsic tissue biology from blood-cell contribution.

#### HMGN1

- **Related proteins** (co-abundance neighbors): LIMA1 (0.90), LRRFIP2 (0.81); STRING partners: EIF6 (0.8), SRP54 (0.707), TCEA1 (0.975)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_14982.1
- **Function (MyGene.info)**: high mobility group nucleosome binding domain 1. The protein encoded by this gene binds nucleosomal DNA and is associated with transcriptionally active chromatin. Along with a similar protein, HMG17, the encoded protein may help maintain an open chromatin configuration around transcribable genes. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: osteoarthritis, hip (0.251); osteoarthritis, knee (0.243); health study participation (0.198); total joint arthroplasty (0.120); neoplasm (0.107)
- **Europe PMC papers**: 1112
- **Why important**: HMGN1 has strong STRING relationships with TCEA1, EIF6, and SRP54 and is represented in a hu.MAP complex with TCEA1 (hu.MAP huMAP3_14982.1). Its established function in nucleosome binding and active chromatin organization connects the module to transcriptional capacity, while its co-abundance links to LIMA1 and LRRFIP2 provide a possible bridge between nuclear regulation and membrane or actin-associated biology. HPA shows broad tissue expression with enhancement in extravillous trophoblasts and megakaryocytes, and the gene has a substantial literature base and disease associations involving joint disease and neoplasia.
- **Conclusion**: Established evidence supports HMGN1 as a chromatin-associated transcriptional regulator and as part of a known interaction neighborhood with TCEA1. Its position supports coordinated transcriptional state as a module component, while a causal role in the shared tissue pattern remains untested.

## Module 13

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (8)**: ARHGEF2, DNAAF5, GIGYF2, HMGCS1, IGF2BP1, LAS1L, WDR36, YTHDF2

### Function

No GO/KEGG term passed global correction; therefore, the module does not support a statistically established pathway-level function from enrichment. Its genes instead suggest a mixed cellular program involving post-transcriptional RNA regulation, translational control, cytoskeletal and small-GTPase signaling, ribosome biogenesis, axonemal cilia assembly, and mevalonate or cholesterol-related metabolism. The co-abundance structure may therefore reflect a shared cellular state rather than one coherent biochemical pathway. IGF2BP1 and YTHDF2 provide a plausible RNA-regulatory axis, while ARHGEF2, WDR36, LAS1L, DNAAF5, and HMGCS1 represent distinct functional branches. These interpretations are functional annotations of individual genes, not evidence of significant module enrichment.

**Cell composition.** This is not a plasma-protein or secreted-protein module: none of the genes is annotated as secreted. It also does not look like a blood-cell module, because the HPA summary reports low immune-cell specificity for most genes and no frequent enriched blood-cell category. The module is more consistent with broadly distributed intracellular proteins, although most genes show cell-type enhancement in HPA. The enhanced cell types are heterogeneous and include reproductive, immune, neural, and ciliated-cell populations rather than a single shared cell type. Kidney protein detection is present for most genes, whereas the autonomic-nervous-system comparison has no matching HPA tissue. Thus, sample cellular composition or a shared intracellular state could contribute to the cross-tissue signal, but a blood contamination explanation is not supported by the supplied HPA evidence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship among module members is the documented IGF2BP1–YTHDF2 interaction. The remaining co-abundance relationships are not supported by high-confidence within-module STRING links in the fact sheet, and no STRING functional enrichment was reported. No hu.MAP complex contains multiple module members. Accordingly, the network should not be interpreted as a known protein complex. The STRING-supported RNA-related pair gives one mechanistic anchor, whereas the other edges may represent co-expression, indirect regulation, shared cell-state dependence, or context-specific biology rather than direct physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 28 gene pairs: IGF2BP1–YTHDF2 (0.872)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a new tissue-pair-specific co-abundance observation, but the supplied evidence does not establish a new molecular complex or a new pathway. Its novelty is supported only in the limited sense that this particular cross-tissue network configuration is not represented by a corresponding hu.MAP multi-member complex and has only one documented high-confidence STRING relationship. Absence from those resources alone cannot prove novelty, because databases are incomplete and co-abundance edges need not be physical interactions. The lack of globally significant GO/KEGG enrichment also prevents a strong claim that the module represents a previously unrecognized coherent biological process. Independent replication, preservation analysis, perturbation experiments, and comparison with existing tissue co-expression resources would be needed to establish novelty.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular RNA and growth-state program in autonomic-nervous-system and kidney samples. IGF2BP1 and YTHDF2 could jointly mark altered RNA handling, translation, and messenger-RNA stability, with GIGYF2 providing a related translational-control context. ARHGEF2 could connect this state to Rho-dependent cytoskeletal signaling, while WDR36 and LAS1L could indicate accompanying ribosome-biogenesis demand. DNAAF5 and HMGCS1 may represent context-dependent ciliary and lipid or mevalonate features rather than components of one direct pathway. This model is explicitly hypothetical: the enrichment analysis does not support it as a globally significant module function, and the network does not demonstrate direct physical assembly of all members.

### Important genes

#### IGF2BP1

- **Related proteins** (co-abundance neighbors): WDR36 (0.88), ARHGEF2 (0.87), DNAAF5 (0.84), HMGCS1 (0.80); STRING partners: YTHDF2 (0.872)
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor 2 mRNA binding protein 1. This gene encodes a member of the insulin-like growth factor 2 mRNA-binding protein family. The protein encoded by this gene contains four K homology domains and two RNA recognition motifs. It functions by binding to the mRNAs of certain genes, including insulin-like growth factor 2, beta-actin and beta-transducin repeat-containing protein, and regulating their translation. Two transcript variants…
- **Diseases (Open Targets)**: neurodegenerative disease (0.568); coronary artery disorder (0.407); type 2 diabetes mellitus (0.403); diabetes mellitus (0.401); hypertensive disorder (0.390)
- **Europe PMC papers**: 6279
- **Why important**: IGF2BP1 is the most connected module member and links several otherwise distinct branches, including ARHGEF2, WDR36, DNAAF5, and HMGCS1. It encodes an RNA-binding protein with KH domains and RNA-recognition motifs and is annotated for RNA localization, messenger-RNA stability, translation control, stress responses, and nervous-system development. It has substantial literature and disease-association coverage, and HPA reports kidney protein detection together with tissue and cell-type enhancement in reproductive and trophoblast-related populations.
- **Conclusion**: Established evidence supports IGF2BP1 as the strongest network hub and as an RNA-regulatory protein with broad disease relevance. Its centrality makes it a leading candidate for organizing the observed co-abundance pattern, but the module data do not prove that it physically regulates the other module members or that it explains the tissue-pair signal.

#### YTHDF2

- **Related proteins** (co-abundance neighbors): GIGYF2 (0.82), ARHGEF2 (0.80); STRING partners: IGF2BP1 (0.872)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: YTH N6-methyladenosine RNA binding protein F2. This gene encodes a member of the YTH (YT521-B homology) superfamily containing YTH domain. The YTH domain is typical for the eukaryotes and is particularly abundant in plants. The YTH domain is usually located in the middle of the protein sequence and may function in binding to RNA. In addition to a YTH domain, this protein has a proline rich region which may be involved in signal transduction. A…
- **Diseases (Open Targets)**: neurodegenerative disease (0.448); type 2 diabetes mellitus (0.157); neoplasm (0.118); hepatocellular carcinoma (0.117); gastric cancer (0.111)
- **Europe PMC papers**: 7075
- **Why important**: YTHDF2 is part of the only documented high-confidence STRING interaction within the module, pairing with IGF2BP1. It is an RNA-binding protein annotated for messenger-RNA catabolism, translational regulation, and post-transcriptional control. It also has extensive literature and disease-association coverage, and its HPA profile includes kidney detection and cell-type enhancement in syncytiotrophoblasts.
- **Conclusion**: Established evidence supports YTHDF2 as an important RNA-turnover and translation regulator and supports its physical association with IGF2BP1. A coordinated IGF2BP1–YTHDF2 RNA-regulatory state is a plausible interpretation, but the module does not establish that this pair drives the co-abundance of the remaining genes.

#### ARHGEF2

- **Related proteins** (co-abundance neighbors): IGF2BP1 (0.87), WDR36 (0.83), YTHDF2 (0.80), LAS1L (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho/Rac guanine nucleotide exchange factor 2. Rho GTPases play a fundamental role in numerous cellular processes that are initiated by extracellular stimuli that work through G protein coupled receptors. The encoded protein may form complex with G proteins and stimulate rho-dependent signals. Alternatively spliced transcript variants encoding different isoforms have been identified.[provided by RefSeq, Jun 2009].
- **Diseases (Open Targets)**: neurodevelopmental disorder with midbrain and hindbrain malformations (0.525); microcephaly (0.140); Abnormality of the skeletal system (0.127); myoepithelial tumor (0.111); Parkinson disease (0.109)
- **Europe PMC papers**: 1619
- **Why important**: ARHGEF2 is among the most connected genes in the module and bridges IGF2BP1, WDR36, YTHDF2, and LAS1L in the co-abundance graph. Its established annotation links it to Rho and Rac guanine-nucleotide-exchange activity, actin organization, cell morphogenesis, intracellular transport, and spindle orientation. HPA reports kidney protein detection and enhancement in monocytes, neutrophils, and oligodendrocytes. It also has meaningful disease and literature coverage.
- **Conclusion**: Established evidence supports ARHGEF2 as a cytoskeletal and small-GTPase signaling regulator with a prominent position in this network. Its connection to the RNA-regulatory genes is a network-level observation, not proof of a direct shared mechanism. It may couple post-transcriptional state changes to cell shape or trafficking, but that coupling remains a hypothesis.

#### DNAAF5

- **Related proteins** (co-abundance neighbors): IGF2BP1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein axonemal assembly factor 5. The protein encoded by this gene is essential for the preassembly or stability of axonemal dynein arms, and is found only in organisms with motile cilia and flagella. Mutations in this gene are associated with primary ciliary dyskinesia-18, a disorder characterized by abnormalities of motile cilia. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Feb 20…
- **Diseases (Open Targets)**: Kartagener Syndrome (0.789); tongue cancer (0.239); ovarian neoplasm (0.173); congenital heart disease (0.152); congenital anomaly of kidney and urinary tract (0.118)
- **Europe PMC papers**: 270
- **Why important**: DNAAF5 is the module member with the clearest specialized ciliary annotation. It is required for preassembly or stability of axonemal dynein arms and is associated with primary ciliary dyskinesia. It connects directly to the IGF2BP1 hub in the co-abundance graph and is enhanced in endometrial ciliated cells. Its disease associations include Kartagener syndrome and congenital abnormalities involving the kidney, although its literature base is more limited than that of the principal RNA regulators.
- **Conclusion**: Established evidence supports DNAAF5 as a motile-cilia and dynein-assembly factor. Its presence may indicate ciliated-cell content or a cilia-related cellular state in part of the shared signal. There is no evidence here that DNAAF5 participates in an IGF2BP1-centered protein complex or that ciliary dysfunction is the overall module function.

#### HMGCS1

- **Related proteins** (co-abundance neighbors): IGF2BP1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3-hydroxy-3-methylglutaryl-CoA synthase 1. Enables protein homodimerization activity. Predicted to be involved in acetyl-CoA metabolic process and farnesyl diphosphate biosynthetic process, mevalonate pathway. Predicted to be located in cytoplasm. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.556); rigid spine syndrome (0.500); mathematical ability (0.289); prostate carcinoma (0.232); Alzheimer disease (0.231)
- **Europe PMC papers**: 3616
- **Why important**: HMGCS1 is connected to IGF2BP1 and provides the module's clearest metabolic branch. It is annotated for acetyl-CoA metabolism, cholesterol and isoprenoid biosynthesis, and the mevalonate pathway. HPA reports liver tissue enhancement, multiple epithelial cell-type enhancements, and kidney protein detection. It also has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports HMGCS1 as a cytosolic enzyme in lipid and mevalonate-related metabolism. Its co-abundance with IGF2BP1 could reflect a shared growth, membrane, or metabolic state, but the supplied data do not demonstrate direct regulation between them or establish that lipid metabolism is a significant module-level function.

## Module 14

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (18)**: ARPC5L, ATG9A, CALU, CFAP20, SPECC1L, DDX41, POLD1, DDX39B, GMFB, MSH2, NEFM, RCN2, DIS3, SOAT1, TARS1, TDRKH, TOMM40, TJP2

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically validated single pathway-level function. Its annotated genes instead suggest several loosely connected cellular programs: neuronal structural biology represented by NEFM; mitochondrial protein import represented by TOMM40; DNA mismatch repair and replication represented by MSH2 and POLD1; RNA processing represented by DDX39B, DDX41, and DIS3; autophagy represented by ATG9A; endoplasmic-reticulum calcium handling represented by CALU and RCN2; and epithelial junction or actin organization represented by TJP2, SPECC1L, ARPC5L, and GMFB. The co-abundance structure therefore appears biologically heterogeneous rather than a clearly defined conserved pathway. The neuronal, epithelial, mitochondrial, nuclear-RNA, DNA-repair, and ER signals may reflect shared cellular composition or coordinated cellular state rather than direct functional coupling.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only RCN2 and CALU have intracellular or membrane secretome annotations, and neither is described as a classical circulating secreted protein. It is also unlikely to be primarily blood-cell derived, because the HPA summary shows low immune-cell specificity for nearly all genes, with only TJP2 showing immune-cell enhancement in non-classical monocytes. Most genes have low tissue specificity, while selected genes are enhanced in brain, skeletal muscle, retina, epididymis, adrenal gland, or testis-related cell types. The frequent enrichment of spermatogenic and trophoblast cell types, together with astrocyte enrichment, suggests that cell-type composition or shared developmental programs could contribute to the cross-tissue signal. Kidney protein detection is widespread among the module genes, whereas autonomic-nervous-system matching tissue protein data are unavailable, so the apparent conservation should not be interpreted as evidence that every gene is intrinsically specific to both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING evidence is limited to two high-confidence known relationships: DDX39B with DDX41 and MSH2 with POLD1. These support established links involving RNA helicase or RNA-processing biology and DNA mismatch repair or replication, respectively, but they do not connect the entire module into one known STRING network. hu.MAP provides additional partial complex support. CALU and RCN2 recur together in several complexes (hu.MAP huMAP3_06399.1), (hu.MAP huMAP3_04958.1), and (hu.MAP huMAP3_10825.1); MSH2 and GMFB occur together in (hu.MAP huMAP3_10130.1); SPECC1L and TJP2 occur together in (hu.MAP huMAP3_05613.1); and DDX39B and DDX41 occur together in the large RNA-processing-associated complex (hu.MAP huMAP3_09943.1). Because these complexes contain only subsets of the module, the evidence favors several embedded molecular neighborhoods rather than one unified complex. The absence of STRING functional enrichment further argues against assigning a specific pathway to the whole module.

**STRING interactions (score >= 0.7)**: 2 of 153 gene pairs: DDX39B–DDX41 (0.874); MSH2–POLD1 (0.994)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06399.1 (CALU, RCN2; 2/3); huMAP3_04958.1 (CALU, RCN2; 2/4); huMAP3_10130.1 (MSH2, GMFB; 2/4); huMAP3_10825.1 (CALU, RCN2; 2/5); huMAP3_05613.1 (SPECC1L, TJP2; 2/11); huMAP3_09943.1 (DDX39B, DDX41; 2/78)

### Novelty

This module may be a new cross-tissue co-abundance observation, but the available evidence is insufficient to call it a new molecular mechanism. Its constituent relationships are not uniformly novel: the MSH2–POLD1 and DDX39B–DDX41 relationships are already represented in STRING, and several gene pairs occur in hu.MAP complexes. Novelty could therefore lie in the coordinated co-abundance of these otherwise distinct neighborhoods across autonomic nervous system and kidney samples, or in the particular tissue-pair context, rather than in discovery of previously unknown physical interactions. Absence of a relationship from STRING or hu.MAP would not establish novelty. Independent replication, cell-composition adjustment, comparison with published cross-tissue modules, and perturbational validation would be needed before claiming a new finding.

**Hypothesis.** Hypothesis: the conserved signal reflects a shared cellular-state or cell-composition program involving neuronal or epithelial structural architecture, ER calcium and protein handling, mitochondrial support, autophagic membrane trafficking, and nuclear RNA or genome maintenance. In kidney, epithelial junction and ER-associated genes could contribute strongly, while in autonomic nervous system, neuronal structural and glial-associated genes could contribute. The apparent bridge between these contexts may be coordinated cellular maintenance under tissue-specific demands rather than direct interaction among all module proteins. This hypothesis predicts that the module will weaken after adjustment for relevant cell types and that its component subprograms will separate when analyzed with cell-resolved data.

### Important genes

#### NEFM

- **Related proteins** (co-abundance neighbors): MSH2 (0.87), CFAP20 (0.87), TARS1 (0.87), TOMM40 (0.85); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neurofilament medium chain. Neurofilaments are type IV intermediate filament heteropolymers composed of light, medium, and heavy chains. Neurofilaments comprise the axoskeleton and functionally maintain neuronal caliber. They may also play a role in intracellular transport to axons and dendrites. This gene encodes the medium neurofilament protein. This protein is commonly used as a biomarker of neuronal damage. Alternative s…
- **Diseases (Open Targets)**: neurodegenerative disease (0.379); placental abruption (0.286); facial pain (0.251); neutropenia (0.249); ovarian dysfunction (0.242)
- **Europe PMC papers**: 1730
- **Why important**: NEFM has one of the strongest network positions in the module and links neuronal structural biology to TOMM40, MSH2, CFAP20, and TARS1 in the co-abundance graph. HPA associates it with brain and retina and with neuronal cell types. Its established role is as the medium neurofilament component of axoskeletal intermediate filaments and as a biomarker of neuronal damage. It has substantial literature and disease relevance to neurodegenerative disease and related neurological phenotypes.
- **Conclusion**: Established evidence supports NEFM as the principal neuronal structural marker in the module. Its module connectivity suggests that neuronal structural state may covary with several maintenance programs, but the data do not establish direct physical interaction with those partners or prove that NEFM drives the cross-tissue module. A neuronal or neuronal-like composition contribution is a plausible hypothesis.

#### TOMM40

- **Related proteins** (co-abundance neighbors): DDX41 (0.88), NEFM (0.85), CALU (0.81), DDX39B (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translocase of outer mitochondrial membrane 40. The protein encoded by this gene is localized in the outer membrane of the mitochondria. It is the channel-forming subunit of the translocase of the mitochondrial outer membrane (TOM) complex that is essential for import of protein precursors into mitochondria. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Aug 2015].
- **Diseases (Open Targets)**: Alzheimer disease (0.325); dementia (0.269); metabolic syndrome (0.262); chronic kidney disease (0.224); Lewy body dementia (0.205)
- **Europe PMC papers**: 2387
- **Why important**: TOMM40 has a strong network position and connects to DDX41, NEFM, CALU, and DDX39B. It encodes the channel-forming subunit of the mitochondrial outer-membrane translocase, making it a central marker of mitochondrial protein import and organelle maintenance. It is detected in kidney and has substantial literature, including disease associations involving Alzheimer disease, dementia, metabolic syndrome, and chronic kidney disease.
- **Conclusion**: Established evidence supports TOMM40 as a mitochondrial maintenance component of the module. Its links to genes from neuronal, ER, and RNA-processing contexts are co-abundance associations, not proof of a shared physical complex. It may report general mitochondrial demand or cellular stress within the conserved signal.

#### MSH2

- **Related proteins** (co-abundance neighbors): NEFM (0.87), DIS3 (0.83), POLD1 (0.82), CFAP20 (0.81); STRING partners: POLD1 (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_10130.1
- **Function (MyGene.info)**: mutS homolog 2. This locus is frequently mutated in hereditary nonpolyposis colon cancer (HNPCC). When cloned, it was discovered to be a human homolog of the E. coli mismatch repair gene mutS, consistent with the characteristic alterations in microsatellite sequences (RER+ phenotype) found in HNPCC. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: Lynch syndrome (0.891); colorectal cancer (0.776); mismatch repair cancer syndrome (0.775); Muir-Torre syndrome (0.752); mismatch repair cancer syndrome 1 (0.740)
- **Europe PMC papers**: 22581
- **Why important**: MSH2 is among the more connected genes in the co-abundance graph and has a high-confidence STRING relationship with POLD1. It is present with GMFB in hu.MAP complex (hu.MAP huMAP3_10130.1). Its established function is mismatch repair and DNA damage tolerance, and it has exceptionally strong disease and literature support through Lynch syndrome and mismatch-repair cancer syndromes.
- **Conclusion**: Established evidence identifies MSH2 as the strongest genome-maintenance anchor in the module, with independent support from STRING and hu.MAP. The co-abundance link to NEFM and CFAP20 does not demonstrate a mechanistic connection between DNA repair and neuronal or ciliary biology. MSH2 may instead reflect proliferative state, DNA maintenance demand, or a shared cell-type signal.

#### ATG9A

- **Related proteins** (co-abundance neighbors): TDRKH (0.86), DDX41 (0.83), RCN2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: autophagy related 9A. Acts upstream of or within autophagosome assembly. Located in endosome; phagophore assembly site; and trans-Golgi network. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); lysosomal storage disease (0.370); cancer (0.094); neoplasm (0.091); triple-negative breast carcinoma (0.076)
- **Europe PMC papers**: 2152
- **Why important**: ATG9A occupies a connecting position between TDRKH, DDX41, and RCN2. It is an established membrane-trafficking factor acting in autophagosome assembly and mitophagy, with localization to endosomal, trans-Golgi, and phagophore-associated compartments. HPA associates it with skeletal muscle and multiple neural cell types, and disease resources link it especially to neurodegenerative and lysosomal disorders.
- **Conclusion**: Established evidence supports ATG9A as an autophagy and membrane-trafficking component. Its placement between RNA-related and ER-associated genes suggests a possible cellular-maintenance interface, but that interpretation is hypothetical because the module contains no globally significant pathway enrichment. It is a useful candidate for testing whether the shared signal reflects organelle quality control.

#### CALU

- **Related proteins** (co-abundance neighbors): SPECC1L (0.81), TOMM40 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_06399.1, huMAP3_04958.1, huMAP3_10825.1
- **Function (MyGene.info)**: calumenin. The product of this gene is a calcium-binding protein localized in the endoplasmic reticulum (ER) and it is involved in such ER functions as protein folding and sorting. This protein belongs to a family of multiple EF-hand proteins (CERC) that include reticulocalbin, ERC-55, and Cab45 and the product of this gene. Alternatively spliced transcript variants encoding different isoforms have been iden…
- **Diseases (Open Targets)**: intelligence (0.490); mathematical ability (0.469); autism spectrum disorder (0.333); attention deficit-hyperactivity disorder (0.333); Alzheimer disease (0.308)
- **Europe PMC papers**: 9190
- **Why important**: CALU is a network bridge between SPECC1L and TOMM40 and repeatedly co-occurs with RCN2 in hu.MAP complexes (hu.MAP huMAP3_06399.1), (hu.MAP huMAP3_04958.1), and (hu.MAP huMAP3_10825.1). It is an ER-localized EF-hand calcium-binding protein involved in ER protein folding and sorting. It is detected in kidney and has extensive literature, with disease-resource associations spanning neurological and cognitive phenotypes.
- **Conclusion**: Established evidence supports CALU as an ER calcium-handling and protein-homeostasis component, with partial complex support alongside RCN2. Its connection to mitochondrial and actin-associated genes supports a possible organelle and cytoskeletal maintenance theme, but a direct CALU-centered mechanism remains unproven. The repeated CALU–RCN2 complex membership makes this pair a strong validation target.

#### TJP2

- **Related proteins** (co-abundance neighbors): ARPC5L (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cell Junctions; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_05613.1
- **Function (MyGene.info)**: tight junction protein 2. This gene encodes a zonula occluden that is a member of the membrane-associated guanylate kinase homolog family. The encoded protein functions as a component of the tight junction barrier in epithelial and endothelial cells and is necessary for proper assembly of tight junctions. Mutations in this gene have been identified in patients with hypercholanemia, and genomic duplication of a 270 kb regio…
- **Diseases (Open Targets)**: cholestasis, progressive familial intrahepatic, 4 (0.800); hypercholanemia, familial 1 (0.647); autosomal dominant nonsyndromic hearing loss (0.558); progressive familial intrahepatic cholestasis type 2 (0.527); deafness (0.467)
- **Europe PMC papers**: 1748
- **Why important**: TJP2 connects ARPC5L in the module and appears with SPECC1L in hu.MAP complex (hu.MAP huMAP3_05613.1). It is a tight-junction scaffold required for epithelial and endothelial barrier organization, and its disease associations include progressive familial intrahepatic cholestasis, hypercholanemia, and hearing loss. HPA places it at plasma membranes and cell junctions and identifies enrichment in several epithelial and neural-associated cell types.
- **Conclusion**: Established evidence supports TJP2 as an epithelial-barrier and junction-organization marker. Its presence is compatible with a kidney epithelial contribution to the conserved module, but it does not show that the entire module is an epithelial program. The TJP2–SPECC1L–ARPC5L neighborhood is a plausible structural submodule requiring cell-resolved validation.

## Module 15

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (13)**: ATXN10, BAX, CYRIB, DDX19B, DNM1L, HARS1, NUDT5, PAFAH1B3, PHIP, PRKDC, PTBP1, GART, TBC1D15

### Function

The module does not support a single statistically established GO or KEGG function: no GO or KEGG term passed global correction, and there are no supplementary STRING enrichment terms. The gene annotations nevertheless suggest a heterogeneous cellular-maintenance program spanning de novo purine synthesis through GART, RNA processing through PTBP1 and DDX19B, translation through HARS1, DNA repair through PRKDC, mitochondrial dynamics through DNM1L, apoptosis through BAX, intracellular trafficking through TBC1D15, and cytoskeletal or immune-signaling regulation through CYRIB. The network contains a relatively connected core around GART, PTBP1, BAX, HARS1, PAFAH1B3 and PRKDC, but its annotated functions are diverse. The most defensible interpretation is therefore a shared cellular-state or housekeeping-associated co-abundance module rather than a narrowly defined pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: every gene has no secretome annotation. Most genes have low tissue specificity, and all are detected by kidney immunohistochemistry, while autonomic-nervous-system protein data are unavailable in HPA. HPA reports low immune-cell specificity for the module as a whole, although several genes show cell-type-enhanced patterns involving neutrophils, neutrophil progenitors, Hofbauer cells, microglia or related cell populations. CYRIB is tissue-enhanced in bone marrow, and several genes are cell-type enhanced without being blood-cell specific. Thus, the module could reflect broadly expressed cellular machinery, kidney sample composition, or a shared cellular state; the evidence does not establish a blood-derived module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and no STRING functional-enrichment term was reported. This argues against a densely documented physical interaction network under the stated STRING criteria, but it does not show that the proteins never interact or that the co-abundance pattern is artifactual. hu.MAP provides the only explicit complex-level support: PRKDC and ATXN10 co-occur in C1 and C2. In both cases they represent only a small subset of very broad complexes, so these observations support some possible shared complex context but do not define the whole module. All other listed genes lack a hu.MAP complex with another module member in the supplied evidence.

**STRING interactions (score >= 0.7)**: 0 of 78 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09042.1 (PRKDC, ATXN10; 2/26); huMAP3_09592.1 (PRKDC, ATXN10; 2/95)

### Novelty

The cross-tissue co-abundance pattern may be a new observation because the module has no high-confidence STRING pairwise interactions, no STRING enrichment, no globally significant GO or KEGG term, and only limited hu.MAP overlap. However, those absences are not evidence of biological novelty by themselves. Several genes are extensively studied and have established roles in common cellular processes, so the likely novel aspect is the particular coordinated pattern across autonomic nervous system and kidney rather than discovery of new gene functions or a new protein complex. Independent cohorts, cell-composition adjustment, replication, and perturbation or biochemical testing would be required before calling the module a novel biological mechanism.

**Hypothesis.** Hypothesis: the module represents a shared cellular-maintenance and stress-response state present in kidney and autonomic-nervous-system samples. Coordinated purine production through GART, RNA processing through PTBP1 and DDX19B, translation through HARS1, genome surveillance through PRKDC and NUDT5, mitochondrial remodeling through DNM1L, and apoptotic control through BAX could be co-regulated when cells adjust biosynthesis, macromolecular quality control and survival. The apparent links to neutrophil-lineage and other cell-type signatures raise an alternative composition hypothesis, namely that a shared cell population contributes to the signal. These are hypotheses, not conclusions from enrichment, because no GO or KEGG term passed global correction and the network lacks STRING-supported physical interactions.

### Important genes

#### GART

- **Related proteins** (co-abundance neighbors): BAX (0.85), DNM1L (0.83), TBC1D15 (0.82), CYRIB (0.81), PAFAH1B3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase. The protein encoded by this gene is a trifunctional polypeptide. It has phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase activity which is required for de novo purine biosynthesis. This enzyme is highly conserved in vertebrates. Alternative splicing of this gene results in two transcript variants encoding different isoforms.…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.606); mesothelioma (0.584); malignant pleural mesothelioma (0.557); adenocarcinoma (0.486); anaplastic lung carcinoma (0.462)
- **Europe PMC papers**: 1890
- **Why important**: GART is the highest-connectivity node in the supplied module and links BAX, DNM1L, TBC1D15, CYRIB and PAFAH1B3. Its established trifunctional activity in de novo purine biosynthesis provides a plausible biosynthetic component for a general cellular-maintenance state. It is broadly expressed, kidney protein is detected, and its literature volume is substantial, making it a strong anchor for interpretation while its cancer associations indicate biological relevance beyond this module.
- **Conclusion**: Established: GART is a purine-biosynthesis enzyme and a central module node. Supported hypothesis: it may mark increased nucleotide supply or cellular metabolic demand in the shared state. Not established: that purine biosynthesis is the defining function of the module.

#### PTBP1

- **Related proteins** (co-abundance neighbors): ATXN10 (0.84), BAX (0.83), HARS1 (0.82), DDX19B (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypyrimidine tract binding protein 1. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA-binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.505); dengue disease (0.372); open-angle glaucoma (0.330); glaucoma (0.309); neoplasm (0.116)
- **Europe PMC papers**: 4849
- **Why important**: PTBP1 is among the most connected nodes and links ATXN10, BAX, HARS1 and DDX19B, placing RNA processing close to both the putative core and peripheral genes. Its established role in pre-mRNA processing and alternative splicing is compatible with broad regulation of cell state. It is broadly expressed, detected in kidney, strongly represented in the literature, and associated in the supplied evidence with neurodevelopmental and other disease areas.
- **Conclusion**: Established: PTBP1 is a widely expressed RNA-binding regulator of splicing and mRNA metabolism. Supported hypothesis: it may coordinate transcript processing across the two tissues. Not established: a module-specific splicing program or causal regulation of the other module genes.

#### BAX

- **Related proteins** (co-abundance neighbors): GART (0.85), PTBP1 (0.83), PAFAH1B3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BCL2 associated X, apoptosis regulator. The protein encoded by this gene belongs to the BCL2 protein family. BCL2 family members form hetero- or homodimers and act as anti- or pro-apoptotic regulators that are involved in a wide variety of cellular activities. This protein forms a heterodimer with BCL2, and functions as an apoptotic activator. The association and the ratio of BAX to BCL2 also determines survival or death of a cell follo…
- **Diseases (Open Targets)**: T-cell acute lymphoblastic leukemia (0.463); colon carcinoma (0.427); endometrial carcinoma (0.383); neurodegenerative disease (0.380); gastric adenocarcinoma (0.375)
- **Europe PMC papers**: 122372
- **Why important**: BAX is a connected bridge between GART, PTBP1 and PAFAH1B3. Its established role as a pro-apoptotic BCL2-family regulator gives the module a direct survival and cell-turnover axis, and its literature volume is exceptionally large. Kidney protein is detected, and its disease associations span malignancy and neurodegeneration, both relevant to tissue stress but not specific to this module.
- **Conclusion**: Established: BAX regulates mitochondrial apoptotic signaling and cell survival. Supported hypothesis: the module may accompany altered survival or stress balance. Not established: that the module is an apoptosis module or that BAX drives the observed co-abundance.

#### PRKDC

- **Related proteins** (co-abundance neighbors): PHIP (0.85), HARS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_09042.1, huMAP3_09592.1
- **Function (MyGene.info)**: protein kinase, DNA-activated, catalytic subunit. This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to DNA-PKcs deficiency (0.752); neurodegenerative disease (0.548); severe combined immunodeficiency (0.470); combined immunodeficiency (0.464); ovarian neoplasm (0.210)
- **Europe PMC papers**: 12461
- **Why important**: PRKDC connects to PHIP and HARS1 and is one of the two module members jointly represented in hu.MAP complexes C1 and C2 with ATXN10. Its established DNA-dependent protein kinase function in double-strand-break repair, recombination and innate immune-related processes provides a genome-maintenance interpretation. It is detected in kidney, shows cell-type enhancement involving erythrocyte progenitors and neutrophils, and has substantial disease literature including immunodeficiency.
- **Conclusion**: Established: PRKDC is a DNA-repair kinase with immune and genome-stability roles. Supported hypothesis: it may indicate shared genome-surveillance demand or provide the limited complex-supported part of the module. Not established: a direct PRKDC–ATXN10 functional pathway in this tissue pair.

#### ATXN10

- **Related proteins** (co-abundance neighbors): PTBP1 (0.84), HARS1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_09042.1, huMAP3_09592.1
- **Function (MyGene.info)**: ataxin 10. This gene encodes a protein that may function in neuron survival, neuron differentiation, and neuritogenesis. These roles may be carried out via activation of the mitogen-activated protein kinase cascade. Expansion of an ATTCT repeat from 9-32 copies to 800-4500 copies in an intronic region of this locus has been associated with spinocerebellar ataxia, type 10. Alternatively spliced transcript var…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 10 (0.624); neurodegenerative disease (0.437); Dupuytren Contracture (0.265); benign endocrine neoplasm (0.215); benign neoplasm of adrenal gland (0.215)
- **Europe PMC papers**: 701
- **Why important**: ATXN10 links PTBP1 and HARS1 and co-occurs with PRKDC in both reported hu.MAP complexes, making it important despite modest network connectivity. Its established annotations include neuron survival or differentiation, neurite-related processes, cytokinesis and cilium assembly, which are pertinent to autonomic nervous system biology and potentially to kidney cellular architecture. It is detected in kidney and has disease associations involving spinocerebellar ataxia and neurodegeneration.
- **Conclusion**: Established: ATXN10 has documented links to neuronal biology, cytokinesis and ciliary or projection-related processes, and it shares hu.MAP complex contexts with PRKDC. Supported hypothesis: it may connect tissue-specific structural or neuronal biology to a general maintenance state. Not established: that ATXN10 explains the conservation of the module between the two tissues.

## Module 16

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (7)**: BAG2, HEATR3, HEATR6, RPL12, RWDD4, TOP2B, WDR18

### Function

No GO/KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The gene annotations nevertheless suggest a broadly intracellular maintenance program involving ribosome biogenesis and transport, protein folding and proteostasis, cytoplasmic translation, RNA processing, and DNA topology. HEATR3 is the central co-abundance hub, connecting WDR18, HEATR6, RWDD4, and TOP2B, while the remaining genes form a loosely connected chain through RWDD4, BAG2, and RPL12. Thus, the most defensible interpretation is a mixed cellular housekeeping module rather than a sharply defined autonomic-nervous-system or kidney pathway. The topology may reflect coordinated expression of general biosynthetic, proteostasis, and nuclear processes, but this remains an inference rather than enrichment-based evidence.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. All module genes have low tissue specificity, and the HPA summary reports low immune-cell specificity for nearly all genes, with no enriched blood-cell category. This argues against interpreting the module primarily as a blood-cell or plasma-protein signal. Several genes show enhanced expression in selected cell types such as trophoblast, decidual stromal, oocyte, or esophageal epithelial populations, but these patterns do not establish a shared autonomic-nervous-system or kidney cell type. Kidney protein detection is present for most assayed genes, whereas autonomic-nervous-system protein comparison is unavailable because there is no matching HPA tissue. Overall, the composition is more consistent with broadly expressed intracellular proteins and possible shared cellular-state effects than with a tissue-specific secretory program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only one high-confidence relationship within the module, RPL12--WDR18, and reports no functional enrichment. This means that most observed co-abundance edges are not independently supported by the supplied STRING interaction network. hu.MAP supplies partial complex-level support: TOP2B and WDR18 co-occur in huMAP3_11063.1 (hu.MAP huMAP3_11063.1) and huMAP3_07162.1 (hu.MAP huMAP3_07162.1). The additional members of those complexes include NAP1L1, NOL9, SENP3, LAS1L, and other nuclear or chromatin-associated proteins, which is compatible with a nuclear RNA-processing or chromatin-related context. However, only a subset of each complex is represented in this module, so the hu.MAP evidence supports specific relationships rather than the entire co-abundance module. The combination of a sparse STRING graph and partial hu.MAP overlap indicates that the module is an expression-coordination signal with limited direct interaction-network corroboration.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: RPL12–WDR18 (0.737)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11063.1 (TOP2B, WDR18; 2/8); huMAP3_07162.1 (TOP2B, WDR18; 2/9)

### Novelty

This module should not be called a definitively new biological complex or pathway. Its cross-tissue co-abundance pattern may be a novel observation, especially because the module combines HEATR3, HEATR6, RWDD4, BAG2, TOP2B, WDR18, and RPL12 in a sparse structure. Nevertheless, known biology overlaps with the module: RPL12--WDR18 is supported by STRING, and TOP2B--WDR18 appears in two hu.MAP complexes (hu.MAP huMAP3_11063.1) and (hu.MAP huMAP3_07162.1). The absence of additional STRING or hu.MAP relationships does not establish novelty, because interaction databases are incomplete and co-abundance need not represent physical binding. A novelty claim therefore requires replication in independent autonomic-nervous-system and kidney cohorts, control for cell composition and technical effects, and validation of the coordinated protein or transcript behavior.

**Hypothesis.** Hypothesis: this conserved module reflects a shared intracellular stress-adaptation and biosynthetic state in autonomic-nervous-system and kidney samples. In this model, HEATR3 may coordinate a ribosome-related or nuclear transport program, WDR18 and TOP2B may connect that state to nuclear RNA-processing or chromatin-associated complexes (hu.MAP huMAP3_11063.1) (hu.MAP huMAP3_07162.1), BAG2 may contribute proteostasis and protein-folding control, and RPL12 may represent the translational output of the state. HEATR6 and RWDD4 may mark less-characterized supporting components of the same coordinated program. This is a mechanistic hypothesis, not a demonstrated pathway: the lack of globally significant GO/KEGG enrichment and the sparse known-interaction support require experimental testing.

### Important genes

#### HEATR3

- **Related proteins** (co-abundance neighbors): WDR18 (0.92), HEATR6 (0.86), RWDD4 (0.84), TOP2B (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HEAT repeat containing 3. The protein encoded by this gene plays a role in ribosomal protein transport and in the assembly of the 5S ribonucleoprotein particle (5S RNP). The encoded protein also may be involved in NOD2-mediated NF-kappaB signaling. [provided by RefSeq, Jul 2016].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.616); Diamond-Blackfan anemia (0.588); Diamond-Blackfan anemia 21 (0.501); Intellectual disability (0.495); Abnormal finger morphology (0.494)
- **Europe PMC papers**: 242
- **Why important**: HEATR3 is the network hub, connected to WDR18, HEATR6, RWDD4, and TOP2B. Its supplied annotation links it to ribosomal protein transport, five-S ribonucleoprotein assembly, nuclear import, large-subunit biogenesis, and possible NOD2-mediated NF-kappaB signaling. It is detected in kidney by HPA and has substantial literature relative to the less-characterized module members. Its central position makes it the strongest candidate for organizing the module's co-abundance pattern.
- **Conclusion**: Established evidence supports HEATR3 as the topological hub and as a protein associated with ribosome-related and nuclear processes. It is plausible, but unproven, that HEATR3 coordinates the conserved module; the co-abundance data do not demonstrate physical binding or causal control.

#### WDR18

- **Related proteins** (co-abundance neighbors): HEATR3 (0.92); STRING partners: RPL12 (0.737)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_11063.1, huMAP3_07162.1
- **Function (MyGene.info)**: WD repeat domain 18. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.417); ovarian neoplasm (0.263); COVID-19 (0.025); age-related macular degeneration (0.025); Alzheimer disease (0.023)
- **Europe PMC papers**: 245
- **Why important**: WDR18 connects directly to HEATR3 and is the only gene with the supplied STRING relationship to RPL12. It is also the module member shared with TOP2B in both hu.MAP complexes (hu.MAP huMAP3_11063.1) and (hu.MAP huMAP3_07162.1). Its annotations include rRNA processing, DNA replication, and nuclear functions, while HPA places the protein in the nucleoplasm and detects it in kidney. These network and complex links make WDR18 the clearest bridge between the co-abundance graph and independently curated molecular complexes.
- **Conclusion**: Established evidence supports WDR18 as a nuclear and ribosome-associated component with partial STRING and hu.MAP support. Its role as a bridge organizing this specific tissue-pair module is a hypothesis that needs targeted interaction and perturbation experiments.

#### TOP2B

- **Related proteins** (co-abundance neighbors): HEATR3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_11063.1, huMAP3_07162.1
- **Function (MyGene.info)**: DNA topoisomerase II beta. This gene encodes a DNA topoisomerase, an enzyme that controls and alters the topologic states of DNA during transcription. This nuclear enzyme is involved in processes such as chromosome condensation, chromatid separation, and the relief of torsional stress that occurs during DNA transcription and replication. It catalyzes the transient breaking and rejoining of two strands of duplex DNA which al…
- **Diseases (Open Targets)**: B-cell immunodeficiency, distal limb anomalies, and urogenital malformations (0.720); neoplasm (0.597); small cell lung carcinoma (0.561); breast cancer (0.552); small cell carcinoma (0.486)
- **Europe PMC papers**: 1781
- **Why important**: TOP2B links to the HEATR3 hub and is present with WDR18 in both hu.MAP complexes (hu.MAP huMAP3_11063.1) and (hu.MAP huMAP3_07162.1). Its established function is to control DNA topology during transcription and replication, with additional roles in chromosome behavior and cellular differentiation. It has extensive disease and literature coverage, including developmental and neoplastic associations, making it biologically interpretable even though it has only a peripheral position in the module graph.
- **Conclusion**: Established evidence supports TOP2B as a DNA-topology enzyme and as a member of the two relevant hu.MAP complexes. A contribution to the module through transcriptional or chromatin-state regulation is plausible, but the supplied data do not show that TOP2B drives the shared tissue pattern.

#### BAG2

- **Related proteins** (co-abundance neighbors): RWDD4 (0.85), RPL12 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BAG cochaperone 2. BAG proteins compete with Hip for binding to the Hsc70/Hsp70 ATPase domain and promote substrate release. All the BAG proteins have an approximately 45-amino acid BAG domain near the C terminus but differ markedly in their N-terminal regions. The predicted BAG2 protein contains 211 amino acids. The BAG domains of BAG1, BAG2, and BAG3 interact specifically with the Hsc70 ATPase domain in vitro and …
- **Diseases (Open Targets)**: dengue disease (0.370); neurodegenerative disease (0.335); RAB23-related Carpenter syndrome (0.190); neoplasm (0.112); gastric cancer (0.098)
- **Europe PMC papers**: 1122
- **Why important**: BAG2 is a bridge between RWDD4 and RPL12 and has the strongest direct functional annotation for proteostasis in the module. It promotes substrate release from Hsp70-family ATPase domains and is associated with protein folding, protein stabilization, and proteasomal processing. It has a substantial literature and disease-association record, including neurodegenerative disease, which is relevant to an autonomic-nervous-system context. Its position suggests a possible connection between protein quality control and the translational component represented by RPL12.
- **Conclusion**: Established evidence supports BAG2 as a cochaperone involved in protein folding and protein-quality control. Its participation in a shared proteostasis state is a reasonable hypothesis, but the module does not establish that BAG2 mechanistically links the other genes.

## Module 17

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (37)**: BOLA2, CBX5, CHORDC1, DHFR, EXOSC2, FKBP3, TUBGCP2, HNRNPH1, HNRNPL, HNRNPR, ISYNA1, MAK16, MATR3, MBD3, WDR77, NUP88, CBFB, PSMC6, PSMC2, PSMA1, DROSHA, RPP30, RRP12, SEH1L, SEPTIN2, PHGDH, SMAP, SMARCA4, SUPT16H, SMNDC1, ALYREF, TMOD3, TRA2B, EFTUD2, WDR12, WDR26, ZNF207

### Function

The strongest interpretation is a nuclear gene-expression and RNA-processing module. The primary evidence is enrichment for nuclear lumen (GO:CC nuclear lumen; q_global = 0.0351) and nuclear protein-containing complex (GO:CC nuclear protein-containing complex; q_global = 0.0439). The genes include spliceosome and RNA-processing factors such as HNRNPL, HNRNPR, HNRNPH1, TRA2B, EFTUD2, EXOSC2, RPP30, DROSHA and SMNDC1; nuclear transport components such as NUP88 and SEH1L; chromatin regulators such as CBX5, SMARCA4, MBD3 and SUPT16H; ribosome-biogenesis factors such as WDR12, MAK16 and RRP12; and proteasome components such as PSMA1, PSMC2 and PSMC6. Thus, the module most plausibly reflects coordinated abundance of nuclear RNA maturation, RNA export, chromatin organization, ribosome biogenesis and nuclear protein-complex machinery. The STRING RNA-metabolism and nuclear-compartment results (5 supplementary STRING terms; within-query FDR 0.0027–0.0407) support this interpretation but are supplementary rather than globally corrected primary evidence. The absence of enriched biological-process terms does not invalidate the module; it indicates that the robust signal is concentrated at the cellular-component and complex level.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly nuclear, nucleolar, nucleoplasmic or associated with nuclear complexes. Most genes have low tissue specificity, and most have low immune-cell specificity, arguing against a simple blood-cell or plasma contamination explanation. HPA nevertheless reports cell-type-enhanced expression for many genes, including microglia, erythrocyte progenitors, cardiomyocytes, distal convoluted tubule cells and other specialized cell types. RRP12 is immune-cell enhanced in neutrophils, while ALYREF is tissue enhanced in bone marrow and CBX5 is tissue enhanced in choroid plexus. Kidney protein detection is broad across the measured module genes, whereas autonomic-nervous-system protein matching was unavailable. The shared signal should therefore be interpreted mainly as a conserved nuclear housekeeping or cell-state program, while allowing that shared cellular composition or cell-state differences between tissues may contribute.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC nuclear lumen | 0.0351 | ALYREF, CBFB, CBX5, DROSHA, EFTUD2, EXOSC2, HNRNPH1, HNRNPL, HNRNPR, MAK16, MATR3, MBD3, NUP88, PSMA1, PSMC2, PSMC6, RPP30, RRP12, SEPTIN2, SMARCA4, SMNDC1, SUPT16H, TRA2B, TUBGCP2, WDR12, WDR26, WDR77, ZNF207 |
| GO:CC nuclear protein-containing complex | 0.0439 | CBFB, CBX5, DROSHA, EFTUD2, EXOSC2, HNRNPH1, HNRNPR, MBD3, NUP88, RPP30, SEH1L, SMARCA4, SMNDC1, SUPT16H, TRA2B, WDR12 |

### STRING and hu.MAP

STRING provides direct or functionally supported relationships among an RNA-binding cluster centered on HNRNPL, HNRNPR, HNRNPH1, MATR3 and TRA2B, an ALYREF-linked RNA-export and processing cluster, a proteasome cluster containing PSMA1, PSMC2 and PSMC6, a nucleoporin pair involving NUP88 and SEH1L, and additional links involving CBX5, SMARCA4, WDR77, MAK16 and WDR12. These relationships are consistent with known molecular machinery rather than an arbitrary co-abundance grouping. hu.MAP independently places HNRNPL, HNRNPR and MATR3 in several heterogeneous nuclear ribonucleoprotein complexes (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_06975.1), PSMA1, PSMC2 and PSMC6 in proteasome complexes (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) (hu.MAP huMAP3_05064.1), NUP88 and SEH1L in a nuclear-pore complex (hu.MAP huMAP3_12581.1), ALYREF and TRA2B in an RNA-processing or export complex (hu.MAP huMAP3_09943.1), and EFTUD2 with WDR77 in a spliceosomal complex (hu.MAP huMAP3_08980.1). Because only subsets of the larger complexes occur in this module, the co-abundance pattern is best viewed as coordinated representation of several connected nuclear systems, not as evidence that all module proteins form one physical complex.

**STRING interactions (score >= 0.7)**: 22 of 666 gene pairs: ALYREF–EFTUD2 (0.89); ALYREF–HNRNPH1 (0.914); ALYREF–HNRNPL (0.844); ALYREF–HNRNPR (0.851); ALYREF–TRA2B (0.869); CBX5–SMARCA4 (0.923); DROSHA–RPP30 (0.727); HNRNPH1–HNRNPL (0.982); HNRNPH1–HNRNPR (0.947); HNRNPH1–MATR3 (0.911); HNRNPH1–TRA2B (0.981); HNRNPL–HNRNPR (0.961); HNRNPL–MATR3 (0.757); HNRNPL–TRA2B (0.903); HNRNPR–MATR3 (0.714); HNRNPR–TRA2B (0.89); MAK16–WDR12 (0.998); NUP88–SEH1L (0.993); PSMA1–PSMC2 (0.999); PSMA1–PSMC6 (0.999); PSMC2–PSMC6 (0.999); SMARCA4–WDR77 (0.798)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Metabolism of RNA (FDR = 0.0027, 16 genes); COMPARTMENTS Nucleus (FDR = 0.0059, 30 genes); Component Nuclear protein-containing complex (FDR = 0.0075, 17 genes); Component Nuclear lumen (FDR = 0.0231, 28 genes); Component Ribonucleoprotein complex (FDR = 0.0407, 12 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07581.1 (HNRNPR, HNRNPL, MATR3; 3/21); huMAP3_10625.1 (HNRNPR, HNRNPL, MATR3; 3/57); huMAP3_09656.1 (PSMA1, PSMC2, PSMC6; 3/64); huMAP3_13725.1 (PSMA1, PSMC2, PSMC6; 3/69); huMAP3_05721.1 (HNRNPL, MATR3; 2/6); huMAP3_07225.1 (HNRNPR, HNRNPL; 2/7); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09654.1 (HNRNPR, HNRNPL; 2/13); huMAP3_10659.1 (HNRNPR, HNRNPL; 2/28); huMAP3_06975.1 (MATR3, TRA2B; 2/31); huMAP3_05064.1 (PSMC2, PSMC6; 2/31); huMAP3_12581.1 (SEH1L, NUP88; 2/58); huMAP3_09943.1 (TRA2B, ALYREF; 2/78); huMAP3_08980.1 (EFTUD2, WDR77; 2/97)

### Novelty

The module is not a wholly new molecular mechanism: many of its relationships and subgroups are already represented in STRING and hu.MAP, especially heterogeneous nuclear ribonucleoprotein, proteasome, nuclear-pore and spliceosomal machinery. The novel aspect may instead be the reproducible co-abundance of these nuclear systems across autonomic nervous system and kidney, particularly if this tissue-pair sharing has not previously been reported. That claim cannot be established from the fact sheet alone. Absence of some module genes from STRING or hu.MAP is not evidence of novelty, because databases are incomplete and the module contains only partial representations of larger complexes. The appropriate conclusion is that the module is biologically coherent and potentially novel at the cross-tissue co-abundance level, but not demonstrably a new protein complex or new molecular pathway.

**Hypothesis.** Hypothesis: autonomic-nervous-system and kidney cells share a regulated nuclear maintenance program in which RNA-binding and splicing factors coordinate transcript processing and export, chromatin regulators control access to transcriptional programs, nucleolar factors support ribosome production, and proteasomes remove damaged or excess nuclear proteins. This integrated program could help both tissues maintain long-lived, highly specialized cells under transcriptional, proteostatic and metabolic demands. The hypothesis predicts coordinated changes in RNA splicing and export, chromatin accessibility, ribosome biogenesis and proteasome activity across the two tissues. It remains a hypothesis because the co-abundance data do not establish directionality, physical interaction among every module member, or causal regulation.

### Important genes

#### HNRNPL

- **Related proteins** (co-abundance neighbors): SUPT16H (0.92), CBX5 (0.87), EFTUD2 (0.85), SMNDC1 (0.85), WDR12 (0.83), RRP12 (0.82), PSMA1 (0.80); STRING partners: ALYREF (0.844), HNRNPH1 (0.982), HNRNPR (0.961), MATR3 (0.757), TRA2B (0.903)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_07581.1, huMAP3_10625.1, huMAP3_05721.1, huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_10659.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is a high-connectivity module hub and is linked by STRING to ALYREF, HNRNPH1, HNRNPR, MATR3 and TRA2B. It is present in the primary nuclear-lumen evidence (GO:CC nuclear lumen; q_global = 0.0351), the supplementary RNA-metabolism and nuclear-complex terms (5 supplementary STRING terms; within-query FDR 0.0027–0.0407), and many hu.MAP heterogeneous nuclear ribonucleoprotein complexes (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1). Its established function is RNA processing and regulation of alternative splicing. It also has substantial literature support and HPA enhancement in several neural and kidney-relevant cell types.
- **Conclusion**: Established evidence supports HNRNPL as a central RNA-processing and splicing component of the module. Hypothesis: its hub position may help couple tissue-specific transcript regulation to the broader nuclear maintenance program shared by the two tissues.

#### HNRNPR

- **Related proteins** (co-abundance neighbors): ALYREF (0.87), SEH1L (0.81), PSMC6 (0.81), CBX5 (0.80); STRING partners: ALYREF (0.851), HNRNPH1 (0.947), HNRNPL (0.961), MATR3 (0.714), TRA2B (0.89)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_07581.1, huMAP3_10625.1, huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_10659.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR connects the RNA-binding cluster to ALYREF, SEH1L, PSMC6 and CBX5 in the module and has strong STRING relationships with HNRNPL, HNRNPH1, MATR3 and TRA2B. It is represented in both globally corrected cellular-component terms (GO:CC nuclear lumen; q_global = 0.0351) (GO:CC nuclear protein-containing complex; q_global = 0.0439), all major supplementary STRING terms (5 supplementary STRING terms; within-query FDR 0.0027–0.0407), and multiple hu.MAP RNA-protein complexes (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1). Its established role is spliceosomal mRNA processing and transport, and its disease associations include neurodevelopmental disorders, intellectual disability, developmental delay and seizure.
- **Conclusion**: Established evidence identifies HNRNPR as a bridge between RNA processing, nuclear organization and other module subsystems. Hypothesis: altered HNRNPR abundance could be one route by which shared nuclear regulation affects neuronal and renal cell states.

#### ALYREF

- **Related proteins** (co-abundance neighbors): HNRNPR (0.87), CBX5 (0.84), BOLA2; BOLA2B (0.81), WDR12 (0.81), TRA2B (0.80); STRING partners: EFTUD2 (0.89), HNRNPH1 (0.914), HNRNPL (0.844), HNRNPR (0.851), TRA2B (0.869)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_09943.1
- **Function (MyGene.info)**: Aly/REF export factor. The protein encoded by this gene is a heat stable, nuclear protein and functions as a molecular chaperone. It is thought to regulate dimerization, DNA binding, and transcriptional activity of basic region-leucine zipper (bZIP) proteins. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.542); dengue disease (0.370); neoplasm (0.103); non-small cell lung carcinoma (0.102); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 1636
- **Why important**: ALYREF is a module connector linking several hnRNP proteins and TRA2B, and it has STRING relationships with EFTUD2, HNRNPH1, HNRNPL, HNRNPR and TRA2B. It appears in the primary nuclear-lumen term (GO:CC nuclear lumen; q_global = 0.0351) and all supplementary STRING categories (5 supplementary STRING terms; within-query FDR 0.0027–0.0407), and it participates with TRA2B in a hu.MAP complex (hu.MAP huMAP3_09943.1). Its established functions include nuclear mRNA export and mRNA metabolism. HPA describes nuclear-speckle and nucleoplasmic localization, with tissue enhancement in bone marrow and cell-type enhancement in erythroid and megakaryocytic progenitors.
- **Conclusion**: Established evidence supports ALYREF as an RNA-export and processing link within the module, with possible relevance to cell-state composition. Hypothesis: ALYREF may coordinate export of transcripts generated by the splicing and chromatin machinery represented elsewhere in the module.

#### SMARCA4

- **Related proteins** (co-abundance neighbors): MBD3 (0.82), DROSHA (0.80); STRING partners: CBX5 (0.923), WDR77 (0.798)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center, Nucleoli rim; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SWI/SNF related BAF chromatin remodeling complex subunit ATPase 4. The protein encoded by this gene is a member of the SWI/SNF family of proteins and is similar to the brahma protein of Drosophila. Members of this family have helicase and ATPase activities and are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI, wh…
- **Diseases (Open Targets)**: intellectual disability, autosomal dominant 16 (0.796); rhabdoid tumor predisposition syndrome 2 (0.788); familial rhabdoid tumor (0.685); rhabdoid tumor (0.627); medulloblastoma (0.586)
- **Europe PMC papers**: 9906
- **Why important**: SMARCA4 is a chromatin-remodeling ATPase connected in the module to MBD3 and DROSHA, and STRING links it to CBX5 and WDR77. It belongs to both primary cellular-component terms (GO:CC nuclear lumen; q_global = 0.0351) (GO:CC nuclear protein-containing complex; q_global = 0.0439) and the supplementary nuclear and nuclear-complex terms (STRING COMPARTMENTS Nucleus; within-query FDR = 0.0059) (STRING Component Nuclear protein-containing complex; within-query FDR = 0.0075) (STRING Component Nuclear lumen; within-query FDR = 0.0231). Its established function is ATP-dependent chromatin remodeling and regulation of transcription. It has extensive literature and disease associations including intellectual disability and rhabdoid tumor predisposition.
- **Conclusion**: Established evidence places SMARCA4 as the module's prominent chromatin and transcriptional regulator. Hypothesis: SMARCA4 could provide an upstream regulatory layer that links chromatin state to the RNA-processing and proteostasis activities co-abundant in both tissues.

#### PSMC2

- **Related proteins** (co-abundance neighbors): HNRNPH1 (0.84), SUPT16H (0.83), SEH1L (0.80); STRING partners: PSMA1 (0.999), PSMC6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1, huMAP3_05064.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is part of the proteasome ATPase component and is strongly linked by STRING to PSMA1 and PSMC6. It is present in the primary nuclear-lumen term (GO:CC nuclear lumen; q_global = 0.0351) and supplementary RNA-metabolism and nuclear-compartment terms (STRING RCTM Metabolism of RNA; within-query FDR = 0.0027) (STRING COMPARTMENTS Nucleus; within-query FDR = 0.0059) (STRING Component Nuclear lumen; within-query FDR = 0.0231), and it occurs with PSMA1 and PSMC6 in multiple hu.MAP proteasome complexes (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) (hu.MAP huMAP3_05064.1). Its established function is ATP-dependent proteasomal protein catabolism and response to oxidative stress. It also has disease associations involving plasma-cell myeloma, mantle-cell lymphoma, neoplasm and amyloidosis.
- **Conclusion**: Established evidence supports PSMC2 as a proteostasis component that gives the module a protein-quality-control dimension beyond RNA processing. Hypothesis: proteasome activity may help maintain the nuclear machinery represented by the module during oxidative or other cellular stress.

## Module 18

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (8)**: MTHFD1, HNRNPK, IPO4, MARCKS, CTPS1, RBM39, CCT7, VPS45

### Function

No GO or KEGG term passed global correction, so enrichment does not assign a specific module function. The gene annotations instead indicate a mixed intracellular program involving folate-mediated one-carbon metabolism and nucleotide synthesis through MTHFD1, pyrimidine and phospholipid precursor synthesis through CTPS1, chaperone-assisted protein folding through CCT7, RNA processing and transcriptional regulation through RBM39 and HNRNPK, intracellular transport through VPS45 and IPO4, and actin-linked membrane organization through MARCKS. The most connected part of the observed graph contains MTHFD1, CCT7, RBM39, and CTPS1. This is more consistent with a shared intracellular maintenance or biosynthetic state than with a narrowly defined tissue-specific pathway, although the co-abundance data do not establish a single biochemical pathway.

**Cell composition.** The module contains no secreted genes, so it is not dominated by plasma or secreted proteins. Most genes have low tissue specificity and low immune-cell specificity, which argues against a straightforward blood-cell contamination explanation. The HPA cell-type evidence is heterogeneous, including hepatocytes, cardiomyocytes, spermatogenic cells, neural cells, smooth muscle cells, urothelial cells, adipocytes, and myeloid cells. MTHFD1 is tissue enriched in liver, IPO4 is tissue enhanced in testis, and RBM39 is tissue enhanced in bone marrow. MARCKS is immune-cell enhanced in intermediate monocytes and neutrophils, but the module as a whole is not blood-cell enriched. Kidney immunohistochemistry detects most module proteins, whereas autonomic nervous system protein detection has no matching HPA tissue. Overall, broadly distributed intracellular proteins and shared cellular states are more plausible explanations than secretion or a uniform blood-cell origin.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair met the supplied high-confidence STRING interaction criterion, STRING functional enrichment was absent, and no hu.MAP complex contained multiple module members. Therefore, the co-abundance relationships are not corroborated by the supplied high-confidence physical-interaction or curated-complex evidence. This does not prove that the proteins never interact; it means that the observed covariance is not explained by the queried resources. The module may reflect coordinated expression, indirect pathway coupling, shared cellular state, or sample composition. The gene annotations support plausible functional links among biosynthesis, RNA regulation, protein folding, trafficking, and membrane dynamics, but not an established shared complex.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The particular cross-tissue co-abundance configuration may be under-characterized, but a new biological mechanism cannot be claimed from the fact sheet alone. The individual genes and their functions are already well studied, and the absence of STRING or hu.MAP support does not prove novelty. Co-abundance modules can capture indirect regulation, cell-state covariance, tissue composition, or relationships not represented in interaction databases. A cautious conclusion is that this may be a new observation at the module level, while its biological novelty remains unproven. Replication, comparison with published co-expression modules, cell-resolved analysis, and perturbation experiments would be needed.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular growth, maintenance, or stress-adaptation state in subsets of cells from autonomic nervous system and kidney samples. MTHFD1 and CTPS1 could supply one-carbon and nucleotide biosynthetic capacity; CCT7 could support folding of newly produced proteins; RBM39 and HNRNPK could coordinate RNA processing and transcriptional responses; IPO4 could support nuclear import; VPS45 could support intracellular sorting; and MARCKS could connect the state to actin organization, membrane trafficking, and cell movement. This is a mechanistic hypothesis, not a result of globally significant enrichment or demonstrated physical complex formation. An alternative explanation is covariance caused by shared broadly expressing cell types or sample composition.

### Important genes

#### MTHFD1

- **Related proteins** (co-abundance neighbors): IPO4 (0.82), CTPS1 (0.82), CCT7 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methylenetetrahydrofolate dehydrogenase, cyclohydrolase and formyltetrahydrofolate synthetase 1. This gene encodes a protein that possesses three distinct enzymatic activities, 5,10-methylenetetrahydrofolate dehydrogenase, 5,10-methenyltetrahydrofolate cyclohydrolase and 10-formyltetrahydrofolate synthetase. Each of these activities catalyzes one of three sequential reactions in the interconversion of 1-carbon derivatives of tetrahydrofolate, which are substrates for methionine, thymidylate, …
- **Diseases (Open Targets)**: combined immunodeficiency and megaloblastic anemia with or without hyperhomocysteinemia (0.773); severe combined immunodeficiency (0.473); neural tube defects, folate-sensitive (0.414); isolated spina bifida (0.376); atrial fibrillation (0.332)
- **Europe PMC papers**: 1939
- **Why important**: MTHFD1 is among the most connected genes and links to IPO4, CTPS1, and CCT7. It encodes a trifunctional enzyme in folate-mediated one-carbon metabolism that contributes to methionine, thymidylate, and purine synthesis. Its annotations include purine biosynthesis, sulfur amino-acid metabolism, neutrophil homeostasis, heart development, and neural tube closure. Its disease associations include combined immunodeficiency, megaloblastic anemia, folate-sensitive neural tube defects, spina bifida, and atrial fibrillation. Its liver-enriched and multi-cell-type HPA pattern supports metabolic relevance but not tissue specificity for this module.
- **Conclusion**: Established: MTHFD1 is a central module gene with important folate and nucleotide-biosynthetic functions and clinically relevant deficiency associations. Hypothesis: it may anchor the biosynthetic component of the shared module. Causality is not established by the co-abundance data.

#### CTPS1

- **Related proteins** (co-abundance neighbors): MTHFD1 (0.82), RBM39 (0.81), CCT7 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CTP synthase 1. This gene encodes an enzyme responsible for the catalytic conversion of UTP (uridine triphosphate) to CTP (cytidine triphospate). This reaction is an important step in the biosynthesis of phospholipids and nucleic acids. Activity of this proten is important in the immune system, and loss of function of this gene has been associated with immunodeficiency. Alternative splicing results in multiple tr…
- **Diseases (Open Targets)**: combined immunodeficiency due to CTPS1 deficiency (0.712); androgenetic alopecia (0.204); hyperpituitarism (0.195); urolithiasis (0.097); alcohol drinking (0.097)
- **Europe PMC papers**: 641
- **Why important**: CTPS1 is among the most connected genes and links to MTHFD1, RBM39, and CCT7. It catalyzes CTP production for pyrimidine, nucleic-acid, and phospholipid biosynthesis, and its activity is important in the immune system. Loss of function is associated with immunodeficiency. Its annotations include pyrimidine biosynthesis and negative regulation of type one interferon production, while its HPA cell-type pattern includes hepatocytes, salivary acinar cells, and smooth muscle cells.
- **Conclusion**: Established: CTPS1 is a central nucleotide-biosynthetic enzyme with a clear immunodeficiency association. Hypothesis: its covariance with MTHFD1 may indicate coordinated biosynthetic demand. The module does not support an immune-only interpretation.

#### CCT7

- **Related proteins** (co-abundance neighbors): VPS45 (0.83), MTHFD1 (0.82), CTPS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is among the most connected genes and links VPS45, MTHFD1, and CTPS1. It is a subunit of the CCT chaperonin complex, which folds proteins including actin and tubulin. This provides a plausible bridge between biosynthetic activity and cytoskeletal or trafficking demands. Its HPA profile is broadly expressed with enhanced signal in spermatogenic cell types, and it has associations with myocardial infarction, preeclampsia, neurodegenerative disease, and hepatocellular carcinoma.
- **Conclusion**: Established: CCT7 participates in chaperone-assisted protein folding and is centrally positioned in the observed graph. Hypothesis: it may couple protein production or remodeling to cytoskeletal maintenance. A complete CCT complex is not demonstrated in this module.

#### RBM39

- **Related proteins** (co-abundance neighbors): HNRNPK (0.82), CTPS1 (0.81), MARCKS (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 39. This gene encodes a member of the U2AF65 family of proteins. The encoded protein is found in the nucleus, where it co-localizes with core spliceosomal proteins. It has been shown to play a role in both steroid hormone receptor-mediated transcription and alternative splicing, and it is also a transcriptional coregulator of the viral oncoprotein v-Rel. Multiple transcript variants have been observed…
- **Diseases (Open Targets)**: neurodegenerative disease (0.401); endometrial cancer (0.220); skin neoplasm (0.217); skin cancer (0.217); actinic keratosis (0.217)
- **Europe PMC papers**: 1169
- **Why important**: RBM39 is among the most connected genes and links HNRNPK, CTPS1, and MARCKS. It is a nuclear RNA-binding and transcriptional coregulatory protein involved in RNA processing, alternative splicing, and steroid-hormone-receptor-mediated transcription. Its nuclear-speckle localization supports a role in regulating cellular gene-expression state. It is tissue enhanced in bone marrow and has disease associations including neurodegenerative disease and neoplastic conditions.
- **Conclusion**: Established: RBM39 functions in RNA processing, splicing, and transcriptional regulation and is centrally positioned in the module. Hypothesis: it may coordinate the expression program linking nucleotide demand with protein and membrane remodeling. The module does not identify a specific RBM39-regulated transcript set.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): VPS45 (0.84), RBM39 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK links VPS45 and RBM39 and has the largest literature base among the selected regulatory genes. It is a broadly expressed heterogeneous nuclear ribonucleoprotein involved in pre-mRNA processing, RNA transport, transcriptional regulation, and signal transduction. Its nucleoplasmic localization and disease associations, including Au-Kline syndrome and neurodevelopmental disease, support importance for cellular state regulation. Its low tissue and cell-type specificity is compatible with a shared intracellular program.
- **Conclusion**: Established: HNRNPK is a broadly acting RNA-binding and transcriptional regulator connected to RBM39 and VPS45. Hypothesis: it may help stabilize a common gene-expression state across the tissue groups. Direct interaction and causal control of the other module genes are not established.

## Module 19

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (7)**: CCDC25, DDX55, FBXO30, HMGN5, PPIE, RBM26, VIRMA

### Function

The module is most consistent with a coordinated nuclear gene-regulatory and RNA-processing program. PPIE links several module members and is associated with RNA binding, spliceosomal mRNA splicing, and protein folding. VIRMA is associated with mRNA processing, alternative polyadenylation, and mRNA methylation; RBM26 with RNA processing; DDX55 with large-subunit rRNA maturation and possible spliceosome or ribosome assembly; and HMGN5 with chromatin organization and transcriptional regulation. FBXO30 contributes a protein-ubiquitination/proteasomal regulation component, while CCDC25 has an annotation related to cell motility. These annotations support a broad nuclear RNA and gene-expression interpretation, but not a narrowly defined pathway. No GO or KEGG term passed global correction, and there was no STRING functional enrichment. Therefore, the functional interpretation is annotation-led and hypothesis-generating rather than evidence of a significantly enriched canonical pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: none of the members is annotated as secreted. All members were detected at the protein level in kidney, whereas the autonomic-nervous-system comparison had no matching HPA tissue entry. Most genes have low tissue specificity and most have low cell-type specificity, arguing against a strongly tissue-restricted program. The module is also not broadly blood-cell enriched overall, although FBXO30 is immune-cell enriched in basophils. HMGN5 is tissue enhanced in testis and has several cell-type-enhanced annotations, including late spermatids, epididymal cells, erythrocyte progenitors, and Sertoli cells. Thus, shared cell composition, a broadly expressed housekeeping-like nuclear program, or sample-specific cellular admixture could contribute to the cross-tissue co-abundance signal. The testis and cell-type annotations for HMGN5 should not be interpreted as evidence that the module is a testis module in these tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The co-abundance network contains relationships among the module genes, but none of the possible within-module gene pairs meets the supplied high-confidence STRING interaction threshold. STRING therefore provides no established physical or functional interaction for this module, and its absence should not be treated as evidence that the proteins never interact. No hu.MAP complex contains multiple module members. The network topology nevertheless places PPIE and FBXO30 as the main internal connectors, with PPIE linking FBXO30, DDX55, and VIRMA, and FBXO30 also linking CCDC25 and VIRMA. These are co-abundance relationships, not validated protein-complex edges. The lack of STRING and hu.MAP support means the module is better viewed as a coordinated expression signature than as a demonstrated molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears to be a potentially novel cross-tissue co-abundance signature, but novelty cannot be established solely from the absence of STRING interactions or hu.MAP complexes. The case for novelty is that the genes form a shared autonomic-nervous-system and kidney expression module despite having no supplied canonical enrichment, no STRING functional enrichment, and no known multi-member hu.MAP complex. The genes themselves are not uniformly unstudied: VIRMA and PPIE have substantial literature support, while the other members have more limited coverage. A definitive novelty claim would require comparison with published tissue co-expression modules, independent cohorts, and prior kidney or autonomic nervous system network studies. At present, the appropriate conclusion is a novel candidate network pattern rather than a proven new biological mechanism.

**Hypothesis.** Hypothesis: in a shared kidney and autonomic-nervous-system cellular context, coordinated regulation of RNA maturation, RNA modification, ribosome or spliceosome-related processes, chromatin accessibility, and protein quality control produces the observed co-abundance pattern. PPIE, VIRMA, RBM26, and DDX55 could mark the RNA-processing component, HMGN5 could reflect chromatin and transcriptional state, and FBXO30 could connect that state to regulated protein turnover. The module may therefore represent a shared nuclear gene-expression state rather than a stable protein complex. An alternative hypothesis is that the signal partly reflects shared cell-type composition or broadly expressed housekeeping activity; this should be tested with cell deconvolution, independent tissue cohorts, and perturbation or protein-interaction experiments.

### Important genes

#### PPIE

- **Related proteins** (co-abundance neighbors): FBXO30 (0.86), DDX55 (0.85), VIRMA (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peptidylprolyl isomerase E. The protein encoded by this gene is a member of the peptidyl-prolyl cis-trans isomerase (PPIase) family. PPIases catalyze the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and accelerate the folding of proteins. This protein contains a highly conserved cyclophilin (CYP) domain as well as an RNA-binding domain. It was shown to possess PPIase and protein folding activities…
- **Diseases (Open Targets)**: dengue disease (0.370); diabetes mellitus (0.102); hemochromatosis type 5 (0.049); sideroblastic anemia 3 (0.049); sleep apnea syndrome (0.047)
- **Europe PMC papers**: 758
- **Why important**: PPIE is the strongest network connector in the supplied topology, linking FBXO30, DDX55, and VIRMA. Its established annotations span peptidyl-prolyl isomerase activity, protein folding, RNA binding, and spliceosomal mRNA splicing. It also has the largest listed literature volume among the module genes and disease associations including dengue disease, diabetes mellitus, hemochromatosis type five, sideroblastic anemia, and sleep apnea syndrome. Its central position makes it a useful candidate marker of the module, although the network does not establish direct physical binding.
- **Conclusion**: Established evidence supports PPIE as a multifunctional RNA- and protein-folding regulator and as a central co-abundance hub. It is a plausible driver or readout of the proposed nuclear program, but causality and its relevance to the shared tissue signal remain hypotheses.

#### VIRMA

- **Related proteins** (co-abundance neighbors): PPIE (0.82), FBXO30 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vir like m6A methyltransferase associated. Enables RNA binding activity. Involved in mRNA alternative polyadenylation and mRNA methylation. Located in cytosol and nuclear speck. Colocalizes with RNA N6-methyladenosine methyltransferase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: smoking initiation (0.355); Abnormality of the skeletal system (0.355); obesity disorder (0.344); orofacial cleft (0.256); cleft palate (0.221)
- **Europe PMC papers**: 1994
- **Why important**: VIRMA connects PPIE and FBXO30 and has a direct annotation to mRNA processing, alternative polyadenylation, and RNA methylation through the m six A methyltransferase complex. It has the broadest listed literature support in the module and associations with smoking initiation, obesity disorder, skeletal abnormalities, and craniofacial developmental traits. Its network position and RNA-modification function make it a strong mechanistic anchor.
- **Conclusion**: Established evidence supports VIRMA as an RNA-processing and RNA-methylation regulator that plausibly explains part of the module's coordinated expression. Whether VIRMA organizes the module in kidney or autonomic nervous system is not established and remains a hypothesis.

#### FBXO30

- **Related proteins** (co-abundance neighbors): PPIE (0.86), VIRMA (0.82), CCDC25 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Immune cell enriched; location Microtubules; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: F-box protein 30. This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.266); hair color (0.192); urolithiasis (0.161); alcohol drinking (0.161); nonpapillary renal cell carcinoma (0.074)
- **Europe PMC papers**: 312
- **Why important**: FBXO30 is one of the principal internal connectors, linking PPIE, VIRMA, and CCDC25. Its F-box annotation places it in the SCF ubiquitin-ligase family and supports a role in regulated protein ubiquitination and proteasomal turnover. It is also immune-cell enriched in basophils and has disease or trait associations including skeletal abnormality, urolithiasis, alcohol drinking, hair color, and nonpapillary renal cell carcinoma. This combination makes it relevant to both network integration and possible tissue or cell-state effects.
- **Conclusion**: Established evidence supports FBXO30 as a candidate protein-turnover regulator and a central co-abundance connector. Its basophil annotation raises a composition-related alternative explanation, but there is insufficient evidence to assign it a specific kidney or autonomic function in this module.

#### HMGN5

- **Related proteins** (co-abundance neighbors): RBM26 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: high mobility group nucleosome binding domain 5. This gene encodes a nuclear protein with similarities to the high mobility group proteins, HMG14 and HMG17, which suggests that this protein may function as a nucleosomal binding and transcriptional activating protein. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: Abnormality of refraction (0.200); urinary bladder carcinoma (0.097); urinary bladder cancer (0.097); osteosarcoma (0.091); gastric cancer (0.086)
- **Europe PMC papers**: 403
- **Why important**: HMGN5 connects to RBM26 and is the only member with tissue-enhanced testis expression in the supplied HPA summary. Its established description supports nucleosome-associated chromatin regulation, transcriptional activation, regulation of cell proliferation, and suppression of apoptosis. It also has cell-type-enhanced annotations spanning reproductive and erythrocyte-progenitor contexts, plus associations with bladder cancer, urinary bladder carcinoma, osteosarcoma, and other traits. This makes it important for distinguishing a genuine nuclear state from cell-composition effects.
- **Conclusion**: Established evidence supports HMGN5 as a chromatin and transcriptional regulator with distinctive cell-type annotations. Its presence may help connect RNA processing to transcriptional state, but it may also be a composition marker; either interpretation requires validation.

#### RBM26

- **Related proteins** (co-abundance neighbors): CCDC25 (0.84), HMGN5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 26. Enables RNA binding activity. Predicted to be involved in mRNA processing. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.495); adolescent idiopathic scoliosis (0.269); schizophrenia (0.263); substance-related disorder (0.175); sialolithiasis (0.161)
- **Europe PMC papers**: 257
- **Why important**: RBM26 is positioned between CCDC25 and HMGN5 and is annotated for RNA binding, mRNA processing, and RNA catabolic processes. Its disease-association list includes neurodegenerative disease, schizophrenia, adolescent idiopathic scoliosis, substance-related disorder, and sialolithiasis, making it relevant to the autonomic and neurological context without proving a tissue-specific role. Its intermediate literature coverage and position at the interface with HMGN5 make it a useful candidate for testing the RNA-processing and chromatin-state connection.
- **Conclusion**: Established evidence supports RBM26 as a predicted RNA-processing regulator and a co-abundance bridge to HMGN5. Its specific molecular contribution to this module is uncertain, so a role in coupling RNA handling to chromatin regulation is a hypothesis rather than a demonstrated mechanism.

## Module 20

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (6)**: CNPY2, CTNND1, POGLUT3, RBP1, SACM1L, UBA5

### Function

The module does not support a single established pathway-level function: no GO or KEGG term passed global correction, and there are no supplementary STRING enrichment terms. Its structure is a connected chain-like subgraph linking CNPY2 with RBP1 and POGLUT3, RBP1 with CTNND1, and CTNND1 with SACM1L and UBA5. The annotations instead point to several related cellular themes: retinoid and lipid handling through RBP1, cell adhesion and signal transduction through CTNND1, phosphoinositide and membrane organization through SACM1L, endoplasmic-reticulum protein glycosylation through POGLUT3, and protein quality-control or stress-related modification through UBA5. CNPY2 may provide an endoplasmic-reticulum-associated regulatory link. These annotations support a cautious interpretation involving epithelial organization, membrane trafficking, and proteostasis, but they do not establish a unified pathway.

**Cell composition.** The module is not dominated by classical plasma proteins or broadly secreted proteins. HPA labels two genes as secreted genes in its summary, although the individual annotations describe CNPY2 and POGLUT3 as intracellular and membrane-associated rather than freely secreted. Most genes have low tissue specificity, while most show cell-type-enhanced expression. Distal convoluted tubule cells are the only repeatedly represented cell type in the summary, and every module protein was detected by kidney immunohistochemistry. The blood-cell evidence does not indicate a strongly blood-cell-derived module overall: most genes have low immune-cell specificity, one is group-enriched in monocyte and myeloid dendritic-cell populations, and one is not detected in immune cells. Thus, shared kidney or epithelial cell composition is a plausible contributor, whereas a plasma-protein or generalized immune-cell explanation is less compelling. HPA provides no matching autonomic-nervous-system tissue protein comparison.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship was present among the module genes, and no STRING functional-enrichment term was reported. No hu.MAP complex contained multiple module members. Therefore, the co-abundance links are not corroborated here as established physical interactions or as membership in a known protein complex. This does not show that the proteins cannot interact; it indicates that the present module is better regarded as a coordinated expression or abundance pattern than as a validated molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unrecognized cross-tissue co-abundance pattern because it lacks high-confidence STRING support, lacks a multi-member hu.MAP complex, and lacks a globally significant GO or KEGG annotation. However, absence from those resources does not prove biological novelty. The constituent genes and their individual functions are already represented in the literature, with particularly substantial literature for RBP1, CTNND1, and SACM1L. The defensible claim is therefore novelty of the specific autonomic-nervous-system–kidney co-abundance configuration, not novelty of the genes, their functions, or a demonstrated physical complex.

**Hypothesis.** Hypothesis: in a shared kidney-associated epithelial or related cell state, coordinated abundance of retinoid handling, cell adhesion, phosphoinositide regulation, endoplasmic-reticulum glycosylation, and ubiquitin-like protein modification could couple epithelial organization with membrane and proteostasis demands. RBP1 could mark retinoid and lipid handling, CTNND1 could connect the state to cell-cell adhesion and signaling, SACM1L could regulate phosphoinositide-dependent membrane organization, POGLUT3 and CNPY2 could reflect endoplasmic-reticulum processing, and UBA5 could reflect stress-responsive protein modification. This is a mechanistic model rather than an established interaction network, and it should be tested with cell-type-resolved measurements, perturbation experiments, and direct protein-interaction assays.

### Important genes

#### CTNND1

- **Related proteins** (co-abundance neighbors): SACM1L (0.82), RBP1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin delta 1. This gene encodes a member of the Armadillo protein family, which function in adhesion between cells and signal transduction. Multiple translation initiation codons and alternative splicing result in many different isoforms being translated. Not all of the full-length natures of the described transcript variants have been determined. Read-through transcription also exists between this gene and the…
- **Diseases (Open Targets)**: blepharocheilodontic syndrome (0.724); listeriosis (0.526); cleft lip (0.510); hereditary disease (0.415); exudative vitreoretinopathy (0.376)
- **Europe PMC papers**: 3021
- **Why important**: CTNND1 is a central connector in the module, linking RBP1 and SACM1L. Its plasma-membrane localization and annotations for cadherin-mediated cell-cell adhesion, cell migration, signal transduction, and protein stabilization make it a plausible structural bridge between tissue organization and intracellular signaling. It is cell-type enhanced in distal convoluted tubule and other epithelial-associated populations, and its blood-cell annotation includes monocyte and myeloid dendritic-cell groups. It also has substantial literature and multiple disease associations in the fact sheet.
- **Conclusion**: Established: CTNND1 is an adhesion and signaling protein with kidney detection and a central position in this module. Hypothesis: it may connect epithelial cell-state composition to the co-abundance of membrane, lipid, and proteostasis regulators. The module does not establish that CTNND1 physically interacts with its neighboring proteins.

#### RBP1

- **Related proteins** (co-abundance neighbors): CNPY2 (0.88), CTNND1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: retinol binding protein 1. This gene encodes the carrier protein involved in the transport of retinol (vitamin A alcohol) from the liver storage site to peripheral tissue. Vitamin A is a fat-soluble vitamin necessary for growth, reproduction, differentiation of epithelial tissues, and vision. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.364); preeclampsia (0.304); dyshidrosis (0.271); Leber congenital amaurosis (0.126); cancer (0.099)
- **Europe PMC papers**: 2911
- **Why important**: RBP1 is one of the two most connected bridge positions in the subgraph, linking CNPY2 to CTNND1. Its established carrier role in retinol transport and its annotations for retinoid metabolism, retinoic-acid biosynthesis, fatty-acid transport, and lipid homeostasis give the module a distinctive metabolic axis. It is tissue enhanced in choroid plexus and ovary, cell-type enhanced in several stromal and reproductive epithelial populations, not detected in immune cells, and detected in kidney. It also has the largest literature volume among the module genes listed in the fact sheet.
- **Conclusion**: Established: RBP1 represents retinoid and lipid handling and is a prominent network bridge. Hypothesis: RBP1 may mark a differentiated epithelial state shared across the sampled tissues, rather than acting as a direct driver of the entire module.

#### SACM1L

- **Related proteins** (co-abundance neighbors): CTNND1 (0.82), UBA5 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SAC1 like phosphatidylinositide phosphatase. This gene encodes an integral membrane protein, which is localized to the endoplasmic reticulum, and functions as a phosphoinositide phosphatase that hydrolyzes phosphatidylinositol 3-phosphate, phosphatidylinositol 4-phosphate, and phosphatidylinositol 3,5-bisphosphate. Deletion of this gene in mouse results in preimplantation lethality. Other studies suggest that this gene is also involved in th…
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); placenta praevia (0.352); alcohol drinking (0.193); autoimmune disorder of central nervous system (0.175); digestive system disorder (0.077)
- **Europe PMC papers**: 1120
- **Why important**: SACM1L connects CTNND1 with UBA5 and is therefore positioned between adhesion-related and protein-modification-related parts of the graph. Its phosphoinositide-phosphatase activity and roles in endoplasmic-reticulum and Golgi organization provide a plausible membrane-trafficking link. Its annotation also includes exocytic insertion of neurotransmitter receptors, which is relevant to the autonomic-nervous-system context, although the module itself does not prove neuronal specificity. SACM1L has substantial literature and disease associations in the fact sheet.
- **Conclusion**: Established: SACM1L regulates phosphoinositides and is associated with endoplasmic-reticulum and Golgi membrane organization. Hypothesis: it could coordinate membrane organization with CTNND1-associated adhesion and UBA5-associated proteostasis in the shared abundance state.

#### CNPY2

- **Related proteins** (co-abundance neighbors): RBP1 (0.88), POGLUT3 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: canopy FGF signaling regulator 2. Predicted to be active in endoplasmic reticulum. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the face (0.266); craniosynostosis (0.266); neurodegenerative disease (0.237); Short stature (0.184); neoplasm (0.088)
- **Europe PMC papers**: 309
- **Why important**: CNPY2 has a bridge position linking RBP1 with POGLUT3, placing it between the retinoid-associated and glycosylation-associated portions of the network. It is predicted to be active in the endoplasmic reticulum and is described as a regulator of FGF signaling, with additional annotations for gene-expression regulation and low-density-lipoprotein clearance. It is detected in kidney and cell-type enhanced across several epithelial or reproductive-associated populations. Its literature volume is smaller than that of the major bridge genes, which makes its role more exploratory.
- **Conclusion**: Established: CNPY2 is an endoplasmic-reticulum-associated candidate regulator with a bridging position in the module. Hypothesis: it may couple ER processing or signaling regulation to retinoid and glycosylation-related cell states, but the available evidence does not establish this mechanism.

#### UBA5

- **Related proteins** (co-abundance neighbors): SACM1L (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin like modifier activating enzyme 5. This gene encodes a member of the E1-like ubiquitin-activating enzyme family. This protein activates ubiquitin-fold modifier 1, a ubiquitin-like post-translational modifier protein, via the formation of a high-energy thioester bond. Alternative splicing results in multiple transcript variants. A pseudogene of this gene has been identified on chromosome 1. [provided by RefSeq, Feb 2016].
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 44 (0.794); spinocerebellar ataxia, autosomal recessive 24 (0.691); autosomal recessive spinocerebellar ataxia 7 (0.554); neurodegenerative disease (0.534); Intellectual disability (0.518)
- **Europe PMC papers**: 573
- **Why important**: UBA5 is a terminal module member connected to SACM1L and encodes an E1-like enzyme that activates a ubiquitin-fold modifier. Its annotations include response to endoplasmic-reticulum stress, neuromuscular processes, erythrocyte and megakaryocyte differentiation, and regulation of type II interferon production. It is detected in kidney and is cell-type enhanced in cardiomyocytes and late spermatids. Its disease associations include developmental and neurodegenerative conditions, while its literature volume is intermediate within this module.
- **Conclusion**: Established: UBA5 is a protein-modification enzyme with links to ER stress and neuromuscular biology. Hypothesis: UBA5 may indicate a proteostasis or stress-response component of the shared module, potentially coordinated with SACM1L-dependent membrane organization. Its terminal graph position does not establish that it controls the module.

## Module 21

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (10)**: CPNE2, ERI1, HSP90AB2P, HSPA8, PKM, PUS7, YARS1, TCOF1, CCT8, NAE1

### Function

The module does not have any GO or KEGG term that passes global multiple-testing correction; therefore, no pathway-level enrichment is established. Its gene-level composition nevertheless points to a mixed cellular-maintenance program rather than a tissue-specific pathway. PKM represents glycolytic energy production; YARS1 represents aminoacylation and protein translation; ERI1 and PUS7 represent RNA processing and RNA modification; HSPA8, CCT8 and the HSP90AB2P pseudogene are associated with proteostasis; NAE1 represents protein neddylation; and CPNE2 is associated with calcium-dependent membrane–cytoplasm signaling. The network therefore most plausibly reflects coordinated demands for energy metabolism, RNA and protein homeostasis, and intracellular stress handling. This interpretation is hypothesis-generating because the absence of globally significant GO or KEGG enrichment means that the module should not be assigned a single established pathway.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins: the HPA summary reports no secreted genes. It is also not blood-cell enriched according to the HPA blood-cell specificity results. Most annotated genes have low tissue specificity, while many show cell-type enhancement across a disparate set of cell types, including reproductive, neural-support, epithelial, muscle, and hematopoietic-associated populations. That scattered pattern does not support a coherent blood-cell or single-cell-type explanation. Protein detection is reported for nearly all assessed genes in kidney, whereas there is no matching HPA tissue for autonomic nervous system. Consequently, the shared module may reflect broadly expressed kidney cellular machinery or a common cellular state captured in both tissue groups, rather than a specialized autonomic–renal lineage program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supplies one high-confidence direct relationship within the module, between CCT8 and HSPA8. This supports a proteostasis-related substructure, but the lack of STRING partners for the other genes and the absence of STRING functional enrichment argue against a densely established interaction network. hu.MAP provides two partial complex matches: (hu.MAP huMAP3_13998.1) contains YARS1 and PUS7, and (hu.MAP huMAP3_14442.1) contains PKM and YARS1. These findings connect YARS1 to RNA-related machinery and to a broader metabolic or cellular-maintenance complex, but each complex contributes only a small subset of its members to this module. Together, STRING and hu.MAP support selected mechanistic links rather than validation of the entire co-abundance module. The remaining edges may represent co-regulation, tissue-state effects, indirect associations, or interactions not captured by these resources.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: CCT8–HSPA8 (0.905)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13998.1 (YARS1, PUS7; 2/23); huMAP3_14442.1 (PKM, YARS1; 2/57)

### Novelty

The shared co-abundance pattern may be a new observation, because the supplied resources show only a limited set of previously catalogued physical or complex relationships and no globally significant pathway enrichment. However, it cannot be called a definitively novel biological complex or pathway. The genes are individually well characterized, several have substantial literature support, and absence from STRING or hu.MAP does not demonstrate novelty. The defensible claim is that the cross-tissue co-abundance organization, rather than the individual molecular functions, is potentially novel and requires replication in independent cohorts, preservation testing, and comparison with cell-composition and technical covariates.

**Hypothesis.** Hypothesis: this module is a shared cellular-stress and biosynthetic state in kidney and autonomic nervous system samples. PKM could supply glycolytic energy, while YARS1 supports translation and ERI1 together with PUS7 supports maturation or modification of RNA. HSPA8 and CCT8 could buffer folding and assembly demands, with NAE1 contributing regulated protein turnover through neddylation. CPNE2 may couple this intracellular state to calcium-sensitive membrane signaling. The observed co-abundance could therefore arise when cells increase energy production, RNA handling, translation, proteostasis, and stress adaptation together. This is a mechanistic hypothesis, not an enrichment result; it should be tested by cell-resolved expression, perturbation of the proposed hubs, and measurement of glycolysis, RNA processing, protein folding, and neddylation.

### Important genes

#### PKM

- **Related proteins** (co-abundance neighbors): YARS1 (0.85), NAE1 (0.81), CPNE2 (0.80), HSP90AB2P (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: pyruvate kinase M1/2. This gene encodes a protein involved in glycolysis. The encoded protein is a pyruvate kinase that catalyzes the transfer of a phosphoryl group from phosphoenolpyruvate to ADP, generating ATP and pyruvate. This protein has been shown to interact with thyroid hormone and may mediate cellular metabolic effects induced by thyroid hormones. This protein has been found to bind Opa protein, a bacterial o…
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); autoimmune disorder of central nervous system (0.370); tympanic membrane perforation (0.204); neoplasm (0.121); hepatocellular carcinoma (0.120)
- **Europe PMC papers**: 8544
- **Why important**: PKM is the strongest network hub in the supplied module and connects the metabolic branch to YARS1, NAE1, CPNE2, and HSP90AB2P. Its established function is pyruvate-kinase activity in glycolysis, and it is detected in kidney by HPA. It also has extensive literature support and broad disease associations in the supplied evidence, making it the clearest candidate for linking cellular energy state to the rest of the module.
- **Conclusion**: Established evidence supports PKM as a glycolytic enzyme and a central co-abundance connector. It is plausible, but unproven, that PKM coordinates energy availability with RNA, proteostasis, and signaling processes in this module.

#### YARS1

- **Related proteins** (co-abundance neighbors): ERI1 (0.89), PKM (0.85), HSP90AB2P (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_13998.1, huMAP3_14442.1
- **Function (MyGene.info)**: tyrosyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Tyrosyl-tRNA synthetase belongs to the class I tRNA synthetase family. Cytokine activities have also been observ…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease dominant intermediate C (0.739); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset 2 (0.707); hereditary disease (0.509); Charcot-Marie-Tooth disease (0.418); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset (0.333)
- **Europe PMC papers**: 215
- **Why important**: YARS1 is a network bridge connecting ERI1, PKM, and HSP90AB2P, and it is the only module member appearing in both huMAP matches (hu.MAP huMAP3_13998.1) and (hu.MAP huMAP3_14442.1). Its established role in tyrosyl-tRNA aminoacylation places it at the interface of translation and cellular biosynthetic demand. Its disease associations include inherited neurological phenotypes, which is relevant to a module shared with autonomic nervous system tissue.
- **Conclusion**: Established evidence supports YARS1 as a translation-related enzyme and a structural bridge between the RNA-associated and metabolic portions of the module. A coordinating role for YARS1 in the shared tissue program remains a hypothesis rather than a demonstrated causal function.

#### ERI1

- **Related proteins** (co-abundance neighbors): TCOF1 (0.90), YARS1 (0.89), PUS7 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exoribonuclease 1. Enables 3'-5' exonuclease activity. Predicted to be involved in exonucleolytic trimming to generate mature 3'-end of 5.8S rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Located in cytoplasm and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: spondyloepimetaphyseal dysplasia, Guo-Campeau type (0.660); Hoxha-Aliu syndrome (0.586); neurodegenerative disease (0.478); hypertensive disorder (0.476); Abnormality of the skeletal system (0.453)
- **Europe PMC papers**: 561
- **Why important**: ERI1 is a highly connected bridge within the RNA-processing branch, linking TCOF1, YARS1, and PUS7. Its established function is three-prime-to-five-prime exonucleolytic processing involved in maturation of five-point-eight-S ribosomal RNA and other RNA-processing activities. The supplied disease associations include skeletal, developmental, neurological, and hypertensive conditions, while HPA identifies renal collecting duct principal cells among its enhanced cell types.
- **Conclusion**: Established evidence supports ERI1 as an RNA maturation factor that could connect ribosome-related processing to translation demand. Its apparent role as a kidney-relevant bridge in this module is plausible but requires cell-specific validation.

#### HSPA8

- **Related proteins** (co-abundance neighbors): HSP90AB2P (0.80); STRING partners: CCT8 (0.905)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Flagellar centriole, Annulus; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 8. This gene encodes a member of the heat shock protein 70 family, which contains both heat-inducible and constitutively expressed members. This protein belongs to the latter group, which are also referred to as heat-shock cognate proteins. It functions as a chaperone, and binds to nascent polypeptides to facilitate correct folding. It also functions as an ATPase in the disassembly of clathrin-coated…
- **Diseases (Open Targets)**: dengue disease (0.505); systemic lupus erythematosus (0.375); smoking initiation (0.199); Lennox-Gastaut syndrome (0.118); neoplasm (0.105)
- **Europe PMC papers**: 6937
- **Why important**: HSPA8 forms the module's clearest STRING-supported relationship with CCT8 and is a constitutively expressed HSP seventy-family chaperone. Its established functions include folding nascent proteins, responding to unfolded proteins, and participating in vesicle disassembly. It has extensive literature support and is detected in kidney, making it a strong candidate for representing proteostasis within the module.
- **Conclusion**: Established evidence supports HSPA8 as a proteostasis and intracellular-trafficking factor, with a known relationship to CCT8. Its participation in a coordinated stress-response state shared by the two tissues is a reasonable hypothesis, not proof that the whole module is a chaperone complex.

#### NAE1

- **Related proteins** (co-abundance neighbors): CCT8 (0.86), PKM (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NEDD8 activating enzyme E1 subunit 1. The protein encoded by this gene binds to the beta-amyloid precursor protein. Beta-amyloid precursor protein is a cell surface protein with signal-transducing properties, and it is thought to play a role in the pathogenesis of Alzheimer's disease. In addition, the encoded protein can form a heterodimer with UBE1C and bind and activate NEDD8, a ubiquitin-like protein. This protein is required for c…
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and ischiopubic hypoplasia (0.576); neurodegenerative disease (0.533); acute myeloid leukemia (0.347); myelodysplastic syndrome (0.345); chronic myelomonocytic leukemia (0.286)
- **Europe PMC papers**: 798
- **Why important**: NAE1 connects PKM to CCT8 in the co-abundance graph and contributes a regulatory layer distinct from glycolysis and RNA processing. Its established function is as a subunit of the NEDD8-activating enzyme, with roles in protein neddylation, cell-cycle checkpoint control, and regulation of apoptotic processes. It also has supplied disease associations involving neurodevelopment, neurodegeneration, and hematologic disorders.
- **Conclusion**: Established evidence supports NAE1 as a neddylation and protein-regulatory factor. Its network placement suggests a possible link between metabolic state and regulated protein turnover, but that cross-process mechanism has not been demonstrated for this module.

## Module 22

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (9)**: DDX31, TMPO, TMPO, RNGTT, MICALL1, MSH3, RBM22, TAF6, TRIM33

### Function

The module is most consistent with a broadly expressed nuclear gene-regulation and RNA-processing program, with a possible connection to genome maintenance. This interpretation comes from the functions of DDX31 in ribosome biogenesis, RBM22 in pre-mRNA splicing, RNGTT in mRNA capping, TAF6 in transcription initiation, MSH3 in mismatch repair, TRIM33 in transcriptional repression and signaling regulation, and TMPO in nuclear-envelope and chromatin organization. MICALL1 adds a membrane-trafficking and cytoskeletal component. The co-abundance graph links these functions through a sparse chain-like structure, but the absence of a globally corrected GO or KEGG term means that no pathway-level enrichment is established. The module should therefore be interpreted as a coordinated expression pattern rather than as a proven biochemical pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and several are broadly distributed nuclear or intracellular proteins, which is compatible with a housekeeping-like expression component. The HPA single-cell annotations are heterogeneous, including progenitor and cytotrophoblast populations, while immune-cell specificity is generally low. This does not support a strongly blood-cell-specific module, although the lymphoid, erythrocyte-progenitor, megakaryocyte-progenitor, monocyte-progenitor, neutrophil-progenitor, and basophil annotations suggest that cellular composition could contribute to the shared signal. Kidney protein detection is available for most annotated genes, whereas matching autonomic-nervous-system protein data are unavailable. Thus, the apparent conservation may reflect broadly expressed cellular machinery, shared cell types, or sample composition rather than a specialized autonomic-kidney function.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and no hu.MAP complex contains multiple module members. Consequently, the co-abundance links are not independently supported here as established physical interactions or membership in a known multiprotein complex. The individual annotations nevertheless describe plausible functional relationships among RNA processing, transcription, nuclear organization, and DNA repair. These relationships are biological context, not evidence that the observed module is a physical complex.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a previously unreported tissue-pair co-abundance pattern, but the available evidence is insufficient to call it a new biological mechanism. Its genes have established functions and disease associations, and the module is compatible with general nuclear and cellular programs. The lack of STRING or hu.MAP support does not demonstrate novelty; it may instead reflect transient regulation, indirect co-expression, incomplete database coverage, or a module driven by cell composition. A defensible novelty claim would require replication in independent autonomic-nervous-system and kidney datasets, preservation after cell-type adjustment, and comparison with published co-expression modules.

**Hypothesis.** Hypothesis: the conserved module reflects coordinated maintenance of gene expression and cellular integrity across autonomic-nervous-system and kidney samples. In this model, TAF6 supports transcription initiation, RNGTT and RBM22 support maturation and processing of transcripts, DDX31 supports ribosome biogenesis, TMPO organizes the nuclear envelope and chromatin, MSH3 contributes mismatch repair, and TRIM33 modulates transcriptional and signaling responses. MICALL1 may connect this intracellular program to membrane trafficking or cell-state transitions. This is a mechanistic hypothesis rather than an established pathway, and the sparse network plus lack of enrichment and complex evidence makes a cell-composition or generalized cellular-state explanation an important alternative.

### Important genes

#### MSH3

- **Related proteins** (co-abundance neighbors): TRIM33 (0.85), TMPO (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutS homolog 3. The protein encoded by this gene forms a heterodimer with MSH2 to form MutS beta, part of the post-replicative DNA mismatch repair system. MutS beta initiates mismatch repair by binding to a mismatch and then forming a complex with MutL alpha heterodimer. This gene contains a polymorphic 9 bp tandem repeat sequence in the first exon. The repeat is present 6 times in the reference genome sequence a…
- **Diseases (Open Targets)**: familial adenomatous polyposis 4 (0.743); endometrial carcinoma (0.651); hereditary neoplastic syndrome (0.576); endometrial cancer (0.374); endometrial neoplasm (0.370)
- **Europe PMC papers**: 4720
- **Why important**: MSH3 occupies a central position in the module graph and has the strongest direct functional anchor to genome maintenance. It forms MutS beta with MSH2 and participates in post-replicative mismatch repair. It also has extensive literature and prominent associations with familial adenomatous polyposis and endometrial neoplasia.
- **Conclusion**: Established evidence supports MSH3 as a mismatch-repair and DNA-integrity gene with substantial disease relevance. It is plausible that its co-abundance marks a proliferative or genome-maintenance state, but the module does not establish that MSH3 drives the shared tissue signal.

#### TRIM33

- **Related proteins** (co-abundance neighbors): DDX31 (0.91), MSH3 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Immune cell enhanced; location Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tripartite motif containing 33. The protein encoded by this gene is thought to be a transcriptional corepressor. However, molecules that interact with this protein have not yet been identified. The protein is a member of the tripartite motif family. This motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. Three alternatively spliced transcript variants for this gene hav…
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); lung carcinoma (0.376); thyroid gland papillary carcinoma (0.374); colorectal adenocarcinoma (0.372); thyroid gland oncocytic adenoma (0.370)
- **Europe PMC papers**: 1635
- **Why important**: TRIM33 is centrally connected within the module and provides a regulatory link to transcription, protein ubiquitination, transforming-growth-factor receptor signaling, and BMP signaling. It has a substantial literature and broad disease associations, including neurodegenerative and malignant conditions.
- **Conclusion**: Established evidence supports TRIM33 as a transcriptional coregulator and signaling modulator. Its position makes it a candidate coordinator of cellular state, but a causal role in this tissue-pair module remains hypothetical because no physical interaction or globally significant enrichment is reported.

#### RBM22

- **Related proteins** (co-abundance neighbors): DDX31 (0.85), TAF6 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 22. This gene encodes an RNA binding protein. The encoded protein may play a role in cell division and may be involved in pre-mRNA splicing. Related pseudogenes exist on chromosomes 6, 7, 9, 13, 16, 18, and X. [provided by RefSeq, Mar 2009].
- **Diseases (Open Targets)**: dengue disease (0.370); neurodegenerative disease (0.358); pneumonitis (0.111); glioblastoma (0.078); anencephaly 1 (0.056)
- **Europe PMC papers**: 353
- **Why important**: RBM22 links the DDX31 branch to TAF6 and supplies a direct RNA-processing component. It is an RNA-binding protein involved in pre-mRNA splicing and has documented associations with cell division and nuclear transport. Its literature is more focused than that of MSH3 or TRIM33, but it is functionally well aligned with the module.
- **Conclusion**: Established evidence supports RBM22 as a splicing-related nuclear regulator. The module may reflect coordinated RNA processing, yet this remains an interpretation of co-abundance rather than proof of a shared spliceosomal complex.

#### RNGTT

- **Related proteins** (co-abundance neighbors): TMPO (0.85), MICALL1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA guanylyltransferase and 5'-phosphatase. Enables mRNA guanylyltransferase activity and triphosphatase activity. Involved in 7-methylguanosine mRNA capping. Predicted to be located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.515); HIV infectious disease (0.503); autoimmune disorder of central nervous system (0.437); alcohol drinking (0.318); liver disorder (0.314)
- **Europe PMC papers**: 311
- **Why important**: RNGTT connects the TMPO region to MICALL1 and represents a specific transcript-maturation function through mRNA capping. It is a nucleoplasmic enzyme with established RNA processing activity and relevant associations spanning neurological, infectious, autoimmune, and liver disorders.
- **Conclusion**: Established evidence supports RNGTT as an mRNA-capping and RNA-processing factor. Its inclusion strengthens the interpretation of a gene-expression maintenance program, but the data do not show that altered capping explains the module.

#### TMPO

- **Related proteins** (co-abundance neighbors): TMPO (0.93), MSH3 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thymopoietin. Through alternative splicing, this gene encodes several distinct LEM domain containing protein isoforms. LEM domain proteins include inner nuclear membrane and intranuclear proteins, and are involved in a variety of cellular functions including gene expression, chromatin organization, and replication and cell cycle control. The encoded alpha isoform is broadly diffuse in the nucleus and contains a…
- **Diseases (Open Targets)**: neurodegenerative disease (0.524); familial isolated dilated cardiomyopathy (0.371); migraine disorder (0.359); alcohol drinking (0.272); iris disorder (0.235)
- **Europe PMC papers**: 1474
- **Why important**: TMPO is a highly connected module member and links nuclear-envelope organization with chromatin, replication, cell-cycle control, and gene regulation. Its protein is detected in kidney, and its annotations include hematopoietic progenitor cell states. It also has substantial literature and disease associations involving neurodegeneration, cardiomyopathy, and migraine.
- **Conclusion**: Established evidence supports TMPO as a nuclear-architecture and genome-regulation factor. It could couple cell-state changes to nuclear organization, but the HPA progenitor annotations also leave open a composition-driven explanation.

## Module 23

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (6)**: DIAPH3, IQGAP3, KNTC1, PKN1, PC, USP8

### Function

The strongest supported function is regulation of small-GTPase-associated cytoskeletal and signaling processes. (GO:MF small GTPase binding; q_global = 0.0147) and (GO:MF GTPase binding; q_global = 0.0236) are the only GO terms passing global correction; both identify DIAPH3, IQGAP3, KNTC1, and PKN1, so this interpretation is not based on a nominal or within-module-only result. DIAPH3 is an actin-remodeling formin, IQGAP3 is linked to actin organization and actomyosin contractile-ring assembly, and PKN1 is a Rho-family-G-protein-activated kinase. Together these genes support a Rho-linked actin, adhesion, and cell-shape program. KNTC1 adds an established chromosome-segregation and spindle-checkpoint function, suggesting that the module may also capture proliferative state or coordinated cytoskeletal remodeling during cell division. PC contributes mitochondrial pyruvate metabolism, while USP8 contributes endosomal sorting and membrane trafficking. Thus, the most defensible overall interpretation is a small-GTPase and actin-regulatory signal associated with proliferative and trafficking-related cellular states, rather than a narrowly defined pathway. The absence of additional globally corrected terms does not invalidate the module.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not strongly characterized as a mature immune-cell module, because the blood-cell specificity annotations are mostly low or absent. However, its tissue and single-cell annotations are strongly skewed toward bone marrow and progenitor-like populations, including erythrocyte, megakaryocyte, monocyte, and neutrophil progenitors, as well as germ-cell stages. Several genes are tissue or cell-type enhanced, while the remainder have low specificity. This pattern raises an important composition explanation: the shared autonomic-nervous-system and kidney signal may partly reflect a shared proliferative or progenitor-associated cell state, or variation in related cell populations, rather than a specialized function of mature autonomic neurons and kidney parenchymal cells. Kidney protein detection is present for PC, USP8, PKN1, and KNTC1, whereas there is no matching HPA tissue for the autonomic-nervous-system comparison. The HPA evidence therefore supports caution about interpreting the module as tissue-specific.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF small GTPase binding | 0.0147 | DIAPH3, IQGAP3, KNTC1, PKN1 |
| GO:MF GTPase binding | 0.0236 | DIAPH3, IQGAP3, KNTC1, PKN1 |

### STRING and hu.MAP

STRING provides supplementary functional support for small-GTPase binding through (STRING Function Small GTPase binding; within-query FDR = 0.0086), which contains the same four genes as (GO:MF small GTPase binding; q_global = 0.0147) and (GO:MF GTPase binding; q_global = 0.0236). However, no high-confidence STRING pairwise interaction is reported among the module genes, and none of the genes has a listed STRING partner in this analysis. Therefore, the co-abundance relationship should not be described as an established physical interaction network. hu.MAP identifies repeated complexes containing KNTC1 and DIAPH3 together in (hu.MAP huMAP3_08936.1) through (hu.MAP huMAP3_11232.1). These complexes are broad and contain many additional proteins, so they establish recurring complex-level co-membership but do not isolate a specific DIAPH3-KNTC1 mechanism or explain the full module. The network topology is consequently more consistent with co-regulated expression or shared cell-state dependence than with a densely documented molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Function Small GTPase binding (FDR = 0.0086, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08936.1 (KNTC1, DIAPH3; 2/13); huMAP3_09053.1 (KNTC1, DIAPH3; 2/25); huMAP3_09114.1 (KNTC1, DIAPH3; 2/30); huMAP3_10202.1 (KNTC1, DIAPH3; 2/52); huMAP3_10287.1 (KNTC1, DIAPH3; 2/53); huMAP3_11232.1 (KNTC1, DIAPH3; 2/78)

### Novelty

This is plausibly a new co-abundance observation for the autonomic-nervous-system and kidney tissue pair, because the module-level relationship is not supported by a corresponding high-confidence STRING interaction network and only the DIAPH3-KNTC1 pair recurs in broad hu.MAP complexes. Nevertheless, it would be incorrect to claim that the biology is wholly novel. Small-GTPase binding, actin remodeling, Rho-linked kinase signaling, chromosome segregation, mitochondrial pyruvate metabolism, and endosomal trafficking are established gene functions. The most defensible novelty claim is therefore the cross-tissue co-abundance of this particular gene combination and its possible coordination across tissue samples. Its interpretation remains vulnerable to shared progenitor or proliferative-cell composition, so absence from interaction databases alone cannot establish a new mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared progenitor or proliferative cell-state program in which small-GTPase signaling coordinates actin remodeling, cell adhesion, and cytokinesis, while KNTC1 supports accurate chromosome segregation. DIAPH3 may provide a cytoskeletal scaffold or remodeling component, PKN1 may transmit Rho-family signals, and IQGAP3 may organize actin and contractile structures. PC could couple this state to mitochondrial anaplerotic and biosynthetic metabolism, while USP8 could couple it to endosomal cargo sorting and membrane signaling. In kidney and autonomic-nervous-system samples, the observed conservation may therefore arise from a shared cell-state or cellular-composition signal rather than a tissue-specific pathway. This hypothesis requires validation with cell-resolved expression, perturbation of the Rho-actin components, and testing of whether the module tracks proliferation or progenitor abundance.

### Important genes

#### DIAPH3

- **Related proteins** (co-abundance neighbors): PKN1 (0.85), PC (0.85), IQGAP3 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Microtubules; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08936.1, huMAP3_09053.1, huMAP3_09114.1, huMAP3_10202.1, huMAP3_10287.1, huMAP3_11232.1
- **Function (MyGene.info)**: diaphanous related formin 3. This gene encodes a member of the diaphanous subfamily of the formin family. Members of this family are involved in actin remodeling and regulate cell movement and adhesion. Mutations in this gene are associated with autosomal dominant auditory neuropathy 1. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss (0.574); smoking initiation (0.376); insomnia (0.342); metabolic syndrome X (0.319); endometriosis (0.314)
- **Europe PMC papers**: 1094
- **Why important**: DIAPH3 has the strongest network position, linking PKN1, PC, and IQGAP3, and it participates in both globally corrected terms (GO:MF small GTPase binding; q_global = 0.0147) and (GO:MF GTPase binding; q_global = 0.0236). Its established function in actin filament polymerization, cytoskeleton organization, cell movement, and adhesion makes it the clearest candidate for connecting the module's small-GTPase signal to cell architecture. It is also represented in every hu.MAP complex reported for the module and has substantial literature, including an established association with autosomal dominant auditory neuropathy.
- **Conclusion**: Established: DIAPH3 is a central co-abundance hub with a documented actin-remodeling role and disease association. Hypothesis: it is a principal organizer of the shared module's cytoskeletal state, but the data do not establish direct physical interactions with the neighboring module genes.

#### PKN1

- **Related proteins** (co-abundance neighbors): DIAPH3 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase N1. The protein encoded by this gene belongs to the protein kinase C superfamily. This kinase is activated by Rho family of small G proteins and may mediate the Rho-dependent signaling pathway. This kinase can be activated by phospholipids and by limited proteolysis. The 3-phosphoinositide dependent protein kinase-1 (PDPK1/PDK1) is reported to phosphorylate this kinase, which may mediate insulin signa…
- **Diseases (Open Targets)**: neurodegenerative disease (0.344); Alzheimer disease (0.300); Parkinson disease (0.296); lysosomal storage disease (0.296); exocrine pancreatic carcinoma (0.273)
- **Europe PMC papers**: 1034
- **Why important**: PKN1 is directly connected to DIAPH3 and appears in both primary GO terms (GO:MF small GTPase binding; q_global = 0.0147) and (GO:MF GTPase binding; q_global = 0.0236) as well as supplementary STRING term (STRING Function Small GTPase binding; within-query FDR = 0.0086). Its established activation by Rho-family small G proteins and its reported role in signaling to the actin cytoskeleton provide a mechanistically coherent link between the enrichment result and cytoskeletal regulation. Its annotations also include protein phosphorylation, epithelial migration, and intracellular signal transduction, with disease associations involving neurological disorders and cancer-related conditions.
- **Conclusion**: Established: PKN1 is a biologically plausible Rho-linked signaling effector within the module. Hypothesis: PKN1 may transmit small-GTPase signals toward DIAPH3-dependent remodeling in the shared cell state, although co-abundance does not demonstrate kinase-substrate or physical interaction relationships here.

#### IQGAP3

- **Related proteins** (co-abundance neighbors): DIAPH3 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoli rim; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IQ motif containing GTPase activating protein 3. Enables calmodulin binding activity and myosin VI light chain binding activity. Predicted to be involved in regulation of actin cytoskeleton organization. Predicted to act upstream of or within several processes, including intracellular signal transduction; positive regulation of macromolecule metabolic process; and positive regulation of mammary gland epithelial cell proliferation. Predicted to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.454); neoplasm (0.113); cancer (0.112); hepatocellular carcinoma (0.112); breast cancer (0.106)
- **Europe PMC papers**: 882
- **Why important**: IQGAP3 is one of the four genes driving (GO:MF small GTPase binding; q_global = 0.0147), (GO:MF GTPase binding; q_global = 0.0236), and (STRING Function Small GTPase binding; within-query FDR = 0.0086), and it is connected to the central DIAPH3 node. Its annotations support actin filament organization, actomyosin contractile-ring assembly, calmodulin binding, and myosin-related function. Its HPA profile is enriched in bone marrow and several progenitor or proliferative cell types, which makes it informative both for the proposed cytoskeletal mechanism and for the possibility that the module reflects cell-state composition.
- **Conclusion**: Established: IQGAP3 is a small-GTPase-associated, actin-related module member with progenitor-enriched expression. Hypothesis: it may help organize contractile or adhesion structures during proliferation, but the current evidence cannot distinguish a causal role from co-expression caused by shared progenitor abundance.

#### KNTC1

- **Related proteins** (co-abundance neighbors): USP8 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_08936.1, huMAP3_09053.1, huMAP3_09114.1, huMAP3_10202.1, huMAP3_10287.1, huMAP3_11232.1
- **Function (MyGene.info)**: kinetochore associated 1. This gene encodes a protein that is one of many involved in mechanisms to ensure proper chromosome segregation during cell division. Experimental evidence indicated that the encoded protein functioned in a similar manner to that of the Drosophila rough deal protein. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.314); osteoarthritis, knee (0.278); osteoarthritis (0.264); preeclampsia (0.178); total knee arthroplasty (0.148)
- **Europe PMC papers**: 576
- **Why important**: KNTC1 is a high-connectivity functional marker in the module because it appears in (GO:MF small GTPase binding; q_global = 0.0147), (GO:MF GTPase binding; q_global = 0.0236), and (STRING Function Small GTPase binding; within-query FDR = 0.0086), and it is repeatedly paired with DIAPH3 in hu.MAP complexes (hu.MAP huMAP3_08936.1) through (hu.MAP huMAP3_11232.1). Its established role in kinetochore assembly, spindle-checkpoint signaling, chromosome segregation, and mitotic exit adds a proliferative dimension that is not explained by actin regulation alone. Its bone-marrow and progenitor-associated HPA pattern reinforces the possibility of a shared dividing-cell state.
- **Conclusion**: Established: KNTC1 marks chromosome-segregation and mitotic machinery and has recurring complex-level co-membership with DIAPH3. Hypothesis: KNTC1 may indicate that the module is coordinated during cell division, with DIAPH3-related cytoskeletal remodeling supporting cytokinesis; the hu.MAP evidence does not prove that these proteins operate together in one complex.

#### PC

- **Related proteins** (co-abundance neighbors): DIAPH3 (0.85), USP8 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyruvate carboxylase. This gene encodes pyruvate carboxylase, which requires biotin and ATP to catalyse the carboxylation of pyruvate to oxaloacetate. The active enzyme is a homotetramer arranged in a tetrahedron which is located exclusively in the mitochondrial matrix. Pyruvate carboxylase is involved in gluconeogenesis, lipogenesis, insulin secretion and synthesis of the neurotransmitter glutamate. Mutations in this …
- **Diseases (Open Targets)**: pyruvate carboxylase deficiency disease (0.818); Congenital lactic acidosis (0.416); pyruvate carboxylase deficiency, infantile form (0.371); pyruvate carboxylase deficiency, benign type (0.370); pyruvate carboxylase deficiency, severe neonatal type (0.370)
- **Europe PMC papers**: 248166
- **Why important**: PC is the bridge between DIAPH3 and USP8 in the co-abundance graph and has kidney protein detection in HPA. Its established mitochondrial role in converting pyruvate to oxaloacetate links the module to anaplerosis, gluconeogenesis, lipogenesis, insulin-related metabolism, and neurotransmitter glutamate synthesis. It is not part of the primary enrichment terms, but its very large literature base and strong metabolic disease annotation make it important for interpreting the module as potentially coupling signaling or proliferation to cellular energy demand.
- **Conclusion**: Established: PC is a mitochondrial metabolic enzyme and a graph bridge, with a documented association with pyruvate carboxylase deficiency. Hypothesis: PC may reflect metabolic support for the shared cell state rather than a direct component of small-GTPase signaling; this metabolic linkage needs independent validation.

## Module 24

**Tissue pair**: autonomic_nervous_system and kidney  
**Genes (5)**: EPB41, NSDHL, MRPS22, TBL2, TRAPPC4

### Function

The module does not support a single statistically established biological function: no GO or KEGG term passed global correction. Its members instead represent several intracellular processes, including cholesterol and sterol biosynthesis through NSDHL, endoplasmic-reticulum to Golgi trafficking and autophagy through TRAPPC4, mitochondrial translation through MRPS22, actin-associated membrane organization through EPB41, and regulatory or stress-response functions reported for TBL2. The co-abundance structure is a short chain-like network linking TBL2 with EPB41 and NSDHL, and EPB41 with TRAPPC4, which is more consistent with a weakly unified expression module than with a demonstrated common biochemical complex.

**Cell composition.** This is not a plasma-protein or secreted-protein module: none of the genes is annotated as secreted. It is also not blood-cell enriched according to HPA, and all genes have low immune-cell specificity. The strongest compositional signal is cell-context specificity rather than a shared tissue-wide program: several genes are enriched in germ-cell populations, while EPB41 is associated with retinal photoreceptor and bipolar-cell populations. TBL2 is tissue enhanced in testis and EPB41 in retina, whereas the remaining genes have low tissue specificity. The module may therefore reflect shared or variable cell-type composition in the sampled tissues rather than a conserved autonomic-nervous-system and kidney pathway. Kidney protein detection is present for several members, but the autonomic-nervous-system protein evidence is unavailable, so tissue-level protein validation is incomplete.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no supplementary STRING enrichment was reported. No hu.MAP complex contains multiple module members. Thus, the co-abundance links are not corroborated here as known physical interactions or as membership in a shared protein complex. The absence of database support does not disprove biological coordination; it indicates that the observed association is primarily an expression-level result and should not be interpreted as a physical molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is a potentially novel co-abundance observation in this tissue-pair analysis because its internal links are not represented by the supplied high-confidence STRING or hu.MAP evidence. However, it cannot be called a newly discovered biological pathway. The lack of globally significant GO or KEGG enrichment, the absence of STRING and hu.MAP support, the small and heterogeneous gene set, and the cell-type-biased HPA pattern all weaken a claim of mechanistic novelty. A defensible conclusion is that the shared co-abundance pattern is dataset-specific or under-characterized, with novelty requiring replication, adjustment for cell composition, and experimental validation.

**Hypothesis.** Hypothesis: the module may report a coordinated cellular-state signal involving membrane and vesicle organization, lipid or sterol handling, mitochondrial protein synthesis, and stress-responsive regulation in particular cell populations shared between the autonomic-nervous-system and kidney samples. TBL2 could link the stress or regulatory state with NSDHL-dependent sterol biology, while EPB41 could connect that state to membrane architecture and TRAPPC4 to intracellular trafficking; MRPS22 may reflect accompanying mitochondrial translational demand. This is a hypothesis rather than an established pathway, because the genes have no globally significant shared annotation and no supporting STRING or hu.MAP relationships.

### Important genes

#### NSDHL

- **Related proteins** (co-abundance neighbors): TBL2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NAD(P) dependent 3-beta-hydroxysteroid dehydrogenase NSDHL. The protein encoded by this gene is localized in the endoplasmic reticulum and is involved in cholesterol biosynthesis. Mutations in this gene are associated with CHILD syndrome, which is a X-linked dominant disorder of lipid metabolism with disturbed cholesterol biosynthesis, and typically lethal in males. Alternatively spliced transcript variants with differing 5' UTR have been found for this ge…
- **Diseases (Open Targets)**: CHILD syndrome (0.805); CK syndrome (0.779); neurodegenerative disease (0.404); hereditary disease (0.188); connective tissue disorder (0.150)
- **Europe PMC papers**: 1567
- **Why important**: NSDHL is the clearest biochemical anchor because it is an endoplasmic-reticulum enzyme in cholesterol and sterol biosynthesis and is linked to CHILD syndrome and other lipid-related disease associations. It has substantial literature support relative to most members and occupies the TBL2-connected end of the co-abundance structure. Its HPA profile is broadly distributed rather than immune or secreted, with cell-type enrichment in several epithelial or reproductive populations.
- **Conclusion**: Established: NSDHL participates in sterol and cholesterol biosynthesis and is disease-associated through disturbed cholesterol metabolism. Established: it is co-abundant with TBL2 in this module. Hypothesis: NSDHL may provide a lipid-homeostasis component of the shared tissue signal, but the data do not establish that sterol metabolism drives the entire module.

#### EPB41

- **Related proteins** (co-abundance neighbors): TBL2 (0.87), TRAPPC4 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: erythrocyte membrane protein band 4.1. The protein encoded by this gene, together with spectrin and actin, constitute the red cell membrane cytoskeletal network. This complex plays a critical role in erythrocyte shape and deformability. Mutations in this gene are associated with type 1 elliptocytosis (EL1). Alternatively spliced transcript variants encoding different isoforms have been described for this gene.[provided by RefSeq, Oct 2…
- **Diseases (Open Targets)**: hereditary elliptocytosis (0.753); neurodegenerative disease (0.513); gout (0.298); schizophrenia (0.207); hereditary disease (0.193)
- **Europe PMC papers**: 1436
- **Why important**: EPB41 is a central connector in the module, linking TBL2 with TRAPPC4. It encodes a membrane-associated erythrocyte band protein involved in the spectrin-actin cytoskeleton, cell-cortex organization, calcium-transport regulation, and response to fluid shear stress. It has the strongest disease and literature support among the module genes, including hereditary elliptocytosis. HPA associates it with the plasma membrane and with retinal and neutrophil-related cell populations, although the overall module is not blood-cell enriched.
- **Conclusion**: Established: EPB41 has membrane-cytoskeletal functions and is associated with hereditary elliptocytosis. Established: it is a topological bridge within the co-abundance subgraph. Hypothesis: it may reflect membrane remodeling or cell-state composition in the samples, but the evidence does not show that it physically binds the other module members.

#### TRAPPC4

- **Related proteins** (co-abundance neighbors): MRPS22 (0.82), EPB41 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: trafficking protein particle complex subunit 4. Involved in autophagy and endoplasmic reticulum to Golgi vesicle-mediated transport. Part of TRAPP complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder with epilepsy, spasticity, and brain atrophy (0.702); glycogen storage disease I (0.570); glycogen storage disease Ib (0.570); congenital disorder of glycosylation, type IIw (0.531); disorder of glycogen metabolism (0.466)
- **Europe PMC papers**: 236
- **Why important**: TRAPPC4 is the second connector in the module, linking EPB41 with MRPS22. It is a component of the TRAPP system and is annotated in endoplasmic-reticulum to Golgi transport, COPII vesicle-coat assembly, autophagy, and vesicle-mediated transport. It also has disease associations involving neurodevelopment, glycogen metabolism, and glycosylation, making it relevant to both tissue contexts. HPA detects the protein in kidney and associates its expression with differentiating germ-cell populations.
- **Conclusion**: Established: TRAPPC4 participates in intracellular trafficking and autophagy-related processes. Established: it occupies a connector position in the observed network. Hypothesis: it could couple membrane or secretory-pathway state to the other module signals, but this proposed coupling is not supported by physical-interaction databases.

#### MRPS22

- **Related proteins** (co-abundance neighbors): TRAPPC4 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial ribosomal protein S22. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: hypotonia with lactic acidemia and hyperammonemia (0.787); 46 XX gonadal dysgenesis (0.631); neurodegenerative disease (0.525); androgenetic alopecia (0.507); hereditary disease (0.495)
- **Europe PMC papers**: 448
- **Why important**: MRPS22 represents mitochondrial biology within the module. It encodes a mitochondrial ribosomal protein required for mitochondrial translation and is associated with mitochondrial and developmental disease phenotypes. It is connected to TRAPPC4 in the co-abundance graph hu.MAP and has HPA cell-type enrichment in late primary spermatocytes, consistent with a potentially cell-state-dependent signal.
- **Conclusion**: Established: MRPS22 contributes to mitochondrial protein synthesis and has disease associations involving mitochondrial or developmental dysfunction. Established: its co-abundance association is with TRAPPC4. Hypothesis: it may indicate altered mitochondrial translational demand in the cell population contributing to the module, but the module does not establish a mitochondrial mechanism.

#### TBL2

- **Related proteins** (co-abundance neighbors): EPB41 (0.87), NSDHL (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transducin beta like 2. This gene encodes a member of the beta-transducin protein family. Most proteins of the beta-transducin family are involved in regulatory functions. This protein is possibly involved in some intracellular signaling pathway. This gene is deleted in Williams-Beuren syndrome, a developmental disorder caused by deletion of multiple genes at 7q11.23. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: gout (0.305); physical activity (0.280); type 2 diabetes mellitus (0.257); Abnormality of the skeletal system (0.243); diabetes mellitus (0.200)
- **Europe PMC papers**: 346
- **Why important**: TBL2 has the highest network connectivity in this small module, linking EPB41 with NSDHL. It is a beta-transducin-family protein with reported regulatory potential and annotations involving the unfolded-protein response, glucose starvation, and hypoxia. It is also deleted in the Williams-Beuren syndrome region and has disease or trait associations involving metabolism and skeletal abnormalities. HPA shows testis enhancement and enrichment in spermatid and primary-spermatocyte populations.
- **Conclusion**: Established: TBL2 has reported regulatory and cellular-stress-related annotations and is the principal network connector to NSDHL and EPB41. Hypothesis: it may coordinate stress or metabolic state with sterol and membrane biology, but its precise role in this module remains uncertain and requires experimental testing.
