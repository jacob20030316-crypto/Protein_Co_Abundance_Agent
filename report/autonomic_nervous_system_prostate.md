# Conserved co-abundance modules: autonomic_nervous_system and prostate

## Module 0

**Tissue pair**: autonomic_nervous_system and prostate  
**Genes (19)**: SFN, AP3B1, COPG2, CIAPIN1, HACL2, HMGA1, JPT1, LYPLA1, MCM7, NME1, PPP4R3A, PPP4C, SNRPB2, RUVBL2, SEC61A1, SRP68, TBC1D15, TPD52, UCHL1

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established pathway-level annotation. Its gene-level evidence instead suggests a mixed intracellular maintenance program linking vesicle and membrane-protein trafficking, endoplasmic-reticulum targeting, protein quality and turnover, DNA-damage control, and cell-state regulation. COPG2 connects the largest portion of the co-abundance subgraph and is annotated for COPI vesicle transport. SEC61A1 and SRP68 provide a coherent endoplasmic-reticulum targeting and translocation axis. PPP4C and PPP4R3A provide a DNA-damage-response and protein-dephosphorylation axis. Other genes connect chromatin, replication, ubiquitin-dependent proteolysis, mitochondrial or metabolic functions, and vesicle biology. These are convergent functional clues, not a globally significant enrichment result.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only SFN is annotated as secreted in other tissues, and the module contains no broad secreted-protein signature. It is also not strongly blood-cell enriched. Most genes have low immune-cell specificity, with only limited immune-cell enhancement or enrichment. The HPA profile is instead mixed, with many genes showing cell-type-enhanced expression in epithelial, trophoblast, germ-cell, ciliated-cell, or progenitor populations and relatively broad tissue specificity for many genes. Prostate protein detection is common among the genes with available measurements, whereas no matching autonomic-nervous-system HPA tissue was available. The shared module may therefore reflect common cellular machinery or shared cell-state composition rather than a prostate-specific or autonomic-neural secretory program. UCHL1 is the notable neural-associated component, with group-enriched brain and pituitary expression, but it is not detected in prostate by the reported HPA evidence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known STRING relationship is PPP4C with PPP4R3A, directly supporting a protein-phosphatase complex. SEC61A1 with SRP68 is also a high-confidence known relationship and supports coupling between the ER translocon and signal-recognition-particle machinery. No STRING functional-enrichment result was reported. hu.MAP independently places PPP4C and PPP4R3A together in two complexes, (hu.MAP huMAP3_11192.1) and (hu.MAP huMAP3_13486.1), although each complex contains many additional proteins and only these two module members. No other hu.MAP complex with multiple module members was reported. Thus, the external interaction evidence validates two local relationships but does not establish one unified physical complex for the whole module. The remaining co-abundance edges may represent coordinated expression, indirect regulation, shared cell composition, or context-specific interactions rather than established protein binding.

**STRING interactions (score >= 0.7)**: 2 of 171 gene pairs: PPP4C–PPP4R3A (0.999); SEC61A1–SRP68 (0.824)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11192.1 (PPP4C, PPP4R3A; 2/15); huMAP3_13486.1 (PPP4C, PPP4R3A; 2/16)

### Novelty

This is a potentially interesting cross-tissue co-abundance pattern, but it cannot be called a new biological complex or a newly discovered pathway. The PPP4C–PPP4R3A and SEC61A1–SRP68 relationships are already supported by established interaction resources, and the two phosphatase subunits occur together in hu.MAP complexes. At the same time, the full module-level combination is not represented by a reported STRING enrichment or a shared hu.MAP complex, and the online search yielded no usable prior report of this exact module. That supports cautious novelty as a tissue-pair-specific co-abundance signature, not proof of biological novelty. Its interpretation is also limited by the absence of globally significant GO or KEGG enrichment and by the possibility of shared cell-state composition.

**Hypothesis.** Hypothesis: the module may represent coordinated maintenance of actively growing or specialized epithelial and reproductive-cell states, in which COPI and ER targeting support protein trafficking, SEC61A1 and SRP68 support membrane and secretory-protein insertion, PPP4C–PPP4R3A regulate DNA-damage responses, and UCHL1, TPD52, and associated trafficking or proteostasis genes tune survival, differentiation, and intracellular remodeling. A shared abundance program of this kind could appear in autonomic nervous system and prostate samples because both contain heterogeneous populations requiring vesicle trafficking, proteostasis, and stress-response machinery. This hypothesis should be tested with cell-resolved data, independent cohorts, protein-level measurements, and perturbation of the nominated genes; co-abundance alone does not establish causality.

### Important genes

#### COPG2

- **Related proteins** (co-abundance neighbors): RUVBL2 (0.87), SRP68 (0.86), TBC1D15 (0.85), CIAPIN1 (0.85), HACL2 (0.84), TPD52 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coat protein complex I subunit gamma 2. Predicted to enable structural molecule activity. Involved in intra-Golgi vesicle-mediated transport. Part of COPI vesicle coat. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.410); skin neoplasm (0.327); Alzheimer disease (0.253); alcohol drinking (0.252); stroke disorder (0.252)
- **Europe PMC papers**: 389
- **Why important**: COPG2 has the strongest network position in the module and connects vesicle-trafficking, ER-associated, metabolic, and proteostasis-related neighbors. It is annotated as a COPI coat component involved in intra-Golgi and Golgi-to-ER transport, and its protein is detected in prostate. Its literature volume is moderate relative to the best-studied module genes, making it a useful candidate for testing whether the module reflects coordinated intracellular trafficking rather than a generic housekeeping signal.
- **Conclusion**: Established evidence supports COPG2 as the principal network connector and as a COPI trafficking component. It is plausible, but unproven, that COPG2 helps organize the module's trafficking-related arm; the co-abundance pattern does not demonstrate that it regulates the other genes.

#### SEC61A1

- **Related proteins** (co-abundance neighbors): NME1 (0.92), RUVBL2 (0.87), SNRPB2 (0.86), LYPLA1 (0.85); STRING partners: SRP68 (0.824)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC61 translocon subunit alpha 1. The protein encoded by this gene belongs to the SECY/SEC61- alpha family. It appears to play a crucial role in the insertion of secretory and membrane polypeptides into the endoplasmic reticulum. This protein found to be tightly associated with membrane-bound ribosomes, either directly or through adaptor proteins. This gene encodes an alpha subunit of the heteromeric SEC61 complex, which also cont…
- **Diseases (Open Targets)**: hyperuricemic nephropathy, familial juvenile type 4 (0.720); immunodeficiency, common variable, 15 (0.529); familial juvenile hyperuricemic nephropathy type 2 (0.515); SEC61A1 deficiency (0.509); severe congenital neutropenia (0.418)
- **Europe PMC papers**: 859
- **Why important**: SEC61A1 occupies a strong network position and connects to NME1, RUVBL2, SNRPB2, and LYPLA1. Its annotated function is the alpha subunit of the ER protein-translocation channel, and its direct STRING relationship with SRP68 gives the module a biologically coherent ER-targeting link. It also has disease associations involving immunodeficiency, neutropenia, and kidney disease and a substantial literature base.
- **Conclusion**: Established evidence supports SEC61A1 as a core ER translocation factor and supports its relationship with SRP68. It may anchor a protein-targeting component of the module, but the data do not show that ER translocation is the dominant module function.

#### PPP4C

- **Related proteins** (co-abundance neighbors): PPP4R3A (0.86), SFN (0.86), TPD52 (0.80); STRING partners: PPP4R3A (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_11192.1, huMAP3_13486.1
- **Function (MyGene.info)**: protein phosphatase 4 catalytic subunit. Enables protein serine/threonine phosphatase activity. Involved in regulation of double-strand break repair via homologous recombination. Located in cytosol; nucleoplasm; and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.432); substance-related disorder (0.166); neoplasm (0.099); breast cancer (0.085); breast carcinoma (0.085)
- **Europe PMC papers**: 473
- **Why important**: PPP4C is connected to PPP4R3A, SFN, and TPD52, and the PPP4C–PPP4R3A edge is the strongest reported STRING relationship. PPP4C is the catalytic subunit of protein phosphatase four and is annotated in homologous-recombination and double-strand-break repair regulation. It is also present with PPP4R3A in both reported hu.MAP complexes and has disease links involving neurodegenerative disease and neoplasia.
- **Conclusion**: Established evidence supports PPP4C as the catalytic component of a known phosphatase relationship with PPP4R3A and as a DNA-damage-response regulator. Its centrality to the entire module remains a hypothesis because the global enrichment analysis did not support a DNA-repair module.

#### UCHL1

- **Related proteins** (co-abundance neighbors): SFN (0.83), RUVBL2 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin C-terminal hydrolase L1. The protein encoded by this gene belongs to the peptidase C12 family. This enzyme is a thiol protease that hydrolyzes a peptide bond at the C-terminal glycine of ubiquitin. This gene is specifically expressed in the neurons and in cells of the diffuse neuroendocrine system. Mutations in this gene may be associated with Parkinson disease.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: early-onset progressive neurodegeneration-blindness-ataxia-spasticity syndrome (0.802); spastic paraplegia 79A, autosomal dominant, with ataxia (0.702); Spastic paraplegia (0.501); young-onset Parkinson disease (0.486); hereditary spastic paraplegia (0.418)
- **Europe PMC papers**: 10149
- **Why important**: UCHL1 provides the clearest tissue-level neural signal, with group-enriched brain and pituitary expression, and is annotated as a ubiquitin hydrolase involved in protein deubiquitination and proteasome-related protein catabolism. It connects SFN and RUVBL2 in the module and has the largest literature volume among the listed genes, with established associations to Parkinson disease and hereditary neurodegenerative disorders.
- **Conclusion**: Established evidence supports UCHL1 as a neural-associated protein-turnover enzyme and disease gene. It may explain part of the autonomic-nervous-system association, but its lack of prostate detection and limited network connectivity argue against treating it as evidence that the whole module is neural.

#### TPD52

