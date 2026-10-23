# Conserved co-abundance modules: rectum and stem_cells

## Module 0

**Tissue pair**: rectum and stem_cells  
**Genes (16)**: BZW2, ATG5, EIF2AK2, FKBP9, FUCA2, LIPA, MAN2A1, MAIP1, NQO1, NUP214, PPIC, PSMA4, PSMD13, MRPS31, TPD52L2, UFSP2

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING functional enrichment. The gene annotations nevertheless suggest a mixed cellular maintenance program involving proteostasis, protein quality control, organelle function, lysosomal and glycan metabolism, oxidative-stress handling, nucleocytoplasmic transport, and autophagy. The network is sparse and appears to contain several functionally distinct branches rather than a single established pathway. The strongest directly supported interaction is the proteasome relationship between PSMA4 and PSMD13, while other links are co-abundance relationships without corresponding STRING support. Thus, the most defensible interpretation is a conserved cellular stress, protein-turnover, and organelle-homeostasis module, with possible contributions from epithelial, stromal, trophoblast-like, and myeloid-related cell states. The absence of globally significant enrichment does not invalidate the module; it limits the strength of pathway-level claims.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. FUCA2 is secreted to blood, whereas LIPA, FKBP9, and PPIC have intracellular or membrane-associated secretome annotations; the remaining genes are not annotated as secreted. Most genes have low tissue specificity, and nearly all show some degree of cell-type enhancement, including trophoblast-like, glial, epithelial, stromal, and reproductive cell types. Blood-cell specificity is generally low, although LIPA and NUP214 show monocyte or myeloid-related enrichment and FKBP9 is immune-cell enhanced. HPA protein detection is broad in rectum for the detected genes, while there is no matching HPA tissue category for stem_cells. These observations argue against interpreting the module as a blood-protein signature, but they leave open the possibility that shared cell composition or a broadly expressed cellular state contributes to the cross-tissue association.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides direct support for the PSMA4–PSMD13 relationship, linking a proteasome core subunit with a proteasome regulatory subunit. This is consistent with a genuine proteasome component embedded in the co-abundance network. No other module pair has a high-confidence STRING interaction in the supplied evidence, and STRING reports no functional enrichment. hu.MAP independently places MAN2A1 and FUCA2 together in C1, C2, and C5, supporting a possible glycan-processing or lysosomal-associated relationship. hu.MAP also places PSMA4 and PSMD13 together in C3 and C4, strongly supporting their membership in proteasome complexes. However, each hu.MAP complex contains many proteins beyond the module, so these findings validate selected local relationships rather than the entire module as one physical complex. The remaining co-abundance edges should be treated as tissue- or cell-state associations until experimentally validated.

**STRING interactions (score >= 0.7)**: 1 of 120 gene pairs: PSMA4–PSMD13 (0.998)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08802.1 (MAN2A1, FUCA2; 2/33); huMAP3_06775.1 (MAN2A1, FUCA2; 2/60); huMAP3_09656.1 (PSMA4, PSMD13; 2/64); huMAP3_13725.1 (PSMA4, PSMD13; 2/69); huMAP3_09327.1 (MAN2A1, FUCA2; 2/93)

### Novelty

This may be a new cross-tissue co-abundance observation, but the module cannot be called a newly discovered molecular complex or pathway. The PSMA4–PSMD13 relationship is already known through STRING and hu.MAP, and the MAN2A1–FUCA2 pairing is represented in several hu.MAP complexes. The lack of STRING support for most other edges and the absence of globally significant GO or KEGG enrichment make the broader biological interpretation provisional. A reasonable novelty claim is therefore that this particular conserved co-abundance pattern across rectum and stem_cells, including its combination of proteasome, mitochondrial, lysosomal, glycan, autophagy, and stress-related genes, may be under-described. Establishing novelty would require comparison with published tissue co-expression modules, independent cohorts, cell-composition correction, and experimental testing; absence from the supplied databases alone is not evidence of novelty.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular quality-control state shared by cells present in rectum and stem_cells. In this model, autophagy through ATG5, proteasomal degradation through PSMA4 and PSMD13, oxidative-stress defense through NQO1, mitochondrial protein synthesis through MRPS31 and mitochondrial maintenance through MAIP1, and lysosomal or glycan processing through LIPA, MAN2A1, and FUCA2 act as partially connected arms of a response to protein, organelle, and metabolic stress. BZW2, EIF2AK2, UFSP2, and NUP214 could connect translational control, innate-stress signaling, ubiquitin-like modification, and nucleocytoplasmic transport. This is a mechanistic hypothesis rather than an established pathway, because the module lacks globally significant enrichment and most edges lack external interaction support.

### Important genes

#### ATG5

- **Related proteins** (co-abundance neighbors): TPD52L2 (0.87), MAN2A1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Primary cilium transition zone, Centrosome, Basal body; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: autophagy related 5. The protein encoded by this gene, in combination with autophagy protein 12, functions as an E1-like activating enzyme in a ubiquitin-like conjugating system. The encoded protein is involved in several cellular processes, including autophagic vesicle formation, mitochondrial quality control after oxidative damage, negative regulation of the innate antiviral immune response, lymphocyte development a…
- **Diseases (Open Targets)**: neurodegenerative disease (0.557); rheumatoid arthritis (0.366); asthma (0.353); systemic lupus erythematosus (0.328); plasma cell myeloma (0.293)
- **Europe PMC papers**: 26318
- **Why important**: ATG5 is a central autophagy and mitophagy factor and has one of the stronger local connections in the module, linking TPD52L2 with MAN2A1. Its annotation connects autophagosome formation, mitochondrial quality control, immune regulation, lymphocyte biology, and apoptosis. It also has extensive literature and disease associations spanning neurodegenerative, autoimmune, respiratory, and plasma-cell disorders, making it a biologically informative anchor for interpreting the module.
- **Conclusion**: Established evidence supports ATG5 as an autophagy and organelle-quality-control gene. Its co-abundance with TPD52L2 and MAN2A1 is compatible with coordinated vesicle, lysosomal, and glycan-related biology, but the module does not establish that ATG5 directly regulates either partner. Its role as a quality-control component is well supported; its role as a driver of this cross-tissue module remains hypothetical.

#### PSMD13

- **Related proteins** (co-abundance neighbors): FUCA2 (0.87), BZW2 (0.82); STRING partners: PSMA4 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 is directly connected to PSMA4 by the strongest STRING relationship supplied and both genes occur together in hu.MAP proteasome complexes C3 and C4. PSMD13 is annotated in ubiquitin-dependent proteolysis, oxidative-stress response, and type-I-interferon-related biology. Its position also links FUCA2 and BZW2 in the co-abundance network, making it a bridge between the validated proteasome signal and less well-established module branches.
- **Conclusion**: Established evidence supports PSMD13 as a proteasome-associated component and supports its physical relationship with PSMA4. Its broader links to FUCA2 and BZW2 are co-abundance observations rather than established physical interactions. PSMD13 is therefore a strong marker of the module’s proteostasis arm, but not proof that the whole module is a proteasome pathway.

#### LIPA

- **Related proteins** (co-abundance neighbors): BZW2 (0.88), PSMA4 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lipase A, lysosomal acid type. This gene encodes lipase A, the lysosomal acid lipase (also known as cholesterol ester hydrolase). This enzyme functions in the lysosome to catalyze the hydrolysis of cholesteryl esters and triglycerides. Mutations in this gene can result in Wolman disease and cholesteryl ester storage disease. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jan 2014].
- **Diseases (Open Targets)**: cholesteryl ester storage disease (0.818); Wolman disease (0.803); lysosomal acid lipase deficiency (0.754); coronary artery disorder (0.563); myocardial infarction (0.523)
- **Europe PMC papers**: 6860
- **Why important**: LIPA has a high local network position through BZW2 and PSMA4 and encodes lysosomal acid lipase, which hydrolyzes cholesteryl esters and triglycerides. HPA associates it with lymphoid tissue, macrophage-lineage and monocyte-related cell types, and vesicular or cytosolic localization. Its disease associations with lysosomal acid lipase deficiency, Wolman disease, lipid storage, and cardiovascular disease give it strong functional and clinical relevance.
- **Conclusion**: Established evidence supports LIPA as a lysosomal lipid-metabolism enzyme and indicates a possible myeloid or macrophage contribution to its abundance. Its connection to the proteasome-associated branch is not independently established. LIPA could report a lipid-handling or immune-cell component of the module, but a direct mechanistic bridge to PSMA4 or BZW2 remains a hypothesis.

#### NQO1

- **Related proteins** (co-abundance neighbors): MRPS31 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NAD(P)H quinone dehydrogenase 1. This gene is a member of the NAD(P)H dehydrogenase (quinone) family and encodes a cytoplasmic 2-electron reductase. This FAD-binding protein forms homodimers and reduces quinones to hydroquinones. This protein's enzymatic activity prevents the one electron reduction of quinones that results in the production of radical species. Mutations in this gene have been associated with tardive dyskinesia (T…
- **Diseases (Open Targets)**: neurodegenerative disease (0.543); gastric cancer (0.354); Friedreich ataxia (0.325); mitochondrial disease (0.312); immunodeficiency disease (0.194)
- **Europe PMC papers**: 20515
- **Why important**: NQO1 connects to MRPS31 and is a well-studied cytosolic reductase involved in quinone metabolism and protection from radical formation. Its annotations include oxidative-stress response and xenobiotic metabolism, and HPA shows enhancement in gastrointestinal epithelial cell types relevant to the rectal context. Its literature is extensive and includes cancer, mitochondrial, toxicant, and neurodegenerative disease contexts.
- **Conclusion**: Established evidence supports NQO1 as an oxidative-stress and quinone-detoxification factor. Its association with MRPS31 may indicate coordination between redox protection and mitochondrial protein synthesis, but this is not demonstrated as a direct interaction. NQO1 is therefore a useful indicator of cellular stress biology within the module, not evidence for a specific disease mechanism.

#### MAN2A1

- **Related proteins** (co-abundance neighbors): ATG5 (0.85), NUP214 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Golgi apparatus; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_08802.1, huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: mannosidase alpha class 2A member 1. This gene encodes a glycosyl hydrolase that localizes to the Golgi and catalyzes the final hydrolytic step in the asparagine-linked oligosaccharide (N-glycan) maturation pathway. Mutations in the mouse homolog of this gene have been shown to cause a systemic autoimmune disease similar to human systemic lupus erythematosus. [provided by RefSeq, Dec 2013].
- **Diseases (Open Targets)**: alcohol drinking (0.456); schizophrenia (0.455); COVID-19 (0.370); smoking initiation (0.364); dislocation (0.344)
- **Europe PMC papers**: 663
- **Why important**: MAN2A1 is a Golgi glycosyl hydrolase involved in N-glycan maturation and is connected to ATG5 and NUP214 in the module. It is independently represented with FUCA2 in hu.MAP complexes C1, C2, and C5, providing the clearest external support for a glycan-processing branch. Its Golgi localization and annotation in carbohydrate and mannose metabolism complement the lysosomal and secretory biology represented elsewhere in the module.
- **Conclusion**: Established evidence supports MAN2A1 as a Golgi N-glycan-processing enzyme and supports its complex-level association with FUCA2. Its co-abundance with ATG5 and NUP214 may reflect coordinated trafficking, stress, or cell-state regulation, but direct functional coupling is unproven. MAN2A1 is a strong marker of the module’s glycan-processing component.

