# Conserved co-abundance modules: cell line and kidney

## Module 0

**Tissue pair**: cell line and kidney  
**Genes (6)**: ABHD14B, APOA1, CNDP2, PCCB, MPST, TKFC

### Function

The module is most consistent with a liver- and intestine-associated metabolic co-abundance program linked to circulating lipid transport, carbohydrate and glycerol metabolism, sulfur-amino-acid handling, peptide and glutathione metabolism, and propionyl-CoA catabolism. APOA1 is the central co-abundance hub and provides the strongest functional anchor through HDL biology, cholesterol efflux, lipid transport, and plasma protein secretion. The remaining genes represent distinct intracellular metabolic activities rather than a single established biochemical complex. No GO or KEGG term passed global correction, so the functional interpretation rests on the individual gene annotations, tissue and cell-type patterns, and the network structure rather than on a globally significant enrichment term.

**Cell composition.** The module is not predominantly an immune-cell module and is not broadly characterized as a housekeeping set. HPA evidence instead points toward hepatic and intestinal biology, especially hepatocytes and enterocytes, with additional cell-type associations for other epithelial and specialized cells. APOA1 is the sole secreted-to-blood protein and is not detected by kidney immunohistochemistry, whereas the other members are intracellular and are detected in kidney tissue. Most members show low immune-cell specificity, with APOA1 having an immune-cell-enhanced association with plasmacytoid dendritic cells. Thus, the shared cell-line and kidney module may reflect a conserved metabolic or tissue-composition signal, and possibly a contribution from circulating or sample-associated APOA1, rather than a blood-cell program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The co-abundance network has a hub-and-spoke organization centered on APOA1, with each other member connected to that hub and no reported high-confidence STRING interaction among any gene pair. There are no hu.MAP complexes containing multiple module members. STRING supplementary tissue evidence links TKFC, MPST, CNDP2, PCCB, and ABHD14B to kidney tissue in (STRING TISSUES Kidney; within-query FDR = 0.0314), but this is supplementary within-query evidence and is not global enrichment evidence. The lack of STRING and hu.MAP relationships argues against interpreting the module as a known physical protein complex. It is more compatible with coordinated abundance, shared tissue regulation, sample composition, or convergent metabolic state.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Kidney (FDR = 0.0314, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a candidate novel co-abundance association rather than a demonstrated new molecular complex or pathway. The shared module appears not to be represented by a known STRING interaction network or hu.MAP complex, which supports novelty at the observed co-abundance-pattern level but cannot establish biological novelty by itself. The absence of globally significant GO or KEGG enrichment further indicates that the module does not map cleanly onto an established annotated pathway. A cautious claim is therefore that coordinated abundance of APOA1 with these metabolic genes across the cell-line and kidney setting may be a previously uncharacterized association, requiring independent cohorts, targeted protein measurements, and perturbation experiments.

**Hypothesis.** Hypothesis: the module reflects a conserved tissue-associated metabolic state in which APOA1 marks hepatic or intestinal lipid handling and is co-regulated with intracellular pathways for glycerol and carbohydrate utilization, sulfur transfer and detoxification, glutathione-related metabolism, peptide turnover, and propionyl-CoA breakdown. The apparent network hub may represent coordinated regulation or shared sample context rather than direct binding. Kidney detection of the intracellular members could reflect a conserved metabolic program, while APOA1 may contribute through circulating protein carryover or tissue-associated lipoprotein exposure. This hypothesis should be tested by examining transcript and protein concordance, cell-type-resolved data, lipid and metabolite measurements, and perturbation of APOA1-associated metabolic conditions.

### Important genes

#### APOA1

- **Related proteins** (co-abundance neighbors): TKFC (0.88), MPST (0.88), CNDP2 (0.85), PCCB (0.82), ABHD14B (0.80); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is the central network hub and the only secreted-to-blood member. Its established role as the major HDL protein, mediator of cholesterol efflux, and cofactor for LCAT gives the module its clearest biological anchor. HPA places it in liver and enterocyte or hepatocyte-associated contexts, and its disease associations include primary hypoalphalipoproteinemia, APOA1 deficiency, and familial visceral amyloidosis. It also has by far the largest literature volume among the module genes, making it the best-supported interpretive marker.
- **Conclusion**: Established evidence supports APOA1 as a liver- and intestine-associated circulating lipid-transport protein and as the principal organizational marker of this co-abundance module. It is not established that APOA1 directly regulates the other members; that connection remains a hypothesis.

#### TKFC

- **Related proteins** (co-abundance neighbors): APOA1 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: triokinase and FMN cyclase. This gene is a member of the family of dihydroxyacetone kinases, which have a protein structure distinct from other kinases. The product of this gene phosphorylates dihydroxyacetone, and also catalyzes the formation of riboflavin 4',5'-phosphate (aka cyclin FMN) from FAD. Several alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jun 2017].
- **Diseases (Open Targets)**: triokinase and FMN cyclase deficiency syndrome (0.627); Sengers syndrome (0.403); COVID-19 (0.371); inborn errors of metabolism (0.333); cardiomyopathy (0.185)
- **Europe PMC papers**: 415
- **Why important**: TKFC is directly connected to the APOA1 hub and has a coherent tissue pattern in intestine and liver, including enterocytes and hepatocytes. Its annotated functions in dihydroxyacetone phosphorylation, glycerol and fructose metabolism, and FMN cyclase activity provide a plausible intermediary-metabolic link to the APOA1-centered tissue program. It also contributes the supplementary kidney-tissue signal in (STRING TISSUES Kidney; within-query FDR = 0.0314) and has a disease association with triokinase and FMN cyclase deficiency syndrome.
- **Conclusion**: Established evidence supports TKFC as an intracellular metabolic enzyme with liver- and intestine-associated expression and a kidney-relevant supplementary signal. Its co-abundance with APOA1 may indicate shared metabolic regulation, but direct functional coupling to APOA1 is not established.

#### MPST

- **Related proteins** (co-abundance neighbors): APOA1 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mercaptopyruvate sulfurtransferase. This protein encoded by this gene catalyzes the transfer of a sulfur ion from 3-mercaptopyruvate to cyanide or other thiol compounds. It may be involved in cysteine degradation and cyanide detoxification. There is confusion in literature between this protein (mercaptopyruvate sulfurtransferase, MPST), which appears to be cytoplasmic, and thiosulfate sulfurtransferase (rhodanese, TST, GeneID:7263),…
- **Diseases (Open Targets)**: neurodegenerative disease (0.261); COVID-19 (0.164); severe acute respiratory syndrome (0.163); colitis (0.080); non-alcoholic fatty liver (0.078)
- **Europe PMC papers**: 1532
- **Why important**: MPST is connected to APOA1 and encodes a sulfurtransferase involved in mercaptopyruvate and cyanide or thiol handling, cysteine degradation, and detoxification-related biology. Its liver and intestinal cell-type associations, mitochondrial localization, kidney detection, and supplementary kidney signal in (STRING TISSUES Kidney; within-query FDR = 0.0314) make it relevant to a tissue metabolic interpretation. Its literature base is substantial relative to most of the module, and its annotations include sulfur-amino-acid catabolism and response to toxic substance.
- **Conclusion**: Established evidence supports MPST as a sulfur-transfer and detoxification enzyme associated with hepatic, intestinal, and kidney contexts. A role in an APOA1-linked metabolic state is plausible but remains a hypothesis rather than a demonstrated biochemical relationship.

#### CNDP2

