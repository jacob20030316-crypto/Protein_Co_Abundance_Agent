# Conserved co-abundance modules: stem_cells and testis

## Module 0

**Tissue pair**: stem_cells and testis  
**Genes (9)**: NUDT1, ACTB, BPHL, FABP5, HSD17B10, LSM8, MCM4, RAP2B, ACAA2

### Function

The module does not have a statistically supported GO or KEGG functional label: no GO or KEGG term passed global correction. Its genes instead suggest a mixed cellular state involving cytoskeletal organization and cell structure through ACTB, genome replication and replication-associated maintenance through MCM4, RNA processing through LSM8, protection from oxidized nucleotides through NUDT1, and mitochondrial lipid or steroid metabolism through ACAA2 and HSD17B10. The sparse network and absence of STRING functional enrichment argue against assigning one unified pathway. A cautious interpretation is a shared cellular-state module combining proliferative or genome-maintenance activity with mitochondrial and structural features rather than a canonical pathway module.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only FABP5 has an intracellular and membrane secretome annotation, and the genes are not blood-cell enriched according to HPA, with low immune-cell specificity throughout. Most genes have cell-type-enhanced rather than broadly uniform expression, especially in esophageal epithelial populations, late spermatids, hepatocytes, and erythrocyte progenitors. Tissue-enhanced signals include bone marrow, liver, kidney, cervix, and esophagus. This heterogeneity suggests that the shared stem-cell and testis signal may reflect a recurring cellular program or shared cell-state composition rather than a tissue-exclusive function. Testis protein detection supports the biological presence of most members there, whereas no matching HPA tissue assessment is available for stem cells. ACTB is comparatively housekeeping-like and broadly expressed, so part of the module may reflect general cellular infrastructure.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship is ACAA2 with HSD17B10. This supports a biologically plausible mitochondrial metabolic connection between fatty-acid beta-oxidation and steroid or lipid metabolism, but it does not establish that the entire module is one physical complex. The remaining module edges are co-abundance relationships without corresponding high-confidence STRING partners in the fact sheet. No hu.MAP complex contains multiple module members. Thus, known molecular support is concentrated in one mitochondrial pair, while the broader network probably combines several processes or reflects coordinated expression rather than a single stable complex.

**STRING interactions (score >= 0.7)**: 1 of 36 gene pairs: ACAA2–HSD17B10 (0.98)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a new co-abundance observation, but it cannot be called a newly discovered molecular pathway on the present evidence. Its sparse connectivity, lack of globally significant GO or KEGG enrichment, absence of STRING functional enrichment, and absence of a multi-member hu.MAP complex make a strong novelty claim inappropriate. The ACAA2-HSD17B10 relationship is already known, and ACTB, MCM4, NUDT1, FABP5, LSM8, and the other genes have established biological functions. What may be novel is their coordinated abundance across stem-cell and testis samples, particularly the juxtaposition of mitochondrial metabolism, replication, RNA processing, and cytoskeletal genes. That claim requires independent replication and control for cell-type composition.

**Hypothesis.** Hypothesis: the module marks a shared state in which metabolically active, differentiating or proliferative cells coordinate mitochondrial lipid handling with genome maintenance, RNA processing, and cytoskeletal organization. ACAA2 and HSD17B10 may form the most concrete metabolic core, while MCM4 and NUDT1 could support replication-associated genome integrity, LSM8 could support RNA maturation, and ACTB could reflect structural remodeling or abundance of a common cellular compartment. The testis and stem-cell association may therefore arise from overlapping developmental or proliferative cell states, but this remains a hypothesis and is not demonstrated by enrichment or complex evidence.

Web sources: https://en.wikipedia.org/wiki/Beta-actin; https://www.genecards.org/card/HSD17B10; https://www.genecards.org/card/ACTB; https://www.nature.com/articles/s41467-024-46572-6

### Important genes

#### ACTB

- **Related proteins** (co-abundance neighbors): RAP2B (0.93), NUDT1 (0.84), MCM4 (0.83), LSM8 (0.82), ACAA2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: actin beta. This gene encodes one of six different actin proteins. Actins are highly conserved proteins that are involved in cell motility, structure, integrity, and intercellular signaling. The encoded protein is a major constituent of the contractile apparatus and one of the two nonmuscle cytoskeletal actins that are ubiquitously expressed. Mutations in this gene cause Baraitser-Winter syndrome 1, which is …
- **Diseases (Open Targets)**: Baraitser-Winter syndrome 1 (0.814); Baraitser-Winter cerebrofrontofacial syndrome (0.745); developmental malformations-deafness-dystonia syndrome (0.742); ACTB-associated syndromic thrombocytopenia (0.701); cancer (0.614)
- **Europe PMC papers**: 53596
- **Why important**: ACTB is the principal network hub, connecting most of the module members through the co-abundance graph. It encodes a ubiquitously expressed nonmuscle actin involved in cell motility, structure, integrity, signaling, polarity, and cytoskeletal organization. Its extensive literature and associations with Baraitser-Winter syndrome, developmental disorders, and syndromic thrombocytopenia make it biologically important, while its low tissue specificity also makes it a possible general cellular-abundance or housekeeping component rather than a specific driver.
- **Conclusion**: Established evidence supports ACTB as a structural and signaling hub and as the main network connector. Hypothesis: ACTB may provide the shared cellular-state scaffold that links otherwise heterogeneous metabolic, replication, and RNA-processing signals, but the network does not prove direct physical interactions.

#### MCM4

