# Conserved co-abundance modules: bone and cell line

## Module 0

**Tissue pair**: bone and cell line  
**Genes (12)**: AACS, ASCC3, COPB1, DDX6, EIF3L, FAM91A1, TUBGCP3, KIF2A, NFKB2, ELAC2, SEC24C, UBE4B

### Function

This is a heterogeneous intracellular maintenance module rather than a cleanly defined pathway. Its genes collectively point to vesicle trafficking between the endoplasmic reticulum and Golgi, RNA processing and decay, translation control, ubiquitin-dependent protein quality control, microtubule organization, and inflammatory transcriptional signaling. The strongest coherent functional theme is intracellular proteostasis and trafficking, supported by SEC24C, COPB1, FAM91A1, UBE4B, and DDX6 annotations. However, no GO or KEGG term passed global correction, and STRING supplied no functional-enrichment result. Therefore, these functional themes are an annotation-based interpretation, not evidence of statistically significant pathway enrichment.

**Cell composition.** The module is composed entirely of intracellular proteins, with no secreted genes. All genes have low tissue specificity in HPA, and no tissue-enriched pattern was observed. Most genes also have low cell-type specificity and low immune-cell specificity. A smaller subset shows cell-type associations, including neutrophils, megakaryocytes or platelets, breast lactating cells, esophageal cells, retinal ganglion cells, cytotrophoblasts, and mast cells or monocytes. NFKB2 has an immune-cell-enhanced pattern and FAM91A1 is associated with neutrophils, but the module is not predominantly blood-cell enriched. The shared bone and cell-line signal is therefore more consistent with broadly expressed cellular machinery than with a plasma-protein or strongly tissue-specific module. Cell composition or immune-cell contribution remains a possible secondary influence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only reported high-confidence STRING relationship is between SEC24C and COPB1. This is biologically coherent because SEC24C is a COPII component involved in ER-to-Golgi export, whereas COPB1 is a coatomer component involved in Golgi-to-ER and intra-Golgi transport. No hu.MAP complex contains at least two module members. The remaining co-abundance relationships are not supported by the supplied high-confidence STRING or hu.MAP evidence, so they should be interpreted as coordinated abundance relationships rather than established physical interactions. The module may connect several cellular processes without representing a single known multiprotein complex.

**STRING interactions (score >= 0.7)**: 1 of 66 gene pairs: COPB1–SEC24C (0.714)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is not established as a new biological pathway by the supplied evidence. Its genes have well-known individual functions, and the SEC24C-COPB1 relationship is already represented in STRING. The absence of a hu.MAP complex and the limited STRING connectivity suggest that the particular cross-process co-abundance pattern may be undercharacterized, but database absence cannot establish novelty. A defensible conclusion is that this may be a novel tissue-pair co-abundance signature or a recurrent expression program assembled from broadly expressed cellular machinery, rather than a newly discovered molecular complex. Independent replication, comparison with other tissue pairs, and perturbation or localization experiments would be needed to claim a new mechanism.

**Hypothesis.** Hypothesis: the module reflects a coordinated cellular stress and maintenance program in which ER and Golgi trafficking, RNA turnover, translation control, ubiquitin-mediated disposal, and cytoskeletal organization are adjusted together. SEC24C and COPB1 may mark the trafficking component, DDX6 and EIF3L the RNA and translation component, and UBE4B the protein-quality-control component. NFKB2 may provide an inducible inflammatory or stress-responsive link. The broadly expressed HPA profile is compatible with a general cellular-state program shared by bone-derived material and the cell line, while the limited immune-cell associations could reflect a secondary contribution from cell composition. This is a hypothesis, not a demonstrated causal pathway.

### Important genes

#### SEC24C

- **Related proteins** (co-abundance neighbors): DDX6 (0.83), COPB1 (0.82), EIF3L (0.81); STRING partners: COPB1 (0.714)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC24 homolog C, COPII component. The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec24p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The product of this gene may play a role in shaping the vesicle, as well as in cargo selection and concentration.…
- **Diseases (Open Targets)**: 22q11.2 deletion syndrome (0.370); neurodegenerative disease (0.369); Alzheimer disease (0.281); lysosomal storage disease (0.274); Parkinson disease (0.274)
- **Europe PMC papers**: 693
- **Why important**: SEC24C occupies a central position in the module and connects DDX6, COPB1, and EIF3L. Its established COPII role gives the module a concrete trafficking anchor: it participates in ER-to-Golgi transport, COPII cargo loading, and vesicle formation. It is also the member of the module with a reported STRING relationship to COPB1, making it important for distinguishing a biologically supported substructure from the broader co-abundance network. Its disease associations include chromosome-deletion and neurodegenerative or lysosomal disorders, and its literature coverage is substantial.
- **Conclusion**: Established evidence supports SEC24C as a core ER-export and vesicle-trafficking component and as part of the only reported STRING-supported pair. It is a plausible anchor for the module's trafficking interpretation. It is not established that SEC24C coordinates the other module processes in this tissue pair; that broader role remains a hypothesis.

#### COPB1

- **Related proteins** (co-abundance neighbors): SEC24C (0.82), AACS (0.80); STRING partners: SEC24C (0.714)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus, Vesicles, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coat protein complex I subunit beta 1. This gene encodes a protein subunit of the coatomer complex associated with non-clathrin coated vesicles. The coatomer complex, also known as the coat protein complex 1, forms in the cytoplasm and is recruited to the Golgi by activated guanosine triphosphatases. Once at the Golgi membrane, the coatomer complex may assist in the movement of protein and lipid components back to the endoplasmic retic…
- **Diseases (Open Targets)**: Baralle-Macken syndrome (0.598); Alzheimer disease (0.463); Parkinson disease (0.462); neurodegenerative disease (0.462); lysosomal storage disease (0.462)
- **Europe PMC papers**: 565
- **Why important**: COPB1 is connected to SEC24C and AACS and provides the complementary Golgi and retrograde-transport side of the trafficking interpretation. Its coatomer function supports intracellular protein and lipid transport between the Golgi and endoplasmic reticulum. The SEC24C-COPB1 relationship is the module's only reported high-confidence STRING interaction. COPB1 has disease associations involving coatomer-related developmental disease and neurodegenerative or lysosomal disorders, with a substantial literature base.
- **Conclusion**: Established evidence supports COPB1 as a coatomer component in ER-Golgi and intra-Golgi trafficking, and supports its relationship with SEC24C. Its co-abundance with the remainder of the module does not prove a shared complex or causal pathway. It is best viewed as a trafficking marker and a supported local connection.

#### DDX6

- **Related proteins** (co-abundance neighbors): SEC24C (0.83), ELAC2 (0.83), AACS (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytoplasmic bodies; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 6. This gene encodes a member of the DEAD box protein family. The protein is an RNA helicase found in P-bodies and stress granules, and functions in translation suppression and mRNA degradation. It is required for microRNA-induced gene silencing. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: intellectual developmental disorder with impaired language and dysmorphic facies (0.650); Intellectual disability (0.555); neurodegenerative disease (0.459); lung carcinoma (0.371); Global developmental delay (0.371)
- **Europe PMC papers**: 3002
- **Why important**: DDX6 has a central network position, linking SEC24C, ELAC2, and AACS. Its established role in P-bodies and stress granules connects the module to mRNA deadenylation, decapping, translation suppression, and RNA quality control. It has extensive literature coverage and disease associations involving intellectual disability, developmental delay, neurodegeneration, and cancer. Its position at the interface of the trafficking and RNA-related portions makes it particularly informative for interpreting the module as a cellular-state program rather than a single canonical pathway.
- **Conclusion**: Established evidence supports DDX6 as an RNA helicase involved in mRNA turnover, translation repression, and P-body biology. The module data support its importance as a network bridge, but do not establish that DDX6 mechanistically couples RNA decay to ER-Golgi trafficking here. That coupling is a hypothesis.

#### UBE4B

- **Related proteins** (co-abundance neighbors): AACS (0.83), KIF2A (0.82), FAM91A1 (0.81), TUBGCP3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitination factor E4B. The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes an additional conjugation factor, E4, which is involved in multi…
- **Diseases (Open Targets)**: neurodegenerative disease (0.372); atrial fibrillation (0.346); atrial flutter (0.266); alcohol drinking (0.211); Alzheimer disease (0.176)
- **Europe PMC papers**: 847
- **Why important**: UBE4B has the strongest network position in the module and connects AACS, KIF2A, FAM91A1, and TUBGCP3. Its established E4 ubiquitination activity supports multiubiquitin-chain assembly and degradation of abnormal or short-lived proteins, including roles in ER-associated degradation and proteasome-mediated quality control. It has extensive literature coverage and reported associations with neurodegenerative disease, atrial arrhythmia, and neuroblastoma biology. Its connections to trafficking and microtubule-related genes make it a strong candidate for a proteostasis-centered interpretation.
- **Conclusion**: Established evidence supports UBE4B as a protein-quality-control and ubiquitination factor with broad cellular relevance. Its network position makes it an important integrator candidate. The data do not demonstrate that UBE4B drives the module or that its ubiquitination activity directly controls the other module members.

#### NFKB2

- **Related proteins** (co-abundance neighbors): ELAC2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nuclear factor kappa B subunit 2. This gene encodes a subunit of the transcription factor complex nuclear factor-kappa-B (NFkB). The NFkB complex is expressed in numerous cell types and functions as a central activator of genes involved in inflammation and immune function. The protein encoded by this gene can function as both a transcriptional activator or repressor depending on its dimerization partner. The p100 full-length prote…
- **Diseases (Open Targets)**: immunodeficiency, common variable, 10 (0.777); common variable immunodeficiency (0.677); immunodeficiency disease (0.467); deficiency in anterior pituitary function - variable immunodeficiency syndrome (0.379); Hodgkins lymphoma (0.379)
- **Europe PMC papers**: 6369
- **Why important**: NFKB2 is the module's clearest signaling and immune-regulatory gene. It encodes an NF-kappa-B component that can act as an activator or repressor and participates in cytokine, lipopolysaccharide, and inflammatory signaling. HPA reports immune-cell enhancement, especially in neutrophils, and its disease associations prominently include common variable immunodeficiency and related immune disorders. Although it has only a peripheral network connection to ELAC2, its very extensive literature coverage and distinctive regulatory function make it important for evaluating whether an inflammatory cell-state contribution is present.
- **Conclusion**: Established evidence supports NFKB2 as an immune and inflammatory transcriptional regulator, and HPA supports a possible immune-cell contribution. Its presence does not establish that the module is an immune module, because the broader module is mostly broadly expressed and lacks global GO or KEGG enrichment. A stress- or cytokine-responsive role is plausible but remains unproven.

## Module 1

**Tissue pair**: bone and cell line  
**Genes (13)**: ABCB7, ACOT9, ATL3, COLGALT1, HK1, ITPR3, PRKDC, POLRMT, SUPT16H, XAB2, UGGT1, XPO1, XRN2

### Function

The module does not support a single strongly established pathway-level function: no GO or KEGG term passed global correction, and STRING reported no functional enrichment. Instead, it appears to be a heterogeneous cellular-maintenance module linking mitochondrial metabolism and transport, nuclear DNA and RNA processes, ER proteostasis, collagen modification, calcium signaling, and membrane or organelle organization. ACOT9 is the main network connector, linking metabolic, ER, and nuclear-associated genes, while PRKDC and XPO1 form the clearest nuclear and complex-associated axis. The appropriate interpretation is therefore coordinated co-abundance of broadly expressed cellular functions rather than a formally enriched pathway. The biological coherence is suggestive but remains hypothesis-generating.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins. HPA assigns low tissue specificity across the module, and most genes have low immune-cell specificity, arguing against a simple blood-cell module. Nevertheless, several genes show cell-type-enhanced patterns involving erythrocyte progenitors, neutrophils, monocytes, dendritic cells, and spermatid populations. COLGALT1 has a blood-cell-enriched pattern and is involved in collagen modification, while UGGT1 and COLGALT1 have intracellular or membrane-associated secretome annotations rather than clear evidence of a circulating secreted-protein program. The shared bone and cell-line signal could therefore reflect broadly expressed housekeeping or organelle functions, with possible contribution from shared cell-state or cellular-composition effects. The HPA summary provides no matching protein-detection result for either queried tissue context, so tissue-level protein validation is unavailable here.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no high-confidence pairwise interactions among the module genes and no supplementary STRING enrichment. This means the co-abundance edges should not be interpreted as established physical protein interactions. hu.MAP supplies partial support: XPO1, ABCB7, and PRKDC occur together in (hu.MAP huMAP3_09592.1); XPO1 and PRKDC occur together in (hu.MAP huMAP3_09042.1); and XPO1 and ABCB7 occur together in (hu.MAP huMAP3_06791.1). These overlaps indicate that parts of the module intersect known multiprotein complexes, especially around nuclear transport, DNA-related processes, and mitochondrial or membrane-associated functions. However, the module contains only fragments of those complexes, so hu.MAP supports selected relationships but not a unified complex interpretation.

**STRING interactions (score >= 0.7)**: 0 of 78 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09592.1 (XPO1, ABCB7, PRKDC; 3/95); huMAP3_09042.1 (XPO1, PRKDC; 2/26); huMAP3_06791.1 (XPO1, ABCB7; 2/31)

### Novelty

The co-abundance pattern may represent a new cross-compartment module, because it has no STRING-supported pairwise network and no globally significant GO or KEGG annotation. However, absence from STRING does not demonstrate novelty, and the hu.MAP overlaps show that several gene combinations are already represented in known complexes. The genes themselves also have established functions and disease associations. The defensible conclusion is that the specific conserved co-abundance organization is potentially novel, while its component biology is not. Novelty would require replication in independent bone and cell-line datasets, control for cellular composition, comparison with published co-expression modules, and experimental testing of whether the observed relationships are coordinated rather than driven by technical or cell-state effects.

**Hypothesis.** Hypothesis: the module reflects a shared cellular stress or biosynthetic-state program in which mitochondrial energy and iron or heme handling, nuclear transport and genome or RNA maintenance, and ER protein-folding or collagen-processing capacity vary together. ACOT9 may connect metabolic state to ER and nuclear-associated co-abundance, while PRKDC, XPO1, ABCB7, and their hu.MAP associations may represent coordinated demands for genome maintenance, nucleocytoplasmic transport, and mitochondrial function. HK1 and POLRMT could indicate coupling between glucose utilization and mitochondrial gene expression, whereas COLGALT1 and UGGT1 could reflect secretory-pathway or extracellular-matrix processing capacity. This is a mechanistic model, not an enrichment-supported conclusion.

### Important genes

#### ACOT9

- **Related proteins** (co-abundance neighbors): ATL3 (0.85), HK1 (0.81), COLGALT1 (0.81), PRKDC (0.80), UGGT1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA thioesterase 9. The protein encoded by this gene is a mitochondrial acyl-CoA thioesterase of unknown function. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2010].
- **Diseases (Open Targets)**: rotator cuff syndrome (0.163); shoulder impingement syndrome (0.162); hepatocellular carcinoma (0.039); laryngeal squamous cell carcinoma (0.016); neoplasm (0.013)
- **Europe PMC papers**: 322
- **Why important**: ACOT9 has the strongest network position and connects genes associated with ER organization, glucose metabolism, collagen modification, DNA repair, and protein quality control. Its annotated role in acyl-CoA and fatty-acid metabolism provides a plausible metabolic anchor for a cross-compartment module. It has disease associations involving musculoskeletal disorders and cancer, with a moderate literature base, but its molecular function is still described as incompletely characterized.
- **Conclusion**: Established evidence supports ACOT9 as the principal co-abundance connector and a mitochondrial acyl-CoA thioesterase involved in fatty-acid metabolism. Hypothesis: ACOT9 may couple metabolic flux to ER and nuclear maintenance programs in the shared module. The network does not establish direct physical interactions or prove that ACOT9 regulates the other genes.

#### PRKDC

- **Related proteins** (co-abundance neighbors): SUPT16H (0.85), XAB2 (0.83), ACOT9 (0.80), ABCB7 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09592.1, huMAP3_09042.1
- **Function (MyGene.info)**: protein kinase, DNA-activated, catalytic subunit. This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to DNA-PKcs deficiency (0.752); neurodegenerative disease (0.548); severe combined immunodeficiency (0.470); combined immunodeficiency (0.464); ovarian neoplasm (0.210)
- **Europe PMC papers**: 12461
- **Why important**: PRKDC is a highly connected nuclear gene in the module and is present in all listed hu.MAP complexes, together with XPO1 and either ABCB7 or the larger complex context. It encodes the catalytic component of DNA-dependent protein kinase and has established roles in double-strand-break repair, recombination, telomere maintenance, and innate immune signaling. Its extensive literature and strong immunodeficiency associations make it a biologically informative marker of genome-maintenance capacity.
- **Conclusion**: Established evidence supports PRKDC as a DNA-repair and genome-stability factor with support from (hu.MAP huMAP3_09592.1), (hu.MAP huMAP3_09042.1), and (hu.MAP huMAP3_06791.1). Hypothesis: its co-abundance with metabolic and organelle genes may mark a shared proliferative, stress-response, or repair state rather than a direct PRKDC-centered complex.

#### XPO1

- **Related proteins** (co-abundance neighbors): XAB2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09592.1, huMAP3_09042.1, huMAP3_06791.1
- **Function (MyGene.info)**: exportin 1. This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSe…
- **Diseases (Open Targets)**: plasma cell myeloma (0.642); B-cell chronic lymphocytic leukemia (0.626); diffuse large B-cell lymphoma (0.602); HIV infectious disease (0.561); neurodegenerative disease (0.522)
- **Europe PMC papers**: 5357
- **Why important**: XPO1 is the only gene represented in all listed hu.MAP complexes and is connected to PRKDC and XAB2 in the module. Its established function in nuclear export links RNA, protein localization, transcriptional regulation, and cell-cycle control. It has substantial literature and disease associations involving hematologic malignancies and viral infection, making it a strong candidate for interpreting the nuclear-transport component.
- **Conclusion**: Established evidence supports XPO1 as a central nuclear-export factor and a bridge across (hu.MAP huMAP3_09592.1), (hu.MAP huMAP3_09042.1), and (hu.MAP huMAP3_06791.1). Hypothesis: variation in XPO1 abundance may coordinate the nuclear and mitochondrial or membrane-associated portions of the module through changes in cargo distribution and cellular state. The module does not demonstrate that XPO1 is the causal hub.

#### HK1

