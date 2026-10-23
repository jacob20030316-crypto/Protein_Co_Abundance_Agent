# Conserved co-abundance modules: bone and skin

## Module 0

**Tissue pair**: bone and skin  
**Genes (7)**: EIF4EBP1, BLTP3A, HNRNPH1, KRT10, KRT9, KRT2, KRT1

### Function

This module is best interpreted as an epithelial keratin intermediate-filament and cornified-envelope program. The primary evidence is the globally corrected enrichment for keratin filament, intermediate-filament organization and intermediate-filament-based processes (4 globally significant GO/KEGG terms, q_global 2.84e-05–0.000228; see the table), intermediate-filament cytoskeleton (GO:CC intermediate filament; q_global = 0.000789) (GO:CC intermediate filament cytoskeleton; q_global = 0.0027), cornified-envelope formation and peptide cross-linking (KEGG Cornified envelope formation - Homo sapiens (human); q_global = 0.00302) (GO:BP peptide cross-linking; q_global = 0.00342) (GO:CC cornified envelope; q_global = 0.00811), skin and epidermis development (GO:BP skin development; q_global = 0.0079) (GO:BP epidermis development; q_global = 0.01), and cadherin signaling (KEGG Cadherin signaling - Homo sapiens (human); q_global = 0.0162). The same four keratins, KRT1, KRT10, KRT2 and KRT9, drive nearly all of these terms. Thus, the strongest interpretation is structural reinforcement and differentiation of stratified epithelial cells, especially suprabasal keratinocytes, rather than a general bone-specific pathway. Cadherin signaling should be interpreted as supplementary context for epithelial cell adhesion, not as evidence for a separate dominant pathway.

**Cell composition.** The module is strongly dominated by skin-associated keratins rather than plasma proteins or a broad housekeeping program. KRT1, KRT2 and KRT10 are tissue-enriched in skin and cell-type enriched in suprabasal keratinocytes, while KRT9 is associated with terminally differentiated palmoplantar epidermis and has lymphoid-tissue enrichment in the HPA summary. Protein detection is present for nearly all module genes in skin, whereas bone has no matching HPA tissue result. Only KRT10 is annotated as secreted in other tissues, so this is not primarily a secreted-protein module. The HPA blood-cell annotations are mixed and mostly low or isolated cell-type signals; one gene is not detected in immune cells. Overall, the shared bone-skin signal is more plausibly related to epithelial or keratin-containing material, or to shared cell composition, than to a blood-cell or plasma-protein module. The broadly expressed genes BLTP3A and HNRNPH1, and the tissue-enhanced translation regulator EIF4EBP1, may represent contextual or regulatory components rather than the core functional identity.

**GO/KEGG enrichment**: 13 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC keratin filament | 2.84e-05 | KRT1, KRT10, KRT2, KRT9 |
| GO:BP intermediate filament organization | 4.46e-05 | KRT1, KRT10, KRT2, KRT9 |
| GO:BP intermediate filament-based process | 0.000228 | KRT1, KRT10, KRT2, KRT9 |
| GO:BP intermediate filament cytoskeleton organization | 0.000228 | KRT1, KRT10, KRT2, KRT9 |
| GO:MF structural constituent of skin epidermis | 0.000428 | KRT1, KRT10, KRT2 |
| GO:CC intermediate filament | 0.000789 | KRT1, KRT10, KRT2, KRT9 |
| GO:CC intermediate filament cytoskeleton | 0.0027 | KRT1, KRT10, KRT2, KRT9 |
| KEGG Cornified envelope formation - Homo sapiens (human) | 0.00302 | KRT1, KRT10, KRT2, KRT9 |
| GO:BP peptide cross-linking | 0.00342 | KRT1, KRT10, KRT2 |
| GO:BP skin development | 0.0079 | KRT1, KRT10, KRT2, KRT9 |
| GO:CC cornified envelope | 0.00811 | KRT1, KRT10, KRT2 |
| GO:BP epidermis development | 0.01 | KRT1, KRT10, KRT2, KRT9 |
| KEGG Cadherin signaling - Homo sapiens (human) | 0.0162 | KRT1, KRT10, KRT2, KRT9 |

### STRING and hu.MAP

STRING supports three high-confidence relationships within the keratin core: KRT1 with KRT10, KRT1 with KRT2, and KRT10 with KRT2. These known relationships reinforce the interpretation that the co-abundance signal captures a real keratin filament program, although STRING evidence is supplementary and does not replace the globally corrected GO/KEGG evidence. KRT9 has no listed STRING partner despite being connected in the co-abundance network, and BLTP3A, HNRNPH1 and EIF4EBP1 also have no listed STRING partners in this module. No hu.MAP complex contains at least two module members. Therefore, the module has a validated interaction-rich keratin core but lacks evidence for a known multi-protein complex spanning the full module. The co-abundance links involving BLTP3A, HNRNPH1 and EIF4EBP1 should not be treated as established physical interactions.