- **Related proteins** (co-abundance neighbors): BPHL (0.85), ACTB (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: minichromosome maintenance complex component 4. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication rel…
- **Diseases (Open Targets)**: primary immunodeficiency with natural-killer cell deficiency and adrenal insufficiency (0.714); X-linked adrenal hypoplasia congenita (0.185); lung adenocarcinoma (0.112); microcephaly (0.111); neoplasm (0.102)
- **Europe PMC papers**: 4082
- **Why important**: MCM4 is connected to ACTB and BPHL and encodes a core component of the MCM replication machinery required for replication initiation, fork formation, and DNA-related processes. Its HPA profile is enhanced in bone marrow and in several germ-cell and progenitor populations, including early spermatids, late primary spermatocytes, late spermatids, and erythrocyte progenitors. It has substantial literature and disease associations involving immunodeficiency, adrenal disease, microcephaly, and neoplasia.
- **Conclusion**: Established evidence supports MCM4 as a genome-replication and progenitor-associated marker. Hypothesis: its presence may indicate a proliferative or developmental component shared by stem-cell and germ-cell populations, although the lack of globally significant enrichment prevents assigning replication as the definitive module function.

#### HSD17B10

- **Related proteins** (co-abundance neighbors): BPHL (0.85); STRING partners: ACAA2 (0.98)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydroxysteroid 17-beta dehydrogenase 10. This gene encodes 3-hydroxyacyl-CoA dehydrogenase type II, a member of the short-chain dehydrogenase/reductase superfamily. The gene product is a mitochondrial protein that catalyzes the oxidation of a wide variety of fatty acids and steroids, and is a subunit of mitochondrial ribonuclease P, which is involved in tRNA maturation. The protein has been implicated in the development of Alzheimer dise…
- **Diseases (Open Targets)**: HSD10 mitochondrial disease (0.829); HSD10 disease, atypical type (0.703); neurodegenerative disease (0.555); mitochondrial disease (0.373); HSD10 disease, neonatal type (0.370)
- **Europe PMC papers**: 1064
- **Why important**: HSD17B10 forms the strongest known STRING-supported pair in the module with ACAA2. It is a mitochondrial enzyme involved in fatty-acid and steroid oxidation, branched-chain amino-acid metabolism, and mitochondrial RNA processing, and it is associated with HSD10 mitochondrial disease and neurodegenerative disease. Its testis detection and cell-type enhancement in hepatocytes and epithelial populations support a metabolically active cellular context.
- **Conclusion**: Established evidence supports HSD17B10 as a multifunctional mitochondrial metabolic and RNA-processing protein and as one half of the module's clearest known molecular relationship. Hypothesis: it may help define a mitochondrial metabolic submodule relevant to the shared co-abundance pattern, but it cannot by itself explain the structural and replication-related members.

#### ACAA2

- **Related proteins** (co-abundance neighbors): ACTB (0.81); STRING partners: HSD17B10 (0.98)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA acyltransferase 2. The encoded protein catalyzes the last step of the mitochondrial fatty acid beta-oxidation spiral. Unlike most mitochondrial matrix proteins, it contains a non-cleavable amino-terminal targeting signal. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: bone remodeling disease (0.270); sinusitis (0.260); refractive error (0.190); kidney disorder (0.151); myopia (0.141)
- **Europe PMC papers**: 3056
- **Why important**: ACAA2 is a mitochondrial thiolase catalyzing the terminal step of mitochondrial fatty-acid beta-oxidation and is the partner of HSD17B10 in the high-confidence STRING relationship. It is tissue-enhanced in liver and cell-type-enhanced in hepatocytes, enterocytes, colonocytes, cholangiocytes, and enteric transient amplifying cells. Its established metabolic function and substantial literature make it a strong anchor for interpreting the mitochondrial component of the module.
- **Conclusion**: Established evidence supports ACAA2 as a mitochondrial fatty-acid oxidation component and as part of the only explicitly supported protein relationship in the module. Hypothesis: coordinated ACAA2 and HSD17B10 abundance may reflect lipid-fuel or steroid-related mitochondrial activity in the shared cell states, but this remains a submodule interpretation rather than a conclusion about all members.

#### NUDT1

- **Related proteins** (co-abundance neighbors): ACTB (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nudix hydrolase 1. Misincorporation of oxidized nucleoside triphosphates into DNA/RNA during replication and transcription can cause mutations that may result in carcinogenesis or neurodegeneration. The protein encoded by this gene is an enzyme that hydrolyzes oxidized purine nucleoside triphosphates, such as 8-oxo-dGTP, 8-oxo-dATP, 2-hydroxy-dATP, and 2-hydroxy rATP, to monophosphates, thereby preventing misincorpo…
- **Diseases (Open Targets)**: prostate carcinoma (0.266); schizophrenia (0.201); bipolar disorder (0.196); major depressive disorder (0.182); attention deficit-hyperactivity disorder (0.161)
- **Europe PMC papers**: 747
- **Why important**: NUDT1 is linked to ACTB in the co-abundance graph and encodes an enzyme that removes oxidized purine nucleoside triphosphates, helping prevent their incorporation into DNA and RNA. Its annotated roles include DNA repair, oxidative-stress response, and DNA protection. HPA enhancement in bone marrow and in erythrocyte progenitors and spermatogenic populations connects it to cell states with replication or differentiation demands. It also has literature and disease-relevant links to cancer and neuropsychiatric conditions.
- **Conclusion**: Established evidence supports NUDT1 as an oxidized-nucleotide sanitizing and genome-protection enzyme. Hypothesis: NUDT1 may couple oxidative metabolic conditions to genome maintenance in the module, particularly alongside MCM4, but the available network does not establish a direct NUDT1–MCM4 mechanism.

## Module 1

**Tissue pair**: stem_cells and testis  
**Genes (11)**: ACADSB, CA2, MLYCD, GMPPA, LRRC20, PPP4R3A, PITPNA, RAB32, OXCT1, STXBP2, SUGP2

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established single pathway function. The gene annotations instead suggest a heterogeneous combination of intracellular trafficking and vesicle biology, lipid and acyl-CoA metabolism, mitochondrial energy use, RNA processing, glycosylation-related metabolism, and intracellular pH regulation. The strongest biological interpretation is therefore a shared co-abundance program involving cellular transport, metabolic state, and specialized cell functions rather than a canonical pathway. The concentration of late spermatid annotations, together with platelet and neutrophil annotations, may indicate a mixture of cell-state programs rather than one unified molecular machine.

**Cell composition.** The module is not dominated by secreted or plasma proteins; all listed genes lack secretome annotation. It is also not uniformly blood-cell specific: most genes have low immune-cell specificity, although several show immune-cell enhancement, particularly in basophils, monocytes, neutrophils, or megakaryocyte-related populations. HPA evidence points to a mixed composition, with enhanced signals across skeletal muscle or tongue, liver, choroid plexus, intestine, stomach, bone marrow, lymphoid tissue, and heart muscle, as well as late spermatids and other specialized cell types. This diversity argues against a simple plasma-protein signature, but a shared abundance pattern could still reflect variable representation of spermatid, platelet, neutrophil, or other cell populations in the tissue samples. Protein detection in testis supports biological presence for most genes assessed there, while no matching HPA tissue evidence is available for stem cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and no hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not corroborated as established physical protein interactions or as membership in a known multiprotein complex. The absence of STRING and hu.MAP support means the network is best interpreted as a coordinated expression or abundance pattern, not as a demonstrated physical interaction network. Several individual functions remain biologically compatible with intracellular transport, metabolism, and vesicle regulation, but those relationships are not established as direct connections within this module.

**STRING interactions (score >= 0.7)**: 0 of 55 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a previously unrecognized tissue-pair co-abundance pattern, because the module links genes from distinct functional areas without support from known STRING interactions or shared hu.MAP complexes. However, it cannot be called a new biological mechanism on that basis alone. The absence of database relationships may reflect context-specific regulation, incomplete interaction coverage, indirect co-regulation, or a mixture of cell types. The appropriate novelty claim is therefore limited: the conserved abundance pattern may be novel in the stem-cell and testis comparison, whereas the individual gene functions and disease associations are already established to varying degrees.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular-state program shared by selected stem-cell and testis populations, particularly cells undergoing specialized differentiation or high biosynthetic and trafficking demands. In this model, PITPNA and RAB32 could coordinate membrane-lipid handling and vesicle or organelle trafficking; STXBP2 could represent regulated vesicle fusion or degranulation-related machinery; MLYCD, ACADSB, and OXCT1 could reflect mitochondrial and lipid or ketone metabolic support; and CA2 could help accommodate intracellular pH and transport requirements. The mixed HPA cell-type pattern suggests that this apparent program may arise from convergent cellular demands or shared cell-type composition rather than direct cooperation among all module proteins. This hypothesis requires validation with cell-resolved expression, perturbation, and protein-interaction experiments.

### Important genes

#### STXBP2

- **Related proteins** (co-abundance neighbors): PPP4R3A (0.85), MLYCD (0.82), LRRC20 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntaxin binding protein 2. This gene encodes a member of the STXBP/unc-18/SEC1 family. The encoded protein is involved in intracellular trafficking, control of SNARE (soluble NSF attachment protein receptor) complex assembly, and the release of cytotoxic granules by natural killer cells. Mutations in this gene are associated with familial hemophagocytic lymphohistiocytosis. Alternatively spliced transcript variants encoding…
- **Diseases (Open Targets)**: Familial hemophagocytic lymphohistiocytosis (0.823); autoinflammatory syndrome (0.466); hereditary hemophagocytic lymphohistiocytosis (0.372); hereditary disease (0.342); Thrombocytopenia (0.153)
- **Europe PMC papers**: 1259
- **Why important**: STXBP2 is one of the more connected genes in the module and links the trafficking-related portion of the network to PPP4R3A, MLYCD, and LRRC20. Its established role in SNARE-complex assembly, intracellular transport, cytotoxic-granule release, neutrophil degranulation, and mast-cell degranulation makes it a strong candidate for interpreting the vesicle-related aspect of the pattern. It also has a well-developed literature and a strong association with familial hemophagocytic lymphohistiocytosis and other inflammatory disorders. HPA links it to late spermatids and multiple immune or myeloid populations.
- **Conclusion**: Established evidence supports STXBP2 as a vesicle-trafficking and regulated-secretion gene with relevance to immune-cell function. Its position in this module is consistent with a shared trafficking state, but the module does not establish a direct STXBP2 interaction with its neighboring genes or prove that immune degranulation is the module function. A role in testis-related trafficking remains a hypothesis.

#### RAB32

- **Related proteins** (co-abundance neighbors): PITPNA (0.85), GMPPA (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB32, member RAS oncogene family. The protein encoded by this gene anchors the type II regulatory subunit of protein kinase A to the mitochondrion and aids in mitochondrial fission. The encoded protein also appears to be involved in autophagy and melanosome secretion. Variations in this gene may be linked to leprosy. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.450); Abnormal skin pigmentation (0.405); fragile X syndrome (0.333); cardiomyopathy (0.252); ovarian dysfunction (0.184)
- **Europe PMC papers**: 1303
- **Why important**: RAB32 connects PITPNA with GMPPA and is annotated for intracellular transport, mitochondrial organization, autophagy, and melanosome secretion. It has substantial literature support and disease links including leprosy, neurodegenerative disease, pigmentation abnormalities, fragile X syndrome, and cardiomyopathy. HPA associates it with bone marrow, megakaryocytes, Hofbauer cells, Kupffer cells, melanocytes, and late spermatids, making it particularly informative for the module's mixture of trafficking, organelle, blood-related, and testis-related signals.
- **Conclusion**: Established evidence supports RAB32 as a regulator of organelle and vesicle-associated processes. Its network placement and HPA profile make it a plausible bridge between lipid handling and specialized-cell trafficking. It is not established that RAB32 mechanistically connects the other module genes in stem cells or testis; that interpretation remains a hypothesis.

#### PITPNA

- **Related proteins** (co-abundance neighbors): LRRC20 (0.90), RAB32 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphatidylinositol transfer protein alpha. This gene encodes a member of a family of lipid-binding proteins that transfer molecules of phosphatidylinositol or phosphatidylcholine between membrane surfaces. The protein is implicated in phospholipase C signaling and in the production of phosphatidylinositol 3,4,5-trisphosphate (PIP3) by phosphoinositide-3-kinase.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.517); dermatophytosis (0.244); response to bronchodilator (0.239); rosacea (0.185); food allergy (0.178)
- **Europe PMC papers**: 389
- **Why important**: PITPNA links LRRC20 and RAB32 and provides a mechanistic connection to phosphatidylinositol and phosphatidylcholine transfer, phospholipid transport, lipid translocation, and phosphoinositide signaling. Its literature base is substantial, and its disease associations include neurodegenerative disease, dermatophytosis, bronchodilator response, rosacea, and food allergy. HPA shows enhancement in neutrophils, retinal pigment epithelial cells, and syncytiotrophoblasts, supporting broad relevance to membrane and specialized-cell biology.
- **Conclusion**: Established evidence supports PITPNA as a membrane-lipid transfer and signaling component. Its location in the module is compatible with a membrane-trafficking interpretation and with the RAB32 connection. The proposed role in coordinating the entire module, or specifically in testis and stem-cell biology, is not established by the supplied evidence.

#### MLYCD

- **Related proteins** (co-abundance neighbors): SUGP2 (0.84), STXBP2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: malonyl-CoA decarboxylase. The product of this gene catalyzes the breakdown of malonyl-CoA to acetyl-CoA and carbon dioxide. Malonyl-CoA is an intermediate in fatty acid biosynthesis, and also inhibits the transport of fatty acyl CoAs into mitochondria. Consequently, the encoded protein acts to increase the rate of fatty acid oxidation. It is found in mitochondria, peroxisomes, and the cytoplasm. Mutations in this gene resu…
- **Diseases (Open Targets)**: malonic aciduria (0.813); hypertrophic cardiomyopathy (0.370); placenta praevia (0.354); alcohol drinking (0.313); preeclampsia (0.303)
- **Europe PMC papers**: 692
- **Why important**: MLYCD links STXBP2 with SUGP2 and represents a metabolic arm of the module. Its enzyme product controls malonyl-CoA breakdown and thereby influences acetyl-CoA production and fatty-acid oxidation across mitochondrial, peroxisomal, and cytoplasmic compartments. It has substantial literature and a strong association with malonic aciduria, as well as links to hypertrophic cardiomyopathy, placenta praevia, alcohol drinking, and preeclampsia. HPA shows enhancement in tongue and several neural, glial, epithelial, photoreceptor, and muscle-related cell types, while it is not detected in immune cells.
- **Conclusion**: Established evidence supports MLYCD as a regulator of acyl-CoA and energy metabolism rather than a trafficking protein. Its connection to STXBP2 in this network may indicate coordinated metabolic and vesicular cell-state regulation, but it may also reflect indirect co-abundance or mixed cell composition. A direct metabolic contribution to the shared stem-cell and testis program is therefore a hypothesis.

#### CA2

- **Related proteins** (co-abundance neighbors): PPP4R3A (0.84), OXCT1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carbonic anhydrase 2. The protein encoded by this gene is one of several isozymes of carbonic anhydrase, which catalyzes reversible hydration of carbon dioxide. Defects in this enzyme are associated with osteopetrosis and renal tubular acidosis. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2014].
- **Diseases (Open Targets)**: autosomal recessive osteopetrosis 3 (0.821); glaucoma (0.614); epilepsy (0.608); ocular hypertension (0.606); open-angle glaucoma (0.602)
- **Europe PMC papers**: 275895
- **Why important**: CA2 links PPP4R3A and OXCT1 and is a well-studied enzyme involved in reversible carbon-dioxide hydration, intracellular pH regulation, and anion transport. It has extensive literature and established disease associations including autosomal recessive osteopetrosis, glaucoma, epilepsy, and ocular hypertension. HPA associates it with choroid plexus, intestine, stomach, erythroid populations, extravillous trophoblasts, foveolar cells, basophils, and testis, highlighting broad epithelial, blood-related, and reproductive relevance.
- **Conclusion**: Established evidence supports CA2 as a pH and transport regulator with important tissue-specific disease consequences. Its network placement may mark physiological transport or metabolic demands in the module, but there is no evidence that CA2 forms a physical complex with PPP4R3A or OXCT1 here. Its proposed contribution to a shared stem-cell and testis mechanism remains unproven.

## Module 2

**Tissue pair**: stem_cells and testis  
**Genes (15)**: ALG1, ARMC8, EML2, ETFDH, FKBP4, GMDS, HOOK1, HSPH1, PHKA2, NDRG1, C17orf75, LCP1, PPP3CA, PPM1F, XPNPEP1

### Function

