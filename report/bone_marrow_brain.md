# Conserved co-abundance modules: bone_marrow and brain

## Module 0

**Tissue pair**: bone_marrow and brain  
**Genes (25)**: ACADSB, ARFIP1, ATP8A1, RNF40, C1orf50, DNAJB14, DUSP3, ECI2, FOXK1, HSDL2, EPHX2, MTIF3, KDSR, LMBRD2, MCFD2, MEAK7, PARD3, LCP1, SLC25A24, TNPO3, TRAPPC8, TRA2B, USP10, ZMYND8, ZNF148

### Function

The module does not support a single statistically established GO or KEGG function: no GO or KEGG term passed global correction, and there was no STRING functional enrichment. Its structure instead suggests several connected cellular-maintenance themes. A mitochondrial lipid and energy-related branch is represented by ECI2, ACADSB and HSDL2, with ECI2 and HSDL2 linked directly in STRING and ACADSB connected to both. ATP8A1 adds phospholipid translocation and membrane homeostasis, while MCFD2, DNAJB14 and TRAPPC8 suggest endoplasmic-reticulum and Golgi cargo handling, protein folding and vesicle trafficking. MTIF3 is the main network hub and provides a mitochondrial protein-synthesis connection. Regulatory and information-processing genes, including DUSP3, USP10, ZNF148, FOXK1, TRA2B and TNPO3, are consistent with modulation of signaling, transcription, RNA processing and protein stability. The most defensible interpretation is therefore a broad, conserved cellular-maintenance module combining mitochondrial metabolism, membrane lipid handling, intracellular trafficking and proteostasis, rather than a narrowly defined pathway.

**Cell composition.** This is not primarily a plasma or secreted-protein module: HPA identifies only one secreted gene, while MCFD2 is classified as intracellular and membrane-associated. The genes are also not predominantly immune-specific. Most have low tissue specificity and low immune-cell specificity, although several are enhanced in neutrophils or neutrophil progenitors, and LCP1 is tissue-enhanced in bone marrow and lymphoid tissue. Liver and hepatocyte enrichment occurs for several metabolic genes, including EPHX2, ECI2 and ACADSB, while other genes show cell-type enhancement in diverse epithelial, muscle, reproductive and neural populations. Protein detection is broad in both bone marrow and brain, with some genes detected preferentially in one of those tissues. Thus, the shared module could partly reflect broadly expressed housekeeping or metabolic programs, with a possible contribution from shared blood-derived or myeloid cell populations in the sampled tissues. The HPA profile does not support interpreting it as a brain-specific neuronal module or as a secreted blood-protein module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a small, coherent known-interaction island involving ACADSB, ECI2 and HSDL2. These relationships support a mitochondrial or peroxisomal lipid-metabolism interpretation for that part of the module, but STRING provides no functional enrichment for the full gene set. The other module edges are not supported by high-confidence STRING interactions in the supplied evidence, so the co-abundance graph should not be treated as a physical interaction map. hu.MAP identifies complex C1, containing HSDL2 and DNAJB14 among the module genes, together with F2RL1 and TEX2 outside the module. This gives limited support for a protein-complex relationship involving HSDL2 and an endoplasmic-reticulum chaperone component, but it does not establish that the whole module is one complex. Overall, known interaction evidence validates selected local relationships while leaving the broader co-abundance structure unresolved.

**STRING interactions (score >= 0.7)**: 3 of 300 gene pairs: ACADSB–ECI2 (0.917); ACADSB–HSDL2 (0.787); ECI2–HSDL2 (0.921)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09313.1 (HSDL2, DNAJB14; 2/4)

### Novelty

The module should be described as a potentially novel cross-tissue co-abundance pattern, not as a newly discovered molecular complex or pathway. Its component functions are largely established, and the ACADSB–ECI2–HSDL2 relationships and the HSDL2–DNAJB14 complex membership provide prior biological context. At the same time, there is no supplied evidence that this exact bone-marrow–brain co-abundance combination has been reported previously, and the absence of broader STRING or hu.MAP support cannot by itself prove novelty. The most appropriate claim is that the cross-tissue association is a hypothesis-generating observation whose novelty requires comparison with published co-expression studies, independent cohorts and perturbation data.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in bone marrow and brain in which mitochondrial lipid utilization and protein synthesis are coordinated with membrane phospholipid remodeling, endoplasmic-reticulum cargo processing and stress-responsive signaling. A metabolic core involving ECI2, ACADSB and HSDL2 could supply or regulate lipid-handling capacity, ATP8A1 could maintain membrane asymmetry, and MCFD2, DNAJB14 and TRAPPC8 could support secretory-pathway quality control and trafficking. The presence of neutrophil-associated and broadly expressed genes raises an alternative or additional hypothesis that part of the signal arises from shared cell-type composition or blood-derived material rather than coordinated regulation within the same cell. These hypotheses require cell-resolved expression, protein-level validation and experimental perturbation.

### Important genes

#### MTIF3

- **Related proteins** (co-abundance neighbors): ARFIP1 (0.91), TRAPPC8 (0.85), USP10 (0.84), TRA2B (0.83), LCP1 (0.81), ACADSB (0.81), DNAJB14 (0.80), HSDL2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial translational initiation factor 3. This gene encodes a translation initiation factor that is involved in mitochondrial protein synthesis. Polymorphism in this gene is associated with the onset of Parkinson's disease. Alternate splicing results in multiple transcript variants. A pseudogene of this gene is found on chromosome 5. [provided by RefSeq, Oct 2009].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.330); metabolic syndrome (0.309); trauma complication (0.117); obesity disorder (0.116); ovarian neoplasm (0.089)
- **Europe PMC papers**: 807
- **Why important**: MTIF3 is the principal network hub in the supplied graph and connects metabolic, trafficking, regulatory and cytoskeletal-associated genes. Its established role in mitochondrial translation gives the module a plausible mitochondrial anchor, and its association with Parkinson disease makes it relevant to the brain component. It also has a substantial literature base compared with many of the less characterized module members.
- **Conclusion**: Established evidence supports MTIF3 as a mitochondrial translation factor and as the topological organizer of the co-abundance pattern. It is plausible, but not demonstrated, that mitochondrial protein-synthesis capacity coordinates the other module branches.

#### ATP8A1

- **Related proteins** (co-abundance neighbors): C1orf50 (0.88), DUSP3 (0.86), SLC25A24 (0.84), MCFD2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase phospholipid transporting 8A1. The P-type adenosinetriphosphatases (P-type ATPases) are a family of proteins which use the free energy of ATP hydrolysis to drive uphill transport of ions across membranes. Several subfamilies of P-type ATPases have been identified. One subfamily catalyzes transport of heavy metal ions. Another subfamily transports non-heavy metal ions (NMHI). The protein encoded by this gene is a member of the t…
- **Diseases (Open Targets)**: hypercholesterolemia, familial, 1 (0.333); neurodegenerative disease (0.317); eye inflammation (0.122); autism spectrum disorder (0.111); placental abruption (0.109)
- **Europe PMC papers**: 661
- **Why important**: ATP8A1 links the module to aminophospholipid translocation and membrane asymmetry, with annotations extending to transport across the blood-brain barrier. It is detected in both tissues and is enhanced in several cell types, including brain-associated and progenitor populations. Its disease associations include familial hypercholesterolemia and neurodegenerative disease, making it relevant to membrane biology in both tissue contexts.
- **Conclusion**: Established evidence supports ATP8A1 as a membrane lipid transporter with neurological and lipid-homeostasis relevance. Its connection to the module's metabolic branch is a biologically reasonable hypothesis, but the co-abundance data do not establish direct regulation or physical interaction.

#### ECI2

- **Related proteins** (co-abundance neighbors): EPHX2 (0.83), ZNF148 (0.80); STRING partners: ACADSB (0.917), HSDL2 (0.921)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Peroxisomes, Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: enoyl-CoA delta isomerase 2. This gene encodes a member of the hydratase/isomerase superfamily. The protein encoded is a key mitochondrial enzyme involved in beta-oxidation of unsaturated fatty acids. It catalyzes the transformation of 3-cis and 3-trans-enoyl-CoA esters arising during the stepwise degradation of cis-, mono-, and polyunsaturated fatty acids to the 2-trans-enoyl-CoA intermediates. Alternatively spliced transcri…
- **Diseases (Open Targets)**: thyroiditis (0.247); glomerulonephritis (0.161); nephritis (0.141); Abnormality of the skeletal system (0.140); brain aneurysm (0.138)
- **Europe PMC papers**: 516
- **Why important**: ECI2 is a mitochondrial and peroxisomal enzyme involved in beta-oxidation of unsaturated fatty acids. It participates in the strongest STRING-supported metabolic relationships in the module, connecting with ACADSB and HSDL2, and it is liver- and hepatocyte-enhanced while also being detected in brain. Its disease associations include skeletal, renal and inflammatory phenotypes, providing broader relevance beyond a purely tissue-specific interpretation.
- **Conclusion**: Established evidence supports ECI2 as a fatty-acid catabolic enzyme and as part of a known metabolic interaction island. It is a strong candidate for the metabolic core of the module, although its absence from bone-marrow protein detection cautions against assuming uniform activity across both tissues.

#### HSDL2

- **Related proteins** (co-abundance neighbors): MTIF3 (0.80); STRING partners: ACADSB (0.787), ECI2 (0.921)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: huMAP3_09313.1
- **Function (MyGene.info)**: hydroxysteroid dehydrogenase like 2. Predicted to enable oxidoreductase activity. Located in mitochondrion and peroxisome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: preeclampsia (0.258); placental retention (0.217); squamous cell carcinoma (0.190); smoking initiation (0.152); cholangiocarcinoma (0.101)
- **Europe PMC papers**: 403
- **Why important**: HSDL2 occupies a bridge position between the high-confidence metabolic STRING relationships and the hu.MAP complex containing DNAJB14. Its mitochondrial and peroxisomal localization and cholesterol-homeostasis annotation connect lipid metabolism to organelle and proteostasis biology. It is detected in both tissues and is cell-type enhanced in adipocytes, myonuclei and neutrophils, which is compatible with a broad metabolic or cell-state signal.
- **Conclusion**: Established evidence supports HSDL2 as a predicted oxidoreductase associated with cholesterol homeostasis, with known relationships to ACADSB and ECI2 and complex membership with DNAJB14. Its role as the mechanistic bridge between metabolism and endoplasmic-reticulum quality control remains a hypothesis.

#### MCFD2

- **Related proteins** (co-abundance neighbors): DNAJB14 (0.96), ATP8A1 (0.81), TNPO3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: multiple coagulation factor deficiency 2, ER cargo receptor complex subunit. This gene encodes a soluble luminal protein with two calmodulin-like EF-hand motifs at its C-terminus. This protein forms a complex with LMAN1 (lectin mannose binding protein 1; also known as ERGIC-53) that facilitates the transport of coagulation factors V (FV) and VIII (FVIII) from the endoplasmic reticulum to the Golgi apparatus via an endoplasmic reticulum Golgi intermediate compartment (ERGIC…
- **Diseases (Open Targets)**: combined deficiency of factor V and factor VIII (0.712); neurodegenerative disease (0.529); multiple intestinal atresia (0.415); factor V and factor VIII, combined deficiency of, type 1 (0.333); autoimmune disorder of central nervous system (0.331)
- **Europe PMC papers**: 433
- **Why important**: MCFD2 connects ATP8A1, DNAJB14 and TNPO3 in the module graph and is the best-supported cargo-trafficking gene among the selected candidates. It forms an established complex with LMAN1 to transport coagulation factors from the endoplasmic reticulum toward the Golgi, and it is linked to combined factor V and factor VIII deficiency. Its detection in both tissues and intracellular or membrane secretome classification make it relevant to shared trafficking biology without implying that the module is secreted.
- **Conclusion**: Established evidence supports MCFD2 as an endoplasmic-reticulum cargo receptor component with a defined secretory-pathway function and disease association. Its placement beside DNAJB14 and TRAPPC8 suggests a possible quality-control or trafficking submodule, but that extension beyond its established complex is inferential.

## Module 1

**Tissue pair**: bone_marrow and brain  
**Genes (5)**: ACOT8, ERGIC2, GBA1, RPL26L1, SUN1

### Function

The module does not have a GO/KEGG term that passed global correction, and STRING reports no supplementary functional enrichment. Its genes nevertheless converge on intracellular membrane and organelle biology: lysosomal glycolipid metabolism through GBA1, endoplasmic-reticulum/Golgi trafficking through ERGIC2, fatty-acid and acyl-CoA metabolism through ACOT8, nuclear-envelope anchoring and cell movement through SUN1, and translation-related biology through RPL26L1. The co-abundance structure is centered on GBA1, which connects to ERGIC2, SUN1, and RPL26L1, while ERGIC2 connects to ACOT8. Thus, the most defensible interpretation is a heterogeneous intracellular homeostasis module involving lysosome, vesicle, lipid, nuclear-envelope, and protein-synthesis processes rather than a single established pathway. The absence of a globally significant enrichment term does not invalidate the module, but it limits pathway-level certainty.

**Cell composition.** All module genes have low tissue specificity and all are detected at the protein level in both bone marrow and brain. HPA reports low immune-cell specificity for every member, so the module is not specifically supported as a blood-cell program. One member, GBA1, is intracellular and membrane-associated rather than secreted; the module contains only one secreted gene according to the HPA summary. The recurrent HPA single-cell annotations are mainly cell-type-enhanced signals involving spermatids, spermatocytes, and epithelial populations, rather than a coherent bone-marrow or brain cell type. Overall, the composition is more consistent with broadly expressed intracellular biology, or with shared cellular composition across samples, than with a tissue-specific blood program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

At the stated STRING confidence threshold, none of the possible within-module gene pairs is represented as a known STRING interaction. No hu.MAP complex contains multiple module members. Therefore, the observed co-abundance edges are not simply a recovery of documented physical interactions or a known multiprotein complex in these resources. The network may reflect coordinated expression, indirect cellular coupling, shared regulation, or context-dependent interactions that are absent from these databases. The lack of database support also means that the apparent centrality of GBA1 is a property of this co-abundance module, not evidence of established physical binding to its neighbors.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is plausibly a novel co-abundance pattern because its member set has no reported high-confidence STRING relationships, no multi-member hu.MAP complex, and no globally significant GO/KEGG enrichment. However, these observations do not prove biological novelty: database coverage is incomplete, co-abundance is not equivalent to physical interaction, and the genes individually have established functions and disease associations. The appropriate conclusion is that this specific cross-tissue co-abundance configuration is insufficiently characterized and merits validation, rather than that it is definitively a newly discovered pathway.

**Hypothesis.** Hypothesis: the module captures coordinated intracellular housekeeping and stress-sensitive organelle biology shared by bone-marrow and brain samples. In this model, GBA1-linked lysosomal glycolipid handling is co-regulated with ERGIC2-dependent secretory-pathway trafficking, ACOT8-dependent lipid metabolism, SUN1-dependent nuclear-envelope organization, and RPL26L1-associated translation. The coordination could arise from shared cell-state programs, organelle remodeling, or common sample-composition effects rather than direct molecular binding. This hypothesis should be tested by replication in independent cohorts, cell-type-resolved data, and perturbation or localization experiments.

### Important genes

#### GBA1

- **Related proteins** (co-abundance neighbors): SUN1 (0.82), RPL26L1 (0.82), ERGIC2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glucosylceramidase beta 1. This gene encodes a lysosomal membrane protein that cleaves the beta-glucosidic linkage of glycosylceramide, an intermediate in glycolipid metabolism. Mutations in this gene cause Gaucher disease, a lysosomal storage disease characterized by an accumulation of glucocerebrosides. A related pseudogene is approximately 12 kb downstream of this gene on chromosome 1. Alternative splicing results in mul…
- **Diseases (Open Targets)**: Gaucher disease (0.815); Gaucher disease type I (0.814); Gaucher disease type II (0.806); Gaucher disease type III (0.798); Gaucher disease perinatal lethal (0.774)
- **Europe PMC papers**: 2888
- **Why important**: GBA1 is the highest-connectivity member of the module and links the lysosomal and glycolipid-metabolism interpretation to three other genes in the co-abundance graph. Its established function is glucosylceramide cleavage in lysosomes, and its mutations cause Gaucher disease. It has substantial literature and strong disease-focused evidence in the supplied resources. Its broad tissue detection and intracellular membrane localization also fit a shared cellular program across bone marrow and brain.
- **Conclusion**: Established evidence supports GBA1 as the strongest functional anchor and network hub of this module. It is reasonable to hypothesize that variation in lysosomal lipid handling contributes to the shared co-abundance signal, but the module does not establish direct interaction between GBA1 and its neighbors or demonstrate that Gaucher-related biology drives the module.

#### ERGIC2

- **Related proteins** (co-abundance neighbors): GBA1 (0.81), ACOT8 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ERGIC and golgi 2. ERGIC2, or PTX1, is a ubiquitously expressed nuclear protein that is downregulated in prostate carcinoma (Kwok et al., 2001 [PubMed 11445006]).[supplied by OMIM, Aug 2008].
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.340); stricture (0.306); neurodegenerative disease (0.147); cholelithiasis (0.095); Thrombocytopenia (0.091)
- **Europe PMC papers**: 177
- **Why important**: ERGIC2 connects GBA1 with ACOT8 and is the bridge between the module's central lysosomal association and its vesicle and lipid-metabolism branch. Its annotated roles in endoplasmic-reticulum-to-Golgi and retrograde Golgi-to-endoplasmic-reticulum transport provide a plausible trafficking component. It is detected in both tissues and has a vesicular and Golgi localization, while its disease literature is more limited than that of GBA1 or SUN1.
- **Conclusion**: Established evidence supports ERGIC2 as a vesicle-trafficking component of the module. Its bridging position makes it important for the mechanistic hypothesis, but whether it connects lysosomal function to ACOT8 biology in these tissues remains a hypothesis rather than a demonstrated mechanism.