**STRING interactions (score >= 0.7)**: 3 of 21 gene pairs: KRT1–KRT10 (0.999); KRT1–KRT2 (0.956); KRT10–KRT2 (0.904)
**STRING functional enrichment (supplementary, within-query FDR)**: DISEASES Epidermolytic hyperkeratosis (FDR = 8.81e-07, 4 genes); Keyword Keratin (FDR = 3.17e-06, 4 genes); SMART Intermediate filament protein (FDR = 6.82e-06, 4 genes); Component Keratin filament (FDR = 7.28e-06, 4 genes); Keyword Intermediate filament (FDR = 7.59e-06, 4 genes); COMPARTMENTS Keratin filament (FDR = 7.82e-06, 4 genes); InterPro Intermediate filament protein, conserved site (FDR = 3.85e-05, 4 genes); InterPro Intermediate filament, rod domain (FDR = 3.85e-05, 4 genes); RCTM Formation of the cornified envelope (FDR = 3.96e-05, 4 genes); DISEASES Bullous congenital ichthyosiform erythroderma (FDR = 9.27e-05, 3 genes); DISEASES Epidermolytic palmoplantar keratoderma (FDR = 9.27e-05, 3 genes); COMPARTMENTS Cornified envelope (FDR = 0.00035, 3 genes); NetworkNeighborAL Mixed, incl. Ichthyosis vulgaris, and Bullous congenital ichthyosiform erythroderma (FDR = 0.00037, 3 genes); Keyword Ichthyosis (FDR = 0.00057, 3 genes); PMID (2025) Mass spectrometric detection of keratins in tear fluid. (FDR = 0.00073, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is not a new discovery of keratin biology: the keratin-filament, epidermal-differentiation and cornified-envelope functions are established by the primary enrichment results, the HPA localization pattern, the gene descriptions, and known disease associations. The specific conserved co-abundance module across bone and skin may still be a dataset-specific observation, particularly because its peripheral links are not represented by STRING or hu.MAP. However, absence from those resources alone cannot establish novelty. A defensible conclusion is that the module provides a potentially interesting cross-tissue co-abundance pattern built around a well-known epithelial keratin program, while any claim that the bone-skin conservation reveals a new mechanism requires independent replication, cell-composition assessment and experimental validation.

**Hypothesis.** Hypothesis: the conserved signal reflects shared abundance of keratin-rich epithelial material or epithelial-cell signatures in the bone and skin datasets, with the KRT1-KRT2-KRT10-KRT9 core representing differentiated intermediate filaments and the BLTP3A-HNRNPH1-EIF4EBP1 branch reflecting transcriptional, RNA-processing or translational context associated with the sampled cells. An alternative hypothesis is that keratin-containing material or related epithelial contamination is present in bone samples. The available evidence does not establish direct physical coupling between the keratin core and the three peripheral proteins, nor does it show that the module has a bone-specific function.

### Important genes

#### KRT1

- **Related proteins** (co-abundance neighbors): KRT2 (0.95), KRT9 (0.90), KRT10 (0.88); STRING partners: KRT10 (0.999), KRT2 (0.956)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 is a central node in the co-abundance subgraph and connects strongly to KRT2, KRT9 and KRT10. It is skin-enriched, detected in skin, and enriched in suprabasal keratinocytes. It participates in every primary GO/KEGG term listed for the module and has extensive literature support. Its disease associations include epidermolytic and palmoplantar keratoderma-related disorders, making it both a structural anchor and a clinically informative marker of epidermal fragility.
- **Conclusion**: Established evidence supports KRT1 as a core structural component of the epidermal intermediate-filament program and a major driver of the module’s functional annotation. Its central network position is consistent with, but does not by itself prove, a causal role in the cross-tissue conservation.

#### KRT2

- **Related proteins** (co-abundance neighbors): KRT1 (0.95), KRT10 (0.93), KRT9 (0.92); STRING partners: KRT1 (0.956), KRT10 (0.904)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location Intermediate filaments, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 2. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is expressed largely in the upper spinous layer of epidermal keratinocytes and mutations in this gene …
- **Diseases (Open Targets)**: superficial epidermolytic ichthyosis (0.815); exfoliative ichthyosis (0.358); Palmoplantar hyperkeratosis (0.267); hereditary disease (0.193); Vertigo (0.145)
- **Europe PMC papers**: 7459
- **Why important**: KRT2 has the strongest network position in the module and connects to KRT1, KRT10 and KRT9. It is skin-enriched and specifically associated with suprabasal keratinocytes. It appears in every primary GO/KEGG term and in the supplementary keratin and epidermolytic-disease signals. Its described role in upper spinous epidermis and its associations with bullous congenital ichthyosiform erythroderma make it an important marker of differentiated epidermal structure.
- **Conclusion**: Established evidence identifies KRT2 as a central suprabasal epidermal keratin and a strong contributor to the module’s interpretation. The module supports coordinated abundance with other keratins, but it does not establish that KRT2 initiates or controls the shared tissue signal.

#### KRT10

- **Related proteins** (co-abundance neighbors): KRT2 (0.93), KRT1 (0.88); STRING partners: KRT1 (0.999), KRT2 (0.904)
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 10. This gene encodes a member of the type I (acidic) cytokeratin family, which belongs to the superfamily of intermediate filament (IF) proteins. Keratins are heteropolymeric structural proteins which form the intermediate filament. These filaments, along with actin microfilaments and microtubules, compose the cytoskeleton of epithelial cells. Mutations in this gene are associated with epidermolytic …
- **Diseases (Open Targets)**: epidermolytic hyperkeratosis 2A, autosomal dominant (0.787); epidermolytic ichthyosis (0.772); congenital reticular ichthyosiform erythroderma (0.727); ichthyosis, annular epidermolytic 1 (0.647); annular epidermolytic ichthyosis (0.642)
- **Europe PMC papers**: 2736
- **Why important**: KRT10 is part of the high-confidence STRING-supported keratin core through its relationships with KRT1 and KRT2, and it is also connected to KRT2 in the co-abundance network. It is skin-enriched, enriched in suprabasal keratinocytes, detected in skin, and present in all primary GO/KEGG terms. Its established role in type I intermediate filaments, keratinocyte differentiation and cornification, together with its epidermolytic hyperkeratosis associations, gives it strong functional and disease relevance.
- **Conclusion**: Established evidence supports KRT10 as a differentiated epidermal intermediate-filament component that helps define the module. Its annotation as secreted in other tissues warrants caution in interpreting tissue measurements, but does not make this module primarily a secreted-protein program.

#### KRT9

- **Related proteins** (co-abundance neighbors): KRT2 (0.92), BLTP3A (0.92), KRT1 (0.90); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 9. This gene encodes the type I keratin 9, an intermediate filament chain expressed only in the terminally differentiated epidermis of palms and soles. Mutations in this gene cause epidermolytic palmoplantar keratoderma. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: epidermolytic palmoplantar keratoderma, 1 (0.828); palmoplantar keratoderma, epidermolytic (0.682); Localized epidermolytic hyperkeratosis (0.511); Palmoplantar hyperkeratosis (0.456); Palmoplantar keratoderma (0.438)
- **Europe PMC papers**: 773
- **Why important**: KRT9 is a highly connected co-abundance node linked to KRT2, KRT1 and BLTP3A. It encodes a type I keratin expressed in terminally differentiated palmoplantar epidermis and is associated with epidermolytic palmoplantar keratoderma. It contributes to most of the primary keratin and epidermal terms, while its lack of listed STRING partners contrasts with its strong co-abundance connectivity and makes it informative for evaluating dataset-specific network structure.
- **Conclusion**: Established evidence supports KRT9 as a specialized differentiated-epidermis keratin and a meaningful component of the module. Its co-abundance connection to BLTP3A is a hypothesis-generating observation rather than an established molecular interaction.

#### BLTP3A

- **Related proteins** (co-abundance neighbors): KRT9 (0.92), HNRNPH1 (0.84), EIF4EBP1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Nuclear membrane; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: bridge-like lipid transfer protein family member 3A. Enables histone deacetylase binding activity and identical protein binding activity. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: artificial cardiac pacemaker (0.340); coronary artery disorder (0.273); coronary atherosclerosis (0.261); obesity disorder (0.245); ulcerative colitis (0.235)
- **Europe PMC papers**: 24
- **Why important**: BLTP3A is a highly connected bridge between KRT9 and the HNRNPH1-EIF4EBP1 branch, despite having no primary GO/KEGG or supplementary STRING term in this module. It has low tissue specificity, a myonuclear cell-type enhancement, an immune-cell enhancement for non-classical monocytes, skin protein detection, and very limited literature compared with the keratin genes. Its annotated activities include histone-deacetylase binding and identical-protein binding, but the fact sheet provides no established link to keratin biology.
- **Conclusion**: Established evidence supports BLTP3A as a network connector with relatively weak functional annotation in this module, not as a validated keratin-pathway component. Its position motivates a hypothesis that it may capture shared cellular state or sample composition, but that interpretation requires independent replication and direct molecular testing.

## Module 1

**Tissue pair**: bone and skin  
**Genes (17)**: GOT2, ACSL3, APMAP, ATP2A2, ATP5F1A, ATP5F1B, CANX, SHMT2, GOLT1B, GPD2, HMOX2, MPDU1, PRKDC, SEC61A1, HM13, DARS2, TRAP1

### Function

This is a conserved intracellular membrane and organelle module, with primary evidence for organelle membranes and mitochondrial membranes (GO:CC organelle membrane; q_global = 0.00588)(GO:CC mitochondrial membrane; q_global = 0.0278)(GO:CC mitochondrial envelope; q_global = 0.0437). It combines mitochondrial energy production, endoplasmic-reticulum protein handling, membrane trafficking, calcium homeostasis, lipid metabolism, amino-acid and one-carbon metabolism, and cellular stress responses. ATP5F1A and ATP5F1B support oxidative phosphorylation; CANX, SEC61A1, MPDU1, and HM13 support ER translocation, glycoprotein folding, glycosylation, and membrane-protein processing; ATP2A2 supports ER or sarcoplasmic-reticulum calcium transport; and SHMT2, DARS2, GOT2, and GPD2 support mitochondrial metabolism. The globally corrected evidence is cellular-component evidence rather than proof of one specific biological process. The integrated interpretation is a membrane-organellar maintenance and energetic-support program.

**Cell composition.** The module is dominated by intracellular membrane, ER, mitochondrial, and metabolic proteins rather than plasma or secreted proteins. HPA reports no secreted genes, and immune-cell specificity is generally low, arguing against a primarily blood-cell-derived module. GPD2 is blood-cell group enriched, and several genes have neutrophil or progenitor annotations, so a limited myeloid contribution cannot be excluded. Most genes have low tissue specificity or broad tissue distribution, with recurring enrichment in liver, skeletal muscle, tongue, and heart muscle. The shared bone-skin signal may therefore reflect common cellular infrastructure or shared cell types rather than a bone-skin-specific pathway. Protein detection in skin is widespread among the module genes, whereas the supplied HPA bone record has no matching protein data, limiting direct protein-level comparison with bone.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC organelle membrane | 0.00588 | ACSL3, ATP2A2, ATP5F1A, ATP5F1B, CANX, DARS2, GOLT1B, GPD2, HM13, HMOX2, MPDU1, SEC61A1, SHMT2, TRAP1 |
| GO:CC membrane | 0.0214 | ACSL3, APMAP, ATP2A2, ATP5F1A, ATP5F1B, CANX, DARS2, GOLT1B, GOT2, GPD2, HM13, HMOX2, MPDU1, PRKDC, SEC61A1, SHMT2, TRAP1 |
| GO:CC mitochondrial membrane | 0.0278 | ACSL3, ATP5F1A, ATP5F1B, CANX, DARS2, GPD2, SHMT2, TRAP1 |
| GO:CC mitochondrial envelope | 0.0437 | ACSL3, ATP5F1A, ATP5F1B, CANX, DARS2, GPD2, SHMT2, TRAP1 |

### STRING and hu.MAP

The strongest known STRING relationships are CANX with ATP2A2 and SEC61A1, ATP5F1A with ATP5F1B, and ATP5F1A with SEC61A1. These support connections among ER calcium or folding machinery and mitochondrial energy biology, but STRING enrichment is supplementary (13 supplementary STRING terms; within-query FDR 0.0069–0.0466) and is not globally corrected evidence. hu.MAP shows recurring membrane and ER-associated complexes containing ACSL3, ATP2A2, SEC61A1, PRKDC, and HM13 (hu.MAP huMAP3_09592.1), and ATP2A2, SEC61A1, and HM13 (hu.MAP huMAP3_06247.1). ATP5F1A and ATP5F1B recur together in ATP-synthase complexes (hu.MAP huMAP3_08750.1)(hu.MAP huMAP3_09307.1)(hu.MAP huMAP3_11095.1), while TRAP1 and DARS2 occur in a mitochondrial complex (hu.MAP huMAP3_13468.1). Other complexes connect ATP2A2 with SEC61A1 (hu.MAP huMAP3_07170.1) and ACSL3 with HM13 (hu.MAP huMAP3_08167.1). Thus, parts of the module recapitulate established physical complexes, while the full cross-organelle co-abundance structure extends beyond currently represented STRING and hu.MAP relationships.

**STRING interactions (score >= 0.7)**: 4 of 136 gene pairs: ATP2A2–CANX (0.849); ATP5F1A–ATP5F1B (0.999); ATP5F1A–SEC61A1 (0.886); CANX–SEC61A1 (0.914)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Organelle membrane (FDR = 0.0069, 12 genes); COMPARTMENTS Membrane (FDR = 0.007, 14 genes); TISSUES Respiratory system (FDR = 0.0135, 11 genes); TISSUES Female reproductive gland (FDR = 0.0135, 13 genes); TISSUES Left atrium (FDR = 0.0135, 4 genes); TISSUES Right atrium (FDR = 0.0135, 4 genes); Component Organelle membrane (FDR = 0.02, 13 genes); TISSUES Lung (FDR = 0.024, 9 genes); TISSUES Left ventricle (FDR = 0.024, 4 genes); COMPARTMENTS Endoplasmic reticulum subcompartment (FDR = 0.0259, 6 genes); COMPARTMENTS Endoplasmic reticulum membrane (FDR = 0.0281, 6 genes); Keyword Membrane (FDR = 0.0285, 13 genes); Keyword Transit peptide (FDR = 0.0466, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09592.1 (ACSL3, ATP2A2, SEC61A1, PRKDC, HM13; 5/95); huMAP3_06247.1 (ATP2A2, SEC61A1, HM13; 3/65); huMAP3_08750.1 (ATP5F1B, ATP5F1A; 2/12); huMAP3_07170.1 (ATP2A2, SEC61A1; 2/14); huMAP3_08167.1 (ACSL3, HM13; 2/24); huMAP3_10473.1 (ATP2A2, ATP5F1A; 2/24); huMAP3_09307.1 (ATP5F1B, ATP5F1A; 2/35); huMAP3_11095.1 (ATP5F1B, ATP5F1A; 2/45); huMAP3_13468.1 (TRAP1, DARS2; 2/99)

### Novelty

This should not be described as a wholly new molecular complex because several relationships and substructures are already established by STRING and hu.MAP. Its potentially novel aspect is the conserved co-abundance organization linking ER protein quality control, calcium handling, mitochondrial energy production, and intermediary metabolism across bone and skin. The fact sheet does not establish whether this exact tissue-pair module has been previously reported. Absence from STRING or hu.MAP cannot prove novelty because those resources do not capture every tissue-specific co-abundance relationship. The appropriate conclusion is that this is a candidate novel systems-level association requiring comparison with published bone and skin co-expression modules and independent replication.

**Hypothesis.** Hypothesis: in bone and skin cells, coordinated expression of ER membrane insertion and quality control, calcium handling, mitochondrial ATP production, and metabolic support maintains membrane-remodeling and proteostatic demands. CANX and SEC61A1 may organize the ER arm, ATP2A2 may couple calcium homeostasis to membrane function, and ATP5F1A with ATP5F1B may provide the energetic arm. TRAP1, SHMT2, GOT2, DARS2, GPD2, and HMOX2 could buffer mitochondrial stress, redox state, amino-acid or one-carbon metabolism, and hypoxia-related demands. This is a mechanistic hypothesis; the supplied evidence does not establish directionality, cell-to-cell coordination, or physical coupling across organelles.

### Important genes

#### CANX

- **Related proteins** (co-abundance neighbors): GOLT1B (0.86), HMOX2 (0.83), ATP5F1B (0.83), HM13 (0.82), MPDU1 (0.82), SEC61A1 (0.82), DARS2 (0.82), GOT2 (0.80); STRING partners: ATP2A2 (0.849), SEC61A1 (0.914)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is the strongest network hub and connects ER-associated genes with mitochondrial and metabolic genes. It appears in every globally corrected cellular-component term (GO:CC organelle membrane; q_global = 0.00588)(GO:CC membrane; q_global = 0.0214)(GO:CC mitochondrial membrane; q_global = 0.0278)(GO:CC mitochondrial envelope; q_global = 0.0437), has STRING relationships with ATP2A2 and SEC61A1, and is an ER calcium-binding chaperone involved in protein folding and ER quality control. Its skin detection and substantial literature support make it an informative module anchor.
- **Conclusion**: Established evidence supports CANX as an ER proteostasis and membrane-quality-control component linking several module neighborhoods. It is a strong marker of the ER arm. Coordination between CANX and mitochondrial energetic state in bone and skin remains hypothetical.

#### ATP2A2

- **Related proteins** (co-abundance neighbors): APMAP (0.85), TRAP1 (0.83), GOLT1B (0.82); STRING partners: CANX (0.849)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_09592.1, huMAP3_06247.1, huMAP3_07170.1, huMAP3_10473.1
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darie…
- **Diseases (Open Targets)**: Darier disease (0.823); acrokeratosis verruciformis (0.663); neurodegenerative disease (0.507); hereditary disease (0.416); schizophrenia (0.406)
- **Europe PMC papers**: 9327
- **Why important**: ATP2A2 connects several module neighbors and appears in the organelle-membrane and membrane terms (GO:CC organelle membrane; q_global = 0.00588)(GO:CC membrane; q_global = 0.0214). It has STRING support with CANX and occurs in multiple hu.MAP membrane or ER complexes (hu.MAP huMAP3_09592.1)(hu.MAP huMAP3_06247.1)(hu.MAP huMAP3_07170.1)(hu.MAP huMAP3_10473.1). Its SERCA calcium-pump function is directly relevant to ER or sarcoplasmic-reticulum physiology, and its association with Darier disease gives it a strong skin-disease connection.
- **Conclusion**: Established evidence identifies ATP2A2 as a calcium-homeostasis and membrane-function component with a direct skin-disease association. Its network position supports a bridging role between ER machinery and broader membrane metabolism. A bone-skin-specific calcium mechanism remains hypothetical.

#### ATP5F1A

- **Related proteins** (co-abundance neighbors): ATP5F1B (0.92), GOT2 (0.80); STRING partners: ATP5F1B (0.999), SEC61A1 (0.886)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_08750.1, huMAP3_10473.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit alpha. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, using an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic po…
- **Diseases (Open Targets)**: mitochondrial complex V (ATP synthase) deficiency, nuclear type 4A (0.655); mitochondrial proton-transporting ATP synthase complex deficiency (0.648); mitochondrial complex V (ATP synthase) deficiency, nuclear type 4B (0.532); hereditary disease (0.394); Mitochondrial encephalopathy (0.371)
- **Europe PMC papers**: 822
- **Why important**: ATP5F1A is a mitochondrial ATP-synthase subunit present in every globally corrected term (GO:CC organelle membrane; q_global = 0.00588)(GO:CC membrane; q_global = 0.0214)(GO:CC mitochondrial membrane; q_global = 0.0278)(GO:CC mitochondrial envelope; q_global = 0.0437). It is linked in STRING to ATP5F1B and SEC61A1 and recurs with ATP5F1B in several hu.MAP ATP-synthase complexes (hu.MAP huMAP3_08750.1)(hu.MAP huMAP3_10473.1)(hu.MAP huMAP3_09307.1)(hu.MAP huMAP3_11095.1). Its established role in proton-motive-force-driven ATP synthesis provides the clearest energetic interpretation of the module.
- **Conclusion**: Established evidence supports ATP5F1A as a central mitochondrial energy-production component and part of a known ATP-synthase complex. Its connection to SEC61A1 supports module-level coupling but does not prove direct ER-mitochondrial regulation. Supplying energy for membrane proteostasis is a hypothesis.

#### ATP5F1B

- **Related proteins** (co-abundance neighbors): ATP5F1A (0.92), GOT2 (0.83), CANX (0.83); STRING partners: ATP5F1A (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_08750.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit beta. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: hypermetabolism due to uncoupled mitochondrial oxidative phosphorylation 2 (0.499); hypertrophic cardiomyopathy (0.212); Alzheimer disease (0.177); hypertensive disorder (0.117); response to xenobiotic stimulus (0.117)
- **Europe PMC papers**: 735
- **Why important**: ATP5F1B is the complementary catalytic ATP-synthase subunit to ATP5F1A, has strong network support from that pair, and appears in every globally corrected term (GO:CC organelle membrane; q_global = 0.00588)(GO:CC membrane; q_global = 0.0214)(GO:CC mitochondrial membrane; q_global = 0.0278)(GO:CC mitochondrial envelope; q_global = 0.0437). It has the strongest STRING relationship in the module with ATP5F1A and recurs in several hu.MAP ATP-synthase complexes (hu.MAP huMAP3_08750.1)(hu.MAP huMAP3_09307.1)(hu.MAP huMAP3_11095.1). Its skeletal-muscle and tongue enhancement and skin detection are consistent with energetic demand, without proving tissue specificity.
- **Conclusion**: Established evidence supports ATP5F1B as a core oxidative-phosphorylation component and energetic marker. Its importance is strongest as part of the ATP5F1A-containing complex rather than as an isolated regulator. Coordination of energy supply with ER function remains hypothetical.

#### SEC61A1

- **Related proteins** (co-abundance neighbors): CANX (0.82); STRING partners: ATP5F1A (0.886), CANX (0.914)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09592.1, huMAP3_06247.1, huMAP3_07170.1
- **Function (MyGene.info)**: SEC61 translocon subunit alpha 1. The protein encoded by this gene belongs to the SECY/SEC61- alpha family. It appears to play a crucial role in the insertion of secretory and membrane polypeptides into the endoplasmic reticulum. This protein found to be tightly associated with membrane-bound ribosomes, either directly or through adaptor proteins. This gene encodes an alpha subunit of the heteromeric SEC61 complex, which also cont…
- **Diseases (Open Targets)**: hyperuricemic nephropathy, familial juvenile type 4 (0.720); immunodeficiency, common variable, 15 (0.529); familial juvenile hyperuricemic nephropathy type 2 (0.515); SEC61A1 deficiency (0.509); severe congenital neutropenia (0.418)
- **Europe PMC papers**: 859
- **Why important**: SEC61A1 is an ER translocon component appearing in the organelle-membrane and membrane terms (GO:CC organelle membrane; q_global = 0.00588)(GO:CC membrane; q_global = 0.0214). It has STRING relationships with CANX and ATP5F1A and recurs in several hu.MAP membrane or ER complexes (hu.MAP huMAP3_09592.1)(hu.MAP huMAP3_06247.1)(hu.MAP huMAP3_07170.1). Its established role in cotranslational insertion and ER organization makes it a mechanistically informative bridge between protein biogenesis and membrane architecture.
- **Conclusion**: Established evidence supports SEC61A1 as the module's principal entry point for secretory and membrane-protein biogenesis. Its association with CANX supports an ER quality-control substructure, while its association with ATP5F1A indicates coordinated co-abundance rather than necessarily direct physical interaction. Functional ER-to-mitochondrial coordination remains hypothetical.

#### SHMT2

- **Related proteins** (co-abundance neighbors): DARS2 (0.82), PRKDC (0.80), TRAP1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine hydroxymethyltransferase 2. This gene encodes the mitochondrial form of a pyridoxal phosphate-dependent enzyme that catalyzes the reversible reaction of serine and tetrahydrofolate to glycine and 5,10-methylene tetrahydrofolate. The encoded product is primarily responsible for glycine synthesis. The activity of the encoded protein has been suggested to be the primary source of intracellular glycine. The gene which encodes th…
- **Diseases (Open Targets)**: neurodevelopmental disorder with cardiomyopathy, spasticity, and brain abnormalities (0.771); microcephaly (0.370); polymicrogyria (0.370); neurodevelopmental disorder (0.336); hereditary disease (0.192)
- **Europe PMC papers**: 2579
- **Why important**: SHMT2 appears in every globally corrected cellular-component term (GO:CC organelle membrane; q_global = 0.00588)(GO:CC membrane; q_global = 0.0214)(GO:CC mitochondrial membrane; q_global = 0.0278)(GO:CC mitochondrial envelope; q_global = 0.0437), connects to DARS2, PRKDC, and TRAP1, and is a mitochondrial enzyme involved in serine, glycine, and one-carbon metabolism. It also recurs in supplementary STRING organelle-membrane and tissue results (STRING COMPARTMENTS Organelle membrane; within-query FDR = 0.0069)(STRING COMPARTMENTS Membrane; within-query FDR = 0.007)(STRING TISSUES Respiratory system; within-query FDR = 0.0135)(STRING TISSUES Female reproductive gland; within-query FDR = 0.0135)(STRING Component Organelle membrane; within-query FDR = 0.02)(STRING TISSUES Lung; within-query FDR = 0.024)(STRING Keyword Membrane; within-query FDR = 0.0285)(STRING Keyword Transit peptide; within-query FDR = 0.0466). Its disease associations and substantial literature make it a strong candidate for linking mitochondrial metabolism with biosynthetic and stress requirements.
- **Conclusion**: Established evidence supports SHMT2 as a mitochondrial metabolic and one-carbon pathway component that may explain co-abundance of metabolic and organelle genes. The data do not establish that SHMT2 controls the module or that metabolic flux is altered in bone or skin. Its role as a metabolic support node is therefore hypothetical.

## Module 2

**Tissue pair**: bone and skin  
**Genes (31)**: ABHD10, ABLIM1, ACOT1, ATXN2, BOLA3, BRD2, DHRS4, EPS15L1, FDFT1, FMC1, GNA13, IKBIP, KGD4, L2HGDH, LDLR, LYRM4, MED12, ALDH6A1, NME3, BCKDHA, PON2, MRPL4, MRPL10, POLRMT, MRPS11, MRPS15, SAP30BP, SYNGR1, IARS2, YARS2, WFS1

### Function

The module is best interpreted as a mitochondrial maintenance and bioenergetics module. Primary enrichment supports mitochondrial localization through the mitochondrial matrix and mitochondrion terms (GO:CC mitochondrial matrix; q_global = 0.00553) (GO:CC mitochondrion; q_global = 0.0132), and supports mitochondrial gene expression and mitochondrial translation (GO:BP mitochondrial gene expression; q_global = 0.0293) (GO:BP mitochondrial translation; q_global = 0.0495). The gene composition connects mitochondrial transcription, mitochondrial translation, aminoacyl-tRNA charging, iron-sulfur cluster assembly, branched-chain amino-acid catabolism, the tricarboxylic-acid cycle, lipid metabolism, and ATP-synthase assembly. Thus, the most defensible function is coordinated support of mitochondrial gene expression and respiratory metabolism, rather than a tissue-specific bone or skin pathway. The STRING enrichment independently supports mitochondrial matrix and mitochondrial localization (6 supplementary STRING terms; within-query FDR 0.0014–0.0183), while the GO/KEGG terms are the primary globally corrected evidence.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the HPA summary identifies only a small minority of secreted genes, with PON2 specifically reported as secreted to blood. Most genes have low tissue specificity, and many are cell-type enhanced rather than restricted to bone or skin. HPA also reports several cell-type associations involving esophageal cells, neutrophils, trophoblasts, parietal cells, and spermatocytes, with immune-cell specificity generally low but a minority of immune-enhanced or immune-enriched genes. Therefore, the shared signal could partly reflect broadly distributed mitochondrial activity or shared cell populations, and should not automatically be assigned to osteoblasts or keratinocytes. The strong mitochondrial enrichment and the broad intracellular localization argue against interpreting the module primarily as blood plasma contamination. Protein detection is widespread in skin, whereas the supplied HPA bone tissue result has no matching tissue assessment.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrial matrix | 0.00553 | ABHD10, ALDH6A1, BCKDHA, BOLA3, IARS2, LYRM4, MRPL10, MRPL4, MRPS11, MRPS15, POLRMT, YARS2 |
| GO:CC mitochondrion | 0.0132 | ABHD10, ACOT1, ALDH6A1, BCKDHA, BOLA3, DHRS4, FMC1, IARS2, KGD4, L2HGDH, LYRM4, MRPL10, MRPL4, MRPS11, MRPS15, NME3, POLRMT, YARS2 |
| GO:BP mitochondrial gene expression | 0.0293 | IARS2, MRPL10, MRPL4, MRPS11, MRPS15, POLRMT, YARS2 |
| GO:BP mitochondrial translation | 0.0495 | IARS2, MRPL10, MRPL4, MRPS11, MRPS15, YARS2 |

### STRING and hu.MAP

STRING provides a coherent but incomplete known-interaction backbone. The strongest known links connect mitochondrial ribosomal proteins MRPL10, MRPL4, MRPS11, and MRPS15, and connect the mitochondrial aminoacyl-tRNA synthetases IARS2 and YARS2. STRING also links BOLA3 with LYRM4, consistent with iron-sulfur cluster biology. These relationships support the mitochondrial interpretation, but most co-abundance edges are not represented as high-confidence STRING physical or functional interactions. hu.MAP independently places MRPL10, MRPL4, and YARS2 together in several mitochondrial RNA-processing or mitoribosomal assemblies (hu.MAP huMAP3_06550.1) (hu.MAP huMAP3_07939.1) (hu.MAP huMAP3_08458.1) (hu.MAP huMAP3_09113.1) (hu.MAP huMAP3_09483.1) (hu.MAP huMAP3_06589.1), places BCKDHA and KGD4 in a metabolic complex (hu.MAP huMAP3_12248.1), and places MRPS11 and MRPS15 in mitochondrial small-subunit complexes (hu.MAP huMAP3_05954.1) and (hu.MAP huMAP3_05807.1). The repeated hu.MAP membership is evidence that parts of the module recapitulate known complexes, while the partial overlap and many isolated module genes indicate that the co-abundance module is broader than a single established complex.

**STRING interactions (score >= 0.7)**: 8 of 465 gene pairs: BOLA3–LYRM4 (0.849); IARS2–YARS2 (0.919); MRPL10–MRPL4 (0.996); MRPL10–MRPS11 (0.973); MRPL10–MRPS15 (0.978); MRPL4–MRPS11 (0.997); MRPL4–MRPS15 (0.998); MRPS11–MRPS15 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Mitochondrial matrix (FDR = 0.0014, 12 genes); Keyword Mitochondrion (FDR = 0.0081, 14 genes); COMPARTMENTS Mitochondrion (FDR = 0.0099, 15 genes); Component Mitochondrion (FDR = 0.0115, 16 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.0127, 10 genes); Keyword Transit peptide (FDR = 0.0183, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06550.1 (MRPL10, MRPL4, YARS2; 3/62); huMAP3_07939.1 (MRPL10, MRPL4, YARS2; 3/68); huMAP3_08458.1 (MRPL10, MRPL4, YARS2; 3/70); huMAP3_09113.1 (MRPL10, MRPL4, YARS2; 3/72); huMAP3_09483.1 (MRPL10, MRPL4, YARS2; 3/74); huMAP3_06589.1 (MRPL10, MRPL4, YARS2; 3/79); huMAP3_12248.1 (BCKDHA, KGD4; 2/22); huMAP3_05954.1 (MRPS11, MRPS15; 2/28); huMAP3_04652.1 (MRPL4, YARS2; 2/30); huMAP3_06439.1 (MRPL10, MRPL4; 2/57); huMAP3_05807.1 (MRPS11, MRPS15; 2/81)

### Novelty

The mitochondrial theme itself is not a new biological finding: it is supported by globally corrected GO evidence, STRING annotations, and multiple hu.MAP complexes. The specific cross-tissue co-abundance module may nevertheless be a useful systems-level observation because it combines mitoribosomal, mitochondrial transcription, iron-sulfur, amino-acid catabolic, lipid, and signaling genes across bone and skin. However, the supplied evidence does not establish that this exact module or its cross-tissue conservation is novel. Partial absence from STRING or hu.MAP cannot prove novelty, because those resources emphasize curated or experimentally supported relationships and do not directly test this co-abundance structure. Novelty should therefore be described as an open empirical question requiring replication, tissue-cell deconvolution, and comparison with previously published co-expression modules.

**Hypothesis.** Hypothesis: the shared bone–skin module reflects a conserved mitochondrial quality and energy-maintenance program that coordinates mitochondrial transcription and translation with respiratory-chain assembly, iron-sulfur cluster maturation, amino-acid oxidation, and lipid handling. In both tissues, cells experiencing comparable energetic, differentiation, or stress demands may co-regulate these genes. The peripheral links involving GNA13, SYNGR1, IKBIP, LDLR, and endocytic or membrane-associated proteins could represent coupling of mitochondrial state to signaling, vesicle trafficking, or cell-state composition, but this coupling is presently a hypothesis rather than an established pathway. Testing should examine cell-resolved expression, mitochondrial content, respiratory function, and whether the module persists after adjustment for shared cell types.

### Important genes

#### POLRMT

- **Related proteins** (co-abundance neighbors): MED12 (0.86), LDLR (0.85), WFS1 (0.84), BRD2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase mitochondrial. This gene encodes a mitochondrial DNA-directed RNA polymerase. The gene product is responsible for mitochondrial gene expression as well as for providing RNA primers for initiation of replication of the mitochondrial genome. Although this polypeptide has the same function as the three nuclear DNA-directed RNA polymerases, it is more closely related to RNA polymerases of phage and mitochondrial pol…
- **Diseases (Open Targets)**: combined oxidative phosphorylation deficiency 55 (0.798); neurodegenerative disease (0.470); neurodevelopmental disorder (0.340); substance-related disorder (0.221); mitochondrial DNA depletion syndrome 4a (0.118)
- **Europe PMC papers**: 1149
- **Why important**: POLRMT is a network-connected mitochondrial gene-expression component and is included in the primary terms for mitochondrial matrix, mitochondrion, and mitochondrial gene expression (GO:CC mitochondrial matrix; q_global = 0.00553) (GO:CC mitochondrion; q_global = 0.0132) (GO:BP mitochondrial gene expression; q_global = 0.0293). Its annotation identifies it as the mitochondrial DNA-directed RNA polymerase responsible for mitochondrial transcription and RNA primers for mitochondrial genome replication. It also has a mitochondrial disease association and more substantial literature support than many less characterized module members.
- **Conclusion**: Established evidence supports POLRMT as a functional anchor for mitochondrial gene expression within the module. Its co-abundance with nuclear transcriptional and signaling genes does not establish direct regulation or a bone–skin-specific role; those connections remain hypotheses.

#### MRPL10

- **Related proteins** (co-abundance neighbors): LDLR (0.85), BOLA3 (0.84), MRPS11 (0.82); STRING partners: MRPL4 (0.996), MRPS11 (0.973), MRPS15 (0.978)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_06550.1, huMAP3_07939.1, huMAP3_08458.1, huMAP3_09113.1, huMAP3_09483.1, huMAP3_06589.1, huMAP3_06439.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein L10. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.532); Alzheimer disease (0.270); Parkinson disease (0.268); lysosomal storage disease (0.268); atrial fibrillation (0.079)
- **Europe PMC papers**: 327
- **Why important**: MRPL10 is one of the most connected mitochondrial genes in the module and participates in all primary enrichment terms (4 globally significant GO/KEGG terms, q_global 0.00553–0.0495; see the table). It has strong STRING links to MRPL4, MRPS11, and MRPS15 and appears in many hu.MAP complexes (hu.MAP huMAP3_06550.1) (hu.MAP huMAP3_07939.1) (hu.MAP huMAP3_08458.1) (hu.MAP huMAP3_09113.1) (hu.MAP huMAP3_09483.1) (hu.MAP huMAP3_06589.1) and (hu.MAP huMAP3_06439.1). Its established function as a mitochondrial large-subunit ribosomal protein makes it a central structural marker of the mitochondrial translation component.
- **Conclusion**: Established evidence strongly supports MRPL10 as a mitoribosomal hub underlying the module’s mitochondrial translation signal. Its network prominence reflects both known complex biology and co-abundance; it should not be treated as proof that MRPL10 drives the entire module.

#### MRPL4

- **Related proteins** (co-abundance neighbors): BOLA3 (0.91); STRING partners: MRPL10 (0.996), MRPS11 (0.997), MRPS15 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_06550.1, huMAP3_07939.1, huMAP3_08458.1, huMAP3_09113.1, huMAP3_09483.1, huMAP3_06589.1, huMAP3_04652.1, huMAP3_06439.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein L4. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.484); lymphatic system disorder (0.275); aortic stenosis (0.056); allergic rhinitis (0.043); gastric cancer (0.020)
- **Europe PMC papers**: 350
- **Why important**: MRPL4 is directly connected in STRING to several mitochondrial ribosomal proteins and appears repeatedly in hu.MAP mitochondrial complexes (hu.MAP huMAP3_06550.1) (hu.MAP huMAP3_07939.1) (hu.MAP huMAP3_08458.1) (hu.MAP huMAP3_09113.1) (hu.MAP huMAP3_09483.1) (hu.MAP huMAP3_06589.1) (hu.MAP huMAP3_04652.1) (hu.MAP huMAP3_06439.1). It is included in every primary enrichment category (4 globally significant GO/KEGG terms, q_global 0.00553–0.0495; see the table) and is annotated as a mitochondrial ribosomal protein involved in translation. Its disease associations provide additional biological relevance, although they do not specifically implicate the bone–skin module.
- **Conclusion**: Established evidence identifies MRPL4 as a core component of the module’s mitoribosomal signal. A hypothesis that variation in MRPL4 contributes to tissue energetic adaptation would require functional and cell-specific testing.

#### BOLA3

- **Related proteins** (co-abundance neighbors): MRPL4 (0.91), MRPS11 (0.84), MRPL10 (0.84); STRING partners: LYRM4 (0.849)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies, Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: bolA family member 3. This gene encodes a protein that plays an essential role in the production of iron-sulfur (Fe-S) clusters for the normal maturation of lipoate-containing 2-oxoacid dehydrogenases, and for the assembly of the mitochondrial respiratory chain complexes. Mutation in this gene has been associated with multiple mitochondrial dysfunctions syndrome-2. Two alternatively spliced transcript variants encoding…
- **Diseases (Open Targets)**: multiple mitochondrial dysfunctions syndrome 2 (0.819); fatal multiple mitochondrial dysfunctions syndrome (0.595); mitochondrial disease (0.371); hereditary disease (0.191); lung adenocarcinoma (0.030)
- **Europe PMC papers**: 443
- **Why important**: BOLA3 links the mitoribosomal neighborhood to mitochondrial iron-sulfur and respiratory-chain biology. It is included in the mitochondrial matrix and mitochondrion primary terms (GO:CC mitochondrial matrix; q_global = 0.00553) (GO:CC mitochondrion; q_global = 0.0132), is supported by several STRING mitochondrial enrichments (4 supplementary STRING terms; within-query FDR 0.0014–0.0115), and has a known STRING relationship with LYRM4. Its annotation describes essential participation in iron-sulfur cluster production and maturation of lipoate-containing dehydrogenases and respiratory-chain complexes. Its established association with multiple mitochondrial dysfunctions syndrome makes it particularly informative for disease-oriented interpretation.
- **Conclusion**: Established evidence supports BOLA3 as a mechanistic bridge between mitochondrial translation-associated genes and respiratory metabolism. The hypothesis that it couples iron-sulfur availability to the observed cross-tissue co-abundance pattern is plausible but not demonstrated by these data.

#### IARS2

- **Related proteins** (co-abundance neighbors): ABLIM1 (0.87), SYNGR1 (0.80); STRING partners: YARS2 (0.919)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 2, mitochondrial. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Two forms of isoleucine-tRNA synthetase exist, a cytoplasmic form and a mitochondrial form. This gene encodes th…
- **Diseases (Open Targets)**: cataract-growth hormone deficiency-sensory neuropathy-sensorineural hearing loss-skeletal dysplasia syndrome (0.724); Leigh syndrome (0.563); hereditary disease (0.416); neurodegenerative disease (0.411); mitochondrial disease (0.374)
- **Europe PMC papers**: 411
- **Why important**: IARS2 is included in all primary mitochondrial enrichment categories (4 globally significant GO/KEGG terms, q_global 0.00553–0.0495; see the table) and in all listed STRING mitochondrial enrichments (6 supplementary STRING terms; within-query FDR 0.0014–0.0183). It encodes the mitochondrial isoleucine-tRNA synthetase, directly linking amino-acid charging to mitochondrial translation. Its strong known STRING relationship with YARS2 provides a specific interaction within the module, and its disease associations connect mitochondrial translation failure with skeletal dysplasia and neurological disease.
- **Conclusion**: Established evidence supports IARS2 as a functional connector between mitochondrial translation and amino-acid metabolism. The module does not establish that IARS2 is rate-limiting or that its disease-linked biology is specifically responsible for the bone–skin conservation.

#### BCKDHA

- **Related proteins** (co-abundance neighbors): FDFT1 (0.91), LYRM4 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_12248.1
- **Function (MyGene.info)**: branched chain keto acid dehydrogenase E1 subunit alpha. The branched-chain alpha-keto acid (BCAA) dehydrogenase (BCKD) complex is an innter mitochondrial enzyme complex that catalyzes the second major step in the catabolism of the branched-chain amino acids leucine, isoleucine, and valine. The BCKD complex consists of three catalytic components: a heterotetrameric (alpha2-beta2) branched-chain alpha-keto acid decarboxylase (E1), a dihydrolipoyl transac…
- **Diseases (Open Targets)**: maple syrup urine disease type 1A (0.840); maple syrup urine disease (0.758); hereditary disease (0.508); refractive error (0.387); classic maple syrup urine disease (0.370)
- **Europe PMC papers**: 1111
- **Why important**: BCKDHA is a mitochondrial branched-chain amino-acid catabolic enzyme, included in the primary mitochondrial terms (GO:CC mitochondrial matrix; q_global = 0.00553) (GO:CC mitochondrion; q_global = 0.0132) and supported by STRING mitochondrial annotations (6 supplementary STRING terms; within-query FDR 0.0014–0.0183). It is present with KGD4 in the hu.MAP metabolic complex (hu.MAP huMAP3_12248.1) and connects in the module to FDFT1 and LYRM4. Its established role in branched-chain amino-acid oxidation and its association with maple syrup urine disease provide a metabolic anchor distinct from the mitoribosomal genes.
- **Conclusion**: Established evidence supports BCKDHA as a representative of mitochondrial substrate oxidation within the module. Its connection to translation and iron-sulfur genes is a systems-level co-abundance relationship, not proof of a direct physical pathway.

## Module 3

**Tissue pair**: bone and skin  
**Genes (34)**: ACLY, MTHFD1, CLTC, FASN, HSPH1, IMPDH2, MMS19, PDCD6IP, PPM1G, PSMC6, PSMC4, PSMC2, PSMD13, PAICS, ATIC, CAD, RPL3, RUVBL2, AARS1, EPRS1, IARS1, KARS1, LARS1, MARS1, NARS1, QARS1, RARS1, CCT5, CCT3, CCT7, CCT8, TLN1, USP5, XPO1

### Function

The strongest interpretation is a conserved intracellular protein-production and proteostasis module. The primary evidence is the coordinated enrichment of ATP and adenyl-nucleotide binding (GO:MF ATP binding; q_global = 1.85e-07), (GO:MF adenyl ribonucleotide binding; q_global = 1.85e-07), (GO:MF adenyl nucleotide binding; q_global = 9.94e-07), aminoacyl-tRNA ligase activity and tRNA aminoacylation (6 globally significant GO/KEGG terms, q_global 1.93e-06–1.93e-06; see the table), and the aminoacyl-tRNA synthetase multienzyme complex (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 9.1e-07). This is supported by the concentration of cytosolic aminoacyl-tRNA synthetases, the CCT chaperonin subunits (GO:CC chaperonin-containing T-complex; q_global = 0.000993), and proteasome regulatory-particle components (GO:CC proteasome regulatory particle; q_global = 0.000993), (GO:CC proteasome accessory complex; q_global = 0.000993), (GO:CC proteasome regulatory particle, base subcomplex; q_global = 0.0249), (KEGG Proteasome - Homo sapiens (human); q_global = 0.0473). Purine and broader nucleotide metabolism also contribute through ATIC, PAICS, IMPDH2, MTHFD1, CAD, and related genes. The CCT subgroup is additionally associated with protein folding and telomerase-RNA or Cajal-body localization (4 globally significant GO/KEGG terms, q_global 9.44e-06–9.44e-06; see the table), (12 globally significant GO/KEGG terms, q_global 0.000283–0.00172; see the table), although those annotations should not be taken to mean that telomerase is the dominant module function. Overall, the module is best viewed as a biosynthetic and quality-control program supporting translation, folding, nucleotide supply, and degradation of damaged or surplus proteins.

**Cell composition.** This is not primarily a plasma-protein, secreted-protein, or blood-cell module. HPA reports low tissue specificity for most genes, low immune-cell specificity for nearly all genes, and only a small secreted-protein component. Protein detection is widespread in skin, while there is no matching HPA bone-tissue measurement in the supplied summary. The genes are predominantly cytosolic or nuclear housekeeping-type components, including translation machinery, chaperones, metabolic enzymes, and proteasome subunits. The HPA single-cell enrichments in germ-cell, trophoblast, epithelial, cardiac, and other cell types therefore suggest broad cellular expression with some context-dependent enhancement rather than a specific blood-cell explanation. The extracellular-region and vesicle annotations (GO:CC extracellular region; q_global = 1.79e-05), (5 globally significant GO/KEGG terms, q_global 0.00014–0.000163; see the table), (GO:CC vesicle; q_global = 0.00179) are compatible with vesicle-associated or broadly detected intracellular proteins and do not establish that the module is a secreted plasma-protein program. Shared abundance in bone and skin may consequently reflect common cellular demand for translation, folding, metabolism, and proteostasis, or shared cell-state composition, rather than a tissue-exclusive pathway.

**GO/KEGG enrichment**: 66 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF ATP binding | 1.85e-07 | AARS1, ACLY, CAD, CCT3, CCT5, CCT7, CCT8, EPRS1, HSPH1, IARS1, KARS1, LARS1, MARS1, MTHFD1, NARS1, PAICS, PSMC2, PSMC4, PSMC6, QARS1, RARS1, RUVBL2 |
| GO:MF adenyl ribonucleotide binding | 1.85e-07 | AARS1, ACLY, CAD, CCT3, CCT5, CCT7, CCT8, EPRS1, HSPH1, IARS1, KARS1, LARS1, MARS1, MTHFD1, NARS1, PAICS, PSMC2, PSMC4, PSMC6, QARS1, RARS1, RUVBL2 |
| GO:CC intracellular protein-containing complex | 7.12e-07 | CCT3, CCT5, CCT7, CCT8, EPRS1, IARS1, KARS1, LARS1, MARS1, MMS19, PSMC2, PSMC4, PSMC6, PSMD13, QARS1, RARS1, RUVBL2 |
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 9.1e-07 | EPRS1, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1 |
| GO:MF adenyl nucleotide binding | 9.94e-07 | AARS1, ACLY, CAD, CCT3, CCT5, CCT7, CCT8, EPRS1, HSPH1, IARS1, KARS1, LARS1, MARS1, MTHFD1, NARS1, PAICS, PSMC2, PSMC4, PSMC6, QARS1, RARS1, RUVBL2 |
| GO:MF aminoacyl-tRNA ligase activity | 1.93e-06 | AARS1, EPRS1, IARS1, KARS1, LARS1, MARS1, NARS1, QARS1, RARS1 |
| GO:BP tRNA aminoacylation for protein translation | 1.93e-06 | AARS1, EPRS1, IARS1, KARS1, LARS1, MARS1, NARS1, QARS1, RARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 1.93e-06 | AARS1, EPRS1, IARS1, KARS1, LARS1, MARS1, NARS1, QARS1, RARS1 |
| GO:BP amino acid activation | 1.93e-06 | AARS1, EPRS1, IARS1, KARS1, LARS1, MARS1, NARS1, QARS1, RARS1 |
| GO:BP tRNA aminoacylation | 1.93e-06 | AARS1, EPRS1, IARS1, KARS1, LARS1, MARS1, NARS1, QARS1, RARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 1.93e-06 | AARS1, EPRS1, IARS1, KARS1, LARS1, MARS1, NARS1, QARS1, RARS1 |
| GO:MF ligase activity | 3.24e-06 | AARS1, CAD, EPRS1, IARS1, KARS1, LARS1, MARS1, MTHFD1, NARS1, PAICS, QARS1, RARS1 |
| GO:MF purine ribonucleotide binding | 6.26e-06 | AARS1, ACLY, CAD, CCT3, CCT5, CCT7, CCT8, EPRS1, HSPH1, IARS1, KARS1, LARS1, MARS1, MTHFD1, NARS1, PAICS, PSMC2, PSMC4, PSMC6, QARS1, RARS1, RUVBL2 |
| GO:MF purine ribonucleoside triphosphate binding | 6.26e-06 | AARS1, ACLY, CAD, CCT3, CCT5, CCT7, CCT8, EPRS1, HSPH1, IARS1, KARS1, LARS1, MARS1, MTHFD1, NARS1, PAICS, PSMC2, PSMC4, PSMC6, QARS1, RARS1, RUVBL2 |
| GO:MF ribonucleotide binding | 7.42e-06 | AARS1, ACLY, CAD, CCT3, CCT5, CCT7, CCT8, EPRS1, HSPH1, IARS1, KARS1, LARS1, MARS1, MTHFD1, NARS1, PAICS, PSMC2, PSMC4, PSMC6, QARS1, RARS1, RUVBL2 |

### STRING and hu.MAP

STRING supports several known physical or functional assemblies. The aminoacyl-tRNA synthetases form a dense interaction cluster, including the especially strong links among EPRS1, IARS1, KARS1, LARS1, MARS1, QARS1, and RARS1, with AARS1 and NARS1 also connected. CCT3, CCT5, CCT7, and CCT8 form a highly coherent CCT chaperonin cluster, while PSMC2, PSMC4, PSMC6, and PSMD13 form a coherent proteasome-regulatory cluster. ATIC, PAICS, IMPDH2, and MTHFD1 support a nucleotide-biosynthesis neighborhood, and ACLY with FASN supports a lipid-biosynthesis neighborhood. hu.MAP independently recovers the multisynthetase complexes (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1), the CCT assemblies (hu.MAP huMAP3_07938.1), (hu.MAP huMAP3_06559.1), (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1), and proteasome assemblies (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1). It also connects metabolic pairs such as CAD with FASN (hu.MAP huMAP3_10103.1) and MTHFD1 with ATIC (hu.MAP huMAP3_12823.1). Thus, much of the observed network structure is already known molecular machinery rather than unexplained pairwise biology. The remaining co-abundance links may represent shared expression control, indirect pathway coupling, or sample-composition effects; STRING and hu.MAP do not by themselves prove direct physical binding for every module edge.

**STRING interactions (score >= 0.7)**: 69 of 561 gene pairs: AARS1–EPRS1 (0.976); AARS1–IARS1 (0.98); AARS1–KARS1 (0.992); AARS1–LARS1 (0.968); AARS1–MARS1 (0.913); AARS1–NARS1 (0.947); AARS1–QARS1 (0.964); AARS1–RARS1 (0.85); ACLY–FASN (0.994); ACLY–MTHFD1 (0.723); ATIC–CCT7 (0.881); ATIC–CLTC (0.864); ATIC–IMPDH2 (0.991); ATIC–MTHFD1 (0.998); ATIC–PAICS (0.997); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT3–RUVBL2 (0.766); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT5–RPL3 (0.731); CCT5–RUVBL2 (0.705); CCT7–CCT8 (0.999); CCT7–IMPDH2 (0.758); CCT7–RPL3 (0.8); CCT7–RUVBL2 (0.802); CCT8–PSMC2 (0.733); CCT8–RUVBL2 (0.776); EPRS1–IARS1 (0.999); EPRS1–KARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–MARS1 (0.999); EPRS1–NARS1 (0.998); EPRS1–QARS1 (0.999); EPRS1–RARS1 (0.999); EPRS1–RPL3 (0.855); IARS1–KARS1 (0.999); IARS1–LARS1 (0.999); IARS1–MARS1 (0.999); IARS1–NARS1 (0.965); IARS1–QARS1 (0.999); IARS1–RARS1 (0.999); IMPDH2–PAICS (0.744); KARS1–LARS1 (0.999); KARS1–MARS1 (0.999); KARS1–NARS1 (0.931); KARS1–QARS1 (0.999); KARS1–RARS1 (0.999); KARS1–RPL3 (0.705); LARS1–MARS1 (0.999); LARS1–NARS1 (0.954); LARS1–QARS1 (0.999); LARS1–RARS1 (0.999); MARS1–NARS1 (0.886); MARS1–QARS1 (0.999); MARS1–RARS1 (0.999); MTHFD1–PAICS (0.9); NARS1–QARS1 (0.887); NARS1–RARS1 (0.909); PSMC2–PSMC4 (0.999); PSMC2–PSMC6 (0.999); PSMC2–PSMD13 (0.999); PSMC2–RPL3 (0.705); PSMC4–PSMC6 (0.999); PSMC4–PSMD13 (0.999); PSMC6–PSMD13 (0.999); QARS1–RARS1 (0.999); QARS1–RPL3 (0.749)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Liver (FDR = 3.48e-10, 30 genes); TISSUES Lymphoblast (FDR = 3.48e-10, 15 genes); Keyword ATP-binding (FDR = 1.93e-09, 22 genes); Function ATP binding (FDR = 1.51e-08, 22 genes); Keyword Ligase (FDR = 3.18e-08, 12 genes); TISSUES Lymphocyte (FDR = 1.32e-07, 16 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 1.36e-07, 9 genes); COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex (FDR = 1.37e-07, 8 genes); Function Ligase activity (FDR = 2.37e-07, 12 genes); Function aminoacyl-tRNA ligase activity (FDR = 2.75e-07, 9 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 2.99e-07, 9 genes); COMPARTMENTS Cytosol (FDR = 3.12e-07, 29 genes); RCTM Cytosolic tRNA aminoacylation (FDR = 3.19e-07, 9 genes); Keyword Acetylation (FDR = 3.53e-07, 33 genes); Function Nucleotide binding (FDR = 5.65e-07, 23 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, IARS1, QARS1, RARS1, MARS1, KARS1, LARS1; 7/14); huMAP3_13688.1 (EPRS1, IARS1, QARS1, RARS1, MARS1, KARS1, LARS1; 7/14); huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_05064.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/31); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_09656.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/64); huMAP3_13725.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/69); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_10103.1 (CAD, FASN; 2/4); huMAP3_12823.1 (MTHFD1, ATIC; 2/7); huMAP3_10302.1 (NARS1, AARS1; 2/9); huMAP3_10115.1 (NARS1, AARS1; 2/14); huMAP3_09042.1 (XPO1, MMS19; 2/26); huMAP3_14982.1 (NARS1, TLN1; 2/28); huMAP3_14306.1 (PPM1G, RUVBL2; 2/55); huMAP3_14442.1 (ATIC, AARS1; 2/57)

