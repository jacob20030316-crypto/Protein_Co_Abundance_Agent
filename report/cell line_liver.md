# Conserved co-abundance modules: cell line and liver

## Module 0

**Tissue pair**: cell line and liver  
**Genes (19)**: ACLY, COPB1, COPS3, DYNC1H1, GARS1, COLGALT1, NAA15, NSF, RO60, SEC23A, SRP72, AARS1, IARS1, LARS1, SARS1, VARS1, TNPO1, XPO1, CSE1L

### Function

This is most convincingly a cytosolic translation-fidelity and protein-biosynthesis module centered on aminoacyl-tRNA charging. The primary evidence is the globally corrected enrichment for aminoacyl-tRNA ligase activity, tRNA aminoacylation, amino acid activation, aminoacyl-tRNA biosynthesis, aminoacyl-tRNA editing, translational fidelity, and tRNA metabolism (11 globally significant GO/KEGG terms, q_global 0.00113–0.00636; see the table). The six synthetase genes AARS1, GARS1, IARS1, LARS1, SARS1, and VARS1 form the clear functional core. The broader module connects this core with nuclear transport, protein maturation, cytoskeletal transport, vesicle trafficking, and secretory-pathway functions represented by genes such as DYNC1H1, NAA15, XPO1, SRP72, COPB1, and SEC23A. The data therefore support a core translation function with associated intracellular protein handling, rather than a narrowly specialized tissue pathway.

**Cell composition.** The module is predominantly composed of broadly expressed, intracellular housekeeping-type proteins. HPA reports low tissue specificity for most genes and low immune-cell specificity for most genes, arguing against a module primarily caused by blood-cell contamination. The HPA summary indicates only a small minority of secreted genes, while the individual annotations mainly place proteins in the cytosol, nucleoplasm, endoplasmic reticulum, Golgi, vesicles, or transport machinery. Liver protein detection is common among the genes with available liver measurements, whereas matching cell-line HPA protein data are unavailable. Some genes show cell-type-enhanced patterns in reproductive cells, pancreatic islets, retinal cells, brain cells, or monocyte-related populations, but these patterns are dispersed rather than defining a coherent blood or secreted-protein signature. The shared module is therefore more consistent with a conserved cellular translation and protein-trafficking program than with a plasma-protein or blood-cell artifact, although sample composition and shared proliferative or metabolically active cell states could still contribute.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF aminoacyl-tRNA ligase activity | 0.00113 | AARS1, GARS1, IARS1, LARS1, SARS1, VARS1 |
| GO:BP tRNA aminoacylation for protein translation | 0.00113 | AARS1, GARS1, IARS1, LARS1, SARS1, VARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 0.00113 | AARS1, GARS1, IARS1, LARS1, SARS1, VARS1 |
| GO:BP amino acid activation | 0.00113 | AARS1, GARS1, IARS1, LARS1, SARS1, VARS1 |
| GO:BP tRNA aminoacylation | 0.00113 | AARS1, GARS1, IARS1, LARS1, SARS1, VARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 0.00136 | AARS1, GARS1, IARS1, LARS1, SARS1, VARS1 |
| GO:MF aminoacyl-tRNA deacylase activity | 0.00172 | AARS1, IARS1, LARS1, VARS1 |
| GO:BP regulation of translational fidelity | 0.00172 | AARS1, IARS1, LARS1, VARS1 |
| GO:BP aminoacyl-tRNA metabolism involved in translational fidelity | 0.00172 | AARS1, IARS1, LARS1, VARS1 |
| GO:MF catalytic activity, acting on a tRNA | 0.00314 | AARS1, GARS1, IARS1, LARS1, SARS1, VARS1 |
| GO:BP tRNA metabolic process | 0.00636 | AARS1, GARS1, IARS1, LARS1, SARS1, VARS1 |

### STRING and hu.MAP

STRING provides strong prior support for the aminoacyl-tRNA synthetase core. The synthetases form a dense set of high-confidence relationships and reproduce the aminoacyl-tRNA biosynthesis, cytosolic tRNA aminoacylation, translation, protein biosynthesis, and editing annotations (5 supplementary STRING terms; within-query FDR 0.00035–0.0012), (STRING RCTM Translation; within-query FDR = 0.0033) (STRING RCTM Metabolism of proteins; within-query FDR = 0.0037) (STRING Keyword Protein biosynthesis; within-query FDR = 0.0042), (STRING Process tRNA aminoacylation for protein translation; within-query FDR = 0.0053), (STRING Pfam Anticodon-binding domain of tRNA ligase; within-query FDR = 0.0137), (STRING Pfam tRNA synthetases class I (M); within-query FDR = 0.0163). STRING also supports a smaller exportin/importin relationship involving CSE1L, TNPO1, and XPO1 (STRING SMART Importin-beta N-terminal domain; within-query FDR = 0.0154), as well as broad cytosolic and protein-metabolism context (STRING COMPARTMENTS Cytosol; within-query FDR = 0.0021), (STRING RCTM Metabolism of proteins; within-query FDR = 0.0037), (STRING Keyword Cytoplasm; within-query FDR = 0.0042), (STRING Keyword Acetylation; within-query FDR = 0.0082). hu.MAP independently places AARS1 with GARS1 and IARS1 with LARS1 in complexes, and places XPO1 with CSE1L and TNPO1 in several complexes (hu.MAP huMAP3_09592.1) (hu.MAP huMAP3_11534.1) (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1) (hu.MAP huMAP3_07170.1) (hu.MAP huMAP3_09042.1) (hu.MAP huMAP3_06791.1) (hu.MAP huMAP3_14442.1). These known relationships show that the module is not an arbitrary correlation cluster: its central synthetase component reflects established molecular organization, while the remaining co-abundance links may reflect shared cellular state, coordinated expression, or indirect functional coupling. The absence of a hu.MAP assignment for several genes does not imply that they lack biological relationships.