## Module 1

**Tissue pair**: rectum and stem_cells  
**Genes (38)**: ABCF1, ADGRE5, ALDH1A2, ANXA3, CDK5RAP3, CNPY3, COG2, CTBP2, DNAAF5, DDX46, DSP, EXD2, FLOT1, FXN, TUBGCP2, GFPT1, CD74, EIF4E, NDUFA10, NOP2, NUP43, PARP4, PES1, PKP2, RPP30, SFXN3, SPATS2L, SPTAN1, SRRT, SUMF2, SUN2, DARS1, TM9SF2, TMOD3, TOMM40, VIL1, WDR43, TJP1

### Function

No GO or KEGG term passed global correction. The module therefore does not support a single statistically established pathway assignment. Its gene content suggests a mixed epithelial and cellular-organization program, with contributions from desmosomal and junctional architecture (DSP, PKP2, TJP1, VIL1), RNA processing and ribosome production (NOP2, PES1, WDR43, RPP30, DDX46), translation and metabolic support (EIF4E, DARS1, GFPT1), vesicle and membrane organization, and mitochondrial functions. The co-abundance graph is sparse and connects these themes through a limited set of bridges, so the most defensible interpretation is a shared tissue or cell-state program rather than a confirmed unified biochemical pathway. The presence of VIL1 and its enteric stem-cell annotation supports an intestinal epithelial component, while the junctional genes support epithelial integrity and polarity.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: only a minority of genes are annotated as secreted, and most genes have low tissue specificity. Protein detection in rectum is broad, whereas there is no matching HPA tissue for stem_cells, so the HPA evidence does not establish equivalent protein expression in both tissues. The module nevertheless contains mixed cell-type signals, including epithelial, stem or progenitor, germ-cell, endothelial, and immune-associated annotations. Neutrophil and other blood-cell signals occur for several genes, and CD74, ADGRE5, and ANXA3 provide particularly plausible immune or blood-derived contributions. Thus, shared abundance may partly reflect common cell populations or sample composition, including epithelial cells and infiltrating or resident immune cells, rather than a program intrinsic to every stem cell.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a small set of high-confidence relationships rather than broad network connectivity. The established relationships include DSP with PKP2 and TJP1, NOP2 with PES1 and WDR43, and CD74 with WDR43. These links validate a desmosomal or junctional component and a nucleolar ribosome-biogenesis component, but they do not demonstrate that the full module is one physical complex. The hu.MAP evidence is limited to (hu.MAP huMAP3_09165.1), where FLOT1 and SPTAN1 occur together in a larger membrane-cytoskeleton complex. Most module genes have no listed hu.MAP complex membership and most co-abundance edges are not supported by the supplied STRING interactions. Accordingly, the network is best viewed as a tissue-level correlation structure containing several known molecular neighborhoods, not as a validated macromolecular complex.

**STRING interactions (score >= 0.7)**: 6 of 703 gene pairs: CD74–WDR43 (0.799); DSP–PKP2 (0.999); DSP–TJP1 (0.853); NOP2–PES1 (0.983); NOP2–WDR43 (0.757); PES1–WDR43 (0.885)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09165.1 (FLOT1, SPTAN1; 2/39)

### Novelty

The module may represent a previously unreported co-abundance pattern shared by rectum and stem_cells, but the supplied evidence is insufficient to call it a new biological mechanism. Its component processes and several pairwise relationships are already well established, especially desmosomal junctions, tight-junction organization, translation, and ribosome biogenesis. The absence of a globally enriched GO or KEGG term and the limited STRING and hu.MAP support argue against claiming a novel pathway. Conversely, absence from those resources does not prove that the co-abundance pattern is novel, because database coverage and tissue-specific correlation structure are incomplete. Novelty would require replication in independent cohorts, control for cell composition, and comparison with published tissue co-expression modules.

**Hypothesis.** Hypothesis: the shared module reflects coordinated maintenance of an epithelial or epithelial-progenitor state that couples cell-cell junction and cytoskeletal integrity with the biosynthetic capacity needed for renewal. In this model, DSP, PKP2, TJP1, and VIL1 maintain epithelial architecture and polarity, while NOP2 and PES1 support ribosome production during proliferation or repair. CD74 and ADGRE5 may indicate an immune-cell or blood-derived overlay that is correlated with the same samples rather than mechanistically part of the epithelial program. This hypothesis should be tested by single-cell deconvolution, spatial localization, perturbation of junctional genes, and independent replication in rectum and stem-cell datasets.

### Important genes

#### DSP

- **Related proteins** (co-abundance neighbors): ALDH1A2 (0.85), VIL1 (0.82), ADGRE5 (0.81); STRING partners: PKP2 (0.999), TJP1 (0.853)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cell Junctions; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: desmoplakin. This gene encodes a protein that anchors intermediate filaments to desmosomal plaques and forms an obligate component of functional desmosomes. Mutations in this gene are the cause of several cardiomyopathies and keratodermas, including skin fragility-woolly hair syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016].
- **Diseases (Open Targets)**: arrhythmogenic cardiomyopathy with wooly hair and keratoderma (0.841); arrhythmogenic right ventricular dysplasia 8 (0.812); arrhythmogenic right ventricular cardiomyopathy (0.760); lethal acantholytic epidermolysis bullosa (0.745); cardiomyopathy, dilated, with wooly hair, keratoderma, and tooth agenesis (0.741)
- **Europe PMC papers**: 17350
- **Why important**: DSP is a central representative of the junctional branch: it is annotated as an obligate desmosomal component, is localized to cell junctions, and has STRING relationships with PKP2 and TJP1. It is tissue-enhanced in epithelial tissues relevant to barrier biology, is detected in rectum, and has extensive disease and literature support involving cardiomyopathy, keratoderma, and epithelial fragility.
- **Conclusion**: Established evidence supports DSP as a structural epithelial-junction gene and as an anchor for the module's barrier or adhesion interpretation. It is not established that DSP drives the entire shared module; its co-abundance with biosynthetic genes remains an association. Hypothesis: DSP marks the epithelial structural state that links the module to tissue integrity.

#### PKP2