#### SUN1

- **Related proteins** (co-abundance neighbors): GBA1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Sad1 and UNC84 domain containing 1. This gene is a member of the unc-84 homolog family and encodes a nuclear envelope protein with an Unc84 (SUN) domain. The protein is involved in nuclear anchorage and migration. Alternatively spliced transcript variants have been described. [provided by RefSeq, Jan 2019].
- **Diseases (Open Targets)**: atrial fibrillation (0.471); neurodegenerative disease (0.406); atrial flutter (0.265); Abnormality of the skeletal system (0.263); cardiac arrhythmia (0.251)
- **Europe PMC papers**: 2828
- **Why important**: SUN1 is the module member linked to nuclear-envelope organization, nuclear anchorage, cell movement, cortical radial-glia migration, and meiotic telomere attachment. Although it has only one module neighbor, that neighbor is GBA1, connecting nuclear-envelope biology to the module's central lysosomal-metabolic signal. SUN1 also has substantial literature and supplied disease associations involving neurodegenerative and skeletal phenotypes, which are relevant to the bone-marrow and brain tissue pair.
- **Conclusion**: Established evidence supports SUN1 as a nuclear-envelope and cellular-architecture marker within the module. Its connection to GBA1 may indicate coordinated cell-state regulation, but a direct lysosome-to-nuclear-envelope mechanism is not established by the supplied network or interaction databases.

#### ACOT8

- **Related proteins** (co-abundance neighbors): ERGIC2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA thioesterase 8. The protein encoded by this gene is a peroxisomal thioesterase that appears to be involved more in the oxidation of fatty acids rather than in their formation. The encoded protein can bind to the human immunodeficiency virus-1 protein Nef, and mediate Nef-induced down-regulation of CD4 in T-cells. [provided by RefSeq, Oct 2010].
- **Diseases (Open Targets)**: enteritis (0.105); breast carcinoma (0.092); breast cancer (0.076); nonpapillary renal cell carcinoma (0.076); pancreatic ductal adenocarcinoma (0.074)
- **Europe PMC papers**: 385
- **Why important**: ACOT8 is the lipid-metabolism member connected to ERGIC2. Its annotations include peroxisomal thioesterase activity and fatty-acid, acyl-CoA, and bile-acid metabolism, providing a metabolic complement to GBA1-mediated glycolipid processing. It is detected in both tissues and has vesicular localization. Its literature and disease-association evidence are more limited than those of the principal network hub.
- **Conclusion**: Established evidence supports ACOT8 as a lipid and acyl-CoA metabolic component. Its co-abundance with ERGIC2 is compatible with coordinated lipid handling and vesicle biology, but the proposed metabolic-trafficking coupling remains a hypothesis.

#### RPL26L1

- **Related proteins** (co-abundance neighbors): GBA1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein L26 like 1. This gene encodes a protein that shares high sequence similarity with ribosomal protein L26. Alternative splicing results in multiple transcript variants encoding the same protein. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.462); amyotrophic lateral sclerosis (0.079); glycogen storage disease VI (0.072); frontotemporal dementia (0.064); Hyperlipoproteinemia type 1 (0.064)
- **Europe PMC papers**: 194
- **Why important**: RPL26L1 is connected directly to GBA1 and contributes a translation-related interpretation to an otherwise organelle-focused module. Its annotation supports cytoplasmic translation, and it is detected in both tissues with endoplasmic-reticulum and cytosolic localization. It has a smaller literature base and weaker supplied disease evidence than GBA1 or SUN1, but its position may indicate a broader cell-state or biosynthetic component.
- **Conclusion**: Established evidence supports RPL26L1 as a translation-associated member that may reflect general biosynthetic activity. Its placement beside GBA1 does not demonstrate translational control of lysosomal metabolism; that relationship should be treated as a co-abundance hypothesis.

## Module 2

**Tissue pair**: bone_marrow and brain  
**Genes (8)**: ATXN2L, CHAF1A, CTTNBP2NL, GIPC1, LAS1L, RRP15, RRP1B, UCHL5

### Function

The module appears to represent a mixed intracellular maintenance program rather than a narrowly defined tissue-specific pathway. Its most coherent functional signal is ribosome biogenesis and large-subunit precursor maturation, supported by the functions of LAS1L, RRP15, and RRP1B and by the supplementary STRING term (STRING Component Preribosome, large subunit precursor; within-query FDR = 0.0059). CHAF1A adds a chromatin-assembly and DNA-replication dimension, while UCHL5 contributes protein deubiquitination and proteasome-related regulation. GIPC1 and CTTNBP2NL provide possible links to membrane trafficking, the actin cytoskeleton, and transporter regulation. No GO or KEGG term passed global correction, so these functional interpretations are based on individual gene annotations and supplementary STRING evidence, not on globally significant enrichment.

**Cell composition.** The module contains no secreted genes, arguing against a plasma-protein or secreted-factor explanation. Most genes have low tissue specificity, and proteins from nearly all module genes are detected in bone marrow and in most surveyed brain regions. The HPA profile shows frequent cell-type enhancement but little general immune-cell specificity, with selected signals in erythrocyte and megakaryocyte progenitors, dendritic cells, microglia, photoreceptor or spermatogenic cells, and epithelial populations. This pattern is compatible with broadly expressed intracellular machinery combined with cell-composition effects in the sampled tissues. CHAF1A is tissue-enhanced in bone marrow, whereas GIPC1 is tissue-enhanced in esophagus; these findings do not establish a brain-specific program. ATXN2L is detected in bone marrow but not in the surveyed brain samples, which also cautions against treating the module as uniformly expressed in every brain cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The network has a compact, hub-like structure centered on GIPC1, with additional links through CTTNBP2NL. The known STRING relationships are LAS1L with RRP1B and RRP15 with RRP1B, with the latter being the stronger of the two reported interactions. These relationships support a real nucleolar or preribosomal subnetwork involving RRP1B, LAS1L, and RRP15, consistent with (STRING Component Preribosome, large subunit precursor; within-query FDR = 0.0059). The remaining co-abundance links are not supported by high-confidence STRING partners in the fact sheet and may reflect co-regulation, indirect biology, or sample-composition effects. No hu.MAP complex contains at least two module members, so there is no independent hu.MAP complex-level confirmation.

