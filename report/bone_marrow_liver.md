# Conserved co-abundance modules: bone_marrow and liver

## Module 0

**Tissue pair**: bone_marrow and liver  
**Genes (17)**: YWHAH, SLC3A2, ARSA, CASP3, CIAO1, DNM1L, DUSP3, GNL1, GMPS, MACROH2A1, LUC7L2, PRKDC, CAD, SRP72, FARSB, VIL1, CSE1L

### Function

The strongest supported function is a cellular response to epidermal growth factor signaling, represented by the globally corrected terms (GO:BP response to epidermal growth factor; q_global = 0.0474) and (GO:BP cellular response to epidermal growth factor stimulus; q_global = 0.0474). CAD, DUSP3, and VIL1 provide the direct enrichment evidence. Their annotations suggest complementary biology: CAD links proliferative signaling to nucleotide synthesis, DUSP3 attenuates EGFR and MAPK signaling, and VIL1 connects EGFR-related signaling with epithelial actin organization and cell shape. The remainder of the module is functionally heterogeneous, including RNA processing, protein targeting to the endoplasmic reticulum, mitochondrial and peroxisomal dynamics, apoptosis, DNA repair, iron-sulfur assembly, chromatin regulation, amino-acid transport, and nucleotide metabolism. Thus, the module is best interpreted as an EGFR-responsive cellular-state module with supporting housekeeping, biosynthetic, stress, and cell-cycle-related components rather than as a single narrowly defined biochemical pathway. The globally corrected GO evidence consists of (GO:BP response to epidermal growth factor; q_global = 0.0474) and (GO:BP cellular response to epidermal growth factor stimulus; q_global = 0.0474); no STRING functional-enrichment term was reported.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: the HPA summary identifies only a single secreted gene, and most proteins are intracellular or membrane-associated. It is also not strongly blood-cell specific. Most genes have low immune-cell specificity, although selected genes show enrichment in platelets, megakaryocyte-related cells, erythrocyte progenitors, neutrophils, basophils, or eosinophils. Most genes have low tissue specificity, while isolated genes are enriched in intestine, skeletal muscle, testis, blood vessel, or brain. Several genes show cell-type enhancement in spermatogenic cells and other specialized cell types. Protein detection is similar in bone marrow and liver for the genes with available HPA evidence, but CSE1L and CASP3 are not detected in one or both listed tissues and VIL1 is detected in liver but not bone marrow. Overall, the shared signal could reflect a broadly expressed cellular program present in both tissues, with possible contributions from shared or variable cell populations, rather than a plasma-protein or uniform immune-cell signature.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP response to epidermal growth factor | 0.0474 | CAD, DUSP3, VIL1 |
| GO:BP cellular response to epidermal growth factor stimulus | 0.0474 | CAD, DUSP3, VIL1 |

### STRING and hu.MAP

STRING provides only a small set of high-confidence pairwise relationships and no functional-enrichment result. The known relationships are CAD with GMPS, CASP3 with PRKDC, and FARSB with GMPS. These links support nucleotide biosynthesis, translation-related biology, and an apoptosis or DNA-damage connection, but they do not by themselves define the entire co-abundance module. hu.MAP provides two partial complex matches. (hu.MAP huMAP3_09042.1) connects CIAO1, CSE1L, and PRKDC within a larger complex, while (hu.MAP huMAP3_09592.1) connects CSE1L and PRKDC within a much broader complex. The overlap with these complexes supports genuine molecular relationships for the CSE1L–PRKDC-centered portion of the module, but the partial overlap and broad complex membership argue against treating either complex as the identity of the whole module. The difference between the dense co-abundance structure and the sparse catalogued interaction structure suggests that co-abundance captures shared cellular state, regulation, or indirect relationships in addition to direct physical interaction.

**STRING interactions (score >= 0.7)**: 3 of 136 gene pairs: CAD–GMPS (0.749); CASP3–PRKDC (0.732); FARSB–GMPS (0.727)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09042.1 (CIAO1, CSE1L, PRKDC; 3/26); huMAP3_09592.1 (CSE1L, PRKDC; 2/95)

### Novelty

This may be a new tissue-pair co-abundance observation, but the fact sheet does not establish that it is a newly discovered molecular pathway or complex. The module contains well-studied genes with established roles in EGFR or MAPK signaling, nucleotide metabolism, apoptosis, DNA repair, protein targeting, and cytoskeletal organization. Most module edges are not represented by the reported STRING or hu.MAP evidence, which makes the particular co-abundance arrangement interesting, but absence from those resources does not prove novelty because such databases are incomplete and primarily describe curated or experimentally supported molecular relationships. A defensible novelty claim would require comparison with prior co-expression modules, tissue-specific datasets, perturbation studies, and independent cohorts. At present, the appropriate conclusion is that the shared bone-marrow–liver module is a potentially novel systems-level pattern built from largely known gene functions.

**Hypothesis.** Hypothesis: the module reflects a conserved proliferative or adaptive cellular state in which EGFR-related signaling induces cytoskeletal and epithelial-state remodeling through VIL1, is tuned by the negative regulator DUSP3, and is supported by CAD-dependent nucleotide production for biosynthetic demand. The associated mitochondrial, apoptotic, DNA-repair, translation, and nuclear-transport genes may represent the downstream resource-management and stress-response machinery required to maintain this state. This hypothesis predicts that module activity should track EGFR or MAPK activity, epithelial or cell-shape remodeling, and nucleotide demand, while varying with the cellular composition of bone marrow and liver samples. It remains a hypothesis because co-abundance does not demonstrate regulatory direction, physical interaction, or causal dependence.

### Important genes

#### VIL1

- **Related proteins** (co-abundance neighbors): LUC7L2 (0.90), CAD (0.88), CSE1L (0.88), CASP3 (0.86), DNM1L (0.85), MACROH2A1 (0.83), PRKDC (0.81), YWHAH (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: villin 1. This gene encodes a member of a family of calcium-regulated actin-binding proteins.  This protein represents a dominant part of the brush border cytoskeleton which functions in the capping, severing, and bundling of actin filaments.  Two mRNAs of 2.7 kb and 3.5 kb have been observed; they result from utilization of alternate poly-adenylation signals present in the terminal exon. [provided by RefSe…
- **Diseases (Open Targets)**: brain aneurysm (0.220); Barrett esophagus (0.084); neoplasm (0.067); cervical adenocarcinoma (0.061); esophageal adenocarcinoma (0.057)
- **Europe PMC papers**: 1564
- **Why important**: VIL1 is the central network hub by weighted connectivity and is one of the three genes supporting (GO:BP response to epidermal growth factor; q_global = 0.0474) and (GO:BP cellular response to epidermal growth factor stimulus; q_global = 0.0474). Its established function as a calcium-regulated actin-binding protein, together with annotations for epithelial glucose absorption, actin organization, cell shape, and EGFR signaling, makes it a strong bridge between the module's signaling and structural features. Its intestine-enriched HPA pattern and extensive literature support biological interpretability, while its liver detection and absence of bone-marrow detection caution against assuming that it represents the same cell type in both tissues.
- **Conclusion**: Established evidence supports VIL1 as the module's structural and EGFR-response anchor. The hypothesis that VIL1 transduces the shared tissue signal into coordinated cytoskeletal remodeling is plausible but requires perturbation or activity-based validation.

#### CAD

- **Related proteins** (co-abundance neighbors): VIL1 (0.88), GMPS (0.85), SRP72 (0.84), SLC3A2 (0.82); STRING partners: GMPS (0.749)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carbamoyl-phosphate synthetase 2, aspartate transcarbamylase, and dihydroorotase. The de novo synthesis of pyrimidine nucleotides is required for mammalian cells to proliferate. This gene encodes a trifunctional protein which is associated with the enzymatic activities of the first 3 enzymes in the 6-step pathway of pyrimidine biosynthesis: carbamoylphosphate synthetase (CPS II), aspartate transcarbamoylase, and dihydroorotase. This protein is regulated by the mitogen-activated…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 50 (0.660); congenital disorder of glycosylation type I (0.595); infantile epileptic-dyskinetic encephalopathy (0.499); type 2 diabetes mellitus (0.286); urolithiasis (0.283)
- **Europe PMC papers**: 60667
- **Why important**: CAD has substantial network connectivity and is present in both globally corrected terms (GO:BP response to epidermal growth factor; q_global = 0.0474) and (GO:BP cellular response to epidermal growth factor stimulus; q_global = 0.0474). It encodes the multifunctional enzyme for de novo pyrimidine biosynthesis, and its regulation by the MAPK cascade provides a direct mechanistic connection between growth-factor signaling and nucleotide supply. The CAD–GMPS STRING relationship further links pyrimidine and purine biosynthetic capacity within the module. CAD has extensive literature and disease-resource coverage, making it one of the most established functional interpreters of the module.
- **Conclusion**: Established evidence supports CAD as a biosynthetic effector associated with the EGFR-responsive state. It is reasonable to hypothesize that CAD helps couple signaling to proliferative or repair-related nucleotide demand, but the co-abundance data do not establish that CAD activity drives the module.

#### DUSP3

- **Related proteins** (co-abundance neighbors): LUC7L2 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dual specificity phosphatase 3. The protein encoded by this gene is a member of the dual specificity protein phosphatase subfamily. These phosphatases inactivate their target kinases by dephosphorylating both the phosphoserine/threonine and phosphotyrosine residues. They negatively regulate members of the mitogen-activated protein (MAP) kinase superfamily (MAPK/ERK, SAPK/JNK, p38), which are associated with cellular proliferatio…
- **Diseases (Open Targets)**: coronary artery disorder (0.231); metabolic syndrome (0.186); neoplasm (0.089); osteosarcoma (0.074); hyperinsulinism due to INSR deficiency (0.057)
- **Europe PMC papers**: 1055
- **Why important**: DUSP3 is one of the genes directly supporting (GO:BP response to epidermal growth factor; q_global = 0.0474) and (GO:BP cellular response to epidermal growth factor stimulus; q_global = 0.0474). Its established phosphatase activity negatively regulates EGFR signaling and MAPK-family pathways, giving it a plausible feedback role within an EGFR-responsive module. Its network connection to LUC7L2 and tissue enhancement in skeletal muscle add context, while its literature and disease associations support relevance beyond a purely computational annotation.
- **Conclusion**: Established evidence supports DUSP3 as a negative regulator that can constrain growth-factor and MAPK signaling. The hypothesis that DUSP3 creates feedback stabilization of the shared module is biologically coherent, but directionality and tissue-specific action remain untested.

#### PRKDC

- **Related proteins** (co-abundance neighbors): VIL1 (0.81); STRING partners: CASP3 (0.732)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: huMAP3_09042.1, huMAP3_09592.1
- **Function (MyGene.info)**: protein kinase, DNA-activated, catalytic subunit. This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to DNA-PKcs deficiency (0.752); neurodegenerative disease (0.548); severe combined immunodeficiency (0.470); combined immunodeficiency (0.464); ovarian neoplasm (0.210)
- **Europe PMC papers**: 12461
- **Why important**: PRKDC is connected to VIL1 in the co-abundance network and is supported by both hu.MAP complex evidence (hu.MAP huMAP3_09042.1) and (hu.MAP huMAP3_09592.1). Its established role as the catalytic subunit of DNA-dependent protein kinase links the module to DNA double-strand-break repair, recombination, telomere maintenance, and innate immune signaling. The STRING relationship with CASP3 connects DNA-damage handling with apoptosis, and PRKDC has extensive literature and strong disease relevance, including immunodeficiency.
- **Conclusion**: Established evidence supports PRKDC as a DNA-repair and genome-surveillance component of the module, with additional support from catalogued complexes and its CASP3 relationship. The hypothesis that PRKDC marks a shared genome-stress or survival state in bone marrow and liver is plausible, but the module does not show whether DNA damage is a cause or consequence of the co-abundance pattern.

## Module 1

**Tissue pair**: bone_marrow and liver  
**Genes (22)**: PGD, BAX, ADAR, TUFM, GFPT1, HYOU1, SNU13, ALDH18A1, PSMC4, PSMC2, PSMD13, CTPS1, RECQL, DARS1, EPRS1, NARS1, RARS1, TARS1, WARS1, CCT7, VPS35, XRCC6

### Function

The module is best interpreted as a conserved core of cellular protein production and proteostasis. The strongest primary evidence is coordinated aminoacyl-tRNA charging and tRNA metabolism through DARS1, EPRS1, NARS1, RARS1, TARS1, and WARS1, supported by the globally corrected terms for aminoacyl-tRNA ligase activity, tRNA aminoacylation, amino acid activation, tRNA metabolic process, and aminoacyl-tRNA biosynthesis (GO:MF catalytic activity, acting on a tRNA; q_global = 0.000996) (GO:MF aminoacyl-tRNA ligase activity; q_global = 0.00623) (GO:BP tRNA aminoacylation for protein translation; q_global = 0.00623) (GO:BP amino acid activation; q_global = 0.00623) (GO:BP tRNA aminoacylation; q_global = 0.00623) (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 0.00623) (GO:BP tRNA metabolic process; q_global = 0.0277). Broad nucleotide and ATP-binding enrichment (GO:MF adenyl nucleotide binding; q_global = 0.000558) (GO:MF ATP binding; q_global = 0.000585) (GO:MF adenyl ribonucleotide binding; q_global = 0.000618) (GO:MF purine nucleotide binding; q_global = 0.000972) (GO:MF purine ribonucleoside triphosphate binding; q_global = 0.00128) (GO:MF purine ribonucleotide binding; q_global = 0.00134) (GO:MF ribonucleotide binding; q_global = 0.00152) (GO:MF nucleotide binding; q_global = 0.00369) (GO:MF nucleoside phosphate binding; q_global = 0.0047) is consistent with the energy requirements of translation, proteasome activity, chaperoning, DNA repair, and nucleotide metabolism. The module also contains a proteasome regulatory component through PSMC2, PSMC4, and PSMD13, a protein-folding component through CCT7, stress and secretory-folding biology through HYOU1, DNA repair factors through RECQL and XRCC6, nucleotide biosynthesis through CTPS1 and PGD, and mitochondrial or amino-acid metabolism through TUFM, ALDH18A1, and GFPT1. The intracellular protein-containing-complex signal (GO:CC intracellular protein-containing complex; q_global = 0.0242) supports a multi-process cellular maintenance module rather than a narrowly tissue-specific pathway. The biological interpretation is therefore coordinated translational capacity with quality control, metabolic support, and genome-protection functions.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only one secreted gene, and the listed proteins are predominantly intracellular. It is also not strongly blood-cell specific overall. Most genes have low tissue specificity and most have low immune-cell specificity, although PGD is enriched in bone marrow and several myeloid populations, WARS1 has immune-cell enhancement in monocytes, and individual genes show enrichment in neutrophils, megakaryocytes, or other cell types. HPA detects most module proteins in bone marrow and many in liver, while several are not detected in one of those tissues. The module therefore could partly reflect shared cellular abundance or common housekeeping demands in the two tissues, rather than a dedicated bone-marrow or liver program. Its apparent conservation is compatible with broadly expressed translational, proteasomal, metabolic, and DNA-maintenance machinery. Cell-type-enhanced annotations are widespread, including reproductive, epithelial, placental, hepatocyte, plasma-cell, and myeloid populations, so bulk-tissue co-abundance should not be interpreted as evidence that every member acts in the same specialized cell.

**GO/KEGG enrichment**: 22 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF adenyl nucleotide binding | 0.000558 | ALDH18A1, CCT7, CTPS1, DARS1, EPRS1, HYOU1, NARS1, PGD, PSMC2, PSMC4, RARS1, RECQL, TARS1, WARS1, XRCC6 |
| GO:MF ATP binding | 0.000585 | ALDH18A1, CCT7, CTPS1, DARS1, EPRS1, HYOU1, NARS1, PSMC2, PSMC4, RARS1, RECQL, TARS1, WARS1, XRCC6 |
| GO:MF adenyl ribonucleotide binding | 0.000618 | ALDH18A1, CCT7, CTPS1, DARS1, EPRS1, HYOU1, NARS1, PSMC2, PSMC4, RARS1, RECQL, TARS1, WARS1, XRCC6 |
| GO:MF purine nucleotide binding | 0.000972 | ALDH18A1, CCT7, CTPS1, DARS1, EPRS1, HYOU1, NARS1, PGD, PSMC2, PSMC4, RARS1, RECQL, TARS1, TUFM, WARS1, XRCC6 |
| GO:MF catalytic activity, acting on a tRNA | 0.000996 | ADAR, DARS1, EPRS1, NARS1, RARS1, TARS1, WARS1 |
| GO:MF carbohydrate derivative binding | 0.00105 | ALDH18A1, CCT7, CTPS1, DARS1, EPRS1, GFPT1, HYOU1, NARS1, PSMC2, PSMC4, RARS1, RECQL, TARS1, TUFM, WARS1, XRCC6 |
| GO:MF purine ribonucleoside triphosphate binding | 0.00128 | ALDH18A1, CCT7, CTPS1, DARS1, EPRS1, HYOU1, NARS1, PSMC2, PSMC4, RARS1, RECQL, TARS1, TUFM, WARS1, XRCC6 |
| GO:MF purine ribonucleotide binding | 0.00134 | ALDH18A1, CCT7, CTPS1, DARS1, EPRS1, HYOU1, NARS1, PSMC2, PSMC4, RARS1, RECQL, TARS1, TUFM, WARS1, XRCC6 |
| GO:MF ribonucleotide binding | 0.00152 | ALDH18A1, CCT7, CTPS1, DARS1, EPRS1, HYOU1, NARS1, PSMC2, PSMC4, RARS1, RECQL, TARS1, TUFM, WARS1, XRCC6 |
| GO:MF catalytic activity, acting on a nucleic acid | 0.00192 | ADAR, DARS1, EPRS1, NARS1, RARS1, RECQL, TARS1, WARS1, XRCC6 |
| GO:MF nucleotide binding | 0.00369 | ALDH18A1, CCT7, CTPS1, DARS1, EPRS1, HYOU1, NARS1, PGD, PSMC2, PSMC4, RARS1, RECQL, TARS1, TUFM, WARS1, XRCC6 |
| GO:MF nucleoside phosphate binding | 0.0047 | ALDH18A1, CCT7, CTPS1, DARS1, EPRS1, HYOU1, NARS1, PGD, PSMC2, PSMC4, RARS1, RECQL, TARS1, TUFM, WARS1, XRCC6 |
| GO:MF aminoacyl-tRNA ligase activity | 0.00623 | DARS1, EPRS1, NARS1, RARS1, TARS1, WARS1 |
| GO:BP tRNA aminoacylation for protein translation | 0.00623 | DARS1, EPRS1, NARS1, RARS1, TARS1, WARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 0.00623 | DARS1, EPRS1, NARS1, RARS1, TARS1, WARS1 |

### STRING and hu.MAP

STRING provides established relationships within several coherent submodules. The aminoacyl-tRNA synthetases show strong interconnections, especially EPRS1 with DARS1, NARS1, RARS1, and TARS1, and additional links among NARS1, RARS1, TARS1, and WARS1. These relationships independently reinforce the translation and tRNA-aminoacylation interpretation, although the STRING enrichment is supplementary rather than primary global evidence. PSMC2, PSMC4, and PSMD13 form a known proteasome-associated group in STRING and occur together in several hu.MAP proteasome complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). EPRS1, DARS1, TARS1, and RARS1 occur together in hu.MAP complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), providing complex-level support for an aminoacylation assembly or associated synthetase machinery. NARS1 and RECQL share hu.MAP associations (hu.MAP huMAP3_10088.1) (hu.MAP huMAP3_10115.1) (hu.MAP huMAP3_14982.1), while RECQL and XRCC6 have a strong STRING relationship consistent with DNA-repair biology. The module therefore contains substantial previously known interaction structure, but many co-abundance edges are not represented by high-confidence STRING links and several genes have no hu.MAP complex assignment. This pattern suggests a biologically connected module assembled from multiple established cellular systems, not necessarily one physical complex.

**STRING interactions (score >= 0.7)**: 21 of 231 gene pairs: ALDH18A1–CTPS1 (0.85); ALDH18A1–EPRS1 (0.723); BAX–XRCC6 (0.972); CTPS1–EPRS1 (0.798); CTPS1–RARS1 (0.739); DARS1–EPRS1 (0.999); DARS1–RARS1 (0.996); EPRS1–NARS1 (0.998); EPRS1–RARS1 (0.999); EPRS1–TARS1 (0.928); EPRS1–WARS1 (0.715); NARS1–RARS1 (0.909); NARS1–TARS1 (0.924); NARS1–WARS1 (0.84); PSMC2–PSMC4 (0.999); PSMC2–PSMD13 (0.999); PSMC4–PSMD13 (0.999); RARS1–TARS1 (0.806); RARS1–WARS1 (0.796); RECQL–XRCC6 (0.898); TARS1–WARS1 (0.818)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword ATP-binding (FDR = 4.61e-05, 14 genes); Keyword Nucleotide-binding (FDR = 0.0001, 15 genes); Function ATP binding (FDR = 0.00024, 14 genes); Function Purine ribonucleotide binding (FDR = 0.00024, 15 genes); Function Purine ribonucleoside triphosphate binding (FDR = 0.00024, 15 genes); Function Carbohydrate derivative binding (FDR = 0.00024, 16 genes); Function Nucleotide binding (FDR = 0.00035, 16 genes); Function aminoacyl-tRNA ligase activity (FDR = 0.00072, 6 genes); Function Catalytic activity, acting on a nucleic acid (FDR = 0.00072, 8 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 0.001, 6 genes); Keyword Protein biosynthesis (FDR = 0.001, 7 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 0.0018, 6 genes); RCTM Cytosolic tRNA aminoacylation (FDR = 0.0026, 6 genes); TISSUES Lymphoblast (FDR = 0.0035, 8 genes); Keyword Ligase (FDR = 0.0037, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, DARS1, TARS1, RARS1; 4/14); huMAP3_13688.1 (EPRS1, DARS1, TARS1, RARS1; 4/14); huMAP3_05064.1 (PSMC2, PSMC4, PSMD13; 3/31); huMAP3_09656.1 (PSMC2, PSMC4, PSMD13; 3/64); huMAP3_13725.1 (PSMC2, PSMC4, PSMD13; 3/69); huMAP3_10088.1 (NARS1, RECQL; 2/10); huMAP3_10115.1 (NARS1, RECQL; 2/14); huMAP3_14982.1 (NARS1, RECQL; 2/28)

### Novelty