No GO or KEGG term passed global correction, so the module does not have a statistically established pathway annotation from enrichment analysis. The gene-level evidence instead suggests a mixed cellular program involving cytoskeletal organization and intracellular transport, mitochondrial and carbohydrate metabolism, protein folding and stress handling, glycosylation, and germ-cell-associated biology. EML2 is the principal network connector and links genes with microtubule, trafficking, phosphatase, metabolic, and cytoskeletal annotations. HOOK1 and C17orf75 support a microtubule-linked vesicle-transport theme, while GMDS and ALG1 support glycan and GDP-fucose-related biosynthetic functions. These themes should be regarded as biological interpretation of the member genes rather than as globally significant enrichment. The module may therefore represent a shared cell-state or structural-metabolic program rather than a single canonical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and many are detected in testis, indicating that the shared signal may reflect broadly used cellular machinery together with testis-associated expression rather than a narrowly tissue-specific secretory program. Cell-type annotations are diverse, including neutrophils, monocytes, epithelial and secretory cell types, spermatogenic cells, and other specialized cells. Although some genes have immune-cell or blood-cell annotations, the overall blood-cell specificity is low, so a blood-contamination explanation is not established. LCP1 is especially compatible with hematopoietic or actin-remodeling biology, whereas HOOK1, C17orf75, FKBP4, and PHKA2 have annotations relevant to spermatogenic or testicular cell states. HPA protein detection in testis is widespread among the module members, but the lack of matching stem-cell tissue data limits direct comparison between the two tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The physical-interaction evidence is limited. The only high-confidence STRING relationship among module members is ALG1 with GMDS, providing independent support for a possible connection between lipid-linked oligosaccharide assembly and GDP-fucose biosynthesis. No STRING functional-enrichment result was reported, and no hu.MAP complex contains multiple module members. Thus, most co-abundance links are not independently supported as known physical interactions or shared complexes. The sparse external interaction support argues against interpreting the module as a well-established protein complex. Instead, it is more consistent with coordinated expression of proteins from partially related cellular processes, with the ALG1-GMDS relationship being the clearest known molecular connection.

**STRING interactions (score >= 0.7)**: 1 of 105 gene pairs: ALG1–GMDS (0.872)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The co-abundance module can reasonably be described as a potentially new cross-tissue association, because the complete member set is not represented by a known hu.MAP complex and has very limited STRING support. However, this does not establish biological novelty: database coverage is incomplete, co-abundance is not equivalent to physical interaction, and the individual genes and several of their functions are already well established. The strongest defensible conclusion is that the shared stem-cell and testis co-abundance pattern is not explained by an already documented protein complex in the supplied resources, but its biological novelty requires independent replication, cell-composition control, and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a shared structural and proteostatic state in stem-cell and testicular cell populations, in which microtubule organization and vesicle trafficking are coordinated with mitochondrial energy handling, glycosylation, protein folding, and stress adaptation. EML2 may organize the structural side of this program, HOOK1 and C17orf75 may connect it to intracellular transport, and GMDS with ALG1 may provide a glycan-biosynthetic component. In testis, this could relate to the specialized cytoskeletal and trafficking demands of germ-cell development; in stem cells, it could instead mark a comparable state of remodeling or differentiation. This is a hypothesis rather than a demonstrated causal mechanism.

### Important genes

#### EML2

- **Related proteins** (co-abundance neighbors): ARMC8 (0.86), XPNPEP1 (0.85), PPP3CA (0.83), HOOK1 (0.83), NDRG1 (0.82), ALG1 (0.81), LCP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EMAP like 2. Enables microtubule binding activity. Involved in negative regulation of microtubule polymerization and regulation of microtubule nucleation. Colocalizes with mitotic spindle. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.445); Abnormality of the skeletal system (0.299); cervical carcinoma (0.289); type 2 diabetes mellitus (0.232); diabetes mellitus (0.195)
- **Europe PMC papers**: 326
- **Why important**: EML2 has the strongest network connectivity in the module and connects multiple otherwise weakly connected branches, including ARMC8, XPNPEP1, PPP3CA, HOOK1, NDRG1, ALG1, and LCP1. Its established annotations involve microtubule binding, regulation of microtubule polymerization, microtubule nucleation, and mitotic-spindle localization. Its HPA profile includes testis detection and cell-type enhancement in syncytiotrophoblasts and rod photoreceptor cells. The relatively substantial literature and disease associations make it a plausible structural organizer, although no STRING or hu.MAP support independently confirms that role in this module.
- **Conclusion**: Established evidence supports EML2 as the central co-abundance connector and a regulator of microtubule-related biology. It is a leading candidate for coordinating the module's structural component, but its proposed organizing role in this particular module remains hypothetical.

#### GMDS

- **Related proteins** (co-abundance neighbors): ETFDH (0.90), ALG1 (0.85); STRING partners: ALG1 (0.872)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GDP-mannose 4,6-dehydratase. GDP-mannose 4,6-dehydratase (GMD; EC 4.2.1.47) catalyzes the conversion of GDP-mannose to GDP-4-keto-6-deoxymannose, the first step in the synthesis of GDP-fucose from GDP-mannose, using NADP+ as a cofactor. The second and third steps of the pathway are catalyzed by a single enzyme, GDP-keto-6-deoxymannose 3,5-epimerase, 4-reductase, designated FX in humans (MIM 137020).[supplied by OMIM, Aug 2009…
- **Diseases (Open Targets)**: open-angle glaucoma (0.497); glaucoma (0.475); Abnormality of the skeletal system (0.474); gastroesophageal reflux disease (0.390); coronary artery disorder (0.373)
- **Europe PMC papers**: 1256
- **Why important**: GMDS occupies the clearest externally supported interaction in the module through its STRING relationship with ALG1. It catalyzes an early step in GDP-fucose production and is annotated for GDP-mannose metabolism, GDP-L-fucose biosynthesis, and Notch signaling. Its HPA pattern is enhanced in gastrointestinal and glandular tissues and in several mucous or epithelial cell types, while protein is detected in testis. Its disease associations and substantial literature provide strong prior biological context.
- **Conclusion**: Established evidence supports GMDS as a GDP-fucose biosynthetic enzyme and as the member with the best-supported molecular link to another module gene. A role for altered glycosylation in the shared co-abundance program is plausible, but the module data do not establish that GMDS drives the module or that Notch signaling is enriched.

#### ALG1

- **Related proteins** (co-abundance neighbors): GMDS (0.85), EML2 (0.81); STRING partners: GMDS (0.872)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ALG1 chitobiosyldiphosphodolichol beta-mannosyltransferase. The enzyme encoded by this gene catalyzes the first mannosylation step in the biosynthesis of lipid-linked oligosaccharides. This gene is mutated in congenital disorder of glycosylation type Ik. [provided by RefSeq, Dec 2008].
- **Diseases (Open Targets)**: ALG1-congenital disorder of glycosylation (0.857); congenital disorder of glycosylation (0.613); neurodegenerative disease (0.536); hereditary disease (0.510); congenital disorder of glycosylation type I (0.436)
- **Europe PMC papers**: 695
- **Why important**: ALG1 is directly paired with GMDS in STRING and encodes an enzyme required for the first mannosylation step of lipid-linked oligosaccharide and protein N-linked glycosylation. It is located in the endoplasmic reticulum, is detected in testis, and has a strong established association with congenital disorders of glycosylation. Its network position is modest, but its functional complementarity with GMDS makes it important for interpreting the only independently supported interaction.
- **Conclusion**: Established evidence supports ALG1 as an endoplasmic-reticulum glycosylation enzyme and supports its known relationship with GMDS. The hypothesis that coordinated ALG1 and GMDS expression reflects a glycan-processing axis in the module is reasonable, but it is not supported by globally significant enrichment.

#### ETFDH

- **Related proteins** (co-abundance neighbors): GMDS (0.90), PPM1F (0.85), FKBP4 (0.83), HSPH1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein dehydrogenase. This gene encodes a component of the electron-transfer system in mitochondria and is essential for electron transfer from a number of mitochondrial flavin-containing dehydrogenases to the main respiratory chain. Mutations in this gene are associated with glutaric acidemia. Alternatively spliced transcript variants that encode distinct isoforms have been observed. [provided by RefSeq, Aug 2013].
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.845); glutaric acidemia IIc (0.704); glutaric aciduria (0.670); hereditary disease (0.523); Abnormality of metabolism/homeostasis (0.407)
- **Europe PMC papers**: 1273
- **Why important**: ETFDH is a central connector within the metabolic and stress-related portion of the module, linking GMDS, PPM1F, FKBP4, and HSPH1. It is a mitochondrial electron-transfer component required for respiratory-chain electron transfer from several flavin-containing dehydrogenases and is involved in fatty-acid beta-oxidation and oxidative-stress responses. Its established disease associations include glutaric acidemia and multiple acyl-CoA dehydrogenase deficiency. HPA shows tissue enhancement in liver and tongue, mitochondrial localization, and testis detection.
- **Conclusion**: Established evidence supports ETFDH as a mitochondrial energy-metabolism and oxidative-stress gene. Its network position suggests that metabolic and proteostatic functions may be coordinated in the module, but this interpretation remains a network-based hypothesis rather than a demonstrated pathway mechanism.

#### NDRG1

- **Related proteins** (co-abundance neighbors): ARMC8 (0.88), EML2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Connecting piece, Mid piece, Principal piece, End piece; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-myc downstream regulated 1. This gene is a member of the N-myc downregulated gene family which belongs to the alpha/beta hydrolase superfamily. The protein encoded by this gene is a cytoplasmic protein involved in stress responses, hormone responses, cell growth, and differentiation. The encoded protein is necessary for p53-mediated caspase activation and apoptosis. Mutations in this gene are a cause of Charcot-Marie-Tooth d…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease type 4D (0.744); Charcot-Marie-Tooth disease type 4 (0.551); hereditary disease (0.453); Charcot-Marie-Tooth disease (0.431); lung carcinoma (0.392)
- **Europe PMC papers**: 5908
- **Why important**: NDRG1 links EML2 with ARMC8 and has a broad functional profile involving stress responses, hormone responses, cell growth, differentiation, hypoxia response, and p53-mediated apoptosis. It is detected in testis and has a distinctive localization across sperm structural regions, while its cell-type annotations include epithelial and pancreatic populations. It has the largest literature volume among the selected genes and established associations with Charcot-Marie-Tooth disease and cancer-related biology. Its position near the module's structural hub makes it a useful candidate for connecting cytoskeletal state with differentiation and stress responses.
- **Conclusion**: Established evidence supports NDRG1 as a stress- and differentiation-associated gene with relevance to testicular cellular structures and disease. Its placement beside EML2 supports a possible bridge between structural organization and cellular stress adaptation, but the direction and mechanism of that relationship are not established.

## Module 3

**Tissue pair**: stem_cells and testis  
**Genes (7)**: ATAD1, DYNC2LI1, NDUFA6, NDUFV1, DDOST, PHB2, TM9SF4

### Function

The module most plausibly reflects mitochondrial respiratory-chain biology coupled to broader intracellular protein-handling and organelle-maintenance processes. The strongest direct functional evidence is the STRING-supported NDUFA6–NDUFV1 relationship and the repeated hu.MAP membership of these genes in respiratory-chain complex I-related assemblies (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1). NDUFA6 is an accessory component involved in complex I assembly and mitochondrial electron transfer, while NDUFV1 is a core complex I subunit carrying the NADH-binding site. ATAD1 and PHB2 add mitochondrial membrane-protein quality control and mitochondrial organization context, respectively. DYNC2LI1 contributes a ciliary retrograde-transport function, DDOST represents endoplasmic-reticulum oligosaccharyltransferase biology, and TM9SF4 represents Golgi, endosomal, intracellular-pH, and vacuolar ATPase-related biology. No GO/KEGG term passed global correction; therefore the functional interpretation is driven by the gene annotations and network/complex evidence rather than significant enrichment. The absence of a globally enriched term does not invalidate the module.