- **Related proteins** (co-abundance neighbors): ITPR3 (0.81), ACOT9 (0.81), POLRMT (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hexokinase 1. Hexokinases phosphorylate glucose to produce glucose-6-phosphate, the first step in most glucose metabolism pathways. This gene encodes a ubiquitous form of hexokinase which localizes to the outer membrane of mitochondria. Mutations in this gene have been associated with hemolytic anemia due to hexokinase deficiency. Alternative splicing of this gene results in several transcript variants which en…
- **Diseases (Open Targets)**: neurodevelopmental disorder with visual defects and brain anomalies (0.757); non-spherocytic hemolytic anemia due to hexokinase deficiency (0.751); Charcot-Marie-Tooth disease type 4G (0.711); retinitis pigmentosa 79 (0.596); retinitis pigmentosa (0.496)
- **Europe PMC papers**: 51843
- **Why important**: HK1 links the module to glucose phosphorylation and mitochondrial metabolism and is connected to ITPR3 and POLRMT. Its mitochondrial localization provides a plausible interface between energy production, calcium-linked signaling, and mitochondrial gene expression. HK1 has extensive literature and established disease associations including hemolytic anemia and neurological or retinal disorders.
- **Conclusion**: Established evidence supports HK1 as a ubiquitous glycolytic enzyme associated with the mitochondrial outer membrane. Hypothesis: HK1 co-abundance may report energetic demand or mitochondrial state in the shared samples. The data do not establish a direct HK1 interaction with ITPR3 or POLRMT.

#### COLGALT1

- **Related proteins** (co-abundance neighbors): ACOT9 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen beta(1-O)galactosyltransferase 1. The protein encoded by this gene is one of two enzymes that transfers galactose moieties to hydroxylysine residues of collagen and mannose binding lectin. This gene is constitutively expressed and encodes a soluble protein that localizes to the endoplasmic reticulum. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: cerebral small vessel disease (0.733); hereditary disease (0.415); familial porencephaly (0.370); vascular dementia (0.111); neoplasm (0.085)
- **Europe PMC papers**: 309
- **Why important**: COLGALT1 contributes a biologically distinctive extracellular-matrix and ER-processing dimension. It modifies collagen and collagen-related substrates, is associated with collagen fibril organization, and shows HPA enrichment across monocyte and related myeloid populations. Its disease associations include cerebral small-vessel and vascular disorders. Although less connected than the central nuclear genes, its link to ACOT9 may be informative for a bone-associated interpretation.
- **Conclusion**: Established evidence supports COLGALT1 as an ER-localized collagen-modifying enzyme with a myeloid-enriched HPA pattern. Hypothesis: its co-abundance with ACOT9 may reflect coupling between metabolic state and matrix-processing or cellular-composition effects in bone-related samples. This does not establish a direct interaction or a bone-specific module function.

#### ABCB7

- **Related proteins** (co-abundance neighbors): PRKDC (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09592.1, huMAP3_06791.1
- **Function (MyGene.info)**: ATP binding cassette subfamily B member 7. The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily ar…
- **Diseases (Open Targets)**: X-linked sideroblastic anemia with ataxia (0.819); sideroblastic anemia (0.378); hereditary disease (0.340); spinocerebellar ataxia type 1 (0.333); mitochondrial disease (0.187)
- **Europe PMC papers**: 1100
- **Why important**: ABCB7 provides a mitochondrial iron, heme, and iron-sulfur-cluster transport perspective and is linked to PRKDC in the co-abundance graph. It appears with XPO1 and PRKDC in (hu.MAP huMAP3_09592.1) and with XPO1 in (hu.MAP huMAP3_06791.1). Its established disease association with X-linked sideroblastic anemia and ataxia makes it a strong indicator of mitochondrial hematologic biology.
- **Conclusion**: Established evidence supports ABCB7 as a mitochondrial transporter involved in heme and iron-sulfur biology, with partial complex support from (hu.MAP huMAP3_09592.1) and (hu.MAP huMAP3_06791.1). Hypothesis: ABCB7 may connect mitochondrial metabolic requirements with nuclear genome-maintenance demands in the shared module. The available evidence does not show that the module is specifically a heme-biosynthesis program.

## Module 2

**Tissue pair**: bone and cell line  
**Genes (22)**: ABCF3, CASP8, CLUH, NCAPD2, COPS3, EIF3C, HARS1, HSP90AA1, HK2, PFDN4, PAICS, RUVBL2, SMC4, FARSB, MARS1, TARS1, CCT3, CCT8, TKFC, TWF1, UBE3A, UCK2

### Function

The strongest primary signal is a broad ATP, adenyl-nucleotide, purine-ribonucleotide and nucleotide-binding program, supported by the globally corrected terms (12 globally significant GO/KEGG terms, q_global 3.82e-05–0.00708; see the table) and (GO:MF anion binding; q_global = 0.00971). This is not evidence for one single biochemical pathway, because many of the contributing proteins are enzymes or ATP-dependent molecular machines with different functions. A second, more specific signal is proteostasis and macromolecular organization: CCT3, CCT8, HSP90AA1, PFDN4 and RUVBL2 support unfolded-protein binding (GO:MF unfolded protein binding; q_global = 0.00778), while CCT3, CCT8, HSP90AA1, RUVBL2, NCAPD2 and SMC4 support chromosome organization (GO:BP positive regulation of chromosome organization; q_global = 0.000632) and (GO:BP regulation of chromosome organization; q_global = 0.0388). The CCT3/CCT8/RUVBL2 combination also supports telomerase-related RNA localization and telomere maintenance (7 globally significant GO/KEGG terms, q_global 0.015–0.0259; see the table). The cytosol term (GO:CC cytosol; q_global = 0.049) is consistent with a predominantly cytosolic, biosynthetic and proteostasis-associated module. Overall, I interpret the module as a core cellular resource program coupling ATP-dependent protein folding, translation-related nucleotide use, purine and carbohydrate metabolism, and selected nuclear chromosome-maintenance functions. The telomere and Cajal-body interpretation is more specific but rests on a smaller subset of genes than the broad nucleotide-binding signal.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the supplied protein-detection fields for the relevant tissues contain no usable matching-tissue measurements. Most genes have low tissue specificity and low immune-cell specificity, arguing against a module that is primarily explained by plasma contamination or a dominant blood-cell population. The module is nevertheless not uniformly housekeeping-like at the single-cell level: many genes are cell-type enhanced, with signals distributed across oocytes, cardiomyocytes, neutrophils, erythrocyte progenitors and spermatocyte-related cells. Tissue-enhanced examples include SMC4 and NCAPD2 in lymphoid tissue, CASP8 in bone marrow, RUVBL2 in testis, HK2 in retina and TKFC in intestine and liver. These dispersed enhancements are compatible with broadly required cellular machinery whose abundance can vary with cell state, proliferation, differentiation or sample composition. HPA protein detection cannot resolve the bone-versus-cell-line protein abundance question here because the supplied fields have no matching-tissue measurements.

**GO/KEGG enrichment**: 24 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF ATP binding | 3.82e-05 | ABCF3, CCT3, CCT8, FARSB, HARS1, HK2, HSP90AA1, MARS1, PAICS, RUVBL2, SMC4, TARS1, TKFC, TWF1, UCK2 |
| GO:MF adenyl ribonucleotide binding | 3.82e-05 | ABCF3, CCT3, CCT8, FARSB, HARS1, HK2, HSP90AA1, MARS1, PAICS, RUVBL2, SMC4, TARS1, TKFC, TWF1, UCK2 |
| GO:MF adenyl nucleotide binding | 0.000118 | ABCF3, CCT3, CCT8, FARSB, HARS1, HK2, HSP90AA1, MARS1, PAICS, RUVBL2, SMC4, TARS1, TKFC, TWF1, UCK2 |
| GO:MF purine ribonucleotide binding | 0.000438 | ABCF3, CCT3, CCT8, FARSB, HARS1, HK2, HSP90AA1, MARS1, PAICS, RUVBL2, SMC4, TARS1, TKFC, TWF1, UCK2 |
| GO:MF purine ribonucleoside triphosphate binding | 0.000438 | ABCF3, CCT3, CCT8, FARSB, HARS1, HK2, HSP90AA1, MARS1, PAICS, RUVBL2, SMC4, TARS1, TKFC, TWF1, UCK2 |
| GO:MF ribonucleotide binding | 0.000495 | ABCF3, CCT3, CCT8, FARSB, HARS1, HK2, HSP90AA1, MARS1, PAICS, RUVBL2, SMC4, TARS1, TKFC, TWF1, UCK2 |
| GO:BP positive regulation of chromosome organization | 0.000632 | CCT3, CCT8, HSP90AA1, NCAPD2, RUVBL2, SMC4 |
| GO:MF purine nucleotide binding | 0.00108 | ABCF3, CCT3, CCT8, FARSB, HARS1, HK2, HSP90AA1, MARS1, PAICS, RUVBL2, SMC4, TARS1, TKFC, TWF1, UCK2 |
| GO:MF carbohydrate derivative binding | 0.00143 | ABCF3, CCT3, CCT8, FARSB, HARS1, HK2, HSP90AA1, MARS1, PAICS, RUVBL2, SMC4, TARS1, TKFC, TWF1, UCK2 |
| GO:MF nucleotide binding | 0.00282 | ABCF3, CCT3, CCT8, FARSB, HARS1, HK2, HSP90AA1, MARS1, PAICS, RUVBL2, SMC4, TARS1, TKFC, TWF1, UCK2 |
| GO:MF nucleoside phosphate binding | 0.00341 | ABCF3, CCT3, CCT8, FARSB, HARS1, HK2, HSP90AA1, MARS1, PAICS, RUVBL2, SMC4, TARS1, TKFC, TWF1, UCK2 |
| GO:MF heterocyclic compound binding | 0.00708 | ABCF3, CCT3, CCT8, FARSB, HARS1, HK2, HSP90AA1, MARS1, PAICS, RUVBL2, SMC4, TARS1, TKFC, TWF1, UCK2 |
| GO:MF unfolded protein binding | 0.00778 | CCT3, CCT8, HSP90AA1, PFDN4, RUVBL2 |
| GO:MF anion binding | 0.00971 | ABCF3, CCT3, CCT8, FARSB, HARS1, HK2, HSP90AA1, MARS1, PAICS, RUVBL2, SMC4, TARS1, TKFC, TWF1, UCK2 |
| GO:BP positive regulation of telomere maintenance via telomerase | 0.015 | CCT3, CCT8, HSP90AA1 |

### STRING and hu.MAP

STRING supports several established relationship clusters. CCT3, CCT8, PFDN4, HSP90AA1 and RUVBL2 form a chaperone/proteostasis neighborhood, consistent with the STRING supplementary terms (STRING Function Unfolded protein binding; within-query FDR = 0.00074), (STRING NetworkNeighborAL Chaperone, and RPAP3/R2TP/prefoldin-like complex; within-query FDR = 0.0268) and (STRING NetworkNeighborAL Chaperone complex, and Prefoldin; within-query FDR = 0.0268). MARS1, HARS1, TARS1 and FARSB form an aminoacyl-tRNA-synthetase neighborhood, reflected by (5 supplementary STRING terms; within-query FDR 0.0042–0.018). NCAPD2 and SMC4 are a particularly strong condensin-related pair and are represented in multiple hu.MAP condensin complexes (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_14663.1). CCT3, CCT8 and PFDN4 co-occur in a hu.MAP complex (hu.MAP huMAP3_14584.1), while CCT3/CCT8 recur across additional hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1). TARS1 and MARS1 occur together in hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). These observations indicate that the module contains real, previously characterized protein-complex relationships, but also that its co-abundance edges are not equivalent to direct physical binding. The module appears to connect several known cellular subsystems: chaperone machinery, translation-related enzymes and chromosome-condensation machinery, with TARS1 occupying a prominent bridging position in the co-abundance graph.

**STRING interactions (score >= 0.7)**: 15 of 231 gene pairs: CCT3–CCT8 (0.999); CCT3–HSP90AA1 (0.767); CCT3–PFDN4 (0.943); CCT3–RUVBL2 (0.766); CCT8–HSP90AA1 (0.823); CCT8–PFDN4 (0.967); CCT8–RUVBL2 (0.776); FARSB–MARS1 (0.705); FARSB–TARS1 (0.735); HARS1–MARS1 (0.878); HARS1–TARS1 (0.865); HSP90AA1–RUVBL2 (0.886); MARS1–TARS1 (0.881); NCAPD2–SMC4 (0.999); PFDN4–RUVBL2 (0.756)
**STRING functional enrichment (supplementary, within-query FDR)**: Function ATP binding (FDR = 7.26e-06, 15 genes); Keyword ATP-binding (FDR = 1.55e-05, 14 genes); TISSUES Male reproductive gland (FDR = 0.0004, 17 genes); TISSUES Testis (FDR = 0.0004, 15 genes); TISSUES Internal male genital organ (FDR = 0.0004, 16 genes); Function Unfolded protein binding (FDR = 0.00074, 5 genes); TISSUES Female reproductive gland (FDR = 0.0024, 16 genes); Function Ligase activity (FDR = 0.0042, 6 genes); Function aminoacyl-tRNA ligase activity (FDR = 0.0133, 4 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 0.018, 4 genes); Keyword Ligase (FDR = 0.018, 5 genes); Keyword Protein biosynthesis (FDR = 0.018, 5 genes); Keyword Cytoplasm (FDR = 0.018, 18 genes); NetworkNeighborAL Chaperone, and RPAP3/R2TP/prefoldin-like complex (FDR = 0.0268, 5 genes); NetworkNeighborAL Chaperone complex, and Prefoldin (FDR = 0.0268, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14584.1 (CCT3, CCT8, PFDN4; 3/61); huMAP3_03084.1 (NCAPD2, SMC4; 2/8); huMAP3_14385.1 (NCAPD2, SMC4; 2/9); huMAP3_09855.1 (NCAPD2, SMC4; 2/10); huMAP3_11457.1 (NCAPD2, SMC4; 2/10); huMAP3_14663.1 (NCAPD2, SMC4; 2/14); huMAP3_02637.1 (TARS1, MARS1; 2/14); huMAP3_13688.1 (TARS1, MARS1; 2/14); huMAP3_07938.1 (CCT3, CCT8; 2/23); huMAP3_06559.1 (CCT3, CCT8; 2/25); huMAP3_09191.1 (CCT3, CCT8; 2/32); huMAP3_10656.1 (CCT3, CCT8; 2/36)

### Novelty

The data do not justify calling this a wholly new molecular complex or a newly discovered pathway. Several component relationships are already documented by high-confidence STRING associations and hu.MAP complexes, especially the CCT/prefoldin neighborhood, the aminoacyl-tRNA-synthetase neighborhood and the SMC4/NCAPD2 condensin relationship. The potentially novel observation is the reproducible co-abundance of these established subsystems in a module conserved across bone and cell line. However, conservation across the tissue pair alone does not establish disease relevance, direct molecular interaction or biological specificity. Absence of hu.MAP or STRING support for genes such as CLUH, CASP8, EIF3C or ABCF3 is not evidence of novelty, because co-abundance can arise from shared regulation, cell state or coordinated demand rather than a stable physical complex. I therefore classify the module as a potentially informative cross-context co-abundance pattern assembled from largely established cellular machinery, with novelty requiring validation in independent cohorts and perturbation or time-resolved experiments.

**Hypothesis.** Hypothesis: the module reflects a coordinated high-demand cellular state in which ATP and nucleotide availability supports protein synthesis, chaperone-assisted folding, metabolic flux and genome maintenance. Increased demand for translation and proteostasis could bring aminoacyl-tRNA synthetases, CCT/prefoldin/HSP90 machinery and nucleotide-producing enzymes into a shared abundance pattern, while proliferative or differentiation-associated states could couple the same program to condensin components and telomere-related functions. TARS1 may act as a co-abundance bridge between the translation-related cluster and the chromosome/chaperone portions of the module. This hypothesis predicts that module activity should track translational load, proteotoxic stress and cell-cycle or differentiation state, rather than representing a single discrete complex. It should be tested by independent tissue datasets, cell-composition adjustment, perturbation of chaperone or translation capacity, and direct measurement of chromosome organization and telomere-related outputs.

### Important genes

#### TARS1

- **Related proteins** (co-abundance neighbors): SMC4 (0.86), HARS1 (0.83), CCT8 (0.83), NCAPD2 (0.83), CASP8 (0.82), COPS3 (0.82), PAICS (0.81), RUVBL2 (0.81), UCK2 (0.81), FARSB (0.81), MARS1 (0.80); STRING partners: FARSB (0.735), HARS1 (0.865), MARS1 (0.881)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: threonyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Threonyl-tRNA synthetase belongs to the class-II aminoacyl-tRNA synthetase family [provided by RefSeq, Jul 2008]…
- **Diseases (Open Targets)**: trichothiodystrophy 7, nonphotosensitive (0.520); trichothiodystrophy (0.430); actinic keratosis (0.356); dyshidrosis (0.315); placental abruption (0.307)
- **Europe PMC papers**: 147
- **Why important**: TARS1 is the most connected and strongest central node in the supplied module graph and links genes from the chaperone, condensin, metabolic and apoptotic neighborhoods. It is a threonyl-tRNA synthetase with an established role in tRNA aminoacylation for translation. It contributes to the broad nucleotide-binding evidence (12 globally significant GO/KEGG terms, q_global 3.82e-05–0.00708; see the table) and (GO:MF anion binding; q_global = 0.00971), the ligase evidence (GO:MF ligase activity; q_global = 0.0472), and the cytosol evidence (GO:CC cytosol; q_global = 0.049). Its STRING relationships with MARS1, HARS1 and FARSB support a known translation-related neighborhood, while its co-abundance links to SMC4 and NCAPD2 extend beyond that neighborhood.
- **Conclusion**: Established evidence supports TARS1 as a central translation-related enzyme and a network bridge. The interpretation that it coordinates translation demand with chaperone or chromosome-maintenance activity is a hypothesis from its co-abundance position, not a demonstrated direct mechanism.

#### CCT3

- **Related proteins** (co-abundance neighbors): HSP90AA1 (0.84), SMC4 (0.82); STRING partners: CCT8 (0.999), HSP90AA1 (0.767), PFDN4 (0.943), RUVBL2 (0.766)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14584.1, huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a core chaperonin subunit with broad connectivity to CCT8, HSP90AA1 and SMC4, and it is represented in the largest set of primary terms in the module. Its established function is ATP-dependent folding of newly synthesized proteins in the CCT/TRiC complex. It contributes to unfolded-protein binding (GO:MF unfolded protein binding; q_global = 0.00778), chromosome organization (GO:BP positive regulation of chromosome organization; q_global = 0.000632) and (GO:BP regulation of chromosome organization; q_global = 0.0388), telomere and Cajal-body terms (7 globally significant GO/KEGG terms, q_global 0.015–0.0259; see the table), and the cytosol term (GO:CC cytosol; q_global = 0.049). It is supported by multiple STRING interactions and repeated hu.MAP complex assignments (hu.MAP huMAP3_14584.1) and (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1).
- **Conclusion**: Established evidence makes CCT3 a strong proteostasis anchor and supports its participation in known chaperone assemblies. Its association with telomere-related terms is statistically supported for the module, but whether CCT3 drives that function in bone or cell line cannot be inferred from co-abundance alone.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): TWF1 (0.81), TARS1 (0.81), PFDN4 (0.80); STRING partners: CCT3 (0.766), CCT8 (0.776), HSP90AA1 (0.886), PFDN4 (0.756)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 is an ATPase and DNA-helicase-related factor with established roles in DNA repair, DNA recombination, replication regulation, telomere maintenance and Cajal-body RNA processes. It contributes to many of the nucleotide-binding and chromosome-organization terms, as well as the telomerase RNA localization terms (5 globally significant GO/KEGG terms, q_global 0.015–0.0237; see the table) and (GO:BP regulation of chromosome organization; q_global = 0.0388). Its STRING links to CCT3, CCT8, HSP90AA1 and PFDN4 define a strong chaperone-associated neighborhood, and it has a relatively central bridging position within the module.
- **Conclusion**: Established evidence supports RUVBL2 as a multifunctional ATP-dependent nuclear and chaperone-associated factor. The module supports a plausible connection between proteostasis and genome-maintenance processes, but it does not establish that RUVBL2 physically assembles with every co-abundant partner in this module.

#### SMC4

- **Related proteins** (co-abundance neighbors): TARS1 (0.86), NCAPD2 (0.84), CLUH (0.82), CCT3 (0.82), HSP90AA1 (0.81); STRING partners: NCAPD2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nuclear speckles, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_03084.1, huMAP3_14385.1, huMAP3_09855.1, huMAP3_11457.1, huMAP3_14663.1
- **Function (MyGene.info)**: structural maintenance of chromosomes 4. This gene belongs to the 'structural maintenance of chromosomes' (SMC) gene family. Members of this gene family play a role in two changes in chromosome structure during mitotic segregation of chromosomes- chromosome condensation and sister chromatid cohesion. The protein encoded by this gene is likely a subunit of the 13S condensin complex, which is involved in chromosome condensation. A pseudoge…
- **Diseases (Open Targets)**: clonal hematopoiesis (0.233); bone marrow failure syndrome (0.148); hepatocellular carcinoma (0.111); central nervous system cancer (0.107); glioma (0.107)
- **Europe PMC papers**: 1967
- **Why important**: SMC4 is a condensin subunit with a direct high-confidence STRING relationship to NCAPD2 and repeated hu.MAP representation in condensin-related complexes (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_14663.1). It contributes to chromosome organization (GO:BP positive regulation of chromosome organization; q_global = 0.000632) and (GO:BP regulation of chromosome organization; q_global = 0.0388), while also connecting in the module graph to TARS1, NCAPD2, CLUH, CCT3 and HSP90AA1. Its HPA profile shows enhancement in lymphoid tissue and several progenitor or differentiating cell types, consistent with a possible contribution from proliferative or developmental state rather than a secreted or plasma origin.
- **Conclusion**: Established evidence identifies SMC4 as a chromosome-condensation factor and confirms a known condensin relationship with NCAPD2. Its links to translation and chaperone genes are best treated as a module-level coordination hypothesis, potentially reflecting cell-cycle or differentiation demand.

#### HSP90AA1

