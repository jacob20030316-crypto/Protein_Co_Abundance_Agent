# Conserved co-abundance modules: cerebrospinal_fluid and placenta

## Module 1

**Tissue pair**: cerebrospinal_fluid and placenta  
**Genes (5)**: DBI, GSTP1, IGFBP3, MDH1, TIMP1

### Function

The module does not have a globally significant GO or KEGG enrichment: no GO or KEGG term passed global correction. Its gene-level biology is nevertheless coherent enough to suggest a mixed extracellular-regulatory, metabolic, lipid-handling, and redox-response signal. TIMP1 and IGFBP3 support extracellular matrix and growth-factor regulation, while MDH1, DBI, and GSTP1 represent central metabolism, lipid handling, and detoxification or oxidative-stress response. The co-abundance structure is centered on TIMP1, with links to IGFBP3, MDH1, and GSTP1, whereas MDH1 connects to DBI. This pattern is better interpreted as a cross-tissue physiological state or cellular-composition signal than as evidence for a defined molecular complex.

**Cell composition.** The module is not predominantly an immune-cell signature: most genes have low immune-cell specificity, with only IGFBP3 showing immune-cell enrichment for plasmacytoid dendritic cells. Two genes, TIMP1 and IGFBP3, are secreted to blood, so circulating protein contribution or blood exposure may influence measurements. HPA annotations otherwise point toward tissue- or cell-associated expression, including placenta, blood vessel, heart muscle, tongue, esophageal epithelial populations, stromal cells, trophoblasts, Hofbauer cells, and hepatocytes. The shared cerebrospinal-fluid and placenta module could therefore reflect soluble proteins together with tissue-associated or cellular-composition effects. The placenta protein-detection evidence is mixed across the module, and there is no matching cerebrospinal-fluid HPA protein-detection evidence in the fact sheet.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no STRING functional-enrichment result was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not supported here as established physical protein interactions or membership in a known multiprotein complex. The known biology is instead at the level of individual proteins: TIMP1 inhibits matrix metalloproteinases and can influence proliferation and apoptosis; IGFBP3 regulates circulating IGF availability; MDH1 participates in cytosolic malate metabolism and the malate-aspartate shuttle; DBI binds acyl-CoA and participates in lipid metabolism; and GSTP1 participates in glutathione-dependent detoxification and oxidative-stress responses.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a previously unrecognized cross-tissue co-abundance pattern, because the module is conserved between cerebrospinal fluid and placenta and is not represented by a high-confidence STRING interaction set or a hu.MAP complex. However, absence from STRING or hu.MAP does not establish novelty: co-abundance modules can capture shared regulation, secretion, tissue composition, or indirect physiology rather than physical interactions. The lack of globally significant GO or KEGG enrichment, the small module, the absence of STRING enrichment, and the mixed tissue and cellular annotations all make a strong claim of a new biological pathway premature. Replication in independent cohorts, control for cellular composition and protein abundance, and targeted testing of the co-abundance relationships would be needed.

**Hypothesis.** Hypothesis: a shared soluble and tissue-state program links extracellular matrix or growth-factor regulation with cellular metabolic and stress-response capacity in cerebrospinal fluid and placenta. In this model, TIMP1 and IGFBP3 represent the extracellular or circulating component, while MDH1, DBI, and GSTP1 reflect metabolic, lipid-handling, and redox state in the contributing cells. The apparent module could arise from coordinated regulation or from correlated mixtures of secreted proteins and tissue-derived cellular material; the current evidence does not distinguish these possibilities.

### Important genes

#### TIMP1