**STRING interactions (score >= 0.7)**: 18 of 171 gene pairs: AARS1–GARS1 (0.983); AARS1–IARS1 (0.98); AARS1–LARS1 (0.968); AARS1–SARS1 (0.881); AARS1–VARS1 (0.938); CSE1L–TNPO1 (0.824); CSE1L–XPO1 (0.976); GARS1–IARS1 (0.97); GARS1–LARS1 (0.895); GARS1–SARS1 (0.975); GARS1–VARS1 (0.86); IARS1–LARS1 (0.999); IARS1–SARS1 (0.908); IARS1–VARS1 (0.9); LARS1–SARS1 (0.933); LARS1–VARS1 (0.968); SARS1–VARS1 (0.879); TNPO1–XPO1 (0.868)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Aminoacyl-tRNA biosynthesis (FDR = 0.00035, 6 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 0.00041, 6 genes); RCTM Cytosolic tRNA aminoacylation (FDR = 0.00042, 6 genes); Function aminoacyl-tRNA ligase activity (FDR = 0.0011, 6 genes); Function aminoacyl-tRNA editing activity (FDR = 0.0012, 4 genes); COMPARTMENTS Cytosol (FDR = 0.0021, 17 genes); RCTM Translation (FDR = 0.0033, 7 genes); RCTM Metabolism of proteins (FDR = 0.0037, 12 genes); Keyword Protein biosynthesis (FDR = 0.0042, 6 genes); Keyword Cytoplasm (FDR = 0.0042, 17 genes); Process tRNA aminoacylation for protein translation (FDR = 0.0053, 6 genes); Keyword Acetylation (FDR = 0.0082, 18 genes); Pfam Anticodon-binding domain of tRNA ligase (FDR = 0.0137, 3 genes); SMART Importin-beta N-terminal domain (FDR = 0.0154, 3 genes); Pfam tRNA synthetases class I (M) (FDR = 0.0163, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09592.1 (XPO1, CSE1L, TNPO1; 3/95); huMAP3_11534.1 (GARS1, AARS1; 2/5); huMAP3_02637.1 (IARS1, LARS1; 2/14); huMAP3_13688.1 (IARS1, LARS1; 2/14); huMAP3_07170.1 (XPO1, CSE1L; 2/14); huMAP3_09042.1 (XPO1, CSE1L; 2/26); huMAP3_06791.1 (XPO1, CSE1L; 2/31); huMAP3_14442.1 (GARS1, AARS1; 2/57)

### Novelty

The biological function itself is not a new discovery: aminoacyl-tRNA synthetases, translation-fidelity mechanisms, and nuclear transport are well-established processes, and many of the synthetase relationships are already represented in STRING and hu.MAP. What may be novel is the specific cross-context co-abundance organization of this synthetase-centered module shared by cell line and liver, particularly its linkage to DYNC1H1, NAA15, XPO1, SRP72, vesicle-trafficking genes, and metabolic or cytoskeletal components. That claim should remain provisional because co-abundance is not equivalent to physical interaction or causal regulation. The module is best described as a potentially novel systems-level association built around a well-known conserved molecular core, rather than as a newly discovered pathway or complex.

**Hypothesis.** Hypothesis: the module represents a coordinated proteostasis program in which aminoacyl-tRNA synthetase abundance is coupled to the demand for accurate cytosolic translation and the handling of newly synthesized proteins. The synthetase core could support amino-acid charging and translational fidelity, while NAA15 could connect nascent-chain maturation, XPO1 and CSE1L or TNPO1 could coordinate nucleocytoplasmic transport, and SRP72, SEC23A, COPB1, and NSF could connect translation to ER targeting and intracellular trafficking. DYNC1H1 may provide a transport backbone that couples these processes to organelle or cytoskeletal movement. This is a mechanistic model rather than an established interaction map; it should be tested by perturbing the synthetase core and assessing translation fidelity, nascent-protein maturation, nuclear transport, and secretory-pathway flux.

### Important genes

#### AARS1

- **Related proteins** (co-abundance neighbors): COPS3 (0.81); STRING partners: GARS1 (0.983), IARS1 (0.98), LARS1 (0.968), SARS1 (0.881), VARS1 (0.938)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_11534.1, huMAP3_14442.1
- **Function (MyGene.info)**: alanyl-tRNA synthetase 1. The human alanyl-tRNA synthetase (AARS) belongs to a family of tRNA synthases, of the class II enzymes.  Class II tRNA synthases evolved early in evolution and are highly conserved. This is reflected by the fact that 498 of the 968-residue polypeptide human AARS shares 41% identity witht the E.coli protein.  tRNA synthases are the enzymes that interpret the RNA code and attach specific aminoacids …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2N (0.762); developmental and epileptic encephalopathy, 29 (0.747); undetermined early-onset epileptic encephalopathy (0.678); trichothiodystrophy 8, nonphotosensitive (0.568); Charcot-Marie-Tooth disease type 2 (0.566)
- **Europe PMC papers**: 672
- **Why important**: AARS1 is part of the central synthetase clique, has strong network support from the other aminoacyl-tRNA synthetases, and contributes to every primary globally corrected enrichment category (11 globally significant GO/KEGG terms, q_global 0.00113–0.00636; see the table). It is a cytosolic alanyl-tRNA synthetase with established roles in tRNA aminoacylation and tRNA processing. Its known links to inherited neurological disease and its substantial literature support make it an informative anchor for the translation-fidelity interpretation. hu.MAP also places it with GARS1 (hu.MAP huMAP3_11534.1), (hu.MAP huMAP3_14442.1).
- **Conclusion**: Established evidence supports AARS1 as a core enzymatic component of the module and a strong representative of its aminoacyl-tRNA charging function. Its disease associations support biological importance, but the co-abundance data do not establish that AARS1 mediates the other trafficking or disease-related features of the module.

#### IARS1

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.87), ACLY (0.84), VARS1 (0.84), LARS1 (0.80); STRING partners: AARS1 (0.98), GARS1 (0.97), LARS1 (0.999), SARS1 (0.908), VARS1 (0.9)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Isoleucine-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family and has been identified as a …
- **Diseases (Open Targets)**: growth retardation, intellectual developmental disorder, hypotonia, and hepatopathy (0.733); Abnormality of the skeletal system (0.332); microcephaly (0.289); Global developmental delay (0.289); Hallux valgus (0.184)
- **Europe PMC papers**: 184
- **Why important**: IARS1 is a central member of the primary enrichment signal and participates in the synthetase clique supported by STRING. It contributes to the editing and translational-fidelity terms (GO:MF aminoacyl-tRNA deacylase activity; q_global = 0.00172) (GO:BP regulation of translational fidelity; q_global = 0.00172) (GO:BP aminoacyl-tRNA metabolism involved in translational fidelity; q_global = 0.00172), has a strong connection to LARS1, and is represented in hu.MAP complexes (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1). Its annotation as an isoleucyl-tRNA synthetase directly supports accurate amino-acid assignment during translation, while its links to developmental and hepatopathy phenotypes are especially relevant to a liver-containing tissue pair.
- **Conclusion**: Established evidence identifies IARS1 as a core translation-fidelity enzyme and a plausible contributor to the shared liver and cell-line signal. It is reasonable to hypothesize that altered IARS1 abundance could affect proteome quality, but the module does not prove such a causal effect in either tissue.

#### LARS1

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.85), NAA15 (0.85), XPO1 (0.80), IARS1 (0.80); STRING partners: AARS1 (0.968), GARS1 (0.895), IARS1 (0.999), SARS1 (0.933), VARS1 (0.968)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: leucyl-tRNA synthetase 1. This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals w…
- **Diseases (Open Targets)**: infantile liver failure syndrome 1 (0.670); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.510); Global developmental delay (0.119); sensorineural hearing loss disorder (0.119); Generalized-onset seizure (0.118)
- **Europe PMC papers**: 267
- **Why important**: LARS1 is a core synthetase with strong STRING relationships to the other charging enzymes and participation in all primary enrichment themes (11 globally significant GO/KEGG terms, q_global 0.00113–0.00636; see the table). It catalyzes leucine-tRNA charging, is associated with a multisynthetase complex, and has documented links to infantile liver failure and cellular responses to amino-acid availability. Its position connecting the synthetase core with DYNC1H1, NAA15, and XPO1 makes it particularly informative for the proposed bridge between translation and intracellular protein handling. hu.MAP includes it with IARS1 (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1).
- **Conclusion**: Established evidence supports LARS1 as both a catalytic core gene and a biologically relevant liver-associated disease gene. The network supports coordinated abundance with transport and maturation machinery, but does not demonstrate that LARS1 directly regulates those processes in this module.