This module should not be called a wholly new molecular complex or a newly discovered pathway. Its central processes, including aminoacyl-tRNA biosynthesis, proteasome function, chaperoning, DNA repair, and nucleotide metabolism, are established, and several of its relationships are already represented in STRING and hu.MAP. The potentially novel aspect is the conserved co-abundance organization across bone marrow and liver, particularly the coordinated coupling of translation machinery with proteasome, metabolic, stress-response, and genome-maintenance genes. That organization may be a new systems-level observation, but novelty cannot be established from the fact sheet alone. The absence of some edges from STRING or complexes from hu.MAP is not evidence of novelty, because database coverage, assay context, cell composition, and condition dependence can explain missing relationships. Independent replication in additional cohorts, comparison with published tissue co-expression modules, and perturbation or protein-level validation would be needed to support a claim of a new module.

**Hypothesis.** Hypothesis: the conserved module represents a shared cellular-resource and quality-control program that maintains protein synthesis in metabolically active or renewing cells while coupling translation to folding, degradation, nucleotide supply, mitochondrial translation, and repair of replication or DNA damage. In bone marrow, this program could support proliferating and differentiating hematopoietic cells; in liver, it could support hepatocyte biosynthetic and metabolic activity. The aminoacyl-tRNA synthetase group may provide the translational core, with CCT7 and HYOU1 buffering folding stress, the proteasome components removing damaged or misfolded proteins, GFPT1, CTPS1, PGD, and ALDH18A1 supplying metabolic or nucleotide resources, and RECQL, XRCC6, and ADAR helping manage genome or RNA integrity. This is a mechanistic model inferred from co-abundance and established annotations, not proof of direct regulation or physical co-assembly. A testable prediction is that perturbing translational or proteotoxic stress should coordinately alter these module genes in both tissues, while cell-type deconvolution should determine how much of the signal comes from shared cell populations.

### Important genes

#### EPRS1

- **Related proteins** (co-abundance neighbors): RECQL (0.86), CTPS1 (0.85), SNU13 (0.85), CCT7 (0.83), PSMC2 (0.83), RARS1 (0.83), GFPT1 (0.83), TARS1 (0.82), XRCC6 (0.82), ALDH18A1 (0.81); STRING partners: ALDH18A1 (0.723), CTPS1 (0.798), DARS1 (0.999), NARS1 (0.998), RARS1 (0.999), TARS1 (0.928), WARS1 (0.715)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is the highest-connectivity translational hub among the selected genes and links the aminoacyl-tRNA synthetase group to CTPS1, CCT7, RECQL, PSMC2, and GFPT1. It is present in every primary enrichment category listed for the module (GO:MF adenyl nucleotide binding; q_global = 0.000558) through (GO:MF catalytic activity, acting on RNA; q_global = 0.0447), in all supplementary STRING terms (STRING Keyword ATP-binding; within-query FDR = 4.61e-05) through (STRING Keyword Ligase; within-query FDR = 0.0037), in the hu.MAP aminoacylation complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), and in numerous high-confidence STRING relationships. Its established function is dual glutamyl- and prolyl-tRNA charging, and its disease associations include hypomyelinating leukodystrophy and developmental disorders. Its literature volume is substantial, supporting a well-established biological role.
- **Conclusion**: Established evidence supports EPRS1 as a central translational hub and a strong anchor for the module's aminoacylation interpretation. The hypothesis that EPRS1 coordinates translation with proteostasis and metabolism in both tissues is plausible from its network position, but direct cross-tissue regulatory action is not established.

#### RARS1

- **Related proteins** (co-abundance neighbors): GFPT1 (0.88), ALDH18A1 (0.86), PSMD13 (0.85), EPRS1 (0.83), VPS35 (0.81), CTPS1 (0.80); STRING partners: CTPS1 (0.739), DARS1 (0.996), EPRS1 (0.999), NARS1 (0.909), TARS1 (0.806), WARS1 (0.796)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 is a high-connectivity member of the aminoacyl-tRNA synthetase core and connects that core to GFPT1, ALDH18A1, CTPS1, and PSMD13. It appears in all primary enrichment terms (GO:MF adenyl nucleotide binding; q_global = 0.000558) through (GO:MF catalytic activity, acting on RNA; q_global = 0.0447), all aminoacylation-related STRING terms, and both hu.MAP aminoacylation complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). STRING supports strong relationships with EPRS1, DARS1, NARS1, TARS1, and WARS1. RARS1 charges arginyl-tRNA, and its disease associations include hypomyelinating leukodystrophy and other hereditary disorders.
- **Conclusion**: Established evidence identifies RARS1 as a core component of the module's tRNA-charging machinery and as an important bridge between translation and the broader network. Its co-abundance with metabolic and proteasomal genes suggests coordinated cellular demand, but a specific causal role in the bone-marrow and liver relationship remains a hypothesis.

#### PSMC2

- **Related proteins** (co-abundance neighbors): CTPS1 (0.88), GFPT1 (0.87), TARS1 (0.86), PSMC4 (0.85), TUFM (0.84), ADAR (0.84), RECQL (0.83), EPRS1 (0.83); STRING partners: PSMC4 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is a prominent network connector between the translational, metabolic, stress, and DNA-maintenance portions of the module. It belongs to the ATP-dependent proteasome regulatory machinery, is linked in STRING to PSMC4 and PSMD13, and occurs in multiple hu.MAP proteasome complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). It contributes to the broad primary nucleotide-binding and intracellular-complex signals (GO:MF adenyl nucleotide binding; q_global = 0.000558) (GO:MF ATP binding; q_global = 0.000585) (GO:MF purine nucleotide binding; q_global = 0.000972) (GO:MF carbohydrate derivative binding; q_global = 0.00105) (GO:MF purine ribonucleoside triphosphate binding; q_global = 0.00128) (GO:MF purine ribonucleotide binding; q_global = 0.00134) (GO:MF ribonucleotide binding; q_global = 0.00152) (GO:MF nucleotide binding; q_global = 0.00369) (GO:MF nucleoside phosphate binding; q_global = 0.0047) (GO:MF heterocyclic compound binding; q_global = 0.0119) (GO:CC intracellular protein-containing complex; q_global = 0.0242). It is detected in both bone marrow and liver, and its disease associations include plasma-cell myeloma, lymphoma, neoplasia, HIV disease, and amyloidosis.
- **Conclusion**: Established evidence supports PSMC2 as the principal proteasome-linked component selected here and as evidence that the module includes protein quality control rather than translation alone. Its position suggests coupling between protein synthesis and degradation, but the co-abundance data do not demonstrate that PSMC2 regulates the aminoacyl-tRNA synthetases.

#### RECQL

- **Related proteins** (co-abundance neighbors): WARS1 (0.87), PSMC4 (0.86), EPRS1 (0.86), CTPS1 (0.84), PSMC2 (0.83), CCT7 (0.82), XRCC6 (0.80), PGD (0.80); STRING partners: XRCC6 (0.898)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: huMAP3_10088.1, huMAP3_10115.1, huMAP3_14982.1
- **Function (MyGene.info)**: RecQ like helicase. The protein encoded by this gene is a member of the RecQ DNA helicase family. DNA helicases are enzymes involved in various types of DNA repair, including mismatch repair, nucleotide excision repair and direct repair. The encoded protein is involved in the processing of Holliday junctions, the suppression of sister chromatid exchanges, telomere maintenance, and is required for genotoxic stress res…
- **Diseases (Open Targets)**: RECON progeroid syndrome (0.595); hereditary neoplastic syndrome (0.505); obesity disorder (0.404); myofibrillar myopathy 8 (0.334); hereditary breast ovarian cancer syndrome (0.328)
- **Europe PMC papers**: 954
- **Why important**: RECQL has high network connectivity and links the translational and proteasomal portions of the module with XRCC6 and PGD. Its established function is a RecQ-family DNA helicase involved in DNA repair, replication-fork processing, recombination, telomere maintenance, and resistance to genotoxic stress. It is represented in the globally corrected nucleotide and nucleic-acid catalytic terms (GO:MF adenyl nucleotide binding; q_global = 0.000558) (GO:MF ATP binding; q_global = 0.000585) (GO:MF purine nucleotide binding; q_global = 0.000972) (GO:MF carbohydrate derivative binding; q_global = 0.00105) (GO:MF purine ribonucleoside triphosphate binding; q_global = 0.00128) (GO:MF purine ribonucleotide binding; q_global = 0.00134) (GO:MF ribonucleotide binding; q_global = 0.00152) (GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.00192) (GO:MF nucleotide binding; q_global = 0.00369) (GO:MF nucleoside phosphate binding; q_global = 0.0047) (GO:MF heterocyclic compound binding; q_global = 0.0119) and has a strong STRING relationship with XRCC6. It also occurs in hu.MAP complexes with NARS1 (hu.MAP huMAP3_10088.1) (hu.MAP huMAP3_10115.1) (hu.MAP huMAP3_14982.1). Its disease associations include RECQL-related progeroid and hereditary neoplastic syndromes.
- **Conclusion**: Established evidence supports RECQL as the genome-maintenance arm of the module and as a bridge between DNA repair and the broader cellular maintenance program. Its connection to aminoacylation complexes is an association in the available data, not proof that RECQL physically participates in tRNA charging.

#### GFPT1

- **Related proteins** (co-abundance neighbors): RARS1 (0.88), PSMC2 (0.87), HYOU1 (0.85), PSMD13 (0.84), TUFM (0.84), EPRS1 (0.83), NARS1 (0.82), ALDH18A1 (0.81), DARS1 (0.81), WARS1 (0.81), SNU13 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamine--fructose-6-phosphate transaminase 1. This gene encodes the first and rate-limiting enzyme of the hexosamine pathway and controls the flux of glucose into the hexosamine pathway. The product of this gene catalyzes the formation of glucosamine 6-phosphate. [provided by RefSeq, Sep 2008].
- **Diseases (Open Targets)**: congenital myasthenic syndrome (0.819); neurodegenerative disease (0.559); congenital myasthenic syndromes with glycosylation defect (0.503); spinal stenosis (0.379); congenital disorder of glycosylation type I (0.370)
- **Europe PMC papers**: 1684
- **Why important**: GFPT1 has the strongest network position in the module and connects aminoacylation, proteasome, mitochondrial, stress, and metabolic genes. It is the rate-limiting enzyme of the hexosamine pathway and supports glucosamine and UDP-linked carbohydrate biosynthesis. It contributes to the primary carbohydrate-derivative binding signal (GO:MF carbohydrate derivative binding; q_global = 0.00105) and the corresponding supplementary STRING signal (STRING Function Carbohydrate derivative binding; within-query FDR = 0.00024), while its network neighbors include RARS1, PSMC2, HYOU1, PSMD13, TUFM, EPRS1, and NARS1. Its disease associations include congenital myasthenic and glycosylation disorders, and it has substantial literature support.
- **Conclusion**: Established evidence supports GFPT1 as a metabolic resource node that may help explain why the translation and proteostasis machinery co-varies with carbohydrate metabolism. The proposed role as a nutrient-sensitive coordinator of the module is a hypothesis rather than a demonstrated regulatory mechanism.

## Module 2

**Tissue pair**: bone_marrow and liver  
**Genes (33)**: ABCF1, ATP1A1, ATP2A2, CLTC, COPB1, DCTN1, DHX9, EIF3C, EIF3L, EZR, FKBP4, HSPH1, EIF4G1, GART, ADSL, RSL1D1, RPL3, SNRPA1, SF3A1, SF3B3, SUPT16H, SPTBN1, SPTAN1, SRP68, IARS1, KARS1, MARS1, VARS1, YARS1, SNRNP200, EFTUD2, UBA6, XPO1

### Function

This is primarily a conserved intracellular RNA and protein-biosynthesis module. The strongest primary evidence is for RNA binding and nucleic-acid binding (GO:MF RNA binding; q_global = 3.14e-07) (GO:MF nucleic acid binding; q_global = 4.65e-06), ribonucleoprotein and protein-containing complexes (GO:CC ribonucleoprotein complex; q_global = 0.00137) (GO:CC protein-containing complex; q_global = 0.0018), protein–RNA complex assembly and organization (GO:BP protein-RNA complex assembly; q_global = 0.0026) (GO:BP protein-RNA complex organization; q_global = 0.00332), ribonucleoprotein-complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.00527), translation and protein biosynthesis (GO:BP translation; q_global = 0.0109) (GO:BP protein biosynthetic process; q_global = 0.0109), and multiple U2 and catalytic spliceosome categories (7 globally significant GO/KEGG terms, q_global 0.0138–0.0448; see the table). The module therefore links pre-mRNA splicing, RNA handling, translation initiation and elongation, aminoacyl-tRNA charging, ribosome-associated processes, and nuclear export. ATP and adenyl-ribonucleotide binding (GO:MF ATP binding; q_global = 0.0248) (GO:MF adenyl ribonucleotide binding; q_global = 0.0261) are consistent with the enzymatic and energy-dependent nature of several components. The broad macromolecule-biosynthesis signal (GO:BP macromolecule biosynthetic process; q_global = 0.0418) supports a general gene-expression and proteostasis function rather than a tissue-specific metabolic pathway. This interpretation is reinforced, but not independently globally corrected, by STRING annotations for RNA binding, ribonucleoprotein complexes, ribonucleoprotein-complex biogenesis, translation, and protein-containing complexes (7 supplementary STRING terms; within-query FDR 5.28e-07–0.0036).

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a single secreted gene, and most genes are intracellular with cytosolic, nucleoplasmic, nucleolar, membrane, vesicular, or cytoskeletal localizations. It is also not blood-cell enriched by HPA: nearly all genes have low immune-cell specificity, with no recurrent enriched blood-cell category. Most genes have low tissue specificity, which is compatible with a broadly expressed housekeeping-like program required for RNA processing, translation, transport, and protein quality control. Some cell-type-enhanced signals occur in diverse specialized cell types, including erythrocyte progenitors, neutrophils, monocytes, cardiomyocytes, epithelial cells, and reproductive cells, but these are heterogeneous rather than evidence for a single blood-cell population. The shared bone-marrow–liver signal is therefore more plausibly a conserved intracellular gene-expression program, although sample composition and shared proliferative or metabolically active cell states could contribute.

**GO/KEGG enrichment**: 20 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF RNA binding | 3.14e-07 | ABCF1, ATP2A2, CLTC, DHX9, EFTUD2, EIF3C, EIF3L, EIF4G1, EZR, FKBP4, IARS1, KARS1, MARS1, RPL3, RSL1D1, SF3A1, SF3B3, SNRNP200, SNRPA1, SPTBN1, SRP68, SUPT16H, XPO1, YARS1 |
| GO:MF nucleic acid binding | 4.65e-06 | ABCF1, ATP2A2, CLTC, DHX9, EFTUD2, EIF3C, EIF3L, EIF4G1, EZR, FKBP4, IARS1, KARS1, MARS1, RPL3, RSL1D1, SF3A1, SF3B3, SNRNP200, SNRPA1, SPTBN1, SRP68, SUPT16H, XPO1, YARS1 |
| GO:CC ribonucleoprotein complex | 0.00137 | DHX9, EFTUD2, EIF3C, EIF3L, RPL3, SF3A1, SF3B3, SNRNP200, SNRPA1, SRP68, XPO1 |
| GO:CC protein-containing complex | 0.0018 | ADSL, ATP1A1, ATP2A2, CLTC, COPB1, DCTN1, DHX9, EFTUD2, EIF3C, EIF3L, EIF4G1, EZR, FKBP4, HSPH1, IARS1, KARS1, MARS1, RPL3, SF3A1, SF3B3, SNRNP200, SNRPA1, SPTAN1, SPTBN1, SRP68, SUPT16H, XPO1 |
| GO:BP protein-RNA complex assembly | 0.0026 | DHX9, EIF3C, EIF3L, SF3A1, SF3B3, SNRNP200, SNRPA1 |
| GO:BP protein-RNA complex organization | 0.00332 | DHX9, EIF3C, EIF3L, SF3A1, SF3B3, SNRNP200, SNRPA1 |
| GO:BP ribonucleoprotein complex biogenesis | 0.00527 | DHX9, EIF3C, EIF3L, SF3A1, SF3B3, SNRNP200, SNRPA1, XPO1 |
| GO:BP translation | 0.0109 | ABCF1, DHX9, EIF3C, EIF3L, EIF4G1, IARS1, KARS1, MARS1, RPL3, VARS1, YARS1 |
| GO:BP protein biosynthetic process | 0.0109 | ABCF1, DHX9, EIF3C, EIF3L, EIF4G1, IARS1, KARS1, MARS1, RPL3, VARS1, YARS1 |
| GO:CC U2-type precatalytic spliceosome | 0.0138 | EFTUD2, SF3A1, SF3B3, SNRNP200, SNRPA1 |
| GO:CC precatalytic spliceosome | 0.0138 | EFTUD2, SF3A1, SF3B3, SNRNP200, SNRPA1 |
| GO:CC catalytic step 2 spliceosome | 0.0193 | EFTUD2, SF3A1, SF3B3, SNRNP200, SNRPA1 |
| GO:CC nuclear lumen | 0.0209 | ABCF1, DHX9, EFTUD2, EIF3L, EZR, FKBP4, HSPH1, IARS1, KARS1, MARS1, RPL3, RSL1D1, SF3A1, SF3B3, SNRNP200, SNRPA1, SPTBN1, SRP68, SUPT16H, XPO1, YARS1 |
| GO:MF ATP binding | 0.0248 | ABCF1, ATP1A1, ATP2A2, DHX9, EIF4G1, FKBP4, GART, HSPH1, IARS1, KARS1, MARS1, SNRNP200, UBA6, VARS1, YARS1 |
| GO:MF adenyl ribonucleotide binding | 0.0261 | ABCF1, ATP1A1, ATP2A2, DHX9, EIF4G1, FKBP4, GART, HSPH1, IARS1, KARS1, MARS1, SNRNP200, UBA6, VARS1, YARS1 |

### STRING and hu.MAP

STRING contains established high-confidence relationships within several coherent submodules. The spliceosomal group includes EFTUD2, SF3A1, SF3B3, SNRNP200, and SNRPA1, with dense mutual STRING support. The translation-initiation group includes EIF3C, EIF3L, and EIF4G1. The aminoacyl-tRNA synthetase group includes IARS1, KARS1, MARS1, VARS1, and YARS1. ATP1A1 and ATP2A2 form a transporter and calcium-homeostasis pair, while SPTAN1 and SPTBN1 form a spectrin pair. DHX9 connects RNA helicase activity to spliceosomal, export, and translation-related genes. These relationships show that the module is not merely a collection of unrelated co-abundant genes; important parts correspond to known molecular systems. hu.MAP independently supports the U-two and spliceosomal assemblies (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_00960.1) (hu.MAP huMAP3_07622.1) (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_04549.1) (hu.MAP huMAP3_09945.1), aminoacyl-tRNA synthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), translation-initiation complexes (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1) (hu.MAP huMAP3_01276.1), and spectrin complexes (hu.MAP huMAP3_07940.1) (hu.MAP huMAP3_05473.1) (hu.MAP huMAP3_09165.1). Additional hu.MAP links involving XPO1, ATP2A2, UBA6, ADSL, and YARS1 (hu.MAP huMAP3_14442.1) (hu.MAP huMAP3_07170.1) (hu.MAP huMAP3_10473.1) (hu.MAP huMAP3_09592.1) suggest connections to export, membrane or calcium-associated machinery, and protein modification. Thus, STRING and hu.MAP provide substantial prior support for the module’s internal architecture, while the cross-tissue co-abundance pattern indicates coordinated activity of these established systems in bone marrow and liver.