- **Related proteins** (co-abundance neighbors): IGFBP3 (0.93), MDH1 (0.93), GSTP1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TIMP metallopeptidase inhibitor 1. This gene belongs to the TIMP gene family. The proteins encoded by this gene family are natural inhibitors of the matrix metalloproteinases (MMPs), a group of peptidases involved in degradation of the extracellular matrix. In addition to its inhibitory role against most of the known MMPs, the encoded protein is able to promote cell proliferation in a wide range of cell types, and may also have an …
- **Diseases (Open Targets)**: neoplasm (0.120); Sepsis (0.119); glioblastoma (0.119); colorectal carcinoma (0.119); neurodegenerative disease (0.117)
- **Europe PMC papers**: 25183
- **Why important**: TIMP1 is the central network node, connecting IGFBP3, MDH1, and GSTP1. It is secreted to blood, is tissue enhanced in blood vessels, and has established roles in matrix metalloproteinase inhibition, cell proliferation, apoptosis, cytokine response, and hormone response. Its disease associations span neoplastic, inflammatory, septic, and neurodegenerative contexts, and it has an extensive literature base.
- **Conclusion**: Established evidence supports TIMP1 as the principal extracellular-regulatory anchor of the module and as a plausible contributor to a soluble cross-tissue signal. It is not established that TIMP1 physically interacts with the other module proteins in this module. A role as the upstream coordinator of the entire module remains a hypothesis.

#### IGFBP3

- **Related proteins** (co-abundance neighbors): TIMP1 (0.93); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor binding protein 3. This gene is a member of the insulin-like growth factor binding protein (IGFBP) family and encodes a protein with an IGFBP domain and a thyroglobulin type-I domain. The protein forms a ternary complex with insulin-like growth factor acid-labile subunit (IGFALS) and either insulin-like growth factor (IGF) I or II. In this form, it circulates in the plasma, prolonging the half-life of IGFs and alter…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.494); lymphatic system disorder (0.383); Alzheimer disease (0.368); cancer (0.365); colorectal cancer (0.365)
- **Europe PMC papers**: 9893
- **Why important**: IGFBP3 is directly connected to TIMP1 and is tissue enhanced in placenta, with enrichment in extravillous trophoblasts. It is secreted to blood and binds IGF together with the acid-labile subunit, thereby affecting IGF persistence and receptor access. Its annotations include regulation of protein phosphorylation, proliferation, signal transduction, and smooth-muscle migration, with disease associations including skeletal abnormalities, Alzheimer disease, and cancer.
- **Conclusion**: Established evidence supports IGFBP3 as the strongest placenta-associated and circulating component of the module, with a plausible role in growth-factor availability. The data do not establish that IGFBP3 drives the shared module or that its association with TIMP1 reflects direct molecular binding.

#### MDH1

