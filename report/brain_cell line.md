# Conserved co-abundance modules: brain and cell line

## Module 0

**Tissue pair**: brain and cell line  
**Genes (46)**: PPP2R5D, AGFG2, PRMT5, ANKRD46, ARHGEF9, ASAP2, PHYKPL, ATG5, CFAP20, GPS1, DPP3, DST, GFM1, EXOC1, TBRG4, FBLN2, GIT2, BPNT2, KIF3A, KIF3C, PRKCD, MLST8, MADD, MAP9, NADK2, NFS1, RASAL2, OPLAH, OSBPL10, PDP1, PFKP, RILPL1, RIPOR1, RUFY2, SACS, BNIP1, SFT2D2, SKIC2, SPEG, SRC, SYBU, TAGLN3, TGM2, UBR1, GC, ZFYVE1

### Function

The strongest interpretation is a neuronal and ciliary intracellular-trafficking module, centered on microtubule-dependent transport, organelle positioning, vesicle handling, and related signaling. This interpretation is supported by the prominent network position of KIF3C, the KIF3A–KIF3C relationship, repeated hu.MAP complexes containing KIF3A and KIF3C (hu.MAP huMAP3_07978.1) (hu.MAP huMAP3_09585.1) (hu.MAP huMAP3_10422.1) (hu.MAP huMAP3_12337.1) (hu.MAP huMAP3_13393.1), and annotations for neuronal transport, cilium assembly, primary cilia, vesicles, exocytosis, endocytosis, and synaptic activity among module members. Additional components connect this trafficking theme to Rho-family regulation through ARHGEF9 and RIPOR1, phospholipid handling through OSBPL10, autophagy through ATG5 and ZFYVE1, and mitochondrial or metabolic maintenance through genes such as GFM1, PDP1, NFS1, and NADK2. However, no GO or KEGG term passed global correction, and there was no STRING functional enrichment. These annotations therefore support a biological interpretation but do not constitute globally significant enrichment. The module appears biologically heterogeneous rather than a narrowly defined pathway.

**Cell composition.** This is not predominantly a plasma or secreted-protein module and is not mainly a blood-cell module. Only GC, FBLN2, and TGM2 are annotated as secreted, while most members are intracellular or membrane-associated. HPA evidence shows a strong brain component, including brain-enriched or brain-enhanced genes and enrichment in excitatory neurons, inhibitory neurons, retinal cells, astrocytes, and related neural cell types. At the same time, most genes have low tissue specificity and many are enhanced in specialized cell types from diverse tissues, including germ cells, epithelial cells, muscle, liver, and immune populations. Several genes show immune-cell enhancement or group enrichment, but the overall profile does not support a blood-cell explanation. The shared brain and cell-line signal could therefore reflect broadly conserved cellular machinery, with a neural contribution in brain samples, rather than a purely brain-specific pathway. Brain protein detection is widespread among the tested brain regions, whereas the supplied cell-line comparison has no matching HPA tissue category and therefore cannot be directly assessed by HPA protein detection.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The high-confidence STRING evidence is sparse and consists of ATG5–ZFYVE1, GIT2–SRC, KIF3A–KIF3C, and PRKCD–SRC. These relationships support links to autophagy or membrane trafficking, signaling and cytoskeletal regulation, and the kinesin machinery, but they do not connect most module members into one established STRING interaction network. hu.MAP provides stronger structural support for selected submodules: KIF3A and KIF3C recur together in the kinesin-related complexes (hu.MAP huMAP3_07978.1) (hu.MAP huMAP3_09585.1) (hu.MAP huMAP3_10422.1) (hu.MAP huMAP3_12337.1) (hu.MAP huMAP3_13393.1), SPEG and OSBPL10 occur together in (hu.MAP huMAP3_11485.1), and GFM1 and PDP1 occur together in the broad mitochondrial and metabolic complex (hu.MAP huMAP3_13468.1). The fact that only a subset of each complex is present means these are partial complex signatures, not evidence that the entire module is one physical complex. Overall, known relationships support several coherent local neighborhoods embedded in a sparse co-abundance graph.

**STRING interactions (score >= 0.7)**: 4 of 1035 gene pairs: ATG5–ZFYVE1 (0.797); GIT2–SRC (0.934); KIF3A–KIF3C (0.992); PRKCD–SRC (0.983)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07978.1 (KIF3C, KIF3A; 2/5); huMAP3_09585.1 (KIF3C, KIF3A; 2/6); huMAP3_10422.1 (KIF3C, KIF3A; 2/8); huMAP3_12337.1 (KIF3C, KIF3A; 2/11); huMAP3_13393.1 (KIF3C, KIF3A; 2/12); huMAP3_11485.1 (SPEG, OSBPL10; 2/26); huMAP3_13468.1 (GFM1, PDP1; 2/99)

### Novelty

The module should not be claimed as a newly discovered molecular complex or pathway. Its most interpretable elements recapitulate known biology, especially the KIF3A–KIF3C kinesin association, the hu.MAP kinesin complexes (hu.MAP huMAP3_07978.1) (hu.MAP huMAP3_09585.1) (hu.MAP huMAP3_10422.1) (hu.MAP huMAP3_12337.1) (hu.MAP huMAP3_13393.1), autophagy-related ATG5–ZFYVE1, and SRC-linked signaling relationships. Conversely, the absence of broad STRING enrichment, the absence of globally significant GO or KEGG terms, and the limited overlap with annotated hu.MAP complexes indicate that the particular cross-tissue co-abundance combination may be a dataset-specific or context-dependent observation. That observation could be useful and potentially novel as a reproducible module, but novelty requires replication in independent brain and cell-line datasets, preservation of the module under resampling, and experimental testing of the proposed links. Absence from interaction databases alone is not evidence of novelty.

**Hypothesis.** Hypothesis: the module represents a conserved cellular state in which kinesin-dependent microtubule transport and ciliary or vesicular trafficking are coordinated with membrane-lipid organization, small-GTPase signaling, autophagic quality control, and mitochondrial metabolic support. KIF3A and KIF3C may provide the transport backbone; ARHGEF9, SRC, PRKCD, GIT2, and related regulators may tune membrane or synaptic signaling; OSBPL10 may couple trafficking to lipid transfer; and ATG5 with ZFYVE1 may connect the system to autophagic membrane dynamics. In brain, this could support neuronal polarity, axonal or synaptic cargo delivery, and ciliary function. The same co-abundance pattern in a cell line may reflect conserved housekeeping machinery or a shared trafficking state rather than neuron-specific function. This is a hypothesis, not a demonstrated causal mechanism.

### Important genes

#### KIF3C

- **Related proteins** (co-abundance neighbors): OSBPL10 (0.91), PRKCD (0.91), SACS (0.90), RIPOR1 (0.90), PPP2R5D (0.89), DST (0.89), SKIC2 (0.88), ANKRD46 (0.88), PFKP (0.87), RASAL2 (0.87), ZFYVE1 (0.87), RUFY2 (0.87), ASAP2 (0.86), MLST8 (0.86), NFS1 (0.86), TBRG4 (0.85), EXOC1 (0.85), UBR1 (0.84), BPNT2 (0.84), RILPL1 (0.83), SFT2D2 (0.83), GFM1 (0.83), TGM2 (0.83), PDP1 (0.82), BNIP1 (0.82), ATG5 (0.81), GIT2 (0.80); STRING partners: KIF3A (0.992)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07978.1, huMAP3_09585.1, huMAP3_10422.1, huMAP3_12337.1, huMAP3_13393.1
- **Function (MyGene.info)**: kinesin family member 3C. Predicted to enable microtubule binding activity and microtubule motor activity. Predicted to be involved in microtubule-based movement. Predicted to act upstream of or within organelle transport along microtubule. Predicted to be located in microtubule cytoskeleton; neuronal cell body; and neuronal ribonucleoprotein granule. Predicted to be part of kinesin complex. Predicted to be active in micro…
- **Diseases (Open Targets)**: atrial fibrillation (0.452); type 2 diabetes mellitus (0.329); atrial flutter (0.297); heart disorder (0.292); thrombophilia (0.288)
- **Europe PMC papers**: 494
- **Why important**: KIF3C is the central network gene in the supplied graph, with the greatest connectivity and weighted strength. It is brain-enriched and enhanced across several neuronal and retinal cell types, and its annotations include microtubule motor activity, microtubule-based movement, organelle transport, and cilium assembly. It has a direct high-confidence STRING relationship with KIF3A and occurs with KIF3A in the repeated hu.MAP complexes (hu.MAP huMAP3_07978.1) (hu.MAP huMAP3_09585.1) (hu.MAP huMAP3_10422.1) (hu.MAP huMAP3_12337.1) (hu.MAP huMAP3_13393.1). Its disease and literature record is substantial, including association with neurological and cardiovascular traits.
- **Conclusion**: Established evidence supports KIF3C as the best network anchor and as a plausible marker of microtubule-dependent transport in this module. It is not established that KIF3C drives the entire module or that every peripheral gene participates in its kinesin complex. The proposed role as the organizing hub of the co-abundance pattern remains a hypothesis.

#### KIF3A

- **Related proteins** (co-abundance neighbors): ARHGEF9 (0.81), FBLN2 (0.80); STRING partners: KIF3C (0.992)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm, Primary cilium, Basal body, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_07978.1, huMAP3_09585.1, huMAP3_10422.1, huMAP3_12337.1, huMAP3_13393.1
- **Function (MyGene.info)**: kinesin family member 3A. Enables protein phosphatase binding activity; small GTPase binding activity; and spectrin binding activity. Involved in protein localization to cell junction and protein transport. Located in centriole and centrosome. Part of kinesin II complex. Colocalizes with spindle microtubule. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.541); ventricular septal defect (0.289); atopic eczema (0.283); alcohol drinking (0.234); asthma (0.225)
- **Europe PMC papers**: 2473
- **Why important**: KIF3A provides the clearest independent confirmation of the kinesin interpretation. It is brain- and retina-enhanced, occurs in neuronal and respiratory ciliated cell types, is localized to the primary cilium and basal body, and is annotated for anterograde axonal transport, intracellular protein localization, and transport along microtubules. It forms the high-confidence STRING pair with KIF3C and appears with KIF3C in the repeated hu.MAP complexes (hu.MAP huMAP3_07978.1) (hu.MAP huMAP3_09585.1) (hu.MAP huMAP3_10422.1) (hu.MAP huMAP3_12337.1) (hu.MAP huMAP3_13393.1). Its literature is extensive and includes neurodegenerative and developmental disease relevance.
- **Conclusion**: Established evidence identifies KIF3A as a known kinesin and ciliary transport component that strengthens the module’s microtubule-trafficking interpretation. The co-abundance data do not prove that the complete canonical kinesin complex is present or active in every sample, so that broader inference remains a hypothesis.

#### ARHGEF9

