# Conserved co-abundance modules: bone and myometrium

## Module 0

**Tissue pair**: bone and myometrium  
**Genes (5)**: YWHAH, FLNA, RSU1, TLN1, VCL

### Function

The strongest interpretation is an actin–integrin adhesion and mechanotransduction module. The primary globally corrected evidence is regulation of cell-substrate adhesion (GO:BP regulation of cell-substrate adhesion; q_global = 0.00356), cell-substrate adhesion (GO:BP cell-substrate adhesion; q_global = 0.0165), and platelet aggregation (GO:BP platelet aggregation; q_global = 0.0481). FLNA, TLN1, and VCL support a focal-adhesion and actin-anchoring core, while RSU1 adds cell-matrix adhesion and Ras-pathway signaling. YWHAH is a phosphoserine-binding signaling adaptor that may connect adhesion machinery to regulated intracellular signaling. The platelet-aggregation term should be interpreted together with the HPA platelet and megakaryocyte enrichment, rather than as evidence that the module is specific to bone or myometrium. STRING terms concerning extracellular-matrix interactions, junctions, and adhesion (STRING NetworkNeighborAL Mixed, incl. Cell-extracellular matrix interactions, and Leukocyte adhesion deficiency 3; within-query FDR = 0.0001), (STRING NetworkNeighborAL Cell-extracellular matrix interactions, and Alpha-catenin/vinculin-like superfamily; within-query FDR = 0.0029), (STRING Process Regulation of cell-substrate adhesion; within-query FDR = 0.0131), (STRING Component Cell-cell junction; within-query FDR = 0.0269), and (STRING Component Anchoring junction; within-query FDR = 0.0296) are supportive only. Overall, the module is most consistent with regulation of cell attachment, cytoskeletal force transmission, junctional organization, and platelet-associated adhesion biology.

**Cell composition.** This is not a plasma or secreted-protein module: every member is classified as non-secreted. The HPA evidence instead shows a strong platelet and megakaryocyte signal across the module, with additional enrichment for megakaryocyte progenitors for RSU1. All genes have low immune-cell specificity, so the signal is not broadly characteristic of leukocytes. Tissue annotations are mixed, including blood vessel enrichment for TLN1 and YWHAH, blood vessel and intestine enrichment for FLNA, and low tissue specificity for VCL and RSU1. Protein detection is present for most assessed genes in myometrium, whereas the bone comparison has no matching HPA tissue protein data. The shared module may therefore reflect a conserved adhesion program in vascular, smooth-muscle, stromal, or platelet-related cells, but platelet or megakaryocyte material in the samples remains an important alternative explanation.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulation of cell-substrate adhesion | 0.00356 | FLNA, RSU1, TLN1, VCL |
| GO:BP cell-substrate adhesion | 0.0165 | FLNA, RSU1, TLN1, VCL |
| GO:BP platelet aggregation | 0.0481 | FLNA, TLN1, VCL |

### STRING and hu.MAP

STRING provides very strong pairwise support for the FLNA–TLN1, FLNA–VCL, and TLN1–VCL relationships. These interactions define a known focal-adhesion and actin-linking core and agree with the globally corrected adhesion terms. STRING also places RSU1 with the adhesion group in network-neighbor and integrin-adhesome annotations, while YWHAH is represented mainly through platelet, junction, and signaling-related annotations. The STRING enrichment results are supplementary and were not globally corrected across all modules, so they should not be treated as independent global significance. No hu.MAP complex contains at least two module members. Thus, the module contains a known physical or functional adhesion core, but the full co-abundance set is not supported as a single established hu.MAP complex.