- **Related proteins** (co-abundance neighbors): TIMP1 (0.93), DBI (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Centrosome, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: malate dehydrogenase 1. This gene encodes an enzyme that catalyzes the NAD/NADH-dependent, reversible oxidation of malate to oxaloacetate in many metabolic pathways, including the citric acid cycle. Two main isozymes are known to exist in eukaryotic cells: one is found in the mitochondrial matrix and the other in the cytoplasm. This gene encodes the cytosolic isozyme, which plays a key role in the malate-aspartate shuttl…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 88 (0.499); prostate carcinoma (0.455); neurodegenerative disease (0.348); asthma (0.320); Abnormality of the skeletal system (0.295)
- **Europe PMC papers**: 3198
- **Why important**: MDH1 occupies an intermediate network position, linking TIMP1 to DBI. It is tissue enhanced in heart muscle and tongue, is detected in placenta, and encodes the cytosolic malate dehydrogenase involved in malate metabolism, the tricarboxylic acid cycle, and the malate-aspartate shuttle. Its disease associations include developmental epileptic encephalopathy and neurodegenerative disease.
- **Conclusion**: Established evidence supports MDH1 as a metabolic-state marker within the module and as a bridge between the extracellular TIMP1 signal and the lipid-associated DBI signal. A mechanistic metabolic connection to TIMP1 is not established by the available interaction databases or enrichment results.

#### DBI

- **Related proteins** (co-abundance neighbors): MDH1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: diazepam binding inhibitor, acyl-CoA binding protein. This gene encodes diazepam binding inhibitor, a protein that is regulated by hormones and is involved in lipid metabolism and the displacement of beta-carbolines and benzodiazepines, which modulate signal transduction at type A gamma-aminobutyric acid receptors located in brain synapses. The protein is conserved from yeast to mammals, with the most highly conserved domain consisting of seven conti…
- **Diseases (Open Targets)**: neurodegenerative disease (0.418); autoimmune disorder of central nervous system (0.192); hepatocellular carcinoma (0.082); glioblastoma (0.078); Wilson disease (0.066)
- **Europe PMC papers**: 11452
- **Why important**: DBI connects to MDH1 and has low overall tissue specificity, with cell-type enhancement in epithelial, hepatic, and epididymal populations. Its established function involves acyl-CoA binding, fatty-acid metabolism, phosphatidylcholine acyl-chain remodeling, and phospholipid transport. It also has disease associations involving neurodegenerative and central-nervous-system autoimmune disorders and a substantial literature base.
- **Conclusion**: Established evidence supports DBI as the lipid-handling component of the module and as a possible indicator of cellular metabolic composition. Its connection to MDH1 is a co-abundance relationship here, not an established physical interaction, and a role in linking lipid metabolism to the extracellular proteins remains hypothetical.

#### GSTP1

- **Related proteins** (co-abundance neighbors): TIMP1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutathione S-transferase pi 1. Glutathione S-transferases (GSTs) are a family of enzymes that play an important role in detoxification by catalyzing the conjugation of many hydrophobic and electrophilic compounds with reduced glutathione. Based on their biochemical, immunologic, and structural properties, the soluble GSTs are categorized into 4 main classes: alpha, mu, pi, and theta. This GST family member is a polymorphic gene…
- **Diseases (Open Targets)**: neurodegenerative disease (0.350); breast cancer (0.117); hepatocellular carcinoma (0.115); neoplasm (0.114); posterior cortical atrophy (0.113)
- **Europe PMC papers**: 12759
- **Why important**: GSTP1 is connected to the central TIMP1 node and is tissue enhanced in esophagus, with enhancement in several epithelial and respiratory cell populations. It is detected in placenta and has established functions in glutathione metabolism, xenobiotic detoxification, prostaglandin metabolism, oxidative-stress response, and inflammatory regulation. It has broad disease associations and an extensive literature base.
- **Conclusion**: Established evidence supports GSTP1 as a redox and detoxification component that may report epithelial or tissue-state contributions to the module. The data do not establish that GSTP1 directly regulates TIMP1 or that oxidative stress causes the complete cross-tissue co-abundance pattern.

## Module 2

**Tissue pair**: cerebrospinal_fluid and placenta  
**Genes (6)**: AEBP1, B2M, VCAN, MFGE8, IGF2R, VASN

### Function

The module is most consistent with an extracellular vascular and stromal remodeling program, with possible links to apoptotic-cell clearance, extracellular-matrix organization, TGF-beta regulation, lysosomal trafficking, and immune-related signaling. This interpretation is based on the functions of AEBP1, MFGE8, VASN, VCAN, B2M, and IGF2R and on their shared co-abundance pattern. However, no GO or KEGG term passed global multiple-testing correction, so there is no globally significant pathway enrichment to support a more specific functional assignment. The absence of significant enrichment does not invalidate the module, but it limits functional certainty.

**Cell composition.** The module is strongly enriched for secreted or extracellularly associated proteins: MFGE8, VCAN, B2M, AEBP1, and VASN have secretome annotations, while IGF2R is an intracellular trafficking receptor. HPA evidence points especially toward blood vessels and decidual stromal cells, with additional fibroblast, pericyte, smooth-muscle, endometrial-stromal, and choroid-plexus-related signals. Several genes also show immune-cell enhancement or enrichment, although the immune profile is mixed rather than uniform. Most genes are detected in placenta, whereas cerebrospinal-fluid protein detection has no matching HPA data in the fact sheet. Thus, the shared module may reflect extracellular vascular or stromal biology, secreted protein carryover, or shared cellular components in the sampled fluids and tissues rather than a dedicated cerebrospinal-fluid–placenta pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationships were present among the module genes, and no hu.MAP complex contained multiple module members. Therefore, the co-abundance structure is not supported by already catalogued high-confidence physical interactions or a known shared protein complex. The lack of STRING and hu.MAP support does not demonstrate that the genes do not interact biologically; it indicates that the observed association is primarily a co-abundance observation rather than a validated interaction network. The strongest internal network position belongs to AEBP1, which connects to VCAN, B2M, VASN, and MFGE8. MFGE8 connects VASN, IGF2R, and AEBP1, while the remaining genes are more peripheral.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously under-characterized co-abundance association, because it has no matching high-confidence STRING interactions, no multi-member hu.MAP complex, and no globally significant GO or KEGG enrichment. Nevertheless, these absences alone do not establish novelty: co-abundance can arise from shared tissue composition, secretion, extracellular transport, or correlated regulation without direct physical interaction. The vascular and decidual-stromal HPA pattern, together with the large amount of prior literature for several genes, suggests that the individual biology is not new. The potentially novel result is therefore the cross-compartment co-abundance pattern linking these genes in cerebrospinal fluid and placenta, not a newly discovered function for the genes themselves.

**Hypothesis.** Hypothesis: a shared vascular-stromal extracellular environment in placenta and cerebrospinal fluid drives coordinated abundance of matrix and secreted proteins, while immune-associated proteins and intracellular trafficking machinery track the same biological or sample-composition state. In this model, VCAN and AEBP1 mark extracellular-matrix and stromal remodeling, MFGE8 contributes apoptotic-cell clearance, VASN modulates TGF-beta-related signaling, and B2M and IGF2R reflect immune or trafficking-related components. This is a mechanistic hypothesis rather than an established pathway, because global enrichment was absent and neither STRING nor hu.MAP provided corroborating interactions.

### Important genes

#### AEBP1

- **Related proteins** (co-abundance neighbors): VCAN (0.94), B2M (0.92), VASN (0.84), MFGE8 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location Vesicles; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: AE binding protein 1. This gene encodes a member of carboxypeptidase A protein family. The encoded protein may function as a transcriptional repressor and play a role in adipogenesis and smooth muscle cell differentiation. Studies in mice suggest that this gene functions in wound healing and abdominal wall development. Overexpression of this gene is associated with glioblastoma. [provided by RefSeq, May 2013].
- **Diseases (Open Targets)**: Ehlers-Danlos syndrome, classic-like, 2 (0.715); Abnormality of the skeletal system (0.414); Ehlers-Danlos syndrome, classic type, 1 (0.340); carpal tunnel syndrome (0.318); autism spectrum disorder (0.266)
- **Europe PMC papers**: 1535
- **Why important**: AEBP1 has the most central network position, connecting the vascular or stromal-associated genes VCAN, VASN, and MFGE8 as well as B2M. HPA places it in blood vessels and stromal or fibroblast-related cell types. Its reported roles in transcriptional repression, proteolysis, collagen-fibril organization, smooth-muscle differentiation, and wound healing make it a plausible coordinator of the module's extracellular and remodeling signal. It also has substantial literature support and disease links involving connective-tissue and skeletal abnormalities.
- **Conclusion**: Established evidence supports AEBP1 as the network hub and as a vascular or stromal-associated gene with roles in transcriptional regulation, protein processing, and matrix organization. It is a plausible module organizer, but the co-abundance data do not establish that AEBP1 regulates the other genes. Any hub-driven mechanism remains a hypothesis.

#### MFGE8

- **Related proteins** (co-abundance neighbors): VASN (0.98), IGF2R (0.85), AEBP1 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: milk fat globule EGF and factor V/VIII domain containing. This gene encodes a preproprotein that is proteolytically processed to form multiple protein products. The major encoded protein product, lactadherin, is a membrane glycoprotein that promotes phagocytosis of apoptotic cells. This protein has also been implicated in wound healing, autoimmune disease, and cancer. Lactadherin can be further processed to form a smaller cleavage product, medin, which c…
- **Diseases (Open Targets)**: AL amyloidosis (0.462); angina pectoris (0.339); myocardial ischemia (0.333); coronary artery bypass (0.314); coronary atherosclerosis (0.312)
- **Europe PMC papers**: 2623
- **Why important**: MFGE8 is highly connected within the module and links AEBP1, VASN, and IGF2R. It is secreted to blood, associated with blood vessels and stromal or pericyte-related cell types, and is detected in placenta. Its established lactadherin function in phagocytosis of apoptotic cells provides a biologically coherent connection to tissue remodeling and immune clearance. It also has extensive literature and disease associations involving amyloidosis, ischemic disease, and vascular pathology.
- **Conclusion**: Established evidence supports MFGE8 as a secreted vascular or stromal protein involved in apoptotic-cell clearance and tissue repair. It is a strong candidate for linking extracellular remodeling to immune clearance in the module. Whether it mechanistically connects the other module members in cerebrospinal fluid and placenta is unproven.

#### VCAN

- **Related proteins** (co-abundance neighbors): AEBP1 (0.94); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles, Mid piece, Principal piece, End piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: versican. This gene is a member of the aggrecan/versican proteoglycan family. The protein encoded is a large chondroitin sulfate proteoglycan and is a major component of the extracellular matrix. This protein is involved in cell adhesion, proliferation, proliferation, migration and angiogenesis and plays a central role in tissue morphogenesis and maintenance. Mutations in this gene are the cause of Wagner s…
- **Diseases (Open Targets)**: Wagner disease (0.745); Abnormality of the skeletal system (0.581); diverticular disease (0.521); inherited retinal dystrophy (0.446); hereditary disease (0.417)
- **Europe PMC papers**: 7002
- **Why important**: VCAN is a major extracellular-matrix proteoglycan and is associated with cell adhesion, migration, angiogenesis, morphogenesis, and glial migration. HPA links it to blood vessels, decidual and endometrial stromal cells, fibroblast-related cells, and myeloid populations. Although its network position is peripheral, its biological role provides a strong matrix context for the module. It has the largest literature volume among the module genes and a defined association with Wagner syndrome.
- **Conclusion**: Established evidence supports VCAN as an extracellular-matrix and vascular or stromal remodeling marker with relevance to development and disease. Its co-abundance with AEBP1 is compatible with matrix remodeling, but the module does not prove a direct interaction or a specific role in cerebrospinal fluid.

#### VASN

- **Related proteins** (co-abundance neighbors): MFGE8 (0.98), AEBP1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Mitochondria; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vasorin. Enables transforming growth factor beta binding activity. Involved in negative regulation of epithelial to mesenchymal transition and negative regulation of transforming growth factor beta receptor signaling pathway. Located in cell surface and extracellular exosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.334); prostate carcinoma (0.318); diverticular disease (0.283); type 2 diabetes mellitus (0.160); urolithiasis (0.107)
- **Europe PMC papers**: 552
- **Why important**: VASN connects directly to MFGE8 and AEBP1 and is tissue-enhanced in blood vessels. HPA also associates it with astrocytes, choroid-plexus epithelial cells, and ependymal cells, giving it particular relevance to the cerebrospinal-fluid side of the tissue pair. Its annotated TGF-beta binding activity and roles in negative regulation of epithelial-to-mesenchymal transition and TGF-beta receptor signaling provide a plausible signaling bridge between vascular, stromal, and barrier-associated biology.
- **Conclusion**: Established evidence supports VASN as an extracellular or cell-surface TGF-beta-related regulator with vascular and nervous-system-associated cellular expression. Its position and annotations make it a useful candidate bridge between the two tissue contexts. A cross-tissue signaling role is a hypothesis, not a demonstrated consequence of this module.

