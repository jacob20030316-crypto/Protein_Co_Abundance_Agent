# Conserved co-abundance modules: liver and stem_cells

## Module 0

**Tissue pair**: liver and stem_cells  
**Genes (14)**: HIBADH, ACSL1, ALDH1A1, ALDH7A1, CNDP2, COQ9, CPT2, EPHX1, MMUT, NNT, NUDT16, SELENBP1, SCP2, TYMP

### Function

The strongest integrated interpretation is a mitochondrial, peroxisomal, and cytosolic metabolic module centered on lipid handling and energy metabolism. Primary enrichment supports long-chain fatty-acid metabolism through (GO:BP long-chain fatty acid metabolic process; q_global = 0.0367), involving ACSL1, CPT2, EPHX1, and SCP2. The supplementary STRING annotations broaden this toward general metabolism and mitochondrial redox, amino-acid, nucleotide, aldehyde, and cofactor pathways through (STRING RCTM Metabolism; within-query FDR = 0.0055) and (STRING KEGG Metabolic pathways; within-query FDR = 0.0123). The network is not a single linear pathway: it contains a lipid-oxidation branch, mitochondrial cofactor and redox functions, aldehyde and small-molecule detoxification, and intermediary amino-acid metabolism. Thus, co-abundance most plausibly reflects coordinated metabolic state rather than a physically unified protein complex.

**Cell composition.** The HPA profile is predominantly tissue-associated rather than secreted: no module gene is secreted, and nearly all proteins are detected in liver. Liver and hepatocyte enrichment is prominent, with additional skeletal-muscle, adipose, adrenal, intestinal, trophoblast, and other cell-type signals. Several genes also show immune-cell enhancement or enrichment, especially ACSL1, ALDH1A1, EPHX1, TYMP, NUDT16, and SELENBP1, with myeloid and granulocyte patterns particularly visible. This does not look like a plasma-protein module. The shared signal could reflect hepatocyte metabolism conserved across the two tissue groups, but immune or other shared-cell contributions should be considered, especially because the stem-cell tissue has no matching HPA tissue-level protein annotation.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP long-chain fatty acid metabolic process | 0.0367 | ACSL1, CPT2, EPHX1, SCP2 |

### STRING and hu.MAP

STRING provides only a small number of high-confidence pairwise relationships relative to the module: ALDH7A1 is linked to CNDP2 and HIBADH. These relationships support a local aldehyde, amino-acid, and small-molecule metabolism neighborhood, but they do not establish the whole module as a physical interaction network. The STRING enrichment terms (STRING RCTM Metabolism; within-query FDR = 0.0055) and (STRING KEGG Metabolic pathways; within-query FDR = 0.0123) support broad metabolic coherence but are supplementary rather than globally corrected primary evidence. hu.MAP contributes complex (hu.MAP huMAP3_13468.1), in which MMUT and CPT2 occur together, consistent with mitochondrial intermediary metabolism and fatty-acid oxidation. Most module genes have no listed hu.MAP complex membership or STRING partner, so the co-abundance structure is stronger as a coordinated expression or protein-abundance program than as a known multiprotein complex.

**STRING interactions (score >= 0.7)**: 2 of 91 gene pairs: ALDH7A1–CNDP2 (0.908); ALDH7A1–HIBADH (0.927)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Metabolism (FDR = 0.0055, 13 genes); KEGG Metabolic pathways (FDR = 0.0123, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (MMUT, CPT2; 2/99)

### Novelty

This is not sufficient evidence to call the module a wholly new biological pathway. Its central functions are established: long-chain fatty-acid metabolism is supported by (GO:BP long-chain fatty acid metabolic process; q_global = 0.0367), and the individual roles of ACSL1, CPT2, SCP2, NNT, aldehyde dehydrogenases, and related metabolic enzymes are well documented in the supplied annotations. The potentially novel aspect is the conserved co-abundance combination across liver and stem_cells, particularly the coupling of lipid handling with redox, aldehyde detoxification, amino-acid catabolism, and mitochondrial cofactor metabolism. That combination should be treated as a candidate systems-level observation requiring validation in independent cohorts, cell-resolved data, and perturbation experiments. Limited STRING and hu.MAP coverage does not by itself prove novelty, because absence from those resources may reflect incomplete interaction knowledge or a regulatory rather than physical relationship.

**Hypothesis.** Hypothesis: the module represents a conserved metabolic stress-adaptation program in hepatocyte-like or metabolically active cells. Coordinated ACSL1, CPT2, and SCP2 activity may channel long-chain fatty acids toward mitochondrial and peroxisomal processing, while NNT supplies reducing power for biosynthesis and reactive-species control. EPHX1 and ALDH7A1 may help handle lipid- and xenobiotic-derived aldehydes, with CNDP2, HIBADH, and MMUT connecting the program to amino-acid and intermediary metabolism. The observed co-abundance may therefore reflect adaptation to changing lipid flux, redox demand, and detoxification load rather than direct binding among all module proteins. Immune-cell signals raise an alternative possibility that part of the pattern reflects shared myeloid or granulocyte contamination or composition; this should be tested by cell-type deconvolution and single-cell validation.

### Important genes

#### ACSL1

- **Related proteins** (co-abundance neighbors): NNT (0.85), COQ9 (0.83), EPHX1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 1. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. Several transcript variants enco…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.510); diabetes mellitus (0.501); diabetic neuropathy (0.404); neurodegenerative disease (0.368); menopause (0.334)
- **Europe PMC papers**: 4992
- **Why important**: ACSL1 is a high-connectivity bridge linking NNT, COQ9, and EPHX1 in the module. It is one of the genes in the primary long-chain fatty-acid term (GO:BP long-chain fatty acid metabolic process; q_global = 0.0367), and its annotation directly places it at the entry point where free long-chain fatty acids become fatty acyl-CoA esters. HPA supports liver, adipose, and skeletal-muscle expression and also shows neutrophil enrichment. Its disease associations include diabetes and diabetic neuropathy, and its substantial literature supports an established role in lipid handling.
- **Conclusion**: Established evidence supports ACSL1 as a key lipid-flux component and a plausible anchor of the module. The hypothesis that it coordinates the module's redox and detoxification branches is plausible from network placement but is not demonstrated by the supplied evidence.

#### CPT2