#### VARS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.84), DYNC1H1 (0.84), SEC23A (0.82), NAA15 (0.80), COPB1 (0.80); STRING partners: AARS1 (0.938), GARS1 (0.86), IARS1 (0.9), LARS1 (0.968), SARS1 (0.879)
- **HPA**: Low tissue specificity; Group enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: valyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. The protein encoded by this gene belongs to class-I aminoacyl-tRNA synthetase family and is located in the class…
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, seizures, and cortical atrophy (0.693); Abnormal brain morphology (0.333); hereditary disease (0.194); Intellectual disability (0.148); Delayed speech and language development (0.148)
- **Europe PMC papers**: 143
- **Why important**: VARS1 is part of the strongest functional core, contributes to every primary enriched GO and KEGG category, and is connected by STRING to the other synthetases (11 globally significant GO/KEGG terms, q_global 0.00113–0.00636; see the table), (5 supplementary STRING terms; within-query FDR 0.00035–0.0012). Its annotation directly supports valine-tRNA aminoacylation and translational fidelity. Within the co-abundance graph it connects the synthetase program to SEC23A, COPB1, DYNC1H1, and NAA15, giving it value as a bridge between translation and protein trafficking. Its disease associations include a neurodevelopmental disorder, and HPA indicates broadly distributed expression with a germ-cell-enhanced pattern.
- **Conclusion**: Established evidence supports VARS1 as a central translation-fidelity component and a possible connector to secretory-pathway machinery. The germ-cell pattern is not sufficient to assign the whole module to reproductive cells, and the bridging role remains a hypothesis based on co-abundance rather than demonstrated physical interaction.

#### DYNC1H1

- **Related proteins** (co-abundance neighbors): IARS1 (0.87), LARS1 (0.85), NAA15 (0.84), VARS1 (0.84), COPS3 (0.82), SRP72 (0.82), SARS1 (0.82), TNPO1 (0.81), CSE1L (0.81), RO60 (0.81), GARS1 (0.80), COPB1 (0.80), ACLY (0.80), NSF (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 1 heavy chain 1. Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polyp…
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy without contractures (0.816); intellectual disability, autosomal dominant 13 (0.815); Charcot-Marie-Tooth disease axonal type 2O (0.799); autosomal dominant non-syndromic intellectual disability (0.634); hereditary disease (0.545)
- **Europe PMC papers**: 1731
- **Why important**: DYNC1H1 has the strongest network centrality in the module and connects the synthetase genes with NAA15, COPS3, SRP72, TNPO1, and other module members. Its established function as a cytoplasmic dynein heavy chain supports intracellular transport, organelle movement, protein sorting, and retrograde transport. It has strong disease relevance, including motor-neuron and neurodevelopmental disorders, and substantial literature support. HPA indicates brain and retinal-cell enrichment, but not a blood-specific pattern.
- **Conclusion**: Established evidence supports DYNC1H1 as an intracellular transport hub that may explain how the translation-centered core is connected to broader cellular logistics. Its centrality does not prove that dynein physically coordinates aminoacyl-tRNA charging, so that integrative role should be treated as a hypothesis.

#### XPO1

- **Related proteins** (co-abundance neighbors): NAA15 (0.82), COLGALT1 (0.81), SRP72 (0.80), LARS1 (0.80); STRING partners: CSE1L (0.976), TNPO1 (0.868)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09592.1, huMAP3_07170.1, huMAP3_09042.1, huMAP3_06791.1
- **Function (MyGene.info)**: exportin 1. This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSe…
- **Diseases (Open Targets)**: plasma cell myeloma (0.642); B-cell chronic lymphocytic leukemia (0.626); diffuse large B-cell lymphoma (0.602); HIV infectious disease (0.561); neurodegenerative disease (0.522)
- **Europe PMC papers**: 5357
- **Why important**: XPO1 links the module to nucleocytoplasmic transport and has connections to NAA15, SRP72, LARS1, and the CSE1L–TNPO1 transport group. STRING and hu.MAP independently support its relationships with CSE1L and TNPO1 (hu.MAP huMAP3_09592.1), (hu.MAP huMAP3_07170.1) (hu.MAP huMAP3_09042.1) (hu.MAP huMAP3_06791.1), (STRING SMART Importin-beta N-terminal domain; within-query FDR = 0.0154). Its established functions include export of RNA and proteins from the nucleus and regulation of several signaling factors. XPO1 also has extensive disease literature, including hematologic malignancy and viral-disease associations, although HPA does not indicate a blood-specific module composition here.
- **Conclusion**: Established evidence supports XPO1 as the module's clearest nuclear-transport component and as a known interaction partner of the exportin/importin subnetwork. Its connection to the synthetase core is supported by co-abundance but not by a demonstrated direct mechanism; it may instead reflect coordinated demand for RNA, protein, and ribosome-related transport.

## Module 1

**Tissue pair**: cell line and liver  
**Genes (6)**: ACSL3, NUP160, PDCD11, EPRS1, QARS1, RARS1

### Function

The strongest interpretation is a translation-support module centered on the aminoacyl-tRNA synthetase multienzyme complex. (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.0109) is the only GO/KEGG term that passed global correction and links EPRS1, QARS1, and RARS1 to this complex. Their annotated functions are charging tRNAs with glutamate/proline, glutamine, and arginine, respectively, thereby supporting protein translation. The STRING annotations independently support aminoacyl-tRNA synthetase activity, class-I catalytic and anticodon-binding domains, and aminoacyl-tRNA biosynthesis (14 supplementary STRING terms; within-query FDR 0.008–0.0376). The remaining genes broaden the module beyond this core: NUP160 participates in nuclear pore-mediated nucleocytoplasmic transport and RNA export, PDCD11 participates in nucleolar rRNA processing, and ACSL3 participates in long-chain fatty-acid metabolism and fatty-acyl-CoA formation. Thus, the module most securely represents a core aminoacylation complex embedded in a broader translation, RNA-processing, and metabolic co-abundance neighborhood. No other GO/KEGG term passed global correction; absence of additional terms does not invalidate the module.

**Cell composition.** The module is not dominated by plasma proteins, secreted proteins, or blood-cell-enriched proteins. All members have low immune-cell specificity, no member is listed as secreted, and the HPA summary does not show an enriched blood-cell pattern. Most members have low tissue specificity, which is compatible with broadly used cellular functions rather than a tissue-restricted program. Several genes show cell-type-enhanced patterns, but these are distributed across distinct cell types rather than forming a coherent blood or secretory signature. HPA protein detection in liver is present for several members, while the cell-line protein evidence is unavailable in the supplied summary. Therefore, the shared signal is more plausibly a conserved intracellular program than a simple plasma carryover or shared blood-cell composition effect, although cellular composition and culture-state effects cannot be excluded.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 0.0109 | EPRS1, QARS1, RARS1 |

### STRING and hu.MAP

STRING provides strong known relationships among EPRS1, QARS1, and RARS1, and also connects EPRS1 with PDCD11. The STRING functional results recapitulate the aminoacyl-tRNA synthetase complex and aminoacyl-tRNA biosynthesis (14 supplementary STRING terms; within-query FDR 0.008–0.0376). hu.MAP independently places EPRS1, QARS1, and RARS1 together in two complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), each containing additional aminoacyl-tRNA synthetases and associated factors. These concordant resources support a genuine biochemical core rather than an interpretation based only on co-abundance. NUP160, ACSL3, and PDCD11 have little or no corresponding STRING or hu.MAP support within the supplied evidence, so their links to the core should be treated as module-level co-abundance relationships rather than established physical complex membership.