- **Related proteins** (co-abundance neighbors): CCT3 (0.84), SMC4 (0.81); STRING partners: CCT3 (0.767), CCT8 (0.823), RUVBL2 (0.886)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein 90 alpha family class A member 1. The protein encoded by this gene is an inducible molecular chaperone that functions as a homodimer. The encoded protein aids in the proper folding of specific target proteins by use of an ATPase activity that is modulated by co-chaperones. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: cancer (0.643); plasma cell myeloma (0.404); non-small cell lung carcinoma (0.394); dengue disease (0.375); Orthomyxoviridae infectious disease (0.375)
- **Europe PMC papers**: 8215
- **Why important**: HSP90AA1 is a highly studied ATP-dependent molecular chaperone with a large literature base and established roles in protein folding and stabilization. It contributes to the nucleotide-binding terms, unfolded-protein binding (GO:MF unfolded protein binding; q_global = 0.00778), chromosome organization (GO:BP positive regulation of chromosome organization; q_global = 0.000632) and (GO:BP regulation of chromosome organization; q_global = 0.0388), telomere-related terms (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 0.015), (GO:BP positive regulation of telomere maintenance; q_global = 0.0237) and (GO:BP positive regulation of telomere maintenance via telomere lengthening; q_global = 0.0259), and cytosol (GO:CC cytosol; q_global = 0.049). STRING supports relationships with CCT3, CCT8 and RUVBL2, placing it at the interface of the chaperone neighborhood and the more nuclear or genome-maintenance-associated part of the module.
- **Conclusion**: Established evidence supports HSP90AA1 as a central proteostasis regulator and a plausible integrator of client-protein stability. Its apparent connection to chromosome and telomere functions may reflect chaperoning of relevant factors or shared cellular stress, but the present data do not distinguish those mechanisms.

## Module 3

**Tissue pair**: bone and cell line  
**Genes (26)**: ACLY, RNPEP, PRMT5, AP3B1, ASNS, CAPN1, CAPN2, DYNC1H1, EXOC4, FASN, GARS1, IQGAP1, KIFBP, KNTC1, NAA15, NCKAP1, PYGB, PYGL, CAD, EPRS1, IARS1, LARS1, QARS1, RARS1, VARS1, VPS35

### Function

The strongest interpretation is a conserved protein-translation and amino-acid utilization module centered on cytosolic aminoacyl-tRNA charging. The primary evidence is the globally corrected enrichment for aminoacyl-tRNA ligase activity, tRNA aminoacylation, amino-acid activation, aminoacyl-tRNA biosynthesis, the aminoacyl-tRNA synthetase multienzyme complex, and tRNA metabolism (11 globally significant GO/KEGG terms, q_global 5.73e-05–0.0146; see the table). The synthetase genes form the clearest functional core: EPRS1, GARS1, IARS1, LARS1, QARS1, RARS1, and VARS1. Additional genes connect this core to amino-acid metabolism, nucleotide synthesis, lipid metabolism, glycogen metabolism, cytoskeletal transport, vesicle biology, and proteolysis. The extracellular-vesicle annotations (GO:CC extracellular organelle; q_global = 0.0316) (GO:CC extracellular membrane-bounded organelle; q_global = 0.0316) (GO:CC extracellular vesicle; q_global = 0.0316) provide broader cellular context but do not by themselves establish that vesicle biology is the central function. Overall, the module is best viewed as a translation-capacity and metabolic-support program, with additional transport and structural components.

**Cell composition.** The module is not dominated by plasma or secreted proteins, and it is not strongly blood-cell specific. HPA describes most genes as having low tissue specificity and low immune-cell specificity, with only limited secreted annotation. A minority of genes show tissue or cell-type enhancement, including liver, pancreas, adipose tissue, brain, bone marrow, esophageal cells, adipocytes, and platelet-associated profiles. PYGL has immune-cell enhancement in eosinophils and neutrophils, but this is insufficient to interpret the whole module as a blood-cell signal. The broad expression pattern and the presence of core translation enzymes support a housekeeping or cellular-capacity component. Because HPA has no matching protein-detection data for the bone or cell-line categories, the tissue-pair interpretation cannot be confirmed at the protein level from this resource.

**GO/KEGG enrichment**: 14 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF aminoacyl-tRNA ligase activity | 5.73e-05 | EPRS1, GARS1, IARS1, LARS1, QARS1, RARS1, VARS1 |
| GO:BP tRNA aminoacylation for protein translation | 5.73e-05 | EPRS1, GARS1, IARS1, LARS1, QARS1, RARS1, VARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 5.73e-05 | EPRS1, GARS1, IARS1, LARS1, QARS1, RARS1, VARS1 |
| GO:BP amino acid activation | 7.2e-05 | EPRS1, GARS1, IARS1, LARS1, QARS1, RARS1, VARS1 |
| GO:BP tRNA aminoacylation | 7.2e-05 | EPRS1, GARS1, IARS1, LARS1, QARS1, RARS1, VARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 7.2e-05 | EPRS1, GARS1, IARS1, LARS1, QARS1, RARS1, VARS1 |
| GO:MF ligase activity | 0.000171 | ASNS, CAD, EPRS1, GARS1, IARS1, LARS1, QARS1, RARS1, VARS1 |
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 0.000287 | EPRS1, IARS1, LARS1, QARS1, RARS1 |
| GO:BP amino acid metabolic process | 0.000843 | ASNS, CAD, EPRS1, GARS1, IARS1, LARS1, QARS1, RARS1, VARS1 |
| GO:MF catalytic activity, acting on a tRNA | 0.0026 | EPRS1, GARS1, IARS1, LARS1, QARS1, RARS1, VARS1 |
| GO:BP tRNA metabolic process | 0.0146 | EPRS1, GARS1, IARS1, LARS1, QARS1, RARS1, VARS1 |
| GO:CC extracellular organelle | 0.0316 | ACLY, AP3B1, CAD, CAPN1, CAPN2, DYNC1H1, FASN, GARS1, IARS1, IQGAP1, NCKAP1, PYGB, PYGL, RARS1, RNPEP, VPS35 |
| GO:CC extracellular membrane-bounded organelle | 0.0316 | ACLY, AP3B1, CAD, CAPN1, CAPN2, DYNC1H1, FASN, GARS1, IARS1, IQGAP1, NCKAP1, PYGB, PYGL, RARS1, RNPEP, VPS35 |
| GO:CC extracellular vesicle | 0.0316 | ACLY, AP3B1, CAD, CAPN1, CAPN2, DYNC1H1, FASN, GARS1, IARS1, IQGAP1, NCKAP1, PYGB, PYGL, RARS1, RNPEP, VPS35 |

### STRING and hu.MAP

STRING provides strong, coherent support for the aminoacyl-tRNA synthetase core. EPRS1, IARS1, LARS1, QARS1, RARS1, VARS1, and GARS1 are connected by high-confidence relationships and are enriched for aminoacyl-tRNA synthetase functions (13 supplementary STRING terms; within-query FDR 8.06e-06–0.00048). The STRING network also supports selected secondary relationships, including ACLY with FASN, ASNS with CAD, CAPN1 with CAPN2, and PYGB with PYGL. hu.MAP independently places EPRS1, IARS1, LARS1, QARS1, and RARS1 in multisynthetase-complex assemblies (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), while CAPN1 with CAPN2, CAD with FASN, and PYGL with PYGB occur in additional complexes (hu.MAP huMAP3_03767.1) (hu.MAP huMAP3_08670.1) (hu.MAP huMAP3_10103.1) (hu.MAP huMAP3_09127.1) (hu.MAP huMAP3_09328.1) (hu.MAP huMAP3_10242.1) (hu.MAP huMAP3_13615.1) (hu.MAP huMAP3_14229.1) (hu.MAP huMAP3_11557.1) (hu.MAP huMAP3_12716.1) (hu.MAP huMAP3_12926.1) (hu.MAP huMAP3_08013.1) (hu.MAP huMAP3_06909.1) (hu.MAP huMAP3_01396.1) (hu.MAP huMAP3_08093.1) (hu.MAP huMAP3_10227.1) (hu.MAP huMAP3_09760.1) (hu.MAP huMAP3_13075.1) (hu.MAP huMAP3_11993.1) (hu.MAP huMAP3_12186.1). Thus, the module contains a well-established multisynthetase component plus several smaller metabolic, proteolytic, and glycogen-related components. The network should not be interpreted as one experimentally demonstrated physical complex containing every module gene; rather, it combines a known translation complex with co-abundant cellular-support processes.

**STRING interactions (score >= 0.7)**: 28 of 325 gene pairs: ACLY–FASN (0.994); ASNS–CAD (0.945); ASNS–GARS1 (0.85); ASNS–IARS1 (0.804); CAPN1–CAPN2 (0.978); EPRS1–GARS1 (0.973); EPRS1–IARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–QARS1 (0.999); EPRS1–RARS1 (0.999); EPRS1–VARS1 (0.97); EXOC4–IQGAP1 (0.934); GARS1–IARS1 (0.97); GARS1–LARS1 (0.895); GARS1–QARS1 (0.925); GARS1–RARS1 (0.892); GARS1–VARS1 (0.86); IARS1–LARS1 (0.999); IARS1–QARS1 (0.999); IARS1–RARS1 (0.999); IARS1–VARS1 (0.9); LARS1–QARS1 (0.999); LARS1–RARS1 (0.999); LARS1–VARS1 (0.968); PYGB–PYGL (0.984); QARS1–RARS1 (0.999); QARS1–VARS1 (0.91); RARS1–VARS1 (0.905)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Aminoacyl-tRNA synthetase (FDR = 8.06e-06, 7 genes); Keyword Ligase (FDR = 8.06e-06, 9 genes); InterPro Rossmann-like alpha/beta/alpha sandwich fold (FDR = 9e-06, 7 genes); InterPro Aminoacyl-tRNA synthetase, class I, conserved site (FDR = 1.18e-05, 6 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 1.33e-05, 7 genes); RCTM Cytosolic tRNA aminoacylation (FDR = 1.55e-05, 7 genes); Function aminoacyl-tRNA ligase activity (FDR = 4.64e-05, 7 genes); Function Ligase activity (FDR = 4.64e-05, 9 genes); NetworkNeighborAL tRNA Aminoacylation, and glutamyl-tRNA(Gln) amidotransferase complex (FDR = 0.00011, 7 genes); Process tRNA aminoacylation for protein translation (FDR = 0.00022, 7 genes); NetworkNeighborAL tRNA Aminoacylation (FDR = 0.00033, 6 genes); Component aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.00042, 5 genes); Keyword Protein biosynthesis (FDR = 0.00048, 7 genes); WikiPathways Amino acid metabolism (FDR = 0.00057, 7 genes); COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.00063, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, IARS1, QARS1, RARS1, LARS1; 5/14); huMAP3_13688.1 (EPRS1, IARS1, QARS1, RARS1, LARS1; 5/14); huMAP3_03767.1 (CAPN1, CAPN2; 2/3); huMAP3_08670.1 (CAPN1, CAPN2; 2/4); huMAP3_10103.1 (CAD, FASN; 2/4); huMAP3_09127.1 (CAPN1, CAPN2; 2/5); huMAP3_09328.1 (CAPN1, CAPN2; 2/6); huMAP3_10242.1 (CAPN1, CAPN2; 2/6); huMAP3_13615.1 (CAPN1, CAPN2; 2/7); huMAP3_14229.1 (CAPN1, CAPN2; 2/7); huMAP3_11557.1 (CAPN1, CAPN2; 2/8); huMAP3_12716.1 (CAPN1, CAPN2; 2/8); huMAP3_12926.1 (CAPN1, CAPN2; 2/8); huMAP3_08013.1 (PYGL, PYGB; 2/8); huMAP3_06909.1 (PYGL, PYGB; 2/9); huMAP3_01396.1 (PYGL, PYGB; 2/10); huMAP3_08093.1 (PYGL, PYGB; 2/12); huMAP3_10227.1 (PYGL, PYGB; 2/14); huMAP3_09760.1 (PYGL, PYGB; 2/15); huMAP3_13075.1 (PYGL, PYGB; 2/15); huMAP3_11993.1 (PYGL, PYGB; 2/20); huMAP3_12186.1 (PYGL, PYGB; 2/23)

### Novelty

The aminoacyl-tRNA synthetase core is not a new biological discovery because it is supported by established STRING relationships, hu.MAP complexes, canonical annotations, and extensive literature. The exact co-abundance module shared by bone and cell line may still represent a new systems-level observation, especially because the module combines the known multisynthetase core with metabolic, transport, cytoskeletal, glycogen, and vesicle-associated genes. However, the fact sheet does not establish that this exact module has not been reported elsewhere. Absence of some genes from STRING or hu.MAP cannot prove novelty, because those resources emphasize physical interactions and curated complexes rather than tissue-pair co-abundance. The defensible conclusion is that the module-level tissue-shared organization may be novel, whereas its central molecular machinery is established.

**Hypothesis.** Hypothesis: the shared bone–cell-line module reflects coordinated cellular demand for protein synthesis and metabolic support. A multisynthetase assembly may maintain accurate tRNA charging and translation through EPRS1, IARS1, LARS1, QARS1, RARS1, VARS1, and GARS1, while ASNS, CAD, ACLY, FASN, PYGL, and PYGB help supply amino-acid, nucleotide, lipid, and carbohydrate resources. DYNC1H1, VPS35, EXOC4, AP3B1, IQGAP1, and the calpains may couple this biosynthetic state to intracellular transport, vesicle handling, cytoskeletal organization, and cellular remodeling. This is a mechanistic model rather than a demonstrated causal pathway; it should be tested by perturbing the synthetase core and measuring translation, amino-acid stress responses, metabolic flux, and module-wide co-abundance in bone-derived and cell-line samples.

### Important genes

#### EPRS1

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.87), IARS1 (0.86), RARS1 (0.85), LARS1 (0.85), VARS1 (0.83), QARS1 (0.81); STRING partners: GARS1 (0.973), IARS1 (0.999), LARS1 (0.999), QARS1 (0.999), RARS1 (0.999), VARS1 (0.97)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is a central member of the synthetase core, connects directly to the other major synthetases in the module, and belongs to both hu.MAP multisynthetase assemblies (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). It contributes to the globally supported aminoacyl-tRNA and translation terms (11 globally significant GO/KEGG terms, q_global 5.73e-05–0.0146; see the table), has a multifunctional glutamyl-prolyl charging role, and has substantial literature and disease annotation.
- **Conclusion**: Established evidence supports EPRS1 as a core translation enzyme and structural or functional anchor of the multisynthetase component. Its central position makes it a strong marker of the module, but the fact sheet does not prove that EPRS1 controls the co-abundance pattern or mediates the bone–cell-line relationship.

#### IARS1

- **Related proteins** (co-abundance neighbors): LARS1 (0.92), EPRS1 (0.86), DYNC1H1 (0.84), ACLY (0.84), CAD (0.84), RNPEP (0.83), NAA15 (0.83), VARS1 (0.82), KNTC1 (0.81), PYGL (0.81), NCKAP1 (0.80); STRING partners: ASNS (0.804), EPRS1 (0.999), GARS1 (0.97), LARS1 (0.999), QARS1 (0.999), RARS1 (0.999), VARS1 (0.9)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Isoleucine-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family and has been identified as a …
- **Diseases (Open Targets)**: growth retardation, intellectual developmental disorder, hypotonia, and hepatopathy (0.733); Abnormality of the skeletal system (0.332); microcephaly (0.289); Global developmental delay (0.289); Hallux valgus (0.184)
- **Europe PMC papers**: 184
- **Why important**: IARS1 has strong connectivity within the module, extensive STRING support with the synthetase group, membership in the hu.MAP multisynthetase assemblies (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), and annotation across the primary aminoacyl-tRNA, translation, and amino-acid metabolism terms (14 globally significant GO/KEGG terms, q_global 5.73e-05–0.0316; see the table). It also has disease associations involving developmental and skeletal abnormalities.
- **Conclusion**: Established evidence identifies IARS1 as an isoleucyl-tRNA synthetase and a core contributor to translational fidelity. Its network position supports a coordinating role within the module, while any specific role in bone biology or in the shared tissue-pair pattern remains a hypothesis.

#### LARS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.92), DYNC1H1 (0.89), EPRS1 (0.85), NAA15 (0.84), RNPEP (0.83), ACLY (0.83), PYGL (0.83), KNTC1 (0.82), RARS1 (0.82); STRING partners: EPRS1 (0.999), GARS1 (0.895), IARS1 (0.999), QARS1 (0.999), RARS1 (0.999), VARS1 (0.968)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: leucyl-tRNA synthetase 1. This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals w…
- **Diseases (Open Targets)**: infantile liver failure syndrome 1 (0.670); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.510); Global developmental delay (0.119); sensorineural hearing loss disorder (0.119); Generalized-onset seizure (0.118)
- **Europe PMC papers**: 267
- **Why important**: LARS1 is a highly connected synthetase member, appears in both hu.MAP multisynthetase assemblies (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), and is linked by STRING to the principal synthetase partners (15 supplementary STRING terms; within-query FDR 8.06e-06–0.00063). Its established functions include leucine-tRNA charging and cellular responses to amino-acid availability, making it a plausible bridge between translation and nutrient state.
- **Conclusion**: Established evidence supports LARS1 as a core enzyme connecting amino-acid sensing context with protein synthesis. Its module-level importance is well supported by network and complex evidence, but a causal nutrient-sensing mechanism in these samples is not demonstrated.

#### DYNC1H1

- **Related proteins** (co-abundance neighbors): NAA15 (0.90), LARS1 (0.89), KNTC1 (0.89), PYGL (0.88), PYGB (0.87), EPRS1 (0.87), IARS1 (0.84), ACLY (0.84), RARS1 (0.84), EXOC4 (0.83), VPS35 (0.83), CAD (0.83), IQGAP1 (0.83), CAPN2 (0.81), RNPEP (0.81), GARS1 (0.81), NCKAP1 (0.81), QARS1 (0.81), AP3B1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 1 heavy chain 1. Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polyp…
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy without contractures (0.816); intellectual disability, autosomal dominant 13 (0.815); Charcot-Marie-Tooth disease axonal type 2O (0.799); autosomal dominant non-syndromic intellectual disability (0.634); hereditary disease (0.545)
- **Europe PMC papers**: 1731
- **Why important**: DYNC1H1 has the strongest network position in the supplied module and connects the synthetase-related genes with glycogen, metabolic, vesicle, and cytoskeletal components. Its established dynein function provides a plausible intracellular transport link, and its disease associations and extensive literature make it biologically important even though it is not part of the primary synthetase enrichment.
- **Conclusion**: Established evidence supports DYNC1H1 as a cytoplasmic dynein motor involved in intracellular movement, organelle transport, and spindle-related processes. Its hub-like co-abundance position suggests coordination between translation and transport, but does not establish direct physical binding to the synthetases or a specific bone mechanism.

#### PYGL

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.88), GARS1 (0.84), LARS1 (0.83), ACLY (0.82), IARS1 (0.81), RARS1 (0.81); STRING partners: PYGB (0.984)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08013.1, huMAP3_06909.1, huMAP3_01396.1, huMAP3_08093.1, huMAP3_10227.1, huMAP3_09760.1, huMAP3_13075.1, huMAP3_11993.1, huMAP3_12186.1
- **Function (MyGene.info)**: glycogen phosphorylase L. This gene encodes a homodimeric protein that catalyses the cleavage of alpha-1,4-glucosidic bonds to release glucose-1-phosphate from liver glycogen stores. This protein switches from inactive phosphorylase B to active phosphorylase A by phosphorylation of serine residue 15. Activity of this enzyme is further regulated by multiple allosteric effectors and hormonal controls. Humans have three glyco…
- **Diseases (Open Targets)**: glycogen storage disease VI (0.821); disorder of glycogen metabolism (0.647); glycogen storage disease XV (0.596); neurodegenerative disease (0.370); Cholecystitis (0.357)
- **Europe PMC papers**: 1838
- **Why important**: PYGL connects the module to glycogen breakdown and glucose homeostasis, is linked to DYNC1H1 and several synthetase-associated genes in the co-abundance graph, and forms a supported glycogen-related pair with PYGB in STRING and hu.MAP (hu.MAP huMAP3_08013.1) (hu.MAP huMAP3_06909.1) (hu.MAP huMAP3_01396.1) (hu.MAP huMAP3_08093.1) (hu.MAP huMAP3_10227.1) (hu.MAP huMAP3_09760.1) (hu.MAP huMAP3_13075.1) (hu.MAP huMAP3_11993.1) (hu.MAP huMAP3_12186.1). Its liver and selected cell-type enrichment also highlights a possible metabolic-state contribution.
- **Conclusion**: Established evidence supports PYGL as a glycogen phosphorylase that mobilizes stored carbohydrate. Its inclusion suggests that energy availability may accompany the translation program, but the proposed coupling between glycogen mobilization and synthetase activity remains a hypothesis.

## Module 4

**Tissue pair**: bone and cell line  
**Genes (10)**: ADPGK, ATP1B3, LACTB, MCM2, MCM7, MT-ND4, PLRG1, RBM39, SFXN1, SSR1

### Function