**STRING interactions (score >= 0.7)**: 2 of 28 gene pairs: LAS1L–RRP1B (0.785); RRP15–RRP1B (0.962)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Preribosome, large subunit precursor (FDR = 0.0059, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is not established as a wholly new molecular machine. Part of it recapitulates known ribosome-biogenesis biology, especially the RRP1B–RRP15–LAS1L relationship supported by STRING and gene annotations. The full cross-tissue co-abundance arrangement may nevertheless be a new observation because the fact sheet provides no prior report of this exact module, and most of its pairwise relationships are absent from the listed interaction resources. That absence alone does not demonstrate novelty: co-abundance can arise from shared regulation, cell-type composition, technical covariance, or indirect pathway relationships. The appropriate conclusion is that the integrated module-level pattern is potentially novel but requires replication and perturbational or molecular validation.

**Hypothesis.** Hypothesis: the shared bone-marrow–brain module reflects a conserved intracellular growth, differentiation, or stress state in which ribosome production is coordinated with chromatin assembly, RNA or stress-granule regulation, protein deubiquitination, and receptor or cytoskeletal trafficking. The nucleolar subnetwork may form the mechanistic core, while GIPC1 and CTTNBP2NL may connect that core to cell-surface or cytoskeletal state. In tissue datasets, the observed conservation could also be produced partly by shared or variable cell populations rather than by a single pathway operating identically in bone marrow and brain. This hypothesis predicts coordinated changes in preribosomal maturation, chromatin replication, and proteostasis when the module is perturbed.

### Important genes

#### GIPC1

- **Related proteins** (co-abundance neighbors): RRP1B (0.92), CHAF1A (0.87), ATXN2L (0.87), RRP15 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GIPC PDZ domain containing family member 1. GIPC1 is a scaffolding protein that regulates cell surface receptor expression and trafficking (Lee et al., 2008 [PubMed 18775991]).[supplied by OMIM, Apr 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); oculopharyngodistal myopathy 2 (0.409); oculopharyngodistal myopathy (0.376); smoking initiation (0.205); risk-taking behaviour (0.192)
- **Europe PMC papers**: 653
- **Why important**: GIPC1 is the principal network hub, connecting the nucleolar-associated genes RRP1B and RRP15 with CHAF1A, ATXN2L, and CTTNBP2NL. Its established annotation as a scaffolding protein that regulates cell-surface receptor expression and trafficking, together with links to actin organization, G-protein-coupled receptor signaling, synaptic transmission, and glutamate secretion, makes it a plausible bridge between intracellular co-abundance and tissue or cell-state biology. It also has comparatively substantial literature coverage and disease associations involving neurodegenerative and muscle phenotypes.
- **Conclusion**: Established evidence supports GIPC1 as the network hub and as a trafficking or scaffolding protein. It is not established that GIPC1 physically links the ribosome-biogenesis genes in this module. Its bridging role in the proposed mechanism is therefore a hypothesis.

#### RRP1B

- **Related proteins** (co-abundance neighbors): GIPC1 (0.92), CTTNBP2NL (0.87); STRING partners: LAS1L (0.785), RRP15 (0.962)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim, Mitotic chromosome; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal RNA processing 1B. Enables transcription coactivator activity. Involved in several processes, including cellular response to virus; positive regulation by host of viral transcription; and positive regulation of transcription by RNA polymerase II. Located in chromosome; granular component; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypertensive disorder (0.184); cardiovascular disorder (0.149); response to xenobiotic stimulus (0.111); essential hypertension (0.108); retinitis pigmentosa (0.107)
- **Europe PMC papers**: 387
- **Why important**: RRP1B is a key connector in the known interaction subnetwork: it is linked by STRING to LAS1L and RRP15, and it participates in the supplementary preribosome term (STRING Component Preribosome, large subunit precursor; within-query FDR = 0.0059). Its annotations include rRNA processing, transcriptional regulation, RNA-splicing regulation, and apoptotic regulation. It therefore provides the strongest direct connection between the module's co-abundance structure and a defined nucleolar function.
- **Conclusion**: Established evidence supports RRP1B as a component associated with ribosome biogenesis and as a central member of the known STRING-supported subnetwork. Its position does not prove that it drives the entire module or that it mediates communication between bone marrow and brain.

#### LAS1L

- **Related proteins** (co-abundance neighbors): CTTNBP2NL (0.89); STRING partners: RRP1B (0.785)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LAS1 like ribosome biogenesis factor. Enables RNA binding activity. Predicted to be involved in maturation of 5.8S rRNA and maturation of LSU-rRNA. Located in membrane. Part of MLL1 complex. Implicated in Wilson-Turner syndrome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Wilson-Turner syndrome (0.658); spinal muscular atrophy with respiratory distress type 2 (0.370); hereditary disease (0.296); Global developmental delay (0.259); neurodevelopmental disorder (0.119)
- **Europe PMC papers**: 286
- **Why important**: LAS1L has a direct STRING relationship with RRP1B and is included in the supplementary preribosome term (STRING Component Preribosome, large subunit precursor; within-query FDR = 0.0059). Its established functions in maturation of five-point-eight-S and large-subunit rRNA provide a specific biochemical interpretation for the nucleolar part of the module. Its disease associations include Wilson-Turner syndrome and developmental or neuromuscular phenotypes, giving it potential relevance beyond generic expression covariance.
- **Conclusion**: Established evidence supports LAS1L as a ribosome-biogenesis factor and as part of the known RRP1B-associated interaction neighborhood. Its role as a conserved driver of the whole tissue-pair module remains unproven.

#### CHAF1A

- **Related proteins** (co-abundance neighbors): GIPC1 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromatin assembly factor 1 subunit A. Chromatin assembly factor I (CAF1) is a nuclear complex consisting of p50, p60 (CHAF1B; MIM 601245), and p150 (CHAF1A) subunits that assembles histone octamers onto replicating DNA in vitro (Kaufman et al., 1995 [PubMed 7600578]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: craniofacial microsomia (0.446); neurodegenerative disease (0.441); Abnormality of the skeletal system (0.116); neoplasm (0.105); gastric cancer (0.098)
- **Europe PMC papers**: 845
- **Why important**: CHAF1A contributes a distinct chromatin and cell-proliferation axis: it is a subunit of chromatin assembly factor one and is annotated for nucleosome assembly and replication-dependent chromatin assembly. It is tissue-enhanced in bone marrow and cell-type enhanced in progenitor populations, including erythrocyte and megakaryocyte progenitors. Its network connection to GIPC1 may therefore mark a relationship between proliferative progenitor state and the broader module. It also has substantial literature coverage and disease associations involving craniofacial, skeletal, neurodegenerative, and neoplastic phenotypes.
- **Conclusion**: Established evidence supports CHAF1A in chromatin assembly and progenitor-associated biology. The connection to ribosome biogenesis is an inference from module co-abundance and is not demonstrated as a direct molecular interaction.

#### RRP15

- **Related proteins** (co-abundance neighbors): GIPC1 (0.83); STRING partners: RRP1B (0.962)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal RNA processing 15 homolog. This gene encodes a protein that co-purifies with human nucleoli. A similar protein in budding yeast is a component of pre-60S ribosomal particles, and is required for the early maturation steps of the 60S subunit. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: Alzheimer disease (0.483); Parkinson disease (0.462); neurodegenerative disease (0.462); lysosomal storage disease (0.462); diaphragmatic hernia (0.282)
- **Europe PMC papers**: 239
- **Why important**: RRP15 is a nucleolar protein associated with early maturation of the large ribosomal subunit and is connected by STRING to RRP1B. It independently reinforces the preribosomal interpretation represented by (STRING Component Preribosome, large subunit precursor; within-query FDR = 0.0059). Its disease-oriented associations include Alzheimer disease, Parkinson disease, neurodegenerative disease, and lysosomal storage disease, making it relevant to the brain side of the tissue pair despite the absence of a globally significant GO or KEGG term.
- **Conclusion**: Established evidence supports RRP15 as a large-subunit ribosome-maturation factor and as a known partner of RRP1B. Its disease associations do not establish that this module causes neurological disease, and its broader role in the shared tissue module remains a hypothesis.

## Module 3

**Tissue pair**: bone_marrow and brain  
**Genes (5)**: CWF19L1, DDX56, MYBBP1A, WDR33, ZNF280C

### Function

The module is best interpreted as a broadly expressed nuclear and nucleolar regulatory module, rather than as a confidently assigned pathway. Its genes point toward transcriptional regulation, chromatin and nucleolar functions, RNA processing, pre-mRNA splicing, and mRNA three-prime-end processing. ZNF280C is the central co-abundance hub, linking WDR33, MYBBP1A, DDX56, and CWF19L1 in the module graph. However, no GO or KEGG term passed global correction, so these functional themes are an interpretation of the individual gene annotations and network structure, not a globally significant enrichment claim. STRING provides one high-confidence known relationship, between DDX56 and MYBBP1A, while the remaining co-abundance links should not be treated as established physical interactions.

**Cell composition.** The module is not dominated by secreted or plasma proteins and does not show blood-cell enrichment. All genes have low immune-cell specificity, and the HPA data show no secreted genes. Most genes have low tissue and cell-type specificity, with protein detected in bone marrow and brain for nearly the whole module. This supports a broadly expressed, intracellular, housekeeping-like or core regulatory composition rather than a specialized blood-cell module. The testis-enhanced signal and the association of ZNF280C with differentiating spermatogonia and early primary spermatocytes are not evidence that the shared bone-marrow and brain module is a testis module. They may indicate a cell-state or germ-cell-related regulatory component, but that interpretation requires validation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING contains one high-confidence interaction within the module: DDX56 with MYBBP1A. This relationship is consistent with a shared nucleolar and RNA-related context, but STRING evidence is supplementary and is not a globally corrected enrichment result. No other module pair has a reported high-confidence STRING interaction. No hu.MAP complex contains multiple module members. Thus, the co-abundance graph extends beyond currently catalogued protein interaction or complex evidence. The unconfirmed edges may reflect coordinated regulation, shared cell composition, indirect biology, or technical covariance rather than direct binding.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: DDX56–MYBBP1A (0.838)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is a potentially novel co-abundance pattern, but it cannot be declared a new biological complex or pathway. The absence of a multi-member hu.MAP complex and the limited STRING connectivity mean that most of the observed network structure is not already represented by these resources. That absence does not prove novelty, because interaction databases are incomplete and co-abundance relationships can be indirect. The strongest defensible claim is that this is a cross-tissue co-abundance association with limited prior interaction support, requiring independent replication, cell-composition control, and experimental testing.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of nuclear gene expression and RNA maturation in cells represented in both bone marrow and brain. A possible model is that ZNF280C-associated transcriptional regulation covaries with WDR33-linked mRNA three-prime-end processing, CWF19L1-linked spliceosomal activity, and the nucleolar functions of MYBBP1A and DDX56. The known DDX56--MYBBP1A relationship provides limited support for a nucleolar RNA-processing component, whereas the links from ZNF280C to the other genes are co-abundance observations rather than proven molecular contacts. This hypothesis should be tested by cell-type-resolved expression analysis, perturbation of the candidate regulators, and assays of transcription, RNA processing, and nucleolar organization.

### Important genes

#### ZNF280C

- **Related proteins** (co-abundance neighbors): WDR33 (0.86), MYBBP1A (0.82), DDX56 (0.82), CWF19L1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger protein 280C. This gene encodes a member of the zinc finger domain-containing protein family. This family member contains multiple Cys2-His2(C2H2)-type zinc finger domains, the most common type of zinc finger domain that self-folds to form a beta-beta-alpha structure that binds a zinc ion. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: retinitis pigmentosa (0.109); Digital flexor tenosynovitis (0.101); cone dystrophy (0.093); cone-rod dystrophy (0.090); exudative vitreoretinopathy (0.080)
- **Europe PMC papers**: 79
- **Why important**: ZNF280C is the module's central network hub, connected to every other member. It is localized to the nucleoplasm and fibrillar center of nucleoli, has transcription-regulatory annotations, and is the only gene with tissue-enhanced and cell-type-enhanced HPA patterns. Its disease associations include several retinal disorders, and its literature support is more limited than that of the better-characterized nucleolar genes. Its hub position makes it the leading candidate for coordinating the module, although the network does not establish a direct molecular mechanism.
- **Conclusion**: Established: ZNF280C is a broadly detected nuclear protein with transcription-related annotations and central co-abundance position. Hypothesis: it may act as an upstream regulatory component that helps couple the other module genes across bone marrow and brain.

#### MYBBP1A

- **Related proteins** (co-abundance neighbors): ZNF280C (0.82); STRING partners: DDX56 (0.838)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MYB binding protein 1a. This gene encodes a nucleolar transcriptional regulator that was first identified by its ability to bind specifically to the Myb proto-oncogene protein. The encoded protein is thought to play a role in many cellular processes including response to nucleolar stress, tumor suppression and synthesis of ribosomal DNA. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep…
- **Diseases (Open Targets)**: neurodegenerative disease (0.507); Non-immune hydrops fetalis (0.370); ventricular septal defect (0.245); lysosomal storage disease (0.191); Meniere disease (0.162)
- **Europe PMC papers**: 763
- **Why important**: MYBBP1A is a nucleolar transcriptional regulator with annotations involving chromatin remodeling, transcriptional control, osteoblast differentiation, nucleolar stress, tumor suppression, and ribosomal DNA synthesis. It participates in the only high-confidence within-module STRING interaction, with DDX56. It also has substantial literature support and disease associations involving neurodegenerative disease and developmental or lysosomal conditions. Although it is a peripheral node in this module graph, its functional annotation and known interaction make it an important biological anchor.
- **Conclusion**: Established: MYBBP1A is a well-studied nucleolar and transcription-related regulator and has a known STRING relationship with DDX56. Hypothesis: it may provide a nucleolar regulatory bridge between transcriptional control and RNA maturation in the shared module.

#### DDX56

- **Related proteins** (co-abundance neighbors): ZNF280C (0.82); STRING partners: MYBBP1A (0.838)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 56. This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribut…
- **Diseases (Open Targets)**: metabolic disease (0.246); hyperlipidemia (0.242); neurodegenerative disease (0.157); Hypercholesterolemia (0.151); alcohol drinking (0.131)
- **Europe PMC papers**: 374
- **Why important**: DDX56 is a nucleolar DEAD-box helicase associated with RNA structure remodeling, ribosome or spliceosome assembly, and RNA-related cellular processes. It forms the module's only high-confidence STRING pair with MYBBP1A. Its annotations also include neuron projection development and antiviral-response-related processes, and it has disease associations including neurodegenerative and metabolic disease. Its protein is detected in brain but not bone marrow, which makes the cross-tissue co-abundance signal particularly important to validate.
- **Conclusion**: Established: DDX56 is a nucleolar RNA-associated factor with a known relationship to MYBBP1A. Hypothesis: DDX56 may connect the module to tissue-shared RNA maturation or ribosome-related cellular states, but its bone-marrow representation needs independent confirmation.

#### WDR33

- **Related proteins** (co-abundance neighbors): ZNF280C (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 33. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.515); dengue disease (0.370); smoking initiation (0.292); connective tissue disorder (0.236); arthropathy (0.149)
- **Europe PMC papers**: 508
- **Why important**: WDR33 is connected to the central hub ZNF280C and has annotations for mRNA three-prime-end processing, DNA damage tolerance, and spermatogenesis. Its WD-repeat architecture is compatible with participation in multiprotein regulatory assemblies. It is broadly detected in the relevant tissues and has the strongest literature support among the module genes. Its disease associations include neurodegenerative disease and several other broad disease categories. Its limited graph degree means it is not a network hub here, but its RNA-processing annotation makes it mechanistically informative.
- **Conclusion**: Established: WDR33 is a broadly expressed WD-repeat protein with mRNA three-prime-end-processing annotation and a reported co-abundance link to ZNF280C. Hypothesis: it may represent the RNA maturation arm of the proposed module, without evidence that it directly binds ZNF280C.

#### CWF19L1

- **Related proteins** (co-abundance neighbors): ZNF280C (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CWF19 like cell cycle control factor 1. This gene encodes a member of the CWF19 protein family. Mutations in this gene have been associated with autosomal recessive spinocerebellar ataxia-17 and mild cognitive disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2014].
- **Diseases (Open Targets)**: autosomal recessive spinocerebellar ataxia 17 (0.776); autosomal recessive cerebellar ataxia (0.374); Intellectual disability (0.261); type 2 diabetes mellitus (0.222); pericarditis (0.220)
- **Europe PMC papers**: 176
- **Why important**: CWF19L1 is connected to ZNF280C and is annotated for spliceosomal mRNA splicing. Mutations are associated with autosomal recessive spinocerebellar ataxia and mild cognitive disability, giving it a direct neurological disease relevance for a brain-containing tissue pair. It is detected in both bone marrow and brain, has meaningful literature support, and provides a complementary RNA-processing function to WDR33 and DDX56.
- **Conclusion**: Established: CWF19L1 is a broadly detected spliceosome-associated gene with established ataxia and cognitive-disability associations. Hypothesis: it may contribute to a shared RNA-splicing state represented in both tissues, but the co-abundance data do not establish a causal role.

## Module 4

**Tissue pair**: bone_marrow and brain  
**Genes (6)**: CUX1, CUX1, GCC1, RCC1L, RFC1, TPX2

### Function

The module does not have a securely defined pathway-level function: no GO or KEGG term passed global correction. Its structure is centered on CUX1, with associations to TPX2, RCC1L, RFC1, and GCC1, while the gene annotations collectively point to transcriptional regulation and differentiation, cell-cycle and mitotic-spindle activity, DNA replication and repair, mitochondrial ribosome biology, and Golgi or membrane trafficking. These functions are heterogeneous, so the most defensible interpretation is a shared co-abundance pattern involving nuclear regulation and proliferation-related processes rather than a demonstrated single biochemical pathway. The absence of globally significant enrichment does not invalidate the module.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and all module proteins are detected in brain while nearly all are detected in bone marrow. TPX2 is tissue enhanced in bone marrow and lymphoid tissue and is enriched in erythrocyte progenitors and T-reg cells; CUX1 is associated with neutrophils and non-classical monocytes. The remaining genes are broadly expressed or show limited cell-type specificity, with GCC1 showing group enrichment in several cell types. This pattern is compatible with a broadly expressed cellular program, but the bone-marrow signal could partly reflect proliferating or immune-related cell populations. It does not support interpreting the module as a plasma-protein signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional-enrichment term was reported, and none of the possible within-module gene pairs met the supplied high-confidence STRING interaction threshold. No hu.MAP complex contained multiple module members. Thus, the co-abundance relationships are not corroborated by a known high-confidence physical interaction network or a shared hu.MAP complex. The module may represent coordinated expression across related cellular states, indirect regulation, shared cell composition, or technical and biological co-variation rather than a stable protein complex.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a newly discovered molecular complex or pathway. Its novelty as a co-abundance pattern is plausible because the supplied analyses identify a conserved bone-marrow–brain module that is not recovered as a STRING interaction cluster or hu.MAP complex, but absence from those resources does not prove novelty. The genes themselves are not uncharacterized: CUX1, TPX2, RFC1, RCC1L, and GCC1 each have prior functional annotations and literature. The appropriate conclusion is that the cross-tissue co-abundance configuration may be novel or understudied, while the underlying gene functions are established to varying degrees.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of a broadly expressed nuclear and membrane-trafficking program that becomes especially visible when bone-marrow and brain samples share proliferative, progenitor-like, or immune-associated cellular variation. CUX1 may provide a regulatory hub linking transcriptional state to TPX2-dependent mitotic organization, RFC1-dependent replication and repair, RCC1L-associated mitochondrial ribosome processes, and GCC1-associated Golgi trafficking. This is a mechanistic hypothesis only; the lack of globally significant GO or KEGG enrichment, STRING support, and hu.MAP complexes means that direct regulatory or physical coupling has not been established by the supplied evidence.

### Important genes

#### CUX1

- **Related proteins** (co-abundance neighbors): CUX1 (0.94), TPX2 (0.86), RCC1L (0.84), GCC1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Golgi apparatus; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cut like homeobox 1. The protein encoded by this gene is a member of the homeodomain family of DNA binding proteins. It may regulate gene expression, morphogenesis, and differentiation and it may also play a role in the cell cycle progession. Several alternatively spliced transcript variants encoding different isoforms have been identified.[provided by RefSeq, Feb 2011].
- **Diseases (Open Targets)**: global developmental delay with or without impaired intellectual development (0.754); cancer (0.588); myelodysplastic syndrome (0.536); hereditary disease (0.519); acute lymphoblastic leukemia (0.509)
- **Europe PMC papers**: 3914
- **Why important**: CUX1 is the central network gene, connecting the other module members in the supplied co-abundance graph. It encodes a homeodomain DNA-binding protein associated with transcriptional regulation, morphogenesis, differentiation, dendrite morphogenesis, and cell-cycle progression. It is detected in both tissues and has immune-cell and neutrophil associations in HPA. Its disease associations include developmental delay, cancer, myelodysplastic syndrome, and acute lymphoblastic leukemia, and it has substantial literature coverage.
- **Conclusion**: Established evidence supports CUX1 as the leading network and regulatory candidate in this module, with relevance to differentiation and hematologic disease. It is reasonable to hypothesize that CUX1 contributes to the shared expression pattern, but the co-abundance data do not establish that it regulates the other module genes.

#### TPX2

- **Related proteins** (co-abundance neighbors): CUX1 (0.86), CUX1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TPX2 microtubule nucleation factor. Enables importin-alpha family protein binding activity and protein kinase binding activity. Involved in activation of protein kinase activity; microtubule cytoskeleton organization; and negative regulation of microtubule depolymerization. Located in intercellular bridge; mitotic spindle; and nucleoplasm. Colocalizes with spindle pole. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.124); neoplasm (0.117); breast carcinoma (0.116); non-small cell lung carcinoma (0.112); breast cancer (0.110)
- **Europe PMC papers**: 4216
- **Why important**: TPX2 is strongly connected to the module hub and has a well-defined role in microtubule nucleation, mitotic-spindle assembly, spindle organization, and activation of protein kinase activity. HPA shows tissue enhancement in bone marrow and lymphoid tissue, as well as enrichment in progenitor and proliferative cell types including erythrocyte progenitors. Its extensive literature and cancer associations make it a biologically informative marker of proliferative state.
- **Conclusion**: Established evidence supports TPX2 as the strongest indicator that the module may capture cell-cycle or progenitor-cell variation, particularly in bone marrow. Its participation in a brain–bone-marrow module could reflect shared proliferative or cellular-composition signals, but a direct TPX2 interaction with the other module genes is not demonstrated.

#### RFC1

- **Related proteins** (co-abundance neighbors): CUX1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: replication factor C subunit 1. This gene encodes the large subunit of replication factor C, a five subunit DNA polymerase accessory protein, which is a DNA-dependent ATPase required for eukaryotic DNA replication and repair. The large subunit acts as an activator of DNA polymerases, binds to the 3' end of primers, and promotes coordinated synthesis of both strands. It may also have a role in telomere stability. Alternatively sp…
- **Diseases (Open Targets)**: cerebellar ataxia with neuropathy and bilateral vestibular areflexia syndrome (0.700); Parkinson disease (0.354); late-onset Parkinson disease (0.333); asthma (0.327); polyneuropathy (0.271)
- **Europe PMC papers**: 2323
- **Why important**: RFC1 is connected to CUX1 and encodes the large subunit of replication factor C, a DNA-dependent ATPase required for DNA replication, DNA repair, primer handling, and telomere maintenance. It is detected in both tissues, is broadly expressed by HPA, and has substantial literature coverage. Its disease associations include cerebellar ataxia with neuropathy and bilateral vestibular areflexia, Parkinson disease, asthma, and polyneuropathy.
- **Conclusion**: Established evidence supports RFC1 as a replication and genome-maintenance component that could mark proliferative or repair-related cellular states. Its role in this module is most plausibly interpretive rather than proof of a shared physical complex, because STRING and hu.MAP provide no corroborating relationship.

#### RCC1L

- **Related proteins** (co-abundance neighbors): CUX1 (0.85), CUX1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RCC1 like. This gene encodes a protein containing regulator of chromosome condensation 1-like repeats. The encoded protein may function as a guanine nucleotide exchange factor. This gene is located in a region of chromosome 7 that is deleted in Williams-Beuren syndrome, a multisystem developmental disorder. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013].
- **Diseases (Open Targets)**: obstructive sleep apnea syndrome (0.345); respiratory system disorder (0.254); hypertensive disorder (0.073); type 2 diabetes mellitus (0.070); essential hypertension (0.060)
- **Europe PMC papers**: 73
- **Why important**: RCC1L is connected to CUX1 and is annotated with mitochondrial fusion and mitochondrial ribosome assembly functions. It is detected in brain but not bone marrow by the supplied HPA immunohistochemistry summary, while its transcript-level tissue and cell-type specificity are low. Although it has less literature coverage than the leading hub and mitotic genes, it adds a mitochondrial and translational dimension to the module and has associations with respiratory, metabolic, and hypertensive disorders.
- **Conclusion**: Established evidence supports RCC1L as a mitochondrial-biology candidate within the module. Its selective protein detection in brain makes it relevant to the cross-tissue interpretation, but the evidence is insufficient to claim that mitochondrial ribosome assembly is a module-level function or that RCC1L mechanistically links to CUX1.

