# Conserved co-abundance modules: prostate and testis

## Module 0

**Tissue pair**: prostate and testis  
**Genes (36)**: PPP2R2A, GOT2, ABHD10, ACADM, APMAP, CS, CPT2, ECI1, ECI2, TSFM, GFUS, FH, IDH3A, IMPA1, PRPSAP2, ME2, MAT2B, MBOAT7, MYG1, MYO1C, MYO6, NNT, PDIA5, PPOX, ADSL, RAB10, SAE1, OXCT1, SYNGR2, YARS2, ACAT1, TIMM50, TKFC, TXNRD2, UBA3, UNC45A

### Function

The strongest interpretation is a mitochondrial metabolic and bioenergetic module. The globally corrected evidence supports catalytic activity (GO:MF catalytic activity; q_global = 0.0375) and mitochondrial matrix localization (GO:CC mitochondrial matrix; q_global = 0.0384). The genes represented in these terms include enzymes of the tricarboxylic acid cycle, fatty-acid oxidation, ketone-body utilization, amino-acid metabolism, redox maintenance, heme synthesis, mitochondrial translation, and mitochondrial protein import. STRING supplementary enrichment independently points to mitochondrial targeting, mitochondria, and the mitochondrial matrix (4 supplementary STRING terms; within-query FDR 4.24e-06–0.0083). The module therefore appears to capture coordinated mitochondrial oxidative metabolism rather than a narrowly specialized pathway. The broad catalytic-activity term should not be overinterpreted as identifying one biochemical reaction.

**Cell composition.** This is predominantly an intracellular, enzyme-rich module rather than a plasma-protein or secreted-protein module. HPA indicates that nearly all members are detected in prostate and testis, while only one member is annotated in the secretome. Most genes have low immune-cell specificity, so the module does not strongly resemble a blood-cell contamination signature; a small subset has immune-cell or blood-cell enrichment, which should nevertheless be considered when interpreting bulk tissue data. The module is not uniformly prostate- or testis-specific. HPA frequently shows liver, tongue, skeletal-muscle, and other tissue enrichment, with hepatocytes among the recurring enhanced cell types and late spermatids also represented. Many genes have low tissue specificity or broad metabolic functions. Thus, the shared prostate–testis signal may reflect a conserved oxidative-metabolic program present in relevant epithelial, germ-cell, or other metabolically active cell populations, rather than a uniquely prostate–testis pathway.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF catalytic activity | 0.0375 | ABHD10, ACADM, ACAT1, ADSL, APMAP, CPT2, CS, ECI1, ECI2, FH, GFUS, GOT2, IDH3A, IMPA1, MAT2B, MBOAT7, ME2, MYG1, MYO1C, MYO6, NNT, OXCT1, PDIA5, PPOX, RAB10, SAE1, TIMM50, TKFC, TXNRD2, UBA3, YARS2 |
| GO:CC mitochondrial matrix | 0.0384 | ABHD10, ACADM, ACAT1, CS, ECI1, FH, GOT2, IDH3A, ME2, MYG1, OXCT1, TXNRD2, YARS2 |

### STRING and hu.MAP

STRING supports a known metabolic core. Particularly coherent relationships connect ACAT1 with CS, ECI2, and OXCT1; ACADM with CPT2, ECI1, and ECI2; and CS with FH, GOT2, IDH3A, ME2, and TXNRD2. The ECI1–ECI2 relationship and the MYO1C–MYO6 relationship are also already represented. These associations indicate that much of the co-abundance structure recapitulates established functional or pathway relationships, although STRING associations are not proof that all proteins form one physical complex in prostate or testis. hu.MAP provides additional support for recurring mitochondrial assemblies involving CPT2, TSFM, and PPOX, as well as smaller assemblies involving ACADM, ME2, NNT, TIMM50, UNC45A, ADSL, and TKFC (hu.MAP huMAP3_13468.1) (hu.MAP huMAP3_06099.1) (hu.MAP huMAP3_09014.1) (hu.MAP huMAP3_03498.1) (hu.MAP huMAP3_12388.1) (hu.MAP huMAP3_10835.1) (hu.MAP huMAP3_08568.1) (hu.MAP huMAP3_09247.1) (hu.MAP huMAP3_14442.1). The complexes are generally partial rather than complete representations of the module, suggesting that the module combines several related mitochondrial processes with supporting cytosolic, membrane, and trafficking functions.