No GO or KEGG term passed global multiple-testing correction, so there is no globally significant functional-enrichment label for this module. The network is therefore best interpreted from its genes and topology rather than from enrichment. MT-ND4 is the central co-abundance hub, connecting mitochondrial complex-I biology with genes involved in membrane transport, RNA processing, mitochondrial metabolism, DNA replication, endoplasmic-reticulum translocation, and serine transport. A distinct, biologically coherent substructure is formed by MCM2 and MCM7, which are established components of the MCM replication machinery. Overall, the module is consistent with a shared cellular-state program involving mitochondrial energy metabolism together with proliferative or genome-replication activity, but the lack of globally significant GO or KEGG enrichment makes that interpretation provisional.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only ADPGK has an intracellular-and-membrane secretome annotation, and no gene is annotated as a conventional secreted protein. It is also not broadly immune-cell specific overall, because most genes have low immune-cell specificity. Nevertheless, several genes are enhanced in bone marrow, neutrophil progenitors, neutrophils, monocytes, erythrocyte progenitors, megakaryocyte progenitors, or related hematopoietic populations. MCM2, MCM7, and RBM39 show bone-marrow enhancement, while MT-ND4, SFXN1, and other genes have tissue or cell-type enhancements outside a single lineage. This pattern raises the possibility that part of the shared signal reflects proliferating hematopoietic or progenitor-cell content, or a general cellular-state effect, rather than a bone-specific extracellular program. The tissue and cell-type annotations are mixed, with several genes having low tissue specificity, so a simple blood-contamination explanation is not established.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship, MCM2-MCM7, directly supporting the replication-related substructure. No other STRING partners or supplementary STRING enrichment terms are reported. hu.MAP independently places MCM2 and MCM7 together in every listed qualifying complex, with the remaining members including MCM3, MCM4, MCM5, MCM6, MCMBP, and, in larger assemblies, GINS, TIPIN, CLSPN, TIMELESS, and CDC45-related replication machinery. These results show that the MCM pair is a known protein-complex signal, not a newly discovered physical interaction. The remaining co-abundance links, especially the many links from MT-ND4, are not supported by reported STRING or hu.MAP relationships and may represent co-regulation, shared cellular composition, organelle state, or indirect association rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: MCM2–MCM7 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06061.1 (MCM7, MCM2; 2/5); huMAP3_05529.1 (MCM7, MCM2; 2/6); huMAP3_07113.1 (MCM7, MCM2; 2/6); huMAP3_14758.1 (MCM7, MCM2; 2/14); huMAP3_08554.1 (MCM7, MCM2; 2/15); huMAP3_11832.1 (MCM7, MCM2; 2/15); huMAP3_12180.1 (MCM7, MCM2; 2/17)

### Novelty

The module should not be presented as a wholly new molecular mechanism. The MCM2-MCM7 relationship and their participation in established replication complexes are already known, and the individual functions of the module genes are well characterized to varying degrees. What may be novel is the reproducible co-abundance configuration shared by bone and cell line, particularly the association of the MT-ND4-centered mitochondrial signal with the MCM pair and the other cellular-process genes. However, novelty at the module level cannot be established from this fact sheet alone. The lack of reported STRING or hu.MAP relationships for most edges is evidence that they are not represented in those resources, but absence from those databases does not prove that the associations are novel or direct. Independent replication, preservation analysis, and comparison with known tissue-composition or cell-cycle signatures would be needed.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular state in which mitochondrial respiratory capacity and amino-acid or metabolic transport co-vary with DNA-replication competence. MT-ND4 may act as a network-level marker of mitochondrial state, while MCM2 and MCM7 mark replication-licensed or proliferating cells. The hematopoietic and progenitor-cell annotations suggest that variation in proliferating marrow-like cell content could help generate the cross-tissue module. Under this hypothesis, the observed edges are primarily coordinated abundance relationships rather than a single physical complex. This should be tested against cell-cycle scores, mitochondrial-content measures, cell-type deconvolution, and independent bone and cell-line datasets.

### Important genes

#### MT-ND4