**STRING interactions (score >= 0.7)**: 3 of 10 gene pairs: FLNA–TLN1 (0.998); FLNA–VCL (0.998); TLN1–VCL (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Mixed, incl. Cell-extracellular matrix interactions, and Leukocyte adhesion deficiency 3 (FDR = 0.0001, 4 genes); NetworkNeighborAL Cell-extracellular matrix interactions, and Alpha-catenin/vinculin-like superfamily (FDR = 0.0029, 3 genes); TISSUES Blood platelet (FDR = 0.0062, 5 genes); TISSUES Gut (FDR = 0.007, 3 genes); Process Regulation of cell-substrate adhesion (FDR = 0.0131, 4 genes); Component Cell-cell junction (FDR = 0.0269, 4 genes); Component Anchoring junction (FDR = 0.0296, 5 genes); PMID (2022) Postnatal Smad3 Inactivation in Murine Smooth Muscle Cells Elicits a Temporally and Regionally Distinct Transcriptional Response. (FDR = 0.0382, 4 genes); PMID (2018) Cell Adhesion and Matrix Stiffness: Coordinating Cancer Cell Invasion and Metastasis. (FDR = 0.0382, 4 genes); PMID (2018) Novel functions for integrin-associated proteins revealed by analysis of myofibril attachment in Drosophila. (FDR = 0.0382, 4 genes); PMID (2013) The role of the actin cytoskeleton in regulating Drosophila behavior. (FDR = 0.0382, 4 genes); PMID (2016) The integrin adhesome network at a glance. (FDR = 0.0408, 4 genes); PMID (2014) Integrins and integrin-associated proteins in the cardiac myocyte. (FDR = 0.0408, 4 genes); PMID (2010) Proteomic characterization of novel alternative splice variant proteins in human epidermal growth factor receptor 2neu-induced breast cancers. (FDR = 0.0408, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The biological ingredients are not novel in isolation: FLNA, TLN1, and VCL are well-established adhesion and cytoskeletal proteins, and their STRING relationships are already known. The co-abundance module may nevertheless represent a new tissue-pair observation if its coordinated appearance in bone and myometrium has not been reported elsewhere. The available evidence does not establish that claim, because absence from hu.MAP and incomplete STRING coverage cannot prove novelty. A cautious conclusion is that this is a potentially novel cross-tissue co-abundance configuration built around a previously known adhesion core, with novelty requiring comparison against published bone and myometrium proteomic or transcriptomic modules and independent replication.

**Hypothesis.** Hypothesis: a shared vascular, smooth-muscle, stromal, or platelet-associated cell population coordinates an integrin-linked adhesion program across bone and myometrium. In this model, TLN1 activates or organizes integrin-associated adhesion, FLNA crosslinks actin and couples it to membrane receptors, and VCL stabilizes force-bearing cell-matrix and cell-cell junctions. RSU1 could modulate the adhesion response through Ras-associated signaling, while YWHAH could tune the phosphorylation-dependent signaling state of the adhesion machinery. The platelet enrichment raises the alternative hypothesis that the shared signal is partly contributed by platelet or megakaryocyte material rather than being intrinsic to the resident tissues. These mechanistic links are hypotheses; the established evidence is the adhesion annotation, the known STRING core, the HPA cell-type pattern, and the observed co-abundance.

### Important genes

#### TLN1

- **Related proteins** (co-abundance neighbors): FLNA (0.86), VCL (0.84), YWHAH (0.82); STRING partners: FLNA (0.998), VCL (0.999)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 is the strongest network-centered member, linking FLNA, VCL, and YWHAH. It occurs in every globally corrected term (GO:BP regulation of cell-substrate adhesion; q_global = 0.00356), (GO:BP cell-substrate adhesion; q_global = 0.0165), and (GO:BP platelet aggregation; q_global = 0.0481), is localized to focal adhesions and the cytosol, and is annotated for integrin activation, cell adhesion, actin organization, and cell-junction assembly. Its HPA profile connects the module to blood vessels, platelets, and megakaryocytes, while its myometrial protein detection supports relevance to the tissue pair. It also has extensive literature and disease evidence.
- **Conclusion**: Established conclusion: TLN1 is a central and biologically plausible organizer of the module's adhesion program. Hypothesis: its abundance may report integrin-dependent mechanical coupling or platelet-associated adhesion across the two tissues.

#### FLNA

- **Related proteins** (co-abundance neighbors): TLN1 (0.86); STRING partners: TLN1 (0.998), VCL (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA participates in every globally corrected term and is the principal bridge between the adhesion core and VCL and TLN1 in STRING. Its established function is actin crosslinking and linkage of actin to membrane glycoproteins, integrins, receptor complexes, and second messengers. HPA places it in plasma membrane, actin-filament, and cytosolic compartments and shows enrichment in vascular, stromal, epithelial, and megakaryocyte-related cell types. It has the largest literature volume among the adhesion-core genes and extensive disease associations.
- **Conclusion**: Established conclusion: FLNA is a strong molecular anchor for the module's cytoskeletal and membrane-adhesion interpretation. Hypothesis: FLNA may transmit tissue-specific mechanical or receptor signals into the shared co-abundance program.

#### VCL

- **Related proteins** (co-abundance neighbors): TLN1 (0.84); STRING partners: FLNA (0.998), TLN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vinculin. Vinculin is a cytoskeletal protein associated with cell-cell and cell-matrix junctions, where it is thought to function as one of several interacting proteins involved in anchoring F-actin to the membrane. Defects in VCL are the cause of cardiomyopathy dilated type 1W. Dilated cardiomyopathy is a disorder characterized by ventricular dilation and impaired systolic function, resulting in congestive…
- **Diseases (Open Targets)**: dilated cardiomyopathy 1W (0.692); hypertrophic cardiomyopathy 15 (0.660); hypertrophic cardiomyopathy (0.652); familial isolated dilated cardiomyopathy (0.642); cancer (0.605)
- **Europe PMC papers**: 10760
- **Why important**: VCL is part of all globally corrected terms and forms the known STRING core with FLNA and TLN1. Its established role is anchoring F-actin at cell-cell and cell-matrix junctions, consistent with focal-adhesion localization and the adhesion and junction annotations. HPA identifies platelet enrichment and protein detection in myometrium. VCL also has substantial literature and a direct association with dilated and hypertrophic cardiomyopathy.
- **Conclusion**: Established conclusion: VCL supports a force-bearing junction and focal-adhesion interpretation of the module. Hypothesis: coordinated VCL abundance may reflect junctional reinforcement in smooth-muscle, vascular, stromal, or platelet-associated cells.

#### RSU1

- **Related proteins** (co-abundance neighbors): YWHAH (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Ras suppressor protein 1. This gene encodes a protein that is involved in the Ras signal transduction pathway, growth inhibition, and nerve-growth factor induced differentiation processes, as determined in mouse and human cell line studies. In mouse, the encoded protein was initially isolated based on its ability to inhibit v-Ras transformation. Multiple alternatively spliced transcript variants for this gene have been rep…
- **Diseases (Open Targets)**: alcohol drinking (0.270); placental retention (0.266); obesity disorder (0.235); neurodegenerative disease (0.213); subarachnoid hemorrhage (0.211)
- **Europe PMC papers**: 614
- **Why important**: RSU1 connects to YWHAH in the co-abundance network and is included in the globally corrected cell-substrate adhesion terms (GO:BP regulation of cell-substrate adhesion; q_global = 0.00356) and (GO:BP cell-substrate adhesion; q_global = 0.0165). Its annotations support cell-matrix adhesion and Ras signaling, while STRING places it in integrin-adhesome and extracellular-matrix interaction neighborhoods. HPA links it to megakaryocyte progenitors, megakaryocytes, and platelets, and protein is detected in myometrium. Although its literature volume is smaller than that of the core structural proteins, it may provide a regulatory rather than purely structural component.
- **Conclusion**: Established conclusion: RSU1 strengthens the adhesion interpretation and connects it to Ras-associated signaling. Hypothesis: RSU1 may regulate how the shared module couples matrix attachment to growth or differentiation signals.

#### YWHAH

- **Related proteins** (co-abundance neighbors): TLN1 (0.82), RSU1 (0.81); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein eta. This gene product belongs to the 14-3-3 family of proteins which mediate signal transduction by binding to phosphoserine-containing proteins. This highly conserved protein family is found in both plants and mammals, and this protein is 99% identical to the mouse, rat and bovine orthologs. This gene contains a 7 bp repeat sequence in its 5' UTR, and changes in the number of this repeat have been as…
- **Diseases (Open Targets)**: COVID-19 (0.371); severe acute respiratory syndrome (0.370); placenta praevia (0.247); chronic hepatitis C virus infection (0.180); response to xenobiotic stimulus (0.080)
- **Europe PMC papers**: 1273
- **Why important**: YWHAH occupies the branch connecting TLN1 and RSU1, despite lacking direct STRING partners within the module and lacking globally corrected GO or KEGG membership. Its established 14-3-3 function is binding phosphoserine-containing proteins to mediate signal transduction and intracellular localization. HPA associates it with blood vessels, brain, platelets, and megakaryocytes, while STRING supplies supplementary platelet and junction evidence (STRING TISSUES Blood platelet; within-query FDR = 0.0062), (STRING Component Cell-cell junction; within-query FDR = 0.0269), and (STRING Component Anchoring junction; within-query FDR = 0.0296). It has substantial literature and disease associations, though less direct adhesion evidence than the structural core.
- **Conclusion**: Established conclusion: YWHAH is a plausible signaling adaptor associated with the module but is less directly established as an adhesion component. Hypothesis: it may connect phosphorylation-dependent signaling to TLN1–RSU1 regulation or may partly mark the platelet-associated component of the module.

## Module 1

**Tissue pair**: bone and myometrium  
**Genes (21)**: PGD, GOT1, PGM3, CAPZB, GMPS, HARS1, IDH1, IMPA1, MAT2A, NRDC, PDXP, PFAS, RAB3GAP2, AARS1, DARS1, THOP1, UBA6, USP5, WDR5, XPO7, XPNPEP1

### Function

The module is best interpreted as a broadly expressed intracellular metabolic and proteostasis program rather than a bone- or myometrium-specific pathway. Its central genes connect amino-acid and nucleotide metabolism, redox metabolism, protein translation, protein modification, peptide processing, and intracellular transport. AARS1 is a prominent network hub linking several of these activities, while the IDH1–GOT1–PGD relationships connect cytosolic carbon metabolism with NADPH-related metabolism. MAT2A, the aminoacyl-tRNA synthetases, GMPS, PFAS, PGM3, UBA6, and USP5 further support a general cellular maintenance program. No GO or KEGG term passed global correction, so these functional interpretations are based on the annotated genes and network structure rather than significant enrichment. The absence of a globally significant term does not invalidate the module.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and most annotated proteins are intracellular, commonly cytosolic or nuclear. Most genes have low tissue specificity and low immune-cell specificity, which is consistent with broadly expressed housekeeping or core metabolic functions rather than a specialized extracellular bone or smooth-muscle program. There is nevertheless a possible cellular-composition contribution. PGD is enriched in bone marrow and several blood-cell categories, PFAS is immune-cell enhanced, and additional genes show selected immune or progenitor-cell enrichments. These observations justify testing for blood or marrow contamination and shared stromal or vascular cell types, but the overall HPA profile does not support interpreting the entire module as a blood-protein module. Myometrium protein detection is available for only part of the module and shows detection for several genes, whereas there is no matching HPA tissue result for bone.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The network contains a small set of already supported physical or functional relationships. STRING supports AARS1 with HARS1 and DARS1, and supports the metabolic links GOT1 with IDH1 and IDH1 with PGD. These links provide independent support for parts of the co-abundance structure, especially the aminoacyl-tRNA synthetase connection and the cytosolic metabolic connection. The STRING functional-enrichment result is empty, so it does not provide a separate pathway-level signal. hu.MAP supplies additional complex-level context. (hu.MAP huMAP3_14442.1) places UBA6, AARS1, GMPS, PGD, and XPNPEP1 in the same large complex, although only a subset of that complex is represented here. (hu.MAP huMAP3_01475.1) and (hu.MAP huMAP3_09400.1) independently connect IDH1 and PGD in smaller complexes, strengthening the interpretation of that pair as a known metabolic association. (hu.MAP huMAP3_05750.1) connects PGM3 and XPO7 in another complex. Most other module edges lack a reported STRING or hu.MAP relationship, so the co-abundance module is not simply a reconstruction of one established protein complex.

**STRING interactions (score >= 0.7)**: 4 of 210 gene pairs: AARS1–DARS1 (0.743); AARS1–HARS1 (0.906); GOT1–IDH1 (0.929); IDH1–PGD (0.877)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (UBA6, AARS1, GMPS, PGD, XPNPEP1; 5/57); huMAP3_01475.1 (IDH1, PGD; 2/3); huMAP3_09400.1 (IDH1, PGD; 2/4); huMAP3_05750.1 (PGM3, XPO7; 2/9)

### Novelty

This is a new tissue-pair co-abundance observation, but the biological machinery represented by it is not wholly new. Several edges and complexes are already documented by STRING or hu.MAP, and the functions of the principal enzymes are established. The potentially novel result is the coordinated abundance of this combination of translation, metabolism, proteostasis, and transport genes across bone and myometrium. That claim should remain provisional because the module could reflect broadly expressed cellular maintenance, shared cell types, technical factors, or blood and marrow contribution. Absence of a relationship from STRING or hu.MAP would not by itself establish novelty. Confirmation in independent cohorts, with cell-composition adjustment and tissue-resolved validation, is needed before calling the cross-tissue module a new biological mechanism.

**Hypothesis.** Hypothesis: the conserved module reflects a shared intracellular resource-management state in cells present in both tissues. In this model, aminoacyl-tRNA charging and methyl-donor production support protein synthesis, IDH1 and PGD help maintain cytosolic carbon flow and reducing capacity, and UBA6, USP5, THOP1, and XPNPEP1 regulate protein or peptide turnover. XPO7 and the actin-associated CAPZB provide transport or structural context, while PGM3 may connect carbohydrate flux with glycosylation-related metabolism. The module may therefore mark cells maintaining biosynthetic and proteostatic capacity under common tissue demands, rather than a dedicated bone–myometrium signaling pathway. The blood-cell enrichment of PGD and related annotations is an alternative explanation that should be tested explicitly.

### Important genes

#### AARS1

- **Related proteins** (co-abundance neighbors): IDH1 (0.92), GOT1 (0.90), HARS1 (0.86), MAT2A (0.86), PGD (0.84), USP5 (0.83), PFAS (0.83), XPO7 (0.83), IMPA1 (0.82), THOP1 (0.82); STRING partners: DARS1 (0.743), HARS1 (0.906)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: alanyl-tRNA synthetase 1. The human alanyl-tRNA synthetase (AARS) belongs to a family of tRNA synthases, of the class II enzymes.  Class II tRNA synthases evolved early in evolution and are highly conserved. This is reflected by the fact that 498 of the 968-residue polypeptide human AARS shares 41% identity witht the E.coli protein.  tRNA synthases are the enzymes that interpret the RNA code and attach specific aminoacids …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2N (0.762); developmental and epileptic encephalopathy, 29 (0.747); undetermined early-onset epileptic encephalopathy (0.678); trichothiodystrophy 8, nonphotosensitive (0.568); Charcot-Marie-Tooth disease type 2 (0.566)
- **Europe PMC papers**: 672
- **Why important**: AARS1 is the strongest network hub in the supplied subgraph and connects the aminoacyl-tRNA synthetase branch with IDH1, GOT1, MAT2A, PGD, USP5, PFAS, and XPO7. Its established function is alanyl-tRNA aminoacylation and translation-related tRNA processing. It also has substantial literature support and disease associations involving inherited neurological disorders. Its participation in (hu.MAP huMAP3_14442.1) and its STRING relationship with HARS1 provide external support for the translation-related part of the module.
- **Conclusion**: Established evidence supports AARS1 as a central translation-supporting component and a plausible integrator of the module. It is not established that AARS1 drives the shared bone–myometrium pattern; its broad expression makes a general housekeeping interpretation more cautious and more likely than a tissue-specific causal role.

#### IDH1

- **Related proteins** (co-abundance neighbors): AARS1 (0.92), PFAS (0.85), XPO7 (0.85), PGD (0.85); STRING partners: GOT1 (0.929), PGD (0.877)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_01475.1, huMAP3_09400.1
- **Function (MyGene.info)**: isocitrate dehydrogenase (NADP(+)) 1. Isocitrate dehydrogenases catalyze the oxidative decarboxylation of isocitrate to 2-oxoglutarate. These enzymes belong to two distinct subclasses, one of which utilizes NAD(+) as the electron acceptor and the other NADP(+). Five isocitrate dehydrogenases have been reported: three NAD(+)-dependent isocitrate dehydrogenases, which localize to the mitochondrial matrix, and two NADP(+)-dependent isoci…
- **Diseases (Open Targets)**: acute myeloid leukemia (0.779); Ollier disease (0.672); glioblastoma (0.657); cholangiocarcinoma (0.652); glioma (0.637)
- **Europe PMC papers**: 29424
- **Why important**: IDH1 is a highly connected metabolic node linked to AARS1, PFAS, XPO7, and PGD. Its established function includes cytosolic isocitrate metabolism, production of two-oxoglutarate, and NADPH regeneration. The IDH1–GOT1 and IDH1–PGD relationships are supported by STRING, and IDH1 and PGD co-occur in (hu.MAP huMAP3_01475.1) and (hu.MAP huMAP3_09400.1). IDH1 also has extensive literature and disease associations, including cancer and skeletal dysplasia-related evidence in the supplied annotations.
- **Conclusion**: Established evidence supports IDH1 as a metabolic anchor and a credible explanation for part of the module's coordinated abundance. The hypothesis that altered IDH1 activity explains conservation between bone and myometrium remains untested and should not be inferred from co-abundance alone.

#### PGD

- **Related proteins** (co-abundance neighbors): IDH1 (0.85), AARS1 (0.84), NRDC (0.83), GOT1 (0.82); STRING partners: IDH1 (0.877)
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14442.1, huMAP3_01475.1, huMAP3_09400.1
- **Function (MyGene.info)**: phosphogluconate dehydrogenase. 6-phosphogluconate dehydrogenase is the second dehydrogenase in the pentose phosphate shunt. Deficiency of this enzyme is generally asymptomatic, and the inheritance of this disorder is autosomal dominant. Hemolysis results from combined deficiency of 6-phosphogluconate dehydrogenase and 6-phosphogluconolactonase suggesting a synergism of the two enzymopathies. Several transcript variants encoding…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); Abnormality of the skeletal system (0.329); autoimmune disorder of central nervous system (0.246); smoking behavior (0.245); essential hypertension (0.199)
- **Europe PMC papers**: 8652
- **Why important**: PGD is connected to IDH1, AARS1, NRDC, and GOT1 and participates in (hu.MAP huMAP3_14442.1), (hu.MAP huMAP3_01475.1), and (hu.MAP huMAP3_09400.1). Its established role is in the oxidative pentose-phosphate pathway and NADPH regeneration. It has strong HPA enrichment in bone-marrow and blood-cell categories, including granulocytic and myeloid populations, and it has substantial literature and disease annotation. These features make it both biologically informative and important for evaluating cellular-composition confounding.
- **Conclusion**: Established evidence supports PGD as a redox and pentose-phosphate component and as a possible marker of blood or marrow-derived contribution. It is not established whether PGD reflects intrinsic metabolism in bone or myometrium cells, or the presence of enriched blood-lineage cells in the samples.

#### MAT2A

- **Related proteins** (co-abundance neighbors): GMPS (0.90), AARS1 (0.86), DARS1 (0.85), HARS1 (0.81), THOP1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionine adenosyltransferase 2A. The protein encoded by this gene catalyzes the production of S-adenosylmethionine (AdoMet) from methionine and ATP. AdoMet is the key methyl donor in cellular processes. [provided by RefSeq, Jun 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.545); familial thoracic aortic aneurysm and aortic dissection (0.416); autoimmune disorder of central nervous system (0.340); prostate carcinoma (0.252); Abnormality of the cardiovascular system (0.192)
- **Europe PMC papers**: 2615
- **Why important**: MAT2A occupies a connected position beside AARS1, DARS1, HARS1, GMPS, and THOP1. Its established function is production of S-adenosylmethionine, a central methyl donor, and its annotations include cellular responses to methionine and regulation of TORC1 signaling. It has extensive literature and disease associations, including cardiovascular and neoplastic contexts. Its HPA profile includes tissue enhancement in pancreas and single-cell enhancement in smooth muscle cells, which is relevant to cautious interpretation of myometrium-related co-abundance.
- **Conclusion**: Established evidence supports MAT2A as a biosynthetic and methylation-state regulator within the module. The smooth-muscle annotation makes it compatible with a myometrial cellular contribution, but it does not demonstrate that MAT2A is responsible for conservation across the two tissues.

#### GOT1

- **Related proteins** (co-abundance neighbors): AARS1 (0.90), PDXP (0.89), THOP1 (0.88), PGD (0.82); STRING partners: IDH1 (0.929)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamic-oxaloacetic transaminase 1. Glutamic-oxaloacetic transaminase is a pyridoxal phosphate-dependent enzyme which exists in cytoplasmic and mitochondrial forms, GOT1 and GOT2, respectively.  GOT plays a role in amino acid metabolism and the urea and tricarboxylic acid cycles. The two enzymes are homodimeric and show close homology. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); Parkinson disease (0.375); Alzheimer disease (0.367); lysosomal storage disease (0.356); obesity disorder (0.172)
- **Europe PMC papers**: 3793
- **Why important**: GOT1 is connected to AARS1, PDXP, THOP1, and PGD, and it has a strong STRING relationship with IDH1. Its established function is cytosolic aminotransferase activity involving amino-acid, oxaloacetate, and two-oxoglutarate metabolism. HPA annotations show enhancement in heart and skeletal muscle and selected cell types, while its literature volume is substantial. It therefore links the module's central translation-associated hub to cytosolic carbon and amino-acid metabolism.
- **Conclusion**: Established evidence supports GOT1 as a metabolic connector in the module. The muscle-related HPA pattern is compatible with shared contractile or muscle-associated cellular contexts, but the supplied evidence does not establish a specific bone–myometrium mechanism or distinguish cell composition from intrinsic metabolic regulation.

## Module 2

**Tissue pair**: bone and myometrium  
**Genes (25)**: PRKAG1, AKR1B1, RNPEP, CPNE3, DCUN1D1, DPYSL2, DPYSL3, EIF6, ILK, PKM, MDH1, NAGK, PARVA, PDLIM4, PGM1, PALM2AKAP2, PLS3, ATIC, NARS1, SARS1, TUBB6, VASP, WDR1, XPO1, CSE1L

### Function

The module is best interpreted as a mixed cytoskeletal, adhesion, cellular-energy, and core metabolic program rather than as a narrowly defined pathway. Its most coherent biological signals are cytoskeletal organization and cell-matrix adhesion through DPYSL2, DPYSL3, ILK, PARVA, VASP, PLS3, PDLIM4, and WDR1; carbohydrate and energy metabolism through PGM1, PKM, MDH1, AKR1B1, NAGK, and PRKAG1; and biosynthetic or information-processing functions through ATIC, NARS1, SARS1, XPO1, CSE1L, and EIF6. The network therefore may reflect coordinated maintenance of cellular structure and energetic capacity in contractile or mechanically active cells. No GO or KEGG term passed global correction, and there was no STRING functional-enrichment result. The functional interpretation is consequently driven by the convergent gene annotations, network topology, known complexes, and tissue or cell-type context rather than by statistically significant pathway enrichment.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only RNPEP is annotated as secreted, with unknown location, and the remaining genes are intracellular or membrane-associated. Most genes have low tissue specificity, so the module is compatible with broadly expressed cellular machinery rather than a sharply tissue-restricted program. HPA also shows substantial cell-type enhancement, including smooth muscle cells, platelets, megakaryocytes, epithelial populations, trophoblast populations, and several neural or muscle-related cell types. Several genes have blood-cell enrichment or enhancement, particularly in platelet or myeloid-related populations, although the overall module has low immune-cell specificity. This raises the possibility that part of the shared bone–myometrium signal reflects common smooth-muscle, vascular, platelet, stromal, or other shared cellular components rather than a bone–myometrium-specific molecular program. The bone protein-detection field has no matching HPA tissue data, whereas myometrium shows protein detection for a subset of the module; absence of detection should not be treated as evidence of absence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports several established relationships within the module: DPYSL2–DPYSL3, ILK–PARVA, CSE1L–XPO1, NARS1–SARS1, ATIC–PRKAG1, and DPYSL3–PDLIM4. These relationships provide direct support for a cytoskeletal DPYSL and integrin-linked adhesion component, a nuclear transport component, and a small aminoacyl-tRNA-synthetase or metabolic-associated connection. hu.MAP independently supports recurring complex structure: DPYSL2 and DPYSL3 occur together in several complexes (hu.MAP huMAP3_00051.1), (hu.MAP huMAP3_11599.1), and (hu.MAP huMAP3_11626.1); ILK and PARVA occur together in (hu.MAP huMAP3_09385.1) and (hu.MAP huMAP3_11194.1); XPO1 and CSE1L occur together in (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_09592.1); and ATIC with PKM occurs in (hu.MAP huMAP3_14442.1) and (hu.MAP huMAP3_12823.1). ATIC, PKM, and PLS3 also co-occur within (hu.MAP huMAP3_14442.1). These observations indicate that portions of the module recover known molecular assemblies or functionally related proteins. However, many module edges are not represented by high-confidence STRING interactions, and several hu.MAP complexes contain only a small subset of their members in the module. Thus, the module is not equivalent to one physical complex; it is a co-abundance structure containing several connected functional neighborhoods.

**STRING interactions (score >= 0.7)**: 6 of 300 gene pairs: ATIC–PRKAG1 (0.826); CSE1L–XPO1 (0.976); DPYSL2–DPYSL3 (0.976); DPYSL3–PDLIM4 (0.748); ILK–PARVA (0.999); NARS1–SARS1 (0.843)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (PLS3, PKM, ATIC; 3/57); huMAP3_00051.1 (DPYSL3, DPYSL2; 2/6); huMAP3_12823.1 (PKM, ATIC; 2/7); huMAP3_11599.1 (DPYSL3, DPYSL2; 2/8); huMAP3_09385.1 (ILK, PARVA; 2/8); huMAP3_11194.1 (ILK, PARVA; 2/10); huMAP3_07170.1 (XPO1, CSE1L; 2/14); huMAP3_09042.1 (XPO1, CSE1L; 2/26); huMAP3_06791.1 (XPO1, CSE1L; 2/31); huMAP3_11626.1 (DPYSL3, DPYSL2; 2/42); huMAP3_09592.1 (XPO1, CSE1L; 2/95)

### Novelty

The module-level finding may be novel, but the fact sheet does not establish that it is a previously unknown biological mechanism. Its strongest relationships and complex memberships are already represented in STRING or hu.MAP, including the DPYSL, ILK–PARVA, XPO1–CSE1L, and ATIC-associated relationships. What could be new is their coordinated co-abundance across bone and myometrium, especially the combination of cytoskeletal adhesion proteins with metabolic, translational, and nuclear-transport proteins. That claim requires comparison with published bone and myometrium co-abundance studies, independent cohorts, and cell-composition-controlled analyses. Absence of an interaction from STRING or hu.MAP would not by itself demonstrate novelty, and the lack of globally significant GO or KEGG enrichment does not invalidate the module.

**Hypothesis.** Mechanistic hypothesis: the shared module reflects a conserved structural-metabolic state in mechanically active or contractile tissue-associated cells. Integrin-linked adhesion and actin or microtubule regulators could coordinate cell shape, attachment, and force transmission, while PGM1, PKM, MDH1, ATIC, and PRKAG1 could provide carbohydrate, nucleotide, and energy support for this state. DPYSL proteins may connect cytoskeletal remodeling to cellular signaling, and nuclear transport proteins may support the associated transcriptional or cell-cycle demands. In bone, this could relate to osteogenic or stromal cell architecture and energetic maintenance; in myometrium, it could relate to smooth-muscle structure and contractile-cell organization. A competing explanation is that the shared signal is mainly driven by common smooth-muscle, vascular, platelet, stromal, or blood-associated cell admixture. This hypothesis should be tested by cell-type deconvolution, spatial localization, perturbation of adhesion or energy-sensing components, and replication in independent tissue cohorts.

### Important genes

#### DPYSL2

- **Related proteins** (co-abundance neighbors): PGM1 (0.91), WDR1 (0.87), ILK (0.86), MDH1 (0.86), CPNE3 (0.86), ATIC (0.84), PLS3 (0.83), PKM (0.82); STRING partners: DPYSL3 (0.976)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Microtubules, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_00051.1, huMAP3_11599.1, huMAP3_11626.1
- **Function (MyGene.info)**: dihydropyrimidinase like 2. This gene encodes a member of the collapsin response mediator protein family. Collapsin response mediator proteins form homo- and hetero-tetramers and facilitate neuron guidance, growth and polarity. The encoded protein promotes microtubule assembly and is required for Sema3A-mediated growth cone collapse, and also plays a role in synaptic signaling through interactions with calcium channels. This…
- **Diseases (Open Targets)**: hypertensive disorder (0.431); autosomal dominant non-syndromic intellectual disability (0.370); cardiovascular disorder (0.297); ovarian neoplasm (0.292); glomerulonephritis (0.269)
- **Europe PMC papers**: 1328
- **Why important**: DPYSL2 is the most connected member of the module and links several metabolic and cytoskeletal neighbors, including PGM1, WDR1, ILK, MDH1, CPNE3, ATIC, PLS3, and PKM. It has direct STRING support with DPYSL3 and appears with DPYSL3 in several hu.MAP complexes (hu.MAP huMAP3_00051.1), (hu.MAP huMAP3_11599.1), and (hu.MAP huMAP3_11626.1). Its established function in collapsin-response-mediator complexes, microtubule assembly, cell polarity, and neuronal or cytoskeletal signaling makes it a plausible organizing point for the structural part of the module. It has extensive literature and disease associations involving neurological and cardiovascular phenotypes.
- **Conclusion**: Established evidence supports DPYSL2 as a central cytoskeletal and signaling-associated member of the module. It is not established that DPYSL2 drives the shared bone–myometrium co-abundance pattern. Its central network position makes it a strong candidate for testing as an organizer of the proposed structural-metabolic state.

#### ILK

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.86), VASP (0.84), DPYSL3 (0.82), PARVA (0.81); STRING partners: PARVA (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: integrin linked kinase. This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastas…
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); familial hypertrophic cardiomyopathy (0.194); Abnormality of the cardiovascular system (0.148); Prolonged QT interval (0.118); neoplasm (0.118)
- **Europe PMC papers**: 8401
- **Why important**: ILK connects DPYSL2, VASP, DPYSL3, and PARVA and is supported by a very strong STRING relationship with PARVA. ILK and PARVA recur together in hu.MAP complexes (hu.MAP huMAP3_09385.1) and (hu.MAP huMAP3_11194.1). ILK is localized to focal adhesion sites, is enhanced in smooth muscle cells and platelet-related cell types, and has established roles in integrin-mediated signaling, cell-matrix adhesion, morphogenesis, and cell survival. Its literature is extensive and includes disease associations involving cardiovascular and neoplastic phenotypes.
- **Conclusion**: Established evidence identifies ILK as a focal-adhesion and integrin-signaling component that is highly relevant to the shared tissue context. The module data support its participation in a coordinated adhesion program, but do not prove that ILK controls the co-abundance module or tissue physiology.

#### PGM1

- **Related proteins** (co-abundance neighbors): ATIC (0.94), DPYSL2 (0.91), CPNE3 (0.86), WDR1 (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglucomutase 1. The protein encoded by this gene is an isozyme of phosphoglucomutase (PGM) and belongs to the phosphohexose mutase family. There are several PGM isozymes, which are encoded by different genes and catalyze the transfer of phosphate between the 1 and 6 positions of glucose. In most cell types, this PGM isozyme is predominant, representing about 90% of total PGM activity. In red cells, PGM2 is a majo…
- **Diseases (Open Targets)**: PGM1-congenital disorder of glycosylation (0.843); MPDU1-congenital disorder of glycosylation (0.551); developmental and epileptic encephalopathy, 36 (0.551); RFT1-congenital disorder of glycosylation (0.551); disorder of glycogen metabolism (0.506)
- **Europe PMC papers**: 3203
- **Why important**: PGM1 connects the prominent DPYSL2–ATIC–CPNE3 neighborhood and is associated with glucose, glycogen, gluconeogenic, and broader carbohydrate metabolism. HPA places it in a skeletal-muscle and tongue-enriched tissue context, and protein detection is reported in myometrium. PGM1 is the predominant phosphoglucomutase isozyme in most cell types and has extensive literature, with established associations to congenital glycosylation and glycogen-metabolism disorders.
- **Conclusion**: Established evidence supports PGM1 as a major metabolic component that could provide carbohydrate-processing capacity in the module. The shared network does not establish a bone–myometrium-specific metabolic pathway, so its role should be interpreted as a plausible metabolic correlate rather than a demonstrated driver.

#### PLS3

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: plastin 3. Plastins are a family of actin-binding proteins that are conserved throughout eukaryote evolution and expressed in most tissues of higher eukaryotes. In humans, two ubiquitous plastin isoforms (L and T) have been identified. Plastin 1 (otherwise known as Fimbrin) is a third distinct plastin isoform which is specifically expressed at high levels in the small intestine. The L isoform is expressed on…
- **Diseases (Open Targets)**: X-linked osteoporosis with fractures (0.727); congenital diaphragmatic hernia (0.553); osteoporosis (0.477); hernia, anterior diaphragmatic (0.380); postmenopausal osteoporosis (0.341)
- **Europe PMC papers**: 1365
- **Why important**: PLS3 provides a direct connection from the DPYSL2 neighborhood to actin filament bundling and network formation. It is included with ATIC and PKM in hu.MAP complex (hu.MAP huMAP3_14442.1), is detected in myometrium, and has an HPA profile involving vascular tissue and several epithelial or immune-associated cell types. Its established functions include actin organization and bone development, and it has a strong disease connection to X-linked osteoporosis and osteoporosis-related phenotypes.
- **Conclusion**: Established evidence makes PLS3 particularly relevant to the bone component and to the structural interpretation of the module. Its inclusion does not prove that the module is osteogenic, because PLS3 can also reflect broadly distributed cytoskeletal or vascular cell populations. It is a useful candidate for testing whether the shared signal has a genuine bone-structural component.

#### ATIC

- **Related proteins** (co-abundance neighbors): PGM1 (0.94), CPNE3 (0.89), TUBB6 (0.86), SARS1 (0.86), NARS1 (0.85), DPYSL2 (0.84); STRING partners: PRKAG1 (0.826)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_14442.1, huMAP3_12823.1
- **Function (MyGene.info)**: 5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase. This gene encodes a bifunctional protein that catalyzes the last two steps of the de novo purine biosynthetic pathway. The N-terminal domain has phosphoribosylaminoimidazolecarboxamide formyltransferase activity, and the C-terminal domain has IMP cyclohydrolase activity. A mutation in this gene results in AICA-ribosiduria. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: AICA-ribosiduria (0.708); cancer (0.571); Intellectual disability (0.463); lung adenocarcinoma (0.390); anaplastic large cell lymphoma (0.374)
- **Europe PMC papers**: 5200
- **Why important**: ATIC is a well-connected bridge between PGM1, CPNE3, TUBB6, SARS1, NARS1, and DPYSL2. It has STRING support with PRKAG1 and appears with PKM in hu.MAP complexes (hu.MAP huMAP3_14442.1) and (hu.MAP huMAP3_12823.1). ATIC catalyzes the final reactions of de novo purine biosynthesis and is linked to cellular nucleotide production, while its HPA profile is broadly expressed and includes myometrial protein detection. It has extensive literature and established disease associations including AICA-ribosiduria and cancer-related phenotypes.
- **Conclusion**: Established evidence supports ATIC as a nucleotide-biosynthetic and metabolic bridge within the module. The data do not show that purine synthesis is globally enriched or that ATIC explains the tissue sharing, because no GO or KEGG term passed global correction. Its network position nevertheless makes it a strong candidate for coupling energetic or biosynthetic state to cytoskeletal maintenance.

## Module 3

**Tissue pair**: bone and myometrium  
**Genes (10)**: GOT2, ATP5F1A, ATP5F1B, CS, CLTC, FH, MESD, OAT, DDOST, RAB18

### Function

The strongest interpretation is a mitochondrial energy and intermediary-metabolism module. CS is the network hub and links the ATP synthase subunits ATP5F1A and ATP5F1B with GOT2, FH, OAT, CLTC and MESD. CS and FH are tricarboxylic-acid-cycle enzymes, GOT2 and OAT connect amino-acid and nitrogen metabolism with mitochondrial metabolism, and ATP5F1A plus ATP5F1B form the catalytic F1 portion of mitochondrial ATP synthase. The supplementary STRING results support mitochondrial matrix, transit-peptide, heart-tissue and amino-acid or urea-cycle associations (10 supplementary STRING terms; within-query FDR 0.0026–0.0465). However, no GO or KEGG term passed global multiple-testing correction, so these annotations are an informed functional interpretation rather than globally significant enrichment. The module may therefore represent coordinated abundance of core mitochondrial proteins and related metabolic proteins rather than a narrowly defined pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the genes are predominantly intracellular, with mitochondrial, endoplasmic-reticulum, endosomal or lysosomal localizations, and only MESD has an intracellular-and-membrane secretome annotation. All genes have low immune-cell specificity in HPA, with no enriched blood-cell category, arguing against a simple blood-cell signal. Most genes show enhanced specificity for selected tissues or cell types rather than ubiquitous housekeeping expression, including skeletal muscle, tongue, liver, heart muscle and several trophoblast or epithelial cell types. The HPA pattern is therefore compatible with shared metabolic or contractile-cell composition, but it does not establish that the bone-myometrium module originates from a particular cell type. Protein detection in myometrium supports presence of much of the module there, whereas the fact sheet provides no matching HPA bone tissue result.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING contains established high-confidence relationships linking ATP5F1A with ATP5F1B, CS and FH; linking CS with FH and GOT2; and linking FH with GOT2 and OAT. These known relationships form a coherent mitochondrial metabolic core and make the module less likely to be an arbitrary collection of co-abundant genes. The supplementary STRING tissue and pathway results are consistent with that core, but their original within-query FDR values are not global enrichment evidence. hu.MAP identifies ATP5F1A and ATP5F1B together in several complexes (hu.MAP huMAP3_08750.1) (hu.MAP huMAP3_09307.1) (hu.MAP huMAP3_11095.1), confirming their membership in ATP synthase-related assemblies. The other module genes do not have hu.MAP complexes with multiple module members in the supplied results, so the hu.MAP evidence supports only part of the module rather than one complete physical complex. RAB18, DDOST, CLTC and MESD provide network links or peripheral connections without supplied STRING or hu.MAP support for a shared physical complex.

**STRING interactions (score >= 0.7)**: 8 of 45 gene pairs: ATP5F1A–ATP5F1B (0.999); ATP5F1A–CS (0.94); ATP5F1A–FH (0.793); ATP5F1B–CS (0.917); CS–FH (0.993); CS–GOT2 (0.952); FH–GOT2 (0.979); FH–OAT (0.859)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Atrium (FDR = 0.0026, 5 genes); TISSUES Left ventricle (FDR = 0.0057, 5 genes); TISSUES Right atrium (FDR = 0.0057, 4 genes); TISSUES Left atrium (FDR = 0.009, 4 genes); TISSUES Subthalamic nucleus (FDR = 0.0109, 3 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.0222, 6 genes); Keyword Transit peptide (FDR = 0.0338, 6 genes); TISSUES Heart (FDR = 0.041, 6 genes); WikiPathways Amino acid metabolism (FDR = 0.0465, 4 genes); WikiPathways Urea cycle and associated pathways (FDR = 0.0465, 3 genes); WikiPathways 7q11.23 copy number variation syndrome (FDR = 0.0465, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08750.1 (ATP5F1B, ATP5F1A; 2/12); huMAP3_09307.1 (ATP5F1B, ATP5F1A; 2/35); huMAP3_11095.1 (ATP5F1B, ATP5F1A; 2/45)

### Novelty

The constituent biology is not new: mitochondrial ATP synthase, the tricarboxylic-acid cycle, amino-acid metabolism, vesicle trafficking and endoplasmic-reticulum protein processing are established processes, and several of the central protein relationships are already represented in STRING or hu.MAP. What may be new is the observation that these genes co-abundance as one conserved module across bone and myometrium. The fact sheet does not demonstrate that this exact cross-tissue module has been reported previously, but it also does not provide an external replication, perturbation experiment, or direct bone-to-myometrium mechanism. Accordingly, the defensible conclusion is that the cross-tissue co-abundance pattern is potentially novel, while its molecular components and much of its interaction structure are established. Lack of STRING or hu.MAP representation for some edges would not by itself prove novelty.

**Hypothesis.** Hypothesis: the conserved module reflects coordinated mitochondrial energy production and carbon or nitrogen flux in a shared metabolically active cell population present in bone and myometrium. CS may organize the co-abundance pattern around the tricarboxylic-acid cycle, with FH and GOT2 supporting carbon and amino-acid exchange, OAT linking ornithine and glutamate-related metabolism, and ATP5F1A plus ATP5F1B supporting ATP synthesis. MESD, DDOST, RAB18 and CLTC may reflect biosynthetic, trafficking or receptor-processing demands associated with that cellular state. This remains a hypothesis because the globally corrected GO/KEGG analysis was negative and co-abundance cannot establish physical interaction, causal regulation or a bone-myometrium signaling axis.

### Important genes

#### CS

- **Related proteins** (co-abundance neighbors): MESD (0.90), ATP5F1A (0.88), ATP5F1B (0.87), GOT2 (0.86), CLTC (0.85), OAT (0.84), FH (0.84); STRING partners: ATP5F1A (0.94), ATP5F1B (0.917), FH (0.993), GOT2 (0.952)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS is the central network gene, with the broadest connectivity and strongest aggregate network support in the module. It encodes citrate synthase, the entry enzyme of the tricarboxylic-acid cycle, is localized to mitochondria, and connects the ATP synthase subunits with GOT2, FH and OAT. It is represented in many of the supplementary STRING mitochondrial, tissue and amino-acid-metabolism terms (STRING TISSUES Atrium; within-query FDR = 0.0026), (STRING TISSUES Left ventricle; within-query FDR = 0.0057), (STRING TISSUES Left atrium; within-query FDR = 0.009), (4 supplementary STRING terms; within-query FDR 0.0222–0.0465). Its extensive literature and disease associations make it the best anchor for interpreting the module as mitochondrial metabolic coordination.
- **Conclusion**: Established evidence supports CS as both the network hub and a core tricarboxylic-acid-cycle enzyme. The hypothesis that CS-driven carbon flux explains conservation of the module between bone and myometrium is plausible but not demonstrated by these data.

#### ATP5F1A

- **Related proteins** (co-abundance neighbors): ATP5F1B (0.97), CS (0.88), RAB18 (0.88), DDOST (0.83), CLTC (0.82); STRING partners: ATP5F1B (0.999), CS (0.94), FH (0.793)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_08750.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit alpha. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, using an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic po…
- **Diseases (Open Targets)**: mitochondrial complex V (ATP synthase) deficiency, nuclear type 4A (0.655); mitochondrial proton-transporting ATP synthase complex deficiency (0.648); mitochondrial complex V (ATP synthase) deficiency, nuclear type 4B (0.532); hereditary disease (0.394); Mitochondrial encephalopathy (0.371)
- **Europe PMC papers**: 822
- **Why important**: ATP5F1A is a highly connected member of the module and is tightly linked to ATP5F1B, CS and FH in STRING. It encodes the alpha subunit of the mitochondrial ATP synthase F1 catalytic sector and is present in all supplied hu.MAP complexes containing multiple module members (hu.MAP huMAP3_08750.1) (hu.MAP huMAP3_09307.1) (hu.MAP huMAP3_11095.1). It also appears across the supplementary mitochondrial, heart-tissue and ATP-synthase-related results (4 supplementary STRING terms; within-query FDR 0.0026–0.009), (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.0222) (STRING Keyword Transit peptide; within-query FDR = 0.0338) (STRING TISSUES Heart; within-query FDR = 0.041), (STRING WikiPathways 7q11.23 copy number variation syndrome; within-query FDR = 0.0465), and has established associations with mitochondrial complex V deficiency.
- **Conclusion**: Established evidence supports ATP5F1A as a physical-complex marker and an indicator of oxidative-phosphorylation capacity. Its role as a driver of the shared bone-myometrium co-abundance pattern remains hypothetical.

#### ATP5F1B

- **Related proteins** (co-abundance neighbors): ATP5F1A (0.97), CS (0.87), RAB18 (0.85); STRING partners: ATP5F1A (0.999), CS (0.917)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_08750.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit beta. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: hypermetabolism due to uncoupled mitochondrial oxidative phosphorylation 2 (0.499); hypertrophic cardiomyopathy (0.212); Alzheimer disease (0.177); hypertensive disorder (0.117); response to xenobiotic stimulus (0.117)
- **Europe PMC papers**: 735
- **Why important**: ATP5F1B is the partner of ATP5F1A in the F1 catalytic sector and is supported by the same three hu.MAP complexes (hu.MAP huMAP3_08750.1) (hu.MAP huMAP3_09307.1) (hu.MAP huMAP3_11095.1). Its STRING links to ATP5F1A and CS, its mitochondrial localization, and its annotations involving ATP biosynthesis, osteoblast differentiation and muscle activity make it particularly relevant to a module shared by bone and myometrium. It also has established associations with mitochondrial ATP-synthase deficiency and other metabolic or cardiac phenotypes.
- **Conclusion**: Established evidence supports ATP5F1B as a biologically meaningful oxidative-phosphorylation component and as a marker of the ATP synthase part of the module. The bone and myometrium relevance is compatible with the annotations but does not establish tissue-specific causality.

#### FH

- **Related proteins** (co-abundance neighbors): CS (0.84); STRING partners: ATP5F1A (0.793), CS (0.993), GOT2 (0.979), OAT (0.859)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fumarate hydratase. The protein encoded by this gene is an enzymatic component of the tricarboxylic acid (TCA) cycle, or Krebs cycle, and catalyzes the formation of L-malate from fumarate. It exists in both a cytosolic form and an N-terminal extended form, differing only in the translation start site used. The N-terminal extended form is targeted to the mitochondrion, where the removal of the extension generates the …
- **Diseases (Open Targets)**: hereditary leiomyomatosis and renal cell cancer (0.838); fumaric aciduria (0.820); hereditary neoplastic syndrome (0.580); Multiple cutaneous leiomyomas (0.575); neurodegenerative disease (0.482)
- **Europe PMC papers**: 42469
- **Why important**: FH is a mitochondrial and cytosolic fumarate hydratase that links fumarate and malate metabolism to the tricarboxylic-acid cycle and urea-cycle-related processes. It has strong STRING relationships with CS, GOT2 and OAT and appears repeatedly in the supplementary mitochondrial, tissue and amino-acid or urea-cycle results (4 supplementary STRING terms; within-query FDR 0.0026–0.009), (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.0222), (STRING TISSUES Heart; within-query FDR = 0.041) (STRING WikiPathways Amino acid metabolism; within-query FDR = 0.0465) (STRING WikiPathways Urea cycle and associated pathways; within-query FDR = 0.0465). Its extensive literature and strong associations with hereditary leiomyomatosis and renal cell cancer, fumaric aciduria and related syndromes make it an important disease-relevant metabolic node.
- **Conclusion**: Established evidence supports FH as a central biochemical bridge within the module and as a clinically important metabolic enzyme. A role for FH in coordinating the shared module across bone and myometrium is a hypothesis rather than an established mechanism.

#### MESD

- **Related proteins** (co-abundance neighbors): CS (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mesoderm development LRP chaperone. Predicted to enable low-density lipoprotein particle receptor binding activity. Involved in ossification and protein folding. Located in endoplasmic reticulum. Implicated in osteogenesis imperfecta type 20. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: osteogenesis imperfecta, type 20 (0.713); osteogenesis imperfecta (0.463); Abnormality of the skeletal system (0.416); osteogenesis imperfecta type 2 (0.370); Hernia of the abdominal wall (0.190)
- **Europe PMC papers**: 405
- **Why important**: MESD is a peripheral network member connected to the CS hub, but it is especially relevant to the bone context because it is annotated for ossification, mesoderm development, protein folding and positive regulation of Wnt signaling, and is associated with osteogenesis imperfecta type twenty. It is localized to the endoplasmic reticulum and has HPA detection in myometrium, providing a possible link between metabolic activity and protein-folding or developmental processes.
- **Conclusion**: Established evidence supports MESD as an endoplasmic-reticulum LRP chaperone with skeletal-development relevance. Its connection to CS in this module may reflect coordinated cellular state, but a direct functional bridge between MESD and the mitochondrial metabolic core is not established here.

## Module 4

**Tissue pair**: bone and myometrium  
**Genes (24)**: ACO1, ANXA6, CAPN1, CAPN2, DNM1L, ENAH, FERMT2, GARS1, GSN, GBE1, HSP90AB2P, HSP90AA1, HSPA8, KATNAL2, NIBAN2, REXO2, PFKM, PFKP, PGM2, CTPS1, STAT1, SWAP70, TARS1, VPS35

### Function

This is a mixed intracellular co-abundance module rather than a module with a demonstrated single canonical pathway. Its genes converge on cytosolic metabolism, protein folding and stress handling, actin and membrane organization, mitochondrial dynamics, intracellular trafficking, and calcium-responsive proteolysis. The strongest functional interpretation comes from the gene annotations and the repeated supplementary STRING themes of cytoplasm and cytosol (STRING Keyword Cytoplasm; within-query FDR = 0.0094) (STRING COMPARTMENTS Cytosol; within-query FDR = 0.0347), with necroptosis-related membership (STRING KEGG Necroptosis; within-query FDR = 0.0242). However, no GO or KEGG term passed global correction, so these observations do not establish statistically significant pathway enrichment. The network contains a relatively connected metabolic and proteostasis core around TARS1, GARS1, ACO1, HSP90AA1, DNM1L and CAPN2, plus more specialized substructures involving the calpains, phosphofructokinases, glycogen metabolism, actin regulation and focal adhesion. Overall, the module is most consistent with a shared cellular maintenance, energetic and contractile-state program, rather than a bone- or myometrium-specific biological process.

**Cell composition.** The module is not dominated by plasma or secreted proteins and is not strongly blood-cell enriched. HPA evidence indicates mostly low tissue specificity and generally low immune-cell specificity, with only a small subset showing immune-cell enhancement. GSN is secreted to blood and has eosinophil enhancement, while SWAP70 and NIBAN2 show blood-cell associations, so blood or immune contribution cannot be excluded for those components. Most genes are intracellular and broadly expressed or cell-type enhanced, including metabolic enzymes, chaperones, cytoskeletal regulators and trafficking proteins. Several genes have smooth-muscle or muscle-related HPA signals, and myometrium protein detection is common among the detected proteins, but bone protein evidence is unavailable in the supplied HPA summary. The shared module may therefore reflect common resident-cell composition or a general contractile, energetic and stress-adaptation state rather than secretion or blood contamination alone.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited set of direct, high-confidence relationships: the CAPN1-CAPN2 pair, the HSP90AA1-HSPA8 and HSP90AA1-STAT1 relationships, the PFKM-PFKP pair, the GARS1-TARS1 pair, the GBE1-PGM2 pair, and the DNM1L-VPS35 relationship. These links provide independent support for several recognizable submodules, especially calpain proteolysis, chaperone and signaling interactions, glycolysis, aminoacyl-tRNA synthesis, glycogen metabolism and organelle trafficking. The STRING functional terms remain supplementary (STRING Keyword Cytoplasm; within-query FDR = 0.0094) (STRING KEGG Necroptosis; within-query FDR = 0.0242) (STRING COMPARTMENTS Cytosol; within-query FDR = 0.0347) and are not global enrichment evidence. hu.MAP independently recovers the CAPN1-CAPN2 pair across multiple calpain-containing complexes (hu.MAP huMAP3_03767.1) (hu.MAP huMAP3_08670.1) (hu.MAP huMAP3_09127.1) (hu.MAP huMAP3_09328.1) (hu.MAP huMAP3_10242.1) (hu.MAP huMAP3_13615.1) (hu.MAP huMAP3_14229.1) (hu.MAP huMAP3_11557.1) (hu.MAP huMAP3_12716.1) (hu.MAP huMAP3_12926.1), the PFKM-PFKP complex (hu.MAP huMAP3_04277.1), and the ACO1-REXO2 complex (hu.MAP huMAP3_12414.1). The repeated calpain complexes suggest that this part of the module reflects a known protease-centered relationship, whereas most other module edges lack corresponding STRING or hu.MAP support and may represent co-abundance, indirect coupling or context-dependent associations.

**STRING interactions (score >= 0.7)**: 7 of 276 gene pairs: CAPN1–CAPN2 (0.978); DNM1L–VPS35 (0.9); GARS1–TARS1 (0.909); GBE1–PGM2 (0.714); HSP90AA1–HSPA8 (0.999); HSP90AA1–STAT1 (0.868); PFKM–PFKP (0.991)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Cytoplasm (FDR = 0.0094, 21 genes); KEGG Necroptosis (FDR = 0.0242, 5 genes); COMPARTMENTS Cytosol (FDR = 0.0347, 19 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03767.1 (CAPN1, CAPN2; 2/3); huMAP3_08670.1 (CAPN1, CAPN2; 2/4); huMAP3_04277.1 (PFKM, PFKP; 2/4); huMAP3_12414.1 (ACO1, REXO2; 2/5); huMAP3_09127.1 (CAPN1, CAPN2; 2/5); huMAP3_09328.1 (CAPN1, CAPN2; 2/6); huMAP3_10242.1 (CAPN1, CAPN2; 2/6); huMAP3_13615.1 (CAPN1, CAPN2; 2/7); huMAP3_14229.1 (CAPN1, CAPN2; 2/7); huMAP3_11557.1 (CAPN1, CAPN2; 2/8); huMAP3_12716.1 (CAPN1, CAPN2; 2/8); huMAP3_12926.1 (CAPN1, CAPN2; 2/8)

### Novelty

The module should not be claimed as a wholly new molecular complex or pathway. Its calpain, phosphofructokinase, chaperone, aminoacyl-tRNA synthetase, glycogen-related and trafficking relationships are already represented in STRING or hu.MAP, and the individual functions of many genes are established. What may be novel is the coordinated co-abundance of this particular combination across bone and myometrium, especially the connection between the known substructures and the less-supported genes. That claim remains provisional because co-abundance does not prove physical interaction, causality or tissue-specific regulation, and absence from interaction databases does not demonstrate novelty. The appropriate conclusion is a potentially novel cross-tissue expression module built partly from known molecular relationships, requiring replication and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a shared resident-cell state in bone and myometrium in which energetic demand and cytoskeletal remodeling are coupled to proteostasis, calcium-sensitive proteolysis and mitochondrial quality control. In this model, glycolytic and glycogen-related genes support energy production, ACO1 and DNM1L connect metabolism to mitochondrial organization, CAPN1 and CAPN2 regulate remodeling of cellular proteins and structures, while GSN, ANXA6, FERMT2, ENAH and SWAP70 support actin, membrane and adhesion dynamics. HSP90AA1, HSPA8 and STAT1 may represent stress-responsive signaling and protein-maintenance inputs. This is a mechanistic hypothesis, not an experimentally established pathway; the co-abundance data cannot determine whether these genes act in the same cells or whether one process drives the others.

### Important genes

#### CAPN1

- **Related proteins** (co-abundance neighbors): PFKM (0.93), SWAP70 (0.89), CTPS1 (0.87), PGM2 (0.84), ACO1 (0.84), VPS35 (0.84), CAPN2 (0.84), GSN (0.83); STRING partners: CAPN2 (0.978)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_03767.1, huMAP3_08670.1, huMAP3_09127.1, huMAP3_09328.1, huMAP3_10242.1, huMAP3_13615.1, huMAP3_14229.1, huMAP3_11557.1, huMAP3_12716.1, huMAP3_12926.1
- **Function (MyGene.info)**: calpain 1. The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpa…
- **Diseases (Open Targets)**: Autosomal recessive spastic paraplegia type 76 (0.781); Alzheimer disease (0.383); neurodegenerative disease (0.326); hereditary spastic paraplegia 11 (0.266); hereditary disease (0.193)
- **Europe PMC papers**: 1869
- **Why important**: CAPN1 is a central and highly connected module member and has a direct STRING relationship with CAPN2. It is also present with CAPN2 in many independent hu.MAP calpain complexes (hu.MAP huMAP3_03767.1) (hu.MAP huMAP3_08670.1) (hu.MAP huMAP3_09127.1) (hu.MAP huMAP3_09328.1) (hu.MAP huMAP3_10242.1) (hu.MAP huMAP3_13615.1) (hu.MAP huMAP3_14229.1) (hu.MAP huMAP3_11557.1) (hu.MAP huMAP3_12716.1) (hu.MAP huMAP3_12926.1). Its established function as a calcium-activated intracellular protease links the module to proteolysis, structural remodeling and cellular stress. It has strong disease and literature support, including an association with hereditary spastic paraplegia and extensive study. HPA places it in myometrium and in several epithelial, trophoblast and platelet-associated cell contexts.
- **Conclusion**: Established: CAPN1 is a plausible structural anchor for a known calpain submodule and provides a credible connection between calcium-sensitive proteolysis and the shared network. Hypothesis: CAPN1 may help couple contractile or mechanical cellular states to remodeling in both tissues, but the module does not show that CAPN1 activity causes the cross-tissue co-abundance pattern.

#### CAPN2

- **Related proteins** (co-abundance neighbors): TARS1 (0.92), DNM1L (0.91), ACO1 (0.88), GARS1 (0.87), CAPN1 (0.84), SWAP70 (0.82); STRING partners: CAPN1 (0.978)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Connecting piece, Mid piece; IHC detected in none
- **hu.MAP 3.0**: huMAP3_03767.1, huMAP3_08670.1, huMAP3_09127.1, huMAP3_09328.1, huMAP3_10242.1, huMAP3_13615.1, huMAP3_14229.1, huMAP3_11557.1, huMAP3_12716.1, huMAP3_12926.1
- **Function (MyGene.info)**: calpain 2. The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpa…
- **Diseases (Open Targets)**: Alzheimer disease (0.389); urolithiasis (0.288); alcohol drinking (0.288); aortic stenosis (0.141); neoplasm (0.105)
- **Europe PMC papers**: 1796
- **Why important**: CAPN2 forms the strongest and most repeatedly supported submodule relationship with CAPN1 in STRING and hu.MAP (hu.MAP huMAP3_03767.1) (hu.MAP huMAP3_08670.1) (hu.MAP huMAP3_09127.1) (hu.MAP huMAP3_09328.1) (hu.MAP huMAP3_10242.1) (hu.MAP huMAP3_13615.1) (hu.MAP huMAP3_14229.1) (hu.MAP huMAP3_11557.1) (hu.MAP huMAP3_12716.1) (hu.MAP huMAP3_12926.1). Its annotated roles include proteolysis, response to hypoxia, response to mechanical stimulus and pregnancy-related biology, which are relevant to tissue remodeling and myometrial physiology. It occupies a connected position linking the calpains to TARS1, GARS1, ACO1, DNM1L and SWAP70. It also has substantial disease and literature support.
- **Conclusion**: Established: CAPN2 is part of a well-supported calpain pair and is a strong candidate for the module's proteolytic and mechanically responsive component. Hypothesis: CAPN2 could mediate remodeling downstream of energetic or mechanical stress shared by bone and myometrium, although this requires activity-level and cell-specific testing.

#### PFKM

- **Related proteins** (co-abundance neighbors): CAPN1 (0.93), CTPS1 (0.87); STRING partners: PFKP (0.991)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_04277.1
- **Function (MyGene.info)**: phosphofructokinase, muscle. Three phosphofructokinase isozymes exist in humans: muscle, liver and platelet. These isozymes function as subunits of the mammalian tetramer phosphofructokinase, which catalyzes the phosphorylation of fructose-6-phosphate to fructose-1,6-bisphosphate. Tetramer composition varies depending on tissue type. This gene encodes the muscle-type isozyme. Mutations in this gene have been associated with g…
- **Diseases (Open Targets)**: glycogen storage disease VII (0.819); disorder of glycogen metabolism (0.372); peroxisome biogenesis disorder (0.333); neurodegenerative disease (0.319); anemia (phenotype) (0.288)
- **Europe PMC papers**: 2506
- **Why important**: PFKM is the muscle-type phosphofructokinase and is linked to PFKP by STRING as well as jointly represented in a hu.MAP complex (hu.MAP huMAP3_04277.1). Its established role in glycolysis and its HPA group enrichment in skeletal muscle make it informative for interpreting the bone-myometrium shared state, especially alongside GBE1 and PGM2. Its disease association with Tarui disease demonstrates that perturbing this metabolic function has direct physiological consequences. It is less central in the co-abundance graph than the calpains, but it provides a specific metabolic anchor rather than a generic housekeeping interpretation.
- **Conclusion**: Established: PFKM supports a glycolytic and muscle-associated component of the module. Hypothesis: coordinated PFKM abundance may indicate increased or altered energetic demand in shared contractile or mechanically active cells, but it does not prove increased glycolytic flux.

#### DNM1L

- **Related proteins** (co-abundance neighbors): GARS1 (0.92), CAPN2 (0.91), TARS1 (0.90), ACO1 (0.88), HSP90AB2P (0.85), STAT1 (0.84), FERMT2 (0.82); STRING partners: VPS35 (0.9)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 1L. This gene encodes a member of the dynamin superfamily of GTPases. The encoded protein mediates mitochondrial and peroxisomal division, and is involved in developmentally regulated apoptosis and programmed necrosis. Dysfunction of this gene is implicated in several neurological disorders, including Alzheimer's disease. Mutations in this gene are associated with the autosomal dominant disorder, ence…
- **Diseases (Open Targets)**: encephalopathy, lethal, due to defective mitochondrial peroxisomal fission 1 (0.815); autosomal dominant optic atrophy, classic form (0.721); neurodegenerative disease (0.531); encephalopathy due to mitochondrial and peroxisomal fission defect (0.455); hereditary disease (0.451)
- **Europe PMC papers**: 3015
- **Why important**: DNM1L is a relatively central connector whose module neighbors include GARS1, TARS1, ACO1, CAPN2, HSP90AB2P, STAT1 and FERMT2. Its STRING relationship with VPS35 supports a link between mitochondrial or peroxisomal dynamics and intracellular trafficking. The established functions of DNM1L include mitochondrial and peroxisomal fission, organelle organization and programmed cell death, and it has well-documented neurological disease associations with substantial literature support. Its HPA profile is broadly expressed and detected in myometrium.
- **Conclusion**: Established: DNM1L supplies a credible organelle-dynamics component and connects several otherwise distinct functional neighborhoods. Hypothesis: altered mitochondrial remodeling may coordinate energy management, stress responses and structural adaptation in the shared module, but co-abundance alone cannot distinguish adaptive remodeling from damage or cell-composition effects.

#### ACO1

- **Related proteins** (co-abundance neighbors): HSP90AA1 (0.93), TARS1 (0.91), GARS1 (0.89), DNM1L (0.88), CAPN2 (0.88), CAPN1 (0.84), CTPS1 (0.84), PGM2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12414.1
- **Function (MyGene.info)**: aconitase 1. The protein encoded by this gene is a bifunctional, cytosolic protein that functions as an essential enzyme in the TCA cycle and interacts with mRNA to control the levels of iron inside cells. When cellular iron levels are high, this protein binds to a 4Fe-4S cluster and functions as an aconitase. Aconitases are iron-sulfur proteins that function to catalyze the conversion of citrate to isocitrate…
- **Diseases (Open Targets)**: smoking initiation (0.300); smoking behavior (0.277); ovarian neoplasm (0.276); attention deficit-hyperactivity disorder (0.261); substance abuse (0.261)
- **Europe PMC papers**: 3372
- **Why important**: ACO1 is among the more connected genes in the module and links HSP90AA1, TARS1, GARS1, DNM1L, CAPN1, CAPN2, CTPS1 and PGM2. Its established bifunctional role in citrate-to-isocitrate conversion and intracellular iron regulation makes it a bridge between central metabolism, redox-related cellular state and post-transcriptional regulation. It has very extensive literature support and a hu.MAP association with REXO2 (hu.MAP huMAP3_12414.1), although no direct STRING partner is reported in the supplied evidence. HPA shows tissue enhancement in liver and cell-type enhancement in adipocytes, hepatocytes and proximal tubule cells, arguing for broad metabolic relevance rather than a specific bone or myometrium identity.
- **Conclusion**: Established: ACO1 is a plausible metabolic and iron-responsive connector within the module. Hypothesis: ACO1 may couple cellular energetic state and iron handling to mitochondrial and proteostasis responses, but the supplied data do not establish altered aconitase activity or iron regulation in either tissue.

#### GSN

- **Related proteins** (co-abundance neighbors): ANXA6 (0.91), GBE1 (0.88), VPS35 (0.84), CTPS1 (0.84), CAPN1 (0.83), GARS1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gelsolin. The protein encoded by this gene binds to the 'plus' ends of actin monomers and filaments to prevent monomer exchange. The encoded calcium-regulated protein functions in both assembly and disassembly of actin filaments. Defects in this gene are a cause of familial amyloidosis Finnish type (FAF). Multiple transcript variants encoding several different isoforms have been found for this gene. [provid…
- **Diseases (Open Targets)**: Finnish type amyloidosis (0.805); AL amyloidosis (0.463); neuropathy (0.418); cardiomyopathy (0.418); cutis laxa (0.417)
- **Europe PMC papers**: 5062
- **Why important**: GSN connects ANXA6, GBE1, VPS35, CTPS1, CAPN1 and GARS1 and therefore links actin organization to trafficking, metabolism and calpain-related remodeling. Its established function is calcium-regulated actin filament assembly and disassembly, and it has extensive literature and disease support, including Finnish-type amyloidosis. HPA places it in myometrium, associates it with heart muscle and vascular or stromal cell contexts, and identifies it as secreted to blood with eosinophil enhancement. That combination makes GSN biologically informative but also important for evaluating possible blood or extracellular contributions.
- **Conclusion**: Established: GSN is a strong cytoskeletal connector and a plausible marker of actin remodeling, with a potential circulating component. Hypothesis: GSN may link calcium-dependent cytoskeletal adaptation to the metabolic and proteolytic parts of the module, but its secreted blood association means that tissue-cell origin should be verified before assigning it a resident-cell mechanism.

## Module 5

**Tissue pair**: bone and myometrium  
**Genes (7)**: ACO2, HSPA5, CANX, PDIA4, PPCS, RRBP1, SEC23A

### Function

The strongest interpretation is an endoplasmic-reticulum proteostasis and secretory-trafficking module. (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00209) identifies protein processing in the endoplasmic reticulum and includes CANX, HSPA5, PDIA4, RRBP1, and SEC23A. This is concordant with the known functions of HSPA5 as an ER chaperone and regulator of ER homeostasis, CANX as an ER glycoprotein-folding chaperone, PDIA4 as a disulfide-isomerase and protein-folding factor, RRBP1 as an ER membrane ribosome-binding and secretory-pathway protein, and SEC23A as a COPII transport component. The supplementary STRING terms (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.00034), (STRING NetworkNeighborAL Mixed, incl. Photodynamic therapy-induced unfolded protein response, and Endoplasmic reticulum quality control compartment; within-query FDR = 0.0021), and (STRING RCTM Antigen Presentation: Folding, assembly and peptide loading of class I MHC; within-query FDR = 0.017) reinforce ER protein folding, ER quality control, and ER-to-Golgi handling, but they are not additional globally corrected evidence. (STRING KEGG Thyroid hormone synthesis; within-query FDR = 0.0121) is compatible with the same chaperone-centered biology but should remain supplementary. ACO2 and PPCS add mitochondrial energy and coenzyme-A biology to the co-abundance neighborhood, without contributing to the primary GO/KEGG enrichment.

**Cell composition.** This does not look like a module dominated by plasma proteins, secreted proteins, or blood cells. The HPA summary indicates broadly distributed expression for most genes, low immune-cell specificity for nearly all members, and only a minority classified as secreted. Several genes show cell-type enhancement, including secretory or trophoblast-related cell types, while RRBP1 has immune-cell enhancement in HPA. Myometrium protein detection is present for most members, whereas bone lacks matching HPA tissue data. Thus, the shared signal is more consistent with a broadly expressed intracellular ER and metabolic program, potentially influenced by shared smooth-muscle or secretory-cell content, than with a simple blood-contamination signature. HPA alone cannot establish the precise cellular source in bone.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human) | 0.00209 | CANX, HSPA5, PDIA4, RRBP1, SEC23A |

### STRING and hu.MAP

STRING provides strong support for a compact ER chaperone subnetwork: CANX, HSPA5, and PDIA4 are mutually connected by high-confidence associations. These relationships are biologically established and agree with their roles in ER folding and quality control. STRING also recovers the broader ER-processing and antigen-presentation-related context in (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.00034), (STRING NetworkNeighborAL Mixed, incl. Photodynamic therapy-induced unfolded protein response, and Endoplasmic reticulum quality control compartment; within-query FDR = 0.0021), and (STRING RCTM Antigen Presentation: Folding, assembly and peptide loading of class I MHC; within-query FDR = 0.017). The remaining co-abundance relationships, including those involving ACO2, PPCS, SEC23A, and RRBP1, are not represented by high-confidence STRING partnerships in the fact sheet. No hu.MAP complex contains multiple module members. Therefore, the network combines a known ER-chaperone core with co-abundance links that may reflect coordinated regulation, indirect cellular context, or tissue-specific coupling rather than one experimentally established multiprotein complex.

**STRING interactions (score >= 0.7)**: 3 of 21 gene pairs: CANX–HSPA5 (0.998); CANX–PDIA4 (0.931); HSPA5–PDIA4 (0.99)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Protein processing in endoplasmic reticulum (FDR = 0.00034, 5 genes); NetworkNeighborAL Mixed, incl. Photodynamic therapy-induced unfolded protein response, and Endoplasmic reticulum quality control compartment (FDR = 0.0021, 4 genes); KEGG Thyroid hormone synthesis (FDR = 0.0121, 3 genes); RCTM Antigen Presentation: Folding, assembly and peptide loading of class I MHC (FDR = 0.017, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The underlying biology is not new: ER chaperoning, disulfide-bond formation, ER quality control, and COPII trafficking are established processes, and the STRING links among CANX, HSPA5, and PDIA4 are already known. The module is also not supported as a newly discovered hu.MAP complex. What may be novel is the coordinated co-abundance of this ER-centered program with ACO2, PPCS, SEC23A, and RRBP1 across bone and myometrium. However, absence from STRING or hu.MAP does not prove novelty, and the present evidence cannot distinguish a new biological interaction from shared regulation, cell composition, or technical co-abundance. The appropriate conclusion is a potentially novel tissue-pair co-abundance pattern built around a largely established ER proteostasis program, not a proven new pathway or complex.

**Hypothesis.** Hypothesis: in both bone and myometrium, cellular demand for synthesis, folding, quality control, and export of proteins coordinately regulates an ER program centered on HSPA5, CANX, PDIA4, RRBP1, and SEC23A. This program may be coupled to mitochondrial citrate-cycle activity through ACO2 and to CoA biosynthetic capacity through PPCS, linking secretory proteostasis with cellular energy and biosynthetic state. In bone, RRBP1-associated secretory organization could be relevant to osteoblast-related activity, while in myometrium the same program could reflect smooth-muscle or secretory-cell physiology. These tissue-specific extensions are hypotheses; the established evidence supports the ER proteostasis and trafficking core more directly than the proposed metabolic coupling.

### Important genes

#### PDIA4

- **Related proteins** (co-abundance neighbors): ACO2 (0.91), PPCS (0.88), RRBP1 (0.86), CANX (0.86), HSPA5 (0.85); STRING partners: CANX (0.931), HSPA5 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 has the strongest network position in the module and connects the ER-centered members with the peripheral co-abundance genes. Its ER localization, multiple thioredoxin domains, disulfide-isomerase activity, and roles in protein folding, secretion, and ER stress directly explain the module's primary (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00209) signal. Its STRING links to CANX and HSPA5 provide established support for the chaperone core. Its disease associations include neurodegenerative disease, neoplasm, liver disorder, and ovarian disease, and its literature volume is substantial.
- **Conclusion**: Established: PDIA4 is a central ER protein-folding and disulfide-processing component and a strong anchor for the module's interpretation. Hypothesis: its network position may make it a regulatory or rate-limiting connector between ER proteostasis and the peripheral metabolic genes, but co-abundance does not establish that causal role.

#### HSPA5

- **Related proteins** (co-abundance neighbors): ACO2 (0.93), CANX (0.86), PDIA4 (0.85); STRING partners: CANX (0.998), PDIA4 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is a core ER HSP70 chaperone and master regulator of ER homeostasis. It participates in (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00209) and all of the relevant supplementary STRING contexts, including ER quality control and antigen-presentation-related folding. Its very strong STRING relationships with CANX and PDIA4 identify a well-established chaperone-centered core. It has broad tissue distribution, myometrium protein detection, extensive disease relevance in the supplied resources, and the largest literature volume among the selected genes.
- **Conclusion**: Established: HSPA5 is a compelling marker of ER folding capacity and proteostasis stress in this module. Hypothesis: coordinated HSPA5 abundance may report a shared increase in secretory or folding demand in bone and myometrium, but the data do not prove activation of an unfolded-protein response.

#### CANX

- **Related proteins** (co-abundance neighbors): PDIA4 (0.86), HSPA5 (0.86); STRING partners: HSPA5 (0.998), PDIA4 (0.931)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is an ER lectin chaperone that assists folding and assembly of newly synthesized glycoproteins and supports retention of misfolded proteins. It belongs to (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00209) and the supplementary STRING terms, and its strong links with HSPA5 and PDIA4 form the most clearly established interaction-centered portion of the module. Its ER localization and myometrium detection fit the tissue-pair context. Its disease associations span neurodegenerative and viral-infection-related conditions, and it has a substantial literature base.
- **Conclusion**: Established: CANX is a mechanistically appropriate component of the ER quality-control core. Hypothesis: CANX may couple glycoprotein quality control to the tissue-specific secretory burden represented by the module, but the co-abundance data do not identify the relevant client proteins.

#### SEC23A

- **Related proteins** (co-abundance neighbors): ACO2 (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A supplies the ER-exit and COPII-trafficking arm of the module. It is included in (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00209) and (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.00034) and is annotated for ER-to-Golgi transport, vesicle budding, and cargo loading. Its co-abundance connection to ACO2 may link trafficking capacity to cellular metabolic state, although no high-confidence STRING partner is listed for it in this module. Its disease associations include craniolenticulosutural dysplasia and other systemic conditions, and it has a meaningful literature base.
- **Conclusion**: Established: SEC23A supports interpretation of the module as extending beyond folding into export of ER cargo. Hypothesis: its association with ACO2 may reflect coordinated control of energy supply and secretory trafficking, but this proposed coupling requires independent validation.

#### RRBP1

- **Related proteins** (co-abundance neighbors): PDIA4 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosome binding protein 1. This gene encodes a ribosome-binding protein of the endoplasmic reticulum (ER) membrane. Studies suggest that this gene plays a role in ER proliferation, secretory pathways and secretory cell differentiation, and mediation of ER-microtubule interactions. Alternative splicing has been observed and protein isoforms are characterized by regions of N-terminal decapeptide and C-terminal heptad repeats.…
- **Diseases (Open Targets)**: cancer (0.476); dengue disease (0.462); neurodegenerative disease (0.324); coronary artery disorder (0.292); placental abruption (0.279)
- **Europe PMC papers**: 1654
- **Why important**: RRBP1 is an ER membrane ribosome-binding protein involved in ER organization, secretory pathways, secretory-cell differentiation, and ER-microtubule interactions. It contributes to (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00209) and (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.00034) and is connected to PDIA4 in the co-abundance graph. Its HPA enrichment in pancreatic and salivary acinar cells and its supplied association with osteoblast differentiation make it relevant to possible secretory-cell and bone-related interpretations. Its disease associations include cancer, neurodegenerative disease, coronary artery disorder, and placental abruption, with a substantial literature base.
- **Conclusion**: Established: RRBP1 provides an ER architecture and secretory-organization explanation for the module and may be particularly relevant to tissue-specific secretory states. Hypothesis: RRBP1 could connect ER structural organization with bone-cell secretory activity in this shared module, but the current evidence cannot establish cell type or direction of effect.

## Module 6

**Tissue pair**: bone and myometrium  
**Genes (10)**: AP1B1, COPB1, COPS7A, HSPH1, NUDCD2, PSMF1, UPF1, SEC24C, VARS1, USO1

### Function

The most coherent interpretation is a conserved intracellular protein-trafficking and proteostasis module, centered on endoplasmic-reticulum-to-Golgi transport, vesicle coating, cargo handling, and Golgi trafficking. This interpretation is supported by the functions of SEC24C, COPB1, USO1, and AP1B1, together with the supplementary STRING compartment terms for Golgi-associated, transport, coated, and vesicle-coat structures (6 supplementary STRING terms; within-query FDR 0.007–0.0363). SEC24C represents COPII cargo selection and budding from the endoplasmic reticulum; COPB1 represents coatomer-dependent Golgi and retrograde trafficking; USO1 supports COPII vesicle tethering and fusion at the Golgi; and AP1B1 supports clathrin-associated sorting at the Golgi. The remaining genes broaden the module toward protein quality control, translation, RNA surveillance, and ubiquitin-pathway regulation: HSPH1 and NUDCD2 are linked to protein folding, PSMF1 to proteasome regulation, COPS7A to COP9-signalosome control, VARS1 to translational fidelity, and UPF1 to nonsense-mediated decay and RNA surveillance. No GO or KEGG term passed global correction. Therefore, the trafficking interpretation is biologically coherent but should be treated as an integrated interpretation of gene functions, network structure, and supplementary STRING evidence rather than as globally significant GO or KEGG enrichment.

**Cell composition.** The module does not have the profile of a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly intracellular, with locations including the Golgi apparatus, vesicles, cytosol, endoplasmic reticulum, nucleoplasm, and microtubules. It also does not show strong blood-cell composition. HPA reports low immune-cell specificity for most genes, with the remainder not detected in immune cells, and no recurrent enriched blood-cell category. Most genes have low tissue specificity, which is compatible with broadly expressed cellular machinery rather than a tissue-restricted program. HPA does identify isolated cell-type or tissue-enhanced signals, including skeletal muscle and myonuclei for USO1, as well as several reproductive or immune-associated cell types for individual genes. These isolated annotations do not establish blood contamination or a shared immune-cell source. The shared bone–myometrium signal is more plausibly related to common intracellular trafficking, folding, and RNA or protein quality-control requirements, although shared cell composition cannot be excluded.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a focused, internally coherent interaction core among COPB1, USO1, and SEC24C: all three pairwise relationships are present at the stated high-confidence threshold, with the strongest support involving COPB1–USO1. The supplementary STRING enrichment terms (6 supplementary STRING terms; within-query FDR 0.007–0.0363) consistently implicate Golgi-associated, transport, coated, and vesicle-coat compartments, and repeatedly involve COPB1, USO1, SEC24C, and AP1B1. These are useful supporting observations, but their reported FDR values are not global corrections across modules and must not be treated as globally significant enrichment. The hu.MAP evidence independently connects USO1, SEC24C, and AP1B1 within complex C1 (hu.MAP huMAP3_12394.1). This indicates that part of the module overlaps known trafficking and vesicle-associated molecular machinery. The other module edges are not supported by the supplied STRING or hu.MAP records. Thus, the module is not a single fully documented physical complex: it contains a known trafficking core plus co-abundance links to proteostasis, translation, and RNA-surveillance genes. Co-abundance may therefore reflect shared cellular state or coordinated activity rather than direct physical binding for every edge.

**STRING interactions (score >= 0.7)**: 3 of 45 gene pairs: COPB1–SEC24C (0.714); COPB1–USO1 (0.869); SEC24C–USO1 (0.761)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Golgi-associated vesicle (FDR = 0.007, 4 genes); COMPARTMENTS Transport vesicle (FDR = 0.0105, 4 genes); COMPARTMENTS Coated vesicle (FDR = 0.014, 4 genes); COMPARTMENTS Vesicle coat (FDR = 0.0182, 3 genes); COMPARTMENTS Golgi-associated vesicle membrane (FDR = 0.0193, 3 genes); Keyword ER-Golgi transport (FDR = 0.0363, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12394.1 (USO1, SEC24C, AP1B1; 3/98)

### Novelty

This module should not be claimed as a wholly new molecular complex. The trafficking relationships among COPB1, USO1, and SEC24C are already represented in STRING, and USO1, SEC24C, and AP1B1 co-occur in hu.MAP complex C1 (hu.MAP huMAP3_12394.1). A potentially novel aspect is the observation that this trafficking-centered program is conserved in the bone–myometrium tissue pair and is co-abundant with genes involved in proteasome regulation, protein folding, translation, and RNA surveillance. However, the fact sheet does not establish whether this exact cross-tissue module has been reported previously, and absence of the remaining relationships from STRING or hu.MAP does not prove novelty. The appropriate conclusion is that the module contains a known vesicle-trafficking core embedded in a potentially tissue-pair-specific co-abundance pattern that requires independent validation.

**Hypothesis.** Hypothesis: in both bone and myometrium, coordinated demand for secretory-pathway and membrane-protein handling links COPII export, Golgi tethering, coatomer retrieval, and adaptor-mediated sorting with cellular safeguards for protein folding, translation, and RNA quality control. In this model, SEC24C, USO1, COPB1, and AP1B1 form the trafficking axis, while HSPH1, PSMF1, COPS7A, VARS1, and UPF1 reflect the proteostasis and gene-expression conditions that support or respond to that trafficking demand. This is a mechanistic hypothesis inferred from co-abundance and annotations, not proof that all module proteins physically interact or that the same cell type generates the signal in both tissues.

### Important genes

#### SEC24C

- **Related proteins** (co-abundance neighbors): VARS1 (0.85), HSPH1 (0.85), UPF1 (0.84); STRING partners: COPB1 (0.714), USO1 (0.761)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: SEC24 homolog C, COPII component. The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec24p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The product of this gene may play a role in shaping the vesicle, as well as in cargo selection and concentration.…
- **Diseases (Open Targets)**: 22q11.2 deletion syndrome (0.370); neurodegenerative disease (0.369); Alzheimer disease (0.281); lysosomal storage disease (0.274); Parkinson disease (0.274)
- **Europe PMC papers**: 693
- **Why important**: SEC24C is the most connected member of the module and is central to the known trafficking core through its STRING relationships with COPB1 and USO1 and its membership in hu.MAP complex C1 (hu.MAP huMAP3_12394.1). Its established function in COPII coat assembly, cargo loading, and endoplasmic-reticulum-to-Golgi transport directly matches the recurring supplementary STRING terms (6 supplementary STRING terms; within-query FDR 0.007–0.0363). It also has substantial literature support and disease associations involving neurodevelopmental and neurodegenerative disorders, making it a strong mechanistic and translational anchor.
- **Conclusion**: Established evidence supports SEC24C as a central component of the module's vesicle-trafficking interpretation. It is reasonable to hypothesize that variation in SEC24C abundance helps organize the shared co-abundance pattern, but the fact sheet does not prove that SEC24C drives the module or that its disease associations explain the bone–myometrium signal.

#### COPB1

- **Related proteins** (co-abundance neighbors): USO1 (0.85), PSMF1 (0.81), AP1B1 (0.80); STRING partners: SEC24C (0.714), USO1 (0.869)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus, Vesicles, Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coat protein complex I subunit beta 1. This gene encodes a protein subunit of the coatomer complex associated with non-clathrin coated vesicles. The coatomer complex, also known as the coat protein complex 1, forms in the cytoplasm and is recruited to the Golgi by activated guanosine triphosphatases. Once at the Golgi membrane, the coatomer complex may assist in the movement of protein and lipid components back to the endoplasmic retic…
- **Diseases (Open Targets)**: Baralle-Macken syndrome (0.598); Alzheimer disease (0.463); Parkinson disease (0.462); neurodegenerative disease (0.462); lysosomal storage disease (0.462)
- **Europe PMC papers**: 565
- **Why important**: COPB1 is highly connected in the module and links the trafficking core to AP1B1 and PSMF1 in the co-abundance graph. It has known STRING relationships with SEC24C and USO1 and is repeatedly represented in the supplementary Golgi and vesicle terms (6 supplementary STRING terms; within-query FDR 0.007–0.0363). Its established coatomer role in Golgi organization, retrograde transport, and intra-Golgi trafficking makes it a strong bridge between vesicle transport and the broader module. It also has substantial literature support and disease associations involving Baralle-Macken syndrome and neurodegenerative or lysosomal disorders.
- **Conclusion**: Established evidence identifies COPB1 as a core trafficking component and a plausible network bridge. The module supports coordinated COPB1 activity with SEC24C and USO1, but it does not establish a tissue-specific COPB1 mechanism or direct coupling to PSMF1.

#### USO1

- **Related proteins** (co-abundance neighbors): COPB1 (0.85), HSPH1 (0.84); STRING partners: COPB1 (0.869), SEC24C (0.761)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: USO1 vesicle transport factor. The protein encoded by this gene is a peripheral membrane protein which recycles between the cytosol and the Golgi apparatus during interphase. It is regulated by phosphorylation: dephosphorylated protein associates with the Golgi membrane and dissociates from the membrane upon phosphorylation. Ras-associated protein 1 recruits this protein to coat protein complex II (COPII) vesicles during buddin…
- **Diseases (Open Targets)**: psoriatic arthritis (0.184); bipolar disorder (0.150); retinitis pigmentosa (0.085); cone dystrophy (0.076); cone-rod dystrophy (0.076)
- **Europe PMC papers**: 546
- **Why important**: USO1 connects the principal trafficking relationships and participates in the strongest-supported STRING links in the module, as well as hu.MAP complex C1 (hu.MAP huMAP3_12394.1). Its established role in COPII vesicle tethering, Golgi recruitment, vesicle fusion, and Golgi transport is highly concordant with (STRING COMPARTMENTS Golgi-associated vesicle; within-query FDR = 0.007), (STRING COMPARTMENTS Transport vesicle; within-query FDR = 0.0105), (STRING COMPARTMENTS Coated vesicle; within-query FDR = 0.014), and (STRING Keyword ER-Golgi transport; within-query FDR = 0.0363). HPA additionally reports tissue enhancement in skeletal muscle and cell-type enhancement in myonuclei, which may be relevant to shared contractile or muscle-associated cellular programs, although this is not specific to myometrium. Its literature and disease associations provide additional biological context.
- **Conclusion**: Established evidence supports USO1 as a central Golgi-tethering component of the conserved trafficking core. The skeletal-muscle and myonuclear HPA signals motivate a hypothesis that tissue physiology influences the module, but they do not demonstrate that USO1 explains conservation between bone and myometrium.

#### AP1B1

- **Related proteins** (co-abundance neighbors): COPB1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: adaptor related protein complex 1 subunit beta 1. Adaptor protein complex 1 is found at the cytoplasmic face of coated vesicles located at the Golgi complex, where it mediates both the recruitment of clathrin to the membrane and the recognition of sorting signals within the cytosolic tails of transmembrane receptors. This complex is a heterotetramer composed of two large, one medium, and one small adaptin subunit. The protein encoded by this gene…
- **Diseases (Open Targets)**: ichthyosiform erythroderma, corneal involvement, and hearing loss (0.715); HIV infectious disease (0.503); MEDNIK syndrome (0.371); neurodegenerative disease (0.370); KID syndrome (0.292)
- **Europe PMC papers**: 500
- **Why important**: AP1B1 is part of hu.MAP complex C1 (hu.MAP huMAP3_12394.1) and is repeatedly included in the supplementary coated-vesicle and vesicle-coat terms (5 supplementary STRING terms; within-query FDR 0.007–0.0193). Its established role as a large subunit of adaptor protein complex one connects Golgi membrane sorting, clathrin recruitment, receptor-cargo recognition, endocytosis, and basolateral secretion to the COPII and coatomer axis. HPA places it in the Golgi and reports cell-type enhancement in Hofbauer cells and microglia, while its disease associations include syndromic disorders and neurodegenerative disease. It therefore provides functional breadth beyond the COPII-centered interactions.
- **Conclusion**: Established evidence supports AP1B1 as a Golgi sorting component that complements the SEC24C–USO1–COPB1 trafficking core. Its co-abundance with the core could reflect coordinated membrane sorting, but the supplied data do not establish direct physical interaction with COPB1 or a specific cell-type source.

#### HSPH1

- **Related proteins** (co-abundance neighbors): SEC24C (0.85), USO1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family H (Hsp110) member 1. This gene encodes a member of the heat shock protein 70 family of proteins. The encoded protein functions as a nucleotide exchange factor for the molecular chaperone heat shock cognate 71 kDa protein (Hsc70). In addition, this protein plays a distinct but related role as a holdase that inhibits the aggregation of misfolded proteins, including the cystic fibrosis transmembrane conductance regulator…
- **Diseases (Open Targets)**: Parkinson disease (0.205); Phenotypic abnormality (0.187); hypertensive disorder (0.131); neoplasm (0.104); major depressive disorder (0.096)
- **Europe PMC papers**: 2050
- **Why important**: HSPH1 is connected to both SEC24C and USO1 in the module and has the largest literature volume among the listed genes. Its established function as an Hsp110-family chaperone and holdase links the trafficking core to protein folding and protection from aggregation. HPA reports low tissue specificity, low immune-cell specificity, and cell-type enhancement in several specialized cell types, without evidence that it is a secreted or blood-cell marker. Its disease associations include Parkinson disease, neoplasms, and other phenotypic abnormalities.
- **Conclusion**: Established evidence supports HSPH1 as a proteostasis component co-abundant with the trafficking core, rather than as a documented vesicle-trafficking factor. A plausible hypothesis is that HSPH1 reflects the folding burden created by membrane and secretory-pathway activity, but the co-abundance data do not establish causal coupling.

## Module 7

**Tissue pair**: bone and myometrium  
**Genes (5)**: ARPC1B, DBNL, DPP3, MYH10, NSFL1C

### Function

No GO or KEGG term passed global correction in the globally significant GO/KEGG evidence set, and STRING functional enrichment is absent. The co-abundance pattern nevertheless brings together genes associated with actin organization, membrane trafficking, intracellular proteolysis, cell shape, and non-muscle motility. DBNL connects the DPP3 and ARPC1B side of the network with the NSFL1C and MYH10 side. This supports a cautious interpretation as a cell-structure and intracellular-trafficking module rather than a formally established pathway. The interpretation is hypothesis-generating, not enrichment-confirmed.

**Cell composition.** The module contains no secreted genes, so it is not a plasma-protein module. Most genes have low tissue specificity, while all genes show some cell-type enhancement. Highlighted cell types include Hofbauer cells, megakaryocytes, platelets, esophageal epithelial cells, trophoblast-related cells, and other specialized cell types. ARPC1B is tissue-enhanced in lymphoid tissue, and MYH10 is tissue-enriched in blood vessel. Most genes have low immune-cell specificity, whereas MYH10 is not detected in immune cells. This pattern does not support a simple blood-cell explanation, but it raises the possibility that the shared signal reflects vascular, stromal, specialized-cell, or broadly distributed cellular machinery rather than a bone–myometrium-specific process. HPA protein detection is mixed in myometrium, and there is no matching HPA bone-tissue result.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, no STRING functional-enrichment result is reported, and no hu.MAP complex contains multiple module members. The co-abundance relationships therefore are not supported by the supplied databases as established physical interactions or membership in a known shared complex. They may reflect coordinated expression, indirect regulation, shared localization, or sample composition. The individual annotations remain biologically coherent: ARPC1B belongs to the Arp2/3 actin-nucleation machinery, MYH10 is a non-muscle myosin involved in actomyosin organization and cell movement, NSFL1C participates in p97-associated membrane and Golgi processes, DPP3 is a cytoplasmic metallopeptidase, and DBNL is associated with membrane organization, Rac signaling, and podosome assembly.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The tissue-pair co-abundance observation may be new because the supplied STRING and hu.MAP evidence does not represent the module as a known interaction group or complex. However, absence from STRING or hu.MAP does not prove biological novelty. The genes are individually well studied, and the pattern could reflect shared cell types, general cytoskeletal or trafficking activity, or dataset-specific covariance. A claim of a new biological module requires replication in independent bone and myometrium datasets, adjustment for cellular composition, and ideally orthogonal protein or perturbation evidence. The appropriate conclusion is that the association is potentially novel but currently unvalidated.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of cell shape, actin-dependent adhesion or motility, intracellular membrane trafficking, and protein turnover in a shared vascular, stromal, or specialized cell population present in bone and myometrium. DBNL may connect membrane and podosome-related organization with the rest of the module; ARPC1B and MYH10 may represent complementary actin-nucleation and actomyosin functions; NSFL1C may couple this state to vesicle or Golgi maintenance; and DPP3 may mark associated cytoplasmic proteolytic activity. This model should be tested against cell-type composition and validated experimentally rather than treated as an established pathway.

### Important genes

#### ARPC1B

- **Related proteins** (co-abundance neighbors): DPP3 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: actin related protein 2/3 complex subunit 1B. This gene encodes one of seven subunits of the human Arp2/3 protein complex. This subunit is a member of the SOP2 family of proteins and is most similar to the protein encoded by gene ARPC1A. The similarity between these two proteins suggests that they both may function as p41 subunit of the human Arp2/3 complex that has been implicated in the control of actin polymerization in cells. It is possib…
- **Diseases (Open Targets)**: platelet abnormalities with eosinophilia and immune-mediated inflammatory disease (0.771); combined immunodeficiency (0.429); autoimmune disorder of central nervous system (0.397); cutaneous leishmaniasis (0.370); immunodeficiency disease (0.346)
- **Europe PMC papers**: 1334
- **Why important**: ARPC1B is the clearest cytoskeletal anchor on the network edge. It is a subunit of the Arp2/3 complex and is annotated for cortical actin organization and actin nucleation. It has the largest literature volume among the module genes and has disease associations involving platelet abnormalities and immunodeficiency. Its HPA profile includes lymphoid and several specialized immune or trophoblast-associated cell types, making it informative for distinguishing actin remodeling from a nonspecific co-abundance signal.
- **Conclusion**: Established evidence supports ARPC1B as an actin-nucleation and cell-structure gene with clinically relevant immune and platelet associations. Its connection to DPP3 is a co-abundance relationship, not a demonstrated physical interaction in the supplied evidence. It is a plausible mechanistic marker of the module, but its tissue-pair role remains hypothetical.

#### MYH10

- **Related proteins** (co-abundance neighbors): NSFL1C (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin heavy chain 10. This gene encodes a member of the myosin superfamily. The protein represents a conventional non-muscle myosin; it should not be confused with the unconventional myosin-10 (MYO10). Myosins are actin-dependent motor proteins with diverse functions including regulation of cytokinesis, cell motility, and cell polarity. Mutations in this gene have been associated with May-Hegglin anomaly and developmen…
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.484); hereditary disease (0.453); congenital ptosis (0.425); Hypertelorism (0.425); Wide nose (0.425)
- **Europe PMC papers**: 3179
- **Why important**: MYH10 is the strongest indicator of non-muscle actomyosin biology. It is located at actin filaments and is annotated for cytokinesis, cell shape, actin-based movement, actomyosin organization, and regulated exocytosis. It is tissue-enriched in blood vessel and is not detected in immune cells in the HPA summary. Its extensive literature and developmental and hematologic disease associations make it valuable for evaluating vascular, stromal, or contractile interpretations.
- **Conclusion**: Established evidence supports MYH10 as a non-muscle myosin involved in cell shape, movement, and actomyosin organization. Its association with NSFL1C does not establish a direct molecular complex. A vascular or stromal contribution is plausible, supported by HPA tissue enrichment but not proven for this module.

#### DBNL

- **Related proteins** (co-abundance neighbors): DPP3 (0.89), NSFL1C (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: drebrin like. Enables cadherin binding activity. Predicted to be involved in several processes, including Rac protein signal transduction; nervous system development; and podosome assembly. Located in cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: glycogen storage disease due to phosphoglycerate mutase deficiency (0.554); rhabdomyolysis (0.259); hereditary disease (0.192); Abnormality of the skeletal system (0.126); neoplasm (0.080)
- **Europe PMC papers**: 541
- **Why important**: DBNL occupies a bridging position in the network and connects DPP3 with NSFL1C. Its annotations include cadherin binding, membrane organization, Rac signaling, endocytosis, and podosome assembly, providing a plausible link between adhesion, membrane remodeling, and trafficking. Its HPA profile is broadly distributed with enhancement in epithelial and specialized cell types, and it has substantial literature and disease associations involving skeletal abnormalities and other conditions.
- **Conclusion**: Established evidence supports DBNL as a membrane and actin-associated organizer with roles in endocytosis, Rac signaling, and podosome biology. Its bridge position makes it important for interpreting the module architecture, but the supplied data do not demonstrate that DBNL physically coordinates the other module members. Its proposed role as an integrator is therefore hypothesis-level.

#### NSFL1C

- **Related proteins** (co-abundance neighbors): DBNL (0.89), MYH10 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NSFL1 cofactor. N-ethylmaleimide-sensitive factor (NSF) and valosin-containing protein (p97) are two ATPases known to be involved in transport vesicle/target membrane fusion and fusions between membrane compartments. A trimer of the protein encoded by this gene binds a hexamer of cytosolic p97 and is required for p97-mediated regrowth of Golgi cisternae from mitotic Golgi fragments. Alternative splicing results i…
- **Diseases (Open Targets)**: neurodegenerative disease (0.326); placenta praevia (0.045); adult T-cell leukemia/lymphoma (0.035); pneumonitis (0.027); hypertensive disorder (0.026)
- **Europe PMC papers**: 308
- **Why important**: NSFL1C links DBNL with MYH10 and provides the principal trafficking and organelle-maintenance interpretation. It is associated with p97-dependent Golgi regrowth and with ubiquitin-dependent protein catabolism, centrosome organization, and mitotic spindle orientation. It is detected in myometrium by immunohistochemistry and has cell-type enhancement in epithelial and oocyte-related populations. Its disease literature includes neurodegenerative and placental associations.
- **Conclusion**: Established evidence supports NSFL1C as a cofactor in p97-linked membrane and Golgi biology with additional roles in cell division and protein turnover. Its connection to MYH10 may reflect coordinated cytoskeletal and trafficking activity, but no direct interaction is reported in STRING or hu.MAP. Its contribution to a shared bone–myometrium program remains a testable hypothesis.

#### DPP3

- **Related proteins** (co-abundance neighbors): DBNL (0.89), ARPC1B (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dipeptidyl peptidase 3. This gene encodes a protein that is a member of the M49 family of metallopeptidases. This cytoplasmic protein binds a single zinc ion with its zinc-binding motif (HELLGH) and has post-proline dipeptidyl aminopeptidase activity, cleaving Xaa-Pro dipeptides from the N-termini of proteins. Increased activity of this protein is associated with endometrial and ovarian cancers. Alternatively spliced tra…
- **Diseases (Open Targets)**: Bardet-Biedl syndrome (0.259); major salivary gland cancer (0.152); neoplasm (0.103); breast carcinoma (0.102); breast cancer (0.100)
- **Europe PMC papers**: 634
- **Why important**: DPP3 is connected to DBNL and ARPC1B and supplies a distinct enzymatic function within an otherwise structural and trafficking-oriented module. It is a cytoplasmic zinc metallopeptidase that cleaves amino-terminal dipeptides, is annotated for proteolysis, is detected in myometrium, and has disease and cancer associations. Its inclusion may indicate linked protein-turnover activity or may reflect a shared cellular state rather than pathway membership.
- **Conclusion**: Established evidence supports DPP3 as a cytoplasmic metallopeptidase and not as a known component of the Arp2/3 or myosin systems. Its network connections are co-abundance links without supplied physical-interaction support. A role in coordinated proteostasis within the proposed module is plausible, but whether it is mechanistically connected to the cytoskeletal genes is unresolved.

## Module 8

**Tissue pair**: bone and myometrium  
**Genes (5)**: BOLA2, S100A11, S100A16, SH3BGRL3, TXN

### Function

The module is most consistent with a calcium-responsive, redox-linked intracellular cell-state program rather than a firmly established bone- or myometrium-specific pathway. S100A11 and S100A16 form the only STRING-supported relationship and are jointly represented in the supplementary calcium-binding annotation (STRING SMART S-100/ICaBP type calcium binding domain; within-query FDR = 0.0389). TXN contributes redox homeostasis, cellular detoxification, and nitric-oxide-related regulation, while SH3BGRL3 is annotated in cytoskeleton organization. S100A11 is also annotated in cell-cell adhesion, cell-population regulation, and smooth-muscle-cell migration. These annotations support a possible connection among calcium signaling, redox control, cytoskeletal state, adhesion, and cellular remodeling. However, no GO/KEGG term passed global correction, so no GO/KEGG pathway can be claimed as significantly enriched for this module.

**Cell composition.** The module does not appear to be dominated by plasma or secreted proteins, and its HPA profile does not indicate a strong blood-cell signature. Most genes show tissue or cell-type enrichment associated with esophageal epithelial populations, especially apical and suprabasal cells, while blood-cell specificity is generally low. One gene is classified as secreted in the module-level HPA summary, but the individual evidence also includes intracellular localization. The strong epithelial signal, together with low immune specificity, suggests that the shared bone–myometrium module may reflect a broadly shared epithelial-like, stress-related, or cellular-state component rather than a specialized tissue function. HPA protein evidence is absent for bone and shows mixed detection in myometrium, so the tissue-level interpretation remains uncertain.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship is the S100A11–S100A16 pair. This supports a known association between the two S100 proteins, but it does not establish that every module edge represents a physical interaction. The supplementary STRING calcium-binding annotation (STRING SMART S-100/ICaBP type calcium binding domain; within-query FDR = 0.0389) is supportive rather than globally significant. Both S100A11 and S100A16 occur together in hu.MAP complexes (hu.MAP huMAP3_09125.1) and (hu.MAP huMAP3_09929.1), providing independent complex-level support for their relationship. The hu.MAP complexes are much broader than this module and contain many epithelial, junctional, protease, barrier, and inflammatory proteins; therefore, the module captures only a small portion of those complexes. TXN and SH3BGRL3 have no listed hu.MAP or STRING partners in the supplied evidence. The remaining co-abundance relationships should therefore be interpreted as network associations, not established biochemical interactions.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: S100A11–S100A16 (0.738)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART S-100/ICaBP type calcium binding domain (FDR = 0.0389, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09125.1 (S100A11, S100A16; 2/53); huMAP3_09929.1 (S100A11, S100A16; 2/75)

### Novelty

The molecular components and the S100A11–S100A16 relationship are not new: they are supported by STRING, hu.MAP, established gene annotations, and substantial literature. The potentially new aspect is the coordinated co-abundance of this particular gene set across bone and myometrium. The fact sheet does not provide an independent cohort, perturbation experiment, replication analysis, or comparison with previously published cross-tissue modules, so it cannot establish that the module is a new biological discovery. Absence of additional STRING or hu.MAP relationships is not evidence of novelty. The most defensible conclusion is that this may be a new tissue-pair co-abundance observation built partly from previously known molecular relationships, requiring external validation.

**Hypothesis.** Hypothesis: the shared bone–myometrium module reflects a conserved intracellular remodeling state in which calcium-responsive S100 proteins coordinate with thioredoxin-dependent redox control and cytoskeletal or adhesion processes. In this model, S100A11 and S100A16 form the core calcium-linked component, TXN buffers redox stress and modulates signaling competence, and SH3BGRL3 connects the state to cytoskeletal organization. The epithelial enrichment may indicate shared epithelial-like or barrier-associated cellular programs in the sampled material, or may reflect cellular admixture, rather than a direct bone–myometrium mechanism. This hypothesis should be tested with cell-resolved data, independent tissue cohorts, and perturbation of the S100 or thioredoxin components.

### Important genes

#### S100A11

- **Related proteins** (co-abundance neighbors): S100A16 (0.85), BOLA2; BOLA2B (0.82), TXN (0.82); STRING partners: S100A16 (0.738)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: S100 calcium binding protein A11. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: skin disorder (0.169); atopic eczema (0.127); skin cancer (0.122); neoplasm (0.115); hepatocellular carcinoma (0.111)
- **Europe PMC papers**: 2722
- **Why important**: S100A11 is a highly connected module member and is directly linked to S100A16 in STRING and both hu.MAP complexes (STRING SMART S-100/ICaBP type calcium binding domain; within-query FDR = 0.0389) (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1). Its annotations include calcium-binding, cell-cell adhesion, regulation of cell proliferation, and positive regulation of smooth-muscle-cell migration. It has the largest literature footprint among the module genes and disease associations spanning skin disorders, atopic eczema, skin cancer, and neoplasia. Its enrichment in esophageal epithelial populations and neutrophils also makes it relevant to interpreting the module's cellular origin.
- **Conclusion**: Established evidence supports S100A11 as a central calcium-associated and remodeling-related component with a known relationship to S100A16. Its role as the driver of the bone–myometrium co-abundance pattern remains a hypothesis, because the module lacks globally significant GO/KEGG enrichment and the HPA profile points toward epithelial rather than tissue-specific biology.

#### S100A16

- **Related proteins** (co-abundance neighbors): BOLA2; BOLA2B (0.86), S100A11 (0.85), TXN (0.81); STRING partners: S100A11 (0.738)
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: S100 calcium binding protein A16. Enables calcium ion binding activity and protein homodimerization activity. Predicted to act upstream of or within response to calcium ion. Located in several cellular components, including cytosol; extracellular space; and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.490); neoplasm (0.107); lung adenocarcinoma (0.104); breast cancer (0.103); breast carcinoma (0.101)
- **Europe PMC papers**: 2006
- **Why important**: S100A16 has a highly connected position in the module and is the other member of the only STRING-supported pair. It is present with S100A11 in both hu.MAP complexes (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1) and contributes to the supplementary calcium-binding signal (STRING SMART S-100/ICaBP type calcium binding domain; within-query FDR = 0.0389). Its curated annotations support calcium-ion binding, homodimerization, and a possible role upstream of calcium responses. It also has a substantial literature base and disease associations including neurodegenerative disease and neoplasia.
- **Conclusion**: Established evidence supports S100A16 as a core calcium-binding partner of S100A11. It is a plausible marker of the module's calcium-responsive state, but a direct role in bone–myometrium biology is not established by the supplied data and should remain hypothetical.

#### TXN

- **Related proteins** (co-abundance neighbors): SH3BGRL3 (0.86), S100A11 (0.82), S100A16 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin. The protein encoded by this gene acts as a homodimer and is involved in many redox reactions. The encoded protein is active in the reversible S-nitrosylation of cysteines in certain proteins, which is part of the response to intracellular nitric oxide. This protein is found in the cytoplasm. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct…
- **Diseases (Open Targets)**: neurodegenerative disease (0.530); smoking initiation (0.288); ovarian neoplasm (0.171); cancer (0.122); neoplasm (0.114)
- **Europe PMC papers**: 4080
- **Why important**: TXN is highly connected to S100A11, S100A16, and SH3BGRL3 in the co-abundance network. Its established function in reversible cysteine redox reactions, redox homeostasis, hydrogen-peroxide detoxification, nitric-oxide-related regulation, and phosphatidylinositol-three-kinase/protein-kinase-B signaling provides a mechanistic complement to the calcium-associated S100 pair. It is detected in myometrium by HPA and has the largest literature footprint among the listed genes, with disease associations including neurodegenerative disease, ovarian neoplasm, and cancer.
- **Conclusion**: Established evidence supports TXN as a plausible redox and signaling component of the module. Its connection to the S100-centered state is supported by co-abundance, not by a listed STRING or hu.MAP relationship; therefore, its proposed role as a mediator of calcium–redox coupling is a hypothesis.

#### SH3BGRL3

- **Related proteins** (co-abundance neighbors): TXN (0.86), BOLA2; BOLA2B (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SH3 domain binding glutamate rich protein like 3. Located in nuclear body. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.108); neoplasm (0.083); gastric cancer (0.079); acute myeloid leukemia (0.078); uncombable hair syndrome (0.076)
- **Europe PMC papers**: 482
- **Why important**: SH3BGRL3 links TXN with BOLA2 or BOLA2B in the module network and is annotated in cytoskeleton organization. It shows cell-type enrichment in several epithelial populations and is detected in myometrium by HPA. Although its literature volume and functional annotation are more limited than those of the S100 genes or TXN, its network position makes it a potentially informative connector between redox-associated and structural cellular programs. Its disease associations include type two diabetes mellitus, gastric cancer, acute myeloid leukemia, and uncombable hair syndrome.
- **Conclusion**: Established evidence supports SH3BGRL3 as a co-abundant structural or cytoskeletal-associated connector, but its molecular function in this module is comparatively uncertain. A role in transmitting the S100–TXN state into cytoskeletal remodeling is a hypothesis requiring experimental testing.

## Module 9

**Tissue pair**: bone and myometrium  
**Genes (6)**: CLIC4, LHPP, NIT2, PFDN4, TRIP6, TTLL12

### Function

No GO or KEGG term passed global correction, and STRING reported no supplementary enrichment. The module therefore does not support a formally established pathway-level function from enrichment analysis. Its gene-level evidence is compatible with a mixed cellular program involving protein folding and proteostasis through PFDN4, intracellular amino-acid and central-carbon metabolism through NIT2, phosphate-containing compound metabolism through LHPP, focal-adhesion and cell-migration signaling through TRIP6, cytoskeletal and polarity regulation through CLIC4, and chromatin, cell-cycle, and interferon-response regulation through TTLL12. The co-abundance structure may consequently represent coordinated abundance of broadly related cellular functions rather than a single canonical pathway.

**Cell composition.** The module is not dominated by secreted or plasma proteins, because none of the genes is annotated as secreted. Most genes have low immune-cell specificity, so the module does not strongly resemble a blood-cell program overall. CLIC4 is an exception, with immune-cell enhancement in memory and naive B cells, and it is also enhanced in vascular, stromal, mesothelial, trophoblast, and plasma-cell populations. The genes show heterogeneous tissue and cell-type patterns, including liver, brain, blood vessel, esophagus, gastric progenitor, esophageal, stromal, trophoblast, and reproductive-cell annotations. Four genes are detected by myometrium immunohistochemistry and two are not detected there. This heterogeneity argues against a simple plasma-protein or uniform housekeeping explanation, while leaving open the possibility that shared stromal, vascular, epithelial, or other cell-composition features contribute to the bone–myometrium co-abundance signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no hu.MAP complex contained multiple module members. Thus, the observed co-abundance edges are not supported here as already established physical interactions or membership in a known multiprotein complex. The absence of STRING and hu.MAP support does not invalidate the co-abundance module: co-regulation, shared cell composition, common stress responses, indirect signaling, or context-dependent interactions can produce correlated abundance without curated physical links. It does mean that a direct molecular network interpretation should remain cautious.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is potentially novel as a tissue-pair co-abundance pattern because its internal relationships lack supporting STRING interactions and shared hu.MAP complexes, and because no globally corrected GO or KEGG term defines it as a known pathway. However, novelty cannot be established from database absence alone. The individual genes and several of their functions are established, and the module could reflect an unrecognized combination of known cellular programs, tissue composition, or technical and biological covariance. The appropriate conclusion is that the shared bone–myometrium co-abundance pattern is a hypothesis-generating finding requiring replication and orthogonal validation, rather than a proven new molecular complex or pathway.

**Hypothesis.** Hypothesis: the module captures a shared stromal, vascular, or contractile-tissue state in bone and myometrium in which focal-adhesion and cytoskeletal remodeling, intracellular metabolic support, proteostasis, and chromatin or cell-cycle regulation are co-varying. TRIP6 and CLIC4 could link adhesion, membrane-associated signaling, polarity, and cytoskeletal behavior; NIT2 and LHPP could reflect metabolic and phosphate-processing state; PFDN4 could support proteostasis; and TTLL12 could couple the state to chromatin, mitotic, and interferon-response regulation. This is a mechanistic model, not an established pathway assignment, and it should be tested by cell-type-resolved expression, protein measurements, and perturbation of adhesion or metabolic regulators.

### Important genes

#### PFDN4

- **Related proteins** (co-abundance neighbors): LHPP (0.90), CLIC4 (0.88), NIT2 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prefoldin subunit 4. This gene encodes a member of the prefoldin beta subunit family. The encoded protein is one of six subunits of prefoldin, a molecular chaperone complex that binds and stabilizes newly synthesized polypeptides, thereby allowing them to fold correctly. The complex, consisting of two alpha and four beta subunits, forms a double beta barrel assembly with six protruding coiled-coils. [provided by RefSe…
- **Diseases (Open Targets)**: neurodegenerative disease (0.451); colorectal cancer (0.341); cervical carcinoma (0.291); atopic eczema (0.193); liver disorder (0.126)
- **Europe PMC papers**: 256
- **Why important**: PFDN4 is among the most connected genes in the module and links LHPP, CLIC4, and NIT2. Its established prefoldin function provides a plausible proteostasis component, and its protein-folding annotation is more coherent with a cellular-state interpretation than with a secreted or blood-derived explanation. It has substantial literature and disease-association coverage, although those associations do not establish a role in this tissue-pair module.
- **Conclusion**: Established evidence supports PFDN4 as a network-central prefoldin subunit involved in protein folding. It is a credible marker of a coordinated intracellular state. A direct role for PFDN4 in the shared bone–myometrium biology remains a hypothesis because there is no enrichment, STRING, or hu.MAP support for this particular module.

#### NIT2

- **Related proteins** (co-abundance neighbors): TRIP6 (0.87), PFDN4 (0.87), LHPP (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nitrilase family member 2. Enables omega-amidase activity. Involved in asparagine metabolic process; glutamine metabolic process; and oxaloacetate metabolic process. Located in centrosome and cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: synovium disorder (0.187); neoplasm (0.079); lung adenocarcinoma (0.074); poisoning (0.037); glaucoma (0.028)
- **Europe PMC papers**: 977
- **Why important**: NIT2 is among the most connected genes and bridges TRIP6, PFDN4, and LHPP. Its annotated omega-amidase activity and links to asparagine, glutamine, oxaloacetate, and related metabolic processes make it a strong candidate for the metabolic component of the module. It is tissue-enhanced in liver and detected in myometrium, while its literature and disease-association record is substantial.
- **Conclusion**: Established evidence supports NIT2 as a cytosolic metabolic enzyme with a central position in this co-abundance structure. It may report metabolic state in shared cells, but the claim that it mechanistically drives the bone–myometrium module is unproven and requires perturbation or flux-based evidence.

#### TRIP6

- **Related proteins** (co-abundance neighbors): TTLL12 (0.88), NIT2 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thyroid hormone receptor interactor 6. This gene is a member of the zyxin family and encodes a protein with three LIM zinc-binding domains. This protein localizes to focal adhesion sites and along actin stress fibers. Recruitment of this protein to the plasma membrane occurs in a lysophosphatidic acid (LPA)-dependent manner and it regulates LPA-induced cell migration. Alternatively spliced variants which encode different protein isofor…
- **Diseases (Open Targets)**: neurodegenerative disease (0.253); hair color (0.224); colorectal carcinoma (0.096); breast cancer (0.089); breast carcinoma (0.089)
- **Europe PMC papers**: 697
- **Why important**: TRIP6 connects NIT2 with TTLL12 and is detected in myometrium. Its focal-adhesion localization, zyxin-family membership, and established roles in cell migration, focal-adhesion assembly, signal transduction, and non-canonical NF-kappa B regulation make it the clearest candidate for linking the module to tissue architecture and remodeling. Its literature and disease-association coverage are substantial.
- **Conclusion**: Established evidence supports TRIP6 as an adhesion- and cytoskeleton-associated signaling protein relevant to cellular movement. Its position suggests a possible architectural bridge within the module, but no direct interaction with the other module genes is established by the supplied STRING or hu.MAP evidence.

#### CLIC4

- **Related proteins** (co-abundance neighbors): PFDN4 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Centrosome; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CLIC family member 4. Chloride channels are a diverse group of proteins that regulate fundamental cellular processes including stabilization of cell membrane potential, transepithelial transport, maintenance of intracellular pH, and regulation of cell volume. Chloride intracellular channel 4 (CLIC4) protein, encoded by the CLIC4 gene, is a member of the p64 family; the gene is expressed in many tissues and exhibits a i…
- **Diseases (Open Targets)**: hypertensive disorder (0.352); Short stature (0.259); cardiovascular disorder (0.237); response to xenobiotic stimulus (0.233); exostosis (0.212)
- **Europe PMC papers**: 4070
- **Why important**: CLIC4 connects to the network hub PFDN4 and has the strongest literature presence among the module genes. It is detected in myometrium, enhanced in blood-vessel and several stromal or mesothelial populations, and has annotations involving cell differentiation, migration, polarity, and cytoskeleton organization. Its immune-cell enhancement is important context because it creates a plausible, though not dominant, cell-composition alternative.
- **Conclusion**: Established evidence supports CLIC4 as an intracellular chloride-channel-family protein associated with membrane, centrosomal, polarity, differentiation, and cytoskeletal processes. It is a useful candidate for connecting tissue remodeling with cell composition. Its contribution to the shared module could reflect stromal or vascular biology, immune admixture, or both; the supplied data cannot distinguish these possibilities.

#### LHPP

- **Related proteins** (co-abundance neighbors): PFDN4 (0.90), NIT2 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles, Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phospholysine phosphohistidine inorganic pyrophosphate phosphatase. Enables inorganic diphosphatase activity and protein homodimerization activity. Involved in phosphate-containing compound metabolic process. Located in cytosol and nuclear speck. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: open-angle glaucoma (0.473); Abnormality of the skeletal system (0.376); spina bifida (0.349); cervical carcinoma (0.321); liver disorder (0.315)
- **Europe PMC papers**: 987
- **Why important**: LHPP is among the most connected genes and links PFDN4 with NIT2. Its phosphatase activity and phosphate-containing compound annotation provide a biochemical complement to the metabolic role of NIT2. It is tissue-enriched in brain, detected in myometrium, and has substantial literature and disease-association coverage, including skeletal-system associations.
- **Conclusion**: Established evidence supports LHPP as a cytosolic and nuclear-speck phosphatase involved in phosphate-containing compound metabolism. Its network position and skeletal-system disease associations make it relevant to the bone side of the comparison, but a specific role in the shared bone–myometrium mechanism remains hypothetical without functional validation.

## Module 10

**Tissue pair**: bone and myometrium  
**Genes (5)**: CRYAB, GSTT1, RAB21, RRAS, SEC22B

### Function

The module is most consistent with a weakly connected cellular-trafficking and stress-response program. RAB21 is the central network gene and connects vesicle-associated or signaling genes, including SEC22B and RRAS, while SEC22B is annotated for ER–Golgi vesicle transport and vesicle fusion. RRAS contributes small-GTPase signaling, cell polarity, adhesion, vascular regulation, and angiogenesis. GSTT1 contributes glutathione-dependent detoxification, and CRYAB contributes small-heat-shock-protein chaperone activity, protein folding, and muscle-related functions. These annotations support a possible convergence of membrane traffic, adhesion or signaling, and cellular stress handling, but they do not establish one specific pathway. No GO or KEGG term passed global correction. The absence of a globally significant term does not invalidate the co-abundance module.

**Cell composition.** The module does not appear to be predominantly composed of plasma proteins or classical secreted proteins based on the available gene-level annotations. The HPA summary does report a secreted gene, but the listed annotations identify the other characterized proteins as intracellular, membrane-associated, vesicular, or lacking secretome annotation. The composition is heterogeneous rather than a clear housekeeping set: CRYAB is enriched in muscle-related tissues, RRAS in blood vessel tissue, and several genes show cell-type enhancement in neutrophils, myoepithelial cells, or other specialized cell populations. RAB21 and SEC22B have neutrophil-associated HPA signals, while RRAS has group enrichment in intermediate and non-classical monocytes. Most characterized genes have low immune-cell specificity or are not detected in immune cells, so blood contamination is not established, but shared immune, vascular, stromal, or smooth-muscle cell composition remains a plausible contributor. Protein detection in myometrium is mixed, with some genes detected and others not detected or lacking data.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was present among the module genes, and no STRING functional-enrichment result was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not supported by the supplied high-confidence physical-interaction or curated-complex evidence. The network may represent coordinated expression across cellular states, tissue composition, or indirect biology rather than a stable physical complex. The strongest co-abundance relationships are centered on RAB21, linking it with GSTT1, SEC22B, and RRAS, while CRYAB is connected to GSTT1. These associations are useful for generating hypotheses but should not be described as experimentally established protein interactions.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel cross-tissue co-abundance observation, because the supplied module is not represented by a matching high-confidence STRING interaction set or a shared hu.MAP complex. However, that absence does not prove novelty: the individual genes and their functions are established, and the module could reflect indirect regulation, cell-type composition, or a context-specific transcriptional program. The limited functional coherence, lack of a globally significant GO or KEGG term, and absence of supporting STRING or hu.MAP structure make the claim of a new biological mechanism preliminary. Its strongest novelty is therefore the observed association across bone and myometrium, not discovery of previously unknown functions for these genes.

**Hypothesis.** Hypothesis: in a shared cellular population or shared physiological state of bone and myometrium, RAB21-mediated membrane trafficking may coordinate with SEC22B-dependent ER–Golgi transport and RRAS signaling to influence adhesion, polarity, migration, or vascular interactions. GSTT1 could provide protection from electrophilic or oxidative stress, while CRYAB could stabilize proteins and cytoskeletal or muscle-associated structures during mechanical or cellular stress. The co-abundance pattern may therefore reflect a coordinated trafficking–signaling–stress adaptation program, possibly contributed by vascular, smooth-muscle, stromal, or selected immune-associated cells. This hypothesis requires validation with independent cohorts, cell-resolved data, and perturbation or protein-level experiments.

### Important genes

#### RAB21

- **Related proteins** (co-abundance neighbors): GSTT1 (0.90), SEC22B (0.85), RRAS (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB21, member RAS oncogene family. This gene belongs to the Rab family of monomeric GTPases, which are involved in the control of cellular membrane traffic. The encoded protein plays a role in the targeted trafficking of integrins via its association with integrin alpha tails. As a consequence, the encoded protein is involved in the regulation of cell adhesion and migration. Expression of this gene is associated with a poor prognos…
- **Diseases (Open Targets)**: neurodegenerative disease (0.469); small intestine neuroendocrine neoplasm (0.095); neoplasm (0.085); posterior cortical atrophy (0.074); nonpapillary renal cell carcinoma (0.065)
- **Europe PMC papers**: 999
- **Why important**: RAB21 has the strongest network position and connects three other module genes, making it the main topological candidate. Its established role as a Rab-family GTPase in intracellular membrane traffic, integrin trafficking, cell adhesion, migration, exocytosis, and receptor-mediated endocytosis provides the clearest bridge between the module structure and a trafficking or adhesion-related interpretation. It also has substantial literature and reported associations with glioma prognosis and several disease areas.
- **Conclusion**: Established evidence supports RAB21 as the module's central trafficking and adhesion-related candidate. It is reasonable to hypothesize that RAB21 helps organize the observed co-abundance pattern, but the module does not demonstrate that RAB21 regulates the other genes.

#### SEC22B

- **Related proteins** (co-abundance neighbors): RAB21 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC22 homolog B, vesicle trafficking protein. The protein encoded by this gene is a member of the SEC22 family of vesicle trafficking proteins. It seems to complex with SNARE and it is thought to play a role in the ER-Golgi protein trafficking. This protein has strong similarity to Mus musculus and Cricetulus griseus proteins.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: inflammatory bowel disease (0.285); luminal A breast carcinoma (0.271); colitis (0.238); enteritis (0.238); Crohn disease (0.233)
- **Europe PMC papers**: 1006
- **Why important**: SEC22B is directly connected to RAB21 in the module and has a defined role in ER–Golgi vesicle transport, retrograde transport, vesicle fusion, and vesicle-mediated processes. Its function supplies a mechanistic component for the trafficking interpretation, even though it has no matching STRING partner or hu.MAP complex with another module member. It also has disease associations involving inflammatory bowel and intestinal disorders and a substantial literature.
- **Conclusion**: Established evidence supports SEC22B as a vesicle-trafficking component. Its participation in a bone–myometrium program is a hypothesis derived from co-abundance, not an established tissue-specific mechanism.

#### RRAS

- **Related proteins** (co-abundance neighbors): RAB21 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAS related. The protein encoded by this gene is a small GTPase involved in diverse processes including angiogenesis, vascular homeostasis and regeneration, cell adhesion, and neuronal axon guidance. Mutations in this gene are found in many invasive cancers. [provided by RefSeq, Jul 2015].
- **Diseases (Open Targets)**: Noonan syndrome (0.424); Noonan syndrome and Noonan-related syndrome (0.370); hypertensive disorder (0.324); neurodegenerative disease (0.288); hereditary disease (0.266)
- **Europe PMC papers**: 1607
- **Why important**: RRAS is connected to RAB21 and adds a signaling dimension to the module. Its established functions include Ras signaling, cell polarity, adhesion, endothelial migration, angiogenesis, vascular homeostasis, and regeneration. HPA evidence links it to blood vessel tissue, several stromal or epithelial cell types, and selected monocyte populations; it is also detected in myometrium. Its disease associations include Noonan syndrome, hypertension-related disease, and neurodegenerative disease.
- **Conclusion**: Established evidence supports RRAS as a plausible vascular, adhesion, and polarity-related contributor. The module may involve vascular or stromal biology, but the HPA pattern does not establish which cell type drives the co-abundance signal.

#### CRYAB

- **Related proteins** (co-abundance neighbors): GSTT1 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: crystallin alpha B. Mammalian lens crystallins are divided into alpha, beta, and gamma families. Alpha crystallins are composed of two gene products: alpha-A and alpha-B, for acidic and basic, respectively. Alpha crystallins can be induced by heat shock and are members of the small heat shock protein (HSP20) family. They act as molecular chaperones although they do not renature proteins and release them in the fashio…
- **Diseases (Open Targets)**: fatal infantile hypertonic myofibrillar myopathy (0.765); myofibrillar myopathy 2 (0.750); dilated cardiomyopathy 1II (0.717); cataract 16 multiple types (0.624); early-onset posterior polar cataract (0.622)
- **Europe PMC papers**: 4517
- **Why important**: CRYAB is the module's muscle- and stress-associated candidate. It is annotated as a small heat-shock-protein chaperone involved in protein folding, stress response, muscle contraction, and regulation of protein-complex assembly. HPA shows tissue enhancement in heart muscle, skeletal muscle, and tongue, with cell-type enhancement in several epithelial or myoepithelial populations and no detection in immune cells. It has substantial literature and disease associations involving myofibrillar myopathy, cardiomyopathy, and cataract.
- **Conclusion**: Established evidence supports CRYAB as a structural and proteostatic stress-response marker, especially relevant to muscle-like or mechanically stressed cells. Its link to the rest of the module is indirect and may reflect cell state or tissue composition rather than a shared physical complex.

#### GSTT1

- **Related proteins** (co-abundance neighbors): RAB21 (0.90), CRYAB (0.86); STRING partners: none
- **HPA**: no annotation
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutathione S-transferase theta 1. The protein encoded by this gene, glutathione S-transferase (GST) theta 1 (GSTT1), is a member of a superfamily of proteins that catalyze the conjugation of reduced glutathione to a variety of electrophilic and hydrophobic compounds. Human GSTs can be divided into five main classes: alpha, mu, pi, theta, and zeta. The theta class includes GSTT1, GSTT2, and GSTT2B. GSTT1 and GSTT2/GSTT2B share 55% …
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 6010
- **Why important**: GSTT1 links RAB21 with CRYAB in the co-abundance graph and provides the module's clearest detoxification component. It encodes a glutathione S-transferase involved in conjugation of electrophilic and hydrophobic compounds and in cellular oxidant detoxification. It has the largest literature volume among the module genes listed in the fact sheet, although no Open Targets association is available. Its HPA entry lacks annotation, so tissue and cell-source interpretation is especially uncertain.
- **Conclusion**: Established evidence supports GSTT1 as an oxidative or electrophile-detoxification gene. Its placement between a trafficking gene and a stress-chaperone gene suggests a possible stress-adaptation axis, but that connection is a hypothesis and could also arise from shared sample composition.

## Module 11

**Tissue pair**: bone and myometrium  
**Genes (8)**: DDX6, EIF3L, HDGF, ME2, PSMC2, TCEA1, TRNT1, UBQLN2

### Function

The module does not support a single statistically established biological function: no GO or KEGG term passed global correction, and STRING functional enrichment was absent. Its genes nevertheless suggest coordinated regulation of core intracellular maintenance processes. DDX6 represents P-body function, mRNA decapping, deadenylation-dependent decay, translation suppression, and microRNA-mediated silencing. TRNT1 supports cytosolic and mitochondrial tRNA maturation and tRNA surveillance, while EIF3L supports translation initiation. PSMC2 and UBQLN2 implicate proteasome-linked protein quality control, ubiquitin-dependent degradation, autophagy, and ER-associated degradation. TCEA1 represents transcription elongation, HDGF represents transcriptional regulation and growth-associated activity, and ME2 represents mitochondrial malate metabolism. The network therefore looks more like a sparse co-abundance pattern linking RNA handling, translation, protein turnover, transcription, and mitochondrial metabolism than a demonstrated pathway module.

**Cell composition.** The HPA profile argues against a module dominated by plasma proteins, secreted proteins, or blood-cell contamination. HDGF is annotated as secreted to blood, but the remaining genes are not secreted, and all genes have low immune-cell specificity. Most genes have low tissue specificity, with ME2 showing tissue enhancement in choroid plexus. Cell-type-enhanced annotations occur for HDGF, ME2, and PSMC2 across distinct cell types, including erythrocyte progenitors, megakaryocytes, choroid plexus epithelial cells, Kupffer cells, gastric progenitor cells, rod photoreceptors, thymic myoid cells, and syncytiotrophoblasts. This scattered pattern does not indicate a coherent blood-cell signature. Protein detection in myometrium is present for most genes, whereas EIF3L is not detected there; bone has no matching HPA tissue data. The shared signal could therefore reflect broadly expressed intracellular programs or shared cellular state rather than a tissue-specific bone–myometrium mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction among the module gene pairs met the supplied high-confidence criterion, and STRING provided no functional enrichment. Thus, the co-abundance relationships are not corroborated here as established physical or functional STRING interactions. hu.MAP provides a limited connection through complex C1: TCEA1 and HDGF occur together in the same reported complex, while the other listed complex members are outside the module. This supports a known relationship between TCEA1 and HDGF, but does not establish that the entire module is a single protein complex. The remaining co-abundance links are not supported by the supplied STRING or hu.MAP evidence.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14982.1 (TCEA1, HDGF; 2/28)

### Novelty

This is best described as a candidate shared co-abundance association rather than a proven new biological module. The absence of STRING interactions and the limited hu.MAP overlap make the observed network less obviously recoverable from established interaction or complex resources, but database absence does not demonstrate novelty. The lack of globally significant GO or KEGG enrichment also prevents assigning a previously recognized pathway identity. A novelty claim would require independent replication in additional bone and myometrium datasets, preservation of the gene-level correlations, and tests against technical, cellular-composition, and clinical covariates. The strongest defensible conclusion is that the tissue-pair co-abundance pattern may be under-characterized, while its biological novelty remains unproven.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular stress or remodeling state in bone and myometrium that couples RNA turnover and translation control with protein quality control, mitochondrial RNA or metabolic activity, and transcriptional regulation. DDX6 could coordinate mRNA repression and decay; TRNT1 and ME2 could report mitochondrial or metabolic support; PSMC2 and UBQLN2 could maintain proteome quality; and the HDGF–TCEA1 relationship could connect this state to transcriptional and growth-associated programs. This is a mechanistic hypothesis, not an established pathway interpretation. It should be tested by replication, cell-type deconvolution, perturbation of hub genes, and measurement of RNA decay, translation, proteasome activity, mitochondrial function, and growth-related transcription.

### Important genes

#### DDX6

- **Related proteins** (co-abundance neighbors): ME2 (0.84), TRNT1 (0.84), UBQLN2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytoplasmic bodies; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 6. This gene encodes a member of the DEAD box protein family. The protein is an RNA helicase found in P-bodies and stress granules, and functions in translation suppression and mRNA degradation. It is required for microRNA-induced gene silencing. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: intellectual developmental disorder with impaired language and dysmorphic facies (0.650); Intellectual disability (0.555); neurodegenerative disease (0.459); lung carcinoma (0.371); Global developmental delay (0.371)
- **Europe PMC papers**: 3002
- **Why important**: DDX6 has the strongest network connectivity in the module and links ME2, TRNT1, and UBQLN2. Its established P-body, mRNA decay, translation-suppression, and microRNA-silencing functions provide the clearest mechanistic entry point into the RNA-regulatory aspect of the module. It also has substantial literature representation and disease associations involving intellectual disability, developmental delay, neurodegeneration, and cancer.
- **Conclusion**: Established evidence supports DDX6 as a central RNA-quality and translation-regulatory component. It is a plausible module hub, but the supplied data do not establish that DDX6 drives the bone–myometrium association or directly regulates the other module genes.

#### ME2

- **Related proteins** (co-abundance neighbors): HDGF (0.85), DDX6 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: malic enzyme 2. This gene encodes a mitochondrial NAD-dependent malic enzyme, a homotetrameric protein, that catalyzes the oxidative decarboxylation of malate to pyruvate. It had previously been weakly linked to a syndrome known as Friedreich ataxia that has since been shown to be the result of mutation in a completely different gene. Certain single-nucleotide polymorphism haplotypes of this gene have been shown …
- **Diseases (Open Targets)**: liver disorder (0.215); diabetes mellitus (0.214); major depressive disorder (0.213); aneurysm (0.133); aortic aneurysm (0.132)
- **Europe PMC papers**: 6359
- **Why important**: ME2 occupies a bridge position between DDX6 and HDGF, connecting the RNA-regulatory side of the network with the transcriptional and growth-associated side. Its established mitochondrial NAD-dependent malic-enzyme activity links the module to oxidative metabolism, and its HPA tissue enhancement in choroid plexus makes it the most tissue-distinctive member in the supplied profile. It has the largest literature volume among the listed genes and disease associations involving liver disorder, diabetes, major depressive disorder, and aneurysm.
- **Conclusion**: Established evidence supports ME2 as a mitochondrial metabolic marker and a structurally important bridge. Its role as a causal metabolic coordinator in bone and myometrium remains a hypothesis rather than a demonstrated conclusion.

#### PSMC2

- **Related proteins** (co-abundance neighbors): EIF3L (0.86), TRNT1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 connects EIF3L with TRNT1 and therefore links translation initiation with tRNA processing. It is an ATPase subunit of the proteasome regulatory complex and has supplied annotations for ubiquitin-dependent proteolysis, oxidative-stress response, and osteoblast differentiation. Its disease associations include plasma-cell myeloma, mantle-cell lymphoma, neoplasm, HIV infection, and amyloidosis, while its literature support is substantial.
- **Conclusion**: Established evidence supports PSMC2 as a proteostasis component with a relevant osteoblast-differentiation annotation. Its network position makes it a plausible connection between translation and protein degradation, but the module data do not show that this proteasome function is specifically activated in either tissue.

#### TRNT1

- **Related proteins** (co-abundance neighbors): DDX6 (0.84), PSMC2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tRNA nucleotidyl transferase 1. The protein encoded by this gene is a CCA-adding enzyme which belongs to the tRNA nucleotidyltransferase/poly(A) polymerase family. This essential enzyme functions by catalyzing the addition of the conserved nucleotide triplet CCA to the 3' terminus of tRNA molecules. Mutations in this gene result in sideroblastic anemia with B-cell immunodeficiency, periodic fevers, and developmental delay. Alter…
- **Diseases (Open Targets)**: congenital sideroblastic anemia-B-cell immunodeficiency-periodic fever-developmental delay syndrome (0.836); retinitis pigmentosa and erythrocytic microcytosis (0.760); inherited retinal dystrophy (0.528); hereditary disease (0.470); autosomal recessive non-syndromic intellectual disability (0.412)
- **Europe PMC papers**: 902
- **Why important**: TRNT1 connects DDX6 with PSMC2 and is therefore positioned at the interface of RNA processing, translation-related quality control, and proteostasis. Its established CCA-adding activity is essential for cytosolic and mitochondrial tRNA maturation, tRNA surveillance, and rescue of stalled cytosolic ribosomes. It has strong disease relevance through syndromes involving sideroblastic anemia, B-cell immunodeficiency, periodic fever, developmental delay, erythrocytic microcytosis, and retinal disease.
- **Conclusion**: Established evidence supports TRNT1 as an essential RNA-maturation and translation-surveillance factor. Its co-abundance with DDX6 and PSMC2 is compatible with a cellular quality-control state, but does not prove a direct functional interaction or a tissue-specific role.

#### HDGF

- **Related proteins** (co-abundance neighbors): TCEA1 (0.91), ME2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_14982.1
- **Function (MyGene.info)**: heparin binding growth factor. This gene encodes a member of the hepatoma-derived growth factor family. The encoded protein has mitogenic and DNA-binding activity and may play a role in cellular proliferation and differentiation. High levels of expression of this gene enhance the growth of many tumors. This gene was thought initially to be located on chromosome X; however, that location has been determined to correspond to a re…
- **Diseases (Open Targets)**: prostate carcinoma (0.394); neurodegenerative disease (0.287); hepatocellular carcinoma (0.115); neoplasm (0.112); non-small cell lung carcinoma (0.111)
- **Europe PMC papers**: 2439
- **Why important**: HDGF is a network bridge between TCEA1 and ME2 and is the only module member supported by the supplied hu.MAP evidence through complex C1 with TCEA1. It has established mitogenic, DNA-binding, transcriptional, chromatin-remodeling, and cell-division-related annotations, and it is the sole gene annotated as secreted to blood. It has substantial literature representation and disease associations involving prostate carcinoma, neurodegenerative disease, hepatocellular carcinoma, and other neoplasms.
- **Conclusion**: Established evidence supports HDGF as a transcriptional and growth-associated factor and supports a reported complex relationship with TCEA1. Its secretion annotation warrants attention to extracellular contribution, but the broad HPA profile and low immune-cell specificity do not support interpreting the module as a blood-derived secreted-protein module.

## Module 12

**Tissue pair**: bone and myometrium  
**Genes (7)**: HSD17B4, DNM2, IDE, PSMA1, PSMA4, SEC23IP, UGGT1

### Function

The module does not have any GO or KEGG term passing global correction, so no statistically supported pathway-level annotation can be assigned from those analyses. Its structure is nevertheless biologically interpretable: the module contains a proteasome alpha-subunit pair, PSMA1 and PSMA4, supported by the supplementary STRING proteasome signatures (STRING SMART Proteasome subunit A N-terminal signature  Add an annotation; within-query FDR = 0.0326) and (STRING Pfam Proteasome subunit; within-query FDR = 0.039), together with genes involved in endocytosis and membrane dynamics, insulin and peptide degradation, ER protein quality control, peroxisomal fatty-acid metabolism, and ER-to-Golgi transport. The co-abundance pattern therefore most plausibly reflects coordinated intracellular protein and membrane homeostasis rather than a demonstrated tissue-specific pathway. The proteasome interpretation is supported by direct interaction and complex evidence, whereas the broader functional integration remains provisional.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only IDE is annotated as secreted in other tissues, while UGGT1 is annotated as intracellular and membrane and the remaining genes are not secretome genes. HPA indicates generally low tissue specificity for most genes, with HSD17B4 tissue enhanced in liver. Cell-type enhancement is common across the module, including neutrophils, adipocytes, microglia, alveolar cells type two, hepatocytes, erythrocyte progenitors, and several trophoblast or germ-cell populations, but blood-cell specificity is generally low and only one gene is immune-cell enhanced. Thus, the shared bone–myometrium signal is unlikely to be explained solely by a uniform blood-cell or plasma-protein signature, although mixed cell composition and broadly distributed intracellular programs remain plausible. In myometrium, protein detection is present for most module genes, whereas bone has no matching HPA tissue protein evidence, so the cross-tissue interpretation should not be treated as direct protein-level confirmation in bone.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, PSMA1–PSMA4, and no STRING partners are reported for the other genes. The same pair appears together in three hu.MAP complexes (hu.MAP huMAP3_00356.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1), each representing larger proteasome-containing assemblies. These findings establish that the PSMA1–PSMA4 edge is a known physical or complex-level relationship rather than a novel inferred association. They also indicate that the module captures only a small portion of much larger proteasome assemblies; the other module genes are not supported as members of those complexes. The remaining co-abundance edges are therefore not corroborated by the supplied STRING or hu.MAP evidence and should be interpreted as network-level associations requiring independent validation.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: PSMA1–PSMA4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Proteasome subunit A N-terminal signature  Add an annotation (FDR = 0.0326, 2 genes); Pfam Proteasome subunit (FDR = 0.039, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00356.1 (PSMA1, PSMA4; 2/33); huMAP3_09656.1 (PSMA1, PSMA4; 2/64); huMAP3_13725.1 (PSMA1, PSMA4; 2/69)

### Novelty

The module-level observation may be a new cross-tissue co-abundance pattern, because the supplied evidence identifies a shared bone–myometrium module containing a mixture of proteasome, trafficking, proteolysis, ER quality-control, and peroxisomal genes. However, novelty is not established merely because most edges are absent from STRING or hu.MAP. PSMA1–PSMA4 is already well known, and the individual functions and disease associations of the genes are established. A defensible conclusion is that the cross-tissue co-abundance configuration is potentially novel, while its molecular mechanism and reproducibility remain unproven. Demonstrating novelty would require replication in independent cohorts, control for cell composition and technical effects, and comparison with existing tissue co-expression modules.

**Hypothesis.** Hypothesis: the shared module reflects coordinated intracellular proteostasis and membrane-organelle remodeling in cells present in both bone and myometrium. In this model, PSMA1 and PSMA4 represent a proteasomal degradation component; UGGT1 supports ER glycoprotein quality control; SEC23IP and DNM2 support ER-to-Golgi trafficking, vesicle biology, endocytosis, and cell motility; IDE contributes peptide turnover; and HSD17B4 links the signal to peroxisomal lipid metabolism and steroid-related metabolism. The observed co-abundance could therefore arise during cellular remodeling, matrix-associated cell activity, or tissue stress, but the fact sheet does not establish causality, directionality, or a specific cell type for this mechanism.

### Important genes

#### PSMA1

- **Related proteins** (co-abundance neighbors): PSMA4 (0.86), HSD17B4 (0.83); STRING partners: PSMA4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_00356.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 20S subunit alpha 1. The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent proc…
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.535); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1417
- **Why important**: PSMA1 is a central member of the module's only directly supported high-confidence STRING pair, interacts with PSMA4, and occurs in all three reported hu.MAP proteasome complexes (hu.MAP huMAP3_00356.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1). Its annotation places it in the twenty-S proteasome core and links it to ubiquitin-dependent protein catabolism, DNA repair, apoptosis, inflammatory regulation, and immune-system processes. It also has substantial disease and literature support, including associations with plasma-cell and other neoplastic disorders.
- **Conclusion**: Established evidence supports PSMA1 as a proteasome-core component and as the strongest mechanistically anchored part of the module. Its module-level co-abundance may indicate proteostasis or stress-related biology, but the data do not show that PSMA1 drives the cross-tissue pattern.

#### PSMA4

- **Related proteins** (co-abundance neighbors): PSMA1 (0.86); STRING partners: PSMA1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_00356.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 20S subunit alpha 4. This gene encodes a core alpha subunit of the 20S proteosome, which is a highly ordered ring-shaped structure composed of four rings of 28 non-identical subunits. Proteasomes cleave peptides in an ATP- and ubiquitin-dependent manner. [provided by RefSeq, Aug 2016].
- **Diseases (Open Targets)**: plasma cell myeloma (0.616); mantle cell lymphoma (0.542); neoplasm (0.513); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1240
- **Why important**: PSMA4 is the direct partner of PSMA1 in STRING and is present with PSMA1 in all three hu.MAP complexes (hu.MAP huMAP3_00356.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1). It encodes another twenty-S proteasome alpha subunit and has annotations involving protein catabolism, DNA repair, apoptosis, oxidative-stress response, and immune-system processes. Its disease associations and literature support are substantial, making it an important independently recognizable component rather than an uncharacterized network member.
- **Conclusion**: Established evidence identifies PSMA4 as a proteasome-core subunit whose association with PSMA1 is known. Its presence supports a proteasome-related interpretation of part of the module, while the absence of broader within-module STRING support limits claims about the other edges.

#### DNM2

- **Related proteins** (co-abundance neighbors): IDE (0.86), SEC23IP (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 2. Dynamins represent one of the subfamilies of GTP-binding proteins. These proteins share considerable sequence similarity over the N-terminal portion of the molecule, which contains the GTPase domain. Dynamins are associated with microtubules. They have been implicated in cell processes such as endocytosis and cell motility, and in alterations of the membrane that accompany certain activities such …
- **Diseases (Open Targets)**: autosomal dominant centronuclear myopathy (0.844); Charcot-Marie-Tooth disease dominant intermediate B (0.830); fetal akinesia-cerebral and retinal hemorrhage syndrome (0.739); autosomal dominant Charcot-Marie-Tooth disease type 2M (0.715); centronuclear myopathy (0.692)
- **Europe PMC papers**: 2412
- **Why important**: DNM2 has high network connectivity within the module and links the trafficking-related SEC23IP branch to the IDE branch. It encodes a dynamin GTPase involved in endocytosis, membrane remodeling, cell motility, post-Golgi transport, and autophagy, with particular relevance to osteoclast-associated bone resorption noted in the supplied annotation. It also has extensive literature and established disease associations involving centronuclear and Charcot-Marie-Tooth myopathies.
- **Conclusion**: Established evidence supports DNM2 as a membrane-dynamics and endocytic regulator with plausible relevance to both tissue remodeling and cellular trafficking. Its bridging position suggests a possible integrative role in the module, but this bridging interpretation is a hypothesis based on co-abundance topology rather than demonstrated molecular interaction.

#### HSD17B4

- **Related proteins** (co-abundance neighbors): UGGT1 (0.84), PSMA1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Peroxisomes; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydroxysteroid 17-beta dehydrogenase 4. The protein encoded by this gene is a bifunctional enzyme that is involved in the peroxisomal beta-oxidation pathway for fatty acids. It also acts as a catalyst for the formation of 3-ketoacyl-CoA intermediates from both straight-chain and 2-methyl-branched-chain fatty acids. Defects in this gene that affect the peroxisomal fatty acid beta-oxidation activity are a cause of D-bifunctional protein d…
- **Diseases (Open Targets)**: d-bifunctional protein deficiency (0.830); Perrault syndrome 1 (0.761); Perrault syndrome (0.736); hereditary disease (0.488); hearing loss disorder (0.370)
- **Europe PMC papers**: 1624
- **Why important**: HSD17B4 connects the PSMA1 branch with UGGT1 in the module and is the only tissue-enhanced gene in the HPA summary, with liver enhancement. It encodes a peroxisomal bifunctional enzyme involved in fatty-acid beta-oxidation and steroid-related metabolism, and its supplied annotations include osteoblast differentiation. It has clear disease relevance through d-bifunctional protein deficiency and related inherited disorders.
- **Conclusion**: Established evidence supports HSD17B4 as a peroxisomal metabolic enzyme with a plausible connection to lipid, steroid, and osteoblast biology. Its placement beside proteasome and ER-quality-control genes suggests coordinated organelle or metabolic remodeling, but no enrichment result establishes that interpretation for the complete module.

#### UGGT1

- **Related proteins** (co-abundance neighbors): HSD17B4 (0.84), IDE (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UDP-glucose glycoprotein glucosyltransferase 1. UDP-glucose:glycoprotein glucosyltransferase (UGT) is a soluble protein of the endoplasmic reticulum (ER) that selectively reglucosylates unfolded glycoproteins, thus providing quality control for protein transport out of the ER.[supplied by OMIM, Oct 2009].
- **Diseases (Open Targets)**: congenital disorder of glycosylation (0.416); hypercholesterolemia, familial, 1 (0.333); connective tissue disorder (0.234); ovarian dysfunction (0.216); chronic laryngitis (0.147)
- **Europe PMC papers**: 507
- **Why important**: UGGT1 occupies a central position in the module's HSD17B4–UGGT1–IDE segment. It encodes an ER quality-control enzyme that reglucosylates incompletely folded glycoproteins and participates in glycoprotein biosynthesis, post-translational folding, and ER mannose processing. Its disease associations include congenital glycosylation and connective-tissue-related disorders, while its literature volume is more limited than that of IDE or DNM2.
- **Conclusion**: Established evidence supports UGGT1 as an ER protein-folding and glycoprotein-quality-control factor. Its co-abundance with trafficking, proteolysis, and metabolic genes is consistent with a proteostasis hypothesis, but the module does not prove that ER quality control is the principal shared tissue function.

#### IDE

- **Related proteins** (co-abundance neighbors): DNM2 (0.86), UGGT1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin degrading enzyme. This gene encodes a zinc metallopeptidase that degrades intracellular insulin, and thereby terminates insulins activity, as well as participating in intercellular peptide signalling by degrading diverse peptides such as glucagon, amylin, bradykinin, and kallidin. The preferential affinity of this enzyme for insulin results in insulin-mediated inhibition of the degradation of other peptides such as…
- **Diseases (Open Targets)**: diabetes mellitus (0.307); type 2 diabetes mellitus (0.287); diabetic retinopathy (0.146); diabetic eye disease (0.144); brain cancer (0.142)
- **Europe PMC papers**: 19876
- **Why important**: IDE is connected to both UGGT1 and DNM2 and has the strongest literature volume among the module genes in the fact sheet. It encodes a zinc metallopeptidase that degrades insulin and several other peptides, and its annotations include proteolysis, insulin-receptor signaling, peptide catabolism, ubiquitin recycling, and antigen processing. It is also annotated as secreted in other tissues, which makes it relevant when considering extracellular or tissue-compartment effects despite the module not being broadly secreted.
- **Conclusion**: Established evidence supports IDE as a multifunctional peptide-degrading enzyme with metabolic and signaling relevance. Its network position makes it a plausible link between membrane trafficking and protein or peptide turnover, but the shared-module data do not establish an insulin-centered mechanism or a causal role for IDE.

## Module 13

**Tissue pair**: bone and myometrium  
**Genes (5)**: FDPS, PPM1G, PFN2, GART, VTA1

### Function

The module does not support a single statistically established pathway: no GO/KEGG term passed global correction, and there was no supplementary STRING functional enrichment. Its genes instead span intracellular vesicle trafficking through VTA1, pre-mRNA-splicing and stress-response regulation through PPM1G, actin dynamics through PFN2, de novo purine synthesis through GART, and sterol and isoprenoid synthesis through FDPS. The network is small and sparse, with the strongest connectivity concentrated around VTA1–PPM1G–PFN2 and terminal links from VTA1 to GART and PFN2 to FDPS. The most cautious interpretation is a co-abundance signature of shared intracellular cellular state or biosynthetic activity rather than a demonstrated common molecular pathway. The absence of enrichment does not invalidate the module.

**Cell composition.** The module is not composed of plasma or secreted proteins: all members are classified as non-secreted, and all show low immune-cell specificity. Thus, a blood-cell or circulating-protein explanation is not supported by the HPA summary. The composition is more consistent with intracellular proteins, including nucleoplasmic, cytosolic, vesicular, and cytoskeletal-associated biology. HPA profiles are heterogeneous rather than bone- or myometrium-specific: several genes are tissue or cell-type enhanced in liver, testis, brain, germ-cell populations, cardiac-related cells, or alveolar cells, while other genes have low tissue specificity. Protein detection in myometrium is mixed, and matched bone protein evidence is unavailable. These observations make shared cell composition, cellular state, or broader tissue contamination plausible explanations for the cross-tissue signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was present among the module members, and there was no STRING functional enrichment. No hu.MAP complex contained multiple members. Therefore, the co-abundance relationships are not recapitulated as established physical interactions or a known multiprotein complex in these resources. The absence of such evidence argues against calling this a known molecular complex, but it does not exclude indirect regulation, coordinated expression, condition-dependent interactions, or associations below the database confidence threshold.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears to be a new data-derived co-abundance association rather than a rediscovery of a documented STRING interaction network or hu.MAP complex. However, it cannot be claimed as a new biological pathway solely because the relationships are absent from those databases. The lack of globally significant GO/KEGG enrichment, the absence of STRING enrichment, the heterogeneous HPA expression patterns, and the lack of a shared annotated complex all make the biological novelty uncertain. The strongest defensible novelty claim is that these genes co-vary in the bone–myometrium analysis; independent replication and experimental validation would be required before assigning a new mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated intracellular resource handling in a shared or recurring cell state. VTA1-mediated endosomal or multivesicular-body trafficking may occur alongside PPM1G-dependent control of splicing and stress-related phosphorylation, PFN2-linked actin remodeling, GART-supported purine production, and FDPS-supported sterol or isoprenoid synthesis. This could represent a proliferative, remodeling, or metabolically active state that is present in both tissues, or a shared cellular composition signal. This is a hypothesis, not an established pathway, because the genes lack significant pathway enrichment, known within-module STRING links, and a shared hu.MAP complex.

### Important genes

#### VTA1

- **Related proteins** (co-abundance neighbors): GART (0.93), PPM1G (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Vesicles, Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vesicle trafficking 1. C6ORF55 encodes a protein involved in trafficking of the multivesicular body, an endosomal compartment involved in sorting membrane proteins for degradation in lysosomes (Ward et al., 2005 [PubMed 15644320]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: HIV infectious disease (0.462); Abnormality of the skeletal system (0.267); Menorrhagia (0.251); COVID-19 (0.192); severe acute respiratory syndrome (0.190)
- **Europe PMC papers**: 1165
- **Why important**: VTA1 is the strongest network connector in the module and links PPM1G with GART. Its established annotation in multivesicular-body sorting, late-endosome trafficking, macroautophagy, and ESCRT-III disassembly gives the module a plausible intracellular trafficking axis. It has low tissue and cell-type specificity, is detected in myometrium, and has substantial literature and disease associations including skeletal-system abnormality and menorrhagia.
- **Conclusion**: Established evidence supports VTA1 as a trafficking and endosomal component and as a structural anchor of this co-abundance module. It is a reasonable candidate for coordinating cellular-state biology, but the module does not establish that VTA1 mechanistically regulates the other members.

#### PPM1G

- **Related proteins** (co-abundance neighbors): PFN2 (0.83), VTA1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase, Mg2+/Mn2+ dependent 1G. The protein encoded by this gene is a member of the PP2C family of Ser/Thr protein phosphatases. PP2C family members are known to be negative regulators of cell stress response pathways. This phosphatase is found to be responsible for the dephosphorylation of Pre-mRNA splicing factors, which is important for the formation of functional spliceosome. Studies of a similar gene in mice suggested a rol…
- **Diseases (Open Targets)**: neurodegenerative disease (0.264); hepatocellular carcinoma (0.110); Crohn disease (0.106); lung adenocarcinoma (0.096); gout (0.081)
- **Europe PMC papers**: 799
- **Why important**: PPM1G is a high-connectivity internal member linking PFN2 and VTA1. It is a PP2C-family serine/threonine phosphatase involved in protein dephosphorylation, pre-mRNA-splicing-factor dephosphorylation, stress-response regulation, and cell-cycle regulation. HPA describes testis enhancement and enrichment in spermatid and spermatocyte populations, while myometrial protein is detected. Its substantial literature and disease associations make it biologically informative despite the lack of STRING or hu.MAP support.
- **Conclusion**: Established evidence supports PPM1G as a regulator of phosphorylation and RNA-processing or cell-state functions. Its position makes it a plausible regulatory bridge in the module, but a direct connection to VTA1 or PFN2 remains hypothetical.

#### PFN2

- **Related proteins** (co-abundance neighbors): PPM1G (0.83), FDPS (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: profilin 2. The protein encoded by this gene is a ubiquitous actin monomer-binding protein belonging to the profilin family. It is thought to regulate actin polymerization in response to extracellular signals. There are two alternatively spliced transcript variants encoding different isoforms described for this gene. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: genetic developmental and epileptic encephalopathy (0.515); neurodegenerative disease (0.354); smoking initiation (0.338); substance abuse (0.219); attention deficit-hyperactivity disorder (0.219)
- **Europe PMC papers**: 1039
- **Why important**: PFN2 is an internal bridge between PPM1G and FDPS and represents the cytoskeletal aspect of the module. Its established functions include actin polymerization, actin-bundle organization, epithelial-cell migration, and modulation of chemical synaptic transmission. HPA shows brain enhancement and cell-type enhancement in neuronal or muscle-related and germ-cell populations. It has substantial literature and disease associations including developmental epileptic encephalopathy and neurodegenerative disease.
- **Conclusion**: Established evidence supports PFN2 as an actin-regulatory protein with broad cell-type relevance. It may link cellular architecture to the other module processes, but the co-abundance data do not establish that PFN2 connects cytoskeletal remodeling to sterol synthesis or phosphatase activity.

#### GART

- **Related proteins** (co-abundance neighbors): VTA1 (0.93); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase. The protein encoded by this gene is a trifunctional polypeptide. It has phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase activity which is required for de novo purine biosynthesis. This enzyme is highly conserved in vertebrates. Alternative splicing of this gene results in two transcript variants encoding different isoforms.…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.606); mesothelioma (0.584); malignant pleural mesothelioma (0.557); adenocarcinoma (0.486); anaplastic lung carcinoma (0.462)
- **Europe PMC papers**: 1890
- **Why important**: GART is a terminal member connected to VTA1 and supplies a direct metabolic interpretation through its trifunctional role in de novo purine and IMP or GMP biosynthesis. It is highly conserved, has low tissue specificity, is detected in myometrium, and has extensive literature and multiple cancer-related disease associations. Its cell-type profile includes cardiac-related cells.
- **Conclusion**: Established evidence supports GART as a purine-biosynthetic enzyme and a marker of biosynthetic demand. It could indicate nucleotide requirements in the shared cellular state, but there is no evidence here that its purine pathway is coordinated mechanistically with VTA1-mediated trafficking.

#### FDPS

- **Related proteins** (co-abundance neighbors): PFN2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: farnesyl diphosphate synthase. This gene encodes an enzyme that catalyzes the production of geranyl pyrophosphate and farnesyl pyrophosphate from isopentenyl pyrophosphate and dimethylallyl pyrophosphate. The resulting product, farnesyl pyrophosphate, is a key intermediate in cholesterol and sterol biosynthesis, a substrate for protein farnesylation and geranylgeranylation, and a ligand or agonist for certain hormone receptors …
- **Diseases (Open Targets)**: porokeratosis 9, multiple types (0.637); disseminated superficial actinic porokeratosis (0.619); osteoporosis (0.611); postmenopausal osteoporosis (0.601); plasma cell myeloma (0.599)
- **Europe PMC papers**: 2675
- **Why important**: FDPS is the terminal member connected to PFN2 and provides the module’s sterol and isoprenoid axis. It produces farnesyl diphosphate, a precursor for cholesterol and sterol synthesis and for protein farnesylation and geranylgeranylation. HPA shows liver enhancement and several epithelial cell-type enhancements, with no myometrial detection. It has extensive literature and disease associations including osteoporosis and postmenopausal osteoporosis.
- **Conclusion**: Established evidence supports FDPS as a central metabolic and protein-prenylation enzyme relevant to bone biology. Its association with PFN2 in this module may indicate coordinated remodeling or metabolic state, but that interpretation is provisional because the relationship is not supported by STRING, hu.MAP, or globally significant pathway enrichment.

## Module 14

**Tissue pair**: bone and myometrium  
**Genes (9)**: PAK2, PSMC4, PSMD13, KARS1, YARS1, CCT5, CCT3, CCT7, CCT8

### Function

The strongest interpretation is a conserved intracellular proteostasis module centered on the chaperonin-containing TCP-1 complex, also called CCT or TRiC. The primary enrichment evidence (GO:CC chaperonin-containing T-complex; q_global = 3.1e-05), (GO:CC protein folding chaperone complex; q_global = 0.00135), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.00201), (GO:MF protein folding chaperone; q_global = 0.0111) and (GO:MF unfolded protein binding; q_global = 0.0326) consistently identifies ATP-dependent chaperone-mediated protein folding, unfolded-protein binding and an intracellular protein-containing complex. CCT3, CCT5, CCT7 and CCT8 account for the core signal and form a densely connected CCT group in both the co-abundance network and STRING. The remaining genes add complementary functions: PSMC4 and PSMD13 represent proteasomal ATPase and non-ATPase machinery, while KARS1 and YARS1 represent aminoacyl-tRNA charging and translation-related activity. PAK2 provides a signaling and cytoskeletal-regulatory component. The globally corrected annotations concerning telomere maintenance, nuclear or Cajal-body localization and fertilization (22 globally significant GO/KEGG terms, q_global 3.1e-05–0.000866; see the table), (8 globally significant GO/KEGG terms, q_global 0.00399–0.0111; see the table), and (4 globally significant GO/KEGG terms, q_global 0.0137–0.0201; see the table) should be regarded as annotations carried by the CCT quartet rather than evidence that this bone-myometrium module is specifically a reproductive or telomere module. The broad ATP or nucleotide-binding enrichments (GO:MF ATP binding; q_global = 0.00299), (GO:MF adenyl ribonucleotide binding; q_global = 0.00299), (GO:MF adenyl nucleotide binding; q_global = 0.00987), and (GO:MF purine ribonucleotide binding; q_global = 0.023) (GO:MF purine ribonucleoside triphosphate binding; q_global = 0.023) (GO:MF ribonucleotide binding; q_global = 0.0253) are consistent with the enzymatic and ATP-dependent machinery represented in the module.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module: HPA reports only one secretome-associated gene, KARS1, with an intracellular and membrane annotation, and the other genes are intracellular. It is also not blood-cell enriched by the available HPA evidence, since every gene has low immune-cell specificity and no blood-cell enrichment is reported. The composition is instead broadly expressed and housekeeping-like, with low tissue specificity for every module gene. HPA nevertheless reports cell-type enhancement for most genes, especially in spermatogenic cells, with additional enhancement in syncytiotrophoblasts and, for individual genes, neutrophils, cardiomyocytes, Hofbauer cells or oocytes. These patterns do not establish that those cell types drive the bone-myometrium signal. Protein detection is reported for several genes in myometrium, whereas matching HPA bone protein data are unavailable. The shared module could therefore reflect conserved cellular proteostasis and biosynthetic activity, shared cell-state composition, or technical co-abundance of abundant intracellular proteins rather than a specialized extracellular bone-myometrium pathway.

**GO/KEGG enrichment**: 52 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chaperonin-containing T-complex | 3.1e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 3.1e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 3.1e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 3.1e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 3.1e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 3.1e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 3.1e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 3.1e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP binding of sperm to zona pellucida | 0.000109 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 0.000109 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to Cajal body | 0.000109 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 0.000109 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 0.000109 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 0.000109 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomere lengthening | 0.000109 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING provides strong prior support for the CCT interpretation: CCT3, CCT5, CCT7 and CCT8 form a mutually connected CCT clique, and the STRING functional annotations (9 supplementary STRING terms; within-query FDR 3.05e-05–0.00015) identify the TCP-1 or Cpn60 chaperonin family and its component complex. The Reactome-linked annotations (STRING RCTM Folding of actin by CCT/TriC; within-query FDR = 0.0002), (STRING RCTM Association of TriC/CCT with target proteins during biosynthesis; within-query FDR = 0.0002), (STRING RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding; within-query FDR = 0.00031) and (STRING RCTM Formation of tubulin folding intermediates by CCT/TriC; within-query FDR = 0.00049) further support CCT-associated folding of actin, tubulin and other nascent proteins. STRING also independently connects KARS1 with YARS1 and PSMC4 with PSMD13, matching aminoacyl-tRNA synthetase and proteasome substructures. The STRING ATP-binding annotation (STRING Keyword ATP-binding; within-query FDR = 0.00023) is supplementary and should not be treated as global enrichment evidence. hu.MAP independently places the four CCT genes together in several complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), while PSMC4 and PSMD13 co-occur in multiple proteasome complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). Thus, much of the module reflects already known physical or complex-level relationships. The co-abundance network additionally links the CCT group with proteasome, translation and signaling genes, but those cross-system links are not all independently confirmed by STRING or hu.MAP.

**STRING interactions (score >= 0.7)**: 8 of 36 gene pairs: CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999); KARS1–YARS1 (0.988); PSMC4–PSMD13 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam TCP-1/cpn60 chaperonin family (FDR = 3.05e-05, 4 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 0.00013, 4 genes); Component Chaperonin-containing T-complex (FDR = 0.00013, 4 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 0.00015, 4 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 0.00015, 4 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 0.00015, 4 genes); InterPro GroEL-like apical domain superfamily (FDR = 0.00015, 4 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 0.00015, 4 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 0.00015, 4 genes); RCTM Folding of actin by CCT/TriC (FDR = 0.0002, 4 genes); RCTM Association of TriC/CCT with target proteins during biosynthesis (FDR = 0.0002, 4 genes); Keyword ATP-binding (FDR = 0.00023, 8 genes); RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding (FDR = 0.00031, 4 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis (FDR = 0.00032, 4 genes); RCTM Formation of tubulin folding intermediates by CCT/TriC (FDR = 0.00049, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_05064.1 (PSMC4, PSMD13; 2/31); huMAP3_09656.1 (PSMC4, PSMD13; 2/64); huMAP3_13725.1 (PSMC4, PSMD13; 2/69)

### Novelty

The module should not be described as a discovery of a new CCT, proteasome or translation complex: those relationships are already well established by STRING and hu.MAP, and the CCT genes have substantial prior literature. A potentially novel aspect is the coordinated co-abundance of these established intracellular systems across bone and myometrium, especially the particular connection of the CCT group with PSMC4, PSMD13, KARS1, YARS1 and PAK2 in this tissue pair. However, the fact sheet does not demonstrate tissue-specific causality, physical interaction for every network edge, or uniqueness relative to other tissue pairs. Absence of a STRING or hu.MAP relationship for PAK2, KARS1 or YARS1 does not by itself prove novelty. The appropriate conclusion is a potentially distinctive cross-tissue co-abundance pattern built largely from canonical proteostasis and biosynthetic machinery, requiring independent replication and comparison with other modules before being called a new biological mechanism.

**Hypothesis.** Hypothesis: bone and myometrium share a cellular state in which high protein synthesis, cytoskeletal remodeling and proteome quality control are coordinated. The CCT machinery may fold newly synthesized structural and signaling proteins, the proteasome may remove damaged or obsolete proteins, and KARS1 and YARS1 may support the corresponding translational demand. PAK2 could connect this proteostasis state to Rho-family-dependent cytoskeletal remodeling, cell migration or stress signaling. This model predicts coordinated changes in protein folding, proteasomal activity, translation and cytoskeletal signaling, but the current co-abundance data do not establish directionality, physical coupling across all components, or a bone-myometrium-specific causal pathway.

### Important genes

#### CCT3

- **Related proteins** (co-abundance neighbors): PSMD13 (0.91), CCT7 (0.91), PAK2 (0.87), CCT8 (0.82); STRING partners: CCT5 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is the strongest network hub in the module and is one of the four genes driving all of the primary CCT-centered enrichment terms (23 globally significant GO/KEGG terms, q_global 3.1e-05–0.000866; see the table), (6 globally significant GO/KEGG terms, q_global 0.00135–0.00289; see the table), (6 globally significant GO/KEGG terms, q_global 0.00399–0.00892; see the table), (6 globally significant GO/KEGG terms, q_global 0.0111–0.0201; see the table), and (GO:BP RNA localization; q_global = 0.028) (GO:MF unfolded protein binding; q_global = 0.0326) (GO:BP positive regulation of DNA metabolic process; q_global = 0.0377). It has direct STRING links to the other CCT subunits, appears in multiple hu.MAP CCT-containing complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), and has an established role in ATP-dependent folding of actin, tubulin and other proteins. Its extensive literature and disease-association record make it a well-supported anchor rather than a speculative marker.
- **Conclusion**: Established: CCT3 is a central component of the TRiC/CCT chaperonin and a major structural and functional explanation for this module. Hypothesis: its hub position may make CCT3 abundance a useful proxy for the shared proteostasis state, but that proxy should be tested experimentally.

#### CCT5

- **Related proteins** (co-abundance neighbors): YARS1 (0.84), PAK2 (0.84); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is a member of the same highly supported CCT quartet, participates in the full set of CCT-centered primary terms, and is connected to CCT3, CCT7 and CCT8 in STRING and to several hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It also connects in the co-abundance graph to YARS1 and PAK2, potentially linking chaperone activity with translation and signaling. CCT5 has substantial literature and documented disease associations, including hereditary sensory and autonomic neuropathy.
- **Conclusion**: Established: CCT5 supports the interpretation of a genuine CCT chaperone signal rather than an isolated annotation artifact. Hypothesis: its cross-links to YARS1 and PAK2 may reflect coupling between protein synthesis, folding and cytoskeletal or stress signaling, but the network alone cannot establish that mechanism.

#### PSMC4

- **Related proteins** (co-abundance neighbors): PSMD13 (0.90), CCT8 (0.88), KARS1 (0.85); STRING partners: PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 4. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.603); mantle cell lymphoma (0.542); neoplasm (0.519); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1065
- **Why important**: PSMC4 is a network connector between the CCT-related portion and the proteasome portion of the module. It is linked to PSMD13 by STRING and co-occurs with PSMD13 in several hu.MAP proteasome complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). Its ATPase and proteasomal annotations contribute to the globally corrected intracellular-complex and nucleotide-binding terms (GO:CC intracellular protein-containing complex; q_global = 0.00103), (GO:MF ATP binding; q_global = 0.00299), (GO:MF adenyl ribonucleotide binding; q_global = 0.00299), (GO:MF adenyl nucleotide binding; q_global = 0.00987), and (GO:MF ATP hydrolysis activity; q_global = 0.0182), and it has a substantial literature and multiple disease associations.
- **Conclusion**: Established: PSMC4 represents proteasomal protein-processing capacity within the module. Hypothesis: its connection to CCT genes may indicate coordinated folding and clearance of proteins during cellular stress or elevated biosynthetic activity.

#### PSMD13

- **Related proteins** (co-abundance neighbors): CCT3 (0.91), PSMC4 (0.90), CCT8 (0.86); STRING partners: PSMC4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 is the proteasome-associated partner of PSMC4 and has a relatively central position in the co-abundance graph, connecting the proteasome pair with CCT3 and CCT8. Its membership in hu.MAP proteasome complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) and its proteasome annotations provide an independent functional interpretation, while its nuclear speckle localization is compatible with intracellular protein and RNA regulatory processes. It has a substantial literature and disease-association record.
- **Conclusion**: Established: PSMD13 supports a proteasome component within the module and is not merely an unannotated co-abundant gene. Hypothesis: the PSMC4-PSMD13 pair may couple proteasomal turnover to CCT-dependent folding, although direct coupling in bone or myometrium remains unproven.

#### PAK2

- **Related proteins** (co-abundance neighbors): CCT3 (0.87), CCT5 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: p21 (RAC1) activated kinase 2. The p21 activated kinases (PAK) are critical effectors that link Rho GTPases to cytoskeleton reorganization and nuclear signaling. The PAK proteins are a family of serine/threonine kinases that serve as targets for the small GTP binding proteins, CDC42 and RAC1, and have been implicated in a wide range of biological activities. The protein encoded by this gene is activated by proteolytic cleavage …
- **Diseases (Open Targets)**: Knobloch syndrome 2 (0.525); Knobloch syndrome (0.454); HIV infectious disease (0.370); atrial fibrillation (0.210); ovarian carcinoma (0.175)
- **Europe PMC papers**: 3704
- **Why important**: PAK2 is important because it is the module's clearest signaling and cytoskeletal regulator. It connects to CCT3 and CCT5 in the co-abundance graph, is annotated as a serine/threonine kinase linking RAC1 and CDC42 to cytoskeletal reorganization and nuclear signaling, and is associated with cell migration, protein phosphorylation, starvation response and apoptosis-related biology. Unlike the CCT and proteasome genes, it has no reported STRING partner or hu.MAP complex in this module, making its inclusion especially informative but also less independently validated.
- **Conclusion**: Established: PAK2 supplies a plausible signaling and cytoskeletal dimension to an otherwise strongly housekeeping-like module. Hypothesis: PAK2 may be the tissue-state link that couples proteostasis to remodeling or stress responses in bone and myometrium, but this interpretation requires targeted validation.