- **Related proteins** (co-abundance neighbors): WDR43 (0.84), EIF4E (0.84), DARS1 (0.81), ADGRE5 (0.80); STRING partners: DSP (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cell Junctions; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plakophilin 2. This gene encodes a member of the arm-repeat (armadillo) and plakophilin gene families. Plakophilin proteins contain numerous armadillo repeats, localize to cell desmosomes and nuclei, and participate in linking cadherins to intermediate filaments in the cytoskeleton. This gene may regulate the signaling activity of beta-catenin and is required to maintain transcription of genes that control intra…
- **Diseases (Open Targets)**: arrhythmogenic right ventricular cardiomyopathy (0.837); cardiomyopathy (0.606); Abnormality of the cardiovascular system (0.573); familial isolated arrhythmogenic right ventricular dysplasia (0.547); atrial fibrillation (0.514)
- **Europe PMC papers**: 2981
- **Why important**: PKP2 is a desmosomal plakophilin that links cadherin-associated structures to intermediate filaments and can influence cell signaling. It has a strong STRING relationship with DSP, is localized to cell junctions, and occupies a prominent position in the co-abundance network. Its disease associations with arrhythmogenic cardiomyopathy provide strong evidence that altered junctional organization has major physiological consequences.
- **Conclusion**: Established evidence supports PKP2 as a key junctional and cytoskeletal component, reinforcing the epithelial-architecture interpretation. The module does not establish a cardiac function in rectum or stem_cells, and the heart annotation should not be transferred directly to these tissues. Hypothesis: PKP2 co-abundance reflects shared requirements for stable cell-cell adhesion.

#### VIL1

- **Related proteins** (co-abundance neighbors): DSP (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: villin 1. This gene encodes a member of a family of calcium-regulated actin-binding proteins.  This protein represents a dominant part of the brush border cytoskeleton which functions in the capping, severing, and bundling of actin filaments.  Two mRNAs of 2.7 kb and 3.5 kb have been observed; they result from utilization of alternate poly-adenylation signals present in the terminal exon. [provided by RefSe…
- **Diseases (Open Targets)**: brain aneurysm (0.220); Barrett esophagus (0.084); neoplasm (0.067); cervical adenocarcinoma (0.061); esophageal adenocarcinoma (0.057)
- **Europe PMC papers**: 1564
- **Why important**: VIL1 is the most tissue-specific epithelial marker among the selected genes: it is tissue-enriched in intestine and cell-type enhanced in colonocytes, enterocytes, and enteric stem cells. It organizes, caps, severs, and bundles actin in the brush-border cytoskeleton, is detected in rectum, and is connected to DSP in the module. These properties directly connect epithelial polarity, actin organization, and the stem-cell tissue context.
- **Conclusion**: Established evidence supports VIL1 as evidence for an intestinal epithelial and progenitor-associated component. It does not by itself prove that all module genes operate in enteric stem cells, because the module may contain multiple cell populations. Hypothesis: VIL1 helps identify the epithelial structural subprogram underlying the shared rectum and stem-cell signal.

#### NOP2

- **Related proteins** (co-abundance neighbors): EIF4E (0.88), PES1 (0.82), PARP4 (0.82); STRING partners: PES1 (0.983), WDR43 (0.757)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP2 nucleolar protein. Enables RNA binding activity. Involved in positive regulation of cell population proliferation; regulation of signal transduction by p53 class mediator; and ribosomal large subunit assembly. Located in nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.273); nonpapillary renal cell carcinoma (0.097); neoplasm (0.097); cancer (0.091); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 2120
- **Why important**: NOP2 represents the nucleolar biosynthetic branch. It participates in ribosomal large-subunit assembly and rRNA maturation, is localized to nucleoli, and is connected in STRING to PES1 and WDR43. It also has substantial literature and cancer or proliferation associations, making it a plausible marker of cells with active growth and protein-production demands.
- **Conclusion**: Established evidence supports NOP2 as a ribosome-biogenesis and proliferation-related gene, and the STRING relationships support a real nucleolar neighborhood within the module. The module does not demonstrate that ribosome biogenesis is globally enriched or that NOP2 causes the shared tissue pattern. Hypothesis: NOP2 reflects biosynthetic demand associated with epithelial renewal or progenitor activity.

#### CD74

- **Related proteins** (co-abundance neighbors): PES1 (0.84), DNAAF5 (0.83); STRING partners: WDR43 (0.799)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Golgi apparatus; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD74 molecule. The protein encoded by this gene associates with class II major histocompatibility complex (MHC) and is an important chaperone that regulates antigen presentation for immune response. It also serves as cell surface receptor for the cytokine macrophage migration inhibitory factor (MIF) which, when bound to the encoded protein, initiates survival pathways and cell proliferation. This protein also in…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.626); neoplasm (0.400); cancer (0.394); lung adenocarcinoma (0.379); squamous cell lung carcinoma (0.376)
- **Europe PMC papers**: 17433
- **Why important**: CD74 is important because it may explain part of the module's composition rather than because it defines the epithelial core. It is a class-II MHC-associated chaperone involved in antigen presentation and immune signaling, is enhanced in lymphoid and several antigen-presenting cell types, is secreted to blood, and has STRING relationships with WDR43 and PES1. Its rectum detection and immune-cell annotations make it a useful indicator of immune or blood-cell admixture.
- **Conclusion**: Established evidence supports CD74 as an immune-associated antigen-presentation gene and as a warning that sample composition may contribute to the shared module. Its relationship to the nucleolar genes is not sufficient to infer a common immune-ribosome complex. Hypothesis: CD74 marks an immune-cell overlay that is co-abundant with the epithelial or regenerative state in the sampled tissues.

## Module 2

**Tissue pair**: rectum and stem_cells  
**Genes (16)**: ACSL3, PYCARD, CWF19L1, DNM1L, LMCD1, METAP1, MEAK7, NRDC, NUDT4, PSMG1, POLR1C, RUFY1, TUBA1C, TBC1D15, ATP6V1C1, XPO1

### Function

No GO or KEGG term passed global correction, so the module has no statistically established pathway annotation. Gene-level evidence instead supports a heterogeneous intracellular maintenance program involving nuclear export through XPO1, transcriptional and RNA-related functions through POLR1C, cytoskeletal organization through TUBA1C, endosomal trafficking through RUFY1 and TBC1D15, vesicle acidification through ATP6V1C1, TOR-associated lysosomal regulation through MEAK7, lipid handling through ACSL3, organelle remodeling through DNM1L, and innate immune signaling through PYCARD. These annotations support a broad cellular homeostasis interpretation rather than a single demonstrated pathway. The network is fragmented into several local connections, and STRING reports no functional-enrichment result. Therefore, the module should not be assigned a specific pathway function on the basis of enrichment.

**Cell composition.** The module is not dominated by plasma or secreted proteins: HPA reports no secreted genes. It is also not broadly blood-cell specific, because most genes have low immune-cell specificity. However, PYCARD is enriched across multiple myeloid and related immune-cell populations, and several genes show enhanced expression in neutrophils. Additional HPA signals involve esophageal epithelial cells, muscle and vascular-associated cells, platelets, cardiomyocytes, and germ-cell populations. Most genes have low tissue specificity, consistent with broadly expressed intracellular machinery. The shared signal may therefore reflect common cellular programs, shared epithelial or stromal populations, immune-cell admixture, or a combination of these. Protein detection is broadly supported in rectum, whereas there is no matching HPA tissue for stem_cells, so tissue-level protein evidence for that comparison is unavailable.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship is ATP6V1C1 with MEAK7. This supports a known connection between vacuolar ATPase-associated compartment acidification and an mTOR-associated protein, but it covers only a small part of the module. hu.MAP complex C1 contains XPO1 and ACSL3 among many additional complex members, providing contextual support for their participation in a larger assembly but not evidence that the entire module is one complex. Most co-abundance relationships lack independent STRING or hu.MAP support. The module is therefore better interpreted as coordinated abundance of several cellular subsystems than as a confirmed physical complex.

**STRING interactions (score >= 0.7)**: 1 of 120 gene pairs: ATP6V1C1–MEAK7 (0.925)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09592.1 (XPO1, ACSL3; 2/95)

### Novelty

The shared co-abundance pattern may be a new tissue-pair observation, but the available evidence does not establish a new molecular mechanism. The ATP6V1C1–MEAK7 relationship is already represented in STRING, and XPO1 and ACSL3 occur together in hu.MAP complex C1. Lack of database support for the remaining relationships does not prove novelty because interaction resources are incomplete and co-abundance does not necessarily indicate direct binding. The absence of globally significant enrichment and the fragmented topology further require caution. Establishing novelty would require replication in independent samples, comparison with published co-expression data, and experimental testing of the proposed relationships.

**Hypothesis.** Hypothesis: the module may represent a shared intracellular stress-and-maintenance state rather than a single pathway. Coordinated abundance of XPO1, POLR1C, TUBA1C, ATP6V1C1, MEAK7, RUFY1, ACSL3, and DNM1L could link nuclear transport, transcriptional support, cytoskeletal organization, endosomal or lysosomal acidification, lipid handling, and organelle remodeling. PYCARD may add an inflammatory or innate-immune component, potentially reflecting myeloid-cell admixture or epithelial stress responses. This remains a hypothesis: the co-abundance data cannot distinguish regulation within cells from differences in cellular composition, and enrichment analysis does not establish the proposed mechanism.

### Important genes

#### XPO1

- **Related proteins** (co-abundance neighbors): NRDC (0.90), NUDT4 (0.88), PSMG1 (0.87), TUBA1C (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: exportin 1. This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSe…
- **Diseases (Open Targets)**: plasma cell myeloma (0.642); B-cell chronic lymphocytic leukemia (0.626); diffuse large B-cell lymphoma (0.602); HIV infectious disease (0.561); neurodegenerative disease (0.522)
- **Europe PMC papers**: 5357
- **Why important**: XPO1 has the strongest network position and connects to NRDC, NUDT4, PSMG1, and TUBA1C. Its established role in nuclear export provides a plausible link between nuclear, RNA-related, and broader cellular processes. It is broadly expressed, detected in rectum, associated with hematologic disease and HIV-related disease in Open Targets, and has extensive literature coverage.
- **Conclusion**: Established evidence supports XPO1 as the principal network hub and a nuclear-export component. Its central position makes it an important candidate for coordinating the module, but the module does not demonstrate that XPO1 regulates its neighbors or that the shared signal is disease-related.

#### ATP6V1C1

- **Related proteins** (co-abundance neighbors): ACSL3 (0.81), TUBA1C (0.81), POLR1C (0.81), METAP1 (0.80); STRING partners: MEAK7 (0.925)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase H+ transporting V1 subunit C1. This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of intracellular compartments of eukaryotic cells. V-ATPase dependent acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 …
- **Diseases (Open Targets)**: neurodegenerative disease (0.565); Alzheimer disease (0.503); lysosomal storage disease (0.502); Parkinson disease (0.502); DOORS syndrome (0.344)
- **Europe PMC papers**: 711
- **Why important**: ATP6V1C1 is highly connected within the module, linking ACSL3, TUBA1C, POLR1C, and METAP1. Its established role as a V-ATPase subunit connects it to intracellular compartment acidification, protein sorting, receptor-mediated endocytosis, and lysosomal biology. It also forms the only high-confidence STRING relationship, with MEAK7.
- **Conclusion**: Established evidence supports ATP6V1C1 as a major vesicle-acidification and intracellular-trafficking component. Its relationship with MEAK7 strengthens this interpretation, but the co-abundance network does not demonstrate direct functional interaction with all of its neighbors.

#### PYCARD

- **Related proteins** (co-abundance neighbors): RUFY1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PYD and CARD domain containing. This gene encodes an adaptor protein that is composed of two protein-protein interaction domains: a N-terminal PYRIN-PAAD-DAPIN domain (PYD) and a C-terminal caspase-recruitment domain (CARD). The PYD and CARD domains are members of the six-helix bundle death domain-fold superfamily that mediates assembly of large signaling complexes in the inflammatory and apoptotic signaling pathways via the act…
- **Diseases (Open Targets)**: severe acute respiratory syndrome (0.370); neoplasm (0.086); Alzheimer disease (0.086); prostate cancer (0.085); Familial prostate cancer (0.085)
- **Europe PMC papers**: 3928
- **Why important**: PYCARD is the clearest immune-associated gene in the module. Its PYD and CARD domains support assembly of inflammatory signaling complexes, and its annotations include innate immune activation, pattern-recognition signaling, and myeloid dendritic-cell activation. HPA shows enrichment across multiple myeloid and related immune populations, while its network connection to RUFY1 places immune signaling near vesicular trafficking.
- **Conclusion**: Established evidence supports PYCARD as an innate-immune and inflammation-related component and a possible indicator of immune-cell composition in rectum samples. It does not establish that the full module is an inflammasome module because there is no globally significant enrichment or broad direct-interaction support.

#### DNM1L

- **Related proteins** (co-abundance neighbors): NUDT4 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 1L. This gene encodes a member of the dynamin superfamily of GTPases. The encoded protein mediates mitochondrial and peroxisomal division, and is involved in developmentally regulated apoptosis and programmed necrosis. Dysfunction of this gene is implicated in several neurological disorders, including Alzheimer's disease. Mutations in this gene are associated with the autosomal dominant disorder, ence…
- **Diseases (Open Targets)**: encephalopathy, lethal, due to defective mitochondrial peroxisomal fission 1 (0.815); autosomal dominant optic atrophy, classic form (0.721); neurodegenerative disease (0.531); encephalopathy due to mitochondrial and peroxisomal fission defect (0.455); hereditary disease (0.451)
- **Europe PMC papers**: 3015
- **Why important**: DNM1L connects to NUDT4 and has an established role in mitochondrial and peroxisomal fission, organelle organization, and apoptosis-related remodeling. Its disease associations include disorders caused by defective mitochondrial and peroxisomal fission and optic atrophy, and it has substantial literature coverage. It is therefore an informative marker of organelle maintenance in an otherwise fragmented network.
- **Conclusion**: Established evidence supports DNM1L as a mitochondrial and peroxisomal dynamics component. Its presence is compatible with a cellular-maintenance or stress hypothesis, but the module does not establish that organelle fission is its dominant shared function.

#### ACSL3

- **Related proteins** (co-abundance neighbors): ATP6V1C1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 3. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme is highly expressed…
- **Diseases (Open Targets)**: prostate adenocarcinoma (0.370); acute myeloid leukemia (0.313); neurodegenerative disease (0.300); ovarian dysfunction (0.253); Abnormality of the skeletal system (0.215)
- **Europe PMC papers**: 2930
- **Why important**: ACSL3 provides the clearest lipid-metabolism interpretation in the module and connects to ATP6V1C1. It activates long-chain fatty acids for lipid biosynthesis and degradation and occurs with XPO1 in hu.MAP complex C1. Its annotations include parathyroid and neutrophil-associated expression, and it has substantial literature coverage and disease associations.
- **Conclusion**: Established evidence supports ACSL3 as a lipid-handling component, with limited external support from hu.MAP complex C1. Its co-abundance with trafficking and acidification genes suggests a possible connection between lipid metabolism and intracellular membrane processes, but that connection remains hypothetical.

## Module 3

**Tissue pair**: rectum and stem_cells  
**Genes (23)**: AGPS, AFDN, CHORDC1, COPG2, CYP51A1, CPSF2, COPS7B, LIG3, DSC2, GARS1, GMPS, HEATR1, KPNA2, MGST1, NOLC1, NUP50, PFDN6, PUM3, GART, RCC1, SRPK1, YARS1, TTLL12

### Function

This is a heterogeneous co-abundance module rather than a cleanly defined pathway module. No GO/KEGG term passed global correction, and STRING reported no functional enrichment, so no pathway should be treated as statistically established for the module as a whole. The gene-level evidence instead suggests coordinated cellular infrastructure involving purine nucleotide production through GART and GMPS, protein translation through GARS1 and YARS1, nuclear import and nucleocytoplasmic organization through KPNA2, NUP50 and RCC1, RNA and ribosome-related processes through HEATR1, NOLC1 and PUM3, protein folding and regulation through CHORDC1 and PFDN6, and epithelial adhesion through AFDN and DSC2. The most defensible interpretation is a shared cellular-state module linking biosynthetic capacity, nuclear and cell-cycle organization, and epithelial structural functions, rather than a single specialized biochemical pathway.

**Cell composition.** The module is predominantly intracellular and broadly distributed rather than plasma-derived or secreted. Only one gene is annotated as secreted, while the great majority have low immune-cell specificity and many have low tissue specificity. Protein detection in rectum is widespread among the genes with available HPA evidence, whereas there is no matching HPA tissue for stem_cells, so cross-tissue protein confirmation is not possible. Several genes show cell-type enhancement in epithelial, reproductive, cardiac, neural or metabolic cell types, including esophageal apical cells, spermatogenic cells and epicardial cells. A small subset has blood-cell enrichment, notably MGST1, DSC2 and SRPK1, but the overall profile does not support a blood-cell or plasma-protein explanation. The shared module may therefore reflect common epithelial or proliferative cellular states, with possible contributions from the mixture of cell types in the samples.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited set of high-confidence pairwise relationships: GARS1 with YARS1, GART with GMPS, HEATR1 with PUM3, and the nuclear-transport or nuclear-organization relationships KPNA2 with NUP50, KPNA2 with RCC1, and NUP50 with RCC1. These links provide direct support for translation-related, purine-related and nuclear-transport substructures, but most co-abundance edges are not independently supported by STRING. hu.MAP provides stronger complex-level support. (hu.MAP huMAP3_14442.1) places GARS1, GMPS, YARS1 and CHORDC1 in a shared complex context, while (hu.MAP huMAP3_10000.1) and (hu.MAP huMAP3_12581.1) both support the RCC1-KPNA2-NUP50 nuclear organization group. (hu.MAP huMAP3_07479.1) also supports the KPNA2-NUP50 pair in a smaller transport-related complex. Thus, part of the module recovers known molecular machinery, while the remaining edges may represent indirect regulation, shared expression state, tissue composition or condition-dependent coordination.

**STRING interactions (score >= 0.7)**: 6 of 253 gene pairs: GARS1–YARS1 (0.989); GART–GMPS (0.937); HEATR1–PUM3 (0.837); KPNA2–NUP50 (0.921); KPNA2–RCC1 (0.888); NUP50–RCC1 (0.75)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (GARS1, GMPS, YARS1, CHORDC1; 4/57); huMAP3_10000.1 (RCC1, KPNA2, NUP50; 3/44); huMAP3_12581.1 (RCC1, KPNA2, NUP50; 3/58); huMAP3_07479.1 (KPNA2, NUP50; 2/6)

### Novelty

The module should not be claimed as a newly discovered molecular complex or pathway. Several of its strongest relationships are already represented in STRING or hu.MAP, especially the GARS1-YARS1, GART-GMPS and KPNA2-NUP50-RCC1 structures. The potentially new aspect is the co-abundance configuration linking these known substructures with epithelial junction, lipid, chaperone, RNA-processing and vesicle-trafficking genes in the shared rectum and stem_cells context. However, database absence for individual edges does not prove novelty, and the lack of globally significant GO/KEGG enrichment prevents a pathway-level novelty claim. The appropriate conclusion is that this is a context-specific association pattern that merits validation, not an established new biological entity.

**Hypothesis.** Hypothesis: the module reflects a shared epithelial or progenitor-like cellular state in which increased biosynthetic and proteostatic capacity is coordinated with nuclear transport, genome-maintenance and cell-junction functions. GART and GMPS could support nucleotide demand, while GARS1 and YARS1 support translation; KPNA2, NUP50 and RCC1 could coordinate nuclear import and cell-cycle organization; and AFDN and DSC2 could connect this intracellular state to epithelial adhesion. TTLL12 may act as a network bridge between epithelial features and biosynthetic or cell-cycle-related genes. This mechanism is provisional: the co-abundance data do not establish physical interaction, directionality, cell-type origin or causality.

### Important genes

#### TTLL12

- **Related proteins** (co-abundance neighbors): AGPS (0.87), AFDN (0.85), GARS1 (0.84), GART (0.84), COPG2 (0.82), GMPS (0.81), DSC2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tubulin tyrosine ligase like 12. Enables H4K20me3 modified histone binding activity and tubulin binding activity. Involved in negative regulation of type I interferon-mediated signaling pathway and regulation of mitotic cell cycle. Located in cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Myoclonus (0.259); neoplasm (0.083); cancer (0.058); prostate carcinoma (0.052); colorectal carcinoma (0.045)
- **Europe PMC papers**: 216
- **Why important**: TTLL12 has the strongest network position in the module and connects biosynthetic, junctional and metabolic genes, including AGPS, AFDN, GARS1, GART, GMPS and DSC2. Its annotations implicate chromatin organization, mitotic-cell-cycle regulation and negative regulation of type I interferon signaling. HPA links it to esophageal epithelial cell types, which is relevant to a rectal epithelial context. Its disease associations are comparatively limited, so its importance here comes mainly from network bridging and biological coherence rather than a large disease literature.
- **Conclusion**: Established: TTLL12 is a central co-abundance connector with annotations related to chromatin and cell-cycle regulation and with epithelial cell-type enhancement. Hypothesis: it may help couple epithelial differentiation or junctional state to proliferative and biosynthetic demands, but this regulatory role is not demonstrated by the present module.

#### KPNA2

- **Related proteins** (co-abundance neighbors): AGPS (0.84), GART (0.84), MGST1 (0.81), CPSF2 (0.80); STRING partners: NUP50 (0.921), RCC1 (0.888)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_10000.1, huMAP3_12581.1, huMAP3_07479.1
- **Function (MyGene.info)**: karyopherin subunit alpha 2. The import of proteins into the nucleus is a process that involves at least 2 steps. The first is an energy-independent docking of the protein to the nuclear envelope and the second is an energy-dependent translocation through the nuclear pore complex. Imported proteins require a nuclear localization sequence (NLS) which generally consists of a short region of basic amino acids or 2 such regions s…
- **Diseases (Open Targets)**: severe acute respiratory syndrome (0.462); Orthomyxoviridae infectious disease (0.462); dengue disease (0.462); COVID-19 (0.373); non-alcoholic fatty liver (0.324)
- **Europe PMC papers**: 2442
- **Why important**: KPNA2 connects the module to AGPS, GART, MGST1 and CPSF2 and is supported by STRING relationships with NUP50 and RCC1. It is present in (hu.MAP huMAP3_10000.1), (hu.MAP huMAP3_12581.1) and (hu.MAP huMAP3_07479.1), making it the clearest bridge between the co-abundance network and several nuclear-transport complexes. Its established function is importin-alpha-mediated nuclear import, and HPA shows enhancement in testis and multiple germ-cell types. It also has a substantial literature and disease-association record, including infectious and metabolic disease contexts.
- **Conclusion**: Established: KPNA2 is a nuclear-import factor with repeated complex support and a central position in the module's nuclear-organization substructure. Hypothesis: coordinated KPNA2 abundance may mark altered nuclear transport in a proliferative or progenitor-like state, but the module does not show which cargoes or signals are involved.

#### RCC1

- **Related proteins** (co-abundance neighbors): AGPS (0.85), HEATR1 (0.82); STRING partners: KPNA2 (0.888), NUP50 (0.75)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_10000.1, huMAP3_12581.1
- **Function (MyGene.info)**: regulator of chromosome condensation 1. Enables several functions, including guanyl-nucleotide exchange factor activity; nucleosomal DNA binding activity; and protein heterodimerization activity. Involved in several processes, including G1/S transition of mitotic cell cycle; regulation of mitotic nuclear division; and spindle organization. Located in chromatin; cytoplasm; and nucleus. Part of protein-containing complex. [provided by All…
- **Diseases (Open Targets)**: injury (0.338); neurodegenerative disease (0.338); myasthenia gravis (0.329); neoplasm (0.104); cancer (0.091)
- **Europe PMC papers**: 3525
- **Why important**: RCC1 is connected to KPNA2 and NUP50 by STRING and occurs in (hu.MAP huMAP3_10000.1) and (hu.MAP huMAP3_12581.1). Its established functions include guanyl-nucleotide exchange activity and regulation of the G1/S transition, mitotic spindle organization, chromosome segregation and nuclear reassembly. HPA identifies late spermatids as a cell type with enhanced expression, and RCC1 has a substantial literature and disease-association record. It therefore provides a plausible cell-cycle and nuclear-organization anchor even though its direct network degree in this module is modest.
- **Conclusion**: Established: RCC1 links the module to Ran-related nuclear organization and mitotic control and is supported by known nuclear complexes. Hypothesis: RCC1 may connect nuclear transport to cell-cycle state in the shared module, but a proliferative interpretation requires independent expression or cell-cycle evidence.

#### GART

- **Related proteins** (co-abundance neighbors): GMPS (0.86), TTLL12 (0.84), KPNA2 (0.84), AGPS (0.83), CHORDC1 (0.82), NOLC1 (0.82); STRING partners: GMPS (0.937)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase. The protein encoded by this gene is a trifunctional polypeptide. It has phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase activity which is required for de novo purine biosynthesis. This enzyme is highly conserved in vertebrates. Alternative splicing of this gene results in two transcript variants encoding different isoforms.…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.606); mesothelioma (0.584); malignant pleural mesothelioma (0.557); adenocarcinoma (0.486); anaplastic lung carcinoma (0.462)
- **Europe PMC papers**: 1890
- **Why important**: GART is among the better-connected genes and directly links to GMPS through STRING, with both genes also connected to TTLL12, KPNA2 and NOLC1 in the co-abundance graph. GART is a trifunctional enzyme in de novo purine biosynthesis, and its annotations include GMP and IMP biosynthetic processes. It has a substantial literature and disease-association record. Its presence in (hu.MAP huMAP3_14442.1) adds complex-level support to the biosynthetic interpretation.
- **Conclusion**: Established: GART is a purine-biosynthetic enzyme whose relationship with GMPS is independently supported by STRING and whose network position connects metabolism to nuclear and nucleolar genes. Hypothesis: the GART-GMPS pair may reflect nucleotide demand associated with growth, repair or differentiation in the shared samples, but pathway activation is not established by enrichment.

#### AFDN

- **Related proteins** (co-abundance neighbors): TTLL12 (0.85), AGPS (0.83), GARS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: afadin, adherens junction formation factor. This gene encodes a multi-domain protein involved in signaling and organization of cell junctions during embryogenesis. It has also been identified as the fusion partner of acute lymphoblastic leukemia (ALL-1) gene, involved in acute myeloid leukemias with t(6;11)(q27;q23) translocation. Alternatively spliced transcript variants encoding different isoforms have been described for this gene, howeve…
- **Diseases (Open Targets)**: colorectal adenocarcinoma (0.401); lung carcinoma (0.371); gastric carcinoma (0.371); carcinoma of liver and intrahepatic biliary tract (0.370); melanoma (0.370)
- **Europe PMC papers**: 633
- **Why important**: AFDN has a relatively strong network position and connects TTLL12, AGPS and GARS1. Its established function is organization of adherens junctions and cell-cell signaling, and HPA places it at the plasma membrane and cell junctions with enhancement in esophageal epithelial cell types. It has documented associations with several carcinoma contexts and a substantial literature. AFDN therefore provides a tissue-structural interpretation for an otherwise largely intracellular module.
- **Conclusion**: Established: AFDN is an epithelial adhesion and signaling factor that occupies a bridging position between junctional and intracellular genes. Hypothesis: its co-abundance may indicate preservation or remodeling of epithelial cell-cell contacts alongside biosynthetic and nuclear-state changes, but the data do not establish whether adhesion is a driver or merely a marker of cell composition.

## Module 4

**Tissue pair**: rectum and stem_cells  
**Genes (15)**: ANXA4, ATP1A1, ATP1B1, BLM, CTNNA1, EIF3C, MACROH2A1, MYH14, ALDH18A1, PDCD4, RSL1D1, SNRPA1, SF3B3, CCT3, SLC30A7

### Function

No GO or KEGG term passed global correction, and STRING supplied no supplementary enrichment. The module therefore does not support one statistically established pathway-level function. Gene-level annotations and network structure instead indicate a mixed cellular program involving epithelial membrane transport and adhesion, intracellular zinc handling, RNA splicing, translation, protein folding, chromatin regulation, DNA repair, and cellular stress or survival. ATP1A1 and RSL1D1 have prominent network positions. The clearest known molecular pairs are the Na+/K+-ATPase subunits ATP1A1 and ATP1B1 and the spliceosomal proteins SF3B3 and SNRPA1. Overall, the evidence supports a shared cellular-state or cell-composition signal more strongly than one unified biochemical pathway.

**Cell composition.** The module contains no secreted genes and is not dominated by plasma proteins. Most genes have low immune-cell specificity, with ATP1B1 showing immune-cell enhancement and MYH14 not detected in immune cells; this argues against a blood-cell-driven interpretation. The module combines broadly expressed housekeeping-type factors with epithelial or tissue-enhanced genes. HPA identifies cell-type enhancement particularly in esophageal apical cells, salivary acinar or duct cells, enterocytes, syncytiotrophoblasts, and related epithelial populations. All module proteins are detected in rectum, while no matching HPA tissue is available for stem_cells. The shared module may therefore reflect a conserved epithelial or proliferative cell state, or shared cell types, rather than a rectum-specific secretory program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides high-confidence support for ATP1A1–ATP1B1 and SF3B3–SNRPA1. The first pair links the catalytic and beta subunits of the Na+/K+-ATPase, while the second links components of the U2 spliceosome. No other module relationships meet the stated STRING threshold, so most co-abundance edges are not independently confirmed as physical or functional interactions. hu.MAP supports partial membership of ATP1B1 and SLC30A7 in complex C1, and partial membership of SF3B3 and SNRPA1 in spliceosomal complexes C2 and C3. Because each complex includes many proteins outside the module, hu.MAP validates functional neighborhoods rather than the complete module as one complex.

**STRING interactions (score >= 0.7)**: 2 of 105 gene pairs: ATP1A1–ATP1B1 (0.999); SF3B3–SNRPA1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07410.1 (ATP1B1, SLC30A7; 2/35); huMAP3_06511.1 (SNRPA1, SF3B3; 2/79); huMAP3_08980.1 (SNRPA1, SF3B3; 2/97)

### Novelty

The constituent biology is established: Na+/K+-ATPase activity, epithelial adhesion, zinc transport, translation, chaperoning, DNA maintenance, and spliceosomal function are not new. The co-abundance combination across rectum and stem_cells could represent a new cross-tissue association, but the current evidence does not establish a novel mechanism. The sparse network, absence of globally significant GO or KEGG enrichment, absence of STRING enrichment, and limited overlap with known complexes favor describing this as a potentially novel module-level pattern requiring replication. Absence from STRING or hu.MAP does not by itself prove novelty.

**Hypothesis.** Hypothesis: the module reflects a conserved epithelial cell-state program coupling membrane ion and zinc homeostasis with junctional organization, biosynthetic capacity, RNA processing, and genome protection. ATP1A1 and ATP1B1 may maintain electrochemical gradients; CTNNA1 and MYH14 may support epithelial architecture; SLC30A7 may support Golgi zinc handling; and SF3B3 with SNRPA1 may support transcript processing. RSL1D1, EIF3C, CCT3, PDCD4, BLM, and MACROH2A1 may represent translational, proteostatic, survival, replication, and chromatin components of the same state. This is a mechanistic hypothesis, not an established causal pathway, and should be tested with cell-resolved data, perturbation, and independent replication.

### Important genes

#### ATP1A1

- **Related proteins** (co-abundance neighbors): CTNNA1 (0.85), ALDH18A1 (0.84), PDCD4 (0.83), MYH14 (0.82), RSL1D1 (0.80); STRING partners: ATP1B1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 has a prominent network position and connects to several otherwise diverse genes. It encodes the catalytic subunit of the Na+/K+-ATPase, which establishes sodium and potassium gradients required for osmoregulation and coupled transport. It is directly supported by STRING through ATP1B1, is detected in rectum, and has extensive literature and disease evidence.
- **Conclusion**: Established evidence supports ATP1A1 as a central membrane-homeostasis gene and as part of the known ATP1A1–ATP1B1 complex. Its network position makes it a plausible organizing marker, but co-abundance does not establish that ATP1A1 drives the other module genes.

#### ATP1B1

- **Related proteins** (co-abundance neighbors): CTNNA1 (0.90), ANXA4 (0.81); STRING partners: ATP1A1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_07410.1
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit beta 1. The protein encoded by this gene belongs to the family of Na+/K+ and H+/K+ ATPases beta chain proteins, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a vari…
- **Diseases (Open Targets)**: cardiovascular disorder (0.634); atrial fibrillation (0.606); congestive heart failure (0.601); heart failure (0.585); cardiac arrhythmia (0.536)
- **Europe PMC papers**: 2226
- **Why important**: ATP1B1 is the known beta-subunit partner of ATP1A1 and is part of hu.MAP complex C1. It connects to CTNNA1 and ANXA4, linking ion transport with epithelial junctional and membrane-associated biology. HPA shows kidney and several epithelial cell-type enhancements, as well as immune-cell enhancement in basophils, and rectal protein is detected.
- **Conclusion**: Established evidence supports ATP1B1 as a component of Na+/K+-ATPase function and as a plausible epithelial membrane marker. Its co-abundance is consistent with coordinated transport and epithelial organization, but it does not prove a direct bridge to the nuclear genes.

#### SF3B3

- **Related proteins** (co-abundance neighbors): SLC30A7 (0.91), RSL1D1 (0.84), EIF3C (0.80); STRING partners: SNRPA1 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Nucleoli rim; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: splicing factor 3b subunit 3. This gene encodes subunit 3 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); dengue disease (0.370); cervical cancer (0.189); cervical carcinoma (0.189); prostate cancer (0.111)
- **Europe PMC papers**: 965
- **Why important**: SF3B3 connects SLC30A7, RSL1D1, and EIF3C and is directly paired with SNRPA1 by STRING. It is a component of the U2 and minor spliceosomes, participates in pre-mRNA splicing, and appears in hu.MAP complexes C2 and C3. It also has substantial literature and disease-related evidence.
- **Conclusion**: Established evidence supports SF3B3 as a spliceosomal component and as one of the best-supported molecular anchors of the module. Its connection to membrane and translation-related genes suggests coordinated cell-state regulation, but that coordination remains hypothetical.

#### SNRPA1

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.83); STRING partners: SF3B3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein polypeptide A'. Enables RNA binding activity. Involved in mRNA splicing, via spliceosome and spermatogenesis. Located in nuclear speck. Part of U2-type catalytic step 2 spliceosome and U2-type precatalytic spliceosome. Implicated in connective tissue disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.538); dengue disease (0.370); phosphorus metabolism disease (0.196); hypotensive disorder (0.196); cancer (0.087)
- **Europe PMC papers**: 520
- **Why important**: SNRPA1 is directly connected to SF3B3 in STRING and appears with SF3B3 in hu.MAP complexes C2 and C3. It contributes to U2-type spliceosome assembly and mRNA splicing and shows cell-type enhancement in trophoblast-related populations. Its network position is less central than SF3B3, but its relationship with SF3B3 is strongly supported within this module.
- **Conclusion**: Established evidence supports SNRPA1 as a spliceosomal partner of SF3B3. It is a strong marker of the RNA-processing component, while any role in coordinating epithelial transport or stem-cell state is hypothetical.

