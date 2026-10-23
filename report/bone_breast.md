# Conserved co-abundance modules: bone and breast

## Module 0

**Tissue pair**: bone and breast  
**Genes (14)**: ABCF3, AMIGO2, BAIAP2, CDK6, FANCI, KRT10, KRT9, KRT2, KRT1, MMS19, MSI2, NCOA4, OCLN, UBE3A

### Function

The module is best interpreted as an epithelial structural and barrier program centered on keratin intermediate filaments and cornified-envelope biology. The primary evidence is the concordant set of globally corrected terms for keratin filament (GO:CC keratin filament; q_global = 0.000757), intermediate filament organization (GO:BP intermediate filament organization; q_global = 0.00105), cornified envelope formation (KEGG Cornified envelope formation - Homo sapiens (human); q_global = 0.00309), intermediate filament-based processes (GO:BP intermediate filament-based process; q_global = 0.00405), intermediate filament cytoskeleton organization (GO:BP intermediate filament cytoskeleton organization; q_global = 0.00405), epidermal structural function (GO:MF structural constituent of skin epidermis; q_global = 0.00832), intermediate filament (GO:CC intermediate filament; q_global = 0.0121), peptide cross-linking (GO:BP peptide cross-linking; q_global = 0.0256), and intermediate filament cytoskeleton (GO:CC intermediate filament cytoskeleton; q_global = 0.0372). The core signal is carried by KRT1, KRT10, KRT2, and KRT9, with OCLN additionally represented in (KEGG Cornified envelope formation - Homo sapiens (human); q_global = 0.00309). This supports epithelial differentiation, mechanical resilience, keratinization, and barrier formation rather than a generic housekeeping function. The remaining module genes may represent correlated tissue, cell-state, regulatory, or sample-composition signals rather than a single fully connected molecular complex.

**Cell composition.** The module is not predominantly a plasma-protein or secreted-protein module: the HPA summary identifies only one secreted gene. Its composition is strongly epithelial and keratinocyte-associated, with tissue enrichment for skin and cell-type enrichment for suprabasal keratinocytes. Breast myoepithelial cells also recur among the enriched cell types, which is relevant to the breast component of the conserved module. Several genes show immune-cell enhancement or associations with hematopoietic, megakaryocyte, platelet, or lymphoid populations, while others have low immune-cell specificity. Therefore, the shared bone-breast signal could reflect epithelial or myoepithelial content, with a possible contribution from shared vascular, marrow, platelet, or immune-associated sample components. The HPA breast protein data show detection for many genes but absence for the keratin core members, so transcript co-abundance should not be equated automatically with coordinated protein abundance in breast.

**GO/KEGG enrichment**: 9 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC keratin filament | 0.000757 | KRT1, KRT10, KRT2, KRT9 |
| GO:BP intermediate filament organization | 0.00105 | KRT1, KRT10, KRT2, KRT9 |
| KEGG Cornified envelope formation - Homo sapiens (human) | 0.00309 | KRT1, KRT10, KRT2, KRT9, OCLN |
| GO:BP intermediate filament-based process | 0.00405 | KRT1, KRT10, KRT2, KRT9 |
| GO:BP intermediate filament cytoskeleton organization | 0.00405 | KRT1, KRT10, KRT2, KRT9 |
| GO:MF structural constituent of skin epidermis | 0.00832 | KRT1, KRT10, KRT2 |
| GO:CC intermediate filament | 0.0121 | KRT1, KRT10, KRT2, KRT9 |
| GO:BP peptide cross-linking | 0.0256 | KRT1, KRT10, KRT2 |
| GO:CC intermediate filament cytoskeleton | 0.0372 | KRT1, KRT10, KRT2, KRT9 |

### STRING and hu.MAP

STRING provides a known, high-confidence keratin subnetwork among KRT1, KRT10, and KRT2. These relationships are consistent with established heterotypic keratin filament biology and support the interpretation of the core as a real structural epithelial program. STRING does not provide an interaction for KRT9 in this module, so its co-abundance with the keratin core is supportive of shared differentiation state but is not independently established here as a STRING interaction. hu.MAP identifies one complex containing MMS19 and FANCI together (hu.MAP huMAP3_09042.1), but the module contains only a small subset of that complex and the other module genes are not represented in a reported hu.MAP complex. Thus, the module combines a known keratin interaction backbone, a limited DNA-repair or iron-sulfur-related complex association, and module-specific co-abundance links that are not established protein-complex evidence.

