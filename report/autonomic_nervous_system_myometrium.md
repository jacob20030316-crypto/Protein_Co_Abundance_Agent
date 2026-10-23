# Conserved co-abundance modules: autonomic_nervous_system and myometrium

## Module 0

**Tissue pair**: autonomic_nervous_system and myometrium  
**Genes (13)**: PGD, GOT1, ADK, DDX39B, HDGFL2, MESD, NRDC, PCNA, PITRM1, PSMC6, RBBP4, AARS1, TNPO1

### Function

The module does not support a single statistically established biological function: no GO or KEGG term passed global correction. Its genes instead suggest a heterogeneous cellular-maintenance program involving nuclear RNA processing and export, DNA replication and repair, chromatin regulation, nucleotide and amino-acid metabolism, mitochondrial protein quality control, and proteasomal degradation. The network contains a relatively connected core around DDX39B, PCNA, ADK, GOT1 and PSMC6, with additional links joining metabolic, nuclear and proteostasis components. These annotations are mechanistic clues rather than enrichment evidence. The shared signal is therefore more consistent with a general cellular state or shared cell composition than with a specific autonomic-nervous-system or myometrial pathway.

**Cell composition.** The module is not dominated by secreted or plasma proteins, and the HPA summary does not indicate a broadly immune-enriched module. Most genes have low tissue specificity and low immune-cell specificity, while several show enhanced expression in muscle, bone marrow, esophagus or reproductive cell types. PGD is notably enriched in bone marrow and several blood-cell populations, and its HPA profile includes neutrophil-related cell types. Other genes show cell-type enhancement in spermatogenic, esophageal, neural or muscle-associated populations. Myometrium protein detection is present for most genes with available data, but the absence of matching autonomic-nervous-system tissue data limits tissue-level comparison. Overall, the module could partly reflect shared ubiquitous cellular programs, with possible contributions from blood or contaminating/shared cell populations; it should not be interpreted as a purified smooth-muscle or neuronal module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

At the stringent STRING interaction threshold, the only directly supported relationship is PCNA with RBBP4. This gives limited confirmation of a nuclear DNA-replication or chromatin-associated connection, but STRING reports no functional enrichment for the module. hu.MAP reports one complex, C1, containing AARS1 and PGD from this module alongside many proteins outside the module. Thus, C1 provides contextual support for a possible association of translation-related and metabolic proteins, but only a small portion of that complex is represented here and it does not establish that the whole co-abundance module is a stable physical complex. Most module edges are therefore co-abundance relationships rather than independently validated physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 78 gene pairs: PCNA–RBBP4 (0.714)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (AARS1, PGD; 2/57)

### Novelty

The shared co-abundance pattern may be a new observation, but the evidence is insufficient to call it a newly discovered biological complex or pathway. The absence of broad STRING enrichment and the limited hu.MAP overlap indicate that most relationships are not already represented as a coherent known interaction system. However, absence from those resources does not prove novelty, because co-abundance can reflect regulation, cell composition, technical context or indirect biology. A credible novelty claim would require replication in independent autonomic-nervous-system and myometrium datasets, adjustment for cell composition, and experimental or orthogonal validation of the strongest edges.

**Hypothesis.** Hypothesis: the module represents a shared cellular-maintenance state involving coordinated RNA processing, nuclear transport, DNA and chromatin handling, nucleotide and redox metabolism, mitochondrial peptide quality control and proteasomal turnover. In myometrium, this state could accompany active tissue maintenance or remodeling, while in autonomic-nervous-system samples it could arise from shared resident cell types or sample composition. PGD-associated hematopoietic signals and the broad HPA profiles raise an alternative hypothesis that part of the cross-tissue module is driven by common non-target cell contributions. These hypotheses require cell-resolved analysis and perturbation testing; they are not established by the enrichment results.

### Important genes

#### DDX39B

- **Related proteins** (co-abundance neighbors): PCNA (0.86), PGD (0.84), PSMC6 (0.82), ADK (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nuclear speckles; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 39B. This gene encodes a member of the DEAD box family of RNA-dependent ATPases that mediate ATP hydrolysis during pre-mRNA splicing. The encoded protein is an essential splicing factor required for association of U2 small nuclear ribonucleoprotein with pre-mRNA, and it also plays an important role in mRNA export from the nucleus to the cytoplasm. This gene belongs to a cluster of genes localized in th…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); Alzheimer disease (0.522); Parkinson disease (0.503); lysosomal storage disease (0.503); neurodevelopmental disorder (0.413)
- **Europe PMC papers**: 1037
- **Why important**: DDX39B is among the most connected genes in the module and links PCNA, PGD, PSMC6 and ADK, placing it at the interface of nuclear processing, metabolism and proteostasis. Its established function in spliceosomal assembly and nuclear mRNA export gives the module a plausible RNA-handling axis. It has nuclear-speckle localization, myometrial protein detection, disease associations spanning neurodegenerative and neurodevelopmental categories, and substantial literature support.
- **Conclusion**: Established evidence supports DDX39B as a central RNA-processing and export factor with strong network relevance. It is a plausible organizing marker of the module, but the data do not establish that it causally drives the shared tissue signal or that its RNA-processing function is specifically altered in either tissue.

#### PCNA

