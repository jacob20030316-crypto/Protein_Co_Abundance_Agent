# Conserved co-abundance modules: breast and testis

## Module 0

**Tissue pair**: breast and testis  
**Genes (10)**: ABCA8, ACACA, ACE, ATP1A1, COPG2, GNA11, MYO1C, SEC23IP, SKIC3, VPS13C

### Function

The module is best interpreted as a coordinated membrane-associated and intracellular trafficking program with links to lipid handling, ion-gradient maintenance, vesicle transport, and cell-surface signaling. ABCA8 is the central co-abundance hub and is connected to ACE, ATP1A1, MYO1C, SEC23IP, VPS13C, SKIC3, COPG2, and ACACA, while GNA11 is also connected to ABCA8. The supplementary STRING term supplementary STRING supports a basal plasma membrane theme through ABCA8, ACE, ATP1A1, and MYO1C, but this is not global enrichment evidence. No GO or KEGG term passed global correction, so no GO or KEGG biological process should be presented as significantly enriched. The annotations nonetheless suggest a composite program involving membrane transport, lipid metabolism, ER-to-Golgi and Golgi trafficking, cytoskeletal movement, RNA quality control, and G-protein signaling rather than a single narrowly defined pathway. The sparse star-like co-abundance structure supports coordinated expression, but does not establish direct molecular interaction or a single physical complex.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: ACE is the only secreted-to-blood gene in the fact sheet, whereas the other genes are intracellular or membrane-associated. The module is also not strongly blood-cell enriched. Most genes have low tissue specificity, several show cell-type enhancement across diverse cell types, and the HPA profile includes enterocytes, oligodendrocytes, alveolar cells, adipocytes, adrenal cortex cells, and other cell types rather than one coherent lineage. Protein detection is broader in testis than breast, although the module is detected in both tissues overall. The shared breast-testis signal may therefore reflect broadly expressed epithelial, membrane, metabolic, or trafficking programs, shared cellular constituents, or sample composition rather than a breast-testis-specific biological mechanism. The HPA profile does not support interpreting the module simply as blood contamination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING evidence is limited to the supplementary basal plasma membrane association, involving ACE, ATP1A1, ABCA8, and MYO1C. No high-confidence STRING interaction was observed among the module genes, and no hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated as established physical protein interactions or as membership in a known hu.MAP complex. The network may capture coordinated regulation, shared cell-type abundance, common membrane or metabolic state, or indirect pathway relationships. Known functional links are strongest at the annotation level: ABCA8 is associated with lipid and cholesterol transport, ATP1A1 with electrochemical gradients, ACE with peptide and vascular regulation, SEC23IP and COPG2 with secretory-pathway trafficking, VPS13C with lipid transfer and organelle biology, ACACA with fatty-acid synthesis, MYO1C with actin-dependent transport, and GNA11 with receptor-mediated signaling.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Component Basal plasma membrane (FDR = 0.0116, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should be described as a potentially novel co-abundance association pattern, not as a newly discovered molecular complex or pathway. Its novelty is supported only in the limited sense that this particular cross-tissue co-abundance configuration is not represented by a matching high-confidence STRING network or hu.MAP complex in the supplied resources. That absence does not prove biological novelty, because co-abundance can arise from shared regulation, cell composition, or indirect relationships, and database coverage is incomplete. The lack of globally significant GO or KEGG enrichment also prevents assigning it a previously established pathway label. A stronger novelty claim would require replication in independent breast and testis datasets, control for cell-type composition, and comparison with published tissue co-expression modules.

**Hypothesis.** Hypothesis: the module represents coordinated expression of a membrane and endomembrane homeostasis program that couples lipid handling and fatty-acid production with vesicle traffic, plasma-membrane ion gradients, and receptor-linked signaling. In this model, ABCA8 acts as the co-abundance organizing feature, while SEC23IP, COPG2, and VPS13C reflect secretory and lipid-transfer processes; ATP1A1, ACE, and GNA11 contribute membrane physiology and signaling; and MYO1C supports cytoskeletal delivery to the membrane. The apparent conservation between breast and testis could arise because both tissues contain cells requiring active membrane remodeling, secretion, transport, or lipid metabolism. This remains a hypothesis because the network lacks corroborating physical interactions, contains no globally significant GO or KEGG term, and may be influenced by cell-type composition.

### Important genes

#### ABCA8

- **Related proteins** (co-abundance neighbors): ACE (0.88), MYO1C (0.86), SEC23IP (0.85), VPS13C (0.84), SKIC3 (0.84), COPG2 (0.84), ATP1A1 (0.83), ACACA (0.82), GNA11 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP binding cassette subfamily A member 8. The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intracellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the ABC1 subfamily. Members of the ABC1 subfamily comprise …
- **Diseases (Open Targets)**: coronary artery bypass (0.359); hypercholesterolemia, familial, 1 (0.341); metabolic syndrome (0.330); response to statin (0.316); coronary atherosclerosis (0.289)
- **Europe PMC papers**: 868
- **Why important**: ABCA8 is the central co-abundance hub, connecting every other module member in the supplied network. Its ABC-transporter annotation and links to lipid transport, cholesterol efflux, sphingomyelin biology, and xenobiotic transport make it the strongest candidate for organizing the module’s membrane and lipid-handling theme. It is also one of the genes contributing to the supplementary basal plasma membrane term. Its disease associations include lipid and cardiovascular traits, and its literature volume is substantial.
- **Conclusion**: Established evidence supports ABCA8 as the network-level anchor and as a membrane-associated transporter related to lipid homeostasis. Hypothesis: ABCA8 may coordinate the expression of membrane, trafficking, and metabolic genes in this module, but the co-abundance network does not establish that it physically regulates the other genes.

#### ACE

- **Related proteins** (co-abundance neighbors): ABCA8 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: angiotensin I converting enzyme. This gene encodes an enzyme involved in blood pressure regulation and electrolyte balance. It catalyzes the conversion of angiotensin I into a physiologically active peptide angiotensin II. Angiotensin II is a potent vasopressor and aldosterone-stimulating peptide that controls blood pressure and fluid-electrolyte balance. This angiotensin converting enzyme (ACE) also inactivates the vasodilator p…
- **Diseases (Open Targets)**: hypertensive disorder (0.750); renal tubular dysgenesis of genetic origin (0.729); renal tubular dysgenesis (0.724); cardiovascular disorder (0.704); diabetic kidney disease (0.689)
- **Europe PMC papers**: 95248
- **Why important**: ACE is a high-literature, secreted enzyme with strong established roles in angiotensin maturation, bradykinin inactivation, vascular regulation, and electrolyte physiology. It is tissue enhanced in intestine and testis, group enriched in enterocytes and late spermatids, and contributes to the supplementary basal plasma membrane term. Its direct connection to the ABCA8 hub links a secreted vascular and epithelial enzyme to the module’s membrane-associated pattern.
- **Conclusion**: Established evidence supports ACE as a biologically important secreted and membrane-compartment-associated enzyme with major cardiovascular and renal disease relevance. Hypothesis: its co-abundance with ABCA8 may reflect epithelial or secretory-cell state, membrane remodeling, or sample composition rather than a direct functional partnership.

#### ATP1A1

- **Related proteins** (co-abundance neighbors): ABCA8 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 encodes the catalytic alpha subunit of the sodium-potassium pump and therefore provides a clear mechanism for maintaining plasma-membrane electrochemical gradients. It contributes to the supplementary basal plasma membrane term, is detected in both tissues, and shows cell-type enhancement in several transport-active epithelial populations. Its extensive disease literature includes cardiac, neurological, and electrolyte-related disorders.
- **Conclusion**: Established evidence supports ATP1A1 as a core determinant of membrane ion homeostasis and epithelial transport physiology. Hypothesis: its co-abundance with ABCA8 may indicate coordinated membrane turnover or transport demand, but there is no supplied evidence for a direct ATP1A1-ABCA8 interaction.

#### SEC23IP

- **Related proteins** (co-abundance neighbors): ABCA8 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC23 interacting protein. This gene encodes a member of the phosphatidic acid preferring-phospholipase A1 family. The encoded protein is localized to endoplasmic reticulum exit sites and plays a critical role in ER-Golgi transport as part of the multimeric coat protein II complex. An orthologous gene in frogs is required for normal neural crest cell development, suggesting that this gene may play a role in Waardenburg synd…
- **Diseases (Open Targets)**: Parkinson disease (0.409); type 2 diabetes mellitus (0.372); cardiomyopathy (0.326); diabetes mellitus (0.294); Genu valgum (0.269)
- **Europe PMC papers**: 265
- **Why important**: SEC23IP is connected directly to the ABCA8 hub and has established roles at ER exit sites, ER-to-Golgi transport, Golgi organization, and the endomembrane system. The fact sheet also associates it with spermatid development, making it particularly relevant to the tissue pair. Its literature volume is smaller than that of ACE or ATP1A1, so it may be an informative but less extensively characterized component.
- **Conclusion**: Established evidence supports SEC23IP as a vesicle-trafficking and ER-Golgi organization factor. Hypothesis: SEC23IP may help explain why the module links membrane transport with tissue contexts requiring active secretion or differentiation, but the module does not demonstrate a specific SEC23IP-dependent mechanism.

#### ACACA

- **Related proteins** (co-abundance neighbors): ABCA8 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA carboxylase alpha. Acetyl-CoA carboxylase (ACC) is a complex multifunctional enzyme system. ACC is a biotin-containing enzyme which catalyzes the carboxylation of acetyl-CoA to malonyl-CoA, the rate-limiting step in fatty acid synthesis. There are two ACC forms, alpha and beta, encoded by two different genes. ACC-alpha is highly enriched in lipogenic tissues. The enzyme is under long term control at the transcriptio…
- **Diseases (Open Targets)**: neurodegenerative disease (0.550); Alzheimer disease (0.463); lysosomal storage disease (0.460); Parkinson disease (0.460); autoimmune disorder of central nervous system (0.383)
- **Europe PMC papers**: 6268
- **Why important**: ACACA is the rate-limiting acetyl-CoA carboxylase for fatty-acid synthesis and is linked to lipogenic tissue biology. Its presence beside the membrane transporter ABCA8 and trafficking genes provides a metabolic counterpart to the module’s membrane and endomembrane features. ACACA has extensive literature and broad disease relevance, including metabolic and neurodegenerative associations.
- **Conclusion**: Established evidence supports ACACA as a major lipid-biosynthetic enzyme. Hypothesis: ACACA may supply or regulate lipid resources needed for membrane remodeling and vesicle production in the shared module, but this metabolic coupling is inferred rather than demonstrated by the supplied network.

#### GNA11

- **Related proteins** (co-abundance neighbors): ABCA8 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein subunit alpha 11. The protein encoded by this gene belongs to the family of guanine nucleotide-binding proteins (G proteins), which function as modulators or transducers in various transmembrane signaling systems. G proteins are composed of 3 units: alpha, beta and gamma. This gene encodes one of the alpha subunits (subunit alpha-11). Mutations in this gene have been associated with hypocalciuric hypercalcemia type…
- **Diseases (Open Targets)**: familial hypoparathyroidism (0.754); familial hypocalciuric hypercalcemia 2 (0.736); autosomal dominant hypocalcemia (0.611); congenital hemangioma (0.494); uveal melanoma (0.469)
- **Europe PMC papers**: 4418
- **Why important**: GNA11 is a signaling transducer for multiple G-protein-coupled receptor pathways, including pathways involving adenylate cyclase and phospholipase C. It is connected to ABCA8 and shows cell-type enhancement in colonocytes and enterocytes, while its disease associations include calcium and parathyroid disorders and uveal melanoma. Its substantial literature provides a well-established signaling anchor for an otherwise mixed module.
- **Conclusion**: Established evidence supports GNA11 as a plasma-membrane signaling mediator with important calcium and endocrine disease associations. Hypothesis: GNA11 may connect membrane composition or transport state to receptor signaling in the module, but the supplied data do not establish a direct relationship with ABCA8 or the other members.

## Module 1

**Tissue pair**: breast and testis  
**Genes (5)**: ATL3, FERMT2, ME3, NIBAN1, USO1

### Function

This is a small, structurally sparse co-abundance module centered on ME3, with ME3 connected to NIBAN1, FERMT2, USO1, and ATL3. No GO or KEGG term passed global multiple-testing correction, so there is no globally significant pathway annotation for this module. The gene annotations nevertheless suggest convergence of mitochondrial malate-to-pyruvate metabolism, cellular stress and phosphorylation regulation, cell-matrix adhesion, ER-to-Golgi trafficking, Golgi function, and ER membrane organization. These annotations support a cautious interpretation as a cellular infrastructure and metabolic-stress module rather than a confidently assigned canonical pathway. The module may reflect coordinated abundance of proteins involved in organelle function, intracellular trafficking, adhesion, and metabolic state, but the enrichment evidence alone does not establish that interpretation.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of its members is annotated as secreted. It is also not a clear blood-cell module. HPA evidence is mixed, with low or tissue-enhanced tissue specificity across the genes and cell-type signals involving cardiomyocytes, myonuclei, adipocytes, podocytes, smooth muscle cells, spermatids, neutrophils, and myeloid dendritic cells. The presence of spermatid and muscle-related signals is compatible with tissue or cell-composition effects in the breast and testis comparison, while the immune-cell annotations warrant caution about blood or immune contributions. However, the mixed HPA profile does not support reducing the module to a single blood-cell population. Protein detection is reported in both tissues for nearly all members, with missing HPA protein information for one gene.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was present among the module genes, and no STRING functional-enrichment result was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not supported here as already known physical protein interactions or as a known multiprotein complex. ME3 is the co-abundance hub, while each other gene is connected only to ME3; this topology may reflect coordinated expression, shared cell composition, or a common physiological state rather than direct molecular binding. The lack of STRING and hu.MAP support is informative about prior interaction evidence but does not invalidate the co-abundance pattern.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module can reasonably be described as a potentially novel co-abundance association pattern, because its gene set has no reported STRING interactions, no shared hu.MAP complex, and no globally significant GO or KEGG term. It should not be called a newly discovered biological pathway or a definitively novel mechanism. Absence from interaction and complex databases does not prove novelty: the pattern could arise from tissue composition, correlated cellular states, technical or sampling effects, or interactions that have not been curated. Independent replication, preservation across cohorts, and cell-composition-aware analyses would be needed before claiming a new biological module.

**Hypothesis.** Hypothesis: in breast and testis samples, variation in a shared cellular state involving metabolic flux and organelle homeostasis may coordinate mitochondrial ME3 abundance with ER architecture, ER-to-Golgi trafficking, Golgi cycling, adhesion-associated signaling, and stress-response regulation. ME3 could act as the network-level marker of this state, while ATL3 and USO1 represent ER and secretory-pathway organization, FERMT2 represents adhesion and mechanosensitive signaling, and NIBAN1 represents stress and apoptosis-related regulation. This is a mechanistic hypothesis generated from co-abundance and gene annotations, not an established physical pathway; the absence of STRING and hu.MAP support makes direct protein-to-protein coupling particularly uncertain.

### Important genes

#### ME3

- **Related proteins** (co-abundance neighbors): NIBAN1 (0.85), FERMT2 (0.83), USO1 (0.83), ATL3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: malic enzyme 3. Malic enzyme catalyzes the oxidative decarboxylation of malate to pyruvate using either NAD+ or NADP+ as a cofactor. Mammalian tissues contain 3 distinct isoforms of malic enzyme: a cytosolic NADP(+)-dependent isoform, a mitochondrial NADP(+)-dependent isoform, and a mitochondrial NAD(+)-dependent isoform. This gene encodes a mitochondrial NADP(+)-dependent isoform. Multiple alternatively spliced …
- **Diseases (Open Targets)**: open-angle glaucoma (0.522); glaucoma (0.486); Abnormality of the skeletal system (0.379); cataract (0.316); age-related macular degeneration (0.313)
- **Europe PMC papers**: 5795
- **Why important**: ME3 is the central co-abundance hub, connected to every other module member, and therefore provides the strongest network-level anchor. Its established function is the mitochondrial NADP-dependent malic enzyme, linking malate metabolism with pyruvate biosynthesis. It has extensive literature and disease-association coverage, including ophthalmic and skeletal-system associations in the supplied evidence.
- **Conclusion**: Established evidence supports ME3 as a mitochondrial metabolic enzyme and the principal statistical hub of this module. It is plausible that ME3 marks a shared metabolic state, but the data do not establish that ME3 regulates the other genes or that its enzyme activity causes their co-abundance.

#### ATL3

- **Related proteins** (co-abundance neighbors): ME3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: atlastin GTPase 3. This gene encodes a member of a family of dynamin-like, integral membrane GTPases. The encoded protein is required for the proper formation of the network of interconnected tubules of the endoplasmic reticulum. Mutations in this gene may be associated with hereditary sensory neuropathy type IF. Alternatively spliced transcript variants that encode distinct isoforms have been described. [provided b…
- **Diseases (Open Targets)**: neuropathy, hereditary sensory, type 1F (0.718); hereditary sensory and autonomic neuropathy type 1 (0.617); hereditary disease (0.193); Familial prostate cancer (0.112); prostate cancer (0.112)
- **Europe PMC papers**: 672
- **Why important**: ATL3 connects directly to the ME3 hub and provides a clear organelle-structural component. It is an ER membrane GTPase involved in ER tubular-network organization and membrane fusion, with an HPA group-enriched signal in early and late spermatids. Its established association with hereditary sensory neuropathy gives it substantial disease relevance.
- **Conclusion**: Established evidence supports ATL3 as an ER-shaping protein with a particularly relevant spermatid-associated expression signal. Its co-abundance with ME3 may indicate coordinated metabolic and ER organization states, but a direct ME3–ATL3 mechanism remains a hypothesis.

#### USO1

- **Related proteins** (co-abundance neighbors): ME3 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: USO1 vesicle transport factor. The protein encoded by this gene is a peripheral membrane protein which recycles between the cytosol and the Golgi apparatus during interphase. It is regulated by phosphorylation: dephosphorylated protein associates with the Golgi membrane and dissociates from the membrane upon phosphorylation. Ras-associated protein 1 recruits this protein to coat protein complex II (COPII) vesicles during buddin…
- **Diseases (Open Targets)**: psoriatic arthritis (0.184); bipolar disorder (0.150); retinitis pigmentosa (0.085); cone dystrophy (0.076); cone-rod dystrophy (0.076)
- **Europe PMC papers**: 546
- **Why important**: USO1 links the ME3 hub to intracellular trafficking. It cycles between the cytosol and Golgi and participates in ER-to-Golgi vesicle transport and Golgi vesicle fusion. Its tissue-enhanced skeletal-muscle and myonuclear signals suggest that cell-state composition could contribute to the association. Its literature volume is moderate among the module genes.
- **Conclusion**: Established evidence supports USO1 as a Golgi and ER-to-Golgi trafficking factor. The module association is consistent with coordinated organelle homeostasis, but it does not demonstrate that USO1 physically interacts with ME3 or that trafficking controls ME3 abundance.

#### FERMT2

- **Related proteins** (co-abundance neighbors): ME3 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Focal adhesion sites; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FERM domain containing kindlin 2. Enables several functions, including actin binding activity; phosphatidylinositol-3,4,5-trisphosphate binding activity; and type I transforming growth factor beta receptor binding activity. Involved in several processes, including cell surface receptor signaling pathway; positive regulation of cell differentiation; and positive regulation of cellular component biogenesis. Acts upstream of or withi…
- **Diseases (Open Targets)**: open-angle glaucoma (0.501); prostate carcinoma (0.488); glaucoma (0.488); neurodegenerative disease (0.473); primary angle-closure glaucoma (0.407)
- **Europe PMC papers**: 1336
- **Why important**: FERMT2 connects to ME3 and contributes a distinct adhesion and signaling dimension. It is localized at focal adhesions and supports actin binding, phosphatidylinositol signaling, integrin-mediated signaling, cell-matrix adhesion, and receptor-related processes. Its cell-type signals include adipocytes, podocytes, and smooth muscle cells, and it has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports FERMT2 as an adhesion and cytoskeletal signaling regulator. Its presence may indicate tissue architecture or cell-state differences shared across the samples. A functional metabolic-to-adhesion relationship is possible but is not demonstrated by this module.

#### NIBAN1

- **Related proteins** (co-abundance neighbors): ME3 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: niban apoptosis regulator 1. This gene encodes a member of the family with sequence similarity 129 protein family. This gene is highly expressed in several cancer cells and may serve as a prognostic marker for certain cancers. The encoded protein may play a role in regulating p53-mediated apoptosis. [provided by RefSeq, Sep 2016].
- **Diseases (Open Targets)**: Chronic pain (0.191); Abnormal male internal genitalia morphology (0.155); alcohol drinking (0.151); urolithiasis (0.151); ovarian neoplasm (0.147)
- **Europe PMC papers**: 147
- **Why important**: NIBAN1 is the only module member directly connected to ME3 without additional module neighbors, making it a peripheral but potentially informative stress-response component. It is associated with ER stress, regulation of phosphorylation, translation, and p53-mediated apoptosis, and HPA reports tissue enhancement in heart muscle and immune-cell enhancement in neutrophils. Its literature volume is smaller than that of ME3 or FERMT2, which makes it a useful candidate for follow-up.
- **Conclusion**: Established evidence supports NIBAN1 as a stress- and apoptosis-related regulator with context-dependent expression. Its co-abundance with ME3 could reflect metabolic stress or cellular composition, but the supplied data do not show that NIBAN1 mediates the module or explain its connection to the other genes.

## Module 2

**Tissue pair**: breast and testis  
**Genes (8)**: BAG5, CEP76, CLMN, FAAH, HIP1, HK1, PCYT2, PSME4

### Function

No GO or KEGG term passed global correction, and STRING reported no supplementary enrichment. Therefore, the module does not support a statistically established pathway-level annotation. Its gene annotations nevertheless suggest a shared cellular program involving centrosome and flagellar-centriole biology through CEP76, sperm chromatin and proteostasis through PSME4 and BAG5, membrane lipid synthesis through PCYT2, vesicle trafficking through HIP1, fatty-acid-amide metabolism through FAAH, and glucose metabolism through HK1. The strongest biological clue is the HPA single-cell pattern, in which the great majority of members are enhanced in late spermatids and several are associated with earlier spermatogenic stages. A cautious functional interpretation is therefore a spermatid-associated cellular-maintenance or differentiation program rather than a defined molecular pathway. The breast signal may reflect expression of the same cellular machinery in breast tissue, shared cell states, or tissue-composition effects. The absence of globally significant enrichment does not invalidate the module; it means that pathway-level evidence is insufficient.

**Cell composition.** The module is not composed of plasma or secreted proteins: every member is annotated as nonsecreted. It is also not broadly blood-cell enriched overall. Most members have low immune-cell specificity, although HIP1 shows a group-enriched pattern across several blood-cell classes, FAAH is immune-cell enhanced in eosinophils, and other isolated blood-cell associations occur. Several genes have low tissue specificity and could represent broadly available cellular machinery, whereas CLMN, BAG5, and PCYT2 show testis-related tissue enhancement and many members show spermatid-associated single-cell enhancement. Protein detection is present for nearly all members in breast and for every member in testis. Thus, the shared module is more consistent with a mixture of broadly expressed cellular functions and a strong spermatogenic or spermatid-associated component than with a plasma-protein or general blood-contamination signature. A contribution from shared cell types or tissue composition remains plausible.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The module has no high-confidence STRING interaction among its member pairs, and no hu.MAP complex contains multiple module members. Accordingly, the co-abundance links should not be interpreted as established direct physical interactions or as a known protein complex. CEP76 is the sole network hub, connected to every other member, while the remaining genes form peripheral links to it. The annotations of the peripheral genes span centrosome control, proteasome activation, nuclear migration, chaperone regulation, lipid metabolism, phospholipid synthesis, endocytosis, and glucose metabolism. This combination, together with the absence of STRING and hu.MAP support, favors a coordinated expression or cell-state signal over a demonstrated biochemical complex. Known functions of individual proteins remain informative, but the module-level relationships are not independently confirmed by these interaction resources.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel co-abundance observation, particularly because the module is conserved across breast and testis while lacking support from the queried STRING and hu.MAP resources. However, it cannot be called a newly discovered molecular complex or a definitively new biological pathway. The lack of STRING or hu.MAP representation alone does not establish novelty, and the absence of globally significant GO or KEGG enrichment limits the strength of a pathway-level novelty claim. The most defensible novelty statement is that the coordinated expression pattern, especially its association with spermatid-related cellular states and a CEP76-centered network structure, appears not to map onto an already recognized interaction module in the supplied resources. Independent replication, tissue-composition control, and perturbational testing would be needed to establish that it is a genuine conserved regulatory program rather than a composition-driven signal.

**Hypothesis.** Hypothesis: the module reflects a coordinated spermatid-associated state in which centrosome and flagellar-centriole regulation through CEP76 is coupled to sperm chromatin and proteostasis through PSME4 and BAG5, membrane remodeling through PCYT2, vesicle trafficking through HIP1, and lipid or energy metabolism through FAAH and HK1. In breast tissue, the same co-abundance pattern may arise from a shared proliferative, ciliary, vesicular, or metabolically active cell state, or from a related cell-population mixture. This is a mechanistic hypothesis rather than an established pathway: the co-abundance graph does not demonstrate direct binding, shared complex membership, or causal regulation.

### Important genes

#### CEP76

- **Related proteins** (co-abundance neighbors): PSME4 (0.94), CLMN (0.89), BAG5 (0.88), FAAH (0.87), PCYT2 (0.86), HIP1 (0.84), HK1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules, Mitotic spindle, Primary cilium, Perinuclear theca, Flagellar centriole; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: centrosomal protein 76. This gene encodes a centrosomal protein which regulates centriole amplification by limiting centriole duplication to once per cell cycle. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2012].
- **Diseases (Open Targets)**: retinitis pigmentosa (0.536); Joubert syndrome 1 (0.482); Bardet-Biedl syndrome (0.465); Joubert syndrome (0.455); complex neurodevelopmental disorder (0.370)
- **Europe PMC papers**: 167
- **Why important**: CEP76 is the central network gene, connected to every other module member, making it the strongest candidate for organizing the observed co-abundance pattern. Its established role in limiting centriole duplication, together with localization to microtubules, the mitotic spindle, primary cilia, the perinuclear theca, and the flagellar centriole, provides a plausible link to spermatid architecture. Its associations with retinitis pigmentosa and Joubert and Bardet-Biedl syndromes also connect it to ciliary biology. The gene has a substantive literature base.
- **Conclusion**: Established evidence supports CEP76 as a centriole- and cilium-related protein and as the network hub. It is therefore the leading candidate for a structural or cell-state anchor of the module. It is not established that CEP76 directly regulates the other module genes; that proposed coordination remains a hypothesis.

#### PCYT2

- **Related proteins** (co-abundance neighbors): CEP76 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphate cytidylyltransferase 2, ethanolamine. This gene encodes an enzyme that catalyzes the formation of CDP-ethanolamine from CTP and phosphoethanolamine in the Kennedy pathway of phospholipid synthesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010].
- **Diseases (Open Targets)**: spastic paraplegia 82, autosomal recessive (0.771); complex hereditary spastic paraplegia (0.554); neurodegenerative disease (0.542); Global developmental delay (0.462); Intellectual disability (0.462)
- **Europe PMC papers**: 4199
- **Why important**: PCYT2 is the module member with a direct enzymatic role in phosphatidylethanolamine and broader phospholipid biosynthesis. It is tissue enhanced in liver and testis and cell-type enriched in late spermatids, making it particularly relevant to membrane production during spermatid differentiation. Its associations with spastic paraplegia and related neurodegenerative phenotypes provide disease evidence, and it has a substantial literature base despite being a peripheral network member.
- **Conclusion**: Established evidence supports PCYT2 as a phospholipid-biosynthesis enzyme with testis and late-spermatid relevance. Its co-abundance with CEP76 may indicate membrane requirements accompanying flagellar or cellular remodeling, but a direct connection to centriole biology is not demonstrated.