**STRING interactions (score >= 0.7)**: 3 of 91 gene pairs: KRT1–KRT10 (0.999); KRT1–KRT2 (0.956); KRT10–KRT2 (0.904)
**STRING functional enrichment (supplementary, within-query FDR)**: DISEASES Epidermolytic hyperkeratosis (FDR = 4.81e-05, 4 genes); Keyword Keratin (FDR = 0.00033, 4 genes); COMPARTMENTS Keratin filament (FDR = 0.00057, 4 genes); SMART Intermediate filament protein (FDR = 0.00061, 4 genes); Keyword Intermediate filament (FDR = 0.00063, 4 genes); Component Keratin filament (FDR = 0.00074, 4 genes); DISEASES Bullous congenital ichthyosiform erythroderma (FDR = 0.0015, 3 genes); DISEASES Epidermolytic palmoplantar keratoderma (FDR = 0.0015, 3 genes); InterPro Intermediate filament protein, conserved site (FDR = 0.0026, 4 genes); InterPro Intermediate filament, rod domain (FDR = 0.0026, 4 genes); RCTM Formation of the cornified envelope (FDR = 0.0042, 4 genes); NetworkNeighborAL Mixed, incl. Ichthyosis vulgaris, and Bullous congenital ichthyosiform erythroderma (FDR = 0.0057, 3 genes); COMPARTMENTS Cornified envelope (FDR = 0.0094, 3 genes); Keyword Ichthyosis (FDR = 0.0107, 3 genes); HPO Congenital bullous ichthyosiform erythroderma (FDR = 0.0175, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09042.1 (MMS19, FANCI; 2/26)

### Novelty

This is not a wholly new biological theme: keratin filament assembly, epidermal differentiation, cornified-envelope formation, and the disease relevance of the keratin genes are already well established by GO, STRING, MyGene.info, Open Targets, and the literature. The module may nevertheless be a new cross-tissue co-abundance observation because the specific association of this broader gene set, including AMIGO2 and several regulatory or genome-maintenance genes, is not reproduced as a known STRING network or hu.MAP complex in the supplied evidence. That absence alone does not establish novelty. A defensible claim is that the potentially novel result is the conservation of this co-abundance pattern across bone and breast, which requires validation in independent cohorts, control for epithelial and blood-cell composition, and comparison with previously published tissue co-expression modules.

**Hypothesis.** Hypothesis: the conserved module reflects variation in epithelial or myoepithelial differentiation and barrier-state abundance across bone and breast samples. A keratinization program involving KRT1, KRT10, KRT2, and KRT9 may co-vary with epithelial junctional integrity through OCLN and with cell-adhesion or membrane organization through AMIGO2. The peripheral genes could reflect linked cell-state regulation, proliferation, proteostasis, DNA-damage handling, or marrow and blood-derived cellular admixture. This hypothesis predicts that module activity will track epithelial or myoepithelial cell abundance and differentiation markers more strongly than a universal intracellular pathway, and that its apparent conservation will weaken after explicit adjustment for cellular composition.

### Important genes

#### AMIGO2

- **Related proteins** (co-abundance neighbors): NCOA4 (0.93), KRT10 (0.88), ABCF3 (0.88), MSI2 (0.86), BAIAP2 (0.85), OCLN (0.84), UBE3A (0.83), FANCI (0.81), CDK6 (0.81), MMS19 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Plasma membrane; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adhesion molecule with Ig like domain 2. Predicted to be involved in several processes, including heterophilic cell-cell adhesion via plasma membrane cell adhesion molecules; homophilic cell adhesion via plasma membrane adhesion molecules; and negative regulation of programmed cell death. Predicted to act upstream of or within positive regulation of synapse assembly. Predicted to be located in nucleus and plasma membrane. Predicted to be…
- **Diseases (Open Targets)**: hypothyroidism (0.288); Abnormality of the skeletal system (0.272); type 2 diabetes mellitus (0.259); diabetes mellitus (0.258); malnutrition (0.248)
- **Europe PMC papers**: 1256
- **Why important**: AMIGO2 is the strongest network hub in the module and connects the keratin core to OCLN, NCOA4, ABCF3, MSI2, BAIAP2, UBE3A, and FANCI. It has HPA enhancement in blood vessel and breast myoepithelial cells, is detected in breast, and is annotated for homophilic and heterophilic cell adhesion and negative regulation of programmed cell death. It is not included in the globally significant GO/KEGG terms, has no supplied STRING or hu.MAP support, and has a substantial but smaller literature base than the major keratins, making it an important candidate bridge rather than an established module mechanism.
- **Conclusion**: Established evidence supports AMIGO2 as the network connector and a cell-adhesion-associated membrane protein. It is plausible, but not demonstrated, that AMIGO2 links epithelial structural state to the keratin program. Its centrality may arise from co-abundance architecture rather than direct physical interaction.

#### KRT1

- **Related proteins** (co-abundance neighbors): KRT9 (0.85), KRT2 (0.83); STRING partners: KRT10 (0.999), KRT2 (0.956)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 is a core keratin member present in every globally significant GO/KEGG term (GO:CC keratin filament; q_global = 0.000757) through (GO:CC intermediate filament cytoskeleton; q_global = 0.0372). It is tissue-enriched in skin and cell-type-enriched in suprabasal keratinocytes, has high-confidence STRING links to KRT10 and KRT2, and is associated with epidermal structural function, keratinization, and epidermolytic or palmoplantar disorders. It also has the largest supplied literature volume among the module genes.
- **Conclusion**: Established evidence identifies KRT1 as a central structural component of differentiated stratified epithelium and a strong anchor for the module interpretation. Its presence in bone-breast co-abundance does not by itself show that bone contains a keratinized epithelial compartment; sample composition or epithelial-like cells must be considered.

#### KRT10

- **Related proteins** (co-abundance neighbors): KRT2 (0.88), AMIGO2 (0.88), KRT9 (0.84); STRING partners: KRT1 (0.999), KRT2 (0.904)
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 10. This gene encodes a member of the type I (acidic) cytokeratin family, which belongs to the superfamily of intermediate filament (IF) proteins. Keratins are heteropolymeric structural proteins which form the intermediate filament. These filaments, along with actin microfilaments and microtubules, compose the cytoskeleton of epithelial cells. Mutations in this gene are associated with epidermolytic …
- **Diseases (Open Targets)**: epidermolytic hyperkeratosis 2A, autosomal dominant (0.787); epidermolytic ichthyosis (0.772); congenital reticular ichthyosiform erythroderma (0.727); ichthyosis, annular epidermolytic 1 (0.647); annular epidermolytic ichthyosis (0.642)
- **Europe PMC papers**: 2736
- **Why important**: KRT10 is present in every globally significant GO/KEGG term (GO:CC keratin filament; q_global = 0.000757) through (GO:CC intermediate filament cytoskeleton; q_global = 0.0372), is tissue-enriched in skin and cell-type-enriched in suprabasal keratinocytes, and forms high-confidence STRING relationships with KRT1 and KRT2. Its annotation links it to keratinocyte differentiation, epidermis development, intermediate filament organization, and cornification, with established associations to epidermolytic hyperkeratosis and related ichthyotic disorders.
- **Conclusion**: Established evidence supports KRT10 as a defining marker of the differentiated keratinocyte and cornification component. It strengthens the epithelial-barrier interpretation, but its lack of breast protein detection in HPA cautions that the breast association may reflect transcript abundance, cellular admixture, or a related epithelial state rather than abundant KRT10 protein.

#### KRT2

- **Related proteins** (co-abundance neighbors): KRT10 (0.88), KRT9 (0.86), KRT1 (0.83); STRING partners: KRT1 (0.956), KRT10 (0.904)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location Intermediate filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 2. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is expressed largely in the upper spinous layer of epidermal keratinocytes and mutations in this gene …
- **Diseases (Open Targets)**: superficial epidermolytic ichthyosis (0.815); exfoliative ichthyosis (0.358); Palmoplantar hyperkeratosis (0.267); hereditary disease (0.193); Vertigo (0.145)
- **Europe PMC papers**: 7459
- **Why important**: KRT2 is present in every globally significant GO/KEGG term (GO:CC keratin filament; q_global = 0.000757) through (GO:CC intermediate filament cytoskeleton; q_global = 0.0372), is enriched in suprabasal keratinocytes, and participates in the high-confidence STRING keratin subnetwork with KRT1 and KRT10. Its known expression in the upper spinous epidermal layer and disease associations with bullous congenital ichthyosiform erythroderma and superficial epidermolytic ichthyosis make it a biologically specific marker of differentiated epidermal structure.
- **Conclusion**: Established evidence supports KRT2 as a core structural and differentiation gene, not merely a generic epithelial marker. Its co-abundance with the other keratins is expected for a coordinated keratinocyte state; the broader links to non-keratin genes remain hypotheses.

#### OCLN

- **Related proteins** (co-abundance neighbors): AMIGO2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cell Junctions; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: occludin. This gene encodes an integral membrane protein that is required for cytokine-induced regulation of the tight junction paracellular permeability barrier. Mutations in this gene are thought to be a cause of band-like calcification with simplified gyration and polymicrogyria (BLC-PMG), an autosomal recessive neurologic disorder that is also known as pseudo-TORCH syndrome. Alternative splicing results…
- **Diseases (Open Targets)**: pseudo-TORCH syndrome (0.792); hypertensive disorder (0.341); neurodegenerative disease (0.337); nodular goiter (0.304); nephrolithiasis (0.272)
- **Europe PMC papers**: 12525
- **Why important**: OCLN is the only non-keratin gene included in the globally significant cornified-envelope term (KEGG Cornified envelope formation - Homo sapiens (human); q_global = 0.00309). It is a plasma-membrane and cell-junction protein, is detected in breast, and has HPA cell-type enhancement in several epithelial populations. Its function in cytokine-regulated tight-junction permeability provides a plausible barrier-related complement to the keratin filament program. It connects to the module through AMIGO2 in the co-abundance graph but has no supplied STRING or hu.MAP support here.
- **Conclusion**: Established evidence supports OCLN as an epithelial junction and permeability-barrier component that is compatible with the module's structural interpretation. It is reasonable to hypothesize coordination with keratinization, but the fact sheet does not establish a direct OCLN-keratin interaction or a causal role in this module.

#### FANCI

- **Related proteins** (co-abundance neighbors): AMIGO2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_09042.1
- **Function (MyGene.info)**: FA complementation group I. The Fanconi anemia complementation group (FANC) currently includes FANCA, FANCB, FANCC, FANCD1 (also called BRCA2), FANCD2, FANCE, FANCF, FANCG, FANCI, FANCJ (also called BRIP1), FANCL, FANCM and FANCN (also called PALB2). The previously defined group FANCH is the same as FANCA. Fanconi anemia is a genetically heterogeneous recessive disorder characterized by cytogenetic instability, hypersensitiv…
- **Diseases (Open Targets)**: Fanconi anemia complementation group I (0.828); Fanconi anemia (0.817); mitochondrial DNA depletion syndrome 4a (0.569); mitochondrial disease (0.528); sensory ataxic neuropathy, dysarthria, and ophthalmoparesis (0.520)
- **Europe PMC papers**: 3049
- **Why important**: FANCI links the module to DNA-damage response and interstrand cross-link repair and is the module member paired with MMS19 in the hu.MAP complex (hu.MAP huMAP3_09042.1). HPA shows enhancement in bone marrow, lymphoid tissue, and several progenitor populations, including megakaryocyte and erythrocyte progenitors. It is detected in breast and has established disease associations with Fanconi anemia. Its network link to AMIGO2 is modest relative to the central keratin relationships, so it may report a distinct cellular component or state.
- **Conclusion**: Established evidence supports FANCI as a genome-maintenance and progenitor-associated gene, with a reported complex association with MMS19 (hu.MAP huMAP3_09042.1). It should not be interpreted as part of the keratin structural mechanism without further evidence. A plausible hypothesis is that FANCI marks proliferative or marrow-derived cellular variation accompanying the epithelial program.

## Module 1

**Tissue pair**: bone and breast  
**Genes (5)**: ADPRS, ARL6IP4, C1orf52, CROCC, RNF115

### Function

No GO or KEGG term passed global correction, so the module does not support a specific pathway-level functional assignment from enrichment. STRING functional enrichment was also absent. The network is organized around RNF115, with ADPRS, CROCC, ARL6IP4, and C1orf52 connected to that central gene. The annotations instead suggest a mixed intracellular module involving ubiquitin-dependent protein regulation, ADP-ribose removal and cellular stress or DNA-repair responses, centrosome and cilium biology, RNA splicing or processing, and RNA binding. These annotations are heterogeneous, so the most defensible interpretation is a possible intracellular proteostasis and cellular-maintenance module rather than a demonstrated pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of its genes is annotated as secreted. All genes have low tissue specificity, and the module lacks a recurrent enriched tissue signature. This argues against a clearly tissue-restricted bone or breast program. The single-cell annotations are heterogeneous, including myonuclei, cytotrophoblasts, esophageal epithelial populations, ciliated cells, photoreceptors, intestinal epithelial populations, and other cell types. Blood-cell evidence is also mixed: most genes have low immune-cell specificity, one is not detected in immune cells, and RNF115 is immune-cell enhanced in basophils. Thus, the shared signal could reflect broadly expressed intracellular biology or shared cellular composition rather than a specialized bone-breast mechanism. Breast protein detection is available for the module and is positive for most genes, whereas no matching bone tissue protein result is available.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was present among any gene pair, and no hu.MAP complex contained multiple module members. Therefore, the co-abundance relationships are not supported here as a known physical interaction network or recognized multiprotein complex. The pattern may reflect indirect regulation, shared expression control, cell-composition effects, or context-dependent relationships. The absence of STRING or hu.MAP support is evidence that the relationships are not represented in those resources, but it is not evidence that the biology is false.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This exact shared co-abundance configuration appears potentially under-characterized because it has no matching high-confidence STRING relationships, no supported multi-member hu.MAP complex, and no globally significant GO or KEGG enrichment. However, it cannot be claimed as a new biological mechanism from these facts alone. Several component genes have established molecular annotations and substantial literature, especially RNF115 and CROCC, while the network is sparse and its genes have heterogeneous functions. The appropriate conclusion is that the module-level association is a candidate novel observation requiring replication and independent validation, not a demonstrated novel pathway.

**Hypothesis.** Hypothesis: in bone and breast samples, variation in a broadly expressed intracellular-maintenance program may coordinate RNF115-associated protein turnover with ADPRS-linked ADP-ribose processing, CROCC-linked centrosome or cilium organization, and ARL6IP4 or C1orf52-linked RNA-related functions. This could arise through shared cellular state or cell composition and need not represent direct physical binding among the proteins. Testing should examine replication across independent cohorts, cell-type composition, protein abundance, and perturbation of RNF115 or the other module members.

### Important genes

#### RNF115

- **Related proteins** (co-abundance neighbors): ADPRS (0.87), CROCC (0.84), ARL6IP4 (0.81), C1orf52 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoli, Mitochondria; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ring finger protein 115. Enables ubiquitin-protein transferase activity. Involved in negative regulation of epidermal growth factor receptor signaling pathway; protein autoubiquitination; and ubiquitin-dependent protein catabolic process via the multivesicular body sorting pathway. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: breast carcinoma (0.167); neoplasm (0.104); breast cancer (0.102); hepatocellular carcinoma (0.098); lung adenocarcinoma (0.077)
- **Europe PMC papers**: 316
- **Why important**: RNF115 is the central network gene, connected to every other module member with the strongest overall network position. Its established annotation as an ubiquitin-protein transferase, together with roles in protein polyubiquitination, endosomal protein catabolism, and negative regulation of epidermal growth factor receptor and toll-like receptor signaling, gives it the clearest mechanistic link to intracellular regulation. It is detected in breast tissue, is immune-cell enhanced in basophils, has disease associations including breast carcinoma and other neoplasms, and has a substantial literature.
- **Conclusion**: Established evidence supports RNF115 as the best candidate hub and a regulator of ubiquitin-dependent signaling or protein turnover. It is only a hypothesis that RNF115 drives the co-abundance module or explains the bone-breast association.

#### ADPRS

- **Related proteins** (co-abundance neighbors): RNF115 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ADP-ribosylserine hydrolase. This gene encodes a member of the ADP-ribosylglycohydrolase family. The encoded enzyme catalyzes the removal of ADP-ribose from ADP-ribosylated proteins. This enzyme localizes to the mitochondria, in addition to the nucleus and cytoplasm.[provided by RefSeq, Feb 2009].
- **Diseases (Open Targets)**: neurodegeneration, childhood-onset, stress-induced, with variable ataxia and seizures (0.777); hereditary disease (0.193); Delayed speech and language development (0.111); Atypical absence seizure (0.111); Axial hypotonia (0.111)
- **Europe PMC papers**: 88
- **Why important**: ADPRS is directly connected to the network hub and has a defined enzymatic function as an ADP-ribosylserine hydrolase. Its reported roles include removal of ADP-ribose from proteins, DNA repair, base-excision repair, cellular response to superoxide, and negative regulation of necroptosis. Its nucleoplasmic localization and breast detection make it relevant to a possible intracellular stress or genome-maintenance interpretation. It also has a documented hereditary neurological disease association.
- **Conclusion**: Established evidence supports ADPRS as a plausible marker of ADP-ribose processing and cellular stress or repair. A functional connection between ADPRS and RNF115 in this module remains unestablished because neither STRING nor hu.MAP supports a known relationship.

#### CROCC

- **Related proteins** (co-abundance neighbors): RNF115 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Centrosome, Basal body; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ciliary rootlet coiled-coil, rootletin. Predicted to enable kinesin binding activity and structural molecule activity. Involved in several processes, including centriole-centriole cohesion; positive regulation of cilium assembly; and positive regulation of protein localization to cilium. Located in cytoskeleton; cytosol; and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: spontaneous abortion (0.351); Abnormality of the skeletal system (0.265); atherosclerosis (0.197); premature menopause (0.139); pulmonary tuberculosis (0.127)
- **Europe PMC papers**: 374
- **Why important**: CROCC is directly connected to RNF115 and encodes rootletin, a structural protein associated with the centrosome and basal body. Its established functions include centriole cohesion, cilium assembly, and protein localization to cilia. It has a relatively substantial literature and disease associations involving skeletal abnormality and other conditions. Its enhancement in ependymal, respiratory ciliated, and photoreceptor cells indicates cell-type-specific expression despite low overall tissue specificity.
- **Conclusion**: Established evidence supports CROCC as a cilium and centrosome biology marker. Its participation in a shared bone-breast intracellular program, or a direct relationship with RNF115, is a hypothesis rather than an established mechanism.

#### ARL6IP4

- **Related proteins** (co-abundance neighbors): RNF115 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ARF like GTPase 6 interacting protein 4. Enables identical protein binding activity. Predicted to be involved in RNA splicing and mRNA processing. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: intelligence (0.186); schizophrenia (0.139); Abdominal pain (0.085); Headache (0.085); Limb pain (0.085)
- **Europe PMC papers**: 187
- **Why important**: ARL6IP4 is directly connected to RNF115 and is annotated as a nuclear protein with a predicted role in RNA splicing and messenger RNA processing. Its enrichment in several absorptive intestinal and related epithelial cell types suggests that cell state may influence its co-abundance. It has a moderate literature base and reported associations with neurological and pain-related traits.
- **Conclusion**: Established evidence supports ARL6IP4 as an RNA-processing-associated gene with cell-type-variable expression. Its role as a mediator of the module or of bone-breast biology is not established and should be treated as a hypothesis.

#### C1orf52

- **Related proteins** (co-abundance neighbors): RNF115 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromosome 1 open reading frame 52. Enables RNA binding activity. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.209); rheumatoid arthritis (0.208); Paralysis (0.066); Alzheimer disease (0.044); conduction system disorder (0.042)
- **Europe PMC papers**: 56
- **Why important**: C1orf52 is directly connected to RNF115 and is annotated as a nucleoplasmic RNA-binding protein. It is the least functionally characterized member of the module, but its inclusion is informative because it may represent an uncharacterized RNA-related component of the co-abundance pattern. It has disease associations including neurodegenerative disease and rheumatoid arthritis, while its literature base is comparatively limited.
- **Conclusion**: Established evidence supports only a general RNA-binding and nucleoplasmic annotation for C1orf52. Any role in coordinating the other module genes, or in a bone-breast mechanism, remains speculative and requires direct functional testing.

