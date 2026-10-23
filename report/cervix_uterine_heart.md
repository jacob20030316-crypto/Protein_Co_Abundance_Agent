# Conserved co-abundance modules: cervix_uterine and heart

## Module 0

**Tissue pair**: cervix_uterine and heart  
**Genes (19)**: BZW2, ADD3, AIMP2, ASPH, ATP1A1, MTHFD1, CKAP4, DHX9, DDX39B, FKBP4, HNRNPH1, HNRNPK, HNRNPL, HNRNPR, MATR3, PNP, ATIC, SERPINH1, XRCC6

### Function

The module is best interpreted as a conserved nuclear RNA-processing and pre-mRNA-splicing module. The primary evidence is the coherent set of globally corrected terms for RNA splicing, spliceosome-mediated mRNA splicing, mRNA processing, mRNA metabolism, and RNA processing (7 globally significant GO/KEGG terms, q_global 0.00108–0.0476; see the table). The same six genes recur across these terms: DDX39B, DHX9, HNRNPH1, HNRNPK, HNRNPL, and HNRNPR. This is supported independently by STRING functional categories for mRNA processing, major-pathway mRNA splicing, RNA-binding, spliceosomal complex, nucleoplasm, and ribonucleoprotein complex (STRING NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex; within-query FDR = 0.0019), (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0045), (STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.0166), (STRING COMPARTMENTS Spliceosomal complex; within-query FDR = 0.0378), (4 supplementary STRING terms; within-query FDR 0.0378–0.0386). The remaining genes likely represent connected cellular processes rather than a second equally established module function: MTHFD1 and ATIC are linked to purine metabolism, XRCC6 to DNA repair, ATP1A1 and ADD3 to membrane or cytoskeletal biology, and SERPINH1 to collagen biosynthesis and protein folding. Thus, the strongest interpretation is a broadly expressed RNA-processing network with peripheral links to translation-related metabolism, genome maintenance, membrane organization, and protein homeostasis.

**Cell composition.** This does not resemble a plasma-protein or secreted-protein module: only one gene is annotated as secreted, and the module is dominated by intracellular proteins, especially nucleoplasmic or nuclear-speckle proteins. The HPA data show low tissue specificity for most genes, with several tissue-enhanced or tissue-enriched signals involving muscle, heart muscle, liver, adipose tissue, and parathyroid gland. Most genes have low immune-cell specificity, and the module is not predominantly blood-cell enriched, although a minority show cell-type enhancement in trophoblast, neutrophil-progenitor, or related populations. Protein detection is complete in cervix and incomplete in heart, which is compatible with a shared, broadly expressed cellular program rather than a cervix-specific secretory signature. The cross-tissue conservation may therefore reflect shared nucleated cell biology, with possible contributions from differences in cellular composition.

**GO/KEGG enrichment**: 7 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA splicing, via transesterification reactions | 0.00108 | DDX39B, DHX9, HNRNPH1, HNRNPK, HNRNPL, HNRNPR |
| GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile | 0.00108 | DDX39B, DHX9, HNRNPH1, HNRNPK, HNRNPL, HNRNPR |
| GO:BP mRNA splicing, via spliceosome | 0.00108 | DDX39B, DHX9, HNRNPH1, HNRNPK, HNRNPL, HNRNPR |
| GO:BP mRNA processing | 0.00403 | DDX39B, DHX9, HNRNPH1, HNRNPK, HNRNPL, HNRNPR |
| GO:BP RNA splicing | 0.00403 | DDX39B, DHX9, HNRNPH1, HNRNPK, HNRNPL, HNRNPR |
| GO:BP mRNA metabolic process | 0.0245 | DDX39B, DHX9, HNRNPH1, HNRNPK, HNRNPL, HNRNPR |
| GO:BP RNA processing | 0.0476 | DDX39B, DHX9, HNRNPH1, HNRNPK, HNRNPL, HNRNPR |

### STRING and hu.MAP

STRING provides a dense, coherent interaction core among DDX39B, DHX9, HNRNPH1, HNRNPK, HNRNPL, HNRNPR, and MATR3. The strongest relationships are concentrated among the heterogeneous nuclear ribonucleoproteins and RNA helicases, while additional links connect DHX9 and HNRNPK to XRCC6. STRING functional categories identify mRNA-processing and spliceosomal relationships, but these are supplementary evidence and are not treated as global enrichment significance (15 supplementary STRING terms; within-query FDR 0.0019–0.0386). hu.MAP independently places HNRNPR, HNRNPL, MATR3, and HNRNPK together in a high-confidence RNA-associated complex (hu.MAP huMAP3_10625.1), and places overlapping subsets of these proteins in additional RNA-binding complexes (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_05721.1), (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_14523.1). ATIC and MTHFD1 also co-occur in a hu.MAP complex (hu.MAP huMAP3_12823.1). These results indicate that much of the module corresponds to already characterized RNA-binding and ribonucleoprotein biology, rather than an isolated or unexplained association.

**STRING interactions (score >= 0.7)**: 23 of 171 gene pairs: ATIC–MTHFD1 (0.998); DDX39B–DHX9 (0.962); DDX39B–HNRNPH1 (0.742); DDX39B–HNRNPK (0.808); DDX39B–HNRNPL (0.807); DDX39B–HNRNPR (0.74); DHX9–HNRNPH1 (0.878); DHX9–HNRNPK (0.939); DHX9–HNRNPL (0.901); DHX9–HNRNPR (0.909); DHX9–MATR3 (0.786); DHX9–XRCC6 (0.819); HNRNPH1–HNRNPK (0.975); HNRNPH1–HNRNPL (0.982); HNRNPH1–HNRNPR (0.947); HNRNPH1–MATR3 (0.911); HNRNPK–HNRNPL (0.99); HNRNPK–HNRNPR (0.962); HNRNPK–MATR3 (0.923); HNRNPK–XRCC6 (0.738); HNRNPL–HNRNPR (0.961); HNRNPL–MATR3 (0.757); HNRNPR–MATR3 (0.714)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex (FDR = 0.0019, 6 genes); NetworkNeighborAL Mixed, incl. CRD-mediated mRNA stabilization, and Zinc finger, CHHC-type (FDR = 0.0019, 5 genes); RCTM mRNA Splicing - Major Pathway (FDR = 0.0045, 6 genes); WikiPathways mRNA processing (FDR = 0.0079, 5 genes); NetworkNeighborAL Mixed, incl. Zinc finger, CHHC-type, and Multisystem proteinopathy (FDR = 0.0108, 4 genes); COMPARTMENTS Nucleoplasm (FDR = 0.0166, 7 genes); SMART RNA recognition motif (FDR = 0.0205, 4 genes); COMPARTMENTS Spliceosomal complex (FDR = 0.0378, 4 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0378, 8 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 0.0378, 6 genes); Keyword mRNA splicing (FDR = 0.0386, 5 genes); Keyword RNA-binding (FDR = 0.0386, 6 genes); Keyword Spliceosome (FDR = 0.0386, 4 genes); Keyword Ubl conjugation (FDR = 0.0386, 10 genes); Keyword Isopeptide bond (FDR = 0.0386, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10625.1 (HNRNPR, HNRNPL, MATR3, HNRNPK; 4/57); huMAP3_07581.1 (HNRNPR, HNRNPL, MATR3; 3/21); huMAP3_10659.1 (HNRNPR, HNRNPL, HNRNPK; 3/28); huMAP3_05721.1 (HNRNPL, MATR3; 2/6); huMAP3_12823.1 (MTHFD1, ATIC; 2/7); huMAP3_07225.1 (HNRNPR, HNRNPL; 2/7); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09654.1 (HNRNPR, HNRNPL; 2/13); huMAP3_14523.1 (HNRNPH1, HNRNPK; 2/33)

### Novelty

The module should not be described as a wholly new molecular complex or a newly discovered splicing pathway. Its central relationships are already represented in STRING, and several of its RNA-binding members co-occur in hu.MAP complexes (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_05721.1), (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_14523.1). The globally corrected enrichment also agrees with established annotations for RNA splicing and RNA processing (7 globally significant GO/KEGG terms, q_global 0.00108–0.0476; see the table). Nevertheless, the tissue-pair-level observation may still be useful: the evidence supports a conserved co-abundance pattern across cervix and heart, and the specific combination of the peripheral genes with the RNA-processing core may be a new observation in this dataset. That is a dataset-level finding rather than proof of a novel biochemical complex. Absence of a gene from STRING or hu.MAP, such as SERPINH1, ATP1A1, ASPH, or CKAP4, is not sufficient to establish novelty.

**Hypothesis.** Hypothesis: in both cervix and heart, a shared cellular state coordinates a core heterogeneous nuclear ribonucleoprotein and RNA-helicase program to regulate pre-mRNA splicing, processing, stability, and export. HNRNPR, HNRNPL, HNRNPH1, HNRNPK, DHX9, and DDX39B could act as the central RNA-processing machinery, while MATR3 may help organize or stabilize selected RNA-associated assemblies. The co-abundance of MTHFD1 and ATIC could reflect coupling of RNA production with nucleotide supply, whereas SERPINH1, CKAP4, ATP1A1, ADD3, and other peripheral genes may report tissue-specific structural, metabolic, or proteostatic context. This is a mechanistic model, not a demonstrated causal pathway; testing would require cell-resolved measurements, physical interaction assays, and perturbation of the candidate core.

### Important genes

#### HNRNPR

- **Related proteins** (co-abundance neighbors): MTHFD1 (0.91), ASPH (0.88), ATP1A1 (0.86), XRCC6 (0.86), FKBP4 (0.83), CKAP4 (0.83), DDX39B (0.83), BZW2 (0.82), HNRNPL (0.81), DHX9 (0.81), MATR3 (0.81), HNRNPH1 (0.80); STRING partners: DDX39B (0.74), DHX9 (0.909), HNRNPH1 (0.947), HNRNPK (0.962), HNRNPL (0.961), MATR3 (0.714)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_07581.1, huMAP3_10659.1, huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR is the strongest network hub in the module and is detected in both tissues by HPA. It belongs to every globally corrected enrichment term (7 globally significant GO/KEGG terms, q_global 0.00108–0.0476; see the table), every listed STRING functional category, and multiple hu.MAP RNA-associated complexes (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10659.1), (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1). Its annotated role as a spliceosome C-complex RNA-binding protein directly matches the module function. Its disease associations include neurodevelopmental disorders, and its substantial literature supports an established biological role.
- **Conclusion**: Established evidence supports HNRNPR as a central RNA-processing component and a credible marker of the module core. It is plausible that HNRNPR helps organize the shared RNA-processing state, but the co-abundance data do not establish that it is causally upstream.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): HNRNPH1 (0.92), MATR3 (0.88), SERPINH1 (0.85), ATIC (0.81), HNRNPR (0.81); STRING partners: DDX39B (0.807), DHX9 (0.901), HNRNPH1 (0.982), HNRNPK (0.99), HNRNPR (0.961), MATR3 (0.757)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_07581.1, huMAP3_10659.1, huMAP3_05721.1, huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is a major RNA-binding hub with strong connectivity to the other hnRNP proteins and MATR3. It appears in all primary terms (7 globally significant GO/KEGG terms, q_global 0.00108–0.0476; see the table), many STRING RNA-processing categories, and a broad set of hu.MAP complexes (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_05721.1), (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1). Its annotation specifically includes regulation of alternative mRNA splicing and mRNA processing. It is detected in both tissues and has a substantial literature base, with reported associations involving neuromuscular disease and cancer.
- **Conclusion**: Established evidence identifies HNRNPL as a core alternative-splicing and RNA-processing component. Its network position makes it a strong candidate for coordinating module activity, but a regulatory direction or tissue-specific target set remains a hypothesis.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): MATR3 (0.87), SERPINH1 (0.81); STRING partners: DDX39B (0.808), DHX9 (0.939), HNRNPH1 (0.975), HNRNPL (0.99), HNRNPR (0.962), MATR3 (0.923), XRCC6 (0.738)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_10659.1, huMAP3_14523.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK participates in all primary enrichment terms (7 globally significant GO/KEGG terms, q_global 0.00108–0.0476; see the table) and has strong STRING connections to DDX39B, DHX9, HNRNPH1, HNRNPL, HNRNPR, MATR3, and XRCC6. It is present in several hu.MAP complexes (hu.MAP huMAP3_10625.1), (hu.MAP huMAP3_10659.1), and (hu.MAP huMAP3_14523.1), is detected in both tissues, and is annotated in RNA processing as well as transcriptional regulation. Its disease associations include Au-Kline syndrome and syndromic neurodevelopmental disorders, with extensive literature support.
- **Conclusion**: Established evidence supports HNRNPK as a multifunctional RNA-processing and gene-regulatory member of the core. Its links to transcription suggest a possible bridge between RNA processing and broader gene regulation, but that bridge is not demonstrated by this module alone.

#### DHX9

- **Related proteins** (co-abundance neighbors): MATR3 (0.92), HNRNPR (0.81); STRING partners: DDX39B (0.962), HNRNPH1 (0.878), HNRNPK (0.939), HNRNPL (0.901), HNRNPR (0.909), MATR3 (0.786), XRCC6 (0.819)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is a highly connected STRING partner of the principal hnRNP proteins and DDX39B, and it also connects to MATR3 and XRCC6. It contributes to every primary term (7 globally significant GO/KEGG terms, q_global 0.00108–0.0476; see the table) and to multiple STRING RNA-processing categories (6 supplementary STRING terms; within-query FDR 0.0019–0.0166), (4 supplementary STRING terms; within-query FDR 0.0378–0.0386), (STRING Keyword Ubl conjugation; within-query FDR = 0.0386), (STRING Keyword Isopeptide bond; within-query FDR = 0.0386). Its established helicase activity supports unwinding of RNA and DNA-RNA complexes, while its annotations include alternative splicing, transcriptional regulation, and interferon-related biology. It is detected in both tissues and has substantial literature and disease associations.
- **Conclusion**: Established evidence supports DHX9 as an enzymatic RNA-helicase component of the module core. It may help couple RNA remodeling with splicing or export, but the tissue-specific direction and functional consequence of that coupling remain hypotheses.

#### DDX39B