#### PSME4

- **Related proteins** (co-abundance neighbors): CEP76 (0.94); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome activator subunit 4. Predicted to enable lysine-acetylated histone binding activity; peptidase activator activity; and proteasome binding activity. Predicted to be involved in DNA repair; proteasomal ubiquitin-independent protein catabolic process; and spermatogenesis, exchange of chromosomal proteins. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Alzheimer disease (0.340); aortic disorder (0.253); intestinal obstruction (0.198); Paralytic ileus (0.198); breast carcinoma (0.197)
- **Europe PMC papers**: 561
- **Why important**: PSME4 links the module to proteasome regulation, DNA repair, DNA-damage response, sperm DNA condensation, exchange of chromosomal proteins, and flagellated sperm motility. Its nucleoplasmic localization and detection in both tissues make it a plausible contributor to nuclear and proteostatic demands of differentiating germ cells. It also has disease associations involving neurodegenerative, vascular, intestinal, and breast-cancer contexts, supported by a substantial literature base.
- **Conclusion**: Established evidence supports PSME4 in proteasome activation, genome maintenance, and sperm-associated nuclear or motility processes. Its presence strengthens the interpretation of a spermatid-maintenance program, but the module does not establish that PSME4 physically interacts with CEP76 or any other member.

#### BAG5