- **Related proteins** (co-abundance neighbors): APOA1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carnosine dipeptidase 2. CNDP2, also known as tissue carnosinase and peptidase A (EC 3.4.13.18), is a nonspecific dipeptidase rather than a selective carnosinase (Teufel et al., 2003 [PubMed 12473676]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: refractive error (0.436); duodenal ulcer (0.344); Abnormality of refraction (0.330); myopia (0.255); kidney disorder (0.253)
- **Europe PMC papers**: 898
- **Why important**: CNDP2 is directly connected to APOA1 and encodes a broadly acting intracellular dipeptidase associated with proteolysis and glutathione metabolism. Its enterocyte and other tissue-cell associations, kidney detection, and inclusion in the supplementary kidney signal in (STRING TISSUES Kidney; within-query FDR = 0.0314) support relevance to tissue metabolic state. Its disease associations include kidney disorder and gastrointestinal conditions, while its literature volume provides more support than the least characterized module members.
- **Conclusion**: Established evidence supports CNDP2 as an intracellular peptidase with links to peptide and glutathione metabolism. Its relationship to APOA1 and the other module genes is currently a co-abundance observation, not an established pathway or physical interaction.

#### PCCB

- **Related proteins** (co-abundance neighbors): APOA1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: propionyl-CoA carboxylase subunit beta. The protein encoded by this gene is a subunit of the propionyl-CoA carboxylase (PCC) enzyme, which is involved in the catabolism of propionyl-CoA. PCC is a mitochondrial enzyme that probably acts as a dodecamer of six alpha subunits and six beta subunits. This gene encodes the beta subunit of PCC. Defects in this gene are a cause of propionic acidemia type II (PA-2). Multiple transcript variants e…
- **Diseases (Open Targets)**: propionic acidemia (0.861); hereditary disease (0.517); hypertensive disorder (0.453); coronary artery disorder (0.438); coronary atherosclerosis (0.428)
- **Europe PMC papers**: 1404
- **Why important**: PCCB is connected to APOA1 and encodes the beta subunit of mitochondrial propionyl-CoA carboxylase, an enzyme required for propionyl-CoA and branched-chain substrate catabolism. Its liver enrichment, kidney detection, supplementary kidney signal in (STRING TISSUES Kidney; within-query FDR = 0.0314), and strong disease association with propionic acidemia make it an important marker of mitochondrial intermediary metabolism. Its literature volume is substantial and its enzymatic role is well established.
- **Conclusion**: Established evidence supports PCCB as a mitochondrial catabolic enzyme and disease-relevant metabolic marker. Its co-abundance with APOA1 may reflect shared hepatic or tissue metabolic regulation, but no direct interaction or common complex is established.

## Module 1

**Tissue pair**: cell line and kidney  
**Genes (17)**: ACLY, COPB1, CYFIP1, DDX6, DYNC1H1, FLII, EIF4G1, NCKAP1, NUP160, EPRS1, IARS1, LARS1, QARS1, VARS1, SNRNP200, VPS45, XPO1

### Function

The strongest interpretation is a cytosolic protein-biosynthesis and translational-fidelity module centered on aminoacyl-tRNA charging. The primary evidence is the globally corrected enrichment for the aminoacyl-tRNA synthetase multienzyme complex (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.000585), aminoacyl-tRNA ligase activity (GO:MF aminoacyl-tRNA ligase activity; q_global = 0.00117), tRNA aminoacylation for protein translation (GO:BP tRNA aminoacylation for protein translation; q_global = 0.00117), amino acid activation (GO:BP amino acid activation; q_global = 0.00169), aminoacyl-tRNA metabolism involved in translational fidelity (GO:BP aminoacyl-tRNA metabolism involved in translational fidelity; q_global = 0.016), and aminoacyl-tRNA biosynthesis (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 0.00169). The broader translation and protein-biosynthetic-process terms (GO:BP translation; q_global = 0.00723) and (GO:BP protein biosynthetic process; q_global = 0.00723) support a role in supplying correctly charged tRNAs for protein synthesis. The presence of RNA-processing and translation-control genes, including DDX6, SNRNP200, EIF4G1, NUP160 and XPO1, suggests that the module is not merely a list of synthetases but is connected to RNA handling, translational regulation, and nucleocytoplasmic communication. The ATP- and adenyl-ribonucleotide-binding terms (GO:MF ATP binding; q_global = 0.0274) and (GO:MF adenyl ribonucleotide binding; q_global = 0.0287) are consistent with the energy-dependent chemistry of aminoacylation, but they are broader supporting evidence rather than a separate module function.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly intracellular. The genes are largely broadly expressed, with low tissue specificity for most members, rather than being strongly restricted to kidney. Protein detection in kidney is widespread across the annotated module, consistent with the module being biologically present in kidney rather than representing a kidney-exclusive program. The module also does not appear to be dominated by blood-cell genes. Most members have low immune-cell specificity, while CYFIP1 shows enrichment across monocyte and myeloid-dendritic-cell categories and NCKAP1 and VARS1 are not detected in immune cells according to the supplied HPA summary. Therefore, a blood-contamination explanation is not favored by the HPA evidence, although shared abundance of broadly expressed housekeeping and translation-related proteins may reflect common cellular requirements in the cell line and kidney samples. The HPA cell-type signals involving spermatids, neural or glial cells, epithelial cells, and pancreatic islet cells should be viewed as context for expression breadth rather than evidence that those cell types drive this particular shared module.

**GO/KEGG enrichment**: 18 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 0.000585 | EPRS1, IARS1, LARS1, QARS1 |
| GO:MF aminoacyl-tRNA ligase activity | 0.00117 | EPRS1, IARS1, LARS1, QARS1, VARS1 |
| GO:BP tRNA aminoacylation for protein translation | 0.00117 | EPRS1, IARS1, LARS1, QARS1, VARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 0.00117 | EPRS1, IARS1, LARS1, QARS1, VARS1 |
| GO:BP amino acid activation | 0.00169 | EPRS1, IARS1, LARS1, QARS1, VARS1 |
| GO:BP tRNA aminoacylation | 0.00169 | EPRS1, IARS1, LARS1, QARS1, VARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 0.00169 | EPRS1, IARS1, LARS1, QARS1, VARS1 |
| GO:BP translation | 0.00723 | CYFIP1, DDX6, EIF4G1, EPRS1, IARS1, LARS1, QARS1, VARS1 |
| GO:BP protein biosynthetic process | 0.00723 | CYFIP1, DDX6, EIF4G1, EPRS1, IARS1, LARS1, QARS1, VARS1 |
| GO:MF catalytic activity, acting on RNA | 0.015 | DDX6, EPRS1, IARS1, LARS1, QARS1, SNRNP200, VARS1 |
| GO:MF aminoacyl-tRNA deacylase activity | 0.016 | IARS1, LARS1, VARS1 |
| GO:BP aminoacyl-tRNA metabolism involved in translational fidelity | 0.016 | IARS1, LARS1, VARS1 |
| GO:MF ATP binding | 0.0274 | ACLY, DDX6, DYNC1H1, EIF4G1, EPRS1, IARS1, LARS1, QARS1, SNRNP200, VARS1 |
| GO:MF adenyl ribonucleotide binding | 0.0287 | ACLY, DDX6, DYNC1H1, EIF4G1, EPRS1, IARS1, LARS1, QARS1, SNRNP200, VARS1 |
| GO:MF catalytic activity, acting on a tRNA | 0.0322 | EPRS1, IARS1, LARS1, QARS1, VARS1 |

### STRING and hu.MAP

STRING provides strong, coherent support for a core aminoacyl-tRNA synthetase subnetwork. EPRS1, IARS1, LARS1, QARS1 and VARS1 are mutually connected in the supplied high-confidence STRING network and jointly support cytosolic tRNA aminoacylation, aminoacyl-tRNA biosynthesis, the aminoacyl-tRNA synthetase multienzyme complex, and translation (STRING InterPro Aminoacyl-tRNA synthetase, class I, conserved site; within-query FDR = 3.36e-05) through (STRING RCTM Selenoamino acid metabolism; within-query FDR = 0.005). hu.MAP independently places EPRS1, IARS1, QARS1 and LARS1 in related multisynthetase complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), with additional synthetases and auxiliary proteins outside the module. This is evidence that the central cluster reflects a known biochemical assembly rather than coincidental co-abundance. Other established relationships include CYFIP1 with NCKAP1 in WAVE or actin-regulatory complexes (hu.MAP huMAP3_02474.1) through (hu.MAP huMAP3_13345.1) and the STRING relationship between DDX6 and EIF4G1. NUP160 and XPO1 are also connected in STRING, while DDX6, SNRNP200, XPO1 and NUP160 form a looser RNA-processing or transport-related neighborhood in the module graph. Several module edges lack corresponding STRING or hu.MAP support. Thus, the network combines a well-established synthetase core with peripheral links that may represent shared regulation, co-expression, indirect functional coupling, or context-specific organization rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 13 of 136 gene pairs: CYFIP1–NCKAP1 (0.999); DDX6–EIF4G1 (0.857); EPRS1–IARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–QARS1 (0.999); EPRS1–VARS1 (0.97); IARS1–LARS1 (0.999); IARS1–QARS1 (0.999); IARS1–VARS1 (0.9); LARS1–QARS1 (0.999); LARS1–VARS1 (0.968); NUP160–XPO1 (0.708); QARS1–VARS1 (0.91)
**STRING functional enrichment (supplementary, within-query FDR)**: InterPro Aminoacyl-tRNA synthetase, class I, conserved site (FDR = 3.36e-05, 5 genes); RCTM Cytosolic tRNA aminoacylation (FDR = 0.00017, 5 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 0.00028, 5 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 0.0003, 5 genes); Keyword Protein biosynthesis (FDR = 0.0003, 6 genes); InterPro Rossmann-like alpha/beta/alpha sandwich fold (FDR = 0.00039, 5 genes); Component aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.00055, 4 genes); COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.00081, 4 genes); Function aminoacyl-tRNA ligase activity (FDR = 0.001, 5 genes); RCTM Translation (FDR = 0.0024, 6 genes); Function Catalytic activity, acting on RNA (FDR = 0.0025, 7 genes); NetworkNeighborAL tRNA Aminoacylation, and glutamyl-tRNA(Gln) amidotransferase complex (FDR = 0.003, 5 genes); Process tRNA aminoacylation for protein translation (FDR = 0.0045, 5 genes); Pfam Anticodon-binding domain of tRNA ligase (FDR = 0.0045, 3 genes); RCTM Selenoamino acid metabolism (FDR = 0.005, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, IARS1, QARS1, LARS1; 4/14); huMAP3_13688.1 (EPRS1, IARS1, QARS1, LARS1; 4/14); huMAP3_02474.1 (CYFIP1, NCKAP1; 2/13); huMAP3_09598.1 (CYFIP1, NCKAP1; 2/23); huMAP3_13345.1 (CYFIP1, NCKAP1; 2/35)

### Novelty

The aminoacyl-tRNA synthetase core is not a new biological discovery: its biochemical function, STRING relationships, and multisynthetase-complex membership are already established by (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.000585) through (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 0.00169), (STRING InterPro Aminoacyl-tRNA synthetase, class I, conserved site; within-query FDR = 3.36e-05) through (STRING Function aminoacyl-tRNA ligase activity; within-query FDR = 0.001), and (hu.MAP huMAP3_02637.1) through (hu.MAP huMAP3_13688.1). The potentially novel observation is the conserved co-abundance of this core with translation-control, RNA-processing, transport, cytoskeletal, and metabolic genes across the cell line and kidney tissue pair. The fact sheet does not provide an external matched-tissue comparison, perturbation experiment, or literature search specifically testing this module, so the module-level novelty cannot be claimed as established. Lack of STRING or hu.MAP support for some peripheral relationships is evidence that those links are less well characterized, but it does not by itself establish novelty. The most defensible conclusion is that this is a biologically plausible conserved module containing a known core and a potentially informative, but unvalidated, peripheral organization.

**Hypothesis.** Hypothesis: in both cell line and kidney, cellular demand for accurate protein synthesis coordinates a cytosolic aminoacyl-tRNA synthetase hub with mRNA translation control, RNA processing and export, intracellular transport, and cytoskeletal organization. The synthetase core may provide the primary abundance signal, while DDX6 and EIF4G1 could couple charged-tRNA supply to selective translation and mRNA turnover; SNRNP200, NUP160 and XPO1 could connect RNA maturation or nuclear export to cytosolic translation; and DYNC1H1, CYFIP1, NCKAP1, COPB1 and related genes could reflect spatial transport or cytoskeletal support for these processes. This is a mechanistic model rather than a demonstrated interaction map. It should be tested by perturbing the synthetase core and measuring tRNA charging, translational output, mRNA stability, RNA export, and intracellular localization in kidney-relevant cells and the cell line.

### Important genes

#### IARS1

- **Related proteins** (co-abundance neighbors): LARS1 (0.89), EPRS1 (0.86), DYNC1H1 (0.86), ACLY (0.84), VARS1 (0.84), SNRNP200 (0.82), DDX6 (0.81); STRING partners: EPRS1 (0.999), LARS1 (0.999), QARS1 (0.999), VARS1 (0.9)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Isoleucine-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family and has been identified as a …
- **Diseases (Open Targets)**: growth retardation, intellectual developmental disorder, hypotonia, and hepatopathy (0.733); Abnormality of the skeletal system (0.332); microcephaly (0.289); Global developmental delay (0.289); Hallux valgus (0.184)
- **Europe PMC papers**: 184
- **Why important**: IARS1 is a topologically central member of the module and participates in nearly all of the primary aminoacylation, translation, and translational-fidelity terms (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.000585) through (GO:BP regulation of translational fidelity; q_global = 0.0339). It is an isoleucyl-tRNA synthetase, is part of the multisynthetase complex in hu.MAP (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), and has extensive STRING support with the other core synthetases. Its disease associations include developmental, skeletal, neurologic, and hypotonia-related phenotypes, while the literature record is substantial. Its kidney protein detection and broad tissue profile support a general cellular role rather than a secreted or blood-specific explanation.
- **Conclusion**: Established: IARS1 is a core aminoacylation and translational-fidelity component with strong network, annotation, complex, and disease evidence. Hypothesis: variation in IARS1 abundance could influence the functional capacity of the entire module by changing accurate isoleucine-tRNA charging.

