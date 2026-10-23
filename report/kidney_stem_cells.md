# Conserved co-abundance modules: kidney and stem_cells

## Module 0

**Tissue pair**: kidney and stem_cells  
**Genes (26)**: HIBADH, AKAP1, BCAT2, CCDC134, CGN, CDK5RAP3, ERCC3, TBRG4, GALNS, GGH, HACL2, INTS8, PPA2, KIF1C, MARK2, MICU2, MPDZ, MYO18A, NDUFAF7, PDP1, PDPR, PAK1IP1, MRPS33, SNX33, TIMM44, TPX2

### Function

The strongest functional interpretation is mitochondrial branched-chain amino-acid metabolism, especially valine catabolism, supported by the globally corrected term (GO:BP valine metabolic process; q_global = 0.0329) and its members BCAT2, HIBADH, and HACL2. BCAT2 initiates branched-chain amino-acid catabolism, while HIBADH catalyzes a subsequent step in valine breakdown. HACL2 is annotated for fatty-acid alpha-oxidation and may indicate broader mitochondrial lipid and organic-acid metabolism. The supplementary STRING terms (STRING Keyword Transit peptide; within-query FDR = 0.0028), (STRING Keyword Mitochondrion; within-query FDR = 0.0287), and (STRING Component Mitochondrial matrix; within-query FDR = 0.0305) support a mitochondrial and mitochondrial-matrix context, but they are not global enrichment evidence. The module also contains genes involved in pyruvate dehydrogenase regulation, mitochondrial protein import, mitochondrial translation, mitochondrial calcium handling, and mitochondrial pyrophosphate metabolism. Its sparse co-abundance structure and limited direct interaction evidence suggest a coordinated metabolic state rather than a single well-defined physical complex. MPDZ, CGN, KIF1C, MARK2, SNX33, MYO18A, and TPX2 additionally point to epithelial polarity, vesicle trafficking, cytoskeletal organization, and cell-cycle-related biology, but these are secondary interpretations rather than the primary module function.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: only a small minority of genes are annotated as secreted, and most are intracellular or membrane-associated. It is also not strongly blood-cell enriched. Most genes have low immune-cell specificity, with only isolated immune-cell enrichment or enhancement. The HPA data show broad representation, with many genes having low tissue specificity, while the tissue-enhanced genes are distributed across skeletal muscle, liver, tongue, testis, kidney, and other tissues. Cell-type enhancement is prominent in several specialized epithelial, trophoblast, germ-cell, and glial populations, so shared cell-type composition or cellular-state effects remain possible. Kidney protein detection is widespread across the module, whereas there is no matching HPA tissue category for stem cells. Overall, the module is more consistent with a broadly expressed intracellular metabolic program, potentially modulated by cell-type composition, than with blood contamination.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP valine metabolic process | 0.0329 | BCAT2, HACL2, HIBADH |

### STRING and hu.MAP

The high-confidence STRING evidence is limited to the known CGN–MPDZ relationship and the PDP1–PDPR relationship. The latter directly supports the pyruvate dehydrogenase phosphatase component of the mitochondrial metabolic interpretation; the former supports an epithelial junction and polarity connection. The supplementary STRING enrichment for mitochondrial and mitochondrial-matrix keywords (STRING Keyword Transit peptide; within-query FDR = 0.0028), (STRING Keyword Mitochondrion; within-query FDR = 0.0287), and (STRING Component Mitochondrial matrix; within-query FDR = 0.0305) is concordant with the annotations of BCAT2, HIBADH, PPA2, PDP1, PDPR, TIMM44, NDUFAF7, MICU2, AKAP1, TBRG4, and MRPS33, but remains supplementary evidence. hu.MAP provides additional support for shared mitochondrial and metabolic machinery: (hu.MAP huMAP3_13468.1) contains NDUFAF7, PDPR, PPA2, and PDP1, while (hu.MAP huMAP3_10525.1) contains PDPR and PPA2. These complexes contain many proteins from mitochondrial metabolism and protein handling, but the module members do not establish that the entire module is one physical complex. The combined evidence indicates partial reuse of known mitochondrial machinery embedded within a broader co-abundance program.