**Cell composition.** The module is not composed of plasma or secreted proteins: HPA reports no secreted genes. All genes have low tissue specificity, and most have low immune-cell specificity, so the shared signal does not resemble a blood-cell or plasma-protein module. HPA does not indicate a broad tissue-specific signature. Several genes show cell-type-enhanced patterns in specialized cells, including spermatids, trophoblast populations, parietal cells, enterocytes, hepatocytes, oocytes, and other differentiated cell types. Protein detection is reported for most assessed genes in testis, whereas there is no matching HPA tissue for the stem-cell group. Thus, the module could partly reflect shared mitochondrial or general organelle requirements of particular cell states, with a possible contribution from germ-cell biology, but the available HPA evidence does not establish a specific shared cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING identifies only the NDUFA6–NDUFV1 pair as a high-confidence interaction, directly supporting a complex I relationship. The remaining module edges are not independently supported by STRING at the stated threshold, so the co-abundance network should not be interpreted as a fully established physical interaction network. hu.MAP provides convergent complex-level support: NDUFA6 and NDUFV1 repeatedly occur together across several respiratory-chain assemblies (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1), while ATAD1 and NDUFA6 co-occur in (hu.MAP huMAP3_07029.1), and ATAD1 and PHB2 co-occur in (hu.MAP huMAP3_10725.1). However, each hu.MAP complex contains many additional members and only a small subset is represented in this module. These data support a shared organelle and complex-I-related context, while also indicating that co-abundance extends beyond known direct physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: NDUFA6–NDUFV1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07029.1 (NDUFA6, ATAD1; 2/8); huMAP3_02819.1 (NDUFV1, NDUFA6; 2/34); huMAP3_14018.1 (NDUFV1, NDUFA6; 2/48); huMAP3_06397.1 (NDUFV1, NDUFA6; 2/49); huMAP3_09982.1 (NDUFV1, NDUFA6; 2/49); huMAP3_09567.1 (NDUFV1, NDUFA6; 2/52); huMAP3_14878.1 (NDUFV1, NDUFA6; 2/53); huMAP3_10725.1 (ATAD1, PHB2; 2/59)

### Novelty

This is not established as a wholly new molecular complex or pathway. The NDUFA6–NDUFV1 relationship is already represented in STRING, and the repeated complex memberships of NDUFA6 and NDUFV1 are already represented in hu.MAP. The module may nevertheless be a potentially novel tissue-pair co-abundance pattern because the exact combination of mitochondrial, ciliary, endoplasmic-reticulum, and membrane-homeostasis genes is not shown here as a previously defined unit. That claim remains provisional: absence of the full module from STRING or hu.MAP would not prove novelty, and the limited direct interaction support argues for validation in independent datasets and experiments.

**Hypothesis.** Hypothesis: in stem-cell and testis-related cellular states, coordinated demand for mitochondrial complex I activity and organelle quality control produces the central NDUFA6–NDUFV1 signal, while ATAD1 and PHB2 connect mitochondrial membrane maintenance to broader proteostasis and membrane-organelle organization. DDOST, DYNC2LI1, and TM9SF4 may reflect parallel requirements for secretory-pathway processing, ciliary transport, and endosomal or vacuolar homeostasis. This model predicts that the module should track mitochondrial respiratory capacity and organelle stress or differentiation state rather than represent a single stable physical complex. It remains a hypothesis because global GO/KEGG enrichment was absent and most pairwise module relationships lack high-confidence STRING support.

### Important genes

#### NDUFA6

- **Related proteins** (co-abundance neighbors): NDUFV1 (0.86), ATAD1 (0.83); STRING partners: NDUFV1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, End piece; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07029.1, huMAP3_02819.1, huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit A6. This gene encodes a member of the LYR family of proteins that contain a highly conserved tripeptide (LYR) motif near the N-terminus. The encoded protein is an accessory subunit of NADH: ubiquinone oxidorerductase (Complex I), which is the largest enzyme of the mitochondrial membrane respiratory chain. Complex I functions in electron transfer from NADH to the respiratory chain. [provided by RefSeq,…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 33 (0.709); type 2 diabetes mellitus (0.609); mitochondrial complex I deficiency (0.601); diabetes mellitus (0.578); neurodegenerative disease (0.567)
- **Europe PMC papers**: 1085
- **Why important**: NDUFA6 is a central network gene, connecting NDUFV1 and ATAD1, and it is the most repeatedly represented module member in hu.MAP respiratory-chain assemblies (hu.MAP huMAP3_07029.1) (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1). Its established function as a complex I accessory subunit links the module directly to mitochondrial electron transfer, complex I assembly, proton-motive-force generation, and oxidative phosphorylation. It also has a substantial literature base and disease associations involving complex I deficiency, diabetes, and neurodegenerative disease.
- **Conclusion**: Established evidence supports NDUFA6 as a core anchor of the module's mitochondrial complex-I interpretation. Its role as a driver of the shared tissue-pair co-abundance pattern is a hypothesis requiring perturbation or replication.

#### NDUFV1

- **Related proteins** (co-abundance neighbors): NDUFA6 (0.86), TM9SF4 (0.80); STRING partners: NDUFA6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_02819.1, huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit V1. The mitochondrial respiratory chain provides energy to cells via oxidative phosphorylation and consists of four membrane-bound electron-transporting protein complexes (I-IV) and an ATP synthase (complex V). This gene encodes a 51 kDa subunit of the NADH:ubiquinone oxidoreductase complex I; a large complex with at least 45 nuclear and mitochondrial encoded subunits that liberates electrons from NAD…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.788); mitochondrial complex I deficiency, nuclear type 4 (0.724); mitochondrial complex I deficiency, nuclear type 1 (0.685); Leigh syndrome (0.635); type 2 diabetes mellitus (0.609)
- **Europe PMC papers**: 4567
- **Why important**: NDUFV1 is a network connector between NDUFA6 and TM9SF4, has the only direct high-confidence STRING relationship in the module through NDUFA6, and recurs with NDUFA6 across multiple hu.MAP respiratory-chain assemblies (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1). It is a core complex I subunit containing the NADH-binding site, making it mechanistically important for electron transfer. It has the largest literature volume in the module and established associations with complex I deficiency, Leigh syndrome, and diabetes.
- **Conclusion**: Established evidence makes NDUFV1 the strongest functional and interaction-supported marker of the module. Whether its co-abundance specifically reflects altered complex I activity in both tissue groups remains a hypothesis.

#### ATAD1

- **Related proteins** (co-abundance neighbors): DYNC2LI1 (0.91), NDUFA6 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoli rim; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07029.1, huMAP3_10725.1
- **Function (MyGene.info)**: ATPase family AAA domain containing 1. Predicted to enable ATP binding activity and transmembrane protein dislocase activity. Involved in extraction of mislocalized protein from mitochondrial outer membrane. Located in mitochondrial outer membrane and peroxisomal membrane. Implicated in hyperekplexia 4. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hyperekplexia 4 (0.637); hereditary hyperekplexia (0.596); neurodegenerative disease (0.503); spondyloepimetaphyseal dysplasia, PAPSS2 type (0.486); placenta praevia (0.215)
- **Europe PMC papers**: 345
- **Why important**: ATAD1 occupies a bridging position between DYNC2LI1 and NDUFA6 and is represented in hu.MAP complexes with NDUFA6 (hu.MAP huMAP3_07029.1) and PHB2 (hu.MAP huMAP3_10725.1). Its established function is ATP-dependent extraction of mislocalized proteins from the mitochondrial outer membrane, providing a plausible quality-control link to the respiratory-chain signal. HPA shows enrichment in early and late spermatids, and disease evidence includes hereditary hyperekplexia.
- **Conclusion**: Established evidence supports ATAD1 as a mitochondrial membrane-proteostasis component that may connect the module to germ-cell state. Its proposed role as a coordinator between complex I biology and protein quality control is a hypothesis.

#### PHB2