- **Related proteins** (co-abundance neighbors): ATP1B3 (0.91), PLRG1 (0.90), RBM39 (0.89), LACTB (0.86), MCM2 (0.85), MCM7 (0.81), SSR1 (0.81), SFXN1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH dehydrogenase subunit 4. Enables NADH dehydrogenase (ubiquinone) activity. Involved in mitochondrial electron transport, NADH to ubiquinone and mitochondrial respiratory chain complex I assembly. Part of mitochondrial respiratory chain complex I. Implicated in Leber hereditary optic neuropathy; Parkinson's disease; macular degeneration; and schizophrenia. Biomarker of Alzheimer's disease. [provided by Alliance of Genome R…
- **Diseases (Open Targets)**: MELAS syndrome (0.747); Leber hereditary optic neuropathy (0.727); mitochondrial disease (0.667); type 2 diabetes mellitus (0.610); mitochondrial complex I deficiency (0.594)
- **Europe PMC papers**: 3804
- **Why important**: MT-ND4 is the strongest network hub, linking nearly every other module member, and encodes a mitochondrial respiratory-chain complex-I subunit. Its HPA annotations include heart-muscle enhancement and several metabolically active cell types, while its disease associations include mitochondrial disorders and neurodegenerative conditions. It also has an extensive literature base. Its centrality makes it the most important marker of the module's mitochondrial component, although network centrality alone does not establish that it regulates the other genes.
- **Conclusion**: Established evidence supports MT-ND4 as a mitochondrial electron-transport gene and the principal co-abundance hub. It is plausible, but unproven, that variation in mitochondrial respiratory state drives much of the module.

#### MCM2

- **Related proteins** (co-abundance neighbors): MT-ND4 (0.85); STRING partners: MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is directly connected to MCM7 in STRING and is present with MCM7 in all qualifying hu.MAP complexes reported for this module. It is a core component of replication initiation and is linked to DNA replication, replication-initiation control, and DNA-damage-related processes. Its bone-marrow and lymphoid-tissue enhancement, together with progenitor-cell annotations, makes it informative for a proliferative or hematopoietic interpretation. It also has the largest literature base among the module genes.
- **Conclusion**: Established evidence identifies MCM2 as a replication-machinery component and a known partner of MCM7. In this module it is a strong marker of replication-competent or proliferating cell content, but the data do not show that MCM2 causes the mitochondrial associations.

#### MCM7

- **Related proteins** (co-abundance neighbors): ADPGK (0.82), MT-ND4 (0.81); STRING partners: MCM2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 forms the only reported high-confidence STRING pair with MCM2 and recurs with MCM2 across the reported hu.MAP replication complexes. It is essential to the conserved MCM replication machinery, with annotations covering replication initiation, fork-associated DNA synthesis, and DNA-damage responses. Its bone-marrow and progenitor-cell enrichment supports the same cellular-state reading as MCM2, and it has a substantial literature base.
- **Conclusion**: Established evidence supports MCM7 as a replication-complex component and confirms that the MCM substructure is biologically grounded. Its connection to the broader module is a co-abundance association whose mechanism remains unresolved.

#### SFXN1

- **Related proteins** (co-abundance neighbors): MT-ND4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sideroflexin 1. Enables D-serine transmembrane transporter activity and L-serine transmembrane transporter activity. Involved in D-serine transport; L-serine transport; and serine import into mitochondrion. Located in mitochondrion. Is integral component of mitochondrial inner membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: placental abruption (0.323); alcohol drinking (0.322); clostridium difficile infection (0.144); refractive error (0.112); scoliosis (0.111)
- **Europe PMC papers**: 568
- **Why important**: SFXN1 provides a mechanistically informative mitochondrial link beyond MT-ND4. It is an inner-mitochondrial-membrane transporter involved in serine import and related metabolic transport, is enhanced in neutrophil progenitors and basophils, and is connected to MT-ND4 in the module. Its literature volume is more limited than that of the MCM genes or MT-ND4, which makes it useful as a testable component rather than a firmly established module driver.
- **Conclusion**: Established evidence supports SFXN1 as a mitochondrial serine-transport protein with hematopoietic cell-type associations. Its co-abundance with MT-ND4 may indicate coordinated mitochondrial and one-carbon metabolic demand, but that interpretation is a hypothesis rather than a demonstrated mechanism.

## Module 5

**Tissue pair**: bone and cell line  
**Genes (16)**: ANXA7, BLVRB, CKS1B, GPS1, CSRP1, FLII, LANCL1, MAP2K3, NAMPT, PAPSS1, PCNP, PHPT1, GART, AARS1, SARS1, CCT6B

### Function

This is a weakly connected, hub-and-spoke co-abundance module centered on CCT6B, with MAP2K3 providing a small secondary link to FLII. The annotated genes span protein folding, stress and MAPK signaling, ubiquitin-dependent protein turnover, heme metabolism, NAD biosynthesis, aminoacyl-tRNA synthesis, actin remodeling, cell-cycle control, sulfation, and purine synthesis. Because the genes do not form a single strongly supported functional pathway, the most defensible interpretation is a shared cellular-state module involving proteostasis, biosynthetic capacity, stress responsiveness, and cytoskeletal or signaling activity rather than a specific pathway. No GO or KEGG term passed global correction; therefore there is no globally significant pathway annotation for this module. The absence of a corrected enrichment term does not invalidate the co-abundance pattern.

**Cell composition.** The module is predominantly composed of intracellular proteins rather than plasma or secreted proteins. Only NAMPT is annotated as secreted to blood, so the module is not mostly a secreted-protein module. HPA indicates generally broad or mixed expression: many genes have low tissue specificity, while tissue-enhanced signals occur in bone marrow, skeletal muscle, blood vessel, intestine, lymphoid tissue, brain, and testis, with CCT6B tissue enriched in testis. Cell-type-enhanced signals are frequent and include reproductive, epithelial, muscle, erythroid, megakaryocytic, and neural cell types. HPA blood-cell specificity is low for most genes, although NAMPT is immune-cell enriched in neutrophils, BLVRB is immune-cell enhanced in classical monocytes, and PAPSS1 has group-enriched signals in basophils and eosinophils. Thus, the module does not look primarily like a blood-cell or plasma-protein signature, but some contribution from shared cell types, marrow-associated cells, erythroid cells, or sample composition remains plausible. HPA reports no matched bone or cell-line protein-detection result for any module gene, so tissue-level protein validation is unavailable here.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only one high-confidence relationship within the module: AARS1 with SARS1. This is biologically coherent because both genes encode aminoacyl-tRNA synthetases involved in translation-related processes, but it is insufficient to establish a densely interacting module. hu.MAP identifies one complex containing two module members, BLVRB and AARS1 (hu.MAP huMAP3_14442.1). The remaining listed complex members are outside the module, so this result supports limited membership in a broader multiprotein assembly rather than a module-specific complex. The sparse STRING and hu.MAP support, together with the star-like co-abundance topology around CCT6B, suggests that the observed relationships are more likely to reflect coordinated abundance or shared cellular state than extensive direct physical interaction. There is no STRING functional-enrichment result for the module.

**STRING interactions (score >= 0.7)**: 1 of 120 gene pairs: AARS1–SARS1 (0.881)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (BLVRB, AARS1; 2/57)

### Novelty

The co-abundance module may represent a new cross-tissue association pattern, but the fact sheet does not establish it as a new biological mechanism. The limited overlap with known STRING and hu.MAP relationships means that much of the module-level organization is not represented by those resources, yet absence from interaction databases alone cannot prove novelty. Several individual genes and functions are already well established, including CCT6B in chaperonin-mediated folding, MAP2K3 in stress-activated MAPK signaling, NAMPT in NAD biosynthesis, AARS1 and SARS1 in translation, and BLVRB in heme metabolism. A defensible novelty claim is therefore restricted to the reproducible co-abundance configuration shared by bone and cell line, pending validation in independent cohorts, perturbation experiments, and protein-level measurements.

**Hypothesis.** Hypothesis: the module reflects a coordinated intracellular adaptation state in which chaperone capacity, translation, NAD production, heme handling, nucleotide synthesis, cytoskeletal remodeling, and stress signaling vary together. CCT6B may act as the abundance hub because its chaperonin function is compatible with broad coordination of protein homeostasis, while MAP2K3 and FLII may connect stress signaling with actin remodeling. NAMPT could couple metabolic or inflammatory state to cellular energy and redox capacity, and the AARS1-SARS1 relationship could mark translational demand. This is a hypothesis about shared cellular state, not proof that these proteins physically regulate one another or form a single biochemical pathway.

### Important genes

#### CCT6B

- **Related proteins** (co-abundance neighbors): MAP2K3 (0.95), PCNP (0.92), GPS1 (0.92), BLVRB (0.90), ANXA7 (0.87), NAMPT (0.87), CSRP1 (0.87), CKS1B (0.86), PHPT1 (0.85), PAPSS1 (0.85), GART (0.84), SARS1 (0.82), LANCL1 (0.81), AARS1 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 6B. This gene encodes a molecular chaperone that is a member of the chaperonin-containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: neurodegenerative disease (0.537); hypertrophic cardiomyopathy (0.177); brain cancer (0.134); systemic lupus erythematosus (0.119); nervous system cancer (0.107)
- **Europe PMC papers**: 246
- **Why important**: CCT6B is the dominant network hub, with the greatest degree and weighted strength in the module. Its established function is as a subunit of the CCT or TRiC chaperonin complex that folds proteins including actin and tubulin. It therefore provides the strongest functional anchor for interpreting the module as related to proteostasis and structural-protein handling. Its tissue-enriched testis and several germ-cell-associated HPA signals indicate that cell-state composition could influence its abundance. The disease-association and literature records show broad prior study, so this is an established and heavily investigated gene rather than a novel annotation.
- **Conclusion**: Established evidence supports CCT6B as the central co-abundance hub and a protein-folding factor. It is reasonable to hypothesize that it organizes the module at the level of shared cellular state, but the network does not demonstrate direct physical control of the other genes by CCT6B.

#### MAP2K3

- **Related proteins** (co-abundance neighbors): CCT6B (0.95), FLII (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitogen-activated protein kinase kinase 3. The protein encoded by this gene is a dual specificity protein kinase that belongs to the MAP kinase kinase family. This kinase is activated by mitogenic and environmental stress, and participates in the MAP kinase-mediated signaling cascade. It phosphorylates and thus activates MAPK14/p38-MAPK. This kinase can be activated by insulin, and is necessary for the expression of glucose transporter. Ex…
- **Diseases (Open Targets)**: neurodegenerative disease (0.456); Abnormality of the skeletal system (0.425); autoimmune disorder of central nervous system (0.370); anthrax infection (0.370); vein disorder (0.319)
- **Europe PMC papers**: 2140
- **Why important**: MAP2K3 is the principal non-hub connector beyond the CCT6B-centered spoke pattern, linking CCT6B to FLII. It encodes a dual-specificity kinase involved in stress-activated MAPK signaling and activation of p38 MAPK, with additional roles reported in glucose-transporter expression and responses to ischemia. HPA marks it as tissue enhanced in bone marrow and cell-type enhanced in erythrocytes and neutrophils, which is relevant to the shared bone and cell-line context. It has substantial literature and disease-association support.
- **Conclusion**: Established evidence supports MAP2K3 as a stress-signaling component that could connect cellular state to the module. Its placement does not prove that MAP2K3 drives the module, and any connection to CCT6B or FLII beyond co-abundance remains a hypothesis.

#### NAMPT

- **Related proteins** (co-abundance neighbors): CCT6B (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nicotinamide phosphoribosyltransferase. This gene encodes a protein that catalyzes the condensation of nicotinamide with 5-phosphoribosyl-1-pyrophosphate to yield nicotinamide mononucleotide, one step in the biosynthesis of nicotinamide adenine dinucleotide. The protein belongs to the nicotinic acid phosphoribosyltransferase (NAPRTase) family and is thought to be involved in many important biological processes, including metabolism, str…
- **Diseases (Open Targets)**: neurodegenerative disease (0.322); asthma (0.259); esophageal squamous cell carcinoma (0.174); Genu varum (0.172); Genu valgum (0.172)
- **Europe PMC papers**: 8350
- **Why important**: NAMPT is a high-literature gene with a central metabolic function in NAD biosynthesis and additional reported roles in stress response, inflammation, signaling, and cell proliferation. It is the only module gene annotated as secreted to blood and is HPA tissue enhanced in lymphoid tissue and cell-type enriched in neutrophils. These features make NAMPT especially informative for distinguishing an intracellular metabolic program from a possible inflammatory or sample-composition contribution.
- **Conclusion**: Established evidence supports NAMPT as a metabolic and stress-response marker with a plausible extracellular inflammatory component. Its co-abundance with the module is consistent with coordinated metabolic state, but the data do not establish that secreted NAMPT mediates the module or that neutrophils account for the shared signal.

#### AARS1

- **Related proteins** (co-abundance neighbors): CCT6B (0.80); STRING partners: SARS1 (0.881)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: alanyl-tRNA synthetase 1. The human alanyl-tRNA synthetase (AARS) belongs to a family of tRNA synthases, of the class II enzymes.  Class II tRNA synthases evolved early in evolution and are highly conserved. This is reflected by the fact that 498 of the 968-residue polypeptide human AARS shares 41% identity witht the E.coli protein.  tRNA synthases are the enzymes that interpret the RNA code and attach specific aminoacids …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2N (0.762); developmental and epileptic encephalopathy, 29 (0.747); undetermined early-onset epileptic encephalopathy (0.678); trichothiodystrophy 8, nonphotosensitive (0.568); Charcot-Marie-Tooth disease type 2 (0.566)
- **Europe PMC papers**: 672
- **Why important**: AARS1 is an aminoacyl-tRNA synthetase required for alanyl-tRNA charging and translation, and it has a direct high-confidence STRING relationship with SARS1, another aminoacyl-tRNA synthetase. AARS1 also participates in the hu.MAP complex represented by (hu.MAP huMAP3_14442.1) through its pairing with BLVRB in the module. Its disease associations include inherited neurological disorders, and its literature base is substantial. The combination of a coherent translation function and the strongest known STRING relationship in the module makes it important despite its peripheral network position.
- **Conclusion**: Established evidence supports AARS1 as a translation-related component and as part of the best-supported known interaction pair in the module. The AARS1-SARS1 relationship supports translational coordination, but it does not establish a larger translation complex comprising the full module.

#### SARS1

- **Related proteins** (co-abundance neighbors): CCT6B (0.82); STRING partners: AARS1 (0.881)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: seryl-tRNA synthetase 1. This gene belongs to the class II amino-acyl tRNA family. The encoded enzyme catalyzes the transfer of L-serine to tRNA (Ser) and is related to bacterial and yeast counterparts. Multiple alternatively spliced transcript variants have been described but the biological validity of all variants is unknown. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, ataxia, and seizures (0.670); autosomal recessive non-syndromic intellectual disability (0.370); autosomal recessive primary microcephaly (0.370); arteriovenous malformations of the brain (0.340); hereditary peripheral neuropathy (0.118)
- **Europe PMC papers**: 400
- **Why important**: SARS1 encodes seryl-tRNA synthetase and is functionally related to AARS1 through aminoacyl-tRNA biology. It is the partner in the sole high-confidence STRING interaction within the module, making it important for interpreting the small amount of externally validated network structure. Its annotations include cytoplasmic translation, tRNA modification, and selenium-related processes, and its disease associations include neurodevelopmental and neurological disorders.
- **Conclusion**: Established evidence supports SARS1 as a translation and tRNA-related enzyme and validates the AARS1-SARS1 edge as a known relationship. Its role in the broader module is still inferential because the remaining module edges are not supported by high-confidence STRING interactions.

#### BLVRB

- **Related proteins** (co-abundance neighbors): CCT6B (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: biliverdin reductase B. The final step in heme metabolism in mammals is catalyzed by the cytosolic biliverdin reductase enzymes A and B (EC 1.3.1.24).[supplied by OMIM, Jul 2009]
- **Diseases (Open Targets)**: neurodegenerative disease (0.125); hepatocellular carcinoma (0.076); cholangiocarcinoma (0.074); ischemic stroke (0.055); neonatal intrahepatic cholestasis due to citrin deficiency (0.045)
- **Europe PMC papers**: 1322
- **Why important**: BLVRB is a bone-marrow-enhanced gene with erythroid and monocyte-associated HPA signals and an established role in the final step of mammalian biliverdin reduction and heme metabolism. It is also the second module member in the hu.MAP complex represented by (hu.MAP huMAP3_14442.1), together with AARS1. Its localization in the cytosol and its marrow and erythroid associations make it relevant to possible sample cell-type effects in bone-related material.
- **Conclusion**: Established evidence supports BLVRB as a heme-metabolism enzyme and as a limited hu.MAP-supported complex member. Its presence may reflect erythroid or marrow-related cellular state, but the data do not show that heme metabolism is the defining function of the entire module.

## Module 6

**Tissue pair**: bone and cell line  
**Genes (18)**: AQR, CHD4, DDX21, DDX24, DHX9, NOL6, NUP155, NUP93, PHIP, POLR1A, POLR1B, POLR2A, LARS2, THOC2, TOP2A, SNRNP200, VIRMA, WDR18

### Function

This is a conserved nuclear gene-expression module centered on RNA metabolism, RNA processing, RNA helicase activity, transcription, and nucleocytoplasmic RNA transport. The primary evidence is strong: RNA metabolic process and nucleic-acid metabolic process are supported by (GO:BP RNA metabolic process; q_global = 3.99e-05) and (GO:BP nucleic acid metabolic process; q_global = 0.000321), while catalytic activity acting on nucleic acid and RNA is supported by (GO:MF catalytic activity, acting on a nucleic acid; q_global = 6.79e-05) and (GO:MF catalytic activity, acting on RNA; q_global = 0.000398). The module also contains a coherent RNA-helicase signal (GO:MF RNA helicase activity; q_global = 0.0038), RNA export and nuclear-export signals (GO:BP RNA export from nucleus; q_global = 0.0038) and (GO:BP nuclear export; q_global = 0.0263), and RNA transport signals (GO:BP nucleic acid transport; q_global = 0.0494), (GO:BP RNA transport; q_global = 0.0494) and (GO:BP establishment of RNA localization; q_global = 0.0494). The presence of RNA polymerase components, spliceosome-associated proteins, nucleolar RNA-processing proteins, nuclear pore proteins, and chromatin regulators indicates that this is not a single narrow pathway. Rather, it represents coordinated activity across transcription, RNA maturation, ribosome-related RNA processing, nuclear export, and chromatin or DNA topology management. The broad gene-expression term (GO:BP gene expression; q_global = 0.00356) and nuclear-complex term (GO:CC nuclear protein-containing complex; q_global = 0.00857) support this interpretation. The unusual terms referring to polymerase IV, polymerase V, plastid transcription, and mitochondrial transcription should not be treated as evidence for plant or plastid biology in this human module; they appear to be broad or imperfectly transferable ontology annotations. STRING enrichment is concordant but supplementary, especially for nucleic-acid catalysis (STRING Function Catalytic activity, acting on a nucleic acid; within-query FDR = 6.67e-06), RNA metabolism (STRING Process RNA metabolic process; within-query FDR = 0.00013), nuclear complexes (STRING Component Nuclear protein-containing complex; within-query FDR = 0.0002), and helicases (STRING Keyword Helicase; within-query FDR = 0.00088) through (STRING Function RNA helicase activity; within-query FDR = 0.00097).

**Cell composition.** The module is overwhelmingly composed of intracellular, broadly expressed nuclear or nucleolar proteins rather than plasma or secreted proteins. The HPA summary reports no secreted genes, predominantly low tissue specificity, predominantly low immune-cell specificity, and no compelling blood-cell signature. Therefore, the shared bone and cell-line module is unlikely to be explained primarily by plasma contamination, secreted proteins, or a blood-cell-enriched population. Its broad expression profile is consistent with housekeeping-type gene-expression machinery, although several genes show cell-type enhancement in reproductive, neural, epithelial, or lymphoid contexts. HPA protein detection for the matched bone and cell-line tissues is unavailable, so tissue-level protein abundance cannot be independently confirmed from that resource. The conservation between bone and cell line is therefore most plausibly related to shared cellular machinery or shared proliferative and transcriptional state, rather than a bone-specific extracellular function.

**GO/KEGG enrichment**: 28 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA metabolic process | 3.99e-05 | AQR, CHD4, DDX21, DDX24, DHX9, LARS2, NOL6, NUP155, PHIP, POLR1A, POLR1B, POLR2A, SNRNP200, THOC2, TOP2A, VIRMA, WDR18 |
| GO:MF catalytic activity, acting on a nucleic acid | 6.79e-05 | AQR, CHD4, DDX21, DDX24, DHX9, LARS2, POLR1A, POLR1B, POLR2A, SNRNP200, TOP2A |
| GO:BP nucleic acid metabolic process | 0.000321 | AQR, CHD4, DDX21, DDX24, DHX9, LARS2, NOL6, NUP155, PHIP, POLR1A, POLR1B, POLR2A, SNRNP200, THOC2, TOP2A, VIRMA, WDR18 |
| GO:MF catalytic activity, acting on RNA | 0.000398 | AQR, DDX21, DDX24, DHX9, LARS2, POLR1A, POLR1B, POLR2A, SNRNP200 |
| GO:MF nucleic acid conformation isomerase activity | 0.000551 | AQR, CHD4, DDX21, DDX24, DHX9, SNRNP200, TOP2A |
| GO:BP RNA biosynthetic process | 0.00147 | AQR, CHD4, DDX21, DHX9, NOL6, NUP155, PHIP, POLR1A, POLR1B, POLR2A, SNRNP200, THOC2, TOP2A, VIRMA, WDR18 |
| GO:BP nucleic acid biosynthetic process | 0.00237 | AQR, CHD4, DDX21, DHX9, NOL6, NUP155, PHIP, POLR1A, POLR1B, POLR2A, SNRNP200, THOC2, TOP2A, VIRMA, WDR18 |
| GO:BP gene expression | 0.00356 | AQR, CHD4, DDX21, DHX9, LARS2, NOL6, NUP155, NUP93, PHIP, POLR1A, POLR1B, POLR2A, SNRNP200, THOC2, TOP2A, VIRMA, WDR18 |
| GO:MF RNA helicase activity | 0.0038 | AQR, DDX21, DDX24, DHX9, SNRNP200 |
| GO:BP RNA export from nucleus | 0.0038 | DHX9, NOL6, NUP155, NUP93, THOC2 |
| GO:MF ATP-dependent activity, acting on RNA | 0.0038 | AQR, DDX21, DDX24, DHX9, SNRNP200 |
| GO:BP nucleobase-containing compound metabolic process | 0.00382 | AQR, CHD4, DDX21, DDX24, DHX9, LARS2, NOL6, NUP155, PHIP, POLR1A, POLR1B, POLR2A, SNRNP200, THOC2, TOP2A, VIRMA, WDR18 |
| GO:MF macromolecular conformation isomerase activity | 0.00441 | AQR, CHD4, DDX21, DDX24, DHX9, SNRNP200, TOP2A |
| GO:MF helicase activity | 0.00555 | AQR, CHD4, DDX21, DDX24, DHX9, SNRNP200 |
| GO:BP transcription by RNA polymerase III | 0.00617 | DDX21, POLR1A, POLR1B, POLR2A |

### STRING and hu.MAP

The network contains several established relationships. AQR and SNRNP200 have a very strong STRING relationship, consistent with spliceosomal machinery, and these genes co-occur in multiple hu.MAP spliceosome-related complexes (hu.MAP huMAP3_06726.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1) and (hu.MAP huMAP3_09945.1). NUP155 and NUP93 form a strong nuclear-pore relationship, supporting the RNA-export interpretation. POLR1A and POLR1B are tightly linked, and POLR1B connects to POLR2A; these polymerase relationships are also reflected in several hu.MAP complexes containing POLR1A, POLR1B and POLR2A (hu.MAP huMAP3_08487.1) through (hu.MAP huMAP3_11092.1), as well as additional polymerase complexes (hu.MAP huMAP3_00807.1) and (hu.MAP huMAP3_09057.1). NOL6 connects to POLR1A, POLR1B and WDR18, consistent with nucleolar and ribosome-biogenesis functions. DDX21, DDX24 and DHX9 form a connected helicase and RNA-processing neighborhood, while CHD4 connects to TOP2A and to other chromatin or transcription-related members. PHIP and TOP2A occur together in hu.MAP complex (hu.MAP huMAP3_07289.1). These findings show that a substantial part of the module recapitulates known molecular machinery rather than representing unsupported associations. At the same time, several module edges have no reported hu.MAP complex support or no listed STRING partner, so the co-abundance structure extends beyond currently catalogued physical complexes.

**STRING interactions (score >= 0.7)**: 15 of 153 gene pairs: AQR–SNRNP200 (0.994); CHD4–TOP2A (0.715); DDX21–DDX24 (0.706); DDX21–DHX9 (0.908); DDX21–POLR1A (0.786); DDX21–POLR1B (0.741); DDX24–NOL6 (0.771); DHX9–POLR2A (0.781); DHX9–SNRNP200 (0.784); NOL6–POLR1A (0.938); NOL6–POLR1B (0.962); NOL6–WDR18 (0.773); NUP155–NUP93 (0.999); POLR1A–POLR1B (0.999); POLR1B–POLR2A (0.826)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Catalytic activity, acting on a nucleic acid (FDR = 6.67e-06, 11 genes); Function Catalytic activity, acting on RNA (FDR = 5.18e-05, 9 genes); Process RNA metabolic process (FDR = 0.00013, 14 genes); Process Nucleic acid metabolic process (FDR = 0.0002, 15 genes); Component Nuclear protein-containing complex (FDR = 0.0002, 12 genes); Keyword Helicase (FDR = 0.00088, 6 genes); Function Helicase activity (FDR = 0.00089, 6 genes); Function RNA helicase activity (FDR = 0.00097, 5 genes); Process Gene expression (FDR = 0.0012, 14 genes); Keyword Nucleus (FDR = 0.0024, 16 genes); COMPARTMENTS Nucleus (FDR = 0.0025, 17 genes); SMART DEAD-like helicases superfamily (FDR = 0.0031, 5 genes); SMART Helicase superfamily c-terminal domain (FDR = 0.0031, 5 genes); RCTM Metabolism of RNA (FDR = 0.0043, 10 genes); Process Macromolecule metabolic process (FDR = 0.0045, 17 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08487.1 (POLR1A, POLR2A, POLR1B; 3/37); huMAP3_06426.1 (POLR1A, POLR2A, POLR1B; 3/38); huMAP3_14318.1 (POLR1A, POLR2A, POLR1B; 3/58); huMAP3_11092.1 (POLR1A, POLR2A, POLR1B; 3/65); huMAP3_07289.1 (TOP2A, PHIP; 2/4); huMAP3_00807.1 (POLR1A, POLR1B; 2/30); huMAP3_09057.1 (POLR1A, POLR1B; 2/36); huMAP3_06726.1 (AQR, SNRNP200; 2/37); huMAP3_08501.1 (AQR, SNRNP200; 2/47); huMAP3_09504.1 (AQR, SNRNP200; 2/51); huMAP3_09945.1 (AQR, SNRNP200; 2/61); huMAP3_09943.1 (VIRMA, THOC2; 2/78)

### Novelty

The module should not be claimed as a newly discovered molecular complex. Many of its central relationships are established spliceosomal, RNA-polymerase, nucleolar, nuclear-pore, and chromatin-associated relationships, as shown by STRING and hu.MAP. Absence of a relationship from either database would not establish novelty because database coverage is incomplete and co-abundance does not require direct physical binding. The potentially novel aspect is the conserved co-abundance pattern across bone and cell line, particularly the coordinated combination of transcription, RNA helicases, spliceosome-associated factors, nuclear export, nucleolar processing, and chromatin or DNA-topology proteins. That observation is a systems-level association rather than proof of a new biochemical pathway. It would require independent validation across additional cohorts, assessment of cell composition and proliferation, perturbation experiments, and testing of whether the module tracks a specific cellular state before being described as a new biological mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared high-throughput nuclear gene-expression state in which transcriptional activity is coupled to RNA maturation, spliceosome function, nucleolar RNA processing, and export through the nuclear pore. In this model, POLR1A, POLR1B and POLR2A represent transcriptional output; AQR, SNRNP200, DHX9, DDX21 and DDX24 support RNA remodeling and splicing; NOL6 and WDR18 support nucleolar RNA processing; and NUP93 and NUP155 support movement of RNA and proteins across the nuclear envelope. CHD4, TOP2A and PHIP may connect this RNA-processing state to chromatin organization, DNA topology, and cell-state regulation. The conserved bone and cell-line signal could therefore arise from shared transcriptional and proliferative demands or from a common nuclear housekeeping program. This remains a hypothesis because co-abundance does not establish directionality, direct binding, or causal coordination.

### Important genes

#### SNRNP200

- **Related proteins** (co-abundance neighbors): POLR2A (0.88), DHX9 (0.88), PHIP (0.84), POLR1B (0.83), THOC2 (0.82), TOP2A (0.81), NUP93 (0.81); STRING partners: AQR (0.994), DHX9 (0.784)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06726.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is the most highly connected module member and has a strong relationship with AQR in STRING. It is a core U5 snRNP and spliceosomal helicase component, appears in many primary enrichment terms including RNA metabolism, RNA helicase activity, RNA processing and nuclear-complex terms, and is represented in several hu.MAP spliceosome complexes (hu.MAP huMAP3_06726.1) through (hu.MAP huMAP3_09945.1). Its disease associations include retinal degeneration, and its substantial literature support makes it a strong anchor for the established RNA-splicing interpretation.
- **Conclusion**: Established evidence supports SNRNP200 as a central spliceosome-associated RNA helicase and a major network anchor. Its module position is consistent with coordination between RNA splicing and broader RNA metabolism. A role as the causal driver of the cross-tissue module is not established and remains a hypothesis.

#### DHX9

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.88), POLR1B (0.85), AQR (0.81), PHIP (0.81), WDR18 (0.80); STRING partners: DDX21 (0.908), POLR2A (0.781), SNRNP200 (0.784)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 has a strong network position and connects to SNRNP200, AQR, PHIP, WDR18 and POLR2A. It is an ATP-dependent RNA and DNA-RNA helicase with reported roles in transcriptional regulation, RNA processing and nuclear export, and it appears in the RNA-helicase, RNA-export, nucleic-acid transport and gene-expression terms (GO:MF RNA helicase activity; q_global = 0.0038), (GO:BP RNA export from nucleus; q_global = 0.0038), (GO:BP nuclear export; q_global = 0.0263), (GO:BP nucleic acid transport; q_global = 0.0494), (GO:BP RNA transport; q_global = 0.0494) and (GO:BP establishment of RNA localization; q_global = 0.0494). It also has extensive literature support and disease associations involving neurodevelopmental and neurodegenerative phenotypes.
- **Conclusion**: Established evidence supports DHX9 as a plausible bridge between RNA remodeling, transcription and export within the module. Its network placement makes it an important integrator, but the data do not show that DHX9 drives the conserved co-abundance pattern or that it specifically mediates bone biology.

#### POLR2A

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.88), NUP93 (0.86), POLR1A (0.81); STRING partners: DHX9 (0.781), POLR1B (0.826)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08487.1, huMAP3_06426.1, huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase II subunit A. This gene encodes the largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene contains a carboxy terminal domain composed of heptapeptide repeats that are essential for polymerase activity. These repeats contain serine and threonine residues that are phosphorylated in actively transcribing RNA polymerase. In addition, …
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and variable intellectual and behavioral abnormalities (0.738); HIV infectious disease (0.600); hereditary disease (0.479); syndromic intellectual disability (0.462); Orthomyxoviridae infectious disease (0.374)
- **Europe PMC papers**: 4546
- **Why important**: POLR2A is the largest subunit of RNA polymerase II and is directly linked in the module to SNRNP200, NUP93 and POLR1A. It contributes to the globally supported terms for RNA metabolism, RNA biosynthesis, gene expression, nucleic-acid catalysis and polymerase-related transcription (GO:BP RNA metabolic process; q_global = 3.99e-05), (GO:MF catalytic activity, acting on a nucleic acid; q_global = 6.79e-05), (GO:BP RNA biosynthetic process; q_global = 0.00147), (GO:BP gene expression; q_global = 0.00356) and (GO:BP transcription by RNA polymerase III; q_global = 0.00617). It is also present in multiple hu.MAP polymerase complexes (hu.MAP huMAP3_08487.1) through (hu.MAP huMAP3_11092.1), and it has substantial literature and disease-association support.
- **Conclusion**: Established evidence identifies POLR2A as a transcriptional core component that connects polymerase activity with RNA processing and nuclear transport. Its presence supports a general nuclear gene-expression program rather than a tissue-specific bone mechanism. The module does not establish altered polymerase activity or a disease-specific POLR2A process.

#### POLR1B

- **Related proteins** (co-abundance neighbors): DHX9 (0.85), SNRNP200 (0.83), CHD4 (0.82); STRING partners: DDX21 (0.741), NOL6 (0.962), POLR1A (0.999), POLR2A (0.826)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08487.1, huMAP3_06426.1, huMAP3_14318.1, huMAP3_11092.1, huMAP3_00807.1, huMAP3_09057.1
- **Function (MyGene.info)**: RNA polymerase I subunit B. Eukaryotic RNA polymerase I (pol I) is responsible for the transcription of ribosomal RNA (rRNA) genes and production of rRNA, the primary component of ribosomes. Pol I is a multisubunit enzyme composed of 6 to 14 polypeptides, depending on the species. Most of the mass of the pol I complex derives from the 2 largest subunits, Rpa1 and Rpa2 in yeast. POLR1B is homologous to Rpa2 (Seither and Grumm…
- **Diseases (Open Targets)**: Treacher Collins syndrome 4 (0.751); Treacher-Collins syndrome (0.383); arthropathy (0.212); Chronic Obstructive Asthma (0.188); lower respiratory tract disorder (0.124)
- **Europe PMC papers**: 521
- **Why important**: POLR1B is a major RNA polymerase I subunit involved in ribosomal RNA transcription. It has a strong relationship with POLR1A and links to DHX9, SNRNP200, CHD4 and POLR2A. It is included in the globally supported transcription, RNA-biosynthetic, nucleic-acid-catalytic and nuclear-complex terms, and it recurs in multiple hu.MAP polymerase complexes (hu.MAP huMAP3_08487.1) through (hu.MAP huMAP3_11092.1), (hu.MAP huMAP3_00807.1) and (hu.MAP huMAP3_09057.1). Its disease associations include Treacher Collins syndrome and related craniofacial phenotypes, which are relevant to skeletal and developmental interpretation.
- **Conclusion**: Established evidence supports POLR1B as a nucleolar transcription component linking ribosomal RNA production to the broader module. Its presence suggests that the conserved signal includes ribosome-biogenesis demand, not only messenger-RNA processing. A direct role in the bone-cell conservation remains unproven.

#### AQR

- **Related proteins** (co-abundance neighbors): DHX9 (0.81), THOC2 (0.80); STRING partners: SNRNP200 (0.994)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06726.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: aquarius intron-binding spliceosomal factor. Enables 3'-5' RNA helicase activity and single-stranded RNA binding activity. Involved in mRNA splicing, via spliceosome. Located in nucleoplasm. Part of U2-type catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dengue disease (0.370); preeclampsia (0.191); male reproductive organ cancer (0.152); poisoning (0.126); drug allergy (0.126)
- **Europe PMC papers**: 1166
- **Why important**: AQR is a spliceosomal intron-binding factor with RNA-helicase activity and is one of the strongest functional anchors of the module. It connects to DHX9 and THOC2 in the co-abundance network, has a very strong STRING relationship with SNRNP200, and co-occurs with SNRNP200 in several hu.MAP spliceosome complexes (hu.MAP huMAP3_06726.1) through (hu.MAP huMAP3_09945.1). It contributes to the primary terms for RNA metabolism, RNA catalysis, helicase activity, nuclear complexes and gene expression (GO:BP RNA metabolic process; q_global = 3.99e-05), (GO:MF catalytic activity, acting on a nucleic acid; q_global = 6.79e-05), (GO:MF catalytic activity, acting on RNA; q_global = 0.000398), (GO:MF RNA helicase activity; q_global = 0.0038), (GO:CC nuclear protein-containing complex; q_global = 0.00857) and (GO:CC catalytic complex; q_global = 0.0297).
- **Conclusion**: Established evidence supports AQR as a spliceosome-linked RNA-processing component that connects RNA remodeling with mRNA export-related machinery. Its importance is reinforced by both network and complex evidence. The module does not establish a novel AQR interaction or a specific AQR-dependent function in bone.

#### CHD4

- **Related proteins** (co-abundance neighbors): POLR1B (0.82), VIRMA (0.81), LARS2 (0.80); STRING partners: TOP2A (0.715)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromodomain helicase DNA binding protein 4. The product of this gene belongs to the SNF2/RAD54 helicase family. It represents the main component of the nucleosome remodeling and deacetylase complex and plays an important role in epigenetic transcriptional repression. Patients with dermatomyositis develop antibodies against this protein. Somatic mutations in this gene are associated with serous endometrial tumors. Alternative splicing result…
- **Diseases (Open Targets)**: Sifrim-Hitz-Weiss syndrome (0.810); neurodegenerative disease (0.551); hereditary disease (0.505); endometrial cancer (0.470); uterine carcinosarcoma (0.439)
- **Europe PMC papers**: 3617
- **Why important**: CHD4 is a chromatin-remodeling helicase and a principal component of the nucleosome-remodeling and deacetylase complex. It connects in the module to POLR1B, VIRMA and LARS2, while STRING links it to TOP2A. It contributes to globally supported nucleic-acid catalytic, conformation-isomerase, RNA-biosynthetic, nuclear-complex and catalytic-complex terms (GO:MF catalytic activity, acting on a nucleic acid; q_global = 6.79e-05), (GO:MF nucleic acid conformation isomerase activity; q_global = 0.000551), (GO:MF macromolecular conformation isomerase activity; q_global = 0.00441), (GO:CC nuclear protein-containing complex; q_global = 0.00857) and (GO:CC catalytic complex; q_global = 0.0297). Its disease associations include developmental syndromes and endometrial cancer, and it has substantial literature support.
- **Conclusion**: Established evidence supports CHD4 as the principal chromatin and DNA-structure component that broadens the module beyond RNA processing. Its presence is compatible with coupling between chromatin state and gene expression. A mechanistic connection from CHD4 to the conserved bone and cell-line co-abundance pattern remains hypothetical.

## Module 7

**Tissue pair**: bone and cell line  
**Genes (5)**: ARK2N, PARVA, PTRHD1, MPST, UBE2E2

### Function

No GO or KEGG term passed global correction, so there is no statistically supported pathway-level functional assignment for this module. The network is organized around UBE2E2, with PTRHD1, PARVA, MPST, and ARK2N connected only to that hub. The gene annotations suggest several biological themes rather than one established process: ubiquitin and ISG15 conjugation, DNA-damage-related regulation, actin-linked adhesion, sulfur-compound metabolism, and peptidyl-tRNA recycling. UBE2E2 and ARK2N provide the strongest indication of protein-modification or proteostasis-related biology, whereas PARVA and MPST point to cellular-structure and metabolic state. Overall, the safest interpretation is a co-abundance pattern involving a ubiquitin-related hub together with genes from distinct cellular compartments and functions, not a confirmed common pathway. Lack of enrichment does not invalidate the module, but it limits functional specificity.

**Cell composition.** The module is not composed of plasma or secreted proteins: all members are annotated as non-secreted. Most genes have low tissue specificity, while MPST is tissue enhanced in liver. All members show cell-type-enhanced expression, but the reported cell types are heterogeneous and include adipocytes, esophageal epithelial populations, immune-related populations, enteric populations, reproductive cells, podocytes, smooth muscle cells, and microglia. Blood-cell specificity is generally low, although UBE2E2 is group enriched across several B-cell, monocyte, and dendritic-cell populations, and PARVA is immune-cell enhanced in MAIT T cells. Thus, the module does not resemble a plasma-protein signature or a uniform blood-cell program. It could still partly reflect shared cell-type composition or cellular state in the bone and cell-line samples. HPA provides no matching bone or cell-line protein-detection result here, so protein-level presence in those sample types cannot be inferred from this summary.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair reaches the stated high-confidence STRING interaction threshold, and no hu.MAP complex contains multiple module members. Therefore, the co-abundance relationships are not corroborated as established physical or functional interactions by these resources. The hub-like position of UBE2E2 is a property of this co-abundance network rather than evidence that it physically binds each neighbor. The lack of STRING and hu.MAP support also argues against interpreting the module as a known multiprotein complex. Known biology remains available for individual genes, especially UBE2E2 as a ubiquitin and ISG15-conjugating enzyme, PARVA as an integrin-linked-kinase-complex and actin-associated protein, MPST as a sulfurtransferase, PTRHD1 as a peptidyl-tRNA hydrolase, and ARK2N as a predicted ubiquitin-ligase-related regulator.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel tissue-pair co-abundance pattern because the genes form a module in the supplied bone and cell-line data despite having no high-confidence STRING-supported pairwise interactions and no shared hu.MAP complex. However, those absences do not establish biological novelty: co-abundance can reflect shared cell composition, regulation, stress, or technical structure, and the individual genes and their functions are already known to varying degrees. The result should therefore be described as a potentially new association at the level of this dataset and tissue comparison, not as discovery of a new molecular complex or pathway. The absence of globally significant GO or KEGG enrichment further means that novelty cannot be claimed from a new pathway annotation.

**Hypothesis.** Hypothesis: the module may reflect a coordinated cellular-state signal in which UBE2E2-centered protein-conjugation or proteostasis activity covaries with actin-adhesion state, sulfur metabolism, translation-quality control, and ubiquitin-related regulation. Such a signal could arise during adaptation to cellular stress, altered proliferation, or differences in the mixture of cell types shared between bone and the cell-line samples. This hypothesis is motivated by the hub topology and the individual annotations, but it is not established by enrichment, STRING, hu.MAP, or direct physical-interaction evidence. Testing would require replication, cell-composition adjustment, perturbation of UBE2E2, and measurement of the proposed processes.

### Important genes

#### UBE2E2

- **Related proteins** (co-abundance neighbors): PTRHD1 (0.86), PARVA (0.85), MPST (0.84), ARK2N (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin conjugating enzyme E2 E2. Enables ISG15 transferase activity and ubiquitin conjugating enzyme activity. Involved in protein modification by small protein conjugation. Acts upstream of or within cellular response to DNA damage stimulus and positive regulation of G1/S transition of mitotic cell cycle. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.589); diabetes mellitus (0.573); Abnormality of the skeletal system (0.510); hypothyroidism (0.470); diabetic eye disease (0.433)
- **Europe PMC papers**: 1699
- **Why important**: UBE2E2 is the central network gene, connected to every other module member and having the strongest weighted network position. Its established annotations include ubiquitin-conjugating and ISG15-transferase activity, protein modification by small-protein conjugation, DNA-damage response, and regulation of cell-cycle transition. It also has substantial literature coverage and multiple disease associations, including diabetes-related and skeletal-system phenotypes. Its broad tissue distribution and enrichment across several immune-cell populations make it a plausible marker of a shared cellular state, while also cautioning that it may reflect composition rather than a bone-specific mechanism.
- **Conclusion**: Established: UBE2E2 is the network hub and has documented roles in ubiquitin and ISG15 conjugation and DNA-damage-related biology. Hypothesis: it may organize or report the cellular-state signal represented by this module. The network does not demonstrate direct binding to the other members or prove that UBE2E2 drives their co-abundance.

#### PARVA

- **Related proteins** (co-abundance neighbors): UBE2E2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Actin filaments, Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: parvin alpha. This gene encodes a member of the parvin family of actin-binding proteins. Parvins are associated with focal contacts and contain calponin homology domains that bind to actin filaments. The encoded protein is part of the integrin-linked kinase signaling complex and plays a role in cell adhesion, motility and survival. [provided by RefSeq, Dec 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.487); osteoarthritis, hip (0.339); total hip arthroplasty (0.339); open-angle glaucoma (0.337); Pancreatic pseudocyst (0.331)
- **Europe PMC papers**: 3949
- **Why important**: PARVA is a direct neighbor of the hub and is localized to actin filaments and focal-adhesion sites. Its established functions include actin binding, cell adhesion, cell polarity, motility, survival, and participation in the integrin-linked kinase signaling complex. It has substantial literature coverage and associations with musculoskeletal and other disease phenotypes. These properties make PARVA the most informative module member for a possible adhesion, cytoskeletal, or tissue-architecture interpretation.
- **Conclusion**: Established: PARVA links the module to focal adhesions, actin organization, adhesion, and survival. Hypothesis: variation in adhesion or cytoskeletal state may be one component of the shared co-abundance pattern. There is no evidence here that PARVA physically interacts with UBE2E2 in this module.

#### MPST

- **Related proteins** (co-abundance neighbors): UBE2E2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mercaptopyruvate sulfurtransferase. This protein encoded by this gene catalyzes the transfer of a sulfur ion from 3-mercaptopyruvate to cyanide or other thiol compounds. It may be involved in cysteine degradation and cyanide detoxification. There is confusion in literature between this protein (mercaptopyruvate sulfurtransferase, MPST), which appears to be cytoplasmic, and thiosulfate sulfurtransferase (rhodanese, TST, GeneID:7263),…
- **Diseases (Open Targets)**: neurodegenerative disease (0.261); COVID-19 (0.164); severe acute respiratory syndrome (0.163); colitis (0.080); non-alcoholic fatty liver (0.078)
- **Europe PMC papers**: 1532
- **Why important**: MPST is a direct neighbor of UBE2E2 and is the only member with tissue-enhanced expression in the supplied HPA summary, namely in liver. It encodes mercaptopyruvate sulfurtransferase and is annotated in sulfur-amino-acid catabolism, cyanide or cyanate detoxification, response to toxic substances, and related developmental processes. It has substantial literature coverage and disease links involving neurological, infectious, and metabolic conditions. Its mitochondrial localization and metabolic function broaden the module beyond nuclear ubiquitin regulation.
- **Conclusion**: Established: MPST is a sulfur-metabolism and detoxification enzyme with liver-enhanced expression in the supplied HPA evidence. Hypothesis: sulfur handling or redox-related metabolic state could covary with the UBE2E2-centered signal. The module does not establish that MPST participates in a shared biochemical pathway with the other genes.

#### PTRHD1

- **Related proteins** (co-abundance neighbors): UBE2E2 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peptidyl-tRNA hydrolase domain containing 1. This gene encodes the enzyme peptidyl-tRNA hydrolase. Peptidyl-tRNA hydrolases perform the essential function of recycling peptidyl-tRNAs. Mutations in this gene are associated with autosomal-recessive intellectual disability and parkinsonism. [provided by RefSeq, May 2017].
- **Diseases (Open Targets)**: neurodevelopmental disorder with early-onset parkinsonism and behavioral abnormalities (0.649); Parkinson disease (0.351); parkinsonian disorder (0.340); Inguinal hernia (0.163); intestinal impaction (0.161)
- **Europe PMC papers**: 118
- **Why important**: PTRHD1 is a direct neighbor of the hub and encodes a peptidyl-tRNA hydrolase involved in recycling peptidyl-tRNAs, a process relevant to translation quality control. It has a documented association with autosomal-recessive intellectual disability and parkinsonism, as well as a smaller literature base than UBE2E2, PARVA, or MPST. Its nucleoplasmic localization and cell-type-enhanced pattern make it useful for considering translational or proteostatic state without overinterpreting it as a pathway member.
- **Conclusion**: Established: PTRHD1 has peptidyl-tRNA hydrolase annotation and disease associations involving neurodevelopment and parkinsonism. Hypothesis: altered translation quality control could accompany the broader cellular state represented by the module. There is no enrichment or interaction evidence establishing PTRHD1 as part of a common complex with UBE2E2.

#### ARK2N

- **Related proteins** (co-abundance neighbors): UBE2E2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: arkadia (RNF111) N-terminal like PKA signaling regulator 2N. Predicted to enable ubiquitin protein ligase activity. Predicted to be involved in ubiquitin-dependent protein catabolic process. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: alcohol drinking (0.230); stroke disorder (0.052); autosomal recessive limb-girdle muscular dystrophy type 2B (0.050); autosomal recessive limb-girdle muscular dystrophy type 2C (0.049); congenital myasthenic syndrome (0.048)
- **Europe PMC papers**: 16
- **Why important**: ARK2N is a direct neighbor of UBE2E2 and is annotated as a predicted ubiquitin-protein-ligase-related regulator involved in ubiquitin-dependent protein catabolism and negative regulation of transcription and viral life cycle. It has relatively sparse literature coverage compared with the other selected genes, which makes it potentially informative for follow-up but also increases uncertainty. Its nucleoplasmic localization and cell-type-enhanced expression are compatible with a regulatory interpretation.
- **Conclusion**: Established: ARK2N has predicted ubiquitin-related and transcriptional regulatory functions, but the evidence is less mature than for the better-studied module members. Hypothesis: ARK2N may contribute to a nuclear protein-turnover or regulatory-state component of the module. The co-abundance network alone cannot establish its enzymatic activity or cooperation with UBE2E2.

## Module 8

**Tissue pair**: bone and cell line  
**Genes (17)**: BOP1, DDX56, HEATR1, MYBBP1A, NOP56, NUP210, PUM3, RBM34, RSL1D1, PDCD11, RRS1, SUPV3L1, TEX10, UTP20, UTP6, WDR36, WDR3

### Function

This is a highly coherent nucleolar ribosome-biogenesis module. The primary evidence is the global enrichment of ribosome biogenesis (GO:BP ribosome biogenesis; q_global = 7.58e-08), nucleolus (GO:CC nucleolus; q_global = 9.03e-08), rRNA processing (GO:BP rRNA processing; q_global = 1.02e-07), preribosome (GO:CC preribosome; q_global = 1.43e-07), rRNA metabolism (GO:BP rRNA metabolic process; q_global = 2.97e-07), ribonucleoprotein-complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 8.93e-07), small-subunit processome (GO:CC small-subunit processome; q_global = 5.78e-06), and eukaryotic ribosome biogenesis (KEGG Ribosome biogenesis in eukaryotes - Homo sapiens (human); q_global = 0.00838). The module also supports RNA processing, RNA binding, small-subunit maturation, and nucleic-acid biosynthesis (9 globally significant GO/KEGG terms, q_global 0.00018–0.038; see the table). Thus, the most defensible interpretation is coordinated expression of factors that assemble and mature pre-ribosomal particles, especially the small-subunit pathway, with contributions to large-subunit maturation. This is a functional interpretation rather than evidence that the co-abundance pattern itself proves physical binding or causal regulation.

**Cell composition.** The module is not composed of plasma proteins or secreted proteins: the HPA summary reports no secreted genes. It is also not blood-cell enriched by the available HPA summary, which reports low immune-cell specificity for nearly all genes and no enriched blood-cell category. Most genes have low tissue specificity, consistent with a broadly expressed, housekeeping-like nucleolar program. Some cell-type-enhanced signals occur in diverse cell types, including differentiating germ cells, epithelial cells, neural cells, and progenitor populations, but these scattered signals do not support a specific blood or shared immune-cell explanation. NUP210 is enhanced in bone marrow and lymphoid tissue and in several progenitor populations, so it may contribute a tissue-context signal, but it is peripheral to the core ribosome-biogenesis pattern.

**GO/KEGG enrichment**: 20 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP ribosome biogenesis | 7.58e-08 | BOP1, DDX56, HEATR1, MYBBP1A, NOP56, PDCD11, RBM34, RRS1, UTP20, UTP6, WDR3, WDR36 |
| GO:CC nucleolus | 9.03e-08 | BOP1, DDX56, HEATR1, MYBBP1A, NOP56, PDCD11, PUM3, RBM34, RRS1, RSL1D1, TEX10, UTP20, UTP6, WDR3, WDR36 |
| GO:BP rRNA processing | 1.02e-07 | BOP1, DDX56, HEATR1, NOP56, PDCD11, RBM34, RRS1, UTP20, UTP6, WDR3, WDR36 |
| GO:CC preribosome | 1.43e-07 | BOP1, HEATR1, NOP56, PDCD11, RRS1, UTP20, UTP6, WDR3, WDR36 |
| GO:BP rRNA metabolic process | 2.97e-07 | BOP1, DDX56, HEATR1, NOP56, PDCD11, RBM34, RRS1, UTP20, UTP6, WDR3, WDR36 |
| GO:BP ribonucleoprotein complex biogenesis | 8.93e-07 | BOP1, DDX56, HEATR1, MYBBP1A, NOP56, PDCD11, RBM34, RRS1, UTP20, UTP6, WDR3, WDR36 |
| GO:CC small-subunit processome | 5.78e-06 | HEATR1, NOP56, PDCD11, UTP20, UTP6, WDR3, WDR36 |
| GO:BP RNA processing | 0.00018 | BOP1, DDX56, HEATR1, NOP56, PDCD11, RBM34, RRS1, SUPV3L1, UTP20, UTP6, WDR3, WDR36 |
| GO:CC 90S preribosome | 0.000197 | BOP1, HEATR1, UTP20, UTP6, WDR3 |
| GO:BP ribosomal small subunit biogenesis | 0.000617 | HEATR1, NOP56, RRS1, UTP20, UTP6, WDR3 |
| GO:MF RNA binding | 0.00103 | BOP1, DDX56, HEATR1, MYBBP1A, NOP56, PDCD11, PUM3, RBM34, RRS1, RSL1D1, SUPV3L1, UTP20, UTP6, WDR3 |
| GO:BP maturation of SSU-rRNA | 0.00181 | HEATR1, RRS1, UTP20, UTP6, WDR3 |
| GO:CC nuclear protein-containing complex | 0.00444 | BOP1, HEATR1, MYBBP1A, NOP56, NUP210, PDCD11, TEX10, UTP20, UTP6, WDR3, WDR36 |
| GO:CC ribonucleoprotein complex | 0.00589 | BOP1, HEATR1, NOP56, PDCD11, RRS1, UTP20, UTP6, WDR3, WDR36 |
| GO:MF snoRNA binding | 0.00809 | HEATR1, NOP56, UTP6, WDR3 |

### STRING and hu.MAP

STRING provides strong supplementary support for rRNA processing, preribosome, nucleolus, ninety-S preribosome, small-subunit processome, and the major rRNA-processing pathway (15 supplementary STRING terms; within-query FDR 1.31e-15–4.56e-07). The dense STRING connectivity among BOP1, HEATR1, NOP56, PDCD11, UTP20, UTP6, WDR3, WDR36, RSL1D1, and related RNA-binding factors indicates that the module is strongly concordant with already known functional relationships and likely reflects a shared nucleolar program rather than an arbitrary co-expression cluster. BOP1 is annotated as part of the PeBoW complex, while UTP20 is a component of the U3 snoRNA complex and PDCD11 is required for rRNA maturation and eighteen-S rRNA generation. No hu.MAP complex contains at least two module members, so hu.MAP supplies no independently confirmed complex assignment for this module. The absence of a hu.MAP complex does not negate the extensive STRING and annotation support.

**STRING interactions (score >= 0.7)**: 88 of 136 gene pairs: BOP1–DDX56 (0.963); BOP1–HEATR1 (0.971); BOP1–MYBBP1A (0.915); BOP1–NOP56 (0.974); BOP1–PDCD11 (0.97); BOP1–PUM3 (0.854); BOP1–RBM34 (0.888); BOP1–RRS1 (0.962); BOP1–RSL1D1 (0.998); BOP1–TEX10 (0.714); BOP1–UTP20 (0.914); BOP1–UTP6 (0.919); BOP1–WDR3 (0.973); BOP1–WDR36 (0.951); DDX56–HEATR1 (0.844); DDX56–MYBBP1A (0.838); DDX56–NOP56 (0.884); DDX56–PDCD11 (0.853); DDX56–PUM3 (0.929); DDX56–RBM34 (0.947); DDX56–RRS1 (0.914); DDX56–RSL1D1 (0.885); DDX56–UTP6 (0.82); DDX56–WDR3 (0.893); DDX56–WDR36 (0.923); HEATR1–MYBBP1A (0.973); HEATR1–NOP56 (0.999); HEATR1–PDCD11 (0.999); HEATR1–PUM3 (0.837); HEATR1–RSL1D1 (0.982); HEATR1–TEX10 (0.747); HEATR1–UTP20 (0.999); HEATR1–UTP6 (0.999); HEATR1–WDR3 (0.999); HEATR1–WDR36 (0.999); MYBBP1A–NOP56 (0.737); MYBBP1A–PDCD11 (0.949); MYBBP1A–PUM3 (0.851); MYBBP1A–RSL1D1 (0.831); MYBBP1A–UTP20 (0.709); MYBBP1A–UTP6 (0.754); MYBBP1A–WDR3 (0.878); MYBBP1A–WDR36 (0.861); NOP56–PDCD11 (0.997); NOP56–PUM3 (0.93); NOP56–RBM34 (0.705); NOP56–RRS1 (0.848); NOP56–RSL1D1 (0.991); NOP56–UTP20 (0.997); NOP56–UTP6 (0.998); NOP56–WDR3 (0.999); NOP56–WDR36 (0.999); PDCD11–PUM3 (0.956); PDCD11–RBM34 (0.709); PDCD11–RRS1 (0.786); PDCD11–RSL1D1 (0.978); PDCD11–TEX10 (0.716); PDCD11–UTP20 (0.999); PDCD11–UTP6 (0.994); PDCD11–WDR3 (0.997); PDCD11–WDR36 (0.998); PUM3–RBM34 (0.873); PUM3–RRS1 (0.962); PUM3–RSL1D1 (0.945); PUM3–UTP20 (0.812); PUM3–UTP6 (0.854); PUM3–WDR3 (0.905); PUM3–WDR36 (0.955); RBM34–RRS1 (0.802); RBM34–RSL1D1 (0.802); RBM34–UTP6 (0.744); RRS1–RSL1D1 (0.992); RRS1–UTP6 (0.76); RRS1–WDR3 (0.789); RRS1–WDR36 (0.7); RSL1D1–UTP20 (0.986); RSL1D1–UTP6 (0.993); RSL1D1–WDR3 (0.993); RSL1D1–WDR36 (0.992); TEX10–UTP6 (0.741); TEX10–WDR3 (0.778); TEX10–WDR36 (0.743); UTP20–UTP6 (0.998); UTP20–WDR3 (0.999); UTP20–WDR36 (0.999); UTP6–WDR3 (0.999); UTP6–WDR36 (0.999); WDR3–WDR36 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL rRNA processing, and Ribosomal large subunit biogenesis (FDR = 1.31e-15, 15 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 2.78e-15, 14 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 3.44e-14, 13 genes); COMPARTMENTS Preribosome (FDR = 1.27e-10, 10 genes); Component Preribosome (FDR = 1.47e-10, 10 genes); COMPARTMENTS Nucleolus (FDR = 5.24e-10, 14 genes); Component Nucleolus (FDR = 8.93e-10, 15 genes); COMPARTMENTS 90S preribosome (FDR = 1.04e-09, 8 genes); Process Ribosome biogenesis (FDR = 1.28e-08, 12 genes); Process rRNA processing (FDR = 1.74e-08, 11 genes); Component 90S preribosome (FDR = 1.82e-08, 7 genes); COMPARTMENTS Small-subunit processome (FDR = 2.85e-08, 7 genes); Component Small-subunit processome (FDR = 1.1e-07, 7 genes); RCTM Major pathway of rRNA processing in the nucleolus and cytosol (FDR = 3.96e-07, 9 genes); COMPARTMENTS Nuclear lumen (FDR = 4.56e-07, 15 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This should not be presented as a newly discovered ribosome-biogenesis mechanism. The core function is already well established by the global GO and KEGG evidence (20 globally significant GO/KEGG terms, q_global 7.58e-08–0.038; see the table), the strong STRING functional concordance (15 supplementary STRING terms; within-query FDR 1.31e-15–4.56e-07), the nucleolar localizations, and known annotations for several members. The potentially novel aspect is the reproducible co-abundance module shared by bone and cell line, or the particular combination and relative coordination of these genes in those tissue groups. That is a dataset-level observation requiring independent replication and perturbation before it can be called a new biological mechanism. Lack of a hu.MAP complex alone does not establish novelty, especially because the module is composed of broadly studied ribosome-biogenesis factors and STRING already captures many relationships.

**Hypothesis.** Mechanistic hypothesis: in both bone and the cell line, variation in cellular growth or biosynthetic demand co-regulates a nucleolar assembly program. Core processome and rRNA-processing factors, including HEATR1, UTP20, UTP6, WDR3, WDR36, PDCD11, and NOP56, may coordinate production and maturation of pre-ribosomal RNA, while BOP1 and associated factors support later large-subunit maturation. MYBBP1A, RSL1D1, and related RNA-binding proteins may couple this ribosome program to nucleolar stress, transcriptional control, senescence, or cell-cycle state. This is a hypothesis: the co-abundance data and enrichment establish a coherent association, not the direction of regulation, physical assembly of every module member, or a bone-specific causal pathway.

### Important genes

#### HEATR1

- **Related proteins** (co-abundance neighbors): WDR3 (0.93), PUM3 (0.84), DDX56 (0.83), SUPV3L1 (0.81), UTP20 (0.81), WDR36 (0.80); STRING partners: BOP1 (0.971), DDX56 (0.844), MYBBP1A (0.973), NOP56 (0.999), PDCD11 (0.999), PUM3 (0.837), RSL1D1 (0.982), TEX10 (0.747), UTP20 (0.999), UTP6 (0.999), WDR3 (0.999), WDR36 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HEAT repeat containing 1. Enables RNA binding activity. Involved in positive regulation of rRNA processing and positive regulation of transcription by RNA polymerase I. Located in fibrillar center and mitochondrion. Implicated in pancreatic ductal carcinoma. Biomarker of glioblastoma. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.475); Alzheimer disease (0.463); Parkinson disease (0.462); lysosomal storage disease (0.462); musculoskeletal system disorder (0.168)
- **Europe PMC papers**: 342
- **Why important**: HEATR1 has a highly central position in the module and is connected in STRING to nearly all major nucleolar components. It appears across essentially the full set of globally significant functional terms, including rRNA processing, preribosome, small-subunit processome, and eukaryotic ribosome biogenesis (20 globally significant GO/KEGG terms, q_global 7.58e-08–0.038; see the table). Its annotation supports RNA binding, positive regulation of rRNA processing, and RNA polymerase I transcription. It also has substantial literature and disease-study coverage, including cancer and neurodegenerative-disease associations.
- **Conclusion**: Established: HEATR1 is a strong central marker of the module's nucleolar rRNA-processing program. Hypothesis: its centrality may make it a useful regulatory entry point for testing whether the shared bone and cell-line module responds to biosynthetic or nucleolar stress.

#### WDR3

- **Related proteins** (co-abundance neighbors): HEATR1 (0.93), NOP56 (0.89), NUP210 (0.86), PUM3 (0.84), BOP1 (0.83), DDX56 (0.83); STRING partners: BOP1 (0.973), DDX56 (0.893), HEATR1 (0.999), MYBBP1A (0.878), NOP56 (0.999), PDCD11 (0.997), PUM3 (0.905), RRS1 (0.789), RSL1D1 (0.993), TEX10 (0.778), UTP20 (0.999), UTP6 (0.999), WDR36 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 3. This gene encodes a nuclear protein containing 10 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, which usually include a trp-asp at the C-terminal end. Proteins belonging to the WD repeat family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. [provid…
- **Diseases (Open Targets)**: presbycusis (0.335); respiratory tract infectious disorder (0.184); neurodegenerative disease (0.143); preeclampsia (0.120); alcohol drinking (0.098)
- **Europe PMC papers**: 280
- **Why important**: WDR3 has one of the strongest module network positions and is connected to multiple core factors, including HEATR1, NOP56, BOP1, DDX56, and PUM3. It is represented in nearly all globally significant terms and is annotated for maturation of the small ribosomal subunit and small-subunit biogenesis (20 globally significant GO/KEGG terms, q_global 7.58e-08–0.038; see the table). Its nucleolar localization and WD-repeat architecture are consistent with a scaffolding or assembly role. It also has disease associations spanning auditory, infectious, neurodegenerative, and pregnancy-related conditions, with a substantial literature base.
- **Conclusion**: Established: WDR3 is a central nucleolar ribosome-biogenesis component and a strong representative of the module. Hypothesis: its network position may reflect an organizing role in coordinating several pre-ribosomal assembly factors, which can be tested by perturbation and interaction assays.

#### UTP20

- **Related proteins** (co-abundance neighbors): HEATR1 (0.81), WDR36 (0.81); STRING partners: BOP1 (0.914), HEATR1 (0.999), MYBBP1A (0.709), NOP56 (0.997), PDCD11 (0.999), PUM3 (0.812), RSL1D1 (0.986), UTP6 (0.998), WDR3 (0.999), WDR36 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UTP20 small subunit processome component. UTP20 is a component of the U3 small nucleolar RNA (snoRNA) (SNORD3A; MIM 180710) protein complex (U3 snoRNP) and is involved in 18S rRNA processing (Wang et al., 2007 [PubMed 17498821]).[supplied by OMIM, Jun 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.437); bacterial arthritis (0.113); cartilage disease (0.050); corneal ulcer (0.044); breast neoplasm (0.041)
- **Europe PMC papers**: 285
- **Why important**: UTP20 is a component of the U3 snoRNA protein complex and is involved in eighteen-S rRNA processing. It is represented across the primary enrichment for ribosome biogenesis, the nucleolus, the preribosome, the small-subunit processome, and small-subunit maturation (20 globally significant GO/KEGG terms, q_global 7.58e-08–0.038; see the table). Its STRING relationships are especially concordant with the module's core processome factors. Its reported roles also include negative regulation of cell population proliferation and associations with neurodegenerative and cartilage-related disease.
- **Conclusion**: Established: UTP20 provides direct mechanistic support for a small-subunit processome interpretation. Hypothesis: UTP20 may connect the shared module to cell-state or proliferative differences between bone and the cell line, but this requires direct testing.

#### BOP1

- **Related proteins** (co-abundance neighbors): WDR3 (0.83), PUM3 (0.81); STRING partners: DDX56 (0.963), HEATR1 (0.971), MYBBP1A (0.915), NOP56 (0.974), PDCD11 (0.97), PUM3 (0.854), RBM34 (0.888), RRS1 (0.962), RSL1D1 (0.998), TEX10 (0.714), UTP20 (0.914), UTP6 (0.919), WDR3 (0.973), WDR36 (0.951)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BOP1 ribosomal biogenesis factor. Enables RNA binding activity. Involved in regulation of cell cycle; regulation of signal transduction by p53 class mediator; and ribosomal large subunit biogenesis. Located in chromosome; nucleolus; and nucleoplasm. Part of PeBoW complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.318); cancer (0.090); neoplasm (0.087); polycystic ovary syndrome (0.082); colorectal carcinoma (0.078)
- **Europe PMC papers**: 1064
- **Why important**: BOP1 is a nucleolar ribosomal-biogenesis factor and a component of the PeBoW complex. Its annotations include large-subunit assembly and maturation of ribosomal RNA, complementing the module's strong small-subunit and preribosome signal (20 globally significant GO/KEGG terms, q_global 7.58e-08–0.038; see the table). It has broad STRING connectivity despite a more modest co-abundance network degree, and it has a substantial literature base with links to cell-cycle control, p53 signaling, cancer, and neurodegenerative disease. HPA reports tissue enhancement in skeletal muscle but no secretion or immune-cell specificity.
- **Conclusion**: Established: BOP1 anchors the interpretation in ribosomal large-subunit maturation and the PeBoW pathway. Hypothesis: its presence may indicate that the shared module coordinates multiple stages of ribosome assembly rather than only small-subunit processing.

#### NOP56

- **Related proteins** (co-abundance neighbors): WDR3 (0.89), UTP6 (0.84), PUM3 (0.84), RRS1 (0.82), RSL1D1 (0.80), MYBBP1A (0.80); STRING partners: BOP1 (0.974), DDX56 (0.884), HEATR1 (0.999), MYBBP1A (0.737), PDCD11 (0.997), PUM3 (0.93), RBM34 (0.705), RRS1 (0.848), RSL1D1 (0.991), UTP20 (0.997), UTP6 (0.998), WDR3 (0.999), WDR36 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP56 ribonucleoprotein. Nop56p is a yeast nucleolar protein that is part of a complex with the nucleolar proteins Nop58p and fibrillarin. Nop56p is required for assembly of the 60S ribosomal subunit and is involved in pre-rRNA processing. The protein encoded by this gene is similar in sequence to Nop56p and is also found in the nucleolus. Expansion of a GGCCTG repeat from 3-8 copies to 1500-2500 copies in an intron of th…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 36 (0.586); neurodegenerative disease (0.495); ovarian neoplasm (0.272); hereditary disease (0.193); cerebellar ataxia (0.121)
- **Europe PMC papers**: 1517
- **Why important**: NOP56 is a nucleolar ribonucleoprotein factor involved in rRNA processing, rRNA modification, and ribosomal-subunit biogenesis. It has strong connections to the central module members and appears in many globally significant terms, including rRNA processing, preribosome, RNA binding, and the ribosome-biogenesis pathway (17 globally significant GO/KEGG terms, q_global 7.58e-08–0.038; see the table). It has the largest literature volume among the selected genes and a well-established disease association with spinocerebellar ataxia type thirty-six.
- **Conclusion**: Established: NOP56 is a well-supported nucleolar RNA-processing component and a disease-relevant anchor for the module. Hypothesis: coordinated NOP56 abundance could influence the efficiency or composition of pre-ribosomal particles, but the present data do not establish such an effect.

## Module 9

**Tissue pair**: bone and cell line  
**Genes (20)**: BRIX1, CDC73, CHD1, COPG2, CPSF1, SLC25A10, ESF1, GTPBP4, KRR1, NOP2, URB1, NUP160, NUP188, NUP85, PDS5B, RBM28, RRP12, RRP1, URB2, UTP4

### Function

The module is most strongly interpreted as a nucleolar ribosome-biogenesis and pre-ribosomal RNA-processing module. The primary evidence is the set of globally corrected terms for ribosome biogenesis (GO:BP ribosome biogenesis; q_global = 0.00104), rRNA processing (GO:BP rRNA processing; q_global = 0.0014), rRNA metabolism (GO:BP rRNA metabolic process; q_global = 0.00299), ribonucleoprotein-complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.00622), RNA processing (GO:BP RNA processing; q_global = 0.00948), and nucleolus localization (GO:CC nucleolus; q_global = 0.0111). These terms converge on maturation and assembly of ribosomal components rather than on a tissue-specific structural or extracellular function. The module contains a coherent core of nucleolar factors, including BRIX1, ESF1, GTPBP4, KRR1, NOP2, RRP1, RRP12, URB1, URB2, and UTP4. The presence of RNA-processing, nuclear-pore, chromatin, transcriptional, mitochondrial-transport, and vesicle-transport genes suggests that the co-abundance signal may also capture coupling between ribosome production and broader nuclear or cellular growth programs. Those extensions are secondary interpretations; the strongest functional conclusion is nucleolar ribosome biogenesis and rRNA processing.

**Cell composition.** The module is not composed of plasma proteins or secreted proteins: HPA reports no secreted genes. Most genes have low tissue specificity, and most have low immune-cell specificity, which is consistent with broadly expressed intracellular housekeeping or growth-related machinery rather than a specialized tissue product. HPA does identify cell-type-enhanced patterns for many genes, but these are distributed across diverse cell types, including oocytes, muscle-related cells, epithelial cells, and progenitor populations. RRP12 is the clearest blood-related exception, with enrichment in bone marrow-associated and myeloid populations and immune enhancement in neutrophils. The overall profile does not support a predominantly blood-cell or plasma-protein explanation, although shared proliferative or nucleated cell content in bone and the cell line could contribute to the conserved co-abundance signal. HPA reports no matching protein-detection result for either the bone or cell-line tissue category, so protein-level confirmation in those specific samples is absent.

**GO/KEGG enrichment**: 6 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP ribosome biogenesis | 0.00104 | BRIX1, ESF1, GTPBP4, KRR1, NOP2, RRP1, URB1, URB2, UTP4 |
| GO:BP rRNA processing | 0.0014 | BRIX1, ESF1, GTPBP4, KRR1, NOP2, RRP1, URB1, UTP4 |
| GO:BP rRNA metabolic process | 0.00299 | BRIX1, ESF1, GTPBP4, KRR1, NOP2, RRP1, URB1, UTP4 |
| GO:BP ribonucleoprotein complex biogenesis | 0.00622 | BRIX1, ESF1, GTPBP4, KRR1, NOP2, RRP1, URB1, URB2, UTP4 |
| GO:BP RNA processing | 0.00948 | BRIX1, CDC73, CPSF1, ESF1, GTPBP4, KRR1, NOP2, RBM28, RRP1, URB1, UTP4 |
| GO:CC nucleolus | 0.0111 | BRIX1, ESF1, GTPBP4, KRR1, NOP2, RBM28, RRP1, RRP12, URB1, URB2, UTP4 |

### STRING and hu.MAP

STRING provides strong supplementary support for a connected ribosome-biogenesis core. The strongest and most recurrent relationships link BRIX1, ESF1, GTPBP4, KRR1, NOP2, RBM28, RRP1, RRP12, URB1, URB2, and UTP4, and STRING functional groups repeatedly identify rRNA processing, preribosome maturation, ribonucleoprotein-complex biogenesis, and the nucleolus (STRING NetworkNeighborAL rRNA processing, and RNA helicase activity; within-query FDR = 3.31e-07) through (STRING Component Nucleolus; within-query FDR = 0.0043). NOP2, BRIX1, GTPBP4, KRR1, RRP1, RRP12, and UTP4 are particularly well embedded in this known interaction neighborhood. A separate STRING-supported group connects NUP160, NUP188, and NUP85, consistent with a nuclear pore complex component, while CDC73 and CHD1 form a weaker transcriptional or chromatin-related connection. hu.MAP independently supports the nuclear-pore interpretation through complexes containing NUP160, NUP188, and NUP85 (hu.MAP huMAP3_08489.1), (hu.MAP huMAP3_09825.1), (hu.MAP huMAP3_04548.1), (hu.MAP huMAP3_09710.1), and related complexes. hu.MAP also links CHD1 with RRP12 in a broader complex (hu.MAP huMAP3_01045.1). Thus, the module contains a well-known nucleolar interaction core plus a nuclear-transport and chromatin-associated peripheral component. These resources indicate that much of the molecular machinery is already established; the co-abundance organization across the bone and cell-line tissue pair is the more distinctive aspect.

**STRING interactions (score >= 0.7)**: 44 of 190 gene pairs: BRIX1–ESF1 (0.851); BRIX1–GTPBP4 (0.998); BRIX1–KRR1 (0.941); BRIX1–NOP2 (0.986); BRIX1–RBM28 (0.948); BRIX1–RRP1 (0.981); BRIX1–RRP12 (0.871); BRIX1–UTP4 (0.892); CDC73–CHD1 (0.729); ESF1–GTPBP4 (0.942); ESF1–KRR1 (0.957); ESF1–NOP2 (0.823); ESF1–RBM28 (0.914); ESF1–RRP1 (0.71); ESF1–RRP12 (0.892); ESF1–UTP4 (0.864); GTPBP4–KRR1 (0.771); GTPBP4–NOP2 (0.993); GTPBP4–RBM28 (0.975); GTPBP4–RRP1 (0.95); GTPBP4–RRP12 (0.981); GTPBP4–UTP4 (0.889); KRR1–NOP2 (0.741); KRR1–RBM28 (0.95); KRR1–RRP1 (0.878); KRR1–RRP12 (0.992); KRR1–UTP4 (0.999); NOP2–RBM28 (0.99); NOP2–RRP1 (0.908); NOP2–RRP12 (0.844); NOP2–URB1 (0.746); NOP2–UTP4 (0.753); NUP160–NUP188 (0.99); NUP160–NUP85 (0.999); NUP188–NUP85 (0.992); RBM28–RRP1 (0.773); RBM28–RRP12 (0.977); RBM28–UTP4 (0.937); RRP1–RRP12 (0.782); RRP1–UTP4 (0.774); RRP12–URB1 (0.741); RRP12–UTP4 (0.891); URB1–URB2 (0.89); URB1–UTP4 (0.831)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL rRNA processing, and RNA helicase activity (FDR = 3.31e-07, 11 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 3.51e-06, 9 genes); NetworkNeighborAL Mixed, incl. Preribosome, large subunit precursor, and Maturation of LSU-rRNA (FDR = 2.09e-05, 6 genes); Process rRNA processing (FDR = 0.0001, 9 genes); Process Ribonucleoprotein complex biogenesis (FDR = 0.0001, 11 genes); Process Ribosome biogenesis (FDR = 0.0001, 10 genes); Process RNA processing (FDR = 0.00044, 12 genes); Keyword Nucleus (FDR = 0.00087, 18 genes); COMPARTMENTS Nucleolus (FDR = 0.0024, 10 genes); COMPARTMENTS Nucleus (FDR = 0.0033, 18 genes); Keyword Ribosome biogenesis (FDR = 0.0034, 5 genes); Process Gene expression (FDR = 0.004, 14 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0041, 13 genes); Component Nucleolus (FDR = 0.0043, 11 genes); NetworkNeighborAL Mixed, incl. Hypotrichosis 11, and Suppressor of forked (FDR = 0.005, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08489.1 (NUP160, NUP188, NUP85; 3/10); huMAP3_09825.1 (NUP160, NUP188, NUP85; 3/27); huMAP3_11232.1 (NUP160, NUP85, PDS5B; 3/78); huMAP3_04548.1 (NUP160, NUP85; 2/2); huMAP3_01045.1 (CHD1, RRP12; 2/5); huMAP3_09710.1 (NUP160, NUP188; 2/13); huMAP3_08298.1 (NUP160, NUP85; 2/24); huMAP3_09114.1 (NUP160, NUP85; 2/30); huMAP3_10202.1 (NUP160, NUP85; 2/52); huMAP3_12581.1 (NUP160, NUP85; 2/58)

### Novelty

This module should not be described as a newly discovered ribosome-biogenesis pathway. Its central genes, functions, and many pairwise relationships are already documented by GO, STRING, hu.MAP, and gene-specific literature. The module may still represent a useful or potentially novel cross-tissue co-abundance pattern, especially if this precise combination and conservation between bone and the cell line have not previously been reported. However, that claim requires comparison with published co-expression or proteomic-module studies and replication in independent datasets. The absence of a hu.MAP or STRING relationship for individual genes is not evidence of novelty, because those databases are incomplete and because co-abundance can reflect shared regulation without direct physical interaction. The most defensible conclusion is that the biological process is established, while the tissue-pair-specific network configuration may be a candidate observation rather than a demonstrated new mechanism.

**Hypothesis.** Hypothesis: the conserved module reflects coordinated control of nucleolar ribosome production in proliferative or metabolically active nucleated cells present in both bone and the cell-line samples. The central rRNA-processing machinery could generate the dominant co-abundance signal, while NUP160, NUP188, and NUP85 couple ribosome-component trafficking and nucleocytoplasmic transport to the nucleolar program. PDS5B, CHD1, and CDC73 may connect this program to chromatin state, cell-cycle organization, and transcriptional output. RRP12's bone-marrow and myeloid enrichment raises the alternative possibility that a progenitor or myeloid-related cellular component contributes in bone, but the broad HPA profile argues against a purely blood-derived explanation. This hypothesis predicts coordinated changes in pre-rRNA maturation, nucleolar organization, nuclear transport, and cellular proliferation, and should be tested by cell-composition analysis, perturbation of the nucleolar core, and validation in independent bone and cell-line datasets.

### Important genes

#### GTPBP4

- **Related proteins** (co-abundance neighbors): RRP12 (0.88), SLC25A10 (0.86), RBM28 (0.84), KRR1 (0.83), UTP4 (0.80); STRING partners: BRIX1 (0.998), ESF1 (0.942), KRR1 (0.771), NOP2 (0.993), RBM28 (0.975), RRP1 (0.95), RRP12 (0.981), UTP4 (0.889)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GTP binding protein 4. GTP-binding proteins are GTPases and function as molecular switches that can flip between two states: active, when GTP is bound, and inactive, when GDP is bound. 'Active' in this context usually means that the molecule acts as a signal to trigger other events in the cell. When an extracellular ligand binds to a G-protein-linked receptor, the receptor changes its conformation and switches on the tr…
- **Diseases (Open Targets)**: gout (0.367); neurodegenerative disease (0.339); chronic kidney disease (0.110); hepatocellular carcinoma (0.100); hypotensive disorder (0.094)
- **Europe PMC papers**: 430
- **Why important**: GTPBP4 is a highly connected member of the module's nucleolar core and participates in every primary globally corrected term (GO:BP ribosome biogenesis; q_global = 0.00104) through (GO:CC nucleolus; q_global = 0.0111). It has extensive STRING support with the principal preribosome and rRNA-processing genes, including BRIX1, ESF1, NOP2, RBM28, RRP1, RRP12, and UTP4, and is repeatedly represented in supplementary STRING groups (STRING NetworkNeighborAL rRNA processing, and RNA helicase activity; within-query FDR = 3.31e-07) through (STRING Component Nucleolus; within-query FDR = 0.0043). Its curated annotations include osteoblast differentiation and regulation of cell proliferation, making it especially relevant to a bone-associated module. It also has disease links involving gout, neurodegenerative disease, chronic kidney disease, and cancer-related conditions, with a substantial literature base.
- **Conclusion**: Established evidence supports GTPBP4 as a central nucleolar ribosome-biogenesis factor and a strong representative of the module's core function. Its bone-relevant annotation makes it a plausible bridge between the generic nucleolar program and the observed tissue pair. It remains a hypothesis, not an established fact, that GTPBP4 drives the conserved bone and cell-line co-abundance pattern.

#### NOP2

- **Related proteins** (co-abundance neighbors): RBM28 (0.81); STRING partners: BRIX1 (0.986), ESF1 (0.823), GTPBP4 (0.993), KRR1 (0.741), RBM28 (0.99), RRP1 (0.908), RRP12 (0.844), URB1 (0.746), UTP4 (0.753)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP2 nucleolar protein. Enables RNA binding activity. Involved in positive regulation of cell population proliferation; regulation of signal transduction by p53 class mediator; and ribosomal large subunit assembly. Located in nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.273); nonpapillary renal cell carcinoma (0.097); neoplasm (0.097); cancer (0.091); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 2120
- **Why important**: NOP2 is a nucleolar RNA-processing and large-subunit assembly factor present in all primary terms (GO:BP ribosome biogenesis; q_global = 0.00104) through (GO:CC nucleolus; q_global = 0.0111). It has particularly broad STRING connectivity across the ribosome-biogenesis core and appears in nearly all relevant supplementary STRING groups, including the preribosome and rRNA-processing groups (STRING NetworkNeighborAL rRNA processing, and RNA helicase activity; within-query FDR = 3.31e-07) through (STRING NetworkNeighborAL Mixed, incl. Hypotrichosis 11, and Suppressor of forked; within-query FDR = 0.005). Its annotations include rRNA processing, large-subunit assembly, and positive regulation of cell proliferation. NOP2 also has a large literature volume and disease associations involving neurodegenerative disease, renal carcinoma, neoplasm, and hepatocellular carcinoma, making it a well-studied biological anchor.
- **Conclusion**: Established evidence identifies NOP2 as a central and well-characterized component of ribosome production with a strong connection to proliferative biology. It is an important marker of the module's nucleolar identity. Any specific role for NOP2 in bone biology or in conserving this module between tissues remains a hypothesis.

#### RRP12

- **Related proteins** (co-abundance neighbors): URB1 (0.89), GTPBP4 (0.88), PDS5B (0.82), UTP4 (0.82); STRING partners: BRIX1 (0.871), ESF1 (0.892), GTPBP4 (0.981), KRR1 (0.992), NOP2 (0.844), RBM28 (0.977), RRP1 (0.782), URB1 (0.741), UTP4 (0.891)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: huMAP3_01045.1
- **Function (MyGene.info)**: ribosomal RNA processing 12 homolog. Enables RNA binding activity. Predicted to be involved in rRNA processing. Located in cytosol; nucleolus; and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.435); bilateral striopallidodentate calcinosis (0.370); colorectal carcinoma (0.079); hepatocellular carcinoma (0.075); neoplasm (0.067)
- **Europe PMC papers**: 367
- **Why important**: RRP12 combines a central position in the module with unusually informative HPA composition evidence. It is part of the nucleolar primary evidence through (GO:CC nucleolus; q_global = 0.0111) and is represented in many STRING groups covering rRNA processing, preribosome maturation, and ribosome biogenesis (STRING NetworkNeighborAL rRNA processing, and RNA helicase activity; within-query FDR = 3.31e-07) through (STRING Process RNA processing; within-query FDR = 0.00044) and (STRING Process Gene expression; within-query FDR = 0.004) through (STRING NetworkNeighborAL Mixed, incl. Hypotrichosis 11, and Suppressor of forked; within-query FDR = 0.005). Its STRING relationships connect it to GTPBP4, KRR1, RBM28, RRP1, URB1, and UTP4. HPA reports group enrichment involving bone marrow and skeletal muscle, together with enhancement in monocyte and neutrophil-related populations. Its disease associations include neurodegenerative disease, brain calcification-related disease, colorectal carcinoma, and hepatocellular carcinoma.
- **Conclusion**: Established evidence supports RRP12 as a nucleolar rRNA-processing factor and as a possible indicator of cellular composition relevant to bone samples. The HPA pattern makes it useful for testing whether progenitor or myeloid content contributes to the module. It is not established that RRP12 specifically explains the cross-tissue conservation or that the module is blood-derived.

#### KRR1

- **Related proteins** (co-abundance neighbors): GTPBP4 (0.83), SLC25A10 (0.80), RBM28 (0.80); STRING partners: BRIX1 (0.941), ESF1 (0.957), GTPBP4 (0.771), NOP2 (0.741), RBM28 (0.95), RRP1 (0.878), RRP12 (0.992), UTP4 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: KRR1 small subunit processome component. Enables RNA binding activity. Predicted to be involved in rRNA processing. Located in chromosome; intercellular bridge; and nuclear lumen. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.491); polycystic ovary syndrome (0.204); complex regional pain syndrome (0.157); glaucoma (0.122); placental abruption (0.110)
- **Europe PMC papers**: 356
- **Why important**: KRR1 is a nucleolar small-subunit processome component and appears in every primary globally corrected term (GO:BP ribosome biogenesis; q_global = 0.00104) through (GO:CC nucleolus; q_global = 0.0111). It is strongly connected in STRING to BRIX1, ESF1, GTPBP4, NOP2, RBM28, RRP1, RRP12, and UTP4, and is included across the principal supplementary ribosome-biogenesis and rRNA-processing groups (STRING NetworkNeighborAL rRNA processing, and RNA helicase activity; within-query FDR = 3.31e-07) through (STRING Component Nucleolus; within-query FDR = 0.0043). Its curated functions include small-subunit rRNA maturation and ribosome biogenesis. Disease associations include neurodegenerative disease, polycystic ovary syndrome, complex regional pain syndrome, glaucoma, and placental abruption, while its literature provides substantial support for its molecular role.
- **Conclusion**: Established evidence supports KRR1 as a core small-subunit maturation factor and a reliable functional marker of the module. Its participation strengthens the interpretation that the signal is a coordinated ribosome-biogenesis program rather than a generic RNA-processing association. A tissue-specific regulatory role is only a hypothesis.