**STRING interactions (score >= 0.7)**: 4 of 15 gene pairs: EPRS1–PDCD11 (0.75); EPRS1–QARS1 (0.999); EPRS1–RARS1 (0.999); QARS1–RARS1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.008, 3 genes); COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.0108, 3 genes); InterPro Aminoacyl-tRNA synthetase, class I, conserved site (FDR = 0.0133, 3 genes); Pfam tRNA synthetases class I (E and Q), catalytic domain (FDR = 0.0207, 2 genes); Pfam tRNA synthetases class I (E and Q), anti-codon binding domain (FDR = 0.0207, 2 genes); Keyword Ligase (FDR = 0.0219, 4 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 0.024, 3 genes); InterPro Glutamyl/glutaminyl-tRNA synthetase (FDR = 0.0318, 2 genes); InterPro Ribosomal protein L25/Gln-tRNA synthetase, anti-codon-binding domain superfamily (FDR = 0.0318, 2 genes); InterPro Rossmann-like alpha/beta/alpha sandwich fold (FDR = 0.0318, 3 genes); InterPro Ribosomal protein L25/Gln-tRNA synthetase, N-terminal (FDR = 0.0318, 2 genes); InterPro Glutamyl/glutaminyl-tRNA synthetase, class Ib, catalytic domain (FDR = 0.0318, 2 genes); InterPro Glutamyl/glutaminyl-tRNA synthetase, class Ib, anti-codon binding domain (FDR = 0.0318, 2 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 0.0376, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, QARS1, RARS1; 3/14); huMAP3_13688.1 (EPRS1, QARS1, RARS1; 3/14)

### Novelty

The central biological finding is not a newly discovered aminoacyl-tRNA synthetase complex: the EPRS1-QARS1-RARS1 relationships are already represented by STRING and hu.MAP, and the functional annotation is well established. The potentially informative aspect is the reproducible co-abundance of this known core with NUP160, ACSL3, and PDCD11 across cell line and liver. However, absence of those peripheral relationships from STRING or hu.MAP does not establish novelty, because database coverage, context dependence, and indirect regulation can all produce such gaps. The appropriate conclusion is that this is a biologically credible conserved module with a potentially context-specific neighborhood, not proof of a new complex or mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated cellular investment in protein synthesis and RNA handling, with the EPRS1-QARS1-RARS1 complex supplying charged tRNAs while NUP160 supports nucleocytoplasmic RNA and protein traffic and PDCD11 supports nucleolar rRNA maturation. ACSL3 may couple this biosynthetic state to fatty-acid activation and lipid metabolic demand. This model is consistent with the annotations and network structure, but the coupling of ACSL3, NUP160, and PDCD11 to the aminoacyl-tRNA synthetase core is a hypothesis from co-abundance rather than an established physical mechanism.

### Important genes

#### EPRS1

- **Related proteins** (co-abundance neighbors): NUP160 (0.85), RARS1 (0.83), QARS1 (0.81), ACSL3 (0.81); STRING partners: PDCD11 (0.75), QARS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is the central network connector in the supplied subgraph and belongs to both hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). It is part of the globally supported term (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.0109) and of all listed STRING functional enrichments (14 supplementary STRING terms; within-query FDR 0.008–0.0376). Its established function is glutamyl- and prolyl-tRNA aminoacylation, with additional annotations involving translation and cellular response to insulin stimulus. It also has substantial literature coverage and disease associations involving hypomyelinating leukodystrophy and neurodevelopmental phenotypes.
- **Conclusion**: Established conclusion: EPRS1 is the best anchor for the module's aminoacylation and translation interpretation. Hypothesis: its central network position may make it a principal coordinator of the broader co-abundance state, but the data do not demonstrate that it regulates the peripheral genes.

#### QARS1

- **Related proteins** (co-abundance neighbors): EPRS1 (0.81); STRING partners: EPRS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutaminyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. In metazoans, 9 aminoacyl-tRNA synthetases specific for glutamine (gln), glutamic acid (glu), and 7 other amino …
- **Diseases (Open Targets)**: diffuse cerebral and cerebellar atrophy - intractable seizures - progressive microcephaly syndrome (0.794); hereditary disease (0.415); intellectual disability, autosomal dominant 43 (0.340); microcephaly (0.298); attention deficit-hyperactivity disorder (0.111)
- **Europe PMC papers**: 253
- **Why important**: QARS1 is a member of (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.0109), has strong STRING connections to EPRS1 and RARS1, and is included in both hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Its established role is glutaminyl-tRNA aminoacylation, and its annotations also include translation, brain development, and regulation of a stress-activated MAPK cascade. Its disease associations include a neurodevelopmental syndrome with cerebral and cerebellar atrophy and seizures, as well as intellectual disability and microcephaly. It has meaningful literature support.
- **Conclusion**: Established conclusion: QARS1 is a core enzymatic component of the conserved aminoacyl-tRNA synthetase signal. Hypothesis: its disease-linked sensitivity to translational or developmental stress may help explain why this core is co-abundant across biologically distinct sample contexts, but that interpretation requires direct perturbation or activity measurements.

#### RARS1

- **Related proteins** (co-abundance neighbors): EPRS1 (0.83); STRING partners: EPRS1 (0.999), QARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 is part of the globally supported complex term (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.0109), connects to EPRS1 and QARS1 in STRING, and is present in both hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Its established function is arginyl-tRNA aminoacylation in translation. It is associated with hypomyelinating and POLR-related leukodystrophy phenotypes and has literature support focused on aminoacylation and inherited disease.
- **Conclusion**: Established conclusion: RARS1 independently reinforces the interpretation that the module contains a functional aminoacyl-tRNA synthetase core. Hypothesis: coordinated abundance of RARS1 with the other core enzymes may buffer translational capacity, but co-abundance alone cannot establish coordinated enzymatic regulation.

#### NUP160

- **Related proteins** (co-abundance neighbors): EPRS1 (0.85), PDCD11 (0.84), ACSL3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 160. NUP160 is 1 of up to 60 proteins that make up the 120-MD nuclear pore complex, which mediates nucleoplasmic transport.[supplied by OMIM, Apr 2004]
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.527); neurodegenerative disease (0.469); Alzheimer disease (0.429)
- **Europe PMC papers**: 812
- **Why important**: NUP160 has a prominent network position outside the synthetase trio and is connected to EPRS1, PDCD11, and ACSL3 in the module graph. Its established annotation is as a nucleoporin involved in the nuclear pore complex, mRNA export, nucleocytoplasmic transport, and ribosomal large-subunit export. It has substantial literature coverage and disease associations involving viral infection, neurodegeneration, and Alzheimer disease. It lacks supplied STRING and hu.MAP support, making it informative as a peripheral module member rather than as a confirmed complex component.
- **Conclusion**: Established conclusion: NUP160 represents the RNA and nucleocytoplasmic-transport axis of the module. Hypothesis: its co-abundance with the synthetase core may reflect coordinated demand for RNA export and translation, but no direct interaction is established here.

