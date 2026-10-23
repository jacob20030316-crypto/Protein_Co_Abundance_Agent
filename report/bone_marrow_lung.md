# Conserved co-abundance modules: bone_marrow and lung

## Module 0

**Tissue pair**: bone_marrow and lung  
**Genes (24)**: MPG, GOT2, ACO2, APEX1, CS, POLE, TUFM, ETFA, SHMT2, HSD17B10, IDH3A, LTN1, CHCHD3, IMMT, NDUFS1, NDUFS2, NSMCE3, PDIA5, PHB1, PHB2, PRDX3, RBM15B, SFXN1, SPINT1

### Function

The primary interpretation is a mitochondrial energy and structural-maintenance module. The strongest evidence is the globally significant enrichment for mitochondrion and mitochondrial matrix (GO:CC mitochondrion; q_global = 6.91e-05) (GO:CC mitochondrial matrix; q_global = 0.000124), mitochondrial organization (GO:BP mitochondrion organization; q_global = 0.00697), amino-acid biosynthesis and two-oxocarboxylic-acid metabolism (KEGG Biosynthesis of amino acids - Homo sapiens (human); q_global = 0.0118) (KEGG 2-Oxocarboxylic acid metabolism - Homo sapiens (human); q_global = 0.014), generation of precursor metabolites and energy (GO:BP generation of precursor metabolites and energy; q_global = 0.019), cellular respiration (GO:BP cellular respiration; q_global = 0.0266), tricarboxylic-acid metabolism (GO:BP tricarboxylic acid metabolic process; q_global = 0.0383), and mitochondrial inner-membrane or nucleoid compartments (5 globally significant GO/KEGG terms, q_global 0.0242–0.0439; see the table). The genes span complementary mitochondrial activities: tricarboxylic-acid-cycle enzymes ACO2, CS, and IDH3A; amino-acid and one-carbon metabolism through GOT2 and SHMT2; respiratory-chain components NDUFS1 and NDUFS2; fatty-acid electron transfer through ETFA; mitochondrial translation through TUFM; redox protection through PRDX3; and inner-membrane or cristae organization through PHB1, PHB2, IMMT, and CHCHD3. The module therefore appears to represent coordinated mitochondrial oxidative metabolism, biosynthetic precursor supply, respiratory-chain activity, redox control, and organelle architecture rather than a narrowly defined single pathway. The co-abundance network reinforces this interpretation: a connected metabolic core links GOT2, ACO2, CS, IDH3A, TUFM, and SHMT2, while respiratory and membrane-organization genes form additional linked components. The globally corrected GO and KEGG results are primary evidence; the STRING enrichments (15 supplementary STRING terms; within-query FDR 8.75e-09–0.0023) are concordant supplementary evidence.

**Cell composition.** This is not primarily a plasma or secreted-protein module and it is not strongly blood-cell specific. Most genes have low immune-cell specificity, while only a minority show immune-cell enhancement, including IDH3A in plasmacytoid dendritic cells, SFXN1 in basophils, and PDIA5 in plasmacytoid dendritic cells. HPA profiles instead point toward tissue-enhanced expression in metabolically active tissues such as skeletal muscle, heart muscle, liver, and tongue, with cell-type enhancement often involving hepatocytes or epithelial and progenitor populations. A small minority of genes have secretome annotations, most notably SPINT1 as secreted to blood; this does not explain the dominant module signal. Protein detection in both bone marrow and lung is common for many members, although several mitochondrial proteins are not detected in one of those tissues. The shared module is therefore more plausibly related to common mitochondrial demand or shared metabolically active cell populations than to a circulating-protein signal or a generic immune-cell signature. The bone-marrow association of POLE and progenitor-related HPA annotations may contribute a tissue-specific component, but the overall composition is broadly mitochondrial and metabolically oriented.

**GO/KEGG enrichment**: 14 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrion | 6.91e-05 | ACO2, APEX1, CHCHD3, CS, ETFA, GOT2, HSD17B10, IDH3A, IMMT, MPG, NDUFS1, NDUFS2, PHB1, PHB2, PRDX3, SFXN1, SHMT2, TUFM |
| GO:CC mitochondrial matrix | 0.000124 | ACO2, CS, ETFA, GOT2, HSD17B10, IDH3A, MPG, NDUFS1, NDUFS2, PRDX3, SHMT2, TUFM |
| GO:BP mitochondrion organization | 0.00697 | CHCHD3, HSD17B10, IMMT, NDUFS1, NDUFS2, PHB1, PHB2, PRDX3 |
| KEGG Biosynthesis of amino acids - Homo sapiens (human) | 0.0118 | ACO2, CS, GOT2, IDH3A, SHMT2 |
| KEGG 2-Oxocarboxylic acid metabolism - Homo sapiens (human) | 0.014 | ACO2, CS, GOT2, IDH3A |
| GO:BP generation of precursor metabolites and energy | 0.019 | ACO2, CS, ETFA, IDH3A, NDUFS1, NDUFS2, PDIA5, SHMT2 |
| GO:MF 4 iron, 4 sulfur cluster binding | 0.0242 | ACO2, NDUFS1, NDUFS2, POLE |
| GO:CC inner mitochondrial membrane protein complex | 0.0242 | CHCHD3, IMMT, PHB1, PHB2 |
| GO:BP cellular respiration | 0.0266 | ACO2, CS, ETFA, IDH3A, NDUFS1, NDUFS2, SHMT2 |
| GO:CC mitochondrial inner membrane | 0.0267 | CHCHD3, IMMT, NDUFS1, NDUFS2, PHB1, PHB2, SFXN1, SHMT2 |
| GO:BP tricarboxylic acid metabolic process | 0.0383 | ACO2, CS, IDH3A |
| GO:CC organelle inner membrane | 0.0406 | CHCHD3, IMMT, NDUFS1, NDUFS2, PHB1, PHB2, SFXN1, SHMT2 |
| GO:CC nucleoid | 0.0439 | HSD17B10, MPG, SHMT2, TUFM |
| GO:CC mitochondrial nucleoid | 0.0439 | HSD17B10, MPG, SHMT2, TUFM |

### STRING and hu.MAP

STRING supports many established relationships within the module. Strong links connect the tricarboxylic-acid-cycle enzymes ACO2, CS, GOT2, and IDH3A; NDUFS1 and NDUFS2 are linked as complex-I core subunits; IMMT is linked to CHCHD3 and to respiratory and prohibitin components; PHB1 and PHB2 form a particularly well-supported prohibitin relationship; and TUFM connects with NDUFS2, PHB1, PHB2, GOT2, and ETFA. APEX1 and MPG also have a known DNA-repair relationship. These links indicate that the network is not composed solely of previously unrelated proteins, but contains recognizable biochemical and structural subsystems. hu.MAP independently supports the PHB1-PHB2 complex (hu.MAP huMAP3_01706.1) and several larger complexes containing PHB1, PHB2, and CHCHD3 (hu.MAP huMAP3_10725.1) (hu.MAP huMAP3_09671.1) (hu.MAP huMAP3_11743.1). It also places NDUFS1 and NDUFS2 together in multiple complex-I-related assemblies (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1), and places SFXN1 with LTN1 in complexes (hu.MAP huMAP3_09691.1) (hu.MAP huMAP3_10473.1). Thus, STRING and hu.MAP validate several local relationships and the mitochondrial interpretation, while also showing that much of the module is a co-abundance neighborhood assembled from multiple known complexes rather than one complete physical complex.