- **Related proteins** (co-abundance neighbors): HNRNPR (0.83), SERPINH1 (0.82); STRING partners: DHX9 (0.962), HNRNPH1 (0.742), HNRNPK (0.808), HNRNPL (0.807), HNRNPR (0.74)
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nuclear speckles; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 39B. This gene encodes a member of the DEAD box family of RNA-dependent ATPases that mediate ATP hydrolysis during pre-mRNA splicing. The encoded protein is an essential splicing factor required for association of U2 small nuclear ribonucleoprotein with pre-mRNA, and it also plays an important role in mRNA export from the nucleus to the cytoplasm. This gene belongs to a cluster of genes localized in th…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); Alzheimer disease (0.522); Parkinson disease (0.503); lysosomal storage disease (0.503); neurodevelopmental disorder (0.413)
- **Europe PMC papers**: 1037
- **Why important**: DDX39B is a spliceosomal RNA-dependent ATPase involved in U2 small nuclear ribonucleoprotein association and nuclear mRNA export. It appears in all primary terms (7 globally significant GO/KEGG terms, q_global 0.00108–0.0476; see the table) and in STRING categories for major-pathway splicing, spliceosomal complex, RNA-binding, and RNA export-related nuclear organization (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0045), (STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.0166), (STRING COMPARTMENTS Spliceosomal complex; within-query FDR = 0.0378), (4 supplementary STRING terms; within-query FDR 0.0378–0.0386). Its strong STRING relationship with DHX9 and connections to the core hnRNP proteins place it at the functional interface between RNA processing and export. It is detected in both tissues and has disease associations involving neurodegeneration and neurodevelopment.
- **Conclusion**: Established evidence supports DDX39B as a core spliceosome and mRNA-export factor. It is a strong candidate for linking transcript maturation to nuclear export, although this module does not prove that export is the principal tissue-level driver.

#### MATR3

- **Related proteins** (co-abundance neighbors): DHX9 (0.92), HNRNPL (0.88), ATP1A1 (0.88), HNRNPK (0.87), XRCC6 (0.81), HNRNPR (0.81); STRING partners: DHX9 (0.786), HNRNPH1 (0.911), HNRNPK (0.923), HNRNPL (0.757), HNRNPR (0.714)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_07581.1, huMAP3_05721.1
- **Function (MyGene.info)**: matrin 3. This gene encodes a nuclear matrix protein, which is proposed to stabilize certain messenger RNA species. Mutations of this gene are associated with distal myopathy 2, which often includes vocal cord and pharyngeal weakness. Alternatively spliced transcript variants, including read-through transcripts composed of the upstream small nucleolar RNA host gene 4 (non-protein coding) and matrin 3 gene s…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.735); distal myopathy with vocal cord weakness (0.569); neurodegenerative disease (0.529); distal myopathy (0.384); hereditary disease (0.193)
- **Europe PMC papers**: 1756
- **Why important**: MATR3 occupies an informative position between the RNA-processing core and other module members. It has STRING relationships with DHX9, HNRNPH1, HNRNPK, HNRNPL, and HNRNPR, and appears in several hu.MAP RNA-associated complexes (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_05721.1). STRING supplementary evidence links it to an mRNA stability complex and RNA-recognition-motif categories (STRING NetworkNeighborAL mRNA processing, and CRD-mediated mRNA stability complex; within-query FDR = 0.0019), (STRING SMART RNA recognition motif; within-query FDR = 0.0205). Its annotation describes a nuclear matrix protein involved in messenger RNA stabilization and post-transcriptional regulation. It is detected in both tissues and has established associations with distal myopathy and amyotrophic lateral sclerosis, supported by substantial literature.
- **Conclusion**: Established evidence supports MATR3 as a nuclear RNA-associated scaffold or stabilizing factor linked to the splicing core. It could connect splicing with RNA stability and muscle-related biology, but that integrative role is a hypothesis rather than a demonstrated property of this module.

## Module 1

**Tissue pair**: cervix_uterine and heart  
**Genes (15)**: ACADVL, AIFM1, CPT2, DSP, HSDL2, IMMT, NDUFA10, NDUFS1, NDUFS2, NNT, PDHB, UQCRC2, OXCT1, SDHA, ALDH5A1

### Function

The module is best interpreted as a mitochondrial energy-metabolism and oxidative-phosphorylation module. The strongest primary evidence is the enrichment of the mitochondrial inner membrane and organelle inner membrane (GO:CC mitochondrial inner membrane; q_global = 0.000751)(GO:CC organelle inner membrane; q_global = 0.00105), with additional support from mitochondrial membrane and envelope terms (GO:CC mitochondrial membrane; q_global = 0.00752)(GO:CC mitochondrial envelope; q_global = 0.0124). Respiratory-chain and aerobic electron-transport terms (GO:CC respiratory chain complex; q_global = 0.0185)(GO:BP aerobic electron transport chain; q_global = 0.0451)(GO:BP ATP synthesis coupled electron transport; q_global = 0.0451)(GO:BP mitochondrial ATP synthesis coupled electron transport; q_global = 0.0451) indicate electron transfer coupled to ATP production. The KEGG associations with diabetic cardiomyopathy, thermogenesis, and non-alcoholic fatty liver disease (KEGG Diabetic cardiomyopathy - Homo sapiens (human); q_global = 0.0211)(KEGG Thermogenesis - Homo sapiens (human); q_global = 0.0319)(KEGG Non-alcoholic fatty liver disease - Homo sapiens (human); q_global = 0.0451) are compatible with altered mitochondrial energy demand, although they should not be interpreted as evidence that the module causes any of those diseases. The broad mitochondrial annotation (GO:CC mitochondrion; q_global = 0.0227), together with the presence of fatty-acid oxidation, ketone utilization, pyruvate entry, redox, and cristae-related genes, suggests coordinated mitochondrial bioenergetics rather than a single narrow pathway.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly mitochondrial. Immune-cell specificity is low for nearly the entire module, so a blood-cell explanation is not supported. HPA detects protein in both cervix and heart, which supports biological presence in both tissues. The frequent tissue-enhanced annotations for tongue, skeletal muscle, heart muscle, and liver, together with cell-type annotations involving myonuclei, cardiomyocytes, hepatocytes, and trophoblasts, suggest metabolically active or mitochondria-rich cell populations. The shared module could therefore reflect a conserved cellular bioenergetic program, while differences in tissue or cell composition could also contribute to the co-abundance pattern.

**GO/KEGG enrichment**: 12 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrial inner membrane | 0.000751 | ACADVL, AIFM1, CPT2, IMMT, NDUFA10, NDUFS1, NDUFS2, NNT, SDHA, UQCRC2 |
| GO:CC organelle inner membrane | 0.00105 | ACADVL, AIFM1, CPT2, IMMT, NDUFA10, NDUFS1, NDUFS2, NNT, SDHA, UQCRC2 |
| GO:CC mitochondrial membrane | 0.00752 | ACADVL, AIFM1, CPT2, IMMT, NDUFA10, NDUFS1, NDUFS2, NNT, SDHA, UQCRC2 |
| GO:CC mitochondrial envelope | 0.0124 | ACADVL, AIFM1, CPT2, IMMT, NDUFA10, NDUFS1, NDUFS2, NNT, SDHA, UQCRC2 |
| GO:CC respiratory chain complex | 0.0185 | NDUFA10, NDUFS1, NDUFS2, NNT, SDHA, UQCRC2 |
| KEGG Diabetic cardiomyopathy - Homo sapiens (human) | 0.0211 | CPT2, NDUFA10, NDUFS1, NDUFS2, PDHB, SDHA, UQCRC2 |
| GO:CC mitochondrion | 0.0227 | ACADVL, AIFM1, ALDH5A1, CPT2, HSDL2, IMMT, NDUFA10, NDUFS1, NDUFS2, NNT, OXCT1, PDHB, SDHA, UQCRC2 |
| KEGG Thermogenesis - Homo sapiens (human) | 0.0319 | CPT2, NDUFA10, NDUFS1, NDUFS2, SDHA, UQCRC2 |
| GO:BP aerobic electron transport chain | 0.0451 | NDUFA10, NDUFS1, NDUFS2, SDHA, UQCRC2 |
| GO:BP ATP synthesis coupled electron transport | 0.0451 | NDUFA10, NDUFS1, NDUFS2, SDHA, UQCRC2 |
| GO:BP mitochondrial ATP synthesis coupled electron transport | 0.0451 | NDUFA10, NDUFS1, NDUFS2, SDHA, UQCRC2 |
| KEGG Non-alcoholic fatty liver disease - Homo sapiens (human) | 0.0451 | NDUFA10, NDUFS1, NDUFS2, SDHA, UQCRC2 |

### STRING and hu.MAP

STRING provides extensive known support for the mitochondrial interpretation, including strong relationships among NDUFA10, NDUFS1, NDUFS2, SDHA, and UQCRC2, as well as links involving IMMT, PDHB, OXCT1, ACADVL, CPT2, and AIFM1. The STRING functional results (STRING Keyword Transit peptide; within-query FDR = 4.58e-05) through (STRING Component Inner mitochondrial membrane protein complex; within-query FDR = 0.0069) consistently point to mitochondria, the inner mitochondrial membrane, respiratory-chain assemblies, and mitochondrial metabolism. These are supplementary network annotations rather than globally corrected enrichment evidence. hu.MAP independently places NDUFS1, NDUFA10, and NDUFS2 together in several respiratory-complex assemblies (hu.MAP huMAP3_14018.1)(hu.MAP huMAP3_06397.1)(hu.MAP huMAP3_09982.1)(hu.MAP huMAP3_09567.1)(hu.MAP huMAP3_14878.1), with additional support for the NDUFS1 and NDUFA10 pair (hu.MAP huMAP3_07653.1)(hu.MAP huMAP3_02819.1). Thus, part of the module recapitulates known physical or functional relationships, especially among respiratory-chain components. The remaining connections may reflect shared mitochondrial localization, coordinated abundance, metabolic coupling, or indirect STRING evidence rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 20 of 105 gene pairs: ACADVL–CPT2 (0.995); ACADVL–HSDL2 (0.787); ALDH5A1–HSDL2 (0.732); IMMT–NDUFS1 (0.901); IMMT–NDUFS2 (0.735); IMMT–UQCRC2 (0.811); NDUFA10–NDUFS1 (0.999); NDUFA10–NDUFS2 (0.999); NDUFA10–SDHA (0.793); NDUFA10–UQCRC2 (0.986); NDUFS1–NDUFS2 (0.999); NDUFS1–PDHB (0.809); NDUFS1–SDHA (0.995); NDUFS1–UQCRC2 (0.998); NDUFS2–SDHA (0.998); NDUFS2–UQCRC2 (0.994); OXCT1–SDHA (0.874); PDHB–SDHA (0.731); PDHB–UQCRC2 (0.905); SDHA–UQCRC2 (0.99)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transit peptide (FDR = 4.58e-05, 13 genes); Keyword Mitochondrion inner membrane (FDR = 0.00018, 9 genes); COMPARTMENTS Mitochondrion (FDR = 0.00029, 14 genes); COMPARTMENTS Mitochondrial inner membrane (FDR = 0.00029, 10 genes); Component Mitochondrial inner membrane (FDR = 0.00036, 10 genes); Keyword Mitochondrion (FDR = 0.00044, 13 genes); Component Mitochondrion (FDR = 0.00067, 14 genes); COMPARTMENTS Mitochondrial respirasome (FDR = 0.00094, 6 genes); Component Mitochondrial respirasome (FDR = 0.0011, 6 genes); DISEASES Mitochondrial metabolism disease (FDR = 0.0032, 8 genes); Component Respiratory chain complex (FDR = 0.0054, 5 genes); Component Oxidoreductase complex (FDR = 0.0054, 6 genes); HPO Acidosis (FDR = 0.0063, 10 genes); HPO Abnormal homeostasis (FDR = 0.0063, 12 genes); Component Inner mitochondrial membrane protein complex (FDR = 0.0069, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14018.1 (NDUFS2, NDUFA10, NDUFS1; 3/48); huMAP3_06397.1 (NDUFS2, NDUFA10, NDUFS1; 3/49); huMAP3_09982.1 (NDUFS2, NDUFA10, NDUFS1; 3/49); huMAP3_09567.1 (NDUFS2, NDUFA10, NDUFS1; 3/52); huMAP3_14878.1 (NDUFS2, NDUFA10, NDUFS1; 3/53); huMAP3_07653.1 (NDUFA10, NDUFS1; 2/7); huMAP3_02819.1 (NDUFA10, NDUFS1; 2/34)

### Novelty

The mitochondrial function itself is not a new biological finding: the globally supported terms, STRING relationships, hu.MAP complexes, gene annotations, and disease knowledge all establish the underlying biology. The potentially novel aspect is the conserved co-abundance module observed across cervix_uterine and heart, particularly the way respiratory-chain, substrate-oxidation, redox, cristae, and structural genes are coordinated in these tissues. However, the fact sheet does not compare this module with prior cross-tissue co-abundance studies or test its reproducibility in independent cohorts. Therefore it should be described as a potentially informative tissue-shared configuration of known mitochondrial biology, not as a demonstrated new pathway or a proven novel protein complex. Lack of hu.MAP or STRING annotation for individual genes would not by itself establish novelty.

**Hypothesis.** Hypothesis: the shared module represents coordinated maintenance of mitochondrial respiratory capacity in metabolically demanding cells of cervix and heart. In this model, complex-I components NDUFS1, NDUFS2, and NDUFA10 cooperate with SDHA and UQCRC2 to support electron transfer, while IMMT helps organize the inner membrane and cristae. CPT2 and ACADVL provide fatty-acid entry and oxidation capacity, PDHB links pyruvate metabolism to the tricarboxylic-acid cycle, OXCT1 supports ketone utilization, and NNT supports mitochondrial reducing power and redox control. The observed co-abundance may therefore arise when cells jointly adjust electron transport, substrate selection, membrane architecture, and oxidative-stress handling. This is a mechanistic interpretation to test, not a causal conclusion from co-abundance alone.

### Important genes

#### NDUFS1

- **Related proteins** (co-abundance neighbors): HSDL2 (0.84), IMMT (0.84), PDHB (0.83), UQCRC2 (0.83), NDUFS2 (0.81); STRING partners: IMMT (0.901), NDUFA10 (0.999), NDUFS2 (0.999), PDHB (0.809), SDHA (0.995), UQCRC2 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1, huMAP3_07653.1, huMAP3_02819.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S1. The protein encoded by this gene belongs to the complex I 75 kDa subunit family. Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Thi…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 5 (0.810); mitochondrial complex I deficiency (0.647); type 2 diabetes mellitus (0.608); Parkinson disease (0.603); diabetes mellitus (0.580)
- **Europe PMC papers**: 2567
- **Why important**: NDUFS1 is a central network hub with links to HSDL2, IMMT, PDHB, UQCRC2, and NDUFS2. It appears in every primary GO and KEGG term listed for the module, including respiratory chain, electron transport, ATP synthesis, and the disease-related pathway terms (GO:CC mitochondrial inner membrane; q_global = 0.000751) through (KEGG Non-alcoholic fatty liver disease - Homo sapiens (human); q_global = 0.0451). It is the largest core subunit of the NADH dehydrogenase complex and participates in multiple hu.MAP assemblies (hu.MAP huMAP3_14018.1) through (hu.MAP huMAP3_02819.1). Its heart- and skeletal-muscle-enhanced HPA profile is also consistent with the tissue context. The gene has substantial disease and literature support involving mitochondrial complex-I deficiency and metabolic disease.
- **Conclusion**: Established: NDUFS1 is a core respiratory-chain component and a major structural and functional connector in this module. Hypothesis: its abundance may help coordinate the respiratory-chain portion of the shared module, but the co-abundance data do not establish that NDUFS1 controls the other genes.

#### NDUFA10

- **Related proteins** (co-abundance neighbors): AIFM1 (0.92), SDHA (0.85); STRING partners: NDUFS1 (0.999), NDUFS2 (0.999), SDHA (0.793), UQCRC2 (0.986)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1, huMAP3_07653.1, huMAP3_02819.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit A10. The protein encoded by this gene is a component of 42 kDa complex I, the first enzyme complex in the electron transport chain of mitochondria. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. A mutation in this gene was found in an individual with Leigh syndrome. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.677); Leigh syndrome (0.674); mitochondrial complex I deficiency, nuclear type 22 (0.668); type 2 diabetes mellitus (0.620); diabetes mellitus (0.578)
- **Europe PMC papers**: 1163
- **Why important**: NDUFA10 has exceptionally strong STRING links to NDUFS1 and NDUFS2 and also connects to SDHA and UQCRC2. It is present in all primary enrichment terms (GO:CC mitochondrial inner membrane; q_global = 0.000751) through (KEGG Non-alcoholic fatty liver disease - Homo sapiens (human); q_global = 0.0451) and in the respiratory-complex hu.MAP assemblies (hu.MAP huMAP3_14018.1) through (hu.MAP huMAP3_02819.1). Its established function is as a complex-I subunit involved in NADH-linked electron transfer and proton-gradient-supported ATP production. Its mitochondrial localization and detection in both tissues support a direct role in the shared mitochondrial signal.
- **Conclusion**: Established: NDUFA10 is a respiratory-chain component whose known interaction and complex evidence strongly support the module interpretation. Hypothesis: coordinated NDUFA10 abundance may mark the amount or assembly state of the complex-I machinery in the two tissues.

