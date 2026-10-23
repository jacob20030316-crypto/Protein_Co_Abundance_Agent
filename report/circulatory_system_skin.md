# Conserved co-abundance modules: circulatory_system and skin

## Module 0

**Tissue pair**: circulatory_system and skin  
**Genes (39)**: SLC3A2, ANAPC1, ASCC3, ASNS, ATP2A2, ATXN2, BABAM1, CCDC25, CENPH, CETN2, DCAF1, DCTN5, DDB2, EHD2, ELP3, ERLIN1, FLNC, IRS2, ITSN1, KDM5C, LGALS8, MPHOSPH6, ABCC1, NEK7, NEMF, DLAT, PHC2, RAB3A, UPF2, RICTOR, MRPL40, SMG8, TEX10, GTF2H1, THOC6, TOP2A, TRAF2, TXNL4A, UTP15

### Function

The module does not have a GO or KEGG term passing global multiple-testing correction; therefore, no pathway-level enrichment can be claimed from the primary evidence. Its gene content instead suggests a mixed cellular maintenance program involving membrane trafficking and endocytosis, calcium handling, solute transport, DNA damage surveillance, chromatin regulation, RNA processing, mitochondrial metabolism, and cell-cycle control. The strongest network-level organizing feature is ITSN1, which is connected to many otherwise diverse genes and is annotated as a membrane-associated coordinator of endocytic traffic and actin assembly. Other coherent functional strands include DNA repair centered on DDB2 and GTF2H1, RNA surveillance and ribosome biogenesis involving SMG8, UPF2, UTP15, MPHOSPH6 and TEX10, and membrane or metabolic functions involving ATP2A2, ABCC1, SLC3A2, RICTOR and DLAT. These strands should be interpreted as biological themes suggested by individual annotations and network structure, not as globally significant enrichment.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, while many show cell-type-enhanced expression across diverse epithelial, neuronal, muscle, reproductive and progenitor populations. Protein detection in skin is reported for most module genes, but this does not establish that the module is skin-specific. Blood-cell specificity is generally low, with a smaller subset enhanced or enriched in neutrophils and other immune populations; ITSN1 and RICTOR are among the genes associated with neutrophil or myeloid signals. The module therefore appears broadly cellular rather than a classical plasma-protein signature. Its presence in circulatory-system and skin data could reflect shared resident or contaminating cell types, general cellular state, or coordinated expression of housekeeping and stress-response functions. The broad HPA distribution and absence of a dominant secreted or blood-cell pattern argue against assigning the module exclusively to circulating blood.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING contains a limited set of high-confidence relationships rather than a dense interaction network. Established links include PHC2 with ANAPC1, ASNS with SLC3A2, CETN2 with DDB2 and GTF2H1, DCAF1 with DDB2, DDB2 with GTF2H1, SMG8 with UPF2, and TEX10 with UTP15. These relationships support several real molecular units, especially the DDB2 DNA-repair region, the SMG8-UPF2 nonsense-mediated-decay pair, and the UTP15-TEX10 ribosome-biogenesis pair, but they do not demonstrate that all module genes form one physical complex. hu.MAP provides additional complex support: NEK7 and EHD2 co-occur in C1; UTP15 and MPHOSPH6 in the ribosome-biogenesis complex C2; DDB2 and DCAF1 in the ubiquitin-ligase and DNA-repair complex C3; and ATP2A2 with ABCC1 in the membrane and organelle-associated complexes C4 and C5. Most module members are not represented in a shared hu.MAP complex, so the module is better viewed as a co-abundance program with several embedded known molecular relationships than as a single established biochemical complex.

**STRING interactions (score >= 0.7)**: 8 of 741 gene pairs: ANAPC1–PHC2 (0.9); ASNS–SLC3A2 (0.767); CETN2–DDB2 (0.917); CETN2–GTF2H1 (0.837); DCAF1–DDB2 (0.967); DDB2–GTF2H1 (0.709); SMG8–UPF2 (0.983); TEX10–UTP15 (0.757)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07274.1 (NEK7, EHD2; 2/2); huMAP3_14264.1 (UTP15, MPHOSPH6; 2/20); huMAP3_09779.1 (DDB2, DCAF1; 2/44); huMAP3_06247.1 (ATP2A2, ABCC1; 2/65); huMAP3_09592.1 (ATP2A2, ABCC1; 2/95)

### Novelty

The module may be a new cross-tissue co-abundance observation, but the available evidence is insufficient to call it a new biological pathway or newly discovered interaction network. Its limited STRING connectivity and the presence of several hu.MAP-supported subcomplexes show that parts of the signal recapitulate known biology. Conversely, the overall combination of endocytic trafficking, skin-relevant calcium handling, DNA repair, RNA quality control, ribosome biogenesis and cell-cycle genes is not identified as one established complex in the supplied resources. Absence of a STRING or hu.MAP relationship is not evidence of novelty, particularly because co-abundance can arise from shared cell composition, regulation, or technical and sampling effects. A defensible conclusion is that the cross-tissue module-level association is potentially novel and hypothesis-generating, but requires replication, cell-type adjustment, independent cohorts, and perturbation or interaction experiments before being considered a new mechanism.

**Hypothesis.** Hypothesis: the shared module reflects a broadly expressed tissue-maintenance state in which membrane trafficking and calcium or solute handling are coordinated with genome-protection and RNA-quality-control systems. In skin, ATP2A2 could connect calcium homeostasis and epidermal biology with the membrane-associated portion of the module, while ABCC1 and SLC3A2 could support transport and cellular stress handling. ITSN1 may organize endocytic and actin-linked trafficking signals. Concurrent expression of DDB2, GTF2H1, BABAM1 and related factors could represent protection from environmental or replication-associated DNA damage, while SMG8, UPF2, UTP15 and MPHOSPH6 could maintain transcript surveillance and ribosome production. RICTOR and IRS2 may provide a growth or nutrient-signaling interface. This is a mechanistic proposal, not an established causal model; alternative explanations include shared cell-type composition, especially contributions from skin epithelial, muscle, progenitor or myeloid populations.

### Important genes

#### ITSN1

- **Related proteins** (co-abundance neighbors): MPHOSPH6 (0.92), THOC6 (0.88), SMG8 (0.85), BABAM1 (0.85), TXNL4A (0.85), TEX10 (0.85), RICTOR (0.84), UPF2 (0.84), KDM5C (0.84), DCAF1 (0.83), DDB2 (0.83), TOP2A (0.83), ELP3 (0.83), ASCC3 (0.83), NEMF (0.82), MRPL40 (0.82), ANAPC1 (0.81), DCTN5 (0.81), TRAF2 (0.81), CETN2 (0.81), NEK7 (0.80), DLAT (0.80), ASNS (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: intersectin 1. The protein encoded by this gene is a cytoplasmic membrane-associated protein that indirectly coordinates endocytic membrane traffic with the actin assembly machinery. In addition, the encoded protein may regulate the formation of clathrin-coated vesicles and could be involved in synaptic vesicle recycling. This protein has been shown to interact with dynamin, CDC42, SNAP23, SNAP25, SPIN90, EPS15,…
- **Diseases (Open Targets)**: hereditary disease (0.531); neurodevelopmental disorder (0.451); Autistic behavior (0.404); Intellectual disability (0.378); autosomal dominant non-syndromic intellectual disability (0.371)
- **Europe PMC papers**: 1094
- **Why important**: ITSN1 is the central network connector in the supplied subgraph, linking membrane trafficking-related genes with DNA repair, RNA surveillance, ribosome biogenesis, signaling and metabolism. Its annotation supports a role in endocytic membrane traffic and actin assembly, and HPA places it at the plasma membrane with expression in several cell types, including macrophage and myeloid-associated populations. It also has substantial literature support and disease associations involving neurodevelopmental phenotypes.
- **Conclusion**: Established evidence supports ITSN1 as the principal network organizer and a membrane-trafficking protein. It is plausible that ITSN1 helps connect otherwise heterogeneous cellular programs, but the co-abundance data do not establish that it physically regulates all linked genes or drives the cross-tissue module.

#### DDB2

- **Related proteins** (co-abundance neighbors): ITSN1 (0.83), FLNC (0.82); STRING partners: CETN2 (0.917), DCAF1 (0.967), GTF2H1 (0.709)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cell Junctions; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_09779.1
- **Function (MyGene.info)**: damage specific DNA binding protein 2. This gene encodes a protein that is necessary for the repair of ultraviolet light-damaged DNA. This protein is the smaller subunit of a heterodimeric protein complex that participates in nucleotide excision repair, and this complex mediates the ubiquitylation of histones H3 and H4, which facilitates the cellular response to DNA damage. This subunit appears to be required for DNA binding. Mutations…
- **Diseases (Open Targets)**: xeroderma pigmentosum group E (0.773); xeroderma pigmentosum (0.515); prostate carcinoma (0.388); skin basal cell carcinoma (0.370); ovarian endometrioid adenocarcinoma with squamous differentiation (0.370)
- **Europe PMC papers**: 3149
- **Why important**: DDB2 is a network-linked DNA-repair gene with direct STRING relationships to CETN2, DCAF1 and GTF2H1 and hu.MAP support with DCAF1 in a larger ubiquitin-ligase and DNA-repair complex. It is annotated for nucleotide-excision repair, ultraviolet response and DNA damage response, has skin detection in HPA, and is strongly associated with xeroderma pigmentosum group E and skin basal cell carcinoma-related disease evidence. This makes it especially relevant to a module shared with skin.
- **Conclusion**: Established evidence supports DDB2 as a biologically meaningful skin-relevant DNA-damage-response component. It may mark protection from ultraviolet or replication-associated damage in the module, but the data do not show that ultraviolet exposure caused the module or that DDB2 controls its other functional branches.

#### ATP2A2

- **Related proteins** (co-abundance neighbors): PHC2 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_06247.1, huMAP3_09592.1
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darie…
- **Diseases (Open Targets)**: Darier disease (0.823); acrokeratosis verruciformis (0.663); neurodegenerative disease (0.507); hereditary disease (0.416); schizophrenia (0.406)
- **Europe PMC papers**: 9327
- **Why important**: ATP2A2 encodes a calcium pump involved in intracellular calcium homeostasis, epidermis development and muscle calcium handling. It is linked to PHC2 in the co-abundance network and occurs with ABCC1 in two hu.MAP complexes. HPA reports group-enriched expression in heart muscle, skeletal muscle and tongue and detection in skin. Its disease associations include Darier disease and acrokeratosis verruciformis, making it a strong bridge between skin biology, calcium regulation and tissue physiology.
- **Conclusion**: Established evidence supports ATP2A2 as a skin- and muscle-relevant calcium-homeostasis gene embedded in known membrane-associated complexes. A plausible interpretation is that calcium handling contributes to the shared module, but the module does not prove a direct ATP2A2-mediated connection to the nuclear and RNA-processing genes.

#### ABCC1

- **Related proteins** (co-abundance neighbors): ANAPC1 (0.86), TOP2A (0.86), KDM5C (0.83), GTF2H1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_06247.1, huMAP3_09592.1
- **Function (MyGene.info)**: ATP binding cassette subfamily C member 1 (ABCC1 blood group). The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra-and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This full transporter is a member of the MRP subfamily which is involved in multi-drug resistance. This pro…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.514); hearing loss, autosomal dominant 77 (0.499); hereditary breast carcinoma (0.475); autosomal dominant nonsyndromic hearing loss (0.407); ischemic stroke (0.314)
- **Europe PMC papers**: 8207
- **Why important**: ABCC1 is a plasma-membrane multispecific organic-anion transporter associated with xenobiotic handling, oxidative stress and leukotriene metabolism. It connects in the module to ANAPC1, TOP2A, KDM5C and GTF2H1, and is represented with ATP2A2 in hu.MAP complexes. HPA shows skin detection and broad tissue specificity, while disease associations include hereditary breast carcinoma, hearing loss and ischemic stroke-related evidence. Its literature volume is substantial.
- **Conclusion**: Established evidence supports ABCC1 as a membrane transport and cellular-stress component that could be relevant to skin exposure and tissue protection. Its network links may reflect coordinated cellular state rather than a single transporter-centered pathway, so a causal role in the module remains hypothetical.

#### RICTOR