**STRING interactions (score >= 0.7)**: 2 of 325 gene pairs: CGN–MPDZ (0.859); PDP1–PDPR (0.891)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transit peptide (FDR = 0.0028, 10 genes); Keyword Mitochondrion (FDR = 0.0287, 11 genes); Component Mitochondrial matrix (FDR = 0.0305, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (NDUFAF7, PDPR, PPA2, PDP1; 4/99); huMAP3_10525.1 (PDPR, PPA2; 2/33)

### Novelty

The co-abundance module may represent a new cross-tissue association pattern, but the available evidence does not justify calling it a wholly new biological pathway or complex. Its central processes, including valine catabolism, pyruvate dehydrogenase regulation, mitochondrial import, and mitochondrial energy metabolism, are established. Several relationships are already supported by STRING or hu.MAP, particularly PDP1–PDPR and the mitochondrial complexes containing PDPR, PPA2, PDP1, and NDUFAF7. Conversely, many module pairs lack curated high-confidence interactions, and the module combines mitochondrial metabolism with epithelial polarity, trafficking, and cell-cycle genes. That combination and its conservation across kidney and stem-cell samples could be a useful new systems-level observation, but absence from STRING or hu.MAP alone cannot establish novelty. Experimental validation, replication in independent cohorts, and comparison with previously reported tissue co-expression modules would be needed.

**Hypothesis.** Hypothesis: the module reflects a coordinated mitochondrial metabolic and cellular-architecture state shared by kidney and stem-cell populations. In this model, branched-chain amino-acid and valine processing through BCAT2, HIBADH, and HACL2 supplies mitochondrial carbon flux, while PDP1 and PDPR regulate pyruvate entry into acetyl-CoA production. PPA2, MICU2, TIMM44, NDUFAF7, TBRG4, MRPS33, and AKAP1 could couple mitochondrial phosphate handling, calcium control, protein import, respiratory-complex assembly, mitochondrial translation, and localized signaling to that metabolic state. MPDZ and CGN, together with KIF1C and MARK2, may connect the metabolic program to epithelial junctions, polarity, and intracellular transport. This is a mechanistic hypothesis rather than a demonstrated pathway, because the network is sparse and most module relationships are co-abundance associations rather than experimentally established physical interactions.

### Important genes

#### BCAT2

- **Related proteins** (co-abundance neighbors): MPDZ (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: branched chain amino acid transaminase 2. This gene encodes a branched chain aminotransferase found in mitochondria. The encoded protein forms a dimer that catalyzes the first step in the production of the branched chain amino acids leucine, isoleucine, and valine. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: hypervalinemia and hyperleucine-isoleucinemia (0.688); neurodegenerative disease (0.236); pancreatic ductal adenocarcinoma (0.104); neoplasm (0.097); cancer (0.091)
- **Europe PMC papers**: 1446
- **Why important**: BCAT2 is a direct member of the globally significant valine metabolic process (GO:BP valine metabolic process; q_global = 0.0329) and catalyzes the first step of branched-chain amino-acid catabolism. It is mitochondrial, connects the module to its clearest primary annotation, and has a substantial literature and disease relevance through branched-chain amino-acid disorders and metabolic disease. Its network connection to MPDZ is not itself a validated metabolic interaction, so its importance comes mainly from pathway specificity and its role as an entry point into the proposed metabolic program.
- **Conclusion**: Established evidence identifies BCAT2 as a mitochondrial branched-chain amino-acid catabolic enzyme and a primary anchor of (GO:BP valine metabolic process; q_global = 0.0329). It is plausible, but not proven, that BCAT2 activity contributes to the shared metabolic state represented by the module.

#### HIBADH

- **Related proteins** (co-abundance neighbors): SNX33 (0.85), GGH (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3-hydroxyisobutyrate dehydrogenase. This gene encodes a mitochondrial 3-hydroxyisobutyrate dehydrogenase enzyme. The encoded protein plays a critical role in the catabolism of L-valine by catalyzing the oxidation of 3-hydroxyisobutyrate to methylmalonate semialdehyde. [provided by RefSeq, Nov 2011].
- **Diseases (Open Targets)**: nephrolithiasis (0.354); hypertensive disorder (0.298); Hallux valgus (0.288); Increased blood pressure (0.283); osteoarthritis (0.282)
- **Europe PMC papers**: 530
- **Why important**: HIBADH is one of the genes in (GO:BP valine metabolic process; q_global = 0.0329) and catalyzes oxidation of a valine-catabolic intermediate in mitochondria. It also appears in all three supplementary mitochondrial STRING terms (STRING Keyword Transit peptide; within-query FDR = 0.0028), (STRING Keyword Mitochondrion; within-query FDR = 0.0287), and (STRING Component Mitochondrial matrix; within-query FDR = 0.0305). Its combination of pathway specificity, mitochondrial localization, disease associations, and direct placement in the module makes it an important metabolic readout, even though its local network connectivity is limited.
- **Conclusion**: Established evidence supports HIBADH as a mitochondrial enzyme in valine catabolism and as part of the primary enriched process. The module may therefore report coordinated branched-chain amino-acid flux, but co-abundance does not demonstrate altered enzyme activity or metabolic flux.

#### PDP1

- **Related proteins** (co-abundance neighbors): GALNS (0.83); STRING partners: PDPR (0.891)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: pyruvate dehydrogenase phosphatase catalytic subunit 1. Pyruvate dehydrogenase (E1) is one of the three components (E1, E2, and E3) of the large pyruvate dehydrogenase complex. Pyruvate dehydrogenase kinases catalyze phosphorylation of serine residues of E1 to inactivate the E1 component and inhibit the complex. Pyruvate dehydrogenase phosphatases catalyze the dephosphorylation and activation of the E1 component to reverse the effects of pyruvate dehyd…
- **Diseases (Open Targets)**: pyruvate dehydrogenase phosphatase deficiency (0.775); COVID-19 (0.305); neurodegenerative disease (0.270); alcohol drinking (0.197); multinodular goiter (0.194)
- **Europe PMC papers**: 1532
- **Why important**: PDP1 is the catalytic subunit of pyruvate dehydrogenase phosphatase and activates pyruvate dehydrogenase by dephosphorylation. It forms the high-confidence STRING relationship with PDPR and is present in hu.MAP complex (hu.MAP huMAP3_13468.1). It therefore provides a mechanistically interpretable bridge from amino-acid-associated mitochondrial metabolism to pyruvate oxidation and acetyl-CoA production, with well-established biochemical and disease relevance.
- **Conclusion**: Established evidence supports PDP1 as a regulator of pyruvate entry into mitochondrial oxidative metabolism and as part of a known PDP1–PDPR relationship. Its proposed role as a central metabolic bridge in this module is reasonable, but the module does not establish that PDP1 controls the co-abundance pattern.

#### PDPR

- **Related proteins** (co-abundance neighbors): MICU2 (0.89); STRING partners: PDP1 (0.891)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1
- **Function (MyGene.info)**: pyruvate dehydrogenase phosphatase regulatory subunit. Pyruvate dehydrogenase complex (PDC) catalyzes the oxidative decarboxylation of pyruvate and links glycolysis to the tricarboxylic acid cycle and fatty acid synthesis. The dephosphorylation and reactivation of PDC is catalyzed by pyruvate dehydrogenase phosphatase (PDP). The dimeric PDP has a catalytic subunit and a regulatory subunit. This gene encodes the FAD-containing regulatory subunit of PDP…
- **Diseases (Open Targets)**: osteoarthritis, hip (0.288); total joint arthroplasty (0.285); osteoarthritis, knee (0.285); viral pneumonia (0.262); Alzheimer disease (0.223)
- **Europe PMC papers**: 326
- **Why important**: PDPR is the regulatory subunit of pyruvate dehydrogenase phosphatase, has the same known STRING relationship with PDP1, and occurs in both hu.MAP complexes (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1). It is also included in the supplementary mitochondrial terms (STRING Keyword Transit peptide; within-query FDR = 0.0028), (STRING Keyword Mitochondrion; within-query FDR = 0.0287), and (STRING Component Mitochondrial matrix; within-query FDR = 0.0305). These convergent annotations make PDPR one of the strongest links between network evidence, complex evidence, and mitochondrial metabolic function.
- **Conclusion**: Established evidence supports PDPR as a component of the pyruvate dehydrogenase phosphatase system and of known mitochondrial complexes. Its inclusion supports a mitochondrial oxidative-metabolism interpretation, while any role in coordinating the other module branches remains hypothetical.

#### PPA2

- **Related proteins** (co-abundance neighbors): MPDZ (0.81), TPX2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1
- **Function (MyGene.info)**: inorganic pyrophosphatase 2. The protein encoded by this gene is localized to the mitochondrion, is highly similar to members of the inorganic pyrophosphatase (PPase) family, and contains the signature sequence essential for the catalytic activity of PPase. PPases catalyze the hydrolysis of pyrophosphate to inorganic phosphate, which is important for the phosphate metabolism of cells. Alternate transcriptional splice variants…
- **Diseases (Open Targets)**: sudden cardiac arrest (0.802); neurodegenerative disease (0.535); hereditary disease (0.513); Abnormality of the cardiovascular system (0.407); dilated cardiomyopathy (0.371)
- **Europe PMC papers**: 1003
- **Why important**: PPA2 is a mitochondrial inorganic pyrophosphatase associated with phosphate metabolism and mitochondrial membrane-potential regulation. It occurs in both hu.MAP complexes (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1) and in the supplementary mitochondrial terms (STRING Keyword Transit peptide; within-query FDR = 0.0028), (STRING Keyword Mitochondrion; within-query FDR = 0.0287), and (STRING Component Mitochondrial matrix; within-query FDR = 0.0305). Although its direct co-abundance connectivity is limited, it is important because it provides a biochemical link between mitochondrial energy state, phosphate handling, and the known PDPR–PDP1 complex context. It also has substantial literature and strong disease associations involving cardiac and mitochondrial dysfunction.
- **Conclusion**: Established evidence supports PPA2 as a mitochondrial phosphate-metabolism protein represented in known complexes. Its proposed role as a metabolic-state sensor or stabilizer within this module is a hypothesis, not a demonstrated causal function.

#### MPDZ

- **Related proteins** (co-abundance neighbors): KIF1C (0.89), BCAT2 (0.86), GGH (0.84), MARK2 (0.82), PPA2 (0.81), CDK5RAP3 (0.81); STRING partners: CGN (0.859)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Centriolar satellite; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: multiple PDZ domain crumbs cell polarity complex component. The protein encoded by this gene has multiple PDZ domains, which are hallmarks of protein-protein interactions. The encoded protein is known to interact with the HTR2C receptor and may cause it to clump at the cell surface. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2015].
- **Diseases (Open Targets)**: Congenital muscular alpha-dystroglycanopathy with brain and eye anomalies (0.779); hydrocephalus, nonsyndromic, autosomal recessive 2 (0.697); Abnormality of the skeletal system (0.540); alcohol drinking (0.513); coronary artery disorder (0.508)
- **Europe PMC papers**: 825
- **Why important**: MPDZ is the most connected node in the module subgraph and links several otherwise distinct branches, including BCAT2, PPA2, GGH, MARK2, KIF1C, and CDK5RAP3. It contains multiple PDZ domains and is annotated for intracellular transport, tight-junction assembly, and cell polarity. Its known STRING relationship with CGN, together with kidney detection and epithelial or specialized-cell enhancement, makes it important for interpreting the module as more than a purely mitochondrial pathway. It also has extensive literature and disease associations involving brain, eye, skeletal, and developmental phenotypes.
- **Conclusion**: Established evidence supports MPDZ as a multi-interaction scaffold involved in transport, polarity, and junctional organization, with a known relationship to CGN. Its apparent bridging position suggests a possible connection between cellular architecture and mitochondrial metabolism, but that cross-branch role is a network-based hypothesis rather than a demonstrated molecular mechanism.

## Module 1

**Tissue pair**: kidney and stem_cells  
**Genes (17)**: SLC1A5, ANAPC7, ATXN2L, SLC4A2, CFAP298, FAM3C, SHMT2, LBR, NECAP2, NOMO2, OCRL, PDIA4, POGLUT3, MRPL45, POLR2D, SPG21, WASHC5

### Function

The module does not support a single strongly established biological function. No GO or KEGG term passed global multiple-testing correction, and there were no supplementary STRING enrichment terms. The co-abundance structure instead links several intracellular processes: mitochondrial translation and one-carbon metabolism through MRPL45 and SHMT2; neutral amino-acid transport through SLC1A5; endoplasmic-reticulum protein folding through PDIA4; membrane trafficking and endocytosis through OCRL and NECAP2; and nuclear, ciliary, and cell-cycle processes through genes such as LBR, CFAP298, POLR2D, and ANAPC7. The network therefore appears biologically heterogeneous rather than a canonical pathway module. Its shared kidney–stem_cells signal may reflect a shared cell state, coordinated organelle or proteostasis activity, or sample-composition effects rather than one defined pathway.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: only a minority of genes are annotated as secreted, and most genes have low immune-cell specificity. Most genes have low tissue specificity but enhanced specificity in particular cell types, including epithelial, trophoblast, neuronal, reproductive, and kidney tubular populations. A smaller subset shows immune or blood-cell associations, including OCRL, FAM3C, LBR, SPG21, and SLC1A5, but the overall HPA pattern does not support a primarily blood-cell-derived module. All module proteins were detected in kidney, whereas HPA has no matching stem-cell tissue for comparison. The mixed cell-type pattern means that shared cell populations or cellular state could contribute to the observed co-abundance.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes, and STRING provides no functional-enrichment support. This argues against the module being a densely established protein-interaction complex. The hu.MAP evidence is limited to complex C1, in which OCRL and NECAP2 occur together with many proteins not present in the module. This provides some support for an endocytic or vesicle-associated relationship involving those two genes, but the module does not reproduce the broader complex. The remaining co-abundance edges lack corresponding STRING or hu.MAP support, so they should be interpreted as expression-level relationships rather than confirmed physical interactions.

**STRING interactions (score >= 0.7)**: 0 of 136 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12394.1 (OCRL, NECAP2; 2/98)

### Novelty

The module may represent a previously unrecognized co-abundance pattern, because its complete gene set is not supported by a corresponding STRING network or a shared hu.MAP complex. However, that database absence does not establish novelty: the genes have established individual functions and several pairwise biological connections are plausible from their annotations. The lack of globally significant GO or KEGG enrichment also prevents claiming discovery of a new coherent pathway. The strongest defensible conclusion is that the kidney–stem_cells co-abundance pattern is potentially novel as a tissue-pair-specific expression module, but it requires replication, cell-composition adjustment, and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a shared regenerative or stress-adaptive cell state in which mitochondrial biosynthetic capacity and amino-acid supply are coordinated with endoplasmic-reticulum folding, membrane trafficking, and selective endocytosis. SHMT2 and SLC1A5 could support metabolic and substrate demands, PDIA4 could support folding of newly synthesized proteins, and OCRL with NECAP2 could organize trafficking or endosomal processing. The links to ciliary, nuclear-envelope, transcriptional, and cell-cycle genes may indicate that this state is especially prominent in specialized epithelial or progenitor-like cells. This is a mechanistic hypothesis, not an established pathway interpretation, because enrichment and physical-interaction evidence are limited.

### Important genes

#### OCRL

- **Related proteins** (co-abundance neighbors): MRPL45 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Microtubules, Primary cilium; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: OCRL inositol polyphosphate-5-phosphatase. This gene encodes an inositol polyphosphate 5-phosphatase. This protein is involved in regulating membrane trafficking and is located in numerous subcellular locations including the trans-Golgi network, clathrin-coated vesicles and, endosomes and the plasma membrane. This protein may also play a role in primary cilium formation. Mutations in this gene cause oculocerebrorenal syndrome of Lowe and a…
- **Diseases (Open Targets)**: oculocerebrorenal syndrome (0.864); Dent disease type 2 (0.814); Dent disease (0.740); nephrocalcinosis (0.469); hypercholesterolemia, familial, 1 (0.333)
- **Europe PMC papers**: 1458
- **Why important**: OCRL is a biologically interpretable membrane-trafficking and phosphoinositide regulator, is connected to MRPL45 in the module, and is one of the two module members represented in complex C1. Its kidney relevance is reinforced by detection in kidney and by cell-type enhancement in choroid plexus epithelial cells and Sertoli cells. It has a strong disease connection to oculocerebrorenal syndrome and Dent disease and substantial literature support.
- **Conclusion**: Established evidence supports OCRL as a kidney-relevant trafficking, phosphoinositide, and primary-cilium gene with important renal disease associations. Its participation in this module suggests that trafficking or ciliary biology may contribute to the shared signal. It is not established that OCRL physically organizes the whole module, because STRING contains no reported partners from this set and the direct co-abundance edge is not a demonstrated interaction.

#### SHMT2

- **Related proteins** (co-abundance neighbors): MRPL45 (0.84), PDIA4 (0.82), SLC1A5 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine hydroxymethyltransferase 2. This gene encodes the mitochondrial form of a pyridoxal phosphate-dependent enzyme that catalyzes the reversible reaction of serine and tetrahydrofolate to glycine and 5,10-methylene tetrahydrofolate. The encoded product is primarily responsible for glycine synthesis. The activity of the encoded protein has been suggested to be the primary source of intracellular glycine. The gene which encodes th…
- **Diseases (Open Targets)**: neurodevelopmental disorder with cardiomyopathy, spasticity, and brain abnormalities (0.771); microcephaly (0.370); polymicrogyria (0.370); neurodevelopmental disorder (0.336); hereditary disease (0.192)
- **Europe PMC papers**: 2579
- **Why important**: SHMT2 is a central metabolic enzyme in the module and connects MRPL45, PDIA4, and SLC1A5, making it one of the most connected nodes. Its established functions include mitochondrial serine and glycine metabolism, one-carbon metabolism, and regulation of oxidative phosphorylation. It has kidney protein detection, liver tissue enhancement, strong literature volume, and disease associations involving neurodevelopment and mitochondrial-related phenotypes.
- **Conclusion**: Established evidence supports SHMT2 as a mitochondrial metabolic and biosynthetic component. Its network position makes it a plausible metabolic bridge between amino-acid transport and organelle or proteostasis processes. The claim that it drives the shared module remains hypothetical because no globally significant GO or KEGG term supports a unified SHMT2-centered pathway.

#### SLC1A5

- **Related proteins** (co-abundance neighbors): SHMT2 (0.81), FAM3C (0.81), MRPL45 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 1 member 5. The SLC1A5 gene encodes a sodium-dependent neutral amino acid transporter that can act as a receptor for RD114/type D retrovirus (Larriba et al., 2001 [PubMed 11781704]).[supplied by OMIM, Jan 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.463); substance abuse (0.231); attention deficit-hyperactivity disorder (0.231); autoimmune disorder of central nervous system (0.213); hypotensive disorder (0.188)
- **Europe PMC papers**: 5038
- **Why important**: SLC1A5 is a plasma-membrane neutral amino-acid transporter connected to SHMT2, FAM3C, and MRPL45. Its documented roles in glutamine, glutamate, and serine transport provide a direct functional link to the mitochondrial metabolic activity represented by SHMT2. It is detected in kidney, has cell-type enhancement in epithelial populations, and has substantial literature volume.
- **Conclusion**: Established evidence supports SLC1A5 as a nutrient-transport component that could supply substrates for biosynthesis and stress adaptation. Its position makes metabolic coupling a credible interpretation of part of the module. It is not established that SLC1A5 explains the entire module or that the co-abundance relationship represents direct regulatory coupling.

#### PDIA4

- **Related proteins** (co-abundance neighbors): NOMO2 (0.85), SHMT2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 is an endoplasmic-reticulum protein-folding and disulfide-isomerase factor connected to SHMT2 and NOMO2. It is annotated for protein folding, secretion, and response to endoplasmic-reticulum stress, is detected in kidney, and is enhanced in several secretory or epithelial cell types. Its substantial literature and disease associations make it a strong marker of proteostasis biology within the module.
- **Conclusion**: Established evidence supports PDIA4 as an ER proteostasis component. Its connection to SHMT2 is consistent with coordination between metabolic supply and protein-folding demand, but that coordination is a hypothesis rather than a demonstrated mechanism. The module does not provide enrichment or interaction evidence sufficient to assign it an ER-stress function with confidence.

#### NECAP2

- **Related proteins** (co-abundance neighbors): CFAP298 (0.83), LBR (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: NECAP endocytosis associated 2. This gene likely encodes a member of the adaptin-ear-binding coat-associated protein family. Studies of a similar protein in rat suggest a role in clathrin-mediated endocytosis. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.431); Alzheimer disease (0.301); Parkinson disease (0.296); lysosomal storage disease (0.296); lobular capilliary hemangioma (0.146)
- **Europe PMC papers**: 132
- **Why important**: NECAP2 is annotated for clathrin-mediated endocytosis and vesicle-mediated transport and is one of the two module genes represented in complex C1. Its module connections to CFAP298 and LBR link it to genes associated with cilia or flagellar biology and the nuclear envelope, while its kidney protein detection and cell-type enhancement add tissue relevance. Its direct disease and literature evidence are more limited than for the other selected genes, making it valuable as a potentially informative but less established connector.
- **Conclusion**: Established evidence supports NECAP2 as an endocytic or vesicle-associated protein and supports its membership in a broader hu.MAP complex with OCRL. Its position suggests that endosomal trafficking could connect the module's metabolic and cellular-organization signals. A central mechanistic role for NECAP2 is presently hypothetical because the module lacks STRING support and the hu.MAP complex contains many proteins outside the module.

## Module 2

**Tissue pair**: kidney and stem_cells  
**Genes (23)**: ABHD10, AUH, COL12A1, CPT2, HSD17B11, HADHB, ETFA, GMPR2, H1-0, FECH, IDH3A, KGD4, GSTZ1, NDUFV1, BCKDHA, PDHX, NAPRT, RMDN3, SEPHS2, ALDH5A1, SUCLG1, SUCLA2, TKFC

### Function

This is a mitochondrial intermediary-metabolism and energy-production module. The strongest primary evidence is global enrichment for small-molecule metabolism (GO:BP small molecule metabolic process; q_global = 1.15e-06), broad metabolic pathways (KEGG Metabolic pathways - Homo sapiens (human); q_global = 4.06e-05), the mitochondrial matrix (GO:CC mitochondrial matrix; q_global = 5.59e-05), oxidoreductase complexes (GO:CC oxidoreductase complex; q_global = 9.35e-05), the tricarboxylic-acid-cycle enzyme complex (GO:CC tricarboxylic acid cycle heteromeric enzyme complex; q_global = 0.000236), organic and carboxylic-acid metabolism (GO:BP carboxylic acid metabolic process; q_global = 0.000251), (GO:BP organic acid metabolic process; q_global = 0.000307), (GO:BP oxoacid metabolic process; q_global = 0.000307), and mitochondrial respiration (GO:CC mitochondrion; q_global = 0.000766), (GO:BP tricarboxylic acid cycle; q_global = 0.015), (GO:BP generation of precursor metabolites and energy; q_global = 0.0153), (GO:BP cellular respiration; q_global = 0.0204), (GO:BP energy derivation by oxidation of organic compounds; q_global = 0.048). The module also contains coordinated components of amino-acid catabolism, fatty-acid oxidation, heme synthesis, NAD metabolism, redox maintenance, and oxidative phosphorylation. The result is therefore more specific than a generic housekeeping signature: it points to integrated mitochondrial carbon flux and energy generation. The co-abundance graph is connected, while the STRING-supported relationships are concentrated among enzymes and structural components of the tricarboxylic-acid cycle, pyruvate and branched-chain amino-acid oxidation, respiratory electron transfer, and fatty-acid oxidation. The global GO/KEGG evidence supports this interpretation; the STRING terms are supplementary rather than independently globally corrected evidence.

**Cell composition.** The module is overwhelmingly composed of intracellular metabolic proteins, especially mitochondrial or mitochondrial-matrix proteins, rather than plasma proteins or secreted factors. HPA reports only COL12A1 as secreted to extracellular matrix, so the module is not primarily a circulating or secreted-protein signature. Most genes have low immune-cell specificity, with only isolated immune-associated signals for HSD17B11 and IDH3A, and the blood-cell pattern does not support a dominant blood-cell contamination explanation. HPA shows frequent enrichment in liver, muscle, intestine, and epithelial or parenchymal cell types, including hepatocytes and enterocytes, which is consistent with metabolically active cells. Kidney protein detection is broad across the module, whereas there is no matching HPA tissue category for stem_cells; thus the kidney interpretation is directly supported, while the stem-cell interpretation should be treated as transcript co-abundance rather than as direct protein evidence. SUCLG1 is tissue-enhanced in kidney, but the broader HPA pattern suggests a shared metabolic cell-state program rather than a kidney-exclusive program.

**GO/KEGG enrichment**: 19 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP small molecule metabolic process | 1.15e-06 | ALDH5A1, AUH, BCKDHA, CPT2, ETFA, FECH, GMPR2, GSTZ1, HADHB, IDH3A, KGD4, NAPRT, NDUFV1, PDHX, SEPHS2, SUCLA2, SUCLG1, TKFC |
| KEGG Metabolic pathways - Homo sapiens (human) | 4.06e-05 | ALDH5A1, AUH, BCKDHA, FECH, GMPR2, GSTZ1, HADHB, HSD17B11, IDH3A, NAPRT, NDUFV1, PDHX, SEPHS2, SUCLA2, SUCLG1, TKFC |
| GO:CC mitochondrial matrix | 5.59e-05 | ABHD10, ALDH5A1, AUH, BCKDHA, ETFA, FECH, GSTZ1, HADHB, IDH3A, PDHX, SUCLA2, SUCLG1 |
| GO:CC oxidoreductase complex | 9.35e-05 | BCKDHA, GMPR2, HADHB, IDH3A, KGD4, NDUFV1, PDHX |
| GO:CC tricarboxylic acid cycle heteromeric enzyme complex | 0.000236 | IDH3A, KGD4, SUCLA2, SUCLG1 |
| GO:BP carboxylic acid metabolic process | 0.000251 | ALDH5A1, AUH, BCKDHA, CPT2, ETFA, GSTZ1, HADHB, IDH3A, KGD4, PDHX, SEPHS2, SUCLA2 |
| GO:BP organic acid metabolic process | 0.000307 | ALDH5A1, AUH, BCKDHA, CPT2, ETFA, GSTZ1, HADHB, IDH3A, KGD4, PDHX, SEPHS2, SUCLA2 |
| GO:BP oxoacid metabolic process | 0.000307 | ALDH5A1, AUH, BCKDHA, CPT2, ETFA, GSTZ1, HADHB, IDH3A, KGD4, PDHX, SEPHS2, SUCLA2 |
| GO:CC mitochondrion | 0.000766 | ABHD10, ALDH5A1, AUH, BCKDHA, CPT2, ETFA, FECH, GSTZ1, HADHB, IDH3A, KGD4, NDUFV1, PDHX, RMDN3, SUCLA2, SUCLG1 |
| GO:BP small molecule catabolic process | 0.00535 | ALDH5A1, AUH, BCKDHA, CPT2, ETFA, GSTZ1, HADHB, TKFC |
| GO:BP organic acid catabolic process | 0.00751 | ALDH5A1, AUH, BCKDHA, CPT2, ETFA, GSTZ1, HADHB |
| GO:BP carboxylic acid catabolic process | 0.00751 | ALDH5A1, AUH, BCKDHA, CPT2, ETFA, GSTZ1, HADHB |
| GO:BP tricarboxylic acid cycle | 0.015 | IDH3A, KGD4, SUCLA2, SUCLG1 |
| GO:BP generation of precursor metabolites and energy | 0.0153 | ETFA, FECH, IDH3A, KGD4, NDUFV1, PDHX, SUCLA2, SUCLG1 |
| GO:MF oxidoreductase activity | 0.0173 | ALDH5A1, BCKDHA, ETFA, GMPR2, GSTZ1, HADHB, HSD17B11, IDH3A, NDUFV1 |

### STRING and hu.MAP

STRING provides established support for a mitochondrial metabolic network. Strong relationships include the SUCLA2–SUCLG1 succinate-CoA ligase pair, IDH3A connections to SUCLA2 and SUCLG1, PDHX connections to BCKDHA, SUCLA2, and SUCLG1, and HADHB connections to ETFA, SUCLA2, and SUCLG1. These links are concordant with known enzyme complexes and pathway adjacency, so they strengthen the view that the co-abundance signal reflects coordinated mitochondrial metabolism rather than an arbitrary gene grouping. The STRING enrichment for mitochondrial localization, metabolism, carboxylic-acid metabolism, and inherited metabolic disorders is supportive but supplementary. hu.MAP supplies a more limited direct complex result: (hu.MAP huMAP3_12248.1) contains PDHX, BCKDHA, and KGD4 together with additional pyruvate and alpha-ketoglutarate dehydrogenase-related components and regulatory proteins. The limited hu.MAP overlap does not invalidate the module; it indicates that much of the module is pathway-coherent without being represented as a single experimentally assembled complex. Co-abundance should not be interpreted as proof of physical interaction for every pair.

**STRING interactions (score >= 0.7)**: 19 of 253 gene pairs: ALDH5A1–IDH3A (0.86); AUH–HADHB (0.7); BCKDHA–IDH3A (0.714); BCKDHA–PDHX (0.951); BCKDHA–SUCLA2 (0.758); BCKDHA–SUCLG1 (0.775); CPT2–HADHB (0.808); ETFA–HADHB (0.829); ETFA–SUCLG1 (0.956); HADHB–SUCLA2 (0.915); HADHB–SUCLG1 (0.94); IDH3A–NDUFV1 (0.722); IDH3A–PDHX (0.763); IDH3A–SUCLA2 (0.972); IDH3A–SUCLG1 (0.902); NDUFV1–SUCLG1 (0.836); PDHX–SUCLA2 (0.892); PDHX–SUCLG1 (0.936); SUCLA2–SUCLG1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transit peptide (FDR = 2.83e-07, 13 genes); RCTM Metabolism (FDR = 7.44e-07, 18 genes); Process Small molecule metabolic process (FDR = 3.62e-06, 17 genes); Component Mitochondrial matrix (FDR = 5.01e-06, 12 genes); COMPARTMENTS Mitochondrion (FDR = 8.67e-06, 15 genes); Keyword Mitochondrion (FDR = 9.48e-06, 14 genes); HPO Abnormal urine carboxylic acid level (FDR = 1.79e-05, 8 genes); DISEASES Inherited metabolic disorder (FDR = 3.62e-05, 13 genes); KEGG Metabolic pathways (FDR = 4.89e-05, 14 genes); HPO Acidosis (FDR = 6.36e-05, 10 genes); COMPARTMENTS Mitochondrial matrix (FDR = 8.52e-05, 10 genes); HPO Lactic acidosis (FDR = 8.74e-05, 8 genes); Component Mitochondrion (FDR = 9.57e-05, 15 genes); DISEASES Amino acid metabolic disorder (FDR = 0.00016, 7 genes); Process Carboxylic acid metabolic process (FDR = 0.00022, 12 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12248.1 (PDHX, BCKDHA, KGD4; 3/22)

### Novelty

The module is plausibly a new tissue-pair co-abundance finding, but its underlying biology is not novel in the strong sense. Its central processes, including the tricarboxylic-acid cycle, branched-chain amino-acid catabolism, fatty-acid oxidation, respiratory electron transfer, and heme synthesis, are established. Several relationships are already represented in STRING, and (hu.MAP huMAP3_12248.1) provides partial hu.MAP support. The potentially novel aspect is the coordinated occurrence of this particular metabolic gene set across kidney and stem_cells, including less connected genes such as ABHD10, NAPRT, RMDN3, and KGD4, rather than discovery of a new biochemical pathway. Database incompleteness, tissue sampling, and the difference between co-abundance and physical interaction prevent absence from STRING or hu.MAP from demonstrating novelty. The appropriate conclusion is therefore a potentially novel cross-tissue module organization built from largely known mitochondrial biology.

**Hypothesis.** Hypothesis: the shared module represents a conserved mitochondrial metabolic state in which stem-like and kidney-associated cells coordinate carbon entry, oxidative metabolism, redox balance, and biosynthetic capacity. PDHX and BCKDHA may couple pyruvate and branched-chain amino-acid catabolism to the tricarboxylic-acid cycle; IDH3A, SUCLG1, and SUCLA2 may maintain cycle flux and nucleotide-level energy exchange; ETFA, HADHB, and CPT2 may provide lipid-derived reducing equivalents; NDUFV1 may couple reducing equivalents to respiratory-chain activity; and FECH, NAPRT, SEPHS2, and GSTZ1 may support heme, NAD, selenium-dependent, and detoxification functions. This is a mechanistic model inferred from coordinated abundance and annotations, not evidence that the module physically operates as one complex or that it has a unique stem-cell-specific function.

### Important genes

#### SUCLG1

- **Related proteins** (co-abundance neighbors): ALDH5A1 (0.85); STRING partners: BCKDHA (0.775), ETFA (0.956), HADHB (0.94), IDH3A (0.902), NDUFV1 (0.836), PDHX (0.936), SUCLA2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase GDP/ADP-forming subunit alpha. This gene encodes the alpha subunit of the heterodimeric enzyme succinate coenzyme A ligase. This enzyme is targeted to the mitochondria and catalyzes the conversion of succinyl CoA and ADP or GDP to succinate and ATP or GTP. Mutations in this gene are the cause of the metabolic disorder fatal infantile lactic acidosis and mitochondrial DNA depletion. [provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome 9 (0.811); neurodegenerative disease (0.520); mitochondrial DNA depletion syndrome (0.507); post term pregnancy (0.280); lysosomal storage disease (0.245)
- **Europe PMC papers**: 1277
- **Why important**: SUCLG1 is a central anchor of the mitochondrial network through its STRING relationships with BCKDHA, ETFA, HADHB, IDH3A, NDUFV1, PDHX, and SUCLA2. It is the alpha subunit of succinate-CoA ligase and is present in globally supported tricarboxylic-acid-cycle, mitochondrial, respiration, and energy-generation terms (GO:BP small molecule metabolic process; q_global = 1.15e-06), (KEGG Metabolic pathways - Homo sapiens (human); q_global = 4.06e-05), (GO:CC mitochondrial matrix; q_global = 5.59e-05), (GO:CC tricarboxylic acid cycle heteromeric enzyme complex; q_global = 0.000236), (GO:CC mitochondrion; q_global = 0.000766), (GO:BP tricarboxylic acid cycle; q_global = 0.015), (GO:BP generation of precursor metabolites and energy; q_global = 0.0153), (GO:BP cellular respiration; q_global = 0.0204), (GO:BP energy derivation by oxidation of organic compounds; q_global = 0.048). Its kidney tissue enhancement is especially relevant to the tissue pair. Its disease associations include mitochondrial DNA depletion and neurodegenerative disease, and it has substantial literature support.
- **Conclusion**: Established evidence supports SUCLG1 as a core tricarboxylic-acid-cycle and energy-metabolism component with strong network connectivity and kidney relevance. It is a credible molecular anchor of the module. The hypothesis that altered SUCLG1 abundance organizes the broader cross-tissue metabolic state remains to be tested.

#### IDH3A

- **Related proteins** (co-abundance neighbors): SUCLA2 (0.81), ETFA (0.80); STRING partners: ALDH5A1 (0.86), BCKDHA (0.714), NDUFV1 (0.722), PDHX (0.763), SUCLA2 (0.972), SUCLG1 (0.902)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: isocitrate dehydrogenase (NAD(+)) 3 catalytic subunit alpha. Isocitrate dehydrogenases catalyze the oxidative decarboxylation of isocitrate to 2-oxoglutarate. These enzymes belong to two distinct subclasses, one of which utilizes NAD(+) as the electron acceptor and the other NADP(+). Five isocitrate dehydrogenases have been reported: three NAD(+)-dependent isocitrate dehydrogenases, which localize to the mitochondrial matrix, and two NADP(+)-dependent isoci…
- **Diseases (Open Targets)**: retinitis pigmentosa 90 (0.791); retinitis pigmentosa (0.467); neurodegenerative disease (0.437); inherited retinal dystrophy (0.381); colorectal carcinoma (0.182)
- **Europe PMC papers**: 1497
- **Why important**: IDH3A is a catalytic mitochondrial isocitrate dehydrogenase subunit and is represented across nearly all of the module's central metabolic evidence, including the tricarboxylic-acid cycle, mitochondrial matrix, oxidoreductase complex, respiration, and energy generation (GO:BP small molecule metabolic process; q_global = 1.15e-06) through (GO:CC tricarboxylic acid cycle heteromeric enzyme complex; q_global = 0.000236), (GO:CC mitochondrion; q_global = 0.000766), (GO:BP tricarboxylic acid cycle; q_global = 0.015), (GO:BP generation of precursor metabolites and energy; q_global = 0.0153), (GO:BP cellular respiration; q_global = 0.0204), and (GO:BP energy derivation by oxidation of organic compounds; q_global = 0.048). It has strong STRING connectivity to ALDH5A1, BCKDHA, NDUFV1, PDHX, SUCLA2, and SUCLG1, placing it at the interface of carbon oxidation and respiratory metabolism. Its disease associations include inherited retinal disease and neurodegenerative disease, with extensive literature support.
- **Conclusion**: Established evidence identifies IDH3A as a central catalytic link between tricarboxylic-acid-cycle flux and mitochondrial redox metabolism. Its inclusion is mechanistically compelling. A specific role in maintaining stem-cell properties or kidney function is a hypothesis rather than an established conclusion from this module.

#### PDHX

- **Related proteins** (co-abundance neighbors): RMDN3 (0.87), GSTZ1 (0.81); STRING partners: BCKDHA (0.951), IDH3A (0.763), SUCLA2 (0.892), SUCLG1 (0.936)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_12248.1
- **Function (MyGene.info)**: pyruvate dehydrogenase complex component X. The pyruvate dehydrogenase (PDH) complex is located in the mitochondrial matrix and catalyzes the conversion of pyruvate to acetyl coenzyme A. The PDH complex thereby links glycolysis to Krebs cycle. The PDH complex contains three catalytic subunits, E1, E2, and E3, two regulatory subunits, E1 kinase and E1 phosphatase, and a non-catalytic subunit, E3 binding protein (E3BP). This gene encodes the …
- **Diseases (Open Targets)**: pyruvate dehydrogenase E3-binding protein deficiency (0.793); hereditary disease (0.453); mitochondrial disease (0.445); Leigh syndrome (0.371); ovarian dysfunction (0.269)
- **Europe PMC papers**: 976
- **Why important**: PDHX links glycolytic pyruvate entry to mitochondrial acetyl-CoA production as the E3-binding component of the pyruvate dehydrogenase complex. It has strong STRING relationships with BCKDHA, IDH3A, SUCLA2, and SUCLG1 and participates in the hu.MAP complex (hu.MAP huMAP3_12248.1). It is represented in the globally supported metabolic, mitochondrial, oxidoreductase, respiration, and alpha-ketoacid-dehydrogenase terms (GO:BP small molecule metabolic process; q_global = 1.15e-06) through (GO:CC oxidoreductase complex; q_global = 9.35e-05), (GO:BP carboxylic acid metabolic process; q_global = 0.000251) through (GO:CC mitochondrion; q_global = 0.000766), (GO:BP generation of precursor metabolites and energy; q_global = 0.0153), (GO:BP cellular respiration; q_global = 0.0204), (GO:CC alpha-ketoacid dehydrogenase complex; q_global = 0.0479), and (GO:BP energy derivation by oxidation of organic compounds; q_global = 0.048). Its disease associations include PDH deficiency, mitochondrial disease, and Leigh syndrome, with substantial literature support.
- **Conclusion**: Established evidence supports PDHX as a structural and pathway-level bridge between pyruvate oxidation and the tricarboxylic-acid cycle. Its network and hu.MAP placement make it one of the strongest module interpreters. Whether PDHX is a limiting regulator of the observed co-abundance state is a hypothesis.

#### BCKDHA

- **Related proteins** (co-abundance neighbors): ABHD10 (0.82); STRING partners: IDH3A (0.714), PDHX (0.951), SUCLA2 (0.758), SUCLG1 (0.775)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_12248.1
- **Function (MyGene.info)**: branched chain keto acid dehydrogenase E1 subunit alpha. The branched-chain alpha-keto acid (BCAA) dehydrogenase (BCKD) complex is an innter mitochondrial enzyme complex that catalyzes the second major step in the catabolism of the branched-chain amino acids leucine, isoleucine, and valine. The BCKD complex consists of three catalytic components: a heterotetrameric (alpha2-beta2) branched-chain alpha-keto acid decarboxylase (E1), a dihydrolipoyl transac…
- **Diseases (Open Targets)**: maple syrup urine disease type 1A (0.840); maple syrup urine disease (0.758); hereditary disease (0.508); refractive error (0.387); classic maple syrup urine disease (0.370)
- **Europe PMC papers**: 1111
- **Why important**: BCKDHA is a catalytic component of the branched-chain alpha-ketoacid dehydrogenase complex and connects branched-chain amino-acid catabolism with the mitochondrial carbon economy. It is part of (hu.MAP huMAP3_12248.1) and has strong STRING relationships with PDHX, SUCLA2, SUCLG1, and IDH3A. It contributes to globally supported metabolic, mitochondrial-matrix, oxidoreductase, amino-acid-catabolic, and alpha-ketoacid-dehydrogenase terms (GO:BP small molecule metabolic process; q_global = 1.15e-06) through (GO:CC oxidoreductase complex; q_global = 9.35e-05), (GO:BP carboxylic acid metabolic process; q_global = 0.000251) through (GO:CC mitochondrion; q_global = 0.000766), (GO:BP small molecule catabolic process; q_global = 0.00535) through (GO:BP carboxylic acid catabolic process; q_global = 0.00751), (GO:MF oxidoreductase activity; q_global = 0.0173), (GO:BP amino acid catabolic process; q_global = 0.0211), and (GO:CC alpha-ketoacid dehydrogenase complex; q_global = 0.0479). Its association with maple syrup urine disease and its substantial literature establish strong biomedical relevance.
- **Conclusion**: Established evidence supports BCKDHA as a major amino-acid catabolic entry point into the mitochondrial metabolic network. Its inclusion indicates that the module integrates amino-acid oxidation rather than representing only the tricarboxylic-acid cycle. A preferential role for BCKDHA in the shared kidney–stem-cell state remains a hypothesis.

#### NDUFV1

- **Related proteins** (co-abundance neighbors): ALDH5A1 (0.84), SEPHS2 (0.80); STRING partners: IDH3A (0.722), SUCLG1 (0.836)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit V1. The mitochondrial respiratory chain provides energy to cells via oxidative phosphorylation and consists of four membrane-bound electron-transporting protein complexes (I-IV) and an ATP synthase (complex V). This gene encodes a 51 kDa subunit of the NADH:ubiquinone oxidoreductase complex I; a large complex with at least 45 nuclear and mitochondrial encoded subunits that liberates electrons from NAD…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.788); mitochondrial complex I deficiency, nuclear type 4 (0.724); mitochondrial complex I deficiency, nuclear type 1 (0.685); Leigh syndrome (0.635); type 2 diabetes mellitus (0.609)
- **Europe PMC papers**: 4567
- **Why important**: NDUFV1 is a core subunit of respiratory-chain complex I and provides a direct link between upstream mitochondrial metabolism and electron transport. It is connected in STRING to IDH3A and SUCLG1 and appears in globally supported terms for metabolic pathways, the mitochondrial matrix, oxidoreductase activity, cellular respiration, and energy derivation (GO:BP small molecule metabolic process; q_global = 1.15e-06), (KEGG Metabolic pathways - Homo sapiens (human); q_global = 4.06e-05), (GO:CC oxidoreductase complex; q_global = 9.35e-05), (GO:CC mitochondrion; q_global = 0.000766), (GO:BP generation of precursor metabolites and energy; q_global = 0.0153) through (GO:BP cellular respiration; q_global = 0.0204), and (GO:BP energy derivation by oxidation of organic compounds; q_global = 0.048). Its associations with complex I deficiency, Leigh syndrome, and diabetes, together with very extensive literature support, make it an important functional readout of respiratory capacity.
- **Conclusion**: Established evidence supports NDUFV1 as the respiratory-chain component of a broader oxidative-metabolism program. It helps explain why the module extends beyond substrate catabolism to energy conversion. The hypothesis that NDUFV1 abundance is coordinated with upstream carbon flux in these tissues requires functional and perturbation testing.

## Module 3

**Tissue pair**: kidney and stem_cells  
**Genes (50)**: ACSF2, ACY1, ADD3, ALDH1B1, ALDH2, ASS1, CMBL, CWC22, DCPS, DCTN1, DCXR, DHRS4, SORD, EIF2AK2, ETFDH, GLRX, HADH, HIBCH, HSPBP1, KIF23, MFGE8, MIPEP, PRORP, MRI1, MME, ORC5, PCCA, PCCB, PCK2, PEPD, PTGR1, UQCRC2, CRYZ, MRPS22, SLC27A2, SCAMP1, SDHA, SEPTIN8, STAMBP, SUOX, SUZ12, DARS1, DARS2, TAP2, ACAT1, MPST, TST, TTC38, RP2, ZW10

### Function

The module is best interpreted as a mitochondrial metabolic module centered on degradation and processing of small, organic, carboxylic, monocarboxylic, fatty-acid, and amino-acid substrates. The strongest primary evidence is the coordinated enrichment for small-molecule catabolism (GO:BP small molecule catabolic process; q_global = 4.89e-05), organic- and carboxylic-acid catabolism (GO:BP organic acid catabolic process; q_global = 9.92e-05)(GO:BP carboxylic acid catabolic process; q_global = 9.92e-05), and mitochondrial matrix localization (GO:CC mitochondrial matrix; q_global = 0.000101), with additional support for mitochondrial localization (GO:CC mitochondrion; q_global = 0.000657), carboxylic-acid metabolism (GO:BP carboxylic acid metabolic process; q_global = 0.000727)(GO:BP organic acid metabolic process; q_global = 0.000943)(GO:BP oxoacid metabolic process; q_global = 0.000943), branched-chain amino-acid degradation (KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 0.00362), fatty-acid catabolism (GO:BP fatty acid catabolic process; q_global = 0.0128)(GO:BP fatty acid metabolic process; q_global = 0.0326)(GO:BP monocarboxylic acid metabolic process; q_global = 0.0399), and tryptophan metabolism (KEGG Tryptophan metabolism - Homo sapiens (human); q_global = 0.0453). The module also contains a broad catalytic-activity signal (GO:MF catalytic activity; q_global = 0.00905). Together, these findings indicate coordinated mitochondrial substrate oxidation rather than a narrowly specialized single pathway. The module includes a particularly coherent propionyl-CoA and branched-chain substrate component involving PCCA, PCCB, HIBCH, ACAT1, HADH, and ETFDH, alongside aldehyde, sulfur-compound, polyol, amino-acid, and respiratory functions. The co-abundance graph is relatively sparse and appears to contain a strongly connected metabolic core plus peripheral branches involving mitochondrial RNA processing, translation, trafficking, cytoskeletal, cell-cycle, and immune-related genes. Those peripheral genes may reflect shared cellular state or tissue composition rather than a single biochemical complex.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: HPA identifies only MFGE8 as secreted to blood, while the other genes are not secreted. It is also not dominated by blood-cell markers. Most genes have low immune-cell specificity, although a minority show immune-cell-enhanced or immune-cell-enriched patterns, including genes associated with dendritic cells, basophils, eosinophils, monocytes, or neutrophils. The stronger compositional signal is epithelial and metabolic: HPA repeatedly points to liver, kidney, intestine, hepatocytes, enterocytes, and proximal tubule cells. Kidney protein detection is widespread across the module, whereas HPA has no matching stem-cell tissue category for protein detection. Thus, the shared kidney/stem-cell module is more consistent with a conserved oxidative-metabolism or epithelial-like cellular program than with a blood contamination explanation, although minor immune or stromal contributions cannot be excluded. MFGE8 may represent a vascular, stromal, or extracellular component embedded in an otherwise intracellular metabolic module.

**GO/KEGG enrichment**: 18 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP small molecule catabolic process | 4.89e-05 | ACAT1, ALDH1B1, ALDH2, DCXR, ETFDH, HADH, HIBCH, MPST, PCCA, PCCB, PCK2, SLC27A2, SORD, TST |
| GO:BP organic acid catabolic process | 9.92e-05 | ACAT1, DCXR, ETFDH, HADH, HIBCH, MPST, PCCA, PCCB, PCK2, SLC27A2, SORD, TST |
| GO:BP carboxylic acid catabolic process | 9.92e-05 | ACAT1, DCXR, ETFDH, HADH, HIBCH, MPST, PCCA, PCCB, PCK2, SLC27A2, SORD, TST |
| GO:CC mitochondrial matrix | 0.000101 | ACAT1, ACSF2, ALDH1B1, ALDH2, DARS2, HADH, HIBCH, MIPEP, MPST, MRPS22, PCCA, PCCB, PCK2, PRORP, SDHA, SUOX, TST |
| GO:BP monocarboxylic acid catabolic process | 0.000389 | ACAT1, DCXR, ETFDH, HADH, PCCA, PCCB, PCK2, SLC27A2, SORD |
| GO:CC mitochondrion | 0.000657 | ACAT1, ACSF2, ALDH1B1, ALDH2, ASS1, CRYZ, DARS2, DCPS, DCXR, DHRS4, ETFDH, HADH, HIBCH, KIF23, MIPEP, MPST, MRPS22, PCCA, PCCB, PCK2, PRORP, SDHA, SORD, SUOX, TST, UQCRC2 |
| GO:BP carboxylic acid metabolic process | 0.000727 | ACAT1, ACSF2, ASS1, DCXR, ETFDH, HADH, HIBCH, MPST, MRI1, PCCA, PCCB, PCK2, PTGR1, SDHA, SLC27A2, SORD, TST |
| GO:BP organic acid metabolic process | 0.000943 | ACAT1, ACSF2, ASS1, DCXR, ETFDH, HADH, HIBCH, MPST, MRI1, PCCA, PCCB, PCK2, PTGR1, SDHA, SLC27A2, SORD, TST |
| GO:BP oxoacid metabolic process | 0.000943 | ACAT1, ACSF2, ASS1, DCXR, ETFDH, HADH, HIBCH, MPST, MRI1, PCCA, PCCB, PCK2, PTGR1, SDHA, SLC27A2, SORD, TST |
| KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human) | 0.00362 | ACAT1, ALDH1B1, ALDH2, HADH, HIBCH, PCCA, PCCB |
| GO:BP small molecule metabolic process | 0.00483 | ACAT1, ACSF2, ALDH1B1, ALDH2, ASS1, DCXR, DHRS4, ETFDH, GLRX, HADH, HIBCH, MME, MPST, MRI1, PCCA, PCCB, PCK2, PTGR1, SDHA, SLC27A2, SORD, TST |
| GO:BP amino acid metabolic process | 0.00544 | ACAT1, ACY1, ASS1, DARS1, DARS2, HIBCH, MPST, MRI1, PCCA, PCCB, PEPD |
| GO:MF catalytic activity | 0.00905 | ACAT1, ACSF2, ACY1, ALDH1B1, ALDH2, ASS1, CMBL, CRYZ, DARS1, DARS2, DCPS, DCXR, DHRS4, EIF2AK2, ETFDH, GLRX, HADH, HIBCH, KIF23, MIPEP, MME, MPST, MRI1, PCCA, PCCB, PCK2, PEPD, PRORP, PTGR1, SDHA, SEPTIN8, SLC27A2, SORD, STAMBP, SUOX, TAP2, TST, UQCRC2 |
| GO:BP fatty acid catabolic process | 0.0128 | ACAT1, ETFDH, HADH, PCCA, PCCB, PCK2, SLC27A2 |
| GO:BP short-chain fatty acid catabolic process | 0.0295 | PCCA, PCCB, PCK2 |

### STRING and hu.MAP

STRING supports several established biochemical relationships. The PCCA-PCCB pair is a known propionyl-CoA carboxylase relationship, and both genes connect to ALDH1B1 and ALDH2 in the STRING network. ACAT1 connects to HADH, HIBCH, and SDHA; DCXR connects to SORD; MPST connects to SUOX and TST; and SDHA connects to UQCRC2. DARS1-DARS2 and DCTN1-ZW10 provide additional known links outside the central metabolic core. The STRING functional results independently support mitochondrial matrix and mitochondrial localization (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 1.63e-05)(STRING Component Mitochondrial matrix; within-query FDR = 2.89e-05)(STRING Keyword Transit peptide; within-query FDR = 0.00019)(STRING Component Mitochondrion; within-query FDR = 0.00031)(STRING Keyword Mitochondrion; within-query FDR = 0.00038)(STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.00054), small-molecule and carboxylic-acid metabolism (STRING Process Small molecule metabolic process; within-query FDR = 5.97e-05)(STRING Process Carboxylic acid metabolic process; within-query FDR = 7.82e-05)(STRING Process Small molecule catabolic process; within-query FDR = 0.00026)(STRING RCTM Metabolism; within-query FDR = 0.0018)(STRING Process Organic acid catabolic process; within-query FDR = 0.0025), and a mixed glutathione or reactive-oxygen-species-related neighborhood (STRING NetworkNeighborAL Mixed, incl. Glutathione metabolism, and Detoxification of Reactive Oxygen Species; within-query FDR = 0.0068). These are supplementary within-query findings, not additional globally corrected evidence. hu.MAP provides complementary support for partially overlapping mitochondrial assemblies. The complexes containing PRORP, PCCA, PCCB, CRYZ, PCK2, DARS2, and ACSF2, as well as the repeated ALDH2-ALDH1B1 and PCCA-ACSF2 associations, indicate that some module members participate in known multi-protein assemblies. The PCCA-PCCB and ALDH2-ALDH1B1 pairings are especially consistent with established biochemical organization. However, most module edges are not represented as direct STRING or hu.MAP relationships, so co-abundance should not be interpreted as physical interaction for the entire module.

**STRING interactions (score >= 0.7)**: 20 of 1225 gene pairs: ACAT1–HADH (0.935); ACAT1–HIBCH (0.751); ACAT1–SDHA (0.762); ACY1–ASS1 (0.844); ADD3–MRI1 (0.796); ALDH1B1–ALDH2 (0.945); ALDH1B1–PCCA (0.821); ALDH1B1–PCCB (0.832); ALDH2–PCCA (0.844); ALDH2–PCCB (0.843); CMBL–HADH (0.795); DARS1–DARS2 (0.96); DCTN1–ZW10 (0.719); DCXR–SORD (0.945); HIBCH–PCCB (0.701); MPST–SUOX (0.977); MPST–TST (0.929); PCCA–PCCB (0.999); SDHA–UQCRC2 (0.99); SUOX–TST (0.982)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Mitochondrial matrix (FDR = 1.63e-05, 16 genes); Component Mitochondrial matrix (FDR = 2.89e-05, 17 genes); Process Small molecule metabolic process (FDR = 5.97e-05, 26 genes); Process Carboxylic acid metabolic process (FDR = 7.82e-05, 19 genes); Keyword Transit peptide (FDR = 0.00019, 16 genes); Process Small molecule catabolic process (FDR = 0.00026, 13 genes); Component Mitochondrion (FDR = 0.00031, 24 genes); Keyword Mitochondrion (FDR = 0.00038, 20 genes); COMPARTMENTS Mitochondrion (FDR = 0.00054, 21 genes); RCTM Metabolism (FDR = 0.0018, 25 genes); Process Cellular amino acid metabolic process (FDR = 0.002, 12 genes); Process Organic acid catabolic process (FDR = 0.0025, 10 genes); TISSUES Liver (FDR = 0.0031, 28 genes); Function Catalytic activity (FDR = 0.0039, 38 genes); NetworkNeighborAL Mixed, incl. Glutathione metabolism, and Detoxification of Reactive Oxygen Species (FDR = 0.0068, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (PRORP, PCCA, PCCB, CRYZ, PCK2, DARS2, ACSF2; 7/99); huMAP3_10458.1 (PRORP, PCCA, PCCB; 3/16); huMAP3_10525.1 (CRYZ, DARS2, ACSF2; 3/33); huMAP3_05942.1 (ALDH2, ALDH1B1; 2/2); huMAP3_08696.1 (PCCA, ACSF2; 2/3); huMAP3_12502.1 (ALDH2, ALDH1B1; 2/3); huMAP3_07052.1 (CRYZ, PCK2; 2/3); huMAP3_09437.1 (PCCA, ACSF2; 2/4); huMAP3_10569.1 (ALDH2, ALDH1B1; 2/4); huMAP3_07028.1 (PCCA, PCCB; 2/4); huMAP3_00213.1 (CRYZ, PCK2; 2/4); huMAP3_10334.1 (CRYZ, PCK2; 2/6); huMAP3_09668.1 (CRYZ, DARS2; 2/8); huMAP3_11232.1 (ZW10, ORC5; 2/78)

### Novelty

The biochemical interpretation is not wholly new: many central relationships, enzyme functions, mitochondrial localizations, and disease links are already established in STRING, hu.MAP, and the gene annotations. The module therefore looks more like a newly identified cross-tissue co-abundance configuration of known mitochondrial metabolic machinery than a discovery of a new enzyme complex or new pathway. Its potentially novel aspect is the coordinated conservation of this broader metabolic program across kidney and stem_cells, including the way a propionyl-CoA and fatty-acid oxidation core co-abundantly associates with amino-acid, aldehyde, sulfur, mitochondrial information-processing, and selected cellular-state genes. That cross-tissue organization requires independent validation and should not be called a new biological mechanism solely because many edges are absent from STRING or hu.MAP. The absence of prior database representation is evidence of limited prior annotation, not proof of novelty.

**Hypothesis.** Hypothesis: this conserved module represents a mitochondrial metabolic-capacity program that enables cells in kidney and stem-cell contexts to process branched-chain amino acids, propionyl-CoA, fatty acids, organic acids, aldehydes, and related small molecules while maintaining respiratory and redox balance. PCCA and PCCB could form a propionyl-CoA-processing hub, with ACAT1, HADH, HIBCH, and ETFDH connecting substrate breakdown to mitochondrial electron transfer. PCK2, ALDH2, ALDH1B1, MPST, TST, and SUOX could extend the program into carbon redistribution, aldehyde detoxification, and sulfur-compound handling. PRORP, DARS2, MRPS22, and MIPEP may indicate that mitochondrial RNA processing, translation, and protein maturation are co-regulated to support this metabolic demand. The peripheral trafficking, cytoskeletal, cell-cycle, and immune-associated genes may reflect the cellular state or mixture of cell types in which the metabolic program is active. This hypothesis predicts coordinated changes in mitochondrial substrate flux and respiratory capacity, but co-abundance alone does not establish causal regulation or direct physical interaction.

### Important genes

#### ACAT1

- **Related proteins** (co-abundance neighbors): ASS1 (0.83), PCCA (0.82), ACSF2 (0.82), SLC27A2 (0.81); STRING partners: HADH (0.935), HIBCH (0.751), SDHA (0.762)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA acetyltransferase 1. This gene encodes a mitochondrially localized enzyme that catalyzes the reversible formation of acetoacetyl-CoA from two molecules of acetyl-CoA. Defects in this gene are associated with 3-ketothiolase deficiency, an inborn error of isoleucine catabolism characterized by urinary excretion of 2-methyl-3-hydroxybutyric acid, 2-methylacetoacetic acid, tiglylglycine, and butanone. [provided by RefSeq,…
- **Diseases (Open Targets)**: beta-ketothiolase deficiency (0.817); hereditary disease (0.470); Abnormality of the skeletal system (0.239); neoplasm (0.115); nonpapillary renal cell carcinoma (0.105)
- **Europe PMC papers**: 4147
- **Why important**: ACAT1 is a central metabolic connector in the module and is represented across nearly all primary metabolic terms, including small-molecule, organic-acid, fatty-acid, branched-chain amino-acid, and tryptophan-related annotations (GO:BP small molecule catabolic process; q_global = 4.89e-05)(GO:BP organic acid catabolic process; q_global = 9.92e-05)(GO:BP carboxylic acid catabolic process; q_global = 9.92e-05)(GO:BP monocarboxylic acid catabolic process; q_global = 0.000389)(GO:BP carboxylic acid metabolic process; q_global = 0.000727)(KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 0.00362)(GO:BP fatty acid catabolic process; q_global = 0.0128)(GO:BP fatty acid metabolic process; q_global = 0.0326)(KEGG Tryptophan metabolism - Homo sapiens (human); q_global = 0.0453). It is mitochondrial, enriched in kidney and liver, and has established functions in acetoacetyl-CoA formation, isoleucine catabolism, and fatty-acid beta-oxidation. STRING links it to HADH, HIBCH, and SDHA, placing it at the interface of substrate breakdown and respiratory metabolism. Its extensive literature and disease association with beta-ketothiolase deficiency make it a strong biological anchor.
- **Conclusion**: Established: ACAT1 is a mitochondrial metabolic enzyme and a strong marker of the module's catabolic core. Hypothesis: its co-abundance may report coordinated regulation of acetyl-CoA and branched-chain substrate utilization across the two tissue contexts.

#### PCCA

- **Related proteins** (co-abundance neighbors): ALDH2 (0.86), ACAT1 (0.82); STRING partners: ALDH1B1 (0.821), ALDH2 (0.844), PCCB (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10458.1, huMAP3_08696.1, huMAP3_09437.1, huMAP3_07028.1
- **Function (MyGene.info)**: propionyl-CoA carboxylase subunit alpha. The protein encoded by this gene is the alpha subunit of the heterodimeric mitochondrial enzyme Propionyl-CoA carboxylase. PCCA encodes the biotin-binding region of this enzyme. Mutations in either PCCA or PCCB (encoding the beta subunit) lead to an enzyme deficiency resulting in propionic acidemia. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by…
- **Diseases (Open Targets)**: propionic acidemia (0.853); hereditary disease (0.487); dilated cardiomyopathy (0.370); neurodegenerative disease (0.357); pontocerebellar hypoplasia type 2D (0.340)
- **Europe PMC papers**: 2633
- **Why important**: PCCA is one half of the propionyl-CoA carboxylase enzyme and is repeatedly represented in the primary enrichment profile, including small-molecule, organic-acid, fatty-acid, amino-acid, and short-chain fatty-acid catabolism (GO:BP small molecule catabolic process; q_global = 4.89e-05)(GO:BP organic acid catabolic process; q_global = 9.92e-05)(GO:BP monocarboxylic acid catabolic process; q_global = 0.000389)(KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 0.00362)(GO:BP amino acid metabolic process; q_global = 0.00544)(GO:BP fatty acid catabolic process; q_global = 0.0128)(GO:BP short-chain fatty acid catabolic process; q_global = 0.0295)(GO:BP fatty acid metabolic process; q_global = 0.0326)(GO:BP monocarboxylic acid metabolic process; q_global = 0.0399). It has strong module connectivity and is linked in STRING to PCCB, ALDH1B1, and ALDH2. hu.MAP places it in several mitochondrial assemblies, including complexes shared with PCCB, PCK2, PRORP, CRYZ, DARS2, and ACSF2. Its kidney detection and established association with propionic acidemia provide both tissue relevance and disease validation.
- **Conclusion**: Established: PCCA is a core propionyl-CoA-processing enzyme with known PCCB partnership and mitochondrial complex support. Hypothesis: PCCA may organize the module's branched-chain and short-chain substrate-processing axis rather than merely track general mitochondrial abundance.

#### PCCB

- **Related proteins** (co-abundance neighbors): HADH (0.84); STRING partners: ALDH1B1 (0.832), ALDH2 (0.843), HIBCH (0.701), PCCA (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10458.1, huMAP3_07028.1
- **Function (MyGene.info)**: propionyl-CoA carboxylase subunit beta. The protein encoded by this gene is a subunit of the propionyl-CoA carboxylase (PCC) enzyme, which is involved in the catabolism of propionyl-CoA. PCC is a mitochondrial enzyme that probably acts as a dodecamer of six alpha subunits and six beta subunits. This gene encodes the beta subunit of PCC. Defects in this gene are a cause of propionic acidemia type II (PA-2). Multiple transcript variants e…
- **Diseases (Open Targets)**: propionic acidemia (0.861); hereditary disease (0.517); hypertensive disorder (0.453); coronary artery disorder (0.438); coronary atherosclerosis (0.428)
- **Europe PMC papers**: 1404
- **Why important**: PCCB is the beta subunit partner of PCCA and is represented in the same broad primary catabolic and metabolic terms, including the short-chain fatty-acid term (GO:BP small molecule catabolic process; q_global = 4.89e-05)(GO:BP organic acid catabolic process; q_global = 9.92e-05)(GO:BP monocarboxylic acid catabolic process; q_global = 0.000389)(KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 0.00362)(GO:BP amino acid metabolic process; q_global = 0.00544)(GO:BP fatty acid catabolic process; q_global = 0.0128)(GO:BP short-chain fatty acid catabolic process; q_global = 0.0295)(GO:BP fatty acid metabolic process; q_global = 0.0326)(GO:BP monocarboxylic acid metabolic process; q_global = 0.0399). The PCCA-PCCB relationship is among the clearest established interactions in STRING, and both genes recur together in hu.MAP complexes. PCCB is mitochondrial, detected in kidney, enriched in liver-related cell types, and linked to propionic acidemia. Its inclusion provides unusually direct biochemical coherence for the module.
- **Conclusion**: Established: PCCB is a validated component of propionyl-CoA carboxylase and strongly corroborates the module's branched-chain and short-chain organic-acid interpretation. Hypothesis: coordinated PCCA-PCCB abundance may reflect regulation of propionyl-CoA flux in the shared cellular program.

#### PCK2

- **Related proteins** (co-abundance neighbors): SLC27A2 (0.84), DCXR (0.82), ASS1 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_07052.1, huMAP3_00213.1, huMAP3_10334.1
- **Function (MyGene.info)**: phosphoenolpyruvate carboxykinase 2, mitochondrial. This gene encodes a mitochondrial enzyme that catalyzes the conversion of oxaloacetate to phosphoenolpyruvate in the presence of guanosine triphosphate (GTP). A cytosolic form of this protein is encoded by a different gene and is the key enzyme of gluconeogenesis in the liver. Alternatively spliced transcript variants have been described. [provided by RefSeq, Apr 2014].
- **Diseases (Open Targets)**: phosphoenolpyruvate carboxykinase deficiency, mitochondrial (0.511); phosphoenolpyruvate carboxykinase deficiency (0.443); neuropathy (0.187); Gait disturbance (0.185); retinitis pigmentosa (0.148)
- **Europe PMC papers**: 2644
- **Why important**: PCK2 links the metabolic interpretation to mitochondrial carbon redistribution. It appears in many primary terms spanning small-molecule and organic-acid metabolism, fatty-acid and short-chain fatty-acid catabolism, and amino-acid-related processes (GO:BP small molecule catabolic process; q_global = 4.89e-05)(GO:BP organic acid catabolic process; q_global = 9.92e-05)(GO:BP monocarboxylic acid catabolic process; q_global = 0.000389)(GO:BP carboxylic acid metabolic process; q_global = 0.000727)(KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 0.00362)(GO:BP amino acid metabolic process; q_global = 0.00544)(GO:BP fatty acid catabolic process; q_global = 0.0128)(GO:BP short-chain fatty acid catabolic process; q_global = 0.0295)(GO:BP fatty acid metabolic process; q_global = 0.0326)(GO:BP monocarboxylic acid metabolic process; q_global = 0.0399). HPA places it in the kidney, intestine, and liver group and in hepatocyte and enterocyte-related cell types. It is present in several hu.MAP complexes with PCCA, PCCB, PRORP, CRYZ, DARS2, and ACSF2, although these complexes are broader than a single canonical pathway. Its established role in mitochondrial oxaloacetate-to-phosphoenolpyruvate conversion and its disease links make it an informative bridge between catabolism and biosynthetic or gluconeogenic carbon handling.
- **Conclusion**: Established: PCK2 is a mitochondrial carbon-routing enzyme associated with the module's metabolic and tissue pattern. Hypothesis: PCK2 may couple oxidative substrate use to mitochondrial carbon export or replenishment in the shared program.

#### ETFDH

- **Related proteins** (co-abundance neighbors): DHRS4 (0.85), ACY1 (0.82), ALDH2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein dehydrogenase. This gene encodes a component of the electron-transfer system in mitochondria and is essential for electron transfer from a number of mitochondrial flavin-containing dehydrogenases to the main respiratory chain. Mutations in this gene are associated with glutaric acidemia. Alternatively spliced transcript variants that encode distinct isoforms have been observed. [provided by RefSeq, Aug 2013].
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.845); glutaric acidemia IIc (0.704); glutaric aciduria (0.670); hereditary disease (0.523); Abnormality of metabolism/homeostasis (0.407)
- **Europe PMC papers**: 1273
- **Why important**: ETFDH provides a mechanistic connection between diverse dehydrogenases and the respiratory chain. It is represented in the primary small-molecule, organic-acid, fatty-acid, and carboxylic-acid terms (GO:BP small molecule catabolic process; q_global = 4.89e-05)(GO:BP organic acid catabolic process; q_global = 9.92e-05)(GO:BP monocarboxylic acid catabolic process; q_global = 0.000389)(GO:BP carboxylic acid metabolic process; q_global = 0.000727)(KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 0.00362)(GO:BP fatty acid catabolic process; q_global = 0.0128)(GO:BP fatty acid metabolic process; q_global = 0.0326)(GO:BP monocarboxylic acid metabolic process; q_global = 0.0399), and STRING places it near DHRS4, ACY1, and ALDH2. It is mitochondrial, associated with liver and muscle-related expression, and has an established role in electron transfer from multiple flavin-dependent dehydrogenases. Its disease association with multiple acyl-CoA dehydrogenase deficiency supports the relevance of the module to respiratory handling of fatty-acid and amino-acid substrates.
- **Conclusion**: Established: ETFDH is a respiratory electron-transfer component that supports oxidation of multiple mitochondrial substrates. Hypothesis: ETFDH may be the functional readout connecting the module's broad catabolic enzyme set to respiratory-chain capacity and redox balance.

## Module 4

**Tissue pair**: kidney and stem_cells  
**Genes (33)**: AFG2A, ATRX, BOD1L1, CIAPIN1, CPSF4, CTDP1, DHX34, EML3, ENOPH1, ERBIN, FRYL, GPHN, GRIPAP1, INTS1, MED22, MGME1, MYL6B, NAA20, NCOR1, IKBKG, OSBPL9, PIR, PRRC2B, RANBP3, RBM26, SCAF11, TSEN34, SNRNP27, GTF2H4, TOX4, TP53BP1, ZGPAT, ZNF451

### Function

The module is best interpreted as a heterogeneous nuclear gene-expression and genome-maintenance module, with converging annotations involving RNA processing, transcription by RNA polymerase II, chromatin regulation, DNA repair, replication-associated integrity, and selected mitochondrial maintenance functions. The network itself is sparse and partitioned into small connected neighborhoods rather than forming one clearly defined physical complex. There are no globally significant GO or KEGG terms: no term passed global multiple-testing correction. The absence of global enrichment does not invalidate the module, but it means that the functional interpretation rests on the concordance of individual gene annotations, network placement, and the limited experimentally supported interactions. Overall, the module is more consistent with a shared cellular state involving transcriptional and RNA-processing capacity, chromatin and DNA-damage management, and general cell maintenance than with a tissue-specific pathway.

**Cell composition.** This is not a plasma or secreted-protein module: no member is classified as secreted. Most genes have low tissue specificity, and kidney protein detection is widespread among the genes with available HPA data. The HPA profile therefore supports a broadly expressed, housekeeping-like nuclear module rather than a kidney-exclusive program. There are cell-type-enhanced signals for neutrophils and several other specialized cell types, and a smaller set of genes has immune-cell-enhanced or immune-cell-enriched annotations. However, most genes have low immune-cell specificity, so the data do not establish that the module is driven by blood contamination. The HPA stem-cell comparison is unavailable because there is no matching HPA tissue category. Shared cell composition, a general proliferative or stress state, or broad expression across both sample groups could therefore contribute to the co-abundance pattern.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a small set of high-confidence anchors within the module: ATRX is linked to TP53BP1, CPSF4 to TSEN34, and GTF2H4 to MED22. These links support DNA-damage and chromatin biology for the ATRX-TP53BP1 pair, and RNA processing or transcriptional regulation for the other pairs, but they do not by themselves define one unified complex. hu.MAP adds several partial complex observations. CPSF4 and SCAF11 co-occur in huMAP complex (hu.MAP huMAP3_10074.1), TP53BP1 and GPHN co-occur in (hu.MAP huMAP3_12566.1), and ZGPAT with SNRNP27 co-occur in the spliceosome-related complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1). In each case only a small fraction of the annotated complex is represented in the module, so these are known relational anchors rather than proof that the entire module is a single biochemical complex. The agreement between the CPSF4-TSEN34 STRING link and the RNA-processing annotations is particularly useful, while the other module edges may reflect coordinated expression or indirect cellular-state relationships.

**STRING interactions (score >= 0.7)**: 3 of 528 gene pairs: ATRX–TP53BP1 (0.742); CPSF4–TSEN34 (0.808); GTF2H4–MED22 (0.848)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10074.1 (CPSF4, SCAF11; 2/8); huMAP3_12566.1 (TP53BP1, GPHN; 2/51); huMAP3_06511.1 (ZGPAT, SNRNP27; 2/79); huMAP3_08980.1 (ZGPAT, SNRNP27; 2/97)

### Novelty

The module may be a new co-abundance observation, but it cannot be claimed as a newly discovered molecular complex or pathway. Its novelty is supported by the absence of a single coherent, densely connected STRING or huMAP architecture and by the mixture of transcription, RNA processing, DNA repair, mitochondrial, and cytoskeletal annotations. At the same time, the individual biology is not novel: several relationships and complexes are already represented in STRING or huMAP, and many member genes have established functions and disease associations. Absence from those resources would not prove novelty, and their limited coverage here should instead be interpreted as evidence that the module is primarily a coordinated expression signature whose mechanistic unity remains to be validated. The appropriate conclusion is a potentially novel tissue-pair co-abundance pattern built from largely known cellular components.

**Hypothesis.** Hypothesis: kidney and stem-cell samples share a cellular state in which transcriptional output, RNA maturation, chromatin organization, and genome surveillance are coordinately regulated. In this model, MED22 and GTF2H4 represent transcriptional control, SNRNP27 and TSEN34 represent RNA maturation and processing, while ATRX and TP53BP1 couple chromatin handling to DNA-damage response. Additional module members could support translation, mitochondrial maintenance, membrane organization, or cell-state signaling. The co-abundance pattern may therefore reflect a common demand for regulated gene expression and genome integrity during renal cellular maintenance or stem-cell-associated growth, rather than a dedicated kidney pathway. This hypothesis should be tested using cell-resolved data, perturbation of the proposed anchor genes, and independent cohorts from both tissues.

### Important genes

#### ATRX

- **Related proteins** (co-abundance neighbors): MED22 (0.85), GTF2H4 (0.85), PIR (0.82), OSBPL9 (0.81); STRING partners: TP53BP1 (0.742)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATRX chromatin remodeler. The protein encoded by this gene contains an ATPase/helicase domain, and thus it belongs to the SWI/SNF family of chromatin remodeling proteins. This protein is found to undergo cell cycle-dependent phosphorylation, which regulates its nuclear matrix and chromatin association, and suggests its involvement in the gene regulation at interphase and chromosomal segregation in mitosis. Mutations in thi…
- **Diseases (Open Targets)**: alpha thalassemia-X-linked intellectual disability syndrome (0.848); intellectual disability-hypotonic facies syndrome, X-linked, 1 (0.786); alpha-thalassemia-myelodysplastic syndrome (0.664); alpha thalassemia-intellectual disability syndrome type 1 (0.606); ATR-X-related syndrome (0.568)
- **Europe PMC papers**: 12307
- **Why important**: ATRX is among the more connected genes in the module and links directly to MED22, GTF2H4, PIR, and OSBPL9 within the co-abundance network. Its established function as a chromatin remodeler, regulator of DNA replication and transcription, and component of the DNA-damage response provides a strong mechanistic bridge between the module's transcriptional and genome-maintenance features. Its direct STRING relationship with TP53BP1 adds an experimentally supported DNA-repair anchor. ATRX also has extensive disease and literature support, including established links to ATR-X-related disorders and intellectual disability.
- **Conclusion**: Established evidence supports ATRX as a central chromatin and genome-integrity component of the module. It is plausible, but not established, that ATRX helps organize the shared co-abundance state; the module does not demonstrate a new ATRX complex or a tissue-specific ATRX mechanism.

#### TP53BP1

- **Related proteins** (co-abundance neighbors): AFG2A (0.84); STRING partners: ATRX (0.742)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_12566.1
- **Function (MyGene.info)**: tumor protein p53 binding protein 1. This gene encodes a protein that functions in the DNA double-strand break repair pathway choice, promoting non-homologous end joining (NHEJ) pathways, and limiting homologous recombination. This protein plays multiple roles in the DNA damage response, including promoting checkpoint signaling following DNA damage, acting as a scaffold for recruitment of DNA damage response proteins to damaged chrom…
- **Diseases (Open Targets)**: neurodegenerative disease (0.367); microcephaly and chorioretinopathy 3 (0.353); alcohol drinking (0.269); urolithiasis (0.269); microcephaly and chorioretinopathy 1 (0.266)
- **Europe PMC papers**: 2200
- **Why important**: TP53BP1 is a functionally consequential DNA-damage-response scaffold that promotes double-strand-break repair through non-homologous end joining, limits homologous recombination, and supports checkpoint signaling. It has a direct STRING link to ATRX and is represented in huMAP complex (hu.MAP huMAP3_12566.1). Although its within-module network connectivity is limited, its biological specificity and established disease relevance make it an important interpretive anchor. Its literature base is substantial and its role in genome surveillance is well established.
- **Conclusion**: Established evidence supports TP53BP1 as a genome-surveillance component that gives the module a plausible DNA-repair dimension. The hypothesis that TP53BP1 activity drives the shared kidney and stem-cell co-abundance pattern remains untested.

#### MED22

- **Related proteins** (co-abundance neighbors): FRYL (0.87), ENOPH1 (0.87), ATRX (0.85), IKBKG (0.82), CIAPIN1 (0.82); STRING partners: GTF2H4 (0.848)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mediator complex subunit 22. This gene encodes a protein component of the mediator complex, which functions in the regulation of transcription by bridging interactions between gene-specific regulatory factors, RNA polymerase II, and general transcription factors. Alternatively spliced transcript variants encoding different isoforms have been observed. [provided by RefSeq, Jul 2013].
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); alcohol drinking (0.156); stroke disorder (0.156); brain compression (0.104); edema (0.104)
- **Europe PMC papers**: 308
- **Why important**: MED22 is one of the more connected network genes and is linked to FRYL, ENOPH1, ATRX, IKBKG, and CIAPIN1. As a Mediator subunit, it connects gene-specific regulatory factors with RNA polymerase II and general transcription machinery. Its direct STRING relationship with GTF2H4 supports a transcriptional-control interpretation, while HPA shows enhancement in several neural cell types without strong tissue specificity. MED22 has a comparatively substantial literature base and disease associations involving neurological traits.
- **Conclusion**: Established evidence supports MED22 as a transcriptional-regulation anchor and a plausible bridge between broad cellular expression and the module's nuclear functions. A specific MED22-dependent mechanism in kidney or stem cells is a hypothesis rather than a demonstrated result.

#### SNRNP27

- **Related proteins** (co-abundance neighbors): NCOR1 (0.87), FRYL (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U4/U6.U5 subunit 27. This gene encodes a serine/arginine-rich (SR) protein. SR proteins play important roles in pre-mRNA splicing by facilitating the recognition and selection of splice sites. The encoded protein associates with the 25S U4/U6.U5 tri-snRNP, a major component of the U2-type spiceosome. The expression of this gene may be altered in cells infected with the human T-cell lymphotropic virus type 1 (HTLV-1) r…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); atrial fibrillation (0.127); intelligence (0.124); heart disorder (0.107); cardiac arrhythmia (0.098)
- **Europe PMC papers**: 150
- **Why important**: SNRNP27 is a spliceosomal U4/U6.U5 tri-snRNP component with an established role in spliceosome assembly and pre-mRNA splicing. It is represented in both huMAP spliceosome-related complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1), providing independent complex-level support for RNA-processing biology. Its network links to NCOR1 and FRYL connect splicing with transcriptional repression and cell-state regulation. The gene has established disease and literature associations, although its literature volume is more limited than that of the major DNA-repair and chromatin factors.
- **Conclusion**: Established evidence supports SNRNP27 as a genuine RNA-splicing component represented in the module. It supports a shared RNA-maturation program, but the co-abundance data do not show that this module contains a complete spliceosome or that SNRNP27 is functionally altered.

#### TSEN34

- **Related proteins** (co-abundance neighbors): ZNF451 (0.89), CPSF4 (0.82), RBM26 (0.81); STRING partners: CPSF4 (0.808)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tRNA splicing endonuclease subunit 34. This gene encodes a catalytic subunit of the tRNA splicing endonuclease, which catalyzes the removal of introns from precursor tRNAs. The endonuclease complex is also associated with a pre-mRNA 3-prime end processing factor. A mutation in this gene results in the neurological disorder pontocerebellar hypoplasia type 2. Multiple alternatively spliced variants, encoding the same protein, have been i…
- **Diseases (Open Targets)**: pontocerebellar hypoplasia type 2C (0.646); pontocerebellar hypoplasia type 2 (0.632); intellectual disability, autosomal recessive 57 (0.407); pontocerebellar hypoplasia (0.193); hereditary disease (0.118)
- **Europe PMC papers**: 204
- **Why important**: TSEN34 combines a direct STRING relationship with CPSF4 and a network connection to RBM26 and ZNF451. It is a catalytic subunit of the tRNA-splicing endonuclease and is also associated with pre-mRNA three-prime-end processing. The CPSF4 relationship links tRNA and messenger-RNA processing themes within the module. TSEN34 has a well-established association with pontocerebellar hypoplasia and related neurological disorders, giving it strong functional and disease relevance despite its modest network connectivity.
- **Conclusion**: Established evidence supports TSEN34 as an RNA-processing anchor and explains part of the module's co-abundance structure through its known relationship with CPSF4. It remains a hypothesis that altered tRNA or messenger-RNA processing is the shared biological driver in kidney and stem-cell samples.

## Module 5

**Tissue pair**: kidney and stem_cells  
**Genes (12)**: AGRN, ALDH4A1, BOLA3, BPHL, HEXB, MANBA, NHERF2, NQO2, REPS1, RINT1, RRBP1, SMARCD1

### Function

No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The module appears functionally heterogeneous rather than a canonical protein complex: its links connect membrane and signaling scaffolding through REPS1 and NHERF2, mitochondrial and metabolic proteins through BPHL, ALDH4A1, and BOLA3, lysosomal carbohydrate catabolism through MANBA and HEXB, and secretory or intracellular trafficking through RRBP1 and RINT1. The co-abundance structure therefore supports a shared cellular-state or tissue-composition signal more strongly than a single established biochemical pathway. The strongest network position is held by REPS1, which links several otherwise distinct functional branches. The absence of globally corrected GO or KEGG enrichment does not invalidate the module, but it limits pathway-level interpretation.

**Cell composition.** The module is not dominated by plasma or broadly secreted proteins, and its HPA profile does not support a predominantly blood-cell module. Most genes have low immune-cell specificity, while a smaller subset is immune-cell enhanced or group enriched. The HPA annotations instead show a mixture of kidney-associated, liver-associated, epithelial, neuronal or glial, secretory, and myeloid cell contexts. Several genes are cell-type enhanced, especially in hepatocytes and renal proximal-tubule cells, while AGRN is associated with several kidney epithelial and podocyte populations. The module has secreted-gene annotations, including AGRN with secretion to extracellular matrix, but the overall set is mainly intracellular, membrane-associated, mitochondrial, lysosomal, nuclear, Golgi, or endoplasmic-reticulum localized. Protein detection in kidney is broadly consistent across the annotated genes, whereas there is no matching HPA tissue category for stem cells. Consequently, the shared signal could reflect conserved renal or epithelial cell biology, cellular composition, or technical co-abundance across tissues; the data do not establish that it is stem-cell specific.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the specified high-confidence threshold, and no hu.MAP complex contained multiple module members. Thus, the observed co-abundance edges are not supported here by high-confidence known physical or functional interactions, and the module does not correspond to a recognized hu.MAP complex. This argues against interpreting the entire module as a pre-existing protein complex. It does not exclude weaker, context-dependent, indirect, tissue-specific, or poorly studied relationships. The internal network still provides useful structure: REPS1 connects BOLA3, SMARCD1, RINT1, and NHERF2; BPHL connects ALDH4A1, NHERF2, and NQO2; and MANBA connects HEXB and RRBP1. These links suggest coordinated abundance across cellular systems rather than a validated physical assembly.

**STRING interactions (score >= 0.7)**: 0 of 66 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel co-abundance association, but it cannot be called a definitively new biological module. The lack of high-confidence STRING relationships and the absence of a shared hu.MAP complex mean that the exact network configuration is not readily represented in those resources. However, database absence alone is not proof of novelty, and several individual genes have substantial literature and established functions. The module may therefore be novel at the level of cross-tissue co-abundance organization or sample-level regulation, while its component biology is largely established. The lack of globally corrected GO or KEGG enrichment further suggests that its novelty is not a newly defined canonical pathway, but possibly a context-dependent combination of known cellular processes.

**Hypothesis.** Hypothesis: the module reflects a coordinated cellular-state program that couples renal or epithelial abundance with metabolic and organelle maintenance. In this model, REPS1 and NHERF2 organize membrane, receptor, and trafficking-related states; RRBP1 supports endoplasmic-reticulum and secretory capacity; BOLA3 and ALDH4A1 report mitochondrial maturation and amino-acid metabolism; and MANBA with HEXB reports lysosomal glycoprotein and carbohydrate turnover. BPHL and NQO2 could contribute xenobiotic and redox handling. The apparent sharing between kidney and stem cells may therefore arise from a conserved requirement for membrane trafficking, proteostasis, mitochondrial metabolism, and lysosomal recycling, or from shared epithelial and progenitor-like cellular composition. This remains a hypothesis because the network lacks high-confidence STRING or hu.MAP support and lacks globally corrected pathway enrichment.

### Important genes

#### REPS1

- **Related proteins** (co-abundance neighbors): BOLA3 (0.89), SMARCD1 (0.87), RINT1 (0.85), NHERF2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RALBP1 associated Eps domain containing 1. This gene encodes a signaling adaptor protein with two EH domains that interacts with proteins that participate in signaling, endocytosis and cytoskeletal changes. The encoded protein has been found in association with intersectin 1 and Src homology 3-domain growth factor receptor-bound 2-like (endophilin) interacting protein 1 when intersectin 1 was isolated from clathrin-coated pits. The encoded…
- **Diseases (Open Targets)**: neurodegeneration with brain iron accumulation (0.593); neurodegeneration with brain iron accumulation 7 (0.437); neurodegenerative disease (0.410); response to radiation (0.331); cardiovascular disorder (0.071)
- **Europe PMC papers**: 437
- **Why important**: REPS1 has the strongest network position in the module and connects membrane-associated signaling and trafficking with BOLA3, SMARCD1, RINT1, and NHERF2. Its established annotation describes an adaptor involved in endocytosis, endosomal transport, and cytoskeletal changes. It also has kidney protein detection, a substantial literature base, and disease associations involving neurodegeneration and radiation response.
- **Conclusion**: Established evidence supports REPS1 as the principal network organizer and an endocytic or trafficking adaptor. Hypothesis: its central position may coordinate the membrane and intracellular-trafficking branch of the shared co-abundance state, but the module does not establish a direct physical interaction or causal role.

#### NHERF2

- **Related proteins** (co-abundance neighbors): BPHL (0.83), AGRN (0.82), REPS1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NHERF family PDZ scaffold protein 2. This gene encodes a member of the NHERF family of PDZ scaffolding proteins. These proteins mediate many cellular processes by binding to and regulating the membrane expression and protein-protein interactions of membrane receptors and transport proteins. The encoded protein plays a role in intestinal sodium absorption by regulating the activity of the sodium/hydrogen exchanger 3, and may also regu…
- **Diseases (Open Targets)**: hypertensive disorder (0.480); essential hypertension (0.399); cardiovascular disorder (0.384); Increased blood pressure (0.375); open-angle glaucoma (0.330)
- **Europe PMC papers**: 519
- **Why important**: NHERF2 is a membrane-associated PDZ scaffold linking REPS1, BPHL, and AGRN. Its established function includes regulating membrane expression and interactions of receptors and transport proteins, including roles involving intestinal sodium absorption and CFTR. Its HPA profile includes vascular and secretory cell contexts and several myeloid populations, and its disease associations include hypertension-related conditions.
- **Conclusion**: Established evidence supports NHERF2 as a plausible membrane-organization and transporter-regulation component. Hypothesis: it may connect epithelial transport or receptor organization with the metabolic and extracellular branches of the module, although the co-abundance data do not prove that it directly scaffolds the other module members.

#### BPHL

- **Related proteins** (co-abundance neighbors): ALDH4A1 (0.87), NHERF2 (0.83), NQO2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biphenyl hydrolase like. This gene encodes a member of the serine protease family of hydrolytic enzymes which contain a serine in their active site. The encoded protein may play a role in activation of the antiviral prodrug valacyclovir. Alternatively spliced transcript variants have been described.[provided by RefSeq, Jan 2009].
- **Diseases (Open Targets)**: alcohol drinking (0.181); urolithiasis (0.181); handedness (0.164); musculoskeletal system disorder (0.122); tooth disorder (0.109)
- **Europe PMC papers**: 358
- **Why important**: BPHL is a network bridge linking ALDH4A1, NHERF2, and NQO2. It is annotated as a serine hydrolase-like enzyme associated with amino-acid metabolism, xenobiotic metabolism, toxic-substance response, and homocysteine metabolism. It is tissue enhanced in kidney and liver, detected in kidney protein data, and has cell-type enhancement in hepatocytes and other epithelial populations.
- **Conclusion**: Established evidence supports BPHL as a kidney- and liver-associated metabolic enzyme candidate within the module. Hypothesis: BPHL may couple epithelial metabolic or detoxification state to membrane-associated abundance, but its exact substrate and role in this module remain unresolved.

#### BOLA3

- **Related proteins** (co-abundance neighbors): REPS1 (0.89), RRBP1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies, Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: bolA family member 3. This gene encodes a protein that plays an essential role in the production of iron-sulfur (Fe-S) clusters for the normal maturation of lipoate-containing 2-oxoacid dehydrogenases, and for the assembly of the mitochondrial respiratory chain complexes. Mutation in this gene has been associated with multiple mitochondrial dysfunctions syndrome-2. Two alternatively spliced transcript variants encoding…
- **Diseases (Open Targets)**: multiple mitochondrial dysfunctions syndrome 2 (0.819); fatal multiple mitochondrial dysfunctions syndrome (0.595); mitochondrial disease (0.371); hereditary disease (0.191); lung adenocarcinoma (0.030)
- **Europe PMC papers**: 443
- **Why important**: BOLA3 links REPS1 and RRBP1 and provides a mitochondrial component to the network. It is established as essential for iron-sulfur cluster production, maturation of lipoate-containing dehydrogenases, and mitochondrial respiratory-chain assembly. Its disease associations include multiple mitochondrial dysfunctions syndrome, and it has kidney protein detection.
- **Conclusion**: Established evidence supports BOLA3 as a mitochondrial Fe-S and respiratory-function marker. Hypothesis: its co-abundance with trafficking and endoplasmic-reticulum genes may indicate coordinated mitochondrial and proteostasis demands in the shared cellular state, rather than a direct BOLA3-centered complex.

#### MANBA

- **Related proteins** (co-abundance neighbors): HEXB (0.89), RRBP1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosidase beta. This gene encodes a member of the glycosyl hydrolase 2 family. The encoded protein localizes to the lysosome where it is the final exoglycosidase in the pathway for N-linked glycoprotein oligosaccharide catabolism. Mutations in this gene are associated with beta-mannosidosis, a lysosomal storage disease that has a wide spectrum of neurological involvement. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: beta-mannosidosis (0.828); primary biliary cholangitis (0.411); diabetes mellitus (0.338); ventricular septal defect (0.306); Hypercholesterolemia (0.296)
- **Europe PMC papers**: 863
- **Why important**: MANBA connects HEXB and RRBP1 and represents lysosomal glycoprotein and oligosaccharide catabolism. It is associated with lysosomal function and beta-mannosidase activity, with disease relevance to beta-mannosidosis. HPA places it in kidney protein data and in several myeloid and neural immune-related cell contexts.
- **Conclusion**: Established evidence supports MANBA as a lysosomal carbohydrate-catabolism component with relevant disease biology. Hypothesis: MANBA may report lysosomal recycling or inflammatory-cell composition within the module, but the data do not distinguish intrinsic renal or stem-cell regulation from variation in cell populations.

#### RRBP1

- **Related proteins** (co-abundance neighbors): MANBA (0.84), BOLA3 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosome binding protein 1. This gene encodes a ribosome-binding protein of the endoplasmic reticulum (ER) membrane. Studies suggest that this gene plays a role in ER proliferation, secretory pathways and secretory cell differentiation, and mediation of ER-microtubule interactions. Alternative splicing has been observed and protein isoforms are characterized by regions of N-terminal decapeptide and C-terminal heptad repeats.…
- **Diseases (Open Targets)**: cancer (0.476); dengue disease (0.462); neurodegenerative disease (0.324); coronary artery disorder (0.292); placental abruption (0.279)
- **Europe PMC papers**: 1654
- **Why important**: RRBP1 links MANBA and BOLA3 and provides a structural connection to the endoplasmic reticulum. It is established as an ER membrane ribosome-binding protein involved in ER proliferation, secretory pathways, secretory-cell differentiation, and ER–microtubule interactions. It has a large literature base, kidney protein detection, and enhancement in pancreatic and placental secretory cell contexts.
- **Conclusion**: Established evidence supports RRBP1 as an ER and secretory-capacity marker. Hypothesis: RRBP1 may connect secretory and proteostasis demands with lysosomal and mitochondrial remodeling in the shared module, but the sparse network and absence of database-supported interactions make this mechanistic interpretation provisional.

## Module 6

**Tissue pair**: kidney and stem_cells  
**Genes (10)**: BAG3, CCN1, IGF1R, PML, CRYZL1, POLR2E, SH3BGRL3, SMS, CTTN, TRIM25

### Function

No GO or KEGG term passed global correction, so the module has no statistically established pathway-level annotation from the primary enrichment analysis. Its gene annotations suggest a mixed cellular program involving cell adhesion and actin-cytoskeleton organization through CTTN and CCN1, growth-factor and receptor signaling through CCN1 and IGF1R, proteostasis and stress handling through BAG3, and transcriptional, antiviral, or stress-response regulation through PML and TRIM25. Because the subgraph is connected but has no high-confidence STRING interaction and no supported hu.MAP complex, the safest interpretation is a coordinated co-abundance pattern rather than a demonstrated molecular complex or single pathway.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: only CCN1 is annotated as secreted to the extracellular matrix. Most genes have low tissue specificity, while nearly all have cell-type-enhanced expression. The HPA profile includes recurring signals in monocytes and granulocyte-related cells, as well as epithelial, stromal, muscle, and reproductive cell types. Several genes have enhanced immune-cell profiles, but the module is not uniformly blood-cell specific. Thus, shared immune or stromal cell composition in kidney and stem-cell samples could contribute to the pattern, and the module should not automatically be interpreted as a kidney-intrinsic program. All module proteins were detected in kidney; corresponding stem-cell tissue-level HPA evidence is unavailable.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair reached the supplied high-confidence STRING interaction threshold, and no hu.MAP complex contained multiple module members. Therefore, the observed co-abundance edges are not supported here as known direct physical interactions or as a shared established complex. Some individual proteins have well-characterized functions, but the fact sheet does not establish direct relationships among the module members. The network should consequently be treated as an expression-association structure whose biological coherence remains provisional.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported co-abundance association, but it cannot be called a new biological discovery from these data alone. Its lack of high-confidence STRING links and hu.MAP complexes supports that the particular combination is not captured by those resources, yet database absence does not prove novelty. The absence of globally significant GO or KEGG enrichment further limits claims of a novel coherent pathway. Novelty would require independent replication, comparison with published co-expression modules, and experimental or perturbational validation.

**Hypothesis.** Hypothesis: the module reflects coordinated variation across a tissue or cell mixture in which extracellular-matrix signaling by CCN1, growth and survival signaling through IGF1R, and adhesion or actin remodeling involving CTTN are coupled to cellular stress and proteostasis responses involving BAG3, PML, and TRIM25. A contribution from immune-cell admixture is also plausible because several members show immune-cell-enhanced HPA profiles. This is a mechanistic hypothesis, not an established interaction model; testing should examine cell-composition adjustment, protein-level co-localization, perturbation of CCN1 or IGF1R signaling, and responses of the stress-regulatory genes.

### Important genes

#### CCN1

- **Related proteins** (co-abundance neighbors): BAG3 (0.87), SH3BGRL3 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cellular communication network factor 1. The secreted protein encoded by this gene is growth factor-inducible and promotes the adhesion of endothelial cells. The encoded protein interacts with several integrins and with heparan sulfate proteoglycan. This protein also plays a role in cell proliferation, differentiation, angiogenesis, apoptosis, and extracellular matrix formation. [provided by RefSeq, Sep 2011].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.575); vein disorder (0.338); lymphatic system disorder (0.338); myalgic encephalomeyelitis/chronic fatigue syndrome (0.260); glomerulonephritis (0.253)
- **Europe PMC papers**: 14168
- **Why important**: CCN1 is a central connector in the module, linking BAG3 and SH3BGRL3, and it is the only annotated secreted extracellular-matrix protein. Its established roles in endothelial adhesion, integrin signaling, migration, angiogenesis, apoptosis, and matrix formation make it a plausible bridge between extracellular context and intracellular co-abundance. It also has substantial literature and disease associations including vascular and glomerular disorders.
- **Conclusion**: Established evidence supports CCN1 as an extracellular-matrix and adhesion signaling factor with relevance to kidney and vascular biology. It is a leading candidate for organizing the module's tissue-context signal. It remains unproven that CCN1 directly drives the co-abundance of the other module genes.

#### BAG3

- **Related proteins** (co-abundance neighbors): CCN1 (0.87), PML (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BAG cochaperone 3. BAG proteins compete with Hip for binding to the Hsc70/Hsp70 ATPase domain and promote substrate release. All the BAG proteins have an approximately 45-amino acid BAG domain near the C terminus but differ markedly in their N-terminal regions. The protein encoded by this gene contains a WW domain in the N-terminal region and a BAG domain in the C-terminal region. The BAG domains of BAG1, BAG2, and …
- **Diseases (Open Targets)**: dilated cardiomyopathy 1HH (0.821); myofibrillar myopathy 6 (0.789); dilated cardiomyopathy (0.726); familial isolated dilated cardiomyopathy (0.678); heart failure (0.654)
- **Europe PMC papers**: 4304
- **Why important**: BAG3 connects CCN1 with PML and is annotated as a cochaperone involved in Hsp-related substrate handling, autophagosome assembly, protein folding, stress response, and apoptosis. Its tissue-enhanced skeletal-muscle signal and strong disease links to cardiomyopathy and myofibrillar myopathy make it biologically important for interpreting a stress or proteostasis component.
- **Conclusion**: Established evidence supports BAG3 as a proteostasis and stress-response regulator with major disease relevance. Its position supports a possible intracellular stress arm of the module. The connection to CCN1 or PML is a co-abundance observation rather than a demonstrated direct mechanism.

#### PML

- **Related proteins** (co-abundance neighbors): CTTN (0.87), POLR2E (0.84), BAG3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PML nuclear body scaffold. The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. This phosphoprotein localizes to nuclear bodies where it functions as a transcription factor and tumor suppressor. Its expression is cell-cycle related and it regulates the p53 response to oncoge…
- **Diseases (Open Targets)**: thyroid gland carcinoma (0.585); uterine corpus leiomyoma (0.548); type 2 diabetes mellitus (0.499); viral infectious disease (0.478); acute myeloid leukemia (0.444)
- **Europe PMC papers**: 21659
- **Why important**: PML has the highest connectivity in the module and links CTTN, POLR2E, and BAG3. It is a nuclear-body scaffold and transcriptional regulator involved in chromatin remodeling, apoptosis, hypoxia response, antiviral defense, and p53-related tumor suppression. Its very large literature base and disease associations make it an important interpretive anchor.
- **Conclusion**: Established evidence supports PML as a nuclear regulatory and stress-response hub. Its network position makes it a plausible coordinator of transcriptional state rather than evidence of a physical module complex. Whether PML regulates this co-abundance pattern is a hypothesis requiring perturbation.

#### IGF1R

- **Related proteins** (co-abundance neighbors): TRIM25 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoli, Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor 1 receptor. This receptor binds insulin-like growth factor with a high affinity. It has tyrosine kinase activity. The insulin-like growth factor I receptor plays a critical role in transformation events. Cleavage of the precursor generates alpha and beta subunits. It is highly overexpressed in most malignant tissues where it functions as an anti-apoptotic agent by enhancing cell survival. Alternatively splice…
- **Diseases (Open Targets)**: growth delay due to insulin-like growth factor I resistance (0.811); Abnormality of the skeletal system (0.612); Graves ophthalmopathy (0.568); gout (0.539); atrial fibrillation (0.529)
- **Europe PMC papers**: 37783
- **Why important**: IGF1R is a receptor tyrosine kinase connected to TRIM25 and is annotated for insulin-like growth-factor signaling, survival, proliferation, migration, and immune response. HPA shows kidney-relevant cell types including podocytes and proximal tubule cells, together with an immune-cell signal. Its extensive literature and disease associations give it strong biological interpretive value.
- **Conclusion**: Established evidence supports IGF1R as a growth, survival, and cell-state receptor relevant to kidney cell biology. It could provide an upstream signaling context for the module, but the supplied network does not establish that IGF1R signaling controls the other members.

#### TRIM25

- **Related proteins** (co-abundance neighbors): IGF1R (0.81), CRYZL1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tripartite motif containing 25. The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein is an RNA binding protein, functions as a ubiquitin E3 ligase and is involved in multiple cellular processes, including regulation of antiviral innate immunity. [provided by RefSeq, S…
- **Diseases (Open Targets)**: dengue disease (0.463); COVID-19 (0.376); severe acute respiratory syndrome (0.372); neoplasm (0.108); hepatocellular carcinoma (0.106)
- **Europe PMC papers**: 4363
- **Why important**: TRIM25 connects IGF1R with CRYZL1 and is an RNA-binding ubiquitin E3 ligase involved in antiviral innate immunity, ubiquitination, oxidative-stress responses, and autophagy regulation. Its enrichment in monocytes and neutrophils is relevant to the possibility that immune composition contributes to the shared module. It also has substantial literature and infectious-disease associations.
- **Conclusion**: Established evidence supports TRIM25 as an immune and proteostatic regulatory factor. Its HPA profile makes immune-cell contribution a credible alternative explanation for part of the module. A direct functional link to IGF1R or CRYZL1 is not established by the supplied interaction resources.

#### CTTN

- **Related proteins** (co-abundance neighbors): PML (0.87), CRYZL1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cortactin. This gene is overexpressed in breast cancer and squamous cell carcinomas of the head and neck. The encoded protein is localized in the cytoplasm and in areas of the cell-substratum contacts. This gene has two roles: (1) regulating the interactions between components of adherens-type junctions and (2) organizing the cytoskeleton and cell adhesion structures of epithelia and carcinoma cells. During …
- **Diseases (Open Targets)**: drug allergy (0.349); placenta praevia (0.265); response to antihypertensive drug (0.260); gallbladder disorder (0.258); non-autoimmune hemolytic anemia (0.240)
- **Europe PMC papers**: 2395
- **Why important**: CTTN is connected to PML and CRYZL1 and encodes cortactin, a well-studied regulator of actin polymerization, epithelial adhesion structures, receptor-mediated endocytosis, and intracellular transport. Its plasma-membrane and vesicular localization, epithelial cell signals, and immune-cell signals make it a plausible interface between adhesion, trafficking, and sample composition.
- **Conclusion**: Established evidence supports CTTN as an actin and membrane-trafficking regulator. It provides a plausible cellular-architecture component of the module, but the association with PML and CRYZL1 should be regarded as co-abundance rather than validated direct binding.

## Module 7

**Tissue pair**: kidney and stem_cells  
**Genes (5)**: BASP1, FAM114A1, PDLIM7, RFTN1, VPS4B

### Function

The module does not have a globally significant GO or KEGG enrichment term. Its gene-level annotations nevertheless suggest several connected cellular themes: membrane-raft organization and immune signaling through RFTN1, actin-associated structural organization through PDLIM7, vesicle, lysosomal and membrane-remodeling processes through VPS4B, and less well characterized developmental or neuronal associations for BASP1 and FAM114A1. The co-abundance topology is centered on RFTN1, which connects to BASP1, VPS4B and PDLIM7, while FAM114A1 connects to PDLIM7. This supports a possible membrane–cytoskeleton–vesicle interface, but the absence of globally corrected enrichment means this interpretation remains gene- and network-based rather than pathway-enrichment-based.

**Cell composition.** The module is not composed of secreted proteins, so it does not resemble a plasma-protein or secretome module. It does show a substantial immune and blood-cell signature: three genes are associated with neutrophils, and additional associations include monocytes, myeloid dendritic cells and other granulocytes. Four genes have cell-type-enhanced expression and one is cell-type-enriched. Tissue associations are heterogeneous, including lymphoid tissue, blood vessel, intestine, skeletal muscle, brain and epididymis. Kidney protein detection is present for most genes, whereas there is no matching HPA stem-cell tissue result. The shared kidney–stem-cell signal could therefore reflect a shared immune or stromal-cell contribution, sample composition, or a broadly distributed cellular program rather than a kidney–stem-cell-specific mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no hu.MAP complex contained multiple module members. Thus, the observed co-abundance relationships are not supported here by documented high-confidence physical interactions or a shared hu.MAP complex. The lack of database support does not invalidate the co-abundance module: the relationships could be indirect, context-dependent, condition-dependent, or driven by shared cell composition. RFTN1 is the network hub, with links to BASP1, VPS4B and PDLIM7, while PDLIM7 links to FAM114A1. These edges should therefore be treated as co-abundance associations rather than established physical interactions.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module appears potentially novel as a co-abundance pattern because none of its within-module relationships is represented by the reported high-confidence STRING interactions or hu.MAP multi-member complexes. However, it cannot be called a new biological mechanism solely because those resources lack the relationships. The genes themselves have established individual functions, disease associations and literature histories, and the blood-cell and neutrophil signal provides a plausible shared-cell explanation. The strongest defensible conclusion is that the kidney–stem-cell co-abundance configuration is a candidate novel association requiring replication, cell-composition adjustment and targeted validation.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of a membrane-associated immune and structural-remodeling program. RFTN1 may organize membrane rafts and immune receptor or nucleic-acid-sensing signaling; PDLIM7 may connect membrane-associated signaling to actin structures; VPS4B may support vesicle and membrane repair or lysosomal trafficking; and BASP1 and FAM114A1 may mark cell-state-specific components of this program. In kidney and stem-cell samples, the apparent module may be generated partly by shared neutrophil or myeloid-cell content rather than by a single intrinsic program in kidney or stem cells. This hypothesis predicts that the module will weaken after immune-cell deconvolution if it is mainly compositional, but will remain in purified relevant cells if it represents a conserved intracellular program.

### Important genes

#### RFTN1

- **Related proteins** (co-abundance neighbors): BASP1 (0.90), VPS4B (0.85), PDLIM7 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: raftlin, lipid raft linker 1. Enables double-stranded RNA binding activity. Involved in B cell receptor signaling pathway; membrane raft assembly; and positive regulation of growth rate. Acts upstream of or within dsRNA transport; response to exogenous dsRNA; and toll-like receptor 3 signaling pathway. Located in endosome; membrane raft; and plasma membrane. Part of protein-containing complex. [provided by Alliance of Genome R…
- **Diseases (Open Targets)**: neurodegenerative disease (0.486); COVID-19 (0.299); lysosomal storage disease (0.288); digestive system disorder (0.282); bone Paget disease (0.230)
- **Europe PMC papers**: 444
- **Why important**: RFTN1 is the central network gene, connected to BASP1, VPS4B and PDLIM7. Its established annotations include membrane-raft assembly, B-cell receptor signaling, transport into membrane rafts, double-stranded RNA binding and Toll-like receptor signaling. It is detected in kidney, has a lymphoid-tissue association, and has a substantial disease and literature record. Its position makes it the most informative candidate for testing whether the module represents coordinated membrane-immune organization.
- **Conclusion**: Established evidence supports RFTN1 as a membrane-raft and immune-signaling component and as the network hub. The claim that it mechanistically drives the whole module is a hypothesis, not demonstrated by the co-abundance data or by STRING and hu.MAP.

#### PDLIM7

- **Related proteins** (co-abundance neighbors): FAM114A1 (0.82), RFTN1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Actin filaments, Focal adhesion sites; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 7. The protein encoded by this gene is representative of a family of proteins composed of conserved PDZ and LIM domains. LIM domains are proposed to function in protein-protein recognition in a variety of contexts including gene transcription and development and in cytoskeletal interaction. The LIM domains of this protein bind to protein kinases, whereas the PDZ domain binds to actin filaments. The g…
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); nasopharyngeal carcinoma (0.121); neoplasm (0.120); lymphoma (0.115); Hodgkins lymphoma (0.105)
- **Europe PMC papers**: 808
- **Why important**: PDLIM7 connects RFTN1 with FAM114A1 and is localized to actin filaments and focal adhesion sites. Its PDZ and LIM domains support protein-recognition and cytoskeletal interactions, while its annotations include actin-cytoskeleton organization, receptor-mediated endocytosis, heart development and muscle structure development. It is detected in kidney and has blood-vessel, muscle, megakaryocyte and neutrophil associations, making it a plausible bridge between structural remodeling and the immune-cell signal.
- **Conclusion**: Established evidence supports PDLIM7 as an actin-associated adaptor with tissue and blood-cell associations relevant to this module. Its proposed role as the structural bridge between membrane signaling and vesicle or immune behavior remains a hypothesis.

#### VPS4B

- **Related proteins** (co-abundance neighbors): RFTN1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vacuolar protein sorting 4 homolog B. The protein encoded by this gene is a member of the AAA protein family (ATPases associated with diverse cellular activities), and is the homolog of the yeast Vps4 protein. In humans, two paralogs of the yeast protein have been identified. The former share a high degree of aa sequence similarity with each other, and also with yeast Vps4 and mouse Skd1 proteins. Mouse Skd1 (suppressor of K+ transpor…
- **Diseases (Open Targets)**: HIV infectious disease (0.462); dentin dysplasia type I (0.375); atypical dentin dysplasia due to SMOC2 deficiency (0.372); cystic kidney disease (0.194); enteritis (0.191)
- **Europe PMC papers**: 868
- **Why important**: VPS4B is a vesicle-localized AAA-family protein associated with plasma-membrane repair, autophagy, vacuole organization and lysosomal transport. It connects directly to the network hub RFTN1 and is detected in kidney. Its vesicle and membrane-remodeling functions provide a mechanistic complement to RFTN1 membrane-raft biology, even though no physical interaction is reported in STRING or hu.MAP.
- **Conclusion**: Established evidence supports VPS4B in membrane trafficking, lysosomal processes, autophagy and membrane repair. Its participation in the specific kidney–stem-cell module and its functional connection to RFTN1 are supported only as co-abundance associations or hypotheses.

#### BASP1

- **Related proteins** (co-abundance neighbors): RFTN1 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: brain abundant membrane attached signal protein 1. This gene encodes a membrane bound protein with several transient phosphorylation sites and PEST motifs. Conservation of proteins with PEST sequences among different species supports their functional significance. PEST sequences typically occur in proteins with high turnover rates. Immunological characteristics of this protein are species specific. This protein also undergoes N-terminal myristoyla…
- **Diseases (Open Targets)**: neurodegenerative disease (0.375); chronic hepatitis (0.345); mixed connective tissue disease (0.283); alcohol drinking (0.268); stroke disorder (0.260)
- **Europe PMC papers**: 1661
- **Why important**: BASP1 is directly connected to RFTN1 and is associated with the plasma membrane, brain and epididymis. It is cell-type-enriched in neutrophils and immune-cell-enriched in the HPA summary, making it particularly important for evaluating whether the module reflects blood-cell composition. BASP1 also has the largest literature record among the module genes and has reported developmental and transcription-related annotations.
- **Conclusion**: Established evidence supports BASP1 as a membrane-associated protein with developmental, neuronal and neutrophil-related expression context. Its role as an immune-linked partner of RFTN1 in this module is plausible but not established by a known complex or interaction.

#### FAM114A1

- **Related proteins** (co-abundance neighbors): PDLIM7 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Golgi apparatus, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: family with sequence similarity 114 member A1. The protein encoded by this gene belongs to the FAM114 family and may play a role in neuronal cell development. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2017].
- **Diseases (Open Targets)**: response to stimulus (0.454); restless legs syndrome (0.382); movement disorder (0.338); neurodegenerative disease (0.335); ocular hypotension (0.193)
- **Europe PMC papers**: 200
- **Why important**: FAM114A1 connects to PDLIM7 and has a Golgi and cytosolic localization. It is associated with esophageal and salivary epithelial cell types and with multiple monocyte, dendritic-cell and neutrophil populations. Its disease and literature record is smaller than that of the better characterized genes, so it is valuable as a potentially underexplored component that may help distinguish a cell-state or composition signal from a canonical pathway.
- **Conclusion**: Established evidence is limited to its family assignment, subcellular localization, possible neuronal-development relevance and HPA cell-type associations. A role in the proposed membrane–cytoskeleton–immune program is a hypothesis requiring direct functional testing.

## Module 8

**Tissue pair**: kidney and stem_cells  
**Genes (5)**: CUX1, CUX1, RHOG, RPUSD2, STX10

### Function

The module does not have a GO or KEGG term passing global correction. Its most coherent interpretation therefore comes from gene functions and network structure rather than formal pathway enrichment. STX10 is the central co-abundance connector, with links to RPUSD2, CUX1, and RHOG. The genes collectively point toward intracellular trafficking and vesicle fusion through STX10, actin organization and cell-shape signaling through RHOG, transcriptional and differentiation control through CUX1, and RNA pseudouridine modification through RPUSD2. These processes do not establish one unified pathway, so the safest functional description is a sparse, cross-lineage intracellular maintenance and regulatory module, potentially combining trafficking, cytoskeletal signaling, transcriptional state, and RNA processing. The absence of a globally significant term does not invalidate the module.

**Cell composition.** The module is not composed of secreted proteins, and the HPA evidence does not support a plasma-protein explanation. All measured module proteins are detected in kidney. Most genes have low tissue specificity, while several show cell-type-enhanced patterns, including neutrophils, esophageal apical cells, cDC, Hofbauer cells, Kupffer cells, and monocytes. RHOG is tissue-enhanced in bone marrow, and CUX1 is immune-cell enhanced in non-classical monocytes. This pattern is compatible with broadly expressed intracellular proteins plus contributions from shared or contaminating cell populations, especially myeloid or other immune-related cells. It does not demonstrate that the conserved kidney and stem-cell module is kidney-specific or stem-cell-specific.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and no STRING functional enrichment was reported. No hu.MAP complex contained at least two module members. Thus, the co-abundance edges are not supported here as established physical protein interactions or membership in a known complex. The absence of STRING and hu.MAP support may reflect context dependence, incomplete coverage, transient interactions, or regulation at the expression-abundance level rather than protein binding.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears to be a potentially novel co-abundance pattern rather than a recognized molecular complex or canonical pathway. Supporting reasons are the lack of globally significant GO or KEGG enrichment, absence of STRING functional enrichment and high-confidence STRING pair support, and absence of a shared hu.MAP complex. However, these observations do not prove biological novelty: the module is small and sparse, the databases are incomplete, and co-abundance relationships can be tissue- or state-specific. The defensible conclusion is that the module is not readily explained by an already catalogued interaction complex, while its mechanistic novelty remains to be tested experimentally and in independent cohorts.

**Hypothesis.** Hypothesis: the conserved module reflects a shared intracellular state involving vesicle trafficking and membrane organization, with STX10 acting as the principal abundance-linked coordinator, RHOG contributing cytoskeletal and polarity signaling, CUX1 marking transcriptional or differentiation state, and RPUSD2 marking RNA-processing demand. In kidney and stem-cell samples, this state could arise from a shared cell population or a common cellular stress, differentiation, or trafficking program rather than from direct binding among all module proteins. This hypothesis predicts that module activity should track vesicle-trafficking and polarity markers, cell-composition markers, and potentially RNA-modification or differentiation states; these predictions are not established by the supplied data.

### Important genes

#### STX10

- **Related proteins** (co-abundance neighbors): RPUSD2 (0.93), CUX1 (0.87), RHOG (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntaxin 10. This gene belongs to the syntaxin family and encodes a soluble N-ethylmaleimide sensitive factor attachment protein receptor (SNARE). The encoded protein is involved in docking and fusion events at the Golgi apparatus. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2012].
- **Diseases (Open Targets)**: osteoarthritis, knee (0.312); venous thromboembolism (0.208); exfoliation syndrome (0.118); brain aneurysm (0.096); skin neoplasm (0.096)
- **Europe PMC papers**: 160
- **Why important**: STX10 is the network hub in the supplied subgraph, connecting to RPUSD2, CUX1, and RHOG. It encodes a Golgi-associated SNARE involved in docking, fusion, intracellular transport, and endosome-to-Golgi retrograde transport. Its central network position and direct relevance to vesicle biology make it the strongest candidate for representing the module's core cellular process. Its literature volume is more limited than that of CUX1 or RHOG, so the module-level interpretation should not rely on extensive prior literature alone.
- **Conclusion**: Established evidence supports STX10 as a Golgi and vesicle-trafficking protein and as the central abundance-linked gene in this module. It is plausible, but not established, that STX10 is the functional coordinator of the shared module or that its trafficking role explains the other genes.

#### RHOG

- **Related proteins** (co-abundance neighbors): STX10 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ras homolog family member G. This gene encodes a member of the Rho family of small GTPases, which cycle between inactive GDP-bound and active GTP-bound states and function as molecular switches in signal transduction cascades. Rho proteins promote reorganization of the actin cytoskeleton and regulate cell shape, attachment, and motility. The encoded protein facilitates translocation of a functional guanine nucleotide exchange…
- **Diseases (Open Targets)**: atrial fibrillation (0.428); cancer (0.373); kidney transplant (0.296); eosinophilic esophagitis (0.239); cardiac arrhythmia (0.128)
- **Europe PMC papers**: 1929
- **Why important**: RHOG is directly connected to STX10 in the module. It is a Rho-family small GTPase involved in actin organization, cell polarity, cell shape, motility, and signal transduction. Its bone-marrow tissue enhancement and enrichment across several immune or myeloid-associated cell types provide a possible cell-state or cell-composition link between samples. Its disease associations include kidney transplant and cancer, and it has substantial literature coverage.
- **Conclusion**: Established evidence supports RHOG as a regulator of cytoskeletal organization and polarity, with HPA evidence for a bone-marrow and cell-type-associated pattern. A role connecting trafficking to cytoskeletal remodeling in this module is a reasonable hypothesis, but direct cooperation with STX10 is not demonstrated because STRING reports no qualifying interaction.

#### CUX1

- **Related proteins** (co-abundance neighbors): CUX1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Golgi apparatus; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cut like homeobox 1. The protein encoded by this gene is a member of the homeodomain family of DNA binding proteins. It may regulate gene expression, morphogenesis, and differentiation and it may also play a role in the cell cycle progession. Several alternatively spliced transcript variants encoding different isoforms have been identified.[provided by RefSeq, Feb 2011].
- **Diseases (Open Targets)**: global developmental delay with or without impaired intellectual development (0.754); cancer (0.588); myelodysplastic syndrome (0.536); hereditary disease (0.519); acute lymphoblastic leukemia (0.509)
- **Europe PMC papers**: 3914
- **Why important**: CUX1 is linked to STX10 in the supplied module network. It encodes a homeobox-family DNA-binding regulator associated with transcriptional regulation, differentiation, cell-cycle progression, and intra-Golgi vesicle-mediated transport. It has the largest literature volume among the listed genes and strong disease associations involving developmental delay, cancer, myelodysplastic syndrome, and acute lymphoblastic leukemia. Its neutrophil and non-classical-monocyte patterns may also indicate a shared cellular composition component.
- **Conclusion**: Established evidence supports CUX1 as a transcriptional and differentiation regulator with additional reported Golgi-related annotation. Its network association with STX10 may indicate coordinated cellular state rather than direct molecular interaction. The proposed role of CUX1 as a transcriptional marker of the module is plausible but not proven by enrichment or physical-interaction evidence.

#### RPUSD2

- **Related proteins** (co-abundance neighbors): STX10 (0.93); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Microtubules; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA pseudouridine synthase domain containing 2. Enables pseudouridine synthase activity. Involved in mRNA pseudouridine synthesis. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: retinitis pigmentosa (0.071); cone-rod dystrophy (0.065); exudative vitreoretinopathy (0.064); Leber congenital amaurosis (0.061); Abnormality of refraction (0.056)
- **Europe PMC papers**: 130
- **Why important**: RPUSD2 is connected to the STX10 hub. It encodes a pseudouridine synthase-domain protein involved in RNA pseudouridine synthesis, RNA processing, and RNA modification, including reported mRNA, rRNA, and tRNA-related functions. Its disease associations include several inherited retinal disorders, and it has a smaller but meaningful literature base. It provides the module with a distinct RNA-processing dimension that is not supplied by the trafficking and cytoskeletal genes.
- **Conclusion**: Established evidence supports RPUSD2 as an RNA pseudouridine-modification factor. Its co-abundance with STX10 could reflect a broader cellular state involving coordinated RNA processing and membrane trafficking, but there is no evidence here that RPUSD2 directly interacts with STX10 or that RNA modification is a significant module-level pathway.

## Module 9

**Tissue pair**: kidney and stem_cells  
**Genes (5)**: CD9, ERMP1, PHLDB1, ARHGAP18, SCRN1

### Function

The module does not have a globally significant GO or KEGG enrichment term, so its function cannot be assigned from enrichment alone. The gene annotations and network structure instead suggest a membrane-associated cellular organization module linking endoplasmic-reticulum stress and proteolysis through ERMP1 with Rho-regulated actin organization through ARHGAP18, basement-membrane and epithelial-transition processes through PHLDB1, exocytosis through SCRN1, and cell adhesion, differentiation, and signal transduction through CD9. ERMP1 is the central co-abundance node, while the other genes form a set of peripheral partners. This supports a cautious interpretation involving membrane organization, trafficking or exocytosis, cytoskeletal remodeling, and cellular stress responses rather than a single established pathway.

**Cell composition.** The module is not predominantly composed of plasma proteins or classically secreted proteins. HPA reports one secreted gene at the module level, while CD9 is specifically annotated as intracellular and membrane-associated. The genes show mixed tissue and cell-type patterns: several have cell-type-enhanced expression, including epithelial, respiratory, stromal, adipocyte, platelet or megakaryocyte, mast-cell, and neural-associated populations. Blood-cell specificity is heterogeneous rather than uniformly immune-cell enriched. All module proteins are detected in kidney, whereas HPA has no matching stem-cell tissue category. Consequently, the shared signal could reflect a broadly shared cellular program, a common epithelial or stromal component, or sample cell composition; the evidence does not support attributing it specifically to blood contamination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and STRING functional enrichment is absent. No hu.MAP complex contains multiple module members. Thus, the co-abundance relationships are not corroborated here as established physical protein interactions or as a known multiprotein complex. The absence of STRING and hu.MAP support does not invalidate the co-abundance module; it indicates that the observed coordination may be tissue- or state-dependent, indirect, transient, or previously uncharacterized.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a novel candidate co-abundance association rather than an established molecular complex or pathway. Its novelty is supported by the lack of reported high-confidence STRING relationships, the lack of a shared hu.MAP complex, and the absence of globally significant GO or KEGG enrichment. However, these absences do not prove that the biology is new: the module may combine known functions through indirect regulation, shared cell composition, or context-specific coordination. The appropriate conclusion is that the kidney–stem-cell conservation of this small co-abundance pattern merits validation, not that a new biochemical complex has been discovered.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular-state program in which ERMP1-associated endoplasmic-reticulum proteostasis and oxidative-stress responses are coordinated with CD9-dependent membrane organization, SCRN1-linked exocytosis, ARHGAP18-mediated actin remodeling, and PHLDB1-associated basement-membrane or epithelial-transition processes. In kidney and stem-cell-related samples, this could represent coordinated membrane trafficking and remodeling during epithelial maintenance, differentiation, or stress adaptation. A competing hypothesis is that the pattern is driven partly by shared epithelial or stromal cell populations rather than by direct regulation among the proteins. This should be tested with cell-resolved expression, perturbation, and protein-interaction experiments.

### Important genes

#### ERMP1

- **Related proteins** (co-abundance neighbors): ARHGAP18 (0.84), PHLDB1 (0.83), SCRN1 (0.83), CD9 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: endoplasmic reticulum metallopeptidase 1. Predicted to enable metal ion binding activity and metalloexopeptidase activity. Involved in cellular response to oxidative stress. Acts upstream of or within endoplasmic reticulum unfolded protein response. Located in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); Catifa syndrome (0.157); Abnormality of the skeletal system (0.152); hair color (0.147); autism (0.111)
- **Europe PMC papers**: 332
- **Why important**: ERMP1 is the central node of the module, co-abundant with every other member and therefore the strongest organizing feature of the network. Its annotation links membrane localization, metal-ion binding, metalloexopeptidase activity, proteolysis, oxidative-stress response, and the endoplasmic-reticulum unfolded-protein response. It has kidney protein detection, tissue enhancement in parathyroid gland, cell-type enhancement in epicardial cells, and an immune-cell association with NK cells. Its literature volume is substantial, although smaller than that of CD9.
- **Conclusion**: Established evidence supports ERMP1 as the network-centered proteostasis and stress-response candidate. It is plausible that ERMP1 helps define the module's cellular state, but the co-abundance data do not establish that it directly regulates the other genes or that its enzymatic activity causes the shared pattern.

#### CD9

- **Related proteins** (co-abundance neighbors): ERMP1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD9 molecule. This gene encodes a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Tetraspanins are cell surface glycoproteins with four transmembrane domains that form multimeric complexes with other cell surface proteins. The encoded protein functions in many cellular processes including differentiation, adhesion, and signal transduction, and expression of this gene plays a cri…
- **Diseases (Open Targets)**: diphtheria (0.527); breast cancer (0.348); poisoning (0.136); response to xenobiotic stimulus (0.136); rheumatic disorder (0.122)
- **Europe PMC papers**: 23911
- **Why important**: CD9 is a plasma-membrane tetraspanin involved in cell adhesion, differentiation, fusion, and signal transduction. It is co-abundant with ERMP1 and has the largest literature volume in the module, making it the best-characterized interface with membrane organization and cell-surface biology. HPA places it in epithelial and respiratory cell types, reports group enrichment in basophils and eosinophils, and detects the protein in kidney. Its intracellular and membrane annotation argues against treating it as a freely secreted plasma protein.
- **Conclusion**: Established evidence supports CD9 as a membrane-organization and adhesion marker that could connect the module to epithelial or cell-composition effects. Its central biological relevance is strong, but the module does not show that CD9 physically binds ERMP1 or that CD9 is the driver of the conserved co-abundance pattern.

#### SCRN1

- **Related proteins** (co-abundance neighbors): ERMP1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: secernin 1. This gene likely encodes a member of the secernin family of proteins. A similar protein in rat functions in regulation of exocytosis in mast cells. Alternatively spliced transcript variants have been described. [provided by RefSeq, Mar 2009].
- **Diseases (Open Targets)**: psoriasis (0.249); diabetes mellitus (0.216); food allergy (0.202); type 2 diabetes mellitus (0.198); Familial prostate cancer (0.157)
- **Europe PMC papers**: 406
- **Why important**: SCRN1 contributes a functionally distinctive exocytosis annotation and is also associated with proteolysis and regulation of the synaptic-vesicle cycle. It is co-abundant with the central ERMP1 node, has tissue enhancement in brain, and is detected in kidney. Its literature volume is moderate, and its known role in secretion-related processes gives it a mechanistic bridge between membrane organization and regulated cargo release.
- **Conclusion**: Established evidence supports SCRN1 as an exocytosis-related component of the module. Its participation in a kidney–stem-cell membrane-trafficking program is a hypothesis derived from the network context, not a demonstrated role in those tissues.

#### ARHGAP18

- **Related proteins** (co-abundance neighbors): ERMP1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho GTPase activating protein 18. ARHGAP18 belongs to a family of Rho (see MIM 165390) GTPase-activating proteins that modulate cell signaling (Potkin et al., 2009 [PubMed 19065146]).[supplied by OMIM, Apr 2010]
- **Diseases (Open Targets)**: obesity disorder (0.342); immune system disorder (0.314); aortic disorder (0.280); prostatitis (0.234); metabolic disease (0.209)
- **Europe PMC papers**: 529
- **Why important**: ARHGAP18 is the module's annotated regulator of Rho-family small-GTPase signaling, actin filament polymerization, cell shape, and cytoskeletal organization. Although it is peripheral in the module and linked directly only to ERMP1, these functions provide a plausible structural counterpart to the membrane and exocytosis annotations. HPA reports broad tissue specificity, several enhanced cell types including lactating, ciliated, mast, megakaryocyte, and platelet populations, and kidney protein detection. Its literature volume is moderate.
- **Conclusion**: Established evidence supports ARHGAP18 as a cytoskeletal and cell-shape regulator. The hypothesis that it coordinates with ERMP1-dependent stress or membrane processes is consistent with the module but is not established by STRING, hu.MAP, or the co-abundance data.

#### PHLDB1

- **Related proteins** (co-abundance neighbors): ERMP1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pleckstrin homology like domain family B member 1. Involved in regulation of embryonic development; regulation of epithelial to mesenchymal transition; and regulation of microtubule cytoskeleton organization. Located in basal cortex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: glioma (0.493); central nervous system cancer (0.481); presbycusis (0.472); hearing loss disorder (0.466); osteogenesis imperfecta, type 23 (0.462)
- **Europe PMC papers**: 408
- **Why important**: PHLDB1 is linked to embryonic development, epithelial-to-mesenchymal transition, microtubule organization, and basement-membrane organization. It is a peripheral partner of ERMP1 and is detected in kidney. Its enhanced cell-type pattern spans adipocyte, stromal, Leydig, and oligodendrocyte-progenitor populations, indicating relevance to differentiated and structural cell states rather than a uniform immune program. Its literature volume is moderate.
- **Conclusion**: Established evidence supports PHLDB1 as a structural and developmental regulator associated with epithelial or basement-membrane biology. Its inclusion in this module may indicate tissue architecture or differentiation state, but a direct mechanistic connection to ERMP1 or the other module members remains hypothetical.

## Module 10

**Tissue pair**: kidney and stem_cells  
**Genes (6)**: COG2, GCC1, ITGA6, LMO7, SSH3, ZFAND5

### Function

The module does not have a statistically supported GO or KEGG functional label: no term passed global correction. Its observed structure is a sparse co-abundance chain linking SSH3 with ZFAND5 and LMO7, and linking SSH3 with COG2, while COG2 connects with ITGA6 and ITGA6 connects with GCC1. The gene annotations suggest several related but not unified processes: actin and cell-adhesion biology through SSH3, LMO7, and ITGA6; Golgi organization and membrane trafficking through COG2 and GCC1; and less-established regulatory functions for ZFAND5. Thus, the most defensible interpretation is a mixed epithelial or tissue-structure-associated module involving cytoskeletal regulation, adhesion, and intracellular trafficking, rather than a demonstrated single pathway. The absence of global GO or KEGG enrichment does not invalidate the co-abundance pattern.

**Cell composition.** The module is not dominated by secreted proteins, because none of its genes is annotated as secreted. It is also not uniformly blood-cell enriched: three genes have low immune-cell specificity, whereas three show immune-cell enhancement, including eosinophil, basophil, or naive CD4 T-cell associations. HPA annotations instead show a mixed composition with tissue-enhanced genes and several cell-type-enhanced genes. Urothelial and esophageal apical cell associations recur, and renal collecting duct intercalated cells are represented for ITGA6. The module may therefore reflect shared epithelial or specialized tissue cell states across kidney and stem-cell samples, with possible contribution from immune-cell composition. Protein detection in kidney supports that most module proteins are detectable there, but the stem-cell HPA comparison is unavailable and should not be inferred.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair meets the supplied high-confidence STRING interaction threshold, and no STRING functional-enrichment term is available. No hu.MAP complex contains multiple module members. Therefore, the co-abundance edges are not corroborated by the supplied STRING or hu.MAP evidence and should be interpreted as coordinated abundance relationships rather than established physical interactions or membership in a known complex. The strongest internal connections center on SSH3, COG2, and ITGA6, but this network topology alone does not establish direct molecular binding.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel cross-tissue co-abundance pattern, but it cannot be called a new biological discovery solely because it is absent from STRING and hu.MAP. The cautious novelty claim is that the particular kidney–stem-cell co-abundance organization, especially the combination of actin-associated, adhesion-associated, and Golgi-trafficking genes, is not explained by the supplied interaction or complex databases. Its biological novelty remains unvalidated because there is no globally significant GO or KEGG term, no STRING enrichment, and no independent experimental confirmation in the fact sheet. Replication in additional cohorts, cell-composition adjustment, and perturbation or localization studies would be needed.

**Hypothesis.** Hypothesis: the module reflects a shared epithelial or epithelial-like cell state in which cell–matrix adhesion and cortical actin remodeling are coordinated with Golgi-dependent membrane trafficking. In this model, ITGA6 marks adhesion and extracellular-matrix engagement, SSH3 and LMO7 participate in actin-associated regulation, and COG2 together with GCC1 supports the trafficking machinery needed to maintain the relevant membrane compartments. ZFAND5 may be a regulatory component associated with the SSH3-centered arm, but its role in this module is presently speculative. An alternative explanation is shared cell-type composition, including epithelial and immune contributions, rather than a single intracellular pathway.

### Important genes

#### SSH3

- **Related proteins** (co-abundance neighbors): ZFAND5 (0.88), LMO7 (0.86), COG2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nuclear speckles, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: slingshot protein phosphatase 3. The ADF (actin-depolymerizing factor)/cofilin family (see MIM 601442) is composed of stimulus-responsive mediators of actin dynamics. ADF/cofilin proteins are inactivated by kinases such as LIM domain kinase-1 (LIMK1; MIM 601329). The SSH family appears to play a role in actin dynamics by reactivating ADF/cofilin proteins in vivo (Niwa et al., 2002 [PubMed 11832213]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: placental abruption (0.326); osteoarthritis (0.173); hepatocellular carcinoma (0.075); rheumatic disorder (0.057); response to xenobiotic stimulus (0.057)
- **Europe PMC papers**: 310
- **Why important**: SSH3 is the most connected node in the module and links the cytoskeletal arm to COG2, ZFAND5, and LMO7. Its established annotation places it in actin dynamics through reactivation of ADF/cofilin proteins, and its GO descriptions include actin cytoskeleton organization and negative regulation of actin filament polymerization. It is detected in kidney and has a substantial literature base. HPA also reports associations with epithelial cell types and immune-cell enhancement.
- **Conclusion**: Established evidence supports SSH3 as the strongest candidate for an actin-regulatory hub in this co-abundance pattern. It is plausible, but not proven, that SSH3 coordinates the adhesion and trafficking-related arms of the module.

#### ITGA6

- **Related proteins** (co-abundance neighbors): COG2 (0.89), GCC1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha 6. The gene encodes a member of the integrin alpha chain family of proteins. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha 6 subunit. This subunit may associate with a beta 1 or beta…
- **Diseases (Open Targets)**: junctional epidermolysis bullosa with pyloric atresia (0.704); epidermolysis bullosa, junctional 6, with pyloric atresia (0.622); prostate carcinoma (0.528); Varicose veins (0.412); prostate cancer (0.408)
- **Europe PMC papers**: 53735
- **Why important**: ITGA6 connects the COG2 and GCC1 trafficking-related side of the graph hu.MAP and has the clearest cell-adhesion annotation. It encodes an integrin alpha subunit involved in cell–matrix adhesion and integrin-mediated signaling, with associations to beta one or beta four integrin complexes. HPA links it to renal collecting duct intercalated cells and other specialized epithelial populations, and its disease literature is extensive, including junctional epidermolysis bullosa and cancer-related associations.
- **Conclusion**: Established evidence supports ITGA6 as an adhesion and membrane-signaling marker that could explain the epithelial component of the module. Its role as a functional bridge to Golgi genes is a hypothesis based on co-abundance topology, not a demonstrated physical interaction.

#### COG2

- **Related proteins** (co-abundance neighbors): ITGA6 (0.89), SSH3 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: component of oligomeric golgi complex 2. This gene encodes a subunit of the conserved oligomeric Golgi complex that is required for maintaining normal structure and activity of the Golgi complex. The encoded protein specifically interacts with the USO1 vesicle docking protein and may be necessary for normal Golgi ribbon formation and trafficking of Golgi enzymes. Mutations of this gene are associated with abnormal glycosylation within th…
- **Diseases (Open Targets)**: congenital disorder of glycosylation, type IIq (0.671); neurodegenerative disease (0.474); congenital disorder of glycosylation type II (0.462); spinal cord disorder (0.215); polycystic ovary syndrome (0.214)
- **Europe PMC papers**: 378
- **Why important**: COG2 is an internal connector between ITGA6 and SSH3. It is an established subunit of the conserved oligomeric Golgi complex and is annotated in Golgi organization, intra-Golgi vesicle transport, retrograde transport, and vesicle recycling. Its disease associations include congenital disorders of glycosylation. HPA reports tissue enhancement in parathyroid gland and localization to the Golgi apparatus.
- **Conclusion**: Established evidence supports COG2 as the strongest trafficking and Golgi-maintenance representative in the module. The proposed coordination of Golgi function with actin and adhesion is biologically plausible but remains unproven for this specific module.

#### LMO7

- **Related proteins** (co-abundance neighbors): SSH3 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LIM domain 7. This gene encodes a protein containing a calponin homology (CH) domain, a PDZ domain, and a LIM domain, and may be involved in protein-protein interactions. Several alternatively spliced transcript variants encoding different isoforms have been found for this gene, however, the full-length nature of some variants is not known. [provided by RefSeq, Jan 2009].
- **Diseases (Open Targets)**: cancer (0.473); neurodegenerative disease (0.436); open-angle glaucoma (0.395); presbycusis (0.377); glaucoma (0.362)
- **Europe PMC papers**: 1196
- **Why important**: LMO7 is connected to SSH3 and is localized to actin filaments. Its domain composition supports protein-interaction functions, and its annotations include regulation of cell adhesion, signaling, and transcriptional regulation. HPA reports enhancement in several epithelial cell types and in heart muscle, while disease associations include cancer, neurodegenerative disease, and glaucoma.
- **Conclusion**: Established evidence supports LMO7 as an actin-associated adhesion regulator and a plausible partner of the SSH3-centered structural arm. The module-specific connection is supported only by co-abundance, because STRING and hu.MAP provide no corroborating relationship here.

#### GCC1

- **Related proteins** (co-abundance neighbors): ITGA6 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Golgi apparatus; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GRIP and coiled-coil domain containing 1. The protein encoded by this gene is a peripheral membrane protein. It is sensitive to brefeldin A. This encoded protein contains a GRIP domain which is thought to be used in targeting. It may play a role in the organization of trans-Golgi network subcompartment involved with membrane transport. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.367); type 2 diabetes mellitus (0.323); duodenal ulcer (0.216); peptic ulcer disease (0.114); gestational diabetes (0.108)
- **Europe PMC papers**: 281
- **Why important**: GCC1 is connected to ITGA6 and is annotated as a peripheral membrane protein involved in organization of a trans-Golgi-network subcompartment and membrane transport. HPA reports group enrichment in cardiomyocytes, spermatids, and epicardial cells, and its disease literature includes neurodegenerative and metabolic disease associations.
- **Conclusion**: Established evidence supports GCC1 as a membrane-trafficking component that complements the COG2 annotation. Its participation in an adhesion-linked trafficking program is a reasonable hypothesis, but there is no direct interaction or complex evidence in the supplied databases.

## Module 11

**Tissue pair**: kidney and stem_cells  
**Genes (5)**: COQ9, DHRS1, DHODH, SIRT3, ACAA1

### Function

The module is most consistent with coordinated cellular metabolism centered on mitochondrial and peroxisomal functions. SIRT3 is a mitochondrial deacetylase associated with respiration, stress responses, and metabolic control; COQ9 supports ubiquinone biosynthesis; DHODH links mitochondrial quinone-dependent respiration to de novo pyrimidine synthesis; and ACAA1 supports peroxisomal fatty-acid beta-oxidation. DHRS1 adds a probable oxidoreductase component. The co-abundance structure, with SIRT3 as the most connected gene and links from SIRT3 to COQ9, DHODH, and ACAA1, supports a metabolic-state interpretation. However, no GO or KEGG term passed global correction, and there was no supplementary STRING enrichment. Thus, this is a biologically motivated functional interpretation rather than a statistically confirmed pathway enrichment.

**Cell composition.** The module does not appear to be driven by plasma proteins, secreted proteins, or blood-cell contamination: all genes are non-secreted according to the HPA summary, and every gene has low immune-cell specificity. Protein detection is present for the module genes in kidney, supporting relevance to the kidney tissue. HPA patterns point mainly toward metabolic and tissue-associated expression rather than a single shared cell type: liver is the most recurrent enriched tissue, with additional signals involving kidney, skeletal muscle, tongue, and esophagus. Several genes show cell-type enhancement across hepatocytes, gastrointestinal epithelial cells, cardiomyocytes, glial populations, and other cell types. This breadth argues against a narrowly kidney-specific or stem-cell-specific marker module and is compatible with a broadly distributed metabolic program. The absence of a matching HPA stem-cell tissue category limits direct interpretation in stem cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair reaches the stated high-confidence STRING interaction threshold, and no hu.MAP complex contains multiple module members. Therefore, the co-abundance links should not be interpreted as established physical protein interactions or as a known multiprotein complex. The absence of STRING and hu.MAP support suggests that the module may capture coordinated regulation, shared cellular state, or tissue composition rather than a canonical molecular complex. The strongest internal co-abundance relationships are SIRT3 with DHODH, ACAA1, and COQ9, together with the COQ9-DHRS1 relationship, but these relationships remain module-specific observations rather than independently validated interactions.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported co-abundance pattern because its member combination has no high-confidence STRING relationships, no shared hu.MAP complex, and no globally significant GO or KEGG enrichment. Nevertheless, these absences do not establish novelty: database coverage is incomplete, co-abundance is distinct from physical interaction, and the individual biochemical functions are already well established. The defensible conclusion is that the integrated module-level association appears potentially novel, while a claim of a new biological pathway or mechanism would be premature.

**Hypothesis.** Hypothesis: in kidney and stem-cell-associated samples, a shared metabolic state may coordinate mitochondrial redox and respiratory capacity with quinone production, pyrimidine synthesis, and peroxisomal lipid oxidation. SIRT3 could act as a central metabolic and stress-response regulator, while COQ9 and DHODH could couple ubiquinone-related mitochondrial activity to nucleotide production, and ACAA1 could reflect linked lipid-processing demand. DHRS1 may contribute redox balancing. This hypothesis predicts coordinated changes in mitochondrial function, coenzyme Q metabolism, pyrimidine synthesis, and peroxisomal fatty-acid oxidation, but the current module does not establish causality, directionality, or direct protein interaction.

### Important genes

#### SIRT3

- **Related proteins** (co-abundance neighbors): DHODH (0.87), ACAA1 (0.85), COQ9 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sirtuin 3. SIRT3 encodes a member of the sirtuin family of class III histone deacetylases, homologs to the yeast Sir2 protein. The encoded protein is found exclusively in mitochondria, where it can eliminate reactive oxygen species, inhibit apoptosis, and prevent the formation of cancer cells. SIRT3 has far-reaching effects on nuclear gene expression, cancer, cardiovascular disease, neuroprotection, aging, a…
- **Diseases (Open Targets)**: uterine corpus leiomyoma (0.399); neurodegenerative disease (0.192); neoplasm (0.118); acute kidney injury (0.115); hepatocellular carcinoma (0.115)
- **Europe PMC papers**: 14006
- **Why important**: SIRT3 has the highest weighted degree in the module and connects to DHODH, ACAA1, and COQ9. Its established mitochondrial localization and roles in protein deacetylation, aerobic respiration, reactive-oxygen control, apoptosis inhibition, stress responses, and metabolic regulation make it the strongest candidate for a coordinating role. It also has extensive literature coverage and disease associations involving kidney injury, cancer, cardiovascular disease, neuroprotection, aging, and metabolic control.
- **Conclusion**: Established evidence supports SIRT3 as the central mitochondrial metabolic and stress-response gene in this module. It is reasonable to regard SIRT3 as an interpretive hub because of its network position and known biology. It remains a hypothesis, not an established fact, that SIRT3 drives the co-abundance of the other genes.

#### COQ9

- **Related proteins** (co-abundance neighbors): DHRS1 (0.86), SIRT3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coenzyme Q9. This locus represents a mitochondrial ubiquinone biosynthesis gene. The encoded protein is likely necessary for biosynthesis of coenzyme Q10, as mutations at this locus have been associated with autosomal-recessive neonatal-onset primary coenzyme Q10 deficiency.[provided by RefSeq, Sep 2010].
- **Diseases (Open Targets)**: encephalopathy-hypertrophic cardiomyopathy-renal tubular disease syndrome (0.766); coenzyme Q10 deficiency (0.635); hereditary disease (0.415); mitochondrial disease (0.372); coenzyme Q10 deficiency, primary, 1 (0.370)
- **Europe PMC papers**: 958
- **Why important**: COQ9 is directly connected to SIRT3 and DHRS1 and is located in mitochondria and cytosol. Its established role in coenzyme Q biosynthesis gives the module a concrete respiratory and redox-related component. COQ9 has disease associations with primary coenzyme Q deficiency, mitochondrial disease, encephalopathy, hypertrophic cardiomyopathy, and renal tubular disease, making it especially relevant to a kidney-linked module.
- **Conclusion**: Established evidence supports COQ9 as a mitochondrial ubiquinone-biosynthesis component with clinically relevant links to renal and mitochondrial disease. Its connection to SIRT3 is a module observation, not a confirmed physical interaction. The hypothesis that COQ9 helps couple respiratory redox capacity to the broader module is biologically plausible but unproven.

#### DHODH

- **Related proteins** (co-abundance neighbors): SIRT3 (0.87); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dihydroorotate dehydrogenase (quinone). The protein encoded by this gene catalyzes the fourth enzymatic step, the ubiquinone-mediated oxidation of dihydroorotate to orotate, in de novo pyrimidine biosynthesis. This protein is a mitochondrial protein located on the outer surface of the inner mitochondrial membrane. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: postaxial acrofacial dysostosis (0.832); rheumatoid arthritis (0.604); psoriatic arthritis (0.523); familial hyperlipidemia (0.377); arthritic joint disease (0.373)
- **Europe PMC papers**: 3668
- **Why important**: DHODH is connected to SIRT3 and provides a distinct biochemical bridge between mitochondrial quinone-dependent electron handling and de novo pyrimidine biosynthesis. It is mitochondrial, enriched in liver, and enhanced in cardiomyocytes, epicardial cells, and hepatocytes. Its disease associations include developmental, inflammatory, lipid, and arthritic conditions, and it has substantial literature coverage.
- **Conclusion**: Established evidence supports DHODH as a mitochondrial enzyme required for de novo pyrimidine production and linked to ubiquinone-mediated oxidation. Its placement beside SIRT3 suggests coordinated mitochondrial and biosynthetic activity in this module. The proposed role as a connector between respiratory redox state and nucleotide demand remains a hypothesis.

#### ACAA1

- **Related proteins** (co-abundance neighbors): SIRT3 (0.85); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Peroxisomes; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA acyltransferase 1. This gene encodes an enzyme operative in the beta-oxidation system of the peroxisomes. Deficiency of this enzyme leads to pseudo-Zellweger syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: hyperpituitarism (0.348); Follicular Cyst (0.127); Sepsis (0.103); neoplasm (0.098); Alzheimer disease (0.082)
- **Europe PMC papers**: 1153
- **Why important**: ACAA1 connects to SIRT3 and is the module gene most directly associated with peroxisomal lipid catabolism. It catalyzes a step in fatty-acid beta-oxidation and is associated with very-long-chain fatty-acid and bile-acid metabolism. HPA identifies kidney and liver as group-enriched tissues and shows enhancement in absorptive and hepatic epithelial cell types. Its disease relevance includes deficiency causing pseudo-Zellweger syndrome.
- **Conclusion**: Established evidence supports ACAA1 as a peroxisomal fatty-acid oxidation enzyme with kidney- and liver-associated expression. Its co-abundance with SIRT3 may reflect coordinated mitochondrial-peroxisomal metabolic demand, but the current data do not demonstrate metabolic flux, organelle communication, or regulation by SIRT3.

#### DHRS1

- **Related proteins** (co-abundance neighbors): COQ9 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dehydrogenase/reductase 1. This gene encodes a member of the short-chain dehydrogenases/reductases (SDR) family. The encoded enzyme contains a conserved catalytic domain and likely functions as an oxidoreductase. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Nov 2008].
- **Diseases (Open Targets)**: essential tremor (0.092); episodic kinesigenic dyskinesia 1 (0.085); hereditary geniospasm (0.083); young-onset Parkinson disease (0.080); hepatocellular carcinoma (0.080)
- **Europe PMC papers**: 208
- **Why important**: DHRS1 is connected to COQ9 and encodes a short-chain dehydrogenase/reductase-family protein with a conserved catalytic domain and probable oxidoreductase activity. It has tissue enhancement in esophagus and liver and cell-type enhancement across several neural, epithelial, and germ-cell populations. Although its literature volume and functional annotation are more limited than those of the other selected genes, it may add a redox-related enzymatic component to the module.
- **Conclusion**: Established evidence supports DHRS1 as a probable oxidoreductase with broad and heterogeneous tissue or cell-type associations. Its connection to COQ9 makes it relevant to the module's redox interpretation, but its exact biochemical substrate and role in this co-abundance pattern are unresolved. Any proposed participation in mitochondrial or broader metabolic coordination is therefore a hypothesis.

## Module 12

**Tissue pair**: kidney and stem_cells  
**Genes (11)**: DIAPH3, DRG2, GGPS1, GNA13, NES, PRXL2B, SNTB1, SSR1, HARS2, TBC1D4, UFSP2

### Function

The module does not support a single statistically established GO or KEGG function: no GO/KEGG term passed global correction. Its sparse co-abundance structure is organized around SNTB1, with smaller links connecting cytoskeletal, vesicle-trafficking, mitochondrial translation, endoplasmic-reticulum targeting, GTPase, and isoprenoid-related genes. The annotations suggest a possible convergence of cellular architecture, intracellular trafficking, protein synthesis and proteostasis, but this is an integrative interpretation rather than a globally significant pathway assignment.

**Cell composition.** The module is not dominated by plasma or secreted proteins; none of its members is annotated as secreted. It is also not broadly characterized as an immune or blood-cell module: most genes have low immune-cell specificity, with one gene immune-cell enhanced and two not detected in immune cells. The composition is heterogeneous, with tissue enhancement across liver, skeletal muscle, heart muscle, brain, bone marrow and testis, and cell-type enhancement in epithelial, stromal, muscle, reproductive and neural populations. Therefore, the shared signal is more consistent with a mixture of cell-state or structural programs than with a plasma-protein or general blood-contamination signature. Kidney protein detection is widespread among the module members, whereas the supplied HPA resource has no matching stem-cell tissue category, so the stem-cell interpretation cannot be assessed directly from HPA.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes. No STRING functional-enrichment result was reported, and no hu.MAP complex contained multiple module members. Thus, the co-abundance relationships are not simply a recovery of a known high-confidence physical interaction network or a known multi-subunit complex. The absence of database support also means that the edges should be interpreted primarily as coordinated abundance relationships, not as demonstrated direct protein contacts.

**STRING interactions (score >= 0.7)**: 0 of 55 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module is potentially novel as a cross-tissue co-abundance pattern because its member combination and internal edges are not represented by high-confidence STRING interactions or shared hu.MAP complexes. However, that evidence is insufficient to claim a new molecular pathway. The heterogeneous HPA tissue and cell-type profile, the lack of globally significant GO/KEGG enrichment, and the sparse network leave open explanations involving shared cellular composition, coordinated regulation, or technical and sampling effects. The strongest defensible conclusion is that the co-abundance configuration is a candidate novel module requiring replication and perturbational validation.

**Hypothesis.** Hypothesis: the module may represent a coordinated cellular-maintenance program in kidney and stem-cell-associated samples that couples cytoskeletal or membrane organization with intracellular trafficking, protein synthesis, and stress or proteostasis control. SNTB1 may organize the co-abundance pattern, while TBC1D4 and DIAPH3 connect trafficking and cytoskeletal remodeling, NES marks a structural or progenitor-like state, and HARS2 and UFSP2 provide mitochondrial translation and protein-quality-control components. This model predicts that the module will track a defined cell state or tissue subpopulation rather than a single canonical pathway, and that its reproducibility should be tested across independent cohorts and cell-composition estimates.

### Important genes

#### SNTB1

- **Related proteins** (co-abundance neighbors): PRXL2B (0.90), NES (0.87), UFSP2 (0.87), HARS2 (0.85), DRG2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntrophin beta 1. Dystrophin is a large, rod-like cytoskeletal protein found at the inner surface of muscle fibers. Dystrophin is missing in Duchenne Muscular Dystrophy patients and is present in reduced amounts in Becker Muscular Dystrophy patients. The protein encoded by this gene is a peripheral membrane protein found associated with dystrophin and dystrophin-related proteins. This gene is a member of the syntro…
- **Diseases (Open Targets)**: prostate carcinoma (0.468); type 2 diabetes mellitus (0.454); diabetes mellitus (0.443); ovarian dysfunction (0.383); liver disorder (0.370)
- **Europe PMC papers**: 537
- **Why important**: SNTB1 is the most central node in the module and connects PRXL2B, NES, UFSP2, HARS2 and DRG2. Its annotated role as a peripheral membrane protein associated with dystrophin-related proteins gives it a plausible structural role, while its kidney detection and epithelial-associated cell-type pattern provide tissue context. It has substantial literature and disease-linked evidence, although the supplied resources do not establish that it directly binds the other module members.
- **Conclusion**: Established: SNTB1 is the network's principal abundance correlate and has a documented membrane-associated cytoskeletal role. Hypothesis: SNTB1 may be a scaffold or marker of the cellular architecture underlying the module, but direct molecular bridging remains unproven.

#### TBC1D4

- **Related proteins** (co-abundance neighbors): DIAPH3 (0.85), DRG2 (0.81), GGPS1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TBC1 domain family member 4. This gene is a member of the Tre-2/BUB2/CDC16 domain family. The protein encoded by this gene is a Rab-GTPase-activating protein, and contains two phopshotyrosine-binding domains (PTB1 and PTB2), a calmodulin-binding domain (CBD), a Rab-GTPase domain, and multiple AKT phosphomotifs. This protein is thought to play an important role in glucose homeostasis by regulating the insulin-dependent traffic…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.355); alcohol drinking (0.344); Insulin resistance (0.338); type 1 diabetes mellitus (0.287); stroke disorder (0.286)
- **Europe PMC papers**: 1259
- **Why important**: TBC1D4 is an internal connector linking DIAPH3, DRG2 and GGPS1. Its annotated Rab-GTPase regulatory domains, insulin-responsive phosphorylation sites and role in GLUT4 trafficking provide a mechanistic link to vesicle movement and metabolic signaling. Its skeletal-muscle and cardiomyocyte associations, kidney detection and disease links to diabetes and insulin resistance make it biologically informative for a cross-tissue module.
- **Conclusion**: Established: TBC1D4 participates in insulin-dependent vesicle trafficking and is relevant to metabolic disease. Hypothesis: it may connect metabolic signaling to the structural and trafficking component of this module, but the co-abundance data do not demonstrate insulin dependence.