**STRING interactions (score >= 0.7)**: 25 of 630 gene pairs: ACADM–ACAT1 (0.717); ACADM–CPT2 (0.853); ACADM–ECI1 (0.732); ACADM–ECI2 (0.916); ACAT1–CS (0.977); ACAT1–ECI2 (0.979); ACAT1–OXCT1 (0.986); ADSL–CS (0.83); ADSL–FH (0.709); ADSL–IDH3A (0.834); CS–FH (0.993); CS–GOT2 (0.952); CS–IDH3A (0.925); CS–ME2 (0.975); CS–TXNRD2 (0.77); ECI1–ECI2 (0.999); FH–GOT2 (0.979); FH–IDH3A (0.864); FH–ME2 (0.989); FH–PPOX (0.805); GOT2–IDH3A (0.889); IDH3A–NNT (0.726); MYO1C–MYO6 (0.916); TSFM–YARS2 (0.822); UBA3–YARS2 (0.753)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transit peptide (FDR = 4.24e-06, 18 genes); Keyword Mitochondrion (FDR = 0.00061, 19 genes); Component Mitochondrial matrix (FDR = 0.0042, 14 genes); COMPARTMENTS Mitochondrion (FDR = 0.0083, 19 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (CPT2, TSFM, PPOX; 3/99); huMAP3_06099.1 (CPT2, TSFM; 2/3); huMAP3_09014.1 (ADSL, TKFC; 2/3); huMAP3_03498.1 (ACADM, ME2; 2/4); huMAP3_12388.1 (ACADM, NNT; 2/7); huMAP3_10835.1 (CPT2, TSFM; 2/7); huMAP3_08568.1 (TIMM50, UNC45A; 2/7); huMAP3_09247.1 (TIMM50, UNC45A; 2/9); huMAP3_14442.1 (ME2, ADSL; 2/57)

### Novelty

The module should not be described as a newly discovered mitochondrial pathway. Its central biology is already well established through the annotations, the coherent STRING relationships, and the hu.MAP complexes. The potentially novel aspect is the coordinated co-abundance of this collection across prostate and testis, particularly the linking of a mitochondrial metabolic core to MBOAT7, SAE1, vesicle or actin-associated genes, and protein-import or redox components. However, absence of a relationship from STRING or hu.MAP does not establish novelty, and the available evidence does not show that this tissue-pair module has been independently demonstrated as a new biological complex. The most defensible conclusion is that this is a potentially informative tissue-shared co-abundance signature built largely from known mitochondrial and metabolic biology, with novelty requiring validation in independent cohorts and perturbation or cell-resolved experiments.

**Hypothesis.** Hypothesis: prostate and testis share a coordinated mitochondrial state in which fatty-acid handling, acetyl-CoA and ketone-body metabolism, tricarboxylic-acid-cycle flux, mitochondrial redox control, and protein import or translation rise and fall together. In germ-cell or metabolically active epithelial contexts, this core may be coupled to phospholipid remodeling through MBOAT7, intracellular trafficking through RAB10 and myosin proteins, and post-translational regulation through SAE1 and UBA3. The proposed mechanism is that common energetic and redox demands generate the co-abundance pattern, while cell composition and developmental state determine its strength. This remains a hypothesis: co-abundance does not establish physical interaction, causal regulation, or directionality.

### Important genes

#### ACAT1

- **Related proteins** (co-abundance neighbors): ECI1 (0.88), IDH3A (0.86), ECI2 (0.84), ACADM (0.83), MBOAT7 (0.82), CS (0.82), ME2 (0.81); STRING partners: ACADM (0.717), CS (0.977), ECI2 (0.979), OXCT1 (0.986)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA acetyltransferase 1. This gene encodes a mitochondrially localized enzyme that catalyzes the reversible formation of acetoacetyl-CoA from two molecules of acetyl-CoA. Defects in this gene are associated with 3-ketothiolase deficiency, an inborn error of isoleucine catabolism characterized by urinary excretion of 2-methyl-3-hydroxybutyric acid, 2-methylacetoacetic acid, tiglylglycine, and butanone. [provided by RefSeq,…
- **Diseases (Open Targets)**: beta-ketothiolase deficiency (0.817); hereditary disease (0.470); Abnormality of the skeletal system (0.239); neoplasm (0.115); nonpapillary renal cell carcinoma (0.105)
- **Europe PMC papers**: 4147
- **Why important**: ACAT1 is a highly connected module member that links the fatty-acid and acetyl-CoA branch to the tricarboxylic-acid-cycle and ketone-body-related core. It is supported by both globally corrected terms (GO:MF catalytic activity; q_global = 0.0375) and (GO:CC mitochondrial matrix; q_global = 0.0384), all mitochondrial STRING supplementary terms, and strong STRING relationships with CS, ECI2, OXCT1, and ACADM. HPA detects it in both tissues and shows enhancement in early spermatids and primary spermatocytes, while its disease association with ketothiolase deficiency is well established. Its substantial literature supports an established metabolic interpretation.
- **Conclusion**: Established evidence supports ACAT1 as a central mitochondrial metabolic anchor of the module. A tissue-shared role in coordinating lipid-derived acetyl-CoA use is plausible, but the module does not establish that ACAT1 regulates the other genes or is the driver of their co-abundance.

#### CS

- **Related proteins** (co-abundance neighbors): ECI2 (0.83), FH (0.83), ACADM (0.82), TIMM50 (0.82), ACAT1 (0.82); STRING partners: ACAT1 (0.977), ADSL (0.83), FH (0.993), GOT2 (0.952), IDH3A (0.925), ME2 (0.975), TXNRD2 (0.77)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS is a central connector within the STRING-supported metabolic core, with relationships to ACAT1, FH, GOT2, IDH3A, ME2, and TXNRD2. It is represented in both primary globally corrected terms (GO:MF catalytic activity; q_global = 0.0375) and (GO:CC mitochondrial matrix; q_global = 0.0384), is mitochondrial in HPA, and encodes the entry enzyme of the tricarboxylic acid cycle. Its very extensive literature and established disease and metabolic relevance make it a strong reference gene for interpreting the module.
- **Conclusion**: Established evidence identifies CS as a core tricarboxylic-acid-cycle component that helps explain the module's mitochondrial and catalytic signature. Its centrality supports pathway coherence, but does not demonstrate a prostate–testis-specific function.

#### IDH3A

- **Related proteins** (co-abundance neighbors): GOT2 (0.86), ACAT1 (0.86), ME2 (0.86), ECI1 (0.84), TIMM50 (0.81), MBOAT7 (0.81), ABHD10 (0.81); STRING partners: ADSL (0.834), CS (0.925), FH (0.864), GOT2 (0.889), NNT (0.726)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in prostate, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: isocitrate dehydrogenase (NAD(+)) 3 catalytic subunit alpha. Isocitrate dehydrogenases catalyze the oxidative decarboxylation of isocitrate to 2-oxoglutarate. These enzymes belong to two distinct subclasses, one of which utilizes NAD(+) as the electron acceptor and the other NADP(+). Five isocitrate dehydrogenases have been reported: three NAD(+)-dependent isocitrate dehydrogenases, which localize to the mitochondrial matrix, and two NADP(+)-dependent isoci…
- **Diseases (Open Targets)**: retinitis pigmentosa 90 (0.791); retinitis pigmentosa (0.467); neurodegenerative disease (0.437); inherited retinal dystrophy (0.381); colorectal carcinoma (0.182)
- **Europe PMC papers**: 1497
- **Why important**: IDH3A has high network connectivity and links GOT2, ACAT1, ME2, ECI1, TIMM50, MBOAT7, and ABHD10. It is present in both primary terms (GO:MF catalytic activity; q_global = 0.0375) and (GO:CC mitochondrial matrix; q_global = 0.0384), all mitochondrial STRING supplementary terms, and several established STRING associations with ADSL, CS, FH, GOT2, and NNT. HPA detects it in both tissues, and its annotation directly places it in the mitochondrial tricarboxylic acid cycle. Its substantial literature and association with inherited retinal disease further support its biological importance.
- **Conclusion**: Established evidence supports IDH3A as a metabolic hub connecting carbon flux, mitochondrial function, and redox-related components. Its connection to MBOAT7 is compatible with coordinated lipid and energy metabolism, but any regulatory coupling between them remains hypothetical.

#### TIMM50

- **Related proteins** (co-abundance neighbors): APMAP (0.88), FH (0.85), ECI1 (0.84), CS (0.82), IDH3A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_08568.1, huMAP3_09247.1
- **Function (MyGene.info)**: translocase of inner mitochondrial membrane 50. This gene encodes a subunit of the TIM23 inner mitochondrial membrane translocase complex. The encoded protein functions as the receptor subunit that recognizes the mitochondrial targeting signal, or presequence, on protein cargo that is destined for the mitochondrial inner membrane and matrix. This protein may also play a role in maintaining the membrane permeability barrier, and knockdown of thi…
- **Diseases (Open Targets)**: 3-methylglutaconic aciduria type 9 (0.773); neurodegenerative disease (0.519); Mitochondrial encephalopathy (0.425); hereditary disease (0.415); Epileptic encephalopathy (0.370)
- **Europe PMC papers**: 442
- **Why important**: TIMM50 connects the metabolic subgraph to mitochondrial protein import and membrane integrity. It has multiple module neighbors, is included in the primary catalytic-activity term (GO:MF catalytic activity; q_global = 0.0375), and is supported by mitochondrial STRING supplementary terms (STRING Keyword Transit peptide; within-query FDR = 4.24e-06), (STRING Keyword Mitochondrion; within-query FDR = 0.00061), and (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0083). Its annotated role as a receptor component of the TIM23 import machinery provides a mechanistic explanation for why mitochondrial metabolic proteins and mitochondrial maintenance genes may co-vary. HPA detects it in both tissues and highlights late spermatids, while its disease associations include mitochondrial encephalopathy and epileptic encephalopathy.
- **Conclusion**: Established evidence supports TIMM50 as a mitochondrial maintenance and import component that broadens the module beyond metabolic enzymes. It may coordinate organelle capacity with metabolic demand, but that coordination is a hypothesis rather than a demonstrated causal relationship.

#### MBOAT7

- **Related proteins** (co-abundance neighbors): RAB10 (0.86), UBA3 (0.84), SAE1 (0.83), ACAT1 (0.82), IMPA1 (0.82), PPP2R2A (0.82), TSFM (0.81), IDH3A (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: membrane bound acylglycerophosphatidylinositol O-acyltransferase MBOAT7. This gene encodes a member of the membrane-bound O-acyltransferases family of integral membrane proteins that have acyltransferase activity. The encoded protein is a lysophosphatidylinositol acyltransferase that has specificity for arachidonoyl-CoA as an acyl donor. This protein is involved in the reacylation of phospholipids as part of the phospholipid remodeling pathway known as the Land cycle. …
- **Diseases (Open Targets)**: intellectual disability, autosomal recessive 57 (0.754); hereditary disease (0.487); autosomal recessive non-syndromic intellectual disability (0.462); complex neurodevelopmental disorder (0.370); neurodegenerative disease (0.345)
- **Europe PMC papers**: 1344
- **Why important**: MBOAT7 has the strongest network position in the supplied module and connects lipid remodeling with ACAT1, IDH3A, RAB10, SAE1, UBA3, and IMPA1. Its annotation identifies lysophosphatidylinositol acylation and phospholipid remodeling, providing a noncanonical membrane-lipid dimension to an otherwise strongly mitochondrial metabolic module. It is included in (GO:MF catalytic activity; q_global = 0.0375) but lacks STRING partners and hu.MAP assignments in the supplied evidence, making it an informative bridge whose association is driven by the co-abundance network rather than by already catalogued interaction evidence. Its disease associations include inherited neurodevelopmental disorders, and it has substantial literature.
- **Conclusion**: Established evidence supports MBOAT7 as a phospholipid-remodeling enzyme and a prominent network connector. Its placement may indicate coupling between membrane composition, trafficking, and mitochondrial metabolism in the shared tissues, but this cross-system coupling is the most clearly testable hypothesis rather than an established mechanism.

## Module 1

**Tissue pair**: prostate and testis  
**Genes (30)**: ABHD11, ANXA6, GLB1, CALD1, CSRP1, CUL4A, ERAP1, FERMT2, FLNA, FLNC, H6PD, GLIPR2, GSN, EPHX1, LPP, ALDH6A1, MYLK, RAD50, RO60, S100A4, SELENBP1, SCARB2, SPRYD4, TIMM44, TLN1, TMED5, TRNT1, THBS1, VCL, GC

### Function

The strongest interpretation is an actin-based cell adhesion and contractility module. The primary evidence is the globally corrected enrichment for actin binding (GO:MF actin binding; q_global = 0.0203), focal adhesion (GO:CC focal adhesion; q_global = 0.0492), cell-substrate junction (GO:CC cell-substrate junction; q_global = 0.0492), and steroid binding (GO:MF steroid binding; q_global = 0.0498). The shared actin-adhesion signal is supported by the convergence of FLNA, FLNC, FERMT2, GSN, TLN1, VCL, CALD1, MYLK, CSRP1, LPP, and ANXA6. The steroid-binding signal is narrower and is contributed by ANXA6, EPHX1, GC, and SCARB2; it may represent a connected biochemical component or tissue-composition effect rather than the central module function. Supplementary STRING results reinforce actin binding, cytoskeletal protein binding, focal adhesion, phosphatidylserine binding, and smooth-muscle contraction (8 supplementary STRING terms; within-query FDR 0.0033–0.0488). Several other genes provide mitochondrial, lysosomal, metabolic, RNA-processing, DNA-repair, or vesicular functions, so the module is not a single purified pathway. Overall, it most plausibly reflects adhesion-linked cytoskeletal organization with contractile and membrane-remodeling features.

**Cell composition.** This module is not dominated by plasma or secreted proteins, but secreted components are present, including GC, GSN, S100A4, THBS1, and ERAP1. GC is liver-enriched and secreted to blood, while GSN and S100A4 are also secreted to blood; these genes could reflect circulating protein or extracellular material rather than expression in the same prostate or testis cells. HPA shows substantial tissue and cell-type heterogeneity: many genes are tissue-enhanced or have low specificity, while smooth muscle, vascular smooth muscle, hepatic stellate, megakaryocyte, platelet, hepatocyte, and myeloid associations recur. The presence of blood-cell-enhanced genes and secreted proteins means that blood, vascular, stromal, smooth-muscle, or shared contaminating cell types may contribute to the conserved co-abundance pattern. At the same time, many module proteins are detected in both prostate and testis, and the adhesion and contractility genes have relevant cellular localizations, so the result need not be explained entirely by blood contamination.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF actin binding | 0.0203 | CALD1, FERMT2, FLNA, FLNC, GC, GSN, MYLK, S100A4, TLN1, VCL |
| GO:CC focal adhesion | 0.0492 | ANXA6, CSRP1, FERMT2, FLNA, FLNC, GSN, LPP, SCARB2, TLN1, VCL |
| GO:CC cell-substrate junction | 0.0492 | ANXA6, CSRP1, FERMT2, FLNA, FLNC, GSN, LPP, SCARB2, TLN1, VCL |
| GO:MF steroid binding | 0.0498 | ANXA6, EPHX1, GC, SCARB2 |

### STRING and hu.MAP

STRING contains a coherent, already known interaction backbone involving FLNA, FLNC, TLN1, VCL, FERMT2, GSN, CALD1, and MYLK. Particularly strong links connect filamins with talin and vinculin, and connect talin or vinculin with gelsolin; these relationships support a real actin-adhesion machinery rather than an arbitrary co-abundance grouping. SCARB2 and THBS1 also form a known pair, consistent with membrane or extracellular-matrix biology. The STRING evidence is supplementary and does not replace the globally corrected GO evidence. hu.MAP provides two complexes containing CALD1 and MYLK (hu.MAP huMAP3_11074.1) and (hu.MAP huMAP3_10673.1), with additional junctional, cytoskeletal, signaling, and trafficking members outside the module. A separate hu.MAP complex contains ANXA6 and GLIPR2 (hu.MAP huMAP3_12658.1). Thus, known physical or functional relationships explain important parts of the module, while the full module is broader than any one established complex.

**STRING interactions (score >= 0.7)**: 19 of 435 gene pairs: CALD1–MYLK (0.832); CALD1–VCL (0.771); FERMT2–FLNA (0.852); FERMT2–FLNC (0.747); FERMT2–TLN1 (0.705); FERMT2–VCL (0.896); FLNA–FLNC (0.907); FLNA–GSN (0.831); FLNA–TLN1 (0.998); FLNA–VCL (0.998); FLNC–GSN (0.749); FLNC–TLN1 (0.996); FLNC–VCL (0.994); GC–GSN (0.826); GSN–TLN1 (0.941); GSN–VCL (0.918); MYLK–VCL (0.814); SCARB2–THBS1 (0.997); TLN1–VCL (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Actin binding (FDR = 0.0033, 11 genes); COMPARTMENTS Focal adhesion (FDR = 0.0109, 10 genes); Function Cytoskeletal protein binding (FDR = 0.0192, 12 genes); KEGG Focal adhesion (FDR = 0.0371, 6 genes); Function Phosphatidylserine binding (FDR = 0.038, 4 genes); RCTM Smooth Muscle Contraction (FDR = 0.0404, 5 genes); Function Actin filament binding (FDR = 0.048, 7 genes); Component Focal adhesion (FDR = 0.0488, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11074.1 (CALD1, MYLK; 2/6); huMAP3_10673.1 (CALD1, MYLK; 2/14); huMAP3_12658.1 (ANXA6, GLIPR2; 2/32)

### Novelty

The module should not be described as a newly discovered actin-adhesion pathway. Its principal relationships and functions are already established by STRING, hu.MAP, gene annotations, and the extensive literature for genes such as FLNA, VCL, MYLK, TLN1, GSN, and THBS1. A potentially novel aspect is the conservation of this particular co-abundance organization across prostate and testis, especially the way adhesion, contractility, steroid-associated proteins, metabolic proteins, and secreted proteins co-vary. However, the fact sheet does not compare this module with prior tissue co-expression modules or provide an independent replication, so that cross-tissue organization remains a candidate finding rather than a demonstrated novel mechanism. Lack of representation in a curated complex database would not by itself establish novelty.

**Hypothesis.** Hypothesis: the module reflects a shared structural state in prostate and testis involving adherent smooth-muscle, vascular, stromal, or epithelial-associated cells. Integrin-linked adhesion may recruit talin, kindlin, vinculin, and filamins to couple the plasma membrane to actin, while caldesmon and MYLK regulate actomyosin contractility. Gelsolin and annexin A6 could remodel actin and phospholipid membranes in a calcium-sensitive manner. THBS1, SCARB2, and the secreted proteins may connect this cellular program to extracellular-matrix, endosomal, platelet, or blood-derived signals. GC, EPHX1, and SCARB2 could additionally indicate steroid or lipid handling. This model predicts that the apparent conservation will be strongest in matched vascular, stromal, smooth-muscle, or epithelial cell populations and will weaken after controlling for cell composition and circulating protein abundance.

### Important genes

#### FLNA

- **Related proteins** (co-abundance neighbors): TLN1 (0.95), FLNC (0.86), THBS1 (0.83), GLIPR2 (0.81); STRING partners: FERMT2 (0.852), FLNC (0.907), GSN (0.831), TLN1 (0.998), VCL (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is a highly connected module gene and occupies the central known interaction backbone with FLNC, TLN1, FERMT2, GSN, VCL, and THBS1. It is an actin crosslinker that links actin to membrane glycoproteins, integrins, receptor complexes, and second messengers. It contributes to all three primary actin-adhesion terms (GO:MF actin binding; q_global = 0.0203) (GO:CC focal adhesion; q_global = 0.0492) (GO:CC cell-substrate junction; q_global = 0.0492), appears across the matching STRING terms, has blood-vessel and stromal-associated HPA patterns, and has extensive disease and literature evidence including developmental and cytoskeletal syndromes.
- **Conclusion**: Established conclusion: FLNA is a strong mechanistic anchor for the module's actin-to-membrane and adhesion interpretation. Hypothesis: its co-abundance across prostate and testis may report a shared mechanically adherent or vascular-associated cell state.

#### TLN1

- **Related proteins** (co-abundance neighbors): FLNA (0.95); STRING partners: FERMT2 (0.705), FLNA (0.998), FLNC (0.996), GSN (0.941), VCL (0.999)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in prostate, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 is localized to focal adhesions and is annotated for cell adhesion, integrin activation, cell-matrix adhesion, and actin organization. It participates in the primary actin-binding, focal-adhesion, and cell-substrate-junction terms (GO:MF actin binding; q_global = 0.0203) (GO:CC focal adhesion; q_global = 0.0492) (GO:CC cell-substrate junction; q_global = 0.0492). Its STRING relationships with FLNA, FLNC, VCL, GSN, and FERMT2 provide a well-established adhesion scaffold, while HPA associates it with blood vessels, megakaryocytes, and platelets. Its disease annotations and substantial literature make it a well-supported biological indicator.
- **Conclusion**: Established conclusion: TLN1 supports an integrin-linked focal-adhesion interpretation. Hypothesis: TLN1 may be a functional bridge through which tissue mechanics couple to the co-abundance of contractile and extracellular-matrix proteins.

#### VCL

- **Related proteins** (co-abundance neighbors): GSN (0.80); STRING partners: CALD1 (0.771), FERMT2 (0.896), FLNA (0.998), FLNC (0.994), GSN (0.918), MYLK (0.814), TLN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in prostate, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vinculin. Vinculin is a cytoskeletal protein associated with cell-cell and cell-matrix junctions, where it is thought to function as one of several interacting proteins involved in anchoring F-actin to the membrane. Defects in VCL are the cause of cardiomyopathy dilated type 1W. Dilated cardiomyopathy is a disorder characterized by ventricular dilation and impaired systolic function, resulting in congestive…
- **Diseases (Open Targets)**: dilated cardiomyopathy 1W (0.692); hypertrophic cardiomyopathy 15 (0.660); hypertrophic cardiomyopathy (0.652); familial isolated dilated cardiomyopathy (0.642); cancer (0.605)
- **Europe PMC papers**: 10760
- **Why important**: VCL is a junctional actin anchor involved in cell-cell and cell-matrix adhesion and appears in the primary actin and adhesion terms (GO:MF actin binding; q_global = 0.0203) (GO:CC focal adhesion; q_global = 0.0492) (GO:CC cell-substrate junction; q_global = 0.0492). Although its direct co-abundance connectivity is limited in the supplied subgraph, it has a broad high-confidence STRING neighborhood involving FLNA, FLNC, TLN1, FERMT2, GSN, CALD1, and MYLK. It is focal-adhesion localized, detected in both target tissues, and linked to cardiomyopathy and other adhesion-relevant disease evidence.
- **Conclusion**: Established conclusion: VCL is a strong independent marker of the known focal-adhesion machinery. Hypothesis: its co-abundance may reflect coordinated stabilization of cell junctions rather than a tissue-specific biochemical pathway.

#### MYLK

- **Related proteins** (co-abundance neighbors): CALD1 (0.93), ANXA6 (0.89); STRING partners: CALD1 (0.832), VCL (0.814)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11074.1, huMAP3_10673.1
- **Function (MyGene.info)**: myosin light chain kinase. This gene, a muscle member of the immunoglobulin gene superfamily, encodes myosin light chain kinase which is a calcium/calmodulin dependent enzyme. This kinase phosphorylates myosin regulatory light chains to facilitate myosin interaction with actin filaments to produce contractile activity. This gene encodes both smooth muscle and nonmuscle isoforms. In addition, using a separate promoter in an …
- **Diseases (Open Targets)**: aortic aneurysm, familial thoracic 7 (0.767); familial thoracic aortic aneurysm and aortic dissection (0.710); megacystis-microcolon-intestinal hypoperistalsis syndrome 1 (0.617); megacystis-microcolon-intestinal hypoperistalsis syndrome (0.597); Rare genetic vascular disease (0.483)
- **Europe PMC papers**: 10503
- **Why important**: MYLK provides the clearest enzymatic link to contractility. It phosphorylates myosin regulatory light chains and is annotated for smooth-muscle contraction, cell migration, and actomyosin activity. It participates in the actin-binding and focal-adhesion STRING signals (STRING Function Actin binding; within-query FDR = 0.0033), (STRING KEGG Focal adhesion; within-query FDR = 0.0371), and (STRING RCTM Smooth Muscle Contraction; within-query FDR = 0.0404), connects to CALD1 and ANXA6 in the module, and is represented with CALD1 in two hu.MAP complexes (hu.MAP huMAP3_11074.1) and (hu.MAP huMAP3_10673.1). Its smooth-muscle, peritubular-myoid, megakaryocyte, and platelet associations are relevant to the tissue-composition interpretation, and it has extensive disease and literature support.
- **Conclusion**: Established conclusion: MYLK supports a contractile actin interpretation and is not merely a generic housekeeping marker. Hypothesis: it may couple the conserved adhesion program to smooth-muscle or peritubular-myoid contractility in the two tissues.

#### ANXA6

- **Related proteins** (co-abundance neighbors): MYLK (0.89), CSRP1 (0.86), LPP (0.83), ERAP1 (0.82), S100A4 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_12658.1
- **Function (MyGene.info)**: annexin A6. Annexin VI belongs to a family of calcium-dependent membrane and phospholipid binding proteins. Several members of the annexin family have been implicated in membrane-related events along exocytotic and endocytotic pathways. The annexin VI gene is approximately 60 kbp long and contains 26 exons. It encodes a protein of about 68 kDa that consists of eight 68-amino acid repeats separated by linking …
- **Diseases (Open Targets)**: systemic lupus erythematosus (0.292); asthma (0.194); poisoning (0.193); stricture (0.193); neoplasm (0.115)
- **Europe PMC papers**: 1621
- **Why important**: ANXA6 has the strongest supplied module connectivity and contributes to focal adhesion, cell-substrate junction, and steroid-binding enrichment (GO:CC focal adhesion; q_global = 0.0492) (GO:CC cell-substrate junction; q_global = 0.0492) (GO:MF steroid binding; q_global = 0.0498). It is a calcium-dependent membrane and phospholipid-binding annexin involved in membrane trafficking and calcium-related processes. Its module neighbors include MYLK, CSRP1, LPP, ERAP1, and S100A4, and it appears in many supplementary cytoskeletal and phosphatidylserine-binding signals (8 supplementary STRING terms; within-query FDR 0.0033–0.0488). It is detected in both prostate and testis and has substantial disease and literature evidence.
- **Conclusion**: Established conclusion: ANXA6 connects membrane phospholipid biology with the actin-adhesion core and is a plausible integrator of the module. Hypothesis: calcium-sensitive membrane remodeling by ANXA6 may coordinate adhesion turnover with contractile signaling.

#### GC

- **Related proteins** (co-abundance neighbors): GSN (0.85); STRING partners: GSN (0.826)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in prostate, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GC vitamin D binding protein. The protein encoded by this gene belongs to the albumin gene family. It is a multifunctional protein found in plasma, ascitic fluid, cerebrospinal fluid and on the surface of many cell types. It binds to vitamin D and its plasma metabolites and transports them to target tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq,…
- **Diseases (Open Targets)**: vitamin D deficiency (0.574); vitamin deficiency (0.552); chronic obstructive pulmonary disease (0.499); squamous cell carcinoma (0.339); central nervous system cancer (0.334)
- **Europe PMC papers**: 363974
- **Why important**: GC is important because it qualifies the biological interpretation. It is liver-enriched, secreted to blood, binds and transports vitamin D and its metabolites, and contributes to actin-binding and steroid-binding enrichment (GO:MF actin binding; q_global = 0.0203) and (GO:MF steroid binding; q_global = 0.0498). Its STRING link to GSN connects a plasma protein with the actin-associated part of the module. GC is also exceptionally well represented in the literature and is detected in both prostate and testis, making it both a biologically informative component and a possible blood-derived or extracellular confounder.
- **Conclusion**: Established conclusion: GC supports the steroid or vitamin-transport component but is not evidence that the entire module is a steroid pathway. Hypothesis: GC co-abundance may partly reflect vascular or plasma exposure shared by the tissue samples rather than intracellular expression in the core adhesion cells.

## Module 2

**Tissue pair**: prostate and testis  
**Genes (38)**: ACADVL, ACO2, AGPS, RNPEP, AP1B1, CDK5RAP3, CPNE3, DNAJC10, DNM1L, GFM1, GALK1, GNL1, HACL2, HMOX2, LNPEP, LRBA, MAP1B, RHOT1, NEK9, OPA1, PDCD4, PDE12, PITRM1, RECQL, SEC23B, SUPV3L1, AARS1, DARS2, IARS2, SARS1, TMEM214, TRAP1, TTLL12, UBE4A, USP5, UGGT1, NAE1, USO1

### Function

The module most plausibly represents coordinated cellular maintenance centered on mitochondrial protein synthesis, mitochondrial quality control, organelle dynamics, and proteostasis, with an additional ER–Golgi trafficking component. This interpretation is supported by the prominent network position of GFM1, OPA1, DARS2, IARS2, PITRM1, TRAP1, DNM1L, and SUPV3L1, whose supplied annotations link mitochondrial translation, mitochondrial RNA turnover, protein folding, proteolysis, mitochondrial fusion or fission, and mitochondrial organization. AARS1 and SARS1 add aminoacyl-tRNA and translation-related functions, while UGGT1, DNAJC10, SEC23B, USO1, and AP1B1 support protein quality control and vesicle transport. The module also contains metabolic genes connected to fatty-acid oxidation, the TCA cycle, ether-lipid synthesis, heme metabolism, and galactose metabolism. However, no GO or KEGG term passed global correction, so this is an integrative gene-level and network-level interpretation rather than a globally significant enrichment claim.

**Cell composition.** The module does not resemble a plasma-protein, broadly secreted, or blood-cell-enriched module. Only a small minority of genes are annotated as secreted, and HPA reports low immune-cell specificity for nearly the entire module with no recurrent enriched blood-cell category. Most genes have low tissue specificity, although many show cell-type-enhanced patterns across diverse epithelial, reproductive, muscle, neuronal, and progenitor populations. Protein detection in both prostate and testis is widespread, supporting a shared cellular maintenance program in the two tissues, but it does not by itself establish prostate- or testis-specific biology. The presence of epididymis-associated DNAJC10 and spermatogenic annotations for PITRM1, HMOX2, USP5, GNL1, and related genes may indicate contributions from specialized reproductive cell states, while the overall HPA profile argues against a simple blood-contamination explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a focused set of known relationships rather than broad functional enrichment. The strongest connected STRING-supported group links AARS1 with DARS2, IARS2, and SARS1, and also links DARS2 with IARS2 and IARS2 with SARS1. These relationships support a translation or aminoacyl-tRNA-associated interpretation, although AARS1 is cytoplasmic whereas DARS2 and IARS2 are mitochondrial in the supplied annotations. STRING also connects DNAJC10 with UGGT1, consistent with ER protein-folding and quality-control biology. No STRING functional-enrichment result was supplied. hu.MAP provides complementary complex-level support: C1 and C2 contain DARS2, GFM1, and IARS2 in mitochondrial translation or mitochondrial metabolic assemblies; C4 contains DARS2 and IARS2; C3 contains USO1, AP1B1, and SEC23B in a vesicle-trafficking assembly; C5 links AARS1 with RECQL; and C6 links AARS1 with TRAP1. Thus, some module edges recapitulate known molecular relationships, while many co-abundance edges are not represented by the supplied STRING or hu.MAP relationships and may reflect shared regulation, organelle state, or cell composition rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 6 of 703 gene pairs: AARS1–DARS2 (0.907); AARS1–IARS2 (0.942); AARS1–SARS1 (0.881); DARS2–IARS2 (0.895); DNAJC10–UGGT1 (0.728); IARS2–SARS1 (0.904)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (TRAP1, DARS2, GFM1, IARS2; 4/99); huMAP3_10525.1 (DARS2, GFM1, IARS2; 3/33); huMAP3_12394.1 (USO1, AP1B1, SEC23B; 3/98); huMAP3_09668.1 (DARS2, IARS2; 2/8); huMAP3_10115.1 (RECQL, AARS1; 2/14); huMAP3_14442.1 (AARS1, TRAP1; 2/57)

### Novelty

The individual biology is not new: mitochondrial translation, mitochondrial dynamics, ER quality control, vesicle trafficking, and the listed disease associations are established for many component genes. The potentially novel observation is the coordinated co-abundance of these processes in a module conserved between prostate and testis. The module is not a single canonical complex, because it combines mitochondrial translation machinery, mitochondrial dynamics, ER quality control, Golgi and vesicle trafficking, metabolism, and genome or cell-cycle maintenance. Its novelty should therefore be stated cautiously as a candidate cross-tissue co-abundance organization rather than a newly discovered molecular complex or pathway. The limited overlap with supplied STRING and hu.MAP relationships supports possible added value from the co-abundance analysis, but absence from either resource cannot establish novelty.

**Hypothesis.** Hypothesis: in prostate and testis cells, a shared demand for high-quality organelle function and specialized protein handling coordinately increases mitochondrial translation, mitochondrial fusion or fission, mitochondrial RNA surveillance, and degradation of damaged proteins, while coupling these processes to ER-to-Golgi cargo handling. GFM1, DARS2, and IARS2 could support mitochondrial protein synthesis; OPA1 and TRAP1 could help preserve mitochondrial structure and proteostasis; PITRM1, SUPV3L1, and PDE12 could remove or process defective mitochondrial products; and USO1, SEC23B, AP1B1, UGGT1, and DNAJC10 could manage delivery and folding of proteins in the secretory pathway. This is a mechanistic model generated from co-abundance and annotations, not a demonstrated causal pathway. It should be tested with cell-type-resolved expression, perturbation of mitochondrial translation or dynamics, and direct measurement of ER stress, mitochondrial respiration, and cargo trafficking in prostate and testis models.

### Important genes

#### GFM1

- **Related proteins** (co-abundance neighbors): PITRM1 (0.90), CDK5RAP3 (0.89), TTLL12 (0.89), TRAP1 (0.89), OPA1 (0.87), HACL2 (0.86), DNM1L (0.86), UGGT1 (0.85), IARS2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1
- **Function (MyGene.info)**: G elongation factor mitochondrial 1. Eukaryotes contain two protein translational systems, one in the cytoplasm and one in the mitochondria. Mitochondrial translation is crucial for maintaining mitochondrial function and mutations in this system lead to a breakdown in the respiratory chain-oxidative phosphorylation system and to impaired maintenance of mitochondrial DNA. This gene encodes one of the mitochondrial translation elongati…
- **Diseases (Open Targets)**: hepatoencephalopathy due to combined oxidative phosphorylation defect type 1 (0.822); neurodegenerative disease (0.463); combined oxidative phosphorylation deficiency (0.451); hereditary disease (0.341); Leigh syndrome (0.313)
- **Europe PMC papers**: 1380
- **Why important**: GFM1 is among the most connected genes in the module and links PITRM1, TRAP1, OPA1, DNM1L, TTLL12, and UGGT1. Its supplied annotation identifies it as a mitochondrial translation elongation factor, and it participates in hu.MAP complexes C1 and C2. It has substantial literature and disease evidence for combined oxidative-phosphorylation defects and hepatoencephalopathy. Its position makes it a strong bridge between mitochondrial translation, mitochondrial quality control, and ER-associated protein handling.
- **Conclusion**: Established evidence supports GFM1 as a mitochondrial translation factor and a central network connector. It is plausible, but not established, that GFM1 coordinates the broader cross-organelle co-abundance pattern in this module.

#### OPA1

- **Related proteins** (co-abundance neighbors): GFM1 (0.87), USO1 (0.87), RHOT1 (0.83), PDE12 (0.83), TMEM214 (0.82), TTLL12 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in prostate, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OPA1 mitochondrial dynamin like GTPase. The protein encoded by this gene is a nuclear-encoded mitochondrial protein with similarity to dynamin-related GTPases. The encoded protein localizes to the inner mitochondrial membrane and helps regulate mitochondrial stability and energy output. This protein also sequesters cytochrome c. Mutations in this gene have been associated with optic atrophy type 1, which is a dominantly inherited optic …
- **Diseases (Open Targets)**: autosomal dominant optic atrophy, classic form (0.846); Behr syndrome (0.812); optic atrophy with or without deafness, ophthalmoplegia, myopathy, ataxia, and neuropathy (0.766); mitochondrial DNA depletion syndrome 14B (cardioencephalomyopathic type) (0.745); optic atrophy (0.653)
- **Europe PMC papers**: 12169
- **Why important**: OPA1 is a connected mitochondrial hub linked to GFM1, RHOT1, PDE12, TRAP1, TMEM214, and TTLL12. Its supplied function covers mitochondrial fusion, inner-membrane organization, mitochondrial stability, and energy output, and it has especially extensive literature and strong disease associations with optic atrophy and mitochondrial disorders. OPA1 provides a mechanistic connection between mitochondrial morphology and the translation and quality-control genes surrounding it.
- **Conclusion**: Established evidence supports OPA1 as a regulator of mitochondrial architecture and stability. Its role as the causal organizer of this prostate–testis module remains a hypothesis based on network position.

#### DARS2

- **Related proteins** (co-abundance neighbors): PITRM1 (0.89), IARS2 (0.88), UBE4A (0.83), ACADVL (0.81); STRING partners: AARS1 (0.907), IARS2 (0.895)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1, huMAP3_09668.1
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 2, mitochondrial. The protein encoded by this gene belongs to the class-II aminoacyl-tRNA synthetase family. It is a mitochondrial enzyme that specifically aminoacylates aspartyl-tRNA. Mutations in this gene are associated with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation (LBSL). [provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: leukoencephalopathy with brain stem and spinal cord involvement-high lactate syndrome (0.843); neurodegenerative disease (0.527); hereditary disease (0.518); hypertensive disorder (0.425); Cerebral cortical atrophy (0.425)
- **Europe PMC papers**: 796
- **Why important**: DARS2 is a mitochondrial aspartyl-tRNA synthetase, is supported by STRING links to AARS1 and IARS2, and occurs in hu.MAP complexes C1, C2, and C4. It is connected to IARS2, PITRM1, ACADVL, and UBE4A, thereby linking mitochondrial translation with mitochondrial metabolism and protein quality control. Its disease annotation includes LBSL and other mitochondrial or neurological disorders, with a substantial literature base.
- **Conclusion**: Established evidence supports DARS2 as a mitochondrial tRNA-charging enzyme and as part of known mitochondrial assemblies. The module suggests coordinated regulation with other translation and organelle-maintenance genes, but does not prove a prostate–testis-specific role.

#### IARS2

- **Related proteins** (co-abundance neighbors): PITRM1 (0.88), DARS2 (0.88), GFM1 (0.85), TRAP1 (0.82); STRING partners: AARS1 (0.942), DARS2 (0.895), SARS1 (0.904)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1, huMAP3_09668.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 2, mitochondrial. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Two forms of isoleucine-tRNA synthetase exist, a cytoplasmic form and a mitochondrial form. This gene encodes th…
- **Diseases (Open Targets)**: cataract-growth hormone deficiency-sensory neuropathy-sensorineural hearing loss-skeletal dysplasia syndrome (0.724); Leigh syndrome (0.563); hereditary disease (0.416); neurodegenerative disease (0.411); mitochondrial disease (0.374)
- **Europe PMC papers**: 411
- **Why important**: IARS2 is a mitochondrial isoleucyl-tRNA synthetase and one of the clearest molecular anchors of the module. It has STRING relationships with AARS1, DARS2, and SARS1 and is present in hu.MAP complexes C1, C2, and C4. Its network neighbors include GFM1, DARS2, PITRM1, and TRAP1, placing it at the intersection of mitochondrial translation, translation fidelity, and mitochondrial proteostasis. Its supplied disease associations include Leigh syndrome and other mitochondrial or hereditary disorders.
- **Conclusion**: Established evidence supports IARS2 as a mitochondrial aminoacyl-tRNA synthetase and component of known mitochondrial complexes. Its centrality to the module is well supported, whereas any direct role in reproductive-tissue specialization remains unproven.

#### USO1

- **Related proteins** (co-abundance neighbors): PDE12 (0.89), OPA1 (0.87), SEC23B (0.83), LRBA (0.83), AP1B1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: USO1 vesicle transport factor. The protein encoded by this gene is a peripheral membrane protein which recycles between the cytosol and the Golgi apparatus during interphase. It is regulated by phosphorylation: dephosphorylated protein associates with the Golgi membrane and dissociates from the membrane upon phosphorylation. Ras-associated protein 1 recruits this protein to coat protein complex II (COPII) vesicles during buddin…
- **Diseases (Open Targets)**: psoriatic arthritis (0.184); bipolar disorder (0.150); retinitis pigmentosa (0.085); cone dystrophy (0.076); cone-rod dystrophy (0.076)
- **Europe PMC papers**: 546
- **Why important**: USO1 is a network connector between PDE12, OPA1, SEC23B, LRBA, and AP1B1 and is part of hu.MAP complex C3 with AP1B1 and SEC23B. Its supplied annotation describes COPII-vesicle capture and ER-to-Golgi transport. HPA places it in the Golgi and reports skeletal-muscle and myonuclear enhancement, while protein is detected in both tissues. USO1 therefore represents the secretory-pathway branch that connects with the mitochondrial-centered part of the module.
- **Conclusion**: Established evidence supports USO1 as a vesicle-transport factor and C3 complex member. Its connection to mitochondrial genes in this module may reflect coordinated organelle homeostasis or shared cell-state regulation; a direct mechanistic coupling is not yet demonstrated.

#### AP1B1

- **Related proteins** (co-abundance neighbors): PDE12 (0.85), HACL2 (0.84), AARS1 (0.83), USO1 (0.83), RNPEP (0.81), USP5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: adaptor related protein complex 1 subunit beta 1. Adaptor protein complex 1 is found at the cytoplasmic face of coated vesicles located at the Golgi complex, where it mediates both the recruitment of clathrin to the membrane and the recognition of sorting signals within the cytosolic tails of transmembrane receptors. This complex is a heterotetramer composed of two large, one medium, and one small adaptin subunit. The protein encoded by this gene…
- **Diseases (Open Targets)**: ichthyosiform erythroderma, corneal involvement, and hearing loss (0.715); HIV infectious disease (0.503); MEDNIK syndrome (0.371); neurodegenerative disease (0.370); KID syndrome (0.292)
- **Europe PMC papers**: 500
- **Why important**: AP1B1 is a connected Golgi-associated gene linked to PDE12, HACL2, AARS1, USO1, RNPEP, and USP5, and it belongs to hu.MAP complex C3. Its established annotation describes clathrin recruitment, cargo recognition, intracellular transport, receptor-mediated endocytosis, and basolateral secretion. Its disease associations include syndromic epithelial and neurodevelopmental disorders, and it has a substantial literature base. It helps define the module's trafficking and membrane-protein-sorting component.
- **Conclusion**: Established evidence supports AP1B1 as a vesicle-sorting and adaptor-complex component. Its inclusion supports a secretory and trafficking dimension of the module, but does not establish that AP1B1 directly regulates mitochondrial translation.

## Module 3

**Tissue pair**: prostate and testis  
**Genes (39)**: ADAM10, AGK, AKAP12, ATPAF2, BCS1L, BLMH, BPHL, CISD2, COG1, COG5, COPS3, DCAKD, DCXR, TUFM, ETFDH, GMPPA, GMPPB, HMGCL, HSDL2, LYPLAL1, METAP1, MESD, APOOL, NADK2, NIPSNAP3A, NTPCR, DBT, PDXDC1, PNPT1, PTRHD1, RTCA, SEC22B, SIRT5, SPR, TATDN1, THEM6, ACAA1, TMEM70, UBE3A

### Function

The strongest interpretation is a mitochondrial metabolic and bioenergetic module. The primary evidence is (GO:CC mitochondrion; q_global = 0.0204), the globally corrected enrichment for mitochondrion, with broad representation of mitochondrial genes including HMGCL, ATPAF2, BCS1L, DBT, ETFDH, NADK2, PNPT1, SIRT5, TMEM70 and TUFM. Their annotated activities span leucine and branched-chain amino-acid degradation, ketone-body formation, fatty-acid oxidation, mitochondrial NADP production, respiratory-chain electron transfer, ATP-synthase assembly, mitochondrial translation and mitochondrial RNA processing. The network therefore appears functionally coherent at the level of mitochondrial energy and metabolic maintenance, although it is not evidence for one discrete molecular complex. The STRING disease enrichments (4 supplementary STRING terms; within-query FDR 0.0054–0.0293) support a metabolic and inherited-disease context, but they are supplementary and were not corrected across all module-term tests. The module also contains secondary processes involving Golgi trafficking, glycosylation, vesicle transport, RNA processing, protein quality control and lipid handling. These may represent connected cellular demands or peripheral components rather than the central function. No GO/KEGG term other than (GO:CC mitochondrion; q_global = 0.0204) passed global correction; the lack of additional globally significant terms does not invalidate the module.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. The HPA summary identifies only a small secreted subset, and most genes have low tissue specificity rather than a strong blood-cell signature. Immune-cell specificity is generally low, so the shared signal is unlikely to be explained mainly by blood contamination or a leukocyte program. Protein detection is extensive in both prostate and testis, supporting biological detectability in both tissues. The HPA patterns do, however, show a mixture of broadly expressed genes and cell-associated signals, including hepatocyte and liver enrichment, epididymal principal-cell enrichment, late spermatocyte or spermatid signals, and occasional neutrophil or other immune-cell associations. This suggests that the module may reflect a conserved metabolic program present across several cell types, with possible contributions from epithelial and germ-cell populations, rather than a prostate-and-testis-exclusive pathway. THEM6 is annotated as secreted with unknown location, while ADAM10 and MESD have intracellular and membrane-associated secretome annotations; these do not dominate the module.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrion | 0.0204 | AGK, APOOL, ATPAF2, BCS1L, BPHL, CISD2, DBT, DCAKD, DCXR, ETFDH, HMGCL, HSDL2, LYPLAL1, NADK2, NIPSNAP3A, NTPCR, PNPT1, PTRHD1, SIRT5, SPR, TATDN1, TMEM70, TUFM |

### STRING and hu.MAP

STRING provides a limited but biologically informative set of high-confidence relationships. The strongest links connect ACAA1 with HMGCL and HSDL2, ATPAF2 with TMEM70, COG1 with COG5, GMPPA with GMPPB, and NADK2 with SIRT5; ETFDH also connects with HSDL2. These are consistent with peroxisomal or mitochondrial lipid metabolism, ATP-synthase biogenesis, Golgi organization, GDP-mannose production and mitochondrial redox regulation. The sparse STRING connectivity means that most co-abundance edges are not established physical or functional interactions in STRING. hu.MAP provides several recurring component-level relationships: GMPPA–GMPPB is supported in a compact complex; HMGCL and ATPAF2 recur together in complexes; COG1–COG5 recur in conserved oligomeric Golgi complexes; and PNPT1 or TATDN1 occur with mitochondrial or nucleic-acid-processing proteins in larger complexes. These observations show that parts of the module contain known molecular machinery, but the hu.MAP matches cover only subsets of the module and do not establish that the entire module is one complex. The remaining co-abundance relationships may reflect shared regulation, shared cell composition or pathway-level coordination.

**STRING interactions (score >= 0.7)**: 8 of 741 gene pairs: ACAA1–DBT (0.848); ACAA1–HMGCL (0.965); ACAA1–HSDL2 (0.916); ATPAF2–TMEM70 (0.96); COG1–COG5 (0.999); ETFDH–HSDL2 (0.701); GMPPA–GMPPB (0.999); NADK2–SIRT5 (0.908)
**STRING functional enrichment (supplementary, within-query FDR)**: DISEASES Disease of metabolism (FDR = 0.0054, 18 genes); DISEASES Inherited metabolic disorder (FDR = 0.0068, 17 genes); DISEASES Amino acid metabolic disorder (FDR = 0.0197, 8 genes); DISEASES Autosomal recessive disease (FDR = 0.0293, 16 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (HMGCL, TATDN1, ATPAF2, PNPT1, NIPSNAP3A; 5/99); huMAP3_01176.1 (GMPPA, GMPPB; 2/2); huMAP3_12282.1 (METAP1, AKAP12; 2/3); huMAP3_01270.1 (HMGCL, ATPAF2; 2/3); huMAP3_09879.1 (GMPPA, GMPPB; 2/3); huMAP3_09533.1 (HMGCL, ATPAF2; 2/4); huMAP3_01694.1 (GMPPA, GMPPB; 2/4); huMAP3_07434.1 (GMPPA, GMPPB; 2/4); huMAP3_05572.1 (GMPPA, GMPPB; 2/5); huMAP3_08741.1 (RTCA, MESD; 2/5); huMAP3_12121.1 (GMPPA, GMPPB; 2/7); huMAP3_04294.1 (COG1, COG5; 2/10); huMAP3_14423.1 (COG1, COG5; 2/11); huMAP3_09176.1 (COG1, COG5; 2/12); huMAP3_10458.1 (TATDN1, PNPT1; 2/16); huMAP3_06247.1 (THEM6, TMEM70; 2/65); huMAP3_09592.1 (THEM6, TMEM70; 2/95)

### Novelty

The module should be regarded as a potentially useful new cross-tissue co-abundance observation, not as a newly discovered mitochondrial pathway or a newly established physical complex. The globally corrected mitochondrial signal is biologically coherent, and the prostate–testis sharing may be valuable because these tissues have specialized metabolic and reproductive functions. Online searching found related literature on mitochondrial metabolism in prostate disease and on defined protein complexes such as GMPPA–GMPPB, but it did not identify this exact gene set or this exact conserved module. That supports novelty of the particular network observation, while the underlying gene functions and several relationships are already well established. Absence of the exact module from STRING or hu.MAP cannot by itself prove novelty, because those resources emphasize curated or experimentally supported interactions and do not necessarily represent co-abundance structure. Independent replication across cohorts, control for cell composition, and validation at the protein or single-cell level would be needed before claiming a novel tissue-shared mechanism.

**Hypothesis.** Hypothesis: the module represents a coordinated mitochondrial fitness program that supports energy production and metabolic flexibility in prostate and testis cells. In this model, HMGCL, ACAA1, DBT and ETFDH route lipid-derived and amino-acid-derived substrates toward mitochondrial or peroxisomal energy metabolism; ATPAF2 and TMEM70 preserve ATP-synthase assembly; BCS1L supports respiratory-chain complex assembly; NADK2 and SIRT5 help maintain mitochondrial redox and metabolic regulation; and PNPT1 and TUFM maintain mitochondrial RNA and protein production. APOOL and CISD2 could link mitochondrial architecture or stress handling to this metabolic state, while GMPPA–GMPPB and COG1–COG5 represent glycosylation and trafficking processes that may support the specialized membrane and secretory demands of the contributing cells. This is a mechanistic proposal, not a demonstrated causal model. An alternative explanation is that the module reflects shared abundance of metabolically active epithelial and germ-cell populations across the two tissues.

Web sources: https://www.nature.com/articles/s41594-021-00591-9; https://www.mdpi.com/1422-0067/24/5/4482; https://pmc.ncbi.nlm.nih.gov/articles/PMC9953833/

### Important genes

#### HMGCL

- **Related proteins** (co-abundance neighbors): RTCA (0.94), APOOL (0.85), COG5 (0.83), DCAKD (0.81), ETFDH (0.80); STRING partners: ACAA1 (0.965)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_01270.1, huMAP3_09533.1
- **Function (MyGene.info)**: 3-hydroxy-3-methylglutaryl-CoA lyase. The protein encoded by this gene belongs to the HMG-CoA lyase family. It is a mitochondrial enzyme that catalyzes the final step of leucine degradation and plays a key role in ketone body formation. Mutations in this gene are associated with HMG-CoA lyase deficiency. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2009].
- **Diseases (Open Targets)**: 3-hydroxy-3-methylglutaric aciduria (0.849); long chain 3-hydroxyacyl-CoA dehydrogenase deficiency (0.548); hereditary disease (0.494); Intellectual disability (0.370); neurodegenerative disease (0.215)
- **Europe PMC papers**: 1278
- **Why important**: HMGCL is among the stronger network-connected genes and is directly supported by (GO:CC mitochondrion; q_global = 0.0204). It encodes the mitochondrial enzyme that performs the final step of leucine degradation and contributes to ketone-body formation. It connects in STRING with ACAA1 and appears in several hu.MAP complexes with ATPAF2. Its established metabolic function, mitochondrial location in the module evidence, inherited HMG-CoA lyase deficiency association and substantial literature make it a central anchor for the interpretation.
- **Conclusion**: Established evidence supports HMGCL as a mitochondrial amino-acid and ketone-body metabolism component of the module. Its co-abundance with other mitochondrial genes is consistent with coordinated metabolic activity. It is not established that HMGCL regulates the entire module or that the prostate–testis sharing is caused by HMGCL.

#### ATPAF2

- **Related proteins** (co-abundance neighbors): ETFDH (0.85), NADK2 (0.85), DCXR (0.82), GMPPA (0.82); STRING partners: TMEM70 (0.96)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_01270.1, huMAP3_09533.1
- **Function (MyGene.info)**: ATP synthase mitochondrial F1 complex assembly factor 2. This gene encodes an assembly factor for the F(1) component of the mitochondrial ATP synthase. This protein binds specifically to the F1 alpha subunit and is thought to prevent this subunit from forming nonproductive homooligomers during enzyme assembly. This gene is located within the Smith-Magenis syndrome region on chromosome 17. An alternatively spliced transcript variant has been described, b…
- **Diseases (Open Targets)**: mitochondrial proton-transporting ATP synthase complex deficiency (0.708); mitochondrial complex V (ATP synthase) deficiency, nuclear type 1 (0.666); mitochondrial disease (0.505); squamous cell carcinoma (0.202); microcephaly (0.111)
- **Europe PMC papers**: 324
- **Why important**: ATPAF2 is a relatively central network gene, is included in (GO:CC mitochondrion; q_global = 0.0204), and has a defined role in assembly of the mitochondrial ATP-synthase F1 component. It connects strongly with TMEM70 in STRING and recurs with HMGCL in hu.MAP complexes. Its disease associations with mitochondrial ATP-synthase deficiency provide functional relevance, while its detection in both tissues and association with early spermatids make it particularly informative for a shared bioenergetic program.
- **Conclusion**: Established evidence supports ATPAF2 as an ATP-synthase assembly factor embedded in the module's mitochondrial function. The data support coordinated abundance with other energy-related genes, but do not demonstrate that ATPAF2 is a limiting factor or causal driver of the module.

#### ACAA1

- **Related proteins** (co-abundance neighbors): PDXDC1 (0.89), COG1 (0.89), APOOL (0.86), SIRT5 (0.83), UBE3A (0.81); STRING partners: DBT (0.848), HMGCL (0.965), HSDL2 (0.916)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Peroxisomes; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA acyltransferase 1. This gene encodes an enzyme operative in the beta-oxidation system of the peroxisomes. Deficiency of this enzyme leads to pseudo-Zellweger syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: hyperpituitarism (0.348); Follicular Cyst (0.127); Sepsis (0.103); neoplasm (0.098); Alzheimer disease (0.082)
- **Europe PMC papers**: 1153
- **Why important**: ACAA1 has strong network connectivity and several high-confidence STRING links, especially to HMGCL and HSDL2. It encodes a peroxisomal acetyl-CoA acyltransferase involved in fatty-acid beta-oxidation and related lipid processes. It is included in the supplementary metabolic disease terms (4 supplementary STRING terms; within-query FDR 0.0054–0.0293), has a well-established biochemical function and disease relevance through pseudo-Zellweger syndrome, and has substantial literature support.
- **Conclusion**: Established evidence supports ACAA1 as a lipid-catabolic and peroxisomal counterpart to the mitochondrial metabolic core. Its position suggests a bridge between lipid handling and the mitochondrial program, but the network does not prove direct metabolic flux from ACAA1 into HMGCL in these tissues.

#### PNPT1

- **Related proteins** (co-abundance neighbors): CISD2 (0.87), SPR (0.83), TMEM70 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10458.1
- **Function (MyGene.info)**: polyribonucleotide nucleotidyltransferase 1. The protein encoded by this gene belongs to the evolutionary conserved polynucleotide phosphorylase family comprised of phosphate dependent 3'-to-5' exoribonucleases implicated in RNA processing and degradation. This enzyme is predominantly localized in the mitochondrial intermembrane space and is involved in import of RNA to mitochondria. Mutations in this gene have been associated with combined …
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 13 (0.807); autosomal recessive nonsyndromic hearing loss 70 (0.740); spinocerebellar ataxia type 25 (0.709); deafness (0.676); hearing loss, autosomal recessive (0.634)
- **Europe PMC papers**: 839
- **Why important**: PNPT1 is included in (GO:CC mitochondrion; q_global = 0.0204), is connected to CISD2, SPR and TMEM70 in the module network, and occurs in hu.MAP complexes containing mitochondrial RNA-processing and metabolic machinery. It participates in mitochondrial RNA import, processing and degradation, and is associated with combined oxidative-phosphorylation deficiency and inherited hearing loss. Its role links mitochondrial gene-expression capacity to the respiratory and metabolic functions represented by the module.
- **Conclusion**: Established evidence supports PNPT1 as a mitochondrial RNA-maintenance component that can sustain oxidative-phosphorylation capacity. The module data support its coordination with mitochondrial metabolism, but do not establish that altered PNPT1 activity drives the shared prostate–testis pattern.

#### GMPPA

- **Related proteins** (co-abundance neighbors): ATPAF2 (0.82); STRING partners: GMPPB (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_01176.1, huMAP3_09879.1, huMAP3_01694.1, huMAP3_07434.1, huMAP3_05572.1, huMAP3_12121.1
- **Function (MyGene.info)**: GDP-mannose pyrophosphorylase A. This gene is thought to encode a GDP-mannose pyrophosphorylase. This enzyme catalyzes the reaction which converts mannose-1-phosphate and GTP to GDP-mannose which is involved in the production of N-linked oligosaccharides. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: triple-A syndrome (0.795); hereditary disease (0.414); syndromic X-linked intellectual disability 17 (0.370); chromosomal instability with tissue-specific radiosensitivity (0.340); neoplasm (0.083)
- **Europe PMC papers**: 747
- **Why important**: GMPPA is connected in the module network to ATPAF2 and has a very strong STRING relationship with GMPPB. The pair recurs across multiple hu.MAP complexes, and the supplied online search identified structural and functional work showing that GMPPA and GMPPB form a defined complex involved in GDP-mannose production, with GMPPA acting as a GDP-mannose sensor and regulator of GMPPB activity. GMPPA therefore provides a well-supported glycosylation and metabolic-control link that is distinct from the mitochondrial core.
- **Conclusion**: Established evidence supports GMPPA as part of the known GMPPA–GMPPB GDP-mannose biosynthetic complex. Its presence in this module may indicate coordinated glycoprotein production or Golgi-related cellular demand, but it remains a hypothesis that this process mechanistically couples to mitochondrial metabolism in prostate and testis.

#### TMEM70

- **Related proteins** (co-abundance neighbors): PNPT1 (0.82); STRING partners: ATPAF2 (0.96)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_06247.1, huMAP3_09592.1
- **Function (MyGene.info)**: transmembrane protein 70. This gene likely encodes a mitochondrial membrane protein. The encoded protein may play a role in biogenesis of mitochondrial ATP synthase. Mutations in this gene have been associated with neonatal mitochondrial encephalocardiomyopathy due to ATP synthase deficiency. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: mitochondrial complex V (ATP synthase) deficiency, nuclear type 2 (0.811); mitochondrial disease (0.597); mitochondrial proton-transporting ATP synthase complex deficiency (0.588); hereditary disease (0.413); cardiomyopathy (0.371)
- **Europe PMC papers**: 490
- **Why important**: TMEM70 is included in (GO:CC mitochondrion; q_global = 0.0204), is linked strongly to ATPAF2 in STRING, and appears with ATPAF2 in hu.MAP complexes. It is a mitochondrial membrane protein implicated in ATP-synthase biogenesis and is associated with mitochondrial complex V deficiency and cardiomyopathy. Its detection in both tissues and its connection to spermatogenic cell types make it a strong complementary marker of the module's bioenergetic interpretation.
- **Conclusion**: Established evidence supports TMEM70 as an ATP-synthase biogenesis component aligned with ATPAF2 and the mitochondrial enrichment. The module suggests coordinated abundance of these factors, but does not establish a tissue-specific TMEM70 mechanism or a causal role in the conserved module.

## Module 4

**Tissue pair**: prostate and testis  
**Genes (40)**: ADK, FDXR, ALDH3A2, ALG5, ANP32E, APEX1, ATP1A1, ATXN10, BABAM2, BLVRA, BROX, CPNE1, DCPS, ELMOD2, GET3, GMFB, HARS1, HDGF, HNRNPH1, HNRNPF, IDI1, MVK, LSM6, SNU13, NSDHL, NUDT5, OLA1, P4HA1, PGM2, PRDX3, PRRC1, PTBP1, GART, ATIC, RAB3GAP2, SRSF7, ACAT2, TST, TMOD3, TMX1

### Function

The module is best interpreted as a broadly expressed intracellular maintenance program combining RNA processing with core metabolic and proteostasis activities. The strongest network-centered signal is an RNA-processing and splicing component: HNRNPF, HNRNPH1, PTBP1, and SRSF7 form a densely connected group supported by high-confidence STRING relationships, while HNRNPF and HNRNPH1 recur across several hu.MAP complexes (hu.MAP huMAP3_07055.1) (hu.MAP huMAP3_06054.1) (hu.MAP huMAP3_11034.1) (hu.MAP huMAP3_13511.1) (hu.MAP huMAP3_14523.1). SNU13 and LSM6 provide an additional spliceosomal and small-nuclear-ribonucleoprotein connection, supported by STRING and hu.MAP (hu.MAP huMAP3_08980.1). A second component concerns sterol and isoprenoid metabolism, represented by ACAT2, IDI1, MVK, and NSDHL, with known STRING relationships among these genes. GART and ATIC form a known purine-biosynthesis relationship in STRING and are represented together in hu.MAP (hu.MAP huMAP3_14442.1). Additional genes connect DNA repair, oxidative stress, ER function, protein trafficking, nucleotide metabolism, and membrane biology. No GO or KEGG term passed global correction, so these annotations are mechanistic interpretation of the constituent genes and network structure rather than globally significant enrichment. The absence of a globally enriched term does not invalidate the module.

**Cell composition.** The module does not appear to be dominated by plasma or secreted proteins, and it is not blood-cell enriched. HPA reports only a small secreted fraction, predominantly intracellular or membrane-associated locations, and low immune-cell specificity for nearly all genes. Most genes have low tissue specificity and many have low cell-type specificity, consistent with a broadly expressed housekeeping-like program. There is some contribution from liver-enhanced genes and from epithelial, trophoblast, adrenal, and reproductive cell states, but these patterns do not establish a prostate- or testis-specific cellular identity. Protein detection is widespread in both prostate and testis, supporting reproducibility of the tissue-pair association while also indicating that the shared signal may reflect common cellular machinery rather than a specialized organ function. The presence of a few blood-cell-enhanced annotations should therefore be treated as minor context, not as evidence that the module is a blood-contamination signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports several internally coherent, already known relationships. The clearest group is the RNA-processing cluster involving HNRNPF, HNRNPH1, PTBP1, and SRSF7, together with the SNU13–LSM6 relationship. STRING also supports the sterol and isoprenoid group involving ACAT2, IDI1, MVK, and NSDHL; the ATIC–GART purine-biosynthesis relationship; and the NUDT5–PGM2 relationship. hu.MAP independently supports repeated association of HNRNPF and HNRNPH1 with hnRNP-containing complexes (hu.MAP huMAP3_07055.1) (hu.MAP huMAP3_06054.1) (hu.MAP huMAP3_11034.1) (hu.MAP huMAP3_13511.1) (hu.MAP huMAP3_14523.1), the APEX1–ATIC–OLA1 membership pattern (hu.MAP huMAP3_14442.1), the ALDH3A2–ATXN10 pattern (hu.MAP huMAP3_09592.1), and the SNU13–LSM6 pattern (hu.MAP huMAP3_08980.1). These databases show that multiple portions of the module recapitulate established molecular machinery. They support biological plausibility, but they do not demonstrate that all co-abundance edges are direct physical interactions or that the complete module is a single physical complex.

**STRING interactions (score >= 0.7)**: 14 of 780 gene pairs: ACAT2–IDI1 (0.828); ACAT2–MVK (0.885); ATIC–GART (0.999); HNRNPF–HNRNPH1 (0.994); HNRNPF–PTBP1 (0.942); HNRNPF–SRSF7 (0.918); HNRNPH1–PTBP1 (0.978); HNRNPH1–SRSF7 (0.922); IDI1–MVK (0.879); IDI1–NSDHL (0.856); LSM6–SNU13 (0.997); MVK–NSDHL (0.811); NUDT5–PGM2 (0.912); PTBP1–SRSF7 (0.933)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (APEX1, ATIC, OLA1; 3/57); huMAP3_07055.1 (HNRNPH1, HNRNPF; 2/3); huMAP3_06054.1 (HNRNPH1, HNRNPF; 2/4); huMAP3_11034.1 (HNRNPH1, HNRNPF; 2/5); huMAP3_13511.1 (HNRNPH1, HNRNPF; 2/9); huMAP3_14523.1 (HNRNPH1, HNRNPF; 2/33); huMAP3_09592.1 (ALDH3A2, ATXN10; 2/95); huMAP3_08980.1 (SNU13, LSM6; 2/97)

### Novelty

The complete prostate–testis co-abundance module should not be called a wholly new molecular pathway. Several of its subnetworks are established RNA-processing, sterol-metabolic, purine-metabolic, and cellular-maintenance relationships, as shown by STRING and hu.MAP. A potentially novel aspect is the specific cross-tissue co-abundance arrangement that links these otherwise distinct processes, but the fact sheet does not provide an external matched-tissue module catalogue, perturbation evidence, or independent replication sufficient to establish novelty. Absence of a complete matching complex in STRING or hu.MAP would not by itself prove novelty. The most defensible conclusion is that this is a potentially useful tissue-shared transcriptional or proteomic organization of known housekeeping programs, with novelty at the level of the integrated co-abundance pattern remaining unconfirmed.

**Hypothesis.** Hypothesis: shared cellular demands in prostate and testis coordinate RNA maturation and alternative splicing with biosynthetic and stress-buffering capacity. The hnRNP and spliceosomal component may regulate processing of transcripts required for sterol production, purine synthesis, ER protein handling, DNA repair, and oxidative-stress control. The sterol and isoprenoid genes may be particularly relevant to membrane production and reproductive-cell physiology, while the purine, redox, and ER genes may support proliferation, differentiation, and protein quality control. This is a mechanistic model generated from the network and gene annotations; the data do not establish directionality, causal regulation, or a direct physical complex.

### Important genes

#### HNRNPF

- **Related proteins** (co-abundance neighbors): HNRNPH1 (0.85), SRSF7 (0.84), HDGF (0.84), PTBP1 (0.84), GMFB (0.82), APEX1 (0.81), ATXN10 (0.80); STRING partners: HNRNPH1 (0.994), PTBP1 (0.942), SRSF7 (0.918)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_07055.1, huMAP3_06054.1, huMAP3_11034.1, huMAP3_13511.1, huMAP3_14523.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein F. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins that complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and regulate alternative splicing, polyadenylation, and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present…
- **Diseases (Open Targets)**: neurodegenerative disease (0.518); dengue disease (0.370); knee fracture (0.322); breast cancer (0.103); posterior cortical atrophy (0.083)
- **Europe PMC papers**: 971
- **Why important**: HNRNPF is the leading network hub in the supplied module and connects the principal RNA-processing group with genes involved in DNA repair, redox biology, and cellular metabolism. Its established role is binding heterogeneous nuclear RNA and regulating pre-mRNA processing, alternative splicing, polyadenylation, and RNA transport. It is supported by several hu.MAP complexes (hu.MAP huMAP3_07055.1) (hu.MAP huMAP3_06054.1) (hu.MAP huMAP3_11034.1) (hu.MAP huMAP3_13511.1) (hu.MAP huMAP3_14523.1) and by high-confidence STRING links to HNRNPH1, PTBP1, and SRSF7. Its extensive literature and disease associations make it a strong interpretive anchor.
- **Conclusion**: Established evidence supports HNRNPF as a central RNA-processing component and a plausible organizer of the module's most coherent network sector. It is not established that HNRNPF causally coordinates the metabolic genes in this module; that connection remains a hypothesis.

#### PTBP1

- **Related proteins** (co-abundance neighbors): APEX1 (0.88), ADK (0.84), HNRNPF (0.84), P4HA1 (0.83), NSDHL (0.83), HDGF (0.81); STRING partners: HNRNPF (0.942), HNRNPH1 (0.978), SRSF7 (0.933)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypyrimidine tract binding protein 1. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA-binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.505); dengue disease (0.372); open-angle glaucoma (0.330); glaucoma (0.309); neoplasm (0.116)
- **Europe PMC papers**: 4849
- **Why important**: PTBP1 is a highly connected module member within the RNA-processing sector and has strong STRING links to HNRNPF, HNRNPH1, and SRSF7. Its established functions include polypyrimidine-tract binding, mRNA processing, and regulation of alternative splicing. It has substantial literature coverage and broad disease associations, consistent with a widely used cellular regulatory factor rather than a tissue-exclusive marker.
- **Conclusion**: Established evidence supports PTBP1 as an important splicing and RNA-processing node that may help explain coordinated abundance of the hnRNP group. A prostate–testis-specific regulatory role or direct control of the other module sectors is not demonstrated.

#### HNRNPH1

- **Related proteins** (co-abundance neighbors): SRSF7 (0.89), HNRNPF (0.85), FDXR (0.85), APEX1 (0.82); STRING partners: HNRNPF (0.994), PTBP1 (0.978), SRSF7 (0.922)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_07055.1, huMAP3_06054.1, huMAP3_11034.1, huMAP3_13511.1, huMAP3_14523.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein H1. This gene encodes a member of a subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins that complex with heterogeneous nuclear RNA. These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the n…
- **Diseases (Open Targets)**: neurodevelopmental disorder with craniofacial dysmorphism and skeletal defects (0.668); dengue disease (0.462); hereditary disease (0.411); neurodevelopmental disorder (0.400); syndromic intellectual disability (0.370)
- **Europe PMC papers**: 1509
- **Why important**: HNRNPH1 is part of the dense RNA-processing core, has strong STRING relationships with HNRNPF, PTBP1, and SRSF7, and recurs across multiple hu.MAP complexes (hu.MAP huMAP3_07055.1) (hu.MAP huMAP3_06054.1) (hu.MAP huMAP3_11034.1) (hu.MAP huMAP3_13511.1) (hu.MAP huMAP3_14523.1). Its annotated functions in pre-mRNA splicing and RNA processing directly match the most internally supported module structure. Its disease and literature records further support its status as a well-established core RNA-binding factor.
- **Conclusion**: Established evidence supports HNRNPH1 as a central component of known hnRNP and splicing machinery. Its co-abundance with sterol, purine, and stress-related genes may reflect coordinated cellular state, but a direct mechanistic bridge is unproven.

#### IDI1

- **Related proteins** (co-abundance neighbors): ACAT2 (0.86), TMX1 (0.82), MVK (0.81); STRING partners: ACAT2 (0.828), MVK (0.879), NSDHL (0.856)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in prostate, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: isopentenyl-diphosphate delta isomerase 1. IDI1 encodes a peroxisomally-localized enzyme that catalyzes the interconversion of isopentenyl diphosphate (IPP) to its highly electrophilic isomer, dimethylallyl diphosphate (DMAPP), which are the substrates for the successive reaction that results in the synthesis of farnesyl diphosphate and, ultimately, cholesterol.  It has been shown in peroxisomal deficiency diseases such as Zellweger syndro…
- **Diseases (Open Targets)**: neurodegenerative disease (0.539); hypotensive disorder (0.215); placental retention (0.191); liver disorder (0.147); esophageal cancer (0.138)
- **Europe PMC papers**: 1844
- **Why important**: IDI1 marks the module's sterol and isoprenoid branch. It catalyzes interconversion of isopentenyl and dimethylallyl diphosphate and participates in cholesterol, isoprenoid, and geranylgeranyl-diphosphate biosynthesis. It connects in STRING to ACAT2, MVK, and NSDHL, providing a coherent metabolic chain rather than an isolated annotation. Its broad literature and disease associations make it a useful metabolic representative of the module.
- **Conclusion**: Established evidence supports IDI1 as a genuine sterol and isoprenoid biosynthesis component whose network relationships are biologically concordant. It is plausible that this pathway contributes to shared prostate–testis cellular physiology, but the module does not prove tissue-specific regulation of IDI1.

#### GART

- **Related proteins** (co-abundance neighbors): ATXN10 (0.85), RAB3GAP2 (0.84), DCPS (0.83), TMX1 (0.81), GET3 (0.81); STRING partners: ATIC (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase. The protein encoded by this gene is a trifunctional polypeptide. It has phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase activity which is required for de novo purine biosynthesis. This enzyme is highly conserved in vertebrates. Alternative splicing of this gene results in two transcript variants encoding different isoforms.…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.606); mesothelioma (0.584); malignant pleural mesothelioma (0.557); adenocarcinoma (0.486); anaplastic lung carcinoma (0.462)
- **Europe PMC papers**: 1890
- **Why important**: GART is a trifunctional enzyme in de novo purine biosynthesis and is connected to ATIC by an exceptionally strong STRING relationship. It also links in the co-abundance network to RAB3GAP2, ATXN10, DCPS, TMX1, and GET3, placing purine production alongside RNA turnover, trafficking, and ER-associated functions. Its substantial literature and cancer associations make it an informative marker of biosynthetic demand.
- **Conclusion**: Established evidence supports GART as a purine-biosynthesis component and as part of a known ATIC–GART relationship. Its inclusion may indicate shared nucleotide demand or general biosynthetic activity, but a specific reproductive-tissue mechanism is not established.

#### APEX1

- **Related proteins** (co-abundance neighbors): PTBP1 (0.88), P4HA1 (0.84), HNRNPH1 (0.82), HNRNPF (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: apurinic/apyrimidinic endodeoxyribonuclease 1. The APEX gene encodes the major AP endonuclease in human cells. It encodes the APEX endonuclease, a DNA repair enzyme with apurinic/apyrimidinic (AP) activity. Such AP activity sites occur frequently in DNA molecules by spontaneous hydrolysis, by DNA damaging agents or by DNA glycosylases that remove specific abnormal bases. The AP sites are the most frequent pre-mutagenic lesions that can prevent…
- **Diseases (Open Targets)**: neurodegenerative disease (0.464); Galloway-Mowat syndrome (0.429); hereditary disease (0.161); neoplasm (0.118); non-small cell lung carcinoma (0.115)
- **Europe PMC papers**: 2928
- **Why important**: APEX1 is a network bridge between the RNA-processing hub and other module sectors, connecting to PTBP1, HNRNPH1, P4HA1, and HNRNPF. Its established function is apurinic/apyrimidinic endonuclease activity in base-excision DNA repair, with additional roles in telomere maintenance and apoptotic signaling. It is also represented with ATIC and OLA1 in hu.MAP complex (hu.MAP huMAP3_14442.1), making it a useful link between genome maintenance and the broader module.
- **Conclusion**: Established evidence supports APEX1 as a DNA-repair and genome-maintenance factor positioned at an interface with the module's RNA-processing network. Its bridging position suggests a shared stress-response program, but does not establish direct regulation by the splicing factors.

## Module 5

**Tissue pair**: prostate and testis  
**Genes (13)**: CAPN2, CORO1C, DPYSL2, EHD1, EZR, RAP1GDS1, GCLC, LTA4H, PLS1, PLS3, TES, VASP, WDR1

### Function

The strongest interpretation is an actin-cytoskeleton and cell-structure module. The primary evidence is the globally corrected enrichment for cytoskeleton organization (GO:BP cytoskeleton organization; q_global = 0.01), regulation of anatomical structure size (GO:BP regulation of anatomical structure size; q_global = 0.0228), actin cytoskeleton (GO:CC actin cytoskeleton; q_global = 0.0331), and actin cytoskeleton organization (GO:BP actin cytoskeleton organization; q_global = 0.0474). The overlapping genes include CAPN2, CORO1C, DPYSL2, EZR, PLS1, PLS3, RAP1GDS1, VASP, and WDR1. These annotations are supported by the supplementary STRING enrichments for actin organization, actin-filament organization, cytoskeletal protein binding, cortical cytoskeleton, and cellular-component organization (10 supplementary STRING terms; within-query FDR 0.005–0.0484). The module therefore most plausibly reflects coordinated regulation of actin architecture, membrane–cytoskeleton coupling, cell shape, adhesion, motility, and structural remodeling. GCLC and LTA4H may connect this structural program with redox or inflammatory biology, while EHD1 may relate to membrane trafficking; these secondary interpretations are less directly supported than the actin-centered interpretation.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the listed proteins are intracellular, membrane-associated, or cytoskeletal. The module is mixed rather than uniformly tissue-specific. Most genes have low tissue specificity, with additional tissue-enhanced signals involving testis, brain, bone marrow, liver, intestine, blood vessel, and seminal vesicle. HPA single-cell annotations repeatedly implicate epithelial, spermatid, platelet, and myeloid-related cell types. Blood-cell specificity is generally low, although some genes show enrichment in platelets, megakaryocytes, NK cells, dendritic-cell populations, monocytes, or neutrophil-related populations. Thus, the prostate–testis association could reflect a shared epithelial or germ-cell structural program, shared vascular or stromal context, or contributions from common cell types in tissue samples. It should not be interpreted as a prostate- or testis-exclusive program without cell-composition and spatial validation. Protein detection is broader in testis than prostate in the HPA evidence, which also argues for caution when assigning the module to a single prostate cell population.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP cytoskeleton organization | 0.01 | CAPN2, CORO1C, DPYSL2, EZR, PLS1, PLS3, RAP1GDS1, VASP, WDR1 |
| GO:BP regulation of anatomical structure size | 0.0228 | EZR, GCLC, PLS1, RAP1GDS1, VASP, WDR1 |
| GO:CC actin cytoskeleton | 0.0331 | CAPN2, CORO1C, EZR, PLS1, PLS3, VASP, WDR1 |
| GO:BP actin cytoskeleton organization | 0.0474 | CORO1C, EZR, PLS1, PLS3, RAP1GDS1, VASP, WDR1 |

### STRING and hu.MAP

The network contains a limited set of high-confidence STRING relationships: CORO1C–PLS3, EZR–PLS1, EZR–VASP, and TES–VASP. These links directly support an actin-associated structural core, especially involving ezrin, plastins, VASP, coronin, and testin. hu.MAP provides additional complex-level support. PLS3, PLS1, EZR, and TES co-occur in a higher-confidence complex (hu.MAP huMAP3_10281.1), while PLS3, PLS1, and TES recur in other complexes (hu.MAP huMAP3_14442.1) (hu.MAP huMAP3_07456.1), and PLS1–PLS3 appear together in several further complexes (hu.MAP huMAP3_05481.1) (hu.MAP huMAP3_03533.1) (hu.MAP huMAP3_10900.1). WDR1 and CORO1C co-occur in an actin-remodeling complex containing other actin regulators (hu.MAP huMAP3_11076.1). These data indicate that some module relationships are already represented in curated or experimentally derived interaction resources, but many co-abundance edges are not supported by high-confidence STRING links. The module is therefore more convincingly a coordinated biological program than a single fully resolved physical complex.

**STRING interactions (score >= 0.7)**: 4 of 78 gene pairs: CORO1C–PLS3 (0.818); EZR–PLS1 (0.899); EZR–VASP (0.844); TES–VASP (0.827)
**STRING functional enrichment (supplementary, within-query FDR)**: Process Regulation of anatomical structure size (FDR = 0.005, 7 genes); COMPARTMENTS Actin cytoskeleton (FDR = 0.0061, 7 genes); Component Actin cytoskeleton (FDR = 0.0125, 7 genes); Process Cytoskeleton organization (FDR = 0.0151, 8 genes); Process Actin filament organization (FDR = 0.0151, 6 genes); Process Actin cytoskeleton organization (FDR = 0.0151, 7 genes); Process Regulation of cellular component organization (FDR = 0.0151, 10 genes); Process Supramolecular fiber organization (FDR = 0.0151, 7 genes); Function Cytoskeletal protein binding (FDR = 0.0151, 8 genes); Component Cortical cytoskeleton (FDR = 0.0484, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10281.1 (PLS3, EZR, PLS1, TES; 4/9); huMAP3_14442.1 (LTA4H, PLS3, PLS1, TES; 4/57); huMAP3_07456.1 (PLS3, PLS1, TES; 3/5); huMAP3_05481.1 (PLS3, PLS1; 2/3); huMAP3_03533.1 (PLS3, PLS1; 2/4); huMAP3_10900.1 (PLS3, PLS1; 2/6); huMAP3_11076.1 (WDR1, CORO1C; 2/10)

### Novelty

The actin-cytoskeleton interpretation is not, by itself, a new biological concept: the functions of EZR, plastins, VASP, WDR1, CORO1C, CAPN2, and TES are established, and several relationships are already represented by STRING or hu.MAP. However, the prostate–testis conserved co-abundance organization may still be a useful systems-level observation, particularly because it combines structural, membrane-associated, spermatid-associated, epithelial, and platelet-related signals. Absence of an edge from STRING or hu.MAP cannot establish novelty, because those resources do not comprehensively represent tissue-specific co-abundance or context-dependent regulation. A defensible novelty claim is therefore limited: this appears to be a potentially context-specific module arrangement rather than a newly discovered molecular function. Independent replication, comparison with published prostate and testis co-expression modules, and validation in purified cell populations would be required before calling it a new finding.

**Hypothesis.** Hypothesis: in prostate and testis samples, a shared membrane–actin remodeling program coordinates cortical actin organization with cell shape, adhesion, junctional behavior, and structural changes associated with epithelial or germ-cell maturation. EZR may couple the plasma membrane to actin, PLS1 and PLS3 may bundle actin filaments, VASP may promote actin assembly at adhesion or junctional sites, and WDR1 together with CORO1C may regulate filament turnover. CAPN2 and RAP1GDS1 could modulate remodeling and signaling, while EHD1 could connect membrane trafficking to the structural program. TES may provide a focal-adhesion or Sertoli/germ-cell-associated context. The observed co-abundance could also partly arise from shared cell-type composition, especially epithelial, spermatid, platelet, or immune-related cells; this alternative must be tested rather than assumed away.

### Important genes

#### EZR

- **Related proteins** (co-abundance neighbors): CAPN2 (0.90), RAP1GDS1 (0.85), PLS3 (0.83); STRING partners: PLS1 (0.899), VASP (0.844)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_10281.1
- **Function (MyGene.info)**: ezrin. The cytoplasmic peripheral membrane protein encoded by this gene functions as a protein-tyrosine kinase substrate in microvilli. As a member of the ERM protein family, this protein serves as an intermediate between the plasma membrane and the actin cytoskeleton. This protein plays a key role in cell surface structure adhesion, migration and organization, and it has been implicated in various human…
- **Diseases (Open Targets)**: hair color (0.477); non-small cell lung carcinoma (0.397); lung adenocarcinoma (0.382); autosomal recessive non-syndromic intellectual disability (0.370); glaucoma (0.347)
- **Europe PMC papers**: 4982
- **Why important**: EZR is a central structural connector in the module’s network and is the only gene directly linked by high-confidence STRING evidence to both PLS1 and VASP. It is present in every primary enrichment term (4 globally significant GO/KEGG terms, q_global 0.01–0.0474; see the table) and every supplementary STRING category (10 supplementary STRING terms; within-query FDR 0.005–0.0484). Its established function as an ERM-family linker between the plasma membrane and actin cytoskeleton makes it a strong mechanistic anchor. It is detected in both prostate and testis and has extensive disease and literature coverage.
- **Conclusion**: Established evidence supports EZR as a core membrane–actin organizer in this module. It is reasonable to hypothesize that EZR helps couple tissue-specific membrane structures to the shared actin program, but the co-abundance data do not establish causality or a prostate–testis-specific mechanism.

#### PLS1

- **Related proteins** (co-abundance neighbors): LTA4H (0.85); STRING partners: EZR (0.899)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_10281.1, huMAP3_14442.1, huMAP3_07456.1, huMAP3_05481.1, huMAP3_03533.1, huMAP3_10900.1
- **Function (MyGene.info)**: plastin 1. Plastins are a family of actin-binding proteins that are conserved throughout eukaryote evolution and expressed in most tissues of higher eukaryotes. In humans, two ubiquitous plastin isoforms (L and T) have been identified. The protein encoded by this gene is a third distinct plastin isoform, which is specifically expressed at high levels in the small intestine. Alternatively spliced transcript v…
- **Diseases (Open Targets)**: hearing loss, autosomal dominant 76 (0.697); autosomal dominant nonsyndromic hearing loss (0.551); neurodegenerative disease (0.370); sensorineural hearing loss disorder (0.259); alcohol drinking (0.241)
- **Europe PMC papers**: 1388
- **Why important**: PLS1 has the broadest hu.MAP participation in the module, recurring with PLS3, EZR, and TES across multiple complexes (hu.MAP huMAP3_10281.1) (hu.MAP huMAP3_14442.1) (hu.MAP huMAP3_07456.1) (hu.MAP huMAP3_05481.1) (hu.MAP huMAP3_03533.1) (hu.MAP huMAP3_10900.1). It appears in all primary enrichment terms (4 globally significant GO/KEGG terms, q_global 0.01–0.0474; see the table) and all supplementary STRING categories (10 supplementary STRING terms; within-query FDR 0.005–0.0484). Its established actin-bundling and microvillus-related functions are directly relevant to cell shape and epithelial specialization. HPA reports tissue enrichment in intestine and detection in testis, so its presence may mark a specialized epithelial or germ-cell structural state rather than a broadly uniform tissue signal.
- **Conclusion**: Established evidence supports PLS1 as an actin-bundle and membrane-structure component. A testis-associated role in the conserved module is plausible, but its absence of prostate protein detection in the supplied HPA evidence means that sample composition or transcript–protein differences must be considered.

#### WDR1

- **Related proteins** (co-abundance neighbors): LTA4H (0.87), DPYSL2 (0.84), TES (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions, Cytosol; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_11076.1
- **Function (MyGene.info)**: WD repeat domain 1. This gene encodes a protein containing 9 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, mostly including a trp-asp at the C-terminal end. WD domains are involved in protein-protein interactions. The encoded protein may help induce the disassembly of actin filaments. Two transcript variants encoding different isoforms have been found for…
- **Diseases (Open Targets)**: periodic fever, immunodeficiency, and thrombocytopenia syndrome (0.705); gout (0.528); neurodegenerative disease (0.526); atrial fibrillation (0.519); intellectual developmental disorder 61 (0.416)
- **Europe PMC papers**: 1861
- **Why important**: WDR1 occupies a connected position linking LTA4H, DPYSL2, and TES and is represented in every primary enrichment term (4 globally significant GO/KEGG terms, q_global 0.01–0.0474; see the table) and every supplementary STRING category (10 supplementary STRING terms; within-query FDR 0.005–0.0484). Its established role in actin-filament disassembly and its hu.MAP association with CORO1C (hu.MAP huMAP3_11076.1) provide a direct rationale for including an actin-turnover regulator in the module. HPA links it to early and late spermatids, megakaryocytes, and platelets, which is relevant to the mixed structural and cell-composition interpretation.
- **Conclusion**: Established evidence supports WDR1 as a regulator of actin filament turnover within the module. The hypothesis that it coordinates remodeling during spermatid or epithelial structural change remains untested and could alternatively reflect contributions from platelet or related cell populations.

#### VASP

- **Related proteins** (co-abundance neighbors): EHD1 (0.85); STRING partners: EZR (0.844), TES (0.827)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions, Focal adhesion sites; IHC detected in prostate, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vasodilator stimulated phosphoprotein. Vasodilator-stimulated phosphoprotein (VASP) is a member of the Ena-VASP protein family. Ena-VASP family members contain an EHV1 N-terminal domain that binds proteins containing E/DFPPPPXD/E motifs and targets Ena-VASP proteins to focal adhesions. In the mid-region of the protein, family members have a proline-rich domain that binds SH3 and WW domain-containing proteins. Their C-terminal EVH2 doma…
- **Diseases (Open Targets)**: neurodegenerative disease (0.215); Hypercholesterolemia (0.133); breast cancer (0.110); breast carcinoma (0.105); hepatocellular carcinoma (0.102)
- **Europe PMC papers**: 5374
- **Why important**: VASP is present in every primary enrichment term (4 globally significant GO/KEGG terms, q_global 0.01–0.0474; see the table) and nearly all supplementary STRING categories (9 supplementary STRING terms; within-query FDR 0.005–0.0151). It has high-confidence STRING relationships with EZR and TES, connecting membrane–actin organization with focal-adhesion and testin-associated context. Its established Ena–VASP functions include actin binding, filament polymerization, focal-adhesion association, and tetramerization. HPA detects it in both tissues and associates it with cell junctions, focal adhesions, platelets, megakaryocytes, and neutrophil-related cells.
- **Conclusion**: Established evidence supports VASP as an actin-assembly and adhesion-associated component. It may help explain the module’s structural phenotype, but its broad cell-type distribution means that a shared blood-cell or vascular contribution cannot be excluded.

#### TES

- **Related proteins** (co-abundance neighbors): WDR1 (0.81); STRING partners: VASP (0.827)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_10281.1, huMAP3_14442.1, huMAP3_07456.1
- **Function (MyGene.info)**: testin LIM domain protein. Cancer-associated chromosomal changes often involve regions containing fragile sites. This gene maps to a common fragile site on chromosome 7q31.2 designated FRA7G. This gene is similar to mouse Testin, a testosterone-responsive gene encoding a Sertoli cell secretory protein containing three LIM domains. LIM domains are double zinc-finger motifs that mediate protein-protein interactions between tr…
- **Diseases (Open Targets)**: open-angle glaucoma (0.490); glaucoma (0.440); placenta praevia (0.258); spinal cord injury (0.246); Joint stiffness (0.173)
- **Europe PMC papers**: 32609
- **Why important**: TES has a direct high-confidence STRING relationship with VASP and recurs with PLS1 and PLS3 in hu.MAP complexes (hu.MAP huMAP3_10281.1) (hu.MAP huMAP3_14442.1) (hu.MAP huMAP3_07456.1). HPA reports tissue enhancement in seminal vesicle and single-cell association with early spermatids and several epithelial populations. Its LIM domains are established protein-interaction modules, and its literature volume is substantial relative to many other module members. It therefore provides a biologically informative link between actin-associated complexes and reproductive-tissue context, despite not appearing in the primary GO terms.
- **Conclusion**: Established evidence supports TES as a reproductive-tissue-associated interaction scaffold connected to the actin network. Its role as a driver of the conserved prostate–testis module is a hypothesis; the available evidence also permits a simpler explanation involving shared reproductive or epithelial cell composition.

## Module 6

**Tissue pair**: prostate and testis  
**Genes (5)**: CYRIB, ENAH, HPRT1, MEMO1, PYGL

### Function

No GO/KEGG term passed global correction, so the module has no statistically established pathway-level annotation from the primary enrichment analysis. Its gene content instead suggests a mixed cellular program involving purine salvage through HPRT1, glycogen and glucose metabolism through PYGL, and cytoskeletal, adhesion, motility, and small-GTPase-related processes through ENAH, MEMO1, and CYRIB. Because these functions are heterogeneous and the module is small, the safest interpretation is a shared cellular-state or cell-composition signal rather than a single defined biochemical pathway.

**Cell composition.** The module is not composed of secreted proteins, arguing against a plasma-protein explanation. Most genes have low tissue specificity, while the tissue-enhanced genes include PYGL in liver and CYRIB in bone marrow. The single-cell annotations are heterogeneous, with recurrent signals in Sertoli cells, neutrophil-lineage cells, and microglia, alongside smooth muscle and several neural or glial populations. HPRT1, MEMO1, and ENAH are detected in both prostate and testis, whereas PYGL and CYRIB are detected in testis but not prostate by the reported IHC summary. This pattern is compatible with shared cell types or sample composition contributing to the prostate-testis co-abundance signal, especially Sertoli-related biology, but it does not establish blood contamination: only PYGL is immune-cell enhanced, CYRIB has low immune-cell specificity, and one gene is not detected in immune cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional-enrichment result was available, no high-confidence STRING interaction was reported among the module genes, and no hu.MAP complex contained multiple module members. Thus the co-abundance relationships are not supported here by previously catalogued high-confidence physical or functional interactions or by a known shared complex. The network should therefore be interpreted as an expression-covariation structure rather than a validated molecular complex. The strongest network position belongs to HPRT1, which connects the other functional neighborhoods represented by PYGL, ENAH, and MEMO1; MEMO1 links HPRT1 with CYRIB.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may represent a previously unreported co-abundance pattern in the prostate-testis comparison, but the available evidence is insufficient to call it a new biological mechanism. The absence of STRING and hu.MAP support does not prove novelty, because those resources capture selected known interactions and complexes rather than all expression relationships. The heterogeneous annotations, lack of globally significant GO/KEGG terms, and absence of STRING enrichment make a strong claim of a novel coherent pathway premature. A defensible novelty statement is that the specific cross-tissue co-abundance configuration appears uncatalogued in the supplied resources and requires independent replication and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a shared somatic or support-cell state in prostate and testis that couples purine salvage and metabolic readiness with actin remodeling, adhesion, and cell motility. HPRT1 and PYGL could mark nucleotide and carbohydrate metabolic demand, while ENAH, MEMO1, and CYRIB could represent cytoskeletal or small-GTPase-related remodeling. The recurrent Sertoli-cell annotation makes a testicular support-cell contribution plausible, but the mixed immune, glial, smooth-muscle, and metabolic annotations also allow a broader cell-composition explanation. This hypothesis should be tested by cell-resolved expression analysis, replication in independent cohorts, and perturbation of the candidate genes in relevant prostate and testis cell models.

### Important genes

#### HPRT1

- **Related proteins** (co-abundance neighbors): PYGL (0.91), ENAH (0.82), MEMO1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hypoxanthine phosphoribosyltransferase 1. The protein encoded by this gene is a transferase, which catalyzes conversion of hypoxanthine to inosine monophosphate and guanine to guanosine monophosphate via transfer of the 5-phosphoribosyl group from 5-phosphoribosyl 1-pyrophosphate. This enzyme plays a central role in the generation of purine nucleotides through the purine salvage pathway. Mutations in this gene result in Lesch-Nyhan syndro…
- **Diseases (Open Targets)**: Lesch-Nyhan syndrome (0.856); hypoxanthine guanine phosphoribosyltransferase partial deficiency (0.827); neurodegenerative disease (0.439); dystonic disorder (0.372); autoimmune disorder of central nervous system (0.370)
- **Europe PMC papers**: 15377
- **Why important**: HPRT1 is the central network connector and has the broadest set of module neighbors. Its established function in hypoxanthine and guanine purine salvage provides a concrete metabolic interpretation, and its HPA profile is compatible with both prostate and testis expression, including early primary spermatocytes and Sertoli cells. Its extensive literature and established links to Lesch-Nyhan syndrome and gout make it the best-supported anchor for the module.
- **Conclusion**: Established evidence supports HPRT1 as a purine-salvage enzyme and the principal network connector. It is plausible, but not established, that HPRT1 links metabolic demand to the other co-abundant genes in this module.

#### ENAH

- **Related proteins** (co-abundance neighbors): HPRT1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Focal adhesion sites, Cytosol; IHC detected in prostate, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ENAH actin regulator. This gene encodes a member of the enabled/ vasodilator-stimulated phosphoprotein. Members of this gene family are involved in actin-based motility. This protein is involved in regulating the assembly of actin filaments and modulates cell adhesion and motility. Alternate splice variants of this gene have been correlated with tumor invasiveness in certain tissues and these variants may serve as prog…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.232); body weight gain (0.219); inherited retinal dystrophy (0.176); type 2 diabetes mellitus (0.121); neoplasm (0.112)
- **Europe PMC papers**: 1290
- **Why important**: ENAH contributes a functionally distinct cytoskeletal and adhesion axis. Its annotated roles in actin regulation, actin-dependent motility, and cell adhesion fit the prostate and testis localization data and its enrichment in Sertoli and smooth muscle cells. Its substantial literature and reported relationship to tumor invasiveness make it relevant to tissue architecture and cellular movement, despite its peripheral network position.
- **Conclusion**: Established evidence supports ENAH as an actin-based motility and adhesion regulator. Its participation in this module may indicate coordinated remodeling of cell contacts, but the co-abundance data do not prove a direct interaction with HPRT1.

#### PYGL

- **Related proteins** (co-abundance neighbors): HPRT1 (0.91); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycogen phosphorylase L. This gene encodes a homodimeric protein that catalyses the cleavage of alpha-1,4-glucosidic bonds to release glucose-1-phosphate from liver glycogen stores. This protein switches from inactive phosphorylase B to active phosphorylase A by phosphorylation of serine residue 15. Activity of this enzyme is further regulated by multiple allosteric effectors and hormonal controls. Humans have three glyco…
- **Diseases (Open Targets)**: glycogen storage disease VI (0.821); disorder of glycogen metabolism (0.647); glycogen storage disease XV (0.596); neurodegenerative disease (0.370); Cholecystitis (0.357)
- **Europe PMC papers**: 1838
- **Why important**: PYGL is the module's clearest glycogen-metabolism marker and is the only tissue-enhanced gene associated with liver in the HPA summary. It is also immune-cell enhanced for eosinophil and neutrophil annotations and is detected in testis. Its established role in glycogen breakdown and its disease associations with glycogen-storage disorders provide a strong metabolic complement to HPRT1.
- **Conclusion**: Established evidence supports PYGL as a glycogen-catabolism and glucose-homeostasis enzyme. A metabolic-state interpretation is reasonable, but the liver and immune-cell annotations mean that its presence could also reflect cell composition rather than a testis-specific mechanism.

#### MEMO1

- **Related proteins** (co-abundance neighbors): CYRIB (0.85), HPRT1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Vesicles; IHC detected in prostate, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mediator of cell motility 1. Involved in regulation of microtubule-based process. Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.419); androgenetic alopecia (0.393); alopecia (0.292); obesity disorder (0.233); Parkinson disease (0.179)
- **Europe PMC papers**: 357
- **Why important**: MEMO1 occupies an intermediate network position, connecting HPRT1 with CYRIB. Its established annotation involves regulation of microtubule-based processes, and its HPA single-cell profile is enriched across neural and glial populations while it is detected in both prostate and testis. Although its literature is more limited than that of HPRT1 or ENAH, its bridging position makes it useful for testing whether metabolic and structural signals are coordinated.
- **Conclusion**: Established evidence supports a role for MEMO1 in microtubule-related regulation. Its proposed role as a bridge between metabolic and cytoskeletal components is a hypothesis derived from this module and is not independently validated by STRING or hu.MAP.

#### CYRIB

- **Related proteins** (co-abundance neighbors): MEMO1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CYFIP related Rac1 interactor B. Enables small GTPase binding activity. Involved in several processes, including cellular response to molecule of bacterial origin; negative regulation of small GTPase mediated signal transduction; and regulation of organelle organization. Located in mitochondrion. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: smoking initiation (0.336); bronchial disorder (0.286); mathematical ability (0.270); Alzheimer disease (0.250); rheumatoid arthritis (0.232)
- **Europe PMC papers**: 75
- **Why important**: CYRIB links to MEMO1 and is tissue-enhanced in bone marrow, with single-cell enhancement in microglia and neutrophil-lineage populations. Its established annotations include small-GTPase binding, regulation of actin polymerization, cell migration, and immune-cell activation. Its relatively small literature base makes it less established than the other anchors, but its functional connection to actin and migration gives it mechanistic value.
- **Conclusion**: Established evidence supports CYRIB as a regulator associated with small-GTPase, actin, migration, and immune-cell processes. Its contribution to a shared prostate-testis structural state is plausible but remains a hypothesis, especially given its testis detection and bone-marrow-associated annotation.

## Module 7

**Tissue pair**: prostate and testis  
**Genes (5)**: EPS15L1, EPS15, NSFL1C, ARHGAP17, USP15

### Function

The module is most consistent with an endocytic and vesicle-trafficking program, centered on the EPS15–EPS15L1 pair. Both genes are associated with endocytosis and endosomal transport, and EPS15 is specifically linked to receptor-mediated endocytosis, receptor recycling, and Golgi-to-endosome transport. The supplementary STRING findings support shared ubiquitin-interacting motif and Eps fifteen homology-domain biology (STRING SMART Ubiquitin-interacting motif.; within-query FDR = 0.0122) (STRING SMART Eps15 homology domain; within-query FDR = 0.0152). However, no GO or KEGG term passed global correction, so these annotations are functional interpretation rather than globally significant enrichment. USP15 adds a deubiquitination and TGF-beta or BMP-signaling context, ARHGAP17 adds regulation of Rho-family GTPases and the actin cytoskeleton, and NSFL1C adds vesicle-fusion and ubiquitin-dependent protein-processing context. Together, the evidence suggests coordination between endocytic sorting, cytoskeletal regulation, and protein quality-control or trafficking processes.

**Cell composition.** The module is not composed of secreted or plasma proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and protein detection is present in both prostate and testis for nearly all or all members. The HPA single-cell annotations nevertheless show frequent neutrophil-related signals, with USP15 being tissue-enhanced in bone marrow and immune-cell enhanced in neutrophils. Thus, the shared prostate–testis pattern may reflect a broadly expressed intracellular program, shared cell types, or sample composition rather than a prostate-and-testis-specific biological pathway. The data do not support interpreting it as a plasma-protein module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence direct relationship, EPS15–EPS15L1, while the remaining tested gene pairs lack STRING relationships at the stated threshold. This strongly supports the central pair but indicates that the full module is not already represented as a densely connected STRING network. hu.MAP independently places EPS15 and EPS15L1 together in multiple complexes (hu.MAP huMAP3_05120.1) through (hu.MAP huMAP3_12394.1). These complexes repeatedly contain adaptor-protein, clathrin-associated, endocytic, sorting, and vesicle-trafficking components. The repeated pairwise membership is consistent with a real shared molecular context, whereas USP15, ARHGAP17, and NSFL1C have no reported hu.MAP or STRING support in this fact sheet. Their module connections may therefore reflect co-abundance, indirect functional coupling, or tissue or cell-state effects rather than established physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: EPS15–EPS15L1 (0.99)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Ubiquitin-interacting motif. (FDR = 0.0122, 2 genes); SMART Eps15 homology domain (FDR = 0.0152, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05120.1 (EPS15, EPS15L1; 2/14); huMAP3_06283.1 (EPS15, EPS15L1; 2/19); huMAP3_08540.1 (EPS15, EPS15L1; 2/19); huMAP3_05849.1 (EPS15, EPS15L1; 2/21); huMAP3_09107.1 (EPS15, EPS15L1; 2/23); huMAP3_08320.1 (EPS15, EPS15L1; 2/24); huMAP3_09403.1 (EPS15, EPS15L1; 2/26); huMAP3_10876.1 (EPS15, EPS15L1; 2/40); huMAP3_10762.1 (EPS15, EPS15L1; 2/62); huMAP3_12918.1 (EPS15, EPS15L1; 2/62); huMAP3_12394.1 (EPS15, EPS15L1; 2/98)

### Novelty

The module should not be claimed as an entirely new molecular complex. The EPS15–EPS15L1 relationship is already strongly supported by STRING and is recurrently represented in hu.MAP endocytic complexes. A potentially novel aspect is the co-abundance association of this established endocytic pair with USP15, ARHGAP17, and NSFL1C specifically across prostate and testis. That interpretation remains provisional because the module is small, globally uncorrected GO and KEGG enrichment is absent, and several edges lack support from the reference interaction resources. Absence from STRING or hu.MAP alone does not establish novelty; independent replication and experimental testing would be needed.

**Hypothesis.** Hypothesis: in a shared prostate and testis cellular context, an EPS15–EPS15L1 endocytic scaffold may coordinate receptor internalization and endosomal sorting with ubiquitin-dependent regulation, Rho-family or actin remodeling, and vesicle-membrane recovery. USP15 could modulate the stability or signaling of selected pathway components, ARHGAP17 could tune cytoskeletal changes needed for membrane trafficking, and NSFL1C could connect trafficking to p97-dependent organelle or protein-quality-control processes. This is a mechanistic model, not an established physical assembly: only the EPS15–EPS15L1 relationship and their recurring hu.MAP context are directly supported here.

### Important genes

#### EPS15

- **Related proteins** (co-abundance neighbors): USP15 (0.84), EPS15L1 (0.84), ARHGAP17 (0.82); STRING partners: EPS15L1 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_05120.1, huMAP3_06283.1, huMAP3_08540.1, huMAP3_05849.1, huMAP3_09107.1, huMAP3_08320.1, huMAP3_09403.1, huMAP3_10876.1, huMAP3_10762.1, huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: epidermal growth factor receptor pathway substrate 15. This gene encodes a protein that is part of the EGFR pathway. The protein is present at clatherin-coated pits and is involved in receptor-mediated endocytosis of EGF. Notably, this gene is rearranged with the HRX/ALL/MLL gene in acute myelogeneous leukemias. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, May 2009].
- **Diseases (Open Targets)**: atrial fibrillation (0.399); Abnormality of the skeletal system (0.383); bile duct carcinoma (0.370); esophageal adenocarcinoma (0.370); B-cell acute lymphoblastic leukemia (0.370)
- **Europe PMC papers**: 2810
- **Why important**: EPS15 is the most connected and strongest node in the module, directly linked to EPS15L1 by STRING and present with EPS15L1 in every listed hu.MAP complex (hu.MAP huMAP3_05120.1) through (hu.MAP huMAP3_12394.1). Its established roles in clathrin-coated pits, receptor-mediated endocytosis, receptor recycling, and endosomal transport give the module its clearest functional anchor. It also has the largest literature volume among the module genes and documented disease associations, including leukemia-related rearrangement and several Open Targets disease links.
- **Conclusion**: Established evidence supports EPS15 as the principal endocytic scaffold and network anchor. It is the strongest candidate for organizing the module’s shared vesicle-trafficking signal. A role in the specific prostate–testis co-abundance pattern remains a hypothesis.

#### EPS15L1

- **Related proteins** (co-abundance neighbors): EPS15 (0.84), NSFL1C (0.81); STRING partners: EPS15 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in prostate, testis
- **hu.MAP 3.0**: huMAP3_05120.1, huMAP3_06283.1, huMAP3_08540.1, huMAP3_05849.1, huMAP3_09107.1, huMAP3_08320.1, huMAP3_09403.1, huMAP3_10876.1, huMAP3_10762.1, huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: epidermal growth factor receptor pathway substrate 15 like 1. Enables cadherin binding activity. Predicted to be involved in endocytosis and endosomal transport. Located in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: split hand-foot malformation (0.370); lysosomal storage disease (0.310); neurodegenerative disease (0.310); Alzheimer disease (0.310); Parkinson disease (0.310)
- **Europe PMC papers**: 426
- **Why important**: EPS15L1 is the second member of the high-confidence STRING pair and shares membership with EPS15 across the hu.MAP complexes (hu.MAP huMAP3_05120.1) through (hu.MAP huMAP3_12394.1). Its annotations independently support endocytosis, endosomal transport, synaptic vesicle endocytosis, and cadherin binding. Its vesicular localization and detection in both tissues reinforce its relevance to the module, while its disease links provide potential clinical context despite a smaller literature base than EPS15.
- **Conclusion**: Established evidence supports EPS15L1 as a functional partner or paralogous component of the module’s endocytic core. The data do not demonstrate that it physically binds the other three module members or that it has a tissue-specific role in prostate or testis.

#### USP15

- **Related proteins** (co-abundance neighbors): EPS15 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in prostate, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin specific peptidase 15. This gene encodes a member of the ubiquitin specific protease (USP) family of deubiquitinating enzymes. USP enzymes play critical roles in ubiquitin-dependent processes through polyubiquitin chain disassembly and hydrolysis of ubiquitin-substrate bonds. The encoded protein associates with the COP9 signalosome, and also plays a role in transforming growth factor beta signalling through deubiquitina…
- **Diseases (Open Targets)**: neurodegenerative disease (0.548); alcohol drinking (0.294); post term pregnancy (0.272); smoking initiation (0.217); injury (0.162)
- **Europe PMC papers**: 1872
- **Why important**: USP15 is directly connected to EPS15 in the module and contributes a distinct ubiquitin-regulatory dimension. It encodes a deubiquitinating enzyme associated with the COP nine signalosome and is annotated in TGF-beta, BMP, protein-stability, and protein-deubiquitination processes. Its bone-marrow and neutrophil-enhanced HPA pattern is important for interpreting possible immune-cell or sample-composition effects. It also has substantial literature and disease associations.
- **Conclusion**: Established evidence supports USP15 as a deubiquitination and signaling regulator whose co-abundance may connect endocytic biology with protein stability or signaling. A direct EPS15–USP15 molecular interaction is not established by the supplied STRING or hu.MAP evidence.

#### ARHGAP17

- **Related proteins** (co-abundance neighbors): EPS15 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho GTPase activating protein 17. RICH1 is a GTPase-activating protein (GAP). GAPs stimulate the intrinsic GTP hydrolysis of small G proteins, such as RHOA (MIM 165390), RAC1 (MIM 602048), and CDC42 (MIM 116952).[supplied by OMIM, Apr 2004].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.559); neurodegenerative disease (0.496); atrial fibrillation (0.367); gout (0.321); diabetic neuropathy (0.277)
- **Europe PMC papers**: 527
- **Why important**: ARHGAP17 connects directly to EPS15 and supplies a plausible membrane-cytoskeleton interface. It is a Rho GTPase-activating protein annotated for regulation of Rho-family signaling, Rac signaling, and actin cytoskeleton organization. Its plasma-membrane and cytosolic localization is compatible with trafficking-associated cytoskeletal control, while its detection in testis but not prostate cautions against assuming equal tissue-level protein behavior.
- **Conclusion**: Established evidence supports ARHGAP17 as a regulator of small-GTPase and actin processes that could be relevant to endocytosis. Its proposed role as a functional bridge to EPS15 is a hypothesis based on module co-abundance and compatible annotations, not a demonstrated physical interaction.

#### NSFL1C

- **Related proteins** (co-abundance neighbors): EPS15L1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NSFL1 cofactor. N-ethylmaleimide-sensitive factor (NSF) and valosin-containing protein (p97) are two ATPases known to be involved in transport vesicle/target membrane fusion and fusions between membrane compartments. A trimer of the protein encoded by this gene binds a hexamer of cytosolic p97 and is required for p97-mediated regrowth of Golgi cisternae from mitotic Golgi fragments. Alternative splicing results i…
- **Diseases (Open Targets)**: neurodegenerative disease (0.326); placenta praevia (0.045); adult T-cell leukemia/lymphoma (0.035); pneumonitis (0.027); hypertensive disorder (0.026)
- **Europe PMC papers**: 308
- **Why important**: NSFL1C connects directly to EPS15L1 and provides a mechanistic link to vesicle and organelle handling. It encodes an NSF and p97 cofactor involved in transport-vesicle or target-membrane fusion and p97-mediated Golgi recovery, with additional annotations in ubiquitin-dependent protein catabolism and centrosome-related processes. Its detection in both tissues and its distinct nucleoplasmic localization broaden the module beyond a simple endocytic pit complex.
- **Conclusion**: Established evidence supports NSFL1C as a vesicle-fusion and p97-related trafficking cofactor. Its connection to EPS15L1 may indicate coordinated cellular trafficking or proteostasis, but the supplied resources do not establish a direct physical complex between them.