#### CTNNA1

- **Related proteins** (co-abundance neighbors): ATP1B1 (0.90), ATP1A1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin alpha 1. This gene encodes a member of the catenin family of proteins that play an important role in cell adhesion process by connecting cadherins located on the plasma membrane to the actin filaments inside the cell. The encoded mechanosensing protein contains three vinculin homology domains and undergoes conformational changes in response to cytoskeletal tension, resulting in the reconfiguration of cadhe…
- **Diseases (Open Targets)**: Butterfly-shaped pigment dystrophy (0.750); hereditary neoplastic syndrome (0.557); hereditary diffuse gastric adenocarcinoma (0.555); colorectal cancer (0.506); exudative vitreoretinopathy (0.390)
- **Europe PMC papers**: 2688
- **Why important**: CTNNA1 links ATP1A1 and ATP1B1 and encodes an actin-associated cadherin-complex component involved in cell adhesion and mechanosensing. It is localized to the plasma membrane and cell junctions, shows epithelial cell-type enhancement, is detected in rectum, and has extensive literature and disease associations including colorectal cancer and hereditary gastric disease.
- **Conclusion**: Established evidence supports CTNNA1 as an epithelial adhesion and mechanotransduction factor and as a plausible bridge between the ATPase pair and epithelial architecture. Its module-level association is compatible with coordinated barrier organization, but causality and relevance to stem cells require direct testing.