- **Related proteins** (co-abundance neighbors): HDGFL2 (0.89), DDX39B (0.86), ADK (0.81); STRING partners: RBBP4 (0.714)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proliferating cell nuclear antigen. The protein encoded by this gene is found in the nucleus and is a cofactor of DNA polymerase delta. The encoded protein acts as a homotrimer and helps increase the processivity of leading strand synthesis during DNA replication. In response to DNA damage, this protein is ubiquitinated and is involved in the RAD6-dependent DNA repair pathway. Two transcript variants encoding the same protein have b…
- **Diseases (Open Targets)**: ataxia-telangiectasia-like disorder (0.497); neurodegenerative disease (0.188); neoplasm (0.118); diabetes mellitus (0.116); hepatocellular carcinoma (0.113)
- **Europe PMC papers**: 61820
- **Why important**: PCNA is a highly connected module member linked to HDGFL2, DDX39B and ADK, and it is the module's strongest anchor to a known STRING relationship through RBBP4. Its established roles in DNA replication, chromatin organization, mismatch repair and damage response connect the module to genome maintenance. It has nucleoplasmic localization, myometrial protein detection, very extensive literature coverage and disease associations involving genome instability and neoplasia.
- **Conclusion**: Established evidence supports PCNA as a genome-maintenance and replication factor that may connect the nuclear part of the module. The co-abundance pattern is compatible with cellular proliferation or repair, but no globally corrected enrichment or direct tissue-specific mechanism demonstrates that interpretation.

#### ADK

- **Related proteins** (co-abundance neighbors): RBBP4 (0.84), PCNA (0.81), DDX39B (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenosine kinase. This gene an enzyme which catalyzes the transfer of the gamma-phosphate from ATP to adenosine, thereby serving as a regulator of concentrations of both extracellular adenosine and intracellular adenine nucleotides. Adenosine has widespread effects on the cardiovascular, nervous, respiratory, and immune systems and inhibitors of the enzyme could play an important pharmacological role in increasing …
- **Diseases (Open Targets)**: adenosine kinase deficiency (0.780); autosomal recessive non-syndromic intellectual disability (0.370); neurodegenerative disease (0.320); hypertensive disorder (0.294); essential hypertension (0.287)
- **Europe PMC papers**: 5244
- **Why important**: ADK links PCNA, RBBP4 and DDX39B, connecting the nuclear module segment with purine salvage and adenine-nucleotide regulation. Its established enzymatic role in adenosine and nucleotide metabolism provides a plausible metabolic input into a cellular-maintenance program. It has nucleoplasmic and cytosolic localization, liver-enhanced tissue expression, a well-described deficiency association and substantial literature support.
- **Conclusion**: Established evidence supports ADK as a nucleotide and adenosine-metabolism component with a strategically bridging network position. It could influence cellular energy or signaling state, but a specific ADK-mediated mechanism for the cross-tissue module remains hypothetical.

#### GOT1

- **Related proteins** (co-abundance neighbors): AARS1 (0.90), MESD (0.89), PSMC6 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamic-oxaloacetic transaminase 1. Glutamic-oxaloacetic transaminase is a pyridoxal phosphate-dependent enzyme which exists in cytoplasmic and mitochondrial forms, GOT1 and GOT2, respectively.  GOT plays a role in amino acid metabolism and the urea and tricarboxylic acid cycles. The two enzymes are homodimeric and show close homology. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); Parkinson disease (0.375); Alzheimer disease (0.367); lysosomal storage disease (0.356); obesity disorder (0.172)
- **Europe PMC papers**: 3793
- **Why important**: GOT1 is highly connected within the module, linking AARS1, MESD and PSMC6. Its established transaminase activity connects amino-acid metabolism with oxaloacetate and related central metabolic processes. HPA shows enhancement in heart muscle, skeletal muscle and tongue, which is relevant to a module shared with a contractile tissue, although its lack of myometrial protein detection argues for caution. It has broad disease associations and substantial literature volume.
- **Conclusion**: Established evidence supports GOT1 as a central metabolic component and a possible indicator of energetic or biosynthetic state. The network does not show that GOT1 specifically mediates autonomic or myometrial biology, and its tissue pattern could instead reflect general muscle-associated metabolism or sample composition.

#### PGD

- **Related proteins** (co-abundance neighbors): DDX39B (0.84); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: phosphogluconate dehydrogenase. 6-phosphogluconate dehydrogenase is the second dehydrogenase in the pentose phosphate shunt. Deficiency of this enzyme is generally asymptomatic, and the inheritance of this disorder is autosomal dominant. Hemolysis results from combined deficiency of 6-phosphogluconate dehydrogenase and 6-phosphogluconolactonase suggesting a synergism of the two enzymopathies. Several transcript variants encoding…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); Abnormality of the skeletal system (0.329); autoimmune disorder of central nervous system (0.246); smoking behavior (0.245); essential hypertension (0.199)
- **Europe PMC papers**: 8652
- **Why important**: PGD connects to DDX39B and is one of the two module members in hu.MAP complex C1. Its established role in the oxidative pentose-phosphate pathway supports NADPH regeneration and redox maintenance. HPA identifies strong association with bone marrow, esophageal cell types and multiple blood-cell populations, including neutrophil-related populations, making it important both mechanistically and for assessing cellular-composition confounding. It has extensive literature support and disease associations including hematologic, neurologic and vascular-related categories.
- **Conclusion**: Established evidence supports PGD as a redox and pentose-phosphate enzyme, and C1 provides limited complex-level context. Its blood and bone-marrow enrichment makes it especially important as a possible marker of shared hematopoietic or contaminating cell content rather than a specific smooth-muscle mechanism.