#### ACSL3

- **Related proteins** (co-abundance neighbors): NUP160 (0.81), PDCD11 (0.81), EPRS1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 3. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme is highly expressed…
- **Diseases (Open Targets)**: prostate adenocarcinoma (0.370); acute myeloid leukemia (0.313); neurodegenerative disease (0.300); ovarian dysfunction (0.253); Abnormality of the skeletal system (0.215)
- **Europe PMC papers**: 2930
- **Why important**: ACSL3 is a well-connected peripheral member and is the only module gene with tissue-enhanced HPA expression, in parathyroid gland, while also showing liver protein detection. Its established function is activation of long-chain fatty acids to fatty acyl-CoA, with roles in lipid biosynthesis, fatty-acid degradation, and very-low-density-lipoprotein particle assembly. It has extensive literature coverage and disease associations including prostate adenocarcinoma, acute myeloid leukemia, and neurodegenerative disease. Its only supplied functional enrichment support is the supplementary ligase annotation (STRING Keyword Ligase; within-query FDR = 0.0219), and it has no supplied STRING partner or hu.MAP complex.
- **Conclusion**: Established conclusion: ACSL3 contributes a lipid-metabolic dimension and is not part of the demonstrated aminoacyl-tRNA synthetase core. Hypothesis: it may link translational demand to membrane or lipid metabolism in liver and cell-line contexts, but this proposed coupling is not established by the current evidence.

#### PDCD11

- **Related proteins** (co-abundance neighbors): NUP160 (0.84), ACSL3 (0.81); STRING partners: EPRS1 (0.75)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 11. PDCD11 is a NF-kappa-B (NFKB1; 164011)-binding protein that colocalizes with U3 RNA (MIM 180710) in the nucleolus and is required for rRNA maturation and generation of 18S rRNA (Sweet et al., 2003 [PubMed 14624448]; Sweet et al., 2008 [PubMed 17654514]).[supplied by OMIM, Oct 2008].
- **Diseases (Open Targets)**: Back pain (0.277); insomnia (0.216); systemic lupus erythematosus (0.170); neoplasm (0.095); colorectal carcinoma (0.093)
- **Europe PMC papers**: 334
- **Why important**: PDCD11 links the peripheral network to EPRS1 in STRING and connects with NUP160 and ACSL3 in the module graph. Its established role is nucleolar rRNA processing, including maturation and cleavage steps needed for generation of the small-subunit rRNA. It is detected in liver by HPA, has disease associations including systemic lupus erythematosus and neoplastic conditions, and has a moderate literature base. It is not included in the supplied hu.MAP complexes and has no supplied functional enrichment term.
- **Conclusion**: Established conclusion: PDCD11 represents nucleolar ribosome-biogenesis biology adjacent to the translation-related core. Hypothesis: its co-abundance with aminoacylation machinery may reflect coordinated ribosome production and translational capacity, but a direct mechanistic connection remains unproven.

## Module 2

**Tissue pair**: cell line and liver  
**Genes (20)**: ATP2A2, CLTC, DHX9, ERMP1, MYBBP1A, MDN1, NOP56, NUP155, NUP85, NUP210, PRKDC, RAB21, RSL1D1, SACM1L, SUPT16H, YARS2, TBL2, TMEM214, TM9SF2, SNRNP200

### Function

The strongest interpretation is a conserved nuclear gene-expression and ribosome-production module. Primary enrichment supports ribonucleoprotein complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0107), nuclear protein-containing complexes (GO:CC nuclear protein-containing complex; q_global = 0.0142), and preribosome biology (GO:CC preribosome; q_global = 0.0288). The genes include nucleolar ribosome-assembly factors such as NOP56, MDN1, RSL1D1, and MYBBP1A; RNA helicases and spliceosomal machinery such as DHX9 and SNRNP200; nuclear-pore components such as NUP155, NUP210, and NUP85; and chromatin or transcription machinery such as SUPT16H. The osteoblast-differentiation term (GO:BP osteoblast differentiation; q_global = 0.0134) is best regarded as a pleiotropic annotation shared by several broadly acting nuclear regulators rather than evidence that the module is specifically an osteoblast program. Supplementary STRING results reinforce ribonucleoprotein biogenesis, preribosome, ribosome biogenesis, RNA processing, nucleolar, and nuclear-complex interpretations (15 supplementary STRING terms; within-query FDR 0.003–0.0428). Overall, the module most plausibly represents coordinated abundance of conserved machinery for ribosome assembly, RNA maturation, nucleocytoplasmic transport, and genome-expression control.

**Cell composition.** The module is not a plasma-protein or secreted-protein module: no genes are annotated as secreted. Most genes have low tissue specificity, consistent with broadly expressed housekeeping or core nuclear machinery. Some cell-type-enhanced signals occur in erythrocyte progenitors, neutrophils, reproductive cells, cardiomyocytes, and related populations, while overall immune-cell specificity is low. Therefore, the shared cell-line and liver signal is more consistent with conserved intracellular machinery than with a liver-specific pathway. The erythrocyte-progenitor and other lineage-associated signals mean that differing cellular composition, including blood-cell contribution, should still be considered when interpreting tissue samples, but the HPA evidence does not support a predominantly blood-cell or plasma-protein module.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP ribonucleoprotein complex biogenesis | 0.0107 | DHX9, MDN1, MYBBP1A, NOP56, PRKDC, SNRNP200 |
| GO:BP osteoblast differentiation | 0.0134 | CLTC, DHX9, MYBBP1A, RSL1D1, SNRNP200 |
| GO:CC nuclear protein-containing complex | 0.0142 | MYBBP1A, NOP56, NUP155, NUP210, NUP85, PRKDC, SNRNP200, SUPT16H |
| GO:CC preribosome | 0.0288 | MDN1, NOP56, PRKDC |

### STRING and hu.MAP

STRING supports a connected but selective subset of relationships. The strongest known relationships include the NUP155–NUP210–NUP85 nuclear-pore cluster, the NOP56–RSL1D1 relationship, the MYBBP1A–RSL1D1 and MYBBP1A–NOP56 relationships, and links of DHX9 with PRKDC and SNRNP200. These known edges support real biological coherence, especially around nuclear transport, nucleolar function, RNA processing, and DNA-associated regulation, but they do not explain every co-abundance edge in the module. hu.MAP independently places NUP155 with NUP210 (hu.MAP huMAP3_07645.1) and NUP155 with NUP85 in nuclear-pore-related complexes (hu.MAP huMAP3_12581.1). The hu.MAP association of PRKDC with ATP2A2 (hu.MAP huMAP3_09592.1) is broader and less directly explanatory for the dominant nucleolar and nuclear-pore interpretation. The limited overlap with individual curated complexes suggests that the module is a cross-complex abundance program rather than one purified physical complex.