#### NES

- **Related proteins** (co-abundance neighbors): SNTB1 (0.87), SSR1 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nestin. This gene encodes a member of the intermediate filament protein family and is expressed primarily in nerve cells. [provided by RefSeq, Sep 2011].
- **Diseases (Open Targets)**: placental abruption (0.267); glioblastoma (0.119); central nervous system cancer (0.119); neoplasm (0.119); congenital fibrosis of the extraocular muscles (0.118)
- **Europe PMC papers**: 53286
- **Why important**: NES is connected to SNTB1 and SSR1 and is annotated as an intermediate-filament protein. Its association with podocytes, pericytes and other specialized cell types is relevant to kidney biology, while its developmental and cell-cycle annotations support a possible progenitor or remodeling state. NES has extensive literature relative to most module members, making it a strong biological anchor, although its broad developmental literature does not by itself identify the module's function.
- **Conclusion**: Established: NES is a structural intermediate-filament component with developmental and proliferative associations and is detected in kidney. Hypothesis: NES may mark the cellular state in which the module is active and may connect structural remodeling with ER-associated protein handling through SSR1.

#### DIAPH3

- **Related proteins** (co-abundance neighbors): TBC1D4 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Microtubules; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: diaphanous related formin 3. This gene encodes a member of the diaphanous subfamily of the formin family. Members of this family are involved in actin remodeling and regulate cell movement and adhesion. Mutations in this gene are associated with autosomal dominant auditory neuropathy 1. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss (0.574); smoking initiation (0.376); insomnia (0.342); metabolic syndrome X (0.319); endometriosis (0.314)
- **Europe PMC papers**: 1094
- **Why important**: DIAPH3 is the module's cytoskeletal remodeling member and is linked to TBC1D4. Its formin activity is annotated in actin organization, actin filament polymerization, cell movement and adhesion. Its HPA pattern includes bone marrow, testis, erythrocyte progenitors and germ-cell populations, and it has established disease association with auditory neuropathy.
- **Conclusion**: Established: DIAPH3 is a formin involved in actin remodeling and has a relevant developmental and disease literature. Hypothesis: DIAPH3 may provide the actin-based trafficking or adhesion arm of the module, but its shared abundance with TBC1D4 does not prove a direct functional partnership.