## Module 1

**Tissue pair**: autonomic_nervous_system and myometrium  
**Genes (10)**: ACO1, ACSL1, CAPN2, FKBP9, MEMO1, REXO2, PDIA4, RDX, SEC23A, STAT1

### Function

The module does not have a globally significant GO or KEGG annotation: no GO/KEGG term passed global correction. STRING supplied neither functional enrichment nor qualifying protein interactions. Nevertheless, the gene-level pattern suggests a composite cellular-maintenance program rather than a single established pathway. It combines lipid activation and fatty-acid handling through ACSL1, mitochondrial citrate and iron-responsive metabolism through ACO1, ER-to-Golgi trafficking through SEC23A, ER protein folding through PDIA4 and FKBP9, cytoskeletal and membrane organization through RDX and MEMO1, RNA surveillance through REXO2, and cytokine-responsive transcription through STAT1. The strongest internal co-abundance links connect these processes into partially separated neighborhoods, with REXO2 bridging mitochondrial or RNA-related biology to trafficking and membrane-associated genes, and ACSL1 linking lipid metabolism to ER-stress and cytokine-responsive components. Thus, the most defensible interpretation is a coordinated metabolic, proteostatic, trafficking, and stress-response state shared by cells present in autonomic nervous system and myometrium samples, not a proven canonical pathway.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: the HPA summary identifies only a minority as secreted, and the individual annotations mainly place proteins intracellularly, in mitochondria, cytosol, ER, Golgi, vesicles, nucleoplasm, or plasma membrane. Most genes have low tissue specificity, so the module is compatible with broadly expressed cellular functions. HPA does not support a strongly blood-cell-driven module overall, because most genes have low immune-cell specificity. ACSL1 has neutrophil-enriched evidence and FKBP9 has neutrophil-enhanced evidence, but this is not sufficient to define the entire module as a blood-cell signal. Tissue-enhanced signals occur in liver, adipose tissue, skeletal muscle, and adrenal gland, while cell-type annotations include hepatocytes, adipocytes, proximal tubule cells, esophageal cells, stromal or glial populations, and neutrophils. HPA protein detection is available for myometrium but not for a matching autonomic-nervous-system tissue; within myometrium, protein detection is limited to a minority of genes. These observations favor a shared cellular-state or shared-cell-type explanation over a secreted-protein module, while leaving sample composition as an important alternative explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING found no qualifying interaction among the module genes and no supplementary STRING enrichment. Therefore, the co-abundance edges should not be interpreted as established physical protein interactions. hu.MAP provides one partial complex observation: (hu.MAP huMAP3_12414.1) contains ACO1 and REXO2 together, although the module includes only part of that complex. This supports a possible connection between aconitase-associated metabolism and RNA surveillance or mitochondrial biology, but it does not establish that the whole module is one physical complex. Overall, the network appears to be a co-expression or co-abundance structure spanning several cellular compartments, with limited support from currently catalogued physical complexes.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12414.1 (ACO1, REXO2; 2/5)

### Novelty

The module may represent a previously unreported shared co-abundance configuration between autonomic nervous system and myometrium, because the supplied databases do not identify it as a STRING interaction network or as a broad hu.MAP complex. However, that is only a candidate novelty claim. Lack of STRING or hu.MAP support does not demonstrate biological novelty, and every selected process and gene has established biological precedent. The defensible conclusion is that the module-level organization and its tissue-pair sharing may be novel or under-described, whereas the underlying molecular functions are not shown to be novel. Confirmation would require comparison with published tissue co-expression modules, independent cohorts, cell-composition adjustment, and replication of the same gene relationships.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular adaptation in which lipid utilization and mitochondrial metabolic state are coordinated with ER protein folding, vesicle trafficking, cytoskeletal remodeling, and cytokine-responsive transcription. In this model, ACSL1 supplies activated fatty-acid substrates, ACO1 reports or regulates mitochondrial and iron-linked metabolic status, SEC23A and the PDIA4–FKBP9 system support secretory-pathway handling, RDX and MEMO1 connect membrane or cytoskeletal organization to cell behavior, STAT1 provides an inflammatory or interferon-responsive regulatory interface, and REXO2 contributes RNA or mitochondrial quality control. The observed pattern could arise from a shared smooth-muscle or stromal cellular state, a stress-responsive state common to the two tissues, or a mixture of related cell types. This mechanism is provisional because global enrichment was absent, STRING found no qualifying interactions, and the data are co-abundance rather than perturbation evidence.

### Important genes

#### REXO2