- **Related proteins** (co-abundance neighbors): CEP76 (0.88); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BAG cochaperone 5. The protein encoded by this gene is a member of the BAG1-related protein family. BAG1 is an anti-apoptotic protein that functions through interactions with a variety of cell apoptosis and growth related proteins including BCL-2, Raf-protein kinase, steroid hormone receptors, growth factor receptors and members of the heat shock protein 70 kDa family. This protein contains a BAG domain near the C-t…
- **Diseases (Open Targets)**: cardiomyopathy, dilated, 2F (0.614); mitochondrial complex IV deficiency, nuclear type 17 (0.533); mitochondrial complex IV deficiency, nuclear-type (0.420); leigh syndrome due to mitochondrial complex iv deficiency (0.420); familial isolated dilated cardiomyopathy (0.391)
- **Europe PMC papers**: 635
- **Why important**: BAG5 is tissue enriched in testis and enhanced across early and late spermatid-related cell states. As a BAG-family cochaperone, it is annotated in protein folding, protein stabilization, and regulation of ubiquitination and proteasomal degradation. Its disease associations include dilated cardiomyopathy and mitochondrial complex IV deficiency, and it has a substantial literature base. Although peripheral in the network, it provides a biologically meaningful proteostasis component.
- **Conclusion**: Established evidence supports BAG5 as a cochaperone and regulator of protein stability and degradation, with strong testis and spermatid relevance in the supplied HPA evidence. Its participation in the proposed module-level proteostasis program is plausible, but causal coordination with CEP76 or PSME4 remains unproven.