- **Related proteins** (co-abundance neighbors): ANKRD46 (0.91), UBR1 (0.89), OPLAH (0.86), PRMT5 (0.84), DPP3 (0.83), SRC (0.83), NADK2 (0.82), AGFG2 (0.82), CFAP20 (0.81), PRKCD (0.81), KIF3A (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Cdc42 guanine nucleotide exchange factor 9. The protein encoded by this gene is a Rho-like GTPase that switches between the active (GTP-bound) state and inactive (GDP-bound) state to regulate CDC42 and other genes. This brain-specific protein also acts as an adaptor protein for the recruitment of gephyrin and together these proteins facilitate receceptor recruitement in GABAnergic and glycinergic synapses. Defects in this gene are the cause…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 8 (0.795); hereditary disease (0.528); X-linked intellectual disability-epilepsy syndrome (0.473); developmental disability (0.455); X-linked complex neurodevelopmental disorder (0.370)
- **Europe PMC papers**: 679
- **Why important**: ARHGEF9 is a comparatively well-connected module member and links the transport-centered neighborhood to neuronal signaling. It is brain- and retina-enhanced, is detected in brain, and is annotated as a CDC42-related guanine-nucleotide exchange factor and adaptor involved in gephyrin recruitment and postsynaptic specialization assembly. Its strong disease associations include developmental and epileptic encephalopathy and X-linked intellectual disability-epilepsy syndromes. It has a substantial literature record and connects in the module to SRC, UBR1, PRMT5, DPP3, and other regulators.
- **Conclusion**: Established evidence supports ARHGEF9 as a neuronal synaptic signaling and cytoskeletal-regulatory component that may explain why a trafficking module is prominent in brain. There is no STRING or hu.MAP support for a direct physical complex with the module’s kinesins, so its placement in a common mechanism is a co-abundance-based hypothesis.

#### SYBU

- **Related proteins** (co-abundance neighbors): GC (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntabulin. Syntabulin/GOLSYN is part of a kinesin motor-adaptor complex that is critical for the anterograde axonal transport of active zone components and contributes to activity-dependent presynaptic assembly during neuronal development (Cai et al., 2007 [PubMed 17611281]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: alcohol drinking (0.333); urolithiasis (0.333); Alzheimer disease (0.319); ovarian neoplasm (0.314); arthropathy (0.297)
- **Europe PMC papers**: 266
- **Why important**: SYBU is a brain-enhanced vesicle-associated protein expressed across several neuronal cell types. Its annotated function is part of a kinesin motor-adaptor system for anterograde axonal transport of active-zone components, with roles in presynaptic assembly, synaptic activity, and dense-core vesicle transport. Within this module it links to GC and therefore connects neuronal transport biology to a secreted plasma protein that may represent tissue or sample composition. Its disease and neuroscience literature is moderate and specifically relevant to neuronal transport.
- **Conclusion**: Established evidence makes SYBU a strong functional bridge between kinesin transport and neuronal vesicle biology. The module does not establish whether SYBU is mechanistically coupled to KIF3A or KIF3C here, nor whether the GC connection is physical rather than abundance-related. Those interpretations remain hypotheses.

#### ATG5

- **Related proteins** (co-abundance neighbors): KIF3C (0.81); STRING partners: ZFYVE1 (0.797)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Primary cilium transition zone, Centrosome, Basal body; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: autophagy related 5. The protein encoded by this gene, in combination with autophagy protein 12, functions as an E1-like activating enzyme in a ubiquitin-like conjugating system. The encoded protein is involved in several cellular processes, including autophagic vesicle formation, mitochondrial quality control after oxidative damage, negative regulation of the innate antiviral immune response, lymphocyte development a…
- **Diseases (Open Targets)**: neurodegenerative disease (0.557); rheumatoid arthritis (0.366); asthma (0.353); systemic lupus erythematosus (0.328); plasma cell myeloma (0.293)
- **Europe PMC papers**: 26318
- **Why important**: ATG5 supplies a quality-control and membrane-remodeling dimension that is not captured by the kinesin genes alone. It is annotated for autophagosome assembly, mitophagy, and autophagy, and is localized in the primary-cilium transition zone, centrosome, and basal body. It has a direct STRING relationship with ZFYVE1, whose FYVE domains support phosphatidylinositol-three-phosphate membrane recruitment and whose annotations include macroautophagy. ATG5 has an exceptionally extensive literature and disease relevance spanning neurodegeneration and immune disorders.
- **Conclusion**: Established evidence supports ATG5 as a plausible autophagic and organelle-quality-control component of the module. Its direct relationship to the transport backbone is not demonstrated by the supplied STRING or hu.MAP evidence, so coupling of autophagy to kinesin and ciliary trafficking is a mechanistic hypothesis rather than an established conclusion.

## Module 1

**Tissue pair**: brain and cell line  
**Genes (25)**: HIBADH, ACADM, C4BPA, CLU, D2HGDH, ERLIN1, EXOC7, FGB, FLNB, QRSL1, AGL, HSPA4L, DTYMK, MAPK10, NIPSNAP2, PFKM, RABGGTA, PNPT1, RAB8A, RMND1, SCFD1, SPATA2, STAT1, STOM, IARS2

### Function

No GO or KEGG term passed global correction, so the module has no statistically established pathway annotation from those analyses. Its network is dominated by C4BPA, with most other genes connected to that hub rather than to one another. Individual gene annotations suggest a mixed program involving circulating complement and coagulation proteins, mitochondrial translation and metabolism, vesicle trafficking, membrane organization, and cytokine or stress signaling. These are interpretive themes from the genes and network, not globally significant enrichment claims. The module may therefore reflect shared abundance across sample components or cell types rather than one unified molecular machine.

**Cell composition.** The composition warrants strong caution about sample and cell-type effects. C4BPA, FGB, and CLU are secreted to blood; C4BPA and FGB are liver-enriched, while CLU is liver-enhanced. HPA also reports frequent enrichment in liver, skeletal muscle, tongue, hepatocytes, syncytiotrophoblasts, esophageal apical cells, Müller glia, and platelets. Most genes have low immune-cell specificity, but several show platelet or blood-cell-associated patterns. A blood or shared-cell-type contribution is therefore plausible. Many intracellular proteins are detected in brain, but the secreted proteins may reflect vascular or sample-fluid material rather than brain-cell expression. The shared brain and cell-line pattern should not be interpreted as brain-specific without controlling for these effects.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides limited direct support. EXOC7 connects with RAB8A, and RAB8A connects with RABGGTA, supporting a small vesicle-trafficking substructure. Most module pairs lack high-confidence STRING support. hu.MAP shows partial overlaps with known complexes: D2HGDH, PNPT1, QRSL1, and IARS2 occur together in a mitochondrial and translation-related complex; ERLIN1, STOM, and RMND1 occur together in membrane or mitochondrial-associated complexes; RAB8A and RABGGTA occur together in Rab-related complexes; and FGB with C4BPA repeatedly overlaps plasma-protein complexes. These overlaps show that some members belong to known biological neighborhoods, but the limited overlap within large complexes and sparse STRING graph argue against treating the entire module as one established physical complex.

**STRING interactions (score >= 0.7)**: 2 of 300 gene pairs: EXOC7–RAB8A (0.798); RAB8A–RABGGTA (0.741)
**STRING functional enrichment (supplementary, within-query FDR)**: DISEASES Autosomal recessive disease (FDR = 0.0483, 12 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (D2HGDH, PNPT1, QRSL1, IARS2; 4/99); huMAP3_10725.1 (ERLIN1, STOM, RMND1; 3/59); huMAP3_09822.1 (STOM, RMND1; 2/28); huMAP3_08395.1 (FGB, C4BPA; 2/43); huMAP3_11094.1 (RAB8A, RABGGTA; 2/43); huMAP3_11860.1 (RAB8A, RABGGTA; 2/44); huMAP3_09531.1 (FGB, C4BPA; 2/47); huMAP3_10101.1 (FGB, C4BPA; 2/49); huMAP3_12042.1 (STOM, SCFD1; 2/56); huMAP3_15040.1 (FGB, C4BPA; 2/64); huMAP3_10678.1 (FGB, C4BPA; 2/71)

### Novelty

This module is not demonstrated to be a new biological pathway or complex. It contains well-established biology involving complement and coagulation, mitochondrial enzymes and RNA processing, Rab geranylgeranylation and trafficking, and signaling or cytoskeletal proteins. Some relationships are represented in STRING or hu.MAP, while many other pairings are not. Absence from those resources does not establish novelty because co-abundance can result from shared cell composition, secretion, or coordinated abundance without direct physical interaction. The defensible conclusion is that the particular cross-tissue co-abundance arrangement is a candidate observation requiring replication and adjustment for blood, hepatocyte, and other cell-type contributions.

**Hypothesis.** Hypothesis: the shared signal may combine circulating liver-derived proteins with intracellular programs common to brain-associated material and the cell line. C4BPA may act as a co-abundance anchor for secreted complement and coagulation proteins, while a smaller intracellular branch reflects mitochondrial translation or metabolism and another branch reflects Rab-dependent vesicle delivery. Brain detection of many intracellular members could indicate genuine expression, whereas the secreted members could reflect vascular or sample-fluid contribution. This hypothesis predicts that the broad module should weaken after adjustment for blood and hepatocyte markers, while the RAB8A–RABGGTA–EXOC7 and mitochondrial substructures may remain more reproducible.

### Important genes

#### C4BPA

- **Related proteins** (co-abundance neighbors): HIBADH (0.90), IARS2 (0.90), RABGGTA (0.89), STAT1 (0.88), RMND1 (0.88), FLNB (0.86), PNPT1 (0.86), AGL (0.86), HSPA4L (0.85), RAB8A (0.85), CLU (0.84), ACADM (0.84), NIPSNAP2 (0.84), STOM (0.84), QRSL1 (0.83), PFKM (0.82), D2HGDH (0.82), ERLIN1 (0.82), EXOC7 (0.81), DTYMK (0.81), SCFD1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: complement component 4 binding protein alpha. This gene encodes a member of a superfamily of proteins composed predominantly of tandemly arrayed short consensus repeats of approximately 60 amino acids. Along with a single, unique beta-chain, seven identical alpha-chains encoded by this gene assemble into the predominant isoform of C4b-binding protein, a multimeric protein that controls activation of the complement cascade through the classica…
- **Diseases (Open Targets)**: venous thromboembolism (0.445); dengue disease (0.370); Thromboembolism (0.332); Alzheimer disease (0.246); Parkinson disease (0.243)
- **Europe PMC papers**: 1611
- **Why important**: C4BPA is the dominant network hub and has the strongest weighted connectivity in the module. It encodes a complement-regulatory protein, is secreted to blood, is liver-enriched, and is immune-cell associated in HPA. It connects in the module to genes spanning mitochondrial, metabolic, signaling, cytoskeletal, and trafficking annotations. Its disease associations include thromboembolic and neurodegenerative conditions, and it has a substantial literature base.
- **Conclusion**: Established: C4BPA is a complement-regulatory blood protein and the principal co-abundance hub. Hypothesis: it may anchor a circulating or sample-composition signal rather than coordinate all intracellular genes mechanistically. It is the most important gene for evaluating possible confounding.

#### FGB

- **Related proteins** (co-abundance neighbors): D2HGDH (0.89); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: fibrinogen beta chain. The protein encoded by this gene is the beta component of fibrinogen, a blood-borne glycoprotein comprised of three pairs of nonidentical polypeptide chains. Following vascular injury, fibrinogen is cleaved by thrombin to form fibrin which is the most abundant component of blood clots. In addition, various cleavage products of fibrinogen and fibrin regulate cell adhesion and spreading, display vas…
- **Diseases (Open Targets)**: congenital afibrinogenemia (0.786); familial dysfibrinogenemia (0.705); congenital fibrinogen deficiency (0.622); familial hypodysfibrinogenemia (0.597); cancer (0.592)
- **Europe PMC papers**: 4215
- **Why important**: FGB is a liver-enriched protein secreted to blood and a component of fibrinogen, with established roles in coagulation, platelet activation, fibrinolysis, and cell adhesion. It appears with C4BPA in several hu.MAP plasma-protein complexes and is included in the supplementary STRING disease term. Its network position is peripheral, but its biological and sample-composition relevance is high and its literature base is substantial.
- **Conclusion**: Established: FGB is a circulating fibrinogen chain with strong relevance to blood and coagulation. Hypothesis: its co-abundance with the module may primarily report plasma or vascular material rather than a brain-cell mechanism.

#### RAB8A

- **Related proteins** (co-abundance neighbors): C4BPA (0.85); STRING partners: EXOC7 (0.798), RABGGTA (0.741)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11094.1, huMAP3_11860.1
- **Function (MyGene.info)**: RAB8A, member RAS oncogene family. The protein encoded by this gene is a member of the RAS superfamily which are small GTP/GDP-binding proteins with an average size of 200 amino acids. The RAS-related proteins of the RAB/YPT family may play a role in the transport of proteins from the endoplasmic reticulum to the Golgi and the plasma membrane. This protein shares 97%, 96%, and 51% similarity with the dog RAB8, mouse MEL, and mouse …
- **Diseases (Open Targets)**: acute respiratory distress syndrome (0.077); non-small cell lung carcinoma (0.076); esophageal cancer (0.076); congenital diarrhea 5 with tufting enteropathy (0.068); inflammatory bowel disease 30 (0.067)
- **Europe PMC papers**: 2105
- **Why important**: RAB8A is connected to the module hub and is the central member of the only explicit STRING-supported trafficking subgraph, connecting with EXOC7 and RABGGTA. It has established functions in exocytosis, Golgi organization, endocytic recycling, and plasma-membrane delivery. HPA associates it with megakaryocyte and platelet lineages, while hu.MAP places it in Rab-related complexes. Its literature volume is substantial.
- **Conclusion**: Established: RAB8A participates in vesicle trafficking and has independent STRING and hu.MAP support for relationships with EXOC7 and RABGGTA. Hypothesis: this is a genuine intracellular submodule within the broader co-abundance pattern, although the data do not establish that it is functionally coupled to C4BPA.

#### D2HGDH

- **Related proteins** (co-abundance neighbors): FGB (0.89), C4BPA (0.82), MAPK10 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: D-2-hydroxyglutarate dehydrogenase. This gene encodes D-2hydroxyglutarate dehydrogenase, a mitochondrial enzyme belonging to the FAD-binding oxidoreductase/transferase type 4 family. This enzyme, which is most active in liver and kidney but also active in heart and brain, converts D-2-hydroxyglutarate to 2-ketoglutarate. Mutations in this gene are present in D-2-hydroxyglutaric aciduria, a rare recessive neurometabolic disorder caus…
- **Diseases (Open Targets)**: D-2-hydroxyglutaric aciduria (0.837); asthma (0.574); atopic eczema (0.520); allergic disease (0.511); allergic rhinitis (0.499)
- **Europe PMC papers**: 509
- **Why important**: D2HGDH is a mitochondrial enzyme that converts D-2-hydroxyglutarate to 2-ketoglutarate and is active in tissues including brain. It connects to FGB, C4BPA, and MAPK10 in the module and is part of the hu.MAP mitochondrial complex containing IARS2, PNPT1, and QRSL1. It has a clear recessive neurometabolic disease association and a meaningful literature base.
- **Conclusion**: Established: D2HGDH represents mitochondrial organic-acid metabolism and is associated with D-2-hydroxyglutaric aciduria. Hypothesis: its co-abundance may reflect a mitochondrial metabolic state shared by brain material and the cell line, but the module provides no globally corrected enrichment evidence for that interpretation.

#### STAT1

- **Related proteins** (co-abundance neighbors): C4BPA (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal transducer and activator of transcription 1. The protein encoded by this gene is a member of the STAT protein family. In response to cytokines and growth factors, STAT family members are phosphorylated by the receptor associated kinases, and then form homo- or heterodimers that translocate to the cell nucleus where they act as transcription activators. The protein encoded by this gene can be activated by various ligands including interferon-…
- **Diseases (Open Targets)**: immunodeficiency 31B (0.786); chronic mucocutaneous candidiasis (0.775); autoimmune enteropathy and endocrinopathy - susceptibility to chronic infections syndrome (0.772); cancer (0.554); immunodeficiency disease (0.482)
- **Europe PMC papers**: 66602
- **Why important**: STAT1 is directly connected to the C4BPA hub and is a broadly important cytokine and growth-factor signal transducer. It mediates interferon and other ligand responses, has brain protein detection, and has extensive disease and literature associations involving immunodeficiency, infection, autoimmunity, and cancer. Its network position is peripheral, but its regulatory function makes it useful for interpreting a possible inflammatory or stress-related context.
- **Conclusion**: Established: STAT1 is a cytokine-responsive transcription factor with major immune and disease relevance. Hypothesis: its co-abundance may indicate a shared signaling or cellular-stress state, but the module alone cannot distinguish that explanation from correlated cell composition.

## Module 2

**Tissue pair**: brain and cell line  
**Genes (46)**: A2M, ABCA2, ACBD5, ADGRL3, AIMP1, AGT, AP3M2, ARPC5, ATG4C, BLTP3B, IBA57, CEP170, CLIC1, CMC1, SPECC1L, DGKQ, DIP2C, EXOC8, FAM171A1, FADS6, FSD1L, GDAP1, GRAMD4, KIF5A, LDHD, MARK1, MTMR12, SBF2, MYCBP, NDUFC1, OPHN1, PDE12, PLIN4, PNMA1, REEP1, ROBO2, SNRK, SRGAP2, SRXN1, IARS1, LARS1, TNS1, ACAA2, TIAM1, VAT1L, WDR47

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent; therefore the module should not be assigned a single pathway function from enrichment. Its internal structure instead suggests a composite program involving neuronal membrane organization, intracellular trafficking, lipid handling, cytoskeletal regulation, mitochondrial maintenance, and translation. The strongest coherent signals are neuronal transport and morphology: KIF5A and REEP1 connect to transport and membrane or organelle organization, ROBO2 and SRGAP2 connect to axon guidance and Rac-related neuronal morphogenesis, and TIAM1, MARK1, DGKQ, and OPHN1 connect to signaling, polarity, cytoskeletal remodeling, or cell shape. A separate translation-associated component is formed by AIMP1, IARS1, and LARS1. These observations support a biologically mixed, brain-associated co-abundance module rather than a single established biochemical pathway.

**Cell composition.** The HPA profile is predominantly compatible with neural and glial biology: brain is the most frequent enriched tissue, and brain neuronal, oligodendrocyte, and microglial cell types are prominent. Most genes have low or broad tissue specificity, so the module is not uniformly neuron-specific. The module is not mostly plasma or secreted proteins: only AGT, A2M, and AIMP1 are annotated as secreted to blood. AGT is liver-enriched and A2M is lung-enhanced, providing a possible circulating or tissue-fluid component, but this does not dominate the module. Immune specificity is generally low, although several genes show enhancement in neutrophils or other blood-cell populations. The pattern therefore does not strongly support a blood-contamination explanation, while shared neural cell types or broadly expressed cellular programs remain plausible. Brain protein detection is widespread for the module, whereas the cell-line HPA comparison has no matching tissue data and is therefore uninformative.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING contains only a small set of high-confidence relationships within the module. The strongest known links are the AIMP1-IARS1-LARS1 translation-associated cluster, the ROBO2-SRGAP2 neuronal guidance pair, the KIF5A-REEP1 transport-related pair, and the GDAP1-SBF2 pair associated with neuropathy biology. These links provide focused support for real biological subnetworks but do not establish dense connectivity across the whole module. hu.MAP independently supports the AIMP1-IARS1-LARS1 multisynthetase-complex component through (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). It also repeatedly places SRGAP2 with TIAM1 and MARK1 in signaling and cytoskeletal complexes through (hu.MAP huMAP3_10808.1), (hu.MAP huMAP3_12897.1), (hu.MAP huMAP3_06971.1), (hu.MAP huMAP3_04537.1), (hu.MAP huMAP3_07596.1), (hu.MAP huMAP3_07838.1), and (hu.MAP huMAP3_09810.1), while AGT and A2M recur together in plasma-protein and extracellular-complex contexts through (hu.MAP huMAP3_07701.1), (hu.MAP huMAP3_09273.1), (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1), and (hu.MAP huMAP3_10678.1). The hu.MAP evidence therefore supports several known subassemblies, but the module-wide organization is not represented as one clearly unified complex.

**STRING interactions (score >= 0.7)**: 6 of 1035 gene pairs: AIMP1–IARS1 (0.996); AIMP1–LARS1 (0.997); GDAP1–SBF2 (0.741); IARS1–LARS1 (0.999); KIF5A–REEP1 (0.855); ROBO2–SRGAP2 (0.962)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (IARS1, AIMP1, LARS1; 3/14); huMAP3_13688.1 (IARS1, AIMP1, LARS1; 3/14); huMAP3_10808.1 (SRGAP2, TIAM1, MARK1; 3/54); huMAP3_12897.1 (SRGAP2, TIAM1, MARK1; 3/93); huMAP3_07701.1 (AGT, A2M; 2/22); huMAP3_09273.1 (AGT, A2M; 2/28); huMAP3_06971.1 (TIAM1, MARK1; 2/28); huMAP3_04537.1 (SRGAP2, TIAM1; 2/29); huMAP3_07596.1 (TIAM1, MARK1; 2/35); huMAP3_09542.1 (SRGAP2, SPECC1L; 2/38); huMAP3_08395.1 (AGT, A2M; 2/43); huMAP3_07838.1 (SRGAP2, TIAM1; 2/43); huMAP3_09531.1 (AGT, A2M; 2/47); huMAP3_10101.1 (AGT, A2M; 2/49); huMAP3_09810.1 (SRGAP2, TIAM1; 2/56); huMAP3_15040.1 (AGT, A2M; 2/64); huMAP3_10678.1 (AGT, A2M; 2/71)

### Novelty

The co-abundance module may be a new cross-tissue association pattern, but the available evidence is insufficient to call it a new molecular mechanism. Its component relationships are largely established: aminoacyl-tRNA synthetase assembly, neuronal guidance and Rac signaling, kinesin-linked transport, mitochondrial and lipid processes, and circulating protein biology are all known areas. The limited STRING connectivity and the repeated hu.MAP membership argue against a wholly novel interaction network, while the combination of these subnetworks in a conserved brain and cell-line co-abundance pattern could still be novel. Absence of a STRING or hu.MAP relationship for many gene pairs is evidence of limited prior interaction coverage, not proof of novelty. The most defensible conclusion is novelty at the level of module composition or co-abundance context, pending replication and comparison with published co-expression modules.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in which neuronal or neuron-like cells coordinate membrane lipid handling, cytoskeletal remodeling, vesicle and organelle transport, mitochondrial quality control, and protein-production capacity. DGKQ-centered signaling and lipid regulation could interface with TIAM1, OPHN1, MARK1, ROBO2, and SRGAP2 to regulate Rac-dependent morphology and membrane dynamics, while KIF5A, REEP1, ABCA2, and related trafficking genes support movement and organization of neuronal cargo. The AIMP1-IARS1-LARS1 complex may represent the translation-support arm of this state, and AGT-A2M may be a separate extracellular or sample-context signal rather than a core intracellular mechanism. This model predicts that the module will be strongest in neural cells with active neurite, membrane, and organelle remodeling, but it should not be treated as established without perturbation, cell-resolved replication, and direct biochemical testing.

### Important genes

#### DGKQ

- **Related proteins** (co-abundance neighbors): ROBO2 (0.95), LDHD (0.93), PNMA1 (0.92), ABCA2 (0.90), KIF5A (0.90), SNRK (0.89), TIAM1 (0.89), ATG4C (0.88), GDAP1 (0.85), AP3M2 (0.82), FSD1L (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: diacylglycerol kinase theta. The protein encoded by this gene contains three cysteine-rich domains, a proline-rich region, and a pleckstrin homology domain with an overlapping Ras-associating domain. It is localized in the speckle domains of the nucleus, and mediates the regeneration of phosphatidylinositol (PI) from diacylglycerol in the PI-cycle during cell signal transduction. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: systemic lupus erythematosus (0.462); Alzheimer disease (0.428); systemic sclerosis (0.427); dementia (0.398); neurodegenerative disease (0.370)
- **Europe PMC papers**: 541
- **Why important**: DGKQ has the strongest network position in the module and links lipid signaling to several otherwise distinct branches, including ROBO2, TIAM1, KIF5A, LDHD, PNMA1, ABCA2, SNRK, and ATG4C. Its annotated diacylglycerol-kinase activity, phosphatidic-acid production, and signaling roles provide a plausible connector between membrane lipid metabolism, cytoskeletal regulation, autophagy, and neuronal functions. Its disease associations include neurodegenerative and dementia-related indications, and its literature base is substantial.
- **Conclusion**: Established evidence supports DGKQ as a central network connector with roles in phosphoinositide-related signaling and membrane biology. It is a strong candidate for organizing the module, but the co-abundance data do not prove that DGKQ regulates the other branches. The proposed integrator role is therefore a hypothesis.

#### KIF5A

- **Related proteins** (co-abundance neighbors): DGKQ (0.90), ADGRL3 (0.87), PLIN4 (0.81); STRING partners: REEP1 (0.855)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 5A. This gene encodes a member of the kinesin family of proteins. Members of this family are part of a multisubunit complex that functions as a microtubule motor in intracellular organelle transport. Mutations in this gene cause autosomal dominant spastic paraplegia 10. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: hereditary spastic paraplegia 10 (0.817); amyotrophic lateral sclerosis (0.717); myoclonus, intractable, neonatal (0.672); hereditary spastic paraplegia (0.576); Spastic paraplegia (0.559)
- **Europe PMC papers**: 1967
- **Why important**: KIF5A is brain-enriched, enhanced in excitatory and inhibitory neurons, and encodes a microtubule motor involved in vesicle and mitochondrial transport along axons. It connects the module to REEP1 through a high-confidence STRING relationship and is linked within the module to DGKQ, ADGRL3, and PLIN4. Its established association with hereditary spastic paraplegia and other motor-neuron disorders makes it particularly informative for a neuronal transport interpretation.
- **Conclusion**: Established evidence supports KIF5A as a neuronal cargo-transport component and as a disease-relevant marker of axonal maintenance. Its presence makes a transport-related module function plausible. Whether the broader module directly controls KIF5A-dependent transport remains unproven.

#### REEP1

- **Related proteins** (co-abundance neighbors): PLIN4 (0.91), MTMR12 (0.89), BLTP3B (0.86), GRAMD4 (0.86), EXOC8 (0.85), CLIC1 (0.84), CEP170 (0.84), WDR47 (0.82), IARS1 (0.81), MYCBP (0.80); STRING partners: KIF5A (0.855)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: receptor accessory protein 1. This gene encodes a mitochondrial protein that functions to enhance the cell surface expression of odorant receptors. Mutations in this gene cause spastic paraplegia autosomal dominant type 31, a neurodegenerative disorder. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: hereditary spastic paraplegia 31 (0.810); neuronopathy, distal hereditary motor, type 5B (0.588); hereditary spastic paraplegia (0.546); hereditary disease (0.485); spinal muscular atrophy, distal, autosomal recessive, 6 (0.468)
- **Europe PMC papers**: 889
- **Why important**: REEP1 is connected to multiple module branches, including PLIN4, MTMR12, BLTP3B, GRAMD4, EXOC8, CLIC1, CEP170, and WDR47, and has a known STRING relationship with KIF5A. Its annotated functions in membrane insertion and endoplasmic-reticulum tubular-network organization connect membrane shape, organelle distribution, and transport. It is detected in brain and enhanced in several neuronal populations, while its disease associations include hereditary spastic paraplegia and distal neuronopathy.
- **Conclusion**: Established evidence supports REEP1 as a membrane and organelle-organization factor with neuronal disease relevance. Its network placement makes it a plausible bridge between transport and membrane-shaping processes. A direct role in the complete module mechanism remains a hypothesis.

#### AIMP1

- **Related proteins** (co-abundance neighbors): FADS6 (0.85); STRING partners: IARS1 (0.996), LARS1 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: aminoacyl tRNA synthetase complex interacting multifunctional protein 1. The protein encoded by this gene is a cytokine that is specifically induced by apoptosis, and it is involved in the control of angiogenesis, inflammation, and wound healing. The release of this cytokine renders the tumor-associated vasculature sensitive to tumor necrosis factor. The precursor protein is identical to the p43 subunit, which is associated with the multi-tRNA synthetase complex, and i…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 3 (0.790); Pelizaeus-Merzbacher-like disease (0.657); POLR-related leukodystrophy (0.657); leukodystrophy (0.372); autosomal recessive non-syndromic intellectual disability (0.371)
- **Europe PMC papers**: 663
- **Why important**: AIMP1 is part of the compact AIMP1-IARS1-LARS1 subnetwork, with strong STRING links to both synthetases and repeated hu.MAP support in (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). It has a dual biological profile: it is associated with the multisynthetase complex and tRNA aminoacylation, while also having extracellular cytokine, angiogenesis, inflammation, and wound-healing functions. Its brain detection and associations with leukodystrophy and developmental disease make it relevant to the shared brain and cell-line context.
- **Conclusion**: Established evidence supports AIMP1 as a translation-complex component and as a multifunctional signaling protein that can have intracellular and secreted roles. The synthetase-complex interpretation is particularly well supported by STRING and hu.MAP. It is not established that its secreted activity contributes to this module.

#### SRGAP2

- **Related proteins** (co-abundance neighbors): FADS6 (0.93); STRING partners: ROBO2 (0.962)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_10808.1, huMAP3_12897.1, huMAP3_04537.1, huMAP3_09542.1, huMAP3_07838.1, huMAP3_09810.1
- **Function (MyGene.info)**: SLIT-ROBO Rho GTPase activating protein 2. This locus encodes a member of the SLIT-ROBO Rho GTPase activating protein family. The encoded protein stimulates GTPase activity of Rac1, and plays a role in cortical neuron development. This locus has several paralogs on human chromosome 1 resulting from segmental duplication. While this locus itself is conserved among various species, the paralogs are found only in the genus Homo, and not in th…
- **Diseases (Open Targets)**: neurodegenerative disease (0.307); Dupuytren Contracture (0.252); type 2 diabetes mellitus (0.212); systemic lupus erythematosus (0.198); fasciitis (0.194)
- **Europe PMC papers**: 813
- **Why important**: SRGAP2 is brain-enriched and linked by high-confidence STRING evidence to ROBO2, a receptor for SLIT-mediated axon guidance. It recurs with TIAM1 and MARK1 across multiple hu.MAP complexes, providing independent support for a neuronal signaling and cytoskeletal subnetwork. Its annotated functions include Rac regulation, lamellipodium assembly, cortical radial-glia migration, cell spreading, and neuronal development. Its disease associations include neurodegenerative disease and other neurological indications.
- **Conclusion**: Established evidence supports SRGAP2 as a neuronal morphogenesis and migration factor within a ROBO-related signaling context. Its network and complex evidence make it an important mechanistic representative of the module's neural branch. The hypothesis that it coordinates the lipid and translation branches is not directly demonstrated.

## Module 3

**Tissue pair**: brain and cell line  
**Genes (6)**: INA, ALDOB, EIF4A2, PRKACB, NME3, XPO7

### Function

The module does not have a statistically established GO or KEGG function: no globally significant GO/KEGG term passed global correction. Its structure is a hub-and-spoke pattern centered on ALDOB, with the remaining genes each connected to ALDOB. The gene annotations suggest several biological themes rather than one confirmed pathway: ALDOB supports fructose metabolism and glycolysis; PRKACB supports cAMP-dependent protein kinase signaling; EIF4A2 supports cytoplasmic translation initiation; XPO7 supports nucleocytoplasmic transport; NME3 supports nucleotide metabolism; and INA supports neuronal intermediate-filament organization. The co-abundance pattern therefore may reflect coordinated expression of metabolic, signaling, translational, transport, and neuronal structural programs, but this interpretation remains descriptive because no GO or KEGG term achieved global significance.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins, and it does not show a blood-cell-enriched pattern in HPA. Most genes have low tissue or cell-type specificity, while INA and PRKACB show brain-related enrichment or enhancement and INA is detected in neuronal cell types. ALDOB instead shows enrichment associated with intestine, kidney, and liver and is not detected by brain immunohistochemistry, making it a possible marker of metabolic or sample-composition effects rather than a core neuronal component. One module gene is annotated as secreted in the aggregate HPA summary, but the module as a whole is not secretome-dominated. The brain protein-detection pattern supports that most module proteins are detectable in brain, whereas the cell-line comparison has no matching HPA tissue context. The shared module could therefore reflect a mixture of broadly expressed cellular machinery with brain-associated neuronal components, rather than a blood-derived signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the specified evidence threshold, and no STRING functional-enrichment result was available. No hu.MAP complex contained multiple module members. Thus, the observed co-abundance edges are not reinforced by high-confidence known protein-protein interactions or a known shared hu.MAP complex. This does not show that the proteins cannot interact; it indicates that the module is primarily a co-abundance relationship and should not be presented as an established physical complex or canonical pathway.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported tissue-pair co-abundance pattern, especially because its particular combination of ALDOB, PRKACB, NME3, EIF4A2, XPO7, and INA is not supported by a known STRING interaction network or hu.MAP complex. However, absence from STRING and hu.MAP alone does not establish novelty. The lack of globally significant GO or KEGG enrichment also prevents a claim that the module defines a new biological pathway. The most defensible conclusion is that this is a potentially novel co-abundance association requiring replication, preservation testing, and comparison with independent brain and cell-line datasets.

**Hypothesis.** Hypothesis: the module captures a coordinated cellular state in which metabolic capacity represented by ALDOB covaries with cAMP signaling represented by PRKACB, while translation initiation, nucleocytoplasmic transport, nucleotide metabolism, and neuronal cytoskeletal structure vary in parallel. ALDOB may act as a network-level expression hub or may instead be a correlated marker of cell composition or metabolic state; the current data cannot distinguish these possibilities. A mechanistic test would examine whether perturbing cAMP signaling or cellular metabolic state changes the abundance or localization of the other module proteins, while controlling for neuronal proportion and sample composition.

### Important genes

#### ALDOB

- **Related proteins** (co-abundance neighbors): PRKACB (0.94), NME3 (0.86), EIF4A2 (0.85), XPO7 (0.84), INA (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldolase, fructose-bisphosphate B. Fructose-1,6-bisphosphate aldolase (EC 4.1.2.13) is a tetrameric glycolytic enzyme that catalyzes the reversible conversion of fructose-1,6-bisphosphate to glyceraldehyde 3-phosphate and dihydroxyacetone phosphate. Vertebrates have 3 aldolase isozymes which are distinguished by their electrophoretic and catalytic properties. Differences indicate that aldolases A, B, and C are distinct proteins, th…
- **Diseases (Open Targets)**: hereditary fructose intolerance (0.846); hereditary disease (0.518); acute liver failure (0.463); disorder of glycogen metabolism (0.455); carbohydrate metabolism disease (0.357)
- **Europe PMC papers**: 2383
- **Why important**: ALDOB is the module's central network hub, connected to every other member in the observed subgraph. Its established function is fructose-bisphosphate aldolase activity in glycolysis, fructose metabolism, and gluconeogenesis. HPA instead places it mainly in intestine, kidney, and liver-associated expression and reports no brain immunohistochemical detection, which makes it important both biologically and as a possible indicator of metabolic or sample-composition effects. It has substantial disease and literature support, including hereditary fructose intolerance and other carbohydrate-metabolism associations.
- **Conclusion**: Established evidence supports ALDOB as the network hub and a metabolic enzyme. It is not established that ALDOB mechanistically organizes the other proteins; its hub status may reflect coordinated abundance, cellular composition, or indirect regulation.

#### INA

- **Related proteins** (co-abundance neighbors): ALDOB (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: internexin neuronal intermediate filament protein alpha. Neurofilaments are type IV intermediate filament heteropolymers composed of light, medium, and heavy chains. Neurofilaments comprise the axoskeleton and they functionally maintain the neuronal caliber. They may also play a role in intracellular transport to axons and dendrites. This gene is a member of the intermediate filament family and is involved in the morphogenesis of neurons. [provided by R…
- **Diseases (Open Targets)**: neurodegenerative disease (0.373); Abnormal brain morphology (0.266); kidney disorder (0.254); pathological myopia (0.111); myopia (0.111)
- **Europe PMC papers**: 35120
- **Why important**: INA is directly connected to ALDOB and is the clearest neuronal structural marker in the module. Its established role is as a type four intermediate-filament protein involved in neuronal morphology, axonal caliber, and intracellular neuronal transport. HPA shows brain, pituitary, and retina enrichment, neuronal cell-type enhancement, intermediate-filament localization, and brain protein detection. It also has the largest literature footprint among the module genes and disease associations involving neurodegenerative disease and abnormal brain morphology.
- **Conclusion**: Established evidence supports INA as a neuronal cytoskeletal component and as evidence that the module can contain a brain-cellular signal. It remains a hypothesis that INA participates in a shared metabolic-signaling program with ALDOB rather than simply marking neuronal abundance.

#### PRKACB

- **Related proteins** (co-abundance neighbors): ALDOB (0.94); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase cAMP-activated catalytic subunit beta. The protein encoded by this gene is a member of the serine/threonine protein kinase family. The encoded protein is a catalytic subunit of cAMP (cyclic AMP)-dependent protein kinase, which mediates signalling though cAMP. cAMP signaling is important to a number of processes, including cell proliferaton and differentiation. Multiple alternatively spliced transcript variants encoding distinct isoform…
- **Diseases (Open Targets)**: cardioacrofacial dysplasia 2 (0.749); Ellis-van Creveld syndrome (0.370); hereditary disease (0.189); thrombophilia (0.094); smoking initiation (0.083)
- **Europe PMC papers**: 2157
- **Why important**: PRKACB is the only direct partner of ALDOB among the module genes that represents a canonical intracellular signaling enzyme. It encodes the catalytic beta subunit of cAMP-dependent protein kinase and is annotated in cAMP-linked receptor signaling, protein phosphorylation, and signal transduction. HPA reports brain tissue enhancement, detection in brain, and enhancement in several neural or neuroendocrine cell types. Its disease evidence includes developmental and congenital disorder associations, and it has a substantial literature base.
- **Conclusion**: Established evidence supports PRKACB as a brain-associated cAMP signaling kinase that could provide regulatory context for the module. A direct regulatory relationship between PRKACB and ALDOB or the other module members is not established by this co-abundance network.

#### EIF4A2

- **Related proteins** (co-abundance neighbors): ALDOB (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4A2. Enables ATP hydrolysis activity. Involved in negative regulation of RNA-directed 5'-3' RNA polymerase activity. Located in perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and speech delay, with or without seizures (0.744); neurodevelopmental disorder (0.565); hereditary disease (0.448); dengue disease (0.370); complex neurodevelopmental disorder (0.370)
- **Europe PMC papers**: 2227
- **Why important**: EIF4A2 is directly connected to the ALDOB hub and represents a core post-transcriptional process rather than a tissue-specific structural marker. Its established function is ATP-dependent participation in translation initiation and regulation of translational initiation. HPA reports low tissue specificity, cytosolic localization, brain protein detection, and enhancement in esophageal apical cells. It has substantial literature support and disease associations involving neurodevelopmental disorders with hypotonia, speech delay, and possible seizures.
- **Conclusion**: Established evidence supports EIF4A2 as a broadly used translational regulator that may report general cellular activity or protein-synthesis demand. Its inclusion does not establish a specialized neuronal translation module, and any link to ALDOB or PRKACB remains a hypothesis.

## Module 4

**Tissue pair**: brain and cell line  
**Genes (42)**: AKAP5, ALKBH4, AMER2, ANXA5, APOC3, CD163, CALB1, C2orf69, CIAO3, SLC44A2, DTNA, ECI2, EXOC3, GFRA1, GOLIM4, HERC4, IGFBP7, IGKC, INF2, ISOC1, CAMK1D, MVK, RHOT1, MLC1, SLC8A1, CYB5R2, NECAP1, NSF, ARHGAP26, SLC15A2, SGTB, SPTBN1, SPTAN1, SYT7, TMEM126B, TUBA4A, TBCK, TRIM9, TTC8, TYMP, SLC32A1, WDR7

### Function

No GO or KEGG term passed global correction, so the functional interpretation must remain evidence-weighted rather than enrichment-based. The gene annotations support a mixed module involving calcium-dependent signaling, synaptic and general vesicle trafficking, membrane organization, actin–spectrin scaffolding, and mitochondrial or metabolic support. The brain-associated component is represented by CALB1, AKAP5, SLC32A1, NSF, MLC1, DTNA, and related genes, whereas other genes indicate myeloid, hepatic, epithelial, or broadly expressed cellular programs. The supplementary STRING calmodulin-binding signal (STRING Keyword Calmodulin-binding; within-query FDR = 0.0274) is consistent with calcium-regulated signaling, but it is not globally corrected enrichment evidence.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module, although secreted or extracellularly detected genes are present, including CD163, APOC3, IGFBP7, and immunoglobulin gene IGKC. HPA evidence indicates substantial heterogeneity: many genes have low tissue specificity, while others are enriched in brain, retina, liver, heart muscle, or lymphoid tissue. The blood-cell signal is important, with enrichment or enhancement in neutrophils, eosinophils, monocytes, basophils, and related myeloid populations. CD163 and IGKC are especially suggestive of blood or immune-cell contribution, and CD163 is not detected in brain by HPA. Conversely, CALB1, MLC1, AKAP5, SLC32A1, NSF, DTNA, and AMER2 support genuine neural or glial biology. Brain protein detection is widespread among the module genes, whereas the cell-line HPA comparison is unavailable. Thus, the shared module may reflect a combination of conserved neuronal or glial biology, broadly expressed cellular machinery, and variable blood-cell or sample-composition effects rather than a single tissue-exclusive process.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known STRING relationship is the spectrin pair SPTAN1–SPTBN1. STRING also reports the supplementary calmodulin-binding set (STRING Keyword Calmodulin-binding; within-query FDR = 0.0274), containing SPTAN1, SPTBN1, AKAP5, SLC8A1, SYT7, and CAMK1D. The hu.MAP evidence is concentrated around the same spectrin pair: SPTAN1 and SPTBN1 occur together in complexes (hu.MAP huMAP3_07940.1), (hu.MAP huMAP3_05473.1), and (hu.MAP huMAP3_09165.1). APOC3 and TYMP each occur with other proteins in the large hu.MAP complex (hu.MAP huMAP3_10678.1), but their co-membership does not establish a direct interaction between them or with the rest of the module. Most module gene pairs are not supported by high-confidence STRING interactions, and most genes have no listed hu.MAP complex. This pattern supports a real local cytoskeletal or membrane-associated core around the spectrins, embedded in a broader co-abundance neighborhood rather than a single physically validated complex.

**STRING interactions (score >= 0.7)**: 1 of 861 gene pairs: SPTAN1–SPTBN1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Calmodulin-binding (FDR = 0.0274, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07940.1 (SPTBN1, SPTAN1; 2/5); huMAP3_05473.1 (SPTBN1, SPTAN1; 2/7); huMAP3_09165.1 (SPTBN1, SPTAN1; 2/39); huMAP3_10678.1 (APOC3, TYMP; 2/71)

### Novelty

The module-level co-abundance pattern may be a new observation, but the available evidence does not establish that it is a new biological mechanism. Its central spectrin relationship is already known in STRING and hu.MAP, and several component functions are well established, including calcium buffering by CALB1, vesicle recycling by NSF, GABA and glycine vesicle transport by SLC32A1, and membrane or cytoskeletal organization by the spectrins. The absence of most other module pairs from STRING or hu.MAP cannot prove novelty because co-abundance can arise from shared regulation, cell composition, or context-dependent biology without a curated physical interaction. A defensible conclusion is that the cross-tissue conserved module is potentially novel as a coordinated expression signature, while its constituent biology is largely established and its mechanistic novelty remains unproven.

**Hypothesis.** Hypothesis: the module reflects a conserved membrane-trafficking and calcium-handling state in neural or glial cells, with CALB1-linked calcium buffering and AKAP5 or CAMK1D-linked signaling coupled to spectrin-supported membrane organization, synaptic-vesicle handling, and NSF-dependent cargo recycling. MLC1 and mitochondrial or metabolic genes may support the membrane and energetic demands of this state. In some samples, the same co-abundance pattern may be strengthened by admixture of myeloid or blood-derived cells and by circulating proteins such as APOC3, IGFBP7, or CD163. This model predicts that the neural core and the blood-cell-associated component should separate when analyzed with cell-type-resolved data and that the proposed functional coupling should be tested by perturbing calcium handling or membrane trafficking rather than inferred from co-abundance alone.

### Important genes

#### CALB1

- **Related proteins** (co-abundance neighbors): CD163 (0.94), WDR7 (0.93), AKAP5 (0.91), RHOT1 (0.84), IGKC (0.84), CAMK1D (0.84), NSF (0.83), TMEM126B (0.81), ISOC1 (0.81), NECAP1 (0.81), TBCK (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calbindin 1. The protein encoded by this gene is a member of the calcium-binding protein superfamily that includes calmodulin and troponin C. Originally described as a 27 kDa protein, it is now known to be a 28 kDa protein. It contains four active calcium-binding domains, and has two modified domains that are thought to have lost their calcium binding capability. This protein is thought to buffer entry of calc…
- **Diseases (Open Targets)**: neurodegenerative disease (0.511); cutaneous melanoma (0.294); stroke disorder (0.293); alcohol drinking (0.291); kidney disorder (0.259)
- **Europe PMC papers**: 9561
- **Why important**: CALB1 is among the most connected genes in the module and links the network to AKAP5, CAMK1D, SLC-related biology, mitochondrial transport, and vesicle machinery. HPA places it in brain and inhibitory-neuron contexts, and its annotated function is calcium buffering after excitatory stimulation. It has substantial literature support and disease associations involving neurological and neurodegenerative phenotypes. Its position makes it a plausible organizing marker for the neural calcium-signaling component.
- **Conclusion**: Established evidence supports CALB1 as a brain-associated calcium-binding protein with a prominent module position. It is reasonable to hypothesize that CALB1 marks the neural component of the module, but the co-abundance data do not demonstrate that CALB1 regulates the other genes.

#### MLC1

- **Related proteins** (co-abundance neighbors): GOLIM4 (0.90), INF2 (0.87), SLC44A2 (0.86), ANXA5 (0.84), SPTAN1 (0.83), CIAO3 (0.83), TBCK (0.82), HERC4 (0.81), IGKC (0.81), ECI2 (0.81), CAMK1D (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: modulator of VRAC current 1. The function of this gene product is unknown; however, homology to other proteins suggests that it may be an integral membrane transporter. Mutations in this gene have been associated with megalencephalic leukoencephalopathy with subcortical cysts, an autosomal recessive neurological disorder. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by …
- **Diseases (Open Targets)**: megalencephalic leukoencephalopathy with subcortical cysts (0.827); hereditary disease (0.414); Seizure (0.370); Bilateral tonic-clonic seizure (0.370); Abnormality of the nervous system (0.340)
- **Europe PMC papers**: 1511
- **Why important**: MLC1 is highly connected within the module and is linked to GOLIM4, INF2, SLC44A2, ANXA5, SPTAN1, and trafficking-related genes. HPA shows brain tissue enrichment and astrocyte or glial enhancement. Its disease association with megalencephalic leukoencephalopathy with subcortical cysts gives it strong neurological relevance, while its annotated links to vesicle transport, osmotic stress, and membrane transport fit the proposed membrane-homeostasis interpretation.
- **Conclusion**: Established evidence supports MLC1 as a brain and glial membrane-homeostasis factor associated with neurological disease. Its network position supports a coordinating role in the module, but a direct functional bridge between MLC1 and the other module branches remains a hypothesis.

#### SPTAN1

- **Related proteins** (co-abundance neighbors): MLC1 (0.83); STRING partners: SPTBN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Microtubules; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_07940.1, huMAP3_05473.1, huMAP3_09165.1
- **Function (MyGene.info)**: spectrin alpha, non-erythrocytic 1. Spectrins are a family of filamentous cytoskeletal proteins that function as essential scaffold proteins that stabilize the plasma membrane and organize intracellular organelles. Spectrins are composed of alpha and beta dimers that associate to form tetramers linked in a head-to-head arrangement. This gene encodes an alpha spectrin that is specifically expressed in nonerythrocytic cells. The encod…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 5 (0.749); developmental delay with or without epilepsy (0.681); spastic paraplegia 91, autosomal dominant, with or without cerebellar ataxia (0.681); infantile spasms (0.651); genetic developmental and epileptic encephalopathy (0.651)
- **Europe PMC papers**: 1422
- **Why important**: SPTAN1 is the module member with the clearest external molecular support: it has a high-confidence STRING relationship with SPTBN1 and occurs with SPTBN1 in several hu.MAP complexes (hu.MAP huMAP3_07940.1), (hu.MAP huMAP3_05473.1), and (hu.MAP huMAP3_09165.1). Spectrin scaffolds stabilize plasma membranes, organize organelles, and connect membrane proteins to the actin cytoskeleton. SPTAN1 is brain-detected by HPA and has strong associations with developmental epileptic encephalopathy and related neurological disorders.
- **Conclusion**: Established evidence identifies SPTAN1 as part of a known spectrin scaffold and as a credible structural core of the module. The module may extend this scaffold into calcium and trafficking programs, but that extension is not established by the interaction databases.

#### SPTBN1

- **Related proteins** (co-abundance neighbors): NSF (0.82); STRING partners: SPTAN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_07940.1, huMAP3_05473.1, huMAP3_09165.1
- **Function (MyGene.info)**: spectrin beta, non-erythrocytic 1. Spectrin is an actin crosslinking and molecular scaffold protein that links the plasma membrane to the actin cytoskeleton, and functions in the determination of cell shape, arrangement of transmembrane proteins, and organization of organelles. It is composed of two antiparallel dimers of alpha- and beta- subunits. This gene is one member of a family of beta-spectrin genes. The encoded protein cont…
- **Diseases (Open Targets)**: developmental delay, impaired speech, and behavioral abnormalities (0.802); cancer (0.597); hereditary disease (0.516); hearing loss disorder (0.459); neurodevelopmental disorder (0.453)
- **Europe PMC papers**: 1635
- **Why important**: SPTBN1 is the obligate partner of the spectrin relationship supported by STRING and hu.MAP (hu.MAP huMAP3_07940.1), (hu.MAP huMAP3_05473.1), and (hu.MAP huMAP3_09165.1). Its annotated functions include actin-cytoskeleton organization, plasma-membrane organization, vesicle-mediated transport, and central nervous system development. HPA detects it in brain, and disease associations include developmental, behavioral, and hearing-related disorders. Its inclusion strengthens the interpretation that the module contains a membrane–cytoskeletal scaffold rather than only a generic expression cluster.
- **Conclusion**: Established evidence supports SPTBN1 as a structural and neuronal-developmental component of the module through its known partnership with SPTAN1. A broader role in coordinating the entire co-abundance module is plausible but remains hypothetical.

#### NSF

- **Related proteins** (co-abundance neighbors): CALB1 (0.83), SPTBN1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-ethylmaleimide sensitive factor, vesicle fusing ATPase. Enables PDZ domain binding activity and ionotropic glutamate receptor binding activity. Involved in intracellular protein transport; positive regulation of protein catabolic process; and positive regulation of receptor recycling. Located in Golgi apparatus; cytosol; and plasma membrane. Implicated in developmental and epileptic encephalopathy. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy 96 (0.561); neurodegenerative disease (0.529); atrial fibrillation (0.310); Abnormality of the skeletal system (0.303); androgenetic alopecia (0.300)
- **Europe PMC papers**: 65784
- **Why important**: NSF connects the CALB1 and SPTAN1 branches and has a well-established role in intracellular protein transport, exocytosis, vesicle recycling, and receptor recycling. HPA shows brain tissue enhancement and neuronal or microglial cell-type enhancement. Its very large literature base and association with developmental epileptic encephalopathy make it a biologically important candidate for linking the module's cytoskeletal and calcium-dependent signals to membrane trafficking.
- **Conclusion**: Established evidence supports NSF as a core vesicle-fusion and recycling ATPase with strong neural relevance. The network supports its candidacy as a bridge between structural and trafficking processes, but the module does not prove that NSF is the causal bridge.

#### CD163

- **Related proteins** (co-abundance neighbors): CALB1 (0.94), SYT7 (0.94), ARHGAP26 (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD163 molecule. The protein encoded by this gene is a member of the scavenger receptor cysteine-rich (SRCR) superfamily, and is exclusively expressed in monocytes and macrophages. It functions as an acute phase-regulated receptor involved in the clearance and endocytosis of hemoglobin/haptoglobin complexes by macrophages, and may thereby protect tissues from free hemoglobin-mediated oxidative damage. This protein…
- **Diseases (Open Targets)**: arthropathy (0.205); acute tonsillitis (0.205); adolescent idiopathic scoliosis (0.193); stroke disorder (0.191); CINCA syndrome (0.185)
- **Europe PMC papers**: 31467
- **Why important**: CD163 is connected to CALB1, SYT7, and ARHGAP26 and is the clearest marker of a possible blood or myeloid contribution. HPA identifies it in monocytes, macrophages, Kupffer cells, and Hofbauer cells, reports secretion to blood, and does not detect it in brain. Its function in hemoglobin–haptoglobin clearance and innate immune sensing provides a biologically coherent explanation for an immune-cell-associated branch, while its large literature base and disease associations make it more informative than an uncharacterized peripheral gene.
- **Conclusion**: Established evidence supports CD163 as a monocyte or macrophage marker and scavenger receptor, not as a neuronal module component. Its presence should therefore be treated as evidence for cell-composition influence or a myeloid-associated subcomponent; a direct CD163 role in the neural module is only a hypothesis.

## Module 5

**Tissue pair**: brain and cell line  
**Genes (17)**: BOP1, CHD1, DDX21, ESF1, GTPBP4, HEATR1, INTS8, KRR1, MYBBP1A, NOP2, NUP188, PLRG1, RBM28, RRP12, PDCD11, THOC2, WDR3

### Function

The module is strongly and coherently associated with nucleolar ribosome biogenesis, especially preribosome assembly, rRNA processing, rRNA metabolism, and ribonucleoprotein complex formation. These conclusions are supported by the globally corrected terms for ribosome biogenesis (GO:BP ribosome biogenesis; q_global = 1.13e-07), rRNA processing (GO:BP rRNA processing; q_global = 2.71e-07), the nucleolus (GO:CC nucleolus; q_global = 4.23e-07), RNA processing (GO:BP RNA processing; q_global = 4.58e-07), rRNA metabolic process (GO:BP rRNA metabolic process; q_global = 8.94e-07), ribonucleoprotein complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 1.72e-06), the preribosome (GO:CC preribosome; q_global = 0.00113), the small-subunit processome (GO:CC small-subunit processome; q_global = 0.00504), and eukaryotic ribosome biogenesis (KEGG Ribosome biogenesis in eukaryotes - Homo sapiens (human); q_global = 0.0191). The broad RNA-binding and nucleic-acid-binding annotations (GO:MF RNA binding; q_global = 0.000123) (GO:MF nucleic acid binding; q_global = 0.000448) indicate that the module is not merely a generic expression cluster but is concentrated in RNA maturation machinery. The RNA polymerase I regulatory terms (GO:BP positive regulation of transcription by RNA polymerase I; q_global = 0.0224) (GO:BP regulation of transcription by RNA polymerase I; q_global = 0.0377) further connect the module to control of ribosomal RNA production. Overall, this is best interpreted as a nucleolar RNA-processing and ribosome-biogenesis module shared by brain and cell line.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and the proteins are predominantly nuclear or nucleolar. Most genes have low tissue specificity, with protein detection in brain for nearly all genes with available data, supporting a broadly expressed intracellular housekeeping-like program rather than a brain-exclusive program. HPA does not support a strong blood-cell composition signal because almost all genes have low immune-cell specificity. RRP12 is an exception, with enrichment in bone marrow, monocyte-lineage cells, neutrophil-lineage cells, and neutrophils; several other genes have cell-type-enhanced annotations in diverse cell types. Thus, the shared brain–cell-line signal is more plausibly a conserved cellular ribosome-biogenesis program than contamination by plasma proteins or blood cells, although cellular composition could contribute to individual co-abundance patterns.

**GO/KEGG enrichment**: 32 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP ribosome biogenesis | 1.13e-07 | BOP1, DDX21, ESF1, GTPBP4, HEATR1, KRR1, MYBBP1A, NOP2, PDCD11, WDR3 |
| GO:BP rRNA processing | 2.71e-07 | BOP1, DDX21, ESF1, GTPBP4, HEATR1, KRR1, NOP2, PDCD11, WDR3 |
| GO:CC nucleolus | 4.23e-07 | BOP1, DDX21, ESF1, GTPBP4, HEATR1, KRR1, MYBBP1A, NOP2, PDCD11, PLRG1, RBM28, RRP12, WDR3 |
| GO:BP RNA processing | 4.58e-07 | BOP1, DDX21, ESF1, GTPBP4, HEATR1, INTS8, KRR1, NOP2, PDCD11, PLRG1, RBM28, THOC2, WDR3 |
| GO:BP rRNA metabolic process | 8.94e-07 | BOP1, DDX21, ESF1, GTPBP4, HEATR1, KRR1, NOP2, PDCD11, WDR3 |
| GO:BP ribonucleoprotein complex biogenesis | 1.72e-06 | BOP1, DDX21, ESF1, GTPBP4, HEATR1, KRR1, MYBBP1A, NOP2, PDCD11, WDR3 |
| GO:CC nuclear protein-containing complex | 3.76e-05 | BOP1, DDX21, HEATR1, INTS8, KRR1, MYBBP1A, NUP188, PDCD11, PLRG1, RBM28, THOC2, WDR3 |
| GO:MF RNA binding | 0.000123 | BOP1, DDX21, ESF1, GTPBP4, HEATR1, KRR1, MYBBP1A, NOP2, PDCD11, RBM28, RRP12, THOC2, WDR3 |
| GO:MF nucleic acid binding | 0.000448 | BOP1, CHD1, DDX21, ESF1, GTPBP4, HEATR1, KRR1, MYBBP1A, NOP2, PDCD11, RBM28, RRP12, THOC2, WDR3 |
| GO:BP RNA biosynthetic process | 0.000608 | BOP1, DDX21, ESF1, GTPBP4, HEATR1, INTS8, KRR1, MYBBP1A, NOP2, PDCD11, PLRG1, RBM28, THOC2, WDR3 |
| GO:BP nucleic acid biosynthetic process | 0.000918 | BOP1, DDX21, ESF1, GTPBP4, HEATR1, INTS8, KRR1, MYBBP1A, NOP2, PDCD11, PLRG1, RBM28, THOC2, WDR3 |
| GO:CC nuclear lumen | 0.000997 | BOP1, CHD1, DDX21, ESF1, GTPBP4, HEATR1, INTS8, KRR1, MYBBP1A, NOP2, PDCD11, PLRG1, RBM28, RRP12, THOC2, WDR3 |
| GO:CC preribosome | 0.00113 | BOP1, HEATR1, KRR1, PDCD11, WDR3 |
| GO:BP RNA metabolic process | 0.00151 | BOP1, DDX21, ESF1, GTPBP4, HEATR1, INTS8, KRR1, MYBBP1A, NOP2, PDCD11, PLRG1, RBM28, THOC2, WDR3 |
| GO:BP nucleobase-containing compound biosynthetic process | 0.00361 | BOP1, DDX21, ESF1, GTPBP4, HEATR1, INTS8, KRR1, MYBBP1A, NOP2, PDCD11, PLRG1, RBM28, THOC2, WDR3 |

### STRING and hu.MAP

STRING provides extensive prior knowledge for the core of the module. BOP1, HEATR1, KRR1, PDCD11, WDR3, GTPBP4, NOP2, RBM28, RRP12, DDX21, ESF1, MYBBP1A, and related members form a densely connected known functional neighborhood. STRING functional annotations independently point to preribosome formation, ribosome biogenesis, rRNA processing, RNA processing, and the nucleolus (15 supplementary STRING terms; within-query FDR 2.44e-12–1.59e-06). These are supplementary corroboration rather than globally corrected enrichment evidence. The module therefore largely recapitulates a known molecular machinery rather than revealing an unexplained interaction system. hu.MAP supplies one high-confidence complex overlap, containing CHD1 and RRP12 together with RPS24, WDR74, and RRBP1 (hu.MAP huMAP3_01045.1). The limited hu.MAP overlap does not contradict the module interpretation: hu.MAP complex membership is narrower than functional association, whereas STRING captures extensive functional and experimental relationships. NUP188 and PLRG1 connect the nucleolar RNA program to nuclear transport and splicing-related organization, but their direct STRING support within this module is limited.

**STRING interactions (score >= 0.7)**: 54 of 136 gene pairs: BOP1–DDX21 (0.838); BOP1–GTPBP4 (0.996); BOP1–HEATR1 (0.971); BOP1–KRR1 (0.818); BOP1–MYBBP1A (0.915); BOP1–NOP2 (0.99); BOP1–PDCD11 (0.97); BOP1–RBM28 (0.918); BOP1–RRP12 (0.901); BOP1–WDR3 (0.973); DDX21–GTPBP4 (0.813); DDX21–MYBBP1A (0.963); DDX21–NOP2 (0.761); ESF1–GTPBP4 (0.942); ESF1–HEATR1 (0.884); ESF1–KRR1 (0.957); ESF1–NOP2 (0.823); ESF1–PDCD11 (0.946); ESF1–RBM28 (0.914); ESF1–RRP12 (0.892); ESF1–WDR3 (0.877); GTPBP4–HEATR1 (0.933); GTPBP4–KRR1 (0.771); GTPBP4–NOP2 (0.993); GTPBP4–PDCD11 (0.928); GTPBP4–RBM28 (0.975); GTPBP4–RRP12 (0.981); GTPBP4–WDR3 (0.951); HEATR1–KRR1 (0.998); HEATR1–MYBBP1A (0.973); HEATR1–PDCD11 (0.999); HEATR1–RBM28 (0.793); HEATR1–RRP12 (0.951); HEATR1–WDR3 (0.999); KRR1–MYBBP1A (0.974); KRR1–NOP2 (0.741); KRR1–PDCD11 (0.999); KRR1–RBM28 (0.95); KRR1–RRP12 (0.992); KRR1–WDR3 (0.999); MYBBP1A–NOP2 (0.864); MYBBP1A–PDCD11 (0.949); MYBBP1A–RRP12 (0.846); MYBBP1A–WDR3 (0.878); NOP2–PDCD11 (0.927); NOP2–RBM28 (0.99); NOP2–RRP12 (0.844); NOP2–WDR3 (0.853); PDCD11–RBM28 (0.976); PDCD11–RRP12 (0.984); PDCD11–WDR3 (0.997); RBM28–RRP12 (0.977); RBM28–WDR3 (0.913); RRP12–WDR3 (0.878)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 2.44e-12, 11 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 1.06e-11, 10 genes); Process Ribosome biogenesis (FDR = 3.93e-10, 11 genes); Process rRNA processing (FDR = 7.37e-10, 10 genes); Process RNA processing (FDR = 7.37e-10, 14 genes); Process ncRNA processing (FDR = 3.9e-09, 11 genes); COMPARTMENTS Nucleolus (FDR = 6.8e-09, 12 genes); Component Nucleolus (FDR = 1.62e-08, 13 genes); RCTM rRNA processing in the nucleus and cytosol (FDR = 1.03e-07, 8 genes); NetworkNeighborAL Mixed, incl. Preribosome, large subunit precursor, and Maturation of LSU-rRNA (FDR = 2.46e-07, 6 genes); RCTM Metabolism of RNA (FDR = 4.06e-07, 11 genes); RCTM Major pathway of rRNA processing in the nucleolus and cytosol (FDR = 9.52e-07, 7 genes); Keyword Nucleus (FDR = 1.15e-06, 17 genes); Keyword Ribosome biogenesis (FDR = 1.37e-06, 6 genes); Keyword rRNA processing (FDR = 1.59e-06, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01045.1 (CHD1, RRP12; 2/5)

### Novelty

The biological function of the module is not a new discovery: ribosome biogenesis, preribosome formation, rRNA processing, and nucleolar localization are already well established for many of its genes and are strongly represented in STRING and the literature. The potentially novel aspect is the observation that these genes form a conserved co-abundance module shared between brain and cell line. However, the fact sheet alone does not establish that this cross-tissue co-abundance structure is new, and absence from hu.MAP or from particular STRING links cannot prove novelty. The most defensible conclusion is that this is a biologically credible conserved module that may provide a new systems-level view of coordinated nucleolar regulation, but a formal novelty claim would require comparison with published co-expression modules, tissue compendia, and independent cohorts.

**Hypothesis.** Hypothesis: the module represents a coordinated nucleolar production line in which RNA-binding and RNA-helicase factors help organize precursor rRNA, small- and large-subunit processome components execute rRNA maturation, and nucleolar transport or RNA-export factors help move correctly processed ribonucleoprotein particles through the nucleus. In brain, this program may support the high demand for RNA and ribosome production associated with neuronal maintenance, while in cell lines it may reflect proliferative or biosynthetic demand. The cross-tissue conservation could therefore arise from shared regulation of ribosome output and nucleolar stress responses. This is a mechanistic hypothesis, not a demonstrated causal model; co-abundance does not establish physical interaction, directionality, or tissue-specific regulation.

### Important genes

#### HEATR1

- **Related proteins** (co-abundance neighbors): PDCD11 (0.86), CHD1 (0.81); STRING partners: BOP1 (0.971), ESF1 (0.884), GTPBP4 (0.933), KRR1 (0.998), MYBBP1A (0.973), PDCD11 (0.999), RBM28 (0.793), RRP12 (0.951), WDR3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HEAT repeat containing 1. Enables RNA binding activity. Involved in positive regulation of rRNA processing and positive regulation of transcription by RNA polymerase I. Located in fibrillar center and mitochondrion. Implicated in pancreatic ductal carcinoma. Biomarker of glioblastoma. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.475); Alzheimer disease (0.463); Parkinson disease (0.462); lysosomal storage disease (0.462); musculoskeletal system disorder (0.168)
- **Europe PMC papers**: 342
- **Why important**: HEATR1 is one of the most central functional members of the module because it appears in essentially the full set of primary enrichment themes, including ribosome biogenesis, preribosome formation, the small-subunit processome, rRNA maturation, RNA binding, and RNA polymerase I regulation (13 globally significant GO/KEGG terms, q_global 1.13e-07–0.0437; see the table). It is located in the nucleolar fibrillar center and has strong STRING relationships with the major nucleolar cluster. Its annotation connects it directly to positive regulation of rRNA processing and RNA polymerase I transcription. The literature links it to neural precursor proliferation, neurodegenerative disease, Alzheimer disease, Parkinson disease, and glioblastoma, while its publication volume is substantial.
- **Conclusion**: Established evidence supports HEATR1 as a core nucleolar ribosome-biogenesis factor and a plausible organizing component of this module. Its disease associations make it biologically relevant to brain, but the module does not demonstrate that HEATR1 mediates any particular neurological disease. A role in coordinating tissue-specific ribosome demand remains a hypothesis.

#### PDCD11

- **Related proteins** (co-abundance neighbors): RRP12 (0.86), HEATR1 (0.86), NUP188 (0.85), MYBBP1A (0.83); STRING partners: BOP1 (0.97), ESF1 (0.946), GTPBP4 (0.928), HEATR1 (0.999), KRR1 (0.999), MYBBP1A (0.949), NOP2 (0.927), RBM28 (0.976), RRP12 (0.984), WDR3 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 11. PDCD11 is a NF-kappa-B (NFKB1; 164011)-binding protein that colocalizes with U3 RNA (MIM 180710) in the nucleolus and is required for rRNA maturation and generation of 18S rRNA (Sweet et al., 2003 [PubMed 14624448]; Sweet et al., 2008 [PubMed 17654514]).[supplied by OMIM, Oct 2008].
- **Diseases (Open Targets)**: Back pain (0.277); insomnia (0.216); systemic lupus erythematosus (0.170); neoplasm (0.095); colorectal carcinoma (0.093)
- **Europe PMC papers**: 334
- **Why important**: PDCD11 has a strong position in the module network and is represented across nearly all primary terms, including ribosome biogenesis, rRNA processing, the nucleolus, the preribosome, the small-subunit processome, and ribonucleoprotein complex biogenesis (9 globally significant GO/KEGG terms, q_global 1.13e-07–0.0149; see the table). It is localized at the nucleolar rim and has extensive STRING relationships with the central nucleolar proteins. Gene-level evidence identifies it as an NF-kappa-B-binding protein that colocalizes with U3 RNA and is required for rRNA maturation and generation of eighteen-S rRNA. Its disease associations include systemic lupus erythematosus, insomnia, back pain, and neoplasm.
- **Conclusion**: Established evidence identifies PDCD11 as a functional rRNA maturation factor and a strong molecular anchor for the module. Its position supports participation in the shared nucleolar machinery. The data do not establish that its disease associations arise through this module or that it links inflammatory signaling to ribosome biogenesis in brain.

#### RBM28

- **Related proteins** (co-abundance neighbors): RRP12 (0.85), NOP2 (0.81), ESF1 (0.81), INTS8 (0.80), KRR1 (0.80); STRING partners: BOP1 (0.918), ESF1 (0.914), GTPBP4 (0.975), HEATR1 (0.793), KRR1 (0.95), NOP2 (0.99), PDCD11 (0.976), RRP12 (0.977), WDR3 (0.913)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 28. The protein encoded by this gene is a specific nucleolar component of the spliceosomal small nuclear ribonucleoprotein (snRNP)complexes . It specifically associates with U1, U2, U4, U5, and U6 small nuclear RNAs (snRNAs), possibly coordinating their transition through the nucleolus. Mutation in this gene causes alopecia, progressive neurological defects, and endocrinopathy (ANE syndrome), a pleiot…
- **Diseases (Open Targets)**: ANE syndrome (0.643); neurodegenerative disease (0.472); microcephaly (0.111); cancer (0.076); colorectal carcinoma (0.075)
- **Europe PMC papers**: 337
- **Why important**: RBM28 has the strongest network position in the supplied module topology and connects multiple parts of the co-abundance graph. It is located in nucleoli, participates in the nucleolar and RNA-binding enrichment landscape (15 globally significant GO/KEGG terms, q_global 4.23e-07–0.0149; see the table), and has extensive STRING relationships with BOP1, GTPBP4, KRR1, NOP2, PDCD11, RRP12, and WDR3. Gene-level information describes a nucleolar component associated with spliceosomal small nuclear ribonucleoproteins and RNA handling. Mutation of RBM28 causes ANE syndrome, involving alopecia, progressive neurological defects, and endocrinopathy. It has a substantial literature base.
- **Conclusion**: Established evidence supports RBM28 as a network-central RNA-processing component that may couple nucleolar RNA maturation with broader RNA-protein complex organization. Its neurological disease association increases its relevance to the brain-shared module. Whether its central co-abundance position reflects regulatory control or simply coordinated expression of a common nucleolar program is unresolved.

#### RRP12

- **Related proteins** (co-abundance neighbors): PDCD11 (0.86), RBM28 (0.85), DDX21 (0.83), GTPBP4 (0.82); STRING partners: BOP1 (0.901), ESF1 (0.892), GTPBP4 (0.981), HEATR1 (0.951), KRR1 (0.992), MYBBP1A (0.846), NOP2 (0.844), PDCD11 (0.984), RBM28 (0.977), WDR3 (0.878)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: huMAP3_01045.1
- **Function (MyGene.info)**: ribosomal RNA processing 12 homolog. Enables RNA binding activity. Predicted to be involved in rRNA processing. Located in cytosol; nucleolus; and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.435); bilateral striopallidodentate calcinosis (0.370); colorectal carcinoma (0.079); hepatocellular carcinoma (0.075); neoplasm (0.067)
- **Europe PMC papers**: 367
- **Why important**: RRP12 is a connected nucleolar member of the module and is included in the primary nucleolar, RNA-binding, nucleic-acid-binding, and ribonucleoprotein terms (6 globally significant GO/KEGG terms, q_global 4.23e-07–0.0149; see the table). It is the module member with the clearest HPA enrichment in bone marrow and myeloid or neutrophil-related cell types, making it important for interpreting tissue composition. RRP12 has extensive STRING links to the main ribosome-biogenesis cluster and is the module member represented with CHD1 in the high-confidence hu.MAP complex (hu.MAP huMAP3_01045.1). Gene-level evidence describes a protein predicted to participate in rRNA processing, with associations to neurodegenerative disease and striopallidodentate calcinosis.
- **Conclusion**: Established evidence supports RRP12 as a nucleolar RNA-processing factor embedded in known ribosome-biogenesis relationships. Its HPA profile raises the possibility that some co-abundance signal is influenced by myeloid or neutrophil-related cell states, although the overall module is not blood-cell specific. Its precise causal contribution to the shared brain–cell-line module remains uncertain.

#### BOP1

- **Related proteins** (co-abundance neighbors): WDR3 (0.83); STRING partners: DDX21 (0.838), GTPBP4 (0.996), HEATR1 (0.971), KRR1 (0.818), MYBBP1A (0.915), NOP2 (0.99), PDCD11 (0.97), RBM28 (0.918), RRP12 (0.901), WDR3 (0.973)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BOP1 ribosomal biogenesis factor. Enables RNA binding activity. Involved in regulation of cell cycle; regulation of signal transduction by p53 class mediator; and ribosomal large subunit biogenesis. Located in chromosome; nucleolus; and nucleoplasm. Part of PeBoW complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.318); cancer (0.090); neoplasm (0.087); polycystic ovary syndrome (0.082); colorectal carcinoma (0.078)
- **Europe PMC papers**: 1064
- **Why important**: BOP1 is a recognized ribosomal biogenesis factor and a component of the PeBoW complex. It appears across the primary ribosome-biogenesis, rRNA-processing, preribosome, large-subunit maturation, nucleolar, and ribonucleoprotein terms (10 globally significant GO/KEGG terms, q_global 1.13e-07–0.0271; see the table). It has particularly broad STRING connectivity to the module’s nucleolar proteins and is detected in brain by HPA. Its gene-level annotation directly supports large-subunit assembly, maturation of five-point-eight-S and large-subunit rRNA, and rRNA processing. BOP1 has the largest literature volume among the selected core factors and is associated with neurodegenerative disease, cancer, and neoplasm.
- **Conclusion**: Established evidence makes BOP1 a strong marker of the large-subunit branch of the module’s ribosome-biogenesis program. Its network and annotation profile support a core mechanistic role, but co-abundance does not show that BOP1 controls the other genes or that its disease associations are mediated through this module.