#### NDUFS2

- **Related proteins** (co-abundance neighbors): NDUFS1 (0.81); STRING partners: IMMT (0.735), NDUFA10 (0.999), NDUFS1 (0.999), SDHA (0.998), UQCRC2 (0.994)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S2. The protein encoded by this gene is a core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (complex I). Mammalian mitochondrial complex I is composed of at least 43 different subunits, 7 of which are encoded by the mitochondrial genome, and the rest are the products of nuclear genes. The iron-sulfur protein fraction of complex I is made up of 7 subunits, including this g…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.758); mitochondrial complex I deficiency, nuclear type 6 (0.665); type 2 diabetes mellitus (0.608); mitochondrial disease (0.596); Parkinson disease (0.588)
- **Europe PMC papers**: 1723
- **Why important**: NDUFS2 is a core complex-I subunit and is included in every primary GO and KEGG term (GO:CC mitochondrial inner membrane; q_global = 0.000751) through (KEGG Non-alcoholic fatty liver disease - Homo sapiens (human); q_global = 0.0451). It has very strong STRING relationships with NDUFA10, NDUFS1, SDHA, and UQCRC2, and it occurs in several hu.MAP respiratory-complex assemblies (hu.MAP huMAP3_14018.1) through (hu.MAP huMAP3_14878.1). Its disease associations include mitochondrial complex-I deficiency and Parkinson disease, while its HPA localization is mitochondrial and its protein is detected in heart.
- **Conclusion**: Established: NDUFS2 is a well-supported respiratory-chain anchor within the module. Hypothesis: its co-abundance with both complex-I and downstream respiratory components may reflect coordinated assembly or turnover of oxidative-phosphorylation machinery.

#### SDHA

- **Related proteins** (co-abundance neighbors): AIFM1 (0.91), IMMT (0.87), NDUFA10 (0.85), PDHB (0.84); STRING partners: NDUFA10 (0.793), NDUFS1 (0.995), NDUFS2 (0.998), OXCT1 (0.874), PDHB (0.731), UQCRC2 (0.99)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate dehydrogenase complex flavoprotein subunit A. This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identi…
- **Diseases (Open Targets)**: mitochondrial complex II deficiency, nuclear type 1 (0.813); pheochromocytoma/paraganglioma syndrome 5 (0.790); dilated cardiomyopathy 1GG (0.768); neurodegeneration with ataxia and late-onset optic atrophy (0.761); gastrointestinal stromal tumor (0.743)
- **Europe PMC papers**: 12756
- **Why important**: SDHA is a network hub connected to AIFM1, IMMT, NDUFA10, and PDHB, and it has strong STRING links to the main respiratory-chain cluster. It appears in every primary term (GO:CC mitochondrial inner membrane; q_global = 0.000751) through (KEGG Non-alcoholic fatty liver disease - Homo sapiens (human); q_global = 0.0451), including the respiratory-chain, ATP-synthesis, cardiomyopathy, thermogenesis, and fatty-liver pathway terms. SDHA is the catalytic flavoprotein subunit of succinate dehydrogenase, linking the tricarboxylic-acid cycle to electron transport. Its heart- and skeletal-muscle-enhanced HPA profile and extensive disease literature, including respiratory deficiency and cardiomyopathy, make it particularly relevant to the tissue pair.
- **Conclusion**: Established: SDHA links central carbon metabolism to respiratory electron transfer and is one of the strongest functional supports for this module. Hypothesis: SDHA may help couple substrate flux to respiratory capacity in the shared tissue program.

#### IMMT

- **Related proteins** (co-abundance neighbors): SDHA (0.87), NDUFS1 (0.84), NNT (0.81), AIFM1 (0.81), PDHB (0.81); STRING partners: NDUFS1 (0.901), NDUFS2 (0.735), UQCRC2 (0.811)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inner membrane mitochondrial protein. Enables RNA binding activity. Involved in cristae formation. Located in mitochondrial inner membrane. Part of MICOS complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); multinodular goiter (0.196); alcohol drinking (0.190); breast cancer (0.094); neoplasm (0.087)
- **Europe PMC papers**: 933
- **Why important**: IMMT is a high-connectivity module gene linked to SDHA, NDUFS1, NNT, AIFM1, and PDHB. It is included in the primary mitochondrial membrane terms (GO:CC mitochondrial inner membrane; q_global = 0.000751) through (GO:CC mitochondrial envelope; q_global = 0.0124) and in the broad mitochondrial term (GO:CC mitochondrion; q_global = 0.0227). Its established function in the MICOS complex and cristae formation provides a structural explanation for its association with respiratory proteins. STRING links IMMT to NDUFS1, NDUFS2, and UQCRC2, while its mitochondrial protein is detected in both tissues.
- **Conclusion**: Established: IMMT is a mitochondrial inner-membrane and cristae-organization protein that connects membrane architecture with respiratory machinery. Hypothesis: coordinated IMMT abundance may support remodeling or maintenance of cristae needed for efficient respiration.

#### CPT2

- **Related proteins** (co-abundance neighbors): DSP (0.81); STRING partners: ACADVL (0.995)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carnitine palmitoyltransferase 2. The protein encoded by this gene is a nuclear protein which is transported to the mitochondrial inner membrane. Together with carnitine palmitoyltransferase I, the encoded protein oxidizes long-chain fatty acids in the mitochondria. Defects in this gene are associated with mitochondrial long-chain fatty-acid (LCFA) oxidation disorders. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: carnitine palmitoyl transferase II deficiency, myopathic form (0.830); carnitine palmitoyl transferase II deficiency, severe infantile form (0.800); carnitine palmitoyl transferase II deficiency, neonatal form (0.772); carnitine palmitoyltransferase II deficiency (0.710); hereditary disease (0.505)
- **Europe PMC papers**: 5133
- **Why important**: CPT2 provides metabolic breadth beyond the respiratory-chain core. It is linked in STRING to ACADVL and appears in the primary mitochondrial membrane, diabetic-cardiomyopathy, thermogenesis, and broad mitochondrial terms (GO:CC mitochondrial inner membrane; q_global = 0.000751)(GO:CC organelle inner membrane; q_global = 0.00105)(GO:CC mitochondrial membrane; q_global = 0.00752)(GO:CC mitochondrial envelope; q_global = 0.0124)(KEGG Diabetic cardiomyopathy - Homo sapiens (human); q_global = 0.0211)(GO:CC mitochondrion; q_global = 0.0227)(KEGG Thermogenesis - Homo sapiens (human); q_global = 0.0319). Its established role in the carnitine shuttle and long-chain fatty-acid oxidation is especially relevant to heart energy metabolism. Its disease associations include several forms of CPT2 deficiency, and its protein is detected in both tissues.
- **Conclusion**: Established: CPT2 connects the module to mitochondrial fatty-acid utilization and has a well-established metabolic disease relationship. Hypothesis: CPT2 may indicate that the shared module coordinates respiratory capacity with lipid-derived substrate supply, although its lower network connectivity makes this interpretation less direct than for the respiratory chain hubs.

## Module 2

**Tissue pair**: cervix_uterine and heart  
**Genes (12)**: AHNAK, GPS1, DNM1L, DYNC1H1, IQGAP1, PLS3, PSMD13, SPTAN1, QARS1, TGM2, USO1, XPO1

### Function

No GO or KEGG term passed global correction, so the module has no globally significant pathway annotation. Its gene composition nevertheless points to a shared cellular infrastructure program involving cytoskeletal and membrane organization, intracellular transport, organelle dynamics, proteostasis, vesicle trafficking, nuclear export, and signal regulation. AHNAK, SPTAN1, IQGAP1, and PLS3 support a structural or membrane-associated component; DNM1L supports mitochondrial and peroxisomal dynamics; USO1 supports ER-to-Golgi trafficking; PSMD13 and XPO1 support protein quality control and nucleocytoplasmic transport; and QARS1 supports core protein translation. The weak functional convergence should be treated as an interpretation of the gene functions and network structure, not as enrichment evidence. The absence of a globally significant term does not invalidate the module.

**Cell composition.** This does not appear to be primarily a plasma-protein, secreted-protein, or blood-cell module. Only TGM2 is annotated as secreted to the extracellular matrix, while the other genes are intracellular or membrane-associated. HPA reports low immune-cell specificity for most genes; PLS3 is group-enriched in NK cells and plasmacytoid dendritic cells, but the module as a whole is not blood-cell enriched. Most genes have low tissue specificity and are detected in both cervix and heart, consistent with broadly expressed cellular machinery rather than a tissue-exclusive program. Several genes show cell-type-enhanced expression in epithelial, vascular, neural, reproductive, or muscle-related populations, so shared stromal, vascular, epithelial, or other common cell populations could contribute to the cross-tissue signal. The HPA protein data support broad detectability in both tissues, with USO1 being detected in cervix but not heart and limited missing or undetected measurements elsewhere.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, IQGAP1-SPTAN1, indicating prior support for a cytoskeletal or membrane-associated connection. No STRING functional-enrichment result was reported. hu.MAP provides the complex association (hu.MAP huMAP3_09165.1), in which AHNAK and SPTAN1 occur together, but they represent only a small part of a much larger complex whose other members are outside this module. Thus, the module contains some previously recognized structural relationships, but most of its co-abundance edges are not supported by the supplied STRING or hu.MAP evidence. The co-abundance network should therefore not be interpreted as a physical interaction map.

**STRING interactions (score >= 0.7)**: 1 of 66 gene pairs: IQGAP1–SPTAN1 (0.753)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09165.1 (AHNAK, SPTAN1; 2/39)

### Novelty

The module may represent a new cross-tissue co-abundance pattern, but the fact sheet is insufficient to establish a new molecular complex or mechanism. Its novelty is supported only in the limited sense that the particular conserved association between cervix and heart, including genes with roles spanning cytoskeletal organization, organelle dynamics, trafficking, proteostasis, and translation, is not directly documented here as a known module. Sparse STRING support and the lack of hu.MAP membership for most genes suggest that the complete configuration is not already captured by the supplied interaction resources, but database absence alone does not prove novelty. A stronger novelty claim would require comparison with published tissue co-expression modules, independent cohorts, preservation statistics, and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a shared structural and logistical state of cells present in both cervix and heart. A membrane-cytoskeleton scaffold involving AHNAK, SPTAN1, IQGAP1, and PLS3 may coordinate cell shape, adhesion, and membrane organization, while DNM1L supports organelle remodeling and USO1 supports secretory-pathway trafficking. TGM2 may connect intracellular stress or remodeling signals to extracellular-matrix organization, with PSMD13, XPO1, GPS1, and QARS1 maintaining proteostasis, nuclear-cytoplasmic exchange, signaling regulation, and protein synthesis. This is a mechanistic model rather than an established pathway assignment, and it should be tested by perturbing the structural and trafficking genes separately in relevant cervix and cardiac cell populations.

### Important genes

#### AHNAK