## Module 2

**Tissue pair**: bone and breast  
**Genes (13)**: AP1G2, MT-ATP8, CCDC167, C8orf33, CNPY3, COMMD1, FAM107B, MAN2B1, MALSU1, STARD3NL, SVIP, SZRD1, TMEM106B

### Function

The module does not have a statistically established GO or KEGG functional label: no term passed global correction. Its structure instead suggests a loosely connected intracellular trafficking and organelle-maintenance program. The strongest network position is occupied by SVIP, which connects to proteins associated with ER-associated degradation, autophagy, vesicle-related processes, cholesterol handling, mitochondrial ATP synthesis, and poorly characterized proteins. STARD3NL links the central SVIP region to late-endosomal cholesterol transport, lysosomal and endosomal biology, and mitochondrial-associated proteins. Additional annotations point to protein quality control, glycoprotein turnover, innate-receptor folding, clathrin-mediated transport, and mitochondrial translation. These annotations are biologically compatible but do not constitute enrichment evidence. The most defensible interpretation is a heterogeneous co-abundance module involving intracellular membrane trafficking, endolysosomal function, protein quality control, and cellular energy-related processes.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a minority as secreted, and CNPY3 and MAN2B1 are described as intracellular or membrane-associated rather than circulating proteins. It is also not broadly blood-cell enriched overall, because most genes have low immune-cell specificity. Nevertheless, several members show cell-type enhancement in monocytes, neutrophils, macrophage or dendritic-cell populations, and related immune or epithelial populations, so variation in shared cell types or immune infiltration could contribute to the bone-breast co-abundance pattern. The predominance of low tissue specificity argues against a narrowly bone- or breast-specific program. HPA protein detection is available for breast for most members, whereas the fact sheet provides no matching bone tissue assessment; therefore the apparent conservation should not be interpreted as proof of identical cell-of-origin biology in both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the specified high-confidence threshold, and STRING supplied no supplementary functional enrichment. Thus the co-abundance edges are not supported here as established physical or functional STRING relationships. hu.MAP provides a single relevant complex overlap (hu.MAP huMAP3_11095.1), containing STARD3NL and MT-ATP8 among a much larger complex. This gives limited support for a shared organelle or membrane-associated context, but the sparse overlap and the absence of hu.MAP assignments for the other genes do not establish a unified complex. Overall, the module should be treated primarily as a coordinated expression or abundance pattern rather than a known protein complex.

**STRING interactions (score >= 0.7)**: 0 of 78 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11095.1 (STARD3NL, MT-ATP8; 2/45)

### Novelty

This module is plausibly a new or at least not previously established cross-tissue co-abundance association, because it has no high-confidence STRING relationships, no STRING enrichment, and only limited hu.MAP overlap (hu.MAP huMAP3_11095.1). However, these absences do not prove novelty: incomplete databases, context-dependent interactions, technical effects, and shared cell composition can all produce an apparently unsupported module. The annotations also describe several individually known processes, including ER quality control, cholesterol transport, lysosomal biology, glycoprotein catabolism, mitochondrial ATP synthesis, and vesicle transport. The novel claim should therefore be restricted to the specific coordinated pattern across bone and breast, which requires independent replication and control for cell-type composition.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of intracellular membrane and organelle homeostasis across bone and breast samples. SVIP may organize a protein-quality-control and trafficking-associated expression state, while STARD3NL may connect that state to late-endosomal cholesterol handling. CNPY3 and MAN2B1 could represent ER folding and glycoprotein turnover, whereas MT-ATP8 and MALSU1 could reflect a linked mitochondrial energy or translation state. The observed pattern may be driven by a shared stromal, epithelial, or myeloid cell population, or by a common stress and organelle-remodeling response, rather than by direct binding among all module members. This hypothesis should be tested with cell-composition adjustment, independent cohorts, perturbation experiments, and measurements of protein localization or interaction.

### Important genes

#### SVIP

- **Related proteins** (co-abundance neighbors): STARD3NL (0.91), COMMD1 (0.85), MT-ATP8 (0.84), AP1G2 (0.83), CCDC167 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: small VCP interacting protein. Endoplasmic reticulum-associated degradation (ERAD) is the pathway by which misfolded proteins in the endoplasmic reticulum are targeted to the proteasome for degradation. Multiple specialized proteins interact with one another during ERAD to complete this process. The protein encoded by this gene is an inhibitor of ERAD, functioning to disrupt the interaction of these protein components. This dow…
- **Diseases (Open Targets)**: sensorineural hearing loss disorder (0.444); hearing loss disorder (0.410); disorder of ear (0.304); placenta praevia (0.238); psoriatic arthritis (0.203)
- **Europe PMC papers**: 305
- **Why important**: SVIP has the strongest network connectivity and links the largest local portion of the module, including STARD3NL, COMMD1, MT-ATP8, AP1G2, and CCDC167. Its established description as a small VCP-interacting protein and regulator of ER-associated degradation, autophagy, protein lipidation, and VCP-complex assembly gives it a plausible organizing role. It also has substantial literature support and breast protein detection, although HPA indicates low tissue specificity.
- **Conclusion**: Established evidence supports SVIP as the principal network hub and as a regulator of ER and protein-homeostasis pathways. It is a plausible module coordinator, but its causal role in the bone-breast association remains a hypothesis because the module has no global GO or KEGG enrichment and no STRING-supported interactions.

#### STARD3NL