- **Related proteins** (co-abundance neighbors): NNT (0.84), HIBADH (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: carnitine palmitoyltransferase 2. The protein encoded by this gene is a nuclear protein which is transported to the mitochondrial inner membrane. Together with carnitine palmitoyltransferase I, the encoded protein oxidizes long-chain fatty acids in the mitochondria. Defects in this gene are associated with mitochondrial long-chain fatty-acid (LCFA) oxidation disorders. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: carnitine palmitoyl transferase II deficiency, myopathic form (0.830); carnitine palmitoyl transferase II deficiency, severe infantile form (0.800); carnitine palmitoyl transferase II deficiency, neonatal form (0.772); carnitine palmitoyltransferase II deficiency (0.710); hereditary disease (0.505)
- **Europe PMC papers**: 5133
- **Why important**: CPT2 is directly represented in (GO:BP long-chain fatty acid metabolic process; q_global = 0.0367) and is annotated as a mitochondrial long-chain fatty-acid oxidation and carnitine-shuttle enzyme. It connects NNT and HIBADH and is one of the two module members in hu.MAP complex (hu.MAP huMAP3_13468.1). HPA supports liver and hepatocyte enrichment, while Open Targets links it strongly to several inherited CPT2 deficiency phenotypes. Its extensive literature makes its role in fatty-acid oxidation especially well established.
- **Conclusion**: Established evidence identifies CPT2 as a core functional marker of the module's mitochondrial lipid-oxidation interpretation. Its complex membership supports a mitochondrial context, but does not prove that all module members operate in the same complex.

#### NNT

- **Related proteins** (co-abundance neighbors): ACSL1 (0.85), CPT2 (0.84), SCP2 (0.84), TYMP (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nicotinamide nucleotide transhydrogenase. This gene encodes an integral protein of the inner mitochondrial membrane. The enzyme couples hydride transfer between NAD(H) and NADP(+) to proton translocation across the inner mitochondrial membrane. Under most physiological conditions, the enzyme uses energy from the mitochondrial proton gradient to produce high concentrations of NADPH. The resulting NADPH is used for biosynthesis and in free …
- **Diseases (Open Targets)**: familial glucocorticoid deficiency (0.638); neurodegenerative disease (0.497); hereditary disease (0.453); atypical hemolytic-uremic syndrome with DGKE deficiency (0.416); Abnormality of the skeletal system (0.396)
- **Europe PMC papers**: 6111
- **Why important**: NNT has among the strongest network connectivity in the module and links ACSL1, CPT2, SCP2, and TYMP. Its annotation describes mitochondrial proton-coupled NADPH production, with roles in NADPH regeneration and reactive oxygen species metabolism. HPA detects it in liver and shows tissue enhancement in skeletal muscle and tongue. The gene has extensive literature and disease associations involving glucocorticoid deficiency, neurodegeneration, and hereditary phenotypes.
- **Conclusion**: Established evidence supports NNT as the redox-support component that could enable lipid metabolism and detoxification. Its proposed role as the energetic or redox coordinator of the entire module remains a hypothesis based on co-abundance and network position.

#### SCP2

- **Related proteins** (co-abundance neighbors): COQ9 (0.92), NNT (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Peroxisomes; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sterol carrier protein 2. This gene encodes two proteins: sterol carrier protein X (SCPx) and sterol carrier protein 2 (SCP2), as a result of transcription initiation from 2 independently regulated promoters. The transcript initiated from the proximal promoter encodes the longer SCPx protein, and the transcript initiated from the distal promoter encodes the shorter SCP2 protein, with the 2 proteins sharing a common C-termi…
- **Diseases (Open Targets)**: sterol carrier protein 2 deficiency (0.708); spermatogenic failure (0.191); stroke disorder (0.187); alcohol drinking (0.186); leukodystrophy (0.119)
- **Europe PMC papers**: 2268
- **Why important**: SCP2 connects COQ9 and NNT and is included in the primary long-chain-fatty-acid term (GO:BP long-chain fatty acid metabolic process; q_global = 0.0367). Its peroxisomal annotation spans fatty-acid beta-oxidation, steroid metabolism, and bile-acid metabolism, and HPA shows liver and hepatocyte enrichment. The gene has a recognized deficiency phenotype and a substantial literature base. It provides a mechanistic link between peroxisomal lipid processing and the mitochondrial/redox portion of the module.
- **Conclusion**: Established evidence supports SCP2 as a liver-centered peroxisomal lipid and sterol metabolism component. The hypothesis that it functionally couples peroxisomal and mitochondrial branches in this module requires direct flux or perturbation evidence.

#### ALDH7A1

- **Related proteins** (co-abundance neighbors): CNDP2 (0.87); STRING partners: CNDP2 (0.908), HIBADH (0.927)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 7 family member A1. The protein encoded by this gene is a member of subfamily 7 in the aldehyde dehydrogenase gene family. These enzymes are thought to play a major role in the detoxification of aldehydes generated by alcohol metabolism and lipid peroxidation. This particular member has homology to a previously described protein from the green garden pea, the 26g pea turgor protein. It is also involved in lysine cata…
- **Diseases (Open Targets)**: pyridoxine-dependent epilepsy (0.793); pyridoxine-dependent epilepsy caused by ALDH7A1 mutant (0.762); hereditary disease (0.538); Seizure (0.528); epilepsy (0.441)
- **Europe PMC papers**: 1705
- **Why important**: ALDH7A1 is the module's strongest local interaction hub in the curated STRING evidence, linking to CNDP2 and HIBADH through the relationships listed in the fact sheet. It is included in both supplementary metabolic terms (STRING RCTM Metabolism; within-query FDR = 0.0055) and (STRING KEGG Metabolic pathways; within-query FDR = 0.0123), is liver-enhanced, and is annotated for aldehyde detoxification and lysine catabolism. Its disease associations include pyridoxine-dependent epilepsy, and its literature supports a well-established role in aldehyde and amino-acid metabolism.
- **Conclusion**: Established evidence supports ALDH7A1 as a detoxification and amino-acid-catabolism component with a validated local network neighborhood. It may connect lipid-peroxidation products to the broader module, but that cross-branch mechanism is a hypothesis rather than a demonstrated interaction.

#### CNDP2

- **Related proteins** (co-abundance neighbors): ALDH7A1 (0.87), TYMP (0.86), ALDH1A1 (0.82), SELENBP1 (0.81); STRING partners: ALDH7A1 (0.908)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carnosine dipeptidase 2. CNDP2, also known as tissue carnosinase and peptidase A (EC 3.4.13.18), is a nonspecific dipeptidase rather than a selective carnosinase (Teufel et al., 2003 [PubMed 12473676]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: refractive error (0.436); duodenal ulcer (0.344); Abnormality of refraction (0.330); myopia (0.255); kidney disorder (0.253)
- **Europe PMC papers**: 898
- **Why important**: CNDP2 is highly connected in the module and links ALDH7A1, TYMP, ALDH1A1, and SELENBP1. It is supported by both supplementary STRING metabolic terms (STRING RCTM Metabolism; within-query FDR = 0.0055) and (STRING KEGG Metabolic pathways; within-query FDR = 0.0123), and its curated STRING relationship with ALDH7A1 is one of the module's few high-confidence physical or functional links. Its annotation covers dipeptide hydrolysis and glutathione-related metabolism, while HPA shows broad cell-type enhancement and liver detection. Its literature and disease associations are more limited than those of the main lipid enzymes, making it a useful candidate for testing whether the module contains a less-characterized metabolic connection.
- **Conclusion**: Established evidence supports CNDP2 as a metabolic and glutathione-related enzyme positioned at the interface of the module's aldehyde, nucleotide, and small-molecule branches. Its role as a mechanistic bridge between these branches is a testable hypothesis, not a confirmed function of the module.

## Module 1

**Tissue pair**: liver and stem_cells  
**Genes (5)**: NT5E, ATP2A2, NUP62, SUPV3L1, TM9SF2

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. The co-abundance pattern therefore does not establish a statistically supported common pathway. The gene annotations instead suggest a heterogeneous cellular module spanning intracellular calcium handling and membrane physiology through ATP2A2, extracellular nucleotide metabolism and lymphocyte-associated biology through NT5E, nuclear transport through NUP62, endosomal membrane biology through TM9SF2, and mitochondrial RNA surveillance through SUPV3L1. The network may represent coordinated cell-state or compartmental behavior rather than a single canonical biochemical pathway.

**Cell composition.** This is not predominantly a plasma-protein or classical secreted-protein module. The HPA summary reports a single secreted gene, while the gene-level annotations describe NT5E as intracellular and membrane-associated and describe the other genes as non-secreted. The module is also not strongly blood-cell enriched: most genes have low immune-cell specificity, with immune-cell enhancement reported for NT5E. Most genes have low tissue specificity, although ATP2A2 is enriched in muscle-related tissues and NT5E is tissue enhanced in cervix. Several genes show cell-type enhancement across diverse cell types, including muscle, endocrine, reproductive, endothelial, and neural progenitor populations. Thus, shared cell types or general cellular-state effects are plausible, but the HPA evidence does not support a simple blood-contamination explanation. Protein detection in liver is reported for most module genes, whereas there is no matching HPA tissue annotation for stem_cells; ATP2A2 is not detected by liver immunohistochemistry despite its transcript-level presence in the module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

None of the possible gene-pair relationships reached the supplied STRING interaction threshold, and no STRING partners were listed for any gene. No hu.MAP complex contains multiple module members. The co-abundance edges are therefore not independently supported here as established physical or functional interactions. The module should be interpreted as a coordinated abundance pattern, not as a validated protein complex or a known interaction network. The absence of STRING and hu.MAP support may reflect indirect regulation, context-specific associations, incomplete database coverage, or a dataset-specific correlation pattern.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module cannot be called a new biological discovery from the supplied evidence alone. It is potentially novel as a liver–stem-cell co-abundance pattern because it lacks overlapping STRING interactions, lacks a multi-member hu.MAP complex, and has no globally significant GO/KEGG annotation. However, those absences do not prove novelty: they may indicate weak or indirect relationships, limited database coverage, heterogeneous cellular composition, or a false-positive correlation structure. A novelty claim would require independent replication in additional liver and stem-cell datasets, preservation of the gene-level correlations, testing against cell-composition covariates, and experimental or perturbational validation.

**Hypothesis.** Hypothesis: the module represents a cross-tissue cellular-state program linking membrane and organelle homeostasis rather than a single molecular complex. In this model, ATP2A2 contributes calcium sequestration, NT5E modulates extracellular nucleotide signals, TM9SF2 contributes endosomal membrane function, NUP62 reflects regulated nucleocytoplasmic transport, and SUPV3L1 reflects mitochondrial RNA quality control. Their coordinated abundance could mark a shared stress, differentiation, or metabolic state in particular cell populations present in liver and stem-cell samples. This is a hypothesis rather than an established pathway; the absence of enrichment and external interaction support makes direct mechanistic coupling uncertain.

### Important genes

#### ATP2A2

- **Related proteins** (co-abundance neighbors): TM9SF2 (0.88), NUP62 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darie…
- **Diseases (Open Targets)**: Darier disease (0.823); acrokeratosis verruciformis (0.663); neurodegenerative disease (0.507); hereditary disease (0.416); schizophrenia (0.406)
- **Europe PMC papers**: 9327
- **Why important**: ATP2A2 has the strongest weighted position in the module and connects the module to TM9SF2 and NUP62. Its established function is calcium transport by a sarcoplasmic or endoplasmic reticulum ATPase, with roles in intracellular calcium homeostasis and muscle contraction–relaxation biology. It has the largest literature volume among the module genes and established disease associations including Darier disease and acrokeratosis verruciformis. HPA evidence links it to heart muscle, skeletal muscle, and tongue, with enhanced representation in cardiomyocytes and myonuclei.
- **Conclusion**: Established evidence supports ATP2A2 as the strongest biological anchor for calcium and membrane-organelle homeostasis in this module. It is not established that ATP2A2 mechanistically drives the other module genes; its inclusion may instead reflect a shared differentiated-cell or membrane-state signature.

#### NT5E

- **Related proteins** (co-abundance neighbors): SUPV3L1 (0.85), NUP62 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 5'-nucleotidase ecto. The protein encoded by this gene is a plasma membrane protein that catalyzes the conversion of extracellular nucleotides to membrane-permeable nucleosides. The encoded protein is used as a determinant of lymphocyte differentiation. Defects in this gene can lead to the calcification of joints and arteries. Two transcript variants encoding different isoforms have been found for this gene.[provided b…
- **Diseases (Open Targets)**: hereditary arterial and articular multiple calcification syndrome (0.721); autosomal recessive spinocerebellar ataxia 20 (0.556); Spinocerebellar atrophy (0.340); non-small cell lung carcinoma (0.329); placental abruption (0.289)
- **Europe PMC papers**: 4404
- **Why important**: NT5E has a strong central position and connects SUPV3L1 with NUP62. It is an ecto-nucleotidase that converts extracellular nucleotides to nucleosides and is associated with lymphocyte differentiation, extracellular ATP responses, and nucleotide catabolism. It has substantial literature and disease associations involving arterial and articular calcification and neurological disease. HPA identifies tissue enhancement in cervix, enhancement across several specialized cell types, and immune-cell enhancement in naive B-cell and naive CD8 T-cell populations.
- **Conclusion**: Established evidence supports NT5E as a plausible membrane signaling and extracellular nucleotide component. The module does not establish that immune signaling is its shared cross-tissue function, because most module genes have low immune-cell specificity and no enrichment term passed global correction.

#### NUP62

- **Related proteins** (co-abundance neighbors): NT5E (0.81), ATP2A2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 62. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. The protein encoded by this gene is a member of the FG-repeat containing nucleoporins and is localized to the nuclear pore ce…
- **Diseases (Open Targets)**: infantile bilateral striatal necrosis (0.609); familial infantile bilateral striatal necrosis (0.590); HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.529)
- **Europe PMC papers**: 1582
- **Why important**: NUP62 occupies a central network position, connecting NT5E and ATP2A2. It is a core nucleoporin involved in nucleocytoplasmic transport, nuclear RNA export, nuclear protein import, and cell-cycle-related nuclear organization. It has disease associations including infantile bilateral striatal necrosis and viral infectious disease, and its literature volume is substantial. HPA detects it in liver and reports cell-type enhancement in germ-cell populations.
- **Conclusion**: Established evidence supports NUP62 as a nuclear transport and nuclear-envelope marker within the module. Its co-abundance with membrane and mitochondrial genes is consistent with coordinated cellular organization, but a direct functional bridge among these proteins remains hypothetical.

#### TM9SF2

- **Related proteins** (co-abundance neighbors): ATP2A2 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transmembrane 9 superfamily member 2. This gene encodes a member of the transmembrane 9 superfamily. The encoded 76 kDa protein localizes to early endosomes in human cells. The encoded protein possesses a conserved and highly hydrophobic C-terminal domain which contains nine transmembrane domains. The protein may play a role in small molecule transport or act as an ion channel. A pseudogene associated with this gene is located on the …
- **Diseases (Open Targets)**: neurodegenerative disease (0.461); lysosomal storage disease (0.367); asthma (0.332); chronic rhinosinusitis (0.298); multinodular goiter (0.273)
- **Europe PMC papers**: 306
- **Why important**: TM9SF2 provides the module's endosomal and multipass-membrane component and is connected to ATP2A2. Its established annotation places it in early endosomes, with possible roles in small-molecule transport or ion-channel activity, membrane localization, ceramide metabolism, and glycosphingolipid biosynthesis. It has a smaller literature volume than the principal module hubs but has disease associations spanning neurodegenerative, lysosomal-storage, respiratory, and thyroid-related conditions.
- **Conclusion**: Established evidence supports TM9SF2 as a membrane-trafficking or lipid-associated component. Its role in this module is most plausibly contextual or state-related; the available data do not establish a direct interaction with ATP2A2 or the other genes.

#### SUPV3L1

- **Related proteins** (co-abundance neighbors): NT5E (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Suv3 like RNA helicase. Enables helicase activity; nucleic acid binding activity; and protein homodimerization activity. Involved in several processes, including mitochondrial RNA metabolic process; mitochondrion morphogenesis; and positive regulation of mitochondrial RNA catabolic process. Located in mitochondrial nucleoid and nucleus. Part of mitochondrial degradosome. [provided by Alliance of Genome Resources, Apr 202…
- **Diseases (Open Targets)**: neurodegenerative disease (0.541); response to vaccine (0.276); neoplasm (0.041); gestational diabetes (0.036); seasonal allergic rhinitis (0.025)
- **Europe PMC papers**: 275
- **Why important**: SUPV3L1 is connected to NT5E and contributes a mitochondrial component that is otherwise distinct from the membrane and nuclear annotations. It encodes a helicase involved in mitochondrial RNA degradation, mitochondrial RNA processing, mitochondrial morphogenesis, and the mitochondrial degradosome. It has disease associations including neurodegenerative disease and a more limited literature volume than ATP2A2, NT5E, or NUP62.
- **Conclusion**: Established evidence supports SUPV3L1 as a mitochondrial RNA quality-control factor. Its presence does not demonstrate a mitochondrial–extracellular nucleotide pathway; the connection to NT5E is currently a co-abundance observation and may reflect a shared cellular state.

## Module 2

**Tissue pair**: liver and stem_cells  
**Genes (30)**: PRKAG1, AMPD2, ARSA, GLB1, BIN1, CIAO1, GPS1, CYFIP1, DNPEP, DPP9, EIF2B4, EPS8L2, GLUL, GNA11, GNS, LIMS1, MTAP, NDRG1, NHLRC2, NRDC, NUP107, PDCD6IP, PDE12, PDXK, PRRC1, SEC23A, TMEM120A, EFTUD2, UBA3, ATP6V1C1

### Function

The module does not have a statistically supported GO or KEGG functional enrichment: no GO/KEGG term passed global correction. Its composition instead suggests a heterogeneous intracellular maintenance module with contributions from proteolysis, lysosomal and glycoconjugate turnover, vesicle trafficking, cytoskeletal organization, translation control, nucleotide and energy metabolism, and cellular signaling. The strongest network anchors are DPP9, GNA11, and UBA3, but the module is not organized around a single coherent pathway. Local functional clues include lysosomal catabolism through ARSA, GLB1, and GNS; ER-to-Golgi trafficking through SEC23A; vesicle and ESCRT-related biology through PDCD6IP; intracellular acidification through ATP6V1C1; protein neddylation through UBA3 and GPS1; and energy sensing through PRKAG1. These annotations support a broad cellular homeostasis interpretation rather than a demonstrated pathway-level function. The lack of enrichment should not be interpreted as evidence that the module is false.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the HPA summary identifies only a minority of genes as secreted, and many annotated proteins are cytosolic, nuclear, vesicular, lysosomal, or membrane-associated. Most genes have low tissue specificity, consistent with broadly expressed cellular machinery rather than a strongly liver-specific program. Liver protein detection is present for many members, but there is no matching HPA stem-cell tissue category, so the HPA data cannot establish equivalent protein expression in stem cells. Cell-type annotations are heterogeneous, with recurring signals for spermatids, neutrophils, monocytes, esophageal apical cells, and several neural or muscle-related cell types. A subset has immune-cell enhancement, but the module is not dominated by blood-cell markers. The shared liver–stem-cell signal could therefore reflect broadly used intracellular processes, shared cell states, or sample-composition effects rather than a specialized liver–stem-cell mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a sparse set of high-confidence relationships within the module. The supported links are ARSA–GLB1, GLB1–GNS, and PRRC1–SEC23A. These relationships reinforce a local lysosomal or glycoconjugate-processing neighborhood and a separate COPII or secretory-trafficking neighborhood, but they do not connect the entire module into a known interaction network. hu.MAP supports the PRRC1–SEC23A pairing in complexes C1 and C2, with the broader complexes containing multiple SEC-family proteins and associated factors. CIAO1–EIF2B4 is represented in complex C3, but that complex is broad and contains many unrelated or context-dependent members. Thus, the external databases validate selected local relationships, especially the SEC23A–PRRC1 pair and the lysosomal enzyme pairings, while also indicating that most co-abundance edges are not established physical interactions. Co-abundance should therefore not be interpreted as direct binding.

**STRING interactions (score >= 0.7)**: 3 of 435 gene pairs: ARSA–GLB1 (0.702); GLB1–GNS (0.957); PRRC1–SEC23A (0.796)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11237.1 (SEC23A, PRRC1; 2/12); huMAP3_13535.1 (SEC23A, PRRC1; 2/14); huMAP3_11232.1 (CIAO1, EIF2B4; 2/78)

### Novelty

The module may represent a novel co-abundance configuration, because most of its internal relationships are absent from the supplied STRING and hu.MAP evidence and the module lacks a globally significant GO or KEGG signature. However, it cannot be called a definitively new biological pathway. Several component functions and local relationships are already established, including lysosomal substrate degradation, COPII trafficking, protein neddylation, V-ATPase biology, and metabolic regulation. Absence from STRING or hu.MAP alone does not prove novelty, since co-abundance can arise from shared regulation, cell composition, indirect pathway coupling, or context-specific interactions. The most defensible conclusion is that the module is a potentially novel cross-tissue expression organization assembled from largely known cellular functions, requiring independent replication and perturbation before being considered a new mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated cellular housekeeping during a shared state of protein and organelle turnover in liver and stem-cell samples. In this model, DPP9-linked proteolytic regulation, lysosomal glycoconjugate processing by ARSA, GLB1, and GNS, intracellular acidification through ATP6V1C1, ER-to-Golgi export through SEC23A, and protein-modification control through UBA3 are coupled indirectly by a common demand for proteostasis, membrane trafficking, and metabolic adaptation. GNA11, LIMS1, EPS8L2, and PDCD6IP could connect signaling, adhesion, cytoskeletal remodeling, and vesicle dynamics. This is a mechanistic proposal rather than an established conclusion; the current evidence does not demonstrate that these proteins act in one physical complex or that the module is specific to stem-cell biology.

### Important genes

#### DPP9

- **Related proteins** (co-abundance neighbors): NHLRC2 (0.93), PDCD6IP (0.87), MTAP (0.85), PRKAG1 (0.81), PDXK (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dipeptidyl peptidase 9. This gene encodes a protein that is a member of the S9B family in clan SC of the serine proteases. The protein has been shown to have post-proline dipeptidyl aminopeptidase activity, cleaving Xaa-Pro dipeptides from the N-termini of proteins. Although the activity of this protein is similar to that of dipeptidyl peptidase 4 (DPP4), it does not appear to be membrane bound. In general, dipeptidyl pe…
- **Diseases (Open Targets)**: hatipoglu immunodeficiency syndrome (0.624); COVID-19 (0.556); idiopathic pulmonary fibrosis (0.436); neurodegenerative disease (0.397); respiratory failure (0.351)
- **Europe PMC papers**: 1869
- **Why important**: DPP9 is a prominent network hub with links to NHLRC2, PDCD6IP, MTAP, PRKAG1, and PDXK. Its established dipeptidyl aminopeptidase activity provides a plausible regulatory connection between proteolysis, inflammatory cell death, and metabolic or stress responses. It also has substantial literature support and disease associations involving immunodeficiency, COVID-related disease, pulmonary fibrosis, respiratory failure, and neurodegeneration.
- **Conclusion**: Established evidence supports DPP9 as an intracellular protease with roles in substrate regulation and inflammatory or cell-death biology, and its network position makes it an important module anchor. The hypothesis that DPP9 coordinates the other module processes is not established; its high co-abundance connectivity may instead reflect shared cellular state or indirect regulation.

#### GNA11

- **Related proteins** (co-abundance neighbors): ARSA (0.89), AMPD2 (0.86), GLB1 (0.85), EPS8L2 (0.82), MTAP (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein subunit alpha 11. The protein encoded by this gene belongs to the family of guanine nucleotide-binding proteins (G proteins), which function as modulators or transducers in various transmembrane signaling systems. G proteins are composed of 3 units: alpha, beta and gamma. This gene encodes one of the alpha subunits (subunit alpha-11). Mutations in this gene have been associated with hypocalciuric hypercalcemia type…
- **Diseases (Open Targets)**: familial hypoparathyroidism (0.754); familial hypocalciuric hypercalcemia 2 (0.736); autosomal dominant hypocalcemia (0.611); congenital hemangioma (0.494); uveal melanoma (0.469)
- **Europe PMC papers**: 4418
- **Why important**: GNA11 is a network hub connecting ARSA, AMPD2, GLB1, EPS8L2, and MTAP. As a heterotrimeric G-protein alpha subunit, it can link receptor signaling to adenylate cyclase and phospholipase C pathways. It is detected in liver and has strong disease relevance for familial hypocalciuric hypercalcemia, hypocalcemia, hypoparathyroidism, and related disorders, with substantial literature volume.
- **Conclusion**: Established evidence supports GNA11 as a signaling transducer and explains why it could bridge metabolic, membrane, and cytoskeletal signals. It is not established that GNA11 drives the module or directly regulates the lysosomal and trafficking genes; that interpretation remains a hypothesis.

#### SEC23A

- **Related proteins** (co-abundance neighbors): PDCD6IP (0.82); STRING partners: PRRC1 (0.796)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11237.1, huMAP3_13535.1
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A is the module representative of COPII-mediated ER export and is supported by both STRING and hu.MAP through its relationship with PRRC1 and complexes C1 and C2. Its known role in ER-to-Golgi transport offers a concrete cellular process that could connect protein maturation, vesicle production, and membrane homeostasis. It also has a defined human disease association with craniolenticulosutural dysplasia.
- **Conclusion**: Established evidence identifies SEC23A as a COPII component required for ER-to-Golgi trafficking, and the SEC23A–PRRC1 relationship is externally supported. The claim that this trafficking axis organizes the full module is not established, particularly because most other module edges lack corresponding physical-interaction support.

#### GLB1

- **Related proteins** (co-abundance neighbors): GNS (0.87), GNA11 (0.85); STRING partners: ARSA (0.702), GNS (0.957)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galactosidase beta 1. This gene encodes a member of the glycosyl hydrolase 35 family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature lysosomal enzyme. This enzyme catalyzes the hydrolysis of a terminal beta-linked galactose residue from ganglioside substrates and other glycoconjugates. Mutat…
- **Diseases (Open Targets)**: mucopolysaccharidosis type 4B (0.849); GM1 gangliosidosis type 1 (0.847); GM1 gangliosidosis type 3 (0.842); GM1 gangliosidosis type 2 (0.842); GM1 gangliosidosis (0.771)
- **Europe PMC papers**: 2663
- **Why important**: GLB1 is part of the clearest local biochemical neighborhood in the module: it connects to GNS and GNA11, and its interaction with GNS has strong STRING support while its interaction with ARSA is also supported. GLB1 is a lysosomal glycosidase involved in degradation of gangliosides and other glycoconjugates, and it has well-established associations with GM1 gangliosidosis and Morquio B syndrome.
- **Conclusion**: Established evidence supports GLB1 as a lysosomal glycoconjugate-degrading enzyme and supports a local functional relationship with GNS and ARSA. It is reasonable to regard this local neighborhood as biologically meaningful, but not to infer that lysosomal catabolism is globally enriched across the module.

#### ATP6V1C1

- **Related proteins** (co-abundance neighbors): UBA3 (0.83), CYFIP1 (0.81), BIN1 (0.81), PDCD6IP (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase H+ transporting V1 subunit C1. This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of intracellular compartments of eukaryotic cells. V-ATPase dependent acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 …
- **Diseases (Open Targets)**: neurodegenerative disease (0.565); Alzheimer disease (0.503); lysosomal storage disease (0.502); Parkinson disease (0.502); DOORS syndrome (0.344)
- **Europe PMC papers**: 711
- **Why important**: ATP6V1C1 links the network hub DPP9-related region to CYFIP1, BIN1, and PDCD6IP. As a V-ATPase component, it supports acidification of intracellular compartments, protein sorting, endocytosis, lysosomal function, and vesicle biology. Its disease associations include neurodegenerative and lysosomal-storage disorders, and HPA annotations include late spermatids and neutrophils.
- **Conclusion**: Established evidence supports ATP6V1C1 as part of the V-ATPase machinery required for intracellular compartment acidification. Its module position makes it a plausible bridge between vesicle turnover and lysosomal processing, but a direct role in the shared liver–stem-cell program remains unproven.

## Module 3

**Tissue pair**: liver and stem_cells  
**Genes (43)**: AASS, ABHD10, FDXR, ANXA7, CLTB, CPVL, D2HGDH, DLG1, ERMP1, ERO1A, FNTA, G6PD, GAR1, GCLC, GSTM3, HACD3, ICAM1, PPA2, IVD, AK1, MAT2B, MTM1, MVP, NDUFA10, NDUFS5, NIF3L1, PGM1, PLS1, PLS3, CTSA, RAB21, RBBP9, RPRD1B, RRAS2, RTN4, SAMHD1, SCFD1, SUN2, TIMM9, TRIM25, UAP1, WASHC4, ZFR

### Function

This module does not support one sharply defined pathway-level function: no GO or KEGG term passed global correction. The most coherent interpretation is a mixed cellular maintenance module linking mitochondrial metabolism, redox protection, carbohydrate and nucleotide handling, intracellular trafficking, cytoskeletal organization, and stress or immune-related regulation. The network is relatively fragmented rather than organized around one dense interaction core. D2HGDH is the most prominent network connector and links mitochondrial and metabolic genes with plastins, PPA2, IVD, AASS, and PGM1. A separate mitochondrial respiratory-chain pair is formed by NDUFS5 and NDUFA10, while PLS1 and PLS3 define an actin-associated branch. GCLC, GSTM3, ERO1A, and ERMP1 support a redox and protein-stress axis; UAP1, PGM1, and AK1 support carbohydrate, nucleotide, and glycosylation-related metabolism. These convergent annotations are biological interpretation of individual genes and network structure, not evidence of globally enriched GO or KEGG pathways. The absence of a globally enriched term does not invalidate the module.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only a small minority are annotated as secreted, and most proteins are intracellular. HPA shows broad expression for many genes, with many having low tissue specificity, while a smaller subset is enhanced in liver or other tissues. Protein detection in liver is common among the annotated genes, whereas there is no matching HPA tissue for stem cells. The module therefore plausibly reflects shared cellular programs present in liver and stem-cell samples rather than a highly tissue-exclusive liver program. There is also a possible cellular-composition contribution: several genes are enhanced in neutrophils, megakaryocytes, NK cells, monocytes, Kupffer cells, or other immune-related populations, and PLS3 is grouped with NK cells and plasmacytoid dendritic cells. However, most genes have low immune-cell specificity, so the evidence does not establish that the module is merely blood contamination. The broad housekeeping-like and metabolic character should be considered when interpreting the cross-tissue conservation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports only a few direct high-confidence relationships within the module: AK1 with PGM1, D2HGDH with MAT2B, NDUFA10 with NDUFS5, and PGM1 with UAP1. These links provide useful anchors for nucleotide, carbohydrate, methionine, and mitochondrial respiratory-chain biology, but the sparse STRING graph argues against describing the whole module as a single established protein complex. hu.MAP provides stronger structural support for several local submodules. PLS1 and PLS3 recur together in multiple complexes (hu.MAP huMAP3_05481.1), (hu.MAP huMAP3_03533.1), (hu.MAP huMAP3_07456.1), (hu.MAP huMAP3_10900.1), and (hu.MAP huMAP3_10281.1), supporting an actin-associated relationship. WASHC4 and CPVL recur together in (hu.MAP huMAP3_06652.1), (hu.MAP huMAP3_08077.1), (hu.MAP huMAP3_10870.1), and (hu.MAP huMAP3_12900.1), supporting an endosomal or trafficking branch. NDUFS5 and NDUFA10 recur together across (hu.MAP huMAP3_02819.1), (hu.MAP huMAP3_14018.1), (hu.MAP huMAP3_06397.1), (hu.MAP huMAP3_09982.1), (hu.MAP huMAP3_09567.1), and (hu.MAP huMAP3_14878.1), consistent with their known complex-I association. FDXR and PPA2 occur together in (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1), while AK1, PLS3, PLS1, UAP1, and PPA2 occur in (hu.MAP huMAP3_14442.1). These observations indicate that parts of the module recapitulate known complexes, whereas the co-abundance links connecting those parts are not generally established physical interactions.

**STRING interactions (score >= 0.7)**: 4 of 903 gene pairs: AK1–PGM1 (0.76); D2HGDH–MAT2B (0.756); NDUFA10–NDUFS5 (0.999); PGM1–UAP1 (0.735)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (AK1, PLS3, PLS1, UAP1, PPA2; 5/57); huMAP3_13468.1 (FDXR, IVD, D2HGDH, PPA2; 4/99); huMAP3_05481.1 (PLS3, PLS1; 2/3); huMAP3_03533.1 (PLS3, PLS1; 2/4); huMAP3_07456.1 (PLS3, PLS1; 2/5); huMAP3_10900.1 (PLS3, PLS1; 2/6); huMAP3_10281.1 (PLS3, PLS1; 2/9); huMAP3_06652.1 (WASHC4, CPVL; 2/14); huMAP3_08077.1 (WASHC4, CPVL; 2/16); huMAP3_10870.1 (WASHC4, CPVL; 2/20); huMAP3_10525.1 (FDXR, PPA2; 2/33); huMAP3_02819.1 (NDUFS5, NDUFA10; 2/34); huMAP3_14018.1 (NDUFS5, NDUFA10; 2/48); huMAP3_06397.1 (NDUFS5, NDUFA10; 2/49); huMAP3_09982.1 (NDUFS5, NDUFA10; 2/49); huMAP3_12900.1 (WASHC4, CPVL; 2/50); huMAP3_09567.1 (NDUFS5, NDUFA10; 2/52); huMAP3_14878.1 (NDUFS5, NDUFA10; 2/53)

### Novelty

This module should not be called a wholly new biological mechanism. Several of its local relationships are already supported by STRING or hu.MAP, and the functions of many genes are well established. The potentially novel result is the cross-tissue co-abundance organization that brings metabolic, mitochondrial, cytoskeletal, trafficking, and stress-related genes together in liver and stem-cell data. That claim remains provisional: the supplied evidence does not include a comparison with previously published co-abundance modules, independent cohorts, perturbation experiments, or direct validation in stem cells. Absence of a STRING or hu.MAP relationship is not evidence of novelty. The appropriate conclusion is that the module may represent a new dataset-level association pattern, but novelty at the mechanistic or biological level is unproven.

**Hypothesis.** Hypothesis: this conserved module reflects a shared cellular adaptation state in which mitochondrial energy and metabolite handling are coordinated with cytosolic carbohydrate and nucleotide metabolism, antioxidant protection, protein-folding stress responses, and membrane or cytoskeletal trafficking. D2HGDH, PPA2, NDUFS5, and NDUFA10 could represent the mitochondrial metabolic and respiratory component; GCLC and GSTM3 could buffer oxidative or electrophilic stress; PLS1, PLS3, WASHC4, and CPVL could couple that state to membrane remodeling and intracellular transport. This could arise from a shared hepatocyte-like or progenitor-like cell program, or from shared cell-type composition across the two tissue groups. It is a testable hypothesis, not a demonstrated causal pathway. Perturbation of the proposed metabolic or redox anchors followed by measurement of the cytoskeletal and trafficking genes would be needed to distinguish coordinated regulation from correlated cell composition.

### Important genes

#### D2HGDH

- **Related proteins** (co-abundance neighbors): GCLC (0.90), PLS3 (0.90), PPA2 (0.84), PLS1 (0.83), IVD (0.83), AASS (0.82), PGM1 (0.80); STRING partners: MAT2B (0.756)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: D-2-hydroxyglutarate dehydrogenase. This gene encodes D-2hydroxyglutarate dehydrogenase, a mitochondrial enzyme belonging to the FAD-binding oxidoreductase/transferase type 4 family. This enzyme, which is most active in liver and kidney but also active in heart and brain, converts D-2-hydroxyglutarate to 2-ketoglutarate. Mutations in this gene are present in D-2-hydroxyglutaric aciduria, a rare recessive neurometabolic disorder caus…
- **Diseases (Open Targets)**: D-2-hydroxyglutaric aciduria (0.837); asthma (0.574); atopic eczema (0.520); allergic disease (0.511); allergic rhinitis (0.499)
- **Europe PMC papers**: 509
- **Why important**: D2HGDH is the strongest network connector in the supplied ordering and links several metabolic and mitochondrial genes, including PPA2, IVD, AASS, PGM1, and MAT2B through the module structure or STRING. Its established function is mitochondrial conversion of D-2-hydroxyglutarate to two-oxoglutarate, with activity especially relevant to liver and kidney. It is associated with D-2-hydroxyglutaric aciduria and has substantial disease and literature support. Its placement makes it a useful candidate for connecting mitochondrial metabolite handling to the broader module, although its HPA profile is broadly expressed rather than stem-cell-specific.
- **Conclusion**: Established: D2HGDH is a mitochondrial metabolic enzyme and a prominent co-abundance connector. Hypothesis: it may help organize the module around mitochondrial metabolite and redox state. The network supports prioritizing it for testing, but does not establish that it causally regulates the other module genes.

#### NDUFS5

- **Related proteins** (co-abundance neighbors): SCFD1 (0.92), ERO1A (0.81); STRING partners: NDUFA10 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_02819.1, huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit S5. This gene is a member of the NADH dehydrogenase (ubiquinone) iron-sulfur protein family. The encoded protein is a subunit of the NADH:ubiquinone oxidoreductase (complex I), the first enzyme complex in the electron transport chain located in the inner mitochondrial membrane. Alternative splicing results in multiple transcript variants and pseudogenes have been identified on chromosomes 1, 4 and 17.…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.608); Parkinson disease (0.605); diabetes mellitus (0.578); neurodegenerative disease (0.576); Alzheimer disease (0.536)
- **Europe PMC papers**: 800
- **Why important**: NDUFS5 is a complex-I subunit and is paired with NDUFA10 by a very strong STRING relationship. The two genes recur together across many hu.MAP complex annotations (hu.MAP huMAP3_02819.1), (hu.MAP huMAP3_14018.1), (hu.MAP huMAP3_06397.1), (hu.MAP huMAP3_09982.1), (hu.MAP huMAP3_09567.1), and (hu.MAP huMAP3_14878.1), providing unusually consistent external support for a genuine mitochondrial respiratory-chain component. NDUFS5 has disease associations involving diabetes and neurodegenerative disease, while its HPA profile includes liver detection and enhancement in several epithelial and platelet-related cell types.
- **Conclusion**: Established: NDUFS5 participates in mitochondrial complex I and forms a supported local module with NDUFA10. Hypothesis: the pair marks respiratory capacity or mitochondrial demand shared by liver and stem-cell samples. It is a strong anchor for the mitochondrial branch, but not proof that respiration explains the entire module.

#### NDUFA10

- **Related proteins** (co-abundance neighbors): TIMM9 (0.82), DLG1 (0.81); STRING partners: NDUFS5 (0.999)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_02819.1, huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit A10. The protein encoded by this gene is a component of 42 kDa complex I, the first enzyme complex in the electron transport chain of mitochondria. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. A mutation in this gene was found in an individual with Leigh syndrome. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.677); Leigh syndrome (0.674); mitochondrial complex I deficiency, nuclear type 22 (0.668); type 2 diabetes mellitus (0.620); diabetes mellitus (0.578)
- **Europe PMC papers**: 1163
- **Why important**: NDUFA10 complements NDUFS5 as a complex-I component and is connected in the co-abundance graph to TIMM9 and DLG1. Its STRING relationship with NDUFS5 and repeated hu.MAP membership provide concordant evidence that this is an established respiratory-chain submodule rather than an isolated annotation. NDUFA10 has reported links to complex-I deficiency and Leigh syndrome, as well as metabolic disease, making it clinically informative despite its modest local connectivity.
- **Conclusion**: Established: NDUFA10 is a mitochondrial complex-I protein with disease relevance and strong external support for its relationship with NDUFS5. Hypothesis: coordinated abundance of this pair may report mitochondrial respiratory state in the shared module. Causality beyond that local pair remains untested.

#### GCLC

- **Related proteins** (co-abundance neighbors): D2HGDH (0.90), MTM1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamate-cysteine ligase catalytic subunit. Glutamate-cysteine ligase, also known as gamma-glutamylcysteine synthetase is the first rate-limiting enzyme of glutathione synthesis. The enzyme consists of two subunits, a heavy catalytic subunit and a light regulatory subunit. This locus encodes the catalytic subunit, while the regulatory subunit is derived from a different gene located on chromosome 1p22-p21. Mutations at this locus have been …
- **Diseases (Open Targets)**: gamma-glutamylcysteine synthetase deficiency (0.766); cystic fibrosis (0.375); neurodegenerative disease (0.373); non-autoimmune hemolytic anemia (0.370); lung adenocarcinoma (0.331)
- **Europe PMC papers**: 8941
- **Why important**: GCLC encodes the catalytic subunit of glutamate-cysteine ligase, the rate-limiting enzyme in glutathione synthesis. It is tissue-enhanced in liver, is connected to D2HGDH and MTM1, and has extensive functional, disease, and literature support, including links to oxidative stress and hemolytic anemia. Its position connects the metabolic portion of the module to a plausible redox-protection program.
- **Conclusion**: Established: GCLC is a major glutathione-biosynthesis enzyme with liver relevance and disease associations. Hypothesis: it may buffer oxidative stress associated with the mitochondrial and metabolic state represented by the module. The co-abundance pattern does not prove that glutathione synthesis is the primary driver.

#### PLS3

- **Related proteins** (co-abundance neighbors): D2HGDH (0.90), MVP (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_14442.1, huMAP3_05481.1, huMAP3_03533.1, huMAP3_07456.1, huMAP3_10900.1, huMAP3_10281.1
- **Function (MyGene.info)**: plastin 3. Plastins are a family of actin-binding proteins that are conserved throughout eukaryote evolution and expressed in most tissues of higher eukaryotes. In humans, two ubiquitous plastin isoforms (L and T) have been identified. Plastin 1 (otherwise known as Fimbrin) is a third distinct plastin isoform which is specifically expressed at high levels in the small intestine. The L isoform is expressed on…
- **Diseases (Open Targets)**: X-linked osteoporosis with fractures (0.727); congenital diaphragmatic hernia (0.553); osteoporosis (0.477); hernia, anterior diaphragmatic (0.380); postmenopausal osteoporosis (0.341)
- **Europe PMC papers**: 1365
- **Why important**: PLS3 encodes an actin-bundling protein and occupies the actin-associated branch with PLS1 and MVP. PLS3 and PLS1 recur together in several hu.MAP complexes (hu.MAP huMAP3_14442.1), (hu.MAP huMAP3_05481.1), (hu.MAP huMAP3_03533.1), (hu.MAP huMAP3_07456.1), (hu.MAP huMAP3_10900.1), and (hu.MAP huMAP3_10281.1), while PLS3 also connects to D2HGDH in the co-abundance graph. HPA supports expression in multiple epithelial cell types and groups it with NK-cell and plasmacytoid-dendritic-cell populations. Its disease associations include bone and fracture phenotypes, and its literature is substantial.
- **Conclusion**: Established: PLS3 is an actin-bundling protein and a reproducible member of several PLS1-containing complex annotations. Hypothesis: the PLS3 branch may link metabolic state to cell shape, adhesion, or epithelial and progenitor-cell architecture. The immune-cell HPA signal also means that cellular composition must be excluded before assigning this branch a cell-intrinsic role.

#### PGM1

- **Related proteins** (co-abundance neighbors): D2HGDH (0.80); STRING partners: AK1 (0.76), UAP1 (0.735)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglucomutase 1. The protein encoded by this gene is an isozyme of phosphoglucomutase (PGM) and belongs to the phosphohexose mutase family. There are several PGM isozymes, which are encoded by different genes and catalyze the transfer of phosphate between the 1 and 6 positions of glucose. In most cell types, this PGM isozyme is predominant, representing about 90% of total PGM activity. In red cells, PGM2 is a majo…
- **Diseases (Open Targets)**: PGM1-congenital disorder of glycosylation (0.843); MPDU1-congenital disorder of glycosylation (0.551); developmental and epileptic encephalopathy, 36 (0.551); RFT1-congenital disorder of glycosylation (0.551); disorder of glycogen metabolism (0.506)
- **Europe PMC papers**: 3203
- **Why important**: PGM1 provides a direct metabolic bridge between glucose, glycogen, and glycosylation-related biology. It is connected to D2HGDH in the module, has STRING support with AK1 and UAP1, and is part of a known carbohydrate-metabolism framework. HPA places it in hepatocytes and other metabolically active cell types, with group enrichment in skeletal muscle and tongue. Its congenital glycosylation and glycogen-metabolism associations, together with substantial literature, make it a useful functional anchor.
- **Conclusion**: Established: PGM1 controls an important step in glucose and glycogen metabolism and has supported links to AK1 and UAP1. Hypothesis: it may couple cellular energy balance to UDP-sugar production and the module's structural or trafficking branches. The available evidence supports prioritization, not a claim that PGM1 drives the shared module.

## Module 4

**Tissue pair**: liver and stem_cells  
**Genes (30)**: ABCF3, DCPH1, ATPAF2, BPHL, COPB1, DCXR, DIAPH1, DUSP23, FAHD1, GALNS, RAP1GDS1, GBE1, GSTT1, HMOX2, HSPA4L, EIF4E, IQGAP2, MYO1D, OPLAH, PAPSS2, PML, PPP6R3, SCPEP1, SCLY, SPR, DARS2, SYNE2, TBC1D17, TIMMDC1, WASHC5

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established single pathway interpretation from enrichment. Its gene content instead suggests a heterogeneous intracellular program combining liver-associated metabolism, redox and detoxification, mitochondrial function, vesicle and endosomal trafficking, cytoskeletal organization, signaling regulation, and protein or translation control. The network is relatively sparse and lacks a central biochemical pathway. DUSP23 is the most connected node and links metabolic genes such as GBE1, DCXR, BPHL and OPLAH with signaling or structural genes such as IQGAP2, SPR and ATPAF2. These features support a cautious interpretation as a coordinated cell-state or tissue-composition signal rather than a proven discrete molecular complex.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: nearly all genes have intracellular annotations, and only a small minority are secreted according to HPA. It is also not uniformly blood-cell enriched, because most genes have low immune-cell specificity. Nevertheless, HPA shows mixed cell-type signals, including hepatocytes, neutrophils, monocytes, myeloid dendritic cells, enterocytes and spermatid populations. Several genes are liver detected or liver enhanced, while others are enriched in skeletal muscle, kidney or testis. The shared liver and stem-cell signal could therefore reflect a combination of hepatocyte-associated metabolism, broadly expressed cellular programs, and shared or variable cell-type composition. HPA protein detection in liver supports that many module proteins are present in liver, but there is no matching HPA tissue for stem_cells, so the cross-tissue interpretation remains limited.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, EIF4E-PML, and reports no supplementary functional enrichment. This is a known relationship and supports a limited connection between translation initiation and PML nuclear-body biology, but it does not establish the entire module as a STRING-supported interaction network. hu.MAP identifies complex C1 containing the module members DARS2 and ATPAF2. Because the complex contains many additional proteins that are not in the module, this is partial membership rather than evidence that most module genes form one complex. The remaining module relationships are therefore primarily co-abundance edges, not independently confirmed physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 435 gene pairs: EIF4E–PML (0.854)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (DARS2, ATPAF2; 2/99)

### Novelty

The module may represent a new co-abundance pattern in this liver and stem-cell comparison, because it combines liver-associated metabolic genes, mitochondrial factors, trafficking and cytoskeletal regulators, and nuclear or translational regulators without a globally significant GO/KEGG signature or broad STRING support. However, novelty cannot be claimed as a newly discovered biological pathway. Known evidence already exists for EIF4E-PML and for the partial hu.MAP complex containing DARS2 and ATPAF2, and several individual genes have well-established functions and disease associations. Absence of most module edges from STRING or hu.MAP is evidence of limited prior interaction support, not proof that the co-abundance pattern itself is novel. Independent cohorts, cell-composition adjustment, perturbation experiments and protein-level validation would be needed to establish novelty.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in which liver-associated metabolic and detoxification activity is coordinated with mitochondrial maintenance, vesicle or endosomal trafficking, cytoskeletal remodeling and stress-responsive regulation. DUSP23 may act as a network-level bridge between metabolic genes and signaling or structural genes, while GBE1, BPHL, DCXR, GSTT1, HMOX2 and SCLY represent metabolic, redox or detoxification components. IQGAP2, MYO1D, WASHC5, TBC1D17 and DIAPH1 could connect this state to membrane trafficking and actin organization, whereas PML and EIF4E could reflect nuclear stress and translational control. An alternative explanation is that the module is produced by mixed hepatocyte, immune-cell and other cell-type contributions rather than by one mechanism operating within a single cell.

### Important genes

#### DUSP23

- **Related proteins** (co-abundance neighbors): GBE1 (0.89), DCXR (0.83), BPHL (0.82), OPLAH (0.81), ATPAF2 (0.80), IQGAP2 (0.80), SPR (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dual specificity phosphatase 23. Enables protein tyrosine/serine/threonine phosphatase activity. Involved in dephosphorylation. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: acute myeloid leukemia (0.321); neurodegenerative disease (0.266); placental retention (0.183); ovarian dysfunction (0.161); Decreased total leukocyte count (0.135)
- **Europe PMC papers**: 227
- **Why important**: DUSP23 has the broadest connectivity in the module and links several metabolic genes with IQGAP2, SPR and ATPAF2. Its established function is protein dephosphorylation, with annotations for dephosphorylation and cilium assembly. HPA shows liver detection and hepatocyte-associated cell-type enhancement. Its disease literature is more limited than that of major signaling phosphatases, but it has a substantial research record and plausible network relevance.
- **Conclusion**: Established evidence supports DUSP23 as the principal network connector and a phosphatase expressed in liver. It is reasonable to hypothesize that it helps coordinate signaling with the metabolic and structural components of the module, but the co-abundance data do not demonstrate that it regulates the neighboring genes.

#### GBE1

- **Related proteins** (co-abundance neighbors): DUSP23 (0.89), WASHC5 (0.84), RAP1GDS1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 1,4-alpha-glucan branching enzyme 1. The protein encoded by this gene is a glycogen branching enzyme that catalyzes the transfer of alpha-1,4-linked glucosyl units from the outer end of a glycogen chain to an alpha-1,6 position on the same or a neighboring glycogen chain. Branching of the chains is essential to increase the solubility of the glycogen molecule and, consequently, in reducing the osmotic pressure within cells. Highest l…
- **Diseases (Open Targets)**: glycogen storage disease due to glycogen branching enzyme deficiency (0.848); adult polyglucosan body disease (0.801); glycogen storage disease due to glycogen branching enzyme deficiency, adult neuromuscular form (0.711); glycogen storage disease due to glycogen branching enzyme deficiency, congenital neuromuscular form (0.591); disorder of glycogen metabolism (0.573)
- **Europe PMC papers**: 1361
- **Why important**: GBE1 connects DUSP23, WASHC5 and RAP1GDS1 and encodes the glycogen branching enzyme, a direct regulator of glycogen architecture and carbohydrate metabolism. It is liver and muscle associated, is detected in liver, and has well-established links to glycogen storage disease and adult polyglucosan body disease. Its function and disease literature are substantial.
- **Conclusion**: Established evidence makes GBE1 a strong metabolic anchor for the module and supports a liver-related glycogen or carbohydrate component. It does not establish that glycogen metabolism is the globally enriched module function, because no GO/KEGG term passed global correction.

#### IQGAP2

- **Related proteins** (co-abundance neighbors): SYNE2 (0.88), DUSP23 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Plasma membrane; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IQ motif containing GTPase activating protein 2. This gene encodes a member of the IQGAP family. The encoded protein contains three IQ domains, one calponin homology domain, one Ras-GAP domain and one WW domain. This protein interacts with components of the cytoskeleton, with cell adhesion molecules, and with several signaling molecules to regulate cell morphology and motility. It also acts as a tumor suppressor and has been found to play a role…
- **Diseases (Open Targets)**: prostate carcinoma (0.374); cholelithiasis (0.344); neurodegenerative disease (0.320); alcohol drinking (0.300); escherichia coli infection (0.269)
- **Europe PMC papers**: 1654
- **Why important**: IQGAP2 connects DUSP23 with SYNE2 and has annotations for signal transduction, actin-cytoskeleton regulation, cell morphology and motility. HPA reports liver tissue enhancement and signals in hematopoietic stem cells, neutrophil progenitors, neutrophils and other cell types. Its tumor-suppressor and innate antiviral associations give it meaningful disease and mechanistic literature.
- **Conclusion**: Established evidence supports IQGAP2 as a liver-associated signaling and cytoskeletal regulator that could connect metabolic state to cell architecture. Its position in this sparse network is compatible with that role, but a direct regulatory relationship with DUSP23 or SYNE2 remains a hypothesis.

#### HMOX2

- **Related proteins** (co-abundance neighbors): PPP6R3 (0.84), TBC1D17 (0.82), GALNS (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heme oxygenase 2. Heme oxygenase, an essential enzyme in heme catabolism, cleaves heme to form biliverdin, which is subsequently converted to bilirubin by biliverdin reductase, and carbon monoxide, a putative neurotransmitter. Heme oxygenase activity is induced by its substrate heme and by various nonheme substances. Heme oxygenase occurs as 2 isozymes, an inducible heme oxygenase-1 and a constitutive heme oxygenas…
- **Diseases (Open Targets)**: autoimmune disorder of central nervous system (0.229); migraine disorder (0.154); schizophrenia (0.140); skin cancer (0.134); cancer (0.085)
- **Europe PMC papers**: 2039
- **Why important**: HMOX2 connects PPP6R3, TBC1D17 and GALNS and encodes constitutive heme oxygenase, participating in heme catabolism, hypoxia response and oxidative-stress biology. It is detected in liver and has extensive literature concerning heme metabolism and stress responses. Its placement beside signaling, trafficking and lysosomal or metabolic genes makes it informative for interpreting the module as a stress-linked cellular state.
- **Conclusion**: Established evidence supports HMOX2 as a heme and oxidative-stress component of the module. A coordinated redox-stress mechanism is plausible, but the co-abundance pattern alone cannot distinguish intracellular stress from differences in cell composition.

#### SPR

- **Related proteins** (co-abundance neighbors): GALNS (0.90), MYO1D (0.86), HSPA4L (0.83), TBC1D17 (0.81), DUSP23 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Nucleoplasm, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sepiapterin reductase. This gene encodes an aldo-keto reductase that catalyzes the NADPH-dependent reduction of pteridine derivatives and is important in the biosynthesis of tetrahydrobiopterin (BH4). Mutations in this gene result in DOPA-responsive dystonia due to sepiaterin reductase deficiency. A pseudogene has been identified on chromosome 1. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: dopa-responsive dystonia due to sepiapterin reductase deficiency (0.830); dystonic disorder (0.550); hereditary disease (0.411); Intellectual disability (0.340); vaginal disorder (0.160)
- **Europe PMC papers**: 32938
- **Why important**: SPR is connected to GALNS, MYO1D, HSPA4L, TBC1D17 and DUSP23, making it one of the more connected bridge genes. It encodes sepiapterin reductase, an enzyme in tetrahydrobiopterin biosynthesis and nitric oxide biology. HPA shows cell-type enhancement in enterocytes and enrichment among several myeloid populations, and the gene has extensive literature and a well-established association with sepiapterin reductase deficiency and dopa-responsive dystonia.
- **Conclusion**: Established evidence supports SPR as a biologically important metabolic enzyme linking the network to redox and nitric-oxide-related metabolism. Its connection to trafficking and phosphatase genes suggests a possible broader state program, but that extension is a hypothesis rather than an established pathway.

## Module 5

**Tissue pair**: liver and stem_cells  
**Genes (5)**: ACAD10, AS3MT, CGN, SORBS2, TRIM23

### Function

No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The network instead combines several established biological themes: TRIM23 is associated with intracellular protein transport, vesicle-mediated transport, autophagy regulation, and protein ubiquitination; ACAD10 with mitochondrial fatty-acid beta-oxidation; CGN with cadherin binding, bicellular tight-junction assembly, epithelial morphogenesis, and microtubule organization; SORBS2 with cytoskeletal organization, Notch signaling, and cardiac muscle development; and AS3MT with arsenical metabolism and methylation. The compact co-abundance structure has TRIM23 as the central connectivity hub, with the other genes forming a mixed metabolic, epithelial-structural, and stress or detoxification signature. These annotations support a candidate coordinated cellular-state program rather than a single established pathway.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins: none of its genes is annotated as secreted. It is also not blood-cell enriched. HPA reports that most genes are not detected in immune cells or have low immune-cell specificity, and no enriched blood-cell types are listed. The genes are not uniformly housekeeping-like: several show tissue or cell-type enhancement, including intestine and epithelial cell types for CGN, heart muscle and cardiomyocytes for SORBS2, adrenal and neural cell types for AS3MT, and choroid plexus epithelial cells or myonuclei for ACAD10. Only TRIM23 has liver protein detection in the supplied HPA summary, while CGN and AS3MT are reported as not detected in liver and the remaining genes lack liver protein data. Thus, a blood-contamination explanation is not supported, but the module may reflect shared or mixed epithelial, metabolic, structural, or cell-state features rather than a liver-specific program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no supplied high-confidence STRING relationships or STRING functional-enrichment terms for this module. The only supplied complex evidence is huMAP complex (hu.MAP huMAP3_05977.1), which contains SORBS2 and CGN together with additional proteins outside the module. This supports a possible shared structural or junction-associated context for those two genes, but it does not establish a complete module-wide physical complex. The lack of STRING partners means that the co-abundance relationships are not corroborated by the supplied STRING network; they may represent co-regulation, tissue composition, indirect biology, or interactions below the selected confidence threshold.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05977.1 (SORBS2, CGN; 2/12)

### Novelty

The module may represent a new co-abundance association, because its genes form a locally connected pattern while lacking supplied STRING support and having only partial huMAP support. However, it should not be called a newly discovered molecular complex or pathway. The absence of STRING or huMAP evidence alone does not prove novelty, and the absence of globally significant GO or KEGG enrichment makes a strong claim of a newly defined biological function premature. The most defensible novelty claim is a potentially novel association linking TRIM23-centered connectivity with ACAD10, CGN, SORBS2, and AS3MT in the shared liver and stem-cell data context. Replication in independent cohorts and validation of expression, localization, and physical or regulatory relationships would be required.

**Hypothesis.** Hypothesis: the module may capture a coordinated cellular-state response in which TRIM23-related trafficking, ubiquitination, and autophagy processes are coupled indirectly to epithelial junction and cytoskeletal organization through CGN and SORBS2, while ACAD10 and AS3MT represent metabolic and detoxification adaptations. The shared liver and stem-cell signal could therefore reflect a common state involving cellular architecture, organelle or vesicle handling, lipid metabolism, and chemical-stress processing, rather than one canonical pathway. This is a hypothesis because the module lacks globally significant enrichment and direct STRING support.

### Important genes

#### TRIM23

- **Related proteins** (co-abundance neighbors): ACAD10 (0.88), CGN (0.86), SORBS2 (0.85), AS3MT (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tripartite motif containing 23. The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. This protein is also a member of the ADP ribosylation factor family of guanine nucleotide-binding family of proteins. Its carboxy terminus contains an ADP-ribosylation factor domain and a guanine…
- **Diseases (Open Targets)**: colorectal carcinoma (0.101); hepatocellular carcinoma (0.095); autism spectrum disorder (0.092); Abnormality of the skeletal system (0.084); catecholaminergic polymorphic ventricular tachycardia (0.082)
- **Europe PMC papers**: 561
- **Why important**: TRIM23 is the network hub, connecting every other module member in the supplied subgraph. Its established annotations include intracellular protein transport, vesicle-mediated transport, positive regulation of autophagy, and protein ubiquitination, providing the strongest candidate link between the module's diverse functional themes. It has liver protein detection and a substantial literature base, with disease associations including colorectal carcinoma, hepatocellular carcinoma, autism spectrum disorder, skeletal-system abnormality, and catecholaminergic polymorphic ventricular tachycardia.
- **Conclusion**: Established evidence supports TRIM23 as the central network-organizing candidate and as a regulator of trafficking, autophagy, and ubiquitin-related biology. It remains unestablished whether TRIM23 directly regulates the other module genes. Hypothesis: TRIM23 may coordinate a shared cellular-state response that produces the observed co-abundance pattern.

#### CGN

- **Related proteins** (co-abundance neighbors): TRIM23 (0.86), ACAD10 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05977.1
- **Function (MyGene.info)**: cingulin. Enables cadherin binding activity. Predicted to act upstream of or within bicellular tight junction assembly; epithelial cell morphogenesis; and microtubule cytoskeleton organization. Located in bicellular tight junction and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.359); nonsyndromic deafness (0.118); skin disorder (0.094); colorectal carcinoma (0.086); ovarian carcinoma (0.065)
- **Europe PMC papers**: 3593
- **Why important**: CGN is connected to TRIM23 and ACAD10 and is the only module member with direct huMAP complex support alongside SORBS2 in (hu.MAP huMAP3_05977.1). Its established functions involve cadherin binding, bicellular tight-junction assembly, epithelial morphogenesis, and microtubule organization. HPA places it at the plasma membrane and cell junctions and reports enhancement in intestinal and several epithelial cell types. CGN also has the largest literature footprint among the selected genes and disease associations including skeletal-system abnormality, nonsyndromic deafness, skin disorder, colorectal carcinoma, and ovarian carcinoma.
- **Conclusion**: Established evidence supports CGN as an epithelial junction and cytoskeletal component, and (hu.MAP huMAP3_05977.1) provides partial complex-level support with SORBS2. Its lack of liver protein detection argues against assuming that the module is a liver epithelial protein complex. Hypothesis: CGN may mark an epithelial-architecture component of the shared co-abundance state.

#### ACAD10

- **Related proteins** (co-abundance neighbors): TRIM23 (0.88), CGN (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA dehydrogenase family member 10. This gene encodes a member of the acyl-CoA dehydrogenase family of enzymes (ACADs), which participate in the beta-oxidation of fatty acids in mitochondria. The encoded enzyme contains a hydrolase domain at the N-terminal portion, a serine/threonine protein kinase catlytic domain in the central region, and a conserved ACAD domain at the C-terminus. Several alternatively spliced transcript variants …
- **Diseases (Open Targets)**: gout (0.258); Thrombocytopenia (0.239); coronary artery disorder (0.208); type 1 diabetes mellitus (0.190); chronic obstructive pulmonary disease (0.189)
- **Europe PMC papers**: 500
- **Why important**: ACAD10 connects TRIM23 and CGN, placing a mitochondrial fatty-acid oxidation enzyme within the central portion of the module rather than at an isolated edge. Its established annotations concern fatty-acid beta-oxidation and fatty-acid catabolism. HPA reports enhanced cell-type expression in choroid plexus epithelial cells and myonuclei, while Open Targets associations include gout, thrombocytopenia, coronary artery disorder, type one diabetes mellitus, and chronic obstructive pulmonary disease. It also has a substantial literature base.
- **Conclusion**: Established evidence supports ACAD10 as the module's metabolic component, but does not establish a direct physical or regulatory connection to CGN or TRIM23. Hypothesis: ACAD10 may reflect a metabolic adaptation coupled indirectly to trafficking, junctional organization, or cellular stress.

#### SORBS2

- **Related proteins** (co-abundance neighbors): TRIM23 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05977.1
- **Function (MyGene.info)**: sorbin and SH3 domain containing 2. Arg and c-Abl represent the mammalian members of the Abelson family of non-receptor protein-tyrosine kinases. They interact with the Arg/Abl binding proteins via the SH3 domains present in the carboxy end of the latter group of proteins. This gene encodes the sorbin and SH3 domain containing 2 protein. It has three C-terminal SH3 domains and an N-terminal sorbin homology (SoHo) domain that interac…
- **Diseases (Open Targets)**: neurodegenerative disease (0.481); mathematical ability (0.422); type 2 diabetes mellitus (0.412); Varicose veins (0.369); atrial fibrillation (0.367)
- **Europe PMC papers**: 1229
- **Why important**: SORBS2 is connected to the central TRIM23 hub and shares huMAP complex (hu.MAP huMAP3_05977.1) with CGN. Its established annotations include cytoskeleton organization, Notch signaling, and cell growth involved in cardiac muscle development. HPA reports enhancement in heart muscle and several specialized cell types, including cardiomyocytes. Its disease associations include neurodegenerative disease, type two diabetes mellitus, varicose veins, and atrial fibrillation, and it has a substantial literature base.
- **Conclusion**: Established evidence supports SORBS2 as a structural and signaling adaptor with a plausible relationship to CGN through (hu.MAP huMAP3_05977.1). The module data do not establish that its cardiac or neural associations are active in liver or stem cells. Hypothesis: SORBS2 may help connect cytoskeletal or junctional remodeling to the broader TRIM23-centered cellular state.

#### AS3MT

- **Related proteins** (co-abundance neighbors): TRIM23 (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: arsenite methyltransferase. AS3MT catalyzes the transfer of a methyl group from S-adenosyl-L-methionine (AdoMet) to trivalent arsenical and may play a role in arsenic metabolism (Lin et al., 2002 [PubMed 11790780]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: schizophrenia (0.378); alcohol drinking (0.277); smoking initiation (0.276); Abnormality of the skeletal system (0.270); intelligence (0.269)
- **Europe PMC papers**: 941
- **Why important**: AS3MT is connected to TRIM23 and is the only module member reported as tissue enriched in adrenal gland. Its established function is arsenite methyltransferase activity, including arsenical metabolism and methylation. HPA reports enhancement across several neural cell types and mitochondrial localization. Its disease and trait associations include schizophrenia, alcohol drinking, smoking initiation, skeletal-system abnormality, and intelligence, and it has a substantial literature base.
- **Conclusion**: Established evidence supports AS3MT as a detoxification and methylation gene with distinctive tissue and cell-type specificity. The supplied data do not establish a direct connection between arsenical metabolism and the other module functions. Hypothesis: AS3MT may represent a chemical-stress or mitochondrial-metabolic component of the shared co-abundance state rather than a member of a single physical complex.

## Module 6

**Tissue pair**: liver and stem_cells  
**Genes (12)**: ACSF3, CD2AP, CPT1A, CYBA, DSTN, ENPP1, GFPT1, LRBA, NSFL1C, PITPNB, RAPH1, USP5

### Function

No GO or KEGG term passed global correction, and STRING reported no functional enrichment. Therefore, the module does not support a statistically established pathway-level assignment from enrichment analysis. Its gene-level pattern instead points to a coordinated cellular program spanning actin remodeling and membrane dynamics (RAPH1, CD2AP, DSTN), vesicle and lipid handling (PITPNB, LRBA, ENPP1), carbohydrate and fatty-acid metabolism (GFPT1, CPT1A, ACSF3), and phagocyte-associated redox biology (CYBA). The central network position of RAPH1, together with the links connecting RAPH1 to metabolic genes and connecting GFPT1 to LRBA and CYBA, is consistent with a cross-compartment co-abundance program rather than a narrowly defined canonical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only ENPP1 is annotated as secreted, with unknown location, while the remaining genes are intracellular or membrane-associated. It is also not broadly characterized as an immune-cell module. Most genes have low immune-cell specificity, although CYBA is immune-cell enhanced and associated with eosinophils, while CD2AP is immune-cell enhanced and associated with plasmacytoid dendritic cells; ENPP1 is immune-cell enhanced and associated with NK cells. HPA also links CYBA to Kupffer cells and dendritic-cell contexts, and CD2AP to plasmacytoid dendritic cells. These observations leave open a contribution from resident or associated immune cells in liver samples, but they do not support a simple blood-contamination explanation. The remaining HPA profile is mixed, with many genes having low tissue specificity and several showing cell-type-enhanced patterns outside blood. Liver protein detection is reported for many members, whereas there is no matching HPA tissue for stem_cells, so the stem-cell interpretation cannot be directly validated by the supplied HPA tissue-protein data.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no STRING functional enrichment. Thus, the co-abundance edges should not be interpreted as established direct physical interactions or as a known STRING protein complex. hu.MAP provides one relevant complex observation: (hu.MAP huMAP3_09592.1) contains CYBA and CPT1A as the module members, alongside many other proteins. This is evidence that these two genes have a reported complex-level association in a large multisubunit context, but it does not establish that the entire module is one complex or that CYBA directly interacts with CPT1A. The absence of hu.MAP assignments for the other members means that their relationships in this module are presently co-abundance relationships rather than curated complex relationships.

**STRING interactions (score >= 0.7)**: 0 of 66 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09592.1 (CYBA, CPT1A; 2/95)

### Novelty

The module may represent a previously unrecognized co-abundance configuration because its genes form a cross-functional network with no matching high-confidence STRING pair and only a partial hu.MAP overlap through (hu.MAP huMAP3_09592.1). However, these database observations do not prove that the biology is new: individual functions and disease associations are already well established, and database coverage, tissue context, cell mixture, and the distinction between co-abundance and physical interaction all limit novelty claims. The defensible conclusion is that the liver–stem-cell shared module is a potentially novel integrative co-abundance signature, not a demonstration of a newly discovered molecular complex or pathway.

**Hypothesis.** Hypothesis: the module reflects coordinated adaptation of membrane trafficking, cytoskeletal remodeling, lipid and carbohydrate metabolism, and redox or immune-related activity in cells represented across liver and stem-cell samples. RAPH1 and CD2AP may organize actin-linked membrane behavior, PITPNB and LRBA may support membrane or vesicle traffic, GFPT1, CPT1A, and ACSF3 may couple nutrient and lipid metabolism to cellular state, and CYBA may mark a phagocyte-like or oxidative-response component. ENPP1 could connect membrane-associated extracellular nucleotide or phosphodiester processing with metabolic and tissue-state signals. This is a mechanistic model derived from gene annotations and the co-abundance structure; it is not established by GO/KEGG enrichment, STRING interactions, or the partial hu.MAP result.

### Important genes

#### RAPH1

- **Related proteins** (co-abundance neighbors): GFPT1 (0.91), PITPNB (0.84), USP5 (0.82), CPT1A (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nuclear bodies, Plasma membrane; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Ras association (RalGDS/AF-6) and pleckstrin homology domains 1. This gene encodes a protein that belongs to the Mig10/Rap1-interacting adaptor molecule/Lamellipodin family of adapter proteins, which function in cell migration. Members of this family contain pleckstrin-homology domains, Ras-association domains, and proline-rich C-termini. The protein encoded by this gene regulates actin dynamics through interaction with Ena/Vasodilator proteins as well as direc…
- **Diseases (Open Targets)**: neurodegenerative disease (0.524); coronary artery disorder (0.469); bone Paget disease (0.316); osteoarthritis (0.283); coronary atherosclerosis (0.279)
- **Europe PMC papers**: 370
- **Why important**: RAPH1 is the most connected node in the supplied module and links actin-regulatory biology to GFPT1, PITPNB, USP5, and CPT1A. Its annotated role in actin-network assembly, cell migration, and membrane-associated signaling makes it a plausible organizing gene for the module's cytoskeletal and trafficking features. It has substantial literature coverage and disease associations spanning neurodegenerative, vascular, and skeletal conditions. HPA shows liver tissue enhancement and liver protein detection.
- **Conclusion**: Established: RAPH1 is a highly connected actin and membrane-associated adaptor with liver-enhanced HPA evidence. Hypothesis: it may coordinate the module's cytoskeletal state with metabolic and membrane processes, but the co-abundance data do not establish that it regulates the other module genes.

#### GFPT1

- **Related proteins** (co-abundance neighbors): RAPH1 (0.91), LRBA (0.86), CYBA (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamine--fructose-6-phosphate transaminase 1. This gene encodes the first and rate-limiting enzyme of the hexosamine pathway and controls the flux of glucose into the hexosamine pathway. The product of this gene catalyzes the formation of glucosamine 6-phosphate. [provided by RefSeq, Sep 2008].
- **Diseases (Open Targets)**: congenital myasthenic syndrome (0.819); neurodegenerative disease (0.559); congenital myasthenic syndromes with glycosylation defect (0.503); spinal stenosis (0.379); congenital disorder of glycosylation type I (0.370)
- **Europe PMC papers**: 1684
- **Why important**: GFPT1 is a network bridge connecting RAPH1, LRBA, and CYBA. It encodes the rate-limiting enzyme of the hexosamine pathway, placing it at a plausible interface between nutrient flux, protein glycosylation-related metabolism, and cellular stress or immune-associated states. It has extensive literature coverage and well documented associations with congenital myasthenic and glycosylation disorders.
- **Conclusion**: Established: GFPT1 has a defined metabolic function and occupies a bridging position in the module. Hypothesis: its co-abundance may report metabolic-state coupling to vesicle or immune-associated programs, but no enriched term or physical interaction confirms that interpretation.

#### CYBA

- **Related proteins** (co-abundance neighbors): DSTN (0.85), ACSF3 (0.83), GFPT1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: cytochrome b-245 alpha chain. Cytochrome b is comprised of a light chain (alpha) and a heavy chain (beta). This gene encodes the light, alpha subunit which has been proposed as a primary component of the microbicidal oxidase system of phagocytes. Mutations in this gene are associated with autosomal recessive chronic granulomatous disease (CGD), that is characterized by the failure of activated phagocytes to generate superoxide…
- **Diseases (Open Targets)**: chronic granulomatous disease (0.735); autoimmune polyendocrine syndrome type 1 (0.340); nerve plexus disorder (0.239); hereditary disease (0.191); oral cavity squamous cell carcinoma (0.095)
- **Europe PMC papers**: 5638
- **Why important**: CYBA is connected to GFPT1, DSTN, and ACSF3 and is the module member with the clearest immune and phagocyte context. It encodes the alpha component of the phagocyte microbicidal oxidase system, and its loss is associated with chronic granulomatous disease. HPA supports enhancement in bone marrow and lymphoid tissue and links it to dendritic, Kupffer, and eosinophil-related contexts. It also participates in the hu.MAP observation (hu.MAP huMAP3_09592.1) with CPT1A.
- **Conclusion**: Established: CYBA is a redox and phagocyte-associated gene with strong disease and tissue-context evidence. Hypothesis: CYBA may indicate a resident immune or oxidative component of the liver-shared module, rather than being a universal driver of the entire network.

#### CPT1A

- **Related proteins** (co-abundance neighbors): RAPH1 (0.81), ENPP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: carnitine palmitoyltransferase 1A. The mitochondrial oxidation of long-chain fatty acids is initiated by the sequential action of carnitine palmitoyltransferase I (which is located in the outer membrane and is detergent-labile) and carnitine palmitoyltransferase II (which is located in the inner membrane and is detergent-stable), together with a carnitine-acylcarnitine translocase. CPT I is the key enzyme in the carnitine-dependent…
- **Diseases (Open Targets)**: carnitine palmitoyl transferase 1A deficiency (0.833); hereditary disease (0.489); hypertensive disorder (0.350); response to xenobiotic stimulus (0.350); aortic stenosis (0.215)
- **Europe PMC papers**: 11255
- **Why important**: CPT1A connects RAPH1 with ENPP1 and is the module's clearest fatty-acid oxidation gene. It controls the carnitine-dependent entry of long-chain fatty acids into mitochondrial oxidation and has extensive literature coverage, including a defined CPT1A deficiency phenotype. HPA detects the protein in liver, and CPT1A is one of the two module members represented in hu.MAP complex (hu.MAP huMAP3_09592.1).
- **Conclusion**: Established: CPT1A is a liver-relevant mitochondrial fatty-acid oxidation enzyme with strong disease and complex-level support. Hypothesis: its co-abundance with RAPH1 and ENPP1 may reflect coupling between lipid oxidation and membrane or extracellular nucleotide biology, but the module does not establish that coupling mechanistically.

#### CD2AP

- **Related proteins** (co-abundance neighbors): LRBA (0.89), NSFL1C (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD2 associated protein. This gene encodes a scaffolding molecule that regulates the actin cytoskeleton. The protein directly interacts with filamentous actin and a variety of cell membrane proteins through multiple actin binding sites, SH3 domains, and a proline-rich region containing binding sites for SH3 domains. The cytoplasmic protein localizes to membrane ruffles, lipid rafts, and the leading edges of cells. It is i…
- **Diseases (Open Targets)**: familial idiopathic steroid-resistant nephrotic syndrome (0.701); focal segmental glomerulosclerosis (0.585); Alzheimer disease (0.493); dementia (0.395); Abnormality of the skeletal system (0.314)
- **Europe PMC papers**: 3461
- **Why important**: CD2AP is a membrane and actin scaffold connected to LRBA and NSFL1C. Its annotated functions include actin organization, membrane trafficking, cell migration, and regulation of protein secretion. HPA associates it with enterocytes and plasmacytoid dendritic cells and detects the protein in liver. Its disease associations include steroid-resistant nephrotic syndrome, focal segmental glomerulosclerosis, and neurodegenerative disease, with substantial literature coverage.
- **Conclusion**: Established: CD2AP is a trafficking and cytoskeletal scaffold with liver detection and relevant immune-cell context. Hypothesis: it may connect membrane remodeling to vesicle turnover within the module, while its co-abundance with the other genes does not prove a shared physical scaffold.

#### ENPP1

- **Related proteins** (co-abundance neighbors): CPT1A (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ectonucleotide pyrophosphatase/phosphodiesterase 1. This gene is a member of the ecto-nucleotide pyrophosphatase/phosphodiesterase (ENPP) family. The encoded protein is a type II transmembrane glycoprotein comprising two identical disulfide-bonded subunits. This protein has broad specificity and cleaves a variety of substrates, including phosphodiester bonds of nucleotides and nucleotide sugars and pyrophosphate bonds of nucleotides and nucleotide …
- **Diseases (Open Targets)**: arterial calcification, generalized, of infancy, 1 (0.846); arterial calcification of infancy (0.828); hypopigmentation-punctate palmoplantar keratoderma syndrome (0.806); hypophosphatemic rickets, autosomal recessive, 2 (0.765); type 2 diabetes mellitus (0.655)
- **Europe PMC papers**: 3416
- **Why important**: ENPP1 forms the link from CPT1A to the module's only annotated secreted protein. It is a membrane-associated ecto-enzyme with broad nucleotide and nucleotide-sugar phosphodiesterase activity, and HPA shows enhancement in placenta and hepatocyte-related cell types, liver protein detection, and association with NK cells. It has substantial literature coverage and strong disease associations involving arterial calcification, rickets, hypopigmentation syndromes, and type two diabetes.
- **Conclusion**: Established: ENPP1 provides extracellular or membrane-associated nucleotide-processing biology and is relevant to liver and metabolic disease contexts. Hypothesis: it may connect cellular energy or lipid state to extracellular signaling in the shared module, but the available evidence does not show that ENPP1 is secreted in this sample context or that it drives the module.

## Module 7

**Tissue pair**: liver and stem_cells  
**Genes (12)**: ADK, APMAP, CANX, CPD, MT-CO1, FAM3C, FBXO2, GALNT2, GBA1, GYG1, PACSIN3, HM13

### Function

The module does not support a single statistically established GO or KEGG function: no GO/KEGG term passed global correction, so there are no globally significant GO/KEGG terms to interpret. Its gene-level annotations instead suggest a mixed cellular program involving glycogen initiation and metabolism through GYG1, lysosomal glycolipid processing through GBA1, peptide and protein processing through CPD and GALNT2, endoplasmic-reticulum quality control and proteolysis through CANX, HM13 and FBXO2, membrane trafficking through PACSIN3, and purine salvage through ADK. The co-abundance structure links these processes weakly across membrane, vesicular, secretory, lysosomal, mitochondrial and cytosolic compartments rather than defining a validated canonical pathway. The only supplementary functional signal is the STRING lectin keyword association involving CANX, FBXO2 and GALNT2 (STRING Keyword Lectin; within-query FDR = 0.012); this is not global enrichment evidence.

**Cell composition.** This is not predominantly a plasma or secreted-protein module. FAM3C is secreted in other tissues, while GBA1 and GALNT2 have intracellular or membrane-associated localization; the remaining genes are not described as secreted. The HPA profile is mixed: most genes have low tissue specificity, with additional tissue-enhanced or group-enriched patterns in liver, muscle, tongue and brain. Several genes show cell-type enhancement in hepatocytes, neutrophils or epithelial populations, but blood-cell specificity is generally low. Liver protein detection is broad across the module, whereas there is no matching HPA tissue for stem_cells. Therefore, shared abundance may partly reflect liver-associated expression or shared cellular composition, but the evidence does not indicate a predominantly blood-derived module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The module has no high-confidence STRING pairwise interactions and no hu.MAP complex containing multiple module members. The observed co-abundance edges are therefore not corroborated by the supplied physical-interaction resources. The supplementary lectin keyword signal connects CANX, FBXO2 and GALNT2 (STRING Keyword Lectin; within-query FDR = 0.012), but it does not establish direct binding or a complex. Together, these results favor co-regulation, shared compartmental or cellular origin, or indirect metabolic coupling over a known stable protein complex.

**STRING interactions (score >= 0.7)**: 0 of 66 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Lectin (FDR = 0.012, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared liver-stem_cells co-abundance pattern may be a novel systems-level association because it is not represented by high-confidence STRING interactions or a multi-member hu.MAP complex. However, absence from those resources does not prove a new biological mechanism: the module may reflect coordinated expression, cell-type mixture, tissue sampling, or incomplete interaction coverage. The strongest defensible conclusion is that this is a potentially novel co-abundance module requiring replication and perturbation-based validation, rather than an established new pathway.

**Hypothesis.** Hypothesis: the module represents coordinated activity of liver-associated metabolic and protein-processing cells, in which glycogen and nucleotide metabolism are coupled to glycoprotein maturation, ER quality control, lysosomal lipid handling and membrane trafficking. A shared cellular-state program or common abundance of hepatocyte-related material could generate the cross-tissue co-abundance pattern without requiring direct physical interaction among the encoded proteins. This hypothesis predicts that the module will track cellular composition and secretory or metabolic load more strongly than it will track a single stable multiprotein complex.

### Important genes

#### APMAP

- **Related proteins** (co-abundance neighbors): GYG1 (0.89), GBA1 (0.88), CPD (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adipocyte plasma membrane associated protein. Enables arylesterase activity. Predicted to be involved in biosynthetic process. Located in cell surface and membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: smoking initiation (0.243); obesity disorder (0.196); Alzheimer disease (0.078); infection (0.077); cervical carcinoma (0.076)
- **Europe PMC papers**: 444
- **Why important**: APMAP is among the most connected nodes in the module and links GYG1, GBA1 and CPD, making it a central bridge between glycogen-related, lysosomal and processing-associated signals. HPA describes liver tissue enhancement and hepatocyte-related cell-type enhancement. Its annotated arylesterase activity and plasma-membrane localization provide a plausible interface between metabolism and the cell surface. Its literature volume is substantial, although less disease-defining than that of some other module genes.
- **Conclusion**: Established evidence supports APMAP as a liver-associated, membrane-localized hub with arylesterase activity and broad disease associations. Its bridging position is consistent with a coordinating role, but the module does not establish that APMAP mechanistically controls the other genes.

#### GYG1

- **Related proteins** (co-abundance neighbors): APMAP (0.89), CPD (0.83), HM13 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycogenin 1. This gene encodes a member of the glycogenin family. Glycogenin is a glycosyltransferase that catalyzes the formation of a short glucose polymer from uridine diphosphate glucose in an autoglucosylation reaction. This reaction is followed by elongation and branching of the polymer, catalyzed by glycogen synthase and branching enzyme, to form glycogen. This gene is expressed in muscle and other tiss…
- **Diseases (Open Targets)**: polyglucosan body myopathy type 2 (0.785); glycogen storage disease XV (0.774); disorder of glycogen metabolism (0.549); polyglucosan body myopathy (0.471); neurodegenerative disease (0.370)
- **Europe PMC papers**: 526
- **Why important**: GYG1 is among the most connected nodes and links APMAP, CPD and HM13. It encodes glycogenin, which initiates glycogen polymer formation, and is associated with glycogen storage disease and polyglucosan body myopathy. HPA shows tissue enhancement in skeletal muscle and tongue and liver protein detection, making it a strong candidate for the metabolic component of the module.
- **Conclusion**: Established evidence identifies GYG1 as a glycogen-initiation enzyme with disease relevance. Its module position supports a role in a metabolic subprogram, but it does not demonstrate that the entire module is a glycogen pathway.

#### CPD

- **Related proteins** (co-abundance neighbors): GALNT2 (0.83), GYG1 (0.83), APMAP (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enhanced; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carboxypeptidase D. The metallocarboxypeptidase family of enzymes is divided into 2 subfamilies based on sequence similarities. The pancreatic carboxypeptidase-like and the regulatory B-type carboxypeptidase subfamilies. Carboxypeptidase D has been identified as a regulatory B-type carboxypeptidase. CPD is a homolog of duck gp180, a hepatitis B virus-binding protein. Transcript variants utilizing alternative polyaden…
- **Diseases (Open Targets)**: neurodegenerative disease (0.348); autoimmune disorder of central nervous system (0.274); mental disorder (0.270); estrogen-receptor positive breast cancer (0.257); Graves disease (0.213)
- **Europe PMC papers**: 13682
- **Why important**: CPD is among the most connected nodes and links GALNT2, GYG1 and APMAP. It is a regulatory B-type carboxypeptidase involved in proteolysis, peptide metabolism and protein processing, and it has extensive literature support. HPA associates it with neutrophils and detects it in liver, so it may also report cellular composition or inflammatory-cell contribution.
- **Conclusion**: Established evidence supports CPD as a protein-processing enzyme with liver detection and neutrophil-associated expression. Its hub position makes it important for interpreting the module as a processing-related network, while the co-abundance data alone cannot distinguish functional coordination from shared cell-type abundance.

#### GBA1

- **Related proteins** (co-abundance neighbors): APMAP (0.88), FAM3C (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glucosylceramidase beta 1. This gene encodes a lysosomal membrane protein that cleaves the beta-glucosidic linkage of glycosylceramide, an intermediate in glycolipid metabolism. Mutations in this gene cause Gaucher disease, a lysosomal storage disease characterized by an accumulation of glucocerebrosides. A related pseudogene is approximately 12 kb downstream of this gene on chromosome 1. Alternative splicing results in mul…
- **Diseases (Open Targets)**: Gaucher disease (0.815); Gaucher disease type I (0.814); Gaucher disease type II (0.806); Gaucher disease type III (0.798); Gaucher disease perinatal lethal (0.774)
- **Europe PMC papers**: 2888
- **Why important**: GBA1 connects APMAP with FAM3C and contributes a lysosomal and sphingolipid-metabolism interpretation. It encodes glucosylceramidase beta and is strongly associated with Gaucher disease and related lysosomal storage disorders. HPA reports intracellular and membrane-associated localization, cell-type enhancement in several epithelial and renal populations, and liver protein detection.
- **Conclusion**: Established evidence supports GBA1 as a lysosomal glycolipid-processing enzyme with major disease relevance. Its position suggests a lipid-handling branch of the module, but there is no evidence that the module constitutes a Gaucher-disease mechanism.

#### HM13

- **Related proteins** (co-abundance neighbors): FBXO2 (0.91), GYG1 (0.81), MT-CO1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: histocompatibility minor 13. The protein encoded by this gene, which localizes to the endoplasmic reticulum, catalyzes intramembrane proteolysis of some signal peptides after they have been cleaved from a preprotein. This activity is required to generate signal sequence-derived human lymphocyte antigen-E epitopes that are recognized by the immune system, and to process hepatitis C virus core protein. The encoded protein is an…
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.097); neoplasm (0.094); breast cancer (0.078); breast carcinoma (0.077); eye disorder (0.077)
- **Europe PMC papers**: 460
- **Why important**: HM13 is among the most connected nodes and links FBXO2, GYG1 and MT-CO1 in the supplied network. It is an ER intramembrane protease involved in signal-peptide processing, antigen-epitope generation and protein maturation. Its placement beside FBXO2 and the supplementary lectin signal (STRING Keyword Lectin; within-query FDR = 0.012) is consistent with an ER and glycoprotein-quality-control component.
- **Conclusion**: Established evidence supports HM13 as an ER protease involved in membrane-protein processing and immune-relevant peptide generation. Its network position supports an ER-processing interpretation, but direct cooperation with the other module genes remains hypothetical because STRING and hu.MAP provide no corroborating relationship.

#### GALNT2

- **Related proteins** (co-abundance neighbors): CPD (0.83), PACSIN3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypeptide N-acetylgalactosaminyltransferase 2. This gene encodes a member of the glycosyltransferase 2 protein family. Members of this family initiate mucin-type O-glycoslation of peptides in the Golgi apparatus. The encoded protein may be involved in O-linked glycosylation of the immunoglobulin A1 hinge region. This gene may influence triglyceride levels, and may be involved Type 2 diabetes, as well as several types of cancer. Alternative spl…
- **Diseases (Open Targets)**: congenital disorder of glycosylation, type iit (0.777); metabolic syndrome (0.546); familial lipoprotein lipase deficiency (0.486); alcohol drinking (0.450); familial hyperlipidemia (0.444)
- **Europe PMC papers**: 1178
- **Why important**: GALNT2 connects CPD and PACSIN3 and is one of the genes in the supplementary STRING lectin keyword signal (STRING Keyword Lectin; within-query FDR = 0.012). It initiates mucin-type O-linked glycosylation in the Golgi and has associations with glycosylation disorders, metabolic syndrome and lipid-related disease. Its Golgi localization makes it a useful marker of secretory-pathway processing within the module.
- **Conclusion**: Established evidence supports GALNT2 as a Golgi glycosyltransferase with metabolic and glycosylation-related disease associations. Its module position and (STRING Keyword Lectin; within-query FDR = 0.012) annotation support a glycoprotein-processing component, but do not establish a direct complex or a unified lectin pathway.

## Module 8

**Tissue pair**: liver and stem_cells  
**Genes (10)**: ALDH2, CAT, DHRS1, SORD, ETFDH, SHMT1, PKLR, ALDH6A1, PTGR1, TUBA4A

### Function

The strongest supported function is cellular oxidoreductase activity, supported by the globally corrected term (GO:MF oxidoreductase activity; q_global = 0.043), which covers ALDH2, ALDH6A1, CAT, DHRS1, ETFDH, PTGR1, and SORD. The supplementary STRING result (STRING Keyword Oxidoreductase; within-query FDR = 0.0038) independently points to the same oxidoreductase theme. The individual annotations refine this into mitochondrial electron transfer and fatty-acid oxidation through ETFDH, aldehyde detoxification through ALDH2, peroxide defense through CAT, branched-chain amino-acid and pyrimidine catabolism through ALDH6A1, polyol metabolism through SORD, and lipid mediator inactivation through PTGR1. SHMT1 and PKLR provide links to one-carbon metabolism and glycolytic energy production, while TUBA4A may reflect cytoskeletal or cellular-state context. Thus, the module is best interpreted as a liver-associated metabolic redox and detoxification program rather than as a single linear pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. Its composition is also not primarily immune-cell specific, although several genes show immune-cell enhancement or enrichment, including ALDH2, ALDH6A1, PTGR1, CAT, and SORD in selected blood-cell categories. The dominant pattern is tissue-associated metabolism: liver enrichment is frequent, and hepatocyte enrichment is prominent, with additional kidney and proximal-tubule associations. Protein detection in liver is widespread across the module, whereas there is no matching HPA tissue for stem_cells. This makes a liver-like metabolic or shared cell-state signal more plausible than a blood-contamination explanation, while the blood-cell annotations remain a possible contributor that should be checked against sample composition.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF oxidoreductase activity | 0.043 | ALDH2, ALDH6A1, CAT, DHRS1, ETFDH, PTGR1, SORD |

### STRING and hu.MAP

The direct STRING evidence is limited but specific: the ALDH2–ALDH6A1 relationship is high-confidence and is concordant with both hu.MAP complexes (hu.MAP huMAP3_06207.1) and (hu.MAP huMAP3_13307.1). These complexes provide established support for a physical or functional aldehyde-dehydrogenase association, with ALDH8A1 additionally represented in (hu.MAP huMAP3_13307.1) outside the module. The remaining co-abundance edges do not have corresponding high-confidence STRING partners or hu.MAP complex assignments in the fact sheet. Therefore, the module contains a validated aldehyde-dehydrogenase core embedded in a broader co-abundance neighborhood, but the broader network should not be treated as an established physical complex. Co-abundance may instead reflect shared tissue expression, metabolic state, compartmental coordination, or indirect regulation.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: ALDH2–ALDH6A1 (0.961)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Oxidoreductase (FDR = 0.0038, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06207.1 (ALDH2, ALDH6A1; 2/2); huMAP3_13307.1 (ALDH2, ALDH6A1; 2/3)

### Novelty

The module should not be described as a completely new biochemical discovery. Its central functions are established, and the ALDH2–ALDH6A1 relationship is already supported by STRING and hu.MAP. However, the liver–stem_cells co-abundance configuration and the coordinated association of mitochondrial redox, aldehyde, peroxide, polyol, lipid-mediator, glycolytic, and one-carbon metabolism may represent a potentially novel systems-level observation. The absence of most module edges from STRING or hu.MAP does not prove novelty, because those resources emphasize curated or experimentally supported interactions rather than every tissue-dependent co-abundance relationship. Novelty would require validation in independent cohorts, control for cell composition, and comparison with existing liver and stem-cell coexpression modules.

**Hypothesis.** Hypothesis: the module represents a shared metabolic adaptation in which liver-like or metabolically active cells coordinate mitochondrial electron transfer, aldehyde clearance, peroxide detoxification, and carbon metabolism. ETFDH may connect respiratory electron transfer and fatty-acid oxidation to the aldehyde-dehydrogenase and antioxidant components, while ALDH2 and ALDH6A1 may handle complementary aldehyde or semialdehyde substrates. CAT could buffer hydrogen peroxide generated during oxidative metabolism, and PTGR1 and SORD could connect redox balance to lipid-mediator and carbohydrate metabolism. In stem_cells, the same co-abundance pattern may reflect a shared metabolic state or a hepatocyte-like contaminating or differentiated population rather than a stem-cell-specific pathway. This mechanism is a testable interpretation, not an established causal model.

### Important genes

#### ETFDH

- **Related proteins** (co-abundance neighbors): SHMT1 (0.88), TUBA4A (0.87), ALDH2 (0.85), PTGR1 (0.83), SORD (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein dehydrogenase. This gene encodes a component of the electron-transfer system in mitochondria and is essential for electron transfer from a number of mitochondrial flavin-containing dehydrogenases to the main respiratory chain. Mutations in this gene are associated with glutaric acidemia. Alternatively spliced transcript variants that encode distinct isoforms have been observed. [provided by RefSeq, Aug 2013].
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.845); glutaric acidemia IIc (0.704); glutaric aciduria (0.670); hereditary disease (0.523); Abnormality of metabolism/homeostasis (0.407)
- **Europe PMC papers**: 1273
- **Why important**: ETFDH has the strongest network position in the module and connects SHMT1, TUBA4A, ALDH2, PTGR1, and SORD. It is also part of the primary oxidoreductase evidence (GO:MF oxidoreductase activity; q_global = 0.043) and supplementary STRING evidence (STRING Keyword Oxidoreductase; within-query FDR = 0.0038). Its established mitochondrial role in electron transfer from flavin-containing dehydrogenases to the respiratory chain, together with fatty-acid oxidation and oxidative-stress annotations, makes it a plausible metabolic hub. Its association with multiple acyl-CoA dehydrogenase deficiency and glutaric acidemia further establishes clinical relevance, and its literature base is substantial.
- **Conclusion**: Established evidence supports ETFDH as a mitochondrial redox and respiratory-metabolism component with a central position in this co-abundance neighborhood. It is a strong candidate for coordinating the module, but a direct causal role in the shared liver–stem_cells pattern remains a hypothesis.

#### ALDH2

- **Related proteins** (co-abundance neighbors): ETFDH (0.85), CAT (0.82); STRING partners: ALDH6A1 (0.961)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06207.1, huMAP3_13307.1
- **Function (MyGene.info)**: aldehyde dehydrogenase 2 family member. This protein belongs to the aldehyde dehydrogenase family of proteins. Aldehyde dehydrogenase is the second enzyme of the major oxidative pathway of alcohol metabolism. Two major liver isoforms of aldehyde dehydrogenase, cytosolic and mitochondrial, can be distinguished by their electrophoretic mobilities, kinetic properties, and subcellular localizations. Most Caucasians have two major isozymes, …
- **Diseases (Open Targets)**: alcohol dependence (0.654); alcohol drinking (0.549); AMED syndrome, digenic (0.503); gout (0.501); atrial fibrillation (0.469)
- **Europe PMC papers**: 7978
- **Why important**: ALDH2 is one of the two genes supported by the high-confidence STRING relationship and both hu.MAP complexes (hu.MAP huMAP3_06207.1) and (hu.MAP huMAP3_13307.1). It belongs to the primary oxidoreductase term (GO:MF oxidoreductase activity; q_global = 0.043) and the supplementary STRING term (STRING Keyword Oxidoreductase; within-query FDR = 0.0038), is liver-enhanced and hepatocyte-enhanced, and has well-established roles in aldehyde catabolism, ethanol metabolism, and cellular detoxification. Its strong disease and trait evidence, including alcohol-related associations, makes it one of the most biologically interpretable genes in the module.
- **Conclusion**: Established evidence identifies ALDH2 as a liver-associated aldehyde-detoxification enzyme and part of a supported ALDH2–ALDH6A1 complex relationship. Its position in the module is consistent with a detoxification core, but the module data do not establish that ALDH2 drives the co-abundance pattern.

#### ALDH6A1

- **Related proteins** (co-abundance neighbors): PKLR (0.85); STRING partners: ALDH2 (0.961)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_06207.1, huMAP3_13307.1
- **Function (MyGene.info)**: aldehyde dehydrogenase 6 family member A1. This gene encodes a member of the aldehyde dehydrogenase protein family. The encoded protein is a mitochondrial methylmalonate semialdehyde dehydrogenase that plays a role in the valine and pyrimidine catabolic pathways. This protein catalyzes the irreversible oxidative decarboxylation of malonate and methylmalonate semialdehydes to acetyl- and propionyl-CoA. Methylmalonate semialdehyde dehydrogen…
- **Diseases (Open Targets)**: methylmalonate semialdehyde dehydrogenase deficiency (0.706); hereditary disease (0.413); alcohol drinking (0.158); atrial fibrillation (0.089); gastric cancer (0.076)
- **Europe PMC papers**: 1031
- **Why important**: ALDH6A1 is the other member of the high-confidence STRING pair with ALDH2 and is present in both hu.MAP complexes (hu.MAP huMAP3_06207.1) and (hu.MAP huMAP3_13307.1). It contributes to (GO:MF oxidoreductase activity; q_global = 0.043) and (STRING Keyword Oxidoreductase; within-query FDR = 0.0038), is associated with liver, hepatocytes, kidney, and proximal-tubule cells, and has a defined mitochondrial role in methylmalonate semialdehyde, valine, and pyrimidine catabolism. Its established deficiency phenotype gives the gene strong mechanistic and clinical relevance despite its relatively peripheral position in the co-abundance graph.
- **Conclusion**: Established evidence supports ALDH6A1 as a mitochondrial catabolic aldehyde-dehydrogenase component that reinforces the ALDH2-centered interpretation. Its participation in the shared module may reflect coordinated mitochondrial substrate handling, but the specific substrate relationship within this module remains unproven.

#### CAT

- **Related proteins** (co-abundance neighbors): ALDH2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Vesicles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catalase. This gene encodes catalase, a key antioxidant enzyme in the bodies defense against oxidative stress. Catalase is a heme enzyme that is present in the peroxisome of nearly all aerobic cells. Catalase converts the reactive oxygen species hydrogen peroxide to water and oxygen and thereby mitigates the toxic effects of hydrogen peroxide. Oxidative stress is hypothesized to play a role in the developme…
- **Diseases (Open Targets)**: acatalasia (0.697); type 2 diabetes mellitus (0.354); COVID-19 (0.299); major depressive disorder (0.272); neurodegenerative disease (0.224)
- **Europe PMC papers**: 432201
- **Why important**: CAT is included in the primary oxidoreductase evidence (GO:MF oxidoreductase activity; q_global = 0.043) and supplementary STRING evidence (STRING Keyword Oxidoreductase; within-query FDR = 0.0038), and it is directly connected to ALDH2 in the module. Its established function is removal of hydrogen peroxide and protection from oxidative stress. The liver and hepatocyte enrichment, together with detection in liver, supports tissue relevance. CAT also has an exceptionally large literature base and broad disease associations, making it an important interpretive anchor for the redox aspect of the module.
- **Conclusion**: Established evidence supports CAT as an antioxidant component linked to the aldehyde-detoxification core. Its co-abundance with ALDH2 is compatible with coordinated management of reactive metabolites, but it does not demonstrate that peroxide production is the cause of the module.

#### PTGR1

- **Related proteins** (co-abundance neighbors): DHRS1 (0.83), ETFDH (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prostaglandin reductase 1. This gene encodes an enzyme that is involved in the inactivation of the chemotactic factor, leukotriene B4. The encoded protein specifically catalyzes the NADP+ dependent conversion of leukotriene B4 to 12-oxo-leukotriene B4. A pseudogene of this gene is found on chromosome 1. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2009].
- **Diseases (Open Targets)**: poisoning (0.285); response to antibiotic (0.280); malunion fracture (0.269); Alzheimer disease (0.242); Parkinson disease (0.241)
- **Europe PMC papers**: 699
- **Why important**: PTGR1 is part of (GO:MF oxidoreductase activity; q_global = 0.043) and (STRING Keyword Oxidoreductase; within-query FDR = 0.0038) and connects DHRS1 with the central ETFDH neighborhood. Its established function is NADP-dependent inactivation of leukotriene B4, with additional prostaglandin and lipoxin metabolism annotations. Liver and hepatocyte enrichment supports tissue relevance, while its immune-cell annotation provides a possible link between metabolic redox state and inflammatory lipid mediators. Its literature volume is smaller than that of ALDH2 or CAT, which makes it both biologically informative and comparatively less characterized in this module context.
- **Conclusion**: Established evidence supports PTGR1 as a lipid-mediator reductase that may connect redox metabolism with inflammatory signaling. Its role as a bridge in this module is plausible from the network and annotations, but whether it contributes functionally to the shared liver–stem_cells program is a hypothesis.

## Module 9

**Tissue pair**: liver and stem_cells  
**Genes (16)**: ALG2, ATP1A1, CLUH, HSD17B7, EIF3C, EMC1, NUP205, ALDH18A1, POLDIP2, RSL1D1, RPL6, SNRPA1, SF3B3, CCT3, TECR, ALYREF

### Function

The module does not have any GO or KEGG term that passes global multiple-testing correction, so no pathway-level function can be claimed from primary enrichment evidence. Its gene-level pattern instead suggests a mixed cellular maintenance program: translation and ribosome-associated activity through RSL1D1, RPL6, EIF3C and CCT3; pre-mRNA splicing through SNRPA1 and SF3B3; membrane, ion-gradient and lipid-related biology through ATP1A1, TECR and HSD17B7; and supporting processes involving glycosylation, nuclear transport, mitochondrial organization and RNA export. The co-abundance graph is sparse and contains several small neighborhoods rather than one densely connected functional unit. These interpretations are biological annotations of member genes, not globally significant enrichment claims.

**Cell composition.** The module is not dominated by secreted proteins and does not show a blood-cell signature in the HPA summary: secreted genes are absent and every member has low immune-cell specificity. Most genes have low tissue specificity, while several are cell-type enhanced across diverse cell types. Liver protein detection is common among the genes with available HPA data, but the pattern is not liver-exclusive; tissue-enhanced genes include liver, parathyroid gland, salivary gland, skeletal muscle and bone marrow examples. The shared module therefore is more consistent with broadly expressed intracellular machinery, with possible contributions from shared cellular states or sample composition, than with a plasma-protein or blood-contamination module. The lack of matching HPA stem-cell tissue data limits direct comparison between the two tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supplies only two high-confidence relationships within the module: RPL6 with RSL1D1, and SF3B3 with SNRPA1. These support known ribosome-associated and spliceosome-associated substructure, respectively, but leave most module edges without corresponding high-confidence STRING support. hu.MAP identifies ATP1A1 with TECR in (hu.MAP huMAP3_10473.1), although they represent only a small subset of that broad complex, and identifies SNRPA1 with SF3B3 in the spliceosome-related complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1). The spliceosome pair is therefore supported independently by both STRING and hu.MAP, whereas the ATP1A1–TECR pairing has weaker complex-context support. Overall, the external interaction evidence validates selected local relationships but not a single physical complex encompassing the whole module.

**STRING interactions (score >= 0.7)**: 2 of 120 gene pairs: RPL6–RSL1D1 (0.919); SF3B3–SNRPA1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10473.1 (ATP1A1, TECR; 2/24); huMAP3_06511.1 (SNRPA1, SF3B3; 2/79); huMAP3_08980.1 (SNRPA1, SF3B3; 2/97)

### Novelty

This should not be called a newly discovered molecular complex or a novel pathway. The strongest relationships are already represented in STRING or hu.MAP, and the member functions are established. The potentially novel observation is the liver–stem-cell co-abundance pattern linking otherwise distinct processes, especially translation, RNA processing, membrane transport and lipid metabolism. However, absence of a relationship from STRING or hu.MAP cannot establish novelty, and the sparse graph, lack of globally significant enrichment and mixed HPA profile make a biological-discovery claim premature. Replication in independent cohorts, cell-composition adjustment, and perturbation or time-course testing would be needed to distinguish a reproducible cross-tissue regulatory module from correlated expression caused by shared cellular state.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular adaptation state in which protein synthesis and RNA maturation are coordinated with membrane homeostasis and lipid or sterol metabolism. In this model, RSL1D1 and EIF3C represent translational capacity, SNRPA1 and SF3B3 represent pre-mRNA processing, while ATP1A1, TECR and HSD17B7 represent membrane-ion and lipid requirements. The observed co-abundance could arise from coordinated regulation during hepatocyte or stem-cell maintenance, differentiation, or metabolic remodeling. This is a hypothesis rather than a demonstrated mechanism; the available interaction and enrichment evidence does not establish direct regulatory links among these branches.

### Important genes

#### RSL1D1

- **Related proteins** (co-abundance neighbors): EIF3C (0.86), SF3B3 (0.84), CCT3 (0.82), ATP1A1 (0.80), RPL6 (0.80); STRING partners: RPL6 (0.919)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal L1 domain containing 1. Enables mRNA 3'-UTR binding activity and mRNA 5'-UTR binding activity. Involved in regulation of apoptotic process and regulation of cellular senescence. Acts upstream of or within regulation of protein localization. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: adolescent idiopathic scoliosis (0.219); hepatocellular carcinoma (0.099); neoplasm (0.099); colorectal carcinoma (0.096); insomnia (0.078)
- **Europe PMC papers**: 381
- **Why important**: RSL1D1 has the strongest network position in the module, connecting EIF3C, SF3B3, CCT3, ATP1A1 and RPL6. Its nucleolar and chromosomal localization, RNA-binding annotations, and reported roles in protein localization, apoptosis and cellular senescence make it a plausible coordinator between translation-related and nuclear processes. The RPL6 relationship is supported by high-confidence STRING evidence. Its literature volume is substantial, and the fact sheet links it to hepatocellular carcinoma and other disease areas.
- **Conclusion**: Established evidence supports RSL1D1 as a central co-abundance connector with nucleolar and RNA-related functions and a known relationship to RPL6. It is a reasonable module anchor, but the data do not prove that it regulates the other module branches or drives the liver–stem-cell association.

#### ATP1A1

- **Related proteins** (co-abundance neighbors): ALG2 (0.86), ALDH18A1 (0.84), RSL1D1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_10473.1
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 is connected to ALG2, ALDH18A1 and RSL1D1 and encodes the catalytic alpha subunit of the sodium–potassium pump, which maintains transmembrane electrochemical gradients and supports coupled transport. HPA shows liver detection and tissue or cell-type enhancement in several epithelial and transport-relevant cell types. It is also the module member paired with TECR in hu.MAP complex (hu.MAP huMAP3_10473.1). Its disease associations and high literature volume make it a biologically prominent candidate.
- **Conclusion**: Established evidence supports ATP1A1 as a membrane homeostasis and ion-gradient marker with a strong tissue-cellular context. Its module connection to translation and metabolism is an association, not evidence that ATP1A1 mechanistically controls those processes.

#### SNRPA1

- **Related proteins** (co-abundance neighbors): EIF3C (0.86), ALYREF (0.80); STRING partners: SF3B3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein polypeptide A'. Enables RNA binding activity. Involved in mRNA splicing, via spliceosome and spermatogenesis. Located in nuclear speck. Part of U2-type catalytic step 2 spliceosome and U2-type precatalytic spliceosome. Implicated in connective tissue disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.538); dengue disease (0.370); phosphorus metabolism disease (0.196); hypotensive disorder (0.196); cancer (0.087)
- **Europe PMC papers**: 520
- **Why important**: SNRPA1 is part of the U2 spliceosome and is connected to EIF3C and ALYREF. It has direct high-confidence STRING support with SF3B3 and occurs with SF3B3 in both spliceosome-related hu.MAP complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1). Its RNA-splicing and snRNP-assembly functions provide one of the clearest mechanistic substructures in the module. Its disease associations and established literature support make it an informative indicator of RNA-processing state.
- **Conclusion**: Established evidence supports SNRPA1 as a core RNA-splicing component and as one half of the module’s best-supported physical or complex-level relationship. The module does not establish altered splicing or a causal role for SNRPA1 in either tissue.

#### SF3B3

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.84); STRING partners: SNRPA1 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Nucleoli rim; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: splicing factor 3b subunit 3. This gene encodes subunit 3 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); dengue disease (0.370); cervical cancer (0.189); cervical carcinoma (0.189); prostate cancer (0.111)
- **Europe PMC papers**: 965
- **Why important**: SF3B3 is a component of the SF3B and U2 snRNP machinery and is annotated for spliceosomal assembly, conformational change and mRNA splicing. Its direct relationship with SNRPA1 is supported by STRING, and the same pair appears in hu.MAP complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1). Its position connects a well-supported spliceosome substructure to RSL1D1, while its disease associations and broad literature provide substantial prior biological context.
- **Conclusion**: Established evidence supports SF3B3 as a representative of spliceosome biology within the module and validates the local SNRPA1–SF3B3 signal. It remains a marker of coordinated abundance rather than proof of altered spliceosome activity.

#### HSD17B7

- **Related proteins** (co-abundance neighbors): POLDIP2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydroxysteroid 17-beta dehydrogenase 7. HSD17B7 encodes an enzyme that functions both as a 17-beta-hydroxysteroid dehydrogenase (EC 1.1.1.62) in the biosynthesis of sex steroids and as a 3-ketosteroid reductase (EC 1.1.1.270) in the biosynthesis of cholesterol (Marijanovic et al., 2003 [PubMed 12829805]).[supplied by OMIM, May 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.517); open-angle glaucoma (0.139); Decreased total leukocyte count (0.081); functional neutrophil defect (0.065); Heterotaxia (0.057)
- **Europe PMC papers**: 1033
- **Why important**: HSD17B7 is connected to POLDIP2 and is tissue-enhanced in liver, making it particularly relevant to the tissue pair. It functions in steroid and cholesterol biosynthesis and is annotated for related lipid pathways. Its connection to a DNA-replication-associated interactor creates a possible bridge between metabolic state and cellular maintenance, although that bridge is not independently confirmed by STRING or hu.MAP. The gene has a substantial literature base and disease associations including neurodegenerative disease and glaucoma.
- **Conclusion**: Established evidence supports HSD17B7 as a liver-relevant sterol and steroid biosynthesis enzyme. Its role as a mechanistic bridge within this module is hypothetical and requires validation beyond co-abundance.

## Module 10

**Tissue pair**: liver and stem_cells  
**Genes (8)**: AP1B1, CPNE3, IDE, MCCC1, MEMO1, OPA1, PDIA5, VPS13C

### Function

The module is most consistent with coordinated organelle maintenance and intracellular trafficking rather than a narrowly defined pathway. VPS13C is the central network connector and is annotated in Golgi-to-endosome transport, phospholipid transport, mitochondrion organization, macroautophagy, and intermembrane lipid transfer. These annotations connect with OPA1-mediated mitochondrial organization, AP1B1-mediated Golgi and vesicle transport, PDIA5-mediated endoplasmic-reticulum protein folding, IDE-mediated peptide proteolysis, and MCCC1-mediated branched-chain amino-acid catabolism. The network therefore suggests a broad relationship among membrane traffic, mitochondrial homeostasis, proteostasis, and metabolism. No GO or KEGG term passed global correction; there are also no supplementary STRING terms. The functional interpretation is consequently gene-based and network-based rather than enrichment-based.

**Cell composition.** The module is predominantly composed of broadly expressed intracellular proteins, with low tissue specificity reported for most genes by HPA. All module proteins were detected in liver, whereas HPA provides no matching stem-cell tissue comparison, so the liver detection pattern cannot establish stem-cell specificity. Only PDIA5 is tissue enhanced in liver, and its single-cell annotations include hepatocytes as well as other cell populations. The module is not strongly blood-cell biased: most genes have low immune-cell specificity, although PDIA5 is immune-cell enhanced in plasmacytoid dendritic cells. Several genes have cell-type-enhanced annotations, including AP1B1 in microglia and Hofbauer cells, CPNE3 in esophageal and neutrophil-progenitor populations, and MCCC1 in alveolar type-two cells. HPA reports two secreted genes overall, but the individual annotations supplied here identify IDE as secreted in other tissues and PDIA5 as intracellular and membrane associated. Overall, the module could partly reflect shared housekeeping or organelle biology rather than a liver-and-stem-cell-specific program, with limited evidence for a dominant blood contamination signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was detected among the module genes, and no STRING functional-enrichment term was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance links are not corroborated here as established physical interactions or as membership in a known multiprotein complex. This does not invalidate the module: co-abundance can reflect coordinated regulation, shared organelle state, common cell composition, or indirect biological relationships. The strongest internal structure is the connectivity of VPS13C to MEMO1, PDIA5, OPA1, AP1B1, IDE, and MCCC1, while OPA1 provides a smaller mitochondrial branch through CPNE3. These links should be regarded as co-abundance relationships, not demonstrated molecular binding events.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be claimed as a newly discovered molecular complex or pathway. Its genes have established and biologically diverse functions, and several have substantial literature and disease annotation, especially OPA1 and IDE. At the same time, the particular liver-and-stem-cell co-abundance grouping is not explained by any globally significant GO or KEGG term, STRING enrichment, STRING interaction, or hu.MAP complex in the supplied evidence. Therefore the most defensible conclusion is that the gene grouping may represent a potentially interesting co-expression observation, but its novelty and biological specificity remain unproven. Absence from STRING or hu.MAP is evidence that the grouping is not already supported there, not proof that it is novel.

**Hypothesis.** Hypothesis: the module reflects a coordinated cellular state in which lipid and membrane handling by VPS13C is coupled to mitochondrial remodeling through OPA1, cargo sorting through AP1B1, endoplasmic-reticulum folding through PDIA5, peptide turnover through IDE, and mitochondrial nutrient metabolism through MCCC1. In liver and stem-cell-related samples, this could arise from shared regulation of organelle quality control and metabolic adaptation rather than from direct binding among the proteins. The hypothesis predicts that module activity should track measurements of mitochondrial integrity, lipid trafficking, secretory-pathway load, proteostasis, and branched-chain amino-acid metabolism. These predictions require independent expression, perturbation, localization, and biochemical testing.

### Important genes

#### VPS13C

- **Related proteins** (co-abundance neighbors): MEMO1 (0.87), PDIA5 (0.84), OPA1 (0.84), AP1B1 (0.83), IDE (0.82), MCCC1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vacuolar protein sorting 13 homolog C. This gene encodes a member of the vacuolar protein sorting-associated 13 gene family. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Oct 2010]
- **Diseases (Open Targets)**: young-onset Parkinson disease (0.726); Parkinson disease (0.545); type 2 diabetes mellitus (0.460); neurodegenerative disease (0.456); diabetes mellitus (0.418)
- **Europe PMC papers**: 1114
- **Why important**: VPS13C is the central connector of the module and links the largest set of module neighbors. Its established annotations span Golgi-to-endosome transport, phospholipid transport, mitochondrion organization, macroautophagy, and intermembrane lipid transfer, making it the best integrative candidate for the module's organelle and membrane-traffic signal. It also has extensive literature and disease associations involving Parkinson disease, young-onset Parkinson disease, and diabetes.
- **Conclusion**: Established evidence supports VPS13C as the principal network and functional anchor. It is plausible, but not demonstrated, that VPS13C coordinates the other module processes; the co-abundance structure alone does not establish that it regulates its neighbors.

#### OPA1

- **Related proteins** (co-abundance neighbors): VPS13C (0.84), CPNE3 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OPA1 mitochondrial dynamin like GTPase. The protein encoded by this gene is a nuclear-encoded mitochondrial protein with similarity to dynamin-related GTPases. The encoded protein localizes to the inner mitochondrial membrane and helps regulate mitochondrial stability and energy output. This protein also sequesters cytochrome c. Mutations in this gene have been associated with optic atrophy type 1, which is a dominantly inherited optic …
- **Diseases (Open Targets)**: autosomal dominant optic atrophy, classic form (0.846); Behr syndrome (0.812); optic atrophy with or without deafness, ophthalmoplegia, myopathy, ataxia, and neuropathy (0.766); mitochondrial DNA depletion syndrome 14B (cardioencephalomyopathic type) (0.745); optic atrophy (0.653)
- **Europe PMC papers**: 12169
- **Why important**: OPA1 is connected to VPS13C and CPNE3 and contributes a distinct mitochondrial branch. It is an inner-mitochondrial-membrane dynamin-like GTPase involved in mitochondrial stability, energy output, mitochondrial fusion, and mitochondrial organization, and it can sequester cytochrome c. OPA1 has extensive literature and strong disease associations with dominant optic atrophy and related mitochondrial disorders.
- **Conclusion**: Established evidence identifies OPA1 as a major mitochondrial-homeostasis component with substantial clinical relevance. Its co-abundance with VPS13C may indicate coordinated mitochondrial and lipid-organelle biology, but a direct VPS13C–OPA1 mechanism remains a hypothesis.

#### AP1B1

- **Related proteins** (co-abundance neighbors): VPS13C (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor related protein complex 1 subunit beta 1. Adaptor protein complex 1 is found at the cytoplasmic face of coated vesicles located at the Golgi complex, where it mediates both the recruitment of clathrin to the membrane and the recognition of sorting signals within the cytosolic tails of transmembrane receptors. This complex is a heterotetramer composed of two large, one medium, and one small adaptin subunit. The protein encoded by this gene…
- **Diseases (Open Targets)**: ichthyosiform erythroderma, corneal involvement, and hearing loss (0.715); HIV infectious disease (0.503); MEDNIK syndrome (0.371); neurodegenerative disease (0.370); KID syndrome (0.292)
- **Europe PMC papers**: 500
- **Why important**: AP1B1 connects to the central VPS13C node and supplies a concrete Golgi and vesicle-trafficking function. As a large subunit of adaptor protein complex one, it participates in clathrin recruitment, cargo recognition, intracellular transport, receptor-mediated endocytosis, and basolateral secretion. Its disease annotations include syndromic disorders involving epithelial, auditory, and neurological features, and it has established literature support.
- **Conclusion**: Established evidence supports AP1B1 as the module's cargo-sorting and vesicle-transport representative. The module may couple lipid handling to cargo trafficking, but the data do not show that AP1B1 directly mediates the VPS13C association.

#### PDIA5

- **Related proteins** (co-abundance neighbors): VPS13C (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein disulfide isomerase family A member 5. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, a TRX-like domain, and a C-terminal ER-retention sequence. The N-terminal TRX-like domain is the primary bind…
- **Diseases (Open Targets)**: spinal stenosis (0.273); blood coagulation disease (0.269); temporomandibular joint disorder (0.262); placenta praevia (0.144); glioblastoma (0.100)
- **Europe PMC papers**: 501
- **Why important**: PDIA5 is connected to VPS13C and is the clearest liver-enhanced member in the HPA summary. It is an endoplasmic-reticulum protein disulfide isomerase with thioredoxin domains that catalyzes protein folding and thiol-disulfide exchange, and it is annotated in protein folding and electron transport chain processes. Its hepatocyte annotation makes it especially relevant to the liver side of the shared module, while its plasmacytoid-dendritic-cell enhancement cautions that cell composition may contribute.
- **Conclusion**: Established evidence supports PDIA5 as an endoplasmic-reticulum proteostasis and liver-associated component. Its co-abundance with VPS13C may reflect coordinated secretory-pathway and membrane-trafficking demand, but this is a hypothesis rather than a demonstrated interaction.

#### IDE

- **Related proteins** (co-abundance neighbors): VPS13C (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin degrading enzyme. This gene encodes a zinc metallopeptidase that degrades intracellular insulin, and thereby terminates insulins activity, as well as participating in intercellular peptide signalling by degrading diverse peptides such as glucagon, amylin, bradykinin, and kallidin. The preferential affinity of this enzyme for insulin results in insulin-mediated inhibition of the degradation of other peptides such as…
- **Diseases (Open Targets)**: diabetes mellitus (0.307); type 2 diabetes mellitus (0.287); diabetic retinopathy (0.146); diabetic eye disease (0.144); brain cancer (0.142)
- **Europe PMC papers**: 19876
- **Why important**: IDE is connected to VPS13C and has the most extensive literature among the module genes. It is an intracellular zinc metallopeptidase that degrades insulin and other peptides and is annotated in proteolysis, insulin-receptor signaling, peptide catabolism, ubiquitin recycling, and antigen processing. Its disease associations include diabetes and diabetic complications, making it particularly relevant to liver metabolism and cellular nutrient signaling.
- **Conclusion**: Established evidence supports IDE as a peptide-turnover and metabolic-signaling component with strong disease relevance. The module may reflect coordinated coupling of peptide turnover with organelle trafficking and metabolism, but the co-abundance data do not establish a causal IDE–VPS13C relationship.

## Module 11

**Tissue pair**: liver and stem_cells  
**Genes (5)**: BCL2L13, COMMD9, ME1, CHCHD4, NDRG2

### Function

The module is most consistent with a coordinated mitochondrial and metabolic state, with possible links to mitochondrial protein import, respiratory-chain assembly, cellular redox balance, apoptosis, and tissue-specific differentiation. CHCHD4 is the central co-abundance connector and has established roles in mitochondrial intermembrane-space protein import, disulfide-relay protein maturation, and respiratory-chain complex assembly. ME1 provides a metabolic link through cytosolic NADPH production and the connection between malate metabolism, glycolysis, and the citric-acid cycle. BCL2L13 contributes an apoptosis-related mitochondrial component, while NDRG2 contributes a differentiated-cell and signaling context. No GO or KEGG term passed global correction, so this functional interpretation is based on individual gene annotations and network structure rather than statistically significant module-level enrichment.

**Cell composition.** The module is not composed of secreted proteins, and its members are predominantly broadly distributed rather than tissue-restricted. Most genes have low tissue specificity, while NDRG2 is tissue enhanced in brain, salivary gland, skeletal muscle, and tongue. All members show cell-type-enhanced patterns, including epithelial, glial, muscle, germ-cell, liver-associated, and immune-associated cell types. Two genes are immune-cell enriched, but the module as a whole does not show strong immune specificity. Liver protein detection is present for most members, whereas BCL2L13 is not detected there. These observations argue against a plasma-protein explanation and do not establish that the shared module is merely a blood-cell contaminant, although shared cell populations or differing cellular composition could contribute to the co-abundance pattern.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and no STRING functional-enrichment result was reported. No hu.MAP complex contained multiple module members. Therefore, the co-abundance edges should not be described as established physical interactions or as membership in a known multiprotein complex. The network is instead a transcript or protein co-abundance structure centered on CHCHD4, with CHCHD4 connected to COMMD9, BCL2L13, and NDRG2, and COMMD9 connected to ME1. The absence of STRING and hu.MAP support limits mechanistic certainty but does not invalidate the reproducible cross-tissue co-abundance observation.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a potentially novel cross-tissue co-abundance association because the module has no reported high-confidence STRING interactions, no shared hu.MAP complex, and no globally significant GO or KEGG enrichment. However, those absences do not prove novelty. The individual genes and their broad biological functions are already established, and the reported co-abundance relationships could reflect shared regulation, cellular composition, metabolic state, or indirect association. A claim of a new biological mechanism would require independent replication, perturbation experiments, and comparison with published co-expression or proteomic networks.

**Hypothesis.** Hypothesis: in liver and stem-cell samples, a shared cellular state coordinately regulates mitochondrial proteostasis and energy metabolism. CHCHD4 may act as the network-linked mitochondrial component, while ME1 supplies redox and anabolic support through NADPH generation. BCL2L13 may couple mitochondrial state to apoptotic sensitivity, and NDRG2 may connect the state to differentiation or signaling programs. COMMD9 could participate in the regulatory bridge between metabolic and mitochondrial features, but its mechanistic role in this module is presently uncertain. This is a hypothesis derived from co-abundance and gene annotations, not an established physical pathway.

### Important genes

#### CHCHD4

- **Related proteins** (co-abundance neighbors): COMMD9 (0.82), BCL2L13 (0.80), NDRG2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coiled-coil-helix-coiled-coil-helix domain containing 4. CHCHD4, a component of human mitochondria, belongs to a protein family whose members share 6 highly conserved cysteine residues constituting a -CXC-CX(9)C-CX(9)C- motif in the C terminus (Hofmann et al., 2005 [PubMed 16185709]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: lactic acidosis (0.333); Abnormal brain morphology (0.333); fetal growth restriction (0.333); Encephalopathy (0.333); Decreased liver function (0.333)
- **Europe PMC papers**: 351
- **Why important**: CHCHD4 is the central network connector, linked to COMMD9, BCL2L13, and NDRG2. Its established mitochondrial localization and functions in intermembrane-space protein import, disulfide-relay maturation, and respiratory-chain complex assembly give the module its strongest mechanistic anchor. It also has substantial literature support and disease associations involving lactic acidosis, encephalopathy, abnormal brain morphology, fetal growth restriction, and decreased liver function.
- **Conclusion**: Established evidence supports CHCHD4 as a mitochondrial protein-import and respiratory-chain assembly factor and as the structural hub of this co-abundance module. It is plausible, but not proven, that CHCHD4 coordinates the other module members or mediates the shared liver and stem-cell state.

#### ME1

- **Related proteins** (co-abundance neighbors): COMMD9 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm, Plasma membrane; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: malic enzyme 1. This gene encodes a cytosolic, NADP-dependent enzyme that generates NADPH for fatty acid biosynthesis. The activity of this enzyme, the reversible oxidative decarboxylation of malate, links the glycolytic and citric acid cycles. The regulation of expression for this gene is complex. Increased expression can result from elevated levels of thyroid hormones or by higher proportions of carbohydrates i…
- **Diseases (Open Targets)**: ovarian dysfunction (0.159); hearing loss disorder (0.156); Abnormality of the skeletal system (0.153); drug-induced lupus erythematosus (0.144); placental abruption (0.142)
- **Europe PMC papers**: 5962
- **Why important**: ME1 is the metabolic representative of the module and is connected to COMMD9. Its established enzymatic role generates NADPH and links malate metabolism with glycolytic and citric-acid-cycle activity, making it relevant to biosynthesis and cellular redox balance. It has the largest literature volume among the module genes and has multiple disease associations.
- **Conclusion**: Established evidence supports ME1 as a cytosolic metabolic and NADPH-producing enzyme. Its co-abundance with the mitochondrial-centered portion of the module supports a possible metabolic coupling, but it does not demonstrate direct interaction with CHCHD4 or a shared biochemical complex.

#### BCL2L13

- **Related proteins** (co-abundance neighbors): CHCHD4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BCL2 like 13. This gene encodes a mitochondrially-localized protein with conserved B-cell lymphoma 2 homology motifs. Overexpression of the encoded protein results in apoptosis. Alternatively spliced transcript variants have been observed for this gene. [provided by RefSeq, Jul 2012].
- **Diseases (Open Targets)**: neurodegenerative disease (0.291); urolithiasis (0.243); alcohol drinking (0.243); Phenotypic abnormality (0.214); sign or symptom (0.214)
- **Europe PMC papers**: 991
- **Why important**: BCL2L13 is a mitochondrial member directly connected to the central CHCHD4 node. Its BCL2 homology motifs and established association with apoptosis provide a plausible link between mitochondrial function and cell-survival decisions. It also has disease associations involving neurodegenerative disease and phenotypic abnormalities, with meaningful literature support.
- **Conclusion**: Established evidence supports BCL2L13 as a mitochondrially localized apoptosis-related protein. Its placement beside CHCHD4 suggests a possible connection between mitochondrial proteostasis and apoptotic sensitivity, but the module does not establish that CHCHD4 regulates BCL2L13.

#### NDRG2

- **Related proteins** (co-abundance neighbors): CHCHD4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Centriolar satellite; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NDRG family member 2. This gene is a member of the N-myc downregulated gene family which belongs to the alpha/beta hydrolase superfamily. The protein encoded by this gene is a cytoplasmic protein that may play a role in neurite outgrowth. This gene may be involved in glioblastoma carcinogenesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2017].
- **Diseases (Open Targets)**: breast carcinoma (0.120); neoplasm (0.119); breast cancer (0.113); hepatocellular carcinoma (0.113); colorectal carcinoma (0.109)
- **Europe PMC papers**: 2150
- **Why important**: NDRG2 is directly connected to CHCHD4 and is the only tissue-enhanced member in the module. Its enrichment in neural, muscle, tongue, and salivary-gland contexts, together with annotations involving signal transduction and substantia-nigra development, gives the module a differentiated-cell and tissue-state dimension. It also has substantial literature and disease associations including breast carcinoma, hepatocellular carcinoma, and colorectal carcinoma.
- **Conclusion**: Established evidence supports NDRG2 as a differentiation- and signaling-associated cytoplasmic protein with tissue-selective expression. Its relationship to the mitochondrial hub is a module-level hypothesis rather than a demonstrated molecular interaction.

#### COMMD9

- **Related proteins** (co-abundance neighbors): ME1 (0.82), CHCHD4 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: COMM domain containing 9. Predicted to be involved in sodium ion transport. Predicted to act upstream of or within cholesterol homeostasis. Located in Golgi apparatus; cytosol; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: atopic eczema (0.133); dermatitis (0.131); brain aneurysm (0.126); psoriasis (0.117); asthma (0.115)
- **Europe PMC papers**: 175
- **Why important**: COMMD9 occupies the bridge position between ME1 and CHCHD4 in the co-abundance graph. Its reported links to endocytic recycling, sodium transport, and cholesterol homeostasis provide a possible regulatory or trafficking connection between metabolism and mitochondrial state. It has disease associations involving inflammatory and dermatologic conditions and an established body of literature, although less extensive than ME1 or NDRG2.
- **Conclusion**: Established evidence supports COMMD9 as a broadly expressed protein with reported roles or predicted involvement in trafficking, ion transport, and cholesterol homeostasis. Its bridge position is compatible with a regulatory role in the module, but this remains speculative because neither STRING nor hu.MAP supports a known complex involving these members.

## Module 12

**Tissue pair**: liver and stem_cells  
**Genes (5)**: EIF3F, HSP90AA1, MAL2, TUBB4B, ZC3HAV1

### Function

No GO or KEGG term passed global correction, so the module has no statistically supported pathway annotation from the primary enrichment analysis. The co-abundance structure is centered on MAL2, with links to HSP90AA1, EIF3F, ZC3HAV1, and TUBB4B. The gene annotations suggest a mixed cellular program involving polarized membrane trafficking, protein folding, translation initiation, antiviral RNA regulation, and microtubule organization. These annotations support biological plausibility but do not establish a single coherent function for the module.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of its members is annotated as secreted. HPA indicates generally low immune-cell specificity, with one gene not detected in immune cells, so the module is not strongly suggestive of a blood-cell contaminant. Most genes have low tissue specificity, while MAL2 is tissue enhanced in esophagus and ZC3HAV1 is tissue enhanced in bone marrow. All members show cell-type-enhanced expression in selected epithelial, reproductive, stromal, or immune-related cell types. Four proteins are detected in liver, whereas there is no matching HPA tissue for stem cells. The shared signal may therefore reflect broadly distributed cellular programs or shared cell types rather than a liver-specific or stem-cell-specific pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional-enrichment result was reported, and no STRING interaction among the module genes met the supplied interaction threshold. No hu.MAP complex contained multiple module members. The observed co-abundance edges are therefore not corroborated by the supplied high-confidence physical-interaction or complex evidence. Known biology remains gene-specific: MAL2 is associated with lipid rafts and polarized transcytosis, HSP90AA1 is a molecular chaperone, EIF3F is part of the translation-initiation machinery, ZC3HAV1 participates in antiviral RNA decay and innate immune responses, and TUBB4B is a microtubule component.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially unusual co-abundance association because the module is not supported by a shared GO or KEGG term, STRING enrichment, high-confidence STRING interactions, or a hu.MAP complex. However, it cannot be called a new biological discovery on that basis alone. Database absence may reflect context dependence, incomplete interaction coverage, or co-regulation without direct physical binding. The strongest defensible conclusion is that the liver and stem-cell co-abundance pattern is a context-specific candidate association requiring independent replication and experimental testing.

**Hypothesis.** Hypothesis: the module may represent a shared polarized-cell stress and proteostasis program in which MAL2-linked membrane organization is coordinated with chaperone activity, translation control, antiviral RNA surveillance, and microtubule-dependent intracellular organization. This could arise from a common epithelial or progenitor-like cellular state in the two tissue groups rather than from a stable multiprotein complex. The hypothesis is supported by the central position of MAL2 and the complementary annotations of its neighbors, but it is not established by enrichment or physical-interaction evidence.

### Important genes

#### MAL2

- **Related proteins** (co-abundance neighbors): HSP90AA1 (0.89), EIF3F (0.85), ZC3HAV1 (0.83), TUBB4B (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mal, T cell differentiation protein 2. This gene encodes a multispan transmembrane protein belonging to the MAL proteolipid family. The protein is a component of lipid rafts and, in polarized cells, it primarily localizes to endosomal structures beneath the apical membrane. It is required for transcytosis, an intracellular transport pathway used to deliver membrane-bound proteins and exogenous cargos from the basolateral to the apical …
- **Diseases (Open Targets)**: cholelithiasis (0.335); hypertensive disorder (0.323); chronic rhinosinusitis with nasal polyps (0.302); chronic bronchitis (0.292); endocrine system disorder (0.284)
- **Europe PMC papers**: 1980
- **Why important**: MAL2 is the network hub, connected to every other module member, and therefore provides the main structural anchor for interpreting the co-abundance pattern. Its established role in lipid rafts, endosomal localization, and transcytosis makes it relevant to polarized membrane trafficking. HPA places it in an esophageal-enhanced and epithelial-associated expression context, while disease associations include cholelithiasis and several airway or endocrine disorders. Its literature volume is substantial.
- **Conclusion**: Established evidence supports MAL2 as the module's network-centered membrane-trafficking gene. The hypothesis that it coordinates the other module signals is plausible from network position but remains unproven because no supplied STRING or hu.MAP evidence supports a physical complex.

#### HSP90AA1

- **Related proteins** (co-abundance neighbors): MAL2 (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein 90 alpha family class A member 1. The protein encoded by this gene is an inducible molecular chaperone that functions as a homodimer. The encoded protein aids in the proper folding of specific target proteins by use of an ATPase activity that is modulated by co-chaperones. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: cancer (0.643); plasma cell myeloma (0.404); non-small cell lung carcinoma (0.394); dengue disease (0.375); Orthomyxoviridae infectious disease (0.375)
- **Europe PMC papers**: 8215
- **Why important**: HSP90AA1 is a highly studied inducible chaperone with established roles in protein folding and co-chaperone-regulated ATPase activity. It is connected to MAL2 in the module and has the largest literature volume among the members. Its disease associations include cancer, plasma-cell myeloma, lung carcinoma, and viral disease, making it relevant to stress and proteostasis interpretations.
- **Conclusion**: Established evidence supports HSP90AA1 as a broadly acting proteostasis factor that could accompany membrane-trafficking changes. Its participation in this specific module is a hypothesis based on co-abundance, not a demonstrated physical interaction or pathway enrichment result.

#### ZC3HAV1

- **Related proteins** (co-abundance neighbors): MAL2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger CCCH-type containing, antiviral 1. This gene encodes a CCCH-type zinc finger protein. This antiviral protein inhibits viral replication by recruiting cellular RNA degradation machineries to degrade viral mRNAs. The encoded protein plays an important role in the innate immune response against multiple DNA and RNA viruses, including Ebola virus, HIV and SARS-CoV-2 (which causes COVID-19). [provided by RefSeq, Sep 2021].
- **Diseases (Open Targets)**: cancer (0.549); hypothyroidism (0.429); neurodegenerative disease (0.358); autoimmune disease (0.308); Hashimoto thyroiditis (0.306)
- **Europe PMC papers**: 979
- **Why important**: ZC3HAV1 is directly connected to the MAL2 hub and has a distinctive antiviral function. It recruits RNA-degradation machinery, restricts viral replication, and promotes interferon and NF-kappaB-related responses. HPA shows bone-marrow tissue enhancement and cell-type enhancement in neutrophil, natural-killer, plasmacytoid-dendritic, and endometrial cell populations. Its disease associations include cancer, autoimmune disease, and thyroid disorders.
- **Conclusion**: Established evidence supports ZC3HAV1 as an innate antiviral and RNA-surveillance factor. Its presence may indicate an inducible defense-state component, but the available evidence does not establish that antiviral signaling is the defining function of the whole module.

#### EIF3F

- **Related proteins** (co-abundance neighbors): MAL2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit F. Enables deubiquitinase activity and identical protein binding activity. Contributes to translation initiation factor activity. Involved in IRES-dependent viral translational initiation; protein deubiquitination; and translational initiation. Located in membrane. Part of eukaryotic translation initiation factor 3 complex. Implicated in autosomal recessive non-syndromic intellectual disability. [pro…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal recessive 67 (0.675); hereditary disease (0.413); developmental disability (0.371); neurodegenerative disease (0.370); syndromic intellectual disability (0.370)
- **Europe PMC papers**: 997
- **Why important**: EIF3F is linked to MAL2 and is an established component of the eukaryotic translation-initiation complex. It contributes to cytoplasmic and IRES-dependent translation initiation and protein deubiquitination. It is detected in liver, has cell-type enhancement in trophoblast and late-spermatid populations, and is associated with autosomal-recessive intellectual disability and broader developmental disorders.
- **Conclusion**: Established evidence supports EIF3F as a translation-control component that could connect cellular state to protein production. Its role in this module is inferential because no primary enrichment term, STRING interaction, or hu.MAP complex links it mechanistically to the other members.

#### TUBB4B

- **Related proteins** (co-abundance neighbors): MAL2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tubulin beta 4B class IVb. Enables double-stranded RNA binding activity. Predicted to be involved in microtubule cytoskeleton organization and mitotic cell cycle. Located in microtubule. Implicated in Leber congenital amaurosis with early-onset deafness. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Leber congenital amaurosis with early-onset deafness (0.651); non-small cell lung carcinoma (0.615); breast cancer (0.605); breast carcinoma (0.598); neoplasm (0.597)
- **Europe PMC papers**: 1308
- **Why important**: TUBB4B is connected to MAL2 and encodes a microtubule component involved in microtubule organization and mitotic processes. Its HPA cell-type associations include epithelial, ciliated, and germ-cell populations, and its disease associations include Leber congenital amaurosis with early-onset deafness and several cancers. It may be relevant to intracellular transport and polarized-cell architecture.
- **Conclusion**: Established evidence supports TUBB4B as a cytoskeletal and microtubule-related gene. Its inclusion is consistent with a membrane-trafficking or polarized-cell hypothesis, but that connection remains speculative without direct interaction or pathway evidence.

## Module 13

**Tissue pair**: liver and stem_cells  
**Genes (5)**: H4C1, HNRNPK, HNRNPL, RAN, RPL12

### Function

The strongest functional interpretation is a chromatin-associated nuclear RNA-processing module. The sole globally corrected GO/KEGG result is chromatin (GO:CC chromatin; q_global = 0.0118), supported by H4C1, HNRNPK, HNRNPL, and RAN. H4C1 is a core histone involved in nucleosome structure and chromatin organization; HNRNPK and HNRNPL are nuclear heterogeneous ribonucleoproteins involved in RNA processing and splicing; and RAN supports nuclear transport, ribosomal subunit export, DNA synthesis, and cell-cycle processes. RPL12 adds a translation-related component, but it is not part of the significant enrichment. The module therefore most plausibly reflects coordinated nuclear gene-expression machinery involving chromatin, RNA handling, and nuclear transport rather than a narrowly defined metabolic pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: none of the genes is annotated as secreted. It also does not have the profile of a broadly blood-cell-enriched module. Most genes have low tissue specificity and low immune-cell specificity. H4C1 is tissue enhanced in lymphoid tissue and skeletal muscle and is group enriched in eosinophils and neutrophils, while the other genes show selected cell-type enrichments across epithelial, progenitor, stromal, glial, and reproductive cell types. Thus, sample blood contamination or a shared immune-cell population is not the leading explanation, although H4C1 could contribute a cell-composition signal. Protein detection in liver supports that the module is represented in liver; the available HPA summary does not provide a matching stem-cell tissue comparison.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chromatin | 0.0118 | H4C1, HNRNPK, HNRNPL, RAN |

### STRING and hu.MAP

The network is centered on HNRNPK, which connects within the module to H4C1, RAN, RPL12, and HNRNPL. The only high-confidence STRING relationship is HNRNPK–HNRNPL, indicating that this pair is an established interaction rather than a novel network-only association. No STRING functional-enrichment result was reported. HNRNPK and HNRNPL also co-occur in both hu.MAP complexes (hu.MAP huMAP3_10659.1) and (hu.MAP huMAP3_10625.1), whose broader membership consists mainly of heterogeneous nuclear ribonucleoproteins and other RNA-processing or RNA-binding factors. These observations support a known hnRNP-centered nuclear machinery, but they do not establish that every co-abundance edge is a direct physical interaction. The links involving H4C1, RAN, and RPL12 may instead reflect coordinated expression, shared cellular state, or indirect functional coupling.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: HNRNPK–HNRNPL (0.99)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10659.1 (HNRNPL, HNRNPK; 2/28); huMAP3_10625.1 (HNRNPL, HNRNPK; 2/57)

### Novelty

This module should not be presented as a newly discovered molecular complex. Its central HNRNPK–HNRNPL relationship and their joint occurrence in hu.MAP complexes are already established, and the functions of the component genes are well characterized. The module may still represent a potentially interesting liver–stem-cell co-abundance pattern, especially because it combines chromatin, hnRNP, nuclear-transport, and ribosomal components. However, the available evidence does not demonstrate tissue-pair-specific biology, a new physical interaction, or a previously unknown mechanism. Absence of additional STRING or hu.MAP relationships is insufficient to establish novelty; it more cautiously indicates that the module is a small expression-associated assembly built around partly known nuclear machinery.

**Hypothesis.** Hypothesis: in liver and stem-cell samples, a shared proliferative or differentiation-related nuclear state coordinately increases chromatin packaging, RNA processing, nuclear transport, and protein synthesis. H4C1 may represent the chromatin or nucleosome component, HNRNPK and HNRNPL may coordinate processing of nuclear transcripts, RAN may support nuclear import and export during active gene expression and cell cycling, and RPL12 may reflect the translational demand associated with that state. This is a mechanistic hypothesis, not a demonstrated physical complex. Testing would require independent replication across samples, cell-composition adjustment, perturbation of HNRNPK or HNRNPL, and measurement of chromatin accessibility, RNA processing, nuclear transport, and translation.

### Important genes

#### HNRNPK

- **Related proteins** (co-abundance neighbors): H4C1; H4C2; H4C3; H4C4; H4C5; H4C6; H4C8; H4C9; H4C11; H4C12; H4C13; H4C14; H4C15; H4C16 (0.85), RAN (0.84), RPL12 (0.83), HNRNPL (0.81); STRING partners: HNRNPL (0.99)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is the principal network hub, connecting all other module members in the co-abundance subgraph. It is a ubiquitously expressed nuclear hnRNP involved in pre-mRNA processing, transcriptional regulation, RNA metabolism, and signal-responsive gene regulation. It is supported by the significant chromatin term (GO:CC chromatin; q_global = 0.0118), forms the high-confidence STRING pair with HNRNPL, and occurs in both hu.MAP complexes (hu.MAP huMAP3_10659.1) and (hu.MAP huMAP3_10625.1). Its extensive literature and disease associations, including Au-Kline syndrome and other neurodevelopmental and neurodegenerative contexts, make it the strongest integrative candidate.
- **Conclusion**: Established evidence supports HNRNPK as the organizing hub of a known nuclear RNA-processing machinery with a chromatin-associated module signal. The hypothesis that it drives the shared liver–stem-cell co-abundance pattern remains unproven and should not be inferred from hub status alone.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): HNRNPK (0.81); STRING partners: HNRNPK (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is the direct high-confidence STRING partner of HNRNPK and co-occurs with it in both hu.MAP complexes (hu.MAP huMAP3_10659.1) and (hu.MAP huMAP3_10625.1). It is a nucleoplasmic hnRNP involved in RNA processing and alternative splicing and contributes directly to the significant chromatin-associated enrichment (GO:CC chromatin; q_global = 0.0118). Its substantial literature and reported disease associations, including cancer and neuromuscular disease contexts, support its importance as the second core component of the module.
- **Conclusion**: Established evidence identifies HNRNPL as a known partner of HNRNPK within broader RNA-binding complexes and as a plausible contributor to coordinated nuclear RNA regulation. It is reasonable to hypothesize that HNRNPK–HNRNPL activity helps define the module, but the co-abundance data do not establish causality or tissue-specific function.

#### H4C1

- **Related proteins** (co-abundance neighbors): none; STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: H4 clustered histone 1. Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Two molecules of each of the four core histones (H2A, H2B, H3, and H4) form an octamer, around which approximately 146 bp of DNA is wrapped in repeating units, called nucleosomes. The linker histone, H1, interacts with linker DNA between nucleosomes and functions in the com…
- **Diseases (Open Targets)**: viral infectious disease (0.503); infectious disease (0.503); Tessadori-Van Haaften neurodevelopmental syndrome 3 (0.462); breast carcinoma (0.390); cancer (0.371)
- **Europe PMC papers**: 216
- **Why important**: H4C1 is the chromatin-structural gene in the module and contributes to the globally corrected chromatin term (GO:CC chromatin; q_global = 0.0118). Histone H4 is a core component of nucleosomes and is linked to chromatin organization, nucleosome assembly, telomere organization, and localization of CENP-A-containing chromatin. Although H4C1 has no reported STRING or hu.MAP relationship in this module and has a peripheral network position, its tissue and blood-cell enrichment patterns make it informative for interpreting cellular composition and chromatin state. Its disease and cancer associations are documented, though its literature volume is more limited than that of the hnRNP and RAN genes.
- **Conclusion**: Established evidence supports H4C1 as the module's chromatin anchor and as a possible indicator of cell-state or cell-composition effects. It should not be treated as proof of a direct H4C1 interaction with HNRNPK or as evidence that the module is driven by histone biology alone.

#### RAN

- **Related proteins** (co-abundance neighbors): HNRNPK (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAN, member RAS oncogene family. RAN (ras-related nuclear protein) is a small GTP binding protein belonging to the RAS superfamily that is essential for the translocation of RNA and proteins through the nuclear pore complex. The RAN protein is also involved in control of DNA synthesis and cell cycle progression. Nuclear localization of RAN requires the presence of regulator of chromosome condensation 1 (RCC1). Mutations in RAN di…
- **Diseases (Open Targets)**: HIV infectious disease (0.565); Orthomyxoviridae infectious disease (0.376); pemphigus foliaceus (0.298); neurodegenerative disease (0.270); Genu valgum (0.136)
- **Europe PMC papers**: 133080
- **Why important**: RAN links the module's central HNRNPK hub to nuclear transport and cell-cycle biology. It is a nuclear GTP-binding protein required for import and export through the nuclear pore, ribosomal subunit export, DNA synthesis, and mitotic progression. RAN contributes to the significant chromatin-associated term (GO:CC chromatin; q_global = 0.0118) and has an exceptionally extensive literature base, together with disease associations involving infectious, neurodegenerative, and other disorders. Its selected progenitor and proliferative cell-type expression patterns are relevant to a liver–stem-cell comparison.
- **Conclusion**: Established evidence supports RAN as a plausible functional bridge between nuclear RNA handling, chromatin-linked activity, and cell proliferation. The idea that RAN-mediated transport mechanistically coordinates the entire module is a hypothesis requiring perturbation and direct functional assays.

#### RPL12

- **Related proteins** (co-abundance neighbors): HNRNPK (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein L12. Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L11P family of ribosomal proteins. It is located in the cytoplasm. The pr…
- **Diseases (Open Targets)**: Duchenne muscular dystrophy (0.503); Orthomyxoviridae infectious disease (0.462); neurodegenerative disease (0.460); cystic fibrosis (0.390); neuromuscular disease caused by qualitative or quantitative defects of dystrophin (0.323)
- **Europe PMC papers**: 1865
- **Why important**: RPL12 is connected to HNRNPK in the module and represents the translation-related component. It encodes a large-subunit ribosomal protein involved in cytoplasmic translation and has liver protein detection in HPA. It is not part of the significant enrichment (GO:CC chromatin; q_global = 0.0118), has no reported STRING or hu.MAP relationship here, and is less central in the network than HNRNPK. Nevertheless, its established ribosomal function and disease associations make it useful for evaluating whether the module reflects a broader biosynthetic state rather than chromatin and RNA processing alone.
- **Conclusion**: Established evidence supports RPL12 as a marker of translational capacity that may accompany the nuclear program. Its inclusion does not demonstrate a direct ribosome–hnRNP complex or a specialized liver–stem-cell mechanism; that interpretation remains hypothetical.
