# Conserved co-abundance modules: brain and ovary

## Module 0

**Tissue pair**: brain and ovary  
**Genes (15)**: SLC3A2, SLC1A5, ACSL3, ATP1B3, MTHFD1L, HSD17B4, GALNT2, GOLIM4, ALDH18A1, RRBP1, SEC22B, HM13, SSR1, STX7, TFRC

### Function

The best-supported interpretation is a membrane-organelle module linking amino-acid transport, iron uptake, intracellular trafficking, and metabolic support. The primary evidence is enrichment for melanosome and pigment-granule components (GO:CC melanosome; q_global = 0.00238) (GO:CC pigment granule; q_global = 0.00238), broad organelle-membrane localization (GO:CC organelle membrane; q_global = 0.0304), and protein digestion and absorption (KEGG Protein digestion and absorption - Homo sapiens (human); q_global = 0.0486). The amino-acid transporter pair SLC1A5 and SLC3A2, together with TFRC, supports nutrient and iron acquisition. SEC22B and STX7 support vesicle trafficking, while GALNT2, RRBP1, SSR1, GOLIM4, and HM13 support ER-Golgi processing and membrane-protein maturation. The ferroptosis and membrane findings (STRING WikiPathways Ferroptosis; within-query FDR = 0.0047) (STRING KEGG Ferroptosis; within-query FDR = 0.0189) are supplementary rather than globally corrected primary evidence. Overall, the module is more consistent with coordinated membrane trafficking and nutrient-handling capacity than with a single narrowly defined biochemical pathway.

**Cell composition.** This is not primarily a soluble plasma-protein module: most members are membrane, ER, Golgi, lysosomal, mitochondrial, or peroxisomal proteins, and only a minority are classified as secreted. However, composition is compatible with shared cellular sources rather than a strictly brain-neuron or ovary-specific program. HPA reports low tissue specificity for most genes, with tissue enhancement distributed across several organs. Many members are cell-type enhanced, including microglia, neutrophils, monocytes, trophoblasts, epithelial or secretory cells, and melanocytes. Several genes have immune-cell enhancement, although most have low immune-cell specificity. TFRC is secreted to blood and is detected in both brain and ovary, while protein detection is more consistently observed in brain than ovary across the module. The shared signal could therefore reflect common membrane-rich cell populations, vascular or immune contributions, or sample composition; the pigment-granule signal should not by itself be interpreted as evidence of a dedicated melanocyte program.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC melanosome | 0.00238 | ATP1B3, SEC22B, SLC1A5, SLC3A2, TFRC |
| GO:CC pigment granule | 0.00238 | ATP1B3, SEC22B, SLC1A5, SLC3A2, TFRC |
| GO:CC organelle membrane | 0.0304 | ACSL3, ALDH18A1, GALNT2, GOLIM4, HM13, HSD17B4, RRBP1, SEC22B, SLC3A2, SSR1, STX7, TFRC |
| KEGG Protein digestion and absorption - Homo sapiens (human) | 0.0486 | ATP1B3, SLC1A5, SLC3A2 |

### STRING and hu.MAP

STRING provides strong direct support for only two within-module relationships: SEC22B with STX7 and SLC1A5 with SLC3A2. These relationships are biologically coherent with vesicle fusion and amino-acid transport, respectively, but the sparse direct interaction structure means that most co-abundance edges are not established physical interactions. hu.MAP gives partial support for several complexes. SLC3A2 and SSR1 occur together in a high-confidence complex (hu.MAP huMAP3_12263.1). ACSL3 and HM13 co-occur in membrane and lipid-related complexes (hu.MAP huMAP3_08167.1) (hu.MAP huMAP3_09592.1). ALDH18A1 and MTHFD1L co-occur in mitochondrial metabolic complexes (hu.MAP huMAP3_10525.1) (hu.MAP huMAP3_13468.1). GOLIM4 and TFRC co-occur in a broader membrane-associated complex (hu.MAP huMAP3_10725.1). Because each complex generally contributes only a small subset of its members to this module, hu.MAP supports compatible local machinery but not a single complete complex. Together, STRING and hu.MAP suggest a real mixture of transporter, trafficking, membrane-proteolysis, lipid, and mitochondrial-metabolic relationships rather than a densely interconnected canonical complex.