#### B2M

- **Related proteins** (co-abundance neighbors): AEBP1 (0.92); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Plasma membrane; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: beta-2-microglobulin. This gene encodes a serum protein found in association with the major histocompatibility complex (MHC) class I heavy chain on the surface of nearly all nucleated cells. The protein has a predominantly beta-pleated sheet structure that can form amyloid fibrils in some pathological conditions. The encoded antimicrobial protein displays antibacterial activity in amniotic fluid. A mutation in this gen…
- **Diseases (Open Targets)**: MHC class I deficiency (0.656); diffuse large B-cell lymphoma (0.595); HIV infectious disease (0.532); amyloidosis, hereditary systemic 6 (0.528); AL amyloidosis (0.468)
- **Europe PMC papers**: 25100
- **Why important**: B2M is connected to the network hub AEBP1 and is a secreted blood-associated protein linked to MHC class one biology and immune regulation. HPA shows broad tissue specificity with several immune and non-immune cell associations, and placenta detection is present. Its extensive literature and disease associations make it a strong indicator of antigen-presentation or inflammatory state, but its broad expression also makes it vulnerable to reflecting sample composition rather than module-specific biology.
- **Conclusion**: Established evidence supports B2M as an MHC class one-associated serum protein with immune relevance and broad cellular distribution. In this module it may report inflammatory or cellular-composition state. It should not be interpreted as evidence for a specialized module pathway without additional experiments.

