# Conserved co-abundance modules: bone_marrow and rectum

## Module 0

**Tissue pair**: bone_marrow and rectum  
**Genes (11)**: SH3BP1, AIFM1, CDK5RAP3, EXD2, MACROH2A1, CHCHD3, IMMT, NSDHL, MRPL19, SLC25A1, VIL1

### Function

This is a heterogeneous module rather than a clearly established single biological pathway. Its strongest functional theme is mitochondrial biology: IMMT and CHCHD3 are components of the MICOS system involved in cristae formation, MRPL19 supports mitochondrial translation, AIFM1 participates in mitochondrial apoptosis and respiratory-chain assembly, and SLC25A1 controls mitochondrial citrate transport. Other genes point to DNA and RNA processing, chromatin regulation, sterol biosynthesis, and epithelial actin organization. EXD2 is the most connected module gene and links several of these functional classes. No GO/KEGG term passed global correction, and STRING functional enrichment was absent. Therefore, the functional interpretation rests on convergent gene-level annotations and network structure, not on statistically significant pathway enrichment. VIL1 and SH3BP1 provide an epithelial cytoskeleton and junctional component, while MACROH2A1 provides a chromatin and transcriptional component.

**Cell composition.** The module is not composed of plasma or secreted proteins: the secretome annotation is absent for every member. HPA evidence indicates that many members have low tissue specificity and low immune-cell specificity, with cell-type enhancement spanning epithelial, hepatic, reproductive, muscular, glial, and progenitor populations. VIL1 is tissue-enriched in intestine and enhanced in colonocytes and enterocytes, whereas SH3BP1 is enhanced in esophagus and enriched in microglia. AIFM1, IMMT, CHCHD3, and several other members are detected in rectum or bone marrow, but the pattern does not resemble a blood-cell-specific module. Two genes have immune-cell enhancement in HPA, involving eosinophil or neutrophil annotations, yet this is insufficient to assign the shared module to blood contamination. The module may instead reflect broadly expressed mitochondrial programs combined with epithelial or other shared cellular states present in the sampled tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The observed network is sparse. STRING supports a high-confidence CHCHD3–IMMT relationship and a lower-confidence AIFM1–MACROH2A1 relationship. These links are biologically compatible with the mitochondrial cristae component and the connection between mitochondrial and nuclear stress or chromatin processes, respectively. No hu.MAP complex contains multiple module members, so the module is not independently supported as a known protein complex. The lack of additional STRING or hu.MAP relationships means that most co-abundance edges should be interpreted as expression covariation rather than established physical interaction. EXD2 is a network hub by module connectivity, but its direct relationships to most module neighbors are not supported by the supplied STRING or hu.MAP evidence.

**STRING interactions (score >= 0.7)**: 2 of 55 gene pairs: AIFM1–MACROH2A1 (0.704); CHCHD3–IMMT (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a novel cross-tissue co-abundance pattern, but the evidence does not justify calling it a newly discovered biological mechanism. The module combines several known processes, especially mitochondrial organization, with intestinal epithelial structure, chromatin regulation, lipid metabolism, and DNA or RNA processing. Its sparse STRING support, absence of a multi-member hu.MAP complex, and lack of global GO/KEGG enrichment argue against a previously recognized coherent complex or pathway. Conversely, absence from STRING or hu.MAP alone cannot establish novelty, because co-abundance can arise from shared cell composition, coordinated regulation, or context-specific biology. The most defensible conclusion is that the cross-tissue association is potentially interesting but mechanistically unresolved.

**Hypothesis.** Hypothesis: the shared module reflects a coordinated cellular-state program in which mitochondrial maintenance and energy or metabolite handling are coupled to epithelial structural state and stress-responsive nuclear regulation. In this model, MICOS components CHCHD3 and IMMT maintain cristae architecture, AIFM1 and SLC25A1 connect mitochondrial integrity with apoptosis or metabolic flux, and EXD2 coordinates the module through its broad co-abundance connectivity and roles in nucleic-acid processing and DNA repair. MACROH2A1 could link mitochondrial or metabolic stress to chromatin regulation, while VIL1 and SH3BP1 could mark an epithelial cytoskeletal context. This is a testable hypothesis, not an enrichment result or an established physical assembly.

### Important genes

#### EXD2

- **Related proteins** (co-abundance neighbors): SLC25A1 (0.88), CDK5RAP3 (0.83), NSDHL (0.83), IMMT (0.82), MRPL19 (0.81), AIFM1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exonuclease 3'-5' domain containing 2. Enables 3'-5' exonuclease activity; metal ion binding activity; and protein homodimerization activity. Involved in nucleic acid metabolic process. Located in intermediate filament cytoskeleton; mitochondrial outer membrane; and site of DNA damage. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.339); intelligence (0.292); diabetes mellitus (0.285); heart disorder (0.265); musculoskeletal system disorder (0.238)
- **Europe PMC papers**: 155
- **Why important**: EXD2 has the highest connectivity in the module and links SLC25A1, CDK5RAP3, NSDHL, IMMT, MRPL19, and AIFM1. Its annotations span mitochondrial localization, nucleic-acid metabolism, RNA processing, replication-fork processing, and homologous-recombination repair. It therefore sits at the intersection of the module's mitochondrial and genome-maintenance signals and has a substantial literature base.
- **Conclusion**: Established: EXD2 is the principal network hub and has documented exonuclease and DNA-repair-related functions. Hypothesis: its hub position may reflect coordination between mitochondrial state and nucleic-acid stress, but the co-abundance data do not establish that EXD2 regulates the other genes.

#### IMMT

- **Related proteins** (co-abundance neighbors): CHCHD3 (0.86), EXD2 (0.82), MACROH2A1 (0.82); STRING partners: CHCHD3 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inner membrane mitochondrial protein. Enables RNA binding activity. Involved in cristae formation. Located in mitochondrial inner membrane. Part of MICOS complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); multinodular goiter (0.196); alcohol drinking (0.190); breast cancer (0.094); neoplasm (0.087)
- **Europe PMC papers**: 933
- **Why important**: IMMT is connected to EXD2, CHCHD3, and MACROH2A1 and is a core MICOS component required for mitochondrial inner-membrane organization and cristae formation. Its very strong STRING relationship with CHCHD3 provides the clearest established physical interaction within the module. It is also among the more extensively studied genes in this set.
- **Conclusion**: Established: IMMT is a mitochondrial cristae-organizing protein and is physically linked to CHCHD3 by STRING evidence. Hypothesis: IMMT may be a structural anchor for the mitochondrial part of the module, but no hu.MAP multi-member complex was supplied.

#### CHCHD3

- **Related proteins** (co-abundance neighbors): IMMT (0.86); STRING partners: IMMT (0.999)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coiled-coil-helix-coiled-coil-helix domain containing 3. The protein encoded by this gene is an inner mitochondrial membrane scaffold protein. Absence of the encoded protein affects the structural integrity of mitochondrial cristae and leads to reductions in ATP production, cell growth, and oxygen consumption. This protein is part of the mitochondrial contact site and cristae organizing system (MICOS). Several transcript variants encoding different isof…
- **Diseases (Open Targets)**: neurodegenerative disease (0.537); smoking initiation (0.414); intelligence (0.385); insomnia (0.362); mathematical ability (0.312)
- **Europe PMC papers**: 549
- **Why important**: CHCHD3 is directly connected to IMMT in the module and has the strongest supplied STRING interaction. It is a MICOS scaffold whose loss affects cristae integrity, ATP production, cell growth, and oxygen consumption. Its tissue enhancement in skeletal muscle and tongue is compatible with substantial mitochondrial demand, although it is not tissue-specific to the two sampled tissues.
- **Conclusion**: Established: CHCHD3 contributes to MICOS structure and mitochondrial cristae formation, and its relationship with IMMT is independently supported by STRING. Hypothesis: the CHCHD3–IMMT pair may represent the most mechanistically coherent subunit of the shared module.

#### VIL1

