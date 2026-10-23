# Conserved co-abundance modules: cell line and skin

## Module 0

**Tissue pair**: cell line and skin  
**Genes (10)**: ABCD3, ATP2C1, BAZ1A, BAZ2A, BPTF, GALNT7, URB1, NUP155, POLRMT, TMEM192

### Function

The strongest functional interpretation is chromatin organization and transcriptional regulation through an ISWI-type remodeling complex. The primary enrichment evidence is (GO:CC ISWI-type complex; q_global = 0.00444), which contains BAZ1A, BAZ2A, and BPTF. The supplementary STRING annotations independently support shared chromatin-remodeling architecture, including bromodomains, PHD-type zinc-finger features, DDT and WHIM domains, and related remodeling-factor motifs (15 supplementary STRING terms; within-query FDR 0.00011–0.0271). The remaining genes do not provide a globally corrected GO or KEGG term, so they should not be assigned a single pathway solely from nominal or supplementary evidence. Their annotations instead suggest connections to calcium handling, glycosylation, mitochondrial transcription, ribosome biogenesis, lipid transport, endosomal or lysosomal biology, and nuclear transport. Thus, the module most plausibly represents a chromatin-regulatory core embedded in a broader cellular state involving transcriptional activity and organelle homeostasis.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are located mainly in intracellular compartments such as the nucleoplasm, nuclear speckles, mitochondria, Golgi apparatus, peroxisomes, endosomes or lysosomes, and the nuclear envelope. Most genes have low tissue specificity, while several show tissue or cell-type enhancement. The HPA patterns include bone marrow and neutrophil-associated enrichment for BAZ1A, reproductive-cell enrichment for POLRMT and NUP155, liver enhancement for ABCD3, and stomach or prostatic-glandular associations for GALNT7. Most genes have low immune-cell specificity, although BAZ1A is immune-cell enhanced in neutrophils and several genes show hematopoietic or neutrophil-related cell-type signals. Therefore, blood contamination is not the dominant explanation supported by the summary, but shared cell-type composition and broad intracellular housekeeping or regulatory programs could contribute to the conserved co-abundance pattern. Protein detection in skin is widespread among the measured genes, whereas the cell-line protein-detection comparison has no informative matching HPA result.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC ISWI-type complex | 0.00444 | BAZ1A, BAZ2A, BPTF |

### STRING and hu.MAP

