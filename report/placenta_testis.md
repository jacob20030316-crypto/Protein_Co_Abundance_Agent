# Conserved co-abundance modules: placenta and testis

## Module 0

**Tissue pair**: placenta and testis  
**Genes (5)**: ABRACL, CLIC4, FSCN1, LDHB, ACAT2

### Function

The module forms a connected co-abundance chain involving FSCN1, ABRACL, ACAT2, CLIC4, and LDHB. The gene annotations suggest a combination of actin organization, cell polarity and migration, lipid metabolism, lactate and redox metabolism, chloride-related regulation, and cellular differentiation. FSCN1 and ABRACL support an actin and motility interpretation; ACAT2 supports cytosolic lipid metabolism; LDHB supports lactate and NAD metabolism; and CLIC4 supports polarity, differentiation, migration, and cytoskeletal regulation. No GO or KEGG term passed global correction, and there was no STRING functional enrichment. Accordingly, the annotations provide a biologically plausible interpretation but do not establish a statistically enriched pathway. The co-abundance structure is more consistent with a coordinated cellular state than with a demonstrated physical complex.

**Cell composition.** All module proteins were detected by HPA in both placenta and testis, and none was annotated as secreted. The module is therefore not dominated by plasma or secreted proteins. The HPA profile is heterogeneous: several genes show cell-type enhancement, with extravillous trophoblasts recurring among the annotations, while ACAT2 is enhanced in early spermatids and CLIC4 is enhanced in stromal, mesothelial, vascular-associated, and plasma-cell-related populations. FSCN1 and CLIC4 have immune-cell-enhanced annotations, but the module overall has low or limited immune-cell specificity rather than a predominantly blood-cell profile. Tissue annotations include liver, heart muscle, kidney, and blood vessel, alongside genes with low tissue specificity. Shared trophoblast, stromal, epithelial, or germ-cell composition may therefore contribute to the placenta-testis pattern. A simple explanation based on plasma proteins or widespread blood contamination is not supported by the HPA evidence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported for any pair of module genes, and no hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated by the supplied physical-interaction or complex resources. The genes nevertheless have partially convergent functional annotations: FSCN1 organizes actin bundles and supports migration and adhesion; ABRACL is predicted to regulate actin filament-based processes; ACAT2 catalyzes cytosolic acetoacetyl-CoA metabolism; LDHB supports pyruvate-lactate interconversion and NAD metabolism; and CLIC4 is associated with chloride-related regulation, differentiation, polarity, migration, and cytoskeletal organization. These relationships support functional plausibility but do not demonstrate direct binding, pathway membership, or a shared molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The placenta-testis co-abundance association may be a new module-level observation because it lacks high-confidence STRING support, lacks a multi-member hu.MAP complex, and has no globally significant GO or KEGG enrichment. However, these absences do not prove novelty. The individual genes and their functions are already established to differing degrees, and the association could reflect shared cell composition or a recurring cellular state rather than a previously unknown molecular mechanism. A defensible novelty claim is therefore limited to the specific tissue-pair co-abundance pattern. Replication in independent cohorts, together with adjustment for cell-type composition, would be needed before claiming a new biological mechanism.

**Hypothesis.** Hypothesis: a shared cellular state in placenta and testis couples cytoskeletal remodeling and polarity with metabolic adaptation. FSCN1 and ABRACL may support actin organization and motility, while CLIC4 may connect membrane or polarity regulation with the cytoskeleton. ACAT2 and LDHB may reflect accompanying lipid and lactate-redox metabolism. The module may therefore mark a migratory, differentiating, metabolically adapted cell state rather than a stable physical complex. This is a hypothesis and is not directly demonstrated by the enrichment, STRING, or hu.MAP results.

### Important genes

#### FSCN1