#### GCC1

- **Related proteins** (co-abundance neighbors): CUX1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Golgi apparatus; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GRIP and coiled-coil domain containing 1. The protein encoded by this gene is a peripheral membrane protein. It is sensitive to brefeldin A. This encoded protein contains a GRIP domain which is thought to be used in targeting. It may play a role in the organization of trans-Golgi network subcompartment involved with membrane transport. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.367); type 2 diabetes mellitus (0.323); duodenal ulcer (0.216); peptic ulcer disease (0.114); gestational diabetes (0.108)
- **Europe PMC papers**: 281
- **Why important**: GCC1 is connected to CUX1 and encodes a peripheral membrane protein with a GRIP domain that may participate in trans-Golgi network organization and membrane transport. It is detected in both tissues and shows group enrichment in cardiomyocytes, epicardial cells, and germ-cell populations rather than a specific bone-marrow or brain signature. Its literature volume is more limited than that of CUX1, TPX2, or RFC1, making it useful as a less-established but functionally distinct module member.
- **Conclusion**: Established evidence supports GCC1 as a Golgi and membrane-trafficking candidate that broadens the module beyond nuclear and proliferative biology. Its presence may reflect general cellular organization or coordinated abundance across cell states, but any direct role in the conserved bone-marrow–brain module remains hypothetical.

## Module 5

**Tissue pair**: bone_marrow and brain  
**Genes (11)**: NCAPH, EZH2, RAE1, RBM15, TAF15, SNW1, SPATS2L, GTF2A2, MELTF, UBE2S, UHRF1

### Function

No GO/KEGG term passed global correction, so the module does not have a statistically established pathway annotation from those analyses. Its gene content nevertheless points toward a nuclear gene-regulatory program involving chromatin repression and remodeling, transcription initiation, RNA processing and export, ubiquitin-dependent regulation, and chromosome organization. The supplementary STRING signal supports a transcription-related theme (STRING RCTM Gene expression (Transcription); within-query FDR = 0.0468), but it is not global enrichment evidence. The co-abundance structure is therefore most consistent with coordinated regulation of gene expression in proliferative or differentiating cells rather than with a single demonstrated biochemical pathway.

**Cell composition.** This is not primarily a plasma or secreted-protein module: nearly all members are intracellular or nuclear, and only MELTF is annotated as having an intracellular and membrane secretome profile. The HPA evidence strongly favors cell-state and tissue-composition explanations. Several genes are enhanced in bone marrow, lymphoid tissue, erythrocyte progenitors, megakaryocyte progenitors, monocyte progenitors, or T-reg cells, while many are also enhanced in spermatogenic cell types. Most genes have cell-type-enhanced rather than broadly uniform expression. Detection in brain for several genes shows that the module can be present there, but it does not establish a brain-specific mechanism. The shared bone-marrow and brain signal may therefore reflect conserved proliferative, progenitor, or other shared cellular states, with possible contribution from blood-cell composition in samples.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports two high-confidence pairwise relationships within the module: EZH2 with UHRF1, and RAE1 with RBM15. The supplementary STRING transcription term contains UBE2S, EZH2, RAE1, GTF2A2, SNW1, TAF15, and UHRF1 (STRING RCTM Gene expression (Transcription); within-query FDR = 0.0468). These links are consistent with the module's transcriptional and nuclear character, but they cover only part of the co-abundance structure. No hu.MAP complex contains multiple module members. Thus, the module is not explained by one already catalogued protein complex; rather, it combines a small set of known relationships with broader coordinated expression.

**STRING interactions (score >= 0.7)**: 2 of 55 gene pairs: EZH2–UHRF1 (0.81); RAE1–RBM15 (0.714)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Gene expression (Transcription) (FDR = 0.0468, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be called a wholly new molecular mechanism. EZH2-UHRF1 and RAE1-RBM15 are already supported by STRING, and the individual genes have established roles in chromatin regulation, transcription, RNA handling, ubiquitination, chromosome organization, and cell differentiation. However, the specific conserved co-abundance module linking these genes across bone marrow and brain is not directly established by the supplied STRING or hu.MAP evidence. Its novelty is therefore best described as a potentially new cross-tissue expression relationship or systems-level grouping, requiring replication, cell-composition control, and perturbation experiments before claiming a new biological pathway.

**Hypothesis.** Hypothesis: the module represents a conserved nuclear regulatory state associated with proliferating or differentiating progenitor-like cells. EZH2 and UHRF1 could coordinate chromatin repression and epigenetic maintenance, while UBE2S could contribute proteostatic and cell-cycle-linked regulation. GTF2A2, TAF15, and SNW1 could support transcriptional initiation, transcriptional regulation, and RNA processing; RAE1 and RBM15 could connect RNA export or RNA regulation with differentiation-related programs. MELTF may mark a cell-surface or iron-related component associated with the cellular state rather than serve as a core nuclear complex member. This model is a hypothesis because global GO/KEGG enrichment is absent, hu.MAP provides no multi-member complex, and most within-module edges are co-abundance relationships rather than demonstrated physical interactions.

### Important genes

#### EZH2

- **Related proteins** (co-abundance neighbors): NCAPH (0.85), UHRF1 (0.83), SPATS2L (0.81), RBM15 (0.81); STRING partners: UHRF1 (0.81)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: enhancer of zeste 2 polycomb repressive complex 2 subunit. This gene encodes a member of the Polycomb-group (PcG) family. PcG family members form multimeric protein complexes, which are involved in maintaining the transcriptional repressive state of genes over successive cell generations. This protein associates with the embryonic ectoderm development protein, the VAV1 oncoprotein, and the X-linked nuclear protein. This protein may play a role in the hema…
- **Diseases (Open Targets)**: Weaver syndrome (0.837); diffuse large B-cell lymphoma (0.615); neurodegenerative disease (0.525); follicular lymphoma (0.517); viral infectious disease (0.486)
- **Europe PMC papers**: 43112
- **Why important**: EZH2 is one of the strongest network-connected genes and links to UHRF1, SPATS2L, RBM15, and NCAPH. It is a Polycomb-associated chromatin regulator with roles in transcriptional repression, chromatin organization, remodeling, and cell proliferation. HPA places it in bone marrow, lymphoid tissue, erythrocyte progenitors, megakaryocyte progenitors, monocyte progenitors, neutrophil progenitors, and T-reg cells. It is also the most literature-rich member of the module and has disease associations including Weaver syndrome and lymphoid malignancies. Its inclusion in the supplementary transcription signal (STRING RCTM Gene expression (Transcription); within-query FDR = 0.0468) reinforces its regulatory relevance.
- **Conclusion**: Established evidence supports EZH2 as a central chromatin and transcriptional regulator with strong relevance to hematopoietic cell states. Its network position makes it a plausible organizing gene, but the module does not prove that EZH2 drives the cross-tissue co-abundance pattern.

#### UHRF1

- **Related proteins** (co-abundance neighbors): EZH2 (0.83), UBE2S (0.81); STRING partners: EZH2 (0.81)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin like with PHD and ring finger domains 1. This gene encodes a member of a subfamily of RING-finger type E3 ubiquitin ligases. The protein binds to specific DNA sequences, and recruits a histone deacetylase to regulate gene expression. Its expression peaks at late G1 phase and continues during G2 and M phases of the cell cycle. It plays a major role in the G1/S transition by regulating topoisomerase IIalpha and retinoblastoma gene expressi…
- **Diseases (Open Targets)**: hypertensive disorder (0.450); type 2 diabetes mellitus (0.424); immunodeficiency-centromeric instability-facial anomalies syndrome (0.371); neurodegenerative disease (0.367); coronary artery disorder (0.362)
- **Europe PMC papers**: 4824
- **Why important**: UHRF1 connects EZH2 and UBE2S and occupies a nucleoplasmic location. It has established functions in epigenetic gene regulation, ubiquitination, DNA damage response, homologous-recombination repair, and cell-cycle control. HPA associates it with bone marrow and lymphoid tissue and with differentiating spermatogonia, erythrocyte progenitors, megakaryocyte progenitors, monocyte progenitors, and plasmacytoid dendritic cells. Its physical STRING relationship with EZH2 and membership in the supplementary transcription signal (STRING RCTM Gene expression (Transcription); within-query FDR = 0.0468) provide direct support for a chromatin-regulatory substructure.
- **Conclusion**: Established evidence supports UHRF1 as a bridge between chromatin regulation, ubiquitin-linked control, and progenitor-cell biology. It is a strong candidate for a mechanistic component of the module, although the co-abundance data alone cannot establish directionality or cooperation with EZH2.

#### RAE1

- **Related proteins** (co-abundance neighbors): MELTF (0.84); STRING partners: RBM15 (0.714)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribonucleic acid export 1. Mutations in the Schizosaccharomyces pombe Rae1 and Saccharomyces cerevisiae Gle2 genes have been shown to result in accumulation of poly(A)-containing mRNA in the nucleus, suggesting that the encoded proteins are involved in RNA export. The protein encoded by this gene is a homolog of yeast Rae1. It contains four WD40 motifs, and has been shown to localize to distinct foci in the nucleoplasm, to …
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); COVID-19 (0.370); Histiocytosis (0.370)
- **Europe PMC papers**: 1837
- **Why important**: RAE1 links the module to RNA export, nucleocytoplasmic transport, nuclear organization, and mitotic spindle regulation. It is connected to MELTF in the co-abundance network and has a STRING relationship with RBM15. HPA shows enrichment in testis and spermatogenic cell types, while its established molecular functions concern RNA export and nuclear transport. It also contributes to the supplementary transcription-related signal (STRING RCTM Gene expression (Transcription); within-query FDR = 0.0468).
- **Conclusion**: Established evidence supports RAE1 as an RNA-transport and nuclear-organization component. Its relationship with RBM15 makes it important for a possible RNA-regulatory branch of the module, but whether that branch is active in brain or bone marrow cells remains a hypothesis.