- **Related proteins** (co-abundance neighbors): ITSN1 (0.84), IRS2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RPTOR independent companion of MTOR complex 2. RICTOR and MTOR (FRAP1; MIM 601231) are components of a protein complex that integrates nutrient- and growth factor-derived signals to regulate cell growth (Sarbassov et al., 2004 [PubMed 15268862]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: lung carcinoma (0.418); dengue disease (0.372); cutaneous melanoma (0.371); kidney neoplasm (0.371); colorectal adenocarcinoma (0.371)
- **Europe PMC papers**: 8609
- **Why important**: RICTOR is a component of the mTOR complex two signaling system and is annotated for growth regulation, cytoskeletal organization, lipid biosynthesis and endothelial-cell proliferation. It connects ITSN1 with IRS2, providing a plausible signaling bridge between membrane trafficking and insulin or cytokine-responsive growth pathways. HPA reports skin detection and immune-cell enhancement in neutrophils, and the gene has disease associations spanning vascular, metabolic and neoplastic conditions.
- **Conclusion**: Established evidence supports RICTOR as a signaling and cytoskeletal regulator with relevance to growth and immune-associated cell states. It is a reasonable candidate for linking cell-surface trafficking to metabolic or growth control in the module, but the co-abundance pattern does not establish mTOR complex activity or endothelial causality.

## Module 1

**Tissue pair**: circulatory_system and skin  
**Genes (44)**: ABHD6, AGPS, FDXR, MTHFD1L, CUX1, CLPB, DERPC, EMC1, FASTKD1, GNAI3, SLC2A1, HACL2, HEXA, HMOX1, HSDL2, IKBKB, PRKACB, KHDRBS3, MED7, NDUFAF4, NFU1, NIT2, OAT, PIK3R2, PCLAF, PCYT2, RASA3, MRPL4, MRPL42, RO60, RPP38, SCAMP2, SNUPN, EARS2, TIMMDC1, TMEM222, TMX1, LCMT2, UBE4A, UQCC1, UXS1, VPS11, VPS18, ZWINT

### Function

No GO/KEGG term passed global correction, and STRING reported no supplementary functional enrichment. The module therefore does not support a single confidently assigned pathway. Its genes instead suggest a composite cellular maintenance program involving mitochondrial RNA handling, mitochondrial translation and respiratory-chain assembly, vesicle and endolysosomal trafficking, lipid metabolism, RNA processing, transcriptional regulation, cell-cycle control, and signal transduction. The strongest functional interpretation is a coordinated cellular state involving organelle quality control, energy metabolism, membrane trafficking, and stress or inflammatory responsiveness rather than a discrete pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a small secreted component, while most genes are intracellular or membrane-associated. Most genes have low tissue specificity and low immune-cell specificity, arguing against a strongly blood-cell-enriched module and against a simple plasma protein signature. Protein detection is broadly reported in skin, whereas the circulatory-system comparison has no matching HPA tissue result. The HPA single-cell annotations are heterogeneous, including epithelial, stromal, neural, reproductive, myeloid, and vascular-associated cell types. Thus, shared cell composition, broadly expressed housekeeping-like programs, or a common organelle and stress state could contribute to the apparent cross-tissue conservation. The lymphoid and monocyte-associated annotations of HMOX1 and the marrow or lymphoid annotations of ZWINT and PCLAF are compatible with some immune or proliferative contribution, but do not establish that the whole module is blood-cell derived.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited but biologically coherent set of pairwise relationships. Known mitochondrial or organelle-related links include EARS2 with MRPL4, MRPL4 with MRPL42, and NDUFAF4 with TIMMDC1. The VPS11–VPS18 relationship supports a vesicle-trafficking complex, while GNAI3 links to PIK3R2 and PRKACB support signaling connections. PCLAF–ZWINT supports a cell-cycle or kinetochore-associated connection. These relationships are consistent with genuine substructure, but they cover only a minority of possible within-module pairs and do not demonstrate a single unified complex. hu.MAP independently places RO60 and EARS2 in several shared complexes, VPS11 and VPS18 together in multiple CORVET or HOPS-related complexes (hu.MAP huMAP3_08749.1), (hu.MAP huMAP3_13822.1), (hu.MAP huMAP3_12433.1), and (hu.MAP huMAP3_12945.1), MRPL4 and MRPL42 together in several mitochondrial ribosome-related complexes (hu.MAP huMAP3_00983.1) through (hu.MAP huMAP3_06589.1), and FDXR with MTHFD1L in mitochondrial metabolic complexes (hu.MAP huMAP3_10525.1), (hu.MAP huMAP3_13468.1). The repeated hu.MAP support for these pairs indicates that parts of the module recapitulate known molecular machinery. The partial membership of each complex, especially in the large mitochondrial complexes, argues for shared cellular context or coordinated abundance rather than recovery of a complete complex.

**STRING interactions (score >= 0.7)**: 7 of 946 gene pairs: EARS2–MRPL4 (0.717); GNAI3–PIK3R2 (0.9); GNAI3–PRKACB (0.733); MRPL4–MRPL42 (0.956); NDUFAF4–TIMMDC1 (0.999); PCLAF–ZWINT (0.913); VPS11–VPS18 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11084.1 (RO60, FASTKD1, EARS2; 3/27); huMAP3_06970.1 (RO60, EARS2; 2/8); huMAP3_08749.1 (VPS11, VPS18; 2/9); huMAP3_13822.1 (VPS11, VPS18; 2/9); huMAP3_12433.1 (VPS11, VPS18; 2/11); huMAP3_09371.1 (RO60, FASTKD1; 2/12); huMAP3_12945.1 (VPS11, VPS18; 2/12); huMAP3_00983.1 (MRPL4, MRPL42; 2/22); huMAP3_10525.1 (FDXR, MTHFD1L; 2/33); huMAP3_06439.1 (MRPL4, MRPL42; 2/57); huMAP3_06550.1 (MRPL4, MRPL42; 2/62); huMAP3_07939.1 (MRPL4, MRPL42; 2/68); huMAP3_08458.1 (MRPL4, MRPL42; 2/70); huMAP3_09113.1 (MRPL4, MRPL42; 2/72); huMAP3_09483.1 (MRPL4, MRPL42; 2/74); huMAP3_06589.1 (MRPL4, MRPL42; 2/79); huMAP3_13468.1 (FDXR, MTHFD1L; 2/99)

### Novelty

This cannot be claimed as a wholly new molecular interaction module. Several component relationships and complex memberships are already represented by STRING and hu.MAP, particularly the VPS11–VPS18, MRPL4–MRPL42, EARS2–MRPL4, and NDUFAF4–TIMMDC1 relationships. At the same time, the specific cross-tissue co-abundance configuration is not directly established by those resources, and the available evidence does not show that this entire gene set has previously been described as a conserved circulatory-system and skin module. The appropriate claim is therefore a potentially novel tissue-pair co-abundance pattern built partly from known molecular machinery, requiring replication in independent cohorts and testing against cell-composition and technical confounding before being considered a new biological mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared organelle-maintenance and stress-adaptation state in cells represented in both circulatory-system and skin samples. Mitochondrial translation and respiratory-chain assembly genes may support energy production, while VPS11 and VPS18 may maintain endolysosomal trafficking and organelle turnover. ABHD6, AGPS, and related lipid-handling genes could connect membrane lipid remodeling with vesicle function. HMOX1, RO60, IKBKB, and the GNAI3-linked signaling neighborhood could couple oxidative or inflammatory stress to transcriptional and trafficking responses. This is a mechanistic hypothesis, not an enrichment result; the absence of globally significant GO/KEGG terms means that it should be tested experimentally rather than treated as established module function.

### Important genes

#### HMOX1

- **Related proteins** (co-abundance neighbors): NFU1 (0.83), HSDL2 (0.82), CUX1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location Golgi apparatus, Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heme oxygenase 1. Heme oxygenase, an essential enzyme in heme catabolism, cleaves heme to form biliverdin, which is subsequently converted to bilirubin by biliverdin reductase, and carbon monoxide, a putative neurotransmitter. Heme oxygenase activity is induced by its substrate heme and by various nonheme substances. Heme oxygenase occurs as 2 isozymes, an inducible heme oxygenase-1 and a constitutive heme oxygenas…
- **Diseases (Open Targets)**: heme oxygenase 1 deficiency (0.686); amyloidosis (0.465); neurodegenerative disease (0.459); cystic fibrosis (0.392); chronic obstructive pulmonary disease (0.360)
- **Europe PMC papers**: 38190
- **Why important**: HMOX1 is a biologically informative stress and inflammatory node. It has a direct neighborhood connection to NFU1 and HSDL2, is tissue-enriched in lymphoid tissue, and is associated with monocyte and macrophage cell types in HPA. Its annotation includes heme oxidation, wound healing in inflammatory response, endothelial proliferation, and regulation of leukocyte migration. It also has exceptionally extensive literature and disease linkage, making it a strong interpretive anchor even though its module degree is modest.
- **Conclusion**: Established evidence supports HMOX1 as an inducible heme-catabolism and stress-response gene with immune and vascular relevance. Its presence is compatible with an inflammatory or oxidative-stress component, but does not prove that this is the principal driver of the module or that the module originates from monocytes.

#### VPS11

- **Related proteins** (co-abundance neighbors): VPS18 (0.86), KHDRBS3 (0.82); STRING partners: VPS18 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_08749.1, huMAP3_13822.1, huMAP3_12433.1, huMAP3_12945.1
- **Function (MyGene.info)**: VPS11 core subunit of CORVET and HOPS complexes. Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene encodes the human homolog of yeast class C Vps11 protein. The mammalian class C Vps proteins are predominantly associated with late…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 12 (0.723); neurodegenerative disease (0.527); POLR-related leukodystrophy (0.527); dystonia 32 (0.410); VPS11-related neurological disorder (0.370)
- **Europe PMC papers**: 849
- **Why important**: VPS11 is a direct network partner of VPS18 and is present with VPS18 in several hu.MAP complexes (hu.MAP huMAP3_08749.1), (hu.MAP huMAP3_13822.1), (hu.MAP huMAP3_12433.1), and (hu.MAP huMAP3_12945.1). It is a core subunit of CORVET and HOPS complexes and is annotated for intracellular protein transport, endosome organization, lysosome organization, and endosome-to-lysosome transport. Its disease associations include VPS11-related neurological disorders and leukodystrophy, and it has a substantial literature base.
- **Conclusion**: Established evidence identifies VPS11 as a vesicle-trafficking and endolysosomal machinery component, with strong support from both STRING and hu.MAP. It is a plausible structural indicator of the module's organelle-trafficking arm, whereas any role in coordinating the other module neighborhoods remains a hypothesis.

#### NDUFAF4

- **Related proteins** (co-abundance neighbors): MED7 (0.83), TMEM222 (0.82), TIMMDC1 (0.80); STRING partners: TIMMDC1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase complex assembly factor 4. NADH:ubiquinone oxidoreductase (complex I) catalyzes the transfer of electrons from NADH to ubiquinone (coenzyme Q) in the first step of the mitochondrial respiratory chain, resulting in the translocation of protons across the inner mitochondrial membrane. This gene encodes a complex I assembly factor. Mutations in this gene are a cause of mitochondrial complex I deficiency. [provided by RefSeq, O…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.714); type 2 diabetes mellitus (0.607); mitochondrial disease (0.597); diabetes mellitus (0.578); mitochondrial complex I deficiency, nuclear type 15 (0.568)
- **Europe PMC papers**: 378
- **Why important**: NDUFAF4 connects the higher-degree neighborhood around MED7 and TMEM222 to TIMMDC1, with the latter relationship strongly supported by STRING. Both genes are mitochondrial, and NDUFAF4 is annotated as a complex I assembly factor whose mutations cause mitochondrial complex I deficiency. It has meaningful disease evidence involving mitochondrial deficiency and metabolic disease, together with a substantial literature base.
- **Conclusion**: Established evidence supports NDUFAF4 as a mitochondrial respiratory-chain assembly factor and supports a genuine NDUFAF4–TIMMDC1 subnetwork. Its participation is consistent with mitochondrial maintenance within the module, but it does not establish that respiratory-chain biology explains the entire module.

#### FASTKD1

- **Related proteins** (co-abundance neighbors): CLPB (0.88), EARS2 (0.85), HSDL2 (0.84), SCAMP2 (0.84), MTHFD1L (0.84), NFU1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_11084.1, huMAP3_09371.1
- **Function (MyGene.info)**: FASTK mitochondrial RNA regulator 1. Enables RNA binding activity. Involved in mitochondrial RNA metabolic process and regulation of mitochondrial mRNA stability. Located in mitochondrion. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: secondary hypertrophic osteoarthropathy (0.190); stroke disorder (0.164); alcohol drinking (0.164); myocardial infarction (0.036); diabetes mellitus (0.036)
- **Europe PMC papers**: 155
- **Why important**: FASTKD1 has one of the strongest network positions in the module and connects mitochondrial or metabolic genes including EARS2, MTHFD1L, NFU1, and HSDL2, as well as SCAMP2 and CLPB. It is localized to mitochondria and is annotated for mitochondrial RNA metabolism, RNA processing, and regulation of mitochondrial mRNA stability. Its disease associations include stroke disorder and myocardial infarction, and it has a moderate literature base.
- **Conclusion**: Established evidence supports FASTKD1 as a mitochondrial RNA-regulatory component and as a useful bridge between several mitochondrial and cellular-maintenance neighborhoods. Its centrality makes it a plausible organizing marker, but the proposed bridging role is inferential because the module lacks globally significant pathway enrichment.

#### ABHD6

- **Related proteins** (co-abundance neighbors): AGPS (0.86), EARS2 (0.84), RO60 (0.83), HACL2 (0.83), HEXA (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: abhydrolase domain containing 6, acylglycerol lipase. Enables acylglycerol lipase activity. Involved in acylglycerol catabolic process. Predicted to be located in late endosome membrane and lysosomal membrane. Predicted to be integral component of membrane. Predicted to be part of AMPA glutamate receptor complex. Predicted to be active in GABA-ergic synapse; glutamatergic synapse; and mitochondrion. Predicted to be integral component of postsynaptic …
- **Diseases (Open Targets)**: Alzheimer disease (0.362); neurodegenerative disease (0.358); lysosomal storage disease (0.357); Parkinson disease (0.357); acquired polycythemia vera (0.142)
- **Europe PMC papers**: 911
- **Why important**: ABHD6 has a relatively central position and links AGPS, EARS2, RO60, HACL2, and HEXA. It is annotated as an acylglycerol lipase involved in acylglycerol and phospholipid-related metabolism, with predicted localization to late endosome and lysosomal membranes. It is tissue-enhanced in liver, appears across several cell types, and has extensive literature with disease associations spanning neurodegenerative and lysosomal disorders.
- **Conclusion**: Established evidence supports ABHD6 as a membrane-associated lipid-metabolism enzyme with plausible endolysosomal relevance. It could connect lipid remodeling to trafficking and mitochondrial state, but that integrative role is a hypothesis rather than a demonstrated function of this module.

## Module 2

**Tissue pair**: circulatory_system and skin  
**Genes (41)**: ABT1, APC, ARID1B, CC2D1B, CLASP1, COG2, DMXL1, GNL1, HECTD3, HMGN5, LACTB, LGMN, MAIP1, MAD1L1, MICAL3, NBN, NCOR1, NDC80, NIPBL, NUP54, OSBPL1A, OSBPL3, MOB4, PPP1R3D, PRRC2C, CHM, RBM15, REPS1, SCRIB, SPART, WARS2, TACC1, TBC1D5, ZFP36L2, TMF1, TP53BP1, TRAPPC12, UBAC2, USP24, USP8, UNK

### Function

No GO or KEGG term passed global correction, and STRING reported no functional enrichment. The module therefore does not support a single statistically established pathway label. Its annotated genes instead suggest a heterogeneous intracellular regulatory program involving chromatin and transcriptional control, DNA-damage surveillance and repair, vesicle and endosomal trafficking, cytoskeletal organization, cell-cycle control, lipid handling, and protein ubiquitination. The network is centered on the poorly characterized hub UNK, with additional connections linking chromatin regulators, trafficking proteins, and structural or signaling proteins. This pattern is more consistent with a shared cellular-state or regulatory module than with a narrowly defined biochemical pathway. The absence of globally significant enrichment does not invalidate the module, but it substantially limits functional specificity.

**Cell composition.** The module is not dominated by plasma or secreted proteins: HPA identifies only one secreted gene, and most proteins are intracellular or membrane-associated. Most genes have low tissue specificity, while many show cell-type enhancement rather than strong tissue restriction. HPA shows frequent associations with neutrophils and additional associations with basophils, NK cells, plasmacytoid dendritic cells, eosinophils, and other immune or progenitor populations. This raises the possibility that the circulatory-system and skin signal partly reflects shared blood-cell or infiltrating-cell composition, although the overall HPA profile does not indicate strong immune-cell specificity for most genes. Skin protein detection is broad across the module, whereas circulatory-system protein evidence is unavailable in the supplied HPA summary. The module should therefore be interpreted as a largely intracellular, broadly expressed program that may be influenced by shared cell types and sample composition rather than as a skin-specific secretory program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides direct high-confidence support for the NBN–TP53BP1 relationship and for the NCOR1–RBM15 relationship. These are established database relationships and connect DNA-damage response with transcriptional or RNA-regulatory functions, but they represent isolated links rather than a densely interconnected STRING network. hu.MAP provides partial-complex support for CC2D1B with USP24 in (hu.MAP huMAP3_04438.1) and (hu.MAP huMAP3_14320.1), and for USP8 with MICAL3 in (hu.MAP huMAP3_13310.1). The remaining complex members are outside the module, so these findings support membership in or proximity to known complexes rather than a complete module-wide physical complex. Most co-abundance edges lack corresponding STRING or hu.MAP support, indicating that the network captures coordinated abundance relationships beyond currently catalogued physical interactions, or relationships that may be indirect, context-dependent, or technically underrepresented.

**STRING interactions (score >= 0.7)**: 2 of 820 gene pairs: NBN–TP53BP1 (0.923); NCOR1–RBM15 (0.739)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04438.1 (CC2D1B, USP24; 2/3); huMAP3_14320.1 (CC2D1B, USP24; 2/4); huMAP3_13310.1 (USP8, MICAL3; 2/11)

### Novelty

This module should not be claimed as a newly discovered biological mechanism. Its shared co-abundance pattern is not reproduced as a densely known interaction network in STRING or hu.MAP, but absence from those resources does not establish novelty. Several component functions and relationships are already well established, including DNA-damage signaling involving NBN and TP53BP1, transcriptional regulation involving ARID1B, NIPBL, and NCOR1, endosomal regulation involving REPS1 and USP8, and cytoskeletal or adhesion functions involving APC and related proteins. The potentially novel aspect is the cross-tissue co-abundance organization of these otherwise heterogeneous genes. Establishing genuine novelty would require independent cohorts, cell-composition adjustment, replication across skin and circulatory samples, and experimental testing of whether the observed co-abundance relationships are mechanistically coupled.

**Hypothesis.** Hypothesis: the module reflects a shared cell-state program linking nuclear integrity and transcriptional regulation to membrane trafficking and cytoskeletal remodeling in cells represented in both skin and circulatory-system samples. In this model, chromatin and DNA-damage regulators such as ARID1B, NIPBL, NBN, and TP53BP1 coordinate cellular stress or proliferative state, while REPS1, APC, USP24, and trafficking-related genes couple that state to endosomal, membrane, and cytoskeletal behavior. The HPA cell-type pattern suggests that variation in myeloid or other shared cell populations could generate part of the signal. This remains a hypothesis because global GO/KEGG enrichment is absent, STRING support is sparse, and most module edges are not established physical interactions.

### Important genes

#### UNK

- **Related proteins** (co-abundance neighbors): REPS1 (0.87), TMF1 (0.87), PRRC2C (0.87), USP24 (0.86), CC2D1B (0.86), TRAPPC12 (0.84), TBC1D5 (0.83), TP53BP1 (0.83), SPART (0.83), GNL1 (0.83), HECTD3 (0.83), USP8 (0.83), RBM15 (0.83), NUP54 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol, Cytoplasmic bodies; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: unk zinc finger. Enables mRNA CDS binding activity. Involved in cell morphogenesis involved in neuron differentiation and negative regulation of cytoplasmic translation. Part of polysome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Hypercholesterolemia (0.136); coronary atherosclerosis (0.082); Alzheimer disease (0.080); erythrocytosis, familial, 6 (0.034); primary familial polycythemia due to EPO receptor mutation (0.034)
- **Europe PMC papers**: 4440
- **Why important**: UNK is the principal topological hub and connects genes spanning translation control, vesicle and membrane trafficking, DNA-damage response, and regulatory processes. Its HPA profile is broadly expressed with skin detection but no immune-cell detection, while the supplied annotation links it to mRNA CDS binding, neuronal morphogenesis, and negative regulation of cytoplasmic translation. Its high network centrality makes it important for explaining the module, even though its molecular function remains poorly characterized.
- **Conclusion**: Established evidence supports UNK as a central co-abundance organizer with an annotation related to RNA and translation regulation. It is not established that UNK mechanistically coordinates the other module processes. A testable hypothesis is that UNK links cytoplasmic translational control with trafficking or stress-responsive cellular states.

#### ARID1B

- **Related proteins** (co-abundance neighbors): NCOR1 (0.90), NIPBL (0.88), MOB4 (0.84), HECTD3 (0.83), MAD1L1 (0.82), REPS1 (0.81), COG2 (0.81), MAIP1 (0.81), SPART (0.80), WARS2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: AT-rich interaction domain 1B. This locus encodes an AT-rich DNA interacting domain-containing protein. The encoded protein is a component of the SWI/SNF chromatin remodeling complex and may play a role in cell-cycle activation. The protein encoded by this locus is similar to AT-rich interactive domain-containing protein 1A. These two proteins function as alternative, mutually exclusive ARID-subunits of the SWI/SNF complex. The…
- **Diseases (Open Targets)**: Coffin-Siris syndrome (0.778); Coffin-Siris syndrome 1 (0.778); hereditary disease (0.557); arid1b-related disorder (0.536); Intellectual disability (0.533)
- **Europe PMC papers**: 4099
- **Why important**: ARID1B is a highly connected module member and encodes a SWI/SNF chromatin-remodeling component. Its annotations include transcriptional regulation, cell differentiation, and mitotic transition, and it is associated with Coffin-Siris syndrome and intellectual disability. Its network links to NIPBL, NCOR1, HECTD3, and cell-cycle-related genes, placing it at a plausible regulatory interface between chromatin state and cellular proliferation.
- **Conclusion**: Established evidence supports ARID1B as a chromatin and transcriptional regulator with strong disease relevance. Its co-abundance with trafficking, cytoskeletal, and damage-response genes does not prove direct coordination. A plausible hypothesis is that shared chromatin or proliferation state drives part of the cross-tissue module.

#### NIPBL

- **Related proteins** (co-abundance neighbors): ARID1B (0.88), NCOR1 (0.85), ABT1 (0.85), NBN (0.81), REPS1 (0.81), ZFP36L2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NIPBL cohesin loading factor. This gene encodes the homolog of the Drosophila melanogaster Nipped-B gene product and fungal Scc2-type sister chromatid cohesion proteins. The Drosophila protein facilitates enhancer-promoter communication of remote enhancers and plays a role in developmental regulation. It is also homologous to a family of chromosomal adherins with broad roles in sister chromatid cohesion, chromosome condensatio…
- **Diseases (Open Targets)**: Cornelia de Lange syndrome (0.864); hereditary disease (0.544); Dislocated radial head (0.462); Intellectual disability (0.384); low grade glioma (0.370)
- **Europe PMC papers**: 2494
- **Why important**: NIPBL is connected to ARID1B, NCOR1, NBN, and regulatory genes in the module. It is a cohesin-loading factor involved in sister-chromatid cohesion, enhancer-promoter communication, chromatin remodeling, development, and DNA repair. Its association with Cornelia de Lange syndrome and its HPA enhancement in neutrophils make it relevant both to nuclear regulation and to possible cell-composition effects.
- **Conclusion**: Established evidence supports NIPBL as a chromatin-organization and genome-maintenance factor with developmental and disease importance. The module does not establish that NIPBL is the cause of the shared tissue signal. A hypothesis is that NIPBL marks a coordinated chromatin and cell-state program that becomes correlated with stress or immune-cell abundance.

#### APC

- **Related proteins** (co-abundance neighbors): MICAL3 (0.83), CLASP1 (0.83), OSBPL3 (0.81), SCRIB (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: APC regulator of Wnt signaling pathway. This gene encodes a tumor suppressor protein that acts as an antagonist of the Wnt signaling pathway. It is also involved in other processes including cell migration and adhesion, transcriptional activation, and apoptosis. Defects in this gene cause familial adenomatous polyposis (FAP), an autosomal dominant pre-malignant disease that usually progresses to malignancy. Mutations in the APC gene hav…
- **Diseases (Open Targets)**: familial adenomatous polyposis 1 (0.847); classic familial adenomatous polyposis (0.797); colorectal cancer (0.791); gastric adenocarcinoma and proximal polyposis of the stomach (0.765); colon carcinoma (0.733)
- **Europe PMC papers**: 201480
- **Why important**: APC is a structurally informative module member connected to MICAL3, CLASP1, OSBPL3, and SCRIB. It regulates Wnt signaling, cell migration, adhesion, apoptosis, microtubule behavior, and cell fate, and is strongly associated with familial adenomatous polyposis and colorectal cancer. Its position connects signaling, adhesion, cytoskeletal organization, and lipid-related membrane processes.
- **Conclusion**: Established evidence supports APC as a major regulator of Wnt signaling, cytoskeletal organization, adhesion, and tumor suppression. The co-abundance relationship with the module’s nuclear and trafficking genes is not sufficient to infer a common APC-controlled pathway. A hypothesis is that APC contributes to a shared epithelial or vascular structural state that is also reflected in skin and blood-associated cell populations.

#### NBN

- **Related proteins** (co-abundance neighbors): CHM (0.86), NIPBL (0.81); STRING partners: TP53BP1 (0.923)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nibrin. Mutations in this gene are associated with Nijmegen breakage syndrome, an autosomal recessive chromosomal instability syndrome characterized by microcephaly, growth retardation, immunodeficiency, and cancer predisposition. The encoded protein is a member of the MRE11/RAD50 double-strand break repair complex which consists of 5 proteins. This gene product is thought to be involved in DNA double-str…
- **Diseases (Open Targets)**: Nijmegen breakage syndrome (0.822); aplastic anemia (0.720); acute lymphoblastic leukemia (0.676); breast cancer (0.611); hereditary neoplastic syndrome (0.577)
- **Europe PMC papers**: 5207
- **Why important**: NBN participates in the MRE11/RAD50 DNA-repair complex and in checkpoint activation. It has a direct high-confidence STRING relationship with TP53BP1 and is connected in the module to NIPBL and CHM. Its association with Nijmegen breakage syndrome, immunodeficiency, chromosomal instability, and cancer predisposition gives it strong disease and mechanistic importance.
- **Conclusion**: Established evidence supports NBN as a DNA double-strand-break repair and checkpoint factor, with an independently catalogued relationship to TP53BP1. The module does not establish that DNA damage is the primary driver of the cross-tissue co-abundance pattern. A hypothesis is that cellular stress or proliferative turnover contributes to coordinated abundance of the DNA-repair branch.

#### REPS1

- **Related proteins** (co-abundance neighbors): UNK (0.87), ARID1B (0.81), NIPBL (0.81), USP24 (0.80), UBAC2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RALBP1 associated Eps domain containing 1. This gene encodes a signaling adaptor protein with two EH domains that interacts with proteins that participate in signaling, endocytosis and cytoskeletal changes. The encoded protein has been found in association with intersectin 1 and Src homology 3-domain growth factor receptor-bound 2-like (endophilin) interacting protein 1 when intersectin 1 was isolated from clathrin-coated pits. The encoded…
- **Diseases (Open Targets)**: neurodegeneration with brain iron accumulation (0.593); neurodegeneration with brain iron accumulation 7 (0.437); neurodegenerative disease (0.410); response to radiation (0.331); cardiovascular disorder (0.071)
- **Europe PMC papers**: 437
- **Why important**: REPS1 is a connector between the central UNK neighborhood, ARID1B and NIPBL, and the UBAC2 and USP24 regulatory branch. Its established functions include endocytosis and endosomal transport through interactions with signaling and cytoskeletal machinery. HPA shows broad tissue specificity with cell-type enhancement in several non-immune populations, making it informative for interpreting the module as a trafficking or cell-state signal rather than a secreted protein program.
- **Conclusion**: Established evidence supports REPS1 as an endocytic and signaling adaptor. Its module position suggests a possible bridge between intracellular trafficking and nuclear regulatory genes, but that bridge is not demonstrated as a physical complex. A hypothesis is that altered receptor internalization or endosomal recycling contributes to the shared abundance pattern in skin-associated and circulating cells.

## Module 3

**Tissue pair**: circulatory_system and skin  
**Genes (15)**: AFG2B, ANXA3, CDA, EXD2, EXTL2, GOLM1, HAUS3, HUS1, LRSAM1, IGF2R, PODXL, SPARC, TIMELESS, VTN, ZNF592

### Function

No GO/KEGG term passed global correction, so the module does not support a globally significant pathway assignment from GO/KEGG. Its most coherent interpretation is a mixed extracellular-adhesion and cell-surface trafficking program, with a secondary contribution from neutrophil- and bone-marrow-associated cell states. The STRING supplementary term (STRING COMPARTMENTS Extracellular region; within-query FDR = 0.0123) places part of the module in the extracellular region, driven by SPARC, VTN, ANXA3, IGF2R, EXTL2, CDA, PODXL, and GOLM1, but (STRING COMPARTMENTS Extracellular region; within-query FDR = 0.0123) is supplementary rather than globally corrected enrichment. The remaining genes include proteins involved in cytoskeletal or membrane organization, Golgi and lysosomal trafficking, DNA damage responses, mitosis, and ubiquitin-related processes. Therefore, the module is better viewed as a co-abundance signature linking extracellular matrix or adhesion biology with cellular-composition and epithelial or hematopoietic signals than as a single established biochemical pathway.

**Cell composition.** The module is not predominantly a plasma or secreted-protein module: only SPARC and VTN are explicitly secreted to blood, while the module-level HPA summary identifies three secreted genes. VTN is liver-enriched and associated with hepatocytes and cholangiocytes, whereas SPARC is associated with stromal cells and several blood-cell groups. HPA also shows repeated associations with neutrophils, neutrophil progenitors, bone marrow, monocytes, basophils, and esophageal apical cells. ANXA3 and CDA are immune-cell or neutrophil-associated, and IGF2R is neutrophil-enriched at the single-cell level. At the same time, many genes have low tissue or immune-cell specificity, and most proteins are intracellular or membrane-associated rather than secreted. The shared circulatory-system and skin signal may therefore reflect a combination of blood-derived or immune-cell content, extracellular proteins present in circulation, and broadly expressed structural or housekeeping-like programs, rather than a skin-specific mechanism. HPA protein detection supports presence in skin for many genes, but the circulatory-system comparison has no matching HPA tissue measurement.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest and only reported high-confidence STRING relationship is SPARC-VTN, supporting a known extracellular interaction. STRING's supplementary extracellular-region term (STRING COMPARTMENTS Extracellular region; within-query FDR = 0.0123) includes eight module genes, but it does not establish a globally significant module pathway. All other module gene pairs lack reported STRING interactions at the stated confidence threshold. No hu.MAP complex contains at least two module members. The network therefore contains one externally supported extracellular link, while most co-abundance edges are not corroborated by the cited STRING or hu.MAP resources. This pattern is consistent with a module assembled from shared expression or cellular composition signals rather than a well-defined physical complex. The SPARC-VTN relationship provides a plausible extracellular anchor, but it should not be extended to claim direct physical interactions among the other module genes.

**STRING interactions (score >= 0.7)**: 1 of 105 gene pairs: SPARC–VTN (0.922)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Extracellular region (FDR = 0.0123, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a new biological pathway or a newly discovered physical complex. No GO/KEGG term passed global correction, hu.MAP reports no multi-member complex, and STRING independently supports only the SPARC-VTN relationship. The co-abundance combination may still be a new observation in the specific cross-tissue analysis, especially because it joins extracellular proteins with neutrophil-associated, epithelial, trafficking, and genome-maintenance genes. However, absence from STRING or hu.MAP alone does not prove novelty, and the HPA pattern provides plausible explanations based on shared cell types or blood contamination. The defensible conclusion is that the cross-tissue co-abundance signature may be dataset-specific and potentially novel as a module, but its component functions and at least one of its relationships are already established.

**Hypothesis.** Hypothesis: the conserved signal reflects a shared extracellular-interface state present across circulatory-system and skin samples. In this model, liver- or stromal-associated circulating proteins such as VTN and SPARC form the extracellular component, while PODXL and IGF2R connect cell-surface organization with intracellular trafficking. ANXA3 and CDA may mark neutrophil or myeloid contribution, and the remaining intracellular genes may reflect parallel epithelial, proliferative, stress-response, or cell-maintenance states. The module could therefore arise when extracellular matrix or adhesion remodeling co-occurs with blood-cell representation and trafficking activity, rather than from one common complex. This hypothesis requires validation with cell-deconvolved data, protein measurements, and perturbation or interaction assays.

### Important genes

#### SPARC

- **Related proteins** (co-abundance neighbors): PODXL (0.94), ZNF592 (0.83), EXTL2 (0.81); STRING partners: VTN (0.922)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: secreted protein acidic and cysteine rich. This gene encodes a cysteine-rich acidic matrix-associated protein. The encoded protein is required for the collagen in bone to become calcified but is also involved in extracellular matrix synthesis and promotion of changes to cell shape. The gene product has been associated with tumor suppression but has also been correlated with metastasis based on changes to cell shape which can promote tumor …
- **Diseases (Open Targets)**: osteogenesis imperfecta (0.707); neurodegenerative disease (0.443); hereditary disease (0.414); osteogenesis imperfecta type 4 (0.381); Abnormality of the skeletal system (0.358)
- **Europe PMC papers**: 17798
- **Why important**: SPARC is a central extracellular anchor in the module, connects to PODXL, ZNF592, and EXTL2 in the co-abundance network, and is the partner in the only high-confidence STRING interaction, with VTN. HPA identifies it as secreted to blood and associated with stromal cells and several blood-cell groups. Its annotated functions include extracellular-matrix synthesis, cell-shape regulation, endothelial migration, and angiogenesis-related processes. It has extensive literature and disease associations involving bone and connective-tissue biology.
- **Conclusion**: Established evidence supports SPARC as the strongest extracellular and matrix-related representative of the module, with a known relationship to VTN. It is a plausible biological driver or marker of the shared signal, but the module data do not establish that SPARC causes the co-abundance pattern or that all module genes participate in its pathway.

#### VTN

- **Related proteins** (co-abundance neighbors): PODXL (0.87), ANXA3 (0.84); STRING partners: SPARC (0.922)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vitronectin. The protein encoded by this gene functions in part as an adhesive glycoprotein. Differential expression of this protein can promote either cell adhesion or migration as it links cells to the extracellular matrix through a variety of ligands. These ligands include integrins, plasminogen activator inhibitor-1, and urokinase plasminogen activator receptor. This secreted protein can be present in the …
- **Diseases (Open Targets)**: hypertensive disorder (0.421); dengue disease (0.376); neurodegenerative disease (0.343); temporal arteritis (0.338); age-related macular degeneration (0.313)
- **Europe PMC papers**: 3940
- **Why important**: VTN links to PODXL and ANXA3 in the module and forms the only high-confidence STRING pair with SPARC. It is a secreted blood protein, is tissue-enriched in liver, and is associated with hepatocytes and cholangiocytes. Its established functions include adhesion, cell-matrix interactions, integrin signaling, and regulation of migration. Its substantial literature and associations with vascular and inflammatory disorders make it important for interpreting a circulatory-system component.
- **Conclusion**: Established evidence supports VTN as a circulating extracellular adhesion factor and as the clearest known interaction partner of SPARC. A reasonable hypothesis is that VTN helps transmit a blood-derived extracellular signal into the shared module, but the skin co-abundance signal could also reflect sample composition rather than local VTN production.

#### PODXL

- **Related proteins** (co-abundance neighbors): SPARC (0.94), VTN (0.87), IGF2R (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: podocalyxin like. This gene encodes a member of the sialomucin protein family. The encoded protein was originally identified as an important component of glomerular podocytes. Podocytes are highly differentiated epithelial cells with interdigitating foot processes covering the outer aspect of the glomerular basement membrane. Other biological activities of the encoded protein include: binding in a membrane protein …
- **Diseases (Open Targets)**: schizophrenia (0.451); young-onset Parkinson disease (0.443); hypertensive disorder (0.429); refractive error (0.383); familial nephrotic syndrome (0.373)
- **Europe PMC papers**: 2372
- **Why important**: PODXL has one of the strongest network positions and connects the extracellular anchor genes SPARC and VTN with IGF2R. HPA identifies kidney and podocyte enrichment, absence from immune cells, and plasma-membrane or endoplasmic-reticulum localization. Its annotated functions include regulation of cell adhesion, migration, and microvillus assembly. It has substantial literature and disease associations, including familial nephrotic syndrome and vascular-related disorders.
- **Conclusion**: Established evidence supports PODXL as a cell-surface adhesion and morphology component that could connect extracellular proteins to epithelial or specialized membrane biology. The module does not show a hu.MAP complex or STRING partners for PODXL, so its proposed bridging role remains a hypothesis based on co-abundance and network placement.

#### ANXA3

- **Related proteins** (co-abundance neighbors): VTN (0.84), CDA (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A3. This gene encodes a member of the annexin family.  Members of this calcium-dependent phospholipid-binding protein family play a role in the regulation of cellular growth and in signal transduction pathways.  This protein functions in the inhibition of phopholipase A2 and cleavage of inositol 1,2-cyclic phosphate to form inositol 1-phosphate. This protein may also play a role in anti-coagulation. […
- **Diseases (Open Targets)**: rheumatoid arthritis (0.318); Meniere disease (0.276); insomnia (0.255); hair color (0.209); refractive error (0.176)
- **Europe PMC papers**: 2243
- **Why important**: ANXA3 connects VTN with CDA and has strong HPA associations with bone marrow, neutrophils, megakaryocytes, and several epithelial or trophoblast cell types. Its annotations include phospholipid binding, signal transduction, phagocytosis, neutrophil degranulation, endothelial migration, and angiogenesis. It has substantial literature and immune or inflammatory disease associations, making it useful for distinguishing a cellular-composition component from a purely extracellular-matrix interpretation.
- **Conclusion**: Established evidence supports ANXA3 as a membrane-associated and neutrophil-linked factor that may represent myeloid content in the shared module. Its connection to VTN is a module-network observation rather than a confirmed physical interaction, so a role in coupling neutrophil biology to extracellular adhesion remains a hypothesis.

#### IGF2R

- **Related proteins** (co-abundance neighbors): PODXL (0.86), EXD2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enhanced; location Golgi apparatus; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor 2 receptor. This gene encodes a receptor for both insulin-like growth factor 2 and mannose 6-phosphate. The binding sites for each ligand are located on different segments of the protein. This receptor has various functions, including in the intracellular trafficking of lysosomal enzymes, the activation of transforming growth factor beta, and the degradation of insulin-like growth factor 2. Mutation or loss o…
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.498); coronary artery disorder (0.477); Hypercholesterolemia (0.369); myocardial ischemia (0.359); coronary atherosclerosis (0.349)
- **Europe PMC papers**: 12245
- **Why important**: IGF2R connects PODXL with EXD2 and is associated by HPA with neutrophils. It is a Golgi-localized receptor involved in insulin-like growth factor and mannose-six-phosphate handling, lysosomal-enzyme targeting, lysosomal transport, and degradation of IGF2. It has extensive literature and disease associations involving liver cancer and coronary or vascular disorders. This makes it an important intracellular trafficking counterpart to the extracellular genes.
- **Conclusion**: Established evidence supports IGF2R as a trafficking and lysosomal receptor with relevance to both hepatic and vascular disease biology. Its position next to PODXL suggests a possible membrane-trafficking bridge in the module, but the available data do not demonstrate a direct interaction or a unified IGF2R-centered mechanism.

## Module 4

**Tissue pair**: circulatory_system and skin  
**Genes (6)**: AKAP12, COL4A2, HLA-DRA, H2AC21, PRKCD, MINDY1

### Function

The strongest functional interpretation is a mixed vascular, immune, apoptotic, and nuclear-regulatory signal rather than a single established pathway. The only globally corrected GO/KEGG evidence is (GO:BP regulation of glial cell apoptotic process; q_global = 0.0393), regulation of glial cell apoptotic process, supported by AKAP12 and PRKCD. This annotation should be interpreted cautiously because the module is from circulatory_system and skin, whereas the term is glial and the overlap is limited. The gene functions nevertheless provide biologically coherent components: AKAP12 is a signaling scaffold associated with protein kinases and phosphatase; PRKCD is a stress-responsive kinase that can regulate apoptosis; COL4A2 is a basement-membrane collagen with anti-angiogenic canstatin activity; HLA-DRA mediates antigen presentation; MINDY1 is a K48-linked deubiquitinase; and H2AC21 encodes a core histone. Thus, the module may reflect coordinated regulation of vascular extracellular matrix, immune presentation, stress or apoptotic signaling, and cellular state. No STRING functional-enrichment term was reported. The absence of additional significant terms does not invalidate the module, but it limits confidence in assigning one unified pathway.

**Cell composition.** The module is not predominantly a plasma or secreted-protein module: only COL4A2 is annotated as secreted to the extracellular matrix. It is also not uniformly blood-cell enriched, although the HPA profile indicates substantial cell-composition influence. HLA-DRA is enriched in antigen-presenting and several B-cell, monocyte, and dendritic-cell populations; MINDY1 and PRKCD show associations with neutrophils or platelets; AKAP12 is immune-cell enriched for basophils; and H2AC21 is tissue enriched in bone marrow with progenitor-cell associations. Several genes are associated with vascular endothelial, pericyte, smooth-muscle, or vascular smooth-muscle cell types. Most genes have skin protein detection, while the tissue-level profile spans low specificity, tissue enhancement, and tissue enrichment rather than a single shared tissue signature. The shared co-abundance signal may therefore reflect mixtures of vascular or stromal cells and circulating or infiltrating immune cells in the samples, in addition to regulation within skin-associated cells.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulation of glial cell apoptotic process | 0.0393 | AKAP12, PRKCD |

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no STRING functional-enrichment term was reported. No hu.MAP complex contained multiple module members. Consequently, the co-abundance edges are not supported here by known physical interaction networks or a documented shared protein complex. The strongest internal network position belongs to MINDY1, which connects to PRKCD, COL4A2, and AKAP12; COL4A2 connects to HLA-DRA; and HLA-DRA connects to H2AC21. These links describe co-abundance structure, not established molecular binding. Known biology is instead supplied mainly by individual gene annotations: COL4A2 is a basement-membrane component, HLA-DRA is an antigen-presentation molecule, AKAP12 is a signaling scaffold, PRKCD is a protein kinase, MINDY1 is a deubiquitinase, and H2AC21 is a histone. The lack of STRING and hu.MAP support argues against calling this a known physical complex.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel co-abundance association, but it cannot be declared a newly discovered biological pathway from the supplied evidence alone. The module combines genes with established individual functions, yet it has no reported high-confidence STRING interaction, no multi-member hu.MAP complex, and no STRING enrichment. Its novelty is therefore most defensible at the level of the cross-tissue co-abundance pattern and its particular juxtaposition of vascular matrix, antigen presentation, signaling, ubiquitin regulation, and chromatin components. The pattern could also arise from shared cell-type composition or sample-level blood contamination, especially given the HPA immune and vascular-cell signals. Confirmation would require replication, cell-composition adjustment, and ideally orthogonal molecular or perturbation evidence.

**Hypothesis.** Hypothesis: the module marks a vascular-interface state shared by skin and circulatory-system samples in which basement-membrane remodeling and endothelial or stromal signaling occur alongside antigen-presenting immune-cell presence and stress or apoptotic regulation. In this model, COL4A2 represents the extracellular-matrix and vascular-interface component, HLA-DRA represents antigen-presenting cells, AKAP12 and PRKCD represent localized signaling and apoptosis-related regulation, while MINDY1 and H2AC21 reflect broader intracellular protein-turnover or chromatin-state consequences. This is a mechanistic hypothesis rather than an established pathway, because the network has no reported STRING or hu.MAP support and (GO:BP regulation of glial cell apoptotic process; q_global = 0.0393) is the only globally corrected functional term.

### Important genes

#### MINDY1

- **Related proteins** (co-abundance neighbors): PRKCD (0.84), COL4A2 (0.84), AKAP12 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MINDY lysine 48 deubiquitinase 1. Enables K48-linked polyubiquitin modification-dependent protein binding activity; Lys48-specific deubiquitinase activity; and cysteine-type carboxypeptidase activity. Predicted to be involved in protein K48-linked deubiquitination. Located in nuclear body. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.473); diabetes mellitus (0.446); hepatocellular carcinoma (0.093); breast cancer (0.084); breast carcinoma (0.081)
- **Europe PMC papers**: 105
- **Why important**: MINDY1 occupies the most connected position in the module and links the signaling genes PRKCD and AKAP12 with the matrix gene COL4A2. Its annotated K48-linked deubiquitinase activity provides a plausible protein-turnover and regulatory mechanism that could connect otherwise diverse module components. It has disease associations including type two diabetes and diabetes mellitus and a moderate literature base, making it a useful mechanistic bridge rather than merely a marker.
- **Conclusion**: Established evidence supports MINDY1 as a nuclear-body-associated K48 deubiquitinase with a central co-abundance position and metabolic disease associations. It is hypothesized, but not demonstrated, to coordinate the module by altering stability or signaling of other cellular regulators.

#### COL4A2

- **Related proteins** (co-abundance neighbors): MINDY1 (0.84), HLA-DRA (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type IV alpha 2 chain. This gene encodes one of the six subunits of type IV collagen, the major structural component of basement membranes. The C-terminal portion of the protein, known as canstatin, is an inhibitor of angiogenesis and tumor growth. Like the other members of the type IV collagen gene family, this gene is organized in a head-to-head conformation with another type IV collagen gene so that each gene pair sh…
- **Diseases (Open Targets)**: brain small vessel disease 2A, autosomal dominant (0.728); porencephaly (0.612); Dupuytren Contracture (0.587); coronary artery disorder (0.548); hemorrhage, intracerebral, susceptibility to (0.541)
- **Europe PMC papers**: 5290
- **Why important**: COL4A2 is a highly studied basement-membrane collagen, is secreted to the extracellular matrix, and is detected in skin. Its module connection to MINDY1 and HLA-DRA places vascular matrix biology next to intracellular regulatory and immune-presentation signals. The encoded collagen has documented roles in extracellular-matrix organization and negative regulation of angiogenesis, and its disease associations include brain small-vessel disease, porencephaly, Dupuytren contracture, coronary artery disorder, and intracerebral hemorrhage susceptibility.
- **Conclusion**: Established evidence supports COL4A2 as the clearest structural and vascular-interface component of the module, with strong disease relevance. A role in coupling matrix remodeling to local immune presentation is a hypothesis based on co-abundance, not a demonstrated interaction.

#### HLA-DRA

- **Related proteins** (co-abundance neighbors): COL4A2 (0.82), H2AC21 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Group enriched; location None; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: major histocompatibility complex, class II, DR alpha. HLA-DRA is one of the HLA class II alpha chain paralogues. This class II molecule is a heterodimer consisting of an alpha and a beta chain, both anchored in the membrane. This molecule is expressed on the surface of various antigen presenting cells such as B lymphocytes, dendritic cells, and monocytes/macrophages, and plays a central role in the immune system and response by presenting peptides de…
- **Diseases (Open Targets)**: Graham Little-Piccardi-Lassueur syndrome (0.263); lichen planopilaris (0.231); Sepsis (0.100); nonpapillary renal cell carcinoma (0.094); diffuse large B-cell lymphoma (0.082)
- **Europe PMC papers**: 9685
- **Why important**: HLA-DRA is connected in the module to COL4A2 and H2AC21 and has the strongest direct immune interpretation. It is tissue enhanced in lung and lymphoid tissue, enriched in conventional dendritic cells, and associated with monocyte, B-cell, and plasmacytoid dendritic-cell populations. Its established function is presentation of extracellular peptides through MHC class II, and it has disease associations including lichen planopilaris, sepsis, renal cancer, and lymphoma.
- **Conclusion**: Established evidence supports HLA-DRA as an antigen-presenting-cell marker and a likely indicator of immune-cell composition in this shared module. Its participation in a coordinated vascular-matrix program remains a hypothesis and may instead reflect co-occurring cell populations.

#### PRKCD

- **Related proteins** (co-abundance neighbors): MINDY1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase C delta. The protein encoded by this gene is a member of the protein kinase C family of serine- and threonine-specific protein kinases. The encoded protein is activated by diacylglycerol and is both a tumor suppressor and a positive regulator of cell cycle progression. Also, this protein can positively or negatively regulate apoptosis. Defects in this gene are a cause of autoimmune lymphoproliferative synd…
- **Diseases (Open Targets)**: autoimmune lymphoproliferative syndrome (0.685); acute myeloid leukemia (0.556); mast cell leukemia (0.475); systemic mastocytosis (0.471); mastocytosis (0.464)
- **Europe PMC papers**: 3335
- **Why important**: PRKCD is one of the two genes supporting the globally corrected term (GO:BP regulation of glial cell apoptotic process; q_global = 0.0393) and is directly connected to the central module gene MINDY1. As protein kinase C delta, it provides a signaling link to stress responses, DNA-damage responses, apoptosis, and immune regulation. It is detected in skin, has cell-type associations with neutrophils and platelets, and is linked to autoimmune lymphoproliferative syndrome, acute myeloid leukemia, mast-cell leukemia, and mastocytosis.
- **Conclusion**: Established evidence supports PRKCD as a stress- and apoptosis-related kinase and as a contributor to (GO:BP regulation of glial cell apoptotic process; q_global = 0.0393). Its role as the signaling mediator that links immune or vascular context to apoptosis in this module is a plausible hypothesis, not proven by the co-abundance network.

#### AKAP12

- **Related proteins** (co-abundance neighbors): MINDY1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: A-kinase anchoring protein 12. The A-kinase anchor proteins (AKAPs) are a group of structurally diverse proteins, which have the common function of binding to the regulatory subunit of protein kinase A (PKA) and confining the holoenzyme to discrete locations within the cell. This gene encodes a member of the AKAP family. The encoded protein is expressed in endothelial cells, cultured fibroblasts, and osteosarcoma cells. It asso…
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); hair color (0.460); cutaneous melanoma (0.403); skin aging (0.376); Abnormality of the skeletal system (0.329)
- **Europe PMC papers**: 2075
- **Why important**: AKAP12 is the other gene supporting (GO:BP regulation of glial cell apoptotic process; q_global = 0.0393) and is connected to MINDY1. Its established scaffold function localizes PKA, protein kinase C, and phosphatase signaling, making it particularly relevant to spatial control of cellular responses. It is expressed in endothelial cells and fibroblasts, is detected in skin, and has reported associations with neurodegenerative disease, cutaneous melanoma, skin aging, and skeletal-system abnormality.
- **Conclusion**: Established evidence supports AKAP12 as a signaling scaffold with vascular and skin-relevant cellular associations and a role in (GO:BP regulation of glial cell apoptotic process; q_global = 0.0393). Its proposed function as a local organizer of the module's signaling and apoptotic response is a hypothesis.

## Module 5

**Tissue pair**: circulatory_system and skin  
**Genes (6)**: ANKRD54, LPIN1, NAGK, PES1, SNX8, TBC1D7

### Function

No GO or KEGG term passed global correction, and STRING reported no supplementary functional enrichment. Therefore, the module does not support a statistically established pathway-level function. Its genes instead point to several cellular processes: intracellular endosome-to-Golgi transport through SNX8, lipid and triglyceride metabolism through LPIN1, amino-sugar salvage through NAGK, growth and nutrient-response regulation through TBC1D7, ribosome biogenesis through PES1, and possible intracellular signaling or kinase regulation through ANKRD54. The most defensible interpretation is a mixed intracellular maintenance module rather than a single established pathway. The co-abundance pattern may reflect shared cellular state, coordinated expression in particular cell populations, or technical or compositional effects rather than direct biochemical cooperation.

**Cell composition.** The module is not dominated by plasma or secreted proteins: every gene is annotated as non-secreted, and all have low immune-cell specificity. This argues against a conventional circulating plasma-protein module or a blood-cell-enriched module. Most genes have low tissue specificity, while LPIN1 is tissue enhanced in skeletal muscle and tongue. Single-cell annotations are heterogeneous, including esophageal apical cells, reproductive cell populations, Hofbauer cells, cDCs, macrophages, and neutrophils. This breadth is more consistent with broadly distributed intracellular proteins plus cell-state or cell-composition effects than with a single lineage-specific program. Protein detection in skin is present for most genes, but the circulatory-system tissue comparison has no matching HPA tissue readout. The shared signal should therefore be interpreted cautiously as potentially reflecting shared resident cell types or general cellular activity in the sampled tissues, not as evidence for a blood-derived module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The module has a sparse co-abundance topology, with one central-looking connector, SNX8, linked to LPIN1, TBC1D7, and ANKRD54, while PES1 connects to ANKRD54 and NAGK connects to LPIN1. However, none of the possible gene pairs reaches the supplied STRING interaction threshold, and STRING lists no partners. No hu.MAP complex contains multiple module members. Thus, the co-abundance relationships are not supported here as known high-confidence physical interactions or membership in a shared protein complex. The network may capture coordinated regulation, shared cellular composition, indirect pathway relationships, or context-specific associations that are absent from current interaction resources.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a newly observed co-abundance association in the circulatory-system and skin comparison, but the evidence does not establish a new biological pathway or protein complex. The absence of STRING and hu.MAP support indicates limited prior representation of direct molecular relationships, but absence from those resources alone cannot prove novelty. The lack of globally significant GO or KEGG enrichment also prevents claiming discovery of a new coherent functional program. A novelty claim would require replication in independent cohorts, preservation of the gene relationships after adjustment for cell composition and tissue-specific factors, and comparison with published co-expression or proteomic modules.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular homeostasis program that combines vesicle trafficking, nutrient and growth control, lipid handling, amino-sugar metabolism, and biosynthetic activity in cells present in both tissues. SNX8 could mark endosomal trafficking, LPIN1 could connect cellular lipid state to transcriptional or metabolic responses, and TBC1D7 could connect nutrient sensing with growth regulation. NAGK, PES1, and ANKRD54 may represent additional metabolic, biosynthetic, or signaling demands in the same cellular states. This is a mechanistic hypothesis, not an established pathway assignment; the sparse network, absent STRING and hu.MAP support, and lack of globally corrected enrichment make indirect regulation or cellular-composition coupling at least as plausible as direct cooperation.

### Important genes

#### SNX8

- **Related proteins** (co-abundance neighbors): LPIN1 (0.82), TBC1D7 (0.82), ANKRD54 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sorting nexin 8. Enables identical protein binding activity and phosphatidylinositol binding activity. Involved in early endosome to Golgi transport and intracellular protein transport. Located in early endosome membrane. Colocalizes with retromer complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: chronic kidney disease (0.406); neuropathic pain (0.229); obesity disorder (0.213); overnutrition (0.176); hypertensive disorder (0.129)
- **Europe PMC papers**: 305
- **Why important**: SNX8 is the most connected node in the module and links LPIN1, TBC1D7, and ANKRD54. Its established annotation places it in early endosome-to-Golgi transport, intracellular protein transport, endosomal membranes, and retromer-associated biology. It is detected in skin and has broad tissue specificity, while its single-cell annotations span several cell types. Its literature volume is modest relative to LPIN1 or PES1, making it a useful candidate for testing whether the module captures a less-studied trafficking-centered program.
- **Conclusion**: Established evidence supports SNX8 as the network connector and an endosomal transport protein. It is a plausible organizing marker for the module, but there is no direct interaction evidence in STRING or hu.MAP and no global enrichment evidence linking the whole module to trafficking. Its role as a mechanistic driver remains a hypothesis.

#### LPIN1

- **Related proteins** (co-abundance neighbors): SNX8 (0.82), NAGK (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lipin 1. This gene encodes a magnesium-ion-dependent phosphatidic acid phosphohydrolase enzyme that catalyzes the penultimate step in triglyceride synthesis including the dephosphorylation of phosphatidic acid to yield diacylglycerol. Expression of this gene is required for adipocyte differentiation and it also functions as a nuclear transcriptional coactivator with some peroxisome proliferator-activated r…
- **Diseases (Open Targets)**: myoglobinuria, acute recurrent, autosomal recessive (0.742); hereditary recurrent myoglobinuria (0.697); Acute rhabdomyolysis (0.455); cardiac arrest (0.320); injury (0.318)
- **Europe PMC papers**: 2508
- **Why important**: LPIN1 connects SNX8 with NAGK and has the strongest tissue-specific signal in the module, including skeletal muscle and tongue. It has an established role in phosphatidic-acid dephosphorylation, triglyceride synthesis and mobilization, fatty-acid catabolism, adipocyte differentiation, and transcriptional coactivation related to lipid metabolism. It also has the largest literature volume among the selected genes and strong disease associations involving recurrent myoglobinuria and rhabdomyolysis.
- **Conclusion**: Established evidence supports LPIN1 as the strongest metabolic and tissue-contextual anchor. Its connection to SNX8 and NAGK is a co-abundance observation, not proof of a shared lipid-trafficking complex. A role in coupling membrane or lipid state to the other module processes is a plausible hypothesis.

#### TBC1D7

- **Related proteins** (co-abundance neighbors): SNX8 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TBC1 domain family member 7. This gene encodes a member of the TBC-domain containing protein family. The encoded protein functions as a subunit of the tuberous sclerosis TSC1-TSC2 complex which plays a role in the regulation of cellular growth and differentiation. Mutations in this gene have been associated with autosomal recessive megalencephaly. Alternative splicing results in multiple transcript variants. Naturally occurri…
- **Diseases (Open Targets)**: macrocephaly/megalencephaly syndrome, autosomal recessive (0.601); genetic developmental and epileptic encephalopathy (0.496); neurodegenerative disease (0.460); isolated megalencephaly (0.370); Macrocephaly (0.343)
- **Europe PMC papers**: 713
- **Why important**: TBC1D7 links to SNX8 and is a component of the TSC one–TSC two growth-regulatory complex. Its annotations include cellular starvation response, negative regulation of TOR signaling, protein ubiquitination, GTPase regulation, and growth-factor response. It is cell-type enhanced in neutrophils but has low immune-cell specificity overall, and it has substantial literature and disease associations involving megalencephaly and developmental encephalopathy.
- **Conclusion**: Established evidence supports TBC1D7 as a nutrient-sensing and growth-regulatory factor. It could explain why a trafficking-associated gene covaries with metabolic genes, but the module does not demonstrate TOR or TSC-complex enrichment. Its proposed coordinating role is therefore hypothesis-level.

#### PES1

- **Related proteins** (co-abundance neighbors): ANKRD54 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli, Nucleoli rim, Mitotic chromosome; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pescadillo ribosomal biogenesis factor 1. This gene encodes a nuclear protein that contains a breast cancer associated gene 1 (BRCA1) C-terminal interaction domain. The encoded protein interacts with BOP1 and WDR12 to form the PeBoW complex, which plays a critical role in cell proliferation via pre-rRNA processing and 60S ribosomal subunit maturation. Expression of this gene may play an important role in breast cancer proliferation and tu…
- **Diseases (Open Targets)**: aortic stenosis (0.137); neoplasm (0.104); head and neck squamous cell carcinoma (0.097); schizophrenia (0.091); neuroblastoma (0.081)
- **Europe PMC papers**: 1080
- **Why important**: PES1 is the module connection to ribosome biogenesis and cell proliferation. It is annotated to preribosomal RNA processing and large-subunit maturation, localizes to nucleolar structures and mitotic chromosomes, and has substantial literature including cancer-related associations. Its single-cell specificity is low, which supports a broadly distributed biosynthetic or proliferative interpretation rather than a narrowly specialized cell type.
- **Conclusion**: Established evidence supports PES1 as a ribosome-biogenesis and proliferation-associated protein. Its presence may indicate general biosynthetic demand or cell-state coupling, but there is no evidence that ribosome biogenesis is a globally enriched module function. A link between growth state and the other module processes remains speculative.

#### NAGK

- **Related proteins** (co-abundance neighbors): LPIN1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-acetylglucosamine kinase. This gene encodes a member of the N-acetylhexosamine kinase family. The encoded protein catalyzes the conversion of N-acetyl-D-glucosamine to N-acetyl-D-glucosamine 6-phosphate, and is the major mammalian enzyme which recovers amino sugars. [provided by RefSeq, Nov 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.201); response to xenobiotic stimulus (0.107); neoplasm (0.086); maturity-onset diabetes of the young (0.078); transient neonatal diabetes mellitus (0.062)
- **Europe PMC papers**: 836
- **Why important**: NAGK connects to LPIN1 and supplies an amino-sugar metabolic dimension. It is the major mammalian enzyme for recovering N-acetylglucosamine and is annotated to amino-sugar metabolism, UDP-N-acetylglucosamine biosynthesis, and related catabolic processes. It is detected in skin and shows cell-type enhancement across epithelial, placental, and Hofbauer-cell annotations, while having a substantial literature base.
- **Conclusion**: Established evidence supports NAGK as a cytosolic amino-sugar salvage enzyme. Its association with LPIN1 could reflect coordinated metabolic state, but no direct interaction or globally significant metabolic enrichment is demonstrated. Its role as part of a shared nutrient or biosynthetic program is a hypothesis.

## Module 6

**Tissue pair**: circulatory_system and skin  
**Genes (12)**: ARHGEF12, C5orf24, POLA2, FOXJ3, FUT8, TUBGCP4, NANP, PHIP, POLR3E, CARS2, VARS2, ZFC3H1

### Function

No GO or KEGG term passed global correction, so the module does not support a formally established shared pathway. Its gene content instead spans RNA processing, transcriptional regulation, DNA replication, mitochondrial translation, glycosylation, cytoskeletal signaling, and centrosomal microtubule organization. The co-abundance pattern is therefore best interpreted as a cross-tissue cellular state or coordinated expression pattern rather than evidence for one defined biochemical function. The strongest functional themes are nuclear gene-expression and RNA-processing activity, mitochondrial protein synthesis, and regulation of cell architecture, but these remain interpretive themes rather than globally significant enrichment results.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the fact sheet reports no secreted genes. It is also not strongly blood-cell enriched. Most genes have low immune-cell specificity, two are not detected in immune cells, and only one is immune-cell enhanced. Most genes have low tissue specificity, while many show cell-type enhancement across diverse cell types including podocytes, glial and neuronal populations, renal tubular cells, and reproductive cells. The proteins are predominantly intracellular, with nuclear, mitochondrial, cytosolic, Golgi, centrosomal, or plasma-membrane locations. Skin protein detection is common among the genes with available skin measurements, whereas circulatory-system protein detection has no matching HPA tissue result. Thus, the shared module is more consistent with broadly expressed cellular programs or shared cell-type composition than with circulating proteins or a blood-contamination signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship within the module is between CARS2 and VARS2. This is biologically coherent because both encode mitochondrial aminoacyl-tRNA synthetases, supporting a small mitochondrial translation submodule. No other listed gene pair has high-confidence STRING support, STRING functional enrichment is absent, and no hu.MAP complex contains multiple module members. Consequently, most co-abundance edges are not independently supported as known physical interactions. The network may capture coordinated expression, indirect regulation, shared cellular state, or cell-composition effects rather than a single protein complex.

**STRING interactions (score >= 0.7)**: 1 of 66 gene pairs: CARS2–VARS2 (0.884)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported co-abundance association, but it cannot be called a new biological pathway on the current evidence. Its lack of globally significant GO or KEGG enrichment, lack of STRING functional enrichment, and absence of a multi-member hu.MAP complex argue against a previously established coherent complex. The known CARS2–VARS2 relationship shows that at least part of the pattern has recognized biological plausibility, while the remaining edges lack corresponding interaction support. Establishing novelty would require replication in independent tissue cohorts, preservation after cell-composition adjustment, comparison with published co-expression modules, and experimental testing. Absence from STRING or hu.MAP alone is not evidence of novelty.

**Hypothesis.** Hypothesis: the shared circulatory-system–skin pattern reflects a broadly expressed intracellular cellular-state program that combines nuclear RNA and transcriptional regulation with mitochondrial translation and cell-architecture control. In this model, the CARS2–VARS2 pair marks coordinated mitochondrial protein synthesis, while ZFC3H1, POLR3E, PHIP, and related nuclear genes reflect linked RNA-processing or transcriptional activity; ARHGEF12 and TUBGCP4 may connect the state to cytoskeletal or centrosomal organization. FUT8 and NANP could contribute metabolic or glycan-processing context. A plausible explanation is shared abundance across particular cell populations or a common proliferative, differentiation, or metabolic state, rather than direct physical assembly of all module proteins. This hypothesis should be tested by single-cell deconvolution, matched protein and transcript measurements, perturbation of the mitochondrial translation pair, and replication in independent circulatory-system and skin datasets.

### Important genes

#### ZFC3H1

- **Related proteins** (co-abundance neighbors): PHIP (0.82), POLA2 (0.81), POLR3E (0.81), ARHGEF12 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger C3H1-type containing. Predicted to enable metal ion binding activity. Predicted to be involved in RNA processing. Located in nucleus. Part of exosome (RNase complex). [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); Short stature (0.323); prostate adenocarcinoma (0.076); type 2 diabetes mellitus (0.071); retinitis pigmentosa (0.071)
- **Europe PMC papers**: 250
- **Why important**: ZFC3H1 has the strongest network position in the module and connects to PHIP, POLA2, POLR3E, and ARHGEF12. Its established annotations place it in nuclear RNA processing and an exosome-associated RNase complex, making it a plausible anchor for the module's gene-expression component. It has skin protein detection and a substantial literature base, while disease associations include neurodegenerative disease and other conditions in Open Targets.
- **Conclusion**: Established evidence supports ZFC3H1 as a highly connected nuclear RNA-processing gene within this network. It is a plausible structural or regulatory anchor, but the module data do not establish that it directly regulates the other module members. Its role as a shared tissue-state marker remains a hypothesis.

#### PHIP

- **Related proteins** (co-abundance neighbors): NANP (0.85), TUBGCP4 (0.83), ZFC3H1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PHIP subunit of CUL4-Ring ligase complex. This gene encodes a protein that binds to the insulin receptor substrate 1 protein and regulates glucose transporter translocation in skeletal muscle cells. The encoded protein may also regulate growth and survival of pancreatic beta cells. Elevated copy number of this gene may be associated with melanoma severity and the encoded protein may promote melanoma metastasis in human patients. [provided…
- **Diseases (Open Targets)**: PHIP-related behavioral problems-intellectual disability-obesity-dysmorphic features syndrome (0.805); Intellectual disability (0.544); hereditary disease (0.543); obesity due to melanocortin 4 receptor deficiency (0.383); obesity disorder (0.383)
- **Europe PMC papers**: 2064
- **Why important**: PHIP is among the most connected genes and links NANP, TUBGCP4, and ZFC3H1. It has established roles in a CUL4-associated complex, insulin-receptor-substrate signaling, glucose-transporter translocation in skeletal muscle, transcriptional regulation, growth, and cell survival. The fact sheet also reports associations with melanoma severity and metastasis and a substantial literature volume, making PHIP especially relevant to a skin-linked module.
- **Conclusion**: Established evidence supports PHIP as a multifunctional signaling and transcriptional regulator with plausible relevance to skin biology and metabolic state. Its central network position makes it important, but the co-abundance data do not prove that PHIP mechanistically drives the module or melanoma-related phenotypes.

#### ARHGEF12

- **Related proteins** (co-abundance neighbors): VARS2 (0.84), NANP (0.81), ZFC3H1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho guanine nucleotide exchange factor 12. Rho GTPases play a fundamental role in numerous cellular processes that are initiated by extracellular stimuli working through G protein-coupled receptors. The encoded protein may form a complex with G proteins and stimulate Rho-dependent signals. This protein has been observed to form a myeloid/lymphoid fusion partner in acute myeloid leukemia. Three transcript variants encoding different isoform…
- **Diseases (Open Targets)**: glaucoma (0.524); open-angle glaucoma (0.511); lymphoid neoplasm (0.370); lung carcinoma (0.370); Chordoid Meningioma (0.370)
- **Europe PMC papers**: 923
- **Why important**: ARHGEF12 connects VARS2, NANP, and ZFC3H1 and provides the clearest link to Rho-dependent signaling, actin organization, and responses initiated by G protein-coupled receptors. It is cell-type enhanced in podocytes, is not detected in immune cells, and has disease associations involving glaucoma and neoplasia. These features make it a candidate bridge between intracellular signaling and cell architecture.
- **Conclusion**: Established evidence supports ARHGEF12 as a Rho-signaling regulator with potential consequences for cell shape, adhesion, and cytoskeletal behavior. Its connection to mitochondrial and RNA-processing genes is not an established physical pathway in this module; that cross-process role is a hypothesis requiring validation.

#### VARS2

- **Related proteins** (co-abundance neighbors): ARHGEF12 (0.84), CARS2 (0.81); STRING partners: CARS2 (0.884)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: valyl-tRNA synthetase 2, mitochondrial. This gene encodes a mitochondrial aminoacyl-tRNA synthetase, which catalyzes the attachment of valine to tRNA(Val) for mitochondrial translation. Mutations in this gene cause combined oxidative phosphorylation deficiency-20, and are also associated with early-onset mitochondrial encephalopathies. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Aug 20…
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 20 (0.791); neurodegenerative disease (0.533); hereditary disease (0.522); mitochondrial disease (0.437); Alzheimer disease (0.370)
- **Europe PMC papers**: 436
- **Why important**: VARS2 is a mitochondrial valyl-tRNA synthetase and forms the strongest known STRING relationship in the module with CARS2. It is linked to mitochondrial translation and oxidative-phosphorylation deficiency, with disease associations involving mitochondrial and neurodegenerative disorders. Its cell-type enhancement across neural and renal populations is consistent with a broadly relevant mitochondrial function.
- **Conclusion**: Established evidence supports VARS2 as part of mitochondrial translational machinery and as a biologically meaningful partner of CARS2. The module may therefore contain a genuine mitochondrial translation signal, but it does not demonstrate that the entire module is a mitochondrial complex.

#### CARS2

- **Related proteins** (co-abundance neighbors): FUT8 (0.81), VARS2 (0.81); STRING partners: VARS2 (0.884)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cysteinyl-tRNA synthetase 2, mitochondrial. This gene encodes a putative member of the class I family of aminoacyl-tRNA synthetases. These enzymes play a critical role in protein biosynthesis by charging tRNAs with their cognate amino acids. This protein is encoded by the nuclear genome but is likely to be imported to the mitochondrion where it is thought to catalyze the ligation of cysteine to tRNA molecules. A splice-site mutation in this…
- **Diseases (Open Targets)**: Combined oxidative phosphorylation defect type 27 (0.757); neurodegenerative disease (0.550); hereditary disease (0.471); mitochondrial disease (0.416); atrial fibrillation (0.389)
- **Europe PMC papers**: 441
- **Why important**: CARS2 is the mitochondrial cysteinyl-tRNA synthetase and the partner of VARS2 in the only high-confidence STRING interaction detected within the module. Its established role in mitochondrial protein biosynthesis and associations with oxidative-phosphorylation disorders and epilepsy provide a strong functional interpretation for this pair. It also has substantial literature support and skin protein detection.
- **Conclusion**: Established evidence supports CARS2 as a credible mitochondrial translation component and as the best-supported physical-interaction node in the module. Its presence strengthens a mitochondrial submodule interpretation, but does not establish a causal role in the shared circulatory-system–skin co-abundance pattern.

#### FUT8

- **Related proteins** (co-abundance neighbors): CARS2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fucosyltransferase 8. This gene encodes an enzyme belonging to the family of fucosyltransferases. The product of this gene catalyzes the transfer of fucose from GDP-fucose to N-linked type complex glycopeptides. This enzyme is distinct from other fucosyltransferases which catalyze alpha1-2, alpha1-3, and alpha1-4 fucose addition. The expression of this gene may contribute to the malignancy of cancer cells and to their …
- **Diseases (Open Targets)**: congenital disorder of glycosylation with defective fucosylation (0.784); hereditary disease (0.415); COVID-19 (0.404); gout (0.400); Abnormality of the skeletal system (0.380)
- **Europe PMC papers**: 3371
- **Why important**: FUT8 is a Golgi fucosyltransferase involved in core fucosylation and N-glycan processing. It connects to CARS2 in the co-abundance graph, although that edge is not independently supported by high-confidence STRING evidence. FUT8 has the largest literature volume among the listed genes and is associated with congenital disorders of glycosylation, cancer biology, and altered invasion or metastasis, making it important for interpreting possible glycan or disease-state context.
- **Conclusion**: Established evidence supports FUT8 as a glycosylation enzyme with broad relevance to protein maturation and disease biology. Its co-abundance with CARS2 may reflect a shared cellular state or indirect regulation; a direct mechanistic connection between glycosylation and mitochondrial translation is only a hypothesis here.

## Module 7

**Tissue pair**: circulatory_system and skin  
**Genes (44)**: ARK2N, ASCC1, ASF1A, BLOC1S6, CDK12, NDUFAF1, DDX10, DMAP1, DPCD, POLD1, DHFR, FBXO30, GEMIN8, GOPC, KDM3B, KIF20A, KIF15, DNAAF2, LARP4, LIMA1, RNGTT, NDUFA7, NSMCE2, GATAD2A, PDP1, PHAX, PINX1, PLEKHA5, PRRC2B, PUM3, RBM7, RFX1, MRPL45, POLR1B, RPAP1, POLR2G, SMYD3, SPATS2, TAF5, UBAP1, UCK2, VAV2, WDR43, ZNF638

### Function

The module is most consistent with a broadly expressed intracellular gene-expression and cellular-maintenance program rather than a narrowly tissue-specific pathway. Its strongest biological themes are RNA synthesis and processing, ribosome biogenesis, chromatin and transcriptional regulation, cell-cycle and cytoskeletal processes, mitochondrial respiration, and cilium-related biology. These interpretations are supported by the annotated functions of POLR1B, POLR2G, RPAP1, WDR43, DDX10, GEMIN8, CDK12, TAF5, KIF20A, NDUFA7, NDUFAF1, and DNAAF2, together with the internal co-abundance structure. However, no GO or KEGG term passed global correction, so no GO or KEGG enrichment claim is statistically established at the required global level. The functional interpretation therefore rests on convergent gene annotations, network organization, STRING relationships, and hu.MAP membership rather than on globally significant enrichment.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and the proteins detected in skin are predominantly intracellular, including nucleoplasmic, nucleolar, cytosolic, mitochondrial, Golgi, or cytoskeletal proteins. The module therefore resembles a broadly expressed housekeeping and cell-state program more than a skin-specific program. HPA also shows enrichment for spermatogenic and progenitor-related cell types, with some representation of neutrophil and other myeloid populations. This raises the possibility that the shared circulatory-system and skin signal reflects common cell populations, proliferative state, or general biosynthetic demand rather than a mechanism unique to either tissue. The HPA blood-cell summary is mostly low immune-cell specificity, so a simple blood-cell explanation is possible but not strongly established. Skin protein detection is widespread among the measured genes, whereas the circulatory-system protein summary has no matching HPA tissue data.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a coherent but incomplete set of known relationships. The most informative connections link POLR1B with POLR2G, DDX10, PUM3, and WDR43; link POLR2G with RNGTT and TAF5; link PUM3 with DDX10 and WDR43; link NDUFA7 with NDUFAF1; link KIF15 with KIF20A; and connect GEMIN8, PHAX, and RBM7. These relationships support RNA polymerase, nucleolar RNA-processing, mitochondrial complex-I assembly, and mitotic machinery substructures within the module. STRING has no functional-enrichment result for the module, so the interaction evidence should not be treated as a globally corrected enrichment result. hu.MAP independently supports repeated polymerase-associated assemblies containing POLR1B, POLR2G, and RPAP1 (hu.MAP huMAP3_14318.1), (hu.MAP huMAP3_11092.1), (hu.MAP huMAP3_09057.1), (hu.MAP huMAP3_08487.1), (hu.MAP huMAP3_06426.1), and related complexes. It also supports repeated chromatin or transcription-associated assemblies containing DPCD and DMAP1 (hu.MAP huMAP3_07843.1), (hu.MAP huMAP3_09291.1), (hu.MAP huMAP3_10481.1), (hu.MAP huMAP3_14306.1), and repeated complex-I assemblies containing NDUFA7 and NDUFAF1 (hu.MAP huMAP3_14018.1), (hu.MAP huMAP3_06397.1), (hu.MAP huMAP3_09982.1), (hu.MAP huMAP3_09567.1), (hu.MAP huMAP3_14878.1). Because only subsets of these larger complexes occur in the module, the evidence supports embedded known molecular subassemblies rather than a single complete complex. The remaining co-abundance links may reflect shared expression or cell state rather than direct physical interaction.

**STRING interactions (score >= 0.7)**: 13 of 946 gene pairs: DDX10–POLR1B (0.858); DDX10–PUM3 (0.946); DDX10–WDR43 (0.938); GEMIN8–PHAX (0.751); KIF15–KIF20A (0.942); NDUFA7–NDUFAF1 (0.978); PHAX–RBM7 (0.7); POLR1B–POLR2G (0.874); POLR1B–PUM3 (0.763); POLR1B–WDR43 (0.831); POLR2G–RNGTT (0.829); POLR2G–TAF5 (0.915); PUM3–WDR43 (0.916)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14318.1 (POLR2G, RPAP1, POLR1B; 3/58); huMAP3_11092.1 (POLR2G, RPAP1, POLR1B; 3/65); huMAP3_07843.1 (DPCD, DMAP1; 2/23); huMAP3_09291.1 (DPCD, DMAP1; 2/27); huMAP3_09057.1 (RPAP1, POLR1B; 2/36); huMAP3_08487.1 (RPAP1, POLR1B; 2/37); huMAP3_06426.1 (RPAP1, POLR1B; 2/38); huMAP3_10481.1 (DPCD, DMAP1; 2/40); huMAP3_14018.1 (NDUFA7, NDUFAF1; 2/48); huMAP3_06397.1 (NDUFA7, NDUFAF1; 2/49); huMAP3_09982.1 (NDUFA7, NDUFAF1; 2/49); huMAP3_09567.1 (NDUFA7, NDUFAF1; 2/52); huMAP3_14878.1 (NDUFA7, NDUFAF1; 2/53); huMAP3_14306.1 (DPCD, DMAP1; 2/55)

### Novelty

The module should not be called a newly discovered molecular complex or a proven new pathway. Several of its internal relationships and subnetworks are already represented by STRING and hu.MAP, especially the polymerase-associated, complex-I, and chromatin-associated components. Its potentially novel aspect is the co-abundance of these established cellular systems across circulatory-system and skin, particularly the way RNA-processing, transcriptional, mitochondrial, cytoskeletal, and ciliary genes occur in one cross-tissue module. That cross-tissue organization is a hypothesis-generating observation, not proof of novelty. Absence of STRING or hu.MAP support for individual genes does not establish novelty, because co-abundance can arise from regulation, cell composition, or shared cellular state without direct physical interaction. Confirmation would require replication in independent cohorts, assessment of cell composition, and comparison with existing cross-tissue co-expression resources.

**Hypothesis.** Hypothesis: the module represents a shared intracellular maintenance program expressed in common or biologically similar cell populations in blood-related samples and skin. A coordinated demand for transcription, RNA processing, ribosome production, chromatin control, mitochondrial energy production, cytoskeletal remodeling, and ciliary or vesicle-related functions could generate the observed co-abundance pattern. The HPA evidence suggests that cell-state composition, including progenitor, spermatogenic-like, epithelial, and selected myeloid signatures, may contribute substantially. A testable prediction is that the module will track cellular proliferation, biosynthetic activity, or ciliated-cell and epithelial-state composition more strongly than it tracks a tissue-specific extracellular function. This is a mechanistic hypothesis, not an established causal explanation.

### Important genes

#### POLR1B

- **Related proteins** (co-abundance neighbors): PRRC2B (0.87), LARP4 (0.81); STRING partners: DDX10 (0.858), POLR2G (0.874), PUM3 (0.763), WDR43 (0.831)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14318.1, huMAP3_11092.1, huMAP3_09057.1, huMAP3_08487.1, huMAP3_06426.1
- **Function (MyGene.info)**: RNA polymerase I subunit B. Eukaryotic RNA polymerase I (pol I) is responsible for the transcription of ribosomal RNA (rRNA) genes and production of rRNA, the primary component of ribosomes. Pol I is a multisubunit enzyme composed of 6 to 14 polypeptides, depending on the species. Most of the mass of the pol I complex derives from the 2 largest subunits, Rpa1 and Rpa2 in yeast. POLR1B is homologous to Rpa2 (Seither and Grumm…
- **Diseases (Open Targets)**: Treacher Collins syndrome 4 (0.751); Treacher-Collins syndrome (0.383); arthropathy (0.212); Chronic Obstructive Asthma (0.188); lower respiratory tract disorder (0.124)
- **Europe PMC papers**: 521
- **Why important**: POLR1B is a central interpretive anchor because it links the RNA polymerase-associated portion of the network to PUM3, DDX10, WDR43, and POLR2G in STRING and occurs with RPAP1 and POLR2G across multiple hu.MAP complexes (hu.MAP huMAP3_14318.1), (hu.MAP huMAP3_11092.1), (hu.MAP huMAP3_09057.1), (hu.MAP huMAP3_08487.1), (hu.MAP huMAP3_06426.1). Its established function is as a subunit of RNA polymerase I, which produces ribosomal RNA. It has a substantial literature base and a disease association with Treacher Collins syndrome. Its HPA profile is broadly expressed, with a spermatogenic cell-type signal and no secretion evidence.
- **Conclusion**: Established: POLR1B supports a nucleolar transcription and ribosome-production component and is one of the best-supported network anchors. Hypothesis: its cross-tissue co-abundance may report shared biosynthetic or proliferative demand rather than a skin-specific process.

#### GEMIN8

- **Related proteins** (co-abundance neighbors): PUM3 (0.91), LARP4 (0.88), CDK12 (0.87), RPAP1 (0.85), KDM3B (0.85), GATAD2A (0.85), POLD1 (0.82), PHAX (0.81), NDUFA7 (0.80); STRING partners: PHAX (0.751)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gem nuclear organelle associated protein 8. The protein encoded by this gene is part of the SMN complex, which is necessary for spliceosomal snRNP assembly in the cytoplasm and pre-mRNA splicing in the nucleus. The encoded protein binds to both SMN1 and the GEMIN6/GEMIN7 heterodimer, mediating their interaction. This protein is found in nuclear Gemini of Cajal bodies (gems) and in the cytoplasm. Three transcript variants encoding the same p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); glaucoma (0.083); open-angle glaucoma (0.062); proximal spinal muscular atrophy (0.018); Alzheimer disease (0.011)
- **Europe PMC papers**: 165
- **Why important**: GEMIN8 has the strongest weighted network connectivity in the supplied module and connects RNA-processing, translation-related, chromatin-associated, and DNA-maintenance neighborhoods through PUM3, LARP4, CDK12, RPAP1, KDM3B, GATAD2A, POLD1, and PHAX. Its established function in the SMN complex and spliceosomal snRNP assembly gives it a plausible integrative role in RNA maturation. It is broadly expressed, intracellular, detected in skin, and has disease associations involving neurodegeneration and proximal spinal muscular atrophy.
- **Conclusion**: Established: GEMIN8 is a highly connected RNA-processing hub with a known role in snRNP assembly. Hypothesis: it may help couple RNA maturation to the broader transcriptional and cellular-maintenance state represented by this module.

#### CDK12

- **Related proteins** (co-abundance neighbors): GEMIN8 (0.87), PRRC2B (0.80), TAF5 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cyclin dependent kinase 12. Enables RNA polymerase II CTD heptapeptide repeat kinase activity and cyclin binding activity. Involved in phosphorylation of RNA polymerase II C-terminal domain; protein autophosphorylation; and regulation of MAP kinase activity. Located in nuclear speck. Part of cyclin K-CDK12 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: prostate adenocarcinoma (0.638); neurodegenerative disease (0.565); Alzheimer disease (0.502); lysosomal storage disease (0.501); Parkinson disease (0.501)
- **Europe PMC papers**: 4245
- **Why important**: CDK12 connects GEMIN8, PRRC2B, and TAF5 and has a direct established role in RNA polymerase II carboxy-terminal-domain phosphorylation, transcription elongation, and RNA splicing. It is located in nuclear speckles, is broadly expressed, and has a large literature base with disease associations including prostate adenocarcinoma and several neurodegenerative or lysosomal disorders. Its position connects transcriptional regulation with RNA-processing features of the module.
- **Conclusion**: Established: CDK12 provides a mechanistic link between transcription elongation and RNA processing. Hypothesis: coordinated CDK12 activity could help explain why polymerase, RNA-binding, and chromatin-related genes co-vary across the two tissues.

#### NDUFAF1

- **Related proteins** (co-abundance neighbors): RBM7 (0.82); STRING partners: NDUFA7 (0.978)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase complex assembly factor 1. This gene encodes a complex I assembly factor protein. Complex I (NADH-ubiquinone oxidoreductase) catalyzes the transfer of electrons from NADH to ubiquinone (coenzyme Q) in the first step of the mitochondrial respiratory chain, resulting in the translocation of protons across the inner mitochondrial membrane. The encoded protein is required for assembly of complex I, and mutations in this gene ar…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.727); mitochondrial complex I deficiency, nuclear type 11 (0.631); type 2 diabetes mellitus (0.608); diabetes mellitus (0.579); mitochondrial complex I deficiency, nuclear type 1 (0.551)
- **Europe PMC papers**: 571
- **Why important**: NDUFAF1 is the clearest mitochondrial anchor. It has a known STRING relationship with NDUFA7 and occurs with NDUFA7 in repeated hu.MAP complex-I assemblies (hu.MAP huMAP3_14018.1), (hu.MAP huMAP3_06397.1), (hu.MAP huMAP3_09982.1), (hu.MAP huMAP3_09567.1), (hu.MAP huMAP3_14878.1). Its established function is assembly of mitochondrial complex I, and mutations are associated with mitochondrial complex-I deficiency. It is intracellular, broadly expressed, detected in skin, and has disease associations involving mitochondrial complex-I deficiency and diabetes.
- **Conclusion**: Established: NDUFAF1 and NDUFA7 support a genuine complex-I assembly submodule. Hypothesis: mitochondrial energy demand may be coordinated with transcription, RNA processing, and cytoskeletal activity in the shared cell state, but the module does not establish a direct causal link.

#### KIF20A

- **Related proteins** (co-abundance neighbors): DPCD (0.84), RFX1 (0.84), DNAAF2 (0.84); STRING partners: KIF15 (0.942)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm, Cytokinetic bridge, Cleavage furrow, Mitotic spindle; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 20A. Enables protein kinase binding activity. Involved in microtubule bundle formation; midbody abscission; and regulation of cytokinesis. Located in several cellular components, including cleavage furrow; intercellular bridge; and midbody. Implicated in restrictive cardiomyopathy. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: cardiomyopathy, familial restrictive, 6 (0.586); familial isolated restrictive cardiomyopathy (0.370); hepatocellular carcinoma (0.123); central nervous system cancer (0.120); neoplasm (0.111)
- **Europe PMC papers**: 2386
- **Why important**: KIF20A connects DNAAF2, DPCD, and RFX1 and has a strong known STRING relationship with KIF15. Its established function includes microtubule-bundle formation, cytokinesis, midbody abscission, and intracellular transport. HPA places it in bone marrow, lymphoid tissue, and testis, with cell-type signals spanning progenitors and proliferative populations. It has extensive literature and an association with restrictive cardiomyopathy and cancer-related disease contexts.
- **Conclusion**: Established: KIF20A contributes a mitotic and cytoskeletal component and is compatible with progenitor or proliferative cell-state effects. Hypothesis: it may connect cellular division or remodeling to the RNA, mitochondrial, and ciliary features of the module.

## Module 8

**Tissue pair**: circulatory_system and skin  
**Genes (16)**: CALD1, HAUS7, HMGCS1, KIF21A, LRWD1, LUC7L, MAD2L1, MLH1, NKRF, OCIAD2, PRIM1, RBM19, RBM45, TAF6, TGFB1I1, YTHDC2

### Function

No GO or KEGG term passed global correction, so the module does not have a statistically established pathway annotation. Its gene content is heterogeneous but points to a combination of cell-cycle and chromosome-maintenance biology, RNA processing and regulation, intracellular transport, lipid biosynthesis, and contractile or cytoskeletal functions. HAUS7 is the most connected module member and is annotated with centrosome cycle, spindle assembly, and microtubule nucleation functions. MAD2L1, LRWD1, and PRIM1 provide additional links to spindle checkpoint control, replication initiation, and chromatin organization. RBM19, RBM45, LUC7L, YTHDC2, NKRF, and TAF6 indicate RNA binding, RNA splicing, RNA modification, transcriptional regulation, or nucleolar activity. HMGCS1 contributes mevalonate and cholesterol biosynthesis, while CALD1 and TGFB1I1 contribute contractile, adhesion, and transforming-growth-factor-related biology. The overall interpretation is therefore a mixed cellular-state module rather than a coherent, globally validated pathway. The lack of enrichment should not be interpreted as evidence that the module is false.

**Cell composition.** The module contains no secreted genes, arguing against a plasma-protein or secretome-driven module. HPA assigns most genes low immune-cell specificity, with only a small subset showing immune-cell enrichment or group enrichment, so a blood-cell explanation is not dominant. The HPA pattern is instead heterogeneous: many genes are cell-type enhanced, particularly in hepatic stellate cells, pericytes, vascular smooth muscle cells, and related stromal or vascular populations, while tissue-enhanced signals include blood vessel, liver, kidney, retina, bone marrow, and testis. Skin protein detection is present for several members, but absent or unavailable for others. This supports the possibility that shared vascular, stromal, smooth-muscle, proliferative, or other resident cell populations contribute to the circulatory-system and skin co-abundance signal. It does not establish that the module represents one specific cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no hu.MAP complex containing multiple module members. Thus, the co-abundance edges are not supported by the queried physical-interaction resources. Several genes do have well-established functions in cellular systems, such as HAUS7 in the augmin complex, MAD2L1 in the spindle assembly checkpoint, MLH1 in mismatch repair, and TAF6 in transcription initiation, but those established relationships are not represented as within-module STRING or hu.MAP links here. The network should therefore be interpreted primarily as a coordinated expression or abundance pattern, not as a demonstrated protein complex or direct interaction network.

**STRING interactions (score >= 0.7)**: 0 of 120 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported tissue-pair co-abundance pattern, because its member genes show no detected high-confidence STRING pair interactions, no detected multi-member hu.MAP complex, and no globally corrected GO or KEGG annotation. However, these observations do not prove biological novelty: database coverage is incomplete, co-abundance can arise from shared cell composition or technical and sampling effects, and the genes themselves have established functions and disease associations. The most defensible conclusion is that the specific cross-tissue module organization is potentially novel and presently mechanistically unresolved, rather than that the underlying biology is new.

**Hypothesis.** Hypothesis: the shared circulatory-system and skin signal reflects coordinated representation of vascular, stromal, smooth-muscle, and proliferative cell states rather than a single molecular complex. In this model, HAUS7, MAD2L1, LRWD1, and PRIM1 mark cell-cycle, centrosome, replication, and chromatin demands; RBM19, RBM45, LUC7L, YTHDC2, NKRF, and TAF6 mark RNA and transcriptional regulation; HMGCS1 supports membrane-lipid and isoprenoid production; and CALD1 with TGFB1I1 reflects cytoskeletal, adhesion, and contractile remodeling. Shared abundance of these cell-state programs could arise from related vascular or stromal populations present in both tissues. This hypothesis requires validation using cell-resolved data, independent cohorts, and perturbation or spatial experiments.

### Important genes

#### HAUS7

- **Related proteins** (co-abundance neighbors): MAD2L1 (0.91), RBM19 (0.84), LUC7L (0.83), LRWD1 (0.82), HMGCS1 (0.82), CALD1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Centrosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HAUS augmin like complex subunit 7. This gene encodes a subunit of the augmin complex, which regulates centrosome and mitotic spindle integrity, and is necessary for the completion of cytokinesis. The encoded protein was identified by interaction with ubiquitin C-terminal hydrolase 37. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2012].
- **Diseases (Open Targets)**: neurodegenerative disease (0.252); glaucoma (0.035); alopecia (0.024); central nervous system cancer (0.007); head and neck squamous cell carcinoma (0.007)
- **Europe PMC papers**: 126
- **Why important**: HAUS7 is the central network connector in the module and links genes involved in RNA biology, lipid metabolism, replication, and cytoskeletal or contractile biology. Its established augmin-complex function in centrosome and mitotic-spindle integrity provides a plausible organizing signal for a proliferative or remodeling cell state. HPA also reports blood-vessel enhancement, which is relevant to the shared tissue pair. Its disease associations include neurodegenerative disease, glaucoma, alopecia, and several cancers, with a moderate literature base.
- **Conclusion**: Established evidence supports HAUS7 as a centrosome and spindle-associated factor with vascular enrichment in HPA. It is a strong marker of the module's network structure, but the data do not establish that HAUS7 drives the cross-tissue co-abundance pattern. A role as a coordinator of proliferative or cytoskeletal state is a hypothesis.

#### HMGCS1

- **Related proteins** (co-abundance neighbors): OCIAD2 (0.84), HAUS7 (0.82), PRIM1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3-hydroxy-3-methylglutaryl-CoA synthase 1. Enables protein homodimerization activity. Predicted to be involved in acetyl-CoA metabolic process and farnesyl diphosphate biosynthetic process, mevalonate pathway. Predicted to be located in cytoplasm. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.556); rigid spine syndrome (0.500); mathematical ability (0.289); prostate carcinoma (0.232); Alzheimer disease (0.231)
- **Europe PMC papers**: 3616
- **Why important**: HMGCS1 is connected to HAUS7, OCIAD2, and PRIM1 and supplies a distinct metabolic interpretation through the mevalonate, cholesterol, and isoprenoid biosynthetic pathways. It has liver-enhanced HPA expression and skin protein detection. Its disease associations span neurodegenerative disease, rigid spine syndrome, prostate carcinoma, and Alzheimer disease, and it has extensive literature support.
- **Conclusion**: Established evidence supports HMGCS1 as a cytosolic enzyme in acetyl-CoA and sterol-related metabolism. Its inclusion suggests that membrane-lipid or isoprenoid demand may accompany the module state, but co-abundance alone does not show that this metabolic program is causally linked to the cell-cycle or stromal signals.

#### CALD1

- **Related proteins** (co-abundance neighbors): HAUS7 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Actin filaments; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caldesmon 1. This gene encodes a calmodulin- and actin-binding protein that plays an essential role in the regulation of smooth muscle and nonmuscle contraction. The conserved domain of this protein possesses the binding activities to Ca(2+)-calmodulin, actin, tropomyosin, myosin, and phospholipids. This protein is a potent inhibitor of the actin-tropomyosin activated myosin MgATPase, and serves as a mediating…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.499); diaphragmatic hernia (0.447); glaucoma (0.405); diverticular disease (0.393); open-angle glaucoma (0.390)
- **Europe PMC papers**: 3386
- **Why important**: CALD1 is directly connected to the central HAUS7 node and represents actin, calmodulin, tropomyosin, and smooth-muscle or nonmuscle contraction biology. HPA places it in cell types including breast myoepithelial cells, decidual stromal cells, hepatic stellate cells, and Leydig cells, with skin protein detection and neutrophil immune enrichment. It has substantial literature and associations with skeletal, diaphragmatic, ocular, and diverticular disorders.
- **Conclusion**: Established evidence supports CALD1 as a cytoskeletal and contractile regulator with relevance to stromal and muscle-like cells. It strengthens the interpretation that tissue composition or vascular and stromal remodeling may contribute to the module. A direct functional bridge between CALD1 and the other module branches remains hypothetical.

#### MLH1

- **Related proteins** (co-abundance neighbors): RBM19 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutL homolog 1. The protein encoded by this gene can heterodimerize with mismatch repair endonuclease PMS2 to form MutL alpha, part of the DNA mismatch repair system. When MutL alpha is bound by MutS beta and some accessory proteins, the PMS2 subunit of MutL alpha introduces a single-strand break near DNA mismatches, providing an entry point for exonuclease degradation. The encoded protein is also involved in DNA…
- **Diseases (Open Targets)**: Lynch syndrome (0.848); colorectal cancer (0.820); mismatch repair cancer syndrome 1 (0.806); Muir-Torre syndrome (0.758); colon carcinoma (0.744)
- **Europe PMC papers**: 25031
- **Why important**: MLH1 is connected to RBM19 and represents a highly established DNA mismatch-repair and DNA-damage-signaling function. It has low tissue and immune-cell specificity in HPA, skin protein detection, extensive literature, and strong disease associations with Lynch syndrome, colorectal cancer, and mismatch-repair cancer syndromes. Its presence may mark genome-maintenance demands in a proliferative cell state.
- **Conclusion**: Established evidence supports MLH1 as a core mismatch-repair factor with major cancer relevance. The module data support using it as a marker of genome-maintenance biology, but they do not establish defective repair or a cancer process in either tissue. Its proposed connection to the module's broader state is therefore interpretive.

#### YTHDC2

- **Related proteins** (co-abundance neighbors): RBM19 (0.82), KIF21A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: YTH N6-methyladenosine RNA binding protein C2. This gene encodes a member of the DEAH (Asp-Glu-Ala-His) subfamily of proteins, part of the DEAD (Asp-Glu-Ala-Asp) box family of RNA helicases. The encoded protein binds to N6-methyladenosine, a common modified RNA nucleotide that is enriched in the stop codons and 3' UTRs of eukaryotic messenger RNAs. Binding of proteins to this modified nucleotide may regulate mRNA translation and stability. Thi…
- **Diseases (Open Targets)**: Hyperhidrosis (0.321); neurodegenerative disease (0.304); preeclampsia (0.277); brain compression (0.211); edema (0.211)
- **Europe PMC papers**: 3247
- **Why important**: YTHDC2 is connected to RBM19 and KIF21A and contributes RNA modification recognition, RNA helicase, translation, and RNA stability biology. It has low broad tissue specificity, a large literature base, and disease associations including hyperhidrosis, neurodegenerative disease, preeclampsia, brain compression, and edema. Its position links the RNA-regulatory branch to the transport-related branch.
- **Conclusion**: Established evidence supports YTHDC2 as an RNA-regulatory helicase that recognizes methylated RNA. Its module role may reflect coordinated post-transcriptional regulation in a shared cell state, but the supplied evidence does not demonstrate a specific YTHDC2-dependent mechanism in circulatory-system or skin tissue.

## Module 9

**Tissue pair**: circulatory_system and skin  
**Genes (6)**: CTNNBIP1, CNN2, FAM91A1, PARP4, RELL1, THTPA

### Function

No GO/KEGG term passed global correction, and there was no supplementary STRING functional enrichment. The gene annotations nevertheless suggest a heterogeneous cellular program rather than a single established pathway: CTNNBIP1 provides a possible negative-Wnt and transcriptional-regulatory component; CNN2 contributes actin-filament and mechanical-organization biology; RELL1 is linked to positive p38MAPK regulation; FAM91A1 to intracellular transport and vesicle tethering; THTPA to thiamine diphosphate metabolism; and PARP4 to poly-ADP-ribosylation, DNA-damage responses, and inflammation. The co-abundance pattern should therefore be interpreted as an association of cell-state or cellular-composition signals, not as proof of a unified biochemical pathway.

**Cell composition.** The module is not dominated by secreted or plasma proteins: none of its genes are annotated as secreted. HPA evidence instead points toward cellular composition. Most genes have cell-type-enhanced expression, with repeated enrichment for neutrophils and neutrophil progenitors, while megakaryocytes, mast cells, eosinophils, and several epithelial or neural cell types also appear. CTNNBIP1 has tissue-enhanced evidence in skin and esophageal cell populations, whereas the other genes are mostly broadly distributed at the tissue level. Protein detection in skin is present for most genes, but this does not establish that the proteins originate from skin cells. Because the module is shared by circulatory_system and skin, a blood-cell contribution, particularly neutrophil-related contribution, or shared immune-cell admixture is a plausible explanation. The mixed HPA pattern also argues against assigning the module exclusively to skin biology.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair in the module reaches the stated STRING interaction threshold, and no STRING functional-enrichment result is available. No hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not supported by the supplied high-confidence physical or functional interaction resources. This does not refute coordinated regulation or shared cellular composition, but it provides no evidence that the module is a known protein complex or a densely connected molecular pathway. The strongest network position belongs to CTNNBIP1, which connects to THTPA, PARP4, and CNN2; RELL1 links CNN2 with FAM91A1. These network relationships are co-abundance observations rather than established molecular interactions.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be novel as a cross-tissue co-abundance pattern, because it has no high-confidence STRING interactions, no multi-member hu.MAP complex, and no globally significant GO/KEGG annotation. However, those absences alone do not establish biological novelty. Several individual gene functions are already established, and the HPA pattern suggests that shared neutrophil or other cell-type composition could generate the signal. The most defensible conclusion is that the specific cross-tissue module configuration is a candidate novel observation whose mechanistic novelty remains unproven and requires replication, cell-composition adjustment, and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a shared immune-cell or blood-cell-associated state present in both circulatory-system and skin samples, with neutrophil-related composition being a leading possibility. Within that state, cytoskeletal organization through CNN2, p38MAPK-associated signaling through RELL1, transcriptional and Wnt regulation through CTNNBIP1, intracellular transport through FAM91A1, metabolic support through THTPA, and stress or inflammatory regulation through PARP4 may covary. This is a mechanistic hypothesis, not an established pathway, because the module lacks globally significant enrichment, STRING support, and hu.MAP support.

### Important genes

#### CTNNBIP1

- **Related proteins** (co-abundance neighbors): THTPA (0.81), PARP4 (0.81), CNN2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin beta interacting protein 1. The protein encoded by this gene binds CTNNB1 and prevents interaction between CTNNB1 and TCF family members. The encoded protein is a negative regulator of the Wnt signaling pathway. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: liver disorder (0.313); adolescent idiopathic scoliosis (0.241); colorectal carcinoma (0.102); breast cancer (0.088); breast carcinoma (0.088)
- **Europe PMC papers**: 852
- **Why important**: CTNNBIP1 is the central network node, connecting to THTPA, PARP4, and CNN2. Its established function as a CTNNB1-interacting negative regulator of Wnt signaling gives the module a plausible regulatory anchor. HPA supports skin and esophageal epithelial association, and its disease-linked literature footprint is substantial relative to several other module members.
- **Conclusion**: Established evidence supports CTNNBIP1 as a Wnt and transcriptional regulator with a prominent position in this co-abundance network. It is plausible, but unproven, that CTNNBIP1 helps coordinate the module or reflects an epithelial component shared by skin and circulation-associated samples.

#### CNN2

- **Related proteins** (co-abundance neighbors): RELL1 (0.87), CTNNBIP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calponin 2. The protein encoded by this gene, which can bind actin, calmodulin, troponin C, and tropomyosin, may function in the structural organization of actin filaments. The encoded protein could play a role in smooth muscle contraction and cell adhesion. Several pseudogenes of this gene have been identified, and are present on chromosomes 1, 2, 3, 6, 9, 11, 13, 15, 16, 21 and 22. Alternative splicing resu…
- **Diseases (Open Targets)**: Pulmonary artery atresia (0.416); asthma (0.410); retinitis pigmentosa (0.370); Alzheimer disease (0.366); chronic rhinosinusitis (0.333)
- **Europe PMC papers**: 983
- **Why important**: CNN2 occupies a bridge-like position between RELL1 and CTNNBIP1 and is annotated for actin-filament, actomyosin, adhesion, and mechanical-response biology. HPA links it to esophageal epithelial cells, megakaryocytes, neutrophil progenitors, and neutrophils. Its disease associations and comparatively substantial literature make it an informative candidate for connecting cellular structure with the immune-cell composition signal.
- **Conclusion**: Established evidence supports CNN2 as a cytoskeletal and mechanical-organization protein. Its network position and HPA profile make it a strong marker candidate for the module, but they do not show that CNN2 physically interacts with RELL1 or CTNNBIP1 or drives the cross-tissue pattern.

#### RELL1

- **Related proteins** (co-abundance neighbors): CNN2 (0.87), FAM91A1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Microtubules; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RELT like 1. Involved in positive regulation of p38MAPK cascade. Located in microtubule cytoskeleton and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: placental abruption (0.275); placental retention (0.173); contracture (0.136); esophageal cancer (0.121); urolithiasis (0.071)
- **Europe PMC papers**: 229
- **Why important**: RELL1 connects CNN2 and FAM91A1 and is associated with positive regulation of the p38MAPK cascade. HPA specifically places it in neutrophils and neutrophil progenitors, as well as other cell types, and it has a plasma-membrane and microtubule localization profile. These features make it relevant to a possible immune-cell activation or stress-response interpretation.
- **Conclusion**: Established evidence supports RELL1 as a p38MAPK-associated membrane and cytoskeletal protein with neutrophil-related expression. A role in an inflammatory or stress-linked module is a reasonable hypothesis, but the supplied data do not establish pathway activation or causality.

#### PARP4

- **Related proteins** (co-abundance neighbors): CTNNBIP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Microtubules, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: poly(ADP-ribose) polymerase family member 4. This gene encodes poly(ADP-ribosyl)transferase-like 1 protein, which is capable of catalyzing a poly(ADP-ribosyl)ation reaction. This protein has a catalytic domain which is homologous to that of poly (ADP-ribosyl) transferase, but lacks an N-terminal DNA binding domain which activates the C-terminal catalytic domain of poly (ADP-ribosyl) transferase. Since this protein is not capable of binding D…
- **Diseases (Open Targets)**: COVID-19 (0.370); severe acute respiratory syndrome (0.370); lung adenocarcinoma (0.222); ventricular septal defect (0.218); frozen shoulder (0.182)
- **Europe PMC papers**: 713
- **Why important**: PARP4 is directly connected to the central CTNNBIP1 node and is annotated for poly-ADP-ribosylation-like activity, DNA repair, DNA-damage response, inflammatory response, and protein modification. HPA associates it with mast cells, neutrophil progenitors, and neutrophils. Its disease links and literature support make it a useful candidate for a stress-response interpretation.
- **Conclusion**: Established evidence supports PARP4 as a nuclear and cytosolic factor related to protein modification, damage responses, and inflammation. Its inclusion is consistent with a cell-stress hypothesis, but the module does not demonstrate PARP4 enzymatic activity or a direct connection to the other module genes.

#### FAM91A1

- **Related proteins** (co-abundance neighbors): RELL1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Microtubules; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: family with sequence similarity 91 member A1. Involved in intracellular protein transport and vesicle tethering to Golgi. Located in cytoplasmic vesicle and trans-Golgi network. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: breast carcinoma (0.075); otitis media (0.051); eustachian tube disorder (0.051); distal arthrogryposis (0.042); brachydactyly type A4 (0.040)
- **Europe PMC papers**: 160
- **Why important**: FAM91A1 is the terminal partner of RELL1 and is annotated for intracellular protein transport and vesicle tethering at the trans-Golgi network. HPA detects cell-type-enhanced expression in neutrophils, while its tissue specificity is low. Although it has a smaller literature base than the leading candidates, it may report vesicle-trafficking biology in the shared cell population.
- **Conclusion**: Established evidence supports FAM91A1 as an intracellular trafficking and vesicle-tethering protein with neutrophil-associated expression. Its network connection makes it relevant to the module, but there is insufficient evidence to claim that it mechanistically couples vesicle transport to RELL1 or to the broader module.

## Module 10

**Tissue pair**: circulatory_system and skin  
**Genes (8)**: DHX9, EIF3C, EIF3L, HNRNPR, MAT2A, RPL12, RPL3, RPL6

### Function

The module is best interpreted as a cytoplasmic gene-expression and protein-synthesis module centered on ribosome function and translation initiation. The strongest primary evidence is the global enrichment for cytoplasmic translation (GO:BP cytoplasmic translation; q_global = 4.43e-06), ribonucleoprotein complex (GO:CC ribonucleoprotein complex; q_global = 0.00025), cytosolic large ribosomal subunit (GO:CC cytosolic large ribosomal subunit; q_global = 0.000408), translation (GO:BP translation; q_global = 0.00485), protein biosynthesis (GO:BP protein biosynthetic process; q_global = 0.00485), large-ribosomal-subunit and cytosolic-ribosome components (GO:CC large ribosomal subunit; q_global = 0.0194) (GO:CC cytosolic ribosome; q_global = 0.0194), and translation-initiation complexes (5 globally significant GO/KEGG terms, q_global 0.025–0.0429; see the table). RPL3, RPL6 and RPL12 represent the large-ribosomal-subunit component, whereas EIF3C and EIF3L represent translation initiation. DHX9 and HNRNPR extend the module toward RNA handling, including RNA unwinding, RNA processing and ribonucleoprotein biology. MAT2A is not represented in the globally enriched terms, but its connection to RPL3 is consistent with a possible link between translation and methyl-donor metabolism. Overall, the most defensible interpretation is coordinated basal translation and RNA-processing activity rather than a tissue-specific signaling pathway.

**Cell composition.** The module is composed entirely of intracellular proteins, with no secreted genes and low immune-cell specificity across the genes. Most genes have low tissue specificity and several are canonical ribosomal or translation-initiation factors, so the module has a broadly expressed housekeeping-like character. HPA detects all module proteins in skin, while the available circulatory-system protein comparison has no matching tissue data. The cell-type-enhanced annotations for subsets of genes include secretory, stromal, suprabasal and neural cell types, but there is no consistent blood-cell enrichment. Therefore, the shared circulatory-system and skin signal could reflect broadly active cellular translation, shared nonimmune cell populations, or sample-composition effects; it should not be interpreted as a secreted blood-protein module.

**GO/KEGG enrichment**: 13 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP cytoplasmic translation | 4.43e-06 | DHX9, EIF3C, EIF3L, RPL12, RPL3, RPL6 |
| GO:CC ribonucleoprotein complex | 0.00025 | DHX9, EIF3C, EIF3L, HNRNPR, RPL12, RPL3, RPL6 |
| GO:CC cytosolic large ribosomal subunit | 0.000408 | RPL12, RPL3, RPL6 |
| GO:BP translation | 0.00485 | DHX9, EIF3C, EIF3L, RPL12, RPL3, RPL6 |
| GO:BP protein biosynthetic process | 0.00485 | DHX9, EIF3C, EIF3L, RPL12, RPL3, RPL6 |
| GO:CC large ribosomal subunit | 0.0194 | RPL12, RPL3, RPL6 |
| GO:CC cytosolic ribosome | 0.0194 | RPL12, RPL3, RPL6 |
| GO:CC eukaryotic translation initiation factor 3 complex | 0.025 | EIF3C, EIF3L |
| GO:CC eukaryotic 43S preinitiation complex | 0.025 | EIF3C, EIF3L |
| GO:CC eukaryotic 48S preinitiation complex | 0.025 | EIF3C, EIF3L |
| GO:CC cytosolic translation preinitiation complex | 0.025 | EIF3C, EIF3L |
| GO:BP formation of cytoplasmic translation initiation complex | 0.0429 | EIF3C, EIF3L |
| GO:MF structural constituent of ribosome | 0.0497 | RPL12, RPL3, RPL6 |

### STRING and hu.MAP

STRING supports a coherent core of known relationships. EIF3C–EIF3L is strongly supported, as are the ribosomal relationships among RPL3, RPL6 and RPL12. DHX9 is linked to HNRNPR and RPL6, and EIF3L is linked to RPL6. These relationships agree with the primary GO interpretation and indicate that much of the module corresponds to established translation and ribonucleoprotein biology. STRING also places the genes in translation-initiation, ribosomal-subunit, RNA-processing and translational-silencing contexts (15 supplementary STRING terms; within-query FDR 8.51e-08–0.00064), but these are supplementary annotations rather than independent globally corrected evidence. hu.MAP identifies EIF3C and EIF3L together in multiple eIF3-related complexes (hu.MAP huMAP3_01276.1) (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1), providing orthogonal complex-level support. The absence of hu.MAP assignments for the other module genes does not negate their ribosomal or RNA-processing functions; it indicates that the module is not identical to a single experimentally defined complex. MAT2A lacks a reported STRING or hu.MAP relationship in the supplied evidence, so its co-abundance connection to RPL3 remains network-level rather than established physical interaction evidence.

**STRING interactions (score >= 0.7)**: 7 of 28 gene pairs: DHX9–HNRNPR (0.909); DHX9–RPL6 (0.958); EIF3C–EIF3L (0.999); EIF3L–RPL6 (0.89); RPL12–RPL3 (0.999); RPL12–RPL6 (0.999); RPL3–RPL6 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Formation of a pool of free 40S subunits (FDR = 8.51e-08, 5 genes); RCTM L13a-mediated translational silencing of Ceruloplasmin expression (FDR = 1.13e-07, 5 genes); RCTM GTP hydrolysis and joining of the 60S ribosomal subunit (FDR = 1.13e-07, 5 genes); Process Cytoplasmic translation (FDR = 2.91e-06, 5 genes); Component Ribonucleoprotein complex (FDR = 6.8e-05, 7 genes); COMPARTMENTS Cytosolic large ribosomal subunit (FDR = 0.00019, 3 genes); RCTM Peptide chain elongation (FDR = 0.00031, 3 genes); RCTM Viral mRNA Translation (FDR = 0.00034, 3 genes); RCTM Selenocysteine synthesis (FDR = 0.00034, 3 genes); RCTM Eukaryotic Translation Termination (FDR = 0.00034, 3 genes); Component Cytosolic large ribosomal subunit (FDR = 0.00036, 3 genes); RCTM Nonsense Mediated Decay (NMD) independent of the Exon Junction Complex (EJC) (FDR = 0.00037, 3 genes); RCTM Response of EIF2AK4 (GCN2) to amino acid deficiency (FDR = 0.00043, 3 genes); NetworkNeighborAL Cytoplasmic ribosomal proteins (FDR = 0.00059, 3 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 0.00064, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01276.1 (EIF3C, EIF3L; 2/17); huMAP3_13175.1 (EIF3C, EIF3L; 2/20); huMAP3_11246.1 (EIF3C, EIF3L; 2/24)

### Novelty

This is unlikely to be a newly discovered molecular mechanism because its central components are well-established ribosomal proteins and translation-initiation factors, and several of its relationships are already supported by STRING and hu.MAP. The potentially novel aspect is the reproducible co-abundance of this particular combination across circulatory_system and skin, especially the placement of MAT2A and RNA-processing genes alongside the translation core. However, the fact sheet does not provide replication, perturbation, disease-state comparison, or independent tissue-specific validation sufficient to establish that this cross-tissue association is novel. Absence of a STRING or hu.MAP edge, particularly for MAT2A, should be viewed as an unresolved relationship rather than evidence of novelty.

**Hypothesis.** Hypothesis: the conserved module reflects a shared cellular program that maintains protein production and RNA handling in cells represented in both circulatory-system and skin samples. The ribosomal core may coordinate with eIF3-mediated translation initiation, while DHX9 and HNRNPR may connect translation to RNA processing or transcript handling. MAT2A could provide a metabolic context in which methyl-donor availability influences gene-expression capacity, but this connection is speculative because MAT2A has no primary enrichment annotation or supplied STRING/hu.MAP relationship. A useful test would be to examine whether module activity tracks cellular composition, translational stress, RNA-processing state, or methionine-cycle activity rather than assuming a specialized skin or vascular pathway.

### Important genes

#### RPL3

- **Related proteins** (co-abundance neighbors): DHX9 (0.89), RPL6 (0.85), EIF3C (0.84), MAT2A (0.81), RPL12 (0.81); STRING partners: RPL12 (0.999), RPL6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein L3. Ribosomes, the complexes that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L3P family of ribosomal proteins and it is located in the cytoplasm. The p…
- **Diseases (Open Targets)**: Duchenne muscular dystrophy (0.506); Orthomyxoviridae infectious disease (0.463); cystic fibrosis (0.389); neuromuscular disease caused by qualitative or quantitative defects of dystrophin (0.323); inflammatory bowel disease (0.308)
- **Europe PMC papers**: 2316
- **Why important**: RPL3 is the strongest network hub in the supplied subgraph and connects the ribosomal core with DHX9, EIF3C and MAT2A. It appears in the primary cytoplasmic-translation, ribonucleoprotein, large-ribosomal-subunit, translation and protein-biosynthesis terms (8 globally significant GO/KEGG terms, q_global 4.43e-06–0.0497; see the table), and it is supported across the STRING translation and ribosome annotations (15 supplementary STRING terms; within-query FDR 8.51e-08–0.00064). It encodes a constituent of the cytosolic large ribosomal subunit, has broad tissue distribution, is detected in skin, and has extensive literature and disease-association coverage.
- **Conclusion**: Established evidence supports RPL3 as a central structural component of the translation machinery and as an important network anchor. Its hub position makes it a useful marker of the module, but does not by itself establish that RPL3 drives the cross-tissue co-abundance pattern or any listed disease association.

#### RPL6

- **Related proteins** (co-abundance neighbors): RPL3 (0.85), DHX9 (0.83); STRING partners: DHX9 (0.958), EIF3L (0.89), RPL12 (0.999), RPL3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein L6. This gene encodes a protein component of the 60S ribosomal subunit. This protein can bind specifically to domain C of the tax-responsive enhancer element of human T-cell leukemia virus type 1, and may participate in tax-mediated transactivation of transcription. As is typical for genes encoding ribosomal proteins, there are multiple processed pseudogenes of this gene dispersed throughout the genom…
- **Diseases (Open Targets)**: Duchenne muscular dystrophy (0.503); Orthomyxoviridae infectious disease (0.463); cystic fibrosis (0.388); stroke disorder (0.370); hypertensive disorder (0.344)
- **Europe PMC papers**: 1588
- **Why important**: RPL6 is a member of the ribosomal core and connects to RPL3, DHX9 and EIF3L. It occurs in nearly all of the primary translation and ribosome terms (8 globally significant GO/KEGG terms, q_global 4.43e-06–0.0497; see the table) and in the corresponding STRING annotations (15 supplementary STRING terms; within-query FDR 8.51e-08–0.00064). Its STRING links to RPL3, RPL12, EIF3L and DHX9 provide strong support for a bridge between the ribosomal and RNA-handling portions of the module. HPA indicates low tissue specificity, skin detection and enhancement in several nonimmune cell types, while the gene has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports RPL6 as both a structural ribosomal component and a connector between translation initiation and RNA-related genes in this module. A specific regulatory role in the shared tissue pattern remains a hypothesis.

#### EIF3C

- **Related proteins** (co-abundance neighbors): RPL3 (0.84), EIF3L (0.81); STRING partners: EIF3L (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_01276.1, huMAP3_13175.1, huMAP3_11246.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C is the central translation-initiation representative of the module. It participates in all of the primary translation-initiation complex terms (5 globally significant GO/KEGG terms, q_global 0.025–0.0429; see the table), as well as the broader translation and ribonucleoprotein terms (4 globally significant GO/KEGG terms, q_global 4.43e-06–0.00485; see the table). It forms a very strongly supported STRING pair with EIF3L and is present with EIF3L in multiple hu.MAP eIF3 complexes (hu.MAP huMAP3_01276.1) (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1). It is broadly expressed, detected in skin, and has disease and cancer associations with a substantial literature base.
- **Conclusion**: Established evidence identifies EIF3C as a component of eIF3 and the cytoplasmic translation-initiation machinery, making it a key functional marker of the module. The data do not establish that altered EIF3C activity causes the observed cross-tissue co-abundance.

#### DHX9

- **Related proteins** (co-abundance neighbors): RPL3 (0.89), RPL6 (0.83); STRING partners: HNRNPR (0.909), RPL6 (0.958)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 provides the clearest non-ribosomal RNA-processing connection. It is an ATP-dependent RNA and DNA–RNA helicase with nuclear and cytoplasmic localization, appears in the primary translation and ribonucleoprotein terms (4 globally significant GO/KEGG terms, q_global 4.43e-06–0.00485; see the table), and connects in the module to RPL3 and RPL6. STRING additionally supports DHX9 relationships with HNRNPR and RPL6 (STRING Component Ribonucleoprotein complex; within-query FDR = 6.8e-05) (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.00064). Its broad tissue profile, skin detection, developmental and neurological disease associations, and large literature base make it an informative candidate for linking RNA processing to translation.
- **Conclusion**: Established evidence supports DHX9 as an RNA helicase associated with RNA processing and with the translation-related module. It is plausible, but not demonstrated, that DHX9 couples transcript processing or export to translation in the shared tissue signal.

#### MAT2A

- **Related proteins** (co-abundance neighbors): RPL3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionine adenosyltransferase 2A. The protein encoded by this gene catalyzes the production of S-adenosylmethionine (AdoMet) from methionine and ATP. AdoMet is the key methyl donor in cellular processes. [provided by RefSeq, Jun 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.545); familial thoracic aortic aneurysm and aortic dissection (0.416); autoimmune disorder of central nervous system (0.340); prostate carcinoma (0.252); Abnormality of the cardiovascular system (0.192)
- **Europe PMC papers**: 2615
- **Why important**: MAT2A is the module's distinctive metabolic gene and is connected to the translation hub RPL3 in the co-abundance network. It encodes the enzyme that produces S-adenosylmethionine, a central methyl donor, and has tissue enhancement in pancreas, cell-type enhancement in smooth muscle cells, skin detection and disease associations involving neurological, vascular and neoplastic conditions. Unlike the translation genes, it has no supplied primary GO/KEGG enrichment, STRING partner or hu.MAP complex assignment, making it important mainly because it may define the distinctive boundary of the module.
- **Conclusion**: Established evidence supports MAT2A as a methyl-donor biosynthesis enzyme and as a co-abundant neighbor of RPL3. Any functional coupling between methyl-donor metabolism and the translation module is a hypothesis requiring biochemical, perturbational or longitudinal validation.

## Module 11

**Tissue pair**: circulatory_system and skin  
**Genes (6)**: HK2, RANGRF, PDLIM7, POMK, SHOC2, WASHC4

### Function

No GO or KEGG term passed global correction, so there is no statistically supported pathway-level assignment for this module. The genes instead suggest a heterogeneous intracellular module involving endosomal and actin-associated organization through WASHC4, glycosylation relevant to dystroglycan through POMK, cytoskeletal and focal-adhesion biology through PDLIM7, glucose metabolism through HK2, RAS–MAPK signaling through SHOC2, and Ran-dependent regulation of cardiac sodium-channel biology through RANGRF. The sparse chain-like topology and absence of functional enrichment argue against treating these genes as an established common biochemical pathway. A shared expression or cellular-composition signal, particularly involving neutrophil-lineage cells, is a more cautious interpretation.

**Cell composition.** All module genes have HPA annotation and none is classified as secreted, so this is not a plasma-protein module. Most genes show low tissue specificity, while the tissue-enhanced signals include blood vessel, intestine, skeletal muscle, and retina. HPA single-cell evidence repeatedly points toward neutrophils or neutrophil progenitors, with additional signals involving eosinophils, basophils, adipocytes, colonocytes, cone photoreceptors, stromal or epithelial populations, and megakaryocytes. PDLIM7 has a blood-cell group-enriched pattern, and HK2 has an immune-cell-enhanced pattern. The combination of intracellular proteins, broad tissue distribution, and granulocyte-associated expression makes shared blood-cell content or shared cell types a plausible contributor to the circulatory-system and skin association. Skin protein detection is present for most genes, whereas PDLIM7 is not detected there by IHC; this supports expression in skin samples but does not establish a unified skin-specific mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was observed among the module members, and there was no supplementary STRING functional enrichment. No hu.MAP complex contained multiple module members. Thus, the module is not supported by currently catalogued physical interaction or complex membership among these proteins. The co-abundance edges may represent coordinated expression, indirect regulation, shared cellular composition, or technical and sampling effects rather than direct molecular binding. The absence of STRING and hu.MAP support does not refute the co-abundance pattern, but it substantially limits mechanistic interpretation.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a previously unreported co-abundance pattern, because the module has no high-confidence internal STRING relationships, no multi-member hu.MAP complex, and no globally significant GO or KEGG annotation. However, those absences do not prove biological novelty. Several members have well-established individual functions and disease associations, including WASHC4 in endosomal transport, POMK in protein O-linked glycosylation, RANGRF in cardiac sodium-channel regulation, PDLIM7 in actin-associated complexes, HK2 in glycolysis, and SHOC2 in RAS–MAPK signaling. The most defensible conclusion is that the specific cross-tissue co-abundance arrangement is under-characterized and potentially novel, while its biological meaning remains unvalidated.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular state present in a subset of blood-associated or granulocyte-related cells represented in both circulatory-system and skin samples. In this model, cellular metabolic demand involving HK2, cytoskeletal and adhesion remodeling involving PDLIM7 and WASHC4, signaling modulation involving SHOC2, and specialized membrane or glycosylation functions involving RANGRF and POMK become co-regulated without forming a single physical complex. This model is provisional because it is based on co-abundance and HPA composition rather than direct perturbation, interaction, or pathway-enrichment evidence.

### Important genes

#### WASHC4

- **Related proteins** (co-abundance neighbors): POMK (0.85), RANGRF (0.81), SHOC2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WASH complex subunit 4. This gene encodes a component of the WASH complex, which functions in the intracellular transport of endosomes. Mutations in this gene have been detected in individuals with autosomal recessive cognitive disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014].
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.611); Intellectual disability (0.345); mathematical ability (0.322); Abnormality of the skeletal system (0.148); corneal ulcer (0.140)
- **Europe PMC papers**: 116
- **Why important**: WASHC4 has the strongest network position in the module and connects to POMK, RANGRF, and SHOC2. Its established annotation places it in the WASH complex, endosome organization, endosomal transport, and regulation of Arp2/3-dependent actin nucleation. It is broadly expressed by HPA, detected in skin, and has a disease association with autosomal recessive intellectual disability.
- **Conclusion**: Established evidence supports WASHC4 as an intracellular trafficking and actin-regulatory protein with disease relevance. Its central network position makes it a useful module anchor, but there is no evidence here that it directly organizes the other module proteins. Its role as a shared driver of the cross-tissue co-abundance pattern remains a hypothesis.

#### POMK

- **Related proteins** (co-abundance neighbors): HK2 (0.87), WASHC4 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein O-mannose kinase. This gene encodes a protein that may be involved in the presentation of the laminin-binding O-linked carbohydrate chain of alpha-dystroglycan (a-DG), which forms transmembrane linkages between the extracellular matrix and the exoskeleton. Some pathogens use this O-linked carbohydrate unit for host entry. Loss of function compound heterozygous mutations in this gene were found in a human patient af…
- **Diseases (Open Targets)**: muscular dystrophy-dystroglycanopathy (congenital with brain and eye anomalies), type a, 12 (0.806); limb-girdle muscular dystrophy due to POMK deficiency (0.694); muscular dystrophy-dystroglycanopathy, type A (0.669); muscular dystrophy-dystroglycanopathy (limb-girdle), type c, 12 (0.653); congenital muscular dystrophy with cerebellar involvement (0.381)
- **Europe PMC papers**: 262
- **Why important**: POMK is directly connected to HK2 and WASHC4 and is the module member most clearly linked to protein O-mannose kinase activity and alpha-dystroglycan glycosylation. Its established disease associations include muscular dystrophy-dystroglycanopathy and Walker–Warburg-spectrum disease. It is detected in skin and has a substantial literature base.
- **Conclusion**: Established evidence supports POMK as a glycosylation enzyme with important developmental and muscular disease consequences. Its connection to HK2 is biologically suggestive but does not demonstrate coupling between glycosylation and glycolysis in this module. Any proposed role in the shared tissue module is therefore exploratory.

#### PDLIM7

- **Related proteins** (co-abundance neighbors): RANGRF (0.91); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Actin filaments, Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 7. The protein encoded by this gene is representative of a family of proteins composed of conserved PDZ and LIM domains. LIM domains are proposed to function in protein-protein recognition in a variety of contexts including gene transcription and development and in cytoskeletal interaction. The LIM domains of this protein bind to protein kinases, whereas the PDZ domain binds to actin filaments. The g…
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); nasopharyngeal carcinoma (0.121); neoplasm (0.120); lymphoma (0.115); Hodgkins lymphoma (0.105)
- **Europe PMC papers**: 808
- **Why important**: PDLIM7 is linked to RANGRF and has a distinctive HPA profile involving blood vessel, intestine, skeletal muscle, neutrophils, and other stromal or muscle-associated cell populations. Its protein localizes to actin filaments and focal adhesion sites, and its established functions include actin cytoskeleton organization, receptor-mediated endocytosis, heart development, and muscle structure development. It also has the largest literature volume among the module's structural and signaling candidates.
- **Conclusion**: Established evidence supports PDLIM7 as an actin-associated scaffold that can connect cytoskeletal organization with tissue structure and adhesion. Its blood-cell enrichment makes it particularly relevant to the possibility of a cellular-composition signal. Whether it mechanistically links the module to skin or circulation cannot be concluded from the present data.

#### HK2

- **Related proteins** (co-abundance neighbors): POMK (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hexokinase 2. Hexokinases phosphorylate glucose to produce glucose-6-phosphate, the first step in most glucose metabolism pathways. This gene encodes hexokinase 2, the predominant form found in skeletal muscle. It localizes to the outer membrane of mitochondria. Expression of this gene is insulin-responsive, and studies in rat suggest that it is involved in the increased rate of glycolysis seen in rapidly growi…
- **Diseases (Open Targets)**: neurodegenerative disease (0.541); urolithiasis (0.247); alcohol drinking (0.247); Hypercholesterolemia (0.184); neoplasm (0.120)
- **Europe PMC papers**: 19870
- **Why important**: HK2 is connected to POMK and provides the clearest metabolic component of the module. It catalyzes the first step of glycolysis, is associated with mitochondrial localization and insulin-responsive metabolism, and is prominent in skeletal muscle and cancer metabolism annotations. HPA indicates retina enhancement, several cell-type-enhanced states, skin detection, and immune-cell enhancement involving eosinophils. HK2 also has an extensive literature base.
- **Conclusion**: Established evidence supports HK2 as a major glycolytic and mitochondrial-associated enzyme. Its presence could reflect altered metabolic state in cells represented across the tissues, but it does not establish a module-wide metabolic pathway because the other members lack globally significant metabolic enrichment. A metabolic contribution is plausible but remains a hypothesis.

#### SHOC2

- **Related proteins** (co-abundance neighbors): WASHC4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SHOC2 leucine rich repeat scaffold protein. This gene encodes a protein that consists almost entirely of leucine-rich repeats, a domain implicated in protein-protein interactions. The protein may function as a scaffold linking RAS to downstream signal transducers in the RAS/ERK MAP kinase signaling cascade. Mutations in this gene have been associated with Noonan-like syndrome with loose anagen hair. [provided by RefSeq, May 2010].
- **Diseases (Open Targets)**: Noonan syndrome-like disorder with loose anagen hair (0.826); Noonan syndrome (0.622); RASopathy (0.546); neurodegenerative disease (0.461); Abnormality of the cardiovascular system (0.452)
- **Europe PMC papers**: 2279
- **Why important**: SHOC2 is connected to WASHC4 and is a recognized leucine-rich-repeat scaffold for RAS–ERK signaling. It is associated with Noonan-like syndrome, Noonan syndrome, RASopathies, and cardiovascular abnormalities. HPA shows low tissue specificity, neutrophil and neutrophil-progenitor enhancement, skin detection, and nucleoplasmic or cytosolic localization. Its literature base is substantial.
- **Conclusion**: Established evidence supports SHOC2 as a signaling scaffold with strong developmental and disease relevance. Its neutrophil-associated expression and connection to WASHC4 make it a plausible marker of a shared cellular state. Direct participation in a common module mechanism is not established by the available interaction or enrichment evidence.

#### RANGRF

- **Related proteins** (co-abundance neighbors): PDLIM7 (0.91), WASHC4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAN guanine nucleotide release factor. This gene encodes a protein that has been shown to function as a guanine nucleotide release factor in mouse and to regulate the expression and function of the Nav1.5 cardiac sodium channel in human. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2010].
- **Diseases (Open Targets)**: cardiac arrhythmia (0.209); Rare familial disorder with hypertrophic cardiomyopathy (0.063); hypertrophic cardiomyopathy (0.063); familial isolated dilated cardiomyopathy (0.061); familial long QT syndrome (0.059)
- **Europe PMC papers**: 235
- **Why important**: RANGRF is connected to PDLIM7 and WASHC4 and has an established role as a Ran guanine-nucleotide release factor and regulator of the Nav1.5 cardiac sodium channel. Its annotations include membrane depolarization, heart contraction, cardiac conduction, and intracellular trafficking. It is detected in skin and has disease associations involving arrhythmia and cardiomyopathy.
- **Conclusion**: Established evidence supports RANGRF as a regulator with cardiac electrophysiology and trafficking-related functions. Its presence may connect the module to vascular or excitable-cell biology, but HPA does not provide evidence for a narrowly defined cardiac cell population in this module. A cardiac or membrane-excitability interpretation is therefore a secondary hypothesis rather than an established module function.
