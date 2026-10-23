# Conserved co-abundance modules: heart and rectum

## Module 0

**Tissue pair**: heart and rectum  
**Genes (11)**: BZW2, ANXA2, CLIC1, DNM1L, HNRNPH1, PDCD6IP, PDK1, PSMD13, ATIC, CCT7, XPNPEP1

### Function

The module does not have a globally significant GO or KEGG annotation: no GO or KEGG term passed global correction. Its organization instead suggests a mixed intracellular maintenance program rather than a single established pathway. The most connected gene, CCT7, encodes a subunit of the TRiC chaperonin complex involved in ATP-dependent folding of actin, tubulin, and other proteins. ATIC supports de novo purine biosynthesis, PDK1 regulates pyruvate dehydrogenase and glucose metabolism, PSMD13 represents proteasome-associated protein degradation, HNRNPH1 supports RNA processing, and DNM1L supports mitochondrial and peroxisomal fission. CLIC1 and ANXA2 connect membrane, vesicle, adhesion, chloride-transport, and oxidant-response biology. Thus, the most defensible interpretation is coordinated cellular proteostasis, RNA and nucleotide metabolism, energy regulation, organelle remodeling, and membrane or vesicle biology. This is an integrative interpretation of the gene functions and network, not a globally validated enrichment result.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins, and it is not strongly blood-cell enriched overall. HPA classifies most genes as having low tissue specificity and low immune-cell specificity. ANXA2 is secreted to blood and has group-enriched blood-cell expression, while PDCD6IP is intracellular and membrane associated; these observations warrant consideration of blood or epithelial contributions but do not establish that they drive the module. Most genes are intracellular proteins with cytosolic, nuclear, vesicular, or membrane-associated localizations. Protein detection is broadly supported in both heart and rectum, although ANXA2 and PDCD6IP show tissue-specific detection differences. BZW2 is tissue enhanced in heart muscle, skeletal muscle, and tongue, whereas ANXA2 is tissue enhanced in esophagus. The HPA single-cell annotations are heterogeneous, including trophoblast, epithelial, platelet, spermatogenic, immune, and muscle-associated cell types. This heterogeneity argues against assigning the module solely to a shared specialized cell type. A shared housekeeping-like or stress-related intracellular component remains plausible, but the module is not uniformly annotated as a canonical housekeeping program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a small amount of high-confidence support. The documented relationships are ATIC with CCT7 and ANXA2 with CLIC1. These links support local coherence around purine metabolism and chaperone biology, and around membrane or redox-associated biology, respectively, but STRING reports no functional enrichment for the query. The module network contains additional co-abundance links that are not represented as high-confidence STRING interactions, so co-abundance should not be interpreted as direct physical binding. hu.MAP identifies complex C1, containing ATIC and XPNPEP1 among the module genes, with many other complex members outside the module. This is evidence that the ATIC-XPNPEP1 pair can occur within a larger protein-complex context, but the limited module representation and the confidence annotation do not establish that the entire co-abundance module is one physical complex. Most module genes have no listed hu.MAP complex or STRING partner in the supplied evidence.

**STRING interactions (score >= 0.7)**: 2 of 55 gene pairs: ANXA2–CLIC1 (0.713); ATIC–CCT7 (0.881)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (ATIC, XPNPEP1; 2/57)

### Novelty

The module may be a new tissue-pair co-abundance observation, but novelty is not established as a new molecular complex or pathway. Supporting reasons are the absence of a globally significant GO or KEGG term, the lack of STRING functional enrichment, the sparse overlap with high-confidence STRING interactions, and the fact that only ATIC and XPNPEP1 share the listed hu.MAP complex C1. However, absence from STRING or hu.MAP cannot prove novelty because those resources emphasize experimentally supported physical or functional relationships and may miss tissue-specific co-regulation, transient interactions, abundance coupling, and technical or cellular-composition effects. The most cautious claim is that this is a potentially novel cross-tissue co-abundance pattern assembled from partly known cellular functions, requiring replication and independent validation.

**Hypothesis.** Hypothesis: in both heart and rectum, a shared intracellular state involving protein folding, proteasome activity, RNA processing, purine production, glucose-to-acetyl-CoA regulation, mitochondrial remodeling, and membrane or vesicle turnover produces coordinated abundance of these proteins. CCT7 may provide a proteostasis-centered hub, with ATIC and XPNPEP1 marking a metabolic or complex-associated branch, while CLIC1 and ANXA2 mark a membrane, vesicle, and redox-associated branch. This could reflect a conserved cellular stress, repair, or remodeling state rather than a single pathway. The hypothesis is consistent with the gene functions and observed network structure, but it is not demonstrated by the enrichment results and could alternatively reflect shared cell composition, sample handling, or correlated expression of broadly used cellular machinery.

### Important genes

#### CCT7

- **Related proteins** (co-abundance neighbors): ATIC (0.86), HNRNPH1 (0.83), XPNPEP1 (0.83), CLIC1 (0.81), DNM1L (0.80); STRING partners: ATIC (0.881)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 has the strongest network position in the module and connects ATIC, HNRNPH1, XPNPEP1, CLIC1, and DNM1L. Established evidence identifies it as a TRiC chaperonin subunit involved in ATP-dependent folding of actin, tubulin, and other proteins, with protein detection in both heart and rectum. Its extensive literature and disease associations make it a strong anchor for interpreting the module as involving proteostasis and structural-cellular maintenance.
- **Conclusion**: Established: CCT7 is a central co-abundance hub with a defined chaperonin function and broad tissue detection. Hypothesis: it may coordinate the module by coupling proteostasis to cytoskeletal, metabolic, membrane, and mitochondrial demands in both tissues.

#### ATIC

- **Related proteins** (co-abundance neighbors): CCT7 (0.86), XPNPEP1 (0.84), BZW2 (0.81); STRING partners: CCT7 (0.881)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, rectum
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: 5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase. This gene encodes a bifunctional protein that catalyzes the last two steps of the de novo purine biosynthetic pathway. The N-terminal domain has phosphoribosylaminoimidazolecarboxamide formyltransferase activity, and the C-terminal domain has IMP cyclohydrolase activity. A mutation in this gene results in AICA-ribosiduria. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: AICA-ribosiduria (0.708); cancer (0.571); Intellectual disability (0.463); lung adenocarcinoma (0.390); anaplastic large cell lymphoma (0.374)
- **Europe PMC papers**: 5200
- **Why important**: ATIC is connected to CCT7, XPNPEP1, and BZW2 and is one of the two module members in hu.MAP complex C1. It is a bifunctional enzyme catalyzing the final steps of de novo purine biosynthesis, and it has strong disease and literature coverage in the supplied evidence. The high-confidence STRING relationship with CCT7 provides an independent known link within the module.
- **Conclusion**: Established: ATIC supplies a clear nucleotide-biosynthesis function and participates in a known complex context with XPNPEP1. Hypothesis: coordinated ATIC abundance may indicate demand for nucleotide production during repair, proliferation, or metabolic adaptation, although the module does not prove any of these states.

#### ANXA2

- **Related proteins** (co-abundance neighbors): CLIC1 (0.82); STRING partners: CLIC1 (0.713)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A2. This gene encodes a member of the annexin family. Members of this calcium-dependent phospholipid-binding protein family play a role in the regulation of cellular growth and in signal transduction pathways. This protein functions as an autocrine factor which heightens osteoclast formation and bone resorption. This gene has three pseudogenes located on chromosomes 4, 9 and 10, respectively. Multiple…
- **Diseases (Open Targets)**: neurodegenerative disease (0.443); Alzheimer disease (0.312); Parkinson disease (0.298); lysosomal storage disease (0.289); benign urinary system neoplasm (0.270)
- **Europe PMC papers**: 12966
- **Why important**: ANXA2 is the module gene with the clearest extracellular and blood-related caveat. It is secreted to blood, is plasma-membrane associated, has group-enriched blood-cell expression, and is tissue enhanced in esophagus. Its known functions include membrane raft assembly, receptor recycling, vesicle budding, adhesion, and angiogenesis. It forms the documented STRING relationship with CLIC1, giving the module a supported membrane-associated substructure, despite ANXA2 having a peripheral position in the co-abundance graph.
- **Conclusion**: Established: ANXA2 can represent membrane, vesicle, adhesion, and possible blood or epithelial contributions, and its relationship with CLIC1 is supported by STRING. Hypothesis: the ANXA2-CLIC1 branch may reflect epithelial or vascular remodeling shared between the sampled tissues, but contamination or cellular composition must be excluded.

#### PDK1

- **Related proteins** (co-abundance neighbors): PSMD13 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in heart, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyruvate dehydrogenase kinase 1. Pyruvate dehydrogenase (PDH) is a mitochondrial multienzyme complex that catalyzes the oxidative decarboxylation of pyruvate and is one of the major enzymes responsible for the regulation of homeostasis of carbohydrate fuels in mammals. The enzymatic activity is regulated by a phosphorylation/dephosphorylation cycle. Phosphorylation of PDH by a specific pyruvate dehydrogenase kinase (PDK) results …
- **Diseases (Open Targets)**: prostate carcinoma (0.398); brain cancer (0.331); Crohn disease (0.282); liver disorder (0.261); Congenital lactic acidosis (0.259)
- **Europe PMC papers**: 21294
- **Why important**: PDK1 is peripheral in the module network but biologically important because it regulates pyruvate dehydrogenase, oxidative decarboxylation of pyruvate, and glucose metabolism. It is detected in both heart and rectum and has extensive literature and disease associations. Its position suggests that it may be a metabolic correlate rather than a network hub.
- **Conclusion**: Established: PDK1 provides a plausible energy-metabolism component and is present in both tissues. Hypothesis: its co-abundance may reflect a shift in fuel utilization or stress-related metabolic regulation that accompanies the broader module state, but the network does not establish causal metabolic rewiring.