#### EPRS1

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.87), IARS1 (0.86), NUP160 (0.85), LARS1 (0.85), VARS1 (0.83), QARS1 (0.81), DDX6 (0.80); STRING partners: IARS1 (0.999), LARS1 (0.999), QARS1 (0.999), VARS1 (0.97)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is among the most connected module genes and bridges the aminoacyl-tRNA synthetase core to DYNC1H1, NUP160, DDX6 and the other synthetases. It encodes a multifunctional glutamyl-prolyl-tRNA synthetase, appears in the multisynthetase complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), and is represented across the primary aminoacylation and translation terms (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.000585) through (GO:MF catalytic activity, acting on RNA; q_global = 0.015) and related terms. It has a substantial literature record and disease associations involving leukodystrophy and neurodevelopment. Its cytosolic location and kidney detection fit the inferred intracellular translation function.
- **Conclusion**: Established: EPRS1 is a central, multifunctional component of the known multisynthetase assembly and the conserved module. Hypothesis: EPRS1 may act as an abundance or organizational bridge between aminoacylation and the module’s RNA-transport or translation-regulatory periphery.

#### LARS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.89), EPRS1 (0.85), SNRNP200 (0.81), DYNC1H1 (0.80); STRING partners: EPRS1 (0.999), IARS1 (0.999), QARS1 (0.999), VARS1 (0.968)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: leucyl-tRNA synthetase 1. This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals w…
- **Diseases (Open Targets)**: infantile liver failure syndrome 1 (0.670); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.510); Global developmental delay (0.119); sensorineural hearing loss disorder (0.119); Generalized-onset seizure (0.118)
- **Europe PMC papers**: 267
- **Why important**: LARS1 has the broadest representation across the primary terms, including aminoacylation, translational fidelity, the multisynthetase complex, and glutaminyl-tRNA-related annotations (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.000585) through (GO:BP glutaminyl-tRNA aminoacylation; q_global = 0.0368). It is a central STRING-connected member of the synthetase core and is present in hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Its established leucine-tRNA charging function is especially relevant because leucine availability and signaling are linked to cellular translation control. LARS1 has documented associations with infantile liver failure and other inherited phenotypes, alongside a substantial literature record.
- **Conclusion**: Established: LARS1 is a core cytosolic synthetase with direct relevance to translation and translational fidelity. Hypothesis: its co-abundance may couple amino-acid sensing or availability to the broader translational state represented by this module, although that regulatory interpretation is not proven by the supplied data.

#### DDX6

- **Related proteins** (co-abundance neighbors): VPS45 (0.81), ACLY (0.81), IARS1 (0.81), EPRS1 (0.80), XPO1 (0.80); STRING partners: EIF4G1 (0.857)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytoplasmic bodies; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 6. This gene encodes a member of the DEAD box protein family. The protein is an RNA helicase found in P-bodies and stress granules, and functions in translation suppression and mRNA degradation. It is required for microRNA-induced gene silencing. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: intellectual developmental disorder with impaired language and dysmorphic facies (0.650); Intellectual disability (0.555); neurodegenerative disease (0.459); lung carcinoma (0.371); Global developmental delay (0.371)
- **Europe PMC papers**: 3002
- **Why important**: DDX6 occupies a high-connectivity bridging position between the synthetase-rich neighborhood and genes involved in mRNA regulation, including EIF4G1, VPS45, ACLY and XPO1. It is a DEAD-box RNA helicase associated with P-bodies and stress granules and is annotated for mRNA decapping, degradation, microRNA-mediated silencing, and negative regulation of translation. Its inclusion in the primary translation and RNA-catalytic terms (GO:BP translation; q_global = 0.00723) through (GO:MF catalytic activity, acting on RNA; q_global = 0.015) and (GO:MF ATP binding; q_global = 0.0274) through (GO:MF adenyl ribonucleotide binding; q_global = 0.0287), plus the STRING relationship with EIF4G1, gives the module a plausible post-transcriptional regulatory dimension. DDX6 also has extensive literature and neurodevelopmental disease associations.
- **Conclusion**: Established: DDX6 is an RNA-turnover and translation-regulatory factor connected to the module’s protein-biosynthesis core. Hypothesis: DDX6 may tune which transcripts use the aminoacylation capacity represented by the module, particularly during stress or altered translational demand.

#### DYNC1H1

- **Related proteins** (co-abundance neighbors): EPRS1 (0.87), IARS1 (0.86), VARS1 (0.84), NCKAP1 (0.81), LARS1 (0.80), COPB1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 1 heavy chain 1. Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polyp…
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy without contractures (0.816); intellectual disability, autosomal dominant 13 (0.815); Charcot-Marie-Tooth disease axonal type 2O (0.799); autosomal dominant non-syndromic intellectual disability (0.634); hereditary disease (0.545)
- **Europe PMC papers**: 1731
- **Why important**: DYNC1H1 is a highly connected peripheral hub linking several synthetases to NCKAP1 and COPB1. It encodes cytoplasmic dynein heavy chain, a motor involved in retrograde transport, organelle movement, protein sorting, spindle dynamics, and microtubule organization. Its ATP-binding representation in (GO:MF ATP binding; q_global = 0.0274) and (GO:MF adenyl ribonucleotide binding; q_global = 0.0287), brain tissue enhancement, retinal-ganglion-cell enhancement, kidney detection, and strong disease literature make it an important bridge between the biochemical translation core and cell architecture. Its disease associations include spinal muscular atrophy, Charcot-Marie-Tooth disease, and intellectual disability.
- **Conclusion**: Established: DYNC1H1 contributes a transport and cytoskeletal dimension to an otherwise translation-centered module and is medically well characterized. Hypothesis: dynein-dependent positioning of RNA, organelles, or translation machinery may help explain the conserved co-abundance link between the synthetase core and the module periphery.

## Module 2

**Tissue pair**: cell line and kidney  
**Genes (9)**: ACOT9, ATP2A2, GALNT7, HK1, NUP93, PHIP, PRKDC, YARS2, UGGT1

### Function

No GO or KEGG term passed global correction, and STRING supplied no functional enrichment, so the module does not support a statistically established pathway assignment. Its strongest interpretable signal is a heterogeneous cellular-maintenance axis centered on PRKDC: DNA double-strand-break repair and genome maintenance, nuclear transport through NUP93, glucose handling through HK1, endoplasmic-reticulum glycoprotein quality control through UGGT1, calcium homeostasis through ATP2A2, mitochondrial translation through YARS2, lipid metabolism through ACOT9, and protein O-linked glycosylation through GALNT7. Because these functions are diverse and the co-abundance graph is sparse, this is better regarded as a coordinated cellular state or shared cellular context than as a demonstrated single biochemical pathway.

**Cell composition.** The module is not dominated by secreted proteins: only one member is annotated in the secretome, and all members were detected in kidney tissue. Most genes have low tissue specificity, while several show cell-type enhancement in erythrocyte progenitors, neutrophils, cardiomyocytes, or other specialized cell types. However, all genes have low immune-cell specificity and no blood-cell enrichment was reported. The pattern therefore does not establish a blood-contamination explanation, although shared cell composition or broadly expressed cellular machinery could contribute to the cell-line and kidney overlap. ATP2A2 has tissue enrichment in muscle-related tissues and GALNT7 has tissue enhancement in stomach, but these isolated signals do not define the module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module pairs, and STRING provided no enrichment. Thus, the observed co-abundance relationships are not corroborated by the supplied STRING interaction network. hu.MAP provides limited but repeated complex-level support: PRKDC and NUP93 co-occur in C1, C2, and C3, while PRKDC and ATP2A2 co-occur in C4. These are partial memberships within larger complexes rather than evidence that all module genes form one complex. The repeated PRKDC–NUP93 pairing is the clearest known structural context, whereas the remaining edges lack supplied database support.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07789.1 (PRKDC, NUP93; 2/7); huMAP3_05673.1 (PRKDC, NUP93; 2/11); huMAP3_09042.1 (PRKDC, NUP93; 2/26); huMAP3_09592.1 (ATP2A2, PRKDC; 2/95)

### Novelty

This module may represent a new co-abundance observation, but it cannot be called a newly discovered molecular complex or pathway. The lack of STRING interactions and the partial hu.MAP matches make the overall combination unusual in the supplied resources, yet database absence alone does not prove novelty. Its novelty is therefore best stated as a potentially novel cross-context expression relationship linking a PRKDC-centered subnetwork with metabolic, trafficking, quality-control, calcium, and glycosylation genes; independent replication and perturbation would be required to establish that interpretation.

**Hypothesis.** Hypothesis: a shared cellular-stress or biosynthetic state coordinates genome surveillance through PRKDC with nuclear transport through NUP93, energy supply through HK1, endoplasmic-reticulum quality control through UGGT1, calcium handling through ATP2A2, mitochondrial protein synthesis through YARS2, lipid handling through ACOT9, and glycoprotein processing through GALNT7. PRKDC may act as the principal network bridge in the co-abundance pattern, but the current evidence does not demonstrate direct regulation or physical binding among these proteins.

### Important genes

#### PRKDC

- **Related proteins** (co-abundance neighbors): PHIP (0.85), HK1 (0.83), ATP2A2 (0.81), UGGT1 (0.81), YARS2 (0.80), GALNT7 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_07789.1, huMAP3_05673.1, huMAP3_09042.1, huMAP3_09592.1
- **Function (MyGene.info)**: protein kinase, DNA-activated, catalytic subunit. This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to DNA-PKcs deficiency (0.752); neurodegenerative disease (0.548); severe combined immunodeficiency (0.470); combined immunodeficiency (0.464); ovarian neoplasm (0.210)
- **Europe PMC papers**: 12461
- **Why important**: PRKDC is the network hub with the greatest weighted connectivity in the module and connects to most of the other members. It encodes the catalytic subunit of DNA-dependent protein kinase, with established roles in DNA double-strand-break repair, recombination, telomere maintenance, and innate immune response. It is present in three hu.MAP pairings with NUP93 and one with ATP2A2, has a strong disease connection to DNA-PKcs deficiency and combined immunodeficiency, and has extensive literature coverage.
- **Conclusion**: Established evidence supports PRKDC as the best network anchor and a genome-maintenance gene. It is plausible that its abundance tracks a broader cellular state, but the module does not establish that PRKDC regulates the other members or that they participate in DNA repair.

#### NUP93

- **Related proteins** (co-abundance neighbors): HK1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_07789.1, huMAP3_05673.1, huMAP3_09042.1
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 is one of the two genes repeatedly represented with PRKDC in hu.MAP complexes and is a core nucleoporin involved in nuclear pore assembly, nucleocytoplasmic transport, nuclear import, and messenger RNA export. It is connected to HK1 in the module and is associated with nephrotic syndrome and familial steroid-resistant nephrotic syndrome, making it particularly relevant to the kidney context.
- **Conclusion**: Established evidence supports NUP93 as a nuclear-transport and kidney-relevant component that strengthens the PRKDC-centered interpretation. Its co-abundance with PRKDC may reflect coordinated nuclear maintenance, but a direct functional interaction is not demonstrated here.