- **Related proteins** (co-abundance neighbors): DNM1L (0.84), IQGAP1 (0.83), PLS3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: huMAP3_09165.1
- **Function (MyGene.info)**: AHNAK nucleoprotein. The protein encoded by this gene is a large (700 kDa) structural scaffold protein consisting of a central domain with 128 aa repeats. The encoded protein may play a role in such diverse processes as blood-brain barrier formation, cell structure and migration, cardiac calcium channel regulation, and tumor metastasis. A much shorter variant encoding a 17 kDa isoform exists for this gene, and the sho…
- **Diseases (Open Targets)**: Aganglionic megacolon (0.266); neoplasm (0.108); hepatocellular carcinoma (0.093); cancer (0.085); melanoma (0.085)
- **Europe PMC papers**: 2886
- **Why important**: AHNAK is a central connector in the module and links DNM1L, IQGAP1, and PLS3, placing it at the interface of organelle dynamics, membrane signaling, and the actin-associated scaffold. It is detected in both tissues, has plasma-membrane and cytosolic localization, and is the module member participating with SPTAN1 in the hu.MAP association (hu.MAP huMAP3_09165.1). Its annotated functions include plasma-membrane repair and structural or migratory processes, and it has substantial literature addressing cancer and tissue structure.
- **Conclusion**: Established evidence supports AHNAK as a large structural scaffold with membrane-related functions and as a participant in (hu.MAP huMAP3_09165.1). Its central position makes it a plausible organizing gene for the module. It remains a hypothesis that AHNAK coordinates the entire cross-tissue module or directly links mitochondrial dynamics to membrane repair.

#### DNM1L

- **Related proteins** (co-abundance neighbors): SPTAN1 (0.86), QARS1 (0.85), AHNAK (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 1L. This gene encodes a member of the dynamin superfamily of GTPases. The encoded protein mediates mitochondrial and peroxisomal division, and is involved in developmentally regulated apoptosis and programmed necrosis. Dysfunction of this gene is implicated in several neurological disorders, including Alzheimer's disease. Mutations in this gene are associated with the autosomal dominant disorder, ence…
- **Diseases (Open Targets)**: encephalopathy, lethal, due to defective mitochondrial peroxisomal fission 1 (0.815); autosomal dominant optic atrophy, classic form (0.721); neurodegenerative disease (0.531); encephalopathy due to mitochondrial and peroxisomal fission defect (0.455); hereditary disease (0.451)
- **Europe PMC papers**: 3015
- **Why important**: DNM1L is among the most connected module genes and bridges SPTAN1, QARS1, and AHNAK. Its established function in mitochondrial and peroxisomal fission provides a strong organelle-dynamics axis for interpreting the module. It is detected in both tissues and has extensive literature and disease evidence, including disorders caused by defective mitochondrial and peroxisomal fission.
- **Conclusion**: Established evidence supports DNM1L as a core regulator of organelle division and a biologically important module member. Its network placement suggests that organelle remodeling may be coupled to the structural machinery represented by AHNAK and SPTAN1. The proposed coupling is a hypothesis because the supplied interaction resources do not establish direct physical relationships for most of these edges.

#### TGM2

- **Related proteins** (co-abundance neighbors): PSMD13 (0.83), XPO1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transglutaminase 2. Transglutaminases are enzymes that catalyze the crosslinking of proteins by epsilon-gamma glutamyl lysine isopeptide bonds. While the primary structure of transglutaminases is not conserved, they all have the same amino acid sequence at their active sites and their activity is calcium-dependent. The protein encoded by this gene acts as a monomer, is induced by retinoic acid, and appears to be invo…
- **Diseases (Open Targets)**: neurodegenerative disease (0.495); autoimmune disorder of central nervous system (0.324); placental abruption (0.297); arterial embolism (0.266); seborrheic dermatitis (0.251)
- **Europe PMC papers**: 4586
- **Why important**: TGM2 connects PSMD13 and XPO1 and is the clearest extracellular-matrix-facing gene in the module. HPA describes it as tissue-enhanced in blood vessel, secreted to extracellular matrix, and detected in both tissues. Its transglutaminase activity, roles in extracellular-matrix organization and apoptosis, and substantial disease literature make it important for linking intracellular stress and remodeling to the extracellular environment.
- **Conclusion**: Established evidence supports TGM2 as a calcium-dependent crosslinking enzyme with extracellular-matrix and apoptosis-related functions. It may provide a vascular or matrix-related explanation for part of the shared cervix-heart signal. It is not established that TGM2 is the driver of the module or that its association with PSMD13 and XPO1 represents a direct mechanistic chain.

#### SPTAN1

- **Related proteins** (co-abundance neighbors): DNM1L (0.86); STRING partners: IQGAP1 (0.753)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Microtubules; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: huMAP3_09165.1
- **Function (MyGene.info)**: spectrin alpha, non-erythrocytic 1. Spectrins are a family of filamentous cytoskeletal proteins that function as essential scaffold proteins that stabilize the plasma membrane and organize intracellular organelles. Spectrins are composed of alpha and beta dimers that associate to form tetramers linked in a head-to-head arrangement. This gene encodes an alpha spectrin that is specifically expressed in nonerythrocytic cells. The encod…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 5 (0.749); developmental delay with or without epilepsy (0.681); spastic paraplegia 91, autosomal dominant, with or without cerebellar ataxia (0.681); infantile spasms (0.651); genetic developmental and epileptic encephalopathy (0.651)
- **Europe PMC papers**: 1422
- **Why important**: SPTAN1 is a membrane and organelle scaffold with a direct high-confidence STRING relationship to IQGAP1 and participation with AHNAK in (hu.MAP huMAP3_09165.1). It connects to DNM1L in the module and is detected in both tissues. Its established role in stabilizing membranes and organizing intracellular structures, together with extensive neurological disease literature, makes it a strong structural anchor.
- **Conclusion**: Established evidence supports SPTAN1 as a non-erythrocytic spectrin involved in cytoskeletal organization and membrane stability, with independent support from STRING and hu.MAP. It is a plausible structural backbone for the module. Whether its co-abundance with DNM1L reflects coordinated organelle organization rather than shared expression remains a hypothesis.

#### IQGAP1

- **Related proteins** (co-abundance neighbors): AHNAK (0.83); STRING partners: SPTAN1 (0.753)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IQ motif containing GTPase activating protein 1. This gene encodes a member of the IQGAP family. The protein contains four IQ domains, one calponin homology domain, one Ras-GAP domain and one WW domain. It interacts with components of the cytoskeleton, with cell adhesion molecules, and with several signaling molecules to regulate cell morphology and motility. Expression of the protein is upregulated by gene amplification in two gastric cancer ce…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.515); Costello syndrome (0.503); allergic rhinitis (0.474)
- **Europe PMC papers**: 3787
- **Why important**: IQGAP1 participates in the module’s only high-confidence STRING relationship, with SPTAN1. It is localized to the plasma membrane and cell junctions and has established roles in cytoskeletal regulation, cell adhesion, cell morphology, motility, and receptor-linked signaling. Its disease associations and substantial literature further support its importance despite its peripheral position in the module graph.
- **Conclusion**: Established evidence supports IQGAP1 as a membrane-associated cytoskeletal and signaling scaffold, and the IQGAP1-SPTAN1 relationship is supported by STRING. It may connect cell-junction organization to the spectrin scaffold in the shared module. A role for IQGAP1 in coordinating the full module, or in explaining the cervix-heart conservation, remains a hypothesis.

## Module 3

**Tissue pair**: cervix_uterine and heart  
**Genes (25)**: APMAP, CAPN1, CAPN2, CLTC, DNM2, GANAB, GSN, GPD2, MACROH2A1, HK1, ITGB1, LMNB2, MYO1C, PDCD6IP, PDLIM1, PPP1CB, RO60, SEC23A, SEPTIN2, SEPTIN9, SPTBN1, DARS1, USP5, VPS35, WDR1

### Function

The module is most consistent with a broadly expressed cytoskeletal and membrane-trafficking program linking cell adhesion, actin organization, vesicle transport, endocytosis, and calcium-regulated proteolysis. ITGB1 is the main network hub and connects adhesion-related membrane organization with calpains, septins, dynamin, and other cytoskeletal proteins. CAPN1 and CAPN2 provide a coherent calpain proteolytic component, while SEPTIN2, SEPTIN9, DNM2, CLTC, MYO1C, SPTBN1, WDR1, and GSN support cytoskeletal remodeling and membrane dynamics. PDCD6IP, SEC23A, VPS35, and GANAB provide additional vesicle, endosomal, and secretory-pathway context. No GO or KEGG term passed global correction; therefore the functional interpretation is based on the gene annotations, network structure, and interaction evidence rather than on statistically significant pathway enrichment.

**Cell composition.** The module is not dominated by secreted or plasma proteins: only a minority are annotated as secreted, and most proteins are intracellular or membrane-associated. HPA indicates low tissue specificity for most genes, with a small set showing tissue enhancement in liver, esophagus, heart muscle, or skeletal muscle. Many genes are cell-type enhanced, including signals in esophageal cells, neutrophils, platelets, trophoblasts, and other cell types, but overall blood-cell specificity is mostly low. The module could therefore reflect a shared, broadly used structural and trafficking program, with possible contribution from shared cell populations or sample composition rather than a cervix-and-heart-specific mechanism. Protein detection is broadly compatible with the module in cervix and somewhat less complete in heart, so absence of immunohistochemical detection for selected genes should not be treated as absence of the module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a small set of high-confidence pairwise relationships within the module: CAPN1 with CAPN2, CLTC with DNM2, and SEPTIN2 with SEPTIN9. These relationships independently support calpain activity, clathrin-mediated membrane dynamics, and septin organization, but the sparse STRING connectivity means that most co-abundance edges are not established physical interactions in STRING. hu.MAP gives repeated support for a CAPN1-CAPN2 component across complexes C1 through C10, usually with CAPNS1 and sometimes CAPN8, CAST, FNTB, or related proteins. Complex C11 supports a septin component containing SEPTIN2 and SEPTIN9. Complex C12 places WDR1 and SPTBN1 in a larger actin and membrane-associated assembly, while C13 places CLTC and SEC23A in a broad trafficking-related complex. These results suggest that parts of the module recapitulate known molecular assemblies, whereas the full module is a higher-level co-abundance neighborhood rather than one established single complex.

**STRING interactions (score >= 0.7)**: 3 of 300 gene pairs: CAPN1–CAPN2 (0.978); CLTC–DNM2 (0.911); SEPTIN2–SEPTIN9 (0.997)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03767.1 (CAPN1, CAPN2; 2/3); huMAP3_08670.1 (CAPN1, CAPN2; 2/4); huMAP3_09127.1 (CAPN1, CAPN2; 2/5); huMAP3_09328.1 (CAPN1, CAPN2; 2/6); huMAP3_10242.1 (CAPN1, CAPN2; 2/6); huMAP3_13615.1 (CAPN1, CAPN2; 2/7); huMAP3_14229.1 (CAPN1, CAPN2; 2/7); huMAP3_11557.1 (CAPN1, CAPN2; 2/8); huMAP3_12716.1 (CAPN1, CAPN2; 2/8); huMAP3_12926.1 (CAPN1, CAPN2; 2/8); huMAP3_02362.1 (SEPTIN2, SEPTIN9; 2/14); huMAP3_09165.1 (WDR1, SPTBN1; 2/39); huMAP3_12394.1 (CLTC, SEC23A; 2/98)

### Novelty

The module should not be claimed as a wholly new molecular discovery. Its strongest internal relationships and several of its complexes are already represented in STRING or hu.MAP, and the functions of its central proteins are well established. The potentially novel aspect is the coordinated co-abundance of these adhesion, cytoskeletal, proteolytic, and trafficking components across cervix and heart. However, the fact sheet does not provide an external replication cohort, perturbation experiment, disease association specific to this module, or a direct comparison with previously reported tissue-pair modules. Absence of STRING or hu.MAP support for individual edges would not establish novelty. The appropriate conclusion is a potentially informative tissue-pair co-abundance pattern built partly from known biology, requiring independent validation before being described as novel.

**Hypothesis.** Hypothesis: the shared module reflects a conserved membrane–cytoskeleton remodeling state present in cells from both tissues. ITGB1 may organize adhesion and focal-adhesion-associated signaling, while septins and spectrin-related proteins stabilize or reorganize cortical actin. DNM2, CLTC, SEC23A, PDCD6IP, and VPS35 may coordinate endocytosis, vesicle budding, recycling, and endosomal routing. Calcium-dependent activation of CAPN1 and CAPN2 could remodel adhesion and cytoskeletal substrates, with WDR1 and GSN contributing actin turnover. This state may support mechanical adaptation, cell shape, membrane turnover, and tissue maintenance. A competing explanation is that the pattern is partly driven by shared vascular, epithelial, platelet, or other cell-type contributions in bulk tissue samples; cell-resolved expression and independent cohorts are needed to distinguish these possibilities.

### Important genes

#### ITGB1