#### DNM1L

- **Related proteins** (co-abundance neighbors): CCT7 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in heart, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 1L. This gene encodes a member of the dynamin superfamily of GTPases. The encoded protein mediates mitochondrial and peroxisomal division, and is involved in developmentally regulated apoptosis and programmed necrosis. Dysfunction of this gene is implicated in several neurological disorders, including Alzheimer's disease. Mutations in this gene are associated with the autosomal dominant disorder, ence…
- **Diseases (Open Targets)**: encephalopathy, lethal, due to defective mitochondrial peroxisomal fission 1 (0.815); autosomal dominant optic atrophy, classic form (0.721); neurodegenerative disease (0.531); encephalopathy due to mitochondrial and peroxisomal fission defect (0.455); hereditary disease (0.451)
- **Europe PMC papers**: 3015
- **Why important**: DNM1L connects to CCT7 and encodes a dynamin-family GTPase involved in mitochondrial and peroxisomal division, organelle organization, and apoptosis-related mitochondrial fragmentation. HPA reports low tissue and cell-type specificity with detection in both heart and rectum. Its established organelle-remodeling function complements the module's chaperone, metabolic, and membrane-associated components.
- **Conclusion**: Established: DNM1L contributes a defined mitochondrial and peroxisomal dynamics function and is linked to the module through CCT7. Hypothesis: the module could accompany organelle remodeling during cellular maintenance or stress, but no direct evidence shows that DNM1L regulates the other module genes.

## Module 1

**Tissue pair**: heart and rectum  
**Genes (9)**: AIMP2, CYRIB, EIF3L, SHMT2, HNRNPL, PSMC6, RUVBL2, CCT8, TIMM50

### Function

The module most plausibly reflects a broad intracellular proteostasis and gene-expression maintenance program rather than a sharply specialized tissue pathway. Its central hub, CCT8, connects protein folding with AIMP2-linked complex assembly, SHMT2-linked one-carbon metabolism, PSMC6-linked proteasomal degradation, RUVBL2-linked DNA repair and telomere maintenance, EIF3L-linked translation initiation, and HNRNPL-linked RNA processing. The two connected components around CCT8 and PSMC6, together with the RUVBL2-HNRNPL links, are consistent with coordinated management of protein production, RNA handling, mitochondrial function, genome maintenance, and protein quality control. However, no GO or KEGG term passed global correction, so this is an interpretation of the gene functions and network topology, not a globally significant pathway-enrichment result. The absence of a significant enrichment term does not invalidate the module.

**Cell composition.** The module is not composed of plasma or secreted proteins: the fact sheet reports no secreted genes. It is also not blood-cell enriched by the HPA summary, since every gene has low immune-cell specificity and no enriched blood-cell category is reported. Most genes have low tissue specificity, and all module proteins are detected in rectum while most are detected in heart, supporting broad cellular presence in both tissues. At the same time, several genes show cell-type-enhanced or tissue-enhanced patterns, including skeletal muscle, liver, testis, microglia, spermatogenic cells, neutrophil-lineage cells, and esophageal cells. These dispersed HPA patterns do not support a simple shared blood-contamination explanation, but they do suggest that the module may reflect a widely used intracellular program whose abundance can vary with cellular composition. The testis, spermatogenic, microglial, and neutrophil-related HPA signals should therefore be treated as context clues rather than evidence that the heart-rectum module is driven by one of those cell types.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING evidence is sparse: the only high-confidence relationship reported within the module is CCT8-RUVBL2, while no STRING functional-enrichment result is available. This relationship supports a connection between the module’s principal folding-related hub and the RUVBL2 genome-maintenance factor, but it does not establish the entire co-abundance structure as a physical complex. No hu.MAP complex contains multiple module members. The remaining module edges are therefore co-abundance relationships without corresponding high-confidence STRING or hu.MAP support in the supplied evidence. Known interaction evidence is consequently concentrated around CCT8 and RUVBL2, whereas the broader module may represent coordinated abundance across several intracellular systems rather than one established multiprotein complex.

**STRING interactions (score >= 0.7)**: 1 of 36 gene pairs: CCT8–RUVBL2 (0.776)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears to be a potentially novel tissue-shared co-abundance module, but novelty cannot be claimed as a newly discovered molecular complex or pathway. The case for novelty is that the complete gene combination and its heart-rectum co-abundance pattern are not supported by a multi-member hu.MAP complex, and STRING provides only one high-confidence internal relationship with no functional-enrichment result. Those observations indicate that the network-level association may not be a previously catalogued complex. They do not prove novelty: several individual genes have well-established functions, extensive literature, and known biological links to translation, folding, RNA processing, proteasomal control, mitochondria, and genome maintenance. The defensible conclusion is that the shared tissue co-abundance configuration may be novel, while its component biology is largely established.

**Hypothesis.** Hypothesis: the module represents a coordinated intracellular maintenance state shared by heart and rectum, in which protein folding and assembly centered on CCT8 are coupled to RNA processing, translation initiation, proteasomal turnover, mitochondrial protein import and one-carbon metabolism, and RUVBL2-associated genome maintenance. In this model, variation in cellular stress, biosynthetic demand, or tissue cell composition could cause these genes to rise and fall together without requiring them to form one physical complex. The CCT8-RUVBL2 relationship provides a plausible molecular bridge, while the other edges may reflect coordinated regulation or shared abundance constraints. This hypothesis requires validation with independent cohorts, perturbation experiments, and orthogonal protein or interaction measurements.

### Important genes

#### CCT8

- **Related proteins** (co-abundance neighbors): AIMP2 (0.91), SHMT2 (0.89), PSMC6 (0.85), RUVBL2 (0.84), EIF3L (0.83), HNRNPL (0.81); STRING partners: RUVBL2 (0.776)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in heart, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is the dominant network hub, connecting the largest portion of the module to AIMP2, SHMT2, PSMC6, RUVBL2, EIF3L, and HNRNPL. Its annotated role as a subunit of the CCT chaperonin places protein folding and assembly at the center of the network. It is detected in both tissues, has broad tissue specificity, and has the largest literature volume among the listed genes. Its disease and cancer associations also make it a biologically prominent candidate for follow-up.
- **Conclusion**: Established evidence supports CCT8 as the topological anchor of the module and as a protein-folding factor. It is reasonable to hypothesize that CCT8 helps organize the shared intracellular maintenance state, but the co-abundance network does not by itself prove that CCT8 regulates the other genes or that all module edges are direct physical interactions.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): CCT8 (0.84), HNRNPL (0.82); STRING partners: CCT8 (0.776)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 is connected to CCT8 and HNRNPL and is the only gene pair in the module supported by a reported high-confidence STRING interaction. Its annotated functions include DNA repair, DNA recombination, DNA replication regulation, telomere maintenance, and snoRNP assembly. It is tissue-enhanced in testis and detected in rectum, so it also provides a possible explanation for part of the module’s cell-state sensitivity.
- **Conclusion**: Established evidence supports RUVBL2 as a genome-maintenance and nucleic-acid-associated factor with a known relationship to CCT8 in the supplied STRING evidence. Its role as a bridge between proteostasis and genome maintenance in this module remains a hypothesis rather than a demonstrated mechanism.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): RUVBL2 (0.82), CCT8 (0.81), AIMP2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL has connections to RUVBL2, CCT8, and AIMP2 and is annotated for RNA processing, mRNA processing, and regulation of alternative splicing. It is detected in both tissues and has a substantial literature base. Its network position makes it a plausible link between the module’s protein-folding core and post-transcriptional gene regulation.
- **Conclusion**: Established evidence supports HNRNPL as an RNA-processing factor and as a well-connected member of the module. It may couple transcript handling to the abundance of proteostasis and genome-maintenance proteins, but that coupling is a hypothesis not directly demonstrated by the supplied data.

#### PSMC6

- **Related proteins** (co-abundance neighbors): TIMM50 (0.87), CCT8 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in heart, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 6. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.606); mantle cell lymphoma (0.542); neoplasm (0.528); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 748
- **Why important**: PSMC6 connects CCT8 with TIMM50 and is an ATPase subunit of the proteasome regulatory particle. Its annotations include proteasomal protein catabolism, ubiquitin-dependent degradation, ER-associated degradation, and response to oxidative stress. It is detected in both tissues, making it a strong candidate for interpreting the module as a protein-quality-control program rather than a tissue-specific secreted or immune signal.
- **Conclusion**: Established evidence supports PSMC6 as a proteasomal degradation factor linked to protein quality control and oxidative stress responses. Its placement beside CCT8 and TIMM50 supports a hypothesis of coordinated folding, turnover, and mitochondrial maintenance, but does not establish direct regulation among these proteins.

#### SHMT2