- **Related proteins** (co-abundance neighbors): SH3BP1 (0.81), MACROH2A1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: villin 1. This gene encodes a member of a family of calcium-regulated actin-binding proteins.  This protein represents a dominant part of the brush border cytoskeleton which functions in the capping, severing, and bundling of actin filaments.  Two mRNAs of 2.7 kb and 3.5 kb have been observed; they result from utilization of alternate poly-adenylation signals present in the terminal exon. [provided by RefSe…
- **Diseases (Open Targets)**: brain aneurysm (0.220); Barrett esophagus (0.084); neoplasm (0.067); cervical adenocarcinoma (0.061); esophageal adenocarcinoma (0.057)
- **Europe PMC papers**: 1564
- **Why important**: VIL1 is tissue-enriched in intestine and enhanced in colonocytes and enterocytes, making it the clearest marker of an intestinal epithelial component. It encodes an actin-binding protein involved in brush-border organization, cell shape, and intestinal glucose absorption. Its connection to SH3BP1 links epithelial actin architecture with a regulator of Rac signaling, cell motility, and epithelial junction formation.
- **Conclusion**: Established: VIL1 is an intestinal epithelial brush-border and actin-cytoskeleton protein, and its HPA pattern supports an epithelial contribution to the module. Hypothesis: VIL1 may indicate that the shared bone-marrow–rectum signal is partly driven by a common epithelial or structural cellular state rather than by a dedicated mitochondrial pathway.

#### AIFM1

- **Related proteins** (co-abundance neighbors): EXD2 (0.81); STRING partners: MACROH2A1 (0.704)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apoptosis inducing factor mitochondria associated 1. This gene encodes a flavoprotein essential for nuclear disassembly in apoptotic cells, and it is found in the mitochondrial intermembrane space in healthy cells. Induction of apoptosis results in the translocation of this protein to the nucleus where it affects chromosome condensation and fragmentation. In addition, this gene product induces mitochondria to release the apoptogenic proteins cytochr…
- **Diseases (Open Targets)**: severe X-linked mitochondrial encephalomyopathy (0.813); X-linked hereditary sensory and autonomic neuropathy with hearing loss (0.798); Charcot-Marie-Tooth disease X-linked recessive 4 (0.761); spondyloepimetaphyseal dysplasia, Bieganski type (0.747); combined oxidative phosphorylation deficiency (0.615)
- **Europe PMC papers**: 1952
- **Why important**: AIFM1 is connected to EXD2 in the co-abundance network and to MACROH2A1 in STRING. It combines mitochondrial respiratory-chain assembly with apoptosis, nuclear disassembly, and chromosome fragmentation, and it has extensive disease and literature support. Its established links to mitochondrial dysfunction make it a plausible functional bridge between organelle maintenance and stress responses.
- **Conclusion**: Established: AIFM1 is a mitochondrial flavoprotein involved in oxidative phosphorylation-related functions and apoptosis, with strong disease relevance. Hypothesis: its module association may reflect a shared mitochondrial stress or survival state, but the data do not demonstrate apoptotic activation in either tissue.

## Module 1

**Tissue pair**: bone_marrow and rectum  
**Genes (9)**: SLC3A2, AIMP1, CUX1, CTNND1, CUX1, HSD17B10, TMPO, NUP50, RCC1

### Function

No GO or KEGG term passed global correction, and STRING reported no supplementary functional enrichment. The module therefore does not support a specific pathway assignment from enrichment evidence. Its gene annotations instead suggest a mixed nuclear and cellular-regulation theme: CUX1 is a transcriptional regulator linked to differentiation and cell-cycle progression; TMPO is associated with nuclear-membrane organization, chromatin organization, replication, and cell-cycle control; RCC1 contributes to cell-cycle regulation, mitotic nuclear events, spindle organization, and chromosome segregation; NUP50 supports importin-mediated nuclear protein import and nucleocytoplasmic transport; CTNND1 supports cell adhesion and signal transduction; SLC3A2 supports amino-acid transport; HSD17B10 supports mitochondrial lipid metabolism and mitochondrial RNA processing; and AIMP1 has intracellular aminoacylation functions as well as cytokine, inflammatory, angiogenic, and wound-healing activities. The network pattern is dominated by CUX1, with the remaining genes connected sparsely, so the most defensible interpretation is a mixed co-abundance module involving nuclear regulation and transport together with cell-state, adhesion, metabolic, and inflammatory signals rather than a single established biological pathway.

**Cell composition.** The HPA profile is predominantly low in tissue specificity, with protein detected in bone marrow and rectum for nearly all genes having tissue protein data. This argues against a module composed mainly of tissue-exclusive proteins. Most genes also show low immune-cell specificity, although CUX1 is immune-cell enhanced in non-classical monocytes, CTNND1 is group enriched across monocyte and myeloid dendritic-cell categories, and TMPO is associated with erythrocyte, megakaryocyte, and monocyte progenitors. Several genes have scattered cell-type enhancement, including epithelial, trophoblast, retinal, and neutrophil categories, which is more consistent with broadly distributed or mixed cell-state signals than with a single purified lineage. AIMP1 is secreted to blood, so circulating protein or blood-derived material could contribute to its co-abundance. SLC3A2 lacks detected protein in both listed tissues, which weakens its use as a tissue-protein marker. Overall, the shared module could partly reflect common cell types, progenitor or myeloid content, or blood-related material in the samples rather than a rectum-and-bone-marrow-specific mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports only the RCC1-NUP50 relationship at the supplied confidence threshold. This is concordant with hu.MAP, where RCC1 and NUP50 occur together in both reported complexes (hu.MAP huMAP3_10000.1) and (hu.MAP huMAP3_12581.1). Those complexes contain many additional nucleoporins, import factors, Ran-system components, and mitotic regulators, so the RCC1-NUP50 pair represents an established nuclear transport and nuclear-organization connection. The other co-abundance relationships, especially the many links incident on CUX1, are not supported by STRING or hu.MAP in the supplied evidence. Thus, the module contains a small known nuclear-complex signal embedded in a broader set of correlations that may reflect co-expression, shared cell composition, or indirect regulation rather than physical binding.

**STRING interactions (score >= 0.7)**: 1 of 36 gene pairs: NUP50–RCC1 (0.75)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10000.1 (RCC1, NUP50; 2/44); huMAP3_12581.1 (RCC1, NUP50; 2/58)

### Novelty

This module should not be called a new molecular complex or a newly established pathway. The RCC1-NUP50 relationship and their joint occurrence in hu.MAP complexes are already known, while the remaining module relationships lack corresponding support in STRING or hu.MAP. The co-abundance pattern across bone marrow and rectum may still be a novel observation in this particular tissue comparison, but absence from interaction resources does not establish novelty. The lack of globally significant GO or KEGG enrichment, the sparse known interaction structure, the broad HPA expression profile, and the possibility of shared blood or progenitor-cell content all make a strong mechanistic novelty claim premature. Independent replication, cell-composition adjustment, and validation of the co-abundance relationships would be needed.

**Hypothesis.** Hypothesis: the module may reflect a shared proliferative or progenitor-associated cell-state program in bone marrow and rectum, with CUX1 coordinating transcriptional state, TMPO supporting nuclear-envelope and chromatin organization, RCC1 and NUP50 contributing nuclear transport and mitotic nuclear functions, and CTNND1, AIMP1, and SLC3A2 capturing adhesion, inflammatory, and nutrient-transport aspects of that state. The apparent module may therefore arise from coordinated abundance across a mixture of progenitor, myeloid, epithelial, and circulating components rather than from a single physical complex. This hypothesis predicts that the module signal should weaken after adjustment for cell composition and should be strongest in samples enriched for proliferative or myeloid-associated cellular states.

### Important genes

#### CUX1

- **Related proteins** (co-abundance neighbors): CUX1 (0.96), AIMP1 (0.90), CTNND1 (0.85), RCC1 (0.84), TMPO (0.84), SLC3A2 (0.84), HSD17B10 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Golgi apparatus; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cut like homeobox 1. The protein encoded by this gene is a member of the homeodomain family of DNA binding proteins. It may regulate gene expression, morphogenesis, and differentiation and it may also play a role in the cell cycle progession. Several alternatively spliced transcript variants encoding different isoforms have been identified.[provided by RefSeq, Feb 2011].
- **Diseases (Open Targets)**: global developmental delay with or without impaired intellectual development (0.754); cancer (0.588); myelodysplastic syndrome (0.536); hereditary disease (0.519); acute lymphoblastic leukemia (0.509)
- **Europe PMC papers**: 3914
- **Why important**: CUX1 is the central network gene, with the greatest connectivity and links to nearly every other listed module member. It is a homeodomain DNA-binding protein involved in transcriptional regulation, morphogenesis, differentiation, and cell-cycle progression. HPA links it to neutrophils and non-classical monocytes, while Open Targets connects it with developmental disorders, cancer, myelodysplastic syndrome, and acute lymphoblastic leukemia. Its substantial literature volume makes it the strongest candidate for interpreting the module's regulatory axis.
- **Conclusion**: Established evidence supports CUX1 as a transcriptional and cell-state regulator and as the network hub. It is plausible that CUX1 helps organize the shared co-abundance pattern, but the data do not establish that it directly regulates the other module genes or causes the tissue-sharing signal.

#### TMPO

- **Related proteins** (co-abundance neighbors): CUX1 (0.88), CUX1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thymopoietin. Through alternative splicing, this gene encodes several distinct LEM domain containing protein isoforms. LEM domain proteins include inner nuclear membrane and intranuclear proteins, and are involved in a variety of cellular functions including gene expression, chromatin organization, and replication and cell cycle control. The encoded alpha isoform is broadly diffuse in the nucleus and contains a…
- **Diseases (Open Targets)**: neurodegenerative disease (0.524); familial isolated dilated cardiomyopathy (0.371); migraine disorder (0.359); alcohol drinking (0.272); iris disorder (0.235)
- **Europe PMC papers**: 1474
- **Why important**: TMPO is directly connected to the module hub and is tissue enhanced in lymphoid tissue. Its HPA single-cell associations include erythrocyte, megakaryocyte, and monocyte progenitors. TMPO encodes LEM-domain protein isoforms involved in nuclear organization, chromatin organization, replication, and cell-cycle control, making it a biologically coherent bridge between the module's cell-state signal and its nuclear component. It also has disease associations involving neurodegeneration, cardiomyopathy, migraine, and iris disorders.
- **Conclusion**: Established evidence supports TMPO as a nuclear-organization and progenitor-associated gene. Its co-abundance with CUX1 is consistent with a shared nuclear or proliferative cell state, but a direct functional relationship within this module remains hypothetical.

#### RCC1

- **Related proteins** (co-abundance neighbors): CUX1 (0.84); STRING partners: NUP50 (0.75)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_10000.1, huMAP3_12581.1
- **Function (MyGene.info)**: regulator of chromosome condensation 1. Enables several functions, including guanyl-nucleotide exchange factor activity; nucleosomal DNA binding activity; and protein heterodimerization activity. Involved in several processes, including G1/S transition of mitotic cell cycle; regulation of mitotic nuclear division; and spindle organization. Located in chromatin; cytoplasm; and nucleus. Part of protein-containing complex. [provided by All…
- **Diseases (Open Targets)**: injury (0.338); neurodegenerative disease (0.338); myasthenia gravis (0.329); neoplasm (0.104); cancer (0.091)
- **Europe PMC papers**: 3525
- **Why important**: RCC1 is connected to CUX1 and forms the most clearly established physical-interaction signal in the module through its relationship with NUP50. It has recognized roles in guanyl-nucleotide exchange, chromosome segregation, mitotic nuclear reassembly, spindle organization, and cell-cycle regulation. It is also present with NUP50 in both hu.MAP complexes (hu.MAP huMAP3_10000.1) and (hu.MAP huMAP3_12581.1), giving it stronger complex-level support than most module genes.
- **Conclusion**: Established evidence supports RCC1 as a nuclear and mitotic regulator and supports its complex-level relationship with NUP50. Its role as a mechanistic driver of the complete module is not established; it may instead mark a shared proliferative or nuclear state.

#### NUP50

- **Related proteins** (co-abundance neighbors): CUX1 (0.84); STRING partners: RCC1 (0.75)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_10000.1, huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 50. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. The protein encoded by this gene is a member of the FG-repeat containing nucleoporins that functions as a soluble cofactor in…
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.527); Histiocytosis (0.370); COVID-19 (0.370)
- **Europe PMC papers**: 851
- **Why important**: NUP50 is connected to RCC1 in STRING and occurs with RCC1 in both hu.MAP complexes (hu.MAP huMAP3_10000.1) and (hu.MAP huMAP3_12581.1). It is a nucleoporin and soluble cofactor for importin-alpha-beta-mediated nuclear protein import, linking the module to nucleocytoplasmic transport. HPA places it in nucleoplasm and nuclear membrane and shows enhancement in conjunctival goblet and esophageal apical cells, consistent with a broadly distributed transport function rather than a tissue-exclusive role.
- **Conclusion**: Established evidence supports NUP50 as a nuclear-import factor and supports its relationship with RCC1. The module data do not show that NUP50 connects physically or functionally to the CUX1-centered portion beyond their co-abundance.

#### CTNND1

- **Related proteins** (co-abundance neighbors): CUX1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin delta 1. This gene encodes a member of the Armadillo protein family, which function in adhesion between cells and signal transduction. Multiple translation initiation codons and alternative splicing result in many different isoforms being translated. Not all of the full-length natures of the described transcript variants have been determined. Read-through transcription also exists between this gene and the…
- **Diseases (Open Targets)**: blepharocheilodontic syndrome (0.724); listeriosis (0.526); cleft lip (0.510); hereditary disease (0.415); exudative vitreoretinopathy (0.376)
- **Europe PMC papers**: 3021
- **Why important**: CTNND1 is connected to CUX1 and encodes a catenin-family protein involved in cell-cell adhesion and signal transduction. HPA associates it with several epithelial and neural-related cell types and with classical, intermediate, and non-classical monocytes and myeloid dendritic cells. Its plasma-membrane localization and disease associations involving developmental and infectious phenotypes provide a plausible link between tissue architecture, immune-cell composition, and the module signal.
- **Conclusion**: Established evidence supports CTNND1 as an adhesion and signaling protein with broad cellular relevance. Its placement beside CUX1 may reflect coordinated cell-state or tissue-composition effects, but a direct CUX1-CTNND1 mechanism is not demonstrated.

#### AIMP1

- **Related proteins** (co-abundance neighbors): CUX1 (0.90), CUX1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aminoacyl tRNA synthetase complex interacting multifunctional protein 1. The protein encoded by this gene is a cytokine that is specifically induced by apoptosis, and it is involved in the control of angiogenesis, inflammation, and wound healing. The release of this cytokine renders the tumor-associated vasculature sensitive to tumor necrosis factor. The precursor protein is identical to the p43 subunit, which is associated with the multi-tRNA synthetase complex, and i…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 3 (0.790); Pelizaeus-Merzbacher-like disease (0.657); POLR-related leukodystrophy (0.657); leukodystrophy (0.372); autosomal recessive non-syndromic intellectual disability (0.371)
- **Europe PMC papers**: 663
- **Why important**: AIMP1 is connected to CUX1 and is distinctive because it is secreted to blood while also functioning as a component-associated aminoacylation factor. Its annotations include cytokine activity, inflammation, angiogenesis, wound healing, leukocyte migration, and protein translation. This makes it important for assessing whether circulating or blood-derived material contributes to the shared module. Its disease associations include several leukodystrophy-related conditions.
- **Conclusion**: Established evidence supports AIMP1 as a multifunctional translation-associated and inflammatory protein with a circulating form. Its inclusion may indicate inflammatory or blood-related sample composition, but it does not establish that secreted AIMP1 drives the nuclear-regulatory relationships in the module.

## Module 2

**Tissue pair**: bone_marrow and rectum  
**Genes (7)**: ACIN1, DNM1L, GPD2, MCCC1, UPF1, RO60, TMLHE

### Function

The module does not have a statistically supported GO or KEGG functional label: no GO or KEGG term passed global correction. Its strongest internal organization is centered on TMLHE, which is connected to every other module member, while the remaining genes form a set of links to this hub rather than a densely interconnected network. The gene annotations suggest a mixed biological signal involving mitochondrial metabolism and quality control, RNA processing and surveillance, apoptosis-related nuclear events, and cellular redox or glycerol-phosphate metabolism. This is therefore best interpreted as a coordinated mitochondrial and cellular-maintenance expression pattern, not as proof of one narrowly defined pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: none of the genes is annotated as secreted. All module proteins are detected in bone marrow, and nearly all are detected in rectum. HPA reports low tissue specificity for every gene, so the shared signal is not tissue-exclusive. Most genes also have low immune-cell specificity, with UPF1 not detected in immune cells. GPD2 is the main blood-related exception, showing group-enriched expression across myeloid cell types and enhancement in neutrophil progenitors. The HPA profile therefore does not support a simple plasma-protein explanation or a uniformly blood-cell-specific module, although myeloid-cell composition could contribute to part of the shared pattern.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING reports no high-confidence interactions among the module genes and no supplementary STRING enrichment. This means the co-abundance links are not recapitulated by the supplied STRING interaction network and should not be presented as established physical interactions. hu.MAP provides two relevant complexes, C1 and C2, each containing MCCC1 and TMLHE, but each complex includes many additional proteins and only these two module members. This supports an established relationship of MCCC1 and TMLHE with broad mitochondrial or metabolic machinery, while providing no comparable complex evidence for the other module genes. The module is consequently a co-expression or co-abundance pattern with limited support from known protein-interaction structure.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10525.1 (MCCC1, TMLHE; 2/33); huMAP3_13468.1 (MCCC1, TMLHE; 2/99)

### Novelty

The shared co-abundance pattern may be a new observation because the module links genes from mitochondrial metabolism, mitochondrial dynamics, RNA surveillance, apoptosis-related nuclear biology, and glycerol-phosphate metabolism without support from STRING interactions or a single globally significant GO or KEGG term. However, it cannot be called a newly discovered biological complex or pathway. Absence from STRING and hu.MAP alone does not establish novelty, and the sparse star-like network, broad tissue expression, and lack of globally corrected enrichment also allow a shared cell-state, metabolic-state, or sample-composition explanation. The defensible conclusion is that the cross-tissue module is potentially novel as a co-abundance pattern, but its mechanistic novelty remains unproven.

**Hypothesis.** Hypothesis: the module reflects coordinated variation in mitochondrial energetic state and cellular quality control across bone marrow and rectal samples. TMLHE and MCCC1 could represent mitochondrial substrate and branched-chain amino-acid or carnitine-related metabolism, GPD2 could reflect redox balancing through the glycerol-phosphate shuttle, and DNM1L could reflect mitochondrial remodeling. The accompanying association with UPF1, RO60, and ACIN1 could indicate coupled RNA surveillance, RNA regulation, and stress or apoptotic responses. This hypothesis is consistent with the annotations and the hub-centered network, but it is not established by enrichment, STRING, or hu.MAP evidence.

### Important genes

#### TMLHE

- **Related proteins** (co-abundance neighbors): RO60 (0.90), ACIN1 (0.88), MCCC1 (0.87), UPF1 (0.87), DNM1L (0.86), GPD2 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_10525.1, huMAP3_13468.1
- **Function (MyGene.info)**: trimethyllysine hydroxylase, epsilon. This gene encodes the protein trimethyllysine dioxygenase which is the first enzyme in the carnitine biosynthesis pathway. Carnitine play an essential role in the transport of activated fatty acids across the inner mitochondrial membrane. The encoded protein converts trimethyllysine into hydroxytrimethyllysine. A pseudogene of this gene is found on chromosome X. Alternate splicing results in multi…
- **Diseases (Open Targets)**: autism (0.576); isolated cerebellar hypoplasia/agenesis (0.259); Agenesis of corpus callosum (0.259); Cerebellar vermis hypoplasia (0.259); Hashimoto thyroiditis (0.206)
- **Europe PMC papers**: 353
- **Why important**: TMLHE is the central network gene, connected to every other module member with comparatively strong co-abundance links. It encodes trimethyllysine dioxygenase, the first enzyme in carnitine biosynthesis, and is located in mitochondria. Its position makes it the principal candidate for organizing the observed module-level signal, although it has no STRING partner or globally significant GO or KEGG annotation in this module. Its literature volume is moderate, and Open Targets links it most strongly in the supplied evidence to autism.
- **Conclusion**: Established: TMLHE is a mitochondrial carnitine-biosynthesis enzyme and the module hub. Hypothesis: variation in mitochondrial fatty-acid transport capacity may help coordinate the other module genes. The network position supports prioritizing TMLHE, but does not demonstrate that it regulates the other genes.

#### MCCC1

- **Related proteins** (co-abundance neighbors): TMLHE (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_10525.1, huMAP3_13468.1
- **Function (MyGene.info)**: methylcrotonyl-CoA carboxylase subunit 1. This gene encodes the large subunit of 3-methylcrotonyl-CoA carboxylase. This enzyme functions as a heterodimer and catalyzes the carboxylation of 3-methylcrotonyl-CoA to form 3-methylglutaconyl-CoA. Mutations in this gene are associated with 3-Methylcrotonylglycinuria, an autosomal recessive disorder of leucine catabolism. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: 3-methylcrotonyl-CoA carboxylase deficiency (0.856); hereditary disease (0.452); Parkinson disease (0.404); neurodegenerative disease (0.387); Lewy body dementia (0.214)
- **Europe PMC papers**: 756
- **Why important**: MCCC1 is directly connected to the TMLHE hub and is one of the two module genes represented in both hu.MAP complexes, C1 and C2. It encodes the large subunit of methylcrotonyl-CoA carboxylase, an enzyme involved in leucine and branched-chain amino-acid catabolism. It is detected in both tissues, has low tissue specificity, and has a well-established deficiency phenotype in the supplied disease evidence.
- **Conclusion**: Established: MCCC1 participates in mitochondrial branched-chain amino-acid catabolism and is associated with methylcrotonyl-CoA carboxylase deficiency. Hypothesis: its co-abundance with TMLHE may mark coordinated mitochondrial substrate handling. The hu.MAP support indicates membership in broad complexes, not a module-specific physical interaction.

#### GPD2

- **Related proteins** (co-abundance neighbors): TMLHE (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Mitochondria; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycerol-3-phosphate dehydrogenase 2. The protein encoded by this gene localizes to the inner mitochondrial membrane and catalyzes the conversion of glycerol-3-phosphate to dihydroxyacetone phosphate, using FAD as a cofactor. Along with GDP1, the encoded protein constitutes the glycerol phosphate shuttle, which reoxidizes NADH formed during glycolysis. Two transcript variants encoding the same protein have been found for this gene.[pr…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.709); diabetes mellitus (0.597); obstructive sleep apnea syndrome (0.424); polycystic ovary syndrome (0.419); obesity disorder (0.415)
- **Europe PMC papers**: 1990
- **Why important**: GPD2 is directly linked to TMLHE and encodes the mitochondrial glycerol-3-phosphate dehydrogenase component of the glycerol-phosphate shuttle, which reoxidizes glycolytic NADH. It is the clearest HPA blood-related signal in the module, with group-enriched expression across several myeloid cell types and enhancement in neutrophil progenitors. It therefore helps connect the metabolic interpretation with a possible bone-marrow or myeloid contribution.
- **Conclusion**: Established: GPD2 supports mitochondrial redox and glycerol-phosphate metabolism and shows myeloid-associated HPA expression. Hypothesis: GPD2 may reflect metabolic differences in myeloid-cell abundance or activation that contribute to the shared module. The evidence does not establish that the module is a myeloid-specific program.

#### DNM1L

- **Related proteins** (co-abundance neighbors): TMLHE (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 1L. This gene encodes a member of the dynamin superfamily of GTPases. The encoded protein mediates mitochondrial and peroxisomal division, and is involved in developmentally regulated apoptosis and programmed necrosis. Dysfunction of this gene is implicated in several neurological disorders, including Alzheimer's disease. Mutations in this gene are associated with the autosomal dominant disorder, ence…
- **Diseases (Open Targets)**: encephalopathy, lethal, due to defective mitochondrial peroxisomal fission 1 (0.815); autosomal dominant optic atrophy, classic form (0.721); neurodegenerative disease (0.531); encephalopathy due to mitochondrial and peroxisomal fission defect (0.455); hereditary disease (0.451)
- **Europe PMC papers**: 3015
- **Why important**: DNM1L is directly connected to the TMLHE hub and encodes a dynamin-family GTPase involved in mitochondrial and peroxisomal fission, organelle organization, and apoptosis-related mitochondrial fragmentation. It has substantial literature and strong supplied disease associations involving defective mitochondrial or peroxisomal fission and neurological disease. Its annotation adds mitochondrial structural remodeling to the metabolic signals represented by TMLHE, MCCC1, and GPD2.
- **Conclusion**: Established: DNM1L is a mitochondrial and peroxisomal division factor with disease associations involving defective organelle fission. Hypothesis: its co-abundance with mitochondrial metabolic genes may indicate coordinated control of mitochondrial content and activity. The module data do not show a direct DNM1L interaction with those metabolic proteins.

#### UPF1

- **Related proteins** (co-abundance neighbors): TMLHE (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UPF1 RNA helicase and ATPase. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons.…
- **Diseases (Open Targets)**: Intellectual disability (0.437); Global developmental delay (0.426); High anterior hairline (0.425); Frontal bossing (0.425); Hypertelorism (0.425)
- **Europe PMC papers**: 4252
- **Why important**: UPF1 is directly connected to TMLHE and is a major component of messenger-RNA surveillance, nonsense-mediated decay, RNA export, and translational termination regulation. It has the largest literature volume among the module genes in the supplied evidence and is associated with developmental and intellectual-disability phenotypes in Open Targets. Its low immune-cell specificity and detection in both tissues make it a plausible broadly expressed cellular-maintenance component rather than a tissue-specific marker.
- **Conclusion**: Established: UPF1 is a central RNA-surveillance and mRNA-quality-control factor with broad cellular relevance. Hypothesis: its co-abundance with the mitochondrial genes may reflect a shared cellular stress or biosynthetic state linking RNA quality control to organelle function. The module does not establish such a mechanistic coupling.

## Module 3

**Tissue pair**: bone_marrow and rectum  
**Genes (38)**: ACLY, ALDOC, BYSL, C1QBP, MTHFD1, CAPRIN1, CLTC, COPB1, DDX21, DDX5, DDX6, EIF2AK2, EIF3L, FUCA2, SHMT2, HNRNPK, HNRNPR, HYOU1, IQGAP1, MATR3, MCM6, SNU13, PDLIM1, PHB1, PHB2, PSMC6, PSMA4, PSMD13, PTBP1, RUVBL2, SUPT16H, STAT1, CCT5, CCT3, CCT7, CCT8, TFRC, TTN

### Function

The strongest interpretation is a broadly expressed protein-folding and RNA-processing module, with a particularly coherent CCT chaperonin submodule. The CCT genes CCT3, CCT5, CCT7 and CCT8 are jointly supported by the globally corrected terms for chaperonin-containing T-complex and ATP-dependent protein folding (GO:CC chaperonin-containing T-complex; q_global = 0.000821), (GO:CC protein folding chaperone complex; q_global = 0.00419), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.00641), (GO:MF unfolded protein binding; q_global = 0.0138) and (GO:MF protein folding chaperone; q_global = 0.0485). The same genes, together with RUVBL2, are associated with RNA and telomerase-RNA localization to the nucleus and Cajal body (7 globally significant GO/KEGG terms, q_global 3.61e-05–0.000821; see the table), (6 globally significant GO/KEGG terms, q_global 0.00285–0.00285; see the table), (GO:BP regulation of telomere maintenance via telomerase; q_global = 0.0068), (GO:BP positive regulation of telomere maintenance via telomere lengthening; q_global = 0.0068), (GO:BP regulation of telomere maintenance via telomere lengthening; q_global = 0.0132), (GO:BP positive regulation of telomere maintenance; q_global = 0.0177), (GO:BP positive regulation of DNA biosynthetic process; q_global = 0.0351) and (GO:BP regulation of telomere maintenance; q_global = 0.0485). These localization terms are biologically plausible for a module containing chaperones, RNA helicases and nuclear RNA-binding proteins, but they should not be interpreted as proof that the entire module directly controls telomerase. The broader module is also enriched for macromolecule biosynthesis, gene expression, primary metabolism, RNA binding and regulation of biosynthetic processes (GO:BP regulation of macromolecule biosynthetic process; q_global = 0.00131), (GO:BP macromolecule biosynthetic process; q_global = 0.00204), (GO:BP gene expression; q_global = 0.00289), (GO:BP regulation of biosynthetic process; q_global = 0.00417), (GO:BP regulation of macromolecule metabolic process; q_global = 0.00631), (GO:BP biosynthetic process; q_global = 0.00679), (GO:BP macromolecule metabolic process; q_global = 0.00827), (GO:BP positive regulation of macromolecule biosynthetic process; q_global = 0.0136), (GO:MF ATP hydrolysis activity; q_global = 0.0173), (7 globally significant GO/KEGG terms, q_global 0.0185–0.027; see the table). Taken together, the module most likely reflects coordinated maintenance of protein folding, RNA handling, translation-related biosynthetic capacity, proteostasis and proliferative or metabolically active cell states.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module. HPA indicates that most genes have low tissue specificity and low immune-cell specificity, while only a minority are secreted or secreted to blood. FUCA2 is secreted to blood, and TFRC and C1QBP are also annotated as secreted to blood, but these genes do not dominate the module. The broad HPA expression pattern supports a housekeeping-like component rather than a specialized rectal or bone-marrow tissue program. There is nevertheless evidence for a shared cellular-composition contribution. STRING supplementary tissue annotations point toward blood, hematopoietic cells, lymphocytes and blood cancer or leukemia-related cells (STRING TISSUES Blood cancer cell; within-query FDR = 1.11e-06), (STRING TISSUES Lymphoblast; within-query FDR = 1.11e-06), (STRING TISSUES Leukemia cell; within-query FDR = 7.06e-06) (STRING TISSUES Lymphocyte; within-query FDR = 0.00031) (STRING TISSUES Hematopoietic cell; within-query FDR = 0.00072), (STRING TISSUES Blood; within-query FDR = 0.0043). HPA additionally links MCM6, TFRC, SUPT16H and other genes to erythroid or myeloid progenitors, while PDLIM1 has blood-cell group enrichment and TFRC has immune-cell enhancement. Therefore, the shared module may partly reflect proliferating or immature hematopoietic cells present in bone marrow and related cell populations in rectum samples, superimposed on a broadly expressed intracellular program. Protein detection in both tissues for most genes is consistent with a real shared tissue signal, although HYOU1, FUCA2, ALDOC and TTN show tissue-detection patterns that caution against treating every member as equally representative of both tissues.

**GO/KEGG enrichment**: 42 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA localization to Cajal body | 3.61e-05 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP telomerase RNA localization to Cajal body | 3.61e-05 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP telomerase RNA localization | 3.61e-05 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP RNA localization to nucleus | 3.61e-05 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:CC chaperonin-containing T-complex | 0.000821 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 0.000821 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 0.000821 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of macromolecule biosynthetic process | 0.00131 | C1QBP, CAPRIN1, CCT3, CCT5, CCT7, CCT8, CLTC, DDX21, DDX5, DDX6, EIF2AK2, HNRNPK, IQGAP1, MATR3, PDLIM1, PHB1, PHB2, PSMC6, PTBP1, RUVBL2, SHMT2, STAT1, SUPT16H, TFRC, TTN |
| GO:BP macromolecule biosynthetic process | 0.00204 | BYSL, C1QBP, CAPRIN1, CCT3, CCT5, CCT7, CCT8, CLTC, DDX21, DDX5, DDX6, EIF2AK2, EIF3L, HNRNPK, HNRNPR, HYOU1, IQGAP1, MATR3, PDLIM1, PHB1, PHB2, PSMC6, PTBP1, RUVBL2, SHMT2, SNU13, STAT1, SUPT16H, TFRC, TTN |
| GO:BP binding of sperm to zona pellucida | 0.00285 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 0.00285 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 0.00285 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 0.00285 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 0.00285 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 0.00285 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING supports several established substructures within the co-abundance network. The CCT3–CCT5–CCT7–CCT8 group forms a highly coherent chaperonin clique, with RUVBL2 connected to this group. Additional known relationships include the PHB1–PHB2 prohibitin pair, the proteasome group involving PSMA4, PSMC6 and PSMD13, the RNA-binding and RNA-processing group involving DDX5, HNRNPK, HNRNPR, MATR3 and PTBP1, the MTHFD1–SHMT2 metabolic pair, and the EIF2AK2–STAT1 relationship. These links indicate that substantial parts of the module recover known molecular machinery rather than arbitrary correlations. hu.MAP independently supports repeated CCT-containing complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), RNA-binding assemblies containing HNRNPR, MATR3 and HNRNPK (hu.MAP huMAP3_10625.1), mitochondrial or membrane-associated assemblies containing TFRC and prohibitin proteins (hu.MAP huMAP3_10725.1), proteasome assemblies (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1), (hu.MAP huMAP3_05064.1), and RNA granule or RNA-processing assemblies involving DDX5, CAPRIN1 and DDX6 (hu.MAP huMAP3_05711.1) (hu.MAP huMAP3_07909.1) (hu.MAP huMAP3_09754.1) (hu.MAP huMAP3_10207.1) (hu.MAP huMAP3_09671.1) (hu.MAP huMAP3_11743.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10631.1) (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_11111.1). The fact that several complexes contain only a subset of their full members means the module is not a single purified complex. It is better viewed as a co-abundance neighborhood that joins several interacting systems, especially chaperoning, RNA metabolism, proteasome function, mitochondrial organization and biosynthetic activity.

**STRING interactions (score >= 0.7)**: 36 of 703 gene pairs: ACLY–MTHFD1 (0.723); BYSL–SNU13 (0.992); C1QBP–PHB1 (0.847); C1QBP–PHB2 (0.964); CAPRIN1–DDX6 (0.724); CAPRIN1–STAT1 (0.77); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT3–RUVBL2 (0.766); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT5–RUVBL2 (0.705); CCT7–CCT8 (0.999); CCT7–RUVBL2 (0.802); CCT8–PSMA4 (0.731); CCT8–RUVBL2 (0.776); CLTC–TFRC (0.84); DDX21–HNRNPR (0.73); DDX5–HNRNPK (0.935); DDX5–HNRNPR (0.844); DDX5–MATR3 (0.894); DDX6–HNRNPK (0.748); EIF2AK2–STAT1 (0.98); HNRNPK–HNRNPR (0.962); HNRNPK–MATR3 (0.923); HNRNPK–PTBP1 (0.997); HNRNPR–MATR3 (0.714); HNRNPR–PTBP1 (0.875); MATR3–PTBP1 (0.83); MTHFD1–SHMT2 (0.996); PHB1–PHB2 (0.999); PSMA4–PSMC6 (0.999); PSMA4–PSMD13 (0.998); PSMC6–PSMD13 (0.999); RUVBL2–SNU13 (0.869)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Blood cancer cell (FDR = 1.11e-06, 23 genes); TISSUES Liver (FDR = 1.11e-06, 32 genes); TISSUES Lymphoblast (FDR = 1.11e-06, 13 genes); TISSUES Digestive gland (FDR = 7.06e-06, 33 genes); TISSUES Leukemia cell (FDR = 7.06e-06, 20 genes); TISSUES Lymphocyte (FDR = 0.00031, 14 genes); TISSUES Hematopoietic cell (FDR = 0.00072, 15 genes); Process Regulation of macromolecule biosynthetic process (FDR = 0.0015, 22 genes); Process Positive regulation of telomerase RNA localization to Cajal body (FDR = 0.0022, 5 genes); Pfam TCP-1/cpn60 chaperonin family (FDR = 0.0032, 4 genes); TISSUES Blood (FDR = 0.0043, 20 genes); TISSUES Embryonic structure (FDR = 0.0055, 22 genes); Function ATP hydrolysis activity (FDR = 0.0057, 10 genes); Function ATP-dependent protein folding chaperone (FDR = 0.0057, 5 genes); Process Regulation of cellular biosynthetic process (FDR = 0.0063, 21 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_10625.1 (HNRNPR, MATR3, HNRNPK; 3/57); huMAP3_10725.1 (TFRC, PHB1, PHB2; 3/59); huMAP3_09656.1 (PSMA4, PSMC6, PSMD13; 3/64); huMAP3_13725.1 (PSMA4, PSMC6, PSMD13; 3/69); huMAP3_01706.1 (PHB1, PHB2; 2/2); huMAP3_05711.1 (DDX5, CAPRIN1; 2/8); huMAP3_07909.1 (DDX5, CAPRIN1; 2/8); huMAP3_09754.1 (DDX5, CAPRIN1; 2/9); huMAP3_10207.1 (DDX6, CAPRIN1; 2/9); huMAP3_09671.1 (PHB1, PHB2; 2/10); huMAP3_11743.1 (PHB1, PHB2; 2/10); huMAP3_07581.1 (HNRNPR, MATR3; 2/21); huMAP3_10631.1 (DDX5, CAPRIN1; 2/28); huMAP3_10659.1 (HNRNPR, HNRNPK; 2/28); huMAP3_11111.1 (DDX5, CAPRIN1; 2/29); huMAP3_05064.1 (PSMC6, PSMD13; 2/31); huMAP3_10862.1 (MCM6, SUPT16H; 2/33); huMAP3_14306.1 (MCM6, RUVBL2; 2/55); huMAP3_06775.1 (FUCA2, HYOU1; 2/60); huMAP3_09327.1 (FUCA2, HYOU1; 2/93)

### Novelty

The underlying molecular functions are not new: the CCT chaperonin, RNA-binding assemblies, proteasome, prohibitin complex, metabolic enzymes and DNA-replication machinery are already represented by STRING and hu.MAP evidence. The module therefore should not be presented as discovery of a new protein complex or an unrecognized function. A potentially novel aspect is the conserved co-abundance of these established systems across bone marrow and rectum. The fact sheet does not provide a prior cross-tissue module, an external replication set or a published equivalent, so module-level novelty remains possible but unproven. The presence of many broadly expressed housekeeping genes and several known complexes also provides a parsimonious alternative explanation: the conservation may reflect shared proliferative, biosynthetic or cell-composition states. Absence of some relationships from STRING or hu.MAP, such as the lack of STRING partners for MCM6, does not establish novelty because database coverage, context dependence and incomplete complex membership can all explain missing links.

**Hypothesis.** Hypothesis: in both bone marrow and rectum, a shared population of metabolically active and partly proliferative cells coordinates CCT-mediated folding of newly synthesized proteins with RNA processing, translation control, proteasome turnover, mitochondrial metabolism and iron uptake. The CCT submodule may support maturation of proteins required for nuclear RNA handling and cell-cycle or telomere-associated processes, while DDX5, HNRNPK, HNRNPR and related factors regulate RNA processing and localization. MCM6 could mark DNA-replication competence, TFRC could support iron-dependent biosynthetic demand, and PHB1–PHB2 with SHMT2 and MTHFD1 could contribute to mitochondrial and one-carbon metabolic support. This is a mechanistic model generated from network convergence and annotations, not a demonstrated causal pathway. It should be tested by cell-type-resolved expression, perturbation of the CCT or RNA-processing components, and replication in independent bone-marrow and rectal cohorts.

### Important genes

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT3 (0.88), HNRNPR (0.88), DDX21 (0.87), CCT7 (0.87), PHB1 (0.86), MTHFD1 (0.85), CAPRIN1 (0.85), DDX5 (0.84), HNRNPK (0.84), SUPT16H (0.83), MCM6 (0.83), ALDOC (0.82), EIF3L (0.82), RUVBL2 (0.81), MATR3 (0.81), PDLIM1 (0.80); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999), PSMA4 (0.731), RUVBL2 (0.776)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is among the most central genes in the module and is connected to the other CCT subunits, RUVBL2, RNA-processing factors, metabolic genes and prohibitin proteins. It is present in essentially the full set of globally corrected CCT, protein-folding, RNA-localization and biosynthetic annotations (42 globally significant GO/KEGG terms, q_global 3.61e-05–0.0485; see the table). STRING and hu.MAP independently place it in the CCT chaperonin complex (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1), and its broad HPA profile is compatible with a shared housekeeping program. It has extensive literature coverage and disease links including cancer-related associations in Open Targets.
- **Conclusion**: Established evidence supports CCT8 as a central component of the CCT chaperonin machinery and as a strong marker of the module's protein-folding axis. Its position also makes it a plausible bridge between chaperoning and the module's RNA or biosynthetic signals. A direct role for CCT8 in the tissue-shared co-abundance mechanism remains a hypothesis rather than a demonstrated causal conclusion.

#### DDX5

- **Related proteins** (co-abundance neighbors): HNRNPR (0.87), CCT7 (0.85), CCT8 (0.84), MTHFD1 (0.83), RUVBL2 (0.82), DDX6 (0.82), SHMT2 (0.80), SNU13 (0.80); STRING partners: HNRNPK (0.935), HNRNPR (0.844), MATR3 (0.894)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_05711.1, huMAP3_07909.1, huMAP3_09754.1, huMAP3_10631.1, huMAP3_11111.1
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 has high network connectivity and links the CCT neighborhood to HNRNPK, HNRNPR, MATR3, DDX6, RUVBL2 and SNU13. It participates in globally corrected macromolecule biosynthesis, gene-expression and mRNA-binding terms (GO:BP regulation of macromolecule biosynthetic process; q_global = 0.00131), (GO:BP macromolecule biosynthetic process; q_global = 0.00204), (GO:BP gene expression; q_global = 0.00289), (GO:BP regulation of biosynthetic process; q_global = 0.00417), (GO:BP regulation of macromolecule metabolic process; q_global = 0.00631), (GO:BP biosynthetic process; q_global = 0.00679), (GO:BP macromolecule metabolic process; q_global = 0.00827), (GO:MF ATP hydrolysis activity; q_global = 0.0173), (4 globally significant GO/KEGG terms, q_global 0.0185–0.0204; see the table). STRING supports its relationships with HNRNPK, HNRNPR and MATR3, while hu.MAP places it in several RNA-processing and RNA-granule assemblies (hu.MAP huMAP3_05711.1) (hu.MAP huMAP3_07909.1) (hu.MAP huMAP3_09754.1), (hu.MAP huMAP3_10631.1), (hu.MAP huMAP3_11111.1). DDX5 has substantial literature coverage and established associations with RNA processing, transcriptional regulation, viral disease and colorectal cancer.
- **Conclusion**: Established evidence identifies DDX5 as an RNA helicase and interaction adaptor that can connect RNA processing with transcription and biosynthetic control. Its network position supports a bridging role in this module. Whether DDX5 actively drives the shared bone-marrow and rectum state, rather than simply reflecting it, remains unresolved.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): CCT3 (0.89), DDX21 (0.86), ACLY (0.84), CCT8 (0.84), MCM6 (0.80), TFRC (0.80); STRING partners: DDX5 (0.935), DDX6 (0.748), HNRNPR (0.962), MATR3 (0.923), PTBP1 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_10659.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is a highly connected nuclear RNA-binding gene positioned between CCT3, CCT8, DDX21, DDX5-related RNA-processing factors, MCM6 and TFRC. It contributes to the globally corrected gene-expression, RNA-binding, biosynthetic and macromolecule-regulation annotations (GO:BP regulation of macromolecule biosynthetic process; q_global = 0.00131), (GO:BP macromolecule biosynthetic process; q_global = 0.00204), (GO:BP gene expression; q_global = 0.00289), (GO:BP regulation of biosynthetic process; q_global = 0.00417), (GO:BP regulation of macromolecule metabolic process; q_global = 0.00631), (GO:BP biosynthetic process; q_global = 0.00679), (GO:BP macromolecule metabolic process; q_global = 0.00827), (GO:BP positive regulation of macromolecule biosynthetic process; q_global = 0.0136), (6 globally significant GO/KEGG terms, q_global 0.0185–0.0252; see the table). STRING supports strong relationships with DDX5, HNRNPR, MATR3 and PTBP1, and hu.MAP places it in a larger heterogeneous nuclear ribonucleoprotein assembly (hu.MAP huMAP3_10625.1), (hu.MAP huMAP3_10659.1). HNRNPK is extensively studied and has established disease associations including Au-Kline syndrome and neurodevelopmental disease.
- **Conclusion**: Established evidence supports HNRNPK as a nuclear RNA-processing and gene-regulatory hub. Its connections to chaperonin, replication-associated and iron-uptake components make it a credible integrator of the module's functional axes. The hypothesis that HNRNPK coordinates the tissue-shared state is plausible but is not directly demonstrated by co-abundance data.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): DDX6 (0.83), DDX5 (0.82), CCT8 (0.81), SHMT2 (0.81); STRING partners: CCT3 (0.766), CCT5 (0.705), CCT7 (0.802), CCT8 (0.776), SNU13 (0.869)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_14306.1
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 is a strategically important connector between the CCT submodule, DDX5 and DDX6, SHMT2 and SNU13. It is included in the globally corrected RNA and telomerase localization terms, ATP-dependent chaperone-related terms, ATP-hydrolysis terms and telomere-maintenance terms (4 globally significant GO/KEGG terms, q_global 3.61e-05–3.61e-05; see the table), (GO:BP regulation of macromolecule biosynthetic process; q_global = 0.00131), (GO:BP macromolecule biosynthetic process; q_global = 0.00204), (GO:BP gene expression; q_global = 0.00289), (GO:CC protein folding chaperone complex; q_global = 0.00419), (GO:BP regulation of macromolecule metabolic process; q_global = 0.00631), (GO:BP biosynthetic process; q_global = 0.00679), (GO:BP macromolecule metabolic process; q_global = 0.00827), (5 globally significant GO/KEGG terms, q_global 0.0136–0.0185; see the table), (GO:BP primary metabolic process; q_global = 0.0192), (GO:BP positive regulation of macromolecule metabolic process; q_global = 0.0211) (GO:BP positive regulation of biosynthetic process; q_global = 0.0252) (GO:BP protein stabilization; q_global = 0.027), (GO:BP regulation of telomere maintenance; q_global = 0.0485). STRING supports connections to the CCT proteins and SNU13, and hu.MAP connects it to a chromatin or DNA-associated complex (hu.MAP huMAP3_14306.1). Its established functions include ATPase and helicase activities, DNA repair, DNA recombination, telomere maintenance and snoRNP assembly, with substantial literature coverage.
- **Conclusion**: Established evidence supports RUVBL2 as a multifunctional ATPase linking RNA, chromatin, DNA and telomere-related processes. It is a plausible molecular bridge explaining why the module combines CCT, RNA-localization and biosynthetic signals. The specific telomerase-related mechanism in bone marrow or rectum remains a hypothesis because the enrichment evidence is indirect.

#### MCM6

- **Related proteins** (co-abundance neighbors): STAT1 (0.85), CCT7 (0.83), TFRC (0.83), CCT8 (0.83), ACLY (0.83), MATR3 (0.82), MTHFD1 (0.82), CAPRIN1 (0.81), HNRNPK (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 6. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: lactose intolerance (0.246); neurodegenerative disease (0.225); obesity disorder (0.166); nervous system disorder (0.141); systemic lupus erythematosus (0.140)
- **Europe PMC papers**: 3766
- **Why important**: MCM6 occupies a connected position linking STAT1, TFRC, CCT7, CCT8, ACLY, MATR3, MTHFD1 and CAPRIN1. HPA identifies it as tissue enhanced in lymphoid tissue and cell-type enhanced in erythroid, megakaryocyte and myeloid progenitors, making it especially relevant to the bone-marrow component and to the possibility of shared proliferative cell states. Its annotations support DNA replication and replication-fork functions, while the module includes globally corrected terms for macromolecule regulation, ATP hydrolysis and primary metabolism (GO:BP regulation of macromolecule metabolic process; q_global = 0.00631), (GO:BP macromolecule metabolic process; q_global = 0.00827), (GO:MF ATP hydrolysis activity; q_global = 0.0173), (GO:BP regulation of primary metabolic process; q_global = 0.0185), (GO:BP primary metabolic process; q_global = 0.0192), (GO:BP regulation of nucleobase-containing compound metabolic process; q_global = 0.0204). hu.MAP places it in chromatin and replication-associated assemblies (hu.MAP huMAP3_10862.1), (hu.MAP huMAP3_14306.1), and it has extensive literature and disease-association coverage.
- **Conclusion**: Established evidence supports MCM6 as a DNA-replication factor and a marker of progenitor or proliferative biology. It may explain part of the hematopoietic composition signal and may connect replication demand to the module's biosynthetic program. Because MCM6 lacks a STRING partner in this module, its precise molecular coupling to the other genes remains uncertain.

#### TFRC

- **Related proteins** (co-abundance neighbors): HYOU1 (0.86), STAT1 (0.85), CCT7 (0.84), MCM6 (0.83), EIF3L (0.83), HNRNPK (0.80); STRING partners: CLTC (0.84)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes, Lysosomes; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_10725.1
- **Function (MyGene.info)**: transferrin receptor. This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: TFRC-related combined immunodeficiency (0.623); type 2 diabetes mellitus (0.518); mucopolysaccharidosis type 2 (0.490); diabetes mellitus (0.471); diabetic retinopathy (0.343)
- **Europe PMC papers**: 14164
- **Why important**: TFRC connects iron uptake and endosomal trafficking to HYOU1, STAT1, MCM6, EIF3L, HNRNPK and CCT7. It is present in many globally corrected biosynthetic and gene-expression terms (GO:BP regulation of macromolecule biosynthetic process; q_global = 0.00131), (GO:BP macromolecule biosynthetic process; q_global = 0.00204), (GO:BP gene expression; q_global = 0.00289), (GO:BP regulation of biosynthetic process; q_global = 0.00417), (GO:BP regulation of macromolecule metabolic process; q_global = 0.00631), (GO:BP biosynthetic process; q_global = 0.00679), (GO:BP macromolecule metabolic process; q_global = 0.00827), (GO:BP positive regulation of macromolecule biosynthetic process; q_global = 0.0136), (GO:BP regulation of primary metabolic process; q_global = 0.0185), (4 globally significant GO/KEGG terms, q_global 0.0192–0.0252; see the table), (GO:BP regulation of protein localization to nucleus; q_global = 0.041). HPA links TFRC to erythrocyte progenitors, macrophages, monocytes and secreted-to-blood protein detection, while STRING supports its relationship with clathrin (STRING TISSUES Blood cancer cell; within-query FDR = 1.11e-06), (STRING TISSUES Liver; within-query FDR = 1.11e-06), (STRING TISSUES Digestive gland; within-query FDR = 7.06e-06), (STRING TISSUES Leukemia cell; within-query FDR = 7.06e-06), (STRING TISSUES Hematopoietic cell; within-query FDR = 0.00072), (STRING Process Regulation of macromolecule biosynthetic process; within-query FDR = 0.0015), (STRING TISSUES Blood; within-query FDR = 0.0043), (STRING TISSUES Embryonic structure; within-query FDR = 0.0055), (STRING Process Regulation of cellular biosynthetic process; within-query FDR = 0.0063). Its established function in cellular iron uptake and erythropoiesis, together with extensive literature and disease associations, makes it informative for interpreting sample composition and metabolic demand.
- **Conclusion**: Established evidence supports TFRC as an iron-uptake and erythropoiesis-associated gene that may mark hematopoietic or metabolically demanding cells. Its presence strengthens the interpretation that the shared module partly reflects cell composition and biosynthetic state rather than a rectum-specific pathway. A direct role for TFRC in coordinating the full module is not established.

## Module 4

**Tissue pair**: bone_marrow and rectum  
**Genes (29)**: AHNAK, ANXA6, CALD1, CAVIN3, CNN1, CFL2, CSRP1, DPYSL2, DPYSL3, EHD1, EHD2, FERMT2, FLNA, FLNC, HSPB1, ILK, ITGA5, MARCKS, PALLD, PARVA, PDLIM4, PDLIM7, RRAS, TUBB6, TGFB1I1, TLN1, TPM1, TPM2, VCL

### Function

The module is most consistently a contractile actin–adhesion and cytoskeletal organization program. The primary evidence is the globally corrected enrichment for myofibril (GO:CC myofibril; q_global = 2.39e-13), contractile muscle fiber (GO:CC contractile muscle fiber; q_global = 3.31e-13), sarcomere (GO:CC sarcomere; q_global = 6.56e-10), focal adhesion (GO:CC focal adhesion; q_global = 2.32e-09), cell-substrate junction (GO:CC cell-substrate junction; q_global = 2.94e-09), actin organization (5 globally significant GO/KEGG terms, q_global 1.66e-08–4.46e-07; see the table), actin binding (GO:MF actin binding; q_global = 5.92e-07), anchoring junction (GO:CC anchoring junction; q_global = 5.14e-08), integrin signaling (KEGG Integrin signaling - Homo sapiens (human); q_global = 0.00165) (GO:BP integrin-mediated signaling pathway; q_global = 0.0305), wound response (GO:BP response to wounding; q_global = 0.000582) (GO:BP wound healing; q_global = 0.00109), and focal adhesion KEGG (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.0444). The muscle-related terms should not be read as proof of skeletal muscle: the gene set also describes smooth-muscle-like and stromal contractile machinery, adhesion to extracellular matrix, force transmission, cell shape, migration, and repair. Platelet aggregation and activation (GO:BP platelet aggregation; q_global = 0.00179) (GO:BP platelet activation; q_global = 0.0112) provide an additional compatible interpretation for a vascular or megakaryocyte-associated contractile state. Thus, the best-supported function is an actomyosin/focal-adhesion module that couples integrin-mediated adhesion to cytoskeletal remodeling and contractility. The co-abundance network is biologically coherent rather than a collection of unrelated annotations: PALLD is a prominent network hub, while the STRING-supported focal-adhesion and sarcomere groupings reinforce the same interpretation (7 supplementary STRING terms; within-query FDR 4.22e-14–3.39e-09).

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It is also not primarily a conventional housekeeping module. HPA instead points toward vascular, intestinal, skeletal-muscle, and heart-muscle tissue associations, with smooth-muscle cells the most frequent enriched cell type and additional stromal, vascular smooth-muscle, myoepithelial, and hepatic-stellate associations. Several genes are detected in both tissues, including FLNA, TGFB1I1, VCL, ILK, PARVA, HSPB1, CSRP1, AHNAK, ANXA6, RRAS, MARCKS, TUBB6, and DPYSL2, whereas other contractile genes show tissue-specific detection. Some members have immune or blood-cell enrichment, including genes associated with neutrophils, monocytes, basophils, megakaryocytes, platelets, or plasmacytoid dendritic cells. Therefore, the shared signal may reflect smooth-muscle, vascular, stromal, epithelial-support, or platelet/megakaryocyte-related cell composition shared between samples, rather than a universal program of every bone-marrow or rectal cell. The HPA pattern does not support interpreting this as simple blood contamination, because many members are associated with structural and contractile non-immune cell types.

**GO/KEGG enrichment**: 62 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC myofibril | 2.39e-13 | AHNAK, CALD1, CFL2, CSRP1, FERMT2, FLNA, FLNC, HSPB1, ILK, PALLD, PARVA, PDLIM4, PDLIM7, TPM1, TPM2, VCL |
| GO:CC contractile muscle fiber | 3.31e-13 | AHNAK, CALD1, CFL2, CSRP1, FERMT2, FLNA, FLNC, HSPB1, ILK, PALLD, PARVA, PDLIM4, PDLIM7, TPM1, TPM2, VCL |
| GO:CC sarcomere | 6.56e-10 | CFL2, CSRP1, FERMT2, FLNA, FLNC, HSPB1, ILK, PALLD, PARVA, PDLIM4, PDLIM7, TPM1, TPM2 |
| GO:CC focal adhesion | 2.32e-09 | AHNAK, ANXA6, CNN1, CSRP1, FERMT2, FLNA, FLNC, HSPB1, ILK, ITGA5, MARCKS, PALLD, PARVA, PDLIM7, RRAS, TGFB1I1, TLN1, VCL |
| GO:CC cell-substrate junction | 2.94e-09 | AHNAK, ANXA6, CNN1, CSRP1, FERMT2, FLNA, FLNC, HSPB1, ILK, ITGA5, MARCKS, PALLD, PARVA, PDLIM7, RRAS, TGFB1I1, TLN1, VCL |
| GO:CC supramolecular polymer | 6.25e-09 | AHNAK, CALD1, CFL2, CSRP1, DPYSL2, DPYSL3, FERMT2, FLNA, FLNC, HSPB1, ILK, PALLD, PARVA, PDLIM4, PDLIM7, TPM1, TPM2, TUBB6, VCL |
| GO:CC supramolecular fiber | 6.25e-09 | AHNAK, CALD1, CFL2, CSRP1, DPYSL2, DPYSL3, FERMT2, FLNA, FLNC, HSPB1, ILK, PALLD, PARVA, PDLIM4, PDLIM7, TPM1, TPM2, TUBB6, VCL |
| GO:BP cytoskeleton organization | 1.66e-08 | CALD1, CAVIN3, CFL2, CNN1, CSRP1, DPYSL2, DPYSL3, EHD2, FERMT2, FLNA, FLNC, ILK, MARCKS, PALLD, PARVA, PDLIM4, PDLIM7, TLN1, TPM1, TPM2, TUBB6 |
| GO:BP actin cytoskeleton organization | 2.01e-08 | CALD1, CAVIN3, CFL2, CNN1, CSRP1, DPYSL3, EHD2, FERMT2, FLNA, FLNC, MARCKS, PALLD, PARVA, PDLIM4, PDLIM7, TLN1, TPM1, TPM2 |
| GO:CC anchoring junction | 5.14e-08 | AHNAK, ANXA6, CNN1, CSRP1, FERMT2, FLNA, FLNC, HSPB1, ILK, ITGA5, MARCKS, PALLD, PARVA, PDLIM4, PDLIM7, RRAS, TGFB1I1, TLN1, VCL |
| GO:BP actin filament-based process | 7.42e-08 | CALD1, CAVIN3, CFL2, CNN1, CSRP1, DPYSL3, EHD2, FERMT2, FLNA, FLNC, MARCKS, PALLD, PARVA, PDLIM4, PDLIM7, TLN1, TPM1, TPM2 |
| GO:CC actin cytoskeleton | 4.46e-07 | AHNAK, CALD1, CFL2, CNN1, DPYSL3, FERMT2, FLNA, ILK, MARCKS, PALLD, PARVA, PDLIM4, PDLIM7, TPM1, TPM2, VCL |
| GO:CC I band | 5.28e-07 | CFL2, CSRP1, FERMT2, FLNA, FLNC, HSPB1, PALLD, PARVA, PDLIM4, PDLIM7 |
| GO:MF actin binding | 5.92e-07 | CALD1, CFL2, CNN1, FERMT2, FLNA, FLNC, MARCKS, PALLD, PARVA, PDLIM4, PDLIM7, TLN1, TPM1, TPM2, VCL |
| GO:CC cytoskeleton | 1.27e-06 | AHNAK, CALD1, CFL2, CNN1, DPYSL2, DPYSL3, FERMT2, FLNA, FLNC, HSPB1, ILK, MARCKS, PALLD, PARVA, PDLIM4, PDLIM7, TGFB1I1, TLN1, TPM1, TPM2, TUBB6, VCL |

### STRING and hu.MAP

STRING contains many high-confidence relationships among the module genes, especially the FLNA–FLNC–VCL–TLN1–ILK–FERMT2–PARVA–ITGA5 focal-adhesion axis, the TPM1–TPM2–CALD1–CNN1 contractile axis, the CFL2–FLNA/FLNC/VCL actin-remodeling links, and the DPYSL2–DPYSL3 pair. These are established molecular relationships and make the module more than a purely statistical co-abundance neighborhood. STRING functional groupings independently support myofibril, focal adhesion, sarcomere, cell junction, supramolecular fiber, cytoskeleton, actin binding, and actin organization (14 supplementary STRING terms; within-query FDR 4.22e-14–3.49e-08); these remain supplementary rather than globally corrected enrichment evidence. hu.MAP adds complexes containing DPYSL2–DPYSL3 (hu.MAP huMAP3_00051.1) (hu.MAP huMAP3_11599.1) (hu.MAP huMAP3_11626.1), TPM1–TPM2 (hu.MAP huMAP3_06153.1), ILK–PARVA (hu.MAP huMAP3_09385.1) (hu.MAP huMAP3_11194.1), and ANXA6–RRAS (hu.MAP huMAP3_12303.1) (hu.MAP huMAP3_12658.1). These complexes are partial because only module members are shown alongside additional complex members. Together, STRING and hu.MAP indicate that many relationships and subassemblies are already known, while the shared tissue-level co-abundance of the complete module is the distinctive observation.

**STRING interactions (score >= 0.7)**: 45 of 406 gene pairs: CALD1–CNN1 (0.867); CALD1–TPM1 (0.869); CALD1–TPM2 (0.747); CALD1–VCL (0.771); CFL2–FLNA (0.888); CFL2–FLNC (0.841); CFL2–VCL (0.83); CNN1–TPM1 (0.792); DPYSL2–DPYSL3 (0.976); DPYSL3–PDLIM4 (0.748); FERMT2–FLNA (0.852); FERMT2–FLNC (0.747); FERMT2–ILK (0.997); FERMT2–PARVA (0.893); FERMT2–TLN1 (0.705); FERMT2–VCL (0.896); FLNA–FLNC (0.907); FLNA–ILK (0.832); FLNA–ITGA5 (0.789); FLNA–TLN1 (0.998); FLNA–VCL (0.998); FLNC–ILK (0.714); FLNC–ITGA5 (0.747); FLNC–TLN1 (0.996); FLNC–TPM2 (0.742); FLNC–VCL (0.994); HSPB1–TGFB1I1 (0.703); ILK–ITGA5 (0.973); ILK–PARVA (0.999); ILK–TGFB1I1 (0.745); ILK–TLN1 (0.996); ILK–VCL (0.995); ITGA5–PARVA (0.735); ITGA5–TLN1 (0.978); ITGA5–VCL (0.78); PARVA–TGFB1I1 (0.724); PARVA–TLN1 (0.939); PARVA–VCL (0.948); PDLIM7–TPM2 (0.857); TGFB1I1–TLN1 (0.764); TGFB1I1–VCL (0.959); TLN1–VCL (0.999); TPM1–TPM2 (0.993); TPM1–VCL (0.957); TPM2–VCL (0.708)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Myofibril (FDR = 4.22e-14, 16 genes); COMPARTMENTS Focal adhesion (FDR = 5.11e-12, 18 genes); Component Focal adhesion (FDR = 4.34e-11, 18 genes); Component Sarcomere (FDR = 4.34e-11, 13 genes); COMPARTMENTS Cell junction (FDR = 2.96e-10, 19 genes); Component Supramolecular fiber (FDR = 5.68e-10, 18 genes); Component Anchoring junction (FDR = 3.39e-09, 19 genes); PMID (2023) Integrated bioinformatics and wet-lab analysis revealed cell adhesion prominent genes CDC42, TAGLN and GSN as prognostic biomarkers in colonic-polyp lesions. (FDR = 4.31e-09, 13 genes); Component Cytoskeleton (FDR = 6.1e-09, 22 genes); Process Actin cytoskeleton organization (FDR = 7.07e-09, 17 genes); Function Actin binding (FDR = 7.91e-09, 16 genes); Function Cytoskeletal protein binding (FDR = 8.14e-09, 19 genes); Process Cytoskeleton organization (FDR = 1.41e-08, 19 genes); Component I band (FDR = 2.11e-08, 10 genes); Component Cell junction (FDR = 3.49e-08, 20 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00051.1 (DPYSL3, DPYSL2; 2/6); huMAP3_06153.1 (TPM2, TPM1; 2/6); huMAP3_11599.1 (DPYSL3, DPYSL2; 2/8); huMAP3_09385.1 (ILK, PARVA; 2/8); huMAP3_11194.1 (ILK, PARVA; 2/10); huMAP3_12303.1 (ANXA6, RRAS; 2/22); huMAP3_12658.1 (ANXA6, RRAS; 2/32); huMAP3_11626.1 (DPYSL3, DPYSL2; 2/42)

### Novelty

The module should not be called a newly discovered molecular complex or a wholly novel pathway. Its central biology is already established by the known actin, integrin, focal-adhesion, sarcomeric, and contractile relationships in STRING and hu.MAP, and by extensive gene-specific literature. Nevertheless, the tissue-pair-level finding may be novel or at least insufficiently characterized: the fact sheet identifies a conserved co-abundance module shared specifically by bone marrow and rectum, and no source in the fact sheet establishes that this exact gene combination, network structure, or cross-tissue conservation has previously been reported. Absence from hu.MAP or STRING cannot prove novelty because those resources catalog physical interactions or complexes rather than every co-expression module. The defensible conclusion is that the molecular components are largely known, whereas the integrated cross-tissue co-abundance architecture is a candidate novel observation requiring replication, cell-type deconvolution, and comparison with published tissue co-expression studies.

**Hypothesis.** Hypothesis: a shared population of contractile vascular, smooth-muscle-like, stromal, epithelial-support, or platelet/megakaryocyte-related cells generates coordinated expression of an integrin–focal-adhesion–actomyosin program in both tissues. In this model, ITGA5, TLN1, FERMT2, ILK, PARVA, FLNA, FLNC, and VCL connect matrix attachment to actin, while TPM1, TPM2, CALD1, CNN1, CFL2, PDLIM proteins, and PALLD tune filament stability, contractility, and force transmission; DPYSL2 and DPYSL3 may connect cytoskeletal remodeling with membrane projections. The same program could support tissue repair and mechanical organization, consistent with wound-related terms (GO:BP response to wounding; q_global = 0.000582) (GO:BP wound healing; q_global = 0.00109). This is a mechanistic hypothesis, not proof of a shared lineage or of active contraction in either tissue. It should be tested by single-cell or spatial localization, cell-type-adjusted co-abundance analysis, protein-level validation, and perturbation of integrin or actin-adhesion components.

### Important genes

#### PALLD

- **Related proteins** (co-abundance neighbors): VCL (0.93), DPYSL3 (0.93), CALD1 (0.93), FLNC (0.91), TGFB1I1 (0.90), FLNA (0.90), EHD2 (0.89), AHNAK (0.89), CFL2 (0.88), PDLIM7 (0.88), CAVIN3 (0.88), FERMT2 (0.86), PDLIM4 (0.85), HSPB1 (0.84), TUBB6 (0.83), TPM2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: palladin, cytoskeletal associated protein. This gene encodes a cytoskeletal protein that is required for organizing the actin cytoskeleton. The protein is a component of actin-containing microfilaments, and it is involved in the control of cell shape, adhesion, and contraction. Polymorphisms in this gene are associated with a susceptibility to pancreatic cancer type 1, and also with a risk for myocardial infarction. Alternative splicing re…
- **Diseases (Open Targets)**: coronary artery disorder (0.444); exocrine pancreatic carcinoma (0.372); coronary atherosclerosis (0.360); Bicuspid aortic valve (0.325); aortic stenosis (0.319)
- **Europe PMC papers**: 1170
- **Why important**: PALLD is the strongest network hub in the supplied module and is connected to structural and signaling components including VCL, FLNC, CALD1, TGFB1I1, FLNA, and EHD2. It appears across a broad set of primary cytoskeletal, junctional, adhesion, and muscle-related terms (19 globally significant GO/KEGG terms, q_global 2.39e-13–7.56e-06; see the table), is localized to actin filaments, and its supplied annotation directly links it to cell shape, adhesion, and contraction. Its disease associations include pancreatic cancer susceptibility, myocardial infarction risk, and coronary disorders, while its literature volume is substantial.
- **Conclusion**: Established: PALLD is a central actin-organizing and adhesion-associated component of this module. Hypothesis: its hub position may help coordinate the shared contractile-adhesion state across the tissues, but hub status alone does not establish causal control.

#### FLNA

- **Related proteins** (co-abundance neighbors): FLNC (0.95), PALLD (0.90), CALD1 (0.85), EHD2 (0.84), CAVIN3 (0.83), HSPB1 (0.81), FERMT2 (0.80); STRING partners: CFL2 (0.888), FERMT2 (0.852), FLNC (0.907), ILK (0.832), ITGA5 (0.789), TLN1 (0.998), VCL (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is a high-connectivity bridge between actin filaments and membrane-associated partners, with supplied STRING relationships to FLNC, TLN1, VCL, ILK, ITGA5, FERMT2, and CFL2. It contributes to nearly every major primary evidence class, including myofibril, focal adhesion, actin binding, integrin signaling, platelet activation, and cell-matrix adhesion (17 globally significant GO/KEGG terms, q_global 2.39e-13–0.0444; see the table). HPA detects it in both tissues, and its established functions include cytoskeletal remodeling, cell shape, migration, integrin interaction, and platelet-related biology. It has extensive disease annotation and a very large literature volume.
- **Conclusion**: Established: FLNA is a plausible structural integrator of the module's membrane–actin and adhesion machinery. Hypothesis: it may help explain why contractile and adhesion signals co-vary across tissues; the data do not show that FLNA drives the module.

#### FLNC

- **Related proteins** (co-abundance neighbors): FLNA (0.95), PALLD (0.91), FERMT2 (0.90), TPM2 (0.85), PDLIM7 (0.85), EHD2 (0.81), CALD1 (0.81); STRING partners: CFL2 (0.841), FERMT2 (0.747), FLNA (0.907), ILK (0.714), ITGA5 (0.747), TLN1 (0.996), TPM2 (0.742), VCL (0.994)
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin C. This gene encodes one of three related filamin genes, specifically gamma filamin. These filamin proteins crosslink actin filaments into orthogonal networks in cortical cytoplasm and participate in the anchoring of membrane proteins for the actin cytoskeleton. Three functional domains exist in filamin: an N-terminal filamentous actin-binding domain, a C-terminal self-association domain, and a membr…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy 26 (0.833); myofibrillar myopathy 5 (0.791); distal myopathy with posterior leg and anterior hand involvement (0.742); dilated cardiomyopathy (0.714); familial restrictive cardiomyopathy (0.660)
- **Europe PMC papers**: 3861
- **Why important**: FLNC links the module's contractile and adhesion arms through strong supplied relationships with FLNA, VCL, TLN1, FERMT2, TPM2, ILK, and CFL2. It is represented in myofibril, sarcomere, focal adhesion, actin organization, muscle-cell development, and sarcomere-organization evidence (11 globally significant GO/KEGG terms, q_global 2.39e-13–0.0416; see the table). HPA associates it with heart and skeletal muscle and with smooth-muscle-related cell populations, and the supplied disease associations include cardiomyopathies and myofibrillar myopathy. Its literature volume is high.
- **Conclusion**: Established: FLNC is a muscle-associated actin crosslinker and membrane-anchor component that fits the module's contractile architecture. Hypothesis: its presence may mark a mechanically specialized structural-cell population shared by the tissues rather than a muscle-cell contamination artifact.

#### ILK

- **Related proteins** (co-abundance neighbors): TGFB1I1 (0.87), PARVA (0.85), RRAS (0.84); STRING partners: FERMT2 (0.997), FLNA (0.832), FLNC (0.714), ITGA5 (0.973), PARVA (0.999), TGFB1I1 (0.745), TLN1 (0.996), VCL (0.995)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: integrin linked kinase. This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastas…
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); familial hypertrophic cardiomyopathy (0.194); Abnormality of the cardiovascular system (0.148); Prolonged QT interval (0.118); neoplasm (0.118)
- **Europe PMC papers**: 8401
- **Why important**: ILK is a key focal-adhesion and integrin-signaling node. It is part of the supplied hu.MAP ILK–PARVA complexes (hu.MAP huMAP3_09385.1) (hu.MAP huMAP3_11194.1) and has strong STRING links to FERMT2, ITGA5, PARVA, TLN1, VCL, FLNA, and TGFB1I1. It appears in primary focal-adhesion, integrin-signaling, cell-matrix adhesion, wound, platelet, and adhesion terms (14 globally significant GO/KEGG terms, q_global 2.32e-09–0.0444; see the table). HPA detects it in both tissues and associates it with focal adhesions, platelets, megakaryocytes, and smooth-muscle cells. The supplied annotation connects it to integrin signal transduction, morphogenesis, epithelial-to-mesenchymal transition, and tumor growth, with a large literature base.
- **Conclusion**: Established: ILK provides a biologically coherent signaling and adhesion bridge within the module. Hypothesis: ILK-dependent matrix sensing could be one mechanism coupling local tissue mechanics to the shared co-abundance program, but co-abundance does not demonstrate ILK enzymatic activity or pathway direction.

#### TPM1

- **Related proteins** (co-abundance neighbors): TGFB1I1 (0.81), PDLIM7 (0.80); STRING partners: CALD1 (0.869), CNN1 (0.792), TPM2 (0.993), VCL (0.957)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_06153.1
- **Function (MyGene.info)**: tropomyosin 1. This gene is a member of the tropomyosin family of highly conserved, widely distributed actin-binding proteins involved in the contractile system of striated and smooth muscles and the cytoskeleton of non-muscle cells. Tropomyosin is composed of two alpha-helical chains arranged as a coiled-coil. It is polymerized end to end along the two grooves of actin filaments and provides stability to the fi…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy (0.798); left ventricular noncompaction (0.760); left ventricular noncompaction 9 (0.664); familial isolated dilated cardiomyopathy (0.639); hypertrophic cardiomyopathy 3 (0.596)
- **Europe PMC papers**: 6278
- **Why important**: TPM1 is a core actin-filament regulator with STRING links to TPM2, CALD1, CNN1, and VCL and a hu.MAP tropomyosin complex containing TPM2 (hu.MAP huMAP3_06153.1). It contributes to the primary myofibril, sarcomere, actin-binding, contractile-bundle, muscle-development, wound, and focal-adhesion evidence (19 globally significant GO/KEGG terms, q_global 2.39e-13–0.0444; see the table). HPA associates it with heart and skeletal muscle and several stromal or myoepithelial cell types; protein detection is reported in rectum. Its supplied disease associations include cardiomyopathies and its literature volume is substantial.
- **Conclusion**: Established: TPM1 supports the interpretation that the module contains a contractile actin-filament program rather than generic cytoskeletal expression. Hypothesis: TPM1-containing filaments may tune force generation or cell mechanics in the shared cell population, but the module does not distinguish among smooth-muscle, stromal, epithelial-support, or platelet-related contexts.

## Module 5

**Tissue pair**: bone_marrow and rectum  
**Genes (23)**: ALDH1A2, ANP32E, ARPC5L, CORO7, DECR1, DNAJB1, EIF3F, GLYR1, HS1BP3, HDHD5, EIF5, LRBA, MYO1E, NOP56, NSUN2, PARP4, PPME1, PRDX3, PTCD3, SRRT, SUMF2, TUBA4A, TBL2

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. The module therefore does not support a single statistically established pathway-level function. Its structure is dominated by ALDH1A2 co-abundance with many otherwise weakly connected genes, alongside smaller signals involving translation initiation, RNA modification and processing, mitochondrial metabolism, oxidative-stress control, cytoskeletal organization, intracellular trafficking and chromatin regulation. ALDH1A2 provides the clearest functional anchor because it catalyzes retinoic-acid synthesis, but the network should be interpreted as a heterogeneous co-abundance program rather than a demonstrated retinoic-acid pathway. The functional interpretation is consequently hypothesis-generating, not pathway-confirmatory.

**Cell composition.** The module is not primarily a plasma or secreted-protein module: only a small minority of genes are annotated as secreted, while most are intracellular. Most genes have low tissue specificity, and protein detection is broadly supported in both bone marrow and rectum. Many genes are cell-type enhanced, with substantial representation among spermatid and spermatocyte populations and additional representation in epithelial, stromal, progenitor and neuronal-related cell types. Blood-cell specificity is generally low, with only isolated enrichment or enhancement involving neutrophils and plasmacytoid dendritic cells. Thus, the shared signal is unlikely to be explained simply by a canonical blood-cell program, although shared cellular composition, broadly expressed intracellular proteins, or sample-level cellular mixtures could contribute. The bone-marrow and rectum overlap should not by itself be interpreted as evidence that the module is tissue-specific.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING evidence is sparse. EIF3F and EIF5 have a high-confidence known interaction, supporting a real translation-initiation relationship within that small part of the module. No other module pairs meet the stated STRING confidence threshold, so the remaining co-abundance edges should not be treated as established physical interactions. hu.MAP provides convergent but limited complex evidence: NSUN2 and DECR1 co-occur in complexes C1, C2 and C3, while the other listed complex members are outside the module. This suggests that these two genes may connect the module to RNA-processing, translation-related, mitochondrial or broader macromolecular complexes, but the fact that only a small subset of each complex is represented limits the claim that the entire module is one complex. Overall, the network is primarily a co-abundance structure with a few externally supported molecular relationships, not a densely validated protein-interaction complex.

**STRING interactions (score >= 0.7)**: 1 of 253 gene pairs: EIF3F–EIF5 (0.973)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11037.1 (NSUN2, DECR1; 2/14); huMAP3_12301.1 (NSUN2, DECR1; 2/26); huMAP3_12727.1 (NSUN2, DECR1; 2/32)

### Novelty

The module may be novel as a tissue-pair co-abundance pattern, but the available evidence is insufficient to call it a newly discovered biological mechanism. Its strongest components are already biologically established: ALDH1A2 has a well-described retinoic-acid biosynthetic function, EIF3F and EIF5 have a known interaction, and NSUN2 with DECR1 recur together in hu.MAP complexes. Conversely, the sparse STRING support, absence of globally significant GO/KEGG enrichment and largely hub-and-spoke topology provide no evidence for a previously unrecognized coherent pathway. Absence from STRING or hu.MAP would not prove novelty, and the observed pattern could reflect coordinated abundance, shared cell states, technical effects or a mixture of unrelated intracellular programs. A claim of novelty would require replication across independent datasets and experiments testing the proposed mechanism.

**Hypothesis.** Hypothesis: in a shared cellular population present in bone marrow and rectum, ALDH1A2-centered variation in intracellular metabolic or differentiation state may covary with retinoic-acid production, mitochondrial lipid handling and oxidative-stress control, while translation, RNA-processing, chromatin, cytoskeletal and trafficking genes track the resulting cell-state demands. The known EIF3F–EIF5 interaction and the repeated NSUN2–DECR1 hu.MAP co-membership may represent smaller functional submodules embedded in this broader co-abundance pattern. This is a mechanistic hypothesis only; the enrichment results do not establish it, and the ALDH1A2-centered correlations do not demonstrate direct physical or regulatory interactions.

### Important genes

#### ALDH1A2

- **Related proteins** (co-abundance neighbors): PARP4 (0.95), GLYR1 (0.92), DNAJB1 (0.89), HDHD5 (0.88), EIF5 (0.87), CORO7 (0.87), TBL2 (0.87), PTCD3 (0.85), SUMF2 (0.85), MYO1E (0.85), LRBA (0.84), SRRT (0.84), PPME1 (0.84), PRDX3 (0.84), NSUN2 (0.83), ANP32E (0.83), NOP56 (0.83), EIF3F (0.83), TUBA4A (0.83), ARPC5L (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 1 family member A2. This protein belongs to the aldehyde dehydrogenase family of proteins. The product of this gene is an enzyme that catalyzes the synthesis of retinoic acid (RA) from retinaldehyde. Retinoic acid, the active derivative of vitamin A (retinol), is a hormonal signaling molecule that functions in developing and adult tissues. The studies of a similar mouse gene suggest that this enzyme and the cytochrom…
- **Diseases (Open Targets)**: diaphragmatic hernia 4, with cardiovascular defects (0.704); osteoarthritis, hand (0.464); osteoarthritis, knee (0.462); Knee pain (0.366); alcohol drinking (0.352)
- **Europe PMC papers**: 3482
- **Why important**: ALDH1A2 is the dominant network hub and has the strongest weighted connectivity in the module. Its established function is synthesis of retinoic acid from retinaldehyde, linking the network to vitamin A metabolism and developmental or differentiation signaling. HPA reports tissue enhancement in endometrium and fallopian tube, cell-type enhancement in stromal, mesothelial, epicardial and hepatic populations, and detection in both relevant tissues. It also has substantial literature coverage and disease associations including developmental and osteoarthritis-related associations.
- **Conclusion**: Established evidence supports ALDH1A2 as the principal topological and biochemical anchor. It is reasonable to hypothesize that variation in retinoic-acid-related cellular state contributes to the module, but the absence of globally significant enrichment and the lack of STRING partners mean that ALDH1A2 cannot be claimed to regulate the other module genes.

#### EIF5

- **Related proteins** (co-abundance neighbors): ALDH1A2 (0.87); STRING partners: EIF3F (0.973)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 5. Eukaryotic translation initiation factor-5 (EIF5) interacts with the 40S initiation complex to promote hydrolysis of bound GTP with concomitant joining of the 60S ribosomal subunit to the 40S initiation complex. The resulting functional 80S ribosomal initiation complex is then active in peptidyl transfer and chain elongations (summary by Si et al., 1996 [PubMed 8663286]).[supplied by OMIM, May 201…
- **Diseases (Open Targets)**: knee fracture (0.219); hair color (0.161); Abnormality of the skeletal system (0.103); liver disorder (0.088); hypertensive disorder (0.079)
- **Europe PMC papers**: 1989
- **Why important**: EIF5 is part of the translation-initiation machinery and is directly connected in STRING to EIF3F, the clearest known physical relationship inside the module. It also covaries with the central ALDH1A2 hub. Its established role in formation and regulation of the cytoplasmic translation-initiation complex makes it a useful indicator of protein-production state. It has substantial literature coverage and several phenotype associations.
- **Conclusion**: Established evidence supports EIF5 as a translation-initiation component and supports its relationship with EIF3F. Its membership in the module most strongly supports a translation-related substructure or shared abundance state; any connection to ALDH1A2-dependent retinoic-acid biology remains hypothetical.

#### EIF3F

- **Related proteins** (co-abundance neighbors): ALDH1A2 (0.83); STRING partners: EIF5 (0.973)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit F. Enables deubiquitinase activity and identical protein binding activity. Contributes to translation initiation factor activity. Involved in IRES-dependent viral translational initiation; protein deubiquitination; and translational initiation. Located in membrane. Part of eukaryotic translation initiation factor 3 complex. Implicated in autosomal recessive non-syndromic intellectual disability. [pro…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal recessive 67 (0.675); hereditary disease (0.413); developmental disability (0.371); neurodegenerative disease (0.370); syndromic intellectual disability (0.370)
- **Europe PMC papers**: 997
- **Why important**: EIF3F is the partner of EIF5 in the high-confidence STRING interaction and is an established subunit-level contributor to translation initiation. It is also associated with translational initiation and IRES-dependent viral translation. Its position adjacent to ALDH1A2 connects the validated translation pair to the central co-abundance pattern. It has substantial literature coverage and disease associations involving developmental disability.
- **Conclusion**: Established evidence supports EIF3F as a translation-initiation factor and supports its interaction with EIF5. The module data do not establish that EIF3F mediates the ALDH1A2-centered pattern, so that broader connection should remain a hypothesis.

#### NSUN2

- **Related proteins** (co-abundance neighbors): ALDH1A2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_11037.1, huMAP3_12301.1, huMAP3_12727.1
- **Function (MyGene.info)**: NOP2/Sun RNA methyltransferase 2. This gene encodes a methyltransferase that catalyzes the methylation of cytosine to 5-methylcytosine (m5C) at position 34 of intron-containing tRNA(Leu)(CAA) precursors. This modification is necessary to stabilize the anticodon-codon pairing and correctly translate the mRNA. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Mar…
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.694); hereditary disease (0.518); Intellectual disability (0.489); phenylketonuria (0.470); neurodegenerative disease (0.462)
- **Europe PMC papers**: 2458
- **Why important**: NSUN2 is a well-characterized RNA methyltransferase involved in tRNA modification, rRNA processing and mRNA processing. It occurs with DECR1 in each of the listed hu.MAP complexes, providing repeated complex-level support that this pair participates in known macromolecular contexts. NSUN2 also has substantial literature coverage and disease associations involving intellectual disability and neurological disease.
- **Conclusion**: Established evidence supports NSUN2 as an RNA-modification and RNA-processing enzyme and supports its repeated co-membership with DECR1 in hu.MAP complexes. The module does not establish that RNA modification is globally enriched or that NSUN2 drives the shared tissue-pair signal.

#### DECR1

- **Related proteins** (co-abundance neighbors): PRDX3 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_11037.1, huMAP3_12301.1, huMAP3_12727.1
- **Function (MyGene.info)**: 2,4-dienoyl-CoA reductase 1. This gene encodes an accessory enzyme which participates in the beta-oxidation and metabolism of unsaturated fatty enoyl-CoA esters. [provided by RefSeq, Jul 2008]
- **Diseases (Open Targets)**: progressive encephalopathy with leukodystrophy due to DECR deficiency (0.411); hypertensive disorder (0.214); insomnia (0.200); neurodegenerative disease (0.198); exostosis (0.089)
- **Europe PMC papers**: 999
- **Why important**: DECR1 is the mitochondrial enzyme that participates in beta-oxidation of unsaturated fatty-acid intermediates. It forms a small co-abundance connection with PRDX3 and appears with NSUN2 in all listed hu.MAP complexes. Its mitochondrial metabolic role complements the module's additional mitochondrial and oxidative-stress annotations, and it has substantial literature coverage including a disease association involving DECR deficiency.
- **Conclusion**: Established evidence supports DECR1 in mitochondrial fatty-acid metabolism and supports its complex-level association with NSUN2. A link between DECR1-mediated lipid metabolism, PRDX3-mediated redox control and ALDH1A2-mediated retinoic-acid synthesis is biologically plausible but remains an untested hypothesis in this module.

#### PRDX3

- **Related proteins** (co-abundance neighbors): DECR1 (0.84), ALDH1A2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Mitochondria; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peroxiredoxin 3. This gene encodes a mitochondrial protein with antioxidant function. The protein is similar to the C22 subunit of Salmonella typhimurium alkylhydroperoxide reductase, and it can rescue bacterial resistance to alkylhydroperoxide in E. coli that lack the C22 subunit. The human and mouse genes are highly conserved, and they map to the regions syntenic between mouse and human chromosomes. Sequence com…
- **Diseases (Open Targets)**: spinocerebellar ataxia, autosomal recessive 32 (0.653); corneal dystrophy, punctiform and polychromatic pre-descemet (0.571); autosomal recessive cerebellar ataxia (0.268); neurodegenerative disease (0.257); hereditary disease (0.191)
- **Europe PMC papers**: 2613
- **Why important**: PRDX3 is a mitochondrial antioxidant protein and is connected to both DECR1 and the ALDH1A2 hub. Its annotations include oxidative-stress response, mitochondrial organization and myeloid-cell differentiation. HPA reports mitochondrial localization and cell-type enhancement in several metabolically active or progenitor-related populations. It also has substantial literature coverage and established disease associations involving neurological and mitochondrial dysfunction.
- **Conclusion**: Established evidence supports PRDX3 as a mitochondrial redox-control protein and supports its local network connection to DECR1 and ALDH1A2. The idea that it buffers oxidative consequences of coordinated retinoic-acid and lipid metabolism is a hypothesis rather than a conclusion from the co-abundance data.

## Module 6

**Tissue pair**: bone_marrow and rectum  
**Genes (6)**: ANXA4, CSTF3, GARS1, MARCHF5, MCM2, WDR11

### Function

No GO or KEGG term passed global correction. No STRING functional-enrichment term was reported. The strongest defensible interpretation therefore comes from the gene identities and network topology rather than from formal pathway enrichment. MARCHF5 is the central co-abundance hub, while the peripheral genes represent mitochondrial quality control, DNA replication, membrane and epithelial biology, translation, RNA processing, and ciliary or trafficking-related functions. Taken together, the module is best interpreted as a heterogeneous cellular-state module, potentially reflecting coordinated biosynthetic, organelle, and proliferative activity rather than a single established pathway. The absence of globally significant enrichment does not invalidate the module.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only one member is annotated as secreted, and the remainder are intracellular or membrane-associated. All members have low immune-cell specificity, with no enriched blood-cell category reported, so the module is not strongly supported as a blood-cell-specific program. Four genes have low tissue specificity and two are tissue-enhanced. HPA evidence points to a mixed composition involving bone marrow or lymphoid biology, epithelial or ductal cell types, trophoblast-related cell types, and broadly expressed cellular machinery. Protein detection is generally present in both tissues where data are available. Thus, shared cell states or broadly present cellular processes are more plausible explanations than a plasma-protein module or a narrowly defined immune-cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no STRING functional-enrichment term was reported. No hu.MAP complex contained multiple module members. Consequently, the co-abundance edges are not corroborated by the supplied physical-interaction or complex resources. This suggests that the module may capture coordinated expression, shared cell composition, common regulation, or indirect biological coupling rather than a known physical complex. The lack of STRING or hu.MAP support also means that MARCHF5 should be treated as a network hub in this dataset, not automatically as a validated molecular interaction hub for all of these proteins.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a previously unreported co-abundance grouping, because the supplied resources do not identify a matching STRING interaction network or hu.MAP complex. However, it cannot be called a new biological mechanism solely from the absence of database support. Several component functions are already well established, including mitochondrial ubiquitin regulation, replication initiation, annexin-mediated membrane biology, translation, RNA three-prime-end processing, and ciliary or trafficking biology. The defensible novelty claim is therefore limited: the tissue-pair co-abundance pattern and its possible coordination may be novel, whereas the individual gene functions are not shown to be novel.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program present in subsets of bone marrow and rectum samples, in which mitochondrial quality control and organelle remodeling are coordinated with replication competence, membrane or epithelial-state regulation, translation, and mRNA maturation. MARCHF5 may mark or contribute to the organelle-state axis, while MCM2 may report proliferative progenitor activity and ANXA4 may report membrane or epithelial features. GARS1 and CSTF3 may represent the biosynthetic and RNA-processing capacity required by that state. This model is provisional: the absence of globally significant GO or KEGG enrichment, STRING interactions, and hu.MAP complexes means that direct regulation and physical coupling remain untested.

### Important genes

#### MARCHF5

- **Related proteins** (co-abundance neighbors): MCM2 (0.88), GARS1 (0.84), ANXA4 (0.84), WDR11 (0.83), CSTF3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: membrane associated ring-CH-type finger 5. MARCH5 is a ubiquitin ligase of the mitochondrial outer membrane that plays a role in the control of mitochondrial morphology by regulating mitofusin-2 (MFN2; MIM 608507) and DRP1 (DNM1L; MIM 603850) (Nakamura et al., 2006 [PubMed 16936636]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: diabetes mellitus (0.299); type 2 diabetes mellitus (0.285); metabolic syndrome (0.272); type 1 diabetes mellitus (0.257); glaucoma (0.171)
- **Europe PMC papers**: 155
- **Why important**: MARCHF5 is the network hub, connected to every other module member with relatively strong co-abundance links. Its established function as a mitochondrial outer-membrane ubiquitin ligase connects the module to mitochondrial morphology, mitofusin and DRP1 regulation, and ubiquitin-dependent control of cellular processes. It has a substantial literature base and disease associations including diabetes and metabolic syndrome.
- **Conclusion**: Established evidence supports MARCHF5 as the structural anchor of the module and as a regulator of mitochondrial dynamics. The co-abundance pattern does not establish that MARCHF5 directly controls the other module genes; that connection remains a hypothesis.

#### MCM2

- **Related proteins** (co-abundance neighbors): MARCHF5 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is tissue-enhanced in bone marrow and lymphoid tissue, is detected in both sampled tissues, and is associated with erythrocyte and megakaryocyte progenitor cell types. Its established role in replication initiation and the replication machinery makes it informative for a proliferative or progenitor-cell component. It also has the largest literature volume among the module genes.
- **Conclusion**: Established evidence supports MCM2 as a marker of DNA-replication competence and proliferative progenitor biology. Its peripheral position in the co-abundance graph argues against treating it as the module's sole driver, and the data do not prove that the entire module represents proliferation.

#### ANXA4

- **Related proteins** (co-abundance neighbors): MARCHF5 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A4. Annexin IV (ANX4) belongs to the annexin family of calcium-dependent phospholipid binding proteins. Although their functions are still not clearly defined, several members of the annexin family have been implicated in membrane-related events along exocytotic and endocytotic pathways. ANX4 has 45 to 59% identity with other members of its family and shares a similar size and exon-intron organization…
- **Diseases (Open Targets)**: atrial fibrillation (0.445); Abnormality of the skeletal system (0.385); dentures (0.301); neurodegenerative disease (0.268); placental abruption (0.235)
- **Europe PMC papers**: 1395
- **Why important**: ANXA4 is connected to the MARCHF5 hub and is tissue-enhanced in gallbladder and pancreas, with enrichment in cholangiocytes, pancreatic duct cells, and syncytiotrophoblasts. Its established annexin function involves calcium-dependent phospholipid binding and membrane-related events, while the supplied annotations also connect it to epithelial differentiation and inflammatory signaling. It is among the more extensively studied genes in the module.
- **Conclusion**: Established evidence supports ANXA4 as a membrane-associated and epithelial-associated component. Its presence may reflect epithelial or membrane-state biology shared across samples, but the module data do not establish a specific ANXA4-mediated pathway.

#### GARS1

- **Related proteins** (co-abundance neighbors): MARCHF5 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycyl-tRNA synthetase 1. This gene encodes glycyl-tRNA synthetase, one of the aminoacyl-tRNA synthetases that charge tRNAs with their cognate amino acids. The encoded enzyme is an (alpha)2 dimer which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Two transcript variants encoding different isoforms ha…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease type 2D (0.790); neuronopathy, distal hereditary motor, type 5A (0.729); neuronopathy, distal hereditary motor, type 5 (0.698); spinal muscular atrophy, infantile, James type (0.649); Charcot-Marie-Tooth disease type 2 (0.565)
- **Europe PMC papers**: 302
- **Why important**: GARS1 is linked to the MARCHF5 hub, is detected in both tissues, and has a broadly expressed cellular localization. Its established function in glycyl-tRNA charging supports a core protein-translation and amino-acid utilization interpretation. It also has disease associations involving inherited motor-neuron disorders and is known as an autoantibody target in polymyositis or dermatomyositis.
- **Conclusion**: Established evidence supports GARS1 as a translation-related housekeeping component rather than a tissue-specific effector. Its co-abundance with MARCHF5 may reflect shared cellular activity or mitochondrial and biosynthetic state, but a direct mechanistic connection is not demonstrated.

#### CSTF3

- **Related proteins** (co-abundance neighbors): MARCHF5 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cleavage stimulation factor subunit 3. The protein encoded by this gene is one of three (including CSTF1 and CSTF2) cleavage stimulation factors that combine to form the cleavage stimulation factor complex (CSTF). This complex is involved in the polyadenylation and 3' end cleavage of pre-mRNAs. The encoded protein functions as a homodimer and interacts directly with both CSTF1 and CSTF2 in the CSTF complex. Alternative splicing results…
- **Diseases (Open Targets)**: dengue disease (0.370); Hydrocephalus (0.192); retinitis pigmentosa (0.085); early-onset non-syndromic cataract (0.084); early-onset zonular cataract (0.080)
- **Europe PMC papers**: 477
- **Why important**: CSTF3 is linked to the MARCHF5 hub and encodes a component of the cleavage stimulation factor complex involved in pre-mRNA cleavage and polyadenylation. This gives the module an established RNA-processing dimension. Its detection in both tissues and low tissue specificity are consistent with a broadly used cellular function.
- **Conclusion**: Established evidence supports CSTF3 as a general mRNA three-prime-end-processing component. Its inclusion is compatible with coordinated transcriptional and post-transcriptional activity, but the network does not establish a specialized CSTF3-centered program.

## Module 7

**Tissue pair**: bone_marrow and rectum  
**Genes (41)**: AP3B1, HSD17B4, DHX9, ADAR, EIF3C, FASN, GTF2I, GMPS, HSPH1, EIF4G1, ITPR3, NOP2, DDOST, ALDH18A1, PSMC2, GART, CAD, RSL1D1, PDCD11, SEC24C, SF3A1, SF3B3, SRP68, SRP72, DARS1, EPRS1, FARSB, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1, TNPO1, TRAP1, TRIM25, SNRNP200, EFTUD2, UGGT1, VPS35

### Function

The strongest interpretation is a conserved core of translational capacity and RNA metabolism. Primary evidence comes from the globally corrected aminoacyl-tRNA synthetase multienzyme complex term (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 2.44e-07), the globally corrected ligase and aminoacyl-tRNA ligase activities (GO:MF ligase activity; q_global = 2.53e-06)(GO:MF aminoacyl-tRNA ligase activity; q_global = 3.53e-06), the tRNA aminoacylation and amino-acid activation processes (GO:BP tRNA aminoacylation for protein translation; q_global = 3.53e-06)(GO:BP amino acid activation; q_global = 3.53e-06)(GO:BP tRNA aminoacylation; q_global = 3.53e-06), and the aminoacyl-tRNA biosynthesis pathway (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 3.53e-06). The module also contains a broader RNA-processing and translation layer, supported by RNA catalytic activity (GO:MF catalytic activity, acting on a tRNA; q_global = 1.34e-05)(GO:MF catalytic activity, acting on RNA; q_global = 5.44e-05), RNA binding (GO:MF RNA binding; q_global = 0.00033), translation and protein biosynthesis (GO:BP translation; q_global = 0.00376)(GO:BP protein biosynthetic process; q_global = 0.00376), and protein-RNA complex assembly and organization (GO:BP protein-RNA complex assembly; q_global = 0.031)(GO:BP protein-RNA complex organization; q_global = 0.0406). A connected nucleotide-supply component is represented by CAD, GART, and GMPS, while ATP and nucleotide binding terms (GO:MF ATP binding; q_global = 0.000208)(GO:MF adenyl ribonucleotide binding; q_global = 0.00022)(GO:MF adenyl nucleotide binding; q_global = 0.00133)(GO:MF purine ribonucleoside triphosphate binding; q_global = 0.00168)(GO:MF purine ribonucleotide binding; q_global = 0.00175)(GO:MF ribonucleotide binding; q_global = 0.00191)(GO:MF purine nucleotide binding; q_global = 0.00766)(GO:MF carbohydrate derivative binding; q_global = 0.00998)(GO:MF nucleotide binding; q_global = 0.0247)(GO:MF anion binding; q_global = 0.0287)(GO:MF nucleoside phosphate binding; q_global = 0.0311) are compatible with the enzymatic demands of translation and biosynthesis. Osteoblast differentiation and ossification terms (GO:BP osteoblast differentiation; q_global = 0.000895)(GO:BP ossification; q_global = 0.00774) are globally supported, but they involve a smaller functional branch and should not override the dominant interpretation as a translation and RNA-processing module.

**Cell composition.** This is not a plasma-protein or secreted-protein module. The genes are predominantly intracellular enzymes, RNA-binding proteins, translation factors, spliceosomal proteins, nucleolar proteins, and chaperones. HPA indicates broadly distributed expression for most genes, with low tissue specificity across the module and protein detection in both tissues for nearly all genes. Blood-cell specificity is generally low, with only limited immune-cell enhancement, so the shared signal is not strongly attributable to a blood-cell program. The presence of cell-type-enhanced genes in several unrelated cell types, including neutrophils, erythrocyte progenitors, epithelial cells, germ-cell populations, and secretory cells, is more consistent with a broadly required biosynthetic program than with one narrowly defined lineage. The small secreted-protein component does not explain the module. The shared bone-marrow and rectum pattern could nevertheless reflect common proliferative or metabolically active cells, rather than a tissue-specific function.

**GO/KEGG enrichment**: 33 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 2.44e-07 | DARS1, EPRS1, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1 |
| GO:MF ligase activity | 2.53e-06 | CAD, DARS1, EPRS1, FARSB, GART, GMPS, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, TRIM25, VARS1 |
| GO:MF aminoacyl-tRNA ligase activity | 3.53e-06 | DARS1, EPRS1, FARSB, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1 |
| GO:BP tRNA aminoacylation for protein translation | 3.53e-06 | DARS1, EPRS1, FARSB, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 3.53e-06 | DARS1, EPRS1, FARSB, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1 |
| GO:BP amino acid activation | 3.53e-06 | DARS1, EPRS1, FARSB, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1 |
| GO:BP tRNA aminoacylation | 3.53e-06 | DARS1, EPRS1, FARSB, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 3.53e-06 | DARS1, EPRS1, FARSB, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1 |
| GO:MF catalytic activity, acting on a tRNA | 1.34e-05 | ADAR, DARS1, EPRS1, FARSB, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1 |
| GO:MF catalytic activity, acting on RNA | 5.44e-05 | ADAR, DARS1, DHX9, EPRS1, FARSB, IARS1, KARS1, LARS1, MARS1, NOP2, QARS1, RARS1, SNRNP200, VARS1 |
| GO:MF ATP binding | 0.000208 | ALDH18A1, CAD, DARS1, DHX9, EIF4G1, EPRS1, FARSB, GART, GMPS, HSPH1, IARS1, ITPR3, KARS1, LARS1, MARS1, PSMC2, QARS1, RARS1, SNRNP200, TRAP1, VARS1 |
| GO:MF adenyl ribonucleotide binding | 0.00022 | ALDH18A1, CAD, DARS1, DHX9, EIF4G1, EPRS1, FARSB, GART, GMPS, HSPH1, IARS1, ITPR3, KARS1, LARS1, MARS1, PSMC2, QARS1, RARS1, SNRNP200, TRAP1, VARS1 |
| GO:MF RNA binding | 0.00033 | ADAR, ALDH18A1, DARS1, DHX9, EFTUD2, EIF3C, EIF4G1, EPRS1, FARSB, FASN, IARS1, KARS1, MARS1, NOP2, PDCD11, RARS1, RSL1D1, SF3A1, SF3B3, SNRNP200, SRP68, SRP72, TNPO1, TRAP1, TRIM25 |
| GO:BP tRNA metabolic process | 0.000521 | DARS1, EPRS1, FARSB, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1 |
| GO:BP amino acid metabolic process | 0.000738 | ALDH18A1, CAD, DARS1, EPRS1, FARSB, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1 |

### STRING and hu.MAP

STRING supports the same interpretation as the primary enrichment, but its enrichment results are supplementary (15 supplementary STRING terms; within-query FDR 1.22e-07–3.52e-05). The aminoacyl-tRNA synthetases form a tightly connected STRING neighborhood, including DARS1, EPRS1, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, and VARS1. The strongest established complex evidence is provided by hu.MAP complexes (hu.MAP huMAP3_02637.1)(hu.MAP huMAP3_13688.1), which contain the multisynthetase-core members EPRS1, DARS1, IARS1, QARS1, RARS1, MARS1, KARS1, and LARS1. The spliceosome-related genes EFTUD2, SF3A1, SF3B3, and SNRNP200 are connected by both STRING and several hu.MAP complexes (hu.MAP huMAP3_08980.1)(hu.MAP huMAP3_00960.1)(hu.MAP huMAP3_07622.1)(hu.MAP huMAP3_08501.1)(hu.MAP huMAP3_09504.1)(hu.MAP huMAP3_04549.1)(hu.MAP huMAP3_09945.1)(hu.MAP huMAP3_06511.1). EIF3C and EIF4G1 connect the module to translation-initiation complexes (hu.MAP huMAP3_13175.1)(hu.MAP huMAP3_11246.1), while GART and FASN and CAD and FASN appear together in hu.MAP complexes (hu.MAP huMAP3_01662.1) (hu.MAP huMAP3_03291.1) (hu.MAP huMAP3_00676.1) (hu.MAP huMAP3_10103.1). Thus, a substantial part of the network recapitulates known physical or functional relationships. The co-abundance graph is therefore biologically coherent, but its edges should not all be interpreted as newly discovered physical interactions.

**STRING interactions (score >= 0.7)**: 75 of 820 gene pairs: ADAR–DHX9 (0.922); ALDH18A1–CAD (0.796); ALDH18A1–EPRS1 (0.723); ALDH18A1–GMPS (0.909); CAD–GART (0.877); CAD–GMPS (0.749); DARS1–EPRS1 (0.999); DARS1–IARS1 (0.996); DARS1–KARS1 (0.996); DARS1–LARS1 (0.996); DARS1–MARS1 (0.999); DARS1–QARS1 (0.999); DARS1–RARS1 (0.996); DHX9–SF3B3 (0.73); DHX9–SNRNP200 (0.784); EFTUD2–EPRS1 (0.744); EFTUD2–KARS1 (0.704); EFTUD2–PDCD11 (0.828); EFTUD2–SF3A1 (0.999); EFTUD2–SF3B3 (0.999); EFTUD2–SNRNP200 (0.999); EIF3C–EIF4G1 (0.99); EIF3C–EPRS1 (0.755); EIF4G1–VPS35 (0.899); EPRS1–FARSB (0.925); EPRS1–GART (0.752); EPRS1–GMPS (0.912); EPRS1–IARS1 (0.999); EPRS1–KARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–MARS1 (0.999); EPRS1–PDCD11 (0.75); EPRS1–QARS1 (0.999); EPRS1–RARS1 (0.999); EPRS1–VARS1 (0.97); FARSB–GMPS (0.727); FARSB–IARS1 (0.914); FARSB–KARS1 (0.813); FARSB–LARS1 (0.814); FARSB–MARS1 (0.705); FARSB–RARS1 (0.706); FARSB–VARS1 (0.776); GART–GMPS (0.937); GMPS–KARS1 (0.835); GMPS–RARS1 (0.872); GMPS–VARS1 (0.797); IARS1–KARS1 (0.999); IARS1–LARS1 (0.999); IARS1–MARS1 (0.999); IARS1–QARS1 (0.999); IARS1–RARS1 (0.999); IARS1–VARS1 (0.9); KARS1–LARS1 (0.999); KARS1–MARS1 (0.999); KARS1–QARS1 (0.999); KARS1–RARS1 (0.999); KARS1–VARS1 (0.978); LARS1–MARS1 (0.999); LARS1–QARS1 (0.999); LARS1–RARS1 (0.999); LARS1–VARS1 (0.968); MARS1–QARS1 (0.999); MARS1–RARS1 (0.999); MARS1–VARS1 (0.902); NOP2–PDCD11 (0.927); NOP2–RSL1D1 (0.982); PDCD11–RSL1D1 (0.978); PDCD11–VARS1 (0.805); QARS1–RARS1 (0.999); QARS1–VARS1 (0.91); RARS1–VARS1 (0.905); SF3A1–SF3B3 (0.999); SF3A1–SNRNP200 (0.999); SF3B3–SNRNP200 (0.999); SRP68–SRP72 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Ligase (FDR = 1.22e-07, 14 genes); RCTM Cytosolic tRNA aminoacylation (FDR = 5.47e-07, 10 genes); RCTM Translation (FDR = 5.47e-07, 15 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 8.74e-07, 10 genes); Keyword Protein biosynthesis (FDR = 8.74e-07, 12 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 1.09e-06, 10 genes); Function Ligase activity (FDR = 1.66e-06, 14 genes); Component aminoacyl-tRNA synthetase multienzyme complex (FDR = 1.98e-06, 8 genes); Function aminoacyl-tRNA ligase activity (FDR = 2.83e-06, 10 genes); COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex (FDR = 3.48e-06, 8 genes); NetworkNeighborAL tRNA Aminoacylation, and glutamyl-tRNA(Gln) amidotransferase complex (FDR = 1.14e-05, 10 genes); Function Catalytic activity, acting on RNA (FDR = 2.35e-05, 13 genes); Process tRNA aminoacylation for protein translation (FDR = 2.7e-05, 10 genes); Process RNA metabolic process (FDR = 2.89e-05, 21 genes); Process Cellular amino acid metabolic process (FDR = 3.52e-05, 14 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, DARS1, IARS1, QARS1, RARS1, MARS1, KARS1, LARS1; 8/14); huMAP3_13688.1 (EPRS1, DARS1, IARS1, QARS1, RARS1, MARS1, KARS1, LARS1; 8/14); huMAP3_08980.1 (SNRNP200, EFTUD2, SF3B3, SF3A1; 4/97); huMAP3_01662.1 (GART, FASN; 2/3); huMAP3_03291.1 (GART, FASN; 2/3); huMAP3_00676.1 (GART, FASN; 2/4); huMAP3_10103.1 (CAD, FASN; 2/4); huMAP3_00960.1 (SNRNP200, EFTUD2; 2/8); huMAP3_07622.1 (SNRNP200, EFTUD2; 2/9); huMAP3_13175.1 (EIF4G1, EIF3C; 2/20); huMAP3_11246.1 (EIF4G1, EIF3C; 2/24); huMAP3_08501.1 (SNRNP200, EFTUD2; 2/47); huMAP3_09504.1 (SNRNP200, EFTUD2; 2/51); huMAP3_04549.1 (SF3B3, SF3A1; 2/52); huMAP3_14442.1 (GMPS, TRAP1; 2/57); huMAP3_09945.1 (SNRNP200, EFTUD2; 2/61); huMAP3_06511.1 (SF3B3, SF3A1; 2/79); huMAP3_13468.1 (ALDH18A1, TRAP1; 2/99)

### Novelty

The biochemical functions represented here are not new: aminoacyl-tRNA synthetase complexes, spliceosomal assemblies, translation-initiation machinery, nucleotide biosynthesis, and RNA processing are all established biology. The module also contains extensive STRING and hu.MAP support, which argues against claiming a novel molecular complex. What may be novel is the reproducible co-abundance configuration shared by bone marrow and rectum, especially the way the multisynthetase, RNA-processing, translation, nucleotide, and proteostasis components are coupled across these tissues. However, the fact sheet alone does not establish that this tissue-pair module has never been reported. Absence of a relationship from STRING or hu.MAP would not prove novelty, and the presence of known relationships makes the appropriate conclusion a potentially novel systems-level association rather than a new pathway or complex. Independent replication, comparison with published tissue co-expression modules, and perturbation or activity measurements would be needed to claim a new finding.

**Hypothesis.** Hypothesis: the shared module represents a cell-state program that coordinates translational fidelity and protein production with RNA maturation, nucleotide supply, and stress handling. The multisynthetase core may provide the central translational backbone; CAD, GART, and GMPS may support nucleotide availability; EFTUD2, SF3A1, SF3B3, SNRNP200, DHX9, and ADAR may coordinate RNA processing; EIF3C and EIF4G1 may couple this to translation initiation; and HSPH1 and TRAP1 may buffer proteotoxic or metabolic stress. In bone marrow this could support biosynthetically active hematopoietic cells, while in rectum it could reflect comparably active epithelial or stromal populations. The osteoblast-related annotations suggest a possible differentiation-associated component, but they do not by themselves demonstrate that the shared module drives osteogenesis.

### Important genes

#### EPRS1

- **Related proteins** (co-abundance neighbors): DHX9 (0.89), DARS1 (0.88), ADAR (0.88), PSMC2 (0.87), EFTUD2 (0.87), RARS1 (0.87), EIF4G1 (0.87), HSPH1 (0.87), LARS1 (0.86), IARS1 (0.85), FARSB (0.85), SRP68 (0.84), HSD17B4 (0.84), TRIM25 (0.84), CAD (0.84), SF3A1 (0.83), TRAP1 (0.82), MARS1 (0.81), NOP2 (0.81), ALDH18A1 (0.81), SF3B3 (0.81), ITPR3 (0.80); STRING partners: ALDH18A1 (0.723), DARS1 (0.999), EFTUD2 (0.744), EIF3C (0.755), FARSB (0.925), GART (0.752), GMPS (0.912), IARS1 (0.999), KARS1 (0.999), LARS1 (0.999), MARS1 (0.999), PDCD11 (0.75), QARS1 (0.999), RARS1 (0.999), VARS1 (0.97)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is a high-connectivity module gene and a central member of the multisynthetase complex. It appears in the primary aminoacylation, translation, RNA-binding, and protein-biosynthesis evidence (4 globally significant GO/KEGG terms, q_global 2.44e-07–3.53e-06; see the table)(8 globally significant GO/KEGG terms, q_global 3.53e-06–0.000738; see the table)(GO:BP translation; q_global = 0.00376) (GO:BP protein biosynthetic process; q_global = 0.00376) (GO:MF nucleic acid binding; q_global = 0.00463)(4 globally significant GO/KEGG terms, q_global 0.0099–0.0287; see the table)(GO:MF nucleoside phosphate binding; q_global = 0.0311), in the STRING aminoacylation and translation evidence (15 supplementary STRING terms; within-query FDR 1.22e-07–3.52e-05), and in hu.MAP multisynthetase complexes (hu.MAP huMAP3_02637.1)(hu.MAP huMAP3_13688.1). Its annotation establishes direct glutamyl- and prolyl-tRNA charging functions, while its disease associations include hypomyelinating leukodystrophy and developmental disorders. Its literature volume is substantial enough to make it a well-characterized anchor rather than an obscure candidate.
- **Conclusion**: Established conclusion: EPRS1 is a core translational and multisynthetase component and is one of the strongest molecular anchors of the module. Hypothesis: variation in EPRS1 abundance may help couple translational capacity to the shared biosynthetic state of bone marrow and rectum.

#### DARS1

- **Related proteins** (co-abundance neighbors): EPRS1 (0.88), PSMC2 (0.87); STRING partners: EPRS1 (0.999), IARS1 (0.996), KARS1 (0.996), LARS1 (0.996), MARS1 (0.999), QARS1 (0.999), RARS1 (0.996)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 1. This gene encodes a member of a multienzyme complex that functions in mediating the attachment of amino acids to their cognate tRNAs. The encoded protein ligates L-aspartate to tRNA(Asp). Mutations in this gene have been found in patients showing hypomyelination with brainstem and spinal cord involvement and leg spasticity. Alternative splicing results in multiple transcript variants. [provided by…
- **Diseases (Open Targets)**: hypomyelination with brain stem and spinal cord involvement and leg spasticity (0.773); atrial fibrillation (0.268); Abnormal brain morphology (0.266); tooth hard tissue disease (0.226); Pancreatic pseudocyst (0.225)
- **Europe PMC papers**: 238
- **Why important**: DARS1 is a member of the densely connected multisynthetase neighborhood and hu.MAP complexes (hu.MAP huMAP3_02637.1)(hu.MAP huMAP3_13688.1), with repeated support across the primary tRNA-aminoacylation and translation terms (10 globally significant GO/KEGG terms, q_global 2.44e-07–5.44e-05; see the table)(GO:BP tRNA metabolic process; q_global = 0.000521)(GO:BP translation; q_global = 0.00376)(GO:BP protein biosynthetic process; q_global = 0.00376). It encodes aspartyl-tRNA synthetase and is linked to hypomyelination with brainstem and spinal cord involvement, as well as other neurological and skeletal associations. Its direct biochemical role and extensive STRING connections make it a representative of the module's central translational machinery even though its co-abundance degree is not among the highest.
- **Conclusion**: Established conclusion: DARS1 provides direct evidence that the module contains canonical tRNA charging machinery rather than only generic RNA-binding proteins. Hypothesis: coordinated DARS1 abundance with the other synthetases may help preserve translational fidelity in the shared cellular state.

#### DHX9

- **Related proteins** (co-abundance neighbors): CAD (0.93), HSPH1 (0.91), EFTUD2 (0.91), RARS1 (0.89), EPRS1 (0.89), VPS35 (0.88), IARS1 (0.88), EIF3C (0.88), SF3A1 (0.88), SNRNP200 (0.86), SF3B3 (0.86), ALDH18A1 (0.85), KARS1 (0.83), VARS1 (0.83), ADAR (0.82), RSL1D1 (0.81), QARS1 (0.81), LARS1 (0.81), MARS1 (0.80), SRP72 (0.80), NOP2 (0.80), EIF4G1 (0.80); STRING partners: ADAR (0.922), SF3B3 (0.73), SNRNP200 (0.784)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is among the most connected genes in the co-abundance graph and links the synthetase-rich region to RNA processing, translation, stress, and spliceosomal neighborhoods. It is represented in numerous globally corrected RNA, nucleotide-binding, translation, protein-RNA assembly, and osteoblast-related terms (4 globally significant GO/KEGG terms, q_global 5.44e-05–0.00033; see the table)(18 globally significant GO/KEGG terms, q_global 0.000895–0.0406; see the table), and it has a known STRING relationship with ADAR (STRING Function Catalytic activity, acting on RNA; within-query FDR = 2.35e-05)(STRING Process RNA metabolic process; within-query FDR = 2.89e-05). Its established function is ATP-dependent unwinding of RNA and DNA-RNA duplexes, with roles in RNA processing, transcriptional regulation, and interferon-related responses. Its disease literature is extensive and includes developmental and neurodegenerative associations.
- **Conclusion**: Established conclusion: DHX9 is a plausible network bridge between RNA remodeling and the module's translation-centered machinery. Hypothesis: DHX9 may coordinate RNA structural remodeling with changes in translation or spliceosome activity across the two tissues.

#### CAD

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.93), DHX9 (0.93), HSPH1 (0.90), EFTUD2 (0.90), SF3B3 (0.89), IARS1 (0.89), RARS1 (0.87), VPS35 (0.86), SRP72 (0.85), QARS1 (0.84), EPRS1 (0.84), EIF3C (0.84), NOP2 (0.83), SF3A1 (0.83), TNPO1 (0.82), EIF4G1 (0.82), ADAR (0.82), AP3B1 (0.82), PDCD11 (0.82), MARS1 (0.81); STRING partners: ALDH18A1 (0.796), GART (0.877), GMPS (0.749)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_10103.1
- **Function (MyGene.info)**: carbamoyl-phosphate synthetase 2, aspartate transcarbamylase, and dihydroorotase. The de novo synthesis of pyrimidine nucleotides is required for mammalian cells to proliferate. This gene encodes a trifunctional protein which is associated with the enzymatic activities of the first 3 enzymes in the 6-step pathway of pyrimidine biosynthesis: carbamoylphosphate synthetase (CPS II), aspartate transcarbamoylase, and dihydroorotase. This protein is regulated by the mitogen-activated…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 50 (0.660); congenital disorder of glycosylation type I (0.595); infantile epileptic-dyskinetic encephalopathy (0.499); type 2 diabetes mellitus (0.286); urolithiasis (0.283)
- **Europe PMC papers**: 60667
- **Why important**: CAD is a high-connectivity metabolic enzyme that links the module to nucleotide production and to the RNA-processing and translation neighborhoods. It is present in globally corrected ligase, ATP-binding, nucleotide-binding, amino-acid-metabolism, and broader biosynthetic terms (GO:MF ligase activity; q_global = 2.53e-06)(GO:MF ATP binding; q_global = 0.000208)(GO:MF adenyl ribonucleotide binding; q_global = 0.00022)(GO:BP amino acid metabolic process; q_global = 0.000738)(5 globally significant GO/KEGG terms, q_global 0.00133–0.00191; see the table)(GO:MF purine nucleotide binding; q_global = 0.00766)(GO:MF carbohydrate derivative binding; q_global = 0.00998) (GO:MF nucleotide binding; q_global = 0.0247) (GO:MF anion binding; q_global = 0.0287)(GO:MF nucleoside phosphate binding; q_global = 0.0311), and STRING connects it to ALDH18A1, GART, and GMPS (STRING Keyword Ligase; within-query FDR = 1.22e-07)(STRING Function Ligase activity; within-query FDR = 1.66e-06)(STRING Process Cellular amino acid metabolic process; within-query FDR = 3.52e-05). hu.MAP also places CAD with FASN (hu.MAP huMAP3_10103.1). Its established trifunctional activity supplies early pyrimidine biosynthesis, a function relevant to proliferating or transcriptionally active cells, and it has a very large literature base with developmental and neurological disease associations.
- **Conclusion**: Established conclusion: CAD is the clearest metabolic-support component of the module and connects nucleotide availability to the translational program. Hypothesis: CAD abundance may mark the biosynthetic demand that permits the RNA and protein production program to operate in both tissues.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): CAD (0.93), EFTUD2 (0.90), DHX9 (0.86), ALDH18A1 (0.85), UGGT1 (0.85), RARS1 (0.84), FARSB (0.81), EIF3C (0.81), SF3A1 (0.80); STRING partners: DHX9 (0.784), EFTUD2 (0.999), SF3A1 (0.999), SF3B3 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is a core U5 spliceosomal helicase with direct STRING relationships to EFTUD2, SF3A1, and SF3B3 and repeated hu.MAP membership in spliceosomal complexes (hu.MAP huMAP3_08980.1)(hu.MAP huMAP3_00960.1)(hu.MAP huMAP3_07622.1)(hu.MAP huMAP3_08501.1)(hu.MAP huMAP3_09504.1)(hu.MAP huMAP3_09945.1). It contributes to globally corrected RNA catalytic, RNA-binding, protein-RNA assembly, and osteoblast-related terms (GO:MF catalytic activity, acting on RNA; q_global = 5.44e-05)(GO:MF RNA binding; q_global = 0.00033)(GO:BP osteoblast differentiation; q_global = 0.000895)(GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.0018)(GO:MF nucleic acid binding; q_global = 0.00463)(GO:BP ossification; q_global = 0.00774)(GO:BP protein-RNA complex assembly; q_global = 0.031) (GO:MF nucleoside phosphate binding; q_global = 0.0311) (GO:BP protein-RNA complex organization; q_global = 0.0406). Its disease associations include retinitis pigmentosa and inherited retinal dystrophy, and it has a substantial literature base. Its network position makes it a representative of the module's pre-mRNA processing arm.
- **Conclusion**: Established conclusion: SNRNP200 demonstrates that the module includes a recognized spliceosomal component rather than being limited to translation. Hypothesis: coordinated spliceosome and aminoacylation activity may support rapid production of correctly processed transcripts in the shared cell state.

#### ADAR

- **Related proteins** (co-abundance neighbors): EPRS1 (0.88), HSPH1 (0.87), EIF4G1 (0.84), CAD (0.82), DHX9 (0.82), VARS1 (0.81), PSMC2 (0.80); STRING partners: DHX9 (0.922)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR links the module to RNA editing, RNA processing, and antiviral response biology. It is connected to DHX9 in STRING and appears in globally corrected RNA catalytic, RNA-binding, nucleic-acid, protein-RNA assembly, and osteoblast-related terms (GO:MF catalytic activity, acting on a tRNA; q_global = 1.34e-05)(GO:MF catalytic activity, acting on RNA; q_global = 5.44e-05)(GO:MF RNA binding; q_global = 0.00033)(GO:BP osteoblast differentiation; q_global = 0.000895)(GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.0018)(GO:MF nucleic acid binding; q_global = 0.00463)(GO:BP ossification; q_global = 0.00774)(GO:BP protein-RNA complex assembly; q_global = 0.031) (GO:MF nucleoside phosphate binding; q_global = 0.0311) (GO:BP protein-RNA complex organization; q_global = 0.0406). Its established function is adenosine-to-inosine editing of double-stranded RNA, with roles in RNA processing and responses to viruses. It has extensive literature and disease associations including Aicardi-Goutières syndrome, dyschromatosis, and interferonopathy.
- **Conclusion**: Established conclusion: ADAR supplies a specific RNA-editing and innate-response dimension to an otherwise translation- and splicing-dominated module. Hypothesis: ADAR may modulate the RNA substrate pool or stress-response state that accompanies the shared co-abundance program.

## Module 8

**Tissue pair**: bone_marrow and rectum  
**Genes (9)**: CASP8, CNOT1, INF2, LACTB, NUP155, PUS1, RNF213, SEC24A, ZW10

### Function

No GO or KEGG term passed global correction, so there is no statistically supported pathway-level assignment from those analyses. The gene set is functionally heterogeneous: CASP8 links apoptosis, cytokine regulation and immune processes; PUS1 supports RNA modification and mitochondrial tRNA biology; SEC24A supports COPII-dependent endoplasmic-reticulum-to-Golgi transport; CNOT1 supports mRNA deadenylation and gene-expression control; ZW10 supports mitotic checkpoint and vesicle-trafficking biology; NUP155 supports nucleocytoplasmic transport; INF2 supports actin organization and mitochondrial fission; and RNF213 supports ubiquitin-related, vascular and defense-associated biology. The co-abundance structure therefore suggests coordinated regulation of broadly distributed cellular maintenance programs, with CASP8 as the main network connector, rather than a single established pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and the module is not blood-cell specific according to HPA. Nevertheless, most genes show cell-type-enhanced expression, with neutrophils the most recurrent enriched cell type, while other signals include cardiomyocytes, innate lymphoid cells, NK cells, T cells, spermatocytes, mast cells, monocytes, colonocytes and megakaryocytes. This mixed pattern argues against interpreting the module as a dedicated blood-cell program. Its presence in bone marrow and rectum may partly reflect shared or variable cell populations, but the HPA evidence does not establish a single contaminating cell type. Protein detection is broadly compatible with the module being measurable in both tissues, although NUP155 lacks detection in rectum and SEC24A lacks detection in bone marrow in the supplied HPA data.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was present among the module genes, and STRING functional enrichment was absent. Thus, the co-abundance edges should not be treated as established physical protein interactions or as a known STRING pathway. The only supplied hu.MAP relationship is (hu.MAP huMAP3_11232.1), a large, heterogeneous complex containing ZW10 and RNF213 among its module members. This provides limited complex-level support for a relationship between those two genes, but the large membership and low representation of the complex within the module do not establish a compact mechanistic complex. Overall, the network is primarily a co-abundance observation with little support from currently catalogued high-confidence physical interactions.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11232.1 (ZW10, RNF213; 2/78)

### Novelty

This may be a novel tissue-pair co-abundance pattern, but the evidence is insufficient to call it a new biological mechanism. The absence of STRING interactions and the limited hu.MAP overlap make the module less recognizable as a previously curated protein complex, yet database absence alone cannot prove novelty. The genes themselves have substantial established biology and disease literature, so the potentially novel element is their coordinated abundance across bone marrow and rectum rather than the discovery of uncharacterized genes. Replication in independent cohorts, preservation after adjustment for cell composition, and testing whether the same edges recur across datasets would be required before claiming a new conserved module.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program combining stress-responsive apoptosis and immune regulation through CASP8, RNA and protein-handling processes through PUS1, CNOT1 and SEC24A, and structural, transport or cell-cycle support through INF2, NUP155 and ZW10, with RNF213 contributing a vascular or inflammatory regulatory component. A plausible explanation for conservation between bone marrow and rectum is a common mixture of proliferative, immune-associated and metabolically active cells, rather than one lineage-specific pathway. This hypothesis predicts that module abundance will track cellular stress, immune-state composition or tissue regeneration, and that its apparent edges may weaken after rigorous cell-composition correction.

### Important genes

#### CASP8

- **Related proteins** (co-abundance neighbors): LACTB (0.89), ZW10 (0.88), SEC24A (0.83), CNOT1 (0.82), RNF213 (0.82), INF2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caspase 8. This gene encodes a member of the cysteine-aspartic acid protease (caspase) family. Sequential activation of caspases plays a central role in the execution-phase of cell apoptosis. Caspases exist as inactive proenzymes composed of a prodomain, a large protease subunit, and a small protease subunit. Activation of caspases requires proteolytic processing at conserved internal aspartic residues to ge…
- **Diseases (Open Targets)**: autoimmune lymphoproliferative syndrome type 2B (0.780); head and neck squamous cell carcinoma (0.612); neurodegenerative disease (0.543); viral infectious disease (0.508); autoimmune lymphoproliferative syndrome (0.477)
- **Europe PMC papers**: 40495
- **Why important**: CASP8 is the central network connector, linking most of the other module members. Its established annotation includes caspase-mediated apoptosis, cytokine production and immune-system regulation, and HPA shows cell-type-enhanced expression across several immune-related cell types as well as tissue enhancement in bone marrow. Its disease associations include autoimmune lymphoproliferative syndromes, viral infection and cancer-related disease, and it has the largest literature volume among the listed genes.
- **Conclusion**: Established evidence supports CASP8 as the strongest integrative candidate and a plausible marker of apoptosis or immune-state biology in the module. It is not established that CASP8 physically connects the other proteins in this module, because STRING reports no such interactions. Its hub position is therefore a co-abundance property, not proof of direct biochemical control.

#### RNF213

- **Related proteins** (co-abundance neighbors): CASP8 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: huMAP3_11232.1
- **Function (MyGene.info)**: ring finger protein 213. This gene encodes a protein containing a C3HC4-type RING finger domain, which is a specialized type of Zn-finger that binds two atoms of zinc and is thought to be involved in mediating protein-protein interactions. The protein also contains an AAA domain, which is associated with ATPase activity. This gene is a susceptibility gene for Moyamoya disease, a vascular disorder of intracranial arteries.…
- **Diseases (Open Targets)**: Moyamoya disease (0.753); angina pectoris (0.490); migraine disorder (0.444); hereditary disease (0.438); Abnormality of the skeletal system (0.431)
- **Europe PMC papers**: 2104
- **Why important**: RNF213 is directly connected to CASP8 in the co-abundance graph and is one of the two module members represented in the hu.MAP complex (hu.MAP huMAP3_11232.1). It has established RING-finger and AAA-domain features, associations with ubiquitin-related processes, defense response and angiogenesis, and a strong disease association with Moyamoya disease. HPA identifies enhanced expression in neutrophils and alveolar cells, making it relevant to the mixed immune and vascular interpretation.
- **Conclusion**: Established evidence supports RNF213 as a biologically consequential immune-vascular and protein-regulatory candidate. The module data support co-abundance with CASP8 and limited complex-level context through (hu.MAP huMAP3_11232.1), but do not establish that RNF213 drives the module or mediates its conservation between tissues.

#### PUS1

- **Related proteins** (co-abundance neighbors): SEC24A (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pseudouridine synthase 1. This gene encodes a pseudouridine synthase that converts uridine to pseudouridine once it has been incorporated into an RNA molecule. The encoded enzyme may play an essential role in tRNA function and in stabilizing the secondary and tertiary structure of many RNAs. A mutation in this gene has been linked to mitochondrial myopathy and sideroblastic anemia. Alternate splicing results in multiple tr…
- **Diseases (Open Targets)**: myopathy, lactic acidosis, and sideroblastic anemia (0.819); mitochondrial disease (0.400); Intellectual disability (0.370); sulfite oxidase deficiency due to molybdenum cofactor deficiency type B1 (0.340); hereditary disease (0.193)
- **Europe PMC papers**: 993
- **Why important**: PUS1 forms the module connection between RNA modification and the central CASP8-linked network through SEC24A. Its established function is pseudouridine synthesis affecting tRNA, mitochondrial RNA and mRNA, and mutations are associated with mitochondrial myopathy and sideroblastic anemia. Its detection in both tissues and mitochondrial localization make it relevant to a cellular maintenance or metabolic-stress interpretation.
- **Conclusion**: Established evidence supports PUS1 as an RNA-quality and mitochondrial-function component. Its module membership may indicate coordinated regulation of RNA handling with broader cellular-state changes, but the data do not establish a direct functional connection between PUS1 and CASP8 or SEC24A.

#### CNOT1

- **Related proteins** (co-abundance neighbors): NUP155 (0.82), CASP8 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CCR4-NOT transcription complex subunit 1. Enables armadillo repeat domain binding activity; molecular adaptor activity; and nuclear receptor binding activity. Contributes to poly(A)-specific ribonuclease activity. Involved in several processes, including negative regulation of signal transduction; positive regulation of cytoplasmic mRNA processing body assembly; and regulation of gene expression. Located in P-body and cytosol. Part of CCR…
- **Diseases (Open Targets)**: holoprosencephaly 12 with or without pancreatic agenesis (0.749); Vissers-Bodmer syndrome (0.697); hereditary disease (0.515); complex neurodevelopmental disorder (0.474); neurodegenerative disease (0.471)
- **Europe PMC papers**: 1262
- **Why important**: CNOT1 connects CASP8 with NUP155 and is the principal represented scaffold for CCR4-NOT-related post-transcriptional regulation in the module. Its established functions include mRNA deadenylation, regulation of translation, gene expression and processing-body assembly. It is detected in both tissues and has a documented association with holoprosencephaly.
- **Conclusion**: Established evidence supports CNOT1 as a broad gene-expression and mRNA-stability regulator that could help explain coordinated abundance of otherwise diverse genes. The module does not demonstrate that CNOT1 regulates the other module members, so this remains a mechanistic interpretation rather than a demonstrated causal relationship.

#### INF2

- **Related proteins** (co-abundance neighbors): CASP8 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inverted formin 2. This gene represents a member of the formin family of proteins. It is considered a diaphanous formin due to the presence of a diaphanous inhibitory domain located at the N-terminus of the encoded protein. Studies of a similar mouse protein indicate that the protein encoded by this locus may function in polymerization and depolymerization of actin filaments. Mutations at this locus have been associ…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease dominant intermediate E (0.827); focal segmental glomerulosclerosis 5 (0.807); focal segmental glomerulosclerosis (0.614); familial idiopathic steroid-resistant nephrotic syndrome (0.554); hereditary disease (0.503)
- **Europe PMC papers**: 1742
- **Why important**: INF2 is connected to CASP8 and contributes an actin and organelle-structure dimension to the module. Its established functions include actin filament polymerization, cytoskeleton organization and regulation of mitochondrial fission. It is cell-type enhanced in several tissue and blood-associated cell types, and is associated with Charcot-Marie-Tooth disease and focal segmental glomerulosclerosis.
- **Conclusion**: Established evidence supports INF2 as a structural and mitochondrial candidate that could couple cellular architecture to stress responses. The module supports coordinated abundance with CASP8, but does not show that INF2 mediates apoptosis, immune behavior or tissue sharing in this context.

## Module 9

**Tissue pair**: bone_marrow and rectum  
**Genes (6)**: COL6A1, COL6A2, COL6A3, FN1, HSPG2, TNC

### Function

This is a conserved extracellular-matrix structural and cell-adhesion module. The primary evidence is exceptionally coherent: every module gene supports extracellular-matrix structural constituent and extracellular-matrix or external-encapsulating-structure annotations (GO:MF extracellular matrix structural constituent; q_global = 2.9e-08), (GO:CC external encapsulating structure; q_global = 2.19e-07), (GO:CC extracellular matrix; q_global = 2.19e-07), while the complete module also maps to ECM-receptor interaction (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 2.9e-08). The collagen-related terms identify a type VI collagen scaffold formed by COL6A1, COL6A2, and COL6A3 (GO:MF extracellular matrix structural constituent conferring tensile strength; q_global = 0.00369), (GO:CC collagen trimer; q_global = 0.00507), (GO:CC collagen type VI trimer; q_global = 0.0193), (GO:CC collagen beaded filament; q_global = 0.0193), (GO:CC basement membrane/interstitial matrix interface; q_global = 0.0193), (GO:CC von-Willerbrand-factor-A-domain-rich collagen trimer; q_global = 0.0193). FN1, HSPG2, and TNC provide matrix-organization, adhesion, and signaling context. Integrin signaling, focal adhesion, and PI3K-Akt pathway annotations (KEGG PI3K-Akt signaling pathway - Homo sapiens (human); q_global = 4.04e-05), (KEGG Integrin signaling - Homo sapiens (human); q_global = 8.05e-05), (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.00018) support a role in coupling matrix composition to cell attachment and intracellular responses, but they should be interpreted as pathway context rather than proof of pathway activation. The collagen-binding and structural-molecule annotations (GO:MF structural molecule activity; q_global = 0.000761), (GO:MF collagen binding; q_global = 0.0109) reinforce a physical extracellular scaffold interpretation. The lung-morphogenesis term (GO:BP lung morphogenesis; q_global = 0.0455) is not sufficient to assign a lung-specific function. Overall, the strongest interpretation is a stromal extracellular-matrix module involved in matrix assembly, tissue architecture, adhesion, and remodeling.

**Cell composition.** The module is composed entirely of secreted extracellular-matrix proteins according to the HPA evidence. It is therefore not a plasma-protein or blood-cell module, and most genes are not detected in immune cells. HPA emphasizes smooth-muscle cells, fibroblasts, hepatic stellate cells, stromal populations, and vascular compartments, which is consistent with stromal and vascular matrix biology rather than hematopoietic identity. The apparent conservation between bone marrow and rectum may consequently reflect shared stromal, vascular, or connective-tissue components in the sampled tissues. HPA protein detection is present for some genes in each tissue but absent for others, so the co-abundance signal should not be interpreted as uniform protein expression throughout either tissue. COL6A2 has a blood-cell group-enriched annotation, but the broader module evidence does not support a blood-cell-centered interpretation.

**GO/KEGG enrichment**: 21 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF extracellular matrix structural constituent | 2.9e-08 | COL6A1, COL6A2, COL6A3, FN1, HSPG2, TNC |
| KEGG ECM-receptor interaction - Homo sapiens (human) | 2.9e-08 | COL6A1, COL6A2, COL6A3, FN1, HSPG2, TNC |
| GO:CC external encapsulating structure | 2.19e-07 | COL6A1, COL6A2, COL6A3, FN1, HSPG2, TNC |
| GO:CC extracellular matrix | 2.19e-07 | COL6A1, COL6A2, COL6A3, FN1, HSPG2, TNC |
| KEGG PI3K-Akt signaling pathway - Homo sapiens (human) | 4.04e-05 | COL6A1, COL6A2, COL6A3, FN1, TNC |
| KEGG Integrin signaling - Homo sapiens (human) | 8.05e-05 | COL6A1, COL6A2, COL6A3, FN1, TNC |
| KEGG Focal adhesion - Homo sapiens (human) | 0.00018 | COL6A1, COL6A2, COL6A3, FN1, TNC |
| GO:CC basement membrane | 0.000232 | COL6A1, FN1, HSPG2, TNC |
| KEGG Human papillomavirus infection - Homo sapiens (human) | 0.000265 | COL6A1, COL6A2, COL6A3, FN1, TNC |
| GO:MF structural molecule activity | 0.000761 | COL6A1, COL6A2, COL6A3, FN1, HSPG2, TNC |
| KEGG Cytoskeleton in muscle cells - Homo sapiens (human) | 0.000939 | COL6A1, COL6A2, COL6A3, FN1, HSPG2 |
| GO:CC endoplasmic reticulum lumen | 0.00184 | COL6A1, COL6A2, COL6A3, FN1, TNC |
| GO:MF extracellular matrix structural constituent conferring tensile strength | 0.00369 | COL6A1, COL6A2, COL6A3 |
| GO:CC collagen trimer | 0.00507 | COL6A1, COL6A2, COL6A3 |
| GO:MF collagen binding | 0.0109 | COL6A1, COL6A2, FN1 |

### STRING and hu.MAP

STRING independently recovers the expected collagen VI relationships among COL6A1, COL6A2, and COL6A3, as well as links from the collagen unit to FN1. FN1 is also linked to HSPG2 and TNC. These relationships are concordant with collagen assembly, matrix cross-linking, adhesion, and extracellular-matrix organization, and they indicate that much of the module reflects already known biology rather than an unexplained interaction pattern. STRING functional enrichment agrees with the primary GO and KEGG interpretation through ECM-receptor interaction, extracellular-matrix structural constituent, collagen formation, integrin interactions, focal adhesion, and matrix degradation (STRING KEGG ECM-receptor interaction; within-query FDR = 1e-09) through (STRING WikiPathways miRNA targets in ECM and membrane receptors; within-query FDR = 1.03e-05). No hu.MAP complex contains multiple module members. This absence means that the module is better represented as an extracellular network of matrix components and known associations than as a hu.MAP-defined intracellular protein complex.

**STRING interactions (score >= 0.7)**: 8 of 15 gene pairs: COL6A1–COL6A2 (0.998); COL6A1–COL6A3 (0.994); COL6A1–FN1 (0.78); COL6A2–COL6A3 (0.994); COL6A2–FN1 (0.802); COL6A3–FN1 (0.736); FN1–HSPG2 (0.996); FN1–TNC (0.814)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG ECM-receptor interaction (FDR = 1e-09, 6 genes); Function Extracellular matrix structural constituent (FDR = 2.19e-09, 6 genes); RCTM ECM proteoglycans (FDR = 2.49e-09, 6 genes); Keyword Extracellular matrix (FDR = 3.85e-09, 6 genes); RCTM Integrin cell surface interactions (FDR = 6.29e-09, 6 genes); COMPARTMENTS External encapsulating structure (FDR = 4.45e-08, 6 genes); COMPARTMENTS Collagen-containing extracellular matrix (FDR = 4.45e-08, 6 genes); NetworkNeighborAL Collagen formation, and Protein complex involved in cell adhesion (FDR = 6.75e-08, 6 genes); RCTM Degradation of the extracellular matrix (FDR = 9.59e-07, 5 genes); KEGG PI3K-Akt signaling pathway (FDR = 1.3e-06, 5 genes); Component Collagen-containing extracellular matrix (FDR = 3.95e-06, 6 genes); KEGG Focal adhesion (FDR = 4.66e-06, 5 genes); WikiPathways PI3K-Akt signaling pathway (FDR = 4.69e-06, 5 genes); KEGG Human papillomavirus infection (FDR = 5.5e-06, 5 genes); WikiPathways miRNA targets in ECM and membrane receptors (FDR = 1.03e-05, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is a biologically convincing conserved co-abundance finding, but it should not be called a newly discovered molecular complex or a wholly novel pathway. The collagen VI genes form an established structural unit, and the STRING links among collagen VI, FN1, HSPG2, and TNC are already known. The potentially novel aspect is the reproducible co-abundance of this particular extracellular-matrix program across bone marrow and rectum, especially if that tissue-pair conservation has not previously been reported in the underlying dataset. However, the fact sheet alone does not establish novelty against all prior co-expression, proteomic, or tissue-compartment studies. The most defensible claim is a new cross-tissue network observation built from largely established extracellular-matrix biology.

**Hypothesis.** Hypothesis: a shared stromal or vascular extracellular-matrix compartment produces coordinated collagen VI, fibronectin, perlecan, and tenascin C abundance in bone marrow and rectum. COL6A1, COL6A2, and COL6A3 may assemble the collagen VI scaffold; FN1 may organize and connect that scaffold with other matrix components; HSPG2 may stabilize and cross-link matrix and cell-surface interactions; and TNC may modulate adhesion and tissue remodeling in a context-dependent manner. The resulting matrix could influence integrin-linked focal adhesion and PI3K-Akt signaling (KEGG PI3K-Akt signaling pathway - Homo sapiens (human); q_global = 4.04e-05), (KEGG Integrin signaling - Homo sapiens (human); q_global = 8.05e-05), (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.00018). This is a mechanistic hypothesis, not proof that these genes directly regulate one another or that the signaling pathways are activated in the measured samples. Testing it would require cell-resolved expression, spatial localization, matrix-protein measurements, and perturbation of stromal matrix components.

### Important genes

#### FN1

- **Related proteins** (co-abundance neighbors): TNC (0.86), COL6A3 (0.85), HSPG2 (0.85), COL6A2 (0.80), COL6A1 (0.80); STRING partners: COL6A1 (0.78), COL6A2 (0.802), COL6A3 (0.736), HSPG2 (0.996), TNC (0.814)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 is the central network connector, linking every other module member in the supplied subgraph. It is a secreted matrix and plasma-associated glycoprotein involved in adhesion, migration, wound healing, coagulation, and cell-matrix signaling. It participates in all major primary module interpretations, including ECM-receptor interaction, integrin signaling, focal adhesion, and collagen binding (GO:MF extracellular matrix structural constituent; q_global = 2.9e-08), (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 2.9e-08), (KEGG PI3K-Akt signaling pathway - Homo sapiens (human); q_global = 4.04e-05), (KEGG Integrin signaling - Homo sapiens (human); q_global = 8.05e-05), (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.00018), (GO:MF collagen binding; q_global = 0.0109). Its links to the collagen VI genes, HSPG2, and TNC are also supported by STRING. It has extensive literature and disease associations involving connective tissue, vascular disease, cancer, and fibronectin deposition disorders.
- **Conclusion**: Established evidence supports FN1 as the organizing hub and a major interface between matrix structure and cell adhesion. Hypothesis: FN1 may coordinate the other module components into a functional matrix niche shared by the two tissues.

#### COL6A1

- **Related proteins** (co-abundance neighbors): COL6A2 (0.96), COL6A3 (0.92), FN1 (0.80); STRING partners: COL6A2 (0.998), COL6A3 (0.994), FN1 (0.78)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is a core component of the collagen VI trimer with COL6A2 and COL6A3. It is connected to both other collagen VI genes and to FN1, and it appears across the primary structural, extracellular-matrix, collagen, adhesion, and pathway annotations (GO:MF extracellular matrix structural constituent; q_global = 2.9e-08) through (GO:BP lung morphogenesis; q_global = 0.0455). Its established functions include maintaining connective-tissue integrity, forming collagen VI microfibrils, and supporting tissue and skeletal-muscle biology. It has well-established associations with Bethlem myopathy and Ullrich congenital muscular dystrophy and substantial literature.
- **Conclusion**: Established evidence identifies COL6A1 as a structural backbone gene for the collagen VI portion of the module. Hypothesis: its coordinated abundance may mark the amount or organization of collagen VI microfibrillar matrix in shared stromal compartments.

#### COL6A3

- **Related proteins** (co-abundance neighbors): COL6A1 (0.92), COL6A2 (0.92), FN1 (0.85); STRING partners: COL6A1 (0.994), COL6A2 (0.994), FN1 (0.736)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 3 chain. This gene encodes the alpha-3 chain, one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The alpha-3 chain of type VI collagen is much larger than the alpha-1 and -2 chains. This difference in size is largely due to an increase in the number of subdomains, similar to von Willebrand Factor type A domains, that are found in the amino termin…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy (0.766); dystonia 27 (0.764); Bethlem myopathy (0.758); Bethlem myopathy 1C (0.747); Bethlem myopathy 1A (0.718)
- **Europe PMC papers**: 5386
- **Why important**: COL6A3 is a collagen VI alpha chain with strong network connections to COL6A1, COL6A2, and FN1. It contributes to the collagen trimer, beaded filament, basement-membrane/interstitial-matrix interface, tensile matrix, and ECM-receptor interpretations (GO:MF extracellular matrix structural constituent; q_global = 2.9e-08), (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 2.9e-08), (GO:CC basement membrane; q_global = 0.000232), (GO:MF extracellular matrix structural constituent conferring tensile strength; q_global = 0.00369), (GO:CC collagen trimer; q_global = 0.00507), (GO:CC collagen type VI trimer; q_global = 0.0193), (GO:CC collagen beaded filament; q_global = 0.0193), (GO:CC basement membrane/interstitial matrix interface; q_global = 0.0193), (GO:CC von-Willerbrand-factor-A-domain-rich collagen trimer; q_global = 0.0193). HPA associates it with smooth muscle and multiple fibroblast or stromal populations. It has established disease links to Bethlem myopathy, Ullrich congenital muscular dystrophy, and related muscle disorders.
- **Conclusion**: Established evidence supports COL6A3 as a key collagen VI assembly and stromal-matrix component. Hypothesis: COL6A3 may help determine matrix architecture or tissue mechanical properties in the conserved stromal program.

#### COL6A2

- **Related proteins** (co-abundance neighbors): COL6A1 (0.96), COL6A3 (0.92), FN1 (0.80); STRING partners: COL6A1 (0.998), COL6A3 (0.994), FN1 (0.802)
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 2 chain. This gene encodes one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The product of this gene contains several domains similar to von Willebrand Factor type A domains. These domains have been shown to bind extracellular matrix proteins, an interaction that explains the importance of this collagen in organizing matrix components. Mutation…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy 1B (0.770); Bethlem myopathy (0.755); Ullrich congenital muscular dystrophy (0.743); Bethlem myopathy 1B (0.723); Bethlem myopathy 1A (0.713)
- **Europe PMC papers**: 4115
- **Why important**: COL6A2 is the third member of the collagen VI structural unit and is strongly connected to COL6A1, COL6A3, and FN1. Its annotations support extracellular-matrix structure, collagen trimers, ECM-receptor interaction, focal adhesion, and integrin-related biology (GO:MF extracellular matrix structural constituent; q_global = 2.9e-08), (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 2.9e-08), (KEGG Integrin signaling - Homo sapiens (human); q_global = 8.05e-05), (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.00018), (GO:MF extracellular matrix structural constituent conferring tensile strength; q_global = 0.00369), (GO:CC collagen trimer; q_global = 0.00507). HPA places it in fibroblast and stromal populations and reports a blood-cell group-enriched signal that warrants attention when interpreting bone marrow. It has established associations with Bethlem myopathy and Ullrich scleroatonic muscular dystrophy.
- **Conclusion**: Established evidence supports COL6A2 as an essential collagen VI scaffold component, while its blood-cell annotation is a possible confounder rather than evidence that the module is hematopoietic. Hypothesis: COL6A2 may contribute to the tissue-specific balance between stromal matrix and any minor blood-cell-associated signal.

#### TNC

- **Related proteins** (co-abundance neighbors): FN1 (0.86); STRING partners: FN1 (0.814)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tenascin C. This gene encodes an extracellular matrix protein with a spatially and temporally restricted tissue distribution. This protein is homohexameric with disulfide-linked subunits, and contains multiple EGF-like and fibronectin type-III domains. It is implicated in guidance of migrating neurons as well as axons during development, synaptic plasticity, and neuronal regeneration. [provided by RefSeq, Jul…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss (0.619); deafness (0.552); osteoarthritis, hip (0.551); total hip arthroplasty (0.468); Varicose veins (0.460)
- **Europe PMC papers**: 12274
- **Why important**: TNC is a secreted extracellular-matrix protein linked to FN1 in the module network. It has tissue-enhanced expression in blood vessel and smooth muscle compartments and is associated with regulation of cell growth, adhesion, epithelial morphogenesis, osteoblast differentiation, and response to wounding. It contributes to the module's ECM-receptor, integrin, focal-adhesion, PI3K-Akt, and wound- or morphogenesis-related annotations (GO:MF extracellular matrix structural constituent; q_global = 2.9e-08), (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 2.9e-08), (KEGG PI3K-Akt signaling pathway - Homo sapiens (human); q_global = 4.04e-05), (KEGG Integrin signaling - Homo sapiens (human); q_global = 8.05e-05), (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.00018), (GO:BP lung morphogenesis; q_global = 0.0455). It also has substantial literature and disease associations involving osteoarthritis, vascular traits, and hearing disorders.
- **Conclusion**: Established evidence supports TNC as a context-dependent matrix signaling and remodeling component connected to the FN1-centered network. Hypothesis: TNC may tune adhesion and remodeling during tissue repair or mechanical adaptation rather than serving as a constitutive structural collagen.

## Module 10

**Tissue pair**: bone_marrow and rectum  
**Genes (6)**: PPP6R3, RBM47, UFSP2, VPS4A, YLPM1, ZCCHC8

### Function

The module does not have a globally significant GO or KEGG enrichment term. Its strongest interpretive signal is a coordinated intracellular RNA and protein-homeostasis theme. UFSP2 is a conserved de-UFMylating cysteine protease involved in activation of the UFM one modifier system and in rescue of stalled cytosolic ribosomes. ZCCHC8 is an accessory scaffold for the nuclear RNA exosome targeting complex and participates in nuclear RNA processing and degradation. RBM47 is an RNA-binding protein associated with RNA editing, alternative splicing, RNA stabilization, interferon signaling, and hematopoietic progenitor differentiation. PPP6R3 contributes to regulation of signal transduction through protein phosphatase six. VPS4A is an AAA ATPase involved in membrane repair, vesicle budding, lysosomal targeting, autophagy, and related cellular organization. YLPM1 has annotated links to RNA binding, nuclear speckles, transcriptional regulation, and telomere maintenance. Taken together, the genes are more consistent with general RNA surveillance, proteostasis, and intracellular regulation than with a narrowly defined tissue-specific pathway. This interpretation remains provisional because the module lacks globally significant pathway enrichment and has only a sparse co-abundance structure.

**Cell composition.** The module is not composed of plasma or secreted proteins: none of the genes is annotated as secreted. Most genes have low tissue specificity and low immune-cell specificity, and all have protein detection in rectum while nearly all are detected in bone marrow. One gene is tissue-enhanced in bone marrow, and several show cell-type-enhanced patterns, including associations with esophageal apical cells, monocytes, neutrophils, choroid plexus epithelial cells, or syncytiotrophoblasts. One gene is immune-cell enhanced and associated with neutrophils. This mixture argues against interpreting the module as a pure blood-cell or secreted-protein signature. It may instead reflect broadly expressed intracellular machinery, with some contribution from shared or variable cell populations in the two tissues. The absence of a clear secreted or uniformly immune-cell composition makes a simple plasma contamination explanation less compelling, but cellular composition remains a plausible contributor to co-abundance.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

At the supplied high-confidence STRING threshold, no pair among the module genes has a recorded interaction, and no STRING functional-enrichment result is available. No hu.MAP complex contains multiple module members. Thus the co-abundance edges are not supported by the reported high-confidence physical-interaction or curated-complex evidence. The biological annotations nevertheless identify plausible processes within individual genes, such as UFSP2-mediated UFMylation control, ZCCHC8-associated nuclear exosome targeting, RBM47-mediated RNA regulation, and VPS4A-mediated membrane and vesicle processes. These are established gene-level functions, not evidence that the proteins form one physical complex. The network may therefore represent coordinated expression of broadly required cellular systems rather than a canonical molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a new biological discovery on the current evidence. Its exact cross-tissue co-abundance pattern may be a potentially novel observation, but the module has no globally significant GO or KEGG term, no supplementary STRING enrichment, no high-confidence STRING pair, and no multi-member hu.MAP complex. The absence of database relationships does not demonstrate novelty, because databases are incomplete and co-abundance does not require direct physical interaction. A novelty claim would require replication in independent cohorts, preservation of the same gene relationships, comparison with published co-expression modules, and ideally experimental or perturbational validation. At present, the defensible conclusion is that this is an unexplained and potentially interesting coordinated-expression module rather than an established new pathway.

**Hypothesis.** Hypothesis: the module reflects a shared cellular stress or maintenance state in which RNA quality control, RNA processing, translational rescue, de-UFMylation, phosphatase regulation, and membrane-trafficking or repair capacity are coordinately regulated in bone marrow and rectum. UFSP2 may represent a central organizing signal because it has the strongest network connectivity and links to ribosome rescue and protein modification, while its co-abundance with ZCCHC8 and RBM47 could indicate coordinated management of damaged, aberrant, or transcription-associated RNA. VPS4A may connect this maintenance state to membrane remodeling or repair. This is a mechanistic hypothesis, not an established interaction model, and it should be tested by replication, cell-type-resolved analysis, and perturbation of the proposed central genes.

### Important genes

#### UFSP2

- **Related proteins** (co-abundance neighbors): YLPM1 (0.91), ZCCHC8 (0.84), VPS4A (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UFM1 specific peptidase 2. This gene encodes a highly conserved cysteine protease. The protein cleaves two C-terminal residues from ubiquitin-fold modifier 1, a ubiquitin-like post-translational modifier protein. Activation of ubiquitin-fold modifier 1 by the encoded protein exposes a C-terminal glycine residue that allows interaction with other proteins and transfer to its target protein. An allelic variant of this gene ha…
- **Diseases (Open Targets)**: spondyloepimetaphyseal dysplasia, di rocco type (0.708); hip dysplasia, Beukes type (0.640); developmental and epileptic encephalopathy 106 (0.611); Intellectual disability (0.546); Seizure (0.492)
- **Europe PMC papers**: 317
- **Why important**: UFSP2 has the strongest network position in the module and connects to YLPM1, ZCCHC8, and VPS4A. Its established function as a UFM one modifier-processing protease links it to post-translational regulation, ribosome disassembly, and rescue of stalled cytosolic ribosomes. It is broadly detected in both tissues, has low tissue specificity, and has disease associations involving skeletal development, neurodevelopment, and seizures. Its literature base is substantial, supporting a comparatively well-developed biological interpretation.
- **Conclusion**: Established evidence supports UFSP2 as a proteostasis and translational-quality-control regulator with relevance to skeletal and neurological disease. Its centrality makes it a leading candidate for organizing the module, but the co-abundance data do not establish that it regulates the other module genes. The proposed central role is therefore a hypothesis.

#### ZCCHC8

- **Related proteins** (co-abundance neighbors): UFSP2 (0.84), RBM47 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger CCHC-type containing 8. This gene encodes a scaffold protein which serves as an assessory factor to the nuclear RNA exosome complex. The encoded protein forms a trimeric human nuclear exosome targeting (NEXT) complex, together with hMTR4 and the RNA-binding factor RBM7 which promotes the exosomal degradation of non-coding promoter-upstream transcripts, enhancer RNAs and 3'-extended products of histone- and small nuclear …
- **Diseases (Open Targets)**: pulmonary fibrosis, and/or bone marrow failure, telomere-related, 5 (0.562); neurodegenerative disease (0.460); dyskeratosis congenita (0.355); inherited aplastic anemia (0.333); inherited acute myeloid leukemia (0.266)
- **Europe PMC papers**: 597
- **Why important**: ZCCHC8 is tissue-enhanced in bone marrow and occupies a bridging position between UFSP2 and RBM47. It is an established scaffold and accessory factor for the nuclear RNA exosome targeting machinery, with functions in RNA processing and degradation. It is detected in both tissues and has disease associations involving bone marrow failure, telomere-related disease, dyskeratosis congenita, aplastic anemia, and acute myeloid leukemia. Its literature base is substantial and directly relevant to RNA surveillance and hematopoietic biology.
- **Conclusion**: Established evidence supports ZCCHC8 as a nuclear RNA-quality-control factor with particular relevance to bone marrow disorders. Its network placement is compatible with a shared RNA-surveillance interpretation, but there is no reported STRING or hu.MAP evidence that it physically complexes with the other module members. Any role as a cross-tissue module mediator remains a hypothesis.

#### RBM47

- **Related proteins** (co-abundance neighbors): PPP6R3 (0.85), ZCCHC8 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 47. Enables RNA binding activity. Predicted to act upstream of or within cytidine to uridine editing and hematopoietic progenitor cell differentiation. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: muscular atrophy (0.271); primary thrombocytopenia (0.267); Pain (0.253); sialolithiasis (0.247); lower urinary tract calculus (0.172)
- **Europe PMC papers**: 768
- **Why important**: RBM47 connects ZCCHC8 and PPP6R3 and is the module gene with immune-cell enhancement associated with neutrophils. It is an RNA-binding protein annotated in RNA editing, alternative splicing, messenger RNA stabilization, interferon signaling, interleukin regulation, and hematopoietic progenitor differentiation. It has the largest literature base among the selected genes and disease associations including thrombocytopenia and muscular atrophy. Its combination of network bridging, RNA biology, and hematopoietic relevance makes it important for interpreting the bone marrow component.
- **Conclusion**: Established evidence supports RBM47 as an RNA regulatory factor with potential relevance to immune and hematopoietic cell biology. Its cell-type-enhanced pattern could contribute to the shared module through cellular composition or state. The data do not establish that RBM47 drives the module or that its relation to ZCCHC8 is physical; those possibilities require experimental testing.

#### VPS4A

- **Related proteins** (co-abundance neighbors): UFSP2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Midbody; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vacuolar protein sorting 4 homolog A. The protein encoded by this gene is a member of the AAA protein family (ATPases associated with diverse cellular activities), and is the homolog of the yeast Vps4 protein. In humans, two paralogs of the yeast protein have been identified. The former share a high degree of aa sequence similarity with each other, and also with yeast Vps4 and mouse Skd1 proteins. The mouse Skd1 (suppressor of K+ tran…
- **Diseases (Open Targets)**: cerebellar hypoplasia-intellectual disability-congenital microcephaly-dystonia-anemia-growth retardation syndrome (0.746); viral infectious disease (0.464); HIV infectious disease (0.462); generalized dystonia (0.259); hereditary disease (0.191)
- **Europe PMC papers**: 998
- **Why important**: VPS4A is directly connected to UFSP2 in the module and has an established role as an AAA ATPase in membrane repair, vesicle budding, lysosomal targeting, autophagy, and cellular organization. It is detected in both tissues, has low tissue specificity, and shows cell-type enhancement in esophageal apical cells. Its disease associations include a neurodevelopmental syndrome involving anemia and growth abnormalities, as well as viral and HIV-related disease categories. Its extensive literature makes its cellular functions comparatively well characterized.
- **Conclusion**: Established evidence supports VPS4A as a membrane-trafficking and repair factor, not as an RNA-surveillance protein. Its connection to UFSP2 may indicate a broader cellular maintenance program, but this is inferential because no high-confidence database interaction was reported. Its inclusion supports a general proteostasis or stress-response hypothesis more than a single dedicated pathway.

#### PPP6R3

- **Related proteins** (co-abundance neighbors): RBM47 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane, Cytosol; IHC detected in bone_marrow, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase 6 regulatory subunit 3. Protein phosphatase regulatory subunits, such as SAPS3, modulate the activity of protein phosphatase catalytic subunits by restricting substrate specificity, recruiting substrates, and determining the intracellular localization of the holoenzyme. SAPS3 is a regulatory subunit for the protein phosphatase-6 catalytic subunit (PPP6C; MIM 612725) (Stefansson and Brautigan, 2006 [PubMed 16769727]).[sup…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.383); hair color (0.341); bone fracture (0.253); Pathologic fracture (0.190); obesity disorder (0.185)
- **Europe PMC papers**: 243
- **Why important**: PPP6R3 is connected to RBM47 and encodes a regulatory subunit that controls the localization and substrate specificity of protein phosphatase six. It is detected in both tissues, has low tissue specificity, and has disease associations involving skeletal abnormalities and fractures. Although its network position is peripheral, it can provide a regulatory link between RNA-associated biology and signal-transduction control.
- **Conclusion**: Established evidence supports PPP6R3 as a signal-transduction regulatory factor. Its presence may indicate that the module captures coordinated regulation rather than a single molecular machine. The available evidence is insufficient to assign it a specific role in the shared bone marrow and rectum program.