### Novelty

The module should not be presented as a newly discovered protein complex or pathway. Its central components are established members of the aminoacyl-tRNA synthetase complex, CCT chaperonin, proteasome, nucleotide biosynthesis, and lipid-biosynthesis systems, as shown by the primary annotations and the known interactions in STRING and hu.MAP. A potentially novel aspect is the reproducible co-abundance of these established systems in a conserved bone-skin module, particularly if that conservation was not previously reported in the underlying tissue analysis. However, the supplied evidence does not include a comparison against prior bone-skin co-abundance studies, nor does it establish a new physical assembly or tissue-specific mechanism. Therefore the defensible conclusion is that this is a potentially interesting tissue-pair co-abundance observation built largely from known cellular machinery, with novelty requiring independent replication and formal comparison to existing tissue-network studies. Absence from a database would not by itself establish novelty.

**Hypothesis.** Hypothesis: bone and skin cells sharing a metabolically active, protein-producing state coordinate aminoacyl-tRNA charging with nucleotide and acetyl-CoA supply, then use CCT-mediated folding and proteasomal turnover to maintain proteome quality during matrix production, differentiation, or environmental stress. In this model, the aminoacyl-tRNA synthetase cluster supplies translational capacity, ATIC, PAICS, IMPDH2, MTHFD1, and CAD supply nucleotide precursors, ACLY and FASN connect carbon metabolism to lipid or membrane biosynthesis, and the CCT and proteasome submodules manage folding and disposal. The hypothesis predicts coordinated changes in translation, nucleotide availability, chaperone activity, and proteasome flux in matched bone and skin cell populations. It remains a hypothesis because co-abundance does not demonstrate causal regulation, direct cross-complex assembly, or a bone-skin-specific signaling pathway.

### Important genes

#### NARS1

- **Related proteins** (co-abundance neighbors): CCT5 (0.85), ATIC (0.83), AARS1 (0.82), CCT7 (0.82), PAICS (0.82), TLN1 (0.82), PDCD6IP (0.80); STRING partners: AARS1 (0.947), EPRS1 (0.998), IARS1 (0.965), KARS1 (0.931), LARS1 (0.954), MARS1 (0.886), QARS1 (0.887), RARS1 (0.909)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_10302.1, huMAP3_10115.1, huMAP3_14982.1
- **Function (MyGene.info)**: asparaginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids.  Asparaginyl-tRNA synthetase is localized to the cytoplasm and belongs to the class II family of tRNA synthetases.  The N-terminal domain represents the signature sequence for the eukaryotic asparaginyl-tRNA synthetases. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, impaired language, and gait abnormalities (0.762); neurodevelopmental disorder with microcephaly, impaired language, epilepsy, and gait abnormalities (0.679); neurodevelopmental disorder (0.567); complex neurodevelopmental disorder (0.462); developmental disability (0.340)
- **Europe PMC papers**: 216
- **Why important**: NARS1 has a prominent module position and connects the aminoacyl-tRNA synthetase cluster to CCT5, ATIC, PAICS, TLN1, and PDCD6IP. It is annotated as the cytosolic asparaginyl-tRNA synthetase and participates in the globally corrected translation and tRNA-aminoacylation terms (6 globally significant GO/KEGG terms, q_global 1.93e-06–1.93e-06; see the table), (GO:BP amino acid metabolic process; q_global = 0.000186), (GO:MF catalytic activity, acting on a tRNA; q_global = 0.000196), (GO:BP tRNA metabolic process; q_global = 0.00185). Its STRING links to the other synthetases and its hu.MAP membership (hu.MAP huMAP3_10302.1), (hu.MAP huMAP3_10115.1), (hu.MAP huMAP3_14982.1) show that this is an established complex-associated component. The supplied disease associations include developmental and neurological disorders, and its literature volume is substantial enough to support a well-established core function.
- **Conclusion**: Established conclusion: NARS1 is a central translational-capacity marker and a credible connector between the synthetase machinery and metabolic or structural parts of the module. Hypothesis: variation in NARS1 abundance could help couple amino-acid availability or translational demand to the broader bone-skin proteostasis state, but the module data do not demonstrate such regulation.

#### EPRS1

- **Related proteins** (co-abundance neighbors): LARS1 (0.87), IARS1 (0.80), CAD (0.80); STRING partners: AARS1 (0.976), IARS1 (0.999), KARS1 (0.999), LARS1 (0.999), MARS1 (0.999), NARS1 (0.998), QARS1 (0.999), RARS1 (0.999), RPL3 (0.855)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is a member of the multisynthetase complex (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1) and is densely connected in STRING to nearly all of the module's aminoacyl-tRNA synthetases. It encodes the multifunctional glutamyl-prolyl-tRNA synthetase and is present across the primary tRNA-aminoacylation and translation evidence (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 9.1e-07), (7 globally significant GO/KEGG terms, q_global 1.93e-06–3.24e-06; see the table), (GO:BP amino acid metabolic process; q_global = 0.000186), (GO:MF catalytic activity, acting on a tRNA; q_global = 0.000196), (GO:BP tRNA metabolic process; q_global = 0.00185). Its disease associations include hypomyelinating leukodystrophy and developmental disability, while its literature volume is moderate. It is therefore a mechanistically informative representative of the most statistically coherent functional block.
- **Conclusion**: Established conclusion: EPRS1 supports the interpretation that the module contains a coordinated multisynthetase translation apparatus rather than isolated synthetase genes. Hypothesis: EPRS1 may act as a dosage-sensitive point through which translational demand and cellular stress influence the conserved module, but this cannot be inferred as a tissue-specific causal role from co-abundance alone.

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT8 (0.93), PSMC2 (0.90), CCT7 (0.88), NARS1 (0.85), AARS1 (0.85), CCT3 (0.84), PSMC4 (0.83), HSPH1 (0.83), PAICS (0.82); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999), RPL3 (0.731), RUVBL2 (0.705)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 has the strongest network position in the supplied module and links the CCT cluster to proteasome and aminoacyl-tRNA-synthetase components. It is part of the CCT complex (hu.MAP huMAP3_07938.1), (hu.MAP huMAP3_06559.1), (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) and has very strong STRING relationships with CCT3, CCT7, and CCT8. Its annotations support ATP-dependent protein folding, protein stabilization, and telomerase-RNA or Cajal-body localization (GO:CC chaperonin-containing T-complex; q_global = 0.000993), (7 globally significant GO/KEGG terms, q_global 0.000993–0.00172; see the table), (GO:BP positive regulation of telomere maintenance; q_global = 0.00853), (GO:CC protein folding chaperone complex; q_global = 0.00853), (GO:MF protein folding chaperone; q_global = 0.0171). It has a substantial literature volume and disease associations involving hereditary sensory and autonomic neuropathy and neurodegenerative disease.
- **Conclusion**: Established conclusion: CCT5 is a strong network and functional representative of the module's protein-folding arm. Hypothesis: CCT5-centered chaperone activity may buffer the increased folding burden created by high translation or differentiation-related remodeling in bone and skin, but the supplied data do not show that CCT5 is the driver of the shared module.

#### PSMC2

- **Related proteins** (co-abundance neighbors): CCT5 (0.90), CCT8 (0.88), PSMC4 (0.83), CAD (0.81), PSMC6 (0.80), PSMD13 (0.80); STRING partners: CCT8 (0.733), PSMC4 (0.999), PSMC6 (0.999), PSMD13 (0.999), RPL3 (0.705)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 connects the CCT neighborhood to the proteasome cluster and is supported by STRING links to PSMC4, PSMC6, and PSMD13. It is a proteasome regulatory-particle ATPase and is included in the globally corrected proteasome terms (GO:CC proteasome regulatory particle; q_global = 0.000993), (GO:CC proteasome accessory complex; q_global = 0.000993), (GO:MF proteasome-activating activity; q_global = 0.0084), (GO:CC proteasome regulatory particle, base subcomplex; q_global = 0.0249), (KEGG Proteasome - Homo sapiens (human); q_global = 0.0473). hu.MAP confirms its membership in multiple proteasome assemblies (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1). Its disease associations include plasma-cell myeloma, mantle-cell lymphoma, neoplasm, HIV infection, and amyloidosis, and its literature volume is substantial.
- **Conclusion**: Established conclusion: PSMC2 marks the module's ATP-dependent protein-degradation and quality-control arm. Hypothesis: coordinated PSMC2 abundance may allow bone and skin cells to remove misfolded or damaged proteins generated during stress or matrix-related activity, but the network does not establish altered proteasome flux.

#### ACLY

- **Related proteins** (co-abundance neighbors): FASN (0.85), XPO1 (0.85), ATIC (0.84), HSPH1 (0.82), MTHFD1 (0.82), CLTC (0.80); STRING partners: FASN (0.994), MTHFD1 (0.723)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP citrate lyase. ATP citrate lyase is the primary enzyme responsible for the synthesis of cytosolic acetyl-CoA in many tissues. The enzyme is a tetramer (relative molecular weight approximately 440,000) of apparently identical subunits. It catalyzes the formation of acetyl-CoA and oxaloacetate from citrate and CoA with a concomitant hydrolysis of ATP to ADP and phosphate. The product, acetyl-CoA, serves several im…
- **Diseases (Open Targets)**: familial hypercholesterolemia (0.532); Hypercholesterolemia (0.532); atherosclerosis (0.470); inherited lipid metabolism disorder (0.467); cardiovascular disorder (0.449)
- **Europe PMC papers**: 7957
- **Why important**: ACLY is a network bridge connecting FASN, MTHFD1, ATIC, HSPH1, and CLTC. It is the cytosolic source of acetyl-CoA described in the fact sheet and is associated with acetyl-CoA, fatty-acid, cholesterol, and citrate metabolism. Its link to FASN is supported by STRING and its pairing with FASN in hu.MAP (hu.MAP huMAP3_10103.1). ACLY is included in the broad nucleotide-binding and metabolic primary evidence (GO:MF ATP binding; q_global = 1.85e-07), (GO:MF adenyl ribonucleotide binding; q_global = 1.85e-07), (GO:MF adenyl nucleotide binding; q_global = 9.94e-07), (GO:MF purine ribonucleotide binding; q_global = 6.26e-06) (GO:MF purine ribonucleoside triphosphate binding; q_global = 6.26e-06) (GO:MF ribonucleotide binding; q_global = 7.42e-06), (9 globally significant GO/KEGG terms, q_global 1.69e-05–7.6e-05; see the table), (GO:CC vesicle; q_global = 0.00179), (GO:MF ion binding; q_global = 0.00259), (GO:MF small molecule binding; q_global = 0.00544), (GO:BP primary metabolic process; q_global = 0.0104). It has extensive literature coverage and disease associations involving hypercholesterolemia, familial hypercholesterolemia, and atherosclerosis.
- **Conclusion**: Established conclusion: ACLY provides a plausible metabolic bridge between the module's biosynthetic machinery and lipid production. Hypothesis: ACLY may help couple carbon flux to the translational and proteostasis demand of shared bone-skin cell states, but the data do not establish that lipid metabolism is the primary reason the module is conserved.

## Module 4

**Tissue pair**: bone and skin  
**Genes (28)**: ACO2, ALDH4A1, ALDH2, CTNND1, DDX24, DDX46, HSD17B8, HK1, MBD3, MED23, MTA2, MMUT, NAA40, NFS1, OPA1, TP53I11, PINX1, PLCB3, PSME4, RAB10, RAB8A, RAB8B, DPF2, RAB11FIP5, RTN1, SIN3A, TRMT6, XTBD1

### Function

The module does not have any GO or KEGG term passing global correction, so no GO/KEGG functional enrichment can be claimed. Nevertheless, the gene-level and network evidence supports a composite intracellular maintenance module rather than a single established pathway. One component is vesicle trafficking and exocytic membrane delivery, centered on RAB8A, RAB8B, RAB10 and RAB11FIP5. This interpretation is supported by the supplementary STRING terms (STRING NetworkNeighborAL Mixed, incl. Exocyst, and FIP domain; within-query FDR = 0.0263) and (STRING NetworkNeighborAL Mixed, incl. Golgi vesicle fusion to target membrane, and GDP/GTP exchange factor Sec2p; within-query FDR = 0.045), and by the repeated hu.MAP assemblies containing the RAB8A–RAB10–RAB8B group (hu.MAP huMAP3_06607.1), (hu.MAP huMAP3_11094.1) and (hu.MAP huMAP3_11860.1). A second component is nuclear chromatin and transcriptional regulation, represented by MTA2, MBD3 and SIN3A through STRING and hu.MAP evidence (hu.MAP huMAP3_15128.1), (hu.MAP huMAP3_03905.1), (hu.MAP huMAP3_08738.1), (hu.MAP huMAP3_09499.1) and (hu.MAP huMAP3_10472.1). A third component is mitochondrial metabolism and stress handling, including ALDH2, ALDH4A1, ACO2, MMUT, HSD17B8, NFS1 and OPA1, with supporting STRING links and metabolic hu.MAP assemblies (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1). Thus, the most defensible interpretation is co-abundance of vesicle transport, gene-regulatory machinery and mitochondrial metabolic capacity, with no evidence that these processes form a single proven biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not strongly blood-cell specific overall. Most genes have low immune-cell specificity, although a subset is immune-cell enhanced or group enriched, including genes associated with monocytes, myeloid dendritic cells, neutrophils and other blood populations. The module is broadly distributed across tissues, with many genes having low tissue specificity and a smaller group enhanced in liver, skeletal muscle, heart muscle, kidney, intestine or testis. Single-cell annotations are heterogeneous, with enrichment in late spermatids, hepatocytes, enterocytes, epithelial populations, retinal cells and selected immune populations. Skin protein detection is common among the tested genes, but this does not establish skin-specific biology, and there is no matching HPA bone tissue assessment. Overall, the shared bone–skin signal could reflect broadly expressed cellular machinery or shared cell states, with a possible contribution from resident or contaminating immune cells, rather than a secreted blood-protein signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a sparse but biologically coherent set of high-confidence relationships. The RAB8A–RAB8B and RAB8A–RAB10 links directly support a vesicle-trafficking subnetwork, while ALDH2 connects to ALDH4A1 and ACO2 connects to ALDH2 and NFS1, supporting a separate mitochondrial metabolic neighborhood. MBD3–MTA2 and MTA2–SIN3A support a chromatin-regulatory neighborhood. The supplementary STRING terms (STRING NetworkNeighborAL Mixed, incl. Exocyst, and FIP domain; within-query FDR = 0.0263) and (STRING NetworkNeighborAL Mixed, incl. Golgi vesicle fusion to target membrane, and GDP/GTP exchange factor Sec2p; within-query FDR = 0.045) specifically connect RAB10, RAB8A, RAB8B and RAB11FIP5 with exocyst-related and Golgi vesicle-fusion biology; these are supportive annotations, not globally corrected enrichment. hu.MAP independently recovers the RAB8A–RAB10–RAB8B combination across several broad Rab assemblies (hu.MAP huMAP3_06607.1), (hu.MAP huMAP3_11094.1), (hu.MAP huMAP3_11860.1), (hu.MAP huMAP3_07302.1) and (hu.MAP huMAP3_01895.1) through (hu.MAP huMAP3_09217.1). It also repeatedly recovers the MTA2–MBD3 pair in chromatin complexes (hu.MAP huMAP3_15128.1), (hu.MAP huMAP3_03905.1), (hu.MAP huMAP3_08738.1), (hu.MAP huMAP3_09499.1) and (hu.MAP huMAP3_10472.1), and the metabolic pairs ALDH4A1–MMUT and HSD17B8–MMUT in (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1). These results indicate that parts of the module reproduce known molecular systems, while many cross-subnetwork co-abundance edges are not represented by known physical interactions.