- **Related proteins** (co-abundance neighbors): CCT8 (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine hydroxymethyltransferase 2. This gene encodes the mitochondrial form of a pyridoxal phosphate-dependent enzyme that catalyzes the reversible reaction of serine and tetrahydrofolate to glycine and 5,10-methylene tetrahydrofolate. The encoded product is primarily responsible for glycine synthesis. The activity of the encoded protein has been suggested to be the primary source of intracellular glycine. The gene which encodes th…
- **Diseases (Open Targets)**: neurodevelopmental disorder with cardiomyopathy, spasticity, and brain abnormalities (0.771); microcephaly (0.370); polymicrogyria (0.370); neurodevelopmental disorder (0.336); hereditary disease (0.192)
- **Europe PMC papers**: 2579
- **Why important**: SHMT2 is directly connected to CCT8 and contributes mitochondrial one-carbon metabolism, glycine biosynthesis, and serine metabolism. It is tissue-enhanced in liver and has a substantial literature base, with disease associations involving neurodevelopment and cardiomyopathy. Its mitochondrial localization broadens the module beyond nucleoplasmic and cytosolic proteostasis toward metabolic support of cellular maintenance.
- **Conclusion**: Established evidence supports SHMT2 as a mitochondrial enzyme in serine, glycine, and one-carbon metabolism. Its co-abundance with CCT8 may indicate that folding capacity tracks metabolic demand or mitochondrial stress, but this interpretation remains a hypothesis and is not supported by a globally significant enrichment term.

## Module 2

**Tissue pair**: heart and rectum  
**Genes (6)**: AMBP, AOC3, BAG3, LAMA5, NID2, TNS1

### Function

The module most plausibly represents extracellular-matrix and basement-membrane organization linked to cell adhesion, focal-adhesion signaling, and vascular or stromal cell biology. NID2 is the central co-abundance hub and is a basement-membrane adhesion protein; LAMA5 is a laminin component; and TNS1 localizes to focal adhesions and links actin to the extracellular matrix. AOC3 adds a vascular and stromal adhesion, amine-metabolism, and inflammatory dimension, while BAG3 contributes a muscle-associated proteostasis and stress-response dimension. AMBP may represent a circulating or liver-derived component rather than a core intracellular member. No GO or KEGG term passed global correction, so this interpretation is based on the individual gene annotations, HPA localization, network structure, and the single high-confidence STRING relationship rather than on statistically significant pathway enrichment. The absence of enrichment does not invalidate the module.

**Cell composition.** The module is not a simple immune-cell module: most genes are not detected in immune cells, although BAG3 is immune-cell enhanced and TNS1 is group enriched in monocyte populations. The HPA pattern is strongly compatible with vascular, stromal, contractile, and adipose-associated cells, especially pericytes, smooth-muscle cells, adipocytes, and hepatic stellate cells. NID2 and LAMA5 are extracellular-matrix or basement-membrane proteins, and AMBP is secreted to blood and enriched in liver hepatocytes. Thus, the shared heart–rectum signal could partly reflect common vascular or stromal cell content, extracellular matrix abundance, or blood-derived material. AOC3, TNS1, and NID2 show vascular or stromal associations, whereas BAG3 is associated with skeletal muscle and smooth muscle. Protein detection in both tissues supports some shared tissue presence, but the lack of detection for several genes in one or both tissues cautions against interpreting every co-abundance link as local production by the same cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The network contains one high-confidence known STRING relationship: LAMA5–NID2. This is biologically coherent because laminin and nidogen are basement-membrane components. The remaining co-abundance edges do not have high-confidence STRING support in the supplied results, and STRING functional enrichment is absent. No hu.MAP complex contains multiple module members. Therefore, the network is better viewed as a co-abundance association centered on an extracellular-matrix hub than as a recovered canonical protein complex. The known LAMA5–NID2 relationship provides a mechanistic anchor, but it does not establish direct physical interaction for the other module pairs.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: LAMA5–NID2 (0.849)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may contain a novel tissue-shared co-abundance pattern, particularly the association of NID2 with BAG3, TNS1, AMBP, and LAMA5 in heart and rectum. However, it cannot be called a definitively new biological mechanism from these data alone. The limited STRING support, absence of a multi-member hu.MAP complex, lack of globally significant GO or KEGG enrichment, and strong HPA indications of vascular, stromal, and circulating contributions all leave open the possibility that the pattern reflects shared cell composition or sample-level extracellular and blood signals. Absence from STRING or hu.MAP is evidence that the configuration is not represented there, but it is not proof of novelty. Independent replication, cell-type-resolved data, and experimental validation would be required to establish a new mechanism.

**Hypothesis.** Hypothesis: the conserved heart–rectum module reflects coordinated abundance of basement-membrane and focal-adhesion machinery in vascular or stromal cells, with NID2 and LAMA5 forming the extracellular scaffold, TNS1 coupling that scaffold to adhesion-site cytoskeletal signaling, and AOC3 marking a vascular stromal state with adhesive, metabolic, and inflammatory potential. BAG3 may indicate mechanical or proteotoxic stress in contractile cells, while AMBP may be a blood- or liver-derived component associated with the extracellular environment rather than a structural core. Under this model, the shared module arises from common vascular or stromal architecture and circulating material in the two tissues, rather than from a single universal pathway operating identically in every cell.

### Important genes

#### NID2

- **Related proteins** (co-abundance neighbors): BAG3 (0.83), TNS1 (0.82), LAMA5 (0.82), AMBP (0.81); STRING partners: LAMA5 (0.849)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in heart, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nidogen 2. This gene encodes a member of the nidogen family of basement membrane proteins. This protein is a cell-adhesion protein that binds collagens I and IV and laminin and may be involved in maintaining the structure of the basement membrane.[provided by RefSeq, Jun 2010].
- **Diseases (Open Targets)**: hearing loss disorder (0.474); benign colon neoplasm (0.439); presbycusis (0.436); sensorineural hearing loss disorder (0.436); Tinnitus (0.360)
- **Europe PMC papers**: 1495
- **Why important**: NID2 is the central network hub, connecting the extracellular-matrix, focal-adhesion, and circulating-protein portions of the module. Its established function is as a basement-membrane nidogen that binds collagen and laminin and supports cell-matrix organization. It is detected in both heart and rectum, is associated with adipocytes and cardiomyocytes, and has substantial literature support. Its direct STRING relationship with LAMA5 gives the module its clearest known molecular anchor.
- **Conclusion**: Established evidence supports NID2 as the principal extracellular-matrix organizer and the most informative representative of the module. The hypothesis that it coordinates the other module members in a shared heart–rectum mechanism remains unproven because most of its co-abundance partners lack corresponding known physical interactions.

#### LAMA5

- **Related proteins** (co-abundance neighbors): AOC3 (0.84), NID2 (0.82); STRING partners: NID2 (0.849)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit alpha 5. This gene encodes one of the vertebrate laminin alpha chains. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins are composed of 3 non identical chains: l…
- **Diseases (Open Targets)**: nephrotic syndrome, IIa 26 (0.761); bent bone dysplasia syndrome 2 (0.563); colorectal cancer (0.491); LAMA5-related multisystemic syndrome (0.475); polyp of colon (0.467)
- **Europe PMC papers**: 2881
- **Why important**: LAMA5 is a major basement-membrane laminin subunit with functions in cell adhesion, integrin signaling, migration, and organ morphogenesis. It is directly linked to NID2 by high-confidence STRING evidence and connects to AOC3 in the co-abundance network. Its broad tissue specificity and association with podocytes, alveolar cells, and endometrial cells suggest a structural extracellular role rather than a narrowly tissue-restricted signal. It also has extensive disease and literature annotation.
- **Conclusion**: Established evidence supports LAMA5 as a structural and signaling component of basement membranes and as the strongest known partner of NID2. Its role as a driver of the shared heart–rectum co-abundance pattern is a hypothesis, particularly because protein detection differs between the two tissues.

#### TNS1

- **Related proteins** (co-abundance neighbors): NID2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Focal adhesion sites; IHC detected in heart, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tensin 1. The protein encoded by this gene localizes to focal adhesions, regions of the plasma membrane where the cell attaches to the extracellular matrix. This protein crosslinks actin filaments and contains a Src homology 2 (SH2) domain, which is often found in molecules involved in signal transduction. This protein is a substrate of calpain II. Alternative splicing results in multiple transcript variant…
- **Diseases (Open Targets)**: coronary artery disorder (0.555); chronic obstructive pulmonary disease (0.550); myocardial infarction (0.513); aortic stenosis (0.462); breast cancer (0.443)
- **Europe PMC papers**: 1434
- **Why important**: TNS1 provides the clearest intracellular connection from extracellular matrix to adhesion-site cytoskeletal organization. It localizes to focal adhesions, crosslinks actin, and is associated with fibroblast migration and cell-matrix adhesion. Its HPA profile points toward blood vessels, pericytes, and contractile or stromal cell populations, and it is detected in both tissues. Its position adjacent to the NID2 hub makes it important despite not having a known STRING partner in this module.
- **Conclusion**: Established evidence supports TNS1 as a focal-adhesion and actin-coupling component consistent with the proposed vascular or stromal interpretation. The idea that TNS1 transmits a NID2- or LAMA5-dependent mechanical signal in this module remains a mechanistic hypothesis.

#### AOC3

- **Related proteins** (co-abundance neighbors): LAMA5 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: amine oxidase copper containing 3. This gene encodes a member of the semicarbazide-sensitive amine oxidase family. Copper amine oxidases catalyze the oxidative conversion of amines to aldehydes in the presence of copper and quinone cofactor. The encoded protein is localized to the cell surface, has adhesive properties as well as monoamine oxidase activity, and may be involved in leukocyte trafficking. Alterations in levels of the e…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.265); metabolic syndrome (0.220); neoplasm (0.105); cancer (0.102); diabetes mellitus (0.089)
- **Europe PMC papers**: 1367
- **Why important**: AOC3 connects to LAMA5 in the co-abundance network and is enriched in blood-vessel and adipose-associated contexts, including pericytes and hepatic stellate cells. Its annotated activities include cell adhesion, inflammatory response, and copper-dependent amine oxidation. It therefore adds a vascular metabolic and inflammatory dimension that is not captured by the basement-membrane genes alone. Its substantial literature and disease associations make it biologically informative even though it lacks a high-confidence STRING partner here.
- **Conclusion**: Established evidence supports AOC3 as an adhesion-associated amine oxidase linked to vascular and stromal biology. Its inclusion may reflect a shared vascular state or extracellular environment, but a direct functional connection to LAMA5 in this module is not established.