- **Related proteins** (co-abundance neighbors): SEC23A (0.87), MEMO1 (0.87), RDX (0.85), ACO1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_12414.1
- **Function (MyGene.info)**: RNA exonuclease 2. This gene encodes a 3'-to-5' exonuclease specific for small (primarily 5 nucleotides or less in length) single-stranded RNA and DNA oligomers. This protein may have a role in DNA repair, replication, and recombination, and in RNA processing and degradation. It may also be involved in resistance of human cells to UV-C-induced cell death through its role in the DNA repair process. [provided by RefSe…
- **Diseases (Open Targets)**: neurodegenerative disease (0.513); lysosomal storage disease (0.258); type 1 interferonopathy (0.185); glomerulonephritis (0.081); ulcerative colitis (0.076)
- **Europe PMC papers**: 303
- **Why important**: REXO2 is the most connected gene in the supplied module and links SEC23A, MEMO1, RDX, and ACO1. Its established function is a small-oligomer RNA and DNA exonuclease with roles in RNA processing, mitochondrial RNA surveillance, and possible DNA repair. It is also one of the two module members in the hu.MAP complex (hu.MAP huMAP3_12414.1), where it occurs with ACO1. Its literature volume is moderate, and its disease associations include neurodegenerative disease and lysosomal storage disease.
- **Conclusion**: Established evidence supports REXO2 as a central network connector involved in nucleic-acid quality control and as a partial member of (hu.MAP huMAP3_12414.1). It is a plausible mechanistic bridge between metabolic and quality-control signals, but the proposed bridge in this tissue pair remains a hypothesis because STRING provides no supporting interaction and no globally significant enrichment was detected.

#### ACSL1

- **Related proteins** (co-abundance neighbors): PDIA4 (0.87), STAT1 (0.86), CAPN2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 1. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. Several transcript variants enco…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.510); diabetes mellitus (0.501); diabetic neuropathy (0.404); neurodegenerative disease (0.368); menopause (0.334)
- **Europe PMC papers**: 4992
- **Why important**: ACSL1 connects the lipid-metabolic side of the module to PDIA4, STAT1, and CAPN2. Its established function is conversion of long-chain fatty acids into fatty acyl-CoA esters, supporting lipid biosynthesis and fatty-acid degradation. HPA shows tissue enhancement in adipose tissue, liver, and skeletal muscle, together with neutrophil-enriched evidence. It has extensive literature and disease associations involving diabetes, diabetic neuropathy, neurodegenerative disease, and menopause.
- **Conclusion**: Established evidence makes ACSL1 a strong candidate marker of lipid and energy-state biology within the module, with a possible contribution from tissue or neutrophil composition. It should not be treated as proof that the module is a lipid pathway, because no GO or KEGG term passed global correction and its module relationships are co-abundance associations.

#### STAT1

- **Related proteins** (co-abundance neighbors): ACSL1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal transducer and activator of transcription 1. The protein encoded by this gene is a member of the STAT protein family. In response to cytokines and growth factors, STAT family members are phosphorylated by the receptor associated kinases, and then form homo- or heterodimers that translocate to the cell nucleus where they act as transcription activators. The protein encoded by this gene can be activated by various ligands including interferon-…
- **Diseases (Open Targets)**: immunodeficiency 31B (0.786); chronic mucocutaneous candidiasis (0.775); autoimmune enteropathy and endocrinopathy - susceptibility to chronic infections syndrome (0.772); cancer (0.554); immunodeficiency disease (0.482)
- **Europe PMC papers**: 66602
- **Why important**: STAT1 is the module's direct regulatory and immune-signaling representative, connected to ACSL1. It is activated by interferons and other cytokines and regulates transcriptional responses including antiviral defense and mesenchymal-cell behavior. It has the largest literature volume among the module genes and strong disease associations involving immunodeficiency, infection susceptibility, autoimmunity-related disease, and cancer.
- **Conclusion**: Established evidence supports STAT1 as a biologically important cytokine-responsive transcription factor. Its presence raises the possibility that inflammatory or interferon-related state contributes to the shared module, but the module cannot be called an immune module: HPA generally indicates low immune-cell specificity, and no global enrichment or STRING enrichment supports that interpretation.

#### SEC23A

- **Related proteins** (co-abundance neighbors): ACO1 (0.92), CAPN2 (0.90), REXO2 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A is highly connected within the trafficking neighborhood, linking ACO1, CAPN2, and REXO2. It is an established COPII component required for ER-to-Golgi vesicle budding and intracellular protein transport. Its literature volume is substantial, and its disease associations include craniolenticulosutural dysplasia and metabolic or reproductive disease-related phenotypes.
- **Conclusion**: Established evidence supports SEC23A as a plausible indicator of secretory-pathway and ER export activity in the module. The module-level interpretation that trafficking is coordinated with metabolism and stress responses is a hypothesis rather than an established complex, because SEC23A has no qualifying STRING partner in this gene set and no hu.MAP assignment here.

#### PDIA4

- **Related proteins** (co-abundance neighbors): ACSL1 (0.87), FKBP9 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 connects ACSL1 to FKBP9 and represents ER proteostasis. It is an ER protein disulfide isomerase involved in protein folding, protein secretion, thiol-disulfide exchange, and ER-stress responses. HPA places it in intracellular and membrane-associated secretome categories and reports detection in myometrium. Its literature includes links to neurodegenerative disease, liver disorders, and ovarian malignancy.
- **Conclusion**: Established evidence supports PDIA4 as a marker of ER folding capacity and stress handling. Its co-abundance with ACSL1 and FKBP9 is consistent with coordination between lipid state and proteostasis, but causality and tissue-specific direction cannot be inferred from this module alone.

#### ACO1