#### HIP1

- **Related proteins** (co-abundance neighbors): CEP76 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: huntingtin interacting protein 1. The product of this gene is a membrane-associated protein that functions in clathrin-mediated endocytosis and protein trafficking within the cell. The encoded protein binds to the huntingtin protein in the brain; this interaction is lost in Huntington's disease. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013].
- **Diseases (Open Targets)**: cancer (0.509); lung carcinoma (0.375); pancreatic ductal adenocarcinoma (0.373); lymphoid neoplasm (0.370); carcinoma of liver and intrahepatic biliary tract (0.370)
- **Europe PMC papers**: 2213
- **Why important**: HIP1 contributes an endocytic and vesicle-trafficking interpretation through its established roles in clathrin-mediated endocytosis, actin organization, and vesicle-mediated transport. It is enhanced in late spermatids and several epithelial or neural cell types. Its blood-cell group-enriched pattern is important because it raises the possibility of a cell-composition contribution. HIP1 also has extensive disease-related annotation involving cancer and neoplasia and a large literature base.
- **Conclusion**: Established evidence supports HIP1 in membrane trafficking and endocytosis, with a possible role in remodeling of differentiating spermatids. The blood-cell pattern means HIP1 could also contribute to sample-composition effects. Its relationship to the other module genes is a co-abundance hypothesis rather than a demonstrated physical interaction.

## Module 3

**Tissue pair**: breast and testis  
**Genes (6)**: CRLF3, ART3, PDCD6IP, SACM1L, SEH1L, THOP1

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING enrichment. The module therefore does not support a single statistically established pathway-level function. Its genes represent several cellular systems: ART3 is an inactive arginine-specific ADP-ribosyltransferase; THOP1 is a cytosolic peptide-cleaving oligopeptidase; SACM1L regulates phosphoinositide dephosphorylation and membrane organization; SEH1L is a nucleoporin associated with the Nup107-160 complex and mitotic chromosome behavior; PDCD6IP participates in ESCRT-dependent vesicle biology and cytokinesis; and CRLF3 is a cytokine-receptor-like protein associated with cell-cycle and receptor-signaling regulation. The co-abundance pattern is consequently most consistent with a context-dependent cellular state involving membrane and vesicle biology, intracellular processing, cell-cycle organization, and signaling, but this functional interpretation remains integrative rather than an enrichment-supported pathway assignment.