#### BAG3

- **Related proteins** (co-abundance neighbors): NID2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in heart, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BAG cochaperone 3. BAG proteins compete with Hip for binding to the Hsc70/Hsp70 ATPase domain and promote substrate release. All the BAG proteins have an approximately 45-amino acid BAG domain near the C terminus but differ markedly in their N-terminal regions. The protein encoded by this gene contains a WW domain in the N-terminal region and a BAG domain in the C-terminal region. The BAG domains of BAG1, BAG2, and …
- **Diseases (Open Targets)**: dilated cardiomyopathy 1HH (0.821); myofibrillar myopathy 6 (0.789); dilated cardiomyopathy (0.726); familial isolated dilated cardiomyopathy (0.678); heart failure (0.654)
- **Europe PMC papers**: 4304
- **Why important**: BAG3 is the module member most clearly associated with muscle biology and cellular stress management. It supports HSP-mediated protein handling, autophagosome assembly, and protection from striated-muscle apoptosis, and it is associated with dilated cardiomyopathy, myofibrillar myopathy, and heart failure. Its co-abundance link to NID2 and detection in both tissues suggest that the module may couple extracellular-matrix state to contractile-cell proteostasis. It also has the strongest literature support among the selected genes.
- **Conclusion**: Established evidence supports BAG3 as a muscle-relevant proteostasis and stress-response protein with important cardiac disease associations. Its relationship with the extracellular-matrix hub is a hypothesis and could alternatively reflect shared smooth-muscle or contractile-cell abundance.

#### AMBP

- **Related proteins** (co-abundance neighbors): NID2 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alpha-1-microglobulin/bikunin precursor. This gene encodes a complex glycoprotein secreted in plasma. The precursor is proteolytically processed into distinct functioning proteins: alpha-1-microglobulin, which belongs to the superfamily of lipocalin transport proteins and may play a role in the regulation of inflammatory processes, and bikunin, which is a urinary trypsin inhibitor belonging to the superfamily of Kunitz-type protease inhi…
- **Diseases (Open Targets)**: systemic lupus erythematosus (0.086); ovarian neoplasm (0.072); posterior cortical atrophy (0.064); breast carcinoma (0.060); diabetes mellitus (0.060)
- **Europe PMC papers**: 1653
- **Why important**: AMBP is a liver-enriched hepatocyte product secreted into blood and processed into proteins involved in inflammatory regulation and protease inhibition. It is connected to NID2 in the co-abundance network but is not detected in heart or rectum by the supplied HPA immunohistochemistry summary. This makes it important for interpreting module composition: it may represent plasma carryover or a systemic signal rather than a resident structural component. Its literature and disease annotations provide additional biological context.
- **Conclusion**: Established evidence supports AMBP as a circulating, liver-derived glycoprotein precursor rather than a core heart–rectum cellular component. Its co-abundance with NID2 may indicate shared extracellular or blood content, but any direct mechanistic role in the proposed tissue module is speculative.

## Module 3

**Tissue pair**: heart and rectum  
**Genes (11)**: ATP2B4, CALD1, CSRP1, FLNA, ITGB1, KANK2, MYH11, NEXN, NID1, SUN2, TLN1

### Function

The module is best interpreted as a contractile, adhesive actin-cytoskeleton program. The primary evidence is the strong and overlapping enrichment for cytoskeleton organization, actin filament-based processes, actin cytoskeleton organization, and cytoskeletal protein binding ((GO:BP cytoskeleton organization; q_global = 0.00394), (GO:BP actin filament-based process; q_global = 0.00689), (GO:BP actin cytoskeleton organization; q_global = 0.0237), (GO:MF cytoskeletal protein binding; q_global = 0.0348)). The represented proteins connect actin filaments to membrane adhesion complexes, regulate cell shape and migration, support smooth-muscle contractility, connect the cytoskeleton to the nuclear envelope, and maintain calcium-dependent contractile control. Together, the module is consistent with structural force transmission and mechanosensitive adhesion in vascular, smooth-muscle, stromal, and cardiomuscular cells.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: HPA identifies only NID1 as secreted to the extracellular matrix, while the other genes are intracellular or membrane-associated. The module is also not broadly immune-cell enriched. Most genes show tissue or cell-type enrichment, especially in smooth-muscle cells, vascular smooth-muscle cells, hepatic stellate cells, and related stromal or contractile populations. Blood-cell specificity is generally low or absent, although some genes have megakaryocyte or platelet-related patterns and CALD1 has an immune-cell-enriched annotation. The shared heart-rectum signal therefore more plausibly reflects conserved resident vascular, smooth-muscle, stromal, or contractile cell populations than a generic blood or secreted-protein signature. HPA protein detection is more frequent in rectum than heart, so transcript-level co-abundance should not be assumed to imply equal protein abundance in both tissues.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP cytoskeleton organization | 0.00394 | CALD1, CSRP1, FLNA, ITGB1, KANK2, MYH11, NEXN, SUN2, TLN1 |
| GO:BP actin filament-based process | 0.00689 | CALD1, CSRP1, FLNA, ITGB1, KANK2, MYH11, SUN2, TLN1 |
| GO:BP actin cytoskeleton organization | 0.0237 | CALD1, CSRP1, FLNA, ITGB1, KANK2, MYH11, TLN1 |
| GO:MF cytoskeletal protein binding | 0.0348 | CALD1, CSRP1, FLNA, ITGB1, MYH11, NEXN, SUN2, TLN1 |

### STRING and hu.MAP

STRING supports a known structural core rather than an isolated statistical association. The strongest relationships include FLNA with ITGB1 and TLN1, ITGB1 with TLN1, and CALD1 with MYH11. These links are biologically coherent with integrin adhesion, actin crosslinking, talin-dependent attachment, and smooth-muscle contractility. STRING functional enrichment independently supports cytoskeletal protein binding ((STRING Function Cytoskeletal protein binding; within-query FDR = 0.0303)), but it is supplementary and does not replace the globally corrected GO evidence. hu.MAP identifies ITGB1 and ATP2B4 together in two membrane-associated complexes ((hu.MAP huMAP3_10980.1), (hu.MAP huMAP3_09336.1)). Because only a small subset of each large complex is represented, these hu.MAP results support possible membrane-complex context but do not establish that the entire module is one physical complex. Most module genes lack hu.MAP assignments and many lack high-confidence STRING pairings, indicating a functionally coherent co-abundance program assembled from several related structural subsystems rather than a single canonical complex.