STRING provides a high-confidence direct relationship between BAZ1A and BPTF, supporting a known physical or functional association within the chromatin-remodeling core. The other module edges are not supported by high-confidence STRING links in the supplied results, so the co-abundance network should not be interpreted as a fully established physical interaction map. hu.MAP identifies a complex containing BPTF and BAZ2A (hu.MAP huMAP3_15095.1), alongside established chromatin and Polycomb-associated proteins including EED, SUZ12, EZH2, EZH1, JARID2, and related factors. Together, STRING, hu.MAP, (GO:CC ISWI-type complex; q_global = 0.00444), and the domain enrichments support a real chromatin-regulatory component, while the remaining co-abundance edges are more plausibly indirect, condition-dependent, or driven by shared cellular state.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: BAZ1A–BPTF (0.935)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Domain in different transcription and chromosome remodeling factors (FDR = 0.00011, 3 genes); Pfam WSTF, HB1, Itc1p, MBD9 motif 1 (FDR = 0.00028, 3 genes); InterPro DDT domain (FDR = 0.0006, 3 genes); InterPro WHIM2 domain (FDR = 0.0006, 3 genes); InterPro Bromodomain, conserved site (FDR = 0.0022, 3 genes); SMART Bromo domain (FDR = 0.0029, 3 genes); COMPARTMENTS ISWI-type complex (FDR = 0.0061, 3 genes); Keyword Bromodomain (FDR = 0.0061, 3 genes); InterPro Bromodomain (FDR = 0.0072, 3 genes); InterPro Bromodomain-like superfamily (FDR = 0.0072, 3 genes); Pfam Williams-Beuren syndrome DDT (WSD), D-TOX E motif (FDR = 0.0114, 2 genes); InterPro Zinc finger, PHD-finger (FDR = 0.0127, 3 genes); InterPro Zinc finger, PHD-type (FDR = 0.0153, 3 genes); InterPro WHIM1 domain (FDR = 0.0181, 2 genes); InterPro Zinc finger, FYVE/PHD-type (FDR = 0.0271, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15095.1 (BPTF, BAZ2A; 2/17)

### Novelty

The chromatin-remodeling biology itself is not a new concept: BPTF, BAZ1A, and BAZ2A have established annotations, domain relationships, and complex-level support. The potentially novel observation is their conservation as a co-abundance module between cell line and skin together with genes spanning calcium transport, mitochondrial transcription, Golgi glycosylation, peroxisomal transport, lysosomal biology, and nuclear transport. The supplied evidence does not establish that this exact cross-tissue module has been previously reported, nor does absence of a STRING or hu.MAP relationship prove novelty. A cautious conclusion is that the module is a potentially novel systems-level co-abundance configuration built around a known chromatin-regulatory core, requiring comparison with published co-expression modules and independent datasets before being called a new biological mechanism.

**Hypothesis.** Hypothesis: a conserved cellular state couples ISWI-related chromatin remodeling with coordinated regulation of transcription, organelle maintenance, and epithelial or lineage-associated functions. BAZ1A, BPTF, and BAZ2A may form the regulatory core, while ATP2C1, POLRMT, GALNT7, ABCD3, TMEM192, NUP155, and URB1 may reflect downstream or parallel demands involving calcium balance, mitochondrial gene expression, protein glycosylation, lipid handling, endolysosomal function, nuclear transport, and ribosome production. The sparse direct interaction evidence argues for a coordinated state or indirect regulatory program rather than a single physical complex containing every module member. This hypothesis predicts that perturbing the chromatin core should alter a subset of the organelle and epithelial-state genes, but that prediction requires experimental testing.

### Important genes

#### BPTF

- **Related proteins** (co-abundance neighbors): BAZ1A (0.86), ATP2C1 (0.84), POLRMT (0.81); STRING partners: BAZ1A (0.935)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_15095.1
- **Function (MyGene.info)**: bromodomain PHD finger transcription factor. This gene was identified by the reactivity of its encoded protein to a monoclonal antibody prepared against brain homogenates from patients with Alzheimer's disease. Analysis of the original protein (fetal Alz-50 reactive clone 1, or FAC1), identified as an 810 aa protein containing a DNA-binding domain and a zinc finger motif, suggested it might play a role in the regulation of transcription. Hig…
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and distal limb anomalies (0.788); Intellectual disability (0.539); hereditary disease (0.538); neurodegenerative disease (0.536); Global developmental delay (0.507)
- **Europe PMC papers**: 1741
- **Why important**: BPTF is a central connector in the module and is directly linked to BAZ1A by high-confidence STRING evidence. It is one of the genes in the globally supported ISWI-type complex term (GO:CC ISWI-type complex; q_global = 0.00444), is present in the hu.MAP complex (hu.MAP huMAP3_15095.1), and carries the broadest set of supplementary chromatin-remodeling domain annotations (15 supplementary STRING terms; within-query FDR 0.00011–0.0271). Its established functions include chromatin remodeling and transcriptional regulation, and it has substantial literature coverage and disease associations involving neurodevelopmental and neurodegenerative conditions.
- **Conclusion**: Established evidence supports BPTF as a principal chromatin-regulatory anchor of the module. It is reasonable to regard BPTF as a driver or marker of the module's transcriptional component. It remains a hypothesis that BPTF mechanistically coordinates the nonchromatin genes in this module.

#### BAZ1A

- **Related proteins** (co-abundance neighbors): BPTF (0.86); STRING partners: BPTF (0.935)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: bromodomain adjacent to zinc finger domain 1A. The BAZ1A gene encodes the accessory subunit of the ATP-dependent chromatin assembly factor (ACF), a member of the ISWI ('imitation switch') family of chromatin remodeling complexes (summarized by Racki et al., 2009 [PubMed 20033039]).[supplied by OMIM, Apr 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); non-small cell lung carcinoma (0.405); lung adenocarcinoma (0.395); hypothyroidism (0.391); psoriasis (0.346)
- **Europe PMC papers**: 666
- **Why important**: BAZ1A participates in the globally supported ISWI-type complex (GO:CC ISWI-type complex; q_global = 0.00444), is the high-confidence STRING partner of BPTF, and has extensive supplementary support for bromodomain, PHD-type, DDT, and WHIM-related chromatin features (15 supplementary STRING terms; within-query FDR 0.00011–0.0271). Its established role as an accessory subunit of the ATP-dependent ACF chromatin-assembly complex gives it direct mechanistic relevance. Its bone-marrow, neutrophil, and neutrophil-progenitor signals also make it important for evaluating whether some module variation reflects cellular composition.
- **Conclusion**: Established evidence identifies BAZ1A as both a chromatin-complex component and a plausible marker of hematopoietic or neutrophil-associated state. The module does not establish that BAZ1A-mediated chromatin remodeling causes the observed tissue conservation or immune-related signal.

#### BAZ2A

- **Related proteins** (co-abundance neighbors): POLRMT (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15095.1
- **Function (MyGene.info)**: bromodomain adjacent to zinc finger domain 2A. Enables histone binding activity. Contributes to RNA polymerase I core promoter sequence-specific DNA binding activity. Predicted to be involved in DNA methylation; histone deacetylation; and negative regulation of macromolecule metabolic process. Predicted to act upstream of or within chromatin organization and histone modification. Located in cytosol and nuclear speck. [provided by Alliance of G…
- **Diseases (Open Targets)**: neurodegenerative disease (0.508); premature birth (0.347); hypothyroidism (0.176); posterior cortical atrophy (0.103); Graves disease (0.098)
- **Europe PMC papers**: 649
- **Why important**: BAZ2A is part of the globally supported ISWI-type complex signal (GO:CC ISWI-type complex; q_global = 0.00444), shares the chromatin-related supplementary annotations (10 supplementary STRING terms; within-query FDR 0.00011–0.0072) and (4 supplementary STRING terms; within-query FDR 0.0127–0.0271), and appears with BPTF in the hu.MAP complex (hu.MAP huMAP3_15095.1). Its established activities include histone binding, rDNA heterochromatin formation, RNA polymerase I promoter-related regulation, and chromatin organization. Its network link to POLRMT may connect the chromatin core to a broader transcriptional or metabolic state.
- **Conclusion**: Established evidence supports BAZ2A as a second major chromatin and transcriptional anchor. The relationship between BAZ2A and POLRMT in this co-abundance module is suggestive of coordinated regulation, but it is not established as a direct physical interaction by the supplied STRING evidence.

#### ATP2C1

- **Related proteins** (co-abundance neighbors): BPTF (0.84), GALNT7 (0.81), TMEM192 (0.80), NUP155 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase secretory pathway Ca2+ transporting 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases. This magnesium-dependent enzyme catalyzes the hydrolysis of ATP coupled with the transport of calcium ions. Defects in this gene cause Hailey-Hailey disease, an autosomal dominant disorder. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Aug 20…
- **Diseases (Open Targets)**: Hailey-Hailey disease (0.801); restless legs syndrome (0.326); movement disorder (0.265); cutaneous lupus erythematosus (0.231); systemic lupus erythematosus (0.225)
- **Europe PMC papers**: 1369
- **Why important**: ATP2C1 is the most connected module gene by the supplied network description and links the chromatin-associated BPTF branch with GALNT7, TMEM192, and NUP155. Its established function is ATP-dependent calcium and manganese transport in the secretory pathway, with roles in intracellular calcium homeostasis and epidermal biology. Its skin detection and strong disease association with Hailey–Hailey disease make it particularly relevant to the cell-line and skin comparison.
- **Conclusion**: Established evidence supports ATP2C1 as an important epithelial and calcium-homeostasis component, not as a member of the ISWI complex. Its connection to the chromatin core is best treated as an indirect co-abundance relationship. A plausible but unproven interpretation is that calcium and epithelial-state regulation help shape the conserved module.

#### POLRMT

- **Related proteins** (co-abundance neighbors): URB1 (0.83), BAZ2A (0.82), BPTF (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase mitochondrial. This gene encodes a mitochondrial DNA-directed RNA polymerase. The gene product is responsible for mitochondrial gene expression as well as for providing RNA primers for initiation of replication of the mitochondrial genome. Although this polypeptide has the same function as the three nuclear DNA-directed RNA polymerases, it is more closely related to RNA polymerases of phage and mitochondrial pol…
- **Diseases (Open Targets)**: combined oxidative phosphorylation deficiency 55 (0.798); neurodegenerative disease (0.470); neurodevelopmental disorder (0.340); substance-related disorder (0.221); mitochondrial DNA depletion syndrome 4a (0.118)
- **Europe PMC papers**: 1149
- **Why important**: POLRMT occupies a bridging position between BPTF, BAZ2A, and URB1 in the module. Its established function is mitochondrial DNA transcription and provision of RNA primers for mitochondrial genome replication. It is detected in skin and shows enhancement in differentiating spermatogonia and spermatid-related cell types, while its disease associations include mitochondrial oxidative-phosphorylation and mitochondrial DNA depletion disorders.
- **Conclusion**: Established evidence supports POLRMT as a mitochondrial gene-expression component that may report cellular energetic or differentiation state. Its placement beside the chromatin regulators is biologically suggestive but does not prove direct chromatin-to-mitochondrial regulation. The proposed bridge between these processes remains a hypothesis.

## Module 1

**Tissue pair**: cell line and skin  
**Genes (11)**: AP2B1, LIG4, GSPT2, MSH3, MSH6, MT-ND4, PAWR, RRP1B, SCAF11, DNTTIP2, UFSP2

### Function

The strongest functional interpretation is a DNA maintenance and repair module. The primary evidence is the globally corrected enrichment for single guanine insertion binding (GO:MF single guanine insertion binding; q_global = 0.0378), positive regulation of helicase activity (GO:BP positive regulation of helicase activity; q_global = 0.0378), and somatic recombination of immunoglobulin gene segments (GO:BP somatic recombination of immunoglobulin gene segments; q_global = 0.0423). MSH3 and MSH6 provide the clearest mismatch-recognition signal, while LIG4 contributes a DNA-end-joining and V(D)J-recombination function. The supplementary STRING annotations reinforce this interpretation through mismatch-repair and nonhomologous-end-joining associations (STRING NetworkNeighborAL Nonhomologous end joining complex, and Mismatch repair complex; within-query FDR = 0.0152) and MutS-family domain annotations (STRING SMART DNA-binding domain of DNA mismatch repair MUTS family; within-query FDR = 0.0308), (STRING SMART ATPase domain of DNA mismatch repair MUTS family; within-query FDR = 0.0308), (STRING Pfam MutS domain I; within-query FDR = 0.0464), (STRING Pfam MutS domain II; within-query FDR = 0.0464). The remaining genes have functions involving mitochondrial respiration, apoptosis, translation termination, UFM1 modification, RNA splicing, chromatin or nucleolar processes, vesicle trafficking, and ribosomal RNA processing. Thus, the module is not a uniform canonical repair complex; it appears to combine a strongly connected repair-associated subset with broadly expressed cellular genes organized around MT-ND4 in the co-abundance graph.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and most have low immune-cell specificity, so the module does not primarily resemble a blood-cell or circulating-protein signature. HPA detects protein in skin for nearly all module members with available skin measurements, consistent with the observed cell-line and skin sharing, but this does not establish a skin-specific biological process. Several genes show cell-type-enhanced expression in reproductive, epithelial, glial, cardiac, or other specialized cell types, indicating a heterogeneous cellular background rather than a single distinctive cell population. The module may therefore reflect a shared cellular state or technical co-abundance pattern superimposed on a genuine repair-associated subset.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF single guanine insertion binding | 0.0378 | MSH3, MSH6 |
| GO:BP positive regulation of helicase activity | 0.0378 | MSH3, MSH6 |
| GO:BP somatic recombination of immunoglobulin gene segments | 0.0423 | LIG4, MSH3, MSH6 |

### STRING and hu.MAP

STRING supports a compact, known relationship cluster among MSH3, MSH6, and LIG4. The strongest interaction is between MSH3 and MSH6, and LIG4 is connected to both mismatch-repair proteins at high confidence (STRING NetworkNeighborAL Nonhomologous end joining complex, and Mismatch repair complex; within-query FDR = 0.0152). These relationships support the biological coherence of the repair-associated core, although STRING does not establish that all module genes act in one physical complex. The MutS-domain annotations for MSH3 and MSH6 (STRING SMART DNA-binding domain of DNA mismatch repair MUTS family; within-query FDR = 0.0308), (STRING SMART ATPase domain of DNA mismatch repair MUTS family; within-query FDR = 0.0308), (STRING Pfam MutS domain I; within-query FDR = 0.0464), (STRING Pfam MutS domain II; within-query FDR = 0.0464) are consistent with their established mismatch-recognition functions. No qualifying hu.MAP complex contains multiple module members. MT-ND4 has the highest co-abundance connectivity in the module, yet it has no reported STRING partners or hu.MAP complex membership here. Consequently, the co-abundance network is broader than the experimentally supported protein-interaction network and should not be interpreted as a physical complex.

**STRING interactions (score >= 0.7)**: 3 of 55 gene pairs: LIG4–MSH3 (0.878); LIG4–MSH6 (0.965); MSH3–MSH6 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Nonhomologous end joining complex, and Mismatch repair complex (FDR = 0.0152, 3 genes); SMART DNA-binding domain of DNA mismatch repair MUTS family (FDR = 0.0308, 2 genes); SMART ATPase domain of DNA mismatch repair MUTS family (FDR = 0.0308, 2 genes); Pfam MutS domain I (FDR = 0.0464, 2 genes); Pfam MutS domain II (FDR = 0.0464, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be claimed as a newly discovered molecular complex. The MSH3–MSH6 mismatch-repair relationship and the LIG4 DNA-repair relationship are already supported by established annotations and high-confidence STRING links. The globally corrected enrichment is also biologically consistent with known DNA repair and immune-recombination functions. What may be novel is the cross-context co-abundance pattern linking this repair-associated core with MT-ND4 and the other broadly expressed genes in cell line and skin. However, the star-like structure centered on MT-ND4, the absence of a corresponding hu.MAP complex, and the lack of STRING support for most peripheral edges make it more appropriate to describe this as a potentially informative co-abundance association rather than a newly established pathway or complex. Absence from hu.MAP or STRING alone is not evidence of novelty.

**Hypothesis.** Hypothesis: a shared cellular state involving DNA surveillance or repair may co-vary with mitochondrial respiratory activity and general RNA, translation, chromatin, and trafficking processes in cell line and skin samples. In this model, MSH3 and MSH6 represent mismatch recognition, LIG4 represents DNA-end joining and recombination-associated repair, and MT-ND4 reflects a mitochondrial or energetic component that is correlated with the repair state rather than physically interacting with it. The peripheral genes could report coordinated changes in biosynthetic, RNA-processing, proteostatic, apoptotic, or vesicular activity. This hypothesis requires validation with independent expression data, protein-level measurements, perturbation experiments, and tests for sample composition or cellular-state confounding.

### Important genes

#### MSH6

- **Related proteins** (co-abundance neighbors): MT-ND4 (0.80); STRING partners: LIG4 (0.965), MSH3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus, Vesicles; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutS homolog 6. This gene encodes a member of the DNA mismatch repair MutS family. In E. coli, the MutS protein helps in the recognition of mismatched nucleotides prior to their repair. A highly conserved region of approximately 150 aa, called the Walker-A adenine nucleotide binding motif, exists in MutS homologs. The encoded protein heterodimerizes with MSH2 to form a mismatch recognition complex that functions …
- **Diseases (Open Targets)**: Lynch syndrome (0.878); colorectal cancer (0.832); endometrial cancer (0.819); mismatch repair cancer syndrome (0.799); mismatch repair cancer syndrome 1 (0.737)
- **Europe PMC papers**: 17901
- **Why important**: MSH6 is a central biological anchor because it belongs to the globally significant terms for guanine insertion binding, helicase regulation, and immunoglobulin-segment recombination (GO:MF single guanine insertion binding; q_global = 0.0378), (GO:BP positive regulation of helicase activity; q_global = 0.0378), (GO:BP somatic recombination of immunoglobulin gene segments; q_global = 0.0423). It has the strongest STRING connectivity within the repair-associated subset, linking to MSH3 and LIG4, and its MutS-family domain annotations provide convergent support (STRING NetworkNeighborAL Nonhomologous end joining complex, and Mismatch repair complex; within-query FDR = 0.0152), (STRING SMART DNA-binding domain of DNA mismatch repair MUTS family; within-query FDR = 0.0308), (STRING SMART ATPase domain of DNA mismatch repair MUTS family; within-query FDR = 0.0308), (STRING Pfam MutS domain I; within-query FDR = 0.0464), (STRING Pfam MutS domain II; within-query FDR = 0.0464). Its established mismatch-repair role and strong disease associations with Lynch syndrome and colorectal and endometrial cancers make it the most clinically prominent repair gene in the module. Its literature volume is exceptionally extensive relative to most peripheral members.
- **Conclusion**: Established evidence supports MSH6 as a mismatch-recognition and DNA-repair component of the module. It is plausible that MSH6 marks the principal repair-related biology represented by the module, but the co-abundance data alone do not prove altered MSH6 activity or a physical complex with every module member.

#### MSH3

- **Related proteins** (co-abundance neighbors): MT-ND4 (0.88); STRING partners: LIG4 (0.878), MSH6 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutS homolog 3. The protein encoded by this gene forms a heterodimer with MSH2 to form MutS beta, part of the post-replicative DNA mismatch repair system. MutS beta initiates mismatch repair by binding to a mismatch and then forming a complex with MutL alpha heterodimer. This gene contains a polymorphic 9 bp tandem repeat sequence in the first exon. The repeat is present 6 times in the reference genome sequence a…
- **Diseases (Open Targets)**: familial adenomatous polyposis 4 (0.743); endometrial carcinoma (0.651); hereditary neoplastic syndrome (0.576); endometrial cancer (0.374); endometrial neoplasm (0.370)
- **Europe PMC papers**: 4720
- **Why important**: MSH3 is the complementary MutS-family member paired with MSH6 in all three globally significant terms (GO:MF single guanine insertion binding; q_global = 0.0378), (GO:BP positive regulation of helicase activity; q_global = 0.0378), (GO:BP somatic recombination of immunoglobulin gene segments; q_global = 0.0423) and in all supplementary MutS-domain annotations (STRING SMART DNA-binding domain of DNA mismatch repair MUTS family; within-query FDR = 0.0308), (STRING SMART ATPase domain of DNA mismatch repair MUTS family; within-query FDR = 0.0308), (STRING Pfam MutS domain I; within-query FDR = 0.0464), (STRING Pfam MutS domain II; within-query FDR = 0.0464). Its strongest STRING relationship is with MSH6, and its known role in MutS beta mismatch recognition directly explains the repair signal. MSH3 also has established links to DNA repair, repeat-element maintenance, recombination, and hereditary neoplastic disease. Its literature volume is substantial, supporting a well-established functional interpretation.
- **Conclusion**: Established evidence identifies MSH3 as a core mismatch-repair component and a strong contributor to the module interpretation. A coordinated MSH3–MSH6 abundance pattern is biologically credible, whereas any functional connection to MT-ND4 or the peripheral genes remains a hypothesis.

#### LIG4

- **Related proteins** (co-abundance neighbors): MT-ND4 (0.87); STRING partners: MSH3 (0.878), MSH6 (0.965)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA ligase 4. The protein encoded by this gene is a DNA ligase that joins single-strand breaks in a double-stranded polydeoxynucleotide in an ATP-dependent reaction. This protein is essential for V(D)J recombination and DNA double-strand break (DSB) repair through nonhomologous end joining (NHEJ). This protein forms a complex with the X-ray repair cross complementing protein 4 (XRCC4), and further interacts wit…
- **Diseases (Open Targets)**: DNA ligase IV deficiency (0.834); plasma cell myeloma (0.662); severe combined immunodeficiency due to DCLRE1C deficiency (0.650); severe combined immunodeficiency (0.615); T-B- severe combined immunodeficiency (0.526)
- **Europe PMC papers**: 3646
- **Why important**: LIG4 supplies the module’s clearest nonhomologous-end-joining and V(D)J-recombination component. It contributes to the globally corrected immunoglobulin-recombination term (GO:BP somatic recombination of immunoglobulin gene segments; q_global = 0.0423) and is linked in STRING to both MSH3 and MSH6 (STRING NetworkNeighborAL Nonhomologous end joining complex, and Mismatch repair complex; within-query FDR = 0.0152). Its established function in DNA double-strand-break repair, together with associations with DNA ligase IV deficiency and severe combined immunodeficiency, gives it strong mechanistic and disease relevance. Its literature volume is extensive.
- **Conclusion**: Established evidence supports LIG4 as a DNA-end-joining and recombination-associated member of the repair core. The simultaneous presence of LIG4 with MSH3 and MSH6 may reflect coordinated DNA-maintenance biology, but it does not demonstrate that mismatch repair and nonhomologous end joining form one physical complex in this module.

#### MT-ND4

- **Related proteins** (co-abundance neighbors): PAWR (0.90), MSH3 (0.88), LIG4 (0.87), GSPT2 (0.84), UFSP2 (0.84), SCAF11 (0.84), DNTTIP2 (0.83), RRP1B (0.83), AP2B1 (0.82), MSH6 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH dehydrogenase subunit 4. Enables NADH dehydrogenase (ubiquinone) activity. Involved in mitochondrial electron transport, NADH to ubiquinone and mitochondrial respiratory chain complex I assembly. Part of mitochondrial respiratory chain complex I. Implicated in Leber hereditary optic neuropathy; Parkinson's disease; macular degeneration; and schizophrenia. Biomarker of Alzheimer's disease. [provided by Alliance of Genome R…
- **Diseases (Open Targets)**: MELAS syndrome (0.747); Leber hereditary optic neuropathy (0.727); mitochondrial disease (0.667); type 2 diabetes mellitus (0.610); mitochondrial complex I deficiency (0.594)
- **Europe PMC papers**: 3804
- **Why important**: MT-ND4 is the dominant topological hub of the co-abundance subgraph, connecting to every other module member with the greatest weighted strength. It encodes a mitochondrial respiratory-chain component involved in NADH-to-ubiquinone electron transport and complex one assembly, and it has extensive literature and disease associations involving mitochondrial disorders, optic neuropathy, Parkinson’s disease, macular degeneration, and related conditions. Its HPA profile includes tissue and cell-type enrichment and protein detection in skin. However, it has no STRING partners or hu.MAP complex membership in the supplied evidence, making its network centrality a co-abundance observation rather than proof of direct molecular interaction.
- **Conclusion**: Established evidence supports MT-ND4 as a mitochondrial respiratory-chain gene and as the principal co-abundance hub. The hypothesis that mitochondrial energetic state is coordinated with DNA repair is biologically plausible, but the current data cannot distinguish true regulation from shared sample composition, mitochondrial abundance, or other confounding.

## Module 2

**Tissue pair**: cell line and skin  
**Genes (11)**: HEATR1, LRBA, PDS5B, PHIP, POLR2A, PDCD11, SUPV3L1, YARS2, TEX10, URB2, YTHDC2

### Function

The module is most consistent with a broadly expressed intracellular RNA-processing and ribosome-biogenesis program, with a prominent nucleolar component and additional mitochondrial RNA and gene-expression links. URB2 occupies a central position connecting several otherwise distinct parts of the network. HEATR1, PDCD11, and TEX10 form the clearest functionally coherent subgroup: all are linked by supplementary STRING evidence to rRNA processing or RNA helicase-related biology (STRING NetworkNeighborAL rRNA processing, and RNA helicase activity; within-query FDR = 0.0215), and their pairwise STRING relationships are already documented. SUPV3L1 adds mitochondrial RNA surveillance and degradation, while POLR2A represents the transcriptional machinery that supplies precursor transcripts for downstream RNA processing. No GO or KEGG term passed global correction; therefore, the functional interpretation rests on the concordance of individual gene annotations, network organization, and supplementary interaction evidence rather than on a globally significant enrichment term.

**Cell composition.** The module does not resemble a plasma-protein or secreted-protein module: the genes are intracellular, and HPA reports no secreted genes. Most genes have low tissue specificity, which is compatible with a broadly expressed, housekeeping-like program involving transcription, RNA processing, ribosome production, mitochondrial RNA metabolism, or genome maintenance. HPA reports low immune-cell specificity for every module gene and no enriched blood-cell category, arguing against a straightforward blood-cell contamination explanation. A subset shows cell-type-enhanced expression, including epicardial, renal epithelial, cardiomyocyte, hematopoietic-stem-cell, and erythrocyte-progenitor contexts, but these signals are heterogeneous rather than indicative of one dominant shared cell type. Protein detection in skin is reported for several genes, supporting biological presence of the module in skin, although the cell-line protein evidence is unavailable rather than negative.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides established physical or functional support for the nucleolar RNA-processing interpretation. HEATR1 and PDCD11 have a particularly strong documented relationship, and both also connect with TEX10; these three genes are all included in the supplementary rRNA-processing and RNA-helicase term (STRING NetworkNeighborAL rRNA processing, and RNA helicase activity; within-query FDR = 0.0215). The module-level co-abundance edges involving URB2, LRBA, PHIP, POLR2A, YTHDC2, and other genes should not automatically be treated as physical interactions, because the fact sheet does not report corresponding STRING partners for most of them. hu.MAP places SUPV3L1 and YARS2 together in both (hu.MAP huMAP3_09113.1) and (hu.MAP huMAP3_06589.1), indicating recurring complex-level support for a mitochondrial or RNA-related association, but each complex contains many additional proteins and only a small subset is represented in this module. Thus, the module combines a known nucleolar interaction cluster, a hu.MAP-supported SUPV3L1–YARS2 association, and co-abundance relationships that remain less specifically characterized.

**STRING interactions (score >= 0.7)**: 3 of 55 gene pairs: HEATR1–PDCD11 (0.999); HEATR1–TEX10 (0.747); PDCD11–TEX10 (0.716)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL rRNA processing, and RNA helicase activity (FDR = 0.0215, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09113.1 (SUPV3L1, YARS2; 2/72); huMAP3_06589.1 (SUPV3L1, YARS2; 2/79)

### Novelty

This cannot be claimed as a wholly new molecular complex or pathway. The HEATR1–PDCD11–TEX10 relationships and the SUPV3L1–YARS2 hu.MAP associations are already represented in external resources. The potentially new observation is the conserved co-abundance organization of these genes across cell line and skin, particularly the coupling of a known nucleolar RNA-processing subgroup to URB2, mitochondrial RNA factors, transcriptional machinery, and genes involved in chromatin, cohesion, trafficking, or RNA regulation. However, absence of several module pairs from STRING or hu.MAP is not evidence of novelty by itself. The appropriate conclusion is that this is a potentially novel cross-tissue co-abundance configuration built partly from previously known molecular relationships, requiring independent replication and perturbation experiments before being described as a new mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated control of RNA production, ribosome assembly, and RNA quality control in cells represented in both cell line and skin. A nucleolar assembly or transcriptional state could increase the co-abundance of POLR2A with URB2 and the HEATR1–PDCD11–TEX10 rRNA-processing group, while SUPV3L1 and YARS2 couple this state to mitochondrial RNA turnover and mitochondrial translation. The remaining associations may represent shared regulation, cellular growth state, or compartmental coordination rather than direct binding. This hypothesis predicts that perturbing nucleolar ribosome-biogenesis factors should alter the abundance or activity of mitochondrial RNA-quality-control components, but that prediction is not established by the current fact sheet.

### Important genes

#### URB2

- **Related proteins** (co-abundance neighbors): LRBA (0.83), YARS2 (0.82), HEATR1 (0.82), PHIP (0.81), POLR2A (0.81), SUPV3L1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: URB2 ribosome biogenesis homolog. Predicted to be involved in ribosome biogenesis. Located in aggresome; midbody; and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: insomnia (0.160); epilepsy (0.118); prostate cancer (0.111); Familial prostate cancer (0.111); alcohol drinking (0.086)
- **Europe PMC papers**: 168
- **Why important**: URB2 is the central network connector in the module, linking the nucleolar RNA-processing subgroup with LRBA, YARS2, PHIP, POLR2A, and SUPV3L1. Its annotation supports a role in ribosome biogenesis and nucleolar biology, and the module’s supplementary STRING signal includes URB2 in the rRNA-processing and RNA-helicase-related gene set (STRING NetworkNeighborAL rRNA processing, and RNA helicase activity; within-query FDR = 0.0215). It has a substantial literature base and additional disease-oriented associations, making it a strong candidate for coordinating the module rather than merely marking one peripheral process.
- **Conclusion**: Established evidence supports URB2 as a ribosome-biogenesis-related nucleolar factor and as the principal co-abundance connector in this module. It is plausible, but not established, that URB2 coordinates the nucleolar and mitochondrial RNA components.

#### HEATR1

- **Related proteins** (co-abundance neighbors): URB2 (0.82); STRING partners: PDCD11 (0.999), TEX10 (0.747)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HEAT repeat containing 1. Enables RNA binding activity. Involved in positive regulation of rRNA processing and positive regulation of transcription by RNA polymerase I. Located in fibrillar center and mitochondrion. Implicated in pancreatic ductal carcinoma. Biomarker of glioblastoma. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.475); Alzheimer disease (0.463); Parkinson disease (0.462); lysosomal storage disease (0.462); musculoskeletal system disorder (0.168)
- **Europe PMC papers**: 342
- **Why important**: HEATR1 is a nucleolar RNA-binding factor annotated for rRNA processing, small-subunit ribosome biogenesis, and RNA polymerase I regulation. It is part of the most coherent known interaction subgroup, with documented STRING relationships to PDCD11 and TEX10 (STRING NetworkNeighborAL rRNA processing, and RNA helicase activity; within-query FDR = 0.0215). Its skin protein detection and cell-type-enhanced expression in epicardial cells further support biological expression in relevant tissues. Its literature includes links to cancer and neurodegenerative disease, while remaining focused enough to be mechanistically informative.
- **Conclusion**: Established evidence identifies HEATR1 as a nucleolar rRNA-processing and ribosome-biogenesis factor embedded in a known interaction neighborhood. Its role as a driver of the cross-tissue co-abundance pattern remains a hypothesis.

#### PDCD11

- **Related proteins** (co-abundance neighbors): TEX10 (0.81); STRING partners: HEATR1 (0.999), TEX10 (0.716)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 11. PDCD11 is a NF-kappa-B (NFKB1; 164011)-binding protein that colocalizes with U3 RNA (MIM 180710) in the nucleolus and is required for rRNA maturation and generation of 18S rRNA (Sweet et al., 2003 [PubMed 14624448]; Sweet et al., 2008 [PubMed 17654514]).[supplied by OMIM, Oct 2008].
- **Diseases (Open Targets)**: Back pain (0.277); insomnia (0.216); systemic lupus erythematosus (0.170); neoplasm (0.095); colorectal carcinoma (0.093)
- **Europe PMC papers**: 334
- **Why important**: PDCD11 is annotated as a nucleolar factor required for rRNA maturation and generation of mature ribosomal RNA, and it has documented STRING relationships with both HEATR1 and TEX10 (STRING NetworkNeighborAL rRNA processing, and RNA helicase activity; within-query FDR = 0.0215). Its nucleolar-rim localization and skin protein detection align with the module’s proposed intracellular RNA-processing function. It also has disease-oriented associations, including systemic lupus erythematosus and neoplastic conditions, which may make regulation of this pathway biologically consequential.
- **Conclusion**: Established evidence supports PDCD11 as a core rRNA-processing component within the known HEATR1–PDCD11–TEX10 interaction group. The module does not establish that PDCD11 connects this nucleolar process to the other co-abundance branches.

#### TEX10

- **Related proteins** (co-abundance neighbors): PDCD11 (0.81), LRBA (0.80); STRING partners: HEATR1 (0.747), PDCD11 (0.716)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: testis expressed 10. Located in mitochondrion and nucleoplasm. Part of MLL1 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.089); placenta praevia (0.078); esophageal squamous cell carcinoma (0.075); urinary bladder carcinoma (0.075); colorectal carcinoma (0.075)
- **Europe PMC papers**: 251
- **Why important**: TEX10 is linked to cleavage and maturation of ribosomal RNA and is part of the documented HEATR1–PDCD11 interaction neighborhood (STRING NetworkNeighborAL rRNA processing, and RNA helicase activity; within-query FDR = 0.0215). It provides an independent molecular anchor for the nucleolar interpretation and connects that subgroup in the co-abundance graph to LRBA. Its cell-type-enhanced expression in cardiomyocytes and epicardial cells suggests that the observed signal may occur in specific tissue cell populations, although HPA also classifies its overall tissue specificity as low.
- **Conclusion**: Established evidence supports TEX10 as a ribosome-biogenesis-related nucleolar factor associated with HEATR1 and PDCD11. Its connection to LRBA and the broader module is a co-abundance observation whose molecular basis remains unresolved.

#### SUPV3L1

- **Related proteins** (co-abundance neighbors): URB2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_09113.1, huMAP3_06589.1
- **Function (MyGene.info)**: Suv3 like RNA helicase. Enables helicase activity; nucleic acid binding activity; and protein homodimerization activity. Involved in several processes, including mitochondrial RNA metabolic process; mitochondrion morphogenesis; and positive regulation of mitochondrial RNA catabolic process. Located in mitochondrial nucleoid and nucleus. Part of mitochondrial degradosome. [provided by Alliance of Genome Resources, Apr 202…
- **Diseases (Open Targets)**: neurodegenerative disease (0.541); response to vaccine (0.276); neoplasm (0.041); gestational diabetes (0.036); seasonal allergic rhinitis (0.025)
- **Europe PMC papers**: 275
- **Why important**: SUPV3L1 encodes a mitochondrial RNA helicase involved in mitochondrial RNA catabolism, mitochondrial RNA processing, and the mitochondrial degradosome. It is included in the supplementary STRING RNA-helicase-related signal (STRING NetworkNeighborAL rRNA processing, and RNA helicase activity; within-query FDR = 0.0215) and occurs with YARS2 in both hu.MAP complexes (hu.MAP huMAP3_09113.1) and (hu.MAP huMAP3_06589.1). This gives the module a mechanistically meaningful mitochondrial RNA-quality-control branch rather than a purely nucleolar interpretation. Its disease associations include neurodegenerative and mitochondrial-relevant contexts.
- **Conclusion**: Established evidence supports SUPV3L1 as a mitochondrial RNA surveillance factor and supports its complex-level association with YARS2 through hu.MAP. Its apparent coordination with nucleolar ribosome biogenesis is a hypothesis generated by the co-abundance pattern.

#### POLR2A

- **Related proteins** (co-abundance neighbors): URB2 (0.81), YTHDC2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase II subunit A. This gene encodes the largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene contains a carboxy terminal domain composed of heptapeptide repeats that are essential for polymerase activity. These repeats contain serine and threonine residues that are phosphorylated in actively transcribing RNA polymerase. In addition, …
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and variable intellectual and behavioral abnormalities (0.738); HIV infectious disease (0.600); hereditary disease (0.479); syndromic intellectual disability (0.462); Orthomyxoviridae infectious disease (0.374)
- **Europe PMC papers**: 4546
- **Why important**: POLR2A encodes the largest subunit of RNA polymerase II and is essential for messenger RNA transcription. In the module it connects URB2 with YTHDC2, providing a plausible transcriptional entry point for coordinated RNA-processing activity. It has the broadest functional and literature footprint among the selected genes, with extensive evidence across transcriptional biology and disease associations, and HPA reports tissue enhancement in lymphoid tissue despite low immune-cell specificity.
- **Conclusion**: Established evidence supports POLR2A as the core transcriptional machinery represented in the module. Its co-abundance with nucleolar and mitochondrial RNA factors may reflect shared regulation or cellular state, but a direct mechanistic coupling is not demonstrated.

## Module 3

**Tissue pair**: cell line and skin  
**Genes (5)**: CAD, EPRS1, IARS1, LARS1, RARS1

### Function

The module is most strongly interpreted as a cytosolic translation-support and aminoacyl-tRNA charging module. The primary evidence is the globally corrected enrichment for the aminoacyl-tRNA synthetase multienzyme complex (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 3.53e-06), aminoacyl-tRNA ligase activity (GO:MF ligase activity; q_global = 7.22e-05) (GO:MF aminoacyl-tRNA ligase activity; q_global = 0.000145) (GO:MF ligase activity, forming carbon-oxygen bonds; q_global = 0.000145), tRNA aminoacylation for protein translation (GO:BP tRNA aminoacylation for protein translation; q_global = 0.000145) (GO:BP amino acid activation; q_global = 0.000177) (GO:BP tRNA aminoacylation; q_global = 0.000177), aminoacyl-tRNA biosynthesis (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 0.000177), amino acid metabolism (GO:BP amino acid metabolic process; q_global = 0.000213), and tRNA-related catalytic activity (GO:MF catalytic activity, acting on a tRNA; q_global = 0.00269) (GO:BP tRNA metabolic process; q_global = 0.00862) (GO:MF catalytic activity, acting on RNA; q_global = 0.0464). EPRS1, IARS1, LARS1, and RARS1 provide the coherent synthetase core, while CAD contributes ligase and amino-acid-metabolism annotations through (GO:MF ligase activity; q_global = 7.22e-05) (GO:BP amino acid metabolic process; q_global = 0.000213). The co-abundance structure is biologically coherent rather than being driven by a single isolated annotation: the synthetase genes are densely connected, and LARS1 is the main topological bridge to CAD. The most defensible interpretation is coordinated abundance of components supporting amino-acid utilization, tRNA charging, translational fidelity, and protein synthesis.

**Cell composition.** This is not a plasma-protein, secreted-protein, or blood-cell-enriched module. HPA assigns all module genes low tissue specificity and low immune-cell specificity, with no secreted genes and no enriched blood-cell category. All module proteins are detected in skin, and their intracellular locations are consistent with cytosolic or nuclear translation-related functions. EPRS1 has a cell-type-enhanced association with salivary acinar cells, but this is not sufficient to define the module as a salivary or blood-cell signal. The shared cell-line and skin module therefore more plausibly reflects a broadly expressed intracellular housekeeping or growth-related program than sample contamination by circulating proteins.

**GO/KEGG enrichment**: 12 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 3.53e-06 | EPRS1, IARS1, LARS1, RARS1 |
| GO:MF ligase activity | 7.22e-05 | CAD, EPRS1, IARS1, LARS1, RARS1 |
| GO:MF aminoacyl-tRNA ligase activity | 0.000145 | EPRS1, IARS1, LARS1, RARS1 |
| GO:BP tRNA aminoacylation for protein translation | 0.000145 | EPRS1, IARS1, LARS1, RARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 0.000145 | EPRS1, IARS1, LARS1, RARS1 |
| GO:BP amino acid activation | 0.000177 | EPRS1, IARS1, LARS1, RARS1 |
| GO:BP tRNA aminoacylation | 0.000177 | EPRS1, IARS1, LARS1, RARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 0.000177 | EPRS1, IARS1, LARS1, RARS1 |
| GO:BP amino acid metabolic process | 0.000213 | CAD, EPRS1, IARS1, LARS1, RARS1 |
| GO:MF catalytic activity, acting on a tRNA | 0.00269 | EPRS1, IARS1, LARS1, RARS1 |
| GO:BP tRNA metabolic process | 0.00862 | EPRS1, IARS1, LARS1, RARS1 |
| GO:MF catalytic activity, acting on RNA | 0.0464 | EPRS1, IARS1, LARS1, RARS1 |

### STRING and hu.MAP

STRING provides very strong known functional or physical support for the synthetase core: EPRS1, IARS1, LARS1, and RARS1 are mutually connected in the reported high-confidence network. The STRING enrichment results independently recover the aminoacyl-tRNA synthetase multienzyme complex, cytosolic tRNA aminoacylation, aminoacyl-tRNA biosynthesis, and related ligase annotations (11 supplementary STRING terms; within-query FDR 9.08e-07–0.00025). hu.MAP identifies two complexes containing the same synthetase quartet (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), with additional synthetases, AIMP proteins, and translation-associated components outside this module. These findings indicate that the core relationships are already established molecular biology, not newly inferred interactions. CAD has no reported STRING partner or hu.MAP complex in this module, so its connection to LARS1 should be interpreted as a co-abundance association rather than evidence of direct physical binding.

**STRING interactions (score >= 0.7)**: 6 of 10 gene pairs: EPRS1–IARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–RARS1 (0.999); IARS1–LARS1 (0.999); IARS1–RARS1 (0.999); LARS1–RARS1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component aminoacyl-tRNA synthetase multienzyme complex (FDR = 9.08e-07, 4 genes); COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex (FDR = 1.34e-06, 4 genes); Keyword Ligase (FDR = 2.55e-06, 5 genes); InterPro Aminoacyl-tRNA synthetase, class I, conserved site (FDR = 4.04e-06, 4 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 8.22e-06, 4 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 1.33e-05, 4 genes); RCTM Cytosolic tRNA aminoacylation (FDR = 1.43e-05, 4 genes); Function Ligase activity (FDR = 1.74e-05, 5 genes); RCTM Selenoamino acid metabolism (FDR = 1.95e-05, 4 genes); InterPro Rossmann-like alpha/beta/alpha sandwich fold (FDR = 2.69e-05, 4 genes); Function aminoacyl-tRNA ligase activity (FDR = 2.88e-05, 4 genes); NetworkNeighborAL tRNA Aminoacylation (FDR = 4.83e-05, 4 genes); Keyword Protein biosynthesis (FDR = 7.99e-05, 4 genes); WikiPathways Amino acid metabolism (FDR = 0.00014, 4 genes); Process tRNA aminoacylation for protein translation (FDR = 0.00025, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, IARS1, RARS1, LARS1; 4/14); huMAP3_13688.1 (EPRS1, IARS1, RARS1, LARS1; 4/14)

### Novelty

The module is unlikely to represent a new aminoacyl-tRNA synthetase complex or a new protein-interaction mechanism, because the central synthetase relationships are already represented by STRING and hu.MAP and are supported by the primary GO/KEGG results. It may nevertheless be a useful tissue-pair co-abundance observation: the data show that this established translation-related machinery is coordinately abundant across cell line and skin. The distinctive aspect may be the inclusion of CAD and the particular abundance relationship linking nucleotide biosynthesis with the synthetase core, but the fact sheet does not establish that this relationship is mechanistically direct or previously unreported. Absence of CAD from the reported STRING and hu.MAP relationships does not by itself demonstrate novelty. A claim that the complete co-abundance module is new would require comparison with prior co-expression, proteomic, and tissue-specific module studies.

**Hypothesis.** Hypothesis: the module represents a coordinated biosynthetic state in which amino-acid charging and translational capacity are coupled to nucleotide supply. In this model, EPRS1, IARS1, LARS1, and RARS1 form the core aminoacyl-tRNA charging machinery, while CAD may mark or help support the precursor demand associated with active protein synthesis and cellular growth. LARS1 may serve as the abundance-level bridge between these processes because it has the strongest reported module connectivity and is the only gene directly connected to CAD in the co-abundance subgraph. This is a mechanistic hypothesis, not proof of a direct CAD-synthetase interaction; it should be tested with perturbation, flux measurements, and independent proteomic datasets.

### Important genes

#### EPRS1

- **Related proteins** (co-abundance neighbors): LARS1 (0.85), IARS1 (0.80); STRING partners: IARS1 (0.999), LARS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is a central member of the synthetase core, connects to IARS1 and LARS1 in the module, and is present in both hu.MAP complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1) and the core STRING relationships. It encodes the multifunctional glutamyl-prolyl-tRNA synthetase and is represented across the primary translation and tRNA-aminoacylation terms (12 globally significant GO/KEGG terms, q_global 3.53e-06–0.0464; see the table). Its annotations also include translational regulation and response to insulin, and it has established disease associations involving hypomyelinating leukodystrophy and developmental phenotypes. The literature support is substantial enough to make it a biologically informative representative of the module rather than a peripheral marker.
- **Conclusion**: Established evidence supports EPRS1 as a core component of the aminoacyl-tRNA charging and translation program. The module data support coordinated abundance with other synthetases, but do not establish that EPRS1 regulates the other genes or that its disease associations explain the tissue-shared module.

#### IARS1

- **Related proteins** (co-abundance neighbors): LARS1 (0.88), RARS1 (0.81), EPRS1 (0.80); STRING partners: EPRS1 (0.999), LARS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Isoleucine-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family and has been identified as a …
- **Diseases (Open Targets)**: growth retardation, intellectual developmental disorder, hypotonia, and hepatopathy (0.733); Abnormality of the skeletal system (0.332); microcephaly (0.289); Global developmental delay (0.289); Hallux valgus (0.184)
- **Europe PMC papers**: 184
- **Why important**: IARS1 is one of the most connected module genes and is linked to EPRS1, LARS1, and RARS1 in STRING and in both hu.MAP complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). It encodes the cytosolic isoleucyl-tRNA synthetase and is included in every primary enrichment term (12 globally significant GO/KEGG terms, q_global 3.53e-06–0.0464; see the table). Its annotations include translational fidelity, tRNA aminoacylation, and isoleucyl-tRNA aminoacylation, while disease evidence includes developmental, skeletal, neurological, and hepatopathy-related phenotypes. It also has established relevance to autoantibody responses in inflammatory muscle disease.
- **Conclusion**: Established evidence identifies IARS1 as a core aminoacyl-tRNA synthetase within the conserved module and as a plausible marker of translational fidelity. The co-abundance data do not show whether IARS1 is functionally limiting or merely co-regulated with the other synthetases.

#### LARS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.88), EPRS1 (0.85), CAD (0.82); STRING partners: EPRS1 (0.999), IARS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: leucyl-tRNA synthetase 1. This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals w…
- **Diseases (Open Targets)**: infantile liver failure syndrome 1 (0.670); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.510); Global developmental delay (0.119); sensorineural hearing loss disorder (0.119); Generalized-onset seizure (0.118)
- **Europe PMC papers**: 267
- **Why important**: LARS1 has the strongest reported topological position in the module and is the bridge between the synthetase-rich portion and CAD. It connects to IARS1, EPRS1, and CAD, is present in both hu.MAP complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), and has the full set of primary GO/KEGG annotations (12 globally significant GO/KEGG terms, q_global 3.53e-06–0.0464; see the table). It encodes the cytosolic leucine-tRNA synthetase, participates in the multisynthetase complex, and is linked to amino-acid starvation and leucine-response biology. Its disease associations include infantile liver failure and related developmental or neurological phenotypes, with substantial literature support.
- **Conclusion**: Established evidence makes LARS1 the strongest network-level candidate for coordinating the synthetase core with the CAD-associated metabolic signal. The proposed coordinating role remains a hypothesis because co-abundance and network position do not prove molecular regulation or direct interaction.

#### RARS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.81); STRING partners: EPRS1 (0.999), IARS1 (0.999), LARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 is a member of the highly supported synthetase core, participates in both hu.MAP complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), and has strong STRING links to EPRS1, IARS1, and LARS1. It is represented in the primary aminoacyl-tRNA, translation, and tRNA-metabolism terms (12 globally significant GO/KEGG terms, q_global 3.53e-06–0.0464; see the table). It encodes arginyl-tRNA synthetase and has disease associations involving hypomyelinating leukodystrophy, developmental phenotypes, and skeletal abnormalities. Although its local co-abundance degree is lower than that of the main hubs, its membership in the established complex makes it important for interpreting the module as a coordinated multi-enzyme unit.
- **Conclusion**: Established evidence supports RARS1 as an authentic component of the cytosolic aminoacyl-tRNA synthetase machinery represented by the module. Its lower local connectivity should not be taken as evidence of lesser biochemical importance, but the data do not establish a unique regulatory role for RARS1 in skin or cell line.

#### CAD

- **Related proteins** (co-abundance neighbors): LARS1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carbamoyl-phosphate synthetase 2, aspartate transcarbamylase, and dihydroorotase. The de novo synthesis of pyrimidine nucleotides is required for mammalian cells to proliferate. This gene encodes a trifunctional protein which is associated with the enzymatic activities of the first 3 enzymes in the 6-step pathway of pyrimidine biosynthesis: carbamoylphosphate synthetase (CPS II), aspartate transcarbamoylase, and dihydroorotase. This protein is regulated by the mitogen-activated…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 50 (0.660); congenital disorder of glycosylation type I (0.595); infantile epileptic-dyskinetic encephalopathy (0.499); type 2 diabetes mellitus (0.286); urolithiasis (0.283)
- **Europe PMC papers**: 60667
- **Why important**: CAD is the only module gene that is not part of the reported synthetase quartet and is the only gene connected to LARS1 in the module subgraph. It contributes to the globally corrected ligase and amino-acid-metabolism terms (GO:MF ligase activity; q_global = 7.22e-05) (GO:BP amino acid metabolic process; q_global = 0.000213), while its established function is the trifunctional first portion of de novo pyrimidine biosynthesis. CAD is regulated by the MAPK cascade and is relevant to proliferation, nucleotide production, and several developmental or metabolic disease associations. Its very large literature base makes it a strong biological anchor for the possible connection between biosynthetic demand and translational capacity.
- **Conclusion**: Established evidence supports CAD as a nucleotide-biosynthesis enzyme associated with the module, but not as a member of the aminoacyl-tRNA synthetase complex. Its apparent relationship to LARS1 is best treated as a hypothesis about coordinated biosynthetic demand rather than a demonstrated physical or regulatory interaction.