**STRING interactions (score >= 0.7)**: 37 of 528 gene pairs: ABCF1–DHX9 (0.921); ADSL–FKBP4 (0.849); ADSL–GART (0.999); ATP1A1–ATP2A2 (0.82); DHX9–SF3B3 (0.73); DHX9–SNRNP200 (0.784); DHX9–XPO1 (0.791); EFTUD2–KARS1 (0.704); EFTUD2–RPL3 (0.837); EFTUD2–SF3A1 (0.999); EFTUD2–SF3B3 (0.999); EFTUD2–SNRNP200 (0.999); EFTUD2–SNRPA1 (0.999); EIF3C–EIF3L (0.999); EIF3C–EIF4G1 (0.99); EIF3L–EIF4G1 (0.924); GART–RPL3 (0.805); IARS1–KARS1 (0.999); IARS1–MARS1 (0.999); IARS1–VARS1 (0.9); IARS1–YARS1 (0.966); KARS1–MARS1 (0.999); KARS1–RPL3 (0.705); KARS1–VARS1 (0.978); KARS1–YARS1 (0.988); MARS1–VARS1 (0.902); MARS1–YARS1 (0.999); RPL3–RSL1D1 (0.846); RPL3–SRP68 (0.959); SF3A1–SF3B3 (0.999); SF3A1–SNRNP200 (0.999); SF3A1–SNRPA1 (0.999); SF3B3–SNRNP200 (0.999); SF3B3–SNRPA1 (0.999); SNRNP200–SNRPA1 (0.999); SPTAN1–SPTBN1 (0.999); VARS1–YARS1 (0.956)
**STRING functional enrichment (supplementary, within-query FDR)**: Function RNA binding (FDR = 5.28e-07, 23 genes); Component Ribonucleoprotein complex (FDR = 3.91e-06, 14 genes); Component Protein-containing complex (FDR = 5.58e-06, 29 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 8.52e-06, 13 genes); Function Heterocyclic compound binding (FDR = 6.09e-05, 29 genes); COMPARTMENTS Protein-containing complex (FDR = 6.38e-05, 29 genes); Function Organic cyclic compound binding (FDR = 6.7e-05, 29 genes); TISSUES Male reproductive gland (FDR = 0.00087, 22 genes); TISSUES Male reproductive system (FDR = 0.00087, 23 genes); TISSUES Female reproductive gland (FDR = 0.00087, 23 genes); TISSUES Lymphocyte (FDR = 0.00087, 13 genes); Process Gene expression (FDR = 0.0014, 18 genes); TISSUES Brain (FDR = 0.0026, 29 genes); Process Ribonucleoprotein complex biogenesis (FDR = 0.0027, 9 genes); RCTM Translation (FDR = 0.0036, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (SNRNP200, SNRPA1, EFTUD2, SF3B3, SF3A1; 5/97); huMAP3_02637.1 (IARS1, MARS1, KARS1; 3/14); huMAP3_13688.1 (IARS1, MARS1, KARS1; 3/14); huMAP3_13175.1 (EIF4G1, EIF3C, EIF3L; 3/20); huMAP3_11246.1 (EIF4G1, EIF3C, EIF3L; 3/24); huMAP3_14442.1 (UBA6, ADSL, YARS1; 3/57); huMAP3_06511.1 (SNRPA1, SF3B3, SF3A1; 3/79); huMAP3_07940.1 (SPTBN1, SPTAN1; 2/5); huMAP3_05473.1 (SPTBN1, SPTAN1; 2/7); huMAP3_00960.1 (SNRNP200, EFTUD2; 2/8); huMAP3_07622.1 (SNRNP200, EFTUD2; 2/9); huMAP3_07170.1 (XPO1, ATP2A2; 2/14); huMAP3_01276.1 (EIF3C, EIF3L; 2/17); huMAP3_10473.1 (ATP1A1, ATP2A2; 2/24); huMAP3_09165.1 (SPTBN1, SPTAN1; 2/39); huMAP3_08501.1 (SNRNP200, EFTUD2; 2/47); huMAP3_09504.1 (SNRNP200, EFTUD2; 2/51); huMAP3_04549.1 (SF3B3, SF3A1; 2/52); huMAP3_09945.1 (SNRNP200, EFTUD2; 2/61); huMAP3_09592.1 (XPO1, ATP2A2; 2/95)

### Novelty

The module should not be described as a newly discovered molecular complex. Much of its structure recapitulates well-established spliceosomal, translation-initiation, aminoacyl-tRNA synthetase, spectrin, and transporter relationships documented by STRING and hu.MAP. A potentially novel aspect is the conserved co-abundance of these connected processes across bone marrow and liver, especially the way the RNA-processing, translation, chaperone, trafficking, and cytoskeletal components are coordinated in the same tissue-pair module. However, this is a systems-level observation rather than proof of a new physical complex or new gene function. Absence of a relationship from STRING or hu.MAP would not establish novelty, and the available evidence does not demonstrate that the module represents a previously unknown mechanism. Its most defensible novelty claim is therefore the tissue-pair-specific co-abundance organization and reproducibility, which require validation in independent cohorts and experiments.

**Hypothesis.** Hypothesis: this conserved module represents a coordinated cellular capacity for processing, exporting, translating, folding, and trafficking RNA-derived protein products. In this model, spliceosomal components and DHX9 support precursor-RNA processing; XPO1 and ribonucleoprotein machinery support nuclear–cytoplasmic RNA exchange; EIF3C, EIF3L, EIF4G1, RPL3, and the aminoacyl-tRNA synthetases support translation; HSPH1 buffers proteotoxic stress; and COPB1, DCTN1, clathrin, spectrins, and membrane pumps support intracellular transport and cell-architecture demands. The shared signal in bone marrow and liver may reflect common requirements for high-throughput gene expression, cell maintenance, differentiation, or protein turnover rather than a secreted or immune-cell-specific program. This remains a hypothesis because co-abundance does not establish physical interaction, directionality, or causal regulation.

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): SUPT16H (0.90), EFTUD2 (0.89), ABCF1 (0.88), SF3A1 (0.88), SF3B3 (0.86), EIF3L (0.85), SNRNP200 (0.85), COPB1 (0.85), ATP1A1 (0.84), MARS1 (0.84), IARS1 (0.83), VARS1 (0.83), XPO1 (0.83), ATP2A2 (0.82), SRP68 (0.82), GART (0.82), RSL1D1 (0.81), YARS1 (0.81), FKBP4 (0.80), KARS1 (0.80), EIF3C (0.80); STRING partners: ABCF1 (0.921), SF3B3 (0.73), SNRNP200 (0.784), XPO1 (0.791)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is the most central network connector among the highlighted genes and links SUPT16H, EFTUD2, ABCF1, SF3A1, SF3B3, EIF3L, SNRNP200, and COPB1. It is an ATP-dependent RNA and DNA–RNA helicase with nuclear and cytoplasmic localization, and it is represented across the RNA-binding, ribonucleoprotein, RNA-complex, translation, and macromolecule-biosynthesis terms (12 globally significant GO/KEGG terms, q_global 3.14e-07–0.0418; see the table). Its extensive literature and disease associations make it a strong biological anchor rather than a generic peripheral housekeeping marker.
- **Conclusion**: Established evidence supports DHX9 as a central RNA-processing and RNA-remodeling component of the module. Its network position makes it a plausible integrator between splicing, RNA export, translation, and transcriptional regulation. It is a candidate module coordinator, but the co-abundance data do not establish that DHX9 controls the other genes.

#### SF3B3

- **Related proteins** (co-abundance neighbors): DHX9 (0.86), YARS1 (0.84), IARS1 (0.84), GART (0.83), HSPH1 (0.82), SRP68 (0.82), EIF4G1 (0.81); STRING partners: DHX9 (0.73), EFTUD2 (0.999), SF3A1 (0.999), SNRNP200 (0.999), SNRPA1 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Nucleoli rim; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_06511.1, huMAP3_04549.1
- **Function (MyGene.info)**: splicing factor 3b subunit 3. This gene encodes subunit 3 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); dengue disease (0.370); cervical cancer (0.189); cervical carcinoma (0.189); prostate cancer (0.111)
- **Europe PMC papers**: 965
- **Why important**: SF3B3 is a core spliceosomal component and participates in the strongest spliceosome-related primary annotations (11 globally significant GO/KEGG terms, q_global 0.00137–0.0448; see the table). It has dense STRING support with EFTUD2, SF3A1, SNRNP200, and SNRPA1, and it occurs in multiple hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_04549.1). It also connects in the co-abundance graph to DHX9, IARS1, YARS1, GART, HSPH1, and SRP68, placing it at the interface between splicing and broader gene expression.
- **Conclusion**: Established evidence identifies SF3B3 as a bona fide spliceosomal hub within the module. Its co-abundance with translation and RNA-handling genes supports coordinated gene-expression machinery. A tissue-pair-specific role in coupling splicing to translation is a hypothesis, not an established function of this module.

#### MARS1

- **Related proteins** (co-abundance neighbors): HSPH1 (0.89), ABCF1 (0.88), SUPT16H (0.86), EIF3C (0.86), DHX9 (0.84), YARS1 (0.84), VARS1 (0.83), COPB1 (0.82), ATP1A1 (0.82), GART (0.81), EIF3L (0.81), EZR (0.81), IARS1 (0.80); STRING partners: IARS1 (0.999), KARS1 (0.999), VARS1 (0.902), YARS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: methionyl-tRNA synthetase 1. This gene encodes a member of the class I family of aminoacyl-tRNA synthetases. These enzymes play a critical role in protein biosynthesis by charging tRNAs with their cognate amino acids. The encoded protein is a component of the multi-tRNA synthetase complex and catalyzes the ligation of methionine to tRNA molecules. [provided by RefSeq, Jan 2011].
- **Diseases (Open Targets)**: severe early-onset pulmonary alveolar proteinosis due to MARS deficiency (0.745); Charcot-Marie-Tooth disease axonal type 2U (0.676); autosomal recessive spastic paraplegia type 70 (0.614); trichothiodystrophy 9, nonphotosensitive (0.428); pulmonary alveolar proteinosis (0.338)
- **Europe PMC papers**: 435
- **Why important**: MARS1 has a relatively central position and connects the RNA and translation portions of the graph, including HSPH1, ABCF1, SUPT16H, EIF3C, DHX9, YARS1, VARS1, and COPB1. It is an aminoacyl-tRNA synthetase required for methionine charging and is part of the multi-tRNA synthetase complex. It contributes to the translation and protein-biosynthesis evidence (9 globally significant GO/KEGG terms, q_global 3.14e-07–0.0418; see the table), has strong STRING relationships with other synthetases, and is supported by hu.MAP aminoacyl-tRNA synthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). Its disease associations include MARS deficiency and neurological or developmental disorders.
- **Conclusion**: Established evidence supports MARS1 as a translation-fidelity and protein-biosynthesis component that helps define the module’s translational arm. Its connection to splicing and stress-related genes is consistent with integrated gene-expression demands, but a direct regulatory bridge between these processes remains a hypothesis.

#### EIF3L

- **Related proteins** (co-abundance neighbors): DHX9 (0.85), YARS1 (0.83), ATP2A2 (0.83), SUPT16H (0.83), COPB1 (0.83), VARS1 (0.82), MARS1 (0.81), CLTC (0.81), IARS1 (0.81), HSPH1 (0.80); STRING partners: EIF3C (0.999), EIF4G1 (0.924)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: huMAP3_13175.1, huMAP3_11246.1, huMAP3_01276.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit L. Enables RNA binding activity. Contributes to translation initiation factor activity. Involved in translational initiation and viral translational termination-reinitiation. Located in membrane. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.503); Hydrocephalus (0.064); open-angle glaucoma (0.042); severe acute respiratory syndrome (0.032); COVID-19 (0.032)
- **Europe PMC papers**: 558
- **Why important**: EIF3L is a central translation-initiation component with connections to DHX9, YARS1, ATP2A2, SUPT16H, COPB1, VARS1, MARS1, and CLTC. It is represented broadly across the primary RNA-binding, ribonucleoprotein, protein–RNA organization, translation, and macromolecule-biosynthesis terms (11 globally significant GO/KEGG terms, q_global 3.14e-07–0.0418; see the table). STRING supports its relationships with EIF3C and EIF4G1, while hu.MAP identifies translation-initiation complexes (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1) (hu.MAP huMAP3_01276.1). It has a substantial literature base and disease associations involving neurodevelopmental and neurological conditions.
- **Conclusion**: Established evidence supports EIF3L as a key translation-initiation scaffold and a bridge between the translational machinery and the wider module. Its co-abundance with spliceosomal genes indicates coordinated gene-expression capacity, but does not prove direct coupling in bone marrow or liver.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): SF3A1 (0.95), DHX9 (0.89), HSPH1 (0.82), ABCF1 (0.81), SRP68 (0.81), GART (0.81); STRING partners: KARS1 (0.704), RPL3 (0.837), SF3A1 (0.999), SF3B3 (0.999), SNRNP200 (0.999), SNRPA1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 is a spliceosomal GTPase and a component of spliceosomal tri-snRNP machinery. It is present in the core spliceosome primary terms (11 globally significant GO/KEGG terms, q_global 0.00137–0.0448; see the table), has strong STRING links to SF3A1, SF3B3, SNRNP200, and SNRPA1, and appears across numerous hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_00960.1) (hu.MAP huMAP3_07622.1) (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1). It also connects to translation-associated and stress-associated genes in the co-abundance network and has a well-established disease association with mandibulofacial dysostosis–microcephaly syndrome.
- **Conclusion**: Established evidence supports EFTUD2 as a structurally and functionally important spliceosome component, confirming that the module contains genuine pre-mRNA-processing machinery. Its network links to translation and cellular stress may indicate coordinated output of gene expression, but this cross-process mechanism remains hypothetical.

## Module 3

**Tissue pair**: bone_marrow and liver  
**Genes (29)**: ABHD10, ATP5PB, COPS3, DYNC1H1, FASN, FLII, GNG12, IPO4, IQGAP1, ITGAV, NCKAP1, NDUFS1, NSF, P4HA1, PDCD6IP, ATIC, RO60, RTN4, SEC63, STAT1, AARS1, IARS2, LARS1, QARS1, SARS1, TNPO1, USP5, USO1, WDR1

### Function

No GO or KEGG term passed global correction, so the function cannot be assigned from statistically significant pathway enrichment. The network instead suggests a composite cellular-maintenance program organized around NCKAP1. Its components include cytoskeletal remodeling and cell adhesion through NCKAP1, ITGAV, FLII, WDR1 and IQGAP1; protein synthesis through the aminoacyl-tRNA synthetases AARS1, IARS2, LARS1, QARS1 and SARS1; mitochondrial energy metabolism through NDUFS1 and ATP5PB; and intracellular trafficking, vesicle handling and nuclear transport through DYNC1H1, USO1, NSF, PDCD6IP, IPO4 and TNPO1. These are coherent cellular functions, but their coexistence should be interpreted as a network-level pattern rather than as a globally validated single pathway. The absence of globally enriched GO or KEGG terms does not invalidate the module.

**Cell composition.** The module is predominantly intracellular rather than plasma or secreted: HPA identifies only a small secreted subset, while most proteins are cytosolic, mitochondrial, nuclear, endoplasmic-reticulum, Golgi or vesicular proteins. HPA indicates broad expression for most genes, with many having low tissue specificity and low immune-cell specificity. Protein detection is broadly similar in bone marrow and liver for most genes. The module is therefore not strongly suggestive of a blood-cell program or a plasma-protein signal. The tissue-enhanced genes point in several directions, including skeletal muscle, brain, adipose tissue, breast and liver, and the single-cell annotations are heterogeneous. The shared signal may consequently reflect broadly expressed cellular machinery, shared cell states, or technical and compositional variation rather than a lineage-specific bone-marrow or liver function.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a well-known aminoacyl-tRNA synthetase subnetwork: AARS1, IARS2, LARS1, QARS1 and SARS1 are mutually connected in the supplied high-confidence interactions. STRING also supports the IPO4–TNPO1 nuclear-transport relationship and the NSF–USO1 vesicle-transport relationship. NDUFS1–ATP5PB provides a mitochondrial respiratory connection. These relationships show that several local edges are biologically plausible and already known, but STRING does not provide a unified interaction explanation for the entire module; many module genes have no supplied high-confidence STRING partner. hu.MAP provides partial complex support: NDUFS1 and ABHD10 occur together in (hu.MAP huMAP3_12412.1); QARS1 and LARS1 occur together in (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1); WDR1 and GNG12 occur together in (hu.MAP huMAP3_09165.1); ATIC and AARS1 occur together in (hu.MAP huMAP3_14442.1); and ATP5PB and TNPO1 occur together in (hu.MAP huMAP3_06247.1). Because each hu.MAP overlap contains only a minority of the corresponding complex, these data support local memberships rather than a single established complex encompassing the module.

**STRING interactions (score >= 0.7)**: 13 of 406 gene pairs: AARS1–IARS2 (0.942); AARS1–LARS1 (0.968); AARS1–QARS1 (0.964); AARS1–SARS1 (0.881); ATP5PB–NDUFS1 (0.886); IARS2–LARS1 (0.996); IARS2–QARS1 (0.992); IARS2–SARS1 (0.904); IPO4–TNPO1 (0.74); LARS1–QARS1 (0.999); LARS1–SARS1 (0.933); NSF–USO1 (0.832); QARS1–SARS1 (0.852)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12412.1 (NDUFS1, ABHD10; 2/5); huMAP3_02637.1 (QARS1, LARS1; 2/14); huMAP3_13688.1 (QARS1, LARS1; 2/14); huMAP3_09165.1 (WDR1, GNG12; 2/39); huMAP3_14442.1 (ATIC, AARS1; 2/57); huMAP3_06247.1 (ATP5PB, TNPO1; 2/65)

### Novelty

The module should not be called a newly discovered molecular complex or pathway. Several of its relationships are established by STRING and hu.MAP, especially the aminoacyl-tRNA synthetase cluster and selected trafficking and mitochondrial links. At the same time, the fact sheet does not identify a previously described co-abundance module shared specifically by bone marrow and liver, so the cross-tissue co-abundance observation may be a potentially useful new systems-level finding. That claim remains provisional: the module has no globally significant GO or KEGG enrichment, its genes span several cellular systems, and the HPA profile is broadly expressed and heterogeneous. Absence of a complete match in STRING or hu.MAP would not by itself prove novelty.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of a broadly expressed cellular-support state in which protein synthesis, mitochondrial energy supply, cytoskeletal organization, adhesion, vesicle traffic and intracellular transport are jointly maintained. NCKAP1 may act as the network bridge linking these otherwise distinct subsystems. In both bone marrow and liver, the signal could arise from cells requiring substantial biosynthetic and trafficking capacity, or from shared variation in cellular composition, rather than from a dedicated tissue-specific pathway. This hypothesis should be tested with cell-composition adjustment, independent cohorts, perturbation experiments, and assessment of whether the module tracks translation, mitochondrial respiration, adhesion or trafficking phenotypes.

### Important genes

#### NCKAP1

- **Related proteins** (co-abundance neighbors): IARS2 (0.90), ABHD10 (0.88), P4HA1 (0.88), AARS1 (0.87), NDUFS1 (0.86), DYNC1H1 (0.85), FLII (0.85), FASN (0.85), SEC63 (0.84), WDR1 (0.84), COPS3 (0.84), IQGAP1 (0.83), RO60 (0.82), SARS1 (0.82), ATIC (0.82), LARS1 (0.82), STAT1 (0.82), QARS1 (0.82), USP5 (0.81), ATP5PB (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NCK associated protein 1. Contributes to small GTPase binding activity. Involved in Rac protein signal transduction; positive regulation of Arp2/3 complex-mediated actin nucleation; and positive regulation of lamellipodium assembly. Located in extracellular exosome and focal adhesion. Part of SCAR complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.528); neurodevelopmental disorder (0.471); hereditary disease (0.451); complex neurodevelopmental disorder (0.443); Intellectual disability (0.437)
- **Europe PMC papers**: 1019
- **Why important**: NCKAP1 is the central network hub in the supplied subgraph, connecting genes from translation, mitochondrial function, cytoskeletal remodeling, adhesion, trafficking and lipid metabolism. Its established functions include Rac signaling, Arp2/3-dependent actin nucleation and lamellipodium assembly, and it is a component of the SCAR complex. HPA describes broad tissue and cell-type expression, consistent with a general cellular organizer rather than a secreted or immune-specific marker. Its disease associations include neurodegenerative and neurodevelopmental disorders, and the literature is extensive.
- **Conclusion**: Established evidence supports NCKAP1 as the principal network integrator and as a regulator of actin remodeling and cell morphology. It is a strong candidate for explaining why otherwise diverse cellular processes co-vary. It is not established that NCKAP1 causally drives this bone-marrow–liver module; that causal role is a hypothesis.

#### AARS1

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.88), NCKAP1 (0.87), USO1 (0.85), GNG12 (0.82), ITGAV (0.81), PDCD6IP (0.81); STRING partners: IARS2 (0.942), LARS1 (0.968), QARS1 (0.964), SARS1 (0.881)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: alanyl-tRNA synthetase 1. The human alanyl-tRNA synthetase (AARS) belongs to a family of tRNA synthases, of the class II enzymes.  Class II tRNA synthases evolved early in evolution and are highly conserved. This is reflected by the fact that 498 of the 968-residue polypeptide human AARS shares 41% identity witht the E.coli protein.  tRNA synthases are the enzymes that interpret the RNA code and attach specific aminoacids …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2N (0.762); developmental and epileptic encephalopathy, 29 (0.747); undetermined early-onset epileptic encephalopathy (0.678); trichothiodystrophy 8, nonphotosensitive (0.568); Charcot-Marie-Tooth disease type 2 (0.566)
- **Europe PMC papers**: 672
- **Why important**: AARS1 is connected to the network hub and to the dense aminoacyl-tRNA synthetase subnetwork comprising IARS2, LARS1, QARS1 and SARS1. It catalyzes alanine attachment to transfer RNA and therefore represents a direct link to translational capacity. It is detected in both bone marrow and liver, has low tissue and cell-type specificity, and has established associations with several inherited neurological disorders. Its literature is substantial, and it also participates in hu.MAP complex (hu.MAP huMAP3_14442.1).
- **Conclusion**: Established evidence supports AARS1 as a marker of protein-synthesis machinery and as a locally well-supported interaction node. Its co-abundance with the other synthetases is compatible with coordinated translational demand. The data do not establish that altered AARS1 activity causes the whole module or that translation is the sole module function.

#### DYNC1H1

- **Related proteins** (co-abundance neighbors): AARS1 (0.88), NCKAP1 (0.85), ITGAV (0.84), TNPO1 (0.84), USO1 (0.83), NSF (0.82), LARS1 (0.82), PDCD6IP (0.81), IPO4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 1 heavy chain 1. Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polyp…
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy without contractures (0.816); intellectual disability, autosomal dominant 13 (0.815); Charcot-Marie-Tooth disease axonal type 2O (0.799); autosomal dominant non-syndromic intellectual disability (0.634); hereditary disease (0.545)
- **Europe PMC papers**: 1731
- **Why important**: DYNC1H1 is one of the stronger connecting nodes after NCKAP1 and links NCKAP1 to ITGAV, TNPO1, USO1, NSF and PDCD6IP. Cytoplasmic dynein is an established microtubule-based motor involved in intracellular transport, organelle movement, spindle dynamics and retrograde transport. HPA reports brain tissue enhancement and detection in bone marrow, while disease associations include motor-neuron, neuropathy and intellectual-disability phenotypes. The literature is extensive.
- **Conclusion**: Established evidence supports DYNC1H1 as a plausible transport and cytoskeletal bridge within the module. Its network placement makes it important for connecting adhesion, vesicle handling and nuclear transport signals. A direct role in coordinating the shared bone-marrow–liver abundance pattern remains unproven.

#### ITGAV

- **Related proteins** (co-abundance neighbors): FASN (0.86), DYNC1H1 (0.84), TNPO1 (0.83), AARS1 (0.81), RTN4 (0.81), FLII (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha V. The product of this gene belongs to the integrin alpha chain family. Integrins are heterodimeric integral membrane proteins composed of an alpha subunit and a beta subunit that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha V subunit. This subunit associates with beta 1, beta 3, beta…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); myocardial infarction (0.396); angina pectoris (0.371); Recurrent thrombophlebitis (0.370); intermediate coronary syndrome (0.370)
- **Europe PMC papers**: 5475
- **Why important**: ITGAV connects the module hub to FASN, DYNC1H1, TNPO1, AARS1, RTN4 and FLII. As an integrin alpha subunit, it participates in heterodimeric cell-surface adhesion receptors and is annotated for cell adhesion, cell-matrix adhesion, angiogenesis and calcium-related signaling. HPA detects it in both tissues and places it at focal adhesion sites and in the cytosol. It has a large literature and disease associations involving vascular and cardiovascular phenotypes.
- **Conclusion**: Established evidence supports ITGAV as the module's most direct cell-adhesion and extracellular-matrix interface. Its presence is compatible with coordinated regulation of adhesion, migration and cytoskeletal organization. The module does not demonstrate a specific ITGAV ligand, integrin heterodimer or adhesion phenotype, so any mechanistic interpretation beyond that remains hypothetical.

#### NDUFS1

- **Related proteins** (co-abundance neighbors): NCKAP1 (0.86); STRING partners: ATP5PB (0.886)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_12412.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S1. The protein encoded by this gene belongs to the complex I 75 kDa subunit family. Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Thi…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 5 (0.810); mitochondrial complex I deficiency (0.647); type 2 diabetes mellitus (0.608); Parkinson disease (0.603); diabetes mellitus (0.580)
- **Europe PMC papers**: 2567
- **Why important**: NDUFS1 is a core subunit of mitochondrial respiratory-chain complex I and is directly connected in STRING to ATP5PB. It supports electron transfer, respiratory-chain assembly and proton-motive-force-linked ATP production. HPA shows enhancement in muscle-related tissues and detection in liver, with low immune-cell specificity. Its disease associations include mitochondrial complex I deficiency and Parkinson disease, and the literature is substantial. It also participates in hu.MAP complex (hu.MAP huMAP3_12412.1).
- **Conclusion**: Established evidence supports NDUFS1 as the mitochondrial energy component of the module and provides a biologically interpretable link to ATP5PB. Its co-abundance may indicate shared energetic demand. The data do not establish that respiratory-chain activity is globally enriched in the module or that mitochondrial dysfunction drives the cross-tissue association.