**STRING interactions (score >= 0.7)**: 4 of 55 gene pairs: CALD1–MYH11 (0.946); FLNA–ITGB1 (0.993); FLNA–TLN1 (0.998); ITGB1–TLN1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Cytoskeletal protein binding (FDR = 0.0303, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10980.1 (ITGB1, ATP2B4; 2/44); huMAP3_09336.1 (ITGB1, ATP2B4; 2/50)

### Novelty

The biological components are not new individually: the actin, integrin, talin, smooth-muscle, basement-membrane, and nuclear-envelope functions are established, and several pairwise relationships are already represented in STRING. The potentially new observation is the conserved co-abundance of these components across heart and rectum, particularly the joint association of contractile machinery, adhesion machinery, and cytoskeletal force-transmission components. The fact sheet does not provide a prior cross-tissue module catalog or an independent replication analysis, so this should be described as a plausible candidate for a new conserved module, not as a proven novel biological entity. Absence from STRING or hu.MAP cannot by itself establish novelty.

**Hypothesis.** Hypothesis: the module represents a conserved force-transmission and contractile-support program in vascular or smooth-muscle-rich resident cells of heart and rectum. Integrin and talin may couple the extracellular matrix to actin through FLNA, while MYH11 and CALD1 provide contractile output, NEXN and KANK2 stabilize or regulate actin-associated adhesion structures, SUN2 transmits cytoskeletal forces to the nucleus, ATP2B4 tunes calcium homeostasis, and NID1 contributes basement-membrane context. Coordinated expression could help cells maintain tissue architecture and adapt contraction, adhesion, and nuclear mechanotransduction to local mechanical load. This is a mechanistic model inferred from the annotations and network structure, not a demonstrated causal pathway.

### Important genes

#### FLNA

- **Related proteins** (co-abundance neighbors): CSRP1 (0.88), TLN1 (0.87), MYH11 (0.86), CALD1 (0.84); STRING partners: ITGB1 (0.993), TLN1 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is the most connected and strongest-positioned module member and links several contractile or adhesive genes within the co-abundance network. It is an actin crosslinker that connects actin to membrane glycoproteins and interacts with integrins and receptor complexes. It participates in every primary GO term ((GO:BP cytoskeleton organization; q_global = 0.00394), (GO:BP actin filament-based process; q_global = 0.00689), (GO:BP actin cytoskeleton organization; q_global = 0.0237), (GO:MF cytoskeletal protein binding; q_global = 0.0348)) and in the supplementary STRING term ((STRING Function Cytoskeletal protein binding; within-query FDR = 0.0303)). Its vascular and intestinal tissue enrichment and extensive disease and literature record make it a strong anchor for interpreting the module.
- **Conclusion**: Established evidence supports FLNA as a central actin-to-membrane scaffolding component of the module. Its position makes it a plausible coordinator of adhesion and force transmission, but the fact sheet does not establish that FLNA causally drives the cross-tissue co-abundance pattern.

#### ITGB1

- **Related proteins** (co-abundance neighbors): KANK2 (0.86), TLN1 (0.84); STRING partners: FLNA (0.993), TLN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_10980.1, huMAP3_09336.1
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is a membrane integrin subunit and a direct bridge between extracellular-matrix adhesion and the cytoskeleton. It is connected to FLNA and TLN1 in STRING with very strong support, occurs in all primary GO terms and the STRING term, and is present in both hu.MAP complexes ((hu.MAP huMAP3_10980.1), (hu.MAP huMAP3_09336.1)). Its established roles in cell adhesion, tissue repair, angiogenesis, and immune or epithelial processes give it broad mechanistic relevance.
- **Conclusion**: Established evidence identifies ITGB1 as a core adhesion receptor component that can couple matrix signals to the actin network. In this module, it is a credible interface between extracellular context and intracellular contractile machinery; whether it is the initiating regulator remains a hypothesis.

#### MYH11

- **Related proteins** (co-abundance neighbors): FLNA (0.86), ATP2B4 (0.84), TLN1 (0.81); STRING partners: CALD1 (0.946)
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin heavy chain 11. The protein encoded by this gene is a smooth muscle myosin belonging to the myosin heavy chain family. The gene product is a subunit of a hexameric protein that consists of two heavy chain subunits and two pairs of non-identical light chain subunits. It functions as a major contractile protein, converting chemical energy into mechanical energy through the hydrolysis of ATP. A chromosomal rearrange…
- **Diseases (Open Targets)**: aortic aneurysm, familial thoracic 4 (0.762); megacystis-microcolon-intestinal hypoperistalsis syndrome 2 (0.757); familial thoracic aortic aneurysm and aortic dissection (0.715); visceral myopathy 2 (0.570); neurodegenerative disease (0.527)
- **Europe PMC papers**: 10247
- **Why important**: MYH11 is the principal contractile motor represented in the module and is enriched in vascular and smooth-muscle cell populations. It participates in all primary GO terms and connects in the network to FLNA, TLN1, and ATP2B4. STRING also supports its established relationship with CALD1. Its major role in smooth-muscle contraction, actomyosin organization, and vascular disease gives the module a clear contractile interpretation.
- **Conclusion**: Established evidence supports MYH11 as the module's contractile effector and strongly favors a smooth-muscle or vascular interpretation. Its co-abundance with adhesion and cytoskeletal genes suggests integrated force transmission, but the direction of regulation is not demonstrated.

#### NEXN

- **Related proteins** (co-abundance neighbors): KANK2 (0.90), SUN2 (0.87), NID1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments; IHC detected in heart, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nexilin F-actin binding protein. This gene encodes a filamentous actin-binding protein that may function in cell adhesion and migration. Mutations in this gene have been associated with dilated cardiomyopathy, also known as CMD1CC. Alternatively spliced transcript variants have been described.[provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: dilated cardiomyopathy 1CC (0.792); hypertrophic cardiomyopathy 20 (0.746); familial isolated dilated cardiomyopathy (0.667); hypertrophic cardiomyopathy (0.584); cardiomyopathy, dilated, 2M (0.565)
- **Europe PMC papers**: 1090
- **Why important**: NEXN is a heart-enriched actin-binding protein with a direct network position connecting KANK2, SUN2, and NID1. It occurs in the primary cytoskeleton organization and cytoskeletal protein-binding terms ((GO:BP cytoskeleton organization; q_global = 0.00394), (GO:MF cytoskeletal protein binding; q_global = 0.0348)) and is detected in both heart and rectum by HPA. Its association with dilated and hypertrophic cardiomyopathy makes it especially informative for the heart component of the shared module.
- **Conclusion**: Established evidence supports NEXN as a heart-relevant actin and adhesion stabilizer within the module. Its connection to SUN2 and NID1 supports a possible bridge from cytoskeletal organization to nuclear and basement-membrane context, but that bridge remains a hypothesis.

#### TLN1

- **Related proteins** (co-abundance neighbors): FLNA (0.87), ITGB1 (0.84), MYH11 (0.81); STRING partners: FLNA (0.998), ITGB1 (0.999)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 is a focal-adhesion cytoskeletal protein that activates integrins and promotes cell attachment, spreading, and migration. It is a central member of the known FLNA–ITGB1–TLN1 STRING subnetwork, participates in all primary GO terms and the STRING term, and has a network position linking adhesion to MYH11. Its platelet and megakaryocyte annotations also provide a possible explanation for part of the shared structural signal without implying that the module is blood-derived.
- **Conclusion**: Established evidence supports TLN1 as a key integrin-activation and focal-adhesion component. It likely helps transmit matrix-derived mechanical information into the actin network, while any specific role in coordinating heart and rectum expression remains unproven.

#### CALD1

- **Related proteins** (co-abundance neighbors): FLNA (0.84); STRING partners: MYH11 (0.946)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caldesmon 1. This gene encodes a calmodulin- and actin-binding protein that plays an essential role in the regulation of smooth muscle and nonmuscle contraction. The conserved domain of this protein possesses the binding activities to Ca(2+)-calmodulin, actin, tropomyosin, myosin, and phospholipids. This protein is a potent inhibitor of the actin-tropomyosin activated myosin MgATPase, and serves as a mediating…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.499); diaphragmatic hernia (0.447); glaucoma (0.405); diverticular disease (0.393); open-angle glaucoma (0.390)
- **Europe PMC papers**: 3386
- **Why important**: CALD1 is a calmodulin- and actin-binding regulator of smooth and nonmuscle contraction. It appears in all primary GO terms and the STRING cytoskeletal-binding term, and it has a strong known STRING relationship with MYH11. Its annotation for smooth-muscle contraction and actin-filament bundle assembly gives functional specificity to the otherwise broader cytoskeletal enrichment.
- **Conclusion**: Established evidence supports CALD1 as a regulator of actomyosin contractility and a functional partner of MYH11. It strengthens the interpretation of the module as contractile rather than merely generic cytoskeletal, although its low direct network connectivity means it need not be the module's central organizer.

## Module 4

**Tissue pair**: heart and rectum  
**Genes (21)**: MTHFD1, CLTC, SORD, DHX9, EIF3C, MACROH2A1, H4C1, HNRNPK, HNRNPR, HSP90AA1, IQGAP1, MATR3, DDOST, RPL12, SERPINH1, QARS1, CCT5, CCT3, TFRC, VPS35, XRCC6

### Function

The module is best interpreted as a broadly expressed intracellular gene-expression and proteostasis program, centered on RNA binding and processing, macromolecule biosynthesis, translation-related activity, chromatin and DNA maintenance, and protein folding. The primary evidence is the globally corrected enrichment for nucleic-acid binding (GO:MF nucleic acid binding; q_global = 0.000387), macromolecule biosynthetic process (GO:BP macromolecule biosynthetic process; q_global = 0.00053), RNA binding (GO:MF RNA binding; q_global = 0.00109), DNA metabolic process (GO:BP DNA metabolic process; q_global = 0.00127), chromosome and telomere organization (GO:BP chromosome organization; q_global = 0.00519)(GO:BP telomere organization; q_global = 0.00624), gene expression (GO:BP gene expression; q_global = 0.0105), ribonucleoprotein complex (GO:CC ribonucleoprotein complex; q_global = 0.0411), and mRNA binding (GO:MF mRNA binding; q_global = 0.0465). The strong internal network structure links an RNA-processing group involving DHX9, HNRNPK, HNRNPR, and MATR3 with a chaperone group involving CCT3 and CCT5, while chromatin and DNA-maintenance genes include MACROH2A1, H4C1, and XRCC6. This is therefore more consistent with a coordinated cellular maintenance and gene-expression state than with a narrowly tissue-specific physiological pathway.

**Cell composition.** The module is not dominated by secreted or plasma proteins: only TFRC is annotated as secreted to blood, and SERPINH1 is intracellular and membrane-associated. Most genes have low tissue specificity, and most have low immune-cell specificity according to HPA. Nevertheless, the supplementary STRING tissue results repeatedly point toward hematopoietic, lymphoid, blood, and blood-cancer contexts (STRING TISSUES Hematopoietic cell; within-query FDR = 0.00065) through (STRING TISSUES Leukemia cell; within-query FDR = 0.011). HPA also identifies several cell-type-enhanced genes in erythrocyte progenitors, neutrophils, monocytes, and related populations. This raises a credible possibility that part of the shared heart–rectum signal reflects blood or shared immune and vascular-associated cellular material rather than a specialized program intrinsic to both organs. The broad detection of module proteins in both tissues supports technical and biological detectability, but does not by itself establish that the same cell type generates the signal in each tissue.

**GO/KEGG enrichment**: 17 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleic acid binding | 0.000387 | CCT3, CCT5, CLTC, DHX9, EIF3C, H4C1, HNRNPK, HNRNPR, HSP90AA1, MACROH2A1, MATR3, RPL12, SERPINH1, TFRC, XRCC6 |
| GO:BP macromolecule biosynthetic process | 0.00053 | CCT3, CCT5, CLTC, DDOST, DHX9, EIF3C, HNRNPK, HNRNPR, HSP90AA1, IQGAP1, MACROH2A1, MATR3, QARS1, RPL12, SERPINH1, TFRC, VPS35, XRCC6 |
| GO:MF RNA binding | 0.00109 | CCT3, CCT5, CLTC, DHX9, EIF3C, H4C1, HNRNPK, HNRNPR, HSP90AA1, MATR3, RPL12, SERPINH1, TFRC, XRCC6 |
| GO:BP DNA metabolic process | 0.00127 | CCT3, CCT5, DHX9, HSP90AA1, MACROH2A1, TFRC, XRCC6 |
| GO:BP biosynthetic process | 0.0046 | CCT3, CCT5, CLTC, DDOST, DHX9, EIF3C, HNRNPK, HNRNPR, HSP90AA1, IQGAP1, MACROH2A1, MATR3, MTHFD1, QARS1, RPL12, SERPINH1, SORD, TFRC, VPS35, XRCC6 |
| GO:BP chromosome organization | 0.00519 | CCT3, CCT5, H4C1, HSP90AA1, MACROH2A1, XRCC6 |
| GO:BP telomere organization | 0.00624 | CCT3, CCT5, H4C1, HSP90AA1, XRCC6 |
| GO:BP positive regulation of DNA metabolic process | 0.00624 | CCT3, CCT5, DHX9, HSP90AA1, TFRC |
| GO:BP gene expression | 0.0105 | CCT3, CCT5, DHX9, EIF3C, HNRNPK, HNRNPR, HSP90AA1, IQGAP1, MACROH2A1, MATR3, QARS1, RPL12, SERPINH1, TFRC, VPS35, XRCC6 |
| GO:BP regulation of DNA metabolic process | 0.0116 | CCT3, CCT5, DHX9, HSP90AA1, TFRC |
| GO:BP macromolecule metabolic process | 0.0155 | CCT3, CCT5, CLTC, DDOST, DHX9, EIF3C, HNRNPK, HNRNPR, HSP90AA1, IQGAP1, MACROH2A1, MATR3, QARS1, RPL12, SERPINH1, TFRC, VPS35, XRCC6 |
| GO:BP regulation of macromolecule biosynthetic process | 0.0157 | CCT3, CCT5, CLTC, DHX9, EIF3C, HNRNPK, HSP90AA1, IQGAP1, MACROH2A1, MATR3, QARS1, TFRC, VPS35, XRCC6 |
| GO:CC ribonucleoprotein complex | 0.0411 | DHX9, EIF3C, HNRNPK, HNRNPR, IQGAP1, RPL12 |
| GO:BP positive regulation of macromolecule metabolic process | 0.0422 | CCT3, CCT5, DHX9, EIF3C, HNRNPK, HSP90AA1, IQGAP1, MACROH2A1, TFRC, VPS35, XRCC6 |
| GO:BP regulation of biosynthetic process | 0.0436 | CCT3, CCT5, CLTC, DHX9, EIF3C, HNRNPK, HSP90AA1, IQGAP1, MACROH2A1, MATR3, QARS1, TFRC, VPS35, XRCC6 |

### STRING and hu.MAP

STRING supports several established relationships within the module. The CCT3–CCT5 and CCT–HSP90AA1 relationships support chaperone and protein-folding biology. DHX9 is connected to HNRNPK, HNRNPR, MATR3, and XRCC6, while HNRNPK, HNRNPR, and MATR3 form a coherent RNA-processing neighborhood. MACROH2A1 is linked to H4C1 and XRCC6, consistent with chromatin and DNA-maintenance biology. CLTC–TFRC supports receptor endocytosis and intracellular trafficking. hu.MAP independently supports an HNRNPR–MATR3–HNRNPK complex (hu.MAP huMAP3_10625.1), multiple CCT3–CCT5-containing complexes (hu.MAP huMAP3_01951.1)(hu.MAP huMAP3_07938.1)(hu.MAP huMAP3_06559.1)(hu.MAP huMAP3_09191.1)(hu.MAP huMAP3_10656.1)(hu.MAP huMAP3_14584.1), additional hnRNP complexes (hu.MAP huMAP3_07581.1)(hu.MAP huMAP3_10659.1), and a MACROH2A1–H4C1 chromatin complex (hu.MAP huMAP3_10862.1). These concordant relationships indicate that the module is not merely an arbitrary correlation cluster: several subnetworks correspond to known molecular assemblies. However, many module edges are not represented by high-confidence STRING interactions, so the full co-abundance structure should not be equated with a physical protein complex.

**STRING interactions (score >= 0.7)**: 14 of 210 gene pairs: CCT3–CCT5 (0.999); CCT3–HSP90AA1 (0.767); CCT5–HSP90AA1 (0.868); CLTC–TFRC (0.84); DHX9–HNRNPK (0.939); DHX9–HNRNPR (0.909); DHX9–MATR3 (0.786); DHX9–XRCC6 (0.819); H4C1–MACROH2A1 (0.943); HNRNPK–HNRNPR (0.962); HNRNPK–MATR3 (0.923); HNRNPK–XRCC6 (0.738); HNRNPR–MATR3 (0.714); MACROH2A1–XRCC6 (0.769)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Nucleic acid binding (FDR = 0.00025, 15 genes); Function RNA binding (FDR = 0.00046, 14 genes); TISSUES Hematopoietic cell (FDR = 0.00065, 13 genes); TISSUES Lymphocyte (FDR = 0.00065, 12 genes); TISSUES Lymphoblast (FDR = 0.001, 9 genes); TISSUES Lymphoid tissue (FDR = 0.0011, 13 genes); TISSUES Blood (FDR = 0.0017, 16 genes); TISSUES Blood cancer cell (FDR = 0.0018, 12 genes); TISSUES Hematopoietic system (FDR = 0.0048, 17 genes); TISSUES Leukemia cell (FDR = 0.011, 10 genes); TISSUES Internal male genital organ (FDR = 0.011, 13 genes); Function Heterocyclic compound binding (FDR = 0.0115, 18 genes); Function Organic cyclic compound binding (FDR = 0.012, 18 genes); Function mRNA binding (FDR = 0.0168, 5 genes); Function DNA binding (FDR = 0.0194, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10625.1 (HNRNPR, MATR3, HNRNPK; 3/57); huMAP3_01951.1 (CCT5, CCT3; 2/8); huMAP3_07581.1 (HNRNPR, MATR3; 2/21); huMAP3_07938.1 (CCT5, CCT3; 2/23); huMAP3_06559.1 (CCT5, CCT3; 2/25); huMAP3_10659.1 (HNRNPR, HNRNPK; 2/28); huMAP3_09191.1 (CCT5, CCT3; 2/32); huMAP3_10862.1 (MACROH2A1, H4C1; 2/33); huMAP3_10656.1 (CCT5, CCT3; 2/36); huMAP3_14584.1 (CCT5, CCT3; 2/61)

### Novelty

The module should not be called a wholly new molecular pathway. Its principal components and several relationships are already well established through STRING, hu.MAP, gene annotations, and extensive literature, particularly the hnRNP RNA-processing group, the CCT chaperonin group, chromatin components, and TFRC-associated endocytosis. The potentially novel finding is the conserved co-abundance organization of these established components across heart and rectum, especially the way RNA processing, chromatin maintenance, chaperoning, translation, trafficking, and possible blood-cell contributions are combined. Absence of some genes from STRING or hu.MAP does not demonstrate novelty, because those resources emphasize physical interactions or curated complexes rather than tissue-pair co-abundance. A claim of novelty would require independent replication, comparison with published tissue co-expression modules, and cell-composition-aware validation.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular-maintenance state in which RNA processing and transport, translation, chaperone-assisted protein folding, chromatin organization, and DNA repair are coordinated. DHX9 and the hnRNP proteins may organize RNA metabolism and transcriptional output; MACROH2A1, H4C1, and XRCC6 may connect this state to chromatin and genome maintenance; CCT3 and CCT5 may buffer the increased demand for folding and stabilization of cellular proteins. TFRC and CLTC may indicate accompanying endocytic and iron-uptake activity. A competing or complementary hypothesis is that blood-derived or immune-associated cells contribute substantially to the shared signal, given the STRING tissue enrichments and HPA cell-type evidence. These are mechanistic hypotheses, not demonstrations of direct regulation or physical interaction among every module member.

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): MATR3 (0.92), CLTC (0.91), TFRC (0.88), CCT3 (0.88), HNRNPK (0.86), MACROH2A1 (0.85), HNRNPR (0.84), SERPINH1 (0.82); STRING partners: HNRNPK (0.939), HNRNPR (0.909), MATR3 (0.786), XRCC6 (0.819)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is a central network connector linking the RNA-binding proteins HNRNPK, HNRNPR, and MATR3 with XRCC6, CCT3, CLTC, TFRC, MACROH2A1, and SERPINH1. It is included in nearly all of the module's core globally corrected functional themes, including RNA binding, DNA metabolism, gene expression, ribonucleoprotein complexes, and mRNA binding (GO:MF nucleic acid binding; q_global = 0.000387)(GO:MF RNA binding; q_global = 0.00109)(GO:BP DNA metabolic process; q_global = 0.00127)(GO:BP positive regulation of DNA metabolic process; q_global = 0.00624)(GO:BP gene expression; q_global = 0.0105)(GO:CC ribonucleoprotein complex; q_global = 0.0411)(GO:MF mRNA binding; q_global = 0.0465). Its established helicase, transcriptional-regulatory, RNA-processing, and nucleic-acid functions make it a strong candidate for connecting the module's RNA and genome-maintenance components. It also has a substantial disease and literature record.
- **Conclusion**: Established evidence supports DHX9 as an important RNA and nucleic-acid metabolism component and as a network bridge. It is plausible, but not proven, that DHX9 helps coordinate the RNA-processing and DNA-maintenance aspects of this module in both tissues.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): DDOST (0.89), MATR3 (0.87), DHX9 (0.86), VPS35 (0.84), SERPINH1 (0.84), CCT3 (0.84); STRING partners: DHX9 (0.939), HNRNPR (0.962), MATR3 (0.923), XRCC6 (0.738)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, rectum
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_10659.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is part of the densest known interaction neighborhood in the module, with established STRING relationships to DHX9, HNRNPR, MATR3, and XRCC6, and membership in hu.MAP RNA-binding complexes (hu.MAP huMAP3_10625.1)(hu.MAP huMAP3_10659.1). It contributes to globally corrected nucleic-acid binding, RNA binding, macromolecule biosynthesis, gene expression, ribonucleoprotein complex, and mRNA-binding terms (GO:MF nucleic acid binding; q_global = 0.000387)(GO:MF RNA binding; q_global = 0.00109)(GO:BP gene expression; q_global = 0.0105)(GO:CC ribonucleoprotein complex; q_global = 0.0411)(GO:MF mRNA binding; q_global = 0.0465). Its known roles in RNA processing and transcription, together with a large literature and disease-association record, make it a strong integrative marker.
- **Conclusion**: Established evidence supports HNRNPK as a central RNA-processing and transcriptional regulator within the module. A coordinating role between RNA metabolism and DNA-maintenance signals is a reasonable hypothesis, but the co-abundance data do not establish causality.