- **Related proteins** (co-abundance neighbors): USP5 (0.91), SEPTIN9 (0.89), MYO1C (0.88), CAPN1 (0.86), CAPN2 (0.85), APMAP (0.84), DNM2 (0.84), SEPTIN2 (0.83), SPTBN1 (0.82), PDLIM1 (0.82), CLTC (0.82), GANAB (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is the strongest network hub in the supplied subgraph and connects many of the module’s major branches, including CAPN1, CAPN2, SEPTIN2, SEPTIN9, DNM2, MYO1C, and APMAP. It is a plasma-membrane and focal-adhesion integrin subunit with established roles in cell adhesion, tissue repair, hemostasis, immune response, angiogenesis, and phagocytosis. Its extensive literature and disease associations make it the clearest candidate for linking co-abundance to adhesion and mechanosensitive membrane organization. HPA shows broad tissue distribution and cell-type enhancement rather than a sharply cervix- or heart-specific pattern.
- **Conclusion**: Established evidence supports ITGB1 as a central adhesion and membrane-organizing component of the module. It is plausible, but not demonstrated, that ITGB1-centered adhesion signaling explains the shared co-abundance pattern.

#### CAPN1

- **Related proteins** (co-abundance neighbors): APMAP (0.91), WDR1 (0.87), ITGB1 (0.86), PDCD6IP (0.83), VPS35 (0.82), HK1 (0.82); STRING partners: CAPN2 (0.978)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: huMAP3_03767.1, huMAP3_08670.1, huMAP3_09127.1, huMAP3_09328.1, huMAP3_10242.1, huMAP3_13615.1, huMAP3_14229.1, huMAP3_11557.1, huMAP3_12716.1, huMAP3_12926.1
- **Function (MyGene.info)**: calpain 1. The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpa…
- **Diseases (Open Targets)**: Autosomal recessive spastic paraplegia type 76 (0.781); Alzheimer disease (0.383); neurodegenerative disease (0.326); hereditary spastic paraplegia 11 (0.266); hereditary disease (0.193)
- **Europe PMC papers**: 1869
- **Why important**: CAPN1 is a highly connected module member and forms the strongest STRING-supported pair with CAPN2. It is the catalytic large subunit of ubiquitous calpain, an intracellular calcium-activated cysteine protease. It also connects in the module to ITGB1, WDR1, PDCD6IP, VPS35, APMAP, and HK1, linking proteolysis with adhesion, actin remodeling, trafficking, and metabolism. CAPN1 has established disease associations including hereditary spastic paraplegia and neurodegenerative disease, and it is detected by HPA in both sampled tissues.
- **Conclusion**: Established evidence supports CAPN1 as a mechanistically coherent proteolytic regulator within the module. Its role as a calcium-responsive mediator of the proposed tissue-remodeling state remains a hypothesis in this tissue-pair context.

#### SEPTIN2

- **Related proteins** (co-abundance neighbors): SEPTIN9 (0.89), RO60 (0.87), LMNB2 (0.84), PPP1CB (0.83), ITGB1 (0.83), SEC23A (0.80); STRING partners: SEPTIN9 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Actin filaments; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: huMAP3_02362.1
- **Function (MyGene.info)**: septin 2. Enables identical protein binding activity. Predicted to be involved in several processes, including cilium assembly; regulation of exocytosis; and smoothened signaling pathway. Predicted to act upstream of or within regulation of L-glutamate import across plasma membrane and regulation of protein localization. Located in several cellular components, including cytoskeleton; photoreceptor connectin…
- **Diseases (Open Targets)**: hypothyroidism (0.239); squamous cell carcinoma (0.201); ischemic stroke (0.189); coronary artery disorder (0.181); skin cancer (0.181)
- **Europe PMC papers**: 281
- **Why important**: SEPTIN2 is a network connector between SEPTIN9, ITGB1, SEC23A, LMNB2, RO60, and PPP1CB. STRING strongly supports its relationship with SEPTIN9, and hu.MAP complex C11 places both proteins in a septin assembly. Septin biology supports cytoskeleton organization, intracellular localization, cytokinesis, cilium assembly, and exocytosis. SEPTIN2 is detected in both cervix and heart by HPA and has disease associations including ischemic stroke and coronary artery disorder, although these associations do not establish a causal role here.
- **Conclusion**: Established evidence supports SEPTIN2 as a structural cytoskeletal and membrane-organization component, together with SEPTIN9. Its contribution to a shared mechanical or trafficking state across the two tissues is a plausible but untested interpretation.

#### DNM2

- **Related proteins** (co-abundance neighbors): SEPTIN9 (0.85), ITGB1 (0.84), APMAP (0.82), GPD2 (0.82); STRING partners: CLTC (0.911)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 2. Dynamins represent one of the subfamilies of GTP-binding proteins. These proteins share considerable sequence similarity over the N-terminal portion of the molecule, which contains the GTPase domain. Dynamins are associated with microtubules. They have been implicated in cell processes such as endocytosis and cell motility, and in alterations of the membrane that accompany certain activities such …
- **Diseases (Open Targets)**: autosomal dominant centronuclear myopathy (0.844); Charcot-Marie-Tooth disease dominant intermediate B (0.830); fetal akinesia-cerebral and retinal hemorrhage syndrome (0.739); autosomal dominant Charcot-Marie-Tooth disease type 2M (0.715); centronuclear myopathy (0.692)
- **Europe PMC papers**: 2412
- **Why important**: DNM2 links the module’s membrane and cytoskeletal branches and has a high-confidence STRING relationship with CLTC. Its established functions include GTPase-dependent membrane remodeling, endocytosis, receptor-mediated endocytosis, post-Golgi transport, and autophagy. It is connected in the module to ITGB1, SEPTIN9, APMAP, and GPD2, and HPA detects it in both tissues. DNM2 also has strong disease associations with centronuclear myopathy and Charcot-Marie-Tooth disease, making it particularly relevant to membrane mechanics and muscle-related tissue biology.
- **Conclusion**: Established evidence supports DNM2 as a membrane fission and trafficking component that can connect adhesion and cytoskeletal organization. Its specific role in generating the cross-tissue co-abundance signal is a hypothesis.

#### GSN

- **Related proteins** (co-abundance neighbors): HK1 (0.91); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gelsolin. The protein encoded by this gene binds to the 'plus' ends of actin monomers and filaments to prevent monomer exchange. The encoded calcium-regulated protein functions in both assembly and disassembly of actin filaments. Defects in this gene are a cause of familial amyloidosis Finnish type (FAF). Multiple transcript variants encoding several different isoforms have been found for this gene. [provid…
- **Diseases (Open Targets)**: Finnish type amyloidosis (0.805); AL amyloidosis (0.463); neuropathy (0.418); cardiomyopathy (0.418); cutis laxa (0.417)
- **Europe PMC papers**: 5062
- **Why important**: GSN is a lower-degree module member but provides a biologically important actin-remodeling and extracellular dimension. It regulates actin filament assembly and disassembly, is tissue-enhanced in heart muscle, and is annotated as secreted to blood. Its HPA profile includes immune-cell enhancement in eosinophils, while its disease associations include Finnish-type amyloidosis, AL amyloidosis, neuropathy, and cardiomyopathy. The combination of heart enhancement, actin regulation, and blood secretion makes GSN useful for evaluating whether the module reflects tissue structure, circulating material, or both.
- **Conclusion**: Established evidence supports GSN as an actin-regulatory protein with a possible blood-derived contribution to bulk tissue measurements. Whether it is a functional driver of the module or a compositional marker cannot be determined from co-abundance alone.

#### WDR1

- **Related proteins** (co-abundance neighbors): CAPN1 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions, Cytosol; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: huMAP3_09165.1
- **Function (MyGene.info)**: WD repeat domain 1. This gene encodes a protein containing 9 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, mostly including a trp-asp at the C-terminal end. WD domains are involved in protein-protein interactions. The encoded protein may help induce the disassembly of actin filaments. Two transcript variants encoding different isoforms have been found for…
- **Diseases (Open Targets)**: periodic fever, immunodeficiency, and thrombocytopenia syndrome (0.705); gout (0.528); neurodegenerative disease (0.526); atrial fibrillation (0.519); intellectual developmental disorder 61 (0.416)
- **Europe PMC papers**: 1861
- **Why important**: WDR1 connects directly to CAPN1 and is included with SPTBN1 in hu.MAP complex C12, which contains many actin, membrane, and signaling proteins. Its established functions include actin filament depolymerization, cortical cytoskeleton organization, platelet formation, and neutrophil-mediated immunity. HPA also identifies cell-type enhancement in megakaryocytes and platelets. WDR1 therefore provides a bridge between the proposed actin-remodeling mechanism and the possibility of platelet or other cell-type contribution.
- **Conclusion**: Established evidence supports WDR1 as an actin-disassembly and cytoskeletal-regulatory component. Its platelet and immune-cell annotations make sample composition an important alternative explanation for part of the module signal.

## Module 4

**Tissue pair**: cervix_uterine and heart  
**Genes (18)**: BAG2, HSPA5, TSFM, GET3, SHMT2, HSP90AA1, IMPDH2, CAMK2D, PANK4, PFKP, PGK1, PSMC4, PSMC2, KARS1, CCT5, CCT3, CCT7, CCT8

### Function

This is most consistent with a conserved intracellular proteostasis and protein-quality-control module, coupled to cellular energy and nucleotide metabolism. The strongest primary evidence is ATP and nucleotide binding across much of the module (5 globally significant GO/KEGG terms, q_global 2.14e-05–0.000309; see the table), ATP-dependent hydrolysis (GO:MF ATP hydrolysis activity; q_global = 0.000339), ATP-dependent protein folding chaperone activity (GO:MF ATP-dependent protein folding chaperone; q_global = 0.000346), protein folding and unfolded-protein binding (GO:MF protein folding chaperone; q_global = 0.000823), (GO:BP protein folding; q_global = 0.00655), (GO:MF unfolded protein binding; q_global = 0.0185), and intracellular protein-containing complexes (GO:CC intracellular protein-containing complex; q_global = 0.0024). The CCT subunits CCT3, CCT5, CCT7, and CCT8 form the clearest functional core, supported by the chaperonin-containing T-complex annotation (GO:CC chaperonin-containing T-complex; q_global = 0.00614) and the CCT-related STRING and hu.MAP evidence. HSP90AA1, HSPA5, and BAG2 extend this toward chaperone-assisted folding, protein stabilization, and stress handling (GO:BP protein folding; q_global = 0.00655), (GO:BP protein maturation; q_global = 0.0167), (GO:CC protein folding chaperone complex; q_global = 0.0174), (GO:BP protein stabilization; q_global = 0.0484). PSMC2 and PSMC4 add proteasomal ATPase and protein-degradation capacity, while PGK1, PFKP, SHMT2, IMPDH2, KARS1, TSFM, and CAMK2D indicate links to glycolysis, one-carbon metabolism, nucleotide production, translation, mitochondrial function, and calcium-dependent signaling. The telomere, Cajal-body, DNA-biosynthetic, and reproductive terms (9 globally significant GO/KEGG terms, q_global 0.000408–0.000408; see the table), (GO:BP regulation of telomere maintenance; q_global = 0.00163) (GO:BP positive regulation of telomere maintenance; q_global = 0.00163) (GO:BP DNA biosynthetic process; q_global = 0.00163), (11 globally significant GO/KEGG terms, q_global 0.00435–0.00614; see the table), (GO:BP telomere organization; q_global = 0.0094) (GO:BP positive regulation of DNA metabolic process; q_global = 0.0094), and (6 globally significant GO/KEGG terms, q_global 0.0215–0.0215; see the table) are globally corrected primary annotations, but they are concentrated in the CCT paralogs and should be interpreted as compatible with chaperone support of nuclear and telomerase-related processes rather than proof that the whole module is a dedicated telomere module. The sperm and fertilization annotations (GO:BP binding of sperm to zona pellucida; q_global = 0.0215), (GO:BP sperm-egg recognition; q_global = 0.0215), (GO:BP single fertilization; q_global = 0.0493), and (GO:BP cell-cell recognition; q_global = 0.0493) likewise appear to reflect annotation properties of the CCT genes and are not sufficient to assign a reproductive function to the conserved tissue module.

**Cell composition.** The module is not dominated by plasma proteins or classical secreted proteins. Most members have low tissue specificity and low immune-cell specificity, and the HPA summary indicates only a small secreted component. Protein detection is widespread in both cervix_uterine and heart, supporting a shared intracellular signal rather than a simple plasma carryover explanation. The module is also not strongly blood-cell enriched; the broad HPA profile argues against an eosinophil or other blood-cell contamination model, although PANK4 has an immune-cell-enhanced eosinophil annotation and should be treated cautiously. The frequent single-cell annotations for spermatocytes, spermatids, oocytes, and trophoblast-related cells probably reflect cell-type-specific expression or annotation structure rather than a shared reproductive cell population in these tissues. CAMK2D is heart-enhanced and cardiomyocyte-associated, while SHMT2 is liver-enhanced and absent by HPA protein detection in heart. Overall, the composition is mainly broadly expressed housekeeping and proteostasis machinery, with a few tissue- or cell-contextualized metabolic and signaling genes.

**GO/KEGG enrichment**: 62 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF ATP binding | 2.14e-05 | CAMK2D, CCT3, CCT5, CCT7, CCT8, GET3, HSP90AA1, HSPA5, KARS1, PANK4, PFKP, PGK1, PSMC2, PSMC4 |
| GO:MF adenyl ribonucleotide binding | 2.14e-05 | CAMK2D, CCT3, CCT5, CCT7, CCT8, GET3, HSP90AA1, HSPA5, KARS1, PANK4, PFKP, PGK1, PSMC2, PSMC4 |
| GO:MF ribonucleotide binding | 0.000309 | CAMK2D, CCT3, CCT5, CCT7, CCT8, GET3, HSP90AA1, HSPA5, KARS1, PANK4, PFKP, PGK1, PSMC2, PSMC4 |
| GO:MF purine ribonucleotide binding | 0.000309 | CAMK2D, CCT3, CCT5, CCT7, CCT8, GET3, HSP90AA1, HSPA5, KARS1, PANK4, PFKP, PGK1, PSMC2, PSMC4 |
| GO:MF purine ribonucleoside triphosphate binding | 0.000309 | CAMK2D, CCT3, CCT5, CCT7, CCT8, GET3, HSP90AA1, HSPA5, KARS1, PANK4, PFKP, PGK1, PSMC2, PSMC4 |
| GO:MF ATP hydrolysis activity | 0.000339 | CCT3, CCT5, CCT7, CCT8, GET3, HSP90AA1, HSPA5, PSMC2, PSMC4 |
| GO:MF ATP-dependent protein folding chaperone | 0.000346 | CCT3, CCT5, CCT7, CCT8, HSP90AA1, HSPA5 |
| GO:MF adenyl nucleotide binding | 0.000355 | CAMK2D, CCT3, CCT5, CCT7, CCT8, GET3, HSP90AA1, HSPA5, KARS1, PANK4, PFKP, PGK1, PSMC2, PSMC4 |
| GO:BP RNA-templated DNA biosynthetic process | 0.000408 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP telomere maintenance via telomerase | 0.000408 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP telomere maintenance via telomere lengthening | 0.000408 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP regulation of telomere maintenance via telomerase | 0.000408 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP positive regulation of telomere maintenance via telomerase | 0.000408 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP regulation of telomere maintenance via telomere lengthening | 0.000408 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |
| GO:BP positive regulation of telomere maintenance via telomere lengthening | 0.000408 | CCT3, CCT5, CCT7, CCT8, HSP90AA1 |

### STRING and hu.MAP

STRING supports a known CCT chaperonin core: CCT3, CCT5, CCT7, and CCT8 are mutually strongly connected, and they connect to HSP90AA1 and HSPA5 (6 supplementary STRING terms; within-query FDR 0.00016–0.0091). STRING also supports the HSP90AA1–HSPA5 chaperone relationship, the PSMC2–PSMC4 proteasome ATPase pair, the KARS1–TSFM translation-related pair, and the PFKP–PGK1 glycolytic pair. These relationships indicate that the co-abundance structure contains established molecular machinery rather than only statistical associations. hu.MAP independently places the CCT quartet in several CCT- and chaperonin-related complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), and places PSMC2 with PSMC4 in proteasome-related complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). However, hu.MAP has no listed complex for SHMT2, IMPDH2, CAMK2D, HSPA5, HSP90AA1, or most of the metabolic and translation-related links. STRING also lacks high-confidence listed links for several of these genes. Thus, the module combines a well-established chaperonin and proteasome backbone with tissue-level co-abundance relationships whose direct physical interactions remain uncertain.