## Module 4

**Tissue pair**: cerebrospinal_fluid and placenta  
**Genes (5)**: FGB, LAMA5, LAMB1, LAMC1, LTBP1

### Function

The module is most consistent with an extracellular-matrix and basement-membrane program centered on laminin assembly and cell–matrix signaling. LAMB1, LAMC1, and LAMA5 form a coherent laminin-related core supported by the strong STRING relationships and the shared hu.MAP memberships (STRING SMART Laminin N-terminal domain (domain VI); within-query FDR = 0.0427) (hu.MAP huMAP3_01175.1) (hu.MAP huMAP3_08112.1) (hu.MAP huMAP3_14233.1). LTBP1 connects this core to latent transforming-growth-factor-beta handling and extracellular-matrix targeting, while FGB adds a blood-borne fibrinogen component associated with cell–matrix adhesion, coagulation, and vascular injury responses. No GO or KEGG term passed global correction, so the functional interpretation is based on gene functions, network structure, STRING, hu.MAP, and HPA evidence rather than statistically significant GO or KEGG enrichment.

**Cell composition.** All genes are annotated as secreted proteins, with four directed to the extracellular matrix or blood. HPA indicates a strong extracellular and stromal or vascular character: fibroblasts are repeatedly represented, and cytotrophoblasts and vascular smooth muscle cells are also represented. Placenta is a frequent enriched tissue, whereas FGB is liver-enriched and hepatocyte-enriched and is secreted to blood. Most genes were not detected in immune cells, with only LTBP1 showing immune-cell enrichment in basophils. Thus, this shared cerebrospinal-fluid and placenta module may reflect extracellular-matrix proteins, vascular or stromal cell material, and circulating blood-derived protein in the samples rather than a cell-intrinsic program shared by all tissues. HPA protein detection in cerebrospinal fluid has no available matching evidence, and placenta protein detection is mixed, so tissue-level protein localization remains incomplete.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The established interaction core is the laminin triangle among LAMA5, LAMB1, and LAMC1 (STRING SMART Laminin N-terminal domain (domain VI); within-query FDR = 0.0427). These relationships are biologically coherent with laminin heterotrimer formation and basement-membrane organization, and they are independently supported by hu.MAP complexes containing LAMB1 and LAMC1 (hu.MAP huMAP3_01175.1) (hu.MAP huMAP3_08112.1) (hu.MAP huMAP3_14233.1). The hu.MAP evidence also places these two laminin subunits in complexes with additional extracellular-matrix and related proteins, but it does not establish that every listed partner belongs to this co-abundance module. LTBP1 and FGB have no reported STRING partners or hu.MAP complexes in the supplied evidence. Consequently, the network combines a well-known laminin subnetwork with co-abundance links involving LTBP1 and FGB whose molecular association is less directly established.