#### MATR3

- **Related proteins** (co-abundance neighbors): XRCC6 (0.92), DHX9 (0.92), MACROH2A1 (0.91), CLTC (0.90), CCT3 (0.89), CCT5 (0.89), HNRNPK (0.87), SERPINH1 (0.86), RPL12 (0.86), HNRNPR (0.82), HSP90AA1 (0.81); STRING partners: DHX9 (0.786), HNRNPK (0.923), HNRNPR (0.714)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, rectum
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_07581.1
- **Function (MyGene.info)**: matrin 3. This gene encodes a nuclear matrix protein, which is proposed to stabilize certain messenger RNA species. Mutations of this gene are associated with distal myopathy 2, which often includes vocal cord and pharyngeal weakness. Alternatively spliced transcript variants, including read-through transcripts composed of the upstream small nucleolar RNA host gene 4 (non-protein coding) and matrin 3 gene s…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.735); distal myopathy with vocal cord weakness (0.569); neurodegenerative disease (0.529); distal myopathy (0.384); hereditary disease (0.193)
- **Europe PMC papers**: 1756
- **Why important**: MATR3 has a high weighted network position and connects the hnRNP neighborhood to DHX9, XRCC6, MACROH2A1, CCT proteins, and SERPINH1. It is supported by STRING relationships and two hu.MAP complexes containing RNA-binding partners (hu.MAP huMAP3_10625.1)(hu.MAP huMAP3_07581.1). Its annotations include messenger-RNA stabilization and post-transcriptional gene regulation, and it contributes to multiple globally corrected RNA-binding and gene-expression terms (GO:MF nucleic acid binding; q_global = 0.000387)(GO:BP macromolecule biosynthetic process; q_global = 0.00053)(GO:MF RNA binding; q_global = 0.00109)(GO:BP gene expression; q_global = 0.0105)(GO:BP macromolecule metabolic process; q_global = 0.0155)(GO:CC ribonucleoprotein complex; q_global = 0.0411). Its association with distal myopathy and neurodegenerative disease gives the gene additional biological relevance to a heart-containing tissue pair.
- **Conclusion**: Established evidence supports MATR3 as a nuclear RNA-processing and RNA-stability component that may connect the module's RNA and structural-maintenance signals. Its role as a tissue-pair-specific driver remains hypothetical.