#### NUP160

- **Related proteins** (co-abundance neighbors): NUP85 (0.84), PDS5B (0.82), CHD1 (0.81); STRING partners: NUP188 (0.99), NUP85 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08489.1, huMAP3_09825.1, huMAP3_11232.1, huMAP3_04548.1, huMAP3_09710.1, huMAP3_08298.1, huMAP3_09114.1, huMAP3_10202.1, huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 160. NUP160 is 1 of up to 60 proteins that make up the 120-MD nuclear pore complex, which mediates nucleoplasmic transport.[supplied by OMIM, Apr 2004]
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.527); neurodegenerative disease (0.469); Alzheimer disease (0.429)
- **Europe PMC papers**: 812
- **Why important**: NUP160 is important because it represents the module's nuclear-pore and transport arm rather than its nucleolar core. It connects in the module network to PDS5B, NUP85, and CHD1, and STRING supports relationships with NUP85 and NUP188 (STRING Keyword Nucleus; within-query FDR = 0.00087), (STRING COMPARTMENTS Nucleus; within-query FDR = 0.0033), and (STRING Process Gene expression; within-query FDR = 0.004). hu.MAP repeatedly places NUP160 with NUP85 and NUP188 in nuclear-pore-related complexes (hu.MAP huMAP3_08489.1), (hu.MAP huMAP3_09825.1), (hu.MAP huMAP3_04548.1), and (hu.MAP huMAP3_09710.1) through (hu.MAP huMAP3_12581.1). Its curated functions include mRNA export, ribosomal large-subunit export, protein import and export, and nucleocytoplasmic transport. It also has a substantial literature base and disease associations involving viral infection, neurodegenerative disease, Alzheimer disease, and developmental disease.
- **Conclusion**: Established evidence supports NUP160 as a nuclear-pore component that could connect nucleolar ribosome production with transport across the nuclear envelope. Its presence broadens the module beyond a simple list of rRNA-processing factors. It remains a hypothesis that NUP160 mechanistically couples transport to the conserved co-abundance program in bone and the cell line.