**STRING interactions (score >= 0.7)**: 21 of 153 gene pairs: BAG2–HSP90AA1 (0.732); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT3–HSP90AA1 (0.767); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT5–HSP90AA1 (0.868); CCT5–HSPA5 (0.727); CCT7–CCT8 (0.999); CCT7–HSP90AA1 (0.849); CCT7–HSPA5 (0.783); CCT7–IMPDH2 (0.758); CCT8–HSP90AA1 (0.823); CCT8–HSPA5 (0.701); CCT8–PSMC2 (0.733); HSP90AA1–HSPA5 (0.968); HSP90AA1–PGK1 (0.713); KARS1–TSFM (0.809); PFKP–PGK1 (0.841); PSMC2–PSMC4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Adenyl nucleotide binding (FDR = 2.08e-06, 15 genes); Keyword ATP-binding (FDR = 3.78e-06, 14 genes); Function ATP binding (FDR = 5.64e-06, 14 genes); Function Small molecule binding (FDR = 9.81e-06, 17 genes); Function Nucleotide binding (FDR = 1.74e-05, 16 genes); Function ATP hydrolysis activity (FDR = 2.24e-05, 9 genes); Function Anion binding (FDR = 5.55e-05, 15 genes); Function Heterocyclic compound binding (FDR = 6.6e-05, 18 genes); Function Organic cyclic compound binding (FDR = 8.13e-05, 18 genes); Function Protein folding chaperone (FDR = 0.00016, 6 genes); Function ATP-dependent protein folding chaperone (FDR = 0.00068, 5 genes); Keyword Chaperone (FDR = 0.0016, 7 genes); Function Unfolded protein binding (FDR = 0.0019, 6 genes); NetworkNeighborAL Chaperone, and RPAP3/R2TP/prefoldin-like complex (FDR = 0.0089, 6 genes); Pfam TCP-1/cpn60 chaperonin family (FDR = 0.0091, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_05064.1 (PSMC2, PSMC4; 2/31); huMAP3_09656.1 (PSMC2, PSMC4; 2/64); huMAP3_13725.1 (PSMC2, PSMC4; 2/69)

### Novelty

The underlying molecular functions are not new: the CCT chaperonin, HSP90AA1 and HSPA5 chaperone systems, proteasome ATPases, glycolytic enzymes, mitochondrial translation machinery, and nucleotide metabolism are established biology. The STRING and hu.MAP overlap strongly supports this conclusion. What may be novel is the reproducible conservation of this particular combined co-abundance pattern across cervix_uterine and heart, especially the way the chaperonin core is coordinated with metabolic, proteasomal, mitochondrial, and cardiac-signaling genes. The fact that some module relationships are absent from STRING or hu.MAP does not establish novelty, because those resources emphasize known physical or curated relationships and do not capture every tissue-level co-abundance association. A claim that this is a new biological complex or a new direct interaction would therefore be premature. Its defensible novelty is as a cross-tissue network-level observation that requires validation in independent cohorts, cell-resolved data, and perturbation experiments.

**Hypothesis.** Hypothesis: the conserved module represents a shared cellular maintenance program in which CCT-mediated folding, HSP90AA1 and HSPA5 stress buffering, BAG2-assisted chaperone handling, and proteasomal ATPase activity maintain protein quality while ATP, nucleotide, glycolytic, one-carbon, and mitochondrial translation processes supply the energy and building blocks required for continual protein turnover. In heart, CAMK2D may connect this maintenance program to calcium-dependent contractile signaling; in cervix_uterine, the same core may reflect epithelial or stromal cellular maintenance. The CCT-centered machinery could also support the telomerase and Cajal-body annotations (9 globally significant GO/KEGG terms, q_global 0.000408–0.000408; see the table), (GO:BP regulation of telomere maintenance; q_global = 0.00163) (GO:BP positive regulation of telomere maintenance; q_global = 0.00163) (GO:BP DNA biosynthetic process; q_global = 0.00163), (11 globally significant GO/KEGG terms, q_global 0.00435–0.00614; see the table), and (4 globally significant GO/KEGG terms, q_global 0.0215–0.0215; see the table), but this remains a mechanistic hypothesis rather than an established tissue-specific function. Testing should examine whether module abundance tracks unfolded-protein stress, proteasome activity, mitochondrial function, and telomerase or Cajal-body phenotypes within matched cell types.

### Important genes

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT8 (0.94), IMPDH2 (0.91), CAMK2D (0.86), HSPA5 (0.85), CCT5 (0.85), PSMC2 (0.84), GET3 (0.82), PSMC4 (0.81), CCT7 (0.81); STRING partners: CCT5 (0.999), CCT7 (0.999), CCT8 (0.999), HSP90AA1 (0.767)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is the highest-connectivity member of the module and links the CCT core to IMPDH2, CAMK2D, HSPA5, PSMC2, PSMC4, and GET3. It appears in all primary enrichment terms (62 globally significant GO/KEGG terms, q_global 2.14e-05–0.0493; see the table), participates in every listed CCT hu.MAP complex (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), and has strong STRING support with the other CCT subunits and HSP90AA1. Its established function is ATP-dependent folding of proteins such as actin and tubulin, and its broad tissue profile fits a conserved housekeeping role. Its substantial literature and disease associations make it a strong anchor for interpreting the module.
- **Conclusion**: Established evidence supports CCT3 as a central chaperonin component and the principal network bridge in this module. The hypothesis that CCT3 coordinates the observed metabolic and proteasomal branches is plausible from its network position but is not demonstrated by the co-abundance data alone.

#### CCT7

- **Related proteins** (co-abundance neighbors): CCT8 (0.88), CCT5 (0.87), SHMT2 (0.86), PSMC4 (0.82), CCT3 (0.81); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT8 (0.999), HSP90AA1 (0.849), HSPA5 (0.783), IMPDH2 (0.758)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is a highly connected CCT-core member with links to CCT3, CCT5, CCT8, SHMT2, PSMC4, and IMPDH2. It appears throughout the primary enrichment profile (62 globally significant GO/KEGG terms, q_global 2.14e-05–0.0493; see the table), is present in the CCT hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), and has strong STRING support with the other CCT subunits, HSP90AA1, HSPA5, and IMPDH2. Its established role is ATP-dependent folding within TRiC, while its disease associations include myocardial infarction and neurodegenerative disease. Its heart and cervix detection makes it relevant to the conserved tissue comparison.
- **Conclusion**: Established evidence identifies CCT7 as a core structural and functional component of the chaperonin signal. Its connection to SHMT2 and IMPDH2 suggests a possible metabolic interface, but a direct regulatory role for CCT7 in those pathways remains hypothetical.

#### CAMK2D

- **Related proteins** (co-abundance neighbors): CCT3 (0.86), IMPDH2 (0.84), CCT8 (0.81), PANK4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Primary cilium tip, Primary cilium transition zone, Principal piece; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium/calmodulin dependent protein kinase II delta. The product of this gene belongs to the serine/threonine protein kinase family and to the Ca(2+)/calmodulin-dependent protein kinase subfamily. Calcium signaling is crucial for several aspects of plasticity at glutamatergic synapses. In mammalian cells, the enzyme is composed of four different chains: alpha, beta, gamma, and delta. The product of this gene is a delta chain. Alternative splicing re…
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.632); atrial fibrillation (0.556); CAMK2D-related neurodevelopmental disorder and dilated cardiomyopathy (0.503); heart conduction disease (0.449); heart failure (0.438)
- **Europe PMC papers**: 2254
- **Why important**: CAMK2D provides the most tissue-contextualized signaling component of the module. It is heart-muscle enhanced, associated with cardiomyocytes, connected in the module to CCT3, IMPDH2, CCT8, and PANK4, and has established functions in calcium-dependent phosphorylation, membrane depolarization, and regulation of heart contraction. It is associated with atrial fibrillation, heart conduction disease, heart failure, and dilated cardiomyopathy. Unlike the CCT genes, it is not supported by a listed hu.MAP complex or STRING interaction, making its co-abundance relationship particularly informative but less mechanistically resolved.
- **Conclusion**: Established evidence supports CAMK2D as a heart-relevant calcium-signaling kinase embedded in a broadly conserved maintenance module. The hypothesis that the chaperone and metabolic machinery modulates CAMK2D-dependent cardiac signaling is attractive but requires direct biochemical or perturbational testing.

#### HSPA5

- **Related proteins** (co-abundance neighbors): KARS1 (0.88), PFKP (0.85), CCT3 (0.85); STRING partners: CCT5 (0.727), CCT7 (0.783), CCT8 (0.701), HSP90AA1 (0.968)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is a major chaperone and ER-homeostasis factor with module links to CCT3, KARS1, and PFKP. It participates in the primary ATP-binding, chaperone, protein-folding, unfolded-protein, and protein-stabilization annotations (8 globally significant GO/KEGG terms, q_global 2.14e-05–0.000355; see the table), (GO:MF protein folding chaperone; q_global = 0.000823) (GO:MF ATP-dependent activity; q_global = 0.00086), (GO:BP protein folding; q_global = 0.00655), (GO:BP protein maturation; q_global = 0.0167), (GO:MF unfolded protein binding; q_global = 0.0185), and (GO:BP protein stabilization; q_global = 0.0484). STRING supports its relationships with HSP90AA1 and several CCT subunits (4 supplementary STRING terms; within-query FDR 0.00016–0.0019), and HPA detects it in both tissues. Its large literature base and associations with stress, infection, neurodegeneration, and cancer make it a biologically important stress-response component.
- **Conclusion**: Established evidence supports HSPA5 as a proteostasis and stress-buffering component that reinforces the module's chaperone interpretation. The module data do not establish whether HSPA5 is responding to stress, causing the shared co-abundance pattern, or simply reflecting general protein-folding demand.

#### SHMT2

- **Related proteins** (co-abundance neighbors): CCT7 (0.86), PSMC4 (0.84), BAG2 (0.82), CCT5 (0.82), CCT8 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine hydroxymethyltransferase 2. This gene encodes the mitochondrial form of a pyridoxal phosphate-dependent enzyme that catalyzes the reversible reaction of serine and tetrahydrofolate to glycine and 5,10-methylene tetrahydrofolate. The encoded product is primarily responsible for glycine synthesis. The activity of the encoded protein has been suggested to be the primary source of intracellular glycine. The gene which encodes th…
- **Diseases (Open Targets)**: neurodevelopmental disorder with cardiomyopathy, spasticity, and brain abnormalities (0.771); microcephaly (0.370); polymicrogyria (0.370); neurodevelopmental disorder (0.336); hereditary disease (0.192)
- **Europe PMC papers**: 2579
- **Why important**: SHMT2 is a mitochondrial enzyme that connects serine and glycine metabolism with one-carbon metabolism and mitochondrial function. It has five module neighbors, including CCT7, PSMC4, BAG2, CCT5, and CCT8, but no listed STRING interaction or hu.MAP complex. It is liver-enhanced, associated with hepatocytes and trophoblast-related cell types, detected in cervix_uterine but not heart, and has strong disease and literature representation. Its selective presence in only part of the tissue comparison may help distinguish a shared core from tissue-specific metabolic coupling.
- **Conclusion**: Established evidence supports SHMT2 as a mitochondrial metabolic component associated with protein-quality-control genes in the network. Its placement may indicate metabolic support for proteostasis or a tissue-specific branch of the module, but the direct connection to the CCT machinery is a hypothesis rather than an established physical interaction.

## Module 5

**Tissue pair**: cervix_uterine and heart  
**Genes (10)**: CLIC1, FKBP3, GSTP1, HSPB1, LYPLA1, NIPSNAP1, PSMA1, RAN, RPL12, SEC22B

### Function

No GO or KEGG term passed global correction, and there are no globally significant GO/KEGG terms; there are also no supplementary supplementary STRING terms. Therefore, the functional interpretation must come from the individual gene annotations and the co-abundance structure rather than from pathway enrichment. The module is most consistent with a broad cellular-maintenance program combining redox and xenobiotic handling through GSTP1 and CLIC1, vesicle and secretory-pathway handling through SEC22B and possibly NIPSNAP1, proteostasis and stress responses through HSPB1, FKBP3 and PSMA1, and nuclear transport, translation and cell-cycle-related processes through RAN and RPL12. The sparse co-abundance graph is compatible with coordinated regulation of several connected cellular-maintenance processes, but it does not demonstrate a single biochemical pathway.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins: the genes have no secretome annotation. HPA reports low immune-cell specificity throughout the module, with no blood-cell enrichment, arguing against a blood-cell explanation. Most genes are broadly expressed or have limited tissue specificity, while a subset is tissue enhanced in esophagus, skeletal muscle, tongue or liver. The recurring single-cell annotations in epithelial and suprabasal populations, together with detection of most tested proteins in both cervix and heart, suggest that shared epithelial, structural or generally stressed cellular populations could contribute to the cross-tissue signal. The module is therefore more consistent with intracellular housekeeping, stress and trafficking biology than with circulating protein contamination, although shared cell composition remains a plausible contributor.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship is reported among the module genes, and no STRING functional enrichment is available. No hu.MAP complex contains multiple module members. The co-abundance edges therefore appear to represent coordinated abundance patterns that are not supported here by established physical interaction evidence. The absence of STRING or hu.MAP support does not invalidate the module, but it weakens any claim that the genes form a known molecular complex. The strongest internal links connect GSTP1 with SEC22B, RAN and LYPLA1; SEC22B with FKBP3 and PSMA1; and LYPLA1 with HSPB1. These links are useful for prioritization, but they should be treated as co-abundance relationships rather than proven molecular contacts.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially interesting cross-tissue co-abundance observation, but it cannot be called a new biological pathway or a definitive novel module from the supplied evidence. The lack of globally significant GO or KEGG enrichment, STRING interactions, and hu.MAP complexes makes the module exploratory. Its possible novelty lies in the coordinated abundance pattern across cervix and heart, especially the connection between redox handling, vesicle trafficking, proteostasis and nuclear or translational functions. However, absence from STRING and hu.MAP alone does not prove novelty. Independent cohort replication, adjustment for cell composition, and comparison with published co-expression or proteomic modules would be required before claiming a new finding.