#### RBM15

- **Related proteins** (co-abundance neighbors): EZH2 (0.81); STRING partners: RAE1 (0.714)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 15. Members of the SPEN (Split-end) family of proteins, including RBM15, have repressor function in several signaling pathways and may bind to RNA through interaction with spliceosome components (Hiriart et al., 2005 [PubMed 16129689]).[supplied by OMIM, Feb 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); lung adenocarcinoma (0.219); esophageal squamous cell carcinoma (0.209); osteosarcoma (0.209); hepatocellular carcinoma (0.206)
- **Europe PMC papers**: 3897
- **Why important**: RBM15 is bone-marrow-enriched, is detected in both bone marrow and brain by HPA, and connects to EZH2 in the module while also having a STRING relationship with RAE1. Its known functions include alternative mRNA splicing, RNA methylation, thrombopoietin-mediated signaling, and regulation of myeloid and megakaryocyte differentiation. These annotations directly connect the module to hematopoietic differentiation and RNA regulation.
- **Conclusion**: Established evidence supports RBM15 as a plausible link between RNA processing and hematopoietic differentiation. Its position at the intersection of the EZH2 and RAE1-related relationships makes it mechanistically important, but the module does not demonstrate a physical RBM15-EZH2 complex or a causal role.

#### TAF15