**STRING interactions (score >= 0.7)**: 7 of 378 gene pairs: ACO2–ALDH2 (0.751); ACO2–NFS1 (0.89); ALDH2–ALDH4A1 (0.85); MBD3–MTA2 (0.996); MTA2–SIN3A (0.783); RAB10–RAB8A (0.831); RAB8A–RAB8B (0.985)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Mixed, incl. Exocyst, and FIP domain (FDR = 0.0263, 4 genes); NetworkNeighborAL Mixed, incl. Golgi vesicle fusion to target membrane, and GDP/GTP exchange factor Sec2p (FDR = 0.045, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06607.1 (RAB8A, RAB10, RAB8B; 3/16); huMAP3_11094.1 (RAB8A, RAB10, RAB8B; 3/43); huMAP3_11860.1 (RAB8A, RAB10, RAB8B; 3/44); huMAP3_15128.1 (MTA2, MBD3, SIN3A; 3/96); huMAP3_13468.1 (MMUT, ALDH4A1, HSD17B8; 3/99); huMAP3_03905.1 (MTA2, MBD3; 2/10); huMAP3_07302.1 (RAB8A, RAB10; 2/13); huMAP3_08738.1 (MTA2, MBD3; 2/17); huMAP3_01895.1 (RAB8A, RAB10; 2/19); huMAP3_06994.1 (RAB8A, RAB10; 2/24); huMAP3_08941.1 (RAB8A, RAB10; 2/28); huMAP3_09217.1 (RAB8A, RAB10; 2/29); huMAP3_10525.1 (MMUT, HSD17B8; 2/33); huMAP3_09499.1 (MTA2, MBD3; 2/33); huMAP3_10472.1 (MTA2, MBD3; 2/36)

### Novelty

This module should not be described as a newly discovered molecular complex or pathway. Several of its strongest interpretable components are already known: Rab-mediated trafficking is represented in STRING and hu.MAP, the MTA2–MBD3–SIN3A regulatory neighborhood is supported by STRING and hu.MAP, and selected metabolic relationships are also catalogued. The possible novelty is instead at the systems level: these vesicle, chromatin and mitochondrial genes co-abundance together in the conserved bone–skin module. That cross-tissue co-abundance relationship may be informative, but it requires replication, control for cell composition, and comparison with existing tissue-expression modules before being called a new biological finding. The absence of a STRING or hu.MAP relationship for an edge does not by itself prove novelty, because co-abundance can reflect shared regulation, cell composition, indirect coupling or technical effects.

**Hypothesis.** Hypothesis: in bone and skin, a shared cellular state may coordinate mitochondrial metabolic capacity and aldehyde or oxidative-stress handling with membrane trafficking and transcriptional control. Rab proteins could support delivery and recycling of surface or secretory machinery, while MTA2–MBD3–SIN3A-associated regulation could help maintain the relevant cell-state program. ALDH2, ALDH4A1, ACO2, MMUT, HSD17B8, NFS1 and OPA1 could reflect the energetic and redox requirements of that state. This is a mechanistic hypothesis, not an established causal model: the lack of globally significant GO or KEGG enrichment, the sparse direct interaction network and the heterogeneous HPA cell-type annotations mean that shared cell composition or parallel regulation remain viable alternatives.

### Important genes

#### RAB8A

- **Related proteins** (co-abundance neighbors): RAB8B (0.88), RTN1 (0.83), RAB10 (0.83); STRING partners: RAB10 (0.831), RAB8B (0.985)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06607.1, huMAP3_11094.1, huMAP3_11860.1, huMAP3_07302.1, huMAP3_01895.1, huMAP3_06994.1, huMAP3_08941.1, huMAP3_09217.1
- **Function (MyGene.info)**: RAB8A, member RAS oncogene family. The protein encoded by this gene is a member of the RAS superfamily which are small GTP/GDP-binding proteins with an average size of 200 amino acids. The RAS-related proteins of the RAB/YPT family may play a role in the transport of proteins from the endoplasmic reticulum to the Golgi and the plasma membrane. This protein shares 97%, 96%, and 51% similarity with the dog RAB8, mouse MEL, and mouse …
- **Diseases (Open Targets)**: acute respiratory distress syndrome (0.077); non-small cell lung carcinoma (0.076); esophageal cancer (0.076); congenital diarrhea 5 with tufting enteropathy (0.068); inflammatory bowel disease 30 (0.067)
- **Europe PMC papers**: 2105
- **Why important**: RAB8A is a central member of the vesicle-trafficking portion of the module, with connections to RAB8B and RAB10 in the co-abundance graph. It has direct STRING support with both paralogous or pathway-related Rab proteins and occurs in many hu.MAP Rab assemblies (hu.MAP huMAP3_06607.1), (hu.MAP huMAP3_11094.1), (hu.MAP huMAP3_11860.1), (hu.MAP huMAP3_07302.1) and (hu.MAP huMAP3_01895.1) through (hu.MAP huMAP3_09217.1). Its supplied annotation links it to exocytosis, Golgi organization and endocytic recycling, while (STRING NetworkNeighborAL Mixed, incl. Exocyst, and FIP domain; within-query FDR = 0.0263) and (STRING NetworkNeighborAL Mixed, incl. Golgi vesicle fusion to target membrane, and GDP/GTP exchange factor Sec2p; within-query FDR = 0.045) provide supplementary support for exocyst-related and Golgi vesicle-fusion biology. Its literature volume is substantial, making it a well-established anchor rather than an uncharacterized candidate.
- **Conclusion**: Established: RAB8A is a plausible representative of a known intracellular trafficking system and is one of the strongest functional anchors of the module. Hypothesis: its co-abundance with metabolic and chromatin genes may indicate coordinated trafficking and cellular-state maintenance in bone and skin, but the module does not establish a RAB8A-dependent mechanism.

#### RAB10

- **Related proteins** (co-abundance neighbors): RAB8A (0.83); STRING partners: RAB8A (0.831)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_06607.1, huMAP3_11094.1, huMAP3_11860.1, huMAP3_07302.1, huMAP3_01895.1, huMAP3_06994.1, huMAP3_08941.1, huMAP3_09217.1
- **Function (MyGene.info)**: RAB10, member RAS oncogene family. RAB10 belongs to the RAS (see HRAS; MIM 190020) superfamily of small GTPases. RAB proteins localize to exocytic and endocytic compartments and regulate intracellular vesicle trafficking (Bao et al., 1998 [PubMed 9918381]).[supplied by OMIM, Mar 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.549); digestive system disorder (0.242); cervical carcinoma (0.215); lobular capilliary hemangioma (0.165); hepatocellular carcinoma (0.109)
- **Europe PMC papers**: 2856
- **Why important**: RAB10 links the module to vesicle transport, Golgi-to-plasma-membrane transport, endosomal transport and exocytosis according to the supplied annotation. It is directly connected to RAB8A in STRING and appears with RAB8A in multiple hu.MAP assemblies (hu.MAP huMAP3_06607.1), (hu.MAP huMAP3_11094.1), (hu.MAP huMAP3_11860.1), (hu.MAP huMAP3_07302.1) and (hu.MAP huMAP3_01895.1) through (hu.MAP huMAP3_09217.1). It is also present in both supplementary STRING terms (STRING NetworkNeighborAL Mixed, incl. Exocyst, and FIP domain; within-query FDR = 0.0263) and (STRING NetworkNeighborAL Mixed, incl. Golgi vesicle fusion to target membrane, and GDP/GTP exchange factor Sec2p; within-query FDR = 0.045). Its cell-type pattern includes suprabasal and apical epithelial populations, which is compatible with a possible epithelial contribution in skin, although it is not skin-specific.
- **Conclusion**: Established: RAB10 supports the interpretation that the module contains a recognized membrane-trafficking subnetwork. Hypothesis: RAB10 may help couple epithelial or other bone–skin cell-surface trafficking to the broader module state, but the co-abundance data do not demonstrate directionality or functional dependence.

#### ALDH2

- **Related proteins** (co-abundance neighbors): HSD17B8 (0.84), ALDH4A1 (0.83), RAB11FIP5 (0.82), NFS1 (0.80); STRING partners: ACO2 (0.751), ALDH4A1 (0.85)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 2 family member. This protein belongs to the aldehyde dehydrogenase family of proteins. Aldehyde dehydrogenase is the second enzyme of the major oxidative pathway of alcohol metabolism. Two major liver isoforms of aldehyde dehydrogenase, cytosolic and mitochondrial, can be distinguished by their electrophoretic mobilities, kinetic properties, and subcellular localizations. Most Caucasians have two major isozymes, …
- **Diseases (Open Targets)**: alcohol dependence (0.654); alcohol drinking (0.549); AMED syndrome, digenic (0.503); gout (0.501); atrial fibrillation (0.469)
- **Europe PMC papers**: 7978
- **Why important**: ALDH2 is a highly studied mitochondrial aldehyde-detoxification enzyme and occupies the metabolic neighborhood linking ALDH4A1, HSD17B8, ACO2 and NFS1 in the module graph. STRING supports its relationships with ALDH4A1 and ACO2, and its supplied function includes aldehyde catabolism and cellular detoxification of aldehydes. HPA indicates liver enhancement and immune-cell enhancement in classical monocytes and myeloid dendritic cells, while skin protein is detected. Its disease and literature associations are extensive, giving this gene strong biological interpretability.
- **Conclusion**: Established: ALDH2 is a credible marker of mitochondrial metabolic and aldehyde-stress capacity within the module. Hypothesis: aldehyde handling may be functionally linked to the vesicle and regulatory components in the shared bone–skin state, but this cross-component link is not directly demonstrated.

#### MTA2

- **Related proteins** (co-abundance neighbors): TP53I11 (0.82); STRING partners: MBD3 (0.996), SIN3A (0.783)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_15128.1, huMAP3_03905.1, huMAP3_08738.1, huMAP3_09499.1, huMAP3_10472.1
- **Function (MyGene.info)**: metastasis associated 1 family member 2. This gene encodes a protein that has been identified as a component of NuRD, a nucleosome remodeling deacetylase complex identified in the nucleus of human cells. It shows a very broad expression pattern and is strongly expressed in many tissues. It may represent one member of a small gene family that encode different but related proteins involved either directly or indirectly in transcriptional r…
- **Diseases (Open Targets)**: neoplasm (0.108); gastric cancer (0.108); Alzheimer disease (0.102); hepatocellular carcinoma (0.100); non-small cell lung carcinoma (0.098)
- **Europe PMC papers**: 1603
- **Why important**: MTA2 represents the nuclear regulatory portion of the module. It is a component of the NuRD-associated chromatin-remodeling machinery, has STRING support with MBD3 and SIN3A, and repeatedly occurs with MBD3 in hu.MAP complexes (hu.MAP huMAP3_15128.1), (hu.MAP huMAP3_03905.1), (hu.MAP huMAP3_08738.1), (hu.MAP huMAP3_09499.1) and (hu.MAP huMAP3_10472.1). Its supplied functions include chromatin organization, transcriptional regulation, cell-fate specification and fibroblast migration. It has broad expression and skin protein detection, so it is relevant to a shared cellular program but not specific to either tissue.
- **Conclusion**: Established: MTA2 provides strong evidence that part of the module reflects known chromatin and transcriptional-regulatory machinery. Hypothesis: MTA2-associated regulation could coordinate the transcriptional response to metabolic or trafficking demands, but no causal connection to the Rab or aldehyde subnetwork is established.

#### NAA40

- **Related proteins** (co-abundance neighbors): PLCB3 (0.90), DPF2 (0.84), SIN3A (0.81), DDX46 (0.81), OPA1 (0.81), MED23 (0.81), XTBD1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-alpha-acetyltransferase 40, NatD catalytic subunit. Enables H2A histone acetyltransferase activity; H4 histone acetyltransferase activity; and peptide-serine-N-acetyltransferase activity. Involved in N-terminal protein amino acid acetylation; histone H2A acetylation; and histone H4 acetylation. Located in centriolar satellite; cytosol; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: corneal neovascularization (0.267); colorectal carcinoma (0.098); Limb pain (0.093); Chronic Obstructive Asthma (0.090); neoplasm (0.088)
- **Europe PMC papers**: 196
- **Why important**: NAA40 is among the more connected genes in the co-abundance graph and provides a bridge to DPF2, DDX46, MED23, OPA1, PLCB3 and XTBD1. Its supplied annotation identifies the NatD catalytic subunit and histone acetylation activity, with involvement in N-terminal protein acetylation and chromatin remodeling. It therefore connects protein modification and nuclear regulation to a mitochondrial and signaling context, although it has no listed STRING partner or hu.MAP complex in this module. Its literature volume is moderate and its HPA profile is broadly distributed rather than tissue-specific.
- **Conclusion**: Established: NAA40 is a biologically plausible regulatory and protein-modification component with a prominent module position, but it has less direct external network support here than the Rab or MTA2–MBD3 components. Hypothesis: NAA40 may help coordinate chromatin or protein-state adaptation across the module, an idea requiring independent experimental testing.

## Module 5

**Tissue pair**: bone and skin  
**Genes (42)**: ACOT9, CIT, PDF, HSD17B4, GFM1, TUFM, AHCTF1, EXOSC1, FH, FUNDC2, GANAB, GCLM, HDGFL3, HYOU1, KIF23, MYO1B, NDUFB5, GATAD2A, PDIA4, PRNP, RACGAP1, MRPL2, MRPL27, MRPL50, RMP64, RPF2, MRPS22, MRPS27, MRPS31, MRPS33, MRPS35, OXCT1, SNAP23, SERPINB6, SUN1, TIMMDC1, TOP2B, UBR5, UGGT1, TCIRG1, WDR74, ZNF316

### Function

The strongest and globally corrected signal is mitochondrial gene expression and mitochondrial translation, supported by the coordinated enrichment of mitochondrial ribosomal proteins and translation factors in (GO:BP mitochondrial translation; q_global = 5.5e-05), (GO:CC organellar ribosome; q_global = 8.43e-05), (GO:CC mitochondrial ribosome; q_global = 8.43e-05), and (GO:BP mitochondrial gene expression; q_global = 0.000587). The associated ribosome, mitochondrial matrix, mitochondrial protein-complex, inner-membrane, and oxidative-phosphorylation-related annotations in (GO:CC ribosomal subunit; q_global = 0.000789) through (GO:CC mitochondrion; q_global = 0.0382) indicate a module centered on production and maintenance of mitochondrially encoded respiratory-chain proteins. The module is therefore best interpreted as a mitochondrial protein-synthesis and respiratory-capacity program, with secondary links to cellular energy metabolism, protein quality control, cytokinesis, and membrane or nuclear organization. The enrichment does not establish that every peripheral gene is part of the mitoribosome; rather, it identifies a strongly connected mitochondrial core embedded in broader cellular-state relationships.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module: the HPA summary identifies only a small minority of secreted genes, and the representative genes are predominantly intracellular, mitochondrial, nuclear, membrane, or endoplasmic-reticulum proteins. Most genes have low tissue specificity, while many are cell-type enhanced. Skin protein detection is widespread among the genes with available measurements, whereas bone has no matching HPA tissue protein annotation, so the apparent bone-skin conservation cannot be validated from bone protein detection in this fact sheet. The HPA pattern does not point to a dominant blood-cell module because most genes have low immune-cell specificity and only a minority are immune-cell enhanced or enriched. Nevertheless, enrichment in bone marrow, lymphoid tissue, neutrophils, erythrocyte progenitors, and reproductive cell types indicates possible contributions from shared proliferative or specialized cell populations. The module could therefore reflect a broadly conserved mitochondrial activity state, with some contribution from cell composition or proliferative hematopoietic cells, rather than a bone- or skin-specific extracellular program.

**GO/KEGG enrichment**: 15 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP mitochondrial translation | 5.5e-05 | GFM1, MRPL2, MRPL27, MRPL50, MRPS22, MRPS27, MRPS31, MRPS33, MRPS35, TUFM |
| GO:CC organellar ribosome | 8.43e-05 | MRPL2, MRPL27, MRPL50, MRPS22, MRPS27, MRPS31, MRPS33, MRPS35 |
| GO:CC mitochondrial ribosome | 8.43e-05 | MRPL2, MRPL27, MRPL50, MRPS22, MRPS27, MRPS31, MRPS33, MRPS35 |
| GO:BP mitochondrial gene expression | 0.000587 | GFM1, MRPL2, MRPL27, MRPL50, MRPS22, MRPS27, MRPS31, MRPS33, MRPS35, TUFM |
| GO:CC ribosomal subunit | 0.000789 | MRPL2, MRPL27, MRPL50, MRPS22, MRPS27, MRPS31, MRPS33, MRPS35 |
| KEGG Ribosome - Homo sapiens (human) | 0.000789 | MRPL2, MRPL27, MRPL50, MRPS22, MRPS27, MRPS31, MRPS33, MRPS35 |
| GO:CC organellar small ribosomal subunit | 0.00604 | MRPS22, MRPS27, MRPS31, MRPS33, MRPS35 |
| GO:CC mitochondrial small ribosomal subunit | 0.00604 | MRPS22, MRPS27, MRPS31, MRPS33, MRPS35 |
| GO:CC ribosome | 0.0106 | MRPL2, MRPL27, MRPL50, MRPS22, MRPS27, MRPS31, MRPS33, MRPS35 |
| GO:CC mitochondrial protein-containing complex | 0.0106 | MRPL2, MRPL27, MRPL50, MRPS22, MRPS27, MRPS31, MRPS33, MRPS35 |
| GO:CC small ribosomal subunit | 0.02 | MRPS22, MRPS27, MRPS31, MRPS33, MRPS35 |
| GO:CC mitochondrial matrix | 0.0247 | ACOT9, FH, GFM1, MRPL2, MRPL27, MRPL50, MRPS22, MRPS27, MRPS31, MRPS33, MRPS35, OXCT1, TUFM |
| GO:MF structural constituent of ribosome | 0.0253 | MRPL2, MRPL27, MRPS22, MRPS31, MRPS33, MRPS35 |
| GO:CC organelle inner membrane | 0.0346 | MRPL2, MRPL27, MRPL50, MRPS22, MRPS27, MRPS31, MRPS33, MRPS35, NDUFB5, SUN1, TIMMDC1 |
| GO:CC mitochondrion | 0.0382 | ACOT9, FH, FUNDC2, GFM1, HYOU1, KIF23, MRPL2, MRPL27, MRPL50, MRPS22, MRPS27, MRPS31, MRPS33, MRPS35, NDUFB5, OXCT1, PDF, RACGAP1, SNAP23, TIMMDC1, TUFM |

### STRING and hu.MAP

STRING strongly supports a canonical mitochondrial translation core. GFM1 and TUFM connect to the mitochondrial large- and small-subunit proteins, while the MRPL and MRPS genes form a dense mutually supported interaction group. PDF also connects to mitochondrial ribosomal proteins. These relationships are concordant with the primary GO and KEGG evidence, although the STRING functional terms remain supplementary (STRING RCTM Mitochondrial translation elongation; within-query FDR = 1.39e-06) through (STRING Process Amide biosynthetic process; within-query FDR = 0.0018). STRING additionally supports smaller subnetworks involving the endoplasmic-reticulum quality-control genes GANAB, HYOU1, PDIA4, and UGGT1; the inner-membrane genes NDUFB5 and TIMMDC1; and the cytokinesis genes KIF23 and RACGAP1. hu.MAP independently places MRPS22, MRPS31, MRPS33, and MRPS35 in a small-subunit-associated complex (hu.MAP huMAP3_05954.1), and places MRPL2, MRPL27, and MRPL50 in several large-subunit-associated complexes (hu.MAP huMAP3_03763.1), (hu.MAP huMAP3_06439.1), and (hu.MAP huMAP3_06550.1) through (hu.MAP huMAP3_06589.1). hu.MAP also supports the GANAB, HYOU1, and PDIA4 quality-control group (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), and the KIF23-RACGAP1 cytokinesis pair (hu.MAP huMAP3_07024.1) through (hu.MAP huMAP3_09542.1). Thus, much of the module reflects already known physical or functional biology, while the co-abundance structure joins these established submodules across mitochondrial translation, protein folding, membrane organization, and cell division.

**STRING interactions (score >= 0.7)**: 58 of 861 gene pairs: CIT–KIF23 (0.902); EXOSC1–RPF2 (0.718); GANAB–HYOU1 (0.83); GANAB–PDIA4 (0.717); GANAB–UGGT1 (0.8); GFM1–MRPL2 (0.961); GFM1–MRPL27 (0.987); GFM1–MRPL50 (0.827); GFM1–MRPS22 (0.978); GFM1–MRPS27 (0.884); GFM1–MRPS31 (0.863); GFM1–MRPS33 (0.84); GFM1–MRPS35 (0.845); GFM1–TUFM (0.965); HYOU1–PDIA4 (0.997); HYOU1–UGGT1 (0.791); KIF23–RACGAP1 (0.999); MRPL2–MRPL27 (0.998); MRPL2–MRPL50 (0.963); MRPL2–MRPS22 (0.87); MRPL2–MRPS27 (0.876); MRPL2–MRPS31 (0.896); MRPL2–MRPS33 (0.871); MRPL2–MRPS35 (0.98); MRPL2–PDF (0.771); MRPL2–TUFM (0.998); MRPL27–MRPL50 (0.968); MRPL27–MRPS22 (0.851); MRPL27–MRPS27 (0.832); MRPL27–MRPS31 (0.844); MRPL27–MRPS33 (0.858); MRPL27–MRPS35 (0.991); MRPL27–PDF (0.947); MRPL27–TUFM (0.999); MRPL50–MRPS22 (0.92); MRPL50–MRPS27 (0.878); MRPL50–MRPS31 (0.86); MRPL50–MRPS33 (0.922); MRPL50–MRPS35 (0.885); MRPL50–TUFM (0.902); MRPS22–MRPS27 (0.999); MRPS22–MRPS31 (0.998); MRPS22–MRPS33 (0.993); MRPS22–MRPS35 (0.998); MRPS22–TUFM (0.988); MRPS27–MRPS31 (0.995); MRPS27–MRPS33 (0.996); MRPS27–MRPS35 (0.991); MRPS27–TUFM (0.943); MRPS31–MRPS33 (0.999); MRPS31–MRPS35 (0.998); MRPS31–TUFM (0.917); MRPS33–MRPS35 (0.992); MRPS33–TUFM (0.913); MRPS35–TUFM (0.94); NDUFB5–TIMMDC1 (0.998); PDIA4–UGGT1 (0.84); RPF2–WDR74 (0.979)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Mitochondrial translation elongation (FDR = 1.39e-06, 10 genes); Process Mitochondrial translation (FDR = 5.88e-05, 10 genes); RCTM Mitochondrial translation initiation (FDR = 6.07e-05, 8 genes); RCTM Mitochondrial translation termination (FDR = 6.07e-05, 8 genes); Component Mitochondrial ribosome (FDR = 0.00012, 8 genes); COMPARTMENTS Mitochondrial ribosome (FDR = 0.00013, 8 genes); COMPARTMENTS Ribosomal subunit (FDR = 0.00013, 8 genes); NetworkNeighborAL Organellar ribosome (FDR = 0.00017, 8 genes); Keyword Ribosomal protein (FDR = 0.00023, 8 genes); Component Ribosomal subunit (FDR = 0.00026, 8 genes); NetworkNeighborAL Organellar small ribosomal subunit (FDR = 0.00061, 5 genes); COMPARTMENTS Mitochondrial small ribosomal subunit (FDR = 0.0017, 5 genes); Process Peptide biosynthetic process (FDR = 0.0018, 12 genes); Process Cellular amide metabolic process (FDR = 0.0018, 15 genes); Process Amide biosynthetic process (FDR = 0.0018, 13 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05954.1 (MRPS22, MRPS35, MRPS31, MRPS33; 4/28); huMAP3_03763.1 (MRPL2, MRPL50, MRPL27; 3/26); huMAP3_06439.1 (MRPL2, MRPL50, MRPL27; 3/57); huMAP3_06775.1 (PDIA4, GANAB, HYOU1; 3/60); huMAP3_06550.1 (MRPL2, MRPL50, MRPL27; 3/62); huMAP3_07939.1 (MRPL2, MRPL50, MRPL27; 3/68); huMAP3_08458.1 (MRPL2, MRPL50, MRPL27; 3/70); huMAP3_09113.1 (MRPL2, MRPL50, MRPL27; 3/72); huMAP3_09483.1 (MRPL2, MRPL50, MRPL27; 3/74); huMAP3_06589.1 (MRPL2, MRPL50, MRPL27; 3/79); huMAP3_05807.1 (MRPS35, MRPS27, MRPS31; 3/81); huMAP3_09327.1 (PDIA4, GANAB, HYOU1; 3/93); huMAP3_07024.1 (KIF23, RACGAP1; 2/3); huMAP3_00688.1 (KIF23, RACGAP1; 2/4); huMAP3_11326.1 (KIF23, RACGAP1; 2/8); huMAP3_13310.1 (KIF23, RACGAP1; 2/11); huMAP3_09542.1 (MYO1B, RACGAP1; 2/38)

### Novelty

The mitochondrial-ribosome portion is not a new molecular discovery: its genes, functions, STRING relationships, and hu.MAP complexes are already well established. The potentially novel observation is the conservation of this coordinated module between bone and skin and the way its mitochondrial core is co-abundant with endoplasmic-reticulum quality control, cytokinesis, nuclear-envelope, and metabolic genes. However, the fact sheet does not provide a systematic comparison with previously published bone-skin co-abundance modules, tissue cohorts, or independent replication datasets. Absence of a gene from STRING or hu.MAP is not evidence of novelty. The appropriate conclusion is that this is a biologically coherent cross-tissue co-abundance finding with a potentially novel tissue-pair context, but it cannot be claimed as a wholly new pathway or protein complex without external replication and comparison to prior network studies.

**Hypothesis.** Hypothesis: the conserved module reflects a shared cellular demand for mitochondrial proteome maintenance and respiratory competence in bone and skin. Coordinated mitochondrial translation may sustain respiratory-chain production, while the linked metabolic genes provide substrates or redox support and the endoplasmic-reticulum quality-control genes manage folding of membrane and secretory proteins during increased biosynthetic demand. The SUN1, KIF23, RACGAP1, and related peripheral relationships suggest that this metabolic state may be coupled to nuclear architecture and cell division in selected cell populations. In bone, the program could support energetically demanding matrix-producing or remodeling cells; in skin, it could support renewing epithelial cells. This tissue-specific interpretation is a hypothesis, not an established consequence of the enrichment analysis, and should be tested with cell-resolved expression, mitochondrial activity measurements, and independent bone and skin cohorts.

### Important genes

#### MRPL27

- **Related proteins** (co-abundance neighbors): ACOT9 (0.88), MRPS35 (0.87), TOP2B (0.86), SERPINB6 (0.84), UBR5 (0.83), UGGT1 (0.83), GFM1 (0.83), EXOSC1 (0.82), OXCT1 (0.82), MRPS27 (0.82), MRPS22 (0.82), MRPS31 (0.81); STRING partners: GFM1 (0.987), MRPL2 (0.998), MRPL50 (0.968), MRPS22 (0.851), MRPS27 (0.832), MRPS31 (0.844), MRPS33 (0.858), MRPS35 (0.991), PDF (0.947), TUFM (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_03763.1, huMAP3_06439.1, huMAP3_06550.1, huMAP3_07939.1, huMAP3_08458.1, huMAP3_09113.1, huMAP3_09483.1, huMAP3_06589.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein L27. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.519); cholangiocarcinoma (0.075); neoplasm (0.045); systemic-onset juvenile idiopathic arthritis (0.020); chronic obstructive pulmonary disease (0.016)
- **Europe PMC papers**: 258
- **Why important**: MRPL27 is the strongest network hub among the highlighted genes and links the mitochondrial translation core to peripheral genes such as ACOT9, TOP2B, SERPINB6, UBR5, UGGT1, and EXOSC1. It is a mitochondrial large-subunit protein and participates across the primary mitochondrial translation, ribosome, matrix, inner-membrane, and mitochondrial annotations (GO:BP mitochondrial translation; q_global = 5.5e-05) through (GO:CC mitochondrion; q_global = 0.0382). Its extensive STRING support and repeated hu.MAP membership show that its central position is biologically interpretable rather than an isolated correlation. It also has disease associations involving neurodegenerative disease and several systemic disorders, with a substantial literature base relative to less characterized module members.
- **Conclusion**: Established evidence supports MRPL27 as a central component of the mitochondrial translation machinery and as a principal connector of the module. It is a strong marker of the module's core function. It is not established that MRPL27 specifically drives the shared bone-skin phenotype; that causal interpretation remains a hypothesis.

#### MRPS33

- **Related proteins** (co-abundance neighbors): MRPS31 (0.85), GATAD2A (0.83); STRING partners: GFM1 (0.84), MRPL2 (0.871), MRPL27 (0.858), MRPL50 (0.922), MRPS22 (0.993), MRPS27 (0.996), MRPS31 (0.999), MRPS35 (0.992), TUFM (0.913)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05954.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein S33. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: bipolar disorder (0.336); ovarian neoplasm (0.253); alopecia areata (0.251); schizophrenia (0.235); obsessive-compulsive disorder (0.235)
- **Europe PMC papers**: 206
- **Why important**: MRPS33 is part of the mitochondrial small ribosomal subunit and is represented in every globally enriched term listed in the fact sheet, including mitochondrial translation, mitochondrial ribosome, ribosomal subunit, mitochondrial matrix, and mitochondrion (GO:BP mitochondrial translation; q_global = 5.5e-05) through (GO:CC mitochondrion; q_global = 0.0382). It has exceptionally dense STRING support with the other mitochondrial ribosomal proteins and appears in hu.MAP small-subunit complex (hu.MAP huMAP3_05954.1). Its network position is not the highest by degree, but its annotation breadth and repeated independent complex support make it a particularly specific indicator of the conserved mitochondrial-ribosome core. Its disease and trait associations include neurological and alopecia-related findings, though these associations do not establish a tissue-specific mechanism here.
- **Conclusion**: Established evidence identifies MRPS33 as a robust small-subunit marker of mitochondrial translation and a useful representative of the module's core. Its role in the bone-skin co-abundance pattern is most defensibly interpreted as participation in a shared mitochondrial program, not as a demonstrated disease effector.

#### GFM1

- **Related proteins** (co-abundance neighbors): MRPL27 (0.83); STRING partners: MRPL2 (0.961), MRPL27 (0.987), MRPL50 (0.827), MRPS22 (0.978), MRPS27 (0.884), MRPS31 (0.863), MRPS33 (0.84), MRPS35 (0.845), TUFM (0.965)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G elongation factor mitochondrial 1. Eukaryotes contain two protein translational systems, one in the cytoplasm and one in the mitochondria. Mitochondrial translation is crucial for maintaining mitochondrial function and mutations in this system lead to a breakdown in the respiratory chain-oxidative phosphorylation system and to impaired maintenance of mitochondrial DNA. This gene encodes one of the mitochondrial translation elongati…
- **Diseases (Open Targets)**: hepatoencephalopathy due to combined oxidative phosphorylation defect type 1 (0.822); neurodegenerative disease (0.463); combined oxidative phosphorylation deficiency (0.451); hereditary disease (0.341); Leigh syndrome (0.313)
- **Europe PMC papers**: 1380
- **Why important**: GFM1 is a mitochondrial translation elongation factor rather than a structural ribosomal protein, giving it functional importance at the level of translation execution. It connects strongly to both mitochondrial ribosomal subunits and TUFM in STRING and is present in the primary mitochondrial translation and mitochondrial matrix terms (GO:BP mitochondrial translation; q_global = 5.5e-05), (GO:BP mitochondrial gene expression; q_global = 0.000587), (GO:CC mitochondrial matrix; q_global = 0.0247), and (GO:CC mitochondrion; q_global = 0.0382), as well as the supplementary translation terms (STRING RCTM Mitochondrial translation elongation; within-query FDR = 1.39e-06), (STRING Process Mitochondrial translation; within-query FDR = 5.88e-05), and (STRING Process Peptide biosynthetic process; within-query FDR = 0.0018) through (STRING Process Amide biosynthetic process; within-query FDR = 0.0018). Its established disease associations with combined oxidative-phosphorylation deficiency, hepatoencephalopathy, and Leigh syndrome provide strong biological relevance to respiratory-chain maintenance. Its literature volume is substantial, supporting a well-characterized function.
- **Conclusion**: Established evidence supports GFM1 as an operational bottleneck or functional readout of mitochondrial translation capacity within the module. The module is consistent with coordinated respiratory-protein synthesis involving GFM1. Whether altered GFM1 activity explains the cross-tissue co-abundance pattern is not established.

#### TUFM

- **Related proteins** (co-abundance neighbors): GANAB (0.88), FH (0.82); STRING partners: GFM1 (0.965), MRPL2 (0.998), MRPL27 (0.999), MRPL50 (0.902), MRPS22 (0.988), MRPS27 (0.943), MRPS31 (0.917), MRPS33 (0.913), MRPS35 (0.94)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Tu translation elongation factor, mitochondrial. This gene encodes a protein which participates in protein translation in mitochondria. Mutations in this gene have been associated with combined oxidative phosphorylation deficiency resulting in lactic acidosis and fatal encephalopathy. A pseudogene has been identified on chromosome 17. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 4 (0.769); neurodegenerative disease (0.502); COVID-19 (0.471); combined oxidative phosphorylation deficiency (0.370); ulcerative colitis (0.303)
- **Europe PMC papers**: 1391
- **Why important**: TUFM is the mitochondrial translation elongation factor that complements GFM1 and is strongly connected to the mitochondrial ribosomal proteins in STRING. It appears in the primary mitochondrial translation, mitochondrial matrix, and mitochondrion annotations (GO:BP mitochondrial translation; q_global = 5.5e-05), (GO:BP mitochondrial gene expression; q_global = 0.000587), (GO:CC mitochondrial matrix; q_global = 0.0247), and (GO:CC mitochondrion; q_global = 0.0382). Its known association with combined oxidative-phosphorylation deficiency and fatal encephalopathy makes it an informative bridge between the module's molecular function and respiratory disease biology. Its mitochondrial localization and substantial literature support strengthen its value as a functional anchor rather than merely a correlated peripheral gene.
- **Conclusion**: Established evidence supports TUFM as a core mitochondrial translation factor and a plausible indicator of respiratory-chain protein-production demand. The data do not demonstrate that TUFM dysfunction is responsible for the shared bone-skin module; that would require perturbation or longitudinal evidence.

#### SUN1

- **Related proteins** (co-abundance neighbors): TCIRG1 (0.88), KIF23 (0.87), MYO1B (0.82), TIMMDC1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Sad1 and UNC84 domain containing 1. This gene is a member of the unc-84 homolog family and encodes a nuclear envelope protein with an Unc84 (SUN) domain. The protein is involved in nuclear anchorage and migration. Alternatively spliced transcript variants have been described. [provided by RefSeq, Jan 2019].
- **Diseases (Open Targets)**: atrial fibrillation (0.471); neurodegenerative disease (0.406); atrial flutter (0.265); Abnormality of the skeletal system (0.263); cardiac arrhythmia (0.251)
- **Europe PMC papers**: 2828
- **Why important**: SUN1 provides a biologically informative connection outside the mitochondrial-ribosome core. It is a nuclear-envelope protein involved in nuclear anchorage and migration, is linked in the module network to TCIRG1, KIF23, MYO1B, and TIMMDC1, and contributes to the globally corrected organelle-inner-membrane annotation (GO:CC organelle inner membrane; q_global = 0.0346). Its established functions include nuclear organization, cell migration, response to mechanical stimulus, and ossification-related biology. It has a comparatively large literature base and disease associations involving skeletal abnormalities and neurodegenerative or cardiac phenotypes. Its presence suggests that the module may couple mitochondrial state to cell architecture or mechanical behavior.
- **Conclusion**: Established evidence supports SUN1 as a nuclear-envelope and cellular-architecture component that may connect the mitochondrial program to cell organization. Its proposed role as a mediator between mitochondrial activity and bone-skin mechanical or regenerative biology is a hypothesis rather than a demonstrated mechanism.

## Module 6

**Tissue pair**: bone and skin  
**Genes (46)**: AFDN, ATP1B1, BAG2, CAVIN1, CPSF6, CTNNA1, HSD17B11, DHFR, ECE1, EPHA2, ERBIN, EZR, FAR1, FXR1, KPNA2, MKI67, MAN2A1, LEMD3, MAPRE2, MCM2, MCM4, MCM5, MCM6, MCM7, MDC1, MICALL1, MRC2, NUCB1, NUDT4, NUSAP1, REXO2, PSIP1, PSPC1, RAI14, RPP38, SLC12A7, SAMHD1, SCFD1, SYNGR2, SPTLC2, SRRT, TWSG1, UTRN, VCL, YES1, ZWINT

### Function

The primary functional signal is a DNA replication and replication-fork module centered on the MCM helicase complex. The same five MCM genes support the MCM complex and DNA replication preinitiation and CMG complexes (GO:CC MCM complex; q_global = 3.39e-05), regulation and initiation of DNA-templated replication (GO:BP regulation of DNA-templated DNA replication initiation; q_global = 0.000136) (GO:BP regulation of DNA-templated DNA replication; q_global = 0.000358) (GO:BP DNA replication initiation; q_global = 0.00875), break-induced replication repair (GO:BP double-strand break repair via break-induced replication; q_global = 0.000358), multiple DNA-helicase activities (7 globally significant GO/KEGG terms, q_global 0.0105–0.0456; see the table), and the human DNA-replication pathway (KEGG DNA replication - Homo sapiens (human); q_global = 0.0287). Thus, the strongest interpretation is coordinated abundance of replication-licensing and replication-fork machinery. The presence of NUSAP1, ZWINT, MKI67, MAPRE2, and DHFR is consistent with a proliferative or progenitor-cell context, while CTNNA1, AFDN, VCL, EZR, EPHA2, and related genes indicate an additional cell-junction, cytoskeletal, and epithelial-state component. The globally corrected evidence supports the replication interpretation; the other functional interpretations are contextual rather than globally enriched.

**Cell composition.** This is not a module dominated by plasma or secreted proteins: HPA identifies only a small minority as secreted, including TWSG1 and NUCB1. Most genes have low tissue specificity, and many are cell-type enhanced rather than restricted to bone or skin. Bone-marrow and lymphoid enrichment is prominent, and several genes are enhanced in progenitor or proliferative cell types. Blood-cell specificity is generally low, although selected genes show enhancement or enrichment in basophils, neutrophils, T-reg cells, NK cells, plasmacytoid dendritic cells, or progenitor populations. Skin protein detection is widespread among the assayed genes, whereas the bone protein comparison has no matching HPA tissue result. Consequently, the shared bone-skin signal could reflect a common proliferative or progenitor-cell state, shared resident cell types, or blood and marrow-related contributions in the samples, rather than a tissue-specific extracellular program.

**GO/KEGG enrichment**: 15 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC MCM complex | 3.39e-05 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication initiation | 0.000136 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP double-strand break repair via break-induced replication | 0.000358 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication | 0.000358 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC DNA replication preinitiation complex | 0.00143 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC CMG complex | 0.00143 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP DNA replication initiation | 0.00875 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded DNA binding | 0.0105 | MCM2, MCM4, MCM5, MCM6, MCM7, SAMHD1 |
| GO:MF four-way junction helicase activity | 0.0122 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF forked DNA-dependent helicase activity | 0.0122 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF double-stranded DNA helicase activity | 0.0166 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF 3'-5' DNA helicase activity | 0.0166 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded 3'-5' DNA helicase activity | 0.0166 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| KEGG DNA replication - Homo sapiens (human) | 0.0287 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded DNA helicase activity | 0.0456 | MCM2, MCM4, MCM5, MCM6, MCM7 |

### STRING and hu.MAP

STRING provides direct high-confidence support for the MCM2-MCM4-MCM5-MCM6-MCM7 clique, with the clique annotated as the MCM complex and CMG-related machinery (4 supplementary STRING terms; within-query FDR 0.00065–0.0026). Its conserved MCM domains and sites are also supported (7 supplementary STRING terms; within-query FDR 0.00094–0.0034), together with replication-stress, prereplicative-complex, DNA-unwinding, and break-induced-replication annotations (4 supplementary STRING terms; within-query FDR 0.0072–0.0074). STRING additionally supports known relationships among AFDN, CTNNA1, and VCL; EZR-VCL; CPSF6, PSPC1, and SRRT; MAPRE2-MCM6; and the proliferative genes NUSAP1, MKI67, and ZWINT. hu.MAP independently recovers the MCM proteins in multiple replication-related complexes, including complexes containing MCM3, CDC45, GINS proteins, TIMELESS, TIPIN, CLSPN, and MCMBP (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_08848.1). It also supports smaller complexes involving MDC1 and MICALL1, ECE1 and MAN2A1, KPNA2 and NUSAP1, MRC2 and SLC12A7, PSIP1 and PSPC1, and CAVIN1 and SCFD1 (hu.MAP huMAP3_05266.1) (hu.MAP huMAP3_06468.1) (hu.MAP huMAP3_08802.1) (hu.MAP huMAP3_10000.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_10848.1) (hu.MAP huMAP3_14270.1) (hu.MAP huMAP3_09336.1) (hu.MAP huMAP3_12042.1) (hu.MAP huMAP3_12581.1) (hu.MAP huMAP3_06775.1) (hu.MAP huMAP3_11349.1) (hu.MAP huMAP3_09327.1). These results indicate that the module contains a well-established replication-complex core plus several weaker or indirect co-abundance neighborhoods. The known MCM and adhesion relationships validate the biological coherence of important parts of the network, but do not establish a direct physical interaction between every co-abundant gene pair.

**STRING interactions (score >= 0.7)**: 20 of 1035 gene pairs: AFDN–CTNNA1 (0.984); AFDN–VCL (0.849); CPSF6–PSPC1 (0.748); CPSF6–SRRT (0.732); CTNNA1–VCL (0.999); EZR–VCL (0.979); MAPRE2–MCM6 (0.846); MCM2–MCM4 (0.999); MCM2–MCM5 (0.999); MCM2–MCM6 (0.999); MCM2–MCM7 (0.999); MCM4–MCM5 (0.999); MCM4–MCM6 (0.999); MCM4–MCM7 (0.999); MCM5–MCM6 (0.999); MCM5–MCM7 (0.999); MCM6–MCM7 (0.999); MKI67–NUSAP1 (0.943); MKI67–ZWINT (0.894); NUSAP1–ZWINT (0.902)
**STRING functional enrichment (supplementary, within-query FDR)**: Component MCM complex (FDR = 0.00065, 5 genes); COMPARTMENTS MCM complex (FDR = 0.0007, 5 genes); InterPro MCM domain (FDR = 0.00094, 5 genes); InterPro Mini-chromosome maintenance, conserved site (FDR = 0.00094, 5 genes); InterPro MCM N-terminal domain (FDR = 0.00094, 5 genes); InterPro Mini-chromosome maintenance protein (FDR = 0.00094, 5 genes); InterPro MCM OB domain (FDR = 0.00094, 5 genes); InterPro MCM, AAA-lid domain (FDR = 0.00094, 5 genes); Component CMG complex (FDR = 0.0024, 5 genes); COMPARTMENTS CMG complex (FDR = 0.0026, 5 genes); Pfam MCM N-terminal domain (FDR = 0.0034, 4 genes); RCTM Activation of ATR in response to replication stress (FDR = 0.0072, 5 genes); RCTM Unwinding of DNA (FDR = 0.0072, 5 genes); RCTM Activation of the pre-replicative complex (FDR = 0.0072, 5 genes); Process Double-strand break repair via break-induced replication (FDR = 0.0074, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05529.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/6); huMAP3_14758.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/14); huMAP3_08554.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_11832.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_12180.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/17); huMAP3_06061.1 (MCM4, MCM7, MCM2, MCM6; 4/5); huMAP3_07113.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_11119.1 (MCM4, MCM5, MCM7, MCM6; 4/14); huMAP3_09860.1 (MCM4, MCM2, MCM6; 3/4); huMAP3_00154.1 (MCM4, MCM2, MCM6; 3/5); huMAP3_09466.1 (MCM4, MCM2, MCM6; 3/23); huMAP3_10862.1 (MCM4, MCM2, MCM6; 3/33); huMAP3_14306.1 (MCM4, MCM2, MCM6; 3/55); huMAP3_02602.1 (MCM4, MCM6; 2/2); huMAP3_05266.1 (MDC1, MICALL1; 2/5); huMAP3_06468.1 (MDC1, MICALL1; 2/6); huMAP3_09238.1 (MCM5, MCM7; 2/11); huMAP3_08848.1 (MCM4, MCM6; 2/15); huMAP3_08802.1 (ECE1, MAN2A1; 2/33); huMAP3_10000.1 (KPNA2, NUSAP1; 2/44); huMAP3_10980.1 (MRC2, SLC12A7; 2/44); huMAP3_10848.1 (MRC2, SLC12A7; 2/46); huMAP3_14270.1 (PSIP1, PSPC1; 2/47); huMAP3_09336.1 (MRC2, SLC12A7; 2/50); huMAP3_12042.1 (CAVIN1, SCFD1; 2/56); huMAP3_12581.1 (KPNA2, NUSAP1; 2/58); huMAP3_06775.1 (ECE1, MAN2A1; 2/60); huMAP3_11349.1 (MRC2, SLC12A7; 2/78); huMAP3_09327.1 (ECE1, MAN2A1; 2/93)