## Module 10

**Tissue pair**: bone and cell line  
**Genes (6)**: GNA13, MYOF, NSF, NUP107, HM13, TBL2

### Function

The module most plausibly reflects a coordinated intracellular membrane-trafficking and cellular-organization program rather than a single established biochemical pathway. NSF supports vesicle-mediated transport, exocytosis, receptor recycling, and intra-Golgi trafficking; HM13 supports endoplasmic-reticulum membrane-protein processing; MYOF supports calcium-dependent membrane fusion and plasma-membrane repair; GNA13 supports heterotrimeric G-protein and Rho signaling; NUP107 supports nuclear transport; and TBL2 has annotations related to cellular stress responses and intracellular signaling. These functions are biologically compatible with a shared co-abundance state involving membrane dynamics, trafficking, signaling, and proteostasis. However, no GO or KEGG term passed global correction, and there were no supplementary STRING enrichment terms. Therefore, this is a functional interpretation of the component annotations and network pattern, not evidence for statistically significant pathway enrichment.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not uniformly blood-cell enriched. Most genes have low immune-cell specificity, although GNA13 is enhanced in bone marrow and several myeloid, dendritic, neutrophil, and platelet cell types, while MYOF is enhanced in intermediate and non-classical monocytes. The remaining genes show disparate cell-type or tissue associations, including brain, testis, reproductive cells, epithelial cells, and plasma cells. This heterogeneity argues against interpreting the module as a simple blood-protein signature. Nevertheless, shared cellular composition, especially immune or myeloid contamination in some samples, could contribute to the cross-tissue co-abundance pattern. The absence of matching HPA protein measurements for the two sampled contexts limits direct protein-level interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module members, and no hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated here as established physical interactions or membership in a known multiprotein complex. The annotations nevertheless provide biologically plausible links through broad cellular processes: NSF and HM13 relate to intracellular membrane handling, GNA13 to signaling, MYOF to membrane fusion and repair, NUP107 to nucleocytoplasmic transport, and TBL2 to stress-responsive intracellular regulation. The sparse network should therefore be treated as a coordinated expression or abundance module, not as a demonstrated physical pathway.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a previously unreported co-abundance relationship in the specific bone and cell-line comparison, because the module has no matching high-confidence STRING interactions, no supported hu.MAP complex, and no globally significant GO or KEGG enrichment. However, those absences do not establish biological novelty: the genes are individually well characterized, their functions are broad and partly convergent, and co-abundance relationships can arise from shared cell composition, common cellular state, or technical effects. The appropriate conclusion is that the module is an exploratory and potentially novel co-abundance pattern, while its mechanistic novelty remains unproven.