#### HK1

- **Related proteins** (co-abundance neighbors): PRKDC (0.83), NUP93 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hexokinase 1. Hexokinases phosphorylate glucose to produce glucose-6-phosphate, the first step in most glucose metabolism pathways. This gene encodes a ubiquitous form of hexokinase which localizes to the outer membrane of mitochondria. Mutations in this gene have been associated with hemolytic anemia due to hexokinase deficiency. Alternative splicing of this gene results in several transcript variants which en…
- **Diseases (Open Targets)**: neurodevelopmental disorder with visual defects and brain anomalies (0.757); non-spherocytic hemolytic anemia due to hexokinase deficiency (0.751); Charcot-Marie-Tooth disease type 4G (0.711); retinitis pigmentosa 79 (0.596); retinitis pigmentosa (0.496)
- **Europe PMC papers**: 51843
- **Why important**: HK1 is a ubiquitous mitochondrial-associated hexokinase and a key entry point into glucose metabolism. It links PRKDC and NUP93 in the module, is detected in kidney, and has extensive literature coverage. Its disease associations include hexokinase-deficiency hemolytic anemia and neurological or retinal disorders, which also makes cell-state and lineage composition relevant considerations.
- **Conclusion**: Established evidence supports HK1 as a metabolic component whose abundance could report energy demand or cellular composition. The module does not show that HK1 supplies energy specifically for DNA repair or nuclear transport.

#### UGGT1

- **Related proteins** (co-abundance neighbors): PRKDC (0.81), ACOT9 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UDP-glucose glycoprotein glucosyltransferase 1. UDP-glucose:glycoprotein glucosyltransferase (UGT) is a soluble protein of the endoplasmic reticulum (ER) that selectively reglucosylates unfolded glycoproteins, thus providing quality control for protein transport out of the ER.[supplied by OMIM, Oct 2009].
- **Diseases (Open Targets)**: congenital disorder of glycosylation (0.416); hypercholesterolemia, familial, 1 (0.333); connective tissue disorder (0.234); ovarian dysfunction (0.216); chronic laryngitis (0.147)
- **Europe PMC papers**: 507
- **Why important**: UGGT1 connects directly to the PRKDC hub and to ACOT9 and performs endoplasmic-reticulum glycoprotein quality control by reglucosylating incompletely folded glycoproteins. It is associated with protein folding, glycoprotein biosynthesis, and ER mannose trimming, and its disease evidence includes congenital disorder of glycosylation. Its cell-type annotation includes erythrocyte progenitors.
- **Conclusion**: Established evidence supports UGGT1 as a protein-quality-control component and gives the module an ER homeostasis dimension. A coordinated ER-stress mechanism is a reasonable possibility, but no enrichment or physical interaction evidence establishes it.

#### ATP2A2