**STRING interactions (score >= 0.7)**: 26 of 276 gene pairs: ACO2–CS (0.999); ACO2–GOT2 (0.753); ACO2–IDH3A (0.998); ACO2–NDUFS1 (0.865); ACO2–NDUFS2 (0.955); APEX1–MPG (0.892); CHCHD3–IMMT (0.999); CS–GOT2 (0.952); CS–IDH3A (0.925); CS–NDUFS1 (0.737); CS–NDUFS2 (0.772); ETFA–TUFM (0.734); GOT2–IDH3A (0.889); GOT2–NDUFS2 (0.802); GOT2–TUFM (0.849); IMMT–NDUFS1 (0.901); IMMT–NDUFS2 (0.735); IMMT–PHB1 (0.741); IMMT–PHB2 (0.751); NDUFS1–NDUFS2 (0.999); NDUFS1–PRDX3 (0.883); NDUFS2–PHB1 (0.705); NDUFS2–TUFM (0.97); PHB1–PHB2 (0.999); PHB1–TUFM (0.797); PHB2–TUFM (0.911)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Mitochondrion (FDR = 8.75e-09, 18 genes); COMPARTMENTS Mitochondrion (FDR = 8.6e-07, 17 genes); Component Mitochondrion (FDR = 2.62e-06, 18 genes); Component Mitochondrial matrix (FDR = 1.14e-05, 12 genes); Keyword Transit peptide (FDR = 1.77e-05, 12 genes); COMPARTMENTS Mitochondrial matrix (FDR = 2.21e-05, 11 genes); Keyword Mitochondrion inner membrane (FDR = 0.00017, 8 genes); Component Mitochondrial protein-containing complex (FDR = 0.0004, 8 genes); COMPARTMENTS Mitochondrial protein complex (FDR = 0.00084, 8 genes); COMPARTMENTS Mitochondrial inner membrane (FDR = 0.00086, 8 genes); Component Inner mitochondrial membrane protein complex (FDR = 0.0011, 6 genes); COMPARTMENTS Inner mitochondrial membrane protein complex (FDR = 0.0012, 6 genes); KEGG 2-Oxocarboxylic acid metabolism (FDR = 0.0012, 4 genes); KEGG Biosynthesis of amino acids (FDR = 0.0016, 5 genes); Keyword 4Fe-4S (FDR = 0.0023, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10725.1 (PHB1, PHB2, CHCHD3; 3/59); huMAP3_01706.1 (PHB1, PHB2; 2/2); huMAP3_09691.1 (LTN1, SFXN1; 2/9); huMAP3_09671.1 (PHB1, PHB2; 2/10); huMAP3_11743.1 (PHB1, PHB2; 2/10); huMAP3_10473.1 (LTN1, SFXN1; 2/24); huMAP3_14018.1 (NDUFS2, NDUFS1; 2/48); huMAP3_06397.1 (NDUFS2, NDUFS1; 2/49); huMAP3_09982.1 (NDUFS2, NDUFS1; 2/49); huMAP3_09567.1 (NDUFS2, NDUFS1; 2/52); huMAP3_14878.1 (NDUFS2, NDUFS1; 2/53)

### Novelty

The mitochondrial function itself is not a new biological discovery: the globally significant annotations, STRING relationships, and hu.MAP complexes largely recapitulate established mitochondrial metabolism, respiration, cristae organization, translation, and DNA-repair biology. The module may nevertheless represent a potentially new cross-tissue co-abundance pattern shared by bone marrow and lung, especially because the selected genes combine metabolic enzymes, respiratory-chain components, cristae machinery, translation, redox defense, and a bone-marrow-associated replication factor. That claim should remain cautious. The fact that some module edges lack STRING or hu.MAP support does not establish novelty, because database coverage, tissue context, abundance regulation, and complex incompleteness can all produce unsupported edges. The defensible conclusion is that the module is a new systems-level association candidate, not a newly discovered mitochondrial pathway or physical complex. Independent replication in additional cohorts, preservation testing, cell-composition adjustment, and experimental perturbation would be needed before calling the cross-tissue module a novel mechanism.

**Hypothesis.** Hypothesis: the shared bone-marrow-lung module reflects coordinated adaptation of metabolically active or progenitor-like cells to respiratory and biosynthetic demand. In this model, ACO2, CS, IDH3A, and GOT2 maintain tricarboxylic-acid and amino-acid flux; SHMT2 and SFXN1 support mitochondrial one-carbon and serine handling; ETFA and NDUFS1-NDUFS2 support electron transfer; PRDX3 limits mitochondrial oxidative damage; TUFM sustains mitochondrial translation; and PHB1, PHB2, IMMT, and CHCHD3 preserve inner-membrane and cristae organization. The observed co-abundance could therefore arise when cells simultaneously increase mitochondrial substrate processing, respiratory capacity, antioxidant protection, and organelle maintenance. POLE, MPG, APEX1, NSMCE3, and RBM15B may represent a linked nuclear replication, repair, or RNA-regulatory demand rather than core members of the mitochondrial mechanism. This is a hypothesis generated by the integrated network and annotation evidence, not a demonstrated causal chain.

### Important genes

#### GOT2

- **Related proteins** (co-abundance neighbors): IDH3A (0.88), TUFM (0.88), PHB2 (0.85), CS (0.85), SHMT2 (0.84), PRDX3 (0.80), APEX1 (0.80); STRING partners: ACO2 (0.753), CS (0.952), IDH3A (0.889), NDUFS2 (0.802), TUFM (0.849)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamic-oxaloacetic transaminase 2. Glutamic-oxaloacetic transaminase is a pyridoxal phosphate-dependent enzyme which exists in cytoplasmic and inner-membrane mitochondrial forms, GOT1 and GOT2, respectively. GOT plays a role in amino acid metabolism and the urea and tricarboxylic acid cycles. The two enzymes are homodimeric and show close homology. Two transcript variants encoding different isoforms have been found for this gene. […
- **Diseases (Open Targets)**: genetic developmental and epileptic encephalopathy (0.618); developmental and epileptic encephalopathy (0.393); Encephalopathy (0.370); neurodegenerative disease (0.356); lagophthalmos (0.298)
- **Europe PMC papers**: 2463
- **Why important**: GOT2 has the strongest network connectivity in the module and links the central metabolic neighborhood to TUFM, PHB2, CS, SHMT2, PRDX3, APEX1, and IDH3A. It is included in the mitochondrial, matrix, amino-acid, and two-oxocarboxylic-acid evidence (4 globally significant GO/KEGG terms, q_global 6.91e-05–0.014; see the table), and its annotation supports amino-acid metabolism and the urea and tricarboxylic-acid cycles. HPA indicates enrichment in metabolically active tissues and hepatocytes rather than immune-cell specificity. Its disease associations include developmental and epileptic encephalopathy and neurodegenerative disease, and it has substantial literature support.
- **Conclusion**: Established evidence supports GOT2 as a mitochondrial metabolic connector and a plausible anchor of the module. Hypothesis: variation in GOT2 abundance may couple amino-acid flux to respiratory and redox activity across the shared tissues. The network supports this coupling, but does not establish that GOT2 controls the module.

#### TUFM

- **Related proteins** (co-abundance neighbors): GOT2 (0.88), PHB2 (0.88), PRDX3 (0.85), ETFA (0.81), IDH3A (0.81), SHMT2 (0.80); STRING partners: ETFA (0.734), GOT2 (0.849), NDUFS2 (0.97), PHB1 (0.797), PHB2 (0.911)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Tu translation elongation factor, mitochondrial. This gene encodes a protein which participates in protein translation in mitochondria. Mutations in this gene have been associated with combined oxidative phosphorylation deficiency resulting in lactic acidosis and fatal encephalopathy. A pseudogene has been identified on chromosome 17. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 4 (0.769); neurodegenerative disease (0.502); COVID-19 (0.471); combined oxidative phosphorylation deficiency (0.370); ulcerative colitis (0.303)
- **Europe PMC papers**: 1391
- **Why important**: TUFM is among the most connected genes and links metabolic, respiratory, antioxidant, and prohibitin neighborhoods. It is included in the mitochondrial and mitochondrial-matrix evidence (GO:CC mitochondrion; q_global = 6.91e-05) (GO:CC mitochondrial matrix; q_global = 0.000124) and mitochondrial-nucleoid evidence (GO:CC nucleoid; q_global = 0.0439) (GO:CC mitochondrial nucleoid; q_global = 0.0439). Its established function is mitochondrial translation, and its disease associations include combined oxidative-phosphorylation deficiency and neurodegenerative disease. It is detected in both bone marrow and lung and has low immune-cell specificity, making it a strong candidate for a shared cellular mitochondrial program rather than a tissue-restricted marker.
- **Conclusion**: Established evidence supports TUFM as a mitochondrial translation factor embedded in a broader oxidative-metabolism network. Hypothesis: increased mitochondrial translation may be coordinated with respiratory-chain assembly and cristae maintenance in the shared module. The co-abundance pattern does not prove that TUFM is the upstream driver.

#### PHB2

- **Related proteins** (co-abundance neighbors): TUFM (0.88), GOT2 (0.85), PHB1 (0.82), POLE (0.81), HSD17B10 (0.81), SFXN1 (0.80); STRING partners: IMMT (0.751), PHB1 (0.999), TUFM (0.911)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: huMAP3_10725.1, huMAP3_01706.1, huMAP3_09671.1, huMAP3_11743.1
- **Function (MyGene.info)**: prohibitin 2. Enables several functions, including protein C-terminus binding activity; protein N-terminus binding activity; and protein dimerization activity. Involved in several processes, including defense response to virus; positive regulation of cell cycle phase transition; and regulation of transcription, DNA-templated. Located in several cellular components, including cell surface; mitochondrial membrane…
- **Diseases (Open Targets)**: breast cancer (0.101); breast carcinoma (0.101); neoplasm (0.100); non-small cell lung carcinoma (0.096); colorectal carcinoma (0.085)
- **Europe PMC papers**: 2714
- **Why important**: PHB2 is a highly connected structural and regulatory member of the module. It participates in mitochondrial organization, inner-membrane, and mitochondrial-complex evidence (5 globally significant GO/KEGG terms, q_global 6.91e-05–0.0406; see the table), has strong STRING links to PHB1, TUFM, and IMMT, and is present in multiple hu.MAP complexes (hu.MAP huMAP3_10725.1) (hu.MAP huMAP3_01706.1) (hu.MAP huMAP3_09671.1) (hu.MAP huMAP3_11743.1). HPA places it in mitochondria with detection in both tissues and low immune-cell specificity. Its functions include participation in the mitochondrial prohibitin complex, mitophagy, and regulation of transcription, with disease associations including cancer and other disorders.
- **Conclusion**: Established evidence supports PHB2 as a structural and organizational component that can connect mitochondrial architecture with cellular regulation. Hypothesis: PHB2 may help stabilize the co-abundance program by coordinating membrane organization, respiratory capacity, and mitochondrial quality control. The module alone cannot distinguish structural causation from coordinated response.

#### NDUFS1

- **Related proteins** (co-abundance neighbors): POLE (0.82); STRING partners: ACO2 (0.865), CS (0.737), IMMT (0.901), NDUFS2 (0.999), PRDX3 (0.883)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S1. The protein encoded by this gene belongs to the complex I 75 kDa subunit family. Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Thi…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 5 (0.810); mitochondrial complex I deficiency (0.647); type 2 diabetes mellitus (0.608); Parkinson disease (0.603); diabetes mellitus (0.580)
- **Europe PMC papers**: 2567
- **Why important**: NDUFS1 is a core complex-I subunit with a central role in NADH-to-ubiquinone electron transfer and oxidative phosphorylation. It appears across the globally significant mitochondrial, respiration, inner-membrane, and iron-sulfur evidence (8 globally significant GO/KEGG terms, q_global 6.91e-05–0.0406; see the table), has strong STRING relationships with NDUFS2, ACO2, IMMT, and PRDX3, and is included with NDUFS2 in several hu.MAP complex-I assemblies (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1). Its disease associations include nuclear complex-I deficiency, mitochondrial disease, Parkinson disease, and diabetes-related traits.
- **Conclusion**: Established evidence supports NDUFS1 as a direct respiratory-chain marker and one of the clearest functional anchors of the module. Hypothesis: coordinated NDUFS1 and NDUFS2 abundance may couple complex-I capacity to tricarboxylic-acid flux and antioxidant protection. The data support association with respiration, not a tissue-specific disease mechanism.

#### CHCHD3

- **Related proteins** (co-abundance neighbors): IMMT (0.80); STRING partners: IMMT (0.999)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: huMAP3_10725.1
- **Function (MyGene.info)**: coiled-coil-helix-coiled-coil-helix domain containing 3. The protein encoded by this gene is an inner mitochondrial membrane scaffold protein. Absence of the encoded protein affects the structural integrity of mitochondrial cristae and leads to reductions in ATP production, cell growth, and oxygen consumption. This protein is part of the mitochondrial contact site and cristae organizing system (MICOS). Several transcript variants encoding different isof…
- **Diseases (Open Targets)**: neurodegenerative disease (0.537); smoking initiation (0.414); intelligence (0.385); insomnia (0.362); mathematical ability (0.312)
- **Europe PMC papers**: 549
- **Why important**: CHCHD3 is a mitochondrial inner-membrane scaffold and MICOS component involved in cristae formation and membrane organization. It is included in mitochondrial-organization and inner-membrane evidence (5 globally significant GO/KEGG terms, q_global 6.91e-05–0.0406; see the table), has a very strong STRING relationship with IMMT, and occurs with PHB1 and PHB2 in hu.MAP (hu.MAP huMAP3_10725.1). HPA shows mitochondrial detection in both tissues, tissue enhancement in skeletal muscle and tongue, and low immune-cell specificity. Its disease and trait associations include neurodegenerative disease and smoking initiation, while its literature volume is more specialized than that of core metabolic enzymes.
- **Conclusion**: Established evidence supports CHCHD3 as the module's cristae and mitochondrial-architecture representative. Hypothesis: CHCHD3 may translate increased respiratory demand into coordinated remodeling or stabilization of inner-membrane structure. The co-abundance result does not demonstrate physical coupling beyond the relationships already supported by STRING and hu.MAP.

#### POLE

- **Related proteins** (co-abundance neighbors): NDUFS2 (0.86), NSMCE3 (0.83), NDUFS1 (0.82), PHB2 (0.81), MPG (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA polymerase epsilon, catalytic subunit. This gene encodes the catalytic subunit of DNA polymerase epsilon. The enzyme is involved in DNA repair and chromosomal DNA replication. Mutations in this gene have been associated with colorectal cancer 12 and facial dysmorphism, immunodeficiency, livedo, and short stature. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal cancer, susceptibility to, 12 (0.739); intrauterine growth retardation, metaphyseal dysplasia, adrenal hypoplasia congenita, genital anomalies, and immunodeficiency (0.735); facial dysmorphism-immunodeficiency-livedo-short stature syndrome (0.732); non-small cell lung carcinoma (0.668); B-cell chronic lymphocytic leukemia (0.660)
- **Europe PMC papers**: 71098
- **Why important**: POLE is a distinctive, relatively peripheral member that connects to NDUFS1, NDUFS2, NSMCE3, MPG, and PHB2 in the module network. It contributes to the iron-sulfur-binding evidence (GO:MF 4 iron, 4 sulfur cluster binding; q_global = 0.0242) and has HPA tissue enhancement in bone marrow with cell-type enhancement in erythrocyte and megakaryocyte progenitors. Its established function is catalytic DNA replication and repair, and it has extensive literature and disease associations involving colorectal cancer, immunodeficiency, chromosomal development, and lung cancer. Its placement differs from the dominant mitochondrial annotations and is therefore informative rather than redundant.
- **Conclusion**: Established evidence supports POLE as a bone-marrow-associated replication and DNA-repair factor, not as a canonical mitochondrial metabolism gene. Hypothesis: POLE may mark a proliferative progenitor component that co-varies with mitochondrial energy production and genome-maintenance demand in bone marrow and lung samples. This interpretation is tentative, and POLE could alternatively reflect cell-composition or an indirect network bridge.

## Module 1

**Tissue pair**: bone_marrow and lung  
**Genes (12)**: ATG16L1, BRCC3, CIAO1, CUSTOS, DDX46, EDC4, NSUN2, PTPN23, RB1, SNRNP40, U2SURP, TCERG1

### Function

The strongest functional interpretation is constitutive nuclear RNA processing, specifically spliceosome-associated pre-mRNA splicing. The primary evidence is the globally corrected KEGG Spliceosome term (KEGG Spliceosome - Homo sapiens (human); q_global = 0.0393), supported by the same STRING enrichment (STRING KEGG Spliceosome; within-query FDR = 0.0123). The genes DDX46, SNRNP40, TCERG1, and U2SURP form the annotated spliceosome-related subset. The remaining genes do not establish a single additional globally significant pathway, so autophagy, mRNA decapping, cell-cycle control, DNA repair, iron-sulfur assembly, and RNA modification should be viewed as gene-level annotations rather than module-level conclusions. The network is sparse but organized around ATG16L1, with the spliceosome-related genes connected mainly through ATG16L1 in the co-abundance graph and with additional known STRING links among DDX46, TCERG1, SNRNP40, and U2SURP. This pattern is consistent with a shared abundance program involving general RNA processing, while the biological meaning of the ATG16L1-centered integration remains unresolved.

**Cell composition.** The module does not resemble a plasma-protein or secreted-protein module: the HPA summary identifies only one secreted gene, and the protein-detection pattern is broadly compatible with intracellular proteins. All genes have low tissue specificity, with no recurrent enriched tissue. Most genes also have low immune-cell specificity, and the HPA summary does not show a recurrent enriched blood-cell population. Therefore, the shared bone-marrow and lung signal is more consistent with broadly expressed housekeeping-like cellular machinery or shared cell states than with a blood-cell-specific or secreted-protein program. Cell-type annotations are limited and heterogeneous, including isolated neural, epithelial, cardiac, melanocytic, and spermatocyte associations, so they do not provide a coherent tissue or cell-type explanation.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Spliceosome - Homo sapiens (human) | 0.0393 | DDX46, SNRNP40, TCERG1, U2SURP |

### STRING and hu.MAP

STRING supports four high-confidence relationships: DDX46 with TCERG1, DDX46 with U2SURP, SNRNP40 with TCERG1, and TCERG1 with U2SURP. These links independently reinforce the spliceosome interpretation, but they account for only part of the co-abundance graph. hu.MAP identifies a complex containing DDX46 and SNRNP40 (hu.MAP huMAP3_08980.1), alongside many additional spliceosomal and snRNP-associated proteins that are not members of this module. Thus, the module overlaps known RNA-splicing machinery rather than defining an entirely unrecognized complex. ATG16L1 has the highest network connectivity in the module, yet it has no listed STRING partner or hu.MAP overlap here; its connection to the spliceosome-associated genes is therefore a co-abundance observation, not established physical interaction evidence.

**STRING interactions (score >= 0.7)**: 4 of 66 gene pairs: DDX46–TCERG1 (0.927); DDX46–U2SURP (0.918); SNRNP40–TCERG1 (0.973); TCERG1–U2SURP (0.741)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Spliceosome (FDR = 0.0123, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (DDX46, SNRNP40; 2/97)

### Novelty

This is not best described as a newly discovered spliceosome mechanism, because the central annotated genes participate in known spliceosome-related relationships and a known hu.MAP complex (hu.MAP huMAP3_08980.1). The potentially novel aspect is the cross-tissue co-abundance configuration: an ATG16L1-centered module combines a spliceosome-associated subset with genes involved in autophagy, RNA decay, cell-cycle regulation, DNA repair, iron-sulfur assembly, and RNA modification. However, absence of several module genes from STRING or hu.MAP does not prove novelty. The defensible conclusion is that the module may represent a novel tissue-pair co-abundance pattern, while its molecular interactions and mechanistic interpretation remain only partly established.

**Hypothesis.** Hypothesis: in both bone marrow and lung, a broadly expressed intracellular program couples basal spliceosome activity with cellular quality-control and stress-responsive processes. ATG16L1 may act as a co-abundance hub reflecting coordination between autophagy-related state and nuclear RNA-processing capacity, while the DDX46, SNRNP40, TCERG1, and U2SURP subset represents the more specifically interpretable spliceosome component. This hypothesis is based on co-abundance topology and annotations, not on demonstrated physical interaction between ATG16L1 and the spliceosome proteins. It should be tested with independent cohorts, cell-composition adjustment, perturbation experiments, and direct protein or RNA interaction assays.

### Important genes

#### ATG16L1

- **Related proteins** (co-abundance neighbors): TCERG1 (0.90), SNRNP40 (0.89), CUSTOS (0.87), DDX46 (0.87), EDC4 (0.86), RB1 (0.85), PTPN23 (0.82), NSUN2 (0.81), BRCC3 (0.81), CIAO1 (0.81), U2SURP (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: autophagy related 16 like 1. The protein encoded by this gene is part of a large protein complex that is necessary for autophagy, the major process by which intracellular components are targeted to lysosomes for degradation. Defects in this gene are a cause of susceptibility to inflammatory bowel disease type 10 (IBD10). Several transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.496); inflammatory bowel disease (0.463); Crohn disease (0.449); type 2 diabetes mellitus (0.329); psoriasis (0.305)
- **Europe PMC papers**: 7605
- **Why important**: ATG16L1 is the central co-abundance hub, connected to every other module member in the supplied graph and having the greatest weighted network strength. Its established annotation places it in autophagosome assembly and autophagy, and it has a strong inflammatory-bowel-disease association in the supplied disease evidence. It is broadly detected in both tissues, has low tissue and immune-cell specificity, and lacks STRING or hu.MAP support within this module.
- **Conclusion**: Established evidence supports ATG16L1 as the network anchor and an autophagy-related gene with inflammatory disease relevance. It is not established that ATG16L1 physically connects the spliceosome subset or that it drives the shared tissue module. Its hub status makes it the leading candidate for a coordinating or state-marker role, but that role remains a hypothesis.

#### TCERG1

- **Related proteins** (co-abundance neighbors): ATG16L1 (0.90); STRING partners: DDX46 (0.927), SNRNP40 (0.973), U2SURP (0.741)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transcription elongation regulator 1. This gene encodes a nuclear protein that regulates transcriptional elongation and pre-mRNA splicing. The encoded protein interacts with the hyperphosphorylated C-terminal domain of RNA polymerase II via multiple FF domains, and with the pre-mRNA splicing factor SF1 via a WW domain. Alternative splicing results in multiple transcripts variants encoding different isoforms. [provided by RefSeq, Jul 2…
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); colorectal cancer (0.336); smoking initiation (0.302); sleep apnea syndrome (0.293); chronic venous hypertension (0.257)
- **Europe PMC papers**: 505
- **Why important**: TCERG1 is one of the four genes in the globally significant Spliceosome term (KEGG Spliceosome - Homo sapiens (human); q_global = 0.0393) and has the densest STRING connectivity among the annotated spliceosome subset, linking to DDX46, SNRNP40, and U2SURP. Its established function includes transcriptional elongation regulation and pre-mRNA splicing. It is detected in both tissues and has low tissue, cell-type, and immune-cell specificity.
- **Conclusion**: Established evidence supports TCERG1 as a transcription and splicing regulator that provides a plausible bridge within the known RNA-processing component. Its connection to ATG16L1 in the co-abundance graph does not establish a direct molecular bridge. The proposed integration with autophagy is therefore a hypothesis.

#### DDX46

- **Related proteins** (co-abundance neighbors): ATG16L1 (0.87); STRING partners: TCERG1 (0.927), U2SURP (0.918)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: DEAD-box helicase 46. This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribu…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); dengue disease (0.370); Hypercholesterolemia (0.203); lung adenocarcinoma (0.074); osteosarcoma (0.053)
- **Europe PMC papers**: 592
- **Why important**: DDX46 is included in the primary Spliceosome term (KEGG Spliceosome - Homo sapiens (human); q_global = 0.0393), has high-confidence STRING links to TCERG1 and U2SURP, and overlaps the hu.MAP complex with SNRNP40 (hu.MAP huMAP3_08980.1). Its established molecular annotation as a DEAD-box helicase is consistent with RNA structural remodeling, prespliceosome assembly, and spliceosomal mRNA splicing. It is detected in both tissues and is broadly expressed by the supplied HPA summary.
- **Conclusion**: Established evidence makes DDX46 a strong marker of the module's spliceosome-related component and a plausible molecularly informative representative. Its co-abundance connection to ATG16L1 is not supported as a physical interaction by the supplied databases. Any role in coupling splicing to autophagy or tissue-specific physiology remains unproven.

#### SNRNP40

- **Related proteins** (co-abundance neighbors): ATG16L1 (0.89); STRING partners: TCERG1 (0.973)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 40. This gene encodes a component of the U5 small nuclear ribonucleoprotein (snRNP) particle. The U5 snRNP is part of the spliceosome, a multiprotein complex that catalyzes the removal of introns from pre-messenger RNAs. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.530); dengue disease (0.377); X-linked lymphoproliferative syndrome (0.058); autoimmune lymphoproliferative syndrome (0.055); Familial hemophagocytic lymphohistiocytosis (0.053)
- **Europe PMC papers**: 235
- **Why important**: SNRNP40 is included in the primary Spliceosome term (KEGG Spliceosome - Homo sapiens (human); q_global = 0.0393), is linked to TCERG1 in STRING, and is one of the two module members in the hu.MAP complex (hu.MAP huMAP3_08980.1). Its established function as a U5 small nuclear ribonucleoprotein component directly supports spliceosomal assembly and pre-mRNA splicing. HPA places it in nuclear speckles and detects it in both tissues.
- **Conclusion**: Established evidence identifies SNRNP40 as a core spliceosome-related member and strengthens the interpretation that the module contains bona fide RNA-processing machinery. The graph does not show SNRNP40 as a broad topological hub, and no evidence here demonstrates that it mediates the cross-tissue module. Its proposed coordinating role is therefore limited to the spliceosome component.

#### U2SURP

- **Related proteins** (co-abundance neighbors): ATG16L1 (0.80); STRING partners: DDX46 (0.918), TCERG1 (0.741)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: U2 snRNP associated SURP domain containing. Enables RNA binding activity. Predicted to be involved in RNA processing. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dengue disease (0.370); arthropathy (0.277); neurodegenerative disease (0.264); alcohol drinking (0.244); Hypercholesterolemia (0.207)
- **Europe PMC papers**: 228
- **Why important**: U2SURP is included in the primary Spliceosome term (KEGG Spliceosome - Homo sapiens (human); q_global = 0.0393) and has STRING links to DDX46 and TCERG1. Its supplied annotation supports RNA binding and RNA processing, and its location in the nucleoplasm is compatible with the module's nuclear RNA-processing interpretation. It is detected in both tissues and has low tissue and cell-type specificity.
- **Conclusion**: Established evidence supports U2SURP as a relevant RNA-processing member that reinforces the spliceosome signal despite its more limited functional annotation and literature volume. Its relationship to ATG16L1 is a co-abundance association rather than an established physical interaction. Its contribution to the proposed cross-process mechanism remains hypothetical.

## Module 2

**Tissue pair**: bone_marrow and lung  
**Genes (5)**: A2M, APOC3, CFH, RBP4, GC

### Function

The strongest functional interpretation is coordinated vitamin transport, supported by the globally corrected GO molecular-function term (GO:MF vitamin transmembrane transporter activity; q_global = 0.0495), which links GC and RBP4 to vitamin transmembrane transporter activity. RBP4 carries retinol from liver stores to peripheral tissues, while GC transports vitamin D and its metabolites. The remaining genes provide biologically compatible extracellular context: APOC3 is involved in triglyceride-rich lipoprotein metabolism, A2M regulates proteases and inflammatory cytokines, and CFH regulates alternative-pathway complement activation. The STRING supplementary terms consistently identify secreted and plasma-associated proteins (15 supplementary STRING terms; within-query FDR 6.47e-06–0.00077), but these are supportive rather than globally corrected pathway evidence. Thus, the module is best viewed as a circulating liver-derived transport, lipid, protease-regulatory, and complement-associated protein program rather than a narrowly defined intracellular pathway.

**Cell composition.** This is a strongly secreted-plasma composition: every module gene is annotated as secreted to blood, and the STRING supplementary evidence repeatedly recovers secreted, signal-bearing, plasma, serum, and fluid-proteome associations (15 supplementary STRING terms; within-query FDR 6.47e-06–0.00077). HPA points primarily to liver enrichment, with hepatocyte enrichment across the module; A2M additionally shows lung tissue enhancement. The genes are generally not immune-cell proteins, although A2M and CFH show enhancement in particular immune-cell types. Protein detection is absent in bone marrow for the module genes and present for only a subset in lung. Therefore, the shared bone-marrow/lung co-abundance pattern may substantially reflect circulating plasma contamination, vascular or extracellular-fluid content, or shared exposure to liver-derived proteins, rather than local production by bone-marrow and lung cells.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF vitamin transmembrane transporter activity | 0.0495 | GC, RBP4 |

### STRING and hu.MAP

STRING identifies only the GC-RBP4 relationship among the tested gene pairs, providing a known connection between two vitamin-binding or vitamin-transport-associated proteins. No STRING relationship is reported for the other module pairs at the stated confidence threshold. hu.MAP provides repeated partial-complex support: GC, A2M, APOC3, and CFH co-occur in broad plasma, complement, protease, and lipoprotein-associated assemblies (hu.MAP huMAP3_15040.1) and (hu.MAP huMAP3_10678.1); APOC3 and RBP4 recur together in additional assemblies (hu.MAP huMAP3_00178.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1); and A2M and APOC3 recur in several others (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1). These complexes contain many proteins outside the module, so they support shared extracellular biochemical context and possible co-packaging or co-regulation, but they do not establish that all module proteins form one physical complex. The sparse direct STRING connectivity and broad hu.MAP membership favor a co-abundance or shared-compartment interpretation over a single stable molecular machine.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: GC–RBP4 (0.749)
**STRING functional enrichment (supplementary, within-query FDR)**: PMID (2017) Proteomic analysis of human follicular fluid associated with successful in vitro fertilization. (FDR = 6.47e-06, 5 genes); Keyword Secreted (FDR = 9.58e-05, 5 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 0.00023, 5 genes); PMID (2016) Diagnostic Potential of Novel Salivary Host Biomarkers as Candidates for the Immunological Diagnosis of Tuberculosis Disease and Monitoring of Tuberculosis Treatment Response. (FDR = 0.00023, 4 genes); PMID (2016) Identification of novel host biomarkers in plasma as candidates for the immunodiagnosis of tuberculosis disease and monitoring of tuberculosis treatment response. (FDR = 0.00023, 4 genes); PMID (2021) Changes in the Proteome Profile of People Achieving Remission of Type 2 Diabetes after Bariatric Surgery. (FDR = 0.00046, 4 genes); Keyword Signal (FDR = 0.00048, 5 genes); PMID (2013) Analysis of human blood plasma proteome from ten healthy volunteers from Indian population. (FDR = 0.0005, 4 genes); PMID (2020) Serum-Based Proteomics Profiling in Adult Patients with Cystic Fibrosis. (FDR = 0.00056, 4 genes); PMID (2020) The Constitutive Proteome of Human Aqueous Humor and Race Specific Alterations. (FDR = 0.00056, 4 genes); PMID (2018) Plasma proteomics reveals gestational age-specific responses to mechanical ventilation and identifies the mechanistic pathways that initiate preterm lung injury. (FDR = 0.00056, 4 genes); PMID (2009) The multiplex bead array approach to identifying serum biomarkers associated with breast cancer. (FDR = 0.00062, 4 genes); PMID (2023) Targeted MRM Quantification of Urinary Proteins in Chronic Kidney Disease Caused by Glomerulopathies. (FDR = 0.00069, 4 genes); PMID (2022) Serum Glycoprotein Markers in Nonalcoholic Steatohepatitis and Hepatocellular Carcinoma. (FDR = 0.00077, 4 genes); PMID (2020) Significant correlation between plasma proteome profile and pain intensity, sensitivity, and psychological distress in women with fibromyalgia. (FDR = 0.00077, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (A2M, APOC3, GC, CFH; 4/64); huMAP3_10678.1 (A2M, APOC3, GC, CFH; 4/71); huMAP3_00178.1 (APOC3, RBP4; 2/9); huMAP3_08796.1 (APOC3, RBP4; 2/15); huMAP3_09832.1 (APOC3, RBP4; 2/18); huMAP3_07541.1 (A2M, APOC3; 2/19); huMAP3_07701.1 (A2M, APOC3; 2/22); huMAP3_09273.1 (A2M, APOC3; 2/28); huMAP3_08395.1 (A2M, APOC3; 2/43); huMAP3_09531.1 (A2M, APOC3; 2/47); huMAP3_10101.1 (A2M, APOC3; 2/49)

### Novelty

The exact conserved co-abundance module may be a new systems-level observation, because the supplied evidence does not identify a previously described module with this precise membership and cross-tissue conservation. However, its component biology is not novel: circulating secretion, liver origin, vitamin transport, lipid transport, complement regulation, and protease inhibition are established properties of the genes. Existing GC-RBP4 connectivity and repeated hu.MAP associations also indicate that several relationships are already known. Consequently, the defensible novelty claim is limited to the module-level co-abundance pattern and its conservation between bone marrow and lung. The data do not establish a new biochemical interaction, a new complex, or a tissue-localized mechanism. The plasma-like composition means that shared blood or extracellular-fluid content is an important alternative explanation.

**Hypothesis.** Hypothesis: the module represents a coordinated circulating protein program in which liver-derived GC and RBP4 support vitamin transport, while APOC3 couples that transport environment to lipoprotein metabolism and A2M and CFH constrain protease and complement activity. In bone marrow and lung samples, this program may appear conserved because both tissues contain or exchange vascular and extracellular fluid, rather than because the same resident cells synthesize all five proteins. A testable prediction is that the module will track plasma or vascular-content markers and liver-derived protein abundance more strongly than local expression by bone-marrow or lung parenchymal cells. A further prediction is that perturbations affecting vitamin status, lipid handling, complement activation, or tissue vascular permeability will alter coordinated module abundance.

### Important genes

#### RBP4

- **Related proteins** (co-abundance neighbors): APOC3 (0.89), A2M (0.80); STRING partners: GC (0.749)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_00178.1, huMAP3_08796.1, huMAP3_09832.1
- **Function (MyGene.info)**: retinol binding protein 4. This protein belongs to the lipocalin family and is the specific carrier for retinol (vitamin A alcohol) in the blood. It delivers retinol from the liver stores to the peripheral tissues. In plasma, the RBP-retinol complex interacts with transthyretin which prevents its loss by filtration through the kidney glomeruli. A deficiency of vitamin A blocks secretion of the binding protein posttranslatio…
- **Diseases (Open Targets)**: progressive retinal dystrophy due to retinol transport defect (0.696); microphthalmia, isolated, with coloboma 10 (0.643); microphthalmia, isolated, with coloboma (0.506); microphthalmia (0.501); inherited retinal dystrophy (0.421)
- **Europe PMC papers**: 18196
- **Why important**: RBP4 has a central network position, connecting to APOC3 and A2M, and is one of the two genes in the globally corrected transporter-activity term (GO:MF vitamin transmembrane transporter activity; q_global = 0.0495). Its established role is transport of retinol from liver stores to peripheral tissues. It is secreted to blood, liver-enriched, hepatocyte-enriched, and extensively represented in the supplementary plasma and fluid-proteome associations (15 supplementary STRING terms; within-query FDR 6.47e-06–0.00077). Its disease annotations prominently involve retinol-transport defects and inherited retinal disease, and it has a substantial literature base.
- **Conclusion**: Established evidence supports RBP4 as a principal vitamin-transport component and a strong marker of the module's liver-derived circulating character. The hypothesis that its co-abundance with the other genes coordinates tissue delivery of vitamins with lipid and innate-defense control remains unproven.

#### GC

- **Related proteins** (co-abundance neighbors): CFH (0.82), A2M (0.81); STRING partners: RBP4 (0.749)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: GC vitamin D binding protein. The protein encoded by this gene belongs to the albumin gene family. It is a multifunctional protein found in plasma, ascitic fluid, cerebrospinal fluid and on the surface of many cell types. It binds to vitamin D and its plasma metabolites and transports them to target tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq,…
- **Diseases (Open Targets)**: vitamin D deficiency (0.574); vitamin deficiency (0.552); chronic obstructive pulmonary disease (0.499); squamous cell carcinoma (0.339); central nervous system cancer (0.334)
- **Europe PMC papers**: 363974
- **Why important**: GC has a central network position, connecting to CFH and A2M, and is the other member of the globally corrected transporter-activity term (GO:MF vitamin transmembrane transporter activity; q_global = 0.0495). It binds and transports vitamin D and related metabolites and is annotated for vitamin transport and vitamin D metabolism. It is secreted to blood, liver-enriched, detected in lung by immunohistochemistry, and repeatedly recovered in supplementary secreted-plasma associations (5 supplementary STRING terms; within-query FDR 6.47e-06–0.00023), (STRING Keyword Signal; within-query FDR = 0.00048) (STRING PMID (2013) Analysis of human blood plasma proteome from ten healthy volunteers from Indian population.; within-query FDR = 0.0005) (STRING PMID (2020) Serum-Based Proteomics Profiling in Adult Patients with Cystic Fibrosis.; within-query FDR = 0.00056), (STRING PMID (2018) Plasma proteomics reveals gestational age-specific responses to mechanical ventilation and identifies the mechanistic pathways that initiate preterm lung injury.; within-query FDR = 0.00056) (STRING PMID (2009) The multiplex bead array approach to identifying serum biomarkers associated with breast cancer.; within-query FDR = 0.00062) (STRING PMID (2023) Targeted MRM Quantification of Urinary Proteins in Chronic Kidney Disease Caused by Glomerulopathies.; within-query FDR = 0.00069), and (STRING PMID (2020) Significant correlation between plasma proteome profile and pain intensity, sensitivity, and psychological distress in women with fibromyalgia.; within-query FDR = 0.00077). Its disease associations include vitamin deficiency and chronic obstructive pulmonary disease, and it has a very large literature base.
- **Conclusion**: Established evidence supports GC as the clearest functional anchor for vitamin transport and as the only module protein with a reported STRING connection to RBP4. The possibility that GC helps organize the broader module through shared extracellular transport or inflammatory context is a hypothesis, not a demonstrated physical mechanism.

#### A2M

- **Related proteins** (co-abundance neighbors): GC (0.81), RBP4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_07541.1, huMAP3_07701.1, huMAP3_09273.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1
- **Function (MyGene.info)**: alpha-2-macroglobulin. The protein encoded by this gene is a protease inhibitor and cytokine transporter. It uses a bait-and-trap mechanism to inhibit a broad spectrum of proteases, including trypsin, thrombin and collagenase. It can also inhibit inflammatory cytokines, and it thus disrupts inflammatory cascades. Mutations in this gene are a cause of alpha-2-macroglobulin deficiency. This gene is implicated in Alzheimer…
- **Diseases (Open Targets)**: myopia (0.206); refractive error (0.151); primary angle-closure glaucoma (0.148); Abnormality of refraction (0.144); Aganglionic megacolon (0.118)
- **Europe PMC papers**: 5133
- **Why important**: A2M occupies a central position by connecting to GC and RBP4 and participates in many hu.MAP assemblies (hu.MAP huMAP3_15040.1), (hu.MAP huMAP3_10678.1), and (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1). Its established functions include broad protease inhibition, cytokine transport, disruption of inflammatory cascades, and negative regulation of complement activation. HPA shows lung tissue enhancement and secretion to blood, with enhancement in several stromal, vascular-associated, hepatic, and immune cell types. It is repeatedly present in the supplementary plasma and secreted-protein evidence (15 supplementary STRING terms; within-query FDR 6.47e-06–0.00077).
- **Conclusion**: Established evidence supports A2M as an extracellular regulatory component that could connect transport-associated proteins to protease, cytokine, and complement control. Its central co-abundance position does not demonstrate that A2M physically binds the vitamin carriers in this module.

#### APOC3

- **Related proteins** (co-abundance neighbors): RBP4 (0.89); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_00178.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07541.1, huMAP3_07701.1, huMAP3_09273.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1
- **Function (MyGene.info)**: apolipoprotein C3. This gene encodes a protein component of triglyceride (TG)-rich lipoproteins (TRLs) including very low density lipoproteins (VLDL), high density lipoproteins (HDL) and chylomicrons. The encoded protein plays a role in role in the metabolism of these TRLs through multiple modes. This protein has been shown to promote the secretion of VLDL1, inhibit lipoprotein lipase enzyme activity, and delay cata…
- **Diseases (Open Targets)**: apolipoprotein c-III deficiency (0.610); hypertriglyceridemia (0.598); coronary artery disorder (0.573); familial lipoprotein lipase deficiency (0.531); Hypercholesterolemia (0.523)
- **Europe PMC papers**: 5854
- **Why important**: APOC3 connects RBP4 and is represented in every listed hu.MAP complex (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_00178.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1), making it a recurring bridge between the module and broad plasma lipoprotein or complement-associated assemblies. It is a secreted, liver-enriched hepatocyte protein that regulates triglyceride-rich lipoprotein metabolism, including inhibition of lipoprotein lipase activity and delayed remnant clearance. It is repeatedly recovered in the supplementary plasma, serum, and secreted-protein associations (15 supplementary STRING terms; within-query FDR 6.47e-06–0.00077). Its disease associations include hypertriglyceridemia and coronary artery disease, with a substantial literature base.
- **Conclusion**: Established evidence supports APOC3 as the module's lipid-transport and lipoprotein-metabolism anchor. Its repeated hu.MAP occurrence suggests shared extracellular biochemical context, but not a single APOC3-containing complex specific to this module.

#### CFH

- **Related proteins** (co-abundance neighbors): GC (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: complement factor H. This gene is a member of the Regulator of Complement Activation (RCA) gene cluster and encodes a protein with twenty short consensus repeat (SCR) domains. This protein is secreted into the bloodstream and has an essential role in the regulation of complement activation, restricting this innate defense mechanism to microbial infections. Mutations in this gene have been associated with hemolytic-ure…
- **Diseases (Open Targets)**: complement factor H deficiency (0.769); age-related macular degeneration (0.750); atypical hemolytic-uremic syndrome (0.729); age related macular degeneration 4 (0.711); Doyne honeycomb retinal dystrophy (0.688)
- **Europe PMC papers**: 9287
- **Why important**: CFH connects GC and occurs with GC in hu.MAP assemblies (hu.MAP huMAP3_15040.1) and (hu.MAP huMAP3_10678.1). It is a secreted regulator of complement activation with liver enrichment, enhancement in hepatocytes and fibroblast-like populations, and immune-cell enhancement in a specific T-cell population. Its supplementary STRING associations repeatedly place it in secreted and plasma proteomic contexts (5 supplementary STRING terms; within-query FDR 6.47e-06–0.00023), (STRING Keyword Signal; within-query FDR = 0.00048), (STRING PMID (2020) Serum-Based Proteomics Profiling in Adult Patients with Cystic Fibrosis.; within-query FDR = 0.00056), and (STRING PMID (2020) The Constitutive Proteome of Human Aqueous Humor and Race Specific Alterations.; within-query FDR = 0.00056). Its disease associations include complement factor H deficiency, atypical hemolytic uremic syndrome, and age-related macular degeneration, supported by a substantial literature base.
- **Conclusion**: Established evidence supports CFH as the module's innate-immune and complement-regulatory component and as a plausible extracellular partner of GC. Whether CFH contributes causally to the conserved co-abundance pattern, rather than merely sharing plasma origin, remains a hypothesis.

## Module 3

**Tissue pair**: bone_marrow and lung  
**Genes (6)**: SLC1A5, ARHGEF12, DAGLB, PLXNB2, SPG21, ATP6V0A1

### Function

No GO or KEGG term passed global correction. The network nevertheless suggests a possible interface between membrane signaling, cell adhesion and migration, Rho-dependent cytoskeletal remodeling, intracellular acidification, lipid signaling, and amino-acid transport. PLXNB2 and ARHGEF12 support receptor-linked cytoskeletal signaling; ATP6V0A1 supports endosomal and lysosomal acidification; DAGLB supports arachidonate and eicosanoid metabolism; SLC1A5 supports neutral amino-acid and glutamine transport; and SPG21 is associated with receptor and antigen-receptor signaling. This is an integrated biological interpretation, not a claim of significantly enriched pathway activity.

**Cell composition.** No member is annotated as secreted, so this is not a plasma or secreted-protein module. Most members have low tissue specificity, while one is tissue enhanced in brain. All members show cell-type enhancement, but the indicated cell types are heterogeneous and include alveolar, myeloid, neural, epithelial, placental, renal and other populations. Immune-related HPA patterns include plasmacytoid dendritic cells, monocytes, myeloid dendritic cells and neutrophils. Protein detection is stronger in lung than bone marrow, although several proteins are detected in both tissues. The conserved module may therefore reflect shared cell types, particularly myeloid or other immune-associated populations, or broadly expressed cellular machinery rather than a tissue-specific pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports one high-confidence relationship, between PLXNB2 and ARHGEF12. The other co-abundance links lack supplied STRING support at the stated threshold. No hu.MAP complex contains multiple module members. The PLXNB2–ARHGEF12 relationship is consistent with plexin-associated signaling and Rho regulation, but the sparse external interaction support means the module should not be treated as an established physical complex. It may instead combine directly related signaling proteins with co-regulated trafficking, metabolic or cell-composition signals.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: ARHGEF12–PLXNB2 (0.994)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The specific conserved co-abundance configuration across bone marrow and lung may be a potentially novel systems-level observation, but it is not established as a new biological discovery. The constituent proteins are individually well characterized, and the PLXNB2–ARHGEF12 relationship is already represented in STRING. The absence of a hu.MAP complex and the limited STRING support do not prove novelty. Independent replication, adjustment for cell composition, and experimental testing would be needed to establish whether the cross-tissue pattern is a genuinely new mechanism.

**Hypothesis.** Hypothesis: the module marks a shared membrane-trafficking and signaling state present in selected bone-marrow and lung cell populations. PLXNB2 may provide an extracellular cue and cell-adhesion or migration interface, with ARHGEF12 coupling that cue to Rho-dependent cytoskeletal remodeling. DAGLB may connect signaling to arachidonate-derived lipid mediators, while SLC1A5 supplies neutral amino-acid and glutamine transport. ATP6V0A1 may support endosomal or lysosomal acidification needed for receptor trafficking and intracellular processing, and SPG21 may modulate immune-receptor-related signaling. A cell-composition explanation, especially involving myeloid or other shared cell types, is an alternative hypothesis.

### Important genes

#### PLXNB2

- **Related proteins** (co-abundance neighbors): ATP6V0A1 (0.85), DAGLB (0.84), ARHGEF12 (0.84); STRING partners: ARHGEF12 (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location None; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plexin B2. Members of the B class of plexins, such as PLXNB2 are transmembrane receptors that participate in axon guidance and cell migration in response to semaphorins (Perrot et al. (2002) [PubMed 12183458]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Intellectual disability (0.519); amelogenesis imperfecta (0.518); sensorineural hearing loss disorder (0.516); cutaneous melanoma (0.486); neurodegenerative disease (0.455)
- **Europe PMC papers**: 2109
- **Why important**: PLXNB2 is the central network hub and has the strongest supplied network position. It is the sole member with the high-confidence STRING relationship to ARHGEF12. Its receptor role links semaphorin-responsive migration, cell adhesion, endocytosis and signaling. HPA supports presence in both tissues and enrichment in monocyte, dendritic-cell and alveolar-cell contexts. Its extensive literature and disease-association coverage make it the best anchor for interpreting the module.
- **Conclusion**: Established evidence supports PLXNB2 as a membrane receptor involved in migration, adhesion and signaling, with a central position in this co-abundance network. It is plausible, but not established, that PLXNB2 organizes the proposed shared signaling state.

#### DAGLB

- **Related proteins** (co-abundance neighbors): PLXNB2 (0.84), SPG21 (0.84), SLC1A5 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: diacylglycerol lipase beta. Enables lipase activity. Involved in arachidonic acid metabolic process. Located in nucleoplasm and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: osteogenesis imperfecta, type 21 (0.493); ulcerative colitis (0.324); coronary artery disorder (0.292); osteogenesis imperfecta type 3 (0.266); cholelithiasis (0.241)
- **Europe PMC papers**: 421
- **Why important**: DAGLB is a highly connected node linking PLXNB2 to SPG21 and SLC1A5. Its annotation directly connects it to arachidonate, eicosanoid and broader lipid metabolism, providing a plausible biochemical link between membrane signaling and inflammatory or metabolic responses. HPA places it in heterogeneous cell-type contexts, including microglia and neutrophil progenitors, while its literature and disease associations support biological relevance.
- **Conclusion**: Established evidence supports DAGLB as a lipid-metabolism enzyme associated with arachidonate and eicosanoid biology. Its role as the metabolic arm of this conserved module is a hypothesis, not a demonstrated causal function.

#### ARHGEF12

- **Related proteins** (co-abundance neighbors): PLXNB2 (0.84); STRING partners: PLXNB2 (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho guanine nucleotide exchange factor 12. Rho GTPases play a fundamental role in numerous cellular processes that are initiated by extracellular stimuli working through G protein-coupled receptors. The encoded protein may form a complex with G proteins and stimulate Rho-dependent signals. This protein has been observed to form a myeloid/lymphoid fusion partner in acute myeloid leukemia. Three transcript variants encoding different isoform…
- **Diseases (Open Targets)**: glaucoma (0.524); open-angle glaucoma (0.511); lymphoid neoplasm (0.370); lung carcinoma (0.370); Chordoid Meningioma (0.370)
- **Europe PMC papers**: 923
- **Why important**: ARHGEF12 is directly connected to PLXNB2 and has the clearest supplied link to Rho activation and actin organization. The STRING relationship with PLXNB2 is high confidence, and the protein is annotated at the plasma membrane and cytosol. Its reported myeloid or lymphoid fusion history and disease associations make it relevant to signaling and hematologic biology.
- **Conclusion**: Established evidence supports ARHGEF12 as a Rho-regulatory signaling factor and supports its known association with PLXNB2. It may mediate cytoskeletal consequences of plexin signaling in this module, but that mechanism has not been established here.

#### ATP6V0A1

- **Related proteins** (co-abundance neighbors): PLXNB2 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase H+ transporting V0 subunit a1. This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 d…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy 104 (0.712); neurodevelopmental disorder with epilepsy and brain atrophy (0.696); Seizure (0.420); hereditary disease (0.414); developmental disability (0.370)
- **Europe PMC papers**: 854
- **Why important**: ATP6V0A1 is tissue enhanced in brain and is annotated as a V-ATPase subunit involved in organelle, lysosomal and endosomal acidification, receptor endocytosis and autophagy-related processes. Its direct network link to PLXNB2 connects intracellular compartment function to the module hub. It has substantial literature and strong disease associations involving neurodevelopment and epilepsy, while HPA detects protein in lung but not bone marrow.
- **Conclusion**: Established evidence supports ATP6V0A1 as an acidification component of intracellular organelles. Its inclusion may reflect vesicle and receptor-trafficking biology or cell-type composition; a specific role in the shared bone-marrow–lung mechanism remains unproven.

#### SLC1A5

- **Related proteins** (co-abundance neighbors): DAGLB (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 1 member 5. The SLC1A5 gene encodes a sodium-dependent neutral amino acid transporter that can act as a receptor for RD114/type D retrovirus (Larriba et al., 2001 [PubMed 11781704]).[supplied by OMIM, Jan 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.463); substance abuse (0.231); attention deficit-hyperactivity disorder (0.231); autoimmune disorder of central nervous system (0.213); hypotensive disorder (0.188)
- **Europe PMC papers**: 5038
- **Why important**: SLC1A5 is connected to DAGLB and encodes a plasma-membrane neutral amino-acid transporter with emphasis on glutamine transport. It is detected in both tissues and shows cell-type enhancement in epithelial and placental contexts, as well as immune enhancement in plasmacytoid dendritic cells. Its extensive literature and disease associations make it a useful marker of nutrient handling and cellular state, although its network position is peripheral.
- **Conclusion**: Established evidence supports SLC1A5 as a neutral amino-acid and glutamine transporter. Its co-abundance with DAGLB may reflect coordinated metabolic demand, signaling or shared cell composition, but causality and pathway membership are hypotheses.

#### SPG21

- **Related proteins** (co-abundance neighbors): DAGLB (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SPG21 abhydrolase domain containing, maspardin. The protein encoded by this gene binds to the hydrophobic C-terminal amino acids of CD4 which are involved in repression of T cell activation. The interaction with CD4 is mediated by the noncatalytic alpha/beta hydrolase fold domain of this protein. It is thus proposed that this gene product modulates the stimulatory activity of CD4. Mutations in this gene are associated with autosomal recessive s…
- **Diseases (Open Targets)**: mast syndrome (0.746); hereditary sensory and autonomic neuropathy with spastic paraplegia (0.503); hereditary spastic paraplegia (0.494); hereditary spastic paraplegia 5A (0.370); alcohol drinking (0.228)
- **Europe PMC papers**: 263
- **Why important**: SPG21 is connected to DAGLB and is annotated in receptor and antigen-receptor signaling. HPA detects it in both tissues and reports immune enhancement in neutrophils, while its disease associations include mast syndrome and hereditary spastic-paraplegia phenotypes. Although its literature volume is more limited than that of the other selected genes, its position may connect lipid-associated biology to immune signaling.
- **Conclusion**: Established evidence supports SPG21 as a disease-associated protein linked to receptor signaling and immune-related biology. Its proposed bridge between DAGLB-associated lipid metabolism and immune-cell state is speculative and requires direct testing.

## Module 4

**Tissue pair**: bone_marrow and lung  
**Genes (13)**: ACIN1, ATXN2L, CHAF1B, EZH2, HEATR5B, PPIL1, ROCK1, SMARCC2, KARS1, TTC5, TXLNA, SNRNP200, EFTUD2

### Function

The strongest interpretation is a conserved nuclear RNA-processing module centered on pre-mRNA metabolism and spliceosome function. (GO:BP mRNA metabolic process; q_global = 0.0481) is the only GO/KEGG term that passed global correction and supports mRNA metabolic process involvement, with ACIN1, ATXN2L, EFTUD2, PPIL1, ROCK1, SNRNP200 and TTC5 contributing. The spliceosome interpretation is further supported, but only as supplementary evidence, by (STRING KEGG Spliceosome; within-query FDR = 0.0175), which includes ACIN1, EFTUD2, PPIL1 and SNRNP200. The module is structurally sparse and contains a prominent TTC5-centered co-abundance pattern together with an EFTUD2-SNRNP200-PPIL1 spliceosomal subnetwork. Other genes connect this RNA-processing signal to chromatin regulation, DNA replication-associated chromatin assembly, cytoskeletal signaling, translation and intracellular trafficking. Thus, the most defensible function is coordinated expression of RNA-processing machinery with linked nuclear regulation, rather than a narrowly tissue-specific pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only one secreted gene, and most proteins are intracellular, commonly nuclear or cytosolic. Most genes have low tissue specificity, and protein detection is broadly present in both bone marrow and lung, which is consistent with a broadly expressed cellular program rather than a tissue-exclusive program. The module is also not strongly blood-cell specific according to HPA, although several genes show cell-type enhancement in erythrocyte, neutrophil and megakaryocyte progenitors, while others are enhanced in respiratory ciliated or deuterosomal cells. EZH2 is tissue enhanced in bone marrow and lymphoid tissue and immune-cell enhanced in T-reg cells, whereas ROCK1 is enhanced in neutrophils and neutrophil progenitors. Consequently, part of the shared signal could reflect proliferative or progenitor-cell representation in the samples, but the broad tissue distribution and intracellular localization argue against interpreting the module simply as a blood-contamination or plasma-protein signature.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP mRNA metabolic process | 0.0481 | ACIN1, ATXN2L, EFTUD2, PPIL1, ROCK1, SNRNP200, TTC5 |

### STRING and hu.MAP

STRING provides a compact, biologically coherent core. EFTUD2 has high-confidence links to PPIL1 and SNRNP200 and a lower-confidence link to KARS1; PPIL1 and SNRNP200 are also strongly linked. These relationships are concordant with spliceosomal biology and with (STRING KEGG Spliceosome; within-query FDR = 0.0175). hu.MAP independently places SNRNP200, EFTUD2 and PPIL1 together in several spliceosome-related complexes, with recurring additional complexes containing established spliceosomal components such as PRPF8, PRPF6, SNRNP40, DDX23, AQR and CDC40. The repeated recovery of the same three module genes across multiple hu.MAP complexes is stronger evidence for a known molecular core than the sparse pairwise STRING graph alone. By contrast, TTC5 is the main co-abundance hub but has no listed STRING partners or hu.MAP complex membership, so its connection to the spliceosomal core is a module-level association rather than an established physical interaction. The same caution applies to most peripheral genes.

**STRING interactions (score >= 0.7)**: 4 of 78 gene pairs: EFTUD2–KARS1 (0.704); EFTUD2–PPIL1 (0.999); EFTUD2–SNRNP200 (0.999); PPIL1–SNRNP200 (0.959)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Spliceosome (FDR = 0.0175, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08501.1 (SNRNP200, EFTUD2, PPIL1; 3/47); huMAP3_09504.1 (SNRNP200, EFTUD2, PPIL1; 3/51); huMAP3_09945.1 (SNRNP200, EFTUD2, PPIL1; 3/61); huMAP3_00960.1 (SNRNP200, EFTUD2; 2/8); huMAP3_07622.1 (SNRNP200, EFTUD2; 2/9); huMAP3_06726.1 (SNRNP200, PPIL1; 2/37); huMAP3_08980.1 (SNRNP200, EFTUD2; 2/97)

### Novelty

The spliceosomal core itself is not a new molecular finding: the EFTUD2-SNRNP200-PPIL1 relationships are already represented by STRING and repeatedly supported by hu.MAP, and the relevant functions are established in the gene annotations and (STRING KEGG Spliceosome; within-query FDR = 0.0175). The conserved co-abundance pattern across bone marrow and lung may still be a useful systems-level observation, particularly because TTC5 links the known spliceosomal core to genes involved in chromatin, cell-cycle and cellular regulation. However, the fact sheet does not establish that this exact thirteen-gene module has not been reported previously, and absence of STRING or hu.MAP support for the peripheral connections cannot prove novelty. The appropriate conclusion is therefore partial novelty: a potentially informative shared tissue co-abundance configuration, but not a newly discovered spliceosomal complex or pathway.

**Hypothesis.** Hypothesis: the module represents a shared transcriptionally active and proliferative cell-state program in bone marrow and lung in which spliceosome assembly and RNA processing are coordinated with chromatin regulation and cellular remodeling. TTC5 may serve as a co-abundance hub linking the EFTUD2-SNRNP200-PPIL1 spliceosomal core to ACIN1, ROCK1, CHAF1B, ATXN2L, EZH2, SMARCC2, TXLNA and HEATR5B. In bone marrow, this program could be especially visible in progenitor populations, while in lung it could be contributed by respiratory ciliated-lineage cells or other broadly expressing nucleated cells. This is a mechanistic model rather than demonstrated physical connectivity; validation would require cell-resolved expression, perturbation of the spliceosomal core or TTC5, and testing whether RNA processing and chromatin-state changes occur together.

### Important genes

#### TTC5

- **Related proteins** (co-abundance neighbors): HEATR5B (0.92), PPIL1 (0.87), ROCK1 (0.86), CHAF1B (0.84), TXLNA (0.82), ATXN2L (0.82), ACIN1 (0.82), EZH2 (0.81), SMARCC2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tetratricopeptide repeat domain 5. Predicted to enable DNA binding activity and chromatin binding activity. Predicted to be involved in DNA repair. Predicted to act upstream of or within positive regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder with cerebral atrophy and variable facial dysmorphism (0.739); autosomal recessive non-syndromic intellectual disability (0.370); neurodevelopmental disorder (0.370); Neurodevelopmental delay (0.118); autosomal recessive spondylocostal dysostosis (0.075)
- **Europe PMC papers**: 767
- **Why important**: TTC5 is the strongest network hub and connects the greatest variety of module members, including the spliceosomal genes PPIL1 and ACIN1, chromatin regulators CHAF1B, EZH2 and SMARCC2, and signaling or trafficking genes such as ROCK1 and TXLNA. It is present in (GO:BP mRNA metabolic process; q_global = 0.0481), is broadly detected in bone marrow and lung, and has annotations involving DNA damage response, gene regulation and mRNA catabolism. Its large literature record and developmental-disorder associations make it biologically important, while its lack of listed STRING partners or hu.MAP membership makes the module connection potentially informative but not established as a physical interaction.
- **Conclusion**: Established evidence supports TTC5 as the co-abundance hub and as a gene linked to nuclear regulation and RNA metabolism. It is plausible, but unproven, that TTC5 coordinates the spliceosomal signal with chromatin or stress-response programs.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.89), KARS1 (0.81), ATXN2L (0.80); STRING partners: KARS1 (0.704), PPIL1 (0.999), SNRNP200 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_08980.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 is a central member of the known spliceosomal core. It is present in (GO:BP mRNA metabolic process; q_global = 0.0481) and (STRING KEGG Spliceosome; within-query FDR = 0.0175), has strong STRING links to PPIL1 and SNRNP200, and occurs across multiple hu.MAP complexes containing the same spliceosomal machinery. Its annotation directly supports spliceosomal snRNP assembly, spliceosome conformational change and mRNA splicing. Its established developmental disease association and substantial literature support make it an important mechanistic anchor.
- **Conclusion**: EFTUD2 is an established spliceosome component and provides strong biological validation for the module's RNA-processing interpretation. Its co-abundance with the other module genes is consistent with coordinated spliceosome activity, but does not by itself establish altered splicing in these tissues.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.89); STRING partners: EFTUD2 (0.999), PPIL1 (0.959)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_06726.1, huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is a U5 snRNP-specific RNA helicase and the most repeatedly represented module member in hu.MAP complexes. It is supported by (GO:BP mRNA metabolic process; q_global = 0.0481) and (STRING KEGG Spliceosome; within-query FDR = 0.0175), has strong STRING relationships with EFTUD2 and PPIL1, and is annotated for tri-snRNP assembly, spliceosome maturation and mRNA splicing. Its disease associations with retinal dystrophy and neurodegenerative conditions emphasize the importance of accurate RNA processing.
- **Conclusion**: SNRNP200 is an established core spliceosomal factor and one of the strongest biological indicators that the module contains a genuine RNA-processing program. The module does not demonstrate that SNRNP200 dysfunction causes the observed cross-tissue co-abundance pattern.

#### PPIL1

- **Related proteins** (co-abundance neighbors): TTC5 (0.87); STRING partners: EFTUD2 (0.999), SNRNP200 (0.959)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_06726.1
- **Function (MyGene.info)**: peptidylprolyl isomerase like 1. This gene is a member of the cyclophilin family of peptidylprolyl isomerases (PPIases). The cyclophilins are a highly conserved, ubiquitous family, members of which play an important role in protein folding, immunosuppression by cyclosporin A, and infection of HIV-1 virions. Based on similarity to other PPIases, this protein could accelerate the folding of proteins and might catalyze the cis-trans…
- **Diseases (Open Targets)**: pontocerebellar hypoplasia, type 14 (0.770); neurodegenerative disease (0.527); pontocerebellar hypoplasia (0.402); dengue disease (0.370); hypothyroidism (0.349)
- **Europe PMC papers**: 348
- **Why important**: PPIL1 completes the repeatedly observed EFTUD2-SNRNP200-PPIL1 core in STRING and hu.MAP. It is present in (GO:BP mRNA metabolic process; q_global = 0.0481) and (STRING KEGG Spliceosome; within-query FDR = 0.0175), and its annotations support spliceosomal mRNA splicing, peptidyl-prolyl isomerization and protein folding. Its cyclophilin-family function provides a plausible biochemical role in conformational control within RNA-processing machinery, while its disease associations show that it is not merely an uncharacterized network passenger.
- **Conclusion**: Established evidence supports PPIL1 as a spliceosome-associated factor within the module's known molecular core. A specific regulatory or catalytic role for PPIL1 in this tissue-shared co-abundance state remains a hypothesis.

#### EZH2

- **Related proteins** (co-abundance neighbors): TTC5 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: enhancer of zeste 2 polycomb repressive complex 2 subunit. This gene encodes a member of the Polycomb-group (PcG) family. PcG family members form multimeric protein complexes, which are involved in maintaining the transcriptional repressive state of genes over successive cell generations. This protein associates with the embryonic ectoderm development protein, the VAV1 oncoprotein, and the X-linked nuclear protein. This protein may play a role in the hema…
- **Diseases (Open Targets)**: Weaver syndrome (0.837); diffuse large B-cell lymphoma (0.615); neurodegenerative disease (0.525); follicular lymphoma (0.517); viral infectious disease (0.486)
- **Europe PMC papers**: 43112
- **Why important**: EZH2 connects the module to chromatin repression, chromatin organization and transcriptional regulation. It is tissue enhanced in bone marrow and lymphoid tissue, cell-type enhanced across several hematopoietic progenitor populations, and immune-cell enhanced in T-reg cells. It is detected in both tissues and has an extensive literature record together with strong associations to developmental and hematologic disease. Although it has no listed STRING or hu.MAP relationship within this module, its HPA pattern makes it relevant to the possibility that cell state or progenitor composition contributes to the shared signal.
- **Conclusion**: Established evidence supports EZH2 as a chromatin regulator with particular relevance to hematopoietic cell states. Its proposed coordination with the spliceosomal core is an inferred module-level relationship, not a demonstrated direct interaction.

#### ACIN1

- **Related proteins** (co-abundance neighbors): TTC5 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apoptotic chromatin condensation inducer 1. Apoptosis is defined by several morphologic nuclear changes, including chromatin condensation and nuclear fragmentation. This gene encodes a nuclear protein that induces apoptotic chromatin condensation after activation by caspase-3, without inducing DNA fragmentation. This protein has also been shown to be a component of a splicing-dependent multiprotein exon junction complex (EJC) that is deposi…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); adolescent idiopathic scoliosis (0.090); hepatocellular carcinoma (0.076); acute lymphoblastic leukemia (0.074); pancreatic neoplasm (0.045)
- **Europe PMC papers**: 894
- **Why important**: ACIN1 links RNA processing to apoptosis and differentiation. It is included in (GO:BP mRNA metabolic process; q_global = 0.0481) and (STRING KEGG Spliceosome; within-query FDR = 0.0175), is annotated as an exon-junction-complex-associated splicing factor, and has additional annotations involving erythrocyte differentiation, monocyte differentiation and apoptotic chromatin condensation. Its detection in both tissues and substantial literature support make it a useful interpretive bridge between the spliceosomal core and lineage or cell-state biology.
- **Conclusion**: Established evidence supports ACIN1 as an RNA-splicing-associated factor with roles in apoptotic and hematopoietic differentiation processes. The module does not establish whether its co-abundance reflects active apoptosis, differentiation, or shared regulation of RNA processing.

## Module 5

**Tissue pair**: bone_marrow and lung  
**Genes (6)**: ACSL4, GLUD1, GIMAP1, GIMAP4, TRIM21, TBXAS1

### Function

The module most plausibly represents a mixed immune-cell and cellular-metabolism program rather than a single, globally established pathway. Its strongest coherent signal is the presence of the IAN-family GTPases GIMAP1 and GIMAP4, supported by the supplementary STRING annotations for AIG1-type guanine-nucleotide-binding and GIMA/IAN/Toc GTPase domains (STRING InterPro AIG1-type guanine nucleotide-binding (G) domain; within-query FDR = 0.0371), (STRING InterPro GTPase GIMA/IAN/Toc; within-query FDR = 0.0371), (STRING NetworkNeighborAL GTPase GIMA/IAN/Toc; within-query FDR = 0.0403). The remaining genes connect this signal to thromboxane and lipid metabolism, mitochondrial amino-acid metabolism, and immune regulation. No GO or KEGG term passed global correction, so no GO/KEGG pathway can be presented as significantly enriched. The absence of a globally significant term does not invalidate the module; it indicates that the available module-level annotation evidence is limited and heterogeneous.

**Cell composition.** This is not a plasma or secreted-protein module: none of the genes is annotated as secreted. The HPA profile instead points toward immune and hematopoietic cell composition. Lymphoid tissue is the most recurrent enriched tissue, while neutrophils are the most recurrent enriched single-cell type; additional signals involve microglia, mast cells, Kupffer cells, macrophages, dendritic cells, monocytes, eosinophils, basophils, and hematopoietic stem cells. Most genes have low immune-cell specificity, with one blood-cell group-enriched gene, so the module may reflect shared immune or myeloid cell content in bone marrow and lung rather than a program uniquely active in both tissues. GLUD1 also has group-enriched tissue expression in kidney and liver, and ACSL4 and GLUD1 show broader cellular distribution, supporting a mixed cell-composition and housekeeping/metabolic interpretation. Protein detection is broader in lung than in bone marrow, although the genes detected in both tissues include several central immune-associated or metabolic components.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship within the module is the direct GIMAP1–GIMAP4 association (STRING InterPro AIG1-type guanine nucleotide-binding (G) domain; within-query FDR = 0.0371), (STRING InterPro GTPase GIMA/IAN/Toc; within-query FDR = 0.0371), (STRING NetworkNeighborAL GTPase GIMA/IAN/Toc; within-query FDR = 0.0403). This pair is therefore the clearest established internal molecular relationship and supports a shared IAN-family GTPase component. STRING functional annotations are supplementary and were not corrected across modules, so they should not be interpreted as globally significant enrichment. The other module edges connect genes with compatible biological themes, including GIMAP1 with TBXAS1 and GIMAP4 with ACSL4 and GLUD1, but the fact sheet does not provide high-confidence STRING support for those pairwise relationships. No hu.MAP complex contains multiple module members. Thus, the network appears to contain one known molecular pair embedded in a broader co-abundance neighborhood, rather than a validated multiprotein complex.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: GIMAP1–GIMAP4 (0.818)
**STRING functional enrichment (supplementary, within-query FDR)**: InterPro AIG1-type guanine nucleotide-binding (G) domain (FDR = 0.0371, 2 genes); InterPro GTPase GIMA/IAN/Toc (FDR = 0.0371, 2 genes); NetworkNeighborAL GTPase GIMA/IAN/Toc (FDR = 0.0403, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a new tissue-pair co-abundance observation, but it cannot be claimed as a newly discovered molecular pathway. The GIMAP1–GIMAP4 relationship and the IAN-family functional annotation are already represented in STRING, while the absence of a shared hu.MAP complex argues against an established complex-level interpretation. The combination of these genes across bone marrow and lung, especially the linkage of IAN-family GTPases with thromboxane synthesis, lipid handling, mitochondrial metabolism, and immune regulation, may be less well characterized. However, absence from hu.MAP or absence of additional STRING edges does not prove novelty. A defensible conclusion is that the tissue-pair co-abundance pattern may be novel, whereas its central GIMAP biology is not.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of immune-cell populations shared between bone marrow and lung, with GIMAP1 and GIMAP4 marking an IAN-family nucleotide-signaling component. This immune-associated state may co-vary with TBXAS1-dependent thromboxane and eicosanoid capacity, ACSL4-dependent long-chain fatty-acid handling, GLUD1-dependent mitochondrial amino-acid metabolism, and TRIM21-dependent ubiquitin and immune-regulatory activity. The pattern could therefore represent a cell-composition-linked immune-metabolic state rather than direct physical cooperation among all module proteins. This hypothesis requires testing with cell-resolved expression, perturbation, and independent tissue cohorts.

### Important genes

#### GIMAP4

- **Related proteins** (co-abundance neighbors): ACSL4 (0.90), GIMAP1 (0.85), GLUD1 (0.82); STRING partners: GIMAP1 (0.818)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GTPase, IMAP family member 4. This gene encodes a protein belonging to the GTP-binding superfamily and to the immuno-associated nucleotide (IAN) subfamily of nucleotide-binding proteins. The encoded protein of this gene may be negatively regulated by T-cell acute lymphocytic leukemia 1 (TAL1). In humans, the IAN subfamily genes are located in a cluster at 7q36.1. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: metabolic syndrome (0.120); lung adenocarcinoma (0.081); non-alcoholic fatty liver (0.064); Sepsis (0.044); ischemic stroke (0.044)
- **Europe PMC papers**: 495
- **Why important**: GIMAP4 is the most connected node in the module and links the established GIMAP1 relationship with ACSL4 and GLUD1. It is an IAN-family GTPase, has lymphoid-tissue enhancement, and is supported by all supplementary STRING functional annotations (STRING InterPro AIG1-type guanine nucleotide-binding (G) domain; within-query FDR = 0.0371), (STRING InterPro GTPase GIMA/IAN/Toc; within-query FDR = 0.0371), (STRING NetworkNeighborAL GTPase GIMA/IAN/Toc; within-query FDR = 0.0403). It also has disease associations involving metabolic, pulmonary, inflammatory, and vascular conditions and has a substantial literature record.
- **Conclusion**: Established evidence supports GIMAP4 as the network anchor and as a member of the IAN-family GTPase group. Its role as a coordinator connecting immune-associated nucleotide biology to the metabolic neighbors is a hypothesis, not a demonstrated mechanism.

#### GIMAP1

- **Related proteins** (co-abundance neighbors): GIMAP4 (0.85), TBXAS1 (0.85); STRING partners: GIMAP4 (0.818)
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GTPase, IMAP family member 1. This gene encodes a protein belonging to the GTP-binding superfamily and to the immuno-associated nucleotide (IAN) subfamily of nucleotide-binding proteins. In humans, the IAN subfamily genes are located in a cluster at 7q36.1. This gene is thought to be involved in the differentiation of T helper (Th) cells of the Th1 lineage, and the related mouse gene has been shown to be critical for the devel…
- **Diseases (Open Targets)**: hypertensive disorder (0.305); essential hypertension (0.284); Thrombophlebitis (0.082); phlebitis (0.082); lung adenocarcinoma (0.045)
- **Europe PMC papers**: 280
- **Why important**: GIMAP1 forms the only high-confidence STRING pair in the module with GIMAP4 and is directly connected to TBXAS1 in the co-abundance graph. It is an IAN-family GTPase with lymphoid-tissue enhancement, has a reported relationship to T-helper-cell differentiation, and the related mouse gene is described as important for mature B- and T-lymphocyte development. It also has disease associations involving hypertension and thrombotic or vascular phenotypes.
- **Conclusion**: Established evidence supports GIMAP1 as an immune-associated IAN-family component and as part of the known GIMAP1–GIMAP4 relationship. Connecting its abundance to thromboxane metabolism through TBXAS1 remains a module-level hypothesis.

#### TBXAS1

- **Related proteins** (co-abundance neighbors): GIMAP1 (0.85), TRIM21 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Endoplasmic reticulum, Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thromboxane A synthase 1. This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. However, this protein is considered a member of the cytochrome P450 superfamily on the basis of sequence similarity rather than functional similarity. This endopla…
- **Diseases (Open Targets)**: ghosal hematodiaphyseal dysplasia (0.787); platelet-type bleeding disorder 14 (0.548); anemia (phenotype) (0.371); bone disorder (0.371); Recurrent thrombophlebitis (0.370)
- **Europe PMC papers**: 1037
- **Why important**: TBXAS1 provides the clearest biochemical bridge from the GIMAP pair toward lipid mediator biology. It catalyzes thromboxane A2 production from prostaglandin H2, is annotated with prostaglandin, fatty-acid, and icosanoid processes, and is blood-cell group enriched across several myeloid populations. It is detected in both tissues, has extensive literature, and has disease associations involving bleeding, anemia, bone, and thrombotic phenotypes.
- **Conclusion**: Established evidence supports TBXAS1 as an endoplasmic-reticulum-associated thromboxane and eicosanoid enzyme with hematopoietic relevance. Its co-abundance with GIMAP1 may reflect shared immune-cell composition or coordinated inflammatory metabolism, but direct functional coupling is not established by the supplied evidence.

#### ACSL4

- **Related proteins** (co-abundance neighbors): GIMAP4 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 4. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme preferentially util…
- **Diseases (Open Targets)**: non-syndromic X-linked intellectual disability (0.734); neurodegenerative disease (0.545); Alport syndrome-intellectual disability-midface hypoplasia-elliptocytosis syndrome (0.509); Alzheimer disease (0.384); Parkinson disease (0.381)
- **Europe PMC papers**: 10097
- **Why important**: ACSL4 is connected to the module hub GIMAP4 and provides a lipid-metabolism dimension through activation of long-chain fatty acids, with preference for arachidonate. It is expressed across several cell types including alveolar cells, mast cells, and neutrophils, has broad tissue specificity, and has a very extensive literature record with disease associations involving neurological and renal disorders.
- **Conclusion**: Established evidence supports ACSL4 as a long-chain fatty-acid and arachidonate-handling enzyme. Its placement beside GIMAP4 suggests a possible immune-lipid interface in the module, but the supplied network does not establish a direct biochemical interaction.

#### TRIM21

- **Related proteins** (co-abundance neighbors): TBXAS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tripartite motif containing 21. This gene encodes a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The encoded protein is part of the RoSSA ribonucleoprotein, which includes a single polypeptide and one of four small RNA molecules. The RoSSA particle localizes to both the cytoplasm and the nucleus. RoSSA intera…
- **Diseases (Open Targets)**: thalassemia (0.320); schizophrenia (0.140); sign or symptom (0.137); inherited hemoglobinopathy (0.135); systemic sclerosis (0.123)
- **Europe PMC papers**: 3875
- **Why important**: TRIM21 connects to TBXAS1 and contributes an immune-regulatory and protein-ubiquitination dimension. It is associated with the RoSSA ribonucleoprotein, autoimmune disease biology, ubiquitination, autophagy, and proteasomal regulation. HPA identifies it in neutrophils and detects it in both tissues, while its disease and literature evidence are extensive.
- **Conclusion**: Established evidence supports TRIM21 as an intracellular immune regulator involved in ubiquitin-related processes and autoimmune disease biology. Its relationship to TBXAS1 in this module may indicate shared myeloid or inflammatory context, but a mechanistic TRIM21–TBXAS1 pathway is not established.

## Module 6

**Tissue pair**: bone_marrow and lung  
**Genes (6)**: PGM3, FKBP15, GMPR2, GRIPAP1, MIB1, OTUD7B

### Function

No GO or KEGG term passed global multiple-testing correction, so the module does not support a specific pathway assignment from enrichment. The gene annotations instead point to a mixed intracellular program involving ubiquitin-dependent regulation, endocytosis, membrane or vesicle-associated processes, carbohydrate and glycoprotein metabolism, purine metabolism, and receptor-trafficking functions. The co-abundance structure is organized around MIB1, with links to PGM3, GRIPAP1, and FKBP15; OTUD7B connects FKBP15 with GMPR2. Thus, the most defensible interpretation is a putative intracellular regulatory and trafficking module with metabolic components, rather than a demonstrated single biological pathway. The lack of enriched GO or KEGG terms does not invalidate the module.

**Cell composition.** All module genes have low tissue specificity in HPA, and none is secreted. Protein was detected for most genes in both bone marrow and lung, with one gene not detected in each tissue. The single-cell annotations are heterogeneous, including microglia, oligodendrocytes, monocytes, Kupffer cells, pancreatic acinar cells, melanocytes, Schwann cells, photoreceptor cells, cardiomyocytes, myonuclei, and podocytes. Blood-cell specificity is generally low, although two genes are immune-cell enhanced and one is annotated as not detected in immune cells. This pattern does not resemble a plasma-protein module or a uniformly blood-cell-enriched module. It is more consistent with broadly expressed intracellular proteins, potentially influenced by shared or mixed cell populations in the sampled tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no STRING functional-enrichment result was available. No hu.MAP complex contained multiple module members. Therefore, the co-abundance relationships are not corroborated here by known high-confidence physical interactions or a shared hu.MAP complex. The absence of such support means the network should be interpreted as a coordinated expression or abundance pattern, not as evidence that all genes form one physical complex. Known functions still provide biologically plausible links: MIB1 and OTUD7B represent opposing ubiquitin-system activities, FKBP15 is associated with membrane, endocytic, and protein-isomerization functions, PGM3 supports glycan-related metabolism, GMPR2 supports purine metabolism, and GRIPAP1 is associated with vesicle and receptor trafficking.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported co-abundance association because the supplied network has no high-confidence STRING edges, no multi-member hu.MAP complex, and no STRING enrichment result. However, these database absences do not prove novelty: co-abundance can reflect shared cell composition, common regulation, technical or sampling effects, or relationships not captured by curated interaction resources. The absence of globally significant GO or KEGG enrichment also prevents a strong claim that this is a newly discovered pathway. The cautious conclusion is that the specific cross-tissue co-abundance pattern appears potentially novel, while its underlying biology remains unvalidated.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of intracellular trafficking and protein homeostasis together with metabolic support in broadly expressed cells shared between bone marrow and lung. MIB1-mediated ubiquitination and OTUD7B-mediated deubiquitination could influence receptor or signaling turnover, while FKBP15 may connect this regulation to membrane or endocytic processes. PGM3 and GMPR2 could provide glycan and nucleotide metabolic context, and GRIPAP1 could represent vesicle or receptor-trafficking regulation. This is a mechanistic hypothesis rather than an established module function and should be tested with cell-resolved data, perturbation experiments, and independent cohorts.

### Important genes

#### MIB1

- **Related proteins** (co-abundance neighbors): PGM3 (0.87), GRIPAP1 (0.85), FKBP15 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Microtubules, Primary cilium; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MIB E3 ubiquitin protein ligase 1. This gene encodes a protein containing multiple ankyrin repeats and RING finger domains that functions as an E3 ubiquitin ligase. The encoded protein positively regulates Notch signaling by ubiquitinating the Notch receptors, thereby facilitating their endocytosis. This protein may also promote the ubiquitination and degradation of death-associated protein kinase 1 (DAPK1). [provided by RefSeq, Ju…
- **Diseases (Open Targets)**: left ventricular noncompaction (0.625); hypercholesterolemia, familial, 1 (0.333); type 2 diabetes mellitus (0.268); Abnormality of the skeletal system (0.266); musculoskeletal system disorder (0.250)
- **Europe PMC papers**: 3711
- **Why important**: MIB1 is the most connected node in the module and links PGM3, GRIPAP1, and FKBP15. Its established E3 ubiquitin-ligase function, positive regulation of Notch receptor endocytosis, and role in protein ubiquitination provide a plausible regulatory anchor for the module. It also has the largest literature volume among the module genes and disease associations involving cardiac, metabolic, and skeletal-system phenotypes.
- **Conclusion**: Established evidence supports MIB1 as the strongest network and functional anchor. It is reasonable to hypothesize that MIB1-related protein turnover or receptor endocytosis contributes to the co-abundance pattern, but the module does not establish that MIB1 directly regulates the other members.

#### OTUD7B

- **Related proteins** (co-abundance neighbors): FKBP15 (0.90), GMPR2 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Microtubules; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OTU deubiquitinase 7B. Enables Lys48-specific deubiquitinase activity and thiol-dependent deubiquitinase. Involved in several processes, including negative regulation of I-kappaB kinase/NF-kappaB signaling; negative regulation of macromolecule metabolic process; and protein deubiquitination. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: atopic eczema (0.145); breast cancer (0.123); breast carcinoma (0.103); non-small cell lung carcinoma (0.090); hepatocellular carcinoma (0.088)
- **Europe PMC papers**: 648
- **Why important**: OTUD7B connects FKBP15 and GMPR2 and contributes a mechanistically complementary deubiquitinase activity to the ubiquitin-ligase function of MIB1. Its established roles include protein deubiquitination, negative regulation of canonical NF-kappa-B signaling, mucosal immune response, and regulation of interleukin-eight production. It is immune-cell enhanced in basophils and has disease associations including atopic eczema and lung carcinoma.
- **Conclusion**: Established evidence supports OTUD7B as a plausible signaling and immune-regulatory component. Its co-abundance with MIB1 is compatible with coordinated ubiquitin-system regulation, but no direct physical relationship or causal connection between them is demonstrated here.

#### FKBP15

- **Related proteins** (co-abundance neighbors): OTUD7B (0.90), MIB1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoli; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FKBP prolyl isomerase family member 15. Predicted to enable actin binding activity and peptidyl-prolyl cis-trans isomerase activity. Predicted to be involved in endocytosis and protein peptidyl-prolyl isomerization. Located in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Wiskott-Aldrich syndrome (0.370); neurodegenerative disease (0.370); schizophrenia (0.199); hereditary disease (0.118); liver disorder (0.037)
- **Europe PMC papers**: 281
- **Why important**: FKBP15 links OTUD7B with MIB1 and is annotated for actin binding, peptidyl-prolyl isomerase activity, endocytosis, and membrane localization. HPA annotations associate it with Kupffer cells, microglia, monocytes, and neutrophils, including an enhanced non-classical-monocyte signal. Its literature volume is smaller than that of the principal ubiquitin and metabolic genes, making it a potentially informative but less established connector.
- **Conclusion**: Established evidence supports FKBP15 as a candidate trafficking or cytoskeletal interface. Its network position makes it important for the module interpretation, while its precise role in the shared bone-marrow and lung pattern remains a hypothesis.

#### PGM3

- **Related proteins** (co-abundance neighbors): MIB1 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglucomutase 3. This gene encodes a member of the phosphohexose mutase family. The encoded protein mediates both glycogen formation and utilization by catalyzing the interconversion of glucose-1-phosphate and glucose-6-phosphate. A non-synonymous single nucleotide polymorphism in this gene may play a role in resistance to diabetic nephropathy and neuropathy. Alternatively spliced transcript variants encoding mult…
- **Diseases (Open Targets)**: immunodeficiency 23 (0.838); severe combined immunodeficiency (0.643); combined immunodeficiency (0.465); hyper-IgE syndrome (0.457); hereditary disease (0.415)
- **Europe PMC papers**: 1095
- **Why important**: PGM3 is connected to MIB1 and has an established role in interconverting glucose phosphate metabolites. It also contributes to glucosamine metabolism, UDP-linked N-acetylglucosamine biosynthesis, and protein glycosylation, and is associated with hemopoiesis. Its disease associations include immunodeficiency and severe combined immunodeficiency, giving it strong biological relevance to bone-marrow biology.
- **Conclusion**: Established evidence supports PGM3 as a metabolic and glycosylation-related component with hematopoietic relevance. Its connection to MIB1 may indicate coordinated regulation of glycoprotein or receptor processing, but that mechanistic link is not established by the supplied data.

#### GMPR2

- **Related proteins** (co-abundance neighbors): OTUD7B (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: guanosine monophosphate reductase 2. This gene encodes an enzyme that catalyzes the irreversible and NADPH-dependent reductive deamination of guanosine monophosphate (GMP) to inosine monophosphate (IMP). The protein also functions in the re-utilization of free intracellular bases and purine nucleosides. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2017].
- **Diseases (Open Targets)**: refractive error (0.440); Abnormality of refraction (0.342); uterine corpus leiomyoma (0.055); prostate carcinoma (0.024); leukemia (0.023)
- **Europe PMC papers**: 193
- **Why important**: GMPR2 is connected to OTUD7B and catalyzes NADPH-dependent conversion of GMP to IMP while participating in purine and nucleotide metabolism. Its HPA single-cell annotations include microglia and oligodendrocytes, and its protein was detected in lung. Although its literature volume and network connectivity are limited, it adds a distinct nucleotide-metabolism dimension to the module.
- **Conclusion**: Established evidence supports GMPR2 as a purine-metabolism component. Its association with OTUD7B may reflect coordinated cellular state or metabolic demand, but a direct functional relationship and a specific role in the cross-tissue module remain unproven.

## Module 7

**Tissue pair**: bone_marrow and lung  
**Genes (6)**: AGRN, ANKZF1, CSTF2T, DENND4C, RFC1, SMG1

### Function

No GO or KEGG term passed global correction, so there is no statistically supported pathway-level functional label for this module. The gene composition instead suggests a mixed cellular module. SMG1 is associated with nonsense-mediated mRNA decay, mRNA export, DNA-damage response and protein phosphorylation. CSTF2T is associated with messenger-RNA cleavage and polyadenylation, while RFC1 participates in DNA replication, DNA repair and telomere maintenance. DENND4C is linked to Rab regulation, protein localization to the plasma membrane and cellular response to insulin. AGRN represents an extracellular matrix and receptor-signaling component, whereas ANKZF1 is associated with protein quality control, ER-associated degradation, oxidative-stress response and rescue of stalled ribosomes. Taken together, the most defensible interpretation is coordinated abundance of broadly expressed genes spanning RNA surveillance and processing, genome maintenance, proteostasis, intracellular trafficking and extracellular matrix biology, rather than a single established pathway.

**Cell composition.** The module does not appear to be a plasma-protein or broadly secreted module. AGRN is the secreted extracellular-matrix member, while the remaining genes are non-secreted intracellular proteins. All listed genes have low tissue specificity, arguing against a sharply tissue-restricted program. The HPA profile also does not support a coherent blood-cell module: most genes have low immune-cell specificity, one is not detected in immune cells, and SMG1 is immune-cell enhanced in basophils. Cell-type signals are heterogeneous, including renal epithelial cell types for AGRN, myonuclei and thymic myoid cells for SMG1, and cardiomyocytes for CSTF2T. Protein detection is broadly compatible with the sampled tissues, although lung detection is not universal. Thus, shared cell composition or general cellular abundance may contribute to the cross-tissue signal, but the evidence does not indicate a simple blood-contamination or plasma-protein explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional-enrichment result was reported. No high-confidence STRING interaction was reported among the module genes, and no hu.MAP complex contained multiple module members. Therefore, the co-abundance edges should not be interpreted as established physical protein interactions or as membership in a known multiprotein complex. The strongest internal network position belongs to SMG1, which connects to ANKZF1, CSTF2T and DENND4C in the co-abundance graph. DENND4C links SMG1 with AGRN, and AGRN links the module to RFC1. This topology may reflect coordinated regulation, shared cell-state abundance or indirect biological coupling, but the external interaction resources do not independently validate those edges.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is a potentially novel cross-tissue co-abundance pattern, but it cannot be claimed as a newly discovered biological mechanism. Its novelty is supported by the absence of a reported high-confidence STRING interaction pattern, the absence of a shared hu.MAP complex, and the lack of globally significant GO or KEGG enrichment. However, those absences do not prove novelty: the genes have substantial prior annotation and literature, and several have well-established individual functions. The most cautious conclusion is that the particular bone-marrow–lung co-abundance organization is not explained by the supplied canonical interaction or pathway resources, while the component biology itself is not novel.

**Hypothesis.** Hypothesis: the module reflects a shared cell-state or sample-composition program in which general transcript and protein quality control is coordinated with genome maintenance, membrane trafficking and extracellular matrix signaling. SMG1 may act as the central regulatory marker, with ANKZF1 and CSTF2T capturing proteostasis and RNA-processing state, RFC1 capturing replication or repair capacity, DENND4C capturing vesicular trafficking, and AGRN capturing extracellular matrix or receptor-associated context. This hypothesis predicts that the co-abundance pattern will weaken or reorganize after adjustment for cell-type composition and proliferative or stress-related state, and that it should not necessarily correspond to a stable physical complex.

### Important genes

#### SMG1

- **Related proteins** (co-abundance neighbors): ANKZF1 (0.85), CSTF2T (0.81), DENND4C (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SMG1 nonsense mediated mRNA decay associated PI3K related kinase. This gene encodes a protein involved in nonsense-mediated mRNA decay (NMD) as part of the mRNA surveillance complex. The protein has kinase activity and is thought to function in NMD by phosphorylating the regulator of nonsense transcripts 1 protein. Alternatively spliced transcript variants have been described, but their full-length nature has yet to be determined. [provided by RefSeq, Mar 2013].
- **Diseases (Open Targets)**: alcohol drinking (0.251); stroke disorder (0.251); contracture (0.158); neoplasm (0.107); refractive error (0.098)
- **Europe PMC papers**: 1969
- **Why important**: SMG1 is the central network gene, connecting RNA-processing, stress-related and trafficking neighbors in the co-abundance graph. Its established annotations include nonsense-mediated mRNA decay, mRNA export, DNA-damage response and kinase activity. It also has the largest literature volume among the module genes in the fact sheet, making it the best-supported biological anchor. HPA places it in the nucleoplasm and reports immune-cell enhancement in basophils.
- **Conclusion**: Established evidence supports SMG1 as an RNA-surveillance and genome-stress regulator. Its role as the driver of this shared module is a hypothesis based on network position, not a demonstrated causal relationship.

#### AGRN

- **Related proteins** (co-abundance neighbors): DENND4C (0.87), RFC1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: agrin. This gene encodes one of several proteins that are critical in the development of the neuromuscular junction (NMJ), as identified in mouse knock-out studies. The encoded protein contains several laminin G, Kazal type serine protease inhibitor, and epidermal growth factor domains. Additional post-translational modifications occur to add glycosaminoglycans and disulfide bonds. In one family with con…
- **Diseases (Open Targets)**: congenital myasthenic syndrome 8 (0.793); congenital myasthenic syndrome (0.680); presynaptic congenital myasthenic syndrome (0.652); postsynaptic congenital myasthenic syndrome (0.626); COVID-19 (0.546)
- **Europe PMC papers**: 2731
- **Why important**: AGRN is a network bridge connecting DENND4C and RFC1, and it is the module's extracellular-matrix and secreted member. Its established biology includes neuromuscular-junction development, cell-surface signaling and cytoskeletal organization, with disease associations to congenital myasthenic syndromes. HPA links its expression to several renal epithelial cell types and confirms protein detection in both sampled tissues.
- **Conclusion**: Established evidence supports AGRN as an extracellular signaling and matrix protein with relevant disease biology. Its connection to the intracellular RNA and DNA-maintenance genes is currently a co-abundance observation and should be treated as a hypothesis.

#### RFC1

- **Related proteins** (co-abundance neighbors): AGRN (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: replication factor C subunit 1. This gene encodes the large subunit of replication factor C, a five subunit DNA polymerase accessory protein, which is a DNA-dependent ATPase required for eukaryotic DNA replication and repair. The large subunit acts as an activator of DNA polymerases, binds to the 3' end of primers, and promotes coordinated synthesis of both strands. It may also have a role in telomere stability. Alternatively sp…
- **Diseases (Open Targets)**: cerebellar ataxia with neuropathy and bilateral vestibular areflexia syndrome (0.700); Parkinson disease (0.354); late-onset Parkinson disease (0.333); asthma (0.327); polyneuropathy (0.271)
- **Europe PMC papers**: 2323
- **Why important**: RFC1 connects to AGRN in the module and represents a well-characterized nuclear replication and repair factor. It participates in DNA replication, DNA repair and telomere maintenance, and has substantial literature and disease associations including neurological and polyneuropathy phenotypes. HPA reports broad tissue distribution and nuclear localization in the fact sheet.
- **Conclusion**: Established evidence supports RFC1 as a replication and DNA-repair factor. Its co-abundance with AGRN does not establish a direct functional relationship; a shared cellular state or indirect regulatory program is the more cautious interpretation.

#### CSTF2T

- **Related proteins** (co-abundance neighbors): SMG1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cleavage stimulation factor subunit 2 tau variant. Enables RNA binding activity. Predicted to be involved in pre-mRNA cleavage required for polyadenylation. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dengue disease (0.370); smoking initiation (0.347); Abnormality of the skeletal system (0.307); laryngeal carcinoma (0.287); breast cancer (0.268)
- **Europe PMC papers**: 341
- **Why important**: CSTF2T is connected to the central SMG1 node and provides a specific RNA-processing interpretation for the module. It encodes a cleavage-stimulation factor tau variant with RNA-binding activity and a role in messenger-RNA three-prime-end processing. HPA reports nucleoplasmic localization and cell-type enhancement in cardiomyocytes.
- **Conclusion**: Established evidence supports CSTF2T as an RNA maturation factor. Its placement beside SMG1 is consistent with coordinated RNA surveillance or processing, but the module does not demonstrate that CSTF2T and SMG1 act together in a physical complex.

#### DENND4C

- **Related proteins** (co-abundance neighbors): AGRN (0.87), SMG1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus, Vesicles, Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DENN domain containing 4C. Enables guanyl-nucleotide exchange factor activity. Predicted to be involved in cellular response to insulin stimulus; protein localization to plasma membrane; and regulation of Rab protein signal transduction. Located in Golgi apparatus and cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.329); metabolic disease (0.232); Peyronie disease (0.203); bilirubin metabolism disease (0.118); intracranial hemorrhage (0.097)
- **Europe PMC papers**: 224
- **Why important**: DENND4C is a bridge between SMG1 and AGRN and is therefore important for connecting the module's nuclear and extracellular-associated portions. Its established annotations include guanine-nucleotide exchange activity, Rab signaling, plasma-membrane localization and response to insulin. HPA places it in the Golgi, vesicles and cytosol, consistent with a trafficking role. Its literature volume is comparatively limited, which makes it a useful but less secure mechanistic anchor.
- **Conclusion**: Established evidence supports DENND4C as a trafficking and Rab-regulatory protein. Its bridging position suggests a possible integrative role in the module, but that role is a hypothesis because neither STRING nor hu.MAP provides independent interaction support.

## Module 8

**Tissue pair**: bone_marrow and lung  
**Genes (6)**: ARFRP1, GALNT7, SLC2A1, HSDL2, OCIAD2, SCYL3

### Function

The module does not have a firmly established pathway-level function from enrichment: no GO or KEGG term passed global correction, and STRING functional enrichment was absent. Its gene annotations instead point to intracellular membrane trafficking, Golgi organization, glycosylation, glucose transport, mitochondrial or peroxisomal metabolism, endocytosis, receptor signalling, and cell migration. ARFRP1 is the central network connector and links genes involved in Golgi trafficking, glycosylation, mitochondrial biology, and glucose transport. This supports a cautious interpretation as a coordinated intracellular trafficking and metabolic state rather than a specific canonical pathway.

**Cell composition.** The module is not composed of secreted proteins. HPA reports low immune-cell specificity for every member, so the module is not strongly characteristic of a blood-cell program. Several genes are tissue or cell-type enhanced, but the reported tissues and cell types are heterogeneous, including placenta, tongue, kidney, stomach, neutrophils, epithelial cells, adipocytes, and glial cells. This heterogeneity does not identify one shared cell type between bone marrow and lung. Protein detection is broadly present in both tissues, with some gene-specific exceptions. A shared housekeeping-like intracellular program or a mixture of cell states is more plausible than a simple plasma-protein or blood-contamination explanation, although sample composition could still contribute.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and no hu.MAP complex contained multiple module members. Thus the co-abundance relationships are not supported by the listed known physical interaction network or by a detected shared complex. The absence of these database relationships does not disprove coordinated regulation or indirect functional coupling. ARFRP1 is the network hub in the co-abundance graph, while SLC2A1 connects the hub to SCYL3; the remaining genes form hub-linked peripheral relationships.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously under-recognized co-abundance association because its member relationships have no corresponding high-confidence STRING interactions or multi-member hu.MAP complex. However, that database absence alone cannot establish a new biological mechanism. The genes individually have established functions and disease associations, and the lack of globally significant enrichment makes the module-level novelty claim tentative. The strongest defensible claim is that this particular cross-tissue co-abundance pattern appears insufficiently explained by the queried interaction and complex resources and requires independent validation.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of intracellular trafficking and cell-surface or secretory-pathway processing coupled to cellular energy handling. In this model, ARFRP1-centered Golgi trafficking could covary with GALNT7-dependent mucin-type O-linked glycosylation, SLC2A1-mediated glucose transport, mitochondrial or peroxisomal functions associated with HSDL2 and OCIAD2, and migration or adhesion-related activity associated with SCYL3. This is a mechanistic hypothesis rather than an established pathway assignment, because enrichment, STRING, and hu.MAP evidence do not independently support it.

### Important genes

#### ARFRP1

- **Related proteins** (co-abundance neighbors): HSDL2 (0.89), GALNT7 (0.86), OCIAD2 (0.80), SLC2A1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ARF related protein 1. The protein encoded by this gene is a membrane-associated GTP-ase which localizes to the plasma membrane and is related to the ADP-ribosylation factor (ARF) and ARF-like (ARL) proteins. This gene plays a role in membrane trafficking between the trans-Golgi network and endosomes. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, May 201…
- **Diseases (Open Targets)**: atopic eczema (0.283); inflammatory bowel disease (0.208); metabolic syndrome (0.205); prostate carcinoma (0.202); dermatitis (0.196)
- **Europe PMC papers**: 406
- **Why important**: ARFRP1 has the strongest network position and connects the other trafficking, glycosylation, mitochondrial, and glucose-transport-related members. Its established annotation places it in membrane trafficking between the trans-Golgi network and endosomes, and it has a substantial literature base and multiple disease-area associations.
- **Conclusion**: Established evidence supports ARFRP1 as the central co-abundance connector and a Golgi trafficking regulator. It is a plausible organizing gene for the module, but the data do not establish that it causally drives the other genes.

#### SLC2A1

- **Related proteins** (co-abundance neighbors): SCYL3 (0.80), ARFRP1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 2 member 1. This gene encodes a major glucose transporter in the mammalian blood-brain barrier. The encoded protein is found primarily in the cell membrane and on the cell surface, where it can also function as a receptor for human T-cell leukemia virus (HTLV) I and II. Mutations in this gene have been found in a family with paroxysmal exertion-induced dyskinesia. [provided by RefSeq, Apr 2013].
- **Diseases (Open Targets)**: encephalopathy due to GLUT1 deficiency (0.852); childhood onset GLUT1 deficiency syndrome 2 (0.833); dystonia 9 (0.804); hereditary cryohydrocytosis with reduced stomatin (0.778); idiopathic generalized epilepsy (0.757)
- **Europe PMC papers**: 14405
- **Why important**: SLC2A1 is the module member with the largest literature volume and has the disease-associated GLUT1 deficiency spectrum in Open Targets. It is also the bridge from ARFRP1 to SCYL3 in the module and encodes a major plasma-membrane glucose transporter with links to hypoxia and cellular metabolism.
- **Conclusion**: Established evidence supports a role in glucose transport and energy-related cellular responses. Its module association may indicate metabolic coupling with trafficking processes, but a tissue-specific role in this module remains unproven.

#### GALNT7

- **Related proteins** (co-abundance neighbors): ARFRP1 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypeptide N-acetylgalactosaminyltransferase 7. This gene encodes GalNAc transferase 7, a member of the GalNAc-transferase family. The enzyme encoded by this gene controls the initiation step of mucin-type O-linked protein glycosylation and transfer of N-acetylgalactosamine to serine and threonine amino acid residues. This enzyme is a type II transmembrane protein and shares common sequence motifs with other family members. Unlike other family …
- **Diseases (Open Targets)**: immune system disorder (0.291); color vision disorder (0.254); Hydrocephalus (0.252); Parkinson disease (0.228); alcohol drinking (0.209)
- **Europe PMC papers**: 758
- **Why important**: GALNT7 is a Golgi-localized transferase that initiates mucin-type O-linked glycosylation and is directly connected to the network hub ARFRP1. Its HPA profile includes tissue and cell-type enhancement in gastrointestinal and neutrophil-associated contexts, providing biological context for regulated glycoprotein processing.
- **Conclusion**: Established evidence supports a specialized glycosylation function and a plausible relationship to Golgi trafficking. Its participation in a shared bone-marrow and lung program is a hypothesis rather than a demonstrated tissue mechanism.

#### OCIAD2

- **Related proteins** (co-abundance neighbors): ARFRP1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OCIA domain containing 2. Predicted to be involved in endocytosis; hematopoietic stem cell homeostasis; and positive regulation of receptor signaling pathway via JAK-STAT. Predicted to act upstream of or within response to bacterium. Predicted to be located in Golgi apparatus; endosome; and lysosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.441); type 2 diabetes mellitus (0.419); diabetes mellitus (0.315); placenta praevia (0.210); uterine corpus leiomyoma (0.210)
- **Europe PMC papers**: 329
- **Why important**: OCIAD2 is linked in the module to ARFRP1 and has annotations involving endocytosis, hematopoietic stem-cell homeostasis, receptor signalling, mitochondrial respiratory-chain assembly, and response to bacteria. It is detected in lung protein assays and has disease associations including skeletal abnormality and diabetes-related traits.
- **Conclusion**: Established evidence supports possible roles in endocytic, mitochondrial, and signalling biology. The co-abundance pattern suggests that OCIAD2 could connect trafficking with cellular state, but its precise contribution to this module is not resolved.

#### HSDL2

- **Related proteins** (co-abundance neighbors): ARFRP1 (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydroxysteroid dehydrogenase like 2. Predicted to enable oxidoreductase activity. Located in mitochondrion and peroxisome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: preeclampsia (0.258); placental retention (0.217); squamous cell carcinoma (0.190); smoking initiation (0.152); cholangiocarcinoma (0.101)
- **Europe PMC papers**: 403
- **Why important**: HSDL2 is connected directly to the ARFRP1 hub and is annotated as an oxidoreductase-related protein located in mitochondria and peroxisomes, with a role in cholesterol homeostasis. Its HPA profile includes enhancement in tongue and several cell types, including neutrophils.
- **Conclusion**: Established evidence supports a metabolic and organelle-associated function. Its relationship to the Golgi-centered portion of the module is mechanistically uncertain, so any proposed trafficking-to-metabolism link should be treated as provisional.

## Module 9

**Tissue pair**: bone_marrow and lung  
**Genes (5)**: ARID2, FIP1L1, GCC2, PHF14, RBM7

### Function

The module does not have a globally significant GO or KEGG enrichment term, and STRING reports no supplementary functional enrichment. Its genes nevertheless converge functionally on intracellular gene regulation: RBM7 is associated with snRNA catabolism, RNA binding, and alternative splicing; FIP1L1 with messenger RNA three-prime-end processing and polyadenylation; ARID2 with PBAF chromatin remodeling and transcriptional regulation; PHF14 with histone binding, chromatin organization, and regulation of transcription; and GCC2 with Golgi and endosome-to-Golgi trafficking. The co-abundance pattern therefore suggests a weak, mixed nuclear gene-expression and cellular-maintenance program rather than a sharply defined canonical pathway. This interpretation is an inference from the annotations, not evidence of significant enrichment.

**Cell composition.** The module is composed entirely of intracellular proteins rather than plasma or secreted proteins. HPA classifies every member as having low immune-cell specificity, and none is secreted. Most members have low tissue specificity, while several show cell-type enhancement in reproductive cell types and one is tissue-enhanced in bone marrow. Protein detection is present for most members in both bone marrow and lung, with one member lacking HPA protein data. The composition therefore does not support a plasma-protein or blood-cell-specific module. It is more consistent with broadly distributed intracellular biology, with possible contributions from shared cellular composition or general cellular-state effects in the two tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship is reported among the module members, and no hu.MAP complex contains multiple members. The observed co-abundance edges are therefore not supported by the supplied catalogues as established physical interactions or membership in a known multiprotein complex. This weakens a direct-complex interpretation, but it does not exclude co-regulation, indirect functional coupling, shared expression control, or interactions below the catalogue thresholds.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module-level co-abundance pattern may be a previously unreported association because its members lack documented high-confidence STRING links and shared hu.MAP complex membership. However, those absences do not establish biological novelty: the genes have established functions, several have substantial literature, and the pattern could reflect broad intracellular expression, shared cellular state, or indirect regulation. The appropriate conclusion is that the cross-tissue co-abundance configuration is potentially novel but remains unvalidated as a new biological mechanism.

**Hypothesis.** Hypothesis: in both bone marrow and lung, a shared intracellular state may coordinate RNA maturation and chromatin-dependent transcription with supporting membrane-trafficking processes. RBM7 and FIP1L1 could represent an RNA-processing branch, ARID2 and PHF14 a chromatin and transcriptional-regulatory branch, and GCC2 a trafficking-related branch. Their co-abundance may reflect coordinated regulation or cell-state composition rather than a physical complex. This hypothesis should be tested with replication, cell-resolved data, perturbation experiments, and independent measurements of RNA processing, chromatin regulation, and trafficking.

### Important genes

#### RBM7

- **Related proteins** (co-abundance neighbors): ARID2 (0.85), FIP1L1 (0.82), PHF14 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 7. Enables 14-3-3 protein binding activity; pre-mRNA intronic binding activity; and snRNA binding activity. Involved in snRNA catabolic process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.424); breast carcinoma (0.096); breast cancer (0.096); neoplasm (0.051); idiopathic pulmonary fibrosis (0.049)
- **Europe PMC papers**: 406
- **Why important**: RBM7 is the central network member, connecting to ARID2, FIP1L1, and PHF14. Its established annotations include pre-mRNA intronic binding, snRNA binding, snRNA catabolism, and regulation of alternative splicing. It is tissue-enhanced in bone marrow and detected at the protein level in both tissues. Its network centrality makes it the strongest candidate for representing the module's RNA-processing and nuclear-regulatory component.
- **Conclusion**: Established evidence supports RBM7 as an RNA-associated nuclear regulator and as the principal connectivity hub of this module. The hypothesis that it coordinates the other module members is plausible from network position but is not demonstrated by the supplied interaction resources.

#### ARID2

- **Related proteins** (co-abundance neighbors): RBM7 (0.85), GCC2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: AT-rich interaction domain 2. This gene encodes a member of the AT-rich interactive domain (ARID)-containing family of DNA-binding proteins. Members of the ARID family have roles in embryonic patterning, cell lineage gene regulation, cell cycle control, transcriptional regulation and chromatin structure modification. This protein functions as a subunit of the polybromo- and BRG1-associated factor or PBAF (SWI/SNF-B) chromatin …
- **Diseases (Open Targets)**: Coffin-Siris syndrome 6 (0.725); hepatocellular carcinoma (0.634); melanoma (0.626); Coffin-Siris syndrome (0.533); hereditary disease (0.533)
- **Europe PMC papers**: 3359
- **Why important**: ARID2 links the central RBM7 branch to GCC2 and is an established subunit of the PBAF chromatin-remodeling complex. Its annotations include chromatin remodeling, transcriptional regulation, cell-cycle regulation, and regulation of cell migration. It has extensive disease and literature associations, including Coffin-Siris syndrome and several cancers, making it the best-supported chromatin-regulatory anchor in the module.
- **Conclusion**: Established evidence supports ARID2 as a chromatin-remodeling and transcriptional regulator. Its connection to RBM7 and GCC2 may indicate coordinated cellular regulation, but the module does not establish a direct ARID2 interaction with those proteins.

#### FIP1L1

- **Related proteins** (co-abundance neighbors): RBM7 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: factor interacting with PAPOLA and CPSF1. This gene encodes a subunit of the CPSF (cleavage and polyadenylation specificity factor) complex that polyadenylates the 3' end of mRNA precursors. This gene, the homolog of yeast Fip1 (factor interacting with PAP), binds to U-rich sequences of pre-mRNA and stimulates poly(A) polymerase activity. Its N-terminus contains a PAP-binding site and its C-terminus an RNA-binding domain. An interstitial …
- **Diseases (Open Targets)**: cancer (0.465); Abnormality of the skeletal system (0.406); dengue disease (0.370); benign neoplasm of pituitary gland (0.206); response to stimulus (0.198)
- **Europe PMC papers**: 1832
- **Why important**: FIP1L1 is directly connected to RBM7 and encodes a component of the cleavage and polyadenylation specificity machinery. Its functions include binding U-rich pre-mRNA sequences and stimulating polyadenylase activity. It is detected in both bone marrow and lung and has substantial literature, including work on the FIP1L1-PDGFRA fusion. It is therefore an important bridge between the module's co-abundance structure and messenger RNA maturation.
- **Conclusion**: Established evidence supports FIP1L1 as an mRNA three-prime-end-processing factor with disease relevance through a known fusion event. Its co-abundance with RBM7 is consistent with coordinated RNA metabolism, but a specific shared mechanism in bone marrow and lung remains a hypothesis.

#### PHF14

- **Related proteins** (co-abundance neighbors): RBM7 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PHD finger protein 14. Predicted to enable histone binding activity. Predicted to be involved in histone H3-K14 acetylation and regulation of transcription by RNA polymerase II. Predicted to act upstream of or within several processes, including lung alveolus development; negative regulation of mesenchymal cell proliferation involved in lung development; and negative regulation of platelet-derived growth factor receptor…
- **Diseases (Open Targets)**: neurodegenerative disease (0.550); lysosomal storage disease (0.343); preeclampsia (0.305); idiopathic pulmonary fibrosis (0.277); COVID-19 (0.237)
- **Europe PMC papers**: 272
- **Why important**: PHF14 is connected to RBM7 and is annotated with histone binding, chromatin organization, and regulation of transcription. The supplied annotations also link it to lung alveolus development, mesenchymal-cell proliferation, and platelet-derived growth factor receptor-alpha signaling, giving it particular relevance to lung biology. It is detected in both tissues, although its literature volume is more limited than that of the other principal regulatory genes.
- **Conclusion**: Established evidence supports PHF14 as a plausible chromatin and transcriptional regulator with lung-development relevance. Its placement beside RBM7 suggests a possible link between RNA processing and chromatin state, but this cross-process relationship is not established by the available interaction databases.

#### GCC2

- **Related proteins** (co-abundance neighbors): ARID2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GRIP and coiled-coil domain containing 2. The protein encoded by this gene is a peripheral membrane protein localized to the trans-Golgi network. It is sensitive to brefeldin A. This encoded protein contains a GRIP domain which is thought to be used in targeting. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2009].
- **Diseases (Open Targets)**: cancer (0.481); kidney disorder (0.203); immunodeficiency disease (0.185); immune system disorder (0.185); Progressive sensorineural hearing impairment (0.111)
- **Europe PMC papers**: 449
- **Why important**: GCC2 is connected to ARID2 and provides the module's clearest trafficking-related component. It is a trans-Golgi peripheral membrane protein involved in protein targeting to lysosomes, Golgi localization, microtubule anchoring, and retrograde endosome-to-Golgi transport. It is detected in both tissues and broadens the module beyond nuclear RNA and chromatin functions.
- **Conclusion**: Established evidence supports GCC2 as a Golgi and endosomal-trafficking regulator. Its co-abundance with ARID2 may reflect indirect coupling through cellular state or membrane and transcriptional homeostasis, but there is no supplied evidence for a direct functional complex.

## Module 10

**Tissue pair**: bone_marrow and lung  
**Genes (7)**: BAZ2A, BOD1L1, CDKN2AIP, CASP6, EHBP1L1, SCAF8, SMG8

### Function

The module has no GO or KEGG term passing global correction, so its function cannot be assigned from enrichment. The gene annotations instead point to a heterogeneous nuclear regulatory and cellular-maintenance program: SCAF8 is linked to RNA polymerase II transcription termination and elongation, BAZ2A to chromatin organization and transcriptional regulation, CDKN2AIP and BOD1L1 to DNA-damage responses, SMG8 to nonsense-mediated mRNA decay, CASP6 to apoptosis and proteolysis, and EHBP1L1 to actin organization and endocytic recycling. The network is organized around SCAF8, with the other genes connected directly to it and no other reported connections. This supports a possible shared transcriptional or RNA-surveillance context, but not a single established pathway. The absence of significant enrichment does not invalidate the module; it indicates that the genes do not collectively resolve to a globally significant GO or KEGG category.

**Cell composition.** The module is not dominated by secreted or plasma proteins: HPA reports no secreted genes. Most genes have low tissue specificity, and most have low cell-type specificity, consistent with broadly expressed intracellular proteins rather than a tissue-restricted secretory program. Protein detection is broadly compatible with both bone marrow and lung, although one gene is not detected in lung and one has no lung data. There is limited evidence for a blood or immune contribution: BOD1L1 is immune-cell enhanced in neutrophils, while EHBP1L1 is annotated in several cell types including neutrophils but is not detected in immune cells by the HPA blood-cell summary. CASP6 is enriched in megakaryocytes among the listed cell types. The additional HPA enrichments span intestinal, skeletal-muscle, epithelial, reproductive, neural, and stromal-related cell types, so the shared signal may reflect broadly expressed genes, mixed cell composition, or a conserved cellular state rather than a bone-marrow–lung-specific function.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional-enrichment result is reported, and none of the possible gene pairs reaches the supplied STRING interaction threshold. No hu.MAP complex contains multiple module members. Thus, the direct co-abundance structure is not supported by a pre-existing high-confidence protein-interaction network or a known shared complex in these resources. The absence of STRING and hu.MAP support means that the module is primarily a transcript-level co-abundance observation; it does not establish physical interaction among the proteins. The strongest network position belongs to SCAF8, which is connected to every other module member, whereas the remaining genes are peripheral in this module.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears novel as a cross-tissue co-abundance module because the supplied resources show no high-confidence STRING pair, no multi-member hu.MAP complex, no STRING enrichment, and no globally significant GO or KEGG term. However, these absences do not prove biological novelty. Several component genes have established functions and substantial literature, so the novelty is more defensibly the specific coordinated association of this gene set across bone marrow and lung, rather than discovery of new gene functions or a new molecular complex. The lack of a web result for the exact gene-set query provides no independent evidence either for or against prior publication.

**Hypothesis.** Hypothesis: the module may represent a conserved intracellular stress-management state shared by cells present in bone marrow and lung. In this model, SCAF8 provides a transcription-associated hub; SMG8 supports surveillance of aberrant transcripts; BAZ2A contributes chromatin and transcriptional control; CDKN2AIP and BOD1L1 contribute genome-integrity responses; CASP6 marks a possible apoptotic or differentiation-related branch; and EHBP1L1 links the state to membrane trafficking and cytoskeletal organization. This is a mechanistic hypothesis, not an established pathway assignment. It should be tested by replication in independent datasets, cell-type deconvolution, perturbation of SCAF8 or the peripheral genes, and measurement of transcriptional surveillance, DNA-damage, apoptotic, and trafficking readouts.

### Important genes

#### SCAF8

- **Related proteins** (co-abundance neighbors): CASP6 (0.86), BAZ2A (0.85), EHBP1L1 (0.83), CDKN2AIP (0.82), BOD1L1 (0.82), SMG8 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SR-related CTD associated factor 8. Enables RNA binding activity and RNA polymerase II C-terminal domain phosphoserine binding activity. Involved in negative regulation of termination of RNA polymerase II transcription, poly(A)-coupled and positive regulation of DNA-templated transcription, elongation. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: retinal artery occlusion (0.276); allergic rhinitis (0.269); ankylosing spondylitis (0.255); asthma (0.247); ovarian dysfunction (0.236)
- **Europe PMC papers**: 247
- **Why important**: SCAF8 is the network hub, directly connected to all other module members, and has the strongest supplied network position. Its established annotations involve RNA polymerase II transcription termination, elongation, and RNA binding. It is detected in both bone marrow and lung, has low tissue and cell-type specificity, and has a substantial literature base. Its disease associations include respiratory and inflammatory conditions among the listed Open Targets associations, although these associations do not establish a role in this module.
- **Conclusion**: Established evidence supports SCAF8 as the best organizational candidate and as a regulator of transcription-associated processes. It is plausible, but unproven, that SCAF8 coordinates the observed module. The hub position is a property of this co-abundance network and should not be interpreted as physical interaction or causal control.

#### SMG8

- **Related proteins** (co-abundance neighbors): SCAF8 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SMG8 nonsense mediated mRNA decay factor. Involved in nuclear-transcribed mRNA catabolic process, nonsense-mediated decay and regulation of protein kinase activity. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Alzahrani-Kuwahara syndrome (0.730); microcephaly (0.483); Short stature (0.483); Intellectual disability (0.483); Abnormal facial shape (0.483)
- **Europe PMC papers**: 261
- **Why important**: SMG8 is directly connected to SCAF8 and has an established role in nonsense-mediated decay and regulation of the nuclear-transcribed mRNA catabolic process. It is detected in both tissues, has low tissue specificity, and is annotated across several neural and epithelial cell types. Its listed disease associations include a developmental syndrome and neurodevelopmental traits, with a moderate literature volume.
- **Conclusion**: Established evidence supports SMG8 as an RNA-quality-control component. Its presence is consistent with the hypothesis that the module reflects transcript surveillance, but the module data do not show that nonsense-mediated decay is active or enriched.

#### CDKN2AIP

- **Related proteins** (co-abundance neighbors): SCAF8 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CDKN2A interacting protein. The protein encoded by this gene regulates the DNA damage response through several different signaling pathways. One such pathway is the p53-HDM2-p21(WAF1) pathway, which is critical to the DNA damage response. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.488); body weight gain (0.231); urolithiasis (0.194); alcohol drinking (0.194); major depressive disorder (0.165)
- **Europe PMC papers**: 412
- **Why important**: CDKN2AIP is directly connected to the SCAF8 hub and is annotated as a regulator of DNA-damage response pathways involving p53, HDM2, and p21, as well as cell growth and protein stability. It is detected in both bone marrow and lung and has cell-type-enhanced annotations in several epithelial and reproductive cell types. It also has disease associations including neurodegenerative disease and neuropsychiatric traits.
- **Conclusion**: Established evidence supports CDKN2AIP as a genome-stress and growth-regulation gene. Its co-abundance with transcription and RNA-surveillance genes motivates a stress-response interpretation, but it does not demonstrate that a p53-dependent response drives the module.

#### BOD1L1

- **Related proteins** (co-abundance neighbors): SCAF8 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biorientation of chromosomes in cell division 1 like 1. Predicted to enable protein phosphatase 2A binding activity and protein phosphatase inhibitor activity. Involved in cellular response to DNA damage stimulus and replication fork processing. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.515); luminal B breast carcinoma (0.321); sialolithiasis (0.292); Paralysis (0.284); hypopituitarism (0.236)
- **Europe PMC papers**: 151
- **Why important**: BOD1L1 is directly connected to SCAF8 and is annotated for replication-fork processing and cellular response to DNA damage, with predicted protein-phosphatase-related activities. It is detected in both tissues and has the clearest blood-cell signal in the module, being immune-cell enhanced in neutrophils. Its literature volume is smaller than that of CASP6 or BAZ2A, while its listed disease associations include cancer-related and neurological or endocrine traits.
- **Conclusion**: Established evidence supports BOD1L1 as a replication and genome-integrity factor and suggests that neutrophil composition could contribute to its signal. A DNA-damage or cell-state interpretation is plausible, but the module cannot distinguish a shared regulatory program from cell-composition effects.

#### CASP6

- **Related proteins** (co-abundance neighbors): SCAF8 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caspase 6. This gene encodes a member of the cysteine-aspartic acid protease (caspase) family of enzymes. Sequential activation of caspases plays a central role in the execution-phase of cell apoptosis. Caspases exist as inactive proenzymes which undergo proteolytic processing at conserved aspartic acid residues to produce two subunits, large and small, that dimerize to form the active enzyme. This protein i…
- **Diseases (Open Targets)**: cirrhosis of liver (0.108); Alzheimer disease (0.105); metabolic dysfunction-associated steatohepatitis (0.099); retinitis pigmentosa (0.099); early-onset non-syndromic cataract (0.092)
- **Europe PMC papers**: 2022
- **Why important**: CASP6 is directly connected to SCAF8 and is the module member with the clearest established enzymatic and apoptotic function. It is a caspase involved in proteolysis, apoptosis, innate immune-response activation, and epithelial differentiation. It is tissue-enhanced in intestine, detected in bone marrow but not detected in lung by the supplied HPA evidence, and is annotated in enteric progenitor populations and megakaryocytes. It also has the largest literature volume among the listed genes.
- **Conclusion**: Established evidence supports CASP6 as an apoptosis- and differentiation-related protease. Its asymmetric tissue detection and cell-type annotations make it a useful marker of possible composition or state effects. It should not be treated as evidence that apoptosis is the defining function of the whole module.

## Module 11

**Tissue pair**: bone_marrow and lung  
**Genes (7)**: BLVRA, C5orf22, PDF, FH, GSTP1, CTSA, SMAP

### Function

The module is best interpreted as a weakly integrated cellular stress, redox, detoxification, and organelle-maintenance program rather than a defined canonical pathway. Its genes include fumarate hydratase and biliverdin reductase A, which support mitochondrial and cytosolic metabolic redox processes; glutathione S-transferase pi one, which supports glutathione-dependent detoxification and responses to reactive oxygen species; cathepsin A, which supports lysosomal protein processing and stability; and mitochondrial peptide deformylase, which supports processing of newly synthesized organellar proteins. The co-abundance structure places C5orf22 as the main connector, with separate branches involving CTSA-PDF and FH-BLVRA. No GO or KEGG term passed global correction, so the functional interpretation is driven by the gene annotations and network structure rather than by significant enrichment. The absence of enrichment does not invalidate the module.

**Cell composition.** The module is not dominated by plasma or secreted proteins. HPA marks a minority of the genes as secreted, while the supplied gene-level annotations mainly describe intracellular, membrane-associated, mitochondrial, cytosolic, vesicular, or nuclear-membrane proteins. Most genes have low immune-cell specificity, although HPA shows immune-cell enrichment or enhancement for C5orf22 and PDF, including basophil and naive B-cell associations. Tissue and cell-type signals are mixed, including liver, esophagus, adrenal gland, mast cells, platelets, respiratory ciliated and deuterosomal cells, Hofbauer cells, and Kupffer cells. Protein detection is broadly compatible with the two tissues, especially lung, but the mixed HPA profile argues against a simple bone-marrow-specific or lung-specific program. The shared module could therefore reflect broadly distributed cellular states or shared cell populations rather than a tissue-restricted biological pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no supplied high-confidence STRING relationships among the module genes and no STRING functional-enrichment result. Thus, the co-abundance edges should not be presented as established protein-protein interactions. The only external complex support is hu.MAP: SMAP and GSTP1 occur together as module members in (hu.MAP huMAP3_13103.1) and (hu.MAP huMAP3_12535.1). These complexes contain many additional proteins, including KLK3, PRTN3, ADAMTS14, TACO1, TPK1, EGLN3, C1orf174, TMEM69, and NFYA depending on the complex. This supports some prior complex-level association for SMAP and GSTP1, but the limited module representation does not establish that the complete co-abundance module is one physical complex. The remaining relationships are not supported by the supplied STRING or hu.MAP evidence.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13103.1 (SMAP, GSTP1; 2/10); huMAP3_12535.1 (SMAP, GSTP1; 2/11)

### Novelty

The module may represent a previously unreported co-abundance pattern, but it cannot be called a definitively new biological mechanism. Its component genes and several of their functions are already well established, and SMAP-GSTP1 has prior hu.MAP complex support in (hu.MAP huMAP3_13103.1) and (hu.MAP huMAP3_12535.1). Conversely, the absence of STRING interactions or a globally enriched GO or KEGG term does not prove novelty; it mainly indicates that the module lacks strong support from those resources. The most defensible conclusion is that the cross-tissue co-abundance configuration is a candidate observation requiring replication, cell-composition controls, and independent perturbation or proteomic validation.

**Hypothesis.** Hypothesis: in both bone marrow and lung, a shared cellular population or shared physiological state coordinately increases mitochondrial and cytosolic metabolic activity, redox buffering, detoxification, lysosomal processing, and organelle protein maturation. FH-BLVRA could represent a metabolic-redox branch, GSTP1 could provide glutathione-dependent protection, and CTSA-PDF could represent lysosomal and mitochondrial proteostatic functions. C5orf22 may be a co-abundance connector or marker of that state rather than a proven molecular organizer. This hypothesis predicts that the module will track oxidative or proteostatic stress and particular cell mixtures more strongly than it tracks a single tissue-specific pathway.

### Important genes

#### C5orf22

- **Related proteins** (co-abundance neighbors): SMAP (0.87), GSTP1 (0.82), CTSA (0.82), FH (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Nuclear membrane; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromosome 5 open reading frame 22
- **Diseases (Open Targets)**: gout (0.281); neurodegenerative disease (0.263); non-autoimmune hemolytic anemia (0.095); Vertigo (0.091); actinic keratosis (0.057)
- **Europe PMC papers**: 70
- **Why important**: C5orf22 is the principal network connector, linking SMAP, GSTP1, CTSA, and FH. HPA places it at the nuclear membrane, with mast-cell and basophil-associated signals and detection in both tissues. It has disease associations reported for gout, neurodegenerative disease, and non-autoimmune hemolytic anemia, but its molecular annotation remains sparse.
- **Conclusion**: Established evidence supports C5orf22 as the topological connector and a tissue-detected, cell-associated marker in this module. Its molecular function and causal role are unresolved. A role as a coordinator of the module is a hypothesis based on network position, not an established function.

#### FH

- **Related proteins** (co-abundance neighbors): BLVRA (0.81), C5orf22 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fumarate hydratase. The protein encoded by this gene is an enzymatic component of the tricarboxylic acid (TCA) cycle, or Krebs cycle, and catalyzes the formation of L-malate from fumarate. It exists in both a cytosolic form and an N-terminal extended form, differing only in the translation start site used. The N-terminal extended form is targeted to the mitochondrion, where the removal of the extension generates the …
- **Diseases (Open Targets)**: hereditary leiomyomatosis and renal cell cancer (0.838); fumaric aciduria (0.820); hereditary neoplastic syndrome (0.580); Multiple cutaneous leiomyomas (0.575); neurodegenerative disease (0.482)
- **Europe PMC papers**: 42469
- **Why important**: FH is connected to the module connector and to BLVRA, forming the clearest metabolic branch. It encodes fumarate hydratase, an enzyme of the tricarboxylic acid cycle with mitochondrial and cytosolic forms, and its annotations include fumarate, malate, arginine, urea-cycle, and DNA-damage-related biology. It also has well-established disease associations involving fumaric aciduria and hereditary leiomyomatosis and renal cell cancer.
- **Conclusion**: The enzymatic role and disease relevance of FH are established. Within this module, its co-abundance may indicate mitochondrial or metabolic-state coupling with BLVRA and C5orf22, but the module does not establish that FH regulates the other genes.

#### GSTP1

- **Related proteins** (co-abundance neighbors): C5orf22 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_13103.1, huMAP3_12535.1
- **Function (MyGene.info)**: glutathione S-transferase pi 1. Glutathione S-transferases (GSTs) are a family of enzymes that play an important role in detoxification by catalyzing the conjugation of many hydrophobic and electrophilic compounds with reduced glutathione. Based on their biochemical, immunologic, and structural properties, the soluble GSTs are categorized into 4 main classes: alpha, mu, pi, and theta. This GST family member is a polymorphic gene…
- **Diseases (Open Targets)**: neurodegenerative disease (0.350); breast cancer (0.117); hepatocellular carcinoma (0.115); neoplasm (0.114); posterior cortical atrophy (0.113)
- **Europe PMC papers**: 12759
- **Why important**: GSTP1 provides a strong biochemical link to glutathione metabolism, xenobiotic detoxification, reactive-oxygen response, and inflammatory regulation. It is tissue-enhanced in esophagus and detected in lung, with cell-type enhancement in esophageal and respiratory epithelial populations. It is also the only gene besides SMAP represented in both hu.MAP complexes (hu.MAP huMAP3_13103.1) and (hu.MAP huMAP3_12535.1).
- **Conclusion**: GSTP1's detoxification and redox functions are established, as is its prior complex-level association with SMAP. Its participation in this cross-tissue module could reflect epithelial or oxidative-stress biology, but the supplied evidence does not show that GSTP1 physically connects the whole module.

#### CTSA

- **Related proteins** (co-abundance neighbors): PDF (0.86), C5orf22 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Vesicles; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cathepsin A. This gene encodes a member of the peptidase S10 family of serine carboxypeptidases. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate two chains that comprise the heterodimeric active enzyme. This enzyme possesses deamidase, esterase and carboxypeptidase activities and acts as a scaffold in the …
- **Diseases (Open Targets)**: galactosialidosis (0.842); cathepsin a-related arteriopathy-strokes-leukoencephalopathy (0.464); hereditary disease (0.451); lysosomal storage disease (0.373); Lynch syndrome (0.340)
- **Europe PMC papers**: 8422
- **Why important**: CTSA is connected to PDF and C5orf22 and encodes a serine carboxypeptidase with deamidase and esterase activities. It also acts as a scaffold in a lysosomal multienzyme complex and is annotated for proteolysis, intracellular protein transport, protein stability, and chaperone-mediated autophagy. HPA shows tissue enhancement in adrenal gland, cell-type enrichment in platelets, vesicular localization, and detection in both tissues. Its disease associations include galactosialidosis and related lysosomal disorders.
- **Conclusion**: CTSA's enzymatic, lysosomal, and disease biology are established. In the module, its branch with PDF may indicate coordinated proteostasis or organelle maintenance, but that interpretation remains a hypothesis because no STRING interaction or globally significant enrichment supports it.

#### BLVRA

- **Related proteins** (co-abundance neighbors): FH (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biliverdin reductase A. The protein encoded by this gene belongs to the biliverdin reductase family, members of which catalyze the conversion of biliverdin to bilirubin in the presence of NADPH or NADH. Mutations in this gene are associated with hyperbiliverdinemia. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Dec 2011].
- **Diseases (Open Targets)**: hyperbiliverdinemia (0.618); neurodegenerative disease (0.315); poisoning (0.255); response to xenobiotic stimulus (0.255); skin disorder (0.227)
- **Europe PMC papers**: 592
- **Why important**: BLVRA is connected to FH and supplies a complementary redox and heme-catabolism signal. It catalyzes conversion of biliverdin to bilirubin using NADPH or NADH and is annotated for heme catabolism and response to xenobiotic stimulus. HPA shows broad tissue detection and cell-type enhancement in several epithelial, placental, and macrophage-associated cell types. It also has a disease association with hyperbiliverdinemia.
- **Conclusion**: BLVRA's biochemical function and relation to heme catabolism are established. Its association with FH in this module is consistent with coordinated metabolic-redox activity, but whether that relationship reflects shared cell composition, common regulation, or direct biological coupling is unresolved.

## Module 12

**Tissue pair**: bone_marrow and lung  
**Genes (9)**: CASP8, COPS7A, LPCAT4, MOGS, PMS1, SACM1L, SEC22B, TIMM50, NAE1

### Function

This is a biologically heterogeneous module with no GO or KEGG term passing global multiple-testing correction. Therefore, the module should not be assigned a formally enriched pathway. Gene-level annotations nevertheless suggest several potentially related cellular processes: apoptotic and immune regulation through CASP8; endoplasmic-reticulum protein glycan processing through MOGS; vesicle trafficking through SEC22B; DNA mismatch repair through PMS1; mitochondrial protein import and apoptosis-related membrane integrity through TIMM50; membrane-lipid metabolism through LPCAT4 and SACM1L; and ubiquitin-like protein regulation through NAE1 and COPS7A. These annotations support a cautious interpretation centered on cellular stress, proteostasis, membrane trafficking, and cell-survival regulation rather than a single established pathway. The co-abundance pattern may reflect coordinated expression in a shared cellular context, but it does not by itself establish direct biochemical cooperation.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not strongly blood-cell specific, because every gene has low immune-cell specificity and there are no enriched blood-cell categories in the summary. Several genes have low tissue specificity, while tissue-enhanced signals occur in bone marrow, brain, and testis. Cell-type annotations are mixed, including neutrophils, innate lymphoid cells, NK-cells, cardiomyocytes, and several spermatogenic populations. Thus, the shared bone-marrow and lung module is more consistent with broadly expressed intracellular genes, with possible contributions from shared or variable cell populations, than with a coherent plasma-protein or blood-cell program. Protein detection is broader in lung than bone marrow, but this observation does not establish tissue-specific function.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional-enrichment result is reported. No STRING interaction among the module genes reaches the stated high-confidence threshold, and no hu.MAP complex contains at least two module members. The module edges are therefore not corroborated by the supplied high-confidence interaction or complex resources. This argues against interpreting the co-abundance edges as established physical interactions. It does not exclude lower-confidence, condition-dependent, indirect, or previously uncurated relationships. The gene annotations do provide plausible process-level connections, especially around apoptosis, endoplasmic-reticulum handling, trafficking, membrane biology, and mitochondrial function, but these remain complementary evidence rather than confirmation of a shared complex.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a novel co-abundance observation, but it cannot be called a newly discovered molecular pathway on the supplied evidence. Its novelty is supported by the absence of high-confidence STRING interactions, the absence of a shared hu.MAP complex, and the lack of a globally significant GO or KEGG term. However, absence from these resources alone does not prove novelty: the pattern could reflect indirect regulation, shared cell composition, tissue-sampling effects, or a weak and context-specific relationship. A defensible claim is that this particular cross-tissue co-abundance configuration is not explained by an already recognized high-confidence interaction module in the supplied databases and requires independent replication and perturbational testing.

**Hypothesis.** Hypothesis: the module reflects a coordinated cellular stress and survival state in which endoplasmic-reticulum glycan processing and vesicle traffic are coupled to membrane-lipid remodeling, ubiquitin-like regulation, mitochondrial import, DNA surveillance, and apoptotic signaling. In this model, MOGS and SEC22B represent secretory-pathway and trafficking functions, LPCAT4 and SACM1L represent membrane-lipid control, NAE1 and COPS7A represent regulation of protein modification, PMS1 represents genome-surveillance capacity, TIMM50 represents mitochondrial import and apoptotic susceptibility, and CASP8 represents a possible downstream or integrating death-signaling component. This is a mechanistic hypothesis, not an established pathway assignment; the sparse network, lack of database-supported interactions, and absence of globally significant enrichment make indirect co-regulation and cell-mixture effects important alternatives.

### Important genes

#### CASP8

- **Related proteins** (co-abundance neighbors): NAE1 (0.87), SACM1L (0.85), MOGS (0.85), COPS7A (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caspase 8. This gene encodes a member of the cysteine-aspartic acid protease (caspase) family. Sequential activation of caspases plays a central role in the execution-phase of cell apoptosis. Caspases exist as inactive proenzymes composed of a prodomain, a large protease subunit, and a small protease subunit. Activation of caspases requires proteolytic processing at conserved internal aspartic residues to ge…
- **Diseases (Open Targets)**: autoimmune lymphoproliferative syndrome type 2B (0.780); head and neck squamous cell carcinoma (0.612); neurodegenerative disease (0.543); viral infectious disease (0.508); autoimmune lymphoproliferative syndrome (0.477)
- **Europe PMC papers**: 40495
- **Why important**: CASP8 has the most central position in the module subgraph and connects to NAE1, SACM1L, MOGS, and COPS7A. Its annotated roles in apoptotic processing, cytokine regulation, immune-system regulation, proteolysis, and angiogenesis make it the strongest candidate for an integrative survival or inflammatory signal. It also has extensive literature coverage and disease associations involving autoimmune lymphoproliferative disease, cancer, neurodegeneration, and viral infection. HPA data show expression in bone marrow and lung and enhancement in several immune-related cell types, although the blood-cell specificity is low.
- **Conclusion**: Established evidence supports CASP8 as an apoptosis and immune-regulation gene and as the most connected member of this module. It is a plausible network anchor, but the module does not establish that CASP8 directly regulates the other members or that apoptosis is the module's primary function.

#### MOGS

- **Related proteins** (co-abundance neighbors): LPCAT4 (0.89), CASP8 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosyl-oligosaccharide glucosidase. This gene encodes the first enzyme in the N-linked oligosaccharide processing pathway. The enzyme cleaves the distal alpha-1,2-linked glucose residue from the Glc(3)-Man(9)-GlcNAc(2) oligosaccharide precursor. This protein is located in the lumen of the endoplasmic reticulum. Defects in this gene are a cause of type IIb congenital disorder of glycosylation (CDGIIb). Two transcript variants encodin…
- **Diseases (Open Targets)**: MOGS-congenital disorder of glycosylation (0.818); congenital disorder of glycosylation (0.374); congenital disorder of glycosylation type II (0.370); severe acute respiratory syndrome (0.370); SRD5A3-congenital disorder of glycosylation (0.370)
- **Europe PMC papers**: 987
- **Why important**: MOGS connects the central CASP8-linked portion of the module with LPCAT4 and is localized to the endoplasmic reticulum. Its established function in the first step of N-linked oligosaccharide processing links the module to protein maturation and endoplasmic-reticulum proteostasis. It has a disease association with congenital disorder of glycosylation and substantial literature coverage. HPA detects the protein in both relevant tissues, while its cell-type annotation is enriched in late spermatids rather than immune cells.
- **Conclusion**: Established evidence supports MOGS as an endoplasmic-reticulum glycan-processing enzyme with disease relevance. Its co-abundance with trafficking, lipid, and apoptotic genes suggests a possible proteostasis connection, but a direct role in a shared module mechanism remains hypothetical.

#### SEC22B

- **Related proteins** (co-abundance neighbors): LPCAT4 (0.90), PMS1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC22 homolog B, vesicle trafficking protein. The protein encoded by this gene is a member of the SEC22 family of vesicle trafficking proteins. It seems to complex with SNARE and it is thought to play a role in the ER-Golgi protein trafficking. This protein has strong similarity to Mus musculus and Cricetulus griseus proteins.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: inflammatory bowel disease (0.285); luminal A breast carcinoma (0.271); colitis (0.238); enteritis (0.238); Crohn disease (0.233)
- **Europe PMC papers**: 1006
- **Why important**: SEC22B links LPCAT4 with PMS1 and is annotated as an ER-to-Golgi and Golgi-to-ER vesicle-trafficking protein involved in vesicle fusion and macroautophagy. It provides a plausible trafficking bridge between membrane metabolism and other module processes. It has disease associations involving inflammatory bowel disease and related inflammatory conditions, and its HPA cell-type annotation is enhanced in neutrophils, although overall immune-cell specificity is low.
- **Conclusion**: Established evidence supports SEC22B in vesicle trafficking and autophagy-related transport. Its position may indicate coordination between membrane handling and cellular stress responses, but neither the network nor the databases demonstrate a direct SEC22B interaction with the other module genes.

#### PMS1

- **Related proteins** (co-abundance neighbors): SEC22B (0.84), TIMM50 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PMS1 homolog 1, mismatch repair system component. This gene encodes a protein belonging to the DNA mismatch repair mutL/hexB family. This protein is thought to be involved in the repair of DNA mismatches, and it can form heterodimers with MLH1, a known DNA mismatch repair protein. Mutations in this gene cause hereditary nonpolyposis colorectal cancer type 3 (HNPCC3) either alone or in combination with mutations in other genes involved in the HNPC…
- **Diseases (Open Targets)**: Lynch syndrome (0.369); colorectal cancer (0.338); ovarian cancer (0.338); hepatocellular carcinoma (0.192); oral cavity squamous cell carcinoma (0.189)
- **Europe PMC papers**: 3550
- **Why important**: PMS1 connects SEC22B with TIMM50 and is an established mismatch-repair component that can form heterodimers with MLH1. Its disease associations include Lynch syndrome and several cancers, and it has substantial literature coverage. HPA shows tissue enhancement in testis and cell-type enhancement across spermatogenic populations, which contributes to the mixed composition of the module rather than supporting a specific immune interpretation.
- **Conclusion**: Established evidence supports PMS1 in DNA mismatch repair and cancer predisposition. Its inclusion could reflect a broader stress, proliferation, or cell-state program, but linking DNA repair to vesicle trafficking or mitochondrial import in this module is a hypothesis requiring experimental validation.

#### TIMM50

- **Related proteins** (co-abundance neighbors): PMS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translocase of inner mitochondrial membrane 50. This gene encodes a subunit of the TIM23 inner mitochondrial membrane translocase complex. The encoded protein functions as the receptor subunit that recognizes the mitochondrial targeting signal, or presequence, on protein cargo that is destined for the mitochondrial inner membrane and matrix. This protein may also play a role in maintaining the membrane permeability barrier, and knockdown of thi…
- **Diseases (Open Targets)**: 3-methylglutaconic aciduria type 9 (0.773); neurodegenerative disease (0.519); Mitochondrial encephalopathy (0.425); hereditary disease (0.415); Epileptic encephalopathy (0.370)
- **Europe PMC papers**: 442
- **Why important**: TIMM50 connects PMS1 to mitochondrial biology and is a receptor component of the TIM23 inner-membrane translocase. Its annotations include mitochondrial protein import, membrane organization, and cytochrome-c release after loss of function, making it relevant to mitochondrial stress and apoptosis. It has disease associations involving mitochondrial and neurodevelopmental disorders. HPA detects it in both tissues and reports enrichment in late spermatids.
- **Conclusion**: Established evidence supports TIMM50 as a mitochondrial import and apoptosis-related gene. Its placement next to PMS1 suggests a possible link between cellular stress surveillance and mitochondrial fate, but the module does not establish that this link is causal or specific to bone marrow and lung.

## Module 13

**Tissue pair**: bone_marrow and lung  
**Genes (6)**: CHURC1, GPS1, HSP90AA1, NIP7, RPL9, MARS1

### Function

The module does not have a uniquely supported pathway annotation: no GO or KEGG term passed global correction, and there are no supplementary STRING functional-enrichment terms. Its network structure is centered on CHURC1, which connects to NIP7, GPS1, MARS1, HSP90AA1, and the RPL9-related signal. The gene annotations suggest a combination of nucleolar and ribosome-related processes, translation, protein folding, protein neddylation regulation, and transcriptional regulation. These annotations should be treated as biological context rather than demonstrated module enrichment. The strongest direct network evidence is the co-abundance hub role of CHURC1 and the known STRING relationship between NIP7 and RPL9. Overall, the module is most consistent with a broadly expressed cellular maintenance and protein-biosynthesis program, but its precise function remains unresolved.

**Cell composition.** All module genes have low tissue specificity in HPA, and all have low immune-cell specificity. None is secreted. The module therefore is not a plasma-protein module and is not specifically blood-cell enriched according to the supplied HPA summary. Protein detection is broadly concordant between bone marrow and lung for most genes, although HPA reports missing or negative observations for some genes. The cell-type-enhanced annotations are heterogeneous, spanning epithelial, hepatic, germ-cell, cardiac, and neutrophil-related cell types rather than identifying a shared cell population. This favors a broadly expressed intracellular program or a shared technical or cellular-composition signal over a tissue-specific secretory program. The absence of a blood-cell-specific signature does not exclude contribution from shared cell types in the samples.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports one high-confidence pair within the module, NIP7 with RPL9. CHURC1 has strong co-abundance connections to the other module members, but the fact sheet reports no STRING partners for CHURC1 and no STRING interaction for the other CHURC1-linked pairs. No hu.MAP complex contains at least two module members. Thus, the module is not independently validated as a known multiprotein complex. The NIP7-RPL9 relationship is compatible with a link between ribosome biogenesis and the large ribosomal subunit, while the remaining co-abundance edges may reflect shared expression, indirect regulation, or cellular state rather than physical binding.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: NIP7–RPL9 (0.877)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may be a new co-abundance observation, but the available evidence is insufficient to call it a newly discovered biological mechanism. Its novelty is supported mainly by the lack of a matching hu.MAP complex, the sparse STRING connectivity, and the absence of globally significant GO or KEGG enrichment. Those absences do not prove novelty, because known biology can be missed by incomplete interaction databases, tissue-specific regulation, modest module size, or heterogeneous cell composition. The module should therefore be described as a potentially novel cross-tissue co-abundance pattern requiring independent validation, rather than as a novel pathway or complex.

**Hypothesis.** Hypothesis: the shared bone-marrow and lung signal represents a broadly expressed intracellular maintenance state in which ribosome assembly and translation capacity are coordinated with protein folding, proteostasis, and regulation of signaling-related protein modification. CHURC1 may act as the expression-level hub linking these processes, while the NIP7-RPL9 relationship provides a specific ribosome-related component. MARS1 could reflect translational demand, HSP90AA1 could reflect chaperone and stress-response capacity, and GPS1 could connect the state to neddylation and signal-transduction control. This is a mechanistic hypothesis, not an experimentally established interaction model.

### Important genes

#### CHURC1

- **Related proteins** (co-abundance neighbors): NIP7 (0.94), GPS1 (0.86), RPL9; RPL9P7; RPL9P8; RPL9P9 (0.83), MARS1 (0.81), HSP90AA1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: churchill domain containing 1. Predicted to enable zinc ion binding activity. Predicted to be involved in positive regulation of transcription, DNA-templated. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: lung adenocarcinoma (0.075); neoplasm (0.059); alcohol drinking (0.023); stroke disorder (0.023); placental abruption (0.022)
- **Europe PMC papers**: 210
- **Why important**: CHURC1 is the central co-abundance hub, connecting every other module member in the supplied subgraph. Its annotation includes predicted zinc-ion binding and positive regulation of DNA-templated transcription, while its HPA profile is broadly expressed and intracellular. It has substantially less literature than HSP90AA1 or RPL9, so its hub position is especially important for interpreting the module and for testing whether the pattern reflects a regulatory rather than merely translational state.
- **Conclusion**: Established evidence supports CHURC1 as the network hub and as a broadly expressed cytosolic protein with predicted transcription-related functions. It is not established that CHURC1 mechanistically organizes the other genes; its possible role as a coordinator of the module is a hypothesis requiring perturbation or independent datasets.

#### NIP7

- **Related proteins** (co-abundance neighbors): CHURC1 (0.94); STRING partners: RPL9 (0.877)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleolar pre-rRNA processing protein NIP7. Enables RNA binding activity. Predicted to be involved in ribosomal large subunit biogenesis. Located in cytosol; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.471); COG8-congenital disorder of glycosylation (0.118); liposarcoma (0.035); arthropathy (0.023); chronic obstructive pulmonary disease (0.021)
- **Europe PMC papers**: 392
- **Why important**: NIP7 is annotated as an RNA-binding nucleolar pre-rRNA-processing protein involved in ribosomal large-subunit biogenesis. It forms the module's only reported high-confidence STRING relationship, with RPL9, and its disease associations include a congenital disorder of glycosylation and neurodegenerative disease. Although it has only one co-abundance neighbor, that neighbor is biologically informative.
- **Conclusion**: Established evidence supports NIP7 as a ribosome-biogenesis factor and supports a known relationship with RPL9. The conclusion that ribosome assembly is a core driver of the whole module remains provisional because no GO or KEGG term passed global correction.

#### RPL9

- **Related proteins** (co-abundance neighbors): none; STRING partners: NIP7 (0.877)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein L9. Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L6P family of ribosomal proteins. It is located in the cytoplasm. As is t…
- **Diseases (Open Targets)**: lipoic acid synthetase deficiency (0.565); Diamond-Blackfan anemia (0.538); Duchenne muscular dystrophy (0.503); Orthomyxoviridae infectious disease (0.462); hereditary disease (0.413)
- **Europe PMC papers**: 1508
- **Why important**: RPL9 encodes a large-subunit ribosomal protein and is annotated in translation-related processes. It is linked to NIP7 by the only reported high-confidence STRING interaction and has disease associations including Diamond-Blackfan anemia and lipoic acid synthetase deficiency. Its high literature volume reflects an established role in ribosome biology, even though it has no additional module edge in the supplied subgraph.
- **Conclusion**: Established evidence supports RPL9 as a structural or functional component of the large ribosomal subunit and supports its relationship with NIP7. Its presence does not establish that the entire module is a ribosomal complex, particularly because hu.MAP reports no shared complex.

#### MARS1

- **Related proteins** (co-abundance neighbors): CHURC1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionyl-tRNA synthetase 1. This gene encodes a member of the class I family of aminoacyl-tRNA synthetases. These enzymes play a critical role in protein biosynthesis by charging tRNAs with their cognate amino acids. The encoded protein is a component of the multi-tRNA synthetase complex and catalyzes the ligation of methionine to tRNA molecules. [provided by RefSeq, Jan 2011].
- **Diseases (Open Targets)**: severe early-onset pulmonary alveolar proteinosis due to MARS deficiency (0.745); Charcot-Marie-Tooth disease axonal type 2U (0.676); autosomal recessive spastic paraplegia type 70 (0.614); trichothiodystrophy 9, nonphotosensitive (0.428); pulmonary alveolar proteinosis (0.338)
- **Europe PMC papers**: 435
- **Why important**: MARS1 encodes methionyl-tRNA synthetase, an enzyme required for charging tRNA with methionine and for protein biosynthesis. It is connected to the CHURC1 hub and has strong disease associations involving pulmonary alveolar proteinosis and several inherited disorders. Its HPA annotation includes enhancement in neutrophils, although the module as a whole has low immune-cell specificity.
- **Conclusion**: Established evidence supports MARS1 as a translation-related enzyme with clinically important loss-of-function associations. Its co-abundance with CHURC1 may indicate coordinated protein-production capacity, but a direct regulatory connection between the genes is not established.

#### HSP90AA1

- **Related proteins** (co-abundance neighbors): CHURC1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein 90 alpha family class A member 1. The protein encoded by this gene is an inducible molecular chaperone that functions as a homodimer. The encoded protein aids in the proper folding of specific target proteins by use of an ATPase activity that is modulated by co-chaperones. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: cancer (0.643); plasma cell myeloma (0.404); non-small cell lung carcinoma (0.394); dengue disease (0.375); Orthomyxoviridae infectious disease (0.375)
- **Europe PMC papers**: 8215
- **Why important**: HSP90AA1 is a well-studied inducible molecular chaperone that supports folding of client proteins through ATP-dependent activity and co-chaperone regulation. It is connected to CHURC1 and has extensive literature and disease associations involving cancer, myeloma, lung carcinoma, and infectious disease. HPA reports low tissue specificity and no detected protein in the listed bone-marrow and lung observations, which cautions against treating its transcript co-abundance as proof of local protein activity.
- **Conclusion**: Established evidence supports HSP90AA1 as a proteostasis and chaperone factor. Its inclusion is compatible with a cellular stress or protein-quality-control interpretation, but the module data do not establish that HSP90AA1 drives the shared tissue pattern.

#### GPS1

- **Related proteins** (co-abundance neighbors): CHURC1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein pathway suppressor 1. This gene is known to suppress G-protein and mitogen-activated signal transduction in mammalian cells. The encoded protein shares significant similarity with Arabidopsis FUS6, which is a regulator of light-mediated signal transduction in plant cells. [provided by RefSeq, Mar 2016].
- **Diseases (Open Targets)**: breast cancer (0.078); breast carcinoma (0.078); esophageal squamous cell carcinoma (0.049); esophageal adenocarcinoma (0.021); cancer (0.020)
- **Europe PMC papers**: 436
- **Why important**: GPS1 is connected to CHURC1 and is annotated as a suppressor of G-protein and mitogen-activated signaling, with roles related to protein neddylation, deneddylation, protein stabilization, and the JNK cascade. It has disease associations involving breast and esophageal cancers. Its position as a peripheral module member makes it useful for evaluating whether the pattern extends beyond translation and proteostasis into signaling control.
- **Conclusion**: Established evidence supports GPS1 as a regulator associated with signal transduction and neddylation-related processes. Its participation in this module may indicate coordinated signaling-state control, but that interpretation is a hypothesis because there is no direct STRING or complex evidence connecting GPS1 to the other members.

## Module 14

**Tissue pair**: bone_marrow and lung  
**Genes (5)**: COQ8A, DNAJC10, FMNL1, HK3, MIA3

### Function

No GO or KEGG term passed global correction, and there is no supplementary STRING enrichment. Therefore, the module does not support a statistically established single pathway or biological process. Its gene annotations suggest several distinct functions: glucose phosphorylation and metabolic support through HK3; mitochondrial ubiquinone biology through COQ8A; endoplasmic-reticulum protein quality control through DNAJC10; actin organization and cell migration through FMNL1; and ER cargo export, secretion, and leukocyte migration through MIA3. The sparse co-abundance structure connects these functions but does not establish that they form one physical pathway. The most cautious interpretation is a shared cellular-state or cell-composition module with metabolic, proteostasis, trafficking, and migratory components.

**Cell composition.** The module is not dominated by secreted or plasma proteins: none of the genes has secretome annotation. HPA evidence shows heterogeneous tissue specificity rather than a uniform tissue program. HK3 and FMNL1 are enriched in bone marrow and lymphoid tissue, while COQ8A is associated with skeletal muscle and tongue, DNAJC10 with epididymis, and MIA3 has low tissue specificity. Neutrophils are the clearest cell-type association, but most genes have low immune-cell specificity, so this is not a uniformly blood-cell-enriched module. Protein detection is present for most genes in both bone marrow and lung, with MIA3 detected in bone marrow but not lung. The shared signal could therefore reflect a mixture of hematopoietic or myeloid representation and broader conserved cellular processes, rather than a lung-specific or bone-marrow-specific secretory program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

At the supplied STRING confidence threshold, none of the possible within-module gene pairs has a reported interaction. No hu.MAP complex contains multiple module members. Thus, the observed edges are co-abundance relationships rather than previously supported protein-protein interactions or membership in a known multiprotein complex. The network has a central-looking connection pattern around HK3, DNAJC10, and COQ8A, with FMNL1 attached to HK3 and MIA3 attached to COQ8A, but the lack of STRING and hu.MAP support argues against treating this topology as a validated molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module-level co-abundance pattern may be a new cross-tissue observation because its particular combination of genes has no corresponding high-confidence STRING relationship or shared hu.MAP complex in the supplied evidence. However, that absence alone does not establish novelty: the genes have established individual functions, and co-abundance can arise from cell composition, expression state, or technical and biological covariance. The defensible conclusion is that the cross-tissue module association is potentially novel and hypothesis-generating, while a new molecular mechanism has not been demonstrated.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular state in which metabolically active and migratory hematopoietic or myeloid-associated cells coordinate glucose utilization through HK3 with mitochondrial coenzyme-Q biology through COQ8A, while DNAJC10 and MIA3 support ER proteostasis and cargo export, and FMNL1 supports actin remodeling and migration. A related possibility is that shared cell-type composition across bone marrow and lung drives part of the covariance. This hypothesis predicts that the module should vary with the abundance or activation state of neutrophil or related myeloid populations and should show coordinated relationships among glycolytic activity, ER stress or secretion, mitochondrial function, and migration. These predictions are not established by the current data.

### Important genes

#### HK3

- **Related proteins** (co-abundance neighbors): FMNL1 (0.95), DNAJC10 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hexokinase 3. Hexokinases phosphorylate glucose to produce glucose-6-phosphate, the first step in most glucose metabolism pathways. This gene encodes hexokinase 3. Similar to hexokinases 1 and 2, this allosteric enzyme is inhibited by its product glucose-6-phosphate. [provided by RefSeq, Apr 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.217); myeloproliferative disorder (0.122); neoplasm (0.111); glioblastoma (0.099); nonpapillary renal cell carcinoma (0.095)
- **Europe PMC papers**: 11024
- **Why important**: HK3 has a central position in the co-abundance subgraph, linking FMNL1 and DNAJC10. Its established function is glucose phosphorylation at the entry point of glycolysis and related glucose metabolism. HPA associates it with bone marrow, lymphoid tissue, monocyte progenitors, macrophages, Kupffer cells, and basophils, making it a plausible contributor to the hematopoietic or myeloid aspect of the module. It also has by far the largest literature volume among these genes and disease associations spanning neurodegenerative disease, myeloproliferative disorder, and neoplasm.
- **Conclusion**: Established evidence supports HK3 as a metabolic gene with relevant bone-marrow and myeloid-associated expression. Its network position makes it a plausible organizing marker of the module, but the data do not establish that HK3 mechanistically drives the other genes or that the module is a glycolysis pathway.

#### DNAJC10

- **Related proteins** (co-abundance neighbors): COQ8A (0.85), HK3 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DnaJ heat shock protein family (Hsp40) member C10. This gene encodes an endoplasmic reticulum co-chaperone which is part of the endoplasmic reticulum-associated degradation complex involved in recognizing and degrading misfolded proteins. The encoded protein reduces incorrect disulfide bonds in misfolded glycoproteins. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Oct 20…
- **Diseases (Open Targets)**: dengue disease (0.370); dry eye syndrome (0.321); type 2 diabetes mellitus (0.317); neurodegenerative disease (0.307); response to antihypertensive drug (0.294)
- **Europe PMC papers**: 547
- **Why important**: DNAJC10 occupies a bridging position between HK3 and COQ8A. It is an ER co-chaperone involved in recognizing misfolded proteins, reducing incorrect disulfide bonds, ER-associated degradation, and the unfolded-protein response. It is detected in both bone marrow and lung, although its tissue annotation is mainly associated with epididymis and its immune-cell specificity is low. Its placement between metabolic and mitochondrial-associated genes makes it important for evaluating a possible cellular-stress interpretation.
- **Conclusion**: Established evidence supports DNAJC10 as an ER proteostasis factor. Its connection in this module is consistent with a shared stress or biosynthetic state, but ER stress is a hypothesis rather than an enrichment result or demonstrated causal process here.

#### COQ8A

- **Related proteins** (co-abundance neighbors): DNAJC10 (0.85), MIA3 (0.84); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coenzyme Q8A. This gene encodes a mitochondrial protein similar to yeast ABC1, which functions in an electron-transferring membrane protein complex in the respiratory chain. It is not related to the family of ABC transporter proteins. Expression of this gene is induced by the tumor suppressor p53 and in response to DNA damage, and inhibiting its expression partially suppresses p53-induced apoptosis. Alternative…
- **Diseases (Open Targets)**: autosomal recessive ataxia due to ubiquinone deficiency (0.841); coenzyme Q10 deficiency (0.636); coenzyme Q10 deficiency, primary, 1 (0.461); hereditary disease (0.401); Abnormality of the skeletal system (0.366)
- **Europe PMC papers**: 397
- **Why important**: COQ8A links DNAJC10 and MIA3 and is annotated to mitochondria. It is involved in ubiquinone biosynthesis and phosphorylation-related functions, providing the clearest mitochondrial and respiratory-chain-related component of the module. Its disease associations include autosomal-recessive ataxia due to ubiquinone deficiency and primary coenzyme-Q deficiency. HPA shows association with skeletal muscle and neural cell types rather than strong immune specificity, which emphasizes the heterogeneous composition of the module.
- **Conclusion**: Established evidence supports COQ8A as a mitochondrial ubiquinone-biology gene with important inherited-disease relevance. Its module association may indicate a conserved energetic component, but it does not demonstrate a direct physical or functional partnership with DNAJC10 or MIA3.

#### FMNL1

- **Related proteins** (co-abundance neighbors): HK3 (0.95); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: formin like 1. This gene encodes a formin-related protein. Formin-related proteins have been implicated in morphogenesis, cytokinesis, and cell polarity. An alternative splice variant has been described but its full length sequence has not been determined. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); ovarian carcinoma (0.283); alcohol drinking (0.226); seasonal allergic rhinitis (0.226); neoplasm (0.106)
- **Europe PMC papers**: 554
- **Why important**: FMNL1 is the module's connection to bone marrow and lymphoid tissue and is the gene most specifically associated with neutrophils in the supplied HPA evidence. Its established functions include actin cytoskeleton organization, cell migration, cell morphogenesis, and actin filament severing. Although it has only one module neighbor, that neighbor is HK3, connecting cellular movement to the module's metabolic component. Its literature and disease associations provide additional support for biological relevance.
- **Conclusion**: Established evidence supports FMNL1 as a cytoskeletal and migratory factor with hematopoietic relevance. It is a strong marker candidate for the cell-composition or migration interpretation, but the current data do not prove that FMNL1-mediated migration causes the observed cross-tissue co-abundance.

#### MIA3

- **Related proteins** (co-abundance neighbors): COQ8A (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MIA SH3 domain ER export factor 3. Enables cargo receptor activity. Involved in several processes, including COPII-coated vesicle cargo loading; cell migration involved in sprouting angiogenesis; and regulation of leukocyte migration. Located in endoplasmic reticulum exit site and endoplasmic reticulum membrane. Is integral component of membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: coronary artery disorder (0.503); myocardial infarction (0.481); odontochondrodysplasia 2 with hearing loss and diabetes (0.471); coronary atherosclerosis (0.464); angina pectoris (0.439)
- **Europe PMC papers**: 604
- **Why important**: MIA3 connects to COQ8A and supplies a trafficking and secretion-related axis. It is an ER-exit-site and membrane protein that functions as a cargo receptor in COPII-coated vesicle loading and is involved in protein secretion, exocytosis, sprouting angiogenesis, and leukocyte migration. It is detected in bone marrow but not lung in the supplied immunohistochemistry summary, so it may also contribute to tissue-specific variation within the shared module. Its disease associations include coronary and vascular disorders and a syndromic developmental disorder.
- **Conclusion**: Established evidence supports MIA3 as an ER export and cargo-trafficking factor with links to leukocyte migration and vascular biology. Its module relationship with COQ8A may reflect coordinated biosynthetic or trafficking state, but no direct interaction or shared complex is supported.

## Module 15

**Tissue pair**: bone_marrow and lung  
**Genes (12)**: DCTN1, DYNC1H1, GANAB, HYOU1, IQGAP1, LMNB1, NSF, PDCD6IP, PDIA4, SDHA, SEPTIN9, USO1

### Function

The strongest interpretation is a conserved intracellular membrane-trafficking, endomembrane-organization, and cytoskeleton–nucleus positioning module. The primary evidence is endomembrane system organization (GO:BP endomembrane system organization; q_global = 0.0241), nuclear migration (GO:BP nuclear migration; q_global = 0.0243), nucleus localization (GO:BP nucleus localization; q_global = 0.0349), and the KEGG vasopressin-regulated water-reabsorption term (KEGG Vasopressin-regulated water reabsorption - Homo sapiens (human); q_global = 0.0123). The latter should be interpreted cautiously: the shared genes are DCTN1, DYNC1H1, and NSF, which are general transport and vesicle-machinery components rather than evidence that this module specifically performs renal water reabsorption. DCTN1 and DYNC1H1 support dynein–dynactin-dependent intracellular transport and nuclear movement; LMNB1 links this process to the nuclear envelope; and NSF, USO1, PDCD6IP, IQGAP1, GANAB, PDIA4, and HYOU1 connect vesicle traffic, membrane organization, protein folding, and cellular stress handling. No GO/KEGG term was significant within the module before correction across all module-term tests, so the globally significant GO/KEGG terms, rather than nominal or within-module values, provide the primary enrichment evidence.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. The HPA summary identifies a minority of secreted genes, while the listed proteins are mainly intracellular, membrane-associated, cytoskeletal, nuclear-envelope, ER, Golgi, mitochondrial, or vesicular proteins. Most genes have low tissue specificity, and all have cell-type-enhanced annotations, with signals distributed across neuronal, muscle, reproductive, plasma-cell, and marrow-related cell types. The module has low immune-cell specificity and no enriched blood-cell category in the HPA summary, so a simple blood-cell contamination explanation is not supported by this evidence. Protein detection in both bone marrow and lung is broad, except for HYOU1, which was not detected in either tissue by the stated HPA assay. The shared signal may therefore reflect conserved cellular machinery or shared cell populations rather than a tissue-specific secreted or blood-cell program.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Vasopressin-regulated water reabsorption - Homo sapiens (human) | 0.0123 | DCTN1, DYNC1H1, NSF |
| GO:BP endomembrane system organization | 0.0241 | DCTN1, IQGAP1, LMNB1, NSF, PDCD6IP, USO1 |
| GO:BP nuclear migration | 0.0243 | DCTN1, DYNC1H1, LMNB1 |
| GO:BP nucleus localization | 0.0349 | DCTN1, DYNC1H1, LMNB1 |

### STRING and hu.MAP

STRING provides a coherent but incomplete physical or functional backbone. The DCTN1–DYNC1H1 relationship is very strongly supported and corresponds to the known dynein–dynactin transport machinery. The GANAB–HYOU1, GANAB–PDIA4, and HYOU1–PDIA4 relationships support an ER protein-folding and quality-control submodule. NSF–USO1 supports vesicle fusion and ER-to-Golgi transport. STRING supplementary enrichment also repeatedly points to vasopressin-regulated water reabsorption, N-linked glycosylation, COPI-related transport, and liver-associated expression, but these are supplementary findings and are not global module-level significance claims. hu.MAP identifies two related complexes, (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), both containing PDIA4, GANAB, and HYOU1. Their shared membership supports an ER or secretory-pathway complex component, although only a subset of each large complex is present in this module. The remaining module relationships are not represented by the supplied high-confidence STRING edges or hu.MAP complexes, indicating that the co-abundance network extends beyond currently catalogued physical complexes.

**STRING interactions (score >= 0.7)**: 5 of 66 gene pairs: DCTN1–DYNC1H1 (0.999); GANAB–HYOU1 (0.83); GANAB–PDIA4 (0.717); HYOU1–PDIA4 (0.997); NSF–USO1 (0.832)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Liver (FDR = 4.79e-05, 12 genes); KEGG Vasopressin-regulated water reabsorption (FDR = 0.0041, 3 genes); WikiPathways Vasopressin-regulated water reabsorption (FDR = 0.008, 3 genes); RCTM Asparagine N-linked glycosylation (FDR = 0.0152, 5 genes); RCTM COPI-mediated anterograde transport (FDR = 0.0152, 4 genes); TISSUES Testis (FDR = 0.0492, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (PDIA4, GANAB, HYOU1; 3/60); huMAP3_09327.1 (PDIA4, GANAB, HYOU1; 3/93)

### Novelty

The module appears biologically interpretable but cannot be declared a wholly new molecular complex or pathway. Several components and relationships are established: DCTN1 with DYNC1H1, PDIA4 with GANAB and HYOU1, and NSF with USO1 are supported by STRING, while PDIA4, GANAB, and HYOU1 recur in hu.MAP complexes. The likely novelty is instead the tissue-pair-specific co-abundance organization of these transport, ER-quality-control, cytoskeletal, and nuclear-envelope genes across bone marrow and lung, together with the particular combination of genes not captured by the supplied known-interaction resources. Absence of other edges from STRING or hu.MAP is not evidence of novel biology by itself. Establishing novelty would require comparison with published co-expression modules, tissue-specific datasets, and independent replication.

**Hypothesis.** Hypothesis: in both bone marrow and lung, coordinated demand for intracellular transport and protein processing links ER-to-Golgi trafficking with cytoskeletal movement and nuclear positioning. The PDIA4–GANAB–HYOU1 group may support folding and quality control of proteins entering the secretory pathway; USO1 and NSF may support vesicle transport and fusion; and the DCTN1–DYNC1H1–LMNB1 axis may couple organelle movement to nuclear-envelope positioning. PDCD6IP and IQGAP1 may connect membrane organization to cytoskeletal or vesicular remodeling. This is a mechanistic hypothesis generated from co-abundance and annotation evidence, not proof of direct physical interaction or causal regulation in either tissue.

### Important genes

#### DCTN1

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.88), PDCD6IP (0.81); STRING partners: DYNC1H1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynactin subunit 1. This gene encodes the largest subunit of dynactin, a macromolecular complex consisting of 10 subunits ranging in size from 22 to 150 kD. Dynactin binds to both microtubules and cytoplasmic dynein. Dynactin is involved in a diverse array of cellular functions, including ER-to-Golgi transport, the centripetal movement of lysosomes and endosomes, spindle formation, chromosome movement, nuclear positi…
- **Diseases (Open Targets)**: Perry syndrome (0.798); amyotrophic lateral sclerosis (0.764); neuronopathy, distal hereditary motor, type 7B (0.743); cancer (0.547); neurodegenerative disease (0.530)
- **Europe PMC papers**: 1985
- **Why important**: DCTN1 is a central network connector and has the broadest primary annotation coverage in the module, appearing in (KEGG Vasopressin-regulated water reabsorption - Homo sapiens (human); q_global = 0.0123), (GO:BP endomembrane system organization; q_global = 0.0241), (GO:BP nuclear migration; q_global = 0.0243), and (GO:BP nucleus localization; q_global = 0.0349). It is the largest dynactin subunit and supports dynein-linked organelle movement, ER-to-Golgi transport, nuclear positioning, and spindle functions. Its high-confidence STRING relationship with DYNC1H1 and substantial literature on neurodegenerative and motor-neuron disease make it a strong mechanistic anchor.
- **Conclusion**: Established: DCTN1 is a plausible core component of the transport and nuclear positioning signal. Hypothesis: its co-abundance may report coordinated dynein–dynactin activity in shared marrow and lung cell populations.

#### PDIA4

- **Related proteins** (co-abundance neighbors): GANAB (0.85), HYOU1 (0.85), SDHA (0.84), SEPTIN9 (0.81); STRING partners: GANAB (0.717), HYOU1 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 occupies a central position in the ER-associated branch, connecting GANAB, HYOU1, SDHA, and SEPTIN9. It is present in both hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), and STRING supports its relationships with GANAB and HYOU1. Its established role in disulfide exchange, protein folding, protein secretion, and immunoglobulin assembly is especially relevant to cells with secretory demands. It also has disease associations involving neurodegenerative disease and neoplasia, with substantial literature support.
- **Conclusion**: Established: PDIA4 is a supported ER protein-folding and secretory-pathway component. Hypothesis: it may coordinate ER quality control with the broader transport program represented by this module.

#### HYOU1

- **Related proteins** (co-abundance neighbors): PDIA4 (0.85), USO1 (0.81); STRING partners: GANAB (0.83), PDIA4 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 is part of the repeated PDIA4–GANAB hu.MAP complex signal and has a high-confidence STRING relationship with PDIA4 plus an additional relationship with GANAB. Its annotated functions include ER protein folding and secretion, response to hypoxia, ER stress, ischemia, and protection from apoptosis. Its cell-type annotations include plasma cells and other specialized cell types, although HPA did not detect its protein in either named tissue.
- **Conclusion**: Established: HYOU1 is a stress-responsive ER quality-control candidate within the module. Hypothesis: its transcript co-abundance may reflect episodic secretory or hypoxic stress rather than stable protein abundance in the two tissues.

#### PDCD6IP

- **Related proteins** (co-abundance neighbors): IQGAP1 (0.83), GANAB (0.83), NSF (0.83), DCTN1 (0.81), USO1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 6 interacting protein. This gene encodes a protein that functions within the ESCRT pathway in the abscission stage of cytokinesis, in intralumenal endosomal vesicle formation, and in enveloped virus budding. Studies using mouse cells have shown that overexpression of this protein can block apoptosis. In addition, the product of this gene binds to the product of the PDCD6 gene, a protein required for apoptosis, in a calc…
- **Diseases (Open Targets)**: HIV infectious disease (0.463); anthrax infection (0.462); alcohol drinking (0.388); autosomal recessive primary microcephaly (0.386); microcephaly 29, primary, autosomal recessive (0.383)
- **Europe PMC papers**: 1668
- **Why important**: PDCD6IP has the strongest network connectivity in the supplied subgraph and links IQGAP1, GANAB, NSF, DCTN1, and USO1. It is included in the primary endomembrane organization term (GO:BP endomembrane system organization; q_global = 0.0241) and is annotated in ESCRT-dependent abscission, intralumenal vesicle formation, and enveloped-virus budding. Its vesicular location and extensive literature make it a useful bridge between membrane remodeling and the transport machinery, even though no STRING partner or hu.MAP complex was supplied for it.
- **Conclusion**: Established: PDCD6IP is a highly connected endomembrane-associated module member. Hypothesis: it may help couple vesicle formation or membrane scission to the transport and ER-processing branches.

#### LMNB1

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lamin B1. This gene encodes one of the two B-type lamin proteins and is a component of the nuclear lamina. A duplication of this gene is associated with autosomal dominant adult-onset leukodystrophy (ADLD). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: microcephaly 26, primary, autosomal dominant (0.723); autosomal dominant primary microcephaly (0.675); adult-onset autosomal dominant demyelinating leukodystrophy (0.670); hereditary disease (0.488); Syndrome with microcephaly as major feature (0.487)
- **Europe PMC papers**: 3851
- **Why important**: LMNB1 provides the clearest nuclear-envelope link. It appears in (GO:BP endomembrane system organization; q_global = 0.0241), (GO:BP nuclear migration; q_global = 0.0243), and (GO:BP nucleus localization; q_global = 0.0349), is tissue-enhanced in bone marrow and lymphoid tissue, and is connected in the module to DYNC1H1. Its established functions include nuclear envelope organization, nuclear migration, heterochromatin formation, and protein localization to the nuclear envelope. Its disease associations include adult-onset demyelinating leukodystrophy and primary microcephaly.
- **Conclusion**: Established: LMNB1 supports the nuclear localization and migration interpretation of the module. Hypothesis: it may provide the structural endpoint through which microtubule-based transport is coordinated with nuclear positioning in the shared tissue context.

## Module 16

**Tissue pair**: bone_marrow and lung  
**Genes (16)**: DDX21, DHX9, DNM1L, GMPS, HNRNPR, EIF4G1, EIF5, NOP2, PSMA1, PSMD13, RSL1D1, SUPT16H, SRP68, SRP72, EPRS1, TRIM25

### Function

The strongest primary annotation is RNA binding (GO:MF RNA binding; q_global = 0.0107), supported by the broad participation of the module genes in RNA handling. The genes span RNA helicase activity, heterogeneous nuclear RNA processing, nucleolar ribosome biogenesis, translation initiation, aminoacyl-tRNA charging, signal-recognition-particle function, and transcription-coupled chromatin remodeling. The network therefore most plausibly represents a conserved RNA-centered gene-expression program, linking RNA processing and ribosome or translation functions with protein targeting and quality-control processes. STRING evidence supports RNA binding (STRING Function RNA binding; within-query FDR = 0.0007) and ribonucleoprotein-complex association (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.0026) (STRING Component Ribonucleoprotein complex; within-query FDR = 0.0085), while signal-recognition-particle involvement (STRING Keyword Signal recognition particle; within-query FDR = 0.0241) and ubiquitin-related annotations (STRING Keyword Isopeptide bond; within-query FDR = 0.0021) (STRING Keyword Ubl conjugation; within-query FDR = 0.0061) suggest connected translational and proteostasis processes. These STRING terms are supplementary rather than globally corrected enrichment evidence. The absence of additional globally significant GO or KEGG terms does not invalidate the module; it indicates that RNA binding is the sole term passing the specified global correction.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and most have low immune-cell specificity, which is more consistent with broadly expressed housekeeping or core gene-expression machinery than with a specialized bone-marrow or lung program. Protein detection is widespread in both tissues, supporting technical and biological observability in the shared tissues. Several genes show cell-type-enhanced patterns, including erythrocyte progenitors, neutrophils, microglia, epithelial cells, and spermatogenic cells, but these annotations are heterogeneous rather than evidence for a single dominant cell population. TRIM25 is the clearest immune-related exception because it is enhanced in neutrophils. Thus, shared cell types or blood contribution could influence the conserved signal, but the overall composition argues more strongly for broadly active intracellular machinery than for a plasma or blood-cell module.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF RNA binding | 0.0107 | DDX21, DHX9, EIF4G1, EIF5, EPRS1, HNRNPR, NOP2, RSL1D1, SRP68, SRP72, SUPT16H, TRIM25 |

### STRING and hu.MAP

STRING provides established high-confidence relationships within several coherent subgroups. DDX21 connects with DHX9, HNRNPR, NOP2, and RSL1D1, supporting a nucleolar and RNA-processing neighborhood. EIF4G1 and EIF5 form a translation-initiation relationship. EPRS1 and GMPS are linked, PSMA1 and PSMD13 form a proteasome relationship, and SRP68 with SRP72 forms the expected signal-recognition-particle pair. These known relationships explain much of the module’s internal structure and indicate that the module is not an entirely unconnected or artifactual gene set. hu.MAP independently places PSMA1 and PSMD13 in proteasome complexes (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1), although only a small portion of each large complex is represented in the module. No supplied hu.MAP complex links the RNA-processing, translation-initiation, SRP, and proteasome portions into one physical complex. The module is therefore better interpreted as a co-abundance network joining several established molecular subsystems than as a single canonical complex.

**STRING interactions (score >= 0.7)**: 10 of 120 gene pairs: DDX21–DHX9 (0.908); DDX21–HNRNPR (0.73); DDX21–NOP2 (0.761); DDX21–RSL1D1 (0.81); DHX9–HNRNPR (0.909); EIF4G1–EIF5 (0.99); EPRS1–GMPS (0.912); NOP2–RSL1D1 (0.982); PSMA1–PSMD13 (0.999); SRP68–SRP72 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function RNA binding (FDR = 0.0007, 13 genes); Keyword Isopeptide bond (FDR = 0.0021, 11 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 0.0026, 8 genes); Keyword Ubl conjugation (FDR = 0.0061, 11 genes); Component Ribonucleoprotein complex (FDR = 0.0085, 8 genes); Keyword Acetylation (FDR = 0.0127, 15 genes); Keyword RNA-binding (FDR = 0.0178, 7 genes); Keyword Signal recognition particle (FDR = 0.0241, 2 genes); Function Organic cyclic compound binding (FDR = 0.0264, 15 genes); Function Heterocyclic compound binding (FDR = 0.0264, 15 genes); TISSUES Liver (FDR = 0.0282, 12 genes); TISSUES Leukemia cell (FDR = 0.0282, 9 genes); TISSUES Endocrine gland (FDR = 0.0305, 16 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09656.1 (PSMA1, PSMD13; 2/64); huMAP3_13725.1 (PSMA1, PSMD13; 2/69)

### Novelty

The biological functions and several pairwise relationships are established rather than novel, as shown by the STRING links and the hu.MAP proteasome assignments. The potentially new observation is the conserved co-abundance organization of these otherwise partly separate RNA-processing, translation, SRP, chromatin, mitochondrial, and proteasome components across bone marrow and lung. However, absence from hu.MAP or STRING would not establish novelty, and the supplied resources do not test whether this exact tissue-shared co-abundance module has been reported previously. The most defensible conclusion is that the module may be a novel systems-level association or regulatory state, but it should not be claimed as a newly discovered molecular complex or entirely new pathway without comparison against published co-expression and tissue-network studies.

**Hypothesis.** Hypothesis: the module reflects a conserved intracellular gene-expression and proteostasis state shared by cells present in bone marrow and lung. Coordinated RNA binding and processing may support ribosome biogenesis, translation initiation, aminoacyl-tRNA charging, and cotranslational targeting through the SRP, while TRIM25-associated ubiquitin regulation and proteasome components help manage damaged or regulated proteins. DHX9, DDX21, HNRNPR, NOP2, and RSL1D1 could form an RNA-processing and nucleolar axis, EIF4G1 and EIF5 could connect that axis to translation initiation, and SRP68 with SRP72 could connect translation to membrane targeting. This is a mechanistic hypothesis generated from co-abundance and known annotations, not proof of direct physical interaction or causal regulation among all module members.

### Important genes

#### EIF4G1

- **Related proteins** (co-abundance neighbors): EIF5 (0.84), TRIM25 (0.83), RSL1D1 (0.82), DNM1L (0.81), SRP68 (0.81), GMPS (0.80); STRING partners: EIF5 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 has the strongest network centrality in the supplied subgraph and connects translation initiation with several otherwise distinct module neighborhoods, including EIF5, TRIM25, RSL1D1, DNM1L, SRP68, and GMPS. Its established role as the large EIF4F scaffold makes it a plausible integrator of mRNA recruitment and translational control. It has extensive literature coverage and disease associations involving neurodegenerative, infectious, and pregnancy-related conditions.
- **Conclusion**: Established evidence supports EIF4G1 as a translation-initiation scaffold and a central co-abundance hub (GO:MF RNA binding; q_global = 0.0107). It is a strong candidate for coordinating the module’s RNA-to-protein-expression signal. It is not established that EIF4G1 causally regulates the other module genes in these tissues; that role remains a hypothesis.

#### DHX9

- **Related proteins** (co-abundance neighbors): SUPT16H (0.85), EPRS1 (0.83), PSMD13 (0.83), HNRNPR (0.82), PSMA1 (0.81); STRING partners: DDX21 (0.908), HNRNPR (0.909)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is a highly connected module gene and is linked in STRING to DDX21 and HNRNPR, while its network neighbors also include SUPT16H, EPRS1, PSMD13, and PSMA1. Its established RNA and DNA-RNA helicase activity, nuclear and cytoplasmic localization, and roles in splicing, transcription, and interferon production place it at the interface of RNA metabolism, gene regulation, and innate responses. It has substantial literature coverage and disease associations involving developmental and neurodegenerative disorders.
- **Conclusion**: Established evidence supports DHX9 as a multifunctional RNA helicase and a plausible bridge between RNA processing and proteostasis-related portions of the module (GO:MF RNA binding; q_global = 0.0107) (STRING Function RNA binding; within-query FDR = 0.0007) (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.0026). Its position makes it an attractive mechanistic connector, but the tissue-shared co-abundance pattern does not by itself demonstrate that DHX9 drives the module.

#### DDX21

- **Related proteins** (co-abundance neighbors): NOP2 (0.82), RSL1D1 (0.82); STRING partners: DHX9 (0.908), HNRNPR (0.73), NOP2 (0.761), RSL1D1 (0.81)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 occupies a nucleolar and mitotic-chromosome location and has STRING relationships with DHX9, HNRNPR, NOP2, and RSL1D1. Its known helicase-associated functions in RNA structural remodeling, ribosome and spliceosome-related processes, transcription, chromatin remodeling, and myeloid dendritic-cell cytokine production make it a biologically informative link between RNA biogenesis and cell-state regulation. It has extensive literature coverage and disease associations involving cancer and neurodegeneration.
- **Conclusion**: Established evidence supports DDX21 as part of the module’s RNA-processing and nucleolar axis (GO:MF RNA binding; q_global = 0.0107) (STRING Function RNA binding; within-query FDR = 0.0007) (STRING Keyword RNA-binding; within-query FDR = 0.0178). Its network links are consistent with a coordinated RNA-biogenesis subsystem. Whether DDX21 explains conservation between bone marrow and lung, or merely follows a broadly expressed housekeeping program, remains unresolved.

#### SRP68

- **Related proteins** (co-abundance neighbors): EIF4G1 (0.81), SRP72 (0.80); STRING partners: SRP72 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal recognition particle 68. This gene encodes a subunit of the signal recognition particle (SRP). The SRP is a ribonucleoprotein complex that transports secreted and membrane proteins to the endoplasmic reticulum for processing. The complex includes a 7S RNA and six protein subunits. The encoded protein is the 68kDa component of the SRP, and forms a heterodimer with the 72kDa subunit that is required for SRP function. Altern…
- **Diseases (Open Targets)**: neurodegenerative disease (0.347); neutropenia, severe congenital, 10, autosomal recessive (0.333); COVID-19 (0.155); metabolic syndrome (0.074); atrial septal defect (0.073)
- **Europe PMC papers**: 440
- **Why important**: SRP68 is the central member of the module’s signal-recognition-particle pair with SRP72, supported by a very strong STRING relationship and the RNA-binding and SRP annotations (GO:MF RNA binding; q_global = 0.0107) (STRING Function RNA binding; within-query FDR = 0.0007) (STRING Keyword Signal recognition particle; within-query FDR = 0.0241). Its established role in signal-sequence recognition and cotranslational targeting connects the module’s RNA and translation machinery to endoplasmic-reticulum delivery of secretory and membrane proteins. Its tissue detection in both tissues and association with neutrophil and epithelial cell contexts make it relevant to shared tissue biology, despite the absence of secreted genes in the module.
- **Conclusion**: Established evidence supports SRP68 as a functional SRP component and as part of a translation-to-membrane-targeting branch of the module. The co-abundance pattern suggests coordination with cytosolic RNA and translation machinery, but it does not establish that this module specifically controls secretion or membrane-protein production in bone marrow or lung.

#### TRIM25

- **Related proteins** (co-abundance neighbors): EIF4G1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tripartite motif containing 25. The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein is an RNA binding protein, functions as a ubiquitin E3 ligase and is involved in multiple cellular processes, including regulation of antiviral innate immunity. [provided by RefSeq, S…
- **Diseases (Open Targets)**: dengue disease (0.463); COVID-19 (0.376); severe acute respiratory syndrome (0.372); neoplasm (0.108); hepatocellular carcinoma (0.106)
- **Europe PMC papers**: 4363
- **Why important**: TRIM25 is the module’s clearest immune-linked regulatory gene. It is an RNA-binding protein and ubiquitin E3 ligase with established roles in antiviral innate immunity, ubiquitin-dependent protein regulation, oxidative-stress response, and autophagy. Its neutrophil-enhanced HPA pattern distinguishes it from the broadly expressed core genes, while its network connection to EIF4G1 places it at the interface of translation and regulatory protein turnover. It has extensive literature coverage and disease associations involving dengue, coronavirus disease, respiratory syndrome, and cancer.
- **Conclusion**: Established evidence supports TRIM25 as an RNA-binding ubiquitin regulator with relevance to innate immunity (GO:MF RNA binding; q_global = 0.0107) (STRING Function RNA binding; within-query FDR = 0.0007) (STRING Keyword Isopeptide bond; within-query FDR = 0.0021) (STRING Keyword Ubl conjugation; within-query FDR = 0.0061). It could help explain tissue or cell-state responsiveness in the shared module, especially where neutrophils contribute to samples. Direct coordination between TRIM25 and the module’s translation and RNA-processing genes is a hypothesis rather than an established mechanism.

## Module 17

**Tissue pair**: bone_marrow and lung  
**Genes (5)**: DNAJB1, PRRC2A, PUM1, SKIC8, TMEM263

### Function

No GO or KEGG term passed global correction, and there is no supplementary STRING functional enrichment. The module therefore does not support a specific pathway-level functional assignment from enrichment analysis. Its strongest signal is a co-abundance pattern centered on TMEM263, connected to proteins involved in RNA regulation, RNA surveillance, translation control, and proteostasis. This is best interpreted as a possible shared cellular gene-expression or protein-homeostasis program rather than as an established pathway. The functional interpretation remains tentative because the network is sparse and lacks external interaction support.

**Cell composition.** The module is not composed of secreted or plasma proteins and does not show a blood-cell-enriched signature. HPA reports low tissue specificity for every member, low immune-cell specificity for most members, and no enriched blood-cell category. Protein detection is broad in bone marrow and largely present in lung, consistent with expression in multiple resident cell types rather than a clearly restricted tissue or immune population. Several genes have cell-type-enhanced HPA patterns in reproductive, epithelial, pancreatic-duct, or podocyte populations, but these annotations are heterogeneous and do not define a coherent bone-marrow or lung cell type. The shared module is therefore unlikely to be explained simply by plasma carryover or a dominant blood-cell population; it may instead reflect broadly expressed housekeeping or stress-related biology, with possible contributions from shared cellular composition.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module members, and no hu.MAP complex contains multiple members. Thus, the co-abundance edges are not corroborated as established physical or functional interactions by these resources. The internal pattern is organized around TMEM263, which is connected to each of the other members, while the remaining genes are peripheral and are not connected to one another in the supplied network. Known gene annotations nevertheless point to potentially related cellular processes: SKI8 participates in transcriptional regulation and RNA surveillance, PUM1 regulates RNA fate and translation, DNAJB1 supports protein folding and chaperone activity, and PRRC2A is associated with mRNA stabilization and cytoplasmic translation. These annotations provide biological context but do not establish a shared protein complex or direct mechanism.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unrecognized co-abundance association in the bone-marrow and lung tissue pair, because the exact module pattern lacks STRING interaction support, lacks a multi-member hu.MAP complex, and has no globally significant GO or KEGG enrichment. However, those absences do not prove novelty: co-abundance can arise from coordinated regulation, cell composition, technical structure, or indirect biology without curated physical interactions. The component genes themselves are not novel biology, especially PUM1 and DNAJB1, which have substantial literature and established functions. A defensible conclusion is that the tissue-pair co-abundance pattern is potentially novel, while its mechanistic interpretation and reproducibility require independent validation.

**Hypothesis.** Hypothesis: in shared bone-marrow and lung cellular environments, TMEM263 may mark or participate in a broad cellular state that coordinates membrane-associated biology with RNA handling and proteostasis. Variation in this state could produce correlated abundance of TMEM263 with SKI8, PUM1, DNAJB1, and PRRC2A through common transcriptional, translational, or stress-responsive regulation rather than direct physical binding. This hypothesis predicts that the association should be tested across independent samples, with cell-type-resolved measurements and perturbation of TMEM263 to determine whether RNA surveillance, translation control, or chaperone activity changes. The current data establish co-abundance, not causality.

### Important genes

#### TMEM263

- **Related proteins** (co-abundance neighbors): SKIC8 (0.86), PUM1 (0.84), DNAJB1 (0.82), PRRC2A (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transmembrane protein 263. Predicted to be integral component of membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: aging (0.377); non-neoplastic bile duct disorder (0.298); osteoarthritis (0.215); placental abruption (0.191); skeletal dysplasia (0.191)
- **Europe PMC papers**: 147
- **Why important**: TMEM263 is the central network member, connected to every other module gene and having the greatest weighted connectivity in the supplied subgraph. HPA detects its protein in both bone marrow and lung, with low tissue and immune-cell specificity, making it a plausible marker of a broadly distributed cellular program. Its annotation identifies it as a predicted integral membrane protein, while Open Targets links it to aging, osteoarthritis, skeletal dysplasia, and other disorders. Its literature volume is modest relative to the other leading candidates, which makes it especially informative for testing whether the module contains a less-characterized regulatory component.
- **Conclusion**: Established evidence supports TMEM263 as the network hub and a broadly detected predicted membrane protein. It is a priority candidate for module validation, but its role in RNA regulation, proteostasis, or the bone-marrow–lung association is a hypothesis rather than an established function.

#### PUM1

- **Related proteins** (co-abundance neighbors): TMEM263 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pumilio RNA binding family member 1. This gene encodes a member of the PUF family, evolutionarily conserved RNA-binding proteins related to the Pumilio proteins of Drosophila and the fem-3 mRNA binding factor proteins of C. elegans. The encoded protein contains a sequence-specific RNA binding domain comprised of eight repeats and N- and C-terminal flanking regions, and serves as a translational regulator of specific mRNAs by binding …
- **Diseases (Open Targets)**: spinocerebellar ataxia 47 (0.751); neurodevelopmental disorder with motor abnormalities, seizures, and facial dysmorphism (0.676); hereditary disease (0.504); neurodegenerative disease (0.487); hypertensive disorder (0.290)
- **Europe PMC papers**: 2316
- **Why important**: PUM1 is a conserved sequence-specific RNA-binding protein that regulates translation, mRNA stability, post-transcriptional gene expression, miRNA processing, and related RNA processes. It is connected to TMEM263 in the module and is detected in both relevant tissues. It has the strongest disease and literature support among the module members, including associations with spinocerebellar ataxia and neurodevelopmental or neurodegenerative disease, making it a biologically interpretable anchor for an RNA-regulatory hypothesis.
- **Conclusion**: Established evidence supports PUM1 as an RNA fate and translation regulator with substantial disease relevance. Its module association may indicate coordinated RNA regulation, but the data do not show that PUM1 mediates the other module relationships or that the module is specific to any PUM1-associated disease.

#### DNAJB1

- **Related proteins** (co-abundance neighbors): TMEM263 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DnaJ heat shock protein family (Hsp40) member B1. This gene encodes a member of the DnaJ or Hsp40 (heat shock protein 40 kD) family of proteins. DNAJ family members are characterized by a highly conserved amino acid stretch called the 'J-domain' and function as one of the two major classes of molecular chaperones involved in a wide range of cellular events, such as protein folding and oligomeric protein complex assembly. The encoded protein is a …
- **Diseases (Open Targets)**: fibrolamellar hepatocellular carcinoma (0.377); hepatocellular adenoma (0.370); bile duct adenocarcinoma (0.370); hepatocellular carcinoma (0.290); hepatoblastoma (0.281)
- **Europe PMC papers**: 2924
- **Why important**: DNAJB1 is a well-characterized Hsp40-family molecular chaperone that supports protein folding and assembly and responds to unfolded-protein and heat-related stress. It is connected to TMEM263, detected in both tissues, and has extensive literature and disease-related annotation, including multiple liver neoplasm associations. Its inclusion gives the module a plausible proteostasis dimension alongside the RNA-related genes.
- **Conclusion**: Established evidence supports DNAJB1 as a chaperone and proteostasis factor. Its co-abundance with TMEM263 is compatible with a shared cellular stress or protein-quality-control state, but no direct interaction or causal link between them is established here.

#### SKIC8

- **Related proteins** (co-abundance neighbors): TMEM263 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SKI8 subunit of superkiller complex. WDR61 is a subunit of the human PAF and SKI complexes, which function in transcriptional regulation and are involved in events downstream of RNA synthesis, such as RNA surveillance (Zhu et al., 2005 [PubMed 16024656]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: dengue disease (0.370); intelligence (0.343); mathematical ability (0.200); Peyronie disease (0.185); exudative vitreoretinopathy (0.059)
- **Europe PMC papers**: 22
- **Why important**: SKIC8 is a subunit of the human PAF and SKI complexes, which are involved in transcriptional regulation, RNA surveillance, nonsense-mediated decay, and rescue of stalled cytosolic ribosomes. It is connected to TMEM263 and detected in both bone marrow and lung. Its cell-type-enhanced HPA pattern is not tissue-specific, so it may reflect a general cellular RNA-surveillance program rather than a lineage-restricted signal.
- **Conclusion**: Established evidence supports SKIC8 as a component of transcription and RNA-surveillance machinery. Its presence supports an RNA quality-control interpretation of the module, but the module data do not demonstrate assembly of a SKI or PAF complex or a direct relationship with TMEM263.

#### PRRC2A

- **Related proteins** (co-abundance neighbors): TMEM263 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proline rich coiled-coil 2A. A cluster of genes, BAT1-BAT5, has been localized in the vicinity of the genes for TNF alpha and TNF beta. These genes are all within the human major histocompatibility complex class III region. This gene has microsatellite repeats which are associated with the age-at-onset of insulin-dependent diabetes mellitus (IDDM) and possibly thought to be involved with the inflammatory process of pancreatic…
- **Diseases (Open Targets)**: neurodegenerative disease (0.477); neoplasm (0.085); hepatocellular carcinoma (0.079); colorectal carcinoma (0.074); type 1 diabetes mellitus (0.051)
- **Europe PMC papers**: 993
- **Why important**: PRRC2A is associated with mRNA stabilization and regulation of cytoplasmic translation and is connected to TMEM263. It is detected in bone marrow but not lung in the supplied HPA protein data, making it a potentially informative contributor to the cross-tissue pattern rather than a uniformly detected component. Its location in the major histocompatibility complex class III region and reported associations with inflammatory or metabolic disease add disease-context relevance, while its literature volume is substantial.
- **Conclusion**: Established evidence supports PRRC2A as an RNA-stability and translation-related factor with disease-associated genomic context. Its participation may reflect post-transcriptional regulation, but the lack of lung protein detection and absence of external interaction support make its role in the shared module uncertain.

## Module 18

**Tissue pair**: bone_marrow and lung  
**Genes (5)**: FUCA2, HMGCL, F11R, NUP54, TBC1D24

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING functional enrichment. The module therefore does not support a statistically established canonical pathway assignment. Its genes represent diverse established functions: epithelial or endothelial adhesion and barrier regulation through F11R, glycoprotein fucose metabolism through FUCA2, mitochondrial leucine degradation and ketone-body formation through HMGCL, Rab-related membrane-trafficking regulation through TBC1D24, and nucleocytoplasmic transport through NUP54. The co-abundance pattern is consequently best interpreted as a candidate cross-tissue state rather than a demonstrated biochemical pathway. The strongest biological themes suggested by the individual annotations are epithelial barrier biology, extracellular glycoprotein processing, cellular trafficking, and metabolic or proteostatic state.

**Cell composition.** The module is not dominated by a uniform plasma-protein or immune-cell signature. FUCA2 is the sole secreted-to-blood protein and is annotated as a plasma alpha-L-fucosidase, whereas the other genes are not secreted. HPA assigns tissue-enhanced expression to FUCA2, HMGCL, and TBC1D24, while F11R and NUP54 have low tissue specificity. All genes have some cell-type-enhanced annotation, but the reported cell types are heterogeneous, including epithelial, stromal, placental, hepatic, neural, renal, and cardiac populations. Blood-cell specificity is generally low; F11R is group-enriched in eosinophils and neutrophils, while TBC1D24 is not detected in immune cells. Protein detection is broader in bone marrow than in lung in the supplied HPA summary, but the module does not present as a simple blood-cell program. The shared signal could instead reflect mixed cellular composition, epithelial or stromal contributions, or a common cellular state across the two tissues. FUCA2 requires particular caution because its gene-specific HPA immunohistochemistry reports no detection in either tissue despite its secreted-protein annotation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship was present among any gene pair in the module, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated by the supplied curated or predicted physical-interaction resources. This argues against interpreting the graph as a known protein complex. It does not invalidate the co-abundance module: co-regulation, shared cell-type composition, secretion or uptake, parallel stress responses, or indirect tissue-level coupling can produce correlated abundance without direct physical binding. The network topology is centered on FUCA2, which connects to F11R, NUP54, and HMGCL, while TBC1D24 connects to HMGCL; this topology is useful for prioritization but does not establish mechanism.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a previously unreported tissue-pair co-abundance pattern, but the supplied evidence is insufficient to call it a new biological mechanism. Its individual gene functions and disease associations are established in the literature, while the specific cross-tissue combination has no support from the supplied STRING or hu.MAP resources. Database absence alone cannot demonstrate novelty, especially because these resources primarily address physical interactions or complexes rather than co-abundance across tissues. A defensible conclusion is that the module is a novel candidate association requiring replication, cell-composition adjustment, independent cohorts, and experimental or perturbational testing. Its apparent novelty lies in the joint co-abundance pattern, not in the genes or their individual functions.

**Hypothesis.** Hypothesis: the module reflects a shared epithelial or stromal cellular state involving barrier organization, extracellular glycoprotein processing, intracellular trafficking, and metabolic adaptation in bone marrow and lung. F11R may mark or participate in junctional barrier biology; FUCA2 may represent extracellular or plasma glycan-processing activity; HMGCL may report altered mitochondrial substrate use; TBC1D24 may connect that state to membrane trafficking; and NUP54 may reflect accompanying changes in nucleocytoplasmic transport. An alternative explanation is shared cell composition or sample-level admixture rather than coordinated regulation within one cell type. This hypothesis is not established by GO/KEGG, STRING, or hu.MAP enrichment and should be tested by cell-resolved expression, protein measurements, covariate-adjusted co-abundance analysis, and perturbation of the proposed barrier, trafficking, and metabolic components.

### Important genes

#### FUCA2

- **Related proteins** (co-abundance neighbors): F11R (0.90), NUP54 (0.84), HMGCL (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alpha-L-fucosidase 2. This gene encodes a plasma alpha-L-fucosidase, which represents 10-20% of the total cellular fucosidase activity. The protein is a member of the glycosyl hydrolase 29 family, and catalyzes the hydrolysis of the alpha-1,6-linked fucose joined to the reducing-end N-acetylglucosamine of the carbohydrate moieties of glycoproteins. This enzyme is essential for Helicobacter pylori adhesion to human gast…
- **Diseases (Open Targets)**: asthma (0.363); chronic rhinosinusitis (0.362); inflammatory bowel disease (0.361); Precordial pain (0.271); major salivary gland cancer (0.180)
- **Europe PMC papers**: 364
- **Why important**: FUCA2 is the network hub, linking three other module members, and therefore has the strongest module-level position. It encodes a plasma alpha-L-fucosidase involved in glycoprotein carbohydrate and fucose metabolism and is the only secreted-to-blood protein in the module. Its HPA annotation is tissue-enhanced in parathyroid gland and cell-type-enhanced in decidual stromal cells, extravillous trophoblasts, and Hofbauer cells. It also has disease associations involving asthma, chronic rhinosinusitis, and inflammatory bowel disease, with a substantial literature record.
- **Conclusion**: Established evidence supports FUCA2 as a secreted glycosidase and the central co-abundance connector. The module does not establish that FUCA2 regulates the other genes or that its enzymatic activity drives the shared tissue signal. Its prominence makes it a strong biomarker candidate, but its lack of STRING and hu.MAP support favors an indirect or composition-related interpretation.

#### F11R

- **Related proteins** (co-abundance neighbors): FUCA2 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Microtubules; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: F11 receptor. Tight junctions represent one mode of cell-to-cell adhesion in epithelial or endothelial cell sheets, forming continuous seals around cells and serving as a physical barrier to prevent solutes and water from passing freely through the paracellular space. The protein encoded by this immunoglobulin superfamily gene member is an important regulator of tight junction assembly in epithelia. In addition…
- **Diseases (Open Targets)**: neurodegenerative disease (0.354); cellulitis (0.135); abscess (0.135); neoplasm (0.115); breast cancer (0.114)
- **Europe PMC papers**: 1583
- **Why important**: F11R is connected directly to the FUCA2 hub and has a clear barrier-related function. It encodes a tight-junction and cell-adhesion regulator involved in epithelial sealing, leukocyte cell-cell adhesion, inflammatory response, and cytokine regulation. HPA places it in several epithelial cell types and reports group enrichment in eosinophils and neutrophils, while protein detection is reported in both tissues. It also has a substantial literature record and disease associations spanning inflammatory and neoplastic contexts.
- **Conclusion**: Established evidence supports F11R as the most direct epithelial or endothelial barrier marker in the module. Its co-abundance with FUCA2 is compatible with a shared barrier or extracellular-interface state, but no physical interaction is supported by STRING or hu.MAP. The immune-cell annotation means that leukocyte admixture remains a competing explanation.

#### HMGCL

- **Related proteins** (co-abundance neighbors): TBC1D24 (0.90), FUCA2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3-hydroxy-3-methylglutaryl-CoA lyase. The protein encoded by this gene belongs to the HMG-CoA lyase family. It is a mitochondrial enzyme that catalyzes the final step of leucine degradation and plays a key role in ketone body formation. Mutations in this gene are associated with HMG-CoA lyase deficiency. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2009].
- **Diseases (Open Targets)**: 3-hydroxy-3-methylglutaric aciduria (0.849); long chain 3-hydroxyacyl-CoA dehydrogenase deficiency (0.548); hereditary disease (0.494); Intellectual disability (0.370); neurodegenerative disease (0.215)
- **Europe PMC papers**: 1278
- **Why important**: HMGCL occupies an internal bridging position between TBC1D24 and FUCA2. It is a mitochondrial enzyme required for the final step of leucine degradation and for ketone-body formation, and mutations cause HMG-CoA lyase deficiency. HPA reports tissue enhancement in liver and cell-type enhancement in hepatocytes and esophageal apical cells, with protein detection in both tissues. It has the largest literature volume among the selected genes and well-established metabolic disease associations.
- **Conclusion**: Established evidence supports HMGCL as a marker of mitochondrial amino-acid and ketone-body metabolism. Its network position suggests that metabolic state may connect the FUCA2-associated signal to TBC1D24, but this is a hypothesis rather than demonstrated biochemical coupling. The liver and hepatocyte annotations also make shared metabolic or cell-composition effects plausible.

#### TBC1D24

- **Related proteins** (co-abundance neighbors): HMGCL (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cell Junctions; IHC detected in bone_marrow, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TBC1 domain family member 24. This gene encodes a protein with a conserved domain, referred to as the TBC domain, characteristic of proteins which interact with GTPases. TBC domain proteins may serve as GTPase-activating proteins for a particular group of GTPases, the Rab (Ras-related proteins in brain) small GTPases which are involved in the regulation of membrane trafficking. Mutations in this gene are associated with famili…
- **Diseases (Open Targets)**: DOORS syndrome (0.809); familial infantile myoclonic epilepsy (0.765); rolandic epilepsy-paroxysmal exercise-induced dystonia-writer's cramp syndrome (0.765); autosomal dominant nonsyndromic hearing loss 65 (0.736); autosomal recessive nonsyndromic hearing loss 86 (0.733)
- **Europe PMC papers**: 656
- **Why important**: TBC1D24 connects to HMGCL and provides a membrane-trafficking dimension absent from the other selected genes. Its conserved TBC domain is associated with regulation of Rab-family GTPases and membrane trafficking. HPA places it at the plasma membrane and cell junctions and reports cell-type enhancement in several neural populations, with no detection in immune cells. It has strong disease associations with epilepsy, hearing loss, and related syndromes.
- **Conclusion**: Established evidence supports TBC1D24 as a trafficking regulator with relevance to membrane and junctional biology. Its co-abundance with HMGCL could indicate a coordinated cellular state involving trafficking and metabolism, but the module does not demonstrate that relationship mechanistically. Its absence from immune-cell detection argues against interpreting this gene as a generic blood-cell marker.

#### NUP54

- **Related proteins** (co-abundance neighbors): FUCA2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 54. The nuclear envelope creates distinct nuclear and cytoplasmic compartments in eukaryotic cells. It consists of two concentric membranes perforated by nuclear pores, large protein complexes that form aqueous channels to regulate the flow of macromolecules between the nucleus and the cytoplasm. These complexes are composed of at least 100 different polypeptide subunits, many of which belong to the n…
- **Diseases (Open Targets)**: dystonia 37, early-onset, with striatal lesions (0.548); Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.526); neurodegenerative disease (0.371)
- **Europe PMC papers**: 541
- **Why important**: NUP54 connects directly to the FUCA2 hub and represents nuclear transport rather than extracellular, junctional, or metabolic biology. It encodes a nucleoporin involved in nuclear pore organization and nucleocytoplasmic transport. HPA reports low tissue specificity, nucleoplasmic localization, cell-type enhancement in cardiomyocytes, detection in bone marrow, and no detection in lung. Its disease and infectious-disease associations and literature record make it biologically relevant despite its peripheral network position.
- **Conclusion**: Established evidence supports NUP54 as a nuclear-pore component. Its co-abundance with FUCA2 may report a broad cellular-state or sample-composition effect rather than a direct functional partnership, particularly because lung protein detection is absent in the supplied HPA evidence and no STRING or hu.MAP relationship is known. NUP54 is therefore useful as a test of whether the module extends beyond extracellular and barrier biology.

## Module 19

**Tissue pair**: bone_marrow and lung  
**Genes (5)**: GNPNAT1, MED30, EMG1, PXMP2, TIA1

### Function

No GO/KEGG term passed global correction, and there are no supplementary STRING terms. Therefore, the module does not support a statistically established pathway-level function from enrichment alone. Its gene content instead suggests a mixed cellular-maintenance program: PXMP2 is a peroxisomal membrane protein, EMG1 supports small-subunit ribosomal RNA maturation and rRNA base methylation, GNPNAT1 participates in UDP-N-acetylglucosamine biosynthesis, TIA1 regulates RNA processing, translation and stress-granule assembly, and MED30 participates in Mediator-dependent transcription. The co-abundance structure is therefore more consistent with coordinated basal organelle, RNA, glycosylation and gene-regulatory biology than with a single demonstrated pathway. These functional assignments are established annotations, whereas any coordination among them in bone marrow and lung remains interpretive.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. It also does not resemble a blood-cell-enriched module, because every gene has low immune-cell specificity and no enriched blood-cell category is reported. Most genes have low tissue specificity, while tissue-enhanced signals recur in liver and cell-type-enhanced signals occur in specialized epithelial, reproductive, pancreatic and platelet-related populations. HPA protein detection is sparse in bone marrow and lung, with limited detection in lung and no detection reported for the other available bone-marrow entries. Thus, the shared bone-marrow–lung signal is unlikely to be explained simply as a plasma-protein or broad blood-cell signature. It may instead reflect a conserved intracellular program, cell-composition effects, or technical co-abundance across tissues; the HPA evidence does not establish which explanation is correct.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair reaches the supplied high-confidence STRING interaction threshold, and no STRING functional-enrichment result is available. No hu.MAP complex contains multiple module members. The observed co-abundance edges are therefore not supported by the supplied catalogued physical-interaction or complex evidence. PXMP2 is the most connected and strongest-associated node within this small subgraph, linking GNPNAT1, TIA1 and EMG1, while EMG1 links PXMP2 with MED30. These network relationships should be interpreted as co-abundance associations rather than established direct molecular interactions. The absence of STRING or hu.MAP support argues against a well-known physical complex, but it does not invalidate the module or prove that the associations are novel biology.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a previously unrecognized cross-tissue co-abundance association, because the module has no supplied high-confidence STRING interactions, no multi-member hu.MAP complex, and no globally significant GO/KEGG term. However, it cannot be called a new biological pathway on these facts alone. The genes are individually well studied to differing extents, and database absence can reflect incomplete coverage, context dependence, indirect regulation or limitations of the interaction resources. The strongest defensible conclusion is that the coordinated association is potentially novel and hypothesis-generating, requiring replication in independent bone-marrow and lung datasets, preservation testing, and experimental or perturbational validation.

**Hypothesis.** Hypothesis: this module reflects coordinated regulation of intracellular housekeeping processes in a shared or technically aligned cell-state component of bone marrow and lung. PXMP2 may occupy a central co-abundance position connecting peroxisomal membrane biology with GNPNAT1-linked glycosylation precursor production, TIA1-linked RNA and stress responses, and EMG1/MED30-linked ribosome biogenesis and transcriptional regulation. A plausible mechanism is that a common metabolic or proteostatic state alters organelle maintenance, RNA processing, translation control and transcription together. This is a hypothesis, not an established pathway, because global enrichment is absent and neither STRING nor hu.MAP supplies physical-complex support.

### Important genes

#### PXMP2

- **Related proteins** (co-abundance neighbors): GNPNAT1 (0.90), TIA1 (0.85), EMG1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peroxisomal membrane protein 2. Located in peroxisomal membrane. Part of protein-containing complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: retinal degeneration (0.161); hepatocellular carcinoma (0.076); neoplasm (0.072); hereditary xanthinuria (0.053); neonatal intrahepatic cholestasis due to citrin deficiency (0.049)
- **Europe PMC papers**: 3426
- **Why important**: PXMP2 is the central network node in the supplied subgraph, connecting GNPNAT1, TIA1 and EMG1, and it has the strongest aggregate co-abundance connectivity. Its established annotation places it in the peroxisomal membrane. HPA indicates liver enhancement and enrichment in gastric chief, hepatocyte and parietal-cell contexts, while Open Targets links it to retinal degeneration, hepatocellular carcinoma, neoplasm, hereditary xanthinuria and neonatal intrahepatic cholestasis due to citrin deficiency. Its substantial literature volume makes it a prominent anchor for interpreting the module, although the disease links do not establish a role in this tissue-pair module.
- **Conclusion**: Established evidence supports PXMP2 as a peroxisomal membrane protein and the principal network anchor. The hypothesis that it coordinates peroxisomal state with the other module processes is plausible from its network position but remains unproven.

#### EMG1

- **Related proteins** (co-abundance neighbors): MED30 (0.84), PXMP2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EMG1 N1-specific pseudouridine methyltransferase. This gene encodes an essential, conserved eukaryotic protein that methylates pseudouridine in 18S rRNA. The related protein in yeast is a component of the small subunit processome and is essential for biogenesis of the ribosomal 40S subunit. A mutation in this gene has been associated with Bowen-Conradi syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Fe…
- **Diseases (Open Targets)**: Bowen-Conradi syndrome (0.671); hereditary disease (0.181); neurodegenerative disease (0.088); retinitis pigmentosa (0.085); cone dystrophy (0.076)
- **Europe PMC papers**: 457
- **Why important**: EMG1 connects PXMP2 with MED30 and has a strong internal network position. It is an essential, conserved N1-specific pseudouridine methyltransferase involved in rRNA processing, small-subunit ribosome biogenesis and rRNA base methylation. HPA reports nucleolar-rim localization, lung detection and absence of bone-marrow detection in the supplied measurements. Open Targets strongly associates it with Bowen-Conradi syndrome and also reports links to hereditary, neurodegenerative and retinal disorders. Its literature volume is moderate, and its mechanistic role in ribosome production gives the module a clear RNA-processing component.
- **Conclusion**: Established evidence supports EMG1 as a ribosome-biogenesis and rRNA-modification factor with a disease connection to Bowen-Conradi syndrome. Its connection to PXMP2 and MED30 may indicate coordinated growth or proteostatic state, but that cross-process mechanism is hypothetical.

#### TIA1

- **Related proteins** (co-abundance neighbors): PXMP2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TIA1 cytotoxic granule associated RNA binding protein. The product encoded by this gene is a member of a RNA-binding protein family and possesses nucleolytic activity against cytotoxic lymphocyte (CTL) target cells. It has been suggested that this protein may be involved in the induction of apoptosis as it preferentially recognizes poly(A) homopolymers and induces DNA fragmentation in CTL targets. The major granule-associated species is a 15-kDa prote…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis 26 with or without frontotemporal dementia (0.663); distal myopathy, Welander type (0.648); Abnormality of the skeletal system (0.530); hereditary disease (0.187); neoplasm (0.114)
- **Europe PMC papers**: 3316
- **Why important**: TIA1 is directly connected to PXMP2 and contributes a distinct RNA-regulatory and stress-response function. It is a cytotoxic-granule-associated RNA-binding protein implicated in alternative splicing, negative regulation of translation, apoptosis and cytoplasmic stress-granule assembly. HPA places it in the nucleoplasm and reports cell-type enhancement in late primary spermatocytes, platelets and tuft cells, without blood-cell specificity. Open Targets associates it with amyotrophic lateral sclerosis with or without frontotemporal dementia, Welander distal myopathy, skeletal-system abnormalities and neoplasm. Its substantial literature volume and disease relevance make it an important interpretive gene.
- **Conclusion**: Established evidence supports TIA1 as an RNA-binding, translation-regulatory and stress-granule factor. Its co-abundance with PXMP2 could reflect a shared stress or proteostasis state, but a direct peroxisome–TIA1 mechanism is not established.

#### GNPNAT1

- **Related proteins** (co-abundance neighbors): PXMP2 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glucosamine-phosphate N-acetyltransferase 1. Enables identical protein binding activity. Predicted to be involved in UDP-N-acetylglucosamine biosynthetic process. Predicted to act upstream of or within cellular response to leukemia inhibitory factor. Predicted to be located in late endosome. Predicted to be active in Golgi apparatus; endoplasmic reticulum; and endoplasmic reticulum-Golgi intermediate compartment. [provided by Alliance of Gen…
- **Diseases (Open Targets)**: rhizomelic dysplasia, Ain-Naz type (0.520); Alzheimer disease (0.217); endocarditis (0.189); myalgic encephalomeyelitis/chronic fatigue syndrome (0.188); clubfoot (0.185)
- **Europe PMC papers**: 379
- **Why important**: GNPNAT1 is connected to the central PXMP2 node and adds a metabolic and glycosylation-related dimension. Its annotation supports UDP-N-acetylglucosamine biosynthesis and places its activity in secretory-pathway-associated compartments including the Golgi, endoplasmic reticulum and related intermediate compartments. HPA reports liver enhancement and cell-type enhancement across hepatocytes, extravillous trophoblasts, late primary spermatocytes, epididymal clear cells and pancreatic acinar cells, with no immune-cell specificity. Open Targets associates it with rhizomelic dysplasia, Ain-Naz type and several other disorders. Its literature volume is smaller than that of PXMP2 or TIA1, making it a useful but less established mechanistic anchor.
- **Conclusion**: Established evidence supports GNPNAT1 as a UDP-N-acetylglucosamine biosynthesis factor with broad specialized-cell expression. Its link to PXMP2 may reflect coordinated organelle or glycosylation-state biology, but this interpretation is a hypothesis.

#### MED30

- **Related proteins** (co-abundance neighbors): EMG1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mediator complex subunit 30. The multiprotein TRAP/Mediator complex facilitates gene expression through a wide variety of transcriptional activators. MED30 is a component of this complex that appears to be metazoan specific (Baek et al., 2002 [PubMed 11909976]).[supplied by OMIM, Nov 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.484); polyarteritis nodosa (0.313); placental retention (0.310); urinary tract infection (0.303); self-injurious ideation (0.278)
- **Europe PMC papers**: 342
- **Why important**: MED30 is connected to EMG1 and contributes transcriptional control through the Mediator complex, including RNA polymerase II preinitiation and transcriptional regulation. HPA reports nucleoplasmic localization, low tissue specificity and cell-type enhancement in basal keratinocytes, with low immune-cell specificity. Open Targets associates it with neurodegenerative disease, polyarteritis nodosa, placental retention, urinary tract infection and self-injurious ideation. Its literature volume is modest, and its network position is peripheral, but it is important because it could provide transcriptional coordination for the other cellular programs.
- **Conclusion**: Established evidence supports MED30 as a Mediator-associated transcriptional regulator. Its association with EMG1 may reflect coordinated transcription and ribosome-production demands, but no physical complex or module-specific regulatory mechanism is demonstrated.