### Novelty

The replication machinery itself is not a new biological finding: the MCM complex, replication initiation, helicase activity, and associated cell-cycle relationships are already well established by STRING, hu.MAP, and the gene literature. The shared co-abundance of this combination across bone and skin may nevertheless be a new observation in this dataset, particularly because the module joins an MCM replication core with junction, cytoskeletal, membrane-trafficking, and extracellular-matrix-related genes. That observation should be treated as a dataset-level association rather than a newly discovered molecular complex. Absence of some genes or edges from STRING or hu.MAP does not demonstrate novelty; it may reflect incomplete databases, context dependence, tissue composition, or co-regulation without direct physical binding. A genuine novel claim would require independent replication across cohorts and experimental testing of the proposed cross-tissue regulatory relationship.

**Hypothesis.** Hypothesis: the conserved bone-skin module reflects a shared abundance program of cycling or progenitor-like cells. In this model, MCM2, MCM4, MCM5, MCM6, and MCM7 provide the replication-licensing and helicase core, while NUSAP1, ZWINT, MKI67, MAPRE2, and DHFR mark associated cell-cycle activity. The co-abundance of CTNNA1, AFDN, VCL, EZR, EPHA2, MRC2, and SLC12A7 could reflect coupling of proliferation to cell adhesion, cytoskeletal organization, membrane transport, and extracellular-matrix handling in the shared cellular environment. TWSG1 and LEMD3 provide a possible BMP or TGF-beta-related context, but their co-abundance does not demonstrate pathway coupling. This model predicts that the module will be strongest in proliferating basal, stromal, marrow, or progenitor populations and will diminish after careful removal of blood-cell and cell-composition effects.

### Important genes

#### MCM2

- **Related proteins** (co-abundance neighbors): MCM6 (0.86), YES1 (0.86), MCM7 (0.85), SLC12A7 (0.83), TWSG1 (0.83); STRING partners: MCM4 (0.999), MCM5 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a central member of the MCM replication core, has direct STRING links to MCM4, MCM5, MCM6, and MCM7, and participates in the globally corrected replication, helicase, preinitiation, CMG, and break-induced-replication terms (15 globally significant GO/KEGG terms, q_global 3.39e-05–0.0456; see the table). It is also present in many hu.MAP replication complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1). Its HPA pattern is enhanced in bone marrow and lymphoid tissue and in multiple progenitor populations, making it informative for distinguishing a genuine tissue program from a proliferative or cellular-composition signal. Its disease associations and extensive literature make it a well-established anchor gene rather than a speculative marker.
- **Conclusion**: Established evidence supports MCM2 as a core replication-licensing component and a principal driver of the module's functional annotation. Its abundance is compatible with proliferating progenitor cells in bone and skin, but the module alone cannot establish that MCM2 causes the cross-tissue association.

#### MCM6

- **Related proteins** (co-abundance neighbors): SLC12A7 (0.94), MCM4 (0.89), MCM2 (0.86), ERBIN (0.81); STRING partners: MAPRE2 (0.846), MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 6. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: lactose intolerance (0.246); neurodegenerative disease (0.225); obesity disorder (0.166); nervous system disorder (0.141); systemic lupus erythematosus (0.140)
- **Europe PMC papers**: 3766
- **Why important**: MCM6 is a core MCM component with strong STRING connectivity to the other MCM genes and an additional relationship to MAPRE2. It occurs across numerous hu.MAP replication complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_08848.1) and contributes to every globally corrected MCM-centered enrichment term (15 globally significant GO/KEGG terms, q_global 3.39e-05–0.0456; see the table). Its HPA profile includes lymphoid tissue and hematopoietic progenitor populations, while its network position connects the replication core to SLC12A7 and ERBIN. Its established role in replication initiation, DNA metabolism, and replication-associated repair, together with substantial literature and disease annotation, makes it a strong bridge gene.
- **Conclusion**: Established evidence identifies MCM6 as both a replication-complex component and a possible network bridge toward membrane or cell-state genes. The bridge interpretation is a hypothesis based on co-abundance topology; a direct regulatory or physical link to SLC12A7 or ERBIN is not established here.

#### NUSAP1

- **Related proteins** (co-abundance neighbors): MCM5 (0.87), REXO2 (0.85), EPHA2 (0.84), AFDN (0.83), CTNNA1 (0.81), ATP1B1 (0.80); STRING partners: MKI67 (0.943), ZWINT (0.902)
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Nucleoplasm, Nucleoli, Nucleoli fibrillar center; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_10000.1, huMAP3_12581.1
- **Function (MyGene.info)**: nucleolar and spindle associated protein 1. NUSAP1 is a nucleolar-spindle-associated protein that plays a role in spindle microtubule organization (Raemaekers et al., 2003 [PubMed 12963707]).[supplied by OMIM, Jun 2009].
- **Diseases (Open Targets)**: microcephaly, seizures, and developmental delay (0.266); hepatocellular carcinoma (0.121); neoplasm (0.116); central nervous system cancer (0.107); cancer (0.107)
- **Europe PMC papers**: 3308
- **Why important**: NUSAP1 links the module to mitotic spindle organization, chromosome segregation, and cytokinesis. It has high-confidence STRING relationships with MKI67 and ZWINT and connects in the module to MCM5, REXO2, EPHA2, AFDN, CTNNA1, and ATP1B1. hu.MAP places it with KPNA2 in nuclear transport-related complexes (hu.MAP huMAP3_10000.1) (hu.MAP huMAP3_12581.1). HPA identifies enrichment in bone marrow and lymphoid tissue and in progenitor or proliferative cell types. Its extensive literature and associations with developmental and neoplastic disease support its importance as a marker of cell-cycle state.
- **Conclusion**: Established evidence supports NUSAP1 as a mitotic and proliferative-state indicator that complements the replication core. It strengthens the interpretation that cell composition or cycling-cell abundance contributes to the shared module, but it does not prove that NUSAP1 mechanistically coordinates the MCM genes.

#### MRC2