**Hypothesis.** Hypothesis: the module marks a shared cellular state in which membrane trafficking, receptor or cargo recycling, membrane repair, and intracellular signaling are coordinated with stress handling and nuclear transport. In this model, NSF and HM13 represent vesicular and endoplasmic-reticulum trafficking capacity, MYOF represents calcium-dependent membrane remodeling, GNA13 couples extracellular signals to Rho-related responses, NUP107 reflects transport across the nuclear pore, and TBL2 links the state to intracellular stress or metabolic regulation. The hypothesis predicts that the module will track cellular stress, membrane turnover, or differences in immune and stromal composition rather than define a stable physical complex. It requires validation with replication, cell-composition adjustment, perturbation, and independent protein or transcript measurements.

### Important genes

#### TBL2

- **Related proteins** (co-abundance neighbors): HM13 (0.83), NUP107 (0.82), MYOF (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transducin beta like 2. This gene encodes a member of the beta-transducin protein family. Most proteins of the beta-transducin family are involved in regulatory functions. This protein is possibly involved in some intracellular signaling pathway. This gene is deleted in Williams-Beuren syndrome, a developmental disorder caused by deletion of multiple genes at 7q11.23. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: gout (0.305); physical activity (0.280); type 2 diabetes mellitus (0.257); Abnormality of the skeletal system (0.243); diabetes mellitus (0.200)
- **Europe PMC papers**: 346
- **Why important**: TBL2 is the most connected member of the module and links HM13, NUP107, and MYOF, making it the principal network connector. Its annotations include endoplasmic-reticulum unfolded-protein response, glucose-starvation response, and hypoxia response, which provide a plausible bridge between membrane handling and cellular stress. It is also associated with skeletal-system abnormality and metabolic disease in Open Targets, relevant to the bone context. Its literature base is smaller than that of NSF but sufficient to support a biologically meaningful, rather than purely computational, interpretation.
- **Conclusion**: Established evidence supports TBL2 as the module's central co-abundance connector and as a protein associated with intracellular regulation and stress responses. The hypothesis that TBL2 organizes the broader trafficking-stress state is not established by the supplied data and requires functional testing.

#### NSF

- **Related proteins** (co-abundance neighbors): GNA13 (0.82), HM13 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-ethylmaleimide sensitive factor, vesicle fusing ATPase. Enables PDZ domain binding activity and ionotropic glutamate receptor binding activity. Involved in intracellular protein transport; positive regulation of protein catabolic process; and positive regulation of receptor recycling. Located in Golgi apparatus; cytosol; and plasma membrane. Implicated in developmental and epileptic encephalopathy. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy 96 (0.561); neurodegenerative disease (0.529); atrial fibrillation (0.310); Abnormality of the skeletal system (0.303); androgenetic alopecia (0.300)
- **Europe PMC papers**: 65784
- **Why important**: NSF is a central bridge between HM13 and GNA13 and has well-established roles in vesicle-mediated transport, exocytosis, intra-Golgi transport, receptor recycling, and protein transport. It has the strongest literature support among the module members and disease associations involving developmental epileptic encephalopathy and neurodegenerative disease. Its brain and neuronal HPA associations also emphasize that this gene may reflect specialized trafficking demands rather than a bone-specific mechanism.
- **Conclusion**: Established evidence strongly supports NSF as a core intracellular trafficking component and an important anchor for the module's membrane-transport interpretation. Its participation in this particular cross-tissue module is supported by co-abundance and annotation compatibility, but a direct physical or causal role within the module remains hypothetical.

#### HM13

- **Related proteins** (co-abundance neighbors): TBL2 (0.83), NSF (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: histocompatibility minor 13. The protein encoded by this gene, which localizes to the endoplasmic reticulum, catalyzes intramembrane proteolysis of some signal peptides after they have been cleaved from a preprotein. This activity is required to generate signal sequence-derived human lymphocyte antigen-E epitopes that are recognized by the immune system, and to process hepatitis C virus core protein. The encoded protein is an…
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.097); neoplasm (0.094); breast cancer (0.078); breast carcinoma (0.077); eye disorder (0.077)
- **Europe PMC papers**: 460
- **Why important**: HM13 connects TBL2 and NSF and encodes an endoplasmic-reticulum intramembrane protease involved in processing signal-peptide-derived products and membrane-protein maturation. This provides a mechanistic connection between endoplasmic-reticulum quality control, membrane-protein processing, and the NSF-associated trafficking functions. It also has a substantial literature base and disease associations involving neoplasia and other disorders.
- **Conclusion**: Established evidence supports HM13 as an endoplasmic-reticulum membrane-processing protein that is functionally compatible with a trafficking and proteostasis module. The idea that HM13 coordinates with NSF or TBL2 in this module is a hypothesis because neither STRING nor hu.MAP provides supporting relationships here.

#### GNA13

- **Related proteins** (co-abundance neighbors): NSF (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein subunit alpha 13. Predicted to enable D5 dopamine receptor binding activity; G-protein beta/gamma-subunit complex binding activity; and GTPase activity. Predicted to be involved in several processes, including Rho protein signal transduction; activation of phospholipase D activity; and multicellular organism aging. Predicted to act upstream of or within several processes, including branching involved in blood vesse…
- **Diseases (Open Targets)**: lymphoma (0.373); neurodegenerative disease (0.370); diffuse large B-cell lymphoma (0.306); ovarian dysfunction (0.212); neoplasm (0.188)
- **Europe PMC papers**: 1664
- **Why important**: GNA13 is the signaling endpoint connected to NSF and is annotated for G-protein signaling, Rho signaling, phospholipase-related regulation, vascular processes, and blood-pressure regulation. It is tissue enhanced in bone marrow and shows enhancement across several myeloid and platelet-related cell types, making it particularly relevant to possible immune or cellular-composition effects in the bone samples. Its disease associations include lymphoma and diffuse large B-cell lymphoma.
- **Conclusion**: Established evidence supports GNA13 as a signaling and cytoskeletal-regulatory protein with a notable bone-marrow and immune-cell context. Its inclusion may reflect signaling coordination with trafficking or may reflect shared myeloid composition; the supplied data do not distinguish these explanations.

#### MYOF

- **Related proteins** (co-abundance neighbors): TBL2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Plasma membrane, Centriolar satellite; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myoferlin. Mutations in dysferlin, a protein associated with the plasma membrane, can cause muscle weakness that affects both proximal and distal muscles. The protein encoded by this gene is a type II membrane protein that is structurally similar to dysferlin. It is a member of the ferlin family and associates with both plasma and nuclear membranes. The protein contains C2 domains that play a role in calcium…
- **Diseases (Open Targets)**: hereditary angioedema (0.443); neurodegenerative disease (0.413); cervical carcinoma (0.134); type 2 diabetes mellitus (0.131); neoplasm (0.112)
- **Europe PMC papers**: 1200
- **Why important**: MYOF is connected to TBL2 and is associated with plasma-membrane repair, calcium-dependent membrane fusion, muscle contraction, blood circulation, and regulation of neurotransmitter secretion. Its vesicle and plasma-membrane localization makes it a useful functional complement to NSF and HM13. HPA places it in several epithelial cell types and in intermediate and non-classical monocytes, so it is also relevant to the possibility that cellular composition contributes to the module.
- **Conclusion**: Established evidence supports MYOF as a membrane-remodeling and repair protein with a plausible role in a trafficking-related cellular state. Its role as a functional partner of TBL2 or as a driver of the shared bone and cell-line pattern is not established and remains hypothetical.