#### BLM

- **Related proteins** (co-abundance neighbors): ANXA4 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BLM RecQ like helicase. The Bloom syndrome is an autosomal recessive disorder characterized by growth deficiency, microcephaly and immunodeficiency among others. It is caused by homozygous or compound heterozygous mutation in the gene encoding DNA helicase RecQ protein on chromosome 15q26. This Bloom-associated helicase unwinds a variety of DNA substrates including Holliday junction, and is involved in several pathways c…
- **Diseases (Open Targets)**: Bloom syndrome (0.850); hereditary neoplastic syndrome (0.576); cancer (0.553); colorectal cancer (0.513); leukemia (0.465)
- **Europe PMC papers**: 15076
- **Why important**: BLM provides a genome-maintenance dimension to an otherwise mixed module. It encodes a RecQ helicase involved in DNA replication, homologous-recombination repair, telomere maintenance, and genome stability. It has extensive literature and disease evidence, including Bloom syndrome, cancer, and colorectal cancer associations, although its network connection is limited to ANXA4.
- **Conclusion**: Established evidence supports BLM as a DNA-repair and genome-stability factor. Its inclusion may indicate a proliferative or stress-resilient cell state, but its weak network connectivity and the lack of enrichment evidence make that interpretation provisional.

## Module 5