#### FASN

- **Related proteins** (co-abundance neighbors): ITGAV (0.86), NCKAP1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fatty acid synthase. The enzyme encoded by this gene is a multifunctional protein. Its main function is to catalyze the synthesis of palmitate from acetyl-CoA and malonyl-CoA, in the presence of NADPH, into long-chain saturated fatty acids. In some cancer cell lines, this protein has been found to be fused with estrogen receptor-alpha (ER-alpha), in which the N-terminus of FAS is fused in-frame with the C-terminus of …
- **Diseases (Open Targets)**: dengue disease (0.469); autism spectrum disorder (0.333); Parkinson disease (0.295); Epileptic encephalopathy (0.211); neurodegenerative disease (0.205)
- **Europe PMC papers**: 21528
- **Why important**: FASN is connected to NCKAP1 and ITGAV and is the module's clearest lipid-biosynthetic enzyme. It catalyzes palmitate synthesis and is annotated for fatty-acid and lipid biosynthesis, nutrient response and osteoblast differentiation. HPA reports tissue enhancement in adipose tissue, breast and liver, while it is not detected in immune cells and is not detected by IHC in the supplied bone-marrow and liver observations. FASN has a very large literature and disease associations including cancer, diabetes-related and neurodegenerative contexts.
- **Conclusion**: Established evidence supports FASN as a tissue-metabolic component that may connect lipid synthesis with adhesion and cytoskeletal state. Its HPA pattern argues against interpreting the module as a simple blood-cell signature. Whether FASN reflects liver-related metabolic contribution, cell-composition variation or a functional metabolic arm of the shared module cannot be resolved from the supplied data.

## Module 4

**Tissue pair**: bone_marrow and liver  
**Genes (28)**: ACLY, CPNE1, CACYBP, DDX5, DDX6, FARP1, FSCN1, HNRNPL, HNRNPR, HSP90AA1, IMPDH2, LMNB1, LMNB2, MATR3, MVD, NUCB2, NUDT12, OLA1, PCNA, PPM1A, PRPS2, PAICS, RAN, RUVBL2, SHFL, NARS2, CCT5, CCT3

### Function

The module represents a broadly expressed intracellular program linking RNA metabolism, nucleic-acid binding, genome maintenance, protein folding and nucleotide metabolism. Primary GO evidence supports nucleic-acid binding (GO:MF nucleic acid binding; q_global = 0.014), mRNA binding (GO:MF mRNA binding; q_global = 0.0262), regulation of DNA biosynthesis (GO:BP positive regulation of DNA biosynthetic process; q_global = 0.00547) (GO:BP regulation of DNA biosynthetic process; q_global = 0.0182), and telomere maintenance, telomere organization and chromosome organization (5 globally significant GO/KEGG terms, q_global 0.0286–0.042; see the table). DDX5, DDX6, HNRNPL, HNRNPR and MATR3 support RNA processing and RNA turnover. PCNA, RUVBL2, RAN and the CCT proteins connect the module to DNA replication, repair, chromosome organization and telomere biology. IMPDH2, PAICS and PRPS2 provide a nucleotide-metabolism context. The negative-regulation terms (GO:BP negative regulation of macromolecule biosynthetic process; q_global = 0.0221) (GO:BP negative regulation of biosynthetic process; q_global = 0.0415) are broad and should not be treated as evidence for one specific inhibitory pathway. STRING annotations support nuclear, ATP-dependent and ubiquitin-associated functions (10 supplementary STRING terms; within-query FDR 0.00072–0.0391), but these are supplementary rather than globally corrected evidence.

**Cell composition.** The module is not dominated by plasma or secreted proteins. NUCB2 is the only gene identified as secreted to blood, while the remaining genes are intracellular. HPA indicates low immune-cell specificity for nearly all genes, with FSCN1 as an immune-cell-enhanced gene and a myeloid dendritic-cell association in the summarized evidence. Most genes have low tissue specificity, although some are enhanced in bone marrow, liver, testis or other tissues. Protein detection is common in both bone marrow and liver. The shared signal therefore appears more consistent with a conserved intracellular program than with plasma contamination. Bone-marrow composition may nevertheless contribute, because LMNB1 and PCNA are bone-marrow enhanced and several genes are associated with progenitor or proliferative cell types. The diverse HPA single-cell associations indicate that this is not specific to one immune lineage.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP positive regulation of DNA biosynthetic process | 0.00547 | CCT3, CCT5, HSP90AA1, PCNA |
| GO:MF nucleic acid binding | 0.014 | CCT3, CCT5, DDX5, DDX6, FSCN1, HNRNPL, HNRNPR, HSP90AA1, IMPDH2, LMNB1, MATR3, NARS2, NUCB2, PCNA, RAN, RUVBL2, SHFL |
| GO:BP regulation of DNA biosynthetic process | 0.0182 | CCT3, CCT5, HSP90AA1, PCNA |
| GO:BP negative regulation of macromolecule biosynthetic process | 0.0221 | CPNE1, DDX5, DDX6, HNRNPL, LMNB1, LMNB2, NUDT12, PCNA, PPM1A, RAN, RUVBL2, SHFL |
| GO:MF mRNA binding | 0.0262 | CCT5, DDX5, DDX6, HNRNPL, HNRNPR, HSP90AA1, SHFL |
| GO:BP positive regulation of telomere maintenance | 0.0286 | CCT3, CCT5, HSP90AA1, RUVBL2 |
| GO:BP telomere maintenance | 0.0296 | CCT3, CCT5, HSP90AA1, PCNA, RUVBL2 |
| GO:BP telomere organization | 0.0372 | CCT3, CCT5, HSP90AA1, PCNA, RUVBL2 |
| GO:BP negative regulation of biosynthetic process | 0.0415 | CPNE1, DDX5, DDX6, HNRNPL, LMNB1, LMNB2, NUDT12, PCNA, PPM1A, RAN, RUVBL2, SHFL |
| GO:BP regulation of telomere maintenance | 0.042 | CCT3, CCT5, HSP90AA1, RUVBL2 |
| GO:BP positive regulation of chromosome organization | 0.042 | CCT3, CCT5, HSP90AA1, RUVBL2 |

### STRING and hu.MAP

STRING supports established relationships within several parts of the module: CCT3-CCT5, CCT5-HSP90AA1, CCT5-RUVBL2, HSP90AA1-RUVBL2, DDX5-HNRNPR, DDX5-MATR3, HNRNPL-HNRNPR, HNRNPL-MATR3, LMNB1-LMNB2 and IMPDH2-PAICS. These findings show that part of the co-abundance structure recapitulates known protein associations and shared functions. hu.MAP supports complexes containing HNRNPR, HNRNPL and MATR3 (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1), LMNB1 and LMNB2 (hu.MAP huMAP3_03501.1) (hu.MAP huMAP3_00325.1) (hu.MAP huMAP3_13519.1) (hu.MAP huMAP3_10433.1) (hu.MAP huMAP3_09259.1) (hu.MAP huMAP3_10492.1) (hu.MAP huMAP3_10614.1), and CCT3 with CCT5 (hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). Most hu.MAP complexes contain many proteins outside the module, so the module is not itself established as one physical complex. Missing STRING or hu.MAP relationships do not prove that individual co-abundance edges are novel.

**STRING interactions (score >= 0.7)**: 15 of 378 gene pairs: CACYBP–HSP90AA1 (0.863); CCT3–CCT5 (0.999); CCT3–HSP90AA1 (0.767); CCT3–RUVBL2 (0.766); CCT5–HSP90AA1 (0.868); CCT5–RAN (0.825); CCT5–RUVBL2 (0.705); DDX5–HNRNPR (0.844); DDX5–MATR3 (0.894); HNRNPL–HNRNPR (0.961); HNRNPL–MATR3 (0.757); HNRNPR–MATR3 (0.714); HSP90AA1–RUVBL2 (0.886); IMPDH2–PAICS (0.744); LMNB1–LMNB2 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Ubl conjugation (FDR = 0.00072, 15 genes); Keyword Isopeptide bond (FDR = 0.0016, 13 genes); Keyword Nucleus (FDR = 0.007, 17 genes); TISSUES Lymphoblast (FDR = 0.014, 8 genes); TISSUES Leukemia cell (FDR = 0.014, 13 genes); Function Nucleic acid binding (FDR = 0.0166, 17 genes); Function mRNA binding (FDR = 0.0166, 7 genes); Function ATP hydrolysis activity (FDR = 0.0168, 7 genes); Keyword ATP-binding (FDR = 0.0178, 12 genes); TISSUES Leukocyte (FDR = 0.0218, 11 genes); TISSUES Lymphocyte (FDR = 0.0218, 10 genes); Function ATP binding (FDR = 0.0391, 12 genes); Function Pyrophosphatase activity (FDR = 0.0391, 9 genes); Function Organic cyclic compound binding (FDR = 0.0391, 22 genes); Function Heterocyclic compound binding (FDR = 0.0391, 22 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07581.1 (HNRNPR, HNRNPL, MATR3; 3/21); huMAP3_10625.1 (HNRNPR, HNRNPL, MATR3; 3/57); huMAP3_03501.1 (LMNB1, LMNB2; 2/2); huMAP3_00325.1 (LMNB1, LMNB2; 2/3); huMAP3_13519.1 (LMNB1, LMNB2; 2/4); huMAP3_10433.1 (LMNB1, LMNB2; 2/5); huMAP3_05721.1 (HNRNPL, MATR3; 2/6); huMAP3_07225.1 (HNRNPR, HNRNPL; 2/7); huMAP3_09259.1 (LMNB1, LMNB2; 2/8); huMAP3_01951.1 (CCT5, CCT3; 2/8); huMAP3_10492.1 (LMNB1, LMNB2; 2/9); huMAP3_10614.1 (LMNB1, LMNB2; 2/9); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09654.1 (HNRNPR, HNRNPL; 2/13); huMAP3_07938.1 (CCT5, CCT3; 2/23); huMAP3_06559.1 (CCT5, CCT3; 2/25); huMAP3_10659.1 (HNRNPR, HNRNPL; 2/28); huMAP3_09191.1 (CCT5, CCT3; 2/32); huMAP3_10656.1 (CCT5, CCT3; 2/36); huMAP3_14584.1 (CCT5, CCT3; 2/61)

### Novelty

The biological functions represented by the module are not new: its genes participate in established CCT chaperoning, hnRNP-mediated RNA processing, nuclear-lamina biology, nucleotide metabolism, DNA replication, DNA repair and telomere maintenance. Several central relationships are already supported by STRING and hu.MAP. However, the particular conserved co-abundance pattern shared by bone marrow and liver may be a new systems-level observation because it combines several known functional neighborhoods without corresponding to one canonical complex. The fact sheet does not identify an exact previously published module, so complete novelty cannot be claimed. The most defensible conclusion is that the component biology is established, while the tissue-pair-specific organization is potentially novel and should be tested against published coexpression modules, independent cohorts and analyses adjusted for cell composition.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular-maintenance or regenerative state in which RNA processing and turnover are coordinated with protein folding, nucleotide production, DNA replication or repair, and telomere or chromosome maintenance. PCNA and the CCT3, CCT5, HSP90AA1 and RUVBL2 group could mark genome-maintenance activity, while DDX5, DDX6, HNRNPL, HNRNPR and MATR3 could regulate RNA processing and transcript fate. IMPDH2, PAICS and PRPS2 could support nucleotide availability, while LMNB1 and LMNB2 could connect nuclear architecture to these processes. In bone marrow, the signal may partly reflect progenitor or proliferative cells; in liver, it may reflect hepatocyte or other intracellular maintenance programs. This is a mechanistic hypothesis, not proof of direct cooperation or a disease-specific pathway. It should be tested using cell-type-resolved expression, adjustment for proliferation and cell composition, protein measurements and perturbation experiments.

### Important genes

#### CCT5

- **Related proteins** (co-abundance neighbors): IMPDH2 (0.89), HNRNPR (0.87), RUVBL2 (0.86), MATR3 (0.85), DDX5 (0.84), OLA1 (0.84), NUDT12 (0.83), HNRNPL (0.83), ACLY (0.83), HSP90AA1 (0.82), FSCN1 (0.81), CCT3 (0.81), LMNB2 (0.80); STRING partners: CCT3 (0.999), HSP90AA1 (0.868), RAN (0.825), RUVBL2 (0.705)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_01951.1, huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is the strongest network hub in the supplied subgraph and connects the chaperonin, RNA-binding, nucleotide-handling and genome-maintenance neighborhoods. It is represented in primary nucleic-acid-binding, mRNA-binding, DNA-biosynthesis and telomere-related terms (10 globally significant GO/KEGG terms, q_global 0.00547–0.042; see the table). Its links to CCT3, HSP90AA1, RAN and RUVBL2 are supported by STRING, and its CCT3 partnership appears in several hu.MAP complexes (hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). It has a substantial literature base and a documented hereditary neuropathy association.
- **Conclusion**: Established evidence supports CCT5 as a central chaperone-associated hub embedded in the module's RNA and genome-maintenance signature. Its proposed role in stabilizing telomere-related or other module proteins in this tissue-shared state remains a hypothesis.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): HNRNPR (0.87), MATR3 (0.87), PCNA (0.87), CCT5 (0.86), DDX5 (0.85), LMNB2 (0.83), DDX6 (0.83), PAICS (0.82), LMNB1 (0.80); STRING partners: CCT3 (0.766), CCT5 (0.705), HSP90AA1 (0.886)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 is a high-connectivity bridge linking RNA-associated proteins, CCT5, PCNA, LMNB2, DDX6 and PAICS. It is represented in primary terms for nucleic-acid binding, biosynthetic regulation, telomere maintenance and chromosome organization (8 globally significant GO/KEGG terms, q_global 0.014–0.042; see the table). Its annotated ATPase and DNA-helicase activities and roles in DNA repair, recombination, replication and telomere maintenance make it a strong candidate for the genome-maintenance arm of the module. STRING supports links to CCT3, CCT5 and HSP90AA1. It also has disease associations involving hypogonadotropic hypogonadism, hepatocellular carcinoma and neoplasm.
- **Conclusion**: Established evidence supports RUVBL2 as a multifunctional ATPase with relevant DNA and telomere functions and as an important network bridge. Its causal contribution to the shared bone-marrow-liver pattern is not established.

#### DDX5

- **Related proteins** (co-abundance neighbors): MATR3 (0.86), HNRNPR (0.85), RUVBL2 (0.85), LMNB1 (0.84), CCT5 (0.84), LMNB2 (0.83), DDX6 (0.82), IMPDH2 (0.80); STRING partners: HNRNPR (0.844), MATR3 (0.894)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 is a highly connected RNA-centered hub associated with MATR3, HNRNPR, DDX6, LMNB1, LMNB2, CCT5 and RUVBL2. It is represented in primary nucleic-acid-binding, mRNA-binding and biosynthetic-regulation terms (4 globally significant GO/KEGG terms, q_global 0.014–0.0415; see the table). Its established functions include RNA remodeling, transcriptional coregulation, alternative splicing and small noncoding-RNA processing. STRING supports relationships with MATR3 and HNRNPR, and DDX5 has a substantial literature and disease-association record.
- **Conclusion**: Established evidence supports DDX5 as a major RNA-processing organizer that could connect transcript handling with nuclear and genome-maintenance processes. It is not established that DDX5 drives the shared module rather than marking broadly active RNA metabolism.

#### MATR3

- **Related proteins** (co-abundance neighbors): RUVBL2 (0.87), DDX5 (0.86), CCT5 (0.85), IMPDH2 (0.85), CCT3 (0.80); STRING partners: DDX5 (0.894), HNRNPL (0.757), HNRNPR (0.714)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: huMAP3_07581.1, huMAP3_10625.1, huMAP3_05721.1
- **Function (MyGene.info)**: matrin 3. This gene encodes a nuclear matrix protein, which is proposed to stabilize certain messenger RNA species. Mutations of this gene are associated with distal myopathy 2, which often includes vocal cord and pharyngeal weakness. Alternatively spliced transcript variants, including read-through transcripts composed of the upstream small nucleolar RNA host gene 4 (non-protein coding) and matrin 3 gene s…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.735); distal myopathy with vocal cord weakness (0.569); neurodegenerative disease (0.529); distal myopathy (0.384); hereditary disease (0.193)
- **Europe PMC papers**: 1756
- **Why important**: MATR3 lies at the intersection of the RNA-binding group and the RUVBL2, CCT and IMPDH2 neighborhoods. It is represented in the globally corrected nucleic-acid-binding term (GO:MF nucleic acid binding; q_global = 0.014). STRING links it to DDX5, HNRNPL and HNRNPR, and hu.MAP repeatedly places it in hnRNP-related complexes (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_05721.1). Its established functions include RNA stabilization and post-transcriptional regulation, with disease associations including amyotrophic lateral sclerosis and distal myopathy with vocal-cord weakness.
- **Conclusion**: Established evidence supports MATR3 as an RNA- and nuclear-matrix-associated connector. Its proposed coupling of RNA stability to chaperone or genome-maintenance components in these tissues is plausible but not directly demonstrated.

#### PCNA