#### HARS2

- **Related proteins** (co-abundance neighbors): SNTB1 (0.85), GNA13 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: histidyl-tRNA synthetase 2, mitochondrial. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is an enzyme belonging to the class II family of aminoacyl-tRNA synthetases. Functioning in the synthesis of histidyl-transfer RNA, the enzyme plays an accessory role in the regulation of protein biosynthesis. The gene is located in a head-to-head orientation with HA…
- **Diseases (Open Targets)**: Perrault syndrome 2 (0.761); Perrault syndrome (0.596); neurodegenerative disease (0.424); sensorineural hearing loss disorder (0.374); Perrault syndrome 1 (0.370)
- **Europe PMC papers**: 460
- **Why important**: HARS2 links SNTB1 with GNA13 and is localized to mitochondria. It encodes a mitochondrial histidyl-tRNA synthetase involved in mitochondrial translation, providing a direct connection to protein biosynthetic capacity. Its association with Perrault syndrome and related disorders gives it strong disease relevance despite a more focused literature base than NES.
- **Conclusion**: Established: HARS2 is required for mitochondrial tRNA charging and mitochondrial translation and is associated with Perrault-spectrum disease. Hypothesis: HARS2 may indicate energetic or biosynthetic demand in the cell state represented by the module, rather than acting as a structural component of the network.