- **Related proteins** (co-abundance neighbors): SEC23A (0.92), REXO2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12414.1
- **Function (MyGene.info)**: aconitase 1. The protein encoded by this gene is a bifunctional, cytosolic protein that functions as an essential enzyme in the TCA cycle and interacts with mRNA to control the levels of iron inside cells. When cellular iron levels are high, this protein binds to a 4Fe-4S cluster and functions as an aconitase. Aconitases are iron-sulfur proteins that function to catalyze the conversion of citrate to isocitrate…
- **Diseases (Open Targets)**: smoking initiation (0.300); smoking behavior (0.277); ovarian neoplasm (0.276); attention deficit-hyperactivity disorder (0.261); substance abuse (0.261)
- **Europe PMC papers**: 3372
- **Why important**: ACO1 is a member of the hu.MAP partial complex (hu.MAP huMAP3_12414.1) with REXO2 and is connected to SEC23A and REXO2 in the module. It is an established bifunctional protein that catalyzes citrate-to-isocitrate conversion when carrying its iron-sulfur cluster and regulates iron-responsive translation when acting through iron-responsive elements. HPA shows liver tissue enhancement and cell-type enhancement in adipocytes, hepatocytes, and proximal tubule cells. It has a substantial literature and disease associations involving ovarian neoplasm and substance-use-related phenotypes.
- **Conclusion**: Established evidence supports ACO1 as a key metabolic and iron-sensing component. Its partnership with REXO2 in (hu.MAP huMAP3_12414.1) provides the clearest complex-level support for a metabolic-quality-control connection, but the broader proposed link to trafficking and inflammatory signaling remains hypothetical.

## Module 3

**Tissue pair**: autonomic_nervous_system and myometrium  
**Genes (6)**: CZIB, DCUN1D1, GGCT, EIF6, RAB21, TPD52L2

### Function

No GO or KEGG term passed global correction, so there is no statistically supported pathway-level annotation for this module. The gene-level annotations suggest a weakly integrated intracellular maintenance program rather than a single established biological pathway. TPD52L2 is the most connected node and links RAB21, EIF6, and CZIB in the co-abundance graph. EIF6 connects to DCUN1D1 and GGCT, producing an architecture with two central nodes and several peripheral partners. The associated functions span membrane trafficking and adhesion regulation through RAB21, translation-related and ribosomal processes through EIF6, ubiquitin and neddylation regulation through DCUN1D1, and glutathione catabolism through GGCT. These functions are biologically plausible as cellular-support processes, but their joint interpretation remains inferential because there is no globally significant enrichment and no STRING functional enrichment.

**Cell composition.** The module does not resemble a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It also does not show a blood-cell signature, because all genes have low immune-cell specificity and no enriched blood-cell population is reported. Most genes have low tissue specificity, which is compatible with broadly expressed cellular machinery rather than a specialized autonomic or myometrial program. A minority of the genes show reproductive or epithelial cell-type associations, especially late spermatids, esophageal cell populations, gastric progenitor cells, and decidual stromal cells. One gene is tissue enriched in testis. This pattern raises the possibility that the shared signal reflects a broadly expressed intracellular program, cell-state composition, or technical co-abundance rather than a tissue-specific mechanism. In myometrium, HPA protein detection is mixed across the genes; the autonomic nervous system has no matching HPA tissue for protein comparison.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no reported hu.MAP complex containing multiple module members. Thus, the co-abundance edges are not corroborated here as established physical or functional interactions by these resources. The graph nevertheless has an internally suggestive organization: TPD52L2 is the central co-abundance connector for RAB21, EIF6, and CZIB, while EIF6 connects with DCUN1D1 and GGCT. This supports coordinated expression but not direct molecular binding. The absence of STRING and hu.MAP support also means that the apparent bridge between vesicle-related, translation-related, ubiquitin-related, and redox-related functions should be treated cautiously.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a previously unreported co-abundance association in the autonomic nervous system and myometrium tissue pair, because the module is not represented by a known STRING interaction pattern or a shared hu.MAP complex. However, it cannot be called a new biological mechanism on that basis alone. Database absence may reflect incomplete coverage, context dependence, indirect regulation, or correlations caused by shared cell states. The lack of globally significant GO or KEGG enrichment further limits claims of pathway novelty. The strongest defensible conclusion is that the tissue-pair co-abundance pattern is potentially novel, while its molecular interpretation remains provisional and requires replication and independent interaction or perturbation evidence.

**Hypothesis.** Hypothesis: the module may mark a shared intracellular cell-maintenance state in which vesicle and adhesion trafficking, translational capacity, protein neddylation, and glutathione handling vary together across samples. TPD52L2 and EIF6 could act as expression-level bridges between these processes, with RAB21 contributing membrane trafficking, DCUN1D1 contributing ubiquitin-system regulation, and GGCT contributing redox-related metabolite handling. This is a hypothesis about coordinated cellular state, not evidence of a physical multiprotein complex or a demonstrated causal pathway. The broad HPA expression pattern and the lack of database-supported interactions make cell composition and general cellular activity important alternative explanations.

### Important genes

#### TPD52L2