**Cell composition.** The module is not dominated by plasma or classically secreted proteins. The secretome annotations identify ART3 and PDCD6IP as intracellular and membrane-associated rather than secreted, while the other genes have no secretome annotation. HPA indicates generally broad tissue distribution for most members, with ART3 showing group-enriched expression in heart muscle, skeletal muscle, testis, and tongue, and CRLF3 showing tissue enhancement in lymphoid tissue. Several members have cell-type-enhanced or group-enriched patterns, including spermatocytes, myonuclei, cardiomyocytes, neutrophil-lineage cells, and esophageal apical cells. However, the blood-cell evidence does not indicate a blood-cell-enriched module: most genes have low immune-cell specificity and one is not detected in immune cells, with no enriched blood-cell category reported. The shared breast-testis signal may therefore reflect a mixture of broadly expressed cellular machinery and tissue or cell-state composition, rather than a blood contaminant or a secreted-protein program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING reports no high-confidence interaction among the module members, and hu.MAP reports no complex containing multiple members. Thus, the co-abundance edges are not corroborated by the available physical-interaction or complex resources. This does not invalidate the module: co-abundance can reflect shared regulation, cellular state, tissue composition, or indirect functional coupling rather than direct binding. The absence of STRING and hu.MAP support does, however, argue against interpreting the module as a known stable multiprotein complex.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported tissue-pair co-abundance pattern, because its particular gene combination is not represented as a shared high-confidence STRING interaction network or hu.MAP complex. Nevertheless, that observation alone does not establish biological novelty. The individual genes and their functions are already established, the module lacks globally significant GO or KEGG enrichment, and several members are broadly expressed or associated with common cellular processes. A cautious conclusion is that the specific breast-testis co-abundance configuration is potentially novel as a data-derived association, while its mechanistic and disease novelty remain unproven. Independent cohorts, protein-level replication, and control for cell composition would be needed to support a new biological claim.

**Hypothesis.** Hypothesis: the module reflects a shared proliferative or membrane-remodeling cellular state present in subsets of breast and testis tissue. In this model, SACM1L could influence phosphoinositide-dependent membrane organization, PDCD6IP could support vesicle formation and cytokinetic remodeling, SEH1L could mark nuclear-pore and mitotic organization, and THOP1 could contribute to intracellular peptide turnover. ART3 and CRLF3 may represent tissue- or cell-state-specific regulatory components of the same expression program. This is a hypothesis rather than an established pathway: the lack of globally significant enrichment, STRING links, and hu.MAP complexes means that direct molecular cooperation has not been demonstrated.

### Important genes

#### ART3

- **Related proteins** (co-abundance neighbors): THOP1 (0.85), SEH1L (0.83), SACM1L (0.83), PDCD6IP (0.81), CRLF3 (0.80); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Principal piece, End piece; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ADP-ribosyltransferase 3 (inactive). This gene encodes an arginine-specific ADP-ribosyltransferase. The encoded protein catalyzes a reversible reaction which modifies proteins by the addition or removal of ADP-ribose to an arginine residue to regulate the function of the modified protein. An ADP-ribosyltransferase pseudogene is located on chromosome 11. Multiple transcript variants encoding different isoforms have been found for this…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.292); bone Paget disease (0.167); atrial fibrillation (0.087); triple-negative breast carcinoma (0.081); breast carcinoma (0.076)
- **Europe PMC papers**: 649
- **Why important**: ART3 is the central network hub, connected to every other module member, and therefore is the strongest candidate for explaining the module's co-abundance structure. Its annotation identifies an inactive arginine-specific ADP-ribosyltransferase, while HPA places it in principal- and end-piece regions of testis and in spermatocyte and muscle-related cell populations. It also has disease associations including type two diabetes, Paget disease of bone, atrial fibrillation, and breast carcinoma, together with substantial literature coverage.
- **Conclusion**: Established: ART3 is the network hub and has a distinctive testis and muscle-associated expression pattern, with disease-linked literature. Hypothesis: ART3 may coordinate or report the tissue-specific cellular state represented by the module. Its hub status does not prove that it physically regulates the other proteins.

#### PDCD6IP

- **Related proteins** (co-abundance neighbors): ART3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 6 interacting protein. This gene encodes a protein that functions within the ESCRT pathway in the abscission stage of cytokinesis, in intralumenal endosomal vesicle formation, and in enveloped virus budding. Studies using mouse cells have shown that overexpression of this protein can block apoptosis. In addition, the product of this gene binds to the product of the PDCD6 gene, a protein required for apoptosis, in a calc…
- **Diseases (Open Targets)**: HIV infectious disease (0.463); anthrax infection (0.462); alcohol drinking (0.388); autosomal recessive primary microcephaly (0.386); microcephaly 29, primary, autosomal recessive (0.383)
- **Europe PMC papers**: 1668
- **Why important**: PDCD6IP is a vesicle-localized intracellular and membrane-associated protein with functions in ESCRT biology, intralumenal endosomal vesicle formation, enveloped-virus budding, apoptosis-related binding, cytokinesis, and autophagy. It is connected to ART3 in the module and has the largest literature volume among the selected genes, as well as disease associations involving infection and primary microcephaly.
- **Conclusion**: Established: PDCD6IP is a well-studied component of membrane-remodeling and cytokinetic processes and is detected in both tissues. Hypothesis: it could provide a mechanistic bridge between vesicle biology and the shared co-abundance state. The module does not establish a direct interaction between PDCD6IP and ART3.

#### SACM1L

- **Related proteins** (co-abundance neighbors): ART3 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SAC1 like phosphatidylinositide phosphatase. This gene encodes an integral membrane protein, which is localized to the endoplasmic reticulum, and functions as a phosphoinositide phosphatase that hydrolyzes phosphatidylinositol 3-phosphate, phosphatidylinositol 4-phosphate, and phosphatidylinositol 3,5-bisphosphate. Deletion of this gene in mouse results in preimplantation lethality. Other studies suggest that this gene is also involved in th…
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); placenta praevia (0.352); alcohol drinking (0.193); autoimmune disorder of central nervous system (0.175); digestive system disorder (0.077)
- **Europe PMC papers**: 1120
- **Why important**: SACM1L is an endoplasmic-reticulum and Golgi-associated phosphoinositide phosphatase involved in phosphatidylinositol metabolism, Golgi organization, and mitotic-spindle-related processes. It is detected in both tissues, has a direct module connection to ART3, has substantial literature coverage, and has disease associations including neurodegenerative disease and central-nervous-system autoimmune disorder.
- **Conclusion**: Established: SACM1L regulates membrane lipid composition and has roles relevant to organelle and mitotic organization. Hypothesis: it may connect membrane remodeling with the vesicle and cell-cycle features suggested by other module members. The co-abundance data do not demonstrate that SACM1L drives the module.

#### SEH1L

- **Related proteins** (co-abundance neighbors): ART3 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEH1 like nucleoporin. The protein encoded by this gene is part of a nuclear pore complex, Nup107-160. This protein contains WD repeats and shares 34% amino acid identity with yeast Seh1 and 30% identity with yeast Sec13. All constituents of the Nup107-160 complex, including this protein, specifically localize to kinetochores in mitosis. Two alternatively spliced transcript variants encoding distinct isoforms have been …
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); COVID-19 (0.370); Histiocytosis (0.370)
- **Europe PMC papers**: 416
- **Why important**: SEH1L is a component of the Nup107-160 nuclear-pore complex and is associated with nucleocytoplasmic transport, nuclear-pore organization, kinetochore localization, chromosome alignment, and cellular responses to nutrient or amino-acid availability. It is broadly expressed, connected to ART3 in the module, and has disease associations involving viral infection and histiocytosis.
- **Conclusion**: Established: SEH1L represents nuclear-pore and mitotic organization rather than a secreted or immune specificity signal. Hypothesis: its presence may indicate a shared transcriptional or proliferative cell state in breast and testis. There is no evidence here that SEH1L forms a physical complex with the other module members.

#### THOP1