**STRING interactions (score >= 0.7)**: 2 of 105 gene pairs: SEC22B–STX7 (0.962); SLC1A5–SLC3A2 (0.894)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Signal-anchor (FDR = 2.8e-05, 6 genes); Keyword Transmembrane helix (FDR = 2.8e-05, 11 genes); Component Integral component of membrane (FDR = 0.00013, 12 genes); Component Melanosome (FDR = 0.00049, 5 genes); Component Organelle membrane (FDR = 0.0031, 12 genes); WikiPathways Ferroptosis (FDR = 0.0047, 4 genes); Keyword Membrane (FDR = 0.0072, 12 genes); Component Membrane (FDR = 0.0073, 15 genes); COMPARTMENTS Membrane (FDR = 0.0101, 13 genes); Process Import into cell (FDR = 0.015, 4 genes); KEGG Ferroptosis (FDR = 0.0189, 3 genes); KEGG Protein digestion and absorption (FDR = 0.0189, 3 genes); Component Basal plasma membrane (FDR = 0.0263, 4 genes); COMPARTMENTS Organelle membrane (FDR = 0.0282, 10 genes); Keyword Glycoprotein (FDR = 0.0292, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12263.1 (SLC3A2, SSR1; 2/2); huMAP3_08167.1 (ACSL3, HM13; 2/24); huMAP3_10525.1 (ALDH18A1, MTHFD1L; 2/33); huMAP3_10725.1 (GOLIM4, TFRC; 2/59); huMAP3_09592.1 (ACSL3, HM13; 2/95); huMAP3_13468.1 (ALDH18A1, MTHFD1L; 2/99)

### Novelty

This module may be a new cross-tissue co-abundance configuration, but the evidence does not establish novelty in the strong sense. The module combines known functions and several known relationships, especially the SLC1A5-SLC3A2 transporter pair, the SEC22B-STX7 trafficking relationship, and partial hu.MAP complex memberships. Its potentially novel aspect is the coordinated occurrence of these processes in a conserved brain-ovary module. Absence of a matching STRING or hu.MAP entity would not prove discovery, because those resources describe physical interactions or complexes rather than every tissue-specific co-abundance pattern. Demonstrating novelty would require comparison with published co-expression modules, independent cohorts, cell-composition estimates, and experimental validation in both tissues.

**Hypothesis.** Hypothesis: the module represents a shared membrane and organelle homeostasis program that couples amino-acid import through SLC1A5-SLC3A2 with iron uptake through TFRC, ER-Golgi cargo handling through SSR1, RRBP1, GALNT2, GOLIM4, and SEC22B, endolysosomal trafficking through STX7, and supporting lipid or mitochondrial metabolism through ACSL3, HSD17B4, ALDH18A1, and MTHFD1L. In brain and ovary, this program may be activated in metabolically active, secretory, vascular, or immune-associated cells and may contribute to pigment-granule or lysosome-related organelle biology. The observed module could therefore reflect a conserved cellular state or shared cell-type mixture rather than a tissue-specific pathway. This remains a hypothesis because the enrichment and network data do not demonstrate causality, cell identity, or direction of regulation.

### Important genes

#### SLC1A5

- **Related proteins** (co-abundance neighbors): ALDH18A1 (0.89), SSR1 (0.89), MTHFD1L (0.87), STX7 (0.86), TFRC (0.84), SEC22B (0.83), GOLIM4 (0.80); STRING partners: SLC3A2 (0.894)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 1 member 5. The SLC1A5 gene encodes a sodium-dependent neutral amino acid transporter that can act as a receptor for RD114/type D retrovirus (Larriba et al., 2001 [PubMed 11781704]).[supplied by OMIM, Jan 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.463); substance abuse (0.231); attention deficit-hyperactivity disorder (0.231); autoimmune disorder of central nervous system (0.213); hypotensive disorder (0.188)
- **Europe PMC papers**: 5038
- **Why important**: SLC1A5 is the most central node by module connectivity and links several metabolic, trafficking, and membrane-associated members. It is a sodium-dependent neutral amino-acid transporter with roles in glutamine and other amino-acid transport. It is present in the globally significant melanosome, pigment-granule, and protein-digestion-and-absorption terms (GO:CC melanosome; q_global = 0.00238) (GO:CC pigment granule; q_global = 0.00238) (KEGG Protein digestion and absorption - Homo sapiens (human); q_global = 0.0486), and it forms the strongest STRING-supported transporter relationship with SLC3A2. It also has extensive literature and disease associations involving neurological and immune-related disorders.
- **Conclusion**: Established evidence supports SLC1A5 as a central amino-acid transport component and a principal structural bridge within the module. It is plausible, but not established, that its transport activity helps couple nutrient availability to the other membrane and organelle processes.

#### SLC3A2

- **Related proteins** (co-abundance neighbors): HSD17B4 (0.85), GALNT2 (0.83); STRING partners: SLC1A5 (0.894)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_12263.1
- **Function (MyGene.info)**: solute carrier family 3 member 2. This gene is a member of the solute carrier family and encodes a cell surface, transmembrane protein. The protein exists as the heavy chain of a heterodimer, covalently bound through di-sulfide bonds to one of several possible light chains. The encoded transporter plays a role in regulation of intracellular calcium levels and transports L-type amino acids. Alternatively spliced transcript variants…
- **Diseases (Open Targets)**: sensorineural hearing loss disorder (0.370); neurodegenerative disease (0.324); neoplasm (0.117); breast cancer (0.113); breast carcinoma (0.110)
- **Europe PMC papers**: 6815
- **Why important**: SLC3A2 is a membrane amino-acid transporter heavy chain and the partner of SLC1A5 in the strongest direct STRING relationship. It appears in every globally significant primary term (GO:CC melanosome; q_global = 0.00238) (GO:CC pigment granule; q_global = 0.00238) (GO:CC organelle membrane; q_global = 0.0304) (KEGG Protein digestion and absorption - Homo sapiens (human); q_global = 0.0486), occurs with SSR1 in a high-confidence hu.MAP complex (hu.MAP huMAP3_12263.1), and has extensive literature. Its position connects nutrient transport to membrane and organelle biology.
- **Conclusion**: Established evidence identifies SLC3A2 as a core transporter and one of the strongest anchors of the module. A coordinated SLC1A5-SLC3A2 transport unit is well supported, whereas its proposed connection to pigment-granule biology is an interpretation of the enrichment context rather than a demonstrated mechanism.

#### TFRC

- **Related proteins** (co-abundance neighbors): ALDH18A1 (0.86), SLC1A5 (0.84), HM13 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes, Lysosomes; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_10725.1
- **Function (MyGene.info)**: transferrin receptor. This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: TFRC-related combined immunodeficiency (0.623); type 2 diabetes mellitus (0.518); mucopolysaccharidosis type 2 (0.490); diabetes mellitus (0.471); diabetic retinopathy (0.343)
- **Europe PMC papers**: 14164
- **Why important**: TFRC is a prominent module node linking SLC1A5 and ALDH18A1 and is included in the primary melanosome, pigment-granule, and organelle-membrane terms (GO:CC melanosome; q_global = 0.00238) (GO:CC pigment granule; q_global = 0.00238) (GO:CC organelle membrane; q_global = 0.0304). It encodes the transferrin receptor required for receptor-mediated cellular iron uptake and is detected in both tissues. HPA also shows associations with erythrocyte progenitors, macrophages, and monocytes, making it especially informative for interpreting possible blood or immune-cell contributions. It has the largest literature volume among the selected genes and substantial disease annotation.
- **Conclusion**: Established evidence supports TFRC as an iron-uptake and endocytic component of the module. Its immune and blood-cell associations mean that TFRC may also mark cellular composition in the samples. A role in linking iron handling to ferroptosis-related biology is plausible from the supplementary STRING evidence (STRING WikiPathways Ferroptosis; within-query FDR = 0.0047) (STRING KEGG Ferroptosis; within-query FDR = 0.0189), but is not primary globally corrected evidence.

#### ALDH18A1

- **Related proteins** (co-abundance neighbors): SLC1A5 (0.89), TFRC (0.86), HM13 (0.82), MTHFD1L (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_10525.1, huMAP3_13468.1
- **Function (MyGene.info)**: aldehyde dehydrogenase 18 family member A1. This gene is a member of the aldehyde dehydrogenase family and encodes a bifunctional ATP- and NADPH-dependent mitochondrial enzyme with both gamma-glutamyl kinase and gamma-glutamyl phosphate reductase activities. The encoded protein catalyzes the reduction of glutamate to delta1-pyrroline-5-carboxylate, a critical step in the de novo biosynthesis of proline, ornithine and arginine. Mutations in …
- **Diseases (Open Targets)**: ALDH18A1-related de Barsy syndrome (0.832); cutis laxa, autosomal dominant 3 (0.816); autosomal recessive complex spastic paraplegia type 9B (0.814); de Barsy syndrome (0.731); autosomal dominant spastic paraplegia type 9 (0.706)
- **Europe PMC papers**: 1168
- **Why important**: ALDH18A1 is a relatively highly connected metabolic bridge between SLC1A5, TFRC, HM13, and MTHFD1L. It encodes a mitochondrial enzyme in proline, ornithine, and arginine biosynthesis and is supported by the organelle-membrane term (GO:CC organelle membrane; q_global = 0.0304). Its membership in two hu.MAP mitochondrial metabolic complexes (hu.MAP huMAP3_10525.1) (hu.MAP huMAP3_13468.1) provides independent structural context, and it has well-established disease associations including de Barsy syndrome and spastic-paraplegia-related disorders.
- **Conclusion**: Established evidence supports ALDH18A1 as a mitochondrial amino-acid and nitrogen-metabolism component that connects the module to biosynthetic metabolism. It is reasonable to hypothesize that it supplies metabolic support for the transporter-rich state, but the co-abundance data do not show a direct biochemical interaction with the transporters.

#### SEC22B

- **Related proteins** (co-abundance neighbors): SLC1A5 (0.83), ACSL3 (0.81); STRING partners: STX7 (0.962)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC22 homolog B, vesicle trafficking protein. The protein encoded by this gene is a member of the SEC22 family of vesicle trafficking proteins. It seems to complex with SNARE and it is thought to play a role in the ER-Golgi protein trafficking. This protein has strong similarity to Mus musculus and Cricetulus griseus proteins.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: inflammatory bowel disease (0.285); luminal A breast carcinoma (0.271); colitis (0.238); enteritis (0.238); Crohn disease (0.233)
- **Europe PMC papers**: 1006
- **Why important**: SEC22B links SLC1A5 and ACSL3 in the module and has a very strong STRING relationship with STX7. It is a vesicle-trafficking protein involved in ER-Golgi transport, vesicle fusion, and autophagy-related processes. It is included in the primary melanosome, pigment-granule, and organelle-membrane terms (GO:CC melanosome; q_global = 0.00238) (GO:CC pigment granule; q_global = 0.00238) (GO:CC organelle membrane; q_global = 0.0304), while its neutrophil enhancement raises the possibility of a shared immune or vesicle-rich cell source.
- **Conclusion**: Established evidence supports SEC22B as a trafficking component and gives a coherent explanation for the SEC22B-STX7 relationship. Its role in assembling the entire module, or in producing pigment-granule biology in both tissues, remains a hypothesis.

#### GALNT2

- **Related proteins** (co-abundance neighbors): SLC3A2 (0.83), RRBP1 (0.82), ATP1B3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypeptide N-acetylgalactosaminyltransferase 2. This gene encodes a member of the glycosyltransferase 2 protein family. Members of this family initiate mucin-type O-glycoslation of peptides in the Golgi apparatus. The encoded protein may be involved in O-linked glycosylation of the immunoglobulin A1 hinge region. This gene may influence triglyceride levels, and may be involved Type 2 diabetes, as well as several types of cancer. Alternative spl…
- **Diseases (Open Targets)**: congenital disorder of glycosylation, type iit (0.777); metabolic syndrome (0.546); familial lipoprotein lipase deficiency (0.486); alcohol drinking (0.450); familial hyperlipidemia (0.444)
- **Europe PMC papers**: 1178
- **Why important**: GALNT2 occupies a connector position between SLC3A2, RRBP1, and ATP1B3. It is a Golgi glycosyltransferase that initiates mucin-type O-linked glycosylation and appears in the primary organelle-membrane term (GO:CC organelle membrane; q_global = 0.0304). Its Golgi localization and links to protein maturation complement the ER and vesicle-trafficking members. It has substantial literature and disease associations involving glycosylation and metabolic disorders.
- **Conclusion**: Established evidence supports GALNT2 as a Golgi protein-processing component that may help explain the organelle-membrane coherence of the module. Its potential influence on transporter maturation or trafficking is mechanistically plausible but not demonstrated by the supplied data.

## Module 1

**Tissue pair**: brain and ovary  
**Genes (7)**: SERPINA1, ALB, APOA1, CLU, C3, TLN2, TF

### Function

The module is best interpreted as a circulating secreted-protein and extracellular-lumen module centered on lipid transport, complement and humoral immunity, protease inhibition, iron transport, and receptor-mediated uptake. The strongest primary evidence is the global enrichment of blood microparticle (GO:CC blood microparticle; q_global = 3.2e-05), endoplasmic-reticulum lumen (GO:CC endoplasmic reticulum lumen; q_global = 6.46e-05), secretory granule and vesicle lumen (5 globally significant GO/KEGG terms, q_global 0.000151–0.00544; see the table), complement and coagulation cascades (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.00533), humoral immune response (GO:BP humoral immune response; q_global = 0.00954), regulation of endocytosis (4 globally significant GO/KEGG terms, q_global 0.00234–0.0443; see the table), HDL particles and reverse cholesterol transport (GO:CC spherical high-density lipoprotein particle; q_global = 0.0117) (GO:BP reverse cholesterol transport; q_global = 0.0277), platelet alpha-granule terms (GO:CC platelet alpha granule lumen; q_global = 0.0196) (GO:CC platelet alpha granule; q_global = 0.0481), and signaling receptor binding (GO:MF signaling receptor binding; q_global = 0.0476). The genes therefore form a coherent extracellular transport and defense signature rather than a canonical intracellular brain or ovarian pathway. The secretory-lumen terms indicate a shared protein-abundance program; they do not by themselves establish that these proteins are synthesized locally in both tissues.

**Cell composition.** The module is strongly dominated by secreted-to-blood proteins: ALB, APOA1, C3, CLU, SERPINA1, and TF are annotated as secreted, while TLN2 is a cytosolic and focal-adhesion protein. HPA shows liver enrichment for most of the module and hepatocyte association for most of the genes, with additional associations to cholangiocytes, enterocytes, endometrial secretory cells, and other epithelial or secretory populations. Several genes also have immune-cell enrichment or enhancement, particularly monocyte, neutrophil, plasmacytoid dendritic-cell, and basophil annotations. Protein detection is absent in ovary and limited in the surveyed brain regions, apart from detection of CLU and TLN2 in brain. Thus, the shared brain–ovary signal is more plausibly a circulating-plasma, vascular, barrier, or shared secretory-cell signal than a tissue-resident neuronal–ovarian program. Blood-cell contribution or sample carryover should be considered explicitly, although the HPA profiles also support a liver-derived plasma-protein explanation.

**GO/KEGG enrichment**: 20 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 3.2e-05 | ALB, APOA1, C3, CLU, TF |
| GO:CC endoplasmic reticulum lumen | 6.46e-05 | ALB, APOA1, C3, CLU, SERPINA1, TF |
| GO:CC secretory granule lumen | 0.000151 | ALB, APOA1, C3, CLU, SERPINA1, TF |
| GO:CC cytoplasmic vesicle lumen | 0.000157 | ALB, APOA1, C3, CLU, SERPINA1, TF |
| GO:CC vesicle lumen | 0.000164 | ALB, APOA1, C3, CLU, SERPINA1, TF |
| GO:BP positive regulation of endocytosis | 0.00234 | APOA1, C3, CLU, TF |
| GO:CC secretory granule | 0.00293 | ALB, APOA1, C3, CLU, SERPINA1, TF |
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 0.00533 | C3, CLU, SERPINA1 |
| GO:CC secretory vesicle | 0.00544 | ALB, APOA1, C3, CLU, SERPINA1, TF |
| GO:BP humoral immune response | 0.00954 | C3, CLU, TF |
| GO:BP positive regulation of receptor-mediated endocytosis | 0.00954 | C3, CLU, TF |
| GO:CC spherical high-density lipoprotein particle | 0.0117 | APOA1, CLU |
| GO:BP regulation of endocytosis | 0.0187 | APOA1, C3, CLU, TF |
| GO:CC platelet alpha granule lumen | 0.0196 | ALB, CLU, SERPINA1 |
| GO:BP humoral immune response mediated by circulating immunoglobulin | 0.0277 | C3, CLU |

### STRING and hu.MAP

STRING supports a dense, biologically coherent extracellular network among ALB, APOA1, C3, CLU, SERPINA1, and TF. The strongest relationships connect albumin with apolipoprotein A1 and SERPINA1, apolipoprotein A1 with CLU and C3, and C3 with CLU and SERPINA1. STRING functional evidence independently recapitulates complement/coagulation, protein–lipid complexes, plasma-protein studies, lipoprotein fractions, and serum protein-corona observations (15 supplementary STRING terms; within-query FDR 6.39e-09–1.08e-07). These annotations are supplementary rather than globally corrected module enrichment. hu.MAP places ALB, APOA1, C3, SERPINA1, and TF together in multiple complexes containing broader plasma, complement, coagulation, lipoprotein, and acute-phase protein repertoires (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_02242.1). This indicates that much of the module reflects established biochemical co-complex or co-occurrence structure. CLU and TLN2 do not appear in the reported hu.MAP complexes, and TLN2 has no reported STRING partner in this module; consequently, their inclusion may reflect tissue-specific co-abundance or a less well-characterized association rather than a demonstrated physical complex.

**STRING interactions (score >= 0.7)**: 13 of 21 gene pairs: ALB–APOA1 (0.998); ALB–C3 (0.959); ALB–CLU (0.831); ALB–SERPINA1 (0.998); ALB–TF (0.9); APOA1–C3 (0.957); APOA1–CLU (0.998); APOA1–SERPINA1 (0.927); APOA1–TF (0.919); C3–CLU (0.803); C3–SERPINA1 (0.859); CLU–SERPINA1 (0.896); SERPINA1–TF (0.848)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Complement and coagulation cascades, and Protein-lipid complex (FDR = 6.39e-09, 6 genes); PMID (2021) Thermal Pain Thresholds Are Significantly Associated with Plasma Proteins of the Immune System in Chronic Widespread Pain-An Exploratory Pilot Study Using Multivariate and Network Analyses. (FDR = 1.37e-08, 6 genes); PMID (2020) Quantitative Protein Corona Composition and Dynamics on Carbon Nanotubes in Biological Environments. (FDR = 1.37e-08, 6 genes); PMID (2010) Utilizing spectral counting to quantitatively characterize tandem removal of abundant proteins (TRAP) in human plasma. (FDR = 1.37e-08, 6 genes); PMID (2023) Protein Corona of Anionic Fluid-Phase Liposomes Compromises Their Integrity Rather than Uptake by Cells. (FDR = 1.6e-08, 6 genes); PMID (2011) Proteomic analyses of host and pathogen responses during bovine mastitis. (FDR = 1.6e-08, 6 genes); PMID (2022) Serum alpha-1-antitrypsin level in the severity prognosis of systemic lupus erythematosus patients: Systematic exploration of novel biomarker. (FDR = 1.65e-08, 6 genes); PMID (2023) Proteomics of high-density lipoprotein subfractions and subclinical atherosclerosis in type 1 diabetes mellitus: a case-control study. (FDR = 2.11e-08, 6 genes); PMID (2010) Quantitative comparison of lipoprotein fractions derived from human plasma and serum by liquid chromatography-tandem mass spectrometry. (FDR = 2.7e-08, 6 genes); PMID (2022) HDL Isolated by Immunoaffinity, Ultracentrifugation, or Precipitation is Compositionally and Functionally Distinct. (FDR = 3.43e-08, 6 genes); PMID (2020) Significant correlation between plasma proteome profile and pain intensity, sensitivity, and psychological distress in women with fibromyalgia. (FDR = 3.43e-08, 6 genes); PMID (2022) Macromolecules Absorbed from Influenza Infection-Based Sera Modulate the Cellular Uptake of Polymeric Nanoparticles. (FDR = 3.93e-08, 6 genes); PMID (2015) Candida albicans Shaving to Profile Human Serum Proteins on Hyphal Surface. (FDR = 6.7e-08, 6 genes); PMID (2020) Multiplexed quantitative proteomics provides mechanistic cues for malaria severity and complexity. (FDR = 1.08e-07, 6 genes); PMID (2016) Proteome Profile and Quantitative Proteomic Analysis of Buffalo (Bubalusbubalis) Follicular Fluid during Follicle Development. (FDR = 1.08e-07, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07432.1 (SERPINA1, C3, APOA1, ALB, TF; 5/18); huMAP3_09434.1 (SERPINA1, C3, APOA1, ALB, TF; 5/33); huMAP3_08395.1 (SERPINA1, C3, APOA1, ALB, TF; 5/43); huMAP3_09531.1 (SERPINA1, C3, APOA1, ALB, TF; 5/47); huMAP3_10101.1 (SERPINA1, C3, APOA1, ALB, TF; 5/49); huMAP3_15040.1 (SERPINA1, C3, APOA1, ALB, TF; 5/64); huMAP3_10678.1 (SERPINA1, C3, APOA1, ALB, TF; 5/71); huMAP3_07265.1 (SERPINA1, APOA1, ALB, TF; 4/20); huMAP3_08224.1 (C3, APOA1, TF; 3/21); huMAP3_02242.1 (C3, TF; 2/9); huMAP3_08700.1 (SERPINA1, ALB; 2/11)

### Novelty

The biological theme itself is not a new discovery: the principal relationships are already supported by STRING, hu.MAP, plasma proteomics, complement biology, lipoprotein biology, and extensive literature. The potentially novel observation is the recurrence of this particular co-abundance module across brain and ovary. However, the supplied evidence does not establish that this cross-tissue module has not been reported previously, and absence of TLN2 or CLU from the reported hu.MAP complexes is not evidence of novelty. A cautious conclusion is that the module is a new computationally observed cross-tissue grouping, but not a newly discovered molecular pathway; its novelty requires comparison with independent tissue proteomes, batch- and plasma-aware analyses, and published cross-tissue co-abundance modules.

**Hypothesis.** Hypothesis: a circulating liver-derived protein milieu is co-measured across brain and ovary samples and is organized around lipid transport, complement regulation, protease inhibition, iron handling, and extracellular protein uptake. ALB, APOA1, SERPINA1, C3, CLU, and TF may travel in overlapping plasma or vesicular environments, while CLU and C3 could influence extracellular cargo handling and receptor-mediated uptake. TLN2 may mark a tissue-interface or cytoskeletal response that links extracellular complement-associated material to cell adhesion or uptake in brain-associated cells. This hypothesis predicts that the module will weaken after rigorous plasma-protein, vascular, and cell-composition adjustment, and that orthogonal assays should distinguish circulating carryover from local production.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): SERPINA1 (0.94), TLN2 (0.90), CLU (0.83); STRING partners: ALB (0.959), APOA1 (0.957), CLU (0.803), SERPINA1 (0.859)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07432.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_08224.1, huMAP3_02242.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a central complement component and occupies a core position connecting SERPINA1, CLU, and TLN2 in the module. It contributes to the globally significant complement, humoral immune, receptor-mediated endocytosis, and signaling-receptor-binding evidence (9 globally significant GO/KEGG terms, q_global 0.00234–0.0476; see the table). HPA supports liver and secreted-to-blood origin with immune-cell association. Its disease associations include complement deficiency, complement glomerulopathy, atypical hemolytic-uremic syndrome, and age-related macular degeneration. It also has exceptionally extensive literature coverage.
- **Conclusion**: Established evidence supports C3 as the principal immune and complement anchor of the module and as a plausible driver of extracellular signaling. It is not established that C3 is locally produced by brain or ovary in this module; the HPA evidence instead favors a circulating or liver-derived contribution.

#### ALB

- **Related proteins** (co-abundance neighbors): TF (0.92), SERPINA1 (0.83), APOA1 (0.82); STRING partners: APOA1 (0.998), C3 (0.959), CLU (0.831), SERPINA1 (0.998), TF (0.9)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07432.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07265.1, huMAP3_08700.1
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB is a highly connected core member and links the principal plasma proteins, including APOA1, SERPINA1, and TF. It contributes to blood microparticle, secretory-lumen, secretory-granule, and platelet-alpha-granule evidence (9 globally significant GO/KEGG terms, q_global 3.2e-05–0.0481; see the table). HPA identifies liver and hepatocyte enrichment and secretion to blood. Its established roles as the major plasma protein, carrier of endogenous and exogenous molecules, and regulator of plasma colloid osmotic pressure make it a strong indicator of plasma composition. It has substantial literature and disease associations including analbuminemia, thyroid-hormone abnormalities, and chronic kidney disease.
- **Conclusion**: Established evidence supports ALB primarily as a marker and functional component of the circulating plasma environment, rather than as a tissue-specific brain–ovary mediator. Its presence raises the possibility that sample plasma or vascular content contributes materially to the shared module.

#### APOA1

- **Related proteins** (co-abundance neighbors): SERPINA1 (0.93), ALB (0.82); STRING partners: ALB (0.998), C3 (0.957), CLU (0.998), SERPINA1 (0.927), TF (0.919)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07432.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07265.1, huMAP3_08224.1
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is a core network member connected to ALB and SERPINA1 and is strongly supported by STRING and hu.MAP. It contributes to HDL-particle, reverse-cholesterol-transport, endocytosis, secretory-lumen, and receptor-binding evidence (5 globally significant GO/KEGG terms, q_global 0.00234–0.0476; see the table). HPA supports liver and intestinal or hepatocyte origin and secretion to blood. Its established function as the major HDL protein, promoter of cholesterol efflux, and cofactor for LCAT gives the module a clear lipid-transport component. Its disease associations include apolipoprotein A-I deficiency, hypoalphalipoproteinemia, and familial visceral amyloidosis, with substantial literature coverage.
- **Conclusion**: Established evidence supports APOA1 as the lipid-transport anchor and as evidence that the module contains HDL-associated material. A local brain or ovarian APOA1 program is not established by the supplied data; circulating HDL or plasma exposure is the more conservative interpretation.

#### SERPINA1

- **Related proteins** (co-abundance neighbors): C3 (0.94), APOA1 (0.93), ALB (0.83); STRING partners: ALB (0.998), APOA1 (0.927), C3 (0.859), CLU (0.896), TF (0.848)
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07432.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07265.1, huMAP3_08700.1
- **Function (MyGene.info)**: serpin family A member 1. The protein encoded by this gene is a serine protease inhibitor belonging to the serpin superfamily whose targets include elastase, plasmin, thrombin, trypsin, chymotrypsin, and plasminogen activator. This protein is produced in the liver, the bone marrow, by lymphocytic and monocytic cells in lymphoid tissue, and by the Paneth cells of the gut. Defects in this gene are associated with chronic obs…
- **Diseases (Open Targets)**: alpha 1-antitrypsin deficiency (0.768); chronic obstructive pulmonary disease (0.690); cirrhosis of liver (0.573); cholelithiasis (0.569); pulmonary emphysema (0.569)
- **Europe PMC papers**: 6526
- **Why important**: SERPINA1 is a core network member connected to C3, APOA1, and ALB and appears across the reported hu.MAP complexes and STRING evidence (STRING NetworkNeighborAL Complement and coagulation cascades, and Protein-lipid complex; within-query FDR = 6.39e-09) (STRING PMID (2021) Thermal Pain Thresholds Are Significantly Associated with Plasma Proteins of the Immune System in Chronic Widespread Pain-An Exploratory Pilot Study Using Multivariate and Network Analyses.; within-query FDR = 1.37e-08) (STRING PMID (2020) Quantitative Protein Corona Composition and Dynamics on Carbon Nanotubes in Biological Environments.; within-query FDR = 1.37e-08) (STRING PMID (2010) Utilizing spectral counting to quantitatively characterize tandem removal of abundant proteins (TRAP) in human plasma.; within-query FDR = 1.37e-08) (STRING PMID (2023) Protein Corona of Anionic Fluid-Phase Liposomes Compromises Their Integrity Rather than Uptake by Cells.; within-query FDR = 1.6e-08) (STRING PMID (2011) Proteomic analyses of host and pathogen responses during bovine mastitis.; within-query FDR = 1.6e-08) (STRING PMID (2022) Serum alpha-1-antitrypsin level in the severity prognosis of systemic lupus erythematosus patients: Systematic exploration of novel biomarker.; within-query FDR = 1.65e-08) (STRING PMID (2023) Proteomics of high-density lipoprotein subfractions and subclinical atherosclerosis in type 1 diabetes mellitus: a case-control study.; within-query FDR = 2.11e-08) (STRING PMID (2010) Quantitative comparison of lipoprotein fractions derived from human plasma and serum by liquid chromatography-tandem mass spectrometry.; within-query FDR = 2.7e-08) (STRING PMID (2022) HDL Isolated by Immunoaffinity, Ultracentrifugation, or Precipitation is Compositionally and Functionally Distinct.; within-query FDR = 3.43e-08) (STRING PMID (2020) Significant correlation between plasma proteome profile and pain intensity, sensitivity, and psychological distress in women with fibromyalgia.; within-query FDR = 3.43e-08) (STRING PMID (2022) Macromolecules Absorbed from Influenza Infection-Based Sera Modulate the Cellular Uptake of Polymeric Nanoparticles.; within-query FDR = 3.93e-08) (STRING PMID (2015) Candida albicans Shaving to Profile Human Serum Proteins on Hyphal Surface.; within-query FDR = 6.7e-08) (STRING PMID (2020) Multiplexed quantitative proteomics provides mechanistic cues for malaria severity and complexity.; within-query FDR = 1.08e-07) (STRING PMID (2016) Proteome Profile and Quantitative Proteomic Analysis of Buffalo (Bubalusbubalis) Follicular Fluid during Follicle Development.; within-query FDR = 1.08e-07) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_08700.1). It contributes to complement/coagulation, secretory-lumen, and platelet-alpha-granule evidence (9 globally significant GO/KEGG terms, q_global 6.46e-05–0.0481; see the table). HPA supports liver, hepatocyte, immune-cell, and blood-secreted origin. Its established serpin activity targets several proteases, including elastase, plasmin, thrombin, trypsin, chymotrypsin, and plasminogen activator. Alpha-one-antitrypsin deficiency, chronic obstructive pulmonary disease, emphysema, and chronic liver disease are established disease links, and the gene has substantial literature coverage.
- **Conclusion**: Established evidence supports SERPINA1 as the protease-regulatory and plasma-defense component of the module. Its co-abundance with complement and lipoprotein proteins is biologically plausible, but the data do not show that it is synthesized locally in brain or ovary.

#### CLU

- **Related proteins** (co-abundance neighbors): C3 (0.83); STRING partners: ALB (0.831), APOA1 (0.998), C3 (0.803), SERPINA1 (0.896)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: clusterin. The protein encoded by this gene is a secreted chaperone that can under some stress conditions also be found in the cell cytosol. It has been suggested to be involved in several basic biological events such as cell death, tumor progression, and neurodegenerative disorders. Alternate splicing results in both coding and non-coding variants.[provided by RefSeq, May 2011].
- **Diseases (Open Targets)**: Alzheimer disease (0.583); dementia (0.525); refractive error (0.444); late-onset Alzheimers disease (0.406); prostate cancer (0.376)
- **Europe PMC papers**: 10677
- **Why important**: CLU is directly connected to C3 and has strong STRING relationships with APOA1, ALB, and SERPINA1. It is present in every globally significant enrichment category summarized by the module, including extracellular vesicle or granule compartments, complement and humoral immunity, endocytosis, HDL biology, reverse cholesterol transport, and receptor binding (20 globally significant GO/KEGG terms, q_global 3.2e-05–0.0481; see the table). HPA supports liver enhancement, secreted-to-blood status, brain detection, and association with endometrial and reproductive-tract secretory cell types. Its established functions include secreted chaperoning, immune-complex clearance, negative regulation of membrane-attack-complex activation, protein folding, and roles in cell death and neurodegenerative disease. It has substantial literature and disease associations including Alzheimer disease and dementia.
- **Conclusion**: Established evidence supports CLU as a multifunctional extracellular chaperone and complement-modulating bridge between lipid transport, immune defense, and protein handling. Its brain detection and reproductive-tract secretory associations make it a plausible tissue-interface contributor, but local production in ovary and a causal role in the shared module remain hypotheses.

## Module 2

**Tissue pair**: brain and ovary  
**Genes (13)**: ABCF3, DDX46, FEN1, EIF4G1, NSUN2, PPM1G, GART, RCC1, SF3A1, SMC2, SMC4, SRPK1, TXLNA

### Function

The module is best interpreted as a conserved nuclear proliferation and chromosome-management program. The primary evidence is regulation of cell cycle (GO:BP regulation of cell cycle; q_global = 0.0393), supported by EIF4G1, FEN1, NSUN2, PPM1G, RCC1, SMC2 and SMC4. The genes also provide supporting context for DNA replication and repair through FEN1, chromosome condensation and segregation through SMC2 and SMC4, cell-cycle control through RCC1 and PPM1G, RNA modification through NSUN2, translation initiation through EIF4G1, and pre-mRNA splicing through SF3A1 and DDX46. Because only one GO or KEGG term passed global correction, these additional processes should be treated as functional context rather than independently globally significant enrichment. The sparse co-abundance graph and absence of STRING functional enrichment suggest a coordinated but heterogeneous expression program rather than a single complete biochemical complex.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. Only one gene is classified as secreted, and the proteins are mainly intracellular, nuclear or cytosolic. Protein detection is broad in brain and nearly complete in ovary, supporting genuine protein presence in both tissues. Most genes have low tissue specificity and low immune-cell specificity, consistent with broadly expressed housekeeping or proliferation-associated genes. However, several genes show enrichment in lymphoid tissue, spermatogenic populations, erythrocyte progenitors or megakaryocyte progenitors, and some show basophil enhancement. The shared brain and ovary signal could therefore reflect a conserved proliferative or germ-cell-associated state, or shared sample cell types, rather than a program specific to neurons or ovarian cells.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulation of cell cycle | 0.0393 | EIF4G1, FEN1, NSUN2, PPM1G, RCC1, SMC2, SMC4 |

### STRING and hu.MAP

STRING supports two high-confidence pairwise relationships: SMC2 with SMC4 and DDX46 with SF3A1. These relationships support condensin-related chromosome organization and spliceosome-related RNA processing. hu.MAP independently places SMC2 and SMC4 together in condensin-associated complexes (hu.MAP huMAP3_03084.1), (hu.MAP huMAP3_14385.1), (hu.MAP huMAP3_09855.1), (hu.MAP huMAP3_11457.1) and (hu.MAP huMAP3_14663.1), and places SF3A1 and DDX46 together in spliceosomal or RNA-processing complexes (hu.MAP huMAP3_04549.1), (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1). These are only selected pairs from larger known complexes, so the module appears to capture coordinated abundance of components rather than a complete physical complex. The lack of reported STRING or hu.MAP relationships for most other genes means that co-abundance should not be interpreted as direct physical interaction.

**STRING interactions (score >= 0.7)**: 2 of 78 gene pairs: DDX46–SF3A1 (0.999); SMC2–SMC4 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03084.1 (SMC2, SMC4; 2/8); huMAP3_14385.1 (SMC2, SMC4; 2/9); huMAP3_09855.1 (SMC2, SMC4; 2/10); huMAP3_11457.1 (SMC2, SMC4; 2/10); huMAP3_14663.1 (SMC2, SMC4; 2/14); huMAP3_04549.1 (SF3A1, DDX46; 2/52); huMAP3_06511.1 (SF3A1, DDX46; 2/79); huMAP3_08980.1 (SF3A1, DDX46; 2/97)

### Novelty

The module is unlikely to represent a wholly new molecular mechanism because its clearest substructures correspond to established condensin and spliceosome relationships, while its primary interpretation is a familiar cell-cycle and chromosome-management program. It may nevertheless be a new systems-level observation if this particular coordinated abundance pattern has not previously been reported across brain and ovary. Absence from STRING or hu.MAP does not establish novelty, because interaction resources are incomplete and the module may reflect indirect regulation, tissue-dependent abundance or cell composition. A firm novelty claim would require comparison with published brain and ovary co-abundance studies and independent datasets, which are not provided here.

**Hypothesis.** Hypothesis: the module reflects a conserved proliferative or germ-cell-associated nuclear state shared by subsets of brain and ovary samples. In this state, SMC2 and SMC4 support chromosome organization, FEN1 and RCC1 support replication, repair and cell-cycle progression, and NSUN2, DDX46, SF3A1 and PPM1G support RNA modification, spliceosome function and phosphorylation control. EIF4G1 may support increased translational demand. This hypothesis predicts that module abundance will track proliferating or differentiating cells and may be stronger in samples containing germ-cell, lymphoid or other cycling-cell contributions. It does not imply that all module genes form one physical complex.

### Important genes

#### SMC2

- **Related proteins** (co-abundance neighbors): SMC4 (0.86); STRING partners: SMC4 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_03084.1, huMAP3_14385.1, huMAP3_09855.1, huMAP3_11457.1, huMAP3_14663.1
- **Function (MyGene.info)**: structural maintenance of chromosomes 2. Predicted to enable ATP binding activity; chromatin binding activity; and single-stranded DNA binding activity. Involved in mitotic chromosome condensation. Located in condensed chromosome; cytoplasm; and nuclear lumen. Part of condensin complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: basal cell carcinoma (0.464); ovarian carcinoma (0.383); aortic stenosis (0.380); cancer (0.363); alcohol drinking (0.359)
- **Europe PMC papers**: 2065
- **Why important**: SMC2 is one half of the condensin-related pair supported directly by STRING and repeatedly represented in hu.MAP complexes (hu.MAP huMAP3_03084.1), (hu.MAP huMAP3_14385.1), (hu.MAP huMAP3_09855.1), (hu.MAP huMAP3_11457.1) and (hu.MAP huMAP3_14663.1). It contributes to (GO:BP regulation of cell cycle; q_global = 0.0393) and is annotated for mitotic chromosome condensation, chromosome organization and chromosome segregation. Its ovarian carcinoma and broader cancer associations make it relevant to proliferative tissue states, and its substantial literature supports an established biological role.
- **Conclusion**: Established evidence supports SMC2 as a central chromosome-condensation and cell-cycle component. Its coordinated abundance may mark a shared cycling or germ-cell-like state in brain and ovary, but that interpretation remains a hypothesis.

#### SMC4

- **Related proteins** (co-abundance neighbors): SMC2 (0.86), EIF4G1 (0.81), PPM1G (0.80); STRING partners: SMC2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nuclear speckles, Cytosol; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_03084.1, huMAP3_14385.1, huMAP3_09855.1, huMAP3_11457.1, huMAP3_14663.1
- **Function (MyGene.info)**: structural maintenance of chromosomes 4. This gene belongs to the 'structural maintenance of chromosomes' (SMC) gene family. Members of this gene family play a role in two changes in chromosome structure during mitotic segregation of chromosomes- chromosome condensation and sister chromatid cohesion. The protein encoded by this gene is likely a subunit of the 13S condensin complex, which is involved in chromosome condensation. A pseudoge…
- **Diseases (Open Targets)**: clonal hematopoiesis (0.233); bone marrow failure syndrome (0.148); hepatocellular carcinoma (0.111); central nervous system cancer (0.107); glioma (0.107)
- **Europe PMC papers**: 1967
- **Why important**: SMC4 is the complementary condensin partner of SMC2, with a very strong direct STRING relationship and repeated hu.MAP support (hu.MAP huMAP3_03084.1) through (hu.MAP huMAP3_14663.1). It contributes to (GO:BP regulation of cell cycle; q_global = 0.0393) and is annotated for mitotic chromosome condensation, chromosome segregation and cell development. Its HPA profile includes lymphoid and several progenitor or spermatogenic cell enrichments, making it informative for interpreting possible cellular composition.
- **Conclusion**: Established evidence identifies SMC4 as a condensin-associated cell-cycle component and a major anchor of the chromosome-organization interpretation. Its tissue and cell-type enrichments support, but do not prove, a shared proliferative or progenitor-cell explanation.

#### FEN1

- **Related proteins** (co-abundance neighbors): SF3A1 (0.89), RCC1 (0.87), TXLNA (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: flap structure-specific endonuclease 1. The protein encoded by this gene removes 5' overhanging flaps in DNA repair and processes the 5' ends of Okazaki fragments in lagging strand DNA synthesis. Direct physical interaction between this protein and AP endonuclease 1 during long-patch base excision repair provides coordinated loading of the proteins onto the substrate, thus passing the substrate from one enzyme to another. The protein is…
- **Diseases (Open Targets)**: neurodegenerative disease (0.496); HIV infectious disease (0.370); hepatocellular carcinoma (0.213); breast carcinoma (0.213); oral cavity squamous cell carcinoma (0.208)
- **Europe PMC papers**: 5275
- **Why important**: FEN1 has a relatively central position in the co-abundance graph and connects to SF3A1 and RCC1. It contributes to (GO:BP regulation of cell cycle; q_global = 0.0393) and has established roles in DNA replication, flap processing, base-excision repair and homologous-recombination-associated repair. HPA detects it in both tissues and shows enhancement in lymphoid and multiple spermatogenic or erythroid progenitor populations. Its extensive literature and disease associations make it a strong bridge between DNA maintenance and the module's tissue context.
- **Conclusion**: Established evidence supports FEN1 as a replication and DNA-repair component consistent with a cycling-cell program. Its network connection to a splicing factor is observed, but a direct mechanistic coupling between DNA repair and splicing remains hypothetical.

#### NSUN2

- **Related proteins** (co-abundance neighbors): GART (0.82), RCC1 (0.82), DDX46 (0.82), SRPK1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP2/Sun RNA methyltransferase 2. This gene encodes a methyltransferase that catalyzes the methylation of cytosine to 5-methylcytosine (m5C) at position 34 of intron-containing tRNA(Leu)(CAA) precursors. This modification is necessary to stabilize the anticodon-codon pairing and correctly translate the mRNA. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Mar…
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.694); hereditary disease (0.518); Intellectual disability (0.489); phenylketonuria (0.470); neurodegenerative disease (0.462)
- **Europe PMC papers**: 2458
- **Why important**: NSUN2 has the highest weighted network position in the module and connects GART, RCC1, DDX46 and SRPK1. It contributes to (GO:BP regulation of cell cycle; q_global = 0.0393) and is an RNA methyltransferase involved in tRNA modification, rRNA processing, mRNA processing and mRNA export. Its intellectual-disability and neurodegenerative-disease associations are relevant to the brain tissue pair, and its substantial literature supports an established role in RNA regulation.
- **Conclusion**: Established evidence supports NSUN2 as a highly connected RNA-modification and RNA-processing component that may explain why RNA metabolism accompanies the cell-cycle signal. Its specific role in generating the shared brain and ovary pattern is unresolved.

#### RCC1

- **Related proteins** (co-abundance neighbors): FEN1 (0.87), NSUN2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: regulator of chromosome condensation 1. Enables several functions, including guanyl-nucleotide exchange factor activity; nucleosomal DNA binding activity; and protein heterodimerization activity. Involved in several processes, including G1/S transition of mitotic cell cycle; regulation of mitotic nuclear division; and spindle organization. Located in chromatin; cytoplasm; and nucleus. Part of protein-containing complex. [provided by All…
- **Diseases (Open Targets)**: injury (0.338); neurodegenerative disease (0.338); myasthenia gravis (0.329); neoplasm (0.104); cancer (0.091)
- **Europe PMC papers**: 3525
- **Why important**: RCC1 connects FEN1 and NSUN2 and contributes to (GO:BP regulation of cell cycle; q_global = 0.0393). It is annotated for the G one/S transition, mitotic spindle organization, chromosome segregation, nuclear reassembly and regulation of mitotic division. It is detected in both tissues and is enriched in late spermatids, providing a relevant link to the reproductive-cell signal. Its disease associations include neurodegenerative disease and injury, supported by a substantial literature base.
- **Conclusion**: Established evidence supports RCC1 as a cell-cycle and chromosome-segregation regulator connecting the DNA-maintenance and RNA-regulatory portions of the module. Its spermatid enrichment supports a reproductive-cell interpretation, but does not establish that the module originates from germ cells.

## Module 3

**Tissue pair**: brain and ovary  
**Genes (14)**: ABHD10, ABHD11, ADAM10, ATP5PB, ATP5F1C, DECR1, ETFA, NIPSNAP2, RAB18, SFXN1, SUCLG1, TIMM50, UQCC1, VDAC2

### Function

This is a mitochondrial energy and metabolic maintenance module. The strongest primary evidence is the global GO cellular-component enrichment for mitochondrial matrix (GO:CC mitochondrial matrix; q_global = 0.000291), mitochondrion (GO:CC mitochondrion; q_global = 0.000879), mitochondrial membrane (GO:CC mitochondrial membrane; q_global = 0.0232), and mitochondrial envelope (GO:CC mitochondrial envelope; q_global = 0.0415). The module combines mitochondrial ATP synthase components ATP5F1C and ATP5PB, the succinate-CoA ligase component SUCLG1, the electron-transfer protein ETFA, the fatty-acid oxidation enzyme DECR1, the mitochondrial serine transporter SFXN1, the import and membrane organization factor TIMM50, and additional mitochondrial proteins. The annotations support coordinated oxidative phosphorylation, proton-motive-force-dependent ATP production, tricarboxylic-acid-cycle-linked metabolism, fatty-acid beta-oxidation, mitochondrial metabolite transport, and protein import. NIPSNAP2 and VDAC2 additionally connect the module to mitochondrial organization, metabolite exchange, and apoptosis-related membrane regulation. The STRING mitochondrial annotations (STRING COMPARTMENTS Mitochondrion; within-query FDR = 4.53e-06) through (STRING COMPARTMENTS Mitochondrial inner membrane; within-query FDR = 0.0208) are consistent supplementary evidence, while (STRING COMPARTMENTS Organelle membrane; within-query FDR = 0.0232) supports a broader organelle-membrane context.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins and does not show a blood-cell signature. HPA reports no secretome annotation for nearly all members; ADAM10 is described as intracellular and membrane-associated rather than a classical soluble secreted protein. Most members have low tissue specificity or are tissue enhanced, with enrichment in metabolically active tissues such as liver, muscle, heart muscle, and tongue. Cell-type enhancements are distributed across epithelial, digestive, muscle, germ-cell, and selected hematopoietic populations rather than being concentrated in one blood lineage. SFXN1 is immune-cell enhanced in basophils, but the overall blood-cell specificity is low. Protein detection in brain is broad across the assayed regions, whereas detection in ovary is less complete. Thus, the shared brain-ovary signal is more plausibly a broadly expressed mitochondrial program, possibly influenced by shared energetic demands or shared cell populations, than a plasma-protein or blood-contamination module.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrial matrix | 0.000291 | ABHD10, ABHD11, ATP5F1C, ATP5PB, DECR1, ETFA, NIPSNAP2, SUCLG1, VDAC2 |
| GO:CC mitochondrion | 0.000879 | ABHD10, ABHD11, ATP5F1C, ATP5PB, DECR1, ETFA, NIPSNAP2, SFXN1, SUCLG1, TIMM50, UQCC1, VDAC2 |
| GO:CC mitochondrial membrane | 0.0232 | ATP5F1C, ATP5PB, NIPSNAP2, SFXN1, TIMM50, UQCC1, VDAC2 |
| GO:CC mitochondrial envelope | 0.0415 | ATP5F1C, ATP5PB, NIPSNAP2, SFXN1, TIMM50, UQCC1, VDAC2 |

### STRING and hu.MAP

STRING supports a real but relatively sparse known interaction backbone. The strongest relationships are ATP5F1C with ATP5PB and SUCLG1, ETFA with SUCLG1, and ATP5F1C with ETFA. These links connect ATP synthase, succinate-CoA ligase, and electron-transfer metabolism, but most co-abundance edges are not represented by high-confidence STRING interactions. hu.MAP repeatedly places ATP5PB and ATP5F1C together in ATP-synthase-related or broader membrane-associated complexes (hu.MAP huMAP3_08716.1) through (hu.MAP huMAP3_11095.1). No other module member appears as a multi-member hu.MAP overlap in the supplied complexes. This establishes ATP5PB and ATP5F1C as a known complex anchor, while the broader module should be interpreted as a co-abundance program that links several mitochondrial processes rather than as one experimentally demonstrated physical complex.

**STRING interactions (score >= 0.7)**: 4 of 91 gene pairs: ATP5F1C–ATP5PB (0.999); ATP5F1C–ETFA (0.715); ATP5F1C–SUCLG1 (0.934); ETFA–SUCLG1 (0.956)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Mitochondrion (FDR = 4.53e-06, 12 genes); Keyword Mitochondrion (FDR = 2.21e-05, 11 genes); Component Mitochondrion (FDR = 6.04e-05, 12 genes); COMPARTMENTS Mitochondrial membrane (FDR = 0.0012, 7 genes); Component Mitochondrial membrane (FDR = 0.0057, 7 genes); Component Mitochondrial matrix (FDR = 0.0059, 7 genes); Keyword Transit peptide (FDR = 0.0078, 7 genes); Keyword Mitochondrion inner membrane (FDR = 0.009, 5 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.0189, 6 genes); COMPARTMENTS Mitochondrial inner membrane (FDR = 0.0208, 5 genes); COMPARTMENTS Organelle membrane (FDR = 0.0232, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08716.1 (ATP5PB, ATP5F1C; 2/15); huMAP3_07476.1 (ATP5PB, ATP5F1C; 2/18); huMAP3_05994.1 (ATP5PB, ATP5F1C; 2/19); huMAP3_08393.1 (ATP5PB, ATP5F1C; 2/19); huMAP3_09775.1 (ATP5PB, ATP5F1C; 2/21); huMAP3_09307.1 (ATP5PB, ATP5F1C; 2/35); huMAP3_11095.1 (ATP5PB, ATP5F1C; 2/45)

### Novelty

The module should not be presented as a newly discovered mitochondrial pathway. Its central functions, including ATP synthase activity, mitochondrial substrate metabolism, fatty-acid oxidation, metabolite transport, and protein import, are established by the gene annotations and by known STRING or hu.MAP relationships. The potentially novel aspect is the coordinated co-abundance of this particular gene set across brain and ovary, especially the association of less well-connected members with the established mitochondrial backbone. However, the fact sheet does not provide an external matched-module catalogue or a prior publication comparison, so module-level novelty cannot be established. Absence of many relationships from STRING or hu.MAP is not evidence that the co-abundance pattern itself is novel.

**Hypothesis.** Hypothesis: this conserved brain-ovary module represents a shared mitochondrial resource-allocation program that maintains ATP production while coordinating carbon and amino-acid handling with fatty-acid oxidation. ATP5F1C and ATP5PB could provide the ATP-synthase structural and energetic anchor; SUCLG1 and ETFA could link respiratory energy generation to tricarboxylic-acid-cycle and fatty-acid-derived electron flow; SFXN1 could couple mitochondrial serine transport to one-carbon and respiratory metabolism; and TIMM50, VDAC2, NIPSNAP2, and related proteins could maintain mitochondrial protein import, membrane exchange, and organelle quality control. This is a mechanistic model derived from co-abundance and annotations, not proof of direct physical interaction or causal regulation.

### Important genes

#### ATP5F1C

- **Related proteins** (co-abundance neighbors): SUCLG1 (0.83), SFXN1 (0.83), DECR1 (0.83), UQCC1 (0.82), ABHD10 (0.80); STRING partners: ATP5PB (0.999), ETFA (0.715), SUCLG1 (0.934)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_08716.1, huMAP3_07476.1, huMAP3_05994.1, huMAP3_08393.1, huMAP3_09775.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit gamma. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: late-onset Alzheimers disease (0.350); scleritis (0.189); diaphragm disorder (0.082); glioblastoma (0.044); external ear disorder (0.042)
- **Europe PMC papers**: 306
- **Why important**: ATP5F1C is the most connected module member and links SUCLG1, SFXN1, DECR1, UQCC1, and ABHD10 within the co-abundance graph. It is present in every primary mitochondrial enrichment term (GO:CC mitochondrial matrix; q_global = 0.000291) through (GO:CC mitochondrial envelope; q_global = 0.0415), in the mitochondrial STRING annotations (STRING COMPARTMENTS Mitochondrion; within-query FDR = 4.53e-06) through (STRING COMPARTMENTS Organelle membrane; within-query FDR = 0.0232), and in every supplied hu.MAP complex (hu.MAP huMAP3_08716.1) through (hu.MAP huMAP3_11095.1). Its established function is as the mitochondrial ATP-synthase gamma subunit, central to proton-motive-force-driven ATP synthesis. It also has a substantial literature base and disease links including late-onset Alzheimer disease.
- **Conclusion**: Established conclusion: ATP5F1C is the strongest energetic and network anchor of the module. Hypothesis: variation in its co-abundance may help report shared respiratory demand in brain and ovary, but the module does not demonstrate that ATP5F1C regulates the other genes.

#### SUCLG1

- **Related proteins** (co-abundance neighbors): ETFA (0.84), ATP5F1C (0.83), ADAM10 (0.83), SFXN1 (0.83); STRING partners: ATP5F1C (0.934), ETFA (0.956)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase GDP/ADP-forming subunit alpha. This gene encodes the alpha subunit of the heterodimeric enzyme succinate coenzyme A ligase. This enzyme is targeted to the mitochondria and catalyzes the conversion of succinyl CoA and ADP or GDP to succinate and ATP or GTP. Mutations in this gene are the cause of the metabolic disorder fatal infantile lactic acidosis and mitochondrial DNA depletion. [provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome 9 (0.811); neurodegenerative disease (0.520); mitochondrial DNA depletion syndrome (0.507); post term pregnancy (0.280); lysosomal storage disease (0.245)
- **Europe PMC papers**: 1277
- **Why important**: SUCLG1 is a highly connected bridge between ETFA, ATP5F1C, SFXN1, and ADAM10. It is supported by the primary matrix and mitochondrion terms (GO:CC mitochondrial matrix; q_global = 0.000291) and (GO:CC mitochondrion; q_global = 0.000879), by mitochondrial STRING terms (STRING COMPARTMENTS Mitochondrion; within-query FDR = 4.53e-06), (STRING Keyword Mitochondrion; within-query FDR = 2.21e-05), (STRING Component Mitochondrion; within-query FDR = 6.04e-05), (STRING Component Mitochondrial matrix; within-query FDR = 0.0059), (STRING Keyword Transit peptide; within-query FDR = 0.0078), and (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.0189), and by strong STRING relationships with ETFA and ATP5F1C. Its established role is the mitochondrial succinate-CoA ligase alpha subunit, linking succinyl-CoA metabolism to succinate and nucleotide-triphosphate production. It has a large literature base and strong disease associations with mitochondrial DNA depletion and lactic-acidosis-related disease.
- **Conclusion**: Established conclusion: SUCLG1 connects central mitochondrial carbon metabolism with the module's energy-producing core. Hypothesis: it may help couple substrate flux to ATP or GTP output in the shared tissue program.

#### ETFA

- **Related proteins** (co-abundance neighbors): SUCLG1 (0.84), DECR1 (0.82), ABHD11 (0.81), VDAC2 (0.81); STRING partners: ATP5F1C (0.715), SUCLG1 (0.956)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein subunit alpha. ETFA participates in catalyzing the initial step of the mitochondrial fatty acid beta-oxidation. It shuttles electrons between primary flavoprotein dehydrogenases and the membrane-bound electron transfer flavoprotein ubiquinone oxidoreductase. Defects in electron-transfer-flavoprotein have been implicated in type II glutaricaciduria in which multiple acyl-CoA dehydrogenase deficiencies result in l…
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.834); glutaric aciduria (0.756); hereditary disease (0.469); multiple acyl-CoA dehydrogenase deficiency, mild type (0.370); multiple acyl-CoA dehydrogenase deficiency, severe neonatal type (0.370)
- **Europe PMC papers**: 1433
- **Why important**: ETFA is a highly connected metabolic bridge, linking SUCLG1, DECR1, ABHD11, and VDAC2. It appears in the primary matrix and mitochondrion terms (GO:CC mitochondrial matrix; q_global = 0.000291) and (GO:CC mitochondrion; q_global = 0.000879) and in the mitochondrial STRING terms (STRING COMPARTMENTS Mitochondrion; within-query FDR = 4.53e-06), (STRING Keyword Mitochondrion; within-query FDR = 2.21e-05), (STRING Component Mitochondrion; within-query FDR = 6.04e-05), (STRING Component Mitochondrial matrix; within-query FDR = 0.0059), (STRING Keyword Transit peptide; within-query FDR = 0.0078), and (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.0189). Its established function is to transfer electrons from multiple acyl-CoA dehydrogenases to the membrane electron-transfer system during fatty-acid beta-oxidation. It has a substantial literature base and strong disease associations with multiple acyl-CoA dehydrogenase deficiency and glutaric aciduria.
- **Conclusion**: Established conclusion: ETFA gives the module a clear fatty-acid-derived electron-transfer component. Hypothesis: ETFA may be a key metabolic link through which lipid substrate availability influences the shared mitochondrial co-abundance state.

#### SFXN1

- **Related proteins** (co-abundance neighbors): VDAC2 (0.92), ATP5F1C (0.83), SUCLG1 (0.83), ATP5PB (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sideroflexin 1. Enables D-serine transmembrane transporter activity and L-serine transmembrane transporter activity. Involved in D-serine transport; L-serine transport; and serine import into mitochondrion. Located in mitochondrion. Is integral component of mitochondrial inner membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: placental abruption (0.323); alcohol drinking (0.322); clostridium difficile infection (0.144); refractive error (0.112); scoliosis (0.111)
- **Europe PMC papers**: 568
- **Why important**: SFXN1 is highly connected to VDAC2, ATP5F1C, SUCLG1, and ATP5PB and is present in the primary mitochondrion, mitochondrial membrane, and mitochondrial envelope terms (GO:CC mitochondrion; q_global = 0.000879), (GO:CC mitochondrial membrane; q_global = 0.0232), and (GO:CC mitochondrial envelope; q_global = 0.0415). Its established function is as an inner-membrane transporter for serine and D-serine, with links to one-carbon metabolism and amino-acid transport. It is detected in both brain and ovary and has a substantial literature base, although it has no supplied STRING partner or hu.MAP complex overlap.
- **Conclusion**: Established conclusion: SFXN1 provides a plausible metabolite-transport component within the mitochondrial program. Hypothesis: its co-abundance with ATP-synthesis and respiratory genes may coordinate serine-derived metabolic input with energetic demand.

#### VDAC2

- **Related proteins** (co-abundance neighbors): SFXN1 (0.92), TIMM50 (0.82), ETFA (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: voltage dependent anion channel 2. This gene encodes a member of the voltage-dependent anion channel pore-forming family of proteins that are considered the main pathway for metabolite diffusion across the mitochondrial outer membrane. The encoded protein is also thought to be involved in the mitochondrial apoptotic pathway via regulation of BCL2-antagonist/killer 1 protein activity. Pseudogenes have been identified on chromosomes …
- **Diseases (Open Targets)**: neurodegenerative disease (0.345); alcohol drinking (0.204); atrial fibrillation (0.175); major depressive disorder (0.143); severe combined immunodeficiency (0.118)
- **Europe PMC papers**: 2914
- **Why important**: VDAC2 connects SFXN1, TIMM50, and ETFA and is present in all primary GO cellular-component terms (GO:CC mitochondrial matrix; q_global = 0.000291) through (GO:CC mitochondrial envelope; q_global = 0.0415). Its established function is as a mitochondrial outer-membrane pore involved in metabolite diffusion, with additional involvement in mitochondrial apoptotic regulation and membrane permeabilization. It has the largest literature base among the selected genes and disease associations including neurodegenerative disease and major depressive disorder. It is detected in brain but not ovary in the supplied HPA protein data, which cautions against assuming identical protein-level behavior across the two tissues.
- **Conclusion**: Established conclusion: VDAC2 is a strategically positioned mitochondrial interface between transport, respiration, and membrane-permeabilization biology. Hypothesis: it could help couple metabolic state to mitochondrial membrane stability, but the tissue-specific detection difference prevents a strong claim that it is the common driver of the cross-tissue module.

## Module 4

**Tissue pair**: brain and ovary  
**Genes (12)**: ACADVL, CANX, CKAP4, EMC1, GNAI3, MOGS, DDOST, PLXNB2, PVR, SEC63, SPTLC1, TMEM214

### Function

The module is most strongly characterized as an endoplasmic-reticulum membrane and protein-processing module. (GO:CC endoplasmic reticulum membrane; q_global = 0.000119), (GO:CC endoplasmic reticulum subcompartment; q_global = 0.000119), (GO:CC nuclear outer membrane-endoplasmic reticulum membrane network; q_global = 0.000133), (GO:CC organelle subcompartment; q_global = 0.000879) and (GO:CC endoplasmic reticulum; q_global = 0.00953) converge on the ER membrane, its subcompartments, and the nuclear-outer-membrane–ER network, while (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00246) identifies protein processing in the ER. The shared genes include calnexin-mediated folding and quality control through CANX, N-linked glycan processing through MOGS and DDOST, ER membrane insertion through EMC1, and protein translocation through SEC63. SPTLC1 adds ER-associated sphingolipid biosynthesis, whereas ACADVL, GNAI3, PVR, PLXNB2 and TMEM214 may connect the core ER program to lipid metabolism, signaling, adhesion, trafficking or stress-related processes. Thus, the best-supported interpretation is coordinated ER proteostasis and membrane-protein handling, with possible links to membrane lipid homeostasis and cell-surface signaling. The globally corrected evidence is cellular-component and pathway focused; it does not by itself establish a specific brain or ovary physiological process.

**Cell composition.** The module is not dominated by secreted proteins: HPA identifies only PVR as secreted with unknown location, while the other proteins are intracellular or membrane-associated. It is also not broadly blood-cell specific. Most genes have low immune-cell specificity, although PVR and PLXNB2 show enrichment across monocyte or dendritic-cell categories, and CKAP4 shows immune-cell enhancement. All genes have low tissue specificity in HPA, and the module is detected in both brain and ovary at the protein level for nearly all assayed genes, with limited missing or negative detection. The recurrent cell-type associations include epithelial, trophoblast, cardiomyocyte and late-spermatid categories rather than a coherent brain- or ovary-specific population. This supports a broadly expressed housekeeping-like ER and membrane program shared across cell types, while leaving open the possibility that variable cell composition contributes to the co-abundance pattern. The evidence does not support interpreting the module primarily as a plasma-protein or blood-contamination module.

**GO/KEGG enrichment**: 6 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC endoplasmic reticulum membrane | 0.000119 | CANX, CKAP4, DDOST, EMC1, GNAI3, MOGS, SEC63, SPTLC1, TMEM214 |
| GO:CC endoplasmic reticulum subcompartment | 0.000119 | CANX, CKAP4, DDOST, EMC1, GNAI3, MOGS, SEC63, SPTLC1, TMEM214 |
| GO:CC nuclear outer membrane-endoplasmic reticulum membrane network | 0.000133 | CANX, CKAP4, DDOST, EMC1, GNAI3, MOGS, SEC63, SPTLC1, TMEM214 |
| GO:CC organelle subcompartment | 0.000879 | CANX, CKAP4, DDOST, EMC1, GNAI3, MOGS, SEC63, SPTLC1, TMEM214 |
| KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human) | 0.00246 | CANX, CKAP4, DDOST, MOGS, SEC63 |
| GO:CC endoplasmic reticulum | 0.00953 | CANX, CKAP4, DDOST, EMC1, GNAI3, MOGS, SEC63, SPTLC1, TMEM214 |

### STRING and hu.MAP

STRING supports a known ER-centered core rather than an entirely disconnected gene set. CANX has high-confidence links to DDOST, EMC1, MOGS and SEC63; DDOST links to EMC1 and MOGS; and SEC63 links to TMEM214. These relationships are concordant with the ER-processing interpretation and include a particularly coherent CANX–MOGS–DDOST axis, alongside EMC1 and SEC63 connections. The STRING supplementary terms (STRING Keyword Transmembrane helix; within-query FDR = 1.42e-05) through (STRING NetworkNeighborAL Mixed, incl. Endoplasmic reticulum protein-containing complex, and Cotranslational protein targeting to membrane; within-query FDR = 0.0205) independently emphasize membrane localization, ER membrane, rough ER, protein-containing complexes, cotranslational targeting and ER protein processing. They are supportive annotations, not globally corrected enrichment evidence. No hu.MAP complex contains at least two module members, so the module is not reproduced as a defined hu.MAP complex. The sparse co-abundance topology, together with the concentrated STRING links, suggests a connected functional backbone with peripheral genes rather than a fully documented physical complex.

**STRING interactions (score >= 0.7)**: 7 of 66 gene pairs: CANX–DDOST (0.886); CANX–EMC1 (0.854); CANX–MOGS (0.952); CANX–SEC63 (0.713); DDOST–EMC1 (0.818); DDOST–MOGS (0.974); SEC63–TMEM214 (0.723)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transmembrane helix (FDR = 1.42e-05, 10 genes); Keyword Membrane (FDR = 5.36e-05, 12 genes); Component Endoplasmic reticulum membrane (FDR = 0.00041, 8 genes); Component Integral component of membrane (FDR = 0.00041, 10 genes); KEGG Protein processing in endoplasmic reticulum (FDR = 0.00046, 5 genes); Component Endoplasmic reticulum protein-containing complex (FDR = 0.0015, 4 genes); COMPARTMENTS Endoplasmic reticulum (FDR = 0.0019, 8 genes); COMPARTMENTS Endoplasmic reticulum membrane (FDR = 0.0019, 6 genes); COMPARTMENTS Endoplasmic reticulum subcompartment (FDR = 0.0019, 6 genes); Keyword Endoplasmic reticulum (FDR = 0.0021, 7 genes); COMPARTMENTS Membrane (FDR = 0.0036, 11 genes); Component Rough endoplasmic reticulum (FDR = 0.0057, 3 genes); Component Organelle membrane (FDR = 0.0057, 10 genes); RCTM Maturation of spike protein (FDR = 0.0184, 3 genes); NetworkNeighborAL Mixed, incl. Endoplasmic reticulum protein-containing complex, and Cotranslational protein targeting to membrane (FDR = 0.0205, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The biological theme is not new: ER folding, glycosylation, translocation and membrane insertion are established functions, and several module relationships are already represented in STRING. The absence of a hu.MAP complex and the limited STRING connectivity for some peripheral genes do not prove novelty. What may be novel is the recurrence of this particular co-abundance module across brain and ovary, including the way a well-known ER core covaries with PVR, PLXNB2, GNAI3, ACADVL, SPTLC1 and TMEM214. That module-level cross-tissue organization should be described as a candidate observation rather than a demonstrated new mechanism. Independent replication, preservation testing, cell-composition adjustment, and comparison with existing cross-tissue co-expression resources would be needed before claiming a new conserved module.

**Hypothesis.** Hypothesis: in both brain and ovary, a shared demand for synthesis, folding, glycosylation and membrane insertion of proteins generates coordinated expression of an ER proteostasis program. CANX, MOGS and DDOST could form the functional processing backbone, with SEC63 supporting ER translocation and EMC1 supporting membrane-protein insertion. SPTLC1 may couple this program to sphingolipid production, while PVR and PLXNB2 may connect ER capacity to cell-surface adhesion, receptor signaling and trafficking; GNAI3 could connect membrane signaling to downstream responses, and ACADVL could reflect linked energetic requirements. TMEM214 may mark an ER-to-Golgi or stress-associated membrane component. This is a mechanistic hypothesis, not a causal conclusion: co-abundance cannot establish that these proteins physically act together or that one regulates the others.

### Important genes

#### CANX

- **Related proteins** (co-abundance neighbors): TMEM214 (0.86), CKAP4 (0.82), MOGS (0.81), SEC63 (0.81), GNAI3 (0.80); STRING partners: DDOST (0.886), EMC1 (0.854), MOGS (0.952), SEC63 (0.713)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is the highest-connectivity hub in the module and links the principal ER-associated neighbors. It appears in every globally corrected GO/KEGG term, every listed STRING supplementary term, and has high-confidence STRING links to DDOST, EMC1 and MOGS. Its established calnexin function in N-linked glycoprotein folding, ER quality control and ER-associated degradation makes it the clearest functional anchor. Its large literature volume and disease links to neurodegenerative and viral diseases also make it a strong translational entry point.
- **Conclusion**: Established: CANX is a central ER chaperone and the strongest network-supported marker of the module's proteostasis function. Hypothesis: variation in CANX abundance may help coordinate the broader module across brain and ovary, but this regulatory role is not demonstrated by the co-abundance data.

#### MOGS

- **Related proteins** (co-abundance neighbors): EMC1 (0.83), CANX (0.81), DDOST (0.80); STRING partners: CANX (0.952), DDOST (0.974)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosyl-oligosaccharide glucosidase. This gene encodes the first enzyme in the N-linked oligosaccharide processing pathway. The enzyme cleaves the distal alpha-1,2-linked glucose residue from the Glc(3)-Man(9)-GlcNAc(2) oligosaccharide precursor. This protein is located in the lumen of the endoplasmic reticulum. Defects in this gene are a cause of type IIb congenital disorder of glycosylation (CDGIIb). Two transcript variants encodin…
- **Diseases (Open Targets)**: MOGS-congenital disorder of glycosylation (0.818); congenital disorder of glycosylation (0.374); congenital disorder of glycosylation type II (0.370); severe acute respiratory syndrome (0.370); SRD5A3-congenital disorder of glycosylation (0.370)
- **Europe PMC papers**: 987
- **Why important**: MOGS is embedded in the global ER cellular-component terms and the ER protein-processing pathway (GO:CC endoplasmic reticulum membrane; q_global = 0.000119) through (GO:CC endoplasmic reticulum; q_global = 0.00953), and it has especially strong STRING links to CANX and DDOST. Its established role as the first enzyme in ER N-linked oligosaccharide processing gives the module a concrete glycan-processing mechanism. Its congenital disorder of glycosylation association provides a direct disease connection, while its substantial literature supports interpretation beyond a purely computational association.
- **Conclusion**: Established: MOGS provides enzymatic evidence that the module includes N-linked glycan maturation within the ER. Hypothesis: MOGS may be a rate-sensitive contributor to coordinated glycoprotein quality control in both tissues, but module data do not establish altered glycosylation flux.

#### DDOST

- **Related proteins** (co-abundance neighbors): SPTLC1 (0.81), MOGS (0.80); STRING partners: CANX (0.886), EMC1 (0.818), MOGS (0.974)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dolichyl-diphosphooligosaccharide--protein glycosyltransferase non-catalytic subunit. This gene encodes a component of the oligosaccharyltransferase complex which catalyzes the transfer of high-mannose oligosaccharides to asparagine residues on nascent polypeptides in the lumen of the rough endoplasmic reticulum. The protein complex co-purifies with ribosomes. The product of this gene is also implicated in the processing of advanced glycation endproducts (AGEs), which form from non…
- **Diseases (Open Targets)**: DDOST-congenital disorder of glycosylation (0.734); young-onset Parkinson disease (0.561); neurodegenerative disease (0.539); dengue disease (0.505); congenital disorder of glycosylation (0.373)
- **Europe PMC papers**: 685
- **Why important**: DDOST is a member of the globally significant ER terms and the ER protein-processing pathway, and it connects in STRING to CANX, EMC1 and MOGS. Its established role as a non-catalytic oligosaccharyltransferase component places it at the interface between nascent-protein synthesis and N-linked glycosylation. Its disease associations include congenital glycosylation disorders and neurodegenerative disease, making it relevant to both the module's biochemical interpretation and the brain context.
- **Conclusion**: Established: DDOST supports cotranslational glycosylation and strengthens the interpretation of a coordinated ER biosynthetic apparatus. Hypothesis: DDOST may couple the abundance of nascent client proteins to the rest of the module, but physical coupling within this tissue-pair module remains unproven.

#### SEC63

- **Related proteins** (co-abundance neighbors): CANX (0.81); STRING partners: CANX (0.713), TMEM214 (0.723)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC63 protein translocation regulator. The Sec61 complex is the central component of the protein translocation apparatus of the endoplasmic reticulum (ER) membrane. The protein encoded by this gene and SEC62 protein are found to be associated with ribosome-free SEC61 complex. It is speculated that Sec61-Sec62-Sec63 may perform post-translational protein translocation into the ER. The Sec61-Sec62-Sec63 complex might also perform the bac…
- **Diseases (Open Targets)**: autosomal dominant polycystic liver disease (0.795); neurodegenerative disease (0.526); polycystic liver disease 1 (0.430); Biliary tract abnormality (0.346); placental abruption (0.232)
- **Europe PMC papers**: 1756
- **Why important**: SEC63 is present in all globally corrected terms and in nearly all supplementary ER annotations. Its established role in ER protein targeting and translocation complements the folding and glycosylation functions of CANX, MOGS and DDOST. Its network links to CANX and TMEM214, together with substantial literature and disease associations involving polycystic liver disease and neurodegeneration, make it an important bridge between ER entry and downstream quality control.
- **Conclusion**: Established: SEC63 represents the ER translocation arm of the module. Hypothesis: coordinated SEC63 abundance could regulate the supply of proteins entering the folding and glycosylation network, but causality and direction cannot be inferred here.

#### EMC1

- **Related proteins** (co-abundance neighbors): MOGS (0.83), PLXNB2 (0.80); STRING partners: CANX (0.854), DDOST (0.818)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ER membrane protein complex subunit 1. This gene encodes a single-pass type I transmembrane protein, which is a subunit of the endoplasmic reticulum membrane protein complex (EMC). Multiple alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2012].
- **Diseases (Open Targets)**: cerebellar atrophy, visual impairment, and psychomotor retardation; (0.769); hereditary disease (0.497); inherited retinal dystrophy (0.487); Global developmental delay (0.411); Cerebellar atrophy (0.410)
- **Europe PMC papers**: 416
- **Why important**: EMC1 is included in the globally corrected ER cellular-component terms and is linked by STRING to CANX and DDOST. Its established function as an ER membrane complex subunit involved in membrane-protein insertion expands the module beyond soluble glycoprotein processing. Its association with cerebellar atrophy, visual impairment, psychomotor retardation and inherited retinal disease gives it particular relevance to nervous-system biology, despite its low tissue specificity.
- **Conclusion**: Established: EMC1 contributes an ER membrane-insertion component and connects membrane biogenesis with proteostasis. Hypothesis: EMC1 may help explain why the conserved module is observed in both neural and reproductive tissues, but tissue-specific functional consequences require experimental testing.

#### SPTLC1

- **Related proteins** (co-abundance neighbors): DDOST (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine palmitoyltransferase long chain base subunit 1. This gene encodes a member of the class-II pyridoxal-phosphate-dependent aminotransferase family. The encoded protein is the long chain base subunit 1 of serine palmitoyltransferase. Serine palmitoyltransferase converts L-serine and palmitoyl-CoA to 3-oxosphinganine with pyridoxal 5'-phosphate and is the key enzyme in sphingolipid biosynthesis. Mutations in this gene were identified in patients wi…
- **Diseases (Open Targets)**: neuropathy, hereditary sensory and autonomic, type 1A (0.702); hereditary sensory and autonomic neuropathy type 1 (0.667); amyotrophic lateral sclerosis 27, juvenile (0.632); Charcot-Marie-Tooth disease (0.582); hereditary sensory and autonomic neuropathy type 2 (0.462)
- **Europe PMC papers**: 1351
- **Why important**: SPTLC1 is included in the globally corrected ER terms and in several supplementary ER and membrane annotations, and it is connected to DDOST in the module. Its established role as the long-chain-base subunit of serine palmitoyltransferase makes it the clearest link to sphingolipid and membrane-lipid biosynthesis. Its hereditary sensory neuropathy and motor-neuron disease associations give it strong relevance to brain biology and provide a disease-linked complement to the ER proteostasis core.
- **Conclusion**: Established: SPTLC1 connects ER membrane organization with sphingolipid synthesis and is independently relevant to neurological disease. Hypothesis: SPTLC1 may couple lipid supply to ER membrane and protein-processing demands in the shared module, but this coupling is not demonstrated by the available network.

## Module 5

**Tissue pair**: brain and ovary  
**Genes (8)**: ACIN1, BCLAF1, ADAR, CLINT1, IGF2BP3, RBM10, RPL12, SRSF7

### Function

The module is most strongly characterized as an RNA regulation and pre-mRNA processing module. The primary evidence is the globally corrected enrichment for negative regulation of mRNA metabolic process (GO:BP negative regulation of mRNA metabolic process; q_global = 0.000684), negative regulation of mRNA splicing through the spliceosome (GO:BP negative regulation of mRNA splicing, via spliceosome; q_global = 0.00115), negative regulation of mRNA processing (GO:BP negative regulation of mRNA processing; q_global = 0.00115), negative regulation of RNA splicing (GO:BP negative regulation of RNA splicing; q_global = 0.00361), mRNA metabolic process (GO:BP mRNA metabolic process; q_global = 0.0164), and negative regulation of gene expression (GO:BP negative regulation of gene expression; q_global = 0.0177). ACIN1, RBM10, and SRSF7 recur across the splicing-related terms, while ADAR, BCLAF1, and IGF2BP3 broaden the module toward RNA editing, RNA-associated regulation, transcript stability, and gene-expression control. The STRING annotations independently support RNA binding, RNA-recognition-motif biology, and RNA metabolism (11 supplementary STRING terms; within-query FDR 0.0015–0.0469), but remain supplementary rather than globally corrected evidence. RPL12 and CLINT1 may represent translational or vesicle-trafficking links, although their presence does not overturn the dominant RNA-processing interpretation.

**Cell composition.** This is not a plasma-protein or secreted-protein module: no member is annotated as secreted, and the encoded proteins are predominantly intracellular, with nuclear, nucleolar, nuclear-speckle, cytosolic, Golgi, or vesicular locations. HPA detects the proteins broadly in brain and nearly uniformly in ovary, which supports biological detectability in both tissues. Most members have low tissue specificity and low immune-cell specificity, so the module is more consistent with a broadly reusable intracellular program than with a blood-contamination signature. Some cell-type-enhanced annotations occur, including neutrophil-related, trophoblast-related, epithelial, and lactating-cell contexts, and CLINT1 is immune-cell enriched for basophils; these observations warrant attention to cell composition, but they do not establish that blood or a shared immune population drives the brain-ovary module.

**GO/KEGG enrichment**: 6 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP negative regulation of mRNA metabolic process | 0.000684 | ACIN1, IGF2BP3, RBM10, SRSF7 |
| GO:BP negative regulation of mRNA splicing, via spliceosome | 0.00115 | ACIN1, RBM10, SRSF7 |
| GO:BP negative regulation of mRNA processing | 0.00115 | ACIN1, RBM10, SRSF7 |
| GO:BP negative regulation of RNA splicing | 0.00361 | ACIN1, RBM10, SRSF7 |
| GO:BP mRNA metabolic process | 0.0164 | ACIN1, ADAR, BCLAF1, IGF2BP3, RBM10, SRSF7 |
| GO:BP negative regulation of gene expression | 0.0177 | ACIN1, ADAR, BCLAF1, IGF2BP3, RBM10, SRSF7 |

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module members. Thus, the co-abundance relationships are not simply reproduced as established direct protein-interaction edges in STRING, and the network should not be interpreted as a validated physical complex. In contrast, hu.MAP repeatedly places SRSF7, BCLAF1, and ACIN1 together in spliceosome-, exon-junction-, RNA-processing-, and related nuclear complexes (hu.MAP huMAP3_06097.1) (hu.MAP huMAP3_10564.1) (hu.MAP huMAP3_11073.1) (hu.MAP huMAP3_09943.1) (hu.MAP huMAP3_06391.1) (hu.MAP huMAP3_07267.1) (hu.MAP huMAP3_09621.1). This is meaningful support for a shared RNA-processing neighborhood, although these genes are only subsets of much larger complexes and hu.MAP co-membership does not prove that every module edge is physical. The combination of absent STRING edges and repeated hu.MAP co-membership suggests that the module captures coordinated abundance of components or regulators associated with RNA processing, rather than a compact, fully resolved protein complex.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Process Negative regulation of mRNA metabolic process (FDR = 0.0015, 4 genes); Keyword RNA-binding (FDR = 0.0025, 6 genes); SMART RNA recognition motif (FDR = 0.0037, 4 genes); Process Negative regulation of gene expression (FDR = 0.0058, 6 genes); Process Negative regulation of mRNA splicing, via spliceosome (FDR = 0.0058, 3 genes); InterPro RNA recognition motif domain (FDR = 0.0225, 4 genes); InterPro Nucleotide-binding alpha-beta plait domain superfamily (FDR = 0.0225, 4 genes); InterPro RNA-binding domain superfamily (FDR = 0.0225, 4 genes); RCTM Metabolism of RNA (FDR = 0.0234, 6 genes); Process mRNA processing (FDR = 0.0294, 5 genes); Keyword mRNA processing (FDR = 0.0469, 4 genes); Keyword Isopeptide bond (FDR = 0.0469, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06097.1 (SRSF7, BCLAF1, ACIN1; 3/22); huMAP3_10564.1 (SRSF7, BCLAF1, ACIN1; 3/37); huMAP3_11073.1 (SRSF7, BCLAF1, ACIN1; 3/67); huMAP3_09943.1 (SRSF7, BCLAF1, ACIN1; 3/78); huMAP3_06391.1 (SRSF7, BCLAF1; 2/16); huMAP3_07267.1 (SRSF7, BCLAF1; 2/16); huMAP3_09621.1 (SRSF7, ACIN1; 2/56)

### Novelty

The module may be novel as a conserved brain-ovary co-abundance pattern and as a particular combination of RNA-processing, RNA-editing, transcript-binding, translation, and trafficking genes. However, it is not novel in the sense that its individual functions are unknown: the RNA-processing roles of ACIN1, RBM10, SRSF7, ADAR, BCLAF1, and IGF2BP3 are established, and the repeated hu.MAP associations among ACIN1, BCLAF1, and SRSF7 show prior complex-level knowledge. The absence of STRING interactions does not prove novelty, because co-abundance can reflect shared regulation, cell state, localization, or indirect pathway coupling. A defensible novelty claim therefore requires replication across independent cohorts, preservation after cell-composition adjustment, and comparison with published cross-tissue co-expression modules.

**Hypothesis.** Hypothesis: the conserved module reflects a shared intracellular RNA-homeostasis program operating in brain and ovary. Coordinated abundance of spliceosome-associated regulators may tune alternative splicing and transcript processing, while ADAR could alter RNA sequence or duplex stability, IGF2BP3 could influence selected transcript fate, and BCLAF1 and ACIN1 could connect RNA processing with nuclear stress or apoptotic-state regulation. RPL12 and CLINT1 may couple this program to translation and vesicle trafficking. This is a mechanistic hypothesis, not a demonstrated pathway: the co-abundance network and enrichment establish coordinated association, whereas causality, directionality, and tissue-specific regulation require perturbation and transcript- or protein-level validation.

### Important genes

#### ACIN1

- **Related proteins** (co-abundance neighbors): BCLAF1 (0.87), ADAR (0.86), RBM10 (0.83), IGF2BP3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_06097.1, huMAP3_10564.1, huMAP3_11073.1, huMAP3_09943.1, huMAP3_09621.1
- **Function (MyGene.info)**: apoptotic chromatin condensation inducer 1. Apoptosis is defined by several morphologic nuclear changes, including chromatin condensation and nuclear fragmentation. This gene encodes a nuclear protein that induces apoptotic chromatin condensation after activation by caspase-3, without inducing DNA fragmentation. This protein has also been shown to be a component of a splicing-dependent multiprotein exon junction complex (EJC) that is deposi…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); adolescent idiopathic scoliosis (0.090); hepatocellular carcinoma (0.076); acute lymphoblastic leukemia (0.074); pancreatic neoplasm (0.045)
- **Europe PMC papers**: 894
- **Why important**: ACIN1 is the strongest network hub in the module, connecting BCLAF1, ADAR, RBM10, and IGF2BP3. It appears in every globally corrected GO term (6 globally significant GO/KEGG terms, q_global 0.000684–0.0177; see the table), all listed STRING supplementary terms, and the repeated hu.MAP complexes (hu.MAP huMAP3_06097.1) (hu.MAP huMAP3_10564.1) (hu.MAP huMAP3_11073.1) (hu.MAP huMAP3_09943.1) (hu.MAP huMAP3_09621.1). Its established functions link apoptotic chromatin condensation with RNA splicing and the exon-junction complex. It also has substantial literature coverage and disease associations including neurodegenerative disease.
- **Conclusion**: Established evidence supports ACIN1 as a central integrator of RNA processing and nuclear apoptotic biology. It is plausible, but not proven, that ACIN1 helps coordinate the conserved module across brain and ovary.

#### SRSF7

- **Related proteins** (co-abundance neighbors): IGF2BP3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_06097.1, huMAP3_10564.1, huMAP3_11073.1, huMAP3_09943.1, huMAP3_06391.1, huMAP3_07267.1, huMAP3_09621.1
- **Function (MyGene.info)**: serine and arginine rich splicing factor 7. The protein encoded by this gene is a member of the serine/arginine (SR)-rich family of pre-mRNA splicing factors, which constitute part of the spliceosome. Each of these factors contains an N-terminal RNA recognition motif (RRM) for binding RNA and a C-terminal RS domain for binding other proteins. The RS domain is rich in serine and arginine residues and facilitates interaction between different…
- **Diseases (Open Targets)**: neurodegenerative disease (0.536); dengue disease (0.370); cystitis (0.221); smoking initiation (0.107); neoplasm (0.082)
- **Europe PMC papers**: 1327
- **Why important**: SRSF7 is a canonical serine- and arginine-rich splicing factor with a direct role in spliceosomal and alternative mRNA splicing regulation. It occurs in all globally corrected terms (6 globally significant GO/KEGG terms, q_global 0.000684–0.0177; see the table), all listed STRING supplementary terms, and every hu.MAP complex reported for this module (hu.MAP huMAP3_06097.1) (hu.MAP huMAP3_10564.1) (hu.MAP huMAP3_11073.1) (hu.MAP huMAP3_09943.1) (hu.MAP huMAP3_06391.1) (hu.MAP huMAP3_07267.1) (hu.MAP huMAP3_09621.1). Its repeated presence across large RNA-processing complexes makes it a strong representative of the module's core splicing biology.
- **Conclusion**: Established evidence identifies SRSF7 as a core spliceosome-associated regulator and a likely anchor of the module's RNA-processing interpretation. Its specific contribution to the brain-ovary conservation remains a hypothesis.

#### RBM10

- **Related proteins** (co-abundance neighbors): ACIN1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 10. This gene encodes a nuclear protein that belongs to a family proteins that contain an RNA-binding motif. The encoded protein associates with hnRNP proteins and may be involved in regulating alternative splicing. Defects in this gene are the cause of the X-linked recessive disorder, TARP syndrome. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Mar 2011].
- **Diseases (Open Targets)**: TARP syndrome (0.787); lung adenocarcinoma (0.629); neurodegenerative disease (0.526); pancreatic adenocarcinoma (0.513); non-small cell lung carcinoma (0.510)
- **Europe PMC papers**: 1601
- **Why important**: RBM10 is directly represented in all globally corrected terms (6 globally significant GO/KEGG terms, q_global 0.000684–0.0177; see the table) and in nearly all RNA-binding and splicing-related STRING annotations (10 supplementary STRING terms; within-query FDR 0.0015–0.0469). It is an RNA-binding protein associated with alternative-splicing regulation, is positioned next to the central ACIN1 hub, and has established disease relevance through TARP syndrome and cancer associations. Its combination of strong annotation support and focused network placement makes it an informative regulatory component.
- **Conclusion**: Established evidence supports RBM10 as a likely transcript-splicing regulator within the module. The network does not establish which transcripts it controls in either tissue, so tissue-specific target selection remains a hypothesis.

#### ADAR

- **Related proteins** (co-abundance neighbors): ACIN1 (0.86), BCLAF1 (0.82), CLINT1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR contributes to the globally corrected mRNA metabolic and negative gene-expression terms (GO:BP mRNA metabolic process; q_global = 0.0164) (GO:BP negative regulation of gene expression; q_global = 0.0177), connects directly to ACIN1 and BCLAF1 in the module, and is annotated as the enzyme responsible for adenosine-to-inosine RNA editing. It has extensive literature coverage and strong disease associations involving Aicardi-Goutieres syndrome, interferonopathy, and dyschromatosis symmetrica hereditaria. Its RNA-editing activity adds a mechanistic layer beyond splicing.
- **Conclusion**: Established evidence supports ADAR as an RNA-editing enzyme that could broaden the module from splicing control to RNA surveillance and transcript remodeling. Its placement does not prove that RNA editing drives the shared brain-ovary pattern.

#### BCLAF1

- **Related proteins** (co-abundance neighbors): ACIN1 (0.87), ADAR (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_06097.1, huMAP3_10564.1, huMAP3_11073.1, huMAP3_09943.1, huMAP3_06391.1, huMAP3_07267.1
- **Function (MyGene.info)**: BCL2 associated transcription factor 1. This gene encodes a transcriptional repressor that interacts with several members of the BCL2 family of proteins. Overexpression of this protein induces apoptosis, which can be suppressed by co-expression of BCL2 proteins. The protein localizes to dot-like structures throughout the nucleus, and redistributes to a zone near the nuclear envelope in cells undergoing apoptosis. Multiple transcript var…
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); Pulmonary artery atresia (0.416); acute myeloid leukemia (0.357); bronchial disorder (0.288); Vertigo (0.253)
- **Europe PMC papers**: 1702
- **Why important**: BCLAF1 is present in the globally corrected mRNA metabolic and negative gene-expression terms (GO:BP mRNA metabolic process; q_global = 0.0164) (GO:BP negative regulation of gene expression; q_global = 0.0177), connects to ACIN1 and ADAR, and co-occurs with SRSF7 and ACIN1 across the hu.MAP complexes (hu.MAP huMAP3_06097.1) (hu.MAP huMAP3_10564.1) (hu.MAP huMAP3_11073.1) (hu.MAP huMAP3_09943.1) (hu.MAP huMAP3_06391.1) (hu.MAP huMAP3_07267.1). It is a nuclear-speckle protein with established links to transcriptional repression, mRNA stabilization, DNA-damage response, and apoptosis. Its network and complex placement make it a plausible bridge between RNA regulation and cell-state control.
- **Conclusion**: Established evidence supports BCLAF1 as a nuclear regulator connecting RNA metabolism with transcriptional and apoptotic programs. Its role as a bridge in this conserved module is a plausible but untested interpretation.

## Module 6

**Tissue pair**: brain and ovary  
**Genes (22)**: ACO2, AIFM1, ATP1A1, ATP2A2, ATP5F1A, ATP5F1B, ALCAM, CPT2, DGLUCY, HIBCH, IDH3A, IVD, IMMT, NDUFA10, NDUFS7, PCCB, PITRM1, UQCRC1, UQCRC2, RMDN3, DARS2, IARS2

### Function

This is a mitochondrial oxidative-energy module. The strongest primary evidence is the broad mitochondrial and mitochondrial-matrix enrichment (GO:CC mitochondrion; q_global = 7.72e-07)(GO:CC mitochondrial matrix; q_global = 3.51e-06), together with mitochondrial membrane, inner-membrane, envelope, and respiratory-chain annotations (GO:CC mitochondrial membrane; q_global = 2.37e-05)(GO:CC mitochondrial envelope; q_global = 6.52e-05)(GO:CC respiratory chain complex; q_global = 0.000337)(GO:CC mitochondrial inner membrane; q_global = 0.000693)(GO:CC organelle inner membrane; q_global = 0.00125). The module also supports aerobic respiration, cellular respiration, oxidative phosphorylation, electron transport, proton transmembrane transport, and ATP biosynthesis (KEGG Oxidative phosphorylation - Homo sapiens (human); q_global = 0.000628)(GO:BP aerobic respiration; q_global = 0.000774)(GO:BP proton transmembrane transport; q_global = 0.000939)(GO:BP oxidative phosphorylation; q_global = 0.00152)(GO:BP cellular respiration; q_global = 0.00172)(GO:BP generation of precursor metabolites and energy; q_global = 0.011)(GO:BP proton motive force-driven mitochondrial ATP synthesis; q_global = 0.0217)(GO:BP aerobic electron transport chain; q_global = 0.0345)(GO:BP ATP biosynthetic process; q_global = 0.045). Its genes span the TCA cycle and related intermediary metabolism, respiratory-chain complexes, ATP synthase, mitochondrial protein organization, amino-acid catabolism, and mitochondrial translation. The transporter terms (GO:CC transmembrane transporter complex; q_global = 3.64e-05)(GO:CC transporter complex; q_global = 5.01e-05)(GO:MF active monoatomic ion transmembrane transporter activity; q_global = 0.000398)(GO:MF monoatomic cation transmembrane transporter activity; q_global = 0.000436)(GO:MF primary active transmembrane transporter activity; q_global = 0.00106)(GO:MF monoatomic ion transmembrane transporter activity; q_global = 0.00119) reflect ATP1A1, ATP2A2, and ATP synthase-associated transport functions, rather than indicating that the module is primarily a plasma-membrane transporter module. Disease pathway labels such as diabetic cardiomyopathy, neurodegeneration, Alzheimer disease, Parkinson disease, and prion disease (KEGG Diabetic cardiomyopathy - Homo sapiens (human); q_global = 1.97e-05)(KEGG Chemical carcinogenesis - reactive oxygen species - Homo sapiens (human); q_global = 0.00433)(KEGG Alzheimer disease - Homo sapiens (human); q_global = 0.0052)(KEGG Prion disease - Homo sapiens (human); q_global = 0.0135)(KEGG Pathways of neurodegeneration - multiple diseases - Homo sapiens (human); q_global = 0.0145)(KEGG Parkinson disease - Homo sapiens (human); q_global = 0.0155) should be interpreted as shared mitochondrial and energetic biology, not as evidence that the module specifically causes any of those diseases.

**Cell composition.** The module is overwhelmingly composed of intracellular mitochondrial or mitochondria-associated proteins, with no indication of a plasma-protein or broadly secreted-protein program. HPA reports only ALCAM as secreted to blood, while the other annotated proteins are non-secreted; most have mitochondrial locations or mitochondrial functions. The HPA profile is not strongly blood-cell driven: most genes have low immune-cell specificity, with only a small minority showing immune-cell enhancement. The tissue and single-cell patterns include muscle, heart, tongue, liver, enterocytes, parietal cells, germ-cell populations, oocytes, and cardiomyocytes, which is compatible with metabolically active cells rather than a uniform brain-ovary-specific lineage. Protein detection is widespread in brain and more variable in ovary, so the shared module may primarily report conserved cellular energy demand and mitochondrial abundance. ALCAM is a plausible cell-adhesion or tissue-interface component, but it is not sufficient to reclassify the module as secreted or immune-cell derived.

**GO/KEGG enrichment**: 44 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrion | 7.72e-07 | ACO2, AIFM1, ATP5F1A, ATP5F1B, CPT2, DARS2, DGLUCY, HIBCH, IARS2, IDH3A, IMMT, IVD, NDUFA10, NDUFS7, PCCB, PITRM1, RMDN3, UQCRC1, UQCRC2 |
| GO:CC mitochondrial matrix | 3.51e-06 | ACO2, ATP5F1A, ATP5F1B, DARS2, DGLUCY, HIBCH, IARS2, IDH3A, IVD, NDUFA10, NDUFS7, PCCB, PITRM1 |
| KEGG Diabetic cardiomyopathy - Homo sapiens (human) | 1.97e-05 | ATP2A2, ATP5F1A, ATP5F1B, CPT2, NDUFA10, NDUFS7, UQCRC1, UQCRC2 |
| GO:CC mitochondrial membrane | 2.37e-05 | AIFM1, ATP5F1A, ATP5F1B, CPT2, DARS2, IMMT, IVD, NDUFA10, NDUFS7, RMDN3, UQCRC1, UQCRC2 |
| GO:CC transmembrane transporter complex | 3.64e-05 | ATP1A1, ATP2A2, ATP5F1A, ATP5F1B, NDUFA10, NDUFS7, UQCRC1, UQCRC2 |
| GO:CC transporter complex | 5.01e-05 | ATP1A1, ATP2A2, ATP5F1A, ATP5F1B, NDUFA10, NDUFS7, UQCRC1, UQCRC2 |
| GO:CC mitochondrial envelope | 6.52e-05 | AIFM1, ATP5F1A, ATP5F1B, CPT2, DARS2, IMMT, IVD, NDUFA10, NDUFS7, RMDN3, UQCRC1, UQCRC2 |
| GO:CC respiratory chain complex | 0.000337 | ATP5F1A, ATP5F1B, NDUFA10, NDUFS7, UQCRC1, UQCRC2 |
| GO:MF active monoatomic ion transmembrane transporter activity | 0.000398 | ATP1A1, ATP2A2, ATP5F1B, NDUFA10, NDUFS7, UQCRC1 |
| GO:MF monoatomic cation transmembrane transporter activity | 0.000436 | ATP1A1, ATP2A2, ATP5F1A, ATP5F1B, NDUFA10, NDUFS7, UQCRC1 |
| KEGG Oxidative phosphorylation - Homo sapiens (human) | 0.000628 | ATP5F1A, ATP5F1B, NDUFA10, NDUFS7, UQCRC1, UQCRC2 |
| KEGG Thermogenesis - Homo sapiens (human) | 0.000652 | ATP5F1A, ATP5F1B, CPT2, NDUFA10, NDUFS7, UQCRC1, UQCRC2 |
| GO:CC mitochondrial inner membrane | 0.000693 | AIFM1, ATP5F1A, ATP5F1B, CPT2, IMMT, NDUFA10, NDUFS7, UQCRC1, UQCRC2 |
| GO:BP aerobic respiration | 0.000774 | ACO2, ATP5F1A, ATP5F1B, IDH3A, NDUFA10, NDUFS7, UQCRC1, UQCRC2 |
| GO:BP proton transmembrane transport | 0.000939 | ATP1A1, ATP5F1A, ATP5F1B, NDUFA10, NDUFS7, UQCRC1 |

### STRING and hu.MAP

STRING provides strong, biologically coherent relationships among respiratory-chain and ATP-synthase genes, including the ATP5F1A–ATP5F1B pair, the NDUFA10–NDUFS7 pair, the UQCRC1–UQCRC2 pair, and links connecting these groups to ACO2, IDH3A, IMMT, and other mitochondrial proteins. It also supports substrate and intermediary-metabolism relationships such as HIBCH–IVD, HIBCH–PCCB, and IVD–PCCB, and the mitochondrial aminoacyl-tRNA synthetase pair DARS2–IARS2. These are largely established biological associations, so the network is not an isolated or wholly uncharacterized interaction set. hu.MAP independently places module genes in respiratory-chain complexes, ATP synthase-related complexes, mitochondrial translation or amino-acid-metabolism assemblies, and complexes containing UQCRC1 and UQCRC2 (hu.MAP huMAP3_13468.1)(hu.MAP huMAP3_10473.1)(hu.MAP huMAP3_14018.1)(hu.MAP huMAP3_07245.1)(hu.MAP huMAP3_09668.1)(hu.MAP huMAP3_08546.1)(hu.MAP huMAP3_08750.1)(hu.MAP huMAP3_06397.1). Several complexes contain only a minority of their full membership, so hu.MAP supports modular embedding in known mitochondrial machinery rather than proving that the entire co-abundance module is a single physical complex. The distinction between STRING associations and hu.MAP complex membership is important: the former supports functional connectivity, whereas the latter provides partial physical-complex context.

**STRING interactions (score >= 0.7)**: 30 of 231 gene pairs: ACO2–ATP5F1A (0.884); ACO2–ATP5F1B (0.874); ACO2–HIBCH (0.878); ACO2–IDH3A (0.998); ACO2–NDUFA10 (0.747); ACO2–UQCRC1 (0.855); ACO2–UQCRC2 (0.879); ATP1A1–ATP2A2 (0.82); ATP5F1A–ATP5F1B (0.999); ATP5F1A–IDH3A (0.855); ATP5F1A–IMMT (0.809); ATP5F1A–NDUFA10 (0.759); ATP5F1A–UQCRC1 (0.97); ATP5F1A–UQCRC2 (0.986); ATP5F1B–IMMT (0.745); ATP5F1B–NDUFA10 (0.938); ATP5F1B–UQCRC1 (0.969); ATP5F1B–UQCRC2 (0.942); DARS2–IARS2 (0.895); HIBCH–IVD (0.704); HIBCH–PCCB (0.701); IDH3A–UQCRC2 (0.713); IMMT–UQCRC2 (0.811); IVD–PCCB (0.842); NDUFA10–NDUFS7 (0.999); NDUFA10–UQCRC1 (0.996); NDUFA10–UQCRC2 (0.986); NDUFS7–UQCRC1 (0.997); NDUFS7–UQCRC2 (0.98); UQCRC1–UQCRC2 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transit peptide (FDR = 3.2e-14, 18 genes); Keyword Mitochondrion (FDR = 4.57e-12, 19 genes); COMPARTMENTS Mitochondrion (FDR = 7.77e-11, 19 genes); Component Mitochondrion (FDR = 4.76e-09, 19 genes); Component Mitochondrial matrix (FDR = 1.36e-07, 13 genes); Component Mitochondrial membrane (FDR = 1.12e-05, 11 genes); COMPARTMENTS Mitochondrial protein complex (FDR = 1.14e-05, 9 genes); PMID (2023) AMPK activator-treated human cardiac spheres enhance maturation and enable pathological modeling. (FDR = 1.18e-05, 10 genes); Component Inner mitochondrial membrane protein complex (FDR = 1.47e-05, 7 genes); COMPARTMENTS Mitochondrial inner membrane (FDR = 1.61e-05, 9 genes); COMPARTMENTS Mitochondrial membrane (FDR = 1.61e-05, 10 genes); COMPARTMENTS Inner mitochondrial membrane protein complex (FDR = 1.67e-05, 7 genes); COMPARTMENTS Mitochondrial matrix (FDR = 1.9e-05, 10 genes); RCTM The citric acid (TCA) cycle and respiratory electron transport (FDR = 2.27e-05, 8 genes); PMID (2015) Evidence of Mitochondrial Dysfunction within the Complex Genetic Etiology of Schizophrenia. (FDR = 2.81e-05, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (NDUFS7, PCCB, CPT2, IVD, DARS2, IARS2; 6/99); huMAP3_10473.1 (ATP1A1, ATP2A2, ATP5F1A; 3/24); huMAP3_14018.1 (NDUFS7, NDUFA10, UQCRC1; 3/48); huMAP3_09982.1 (NDUFS7, NDUFA10, UQCRC1; 3/49); huMAP3_07245.1 (UQCRC2, ATP5F1A; 2/4); huMAP3_09668.1 (DARS2, IARS2; 2/8); huMAP3_12238.1 (HIBCH, ACO2; 2/9); huMAP3_08546.1 (UQCRC2, UQCRC1; 2/9); huMAP3_09600.1 (UQCRC2, UQCRC1; 2/9); huMAP3_08750.1 (ATP5F1B, ATP5F1A; 2/12); huMAP3_12621.1 (UQCRC2, UQCRC1; 2/22); huMAP3_10623.1 (UQCRC2, UQCRC1; 2/24); huMAP3_12457.1 (UQCRC2, UQCRC1; 2/31); huMAP3_10525.1 (DARS2, IARS2; 2/33); huMAP3_09307.1 (ATP5F1B, ATP5F1A; 2/35); huMAP3_11095.1 (ATP5F1B, ATP5F1A; 2/45); huMAP3_06397.1 (NDUFS7, NDUFA10; 2/49); huMAP3_09567.1 (NDUFS7, NDUFA10; 2/52); huMAP3_14878.1 (NDUFS7, NDUFA10; 2/53); huMAP3_06247.1 (ATP2A2, UQCRC2; 2/65)

### Novelty

The module should not be called a newly discovered mitochondrial pathway. Its central biology is already well established through annotated oxidative-phosphorylation genes, strong STRING links, and multiple hu.MAP complexes. The potentially new result is the coordinated co-abundance of this particular combination across brain and ovary, especially the joint placement of respiratory-chain, ATP-synthesis, TCA-cycle, substrate-catabolism, mitochondrial-translation, membrane-organization, and calcium or adhesion-related genes in a shared tissue-pair module. That cross-tissue co-abundance pattern is not demonstrated to be present in the supplied reference resources, but absence from STRING or hu.MAP alone cannot establish novelty. A defensible conclusion is therefore partial novelty: the component functions and many relationships are established, while the tissue-pair-level organization and its reproducibility require independent cohorts, preservation testing, cell-composition adjustment, and preferably experimental or longitudinal validation.

**Hypothesis.** Hypothesis: this shared module represents a conserved mitochondrial capacity program that coordinates substrate oxidation, respiratory-chain electron transfer, proton-gradient utilization, ATP production, mitochondrial membrane architecture, and quality control in energetically demanding brain and ovarian cells. The co-abundance of ACO2, IDH3A, CPT2, HIBCH, IVD, and PCCB could couple carbon and amino-acid or fatty-acid metabolism to respiratory demand, while NDUFA10, NDUFS7, UQCRC1, UQCRC2, ATP5F1A, and ATP5F1B could couple electron transport to ATP synthesis. IMMT could provide a structural link through cristae organization, and ATP1A1 and ATP2A2 could connect cellular ion and calcium handling to energy use. ALCAM may reflect tissue architecture or cell-state composition rather than a core mitochondrial mechanism. This remains a hypothesis: co-abundance does not establish direct regulation, physical interaction, or causal direction, and the pattern could partly reflect differences in mitochondrial content or the mixture of metabolically active cell types.

### Important genes

#### ATP5F1A

- **Related proteins** (co-abundance neighbors): ATP5F1B (0.87), AIFM1 (0.84), ACO2 (0.83), IMMT (0.82), HIBCH (0.80); STRING partners: ACO2 (0.884), ATP5F1B (0.999), IDH3A (0.855), IMMT (0.809), NDUFA10 (0.759), UQCRC1 (0.97), UQCRC2 (0.986)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_10473.1, huMAP3_07245.1, huMAP3_08750.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit alpha. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, using an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic po…
- **Diseases (Open Targets)**: mitochondrial complex V (ATP synthase) deficiency, nuclear type 4A (0.655); mitochondrial proton-transporting ATP synthase complex deficiency (0.648); mitochondrial complex V (ATP synthase) deficiency, nuclear type 4B (0.532); hereditary disease (0.394); Mitochondrial encephalopathy (0.371)
- **Europe PMC papers**: 822
- **Why important**: ATP5F1A is a central network connector and is annotated as the catalytic alpha subunit of mitochondrial ATP synthase. It participates in the mitochondrial, membrane, transporter, respiratory-chain, oxidative-phosphorylation, proton-motive-force, ATP-biosynthesis, and energy-related primary terms (GO:CC mitochondrion; q_global = 7.72e-07)(GO:CC mitochondrial matrix; q_global = 3.51e-06)(GO:CC mitochondrial membrane; q_global = 2.37e-05)(GO:CC respiratory chain complex; q_global = 0.000337)(KEGG Oxidative phosphorylation - Homo sapiens (human); q_global = 0.000628)(GO:BP aerobic respiration; q_global = 0.000774)(GO:BP oxidative phosphorylation; q_global = 0.00152)(GO:BP proton motive force-driven mitochondrial ATP synthesis; q_global = 0.0217)(GO:BP ATP biosynthetic process; q_global = 0.045). STRING links it strongly to ATP5F1B, ACO2, IDH3A, IMMT, NDUFA10, UQCRC1, and UQCRC2, and hu.MAP places it in several ATP-synthase-related complexes (hu.MAP huMAP3_10473.1)(hu.MAP huMAP3_07245.1)(hu.MAP huMAP3_08750.1)(hu.MAP huMAP3_09307.1)(hu.MAP huMAP3_11095.1). It is detected in both brain and ovary, and its disease associations include mitochondrial complex-V deficiency and mitochondrial encephalopathy. Its literature is substantial, supporting an established core role rather than a speculative marker.
- **Conclusion**: Established evidence identifies ATP5F1A as a central ATP-synthesis component and a plausible energetic hub of the module. The co-abundance data support its use as a representative module gene, but do not show that ATP5F1A drives the shared brain-ovary pattern.

#### NDUFA10

- **Related proteins** (co-abundance neighbors): DGLUCY (0.87), PCCB (0.84), RMDN3 (0.83), IMMT (0.81); STRING partners: ACO2 (0.747), ATP5F1A (0.759), ATP5F1B (0.938), NDUFS7 (0.999), UQCRC1 (0.996), UQCRC2 (0.986)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_09982.1, huMAP3_06397.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit A10. The protein encoded by this gene is a component of 42 kDa complex I, the first enzyme complex in the electron transport chain of mitochondria. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. A mutation in this gene was found in an individual with Leigh syndrome. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.677); Leigh syndrome (0.674); mitochondrial complex I deficiency, nuclear type 22 (0.668); type 2 diabetes mellitus (0.620); diabetes mellitus (0.578)
- **Europe PMC papers**: 1163
- **Why important**: NDUFA10 is a network connector linking DGLUCY, PCCB, RMDN3, IMMT, and the respiratory-chain group. It is a component of mitochondrial complex I and is annotated for NADH-to-ubiquinone electron transfer, aerobic respiration, proton transport, and proton-motive-force-driven ATP synthesis (GO:CC mitochondrion; q_global = 7.72e-07)(GO:CC mitochondrial matrix; q_global = 3.51e-06)(GO:CC mitochondrial membrane; q_global = 2.37e-05)(GO:CC respiratory chain complex; q_global = 0.000337)(KEGG Oxidative phosphorylation - Homo sapiens (human); q_global = 0.000628)(GO:BP aerobic respiration; q_global = 0.000774)(GO:BP oxidative phosphorylation; q_global = 0.00152)(GO:BP aerobic electron transport chain; q_global = 0.0345). STRING supports strong links to NDUFS7, UQCRC1, UQCRC2, and ATP synthase subunits. hu.MAP repeatedly places it with NDUFS7 and UQCRC1 in respiratory-chain assemblies (hu.MAP huMAP3_14018.1)(hu.MAP huMAP3_09982.1)(hu.MAP huMAP3_06397.1)(hu.MAP huMAP3_09567.1)(hu.MAP huMAP3_14878.1). It is detected in both brain and ovary, and its disease associations include complex-I deficiency, Leigh syndrome, and diabetes-related traits. Its literature is substantial.
- **Conclusion**: Established evidence supports NDUFA10 as an electron-transport and respiratory-chain anchor. Its placement in the module is consistent with coupling complex-I activity to downstream respiratory-chain and ATP-synthesis capacity; whether its abundance is functionally limiting in either tissue remains untested.

#### ACO2

- **Related proteins** (co-abundance neighbors): ATP1A1 (0.86), IMMT (0.84), ATP5F1A (0.83), IDH3A (0.82); STRING partners: ATP5F1A (0.884), ATP5F1B (0.874), HIBCH (0.878), IDH3A (0.998), NDUFA10 (0.747), UQCRC1 (0.855), UQCRC2 (0.879)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_12238.1
- **Function (MyGene.info)**: aconitase 2. The protein encoded by this gene belongs to the aconitase/IPM isomerase family. It is an enzyme that catalyzes the interconversion of citrate to isocitrate via cis-aconitate in the second step of the TCA cycle. This protein is encoded in the nucleus and functions in the mitochondrion. It was found to be one of the mitochondrial matrix proteins that are preferentially degraded by the serine proteas…
- **Diseases (Open Targets)**: infantile cerebellar-retinal degeneration (0.814); optic atrophy 9 (0.693); autosomal dominant optic atrophy, classic form (0.619); optic atrophy (0.601); mitochondrial disease (0.505)
- **Europe PMC papers**: 3559
- **Why important**: ACO2 has a prominent network position and links IMMT, ATP synthase, IDH3A, ATP1A1, and HIBCH. It catalyzes a central TCA-cycle conversion and is included in primary terms for mitochondrial matrix, aerobic respiration, energy derivation, precursor-metabolite generation, and metabolic pathways (GO:CC mitochondrion; q_global = 7.72e-07)(GO:CC mitochondrial matrix; q_global = 3.51e-06)(GO:BP aerobic respiration; q_global = 0.000774)(GO:BP cellular respiration; q_global = 0.00172)(GO:BP energy derivation by oxidation of organic compounds; q_global = 0.00395)(GO:BP generation of precursor metabolites and energy; q_global = 0.011)(KEGG Metabolic pathways - Homo sapiens (human); q_global = 0.0442). STRING gives strong support for relationships with IDH3A, ATP synthase subunits, HIBCH, UQCRC1, and UQCRC2. hu.MAP provides additional context through a complex containing ACO2 and HIBCH (hu.MAP huMAP3_12238.1). HPA detects the protein in both brain and ovary, with enhancement in heart and skeletal muscle as well as tongue. Its disease associations include optic atrophy and mitochondrial disease, and its literature volume is substantial.
- **Conclusion**: Established evidence places ACO2 at the interface between TCA-cycle carbon processing and respiratory energy production. It is an informative metabolic bridge in this module, but the module does not establish altered TCA flux or a tissue-specific ACO2 mechanism.

#### IMMT

- **Related proteins** (co-abundance neighbors): ATP1A1 (0.88), AIFM1 (0.86), UQCRC2 (0.85), ACO2 (0.84), ATP5F1A (0.82), NDUFA10 (0.81), ALCAM (0.81), RMDN3 (0.81); STRING partners: ATP5F1A (0.809), ATP5F1B (0.745), UQCRC2 (0.811)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inner membrane mitochondrial protein. Enables RNA binding activity. Involved in cristae formation. Located in mitochondrial inner membrane. Part of MICOS complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); multinodular goiter (0.196); alcohol drinking (0.190); breast cancer (0.094); neoplasm (0.087)
- **Europe PMC papers**: 933
- **Why important**: IMMT has the highest weighted network position in the supplied module and connects respiratory, ATP-synthesis, membrane, metabolic, adhesion-associated, and structural neighbors. It is a mitochondrial inner-membrane protein involved in cristae formation and the MICOS complex, and it is represented across the primary mitochondrial membrane and membrane-organization terms (GO:CC mitochondrion; q_global = 7.72e-07)(GO:CC mitochondrial membrane; q_global = 2.37e-05)(GO:CC mitochondrial envelope; q_global = 6.52e-05)(GO:CC mitochondrial inner membrane; q_global = 0.000693)(GO:CC organelle inner membrane; q_global = 0.00125)(GO:CC organelle envelope; q_global = 0.00535)(GO:CC membrane protein complex; q_global = 0.00741). STRING links it to ATP synthase, UQCRC2, ACO2, NDUFA10, AIFM1, and RMDN3. Although hu.MAP does not list it in the supplied complexes, its established cristae role provides a plausible structural explanation for its network position. HPA shows oocyte enhancement and protein detection in brain but not ovary; this discordance cautions against treating it as a direct tissue-specific driver. Its literature and disease-association evidence support relevance to mitochondrial and neurodegenerative biology.
- **Conclusion**: Established evidence supports IMMT as a mitochondrial inner-membrane and cristae-organization component with an unusually central position in this co-abundance network. A structural role coordinating respiratory machinery is plausible, but the apparent ovary protein-detection discrepancy means the shared tissue signal needs careful validation.

#### ATP2A2

- **Related proteins** (co-abundance neighbors): ATP1A1 (0.83); STRING partners: ATP1A1 (0.82)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_10473.1, huMAP3_06247.1
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darie…
- **Diseases (Open Targets)**: Darier disease (0.823); acrokeratosis verruciformis (0.663); neurodegenerative disease (0.507); hereditary disease (0.416); schizophrenia (0.406)
- **Europe PMC papers**: 9327
- **Why important**: ATP2A2 connects to ATP1A1 and represents calcium handling alongside the mitochondrial energy program. It encodes a SERCA calcium pump and is included in primary transporter, cation-transport, membrane-complex, cardiac-contraction, neurodegeneration, and diabetic-cardiomyopathy terms (KEGG Diabetic cardiomyopathy - Homo sapiens (human); q_global = 1.97e-05)(GO:CC transmembrane transporter complex; q_global = 3.64e-05)(GO:CC transporter complex; q_global = 5.01e-05)(GO:MF active monoatomic ion transmembrane transporter activity; q_global = 0.000398)(GO:MF monoatomic cation transmembrane transporter activity; q_global = 0.000436)(GO:MF primary active transmembrane transporter activity; q_global = 0.00106)(KEGG Cardiac muscle contraction - Homo sapiens (human); q_global = 0.00489)(KEGG Alzheimer disease - Homo sapiens (human); q_global = 0.0052)(GO:BP transmembrane transport; q_global = 0.00581)(GO:BP monoatomic ion transmembrane transport; q_global = 0.0186). hu.MAP places it with ATP1A1 and in a broader membrane-associated complex (hu.MAP huMAP3_10473.1)(hu.MAP huMAP3_06247.1), while STRING supports the ATP1A1 relationship. HPA reports detection in both brain and ovary and enrichment in heart muscle, skeletal muscle, tongue, cardiomyocytes, and endometrial ciliated cells. Its disease associations include Darier disease and neurodegenerative and schizophrenia-related traits, and its literature is extensive.
- **Conclusion**: Established evidence identifies ATP2A2 as a calcium-transport component that may connect energetic metabolism with calcium homeostasis. Its inclusion supports an energy-demand and ion-handling interpretation, but does not demonstrate direct mitochondrial regulation or disease causality.

#### UQCRC2

- **Related proteins** (co-abundance neighbors): UQCRC1 (0.90), IMMT (0.85); STRING partners: ACO2 (0.879), ATP5F1A (0.986), ATP5F1B (0.942), IDH3A (0.713), IMMT (0.811), NDUFA10 (0.986), NDUFS7 (0.98), UQCRC1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_07245.1, huMAP3_08546.1, huMAP3_09600.1, huMAP3_12621.1, huMAP3_10623.1, huMAP3_12457.1, huMAP3_06247.1
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase core protein 2. The protein encoded by this gene is located in the mitochondrion, where it is part of the ubiquinol-cytochrome c reductase complex (also known as complex III). This complex constitutes a part of the mitochondrial respiratory chain. Defects in this gene are a cause of mitochondrial complex III deficiency nuclear type 5. [provided by RefSeq, Jul 2015].
- **Diseases (Open Targets)**: mitochondrial complex III deficiency (0.732); neurodegenerative disease (0.423); mitochondrial disease (0.312); gastric cancer (0.085); adrenoleukodystrophy (0.075)
- **Europe PMC papers**: 3297
- **Why important**: UQCRC2 is a core protein of mitochondrial complex III and has strong STRING connectivity to UQCRC1, NDUFA10, NDUFS7, ATP synthase subunits, ACO2, IDH3A, and IMMT. It is represented throughout the primary mitochondrial, respiratory-chain, oxidative-phosphorylation, aerobic-respiration, electron-transport, and ATP-related terms (GO:CC mitochondrion; q_global = 7.72e-07)(KEGG Diabetic cardiomyopathy - Homo sapiens (human); q_global = 1.97e-05)(GO:CC mitochondrial membrane; q_global = 2.37e-05)(GO:CC respiratory chain complex; q_global = 0.000337)(KEGG Oxidative phosphorylation - Homo sapiens (human); q_global = 0.000628)(GO:BP aerobic respiration; q_global = 0.000774)(GO:BP oxidative phosphorylation; q_global = 0.00152)(GO:BP cellular respiration; q_global = 0.00172)(GO:BP aerobic electron transport chain; q_global = 0.0345). hu.MAP repeatedly places it with UQCRC1 in respiratory-chain and membrane complexes (hu.MAP huMAP3_07245.1)(hu.MAP huMAP3_08546.1)(hu.MAP huMAP3_09600.1)(hu.MAP huMAP3_12621.1)(hu.MAP huMAP3_10623.1)(hu.MAP huMAP3_12457.1). HPA detects it in both brain and ovary, and its disease associations include complex-III deficiency and neurodegenerative disease. Its literature is substantial.
- **Conclusion**: Established evidence supports UQCRC2 as a respiratory-chain complex-III anchor and a strong marker of the module's electron-transport core. Its network links suggest coordinated abundance across respiratory machinery, but not a newly discovered complex or a causal tissue-specific role.

## Module 7

**Tissue pair**: brain and ovary  
**Genes (16)**: ADNP, ATXN2L, EHMT1, EXOSC7, MMTAG2, NCOR1, PRRC2C, RAVER1, RBM22, POLR2D, RRP1B, SMNDC1, DNTTIP2, UBAP2, ZC3H4, ZPR1

### Function

The strongest interpretation is a conserved RNA- and nucleic-acid-associated regulatory module. The primary enrichment evidence is (GO:MF nucleic acid binding; q_global = 0.0138) nucleic acid binding and (GO:MF RNA binding; q_global = 0.0377) RNA binding, with broad overlap across the module. The individual annotations support RNA processing, pre-mRNA splicing, rRNA maturation, RNA surveillance, RNA polymerase transcriptional regulation, stress-granule assembly, and chromatin-mediated repression. (STRING Function Nucleic acid binding; within-query FDR = 0.0131) and (STRING Function RNA binding; within-query FDR = 0.0202) independently support the same functional theme, but are supplementary rather than globally corrected evidence. Together, the module is most consistent with coordinated control of RNA metabolism and gene expression, with a possible transcriptional and chromatin-regulatory component. No GO or KEGG term passed within-module correction, so the functional interpretation should remain integrative rather than being assigned to a single narrowly defined pathway.

**Cell composition.** This is not a plasma-protein, secreted-protein, or blood-cell-enriched module. HPA reports no secreted genes and uniformly low immune-cell specificity. Most genes have low tissue specificity and low cell-type specificity, while a subset shows enrichment in spermatogenic cells, with isolated enrichment in oocytes, photoreceptors, cardiomyocytes, plasma cells, or neutrophils. Protein detection is broad in both brain and ovary for many members. The composition therefore favors a broadly expressed intracellular housekeeping or regulatory program shared by resident cells in the two tissues, rather than a signal caused by circulating blood or secreted proteins. The spermatogenic associations may reflect shared transcriptional or RNA-processing programs, but they do not by themselves establish a germ-cell origin in the brain–ovary comparison.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleic acid binding | 0.0138 | ADNP, ATXN2L, C1orf35, DNTTIP2, EXOSC7, NCOR1, PRRC2C, RAVER1, RBM22, RRP1B, SMNDC1, UBAP2, ZC3H4 |
| GO:MF RNA binding | 0.0377 | ATXN2L, C1orf35, DNTTIP2, EXOSC7, PRRC2C, RAVER1, RBM22, RRP1B, SMNDC1, UBAP2, ZC3H4 |

### STRING and hu.MAP

At the stated high-confidence threshold, none of the possible gene pairs has a STRING interaction. Thus, the co-abundance edges should not be interpreted as established physical protein interactions, and the module may represent coordinated regulation, shared expression control, or common cellular state rather than a single physical complex. STRING functional enrichment nevertheless reproduces the nucleic-acid-binding and RNA-binding themes in (STRING Function Nucleic acid binding; within-query FDR = 0.0131) and (STRING Function RNA binding; within-query FDR = 0.0202). hu.MAP provides limited physical-complex support: ADNP and EHMT1 repeatedly co-occur in several chromatin-associated complexes (hu.MAP huMAP3_01874.1) through (hu.MAP huMAP3_11539.1), while DNTTIP2 and MMTAG2 co-occur in a broader RNA- and ribosome-associated complex (hu.MAP huMAP3_05807.1). These observations support specific mechanistic links, especially for ADNP–EHMT1 and DNTTIP2–MMTAG2, but the repeated complexes contain only a small subset of the module and do not establish one unified complex for all members.

**STRING interactions (score >= 0.7)**: 0 of 120 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Function Nucleic acid binding (FDR = 0.0131, 13 genes); Function RNA binding (FDR = 0.0202, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01874.1 (ADNP, EHMT1; 2/6); huMAP3_08464.1 (ADNP, EHMT1; 2/6); huMAP3_00075.1 (ADNP, EHMT1; 2/7); huMAP3_06802.1 (ADNP, EHMT1; 2/8); huMAP3_07706.1 (ADNP, EHMT1; 2/9); huMAP3_07798.1 (ADNP, EHMT1; 2/10); huMAP3_09707.1 (ADNP, EHMT1; 2/12); huMAP3_09232.1 (ADNP, EHMT1; 2/27); huMAP3_10311.1 (ADNP, EHMT1; 2/32); huMAP3_11539.1 (ADNP, EHMT1; 2/32); huMAP3_05807.1 (DNTTIP2, MMTAG2; 2/81)

### Novelty

The module is best described as a potentially novel cross-tissue co-abundance pattern, not as a newly established molecular complex. Its novelty lies in the coordinated brain–ovary abundance relationship and in the combination of RNA-binding, RNA-processing, transcriptional, and chromatin regulators. The absence of high-confidence STRING links and the limited overlap with hu.MAP argue against simply rediscovering a well-defined canonical complex, but database absence cannot prove biological novelty. The broad HPA expression pattern also means that the finding could reflect a shared intracellular regulatory state or cellular composition rather than a tissue-specific mechanism. Independent replication, preservation across cohorts, cell-type-aware analysis, and experimental interaction or perturbation studies would be needed before calling it a new biological pathway.

**Hypothesis.** Hypothesis: the module represents a coordinated post-transcriptional and transcriptional-control state in which RNA-binding and RNA-processing factors regulate RNA maturation, surveillance, splicing, and translation, while ADNP, EHMT1, and NCOR1 connect this state to chromatin repression and transcriptional control. PRRC2C may organize the co-abundance signal through stress-granule and cytoplasmic translation-related processes, whereas the DNTTIP2–EXOSC7 and DNTTIP2–SMNDC1 relationships may reflect coupled RNA and ribosome biogenesis. This model predicts coordinated changes in RNA processing and transcriptional output in the relevant brain and ovarian cell populations, but it remains a hypothesis because the network lacks high-confidence STRING pairwise interactions and the hu.MAP evidence covers only selected members.

### Important genes

#### PRRC2C

- **Related proteins** (co-abundance neighbors): NCOR1 (0.88), RBM22 (0.86), MMTAG2 (0.85), RRP1B (0.84), UBAP2 (0.83), ZC3H4 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proline rich coiled-coil 2C. Enables protein C-terminus binding activity. Involved in stress granule assembly. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.425); neurodegenerative disease (0.387); mathematical ability (0.278); alcohol drinking (0.250); intelligence (0.209)
- **Europe PMC papers**: 327
- **Why important**: PRRC2C is the central network hub by weighted connectivity and links NCOR1, RBM22, MMTAG2, RRP1B, UBAP2, and ZC3H4. It belongs to both primary enrichment terms (GO:MF nucleic acid binding; q_global = 0.0138) and (GO:MF RNA binding; q_global = 0.0377), is localized to the cytosol, and is annotated for stress-granule assembly and regulation of cytoplasmic translation. Its moderate literature base and disease associations with neurodegenerative and skeletal abnormalities make it a useful candidate for connecting the module's RNA-binding signal to cellular stress and translation.
- **Conclusion**: Established evidence supports PRRC2C as the strongest co-abundance organizer and as an RNA-associated cytoplasmic regulator. It is plausible, but not established, that PRRC2C helps coordinate nuclear RNA regulators with cytoplasmic stress-granule or translation responses.

#### DNTTIP2

- **Related proteins** (co-abundance neighbors): EXOSC7 (0.92), SMNDC1 (0.91), MMTAG2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_05807.1
- **Function (MyGene.info)**: deoxynucleotidyltransferase terminal interacting protein 2. This gene is thought to be involved in chromatin remodeling and gene transcription. The encoded nuclear protein binds to and enhances the transcriptional activity of the estrogen receptor alpha, and also interacts with terminal deoxynucleotidyltransferase. The expression profile of this gene is a potential biomarker for chronic obstructive pulmonary disease. [provided by RefSeq, Dec 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.164); narcolepsy (0.117); Aphasia (0.113); alcohol drinking (0.068); device complication (0.046)
- **Europe PMC papers**: 1134
- **Why important**: DNTTIP2 connects EXOSC7, SMNDC1, and MMTAG2 and belongs to both primary enrichment terms (GO:MF nucleic acid binding; q_global = 0.0138) and (GO:MF RNA binding; q_global = 0.0377). Its nucleolar localization and annotations for RNA processing and small-subunit ribosome biogenesis provide a concrete link to RNA maturation. It also participates with MMTAG2 in hu.MAP complex (hu.MAP huMAP3_05807.1). Its substantial literature footprint makes it one of the better-characterized mechanistic anchors in the module.
- **Conclusion**: Established evidence supports a role for DNTTIP2 in RNA and ribosome-related processing and provides the clearest complex-level connection outside the ADNP–EHMT1 pair. The hypothesis that it drives the shared brain–ovary co-abundance pattern remains untested.

#### ZC3H4

- **Related proteins** (co-abundance neighbors): ADNP (0.87), MMTAG2 (0.85), PRRC2C (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger CCCH-type containing 4. This gene encodes a member of a family of CCCH (C-x8-C-x5-C-x3-H type) zinc finger domain-containing proteins. These zinc finger domains, which coordinate zinc finger binding and are characterized by three cysteine residues and one histidine residue, are nucleic acid-binding. Other family members are known to function in post-transcriptional regulation. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.415); Abnormality of the skeletal system (0.355); Chest pain (0.352); neurodegenerative disease (0.344); obesity disorder (0.293)
- **Europe PMC papers**: 309
- **Why important**: ZC3H4 is connected to ADNP, MMTAG2, and PRRC2C and is present in both primary enrichment terms (GO:MF nucleic acid binding; q_global = 0.0138) and (GO:MF RNA binding; q_global = 0.0377). Its CCCH zinc-finger domains support nucleic-acid binding, while its annotations implicate transcriptional elongation control, nuclear RNA surveillance, and lncRNA turnover. It therefore bridges RNA binding with transcriptional and RNA-quality-control functions.
- **Conclusion**: Established evidence supports ZC3H4 as a nuclear nucleic-acid regulator with roles in transcriptional repression and RNA surveillance. Its network position makes it a credible bridge between the cytoplasmic PRRC2C branch and the nuclear regulatory branch, but that bridging role is a hypothesis.

#### ADNP

- **Related proteins** (co-abundance neighbors): ZC3H4 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Centrosome; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_01874.1, huMAP3_08464.1, huMAP3_00075.1, huMAP3_06802.1, huMAP3_07706.1, huMAP3_07798.1, huMAP3_09707.1, huMAP3_09232.1, huMAP3_10311.1, huMAP3_11539.1
- **Function (MyGene.info)**: activity dependent neuroprotector homeobox. Vasoactive intestinal peptide is a neuroprotective factor that has a stimulatory effect on the growth of some tumor cells and an inhibitory effect on others. This gene encodes a protein that is upregulated by vasoactive intestinal peptide and may be involved in its stimulatory effect on certain tumor cells. The encoded protein contains one homeobox and nine zinc finger domains, suggesting that it …
- **Diseases (Open Targets)**: ADNP-related multiple congenital anomalies - intellectual disability - autism spectrum disorder (0.788); hereditary disease (0.548); Intellectual disability (0.533); neurodegenerative disease (0.494); prostate carcinoma (0.420)
- **Europe PMC papers**: 1699
- **Why important**: ADNP connects to ZC3H4 and is present in the primary nucleic-acid-binding term (GO:MF nucleic acid binding; q_global = 0.0138). It contains a homeobox and zinc-finger domains, is associated with transcriptional regulation and neuron-projection development, and has strong disease associations involving intellectual disability, autism-spectrum-related abnormalities, and neurodegeneration. ADNP repeatedly co-occurs with EHMT1 across hu.MAP chromatin-associated complexes (hu.MAP huMAP3_01874.1) through (hu.MAP huMAP3_11539.1), giving it the strongest complex-level support for a chromatin-regulatory submodule.
- **Conclusion**: Established evidence supports ADNP as a transcriptional regulator with important neurodevelopmental relevance and recurring association with EHMT1-containing complexes. Its contribution to the ovary-shared module and to RNA processing is not established and should be treated as a cross-tissue co-regulation hypothesis.

#### EHMT1

- **Related proteins** (co-abundance neighbors): NCOR1 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_01874.1, huMAP3_08464.1, huMAP3_00075.1, huMAP3_06802.1, huMAP3_07706.1, huMAP3_07798.1, huMAP3_09707.1, huMAP3_09232.1, huMAP3_10311.1, huMAP3_11539.1
- **Function (MyGene.info)**: euchromatic histone lysine methyltransferase 1. The protein encoded by this gene is a histone methyltransferase that methylates the lysine-9 position of histone H3. This action marks the genomic region packaged with these methylated histones for transcriptional repression. This protein may be involved in the silencing of MYC- and E2F-responsive genes and therefore could play a role in the G0/G1 cell cycle transition. Defects in this gene are a …
- **Diseases (Open Targets)**: Kleefstra syndrome 1 (0.748); Kleefstra syndrome (0.677); hereditary disease (0.547); Intellectual disability (0.514); Kleefstra syndrome due to 9q34 microdeletion (0.462)
- **Europe PMC papers**: 2274
- **Why important**: EHMT1 is connected to NCOR1 and repeatedly appears with ADNP in hu.MAP complexes (hu.MAP huMAP3_01874.1) through (hu.MAP huMAP3_11539.1). Its histone lysine methyltransferase activity and annotations for chromatin organization, heterochromatin formation, and epigenetic repression provide a mechanistic route from the module to transcriptional control. It also has a substantial literature base and well-established disease associations with Kleefstra syndrome and intellectual disability.
- **Conclusion**: Established evidence supports EHMT1 as a chromatin-repressive enzyme and supports an ADNP–EHMT1-associated regulatory branch. Its inclusion in a shared brain–ovary co-abundance module does not prove that the entire module is an EHMT1 complex or that EHMT1 directly controls the RNA-binding genes.

#### NCOR1

- **Related proteins** (co-abundance neighbors): ZPR1 (0.90), EHMT1 (0.88), PRRC2C (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nuclear receptor corepressor 1. This gene encodes a protein that mediates ligand-independent transcription repression of thyroid-hormone and retinoic-acid receptors by promoting chromatin condensation and preventing access of the transcription machinery. It is part of a complex which also includes histone deacetylases and transcriptional regulators similar to the yeast protein Sin3p. This gene is located between the Charcot-Mari…
- **Diseases (Open Targets)**: breast adenocarcinoma (0.516); urinary bladder carcinoma (0.379); lung carcinoma (0.373); thyroid tumor (0.372); viral infectious disease (0.371)
- **Europe PMC papers**: 5492
- **Why important**: NCOR1 connects PRRC2C, EHMT1, and ZPR1 and is present in (GO:MF nucleic acid binding; q_global = 0.0138). It is a well-studied nuclear receptor corepressor involved in transcriptional repression, chromatin condensation, and regulation of metabolic transcriptional programs. It has the largest literature footprint among the selected genes and broad disease associations, making it an important interpretive anchor despite its limited network connectivity.
- **Conclusion**: Established evidence supports NCOR1 as a transcriptional corepressor that can connect chromatin regulation with nuclear gene-expression control. Its link to PRRC2C and EHMT1 in this module supports a regulatory interpretation, but the direction of regulation and relevance to the shared tissues remain hypotheses.

## Module 8

**Tissue pair**: brain and ovary  
**Genes (12)**: ATL3, CD44, HMGCL, ITGA3, ITGAV, ITGB1, LNPEP, MAN2A1, SLC16A3, ABCC1, MYOF, NCSTN

### Function

The strongest interpretation is a plasma-membrane cell-adhesion and extracellular-matrix interaction module. (GO:CC plasma membrane region; q_global = 0.000436) places most of the module in the plasma-membrane region, while (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.00825) identifies ECM-receptor interaction. The integrin-centered evidence is especially coherent: ITGA3, ITGAV and ITGB1 support fibronectin binding (GO:MF fibronectin binding; q_global = 0.0107), integrin complexes (GO:CC integrin complex; q_global = 0.0141), receptor complexes (GO:CC receptor complex; q_global = 0.0263), the integrin alpha-three-beta-one and alpha-v-beta-one complexes (GO:CC integrin alpha3-beta1 complex; q_global = 0.0288) (GO:CC integrin alphav-beta1 complex; q_global = 0.0288), and cell adhesion or wound-healing-related processes (4 globally significant GO/KEGG terms, q_global 0.0227–0.0466; see the table). Thus, the established functional signal is cell-matrix adhesion, adhesion-dependent signaling, and cellular spreading or migration. The remaining genes suggest associated membrane organization, glycoprotein processing, vesicle or membrane repair, solute transport, peptide processing, and metabolic support, but these are secondary interpretations because they are not represented by globally corrected GO or KEGG terms. The module is therefore better viewed as an adhesion and membrane-interface program than as a single canonical biochemical pathway.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. The proteins are mainly membrane-associated or intracellular, with CD44 annotated as secreted to blood and LNPEP having intracellular and membrane localization. HPA reports low tissue specificity for most genes, with only a few tissue-enhanced genes and enrichment across diverse epithelial, vascular, neural-support, reproductive, and immune-related cell types. Several genes have neutrophil or monocyte associations, but most genes have low immune-cell specificity and some are not detected in immune cells. The module could therefore partly reflect shared cell types or membrane-rich cellular material in brain and ovary samples, but the evidence does not support interpreting it mainly as a blood-contamination signature. Detection of nearly all assessed proteins in brain and most assessed proteins in ovary is consistent with a genuine shared tissue signal, although bulk-tissue co-abundance cannot establish that the same cell type expresses every member.

**GO/KEGG enrichment**: 12 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC plasma membrane region | 0.000436 | ABCC1, CD44, ITGA3, ITGAV, ITGB1, MYOF, NCSTN, SLC16A3 |
| KEGG ECM-receptor interaction - Homo sapiens (human) | 0.00825 | CD44, ITGA3, ITGAV, ITGB1 |
| GO:MF fibronectin binding | 0.0107 | ITGA3, ITGAV, ITGB1 |
| GO:CC integrin complex | 0.0141 | ITGA3, ITGAV, ITGB1 |
| GO:BP wound healing, spreading of cells | 0.0227 | CD44, ITGAV, ITGB1 |
| GO:BP epiboly | 0.0227 | CD44, ITGAV, ITGB1 |
| GO:BP epiboly involved in wound healing | 0.0227 | CD44, ITGAV, ITGB1 |
| GO:CC receptor complex | 0.0263 | CD44, ITGA3, ITGAV, ITGB1 |
| GO:CC integrin alpha3-beta1 complex | 0.0288 | ITGA3, ITGB1 |
| GO:CC integrin alphav-beta1 complex | 0.0288 | ITGAV, ITGB1 |
| GO:BP heterotypic cell-cell adhesion | 0.0335 | CD44, ITGAV, ITGB1 |
| GO:CC protein complex involved in cell adhesion | 0.0466 | ITGA3, ITGAV, ITGB1 |

### STRING and hu.MAP

STRING provides a known interaction core involving CD44, ITGAV, ITGA3 and ITGB1. The strongest relationships connect the integrin subunits into established receptor complexes, while CD44 is linked to ITGAV and ITGB1 and more weakly to SLC16A3. STRING enrichment also independently supports membrane localization, integrin complexes, ECM-receptor interaction, and cell-surface interactions at the vascular wall (15 supplementary STRING terms; within-query FDR 3.5e-07–0.0028). These relationships indicate that the central adhesion signal is biologically established rather than produced solely by correlation. Most other module edges do not have a listed high-confidence STRING relationship, so the full co-abundance neighborhood should not be treated as a validated physical complex. hu.MAP supports partial membership of ITGA3, ITGB1 and LNPEP in several larger adhesion or membrane-associated complexes (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1), with additional partial ITGA3-ITGB1 or ITGA3-LNPEP complexes (hu.MAP huMAP3_06815.1) (hu.MAP huMAP3_08103.1) (hu.MAP huMAP3_09105.1) (hu.MAP huMAP3_08689.1). Because these complexes contain many proteins absent from the module, they support contextual compatibility rather than a complete module-wide complex.

**STRING interactions (score >= 0.7)**: 6 of 66 gene pairs: CD44–ITGAV (0.85); CD44–ITGB1 (0.957); CD44–SLC16A3 (0.717); ITGA3–ITGAV (0.968); ITGA3–ITGB1 (0.999); ITGAV–ITGB1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transmembrane helix (FDR = 3.5e-07, 11 genes); Component Integral component of plasma membrane (FDR = 6.79e-07, 8 genes); Component Integral component of membrane (FDR = 9.3e-06, 11 genes); Component Plasma membrane region (FDR = 5.23e-05, 8 genes); RCTM Cell surface interactions at the vascular wall (FDR = 0.00012, 5 genes); COMPARTMENTS Plasma membrane region (FDR = 0.00023, 7 genes); Keyword Glycoprotein (FDR = 0.00049, 8 genes); Keyword Cell membrane (FDR = 0.00049, 8 genes); Keyword Integrin (FDR = 0.0012, 3 genes); Keyword Disulfide bond (FDR = 0.0012, 7 genes); COMPARTMENTS Integral component of membrane (FDR = 0.0014, 7 genes); COMPARTMENTS Integral component of plasma membrane (FDR = 0.0015, 5 genes); KEGG ECM-receptor interaction (FDR = 0.0018, 4 genes); COMPARTMENTS Extracellular region (FDR = 0.0022, 8 genes); Component Integrin complex (FDR = 0.0028, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10503.1 (ITGB1, ITGA3, LNPEP; 3/27); huMAP3_10980.1 (ITGB1, ITGA3, LNPEP; 3/44); huMAP3_09336.1 (ITGB1, ITGA3, LNPEP; 3/50); huMAP3_06815.1 (ITGB1, ITGA3; 2/5); huMAP3_08103.1 (ITGA3, LNPEP; 2/23); huMAP3_09105.1 (ITGA3, LNPEP; 2/24); huMAP3_08689.1 (ITGA3, LNPEP; 2/37)

### Novelty

The module may be a new cross-tissue co-abundance observation, but the underlying biology is not a newly discovered adhesion mechanism. The integrin core, CD44 relationships, ECM-receptor interaction, and partial hu.MAP complexes are already known, and the relevant genes have established roles in cell adhesion, migration, membrane organization, transport, and repair. The potentially novel result is the specific coordinated abundance of this broader gene set in both brain and ovary, including genes that are not connected by known STRING or hu.MAP relationships. That claim requires independent replication, cell-type-resolved analysis, and ideally spatial or protein-level validation. Absence of an edge from STRING or hu.MAP is evidence of incomplete prior annotation, not proof that the relationship or module is novel.

**Hypothesis.** Hypothesis: in both brain and ovary, a shared population of membrane-bearing structural or epithelial-like cells coordinates integrin-mediated attachment to extracellular matrix with CD44-dependent cell-cell or hyaluronan interactions. ITGA3-ITGB1 and ITGAV-containing receptors may organize adhesion and spreading, while MYOF may support membrane remodeling or repair, SLC16A3 may couple local lactate and pyruvate flux to the energetic demands of adhesion, ABCC1 may contribute membrane transport, and MAN2A1 may influence glycosylation of surface proteins. This is a mechanistic hypothesis rather than a demonstrated pathway: co-abundance does not establish direct regulation, physical assembly, or causal direction. A useful test would combine single-cell or spatial expression with perturbation of the integrin-CD44 axis and measurement of adhesion, migration, and membrane-repair phenotypes.

### Important genes

#### ITGA3

- **Related proteins** (co-abundance neighbors): MYOF (0.86), ABCC1 (0.85), SLC16A3 (0.83), MAN2A1 (0.83), ITGB1 (0.81); STRING partners: ITGAV (0.968), ITGB1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_10503.1, huMAP3_10980.1, huMAP3_09336.1, huMAP3_06815.1, huMAP3_08103.1, huMAP3_09105.1, huMAP3_08689.1
- **Function (MyGene.info)**: integrin subunit alpha 3. The gene encodes a member of the integrin alpha chain family of proteins. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain that function as cell surface adhesion molecules. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha 3 subunit. This subunit joins with a beta 1 subunit to form an …
- **Diseases (Open Targets)**: epidermolysis bullosa, junctional 7, with interstitial lung disease and nephrotic syndrome (0.807); neurodegenerative disease (0.503); junctional epidermolysis bullosa (0.372); junctional epidermolysis bullosa Herlitz type (0.370); epidermolysis bullosa simplex 4, localized or generalized intermediate, autosomal recessive (0.370)
- **Europe PMC papers**: 4167
- **Why important**: ITGA3 is the most central node by weighted connectivity in the module and participates in nearly all major evidence streams. It forms the alpha-three-beta-one integrin with ITGB1, binds extracellular-matrix proteins including laminins, and appears in the globally corrected plasma-membrane, ECM, fibronectin-binding, integrin-complex, adhesion, and receptor-complex terms (7 globally significant GO/KEGG terms, q_global 0.000436–0.0466; see the table). It also has extensive STRING and hu.MAP support and substantial literature, with established links to junctional epidermolysis bullosa and neurodegenerative disease.
- **Conclusion**: Established evidence supports ITGA3 as a core adhesion receptor and a principal structural anchor of the module. It is reasonable to hypothesize that its coordinated abundance helps define the shared module, but the data do not show that ITGA3 initiates the cross-tissue program or that it is causal for the co-abundance pattern.

#### ITGB1

- **Related proteins** (co-abundance neighbors): ATL3 (0.84), ITGAV (0.82), ABCC1 (0.81), ITGA3 (0.81); STRING partners: CD44 (0.957), ITGA3 (0.999), ITGAV (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_10503.1, huMAP3_10980.1, huMAP3_09336.1, huMAP3_06815.1
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is a highly connected hub and the common beta subunit for the integrin complexes represented in the module. It contributes to every globally corrected term involving the adhesion receptor core (12 globally significant GO/KEGG terms, q_global 0.000436–0.0466; see the table), has strong STRING support with ITGA3, ITGAV and CD44, and occurs in several hu.MAP complexes (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1) (hu.MAP huMAP3_06815.1). Its broad functions include cell adhesion, tissue repair, angiogenesis, phagocytosis, and signaling, and it has extensive literature and disease associations involving inflammation and immune-related disorders.
- **Conclusion**: Established evidence identifies ITGB1 as the principal shared integrin signaling and adhesion component. A plausible hypothesis is that ITGB1 couples extracellular-matrix engagement to intracellular responses in the conserved module, but the module alone cannot distinguish that mechanism from coordinated abundance caused by shared cell composition.

#### ITGAV

- **Related proteins** (co-abundance neighbors): LNPEP (0.82), ITGB1 (0.82), NCSTN (0.81); STRING partners: CD44 (0.85), ITGA3 (0.968), ITGB1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha V. The product of this gene belongs to the integrin alpha chain family. Integrins are heterodimeric integral membrane proteins composed of an alpha subunit and a beta subunit that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha V subunit. This subunit associates with beta 1, beta 3, beta…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); myocardial infarction (0.396); angina pectoris (0.371); Recurrent thrombophlebitis (0.370); intermediate coronary syndrome (0.370)
- **Europe PMC papers**: 5475
- **Why important**: ITGAV is a central integrin alpha subunit with strong links to ITGA3 and ITGB1 and a STRING connection to CD44. It appears in the ECM-receptor, fibronectin-binding, integrin-complex, receptor-complex, wound-healing, epiboly, cell-cell adhesion, and adhesion-complex terms (11 globally significant GO/KEGG terms, q_global 0.000436–0.0466; see the table). Its established functions include cell-matrix adhesion, angiogenesis, vasculogenesis, and calcium-related signaling, while its disease associations include neurodegenerative and cardiovascular conditions. It also has substantial literature support.
- **Conclusion**: Established evidence supports ITGAV as a second major receptor arm that broadens the module beyond the alpha-three-beta-one complex. It may provide context-dependent adhesion or signaling functions in brain and ovary, but which ligand, heterodimer, or downstream pathway is active cannot be inferred from these data.

#### CD44

- **Related proteins** (co-abundance neighbors): MYOF (0.81); STRING partners: ITGAV (0.85), ITGB1 (0.957), SLC16A3 (0.717)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD44 molecule (IN blood group). The protein encoded by this gene is a cell-surface glycoprotein involved in cell-cell interactions, cell adhesion and migration. It is a receptor for hyaluronic acid (HA) and can also interact with other ligands, such as osteopontin, collagens, and matrix metalloproteinases (MMPs). This protein participates in a wide variety of cellular functions including lymphocyte activation, recirculation and …
- **Diseases (Open Targets)**: nephrolithiasis, calcium oxalate (0.523); calcium oxalate urolithiasis (0.521); uterine corpus leiomyoma (0.480); systemic lupus erythematosus (0.467); autoimmune disease (0.330)
- **Europe PMC papers**: 102058
- **Why important**: CD44 is a well-studied cell-surface glycoprotein and receptor for hyaluronan that mediates cell-cell interaction, migration, cell-matrix adhesion, and inflammatory or metastatic behavior. It connects in STRING to ITGAV, ITGB1 and SLC16A3 and contributes to the globally corrected plasma-membrane, ECM-receptor, wound-healing, epiboly, receptor-complex, and heterotypic-adhesion terms (7 globally significant GO/KEGG terms, q_global 0.000436–0.0335; see the table). Its extensive literature and associations with autoimmune disease and uterine leiomyoma make it an informative interface between adhesion biology and tissue state.
- **Conclusion**: Established evidence supports CD44 as a membrane-interface partner that complements integrin adhesion with hyaluronan-dependent cell interaction and migration. It could mark activated or remodeling cells in the shared module, but that interpretation remains a hypothesis because isoform usage, ligand engagement, and cell identity were not resolved.

#### MYOF

- **Related proteins** (co-abundance neighbors): ITGA3 (0.86), CD44 (0.81), MAN2A1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Plasma membrane, Centriolar satellite; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myoferlin. Mutations in dysferlin, a protein associated with the plasma membrane, can cause muscle weakness that affects both proximal and distal muscles. The protein encoded by this gene is a type II membrane protein that is structurally similar to dysferlin. It is a member of the ferlin family and associates with both plasma and nuclear membranes. The protein contains C2 domains that play a role in calcium…
- **Diseases (Open Targets)**: hereditary angioedema (0.443); neurodegenerative disease (0.413); cervical carcinoma (0.134); type 2 diabetes mellitus (0.131); neoplasm (0.112)
- **Europe PMC papers**: 1200
- **Why important**: MYOF links the adhesion-centered portion of the network to membrane dynamics: it connects to ITGA3 and CD44 and is annotated for calcium-dependent membrane fusion and plasma-membrane repair. It is detected in both tissues, is enhanced in several endometrial and urothelial cell types, and has an immune-cell association with monocytes. Its literature is smaller than that of the core integrins or CD44, but it has established relevance to membrane repair, muscle biology, neurotransmitter secretion, and neurodegenerative disease.
- **Conclusion**: Established evidence supports MYOF as a membrane-remodeling or repair component associated with the adhesion interface. The hypothesis that MYOF enables rapid membrane adaptation during integrin-dependent spreading is biologically plausible, but it is not directly demonstrated by the co-abundance network.

## Module 9

**Tissue pair**: brain and ovary  
**Genes (12)**: BRIX1, DDX21, MYBBP1A, NOL11, NOP2, RFC4, RPL3, RPL6, RPL9, RPF2, RRS1, TCOF1

### Function

This is a nucleolar ribosome-biogenesis and ribosomal-large-subunit assembly module. The primary evidence is unusually coherent: rRNA binding (GO:MF rRNA binding; q_global = 2.39e-05), large-subunit assembly (GO:BP ribosomal large subunit assembly; q_global = 9.61e-05), rRNA metabolism (GO:BP rRNA metabolic process; q_global = 0.000141), ribosome biogenesis (GO:BP ribosome biogenesis; q_global = 0.000303), nucleolar localization (GO:CC nucleolus; q_global = 0.000916), rRNA processing (GO:BP rRNA processing; q_global = 0.00112), ribosome assembly (GO:BP ribosome assembly; q_global = 0.0015), and ribonucleoprotein-complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.00194) all pass global correction. The module also includes large-subunit ribosomal proteins RPL3, RPL6, and RPL9 (GO:CC cytosolic large ribosomal subunit; q_global = 0.00196) (GO:CC large ribosomal subunit; q_global = 0.0227). DDX21, MYBBP1A, NOL11, and TCOF1 connect the module to RNA polymerase I transcription and nucleolar regulation (GO:BP transcription by RNA polymerase I; q_global = 0.0104) (GO:BP positive regulation of transcription by RNA polymerase I; q_global = 0.0278) (GO:BP regulation of transcription by RNA polymerase I; q_global = 0.0466). The p53-related term (GO:BP signal transduction by p53 class mediator; q_global = 0.0307) is compatible with a nucleolar-stress or growth-control interface, but it should not be interpreted as evidence that the module is primarily a p53 module. RFC4 is the least specific member functionally and may represent a linked nucleoplasmic replication or repair signal rather than the module core. The broad RNA- and nucleic-acid-binding terms (GO:MF nucleic acid binding; q_global = 0.000519) (GO:MF RNA binding; q_global = 0.000655) support, but do not replace, the more specific ribosome-biogenesis interpretation.

**Cell composition.** The module is composed of intracellular nucleolar, RNA-processing, ribosome-biogenesis, and ribosomal-protein genes. HPA assigns low tissue specificity to every member, with no enriched tissue category, so the shared brain–ovary signal is not evidence for a brain- or ovary-exclusive program. The genes are not secreted proteins, and all have low immune-cell specificity; therefore the module is not suggestive of a plasma-protein or blood-cell contamination signal. HPA detects protein for most members in brain and for a subset in ovary, consistent with broad cellular expression and with the possibility that the co-abundance reflects a shared proliferative, biosynthetic, or nucleolar state. Cell-type enhancement in oocytes for BRIX1 and TCOF1, and in several neural or trophoblast-related cell types for other genes, is compatible with cell-state or composition effects, but does not establish a specialized oocyte–neuron mechanism.

**GO/KEGG enrichment**: 20 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF rRNA binding | 2.39e-05 | BRIX1, DDX21, RPF2, RPL9, RRS1 |
| GO:BP ribosomal large subunit assembly | 9.61e-05 | BRIX1, NOP2, RPF2, RRS1 |
| GO:BP rRNA metabolic process | 0.000141 | BRIX1, DDX21, NOL11, NOP2, RPF2, RRS1, TCOF1 |
| GO:BP ribosome biogenesis | 0.000303 | BRIX1, DDX21, MYBBP1A, NOL11, NOP2, RPF2, RRS1 |
| GO:MF nucleic acid binding | 0.000519 | BRIX1, DDX21, MYBBP1A, NOL11, NOP2, RFC4, RPF2, RPL3, RPL6, RPL9, RRS1, TCOF1 |
| GO:MF RNA binding | 0.000655 | BRIX1, DDX21, MYBBP1A, NOL11, NOP2, RPF2, RPL3, RPL6, RPL9, RRS1, TCOF1 |
| GO:CC nucleolus | 0.000916 | BRIX1, DDX21, MYBBP1A, NOL11, NOP2, RPF2, RPL3, RRS1, TCOF1 |
| GO:BP rRNA processing | 0.00112 | BRIX1, DDX21, NOL11, NOP2, RPF2, RRS1 |
| GO:BP ribosome assembly | 0.0015 | BRIX1, NOP2, RPF2, RRS1 |
| GO:BP ribonucleoprotein complex biogenesis | 0.00194 | BRIX1, DDX21, MYBBP1A, NOL11, NOP2, RPF2, RRS1 |
| GO:CC cytosolic large ribosomal subunit | 0.00196 | RPL3, RPL6, RPL9 |
| GO:BP ribosomal large subunit biogenesis | 0.00646 | BRIX1, NOP2, RPF2, RRS1 |
| GO:BP transcription by RNA polymerase I | 0.0104 | DDX21, MYBBP1A, NOL11, TCOF1 |
| GO:CC large ribosomal subunit | 0.0227 | RPL3, RPL6, RPL9 |
| GO:BP positive regulation of transcription by RNA polymerase I | 0.0278 | DDX21, MYBBP1A, NOL11 |

### STRING and hu.MAP

STRING independently supports the same biological interpretation: rRNA binding (STRING Function rRNA binding; within-query FDR = 1.67e-07), ribosome biogenesis (STRING Keyword Ribosome biogenesis; within-query FDR = 1.94e-06) (STRING Process Ribosome biogenesis; within-query FDR = 6.4e-06), large-subunit assembly (STRING Process Ribosomal large subunit assembly; within-query FDR = 6.4e-06), nucleolar localization (STRING COMPARTMENTS Nucleolus; within-query FDR = 1.47e-05) (STRING Component Nucleolus; within-query FDR = 0.0002), and rRNA processing (STRING Process rRNA metabolic process; within-query FDR = 4.02e-05) (STRING RCTM rRNA processing in the nucleus and cytosol; within-query FDR = 0.00013) (STRING Process rRNA processing; within-query FDR = 0.0004). The high-confidence STRING graph contains a dense core around BRIX1, RPF2, NOP2, RRS1, DDX21, and the large-subunit proteins, with particularly strong links among BRIX1–RPF2, RPF2–RRS1, BRIX1–NOP2, NOP2–RPF2, and the RPL3–RPL6–RPL9 group. These are mostly established functional or physical associations, so the co-abundance module recapitulates a known ribosome-production neighborhood rather than defining an entirely disconnected interaction system. STRING support is supplementary because its reported significance is within-query and not globally corrected across modules. No hu.MAP complex contains multiple module members in the supplied result, so there is no hu.MAP-confirmed multi-member complex to cite. The absence of a hu.MAP complex does not negate the STRING and GO-supported functional coherence.

**STRING interactions (score >= 0.7)**: 24 of 66 gene pairs: BRIX1–DDX21 (0.709); BRIX1–MYBBP1A (0.76); BRIX1–NOP2 (0.986); BRIX1–RPF2 (0.993); BRIX1–RPL3 (0.871); BRIX1–RPL6 (0.892); BRIX1–RPL9 (0.862); BRIX1–RRS1 (0.977); DDX21–MYBBP1A (0.963); DDX21–NOP2 (0.761); DDX21–RRS1 (0.842); MYBBP1A–NOP2 (0.864); MYBBP1A–RPF2 (0.738); NOP2–RPF2 (0.989); NOP2–RPL6 (0.915); NOP2–RPL9 (0.766); NOP2–RRS1 (0.944); RPF2–RPL3 (0.864); RPF2–RPL6 (0.746); RPF2–RRS1 (0.999); RPL3–RPL6 (0.999); RPL3–RPL9 (0.999); RPL3–RRS1 (0.75); RPL6–RPL9 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function rRNA binding (FDR = 1.67e-07, 6 genes); Keyword Ribosome biogenesis (FDR = 1.94e-06, 6 genes); Process Ribosomal large subunit assembly (FDR = 6.4e-06, 5 genes); Process Ribosome biogenesis (FDR = 6.4e-06, 8 genes); COMPARTMENTS Nucleolus (FDR = 1.47e-05, 9 genes); Process rRNA metabolic process (FDR = 4.02e-05, 7 genes); Function Nucleic acid binding (FDR = 0.0001, 12 genes); Function RNA binding (FDR = 0.0001, 11 genes); RCTM rRNA processing in the nucleus and cytosol (FDR = 0.00013, 6 genes); Component Nucleolus (FDR = 0.0002, 9 genes); COMPARTMENTS Intracellular non-membrane-bounded organelle (FDR = 0.00025, 12 genes); Process rRNA processing (FDR = 0.0004, 6 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 0.00047, 6 genes); Function 5S rRNA binding (FDR = 0.00071, 3 genes); NetworkNeighborAL Cytoplasmic ribosomal proteins (FDR = 0.00093, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The biological function is not a new discovery: the principal members already have established roles in nucleolar RNA processing, ribosome biogenesis, large-subunit assembly, or cytosolic large-ribosomal-subunit structure, and STRING contains many corresponding relationships. What may be novel is the reproducible brain–ovary co-abundance pairing and the precise membership or organization of this conserved module, especially the joint behavior of nucleolar factors with selected large-subunit proteins and RFC4. That claim remains provisional because the fact sheet does not provide an external catalog comparison, replication cohort, direction of abundance, tissue covariates, or perturbation evidence. Lack of a hu.MAP complex is not evidence of novelty, and the presence of known STRING edges argues against presenting the module as a newly discovered molecular complex. The strongest defensible conclusion is a potentially novel cross-tissue co-abundance pattern built from largely established ribosome-biogenesis machinery.

**Hypothesis.** Hypothesis: in both brain and ovary, variation in a shared cellular biosynthetic or growth-related state coordinately changes nucleolar rRNA production, processing, and large-ribosomal-subunit maturation. BRIX1, RPF2, RRS1, and NOP2 may form the central maturation and assembly axis, with DDX21 and NOL11 supporting RNA remodeling and rRNA maturation, TCOF1 linking the program to RNA polymerase I transcription, and RPL3, RPL6, and RPL9 reflecting the resulting large-subunit output. MYBBP1A may connect the program to nucleolar stress and transcriptional control, while RFC4 may mark a coupled replication or DNA-repair state. This is a mechanistic model, not demonstrated causality; testing would require matched cell-type analysis, perturbation of central nucleolar factors, and measurement of pre-rRNA processing, mature ribosome output, and nucleolar-stress responses.

### Important genes

#### RPF2

- **Related proteins** (co-abundance neighbors): BRIX1 (0.91), NOL11 (0.84), TCOF1 (0.83); STRING partners: BRIX1 (0.993), MYBBP1A (0.738), NOP2 (0.989), RPL3 (0.864), RPL6 (0.746), RRS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosome production factor 2 homolog. Enables 5S rRNA binding activity. Involved in protein localization to nucleolus; regulation of signal transduction by p53 class mediator; and ribosomal large subunit biogenesis. Located in chromosome; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.479); Hypercholesterolemia (0.196); colorectal carcinoma (0.079); Helicobacter pylori infectious disease (0.048); asthma (0.047)
- **Europe PMC papers**: 424
- **Why important**: RPF2 has a central position in the module and connects to BRIX1, NOL11, and TCOF1. It is represented across many of the specific primary terms, including rRNA binding, large-subunit assembly, rRNA processing, ribosome biogenesis, and p53-class signal regulation (7 globally significant GO/KEGG terms, q_global 2.39e-05–0.0307; see the table). Its curated function includes five-S rRNA binding, LSU-rRNA maturation, and large-subunit biogenesis. It also has substantial literature and disease- and neurodegeneration-related evidence in Open Targets, making it both mechanistically informative and experimentally tractable.
- **Conclusion**: Established: RPF2 is a strong marker and plausible core component of the ribosome-biogenesis program, supported by its network position, primary annotations, nucleolar localization, and STRING relationships. Hypothesis: its centrality may make it a useful perturbation point for testing whether the shared brain–ovary module controls ribosome output rather than merely reflecting correlated expression.

#### BRIX1

- **Related proteins** (co-abundance neighbors): RPF2 (0.91), RPL3 (0.84); STRING partners: DDX21 (0.709), MYBBP1A (0.76), NOP2 (0.986), RPF2 (0.993), RPL3 (0.871), RPL6 (0.892), RPL9 (0.862), RRS1 (0.977)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Mitotic chromosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biogenesis of ribosomes BRX1. Enables RNA binding activity. Predicted to be involved in ribosomal large subunit assembly. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: colorectal cancer (0.077); cancer (0.077); colorectal carcinoma (0.074); deficiency anemia (0.065); sialolithiasis (0.060)
- **Europe PMC papers**: 251
- **Why important**: BRIX1 is represented in nearly all of the most specific primary terms and is connected in the module to RPF2 and RPL3. STRING places it in a much broader known interaction neighborhood, including RPF2, NOP2, RRS1, DDX21, and large-subunit proteins. Its curated function is ribosomal large-subunit assembly and rRNA processing. HPA additionally reports cell-type enhancement in oocytes and trophoblast populations, which is relevant to the ovary-containing tissue pair. Although its literature volume is smaller than that of several other members, that makes it a useful candidate for assessing whether this cross-tissue module contains a less extensively studied assembly component.
- **Conclusion**: Established: BRIX1 is a nucleolar ribosome-production factor with strong module and STRING support. Hypothesis: its oocyte-associated HPA pattern may contribute to the conserved tissue-pair signal, but this cannot be separated from broad cell-state or composition effects using the supplied data.

#### DDX21

- **Related proteins** (co-abundance neighbors): NOL11 (0.85), MYBBP1A (0.84), NOP2 (0.84); STRING partners: BRIX1 (0.709), MYBBP1A (0.963), NOP2 (0.761), RRS1 (0.842)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 occupies a bridging position between NOL11, MYBBP1A, and NOP2 and is represented in primary terms for rRNA binding, rRNA metabolism, nucleolar localization, rRNA processing, and RNA polymerase I regulation (7 globally significant GO/KEGG terms, q_global 2.39e-05–0.0466; see the table). As a DEAD-box RNA helicase, it provides a plausible RNA-remodeling activity within the module. It has strong STRING relationships, extensive literature, and disease associations involving neurodegenerative disease and cancer-related conditions.
- **Conclusion**: Established: DDX21 is a well-supported RNA and nucleolar regulatory component of the module. Hypothesis: DDX21 may coordinate rRNA structural remodeling with transcriptional regulation, thereby linking the assembly machinery to changes in cellular growth or nucleolar stress.

#### TCOF1

- **Related proteins** (co-abundance neighbors): RRS1 (0.85), RFC4 (0.83), RPF2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: treacle ribosome biogenesis factor 1. This gene encodes a nucleolar protein with a LIS1 homology domain. The protein is involved in ribosomal DNA gene transcription through its interaction with upstream binding factor (UBF). Mutations in this gene have been associated with Treacher Collins syndrome, a disorder which includes abnormal craniofacial development. Multiple transcript variants encoding different isoforms have been found for…
- **Diseases (Open Targets)**: Treacher Collins syndrome 1 (0.761); Treacher-Collins syndrome (0.713); hereditary disease (0.472); neurodegenerative disease (0.459); Emery-Dreifuss muscular dystrophy 4, autosomal dominant (0.266)
- **Europe PMC papers**: 1248
- **Why important**: TCOF1 links RRS1, RFC4, and RPF2 in the co-abundance graph and appears in primary terms for rRNA metabolism, nucleolar localization, and RNA polymerase I transcription (5 globally significant GO/KEGG terms, q_global 0.000141–0.0466; see the table). Its curated role in ribosome biogenesis and nucleolar large-rRNA transcription is reinforced by the Treacher Collins syndrome association, which provides a strong developmental and disease relevance. HPA detects it in both brain and ovary and reports oocyte enhancement, directly matching the tissue pair more closely than many other members.
- **Conclusion**: Established: TCOF1 is a disease-linked nucleolar transcription and ribosome-biogenesis factor that plausibly anchors the shared tissue signal. Hypothesis: TCOF1 may couple rDNA transcriptional activity to downstream ribosome maturation in this module, but the co-abundance data do not demonstrate physical coupling or directionality.

#### NOP2

- **Related proteins** (co-abundance neighbors): DDX21 (0.84); STRING partners: BRIX1 (0.986), DDX21 (0.761), MYBBP1A (0.864), RPF2 (0.989), RPL6 (0.915), RPL9 (0.766), RRS1 (0.944)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP2 nucleolar protein. Enables RNA binding activity. Involved in positive regulation of cell population proliferation; regulation of signal transduction by p53 class mediator; and ribosomal large subunit assembly. Located in nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.273); nonpapillary renal cell carcinoma (0.097); neoplasm (0.097); cancer (0.091); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 2120
- **Why important**: NOP2 is a highly connected STRING member and links to BRIX1, DDX21, MYBBP1A, RPF2, RPL6, RPL9, and RRS1. It appears in the primary terms for large-subunit assembly, rRNA processing, ribosome biogenesis, nucleolar localization, and p53-class signaling (8 globally significant GO/KEGG terms, q_global 9.61e-05–0.0307; see the table). Its curated functions include rRNA maturation and large-subunit biogenesis, while its broad literature and cancer-related associations make it a prominent growth-state marker.
- **Conclusion**: Established: NOP2 is a central, well-characterized nucleolar ribosome-biogenesis component with strong independent network support. Hypothesis: its coordinated abundance may report increased demand for ribosome production in a shared biosynthetic state, rather than a tissue-specific pathway.

#### RPL3

- **Related proteins** (co-abundance neighbors): RPL9; RPL9P7; RPL9P8; RPL9P9 (0.86), RPL6 (0.86), BRIX1 (0.84); STRING partners: BRIX1 (0.871), RPF2 (0.864), RPL6 (0.999), RPL9 (0.999), RRS1 (0.75)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Cytosol; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein L3. Ribosomes, the complexes that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L3P family of ribosomal proteins and it is located in the cytoplasm. The p…
- **Diseases (Open Targets)**: Duchenne muscular dystrophy (0.506); Orthomyxoviridae infectious disease (0.463); cystic fibrosis (0.389); neuromuscular disease caused by qualitative or quantitative defects of dystrophin (0.323); inflammatory bowel disease (0.308)
- **Europe PMC papers**: 2316
- **Why important**: RPL3 is a core large-subunit ribosomal protein and is linked in the module to RPL6, RPL9, and BRIX1. It contributes to the globally corrected large-subunit and nucleolar terms (GO:CC nucleolus; q_global = 0.000916) (GO:CC cytosolic large ribosomal subunit; q_global = 0.00196) (GO:CC large ribosomal subunit; q_global = 0.0227) and has very strong STRING relationships with the other large-subunit proteins. It is detected by HPA in both brain and ovary and has the largest literature volume among the selected genes, together with disease associations including neuromuscular and infectious-disease contexts.
- **Conclusion**: Established: RPL3 represents the mature large-ribosomal-subunit output side of the module and strengthens the interpretation that the network extends from nucleolar assembly factors to ribosome components. Hypothesis: coordinated RPL3 abundance may reflect altered ribosome availability or translational capacity, but it does not by itself establish altered translation.

## Module 10

**Tissue pair**: brain and ovary  
**Genes (15)**: CD2AP, CHD4, DHX9, FIP1L1, HNRNPH1, EIF6, PRPF4, RBM39, RPAP3, SF3B3, SNRNP40, SUPT16H, TMOD3, EFTUD2, ZNF326

### Function

This is a nuclear RNA-processing and pre-mRNA-splicing module, with particularly strong evidence for spliceosome and spliceosomal snRNP activity. The primary evidence is the convergence of (GO:BP mRNA processing; q_global = 0.000183) through (GO:BP mRNA metabolic process; q_global = 0.00196) on mRNA processing, RNA splicing, and RNA metabolism, together with (GO:CC spliceosomal snRNP complex; q_global = 0.0095) through (GO:CC small nuclear ribonucleoprotein complex; q_global = 0.0142) and (GO:CC spliceosomal complex; q_global = 0.0247) through (GO:CC spliceosomal tri-snRNP complex; q_global = 0.0486) on spliceosomal, U two, and tri-snRNP complexes. The module also includes genes involved in transcriptional elongation, chromatin remodeling, RNA helicase activity, RNA binding, and messenger-RNA three-prime-end processing. Thus, the most defensible interpretation is a conserved core RNA maturation program rather than a tissue-specific signaling pathway. The broad RNA-biosynthetic terms (GO:BP RNA biosynthetic process; q_global = 0.0196), (GO:BP nucleic acid biosynthetic process; q_global = 0.0277), and (GO:BP RNA metabolic process; q_global = 0.045) are consistent with coupling between transcription and downstream RNA processing. The module is biologically coherent even though some members do not individually carry the enriched annotations.

**Cell composition.** The module is not composed of plasma or secreted proteins: HPA reports no secreted genes. It is also not strongly blood-cell specific, with almost all genes showing low immune-cell specificity and only one showing immune-cell enhancement. Most genes have low tissue specificity, and protein detection is present in brain for the entire module and in ovary for nearly the entire module. This supports a broadly expressed intracellular program rather than a blood-contamination explanation. Cell-type enhancements are heterogeneous, including glial, retinal, germ-cell, epithelial, enterocyte, and erythrocyte-progenitor categories. These annotations may reflect expression differences among cell types, but they do not displace the stronger common nuclear RNA-processing interpretation. The module may therefore reflect a shared requirement for RNA maturation across brain and ovary, with some peripheral cell-type contributions.

**GO/KEGG enrichment**: 18 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP mRNA processing | 0.000183 | DHX9, EFTUD2, FIP1L1, HNRNPH1, PRPF4, RBM39, SF3B3, SNRNP40, ZNF326 |
| GO:BP RNA splicing | 0.000879 | DHX9, EFTUD2, HNRNPH1, PRPF4, RBM39, SF3B3, SNRNP40, ZNF326 |
| GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile | 0.00101 | DHX9, EFTUD2, HNRNPH1, PRPF4, RBM39, SF3B3, SNRNP40 |
| GO:BP mRNA splicing, via spliceosome | 0.00101 | DHX9, EFTUD2, HNRNPH1, PRPF4, RBM39, SF3B3, SNRNP40 |
| GO:BP RNA splicing, via transesterification reactions | 0.00107 | DHX9, EFTUD2, HNRNPH1, PRPF4, RBM39, SF3B3, SNRNP40 |
| GO:BP RNA processing | 0.00141 | DHX9, EFTUD2, EIF6, FIP1L1, HNRNPH1, PRPF4, RBM39, SF3B3, SNRNP40, ZNF326 |
| GO:BP mRNA metabolic process | 0.00196 | DHX9, EFTUD2, FIP1L1, HNRNPH1, PRPF4, RBM39, SF3B3, SNRNP40, ZNF326 |
| GO:CC spliceosomal snRNP complex | 0.0095 | EFTUD2, PRPF4, SF3B3, SNRNP40 |
| GO:CC small nuclear ribonucleoprotein complex | 0.0142 | EFTUD2, PRPF4, SF3B3, SNRNP40 |
| GO:BP RNA biosynthetic process | 0.0196 | CHD4, DHX9, EFTUD2, EIF6, FIP1L1, HNRNPH1, PRPF4, RBM39, SF3B3, SNRNP40, SUPT16H, ZNF326 |
| GO:CC spliceosomal complex | 0.0247 | EFTUD2, HNRNPH1, PRPF4, SF3B3, SNRNP40 |
| GO:CC Sm-like protein family complex | 0.0252 | EFTUD2, PRPF4, SF3B3, SNRNP40 |
| GO:BP nucleic acid biosynthetic process | 0.0277 | CHD4, DHX9, EFTUD2, EIF6, FIP1L1, HNRNPH1, PRPF4, RBM39, SF3B3, SNRNP40, SUPT16H, ZNF326 |
| GO:CC catalytic step 2 spliceosome | 0.0371 | EFTUD2, HNRNPH1, SF3B3, SNRNP40 |
| GO:BP RNA metabolic process | 0.045 | CHD4, DHX9, EFTUD2, EIF6, FIP1L1, HNRNPH1, PRPF4, RBM39, SF3B3, SNRNP40, SUPT16H, ZNF326 |

### STRING and hu.MAP

STRING provides an internally consistent interaction backbone for the spliceosomal portion of the module. EFTUD2, PRPF4, SF3B3, and SNRNP40 form especially well-supported relationships, while DHX9, HNRNPH1, RBM39, and ZNF326 provide an RNA-processing and regulatory neighborhood. The STRING enrichment results (STRING Keyword mRNA processing; within-query FDR = 9.74e-07) through (STRING Process RNA splicing; within-query FDR = 0.00029), (STRING Process RNA processing; within-query FDR = 0.00051), (STRING Keyword Spliceosome; within-query FDR = 0.00077), and (STRING Process mRNA splicing, via spliceosome; within-query FDR = 0.002) independently agree with mRNA processing and spliceosome biology, but they remain supplementary evidence rather than globally corrected enrichment. hu.MAP independently places PRPF4, EFTUD2, SF3B3, and SNRNP40 together in a spliceosomal complex in (hu.MAP huMAP3_08980.1), with EFTUD2 and SNRNP40 recurring across additional complexes in (hu.MAP huMAP3_00424.1) through (hu.MAP huMAP3_09945.1) and PRPF4 with SF3B3 in (hu.MAP huMAP3_06511.1). These results indicate that part of the module corresponds to a known physical and functional spliceosomal machinery. The weaker or absent external links for genes such as TMOD3, CD2AP, EIF6, RPAP3, and several transcriptional regulators suggest that the co-abundance module is broader than a single canonical complex and may capture coordinated cellular state in addition to direct physical binding.

**STRING interactions (score >= 0.7)**: 12 of 105 gene pairs: CHD4–SUPT16H (0.815); DHX9–HNRNPH1 (0.878); DHX9–RBM39 (0.909); DHX9–SF3B3 (0.73); EFTUD2–PRPF4 (0.999); EFTUD2–RPAP3 (0.762); EFTUD2–SF3B3 (0.999); EFTUD2–SNRNP40 (0.999); HNRNPH1–ZNF326 (0.838); PRPF4–SF3B3 (0.995); PRPF4–SNRNP40 (0.986); SF3B3–SNRNP40 (0.852)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword mRNA processing (FDR = 9.74e-07, 9 genes); WikiPathways mRNA processing (FDR = 2.39e-06, 7 genes); Keyword mRNA splicing (FDR = 2.58e-06, 8 genes); RCTM mRNA Splicing - Major Pathway (FDR = 8.43e-05, 7 genes); RCTM Processing of Capped Intron-Containing Pre-mRNA (FDR = 8.43e-05, 8 genes); Process mRNA processing (FDR = 0.00014, 9 genes); Process RNA splicing (FDR = 0.00029, 8 genes); COMPARTMENTS Nucleoplasm (FDR = 0.00033, 10 genes); COMPARTMENTS Nuclear lumen (FDR = 0.00033, 12 genes); Process RNA processing (FDR = 0.00051, 10 genes); Keyword Spliceosome (FDR = 0.00077, 5 genes); Process Gene expression (FDR = 0.0013, 12 genes); Process RNA metabolic process (FDR = 0.0013, 11 genes); Keyword Isopeptide bond (FDR = 0.0013, 10 genes); Process mRNA splicing, via spliceosome (FDR = 0.002, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (PRPF4, EFTUD2, SF3B3, SNRNP40; 4/97); huMAP3_00424.1 (EFTUD2, SNRNP40; 2/8); huMAP3_00960.1 (EFTUD2, SNRNP40; 2/8); huMAP3_07622.1 (EFTUD2, SNRNP40; 2/9); huMAP3_08501.1 (EFTUD2, SNRNP40; 2/47); huMAP3_09504.1 (EFTUD2, SNRNP40; 2/51); huMAP3_09945.1 (EFTUD2, SNRNP40; 2/61); huMAP3_06511.1 (PRPF4, SF3B3; 2/79)

### Novelty

The spliceosomal function itself is not a new biological concept: the GO, STRING, and hu.MAP evidence identifies established RNA-processing machinery and known complex relationships. The fact sheet therefore does not justify calling the molecular function newly discovered. A potentially novel result is the reproducible co-abundance organization of this combination of spliceosomal, transcriptional, chromatin, and cytoskeletal or membrane-associated genes across brain and ovary. However, novelty of that cross-tissue module cannot be established from absence or presence in STRING or hu.MAP alone. Without an external publication or database comparison specifically describing this conserved brain-ovary module, the appropriate conclusion is that the module is a potentially novel systems-level observation, while its principal molecular components and their core interactions are established.

**Hypothesis.** Hypothesis: a shared demand for coordinated transcription, chromatin access, RNA processing, and spliceosome assembly creates the conserved brain-ovary co-abundance pattern. In this model, FACT-related transcriptional control through SUPT16H, chromatin remodeling through CHD4, RNA helicase and RNA-binding regulation through DHX9 and HNRNPH1, and spliceosomal assembly through EFTUD2, PRPF4, SF3B3, and SNRNP40 jointly maintain mature transcript production. RBM39 and ZNF326 could help couple transcriptional regulation to alternative splicing, while FIP1L1 could connect spliceosomal activity to messenger-RNA three-prime-end processing. The cytoskeletal or membrane-associated genes may represent cell-state coupling rather than members of the same physical complex. This hypothesis should be tested with tissue- and cell-type-resolved expression, perturbation of spliceosomal components, and measurement of transcript isoforms in brain and ovary.

### Important genes

#### SNRNP40

- **Related proteins** (co-abundance neighbors): FIP1L1 (0.89), RBM39 (0.84), EFTUD2 (0.84), SUPT16H (0.82), PRPF4 (0.81), HNRNPH1 (0.81), CHD4 (0.80), SF3B3 (0.80); STRING partners: EFTUD2 (0.999), PRPF4 (0.986), SF3B3 (0.852)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_00424.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 40. This gene encodes a component of the U5 small nuclear ribonucleoprotein (snRNP) particle. The U5 snRNP is part of the spliceosome, a multiprotein complex that catalyzes the removal of introns from pre-messenger RNAs. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.530); dengue disease (0.377); X-linked lymphoproliferative syndrome (0.058); autoimmune lymphoproliferative syndrome (0.055); Familial hemophagocytic lymphohistiocytosis (0.053)
- **Europe PMC papers**: 235
- **Why important**: SNRNP40 is the strongest network hub in the supplied subgraph and is connected to both the central spliceosomal genes and broader transcriptional or RNA-processing members. It appears in every primary enrichment term, in every supplementary STRING term, and across the recurring hu.MAP complexes (hu.MAP huMAP3_08980.1) through (hu.MAP huMAP3_09945.1). Its established function is as a U5 snRNP subunit involved in spliceosome assembly and intron removal. It has substantial literature support and disease-relevant links including neurodegenerative disease.
- **Conclusion**: Established evidence supports SNRNP40 as a central structural and functional marker of the module's spliceosomal core. It is a strong candidate for experimental perturbation. The hypothesis that its hub position explains the cross-tissue co-abundance pattern remains unproven.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): SNRNP40 (0.84); STRING partners: PRPF4 (0.999), RPAP3 (0.762), SF3B3 (0.999), SNRNP40 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_00424.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 is present in every primary GO term and every supplementary STRING term, has strong STRING relationships with PRPF4, SF3B3, and SNRNP40, and recurs across many hu.MAP complexes (hu.MAP huMAP3_08980.1) through (hu.MAP huMAP3_09945.1). It encodes a spliceosomal GTPase involved in tri-snRNP assembly and spliceosome conformational change. Its association with mandibulofacial dysostosis and microcephaly gives the module a direct human disease connection, particularly relevant to developmental biology and neural tissues. Its literature volume is substantial.
- **Conclusion**: Established evidence identifies EFTUD2 as a core spliceosomal component and a disease-relevant anchor of the module. A possible role in coordinating tissue-specific transcript maturation is a hypothesis, not demonstrated by the co-abundance data alone.

#### PRPF4

- **Related proteins** (co-abundance neighbors): RPAP3 (0.82), SNRNP40 (0.81); STRING partners: EFTUD2 (0.999), SF3B3 (0.995), SNRNP40 (0.986)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_06511.1
- **Function (MyGene.info)**: pre-mRNA splicing tri-snRNP complex factor PRPF4. The protein encoded by this gene is part of a heteromeric complex that binds U4, U5, and U6 small nuclear RNAs and is involved in pre-mRNA splicing. The encoded protein also is a mitotic checkpoint protein and a regulator of chemoresistance in human ovarian cancer. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: retinitis pigmentosa (0.634); retinitis pigmentosa 70 (0.578); inherited retinal dystrophy (0.377); neurodegenerative disease (0.203); refractive error (0.083)
- **Europe PMC papers**: 461
- **Why important**: PRPF4 is present in nearly all primary enrichment terms, has very strong STRING links to EFTUD2, SF3B3, and SNRNP40, and occurs in the spliceosomal hu.MAP complexes (hu.MAP huMAP3_08980.1) and (hu.MAP huMAP3_06511.1). Its established function is participation in the U4, U5, and U6 tri-snRNP and spliceosomal assembly. It also has disease associations involving retinal degeneration and neurodegenerative disease, making it particularly informative for the brain component and the retinally enriched context elsewhere in the module. Its literature support is substantial.
- **Conclusion**: Established evidence supports PRPF4 as a core tri-snRNP assembly factor and a plausible bridge between the module's network structure and its brain-related disease relevance. The suggestion that altered PRPF4 abundance drives the shared brain-ovary module is a hypothesis requiring direct testing.

#### SF3B3

- **Related proteins** (co-abundance neighbors): SUPT16H (0.81), SNRNP40 (0.80); STRING partners: DHX9 (0.73), EFTUD2 (0.999), PRPF4 (0.995), SNRNP40 (0.852)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Nucleoli rim; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_06511.1
- **Function (MyGene.info)**: splicing factor 3b subunit 3. This gene encodes subunit 3 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); dengue disease (0.370); cervical cancer (0.189); cervical carcinoma (0.189); prostate cancer (0.111)
- **Europe PMC papers**: 965
- **Why important**: SF3B3 is repeatedly represented in the primary RNA-processing and spliceosomal terms, has very strong STRING relationships with EFTUD2, PRPF4, and SNRNP40, and appears in (hu.MAP huMAP3_08980.1) and (hu.MAP huMAP3_06511.1). It is a component of the SF3B complex and U2 snRNP that helps anchor the spliceosome near the intron branch site. Its disease associations include neurodegenerative disease and cancer, and its literature volume is substantial. HPA detects the protein in both tissues and places it in nuclear compartments compatible with its established function.
- **Conclusion**: Established evidence supports SF3B3 as a central U2-spliceosome component and a robust molecular indicator of the module's RNA-splicing function. Its precise contribution to conservation between brain and ovary remains a hypothesis.

#### DHX9

- **Related proteins** (co-abundance neighbors): SUPT16H (0.82); STRING partners: HNRNPH1 (0.878), RBM39 (0.909), SF3B3 (0.73)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 links RNA processing with transcriptional regulation and nucleic-acid metabolism. It is included in many primary GO terms, has STRING relationships with HNRNPH1, RBM39, and SF3B3, and is connected in the module to the transcriptional elongation factor SUPT16H. Its established enzymatic activity is ATP-dependent unwinding of RNA-containing duplexes, and its annotations include alternative splicing and transcriptional regulation. It has extensive literature support and disease associations involving neurodevelopment and neurodegeneration.
- **Conclusion**: Established evidence supports DHX9 as a regulatory RNA helicase that could connect spliceosomal activity with transcription and RNA export. Its position as a mechanistic coordinator in this particular conserved module is a hypothesis rather than a demonstrated causal relationship.

## Module 11

**Tissue pair**: brain and ovary  
**Genes (7)**: DDX5, RFC2, QARS1, CCT5, CCT3, CCT7, CCT8

### Function

The strongest interpretation is a conserved intracellular proteostasis and nuclear RNA–DNA maintenance module. The core signal is the CCT/TRiC chaperonin: CCT3, CCT5, CCT7, and CCT8 jointly support ATP-dependent folding and protein stabilization, with especially strong support from (GO:CC chaperonin-containing T-complex; q_global = 4.24e-07), (GO:MF ATP-dependent protein folding chaperone; q_global = 7.41e-05), (GO:CC protein folding chaperone complex; q_global = 0.000156), (GO:MF protein folding chaperone; q_global = 0.00054), (GO:MF unfolded protein binding; q_global = 0.00159), (GO:BP protein stabilization; q_global = 0.0187), and (GO:BP protein folding; q_global = 0.0215). The same core is associated with RNA localization to Cajal bodies, telomerase-RNA localization, telomere maintenance, and regulation of DNA biosynthesis in (12 globally significant GO/KEGG terms, q_global 4.24e-07–1.46e-06; see the table), (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 3.52e-06) (GO:BP regulation of DNA biosynthetic process; q_global = 3.62e-06), (GO:BP positive regulation of telomere maintenance via telomere lengthening; q_global = 6.81e-06) (GO:BP regulation of telomere maintenance via telomerase; q_global = 2.88e-05), (6 globally significant GO/KEGG terms, q_global 4.06e-05–0.000124; see the table), (GO:BP positive regulation of telomere maintenance; q_global = 0.00033), (GO:BP regulation of telomere maintenance; q_global = 0.00115), (GO:BP positive regulation of chromosome organization; q_global = 0.00159), and (8 globally significant GO/KEGG terms, q_global 0.00334–0.00578; see the table). RFC2 adds a DNA replication and DNA metabolic component, while DDX5 adds RNA helicase, RNA processing, splicing, and transcriptional regulatory functions according to the gene-level annotations. QARS1 contributes translational capacity through glutaminyl-tRNA aminoacylation. The fertilization, sperm–zona-pellucida, and cell-recognition terms are globally significant in (GO:BP binding of sperm to zona pellucida; q_global = 3.52e-06), (GO:BP sperm-egg recognition; q_global = 6.81e-06), (GO:BP cell-cell recognition; q_global = 4.06e-05), (GO:BP cell recognition; q_global = 0.000235), (GO:BP single fertilization; q_global = 0.000279), (GO:BP fertilization; q_global = 0.00115), and (GO:CC zona pellucida receptor complex; q_global = 0.0117), but they are driven largely by the CCT quartet and should not be treated as evidence that this is a gamete-specific fertilization module. Overall, the evidence supports a general chaperone-centered module linked to proteome maintenance and nuclear information processing, with reproductive and telomere-related annotations requiring cautious interpretation.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and all module proteins are detected in both brain and ovary. It is also not blood-cell enriched; every gene has low immune-cell specificity. All genes have low tissue specificity, which argues against a narrowly brain- or ovary-restricted program. The module is therefore compatible with broadly expressed housekeeping or proliferative-cell biology, especially protein folding, RNA handling, translation, and DNA maintenance. HPA cell-type enhancement in oocytes, spermatogenic populations, and cytotrophoblast populations may indicate activity in particular developmental or reproductive cell states, but it does not establish that the shared brain–ovary signal originates from those cell types. The shared module may consequently reflect conserved cellular composition or general biosynthetic demand rather than a tissue-specific brain–ovary mechanism.

**GO/KEGG enrichment**: 65 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chaperonin-containing T-complex | 4.24e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 4.24e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 4.24e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of DNA biosynthetic process | 5.13e-07 | CCT3, CCT5, CCT7, CCT8, RFC2 |
| GO:BP RNA localization to Cajal body | 1.46e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 1.46e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 1.46e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 1.46e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 1.46e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 1.46e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 1.46e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 1.46e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 1.46e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP binding of sperm to zona pellucida | 3.52e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 3.52e-06 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING provides direct high-confidence support for the complete CCT subnetwork among CCT3, CCT5, CCT7, and CCT8, consistent with a known CCT/TriC complex rather than an unexplained collection of genes. STRING functional annotations independently recover the TCP chaperonin family, the chaperonin-containing T-complex, actin folding by CCT, cellular proteostasis, and the telomere-related annotations (15 supplementary STRING terms; within-query FDR 4e-07–5.66e-06). These STRING results are supplementary and corroborate the globally corrected GO evidence; their within-query FDR must not be interpreted as global enrichment significance. hu.MAP independently places the same CCT quartet together in several complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1), with a smaller overlapping complex in (hu.MAP huMAP3_01951.1). The complexes include other CCT subunits, TCP1, prefoldin- or tubulin-related components, and proteins associated with trafficking, cytoskeletal organization, and regulation. Thus, the network is strongly anchored in a known multisubunit chaperonin assembly. In contrast, DDX5, RFC2, and QARS1 have no reported STRING partners or hu.MAP complexes in this module’s supplied evidence, so their links may represent co-abundance relationships, indirect biology, or context-specific associations rather than established physical interactions.

**STRING interactions (score >= 0.7)**: 6 of 21 gene pairs: CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam TCP-1/cpn60 chaperonin family (FDR = 4e-07, 4 genes); Component Chaperonin-containing T-complex (FDR = 9.26e-07, 4 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 1e-06, 4 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 1.6e-06, 4 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 1.6e-06, 4 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 1.6e-06, 4 genes); InterPro GroEL-like apical domain superfamily (FDR = 1.6e-06, 4 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 1.6e-06, 4 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 1.6e-06, 4 genes); RCTM Folding of actin by CCT/TriC (FDR = 2.37e-06, 4 genes); TISSUES Lymphoblast (FDR = 2.81e-06, 6 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis (FDR = 2.99e-06, 4 genes); Process Binding of sperm to zona pellucida (FDR = 5.66e-06, 4 genes); Process Positive regulation of telomere maintenance via telomerase (FDR = 5.66e-06, 4 genes); Process Positive regulation of establishment of protein localization to telomere (FDR = 5.66e-06, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8)

### Novelty

The module is unlikely to represent discovery of a new CCT complex: its central CCT relationships are already well established by STRING and hu.MAP, and the CCT quartet is a canonical chaperonin assembly. The potentially novel aspect is the reproducible co-abundance configuration shared by brain and ovary, particularly the association of the CCT core with DDX5, RFC2, and QARS1 in this tissue pair. That association should be described as a candidate context-specific module, not as a newly discovered physical complex or a proven brain–ovary mechanism. Absence of DDX5, RFC2, and QARS1 from the supplied STRING and hu.MAP relationships does not prove novelty, because database coverage, experimental context, and indirect regulation can all limit detection. The evidence supports novelty at the level of the tissue-pair co-abundance pattern, while established biology explains much of its central structure.

**Hypothesis.** Hypothesis: in shared brain and ovary cellular populations, increased demand for proteome quality control engages the CCT/TRiC chaperonin core, while DDX5 coordinates RNA processing and nuclear RNA handling, RFC2 supports replication-associated DNA transactions, and QARS1 sustains translation. Through this coordinated state, CCT-dependent folding could support proteins involved in Cajal-body and telomere processes, producing the observed co-abundance pattern. The reproductive and telomere annotations may reflect shared requirements of highly active or developmentally specialized cells rather than a direct fertilization function. This hypothesis predicts that the module will track cellular biosynthetic or proliferative state and that perturbing the CCT core will alter selected RNA-processing, replication, and telomere-associated outputs. These mechanistic links remain hypotheses and are not established by co-abundance alone.

### Important genes

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT3 (0.94), CCT8 (0.92), CCT7 (0.87); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is a central network member with strong connections to the other CCT subunits and participation in every supplied hu.MAP complex containing the module core. It belongs to the CCT/TRiC ATP-dependent folding machine supported by (GO:CC chaperonin-containing T-complex; q_global = 4.24e-07), (GO:MF ATP-dependent protein folding chaperone; q_global = 7.41e-05), (GO:CC protein folding chaperone complex; q_global = 0.000156), (GO:MF protein folding chaperone; q_global = 0.00054), (GO:MF unfolded protein binding; q_global = 0.00159), (GO:BP protein stabilization; q_global = 0.0187), and (GO:BP protein folding; q_global = 0.0215). It has extensive literature coverage and a disease association with hereditary sensory and autonomic neuropathy with spastic paraplegia, making it especially relevant to the brain component.
- **Conclusion**: Established evidence supports CCT5 as a core structural and functional component of the module and as a plausible contributor to proteostasis in brain and ovary. Its disease association makes it biologically important, but the module does not establish that CCT5 causes the tissue-pair co-abundance pattern or mediates the telomere and reproductive annotations.

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT5 (0.94), CCT8 (0.84); STRING partners: CCT5 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is part of the tightly supported CCT quartet, has direct STRING relationships with the other core subunits, and appears in all supplied hu.MAP complexes containing the complete quartet. It participates across the globally significant chaperone, Cajal-body, telomere, DNA-biosynthetic, and cell-recognition annotations. Its substantial literature and associations with neurodevelopmental and neurodegenerative disorders increase its relevance to a brain–ovary module.
- **Conclusion**: Established evidence identifies CCT3 as a core chaperonin component whose co-abundance is most parsimoniously interpreted through the known CCT complex. A role in coupling chaperone activity to nuclear RNA or telomere biology is plausible from the annotations, but remains a hypothesis rather than a demonstrated causal function in this module.

#### CCT7

- **Related proteins** (co-abundance neighbors): CCT5 (0.87), CCT8 (0.85), DDX5 (0.82); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is a highly connected core member and is linked to CCT3, CCT5, and CCT8 by STRING, while also appearing in all supplied hu.MAP complexes containing the core. HPA reports cell-type enhancement in spermatogenic populations, and the gene has associations with neurodegenerative disease, preeclampsia, and other disorders. Its participation in the CCT, telomere, and protein-folding evidence makes it an important bridge between general proteostasis and reproductive-cell observations.
- **Conclusion**: Established evidence supports CCT7 as a central CCT subunit expressed in both tissues and relevant to the module’s conserved chaperone signal. The spermatogenic association may indicate a broader developmental or germ-cell state, but it does not demonstrate a specific reproductive mechanism in brain or ovary.

#### DDX5

- **Related proteins** (co-abundance neighbors): CCT7 (0.82), RFC2 (0.82), QARS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 is a network bridge linking the CCT-connected portion to RFC2 and QARS1. Unlike the CCT genes, it is a DEAD-box RNA helicase with established roles in RNA-structure remodeling, transcriptional coregulation, splicing, and small noncoding-RNA processing. It contributes to the globally significant ATP- and nucleotide-related terms and has the largest literature volume among the module genes, together with multiple infectious-disease and cancer associations.
- **Conclusion**: Established evidence supports DDX5 as an RNA-processing and nuclear regulatory component that may explain why the module extends beyond chaperone biology. Its absence from the supplied STRING and hu.MAP relationships means the specific connection to the CCT core is not established as a physical interaction; a co-regulated RNA-processing role is therefore the more cautious interpretation.

#### RFC2

- **Related proteins** (co-abundance neighbors): DDX5 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: replication factor C subunit 2. This gene encodes a member of the activator 1 small subunits family. The elongation of primed DNA templates by DNA polymerase delta and epsilon requires the action of the accessory proteins, proliferating cell nuclear antigen (PCNA) and replication factor C (RFC). Replication factor C, also called activator 1, is a protein complex consisting of five distinct subunits. This gene encodes the 40 kD s…
- **Diseases (Open Targets)**: neurodegenerative disease (0.509); ovarian dysfunction (0.202); hypotensive disorder (0.170); hepatocellular carcinoma (0.087); colorectal carcinoma (0.085)
- **Europe PMC papers**: 1272
- **Why important**: RFC2 is the module’s clearest replication-associated gene. Its annotations support DNA replication, replication-checkpoint signaling, DNA repair, and stimulation of DNA polymerase activity, and it contributes to the globally significant DNA-biosynthetic and DNA-metabolic terms (GO:BP positive regulation of DNA biosynthetic process; q_global = 5.13e-07), (GO:BP regulation of DNA biosynthetic process; q_global = 3.62e-06), (GO:BP DNA biosynthetic process; q_global = 7.05e-05), (GO:BP positive regulation of DNA metabolic process; q_global = 0.000824), and (GO:BP regulation of DNA metabolic process; q_global = 0.00578). It is connected to DDX5 in the co-abundance network and has an association with ovarian dysfunction as well as neurological disease.
- **Conclusion**: Established evidence supports RFC2 as a DNA replication and repair factor that broadens the module beyond proteostasis. The network suggests coordination between RNA processing and replication-related activity, but does not prove that RFC2 is functionally regulated by the CCT quartet or that this module directly drives ovarian dysfunction.

## Module 12

**Tissue pair**: brain and ovary  
**Genes (5)**: ELMO2, MCCC1, DBT, HSPG2, TFAM

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established canonical pathway assignment. The genes instead indicate a mixed biological signal involving mitochondrial genome maintenance and transcription through TFAM, branched-chain amino-acid catabolism through DBT and MCCC1, extracellular-matrix organization through HSPG2, and cytoskeletal organization or cell motility through ELMO2. TFAM is the central co-abundance connector, while the remaining relationships form separate metabolic, extracellular, and motility-associated links. The most defensible interpretation is therefore a shared abundance program or composite cellular-state signal rather than a demonstrated single biochemical pathway. The supplementary STRING term (STRING Pfam Biotin-requiring enzyme; within-query FDR = 0.0411), involving DBT and MCCC1 and biotin-requiring enzymes, is directionally consistent with the metabolic component but is not globally corrected enrichment evidence.

**Cell composition.** The module is not predominantly composed of plasma proteins, secreted proteins, or blood-cell-specific proteins. Most genes have low tissue specificity, most have low immune-cell specificity, and only HSPG2 is annotated as secreted to the extracellular matrix. HSPG2 is tissue-enhanced in blood vessel, whereas the cell-type annotations are heterogeneous and include epithelial, neutrophil, alveolar, parietal, prostatic, adipocyte, stromal, trophoblast, and spermatid populations. This heterogeneity does not support a simple blood-contamination explanation, although shared vascular, epithelial, stromal, or other cellular composition could contribute to the brain–ovary co-abundance pattern. Protein detection is broad in brain and nearly broad in ovary, with DBT being the ovary exception in the supplied immunohistochemistry summary. Overall, the module is mainly intracellular and broadly detected, with one extracellular-matrix component rather than a coherent blood or secretome signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no hu.MAP complex containing multiple module members. Thus, the co-abundance edges are not supported by established physical or functional interactions in those resources. The lack of curated links argues against interpreting the graph as a known protein complex. It may instead reflect coordinated expression, shared cellular composition, indirect metabolic or structural coupling, or a statistical pattern specific to the tissue datasets. The supplementary STRING annotation (STRING Pfam Biotin-requiring enzyme; within-query FDR = 0.0411) connects DBT and MCCC1 at the functional-category level through biotin-requiring enzymes, but this does not establish a direct interaction or global enrichment.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam Biotin-requiring enzyme (FDR = 0.0411, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The co-abundance pattern appears potentially novel as a cross-tissue module because it has no matching multi-member hu.MAP complex and no high-confidence STRING relationships among its members. However, that absence alone does not prove biological novelty: the genes themselves have established functions, disease associations, and substantial prior literature, and the module may reflect a new combination of known genes or a tissue-specific expression pattern rather than a new molecular mechanism. The strongest novelty claim is therefore limited to the observed brain–ovary co-abundance organization, not to the individual gene functions or to a newly discovered protein complex.

**Hypothesis.** Hypothesis: the module represents a shared cellular-state program in brain and ovary in which mitochondrial activity and metabolic substrate handling are coordinated with extracellular-matrix and cell-motility context. TFAM may mark the mitochondrial transcriptional or energetic component; DBT and MCCC1 may capture branched-chain amino-acid and biotin-dependent metabolic capacity; HSPG2 may reflect vascular or stromal extracellular-matrix context; and ELMO2 may reflect cytoskeletal remodeling or migratory activity. The inferred co-abundance could therefore arise from coordinated metabolic demand and tissue-cellular composition rather than direct protein binding. This hypothesis requires validation with independent datasets, cell-type deconvolution, perturbation experiments, and measurements of mitochondrial and branched-chain-amino-acid flux.

### Important genes

#### TFAM

- **Related proteins** (co-abundance neighbors): DBT (0.87), MCCC1 (0.84), HSPG2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transcription factor A, mitochondrial. This gene encodes a key mitochondrial transcription factor containing two high mobility group motifs. The encoded protein also functions in mitochondrial DNA replication and repair. Sequence polymorphisms in this gene are associated with Alzheimer's and Parkinson's diseases. There are pseudogenes for this gene on chromosomes 6, 7, and 11. Alternative splicing results in multiple transcript variant…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome 15 (hepatocerebral type) (0.689); neurodegenerative disease (0.550); stroke disorder (0.191); alcohol drinking (0.189); musculoskeletal system disorder (0.132)
- **Europe PMC papers**: 14423
- **Why important**: TFAM has the strongest central network position in the supplied module and connects to DBT, MCCC1, and HSPG2. It is a mitochondrial transcription factor involved in mitochondrial DNA replication and repair, with annotations related to mitochondrial transcription, hypoxia response, and nutrient response. Its associations with mitochondrial DNA depletion syndrome and neurodegenerative disease, together with extensive literature, make it the most informative candidate for the module's mitochondrial component.
- **Conclusion**: Established evidence supports TFAM as a mitochondrial genome-maintenance and transcription factor and as the module's central co-abundance connector. It is plausible, but not established, that TFAM coordinates the other module components or explains the cross-tissue signal.

#### DBT

- **Related proteins** (co-abundance neighbors): TFAM (0.87), ELMO2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dihydrolipoamide branched chain transacylase E2. The branched-chain alpha-keto acid dehydrogenase complex (BCKD) is an inner-mitochondrial enzyme complex involved in the breakdown of the branched-chain amino acids isoleucine, leucine, and valine. The BCKD complex is thought to be composed of a core of 24 transacylase (E2) subunits, and associated decarboxylase (E1), dehydrogenase (E3), and regulatory subunits. This gene encodes the transacylase …
- **Diseases (Open Targets)**: maple syrup urine disease (0.710); maple syrup urine disease type 1A (0.695); maple syrup urine disease type 2 (0.659); intermittent maple syrup urine disease (0.370); classic maple syrup urine disease (0.370)
- **Europe PMC papers**: 15522
- **Why important**: DBT is a mitochondrial E2 component of the branched-chain alpha-keto-acid dehydrogenase complex and is directly linked in the module to TFAM and ELMO2. It contributes the clearest enzymatic interpretation of branched-chain amino-acid catabolism and is the subject of strong disease evidence for maple syrup urine disease. DBT also participates in the supplementary STRING category (STRING Pfam Biotin-requiring enzyme; within-query FDR = 0.0411) with MCCC1 and has extensive literature support.
- **Conclusion**: Established evidence supports DBT as a mitochondrial branched-chain-amino-acid catabolic enzyme. Its module relationship to TFAM and ELMO2 is a co-abundance observation, not evidence that these proteins form a physical complex or that DBT drives the entire module.

#### MCCC1

- **Related proteins** (co-abundance neighbors): TFAM (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methylcrotonyl-CoA carboxylase subunit 1. This gene encodes the large subunit of 3-methylcrotonyl-CoA carboxylase. This enzyme functions as a heterodimer and catalyzes the carboxylation of 3-methylcrotonyl-CoA to form 3-methylglutaconyl-CoA. Mutations in this gene are associated with 3-Methylcrotonylglycinuria, an autosomal recessive disorder of leucine catabolism. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: 3-methylcrotonyl-CoA carboxylase deficiency (0.856); hereditary disease (0.452); Parkinson disease (0.404); neurodegenerative disease (0.387); Lewy body dementia (0.214)
- **Europe PMC papers**: 756
- **Why important**: MCCC1 is the large subunit of methylcrotonyl-CoA carboxylase and participates in leucine and branched-chain-amino-acid catabolism as well as biotin metabolism. It is connected to TFAM and shares the supplementary STRING annotation (STRING Pfam Biotin-requiring enzyme; within-query FDR = 0.0411) with DBT, providing the most coherent metabolic pair in the module. Its association with methylcrotonyl-CoA carboxylase deficiency and neurodegenerative disease adds disease relevance, even though its literature volume is more limited than that of TFAM or DBT.
- **Conclusion**: Established evidence supports MCCC1 as a mitochondrial leucine-catabolism enzyme and as part of the supplementary biotin-enzyme signal. A coordinated metabolic relationship with DBT is plausible, but global enrichment and direct module-level mechanistic coupling are not established.

#### HSPG2

- **Related proteins** (co-abundance neighbors): TFAM (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 is the module's extracellular-matrix and vascular-context gene. It is tissue-enhanced in blood vessel, is secreted to the extracellular matrix, and encodes perlecan, a multidomain proteoglycan that binds and cross-links extracellular-matrix and cell-surface components. Its connection to the central TFAM node is notable because it links the mitochondrial-associated portion of the graph to tissue architecture, angiogenesis, development, and cell differentiation. It also has substantial literature and disease associations including Schwartz-Jampel syndrome and dyssegmental dysplasia.
- **Conclusion**: Established evidence supports HSPG2 as an extracellular-matrix organizer with vascular and developmental relevance. Its co-abundance with TFAM may reflect shared tissue or cellular state rather than a direct molecular interaction; linking it mechanistically to mitochondrial regulation remains a hypothesis.

#### ELMO2

- **Related proteins** (co-abundance neighbors): DBT (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: engulfment and cell motility 2. The protein encoded by this gene interacts with the dedicator of cyto-kinesis 1 protein. Similarity to a C. elegans protein suggests that this protein may function in phagocytosis of apoptotic cells and in cell migration. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: primary intraosseous venous malformation (0.667); neurodegenerative disease (0.504); cutaneous leishmaniasis (0.462); Parkinson disease (0.456); Alzheimer disease (0.456)
- **Europe PMC papers**: 452
- **Why important**: ELMO2 provides the module's cell-motility and cytoskeletal component and is connected to DBT. Its annotated functions include actin-filament organization, chemotaxis, phagocytosis, and cell migration. The HPA cell-type annotations are heterogeneous, including esophageal apical cells and neutrophils, while disease associations include neurodegenerative disease and vascular malformation. Although its literature volume is more limited, it may help explain a cell-composition or remodeling component that is not captured by the mitochondrial genes.
- **Conclusion**: Established evidence supports ELMO2 in cytoskeletal organization and cell motility. Its association with DBT in this module is a co-abundance relationship without STRING or hu.MAP support, so any metabolic-motility coupling should be treated as a hypothesis.

## Module 13

**Tissue pair**: brain and ovary  
**Genes (7)**: KPNA2, MCM2, MCM4, MCM5, MCM6, MCM7, NASP

### Function

This is a DNA-replication and genome-maintenance module centered on the MCM helicase complex. The primary evidence is exceptionally coherent: the MCM complex, CMG complex, replication preinitiation, DNA-replication initiation, DNA helicase activity, homologous recombination, recombinational repair, chromosome biology, and cell-cycle replication terms all pass global correction (GO:CC MCM complex; q_global = 1.58e-09) through (GO:MF ribonucleoside triphosphate phosphatase activity; q_global = 0.0493). Five MCM genes account for the dominant signal, while the broader DNA-replication and DNA-metabolism terms also include KPNA2 and NASP (GO:BP DNA recombination; q_global = 2.52e-05), (GO:BP DNA replication; q_global = 4.71e-05), (GO:BP DNA metabolic process; q_global = 0.000166), (GO:BP regulation of DNA metabolic process; q_global = 0.000192), (GO:CC chromosome; q_global = 0.0301). The module therefore most strongly represents licensing and operation of replication forks, with a related contribution from replication-associated DNA repair and chromatin handling. The enrichment does not by itself establish that every tissue sample was actively replicating; co-abundance can reflect the abundance of proliferating cells or shared progenitor-like cell states.

**Cell composition.** The module is not composed of plasma or secreted proteins: HPA reports no secreted genes, and all proteins are localized to the nucleoplasm where reported. It is also not strongly immune-cell specific according to HPA. However, its cellular composition is informative and potentially confounding for interpretation of a brain-and-ovary shared module. HPA associates most genes with tissue-enhanced expression in bone marrow or lymphoid tissue and with progenitor populations, especially erythrocyte, megakaryocyte, and monocyte progenitors. Several genes are also enhanced in trophoblast or germ-cell populations, and KPNA2 is associated with oocytes. This pattern is consistent with a broadly conserved proliferation program and raises the possibility that the shared signal reflects proliferating or progenitor-like cells, tissue admixture, or common cell-state composition rather than a brain-and-ovary-specific function. Protein detection is present for several genes in both tissues, but the tissue-level detection pattern is not uniform, so the module should not be interpreted as equally active in every cell type of either tissue.

**GO/KEGG enrichment**: 48 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC MCM complex | 1.58e-09 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP double-strand break repair via break-induced replication | 6.62e-09 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC CMG complex | 4.4e-08 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication initiation | 8.57e-08 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC DNA replication preinitiation complex | 8.57e-08 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication | 3.63e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF four-way junction helicase activity | 1.78e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF forked DNA-dependent helicase activity | 1.78e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF double-stranded DNA helicase activity | 2.28e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF 3'-5' DNA helicase activity | 2.28e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded 3'-5' DNA helicase activity | 2.28e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP DNA replication initiation | 4.51e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| KEGG DNA replication - Homo sapiens (human) | 5.52e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded DNA helicase activity | 6.7e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded DNA binding | 9.63e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |

### STRING and hu.MAP

STRING supports a dense, known MCM core: MCM2, MCM4, MCM5, MCM6, and MCM7 are mutually connected with very strong functional associations, and the supplementary STRING terms identify the MCM and CMG complexes, MCM domains, DNA unwinding, replication initiation, and break-induced replication (STRING Component MCM complex; within-query FDR = 3.46e-09) through (STRING Process DNA unwinding involved in DNA replication; within-query FDR = 1.26e-07). NASP has STRING links to MCM6 and MCM7, whereas KPNA2 has no STRING partner in this module. hu.MAP independently places the five MCM proteins together in multiple replication and CMG-related complexes (hu.MAP huMAP3_05529.1) through (hu.MAP huMAP3_08848.1), often alongside MCM3, CDC45, GINS proteins, TIMELESS, TIPIN, CLSPN, and MCMBP. hu.MAP also links NASP with MCM2 in a chromatin and histone-related complex (hu.MAP huMAP3_10747.1). Thus, most of the module is a partial observation of well-established replication machinery, while KPNA2 is connected mainly through the co-abundance network and NASP occupies a peripheral chromatin-associated position. These resources strongly support biological coherence, but they do not prove that all module edges are direct physical interactions or that co-abundance represents complex assembly in the sampled tissues.

**STRING interactions (score >= 0.7)**: 12 of 21 gene pairs: MCM2–MCM4 (0.999); MCM2–MCM5 (0.999); MCM2–MCM6 (0.999); MCM2–MCM7 (0.999); MCM4–MCM5 (0.999); MCM4–MCM6 (0.999); MCM4–MCM7 (0.999); MCM5–MCM6 (0.999); MCM5–MCM7 (0.999); MCM6–MCM7 (0.999); MCM6–NASP (0.709); MCM7–NASP (0.81)
**STRING functional enrichment (supplementary, within-query FDR)**: Component MCM complex (FDR = 3.46e-09, 5 genes); COMPARTMENTS MCM complex (FDR = 3.74e-09, 5 genes); InterPro MCM domain (FDR = 5.99e-09, 5 genes); InterPro Mini-chromosome maintenance, conserved site (FDR = 5.99e-09, 5 genes); InterPro MCM N-terminal domain (FDR = 5.99e-09, 5 genes); InterPro Mini-chromosome maintenance protein (FDR = 5.99e-09, 5 genes); InterPro MCM OB domain (FDR = 5.99e-09, 5 genes); InterPro MCM, AAA-lid domain (FDR = 5.99e-09, 5 genes); Component CMG complex (FDR = 8.81e-09, 5 genes); COMPARTMENTS CMG complex (FDR = 9.53e-09, 5 genes); RCTM Unwinding of DNA (FDR = 2.51e-08, 5 genes); Process Double-strand break repair via break-induced replication (FDR = 4.01e-08, 5 genes); Keyword DNA replication (FDR = 7.29e-08, 6 genes); Process Regulation of DNA-templated DNA replication initiation (FDR = 8.67e-08, 5 genes); Process DNA unwinding involved in DNA replication (FDR = 1.26e-07, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05529.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/6); huMAP3_14758.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/14); huMAP3_08554.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_11832.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_12180.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/17); huMAP3_06061.1 (MCM4, MCM7, MCM2, MCM6; 4/5); huMAP3_07113.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_11119.1 (MCM4, MCM5, MCM7, MCM6; 4/14); huMAP3_09860.1 (MCM4, MCM2, MCM6; 3/4); huMAP3_00154.1 (MCM4, MCM2, MCM6; 3/5); huMAP3_09466.1 (MCM4, MCM2, MCM6; 3/23); huMAP3_10862.1 (MCM4, MCM2, MCM6; 3/33); huMAP3_14306.1 (MCM4, MCM2, MCM6; 3/55); huMAP3_02602.1 (MCM4, MCM6; 2/2); huMAP3_09238.1 (MCM5, MCM7; 2/11); huMAP3_08848.1 (MCM4, MCM6; 2/15); huMAP3_10747.1 (NASP, MCM2; 2/25)

### Novelty

The molecular function is not a new discovery: the MCM core, the CMG-related machinery, replication initiation, and replication-associated repair are already well established in STRING, hu.MAP, MyGene.info annotations, and the literature. Absence of a KPNA2 interaction in STRING or the limited representation of NASP in the listed hu.MAP complexes would not establish novelty. The potentially novel aspect is the observation that this particular combination of replication-core genes with KPNA2 and NASP forms a conserved co-abundance module across brain and ovary. That cross-tissue organization may be a useful systems-level finding, but it cannot be called a new molecular mechanism without independent replication, comparison with other tissues, cell-composition control, and experimental validation. The HPA progenitor and germ-cell pattern makes a shared proliferative or developmental cell state an important alternative explanation.

**Hypothesis.** Hypothesis: the module reflects a conserved nuclear program in proliferating or progenitor-like cells that couples MCM-dependent replication-fork licensing and unwinding with DNA-repair capacity, nuclear import, and replication-associated chromatin assembly. In this model, the tightly connected MCM proteins form the functional replication core, KPNA2 may support nuclear delivery of replication or repair factors, and NASP may coordinate histone handling during replication-coupled chromatin assembly. The hypothesis predicts that module activity will track cell-cycle state and proliferative cell abundance in brain and ovary samples, and that its apparent cross-tissue conservation will diminish after rigorous adjustment for cell composition. The roles of KPNA2 and NASP within this particular module remain hypotheses rather than demonstrated direct interactions.

### Important genes

#### MCM4

- **Related proteins** (co-abundance neighbors): MCM6 (0.92), MCM7 (0.91), MCM2 (0.90), NASP (0.89), KPNA2 (0.89), MCM5 (0.85); STRING partners: MCM2 (0.999), MCM5 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 4. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication rel…
- **Diseases (Open Targets)**: primary immunodeficiency with natural-killer cell deficiency and adrenal insufficiency (0.714); X-linked adrenal hypoplasia congenita (0.185); lung adenocarcinoma (0.112); microcephaly (0.111); neoplasm (0.102)
- **Europe PMC papers**: 4082
- **Why important**: MCM4 is the strongest network hub in the module, connecting every other module gene, including the dense MCM core, KPNA2, and NASP. It participates in essentially the full set of globally significant replication, helicase, repair, and chromosome annotations (GO:CC MCM complex; q_global = 1.58e-09) through (GO:MF ribonucleoside triphosphate phosphatase activity; q_global = 0.0493). STRING and hu.MAP place it repeatedly in the MCM and CMG-related machinery (STRING Component MCM complex; within-query FDR = 3.46e-09) through (STRING Process DNA unwinding involved in DNA replication; within-query FDR = 1.26e-07), (hu.MAP huMAP3_05529.1) through (hu.MAP huMAP3_08848.1). Its established role in the MCM helicase and replication-initiation machinery is supported by extensive annotation and a substantial literature base. Disease associations include immunodeficiency with natural-killer-cell deficiency and adrenal insufficiency, adrenal hypoplasia, microcephaly, and neoplastic disease.
- **Conclusion**: Established conclusion: MCM4 is a central, highly supported component of the module and is the best representative of its replication-core function. Hypothesis: variation in MCM4 abundance may be a particularly sensitive marker of the shared proliferative or replication-competent cell state, but the co-abundance data do not establish that MCM4 drives the tissue-level pattern.

#### MCM2

- **Related proteins** (co-abundance neighbors): MCM6 (0.90), MCM4 (0.90), MCM7 (0.90), KPNA2 (0.85), MCM5 (0.84); STRING partners: MCM4 (0.999), MCM5 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_10747.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a highly connected member of the MCM core and links to KPNA2 in the module. It appears across the globally significant MCM, CMG, DNA-replication, DNA-repair, homologous-recombination, and cell-cycle terms (GO:CC MCM complex; q_global = 1.58e-09) through (GO:MF ribonucleoside triphosphate phosphatase activity; q_global = 0.0493). It is supported by very strong STRING associations with the other MCM genes and by many hu.MAP complexes (STRING Component MCM complex; within-query FDR = 3.46e-09) through (STRING Process DNA unwinding involved in DNA replication; within-query FDR = 1.26e-07), (hu.MAP huMAP3_05529.1) through (hu.MAP huMAP3_07113.1), (hu.MAP huMAP3_09860.1) through (hu.MAP huMAP3_14306.1), (hu.MAP huMAP3_10747.1). It has the largest literature representation among the listed genes and established associations with hearing loss, developmental abnormalities, and other disease phenotypes.
- **Conclusion**: Established conclusion: MCM2 is a core replication-initiation and fork-associated component, not merely a passive marker of the module. Hypothesis: its co-abundance with KPNA2 could indicate coordinated nuclear availability of replication machinery, but this relationship is not demonstrated as a direct biochemical interaction here.

#### MCM7

- **Related proteins** (co-abundance neighbors): MCM6 (0.94), MCM5 (0.93), MCM4 (0.91), MCM2 (0.90); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM6 (0.999), NASP (0.81)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 is a strongly connected MCM-core member and is also the main bridge from that core to NASP in STRING. It contributes to the globally significant replication, helicase, DNA-repair, chromosome, and cell-cycle terms (GO:CC MCM complex; q_global = 1.58e-09) through (GO:BP double-strand break repair; q_global = 0.00111), (GO:MF macromolecular conformation isomerase activity; q_global = 0.00213) through (GO:MF ATP-dependent activity; q_global = 0.0321), (GO:MF ribonucleoside triphosphate phosphatase activity; q_global = 0.0493). It is present in numerous hu.MAP complexes involving the MCM and CMG machinery (hu.MAP huMAP3_05529.1) through (hu.MAP huMAP3_11119.1), (hu.MAP huMAP3_09238.1), and has extensive literature support. Its disease associations include Meier-Gorlin syndrome, spastic paraplegia, AP-four deficiency syndrome, microcephaly, and trichiasis.
- **Conclusion**: Established conclusion: MCM7 reinforces the interpretation that the module contains authentic replication-helicase machinery. Hypothesis: the MCM7-NASP relationship may connect fork progression with histone handling or replication-coupled chromatin assembly, but the network does not establish directionality or mechanism.

#### KPNA2

- **Related proteins** (co-abundance neighbors): MCM4 (0.89), MCM2 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: karyopherin subunit alpha 2. The import of proteins into the nucleus is a process that involves at least 2 steps. The first is an energy-independent docking of the protein to the nuclear envelope and the second is an energy-dependent translocation through the nuclear pore complex. Imported proteins require a nuclear localization sequence (NLS) which generally consists of a short region of basic amino acids or 2 such regions s…
- **Diseases (Open Targets)**: severe acute respiratory syndrome (0.462); Orthomyxoviridae infectious disease (0.462); dengue disease (0.462); COVID-19 (0.373); non-alcoholic fatty liver (0.324)
- **Europe PMC papers**: 2442
- **Why important**: KPNA2 is a peripheral module gene connected to MCM4 and MCM2 but absent from the listed STRING interactions and hu.MAP complexes. Its established function is importin-alpha-mediated nuclear import of proteins carrying nuclear localization signals. It contributes to globally corrected terms involving DNA recombination and DNA metabolism (GO:BP DNA recombination; q_global = 2.52e-05), (GO:BP DNA metabolic process; q_global = 0.000166), (GO:BP regulation of DNA metabolic process; q_global = 0.000192), and its HPA profile includes germ-cell and oocyte-associated cell types. It also has a substantial literature base and disease or infection associations involving viral nuclear entry and metabolic disease.
- **Conclusion**: Established conclusion: KPNA2 provides a plausible nuclear-transport context for the replication-associated core, but its direct membership in a replication complex is not established by the supplied interaction resources. Hypothesis: KPNA2 may coordinate nuclear import of replication or repair factors in the shared cell state; this should be tested experimentally rather than inferred from co-abundance alone.

#### NASP

- **Related proteins** (co-abundance neighbors): MCM4 (0.89); STRING partners: MCM6 (0.709), MCM7 (0.81)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain, ovary
- **hu.MAP 3.0**: huMAP3_10747.1
- **Function (MyGene.info)**: nuclear autoantigenic sperm protein. This gene encodes a H1 histone binding protein that is involved in transporting histones into the nucleus of dividing cells. Multiple isoforms are encoded by transcript variants of this gene. The somatic form is expressed in all mitotic cells, is localized to the nucleus, and is coupled to the cell cycle. The testicular form is expressed in embryonic tissues, tumor cells, and the testis. In male g…
- **Diseases (Open Targets)**: neurodegenerative disease (0.445); Paralytic ileus (0.301); glioma (0.080); central nervous system cancer (0.080); hepatocellular carcinoma (0.076)
- **Europe PMC papers**: 1349
- **Why important**: NASP is the most peripheral gene in the module, connected in the co-abundance graph to MCM4 and supported by STRING links to MCM6 and MCM7. It appears in globally corrected DNA-replication, DNA-metabolism, and chromosome terms (GO:BP DNA replication; q_global = 4.71e-05), (GO:BP DNA metabolic process; q_global = 0.000166), (GO:CC chromosome; q_global = 0.0301). MyGene.info describes its established role in H1 histone binding and histone transport into nuclei of dividing cells, with roles in nucleosome and replication-dependent chromatin assembly. hu.MAP places NASP with MCM2 in a histone and chromatin-related complex (hu.MAP huMAP3_10747.1). Its literature volume is smaller than that of the MCM genes, making it a useful connector but a less extensively characterized module anchor.
- **Conclusion**: Established conclusion: NASP supports a replication-coupled chromatin interpretation and is not simply an unrelated peripheral gene. Hypothesis: NASP may help explain why this module is conserved across tissues with proliferating or germ-cell-like populations, by coupling DNA synthesis to histone handling; the supplied data do not prove that it physically assembles with the MCM core in these tissues.