- **Related proteins** (co-abundance neighbors): PRKDC (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darie…
- **Diseases (Open Targets)**: Darier disease (0.823); acrokeratosis verruciformis (0.663); neurodegenerative disease (0.507); hereditary disease (0.416); schizophrenia (0.406)
- **Europe PMC papers**: 9327
- **Why important**: ATP2A2 is connected to the PRKDC hub and is the module member with tissue enrichment in heart muscle, skeletal muscle, and tongue. It encodes a SERCA calcium pump involved in intracellular calcium homeostasis and contraction-relaxation physiology, is represented with PRKDC in hu.MAP, and is strongly associated with Darier disease.
- **Conclusion**: Established evidence supports ATP2A2 as a calcium-homeostasis and tissue-state marker. Its inclusion could reflect cellular calcium handling or sample composition, but the current data do not show that it mechanistically couples calcium transport to PRKDC.

#### YARS2

- **Related proteins** (co-abundance neighbors): PRKDC (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tyrosyl-tRNA synthetase 2. This gene encodes a mitochondrial protein that catalyzes the attachment of tyrosine to tRNA(Tyr). Mutations in this gene are associated with myopathy with lactic acidosis and sideroblastic anemia type 2 (MLASA2). [provided by RefSeq, Jan 2011].
- **Diseases (Open Targets)**: myopathy, lactic acidosis, and sideroblastic anemia (0.794); mitochondrial disease (0.509); neurodegenerative disease (0.478); hereditary disease (0.452); pericarditis (0.214)
- **Europe PMC papers**: 430
- **Why important**: YARS2 connects to PRKDC and encodes the mitochondrial tyrosyl-tRNA synthetase required for mitochondrial translation. It is detected in kidney, shows cell-type enhancement in cardiomyocytes and epicardial cells, and is associated with myopathy, lactic acidosis, and sideroblastic anemia as well as mitochondrial disease.
- **Conclusion**: Established evidence supports YARS2 as a mitochondrial protein-synthesis component that may reflect organelle demand or cellular energetic state. Its proposed participation in the module-wide mechanism remains hypothetical because it has no supplied STRING or hu.MAP support.

## Module 3

**Tissue pair**: cell line and kidney  
**Genes (18)**: AQR, BOP1, CHD1, CNOT1, DHX36, DHX9, HEATR1, MYBBP1A, MTA2, NOP56, URB1, POLR1A, POLR2A, PDCD11, THOC2, WDR18, WDR36, WDR3

### Function

This is a nuclear and nucleolar RNA-production module centered on ribosome biogenesis and RNA processing. The strongest primary evidence is the broad and highly coherent enrichment for RNA biosynthetic processes, RNA metabolism, ribonucleoprotein-complex biogenesis, ribosome biogenesis, rRNA processing, preribosome, small-subunit processome, nucleolus, RNA binding, and nuclear compartments (19 globally significant GO/KEGG terms, q_global 7.14e-06–0.00419; see the table), (7 globally significant GO/KEGG terms, q_global 0.011–0.048; see the table). The module also includes transcriptional, mRNA-processing, RNA-export, helicase, chromatin, and mRNA-decay components, indicating coupling between production of RNA, its maturation, and nuclear handling. The STRING results independently support this interpretation through rRNA processing, preribosome, ribosome biogenesis, RNA metabolism, nucleic-acid binding, and nuclear-lumen annotations (15 supplementary STRING terms; within-query FDR 1.29e-06–2.93e-05), although these are supplementary evidence rather than globally corrected GO/KEGG evidence.

**Cell composition.** The module is not composed of plasma or secreted proteins: HPA reports no secreted genes. It is also not blood-cell enriched; the genes have low immune-cell specificity or are not detected in immune cells, and no blood-cell enrichment is reported. Most genes have low tissue specificity, consistent with broadly deployed nuclear housekeeping machinery rather than a specialized kidney secretory program. The kidney protein data are compatible with this interpretation because most genes are detected in kidney, while the reported tissue- and cell-type-enhanced signals are scattered across skeletal muscle, lymphoid tissue, germ-cell populations, esophageal cells, oocytes, pancreatic acinar cells, epithelial cells, and other cell types. The shared cell-line–kidney module therefore most plausibly reflects conserved intracellular RNA and ribosome biology, not plasma contamination or a common blood-cell contribution.

**GO/KEGG enrichment**: 28 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA biosynthetic process | 7.14e-06 | AQR, BOP1, CNOT1, DHX36, DHX9, HEATR1, MTA2, MYBBP1A, NOP56, PDCD11, POLR1A, POLR2A, THOC2, URB1, WDR18, WDR3, WDR36 |
| GO:BP nucleic acid biosynthetic process | 1.2e-05 | AQR, BOP1, CNOT1, DHX36, DHX9, HEATR1, MTA2, MYBBP1A, NOP56, PDCD11, POLR1A, POLR2A, THOC2, URB1, WDR18, WDR3, WDR36 |
| GO:BP RNA metabolic process | 2.73e-05 | AQR, BOP1, CNOT1, DHX36, DHX9, HEATR1, MTA2, MYBBP1A, NOP56, PDCD11, POLR1A, POLR2A, THOC2, URB1, WDR18, WDR3, WDR36 |
| GO:BP ribonucleoprotein complex biogenesis | 2.82e-05 | BOP1, DHX9, HEATR1, MYBBP1A, NOP56, PDCD11, URB1, WDR18, WDR3, WDR36 |
| GO:BP ribosome biogenesis | 3.64e-05 | BOP1, HEATR1, MYBBP1A, NOP56, PDCD11, URB1, WDR18, WDR3, WDR36 |
| GO:BP rRNA processing | 6.52e-05 | BOP1, HEATR1, NOP56, PDCD11, URB1, WDR18, WDR3, WDR36 |
| GO:BP nucleobase-containing compound biosynthetic process | 7.75e-05 | AQR, BOP1, CNOT1, DHX36, DHX9, HEATR1, MTA2, MYBBP1A, NOP56, PDCD11, POLR1A, POLR2A, THOC2, URB1, WDR18, WDR3, WDR36 |
| GO:BP RNA processing | 0.000124 | AQR, BOP1, DHX36, DHX9, HEATR1, NOP56, PDCD11, THOC2, URB1, WDR18, WDR3, WDR36 |
| GO:BP rRNA metabolic process | 0.000164 | BOP1, HEATR1, NOP56, PDCD11, URB1, WDR18, WDR3, WDR36 |
| GO:BP nucleic acid metabolic process | 0.000179 | AQR, BOP1, CNOT1, DHX36, DHX9, HEATR1, MTA2, MYBBP1A, NOP56, PDCD11, POLR1A, POLR2A, THOC2, URB1, WDR18, WDR3, WDR36 |
| GO:MF nucleic acid binding | 0.000185 | AQR, BOP1, CHD1, CNOT1, DHX36, DHX9, HEATR1, MTA2, MYBBP1A, NOP56, PDCD11, POLR1A, POLR2A, THOC2, URB1, WDR3 |
| GO:CC preribosome | 0.000234 | BOP1, HEATR1, NOP56, PDCD11, WDR3, WDR36 |
| GO:CC small-subunit processome | 0.000668 | HEATR1, NOP56, PDCD11, WDR3, WDR36 |
| GO:CC nuclear protein-containing complex | 0.000727 | AQR, BOP1, HEATR1, MTA2, MYBBP1A, NOP56, PDCD11, POLR1A, THOC2, WDR18, WDR3, WDR36 |
| GO:CC nucleolus | 0.000748 | BOP1, DHX9, HEATR1, MYBBP1A, NOP56, PDCD11, POLR1A, URB1, WDR18, WDR3, WDR36 |

### STRING and hu.MAP

STRING shows a dense, biologically coherent set of known or strongly supported relationships among the nucleolar genes, especially BOP1, HEATR1, NOP56, PDCD11, WDR3, WDR36, WDR18, MYBBP1A, POLR1A, and URB1. These relationships closely match the ribosome-biogenesis and rRNA-processing interpretation and indicate that much of the module recapitulates an established nucleolar interaction neighborhood. DHX9–DHX36 and DHX9–POLR2A provide additional links to RNA helicase and transcriptional functions. hu.MAP identifies POLR1A and POLR2A together in several RNA-polymerase-related complexes (hu.MAP huMAP3_08487.1) (hu.MAP huMAP3_06426.1) (hu.MAP huMAP3_14318.1) (hu.MAP huMAP3_11092.1), but only these two module members are represented in those complexes. The lack of hu.MAP assignments for many other genes does not contradict their function; it indicates that the module is broader than the specific complexes represented in hu.MAP and may capture shared abundance or pathway-level coordination rather than one purified physical complex.

**STRING interactions (score >= 0.7)**: 40 of 153 gene pairs: BOP1–HEATR1 (0.971); BOP1–MYBBP1A (0.915); BOP1–NOP56 (0.974); BOP1–PDCD11 (0.97); BOP1–POLR1A (0.933); BOP1–URB1 (0.721); BOP1–WDR18 (0.967); BOP1–WDR3 (0.973); BOP1–WDR36 (0.951); DHX36–DHX9 (0.815); DHX9–POLR2A (0.781); HEATR1–MYBBP1A (0.973); HEATR1–NOP56 (0.999); HEATR1–PDCD11 (0.999); HEATR1–POLR1A (0.938); HEATR1–URB1 (0.914); HEATR1–WDR18 (0.867); HEATR1–WDR3 (0.999); HEATR1–WDR36 (0.999); MYBBP1A–NOP56 (0.737); MYBBP1A–PDCD11 (0.949); MYBBP1A–POLR1A (0.964); MYBBP1A–WDR3 (0.878); MYBBP1A–WDR36 (0.861); NOP56–PDCD11 (0.997); NOP56–POLR1A (0.918); NOP56–WDR3 (0.999); NOP56–WDR36 (0.999); PDCD11–POLR1A (0.985); PDCD11–URB1 (0.973); PDCD11–WDR18 (0.812); PDCD11–WDR3 (0.997); PDCD11–WDR36 (0.998); POLR1A–URB1 (0.906); POLR1A–WDR3 (0.948); POLR1A–WDR36 (0.926); URB1–WDR36 (0.878); WDR18–WDR3 (0.801); WDR18–WDR36 (0.866); WDR3–WDR36 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL rRNA processing, and RNA helicase activity (FDR = 1.29e-06, 9 genes); RCTM Metabolism of RNA (FDR = 2.22e-06, 12 genes); Process RNA metabolic process (FDR = 2.59e-06, 15 genes); Function Nucleic acid binding (FDR = 2.66e-06, 17 genes); COMPARTMENTS Nuclear lumen (FDR = 2.83e-06, 15 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 4.21e-06, 8 genes); Process Nucleic acid metabolic process (FDR = 4.3e-06, 16 genes); Keyword Nucleus (FDR = 4.9e-06, 18 genes); Process Ribonucleoprotein complex biogenesis (FDR = 6.3e-06, 10 genes); Process Ribosome biogenesis (FDR = 6.3e-06, 9 genes); Process rRNA processing (FDR = 1.54e-05, 8 genes); RCTM Major pathway of rRNA processing in the nucleolus and cytosol (FDR = 1.71e-05, 7 genes); COMPARTMENTS Nucleolus (FDR = 2.93e-05, 10 genes); COMPARTMENTS Preribosome (FDR = 2.93e-05, 6 genes); COMPARTMENTS 90S preribosome (FDR = 2.93e-05, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08487.1 (POLR1A, POLR2A; 2/37); huMAP3_06426.1 (POLR1A, POLR2A; 2/38); huMAP3_14318.1 (POLR1A, POLR2A; 2/58); huMAP3_11092.1 (POLR1A, POLR2A; 2/65)

### Novelty

The biological function is not a new discovery: ribosome biogenesis, rRNA processing, nucleolar localization, and RNA metabolism are well established for many of these genes, and the STRING relationships reinforce that prior knowledge. The potentially novel aspect is the recurrence of this coordinated abundance pattern across cell line and kidney, particularly the way canonical nucleolar machinery is coupled to RNA polymerase, helicase, mRNA-export, chromatin, and mRNA-decay genes. However, the fact sheet does not establish that this cross-tissue co-abundance module is absent from prior co-abundance studies, nor does absence from hu.MAP or incomplete STRING coverage prove novelty. The defensible conclusion is that this is a biologically credible conserved module with possible dataset-specific organizational novelty, not a demonstrably new molecular complex or newly discovered pathway.

**Hypothesis.** Hypothesis: conserved cellular demand for RNA production coordinates a nucleolar ribosome-biogenesis core with broader nuclear RNA-handling machinery. In this model, POLR1A-driven precursor-rRNA transcription feeds a nucleolar processing and assembly system involving HEATR1, NOP56, PDCD11, WDR3, WDR36, WDR18, BOP1, and URB1, while POLR2A, AQR, THOC2, DHX9, DHX36, CNOT1, MTA2, and CHD1 connect this core to messenger-RNA transcription, processing, export, decay, helicase activity, and chromatin regulation. The shared abundance pattern may therefore report a common cellular state of high or coordinated RNA-production capacity rather than a single stable complex. This hypothesis should be tested with perturbation, nucleolar localization, and RNA-processing assays rather than inferred from co-abundance alone.

### Important genes

#### WDR3

- **Related proteins** (co-abundance neighbors): NOP56 (0.90), PDCD11 (0.86), POLR2A (0.85), URB1 (0.84), BOP1 (0.83), CNOT1 (0.83), CHD1 (0.83), DHX36 (0.82), POLR1A (0.81); STRING partners: BOP1 (0.973), HEATR1 (0.999), MYBBP1A (0.878), NOP56 (0.999), PDCD11 (0.997), POLR1A (0.948), WDR18 (0.801), WDR36 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 3. This gene encodes a nuclear protein containing 10 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, which usually include a trp-asp at the C-terminal end. Proteins belonging to the WD repeat family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. [provid…
- **Diseases (Open Targets)**: presbycusis (0.335); respiratory tract infectious disorder (0.184); neurodegenerative disease (0.143); preeclampsia (0.120); alcohol drinking (0.098)
- **Europe PMC papers**: 280
- **Why important**: WDR3 is the strongest network hub in the module and connects the principal nucleolar cluster, including NOP56, PDCD11, HEATR1, POLR2A, URB1, BOP1, CNOT1, CHD1, and DHX36. It is annotated for maturation of small-subunit rRNA and small-subunit biogenesis, occupies the nucleoli, and participates in every major primary enrichment theme listed for the module. Its many strong STRING relationships make it an important structural and functional anchor. Its disease-linked literature is more limited than that of the major polymerase and chromatin genes, which makes its central position especially informative for module interpretation.
- **Conclusion**: Established evidence supports WDR3 as a central nucleolar ribosome-biogenesis component and a key connector in this module. It is a plausible organizing hub, but the co-abundance data alone do not prove that WDR3 physically scaffolds all of the module relationships.

#### PDCD11

- **Related proteins** (co-abundance neighbors): WDR3 (0.86), HEATR1 (0.85), MYBBP1A (0.84), POLR2A (0.83), THOC2 (0.83), NOP56 (0.81); STRING partners: BOP1 (0.97), HEATR1 (0.999), MYBBP1A (0.949), NOP56 (0.997), POLR1A (0.985), URB1 (0.973), WDR18 (0.812), WDR3 (0.997), WDR36 (0.998)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 11. PDCD11 is a NF-kappa-B (NFKB1; 164011)-binding protein that colocalizes with U3 RNA (MIM 180710) in the nucleolus and is required for rRNA maturation and generation of 18S rRNA (Sweet et al., 2003 [PubMed 14624448]; Sweet et al., 2008 [PubMed 17654514]).[supplied by OMIM, Oct 2008].
- **Diseases (Open Targets)**: Back pain (0.277); insomnia (0.216); systemic lupus erythematosus (0.170); neoplasm (0.095); colorectal carcinoma (0.093)
- **Europe PMC papers**: 334
- **Why important**: PDCD11 has a highly connected position linking WDR3, HEATR1, MYBBP1A, POLR2A, THOC2, and NOP56, and it has strong STRING support with the principal ribosome-biogenesis genes. The supplied annotation directly links PDCD11 to U3 RNA, rRNA maturation, and generation of eighteen-S rRNA, while HPA places it at the nucleolar rim and detects it in kidney. It has a substantial literature and disease-association record, including systemic lupus erythematosus and neoplastic associations in the supplied evidence.
- **Conclusion**: Established evidence identifies PDCD11 as a functionally relevant rRNA-processing factor that connects nucleolar maturation with broader nuclear RNA machinery. Its position makes it a strong candidate for mediating coordination within the module, although a direct causal role in the cross-tissue abundance pattern remains a hypothesis.

#### HEATR1

- **Related proteins** (co-abundance neighbors): URB1 (0.87), PDCD11 (0.85), CHD1 (0.84), WDR36 (0.80); STRING partners: BOP1 (0.971), MYBBP1A (0.973), NOP56 (0.999), PDCD11 (0.999), POLR1A (0.938), URB1 (0.914), WDR18 (0.867), WDR3 (0.999), WDR36 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HEAT repeat containing 1. Enables RNA binding activity. Involved in positive regulation of rRNA processing and positive regulation of transcription by RNA polymerase I. Located in fibrillar center and mitochondrion. Implicated in pancreatic ductal carcinoma. Biomarker of glioblastoma. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.475); Alzheimer disease (0.463); Parkinson disease (0.462); lysosomal storage disease (0.462); musculoskeletal system disorder (0.168)
- **Europe PMC papers**: 342
- **Why important**: HEATR1 is embedded in the core nucleolar interaction neighborhood and links URB1, PDCD11, CHD1, and WDR36 in the co-abundance graph while showing very strong STRING relationships with BOP1, NOP56, WDR3, and WDR36. Its annotations directly support rRNA processing, small-subunit biogenesis, and positive regulation of RNA polymerase I transcription. HPA places it in the nucleolar fibrillar center and reports kidney detection. It also has disease and cancer-related associations, including pancreatic ductal carcinoma and glioblastoma biomarker evidence.
- **Conclusion**: Established evidence supports HEATR1 as a nucleolar ribosome-biogenesis and RNA-polymerase-I-associated factor. Its network and annotation profile make it a strong bridge between rRNA maturation and transcription, but the module does not establish whether it is a limiting regulator in either cell line or kidney.

#### NOP56

- **Related proteins** (co-abundance neighbors): WDR3 (0.90), PDCD11 (0.81), MYBBP1A (0.81); STRING partners: BOP1 (0.974), HEATR1 (0.999), MYBBP1A (0.737), PDCD11 (0.997), POLR1A (0.918), WDR3 (0.999), WDR36 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP56 ribonucleoprotein. Nop56p is a yeast nucleolar protein that is part of a complex with the nucleolar proteins Nop58p and fibrillarin. Nop56p is required for assembly of the 60S ribosomal subunit and is involved in pre-rRNA processing. The protein encoded by this gene is similar in sequence to Nop56p and is also found in the nucleolus. Expansion of a GGCCTG repeat from 3-8 copies to 1500-2500 copies in an intron of th…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 36 (0.586); neurodegenerative disease (0.495); ovarian neoplasm (0.272); hereditary disease (0.193); cerebellar ataxia (0.121)
- **Europe PMC papers**: 1517
- **Why important**: NOP56 is a canonical nucleolar ribonucleoprotein component with annotations for rRNA processing, rRNA modification, small-subunit biogenesis, and assembly of the large ribosomal subunit. It is closely connected in STRING to BOP1, HEATR1, PDCD11, WDR3, POLR1A, and WDR36, and it is located in the nucleolar fibrillar center with kidney detection. NOP56 has extensive literature and a particularly important disease association with spinocerebellar ataxia type thirty-six.
- **Conclusion**: Established evidence strongly supports NOP56 as a core rRNA-processing and ribonucleoprotein factor, making it one of the most interpretable members of the module. Its disease association demonstrates that disruption of this conserved machinery can have tissue-specific consequences, but it does not show that the present module is disease-associated.

#### POLR1A

- **Related proteins** (co-abundance neighbors): MTA2 (0.83), POLR2A (0.83), WDR3 (0.81); STRING partners: BOP1 (0.933), HEATR1 (0.938), MYBBP1A (0.964), NOP56 (0.918), PDCD11 (0.985), URB1 (0.906), WDR3 (0.948), WDR36 (0.926)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoli fibrillar center; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_08487.1, huMAP3_06426.1, huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase I subunit A. The protein encoded by this gene is the largest subunit of the RNA polymerase I complex. The encoded protein represents the catalytic subunit of the complex, which transcribes DNA into ribosomal RNA precursors. Defects in this gene are a cause of the Cincinnati type of acrofacial dysostosis. [provided by RefSeq, May 2016].
- **Diseases (Open Targets)**: choanal atresia-hearing loss-cardiac defects-craniofacial dysmorphism syndrome (0.780); acrofacial dysostosis Cincinnati type (0.723); leukodystrophy, hypomyelinating, 27 (0.459); acrofacial dysostosis (0.372); microtia (0.370)
- **Europe PMC papers**: 555
- **Why important**: POLR1A is the catalytic subunit of RNA polymerase I and provides the transcriptional entry point for precursor rRNA production. It connects to WDR3, POLR2A, and MTA2 in the co-abundance graph and has strong STRING relationships with the nucleolar ribosome-biogenesis cluster. It is represented with POLR2A in several hu.MAP polymerase-related complexes (hu.MAP huMAP3_08487.1) (hu.MAP huMAP3_06426.1) (hu.MAP huMAP3_14318.1) (hu.MAP huMAP3_11092.1), is localized to the nucleolar fibrillar center, and has established associations with craniofacial and leukodystrophy-related disorders. Its literature base is substantial.
- **Conclusion**: Established evidence supports POLR1A as the principal rRNA-transcription component of the module and as a mechanistic link between transcription and downstream nucleolar processing. Its co-abundance with processing factors is consistent with coordinated pathway activity, but does not prove direct physical binding to every processing factor.

#### POLR2A

- **Related proteins** (co-abundance neighbors): CHD1 (0.86), WDR3 (0.85), URB1 (0.83), PDCD11 (0.83), POLR1A (0.83); STRING partners: DHX9 (0.781)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08487.1, huMAP3_06426.1, huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase II subunit A. This gene encodes the largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene contains a carboxy terminal domain composed of heptapeptide repeats that are essential for polymerase activity. These repeats contain serine and threonine residues that are phosphorylated in actively transcribing RNA polymerase. In addition, …
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and variable intellectual and behavioral abnormalities (0.738); HIV infectious disease (0.600); hereditary disease (0.479); syndromic intellectual disability (0.462); Orthomyxoviridae infectious disease (0.374)
- **Europe PMC papers**: 4546
- **Why important**: POLR2A is the largest subunit of RNA polymerase II and connects the nucleolar-associated network to messenger-RNA transcription. It is linked in the module graph to CHD1, WDR3, URB1, PDCD11, and POLR1A, appears in the shared hu.MAP polymerase complexes (hu.MAP huMAP3_08487.1) (hu.MAP huMAP3_06426.1) (hu.MAP huMAP3_14318.1) (hu.MAP huMAP3_11092.1), and contributes to the primary RNA-biosynthetic, nucleic-acid-binding, nuclear, and transcription-related terms. HPA reports enhancement in lymphoid tissue and several kidney-relevant epithelial cell types. It has the largest literature volume among the selected genes and broad disease relevance, including neurodevelopmental disorders.
- **Conclusion**: Established evidence supports POLR2A as the module's connection to RNA polymerase II transcription and general nuclear gene expression. Its presence suggests coordinated RNA production beyond ribosome biogenesis, but whether this reflects a regulatory interaction with the nucleolar core or simply shared cellular demand is unresolved.

## Module 4

**Tissue pair**: cell line and kidney  
**Genes (13)**: DDX21, GTPBP4, INTS8, KRR1, NAA15, NOL6, NUP188, RSL1D1, RRP12, SUPT16H, CCT3, UTP15, UTP4

### Function

The module is best interpreted as a nucleolar ribosome-biogenesis and RNA-processing module, with particular emphasis on maturation of the small ribosomal subunit. The primary evidence is the coordinated enrichment for RNA binding (GO:MF RNA binding; q_global = 0.00161), rRNA processing (GO:BP rRNA processing; q_global = 0.00179), rRNA metabolic process (GO:BP rRNA metabolic process; q_global = 0.00358), the small-subunit processome (GO:CC small-subunit processome; q_global = 0.00512), ribosome biogenesis (GO:BP ribosome biogenesis; q_global = 0.00783), the nucleolus (GO:CC nucleolus; q_global = 0.0169), small-subunit biogenesis (GO:BP ribosomal small subunit biogenesis; q_global = 0.0171), and the eukaryotic ribosome-biogenesis pathway (KEGG Ribosome biogenesis in eukaryotes - Homo sapiens (human); q_global = 0.0171). Preribosome and ribonucleoprotein-complex biogenesis evidence further supports this interpretation (GO:CC preribosome; q_global = 0.0234) (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0329). The broad RNA-binding signal (GO:MF RNA binding; q_global = 0.00161) (GO:MF nucleic acid binding; q_global = 0.0253) is consistent with a nucleolar RNA-processing machinery rather than with a secreted or membrane-associated function. The module also contains genes with related nuclear functions, including chromatin transcription, RNA polymerase II-associated processing, nucleocytoplasmic transport, and protein maturation, which may represent functional interfaces or secondary co-abundance effects rather than the central module function.

**Cell composition.** This is not a plasma-protein or secreted-protein module: HPA reports no secreted genes. Most genes have low tissue specificity and low immune-cell specificity, arguing against a module dominated by blood contamination or a particular blood-cell population. HPA does show selected cell-type or tissue enhancement, including bone marrow, skeletal muscle, neutrophils, erythrocyte progenitors, germ-cell populations, retinal horizontal cells, epicardial cells, oocytes, and proximal tubule cells. These isolated enrichments are heterogeneous and do not establish a common contaminating cell type. The overall composition is therefore more compatible with a broadly expressed housekeeping-like nucleolar program, with possible modulation by cellular proliferation, differentiation, or tissue composition. Protein detection in kidney for most genes is consistent with the module being relevant to kidney samples, although detection does not by itself establish a kidney-specific function.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF RNA binding | 0.00161 | CCT3, DDX21, GTPBP4, KRR1, NAA15, NOL6, RRP12, RSL1D1, SUPT16H, UTP15, UTP4 |
| GO:BP rRNA processing | 0.00179 | DDX21, GTPBP4, KRR1, NOL6, UTP15, UTP4 |
| GO:BP rRNA metabolic process | 0.00358 | DDX21, GTPBP4, KRR1, NOL6, UTP15, UTP4 |
| GO:CC small-subunit processome | 0.00512 | KRR1, NOL6, UTP15, UTP4 |
| GO:BP ribosome biogenesis | 0.00783 | DDX21, GTPBP4, KRR1, NOL6, UTP15, UTP4 |
| GO:CC nucleolus | 0.0169 | DDX21, GTPBP4, KRR1, NOL6, RRP12, RSL1D1, UTP15, UTP4 |
| GO:BP ribosomal small subunit biogenesis | 0.0171 | KRR1, NOL6, UTP15, UTP4 |
| KEGG Ribosome biogenesis in eukaryotes - Homo sapiens (human) | 0.0171 | GTPBP4, NOL6, UTP15, UTP4 |
| GO:CC preribosome | 0.0234 | KRR1, NOL6, UTP15, UTP4 |
| GO:MF nucleic acid binding | 0.0253 | CCT3, DDX21, GTPBP4, KRR1, NAA15, NOL6, RRP12, RSL1D1, SUPT16H, UTP15, UTP4 |
| GO:BP ribonucleoprotein complex biogenesis | 0.0329 | DDX21, GTPBP4, KRR1, NOL6, UTP15, UTP4 |

### STRING and hu.MAP

STRING provides substantial prior support for a known ribosome-biogenesis network. The strongest relationships form a densely interconnected core involving KRR1, NOL6, UTP15, UTP4, RSL1D1, RRP12, and GTPBP4, with additional links to DDX21. STRING functional results independently point to preribosome assembly, rRNA processing, the small-subunit processome, the nucleolus, and RNA metabolism (10 supplementary STRING terms; within-query FDR 2.77e-07–0.004). The literature-linked STRING results also connect several members to early preribosome assembly and ribosomal-protein assembly studies (STRING PMID (2016) Stepwise and dynamic assembly of the earliest precursors of small ribosomal subunits in yeast.; within-query FDR = 0.0012) (STRING PMID (2012) Interrelationships between yeast ribosomal protein assembly events and transient ribosome biogenesis factors interactions in early pre-ribosomes.; within-query FDR = 0.0029). These are supplementary confirmations rather than replacements for the globally corrected GO and KEGG evidence. The module network itself is sparser than the STRING prior network and includes peripheral genes such as INTS8, SUPT16H, NUP188, NAA15, and CCT3, suggesting that co-abundance captures a core nucleolar program together with expression-linked nuclear and proteostasis interfaces. hu.MAP identifies UTP15 and UTP4 together in a high-confidence small-subunit-processome-related complex (hu.MAP huMAP3_01743.1) and in a broader RNA-processing and exosome-associated complex (hu.MAP huMAP3_14264.1). The limited hu.MAP overlap means that the module is not simply a direct recovery of a single catalogued complex, while the STRING links show that much of its central core is already biologically established.

**STRING interactions (score >= 0.7)**: 23 of 78 gene pairs: DDX21–GTPBP4 (0.813); DDX21–RSL1D1 (0.81); GTPBP4–KRR1 (0.771); GTPBP4–NOL6 (0.781); GTPBP4–RRP12 (0.981); GTPBP4–RSL1D1 (0.996); GTPBP4–UTP15 (0.832); GTPBP4–UTP4 (0.889); KRR1–NOL6 (0.998); KRR1–RRP12 (0.992); KRR1–RSL1D1 (0.995); KRR1–UTP15 (0.998); KRR1–UTP4 (0.999); NOL6–RRP12 (0.863); NOL6–RSL1D1 (0.996); NOL6–UTP15 (0.998); NOL6–UTP4 (0.999); RRP12–RSL1D1 (0.97); RRP12–UTP15 (0.724); RRP12–UTP4 (0.891); RSL1D1–UTP15 (0.924); RSL1D1–UTP4 (0.996); UTP15–UTP4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 2.77e-07, 8 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 1.39e-06, 7 genes); Process rRNA processing (FDR = 2.58e-06, 8 genes); Process ncRNA processing (FDR = 3.25e-06, 9 genes); NetworkNeighborAL Small-subunit processome (FDR = 0.0003, 4 genes); COMPARTMENTS Nucleolus (FDR = 0.00064, 8 genes); Process Gene expression (FDR = 0.00066, 11 genes); Function RNA binding (FDR = 0.0008, 11 genes); Process RNA metabolic process (FDR = 0.0011, 10 genes); PMID (2016) Stepwise and dynamic assembly of the earliest precursors of small ribosomal subunits in yeast. (FDR = 0.0012, 6 genes); PMID (2012) Interrelationships between yeast ribosomal protein assembly events and transient ribosome biogenesis factors interactions in early pre-ribosomes. (FDR = 0.0029, 5 genes); KEGG Ribosome biogenesis in eukaryotes (FDR = 0.0035, 4 genes); RCTM rRNA modification in the nucleus and cytosol (FDR = 0.004, 4 genes); RCTM Major pathway of rRNA processing in the nucleolus and cytosol (FDR = 0.004, 5 genes); Keyword Nucleus (FDR = 0.0067, 12 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01743.1 (UTP15, UTP4; 2/6); huMAP3_14264.1 (UTP15, UTP4; 2/20)

### Novelty

The biological function is not a new discovery: ribosome biogenesis, rRNA processing, the nucleolus, and the small-subunit processome are already strongly represented in GO, KEGG, STRING, and hu.MAP. The module-level observation may nevertheless be useful or potentially novel as a conserved co-abundance pattern shared by cell line and kidney, especially because it combines a known small-subunit-processome core with peripheral genes involved in transcription, nuclear transport, RNA surveillance, and protein folding. However, the available evidence does not establish that this cross-context co-abundance arrangement is unprecedented. Absence of a complete matching complex in hu.MAP or absence of an interaction for some genes in STRING cannot by itself demonstrate novelty. A defensible conclusion is that the module represents a new context-specific organization or recovery of a largely known ribosome-biogenesis program, rather than a newly discovered molecular pathway.

**Hypothesis.** Hypothesis: in both cell line and kidney, coordinated abundance of a nucleolar RNA-processing machinery supports demand for ribosome production and translational capacity. A central small-subunit-processome assembly involving KRR1, NOL6, UTP15, and UTP4 may be coupled through GTPBP4 and RRP12 to rRNA remodeling, preribosome maturation, and nucleolar trafficking. DDX21 could provide RNA-helicase activity at the interface between rRNA structure and assembly, while RSL1D1 and the peripheral nuclear factors may reflect linked RNA surveillance, transcriptional, or cell-state programs. The co-abundance pattern could therefore report coordinated nucleolar workload rather than a stable physical complex containing every module member. This hypothesis should be tested by perturbing the core processome genes and measuring pre-rRNA maturation, nucleolar organization, ribosome output, and the abundance of the peripheral module proteins in relevant cellular contexts.

### Important genes

#### GTPBP4

- **Related proteins** (co-abundance neighbors): DDX21 (0.87), SUPT16H (0.85), KRR1 (0.83), RSL1D1 (0.82), NAA15 (0.81), NUP188 (0.81), RRP12 (0.81), CCT3 (0.80); STRING partners: DDX21 (0.813), KRR1 (0.771), NOL6 (0.781), RRP12 (0.981), RSL1D1 (0.996), UTP15 (0.832), UTP4 (0.889)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GTP binding protein 4. GTP-binding proteins are GTPases and function as molecular switches that can flip between two states: active, when GTP is bound, and inactive, when GDP is bound. 'Active' in this context usually means that the molecule acts as a signal to trigger other events in the cell. When an extracellular ligand binds to a G-protein-linked receptor, the receptor changes its conformation and switches on the tr…
- **Diseases (Open Targets)**: gout (0.367); neurodegenerative disease (0.339); chronic kidney disease (0.110); hepatocellular carcinoma (0.100); hypotensive disorder (0.094)
- **Europe PMC papers**: 430
- **Why important**: GTPBP4 is the strongest network hub in the module and connects the core nucleolar ribosome-biogenesis genes with peripheral factors including DDX21, SUPT16H, NAA15, NUP188, RRP12, and CCT3. It participates in nearly all of the central primary enrichment themes, including RNA binding, rRNA processing, nucleolar biology, ribosome biogenesis, and the eukaryotic ribosome-biogenesis pathway (8 globally significant GO/KEGG terms, q_global 0.00161–0.0329; see the table). STRING independently supports links to the preribosome and rRNA-processing machinery (4 supplementary STRING terms; within-query FDR 2.77e-07–3.25e-06). It also has kidney protein detection and a substantial literature, with disease associations including chronic kidney disease and cancer-related conditions.
- **Conclusion**: Established evidence identifies GTPBP4 as a central co-abundance hub and a component of the nucleolar ribosome-biogenesis program. Its network position makes it a plausible organizing node, but the data do not prove that it causally drives the entire module. A testable hypothesis is that perturbing GTPBP4 will affect both the core processome-associated genes and the peripheral nuclear interfaces.

#### DDX21

- **Related proteins** (co-abundance neighbors): GTPBP4 (0.87), RRP12 (0.83); STRING partners: GTPBP4 (0.813), RSL1D1 (0.81)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 is a nucleolar-rim RNA helicase with a direct mechanistic connection to RNA structure and ribosome or RNP assembly. It is represented in the primary RNA-binding, rRNA-processing, nucleolar, ribosome-biogenesis, and RNP-biogenesis terms (7 globally significant GO/KEGG terms, q_global 0.00161–0.0329; see the table). It links to GTPBP4 and RRP12 in the module and has STRING support for rRNA processing and nucleolar organization (4 supplementary STRING terms; within-query FDR 2.77e-07–0.00064). DDX21 has the largest literature volume among the selected genes and has disease associations involving neurodegenerative and cancer-related conditions.
- **Conclusion**: Established evidence supports DDX21 as an RNA-processing and nucleolar component of the module, with a plausible role in remodeling RNA during ribosome assembly. Its lower local degree than GTPBP4 does not diminish its mechanistic importance, because helicase activity can be functionally central without producing many abundance correlations. Whether DDX21 controls the shared cell-line and kidney co-abundance state remains a hypothesis.

#### NOL6

- **Related proteins** (co-abundance neighbors): INTS8 (0.84); STRING partners: GTPBP4 (0.781), KRR1 (0.998), RRP12 (0.863), RSL1D1 (0.996), UTP15 (0.998), UTP4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleolar protein 6. The nucleolus is a dense subnuclear membraneless organelle that assembles around clusters of rRNA genes and functions in ribosome biogenesis. This gene encodes a nucleolar RNA-associated protein that is highly conserved between species. RNase treatment of permeabilized cells indicates that the nucleolar localization is RNA dependent. Further studies suggest that the protein is associated with ribo…
- **Diseases (Open Targets)**: neurodegenerative disease (0.119); hepatocellular carcinoma (0.054); hidradenitis (0.052); response to xenobiotic stimulus (0.045); gastric cancer (0.036)
- **Europe PMC papers**: 335
- **Why important**: NOL6 has the broadest annotation coverage within the primary enrichment results, appearing in RNA binding, rRNA processing, the small-subunit processome, ribosome biogenesis, the nucleolus, preribosome, and RNP-biogenesis terms (11 globally significant GO/KEGG terms, q_global 0.00161–0.0329; see the table). Its known function as an RNA-associated nucleolar protein involved in pre-rRNA and small-subunit maturation is directly concordant with the module interpretation. It is strongly connected in STRING to the core processome genes and appears across the STRING functional themes (15 supplementary STRING terms; within-query FDR 2.77e-07–0.0067). Its HPA profile includes nucleolar localization and cell-type enhancement in spermatid populations.
- **Conclusion**: Established evidence makes NOL6 a core functional marker of the module's small-subunit ribosome-biogenesis program. Its modest module degree likely reflects the measured co-abundance topology rather than limited biological relevance, because its external interaction and annotation evidence is extensive. A reasonable hypothesis is that NOL6 helps anchor the shared co-abundance signal to pre-rRNA maturation.

#### UTP4

- **Related proteins** (co-abundance neighbors): RRP12 (0.81); STRING partners: GTPBP4 (0.889), KRR1 (0.999), NOL6 (0.999), RRP12 (0.891), RSL1D1 (0.996), UTP15 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_01743.1, huMAP3_14264.1
- **Function (MyGene.info)**: UTP4 small subunit processome component. This gene encodes a WD40-repeat-containing protein that is localized to the nucleolus. Mutation of this gene causes North American Indian childhood cirrhosis, a severe intrahepatic cholestasis that results in transient neonatal jaundice, and progresses to periportal fibrosis and cirrhosis in childhood and adolescence. Alternative splicing results in multiple transcript variants. [provided by RefSe…
- **Diseases (Open Targets)**: hereditary North American Indian childhood cirrhosis (0.420); cardiovascular disorder (0.101); basal cell carcinoma (0.079); hypertensive disorder (0.064); osteosarcoma (0.052)
- **Europe PMC papers**: 214
- **Why important**: UTP4 is a small-subunit-processome component and is present in every primary enrichment theme listed for the module (11 globally significant GO/KEGG terms, q_global 0.00161–0.0329; see the table). It is part of the densely connected STRING core and is paired with UTP15 in both hu.MAP complexes (hu.MAP huMAP3_01743.1) (hu.MAP huMAP3_14264.1). HPA places UTP4 in the nucleolar fibrillar center and reports kidney detection, with cell-type enhancement in oocytes and proximal tubule cells. Its established disease association with North American Indian childhood cirrhosis provides a direct example of the physiological consequences of disrupting this ribosome-biogenesis machinery.
- **Conclusion**: Established evidence identifies UTP4 as a core processome component and a strong molecular anchor for the module. The disease association supports the importance of intact UTP4 function, but does not show that this module causes kidney disease or any other listed condition. UTP4 is a strong candidate for testing whether the shared module reflects functional small-subunit assembly.

#### RRP12

- **Related proteins** (co-abundance neighbors): DDX21 (0.83), UTP4 (0.81), SUPT16H (0.81), GTPBP4 (0.81); STRING partners: GTPBP4 (0.981), KRR1 (0.992), NOL6 (0.863), RSL1D1 (0.97), UTP15 (0.724), UTP4 (0.891)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal RNA processing 12 homolog. Enables RNA binding activity. Predicted to be involved in rRNA processing. Located in cytosol; nucleolus; and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.435); bilateral striopallidodentate calcinosis (0.370); colorectal carcinoma (0.079); hepatocellular carcinoma (0.075); neoplasm (0.067)
- **Europe PMC papers**: 367
- **Why important**: RRP12 provides a bridge between the central nucleolar machinery and the broader module. It connects to GTPBP4, DDX21, UTP4, and SUPT16H in the co-abundance graph, has very strong STRING relationships to several core processome-associated genes, and appears in the primary RNA-binding and nucleolar terms (GO:MF RNA binding; q_global = 0.00161) (GO:CC nucleolus; q_global = 0.0169) (GO:MF nucleic acid binding; q_global = 0.0253). Its annotation identifies it as an rRNA-processing factor, while HPA reports group enrichment in bone marrow and cell-type enhancement in myeloid and neutrophil-related populations. It also has disease associations including neurodegenerative and neoplastic conditions.
- **Conclusion**: Established evidence supports RRP12 as an RNA-binding and nucleolar ribosome-biogenesis factor that may connect core assembly to tissue or cell-state variation. The HPA pattern raises the possibility that abundance of this component is sensitive to hematopoietic or myeloid composition, but the low immune specificity of most of the module argues against reducing the entire module to blood contamination. Its bridging role is a hypothesis that requires perturbation or cell-resolved validation.

## Module 5

**Tissue pair**: cell line and kidney  
**Genes (5)**: EIF3C, HARS1, KIFBP, RUVBL2, TARS1

### Function

The module does not have a globally significant GO or KEGG enrichment: no globally significant GO/KEGG term passed global correction. Its supplementary STRING signals point toward protein biosynthesis and aminoacyl-tRNA synthetase activity, because HARS1 and TARS1 share an anticodon-binding annotation (STRING Pfam Anticodon binding domain; within-query FDR = 0.0341), while EIF3C, HARS1, and TARS1 contribute to the protein-biosynthesis signal (STRING Keyword Protein biosynthesis; within-query FDR = 0.0372). The gene set is therefore most consistent with a cytosolic protein-production and translation-support context, but it is not functionally homogeneous: RUVBL2 contributes DNA maintenance and ATPase biology, KIFBP contributes microtubule- and mitochondrion-associated transport, and EIF3C contributes translation initiation. The network is a short chain with HARS1 and TARS1 as its most clearly connected functional pair, and EIF3C linking that pair toward KIFBP.

**Cell composition.** The module is not dominated by plasma or secreted proteins: all genes are annotated as non-secreted, cytosolic or intracellular proteins. HPA reports low immune-cell specificity for every gene, with no enriched blood-cell category, arguing against a blood-cell explanation. Most genes have low tissue specificity, and all are detected in kidney. Individual cell-type-enhanced annotations occur for EIF3C, KIFBP, and RUVBL2, including neural, oocyte, germ-cell, and ciliated-cell contexts, but these patterns do not define a shared tissue identity. The module therefore looks more like a broadly expressed intracellular program measured in kidney than a plasma, secreted, or blood-contamination module. The HPA summary provides no matching cell-line tissue protein comparison.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports one high-confidence relationship, between HARS1 and TARS1. This is biologically plausible because both are cytoplasmic aminoacyl-tRNA synthetases and both contribute to the supplementary anticodon-binding and protein-biosynthesis signals (STRING Pfam Anticodon binding domain; within-query FDR = 0.0341) (STRING Keyword Protein biosynthesis; within-query FDR = 0.0372). The remaining module links are not supported by high-confidence STRING partners in the supplied evidence. No hu.MAP complex contains at least two module members, so the module is not supported as a known hu.MAP multiprotein complex. Overall, the network combines one established functional association with co-abundance links that may reflect shared regulation, cellular state, or indirect coupling rather than physical binding.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: HARS1–TARS1 (0.865)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam Anticodon binding domain (FDR = 0.0341, 2 genes); Keyword Protein biosynthesis (FDR = 0.0372, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This should not be called a newly discovered protein complex or a proven new pathway. The HARS1-TARS1 relationship and the translation-related biology are already established by STRING and gene annotations. Conversely, the absence of hu.MAP support and the lack of additional supplied STRING relationships leave open the possibility that the particular co-abundance arrangement across cell line and kidney is a new systems-level observation. Database absence alone is insufficient to establish novelty, so the appropriate conclusion is a potentially novel co-abundance pattern built partly from known biology, requiring independent replication and experimental testing.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular state involving protein-production demand, in which translation initiation through EIF3C is coordinated with aminoacyl-tRNA charging through HARS1 and TARS1. RUVBL2 may mark a linked ATPase, genome-maintenance, or proliferative state, while KIFBP may connect that state to microtubule-dependent mitochondrial or neuronal-type transport programs. The observed co-abundance could therefore arise from coordinated regulation of translation, energy or organelle distribution, and cellular maintenance rather than from one stable physical complex. This is a hypothesis, not a conclusion from enrichment, because no GO or KEGG term passed global correction and hu.MAP supplied no supporting complex.

### Important genes

#### HARS1

- **Related proteins** (co-abundance neighbors): TARS1 (0.82), EIF3C (0.81); STRING partners: TARS1 (0.865)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: histidyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a cytoplasmic enzyme which belongs to the class II family of aminoacyl-tRNA synthetases. The enzyme is responsible for the synthesis of histidyl-transfer RNA, which is essential for the incorporation of histidine into proteins. The gene is located in a head-to-hea…
- **Diseases (Open Targets)**: autosomal dominant Charcot-Marie-Tooth disease type 2W (0.763); Usher syndrome type 3B (0.540); spastic ataxia (0.510); Intellectual disability (0.486); Dysarthria (0.484)
- **Europe PMC papers**: 197
- **Why important**: HARS1 is a central node in the module and forms the only supplied high-confidence STRING relationship, with TARS1. Its established function is cytoplasmic histidyl-tRNA aminoacylation, directly connecting the network to translation. It contributes to both supplementary STRING signals (STRING Pfam Anticodon binding domain; within-query FDR = 0.0341) (STRING Keyword Protein biosynthesis; within-query FDR = 0.0372), has kidney protein detection, and has substantial disease and literature support, including associations with inherited neurological disorders.
- **Conclusion**: Established evidence supports HARS1 as a core translation-related component and as the strongest known interaction anchor in the module. Its co-abundance with EIF3C and TARS1 is consistent with coordinated protein synthesis. It is not established that HARS1 functionally recruits the other module members in this tissue pair.

#### TARS1

- **Related proteins** (co-abundance neighbors): HARS1 (0.82), RUVBL2 (0.81); STRING partners: HARS1 (0.865)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: threonyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Threonyl-tRNA synthetase belongs to the class-II aminoacyl-tRNA synthetase family [provided by RefSeq, Jul 2008]…
- **Diseases (Open Targets)**: trichothiodystrophy 7, nonphotosensitive (0.520); trichothiodystrophy (0.430); actinic keratosis (0.356); dyshidrosis (0.315); placental abruption (0.307)
- **Europe PMC papers**: 147
- **Why important**: TARS1 is a central node adjacent to HARS1 and RUVBL2 and participates in the only high-confidence STRING pair. Its established function is cytoplasmic threonyl-tRNA aminoacylation, and it contributes to the supplementary anticodon-binding and protein-biosynthesis signals (STRING Pfam Anticodon binding domain; within-query FDR = 0.0341) (STRING Keyword Protein biosynthesis; within-query FDR = 0.0372). It is detected in kidney and has disease annotations and a substantial literature base.
- **Conclusion**: Established evidence identifies TARS1 as a core aminoacylation component and the most direct bridge from the translation-related pair toward RUVBL2. The module supports coordinated abundance with HARS1, but it does not demonstrate a new TARS1-containing complex or a direct mechanistic link to RUVBL2.

#### EIF3C

- **Related proteins** (co-abundance neighbors): KIFBP (0.83), HARS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C has a central network position, connecting KIFBP with HARS1. It is a component of the eukaryotic translation-initiation factor and contributes to cytoplasmic translation initiation and positive regulation of translation. It is detected in kidney, has the largest supplied literature volume among the module genes, and contributes to the supplementary protein-biosynthesis signal (STRING Keyword Protein biosynthesis; within-query FDR = 0.0372).
- **Conclusion**: Established evidence supports EIF3C as the module's translation-initiation anchor and makes it a plausible coordinator of the HARS1-TARS1 translation-related signal. The link to KIFBP remains a co-abundance observation; the data do not establish that EIF3C directly controls microtubule or mitochondrial transport through KIFBP.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): TARS1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 is a peripheral bridge connected to TARS1 and has a substantial literature base. Its established annotations include ATPase and DNA-helicase activities, DNA repair, DNA recombination, telomere maintenance, and snoRNP assembly. It is tissue-enhanced in testis and detected in kidney, giving it a distinctive expression context within this otherwise broadly expressed module.
- **Conclusion**: Established evidence supports RUVBL2 as an intracellular ATPase and genome-maintenance factor that may report a cellular state associated with the translation-related genes. Its connection to TARS1 is not supported by the supplied high-confidence STRING or hu.MAP evidence, so any functional coupling between them remains a hypothesis.

#### KIFBP

- **Related proteins** (co-abundance neighbors): EIF3C (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family binding protein. This gene encodes a kinesin family member 1 binding protein that is characterized by two tetratrico peptide repeats. The encoded protein localizes to the mitochondria and may be involved in regulating transport of the mitochondria. Mutations in this gene are associated with Goldberg-Shprintzen megacolon syndrome. [provided by RefSeq, Mar 2010].
- **Diseases (Open Targets)**: Goldberg-Shprintzen syndrome (0.723); Shprintzen-Goldberg syndrome (0.379); epilepsy (0.148); neuropathy (0.119); African iron overload (0.070)
- **Europe PMC papers**: 54
- **Why important**: KIFBP is the peripheral module member connected to EIF3C and has the most limited supplied literature volume. Its established annotations implicate kinesin binding, microtubule organization, mitochondrial transport along microtubules, and neuron projection maintenance. It is detected in kidney and has a strong disease association with Goldberg-Shprintzen megacolon syndrome, making it biologically important despite its peripheral network position.
- **Conclusion**: Established evidence supports KIFBP as a cytoskeletal and organelle-transport regulator rather than a translation factor. Its co-abundance with EIF3C may indicate shared cellular-state regulation or transport of translation-related machinery, but a direct mechanistic connection is not established by the supplied interaction resources.