- **Related proteins** (co-abundance neighbors): MELTF (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TATA-box binding protein associated factor 15. This gene encodes a member of the TET family of RNA-binding proteins. The encoded protein plays a role in RNA polymerase II gene transcription as a component of a distinct subset of multi-subunit transcription initiation factor TFIID complexes. Translocations involving this gene play a role in acute leukemia and extraskeletal myxoid chondrosarcoma, and mutations in this gene may play a role in amy…
- **Diseases (Open Targets)**: HIV infectious disease (0.578); extraskeletal myxoid chondrosarcoma (0.403); pleural mesothelioma (0.195); amyotrophic lateral sclerosis (0.183); urinary bladder cancer (0.166)
- **Europe PMC papers**: 2376
- **Why important**: TAF15 is connected to MELTF in the module and contributes to the supplementary transcription signal (STRING RCTM Gene expression (Transcription); within-query FDR = 0.0468). It is a nucleoplasmic RNA-binding protein involved in RNA polymerase transcription, transcriptional regulation, and mRNA stabilization. HPA detects it in both bone marrow and brain and identifies enhanced expression in astrocytes, choroid plexus epithelial cells, microglia, and oligodendrocytes. Its disease associations include acute leukemia-related translocations, extraskeletal myxoid chondrosarcoma, and amyotrophic lateral sclerosis.
- **Conclusion**: Established evidence supports TAF15 as a transcriptional and RNA-stability regulator with relevance in both neural and hematopoietic contexts. Its presence supports a shared gene-expression program, but its single module edge and lack of a hu.MAP complex make a central structural role uncertain.

## Module 6

**Tissue pair**: bone_marrow and brain  
**Genes (5)**: DCP1A, GFM2, MRRF, TRIM24, ZNF326

### Function

The module does not have a statistically supported GO or KEGG enrichment after correction across all module-term tests, so no pathway-level function can be assigned from enrichment. Its gene annotations instead suggest a mixed regulatory and gene-expression maintenance program. TRIM24 is a chromatin-associated transcriptional regulator and ubiquitination-related protein; ZNF326 is linked to transcriptional elongation and RNA splicing; DCP1A participates in messenger RNA decapping and decay; and GFM2 with MRRF supports mitochondrial ribosome recycling and mitochondrial translation. The network is therefore more consistent with coordinated regulation of gene expression, RNA processing and mitochondrial protein synthesis than with a single established biological pathway. This interpretation remains inferential because the module lacks globally significant GO or KEGG terms and most connections are not supported by the supplied high-confidence STRING or hu.MAP evidence.

**Cell composition.** The module is not composed of plasma or secreted proteins: the supplied HPA summary reports no secreted genes. It is also not blood-cell enriched, because every gene has low immune-cell specificity and no enriched blood-cell category is reported. Most genes show low tissue specificity, with protein detection in bone marrow and brain, which is compatible with broadly expressed intracellular proteins. There are nevertheless selected cell-type or tissue associations: TRIM24 is associated with adrenal cortex cells and thymocytes, ZNF326 with retina and cone and rod photoreceptors, and MRRF with early and late spermatids. These annotations suggest a broadly distributed intracellular module with some specialized-cell associations, rather than a blood-derived or secreted module. Protein detection in both tissues supports detectability but does not establish a shared cell-type origin.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only supplied high-confidence STRING relationship is the direct GFM2–MRRF interaction. This is biologically coherent because both proteins participate in mitochondrial ribosome recycling and mitochondrial translation. TRIM24, ZNF326 and DCP1A have no listed STRING partners at the stated threshold. No hu.MAP complex contains at least two module members. Thus, one compact and functionally plausible mitochondrial pair is already known, while the remaining co-abundance edges are not independently supported by the supplied interaction or complex resources. The network may therefore combine a genuine mitochondrial submodule with expression-level coordination involving nuclear transcriptional regulation and messenger RNA decay.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: GFM2–MRRF (0.998)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be called a wholly new molecular complex. The GFM2–MRRF relationship is already known in STRING, and the individual functions of all genes are established. However, the conserved co-abundance pattern across bone marrow and brain appears potentially novel as a cross-tissue regulatory association because no hu.MAP complex covers multiple module members and most module edges lack high-confidence STRING support. This is suggestive rather than proof of novelty: co-abundance can arise from shared expression programs, cell composition, technical effects or indirect regulation. Demonstrating novelty would require replication in independent cohorts and comparison with existing co-expression studies.

**Hypothesis.** Hypothesis: the module represents a shared intracellular gene-expression maintenance program in bone marrow and brain. TRIM24 may coordinate chromatin and transcriptional state, ZNF326 may connect transcriptional elongation with RNA splicing, DCP1A may influence messenger RNA turnover, and the GFM2–MRRF pair may preserve mitochondrial translation and respiratory capacity. A common cellular demand for transcriptional, post-transcriptional and mitochondrial quality control could generate the observed co-abundance pattern without requiring direct physical interaction among all members. This model predicts that module activity will track cellular metabolic and RNA-processing state, while the GFM2–MRRF relationship should be the most directly mechanistic part of the module.

### Important genes

#### TRIM24

- **Related proteins** (co-abundance neighbors): ZNF326 (0.84), GFM2 (0.82), MRRF (0.81), DCP1A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tripartite motif containing 24. The protein encoded by this gene mediates transcriptional control by interaction with the activation function 2 (AF2) region of several nuclear receptors, including the estrogen, retinoic acid, and vitamin D3 receptors. The protein localizes to nuclear bodies and is thought to associate with chromatin and heterochromatin-associated factors. The protein is a member of the tripartite motif (TRIM) fa…
- **Diseases (Open Targets)**: cancer (0.609); neurodegenerative disease (0.540); leukemia (0.380); lung adenocarcinoma (0.374); acute lymphoblastic leukemia (0.372)
- **Europe PMC papers**: 2114
- **Why important**: TRIM24 is the central network node, connected to every other module member and having the greatest weighted connectivity in the supplied graph. Its established functions in chromatin organization, RNA polymerase transcriptional regulation, nuclear receptor interaction and protein ubiquitination make it a plausible coordinator of the module's nuclear regulatory component. It also has substantial literature volume and disease associations spanning cancer, leukemia and neurodegenerative disease.
- **Conclusion**: Established evidence supports TRIM24 as the leading network-level candidate and a chromatin and transcriptional regulator. It is a plausible module coordinator, but the co-abundance network does not establish that TRIM24 directly regulates the other four genes in this module.

#### GFM2

- **Related proteins** (co-abundance neighbors): TRIM24 (0.82); STRING partners: MRRF (0.998)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GTP dependent ribosome recycling factor mitochondrial 2. Eukaryotes contain two protein translational systems, one in the cytoplasm and one in the mitochondria. Mitochondrial translation is crucial for maintaining mitochondrial function and mutations in this system lead to a breakdown in the respiratory chain-oxidative phosphorylation system and to impaired maintenance of mitochondrial DNA. This gene encodes one of the mitochondrial translation elongati…
- **Diseases (Open Targets)**: combined oxidative phosphorylation deficiency (0.727); mitochondrial disease (0.456); Leigh syndrome (0.216); hereditary disease (0.193); Alzheimer disease (0.191)
- **Europe PMC papers**: 185
- **Why important**: GFM2 is one half of the only supplied high-confidence STRING pair and is annotated as a mitochondrial translation and ribosome-recycling factor. Its mitochondrial localization and associations with combined oxidative phosphorylation deficiency, mitochondrial disease, Leigh syndrome and Alzheimer disease make it important for interpreting the module's possible metabolic component.
- **Conclusion**: Established evidence supports GFM2 as a mitochondrial translation factor and as part of a known relationship with MRRF. Its participation in the broader module is a hypothesis based on co-abundance and network placement, not proof of a direct interaction with TRIM24.

#### MRRF

- **Related proteins** (co-abundance neighbors): TRIM24 (0.81); STRING partners: GFM2 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules, Cytokinetic bridge; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial ribosome recycling factor. This gene encodes a ribosome recycling factor, which is a component of the mitochondrial translational machinery. The encoded protein, along with mitochondrial elongation factor 2, functions in ribosomal recycling at the termination of mitochondrial translation by mediating the disassembly of ribosomes from messenger RNA. A pseudogene of this gene has been identified on chromosome X. [provided by …
- **Diseases (Open Targets)**: neurodegenerative disease (0.415); ocular hypotension (0.173); myoepithelial tumor (0.111); deficiency anemia (0.101); squamous cell lung carcinoma (0.038)
- **Europe PMC papers**: 170
- **Why important**: MRRF forms the complementary member of the known GFM2–MRRF interaction and is directly involved in mitochondrial ribosome recycling and mitochondrial translational termination. Its shared detection in bone marrow and brain and its disease associations involving neurodegenerative disease and deficiency anemia make it relevant to a cross-tissue mitochondrial maintenance interpretation.
- **Conclusion**: Established evidence supports MRRF as a mitochondrial ribosome-recycling factor that works with GFM2. The module-level conclusion that this mitochondrial pair is coordinated with nuclear RNA and chromatin regulators remains a hypothesis.

#### ZNF326

- **Related proteins** (co-abundance neighbors): TRIM24 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger protein 326. Enables RNA polymerase II complex binding activity. Involved in regulation of DNA-templated transcription, elongation and regulation of RNA splicing. Located in nucleoplasm. Part of DBIRD complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: ocular hypotension (0.227); insomnia (0.222); adolescent idiopathic scoliosis (0.207); juvenile dermatomyositis (0.205); major depressive disorder (0.205)
- **Europe PMC papers**: 258
- **Why important**: ZNF326 is selectively associated with retina and photoreceptor cell types in the supplied HPA evidence, is detected in both tissues, and is annotated for transcriptional elongation and RNA splicing. It connects the broadly expressed module to a specialized neural or retinal expression context and is a component of the DBIRD complex according to the supplied annotation.
- **Conclusion**: Established evidence supports ZNF326 as a nuclear transcription and RNA-splicing regulator with retinal and photoreceptor associations. Its role as a bridge between TRIM24 and the mitochondrial pair is not established by the available interaction resources and should be treated as a hypothesis.

#### DCP1A

- **Related proteins** (co-abundance neighbors): TRIM24 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytoplasmic bodies; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: decapping mRNA 1A. Decapping is a key step in general and regulated mRNA decay. The protein encoded by this gene is a decapping enzyme. This protein and another decapping enzyme form a decapping complex, which interacts with the nonsense-mediated decay factor hUpf1 and may be recruited to mRNAs containing premature termination codons. This protein also participates in the TGF-beta signaling pathway. Alternative spli…
- **Diseases (Open Targets)**: ocular hypotension (0.218); Abnormality of the skeletal system (0.217); injury (0.198); alopecia (0.194); adverse effect (0.187)
- **Europe PMC papers**: 1172
- **Why important**: DCP1A is connected to TRIM24 in the module and has substantial literature volume. Its established role in messenger RNA decapping, deadenylation-dependent and independent RNA decay, stress-granule localization and TGF-beta pathway participation provides a post-transcriptional component complementary to the chromatin and mitochondrial annotations.
- **Conclusion**: Established evidence supports DCP1A as an mRNA-decapping and RNA-decay factor. Its inclusion supports a possible RNA homeostasis interpretation, but no supplied evidence demonstrates a direct physical or regulatory relationship between DCP1A and TRIM24.

## Module 7

**Tissue pair**: bone_marrow and brain  
**Genes (5)**: EIF3C, MAD2L1, MED18, SRP68, SRP72

### Function

The strongest interpretation is a conserved module centered on translation and protein targeting to the endoplasmic reticulum. The primary globally corrected evidence is concentrated on SRP68 and SRP72: signal recognition particle binding (GO:MF signal recognition particle binding; q_global = 0.0125), seven-S RNA binding (GO:MF 7S RNA binding; q_global = 0.0216), the signal recognition particle and ER-targeting compartment (GO:CC signal recognition particle, endoplasmic reticulum targeting; q_global = 0.0321) (GO:CC signal recognition particle; q_global = 0.0321), and ribosome binding (GO:MF ribosome binding; q_global = 0.0362). EIF3C extends this interpretation toward cytoplasmic translation initiation and ribosome-associated activity, while the co-abundance links to MED18 and MAD2L1 suggest connections to transcriptional regulation and proliferative cell biology rather than a single narrowly specialized pathway. The absence of additional primary terms for MED18 and MAD2L1 does not invalidate their membership or the module.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and all have low immune-cell specificity, arguing against a module that is simply a blood-cell marker. Protein detection is present in both bone marrow and brain for most genes with available data. Cell-type-enhanced annotations span neuronal, glial, epithelial, trophoblast, and progenitor populations, while MAD2L1 is tissue-enhanced in bone marrow and lymphoid tissue and is associated with erythrocyte progenitors. Thus, the shared signal is more consistent with broadly used intracellular machinery, potentially modulated by shared proliferative or cellular-composition features, than with a dedicated secreted or immune-cell program.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF signal recognition particle binding | 0.0125 | SRP68, SRP72 |
| GO:MF 7S RNA binding | 0.0216 | SRP68, SRP72 |
| GO:CC signal recognition particle, endoplasmic reticulum targeting | 0.0321 | SRP68, SRP72 |
| GO:CC signal recognition particle | 0.0321 | SRP68, SRP72 |
| GO:MF ribosome binding | 0.0362 | EIF3C, SRP68, SRP72 |

### STRING and hu.MAP

The clearest known relationship is the very strong STRING association between SRP68 and SRP72 (7 supplementary STRING terms; within-query FDR 0.0088–0.04), consistent with the established SRP68-SRP72 heterodimer and with the globally significant SRP annotations (5 globally significant GO/KEGG terms, q_global 0.0125–0.0362; see the table). STRING also places EIF3C, SRP68, and SRP72 in a broader ribonucleoprotein-complex-binding signal (STRING Function Ribonucleoprotein complex binding; within-query FDR = 0.0428), but this is supplementary evidence rather than global enrichment evidence. No other module pair reaches the stated STRING interaction threshold, and no hu.MAP complex contains at least two module members. Therefore, the network contains one well-established molecular core surrounded by co-abundance links that are not independently supported here as stable physical complexes.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: SRP68–SRP72 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Signal recognition particle (FDR = 0.0088, 2 genes); KEGG Protein export (FDR = 0.021, 2 genes); Component Signal recognition particle, endoplasmic reticulum targeting (FDR = 0.0211, 2 genes); COMPARTMENTS Signal recognition particle, endoplasmic reticulum targeting (FDR = 0.023, 2 genes); Function Signal recognition particle binding (FDR = 0.0304, 2 genes); Function 7S RNA binding (FDR = 0.0304, 2 genes); NetworkNeighborAL Signal recognition particle (FDR = 0.04, 2 genes); Function Ribonucleoprotein complex binding (FDR = 0.0428, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears to be a potentially interesting tissue-pair co-abundance observation, but it should not be called a newly discovered molecular complex. The SRP68-SRP72 relationship and their functions are already established, and the SRP interpretation is independently supported by GO and STRING. The possible novelty lies instead in the coordinated abundance of this known SRP core with EIF3C, MED18, and MAD2L1 across bone marrow and brain. Because the remaining relationships lack STRING support and hu.MAP provides no multi-member complex, the result is best described as a novel or hypothesis-generating co-abundance configuration rather than proof of a new physical interaction or pathway.

**Hypothesis.** Hypothesis: the module reflects coordinated demand for protein synthesis and ER targeting in cells present in both bone marrow and brain. SRP68 and SRP72 may form the core of an SRP-dependent cotranslational targeting signal, EIF3C may couple that signal to translation initiation, and MED18 and MAD2L1 may capture transcriptional and cell-cycle states that influence the abundance of this biosynthetic machinery. The tissue-pair conservation could therefore arise from shared intracellular requirements combined with cell-state composition, rather than from a tissue-specific secretory program. This hypothesis requires validation with expression covariates, cell-type deconvolution, perturbation, and direct protein-complex assays.

### Important genes

#### SRP68

- **Related proteins** (co-abundance neighbors): MED18 (0.84), SRP72 (0.80); STRING partners: SRP72 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal recognition particle 68. This gene encodes a subunit of the signal recognition particle (SRP). The SRP is a ribonucleoprotein complex that transports secreted and membrane proteins to the endoplasmic reticulum for processing. The complex includes a 7S RNA and six protein subunits. The encoded protein is the 68kDa component of the SRP, and forms a heterodimer with the 72kDa subunit that is required for SRP function. Altern…
- **Diseases (Open Targets)**: neurodegenerative disease (0.347); neutropenia, severe congenital, 10, autosomal recessive (0.333); COVID-19 (0.155); metabolic syndrome (0.074); atrial septal defect (0.073)
- **Europe PMC papers**: 440
- **Why important**: SRP68 is a central node tied to both MED18 and SRP72. It is present in every primary globally corrected term (5 globally significant GO/KEGG terms, q_global 0.0125–0.0362; see the table) and every listed STRING enrichment (8 supplementary STRING terms; within-query FDR 0.0088–0.0428). Its established function is as a signal recognition particle subunit that forms a heterodimer with SRP72 and supports cotranslational targeting of secretory and membrane proteins to the ER. It is detected by HPA in both bone marrow and brain, while showing low tissue and immune-cell specificity. Its disease associations include neurodegenerative disease and severe congenital neutropenia, and its literature volume indicates substantial prior study.
- **Conclusion**: Established evidence supports SRP68 as a core functional member of the module and as one half of the known SRP68-SRP72 molecular pair. The hypothesis that its co-abundance with EIF3C, MED18, and MAD2L1 reports coordinated regulation of translational capacity across the two tissues is plausible but not established by the supplied data.

#### SRP72

- **Related proteins** (co-abundance neighbors): EIF3C (0.83), SRP68 (0.80); STRING partners: SRP68 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal recognition particle 72. This gene encodes the 72 kDa subunit of the signal recognition particle (SRP), a ribonucleoprotein complex that mediates the targeting of secretory proteins to the endoplasmic reticulum (ER). The SRP complex consists of a 7S RNA and 6 protein subunits: SRP9, SRP14, SRP19, SRP54, SRP68, and SRP72, that are bound to the 7S RNA as monomers or heterodimers. SRP has at least 3 distinct functions that c…
- **Diseases (Open Targets)**: autosomal dominant aplasia and myelodysplasia (0.641); neurodegenerative disease (0.416); intracranial subdural hematoma (0.280); type 2 diabetes mellitus (0.044); oropharynx cancer (0.032)
- **Europe PMC papers**: 696
- **Why important**: SRP72 is a central node tied to EIF3C and SRP68 and is present in every primary globally corrected term (5 globally significant GO/KEGG terms, q_global 0.0125–0.0362; see the table) and every listed STRING enrichment (8 supplementary STRING terms; within-query FDR 0.0088–0.0428). It is an established SRP subunit involved in signal recognition, translational arrest, and ER targeting, and it forms the known functional pair with SRP68. HPA detects it in both bone marrow and brain with low tissue and immune-cell specificity. Its disease associations include autosomal dominant aplasia and myelodysplasia and neurodegenerative disease, and it has substantial literature support.
- **Conclusion**: Established evidence identifies SRP72 as a core SRP component and a strong biological anchor for the module. The association with EIF3C may indicate coordination between translation initiation and ER targeting, but the supplied network does not establish a direct physical EIF3C-SRP72 interaction.

#### EIF3C

- **Related proteins** (co-abundance neighbors): SRP72 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C connects directly to SRP72 and is the third gene in the primary ribosome-binding term (GO:MF ribosome binding; q_global = 0.0362). Its established function is as a subunit of the eukaryotic translation initiation factor complex, with roles in ribosome binding, translation initiation, and positive regulation of translation. HPA detects it in both tissues and reports cell-type enhancement across neuronal and glial populations. It has the largest literature volume among the selected translation-related genes and has reported associations with neoplastic and developmental phenotypes.
- **Conclusion**: Established evidence supports EIF3C as a translation-initiation component that broadens the module beyond the SRP pair. The hypothesis that EIF3C couples cytoplasmic initiation to SRP-dependent ER targeting is mechanistically reasonable, but the module data alone cannot distinguish direct coupling from correlated translational demand.

#### MED18

- **Related proteins** (co-abundance neighbors): SRP68 (0.84), MAD2L1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mediator complex subunit 18. MED18 is a component of the Mediator complex, which is a coactivator for DNA-binding factors that activate transcription via RNA polymerase II (Sato et al., 2003 [PubMed 12584197]).[supplied by OMIM, Oct 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); gastroparesis (0.205); exostosis (0.055); corneal ulcer (0.049); gastric cancer (0.037)
- **Europe PMC papers**: 488
- **Why important**: MED18 is a network bridge between SRP68 and MAD2L1, giving it a potentially important position at the interface between the SRP-centered signal and a cell-cycle-associated signal. Its established function is as a Mediator complex subunit involved in RNA polymerase II transcriptional regulation, transcription initiation, and elongation. HPA reports low tissue specificity and detects the protein in brain but not bone marrow. It has reported links to neurodegenerative disease and other disorders, with a meaningful literature base.
- **Conclusion**: Established evidence supports MED18 as a general transcriptional coactivator, but it has no primary GO/KEGG annotation and no listed STRING or hu.MAP support within this module. Its connection to SRP biology is therefore a co-abundance observation and a hypothesis about coordinated transcriptional and translational state, not an established molecular interaction.

#### MAD2L1

- **Related proteins** (co-abundance neighbors): MED18 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitotic arrest deficient 2 like 1. MAD2L1 is a component of the mitotic spindle assembly checkpoint that prevents the onset of anaphase until all chromosomes are properly aligned at the metaphase plate.  MAD2L1 is related to the MAD2L2 gene located on chromosome 1.  A MAD2 pseudogene has been mapped to chromosome 14. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: alcohol drinking (0.433); cornea transplantation (0.342); connective tissue disorder (0.314); hypotensive disorder (0.294); Tietze syndrome (0.294)
- **Europe PMC papers**: 3856
- **Why important**: MAD2L1 is connected to MED18 and is the only gene with tissue-enhanced HPA annotation in bone marrow and lymphoid tissue. Its established function is as a spindle-assembly-checkpoint component that delays anaphase until chromosomes are properly aligned and regulates mitotic progression. Its association with erythrocyte progenitors is relevant to bone-marrow biology. It has the largest literature volume in the module and reported associations with connective-tissue and other clinical phenotypes, despite lacking primary enrichment-term support and listed STRING or hu.MAP support here.
- **Conclusion**: Established evidence supports MAD2L1 as a marker of cell-cycle and proliferative state, particularly relevant to the bone-marrow context. Its inclusion may indicate that the module captures shared cellular state or composition rather than a single biochemical complex. Any mechanistic link from spindle-checkpoint activity to SRP-dependent protein targeting remains a hypothesis.

## Module 8

**Tissue pair**: bone_marrow and brain  
**Genes (5)**: MLLT1, INTS8, NCSTN, OGFOD1, ORC5

### Function

The module does not support a single statistically established GO or KEGG function: no globally significant GO/KEGG term passed global correction, and there are no supplementary supplementary STRING terms. Its gene-level annotations instead point to a mostly nuclear, broadly expressed cellular program involving RNA processing and transcriptional control through INTS8 and MLLT1, DNA-replication initiation through ORC5, and translational termination, protein hydroxylation, and stress-granule biology through OGFOD1. NCSTN contributes a distinct membrane-proteolysis function through the gamma-secretase complex. The network is therefore more consistent with a weakly connected collection of broadly expressed regulatory and maintenance genes than with a coherent tissue-specific pathway. The absence of enrichment does not invalidate the module, but it limits functional interpretation.

**Cell composition.** The module is not composed of plasma proteins or secreted proteins: the HPA evidence reports no secreted genes. All module genes have low tissue specificity and low immune-cell specificity, with no recurrent enriched blood-cell category. Protein detection is present in brain for every member and in bone marrow for most members. HPA single-cell annotations span several unrelated cell types, including trophoblast populations, retinal horizontal cells, neutrophils, epicardial cells, and oocytes. This pattern favors broadly expressed cellular genes, with possible effects from shared cell states or ubiquitous cellular programs, rather than a module representing a specialized blood-cell or brain-cell population.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

At the stated STRING confidence threshold, none of the possible module gene pairs has a supported STRING interaction, and STRING functional enrichment is absent. No hu.MAP complex contains multiple module members. Nevertheless, the genes have established biological relationships to complexes or molecular systems outside the detected module edges: INTS8 is a subunit of the Integrator complex; NCSTN is an integral component of gamma-secretase; MLLT1 is a super elongation complex subunit; and ORC5 is a subunit of the origin recognition complex. OGFOD1 has annotated roles in hydroxylation, translational termination, and stress-granule assembly. Thus, the module does not recapitulate a known physical complex in STRING or hu.MAP, and its co-abundance links should not be treated as evidence of direct protein binding.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel co-abundance association rather than a newly discovered molecular complex or pathway. The absence of STRING and hu.MAP support means that the particular cross-tissue co-abundance pattern is not explained by the referenced interaction resources, but that absence alone cannot establish biological novelty. The lack of globally significant GO or KEGG enrichment and the mixture of functions further argue against claiming discovery of a new unified pathway. A defensible novelty claim would require replication in independent cohorts, preservation of the gene-level correlations, and testing against relevant expression, cell-composition, and technical covariates.

**Hypothesis.** Hypothesis: the shared bone-marrow–brain module reflects a broadly expressed nuclear and cellular-maintenance program that becomes co-abundant across these tissues because of common demands for RNA processing, transcriptional regulation, replication-related control, translational quality control, and stress adaptation. INTS8 may provide the central co-abundance anchor, while the other genes represent partially independent regulatory processes that converge at the level of cellular state rather than direct physical interaction. NCSTN may reflect a linked membrane-proteolysis or cell-state component. This hypothesis is not established by the enrichment or interaction evidence and should be tested by replication, cell-resolved analysis, and perturbation or longitudinal data.

### Important genes

#### INTS8

- **Related proteins** (co-abundance neighbors): NCSTN (0.86), MLLT1 (0.84), OGFOD1 (0.80), ORC5 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrator complex subunit 8. This gene encodes a subunit of the Integrator complex which is involved in the cleavage of small nuclear RNAs U1 and U2 within the nucleus. The encoded protein associates with RNA polymerase II and is recruited to the U1 and U2 small nuclear RNA genes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012].
- **Diseases (Open Targets)**: neurodevelopmental disorder with cerebellar hypoplasia and spasticity (0.616); response to stress (0.282); splenic disorder (0.212); pulmonary edema (0.204); hyperaldosteronism (0.195)
- **Europe PMC papers**: 259
- **Why important**: INTS8 is the central network gene, connected to every other module member and having the strongest weighted connectivity in the supplied subgraph. Its established functions in Integrator-complex biology, small nuclear RNA processing, RNA polymerase II transcriptional regulation, chromatin localization, and transcription-initiation surveillance make it the strongest candidate for representing the module's nuclear regulatory axis. Its disease evidence includes a neurodevelopmental disorder with cerebellar hypoplasia and spasticity, and it has a substantial literature base.
- **Conclusion**: Established evidence supports INTS8 as the network anchor and as a regulator of nuclear RNA and transcriptional processes. It is plausible, but unproven, that variation in INTS8-centered cellular regulation contributes to the shared co-abundance pattern.

#### NCSTN

- **Related proteins** (co-abundance neighbors): INTS8 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nicastrin. This gene encodes a type I transmembrane glycoprotein that is an integral component of the multimeric gamma-secretase complex. The encoded protein cleaves integral membrane proteins, including Notch receptors and beta-amyloid precursor protein, and may be a stabilizing cofactor required for gamma-secretase complex assembly. The cleavage of beta-amyloid precursor protein yields amyloid beta peptide…
- **Diseases (Open Targets)**: acne inversa, familial, 1 (0.724); neurodegenerative disease (0.525); desmoid tumor (0.503); Alzheimer disease (0.406); hidradenitis suppurativa (0.389)
- **Europe PMC papers**: 2357
- **Why important**: NCSTN is the only module member annotated as a core component of gamma-secretase, linking the module to membrane-protein ectodomain proteolysis, Notch processing, and amyloid precursor-protein processing. It is directly connected to INTS8 in the module, although it has no STRING or hu.MAP support within the supplied evidence. NCSTN has the largest literature volume among the listed genes and disease associations involving neurodegeneration, Alzheimer disease, acne inversa, and hidradenitis suppurativa.
- **Conclusion**: Established evidence supports NCSTN as a gamma-secretase component with relevance to neural and inflammatory disease biology. Its connection to the nuclear genes is a co-abundance observation, not evidence that gamma-secretase physically interacts with the module. A shared cell-state or regulatory explanation remains hypothetical.

#### MLLT1

- **Related proteins** (co-abundance neighbors): INTS8 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MLLT1 super elongation complex subunit. Predicted to be involved in regulation of transcription, DNA-templated. Predicted to act upstream of or within negative regulation of protein kinase activity. Located in cytosol; fibrillar center; and nucleoplasm. Part of transcription elongation factor complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.501); acute myeloid leukemia (0.395); acute lymphoblastic leukemia (0.381); B-cell acute lymphoblastic leukemia (0.370); lysosomal storage disease (0.352)
- **Europe PMC papers**: 956
- **Why important**: MLLT1 is connected to INTS8 and is annotated as a super elongation complex subunit involved in transcriptional regulation. Its disease associations include neurodegenerative disease and acute leukemias, which are relevant to the brain and bone-marrow tissue context. It also has a substantial literature base, making it a useful bridge between transcriptional control and disease-relevant cellular states.
- **Conclusion**: Established evidence supports MLLT1 as a transcription-elongation regulator with disease relevance in neural and hematologic contexts. Its participation in this shared module may indicate coordinated transcriptional state, but the available data do not establish a direct mechanistic link to INTS8 or the other genes.

#### OGFOD1

- **Related proteins** (co-abundance neighbors): INTS8 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 2-oxoglutarate and iron dependent oxygenase domain containing 1. Enables peptidyl-proline 3-dioxygenase activity. Involved in several processes, including peptidyl-proline hydroxylation; regulation of translational termination; and stress granule assembly. Located in cytoplasmic stress granule; cytosol; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.513); retinitis pigmentosa 74 (0.118); Bardet-Biedl syndrome 2 (0.118); breast carcinoma (0.099); breast cancer (0.093)
- **Europe PMC papers**: 200
- **Why important**: OGFOD1 is connected to INTS8 and contributes a distinct set of functions involving peptidyl-proline hydroxylation, translational termination, stress-granule assembly, and cell-population proliferation. Its annotations are relevant to cellular stress and translational control, while its disease evidence includes neurodegenerative disease and a retinal disorder. The gene has a smaller literature base than the best-studied members, so it may be particularly informative for testing the module rather than assuming its role.
- **Conclusion**: Established evidence supports OGFOD1 as an oxygenase-domain protein associated with translation and stress responses. Its inclusion is consistent with a cellular-maintenance hypothesis, but whether it is a driver, a responder, or a correlated passenger in the module is unresolved.