- **Related proteins** (co-abundance neighbors): ACAT2 (0.85), ABRACL (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fascin actin-bundling protein 1. This gene encodes a member of the fascin family of actin-binding proteins. Fascin proteins organize F-actin into parallel bundles, and are required for the formation of actin-based cellular protrusions. The encoded protein plays a critical role in cell migration, motility, adhesion and cellular interactions. Expression of this gene is known to be regulated by several microRNAs, and overexpression …
- **Diseases (Open Targets)**: ankylosing spondylitis (0.355); Alzheimer disease (0.179); hypothyroidism (0.164); neoplasm (0.118); breast cancer (0.116)
- **Europe PMC papers**: 4005
- **Why important**: FSCN1 is a central network connector linking ABRACL with ACAT2. It encodes an actin-bundling protein involved in cellular protrusions, migration, motility, adhesion, cell-cell interactions, polarity, lamellipodium assembly, and microspike assembly. HPA places it in the plasma membrane and cytosol and reports cell-type enhancement in extravillous trophoblasts and other epithelial or migratory-associated populations. It has extensive literature and disease associations including neoplasm and breast cancer.
- **Conclusion**: Established evidence supports FSCN1 as the strongest cytoskeletal and migration-related anchor of the module. Its central position and trophoblast-associated annotation make it a plausible marker of the shared cellular state. Direct regulation of the other module genes by FSCN1 remains a hypothesis.

#### ACAT2

- **Related proteins** (co-abundance neighbors): FSCN1 (0.85), CLIC4 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA acetyltransferase 2. The product of this gene is an enzyme involved in lipid metabolism, and it encodes cytosolic acetoacetyl-CoA thiolase. This gene shows complementary overlapping with the 3-prime region of the TCP1 gene in both mouse and human. These genes are encoded on opposite strands of DNA, as well as in opposite transcriptional orientation. Alternatively spliced transcript variants encoding different isoforms…
- **Diseases (Open Targets)**: intellectual developmental disorder with polymicrogyria and seizures (0.484); neurodegenerative disease (0.441); prostate carcinoma (0.223); acetyl-CoA acetyltransferase-2 deficiency (0.119); ZTTK syndrome (0.118)
- **Europe PMC papers**: 2623
- **Why important**: ACAT2 connects FSCN1 with CLIC4 and provides the clearest lipid-metabolism component. It encodes cytosolic acetoacetyl-CoA thiolase and is annotated in lipid and fatty-acid metabolism. HPA reports tissue enhancement in liver and cell-type enhancement in early spermatids, with protein detected in both placenta and testis. It also has substantial literature and disease associations including ACAT2 deficiency, neurodegenerative disease, and prostate carcinoma.
- **Conclusion**: Established evidence supports ACAT2 as a metabolic component potentially relevant to testicular germ-cell biology and tissue metabolic state. Its network placement is consistent with a possible connection between metabolism and cytoskeletal or membrane-related regulation, but that mechanistic connection is not established.

#### LDHB

- **Related proteins** (co-abundance neighbors): ABRACL (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lactate dehydrogenase B. This gene encodes the B subunit of lactate dehydrogenase enzyme, which catalyzes the interconversion of pyruvate and lactate with concomitant interconversion of NADH and NAD+ in a post-glycolysis process. Alternatively spliced transcript variants have been found for this gene. Recent studies have shown that a C-terminally extended isoform is produced by use of an alternative in-frame translation t…
- **Diseases (Open Targets)**: glycogen storage disease due to lactate dehydrogenase H-subunit deficiency (0.724); type 2 diabetes mellitus (0.271); adverse effect (0.184); neoplasm (0.117); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 5204
- **Why important**: LDHB is connected to the module through ABRACL and supplies a clear lactate-redox interpretation. It encodes the B subunit of lactate dehydrogenase and supports pyruvate-lactate interconversion and NAD metabolism. HPA reports tissue enhancement in heart muscle and kidney, cell-type enrichment in parietal cells, and protein detection in both tissues under study. LDHB also has extensive literature and disease associations including lactate dehydrogenase deficiency and type two diabetes mellitus.
- **Conclusion**: Established evidence supports LDHB as a metabolic and redox marker rather than a structural hub. Its presence is consistent with altered energy metabolism in the shared state, but the supplied network does not establish functional coupling between LDHB and ABRACL or the remaining genes.

#### CLIC4

- **Related proteins** (co-abundance neighbors): ACAT2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Centrosome; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CLIC family member 4. Chloride channels are a diverse group of proteins that regulate fundamental cellular processes including stabilization of cell membrane potential, transepithelial transport, maintenance of intracellular pH, and regulation of cell volume. Chloride intracellular channel 4 (CLIC4) protein, encoded by the CLIC4 gene, is a member of the p64 family; the gene is expressed in many tissues and exhibits a i…
- **Diseases (Open Targets)**: hypertensive disorder (0.352); Short stature (0.259); cardiovascular disorder (0.237); response to xenobiotic stimulus (0.233); exostosis (0.212)
- **Europe PMC papers**: 4070
- **Why important**: CLIC4 connects to ACAT2 and contributes membrane, polarity, differentiation, and cytoskeletal interpretations. HPA places it at the plasma membrane and centrosome and reports tissue enhancement in blood vessel and cell-type enhancement in extravillous trophoblasts, mesothelial cells, endometrial stromal cells, and plasma cells. It has substantial literature and disease associations including hypertensive and cardiovascular disorders.
- **Conclusion**: Established evidence supports CLIC4 as a regulator associated with cellular architecture, polarity, differentiation, and migration. Its trophoblast and vascular annotations make it relevant to placental remodeling and potentially to a shared tissue state. A direct interaction with ACAT2 or a role in the complete module mechanism remains hypothetical.

#### ABRACL

- **Related proteins** (co-abundance neighbors): LDHB (0.85), FSCN1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ABRA C-terminal like. Predicted to be involved in regulation of actin filament-based process. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: cardiovascular disorder (0.254); ovarian dysfunction (0.254); neurodegenerative disease (0.251); central nervous system cancer (0.078); glioma (0.078)
- **Europe PMC papers**: 186
- **Why important**: ABRACL occupies an intermediate position linking FSCN1 with LDHB and is the least extensively characterized member in the supplied evidence. It is predicted to regulate actin filament-based processes and is annotated to the nucleoplasm. HPA reports enhancement in extravillous trophoblasts and several epithelial cell types, with protein detected in both placenta and testis. Its literature volume is more limited than that of the other selected genes, while reported disease associations include cardiovascular, ovarian, neurodegenerative, and central nervous system disorders.
- **Conclusion**: Established evidence supports ABRACL as a possible actin-regulatory component with relevance to cell state, but its molecular function is less firmly characterized. Its intermediate network position makes it a candidate connector between cytoskeletal and metabolic signals; that connector role is a hypothesis requiring experimental validation.

## Module 1

**Tissue pair**: placenta and testis  
**Genes (5)**: ANXA6, CANX, EZR, NARS1, VPS35

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING enrichment. The gene annotations nevertheless suggest a broad cellular maintenance module rather than a narrowly defined pathway: CANX supports endoplasmic-reticulum protein folding and quality control; VPS35 supports endosomal-to-Golgi protein transport and lysosome organization; ANXA6 is involved in calcium-dependent membrane and phospholipid processes; EZR links the plasma membrane to the actin cytoskeleton; and NARS1 supports cytoplasmic translation through tRNA aminoacylation. The co-abundance pattern is therefore consistent with coordinated proteostasis, intracellular trafficking, membrane organization, and protein synthesis, but this functional interpretation remains annotation-based rather than enrichment-proven.

**Cell composition.** This is not a plasma-protein or secreted-protein module: none of the genes is annotated as secreted. All genes have low tissue specificity, and all are detected at the protein level in both placenta and testis. The module also has low immune-cell specificity, arguing against an obvious blood-cell signature. Cell-type evidence is mixed: CANX is enriched in late spermatids; ANXA6 and EZR show enhancement in several cell types including syncytiotrophoblasts; and other annotations include adipocytes, hepatic stellate cells, peritubular myoid cells, and rod photoreceptor cells. Thus the shared signal is more consistent with broadly expressed cellular machinery, potentially modulated by placental and testicular cell types, than with a tissue-exclusive or blood-derived module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship was detected among the module genes, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. The co-abundance edges therefore do not reproduce established physical interactions or a recognized multiprotein complex in these resources. This does not invalidate the module: co-abundance can reflect shared regulation, common cellular state, parallel trafficking demands, or indirect relationships. The strongest apparent network structure links CANX with ANXA6, NARS1, and VPS35, links ANXA6 with VPS35, and links NARS1 with EZR, but these relationships should be treated as module-level co-abundance associations rather than confirmed molecular binding.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact shared placenta-testis co-abundance module appears potentially novel because it is not represented by a matching high-confidence STRING interaction pattern or a multi-member hu.MAP complex, and no pathway database enrichment provides an established label. However, absence from STRING or hu.MAP alone cannot establish biological novelty. The individual functions of the genes are well established, and the module may represent a new tissue-pair-specific co-regulation pattern assembled from known cellular processes. Independent replication, comparison with additional tissue cohorts, and experimental testing would be needed to distinguish a reproducible biological module from a dataset-specific association.

**Hypothesis.** Hypothesis: in placenta and testis, a shared cellular state coordinates endoplasmic-reticulum quality control, endosomal recycling, calcium-sensitive membrane behavior, actin-linked surface organization, and translation. CANX could maintain folding quality, VPS35 could route membrane proteins, ANXA6 and EZR could organize membrane-cytoskeletal responses, and NARS1 could sustain protein synthesis during high membrane and protein-remodeling demand. The shared signal may therefore arise from convergent proteostasis and membrane-organization requirements in syncytiotrophoblasts and spermatogenic or related testicular cells, rather than from a single physical complex.

### Important genes

#### CANX

- **Related proteins** (co-abundance neighbors): ANXA6 (0.84), NARS1 (0.82), VPS35 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is the most connected gene in the module and links the membrane-associated ANXA6 and VPS35 branch with the NARS1 branch. Its established endoplasmic-reticulum chaperone role provides a direct mechanistic entry point for protein folding, glycoprotein quality control, secretion, and ER-associated degradation. It is detected in both tissues and is enriched in late spermatids. Its extensive literature and disease links make it a strong anchor for interpreting the module.
- **Conclusion**: Established evidence supports CANX as an endoplasmic-reticulum folding and quality-control factor with a central position in this module. It is plausible, but not demonstrated, that CANX helps couple protein-folding demand to the other co-abundant processes.

#### VPS35

- **Related proteins** (co-abundance neighbors): ANXA6 (0.90), CANX (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS35 retromer complex component. This gene belongs to a group of vacuolar protein sorting (VPS) genes. The encoded protein is a component of a large multimeric complex, termed the retromer complex, involved in retrograde transport of proteins from endosomes to the trans-Golgi network. The close structural similarity between the yeast and human proteins that make up this complex suggests a similarity in function. Expression studie…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.743); neurodegenerative disease (0.553); young-onset Parkinson disease (0.503); Parkinson disease (0.482); Parkinson disease, dominant (0.370)
- **Europe PMC papers**: 3611
- **Why important**: VPS35 occupies a central position alongside ANXA6 and CANX and is the core component of the retromer transport machinery. Its established roles in endosomal-to-Golgi retrograde transport, lysosome organization, and protein transport connect the module to intracellular cargo sorting. It has substantial literature and strong disease associations with Parkinson disease and neurodegeneration.
- **Conclusion**: Established evidence supports VPS35 as a protein-trafficking and endosomal-organization factor. Its co-abundance with CANX and ANXA6 is compatible with coordinated proteostasis and membrane trafficking, but the module does not establish a direct physical interaction or a tissue-specific VPS35 mechanism.

#### ANXA6

- **Related proteins** (co-abundance neighbors): VPS35 (0.90), CANX (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A6. Annexin VI belongs to a family of calcium-dependent membrane and phospholipid binding proteins. Several members of the annexin family have been implicated in membrane-related events along exocytotic and endocytotic pathways. The annexin VI gene is approximately 60 kbp long and contains 26 exons. It encodes a protein of about 68 kDa that consists of eight 68-amino acid repeats separated by linking …
- **Diseases (Open Targets)**: systemic lupus erythematosus (0.292); asthma (0.194); poisoning (0.193); stricture (0.193); neoplasm (0.115)
- **Europe PMC papers**: 1621
- **Why important**: ANXA6 forms a prominent connection with VPS35 and CANX and is annotated as a calcium-dependent membrane and phospholipid-binding protein. Its functions in calcium transport, mitochondrial calcium homeostasis, and membrane-related processes provide a possible bridge between trafficking and cellular signaling. HPA evidence places it in several cell types, including syncytiotrophoblasts and peritubular myoid cells, and it has substantial literature and disease associations.
- **Conclusion**: Established evidence supports ANXA6 as a membrane and calcium-regulatory protein. Its module position makes it a plausible coordinator of membrane dynamics between trafficking and folding systems, but that coordinating role remains a hypothesis.

#### EZR

- **Related proteins** (co-abundance neighbors): NARS1 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ezrin. The cytoplasmic peripheral membrane protein encoded by this gene functions as a protein-tyrosine kinase substrate in microvilli. As a member of the ERM protein family, this protein serves as an intermediate between the plasma membrane and the actin cytoskeleton. This protein plays a key role in cell surface structure adhesion, migration and organization, and it has been implicated in various human…
- **Diseases (Open Targets)**: hair color (0.477); non-small cell lung carcinoma (0.397); lung adenocarcinoma (0.382); autosomal recessive non-syndromic intellectual disability (0.370); glaucoma (0.347)
- **Europe PMC papers**: 4982
- **Why important**: EZR is the terminal member of the NARS1-linked branch and connects the module to the plasma membrane and actin cytoskeleton. Its established functions include cell-surface organization, adhesion, migration, and regulation of cell shape. It is enhanced in several epithelial or epithelial-like cell types, including syncytiotrophoblasts, and has the largest literature volume among the module genes.
- **Conclusion**: Established evidence supports EZR as a membrane–cytoskeleton linker involved in surface architecture and cell behavior. Its association with NARS1 may reflect shared cellular state or coordinated remodeling rather than a known direct complex, so a role in coupling translation to membrane organization is only a hypothesis.

#### NARS1

- **Related proteins** (co-abundance neighbors): EZR (0.88), CANX (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: asparaginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids.  Asparaginyl-tRNA synthetase is localized to the cytoplasm and belongs to the class II family of tRNA synthetases.  The N-terminal domain represents the signature sequence for the eukaryotic asparaginyl-tRNA synthetases. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, impaired language, and gait abnormalities (0.762); neurodevelopmental disorder with microcephaly, impaired language, epilepsy, and gait abnormalities (0.679); neurodevelopmental disorder (0.567); complex neurodevelopmental disorder (0.462); developmental disability (0.340)
- **Europe PMC papers**: 216
- **Why important**: NARS1 provides the module's clearest direct link to core protein synthesis through asparaginyl-tRNA aminoacylation. It connects to CANX and EZR in the co-abundance graph, potentially linking translational capacity with protein-folding and membrane-organization demands. Its disease associations include neurodevelopmental disorders, although its literature volume is smaller than that of the other selected genes.
- **Conclusion**: Established evidence supports NARS1 as a cytoplasmic translation factor. Its inclusion suggests that translational demand may accompany the module's trafficking and membrane processes, but any tissue-pair-specific coupling between translation and those processes remains unproven.

## Module 3

**Tissue pair**: placenta and testis  
**Genes (11)**: COL18A1, COTL1, DPYSL3, IGFBP7, NUCB1, PDLIM5, PEPD, PLS3, SPARC, TAGLN2, TKT

### Function

The module does not have a globally significant GO or KEGG enrichment term; no GO or KEGG term passed global correction. Its biological signal is therefore inferential rather than pathway-enrichment proof. The strongest interpretation is a mixed vascular and extracellular-matrix, cell-adhesion, cytoskeletal, and tissue-remodelling program, with an additional metabolic and immune-cell component. IGFBP7, SPARC, and COL18A1 support vascular biology, extracellular-matrix organization, angiogenesis-related regulation, and cell-shape changes. TAGLN2, PLS3, COTL1, DPYSL3, and PDLIM5 support actin organization, membrane or cytoskeletal structure, and cellular morphology. TKT and PEPD provide metabolic and collagen-related functions, while NUCB1 may connect the module to Golgi calcium regulation and signal transduction. The sparse network and the absence of a coherent GO, KEGG, or STRING functional-enrichment result argue against calling this a single established biochemical pathway.

**Cell composition.** This is a mixed-composition module rather than a uniformly secreted or housekeeping module. Several genes are secreted to blood or extracellular matrix, including NUCB1, IGFBP7, SPARC, and COL18A1, while the remaining genes are mainly intracellular or membrane-associated. HPA data show protein detection in both placenta and testis for most genes, but this does not establish that all genes originate from the same cell type. The cell-type annotations repeatedly point to pericytes, vascular smooth-muscle cells, extravillous trophoblasts, fibroblast-like stromal cells, and peritubular myoid cells, consistent with shared vascular, stromal, and contractile compartments. The module also has a substantial blood-associated signature involving neutrophils, monocytes, eosinophils, myeloid dendritic cells, platelets, and related immune or hematopoietic populations. TKT, PLS3, and COTL1 are particularly compatible with blood-cell or cytoskeletal contributions. Thus, shared stromal or vascular biology is plausible, but blood-cell content or blood-derived proteins could also contribute to the placenta-testis co-abundance pattern. The lack of uniform tissue specificity and the mixture of secreted, cytosolic, membrane, and nuclear proteins argue against interpreting the module as a pure tissue-specific program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship supplied for the module is the SPARC-COL18A1 pair. This is biologically concordant with extracellular-matrix and vascular remodelling, and it provides an independently supported anchor for that part of the interpretation. The other module edges are co-abundance relationships rather than established high-confidence physical interactions in the supplied STRING result. No hu.MAP complex contains multiple module members. Consequently, the module is not supported as a known multiprotein complex. Its structure is sparse and appears to contain a vascular or extracellular-matrix branch centered on SPARC and COL18A1, an IGFBP7-linked core connected to cytoskeletal genes, and smaller links involving metabolic or actin-associated proteins. The network therefore may reflect coordinated expression across related cell states or tissue compartments rather than direct physical binding among most members.

**STRING interactions (score >= 0.7)**: 1 of 55 gene pairs: COL18A1–SPARC (0.757)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should be considered a potentially new co-abundance association pattern, but not a demonstrated new molecular complex or pathway. The combination of genes is not independently validated as a coherent unit by the supplied STRING functional enrichment or hu.MAP evidence, and only the SPARC-COL18A1 relationship is already represented by the supplied interaction evidence. That supports novelty at the level of the observed placenta-testis co-abundance organization, especially if this exact module was not previously reported. However, absence from STRING or hu.MAP alone cannot establish novelty, because those resources emphasize curated or experimentally supported molecular relationships and may not capture tissue-specific co-expression. The novelty claim therefore requires replication in independent placenta and testis datasets, preservation of the module across cohorts, cell-type deconvolution, and testing against blood contamination and shared stromal or vascular composition.

**Hypothesis.** Hypothesis: the module reflects a shared perivascular and stromal remodelling state present in placenta and testis. In this model, IGFBP7, SPARC, and COL18A1 coordinate extracellular-matrix composition, cell adhesion, angiogenesis-related signalling, and tissue architecture; PLS3, TAGLN2, COTL1, DPYSL3, and PDLIM5 support actin-based cell shape, contractility, or membrane scaffolding; and TKT, PEPD, and NUCB1 provide metabolic, collagen-related, and calcium or secretory support. The same expression pattern could be generated by shared perivascular, smooth-muscle, fibroblast-like, trophoblast, or myoid populations, with an additional contribution from blood-associated cells or circulating proteins. This is a mechanistic model to test, not an established pathway assignment.

### Important genes

#### SPARC

- **Related proteins** (co-abundance neighbors): IGFBP7 (0.88), COL18A1 (0.84); STRING partners: COL18A1 (0.757)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: secreted protein acidic and cysteine rich. This gene encodes a cysteine-rich acidic matrix-associated protein. The encoded protein is required for the collagen in bone to become calcified but is also involved in extracellular matrix synthesis and promotion of changes to cell shape. The gene product has been associated with tumor suppression but has also been correlated with metastasis based on changes to cell shape which can promote tumor …
- **Diseases (Open Targets)**: osteogenesis imperfecta (0.707); neurodegenerative disease (0.443); hereditary disease (0.414); osteogenesis imperfecta type 4 (0.381); Abnormality of the skeletal system (0.358)
- **Europe PMC papers**: 17798
- **Why important**: SPARC is a central bridge between the IGFBP7-linked portion of the network and COL18A1, and it is the strongest extracellular-matrix anchor in the module. Its annotation supports matrix synthesis, cell-shape regulation, endothelial migration, and angiogenesis-related control. It is detected in both relevant tissues, is associated with stromal, trophoblast, and fibroblast-like cell types, and has extensive literature and disease annotation, including skeletal and connective-tissue disease.
- **Conclusion**: Established evidence supports SPARC as an extracellular-matrix and vascular-remodelling gene with strong relevance to the module. Its network position and the supported relationship with COL18A1 make it a leading candidate for the module's structural arm. The hypothesis that SPARC organizes the entire shared placenta-testis program remains unproven.

#### IGFBP7

- **Related proteins** (co-abundance neighbors): DPYSL3 (0.89), SPARC (0.88), NUCB1 (0.86), TAGLN2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor binding protein 7. This gene encodes a member of the insulin-like growth factor (IGF)-binding protein (IGFBP) family. IGFBPs bind IGFs with high affinity, and regulate IGF availability in body fluids and tissues and modulate IGF binding to its receptors. This protein binds IGF-I and IGF-II with relatively low affinity, and belongs to a subfamily of low-affinity IGFBPs. It also stimulates prostacyclin production and …
- **Diseases (Open Targets)**: familial retinal arterial macroaneurysm (0.607); schizophrenia (0.346); hyperemesis gravidarum (0.328); alcohol drinking (0.314); atrial fibrillation (0.314)
- **Europe PMC papers**: 4402
- **Why important**: IGFBP7 is among the most connected genes in the module and links DPYSL3, SPARC, NUCB1, and TAGLN2. It is tissue-enhanced in blood vessels, secreted to blood, associated with fibroblasts and hepatic stellate cells, and annotated for IGF regulation, angiogenesis, cell adhesion, implantation, and regulation of cell proliferation. It also has substantial literature and disease associations.
- **Conclusion**: Established evidence supports IGFBP7 as a vascular, extracellular, and growth-regulatory protein that plausibly explains the module's connection between matrix and cytoskeletal features. Its blood secretion and immune-cell association mean that circulating protein or sample composition could contribute to the signal. A direct coordinating role in this module is a hypothesis rather than demonstrated causation.

#### COL18A1

- **Related proteins** (co-abundance neighbors): SPARC (0.84); STRING partners: SPARC (0.757)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type XVIII alpha 1 chain. This gene encodes the alpha chain of type XVIII collagen. This collagen is one of the multiplexins, extracellular matrix proteins that contain multiple triple-helix domains (collagenous domains) interrupted by non-collagenous domains. A long isoform of the protein has an N-terminal domain that is homologous to the extracellular part of frizzled receptors. Proteolytic processing at several endogeno…
- **Diseases (Open Targets)**: Knobloch syndrome 1 (0.778); Knobloch syndrome (0.700); hereditary glaucoma, primary closed-angle (0.593); Dupuytren Contracture (0.587); severe early-childhood-onset retinal dystrophy (0.501)
- **Europe PMC papers**: 5223
- **Why important**: COL18A1 is the module's extracellular-matrix collagen and is directly connected to SPARC in the supplied high-confidence STRING evidence. It is enhanced in blood vessel and liver, is secreted to extracellular matrix, and can produce endostatin through proteolytic processing. Its established functions include angiogenesis-related regulation and endothelial morphogenesis, and it has strong disease associations involving Knobloch syndrome and ocular disease.
- **Conclusion**: Established evidence supports COL18A1 as an extracellular-matrix and vascular-architecture component, and its supported relationship with SPARC gives the module a credible matrix-remodelling core. The module data do not demonstrate that COL18A1-derived products drive co-abundance in either tissue, so that mechanistic interpretation remains a hypothesis.

#### PLS3

- **Related proteins** (co-abundance neighbors): NUCB1 (0.86), TKT (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cytosol; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plastin 3. Plastins are a family of actin-binding proteins that are conserved throughout eukaryote evolution and expressed in most tissues of higher eukaryotes. In humans, two ubiquitous plastin isoforms (L and T) have been identified. Plastin 1 (otherwise known as Fimbrin) is a third distinct plastin isoform which is specifically expressed at high levels in the small intestine. The L isoform is expressed on…
- **Diseases (Open Targets)**: X-linked osteoporosis with fractures (0.727); congenital diaphragmatic hernia (0.553); osteoporosis (0.477); hernia, anterior diaphragmatic (0.380); postmenopausal osteoporosis (0.341)
- **Europe PMC papers**: 1365
- **Why important**: PLS3 connects NUCB1 to TKT and provides a cytoskeletal counterpart to the extracellular-matrix genes. It encodes an actin-binding plastin, is enhanced in blood vessels, is detected in both tissues, and is annotated for actin-bundle and actin-network formation. Its associations with osteoporosis and fracture-related disorders give it functional disease relevance, while its literature base is substantial.
- **Conclusion**: Established evidence supports PLS3 as an actin-architecture gene that could translate extracellular or vascular cues into cell shape and mechanical behaviour. Its association with vascular and epithelial cell types supports a structural interpretation, but the module does not establish whether PLS3 reflects stromal cells, epithelial cells, blood-associated cells, or a shared response.

#### TKT

- **Related proteins** (co-abundance neighbors): PEPD (0.84), PLS3 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transketolase. This gene encodes a thiamine-dependent enzyme which plays a role in the channeling of excess sugar phosphates to glycolysis in the pentose phosphate pathway. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: transketolase deficiency (0.663); neurodegenerative disease (0.409); cardiomyopathy (0.382); alcohol drinking (0.261); urolithiasis (0.259)
- **Europe PMC papers**: 3981
- **Why important**: TKT links PLS3 with PEPD and is the clearest metabolic component of the module. It is enhanced in bone marrow, associated with multiple myeloid populations, detected in both tissues, and has an established role in the non-oxidative pentose-phosphate pathway. Its literature and disease annotations include transketolase deficiency and cardiomyopathy.
- **Conclusion**: Established evidence supports TKT as a metabolic and potentially blood-cell-associated contributor rather than as a specific extracellular-matrix factor. Its position may indicate metabolic support for proliferating, activated, or remodelling cells, but it may also reflect cell-type composition. A direct metabolic role in the proposed vascular-stromal mechanism is therefore a testable hypothesis.

## Module 4

**Tissue pair**: placenta and testis  
**Genes (6)**: CSRP1, FLNA, FLNB, FLNC, LGALS1, MAP1B

### Function

This is most consistent with a cytoskeletal and cell-adhesion module centered on actin organization, membrane anchoring, cellular shape, and migration. The strongest functional clue is the tightly connected filamin core formed by FLNA, FLNB, and FLNC, supported by the supplementary STRING domain enrichments (5 supplementary STRING terms; within-query FDR 0.0107–0.0446). CSRP1 adds a LIM-domain regulatory and muscle-development component, while MAP1B links the module to microtubule organization. LGALS1 may connect the structural program with cell–matrix signaling and regulation of cell survival. No GO/KEGG term passed global correction, so the proposed function is based on gene annotations, network structure, HPA patterns, and supplementary STRING evidence rather than globally significant pathway enrichment.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only LGALS1 is annotated as secreted to blood, and the other proteins are intracellular or membrane-associated. It is also not blood-cell enriched; the genes have low immune-cell specificity or are not detected in immune cells, and no enriched blood-cell category is reported. HPA instead points toward vascular, smooth-muscle, stromal, trophoblast, and muscle-associated biology. The shared placenta–testis signal may therefore reflect common stromal, vascular, smooth-muscle, or contractile cell populations, rather than a placenta–testis-specific secreted program. The broad detection of most proteins in both tissues supports biological presence, although the lack of FLNC detection in these tissue protein assays cautions against assuming uniform contribution from every gene.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a well-supported internal filamin relationship: FLNA, FLNB, and FLNC are mutually connected and collectively account for the supplementary filamin-domain signals (5 supplementary STRING terms; within-query FDR 0.0107–0.0446). This is established prior knowledge and strongly supports a real structural submodule rather than an arbitrary co-abundance pattern. The remaining relationships involving CSRP1, LGALS1, and MAP1B are present in the co-abundance network but are not listed as high-confidence STRING interactions, so they should be interpreted as module-level associations rather than established direct physical binding. No hu.MAP complex contains at least two module members. Thus, the module has a known filamin-centered interaction core but no independently supported hu.MAP complex spanning the full module.

**STRING interactions (score >= 0.7)**: 3 of 15 gene pairs: FLNA–FLNB (0.979); FLNA–FLNC (0.907); FLNB–FLNC (0.921)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Filamin-type immunoglobulin domains (FDR = 0.0107, 3 genes); InterPro Filamin/ABP280 repeat (FDR = 0.0439, 3 genes); InterPro Filamin/ABP280 repeat-like (FDR = 0.0439, 3 genes); InterPro Filamin family (FDR = 0.0439, 3 genes); InterPro Immunoglobulin E-set (FDR = 0.0446, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The filamin component is not novel in a molecular-interaction sense because the FLNA–FLNB–FLNC relationships and their shared repeat architecture are already represented in STRING. The broader co-abundance association with CSRP1, LGALS1, and MAP1B may nevertheless be a new tissue-pair observation, especially because it is not represented by a hu.MAP complex. However, absence from hu.MAP or absence of listed STRING partners does not establish novelty. The defensible conclusion is that this is a potentially novel placenta–testis co-abundance context built around a known filamin cytoskeletal core, not a newly discovered protein complex or pathway.

**Hypothesis.** Mechanistic hypothesis: a shared vascular, stromal, smooth-muscle, or trophoblast-associated cell program in placenta and testis increases coordinated expression of filamin proteins together with CSRP1, LGALS1, and MAP1B. The filamins could organize cortical actin and membrane receptors, CSRP1 could support contractile or differentiation-related regulation, MAP1B could coordinate microtubule architecture, and LGALS1 could modulate cell–matrix interactions and survival signaling. This hypothesis predicts that the module will be strongest in cells undergoing adhesion, migration, remodeling, or contractile differentiation. It remains a hypothesis because there is no globally significant GO/KEGG enrichment and no hu.MAP complex linking all module members.

### Important genes

#### FLNA

- **Related proteins** (co-abundance neighbors): CSRP1 (0.93), LGALS1 (0.88), FLNC (0.87), FLNB (0.83); STRING partners: FLNB (0.979), FLNC (0.907)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is the leading network hub, connecting the filamin core with CSRP1 and LGALS1. Its established function as an actin crosslinker and linker between actin, membrane glycoproteins, integrins, and receptor complexes gives it a plausible organizing role. It has extensive literature, strong disease associations including periventricular nodular heterotopia and skeletal-development syndromes, and supplementary STRING support through all filamin-domain terms (5 supplementary STRING terms; within-query FDR 0.0107–0.0446).
- **Conclusion**: Established evidence supports FLNA as a central actin–membrane scaffold and the principal structural organizer of this module. It is reasonable, but not proven, to hypothesize that FLNA coordinates the module's tissue-remodeling signal.

#### FLNC

- **Related proteins** (co-abundance neighbors): FLNA (0.87), FLNB (0.80); STRING partners: FLNA (0.907), FLNB (0.921)
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin C. This gene encodes one of three related filamin genes, specifically gamma filamin. These filamin proteins crosslink actin filaments into orthogonal networks in cortical cytoplasm and participate in the anchoring of membrane proteins for the actin cytoskeleton. Three functional domains exist in filamin: an N-terminal filamentous actin-binding domain, a C-terminal self-association domain, and a membr…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy 26 (0.833); myofibrillar myopathy 5 (0.791); distal myopathy with posterior leg and anterior hand involvement (0.742); dilated cardiomyopathy (0.714); familial restrictive cardiomyopathy (0.660)
- **Europe PMC papers**: 3861
- **Why important**: FLNC is part of the mutually connected filamin triad and is associated with muscle tissue, cardiomyocytes, myonuclei, and smooth-muscle cells in HPA. Its annotated roles in actin-cytoskeleton and sarcomere organization, together with strong cardiomyopathy and myopathy associations, make it especially informative for a contractile or muscle-related interpretation. It also contributes to every supplementary filamin-domain signal (5 supplementary STRING terms; within-query FDR 0.0107–0.0446).
- **Conclusion**: Established evidence supports FLNC as a muscle- and sarcomere-associated actin scaffold within the known filamin core. Its absence from the placenta and testis protein detection in the fact sheet means that its co-abundance signal should be treated cautiously and may reflect a specific cell population or transcript-level regulation.

#### FLNB

- **Related proteins** (co-abundance neighbors): FLNA (0.83), FLNC (0.80); STRING partners: FLNA (0.979), FLNC (0.921)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin B. This gene encodes a member of the filamin family. The encoded protein interacts with glycoprotein Ib alpha as part of the process to repair vascular injuries. The platelet glycoprotein Ib complex includes glycoprotein Ib alpha, and it binds the actin cytoskeleton. Mutations in this gene have been found in several conditions: atelosteogenesis type 1 and type 3; boomerang dysplasia; autosomal domina…
- **Diseases (Open Targets)**: Larsen syndrome (0.829); spondylocarpotarsal synostosis syndrome (0.775); atelosteogenesis type I (0.763); atelosteogenesis type III (0.756); Boomerang dysplasia (0.723)
- **Europe PMC papers**: 2274
- **Why important**: FLNB completes the strongly supported filamin triad and is connected to FLNA and FLNC in STRING. Its functions include actin-cytoskeleton organization and interaction with the platelet glycoprotein Ib complex, linking cytoskeletal architecture with vascular injury responses. HPA also associates it with extravillous trophoblasts, making it particularly relevant to the placenta side of the shared module. Its skeletal dysplasia associations provide substantial biological and disease context.
- **Conclusion**: Established evidence supports FLNB as a membrane-associated actin scaffold with vascular and developmental relevance. Its trophoblast association makes it a plausible contributor to the shared tissue signal, but a direct placenta–testis mechanism is not established.

#### CSRP1

- **Related proteins** (co-abundance neighbors): FLNA (0.93), LGALS1 (0.86), MAP1B (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cysteine and glycine rich protein 1. This gene encodes a member of the cysteine-rich protein (CSRP) family. This gene family includes a group of LIM domain proteins, which may be involved in regulatory processes important for development and cellular differentiation. The LIM/double zinc-finger motif found in this gene product occurs in proteins with critical functions in gene regulation, cell growth, and somatic differentiation. Alte…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy (0.272); placenta praevia (0.160); Varicose veins (0.113); acute myeloid leukemia (0.091); hepatocellular carcinoma (0.084)
- **Europe PMC papers**: 822
- **Why important**: CSRP1 has a prominent position among the non-filamin genes, connecting to FLNA, LGALS1, and MAP1B. Its LIM-domain architecture and annotations for sarcomere organization, muscle development, and platelet aggregation fit a structural and contractile interpretation. HPA links it to blood vessels, decidual stromal cells, extravillous trophoblasts, hepatic stellate cells, and myoepithelial or megakaryocyte populations. Its disease associations include hypertrophic cardiomyopathy and placenta praevia.
- **Conclusion**: Established evidence supports CSRP1 as a differentiation- and contractility-associated regulatory component. Its placement between the filamin-centered and non-filamin portions of the network suggests a bridging role, but direct molecular bridging has not been demonstrated here.

#### LGALS1

- **Related proteins** (co-abundance neighbors): FLNA (0.88), CSRP1 (0.86), MAP1B (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galectin 1. The galectins are a family of beta-galactoside-binding proteins implicated in modulating cell-cell and cell-matrix interactions. This gene product may act as an autocrine negative growth factor that regulates cell proliferation. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: glaucoma (0.349); open-angle glaucoma (0.343); chronic kidney disease (0.330); smoking initiation (0.162); melanoma (0.121)
- **Europe PMC papers**: 4025
- **Why important**: LGALS1 is a highly connected non-filamin member linked to FLNA, CSRP1, and MAP1B. As a secreted-to-blood galectin involved in cell–cell and cell–matrix interactions and apoptotic regulation, it provides a signaling and extracellular-interface dimension to an otherwise cytoskeletal module. HPA associates it with decidual stromal cells, endometrial stromal cells, extravillous trophoblasts, and fibroblasts, which is relevant to tissue remodeling in placenta and potentially testis.
- **Conclusion**: Established evidence supports LGALS1 as a cell–matrix and survival-signaling factor that could accompany stromal remodeling. Its role as a direct coordinator of the filamin network is hypothetical because no listed STRING interaction or hu.MAP complex connects it to the other module members.

## Module 5

**Tissue pair**: placenta and testis  
**Genes (6)**: DPP3, DPYSL2, GBE1, LTA4H, SARS1, TARS1

### Function

No GO/KEGG term passed global correction, and STRING supplied no functional enrichment. Therefore, the module does not support assignment to a single significantly enriched canonical pathway. Its genes represent a functionally mixed set of cytosolic proteins: LTA4H and DPP3 contribute peptide or inflammatory-lipid processing, GBE1 contributes glycogen branching, TARS1 and SARS1 contribute aminoacyl-tRNA charging, and DPYSL2 contributes cytoskeletal and neuronal signaling functions. The network may reflect coordinated abundance of broadly expressed intracellular proteins or shared cellular context rather than one unified biochemical process.

**Cell composition.** All module proteins were detected in both placenta and testis, and none is secreted. This argues against a module dominated by plasma or secreted proteins. Most genes have low tissue specificity and low immune-cell specificity, consistent with broadly expressed intracellular proteins rather than a placenta- or testis-exclusive program. GBE1 is tissue enhanced in skeletal muscle and DPYSL2 in brain. Several genes show enhancement in neutrophil-related cell types, and DPYSL2 is enriched in several myeloid cell categories. However, the module is not predominantly blood-cell enriched, so HPA does not establish that the shared signal is caused by blood contamination or a common infiltrating cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship supplied is SARS1–TARS1. This is consistent with a known connection between two class-II aminoacyl-tRNA synthetases. The other module relationships are not supported by high-confidence STRING partners in the supplied evidence. No hu.MAP complex contains multiple module members. Thus, the broader co-abundance structure is only partly supported by known molecular interaction evidence and may reflect indirect biology, correlated expression, shared cellular context, or previously unrecognized relationships rather than one physical complex.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: SARS1–TARS1 (0.915)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The evidence does not establish a new molecular complex or pathway. The absence of globally significant GO/KEGG enrichment, STRING functional enrichment, and a multi-member hu.MAP complex limits claims of mechanistic novelty. Nevertheless, absence from STRING or hu.MAP does not prove that the co-abundance pattern is not novel, because those resources are incomplete and co-abundance relationships can be indirect. The placenta–testis co-abundance pattern is therefore a potentially novel systems-level observation, but it requires replication, tissue deconvolution, and experimental testing before being considered a new biological mechanism.

**Hypothesis.** Hypothesis: the module reflects a coordinated cytosolic biosynthetic, metabolic, and stress-related state shared by particular cell populations in placenta and testis. Aminoacyl-tRNA synthetases may support translational demand, while glycogen handling, peptide processing, inflammatory-lipid metabolism, and cytoskeletal organization respond to the same cellular state. SARS1–TARS1 provides the clearest known molecular anchor. The coordination of these activities across the full module is not established, and cell-composition effects, especially contributions from myeloid-like or other specialized cells, remain an alternative explanation.

### Important genes

#### LTA4H

- **Related proteins** (co-abundance neighbors): GBE1 (0.94), TARS1 (0.88), DPYSL2 (0.82), SARS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: leukotriene A4 hydrolase. The protein encoded by this gene is an enzyme that contains both hydrolase and aminopeptidase activities. The hydrolase activity is used in the final step of the biosynthesis of leukotriene B4, a proinflammatory mediator. The aminopeptidase activity has been shown to degrade proline-glycine-proline (PGP), a neutrophil chemoattractant and biomarker for chronic obstructive pulmonary disease (COPD). …
- **Diseases (Open Targets)**: hypotensive disorder (0.198); small intestine neuroendocrine neoplasm (0.150); cystic fibrosis (0.104); COVID-19 (0.096); hepatocellular carcinoma (0.086)
- **Europe PMC papers**: 1823
- **Why important**: LTA4H is the most connected gene in the module and links GBE1, TARS1, DPYSL2, and SARS1. It has established leukotriene A hydrolase and aminopeptidase activities, including participation in leukotriene B synthesis and degradation of a neutrophil chemoattractant. Its HPA profile is broadly expressed but includes monocyte and neutrophil-progenitor enhancement. It also has extensive literature and several disease associations.
- **Conclusion**: Established evidence supports LTA4H as a central network connector with inflammatory-lipid and peptide-processing functions. It is a plausible module anchor, but the module does not establish that leukotriene biology is the shared placenta–testis mechanism.

#### GBE1

- **Related proteins** (co-abundance neighbors): LTA4H (0.94), TARS1 (0.88), DPP3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 1,4-alpha-glucan branching enzyme 1. The protein encoded by this gene is a glycogen branching enzyme that catalyzes the transfer of alpha-1,4-linked glucosyl units from the outer end of a glycogen chain to an alpha-1,6 position on the same or a neighboring glycogen chain. Branching of the chains is essential to increase the solubility of the glycogen molecule and, consequently, in reducing the osmotic pressure within cells. Highest l…
- **Diseases (Open Targets)**: glycogen storage disease due to glycogen branching enzyme deficiency (0.848); adult polyglucosan body disease (0.801); glycogen storage disease due to glycogen branching enzyme deficiency, adult neuromuscular form (0.711); glycogen storage disease due to glycogen branching enzyme deficiency, congenital neuromuscular form (0.591); disorder of glycogen metabolism (0.573)
- **Europe PMC papers**: 1361
- **Why important**: GBE1 is strongly connected to LTA4H, TARS1, and DPP3 and is the clearest glycogen-metabolism component. Its enzyme activity is required for glycogen branching, and its highest expression is associated with liver and muscle biology. HPA identifies skeletal-muscle enhancement and enhancement in metabolically active muscle and cardiac cell types. Its disease associations include glycogen-branching enzyme deficiency and related glycogen-storage disorders.
- **Conclusion**: Established evidence supports GBE1 as a metabolic component and an important bridge between metabolic and peptide-processing members. A shared glycogen-related program in placenta and testis remains a hypothesis because no GO/KEGG term passed global correction.

#### TARS1

- **Related proteins** (co-abundance neighbors): GBE1 (0.88), LTA4H (0.88), DPYSL2 (0.80); STRING partners: SARS1 (0.915)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: threonyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Threonyl-tRNA synthetase belongs to the class-II aminoacyl-tRNA synthetase family [provided by RefSeq, Jul 2008]…
- **Diseases (Open Targets)**: trichothiodystrophy 7, nonphotosensitive (0.520); trichothiodystrophy (0.430); actinic keratosis (0.356); dyshidrosis (0.315); placental abruption (0.307)
- **Europe PMC papers**: 147
- **Why important**: TARS1 is a highly connected internal node and forms the module's only high-confidence STRING-supported pair with SARS1. It performs threonyl-tRNA aminoacylation, an established core translation function. Its low tissue and cell-type specificity is compatible with a broadly required cytosolic role. Its disease associations include trichothiodystrophy-related conditions and placental abruption.
- **Conclusion**: Established evidence supports TARS1 as a general protein-synthesis component and as one half of the module's only externally supported interaction pair. Its role in coordinating the entire module is hypothetical.

#### DPYSL2

- **Related proteins** (co-abundance neighbors): LTA4H (0.82), TARS1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Microtubules, Cytosol; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dihydropyrimidinase like 2. This gene encodes a member of the collapsin response mediator protein family. Collapsin response mediator proteins form homo- and hetero-tetramers and facilitate neuron guidance, growth and polarity. The encoded protein promotes microtubule assembly and is required for Sema3A-mediated growth cone collapse, and also plays a role in synaptic signaling through interactions with calcium channels. This…
- **Diseases (Open Targets)**: hypertensive disorder (0.431); autosomal dominant non-syndromic intellectual disability (0.370); cardiovascular disorder (0.297); ovarian neoplasm (0.292); glomerulonephritis (0.269)
- **Europe PMC papers**: 1328
- **Why important**: DPYSL2 connects LTA4H and TARS1 and provides the clearest cytoskeletal and signaling interpretation. It belongs to the collapsin-response-mediator-protein family, promotes microtubule assembly, participates in semaphorin-mediated growth-cone responses, and contributes to synaptic signaling. HPA shows brain tissue enhancement and enrichment across neuronal, retinal, Kupffer-cell, and several myeloid categories. It is implicated in neurological and cardiovascular disorders and has substantial literature.
- **Conclusion**: Established evidence supports DPYSL2 as a cytoskeletal and signaling protein with strong cell-context dependence. Its presence may indicate specialized cellular composition or cellular remodeling rather than a direct metabolic pathway, and its connection to the other module functions is not experimentally established.

#### SARS1

- **Related proteins** (co-abundance neighbors): LTA4H (0.81); STRING partners: TARS1 (0.915)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: seryl-tRNA synthetase 1. This gene belongs to the class II amino-acyl tRNA family. The encoded enzyme catalyzes the transfer of L-serine to tRNA (Ser) and is related to bacterial and yeast counterparts. Multiple alternatively spliced transcript variants have been described but the biological validity of all variants is unknown. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, ataxia, and seizures (0.670); autosomal recessive non-syndromic intellectual disability (0.370); autosomal recessive primary microcephaly (0.370); arteriovenous malformations of the brain (0.340); hereditary peripheral neuropathy (0.118)
- **Europe PMC papers**: 400
- **Why important**: SARS1 is the direct STRING-linked partner of TARS1 and supplies the clearest known interaction evidence in the module. It catalyzes seryl-tRNA formation and is associated with cytoplasmic translation, tRNA modification, and selenocysteine incorporation. It is broadly expressed, cytosolic, and associated with neurodevelopmental and microcephaly-related disorders.
- **Conclusion**: Established evidence supports SARS1 as a translation-related enzyme and as a known interaction partner of TARS1. The pair may mark translational demand, but there is no evidence that SARS1 directly connects aminoacylation machinery to the other module functions.

## Module 6

**Tissue pair**: placenta and testis  
**Genes (13)**: EEA1, HNRNPK, IMPDH2, IQGAP1, PLEC, RRBP1, RTN4, SEPTIN2, SEPTIN9, SPTBN1, SPTAN1, TLN1, TXNDC5

### Function

The strongest primary evidence supports a cytoskeletal cell-division module. Both globally corrected terms, (GO:BP cytokinesis; q_global = 0.0348) cytokinesis and (GO:BP cytoskeleton-dependent cytokinesis; q_global = 0.0348) cytoskeleton-dependent cytokinesis, identify IQGAP1, PLEC, SEPTIN2, SEPTIN9, and SPTBN1. These genes connect cytokinesis with actin organization, membrane-associated scaffolding, septin structures, and cell-shape control. The network also contains TLN1, SPTAN1, and EEA1, supporting links to adhesion, spectrin-based membrane organization, and vesicle trafficking. TXNDC5, RRBP1, and RTN4 provide an endoplasmic reticulum and protein-folding component, while IMPDH2 and HNRNPK may represent metabolic and RNA-processing connections rather than the central module function. No STRING functional enrichment was reported. Overall, the most defensible interpretation is a conserved cytoskeleton-linked cytokinesis and membrane-organization program.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the HPA summary reports only one secretome-annotated gene, TXNDC5, and the proteins are mainly intracellular, cytoskeletal, endoplasmic-reticulum, vesicular, or nuclear proteins. Most genes have low tissue specificity, which is consistent with a broadly used cellular machinery rather than a placenta- or testis-exclusive program. Protein detection is widespread in both tissues. Several genes show cell-type enrichment, including neutrophils, urothelial cells, endothelial or vascular-related populations, adipocyte-lineage cells, Leydig cells, and epithelial populations. Some immune-cell associations are present, but the overall HPA profile has low immune-cell specificity and does not strongly support a blood-cell-driven module. A contribution from shared stromal, vascular, epithelial, or other common cell populations remains possible and should be considered when interpreting tissue-level co-abundance.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP cytokinesis | 0.0348 | IQGAP1, PLEC, SEPTIN2, SEPTIN9, SPTBN1 |
| GO:BP cytoskeleton-dependent cytokinesis | 0.0348 | IQGAP1, PLEC, SEPTIN2, SEPTIN9, SPTBN1 |

### STRING and hu.MAP

The strongest known STRING relationships are the SEPTIN2–SEPTIN9 pair, the SPTAN1–SPTBN1 spectrin pair, IQGAP1–TLN1, IQGAP1–SPTAN1, PLEC–SPTAN1, and PLEC–TLN1. These relationships support an established cytoskeletal and membrane-scaffold backbone rather than an arbitrary set of correlated genes. hu.MAP independently places SPTBN1 with SPTAN1 in several spectrin-associated complexes (hu.MAP huMAP3_07940.1), (hu.MAP huMAP3_05473.1), and (hu.MAP huMAP3_09165.1), and places SEPTIN2 with SEPTIN9 in a septin complex (hu.MAP huMAP3_02362.1). The complexes include additional spectrin, actin-regulatory, adhesion, signaling, and membrane-associated proteins not present in the module. Thus, the network recovers known molecular substructures while also linking them through co-abundance. STRING provided no functional-enrichment term, so the interaction evidence should support, but not replace, the globally corrected GO evidence.

**STRING interactions (score >= 0.7)**: 6 of 78 gene pairs: IQGAP1–SPTAN1 (0.753); IQGAP1–TLN1 (0.893); PLEC–SPTAN1 (0.795); PLEC–TLN1 (0.706); SEPTIN2–SEPTIN9 (0.997); SPTAN1–SPTBN1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07940.1 (SPTBN1, SPTAN1; 2/5); huMAP3_05473.1 (SPTBN1, SPTAN1; 2/7); huMAP3_02362.1 (SEPTIN2, SEPTIN9; 2/14); huMAP3_09165.1 (SPTBN1, SPTAN1; 2/39)

### Novelty

The biological components are not novel individually: septin, spectrin, plectin, talin, and IQGAP1 relationships are already represented in STRING, and spectrin and septin associations are represented in hu.MAP. The likely novelty is therefore at the level of a conserved placenta–testis co-abundance module that integrates cytokinesis, cytoskeletal scaffolding, adhesion, vesicle or endoplasmic-reticulum organization, and nucleotide or RNA-related genes. This is a plausible new systems-level observation, but it should not be called a newly discovered molecular complex. The evidence supports novelty of the tissue-pair co-abundance context rather than novelty of the individual interactions. Lack of STRING or hu.MAP annotation for some genes is not, by itself, evidence of novelty.

**Hypothesis.** Hypothesis: in both placenta and testis, a shared population of proliferating or structurally active cells coordinates cytokinesis with remodeling of the actin, septin, spectrin, and intermediate-filament cytoskeleton. IQGAP1 and TLN1 may connect membrane adhesion and signaling to the cytoskeletal machinery; SEPTIN2 and SEPTIN9 may organize division-associated filaments; SPTAN1 and SPTBN1 may stabilize the membrane-associated scaffold; and PLEC may couple this scaffold to intermediate filaments. The ER and vesicle-associated genes could reflect the membrane and protein-trafficking demands of these cells. TXNDC5, RRBP1, and RTN4 may indicate an associated secretory or ER-stress context, but that interpretation is provisional because they were not included in the primary enriched terms. This hypothesis requires validation with cell-resolved expression, proliferation markers, and protein-level or perturbation experiments.

### Important genes

#### SEPTIN9

- **Related proteins** (co-abundance neighbors): SEPTIN2 (0.93), TXNDC5 (0.91), TLN1 (0.85), IQGAP1 (0.83), RTN4 (0.83); STRING partners: SEPTIN2 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in placenta, testis
- **hu.MAP 3.0**: huMAP3_02362.1
- **Function (MyGene.info)**: septin 9. This gene is a member of the septin family involved in cytokinesis and cell cycle control. This gene is a candidate for the ovarian tumor suppressor gene. Mutations in this gene cause hereditary neuralgic amyotrophy, also known as neuritis with brachial predilection. A chromosomal translocation involving this gene on chromosome 17 and the MLL gene on chromosome 11 results in acute myelomonocytic l…
- **Diseases (Open Targets)**: neuralgic amyotrophy (0.564); hypertensive disorder (0.496); cataract (0.437); essential hypertension (0.426); alcohol drinking (0.420)
- **Europe PMC papers**: 748
- **Why important**: SEPTIN9 has the strongest network position in the module and connects to SEPTIN2, TXNDC5, TLN1, IQGAP1, and RTN4. It belongs to both primary cytokinesis terms (GO:BP cytokinesis; q_global = 0.0348) and (GO:BP cytoskeleton-dependent cytokinesis; q_global = 0.0348), is part of the hu.MAP septin complex (hu.MAP huMAP3_02362.1), and forms a very strong known STRING relationship with SEPTIN2. Its established role in cytokinesis and cell-cycle control makes it a central candidate for the module's division-related component. It also has substantial literature and disease links involving neuralgic amyotrophy and leukemia-associated rearrangement.
- **Conclusion**: Established evidence supports SEPTIN9 as a core cytokinesis and septin-organization gene in this module. It is reasonable to hypothesize that its co-abundance reflects division-associated cytoskeletal remodeling in shared placental and testicular cell populations, but the tissue-specific mechanism is not established.

#### SPTBN1

- **Related proteins** (co-abundance neighbors): SPTAN1 (0.91), TLN1 (0.90), PLEC (0.88), EEA1 (0.82); STRING partners: SPTAN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta, testis
- **hu.MAP 3.0**: huMAP3_07940.1, huMAP3_05473.1, huMAP3_09165.1
- **Function (MyGene.info)**: spectrin beta, non-erythrocytic 1. Spectrin is an actin crosslinking and molecular scaffold protein that links the plasma membrane to the actin cytoskeleton, and functions in the determination of cell shape, arrangement of transmembrane proteins, and organization of organelles. It is composed of two antiparallel dimers of alpha- and beta- subunits. This gene is one member of a family of beta-spectrin genes. The encoded protein cont…
- **Diseases (Open Targets)**: developmental delay, impaired speech, and behavioral abnormalities (0.802); cancer (0.597); hereditary disease (0.516); hearing loss disorder (0.459); neurodevelopmental disorder (0.453)
- **Europe PMC papers**: 1635
- **Why important**: SPTBN1 is a highly connected bridge between SPTAN1, TLN1, PLEC, and EEA1. It belongs to both primary cytokinesis terms (GO:BP cytokinesis; q_global = 0.0348) and (GO:BP cytoskeleton-dependent cytokinesis; q_global = 0.0348), participates with SPTAN1 in several hu.MAP complexes (hu.MAP huMAP3_07940.1), (hu.MAP huMAP3_05473.1), and (hu.MAP huMAP3_09165.1), and has an exceptionally strong known STRING relationship with SPTAN1. Its spectrin function directly links actin, membrane organization, organelle arrangement, and cell shape. It has extensive literature and disease associations involving developmental and neurodevelopmental phenotypes.
- **Conclusion**: Established evidence identifies SPTBN1 as a structural scaffold and a key bridge between the module's cytokinesis and membrane-organization components. A role in coordinating division with membrane stability is a supported hypothesis, not a demonstrated mechanism in these tissues.

#### IQGAP1

- **Related proteins** (co-abundance neighbors): TLN1 (0.93), SEPTIN9 (0.83); STRING partners: SPTAN1 (0.753), TLN1 (0.893)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IQ motif containing GTPase activating protein 1. This gene encodes a member of the IQGAP family. The protein contains four IQ domains, one calponin homology domain, one Ras-GAP domain and one WW domain. It interacts with components of the cytoskeleton, with cell adhesion molecules, and with several signaling molecules to regulate cell morphology and motility. Expression of the protein is upregulated by gene amplification in two gastric cancer ce…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.515); Costello syndrome (0.503); allergic rhinitis (0.474)
- **Europe PMC papers**: 3787
- **Why important**: IQGAP1 links TLN1 and SEPTIN9 in the module and has known STRING relationships with TLN1 and SPTAN1. It is included in both primary cytokinesis terms (GO:BP cytokinesis; q_global = 0.0348) and (GO:BP cytoskeleton-dependent cytokinesis; q_global = 0.0348), is localized to the plasma membrane and cell junctions, and is known to interact with cytoskeletal, adhesion, and signaling proteins. Its literature is extensive, with disease associations including cancer and RAS-pathway-related syndromes.
- **Conclusion**: Established evidence supports IQGAP1 as a membrane-proximal organizer connecting signaling, adhesion, and cytokinetic cytoskeletal remodeling. It is a strong candidate for regulating the interface between cell shape and division in the module, although the specific shared placenta–testis process remains hypothetical.

#### TLN1

- **Related proteins** (co-abundance neighbors): IQGAP1 (0.93), SPTBN1 (0.90), SEPTIN9 (0.85), RRBP1 (0.82), EEA1 (0.81); STRING partners: IQGAP1 (0.893), PLEC (0.706)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 is among the most connected genes in the co-abundance graph and links IQGAP1, SPTBN1, SEPTIN9, RRBP1, and EEA1. Its known STRING relationships with IQGAP1 and PLEC support a membrane-adhesion and cytoskeletal scaffold. TLN1 is associated with focal adhesions, integrin activation, cell adhesion, migration, and actin organization, and has a large literature base with disease links involving cancer and developmental syndromes. Its HPA profile is enhanced in blood vessels and enriched in megakaryocyte and platelet populations.
- **Conclusion**: Established evidence supports TLN1 as the module's adhesion and integrin-associated anchor. Its vascular and platelet-related HPA pattern warrants attention to shared vascular or stromal cell content, but does not establish that blood contamination explains the module.

#### PLEC

- **Related proteins** (co-abundance neighbors): IMPDH2 (0.90), SPTBN1 (0.88); STRING partners: SPTAN1 (0.795), TLN1 (0.706)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments, Cytosol; IHC detected in placenta, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plectin. Plectin is a prominent member of an important family of structurally and in part functionally related proteins, termed plakins or cytolinkers, that are capable of interlinking different elements of the cytoskeleton. Plakins, with their multi-domain structure and enormous size, not only play crucial roles in maintaining cell and tissue integrity and orchestrating dynamic changes in cytoarchitecture…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 5B, with muscular dystrophy (0.796); epidermolysis bullosa simplex 5A, Ogna type (0.775); autosomal recessive limb-girdle muscular dystrophy type 2Q (0.768); epidermolysis bullosa simplex 5C, with pyloric atresia (0.755); epidermolysis bullosa simplex with nail dystrophy (0.695)
- **Europe PMC papers**: 2578
- **Why important**: PLEC connects IMPDH2 with SPTBN1 and has known STRING relationships with SPTAN1 and TLN1. It is included in both primary cytokinesis terms (GO:BP cytokinesis; q_global = 0.0348) and (GO:BP cytoskeleton-dependent cytokinesis; q_global = 0.0348) and is a major cytolinker that integrates intermediate filaments with other cytoskeletal systems. Its HPA profile is enhanced in skeletal muscle and in urothelial cells, and it has extensive literature and strong disease associations involving epidermolysis bullosa and muscular dystrophy.
- **Conclusion**: Established evidence supports PLEC as a structural integrator that could connect the spectrin and adhesion machinery to intermediate filaments during cell remodeling. Its contribution to cytokinesis is supported by the primary enrichment, whereas a specific role in the shared tissue context remains a hypothesis.