**Hypothesis.** Hypothesis: the module may represent a shared intracellular adaptation program that links oxidative or electrophilic stress handling with protein folding, proteasomal turnover, membrane trafficking and nuclear transport. GSTP1 and CLIC1 could buffer redox and oxidant-related stress; HSPB1 and FKBP3 could support protein quality control and folding; SEC22B and NIPSNAP1 could influence vesicular or organelle trafficking; and RAN, RPL12 and PSMA1 could connect the response to nuclear transport, translation and protein degradation. The cross-tissue signal may arise when comparable epithelial or other non-blood cell populations in cervix and heart experience related metabolic or proteotoxic demands. This is a mechanistic hypothesis, not an established pathway assignment, because the module lacks globally significant enrichment and known complex support.

### Important genes

#### GSTP1

- **Related proteins** (co-abundance neighbors): SEC22B (0.93), RAN (0.88), LYPLA1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutathione S-transferase pi 1. Glutathione S-transferases (GSTs) are a family of enzymes that play an important role in detoxification by catalyzing the conjugation of many hydrophobic and electrophilic compounds with reduced glutathione. Based on their biochemical, immunologic, and structural properties, the soluble GSTs are categorized into 4 main classes: alpha, mu, pi, and theta. This GST family member is a polymorphic gene…
- **Diseases (Open Targets)**: neurodegenerative disease (0.350); breast cancer (0.117); hepatocellular carcinoma (0.115); neoplasm (0.114); posterior cortical atrophy (0.113)
- **Europe PMC papers**: 12759
- **Why important**: GSTP1 is the most connected and strongest-weighted node in the module, linking the vesicle-trafficking, nuclear-transport and lipid-handling portions of the graph. Its established glutathione-transferase activity, roles in glutathione and xenobiotic metabolism, response to reactive oxygen species and negative regulation of acute inflammation make it the clearest functional anchor for a stress-response interpretation. It is tissue enhanced in esophagus and detected in both relevant tissues. It also has extensive literature and disease associations including cancer and neurodegenerative disease.
- **Conclusion**: Established evidence supports GSTP1 as a redox, detoxification and stress-response enzyme with a central position in this co-abundance graph. It is a strong module marker. A role as the upstream coordinator of the entire module remains hypothetical and is not demonstrated by the available interaction or enrichment evidence.

#### SEC22B

- **Related proteins** (co-abundance neighbors): GSTP1 (0.93), FKBP3 (0.87), PSMA1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC22 homolog B, vesicle trafficking protein. The protein encoded by this gene is a member of the SEC22 family of vesicle trafficking proteins. It seems to complex with SNARE and it is thought to play a role in the ER-Golgi protein trafficking. This protein has strong similarity to Mus musculus and Cricetulus griseus proteins.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: inflammatory bowel disease (0.285); luminal A breast carcinoma (0.271); colitis (0.238); enteritis (0.238); Crohn disease (0.233)
- **Europe PMC papers**: 1006
- **Why important**: SEC22B is tied for the highest connectivity and has strong links to GSTP1, FKBP3 and PSMA1. Its established function in ER-to-Golgi and Golgi-to-ER vesicle transport and vesicle fusion provides a plausible trafficking axis within the module. It is broadly expressed, has a neutrophil-associated single-cell annotation without overall blood-cell specificity, and has literature and disease associations involving inflammatory bowel disease and colitis.
- **Conclusion**: Established evidence supports SEC22B as a vesicle-trafficking component that may explain part of the module's shared intracellular organization. Its connection to redox and proteostasis genes is a module-level hypothesis rather than a demonstrated physical pathway.

#### RAN

- **Related proteins** (co-abundance neighbors): GSTP1 (0.88), RPL12 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAN, member RAS oncogene family. RAN (ras-related nuclear protein) is a small GTP binding protein belonging to the RAS superfamily that is essential for the translocation of RNA and proteins through the nuclear pore complex. The RAN protein is also involved in control of DNA synthesis and cell cycle progression. Nuclear localization of RAN requires the presence of regulator of chromosome condensation 1 (RCC1). Mutations in RAN di…
- **Diseases (Open Targets)**: HIV infectious disease (0.565); Orthomyxoviridae infectious disease (0.376); pemphigus foliaceus (0.298); neurodegenerative disease (0.270); Genu valgum (0.136)
- **Europe PMC papers**: 133080
- **Why important**: RAN is a highly studied gene with extensive literature and is connected to GSTP1 and RPL12. Its established roles in nuclear import and export, ribosomal subunit export, DNA metabolism, cell-cycle progression and chromosome segregation make it a plausible bridge between cytoplasmic stress responses and nuclear or translational activity. HPA describes low tissue specificity and enrichment in several proliferative or epithelial-related cell types, while disease associations include infectious, neurodegenerative and other disorders.
- **Conclusion**: Established evidence supports RAN as a core nuclear-transport and cell-cycle regulator whose abundance could reflect general cellular activity or stress. The hypothesis that RAN functionally couples the other module branches is plausible but unproven, particularly because no known high-confidence interactions were retrieved.

#### HSPB1

- **Related proteins** (co-abundance neighbors): LYPLA1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family B (small) member 1. This gene encodes a member of the small heat shock protein (HSP20) family of proteins. In response to environmental stress, the encoded protein translocates from the cytoplasm to the nucleus and functions as a molecular chaperone that promotes the correct folding of other proteins. This protein plays an important role in the differentiation of a wide variety of cell types. Expression of this gene …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2F (0.810); neuronopathy, distal hereditary motor, type 2B (0.808); Charcot-Marie-Tooth disease (0.540); hereditary disease (0.510); distal hereditary motor neuropathy type 2 (0.455)
- **Europe PMC papers**: 10348
- **Why important**: HSPB1 is the module's principal stress-chaperone candidate and is connected to LYPLA1. Its established functions include molecular chaperoning, protein folding, responses to unfolded protein and heat stress, and regulation of translation-related processes. It is tissue enhanced in esophagus, appears in several epithelial and stromal cell annotations, is detected in both relevant tissues, and has substantial literature together with strong hereditary neuropathy and cancer-related associations.
- **Conclusion**: Established evidence supports HSPB1 as a proteostasis and cellular-stress component of the module. Its placement next to LYPLA1 supports a local stress or membrane-lipid-handling interpretation, but the proposed coordination with GSTP1, SEC22B and RAN remains a hypothesis.

#### PSMA1

- **Related proteins** (co-abundance neighbors): NIPSNAP1 (0.91), SEC22B (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 20S subunit alpha 1. The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent proc…
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.535); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1417
- **Why important**: PSMA1 is connected to SEC22B and NIPSNAP1 and represents the proteasome branch of the graph. Its established role as a core proteasome subunit links the module to ubiquitin-dependent protein catabolism, DNA damage responses, apoptosis and inflammatory regulation. It is detected in both relevant tissues, has broad cellular annotations, and has disease associations including plasma cell myeloma, lymphoma, neoplasm and amyloidosis.
- **Conclusion**: Established evidence supports PSMA1 as a protein-quality-control and degradation component. Its module position suggests that proteasomal capacity may covary with trafficking and stress handling, but the module does not establish a specific proteasome-centered mechanism.

## Module 6

**Tissue pair**: cervix_uterine and heart  
**Genes (9)**: CNDP2, DPYSL2, FBLN1, FERMT2, FLNA, LTA4H, PALLD, TLN1, VIM

### Function

The module is most consistent with a cytoskeletal cell-adhesion and extracellular-matrix organization program, particularly involving integrin-associated adhesion, actin and intermediate-filament architecture, cell shape, migration, and contractility. The strongest direct support comes from the annotations of FERMT2, FLNA, TLN1, PALLD, VIM, and FBLN1, which collectively connect focal adhesions, integrin signaling, actin organization, intermediate filaments, and extracellular matrix. LTA4H adds a plausible inflammatory-lipid and peptide-processing component, while DPYSL2 links the module to microtubule organization and cell polarity. No GO or KEGG term passed global correction, so the proposed function is an interpretation of the gene annotations and network structure rather than a globally significant enrichment result. The absence of a globally significant term does not invalidate the module.

**Cell composition.** The module does not appear to be dominated by plasma or broadly secreted proteins: only FBLN1 is annotated as secreted to the extracellular matrix, while most members are intracellular or cytoskeletal. It also does not have the profile of a strongly blood-cell-specific module. Most genes have low immune-cell specificity, although several show enrichment in monocyte or dendritic-cell populations. The HPA pattern instead points toward vascular, stromal, smooth-muscle, fibroblast-like, decidual, hepatic-stellate, and related structural cell populations. Blood-vessel enrichment is recurrent, and several genes are associated with decidual stromal cells or smooth-muscle cells. Thus, the shared cervix and heart signal could reflect conserved vascular or stromal structural cells, with possible contributions from immune or platelet-associated populations, rather than simply circulating plasma proteins or a generalized housekeeping program. Protein detection is also tissue-dependent: several members are detected in cervix but not heart, so the cross-tissue co-abundance pattern should not be interpreted as uniform protein expression in every cardiac cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a connected adhesion-cytoskeletal subnetwork involving FLNA, TLN1, and FERMT2. The FLNA-TLN1 relationship is especially strong in the supplied STRING results, and both FLNA-FERMT2 and FERMT2-TLN1 are also supported. These relationships are biologically coherent with filamin-mediated actin crosslinking, talin-dependent integrin activation, and kindlin-mediated focal-adhesion signaling. The remaining co-abundance relationships are not represented among the supplied high-confidence STRING interactions, so co-abundance should not be equated with direct physical binding. No hu.MAP complex contains multiple module members. Overall, the known STRING relationships support a real adhesion-related core, while the broader module may represent coordinated expression across a structural cell state rather than one established molecular complex.

**STRING interactions (score >= 0.7)**: 3 of 36 gene pairs: FERMT2–FLNA (0.852); FERMT2–TLN1 (0.705); FLNA–TLN1 (0.998)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The individual biology of the main genes and the FLNA-TLN1-FERMT2 adhesion relationships is established, so the module should not be presented as a newly discovered protein complex or as a new function for these genes. The potentially novel aspect is the conserved co-abundance of this particular combination across cervix and heart, including genes connected to adhesion, cytoskeletal remodeling, extracellular matrix, peptide processing, leukotriene metabolism, and microtubule organization. The absence of a hu.MAP complex or of STRING support for many pairwise links does not prove novelty; it may reflect indirect regulation, shared cell composition, tissue context, or incomplete interaction databases. A claim of a new mechanism would require independent replication, cell-type-resolved analysis, and experimental validation.

**Hypothesis.** Hypothesis: the module marks a conserved vascular-stromal structural state shared by cervix and heart. In this state, FERMT2 and TLN1 may coordinate integrin activation and focal-adhesion assembly, FLNA and PALLD may organize actin-linked cell shape and contractility, VIM may reinforce intermediate-filament connections during migration or mechanical stress, and FBLN1 may couple the cellular adhesion machinery to extracellular matrix. LTA4H could modulate local inflammatory lipid or peptide signals, while DPYSL2 could connect adhesion remodeling to microtubule organization and polarity. This hypothesis predicts association with vascular, smooth-muscle, fibroblast-like, or decidual stromal cells and does not imply that every member physically interacts with every other member.

### Important genes

#### FLNA

- **Related proteins** (co-abundance neighbors): VIM (0.83), DPYSL2 (0.82); STRING partners: FERMT2 (0.852), TLN1 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is a key structural integrator in the module. It links actin filaments to membrane glycoproteins and receptor complexes, and its annotations include cell-shape remodeling, migration, platelet activation, and vascular-associated cell types. Its supplied network relationships connect it to the adhesion proteins TLN1 and FERMT2, while its literature and disease-association record is extensive. It is therefore a strong anchor for interpreting the module as an adhesion and cytoskeletal program.
- **Conclusion**: Established evidence supports FLNA as an actin-to-membrane scaffold involved in adhesion, migration, and signaling, with known relationships to TLN1 and FERMT2. The module-specific hypothesis is that FLNA helps organize the shared vascular or stromal structural state; the co-abundance data alone do not establish a new FLNA interaction or a tissue-specific mechanism.

#### TLN1

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.85); STRING partners: FERMT2 (0.705), FLNA (0.998)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 is a focal-adhesion protein that activates integrins and organizes actin at cell-cell and cell-matrix contacts. It has a vascular tissue association, a platelet or megakaryocyte-related single-cell pattern, and supplied STRING links to both FLNA and FERMT2. Its annotation also includes cell adhesion, integrin signaling, junction assembly, and actin organization, making it central to the proposed structural interpretation.
- **Conclusion**: Established evidence supports TLN1 as an integrin-associated cytoskeletal organizer. The module suggests that talin-dependent adhesion may be coordinated with FLNA and FERMT2 in cervix and heart, but it does not demonstrate that this module is a single talin-containing complex in either tissue.

#### FERMT2

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.87); STRING partners: FLNA (0.852), TLN1 (0.705)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Focal adhesion sites; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FERM domain containing kindlin 2. Enables several functions, including actin binding activity; phosphatidylinositol-3,4,5-trisphosphate binding activity; and type I transforming growth factor beta receptor binding activity. Involved in several processes, including cell surface receptor signaling pathway; positive regulation of cell differentiation; and positive regulation of cellular component biogenesis. Acts upstream of or withi…
- **Diseases (Open Targets)**: open-angle glaucoma (0.501); prostate carcinoma (0.488); glaucoma (0.488); neurodegenerative disease (0.473); primary angle-closure glaucoma (0.407)
- **Europe PMC papers**: 1336
- **Why important**: FERMT2 is a focal-adhesion and integrin-signaling protein with actin-binding, phosphoinositide-binding, and transforming-growth-factor-receptor-related functions. It is detected in both tissues in the supplied HPA evidence and is enriched in smooth-muscle cells. Its network and STRING connections place it at the interface between the co-abundance structure and the known FLNA-TLN1 adhesion subnetwork.
- **Conclusion**: Established evidence supports FERMT2 as a mediator of integrin-dependent cell-matrix adhesion and receptor signaling. A reasonable module-specific hypothesis is that it helps couple extracellular matrix engagement to cytoskeletal remodeling in vascular or stromal cells, but causality and direction of regulation remain untested.