- **Related proteins** (co-abundance neighbors): ART3 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thimet oligopeptidase 1. The protein encoded by this gene is a kininase that uses zinc as a cofactor. The encoded oligopeptidase cleaves cytosolic peptides, making them unavailable for display on antigen-presenting cells. This protein also cleaves neuropeptides under 20 aa in length and can degrade beta-amyloid precursor protein to amyloidogenic peptides. [provided by RefSeq, Nov 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.371); Hypercholesterolemia (0.325); atrial fibrillation (0.246); asthma (0.245); neuroendocrine neoplasm (0.144)
- **Europe PMC papers**: 460
- **Why important**: THOP1 is the only module member whose reported module connection is restricted to ART3, but it contributes a distinct biochemical function: cytosolic zinc-dependent cleavage of short peptides, including peptides relevant to antigen presentation and neuropeptide processing. It is detected in both tissues, has cell-type-enhanced expression in absorptive and hepatic cell types, and has disease associations including neurodegenerative disease and hypercholesterolemia.
- **Conclusion**: Established: THOP1 is a cytosolic peptide-processing enzyme with broad tissue behavior and established disease literature. Hypothesis: it may reflect intracellular proteolytic or metabolic state within the shared module. Its function is not supported as a globally enriched module pathway.

#### CRLF3

- **Related proteins** (co-abundance neighbors): ART3 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytokine receptor like factor 3. This gene encodes a cytokine receptor-like factor that may negatively regulate cell cycle progression at the G0/G1 phase. Studies of the related rat protein suggest that it may regulate neuronal morphology and synaptic vesicle biogenesis. This gene is one of several genes located in the neurofibromatosis type I tumor suppressor region on the q arm of chromosome 17, a region that is subject to micr…
- **Diseases (Open Targets)**: neurodegenerative disease (0.383); breast cancer (0.160); breast carcinoma (0.140); mouth disorder (0.135); osteoarthritis (0.128)
- **Europe PMC papers**: 294
- **Why important**: CRLF3 is the module member with tissue enhancement in lymphoid tissue and cell-type enhancement in cardiomyocytes and neutrophil-related populations, while still being detected in both breast and testis. Its annotation links it to negative regulation of cell growth, G one to S transition, transcriptional regulation, and JAK-STAT-related receptor signaling. It is connected to ART3 and has disease associations including breast cancer, breast carcinoma, neurodegenerative disease, and osteoarthritis.
- **Conclusion**: Established: CRLF3 is a receptor-like signaling and cell-growth regulator with tissue- and cell-type contextual expression. Hypothesis: it may contribute the regulatory or cell-state component of the module, especially where epithelial, muscle, or lymphoid-associated cells are present. The data do not establish a causal role in breast or testis disease.

## Module 4

**Tissue pair**: breast and testis  
**Genes (11)**: DGUOK, DNAL1, FBXW9, HACL1, HVCN1, NME7, NRDC, PIP4K2C, PSD3, STK39, VPS13A

### Function

No GO or KEGG term passed global multiple-testing correction, and STRING returned no supplementary enrichment. Therefore, the module does not support a statistically established single pathway or process. Its gene-level annotations suggest a mixed cellular program involving motile-cilium and sperm-flagellum biology, microtubule or centrosome organization, ion and redox regulation, mitochondrial nucleotide metabolism, phosphoinositide and vesicle biology, lipid alpha-oxidation, and cellular stress signaling. The strongest coherent biological signal is a ciliated or flagellated-cell context, centered on DNAL1 and NME7, but the module also contains broadly functioning metabolic, trafficking, and signaling genes. These annotations are hypotheses about module interpretation rather than globally significant enrichment.

**Cell composition.** The module is not dominated by secreted or plasma proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, while several show cell-type-enhanced expression. The recurrent cell types include early and late spermatogenic populations and multiple ciliated epithelial populations, with additional signals in choroid plexus, brain, skeletal muscle, and other cell types. Immune-cell specificity is generally low, with only HACL1 annotated as immune-cell enriched in basophils and PSD3 not detected in immune cells. Thus, a blood-cell explanation is not favored by the HPA evidence. The breast-testis sharing may instead reflect common ciliated or flagellated-cell biology, shared cellular programs, or co-abundance driven by mixtures of cell types. Protein detection is more frequent in testis than breast, and DNAL1, HVCN1, and FBXW9 are detected in testis but not breast, whereas PSD3 is not detected in either tissue. These differences caution against interpreting the module as a uniform protein complex present in both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The module has no STRING interactions above the supplied confidence threshold, and no STRING functional enrichment. No hu.MAP complex contains at least two module members. Consequently, the co-abundance edges are not corroborated by the supplied high-confidence physical-interaction resources. The network is therefore better viewed as a coordinated abundance pattern than as evidence for a known molecular complex. There is nevertheless a biologically suggestive internal structure: DNAL1 is the principal network hub and connects to HACL1, NME7, PIP4K2C, FBXW9, VPS13A, and DGUOK; HVCN1 links VPS13A, STK39, and DGUOK; and PSD3 links PIP4K2C with NRDC. These edges may represent shared regulation, cell-state composition, or indirect functional coupling rather than direct binding.

**STRING interactions (score >= 0.7)**: 0 of 55 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel tissue-pair co-abundance module, but the evidence does not establish a new molecular complex or pathway. The absence of STRING and hu.MAP support argues against simply rediscovering a well-defined annotated complex, yet absence from those resources alone cannot prove novelty. The gene set combines established cilia or flagella-associated genes with genes involved in metabolism, trafficking, signaling, and organelle maintenance, without globally significant GO or KEGG enrichment. A cautious conclusion is that the breast-testis co-abundance pattern may be a new systems-level observation, while its molecular mechanism and reproducibility require validation in independent cohorts, cell-type-aware analyses, and perturbation or localization experiments.

**Hypothesis.** Hypothesis: the module reflects a shared ciliated or flagellated-cell state rather than a single physical complex. In testis, coordinated abundance may arise from spermatogenic cells undergoing axoneme and sperm-flagellum assembly, with DNAL1 and NME7 contributing to motility-related structures. In breast or breast-associated samples, the same co-abundance pattern may reflect ciliated epithelial cells or a related cytoskeletal and organelle program. VPS13A, PIP4K2C, DGUOK, HVCN1, and STK39 could connect this structural program to membrane lipid handling, autophagy, mitochondrial nucleotide metabolism, ion or redox homeostasis, and stress signaling. This hypothesis predicts that the module will be strongest after accounting for cell-type composition, will track ciliated or spermatogenic cell abundance, and will not necessarily correspond to direct protein-protein interactions.

### Important genes

#### DNAL1