- **Related proteins** (co-abundance neighbors): AFDN (0.89), ERBIN (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_10980.1, huMAP3_10848.1, huMAP3_09336.1, huMAP3_11349.1
- **Function (MyGene.info)**: mannose receptor C-type 2. This gene encodes a member of the mannose receptor family of proteins that contain a fibronectin type II domain and multiple C-type lectin-like domains. The encoded protein plays a role in extracellular matrix remodeling by mediating the internalization and lysosomal degradation of collagen ligands. Expression of this gene may play a role in the tumorigenesis and metastasis of several malignancies…
- **Diseases (Open Targets)**: abdominal aortic aneurysm (0.448); aortic aneurysm (0.396); aneurysm (0.393); type 2 diabetes mellitus (0.323); hypertensive disorder (0.321)
- **Europe PMC papers**: 1288
- **Why important**: MRC2 provides a tissue-relevant extracellular and matrix-remodeling connection. It mediates collagen-ligand internalization and lysosomal degradation and is annotated for osteoblast differentiation and collagen catabolism. In the module it connects to AFDN and ERBIN, while hu.MAP places it with SLC12A7 in several membrane or cell-state complexes (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_10848.1) (hu.MAP huMAP3_14270.1) (hu.MAP huMAP3_09336.1) (hu.MAP huMAP3_11349.1). HPA detects it in skin and in cell types including fibro-adipogenic progenitors, and it has disease associations involving vascular and metabolic disorders. Its literature is substantial relative to many peripheral module genes.
- **Conclusion**: Established evidence supports MRC2 as a matrix-remodeling and osteoblast-related component that may help explain why a replication-associated program is shared between bone and skin. The proposed connection between MRC2 and the MCM-centered program remains a co-abundance hypothesis rather than a demonstrated molecular mechanism.

#### CTNNA1

- **Related proteins** (co-abundance neighbors): NUSAP1 (0.81), TWSG1 (0.80); STRING partners: AFDN (0.984), VCL (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin alpha 1. This gene encodes a member of the catenin family of proteins that play an important role in cell adhesion process by connecting cadherins located on the plasma membrane to the actin filaments inside the cell. The encoded mechanosensing protein contains three vinculin homology domains and undergoes conformational changes in response to cytoskeletal tension, resulting in the reconfiguration of cadhe…
- **Diseases (Open Targets)**: Butterfly-shaped pigment dystrophy (0.750); hereditary neoplastic syndrome (0.557); hereditary diffuse gastric adenocarcinoma (0.555); colorectal cancer (0.506); exudative vitreoretinopathy (0.390)
- **Europe PMC papers**: 2688
- **Why important**: CTNNA1 is a cell-junction and mechanosensing gene that connects cadherin complexes to actin. It is linked in STRING to AFDN and VCL, with strong support for the adhesion neighborhood, and is connected in the module to NUSAP1 and TWSG1. HPA places it in esophageal apical cells and detects it in skin. Its established roles in cell adhesion, migration, gap-junction assembly, and cytoskeletal tension, together with substantial literature and disease associations involving pigmentary and epithelial disorders, make it a useful representative of the module's structural arm.
- **Conclusion**: Established evidence supports CTNNA1 as an adhesion and mechanotransduction component that may reflect epithelial or stromal architecture in skin and bone samples. Its relationship to the replication core is best regarded as a hypothesis about coordinated cellular state, not as evidence that CTNNA1 directly regulates DNA replication.

## Module 7

**Tissue pair**: bone and skin  
**Genes (40)**: PGM3, ASCC3, CDC73, CNOT12, CPSF7, DIDO1, DPYSL3, FAF1, FLNC, FRYL, GMPPA, GNL1, GOPC, HDAC2, HSPA13, IPO4, LACTB, LTA4H, METAP1, MAP1A, MAP1B, MAP1S, MAPKAPK3, NAA50, NME7, POMP, PTK7, PFAS, RBM12, SEC23IP, SNTB2, SPAG5, TCP11L1, TCEA1, UAP1, USO1, UTP20, WIPF2, YLPM1, ZNF638

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. The module therefore does not support a single statistically established pathway assignment. Its strongest interpretable themes are a cytoskeletal and microtubule-associated component, represented by MAP1A, MAP1B, MAP1S, DPYSL3, FLNC and NME7; RNA processing and transcriptional control, represented by YLPM1, ZNF638, RBM12, TCEA1, CDC73 and CPSF7; and metabolic or trafficking functions involving glycan precursor synthesis, vesicle transport and proteostasis. The network is sparse, with MAP1A acting as the main connectivity hub and several smaller branches. These observations support a broad cellular-organization module rather than a dedicated bone or skin pathway. The functional interpretation remains hypothesis-generating because no GO/KEGG term achieved global significance.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only a small minority are annotated as secreted, and most genes have low tissue specificity. HPA annotations show mixtures of muscle, neuronal, reproductive, epithelial and immune-cell-associated signals, including recurring associations with skeletal muscle, myonuclei, spermatocytes, neutrophils and photoreceptor cells. Most genes have low immune-cell specificity, although a subset is enriched or enhanced in neutrophils, basophils, plasmacytoid dendritic cells or T-regulatory cells. Thus, a blood-cell explanation is possible for part of the signal but is not the dominant interpretation. The shared bone-skin module could instead reflect broadly expressed cellular machinery, shared stromal or vascular cell types, or sample-composition effects. Protein detection is available for skin for many members, whereas the bone comparison has no matching HPA tissue protein dataset; this limits tissue-specific interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

Known relationships are limited but informative. STRING supports CDC73-TCEA1, GMPPA-PGM3 and PGM3-UAP1 as high-confidence interactions. These links define small, already recognized transcriptional and glycan-biosynthetic neighborhoods, but they do not explain the entire module. hu.MAP repeatedly places MAP1A with MAP1B or MAP1S in partial complexes (hu.MAP huMAP3_10774.1), (hu.MAP huMAP3_10983.1), (hu.MAP huMAP3_10317.1), (hu.MAP huMAP3_09907.1) and (hu.MAP huMAP3_10305.1). It also repeatedly places YLPM1 with ZNF638 in RNA-associated complexes (hu.MAP huMAP3_02281.1) through (hu.MAP huMAP3_10098.1), places TCEA1 with RBM12 in larger transcription- or translation-associated assemblies (hu.MAP huMAP3_10302.1), (hu.MAP huMAP3_10088.1) and (hu.MAP huMAP3_14982.1), and places LTA4H with UAP1 in a broad complex (hu.MAP huMAP3_14442.1). Because these complexes contain only subsets of module genes, and several are large or lower-confidence assemblies, they support pre-existing molecular neighborhoods rather than a demonstrated physical complex containing the whole module. The sparse STRING graph and partial hu.MAP overlap suggest that co-abundance adds a tissue-level relationship beyond the set of already catalogued direct interactions.

**STRING interactions (score >= 0.7)**: 3 of 780 gene pairs: CDC73–TCEA1 (0.96); GMPPA–PGM3 (0.795); PGM3–UAP1 (0.997)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10774.1 (MAP1B, MAP1A; 2/4); huMAP3_10983.1 (MAP1B, MAP1A; 2/4); huMAP3_10317.1 (MAP1B, MAP1S; 2/4); huMAP3_09907.1 (MAP1B, MAP1A; 2/5); huMAP3_10305.1 (MAP1B, MAP1A; 2/5); huMAP3_02281.1 (YLPM1, ZNF638; 2/5); huMAP3_08667.1 (YLPM1, ZNF638; 2/5); huMAP3_06755.1 (YLPM1, ZNF638; 2/6); huMAP3_08625.1 (YLPM1, ZNF638; 2/6); huMAP3_09844.1 (YLPM1, ZNF638; 2/6); huMAP3_01533.1 (YLPM1, ZNF638; 2/7); huMAP3_06354.1 (YLPM1, ZNF638; 2/7); huMAP3_10302.1 (TCEA1, RBM12; 2/9); huMAP3_08096.1 (YLPM1, ZNF638; 2/9); huMAP3_09569.1 (YLPM1, ZNF638; 2/9); huMAP3_10088.1 (TCEA1, RBM12; 2/10); huMAP3_07030.1 (YLPM1, ZNF638; 2/10); huMAP3_08950.1 (YLPM1, ZNF638; 2/10); huMAP3_09973.1 (YLPM1, ZNF638; 2/10); huMAP3_10643.1 (YLPM1, ZNF638; 2/13); huMAP3_09895.1 (YLPM1, ZNF638; 2/14); huMAP3_09778.1 (YLPM1, ZNF638; 2/16); huMAP3_10098.1 (YLPM1, ZNF638; 2/17); huMAP3_14982.1 (TCEA1, RBM12; 2/28); huMAP3_10150.1 (ZNF638, FAF1; 2/38); huMAP3_14442.1 (LTA4H, UAP1; 2/57)

### Novelty

The module-level finding may be new because the co-abundance relationship across bone and skin is not established by the supplied interaction resources, and the genes do not form a single canonical STRING-enriched pathway or complete hu.MAP complex. However, it would be incorrect to call the biology entirely novel: the MAP1A-MAP1B and MAP1A-MAP1S associations, the PGM3-UAP1 and GMPPA-PGM3 relationships, and the TCEA1-CDC73 relationship are already represented in established resources. The appropriate conclusion is that the cross-tissue co-abundance pattern is potentially novel, while its component molecular functions and several local relationships are established. Direct comparison against prior bone-skin co-abundance studies would be required before claiming a definitive new finding.

**Hypothesis.** Hypothesis: the module represents a shared cellular state in which cytoskeletal organization and polarity are coordinated with transcriptional and RNA-processing capacity, vesicle trafficking, proteostasis and glycan precursor metabolism. MAP1A and MAP1B may mark the structural arm, PTK7 and associated membrane or trafficking proteins may connect polarity and adhesion signals, and PGM3-UAP1-GMPPA may support glycan-related biosynthetic demand. The co-abundance pattern may therefore arise from shared stromal, vascular, epithelial or other structural cell populations, or from tissue remodeling, rather than from a bone-skin-specific biochemical pathway. This hypothesis should be tested with cell-resolved expression, independent cohorts and perturbation experiments; the current data do not establish causality or direct physical coupling among all of these processes.

### Important genes

#### MAP1A

- **Related proteins** (co-abundance neighbors): YLPM1 (0.95), PGM3 (0.90), PFAS (0.89), MAP1B (0.89), CNOT12 (0.87), GMPPA (0.85), ASCC3 (0.85), ZNF638 (0.85), UTP20 (0.84), GNL1 (0.84), USO1 (0.83), MAP1S (0.83), HDAC2 (0.83), IPO4 (0.82), LTA4H (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10774.1, huMAP3_10983.1, huMAP3_09907.1, huMAP3_10305.1
- **Function (MyGene.info)**: microtubule associated protein 1A. This gene encodes a protein that belongs to the microtubule-associated protein family. The proteins of this family are thought to be involved in microtubule assembly, which is an essential step in neurogenesis. The product of this gene is a precursor polypeptide that presumably undergoes proteolytic processing to generate the final MAP1A heavy chain and LC2 light chain. Expression of this gene is …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.340); venous thromboembolism (0.238); hereditary disease (0.118); autism spectrum disorder (0.094); urinary bladder cancer (0.075)
- **Europe PMC papers**: 1240
- **Why important**: MAP1A is the principal network hub in the supplied subgraph and connects to multiple branches, including YLPM1, PGM3, PFAS, MAP1B, GMPPA and ZNF638. It encodes a microtubule-associated protein involved in microtubule assembly and neuronal cytoskeletal organization. Its brain-enriched HPA profile and substantial literature support make it the clearest structural anchor of the module. It also recurs with MAP1B in several hu.MAP complexes (hu.MAP huMAP3_10774.1), (hu.MAP huMAP3_10983.1), (hu.MAP huMAP3_09907.1) and (hu.MAP huMAP3_10305.1).
- **Conclusion**: Established: MAP1A is a microtubule-associated protein, a prominent module hub, and a repeated member of hu.MAP assemblies with MAP1B. Established disease associations include neurodevelopmental and neuropsychiatric conditions in the supplied evidence. Hypothesis: its centrality may reflect a shared cytoskeletal or cell-state program linking otherwise diverse module branches, but this does not demonstrate a bone- or skin-specific role.

#### MAP1B

- **Related proteins** (co-abundance neighbors): MAP1A (0.89), NME7 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_10774.1, huMAP3_10983.1, huMAP3_10317.1, huMAP3_09907.1, huMAP3_10305.1
- **Function (MyGene.info)**: microtubule associated protein 1B. This gene encodes a protein that belongs to the microtubule-associated protein family. The proteins of this family are thought to be involved in microtubule assembly, which is an essential step in neurogenesis. The product of this gene is a precursor polypeptide that presumably undergoes proteolytic processing to generate the final MAP1B heavy chain and LC1 light chain. Gene knockout studies of th…
- **Diseases (Open Targets)**: periventricular nodular heterotopia 9 (0.762); hearing loss, autosomal dominant 83 (0.547); neurodegenerative disease (0.538); periventricular nodular heterotopia (0.522); hereditary disease (0.496)
- **Europe PMC papers**: 3710
- **Why important**: MAP1B provides an independent cytoskeletal anchor and connects MAP1A with NME7. It is annotated for microtubule organization, microtubule bundling, neuron migration and axonogenesis, and it is repeatedly represented with MAP1A or MAP1S in hu.MAP complexes (hu.MAP huMAP3_10774.1) through (hu.MAP huMAP3_10305.1). Its tissue-enhanced profile includes blood vessel, brain and retina, while it is detected in skin.
- **Conclusion**: Established: MAP1B has a well-supported role in microtubule organization and participates in recognized complexes with MAP1A and MAP1S. Established disease associations include neurodevelopmental and hereditary neurological disorders. Hypothesis: MAP1B may help explain the module's cross-tissue conservation through cytoskeletal requirements shared by vascular, stromal and epithelial cells, but the co-abundance data do not prove that it drives the module.

#### PGM3

- **Related proteins** (co-abundance neighbors): MAP1A (0.90); STRING partners: GMPPA (0.795), UAP1 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglucomutase 3. This gene encodes a member of the phosphohexose mutase family. The encoded protein mediates both glycogen formation and utilization by catalyzing the interconversion of glucose-1-phosphate and glucose-6-phosphate. A non-synonymous single nucleotide polymorphism in this gene may play a role in resistance to diabetic nephropathy and neuropathy. Alternatively spliced transcript variants encoding mult…
- **Diseases (Open Targets)**: immunodeficiency 23 (0.838); severe combined immunodeficiency (0.643); combined immunodeficiency (0.465); hyper-IgE syndrome (0.457); hereditary disease (0.415)
- **Europe PMC papers**: 1095
- **Why important**: PGM3 identifies a distinct metabolic branch. It is connected in STRING to UAP1 with very strong support and to GMPPA with substantial support, while its annotated functions include carbohydrate metabolism, UDP-N-acetylglucosamine production and protein glycosylation. Its disease associations include immunodeficiency and severe combined immunodeficiency, giving it clear biological and clinical relevance despite its limited direct connectivity in the co-abundance graph.
- **Conclusion**: Established: PGM3 participates in carbohydrate and glycan precursor metabolism, and its local STRING relationships with UAP1 and GMPPA are known. Established disease evidence links PGM3 to immunodeficiency phenotypes. Hypothesis: coordinated abundance of PGM3 with cytoskeletal and transcriptional genes may indicate biosynthetic support for remodeling or cell-surface protein production, but the module does not establish that glycosylation is its primary function.

#### PTK7

- **Related proteins** (co-abundance neighbors): SNTB2 (0.91), NAA50 (0.83), METAP1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein tyrosine kinase 7 (inactive). This gene encodes a member of the receptor protein tyrosine kinase family of proteins that transduce extracellular signals across the cell membrane. The encoded protein lacks detectable catalytic tyrosine kinase activity, is involved in the Wnt signaling pathway and plays a role in multiple cellular processes including polarity and adhesion. Alternatively spliced transcript variants encoding multi…
- **Diseases (Open Targets)**: neurodegenerative disease (0.319); coronary artery disorder (0.309); asthma (0.267); neoplasm (0.118); esophageal squamous cell carcinoma (0.112)
- **Europe PMC papers**: 2106
- **Why important**: PTK7 is an inactive receptor-type tyrosine kinase involved in Wnt signaling, cell polarity, adhesion, migration and actin organization. Its network links connect it to SNTB2, NAA50 and METAP1, providing a membrane-associated interface between signaling, cytoskeletal organization and protein maturation. HPA places it at the plasma membrane and reports secretion to blood, while its literature and disease-association record are substantial.
- **Conclusion**: Established: PTK7 is a catalytically inactive signaling receptor with roles in polarity, adhesion, migration and cytoskeletal organization. Established disease associations include neurodegenerative, coronary and airway disorders in the supplied evidence. Hypothesis: PTK7 could connect extracellular or membrane cues to the structural portion of the module in skin or stromal cells, but the available network does not establish a direct PTK7 interaction with the module hub.

#### CDC73

- **Related proteins** (co-abundance neighbors): LACTB (0.80); STRING partners: TCEA1 (0.96)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell division cycle 73. This gene encodes a tumor suppressor that is involved in transcriptional and post-transcriptional control pathways. The protein is a component of the the PAF protein complex, which associates with the RNA polymerase II subunit POLR2A and with a histone methyltransferase complex. This protein appears to facilitate the association of 3' mRNA processing factors with actively-transcribed chromatin. Mu…
- **Diseases (Open Targets)**: hyperparathyroidism 2 with jaw tumors (0.810); parathyroid gland carcinoma (0.802); familial isolated hyperparathyroidism (0.738); hyperparathyroidism (0.599); hereditary neoplastic syndrome (0.555)
- **Europe PMC papers**: 2210
- **Why important**: CDC73 is linked by STRING to TCEA1, forming the module's clearest known transcription-elongation neighborhood. It encodes a tumor suppressor involved in transcriptional and post-transcriptional control, RNA polymerase association, stem-cell maintenance and Wnt regulation. Its skin protein detection and strong disease associations, especially hyperparathyroidism-jaw tumor syndromes and parathyroid carcinoma, make it important for interpreting a module shared with bone-related tissue.
- **Conclusion**: Established: CDC73 participates in transcriptional control and is a recognized disease gene for hyperparathyroidism and jaw-tumor syndromes; its relationship with TCEA1 is supported by STRING. Hypothesis: the CDC73-TCEA1 branch may reflect transcriptional state or tissue remodeling associated with the shared module, but it does not establish a causal link between this module and skeletal disease.

## Module 8

**Tissue pair**: bone and skin  
**Genes (16)**: ANLN, CCNB1, ERCC6L, FBXL18, HMMR, KIF11, KIFC1, MED20, PAK1, PHLDB2, RBM7, RFC3, SYNJ2BP, UBE2T, UHRF1, WAPL

### Function

The primary, globally corrected evidence supports a mitotic nuclear-division module (GO:BP mitotic nuclear division; q_global = 0.0169)(GO:BP nuclear division; q_global = 0.0385). Its genes converge on spindle assembly and dynamics, chromosome positioning, sister-chromatid segregation, cytokinesis, and cell-cycle control. The STRING supplementary evidence independently reinforces kinetochore activity, spindle elongation, Polo-like-kinase-associated events, mitosis, and cell-cycle biology (STRING NetworkNeighborAL Mixed, incl. Amplification of signal from the kinetochores, and Mitotic sister chromatid segregation; within-query FDR = 0.0008)(STRING NetworkNeighborAL Mixed, incl. Spindle elongation, and Polo-like kinase mediated events; within-query FDR = 0.0008)(STRING Keyword Mitosis; within-query FDR = 0.005)(STRING Keyword Cell cycle; within-query FDR = 0.0065). The module therefore most plausibly represents coordinated proliferative cell division rather than a bone- or skin-specific structural program. DNA replication, DNA repair, ubiquitination, RNA processing, and cytoskeletal regulation among individual genes may represent supporting functions or peripheral connections rather than the principal module identity.

**Cell composition.** The module contains no secreted genes. HPA profiles show frequent enrichment in bone marrow and lymphoid tissue and strong enrichment in progenitor cell types, especially erythrocyte, monocyte, and megakaryocyte progenitors. This is consistent with a proliferative progenitor or hematopoietic-cell signal that can be shared across sampled tissues, and it raises the possibility that the apparent bone-skin conservation partly reflects shared cell populations or blood-associated material. Most genes are cell-type enhanced rather than broadly uniform housekeeping genes, although several have low tissue or immune-cell specificity. Skin protein detection is common among the measured genes, but the absence of matching bone protein data limits tissue-level protein comparison. The profile does not support a plasma-protein or secreted-factor interpretation.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP mitotic nuclear division | 0.0169 | ANLN, CCNB1, KIF11, KIFC1, UHRF1, WAPL |
| GO:BP nuclear division | 0.0385 | ANLN, CCNB1, KIF11, KIFC1, UHRF1, WAPL |

### STRING and hu.MAP

The module contains a coherent STRING-supported mitotic core. CCNB1, KIF11, HMMR, ANLN, and KIFC1 have multiple high-confidence relationships that align with spindle and cytokinesis biology; UHRF1, ERCC6L, WAPL, and UBE2T connect cell division with chromatin, DNA-damage, or ubiquitin-related processes. The STRING enrichment terms are supplementary and not global enrichment evidence, but they are mechanistically concordant with (GO:BP mitotic nuclear division; q_global = 0.0169) and (GO:BP nuclear division; q_global = 0.0385). hu.MAP reports no complex containing at least two module members, so the module is not supported as a previously catalogued hu.MAP complex. STRING relationships indicate that much of the central biology is already known, while the co-abundance organization and some peripheral connections may still be informative.

**STRING interactions (score >= 0.7)**: 13 of 120 gene pairs: ANLN–CCNB1 (0.86); ANLN–HMMR (0.88); ANLN–KIF11 (0.947); CCNB1–ERCC6L (0.72); CCNB1–HMMR (0.942); CCNB1–KIF11 (0.966); CCNB1–KIFC1 (0.726); CCNB1–UBE2T (0.851); HMMR–KIF11 (0.928); KIF11–KIFC1 (0.963); KIF11–UHRF1 (0.708); RFC3–WAPL (0.783); UBE2T–UHRF1 (0.709)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Mixed, incl. Amplification of signal from the kinetochores, and Mitotic sister chromatid segregation (FDR = 0.0008, 6 genes); NetworkNeighborAL Mixed, incl. Spindle elongation, and Polo-like kinase mediated events (FDR = 0.0008, 5 genes); NetworkNeighborAL Mixed, incl. Spindle elongation, and Polo-like kinase mediated events (FDR = 0.0027, 4 genes); Keyword Mitosis (FDR = 0.005, 6 genes); Keyword Cell cycle (FDR = 0.0065, 7 genes); NetworkNeighborAL Mixed, incl. Spindle elongation, and Outer kinetochore (FDR = 0.0423, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This should not be described as a wholly new mitosis pathway: the principal genes and many of their pairwise relationships are established, and the globally corrected GO evidence gives a familiar biological interpretation. At the same time, the specific conserved co-abundance module across bone and skin is not established by the supplied resources. The lack of a matching hu.MAP complex and the incomplete STRING coverage of the module are compatible with a novel tissue-pair co-abundance configuration, but they do not prove novelty. A defensible claim is therefore contextual novelty: a potentially new cross-tissue organization of known proliferative machinery, requiring replication in independent cohorts and control for cell-composition effects.

**Hypothesis.** Hypothesis: the conserved module reflects synchronized proliferation of progenitor-like cells present in both bone-associated and skin-associated samples. A CCNB1-centered mitotic program may coordinate KIF11- and KIFC1-dependent spindle behavior with HMMR microtubule-associated activity and ANLN-mediated cytokinetic remodeling, while UHRF1, ERCC6L, WAPL, RFC3, and UBE2T help maintain chromosome, replication, and damage-response integrity. PHLDB2 and PAK1 could connect this proliferative state to cortical cytoskeleton, adhesion, migration, and morphology. This hypothesis predicts that module abundance will track proliferating progenitor or cycling-cell abundance and should weaken after careful adjustment for cellular composition.

### Important genes

#### CCNB1

- **Related proteins** (co-abundance neighbors): PHLDB2 (0.87), PAK1 (0.84); STRING partners: ANLN (0.86), ERCC6L (0.72), HMMR (0.942), KIF11 (0.966), KIFC1 (0.726), UBE2T (0.851)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cyclin B1. The protein encoded by this gene is a regulatory protein involved in mitosis. The gene product complexes with p34(cdc2) to form the maturation-promoting factor (MPF). The encoded protein is necessary for proper control of the G2/M transition phase of the cell cycle. [provided by RefSeq, Aug 2017].
- **Diseases (Open Targets)**: neurodegenerative disease (0.300); cardiovascular disorder (0.234); hypertensive disorder (0.209); Abnormality of the skeletal system (0.196); Increased blood pressure (0.161)
- **Europe PMC papers**: 11102
- **Why important**: CCNB1 is a central functional anchor: its annotation directly links it to the G2/M transition, mitotic spindle organization, and chromosome alignment. It has multiple high-confidence STRING relationships and participates in every listed STRING supplementary enrichment that contains the core mitotic signal (STRING NetworkNeighborAL Mixed, incl. Amplification of signal from the kinetochores, and Mitotic sister chromatid segregation; within-query FDR = 0.0008)(STRING NetworkNeighborAL Mixed, incl. Spindle elongation, and Polo-like kinase mediated events; within-query FDR = 0.0008)(STRING NetworkNeighborAL Mixed, incl. Spindle elongation, and Polo-like kinase mediated events; within-query FDR = 0.0027)(STRING Keyword Mitosis; within-query FDR = 0.005)(STRING Keyword Cell cycle; within-query FDR = 0.0065)(STRING NetworkNeighborAL Mixed, incl. Spindle elongation, and Outer kinetochore; within-query FDR = 0.0423). Its high literature volume and disease links make it a well-established marker of proliferative state, while its module position connects it to both spindle machinery and peripheral cytoskeletal genes.
- **Conclusion**: Established evidence supports CCNB1 as a principal indicator and likely driver-associated marker of the module's mitotic program. The co-abundance data do not establish that CCNB1 mechanistically regulates the other module genes in bone or skin; that part remains a hypothesis.

#### ANLN

- **Related proteins** (co-abundance neighbors): PHLDB2 (0.83), HMMR (0.81), PAK1 (0.80); STRING partners: CCNB1 (0.86), HMMR (0.88), KIF11 (0.947)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: anillin, actin binding protein. This gene encodes an actin-binding protein that plays a role in cell growth and migration, and in cytokinesis. The encoded protein is thought to regulate actin cytoskeletal dynamics in podocytes, components of the glomerulus. Mutations in this gene are associated with focal segmental glomerulosclerosis 8. Alternative splicing results in multiple transcript variants encoding different isoforms. [pr…
- **Diseases (Open Targets)**: familial idiopathic steroid-resistant nephrotic syndrome (0.657); focal segmental glomerulosclerosis (0.576); seasonal allergic rhinitis (0.343); alcohol drinking (0.343); prostate carcinoma (0.284)
- **Europe PMC papers**: 2621
- **Why important**: ANLN links the module's spindle-associated core to cytokinesis and the actomyosin contractile ring. It is supported by both globally corrected nuclear-division terms (GO:BP mitotic nuclear division; q_global = 0.0169)(GO:BP nuclear division; q_global = 0.0385) and several STRING mitosis and spindle terms (STRING NetworkNeighborAL Mixed, incl. Amplification of signal from the kinetochores, and Mitotic sister chromatid segregation; within-query FDR = 0.0008)(STRING NetworkNeighborAL Mixed, incl. Spindle elongation, and Polo-like kinase mediated events; within-query FDR = 0.0008)(STRING NetworkNeighborAL Mixed, incl. Spindle elongation, and Polo-like kinase mediated events; within-query FDR = 0.0027)(STRING Keyword Mitosis; within-query FDR = 0.005)(STRING Keyword Cell cycle; within-query FDR = 0.0065). Its high-confidence relationships with CCNB1, HMMR, and KIF11 give it a strategically important bridge position, while its disease association with focal segmental glomerulosclerosis illustrates the relevance of altered cytoskeletal division machinery.
- **Conclusion**: Established evidence supports ANLN as the module's strongest cytokinetic and cortical-remodeling representative. A role in coordinating tissue-specific progenitor behavior is plausible but is not demonstrated by this module alone.

#### KIF11

- **Related proteins** (co-abundance neighbors): HMMR (0.83), UHRF1 (0.82); STRING partners: ANLN (0.947), CCNB1 (0.966), HMMR (0.928), KIFC1 (0.963), UHRF1 (0.708)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Mid piece; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 11. This gene encodes a motor protein that belongs to the kinesin-like protein family. Members of this protein family are known to be involved in various kinds of spindle dynamics. The function of this gene product includes chromosome positioning, centrosome separation and establishing a bipolar spindle during cell mitosis. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: microcephaly with or without chorioretinopathy, lymphedema, or intellectual disability (0.821); hereditary disease (0.509); inherited retinal dystrophy (0.507); neurodegenerative disease (0.484); microcephaly (0.412)
- **Europe PMC papers**: 3618
- **Why important**: KIF11 is a mitotic kinesin required for centrosome separation, bipolar-spindle establishment, chromosome positioning, and spindle assembly. It has strong STRING relationships with ANLN, CCNB1, HMMR, and KIFC1 and appears across the STRING spindle, kinetochore, and cell-cycle enrichments (STRING NetworkNeighborAL Mixed, incl. Amplification of signal from the kinetochores, and Mitotic sister chromatid segregation; within-query FDR = 0.0008)(STRING NetworkNeighborAL Mixed, incl. Spindle elongation, and Polo-like kinase mediated events; within-query FDR = 0.0008)(STRING NetworkNeighborAL Mixed, incl. Spindle elongation, and Polo-like kinase mediated events; within-query FDR = 0.0027)(STRING Keyword Mitosis; within-query FDR = 0.005)(STRING Keyword Cell cycle; within-query FDR = 0.0065)(STRING NetworkNeighborAL Mixed, incl. Spindle elongation, and Outer kinetochore; within-query FDR = 0.0423). Its bone-marrow and progenitor-cell enrichment is consistent with the proposed proliferative-cell interpretation, and its substantial literature and disease associations provide strong external biological support.
- **Conclusion**: Established evidence supports KIF11 as a core spindle-machinery component and a useful mechanistic marker of the module. The shared bone-skin context may reflect common cycling progenitors, but the supplied evidence does not prove that KIF11 is specifically responsible for cross-tissue conservation.

#### UHRF1

- **Related proteins** (co-abundance neighbors): KIF11 (0.82), ERCC6L (0.82), UBE2T (0.80); STRING partners: KIF11 (0.708), UBE2T (0.709)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin like with PHD and ring finger domains 1. This gene encodes a member of a subfamily of RING-finger type E3 ubiquitin ligases. The protein binds to specific DNA sequences, and recruits a histone deacetylase to regulate gene expression. Its expression peaks at late G1 phase and continues during G2 and M phases of the cell cycle. It plays a major role in the G1/S transition by regulating topoisomerase IIalpha and retinoblastoma gene expressi…
- **Diseases (Open Targets)**: hypertensive disorder (0.450); type 2 diabetes mellitus (0.424); immunodeficiency-centromeric instability-facial anomalies syndrome (0.371); neurodegenerative disease (0.367); coronary artery disorder (0.362)
- **Europe PMC papers**: 4824
- **Why important**: UHRF1 is one of the genes in both globally corrected nuclear-division terms (GO:BP mitotic nuclear division; q_global = 0.0169)(GO:BP nuclear division; q_global = 0.0385). Its annotated functions connect cell-cycle progression with transcriptional regulation, DNA-damage response, homologous-recombination repair, and ubiquitination. It connects in the module to KIF11, ERCC6L, and UBE2T, and its enrichment in bone marrow, lymphoid tissue, and several progenitor types supports a proliferative progenitor interpretation. Its large literature base and disease associations make it an important regulatory and disease-relevant member.
- **Conclusion**: Established evidence supports UHRF1 as a bridge between mitotic proliferation and genome-maintenance programs. It may help explain why DNA repair and ubiquitin-related genes accompany the spindle module, but direct mechanistic coupling in these tissues remains a hypothesis.

#### HMMR

- **Related proteins** (co-abundance neighbors): KIF11 (0.83), ERCC6L (0.82), ANLN (0.81), WAPL (0.81); STRING partners: ANLN (0.88), CCNB1 (0.942), KIF11 (0.928)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Microtubules; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hyaluronan mediated motility receptor. The protein encoded by this gene is involved in cell motility. It is expressed in breast tissue and together with other proteins, it forms a complex with BRCA1 and BRCA2, thus is potentially associated with higher risk of breast cancer. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene. [provided by RefSeq, Dec 2008].
- **Diseases (Open Targets)**: ovarian cancer (0.342); thyroid gland carcinoma (0.306); alcohol drinking (0.298); Alzheimer disease (0.279); Parkinson disease (0.279)
- **Europe PMC papers**: 2289
- **Why important**: HMMR occupies a highly connected position within the module and has strong STRING relationships with ANLN, CCNB1, and KIF11. It occurs across the supplementary spindle and kinetochore terms (STRING NetworkNeighborAL Mixed, incl. Amplification of signal from the kinetochores, and Mitotic sister chromatid segregation; within-query FDR = 0.0008)(STRING NetworkNeighborAL Mixed, incl. Spindle elongation, and Polo-like kinase mediated events; within-query FDR = 0.0008)(STRING NetworkNeighborAL Mixed, incl. Spindle elongation, and Polo-like kinase mediated events; within-query FDR = 0.0027)(STRING NetworkNeighborAL Mixed, incl. Spindle elongation, and Outer kinetochore; within-query FDR = 0.0423), while its microtubule localization and cell-motility annotation provide a plausible link between mitotic machinery and cellular movement. Its enrichment in bone marrow, lymphoid tissue, and progenitor populations, together with substantial literature and cancer associations, makes it important for interpreting the module beyond a simple proliferation marker.
- **Conclusion**: Established evidence supports HMMR as a microtubule-associated bridge between cell division and motility-related biology. A specific role in coordinating progenitor migration or tissue remodeling is plausible, but it is not established by the co-abundance evidence.

## Module 9

**Tissue pair**: bone and skin  
**Genes (6)**: PRMT5, CAPN1, CCDC6, MAP3K20, YARS1, TRIM25

### Function

The module does not support a single established pathway-level function. No GO or KEGG term passed global correction, and there was no supplementary STRING enrichment. Its structure is a star-like co-abundance pattern centered on MAP3K20, with CAPN1, PRMT5, YARS1, CCDC6, and TRIM25 each connected only to MAP3K20. The gene annotations suggest a possible convergence of cytosolic signaling, stress and damage responses, proteolysis, transcriptional and chromatin regulation, translation, cytoskeletal organization, and innate immune regulation. These annotations are heterogeneous, so the most defensible interpretation is a candidate cellular stress-response or remodeling module rather than a demonstrated canonical pathway. The absence of enrichment does not invalidate the module, but it limits functional specificity.

**Cell composition.** The module is composed entirely of intracellular proteins in the supplied HPA summary; no member is secreted. Most members have low tissue specificity, while MAP3K20 is enhanced in skeletal muscle and tongue and CAPN1 is enhanced in esophagus. Most members show cell-type-enhanced expression, with esophageal apical cells recurring among the enriched cell types, alongside muscle, vascular, reproductive, trophoblast, platelet, and immune-cell signals. Only MAP3K20 and TRIM25 are described as immune-cell enhanced, while the other genes have low immune-cell specificity. Thus, the module is not predominantly a plasma-protein or blood-cell module, although shared epithelial, muscle, platelet, or minor immune-cell composition could contribute to the bone-skin association. Protein detection in skin supports that the members are present there; comparable HPA bone protein evidence is unavailable in the fact sheet.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair met the supplied STRING interaction threshold, and no hu.MAP complex contained multiple module members. Therefore, the co-abundance relationships are not corroborated as high-confidence physical or functional interactions by these resources. The network may represent coordinated abundance without direct binding, indirect regulation, shared cell composition, or a tissue-specific association that is absent from current interaction databases. The strongest network position belongs to MAP3K20, whereas CAPN1, PRMT5, YARS1, CCDC6, and TRIM25 are peripheral members connected to it in the inferred co-abundance graph.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel co-abundance pattern, because the supplied databases provide no high-confidence STRING interactions, no multi-member hu.MAP complex, no STRING functional enrichment, and no globally significant GO or KEGG term. However, those absences do not establish biological novelty: the pattern could reflect indirect regulation, shared cell types, tissue composition, protein abundance effects, or incomplete database coverage. The appropriate conclusion is that the module is not already explained by the supplied interaction and pathway resources, but its novelty and reproducibility require independent validation, preferably with cell-composition adjustment and replication in additional bone and skin datasets.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular stress-remodeling program in bone and skin, with MAP3K20 acting as a co-abundance hub that links stress or checkpoint signaling to proteolysis through CAPN1, transcriptional and chromatin regulation through PRMT5, translational or stress-response biology through YARS1, cytoskeletal organization through CCDC6, and ubiquitin-mediated antiviral or oxidative-stress regulation through TRIM25. This is a mechanistic hypothesis rather than an established pathway assignment. An alternative explanation is coordinated abundance caused by shared epithelial, muscle, platelet, or other cell-type contributions rather than direct molecular cooperation.

### Important genes

#### MAP3K20

- **Related proteins** (co-abundance neighbors): CAPN1 (0.84), PRMT5 (0.82), YARS1 (0.80), CCDC6 (0.80), TRIM25 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitogen-activated protein kinase kinase kinase 20. This gene is a member of the MAPKKK family of signal transduction molecules and encodes a protein with an N-terminal kinase catalytic domain, followed by a leucine zipper motif and a sterile-alpha motif (SAM). This magnesium-binding protein forms homodimers and is located in the cytoplasm. The protein mediates gamma radiation signaling leading to cell cycle arrest and activity of this protein play…
- **Diseases (Open Targets)**: myopathy, centronuclear, 6, with fiber-type disproportion (0.750); split-foot malformation-mesoaxial polydactyly syndrome (0.743); smoking initiation (0.401); centronuclear myopathy (0.386); congenital fiber-type disproportion myopathy (0.370)
- **Europe PMC papers**: 353
- **Why important**: MAP3K20 is the central network gene, connected to every other member and having the greatest weighted network position in the supplied graph. Its annotation as a MAP kinase kinase kinase links it to MAPK and JNK signaling, DNA-damage checkpoint regulation, inflammatory response, chromosome segregation, and pro-apoptotic activity. HPA describes tissue enhancement in skeletal muscle and tongue, several muscle-related cell types, and myeloid dendritic cells. Its disease associations include centronuclear and congenital fiber-type disproportion myopathies. The literature record is substantial, supporting it as the most informative candidate hub.
- **Conclusion**: Established evidence supports MAP3K20 as the network hub and as a signaling protein involved in checkpoint, stress, inflammatory, and apoptotic biology. It is plausible that MAP3K20 organizes the module, but the co-abundance graph does not establish physical interaction or causality.

#### PRMT5

- **Related proteins** (co-abundance neighbors): MAP3K20 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein arginine methyltransferase 5. This gene encodes an enzyme that belongs to the methyltransferase family. The encoded protein catalyzes the transfer of methyl groups to the amino acid arginine, in target proteins that include histones, transcriptional elongation factors and the tumor suppressor p53. This gene plays a role in several cellular processes, including transcriptional regulation, and the assembly of small nuclear ribon…
- **Diseases (Open Targets)**: neurodegenerative disease (0.207); breast cancer (0.140); neoplasm (0.119); hepatocellular carcinoma (0.117); colorectal carcinoma (0.116)
- **Europe PMC papers**: 6035
- **Why important**: PRMT5 is a direct network neighbor of MAP3K20 and has broad cellular functions involving arginine methylation, transcriptional regulation, chromatin remodeling, spliceosomal small nuclear ribonucleoprotein assembly, and mitotic regulation. It is detected in nucleoplasm and cytosol and has extensive literature coverage. Its broad disease associations, including cancer and neurodegenerative disease, make it relevant to cell-state regulation, although they do not specifically implicate this bone-skin module.
- **Conclusion**: Established evidence supports PRMT5 as a major regulator of gene expression and RNA-processing-related cellular state. Its participation here may indicate coordinated stress or remodeling biology, but a direct MAP3K20-PRMT5 mechanism remains hypothetical.

#### TRIM25

- **Related proteins** (co-abundance neighbors): MAP3K20 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tripartite motif containing 25. The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein is an RNA binding protein, functions as a ubiquitin E3 ligase and is involved in multiple cellular processes, including regulation of antiviral innate immunity. [provided by RefSeq, S…
- **Diseases (Open Targets)**: dengue disease (0.463); COVID-19 (0.376); severe acute respiratory syndrome (0.372); neoplasm (0.108); hepatocellular carcinoma (0.106)
- **Europe PMC papers**: 4363
- **Why important**: TRIM25 is a direct neighbor of MAP3K20 and is an RNA-binding RING-family ubiquitin E3 ligase involved in cytoplasmic pattern-recognition signaling, antiviral innate immunity, protein ubiquitination, oxidative-stress response, and autophagy regulation. HPA identifies enhancement in several immune-related cell types, including neutrophils, while the supplied disease associations include viral diseases and neoplasms. Its substantial literature volume makes it a strong candidate for interpreting any immune or stress component of the module.
- **Conclusion**: Established evidence supports TRIM25 as a regulator of ubiquitin-dependent and innate immune processes. Its presence does not make the module an immune module, because most members have low immune-cell specificity; it instead supports a possible stress or inflammatory facet that requires direct testing.

#### CAPN1

- **Related proteins** (co-abundance neighbors): MAP3K20 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calpain 1. The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpa…
- **Diseases (Open Targets)**: Autosomal recessive spastic paraplegia type 76 (0.781); Alzheimer disease (0.383); neurodegenerative disease (0.326); hereditary spastic paraplegia 11 (0.266); hereditary disease (0.193)
- **Europe PMC papers**: 1869
- **Why important**: CAPN1 is connected to the MAP3K20 hub and encodes a calcium-activated intracellular cysteine protease involved in proteolysis, regulation of catalytic activity, autophagy, proliferation, and neuronal signaling. HPA reports enhancement in esophagus and in esophageal epithelial, trophoblast, and platelet-associated cell types. CAPN1 has extensive literature and disease associations that include hereditary spastic paraplegia and neurodegenerative disease, making it relevant to cytoskeletal and tissue-remodeling interpretations.
- **Conclusion**: Established evidence supports CAPN1 as an intracellular proteolytic regulator with potential relevance to tissue remodeling. Its module association could reflect coordinated turnover or cell-state changes, but the data do not demonstrate that CAPN1 is functionally downstream of MAP3K20.

#### YARS1

- **Related proteins** (co-abundance neighbors): MAP3K20 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tyrosyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Tyrosyl-tRNA synthetase belongs to the class I tRNA synthetase family. Cytokine activities have also been observ…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease dominant intermediate C (0.739); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset 2 (0.707); hereditary disease (0.509); Charcot-Marie-Tooth disease (0.418); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset (0.333)
- **Europe PMC papers**: 215
- **Why important**: YARS1 is a direct neighbor of MAP3K20 and is an aminoacyl-tRNA synthetase required for tyrosyl-tRNA charging and protein translation. The supplied annotation also describes stress, starvation, apoptosis, and cytokine-related activities. Unlike several other members, YARS1 has low cell-type specificity in the HPA summary, making it a possible broadly expressed cellular component rather than a marker of one particular cell population. Its disease associations include Charcot-Marie-Tooth disease and a multisystem infantile-onset disorder.
- **Conclusion**: Established evidence supports YARS1 as a translation-related enzyme with additional stress-associated functions. In this module it may represent general biosynthetic or stress-state biology, but its relationship to the other genes is not mechanistically established.

## Module 10

**Tissue pair**: bone and skin  
**Genes (26)**: ATXN2L, DDX21, DHX9, DIAPH1, ADAR, H2AC21, MACROH2A1, HMGA1, HNRNPL, HNRNPR, LMNB1, MATR3, MYBBP1A, NOC3L, NOL6, NOP2, NOP56, NUP214, RCC1, SF3A1, SF3B3, SMARCE1, SNW1, TP53BP1, EFTUD2, UTP14A

### Function

This is a conserved nuclear RNA and gene-expression module. The primary evidence is the globally corrected enrichment for nucleic-acid binding (GO:MF nucleic acid binding; q_global = 7.47e-08), RNA binding (GO:MF RNA binding; q_global = 9.84e-05), nuclear lumen and nucleoplasm (GO:CC nuclear lumen; q_global = 0.000304) (GO:CC nucleoplasm; q_global = 0.000369), the nucleus (GO:CC nucleus; q_global = 0.000972), nuclear protein-containing complexes (GO:CC nuclear protein-containing complex; q_global = 0.00554), RNA metabolism (GO:BP RNA metabolic process; q_global = 0.0067), chromatin (GO:CC chromatin; q_global = 0.00776), gene expression (GO:BP gene expression; q_global = 0.00794), RNA processing (GO:BP RNA processing; q_global = 0.00833), ribonucleoprotein complexes (GO:CC ribonucleoprotein complex; q_global = 0.00945), RNA biosynthesis (GO:BP RNA biosynthetic process; q_global = 0.00971), ribonucleoprotein-complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0104), and related nucleic-acid and macromolecule processes (4 globally significant GO/KEGG terms, q_global 0.012–0.0454; see the table). The spliceosomal catalytic-step term (GO:CC catalytic step 2 spliceosome; q_global = 0.0351) and DNA-binding terms (GO:MF DNA binding; q_global = 0.0204) (GO:MF sequence-specific DNA binding; q_global = 0.0359) indicate additional links to pre-mRNA splicing and chromatin regulation. Together, the module is best interpreted as coordinated nuclear RNA processing, ribosome biogenesis, chromatin regulation, and nucleocytoplasmic gene-expression control rather than as a tissue-specific extracellular pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not strongly blood-cell specific overall, because nearly all genes have low immune-cell specificity, although individual genes show enhancement in neutrophils or progenitor populations. Most genes have low tissue specificity, while several show cell-type enhancement in keratinocytes, neutrophils, germ-cell populations, or progenitors. Protein detection in skin is widespread among the tested genes, whereas bone has no matching HPA tissue-protein result. Thus, the shared bone-skin signal is more consistent with a broadly expressed nuclear program, potentially influenced by shared proliferative or differentiating cells, than with plasma carryover or a simple blood-cell module. The bone-marrow and progenitor enrichments warrant attention to cellular composition, but they do not by themselves establish blood contamination.

**GO/KEGG enrichment**: 25 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleic acid binding | 7.47e-08 | ADAR, ATXN2L, DDX21, DHX9, DIAPH1, EFTUD2, H2AC21, HMGA1, HNRNPL, HNRNPR, LMNB1, MACROH2A1, MATR3, MYBBP1A, NOC3L, NOL6, NOP2, NOP56, RCC1, SF3A1, SF3B3, SMARCE1, SNW1, TP53BP1, UTP14A |
| GO:MF RNA binding | 9.84e-05 | ADAR, ATXN2L, DDX21, DHX9, DIAPH1, EFTUD2, HMGA1, HNRNPL, HNRNPR, MATR3, MYBBP1A, NOC3L, NOL6, NOP2, NOP56, SF3A1, SF3B3, SMARCE1, SNW1, UTP14A |
| GO:CC nuclear lumen | 0.000304 | ADAR, ATXN2L, DDX21, DHX9, EFTUD2, HMGA1, HNRNPL, HNRNPR, LMNB1, MACROH2A1, MATR3, MYBBP1A, NOC3L, NOL6, NOP2, NOP56, NUP214, RCC1, SF3A1, SF3B3, SMARCE1, SNW1, TP53BP1, UTP14A |
| GO:CC nucleoplasm | 0.000369 | ADAR, ATXN2L, DDX21, DHX9, EFTUD2, HMGA1, HNRNPL, HNRNPR, LMNB1, MACROH2A1, MYBBP1A, NOC3L, NOL6, NOP2, NOP56, NUP214, RCC1, SF3A1, SF3B3, SMARCE1, SNW1, TP53BP1, UTP14A |
| GO:CC nucleus | 0.000972 | ADAR, ATXN2L, DDX21, DHX9, DIAPH1, EFTUD2, H2AC21, HMGA1, HNRNPL, HNRNPR, LMNB1, MACROH2A1, MATR3, MYBBP1A, NOC3L, NOL6, NOP2, NOP56, NUP214, RCC1, SF3A1, SF3B3, SMARCE1, SNW1, TP53BP1, UTP14A |
| GO:CC nuclear protein-containing complex | 0.00554 | ADAR, DDX21, EFTUD2, HMGA1, HNRNPR, MYBBP1A, NOL6, NOP56, NUP214, SF3A1, SF3B3, SMARCE1, SNW1, UTP14A |
| GO:BP RNA metabolic process | 0.0067 | ADAR, ATXN2L, DDX21, DHX9, EFTUD2, HMGA1, HNRNPL, HNRNPR, MACROH2A1, MYBBP1A, NOL6, NOP2, NOP56, SF3A1, SF3B3, SMARCE1, SNW1, TP53BP1, UTP14A |
| GO:CC chromatin | 0.00776 | DDX21, DHX9, H2AC21, HMGA1, HNRNPL, MACROH2A1, MYBBP1A, RCC1, SF3B3, SMARCE1 |
| GO:BP gene expression | 0.00794 | ADAR, DDX21, DHX9, EFTUD2, H2AC21, HMGA1, HNRNPL, HNRNPR, LMNB1, MACROH2A1, MATR3, MYBBP1A, NOL6, NOP2, NOP56, NUP214, SF3A1, SF3B3, SMARCE1, SNW1, TP53BP1, UTP14A |
| GO:BP RNA processing | 0.00833 | ADAR, DDX21, DHX9, EFTUD2, HNRNPL, HNRNPR, NOL6, NOP2, NOP56, SF3A1, SF3B3, SNW1, UTP14A |
| GO:CC ribonucleoprotein complex | 0.00945 | ADAR, DHX9, EFTUD2, HNRNPL, HNRNPR, NOL6, NOP56, SF3A1, SF3B3, SNW1, UTP14A |
| GO:BP RNA biosynthetic process | 0.00971 | ADAR, DDX21, DHX9, EFTUD2, HMGA1, HNRNPL, HNRNPR, MACROH2A1, MYBBP1A, NOL6, NOP2, NOP56, SF3A1, SF3B3, SMARCE1, SNW1, TP53BP1, UTP14A |
| GO:BP ribonucleoprotein complex biogenesis | 0.0104 | ADAR, DDX21, DHX9, MYBBP1A, NOL6, NOP2, NOP56, SF3A1, SF3B3, UTP14A |
| GO:BP nucleic acid metabolic process | 0.012 | ADAR, ATXN2L, DDX21, DHX9, EFTUD2, HMGA1, HNRNPL, HNRNPR, MACROH2A1, MYBBP1A, NOC3L, NOL6, NOP2, NOP56, SF3A1, SF3B3, SMARCE1, SNW1, TP53BP1, UTP14A |
| GO:BP nucleic acid biosynthetic process | 0.0163 | ADAR, DDX21, DHX9, EFTUD2, HMGA1, HNRNPL, HNRNPR, MACROH2A1, MYBBP1A, NOL6, NOP2, NOP56, SF3A1, SF3B3, SMARCE1, SNW1, TP53BP1, UTP14A |

### STRING and hu.MAP

STRING independently supports a nuclear and RNA-centered interpretation through the supplementary compartment and function terms (10 supplementary STRING terms; within-query FDR 4.98e-12–0.00028), with additional support for RNA metabolism (STRING RCTM Metabolism of RNA; within-query FDR = 0.00017) and ribonucleoprotein complexes (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.00028). Several relationships are already well represented: the DDX21–DHX9 and DDX21–MYBBP1A links, the HNRNPL–HNRNPR and DHX9–HNRNPL/HNRNPR links, the NOL6–NOP56–UTP14A–NOP2 nucleolar group, and the SF3A1–SF3B3–EFTUD2–SNW1 spliceosomal group. hu.MAP independently identifies an hnRNP and RNA-editing complex containing HNRNPL, HNRNPR, MATR3, and ADAR (hu.MAP huMAP3_10625.1), spliceosomal complexes containing EFTUD2, SF3B3, and SF3A1 (hu.MAP huMAP3_08980.1), and nuclear-pore or transport complexes containing RCC1 and NUP214 (hu.MAP huMAP3_08641.1) (hu.MAP huMAP3_10000.1) (hu.MAP huMAP3_12581.1). These concordant relationships indicate that the module is not merely an arbitrary co-abundance cluster: substantial parts correspond to known RNA-processing, nucleolar, spliceosomal, hnRNP, and nuclear-transport machinery. Conversely, many module edges lack a reported STRING or hu.MAP relationship, so co-abundance should not be treated as proof of direct physical interaction.

**STRING interactions (score >= 0.7)**: 33 of 325 gene pairs: ADAR–DHX9 (0.922); DDX21–DHX9 (0.908); DDX21–HNRNPR (0.73); DDX21–MYBBP1A (0.963); DDX21–NOP2 (0.761); DDX21–NOP56 (0.811); DHX9–HNRNPL (0.901); DHX9–HNRNPR (0.909); DHX9–MATR3 (0.786); DHX9–SF3B3 (0.73); EFTUD2–SF3A1 (0.999); EFTUD2–SF3B3 (0.999); EFTUD2–SNW1 (0.999); H2AC21–SMARCE1 (0.823); HNRNPL–HNRNPR (0.961); HNRNPL–MATR3 (0.757); HNRNPR–MATR3 (0.714); MYBBP1A–NOC3L (0.755); MYBBP1A–NOL6 (0.97); MYBBP1A–NOP2 (0.864); MYBBP1A–NOP56 (0.737); NOC3L–NOP2 (0.978); NOC3L–NOP56 (0.771); NOC3L–UTP14A (0.854); NOL6–NOP2 (0.881); NOL6–NOP56 (0.998); NOL6–UTP14A (0.997); NOP2–NOP56 (0.969); NOP2–UTP14A (0.866); NOP56–UTP14A (0.998); SF3A1–SF3B3 (0.999); SF3A1–SNW1 (0.989); SF3B3–SNW1 (0.99)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Nuclear lumen (FDR = 4.98e-12, 24 genes); Keyword Isopeptide bond (FDR = 2.2e-09, 21 genes); Function Nucleic acid binding (FDR = 5.38e-09, 25 genes); Keyword Ubl conjugation (FDR = 2.24e-08, 21 genes); COMPARTMENTS Nucleus (FDR = 6.92e-08, 26 genes); Keyword Nucleus (FDR = 1.07e-07, 25 genes); COMPARTMENTS Nucleoplasm (FDR = 2.42e-05, 14 genes); Component Nucleoplasm (FDR = 3.91e-05, 23 genes); Component Nuclear lumen (FDR = 3.91e-05, 24 genes); Function RNA binding (FDR = 6.69e-05, 19 genes); Component Nucleus (FDR = 8.03e-05, 26 genes); RCTM Metabolism of RNA (FDR = 0.00017, 14 genes); Keyword Methylation (FDR = 0.00021, 12 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 0.00028, 11 genes); TISSUES Leukemia cell (FDR = 0.0011, 14 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10625.1 (HNRNPR, HNRNPL, MATR3, ADAR; 4/57); huMAP3_07581.1 (HNRNPR, HNRNPL, MATR3; 3/21); huMAP3_08980.1 (EFTUD2, SF3B3, SF3A1; 3/97); huMAP3_05721.1 (HNRNPL, MATR3; 2/6); huMAP3_07225.1 (HNRNPR, HNRNPL; 2/7); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09654.1 (HNRNPR, HNRNPL; 2/13); huMAP3_08641.1 (RCC1, NUP214; 2/19); huMAP3_10659.1 (HNRNPR, HNRNPL; 2/28); huMAP3_10000.1 (RCC1, NUP214; 2/44); huMAP3_08501.1 (SNW1, EFTUD2; 2/47); huMAP3_09504.1 (SNW1, EFTUD2; 2/51); huMAP3_04549.1 (SF3B3, SF3A1; 2/52); huMAP3_12581.1 (RCC1, NUP214; 2/58); huMAP3_09945.1 (SNW1, EFTUD2; 2/61); huMAP3_06511.1 (SF3B3, SF3A1; 2/79)

### Novelty

The module is unlikely to represent a wholly new molecular pathway, because its central processes and several subnetworks are already established by GO, STRING, and hu.MAP. Its potential novelty is instead at the systems level: a coordinated co-abundance program shared by bone and skin that brings together nucleolar ribosome biogenesis, RNA helicases and RNA-binding proteins, spliceosomal components, chromatin regulators, and nuclear transport proteins. This tissue-pair organization and the particular co-abundance wiring may be novel, but that cannot be concluded from absence of STRING or hu.MAP links alone. Demonstrating novelty would require comparison with published bone and skin co-expression modules, matched bulk and single-cell datasets, and independent replication across cohorts.

**Hypothesis.** Hypothesis: the shared module reflects a conserved demand for nuclear RNA production and quality control during renewal or differentiation of bone- and skin-associated cells. In this model, DDX21, DHX9, ADAR, and hnRNP proteins coordinate RNA remodeling, editing, and handling; NOL6, NOP56, NOP2, UTP14A, and MYBBP1A support nucleolar ribosome biogenesis; SF3A1, SF3B3, EFTUD2, and SNW1 support spliceosome function; and LMNB1, chromatin-associated proteins, TP53BP1, RCC1, and NUP214 couple RNA metabolism to nuclear architecture, DNA damage responses, and transport. The HPA pattern suggests that this may be a broadly expressed cellular-state program rather than a specialized bone-skin pathway. This mechanism is a hypothesis generated from the integrated evidence and requires perturbation and cell-composition-aware validation.

### Important genes

#### LMNB1

- **Related proteins** (co-abundance neighbors): NOP56 (0.86), HNRNPL (0.85), MATR3 (0.85), NOL6 (0.84), DDX21 (0.84), NUP214 (0.80), MYBBP1A (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lamin B1. This gene encodes one of the two B-type lamin proteins and is a component of the nuclear lamina. A duplication of this gene is associated with autosomal dominant adult-onset leukodystrophy (ADLD). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: microcephaly 26, primary, autosomal dominant (0.723); autosomal dominant primary microcephaly (0.675); adult-onset autosomal dominant demyelinating leukodystrophy (0.670); hereditary disease (0.488); Syndrome with microcephaly as major feature (0.487)
- **Europe PMC papers**: 3851
- **Why important**: LMNB1 is a hub-like module member connecting nucleolar, hnRNP, helicase, and nuclear-pore-associated genes. It is present in the strongest nuclear and chromatin-related primary terms (7 globally significant GO/KEGG terms, q_global 7.47e-08–0.0359; see the table) and is annotated as a nuclear-lamina component involved in nuclear-envelope organization, heterochromatin formation, nuclear migration, and pore localization. Its association with adult-onset autosomal dominant demyelinating leukodystrophy and primary microcephaly gives the nuclear-architecture signal disease relevance. It also has a substantial literature base.
- **Conclusion**: Established: LMNB1 is a nuclear-lamina and chromatin-associated gene with strong module connectivity and relevant neurological disease associations. Hypothesis: LMNB1 may help couple nuclear architecture to coordinated RNA processing in the shared bone-skin state; the co-abundance data do not establish direct regulation of the other module genes.

#### DDX21

- **Related proteins** (co-abundance neighbors): NOL6 (0.87), NOP2 (0.85), LMNB1 (0.84), HNRNPR (0.82), NOP56 (0.82), MYBBP1A (0.81); STRING partners: DHX9 (0.908), HNRNPR (0.73), MYBBP1A (0.963), NOP2 (0.761), NOP56 (0.811)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 is a highly connected bridge between nucleolar genes, RNA-binding proteins, and the RNA helicase DHX9. It contributes to nearly all major primary RNA, nucleolar, ribonucleoprotein, and gene-expression terms (7 globally significant GO/KEGG terms, q_global 7.47e-08–0.0104; see the table). Its known functions include RNA helicase activity, ribosome and spliceosome assembly, chromatin remodeling, and transcriptional regulation, and its annotations include osteoblast differentiation. STRING also supports links to DHX9, HNRNPR, MYBBP1A, NOP2, and NOP56.
- **Conclusion**: Established: DDX21 is a plausible central coordinator of nucleolar RNA metabolism and transcriptional regulation, with direct STRING support for several module relationships. Hypothesis: its presence may connect the shared module to differentiation-associated RNA processing in bone and skin cells.

#### ADAR

- **Related proteins** (co-abundance neighbors): DHX9 (0.84), HNRNPR (0.82), RCC1 (0.80); STRING partners: DHX9 (0.922)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_10625.1
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR links the RNA-processing component to RNA editing, innate antiviral biology, and nuclear transport. It is represented across the primary RNA, nucleic-acid, ribonucleoprotein, and gene-expression terms (6 globally significant GO/KEGG terms, q_global 7.47e-08–0.0104; see the table) and has a strong STRING relationship with DHX9. ADAR is a well-studied gene with a large literature base and disease associations including Aicardi-Goutieres syndrome and dyschromatosis symmetrica hereditaria. hu.MAP places it with HNRNPL, HNRNPR, and MATR3 in an RNA-associated complex (hu.MAP huMAP3_10625.1).
- **Conclusion**: Established: ADAR supplies a specific RNA-editing function within an otherwise broad nuclear RNA module and is supported by both STRING and hu.MAP evidence. Hypothesis: ADAR-dependent editing may tune RNA quality control or stress responses in the shared tissue state, but no tissue-specific editing effect is demonstrated here.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): LMNB1 (0.85), DHX9 (0.82), HNRNPR (0.82); STRING partners: DHX9 (0.901), HNRNPR (0.961), MATR3 (0.757)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_07581.1, huMAP3_05721.1, huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_10659.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is a central RNA-binding and hnRNP component, connected in the module to LMNB1, DHX9, and HNRNPR. It appears across the primary RNA-binding, RNA-processing, nuclear, ribonucleoprotein, and gene-expression terms (5 globally significant GO/KEGG terms, q_global 7.47e-08–0.00945; see the table). STRING supports its relationships with DHX9, HNRNPR, and MATR3, while hu.MAP places it in several hnRNP complexes (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1). It is a well-studied regulator of RNA processing and alternative splicing.
- **Conclusion**: Established: HNRNPL is a major integrator of the module's RNA-binding and splicing evidence and has convergent STRING and hu.MAP support. Hypothesis: it may coordinate transcript processing across the shared bone-skin cellular program rather than act as a tissue-specific effector.

#### NOP56

- **Related proteins** (co-abundance neighbors): LMNB1 (0.86), NOL6 (0.84), DDX21 (0.82), H2AC21 (0.80); STRING partners: DDX21 (0.811), MYBBP1A (0.737), NOC3L (0.771), NOL6 (0.998), NOP2 (0.969), UTP14A (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP56 ribonucleoprotein. Nop56p is a yeast nucleolar protein that is part of a complex with the nucleolar proteins Nop58p and fibrillarin. Nop56p is required for assembly of the 60S ribosomal subunit and is involved in pre-rRNA processing. The protein encoded by this gene is similar in sequence to Nop56p and is also found in the nucleolus. Expansion of a GGCCTG repeat from 3-8 copies to 1500-2500 copies in an intron of th…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 36 (0.586); neurodegenerative disease (0.495); ovarian neoplasm (0.272); hereditary disease (0.193); cerebellar ataxia (0.121)
- **Europe PMC papers**: 1517
- **Why important**: NOP56 is a nucleolar connector within the dense NOL6, NOP2, UTP14A, and related ribosome-biogenesis subnetwork. It contributes to the primary nucleic-acid, RNA-processing, ribonucleoprotein, and ribosome-biogenesis-related terms (7 globally significant GO/KEGG terms, q_global 7.47e-08–0.0104; see the table). STRING strongly supports its relationships with NOL6, NOP2, and UTP14A. Its established functions include pre-rRNA processing, rRNA modification, and small-subunit maturation, and its repeat expansion is associated with spinocerebellar ataxia type six and related neurological disease. It has a substantial literature base.
- **Conclusion**: Established: NOP56 marks a coherent nucleolar ribosome-biogenesis subnetwork supported by both annotation and STRING. Hypothesis: coordinated NOP56 activity may reflect increased ribosome-production capacity during renewal or differentiation, although the module does not prove altered ribosome output.

## Module 11

**Tissue pair**: bone and skin  
**Genes (10)**: BICD2, GCC2, GEMIN4, HSDL1, MVK, MOV10, ORC2, RPP30, RPP40, TMEM65

### Function

The module does not have any GO or KEGG term passing global multiple-testing correction. Therefore, its function must be inferred from the gene identities and network structure rather than from a statistically validated enrichment label. The clearest coherent component is RNA maturation: RPP30 and RPP40 are ribonuclease P/MRP subunits involved in tRNA five-prime-leader removal and RNA processing, and GEMIN4 supports spliceosomal small nuclear ribonucleoprotein assembly and rRNA processing. MOV10 adds RNA helicase and post-transcriptional RNA-regulatory functions, while ORC2 represents DNA-replication initiation. BICD2 and GCC2 indicate Golgi and retrograde vesicle trafficking, MVK indicates mevalonate and sterol biology, and HSDL1 with TMEM65 suggests a mitochondrial or membrane-associated metabolic component. Overall, this is best interpreted as a mixed cellular-maintenance module with a relatively strong RNA-processing core and additional trafficking, replication, membrane, and metabolic links. The absence of a globally significant GO or KEGG term does not invalidate the module; it indicates that no single annotation category dominates sufficiently across the full gene set.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly intracellular or membrane-associated. The HPA profile is broadly expressed for most genes, with tissue enhancement reported for BICD2 in skin and MVK in liver. Recurring single-cell annotations include germ-cell populations, esophageal epithelial populations, neutrophils, and platelets, but HPA reports low immune-cell specificity for every module gene and no recurring enriched blood-cell category. Thus, the module does not strongly resemble a blood-contamination signature. Its conservation between bone and skin may instead reflect shared basal cellular processes, shared epithelial or stromal cell states, or coordinated expression of broadly useful intracellular machinery. Skin protein detection is reported for several genes, whereas bone protein detection is unavailable in the supplied HPA tissue comparison, so the tissue-level protein evidence does not establish bone-specific expression.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence direct relationship within the module, between RPP30 and RPP40. This strongly supports the interpretation that these two genes represent a real ribonuclease P/MRP-related interaction rather than an arbitrary co-abundance pair. The STRING supplementary enrichment (STRING NetworkNeighborAL Endoribonuclease complex, and Argonaute hook; within-query FDR = 0.0493) connects RPP40, RPP30, and MOV10 to an endoribonuclease-related complex and Argonaute-associated biology, but this is supplementary within-query evidence and is not global enrichment significance. hu.MAP independently places RPP30 and RPP40 together in each of the listed complexes (hu.MAP huMAP3_06709.1), (hu.MAP huMAP3_08418.1), (hu.MAP huMAP3_12090.1), and (hu.MAP huMAP3_08469.1). Because the same pair accounts for the overlap in all of these complexes, hu.MAP supports a known RPP30-RPP40 complex relationship rather than demonstrating that the entire module is one established complex. The other module relationships are not supported by the supplied high-confidence STRING or hu.MAP records, so they may reflect co-abundance, indirect biology, cell-state effects, or uncharacterized associations.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: RPP30–RPP40 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Endoribonuclease complex, and Argonaute hook (FDR = 0.0493, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06709.1 (RPP40, RPP30; 2/11); huMAP3_08418.1 (RPP40, RPP30; 2/13); huMAP3_12090.1 (RPP40, RPP30; 2/13); huMAP3_08469.1 (RPP40, RPP30; 2/14)

### Novelty

The module should not be called a newly discovered molecular complex. Its strongest molecular relationship, RPP30-RPP40, is already supported by STRING and by multiple hu.MAP complex records, and the functions of many individual genes are established. What may be novel is the coordinated co-abundance of this particular combination across bone and skin, especially the linkage of the known ribonuclease P/MRP pair with BICD2, GEMIN4, ORC2, MOV10, HSDL1, TMEM65, MVK, and GCC2. However, the supplied evidence does not include a systematic comparison against prior tissue co-abundance modules, so it cannot establish that this cross-tissue module is new. The appropriate conclusion is that the module contains known biology arranged in a potentially distinctive tissue-pair co-abundance pattern, with novelty remaining unproven.

**Hypothesis.** Hypothesis: in bone and skin, a shared cellular state coordinates core RNA maturation and quality-control capacity with the biosynthetic, trafficking, and membrane demands of metabolically active or differentiating cells. RPP30 and RPP40 could form the central RNA-processing anchor, with GEMIN4 and MOV10 contributing RNA assembly or post-transcriptional regulation. BICD2 and GCC2 could couple this state to Golgi and retrograde transport, while MVK could connect it to sterol and isoprenoid metabolism and HSDL1 with TMEM65 to mitochondrial or membrane functions. ORC2 may indicate that the state also includes replication competence or proliferative activity. This is a mechanistic model generated from annotations and network position, not a demonstrated causal pathway; direct perturbation, cell-type-resolved expression, and protein interaction experiments would be needed to test it.

### Important genes

#### RPP30

- **Related proteins** (co-abundance neighbors): RPP40 (0.86), BICD2 (0.81); STRING partners: RPP40 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_06709.1, huMAP3_08418.1, huMAP3_12090.1, huMAP3_08469.1
- **Function (MyGene.info)**: ribonuclease P/MRP subunit p30. Enables ribonuclease P RNA binding activity. Contributes to ribonuclease P activity. Involved in tRNA 5'-leader removal. Part of multimeric ribonuclease P complex and ribonuclease MRP complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); alcohol drinking (0.297); ovarian dysfunction (0.260); Chest pain (0.230); hyperpituitarism (0.205)
- **Europe PMC papers**: 1572
- **Why important**: RPP30 is one of the two genes forming the strongest known within-module interaction, with RPP40 supported by STRING and by all listed hu.MAP overlaps (hu.MAP huMAP3_06709.1), (hu.MAP huMAP3_08418.1), (hu.MAP huMAP3_12090.1), and (hu.MAP huMAP3_08469.1). It has a direct ribonuclease P/MRP role in tRNA processing and RNA processing, placing it at the most coherent functional core of the module. Its disease associations include neurodegenerative disease and reproductive or endocrine-related phenotypes, and the fact sheet indicates substantial literature coverage.
- **Conclusion**: Established evidence supports RPP30 as a ribonuclease P/MRP subunit and as a central member of the known RPP30-RPP40 complex. The hypothesis that its co-abundance links RNA maturation to the bone-skin shared state is plausible, but the module data do not establish that RPP30 drives the tissue phenotype.

#### RPP40

- **Related proteins** (co-abundance neighbors): GEMIN4 (0.88), RPP30 (0.86); STRING partners: RPP30 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06709.1, huMAP3_08418.1, huMAP3_12090.1, huMAP3_08469.1
- **Function (MyGene.info)**: ribonuclease P/MRP subunit p40. Enables ribonuclease P RNA binding activity. Contributes to ribonuclease P activity. Involved in tRNA 5'-leader removal. Part of multimeric ribonuclease P complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.480); familial hemolytic anemia (0.186); keratinocyte carcinoma (0.117); squamous cell carcinoma (0.117); basal cell carcinoma (0.111)
- **Europe PMC papers**: 248
- **Why important**: RPP40 is directly connected to RPP30 by the strongest STRING relationship in the module and recurs with RPP30 in every listed hu.MAP complex (hu.MAP huMAP3_06709.1), (hu.MAP huMAP3_08418.1), (hu.MAP huMAP3_12090.1), and (hu.MAP huMAP3_08469.1). It contributes to ribonuclease P activity and tRNA five-prime-leader removal, providing an independent functional basis for the RNA-processing interpretation. Its annotations include RNA processing and disease associations involving neurodegenerative and keratinocyte or skin malignancy contexts, with meaningful literature support.
- **Conclusion**: Established evidence identifies RPP40 as a ribonuclease P/MRP component that partners with RPP30. Its presence strongly anchors the module in known RNA-processing machinery, while any specific role in coordinating bone and skin biology remains a hypothesis.

#### BICD2

- **Related proteins** (co-abundance neighbors): MVK (0.82), GCC2 (0.81), RPP30 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Plasma membrane, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BICD cargo adaptor 2. This gene is one of two human homologs of Drosophila bicaudal-D and a member of the Bicoid family. It has been implicated in dynein-mediated, minus end-directed motility along microtubules. It has also been reported to be a phosphorylation target of NIMA related kinase 8. Two alternative splice variants have been described. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy with contractures (0.807); spinal muscular atrophy, lower extremity-predominant, 2B, prenatal onset, autosomal dominant (0.740); hereditary disease (0.478); neuronopathy, distal hereditary motor, autosomal dominant (0.460); arthrogryposis multiplex congenita (0.437)
- **Europe PMC papers**: 925
- **Why important**: BICD2 has the broadest network connectivity in the module and links MVK, GCC2, and RPP30, making it a plausible bridge between the RNA-processing core and Golgi, vesicle, and metabolic features. Its established functions include dynein-mediated minus-end-directed transport, retrograde vesicle transport, and Golgi localization. It is tissue-enhanced in skin, has cell annotations spanning keratinocyte and neutrophil-related populations, and has substantial literature and disease evidence for inherited motor-neuron and contracture syndromes.
- **Conclusion**: Established evidence supports BICD2 as a microtubule-based cargo adaptor involved in organelle and Golgi transport. Its bridging position makes it a strong candidate for coupling intracellular trafficking to the shared bone-skin module, but the causal bridge is not demonstrated by the co-abundance network.

#### MOV10

- **Related proteins** (co-abundance neighbors): ORC2 (0.82), HSDL1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Mov10 RNA helicase. Enables 5'-3' RNA helicase activity and RNA binding activity. Involved in defense response to virus; negative regulation of transposition, RNA-mediated; and posttranscriptional regulation of gene expression. Located in P-body and cytosol. Implicated in hypertension. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.516); cancer (0.467); Thrombocytopenia (0.364); open-angle glaucoma (0.344); hypertensive disorder (0.329)
- **Europe PMC papers**: 1449
- **Why important**: MOV10 connects ORC2 and HSDL1 in the module and is the third gene named in the supplementary STRING functional signal (STRING NetworkNeighborAL Endoribonuclease complex, and Argonaute hook; within-query FDR = 0.0493). It is an RNA helicase involved in RNA binding, antiviral defense, transposable-element control, and microRNA-mediated post-transcriptional regulation. Its literature is substantial and its disease associations include cancer, thrombocytopenia, hypertension-related disease, and neurodegenerative disease.
- **Conclusion**: Established evidence supports MOV10 as an RNA-regulatory helicase with broad post-transcriptional functions. Its inclusion alongside RPP30 and RPP40 supports an RNA-centered interpretation, but the supplementary STRING result does not establish a direct physical interaction between MOV10 and the RPP subunits.

#### MVK

- **Related proteins** (co-abundance neighbors): BICD2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mevalonate kinase. This gene encodes the peroxisomal enzyme mevalonate kinase. Mevalonate is a key intermediate, and mevalonate kinase a key early enzyme, in isoprenoid and sterol synthesis. Mevalonate kinase deficiency caused by mutation of this gene results in mevalonic aciduria, a disease characterized psychomotor retardation, failure to thrive, hepatosplenomegaly, anemia and recurrent febrile crises. Defects in …
- **Diseases (Open Targets)**: hyperimmunoglobulinemia D with periodic fever (0.847); mevalonic aciduria (0.838); porokeratosis 3, disseminated superficial actinic type (0.748); mevalonate kinase deficiency (0.590); methylmalonic aciduria cblb type (0.555)
- **Europe PMC papers**: 3311
- **Why important**: MVK is connected to BICD2, thereby placing a well-characterized metabolic enzyme at the trafficking edge of the module. It catalyzes an early step in mevalonate, sterol, and isoprenoid biosynthesis, is tissue-enhanced in liver, and is detected in skin by HPA. It has strong disease evidence for mevalonate kinase deficiency, hyperimmunoglobulinemia D with periodic fever, and related metabolic or inflammatory phenotypes, together with extensive literature coverage.
- **Conclusion**: Established evidence supports MVK as a mevalonate-pathway enzyme with important metabolic and inflammatory disease relevance. Its network connection to BICD2 suggests a possible link between lipid or isoprenoid metabolism and vesicle trafficking in the shared module, but that connection remains a hypothesis rather than a demonstrated mechanism.

## Module 12

**Tissue pair**: bone and skin  
**Genes (6)**: CTSC, CDC50A, DHCR7, NRAS, RHOG, SCD

### Function

The strongest interpretation is an endoplasmic-reticulum-associated membrane and lipid-homeostasis module. The globally corrected cellular-component result (GO:CC endoplasmic reticulum; q_global = 0.0155) places every module gene in the endoplasmic reticulum, supporting a coherent subcellular localization rather than a specific pathway assignment. The gene annotations further point to phospholipid translocation through CDC50A, fatty-acid desaturation through SCD, sterol conversion through DHCR7, membrane-associated Ras and Rho signaling through NRAS and RHOG, and lysosomal protease and immune-cell protease regulation through CTSC. Thus, the module appears to combine ER membrane lipid handling with membrane signaling and vesicular or lysosomal biology. The network is sparse and organized around CDC50A, with links to CTSC, SCD and DHCR7, while CTSC connects to NRAS and NRAS connects to RHOG. This topology supports a related membrane-cellular program, but does not establish direct biochemical interactions among all genes.

**Cell composition.** The module is not dominated by secreted or plasma proteins: only CTSC has an intracellular-and-membrane secretome annotation, and the module has one secreted-gene annotation overall. All genes have low immune-cell specificity, and no enriched blood-cell category is reported, arguing against a straightforward blood-cell module. At the same time, the genes are not uniformly tissue restricted. HPA reports low tissue specificity for CDC50A, CTSC and NRAS, while RHOG is tissue enhanced in bone marrow and SCD is tissue enhanced in adipose tissue, brain and liver; DHCR7 is tissue enhanced in liver. Cell-type enhancement is reported for every gene, with repeated signals in esophageal apical cells and additional signals in Kupffer, Hofbauer and alveolar type two cells. Protein detection is reported in skin for most genes, whereas there is no matching HPA bone tissue result. Consequently, the shared bone-skin signal could reflect a broadly distributed ER and membrane program, shared epithelial or stromal biology, or sample cellular composition; the HPA evidence does not support a specific blood contamination explanation.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC endoplasmic reticulum | 0.0155 | CDC50A, CTSC, DHCR7, NRAS, RHOG, SCD |

### STRING and hu.MAP

The STRING enrichment results (STRING Component Endoplasmic reticulum; within-query FDR = 0.0063) and (STRING COMPARTMENTS Endoplasmic reticulum; within-query FDR = 0.0495) independently support an endoplasmic-reticulum localization, but they are supplementary and are not global multiple-testing evidence. Their listed gene overlap includes CTSC, RHOG, DHCR7, NRAS and SCD; (STRING Component Endoplasmic reticulum; within-query FDR = 0.0063) names TMEM30A rather than CDC50A, so this result should be interpreted cautiously and not as definitive confirmation of every module member. No high-confidence STRING interaction is reported among the module gene pairs. hu.MAP provides a different kind of support: SCD and DHCR7 co-occur in four reported complexes (hu.MAP huMAP3_08167.1) (hu.MAP huMAP3_06791.1) (hu.MAP huMAP3_06247.1) (hu.MAP huMAP3_09592.1), each as a small subset of a much larger complex. This establishes that SCD and DHCR7 have known complex-level context, but it does not demonstrate a complex containing the whole module. CDC50A, CTSC, NRAS and RHOG have no hu.MAP or STRING partners listed in this evidence set. Overall, the network is more strongly supported by shared localization and functional coherence than by already catalogued direct physical interactions.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Component Endoplasmic reticulum (FDR = 0.0063, 6 genes); COMPARTMENTS Endoplasmic reticulum (FDR = 0.0495, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08167.1 (SCD, DHCR7; 2/24); huMAP3_06791.1 (SCD, DHCR7; 2/31); huMAP3_06247.1 (SCD, DHCR7; 2/65); huMAP3_09592.1 (SCD, DHCR7; 2/95)

### Novelty

This may be a new co-abundance module in the specific bone-skin comparison, but the fact sheet is insufficient to call it a wholly new biological discovery. The absence of high-confidence STRING pairwise interactions and the limited hu.MAP overlap suggest that the exact cross-gene co-abundance organization is not already represented as a well-established interaction network. However, ER localization, lipid metabolism, Ras or Rho signaling, lysosomal protease biology, and the SCD-DHCR7 complex context are established findings. Therefore, the defensible claim is novelty of the tissue-shared co-abundance pattern or its integration of these processes, pending comparison with published co-expression modules, tissue datasets and experimental validation. Database absence alone is not evidence that the biology is novel.

**Hypothesis.** Hypothesis: in bone and skin, coordinated ER membrane lipid remodeling involving CDC50A, SCD and DHCR7 may alter membrane composition and trafficking, thereby influencing the membrane localization or activity of NRAS and RHOG. This could couple lipid and sterol homeostasis to cytoskeletal signaling, cell shape, proliferation or motility, while CTSC may connect the program to vesicular and protease-related functions in resident or neighboring cells. The hypothesis is motivated by (GO:CC endoplasmic reticulum; q_global = 0.0155), the network topology, the (STRING Component Endoplasmic reticulum; within-query FDR = 0.0063) and (STRING COMPARTMENTS Endoplasmic reticulum; within-query FDR = 0.0495) localization signals, and the SCD-DHCR7 hu.MAP overlap (hu.MAP huMAP3_08167.1) (hu.MAP huMAP3_06791.1) (hu.MAP huMAP3_06247.1) (hu.MAP huMAP3_09592.1). It remains a mechanistic proposal rather than an established causal pathway.

### Important genes

#### CDC50A

- **Related proteins** (co-abundance neighbors): CTSC (0.81), SCD (0.81), DHCR7 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell division cycle 50 P4-ATPase accessory subunit A. Enables aminophospholipid flippase activity. Involved in several processes, including phospholipid transport; positive regulation of transport; and xenobiotic transmembrane transport. Located in endoplasmic reticulum and plasma membrane. Part of phospholipid-translocating ATPase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: atrial fibrillation (0.243); placenta praevia (0.116); restless legs syndrome (0.110); neoplasm (0.090); atrial flutter (0.081)
- **Europe PMC papers**: 416
- **Why important**: CDC50A has the highest weighted network connectivity in the module and links the central network branch to CTSC, SCD and DHCR7. Its established function as a P-four ATPase accessory subunit connects the module to aminophospholipid translocation, endosomal transport and membrane or ER biology. It is included in (GO:CC endoplasmic reticulum; q_global = 0.0155), although no STRING partner or hu.MAP complex is listed for it. Its literature base is substantial, and its annotations provide a plausible membrane-organizing role.
- **Conclusion**: Established evidence supports CDC50A as the network-centered phospholipid-transport component of the module. It is a reasonable candidate for coordinating the lipid and trafficking signals, but a direct causal bridge to the other genes is only a hypothesis.

#### SCD

- **Related proteins** (co-abundance neighbors): CDC50A (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_08167.1, huMAP3_06791.1, huMAP3_06247.1, huMAP3_09592.1
- **Function (MyGene.info)**: stearoyl-CoA desaturase. This gene encodes an enzyme involved in fatty acid biosynthesis, primarily the synthesis of oleic acid. The protein belongs to the fatty acid desaturase family and is an integral membrane protein located in the endoplasmic reticulum. Transcripts of approximately 3.9 and 5.2 kb, differing only by alternative polyadenlyation signals, have been detected. A gene encoding a similar enzyme is located on…
- **Diseases (Open Targets)**: Alzheimer disease (0.483); Parkinson disease (0.476); neurodegenerative disease (0.463); lysosomal storage disease (0.462); cataract (0.397)
- **Europe PMC papers**: 36923
- **Why important**: SCD is an ER integral membrane enzyme with extensive literature and a direct role in monounsaturated fatty-acid biosynthesis. It is part of (GO:CC endoplasmic reticulum; q_global = 0.0155) and (STRING Component Endoplasmic reticulum; within-query FDR = 0.0063) (STRING COMPARTMENTS Endoplasmic reticulum; within-query FDR = 0.0495), and it co-occurs with DHCR7 in all listed hu.MAP complexes (hu.MAP huMAP3_08167.1) (hu.MAP huMAP3_06791.1) (hu.MAP huMAP3_06247.1) (hu.MAP huMAP3_09592.1). Its tissue-enhanced expression in adipose tissue, brain and liver and skin protein detection support a metabolically relevant membrane-lipid contribution.
- **Conclusion**: Established evidence identifies SCD as a strong biochemical anchor for ER lipid remodeling and as the best-supported complex-associated component. Its connection to NRAS, RHOG or CTSC in this module should be regarded as a co-abundance association, not a demonstrated direct interaction.

#### DHCR7

- **Related proteins** (co-abundance neighbors): CDC50A (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_08167.1, huMAP3_06791.1, huMAP3_06247.1, huMAP3_09592.1
- **Function (MyGene.info)**: 7-dehydrocholesterol reductase. This gene encodes an enzyme that removes the C(7-8) double bond in the B ring of sterols and catalyzes the conversion of 7-dehydrocholesterol to cholesterol. This gene is ubiquitously expressed and its transmembrane protein localizes to the endoplasmic reticulum membrane and nuclear outer membrane. Mutations in this gene cause Smith-Lemli-Opitz syndrome (SLOS); a syndrome that is metabolically cha…
- **Diseases (Open Targets)**: Smith-Lemli-Opitz syndrome (0.867); hereditary disease (0.550); neurodegenerative disease (0.477); Intellectual disability (0.464); cataract (0.464)
- **Europe PMC papers**: 3788
- **Why important**: DHCR7 is an ER enzyme that converts seven-dehydrocholesterol to cholesterol and is annotated for cholesterol and sterol biosynthesis. It contributes to (GO:CC endoplasmic reticulum; q_global = 0.0155) and (STRING Component Endoplasmic reticulum; within-query FDR = 0.0063) (STRING COMPARTMENTS Endoplasmic reticulum; within-query FDR = 0.0495) and co-occurs with SCD in the listed hu.MAP complexes (hu.MAP huMAP3_08167.1) (hu.MAP huMAP3_06791.1) (hu.MAP huMAP3_06247.1) (hu.MAP huMAP3_09592.1). Its established disease association with Smith-Lemli-Opitz syndrome makes it biologically important, while liver tissue enhancement and skin protein detection reinforce its relevance to lipid homeostasis.
- **Conclusion**: Established evidence supports DHCR7 as the sterol-homeostasis arm of the module and as a known complex-context partner of SCD. Its proposed influence on signaling or tissue remodeling through this module remains unproven.

#### NRAS

- **Related proteins** (co-abundance neighbors): CTSC (0.83), RHOG (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NRAS proto-oncogene, GTPase. This is an N-ras oncogene encoding a membrane protein that shuttles between the Golgi apparatus and the plasma membrane. This shuttling is regulated through palmitoylation and depalmitoylation by the ZDHHC9-GOLGA7 complex. The encoded protein, which has intrinsic GTPase activity, is activated by a guanine nucleotide-exchange factor and inactivated by a GTPase activating protein. Mutations in this …
- **Diseases (Open Targets)**: Noonan syndrome (0.828); Noonan syndrome 6 (0.807); large congenital melanocytic nevus (0.707); nevus, epidermal (0.700); acute myeloid leukemia (0.699)
- **Europe PMC papers**: 32202
- **Why important**: NRAS is an extensively studied membrane-associated small GTPase with the highest literature volume among the module genes. It occupies an intermediate network position, connecting CTSC and RHOG, and is included in (GO:CC endoplasmic reticulum; q_global = 0.0155) and (STRING Component Endoplasmic reticulum; within-query FDR = 0.0063) (STRING COMPARTMENTS Endoplasmic reticulum; within-query FDR = 0.0495). Its established roles in Ras signaling, MAPK regulation, proliferation and developmental disease make it a plausible signaling output of membrane-state changes.
- **Conclusion**: Established evidence supports NRAS as the signaling component linking the membrane module to Ras biology. The hypothesis that ER lipid remodeling regulates NRAS activity in this bone-skin module is plausible but is not demonstrated by the supplied co-abundance data.

#### CTSC

- **Related proteins** (co-abundance neighbors): NRAS (0.83), CDC50A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cathepsin C. This gene encodes a member of the peptidase C1 family and lysosomal cysteine proteinase that appears to be a central coordinator for activation of many serine proteinases in cells of the immune system. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate heavy and light chains that form a disulfide…
- **Diseases (Open Targets)**: Papillon-Lefevre disease (0.837); Haim-Munk syndrome (0.802); periodontitis, aggressive 1 (0.676); periodontitis, aggressive (0.573); periodontitis (0.560)
- **Europe PMC papers**: 4518
- **Why important**: CTSC has substantial literature, the second-highest network connectivity, and links CDC50A to NRAS. It is included in (GO:CC endoplasmic reticulum; q_global = 0.0155) and both supplementary STRING ER terms (STRING Component Endoplasmic reticulum; within-query FDR = 0.0063) (STRING COMPARTMENTS Endoplasmic reticulum; within-query FDR = 0.0495). Its established lysosomal cysteine-protease function and role in activating immune-cell serine proteases, together with associations with Papillon-Lefevre disease and periodontitis, make it relevant to tissue remodeling and inflammatory biology. HPA detects it in skin and reports cell-type enhancement in macrophage-related populations, although blood-cell specificity is low.
- **Conclusion**: Established evidence supports CTSC as a vesicular or protease-related component that may connect membrane trafficking to tissue and immune processes. A direct functional coupling to CDC50A or NRAS in this module remains a hypothesis.

## Module 13

**Tissue pair**: bone and skin  
**Genes (6)**: COQ9, ETFA, GOSR1, HSD17B10, IMMT, MRPL52

### Function

The module is most consistent with a mitochondrial maintenance and energy-metabolism program, with additional links to mitochondrial translation, inner-membrane architecture, and secretory trafficking. The strongest structural clue is a co-abundance hub formed by MRPL52, which connects to COQ9, HSD17B10, IMMT, and GOSR1, while HSD17B10 also connects to ETFA. The gene annotations support mitochondrial translation through MRPL52, ubiquinone production through COQ9, fatty-acid and lipid metabolism through HSD17B10 and ETFA, and cristae organization through IMMT. GOSR1 adds a vesicle-transport component. No GO or KEGG term passed global correction, so these functional assignments are gene-level interpretations rather than globally significant enrichment claims. The STRING riboflavin and coenzyme-Q disorder result (STRING WikiPathways Riboflavin and CoQ disorders; within-query FDR = 0.0341) is supplementary only.

**Cell composition.** The module is not composed of secreted proteins and is not blood-cell enriched according to HPA: all genes have low immune-cell specificity and no secreted genes were identified. All module proteins were detected in skin, supporting biological relevance to the sampled skin tissue. However, the module is not uniformly skin-specific. Some genes are tissue enhanced in tongue, skeletal muscle, or liver, while others have low tissue specificity. Cell-type annotations include hepatocytes, esophageal epithelial populations, platelets, and other low-specificity patterns. Thus, the shared bone-skin signal is more plausibly a broadly relevant mitochondrial or cellular metabolic program than a blood-contamination signature, although shared cell composition and general tissue metabolic state remain possible explanations.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the stated high-confidence threshold, and no hu.MAP complex contained multiple module members. Therefore, the co-abundance edges are not corroborated here as established high-confidence physical interactions or as membership in a recognized multi-member complex. The supplementary STRING association (STRING WikiPathways Riboflavin and CoQ disorders; within-query FDR = 0.0341) links COQ9 and ETFA to a riboflavin and coenzyme-Q disorder pathway, which is biologically compatible with mitochondrial metabolism but is not globally corrected enrichment. The absence of STRING and hu.MAP support argues for caution: the network may reflect coordinated regulation, shared tissue abundance, or indirect pathway coupling rather than a single physical complex.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: WikiPathways Riboflavin and CoQ disorders (FDR = 0.0341, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially interesting conserved co-abundance pattern, but it cannot be claimed as a new biological discovery from the present evidence alone. The pattern is not represented by a recognized STRING interaction set or a hu.MAP multi-member complex, which makes the particular co-abundance configuration less obviously established. Nevertheless, every gene has an existing biological annotation, and the mitochondrial, metabolic, cristae, translation, and trafficking functions are already known individually. The lack of globally significant GO or KEGG enrichment also limits claims of a newly defined pathway. Novelty would require independent replication in bone and skin, comparison with published co-expression or proteomic modules, and testing whether the same gene-level relationships persist after adjustment for cell composition and tissue-wide mitochondrial abundance.

**Hypothesis.** Hypothesis: the module represents coordinated mitochondrial quality and energy-support activity shared by bone and skin cells. In this model, MRPL52 reflects mitochondrial protein synthesis, IMMT reflects maintenance of inner-membrane and cristae architecture, COQ9 supports ubiquinone production, and HSD17B10 together with ETFA supports lipid and fatty-acid oxidation. GOSR1 may represent a linked requirement for intracellular membrane trafficking. The observed co-abundance could therefore arise when tissues increase mitochondrial capacity and membrane-handling activity together, but this mechanistic interpretation remains a hypothesis because the module lacks globally significant enrichment and high-confidence external interaction support.

### Important genes

#### MRPL52

- **Related proteins** (co-abundance neighbors): COQ9 (0.84), HSD17B10 (0.84), IMMT (0.81), GOSR1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial ribosomal protein L52. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.511); type 2 diabetes mellitus (0.206); breast cancer (0.076); prostate carcinoma (0.066); Dupuytren Contracture (0.054)
- **Europe PMC papers**: 220
- **Why important**: MRPL52 is the network hub, connecting to COQ9, HSD17B10, IMMT, and GOSR1. Its annotated role in mitochondrial translation provides a central link between the module's mitochondrial metabolism and organelle-maintenance features. It is detected in skin, has low immune-cell specificity, and has a substantial literature base. Its disease associations include neurodegenerative disease and type two diabetes mellitus.
- **Conclusion**: Established evidence supports MRPL52 as the structural and mitochondrial-translation anchor of the module. It is reasonable to hypothesize that variation in mitochondrial protein synthesis helps coordinate the other module members, but the co-abundance data do not prove that MRPL52 regulates them.

#### HSD17B10

- **Related proteins** (co-abundance neighbors): MRPL52 (0.84), ETFA (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydroxysteroid 17-beta dehydrogenase 10. This gene encodes 3-hydroxyacyl-CoA dehydrogenase type II, a member of the short-chain dehydrogenase/reductase superfamily. The gene product is a mitochondrial protein that catalyzes the oxidation of a wide variety of fatty acids and steroids, and is a subunit of mitochondrial ribonuclease P, which is involved in tRNA maturation. The protein has been implicated in the development of Alzheimer dise…
- **Diseases (Open Targets)**: HSD10 mitochondrial disease (0.829); HSD10 disease, atypical type (0.703); neurodegenerative disease (0.555); mitochondrial disease (0.373); HSD10 disease, neonatal type (0.370)
- **Europe PMC papers**: 1064
- **Why important**: HSD17B10 bridges the MRPL52-centered portion of the network to ETFA. Its established functions include mitochondrial tRNA maturation, fatty-acid and lipid metabolism, and multiple oxidation reactions. It has a comparatively extensive literature base and is associated with HSD10 mitochondrial disease, atypical and neonatal HSD10 disease, and neurodegenerative disease.
- **Conclusion**: Established evidence makes HSD17B10 a plausible metabolic bridge within the module and a clinically informative gene. The hypothesis that it couples mitochondrial translation with fatty-acid oxidation in this tissue-shared module remains untested.

#### COQ9

- **Related proteins** (co-abundance neighbors): MRPL52 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coenzyme Q9. This locus represents a mitochondrial ubiquinone biosynthesis gene. The encoded protein is likely necessary for biosynthesis of coenzyme Q10, as mutations at this locus have been associated with autosomal-recessive neonatal-onset primary coenzyme Q10 deficiency.[provided by RefSeq, Sep 2010].
- **Diseases (Open Targets)**: encephalopathy-hypertrophic cardiomyopathy-renal tubular disease syndrome (0.766); coenzyme Q10 deficiency (0.635); hereditary disease (0.415); mitochondrial disease (0.372); coenzyme Q10 deficiency, primary, 1 (0.370)
- **Europe PMC papers**: 958
- **Why important**: COQ9 is directly connected to the module hub and is annotated as a mitochondrial ubiquinone biosynthesis factor. It is also one of the two genes in the supplementary STRING result (STRING WikiPathways Riboflavin and CoQ disorders; within-query FDR = 0.0341) and is associated with primary coenzyme-Q deficiency and a multisystem encephalopathy-cardiomyopathy-renal syndrome. Its tissue annotation includes skeletal muscle and tongue, and it is detected in skin.
- **Conclusion**: Established evidence supports COQ9 as the clearest coenzyme-Q and respiratory-metabolism component of the module. It may mark energetic demand or respiratory capacity in the shared tissues, but (STRING WikiPathways Riboflavin and CoQ disorders; within-query FDR = 0.0341) is supplementary and does not establish module-wide pathway enrichment.

#### ETFA

- **Related proteins** (co-abundance neighbors): HSD17B10 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein subunit alpha. ETFA participates in catalyzing the initial step of the mitochondrial fatty acid beta-oxidation. It shuttles electrons between primary flavoprotein dehydrogenases and the membrane-bound electron transfer flavoprotein ubiquinone oxidoreductase. Defects in electron-transfer-flavoprotein have been implicated in type II glutaricaciduria in which multiple acyl-CoA dehydrogenase deficiencies result in l…
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.834); glutaric aciduria (0.756); hereditary disease (0.469); multiple acyl-CoA dehydrogenase deficiency, mild type (0.370); multiple acyl-CoA dehydrogenase deficiency, severe neonatal type (0.370)
- **Europe PMC papers**: 1433
- **Why important**: ETFA is connected to HSD17B10 and supplies a direct mitochondrial electron-transfer and fatty-acid beta-oxidation function. It is the second gene in the supplementary STRING finding (STRING WikiPathways Riboflavin and CoQ disorders; within-query FDR = 0.0341), has a substantial literature base, and is associated with multiple acyl-CoA dehydrogenase deficiency and glutaric aciduria. HPA places it in liver- and tongue-enhanced contexts and in hepatocyte and platelet-associated annotations, while it is also detected in skin.
- **Conclusion**: Established evidence identifies ETFA as a key fatty-acid oxidation and electron-transfer component. Its co-abundance with HSD17B10 supports a plausible metabolic submodule, but the available evidence does not show that this relationship is a direct physical interaction or specific to bone and skin.

#### IMMT

- **Related proteins** (co-abundance neighbors): MRPL52 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inner membrane mitochondrial protein. Enables RNA binding activity. Involved in cristae formation. Located in mitochondrial inner membrane. Part of MICOS complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); multinodular goiter (0.196); alcohol drinking (0.190); breast cancer (0.094); neoplasm (0.087)
- **Europe PMC papers**: 933
- **Why important**: IMMT is connected to the network hub and is an established component of the MICOS complex, with roles in inner-membrane organization and cristae formation. It is detected in skin and has a substantial literature base, with reported associations including neurodegenerative disease and multinodular goiter. Its structural role complements the metabolic annotations of COQ9, HSD17B10, and ETFA.
- **Conclusion**: Established evidence supports IMMT as the module's mitochondrial architecture marker. A reasonable hypothesis is that cristae organization coordinates respiratory and lipid-oxidation capacity in the shared tissues, but the module does not demonstrate that causal mechanism.

## Module 14

**Tissue pair**: bone and skin  
**Genes (5)**: DNAJB12, TBRG4, GNS, POLDIP2, TMX1

### Function

No GO or KEGG term passed global correction, so the module does not have a globally significant pathway annotation. The gene-level evidence nevertheless points to a mixed cellular-maintenance module. DNAJB12 and TMX1 support endoplasmic-reticulum protein folding, protein quality control, disulfide-bond handling, ER stress responses, and ER-associated degradation. GNS supports lysosomal degradation of glycosaminoglycans. TBRG4 is mitochondrial, but the fact sheet supplies no functional annotation for it. POLDIP2 is associated with DNA polymerase delta and error-free translesion synthesis. The co-abundance graph is centered on DNAJB12, which connects to every other module member, whereas the remaining genes are peripheral. Thus, the safest interpretation is a cellular proteostasis and stress-associated module with additional lysosomal, mitochondrial, and genome-maintenance components, rather than a single established pathway. The absence of enriched GO or KEGG terms does not invalidate the module.

**Cell composition.** The HPA profile argues against a blood-cell or plasma-protein explanation as the primary interpretation. Most genes have low tissue specificity and low immune-cell specificity, although GNS is immune-cell enhanced and associated with non-classical monocytes. The module includes two secreted genes according to the HPA summary, but the gene-level entries describe TMX1 and GNS as intracellular or membrane-associated rather than classical soluble secreted proteins. Skin protein detection is reported for DNAJB12, TMX1, GNS, and TBRG4, while POLDIP2 has no matching detection. The cell-type enrichments are dispersed across reproductive, trophoblast, adrenal, epithelial, hepatic, and immune populations, with no single shared cell type dominating. POLDIP2 has tissue-enhanced expression in skeletal muscle. Overall, broad expression and mixed cell-type associations suggest that the bone-skin conservation may reflect a shared cellular state or cell composition rather than a tissue-exclusive program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional-enrichment term was reported, and none of the possible within-module gene pairs reached the stated STRING interaction threshold. Therefore, STRING provides no high-confidence known interaction support for the co-abundance edges. hu.MAP supplies a more specific piece of evidence: GNS and POLDIP2 co-occur in (hu.MAP huMAP3_08944.1), (hu.MAP huMAP3_10485.1), and (hu.MAP huMAP3_11879.1), each of which also contains proteins outside this module. This repeated pairwise complex membership supports a possible relationship between GNS and POLDIP2, but it does not establish that the entire five-gene module is one physical complex. DNAJB12, TMX1, and TBRG4 have no reported hu.MAP membership here. The discrepancy between the co-abundance network and the absence of STRING edges indicates that the module is primarily an expression or abundance-coordination signal, not a validated protein-interaction network.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08944.1 (GNS, POLDIP2; 2/4); huMAP3_10485.1 (GNS, POLDIP2; 2/7); huMAP3_11879.1 (GNS, POLDIP2; 2/7)

### Novelty

This is a potentially novel conserved bone-skin co-abundance pattern, but the fact sheet does not establish it as a newly discovered biological complex or pathway. The lack of STRING support and the partial hu.MAP overlap make the coordinated abundance pattern less familiar in interaction databases, yet database absence alone cannot prove novelty. The absence of globally significant GO or KEGG enrichment also means there is no independently validated pathway label. A defensible claim is that the tissue-pair co-abundance association is a candidate finding requiring replication, cell-composition control, and orthogonal validation, rather than a confirmed novel mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated handling of cellular stress and macromolecular quality control in cells shared between bone and skin. DNAJB12 may act as the abundance-network hub linking ER chaperone activity to TMX1-mediated disulfide and ER quality-control processes, while GNS contributes lysosomal turnover of extracellular-matrix-related glycosaminoglycans. TBRG4 and POLDIP2 may mark accompanying mitochondrial and genome-maintenance demands. The repeated hu.MAP association of GNS with POLDIP2 suggests a possible connection between lysosomal substrate processing and cellular maintenance, but this is only a hypothesis because the module lacks STRING support, lacks globally significant enrichment, and contains genes from distinct annotated compartments.

### Important genes

#### DNAJB12

- **Related proteins** (co-abundance neighbors): TMX1 (0.85), GNS (0.82), TBRG4 (0.81), POLDIP2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane, Endoplasmic reticulum; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DnaJ heat shock protein family (Hsp40) member B12. DNAJB12 belongs to the evolutionarily conserved DNAJ/HSP40 family of proteins, which regulate molecular chaperone activity by stimulating ATPase activity. DNAJ proteins may have up to 3 distinct domains: a conserved 70-amino acid J domain, usually at the N terminus; a glycine/phenylalanine (G/F)-rich region; and a cysteine-rich domain containing 4 motifs resembling a zinc finger domain (Ohtsuka an…
- **Diseases (Open Targets)**: renal cell carcinoma (0.220); mathematical ability (0.184); stroke disorder (0.156); alcohol drinking (0.156); Abnormality of refraction (0.156)
- **Europe PMC papers**: 415
- **Why important**: DNAJB12 is the network hub, connecting to every other module member in the supplied graph. Its HSP40-family function provides the clearest organizing biology: stimulation of chaperone activity, protein folding, ER-associated degradation, complex assembly, and responses to misfolded proteins. It is detected in skin and has a substantial literature base, making it the strongest candidate for coordinating the module's abundance pattern.
- **Conclusion**: Established evidence supports DNAJB12 as an ER-associated proteostasis factor and as the central co-abundance connector. It is plausible, but unproven, that DNAJB12 helps coordinate the other module genes in bone and skin.

#### TMX1

- **Related proteins** (co-abundance neighbors): DNAJB12 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin related transmembrane protein 1. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, a catalytically active thioredoxin domain, and one transmembrane domain. Unlike most members of this gene family, it lacks a C-terminal ER-retention sequence. The …
- **Diseases (Open Targets)**: adolescent idiopathic scoliosis (0.247); Alkalosis (0.193); cutaneous lupus erythematosus (0.180); cleft lip (0.137); cleft palate (0.106)
- **Europe PMC papers**: 415
- **Why important**: TMX1 is the direct network partner of DNAJB12 and is an ER membrane thioredoxin-family protein involved in protein folding, thiol-disulfide interchange, ER stress responses, calcium transport regulation, and ER-associated degradation. Its skin detection and substantial literature base strengthen its relevance to a skin-associated proteostasis interpretation.
- **Conclusion**: Established evidence supports TMX1 as an ER redox and quality-control component linked to the module hub. Its role as a functional partner within this particular conserved tissue module remains a hypothesis because no STRING interaction was reported.

#### GNS

- **Related proteins** (co-abundance neighbors): DNAJB12 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_08944.1, huMAP3_10485.1, huMAP3_11879.1
- **Function (MyGene.info)**: glucosamine (N-acetyl)-6-sulfatase. The product of this gene is a lysosomal enzyme found in all cells. It is involved in the catabolism of heparin, heparan sulphate, and keratan sulphate. Deficiency of this enzyme results in the accumulation of undegraded substrate and the lysosomal storage disorder mucopolysaccharidosis type IIID (Sanfilippo D syndrome). Mucopolysaccharidosis type IIID is the least common of the four subtypes of Sa…
- **Diseases (Open Targets)**: mucopolysaccharidosis type 3D (0.811); mucopolysaccharidosis type 3 (0.610); mucopolysaccharidosis (0.372); ventricular fibrillation (0.233); preeclampsia (0.223)
- **Europe PMC papers**: 3078
- **Why important**: GNS connects to DNAJB12 and is the most functionally distinctive lysosomal gene in the module. It catalyzes degradation of heparin, heparan sulfate, and keratan sulfate and is linked to mucopolysaccharidosis type three D. It is present in all three reported hu.MAP complexes with POLDIP2, has the largest literature base among the module genes, and is detected in skin. Its immune-cell enhancement also makes it important for evaluating cellular-composition effects.
- **Conclusion**: Established evidence supports GNS as a lysosomal glycosaminoglycan-catabolism enzyme with a strong disease association. Its connection to ER proteostasis or POLDIP2 in this module is not established and should be treated as a testable hypothesis.

#### POLDIP2

- **Related proteins** (co-abundance neighbors): DNAJB12 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08944.1, huMAP3_10485.1, huMAP3_11879.1
- **Function (MyGene.info)**: DNA polymerase delta interacting protein 2. This gene encodes a protein that interacts with the DNA polymerase delta p50 subunit, as well as with proliferating cell nuclear antigen. The encoded protein maybe play a role in the ability of the replication fork to bypass DNA lesions. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.333); brain ischemia (0.091); breast cancer (0.082); breast carcinoma (0.077); familial thoracic aortic aneurysm and aortic dissection (0.066)
- **Europe PMC papers**: 510
- **Why important**: POLDIP2 is a peripheral network member but repeatedly co-occurs with GNS in (hu.MAP huMAP3_08944.1), (hu.MAP huMAP3_10485.1), and (hu.MAP huMAP3_11879.1). Its annotated interaction with DNA polymerase delta and PCNA, together with its role in error-free translesion synthesis, gives the module a genome-maintenance dimension. It is tissue enhanced in skeletal muscle, detected in several epithelial and hepatic cell types, and has a substantial literature base.
- **Conclusion**: Established evidence supports POLDIP2 as a DNA-replication and lesion-bypass-associated protein and supports repeated partial-complex membership with GNS. Any role in linking genome maintenance to the ER or lysosomal biology of this module is speculative.

#### TBRG4

- **Related proteins** (co-abundance neighbors): DNAJB12 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: not available
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 602
- **Why important**: TBRG4 is a peripheral module member located in mitochondria and connects directly to the DNAJB12 hub. Although the fact sheet provides no MyGene.info or Open Targets annotation for TBRG4, it has a meaningful literature record and cell-type-enhanced expression in trophoblast and germ-cell populations. Its inclusion adds a mitochondrial component that should not be ignored when testing the module's cellular-stress interpretation.
- **Conclusion**: Established evidence from the fact sheet is limited to mitochondrial localization, network placement, and expression associations. A role for TBRG4 in the proposed proteostasis or stress mechanism is currently a hypothesis, not an established conclusion.