- **Related proteins** (co-abundance neighbors): RUVBL2 (0.87), CACYBP (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proliferating cell nuclear antigen. The protein encoded by this gene is found in the nucleus and is a cofactor of DNA polymerase delta. The encoded protein acts as a homotrimer and helps increase the processivity of leading strand synthesis during DNA replication. In response to DNA damage, this protein is ubiquitinated and is involved in the RAD6-dependent DNA repair pathway. Two transcript variants encoding the same protein have b…
- **Diseases (Open Targets)**: ataxia-telangiectasia-like disorder (0.497); neurodegenerative disease (0.188); neoplasm (0.118); diabetes mellitus (0.116); hepatocellular carcinoma (0.113)
- **Europe PMC papers**: 61820
- **Why important**: PCNA is the clearest marker of the DNA-replication and repair interpretation. It appears in primary DNA-biosynthesis terms (GO:BP positive regulation of DNA biosynthetic process; q_global = 0.00547) (GO:BP regulation of DNA biosynthetic process; q_global = 0.0182) and in telomere, chromosome-organization and biosynthetic-regulation terms (5 globally significant GO/KEGG terms, q_global 0.0221–0.042; see the table). Its established role as a DNA-polymerase processivity factor and participant in mismatch repair and DNA-damage responses provides a strong functional anchor. HPA marks it as bone-marrow tissue enhanced, and STRING supports its relationship with RUVBL2. It also has an exceptionally large literature base and disease associations including ataxia-telangiectasia-like disorder and hepatocellular carcinoma.
- **Conclusion**: Established evidence supports PCNA as a DNA-replication and repair component and as a plausible indicator of proliferative or regenerative activity. The supplied HPA summary does not show liver protein detection, so equivalent protein activity in both tissues should not be assumed.

## Module 5

**Tissue pair**: bone_marrow and liver  
**Genes (13)**: ACSF3, ARPC5L, MTHFD1, DUSP23, GBE1, HADH, HK3, INPP1, ITIH4, MAT2B, NNT, PGM1, SCP2

### Function

The module does not have any GO or KEGG term that passed global correction, and STRING reports no supplementary functional enrichment. Therefore, a single pathway assignment is not statistically established. Its gene content nevertheless suggests a mixed metabolic and cellular-maintenance program. HK3, PGM1, and GBE1 support glucose and glycogen handling; MTHFD1 supports folate-mediated one-carbon metabolism and nucleotide precursor synthesis; NNT supports mitochondrial NADPH production and redox protection; HADH and SCP2 support mitochondrial and peroxisomal fatty-acid and sterol metabolism. DUSP23, ARPC5L, and INPP1 add possible regulation of phosphorylation, actin organization, and phosphatidylinositol signaling. The most defensible interpretation is coordinated metabolic capacity rather than a narrowly defined biological pathway.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: ITIH4 is the clear secreted-to-blood component, while the other genes are intracellular or membrane-associated. Most proteins are detected in both bone marrow and liver. HPA indicates generally low immune-cell specificity, with only limited immune-cell enhancement, so this is not a strongly blood-cell-specific module. Several genes show hepatocyte enhancement, and the module also contains liver- or skeletal-muscle-associated genes, including MTHFD1, SCP2, GBE1, PGM1, and NNT. The pattern is therefore compatible with a shared metabolic program or shared cell-composition signal involving hepatocyte-like and metabolically active cells, rather than a simple plasma-protein signature. ITIH4 may additionally reflect liver-derived blood protein in samples.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides two high-confidence relationships within the module: GBE1 with PGM1, and HADH with SCP2. These support established links between glycogen metabolism and between fatty-acid or sterol metabolism, respectively. Most module relationships are not represented by high-confidence STRING associations, and STRING reports no functional enrichment. hu.MAP identifies complex C1 containing MTHFD1 and HADH together with other complex members that are outside this module. This is evidence for a partially represented known molecular complex, but not evidence that the entire co-abundance module is a physical complex. Overall, the network combines a small amount of previously supported molecular connectivity with many relationships that may reflect co-expression, shared cell state, or indirect metabolic coordination.

**STRING interactions (score >= 0.7)**: 2 of 78 gene pairs: GBE1–PGM1 (0.942); HADH–SCP2 (0.905)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12823.1 (MTHFD1, HADH; 2/7)

### Novelty

The module should not be described as a definitively new biological discovery. Its constituent functions and the GBE1-PGM1, HADH-SCP2, and C1 complex relationships are already established, and the genes have substantial prior disease and literature annotation. At the same time, the specific conserved co-abundance arrangement across bone marrow and liver is not explained by the available STRING or hu.MAP evidence. The lack of global GO or KEGG enrichment and the sparse known interaction support make the module hypothesis-generating rather than a validated new pathway. Absence from interaction databases alone cannot establish novelty; independent replication, preservation testing, cell-composition adjustment, and experimental validation would be needed.

**Hypothesis.** Hypothesis: the conserved module reflects a shared metabolic and redox state present in metabolically active cells from bone marrow and liver. Glycogen and glucose processing through HK3, PGM1, and GBE1 may be coordinated with folate-dependent biosynthetic capacity through MTHFD1, while NNT supplies reducing power and HADH with SCP2 supports lipid oxidation and sterol handling. The association may arise from a common cellular state or tissue-composition component rather than direct physical interaction among all members. ITIH4 could contribute a liver-derived circulating signal, whereas the low immune-cell specificity argues against interpreting the module as a dedicated hematopoietic immune program.

### Important genes

#### MTHFD1

- **Related proteins** (co-abundance neighbors): NNT (0.88), GBE1 (0.83), DUSP23 (0.82), PGM1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: huMAP3_12823.1
- **Function (MyGene.info)**: methylenetetrahydrofolate dehydrogenase, cyclohydrolase and formyltetrahydrofolate synthetase 1. This gene encodes a protein that possesses three distinct enzymatic activities, 5,10-methylenetetrahydrofolate dehydrogenase, 5,10-methenyltetrahydrofolate cyclohydrolase and 10-formyltetrahydrofolate synthetase. Each of these activities catalyzes one of three sequential reactions in the interconversion of 1-carbon derivatives of tetrahydrofolate, which are substrates for methionine, thymidylate, …
- **Diseases (Open Targets)**: combined immunodeficiency and megaloblastic anemia with or without hyperhomocysteinemia (0.773); severe combined immunodeficiency (0.473); neural tube defects, folate-sensitive (0.414); isolated spina bifida (0.376); atrial fibrillation (0.332)
- **Europe PMC papers**: 1939
- **Why important**: MTHFD1 is one of the most connected genes in the module and links NNT, GBE1, DUSP23, and PGM1. It is a trifunctional folate enzyme involved in one-carbon metabolism, purine synthesis, and thymidylate-related precursor production. HPA describes liver enrichment, hepatocyte enhancement, cytosolic localization, and detection in both tissues. Its disease associations include combined immunodeficiency and megaloblastic anemia, making it especially relevant to a bone-marrow and liver comparison. The literature base is substantial.
- **Conclusion**: Established: MTHFD1 is a central network connector with core biosynthetic functions and relevant hematologic and hepatic expression evidence. Hypothesis: it may organize the module around biosynthetic demand and redox-supported nucleotide production, but the absence of globally significant enrichment prevents assigning it as the definitive module driver.

#### HK3

- **Related proteins** (co-abundance neighbors): ACSF3 (0.83), MAT2B (0.83), ITIH4 (0.81), INPP1 (0.81), ARPC5L (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hexokinase 3. Hexokinases phosphorylate glucose to produce glucose-6-phosphate, the first step in most glucose metabolism pathways. This gene encodes hexokinase 3. Similar to hexokinases 1 and 2, this allosteric enzyme is inhibited by its product glucose-6-phosphate. [provided by RefSeq, Apr 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.217); myeloproliferative disorder (0.122); neoplasm (0.111); glioblastoma (0.099); nonpapillary renal cell carcinoma (0.095)
- **Europe PMC papers**: 11024
- **Why important**: HK3 has the strongest network connectivity in the module and connects glucose phosphorylation with ACSF3, MAT2B, ITIH4, INPP1, and ARPC5L. Hexokinase activity supplies glucose-six-phosphate to downstream carbohydrate pathways. HPA links HK3 to bone marrow and lymphoid tissue, macrophage and monocyte-progenitor-related cell types, and basophil enhancement, while it is not detected in liver by the reported immunohistochemistry. Its literature volume is extensive and its disease associations include myeloproliferative disorder and neoplasm.
- **Conclusion**: Established: HK3 is a prominent network hub with a plausible carbohydrate-entry function and a bone-marrow-associated expression pattern. Hypothesis: HK3 may connect metabolic activity to the cellular composition of bone marrow, but its relationship to the liver side of the conserved module remains unresolved.

#### NNT

- **Related proteins** (co-abundance neighbors): MTHFD1 (0.88), SCP2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nicotinamide nucleotide transhydrogenase. This gene encodes an integral protein of the inner mitochondrial membrane. The enzyme couples hydride transfer between NAD(H) and NADP(+) to proton translocation across the inner mitochondrial membrane. Under most physiological conditions, the enzyme uses energy from the mitochondrial proton gradient to produce high concentrations of NADPH. The resulting NADPH is used for biosynthesis and in free …
- **Diseases (Open Targets)**: familial glucocorticoid deficiency (0.638); neurodegenerative disease (0.497); hereditary disease (0.453); atypical hemolytic-uremic syndrome with DGKE deficiency (0.416); Abnormality of the skeletal system (0.396)
- **Europe PMC papers**: 6111
- **Why important**: NNT connects MTHFD1 and SCP2 and provides a mechanistic bridge between biosynthesis and lipid or sterol metabolism. Its mitochondrial transhydrogenase activity generates NADPH used in biosynthesis and reactive-oxygen control. HPA shows tissue enhancement in skeletal muscle, hepatocyte-related cell enhancement, mitochondrial localization, and detection in both tissues. It also has a substantial literature base and disease associations involving glucocorticoid deficiency, hereditary disease, and redox-relevant pathology.
- **Conclusion**: Established: NNT is a plausible redox-supporting connector between otherwise distinct metabolic parts of the module. Hypothesis: the shared module may track a requirement for mitochondrial NADPH during combined biosynthetic and oxidative metabolism, although co-abundance does not establish flux or causality.

#### GBE1

- **Related proteins** (co-abundance neighbors): MTHFD1 (0.83); STRING partners: PGM1 (0.942)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 1,4-alpha-glucan branching enzyme 1. The protein encoded by this gene is a glycogen branching enzyme that catalyzes the transfer of alpha-1,4-linked glucosyl units from the outer end of a glycogen chain to an alpha-1,6 position on the same or a neighboring glycogen chain. Branching of the chains is essential to increase the solubility of the glycogen molecule and, consequently, in reducing the osmotic pressure within cells. Highest l…
- **Diseases (Open Targets)**: glycogen storage disease due to glycogen branching enzyme deficiency (0.848); adult polyglucosan body disease (0.801); glycogen storage disease due to glycogen branching enzyme deficiency, adult neuromuscular form (0.711); glycogen storage disease due to glycogen branching enzyme deficiency, congenital neuromuscular form (0.591); disorder of glycogen metabolism (0.573)
- **Europe PMC papers**: 1361
- **Why important**: GBE1 is directly linked to PGM1 in STRING and is connected to MTHFD1 in the module. Its enzyme activity creates glycogen branches, and its highest expression is described in liver and muscle. HPA shows skeletal-muscle tissue enhancement and enhancement in adipocytes, cardiomyocytes, myonuclei, neutrophil progenitors, and neutrophils. Its disease associations are strongly centered on glycogen storage and polyglucosan disorders, with a substantial literature base.
- **Conclusion**: Established: GBE1 and PGM1 provide the clearest known metabolic subrelationship in the module and support glycogen-related interpretation. Hypothesis: glycogen storage or mobilization may be one component of the shared tissue program, but the absence of global enrichment means this cannot be generalized to the whole module.

#### HADH

- **Related proteins** (co-abundance neighbors): DUSP23 (0.81); STRING partners: SCP2 (0.905)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: huMAP3_12823.1
- **Function (MyGene.info)**: hydroxyacyl-CoA dehydrogenase. This gene is a member of the 3-hydroxyacyl-CoA dehydrogenase gene family. The encoded protein functions in the mitochondrial matrix to catalyze the oxidation of straight-chain 3-hydroxyacyl-CoAs as part of the beta-oxidation pathway. Its enzymatic activity is highest with medium-chain-length fatty acids. Mutations in this gene cause one form of familial hyperinsulinemic hypoglycemia. The human gen…
- **Diseases (Open Targets)**: hyperinsulinemic hypoglycemia, familial, 4 (0.814); 3-hydroxyacyl-CoA dehydrogenase deficiency (0.784); long chain 3-hydroxyacyl-CoA dehydrogenase deficiency (0.596); hyperinsulinemic hypoglycemia (0.417); familial hyperinsulinism (0.334)
- **Europe PMC papers**: 2217
- **Why important**: HADH is connected to DUSP23 in the module, to SCP2 by STRING, and to MTHFD1 through complex C1. It catalyzes a step in mitochondrial fatty-acid beta-oxidation and is associated with familial hyperinsulinemic hypoglycemia and related dehydrogenase deficiency. HPA shows enhancement in hepatocytes and several metabolically active epithelial or reproductive cell types, with mitochondrial localization and detection in both tissues. Its literature base is substantial.
- **Conclusion**: Established: HADH contributes a supported fatty-acid oxidation component and participates in both a known STRING relationship and a partially represented hu.MAP complex. Hypothesis: HADH may couple lipid oxidation to the broader redox and biosynthetic state represented by NNT and MTHFD1, but the module does not establish a direct biochemical assembly.

## Module 6

**Tissue pair**: bone_marrow and liver  
**Genes (9)**: ACSL5, AGRN, ALDH3A2, CYP27A1, DNPEP, GOLIM4, GYS1, PDXP, WASHC5

### Function

The module does not have a globally significant GO or KEGG enrichment term. Therefore, no pathway function can be assigned from enrichment alone. Its gene content suggests two biological themes that are joined by co-abundance rather than by established molecular interactions: a liver-associated lipid and sterol metabolic theme involving CYP27A1, ACSL5, and ALDH3A2, and a broader cellular organization and trafficking theme involving AGRN, WASHC5, PDXP, GOLIM4, DNPEP, and GYS1. AGRN is the most connected node in the module and links genes with otherwise heterogeneous functions. The safest interpretation is a tissue-associated expression module with a prominent hepatic lipid-metabolism component, not a demonstrated biochemical pathway.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only AGRN is annotated as secreted to the extracellular matrix. Most members are intracellular proteins, including mitochondrial, cytosolic, endoplasmic-reticulum, Golgi, or microtubule-associated proteins. HPA evidence points more strongly toward liver and epithelial or parenchymal cell contexts than toward a shared blood-cell program. Several genes have liver enrichment or liver protein detection, while the blood-cell evidence is mostly low immune-cell specificity, with isolated associations to classical monocytes, neutrophils, eosinophils, or plasmacytoid dendritic cells. The single-cell annotations are heterogeneous and include enterocytes, podocytes, oligodendrocytes, epithelial populations, and muscle-related cells. Thus, the shared bone-marrow and liver signal could partly reflect tissue composition, vascular or stromal contribution, or broadly shared cellular physiology rather than a module specific to hematopoietic cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction passed the supplied high-confidence interaction threshold, and there is no supplementary STRING functional-enrichment result. No hu.MAP complex contains multiple members of this module. Consequently, the co-abundance edges should not be interpreted as established protein-protein interactions or as membership in a known multiprotein complex. The absence of STRING and hu.MAP support indicates that the network captures coordinated abundance in these tissues, but it does not by itself establish a new physical mechanism or prove that the relationships are biologically novel.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel tissue-level co-abundance pattern, because the module is not represented by a known high-confidence STRING interaction network or a shared hu.MAP complex. However, it cannot be called a newly discovered biological pathway or protein complex. The genes themselves have well-established functions and disease associations, especially CYP27A1, AGRN, ACSL5, ALDH3A2, GYS1, and WASHC5. The lack of global GO or KEGG enrichment and the absence of known physical interactions make the strongest novelty claim one of coordinated abundance across bone marrow and liver, pending replication in independent cohorts and testing against cell-composition, batch, and tissue-mixture confounders.

**Hypothesis.** Hypothesis: the module reflects a shared tissue-state or cellular-composition signal in which a liver-associated lipid and sterol program is correlated with intracellular trafficking, cytoskeletal, glycogen, and extracellular-matrix-related genes. CYP27A1, ACSL5, and ALDH3A2 could represent coordinated mitochondrial, fatty-acid, sterol, and aldehyde handling, while AGRN and WASHC5 may mark extracellular-matrix or cytoskeletal and endosomal organization that links this metabolic state to cell structure. This hypothesis predicts that the module will weaken after adjustment for hepatocyte, epithelial, stromal, and other cell-type proportions, and that any remaining coordination should be tested with independent expression datasets and perturbation experiments. It is a mechanistic proposal, not an established conclusion.

### Important genes

#### AGRN

- **Related proteins** (co-abundance neighbors): WASHC5 (0.88), GYS1 (0.87), DNPEP (0.82), PDXP (0.81), GOLIM4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: agrin. This gene encodes one of several proteins that are critical in the development of the neuromuscular junction (NMJ), as identified in mouse knock-out studies. The encoded protein contains several laminin G, Kazal type serine protease inhibitor, and epidermal growth factor domains. Additional post-translational modifications occur to add glycosaminoglycans and disulfide bonds. In one family with con…
- **Diseases (Open Targets)**: congenital myasthenic syndrome 8 (0.793); congenital myasthenic syndrome (0.680); presynaptic congenital myasthenic syndrome (0.652); postsynaptic congenital myasthenic syndrome (0.626); COVID-19 (0.546)
- **Europe PMC papers**: 2731
- **Why important**: AGRN is the most connected node in the module and links several otherwise diverse genes, giving it the strongest network-centrality rationale. It encodes an extracellular-matrix protein with established roles in neuromuscular-junction development and reported roles in cell-surface signaling and cytoskeletal organization. HPA detects it in both relevant tissues and does not detect it in immune cells, which argues against interpreting it as a simple blood-cell marker. Its congenital myasthenic-syndrome associations and substantial literature make it biologically prominent, although those disease links do not establish a role in this module.
- **Conclusion**: Established: AGRN is the central co-abundance connector and an extracellular-matrix and signaling protein with disease relevance. Hypothesis: it may couple cellular structural state or matrix-related biology to the metabolic genes in this module, but the available interaction resources do not support a direct molecular complex.

#### CYP27A1

- **Related proteins** (co-abundance neighbors): WASHC5 (0.84), ACSL5 (0.83), ALDH3A2 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome P450 family 27 subfamily A member 1. This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This mitochondrial protein oxidizes cholesterol intermediates as part of the bile synthesis pathway. Since the conversion of cholesterol to bile acids is the major…
- **Diseases (Open Targets)**: cerebrotendinous xanthomatosis (0.867); Abnormality of the cardiovascular system (0.541); Senior-Loken syndrome 1 (0.340); photosensitive epilepsy (0.185); Seizure (0.185)
- **Europe PMC papers**: 5567
- **Why important**: CYP27A1 is a highly connected member of the liver-associated branch and is annotated as a mitochondrial cytochrome P450 involved in cholesterol-intermediate oxidation, bile-acid synthesis, sterol metabolism, and vitamin D metabolism. HPA places it in liver-enriched tissue and hepatocyte-related contexts, with no liver protein-detection ambiguity in the supplied evidence. Its established association with cerebrotendinous xanthomatosis and extensive literature make it a strong functional anchor for the hepatic metabolic interpretation.
- **Conclusion**: Established: CYP27A1 provides the clearest biochemical rationale for a liver-linked sterol and bile-acid component. Hypothesis: its co-abundance with ACSL5 and ALDH3A2 may represent coordinated lipid-handling state, but enrichment and physical interaction evidence do not establish that this is a single pathway.

#### ACSL5

- **Related proteins** (co-abundance neighbors): CYP27A1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 5. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme is highly expressed…
- **Diseases (Open Targets)**: mathematical ability (0.427); diarrhea 13 (0.341); idiopathic pulmonary fibrosis (0.292); arthritic joint disease (0.252); adrenal gland disorder (0.223)
- **Europe PMC papers**: 1812
- **Why important**: ACSL5 is connected to CYP27A1 and is a long-chain fatty-acyl-CoA synthetase involved in fatty-acid activation, lipid biosynthesis, and fatty-acid degradation. Its HPA profile is tissue-enhanced in liver and intestine and cell-type-enhanced in enterocyte and related epithelial populations, supporting a metabolic and epithelial context. It has substantial literature and multiple disease-associated signals, although the supplied disease associations are not specific evidence for this module.
- **Conclusion**: Established: ACSL5 is a plausible marker of long-chain fatty-acid metabolism in the liver-associated branch. Hypothesis: it may cooperate functionally with CYP27A1 in a lipid-processing state, but the module data show co-abundance rather than direct cooperation.

#### ALDH3A2

- **Related proteins** (co-abundance neighbors): CYP27A1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 3 family member A2. Aldehyde dehydrogenase isozymes are thought to play a major role in the detoxification of aldehydes generated by alcohol metabolism and lipid peroxidation. This gene product catalyzes the oxidation of long-chain aliphatic aldehydes to fatty acid. Mutations in the gene cause Sjogren-Larsson syndrome. Alternatively spliced transcript variants encoding different isoforms have been found for this gene…
- **Diseases (Open Targets)**: Sjogren-Larsson syndrome (0.850); hereditary disease (0.415); cerebral palsy (0.340); neurodegenerative disease (0.193); neoplasm (0.099)
- **Europe PMC papers**: 1499
- **Why important**: ALDH3A2 is connected to CYP27A1 and encodes an aldehyde dehydrogenase that oxidizes long-chain aliphatic aldehydes generated during lipid peroxidation and related metabolism. It is tissue-enhanced in liver and detected there at the protein level. Its established association with Sjogren-Larsson syndrome and substantial literature provide a strong disease and functional rationale for prioritization.
- **Conclusion**: Established: ALDH3A2 supports an interpretation involving aldehyde detoxification and lipid-peroxidation handling in liver. Hypothesis: its co-abundance with CYP27A1 and ACSL5 could reflect coordinated protection from or processing of lipid-derived metabolites, but this remains untested.

#### WASHC5

- **Related proteins** (co-abundance neighbors): AGRN (0.88), CYP27A1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WASH complex subunit 5. This gene encodes a 134 kDa protein named strumpellin that is predicted to have multiple transmembrane domains and a spectrin-repeat-containing domain. This ubiquitously expressed gene has its highest expression in skeletal muscle. The protein is named for Strumpell disease; a form of hereditary spastic paraplegia (HSP). Spastic paraplegias are a diverse group of disorders in which the autosomal d…
- **Diseases (Open Targets)**: hereditary spastic paraplegia 8 (0.802); Ritscher-Schinzel syndrome 1 (0.727); Ritscher-Schinzel syndrome (0.711); hereditary disease (0.493); hereditary spastic paraplegia (0.350)
- **Europe PMC papers**: 238
- **Why important**: WASHC5 connects the AGRN and CYP27A1 portions of the graph, making it important as a topological bridge despite its limited degree. It encodes strumpellin, a WASH-complex subunit involved in endosome organization, endosomal transport, actin polymerization, and regulation of Arp2/3-mediated actin nucleation. HPA detects it in both tissues and reports oligodendrocyte-related cell-type enhancement. Its hereditary spastic paraplegia and Ritscher-Schinzel syndrome associations support biological importance, while its more limited literature volume than the major metabolic genes makes its module-specific role less established.
- **Conclusion**: Established: WASHC5 is a cytoskeletal and endosomal-trafficking gene that bridges the two main co-abundance branches. Hypothesis: it may link intracellular trafficking or actin state to the liver-associated metabolic signal, but no STRING or hu.MAP evidence supports a direct complex involving these module members.

## Module 7

**Tissue pair**: bone_marrow and liver  
**Genes (7)**: AFM, EFHD2, EWSR1, GNAI3, ME2, RAB8B, TXLNA

### Function

The module has no GO or KEGG term passing global correction, and STRING reports no functional enrichment. Therefore, its function cannot be assigned from enrichment statistics alone. The network is star-like, with AFM connected to every other member, while the remaining genes have no connections to one another. The gene annotations suggest several biological themes rather than one established pathway: AFM is a liver-derived extracellular transport and protein-stabilization factor; RAB8B is involved in vesicle trafficking and exocytosis; GNAI3 participates in G-protein and receptor signaling; ME2 supports mitochondrial malate-to-pyruvate metabolism; EFHD2 is linked to actin crosslinking and cadherin binding; TXLNA is associated with syntaxin binding and exocytosis; and EWSR1 has roles in transcriptional regulation and RNA processing. The most defensible interpretation is a tissue-pair co-abundance pattern centered on AFM, with possible contributions from secretion, membrane trafficking, signaling, metabolism, and cell-state composition. These annotations are functional clues, not evidence of a single validated pathway.

**Cell composition.** The module is not predominantly composed of secreted or plasma proteins: AFM is the secreted-to-blood member, whereas the other genes are intracellular or membrane-associated. AFM has liver-enriched expression and is associated with hepatocytes and proximal tubule cells, making liver-derived circulating protein a plausible contributor. Several other members have cell-type-enhanced expression involving neutrophils, monocytes, or related immune and hematopoietic populations, while RAB8B is enhanced in bone marrow and EFHD2 is immune-cell enhanced for neutrophils. At the same time, most members have low tissue or low immune-cell specificity, so the module is not a clean blood-cell signature. HPA protein detection is stronger in bone marrow than in liver for the module overall, while AFM protein is not detected by IHC in either listed tissue despite its liver-enriched and secreted annotation. Thus, shared blood exposure, hepatocyte-derived AFM, and shared or variable cell-type composition could all contribute to the cross-tissue module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair reaches the supplied STRING interaction threshold, and STRING provides no supplementary enrichment. Consequently, the co-abundance edges are not supported here by high-confidence, already catalogued STRING relationships. hu.MAP provides one relevant complex association, (hu.MAP huMAP3_14442.1), in which ME2 and EFHD2 occur among the members of a much larger complex. This supports some possible biochemical or proteomic context for those two genes, but it does not establish that they directly interact or that the entire module is a single complex. The combination of a hub-centered co-abundance pattern, absent STRING links, and only partial hu.MAP membership indicates that the network is primarily an expression or abundance association rather than a demonstrated physical interaction network.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (ME2, EFHD2; 2/57)

### Novelty

The module may represent a tissue-pair-specific co-abundance pattern, but it should not be called a newly discovered biological pathway. AFM-centered links to TXLNA, EWSR1, RAB8B, ME2, EFHD2, and GNAI3 are not represented by the supplied STRING evidence, and most are also absent from the supplied hu.MAP evidence. That absence is compatible with a potentially undercharacterized association, but it does not prove novelty: co-abundance can arise from shared tissue composition, circulating protein contamination or exposure, technical effects, or correlated regulation without direct molecular interaction. The lack of globally significant GO or KEGG enrichment further limits claims of a coherent new function. A cautious novelty claim is therefore that this particular cross-tissue co-abundance configuration may be data-specific and worth independent replication, not that it establishes a novel mechanism.

**Hypothesis.** Hypothesis: a liver-derived, circulating AFM signal is coupled across the bone-marrow and liver samples to variation in membrane trafficking, exocytosis, receptor signaling, mitochondrial metabolism, and cytoskeletal state. In this model, AFM is the abundance hub or an indirect marker of a shared physiological state; RAB8B and TXLNA could reflect vesicle handling, GNAI3 could reflect receptor-linked signaling, ME2 could reflect metabolic state, and EFHD2 could reflect actin or adhesion remodeling. The apparent association with EWSR1 may instead reflect a broader cellular-state or transcript-processing component. This hypothesis is not established by the enrichment results, STRING, or hu.MAP and requires validation using independent cohorts, cell-type-resolved data, protein measurements, and perturbation or interaction assays.

### Important genes

#### AFM

- **Related proteins** (co-abundance neighbors): TXLNA (0.91), EWSR1 (0.84), RAB8B (0.84), ME2 (0.81), EFHD2 (0.80), GNAI3 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: afamin. This gene is a member of the albumin gene family, which is comprised of four genes that localize to chromosome 4 in a tandem arrangement. These four genes encode structurally-related serum transport proteins that are known to be evolutionarily related. The protein encoded by this gene is regulated developmentally, expressed in the liver and secreted into the bloodstream. [provided by RefSeq, Jul 2…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.249); prostate carcinoma (0.204); adrenal gland disorder (0.103); non-alcoholic fatty liver (0.091); metabolic syndrome (0.082)
- **Europe PMC papers**: 24965
- **Why important**: AFM is the network hub, connecting to every other module member, and is the only annotated secreted-to-blood protein. It is liver-enriched, belongs to the albumin family of serum transport proteins, and is linked to nutrient response, protein stabilization, vitamin transport, and extracellular protein transport. Its extensive literature and disease-association record make it the strongest biological anchor, while its absence from STRING and hu.MAP leaves the hub role as an association-based observation rather than a demonstrated interaction hub.
- **Conclusion**: Established evidence supports AFM as a liver-associated circulating transport protein and as the central co-abundance correlate in this module. It is plausible that AFM helps report a shared systemic or hepatic state, but the data do not establish that AFM mechanistically regulates the other genes.

#### RAB8B

- **Related proteins** (co-abundance neighbors): AFM (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB8B, member RAS oncogene family. RAB proteins, like RAB8B, are low molecular mass monomeric GTPases that localize on the cytoplasmic surfaces of distinct membrane-bound organelles. RAB proteins function in intracellular vesicle transport by aiding in the docking and/or fusion of vesicles with their target membranes (summary by Chen et al., 1997 [PubMed 9030196]).[supplied by OMIM, Nov 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.287); placenta praevia (0.192); tooth disorder (0.126); osteoarthritis, hip (0.095); infection (0.072)
- **Europe PMC papers**: 871
- **Why important**: RAB8B is directly connected to AFM and has annotations for vesicle docking and fusion, exocytosis, endocytic recycling, antigen processing, and cell-projection organization. HPA shows bone-marrow tissue enhancement and cell-type enhancement across several hematopoietic or specialized populations, including monocytes and neutrophil progenitors. Its established trafficking function provides a biologically coherent link to the secreted-protein aspect of the module.
- **Conclusion**: Established evidence supports RAB8B as a vesicle-trafficking regulator with relevant bone-marrow cellular expression. Its relationship with AFM is a co-abundance association; whether it contributes to AFM secretion or merely tracks cell composition is a hypothesis.

#### GNAI3

- **Related proteins** (co-abundance neighbors): AFM (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Centrosome, Principal piece; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein subunit alpha i3. Guanine nucleotide-binding proteins (G proteins) are involved as modulators or transducers in various transmembrane signaling pathways. G proteins are composed of 3 units: alpha, beta and gamma. This gene encodes an alpha subunit and belongs to the G-alpha family. Mutation in this gene, resulting in a gly40-to-arg substitution, is associated with auriculocondylar syndrome, and shown to affect down…
- **Diseases (Open Targets)**: auriculocondylar syndrome (0.764); agnathia-otocephaly complex (0.370); hereditary disease (0.191); Abnormality of the skeletal system (0.140); frozen shoulder (0.135)
- **Europe PMC papers**: 1172
- **Why important**: GNAI3 is connected to AFM and has broad signaling annotations involving G-protein-coupled receptors, adenylate cyclase inhibition, signal transduction, and macroautophagy. It is cell-type enhanced in neutrophils and has a strong disease association with auriculocondylar syndrome, as well as skeletal-system associations. Its signaling role could connect extracellular or membrane cues with intracellular cellular-state changes.
- **Conclusion**: Established evidence supports GNAI3 as a G-protein signaling component with relevant hematopoietic expression and disease biology. The module does not show that GNAI3 transduces an AFM-dependent signal; that proposed connection remains mechanistic speculation.

#### ME2

- **Related proteins** (co-abundance neighbors): AFM (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: malic enzyme 2. This gene encodes a mitochondrial NAD-dependent malic enzyme, a homotetrameric protein, that catalyzes the oxidative decarboxylation of malate to pyruvate. It had previously been weakly linked to a syndrome known as Friedreich ataxia that has since been shown to be the result of mutation in a completely different gene. Certain single-nucleotide polymorphism haplotypes of this gene have been shown …
- **Diseases (Open Targets)**: liver disorder (0.215); diabetes mellitus (0.214); major depressive disorder (0.213); aneurysm (0.133); aortic aneurysm (0.132)
- **Europe PMC papers**: 6359
- **Why important**: ME2 is connected to AFM and is one of the two module members occurring in the hu.MAP complex (hu.MAP huMAP3_14442.1). It encodes a mitochondrial NAD-dependent malic enzyme involved in oxidative decarboxylation of malate to pyruvate and regulation of NADP metabolism. Its tissue and cell-type patterns include choroid plexus, Kupffer cells, and other specialized cell populations, and it has substantial literature and disease-association coverage including liver disorder and diabetes.
- **Conclusion**: Established evidence supports ME2 as a mitochondrial metabolic enzyme and supports its partial membership in (hu.MAP huMAP3_14442.1). Its co-abundance with AFM could indicate a shared hepatic or metabolic state, but the module does not establish direct physical coupling or a causal metabolic role.

#### EFHD2

- **Related proteins** (co-abundance neighbors): AFM (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: EF-hand domain family member D2. Enables cadherin binding activity. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: alcoholic pancreatitis (0.133); cancer (0.099); neoplasm (0.085); melanoma (0.079); lung cancer (0.078)
- **Europe PMC papers**: 542
- **Why important**: EFHD2 is connected to AFM, is the second module member in hu.MAP complex (hu.MAP huMAP3_14442.1), and is annotated for cadherin binding and actin crosslink formation. HPA identifies enhancement in neutrophils and detection in bone marrow but not liver, making it relevant to a possible hematopoietic or cell-structural component of the shared pattern. Its more limited literature base makes it less established than AFM, ME2, or GNAI3, but its structural annotation is useful for interpreting the network.
- **Conclusion**: Established evidence supports EFHD2 as a cytoskeletal or adhesion-associated protein with partial complex context in (hu.MAP huMAP3_14442.1). Its association with AFM may reflect bone-marrow cell composition or coordinated structural state rather than a direct role in hepatic secretion.

## Module 8

**Tissue pair**: bone_marrow and liver  
**Genes (23)**: AIMP1, CAPN1, CLIC4, DDI2, EIF2B5, GMPPB, HNRNPH1, EIF6, AK4, MTAP, NDUFA9, PDCD10, PDXDC1, RHOG, SCFD1, SMS, SUCLA2, TXN, TMX1, TOMM40, TXNDC17, UGDH, XPO7

### Function

The functional enrichment of this module converges on thioredoxin-mediated redox regulation and methionine salvage / polyamine biosynthesis. Protein-disulfide reductase activity is the most distinctive molecular-function signal (GO:MF protein-disulfide reductase activity; q_global = 0.00255), with the related disulfide oxidoreductase and sulfur-donor oxidoreductase terms (GO:MF disulfide oxidoreductase activity; q_global = 0.00419) (GO:MF oxidoreductase activity, acting on a sulfur group of donors; q_global = 0.011), all driven by the thioredoxin-family members TXN, TXNDC17 and TMX1. STRING independently supports this redox signature through the redox-active center keyword (STRING Keyword Redox-active center; within-query FDR = 0.011), and it also recovers the methionine de novo and salvage pathway (STRING WikiPathways Methionine de novo and salvage pathway; within-query FDR = 0.0022) linking TXN with spermine synthase (SMS) and methylthioadenosine phosphorylase (MTAP). TXN therefore provides a mechanistic bridge between the two axes, consistent with its role as the electron donor for methionine sulfoxide reductases, which couple thioredoxin-dependent reducing power to the recycling of oxidized methionine residues. The co-abundance of SMS and MTAP further supports a coupled polyamine-methionine salvage program: SMS produces methylthioadenosine during spermine biosynthesis, whereas MTAP cleaves methylthioadenosine to recycle methionine. Cytosolic and extracellular-exosome localization terms (GO:CC cytosol; q_global = 0.000213) (GO:CC extracellular exosome; q_global = 0.000488), a nucleobase-containing small-molecule metabolism term (GO:BP nucleobase-containing small molecule metabolic process; q_global = 0.00817) and a mitochondria-associated ER membrane contact-site term involving TMX1 and TOMM40 (GO:CC mitochondria-associated endoplasmic reticulum membrane contact site; q_global = 0.0437) place this redox and salvage core within a broader intracellular metabolic context.

**Cell composition.** The module is not dominated by plasma or secreted proteins: most members are intracellular, broadly expressed proteins with low tissue specificity, and only a few are annotated as secreted. Few members show blood-cell enrichment, so blood contamination is unlikely to explain the shared signal on its own. All members have HPA annotation and many are detected by immunohistochemistry in liver and in bone marrow. STRING tissue enrichment identifies the digestive gland as the dominant tissue signal (STRING TISSUES Digestive gland; within-query FDR = 0.0011), with a broader visceral signal (STRING TISSUES Viscus; within-query FDR = 0.0054), supporting the liver component of this cross-tissue module. Acetylation is the strongest STRING keyword enrichment (STRING Keyword Acetylation; within-query FDR = 2.58e-05), covering most members and suggesting a shared post-translational regulatory layer.

**GO/KEGG enrichment**: 7 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC cytosol | 0.000213 | AIMP1, CAPN1, CLIC4, DDI2, EIF2B5, EIF6, GMPPB, HNRNPH1, MTAP, PDCD10, RHOG, SCFD1, SMS, TOMM40, TXN, TXNDC17, UGDH |
| GO:CC extracellular exosome | 0.000488 | CAPN1, CLIC4, EIF6, MTAP, PDCD10, RHOG, SMS, SUCLA2, TXN, TXNDC17, UGDH |
| GO:MF protein-disulfide reductase activity | 0.00255 | TMX1, TXN, TXNDC17 |
| GO:MF disulfide oxidoreductase activity | 0.00419 | TMX1, TXN, TXNDC17 |
| GO:BP nucleobase-containing small molecule metabolic process | 0.00817 | AK4, EIF6, GMPPB, MTAP, NDUFA9, SUCLA2, UGDH |
| GO:MF oxidoreductase activity, acting on a sulfur group of donors | 0.011 | TMX1, TXN, TXNDC17 |
| GO:CC mitochondria-associated endoplasmic reticulum membrane contact site | 0.0437 | TMX1, TOMM40 |

### STRING and hu.MAP

STRING records only three high-confidence interactions among all possible member pairs: TXNDC17 with TXN, TXN with TMX1, and SMS with MTAP, the last being the highest-confidence pair in the module. These three known relationships correspond exactly to the redox and methionine-salvage axes, while the remaining co-abundance relationships, including those of AIMP1, CAPN1 and EIF2B5, are not documented as physical interactions. hu.MAP contains no complex covering the module; the only matches are partial complexes that pair EIF2B5 with XPO7 (hu.MAP huMAP3_10202.1) (hu.MAP huMAP3_10287.1) (hu.MAP huMAP3_11232.1), which do not include the redox, salvage or other members. The module as a whole has therefore not been characterized as a functional unit.

**STRING interactions (score >= 0.7)**: 3 of 253 gene pairs: MTAP–SMS (0.986); TMX1–TXN (0.858); TXN–TXNDC17 (0.847)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Acetylation (FDR = 2.58e-05, 16 genes); TISSUES Digestive gland (FDR = 0.0011, 14 genes); WikiPathways Methionine de novo and salvage pathway (FDR = 0.0022, 3 genes); TISSUES Viscus (FDR = 0.0054, 17 genes); Keyword Redox-active center (FDR = 0.011, 3 genes); Component Extracellular exosome (FDR = 0.016, 11 genes); Process Organonitrogen compound biosynthetic process (FDR = 0.017, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10202.1 (EIF2B5, XPO7; 2/52); huMAP3_10287.1 (EIF2B5, XPO7; 2/53); huMAP3_11232.1 (EIF2B5, XPO7; 2/78)

### Novelty

The clinical relevance of this module is highlighted by the convergence of three members, AIMP1, CAPN1 and EIF2B5, each independently implicated in heritable white matter disease: AIMP1 in hypomyelinating leukodystrophy and Pelizaeus-Merzbacher-like disease, CAPN1 in autosomal recessive spastic paraplegia type 76, and EIF2B5 in leukoencephalopathy with vanishing white matter. No common molecular mechanism has been proposed to explain their convergence on white matter pathology, and the pipeline recovers their association through an orthogonal approach: protein co-abundance across liver and bone marrow. Together with the sparse STRING coverage and the absence of a covering hu.MAP complex, this identifies the module as a coordination pattern that current interaction and complex databases do not capture.

**Hypothesis.** Hypothesis: the module represents a translational checkpoint and stress-response program. AIMP1 and EIF2B5 both participate in the GCN2-eIF2alpha-eIF2B integrated stress response axis: EIF2B5 dysfunction leads to integrated stress response deregulation in white matter astrocytes, and AIMP1, a component of the multi-aminoacyl-tRNA synthetase complex, connects upstream to the same axis through the nutrient-sensing kinase GCN2. The same GCN2-eIF2alpha axis is a central regulator of hematopoietic stem cell proteostasis in bone marrow, which offers a biological basis for why this program surfaces as a liver-bone marrow co-abundance signal. The co-abundance of CAPN1 with AIMP1 and EIF2B5 suggests that calpain-1 participates in the same translational and proteostatic program whose disruption leads to white matter pathology, an association that has not been reported. Coupled thioredoxin redox capacity and methionine salvage would supply the reducing power and methionine recycling such a stress-response program requires. These links are hypotheses that co-abundance alone cannot establish.

### Important genes

#### TXN

- **Related proteins** (co-abundance neighbors): TXNDC17 (0.87), SMS (0.87), CAPN1 (0.83); STRING partners: TMX1 (0.858), TXNDC17 (0.847)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin. The protein encoded by this gene acts as a homodimer and is involved in many redox reactions. The encoded protein is active in the reversible S-nitrosylation of cysteines in certain proteins, which is part of the response to intracellular nitric oxide. This protein is found in the cytoplasm. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct…
- **Diseases (Open Targets)**: neurodegenerative disease (0.530); smoking initiation (0.288); ovarian neoplasm (0.171); cancer (0.122); neoplasm (0.114)
- **Europe PMC papers**: 4080
- **Why important**: TXN is the hub of the redox axis: it carries the protein-disulfide reductase and redox-active center signals (GO:MF protein-disulfide reductase activity; q_global = 0.00255) (STRING Keyword Redox-active center; within-query FDR = 0.011), has the module's STRING interactions with TXNDC17 and TMX1, and is the only member shared with the methionine de novo and salvage pathway (STRING WikiPathways Methionine de novo and salvage pathway; within-query FDR = 0.0022).
- **Conclusion**: TXN is the mechanistic bridge of the module, linking thioredoxin-dependent reducing power to methionine recycling through methionine sulfoxide reduction.

#### SMS

- **Related proteins** (co-abundance neighbors): TXN (0.87), EIF6 (0.82), MTAP (0.82), UGDH (0.80); STRING partners: MTAP (0.986)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: spermine synthase. This gene encodes a protein belonging to the spermidine/spermin synthase family and catalyzes the production of spermine from spermidine. Pseudogenes of this gene are located on chromosomes 1, 5, 6 and X. Mutations in this gene cause an X-linked intellectual disability called Snyder-Robinson Syndrome (SRS). Multiple transcript variants encoding different isoforms have been found for this gene. [pr…
- **Diseases (Open Targets)**: syndromic X-linked intellectual disability Snyder type (0.814); hereditary disease (0.484); Intellectual disability (0.337); autoimmune disorder of central nervous system (0.336); neurodegenerative disease (0.331)
- **Europe PMC papers**: 14362
- **Why important**: SMS forms the highest-confidence STRING pair of the module with MTAP and belongs to the methionine de novo and salvage pathway (STRING WikiPathways Methionine de novo and salvage pathway; within-query FDR = 0.0022); it produces methylthioadenosine during spermine biosynthesis.
- **Conclusion**: Together with MTAP, SMS defines a coupled polyamine-methionine salvage program within the module.

#### MTAP

- **Related proteins** (co-abundance neighbors): SMS (0.82); STRING partners: SMS (0.986)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methylthioadenosine phosphorylase. This gene encodes an enzyme that plays a major role in polyamine metabolism and is important for the salvage pathway of both adenine and methionine. The encoded enzyme is deficient in many cancers. Multiple alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Sep 2021].
- **Diseases (Open Targets)**: diaphyseal medullary stenosis-bone malignancy syndrome (0.702); cutaneous melanoma (0.524); melanoma (0.509); coronary artery disorder (0.420); lung adenocarcinoma (0.407)
- **Europe PMC papers**: 3295
- **Why important**: MTAP cleaves methylthioadenosine generated by SMS to recycle methionine, is linked to SMS by the strongest STRING interaction in the module, and appears in the salvage and nucleobase-metabolism annotations (STRING WikiPathways Methionine de novo and salvage pathway; within-query FDR = 0.0022) (GO:BP nucleobase-containing small molecule metabolic process; q_global = 0.00817).
- **Conclusion**: MTAP closes the methionine salvage loop that the module couples to thioredoxin redox regulation.

#### AIMP1

- **Related proteins** (co-abundance neighbors): CAPN1 (0.90), TMX1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aminoacyl tRNA synthetase complex interacting multifunctional protein 1. The protein encoded by this gene is a cytokine that is specifically induced by apoptosis, and it is involved in the control of angiogenesis, inflammation, and wound healing. The release of this cytokine renders the tumor-associated vasculature sensitive to tumor necrosis factor. The precursor protein is identical to the p43 subunit, which is associated with the multi-tRNA synthetase complex, and i…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 3 (0.790); Pelizaeus-Merzbacher-like disease (0.657); POLR-related leukodystrophy (0.657); leukodystrophy (0.372); autosomal recessive non-syndromic intellectual disability (0.371)
- **Europe PMC papers**: 663
- **Why important**: AIMP1 is a component of the multi-aminoacyl-tRNA synthetase complex and is linked by Open Targets to hypomyelinating leukodystrophy and Pelizaeus-Merzbacher-like disease.
- **Conclusion**: AIMP1 connects the module to the GCN2-dependent integrated stress response and to heritable white matter disease; its role in the shared program is a hypothesis.

#### CAPN1

- **Related proteins** (co-abundance neighbors): AIMP1 (0.90), EIF2B5 (0.88), TXN (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calpain 1. The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpa…
- **Diseases (Open Targets)**: Autosomal recessive spastic paraplegia type 76 (0.781); Alzheimer disease (0.383); neurodegenerative disease (0.326); hereditary spastic paraplegia 11 (0.266); hereditary disease (0.193)
- **Europe PMC papers**: 1869
- **Why important**: CAPN1 encodes calpain-1, a calcium-activated intracellular cysteine protease, and is linked by Open Targets to autosomal recessive spastic paraplegia type 76.
- **Conclusion**: Its co-abundance with AIMP1 and EIF2B5 suggests that calpain-1 belongs to the same translational and proteostatic program, an association not previously reported.

#### EIF2B5

- **Related proteins** (co-abundance neighbors): CAPN1 (0.88), XPO7 (0.88), SCFD1 (0.88), CLIC4 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: huMAP3_10202.1, huMAP3_10287.1, huMAP3_11232.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 2B subunit epsilon. This gene encodes one of five subunits of eukaryotic translation initiation factor 2B (EIF2B), a GTP exchange factor for eukaryotic initiation factor 2 and an essential regulator for protein synthesis. Mutations in this gene and the genes encoding other EIF2B subunits have been associated with leukoencephalopathy with vanishing white matter. [provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: leukoencephalopathy with vanishing white matter (0.838); leukoencephalopathy with vanishing white matter 1 (0.743); leukoencephalopathy with vanishing white matter 5 (0.698); ovarioleukodystrophy (0.625); hereditary disease (0.496)
- **Europe PMC papers**: 699
- **Why important**: EIF2B5 encodes a subunit of the eIF2B guanine nucleotide exchange factor that controls protein synthesis, is linked by Open Targets to leukoencephalopathy with vanishing white matter, and is the module member found in the partial hu.MAP complexes (hu.MAP huMAP3_10202.1) (hu.MAP huMAP3_10287.1) (hu.MAP huMAP3_11232.1).
- **Conclusion**: EIF2B5 anchors the integrated stress response axis of the module and connects it to vanishing white matter disease.

## Module 9

**Tissue pair**: bone_marrow and liver  
**Genes (18)**: ANXA5, HSPA5, CAPZB, CAPZA2, CNN2, DPYSL2, GARS1, HSPA8, NIBAN2, PLIN3, PLOD2, PTBP1, PYGB, SEPTIN9, PHGDH, CCT8, TXNDC5, UFSP2

### Function

The strongest functional interpretation is a cellular protein-handling and cytoskeletal organization module, with a globally significant cadherin-binding signal (GO:MF cadherin binding; q_global = 0.0368). The (GO:MF cadherin binding; q_global = 0.0368) overlap includes CAPZB, CCT8, CNN2, HSPA5, HSPA8, NIBAN2, PLIN3, and SEPTIN9. Their annotations connect cadherin binding with actin filament regulation, cytoskeletal organization, protein folding, endoplasmic-reticulum homeostasis, vesicle trafficking, lipid-droplet biology, and RNA or protein processing. PLOD2 is the principal network hub and links many otherwise weakly connected module members, but it has no globally significant GO/KEGG annotation. The module therefore appears to combine cytoskeletal or adhesion-related processes with proteostasis and cellular stress functions rather than representing a single narrowly defined pathway. No KEGG term passed global correction, and (GO:MF cadherin binding; q_global = 0.0368) is the only globally corrected GO or KEGG term. The STRING cadherin-binding result (STRING Function Cadherin binding; within-query FDR = 0.0394) is concordant but supplementary, not independent global evidence.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. The HPA summary identifies a secreted subset, while most genes are intracellular or membrane-associated, including cytosolic, nuclear, actin-filament, lipid-droplet, and endoplasmic-reticulum proteins. Most genes have low tissue specificity, and the protein is detected for much of the module in both bone marrow and liver. Blood-cell specificity is generally low, although selected genes show enrichment or enhancement in monocytes, dendritic-cell populations, plasma cells, megakaryocytes, neutrophils, or other immune-related cell types. The HPA pattern therefore does not support a simple plasma-protein explanation, but a shared cellular composition or shared stress, adhesion, and intracellular-proteostasis state in the two tissues remains plausible. The STRING alimentary-canal tissue result (STRING TISSUES Alimentary canal; within-query FDR = 0.0224) is supplementary and should not be treated as a globally corrected tissue-specific conclusion.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF cadherin binding | 0.0368 | CAPZB, CCT8, CNN2, HSPA5, HSPA8, NIBAN2, PLIN3, SEPTIN9 |

### STRING and hu.MAP

The STRING evidence is concentrated in a small connected core. CAPZA2 and CAPZB have a very strong known association, and CCT8, HSPA5, HSPA8, TXNDC5, and PLIN3 form additional known relationships, including a strong HSPA5-HSPA8 association and an HSPA8-PLIN3 association. These relationships support real protein-folding, endoplasmic-reticulum, vesicle, and cytoskeletal biology, but most module pairs are not represented by high-confidence STRING links. hu.MAP identifies CAPZA2 and CAPZB together in several actin-capping or actin-regulatory complexes (hu.MAP huMAP3_02458.1) through (hu.MAP huMAP3_12900.1); the remaining complex members are mostly outside this module. Thus, the module contains a well-supported CAPZA2-CAPZB complex and a known chaperone-centered STRING core, while the broader co-abundance pattern extends beyond currently catalogued physical complexes.

**STRING interactions (score >= 0.7)**: 6 of 153 gene pairs: CAPZA2–CAPZB (0.999); CCT8–HSPA5 (0.701); CCT8–HSPA8 (0.905); HSPA5–HSPA8 (0.983); HSPA5–TXNDC5 (0.798); HSPA8–PLIN3 (0.967)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Alimentary canal (FDR = 0.0224, 13 genes); Function Cadherin binding (FDR = 0.0394, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02458.1 (CAPZA2, CAPZB; 2/10); huMAP3_06652.1 (CAPZA2, CAPZB; 2/14); huMAP3_08077.1 (CAPZA2, CAPZB; 2/16); huMAP3_10870.1 (CAPZA2, CAPZB; 2/20); huMAP3_12900.1 (CAPZA2, CAPZB; 2/50)

### Novelty

The module should not be declared a wholly new molecular complex or pathway. Several relationships and functions are already established by STRING and hu.MAP, especially the CAPZA2-CAPZB actin-capping pair and the HSPA5-HSPA8-centered chaperone relationships. Nevertheless, the cross-tissue co-abundance configuration may be a novel systems-level observation because the complete set is sparse, contains many genes without recorded STRING or hu.MAP relationships, and has no single globally corrected pathway annotation beyond cadherin binding (GO:MF cadherin binding; q_global = 0.0368). Absence from STRING or hu.MAP cannot establish novelty: it may reflect incomplete interaction coverage, indirect regulation, shared cell composition, or correlated cellular state. The defensible conclusion is possible novelty of the bone-marrow–liver co-abundance pattern, not proof of a new biochemical complex.

**Hypothesis.** Hypothesis: the conserved module reflects a shared cellular state involving adhesion-associated actin remodeling and proteostasis. In this model, CAPZA2 and CAPZB regulate actin-barbed-end dynamics, CNN2 and SEPTIN9 support actin or cytoskeletal organization, while HSPA5, HSPA8, CCT8, and TXNDC5 maintain folding and stress-handling capacity. PLOD2 could connect this state to extracellular-matrix collagen maturation and hypoxia-related cellular adaptation, while PLIN3 could connect vesicle and lipid-droplet handling to the same state. NIBAN2 and ANXA5 may reflect adhesion, membrane, or survival-related regulation. This is a mechanistic hypothesis, not a demonstrated causal pathway; the co-abundance data cannot determine whether these genes act in one cell type, in interacting cell populations, or merely respond to a shared tissue condition.

### Important genes

#### PLOD2

- **Related proteins** (co-abundance neighbors): HSPA8 (0.90), CAPZB (0.86), GARS1 (0.85), TXNDC5 (0.84), PYGB (0.83), PHGDH (0.83), PTBP1 (0.83), DPYSL2 (0.82), CCT8 (0.82), CAPZA2 (0.81), PLIN3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Not detected in immune cells; location Nucleoli, Cytosol; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: procollagen-lysine,2-oxoglutarate 5-dioxygenase 2. The protein encoded by this gene is a membrane-bound homodimeric enzyme that is localized to the cisternae of the rough endoplasmic reticulum. The enzyme (cofactors iron and ascorbate) catalyzes the hydroxylation of lysyl residues in collagen-like peptides. The resultant hydroxylysyl groups are attachment sites for carbohydrates in collagen and thus are critical for the stability of intermolecular…
- **Diseases (Open Targets)**: Bruck syndrome (0.779); osteogenesis imperfecta (0.572); osteoarthritis (0.552); osteoarthritis, hip (0.531); osteoarthritis, knee (0.472)
- **Europe PMC papers**: 3025
- **Why important**: PLOD2 is the central network hub, connecting many module members with relatively strong co-abundance links. Its established function is collagen-like peptide lysyl hydroxylation in the endoplasmic reticulum, supporting collagen crosslink stability and extracellular-matrix organization. It is detected in both bone marrow and liver, has low tissue specificity, is linked to hypoxia and collagen biology, and has extensive literature and disease associations including connective-tissue and skeletal disorders. It has no globally significant GO/KEGG annotation and no recorded STRING or hu.MAP partner in this module, so its hub status is based on the co-abundance network rather than known physical interactions.
- **Conclusion**: Established evidence supports PLOD2 as the module's co-abundance organizer and as a collagen-maturation enzyme. The hypothesis that it coordinates the other module processes through matrix, hypoxia, or endoplasmic-reticulum state is plausible but unproven.

#### HSPA5

- **Related proteins** (co-abundance neighbors): HSPA8 (0.84); STRING partners: CCT8 (0.701), HSPA8 (0.983), TXNDC5 (0.798)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is part of the globally significant cadherin-binding overlap (GO:MF cadherin binding; q_global = 0.0368) and the supplementary STRING terms (STRING TISSUES Alimentary canal; within-query FDR = 0.0224) and (STRING Function Cadherin binding; within-query FDR = 0.0394). It is an endoplasmic-reticulum HSP70 chaperone and master regulator of ER homeostasis, has strong known STRING relationships with HSPA8, CCT8, and TXNDC5, and is detected in both tissues. Its very extensive literature and disease associations make it a strong biological anchor for the proteostasis and stress component of the module.
- **Conclusion**: Established evidence supports HSPA5 as a known chaperone-centered component that links several module genes. It may report a shared unfolded-protein or secretory burden across bone marrow and liver, but the module does not establish that HSPA5 initiates or causes the broader co-abundance pattern.

#### HSPA8

- **Related proteins** (co-abundance neighbors): PLOD2 (0.90), HSPA5 (0.84); STRING partners: CCT8 (0.905), HSPA5 (0.983), PLIN3 (0.967)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Flagellar centriole, Annulus; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 8. This gene encodes a member of the heat shock protein 70 family, which contains both heat-inducible and constitutively expressed members. This protein belongs to the latter group, which are also referred to as heat-shock cognate proteins. It functions as a chaperone, and binds to nascent polypeptides to facilitate correct folding. It also functions as an ATPase in the disassembly of clathrin-coated…
- **Diseases (Open Targets)**: dengue disease (0.505); systemic lupus erythematosus (0.375); smoking initiation (0.199); Lennox-Gastaut syndrome (0.118); neoplasm (0.105)
- **Europe PMC papers**: 6937
- **Why important**: HSPA8 is included in (GO:MF cadherin binding; q_global = 0.0368), (STRING TISSUES Alimentary canal; within-query FDR = 0.0224), and (STRING Function Cadherin binding; within-query FDR = 0.0394), and has known STRING links with CCT8, HSPA5, and PLIN3. It is a constitutively expressed HSP70 chaperone involved in nascent-protein folding and clathrin-coated-vesicle disassembly. It is detected in both tissues, occupies the chaperone-centered part of the network, and has very extensive literature with disease associations.
- **Conclusion**: Established evidence supports HSPA8 as a broadly expressed proteostasis and membrane-trafficking component of the module. Its connectivity suggests coordination with HSPA5, CCT8, and PLIN3, but a specific bone-marrow–liver mechanism remains a hypothesis.

#### CAPZB

- **Related proteins** (co-abundance neighbors): PLOD2 (0.86); STRING partners: CAPZA2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: huMAP3_02458.1, huMAP3_06652.1, huMAP3_08077.1, huMAP3_10870.1, huMAP3_12900.1
- **Function (MyGene.info)**: capping actin protein of muscle Z-line subunit beta. This gene encodes the beta subunit of the barbed-end actin binding protein, which belongs to the F-actin capping protein family. The capping protein is a heterodimeric actin capping protein that blocks actin filament assembly and disassembly at the fast growing (barbed) filament ends and functions in regulating actin filament dynamics as well as in stabilizing actin filament lengths in muscle and …
- **Diseases (Open Targets)**: neurodegenerative disease (0.525); hypothyroidism (0.454); nontoxic goiter (0.440); multinodular goiter (0.428); thyrotoxicosis (0.414)
- **Europe PMC papers**: 1148
- **Why important**: CAPZB is in (GO:MF cadherin binding; q_global = 0.0368), (STRING TISSUES Alimentary canal; within-query FDR = 0.0224), and (STRING Function Cadherin binding; within-query FDR = 0.0394), is paired with CAPZA2 by a very strong STRING association, and occurs with CAPZA2 in every listed hu.MAP complex (hu.MAP huMAP3_02458.1) through (hu.MAP huMAP3_12900.1). Its established role is actin barbed-end capping and regulation of actin filament dynamics. It is detected in both tissues, has moderate literature coverage, and has disease associations including thyroid and neurological conditions.
- **Conclusion**: Established evidence supports CAPZB as the clearest actin-complex marker in the module. The hypothesis that the CAPZA2-CAPZB pair links cadherin-associated adhesion to the wider co-abundance state is consistent with (GO:MF cadherin binding; q_global = 0.0368) but is not demonstrated by the network alone.

#### NIBAN2

- **Related proteins** (co-abundance neighbors): SEPTIN9 (0.84), PYGB (0.84), ANXA5 (0.81), CNN2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: niban apoptosis regulator 2. Enables transcription coactivator activity. Involved in several processes, including gonadotropin secretion; positive regulation of transcription regulatory region DNA binding activity; and regulation of cellular macromolecule biosynthetic process. Located in several cellular components, including adherens junction; cytosol; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: asthma (0.281); prostate carcinoma (0.252); melanoma (0.081); neoplasm (0.080); osteoporosis (0.079)
- **Europe PMC papers**: 91
- **Why important**: NIBAN2 is in the globally significant cadherin-binding overlap (GO:MF cadherin binding; q_global = 0.0368) and supplementary STRING term (STRING Function Cadherin binding; within-query FDR = 0.0394). It is annotated in adherens-junction and transcriptional regulation processes, shows co-abundance links to SEPTIN9, PYGB, ANXA5, and CNN2, and has tissue or cell-type evidence involving esophageal apical cells and classical monocytes. Its literature volume is limited relative to the chaperones, making it a potentially informative but less established module component.
- **Conclusion**: Established evidence supports NIBAN2 as a cadherin-associated and regulatory gene that occupies the module's adhesion-linked branch. Its potential role as a bridge between adhesion, survival regulation, and immune-cell state is a hypothesis requiring independent functional validation.

## Module 10

**Tissue pair**: bone_marrow and liver  
**Genes (9)**: ANXA7, GFM1, GFUS, GBP1, NUDT6, OCIAD1, BCKDHA, PCYT2, TBC1D24

### Function

No GO or KEGG term passed global multiple-testing correction, and there was no supplementary STRING functional enrichment. The module therefore does not support a statistically established pathway-level function. Its gene content is heterogeneous: it includes mitochondrial translation, branched-chain amino-acid catabolism, phospholipid synthesis, GDP-fucose synthesis, interferon-inducible defense, membrane trafficking, and hematopoietic stem-cell or receptor-signaling annotations. The co-abundance pattern is consequently better described as a cross-tissue expression module than as a demonstrated biochemical pathway. TBC1D24 is the most connected hub in the module, while NUDT6 links several otherwise separate functional groupings. These network observations generate biological hypotheses but do not establish physical or functional interactions.

**Cell composition.** The module is not predominantly plasma or secreted: only a single member has a secretome annotation, and the remaining genes are intracellular or membrane-associated. It is also not blood-cell enriched according to HPA: the members have low immune-cell specificity or are not detected in immune cells, and no enriched blood-cell category is reported. Most proteins are detected in both bone marrow and liver, although GBP1 is not detected in either tissue in the HPA immunohistochemistry summary. Tissue specificity is mixed, with several broadly expressed genes and a smaller set showing liver, lymphoid-tissue, testis, or salivary-gland enhancement. Single-cell annotations are diverse, including neural, germ-cell, adipocyte, epithelial, stromal, and cardiac-associated cell types. Thus, the shared module is unlikely to be explained simply by a plasma-protein signal or a conventional blood-cell compartment; shared expression of broadly expressed intracellular genes, mixed cellular composition, or coordinated tissue-state effects remain plausible explanations.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction meets the stated high-confidence threshold, and no hu.MAP complex contains multiple module members. Therefore, the co-abundance edges are not corroborated here as established high-confidence protein-protein interactions or as membership in a known multi-member hu.MAP complex. The absence of STRING and hu.MAP support does not invalidate the co-abundance module: co-regulation, cell-composition effects, transient interactions, incomplete database coverage, or indirect relationships can produce coordinated abundance without a catalogued physical interaction. The available evidence supports a statistical expression relationship, not a demonstrated molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may represent a previously unrecognized co-abundance association because its members have no reported high-confidence STRING interactions with one another and no shared hu.MAP complex. However, those database absences alone do not prove novelty. Several members have well-established individual functions and substantial literature, while the module contains functionally disparate genes. The defensible conclusion is that the shared bone-marrow–liver co-abundance pattern is potentially novel as a module-level observation, but its biological novelty and mechanism require independent replication, control for cell composition and tissue state, and experimental validation.

**Hypothesis.** Hypothesis: the module reflects coordinated variation in a broadly expressed intracellular program that couples mitochondrial and metabolic capacity with membrane and phospholipid biology, while being modulated by interferon-related or tissue-state signals. TBC1D24 may act as a network-level connector between membrane trafficking-associated biology and the PCYT2, GFM1, and OCIAD1-associated expression pattern; NUDT6 may connect metabolic and defense-related genes. This is a hypothesis based on co-abundance and annotations, not evidence of direct molecular interaction. Testing should include cell-composition adjustment, replication in independent bone-marrow and liver cohorts, perturbation of candidate hubs, and measurement of mitochondrial translation, lipid synthesis, membrane trafficking, and interferon-response readouts.

### Important genes

#### TBC1D24

- **Related proteins** (co-abundance neighbors): ANXA7 (0.90), PCYT2 (0.84), GFM1 (0.81), OCIAD1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cell Junctions; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TBC1 domain family member 24. This gene encodes a protein with a conserved domain, referred to as the TBC domain, characteristic of proteins which interact with GTPases. TBC domain proteins may serve as GTPase-activating proteins for a particular group of GTPases, the Rab (Ras-related proteins in brain) small GTPases which are involved in the regulation of membrane trafficking. Mutations in this gene are associated with famili…
- **Diseases (Open Targets)**: DOORS syndrome (0.809); familial infantile myoclonic epilepsy (0.765); rolandic epilepsy-paroxysmal exercise-induced dystonia-writer's cramp syndrome (0.765); autosomal dominant nonsyndromic hearing loss 65 (0.736); autosomal recessive nonsyndromic hearing loss 86 (0.733)
- **Europe PMC papers**: 656
- **Why important**: TBC1D24 is the most connected gene in the module and links ANXA7, PCYT2, GFM1, and OCIAD1. Its TBC domain is associated with regulation of Rab small GTPases and membrane trafficking. HPA places it at the plasma membrane and cell junctions, with expression enhanced in several neural and renal cell types and absent from immune cells. It has strong disease relevance for familial infantile myoclonic epilepsy and related neurological or hearing disorders, and it has substantial literature.
- **Conclusion**: Established evidence supports TBC1D24 as the top network hub and as a membrane-trafficking-associated disease gene. It is a plausible module coordinator, but the module does not establish that it regulates the other members or that its neurological functions explain the bone-marrow–liver pattern.

#### NUDT6

- **Related proteins** (co-abundance neighbors): GFUS (0.85), GBP1 (0.82), BCKDHA (0.82), GFM1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nudix hydrolase 6. This gene overlaps and lies on the opposite strand from FGF2 gene, and is thought to be the FGF2 antisense gene. The two genes are independently transcribed, and their expression shows an inverse relationship, suggesting that this antisense transcript may regulate FGF2 expression. This gene has also been shown to have hormone-regulatory and antiproliferative actions in the pituitary that are indep…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.439); neurodegenerative disease (0.404); atrial fibrillation (0.399); type 2 diabetes mellitus (0.224); arthropathy (0.188)
- **Europe PMC papers**: 274
- **Why important**: NUDT6 has high connectivity and links GFUS, GBP1, BCKDHA, and GFM1, making it the principal bridge between otherwise distinct functional annotations. It is reported as an antisense-overlapping gene near FGF2 with possible hormone-regulatory and antiproliferative actions. HPA indicates low tissue specificity and enhanced expression in adipocytes and late primary spermatocytes. Its literature and disease associations are more limited than those of several other members, which makes its bridging position particularly informative.
- **Conclusion**: Established evidence supports NUDT6 as a central co-abundance connector, but its molecular role in this module is uncertain. A regulatory or transcript-level bridging function is a hypothesis that requires direct expression, perturbation, and molecular-interaction testing.

#### GFM1

- **Related proteins** (co-abundance neighbors): NUDT6 (0.81), TBC1D24 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G elongation factor mitochondrial 1. Eukaryotes contain two protein translational systems, one in the cytoplasm and one in the mitochondria. Mitochondrial translation is crucial for maintaining mitochondrial function and mutations in this system lead to a breakdown in the respiratory chain-oxidative phosphorylation system and to impaired maintenance of mitochondrial DNA. This gene encodes one of the mitochondrial translation elongati…
- **Diseases (Open Targets)**: hepatoencephalopathy due to combined oxidative phosphorylation defect type 1 (0.822); neurodegenerative disease (0.463); combined oxidative phosphorylation deficiency (0.451); hereditary disease (0.341); Leigh syndrome (0.313)
- **Europe PMC papers**: 1380
- **Why important**: GFM1 connects to NUDT6 and TBC1D24 and encodes a mitochondrial translation elongation factor. Its established function links it to mitochondrial protein synthesis, respiratory-chain maintenance, and oxidative-phosphorylation biology. HPA places it in mitochondria with low tissue specificity, and it has extensive literature and disease associations involving combined oxidative-phosphorylation defects and hepatoencephalopathy.
- **Conclusion**: Established evidence supports GFM1 as a mitochondrial translation gene with direct relevance to cellular energetic capacity. Its presence supports a metabolic component to the module, but no enrichment result or interaction evidence shows that mitochondrial translation is the module-wide function.

#### PCYT2

- **Related proteins** (co-abundance neighbors): TBC1D24 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphate cytidylyltransferase 2, ethanolamine. This gene encodes an enzyme that catalyzes the formation of CDP-ethanolamine from CTP and phosphoethanolamine in the Kennedy pathway of phospholipid synthesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010].
- **Diseases (Open Targets)**: spastic paraplegia 82, autosomal recessive (0.771); complex hereditary spastic paraplegia (0.554); neurodegenerative disease (0.542); Global developmental delay (0.462); Intellectual disability (0.462)
- **Europe PMC papers**: 4199
- **Why important**: PCYT2 is connected to the TBC1D24 hub and catalyzes a key step in the Kennedy pathway for phosphatidylethanolamine and phospholipid synthesis. It is liver- and testis-enhanced by HPA and has extensive literature, including associations with spastic paraplegia and neurodevelopmental disease. Its function provides a concrete membrane-lipid interpretation for part of the module.
- **Conclusion**: Established evidence supports PCYT2 as a phospholipid-biosynthesis enzyme and a biologically important module member. Its connection to TBC1D24 suggests a testable membrane-biology hypothesis, but does not establish a direct protein interaction or a shared pathway for all members.

#### GBP1

- **Related proteins** (co-abundance neighbors): NUDT6 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: guanylate binding protein 1. Guanylate binding protein expression is induced by interferon. Guanylate binding proteins are characterized by their ability to specifically bind guanine nucleotides (GMP, GDP, and GTP) and are distinguished from the GTP-binding proteins by the presence of 2 binding motifs rather than 3. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: bacterial infectious disease (0.528); Orthomyxoviridae infectious disease (0.374); neurodegenerative disease (0.302); muscular disease (0.195); neoplasm (0.116)
- **Europe PMC papers**: 3935
- **Why important**: GBP1 is connected to NUDT6 and is an interferon-inducible guanylate-binding protein involved in innate defense annotations, including responses to bacteria and protozoa. It is liver- and lymphoid-tissue-enhanced and has extensive literature. Unlike most members, it is not detected in the reported bone-marrow or liver immunohistochemistry results, so its inclusion may reflect transcript-level regulation, sensitivity differences, or a distinct tissue-state signal.
- **Conclusion**: Established evidence supports GBP1 as an immune-response-associated gene, but HPA does not support a simple immune-cell-composition explanation for the module. Its co-abundance with NUDT6 is compatible with an interferon or inflammatory state hypothesis, which requires independent testing.

#### OCIAD1

- **Related proteins** (co-abundance neighbors): TBC1D24 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OCIA domain containing 1. Predicted to be involved in several processes, including hematopoietic stem cell homeostasis; positive regulation of receptor signaling pathway via JAK-STAT; and regulation of stem cell differentiation. Located in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Alzheimer disease (0.101); maturity-onset diabetes of the young (0.080); breast carcinoma (0.070); primary familial polycythemia due to EPO receptor mutation (0.068); pyruvate kinase hyperactivity (0.067)
- **Europe PMC papers**: 246
- **Why important**: OCIAD1 is connected to TBC1D24 and is annotated to endocytosis, JAK-STAT receptor signaling, hematopoietic stem-cell homeostasis, and stem-cell differentiation. HPA places it in vesicles, reports low cell-type specificity, and detects it in both tissues. It has a smaller literature base than the best-studied genes, making its position beside the central hub useful for generating a focused mechanistic hypothesis.
- **Conclusion**: Established evidence supports OCIAD1 as a vesicle- and signaling-associated gene with relevance to hematopoietic homeostasis. Its network placement suggests a possible link between membrane trafficking and stem-cell or receptor signaling, but that link remains hypothetical in this module.

## Module 11

**Tissue pair**: bone_marrow and liver  
**Genes (21)**: AP3S1, COQ8A, CASK, DDX39B, EEA1, ELMOD2, GMPR2, ILK, LIMS1, MAT2A, NLRX1, NUP107, PAK2, PDLIM1, RNH1, POLR2B, SEC24C, SUPV3L1, SYNJ2BP, TFAM, UNC45A

### Function

This is a sparse, ELMOD2-centered co-abundance module with several plausible functional themes rather than a statistically established pathway. ELMOD2 has the strongest network position and connects genes involved in cytoskeletal signaling, vesicle trafficking, RNA processing, nucleocytoplasmic transport, mitochondrial biology, and cellular stress or antiviral responses. The adhesion-related component is supported by LIMS1 and ILK, while the mitochondrial component includes SUPV3L1, COQ8A, NLRX1, SYNJ2BP, and TFAM. PAK2, PDLIM1, and ILK provide a cytoskeletal and cell-matrix signaling context. However, no GO or KEGG term passed global correction, so these themes are functional interpretation of the gene annotations and network structure, not globally significant enrichment. STRING supplied no functional enrichment either. The module is therefore best described as a cross-compartment cellular maintenance and signaling pattern, potentially involving cytoskeletal adhesion, organelle homeostasis, intracellular trafficking, RNA handling, and stress-response regulation.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and the overall HPA profile is not strongly immune-cell specific. Thus, the shared signal is unlikely to be explained simply by a plasma-protein component or a broad blood-cell signature. Nevertheless, several genes show cell-type-enhanced expression in megakaryocytes or platelets, neutrophils, eosinophils, basophils, or B-cell populations, and some genes are detected in bone marrow or liver. This leaves open the possibility that shared cellular subpopulations, particularly hematopoietic or platelet-related cells, contribute to the co-abundance pattern. Other HPA signals point to skeletal muscle, esophageal, pancreatic, and neural cell types, indicating a heterogeneous and broadly distributed cellular program rather than a tissue-restricted liver or bone-marrow program. Protein detection in both tissues for several genes is compatible with a shared cellular process, but absence of detection for some genes in one tissue cautions against assuming that every member is active in the same cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known pairwise relationship is the STRING interaction between ILK and LIMS1. This agrees with their established integrin-associated adhesion biology and provides direct support for an adhesion submodule. hu.MAP independently places ILK and LIMS1 together in several complexes, with recurring partners including PXN, LIMS2, PARVG, PARVB, PARVA, RSU1, and in one complex additional trafficking-related proteins. This convergence indicates that the ILK-LIMS1 relationship is a known molecular association rather than a novel interaction inferred only from co-abundance. hu.MAP also places COQ8A and UNC45A together in a complex containing mitochondrial and protein-homeostasis-associated proteins, including PYCR1, OXA1L, TIMM50, GCDH, RNF5, AASS, and AFG3L2. Most other module relationships are absent from the supplied high-confidence STRING and hu.MAP results. Consequently, the network should not be interpreted as a fully validated physical complex. It is more consistent with a co-abundance network containing a known adhesion pair, a possible mitochondrial or proteostasis association, and additional relationships that may reflect shared regulation, cell composition, or indirect biology.

**STRING interactions (score >= 0.7)**: 1 of 210 gene pairs: ILK–LIMS1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06647.1 (LIMS1, ILK; 2/6); huMAP3_04827.1 (LIMS1, ILK; 2/7); huMAP3_09385.1 (LIMS1, ILK; 2/8); huMAP3_09247.1 (COQ8A, UNC45A; 2/9); huMAP3_11194.1 (LIMS1, ILK; 2/10)

### Novelty

The module should be considered a potentially interesting but unproven finding, not an established new biological module. The supplied evidence does not identify a previously reported module with this exact gene composition, tissue pairing, and network structure. At the same time, the presence of the well-established ILK-LIMS1 interaction and the known functions of many component genes argues against claiming that the underlying biology is wholly new. The sparse STRING network and limited hu.MAP overlap mean that much of the particular co-abundance arrangement is not already represented as a known molecular complex, but absence from these resources does not demonstrate novelty. A stronger novelty claim would require independent cohorts, replication across platforms, adjustment for cell composition, and comparison with published co-expression or proteomic modules.

**Hypothesis.** Hypothesis: the shared bone-marrow–liver pattern reflects coordinated variation in a broadly expressed cellular maintenance program that couples integrin-linked cytoskeletal signaling with mitochondrial quality control, intracellular trafficking, RNA handling, and antiviral or stress-response regulation. ELMOD2 may act as a network-level marker of this coordinated state, while the ILK-LIMS1 pair may represent an adhesion-associated branch and the COQ8A-associated genes a mitochondrial branch. In samples containing variable proportions of megakaryocytes, platelets, or other hematopoietic cells, part of the signal could instead arise from shared cell-type composition. This hypothesis predicts that the module will correlate with measures of adhesion and cytoskeletal state, mitochondrial function, intracellular transport, and cell-composition markers, but it does not establish direct biochemical coupling among all module members.

### Important genes

#### ELMOD2

- **Related proteins** (co-abundance neighbors): PAK2 (0.93), AP3S1 (0.86), DDX39B (0.86), LIMS1 (0.86), SUPV3L1 (0.85), SEC24C (0.84), NUP107 (0.83), POLR2B (0.83), TFAM (0.83), GMPR2 (0.82), UNC45A (0.81), RNH1 (0.81), MAT2A (0.81), PDLIM1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Actin filaments; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ELMO domain containing 2. This gene encodes one of six engulfment and motility (ELMO) domain-containing proteins. This gene is thought to play a role in antiviral responses. Mutations in this gene may be involved in the cause of familial idiopathic pulmonary fibrosis. [provided by RefSeq, Sep 2010].
- **Diseases (Open Targets)**: fungal infectious disease (0.255); glioblastoma (0.057); hyperlipoproteinemia type V (0.044); central nervous system cancer (0.044); glioma (0.044)
- **Europe PMC papers**: 219
- **Why important**: ELMOD2 is the central network gene, with the highest degree and weighted strength in the module. It connects PAK2, AP3S1, DDX39B, LIMS1, SUPV3L1, SEC24C, NUP107, POLR2B, and other members spanning cytoskeletal signaling, vesicle trafficking, RNA processing, nuclear transport, and mitochondrial biology. Its annotation includes a possible role in antiviral responses and familial idiopathic pulmonary fibrosis, while its literature volume is more limited than that of several established pathway genes. Its central position makes it the most informative candidate for testing whether the module represents coordinated regulation or merely indirect co-abundance.
- **Conclusion**: Established evidence supports ELMOD2 as the network hub and supports possible roles in antiviral defense. It is not established that ELMOD2 mechanistically organizes the other module branches. The most appropriate conclusion is that ELMOD2 is a strong module marker and a plausible regulatory candidate, requiring perturbation or independent molecular evidence before being assigned a causal role.

#### LIMS1

- **Related proteins** (co-abundance neighbors): ELMOD2 (0.86); STRING partners: ILK (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: huMAP3_06647.1, huMAP3_04827.1, huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: LIM zinc finger domain containing 1. The protein encoded by this gene is an adaptor protein which contains five LIM domains, or double zinc fingers. The protein is likely involved in integrin signaling through its LIM domain-mediated interaction with integrin-linked kinase, found in focal adhesion plaques. It is also thought to act as a bridge linking integrin-linked kinase to NCK adaptor protein 2, which is involved in growth factor…
- **Diseases (Open Targets)**: placental abruption (0.297); poisoning (0.245); stroke disorder (0.211); alcohol drinking (0.211); Hirsutism (0.181)
- **Europe PMC papers**: 739
- **Why important**: LIMS1 is directly connected to ILK in STRING with very high confidence and occurs with ILK in several hu.MAP complexes. Its annotation supports integrin signaling, cell-matrix adhesion, cell-cell junction organization, and linkage to NCK adaptor signaling. HPA identifies enhancement in megakaryocytes, monocytes, and platelets, and protein is detected in both relevant tissues. Its network degree within this sparse module is limited, but its relationship with ILK is the clearest supported molecular interaction in the module.
- **Conclusion**: Established evidence supports LIMS1 as a member of an integrin-associated adhesion complex and as part of a platelet- or megakaryocyte-relevant cellular context. The module does not establish that LIMS1 drives the cross-tissue pattern or links adhesion directly to mitochondrial and RNA-processing genes. Its strongest interpretation is as an anchor of the known adhesion branch.

#### ILK

- **Related proteins** (co-abundance neighbors): CASK (0.82); STRING partners: LIMS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_06647.1, huMAP3_04827.1, huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: integrin linked kinase. This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastas…
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); familial hypertrophic cardiomyopathy (0.194); Abnormality of the cardiovascular system (0.148); Prolonged QT interval (0.118); neoplasm (0.118)
- **Europe PMC papers**: 8401
- **Why important**: ILK forms the module's best-supported known interaction with LIMS1 and recurs with LIMS1 across several hu.MAP complexes. Its established annotation links it to beta-integrin signaling, cell-matrix adhesion, cell morphogenesis, and mitotic spindle organization. HPA places it at focal adhesion sites and shows enhancement in megakaryocytes, platelets, and smooth muscle cells. Its large literature base and disease associations involving cardiovascular and neoplastic phenotypes make it a biologically interpretable representative of the adhesion and cytoskeletal branch.
- **Conclusion**: Established evidence supports ILK as an integrin-associated signaling and adhesion protein participating in a known LIMS1-centered complex. The co-abundance data support its membership in an adhesion-related module but do not show that ILK activity explains the entire module. Any proposed connection from ILK to mitochondrial or antiviral processes remains hypothetical.

#### COQ8A

- **Related proteins** (co-abundance neighbors): SUPV3L1 (0.89), SYNJ2BP (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09247.1
- **Function (MyGene.info)**: coenzyme Q8A. This gene encodes a mitochondrial protein similar to yeast ABC1, which functions in an electron-transferring membrane protein complex in the respiratory chain. It is not related to the family of ABC transporter proteins. Expression of this gene is induced by the tumor suppressor p53 and in response to DNA damage, and inhibiting its expression partially suppresses p53-induced apoptosis. Alternative…
- **Diseases (Open Targets)**: autosomal recessive ataxia due to ubiquinone deficiency (0.841); coenzyme Q10 deficiency (0.636); coenzyme Q10 deficiency, primary, 1 (0.461); hereditary disease (0.401); Abnormality of the skeletal system (0.366)
- **Europe PMC papers**: 397
- **Why important**: COQ8A provides a distinct mitochondrial and metabolic signal within the module. It is linked to ubiquinone biosynthesis and mitochondrial respiratory-chain biology, has a hu.MAP association with UNC45A, and is associated with autosomal recessive ataxia due to ubiquinone deficiency and coenzyme Q deficiency. HPA reports tissue enrichment in skeletal muscle and tongue and several neural cell-type enhancements. Its network position is peripheral, but its function is mechanistically specific and offers a testable explanation for the mitochondrial branch.
- **Conclusion**: Established evidence supports COQ8A as a mitochondrial coenzyme-Q-related protein with disease relevance. Its presence does not prove that the complete module is a respiratory-chain or coenzyme-Q module, especially because global GO and KEGG enrichment was absent. It is best regarded as a biologically informative branch marker and a candidate for testing mitochondrial involvement.

#### PAK2

- **Related proteins** (co-abundance neighbors): ELMOD2 (0.93), CASK (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: p21 (RAC1) activated kinase 2. The p21 activated kinases (PAK) are critical effectors that link Rho GTPases to cytoskeleton reorganization and nuclear signaling. The PAK proteins are a family of serine/threonine kinases that serve as targets for the small GTP binding proteins, CDC42 and RAC1, and have been implicated in a wide range of biological activities. The protein encoded by this gene is activated by proteolytic cleavage …
- **Diseases (Open Targets)**: Knobloch syndrome 2 (0.525); Knobloch syndrome (0.454); HIV infectious disease (0.370); atrial fibrillation (0.210); ovarian carcinoma (0.175)
- **Europe PMC papers**: 3704
- **Why important**: PAK2 connects the central ELMOD2 neighborhood with CASK and represents a signaling link between small-GTPase-regulated cytoskeletal reorganization and nuclear signaling. Its annotation includes protein phosphorylation, cell migration, signal transduction, starvation response, and apoptosis-related activation. HPA shows cell-type enhancement in neutrophils, and PAK2 has substantial literature and disease-related evidence. Although its network degree is modest, its function provides a plausible bridge between cytoskeletal state, migration, and cellular stress.
- **Conclusion**: Established evidence supports PAK2 as a Rho-family effector involved in cytoskeletal signaling, migration, and apoptosis-related processes. The module supports an association of PAK2 abundance with ELMOD2 and CASK, but not a direct pathway connecting PAK2 to every other module member. Its role in the proposed cross-compartment mechanism remains a hypothesis.

## Module 12

**Tissue pair**: bone_marrow and liver  
**Genes (12)**: DMAC2L, CPPED1, IMPA1, MOGS, POR, PEPD, PHB2, MRPL11, RRAS2, SSR1, THOP1, TRAP1

### Function

This is a coordinated cellular-maintenance module rather than a statistically established pathway module. No GO or KEGG term passed global correction, so no GO or KEGG enrichment can be claimed as primary evidence. The genes collectively point toward linked mitochondrial energy maintenance, protein folding and quality control, endoplasmic-reticulum processing, intracellular peptide and amino-acid metabolism, lipid and xenobiotic handling, and signal transduction. DMAC2L is the network hub, while the remaining genes form a hub-and-spoke co-abundance pattern. This topology supports coordinated regulation or shared cellular-state dependence, but it does not by itself demonstrate direct molecular interactions or a single biochemical pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: HPA reports no secreted genes. Most genes have low tissue specificity, and HPA protein detection is generally present in both bone marrow and liver, which is consistent with broadly expressed intracellular machinery rather than a liver-specific secretory program. Several genes show cell-type-enhanced expression in hepatocytes, enterocytes, neutrophils, reproductive cells, or other cell types, indicating a heterogeneous cellular contribution. Blood-cell specificity is generally low, with only limited immune-cell enhancement, including neutrophil and memory B-cell signals. The shared module could therefore reflect conserved intracellular programs across sampled cells, but shared cell-type composition or varying cellular mixtures in bone marrow and liver remain plausible explanations.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There is no high-confidence STRING interaction among the module genes and no STRING functional enrichment. No hu.MAP complex contains multiple module members. Thus, the observed co-abundance relationships are not supported here as previously catalogued physical protein interactions or as membership in a known multiprotein complex. The absence of STRING and hu.MAP support argues against interpreting the module as a validated physical complex, while still allowing coordinated transcription, common cell-state regulation, indirect pathway coupling, or context-dependent interactions.

**STRING interactions (score >= 0.7)**: 0 of 66 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module appears potentially novel as a tissue-pair co-abundance pattern because its internal relationships are not represented by high-confidence STRING interactions or a shared hu.MAP complex, and no established enrichment signal supports a known pathway-level annotation. However, this is not proof of a new biological mechanism. Database coverage, context dependence, modest effect sizes, shared cellular composition, and indirect regulation can all produce a co-abundance module without known physical interactions. The defensible conclusion is that this is a potentially novel expression-level association requiring replication and experimental validation, not an established new complex or pathway.

**Hypothesis.** Hypothesis: a conserved intracellular stress and metabolic-state program links mitochondrial energy handling with ER proteostasis and intermediary metabolism in cells represented in both bone marrow and liver. DMAC2L may mark the shared cellular state, while TRAP1, PHB2, and MRPL11 represent mitochondrial chaperoning, mitochondrial membrane organization, and mitochondrial translation; SSR1 and MOGS represent ER translocation and N-linked glycan processing; and PEPD, POR, THOP1, and IMPA1 connect peptide, xenobiotic, amino-acid, lipid, and signaling metabolism. The module may therefore arise when cells coordinate energy production, protein processing, peptide turnover, and stress adaptation. This remains a mechanistic hypothesis because the enrichment, STRING, and complex evidence do not establish causality or direct binding.

### Important genes

#### DMAC2L

- **Related proteins** (co-abundance neighbors): TRAP1 (0.92), PEPD (0.89), POR (0.88), THOP1 (0.85), SSR1 (0.84), MOGS (0.83), MRPL11 (0.82), IMPA1 (0.81), PHB2 (0.81), CPPED1 (0.81), RRAS2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: distal membrane arm assembly component 2 like. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. This gene en…
- **Diseases (Open Targets)**: L-2-hydroxyglutaric aciduria (0.446); hereditary disease (0.399); congenital ptosis (0.086); cataract (0.073); Duane retraction syndrome (0.071)
- **Europe PMC papers**: 37
- **Why important**: DMAC2L is the central hub of the module, connected to every other member in the supplied co-abundance subgraph and having the greatest weighted network strength. Its annotated role as a mitochondrial ATP-synthase subunit places it at the intersection of proton-gradient use and oxidative phosphorylation. Despite limited literature volume and no STRING or hu.MAP support, its network position makes it the most informative marker of the module's shared state.
- **Conclusion**: Established evidence supports DMAC2L as a mitochondrial ATP-synthase component and the module's expression hub. Hypothesis: DMAC2L may act as a readout, or possibly a contributor, to coordinated mitochondrial and proteostasis-related regulation. Its causal importance is unproven and should not be inferred solely from hub status.

#### POR

- **Related proteins** (co-abundance neighbors): DMAC2L (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome p450 oxidoreductase. This gene encodes an endoplasmic reticulum membrane oxidoreductase that is essential for multiple metabolic processes, including reactions catalyzed by cytochrome P450 proteins for metabolism of steroid hormones, drugs and xenobiotics. The encoded protein has a flavin adenine dinucleotide (FAD)-binding domain and a flavodoxin-like domain which bind two cofactors, FAD and FMN, that allow it to dona…
- **Diseases (Open Targets)**: congenital adrenal hyperplasia due to cytochrome P450 oxidoreductase deficiency (0.834); Antley-Bixler syndrome with genital anomalies and disordered steroidogenesis (0.810); congenital adrenal hyperplasia (0.534); coffee consumption (0.446); Antley-Bixler syndrome without genital anomalies or disordered steroidogenesis (0.444)
- **Europe PMC papers**: 28661
- **Why important**: POR is a liver-enhanced gene with cell-type enhancement in hepatocytes, enterocytes, and neutrophils, and it is detected at the protein level in both tissues. Its established function is electron transfer from NADPH to microsomal cytochrome P450 enzymes, linking the module to steroid, drug, xenobiotic, fatty-acid, and nutrient-related metabolism. It also has substantial literature and disease annotation, making it a biologically interpretable anchor despite its peripheral network position.
- **Conclusion**: Established evidence supports POR as an ER-associated oxidoreductase central to microsomal metabolism. Hypothesis: POR may couple the module to hepatic metabolic load or redox state, but the co-abundance data do not establish that POR drives the module or that all module members participate in P450 metabolism.

#### PEPD

- **Related proteins** (co-abundance neighbors): DMAC2L (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peptidase D. This gene encodes a member of the peptidase family. The protein forms a homodimer that hydrolyzes dipeptides or tripeptides with C-terminal proline or hydroxyproline residues. The enzyme serves an important role in the recycling of proline, and may be rate limiting for the production of collagen. Mutations in this gene result in prolidase deficiency, which is characterized by the excretion of larg…
- **Diseases (Open Targets)**: prolidase deficiency (0.822); type 2 diabetes mellitus (0.425); Abnormality of the skeletal system (0.411); diabetes mellitus (0.409); obesity disorder (0.354)
- **Europe PMC papers**: 1500
- **Why important**: PEPD is tissue-enhanced in intestine and kidney and cell-type-enhanced in enterocytes, hepatocytes, Hofbauer cells, and proximal tubule cells, with protein detected in both tissues. Its enzyme function in hydrolyzing proline- and hydroxyproline-containing peptides links it to peptide recycling and collagen-related proline availability. Its disease association with prolidase deficiency and substantial literature provide stronger functional support than the module-level enrichment results.
- **Conclusion**: Established evidence supports PEPD as a proline-related peptidase involved in peptide and amino-acid metabolism. Hypothesis: PEPD may connect intracellular peptide turnover with the energetic and matrix-related demands of cells contributing to the shared module. A direct relationship to the other module genes remains unestablished.

#### TRAP1

- **Related proteins** (co-abundance neighbors): DMAC2L (0.92); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TNF receptor associated protein 1. This gene encodes a mitochondrial chaperone protein that is member of the heat shock protein 90 (HSP90) family. The encoded protein has ATPase activity and interacts with tumor necrosis factor type I. This protein may function in regulating cellular stress responses. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jan 2013].
- **Diseases (Open Targets)**: congenital anomaly of kidney and urinary tract (0.643); VACTERL/vater association (0.492); atrial fibrillation (0.467); neurodegenerative disease (0.372); Blindness (0.338)
- **Europe PMC papers**: 2586
- **Why important**: TRAP1 is a mitochondrial HSP ninety-family chaperone with documented roles in protein folding, cellular stress responses, respiratory regulation, reactive-oxygen control, and protection from intrinsic apoptotic signaling in response to oxidative stress. It is detected in both tissues and has the largest literature volume among the selected genes. Its direct module connection is limited to DMAC2L, but its function provides a strong mechanistic bridge between mitochondrial state and proteostasis.
- **Conclusion**: Established evidence supports TRAP1 as a mitochondrial stress-response and chaperone protein. Hypothesis: TRAP1 may help explain why mitochondrial energy genes and ER or metabolic genes co-vary across samples by reflecting a shared proteotoxic or oxidative-stress state. The module does not demonstrate a direct TRAP1 interaction with the other genes.

#### SSR1

- **Related proteins** (co-abundance neighbors): DMAC2L (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal sequence receptor subunit 1. The signal sequence receptor (SSR) is a glycosylated endoplasmic reticulum (ER) membrane receptor associated with protein translocation across the ER membrane. The SSR consists of 2 subunits, a 34-kD glycoprotein encoded by this gene and a 22-kD glycoprotein. This gene generates several mRNA species as a result of complex alternative polyadenylation. This gene is unusual in that it utilizes arrays…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.470); diabetes mellitus (0.344); neurodegenerative disease (0.329); Inguinal hernia (0.322); refractive error (0.315)
- **Europe PMC papers**: 938
- **Why important**: SSR1 is an ER membrane component of the signal sequence receptor, involved in cotranslational protein targeting and translocation into the ER. It is broadly tissue-specific, detected in liver, and represented in the module as a peripheral partner of DMAC2L. Its function complements the mitochondrial genes by introducing protein-entry and ER-processing biology into the module's interpretation.
- **Conclusion**: Established evidence supports SSR1 as an ER protein-translocation component. Hypothesis: SSR1 may indicate that the shared cellular state involves coordinated mitochondrial capacity and secretory-pathway protein handling, even though the module contains no secreted proteins. Its absence from bone-marrow protein detection and lack of known database interactions make this interpretation provisional.