**STRING interactions (score >= 0.7)**: 8 of 190 gene pairs: DHX9–PRKDC (0.74); DHX9–SNRNP200 (0.784); MYBBP1A–NOP56 (0.737); MYBBP1A–RSL1D1 (0.831); NOP56–RSL1D1 (0.991); NUP155–NUP210 (0.991); NUP155–NUP85 (0.998); NUP210–NUP85 (0.988)
**STRING functional enrichment (supplementary, within-query FDR)**: Process Ribonucleoprotein complex biogenesis (FDR = 0.003, 7 genes); Component Preribosome (FDR = 0.0033, 4 genes); COMPARTMENTS Preribosome (FDR = 0.0035, 4 genes); Process Osteoblast differentiation (FDR = 0.0125, 5 genes); Process Ribosome biogenesis (FDR = 0.0125, 5 genes); Process RNA metabolic process (FDR = 0.0151, 9 genes); Component Nuclear protein-containing complex (FDR = 0.0176, 7 genes); Process ncRNA processing (FDR = 0.0189, 5 genes); Process rRNA processing (FDR = 0.0203, 4 genes); Process RNA processing (FDR = 0.0203, 7 genes); Process ncRNA metabolic process (FDR = 0.0203, 6 genes); Process Gene expression (FDR = 0.0357, 10 genes); Keyword mRNA transport (FDR = 0.0365, 4 genes); COMPARTMENTS Nucleolus (FDR = 0.0373, 6 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 0.0428, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07645.1 (NUP155, NUP210; 2/7); huMAP3_12581.1 (NUP155, NUP85; 2/58); huMAP3_09592.1 (ATP2A2, PRKDC; 2/95)

### Novelty

This is plausibly a new co-abundance observation, but it is not a wholly new molecular mechanism. Its central processes, including ribosome biogenesis, RNA processing, nuclear transport, DNA repair, and chromatin regulation, are established. Several internal relationships are already represented by STRING or hu.MAP, particularly the nucleoporin cluster and the NOP56–RSL1D1 interaction. Conversely, much of the module is not captured as one shared curated complex, and the cross-context conservation between cell line and liver may be a novel systems-level observation. The available evidence therefore supports novelty of the module-level organization or preservation, not a claim that the constituent biology or every pairwise association is previously unknown. Absence from a database alone would not establish novelty.

**Hypothesis.** Hypothesis: the module reflects a coordinated cellular demand for maintaining gene expression during active growth or cellular stress. Ribosome assembly and preribosome maturation may be coupled to RNA helicase activity, spliceosome function, nuclear-pore transport, chromatin remodeling, and DNA-damage surveillance. In this model, PRKDC and associated nuclear regulators provide genome-integrity and transcriptional control, NOP56, MDN1, RSL1D1, and MYBBP1A support nucleolar and ribosome-related processes, and NUP155, NUP210, and NUP85 regulate the nuclear exchange required to connect these processes. This hypothesis predicts coordinated changes in ribosome production, RNA processing, nuclear transport, and DNA-repair activity, but the co-abundance data alone do not establish direct physical cooperation or causal direction.

### Important genes

#### PRKDC

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.93), DHX9 (0.88), RSL1D1 (0.88), SUPT16H (0.85), CLTC (0.84), MDN1 (0.84), NUP85 (0.84), SACM1L (0.83), NOP56 (0.82), TMEM214 (0.81), ATP2A2 (0.81); STRING partners: DHX9 (0.74)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: protein kinase, DNA-activated, catalytic subunit. This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to DNA-PKcs deficiency (0.752); neurodegenerative disease (0.548); severe combined immunodeficiency (0.470); combined immunodeficiency (0.464); ovarian neoplasm (0.210)
- **Europe PMC papers**: 12461
- **Why important**: PRKDC is the highest-connectivity and strongest-weighted node in the module. It links the ribonucleoprotein and nuclear-complex portions of the network and is present in the primary ribonucleoprotein-biogenesis, nuclear-complex, and preribosome terms (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0107) (GO:CC nuclear protein-containing complex; q_global = 0.0142) (GO:CC preribosome; q_global = 0.0288). Its established function in DNA-dependent protein kinase activity, DNA double-strand-break repair, recombination, innate immune signaling, and maturation of ribosomal RNA makes it a strong integrator of genome integrity and gene-expression control. It also has extensive literature and disease links to DNA-PK deficiency and immunodeficiency.
- **Conclusion**: Established evidence supports PRKDC as a central network hub with roles in DNA repair and nuclear or ribosomal processes. The hypothesis that it coordinates the other module processes is plausible from its position and annotations, but direct causal coordination is not demonstrated.

#### NOP56

- **Related proteins** (co-abundance neighbors): NUP155 (0.85), SNRNP200 (0.84), PRKDC (0.82), RAB21 (0.82), RSL1D1 (0.81), MDN1 (0.81), MYBBP1A (0.81); STRING partners: MYBBP1A (0.737), RSL1D1 (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP56 ribonucleoprotein. Nop56p is a yeast nucleolar protein that is part of a complex with the nucleolar proteins Nop58p and fibrillarin. Nop56p is required for assembly of the 60S ribosomal subunit and is involved in pre-rRNA processing. The protein encoded by this gene is similar in sequence to Nop56p and is also found in the nucleolus. Expansion of a GGCCTG repeat from 3-8 copies to 1500-2500 copies in an intron of th…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 36 (0.586); neurodegenerative disease (0.495); ovarian neoplasm (0.272); hereditary disease (0.193); cerebellar ataxia (0.121)
- **Europe PMC papers**: 1517
- **Why important**: NOP56 occupies a highly connected position within the nucleolar portion of the module and is present in the primary ribonucleoprotein-biogenesis, nuclear-complex, and preribosome terms (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0107) (GO:CC nuclear protein-containing complex; q_global = 0.0142) (GO:CC preribosome; q_global = 0.0288). Its established roles in rRNA processing, rRNA modification, and ribosomal-subunit biogenesis directly match the dominant module interpretation. Its known STRING relationships with RSL1D1 and MYBBP1A further support a nucleolar subnetwork. NOP56 also has substantial literature and a clear disease association with spinocerebellar ataxia type thirty-six.
- **Conclusion**: Established evidence identifies NOP56 as a core nucleolar and ribosome-biogenesis component. It is a strong candidate for anchoring the module's ribonucleoprotein interpretation. Its role as a coordinator between the nucleolar and nuclear-pore portions remains a hypothesis.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): PRKDC (0.93), TMEM214 (0.86), RSL1D1 (0.85), DHX9 (0.85), NUP210 (0.85), NOP56 (0.84), NUP85 (0.83), YARS2 (0.80), SUPT16H (0.80); STRING partners: DHX9 (0.784)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is one of the more connected nodes and is present in the primary ribonucleoprotein-biogenesis, osteoblast-differentiation, and nuclear-complex terms (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0107) (GO:BP osteoblast differentiation; q_global = 0.0134) (GO:CC nuclear protein-containing complex; q_global = 0.0142). It encodes the U5 small nuclear ribonucleoprotein helicase and is an established component of spliceosome assembly, spliceosomal conformational change, and pre-mRNA splicing. Its STRING relationship with DHX9 and its links to several nuclear-complex members connect RNA processing with the broader module. It has a substantial literature and strong disease associations with retinitis pigmentosa and inherited retinal dystrophy.
- **Conclusion**: Established evidence supports SNRNP200 as the principal spliceosomal and RNA-processing representative in the module. Its co-abundance with nucleolar and nuclear-pore genes suggests coordinated RNA maturation, but it does not prove that the module forms one spliceosomal complex.

#### NUP155

- **Related proteins** (co-abundance neighbors): NOP56 (0.85); STRING partners: NUP210 (0.991), NUP85 (0.998)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07645.1, huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 155. Nucleoporins are proteins that play an important role in the assembly and functioning of the nuclear pore complex (NPC) which regulates the movement of macromolecules across the nuclear envelope (NE). The protein encoded by this gene plays a role in the fusion of NE vesicles and formation of the double membrane NE. The protein may also be involved in cardiac physiology and may be associated with t…
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); atrial fibrillation (0.470); familial atrial fibrillation (0.390)
- **Europe PMC papers**: 944
- **Why important**: NUP155 is part of the primary nuclear protein-containing-complex term (GO:CC nuclear protein-containing complex; q_global = 0.0142) and forms a highly supported STRING cluster with NUP210 and NUP85. It is also present in two hu.MAP nuclear-pore-related complexes (hu.MAP huMAP3_07645.1) (hu.MAP huMAP3_12581.1). Its established role in nuclear-pore assembly, RNA export, protein import, nuclear-envelope organization, and nuclear-membrane biology provides the clearest link between nucleolar activity and nucleocytoplasmic transport. It has substantial literature and disease associations with atrial fibrillation and familial atrial fibrillation.
- **Conclusion**: Established evidence supports NUP155 as a nuclear-pore module component that may connect nuclear transport with RNA and ribosome-related processes. Its inclusion does not establish that altered nuclear transport causes the observed co-abundance pattern.