- **Related proteins** (co-abundance neighbors): SVIP (0.91), MAN2B1 (0.82), MALSU1 (0.82), TMEM106B (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_11095.1
- **Function (MyGene.info)**: STARD3 N-terminal like. This gene encodes a late-endosomal protein that contains a conserved MENTAL (MLN64 N-terminal) domain. The encoded protein binds cholesterol molecules and may play a role in endosomal cholesterol transport through interactions with metastatic lymph node protein 64 (MLN64). [provided by RefSeq, Sep 2011].
- **Diseases (Open Targets)**: bone fracture (0.231); alcohol drinking (0.231); bone Paget disease (0.218); osteoporosis (0.183); Dupuytren Contracture (0.183)
- **Europe PMC papers**: 240
- **Why important**: STARD3NL is a highly connected node near the module core and links SVIP with MAN2B1, MALSU1, and TMEM106B. Its known late-endosomal MENTAL domain and cholesterol-binding or cholesterol-transport role provide a coherent connection to endosomal membrane biology. It is also the only non-mitochondrial member participating in the hu.MAP overlap with MT-ATP8 (hu.MAP huMAP3_11095.1), and its disease associations include bone-related phenotypes such as fracture, Paget disease, and osteoporosis.
- **Conclusion**: Established evidence supports STARD3NL as a late-endosomal cholesterol-handling protein with a strategically important position in this module. Its possible role as a bridge between membrane lipid handling and bone-breast co-abundance is a hypothesis, not a demonstrated mechanism.

#### CNPY3

- **Related proteins** (co-abundance neighbors): CCDC167 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Plasma membrane; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: canopy FGF signaling regulator 3. This gene encodes a protein that binds members of the toll-like receptor protein family and functions as a chaperone to aid in folding and export of these proteins. Alternative splicing results in multiple transcript variants. Naturally occuring readthrough transcription occurs between this locus and the downstream GNMT (glycine N-methyltransferase) gene and is represented with GeneID:107080644. […
- **Diseases (Open Targets)**: genetic developmental and epileptic encephalopathy (0.676); infantile spasms (0.370); hypertension, pregnancy-induced (0.099); neoplasm (0.096); breast carcinoma (0.074)
- **Europe PMC papers**: 293
- **Why important**: CNPY3 is connected to CCDC167 and is an ER and plasma-membrane-associated chaperone for Toll-like receptor folding and export. Its HPA cell-type profile includes monocytes, neutrophils, Hofbauer cells, Kupffer cells, and dendritic-related populations, making it relevant to the possibility that immune or myeloid composition contributes to the shared module. It also has breast protein detection and a substantial literature base.
- **Conclusion**: Established evidence supports CNPY3 as an innate-receptor folding and export factor with a myeloid-associated expression profile. Its inclusion may indicate immune-cell or ER-trafficking biology, but the fact sheet does not establish whether it is a driver or merely a marker of the relevant cell population.

#### MAN2B1

- **Related proteins** (co-abundance neighbors): STARD3NL (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Nucleoplasm, Vesicles; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosidase alpha class 2B member 1. This gene encodes an enzyme that hydrolyzes terminal, non-reducing alpha-D-mannose residues in alpha-D-mannosides. Its activity is necessary for the catabolism of N-linked carbohydrates released during glycoprotein turnover and it is member of family 38 of glycosyl hydrolases. The full length protein is processed in two steps. First, a 49 aa leader sequence is cleaved off and the remainder of the …
- **Diseases (Open Targets)**: alpha-mannosidosis (0.858); hereditary disease (0.516); Intellectual disability (0.426); alpha-mannosidosis, adult form (0.379); alpha-mannosidosis, infantile form (0.378)
- **Europe PMC papers**: 731
- **Why important**: MAN2B1 connects to STARD3NL and supplies a defined lysosomal or glycoprotein-turnover function through degradation of terminal mannose residues in N-linked carbohydrates. It has strong disease relevance through alpha-mannosidosis and broad support in the literature. HPA associates it with myeloid and antigen-presenting cell populations and places it in vesicular and nucleoplasmic compartments.
- **Conclusion**: Established evidence supports MAN2B1 as a lysosomal glycoprotein-catabolism enzyme and as a possible indicator of myeloid or vesicular biology. Its proposed participation in a shared endolysosomal program is reasonable but remains inferential because no module-level enrichment passed global correction.

#### MT-ATP8

- **Related proteins** (co-abundance neighbors): SVIP (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F0 subunit 8. Contributes to proton-transporting ATP synthase activity, rotational mechanism. Involved in mitochondrial ATP synthesis coupled proton transport. Part of mitochondrial proton-transporting ATP synthase complex. Implicated in multiple sclerosis and urinary bladder cancer. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: mitochondrial disease (0.574); MELAS syndrome (0.565); MERRF syndrome (0.525); mitochondrial complex IV deficiency, nuclear-type (0.521); leigh syndrome due to mitochondrial complex iv deficiency (0.521)
- **Europe PMC papers**: 3137
- **Why important**: MT-ATP8 is directly connected to SVIP and is the second module member in the hu.MAP complex overlap (hu.MAP huMAP3_11095.1). It encodes a mitochondrial ATP synthase subunit involved in proton-driven mitochondrial ATP synthesis and is associated with mitochondrial disease phenotypes. Its tissue-enhanced HPA profile in heart muscle and cell-type associations including hepatocytes, pancreatic acinar cells, platelets, urothelial cells, and basophils suggest that its abundance may also be sensitive to cellular composition.
- **Conclusion**: Established evidence supports MT-ATP8 as a mitochondrial energy-production component and provides limited complex-level support through (hu.MAP huMAP3_11095.1). Its connection to the module may indicate energetic coupling to membrane and protein-homeostasis processes, but this coupling is a hypothesis and could alternatively reflect differences in mitochondrial content or cell mixture.

#### COMMD1

- **Related proteins** (co-abundance neighbors): SVIP (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: copper metabolism domain containing 1. COMMD1 is a regulator of copper homeostasis, sodium uptake, and NF-kappa-B (see MIM 164011) signaling (de Bie et al., 2005 [PubMed 16267171]).[supplied by OMIM, Sep 2009]
- **Diseases (Open Targets)**: neurodegenerative disease (0.488); Parkinson disease (0.305); infectious disease (0.275); autoimmune disease (0.225); cervical carcinoma (0.212)
- **Europe PMC papers**: 942
- **Why important**: COMMD1 is not a highly connected node, but it is directly connected to the central SVIP hub and has the largest literature support among the selected genes. Its established roles in copper homeostasis, NF-kappa-B signaling, endocytic recycling, Golgi-to-plasma-membrane transport, and ubiquitin-dependent proteasomal regulation connect immune signaling, trafficking, and protein turnover. It also has disease associations spanning neurodegenerative and autoimmune disease.
- **Conclusion**: Established evidence supports COMMD1 as a multifunctional regulator of trafficking, signaling, and protein degradation. Its direct association with SVIP makes it a useful interpretive link between ER quality control and signaling or recycling, but the module does not demonstrate that COMMD1 mediates the cross-tissue pattern.

## Module 3

**Tissue pair**: bone and breast  
**Genes (8)**: CBX8, CCDC137, HMGA2, ISY1, MIDEAS, NUP35, SMARCD1, SYNPO

### Function

The best-supported interpretation is a mixed nuclear gene-regulatory module rather than a single established biochemical pathway. HMGA2, SMARCD1, CBX8, and MIDEAS support chromatin organization and transcriptional regulation, while ISY1 supports spliceosome-dependent mRNA processing. NUP35 adds a nuclear-envelope and nucleocytoplasmic-transport connection, and SYNPO represents an actin-associated cell-shape and motility component. The co-abundance graph is compact and connected through these regulatory and structural links, but the absence of globally significant GO or KEGG enrichment globally significant GO/KEGG means that no pathway-level function has been statistically established. The annotations therefore support a broad cellular-state interpretation involving nuclear regulation, RNA processing, differentiation, and cell architecture, rather than a specific pathway.

**Cell composition.** This does not look like a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly intracellular or nuclear. Most genes have low tissue specificity, with isolated enrichment in bone marrow, testis, vascular or muscle tissues and varied cell-type enrichment. Most genes also have low immune-cell specificity, although HMGA2 and SYNPO show immune-cell-enhanced annotations in basophils and naive B cells. Thus, the module is not strongly characterized as a blood-cell module, but the immune-cell signals and the broad, heterogeneous HPA pattern mean that shared cell composition cannot be excluded. Breast protein detection is available for the module, whereas matching bone tissue protein data are unavailable, so the breast detection pattern should not be interpreted as evidence of bone-specific protein expression.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interactions are reported among the module genes, and no STRING functional-enrichment result is available. No hu.MAP complex contains multiple module members. Consequently, the co-abundance edges should not be treated as established direct physical interactions or as evidence of a known multiprotein complex. The annotations instead indicate potentially compatible cellular roles: HMGA2, SMARCD1, CBX8, and MIDEAS participate in chromatin or transcriptional control; ISY1 participates in spliceosome function; NUP35 participates in nuclear transport; and SYNPO participates in actin organization. These are functional annotations and not demonstrated relationships within this module.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported cross-tissue co-abundance pattern, but the available evidence is insufficient to call it a new biological mechanism. Its lack of high-confidence STRING links and hu.MAP complexes suggests that the observed association is not already captured as a canonical interaction module, yet database absence alone does not prove novelty. The absence of globally significant GO or KEGG enrichment also prevents a claim of a newly defined pathway. The most defensible conclusion is that this is a potentially novel or under-characterized co-abundance association whose reproducibility, cell-type origin, and relationship to known regulatory states require independent validation.

**Hypothesis.** Hypothesis: the module reflects a shared differentiation or proliferative cellular state present in bone and breast samples. In this model, HMGA2 may help establish a developmental chromatin state, SMARCD1 and CBX8 may remodel or repress selected transcriptional programs, and MIDEAS may reinforce transcriptional corepression. ISY1 may coordinate the corresponding RNA-processing program, while NUP35 may support the required nuclear transport. SYNPO could connect this nuclear state to changes in actin organization and cell morphology. A contribution from shared stromal, epithelial, vascular, muscle-like, or minor immune-cell populations is also plausible because the HPA cell-type annotations are heterogeneous. This is a mechanistic hypothesis, not an established causal model.

### Important genes

#### HMGA2

- **Related proteins** (co-abundance neighbors): SYNPO (0.87), NUP35 (0.85), ISY1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Nucleoli, Nucleoli rim; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: high mobility group AT-hook 2. This gene encodes a protein that belongs to the non-histone chromosomal high mobility group (HMG) protein family. HMG proteins function as architectural factors and are essential components of the enhancesome. This protein contains structural DNA-binding domains and may act as a transcriptional regulating factor. Identification of the deletion, amplification, and rearrangement of this gene that ar…
- **Diseases (Open Targets)**: Silver-Russell syndrome 5 (0.762); type 2 diabetes mellitus (0.554); diabetes mellitus (0.536); Abnormality of the skeletal system (0.487); atrial fibrillation (0.457)
- **Europe PMC papers**: 11026
- **Why important**: HMGA2 is a central connector in the co-abundance graph and has the strongest network prominence in the module. Its established role as a chromatin-associated architectural and transcriptional regulator, together with annotations involving epithelial-to-mesenchymal transition, chondrocyte differentiation, mesenchymal differentiation, and skeletal abnormalities, makes it particularly relevant to a bone–breast shared state. It is also the most extensively studied gene in the module and has substantial disease and developmental literature.
- **Conclusion**: Established evidence supports HMGA2 as a developmental chromatin regulator associated with mesenchymal and skeletal biology. Its central module position is consistent with, but does not prove, a coordinating role in this co-abundance pattern. The proposed role of HMGA2 as an upstream driver of the entire module remains a hypothesis.

#### SMARCD1

- **Related proteins** (co-abundance neighbors): ISY1 (0.83), CBX8 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SWI/SNF related BAF chromatin remodeling complex subunit D1. The protein encoded by this gene is a member of the SWI/SNF family of proteins, whose members display helicase and ATPase activities and which are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI and has sequence similarity to the yeast Swp73 protein…
- **Diseases (Open Targets)**: Coffin-Siris syndrome 11 (0.736); syndromic intellectual disability (0.416); Intellectual disability (0.372); Coffin-Siris syndrome (0.371); Global developmental delay (0.370)
- **Europe PMC papers**: 1063
- **Why important**: SMARCD1 is a bridge between ISY1 and CBX8 in the module and encodes a component of an ATP-dependent chromatin-remodeling complex. Its established annotations include chromatin remodeling, transcriptional regulation, cell differentiation, proliferation, and developmental processes. It has substantial literature and disease association through Coffin-Siris syndrome and related developmental phenotypes, making it an important candidate for interpreting the nuclear regulatory component.
- **Conclusion**: Established evidence supports SMARCD1 as a chromatin-remodeling and transcriptional regulator. Its module position suggests coordination with RNA processing and chromatin repression, but the co-abundance data do not establish direct interaction or causal control in bone or breast.

#### ISY1

- **Related proteins** (co-abundance neighbors): MIDEAS (0.84), SMARCD1 (0.83), HMGA2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ISY1 spliceosome associated protein. Enables RNA binding activity. Involved in mRNA splicing, via spliceosome. Located in nucleus. Part of U2-type catalytic step 1 spliceosome and catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dengue disease (0.370); myotonic syndrome (0.151); liver disorder (0.134); acute tonsillitis (0.123); placenta praevia (0.033)
- **Europe PMC papers**: 415
- **Why important**: ISY1 is one of the most connected module genes and links MIDEAS and SMARCD1 with HMGA2. It is an established spliceosome-associated protein involved in catalytic spliceosome formation, splice-site recognition, and mRNA splicing. Its network position provides a plausible connection between transcriptional chromatin state and downstream RNA maturation, and it has a substantial literature base compared with the less characterized module members.
- **Conclusion**: Established evidence supports ISY1 as a core RNA-splicing factor. Its inclusion in this module is consistent with coordinated regulation of transcription and RNA processing, but there is no evidence here that it specifically mediates the bone–breast association.

#### CBX8

- **Related proteins** (co-abundance neighbors): SMARCD1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromobox 8. Enables methylated histone binding activity. Involved in negative regulation of transcription by RNA polymerase II. Located in chromatin and nucleoplasm. Part of PRC1 complex. Biomarker of esophagus squamous cell carcinoma and glioblastoma. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: atrial fibrillation (0.509); smoking initiation (0.437); risk-taking behaviour (0.430); breast carcinoma (0.393); attention deficit-hyperactivity disorder (0.326)
- **Europe PMC papers**: 1166
- **Why important**: CBX8 connects to SMARCD1 and represents the chromatin-repression arm of the module. It binds methylated histones, participates in a Polycomb-related complex, and is annotated in transcriptional repression, heterochromatin formation, DNA repair, proliferation, and collagen biosynthesis. Its breast-carcinoma association and substantial literature make it relevant to the tissue context, despite its peripheral position in the co-abundance graph.
- **Conclusion**: Established evidence supports CBX8 as a chromatin-binding transcriptional repressor with roles in proliferation and genome regulation. Its co-abundance with SMARCD1 is compatible with a shared chromatin state, but does not demonstrate a direct complex or a breast-specific mechanism.

#### SYNPO

- **Related proteins** (co-abundance neighbors): HMGA2 (0.87), CCDC137 (0.87); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: synaptopodin. Synaptopodin is an actin-associated protein that may play a role in actin-based cell shape and motility. The name synaptopodin derives from the protein's associations with postsynaptic densities and dendritic spines and with renal podocytes (Mundel et al., 1997 [PubMed 9314539]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: nephrotic syndrome (0.260); Hypocalcemia (0.159); cervical carcinoma (0.156); osteoarthritis, hip (0.148); osteoarthritis, knee (0.148)
- **Europe PMC papers**: 1599
- **Why important**: SYNPO is the module member that most clearly connects nuclear regulatory genes to cell architecture. It is linked to HMGA2 and CCDC137 in the co-abundance graph and encodes an actin-associated protein involved in stress-fiber assembly, actin-bundle organization, cell shape, and motility-related processes. Its enrichment across vascular, cardiac, skeletal-muscle, epithelial, and immune-related cell annotations suggests that it may report cellular composition or structural state. It also has meaningful disease literature, including renal and musculoskeletal associations.
- **Conclusion**: Established evidence supports SYNPO as an actin-associated structural regulator rather than a nuclear transcriptional factor. Its presence may indicate a coordinated morphological state or shared cell population. Any claim that SYNPO functionally links the chromatin program to tissue remodeling remains a hypothesis.

## Module 4

**Tissue pair**: bone and breast  
**Genes (8)**: CCDC86, EPHA2, EPHB2, ERBIN, ERLIN2, ITGA5, ITGAV, NEGR1

### Function

The module is best interpreted as a cell-surface adhesion and vascular signaling module, with a particularly strong endothelial-growth-factor and integrin-receptor component. The primary evidence is the globally corrected enrichment for vascular endothelial growth factor signaling and cellular response to vascular endothelial growth factor stimulus (GO:BP vascular endothelial growth factor signaling pathway; q_global = 0.00424)(GO:BP cellular response to vascular endothelial growth factor stimulus; q_global = 0.0126), signaling receptor and molecular transducer activity (GO:MF signaling receptor activity; q_global = 0.0139)(GO:MF molecular transducer activity; q_global = 0.0139), integrin-mediated adhesion (GO:BP cell adhesion mediated by integrin; q_global = 0.0154), vascular endothelial growth factor receptor signaling (GO:BP vascular endothelial growth factor receptor signaling pathway; q_global = 0.0187), and broad cell adhesion (GO:BP cell adhesion; q_global = 0.0238). EPHA2, EPHB2, ITGA5, and ITGAV provide the clearest functional core. EPHA2 and ERBIN also support a possible link to negative regulation of chemokine production (GO:BP negative regulation of chemokine production; q_global = 0.0476), but this does not by itself establish an immune-function module. The sparse subgraph is nevertheless biologically coherent: receptor tyrosine kinases, integrin adhesion receptors, a cell-junction scaffold, and cell-adhesion-associated proteins are connected into a shared membrane and adhesion signaling program. No KEGG term is reported as primary evidence in the fact sheet.

**Cell composition.** This does not look like a module dominated by broadly expressed housekeeping proteins. Most members are membrane-associated, junctional, receptor, adhesion, or signaling proteins, with ERLIN2 providing an endoplasmic-reticulum lipid-raft component and CCDC86 providing a more nuclear, mitotic-associated component. The HPA summary reports two secreted genes, although the gene-level descriptions mainly emphasize intracellular, membrane, junctional, vesicular, or focal-adhesion localization rather than a uniformly secreted program. Blood contamination is not the simplest explanation: most genes have low or absent immune-cell specificity, while only a minority show immune-cell enrichment or enhancement. HPA instead points to multiple possible cellular sources, including fibroblast, endothelial-associated, epithelial, neuronal, and other tissue-restricted cell types. The breast protein evidence is present for most members, but the lack of matching HPA bone protein data prevents a direct tissue-level comparison. Thus, the conserved signal could reflect shared vascular, stromal, epithelial, or other adherent cell populations in bone and breast, rather than a purely blood-derived signal.

**GO/KEGG enrichment**: 8 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP vascular endothelial growth factor signaling pathway | 0.00424 | EPHA2, EPHB2, ITGA5 |
| GO:BP cellular response to vascular endothelial growth factor stimulus | 0.0126 | EPHA2, EPHB2, ITGA5 |
| GO:MF signaling receptor activity | 0.0139 | EPHA2, EPHB2, ITGA5, ITGAV |
| GO:MF molecular transducer activity | 0.0139 | EPHA2, EPHB2, ITGA5, ITGAV |
| GO:BP cell adhesion mediated by integrin | 0.0154 | EPHA2, ITGA5, ITGAV |
| GO:BP vascular endothelial growth factor receptor signaling pathway | 0.0187 | EPHA2, EPHB2, ITGA5 |
| GO:BP cell adhesion | 0.0238 | EPHA2, EPHB2, ERBIN, ITGA5, ITGAV, NEGR1 |
| GO:BP negative regulation of chemokine production | 0.0476 | EPHA2, ERBIN |

### STRING and hu.MAP

STRING supports two especially clear pre-existing pairwise relationships: EPHA2 with EPHB2 and ITGA5 with ITGAV. The supplementary STRING enrichments also converge on receptor complexes, cell adhesion, glycoproteins, plasma-membrane components, integrins, and tyrosine-protein kinases (STRING Component Receptor complex; within-query FDR = 0.0011)(STRING Keyword Glycoprotein; within-query FDR = 0.004)(STRING Keyword Receptor; within-query FDR = 0.004)(STRING Keyword Cell adhesion; within-query FDR = 0.0049)(STRING COMPARTMENTS Integral component of plasma membrane; within-query FDR = 0.0159)(STRING Keyword Integrin; within-query FDR = 0.0227)(STRING Keyword Tyrosine-protein kinase; within-query FDR = 0.029). These are supportive context rather than independent global enrichment evidence. hu.MAP contributes a receptor complex containing EPHA2 and EPHB2, with EPHA6 as the additional complex member (hu.MAP huMAP3_06834.1). The remaining module relationships, including the links involving NEGR1, ERBIN, and CCDC86, are not represented by high-confidence STRING partners or hu.MAP complexes in the supplied results. Therefore, part of the module recapitulates known receptor and integrin biology, while the complete co-abundance configuration extends beyond the currently catalogued physical-interaction and complex evidence.

**STRING interactions (score >= 0.7)**: 2 of 28 gene pairs: EPHA2–EPHB2 (0.851); ITGA5–ITGAV (0.946)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Receptor complex (FDR = 0.0011, 4 genes); Keyword Glycoprotein (FDR = 0.004, 6 genes); Keyword Receptor (FDR = 0.004, 4 genes); Keyword Cell adhesion (FDR = 0.0049, 4 genes); Keyword Host cell receptor for virus entry (FDR = 0.0049, 3 genes); Keyword Signal (FDR = 0.012, 5 genes); Keyword Disulfide bond (FDR = 0.012, 5 genes); COMPARTMENTS Integral component of plasma membrane (FDR = 0.0159, 4 genes); SMART Ephrin receptor ligand binding domain (FDR = 0.0165, 2 genes); Pfam Ephrin type-A receptor 2 transmembrane domain (FDR = 0.0218, 2 genes); Keyword Integrin (FDR = 0.0227, 2 genes); Keyword Cell junction (FDR = 0.0239, 4 genes); Keyword Cell membrane (FDR = 0.0239, 5 genes); SMART Integrin alpha (beta-propellor repeats). (FDR = 0.0287, 2 genes); Keyword Tyrosine-protein kinase (FDR = 0.029, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06834.1 (EPHA2, EPHB2; 2/3)

### Novelty

The module should not be called a wholly new molecular interaction discovery. The EPHA2–EPHB2 relationship is supported by both STRING and hu.MAP, and the ITGA5–ITGAV relationship is supported by STRING. However, the conserved co-abundance module across bone and breast, including its full combination of Eph receptors, integrins, NEGR1, ERBIN, ERLIN2, and CCDC86, is not fully explained by those resources. The absence of STRING or hu.MAP evidence for several edges is compatible with a tissue-contextual association, indirect regulation, co-expression, or incomplete database coverage; it is not proof of novelty. The defensible conclusion is that the cross-tissue module configuration is a potentially novel systems-level observation built partly from established interactions, requiring validation with independent cohorts, cell-type-resolved data, and perturbation or protein-interaction experiments.

**Hypothesis.** Hypothesis: in both bone and breast, a shared adherent vascular or stromal cell population co-regulates Eph receptor signaling with integrin-dependent extracellular-matrix adhesion. EPHA2 and EPHB2 may coordinate receptor-mediated cell positioning, contact, and growth-factor responses, while ITGA5 and ITGAV may couple matrix engagement to vascular signaling and cytoskeletal organization. NEGR1 and ERBIN could help connect cell-cell or cell-matrix adhesion to membrane organization and receptor regulation, with ERLIN2 potentially modifying lipid-raft and endoplasmic-reticulum signaling. The CCDC86 association may represent a context-dependent proliferative or cell-state signal rather than a direct component of the adhesion machinery. This mechanism is a testable interpretation, not an established causal model.

### Important genes

#### EPHA2

- **Related proteins** (co-abundance neighbors): EPHB2 (0.86), ERBIN (0.81); STRING partners: EPHB2 (0.851)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06834.1
- **Function (MyGene.info)**: EPH receptor A2. This gene belongs to the ephrin receptor subfamily of the protein-tyrosine kinase family. EPH and EPH-related receptors have been implicated in mediating developmental events, particularly in the nervous system. Receptors in the EPH subfamily typically have a single kinase domain and an extracellular region containing a Cys-rich domain and 2 fibronectin type III repeats. The ephrin receptors are d…
- **Diseases (Open Targets)**: early-onset posterior polar cataract (0.770); total early-onset cataract (0.770); early-onset non-syndromic cataract (0.681); colorectal cancer (0.594); chronic myeloid leukemia (0.583)
- **Europe PMC papers**: 8524
- **Why important**: EPHA2 is the strongest functional anchor because it participates in every primary enrichment theme reported for the gene, including vascular endothelial growth factor signaling, receptor activity, integrin-mediated adhesion, cell adhesion, and negative regulation of chemokine production (GO:BP vascular endothelial growth factor signaling pathway; q_global = 0.00424)(GO:BP cellular response to vascular endothelial growth factor stimulus; q_global = 0.0126)(GO:MF signaling receptor activity; q_global = 0.0139)(GO:MF molecular transducer activity; q_global = 0.0139)(GO:BP cell adhesion mediated by integrin; q_global = 0.0154)(GO:BP vascular endothelial growth factor receptor signaling pathway; q_global = 0.0187)(GO:BP cell adhesion; q_global = 0.0238)(GO:BP negative regulation of chemokine production; q_global = 0.0476). It connects to EPHB2 in STRING and to the hu.MAP receptor complex (hu.MAP huMAP3_06834.1), and its network position links the receptor core to ERBIN. Its receptor-tyrosine-kinase biology, vascular and osteoblast annotations, disease associations, and extensive literature make it a high-confidence interpretive entry point.
- **Conclusion**: Established: EPHA2 is a membrane receptor tyrosine kinase associated with angiogenesis, cell adhesion, and osteoblast differentiation, and it is supported by both the module enrichment and external interaction resources. Hypothesis: EPHA2 may coordinate the shared bone-breast adhesion and vascular response, but the co-abundance data do not demonstrate that it causally controls the other module members.

#### EPHB2

- **Related proteins** (co-abundance neighbors): EPHA2 (0.86), ITGAV (0.84), CCDC86 (0.81); STRING partners: EPHA2 (0.851)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_06834.1
- **Function (MyGene.info)**: EPH receptor B2. This gene encodes a member of the Eph receptor family of receptor tyrosine kinase transmembrane glycoproteins. These receptors are composed of an N-terminal glycosylated ligand-binding domain, a transmembrane region and an intracellular kinase domain. They bind ligands called ephrins and are involved in diverse cellular processes including motility, division, and differentiation. A distinguishing …
- **Diseases (Open Targets)**: medullary thyroid gland carcinoma (0.542); Familial prostate cancer (0.477); Rare hemorrhagic disorder due to a constitutional platelet anomaly (0.450); osteoarthritis, hip (0.404); neoplasm (0.398)
- **Europe PMC papers**: 4927
- **Why important**: EPHB2 is a highly connected receptor member of the module and contributes to the vascular signaling, receptor-activity, and cell-adhesion primary terms (GO:BP vascular endothelial growth factor signaling pathway; q_global = 0.00424)(GO:BP cellular response to vascular endothelial growth factor stimulus; q_global = 0.0126)(GO:MF signaling receptor activity; q_global = 0.0139)(GO:MF molecular transducer activity; q_global = 0.0139)(GO:BP vascular endothelial growth factor receptor signaling pathway; q_global = 0.0187)(GO:BP cell adhesion; q_global = 0.0238). It forms the best-supported receptor pair with EPHA2 in STRING and belongs to the hu.MAP complex (hu.MAP huMAP3_06834.1). Its annotated roles in angiogenesis, cell-surface receptor tyrosine-kinase signaling, motility, division, and differentiation provide a direct mechanistic basis for interpreting the module as a signaling and adhesion program. It also has substantial literature and disease-annotation support.
- **Conclusion**: Established: EPHB2 is a membrane Eph receptor with known signaling and developmental functions, and its relationship with EPHA2 is independently supported. Hypothesis: EPHB2 may help translate shared tissue or cell-contact cues into coordinated adhesion and vascular behavior in bone and breast.

#### ITGA5

- **Related proteins** (co-abundance neighbors): NEGR1 (0.83); STRING partners: ITGAV (0.946)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha 5. The product of this gene belongs to the integrin alpha chain family. Integrins are heterodimeric integral membrane proteins composed of an alpha subunit and a beta subunit that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha 5 subunit. This subunit associates with the beta 1 subunit t…
- **Diseases (Open Targets)**: skin disorder (0.223); body weight gain (0.174); non-small cell lung carcinoma (0.116); neoplasm (0.115); hepatocellular carcinoma (0.108)
- **Europe PMC papers**: 6985
- **Why important**: ITGA5 is one of the central genes in the primary vascular-growth-factor and integrin adhesion enrichments (GO:BP vascular endothelial growth factor signaling pathway; q_global = 0.00424)(GO:BP cellular response to vascular endothelial growth factor stimulus; q_global = 0.0126)(GO:MF signaling receptor activity; q_global = 0.0139)(GO:MF molecular transducer activity; q_global = 0.0139)(GO:BP cell adhesion mediated by integrin; q_global = 0.0154)(GO:BP vascular endothelial growth factor receptor signaling pathway; q_global = 0.0187)(GO:BP cell adhesion; q_global = 0.0238). Its annotation as the alpha subunit of the beta-one fibronectin receptor directly supports an extracellular-matrix interpretation. It is tissue enhanced in blood vessels and cell-type enhanced in fibroblast, lymphatic endothelial, stromal, trophoblast, and monocyte populations, which is informative for a shared vascular or stromal source. Its relationship with ITGAV is strongly supported by STRING, and its extensive literature and cancer-related annotations make it a well-established adhesion and invasion marker.
- **Conclusion**: Established: ITGA5 provides a credible matrix-adhesion and vascular-cell component of the module, with direct enrichment and STRING support. Hypothesis: ITGA5 may couple fibronectin engagement to Eph-receptor signaling in the conserved tissue program.

#### ITGAV

- **Related proteins** (co-abundance neighbors): EPHB2 (0.84), NEGR1 (0.83); STRING partners: ITGA5 (0.946)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha V. The product of this gene belongs to the integrin alpha chain family. Integrins are heterodimeric integral membrane proteins composed of an alpha subunit and a beta subunit that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha V subunit. This subunit associates with beta 1, beta 3, beta…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); myocardial infarction (0.396); angina pectoris (0.371); Recurrent thrombophlebitis (0.370); intermediate coronary syndrome (0.370)
- **Europe PMC papers**: 5475
- **Why important**: ITGAV contributes to the primary receptor-activity, molecular-transducer, integrin adhesion, and cell-adhesion terms (GO:MF signaling receptor activity; q_global = 0.0139)(GO:MF molecular transducer activity; q_global = 0.0139)(GO:BP cell adhesion mediated by integrin; q_global = 0.0154)(GO:BP cell adhesion; q_global = 0.0238). It occupies a bridging position between EPHB2 and NEGR1 in the co-abundance graph, while its alpha-subunit biology supports cell-matrix adhesion, angiogenesis, vasculogenesis, and cytoskeletal or calcium-linked signaling. The ITGA5–ITGAV relationship is strongly supported by STRING, and its focal-adhesion localization is consistent with the proposed membrane-to-matrix signaling mechanism.
- **Conclusion**: Established: ITGAV is a plausible adhesion receptor component with primary enrichment support and a known relationship to ITGA5. Hypothesis: ITGAV may serve as a matrix signaling bridge between integrin adhesion and Eph-receptor-dependent cell behavior.

#### NEGR1

- **Related proteins** (co-abundance neighbors): ERLIN2 (0.91), ITGA5 (0.83), ITGAV (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles, Actin filaments, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neuronal growth regulator 1. Predicted to act upstream of or within several processes, including feeding behavior; locomotory behavior; and positive regulation of neuron projection development. Predicted to be located in extracellular region and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: major depressive disorder (0.585); intelligence (0.571); obesity disorder (0.547); Abnormality of the skeletal system (0.539); schizophrenia (0.505)
- **Europe PMC papers**: 1724
- **Why important**: NEGR1 has a prominent network position, connecting ERLIN2 with both integrin genes, and it is the only member in the supplied list with this particular combination of adhesion-associated and membrane-related connections. It contributes to the primary cell-adhesion term (GO:BP cell adhesion; q_global = 0.0238) and to supplementary STRING themes involving glycoproteins, cell adhesion, signaling, disulfide bonds, and cell membranes (STRING Keyword Glycoprotein; within-query FDR = 0.004)(STRING Keyword Cell adhesion; within-query FDR = 0.0049)(STRING Keyword Signal; within-query FDR = 0.012)(STRING Keyword Disulfide bond; within-query FDR = 0.012)(STRING Keyword Cell membrane; within-query FDR = 0.0239). Its HPA profile is brain enhanced and enriched in several neuronal or progenitor cell types, while its annotations include heterophilic cell-cell adhesion, synapse assembly, protein localization, and skeletal-system abnormality associations. Its literature is substantial, though its direct placement in this receptor-integrin module is less established than for the receptor and integrin genes.
- **Conclusion**: Established: NEGR1 is associated with cell-cell adhesion and membrane-related biology and is connected to the module's integrin side in the observed network. Hypothesis: NEGR1 may mark a specialized cell-contact or differentiation state that helps explain the conserved co-abundance pattern, but a direct biochemical link to the Eph-integrin core remains unproven.

## Module 5

**Tissue pair**: bone and breast  
**Genes (6)**: CFAP20, HSD17B8, GOLGA7, NCAM1, NCOR2, TOE1

### Function

The module does not support a single established pathway or molecular process: no GO or KEGG term passed global correction, and STRING functional enrichment was absent. Its structure is a hub-and-spoke co-abundance pattern centered on NCAM1, with weaker links to genes involved in steroid metabolism, Golgi-to-plasma-membrane transport and palmitoylation, transcriptional repression, RNA processing, and ciliary or flagellar biology. The most defensible interpretation is therefore a shared expression state rather than a validated biochemical pathway. NCAM1 provides a plausible cell-adhesion and cell-interaction axis, but the apparent combination with the other genes is biologically heterogeneous.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. Only NCAM1 is annotated as secreted in other tissues, while its principal annotated location is the plasma membrane; the remaining genes are non-secreted or have intracellular or ciliary annotations. The HPA profile is also not that of a uniformly blood-cell module: most genes have low immune-cell specificity, although NCAM1 is immune-cell enriched in NK cells and NCOR2 is immune-cell enhanced in basophils. Most genes have cell-type-enhanced rather than uniformly broad single-cell patterns, including reproductive-cell, enterocyte, epithelial, neural, trophoblast, megakaryocyte, and ciliary-cell annotations. Breast protein detection is present for most members, whereas matching bone protein data are unavailable, and NCAM1 is not detected in breast by immunohistochemistry. Thus, shared cell composition, low-level expression variation, or sampling-related cellular admixture remain plausible explanations; the data do not establish a bone-and-breast-specific mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair reaches the reported high-confidence STRING interaction threshold, and no hu.MAP complex contains multiple module members. Consequently, the five co-abundance edges should not be interpreted as established physical interactions, shared complexes, or direct regulatory links. The star-like topology is driven by NCAM1, while each peripheral gene is connected only to that hub in this subgraph. The absence of STRING and hu.MAP support weakens a protein-complex interpretation, although it does not exclude co-regulation, indirect relationships, tissue-composition effects, or context-dependent interactions.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported co-abundance pattern, but the available evidence is insufficient to call it a new biological mechanism. Its novelty is supported only in the limited sense that the particular cross-tissue co-abundance grouping has no reported high-confidence STRING or hu.MAP counterpart in the fact sheet. That absence alone does not prove novelty. The lack of globally significant GO or KEGG enrichment, absence of STRING enrichment, heterogeneous gene functions, and hub-dominated topology make a technical or cell-composition explanation at least as plausible as a new conserved pathway. A stronger novelty claim would require replication, control for cell composition, and comparison with independent co-expression datasets.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state or cell-mixture signal in bone and breast in which NCAM1 marks a membrane-associated adhesion or immune-related component, while correlated variation in steroid handling, transcriptional repression, membrane trafficking, RNA processing, and ciliary programs produces the peripheral associations. HSD17B8 and NCOR2 could provide hormone-responsive context, and GOLGA7 could influence membrane-protein trafficking, but these are mechanistic possibilities rather than demonstrated links. This hypothesis predicts that the module should weaken after adjustment for relevant cell populations and should replicate most strongly in samples containing comparable NCAM1-positive or otherwise compositionally similar cells.

### Important genes

#### NCAM1

- **Related proteins** (co-abundance neighbors): HSD17B8 (0.84), GOLGA7 (0.81), NCOR2 (0.80), TOE1 (0.80), CFAP20 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neural cell adhesion molecule 1. This gene encodes a cell adhesion protein which is a member of the immunoglobulin superfamily. The encoded protein is involved in cell-to-cell interactions as well as cell-matrix interactions during development and differentiation. The encoded protein plays a role in the development of the nervous system by regulating neurogenesis, neurite outgrowth, and cell migration. This protein is also involv…
- **Diseases (Open Targets)**: major depressive disorder (0.532); smoking initiation (0.501); gastroesophageal reflux disease (0.498); schizophrenia (0.463); irritable bowel syndrome (0.462)
- **Europe PMC papers**: 6731
- **Why important**: NCAM1 is the sole network hub, connected to every other module member, and therefore dominates the module's topology. Its established functions include cell-to-cell and cell-matrix interactions, neural development, cell migration, and expansion of lymphocyte and NK-cell populations. HPA places it at the plasma membrane, with tissue enhancement in brain and heart muscle and immune-cell enrichment in NK cells. It also has the largest literature volume among the module genes and multiple disease associations.
- **Conclusion**: Established: NCAM1 is the best marker and biological anchor of the module, with strong evidence for adhesion and cell-interaction functions and a possible immune or neural cellular contribution. Hypothesis: its centrality may reflect a shared NCAM1-positive cell state or cell-composition effect rather than direct molecular coordination with all peripheral genes.

#### HSD17B8

- **Related proteins** (co-abundance neighbors): NCAM1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydroxysteroid 17-beta dehydrogenase 8. In mice, the Ke6 protein is a 17-beta-hydroxysteroid dehydrogenase that can regulate the concentration of biologically active estrogens and androgens. It is preferentially an oxidative enzyme and inactivates estradiol, testosterone, and dihydrotestosterone. However, the enzyme has some reductive activity and can synthesize estradiol from estrone. The protein encoded by this gene is similar to Ke6 …
- **Diseases (Open Targets)**: maturity-onset diabetes of the young (0.083); breast cancer (0.074); breast carcinoma (0.074); maturity-onset diabetes of the young type 3 (0.072); hyperproinsulinemia (0.051)
- **Europe PMC papers**: 429
- **Why important**: HSD17B8 is a peripheral member linked only to NCAM1, but it contributes a distinct and biologically relevant steroid-metabolism axis. Its annotated function includes oxidative inactivation of estradiol, testosterone, and dihydrotestosterone, with some reductive steroid activity, and its reported processes include estrogen biosynthesis and metabolism. It is detected in breast tissue and has disease associations involving breast cancer and metabolic disease.
- **Conclusion**: Established: HSD17B8 is an estrogen- and androgen-metabolism enzyme with breast relevance. Hypothesis: its co-abundance with NCAM1 could reflect hormone-responsive epithelial or stromal variation, but the module provides no evidence that HSD17B8 directly regulates NCAM1 or that the module is an estrogen pathway.

#### NCOR2

- **Related proteins** (co-abundance neighbors): NCAM1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Immune cell enhanced; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nuclear receptor corepressor 2. This gene encodes a nuclear receptor co-repressor that mediates transcriptional silencing of certain target genes. The encoded protein is a member of a family of thyroid hormone- and retinoic acid receptor-associated co-repressors. This protein acts as part of a multisubunit complex which includes histone deacetylases to modify chromatin structure that prevents basal transcriptional activity of ta…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.493); prostate adenocarcinoma (0.443); colorectal adenocarcinoma (0.412); smoking initiation (0.403); respiratory system disorder (0.398)
- **Europe PMC papers**: 3320
- **Why important**: NCOR2 is a peripheral member connected to NCAM1 and encodes a transcriptional corepressor that works with histone deacetylase-containing complexes hu.MAP. Its annotations include transcriptional silencing, response to estradiol, lactation, and skeletal-system abnormality associations, making it relevant to both breast and bone contexts. It is detected in breast tissue and has a substantial literature base.
- **Conclusion**: Established: NCOR2 can modulate nuclear-receptor-linked transcription and chromatin state and has disease relevance spanning skeletal and cancer contexts. Hypothesis: NCOR2 may provide a transcriptional context in which NCAM1 and HSD17B8 vary together, but the lack of enrichment and physical-network support prevents assigning it a causal coordinating role.

#### GOLGA7

- **Related proteins** (co-abundance neighbors): NCAM1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: golgin A7. Involved in Golgi to plasma membrane protein transport; peptidyl-L-cysteine S-palmitoylation; and protein stabilization. Acts upstream of or within Golgi to plasma membrane transport. Located in Golgi membrane and Golgi stack. Is intrinsic component of Golgi membrane. Part of palmitoyltransferase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: COVID-19 (0.370); disorder of ear (0.312); neurodegenerative disease (0.312); body weight gain (0.223); placenta praevia (0.212)
- **Europe PMC papers**: 402
- **Why important**: GOLGA7 is a peripheral member connected only to NCAM1 and contributes a membrane-trafficking and palmitoylation interpretation. It is annotated as a Golgi-membrane component involved in Golgi-to-plasma-membrane transport, protein stabilization, and a palmitoyltransferase complex. It is detected in breast tissue and has disease associations including neurodegenerative disease and body-weight-related disease.
- **Conclusion**: Established: GOLGA7 participates in Golgi-to-surface transport and protein palmitoylation, processes that could affect membrane proteins such as NCAM1. Hypothesis: GOLGA7 may influence the abundance or localization of NCAM1 indirectly, but no STRING or hu.MAP evidence in this module establishes such a connection.

## Module 6

**Tissue pair**: bone and breast  
**Genes (5)**: CTDSPL2, FOXK1, TMEM237, WDR33, ZNF207

### Function

This module does not have a globally significant GO or KEGG enrichment term. STRING functional enrichment is also absent. Its co-abundance structure nevertheless links genes with complementary cellular roles: TMEM237 is associated with primary cilia and WNT signaling; FOXK1 with transcriptional repression, glucose homeostasis, and autophagy; CTDSPL2 with RNA polymerase II regulation, transcription, BMP-related regulation, cartilage, and bone development; ZNF207 with microtubules, mitotic spindle assembly, and chromosome segregation; and WDR33 with mRNA three-prime-end processing. The network is therefore compatible with coordinated regulation of nuclear gene expression, RNA processing, cell division, and ciliary or developmental signaling, but the module should not be assigned a single established pathway function from enrichment alone.

**Cell composition.** The module is not composed of plasma or secreted proteins: every member has no reported secretome annotation. The HPA evidence does not indicate blood-cell enrichment; four genes have low immune-cell specificity and one is not detected in immune cells. Four genes have low tissue specificity, while TMEM237 is tissue enriched in retina. Cell-type enhancement is distributed across basal keratinocytes, breast myoepithelial cells, lactotrophs, somatotrophs, and rod photoreceptor cells rather than concentrated in a blood lineage. All members were detected by breast immunohistochemistry, whereas matching HPA protein evidence for bone was unavailable. Thus, the shared bone–breast signal is more consistent with broadly expressed intracellular proteins, or with shared epithelial or developmental cellular programs, than with a plasma-protein or blood-contamination module. The HPA evidence alone does not establish which cell population generated the co-abundance pattern.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction passes the supplied high-confidence threshold, and no hu.MAP complex contains multiple module members. Consequently, the co-abundance edges are not supported here as established physical protein interactions or as a known multiprotein complex. The network may represent coordinated regulation, shared cellular-state dependence, indirect functional coupling, or tissue-composition effects. The strongest topological bridge is the FOXK1–CTDSPL2–WDR33 side together with the FOXK1–TMEM237–ZNF207 side, but this topology is an expression-network observation rather than evidence of direct binding.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially interesting cross-tissue co-abundance observation, but it cannot be called a newly established biological module on the present evidence. No GO or KEGG term passes global correction, STRING supplies no enrichment supplementary STRING and no high-confidence interaction support, and hu.MAP supplies no shared complex. These negative resources do not prove novelty, because co-abundance relationships can be absent from interaction and complex databases. The strongest defensible conclusion is that the particular coordinated expression pattern across bone and breast appears insufficiently characterized by the supplied reference resources and requires independent replication, tissue-cell deconvolution, and experimental or orthogonal network validation before being considered a novel mechanism.

**Hypothesis.** Hypothesis: the module marks a shared intracellular state involving transcriptional and RNA-processing control, cell-cycle or microtubule organization, and ciliary or WNT-related developmental signaling in a breast- and bone-relevant cellular context. FOXK1 could provide transcriptional and metabolic regulation, CTDSPL2 could connect transcriptional control with BMP and skeletal-development programs, WDR33 could reflect RNA maturation, and TMEM237 together with ZNF207 could couple ciliary or membrane organization to microtubule and mitotic processes. This model is explicitly provisional: the absence of globally significant enrichment, STRING support, and hu.MAP support means the co-abundance pattern could instead reflect a shared cell state or composition effect.

### Important genes

#### FOXK1

- **Related proteins** (co-abundance neighbors): CTDSPL2 (0.83), TMEM237 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: forkhead box K1. Enables 14-3-3 protein binding activity; DNA-binding transcription repressor activity, RNA polymerase II-specific; and transcription cis-regulatory region binding activity. Involved in several processes, including cellular glucose homeostasis; negative regulation of autophagy; and regulation of transcription, DNA-templated. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resource…
- **Diseases (Open Targets)**: neurodegenerative disease (0.520); Abnormality of the skeletal system (0.456); hypothyroidism (0.393); Parkinson disease (0.374); autoimmune disorder of central nervous system (0.370)
- **Europe PMC papers**: 1745
- **Why important**: FOXK1 is a central connector in the module, linking CTDSPL2 and TMEM237. Its established annotations include RNA polymerase II transcriptional repression, DNA-templated transcription, intracellular glucose homeostasis, and negative regulation of autophagy. It has the largest literature volume among the module genes and has Open Targets associations with skeletal-system abnormality and several neurological or autoimmune conditions.
- **Conclusion**: Established evidence supports FOXK1 as the most plausible regulatory hub and a candidate coordinator of transcriptional and metabolic cell state. It is a mechanistic candidate, not a proven driver of the bone–breast module; its hub position is based on co-abundance topology rather than demonstrated physical interactions.

#### CTDSPL2

- **Related proteins** (co-abundance neighbors): FOXK1 (0.83), WDR33 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CTD small phosphatase like 2. Enables RNA polymerase II CTD heptapeptide repeat phosphatase activity. Predicted to act upstream of or within negative regulation of BMP signaling pathway; positive regulation of protein export from nucleus; and protein dephosphorylation. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.482); neoplasm (0.084); acute myeloid leukemia (0.078); non-small cell lung carcinoma (0.077); osteosarcoma (0.074)
- **Europe PMC papers**: 210
- **Why important**: CTDSPL2 connects FOXK1 and WDR33 and encodes a protein with RNA polymerase II CTD phosphatase activity. Its annotations include transcriptional regulation, protein dephosphorylation, BMP-related regulation, cartilage development, bone development, and growth-plate chondrocyte growth. These links make it especially relevant to the bone component and to a transcriptional mechanism.
- **Conclusion**: Established annotations make CTDSPL2 a strong candidate for linking transcriptional control with skeletal and developmental biology. The bone-related interpretation remains a hypothesis because no enrichment term passed global correction and no direct module-specific interaction was established.

#### TMEM237

- **Related proteins** (co-abundance neighbors): ZNF207 (0.87), FOXK1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Nuclear speckles, Plasma membrane, Microtubules, Primary cilium; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transmembrane protein 237. The protein encoded by this gene is a tetraspanin protein that is thought to be involved in WNT signaling. Defects in this gene are a cause of Joubert syndrome-14. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: Joubert syndrome 14 (0.775); Joubert syndrome (0.772); Joubert syndrome with oculorenal defect (0.619); Joubert syndrome and related disorders (0.455); Meckel syndrome (0.439)
- **Europe PMC papers**: 315
- **Why important**: TMEM237 is a network connector linked to FOXK1 and ZNF207. It is annotated as a tetraspanin-like transmembrane protein associated with WNT signaling, cilium assembly, ciliary transition-zone localization, and riboflavin transport. It is tissue enriched in retina and cell-type enhanced in basal keratinocytes, breast myoepithelial cells, and rod photoreceptors. It also has established disease associations with Joubert syndrome and related ciliopathies.
- **Conclusion**: Established evidence supports TMEM237 as the module member most suggestive of ciliary and WNT-related biology. Its breast and developmental relevance is plausible, but the module does not establish that TMEM237 mediates the shared bone–breast signal or physically interacts with its network neighbors.

#### WDR33

- **Related proteins** (co-abundance neighbors): CTDSPL2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 33. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.515); dengue disease (0.370); smoking initiation (0.292); connective tissue disorder (0.236); arthropathy (0.149)
- **Europe PMC papers**: 508
- **Why important**: WDR33 is a terminal module member connected to CTDSPL2 and is annotated for mRNA three-prime-end processing, DNA-damage tolerance, and spermatogenesis. As a WD-repeat protein, it may participate in multiprotein assemblies, although no hu.MAP complex involving another module member is reported. It has a substantial literature record and Open Targets associations including connective-tissue disorder and arthropathy.
- **Conclusion**: Established evidence supports WDR33 as an RNA-processing component that could reflect a broad nuclear regulatory state. Its role in this module is currently inferential; the network and annotations do not demonstrate a specific bone–breast mechanism.

#### ZNF207

- **Related proteins** (co-abundance neighbors): TMEM237 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger protein 207. Enables microtubule binding activity. Involved in several processes, including mitotic nuclear division; mitotic spindle assembly checkpoint signaling; and protein stabilization. Located in kinetochore; nuclear lumen; and spindle matrix. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.565); Alzheimer disease (0.463); lysosomal storage disease (0.462); Parkinson disease (0.462); rectosigmoid junction neoplasm (0.148)
- **Europe PMC papers**: 409
- **Why important**: ZNF207 is connected to TMEM237 and is annotated for microtubule binding, mitotic spindle assembly checkpoint signaling, kinetochore attachment, microtubule polymerization, and sister-chromatid segregation. Its localization and functions provide a plausible cell-division and cytoskeletal complement to the ciliary and transcriptional annotations of other members.
- **Conclusion**: Established evidence supports ZNF207 as a candidate indicator of mitotic and microtubule organization. Its contribution to the module is a hypothesis based on topology and annotation; no direct interaction with TMEM237 is supported by the supplied STRING or hu.MAP results.

## Module 7

**Tissue pair**: bone and breast  
**Genes (10)**: DNM2, GFPT1, HARS1, AK6, RPS6KA1, METTL2B, PPIL3, SMS, TATDN1, TTI1

### Function

This module does not have a globally significant GO or KEGG enrichment term; no GO or KEGG term passed global correction. Its gene annotations nevertheless point to a broadly cellular program rather than a single specialized pathway. METTL2B is a highly connected co-abundance hub associated with tRNA methylation and tRNA metabolism. The peripheral genes span TOR signaling and protein stabilization through TTI1, hexosamine-pathway flux through GFPT1, MAPK-linked phosphorylation and growth regulation through RPS6KA1, translation through HARS1, vesicle trafficking and endocytosis through DNM2, nucleotide interconversion through AK6, polyamine synthesis through SMS, and protein folding or splicing through PPIL3. The star-like topology and the absence of STRING functional enrichment argue against assigning this module to one established biological pathway. The most defensible interpretation is a METTL2B-centered co-abundance pattern involving general biosynthetic, signaling, proteostatic, and trafficking processes.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. All genes have low tissue specificity and low immune-cell specificity, with no frequent enriched blood-cell category. Single-cell annotations are scattered across neutrophils, goblet cells, germ-cell populations, choroid-plexus epithelial cells, cardiomyocytes, and other cell types rather than concentrated in one shared lineage. Thus, the module does not strongly resemble a blood-contamination or blood-cell module. Its broad tissue distribution is more consistent with generally expressed intracellular biology, although shared cellular composition or common regulatory states in bone and breast samples cannot be excluded. Protein detection is reported for most genes in breast, while bone has no matching HPA tissue result; this asymmetry limits tissue-specific interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction is reported among the module genes at the specified high-confidence threshold, and STRING provides no supplementary functional enrichment. Therefore, the co-abundance edges should not be interpreted as established direct physical interactions. huMAP identifies one complex, C1, containing TTI1 and DNM2 among a much larger set of proteins. This provides limited evidence that these two genes can occur in a shared complex context, but the broad membership and sparse overlap with the module make it insufficient to explain the whole module. Overall, the network is primarily a co-abundance association rather than a reconstruction of a known protein complex.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11232.1 (TTI1, DNM2; 2/78)

### Novelty

The exact bone–breast co-abundance module appears to be a candidate novel systems-level observation because it is not represented by a coherent high-confidence STRING network, has no STRING enrichment, and has only a limited huMAP overlap. However, these database absences do not establish molecular novelty. The genes are individually well characterized, and the star-like structure may reflect shared regulation, common cellular state, technical covariance, or an indirect relationship centered on METTL2B. Accordingly, the appropriate claim is a potentially novel cross-tissue co-abundance pattern that requires replication and experimental validation, not a newly discovered physical pathway.

**Hypothesis.** Hypothesis: a shared intracellular state in bone and breast coordinately increases METTL2B-associated RNA modification and translation capacity while coupling it to TOR regulation, hexosamine metabolism, kinase signaling, protein folding, polyamine metabolism, and membrane trafficking. Within this model, DNM2 could connect the state to endocytosis and osteoclast-related membrane remodeling, while TTI1 could connect it to TOR complexes. This is a mechanistic hypothesis rather than an established pathway: the weakly connected network, lack of globally enriched GO or KEGG terms, and absence of STRING interactions mean that the observed edges may represent indirect or sample-level co-regulation.

### Important genes

#### METTL2B

- **Related proteins** (co-abundance neighbors): TATDN1 (0.88), TTI1 (0.86), GFPT1 (0.84), RPS6KA1 (0.84), HARS1 (0.84), DNM2 (0.83), AK6 (0.81), SMS (0.80), PPIL3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methyltransferase 2B, tRNA N3-cytidine. This gene is a member of a family of methyltransferases that share homology with, but are distinct from, the UbiE family of methyltransferases. Alternatively spliced variants which encode different protein isoforms have been described; however, not all variants have been fully characterized. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: osteoarthritis (0.118); ventricular septal defect (0.104); self-injurious ideation (0.067); Precordial pain (0.051); systemic sclerosis (0.034)
- **Europe PMC papers**: 161
- **Why important**: METTL2B is the central network hub, connected to every other module member, and encodes a tRNA methyltransferase involved in tRNA metabolism and tRNA methylation. Its broad tissue and cell-type profile is compatible with a general intracellular program rather than a lineage-restricted signal. Its disease links include osteoarthritis and other conditions, and it has an established but comparatively modest literature base.
- **Conclusion**: Established evidence supports METTL2B as the network anchor and as a regulator of tRNA modification. The hypothesis that it organizes the cross-tissue module is plausible from network position but is not demonstrated as a direct molecular interaction.

#### TTI1

- **Related proteins** (co-abundance neighbors): METTL2B (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_11232.1
- **Function (MyGene.info)**: TELO2 interacting protein 1. Involved in regulation of TOR signaling. Located in cytoplasm. Part of TORC1 complex and TORC2 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly and movement abnormalities (0.625); Severe intellectual disability (0.407); neurodevelopmental disorder (0.298); Abnormal brain morphology (0.266); neurodegenerative disease (0.248)
- **Europe PMC papers**: 511
- **Why important**: TTI1 is linked to METTL2B in the module and is the only gene besides DNM2 represented with another module member in huMAP complex C1. It participates in TORC1 and TORC2, TOR signaling regulation, protein stabilization, and DNA-damage checkpoint regulation. Its disease associations include neurodevelopmental and neurodegenerative conditions, and it has a substantial literature base.
- **Conclusion**: Established evidence supports TTI1 as a TOR-associated regulatory and protein-stability factor and supports a limited complex relationship through C1. Its proposed role in coupling the module to nutrient sensing or growth signaling remains a hypothesis.

#### DNM2

- **Related proteins** (co-abundance neighbors): METTL2B (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_11232.1
- **Function (MyGene.info)**: dynamin 2. Dynamins represent one of the subfamilies of GTP-binding proteins. These proteins share considerable sequence similarity over the N-terminal portion of the molecule, which contains the GTPase domain. Dynamins are associated with microtubules. They have been implicated in cell processes such as endocytosis and cell motility, and in alterations of the membrane that accompany certain activities such …
- **Diseases (Open Targets)**: autosomal dominant centronuclear myopathy (0.844); Charcot-Marie-Tooth disease dominant intermediate B (0.830); fetal akinesia-cerebral and retinal hemorrhage syndrome (0.739); autosomal dominant Charcot-Marie-Tooth disease type 2M (0.715); centronuclear myopathy (0.692)
- **Europe PMC papers**: 2412
- **Why important**: DNM2 is connected to the central METTL2B hub and is the second module member represented in huMAP complex C1. It has extensive functional annotation for endocytosis, post-Golgi vesicle transport, autophagy, and cell motility, with explicit relevance to membrane remodeling during bone resorption. It has strong disease relevance, including neuromuscular disorders, and a large literature base.
- **Conclusion**: Established evidence supports DNM2 as a membrane-trafficking and cytoskeletal regulator with a plausible connection to bone-cell biology. Its participation in a shared METTL2B-centered program in bone and breast is not established and should be tested experimentally.

#### GFPT1

- **Related proteins** (co-abundance neighbors): METTL2B (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamine--fructose-6-phosphate transaminase 1. This gene encodes the first and rate-limiting enzyme of the hexosamine pathway and controls the flux of glucose into the hexosamine pathway. The product of this gene catalyzes the formation of glucosamine 6-phosphate. [provided by RefSeq, Sep 2008].
- **Diseases (Open Targets)**: congenital myasthenic syndrome (0.819); neurodegenerative disease (0.559); congenital myasthenic syndromes with glycosylation defect (0.503); spinal stenosis (0.379); congenital disorder of glycosylation type I (0.370)
- **Europe PMC papers**: 1684
- **Why important**: GFPT1 is connected to METTL2B and encodes the rate-limiting enzyme of the hexosamine pathway, controlling glucose entry into glucosamine metabolism and UDP-N-acetylglucosamine biosynthesis. It has disease associations involving congenital myasthenic and glycosylation disorders, as well as spinal stenosis, and it has an extensive literature base. Its goblet-cell annotation is isolated rather than evidence of a shared tissue-specific identity.
- **Conclusion**: Established evidence supports GFPT1 as a metabolic control point for hexosamine flux and glycosylation-related biology. Its proposed role as a metabolic arm of this module is biologically plausible but remains an inference from annotation and co-abundance.

#### RPS6KA1

- **Related proteins** (co-abundance neighbors): METTL2B (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein S6 kinase A1. This gene encodes a member of the RSK (ribosomal S6 kinase) family of serine/threonine kinases. This kinase contains 2 nonidentical kinase catalytic domains and phosphorylates various substrates, including members of the mitogen-activated kinase (MAPK) signalling pathway. The activity of this protein has been implicated in controlling cell growth and differentiation. Alternate transcriptional spli…
- **Diseases (Open Targets)**: neurodegenerative disease (0.490); hypothyroidism (0.392); bone disorder (0.306); type 2 diabetes mellitus (0.256); response to statin (0.205)
- **Europe PMC papers**: 1449
- **Why important**: RPS6KA1 is connected to METTL2B and encodes a serine-threonine kinase with roles in MAPK-linked phosphorylation, signal transduction, cell growth, differentiation, and TOR-related regulation. It has disease associations including bone disorder, neurodegenerative disease, and type two diabetes, and it has an extensive literature base. Its HPA annotations span several epithelial and neural-related cell types, supporting broad rather than tissue-exclusive expression.
- **Conclusion**: Established evidence supports RPS6KA1 as a signaling and growth regulator. It could provide a regulatory bridge between the module and growth or differentiation states, but the module data do not prove that it mediates the observed cross-tissue association.