#### ORC5

- **Related proteins** (co-abundance neighbors): INTS8 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: origin recognition complex subunit 5. The origin recognition complex (ORC) is a highly conserved six subunit protein complex essential for the initiation of the DNA replication in eukaryotic cells. Studies in yeast demonstrated that ORC binds specifically to origins of replication and serves as a platform for the assembly of additional initiation factors such as Cdc6 and Mcm proteins. The protein encoded by this gene is a subunit of t…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); response to antihypertensive drug (0.263); heart failure (0.263); schizophrenia (0.241); arthropathy (0.103)
- **Europe PMC papers**: 614
- **Why important**: ORC5 is connected to INTS8 and is a subunit of the origin recognition complex, which is essential for DNA-replication initiation. Its disease associations include neurodegenerative disease, schizophrenia, heart failure, and response to antihypertensive drug. The gene has a substantial literature base and provides the module with a DNA-replication and cell-cycle-related component distinct from the RNA-processing functions of INTS8 and MLLT1.
- **Conclusion**: Established evidence supports ORC5 as a replication-initiation factor. Its co-abundance with the other genes may reflect shared cellular proliferation, repair, or maintenance states, but the supplied data do not demonstrate that the module is a replication program or that ORC5 mechanistically organizes the module.

## Module 9

**Tissue pair**: bone_marrow and brain  
**Genes (5)**: SHMT2, HSD17B10, ALDH18A1, PHB2, PRDX3

### Function

The module is most strongly associated with mitochondrial amino-acid metabolism. The primary evidence is the global enrichment of proteinogenic amino-acid metabolic process (GO:BP proteinogenic amino acid metabolic process; q_global = 0.0445) and L-amino-acid metabolic process (GO:BP L-amino acid metabolic process; q_global = 0.0488), driven by ALDH18A1, HSD17B10, and SHMT2. The individual functions support a broader mitochondrial metabolic interpretation: SHMT2 contributes to serine, glycine, and one-carbon metabolism; ALDH18A1 supports glutamate-dependent proline, ornithine, and arginine biosynthesis; HSD17B10 contributes to amino-acid, fatty-acid, steroid, and mitochondrial RNA-processing functions. STRING independently supports a mitochondrial context (STRING Keyword Mitochondrion; within-query FDR = 0.0187). PRDX3 adds mitochondrial antioxidant activity, while PHB2 supports mitochondrial organization and mitophagy. Thus, the most defensible interpretation is coordinated mitochondrial metabolic and stress-maintenance activity rather than a narrowly defined single pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: every gene is annotated as non-secreted, and all module proteins were detected in both bone marrow and brain. The genes have low immune-cell specificity, with no enriched blood-cell category, so the module is not readily explained by a blood-cell-specific signature. Several genes are broadly expressed, while SHMT2 and ALDH18A1 show tissue enhancement in liver and salivary gland respectively. Cell-type enhancement is present across the module, including hepatocytes, esophageal epithelial populations, trophoblast populations, and salivary acinar cells. These observations are compatible with a conserved cellular mitochondrial program shared across tissues, although sample composition or shared cell states could still contribute. The data do not support interpreting this module primarily as a circulating, secreted, or blood-cell module.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP proteinogenic amino acid metabolic process | 0.0445 | ALDH18A1, HSD17B10, SHMT2 |
| GO:BP L-amino acid metabolic process | 0.0488 | ALDH18A1, HSD17B10, SHMT2 |

### STRING and hu.MAP