- **Related proteins** (co-abundance neighbors): COPG2 (0.83), AP3B1 (0.80), PPP4C (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tumor protein D52. Enables calcium ion binding activity and protein homodimerization activity. Involved in B cell differentiation. Located in endoplasmic reticulum and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: prostate carcinoma (0.393); rheumatoid arthritis (0.347); skin disorder (0.267); cervical carcinoma (0.256); Parkinson disease (0.252)
- **Europe PMC papers**: 1217
- **Why important**: TPD52 connects COPG2, AP3B1, and PPP4C, thereby bridging trafficking, vesicle biology, and the phosphatase arm. It is annotated for calcium binding, secretion, proliferation, and B-cell differentiation, is tissue-enhanced in retina, and is detected in prostate. Its disease associations include prostate carcinoma and rheumatoid arthritis, and it has a substantial literature base.
- **Conclusion**: Established evidence supports TPD52 as a multifunctional vesicle- and cell-state-associated protein with relevance to prostate disease. It is a reasonable bridge candidate for the module, but the data do not establish whether it drives prostate biology or merely reflects the cellular composition of the samples.

## Module 1

**Tissue pair**: autonomic_nervous_system and prostate  
**Genes (49)**: SLC3A2, PGM3, APMAP, ATP1A1, ATG4B, CKAP4, CLASP2, CNOT9, CPNE3, CPSF6, COPS8, DBR1, HSD17B4, EIF2AK2, EIF2B4, GNPNAT1, H1-10, HDGF, HDHD5, HEATR1, CPOX, JPT2, LRBA, IGF2R, MTA2, NAA15, NLN, NUP160, NUP93, PYCR1, PDIA4, PDXDC1, PNPT1, POP1, PRDX4, PSIP1, PSPC1, PPAT, RBM12, RFC3, SEC63, TBL2, ACAT1, TIA1, TIMM8A, SLC25A1, UBA6, UBE4A, ATP6V1A

### Function

No GO/KEGG term passed global correction, and there are no supplementary STRING enrichment terms. Therefore, the module does not support a single statistically established pathway-level annotation. Its gene content instead suggests a broad cellular maintenance and proteostasis program spanning RNA processing and nuclear organization, nucleocytoplasmic transport, mitochondrial and intermediary metabolism, protein translocation and folding in the endoplasmic reticulum, redox control, and membrane or vesicle functions. The higher-connectivity genes link several of these processes, but the network does not establish one unified biochemical pathway. The most defensible interpretation is a conserved cellular-state module rather than a tissue-specific autonomic or prostate pathway.

**Cell composition.** The HPA profile is dominated by low tissue specificity and low immune-cell specificity, arguing against a module composed primarily of plasma proteins, secreted proteins, or blood-cell markers. Only a small secreted component is identified. Enhanced expression in liver, pancreas, brain, testis, and reproductive cell types is dispersed rather than defining a coherent autonomic-nervous-system or prostate identity. Some genes are enhanced in hepatocytes, spermatogenic cells, trophoblasts, or myeloid populations, so sample cellular composition could contribute to parts of the signal. Overall, however, the profile is more consistent with broadly expressed intracellular proteins than with a blood-contamination module. Prostate protein detection is common among the measured genes, whereas matching HPA protein data are unavailable for autonomic nervous system, so tissue-specific interpretation remains asymmetric.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a few high-confidence pairwise relationships: CPSF6--PSPC1, GNPNAT1--PGM3, and NUP160--NUP93. These support established links involving nuclear RNA or paraspeckle biology, hexosamine and glycosylation-related metabolism, and the nuclear pore, but they do not explain most of the co-abundance subgraph. hu.MAP supplies additional partial complex evidence. SLC3A2 and APMAP form the complete observed subset of (hu.MAP huMAP3_08813.1); PYCR1 and PPAT occur together in (hu.MAP huMAP3_10767.1); SLC25A1 and NUP93 occur in (hu.MAP huMAP3_09042.1); HDGF and RBM12 occur in (hu.MAP huMAP3_14982.1); PSIP1 and PSPC1 occur in (hu.MAP huMAP3_14270.1); NUP160 and EIF2B4 occur in (hu.MAP huMAP3_10202.1) and (hu.MAP huMAP3_11232.1); IGF2R and PDIA4 occur in (hu.MAP huMAP3_06775.1). Most of these complexes contain many members absent from the module, so they provide contextual support rather than proof that the whole module is a single physical complex. Overall, STRING and hu.MAP indicate several known molecular islands embedded within a broader co-abundance pattern.

**STRING interactions (score >= 0.7)**: 3 of 1176 gene pairs: CPSF6–PSPC1 (0.748); GNPNAT1–PGM3 (0.997); NUP160–NUP93 (0.991)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08813.1 (SLC3A2, APMAP; 2/2); huMAP3_10767.1 (PYCR1, PPAT; 2/8); huMAP3_09042.1 (SLC25A1, NUP93; 2/26); huMAP3_14982.1 (HDGF, RBM12; 2/28); huMAP3_14270.1 (PSIP1, PSPC1; 2/47); huMAP3_10202.1 (NUP160, EIF2B4; 2/52); huMAP3_06775.1 (IGF2R, PDIA4; 2/60); huMAP3_11232.1 (NUP160, EIF2B4; 2/78)

### Novelty

The module should not be called a newly discovered molecular complex or pathway. Its component functions and several relationships are already represented in STRING and hu.MAP, while the absence of database interactions for many co-abundant pairs does not demonstrate novelty. A potentially novel aspect is the reproducible co-abundance of these otherwise distinct functional islands across autonomic nervous system and prostate, but that claim requires replication in independent cohorts, control for cell composition, and comparison with published tissue co-expression modules. The current evidence supports a new candidate cross-tissue association pattern, not a proven novel mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared cellular stress-adaptation and biosynthetic state present in particular cell populations across the two tissue groups. Coordinated activity of mitochondrial and metabolic genes such as CPOX and GNPNAT1, ER folding and redox genes such as PRDX4, and nuclear RNA-processing and transport genes such as CPSF6 and NUP93 could maintain protein synthesis, trafficking, RNA handling, and oxidative balance during changing metabolic or secretory demand. This hypothesis is consistent with the mixed subcellular annotations and partial STRING or hu.MAP connections, but it is not established by enrichment because no globally significant GO/KEGG term passed global correction. It should be tested by cell-resolved expression, perturbation of the proposed hub genes, and measurement of RNA processing, mitochondrial function, ER stress, and redox phenotypes.

### Important genes

#### CPSF6

- **Related proteins** (co-abundance neighbors): CPOX (0.89), NUP93 (0.89), RBM12 (0.88), UBA6 (0.86), GNPNAT1 (0.85), NAA15 (0.82), POP1 (0.82), PSPC1 (0.81); STRING partners: PSPC1 (0.748)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cleavage and polyadenylation specific factor 6. The protein encoded by this gene is one subunit of a cleavage factor required for 3' RNA cleavage and polyadenylation processing. The interaction of the protein with the RNA is one of the earliest steps in the assembly of the 3' end processing complex and facilitates the recruitment of other processing factors. The cleavage factor complex is composed of four polypeptides. This gene encodes the 68k…
- **Diseases (Open Targets)**: cancer (0.579); neurodegenerative disease (0.463); Abnormality of the skeletal system (0.451); smoking initiation (0.424); leukemia (0.376)
- **Europe PMC papers**: 1665
- **Why important**: CPSF6 is among the more highly connected genes in the module and links CPOX, GNPNAT1, RBM12, NAA15, NUP93, PSPC1, and other module members. Its established function is as a cleavage and polyadenylation factor involved in messenger RNA three-prime-end processing, RNA export, and alternative polyadenylation. The STRING relationship with PSPC1 supports a nuclear RNA-processing connection. It has substantial literature and disease-area associations, including cancer and neurodegenerative disease.
- **Conclusion**: Established evidence supports CPSF6 as a central nuclear RNA-processing component and as part of a known relationship with PSPC1. Its connectivity supports a coordinating role in the module, but co-abundance alone does not show that CPSF6 regulates the other module genes. A role in coupling RNA maturation to the broader metabolic and stress-related state remains a hypothesis.

#### NUP93

- **Related proteins** (co-abundance neighbors): CPSF6 (0.89), CPOX (0.83), PDIA4 (0.82), NAA15 (0.82), GNPNAT1 (0.80); STRING partners: NUP160 (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09042.1
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 is a highly connected nuclear-pore gene linked in the module to CPSF6, CPOX, PDIA4, NAA15, and GNPNAT1. Its established functions include nuclear import, nucleocytoplasmic transport, nuclear-envelope organization, polyadenylated RNA export, and nuclear-pore assembly. The NUP160--NUP93 relationship is strongly supported by STRING, and their joint placement in hu.MAP context (hu.MAP huMAP3_09042.1), together with NUP160 participation in (hu.MAP huMAP3_10202.1) and (hu.MAP huMAP3_11232.1), gives this branch strong external support. NUP93 also has extensive literature and disease associations involving kidney disease and infection.
- **Conclusion**: Established evidence supports NUP93 as a nuclear-pore and transport component with a known relationship to NUP160. Its position may connect RNA processing and transport to the rest of the module, but the module does not establish altered nuclear transport as its defining function.

#### GNPNAT1

- **Related proteins** (co-abundance neighbors): NLN (0.91), RBM12 (0.88), CPOX (0.87), NAA15 (0.87), CPSF6 (0.85), PSPC1 (0.85), TIMM8A (0.82), HDGF (0.82), NUP93 (0.80); STRING partners: PGM3 (0.997)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glucosamine-phosphate N-acetyltransferase 1. Enables identical protein binding activity. Predicted to be involved in UDP-N-acetylglucosamine biosynthetic process. Predicted to act upstream of or within cellular response to leukemia inhibitory factor. Predicted to be located in late endosome. Predicted to be active in Golgi apparatus; endoplasmic reticulum; and endoplasmic reticulum-Golgi intermediate compartment. [provided by Alliance of Gen…
- **Diseases (Open Targets)**: rhizomelic dysplasia, Ain-Naz type (0.520); Alzheimer disease (0.217); endocarditis (0.189); myalgic encephalomeyelitis/chronic fatigue syndrome (0.188); clubfoot (0.185)
- **Europe PMC papers**: 379
- **Why important**: GNPNAT1 is among the most connected genes and links CPOX, RBM12, NAA15, CPSF6, PSPC1, TIMM8A, and HDGF. It is associated with UDP-N-acetylglucosamine biosynthesis and with Golgi and endoplasmic-reticulum-related cellular localization. Its STRING relationship with PGM3 provides a known metabolic connection relevant to glycan precursor production. HPA shows liver enhancement and cell-type enhancement in hepatocytes and other secretory or reproductive populations, while prostate protein detection supports its presence in one tissue under study.
- **Conclusion**: Established evidence supports GNPNAT1 as a metabolic and glycosylation-related component with a known relationship to PGM3. Its central network position makes it a plausible bridge between metabolism and protein or membrane processing, but any claim that it drives the cross-tissue module is currently hypothetical.

#### CPOX

- **Related proteins** (co-abundance neighbors): COPS8 (0.94), CPSF6 (0.89), NLN (0.89), NAA15 (0.88), GNPNAT1 (0.87), UBA6 (0.86), RBM12 (0.84), NUP93 (0.83), IGF2R (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Not detected in immune cells; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coproporphyrinogen oxidase. The protein encoded by this gene is the sixth enzyme of the heme biosynthetic pathway. The encoded enzyme is soluble and found in the intermembrane space of mitochondria. This enzyme catalyzes the stepwise oxidative decarboxylation of coproporphyrinogen III to protoporphyrinogen IX, a precursor of heme. Defects in this gene are a cause of hereditary coproporphyria (HCP).[provided by RefSeq, Oct 20…
- **Diseases (Open Targets)**: hereditary coproporphyria (0.823); harderoporphyria (0.771); neurodegenerative disease (0.526); CPOX-related hereditary coproporphyria (0.519); hereditary disease (0.470)
- **Europe PMC papers**: 1085
- **Why important**: CPOX has the strongest network connectivity in the supplied module and links metabolic, RNA-processing, transport, and ubiquitin-related neighbors. It encodes the mitochondrial coproporphyrinogen oxidase of the heme biosynthetic pathway and is associated with hereditary coproporphyria and other disease annotations. Its mitochondrial localization and relationship to heme production provide a biologically distinct axis from the nuclear and ER components. It has substantial literature and is not merely a poorly characterized network node.
- **Conclusion**: Established evidence supports CPOX as a mitochondrial heme-biosynthesis enzyme and as a prominent co-abundance hub. The module does not establish heme biosynthesis as a globally enriched pathway, so the proposed connection between heme or mitochondrial state and the other module branches remains a hypothesis.

#### PRDX4

- **Related proteins** (co-abundance neighbors): PNPT1 (0.89), ATG4B (0.87), APMAP (0.86), TIMM8A (0.86); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peroxiredoxin 4. The protein encoded by this gene is an antioxidant enzyme and belongs to the peroxiredoxin family. The protein is localized to the cytoplasm. Peroxidases of the peroxiredoxin family reduce hydrogen peroxide and alkyl hydroperoxides to water and alcohol with the use of reducing equivalents derived from thiol-containing donor molecules. This protein has been found to play a regulatory role in the ac…
- **Diseases (Open Targets)**: Neurodevelopmental delay (0.118); neoplasm (0.113); cancer (0.097); lung adenocarcinoma (0.096); gastric cancer (0.095)
- **Europe PMC papers**: 1836
- **Why important**: PRDX4 connects PNPT1, ATG4B, APMAP, and TIMM8A and is annotated as an antioxidant enzyme involved in hydrogen-peroxide removal, redox homeostasis, and oxidative-stress responses. HPA places it in the endoplasmic reticulum and shows tissue enrichment in pancreas with enhancement in hepatocytes, pancreatic acinar cells, reproductive cells, and epididymal cells; prostate protein detection is also reported. Its position links ER or redox biology to mitochondrial RNA handling, autophagy, membrane-associated proteins, and protein-folding contexts.
- **Conclusion**: Established evidence supports PRDX4 as an ER-associated redox and oxidative-stress factor with a plausible connection to protein-folding demand. Its module position is compatible with a stress-adaptation interpretation, but it does not prove that oxidative stress organizes the entire shared module.

## Module 2

**Tissue pair**: autonomic_nervous_system and prostate  
**Genes (47)**: SLC1A5, ALG2, NUDT2, HSPA5, CISD1, CDK5RAP3, CPNE1, CUL4A, DDX5, ECHS1, ECI1, ERLIN2, ERO1A, FKBP2, HDGFL2, HEXB, ME2, IMMT, MRE11, MTX1, NDUFA10, NDUFS1, NDUFS2, PDHB, OPA1, PITRM1, UQCRC1, RPA3, RMDN3, RRBP1, SEC24D, SCARB2, PHGDH, HM13, SPR, STT3A, SUCLA2, AARS1, ACAA1, TIAL1, TIMM50, TMTC3, TOMM40, TTLL12, UBQLN2, UNC45A, WDR26

### Function

No GO or KEGG term passed global correction, so those resources provide no primary enrichment evidence for this module. The functional interpretation instead rests on the gene annotations, network structure, STRING evidence, and hu.MAP complexes. The strongest coherent signal is mitochondrial proteostasis and energy metabolism: mitochondrial protein import and membrane organization are represented by TOMM40, TIMM50, MTX1, IMMT, and OPA1; respiratory-chain activity is represented by NDUFS1, NDUFS2, NDUFA10, and UQCRC1; and central or lipid-associated metabolism is represented by PDHB, SUCLA2, ECHS1, ECI1, ACAA1, and ME2. ER and protein-quality-control genes, including HSPA5, ERO1A, STT3A, HM13, and ERLIN2, suggest an ER–mitochondrial proteostasis component. The co-abundance structure therefore most plausibly reflects coordinated mitochondrial import, respiratory function, metabolic substrate use, and membrane or protein-quality maintenance rather than a narrowly defined pathway. The absence of globally enriched GO or KEGG terms does not invalidate this interpretation.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a minority as secreted, and the listed proteins are predominantly intracellular or membrane-associated. It is also not strongly blood-cell enriched. Most genes have low immune-cell specificity, although a subset shows immune-cell enhancement or group enrichment, particularly genes such as SCARB2, SPR, FKBP2, PHGDH, and RRBP1. Many genes have low tissue specificity, consistent with broadly used cellular machinery, while tissue-enhanced signals occur in muscle, tongue, esophagus, liver, parathyroid gland, and other tissues. This composition argues against interpreting the shared module primarily as a plasma-protein or blood-contamination signature. It is compatible with a conserved cellular program present in multiple cell types, potentially influenced by the abundance of metabolically active or secretory cells. HPA protein detection supports broad representation in prostate, whereas no matching HPA tissue was available for autonomic nervous system.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports several established mitochondrial relationships. The most coherent cluster contains NDUFS1, NDUFS2, NDUFA10, and UQCRC1, with strong links among respiratory-chain components; PDHB, SUCLA2, and ME2 connect central carbon metabolism to this cluster. ACAA1, ECHS1, and ECI1 form a fatty-acid oxidation-related relationship set. IMMT, MTX1, TOMM40, and TIMM50 provide established mitochondrial membrane, import, and cristae-associated links, while ERO1A–HSPA5 supports an ER protein-folding relationship. hu.MAP independently places NDUFS1, NDUFS2, NDUFA10, and UQCRC1 together across several respiratory-complex models (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1), and places ECHS1 with ECI1 (hu.MAP huMAP3_12099.1). Additional hu.MAP links connect TIMM50 with UNC45A, ME2 with SCARB2 or AARS1, STT3A with HM13, and ERLIN2 with RMDN3 (hu.MAP huMAP3_08568.1) (hu.MAP huMAP3_05184.1) (hu.MAP huMAP3_09247.1) (hu.MAP huMAP3_08042.1) (hu.MAP huMAP3_09904.1) (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_07410.1) (hu.MAP huMAP3_14442.1) (hu.MAP huMAP3_10725.1) (hu.MAP huMAP3_06247.1) (hu.MAP huMAP3_09592.1). Thus, part of the module recapitulates known physical or functional complexes, especially mitochondrial respiratory machinery and fatty-acid metabolism. The remaining co-abundance edges may represent shared regulation, organelle coupling, cell composition, or indirect relationships rather than direct physical interactions.

**STRING interactions (score >= 0.7)**: 23 of 1081 gene pairs: ACAA1–ECHS1 (0.977); ACAA1–ECI1 (0.825); ACAA1–SUCLA2 (0.86); ECHS1–ECI1 (0.855); ERO1A–HSPA5 (0.875); IMMT–MTX1 (0.965); IMMT–NDUFS1 (0.901); IMMT–NDUFS2 (0.735); IMMT–TOMM40 (0.961); ME2–PDHB (0.948); MTX1–TOMM40 (0.95); NDUFA10–NDUFS1 (0.999); NDUFA10–NDUFS2 (0.999); NDUFA10–UQCRC1 (0.996); NDUFS1–NDUFS2 (0.999); NDUFS1–PDHB (0.809); NDUFS1–SUCLA2 (0.777); NDUFS1–UQCRC1 (0.998); NDUFS2–SUCLA2 (0.837); NDUFS2–UQCRC1 (0.999); PDHB–SUCLA2 (0.921); PDHB–UQCRC1 (0.826); TIMM50–TOMM40 (0.971)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Integral component of membrane (FDR = 0.0035, 21 genes); Keyword Transit peptide (FDR = 0.0126, 14 genes); Keyword Mitochondrion (FDR = 0.0137, 18 genes); Keyword Transmembrane (FDR = 0.0252, 14 genes); Component Mitochondrion (FDR = 0.0414, 21 genes); Component Mitochondrial protein-containing complex (FDR = 0.043, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14018.1 (NDUFS2, NDUFA10, NDUFS1, UQCRC1; 4/48); huMAP3_09982.1 (NDUFS2, NDUFA10, NDUFS1, UQCRC1; 4/49); huMAP3_06397.1 (NDUFS2, NDUFA10, NDUFS1; 3/49); huMAP3_09567.1 (NDUFS2, NDUFA10, NDUFS1; 3/52); huMAP3_14878.1 (NDUFS2, NDUFA10, NDUFS1; 3/53); huMAP3_12099.1 (ECHS1, ECI1; 2/2); huMAP3_07653.1 (NDUFA10, NDUFS1; 2/7); huMAP3_08568.1 (TIMM50, UNC45A; 2/7); huMAP3_05184.1 (ME2, SCARB2; 2/9); huMAP3_09247.1 (TIMM50, UNC45A; 2/9); huMAP3_08042.1 (ME2, SCARB2; 2/13); huMAP3_09904.1 (SLC1A5, CISD1; 2/22); huMAP3_02819.1 (NDUFA10, NDUFS1; 2/34); huMAP3_07410.1 (STT3A, HM13; 2/35); huMAP3_14442.1 (ME2, AARS1; 2/57); huMAP3_10725.1 (ERLIN2, RMDN3; 2/59); huMAP3_06247.1 (STT3A, HM13; 2/65); huMAP3_09592.1 (STT3A, HM13; 2/95)

### Novelty

The module should not be described as a newly discovered mitochondrial complex or pathway, because many of its central relationships are already represented in STRING and hu.MAP. Its potentially novel aspect is the reproducible co-abundance organization shared by autonomic nervous system and prostate, particularly the combination of respiratory-chain, mitochondrial-import, ER-quality-control, and metabolic genes in one tissue-pair module. That claim remains provisional because co-abundance is not equivalent to physical interaction or causation, and the supplied evidence does not include an external replication cohort, perturbation experiment, or comparison with previously reported tissue modules. Lack of a STRING or hu.MAP relationship is not evidence of novelty. The most defensible conclusion is that this is a potentially novel tissue-pair co-abundance configuration built partly from well-established biology.

**Hypothesis.** Hypothesis: the shared module reflects a conserved organelle-maintenance program that coordinates mitochondrial protein import and cristae organization with respiratory-chain assembly, pyruvate and fatty-acid metabolism, ER folding, glycosylation, and quality control. In autonomic nervous system and prostate, variation in the abundance of metabolically active or secretory cells could produce coordinated expression of this program. TOMM40 and TIMM50 may couple precursor import to mitochondrial respiratory capacity, while MTX1, IMMT, and OPA1 may help preserve mitochondrial membrane architecture. ER genes such as HSPA5, ERO1A, STT3A, and HM13 could reflect the parallel burden of membrane-protein maturation and stress control. This is a mechanistic model, not an established causal explanation; it should be tested by cell-type-resolved measurements, independent tissue cohorts, and perturbation of mitochondrial import or ER proteostasis followed by assessment of respiratory and co-abundance effects.

### Important genes

#### NDUFS1

- **Related proteins** (co-abundance neighbors): TTLL12 (0.87), MTX1 (0.86), UQCRC1 (0.82), ME2 (0.81), TOMM40 (0.80); STRING partners: IMMT (0.901), NDUFA10 (0.999), NDUFS2 (0.999), PDHB (0.809), SUCLA2 (0.777), UQCRC1 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_09982.1, huMAP3_06397.1, huMAP3_09567.1, huMAP3_14878.1, huMAP3_07653.1, huMAP3_02819.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S1. The protein encoded by this gene belongs to the complex I 75 kDa subunit family. Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Thi…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 5 (0.810); mitochondrial complex I deficiency (0.647); type 2 diabetes mellitus (0.608); Parkinson disease (0.603); diabetes mellitus (0.580)
- **Europe PMC papers**: 2567
- **Why important**: NDUFS1 is a high-connectivity module gene and a core respiratory-chain complex I component. It has strong STRING links to NDUFA10, NDUFS2, UQCRC1, IMMT, PDHB, and SUCLA2, and it recurs across multiple hu.MAP respiratory-complex models (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1), (hu.MAP huMAP3_07653.1), and (hu.MAP huMAP3_02819.1). Its HPA profile is enhanced in heart muscle, skeletal muscle, and tongue, and its disease associations include complex I deficiency, mitochondrial disease, Parkinson disease, and diabetes. Its substantial literature supports an established role in electron transfer and mitochondrial ATP production.
- **Conclusion**: Established evidence supports NDUFS1 as a central respiratory-chain anchor of the module. Its position and annotations make it a strong marker of mitochondrial energy capacity. It is not evidence by itself that the shared module causes neurological or prostate disease.

#### NDUFS2

- **Related proteins** (co-abundance neighbors): TTLL12 (0.88), TOMM40 (0.87), SLC1A5 (0.87), TMTC3 (0.87), MTX1 (0.85), PDHB (0.84), SPR (0.82), ERLIN2 (0.82), TIMM50 (0.81), RPA3 (0.81); STRING partners: IMMT (0.735), NDUFA10 (0.999), NDUFS1 (0.999), SUCLA2 (0.837), UQCRC1 (0.999)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_09982.1, huMAP3_06397.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S2. The protein encoded by this gene is a core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (complex I). Mammalian mitochondrial complex I is composed of at least 43 different subunits, 7 of which are encoded by the mitochondrial genome, and the rest are the products of nuclear genes. The iron-sulfur protein fraction of complex I is made up of 7 subunits, including this g…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.758); mitochondrial complex I deficiency, nuclear type 6 (0.665); type 2 diabetes mellitus (0.608); mitochondrial disease (0.596); Parkinson disease (0.588)
- **Europe PMC papers**: 1723
- **Why important**: NDUFS2 is among the most connected genes in the module and is a core complex I subunit. It has very strong STRING relationships with NDUFA10, NDUFS1, and UQCRC1, and appears in several hu.MAP respiratory-complex models (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1), (hu.MAP huMAP3_02819.1). It connects in the module to TOMM40, MTX1, PDHB, SUCLA2, and ER-associated genes, linking respiratory machinery to the broader organelle network. Its annotations include complex I assembly, mitochondrial electron transport, and ATP synthesis, with disease associations involving complex I deficiency, mitochondrial disease, diabetes, and Parkinson disease.
- **Conclusion**: Established evidence identifies NDUFS2 as a respiratory-chain core gene and a major network-supported anchor. A reasonable hypothesis is that its co-abundance tracks respiratory-complex integrity in both tissues, but the module data do not establish altered complex I activity.

#### TOMM40

- **Related proteins** (co-abundance neighbors): SLC1A5 (0.95), TIMM50 (0.93), AARS1 (0.89), TTLL12 (0.89), NDUFS2 (0.87), MTX1 (0.85), ECHS1 (0.84), ERO1A (0.83), HSPA5 (0.81), NDUFS1 (0.80); STRING partners: IMMT (0.961), MTX1 (0.95), TIMM50 (0.971)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translocase of outer mitochondrial membrane 40. The protein encoded by this gene is localized in the outer membrane of the mitochondria. It is the channel-forming subunit of the translocase of the mitochondrial outer membrane (TOM) complex that is essential for import of protein precursors into mitochondria. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Aug 2015].
- **Diseases (Open Targets)**: Alzheimer disease (0.325); dementia (0.269); metabolic syndrome (0.262); chronic kidney disease (0.224); Lewy body dementia (0.205)
- **Europe PMC papers**: 2387
- **Why important**: TOMM40 is a highly connected mitochondrial membrane gene linking SLC1A5, TIMM50, MTX1, IMMT, NDUFS2, ERO1A, and metabolic genes. STRING supports relationships with IMMT, MTX1, and TIMM50, while the functional annotation identifies TOMM40 as the channel-forming component of the outer-membrane translocase that imports mitochondrial precursor proteins. It has broad tissue specificity, prostate protein detection, extensive literature, and disease associations including Alzheimer disease, dementia, metabolic syndrome, and kidney disease.
- **Conclusion**: Established evidence supports TOMM40 as the module's mitochondrial entry-point component and a bridge between import machinery and respiratory biology. Its network position makes it important for interpreting the module as an organelle-coordination signal, although co-abundance does not demonstrate altered import flux.

#### TIMM50

- **Related proteins** (co-abundance neighbors): AARS1 (0.93), TOMM40 (0.93), TTLL12 (0.89), SLC1A5 (0.88), UBQLN2 (0.87), HM13 (0.85), ECI1 (0.84), NDUFS2 (0.81), PITRM1 (0.81), OPA1 (0.80); STRING partners: TOMM40 (0.971)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_08568.1, huMAP3_09247.1
- **Function (MyGene.info)**: translocase of inner mitochondrial membrane 50. This gene encodes a subunit of the TIM23 inner mitochondrial membrane translocase complex. The encoded protein functions as the receptor subunit that recognizes the mitochondrial targeting signal, or presequence, on protein cargo that is destined for the mitochondrial inner membrane and matrix. This protein may also play a role in maintaining the membrane permeability barrier, and knockdown of thi…
- **Diseases (Open Targets)**: 3-methylglutaconic aciduria type 9 (0.773); neurodegenerative disease (0.519); Mitochondrial encephalopathy (0.425); hereditary disease (0.415); Epileptic encephalopathy (0.370)
- **Europe PMC papers**: 442
- **Why important**: TIMM50 is highly connected and links TOMM40, AARS1, TTLL12, SLC1A5, HM13, ECI1, and NDUFS2. It is supported by STRING relationships and by hu.MAP complexes involving mitochondrial membrane or protein-handling components (hu.MAP huMAP3_08568.1) and (hu.MAP huMAP3_09247.1). Its annotation identifies it as a receptor subunit of the TIM23 inner-membrane translocase, with roles in mitochondrial precursor recognition, membrane organization, cytochrome c release, and apoptosis. It is detected in prostate and has disease associations involving mitochondrial encephalopathy, neurodegeneration, and epileptic encephalopathy.
- **Conclusion**: Established evidence supports TIMM50 as a key inner-membrane import and mitochondrial-stability component. Its coordinated abundance with TOMM40 and respiratory genes supports a hypothesis of linked mitochondrial precursor handling and energy machinery, but does not establish a causal direction.

#### OPA1

- **Related proteins** (co-abundance neighbors): PITRM1 (0.90), CISD1 (0.86), MTX1 (0.85), PDHB (0.85), ACAA1 (0.84), IMMT (0.82), TIMM50 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OPA1 mitochondrial dynamin like GTPase. The protein encoded by this gene is a nuclear-encoded mitochondrial protein with similarity to dynamin-related GTPases. The encoded protein localizes to the inner mitochondrial membrane and helps regulate mitochondrial stability and energy output. This protein also sequesters cytochrome c. Mutations in this gene have been associated with optic atrophy type 1, which is a dominantly inherited optic …
- **Diseases (Open Targets)**: autosomal dominant optic atrophy, classic form (0.846); Behr syndrome (0.812); optic atrophy with or without deafness, ophthalmoplegia, myopathy, ataxia, and neuropathy (0.766); mitochondrial DNA depletion syndrome 14B (cardioencephalomyopathic type) (0.745); optic atrophy (0.653)
- **Europe PMC papers**: 12169
- **Why important**: OPA1 connects mitochondrial membrane organization to metabolic genes including PDHB, ACAA1, CISD1, and PITRM1, and also connects to IMMT, MTX1, and TIMM50. Its annotation supports roles in inner-membrane organization, mitochondrial fusion, fission, stability, energy output, and cytochrome c sequestration. It has very extensive literature and strong disease associations with dominant optic atrophy, Behr syndrome, mitochondrial DNA depletion, and related neuromuscular phenotypes. HPA places it in mitochondria with prostate protein detection.
- **Conclusion**: Established evidence supports OPA1 as a mitochondrial architecture and stress-response component that complements the import and respiratory genes. Its presence suggests that membrane structure may be part of the shared program. A direct role in generating the tissue-pair co-abundance pattern remains hypothetical.

## Module 3

**Tissue pair**: autonomic_nervous_system and prostate  
**Genes (33)**: ABCF3, ACSL1, ARFIP2, ATXN2L, CNDP2, CNOT12, CNPY3, DCPS, DCXR, EPB41, GAK, GARS1, GGCT, GRIPAP1, H1-2, IQGAP2, LIMA1, MOV10, PDCD4, PDIA5, PLXNB2, CTPS2, RNASEH2A, SMARCC2, U2SURP, SRRT, TCERG1, TFAM, TOM1, TRAPPC4, UTP20, YLPM1, YTHDF2

### Function

No GO or KEGG term passed global correction, so the module does not have a globally significant pathway annotation. Its gene-level evidence nevertheless points to a predominantly intracellular, nuclear gene-expression and RNA-processing program. TCERG1, DCPS, SRRT, U2SURP, YLPM1, CNOT12, MOV10, ATXN2L and YTHDF2 support transcriptional control, pre-mRNA processing, RNA decay, RNA binding and post-transcriptional regulation. SMARCC2 adds chromatin remodeling, while RNASEH2A and H1-2 connect the module to genome maintenance and chromatin organization. Other branches involve mitochondrial maintenance and metabolism through TFAM, GGCT, CNDP2, ACSL1 and DCXR, and vesicle, membrane or cytoskeletal organization through ARFIP2, TRAPPC4, TOM1, LIMA1, IQGAP2, PLXNB2 and EPB41. The most defensible interpretation is therefore a broad cellular homeostasis module coupling RNA and transcriptional regulation with mitochondrial, metabolic, trafficking and structural processes, rather than a narrowly defined tissue-specific pathway.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module: the HPA summary identifies only a small minority of genes as secreted, and the listed proteins are mainly intracellular or membrane-associated. Most genes have low tissue specificity, which argues against a strongly specialized autonomic-nervous-system or prostate identity. Many genes are cell-type enhanced across diverse epithelial, reproductive, hepatic, muscle, adipose and trophoblast populations, while immune-cell specificity is low for most genes. A subset is associated with neutrophils, monocytes, plasmacytoid dendritic cells or other blood-cell populations, so variable immune or blood-cell contribution could influence the co-abundance signal, but the module is not uniformly blood-cell enriched. The liver-associated HPA pattern and broad expression also make a shared housekeeping or general cellular-state component plausible. Protein detection is broadly present in prostate for nearly all genes with available prostate measurements, whereas matching autonomic-nervous-system HPA protein data are unavailable; this limits tissue-specific interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports only a small connected subset of the module: TCERG1 is linked to SRRT and U2SURP, and SMARCC2 is linked to YLPM1. These relationships are consistent with known RNA-processing, transcriptional and nuclear regulatory connections. The absence of STRING enrichment and the sparse high-confidence interaction map indicate that most co-abundance edges are not independently supported as known physical or functional interactions in this resource. No hu.MAP complex contains multiple module members. Thus, the module is better viewed as a coordinated expression program containing a few established molecular links than as a single experimentally established protein complex.

**STRING interactions (score >= 0.7)**: 3 of 528 gene pairs: SMARCC2–YLPM1 (0.779); SRRT–TCERG1 (0.839); TCERG1–U2SURP (0.741)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact shared co-abundance module may be a new observation in this tissue-pair analysis, but the fact sheet does not establish that it is a new biological mechanism. The sparse STRING support, absence of a multi-member hu.MAP complex and lack of globally significant GO or KEGG enrichment make a claim of a novel pathway premature. Several component functions are already well established, including TCERG1-mediated transcription and splicing, DCPS-mediated mRNA decapping, TFAM-mediated mitochondrial genome maintenance, ACSL1-mediated fatty-acid activation and IQGAP2-mediated cytoskeletal signaling. A stronger novelty claim would require replication in independent cohorts, preservation of the module across datasets, cell-composition adjustment, and experiments showing that the genes act together rather than merely covarying because of shared cellular state.

**Hypothesis.** Hypothesis: this shared module reflects a conserved cellular-maintenance state present in both autonomic nervous system and prostate samples, in which nuclear RNA processing and transcriptional control are coordinated with mitochondrial quality, lipid handling, vesicle trafficking and cytoskeletal organization. TCERG1, DCPS, SRRT, U2SURP and SMARCC2 may form the regulatory core, while TFAM, ACSL1, GGCT and CNDP2 may report metabolic or mitochondrial demands, and ARFIP2, IQGAP2, LIMA1 and related genes may connect that state to membrane and cytoskeletal remodeling. An alternative explanation is that shared broad cell types, low-specificity housekeeping expression or variable immune-cell contribution drive the co-abundance pattern. This hypothesis should be tested by single-cell or spatial analysis, adjustment for blood-cell abundance, and perturbation of the proposed regulatory genes.

### Important genes

#### TCERG1

- **Related proteins** (co-abundance neighbors): RNASEH2A (0.88), ATXN2L (0.88), DCPS (0.88), GGCT (0.87), SMARCC2 (0.82), SRRT (0.81); STRING partners: SRRT (0.839), U2SURP (0.741)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transcription elongation regulator 1. This gene encodes a nuclear protein that regulates transcriptional elongation and pre-mRNA splicing. The encoded protein interacts with the hyperphosphorylated C-terminal domain of RNA polymerase II via multiple FF domains, and with the pre-mRNA splicing factor SF1 via a WW domain. Alternative splicing results in multiple transcripts variants encoding different isoforms. [provided by RefSeq, Jul 2…
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); colorectal cancer (0.336); smoking initiation (0.302); sleep apnea syndrome (0.293); chronic venous hypertension (0.257)
- **Europe PMC papers**: 505
- **Why important**: TCERG1 is among the most topologically central genes in the module and connects several module members, including RNASEH2A, ATXN2L, DCPS, GGCT, SMARCC2 and SRRT. Its established functions in transcriptional elongation, pre-mRNA splicing and RNA polymerase II regulation provide the clearest bridge between the module's nuclear regulatory components. It also has substantial literature coverage and disease links involving neurodegeneration and other complex traits.
- **Conclusion**: Established evidence supports TCERG1 as a plausible regulatory hub for transcription and RNA processing. It is reasonable to treat it as a candidate core gene, but the co-abundance data do not prove that TCERG1 causally coordinates the other module members.

#### DCPS

- **Related proteins** (co-abundance neighbors): SMARCC2 (0.89), TCERG1 (0.88), U2SURP (0.87), GGCT (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: decapping enzyme, scavenger. This gene encodes a member of the histidine triad family of pyrophosphatases that removes short mRNA fragments containing the 5' mRNA cap structure, which appear in the 3' -> 5' mRNA decay pathway, following deadenylation and exosome-mediated turnover. This enzyme hydrolyzes the triphosphate linkage of the cap structure (7-methylguanosine nucleoside triphosphate) to yield 7-methylguanosine monopho…
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.670); neurodegenerative disease (0.574); autoimmune disorder of central nervous system (0.428); response to statin (0.282); urinary system disorder (0.201)
- **Europe PMC papers**: 886
- **Why important**: DCPS is connected to the central TCERG1 region and to SMARCC2, U2SURP and GGCT, placing it at the intersection of RNA decay, splicing and chromatin-associated regulation. Its established role is removal of capped mRNA fragments during nuclear RNA turnover, and it has disease associations involving neurological and immune-related disorders. HPA places it in nucleoplasm and shows tissue enhancement in liver and cell-type enhancement in plasmacytoid dendritic and plasma cells.
- **Conclusion**: Established evidence supports DCPS as a biologically coherent RNA-turnover component of the module. Its immune-cell pattern could also make it sensitive to sample composition, so a tissue-intrinsic role should not be assumed without cell-resolved validation.

#### TFAM

- **Related proteins** (co-abundance neighbors): ACSL1 (0.86), CNDP2 (0.86), CNPY3 (0.85), ARFIP2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transcription factor A, mitochondrial. This gene encodes a key mitochondrial transcription factor containing two high mobility group motifs. The encoded protein also functions in mitochondrial DNA replication and repair. Sequence polymorphisms in this gene are associated with Alzheimer's and Parkinson's diseases. There are pseudogenes for this gene on chromosomes 6, 7, and 11. Alternative splicing results in multiple transcript variant…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome 15 (hepatocerebral type) (0.689); neurodegenerative disease (0.550); stroke disorder (0.191); alcohol drinking (0.189); musculoskeletal system disorder (0.132)
- **Europe PMC papers**: 14423
- **Why important**: TFAM links the module's metabolic branch to mitochondrial transcription, mitochondrial DNA replication and repair, and responses to hypoxia or nutrients. It connects to ACSL1, CNDP2, CNPY3 and ARFIP2, thereby relating mitochondrial maintenance to lipid metabolism, protein handling and membrane organization. TFAM has extensive literature and established associations with mitochondrial disease and neurodegenerative disorders.
- **Conclusion**: Established evidence supports TFAM as an important indicator of mitochondrial state within the module. The hypothesis that mitochondrial stress drives the entire shared module remains unproven and could instead reflect general metabolic variation.

#### ACSL1

- **Related proteins** (co-abundance neighbors): CNDP2 (0.88), TFAM (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 1. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. Several transcript variants enco…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.510); diabetes mellitus (0.501); diabetic neuropathy (0.404); neurodegenerative disease (0.368); menopause (0.334)
- **Europe PMC papers**: 4992
- **Why important**: ACSL1 is connected to TFAM and CNDP2 and provides a direct metabolic link through activation of long-chain fatty acids for lipid synthesis and degradation. HPA shows enhancement in liver, skeletal muscle and adipose tissue and enrichment in neutrophils, while disease associations include diabetes and diabetic neuropathy. Its literature is substantial, making its metabolic function well established.
- **Conclusion**: Established evidence supports ACSL1 as a marker of lipid-handling and metabolic state. Its inclusion may reflect tissue metabolism or neutrophil abundance rather than a specific autonomic-nervous-system to prostate mechanism.

#### IQGAP2

- **Related proteins** (co-abundance neighbors): PDIA5 (0.83), GRIPAP1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Plasma membrane; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IQ motif containing GTPase activating protein 2. This gene encodes a member of the IQGAP family. The encoded protein contains three IQ domains, one calponin homology domain, one Ras-GAP domain and one WW domain. This protein interacts with components of the cytoskeleton, with cell adhesion molecules, and with several signaling molecules to regulate cell morphology and motility. It also acts as a tumor suppressor and has been found to play a role…
- **Diseases (Open Targets)**: prostate carcinoma (0.374); cholelithiasis (0.344); neurodegenerative disease (0.320); alcohol drinking (0.300); escherichia coli infection (0.269)
- **Europe PMC papers**: 1654
- **Why important**: IQGAP2 connects PDIA5 and GRIPAP1 and represents the module's signaling, adhesion and cytoskeletal branch. Its established activities include regulation of actin organization, cell morphology, motility, signaling and innate antiviral responses. It has a prostate-carcinoma association in Open Targets, is detected in prostate, and has substantial literature coverage.
- **Conclusion**: Established evidence supports IQGAP2 as a plausible structural and signaling component with relevance to prostate biology. Its role as a mediator linking the nuclear and metabolic portions of this module is a hypothesis rather than a demonstrated mechanism.

## Module 4

**Tissue pair**: autonomic_nervous_system and prostate  
**Genes (33)**: ABHD14B, AHNAK, SERPINC1, ANXA6, ARRB1, BIN1, CALD1, CAPN1, CAPN2, CBR1, CFL2, DNM2, EEA1, EHD1, EHD4, EXOC7, FERMT2, FLNA, RAP1GDS1, GCLC, HBA1, HSPA4L, LNPK, REXO2, PARVA, PDLIM1, PHPT1, PLEC, RBM3, SEPTIN8, TIGAR, VASP, WDR1

### Function

The module is best interpreted as a contractile, actin-centered membrane and cell-adhesion program. The primary globally corrected evidence supports myofibril and contractile muscle-fiber organization (GO:CC myofibril; q_global = 0.000551), actin-cytoskeleton organization (GO:BP actin cytoskeleton organization; q_global = 0.000564), actin cytoskeleton and actin-filament processes (GO:CC actin cytoskeleton; q_global = 0.00111)(GO:BP actin filament-based process; q_global = 0.00121), sarcomere and Z-disc structure (GO:CC sarcomere; q_global = 0.0123)(GO:CC Z disc; q_global = 0.0181), actomyosin organization (GO:BP actomyosin structure organization; q_global = 0.0183), focal adhesion and cell-substrate junctions (GO:CC focal adhesion; q_global = 0.00499)(GO:CC cell-substrate junction; q_global = 0.00499), and plasma-membrane localization (GO:CC plasma membrane; q_global = 0.0452). This is a coherent structural and mechanical program rather than a pathway defined by a single signaling cascade. The module also contains genes involved in endocytosis, vesicle trafficking, redox control, and RNA or protein quality processes, but these appear to be peripheral or context-dependent features rather than the dominant interpretation. No KEGG term is listed among the supplied globally corrected primary terms. The absence of a specific KEGG term does not invalidate the module.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: SERPINC1 is the supplied secreted-to-blood gene, while most members are intracellular or membrane-associated. HBA1 is an erythrocyte-associated gene and may reflect blood contamination or blood-cell content, particularly because the module also includes platelet- and megakaryocyte-associated signals such as WDR1, VASP, PDLIM1, and FLNA. However, the HPA summary does not support a purely blood-cell explanation: most genes have low tissue specificity, immune-cell specificity is generally low, and the recurrent tissue and cell-type signals include skeletal or smooth muscle, endothelial or stromal-related cells, platelets, megakaryocytes, and epithelial populations. The enrichment of muscle-related genes and prostate protein detection is compatible with a genuine contractile or adhesion program in prostate-associated tissue, while the autonomic-nervous-system comparison may capture shared smooth-muscle, vascular, stromal, or perivascular cellular components. The module should therefore be interpreted as a mixed structural program with possible contributions from shared cell types and blood-related material, not as a blood module by default.

**GO/KEGG enrichment**: 20 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC myofibril | 0.000551 | AHNAK, BIN1, CALD1, CFL2, FERMT2, FLNA, PARVA, PDLIM1, PLEC |
| GO:BP actin cytoskeleton organization | 0.000564 | ARRB1, BIN1, CALD1, CFL2, DNM2, FERMT2, FLNA, PARVA, PDLIM1, PHPT1, PLEC, RAP1GDS1, VASP, WDR1 |
| GO:CC contractile muscle fiber | 0.000687 | AHNAK, BIN1, CALD1, CFL2, FERMT2, FLNA, PARVA, PDLIM1, PLEC |
| GO:CC actin cytoskeleton | 0.00111 | AHNAK, BIN1, CALD1, CAPN2, CFL2, DNM2, FERMT2, FLNA, PARVA, PDLIM1, PLEC, VASP, WDR1 |
| GO:BP actin filament-based process | 0.00121 | ARRB1, BIN1, CALD1, CFL2, DNM2, FERMT2, FLNA, PARVA, PDLIM1, PHPT1, PLEC, RAP1GDS1, VASP, WDR1 |
| GO:CC I band | 0.00215 | BIN1, CFL2, FERMT2, FLNA, PARVA, PDLIM1, PLEC |
| GO:CC anchoring junction | 0.00326 | AHNAK, ANXA6, CAPN1, CAPN2, DNM2, EHD4, FERMT2, FLNA, PARVA, PDLIM1, PLEC, REXO2, VASP, WDR1 |
| GO:CC focal adhesion | 0.00499 | AHNAK, ANXA6, CAPN1, CAPN2, DNM2, FERMT2, FLNA, PARVA, PDLIM1, PLEC, REXO2, VASP |
| GO:CC cell-substrate junction | 0.00499 | AHNAK, ANXA6, CAPN1, CAPN2, DNM2, FERMT2, FLNA, PARVA, PDLIM1, PLEC, REXO2, VASP |
| GO:MF actin binding | 0.00566 | BIN1, CALD1, CFL2, FERMT2, FLNA, PARVA, PDLIM1, PHPT1, PLEC, VASP, WDR1 |
| GO:CC cell junction | 0.00726 | AHNAK, ANXA6, BIN1, CAPN1, CAPN2, DNM2, EEA1, EHD1, EHD4, FERMT2, FLNA, PARVA, PDLIM1, PLEC, REXO2, SEPTIN8, VASP, WDR1 |
| GO:BP actin filament organization | 0.00872 | ARRB1, BIN1, CALD1, CFL2, DNM2, FERMT2, FLNA, PDLIM1, PLEC, VASP, WDR1 |
| GO:BP cytoskeleton organization | 0.0114 | ARRB1, BIN1, CALD1, CAPN2, CFL2, DNM2, FERMT2, FLNA, PARVA, PDLIM1, PHPT1, PLEC, RAP1GDS1, VASP, WDR1 |
| GO:CC sarcomere | 0.0123 | BIN1, CFL2, FERMT2, FLNA, PARVA, PDLIM1, PLEC |
| GO:CC Z disc | 0.0181 | BIN1, CFL2, FLNA, PARVA, PDLIM1, PLEC |

### STRING and hu.MAP

STRING provides independent support for a connected actin, adhesion, membrane-remodeling, and proteolysis framework. Established high-confidence relationships include BIN1-DNM2, CAPN1-CAPN2, CFL2-WDR1, CFL2-FLNA, FERMT2-FLNA, FERMT2-PARVA, FLNA-PLEC, FLNA-VASP, and FLNA-WDR1. STRING compartment annotations converge on cell junctions, focal adhesions, anchoring junctions, myofibrils, I bands, actin cytoskeleton, cell periphery, and plasma membrane (STRING COMPARTMENTS Cell junction; within-query FDR = 8.14e-05)(STRING COMPARTMENTS Focal adhesion; within-query FDR = 0.00014)(STRING COMPARTMENTS Anchoring junction; within-query FDR = 0.00014)(STRING Component Myofibril; within-query FDR = 0.00063)(STRING Component I band; within-query FDR = 0.0011)(STRING Component Cell periphery; within-query FDR = 0.0012)(STRING Component Actin cytoskeleton; within-query FDR = 0.0015)(STRING Component Plasma membrane; within-query FDR = 0.0032)(STRING Component Z disc; within-query FDR = 0.0032)(STRING Function Actin binding; within-query FDR = 0.0058). These are supplementary confirmations and not replacements for the globally corrected enrichment evidence. hu.MAP adds experimentally supported complex-level structure: CFL2-WDR1 occurs in a complete small complex (hu.MAP huMAP3_02272.1); EHD1-EHD4 recur in several endocytic or recycling complexes (hu.MAP huMAP3_04633.1)(hu.MAP huMAP3_03942.1)(hu.MAP huMAP3_07540.1)(hu.MAP huMAP3_10988.1); CAPN1-CAPN2 recur in calpain-related complexes, often with CAPNS1 or other calpain components (hu.MAP huMAP3_03767.1)(hu.MAP huMAP3_08670.1)(hu.MAP huMAP3_09328.1)(hu.MAP huMAP3_10242.1); and WDR1-CFL2 or WDR1-AHNAK occur in larger actin-associated assemblies (hu.MAP huMAP3_06026.1)(hu.MAP huMAP3_11076.1)(hu.MAP huMAP3_09165.1). SERPINC1 and HBA1 occur together in a broad blood-protein complex (hu.MAP huMAP3_15040.1), which reinforces the possibility of a blood-related component but does not define the whole module. Overall, known interactions cover important substructures, while the complete co-abundance module is broader than any single physical complex.

**STRING interactions (score >= 0.7)**: 15 of 528 gene pairs: AHNAK–CAPN1 (0.813); AHNAK–PLEC (0.73); ARRB1–DNM2 (0.727); BIN1–DNM2 (0.992); BIN1–EHD1 (0.708); CAPN1–CAPN2 (0.978); CFL2–FLNA (0.888); CFL2–VASP (0.873); CFL2–WDR1 (0.993); EHD1–EHD4 (0.795); FERMT2–FLNA (0.852); FERMT2–PARVA (0.893); FLNA–PLEC (0.812); FLNA–VASP (0.772); FLNA–WDR1 (0.874)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Cell junction (FDR = 8.14e-05, 15 genes); COMPARTMENTS Focal adhesion (FDR = 0.00014, 12 genes); COMPARTMENTS Anchoring junction (FDR = 0.00014, 13 genes); Component Myofibril (FDR = 0.00063, 9 genes); Component Focal adhesion (FDR = 0.0011, 12 genes); Component I band (FDR = 0.0011, 7 genes); Component Anchoring junction (FDR = 0.0011, 14 genes); Component Cell periphery (FDR = 0.0012, 21 genes); Component Actin cytoskeleton (FDR = 0.0015, 11 genes); COMPARTMENTS Cell periphery (FDR = 0.0018, 16 genes); Component Plasma membrane (FDR = 0.0032, 19 genes); Component Z disc (FDR = 0.0032, 6 genes); COMPARTMENTS Actin cytoskeleton (FDR = 0.0053, 10 genes); Function Actin binding (FDR = 0.0058, 11 genes); Component Cell junction (FDR = 0.0064, 15 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02272.1 (WDR1, CFL2; 2/2); huMAP3_04633.1 (EHD4, EHD1; 2/2); huMAP3_03767.1 (CAPN1, CAPN2; 2/3); huMAP3_03942.1 (EHD4, EHD1; 2/3); huMAP3_07540.1 (EHD4, EHD1; 2/3); huMAP3_08670.1 (CAPN1, CAPN2; 2/4); huMAP3_09127.1 (CAPN1, CAPN2; 2/5); huMAP3_06026.1 (WDR1, CFL2; 2/5); huMAP3_10988.1 (EHD4, EHD1; 2/5); huMAP3_09328.1 (CAPN1, CAPN2; 2/6); huMAP3_10242.1 (CAPN1, CAPN2; 2/6); huMAP3_13615.1 (CAPN1, CAPN2; 2/7); huMAP3_14229.1 (CAPN1, CAPN2; 2/7); huMAP3_11557.1 (CAPN1, CAPN2; 2/8); huMAP3_12716.1 (CAPN1, CAPN2; 2/8); huMAP3_12926.1 (CAPN1, CAPN2; 2/8); huMAP3_08533.1 (TIGAR, PHPT1; 2/9); huMAP3_11076.1 (WDR1, CFL2; 2/10); huMAP3_09165.1 (WDR1, AHNAK; 2/39); huMAP3_15040.1 (SERPINC1, HBA1; 2/64)

### Novelty

The biological theme is not new: actin remodeling, focal adhesion, contractility, endocytosis, calpain activity, and cytoskeletal scaffolding are established functions of the constituent genes. Several relationships and complexes are already represented in STRING and hu.MAP, so the module should not be claimed as a newly discovered protein complex or pathway. The potentially novel aspect is the reproducible co-abundance organization shared by autonomic_nervous_system and prostate, particularly the combination of contractile-fiber, adhesion, membrane-trafficking, redox, and blood-associated features in these tissue groups. That claim requires replication in independent cohorts, control for cell composition and blood contamination, and comparison with previously reported cross-tissue co-expression modules. Absence of some module pairs from STRING or hu.MAP is evidence of incomplete prior coverage, not proof that those relationships are novel.

**Hypothesis.** Hypothesis: the shared module represents a cell-structural remodeling state in contractile, smooth-muscle-like, vascular, stromal, or epithelial-associated cells. Integrin-linked adhesion through FERMT2 and PARVA may couple extracellular attachment to actin through FLNA, PLEC, VASP, and PDLIM1; CFL2 and WDR1 may tune actin filament turnover; BIN1, DNM2, EHD1, and EHD4 may coordinate membrane curvature, endocytosis, and recycling; and CAPN1-CAPN2 may provide calcium-responsive proteolytic remodeling. GCLC, TIGAR, and CBR1 could indicate accompanying management of oxidative or metabolic stress, while SERPINC1 and HBA1 may reflect vascular or blood-derived material. This model predicts that module abundance will track contractile or adhesion-related cell composition and mechanical or injury-related remodeling, rather than representing a single universal pathway operating identically in every cell.

### Important genes

#### FLNA

- **Related proteins** (co-abundance neighbors): FERMT2 (0.91), SERPINC1 (0.87), PARVA (0.81), VASP (0.80); STRING partners: CFL2 (0.888), FERMT2 (0.852), PLEC (0.812), VASP (0.772), WDR1 (0.874)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is a central structural connector in the module, linking actin filaments to membrane glycoproteins and interacting with integrins and receptor complexes. It occupies a strongly connected position in the module and has STRING support with FERMT2, PLEC, VASP, WDR1, and CFL2. It is represented across nearly all primary enrichment themes, including myofibril, actin organization, focal adhesion, junctions, sarcomere, Z disc, and plasma membrane (GO:CC myofibril; q_global = 0.000551)(GO:BP actin cytoskeleton organization; q_global = 0.000564)(GO:CC anchoring junction; q_global = 0.00326)(GO:CC focal adhesion; q_global = 0.00499)(GO:CC sarcomere; q_global = 0.0123)(GO:CC Z disc; q_global = 0.0181)(GO:CC plasma membrane; q_global = 0.0452). Its HPA localization spans plasma membrane, actin filaments, and cytosol, and its disease literature is substantial, including developmental and skeletal syndromes.
- **Conclusion**: Established evidence supports FLNA as a structural hub that can physically and functionally connect the actin, adhesion, and membrane aspects of the module. It is a strong candidate for an organizing component, but the co-abundance data alone do not establish that FLNA controls the shared tissue program.

#### FERMT2

- **Related proteins** (co-abundance neighbors): FLNA (0.91), PARVA (0.88), SERPINC1 (0.86), VASP (0.83), EHD1 (0.80); STRING partners: FLNA (0.852), PARVA (0.893)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Focal adhesion sites; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FERM domain containing kindlin 2. Enables several functions, including actin binding activity; phosphatidylinositol-3,4,5-trisphosphate binding activity; and type I transforming growth factor beta receptor binding activity. Involved in several processes, including cell surface receptor signaling pathway; positive regulation of cell differentiation; and positive regulation of cellular component biogenesis. Acts upstream of or withi…
- **Diseases (Open Targets)**: open-angle glaucoma (0.501); prostate carcinoma (0.488); glaucoma (0.488); neurodegenerative disease (0.473); primary angle-closure glaucoma (0.407)
- **Europe PMC papers**: 1336
- **Why important**: FERMT2 is a high-connectivity module member with links to FLNA, PARVA, SERPINC1, VASP, and EHD1. It is localized to focal adhesion sites and is annotated for cell adhesion, cell-matrix adhesion, integrin-mediated signaling, receptor signaling, and cell-junction localization. It appears in almost every primary enrichment theme, including myofibril, focal adhesion, anchoring junction, actin binding, and plasma membrane (GO:CC myofibril; q_global = 0.000551)(GO:BP actin cytoskeleton organization; q_global = 0.000564)(GO:CC anchoring junction; q_global = 0.00326)(GO:CC focal adhesion; q_global = 0.00499)(GO:MF actin binding; q_global = 0.00566)(GO:CC plasma membrane; q_global = 0.0452). Its HPA profile includes smooth-muscle and podocyte-associated cell types, and its disease associations include prostate carcinoma and glaucoma.
- **Conclusion**: Established evidence makes FERMT2 a plausible adhesion-to-cytoskeleton linker and an important interpreter of the module's mechanical phenotype. Its prostate association is noteworthy, but whether it has a specific role in the shared autonomic-nervous-system and prostate signal remains a hypothesis.

#### CFL2

- **Related proteins** (co-abundance neighbors): CBR1 (0.86), AHNAK (0.85), EHD1 (0.84), VASP (0.83); STRING partners: FLNA (0.888), VASP (0.873), WDR1 (0.993)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_02272.1, huMAP3_06026.1, huMAP3_11076.1
- **Function (MyGene.info)**: cofilin 2. This gene encodes an intracellular protein that is involved in the regulation of actin-filament dynamics. This protein is a major component of intranuclear and cytoplasmic actin rods. It can bind G- and F-actin in a 1:1 ratio of cofilin to actin, and it reversibly controls actin polymerization and depolymerization in a pH-dependent manner. Mutations in this gene cause nemaline myopathy type 7, a f…
- **Diseases (Open Targets)**: nemaline myopathy 7 (0.758); typical nemaline myopathy (0.599); atrial fibrillation (0.525); nemaline myopathy (0.376); Takayasu arteritis (0.303)
- **Europe PMC papers**: 1415
- **Why important**: CFL2 is a muscle-enriched actin-filament regulator that controls actin polymerization, depolymerization, and severing. It is supported by STRING relationships with FLNA, VASP, and WDR1 and by hu.MAP complexes with WDR1 (hu.MAP huMAP3_02272.1)(hu.MAP huMAP3_06026.1)(hu.MAP huMAP3_11076.1). It contributes to the myofibril, I band, sarcomere, Z disc, actin-binding, and actomyosin evidence (GO:CC myofibril; q_global = 0.000551)(GO:CC I band; q_global = 0.00215)(GO:MF actin binding; q_global = 0.00566)(GO:CC sarcomere; q_global = 0.0123)(GO:CC Z disc; q_global = 0.0181)(GO:BP actomyosin structure organization; q_global = 0.0183). HPA identifies enrichment in heart muscle, skeletal muscle, and tongue, with smooth-muscle-associated single-cell expression. Its disease associations include nemaline myopathy and atrial fibrillation.
- **Conclusion**: Established evidence supports CFL2 as a core effector of actin turnover in a contractile or muscle-like structural program. Its presence favors a genuine cytoskeletal interpretation over a purely nonspecific housekeeping explanation, although the precise contributing cell type in each tissue is unresolved.

#### BIN1

- **Related proteins** (co-abundance neighbors): CALD1 (0.83); STRING partners: DNM2 (0.992), EHD1 (0.708)
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: bridging integrator 1. This gene encodes several isoforms of a nucleocytoplasmic adaptor protein, one of which was initially identified as a MYC-interacting protein with features of a tumor suppressor. Isoforms that are expressed in the central nervous system may be involved in synaptic vesicle endocytosis and may interact with dynamin, synaptojanin, endophilin, and clathrin. Isoforms that are expressed in muscle and ub…
- **Diseases (Open Targets)**: myopathy, centronuclear, 2 (0.781); autosomal recessive centronuclear myopathy (0.601); Alzheimer disease (0.553); autosomal dominant centronuclear myopathy (0.507); dementia (0.507)
- **Europe PMC papers**: 5080
- **Why important**: BIN1 connects muscle and membrane biology. It is associated with DNM2 and EHD1 in STRING, is represented in the myofibril, I band, sarcomere, Z-disc, actin, and endocytosis-related annotations, and has strong disease associations with centronuclear myopathies and Alzheimer disease. HPA supports skeletal-muscle and smooth-muscle-related cell contexts as well as several immune-cell populations. Its annotation includes synaptic-vesicle endocytosis, endosome-to-lysosome transport, and cytoskeleton organization.
- **Conclusion**: Established evidence supports BIN1 as a bridge between contractile architecture and membrane remodeling, a particularly relevant interpretation for a module shared across a nervous-system-related tissue group and prostate. The cross-tissue co-abundance pattern may reflect shared membrane-trafficking or contractile cell states, but this remains a hypothesis.

#### PLEC

- **Related proteins** (co-abundance neighbors): RAP1GDS1 (0.89); STRING partners: AHNAK (0.73), FLNA (0.812)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments, Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plectin. Plectin is a prominent member of an important family of structurally and in part functionally related proteins, termed plakins or cytolinkers, that are capable of interlinking different elements of the cytoskeleton. Plakins, with their multi-domain structure and enormous size, not only play crucial roles in maintaining cell and tissue integrity and orchestrating dynamic changes in cytoarchitecture…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 5B, with muscular dystrophy (0.796); epidermolysis bullosa simplex 5A, Ogna type (0.775); autosomal recessive limb-girdle muscular dystrophy type 2Q (0.768); epidermolysis bullosa simplex 5C, with pyloric atresia (0.755); epidermolysis bullosa simplex with nail dystrophy (0.695)
- **Europe PMC papers**: 2578
- **Why important**: PLEC is a large cytolinker that interconnects cytoskeletal systems and provides scaffolding for cell shape and tissue integrity. It is present in every supplied primary enrichment theme, including myofibril, actin organization, focal adhesion, sarcomere, Z disc, actomyosin structure, and plasma membrane (GO:CC myofibril; q_global = 0.000551)(GO:BP actin cytoskeleton organization; q_global = 0.000564)(GO:CC focal adhesion; q_global = 0.00499)(GO:CC sarcomere; q_global = 0.0123)(GO:CC Z disc; q_global = 0.0181)(GO:BP actomyosin structure organization; q_global = 0.0183)(GO:CC plasma membrane; q_global = 0.0452). STRING supports relationships with AHNAK and FLNA, while HPA shows skeletal-muscle tissue enhancement and prostate protein detection. Its disease associations include epidermolysis bullosa and muscular dystrophy.
- **Conclusion**: Established evidence supports PLEC as a broad cytoskeletal scaffold that can integrate the module's contractile, junctional, and membrane features. Because its direct module connectivity is limited in the supplied co-abundance graph, it is better viewed as a biologically important scaffold than as the sole network hub.

## Module 5

**Tissue pair**: autonomic_nervous_system and prostate  
**Genes (41)**: ACO2, MAOA, ASPH, ATP13A1, ATP5PB, ATP5F1C, CMBL, CNOT1, COG1, COX20, SORD, DLG1, GFM1, HACD3, HMOX2, HSDL2, IDH3A, INTS3, L2HGDH, MANF, MBOAT7, APOO, PCYOX1L, PHB2, PIP4K2C, PPCS, PRDX3, UQCRC2, RAB3GAP2, RRP12, RTN3, SEC23B, SCP2, SDHA, SFXN1, SFXN3, DARS2, IARS2, YARS2, TRMT10C, UBA3

### Function

The module is most strongly interpreted as a mitochondrial energy-metabolism and mitochondrial-protein-maintenance module. The primary enrichment evidence consistently places it in the mitochondrion, mitochondrial membrane, mitochondrial envelope, and mitochondrial inner membrane (GO:CC mitochondrial membrane; q_global = 0.0102)(GO:CC mitochondrion; q_global = 0.0138)(GO:CC organelle membrane; q_global = 0.0175)(GO:CC mitochondrial envelope; q_global = 0.0263)(GO:CC mitochondrial inner membrane; q_global = 0.0351). The genes span the tricarboxylic-acid cycle and respiratory chain, ATP synthase, mitochondrial translation, mitochondrial RNA processing, amino-acid transport, redox protection, and mitochondrial membrane organization. This combination suggests coordinated variation in oxidative phosphorylation capacity and the supporting processes needed to build, maintain, and protect mitochondrial respiratory machinery. The organelle-level interpretation is also supported by the STRING mitochondrial annotations (STRING Keyword Mitochondrion; within-query FDR = 2.45e-05)(STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.00024)(STRING Component Mitochondrion; within-query FDR = 0.0024) and by the presence of transport, translation, and inner-membrane components (STRING Keyword Transit peptide; within-query FDR = 0.0056)(STRING Component Mitochondrial inner membrane; within-query FDR = 0.0153)(STRING Component Mitochondrial membrane; within-query FDR = 0.0153)(STRING Component Mitochondrial protein-containing complex; within-query FDR = 0.0355). The module should therefore be viewed as a coordinated mitochondrial state rather than as evidence for one narrowly defined biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only a minority are annotated as secreted to blood, and most proteins have intracellular mitochondrial, cytosolic, endoplasmic-reticulum, vesicular, or nucleolar locations. HPA indicates that low tissue specificity is common, while tissue-enhanced genes are distributed across muscle, tongue, liver, kidney, brain, intestine, adrenal tissue, and other sites. This broad distribution is compatible with a widely used mitochondrial program rather than a prostate-specific program. Most genes have low immune-cell specificity, although subsets show enhancement in neutrophils, basophils, plasmacytoid dendritic cells, and other immune populations. Several genes are also enhanced in enterocytes, parietal cells, adipocytes, or muscle-related cell types. Thus, blood contamination is not the leading explanation, but shared cell-type composition and differences in mitochondrial abundance remain plausible contributors to the conserved co-abundance pattern. Prostate protein detection is broad among the module genes, whereas there is no matching HPA tissue for the autonomic nervous system, so the cross-tissue interpretation should not be treated as direct evidence of identical cellular origin.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrial membrane | 0.0102 | APOO, ATP5F1C, ATP5PB, COX20, DARS2, L2HGDH, MAOA, PHB2, SDHA, SFXN1, SFXN3, SORD, UQCRC2 |
| GO:CC mitochondrion | 0.0138 | ACO2, APOO, ATP5F1C, ATP5PB, COX20, DARS2, GFM1, HSDL2, IARS2, IDH3A, L2HGDH, MAOA, PHB2, PRDX3, SCP2, SDHA, SFXN1, SFXN3, SORD, TRMT10C, UQCRC2, YARS2 |
| GO:CC organelle membrane | 0.0175 | APOO, ASPH, ATP13A1, ATP5F1C, ATP5PB, CNOT1, COG1, COX20, DARS2, DLG1, HACD3, HMOX2, L2HGDH, MAOA, MBOAT7, PHB2, RAB3GAP2, RRP12, RTN3, SDHA, SEC23B, SFXN1, SFXN3, SORD, UQCRC2 |
| GO:CC mitochondrial envelope | 0.0263 | APOO, ATP5F1C, ATP5PB, COX20, DARS2, L2HGDH, MAOA, PHB2, SDHA, SFXN1, SFXN3, SORD, UQCRC2 |
| GO:CC mitochondrial inner membrane | 0.0351 | APOO, ATP5F1C, ATP5PB, COX20, L2HGDH, PHB2, SDHA, SFXN1, SFXN3, UQCRC2 |

### STRING and hu.MAP

STRING provides established relationships among core mitochondrial proteins. Strong connections link ACO2, IDH3A, SDHA, and UQCRC2, while ATP5F1C and ATP5PB form a particularly coherent ATP-synthase-associated pair. DARS2, IARS2, and YARS2 are connected as mitochondrial aminoacyl-tRNA synthetases, and HSDL2 is linked with SCP2 in lipid and oxidative metabolism. These relationships support biological coherence but are supplementary evidence rather than additional globally corrected enrichment evidence. hu.MAP independently places DARS2, GFM1, and IARS2 in mitochondrial translation-related complexes (hu.MAP huMAP3_10525.1)(hu.MAP huMAP3_13468.1)(hu.MAP huMAP3_09668.1), ATP5F1C and ATP5PB in multiple ATP synthase-associated complexes (hu.MAP huMAP3_08716.1)(hu.MAP huMAP3_07476.1)(hu.MAP huMAP3_05994.1)(hu.MAP huMAP3_08393.1)(hu.MAP huMAP3_09775.1)(hu.MAP huMAP3_09307.1)(hu.MAP huMAP3_11095.1), and UQCRC2 with MBOAT7 in a respiratory-chain-associated complex (hu.MAP huMAP3_12457.1). Additional hu.MAP evidence links MBOAT7 and PHB2 in a membrane-associated complex (hu.MAP huMAP3_10725.1). The module therefore contains both known physical or functional protein groupings and co-abundance links that connect them. It is not, however, a single fully reconstructed protein complex.

**STRING interactions (score >= 0.7)**: 19 of 820 gene pairs: ACO2–IDH3A (0.998); ACO2–SDHA (0.975); ACO2–UQCRC2 (0.879); ATP5F1C–ATP5PB (0.999); ATP5F1C–GFM1 (0.77); ATP5F1C–IDH3A (0.814); ATP5F1C–SDHA (0.75); ATP5F1C–UQCRC2 (0.98); ATP5PB–IDH3A (0.735); ATP5PB–SDHA (0.755); ATP5PB–UQCRC2 (0.973); DARS2–IARS2 (0.895); DARS2–YARS2 (0.881); HSDL2–SCP2 (0.704); IARS2–YARS2 (0.919); IDH3A–SDHA (0.819); IDH3A–UQCRC2 (0.713); SDHA–UQCRC2 (0.99); UBA3–YARS2 (0.753)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Mitochondrion (FDR = 2.45e-05, 21 genes); COMPARTMENTS Mitochondrion (FDR = 0.00024, 21 genes); Component Mitochondrion (FDR = 0.0024, 22 genes); Keyword Transit peptide (FDR = 0.0056, 13 genes); Component Mitochondrial inner membrane (FDR = 0.0153, 10 genes); Component Organelle membrane (FDR = 0.0153, 24 genes); Component Mitochondrial membrane (FDR = 0.0153, 12 genes); Component Integral component of organelle membrane (FDR = 0.0317, 7 genes); Keyword Mitochondrion inner membrane (FDR = 0.0333, 8 genes); Component Mitochondrial protein-containing complex (FDR = 0.0355, 8 genes); Keyword Oxidoreductase (FDR = 0.0452, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10525.1 (DARS2, GFM1, IARS2; 3/33); huMAP3_06247.1 (UQCRC2, ATP5PB, HACD3; 3/65); huMAP3_13468.1 (DARS2, GFM1, IARS2; 3/99); huMAP3_09668.1 (DARS2, IARS2; 2/8); huMAP3_08716.1 (ATP5PB, ATP5F1C; 2/15); huMAP3_07476.1 (ATP5PB, ATP5F1C; 2/18); huMAP3_05994.1 (ATP5PB, ATP5F1C; 2/19); huMAP3_08393.1 (ATP5PB, ATP5F1C; 2/19); huMAP3_09775.1 (ATP5PB, ATP5F1C; 2/21); huMAP3_12457.1 (UQCRC2, MBOAT7; 2/31); huMAP3_09307.1 (ATP5PB, ATP5F1C; 2/35); huMAP3_11095.1 (ATP5PB, ATP5F1C; 2/45); huMAP3_10725.1 (MBOAT7, PHB2; 2/59)

### Novelty

The module-level observation may be a new cross-tissue co-abundance result, but the underlying biology is not new. Its central components are established mitochondrial respiratory, ATP-synthase, metabolic, translation, and membrane proteins, and many of their relationships are already represented in STRING or hu.MAP. The absence of a hu.MAP record for several genes does not establish novelty, because incomplete complex coverage and context-specific co-abundance are expected. Conversely, the presence of known interactions does not invalidate the module: the potentially novel aspect is the reproducible conservation of this combined mitochondrial state across autonomic nervous system and prostate co-abundance data. A claim of discovery would require replication in independent cohorts, control for cell composition and mitochondrial abundance, and comparison with published tissue-specific modules. On the present evidence, the appropriate conclusion is a potentially novel tissue-pair co-abundance pattern built from largely established mitochondrial biology.

**Hypothesis.** Hypothesis: variation in mitochondrial respiratory demand or mitochondrial quality control produces a coordinated state across the two tissues. In this model, respiratory-chain and ATP-synthase components work with tricarboxylic-acid-cycle enzymes to determine oxidative-phosphorylation capacity; SFXN1 and SFXN3 regulate mitochondrial serine availability; DARS2 and related translational factors maintain mitochondrial protein synthesis; and PHB2, PRDX3, and membrane-associated factors support cristae organization and protection from oxidative stress. The observed co-abundance could therefore reflect coordinated mitochondrial biogenesis, energetic demand, or stress adaptation rather than direct physical interaction among all module members. This is a testable hypothesis, not a demonstrated causal mechanism.

### Important genes

#### SDHA

- **Related proteins** (co-abundance neighbors): DARS2 (0.87), MAOA (0.87), SFXN3 (0.84), MANF (0.83), HSDL2 (0.83), SFXN1 (0.82), IARS2 (0.81), DLG1 (0.80); STRING partners: ACO2 (0.975), ATP5F1C (0.75), ATP5PB (0.755), IDH3A (0.819), UQCRC2 (0.99)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate dehydrogenase complex flavoprotein subunit A. This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identi…
- **Diseases (Open Targets)**: mitochondrial complex II deficiency, nuclear type 1 (0.813); pheochromocytoma/paraganglioma syndrome 5 (0.790); dilated cardiomyopathy 1GG (0.768); neurodegeneration with ataxia and late-onset optic atrophy (0.761); gastrointestinal stromal tumor (0.743)
- **Europe PMC papers**: 12756
- **Why important**: SDHA has the strongest network position in the supplied module and is present in every primary mitochondrial enrichment term (GO:CC mitochondrial membrane; q_global = 0.0102)(GO:CC mitochondrion; q_global = 0.0138)(GO:CC organelle membrane; q_global = 0.0175)(GO:CC mitochondrial envelope; q_global = 0.0263)(GO:CC mitochondrial inner membrane; q_global = 0.0351). It is a catalytic subunit of succinate dehydrogenase, linking the tricarboxylic-acid cycle to respiratory electron transport. Its STRING links to ACO2, IDH3A, ATP5F1C, ATP5PB, and UQCRC2 connect central metabolism, respiratory-chain function, and ATP synthesis. It also has extensive disease and literature support, including mitochondrial respiratory deficiency and tumor-related associations.
- **Conclusion**: Established conclusion: SDHA is a strong anchor for the module's mitochondrial energy-metabolism interpretation. Hypothesis: its central co-abundance position may mark variation in integrated respiratory capacity, but the data do not establish that SDHA regulates the other genes.

#### ATP5F1C

- **Related proteins** (co-abundance neighbors): RRP12 (0.90), SFXN3 (0.83), ACO2 (0.81), PPCS (0.81); STRING partners: ATP5PB (0.999), GFM1 (0.77), IDH3A (0.814), SDHA (0.75), UQCRC2 (0.98)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08716.1, huMAP3_07476.1, huMAP3_05994.1, huMAP3_08393.1, huMAP3_09775.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit gamma. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: late-onset Alzheimers disease (0.350); scleritis (0.189); diaphragm disorder (0.082); glioblastoma (0.044); external ear disorder (0.042)
- **Europe PMC papers**: 306
- **Why important**: ATP5F1C is present in all primary mitochondrial cellular-component terms (GO:CC mitochondrial membrane; q_global = 0.0102)(GO:CC mitochondrion; q_global = 0.0138)(GO:CC organelle membrane; q_global = 0.0175)(GO:CC mitochondrial envelope; q_global = 0.0263)(GO:CC mitochondrial inner membrane; q_global = 0.0351) and is repeatedly connected by STRING to ATP5PB, UQCRC2, SDHA, IDH3A, and GFM1. hu.MAP places it with ATP5PB in multiple ATP-synthase-associated complexes (hu.MAP huMAP3_08716.1)(hu.MAP huMAP3_07476.1)(hu.MAP huMAP3_05994.1)(hu.MAP huMAP3_08393.1)(hu.MAP huMAP3_09775.1)(hu.MAP huMAP3_09307.1)(hu.MAP huMAP3_11095.1). Its annotated function in oxidative phosphorylation and proton-motive-force driven ATP synthesis makes it a direct indicator of mitochondrial energy conversion.
- **Conclusion**: Established conclusion: ATP5F1C represents the ATP-synthesis arm of the module and is supported by both network and complex evidence. Hypothesis: its co-abundance may report coordinated assembly or abundance of ATP synthase with upstream respiratory machinery.

#### DARS2

- **Related proteins** (co-abundance neighbors): HSDL2 (0.90), L2HGDH (0.87), SDHA (0.87), IDH3A (0.82), SCP2 (0.81); STRING partners: IARS2 (0.895), YARS2 (0.881)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_10525.1, huMAP3_13468.1, huMAP3_09668.1
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 2, mitochondrial. The protein encoded by this gene belongs to the class-II aminoacyl-tRNA synthetase family. It is a mitochondrial enzyme that specifically aminoacylates aspartyl-tRNA. Mutations in this gene are associated with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation (LBSL). [provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: leukoencephalopathy with brain stem and spinal cord involvement-high lactate syndrome (0.843); neurodegenerative disease (0.527); hereditary disease (0.518); hypertensive disorder (0.425); Cerebral cortical atrophy (0.425)
- **Europe PMC papers**: 796
- **Why important**: DARS2 has a relatively central network position and appears in most primary mitochondrial terms (GO:CC mitochondrial membrane; q_global = 0.0102)(GO:CC mitochondrion; q_global = 0.0138)(GO:CC organelle membrane; q_global = 0.0175)(GO:CC mitochondrial envelope; q_global = 0.0263). It encodes a mitochondrial aspartyl-tRNA synthetase and is connected by STRING to IARS2 and YARS2. hu.MAP independently places DARS2 with GFM1 and IARS2 in several mitochondrial translation-related complexes (hu.MAP huMAP3_10525.1)(hu.MAP huMAP3_13468.1)(hu.MAP huMAP3_09668.1). Its disease association with leukoencephalopathy and lactate elevation provides strong biological relevance to the link between mitochondrial translation and energetic dysfunction.
- **Conclusion**: Established conclusion: DARS2 supports a mitochondrial protein-production component within the module, beyond respiratory-chain abundance alone. Hypothesis: coordinated abundance of DARS2 and respiratory proteins may reflect matching mitochondrial translation capacity to respiratory-chain demand.

#### SFXN1

- **Related proteins** (co-abundance neighbors): HACD3 (0.91), ATP13A1 (0.82), SDHA (0.82), PIP4K2C (0.81), DLG1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sideroflexin 1. Enables D-serine transmembrane transporter activity and L-serine transmembrane transporter activity. Involved in D-serine transport; L-serine transport; and serine import into mitochondrion. Located in mitochondrion. Is integral component of mitochondrial inner membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: placental abruption (0.323); alcohol drinking (0.322); clostridium difficile infection (0.144); refractive error (0.112); scoliosis (0.111)
- **Europe PMC papers**: 568
- **Why important**: SFXN1 is present in all primary mitochondrial terms (GO:CC mitochondrial membrane; q_global = 0.0102)(GO:CC mitochondrion; q_global = 0.0138)(GO:CC organelle membrane; q_global = 0.0175)(GO:CC mitochondrial envelope; q_global = 0.0263)(GO:CC mitochondrial inner membrane; q_global = 0.0351) and occupies a connected position linking SDHA, HACD3, ATP13A1, PIP4K2C, and DLG1. It is an inner-membrane serine and D-serine transporter involved in mitochondrial serine import and one-carbon metabolism. HPA shows liver and neutrophil-progenitor enhancement, while the disease evidence includes metabolic and developmental associations. Its transporter function adds a metabolic-input dimension to the respiratory module.
- **Conclusion**: Established conclusion: SFXN1 is a plausible bridge between mitochondrial substrate supply and oxidative metabolism. Hypothesis: variation in mitochondrial serine transport may help explain coordinated changes in respiratory and translation-related proteins, although causality is not shown.

#### UQCRC2

- **Related proteins** (co-abundance neighbors): PRDX3 (0.82); STRING partners: ACO2 (0.879), ATP5F1C (0.98), ATP5PB (0.973), IDH3A (0.713), SDHA (0.99)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_06247.1, huMAP3_12457.1
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase core protein 2. The protein encoded by this gene is located in the mitochondrion, where it is part of the ubiquinol-cytochrome c reductase complex (also known as complex III). This complex constitutes a part of the mitochondrial respiratory chain. Defects in this gene are a cause of mitochondrial complex III deficiency nuclear type 5. [provided by RefSeq, Jul 2015].
- **Diseases (Open Targets)**: mitochondrial complex III deficiency (0.732); neurodegenerative disease (0.423); mitochondrial disease (0.312); gastric cancer (0.085); adrenoleukodystrophy (0.075)
- **Europe PMC papers**: 3297
- **Why important**: UQCRC2 is present in every primary mitochondrial enrichment term (GO:CC mitochondrial membrane; q_global = 0.0102)(GO:CC mitochondrion; q_global = 0.0138)(GO:CC organelle membrane; q_global = 0.0175)(GO:CC mitochondrial envelope; q_global = 0.0263)(GO:CC mitochondrial inner membrane; q_global = 0.0351) and is strongly connected in STRING to SDHA, ATP5F1C, ATP5PB, ACO2, and IDH3A. It is a core component of respiratory complex III and is represented in hu.MAP complexes with ATP5PB and MBOAT7 (hu.MAP huMAP3_06247.1)(hu.MAP huMAP3_12457.1). Its established links to mitochondrial complex III deficiency and other mitochondrial disease make it an informative respiratory-chain marker.
- **Conclusion**: Established conclusion: UQCRC2 reinforces the interpretation that the module covers connected respiratory-chain and ATP-synthesis machinery. Hypothesis: its co-abundance with ATP-synthase and tricarboxylic-acid-cycle proteins could indicate coordinated oxidative-phosphorylation remodeling.