#### MDN1

- **Related proteins** (co-abundance neighbors): PRKDC (0.84), NOP56 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoli, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: midasin AAA ATPase 1. Predicted to enable ATP binding activity. Involved in ribosomal large subunit assembly. Located in cytosol; intermediate filament cytoskeleton; and nuclear lumen. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Alzheimer disease (0.463); neurodegenerative disease (0.462); Parkinson disease (0.462); lysosomal storage disease (0.462); rheumatic disorder (0.271)
- **Europe PMC papers**: 601
- **Why important**: MDN1 is present in the primary ribonucleoprotein-biogenesis and preribosome terms (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0107) (GO:CC preribosome; q_global = 0.0288) and is repeatedly supported by the supplementary ribosome, rRNA-processing, and nucleolar results (11 supplementary STRING terms; within-query FDR 0.003–0.0428). Its established function as a ribosomal large-subunit assembly factor directly supports the module's central interpretation. Although its network degree is limited, its annotation is highly specific to the nucleolar and ribosome-assembly axis. It has disease associations spanning neurodegenerative and lysosomal-storage disorders and a substantial literature.
- **Conclusion**: Established evidence supports MDN1 as a biologically specific marker of ribosome assembly within the module. Its lower network connectivity does not diminish its interpretive value; it may represent a specialized process component rather than a network hub. A direct functional bridge to PRKDC or the nucleoporins remains hypothetical.

## Module 3

**Tissue pair**: cell line and liver  
**Genes (7)**: FASN, FMO4, MTX1, NCKAP1, PCYT2, MARS1, TARS1

### Function

No GO or KEGG term passed global correction, so the module does not have a statistically established pathway annotation from the enrichment analysis. Its gene content instead suggests a mixed metabolic and cellular-maintenance program. FMO4 supports xenobiotic and small-molecule oxidation; FASN supports fatty-acid synthesis; PCYT2 supports phospholipid synthesis; MTX1 supports mitochondrial organization; MARS1 and TARS1 support aminoacyl-tRNA charging and protein biosynthesis; and NCKAP1 supports Rac signaling, actin nucleation, and cell migration. The co-abundance graph is therefore more consistent with coordinated hepatocyte metabolic state, translation capacity, membrane-lipid metabolism, and organelle or cytoskeletal maintenance than with one narrowly defined pathway. This is an interpretation of gene function, not a globally significant GO or KEGG enrichment claim.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of its genes is annotated as secreted. It is also unlikely to be a blood-cell module, because the HPA evidence shows low immune-cell specificity for most genes and no detected immune-cell specificity for the remainder. All genes have liver protein detection in the available liver evidence except FASN, whose liver protein signal is reported as not detected. The tissue pattern is mixed rather than liver-exclusive: several genes have low tissue specificity, while others are enhanced in liver, kidney, adipose tissue, breast, or testis. The single-cell annotations likewise span hepatocytes, renal tubular cells, adipocytes, cardiomyocytes, epicardial cells, late spermatids, and other cell types. Thus, the shared cell-line and liver module may reflect a broadly used intracellular program with a liver metabolic component, rather than blood contamination or a secreted-protein signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, between MARS1 and TARS1. This is biologically coherent because both are aminoacyl-tRNA synthetases involved in translation-related activity. The same pair occurs together in two hu.MAP complexes, (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Those complexes contain many additional aminoacyl-tRNA synthetases and associated translation factors, although only MARS1 and TARS1 from this module are represented in either complex. The STRING and hu.MAP evidence therefore supports a real translation-associated submodule centered on MARS1 and TARS1. The remaining module edges are not supported by the listed high-confidence STRING interactions or hu.MAP complexes, so the complete co-abundance structure should not be treated as a known physical complex.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: MARS1–TARS1 (0.881)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (TARS1, MARS1; 2/14); huMAP3_13688.1 (TARS1, MARS1; 2/14)

### Novelty

The co-abundance module may represent a previously unreported association across liver and cell-line data, but the available evidence is insufficient to call it a new biological mechanism. Several component functions are established, including aminoacyl-tRNA charging, fatty-acid synthesis, phospholipid synthesis, mitochondrial organization, xenobiotic oxidation, and actin regulation. The MARS1–TARS1 relationship is already supported by STRING and by hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), so that part is not novel. The potentially novel aspect is the cross-functional co-abundance pattern linking these established processes. Because most within-module relationships lack independent STRING or hu.MAP support and because no GO or KEGG term passed global correction, the module should be described as a candidate systems-level association requiring replication and experimental testing, not as a demonstrated novel complex or pathway.

**Hypothesis.** Hypothesis: the module reflects a coordinated intracellular state in which liver-associated metabolic activity is coupled to the biosynthetic and structural demands of active cells. FMO4, FASN, and PCYT2 could represent linked handling of xenobiotic oxidation and lipid production, while MTX1 could connect that metabolic state to mitochondrial organization. MARS1 and TARS1 could indicate increased translational capacity, and NCKAP1 could connect the state to cytoskeletal remodeling or cell movement. This hypothesis predicts that the module will track hepatocyte metabolic load, membrane remodeling, mitochondrial demand, and protein synthesis more closely than immune-cell abundance or extracellular protein release. The proposed links beyond the MARS1–TARS1 relationship remain hypotheses because they are not established by the reported STRING, hu.MAP, GO, or KEGG evidence.