#### CCT3

- **Related proteins** (co-abundance neighbors): QARS1 (0.94), MACROH2A1 (0.90), MATR3 (0.89), EIF3C (0.89), DHX9 (0.88), XRCC6 (0.87), CLTC (0.87), HNRNPK (0.84), HNRNPR (0.82), CCT5 (0.81), SERPINH1 (0.80); STRING partners: CCT5 (0.999), HSP90AA1 (0.767)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in heart, rectum
- **hu.MAP 3.0**: huMAP3_01951.1, huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a high-position module member and is strongly connected to CCT5, HSP90AA1, DHX9, MATR3, XRCC6, EIF3C, QARS1, and other module genes. It participates in many globally corrected terms, including macromolecule biosynthesis, DNA and chromosome processes, gene expression, and RNA-related functions (GO:MF nucleic acid binding; q_global = 0.000387) through (GO:BP regulation of macromolecule biosynthetic process; q_global = 0.0157) and (GO:BP positive regulation of macromolecule metabolic process; q_global = 0.0422)(GO:BP regulation of biosynthetic process; q_global = 0.0436)(GO:BP regulation of macromolecule metabolic process; q_global = 0.0469). Its established function in the CCT chaperonin complex, including folding of actin and tubulin, and its membership in multiple hu.MAP CCT-containing complexes make it the clearest proteostasis representative.
- **Conclusion**: Established evidence supports CCT3 as a chaperone component that may stabilize proteins required by the module's gene-expression and cellular-maintenance programs. The hypothesis that its abundance couples proteostasis to the RNA and chromatin subnetworks requires functional testing.

#### XRCC6

- **Related proteins** (co-abundance neighbors): MATR3 (0.92), MACROH2A1 (0.92), RPL12 (0.91), SERPINH1 (0.88), CCT3 (0.87), HNRNPR (0.84), H4C1; H4C2; H4C3; H4C4; H4C5; H4C6; H4C8; H4C9; H4C11; H4C12; H4C13; H4C14; H4C15; H4C16 (0.84), HSP90AA1 (0.83), CCT5 (0.83); STRING partners: DHX9 (0.819), HNRNPK (0.738), MACROH2A1 (0.769)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: X-ray repair cross complementing 6. The p70/p80 autoantigen is a nuclear complex consisting of two subunits with molecular masses of approximately 70 and 80 kDa. The complex functions as a single-stranded DNA-dependent ATP-dependent helicase. The complex may be involved in the repair of nonhomologous DNA ends such as that required for double-strand break repair, transposition, and V(D)J recombination. High levels of autoantibodies t…
- **Diseases (Open Targets)**: HIV infectious disease (0.505); neurodegenerative disease (0.441); intelligence (0.209); breast cancer (0.175); Abnormality of the skeletal system (0.154)
- **Europe PMC papers**: 2742
- **Why important**: XRCC6 occupies a prominent position connecting MATR3, MACROH2A1, DHX9, HNRNPK, HNRNPR, CCT3, HSP90AA1, SERPINH1, and histone genes. It is represented in globally corrected nucleic-acid binding, DNA metabolism, chromosome organization, telomere organization, and regulation of DNA metabolism (GO:MF nucleic acid binding; q_global = 0.000387)(GO:BP DNA metabolic process; q_global = 0.00127)(GO:BP chromosome organization; q_global = 0.00519)(GO:BP telomere organization; q_global = 0.00624)(GO:BP positive regulation of DNA metabolic process; q_global = 0.00624)(GO:BP regulation of DNA metabolic process; q_global = 0.0116). Its established role in DNA-dependent repair and nonhomologous end joining, together with a substantial literature and disease-association record, makes it a key genome-maintenance gene in the module.
- **Conclusion**: Established evidence supports XRCC6 as the strongest DNA-repair and genome-maintenance representative. Its network links to RNA-binding and chromatin genes suggest coordination within the module, but do not prove a shared repair complex.

#### TFRC