## Module 13

**Tissue pair**: kidney and stem_cells  
**Genes (5)**: FAF1, GAR1, HDAC1, POLR1B, ZC3HAV1L

### Function

The module is most consistent with a broadly expressed nuclear and nucleolar gene program related to ribosome biogenesis, ribosomal RNA production and modification, chromatin regulation, and control of protein turnover or apoptosis. GAR1 links the module to H/ACA snoRNP activity, rRNA pseudouridylation, and ribosome biogenesis, while POLR1B links it to RNA polymerase I transcription of ribosomal RNA. HDAC1 supports a chromatin and transcriptional-regulation component, and FAF1 supports apoptosis and ubiquitin-dependent protein catabolism. No GO/KEGG term passed global correction, so these functional interpretations come from the individual gene annotations and network organization rather than from globally significant enrichment. The module therefore appears to represent a shared cellular maintenance or biosynthetic program rather than a tissue-specific kidney or stem-cell pathway.

**Cell composition.** The genes are intracellular rather than plasma or secreted proteins, and the secretome contains none of them. HPA assigns low tissue specificity to every member, with kidney protein detection for several genes and no matching stem-cell tissue result. Most members also have low immune-cell specificity, although ZC3HAV1L is reported as immune-cell enriched in basophils. Cell-type-enhanced signals are scattered across syncytiotrophoblasts, germ-cell populations, adipocytes, adrenal medulla cells, and gonadotrophs rather than concentrated in kidney or stem cells. This pattern argues against a plasma-protein or blood-cell contamination explanation, while supporting the possibility that the shared module reflects broadly expressed cellular machinery or common cell-state features.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The network contains a high-confidence STRING relationship between GAR1 and POLR1B, providing independent support for a connection between nucleolar RNA processing and ribosomal RNA transcription. The remaining co-abundance links are not represented by high-confidence STRING partners in the supplied evidence, so co-abundance should not be treated as proof of direct physical interaction. No hu.MAP complex contains multiple module members. Thus, the module has a supported nucleolar core centered on GAR1 and POLR1B, but its broader structure may reflect coordinated regulation, shared expression state, or indirect cellular coupling rather than a single established multiprotein complex. STRING functional enrichment provided no supplementary terms.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: GAR1–POLR1B (0.775)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel tissue-pair co-abundance pattern, but the available evidence does not establish a new molecular complex or a newly discovered function. The GAR1–POLR1B relationship is already supported by STRING, and the functions of GAR1, POLR1B, HDAC1, and FAF1 are established individually. The absence of a multi-member hu.MAP complex and the limited STRING connectivity indicate that the exact five-gene co-abundance configuration is not strongly represented in the supplied reference resources, but absence from those resources alone cannot prove novelty. The strongest defensible claim is that this is a potentially novel shared co-abundance arrangement built partly from known nucleolar and regulatory biology.