**Tissue pair**: rectum and stem_cells  
**Genes (14)**: ARFGAP1, TRIP10, DAB2, GNAI3, ITGB5, PLBD1, SLC25A20, MTX1, OCIAD1, CTSA, MRPL4, POLR2A, SRP68, TAP2

### Function

This module does not have a statistically supported GO or KEGG functional enrichment term: no globally significant GO/KEGG term passed global correction. The module therefore should not be assigned a single pathway based on enrichment. Its genes instead suggest a mixed cellular program involving membrane trafficking and endocytosis, integrin-mediated adhesion, intracellular signaling, mitochondrial organization and metabolism, antigen processing, lysosomal or proteolytic activity, and transcriptional or translational support. The network is sparse and appears to connect several functional neighborhoods rather than represent one established molecular complex. The strongest biological interpretation is a context-dependent epithelial or progenitor-cell state involving trafficking, adhesion, organelle function, and signaling, but this remains an interpretation from individual gene functions rather than an enrichment-supported conclusion.

**Cell composition.** The module is not dominated by secreted proteins: only a minority of genes have secretome annotations, including PLBD1 and CTSA. It is also not uniformly blood-cell specific. Most genes have low immune-cell specificity, although PLBD1 is group enriched in monocyte and myeloid-cell populations, and DAB2 and TRIP10 show enrichment in plasmacytoid dendritic cells. Platelet-associated expression is seen for DAB2, ITGB5, and CTSA, while several genes are enhanced in esophageal apical cells and related epithelial populations. HPA protein detection is present for most genes in rectum, whereas there is no matching HPA tissue category for stem_cells. The mixture of broadly expressed cellular machinery with cell-type-enhanced genes means that the shared signal could reflect a common epithelial or progenitor-associated state, technical or cellular composition effects, or a contribution from vascular, platelet, or myeloid-associated cells. It should not be described as a plasma-protein module or as a blood-cell module on the available evidence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional-enrichment term was reported, and no high-confidence STRING interaction was detected among the module genes. No hu.MAP complex contains multiple module members. Thus, the co-abundance relationships are not explained by a previously catalogued dense physical interaction complex. The absence of curated interactions does not imply that the genes are biologically unrelated: the module contains plausible functional links, such as DAB2 with ITGB5 in adhesion and endocytosis, MTX1 with mitochondrial and membrane-protein handling, and OCIAD1 with signaling and stem-cell homeostasis. These links are functional interpretations from the gene annotations, not experimentally established within-module interactions.

**STRING interactions (score >= 0.7)**: 0 of 91 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel co-abundance pattern, but it cannot be claimed as a newly discovered molecular pathway. The case for novelty is that the module is sparse, lacks high-confidence STRING edges, lacks a shared hu.MAP complex, and lacks a globally significant GO or KEGG term. However, absence from STRING or hu.MAP alone does not prove novelty, because co-abundance can arise from coordinated regulation, shared cell composition, tissue context, or indirect biological relationships. The most defensible conclusion is that the rectum–stem_cells co-abundance pattern is a potentially novel tissue-pair observation whose molecular mechanism remains unvalidated.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular state in which epithelial or progenitor-like cells coordinate receptor trafficking, integrin-dependent adhesion, vesicle handling, mitochondrial activity, and selective immune or stress-related processing. DAB2 and ITGB5 could organize the membrane-adhesion and endocytic arm, OCIAD1 could connect receptor signaling with stem-cell homeostasis, while MTX1, SLC25A20, and CTSA could represent organelle, metabolic, and degradative support. TAP2 could indicate an antigen-processing component. This model predicts that the module will vary with epithelial or progenitor abundance and with inflammatory, vascular, platelet, or myeloid contamination, and should therefore be tested using cell-resolved expression, protein localization, and perturbation rather than inferred from co-abundance alone.

### Important genes

#### DAB2

- **Related proteins** (co-abundance neighbors): SLC25A20 (0.86), ITGB5 (0.85), GNAI3 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Vesicles, Plasma membrane; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DAB adaptor protein 2. This gene encodes a mitogen-responsive phosphoprotein. It is expressed in normal ovarian epithelial cells, but is down-regulated or absent from ovarian carcinoma cell lines, suggesting its role as a tumor suppressor. This protein binds to the SH3 domains of GRB2, an adaptor protein that couples tyrosine kinase receptors to SOS (a guanine nucleotide exchange factor for Ras), via its C-terminal prol…
- **Diseases (Open Targets)**: gout (0.381); macular degeneration (0.366); exocrine pancreatic carcinoma (0.322); spinal stenosis (0.312); Genu valgum (0.272)
- **Europe PMC papers**: 7584
- **Why important**: DAB2 has one of the strongest network positions in the module and connects to SLC25A20, ITGB5, and GNAI3. Its annotations support receptor-mediated endocytosis, integrin signaling, vesicle or plasma-membrane localization, and modulation of growth-factor signaling. Its HPA profile includes platelet and plasmacytoid dendritic-cell enrichment, while its disease and cancer literature is substantial. It is therefore a useful candidate for linking membrane trafficking, adhesion, signaling, and cellular composition.
- **Conclusion**: Established evidence supports DAB2 as an endocytic and signaling adaptor with a central position in this sparse module. It is plausible, but not established, that DAB2 is a regulatory organizer of the shared co-abundance state. The platelet and plasmacytoid-dendritic-cell annotations require cell-composition controls before assigning the signal to epithelial or stem cells.

#### ITGB5

- **Related proteins** (co-abundance neighbors): TRIP10 (0.87), DAB2 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 5. This gene encodes a beta subunit of integrin, which can combine with different alpha chains to form a variety of integrin heterodimers. Integrins are integral cell-surface receptors that participate in cell adhesion as well as cell-surface mediated signaling. The alphav beta5 integrin is involved in adhesion to vitronectin. [provided by RefSeq, Aug 2017].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.569); coronary artery disorder (0.567); carpal tunnel syndrome (0.490); migraine disorder (0.452); open-angle glaucoma (0.451)
- **Europe PMC papers**: 2960
- **Why important**: ITGB5 is directly connected to DAB2 and TRIP10 and is annotated for integrin-mediated adhesion, cell-matrix interaction, migration, and transforming-growth-factor-beta receptor signaling. Its plasma-membrane localization and blood-vessel tissue enhancement make it a strong candidate for the adhesion and tissue-interface component of the module. It also has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports ITGB5 as a cell-surface adhesion and signaling receptor subunit. Its network placement supports a role at the interface between extracellular matrix interaction and endocytic or cytoskeletal processes. A specific role in maintaining the shared rectum–stem_cells state remains a hypothesis.

#### OCIAD1

- **Related proteins** (co-abundance neighbors): ARFGAP1 (0.82), SRP68 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OCIA domain containing 1. Predicted to be involved in several processes, including hematopoietic stem cell homeostasis; positive regulation of receptor signaling pathway via JAK-STAT; and regulation of stem cell differentiation. Located in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Alzheimer disease (0.101); maturity-onset diabetes of the young (0.080); breast carcinoma (0.070); primary familial polycythemia due to EPO receptor mutation (0.068); pyruvate kinase hyperactivity (0.067)
- **Europe PMC papers**: 246
- **Why important**: OCIAD1 links ARFGAP1 and SRP68 in the module and is annotated for endocytosis, positive regulation of JAK–STAT receptor signaling, hematopoietic stem-cell homeostasis, and regulation of stem-cell differentiation. Its vesicular localization and relatively limited literature make it particularly informative for the tissue-pair interpretation, because it offers a biologically relevant connection to progenitor or stem-cell regulation without being a canonical high-abundance housekeeping component.
- **Conclusion**: Established evidence supports OCIAD1 as a membrane-associated regulator connected to receptor signaling and stem-cell-related processes. Its position suggests a possible bridge between vesicle trafficking and cell-state regulation. Whether it drives the shared module or merely tracks the relevant cell population is unresolved.

#### TAP2

- **Related proteins** (co-abundance neighbors): MTX1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transporter 2, ATP binding cassette subfamily B member. The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily ar…
- **Diseases (Open Targets)**: MHC class I deficiency (0.729); MHC class I deficiency 2 (0.477); hereditary disease (0.193); neoplasm (0.107); cancer (0.097)
- **Europe PMC papers**: 4557
- **Why important**: TAP2 is connected to MTX1 and provides the clearest immune-related functional annotation in the module: ATP-dependent peptide transport into the endoplasmic reticulum and MHC class I antigen processing. It has strong disease relevance through MHC class I deficiency and a substantial literature base. Its endoplasmic-reticulum localization complements the module's vesicle, mitochondrial, and membrane-trafficking annotations.
- **Conclusion**: Established evidence supports TAP2 as an antigen-processing and peptide-transport component. Its presence may indicate an interferon or immune-processing influence, but the HPA profile does not support interpreting the entire module as immune-cell specific. TAP2 could therefore mark a state-dependent epithelial antigen-presentation program or reflect a minor immune contribution.

#### CTSA