**STRING interactions (score >= 0.7)**: 3 of 10 gene pairs: LAMA5–LAMB1 (0.998); LAMA5–LAMC1 (0.999); LAMB1–LAMC1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Laminin N-terminal domain (domain VI) (FDR = 0.0427, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01175.1 (LAMB1, LAMC1; 2/2); huMAP3_08112.1 (LAMB1, LAMC1; 2/5); huMAP3_14233.1 (LAMB1, LAMC1; 2/14)

### Novelty

The laminin relationships are not a new molecular discovery: they are strongly supported by STRING, hu.MAP, and established laminin biology. The possible novel aspect is the coordinated occurrence of this laminin core with LTBP1 and FGB across cerebrospinal fluid and placenta. That interpretation is provisional because co-abundance can arise from shared secretion, vascular contribution, extracellular-matrix turnover, or sample composition. The absence of LTBP1 or FGB relationships from the supplied STRING and hu.MAP results does not prove novelty, and the lack of globally significant GO or KEGG enrichment neither validates nor invalidates the module. Overall, this is best described as a potentially informative cross-tissue co-abundance configuration built around a known laminin module, rather than a demonstrated new pathway or complex.

**Hypothesis.** Hypothesis: a shared vascular or stromal extracellular-matrix state in placenta and cerebrospinal fluid promotes coordinated release or persistence of laminin subunits and LTBP1, while circulating fibrinogen contributes a blood-derived signal linked to matrix remodeling or vascular permeability. LTBP1 could couple basement-membrane organization to storage and activation of latent transforming growth factor beta, and FGB could mark accompanying coagulation-related or injury-related extracellular remodeling. This mechanism predicts that the module will track vascular or stromal material and matrix turnover more strongly than immune-cell abundance; it requires direct testing with cell-resolved measurements, vascular or blood contamination markers, and measurements of transforming-growth-factor-beta activity.

### Important genes

#### LTBP1

- **Related proteins** (co-abundance neighbors): LAMA5 (0.94), FGB (0.91), LAMC1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: latent transforming growth factor beta binding protein 1. The protein encoded by this gene belongs to the family of latent TGF-beta binding proteins (LTBPs). The secretion and activation of TGF-betas is regulated by their association with latency-associated proteins and with latent TGF-beta binding proteins. The product of this gene targets latent complexes of transforming growth factor beta to the extracellular matrix, where the latent cytokine is subse…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.551); diverticular disease (0.523); autosomal recessive cutis laxa type 2 (0.507); osteoarthritis, knee (0.485); osteoarthritis, hip (0.467)
- **Europe PMC papers**: 2354
- **Why important**: LTBP1 has the strongest network position, linking both the laminin core and FGB. Its established function is to target latent transforming-growth-factor-beta complexes to the extracellular matrix and regulate their secretion and activation. HPA supports vascular, fibroblast, hepatic-stellate, and progenitor-associated expression, and its extracellular-matrix secretion is compatible with the proposed bridge between matrix structure and signaling. It also has substantial literature and disease associations involving connective-tissue and skeletal abnormalities.
- **Conclusion**: Established evidence supports LTBP1 as the module's matrix-signaling connector and as a plausible biological bridge between laminins and FGB. It is a leading mechanistic candidate, but the specific cross-tissue co-abundance relationship and any causal role in cerebrospinal-fluid or placental biology remain hypotheses.