**Hypothesis.** Hypothesis: kidney and stem-cell samples share a cellular state in which nucleolar ribosomal RNA production and modification are coordinated with chromatin regulation and stress or apoptosis-related protein control. GAR1 and POLR1B may form the functional nucleolar axis, HDAC1 may tune the transcriptional or chromatin environment, and FAF1 may connect this state to protein quality control or apoptotic signaling. ZC3HAV1L may mark a less characterized cytosolic regulatory component of the same state. This is a mechanistic hypothesis from co-abundance and annotations; direct biochemical coupling among all members requires experimental testing.

### Important genes

#### GAR1

- **Related proteins** (co-abundance neighbors): FAF1 (0.87), POLR1B (0.84), HDAC1 (0.82); STRING partners: POLR1B (0.775)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GAR1 ribonucleoprotein. This gene is a member of the H/ACA snoRNPs (small nucleolar ribonucleoproteins) gene family. snoRNPs are involved in various aspects of rRNA processing and modification and have been classified into two families: C/D and H/ACA. The H/ACA snoRNPs also include the DKC1, NOLA2 and NOLA3 proteins. These four H/ACA snoRNP proteins localize to the dense fibrillar components of nucleoli and to coiled (Ca…
- **Diseases (Open Targets)**: neurodegenerative disease (0.400); prostate carcinoma (0.198); Thrombocytopenia (0.048); familial primary hypomagnesemia with normocalciuria and normocalcemia (0.041); renal hypomagnesemia 2 (0.041)
- **Europe PMC papers**: 1232
- **Why important**: GAR1 is the central network gene, connecting the nucleolar POLR1B edge with FAF1 and HDAC1. Its established H/ACA snoRNP role, rRNA pseudouridylation, ribosome biogenesis, and telomere-maintenance annotations provide the clearest functional anchor for the module. It is detected in kidney, has nucleolar localization, has substantial literature support, and carries disease associations including neurodegenerative disease, prostate carcinoma, thrombocytopenia, and renal hypomagnesemia.
- **Conclusion**: Established evidence supports GAR1 as the best candidate for the module's nucleolar and ribosome-biogenesis anchor. Its central network position makes it a plausible organizing gene, but the co-abundance data do not prove that GAR1 physically recruits the other module members.

#### POLR1B

- **Related proteins** (co-abundance neighbors): GAR1 (0.84); STRING partners: GAR1 (0.775)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase I subunit B. Eukaryotic RNA polymerase I (pol I) is responsible for the transcription of ribosomal RNA (rRNA) genes and production of rRNA, the primary component of ribosomes. Pol I is a multisubunit enzyme composed of 6 to 14 polypeptides, depending on the species. Most of the mass of the pol I complex derives from the 2 largest subunits, Rpa1 and Rpa2 in yeast. POLR1B is homologous to Rpa2 (Seither and Grumm…
- **Diseases (Open Targets)**: Treacher Collins syndrome 4 (0.751); Treacher-Collins syndrome (0.383); arthropathy (0.212); Chronic Obstructive Asthma (0.188); lower respiratory tract disorder (0.124)
- **Europe PMC papers**: 521
- **Why important**: POLR1B is directly connected to GAR1 in STRING and occupies the nucleolar fibrillar center. As a subunit of RNA polymerase I, it is directly relevant to ribosomal RNA transcription, making it mechanistically complementary to GAR1-mediated rRNA processing and modification. It has established developmental and disease relevance through Treacher Collins syndrome associations and a substantial literature base.
- **Conclusion**: Established evidence supports POLR1B as the transcriptional counterpart to GAR1 in a nucleolar ribosome-production program. The module suggests coordinated activity of these processes, but does not demonstrate altered RNA polymerase I activity in either tissue group.

#### HDAC1

- **Related proteins** (co-abundance neighbors): GAR1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: histone deacetylase 1. Histone acetylation and deacetylation, catalyzed by multisubunit complexes, play a key role in the regulation of eukaryotic gene expression. The protein encoded by this gene belongs to the histone deacetylase/acuc/apha family and is a component of the histone deacetylase complex. It also interacts with retinoblastoma tumor-suppressor protein and this complex is a key element in the control of cell…
- **Diseases (Open Targets)**: neoplasm (0.573); primary cutaneous T-cell non-Hodgkin lymphoma (0.568); plasma cell myeloma (0.567); T-cell non-Hodgkin lymphoma (0.521); peripheral T-cell lymphoma, not otherwise specified (0.518)
- **Europe PMC papers**: 29753
- **Why important**: HDAC1 is connected to GAR1 and contributes a chromatin-regulatory axis through histone deacetylation, chromatin organization, chromatin remodeling, and transcriptional control. It is detected in kidney, is broadly expressed, has very extensive literature support, and has numerous neoplasm and lymphoid malignancy associations. Its position next to GAR1 makes it a candidate regulator of the nuclear state represented by the module.
- **Conclusion**: Established evidence supports HDAC1 as a chromatin and transcriptional regulator that could accompany nucleolar activity. Its role as a causal bridge between chromatin regulation and the GAR1–POLR1B axis remains hypothetical in this module.

#### FAF1

- **Related proteins** (co-abundance neighbors): GAR1 (0.87), ZC3HAV1L (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Fas associated factor 1. Interaction of Fas ligand (TNFSF6) with the FAS antigen (TNFRSF6) mediates programmed cell death, also called apoptosis, in a number of organ systems. The protein encoded by this gene binds to FAS antigen and can initiate apoptosis or enhance apoptosis initiated through FAS antigen. Initiation of apoptosis by the protein encoded by this gene requires a ubiquitin-like domain but not the FAS-binding…
- **Diseases (Open Targets)**: diabetes mellitus (0.354); atrial fibrillation (0.341); renal carcinoma (0.340); type 2 diabetes mellitus (0.340); hypothyroidism (0.315)
- **Europe PMC papers**: 1111
- **Why important**: FAF1 links GAR1 to ZC3HAV1L and provides the module with an apoptosis and protein-quality-control dimension. Its annotations include Fas signaling, positive regulation of apoptosis, ubiquitin-dependent protein catabolism, and ER-associated degradation. It is detected in kidney, has substantial literature support, and is associated with renal carcinoma, diabetes mellitus, atrial fibrillation, and other disorders.
- **Conclusion**: Established evidence supports FAF1 as a regulator of apoptosis and protein turnover positioned at an interface with the nucleolar core. Whether it reflects a stress-response component of the shared module, rather than a direct mechanistic partner of GAR1, is unresolved.

#### ZC3HAV1L

- **Related proteins** (co-abundance neighbors): FAF1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ZC3HAV1 like. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: stroke disorder (0.188); alcohol drinking (0.188); primary biliary cholangitis (0.134); preeclampsia (0.063); hypothyroidism (0.027)
- **Europe PMC papers**: 130
- **Why important**: ZC3HAV1L is the least characterized member but is important because it forms the terminal connection from FAF1 and may represent the unexplained edge of the module. HPA places it in the cytosol, reports cell-type enhancement in adipocytes, adrenal medulla cells, and gonadotrophs, and reports immune-cell enrichment in basophils. It has limited literature support and disease associations including stroke disorder, primary biliary cholangitis, preeclampsia, and hypothyroidism, making it a useful candidate for follow-up rather than a firmly interpreted driver.
- **Conclusion**: Established evidence supports ZC3HAV1L as a cytosolic, broadly tissue nonspecific gene with limited functional characterization. Its placement next to FAF1 makes a regulatory connection plausible, but any role in nucleolar, chromatin, or apoptosis biology is currently a hypothesis.