- **Related proteins** (co-abundance neighbors): DDOST (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_10725.1
- **Function (MyGene.info)**: prohibitin 2. Enables several functions, including protein C-terminus binding activity; protein N-terminus binding activity; and protein dimerization activity. Involved in several processes, including defense response to virus; positive regulation of cell cycle phase transition; and regulation of transcription, DNA-templated. Located in several cellular components, including cell surface; mitochondrial membrane…
- **Diseases (Open Targets)**: breast cancer (0.101); breast carcinoma (0.101); neoplasm (0.100); non-small cell lung carcinoma (0.096); colorectal carcinoma (0.085)
- **Europe PMC papers**: 2714
- **Why important**: PHB2 is connected to DDOST in the module and appears with ATAD1 in hu.MAP complex (hu.MAP huMAP3_10725.1). It is an established component of the mitochondrial prohibitin complex and is annotated in mitochondrial organization and mitophagy, making it relevant to organelle integrity. It also has a substantial literature base and reported links to transcription, cell-cycle regulation, antiviral defense, and cancer-related disease contexts.
- **Conclusion**: Established evidence supports PHB2 as an organelle-organization and mitochondrial-quality-control contributor. Its connection to the module's respiratory-chain signal is plausible but not directly demonstrated by the available interaction evidence.

#### DYNC2LI1

- **Related proteins** (co-abundance neighbors): ATAD1 (0.91), DDOST (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Cytosol, Mid piece; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 2 light intermediate chain 1. This gene encodes a protein that is a component of the dynein-2 microtubule motor protein complex that plays a role in the retrograde transport of cargo in primary cilia via the intraflagellar transport system. This gene is ubiquitously expressed and its protein, which localizes to the axoneme and Golgi apparatus, interacts directly with the cytoplasmic dynein 2 heavy chain 1 protein to form part …
- **Diseases (Open Targets)**: Ellis-van Creveld syndrome (0.748); Jeune syndrome (0.666); sitosterolemia (0.567); sitosterolemia 2 (0.563); Abnormality of the cardiovascular system (0.539)
- **Europe PMC papers**: 277
- **Why important**: DYNC2LI1 has a relatively central position in the small module, linking ATAD1 and DDOST. It is an established component of the cytoplasmic dynein two motor complex and is involved in retrograde transport within primary cilia and cilium assembly. HPA shows cell-type enhancement in late primary spermatocytes and detection in testis, while disease associations include ciliopathy syndromes such as Ellis-van Creveld syndrome and Jeune syndrome.
- **Conclusion**: Established evidence supports DYNC2LI1 as a ciliary-transport gene with relevance to testis-associated cell states. Its connection to mitochondrial and secretory-pathway genes is a network-based hypothesis rather than an established shared biochemical complex.

## Module 4

**Tissue pair**: stem_cells and testis  
**Genes (6)**: COL1A2, COL6A1, IDH2, LAMC1, QKI, STX7

### Function

The module is best interpreted as an extracellular-matrix and cell-adhesion program. The primary evidence is (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0432), the globally corrected KEGG ECM-receptor interaction term, supported by COL1A2, COL6A1, and LAMC1. These genes encode structural extracellular-matrix components: type I collagen, collagen VI, and laminin gamma one. The supplementary STRING results reinforce an ECM, focal-adhesion, and PI3K-Akt-associated interpretation (7 supplementary STRING terms; within-query FDR 0.0032–0.046), but they are not additional globally corrected evidence. COL1A2 is the central co-abundance hub and connects the ECM genes with QKI, IDH2, and STX7, while the latter genes do not independently support a specific enriched pathway. Overall, the module most plausibly reflects extracellular-matrix organization, basement-membrane or stromal structure, and signaling through cell-matrix contacts rather than a canonical intracellular complex.

**Cell composition.** The composition strongly favors extracellular-matrix biology: COL1A2, COL6A1, and LAMC1 are secreted to or associated with the extracellular matrix according to HPA evidence. HPA single-cell annotations repeatedly point to fibroblasts, fibro-adipogenic progenitors, and stromal populations, with additional enrichment in decidual and endometrial stromal cells. This makes a stromal or mesenchymal source plausible in both tissues. The module is not dominated by broadly expressed housekeeping genes. It is also unlikely to be primarily explained by circulating immune cells, because several genes are not detected in immune cells and the remaining immune-cell evidence is limited or gene-specific, although STX7 has broad blood-cell enrichment and could reflect a shared myeloid or immune-associated component. The shared signal may therefore reflect common stromal or connective-tissue cell content, tissue remodeling, or extracellular-matrix production rather than a stem-cell-specific or germ-cell-specific program.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG ECM-receptor interaction - Homo sapiens (human) | 0.0432 | COL1A2, COL6A1, LAMC1 |

### STRING and hu.MAP

STRING supports two high-confidence relationships within the module: COL1A2 with COL6A1 and COL1A2 with LAMC1. These connections are biologically coherent with the ECM interpretation and identify COL1A2 as the network anchor. The other co-abundance links, including those involving QKI, IDH2, and STX7, are not represented by reported high-confidence STRING partnerships in the fact sheet and should not be treated as established physical interactions. No hu.MAP complex contains multiple module members. Thus, the module resembles a coordinated ECM-associated expression program rather than a known stable multiprotein complex.

**STRING interactions (score >= 0.7)**: 2 of 15 gene pairs: COL1A2–COL6A1 (0.875); COL1A2–LAMC1 (0.701)
**STRING functional enrichment (supplementary, within-query FDR)**: WikiPathways miRNA targets in ECM and membrane receptors (FDR = 0.0032, 3 genes); KEGG ECM-receptor interaction (FDR = 0.0128, 3 genes); KEGG PI3K-Akt signaling pathway (FDR = 0.0167, 3 genes); KEGG Focal adhesion (FDR = 0.0211, 3 genes); KEGG Human papillomavirus infection (FDR = 0.0211, 3 genes); WikiPathways PI3K-Akt signaling pathway (FDR = 0.0285, 3 genes); Keyword Extracellular matrix (FDR = 0.046, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The biological theme is not new: collagen, laminin, ECM-receptor interaction, focal adhesion, and PI3K-Akt signaling are established areas of biology, and the COL1A2–COL6A1 and COL1A2–LAMC1 relationships are already represented in STRING. The potentially novel aspect is the observation that these genes co-abundance together across the stem-cell and testis tissue pair, particularly alongside QKI, IDH2, and STX7. However, the fact sheet does not provide an external catalogue of prior tissue-pair modules, so the exact shared module cannot be declared a new discovery. Absence from hu.MAP, or absence of additional STRING links, is not evidence of novelty; it mainly indicates that the observed co-abundance pattern is not a documented complex or densely connected physical interaction network.

**Hypothesis.** Hypothesis: the module reflects a shared stromal or mesenchymal extracellular-matrix state in stem-cell and testis samples. COL1A2, COL6A1, and LAMC1 may jointly mark production and organization of collagenous matrix and basement-membrane material, with matrix engagement potentially influencing focal-adhesion and PI3K-Akt signaling as suggested by (STRING KEGG PI3K-Akt signaling pathway; within-query FDR = 0.0167), (STRING KEGG Focal adhesion; within-query FDR = 0.0211), and (STRING WikiPathways PI3K-Akt signaling pathway; within-query FDR = 0.0285). QKI, IDH2, and STX7 may be correlated secondary signals associated with RNA regulation, cellular metabolism, and vesicle or lysosome trafficking, respectively, rather than core ECM constituents. This hypothesis should be tested using cell-composition estimates, spatial localization, protein-level measurements, and perturbation of matrix production or cell-matrix signaling.

### Important genes

#### COL1A2

- **Related proteins** (co-abundance neighbors): QKI (0.90), IDH2 (0.85), LAMC1 (0.85), STX7 (0.84), COL6A1 (0.81); STRING partners: COL6A1 (0.875), LAMC1 (0.701)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type I alpha 2 chain. This gene encodes the pro-alpha2 chain of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIB, recessive Ehlers-Danlos syndrome Classi…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 2 (0.845); osteogenesis imperfecta type 3 (0.830); osteogenesis imperfecta type 4 (0.820); Ehlers-Danlos syndrome, cardiac valvular type (0.777); osteogenesis imperfecta type 1 (0.770)
- **Europe PMC papers**: 67901
- **Why important**: COL1A2 is the module hub, connecting every other module member in the co-abundance graph. It is part of the globally corrected ECM-receptor interaction signal (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0432) and all reported supplementary STRING enrichments (7 supplementary STRING terms; within-query FDR 0.0032–0.046). Its protein forms type I collagen, a major fibrillar component of connective tissues, and HPA places it in extracellular matrix with fibroblast, stromal, and fibro-adipogenic progenitor associations. Its extensive disease and literature evidence, including osteogenesis imperfecta and several connective-tissue disorders, makes it the strongest biological anchor for the module.
- **Conclusion**: Established evidence supports COL1A2 as the central structural ECM gene and the principal marker of the module's stromal interpretation. A role as the driver of the observed cross-tissue co-abundance is a hypothesis, not demonstrated causation.

#### COL6A1

- **Related proteins** (co-abundance neighbors): COL1A2 (0.81); STRING partners: COL1A2 (0.875)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is one of the three genes in (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0432) and is a known STRING partner of COL1A2. It encodes a collagen VI chain, and HPA associates it with fibroblasts, fibro-adipogenic progenitors, and stromal cells while classifying it as secreted to extracellular matrix. Its established links to Bethlem myopathy, Ullrich congenital muscular dystrophy, and other collagen-six disorders provide strong functional and disease relevance.
- **Conclusion**: Established evidence supports COL6A1 as a core extracellular-matrix component that strengthens the interpretation of a connective-tissue or stromal program. Its contribution to the shared stem-cell–testis signal may reflect matrix-producing cell content or remodeling, but the fact sheet does not establish which mechanism applies.

#### LAMC1

- **Related proteins** (co-abundance neighbors): COL1A2 (0.85); STRING partners: COL1A2 (0.701)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Plasma membrane; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit gamma 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: Fuchs' endothelial dystrophy (0.487); prostate carcinoma (0.467); colorectal cancer (0.447); eye disorder (0.434); benign colon neoplasm (0.427)
- **Europe PMC papers**: 4227
- **Why important**: LAMC1 is the laminin gamma one subunit and is one of the three genes in (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0432) and (7 supplementary STRING terms; within-query FDR 0.0032–0.046). It is a known STRING partner of COL1A2. Laminins are basement-membrane glycoproteins involved in adhesion, migration, differentiation, and signaling, while HPA places LAMC1 in the extracellular matrix and plasma-membrane-associated compartments and associates it with fibroblasts and fibro-adipogenic progenitors. This gives LAMC1 a complementary basement-membrane role beside the collagen genes.
- **Conclusion**: Established evidence supports LAMC1 as a core basement-membrane and cell-adhesion component of the module. Its possible role in coupling the matrix to PI3K-Akt or focal-adhesion signaling is biologically plausible and supported only as pathway-level supplementary evidence, not as a demonstrated mechanism in this module.

#### QKI

- **Related proteins** (co-abundance neighbors): COL1A2 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: QKI, KH domain containing RNA binding. The protein encoded by this gene is an RNA-binding protein that regulates pre-mRNA splicing, export of mRNAs from the nucleus, protein translation, and mRNA stability. The encoded protein is involved in myelinization and oligodendrocyte differentiation and may play a role in schizophrenia. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, …
- **Diseases (Open Targets)**: cancer (0.564); neurodegenerative disease (0.499); cataract (0.488); sensorineural hearing loss disorder (0.438); type 2 diabetes mellitus (0.413)
- **Europe PMC papers**: 3460
- **Why important**: QKI is the only module member directly connected to the ECM hub COL1A2 while lacking a reported STRING partner or enriched GO/KEGG term. It encodes an RNA-binding protein involved in pre-mRNA processing, mRNA localization, translation, and stability, and HPA associates it with several neural and muscle-related cell types. Its position suggests that it may capture a regulatory or cell-state component accompanying the ECM signal rather than being a structural matrix protein. Its established associations with myelinization, oligodendrocyte differentiation, schizophrenia-related biology, cancer, and neurodegenerative disease add functional importance despite its peripheral network position.
- **Conclusion**: Established evidence supports QKI as an RNA-regulatory gene correlated with the COL1A2-centered module, but not as an established ECM component. Its connection may indicate coordinated cell-state regulation or shared cellular composition; any direct regulatory role in the ECM program remains a hypothesis.

## Module 5

**Tissue pair**: stem_cells and testis  
**Genes (19)**: CYP51A1, COPS7B, CACYBP, DHCR24, FDFT1, HACD3, IDI1, MGST2, MVD, PPP1R12A, PRAF2, PSIP1, RAB23, SNRPA1, SLC25A24, SEPTIN8, TAMM41, TECR, THY1

### Function

The primary evidence supports a sterol and cholesterol biosynthetic module. Multiple globally corrected GO terms identify cholesterol biosynthesis, sterol biosynthesis, cholesterol and sterol metabolism, lipid biosynthesis, and related small-molecule and alcohol biosynthetic processes (10 globally significant GO/KEGG terms, q_global 0.00905–0.0497; see the table). The recurring core of CYP51A1, DHCR24, FDFT1, IDI1, and MVD maps coherently onto successive steps of the mevalonate-to-cholesterol pathway. HACD3 and TECR extend the module toward fatty-acid elongation and broader membrane-lipid synthesis, while TAMM41 is consistent with mitochondrial phospholipid biosynthesis. The topology contains a connected sterol-enzyme neighborhood and a separate HACD3–TECR relationship, with additional links to trafficking, cytoskeletal, RNA-processing, and regulatory genes. Thus, the strongest interpretation is coordinated lipid and sterol supply rather than a single specialized signaling pathway. The globally corrected GO evidence is sufficient for this functional assignment; the STRING pathway results provide convergent supplementary support (15 supplementary STRING terms; within-query FDR 3.02e-06–0.0223).

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It is also not strongly blood-cell enriched, because most genes have low immune-cell specificity or are not detected in immune cells, with only MGST2 showing immune-cell enhancement. Most genes have low tissue specificity, although several are enhanced in liver, brain, adrenal gland, epididymis, or smooth muscle. Many genes are cell-type enhanced, including genes associated with late spermatids, primary spermatocytes, epididymal cells, oocytes, and esophageal epithelial cells. Protein detection in testis is widespread among the module genes, whereas matching HPA protein evidence is unavailable for stem cells. Therefore, the shared module is compatible with a broadly deployed lipid-metabolic program that is particularly visible in testicular germ-cell or supporting-cell contexts; it should not be interpreted as a blood-contamination signature. Shared cell types or common metabolic demands could nevertheless contribute to its conservation between the tissue groups.

**GO/KEGG enrichment**: 10 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP cholesterol biosynthetic process | 0.00905 | CYP51A1, DHCR24, FDFT1, IDI1, MVD |
| GO:BP secondary alcohol biosynthetic process | 0.00905 | CYP51A1, DHCR24, FDFT1, IDI1, MVD |
| GO:BP sterol biosynthetic process | 0.015 | CYP51A1, DHCR24, FDFT1, IDI1, MVD |
| GO:BP lipid biosynthetic process | 0.0162 | CYP51A1, DHCR24, FDFT1, HACD3, IDI1, MVD, TAMM41, TECR |
| GO:BP cholesterol metabolic process | 0.0271 | CYP51A1, DHCR24, FDFT1, IDI1, MVD |
| GO:BP sterol metabolic process | 0.0351 | CYP51A1, DHCR24, FDFT1, IDI1, MVD |
| GO:BP secondary alcohol metabolic process | 0.0395 | CYP51A1, DHCR24, FDFT1, IDI1, MVD |
| GO:BP small molecule biosynthetic process | 0.0445 | CYP51A1, DHCR24, FDFT1, HACD3, IDI1, MGST2, MVD, TECR |
| GO:BP alcohol biosynthetic process | 0.0445 | CYP51A1, DHCR24, FDFT1, IDI1, MVD |
| GO:BP steroid biosynthetic process | 0.0497 | CYP51A1, DHCR24, FDFT1, IDI1, MVD |

### STRING and hu.MAP

STRING provides strong prior support for the central sterol pathway: CYP51A1, DHCR24, FDFT1, IDI1, and MVD are mutually connected through several high-confidence relationships, while HACD3 and TECR form a separate high-confidence pair. These known relationships indicate that a substantial part of the module recapitulates an established biochemical pathway rather than an unexplained interaction system. The module contains no listed STRING partners for several peripheral genes, so their co-abundance links should not be treated as established physical interactions. hu.MAP places DHCR24 and HACD3 together in several lipid- and membrane-associated complexes (hu.MAP huMAP3_07410.1) (hu.MAP huMAP3_06247.1) (hu.MAP huMAP3_09592.1), but they represent only a small fraction of the members of those complexes and the confidence is not uniformly high. This supports shared cellular machinery or membrane-lipid context, but does not establish that the entire co-abundance module is one physical complex.

**STRING interactions (score >= 0.7)**: 10 of 171 gene pairs: CYP51A1–DHCR24 (0.992); CYP51A1–FDFT1 (0.997); CYP51A1–IDI1 (0.942); CYP51A1–MVD (0.869); DHCR24–FDFT1 (0.831); DHCR24–IDI1 (0.765); FDFT1–IDI1 (0.94); FDFT1–MVD (0.873); HACD3–TECR (0.984); IDI1–MVD (0.998)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Lipid biosynthesis (FDR = 3.02e-06, 8 genes); Keyword Cholesterol biosynthesis (FDR = 0.0001, 5 genes); WikiPathways Cholesterol synthesis disorders (FDR = 0.00049, 5 genes); WikiPathways Cholesterol metabolism (FDR = 0.00092, 5 genes); WikiPathways Cholesterol metabolism with Bloch and Kandutsch-Russell pathways (FDR = 0.0012, 5 genes); WikiPathways Cholesterol metabolism (FDR = 0.0016, 5 genes); WikiPathways Cholesterol biosynthesis pathway (FDR = 0.0021, 4 genes); WikiPathways Cholesterol biosynthesis pathway in hepatocytes (FDR = 0.0021, 5 genes); RCTM Cholesterol biosynthesis (FDR = 0.0035, 5 genes); NetworkNeighborAL Cholesterol biosynthesis (FDR = 0.0039, 5 genes); WikiPathways Sterol regulatory element-binding proteins (SREBP) signaling (FDR = 0.0062, 4 genes); Process Cholesterol biosynthetic process (FDR = 0.0156, 5 genes); Process Lipid biosynthetic process (FDR = 0.0156, 8 genes); Process Small molecule biosynthetic process (FDR = 0.0189, 8 genes); RCTM Activation of gene expression by SREBF (SREBP) (FDR = 0.0223, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07410.1 (DHCR24, HACD3; 2/35); huMAP3_06247.1 (DHCR24, HACD3; 2/65); huMAP3_09592.1 (DHCR24, HACD3; 2/95)

### Novelty

The cholesterol-biosynthesis core is not a new biological pathway: its enzymes, disease links, and STRING pathway associations are already well established. The conserved co-abundance pattern between stem cells and testis may still be a useful module-level observation, especially because it combines sterol enzymes with membrane, mitochondrial, trafficking, cytoskeletal, and germ-cell-associated genes. However, the fact sheet does not provide an external comparison with previously published co-abundance modules, and absence of some genes or edges from STRING and hu.MAP cannot prove novelty. The defensible conclusion is that the biochemical function is established, while the particular tissue-pair module organization is potentially interesting but not demonstrated here to be a new finding.

**Hypothesis.** Hypothesis: the module coordinates membrane-sterol and related lipid production with the membrane remodeling, organelle maintenance, and cellular differentiation demands shared by stem-cell populations and testicular germ-cell environments. The sterol core may provide cholesterol and isoprenoid intermediates, HACD3 and TECR may support fatty-acid chain processing, and TAMM41 may connect lipid production to mitochondrial membrane maintenance. The peripheral genes could reflect coupling to intracellular trafficking, cytoskeletal organization, RNA processing, proteostasis, and cell-state regulation. This model predicts that module activity will track sterol and membrane-lipid flux and may vary with germ-cell differentiation or stem-cell state, but the co-abundance data alone do not establish directionality, enzymatic flux, or physical binding.

### Important genes

#### CYP51A1

- **Related proteins** (co-abundance neighbors): DHCR24 (0.85), FDFT1 (0.82); STRING partners: DHCR24 (0.992), FDFT1 (0.997), IDI1 (0.942), MVD (0.869)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome P450 family 51 subfamily A member 1. This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This endoplasmic reticulum protein participates in the synthesis of cholesterol by catalyzing the removal of the 14alpha-methyl group from lanosterol. Homologous g…
- **Diseases (Open Targets)**: Developmental cataract (0.398); early-onset non-syndromic cataract (0.371); cataract (0.371); Prolonged QT interval (0.346); neurodegenerative disease (0.280)
- **Europe PMC papers**: 1488
- **Why important**: CYP51A1 is a central endoplasmic-reticulum enzyme in cholesterol and steroid biosynthesis. It lies in the sterol-enzyme portion of the network and has established STRING links to DHCR24, FDFT1, IDI1, and MVD. It appears in every globally corrected GO term and every listed STRING enrichment category (10 globally significant GO/KEGG terms, q_global 0.00905–0.0497; see the table), (15 supplementary STRING terms; within-query FDR 3.02e-06–0.0223). HPA reports liver enhancement, testis protein detection, and enhancement in several spermatid and muscle-associated cell types. Its literature base is substantial, and its known role makes it a strong biochemical anchor rather than merely a topological hub.
- **Conclusion**: Established evidence identifies CYP51A1 as a core cholesterol-pathway component that helps explain the module's function and its presence in testis. The hypothesis that its coordinated abundance marks increased sterol demand in shared stem-cell and testicular states is plausible but not proven by this module.

#### IDI1

- **Related proteins** (co-abundance neighbors): PRAF2 (0.84), THY1 (0.82); STRING partners: CYP51A1 (0.942), DHCR24 (0.765), FDFT1 (0.94), MVD (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: isopentenyl-diphosphate delta isomerase 1. IDI1 encodes a peroxisomally-localized enzyme that catalyzes the interconversion of isopentenyl diphosphate (IPP) to its highly electrophilic isomer, dimethylallyl diphosphate (DMAPP), which are the substrates for the successive reaction that results in the synthesis of farnesyl diphosphate and, ultimately, cholesterol.  It has been shown in peroxisomal deficiency diseases such as Zellweger syndro…
- **Diseases (Open Targets)**: neurodegenerative disease (0.539); hypotensive disorder (0.215); placental retention (0.191); liver disorder (0.147); esophageal cancer (0.138)
- **Europe PMC papers**: 1844
- **Why important**: IDI1 connects the upstream isoprenoid branch to downstream sterol production by interconverting isopentenyl and dimethylallyl diphosphates. It is part of every globally corrected GO term and every listed STRING enrichment category (10 globally significant GO/KEGG terms, q_global 0.00905–0.0497; see the table), (15 supplementary STRING terms; within-query FDR 3.02e-06–0.0223), and it has strong STRING relationships with CYP51A1, FDFT1, MVD, and DHCR24. It is cell-type enhanced in several epithelial, epididymal, and lactating-cell contexts and is detected in testis. Its established biochemical position and broad literature support make it an informative indicator of pathway-level coordination.
- **Conclusion**: Established evidence supports IDI1 as an upstream control point within the module's isoprenoid and cholesterol program. A possible interpretation is that the module coordinates precursor supply with sterol synthesis, but flux through this step cannot be inferred from co-abundance.

#### FDFT1

- **Related proteins** (co-abundance neighbors): CYP51A1 (0.82), THY1 (0.81); STRING partners: CYP51A1 (0.997), DHCR24 (0.831), IDI1 (0.94), MVD (0.873)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: farnesyl-diphosphate farnesyltransferase 1. This gene encodes a membrane-associated enzyme located at a branch point in the mevalonate pathway. The encoded protein is the first specific enzyme in cholesterol biosynthesis, catalyzing the dimerization of two molecules of farnesyl diphosphate in a two-step reaction to form squalene. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: squalene synthase deficiency (0.519); Hypercholesterolemia (0.398); Abnormality of the skeletal system (0.353); inherited lipid metabolism disorder (0.324); myopathy (0.281)
- **Europe PMC papers**: 2443
- **Why important**: FDFT1 catalyzes the committed squalene-forming step of cholesterol biosynthesis and therefore links farnesyl-diphosphate production to sterol synthesis. It is in every globally corrected GO term and every listed STRING enrichment category (10 globally significant GO/KEGG terms, q_global 0.00905–0.0497; see the table), (15 supplementary STRING terms; within-query FDR 3.02e-06–0.0223). Its STRING connections to CYP51A1, DHCR24, IDI1, and MVD form a coherent biochemical neighborhood. HPA shows testis detection and enhancement in early and late spermatid-related cell types, while disease associations include squalene synthase deficiency and inherited lipid disorders. Its large literature base further supports its importance.
- **Conclusion**: Established evidence makes FDFT1 a central pathway bottleneck and a strong marker of the module's sterol-biosynthetic identity. The hypothesis that its coordinated regulation helps meet membrane or differentiation-associated lipid demand in testis and stem cells remains to be tested.

#### DHCR24

- **Related proteins** (co-abundance neighbors): CYP51A1 (0.85), MVD (0.80); STRING partners: CYP51A1 (0.992), FDFT1 (0.831), IDI1 (0.765)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07410.1, huMAP3_06247.1, huMAP3_09592.1
- **Function (MyGene.info)**: 24-dehydrocholesterol reductase. This gene encodes a flavin adenine dinucleotide (FAD)-dependent oxidoreductase which catalyzes the reduction of the delta-24 double bond of sterol intermediates during cholesterol biosynthesis. The protein contains a leader sequence that directs it to the endoplasmic reticulum membrane. Missense mutations in this gene have been associated with desmosterolosis. Also, reduced expression of the gene …
- **Diseases (Open Targets)**: desmosterolosis (0.821); Non-immune hydrops fetalis (0.425); hereditary disease (0.193); digestive system disorder (0.159); schizophrenia (0.112)
- **Europe PMC papers**: 2845
- **Why important**: DHCR24 catalyzes reduction of a sterol intermediate during cholesterol biosynthesis and is present in every globally corrected GO term (10 globally significant GO/KEGG terms, q_global 0.00905–0.0497; see the table). It has strong STRING links to the sterol core and is the only selected gene with membership in all listed hu.MAP complexes (hu.MAP huMAP3_07410.1) (hu.MAP huMAP3_06247.1) (hu.MAP huMAP3_09592.1), where it occurs with HACD3 in lipid- and membrane-associated contexts. HPA shows enhancement in liver and adrenal gland, testis protein detection, and broad enhancement across several epithelial and adrenal cell types. Its association with desmosterolosis provides a direct disease connection, and its literature volume is substantial.
- **Conclusion**: Established evidence supports DHCR24 as both a core sterol enzyme and a bridge to broader membrane-lipid machinery. Its hu.MAP context suggests possible coupling of sterol handling to membrane systems, but the complex data do not demonstrate that this module is a single physical complex.

#### MVD

- **Related proteins** (co-abundance neighbors): DHCR24 (0.80); STRING partners: CYP51A1 (0.869), FDFT1 (0.873), IDI1 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mevalonate diphosphate decarboxylase. The enzyme mevalonate pyrophosphate decarboxylase catalyzes the conversion of mevalonate pyrophosphate into isopentenyl pyrophosphate in one of the early steps in cholesterol biosynthesis. It decarboxylates and dehydrates its substrate while hydrolyzing ATP. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: disseminated superficial actinic porokeratosis (0.767); porokeratosis 7, multiple types (0.684); neurodegenerative disease (0.547); skin disorder (0.328); linear porokeratosis (0.323)
- **Europe PMC papers**: 9949
- **Why important**: MVD performs an early mevalonate-pathway reaction that supplies isoprenoid precursors for downstream sterol production. It appears in every globally corrected GO term and every listed STRING enrichment category (10 globally significant GO/KEGG terms, q_global 0.00905–0.0497; see the table), (15 supplementary STRING terms; within-query FDR 3.02e-06–0.0223), and has strong STRING relationships with IDI1, CYP51A1, and FDFT1. HPA reports testis detection and enhancement in epididymal, epithelial, and lactating-cell contexts. Its disease associations include porokeratosis and broader neurodegenerative and skin-disorder links, and it has a large literature base. Its position connects upstream precursor generation to the rest of the sterol core.
- **Conclusion**: Established evidence identifies MVD as an upstream contributor to the coordinated mevalonate and cholesterol program. The hypothesis that MVD abundance couples precursor availability to cell-state-specific membrane production is mechanistically reasonable, but it requires metabolic or perturbation experiments.

## Module 6

**Tissue pair**: stem_cells and testis  
**Genes (6)**: CIAPIN1, DNPEP, ERLIN1, NDC1, SMPD4, PPIL1

### Function

This is a sparse, connected co-abundance module organized around SMPD4, with links to ERLIN1, NDC1, DNPEP, and a PPIL1-DNPEP-CIAPIN1 branch. No GO or KEGG term passed global correction, so there is no statistically established pathway enrichment for this module. The gene annotations nevertheless point to a possible intersection of nuclear-envelope and nuclear-pore biology, ER membrane lipid regulation, intracellular protein processing, mitochondrial stress protection, and cell-state maintenance. The strongest functional anchor is SMPD4: it is an ER and outer nuclear-envelope sphingomyelinase implicated in ceramide production, ER organization, cellular stress responses, and cell-cycle or differentiation phenotypes. NDC1 provides a nuclear-pore assembly connection, while ERLIN1 provides an ER lipid-homeostasis connection. These annotations support a focused cellular-process interpretation, but not a claim of a single established pathway.

**Cell composition.** The module does not resemble a plasma-protein, secreted-protein, or blood-cell contamination module. All members are non-secreted intracellular proteins, and the HPA summary reports low immune-cell specificity throughout. Most genes have low tissue specificity, although ERLIN1 is tissue enhanced in liver. Cell-type-enhanced signals are diverse and include germ-cell, spermatogenic, oocyte, trophoblast, erythrocyte-progenitor, and myeloid-progenitor populations. Thus, the shared stem-cell and testis signal may reflect a broadly reusable intracellular state or shared progenitor biology rather than a testis-specific secreted program. Protein detection is reported for most assessed genes in testis, whereas matching HPA tissue data are unavailable for stem cells; this limits direct protein-level comparison.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no high-confidence interaction for any module pair and no supplementary STRING functional enrichment. Therefore, the co-abundance edges should not be interpreted as established physical interactions. hu.MAP provides the main external structural support: NDC1 and SMPD4 co-occur as module members in complex C1 and complex C2, alongside nucleoporins and SENP proteins. This supports a possible relationship between SMPD4-associated membrane biology and nuclear-pore or nuclear-envelope machinery, but the complexes contain additional proteins and do not establish a direct NDC1-SMPD4 interaction. The absence of STRING links, together with the partial hu.MAP overlap, suggests that the module captures coordinated abundance across related cellular processes rather than a fully known canonical complex.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09497.1 (NDC1, SMPD4; 2/6); huMAP3_07645.1 (NDC1, SMPD4; 2/7)

### Novelty

The module may represent a potentially under-characterized co-abundance pattern, but it cannot be called a definitively new biological finding. Its novelty is supported by the absence of high-confidence STRING relationships among the module genes, the lack of STRING enrichment, and the fact that only NDC1 and SMPD4 are jointly represented in the hu.MAP complexes. However, absence from interaction resources is not evidence of novelty by itself. Existing literature already connects SMPD4 to ER and nuclear-envelope biology, cell division, stem-cell proliferation, and developmental disease, while the hu.MAP results provide prior support for related protein-complex context. A new finding would require independent replication, comparison with other tissue pairs, and experimental testing of the proposed relationships.

**Hypothesis.** Hypothesis: this module reflects a conserved intracellular adaptation of stem or germ-cell states that coordinates nuclear-envelope and pore assembly with ER membrane-lipid homeostasis, protein quality control, and stress tolerance. In this model, SMPD4 and ERLIN1 organize an ER and nuclear-envelope lipid environment, NDC1 supports nuclear-pore assembly, and the PPIL1-DNPEP-CIAPIN1 branch reflects protein folding or turnover together with mitochondrial and anti-apoptotic stress protection. Such coordination could be useful during proliferation, differentiation, or germ-cell maturation. This is a mechanistic hypothesis based on annotations, network topology, and partial hu.MAP support; the co-abundance data do not establish causality, direct binding, or the direction of regulation.

Web sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC10393401/

### Important genes

#### SMPD4

- **Related proteins** (co-abundance neighbors): ERLIN1 (0.81), NDC1 (0.80), DNPEP (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear membrane; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_09497.1, huMAP3_07645.1
- **Function (MyGene.info)**: sphingomyelin phosphodiesterase 4. The protein encoded by this gene is a sphingomyelinase that catalyzes the hydrolysis of membrane sphingomyelin to form phosphorylcholine and ceramide. This gene is activated by DNA damage, cellular stress, and tumor necrosis factor, but it is downregulated by wild-type p53. The encoded protein localizes to the endoplasmic reticulum and Golgi network. [provided by RefSeq, Mar 2017].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, arthrogryposis, and structural brain anomalies (0.762); neurodegenerative disease (0.444); hereditary disease (0.415); diabetes mellitus (0.373); type 1 diabetes mellitus (0.372)
- **Europe PMC papers**: 426
- **Why important**: SMPD4 is the central network connector, linking ERLIN1, NDC1, and DNPEP. It is an ER and nuclear-envelope sphingomyelinase that produces ceramide and is annotated for ER organization, lipid catabolism, stress response, and ceramide biosynthesis. It is also present with NDC1 in both hu.MAP complexes C1 and C2. Its disease associations include a severe neurodevelopmental disorder with microcephaly and structural brain abnormalities, and the literature specifically reports effects of SMPD4 loss on neural-stem-cell proliferation, mitosis, nuclear-envelope dynamics, and post-mitotic nuclear-pore insertion.
- **Conclusion**: Established evidence supports SMPD4 as the leading functional anchor and a biologically plausible link between membrane lipid metabolism, nuclear-envelope dynamics, and cell-state control. The module does not establish that SMPD4 drives the shared stem-cell and testis pattern, so any causal role in this module remains a hypothesis.

#### NDC1

- **Related proteins** (co-abundance neighbors): SMPD4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_09497.1, huMAP3_07645.1
- **Function (MyGene.info)**: NDC1 transmembrane nucleoporin. A structural constituent of nuclear pore. Involved in nuclear pore complex assembly and nuclear pore localization. Located in actin cytoskeleton; nuclear membrane; and plasma membrane. Part of nuclear pore. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder with achalasia, polyneuropathy, and alacrima (0.658); Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.526); Histiocytosis (0.370)
- **Europe PMC papers**: 778
- **Why important**: NDC1 is a nuclear-membrane transmembrane nucleoporin involved in nuclear-pore organization, assembly, localization, and nucleocytoplasmic transport. It is linked to SMPD4 in hu.MAP complexes C1 and C2, giving it the clearest external complex-level connection to the module's central gene. Its HPA cell-type signals include erythrocyte and monocyte progenitors, and it is detected in testis.
- **Conclusion**: Established evidence supports NDC1 as a nuclear-pore and nuclear-envelope component that gives the module a coherent structural interpretation. The co-abundance relationship with SMPD4 may indicate coordinated nuclear-envelope demand, but it is not evidence of direct binding or a specific testis mechanism.

#### ERLIN1

- **Related proteins** (co-abundance neighbors): SMPD4 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ER lipid raft associated 1. The protein encoded by this gene is part of a protein complex that mediates degradation of inositol 1,4,5-trisphosphate receptors in the endoplasmic reticulum. The encoded protein also binds cholesterol and regulates the SREBP signaling pathway, which promotes cellular cholesterol homeostasis. Defects in this gene have been associated with spastic paraplegia 62. [provided by RefSeq, Dec 2016].
- **Diseases (Open Targets)**: hereditary spastic paraplegia 62 (0.694); hereditary spastic paraplegia (0.594); cystic fibrosis (0.462); juvenile amyotrophic lateral sclerosis (0.455); Abnormality of the liver (0.406)
- **Europe PMC papers**: 478
- **Why important**: ERLIN1 is directly connected to the central SMPD4 node and is located in the ER. It participates in degradation of inositol-trisphosphate receptors, binds cholesterol, and regulates SREBP-linked cholesterol and fatty-acid homeostasis. It is associated with hereditary spastic paraplegia and related neurological phenotypes. Its tissue-enhanced liver signal and progenitor or neutrophil cell-type signals indicate that it is not restricted to testis.
- **Conclusion**: Established evidence supports ERLIN1 as the module's strongest ER lipid-homeostasis partner and as a plausible complement to SMPD4. Its inclusion supports coordinated ER membrane regulation, but the module alone cannot distinguish lipid-homeostasis biology from a broader shared cellular-state effect.

#### CIAPIN1

- **Related proteins** (co-abundance neighbors): PPIL1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytokine induced apoptosis inhibitor 1. CIAPIN1 is a cytokine-induced inhibitor of apoptosis with no relation to apoptosis regulatory molecules of the BCL2 (MIM 151430) or CASP (see MIM 147678) families. Expression of CIAPIN1 is dependent on growth factor stimulation (Shibayama et al., 2004 [PubMed 14970183]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.513); coronary atherosclerosis (0.247); neoplasm (0.098); breast cancer (0.096); breast carcinoma (0.096)
- **Europe PMC papers**: 992
- **Why important**: CIAPIN1 is the terminal member of the PPIL1-DNPEP-CIAPIN1 branch and is annotated for iron-sulfur cluster assembly, hemopoiesis, oxidative-stress response, and negative regulation of apoptosis. It is localized to mitochondria, has cell-type-enhanced signals in trophoblasts, spermatocytes, and oocytes, and has substantial disease and cancer literature.
- **Conclusion**: Established evidence supports CIAPIN1 as a mitochondrial and stress-survival component that could complement the membrane and nuclear-envelope processes in the module. Its position at the branch end makes it a plausible marker of a coordinated cellular state, but a direct mechanistic connection to SMPD4 or NDC1 is not established.

#### PPIL1

- **Related proteins** (co-abundance neighbors): DNPEP (0.83), CIAPIN1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peptidylprolyl isomerase like 1. This gene is a member of the cyclophilin family of peptidylprolyl isomerases (PPIases). The cyclophilins are a highly conserved, ubiquitous family, members of which play an important role in protein folding, immunosuppression by cyclosporin A, and infection of HIV-1 virions. Based on similarity to other PPIases, this protein could accelerate the folding of proteins and might catalyze the cis-trans…
- **Diseases (Open Targets)**: pontocerebellar hypoplasia, type 14 (0.770); neurodegenerative disease (0.527); pontocerebellar hypoplasia (0.402); dengue disease (0.370); hypothyroidism (0.349)
- **Europe PMC papers**: 348
- **Why important**: PPIL1 links DNPEP with CIAPIN1 and is a cyclophilin-family peptidyl-prolyl isomerase-like protein. Its annotations include protein folding, peptidyl-prolyl isomerization, and spliceosome-related mRNA processing. HPA identifies enhanced signals across differentiating spermatogonia, oocytes, and trophoblast populations, which is relevant to a module shared across developmental and germ-cell contexts.
- **Conclusion**: Established evidence supports PPIL1 as a candidate protein-folding or RNA-processing component of the shared state. The network and cell-type evidence make it biologically relevant, but its precise enzymatic contribution and any functional coupling to the SMPD4-NDC1 arm remain hypothetical.

## Module 7

**Tissue pair**: stem_cells and testis  
**Genes (5)**: EIF3C, MCM2, MMUT, SF3B3, ALDH5A1

### Function

This is a small, weakly connected co-abundance module with no globally significant GO or KEGG enrichment. Its genes nevertheless suggest several established biological themes: pre-mRNA splicing through SF3B3, translation initiation through EIF3C, genome-replication initiation through MCM2, and mitochondrial or intermediary metabolism through ALDH5A1 and MMUT. These annotations do not establish one unified pathway. The network is therefore best interpreted as a coordinated expression signal spanning RNA processing, proliferation-associated nuclear functions, translation, and metabolism rather than as a demonstrated molecular complex or pathway. The lack of globally significant GO or KEGG terms does not invalidate the module.

**Cell composition.** The module is not dominated by secreted or plasma proteins, and all members have low immune-cell specificity. It therefore does not resemble a blood-cell or circulating-protein module. The HPA profile is heterogeneous: ALDH5A1 and MMUT are liver-enhanced and hepatocyte-enhanced, MCM2 is enhanced in bone marrow and lymphoid tissue and in progenitor populations including differentiating spermatogonia, while SF3B3 and EIF3C have low tissue specificity. Four genes are cell-type enhanced and one is cell-type enriched, with signals spanning hepatocytes, neural cell types, reproductive or progenitor populations, and esophageal apical cells. All members are detected by immunohistochemistry in testis. The shared stem-cell and testis signal may therefore reflect common proliferative, germline-supporting, or metabolically active cell states, but the HPA pattern also raises the possibility that the module captures broadly deployed cellular programs rather than a testis-specific mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is present among the module genes, and no STRING functional-enrichment result is available. No hu.MAP complex contains multiple module members. The observed co-abundance edges are therefore not supported by the supplied protein-interaction or complex resources. SF3B3 is independently annotated as a spliceosomal component, EIF3C as a component of the translation-initiation complex, and MCM2 as part of the replication machinery, but these established complexes do not connect the full module in the available evidence. The co-abundance relationships may consequently reflect shared regulation, cell-state composition, or indirect functional coupling rather than direct physical interaction.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is a new co-abundance observation in this analysis, but it should not be called a newly discovered biological pathway. Its genes have extensive prior functional and disease literature, and the absence of STRING or hu.MAP support does not prove novelty. What is potentially novel is the cross-tissue co-abundance pattern linking these particular genes in stem cells and testis. Because there is no globally significant GO or KEGG term and no supporting known interaction complex, the biological interpretation remains provisional and requires independent replication and experimental testing.

**Hypothesis.** Hypothesis: the module may represent a shared cellular-state program in stem cells and testis that coordinates proliferation or germ-cell development with the biosynthetic demands of active cells. MCM2 could mark replication competence, SF3B3 could support regulated pre-mRNA processing, EIF3C could support increased translation, and ALDH5A1 together with MMUT could reflect metabolic adaptation. The liver and hepatocyte signals indicate that the metabolic component is not specific to stem cells or testis, so this hypothesis should be tested against cell composition, proliferation markers, germ-cell stage, and metabolic state rather than assumed to describe a single physical pathway.

### Important genes

#### MCM2

- **Related proteins** (co-abundance neighbors): SF3B3 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is the strongest hub-like nuclear gene in the module's replication-related branch and is a highly conserved component of the pre-replication machinery. Its annotations include DNA replication initiation and replication-fork functions. The HPA signal in bone marrow, lymphoid tissue, progenitor populations, and differentiating spermatogonia makes it especially relevant to a stem-cell and testis comparison. It also has the largest literature volume among the module genes and established disease associations involving inherited hearing loss and other abnormalities.
- **Conclusion**: Established evidence supports MCM2 as a marker and mediator of replication competence. In this module, it may indicate a proliferative or progenitor-cell state. It is not established that MCM2 directly drives the co-abundance relationship with the other genes.

#### SF3B3

- **Related proteins** (co-abundance neighbors): EIF3C (0.85), MCM2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Nucleoli rim; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: splicing factor 3b subunit 3. This gene encodes subunit 3 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); dengue disease (0.370); cervical cancer (0.189); cervical carcinoma (0.189); prostate cancer (0.111)
- **Europe PMC papers**: 965
- **Why important**: SF3B3 occupies a central position in the small network and connects the replication-associated MCM2 branch with the translation-associated EIF3C branch. It is an annotated subunit of the SF3B spliceosomal complex and participates in U2 and minor U twelve-type spliceosome functions, pre-mRNA splicing, and spliceosome remodeling. Its broad tissue profile and testis detection are compatible with a general RNA-processing requirement in active cells. It has substantial literature and disease links including neurodegenerative disease, dengue disease, and cancer contexts.
- **Conclusion**: Established evidence supports SF3B3 as a core RNA-splicing factor. Its position makes it a plausible integrator of nuclear and translational cell-state signals, but the module does not demonstrate a direct SF3B3 interaction with MCM2 or EIF3C.

#### EIF3C

- **Related proteins** (co-abundance neighbors): SF3B3 (0.85), ALDH5A1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C connects SF3B3 with ALDH5A1 and is an annotated subunit of the eukaryotic translation-initiation complex. Its established functions include ribosome binding, cytoplasmic translation initiation, and positive regulation of translation. Its low tissue specificity but broad neural cell-type enhancement suggests a widely used cellular function rather than a tissue-restricted role. It has substantial literature and reported associations with neoplasm, hepatocellular carcinoma, ovarian cancer, and a developmental syndrome.
- **Conclusion**: Established evidence supports EIF3C as a translation-initiation factor. Within this module it may reflect increased protein-production capacity accompanying active or proliferative cells, but a specific translational program in stem cells and testis is not established.

#### ALDH5A1

- **Related proteins** (co-abundance neighbors): EIF3C (0.81), MMUT (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 5 family member A1. This protein belongs to the aldehyde dehydrogenase family of proteins. This gene encodes a mitochondrial NAD(+)-dependent succinic semialdehyde dehydrogenase. A deficiency of this enzyme, known as 4-hydroxybutyricaciduria, is a rare inborn error in the metabolism of the neurotransmitter 4-aminobutyric acid (GABA). In response to the defect, physiologic fluids from patients accumulate GHB, a compou…
- **Diseases (Open Targets)**: succinic semialdehyde dehydrogenase deficiency (0.843); epilepsy (0.608); bipolar disorder (0.607); Seizure (0.595); major depressive disorder (0.576)
- **Europe PMC papers**: 1100
- **Why important**: ALDH5A1 is positioned between the translation-associated EIF3C branch and the metabolic MMUT branch. It encodes a mitochondrial succinic semialdehyde dehydrogenase involved in GABA-shunt, succinate, glutamate, and GABA catabolism. Its liver and hepatocyte enhancement, mitochondrial localization, testis detection, and strong disease association with succinic semialdehyde dehydrogenase deficiency make it an important metabolic anchor. Its literature volume is substantial.
- **Conclusion**: Established evidence supports ALDH5A1 as a mitochondrial metabolic enzyme with major neurological disease relevance. In this module it may represent metabolic support for active cells, but the co-abundance data do not establish that its metabolic pathway is mechanistically coupled to splicing, translation, or replication.

#### MMUT

- **Related proteins** (co-abundance neighbors): ALDH5A1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methylmalonyl-CoA mutase. This gene encodes the mitochondrial enzyme methylmalonyl Coenzyme A mutase. In humans, the product of this gene is a vitamin B12-dependent enzyme which catalyzes the isomerization of methylmalonyl-CoA to succinyl-CoA, while in other species this enzyme may have different functions. Mutations in this gene may lead to various types of methylmalonic aciduria. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: methylmalonic aciduria due to methylmalonyl-CoA mutase deficiency (0.829); vitamin B12-unresponsive methylmalonic acidemia type mut0 (0.627); methylmalonic acidemia (0.578); vitamin B12-unresponsive methylmalonic acidemia type mut- (0.549); Methylmalonic aciduria (0.519)
- **Europe PMC papers**: 499
- **Why important**: MMUT is the metabolic endpoint of the module's linear branch with ALDH5A1. It encodes the vitamin B twelve-dependent enzyme that converts methylmalonyl-CoA to succinyl-CoA and participates in propionyl-CoA and homocysteine metabolism. Its liver and hepatocyte enhancement, cytosolic localization, testis detection, and established association with methylmalonic aciduria make it informative for interpreting the metabolic component. Its literature volume is lower than that of MCM2 but still substantial.
- **Conclusion**: Established evidence supports MMUT as a central intermediary-metabolism enzyme. Its presence supports a possible metabolic-state component in the module, while the specific link to stem-cell or testis biology remains a hypothesis.