#### LAMC1

- **Related proteins** (co-abundance neighbors): LAMB1 (0.94), LTBP1 (0.84); STRING partners: LAMA5 (0.999), LAMB1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Plasma membrane; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_01175.1, huMAP3_08112.1, huMAP3_14233.1
- **Function (MyGene.info)**: laminin subunit gamma 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: Fuchs' endothelial dystrophy (0.487); prostate carcinoma (0.467); colorectal cancer (0.447); eye disorder (0.434); benign colon neoplasm (0.427)
- **Europe PMC papers**: 4227
- **Why important**: LAMC1 is a core laminin subunit with strong links to LAMB1 and LAMA5 in STRING and membership in all supplied hu.MAP complexes containing module laminin members (STRING SMART Laminin N-terminal domain (domain VI); within-query FDR = 0.0427) (hu.MAP huMAP3_01175.1) (hu.MAP huMAP3_08112.1) (hu.MAP huMAP3_14233.1). Its established functions include basement-membrane structure, cell adhesion, migration, tissue development, and signaling. HPA shows placenta enhancement, extracellular-matrix secretion, and fibroblast-related cell-type enhancement. It has a large literature base and multiple disease associations.
- **Conclusion**: Established evidence identifies LAMC1 as a central structural component of the laminin portion of the module. Its role in the cross-tissue pattern is likely structural or abundance-driven, but whether it mediates a specific shared cerebrospinal-fluid and placental process is unproven.

#### LAMB1