- **Related proteins** (co-abundance neighbors): MRPL4 (0.82), MTX1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Vesicles; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cathepsin A. This gene encodes a member of the peptidase S10 family of serine carboxypeptidases. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate two chains that comprise the heterodimeric active enzyme. This enzyme possesses deamidase, esterase and carboxypeptidase activities and acts as a scaffold in the …
- **Diseases (Open Targets)**: galactosialidosis (0.842); cathepsin a-related arteriopathy-strokes-leukoencephalopathy (0.464); hereditary disease (0.451); lysosomal storage disease (0.373); Lynch syndrome (0.340)
- **Europe PMC papers**: 8422
- **Why important**: CTSA connects MRPL4 and MTX1 and encodes a multifunctional lysosomal or vesicular carboxypeptidase with proteolytic, esterase, deamidase, and scaffold roles. It is detected in rectum, enriched in platelets, and has extensive literature and strong disease associations, including galactosialidosis and related arteriopathy. Its network location places degradative and vesicular biology between mitochondrial and translational components.
- **Conclusion**: Established evidence supports CTSA as a lysosomal multienzyme-complex component involved in proteolysis and intracellular protein handling. It may contribute to the module's vesicle and organelle-maintenance signal. A platelet-derived contribution is possible, but the available data do not establish whether CTSA is mechanistically active in the conserved tissue-pair program.

## Module 7

**Tissue pair**: rectum and stem_cells  
**Genes (5)**: COPS3, ENG, GAR1, RFC4, UFD1

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established shared pathway assignment. The genes instead represent distinct biological processes: ENG is associated with endothelial TGF-beta receptor signaling, vasculogenesis, blood-vessel morphogenesis and hypoxia response; UFD1 with ER-associated degradation and ubiquitin-dependent protein catabolism; GAR1 with H/ACA snoRNP function, ribosome biogenesis, rRNA pseudouridylation and telomere maintenance; RFC4 with DNA replication, replication-checkpoint signaling and DNA repair; and COPS3 with the COP9 signalosome, protein deneddylation, ubiquitin-dependent catabolism and regulation of DNA-damage signaling. Taken together, the module is best interpreted as a weakly connected co-abundance signature spanning vascular signaling, genome maintenance, RNA processing and proteostasis rather than as an established single biological pathway. The lack of an enriched term is not evidence that the module is false.

**Cell composition.** All module genes have HPA annotations. Most show low tissue specificity and low immune-cell specificity, while all are reported as cell-type enhanced in at least one HPA cell type. The cell-type pattern includes syncytiotrophoblasts and germ-cell populations, with additional enrichment in trophoblast, hepatic stellate, Leydig, peritubular myoid and erythrocyte-progenitor contexts. ENG is tissue enhanced in heart muscle and is group enriched in several myeloid and NK-cell populations, whereas the other genes have low immune-cell specificity. No gene is annotated as secreted, arguing against a plasma-protein explanation. Protein detection in rectum is reported for most of the module, although ENG is not detected by rectal IHC. The HPA pattern therefore supports broadly expressed intracellular or membrane-associated biology with cell-state associations, and it does not establish that the shared signal is caused by blood contamination or a single shared cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was detected among the module gene pairs, and STRING functional enrichment was absent. No hu.MAP complex contained multiple module members. Thus, the co-abundance links are not corroborated by the supplied physical-interaction or curated-complex evidence. The biological relationships that are already known are mainly within individual gene functions: UFD1 participates in an ER-associated degradation complex with other proteins not present in the module; GAR1 belongs to the H/ACA snoRNP system with DKC1, NOLA2 and NOLA3; RFC4 is a subunit of the replication factor C complex; COPS3 is a COP9 signalosome subunit; and ENG is a component of the TGF-beta receptor complex. These established external relationships make the gene annotations credible, but they do not validate a direct physical module among the five members.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a dataset-specific co-abundance pattern, but it cannot be called a new biological mechanism from the supplied evidence. The absence of STRING and hu.MAP support makes a previously unrecognized physical complex unlikely, while the absence of globally significant GO/KEGG enrichment prevents a strong pathway claim. A potentially novel aspect is the joint co-abundance of ENG with genes involved in ER quality control, nucleolar RNA processing, DNA replication and COP9 signaling in rectum and stem-cell samples. However, that observation requires replication in independent cohorts, adjustment for cell composition and comparison with existing co-expression resources before it can be considered a new finding.

**Hypothesis.** Hypothesis: the module reflects a shared proliferative or stress-adaptive cell state in which vascular or membrane signaling involving ENG covaries with intracellular programs for protein quality control, ribosome and RNA maturation, DNA replication and damage handling. ENG may mark the cellular or microenvironmental context, while UFD1, GAR1, RFC4 and COPS3 may reflect coordinated demands for proteostasis, biosynthetic capacity, genome duplication and signal regulation. This is a mechanistic hypothesis only; the current evidence does not demonstrate direct regulation among these genes or prove that they operate in one pathway.

### Important genes

#### ENG

- **Related proteins** (co-abundance neighbors): UFD1 (0.90), GAR1 (0.87), RFC4 (0.85), COPS3 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: endoglin. This gene encodes a homodimeric transmembrane protein which is a major glycoprotein of the vascular endothelium. This protein is a component of the transforming growth factor beta receptor complex and it binds to the beta1 and beta3 peptides with high affinity. Mutations in this gene cause hereditary hemorrhagic telangiectasia, also known as Osler-Rendu-Weber syndrome 1, an autosomal dominant mult…
- **Diseases (Open Targets)**: telangiectasia, hereditary hemorrhagic, type 1 (0.855); hereditary hemorrhagic telangiectasia (0.840); vascular disorder (0.598); arteriovenous hemangioma/malformation (0.587); capillary disorder (0.579)
- **Europe PMC papers**: 46026
- **Why important**: ENG is the central node of the module, connected to every other member in the co-abundance subgraph and having the strongest network position. Its established function as endoglin, a transmembrane component of the TGF-beta receptor complex, links it to endothelial biology, vasculogenesis, blood-vessel morphogenesis and hypoxia response. It has a strong hereditary hemorrhagic telangiectasia disease association and extensive literature coverage. HPA also gives it the distinctive heart-muscle tissue enhancement and group enrichment in several immune-cell populations.
- **Conclusion**: Established evidence supports ENG as the best contextual anchor and likely marker of vascular or cell-state biology. Its centrality is co-abundance centrality, not proof of physical interaction or causal control. The proposed role of ENG in coordinating the other module genes remains a hypothesis.

#### UFD1