### Important genes

#### MARS1

- **Related proteins** (co-abundance neighbors): FMO4 (0.89), TARS1 (0.83); STRING partners: TARS1 (0.881)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: methionyl-tRNA synthetase 1. This gene encodes a member of the class I family of aminoacyl-tRNA synthetases. These enzymes play a critical role in protein biosynthesis by charging tRNAs with their cognate amino acids. The encoded protein is a component of the multi-tRNA synthetase complex and catalyzes the ligation of methionine to tRNA molecules. [provided by RefSeq, Jan 2011].
- **Diseases (Open Targets)**: severe early-onset pulmonary alveolar proteinosis due to MARS deficiency (0.745); Charcot-Marie-Tooth disease axonal type 2U (0.676); autosomal recessive spastic paraplegia type 70 (0.614); trichothiodystrophy 9, nonphotosensitive (0.428); pulmonary alveolar proteinosis (0.338)
- **Europe PMC papers**: 435
- **Why important**: MARS1 is a central connector in the module and is one of the two genes with direct high-confidence STRING support. It is a methionyl-tRNA synthetase and a component of the multi-tRNA synthetase complex. It also occurs in hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), giving it the strongest direct complex-level support in the module. Its disease associations include severe early-onset pulmonary alveolar proteinosis, Charcot-Marie-Tooth disease, spastic paraplegia, and trichothiodystrophy. Its substantial literature base makes it a well-characterized anchor for interpreting the translation-related part of the module.
- **Conclusion**: Established: MARS1 supports aminoacyl-tRNA charging and participates in known multi-synthetase complexes with TARS1. Hypothesis: its co-abundance with the metabolic genes may mark increased protein-production demand during a liver-associated metabolic state.

#### TARS1

- **Related proteins** (co-abundance neighbors): MARS1 (0.83), NCKAP1 (0.82); STRING partners: MARS1 (0.881)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: threonyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Threonyl-tRNA synthetase belongs to the class-II aminoacyl-tRNA synthetase family [provided by RefSeq, Jul 2008]…
- **Diseases (Open Targets)**: trichothiodystrophy 7, nonphotosensitive (0.520); trichothiodystrophy (0.430); actinic keratosis (0.356); dyshidrosis (0.315); placental abruption (0.307)
- **Europe PMC papers**: 147
- **Why important**: TARS1 is directly connected to MARS1 in STRING and co-occurs with MARS1 in hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). It is a threonyl-tRNA synthetase with a core role in tRNA aminoacylation and translation. Its presence gives the module a defined, independently supported translation-related component, even though the module as a whole lacks globally significant GO or KEGG enrichment. Its disease associations include trichothiodystrophy and other inherited disorders.
- **Conclusion**: Established: TARS1 is a translation-associated enzyme and forms a supported relationship with MARS1. Hypothesis: coordinated TARS1 and MARS1 abundance may indicate cellular demand for protein synthesis rather than a complete aminoacyl-tRNA synthetase complex.

#### FASN

- **Related proteins** (co-abundance neighbors): NCKAP1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fatty acid synthase. The enzyme encoded by this gene is a multifunctional protein. Its main function is to catalyze the synthesis of palmitate from acetyl-CoA and malonyl-CoA, in the presence of NADPH, into long-chain saturated fatty acids. In some cancer cell lines, this protein has been found to be fused with estrogen receptor-alpha (ER-alpha), in which the N-terminus of FAS is fused in-frame with the C-terminus of …
- **Diseases (Open Targets)**: dengue disease (0.469); autism spectrum disorder (0.333); Parkinson disease (0.295); Epileptic encephalopathy (0.211); neurodegenerative disease (0.205)
- **Europe PMC papers**: 21528
- **Why important**: FASN is the principal fatty-acid biosynthetic enzyme in the module and connects to NCKAP1 in the co-abundance graph. It is tissue-enhanced in adipose tissue, breast, and liver and is associated with lipid biosynthesis and nutrient response. It has a very substantial literature base and disease associations including dengue disease, autism spectrum disorder, Parkinson disease, and neurodegenerative disease. Its annotation provides a strong metabolic interpretation for the liver-associated component of the module.
- **Conclusion**: Established: FASN catalyzes palmitate synthesis and participates in fatty-acid and lipid biosynthesis. Hypothesis: its association with NCKAP1 and the translation-related genes may reflect coordinated membrane production and cellular growth or remodeling.

#### FMO4

- **Related proteins** (co-abundance neighbors): MARS1 (0.89), MTX1 (0.82), PCYT2 (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: flavin containing dimethylaniline monoxygenase 4. Metabolic N-oxidation of diet-derived amino-trimethylamine (TMA) is mediated by flavin-containing monooxygenase and is subject to an inherited FMO3 polymorphism in man. This results in a small subpopulation with reduced TMA N-oxidation capacity and causes fish odor syndrome (Trimethylaminuria). Three forms of the enzyme are encoded by genes clustered in the 1q23-q25 region. Flavin-containing monoo…
- **Diseases (Open Targets)**: neurodegenerative disease (0.394); brain aneurysm (0.343); alcohol drinking (0.320); stroke disorder (0.214); Abnormal nasolacrimal system morphology (0.182)
- **Europe PMC papers**: 382
- **Why important**: FMO4 has the strongest network position in the module and links MARS1, MTX1, and PCYT2. It is group-enriched in kidney and liver and is enhanced in several epithelial cell types, including hepatocytes and renal tubular cells. Its annotated function is flavin-dependent oxidation in xenobiotic metabolism, making it a plausible marker of tissue metabolic specialization. It also has disease and trait associations involving neurodegenerative disease, brain aneurysm, alcohol drinking, and stroke disorder.
- **Conclusion**: Established: FMO4 is a flavin-containing monooxygenase associated with xenobiotic metabolic processes and liver or kidney expression. Hypothesis: FMO4 may act as a metabolic-state marker that links lipid and mitochondrial features to the shared co-abundance pattern.

#### PCYT2

- **Related proteins** (co-abundance neighbors): FMO4 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphate cytidylyltransferase 2, ethanolamine. This gene encodes an enzyme that catalyzes the formation of CDP-ethanolamine from CTP and phosphoethanolamine in the Kennedy pathway of phospholipid synthesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010].
- **Diseases (Open Targets)**: spastic paraplegia 82, autosomal recessive (0.771); complex hereditary spastic paraplegia (0.554); neurodegenerative disease (0.542); Global developmental delay (0.462); Intellectual disability (0.462)
- **Europe PMC papers**: 4199
- **Why important**: PCYT2 connects to FMO4 and provides the module with a direct phospholipid-biosynthesis component through the Kennedy pathway. It is tissue-enhanced in liver and testis and cell-type enriched in late spermatids. Its disease associations include spastic paraplegia, neurodegenerative disease, global developmental delay, and intellectual disability. Its established biochemical role makes it informative for interpreting the membrane-lipid aspect of the module.
- **Conclusion**: Established: PCYT2 catalyzes a step in phosphatidylethanolamine and phospholipid synthesis. Hypothesis: PCYT2 may connect FMO4-linked metabolic activity with membrane remodeling and the biosynthetic requirements of translation.