#### VIM

- **Related proteins** (co-abundance neighbors): FLNA (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vimentin. This gene encodes a type III intermediate filament protein. Intermediate filaments, along with microtubules and actin microfilaments, make up the cytoskeleton. The encoded protein is responsible for maintaining cell shape and integrity of the cytoplasm, and stabilizing cytoskeletal interactions. This protein is involved in neuritogenesis and cholesterol transport and functions as an organizer of a…
- **Diseases (Open Targets)**: dengue disease (0.516); early-onset non-syndromic cataract (0.462); early-onset partial cataract (0.458); Developmental cataract (0.435); cataract (0.372)
- **Europe PMC papers**: 86568
- **Why important**: VIM encodes vimentin, an intermediate-filament protein that maintains cell shape and cytoplasmic integrity and participates in attachment, migration, and signaling. It is associated with blood vessels, fibroblasts, decidual stromal cells, hepatic stellate cells, and other structural cell types. Its supplied relationship with FLNA provides a plausible bridge between intermediate filaments and actin-linked adhesion machinery. VIM also has the largest literature record among the module members, indicating extensive established biological relevance.
- **Conclusion**: Established evidence supports VIM as a structural and migration-associated intermediate filament. In this module, VIM may report or help stabilize a mechanically responsive stromal or vascular cell state, but the co-abundance relationship does not prove direct functional cooperation with FLNA in these tissues.

#### FBLN1

- **Related proteins** (co-abundance neighbors): LTA4H (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibulin 1. Fibulin 1 is a secreted glycoprotein that becomes incorporated into a fibrillar extracellular matrix. Calcium-binding is apparently required to mediate its binding to laminin and nidogen. It mediates platelet adhesion via binding fibrinogen. Four splice variants which differ in the 3' end have been identified. Each variant encodes a different isoform, but no functional distinctions have been ident…
- **Diseases (Open Targets)**: synpolydactyly type 2 (0.447); FBLN1-related developmental delay-central nervous system anomaly-syndactyly syndrome (0.377); synpolydactyly (0.371); adolescent idiopathic scoliosis (0.306); alcohol drinking (0.219)
- **Europe PMC papers**: 2655
- **Why important**: FBLN1 is the module's clearest extracellular-matrix component. It is secreted into the matrix, binds matrix-associated proteins, can mediate platelet adhesion, and is annotated for extracellular-matrix organization and integrin-mediated signaling. It is detected in both tissues and is associated with decidual stromal, endometrial, choroid-plexus, and non-classical monocyte populations. It therefore connects the intracellular adhesion machinery to the extracellular environment and is especially informative for interpreting tissue composition.
- **Conclusion**: Established evidence supports FBLN1 as a secreted matrix glycoprotein involved in matrix organization and adhesion. The module-specific interpretation is that FBLN1 may reflect or contribute to matrix remodeling around vascular or stromal cells, but the data do not establish that it directly binds the intracellular module members in cervix or heart.

## Module 7

**Tissue pair**: cervix_uterine and heart  
**Genes (5)**: GSR, PKM, ADSL, TKT, TXNDC5

### Function

The module is most consistent with a coupled metabolic, redox, and protein-homeostasis program. TKT links pentose-phosphate metabolism to glycolytic intermediates, PKM supports glycolytic ATP and pyruvate production, ADSL supports de novo purine and AMP biosynthesis, and GSR maintains reduced glutathione for antioxidant defense. TXNDC5 adds an endoplasmic-reticulum protein-folding and thiol-disulfide-isomerase function. The network architecture supports TXNDC5 as the central connector, with the other genes forming a mixed metabolic and proteostasis neighborhood. However, no GO or KEGG term passed global correction, so this functional interpretation is based on individual gene annotations and network structure rather than statistically significant module-level enrichment. The observed program may therefore represent coordinated cellular state rather than a single established pathway.

**Cell composition.** The module is not predominantly composed of secreted proteins: the HPA summary identifies only one secreted gene, while TXNDC5 is described as intracellular and membrane-associated with endoplasmic-reticulum localization. The genes show mixed tissue specificity, including low-specificity, tissue-enhanced, and group-enriched patterns. Skeletal muscle and tongue recur among enriched tissues, while bone marrow appears for TKT. Single-cell annotations are heterogeneous, including epithelial, trophoblast, progenitor, and immune-related populations. Blood-cell annotations occur for several genes, especially TKT, TXNDC5, and GSR, but the module is not uniformly blood-cell specific. Thus, a shared blood or immune-cell contribution is possible but not established. Detection in cervix is complete, whereas heart detection is incomplete, with TXNDC5 and GSR not detected in heart; this limits a simple interpretation as a uniformly expressed heart-and-cervix tissue program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports two high-confidence relationships: TKT with PKM and TKT with GSR. These links connect glycolytic or pentose-phosphate metabolism with redox defense, but STRING reports no supplementary functional enrichment. TXNDC5 has no listed STRING partners despite being the central node in the co-abundance network, indicating that its network centrality is not independently supported by the listed STRING interaction set. hu.MAP identifies one complex containing PKM and ADSL among the module members, providing independent complex-level support for a relationship between glycolytic energy production and purine biosynthesis. The complex contains many additional proteins, so its presence does not establish that the entire module is one physical complex. Overall, external interaction evidence supports selected edges and a metabolic relationship, while the broader co-abundance structure remains distinct from known physical-interaction evidence.

**STRING interactions (score >= 0.7)**: 2 of 10 gene pairs: GSR–TKT (0.751); PKM–TKT (0.951)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (PKM, ADSL; 2/57)

### Novelty

This module should not be called a newly discovered biological complex or pathway. The fact sheet provides prior support for the PKM–TKT and TKT–GSR relationships in STRING and for the PKM–ADSL pairing in hu.MAP. At the same time, the complete co-abundance pattern, particularly the central placement of TXNDC5 alongside these metabolic enzymes, is not established by the listed resources. Absence of TXNDC5 partners from STRING and absence of a matching hu.MAP complex do not prove novelty, because co-abundance can reflect shared regulation, cell composition, or stress state rather than physical interaction. The defensible conclusion is that the module contains a potentially interesting cross-process co-abundance pattern, but its novelty requires independent replication, tissue-cell deconvolution, and comparison with published co-expression resources.

**Hypothesis.** Hypothesis: the shared cervix-and-heart module reflects a cellular adaptation that coordinates energy and precursor metabolism with oxidative and protein-folding stress. Increased glycolytic and pentose-phosphate activity could provide ATP, biosynthetic intermediates, and reducing-equivalent support, while GSR maintains glutathione-dependent redox buffering, ADSL supports purine production, and TXNDC5 supports folding of oxidized or newly synthesized proteins in the endoplasmic reticulum. The pattern could arise from a shared hypoxic, inflammatory, or metabolically stressed cell state, or from similar contributions of particular cell populations in the two tissues. This is a mechanistic proposal, not a demonstrated causal pathway; the lack of globally significant GO or KEGG enrichment and incomplete heart protein detection argue for validation at the cell-type and experimental level.

### Important genes

#### TXNDC5

- **Related proteins** (co-abundance neighbors): PKM (0.90), TKT (0.87), ADSL (0.86), GSR (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Endoplasmic reticulum; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin domain containing 5. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal endoplasmic reticulum (ER)-signal sequence, three catalytically active thioredoxin domains and a C-terminal ER-retention sequence. Its expression is induced by hypoxia and its role ma…
- **Diseases (Open Targets)**: colorectal carcinoma (0.321); spinal stenosis (0.203); neoplasm (0.096); central nervous system cancer (0.092); glioma (0.091)
- **Europe PMC papers**: 1026
- **Why important**: TXNDC5 is the central connector in the module, linking every other member in the co-abundance subgraph. Its established function as an endoplasmic-reticulum thioredoxin-domain protein involved in protein folding and thiol-disulfide interchange provides a proteostasis and redox interpretation that complements the metabolic enzymes. It is associated with hypoxia-induced protection from apoptosis, has disease associations involving neoplasia and other disorders, and has substantial literature support. HPA places it in the endoplasmic reticulum and reports low tissue specificity, with selected immune and epithelial cell annotations.
- **Conclusion**: Established evidence supports TXNDC5 as the network hub and as an endoplasmic-reticulum folding and redox protein. It is a strong candidate for coordinating the module, but a causal role in the shared tissue program is only a hypothesis because it lacks listed STRING partners and is not detected in heart by the reported HPA protein assay.

#### TKT

- **Related proteins** (co-abundance neighbors): TXNDC5 (0.87); STRING partners: GSR (0.751), PKM (0.951)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transketolase. This gene encodes a thiamine-dependent enzyme which plays a role in the channeling of excess sugar phosphates to glycolysis in the pentose phosphate pathway. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: transketolase deficiency (0.663); neurodegenerative disease (0.409); cardiomyopathy (0.382); alcohol drinking (0.261); urolithiasis (0.259)
- **Europe PMC papers**: 3981
- **Why important**: TKT is connected to TXNDC5 in the co-abundance network and has two listed high-confidence STRING relationships, with PKM and GSR. Its established enzyme function in the non-oxidative pentose-phosphate pathway connects sugar-phosphate handling to glycolytic intermediates and can support biosynthetic and redox demands. HPA reports bone-marrow enrichment and multiple myeloid-cell annotations, making it important for evaluating metabolic state versus cell-composition effects. It also has disease associations including transketolase deficiency and cardiomyopathy and substantial literature support.
- **Conclusion**: Established evidence supports TKT as the strongest bridge between the co-abundance module and independently known metabolic and redox relationships. Its immune and bone-marrow annotations mean that a cell-composition contribution must be considered. Its proposed role as a driver of the shared module remains hypothetical.

#### PKM

- **Related proteins** (co-abundance neighbors): TXNDC5 (0.90); STRING partners: TKT (0.951)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: pyruvate kinase M1/2. This gene encodes a protein involved in glycolysis. The encoded protein is a pyruvate kinase that catalyzes the transfer of a phosphoryl group from phosphoenolpyruvate to ADP, generating ATP and pyruvate. This protein has been shown to interact with thyroid hormone and may mediate cellular metabolic effects induced by thyroid hormones. This protein has been found to bind Opa protein, a bacterial o…
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); autoimmune disorder of central nervous system (0.370); tympanic membrane perforation (0.204); neoplasm (0.121); hepatocellular carcinoma (0.120)
- **Europe PMC papers**: 8544
- **Why important**: PKM is connected to TXNDC5 and to TKT through a high-confidence STRING relationship. Its established function in glycolysis supplies pyruvate and ATP and is compatible with a coordinated energy-demand or stress-response program. HPA reports enhancement in skeletal muscle and tongue and protein detection in both tissues represented by the module, while its disease associations and very substantial literature support make it a well-characterized metabolic anchor. PKM also participates in the hu.MAP complex containing ADSL.
- **Conclusion**: Established evidence supports PKM as a metabolic anchor with independent support from STRING and hu.MAP. Its co-abundance with TXNDC5 may reflect coupling between energy metabolism and proteostasis, but this coupling is a hypothesis rather than proof of direct regulation.

#### GSR

- **Related proteins** (co-abundance neighbors): TXNDC5 (0.83); STRING partners: TKT (0.751)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutathione-disulfide reductase. This gene encodes a member of the class-I pyridine nucleotide-disulfide oxidoreductase family. This enzyme is a homodimeric flavoprotein. It is a central enzyme of cellular antioxidant defense, and reduces oxidized glutathione disulfide (GSSG) to the sulfhydryl form GSH, which is an important cellular antioxidant. Rare mutations in this gene result in hereditary glutathione reductase deficiency. M…
- **Diseases (Open Targets)**: hemolytic anemia due to glutathione reductase deficiency (0.702); glioblastoma (0.558); plasma cell myeloma (0.537); Hodgkins lymphoma (0.531); non-Hodgkin lymphoma (0.506)
- **Europe PMC papers**: 6439
- **Why important**: GSR is connected to TXNDC5 in the co-abundance network and to TKT in STRING. Its established function is regeneration of reduced glutathione from glutathione disulfide, making it a direct marker of cellular antioxidant capacity and redox homeostasis. HPA reports immune-related annotations, including neutrophil progenitors and basophils, and protein detection in cervix but not heart. It has disease associations involving glutathione-reductase deficiency and hematologic or neoplastic conditions, together with substantial literature support.
- **Conclusion**: Established evidence supports GSR as the module's redox-defense component and provides a plausible metabolic link through TKT. Its absent heart protein detection and immune annotations make sample composition or tissue-state differences important alternative explanations. A shared oxidative-stress mechanism is therefore plausible but unproven.

#### ADSL

- **Related proteins** (co-abundance neighbors): TXNDC5 (0.86); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, heart
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: adenylosuccinate lyase. The protein encoded by this gene belongs to the lyase 1 family. It is an essential enzyme involved in purine metabolism, and catalyzes two non-sequential reactions in the de novo purine biosynthetic pathway: the conversion of succinylaminoimidazole carboxamide ribotide (SAICAR) to aminoimidazole carboxamide ribotide (AICAR) and the conversion of adenylosuccinate (S-AMP) to adenosine monophosphate …
- **Diseases (Open Targets)**: adenylosuccinate lyase deficiency (0.852); neurodegenerative disease (0.528); hereditary disease (0.486); Intellectual disability (0.464); Epileptic encephalopathy (0.462)
- **Europe PMC papers**: 1131
- **Why important**: ADSL is connected to TXNDC5 and shares the hu.MAP complex with PKM. Its established function in de novo purine biosynthesis and AMP production adds nucleotide supply to the module's energy and biosynthetic interpretation. HPA reports group enrichment in skeletal muscle and tongue and detection in both cervix and heart. Its disease associations include adenylosuccinate lyase deficiency, intellectual disability, and epileptic encephalopathy, with a substantial disease and literature record.
- **Conclusion**: Established evidence supports ADSL as the nucleotide-biosynthesis component and as an independent hu.MAP-supported partner of PKM. Its connection to TXNDC5 may reflect coordinated biosynthetic and proteostasis demand, but the mechanism and direction of regulation remain hypothetical.