- **Related proteins** (co-abundance neighbors): ENG (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin recognition factor in ER associated degradation 1. The protein encoded by this gene forms a complex with two other proteins, nuclear protein localization-4 and valosin-containing protein, and this complex is necessary for the degradation of ubiquitinated proteins. In addition, this complex controls the disassembly of the mitotic spindle and the formation of a closed nuclear envelope after mitosis. Mutations in this gene have been associated with C…
- **Diseases (Open Targets)**: dengue disease (0.370); alcohol drinking (0.225); infection (0.079); neoplasm (0.076); acute lymphoblastic leukemia (0.075)
- **Europe PMC papers**: 1223
- **Why important**: UFD1 is the module member most directly associated with ER-associated degradation and ubiquitin-dependent protein catabolism. It also participates in control of mitotic-spindle disassembly and nuclear-envelope reformation, connecting proteostasis with cell division. Its single module connection is to ENG, so it is not a network hub, but its function provides a plausible stress and protein-quality-control dimension. It has disease associations involving developmental and cardiac or craniofacial defects and a moderate literature base.
- **Conclusion**: Established evidence supports UFD1 as a proteostasis and cell-division factor. Its inclusion may indicate an adaptive intracellular state, but the module does not establish that ER-associated degradation is the shared function.

#### GAR1

- **Related proteins** (co-abundance neighbors): ENG (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GAR1 ribonucleoprotein. This gene is a member of the H/ACA snoRNPs (small nucleolar ribonucleoproteins) gene family. snoRNPs are involved in various aspects of rRNA processing and modification and have been classified into two families: C/D and H/ACA. The H/ACA snoRNPs also include the DKC1, NOLA2 and NOLA3 proteins. These four H/ACA snoRNP proteins localize to the dense fibrillar components of nucleoli and to coiled (Ca…
- **Diseases (Open Targets)**: neurodegenerative disease (0.400); prostate carcinoma (0.198); Thrombocytopenia (0.048); familial primary hypomagnesemia with normocalciuria and normocalcemia (0.041); renal hypomagnesemia 2 (0.041)
- **Europe PMC papers**: 1232
- **Why important**: GAR1 represents the nucleolar RNA-processing component of the module. It is a member of H/ACA snoRNPs and is associated with rRNA pseudouridylation, ribosome biogenesis and telomere maintenance through telomerase. It has a single co-abundance connection to ENG and no detected STRING or hu.MAP relationship within the module. Its literature volume is comparable to that of several other non-hub members, and its annotations provide a biologically distinct interpretation of the signal.
- **Conclusion**: Established evidence supports GAR1 as a ribosome- and RNA-maturation factor. Its presence is compatible with biosynthetic or proliferative demand, but a direct connection to ENG or the remaining module genes is not demonstrated.

#### RFC4

- **Related proteins** (co-abundance neighbors): ENG (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: replication factor C subunit 4. The elongation of primed DNA templates by DNA polymerase delta and DNA polymerase epsilon requires the accessory proteins proliferating cell nuclear antigen (PCNA) and replication factor C (RFC). RFC, also named activator 1, is a protein complex consisting of five distinct subunits of 140, 40, 38, 37, and 36 kD. This gene encodes the 37 kD subunit. This subunit forms a core complex with the 36 and…
- **Diseases (Open Targets)**: Morimoto-Ryu-Malicdan neuromuscular syndrome (0.541); congenital myopathy with cores (0.372); congenital myopathy (0.372); sensorineural hearing loss disorder (0.370); neoplasm (0.107)
- **Europe PMC papers**: 1438
- **Why important**: RFC4 is the module member most directly tied to DNA synthesis and genome maintenance. It is a subunit of replication factor C and is annotated for DNA replication, replication-checkpoint signaling, DNA strand elongation and DNA repair. It connects only to ENG in the module, yet it is important because it supplies a clear cell-cycle and genome-integrity interpretation. It also has documented congenital neuromuscular and hearing-related disease associations and a substantial literature base.
- **Conclusion**: Established evidence supports RFC4 as a DNA-replication and repair factor. Its co-abundance may indicate proliferative or replication stress, but the data do not show that RFC4 is regulated by ENG or that replication is the module's primary function.

#### COPS3

- **Related proteins** (co-abundance neighbors): ENG (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: COP9 signalosome subunit 3. The protein encoded by this gene possesses kinase activity that phosphorylates regulators involved in signal transduction. It phosphorylates I kappa-Balpha, p105, and c-Jun. It acts as a docking site for complex-mediated phosphorylation. The gene is located within the Smith-Magenis syndrome region on chromosome 17. Several transcript variants encoding different isoforms have been found for this ge…
- **Diseases (Open Targets)**: neurodegenerative disease (0.416); osteosarcoma (0.101); lung carcinoma (0.071); lung cancer (0.071); neoplasm (0.067)
- **Europe PMC papers**: 1103
- **Why important**: COPS3 is a component of the COP9 signalosome and is associated with protein deneddylation, ubiquitin-dependent catabolism, signal transduction and regulation of DNA-damage responses. Like the other peripheral members, it has one module connection, but it provides a bridge between proteostasis, signaling and genome surveillance. It has disease associations involving neurodegenerative disease and cancer-related conditions and a substantial literature base.
- **Conclusion**: Established evidence supports COPS3 as a signal-regulatory and protein-modification factor. Its presence is consistent with a broad cellular stress or growth state, but the module does not establish a specific COP9-mediated mechanism.

## Module 8

**Tissue pair**: rectum and stem_cells  
**Genes (6)**: H1-5, HNRNPK, HNRNPL, PHB1, RPL12, VDAC2

### Function

This is a mixed intracellular co-abundance module rather than a clearly defined pathway module. Its strongest structural signals are the known HNRNPK–HNRNPL RNA-binding pair and the PHB1–VDAC2 mitochondrial pair, with RPL12 and H1-5 connected to the same local network. The gene annotations collectively point to RNA processing and transcriptional regulation, mitochondrial organization and outer-membrane function, protein synthesis, and chromatin compaction. However, no GO or KEGG term passed global correction, so no GO or KEGG function can be called significantly enriched. The STRING tissue annotations for brain cell lines and interstitial cells of Cajal are supplementary (STRING TISSUES Brain cell line; within-query FDR = 0.0188) (STRING TISSUES Interstitial cell of Cajal; within-query FDR = 0.0216) and may indicate shared cellular programs, but they do not establish a tissue-specific function for this module.

**Cell composition.** The module is not predominantly composed of plasma proteins or classical secreted proteins. Most genes have low tissue specificity and low immune-cell specificity, and the proteins are largely intracellular, located in the nucleoplasm, mitochondria, or cytoplasmic translation machinery. HPA detects all module proteins in rectum, whereas there is no matching HPA tissue for stem_cells. H1-5 is enriched in bone marrow and lymphoid tissue and in erythrocyte, megakaryocyte, and monocyte progenitors, so a hematopoietic or sample-composition contribution is possible. Nevertheless, the overall HPA profile does not support a broadly blood-cell-specific module. Several genes show epithelial or other cell-type enhancement, including esophageal basal, apical, and suprabasal cells, which is compatible with a shared epithelial or progenitor-related cellular context but is not proof of one.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports two high-confidence pairwise relationships within the module: HNRNPK with HNRNPL, and PHB1 with VDAC2. The HNRNPK–HNRNPL pair is also present in two hu.MAP complexes (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_10625.1), each containing many additional RNA-binding and RNA-processing proteins. PHB1–VDAC2 is present in a hu.MAP complex (hu.MAP huMAP3_10725.1) containing mitochondrial, membrane, and organelle-associated proteins. RPL12 and H1-5 have no listed STRING partners or hu.MAP complexes within this evidence set. Thus, the network contains two externally supported interaction anchors but also several edges that are not independently confirmed by STRING or hu.MAP. The supplementary STRING tissue terms (STRING TISSUES Brain cell line; within-query FDR = 0.0188) (STRING TISSUES Interstitial cell of Cajal; within-query FDR = 0.0216) involve the HNRNP and mitochondrial genes, but their within-query significance does not constitute global enrichment.

**STRING interactions (score >= 0.7)**: 2 of 15 gene pairs: HNRNPK–HNRNPL (0.99); PHB1–VDAC2 (0.91)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Brain cell line (FDR = 0.0188, 4 genes); TISSUES Interstitial cell of Cajal (FDR = 0.0216, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10659.1 (HNRNPL, HNRNPK; 2/28); huMAP3_10625.1 (HNRNPL, HNRNPK; 2/57); huMAP3_10725.1 (PHB1, VDAC2; 2/59)

### Novelty

The biological ingredients are not novel in isolation: HNRNPK–HNRNPL RNA-processing relationships, PHB1–VDAC2 association, and the corresponding hu.MAP complexes are already documented. The potentially new observation is their co-abundance in a module shared by rectum and stem_cells, together with RPL12 and H1-5. The fact sheet does not establish that this exact cross-tissue module has been reported previously, but it also provides no independent replication, perturbation, or literature comparison showing that it is new. Therefore the appropriate conclusion is that the module may represent a novel co-abundance pattern, while its molecular interactions are largely established and absence from a reference interaction resource would not prove novelty.

**Hypothesis.** Hypothesis: the shared module reflects coordinated support for cellular state maintenance in epithelial or progenitor-like cells, combining RNA maturation and post-transcriptional regulation through HNRNPK and HNRNPL, mitochondrial membrane and apoptotic-metabolic control through PHB1 and VDAC2, and chromatin or biosynthetic capacity through H1-5 and RPL12. A shared cell-state composition between rectum and stem_cells could generate this pattern, with H1-5 potentially marking a hematopoietic contribution in some samples. This hypothesis should be tested by cell-type deconvolution, independent cohorts, protein-level co-variation, and perturbation of the RNA-processing and mitochondrial components.

### Important genes

#### PHB1

- **Related proteins** (co-abundance neighbors): VDAC2 (0.92), RPL12 (0.83), H1-5 (0.82), HNRNPK (0.80); STRING partners: VDAC2 (0.91)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_10725.1
- **Function (MyGene.info)**: prohibitin 1. This gene is evolutionarily conserved, and its product is proposed to play a role in human cellular senescence and tumor suppression. Antiproliferative activity is reported to be localized to the 3' UTR, which is proposed to function as a trans-acting regulatory RNA. Several pseudogenes of this gene have been identified. Alternative splicing results in multiple transcript variants. [provided by Re…
- **Diseases (Open Targets)**: coronary artery disorder (0.458); myocardial ischemia (0.454); hypertensive disorder (0.396); heart disorder (0.343); asthma (0.339)
- **Europe PMC papers**: 1249
- **Why important**: PHB1 is the strongest network hub in the module and connects the mitochondrial VDAC2 branch with RPL12, H1-5, and HNRNPK. HPA places it in mitochondria and reports enhancement in esophageal basal cells and salivary acinar cells. Its annotation includes mitochondrion organization, transcriptional regulation, cellular senescence, and tumor-suppression-related biology. It has extensive literature and disease associations including cardiovascular disorders and asthma.
- **Conclusion**: Established: PHB1 is a central module connector with mitochondrial and regulatory annotations and an externally supported relationship with VDAC2 through STRING and hu.MAP (hu.MAP huMAP3_10725.1). Hypothesis: PHB1 may help couple mitochondrial state to broader epithelial or progenitor cell-state regulation in this module.

#### VDAC2

- **Related proteins** (co-abundance neighbors): PHB1 (0.92), RPL12 (0.87), H1-5 (0.86); STRING partners: PHB1 (0.91)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_10725.1
- **Function (MyGene.info)**: voltage dependent anion channel 2. This gene encodes a member of the voltage-dependent anion channel pore-forming family of proteins that are considered the main pathway for metabolite diffusion across the mitochondrial outer membrane. The encoded protein is also thought to be involved in the mitochondrial apoptotic pathway via regulation of BCL2-antagonist/killer 1 protein activity. Pseudogenes have been identified on chromosomes …
- **Diseases (Open Targets)**: neurodegenerative disease (0.345); alcohol drinking (0.204); atrial fibrillation (0.175); major depressive disorder (0.143); severe combined immunodeficiency (0.118)
- **Europe PMC papers**: 2914
- **Why important**: VDAC2 is a high-connectivity mitochondrial component linked to PHB1, RPL12, and H1-5, and it is part of hu.MAP complex (hu.MAP huMAP3_10725.1). Its established annotations include metabolite diffusion across the mitochondrial outer membrane, transport, phospholipid-related processes, and mitochondrial outer-membrane permeabilization. It has substantial literature and disease associations spanning neurodegenerative and cardiac conditions.
- **Conclusion**: Established: VDAC2 supplies a credible mitochondrial outer-membrane and transport component, with the PHB1 relationship supported by STRING and hu.MAP (hu.MAP huMAP3_10725.1). Hypothesis: its co-abundance with nuclear RNA-processing genes may reflect coordinated adaptation of mitochondrial function during a shared cellular state rather than a single canonical pathway.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): HNRNPL (0.81), PHB1 (0.80); STRING partners: HNRNPL (0.99)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is one of the two module genes embedded in both listed hu.MAP RNA-associated complexes (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_10625.1) and forms the strongest STRING relationship in the module with HNRNPL. It is a widely studied heterogeneous nuclear ribonucleoprotein involved in RNA processing, mRNA splicing, transcriptional regulation, and signal transduction. It also has strong disease associations, including Au-Kline syndrome and neurodevelopmental disease.
- **Conclusion**: Established: HNRNPK is a core RNA-processing anchor supported by both STRING and hu.MAP. Hypothesis: it may organize the post-transcriptional component of the shared module and link that component indirectly to mitochondrial or proliferative state through its regulatory functions.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): HNRNPK (0.81); STRING partners: HNRNPK (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is the partner of HNRNPK in STRING and both hu.MAP complexes (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_10625.1). Its annotations support regulation of alternative mRNA splicing, RNA processing, mRNA maturation, and transcriptional repression. HPA shows enhancement in several neural and epithelial-related cell types, while its disease associations include dengue disease and cancer-related conditions. Its literature base is substantial despite its lower network connectivity within this module.
- **Conclusion**: Established: HNRNPL provides the clearest independently supported RNA-processing relationship in the module through its partnership with HNRNPK. Hypothesis: the HNRNPK–HNRNPL pair may define a post-transcriptional cell-state program shared across the two tissues, but the module data do not demonstrate direct regulation of the other module genes.

#### H1-5

- **Related proteins** (co-abundance neighbors): VDAC2 (0.86), PHB1 (0.82), RPL12 (0.81); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: H1.5 linker histone, cluster member. Histones are basic nuclear proteins responsible for nucleosome structure of the chromosomal fiber in eukaryotes. Two molecules of each of the four core histones (H2A, H2B, H3, and H4) form an octamer, around which approximately 146 bp of DNA is wrapped in repeating units, called nucleosomes. The linker histone, H1, interacts with linker DNA between nucleosomes and functions in the compaction of ch…
- **Diseases (Open Targets)**: breast carcinoma (0.116); neoplasm (0.080); breast cancer (0.080); sebaceous of Jadassohn nevus (0.074); actinic keratosis (0.071)
- **Europe PMC papers**: 117344
- **Why important**: H1-5 is a highly connected module member despite having no listed STRING partner or hu.MAP complex in the evidence set. It encodes a linker histone involved in nucleosome organization, chromatin compaction, chromosome condensation, and transcriptional regulation. HPA specifically associates it with bone marrow and lymphoid tissue and with erythrocyte, megakaryocyte, and monocyte progenitors. It also has a very large literature base and reported neoplasm-related associations.
- **Conclusion**: Established: H1-5 contributes a chromatin-associated component and has the strongest hematopoietic tissue context in the module. Hypothesis: its presence may indicate a shared progenitor or sample-composition signal, or coordinated chromatin remodeling, but the current evidence cannot distinguish these explanations.