- **Related proteins** (co-abundance neighbors): DHX9 (0.88), HNRNPR (0.86), SERPINH1 (0.84), RPL12 (0.83), DDOST (0.82); STRING partners: CLTC (0.84)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes, Lysosomes; IHC detected in heart, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transferrin receptor. This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: TFRC-related combined immunodeficiency (0.623); type 2 diabetes mellitus (0.518); mucopolysaccharidosis type 2 (0.490); diabetes mellitus (0.471); diabetic retinopathy (0.343)
- **Europe PMC papers**: 14164
- **Why important**: TFRC connects the module to DHX9, HNRNPR, SERPINH1, RPL12, and DDOST, and has a direct STRING relationship with CLTC. It contributes to globally corrected nucleic-acid binding, DNA metabolism, gene expression, and macromolecule biosynthetic themes (GO:MF nucleic acid binding; q_global = 0.000387)(GO:BP macromolecule biosynthetic process; q_global = 0.00053)(GO:BP DNA metabolic process; q_global = 0.00127)(GO:BP positive regulation of DNA metabolic process; q_global = 0.00624)(GO:BP gene expression; q_global = 0.0105)(GO:BP regulation of DNA metabolic process; q_global = 0.0116). Its established role in transferrin-mediated iron uptake and erythropoiesis, HPA evidence for erythrocyte-progenitor and monocyte enhancement, and secretion to blood make it particularly informative for interpreting tissue composition.
- **Conclusion**: Established evidence supports TFRC as an iron-uptake and endocytic component with a possible blood-cell contribution to the shared signal. Its presence does not demonstrate that iron metabolism is the central function of the module; it may instead be a cell-composition or trafficking readout.

## Module 5

**Tissue pair**: heart and rectum  
**Genes (5)**: CTNNA1, PSMC2, FARSB, RARS1, USO1

### Function

The module does not have a globally significant GO or KEGG enrichment term; therefore, its function should be inferred cautiously from the individual gene annotations and network structure rather than from enrichment. The genes collectively point to core intracellular maintenance involving translation, protein quality control, vesicle transport, and cell adhesion. RARS1 is the central network connector and links the aminoacyl-tRNA synthetase FARSB with USO1, PSMC2, and CTNNA1. This pattern is more consistent with coordinated cellular homeostasis than with a narrowly defined biological pathway. The absence of a globally corrected GO or KEGG term does not invalidate the module.

**Cell composition.**  The module is not dominated by plasma proteins, secreted proteins, or blood-cell-enriched genes: none of the genes is annotated as secreted, and all have low immune-cell specificity. Most genes have low tissue specificity, while USO1 is tissue enhanced in skeletal muscle. Cell-type annotations are heterogeneous, involving oocytes, myonuclei, syncytiotrophoblasts, and esophageal apical cells. Protein detection is present for all module genes in rectum and for most in heart. These observations argue against a simple blood-contamination explanation, while leaving open the possibility that shared cellular composition or broadly distributed intracellular activity contributes to the conserved co-abundance pattern.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

 The only high-confidence known interaction within the module is between FARSB and RARS1. STRING functional enrichment is absent. No complex contains multiple module members. Thus, the network is largely unsupported by previously catalogued physical interaction or complex membership, apart from the biologically coherent pairing of two aminoacyl-tRNA synthetase components. The co-abundance links involving USO1, PSMC2, and CTNNA1 should therefore be interpreted as module-level expression or protein-abundance relationships, not as established direct physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: FARSB–RARS1 (0.706)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a previously unreported conserved co-abundance module shared by heart and rectum, because the particular combination and co-abundance structure are not represented by a multi-member hu.MAP complex and have little support from STRING. However, it cannot be called definitively new on that basis alone. The genes encode established, broadly relevant cellular proteins, and the sparse network may reflect shared housekeeping activity, cellular composition, or correlated regulation rather than a novel molecular complex. The strongest defensible conclusion is that the cross-tissue co-abundance pattern is potentially novel, whereas the individual biological functions are established.

**Hypothesis.** Hypothesis: the module reflects coordinated maintenance of intracellular proteostasis and tissue-cellular architecture. A possible mechanism is that translational capacity, represented by RARS1 and FARSB, covaries with proteasomal turnover through PSMC2, secretory-pathway organization through USO1, and cadherin-linked mechanosensitive adhesion through CTNNA1. In heart and rectum, shared demands for protein renewal, vesicle trafficking, and mechanical or junctional organization could produce the observed conserved abundance pattern. This is a hypothesis derived from the gene functions and network topology, not an experimentally established pathway or physical complex.

### Important genes

#### RARS1

- **Related proteins** (co-abundance neighbors): FARSB (0.85), USO1 (0.83), PSMC2 (0.82), CTNNA1 (0.81); STRING partners: FARSB (0.706)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 is the central connector of the module and is linked to every other member in the co-abundance subgraph. It encodes arginyl-tRNA synthetase, a core component of protein translation, and is the only module gene participating in the known STRING relationship with FARSB. It also has a substantial literature base and disease associations involving leukodystrophy and skeletal abnormalities.
- **Conclusion**: Established evidence supports RARS1 as a central translation-related gene and the principal network hub. Its centrality makes it a plausible organizing marker of the module, but it does not prove that RARS1 mechanistically regulates the other module genes.

#### FARSB

- **Related proteins** (co-abundance neighbors): RARS1 (0.85); STRING partners: RARS1 (0.706)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phenylalanyl-tRNA synthetase subunit beta. This gene encodes a highly conserved enzyme that belongs to the aminoacyl-tRNA synthetase class IIc subfamily. This enzyme comprises the regulatory beta subunits that form a tetramer with two catalytic alpha subunits. In the presence of ATP, this tetramer is responsible for attaching L-phenylalanine to the terminal adenosine of the appropriate tRNA. A pseudogene located on chromosome 10 has been i…
- **Diseases (Open Targets)**: Rajab interstitial lung disease with brain calcifications 1 (0.789); Rajab interstitial lung disease with brain calcifications (0.611); cirrhosis of liver (0.498); Cerebral calcification (0.498); Vascular dilatation (0.497)
- **Europe PMC papers**: 360
- **Why important**: FARSB is the partner of RARS1 in the only known high-confidence STRING interaction within the module. It encodes the beta subunit of phenylalanyl-tRNA synthetase, participates in protein translation and phenylalanyl-tRNA aminoacylation, and has disease associations including interstitial lung disease with brain calcifications. Its literature base is substantial relative to the small module.
- **Conclusion**: Established evidence supports FARSB as a translation-related enzyme component and as a known interaction partner of RARS1. Its isolated position in the co-abundance graph suggests that its importance may derive from the translation-related pair rather than from broad network connectivity.

#### PSMC2

- **Related proteins** (co-abundance neighbors): RARS1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in heart, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is a proteasome regulatory ATPase and is associated with ubiquitin-dependent protein catabolism and responses to oxidative stress. It is linked to RARS1 in the module and has the largest literature volume among the listed genes, with disease associations involving plasma-cell and other neoplastic disorders. Its presence connects translation-related activity with protein turnover.
- **Conclusion**: Established evidence supports PSMC2 as a component of proteasomal protein quality control. Its module association is compatible with coordinated proteostasis, but the data do not establish a direct interaction with RARS1 or a specific disease mechanism in heart or rectum.

#### USO1

- **Related proteins** (co-abundance neighbors): RARS1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: USO1 vesicle transport factor. The protein encoded by this gene is a peripheral membrane protein which recycles between the cytosol and the Golgi apparatus during interphase. It is regulated by phosphorylation: dephosphorylated protein associates with the Golgi membrane and dissociates from the membrane upon phosphorylation. Ras-associated protein 1 recruits this protein to coat protein complex II (COPII) vesicles during buddin…
- **Diseases (Open Targets)**: psoriatic arthritis (0.184); bipolar disorder (0.150); retinitis pigmentosa (0.085); cone dystrophy (0.076); cone-rod dystrophy (0.076)
- **Europe PMC papers**: 546
- **Why important**: USO1 is a Golgi-associated vesicle transport factor involved in endoplasmic-reticulum-to-Golgi transport, vesicle fusion, and intracellular protein trafficking. It is tissue enhanced in skeletal muscle and cell-type enhanced in myonuclei, making it particularly relevant to the muscle-associated context of the module. It is connected to RARS1 in the co-abundance network despite having no reported STRING partner within the module.
- **Conclusion**: Established evidence supports USO1 as a vesicle-trafficking factor with a tissue pattern compatible with muscle-related biology. Its connection to RARS1 is a co-abundance observation, not evidence of a known physical interaction; a role in coordinating trafficking with translation remains hypothetical.

#### CTNNA1

- **Related proteins** (co-abundance neighbors): RARS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in heart, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin alpha 1. This gene encodes a member of the catenin family of proteins that play an important role in cell adhesion process by connecting cadherins located on the plasma membrane to the actin filaments inside the cell. The encoded mechanosensing protein contains three vinculin homology domains and undergoes conformational changes in response to cytoskeletal tension, resulting in the reconfiguration of cadhe…
- **Diseases (Open Targets)**: Butterfly-shaped pigment dystrophy (0.750); hereditary neoplastic syndrome (0.557); hereditary diffuse gastric adenocarcinoma (0.555); colorectal cancer (0.506); exudative vitreoretinopathy (0.390)
- **Europe PMC papers**: 2688
- **Why important**: CTNNA1 encodes alpha-catenin, which connects cadherin-containing cell junctions to actin and functions as a mechanosensing adhesion protein. It is detected in both heart and rectum, localizes to the plasma membrane and cell junctions, and has extensive literature and disease associations including pigment dystrophy, hereditary diffuse gastric adenocarcinoma, colorectal cancer, and exudative vitreoretinopathy. Its presence introduces tissue architecture and mechanical signaling into the module.
- **Conclusion**: Established evidence supports CTNNA1 as a cell-adhesion and mechanotransduction protein relevant to both sampled tissues. Its co-abundance relationship with RARS1 may reflect shared tissue state, junctional organization, or cellular composition, but no direct molecular connection between the two proteins is established here.