The strongest directly supported external relationship is the STRING association between ALDH18A1 and SHMT2, and both genes participate in the globally significant amino-acid terms (GO:BP proteinogenic amino acid metabolic process; q_global = 0.0445) and (GO:BP L-amino acid metabolic process; q_global = 0.0488). STRING also places the complete module in a mitochondrial keyword context (STRING Keyword Mitochondrion; within-query FDR = 0.0187), but this is supplementary evidence rather than globally corrected enrichment. No other module pair has a high-confidence STRING interaction in the supplied results, and no hu.MAP complex contains multiple module members. Therefore, the co-abundance structure extends beyond currently captured physical-interaction or curated-complex evidence. The network may reflect coordinated pathway activity, shared mitochondrial regulation, or correlated cellular demand rather than a single stable protein complex.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: ALDH18A1–SHMT2 (0.804)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Mitochondrion (FDR = 0.0187, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel cross-tissue co-abundance module, but the supplied evidence is insufficient to claim a completely new biological pathway. Its potentially distinctive feature is the coordinated association of mitochondrial amino-acid metabolism, redox protection, lipid-related mitochondrial activity, and mitochondrial organization across bone marrow and brain. The limited STRING connectivity and absence of a multi-member hu.MAP complex argue against simply identifying a well-established canonical complex. However, absence from STRING or hu.MAP alone does not establish novelty, because co-abundance relationships can represent regulation, metabolic coupling, tissue composition, or condition-dependent interactions. A stronger novelty claim would require comparison with published co-expression modules, independent cohorts, and perturbation or biochemical validation.

**Hypothesis.** Hypothesis: this module represents a conserved mitochondrial resource-management program that couples amino-acid flux with redox control and organelle quality maintenance in bone marrow and brain. SHMT2 and ALDH18A1 may provide linked metabolic inputs, HSD17B10 may connect amino-acid-related activity with broader mitochondrial fatty-acid, steroid, and RNA-processing functions, while PRDX3 and PHB2 may help maintain mitochondrial redox balance, membrane organization, and quality control. The observed co-abundance could therefore arise when cells increase mitochondrial biosynthetic capacity and protection together. This is a mechanistic hypothesis, not a demonstrated physical complex or causal pathway.

### Important genes

#### SHMT2

- **Related proteins** (co-abundance neighbors): ALDH18A1 (0.82), HSD17B10 (0.80); STRING partners: ALDH18A1 (0.804)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine hydroxymethyltransferase 2. This gene encodes the mitochondrial form of a pyridoxal phosphate-dependent enzyme that catalyzes the reversible reaction of serine and tetrahydrofolate to glycine and 5,10-methylene tetrahydrofolate. The encoded product is primarily responsible for glycine synthesis. The activity of the encoded protein has been suggested to be the primary source of intracellular glycine. The gene which encodes th…
- **Diseases (Open Targets)**: neurodevelopmental disorder with cardiomyopathy, spasticity, and brain abnormalities (0.771); microcephaly (0.370); polymicrogyria (0.370); neurodevelopmental disorder (0.336); hereditary disease (0.192)
- **Europe PMC papers**: 2579
- **Why important**: SHMT2 is a central network participant, is directly present in both globally significant GO terms (GO:BP proteinogenic amino acid metabolic process; q_global = 0.0445) and (GO:BP L-amino acid metabolic process; q_global = 0.0488), and has the strongest direct STRING-supported relationship in the module through ALDH18A1. Its mitochondrial serine-to-glycine and one-carbon functions provide a plausible metabolic bridge linking amino-acid metabolism to biosynthetic demand. Its disease associations include neurodevelopmental phenotypes with brain abnormalities, and its substantial literature supports an established biological role.
- **Conclusion**: Established evidence supports SHMT2 as a core mitochondrial amino-acid and one-carbon metabolism gene in this module. It is a leading candidate for the metabolic anchor of the module. It is not established that SHMT2 causally organizes the entire cross-tissue co-abundance pattern.

#### ALDH18A1

- **Related proteins** (co-abundance neighbors): SHMT2 (0.82); STRING partners: SHMT2 (0.804)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 18 family member A1. This gene is a member of the aldehyde dehydrogenase family and encodes a bifunctional ATP- and NADPH-dependent mitochondrial enzyme with both gamma-glutamyl kinase and gamma-glutamyl phosphate reductase activities. The encoded protein catalyzes the reduction of glutamate to delta1-pyrroline-5-carboxylate, a critical step in the de novo biosynthesis of proline, ornithine and arginine. Mutations in …
- **Diseases (Open Targets)**: ALDH18A1-related de Barsy syndrome (0.832); cutis laxa, autosomal dominant 3 (0.816); autosomal recessive complex spastic paraplegia type 9B (0.814); de Barsy syndrome (0.731); autosomal dominant spastic paraplegia type 9 (0.706)
- **Europe PMC papers**: 1168
- **Why important**: ALDH18A1 is directly represented in both primary GO terms (GO:BP proteinogenic amino acid metabolic process; q_global = 0.0445) and (GO:BP L-amino acid metabolic process; q_global = 0.0488) and has the module's clearest STRING-supported partner, SHMT2. Its mitochondrial bifunctional enzyme activity links glutamate utilization with proline, ornithine, and arginine biosynthesis, giving it a complementary role to SHMT2 within amino-acid metabolism. It has well-established associations with de Barsy syndrome, cutis laxa, and spastic paraplegia phenotypes, together with substantial literature.
- **Conclusion**: Established evidence supports ALDH18A1 as a key amino-acid biosynthetic component and as the best-supported direct interaction partner of SHMT2. Its peripheral network position does not diminish its pathway importance. A causal role in coordinating the whole module remains a hypothesis.

#### HSD17B10

- **Related proteins** (co-abundance neighbors): PRDX3 (0.80), SHMT2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydroxysteroid 17-beta dehydrogenase 10. This gene encodes 3-hydroxyacyl-CoA dehydrogenase type II, a member of the short-chain dehydrogenase/reductase superfamily. The gene product is a mitochondrial protein that catalyzes the oxidation of a wide variety of fatty acids and steroids, and is a subunit of mitochondrial ribonuclease P, which is involved in tRNA maturation. The protein has been implicated in the development of Alzheimer dise…
- **Diseases (Open Targets)**: HSD10 mitochondrial disease (0.829); HSD10 disease, atypical type (0.703); neurodegenerative disease (0.555); mitochondrial disease (0.373); HSD10 disease, neonatal type (0.370)
- **Europe PMC papers**: 1064
- **Why important**: HSD17B10 is a network-central member and contributes to both primary amino-acid metabolic terms (GO:BP proteinogenic amino acid metabolic process; q_global = 0.0445) and (GO:BP L-amino acid metabolic process; q_global = 0.0488). Its mitochondrial enzyme activity spans isoleucine catabolism, fatty-acid and steroid metabolism, and it also participates in mitochondrial RNA processing. The gene has strong disease relevance through HSD10 mitochondrial disease and neurodegenerative disease associations, making it particularly important for interpreting a module shared by brain and bone marrow.
- **Conclusion**: Established evidence supports HSD17B10 as a mitochondrial metabolic and RNA-processing gene that broadens the module beyond amino-acid biosynthesis. Its presence is consistent with a general mitochondrial function rather than proof of a specific disease mechanism in this module.

#### PRDX3

- **Related proteins** (co-abundance neighbors): PHB2 (0.82), HSD17B10 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Mitochondria; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peroxiredoxin 3. This gene encodes a mitochondrial protein with antioxidant function. The protein is similar to the C22 subunit of Salmonella typhimurium alkylhydroperoxide reductase, and it can rescue bacterial resistance to alkylhydroperoxide in E. coli that lack the C22 subunit. The human and mouse genes are highly conserved, and they map to the regions syntenic between mouse and human chromosomes. Sequence com…
- **Diseases (Open Targets)**: spinocerebellar ataxia, autosomal recessive 32 (0.653); corneal dystrophy, punctiform and polychromatic pre-descemet (0.571); autosomal recessive cerebellar ataxia (0.268); neurodegenerative disease (0.257); hereditary disease (0.191)
- **Europe PMC papers**: 2613
- **Why important**: PRDX3 is a network-central member connected to HSD17B10 and PHB2, and it is included in the supplementary mitochondrial STRING term (STRING Keyword Mitochondrion; within-query FDR = 0.0187). Its established mitochondrial antioxidant function provides a redox-protection component that complements the metabolic enzymes. It has associations with cerebellar ataxia and neurodegenerative disease and has substantial literature, including evidence related to oxidative stress and myeloid differentiation.
- **Conclusion**: Established evidence supports PRDX3 as the module's mitochondrial redox-protection component. Its co-abundance with metabolic and organelle-maintenance genes supports coordinated mitochondrial stress management, but does not prove that oxidative stress drives the module.

#### PHB2

- **Related proteins** (co-abundance neighbors): PRDX3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prohibitin 2. Enables several functions, including protein C-terminus binding activity; protein N-terminus binding activity; and protein dimerization activity. Involved in several processes, including defense response to virus; positive regulation of cell cycle phase transition; and regulation of transcription, DNA-templated. Located in several cellular components, including cell surface; mitochondrial membrane…
- **Diseases (Open Targets)**: breast cancer (0.101); breast carcinoma (0.101); neoplasm (0.100); non-small cell lung carcinoma (0.096); colorectal carcinoma (0.085)
- **Europe PMC papers**: 2714
- **Why important**: PHB2 is connected to PRDX3 and is included in the supplementary mitochondrial STRING term (STRING Keyword Mitochondrion; within-query FDR = 0.0187). Its established roles include mitochondrial membrane-associated prohibitin-complex functions, mitophagy, mitochondrial organization, and regulation of cellular processes. It has the largest literature volume among the module genes, although its listed disease associations are less specific than those of several metabolic genes.
- **Conclusion**: Established evidence supports PHB2 as an organelle-organization and mitochondrial-quality-control component. Its position at the edge of the co-abundance subgraph makes it a plausible functional extender of the module, but not evidence that the module is a prohibitin complex, especially because hu.MAP reports no multi-member complex.

## Module 10

**Tissue pair**: bone_marrow and brain  
**Genes (5)**: MICALL1, MTHFS, NKRF, PHACTR4, PHF23

### Function

This is a heterogeneous intracellular regulatory module rather than a clearly established canonical pathway. Its genes collectively implicate membrane trafficking and actin organization through MICALL1 and PHACTR4, transcriptional repression through NKRF, one-carbon folate metabolism through MTHFS, and regulation of autophagy and protein ubiquitination through PHF23. No GO or KEGG term passed global correction, so these annotations support biological interpretation only as gene-level evidence and do not establish enrichment. The co-abundance structure may therefore represent a shared regulatory or cellular-state program rather than a single defined molecular complex.

**Cell composition.** The module contains no secreted genes and is not predominantly composed of plasma proteins. Most genes have low tissue specificity, while all are cell-type enhanced in the HPA evidence. The strongest recurring single-cell associations involve esophageal epithelial cells and trophoblast populations, with MTHFS also associated with hepatocytes, megakaryocytes, syncytiotrophoblasts, and neutrophils. Blood-cell specificity is generally low, although MTHFS is immune-cell enhanced and neutrophil associated. Protein detection in bone marrow and brain is present for most genes, but this does not demonstrate brain- or marrow-specific function. The shared module could partly reflect broadly expressed intracellular programs or shared cellular composition rather than a tissue-specific pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and no hu.MAP complex contains multiple module members. Thus, the observed co-abundance links are not supported here as established physical protein interactions or as membership in a known multiprotein complex. The absence of STRING and hu.MAP support favors a co-expression or shared-regulation interpretation, while not ruling out indirect, context-dependent, transient, or incompletely curated relationships.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module is plausibly a novel co-abundance observation, because its internal relationships are absent from the supplied high-confidence STRING and hu.MAP results and because no globally significant GO or KEGG signal defines it as a known pathway. However, it cannot be called a new biological mechanism solely from database absence. The genes themselves have prior functional annotations, disease associations, and literature, so the defensible novelty claim is the shared bone-marrow–brain co-abundance pattern and its possible coordination, not discovery of the individual gene functions.

**Hypothesis.** Hypothesis: this module reflects a shared intracellular state in selected marrow and brain-associated cells in which membrane remodeling and endocytic trafficking are coordinated with transcriptional restraint, folate-dependent metabolic capacity, and control of autophagy or protein turnover. MICALL1 and PHACTR4 may represent the membrane and actin-regulatory arm, NKRF and PHF23 the nuclear regulatory arm, and MTHFS a metabolic or cell-composition-linked arm. This model is provisional: the lack of globally significant enrichment, STRING interactions, and hu.MAP complexes means that direct molecular coupling remains to be tested experimentally.

### Important genes

#### MICALL1

- **Related proteins** (co-abundance neighbors): PHACTR4 (0.85), MTHFS (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cell Junctions, Centriolar satellite, Cytosol; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MICAL like 1. Enables identical protein binding activity; phosphatidic acid binding activity; and small GTPase binding activity. Involved in several processes, including plasma membrane tubulation; protein localization to endosome; and slow endocytic recycling. Located in late endosome and recycling endosome membrane. Is extrinsic component of membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: obesity disorder (0.099); Alzheimer disease (0.038); COVID-19 (0.032); severe acute respiratory syndrome (0.032); Epiretinal membrane (0.027)
- **Europe PMC papers**: 165
- **Why important**: MICALL1 is a central connector in the observed co-abundance subgraph, linking PHACTR4 and MTHFS. Its established annotations involve phosphatidic-acid binding, small-GTPase binding, plasma-membrane tubulation, endocytosis, endosomal targeting, actin organization, and neuron projection development. It is detected at the protein level in both relevant tissues and has disease associations including Alzheimer disease and obesity disorder. Its literature is smaller than that of several other module genes, which makes its role in this module especially informative but less firmly established.
- **Conclusion**: Established evidence supports MICALL1 as a membrane-trafficking and cytoskeletal regulator. Its position and annotations make it a plausible organizing gene for the module, but a direct functional link to MTHFS or PHACTR4 is a hypothesis rather than demonstrated interaction.

#### PHACTR4

- **Related proteins** (co-abundance neighbors): MICALL1 (0.85), NKRF (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphatase and actin regulator 4. This gene encodes a member of the phosphatase and actin regulator (PHACTR) family. Other PHACTR family members have been shown to inhibit protein phosphatase 1 (PP1) activity, and the homolog of this gene in the mouse has been shown to interact with actin and PP1. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: uterine corpus leiomyoma (0.409); substance-related disorder (0.218); type 2 diabetes mellitus (0.198); familial long QT syndrome (0.115); Brugada syndrome (0.110)
- **Europe PMC papers**: 308
- **Why important**: PHACTR4 is another central connector, positioned between MICALL1 and NKRF. It belongs to the phosphatase and actin regulator family, with annotations involving actin organization, Rho signaling, cell migration, and developmental processes. Its protein is detected in bone marrow and brain, and it has a comparatively substantial literature and disease-association record, including cardiac rhythm disorders, type two diabetes mellitus, and uterine corpus leiomyoma.
- **Conclusion**: Established evidence supports PHACTR4 as a candidate link between actin or Rho-regulated cell organization and nuclear or transcriptional regulation. Its bridging role in this module is supported by network position, but the shared tissue pattern does not prove that it drives the co-abundance relationship.

#### NKRF

- **Related proteins** (co-abundance neighbors): PHACTR4 (0.83), PHF23 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NFKB repressing factor. This gene encodes a transcriptional repressor that interacts with specific negative regulatory elements to mediate transcriptional repression of certain nuclear factor kappa B responsive genes. The protein localizes predominantly to the nucleolus with a small fraction found in the nucleoplasm and cytoplasm. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Mar 2010].
- **Diseases (Open Targets)**: chronic obstructive pulmonary disease (0.078); Alzheimer disease (0.078); myocardial infarction (0.074); hydrops fetalis (0.070); aortic stenosis (0.067)
- **Europe PMC papers**: 570
- **Why important**: NKRF is a central connector linking PHACTR4 and PHF23 and has the largest literature base among the module genes in the supplied evidence. It encodes a nucleolar and nucleoplasmic transcriptional repressor that regulates selected nuclear factor kappa B responsive genes and broader RNA polymerase II transcription. It is associated in the supplied disease-resource evidence with Alzheimer disease, chronic obstructive pulmonary disease, myocardial infarction, hydrops fetalis, and aortic stenosis.
- **Conclusion**: Established evidence supports NKRF as a transcriptional repression and inflammatory-response regulator. It is a plausible nuclear coordinator of the module, but no supplied evidence establishes a direct connection between NKRF and the membrane, metabolic, or autophagy-related genes.

#### MTHFS

- **Related proteins** (co-abundance neighbors): MICALL1 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methenyltetrahydrofolate synthetase. The protein encoded by this gene is an enzyme that catalyzes the conversion of 5-formyltetrahydrofolate to 5,10-methenyltetrahydrofolate, a precursor of reduced folates involved in 1-carbon metabolism. An increased activity of the encoded protein can result in an increased folate turnover rate and folate depletion. Three transcript variants encoding two different isoforms have been found for this …
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, epilepsy, and hypomyelination (0.715); neurodegenerative disease (0.361); Alzheimer disease (0.346); lysosomal storage disease (0.338); Parkinson disease (0.295)
- **Europe PMC papers**: 406
- **Why important**: MTHFS provides the module's most specific metabolic function and connects to MICALL1 in the observed subgraph. It catalyzes a step in folate and tetrahydrofolate interconversion and one-carbon metabolism. HPA evidence identifies liver enrichment, associations with hepatocytes, megakaryocytes, syncytiotrophoblasts, and neutrophils, and immune-cell enhancement. It has a substantial literature and disease associations involving neurodevelopmental disease, neurodegeneration, Alzheimer disease, lysosomal storage disease, and Parkinson disease.
- **Conclusion**: Established evidence supports MTHFS as a folate-metabolism enzyme and as a possible marker of cell composition or metabolic state. Its presence may connect cellular metabolism to the module, but the co-abundance relationship with MICALL1 is not a demonstrated biochemical interaction.

#### PHF23

- **Related proteins** (co-abundance neighbors): NKRF (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PHD finger protein 23. Predicted to enable metal ion binding activity. Involved in negative regulation of autophagosome assembly; negative regulation of autophagosome maturation; and positive regulation of protein ubiquitination. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.082); lung cancer (0.075); lung carcinoma (0.075); neoplasm (0.075); leukemia (0.033)
- **Europe PMC papers**: 230
- **Why important**: PHF23 is the terminal nuclear component connected to NKRF and contributes a distinct protein-quality and autophagy-related interpretation. Its annotations include positive regulation of protein ubiquitination and negative regulation of autophagosome assembly and maturation. It is detected in bone marrow and brain, is enhanced in esophageal apical cells and syncytiotrophoblasts, and has reported associations with lung cancer, non-small cell lung carcinoma, neoplasm, and leukemia. Its literature is intermediate within this module.
- **Conclusion**: Established evidence supports PHF23 as a nuclear regulator of ubiquitination and autophagy-related processes. Its link to NKRF suggests a possible transcriptional or protein-turnover arm of the module, but that connection remains an inferred hypothesis because no STRING or hu.MAP relationship is supplied.