- **Related proteins** (co-abundance neighbors): HACL1 (0.91), NME7 (0.88), PIP4K2C (0.85), FBXW9 (0.83), VPS13A (0.81), DGUOK (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Basal body, Cytosol, Principal piece; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein axonemal light chain 1. This gene encodes an axonemal dynein light chain which functions as a component of the outer dynein arms complex. This complex acts as the molecular motor that provides the force to move cilia in an ATP-dependent manner. The encoded protein is expressed in tissues with motile cilia or flagella and may be involved in the movement of sperm flagella. Alternate splicing results in multiple transcript …
- **Diseases (Open Targets)**: Kartagener Syndrome (0.744); bronchiectasis (0.370); hereditary disease (0.187); Abnormality of the skeletal system (0.166); cervical carcinoma (0.112)
- **Europe PMC papers**: 331
- **Why important**: DNAL1 is the central network hub, with the broadest set of module connections. Its HPA profile is testis-enhanced and enriched in early spermatids and several ciliated epithelial cell types. Its annotated role as an axonemal dynein light-chain component, together with outer dynein-arm assembly and sperm-flagellum motility annotations, provides the clearest functional anchor for the module. Its disease associations include Kartagener syndrome and bronchiectasis, and its literature volume is substantial.
- **Conclusion**: Established evidence supports DNAL1 as a cilia and flagellum-associated structural gene and as the network's key organizational node. The hypothesis that DNAL1 helps define the shared breast-testis co-abundance state is plausible, but the module does not establish direct interactions between DNAL1 and its co-abundant neighbors.

#### NME7

- **Related proteins** (co-abundance neighbors): DNAL1 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NME/NM23 family member 7. This gene encodes a member of the non-metastatic expressed family of nucleoside diphosphate kinases. Members of this family are enzymes that catalyzes phosphate transfer from nucleoside triphosphates to nucleoside diphosphates. This protein contains two kinase domains, one of which is involved in autophosphorylation and the other may be inactive. This protein localizes to the centrosome and functi…
- **Diseases (Open Targets)**: situs inversus (0.373); blood coagulation disease (0.293); Abnormality of limbs (0.287); Thromboembolism (0.273); venous thromboembolism (0.270)
- **Europe PMC papers**: 443
- **Why important**: NME7 is directly connected to DNAL1 and has cell-type-enhanced expression in ependymal cells and respiratory ciliated cells. Its annotations link centrosomal gamma-tubulin-complex function, microtubule nucleation, nucleotide phosphate transfer, and flagellated sperm motility. The situs inversus association is relevant to ciliary biology, and its literature volume is intermediate within this module.
- **Conclusion**: Established evidence supports NME7 as a plausible bridge between centrosome or microtubule organization and motile-cilium biology. Its co-abundance with DNAL1 is consistent with a shared ciliary or flagellar state, but does not demonstrate a direct DNAL1-NME7 complex in this dataset.

#### HVCN1

- **Related proteins** (co-abundance neighbors): VPS13A (0.91), STK39 (0.89), DGUOK (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydrogen voltage gated channel 1. This gene encodes a voltage-gated protein channel protein expressed more highly in certain cells of the immune system. Phagocytic cells produce superoxide anions which require this channel protein, and in B cells this same process facilitates antibody production. This same channel protein, however, can also regulate functions in other cells including spermatozoa. Multiple transcript variants encod…
- **Diseases (Open Targets)**: Joubert syndrome (0.551); Meckel syndrome (0.548); Joubert syndrome and related disorders (0.489); neurodegenerative disease (0.349); gastroesophageal reflux disease (0.218)
- **Europe PMC papers**: 729
- **Why important**: HVCN1 occupies a connecting position between the VPS13A-DNAL1 side of the network and the STK39-DGUOK side. It is tissue-enriched in choroid plexus and cell-type-enhanced in early spermatids and late primary spermatocytes. Its voltage-gated proton-channel function is linked to intracellular pH, redox homeostasis, phagocyte activity, and spermatozoan regulation. It has a relatively large literature base and disease associations involving ciliopathy-related disorders.
- **Conclusion**: Established evidence supports HVCN1 as an ion-channel and redox-regulatory gene with relevance to sperm and selected epithelial or immune contexts. Its position suggests a possible physiological link between ion or redox state and the module, but the module does not establish that HVCN1 regulates the ciliary genes.

#### VPS13A

- **Related proteins** (co-abundance neighbors): HVCN1 (0.91), DNAL1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vacuolar protein sorting 13 homolog A. The protein encoded by this gene may control steps in the cycling of proteins through the trans-Golgi network to endosomes, lysosomes and the plasma membrane. Mutations in this gene cause the autosomal recessive disorder, chorea-acanthocytosis. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: VPS13A-related neurodegenerative disease (0.839); neurodegenerative disease (0.541); hereditary disease (0.473); open-angle glaucoma (0.296); cholelithiasis (0.269)
- **Europe PMC papers**: 902
- **Why important**: VPS13A connects HVCN1 and DNAL1 and is detected in both breast and testis, making it useful for interpreting the shared tissue-pair signal. Its functions include intracellular protein localization, Golgi-to-endosome transport, autophagy, mitochondrial organization, and phospholipid transport. Mutations cause chorea-acanthocytosis, and it has a substantial literature volume. Its myonuclear cell-type enhancement also fits a broad organelle-maintenance or specialized-cell context.
- **Conclusion**: Established evidence supports VPS13A as a trafficking, lipid-transfer, autophagy, and organelle-maintenance factor. Its network placement makes it a candidate coordinator of membrane or organelle demands associated with specialized cells, but that coordinating role remains a hypothesis rather than a demonstrated mechanism.

#### PIP4K2C

- **Related proteins** (co-abundance neighbors): DNAL1 (0.85), PSD3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphatidylinositol-5-phosphate 4-kinase type 2 gamma. Enables 1-phosphatidylinositol-4-phosphate 5-kinase activity and identical protein binding activity. Involved in several processes, including 1-phosphatidyl-1D-myo-inositol 4,5-bisphosphate biosynthetic process; negative regulation of 1-phosphatidylinositol-4-phosphate 5-kinase activity; and positive regulation of autophagosome assembly. Located in several cellular components, including autophagos…
- **Diseases (Open Targets)**: neurodegenerative disease (0.480); autoimmune disorder of central nervous system (0.347); smoking initiation (0.077); common variable immunodeficiency (0.066); isolated agammaglobulinemia (0.063)
- **Europe PMC papers**: 397
- **Why important**: PIP4K2C connects the DNAL1 hub to PSD3 and is detected in both tissues. It participates in phosphatidylinositol metabolism, phosphoinositide biosynthesis, autophagy regulation, and negative regulation of insulin-receptor signaling. Its cell-type-enhanced expression includes late spermatids and epididymal principal cells, providing a reproductive-tissue connection. Its disease associations include neurodegenerative and immune-related disorders, and its literature volume is substantial enough to support functional interpretation.
- **Conclusion**: Established evidence supports PIP4K2C as a phosphoinositide and autophagy regulator that could influence membrane organization in specialized cells. Its connection to DNAL1 is compatible with coordinated structural and membrane biology, but no direct molecular relationship between the two genes is established by STRING or hu.MAP here.

## Module 5

**Tissue pair**: breast and testis  
**Genes (6)**: APPL2, FSD1, GMPR, STX18, VPS11, VPS53

### Function

The module has no GO or KEGG term that passed global multiple-testing correction, so its function cannot be assigned from enrichment alone. Its network is a star-like co-abundance structure centered on GMPR, with links to STX18, APPL2, FSD1, VPS11, and VPS53. The gene annotations suggest convergence of intracellular purine metabolism with several vesicle-trafficking, endosomal, Golgi, lysosomal, and microtubule-related processes. This is a biologically coherent hypothesis-generating pattern, but the absence of STRING functional enrichment and the lack of globally significant GO or KEGG terms mean that the apparent convergence should not be treated as an established pathway-level annotation. The module may reflect coordinated abundance of cellular maintenance processes rather than a single canonical complex or pathway.

**Cell composition.** All module genes have HPA annotations and none is secreted, arguing against a plasma-protein module. Protein was detected in breast for most genes and in testis for all genes, consistent with the module being measurable in both tissues. The HPA profile is heterogeneous: some genes show low tissue specificity, while others are enriched in brain, skeletal muscle, tongue, or cervix. All genes show cell-type enhancement, with repeated representation among neural and glial cell types; several genes also show enhancement or grouping in immune-cell populations. GMPR is enhanced in differentiating spermatogonia and blood-cell populations, FSD1 is enriched in brain and several lymphoid or innate immune populations, and APPL2 is enhanced in Sertoli cells and neutrophils. These observations do not support a simple housekeeping interpretation, but they do raise the possibility that the shared breast–testis signal reflects common cell types, cellular composition, or broadly used intracellular trafficking and metabolic machinery rather than a tissue-specific secreted program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module gene pair reaches the supplied STRING interaction threshold, and no STRING functional enrichment is reported. No hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not independently supported here as high-confidence physical or functional interactions, and the module does not correspond to a known multi-member hu.MAP complex. The annotations nevertheless describe established cellular roles: STX18 participates in ER–Golgi membrane fusion and transport; APPL2 acts on Rab endosomal membranes; VPS11 is a core subunit of CORVET and HOPS complexes; and VPS53 is a GARP-complex subunit involved in retrograde trafficking. These established functions are relationships to cellular systems, not evidence that the module genes form one physical complex. GMPR is the network hub, but its hub status is based on the co-abundance graph and is not corroborated by STRING or hu.MAP in this fact sheet.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is a potentially novel cross-tissue co-abundance association, because its specific gene combination is not represented by high-confidence STRING links or a shared hu.MAP complex. However, absence from those resources alone does not establish novelty: the pattern could arise from correlated expression, shared cell-type composition, indirect regulation, or technical and sampling effects. The lack of globally significant GO or KEGG enrichment also prevents claiming discovery of a new pathway. The defensible conclusion is that the breast–testis co-abundance pattern is a novel candidate module requiring replication and orthogonal validation, rather than a demonstrated new molecular complex or pathway.

**Hypothesis.** Hypothesis: the module captures a coordinated cellular-maintenance state in which purine recycling through GMPR covaries with membrane and organelle trafficking. In this model, GMPR is the abundance-correlated hub, while STX18, APPL2, VPS11, and VPS53 represent ER, endosomal, lysosomal, Golgi, and recycling compartments, and FSD1 represents a possible cytoskeletal or cell-division component. The shared breast–testis signal could arise in a common cellular subpopulation, including germline-supporting or immune-associated cells, or from a conserved demand for nucleotide metabolism and vesicle traffic. This hypothesis predicts that the module should replicate across independent breast and testis datasets, remain after adjustment for cell composition, and show coordinated protein or transcript changes during perturbation of purine metabolism or intracellular trafficking.

### Important genes

#### GMPR

- **Related proteins** (co-abundance neighbors): STX18 (0.86), APPL2 (0.86), FSD1 (0.84), VPS11 (0.83), VPS53 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: guanosine monophosphate reductase. This gene encodes an enzyme that catalyzes the irreversible and NADPH-dependent reductive deamination of GMP to IMP. The protein also functions in the re-utilization of free intracellular bases and purine nucleosides.[provided by RefSeq, Oct 2009].
- **Diseases (Open Targets)**: chronic kidney disease (0.445); hypertrophic cardiomyopathy (0.333); Alzheimer disease (0.280); Abnormal blistering of the skin (0.273); disorder of appendix (0.258)
- **Europe PMC papers**: 740
- **Why important**: GMPR is the central node of the module and connects to every other member in the supplied co-abundance graph. It encodes guanosine monophosphate reductase, linking the module to irreversible GMP-to-IMP conversion and purine salvage. It is detected in both tissues, has tissue enhancement in skeletal muscle and tongue, and has substantial literature and disease-association coverage relative to several other members.
- **Conclusion**: Established evidence supports GMPR as the network hub and as a purine-metabolism enzyme. It is the strongest candidate for a coordinating metabolic signal, but the graph does not prove that GMPR regulates the other genes. Its proposed role as the biochemical anchor of the module is therefore a hypothesis.

#### VPS11

- **Related proteins** (co-abundance neighbors): GMPR (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS11 core subunit of CORVET and HOPS complexes. Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene encodes the human homolog of yeast class C Vps11 protein. The mammalian class C Vps proteins are predominantly associated with late…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 12 (0.723); neurodegenerative disease (0.527); POLR-related leukodystrophy (0.527); dystonia 32 (0.410); VPS11-related neurological disorder (0.370)
- **Europe PMC papers**: 849
- **Why important**: VPS11 is connected to the module hub and encodes a core subunit of the CORVET and HOPS vesicle-tethering complexes. Its annotations place it in endosome organization, lysosomal transport, and intracellular protein transport. It is detected in both tissues, shows broad tissue distribution, and has prominent associations with leukodystrophy, neurodegeneration, dystonia, and a VPS11-related neurological disorder.
- **Conclusion**: Established evidence supports VPS11 as a component of conserved endosomal and lysosomal trafficking machinery with important neurological disease associations. Within this module, it provides a strong trafficking interpretation, but no evidence here demonstrates a direct physical interaction with GMPR or a breast–testis-specific mechanism.

#### VPS53

- **Related proteins** (co-abundance neighbors): GMPR (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS53 subunit of GARP complex. This gene encodes a protein with sequence similarity to the yeast Vps53p protein. Vps53p is involved in retrograde vesicle trafficking in late Golgi. [provided by RefSeq, Jul 2008]
- **Diseases (Open Targets)**: pontocerebellar hypoplasia type 2E (0.732); progressive cerebello-cerebral atrophy (0.656); prostate carcinoma (0.539); neurodegenerative disease (0.528); prostate cancer (0.480)
- **Europe PMC papers**: 504
- **Why important**: VPS53 is connected to GMPR and is a subunit of the GARP complex, which supports retrograde trafficking from endosomes toward the Golgi and endocytic recycling. It is detected in both tissues and has Golgi and vesicle localization. Its disease associations include pontocerebellar hypoplasia and progressive cerebello-cerebral atrophy, making it important for interpreting the neurological and trafficking dimensions of the module.
- **Conclusion**: Established evidence supports VPS53 as a Golgi and endosomal trafficking factor with disease relevance. Its placement beside VPS11 strengthens the interpretation that vesicle transport is represented in the module, although the absence of a shared hu.MAP complex or STRING interaction means this remains functional convergence rather than proven complex membership.

#### STX18

- **Related proteins** (co-abundance neighbors): GMPR (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Plasma membrane; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntaxin 18. This gene encodes a member of the syntaxin family of soluble N-ethylmaleimide-sensitive factor attachment protein receptors (SNAREs) which is part of a membrane tethering complex that includes other SNAREs and several peripheral membrane proteins, and is involved in vesicular transport between the endoplasmic reticulum (ER) and the Golgi complex. The encoded protein is important for the organizati…
- **Diseases (Open Targets)**: neurodegenerative disease (0.523); Hyperhidrosis (0.265); trauma complication (0.248); osteoarthritis (0.248); sialolithiasis (0.230)
- **Europe PMC papers**: 330
- **Why important**: STX18 is the module’s ER- and membrane-associated member and is connected to GMPR. It encodes a syntaxin involved in ER–Golgi transport, membrane fusion, and ER organization. It is detected in both tissues and has reported ER and plasma-membrane localization, while its literature and disease-association coverage indicate that it is a recognized trafficking gene.
- **Conclusion**: Established evidence supports STX18 as an ER–Golgi SNARE and membrane-organization factor. It supplies a plausible membrane-trafficking component to the module, but the observed co-abundance edge does not establish direct coupling between STX18-mediated transport and GMPR-dependent purine metabolism.

#### APPL2

- **Related proteins** (co-abundance neighbors): GMPR (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in breast, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor protein, phosphotyrosine interacting with PH domain and leucine zipper 2. The protein encoded by this gene is one of two effectors of the small GTPase RAB5A/Rab5, which are involved in a signal transduction pathway. Both effectors contain an N-terminal Bin/Amphiphysin/Rvs (BAR) domain, a central pleckstrin homology (PH) domain, and a C-terminal phosphotyrosine binding (PTB) domain, and they bind the Rab5 through the BAR domain. They are associated with endosomal membran…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.452); injury (0.317); Hypernatremia (0.226); open-angle glaucoma (0.218); osteomyelitis (0.183)
- **Europe PMC papers**: 456
- **Why important**: APPL2 is connected to GMPR and encodes a Rab5 effector associated with endosomal membranes, signal transduction, and nuclear translocation after EGF stimulation. HPA places it in vesicles and detects it in both tissues; it is also enhanced in Sertoli cells and neutrophils, which is relevant to the shared tissue and cell-composition interpretation.
- **Conclusion**: Established evidence supports APPL2 as an endosomal signaling adaptor with roles in Rab5-associated trafficking and signal transduction. In this module it may connect vesicle state to signaling or cell-type composition, but a specific role in the breast–testis module is not established.

#### FSD1

- **Related proteins** (co-abundance neighbors): GMPR (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin type III and SPRY domain containing 1. This gene encodes a centrosome associated protein that is characterized by an N-terminal coiled-coil region downstream of B-box (BBC) domain, a central fibronectin type III domain, and a C-terminal repeats in splA and RyR (SPRY) domain. The encoded protein associates with a subset of microtubules and may be involved in the stability and organization of microtubules during cytokinesis. [provided by…
- **Diseases (Open Targets)**: neurodegenerative disease (0.198); psoriasis (0.030); erythematosquamous dermatosis (0.028); seborrheic dermatitis (0.028); glioblastoma (0.025)
- **Europe PMC papers**: 466
- **Why important**: FSD1 is connected to GMPR and encodes a centrosome-associated protein implicated in microtubule organization, cytokinesis, and mitotic-spindle organization. It is tissue enriched in brain, detected in testis but not breast, and enhanced in neuronal, spermatogonial, and selected immune-cell populations. These features make it important for considering cell-state and cytoskeletal explanations for the module.
- **Conclusion**: Established evidence supports FSD1 as a centrosome and microtubule-associated factor involved in cell division. Its testis detection and cell-type pattern make it a plausible contributor to the shared module, but the lack of breast detection and the absence of independent interaction support argue against assigning it a universal role in the module without replication.