- **Related proteins** (co-abundance neighbors): RAB21 (0.84), EIF6 (0.83), CZIB (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TPD52 like 2. This gene encodes a member of the tumor protein D52-like family. These proteins are characterized by an N-terminal coiled-coil motif that is used to form homo- and heteromeric complexes with other tumor protein D52-like proteins. Expression of this gene may be a marker for breast cancer and acute lymphoblastic leukemia. Alternatively spliced transcript variants encoding multiple isoforms have been…
- **Diseases (Open Targets)**: breast cancer (0.088); breast carcinoma (0.087); neoplasm (0.078); gastric cancer (0.078); posterior cortical atrophy (0.077)
- **Europe PMC papers**: 1316
- **Why important**: TPD52L2 has the strongest network position and connects the largest set of module partners, including RAB21, EIF6, and CZIB. Its tumor protein D family membership and coiled-coil architecture support a potential role in protein-complex organization, while its vesicular localization is compatible with the trafficking-related interpretation. It has broad tissue specificity, neuronal and glial cell-type enhancement, myometrial protein detection, disease associations involving breast and gastric cancer, and substantial literature coverage.
- **Conclusion**: Established evidence supports TPD52L2 as the central co-abundance connector and as a member of a coiled-coil protein family associated with vesicles and cancer-related expression. It is a plausible module anchor, but there is no STRING or hu.MAP evidence here establishing direct interaction with the other module genes. Its role as a functional coordinator in this tissue pair remains a hypothesis.

#### EIF6

- **Related proteins** (co-abundance neighbors): DCUN1D1 (0.84), TPD52L2 (0.83), GGCT (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 6. Hemidesmosomes are structures which link the basal lamina to the intermediate filament cytoskeleton. An important functional component of hemidesmosomes is the integrin beta-4 subunit (ITGB4), a protein containing two fibronectin type III domains. The protein encoded by this gene binds to the fibronectin type III domains of ITGB4 and may help link ITGB4 to the intermediate filament cytoskeleton. T…
- **Diseases (Open Targets)**: neurodegenerative disease (0.153); urolithiasis (0.135); alcohol drinking (0.135); exstrophy-epispadias complex (0.118); freckles (0.115)
- **Europe PMC papers**: 1420
- **Why important**: EIF6 is a second highly connected node and links TPD52L2 with DCUN1D1 and GGCT. Its curated annotations involve ribosomal subunit export, ribosomal RNA maturation, translation initiation, glycolytic regulation, and insulin response, giving it a plausible cellular-capacity role within the module. It has broad tissue specificity, epithelial cell-type enhancement, disease associations including neurodegenerative disease, and substantial literature coverage.
- **Conclusion**: Established evidence supports EIF6 as a translation- and ribosome-related factor with a central position in the co-abundance graph. Its bridging position makes it important for interpreting the module as a general intracellular state. A direct mechanistic connection between EIF6 and the other module genes is not established by the supplied STRING or hu.MAP results.

#### RAB21

- **Related proteins** (co-abundance neighbors): TPD52L2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB21, member RAS oncogene family. This gene belongs to the Rab family of monomeric GTPases, which are involved in the control of cellular membrane traffic. The encoded protein plays a role in the targeted trafficking of integrins via its association with integrin alpha tails. As a consequence, the encoded protein is involved in the regulation of cell adhesion and migration. Expression of this gene is associated with a poor prognos…
- **Diseases (Open Targets)**: neurodegenerative disease (0.469); small intestine neuroendocrine neoplasm (0.095); neoplasm (0.085); posterior cortical atrophy (0.074); nonpapillary renal cell carcinoma (0.065)
- **Europe PMC papers**: 999
- **Why important**: RAB21 is the module's clearest membrane-trafficking and adhesion-related component. Its established annotations include intracellular transport, exocytosis, receptor-mediated endocytosis, axonal transport, and regulation of adhesion and migration through integrin trafficking. It is connected to TPD52L2, shows enhancement in spermatids and neutrophils, has myometrial protein detection, and has disease associations involving neurodegenerative disease and neoplasia.
- **Conclusion**: Established evidence supports RAB21 as a regulator of membrane traffic, integrin handling, and cell movement. Its peripheral network position means it does not by itself define the whole module, but it provides a biologically coherent trafficking arm. Linking RAB21 mechanistically to EIF6 or TPD52L2 in this tissue pair is currently a hypothesis.

#### DCUN1D1

- **Related proteins** (co-abundance neighbors): EIF6 (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: defective in cullin neddylation 1 domain containing 1. Enables cullin family protein binding activity. Involved in positive regulation of protein neddylation and regulation of protein ubiquitination. Located in cytosol and nucleoplasm. Part of ubiquitin ligase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.517); Parkinson disease (0.249); macular degeneration (0.217); alcohol drinking (0.206); Lewy body dementia (0.123)
- **Europe PMC papers**: 361
- **Why important**: DCUN1D1 is the module's most specialized tissue-associated gene in the HPA summary, being tissue enriched in testis and cell-type enriched in late spermatids. Its curated function involves cullin binding and positive regulation of protein neddylation and ubiquitination. Although peripheral in the co-abundance graph, it connects directly to EIF6 and may represent a regulatory arm distinct from trafficking and translation. It also has disease associations involving neurodegenerative disorders and Parkinson disease.
- **Conclusion**: Established evidence supports DCUN1D1 as a regulator of cullin neddylation and ubiquitination, with a notable reproductive-cell expression pattern. Its presence may reflect a shared regulatory state or cell-type contribution rather than a myometrial-specific mechanism. Any proposed coordination with EIF6 or the rest of the module remains unproven.

#### GGCT

- **Related proteins** (co-abundance neighbors): EIF6 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gamma-glutamylcyclotransferase. The protein encoded by this gene catalyzes the formation of 5-oxoproline from gamma-glutamyl dipeptides, the penultimate step in glutathione catabolism, and may play a critical role in glutathione homeostasis. The encoded protein may also play a role in cell proliferation, and the expression of this gene is a potential marker for cancer. Pseudogenes of this gene are located on the long arm of chro…
- **Diseases (Open Targets)**: ovarian neoplasm (0.161); male reproductive organ cancer (0.137); nephritis (0.104); Nephropathy (0.104); thyroid gland papillary carcinoma (0.103)
- **Europe PMC papers**: 1442
- **Why important**: GGCT contributes the clearest metabolic and redox-related annotation. It catalyzes a step in glutathione catabolism and may contribute to glutathione homeostasis and cell proliferation. It is connected to EIF6, shows broad tissue specificity with several epithelial and reproductive cell-type enhancements, has myometrial protein detection, and has disease associations involving ovarian and other neoplasms as well as nephritis.
- **Conclusion**: Established evidence supports GGCT as a glutathione-catabolism enzyme with possible relevance to redox balance and proliferation. Its network position makes it a peripheral contributor to the proposed intracellular-state interpretation. Whether GGCT activity is coordinated with translation or trafficking in these tissues is a hypothesis requiring functional testing.

## Module 4

**Tissue pair**: autonomic_nervous_system and myometrium  
**Genes (9)**: DBNL, EHD1, EPS15L1, GCLC, EIF4G1, NSFL1C, TSG101, UBQLN2, XPNPEP1

### Function

No GO/KEGG term passed global correction, so the module does not support a formally significant pathway assignment. Its gene-level annotations and co-abundance structure instead suggest a possible intracellular membrane-trafficking and proteostasis program, with links to endocytosis, endosomal transport, vesicle-mediated transport, ubiquitin-dependent degradation, translation, and protection from oxidative stress. EHD1 is the principal network connector, linking EPS15L1, UBQLN2, DBNL, XPNPEP1, and EIF4G1, while EPS15L1 and DBNL provide additional connectivity. These relationships are biologically coherent at the level of cellular logistics, but the absence of globally significant enrichment means this interpretation remains functional inference rather than enrichment-based proof.

**Cell composition.** The module is not dominated by secreted or plasma proteins: no member is annotated as secreted. Most genes have low tissue specificity, and most have low blood-cell specificity, arguing against a simple plasma-protein or broad blood-contamination explanation. Nevertheless, HPA single-cell annotations repeatedly point to esophageal epithelial cells, neutrophils, platelets, spermatids, and other specialized cell types, with one member showing immune-cell enhancement. The module may therefore reflect a shared intracellular program or shared cell-type composition rather than a tissue-specific autonomic-nervous-system or myometrial pathway. Protein detection in myometrium is widespread among the members, whereas matching autonomic-nervous-system protein data are unavailable; this supports presence in myometrium but does not establish tissue-specific activity.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair met the supplied high-confidence STRING interaction criterion, no supplementary STRING functional-enrichment result was reported, and no hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not independently corroborated by the cited interaction or complex resources. The lack of STRING and hu.MAP support weakens claims that the entire module is a pre-existing physical complex, but it does not invalidate co-regulation or indirect functional coupling. The strongest internal structure is centered on EHD1 and EPS15L1, with DBNL connecting trafficking-related genes to GCLC and NSFL1C.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a newly discovered molecular complex or definitively novel pathway. Its component functions are established and several genes are extensively studied, while the absence of STRING or hu.MAP representation alone cannot prove novelty. The potentially novel aspect is the tissue-pair-specific co-abundance combination and its internal organization around EHD1, EPS15L1, DBNL, and associated proteostasis, translation, peptide-processing, and redox genes. That claim requires independent replication, cell-composition control, and comparison with other tissue pairs before it can be considered a new biological finding.

**Hypothesis.** Hypothesis: in a shared cell population present in autonomic nervous system and myometrium, altered membrane turnover and endocytic trafficking are co-regulated with protein quality control, translational capacity, peptide processing, and glutathione synthesis. EHD1, EPS15L1, and DBNL could form a trafficking-associated regulatory backbone; UBQLN2 and NSFL1C could connect this state to ubiquitin-dependent proteostasis and membrane-compartment recovery; EIF4G1 and GCLC could reflect coordinated control of protein production and oxidative-stress buffering. XPNPEP1 may link the state to neuropeptide or peptide-hormone processing. This is a mechanistic proposal, not an established module-level causal mechanism.

### Important genes

#### EHD1

- **Related proteins** (co-abundance neighbors): UBQLN2 (0.88), XPNPEP1 (0.88), EPS15L1 (0.87), DBNL (0.86), EIF4G1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Plasma membrane; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EH domain containing 1. This gene belongs to a highly conserved gene family encoding EPS15 homology (EH) domain-containing proteins. The protein-binding EH domain was first noted in EPS15, a substrate for the epidermal growth factor receptor. The EH domain has been shown to be an important motif in proteins involved in protein-protein interactions and in intracellular sorting. The protein encoded by this gene is thought …
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.107); neoplasm (0.101); device complication (0.091); lung adenocarcinoma (0.079); osteosarcoma (0.074)
- **Europe PMC papers**: 1857
- **Why important**: EHD1 has the strongest network connectivity in the supplied subgraph and links the central trafficking-related cluster to UBQLN2, XPNPEP1, EPS15L1, DBNL, and EIF4G1. Its established annotations include endocytosis, intracellular protein transport, endocytic recycling, and possible IGF receptor internalization. It is detected in myometrium and has a substantial literature base, making it the most informative anchor for interpreting the module.
- **Conclusion**: Established evidence supports EHD1 as an endocytic and recycling factor and as the principal network connector. The hypothesis that it organizes the entire shared module is plausible from network position but is not demonstrated by STRING, hu.MAP, or enrichment evidence.

#### EPS15L1

- **Related proteins** (co-abundance neighbors): UBQLN2 (0.90), EHD1 (0.87), DBNL (0.86), TSG101 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: epidermal growth factor receptor pathway substrate 15 like 1. Enables cadherin binding activity. Predicted to be involved in endocytosis and endosomal transport. Located in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: split hand-foot malformation (0.370); lysosomal storage disease (0.310); neurodegenerative disease (0.310); Alzheimer disease (0.310); Parkinson disease (0.310)
- **Europe PMC papers**: 426
- **Why important**: EPS15L1 is a highly connected member adjacent to EHD1, UBQLN2, DBNL, and TSG101. Its gene-level annotations support endocytosis, endosomal transport, synaptic-vesicle endocytosis, cadherin binding, and membrane localization. Its presence in myometrium and association with neurodegenerative and lysosomal disease categories make it relevant to both trafficking biology and disease interpretation.
- **Conclusion**: Established evidence supports EPS15L1 as a membrane-associated endocytic factor. Its position beside EHD1 and TSG101 supports a trafficking interpretation, but a direct physical complex or tissue-specific causal role is not established here.

#### DBNL

- **Related proteins** (co-abundance neighbors): EHD1 (0.86), EPS15L1 (0.86), GCLC (0.85), NSFL1C (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: drebrin like. Enables cadherin binding activity. Predicted to be involved in several processes, including Rac protein signal transduction; nervous system development; and podosome assembly. Located in cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: glycogen storage disease due to phosphoglycerate mutase deficiency (0.554); rhabdomyolysis (0.259); hereditary disease (0.192); Abnormality of the skeletal system (0.126); neoplasm (0.080)
- **Europe PMC papers**: 541
- **Why important**: DBNL is a central connector linking EHD1 and EPS15L1 to GCLC and NSFL1C. Its annotations include membrane organization, endocytosis, Rac signaling, synapse assembly, neuron projection morphogenesis, and podosome assembly. HPA places it in vesicles and at the plasma membrane and highlights platelet, megakaryocyte, epithelial, and Hofbauer-cell expression, which is important when considering cell-composition effects.
- **Conclusion**: Established evidence supports DBNL as a cytoplasmic membrane-organizing and actin-associated factor. Its bridging position suggests a possible connection between trafficking and stress-related processes, but the module does not establish that DBNL mediates this connection in either tissue.

#### UBQLN2

- **Related proteins** (co-abundance neighbors): EPS15L1 (0.90), EHD1 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquilin 2. This gene encodes an ubiquitin-like protein (ubiquilin) that shares high degree of similarity with related products in yeast, rat and frog. Ubiquilins contain a N-terminal ubiquitin-like domain and a C-terminal ubiquitin-associated domain. They physically associate with both proteasomes and ubiquitin ligases; and thus, are thought to functionally link the ubiquitination machinery to the proteasome…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis type 15 (0.798); amyotrophic lateral sclerosis (0.644); familial amyotrophic lateral sclerosis (0.508); juvenile amyotrophic lateral sclerosis (0.372); amyotrophic lateral sclerosis, dominant (0.370)
- **Europe PMC papers**: 1702
- **Why important**: UBQLN2 connects directly to EHD1 and EPS15L1 and has established roles in ubiquitin-dependent protein catabolism, autophagosome assembly, ER-associated degradation, and regulation of clathrin-dependent endocytosis. Its disease associations include amyotrophic lateral sclerosis, and it has a substantial literature base. It therefore provides a strong proteostasis dimension to the otherwise trafficking-centered interpretation.
- **Conclusion**: Established evidence supports UBQLN2 as a proteostasis and degradation regulator with links to endocytosis. Its co-abundance with the trafficking genes is consistent with coordinated membrane-protein quality control, but this coordination remains a hypothesis.

#### GCLC

- **Related proteins** (co-abundance neighbors): DBNL (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamate-cysteine ligase catalytic subunit. Glutamate-cysteine ligase, also known as gamma-glutamylcysteine synthetase is the first rate-limiting enzyme of glutathione synthesis. The enzyme consists of two subunits, a heavy catalytic subunit and a light regulatory subunit. This locus encodes the catalytic subunit, while the regulatory subunit is derived from a different gene located on chromosome 1p22-p21. Mutations at this locus have been …
- **Diseases (Open Targets)**: gamma-glutamylcysteine synthetase deficiency (0.766); cystic fibrosis (0.375); neurodegenerative disease (0.373); non-autoimmune hemolytic anemia (0.370); lung adenocarcinoma (0.331)
- **Europe PMC papers**: 8941
- **Why important**: GCLC is connected to DBNL and encodes the catalytic subunit of the rate-limiting enzyme for glutathione synthesis. Its annotations include glutathione biosynthesis, oxidative-stress response, nutrient response, and hormone response. It is tissue-enhanced in liver, immune-cell enhanced for NK cells, detected in myometrium, and associated with inherited glutathione-synthesis deficiency and hemolytic anemia, giving it a clear redox and disease-relevance dimension.
- **Conclusion**: Established evidence supports GCLC as a core glutathione-biosynthesis enzyme. Its connection to DBNL may indicate coupling between membrane organization and redox buffering, but the module cannot establish whether oxidative stress drives the co-abundance pattern or is merely correlated with it.