- **Related proteins** (co-abundance neighbors): LAMC1 (0.94), LAMA5 (0.81); STRING partners: LAMA5 (0.998), LAMC1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_01175.1, huMAP3_08112.1, huMAP3_14233.1
- **Function (MyGene.info)**: laminin subunit beta 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins are composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respecti…
- **Diseases (Open Targets)**: cobblestone lissencephaly without muscular or ocular involvement (0.800); Fuchs' endothelial dystrophy (0.494); eye disorder (0.434); corneal disorder (0.424); corneal dystrophy (0.423)
- **Europe PMC papers**: 3735
- **Why important**: LAMB1 is a core laminin subunit and is strongly connected to LAMC1 and LAMA5 (STRING SMART Laminin N-terminal domain (domain VI); within-query FDR = 0.0427). It is present in all supplied hu.MAP complexes containing module laminin members (hu.MAP huMAP3_01175.1) (hu.MAP huMAP3_08112.1) (hu.MAP huMAP3_14233.1), giving it both network and complex-level support. Its established annotations include cell adhesion, cell migration, signal transduction, and neuronal–glial interaction during cortical radial-glia migration. HPA supports placenta, cytotrophoblast, decidual stromal, and endometrial stromal associations, and it has extensive literature and disease associations.
- **Conclusion**: Established evidence supports LAMB1 as a principal structural and signaling component of the module, with particular relevance to placental stromal and trophoblast biology. The shared tissue-level co-abundance may reflect laminin production or extracellular persistence rather than a newly defined LAMB1 pathway.

#### LAMA5

- **Related proteins** (co-abundance neighbors): LTBP1 (0.94), LAMB1 (0.81); STRING partners: LAMB1 (0.998), LAMC1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit alpha 5. This gene encodes one of the vertebrate laminin alpha chains. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins are composed of 3 non identical chains: l…
- **Diseases (Open Targets)**: nephrotic syndrome, IIa 26 (0.761); bent bone dysplasia syndrome 2 (0.563); colorectal cancer (0.491); LAMA5-related multisystemic syndrome (0.475); polyp of colon (0.467)
- **Europe PMC papers**: 2881
- **Why important**: LAMA5 completes the strongly connected laminin core with LAMB1 and LAMC1 (STRING SMART Laminin N-terminal domain (domain VI); within-query FDR = 0.0427). Its established functions include integrin-mediated signaling, organ morphogenesis, cell adhesion, and cell migration. HPA shows cytotrophoblast and podocyte-related enhancement, extracellular-matrix secretion, and vesicular localization. It has substantial literature and disease associations involving renal, skeletal, and multisystem phenotypes.
- **Conclusion**: Established evidence supports LAMA5 as the alpha-chain component that gives the laminin core its matrix-receptor and tissue-patterning relevance. Its contribution to the shared module is biologically plausible, but a specific placenta–cerebrospinal-fluid mechanism remains a hypothesis.

#### FGB

- **Related proteins** (co-abundance neighbors): LTBP1 (0.91); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibrinogen beta chain. The protein encoded by this gene is the beta component of fibrinogen, a blood-borne glycoprotein comprised of three pairs of nonidentical polypeptide chains. Following vascular injury, fibrinogen is cleaved by thrombin to form fibrin which is the most abundant component of blood clots. In addition, various cleavage products of fibrinogen and fibrin regulate cell adhesion and spreading, display vas…
- **Diseases (Open Targets)**: congenital afibrinogenemia (0.786); familial dysfibrinogenemia (0.705); congenital fibrinogen deficiency (0.622); familial hypodysfibrinogenemia (0.597); cancer (0.592)
- **Europe PMC papers**: 4215
- **Why important**: FGB is the peripheral module member connected to LTBP1 and is distinct from the laminin core. It encodes a blood-borne fibrinogen component whose established functions include fibrin formation, blood coagulation, platelet activation, fibrinolysis, and cell–matrix adhesion. HPA identifies liver and hepatocytes as enriched and describes secretion to blood. It has extensive literature and strong associations with inherited fibrinogen disorders and cancer-related biology.
- **Conclusion**: Established evidence supports FGB as a circulating or vascular-context marker that may connect the matrix program to coagulation and tissue injury. Its presence does not establish a direct physical complex with laminins or LTBP1; blood contribution, vascular permeability, or extracellular remodeling are alternative explanations.
