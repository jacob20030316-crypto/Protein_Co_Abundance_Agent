# Conserved co-abundance modules: liver and prostate

## Module 0

**Tissue pair**: liver and prostate  
**Genes (14)**: PPP2R2A, ADAM10, ELMOD2, HEXA, IDH3A, LSM6, MAP2K3, NDUFV1, PDHB, TFAM, UBA3, UCHL5, ATP6V1C1, TJP2

### Function

The module does not support a single strongly established biological function from enrichment analysis: no GO or KEGG term passed global correction, and there were no supplementary STRING-enrichment terms. The most coherent functional signal is mitochondrial energy and carbon metabolism, represented by PDHB, IDH3A, NDUFV1 and TFAM. PDHB links pyruvate metabolism to the tricarboxylic acid cycle, IDH3A catalyzes a tricarboxylic-acid-cycle reaction, NDUFV1 participates in respiratory-chain electron transfer, and TFAM supports mitochondrial transcription, DNA replication and repair. Other members implicate lysosomal carbohydrate degradation, proteostasis, RNA splicing, MAPK signaling, cell junctions and vesicle acidification. The sparse network therefore appears functionally mixed rather than a canonical pathway module. The mitochondrial interpretation is a biologically plausible theme, not a globally significant GO or KEGG enrichment result.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the HPA summary identifies only a small minority as secreted, and most proteins are intracellular. It is also not broadly blood-cell specific according to HPA, although several genes show cell-type-enhanced patterns involving neutrophils, trophoblast-related cells, spermatids and other specialized cell types. Most genes have low tissue specificity, while a few show tissue enhancement in tongue or bone marrow. Protein detection is generally present in both liver and prostate, with some genes detected in only one of the two tissues. These observations are compatible with a shared housekeeping or cellular-state signal, possibly influenced by common cell types or sample composition, but they do not establish that the module is caused by blood contamination or a particular infiltrating population.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The known high-confidence STRING relationships are concentrated in a mitochondrial metabolic triangle involving IDH3A, PDHB and NDUFV1. PDHB is connected to IDH3A and NDUFV1, and IDH3A is also connected to NDUFV1. These interactions support a real biochemical relationship among part of the module, but they do not explain the entire co-abundance structure. The remaining module relationships are not represented by high-confidence STRING partners in the fact sheet. No hu.MAP complex contains at least two module members. Thus, the module is not a recovered known protein complex; it combines a partly known mitochondrial interaction group with additional associations that may reflect co-regulation, shared cellular state or indirect biology.

**STRING interactions (score >= 0.7)**: 3 of 91 gene pairs: IDH3A–NDUFV1 (0.722); IDH3A–PDHB (0.856); NDUFV1–PDHB (0.738)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The cross-tissue co-abundance observation may be a potentially new combination of genes shared by liver and prostate, but the fact sheet does not establish a new molecular mechanism. Several component genes and the mitochondrial relationships among IDH3A, PDHB and NDUFV1 are already well characterized, and the module has no globally significant GO or KEGG annotation, no STRING functional-enrichment result and no multi-member hu.MAP complex. Absence from STRING or hu.MAP alone cannot prove novelty. The most defensible conclusion is that the cross-tissue co-abundance pattern is potentially novel at the module level, while its strongest biochemical substructure is established and the overall mechanism remains unvalidated. Independent replication, preservation testing and experimental or perturbational validation would be required before claiming a new conserved biological program.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular metabolic and quality-control state present in liver and prostate cells. Mitochondrial carbon flux and respiratory capacity may covary through PDHB, IDH3A, NDUFV1 and TFAM, while ubiquitin-related regulation, lysosomal processing, vesicle acidification, RNA handling and epithelial or cell-junction processes track the same cellular state. The observed co-abundance could therefore represent coordinated adaptation to energetic, proteostatic or stress-related demands rather than one physical complex. HPA cell-type patterns also raise the alternative possibility that shared specialized cell populations contribute to the signal. This hypothesis is not demonstrated by the enrichment results and should be tested with cell-resolved data and measurements of mitochondrial activity, protein turnover and tissue composition.

### Important genes

#### PDHB

- **Related proteins** (co-abundance neighbors): ELMOD2 (0.87), IDH3A (0.82); STRING partners: IDH3A (0.856), NDUFV1 (0.738)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyruvate dehydrogenase E1 subunit beta. The pyruvate dehydrogenase (PDH) complex is a nuclear-encoded mitochondrial multienzyme complex that catalyzes the overall conversion of pyruvate to acetyl-CoA and carbon dioxide, and provides the primary link between glycolysis and the tricarboxylic acid (TCA) cycle. The PDH complex is composed of multiple copies of three enzymatic components: pyruvate dehydrogenase (E1), dihydrolipoamide acetylt…
- **Diseases (Open Targets)**: pyruvate dehydrogenase E1-beta deficiency (0.796); pyruvate decarboxylase deficiency (0.672); pyruvate dehydrogenase phosphatase deficiency (0.421); neurodegenerative disease (0.392); hereditary disease (0.190)
- **Europe PMC papers**: 3002
- **Why important**: PDHB is a central metabolic member of the module, connecting pyruvate-derived carbon to acetyl-CoA and the tricarboxylic acid cycle. It is directly connected in STRING to IDH3A and NDUFV1, making it part of the module's clearest known biochemical substructure. Its mitochondrial localization and established association with pyruvate dehydrogenase deficiency further strengthen its biological interpretability. It has a substantial literature base and is detected in prostate, although not in liver in the supplied HPA immunohistochemistry summary.
- **Conclusion**: Established evidence supports PDHB as a mitochondrial carbon-metabolism gene and as a member of a known interaction group with IDH3A and NDUFV1. It is a strong anchor for the metabolic interpretation. It remains a hypothesis that PDHB drives the liver-prostate co-abundance pattern or coordinates the other module branches.

#### IDH3A

- **Related proteins** (co-abundance neighbors): PDHB (0.82); STRING partners: NDUFV1 (0.722), PDHB (0.856)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: isocitrate dehydrogenase (NAD(+)) 3 catalytic subunit alpha. Isocitrate dehydrogenases catalyze the oxidative decarboxylation of isocitrate to 2-oxoglutarate. These enzymes belong to two distinct subclasses, one of which utilizes NAD(+) as the electron acceptor and the other NADP(+). Five isocitrate dehydrogenases have been reported: three NAD(+)-dependent isocitrate dehydrogenases, which localize to the mitochondrial matrix, and two NADP(+)-dependent isoci…
- **Diseases (Open Targets)**: retinitis pigmentosa 90 (0.791); retinitis pigmentosa (0.467); neurodegenerative disease (0.437); inherited retinal dystrophy (0.381); colorectal carcinoma (0.182)
- **Europe PMC papers**: 1497
- **Why important**: IDH3A is a catalytic tricarboxylic-acid-cycle enzyme and is directly connected to PDHB and NDUFV1 in STRING. It therefore links central carbon metabolism with the respiratory-associated portion of the module. Its supplied disease associations include inherited retinal disease and broader neurodegenerative and cancer-related associations. Its HPA profile includes enhancement in plasmacytoid dendritic cells and detection in prostate, making cell composition a possible interpretive consideration. The literature is substantial.
- **Conclusion**: Established evidence supports IDH3A as a mitochondrial metabolic enzyme embedded in a known interaction subnetwork. It is an important indicator of the module's metabolic component. A role as a regulator of the conserved tissue-pair co-abundance state is only a hypothesis.

#### NDUFV1

- **Related proteins** (co-abundance neighbors): ADAM10 (0.82); STRING partners: IDH3A (0.722), PDHB (0.738)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit V1. The mitochondrial respiratory chain provides energy to cells via oxidative phosphorylation and consists of four membrane-bound electron-transporting protein complexes (I-IV) and an ATP synthase (complex V). This gene encodes a 51 kDa subunit of the NADH:ubiquinone oxidoreductase complex I; a large complex with at least 45 nuclear and mitochondrial encoded subunits that liberates electrons from NAD…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.788); mitochondrial complex I deficiency, nuclear type 4 (0.724); mitochondrial complex I deficiency, nuclear type 1 (0.685); Leigh syndrome (0.635); type 2 diabetes mellitus (0.609)
- **Europe PMC papers**: 4567
- **Why important**: NDUFV1 is a core subunit of mitochondrial respiratory complex I and participates in NADH-linked electron transfer and ATP production. It is connected in STRING to both PDHB and IDH3A, providing a plausible bridge between respiratory function and tricarboxylic-acid-cycle metabolism. Its disease associations include mitochondrial complex I deficiency and Leigh syndrome, and it has a substantial literature base. It is detected in both liver and prostate in the supplied HPA evidence.
- **Conclusion**: Established evidence supports NDUFV1 as a respiratory-chain component and as part of the known mitochondrial interaction group in this module. It supports an energy-state interpretation. It is not established that variation in NDUFV1 explains the full module or its conservation between tissues.

#### TFAM

- **Related proteins** (co-abundance neighbors): ADAM10 (0.87), ELMOD2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Mitochondria; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transcription factor A, mitochondrial. This gene encodes a key mitochondrial transcription factor containing two high mobility group motifs. The encoded protein also functions in mitochondrial DNA replication and repair. Sequence polymorphisms in this gene are associated with Alzheimer's and Parkinson's diseases. There are pseudogenes for this gene on chromosomes 6, 7, and 11. Alternative splicing results in multiple transcript variant…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome 15 (hepatocerebral type) (0.689); neurodegenerative disease (0.550); stroke disorder (0.191); alcohol drinking (0.189); musculoskeletal system disorder (0.132)
- **Europe PMC papers**: 14423
- **Why important**: TFAM is a mitochondrial transcription factor with roles in mitochondrial DNA replication and repair, providing a regulatory complement to the enzymatic mitochondrial genes. It has a relatively prominent network connection to ELMOD2 and is detected in both tissues. HPA reports enrichment in early and late spermatid cell types, which makes cell-type composition relevant when interpreting the prostate signal. Its disease associations include hepatocerebral mitochondrial DNA depletion and neurodegenerative disease, and it has an extensive literature base.
- **Conclusion**: Established evidence supports TFAM as a mitochondrial genome-maintenance and transcription factor. It strengthens the hypothesis that mitochondrial state contributes to the module. The supplied data do not show a direct known complex or STRING interaction linking TFAM to the IDH3A-PDHB-NDUFV1 group, so that integration remains hypothetical.

#### TJP2

- **Related proteins** (co-abundance neighbors): ATP6V1C1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cell Junctions; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tight junction protein 2. This gene encodes a zonula occluden that is a member of the membrane-associated guanylate kinase homolog family. The encoded protein functions as a component of the tight junction barrier in epithelial and endothelial cells and is necessary for proper assembly of tight junctions. Mutations in this gene have been identified in patients with hypercholanemia, and genomic duplication of a 270 kb regio…
- **Diseases (Open Targets)**: cholestasis, progressive familial intrahepatic, 4 (0.800); hypercholanemia, familial 1 (0.647); autosomal dominant nonsyndromic hearing loss (0.558); progressive familial intrahepatic cholestasis type 2 (0.527); deafness (0.467)
- **Europe PMC papers**: 1748
- **Why important**: TJP2 provides a non-mitochondrial axis that is important for interpreting the module. It encodes a tight-junction component involved in epithelial barrier organization and cell-cell adhesion, is detected in both liver and prostate, and connects in the co-abundance graph to ATP6V1C1. Its disease associations include progressive familial intrahepatic cholestasis, hypercholanemia and hearing loss. Its HPA cell-type enhancements span several epithelial and glial populations, while non-classical monocyte enhancement suggests that cellular composition may influence its abundance.
- **Conclusion**: Established evidence supports TJP2 as an epithelial junction and barrier protein with clinically relevant liver-associated disease links. Its presence argues against treating the module as a purely mitochondrial pathway. A coordinated relationship between epithelial integrity, vesicle acidification and mitochondrial metabolism is a plausible but unproven explanation for its co-abundance with the metabolic genes.

## Module 1

**Tissue pair**: liver and prostate  
**Genes (43)**: SLC3A2, PGD, FDXR, ATXN10, BCS1L, HSPA5, CS, CNOT1, MT-CO2, DPP3, EMC1, ERO1A, FKBP4, GFPT1, COLGALT1, HSPA8, HYOU1, DTYMK, LYPLA1, EEF1E1, SLC16A1, NDUFS1, SNU13, NPM3, ALDH18A1, PHB2, PNPT1, CTSA, PRDX4, PSMA1, ATIC, SYNGR2, SPR, CTTN, SRP68, IARS2, NARS1, RARS1, SARS1, TARS1, CCT8, TMEM70, TTLL12

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. The gene-level evidence nevertheless supports a composite cellular maintenance module rather than a narrowly tissue-specific pathway. Its central features are cytoplasmic translation and tRNA aminoacylation, mitochondrial RNA handling and energy metabolism, protein folding and proteostasis, endoplasmic-reticulum processing, and nucleotide or carbohydrate metabolism. The network core is especially connected to aminoacyl-tRNA synthetases, chaperones, and mitochondrial proteins. This pattern is consistent with coordinated abundance of machinery that supports protein production, folding, mitochondrial function, and cellular stress adaptation. The functional interpretation is therefore biologically plausible but should not be described as statistically confirmed pathway enrichment.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only a minority are annotated as secreted, while most have intracellular localizations. HPA indicates broadly distributed expression for most genes, with low tissue specificity and low immune-cell specificity predominating. Protein detection is frequent in both liver and prostate, supporting a shared cellular program, although detection does not establish tissue specificity. Several genes show enrichment in particular cell types, including epithelial, reproductive, muscle, trophoblast, and myeloid-associated populations. Thus, the module is more consistent with broadly expressed housekeeping and stress or metabolic machinery than with a blood-cell module. Some co-abundance could still reflect shared cell types or sample composition, especially given the cell-type-enriched genes, but the HPA evidence does not support a predominantly blood-derived or secreted interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports established relationships in several local neighborhoods. The aminoacyl-tRNA synthetase cluster includes IARS2, NARS1, RARS1, SARS1, and TARS1, with EEF1E1 linked to the synthetase machinery. The chaperone neighborhood includes HSPA5, HSPA8, HYOU1, CCT8, and FKBP4, while mitochondrial relationships include BCS1L, MT-CO2, NDUFS1, CS, and ALDH18A1. hu.MAP independently places module members in complexes involving mitochondrial RNA and metabolic machinery (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1), aminoacyl-tRNA synthetase assemblies (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), stress-related chaperones (hu.MAP huMAP3_07455.1), mitochondrial prohibitin machinery (hu.MAP huMAP3_09122.1), and additional metabolic or membrane-associated complexes (hu.MAP huMAP3_14442.1) and (hu.MAP huMAP3_09592.1). These known interactions and complexes indicate that the co-abundance network is anchored by real cellular systems rather than being composed entirely of isolated associations. They also suggest that some edges reflect shared complex membership or common cellular demand, not necessarily direct physical interaction.

**STRING interactions (score >= 0.7)**: 28 of 903 gene pairs: ALDH18A1–CS (0.704); ALDH18A1–FDXR (0.887); BCS1L–MT-CO2 (0.831); BCS1L–NDUFS1 (0.73); CCT8–HSPA5 (0.701); CCT8–HSPA8 (0.905); CCT8–PSMA1 (0.797); CS–IARS2 (0.702); CS–NDUFS1 (0.737); CS–PGD (0.709); EEF1E1–IARS2 (0.772); EEF1E1–RARS1 (0.996); ERO1A–HSPA5 (0.875); FKBP4–HSPA8 (0.942); HSPA5–HSPA8 (0.983); HSPA5–HYOU1 (0.999); HSPA8–HYOU1 (0.746); IARS2–NARS1 (0.889); IARS2–RARS1 (0.979); IARS2–SARS1 (0.904); IARS2–TARS1 (0.89); MT-CO2–NDUFS1 (0.976); NARS1–RARS1 (0.909); NARS1–SARS1 (0.843); NARS1–TARS1 (0.924); RARS1–SARS1 (0.933); RARS1–TARS1 (0.806); SARS1–TARS1 (0.915)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (FDXR, ALDH18A1, PNPT1, IARS2; 4/99); huMAP3_02637.1 (EEF1E1, TARS1, RARS1; 3/14); huMAP3_13688.1 (EEF1E1, TARS1, RARS1; 3/14); huMAP3_10525.1 (FDXR, ALDH18A1, IARS2; 3/33); huMAP3_09122.1 (DTYMK, PHB2; 2/3); huMAP3_07455.1 (HSPA5, HYOU1; 2/4); huMAP3_14442.1 (ATIC, PGD; 2/57); huMAP3_09592.1 (TMEM70, ATXN10; 2/95)

### Novelty

The module should not be claimed as a wholly new biological function. Its major components and many of its relationships are already represented in STRING and hu.MAP, and the underlying processes are well established. The potentially novel result is the conserved co-abundance configuration across liver and prostate, particularly the joint coupling of translation machinery, mitochondrial metabolism, and proteostasis. However, absence of a matching STRING or hu.MAP entity would not by itself prove novelty, and the supplied evidence does not provide a formal comparison with previously reported tissue co-abundance modules. The most defensible conclusion is that this may be a new systems-level observation or repurposing of known machinery, not a newly discovered molecular pathway.

**Hypothesis.** Hypothesis: the shared liver–prostate module represents a coordinated proteostasis and bioenergetic maintenance state. High translational demand or cellular stress may couple aminoacyl-tRNA charging with cytoplasmic and endoplasmic-reticulum chaperoning, while mitochondrial RNA processing, respiratory-chain function, amino-acid metabolism, and redox control maintain the energy and reducing capacity needed for protein synthesis and folding. This state could be shared by metabolically active epithelial cells in both organs, with individual cell-type-enriched genes reflecting local composition rather than defining the entire module. This mechanism is a testable interpretation, not an established causal model.

### Important genes

#### RARS1

- **Related proteins** (co-abundance neighbors): GFPT1 (0.94), EEF1E1 (0.90), DTYMK (0.88), CNOT1 (0.85), SNU13 (0.85), NARS1 (0.84), PNPT1 (0.82), EMC1 (0.82), PSMA1 (0.82), TARS1 (0.82), ALDH18A1 (0.81), CTSA (0.81), SLC3A2 (0.81), HYOU1 (0.81), CCT8 (0.81); STRING partners: EEF1E1 (0.996), IARS2 (0.979), NARS1 (0.909), SARS1 (0.933), TARS1 (0.806)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 is the most connected node among the supplied genes and links the co-abundance core to EEF1E1, NARS1, IARS2, and other translation-related proteins. Its established function is arginyl-tRNA aminoacylation, and it is broadly expressed with protein detected in both liver and prostate. Its disease associations include hypomyelinating leukodystrophy and related hereditary disorders, while its literature base is substantial. It is therefore a strong network and functional representative of the translation component.
- **Conclusion**: Established evidence supports RARS1 as a central translation-maintenance component of the module. Its centrality does not prove that it drives the module, but it makes coordinated translational capacity a credible interpretation.

#### ALDH18A1

- **Related proteins** (co-abundance neighbors): SRP68 (0.93), COLGALT1 (0.86), DTYMK (0.85), CTSA (0.85), PNPT1 (0.85), SLC3A2 (0.84), GFPT1 (0.82), TARS1 (0.82), FKBP4 (0.81), RARS1 (0.81), TTLL12 (0.81); STRING partners: CS (0.704), FDXR (0.887)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1
- **Function (MyGene.info)**: aldehyde dehydrogenase 18 family member A1. This gene is a member of the aldehyde dehydrogenase family and encodes a bifunctional ATP- and NADPH-dependent mitochondrial enzyme with both gamma-glutamyl kinase and gamma-glutamyl phosphate reductase activities. The encoded protein catalyzes the reduction of glutamate to delta1-pyrroline-5-carboxylate, a critical step in the de novo biosynthesis of proline, ornithine and arginine. Mutations in …
- **Diseases (Open Targets)**: ALDH18A1-related de Barsy syndrome (0.832); cutis laxa, autosomal dominant 3 (0.816); autosomal recessive complex spastic paraplegia type 9B (0.814); de Barsy syndrome (0.731); autosomal dominant spastic paraplegia type 9 (0.706)
- **Europe PMC papers**: 1168
- **Why important**: ALDH18A1 is a highly connected mitochondrial enzyme linking glutamate-derived amino-acid metabolism to the module. It participates in proline, ornithine, and arginine biosynthetic routes and is present in two of the mitochondrial hu.MAP complexes (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1). Its disease associations include de Barsy syndrome and hereditary spastic-paraplegia-related disorders, and it has a substantial literature base. Its HPA profile is tissue enhanced in salivary gland rather than liver or prostate, so its inclusion is more consistent with a shared metabolic program than with strict organ specificity.
- **Conclusion**: Established evidence supports ALDH18A1 as a mitochondrial metabolic bridge within the module. Its connection to the liver–prostate co-abundance pattern may reflect shared amino-acid and mitochondrial demand, but that tissue-level mechanism remains a hypothesis.

#### HSPA5

- **Related proteins** (co-abundance neighbors): HSPA8 (0.84); STRING partners: CCT8 (0.701), ERO1A (0.875), HSPA8 (0.983), HYOU1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_07455.1
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is a central ER chaperone and master regulator of ER homeostasis. It has strong STRING relationships with HSPA8, HYOU1, ERO1A, and CCT8 and belongs with HYOU1 in hu.MAP complex (hu.MAP huMAP3_07455.1). These links provide direct support for a proteostasis neighborhood. HSPA5 has extensive literature and disease associations involving stress, neurodegeneration, and cancer, although its broad functions make disease associations nonspecific for this module.
- **Conclusion**: Established evidence supports HSPA5 as an important proteostasis component and a plausible indicator of folding or ER-stress capacity. It should not be interpreted as proof that pathological ER stress caused the module because the co-abundance data are not causal.

#### IARS2

- **Related proteins** (co-abundance neighbors): SPR (0.84); STRING partners: CS (0.702), EEF1E1 (0.772), NARS1 (0.889), RARS1 (0.979), SARS1 (0.904), TARS1 (0.89)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 2, mitochondrial. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Two forms of isoleucine-tRNA synthetase exist, a cytoplasmic form and a mitochondrial form. This gene encodes th…
- **Diseases (Open Targets)**: cataract-growth hormone deficiency-sensory neuropathy-sensorineural hearing loss-skeletal dysplasia syndrome (0.724); Leigh syndrome (0.563); hereditary disease (0.416); neurodegenerative disease (0.411); mitochondrial disease (0.374)
- **Europe PMC papers**: 411
- **Why important**: IARS2 is a mitochondrial isoleucine-tRNA synthetase that connects mitochondrial translation with the broader synthetase cluster. It participates in hu.MAP complexes (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1) and has multiple STRING links to NARS1, RARS1, SARS1, and TARS1. Its established disease associations include Leigh syndrome and other mitochondrial or sensory-neurologic disorders. Although its network degree within the module is limited, its cross-compartment role makes it informative for linking translation to mitochondrial function.
- **Conclusion**: Established evidence supports IARS2 as a mitochondrial translation marker that reinforces the module’s integrated translation–mitochondrial interpretation. Its position does not establish direct functional coordination with every neighboring gene.

#### HYOU1

- **Related proteins** (co-abundance neighbors): TARS1 (0.92), TMEM70 (0.88), GFPT1 (0.86), SYNGR2 (0.84), RARS1 (0.81); STRING partners: HSPA5 (0.999), HSPA8 (0.746)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07455.1
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 is an ER-associated stress and folding protein with established roles in responses to hypoxia and ER stress, ER-to-Golgi transport, and protection from apoptosis. It is linked in STRING to HSPA5 and HSPA8 and is included in hu.MAP complex (hu.MAP huMAP3_07455.1). Its network connections also reach TARS1, GFPT1, TMEM70, and SYNGR2, placing stress adaptation between translation, metabolism, and membrane trafficking. Its disease associations include granulocytopenia with immunoglobulin abnormality and several stress-related disease areas.
- **Conclusion**: Established evidence supports HYOU1 as a stress-adaptation and protein-folding component. The hypothesis that it couples hypoxic or ER stress to the mitochondrial and translational parts of the module is plausible but not demonstrated by the supplied co-abundance data.

## Module 2

**Tissue pair**: liver and prostate  
**Genes (44)**: ABCF1, ABHD10, ACACA, ACSL3, PRMT5, AP3B1, CLUH, CTNND1, DDX6, DNAJB1, DNM1L, EIF3C, FUS, G6PD, GMDS, GMPPB, GTF2I, MAT2A, MIX23, NIBAN2, NTPCR, NUP205, NUDCD2, PAK2, PNP, PPP4C, PPM1G, PTGR3, UPF1, SNRPA1, SEC24C, PSAT1, SF3B3, SNRPD1, SUPV3L1, TACO1, CCT3, TECR, TXLNA, UCHL3, UNC45A, VAMP8, ATP6V1A, ZW10

### Function

This is a heterogeneous intracellular co-abundance module, not a module with a single globally validated GO or KEGG function. No GO/KEGG term passed global correction, and STRING functional enrichment was absent. The strongest coherent biological signals are RNA processing and post-transcriptional control, supported by the spliceosomal genes SNRPD1, SNRPA1, SF3B3, PRMT5, PPM1G, FUS, DDX6 and UPF1; lipid and fatty-acyl metabolism, supported by ACACA, ACSL3 and TECR; and protein synthesis, folding, organelle maintenance and trafficking, supported by EIF3C, CCT3, ATP6V1A, VAMP8, SEC24C, DNM1L and TACO1. The network may therefore reflect a shared cellular state involving biosynthetic activity, RNA handling, proteostasis and membrane or organelle homeostasis rather than a narrowly specialized liver or prostate pathway. The high-connectivity genes GTF2I and ABCF1 connect several of these processes, but their network centrality should not be interpreted as proof of a single causal mechanism.

**Cell composition.** The module is predominantly composed of broadly expressed intracellular proteins rather than plasma or secreted proteins. HPA assigns low tissue specificity to most genes, and there are no secreted genes. Protein detection is broad in both liver and prostate, consistent with a shared cellular program rather than a tissue-restricted secretory signature. Most genes also have low immune-cell specificity, so the module is not strongly indicative of blood-cell contamination. A minority of genes show cell-type-enhanced or cell-type-enriched patterns, including esophageal epithelial cells, trophoblast-related cells, spermatogenic cells, neutrophils, hepatocytes, epididymal cells and other specialized populations. These patterns may reflect broadly shared cellular machinery or differences in cellular composition, but the HPA summary does not support interpreting the module primarily as a blood or plasma-protein module. PPM1G, CLUH, MAT2A and PSAT1 lack protein detection in one or both relevant tissues, so co-abundance does not require uniform protein detection across all module members.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a set of internally coherent, already known relationships rather than broad coverage of the module. The clearest known interactions are the spliceosomal links among PRMT5, SNRPD1, SF3B3 and SNRPA1; the RNA surveillance or decay connection between DDX6 and UPF1; the glycan-related enzyme connection between GMDS and GMPPB; the lipid-related connection between ACACA and ACSL3; and the CCT3 to PPP4C relationship. These links support genuine biological structure within parts of the co-abundance module, while the absence of STRING partners for many highly connected co-abundance genes indicates that co-abundance extends beyond currently catalogued physical or functional interactions. hu.MAP independently identifies the spliceosomal group containing PRMT5, SNRPA1, SNRPD1 and SF3B3 in (hu.MAP huMAP3_06511.1), (hu.MAP huMAP3_08980.1) and (hu.MAP huMAP3_04549.1). It also places NUP205 with UNC45A in (hu.MAP huMAP3_09042.1), and ZW10 with VAMP8 in (hu.MAP huMAP3_06458.1), (hu.MAP huMAP3_08929.1) and (hu.MAP huMAP3_10587.1). The repeated spliceosomal complexes are the strongest complex-level support for a real molecular submodule. The pairs in the other hu.MAP complexes are more limited, so they support possible links but do not establish that the entire co-abundance module is one physical complex.

**STRING interactions (score >= 0.7)**: 8 of 946 gene pairs: ACACA–ACSL3 (0.797); CCT3–PPP4C (0.79); DDX6–UPF1 (0.93); GMDS–GMPPB (0.892); PRMT5–SNRPD1 (0.991); SF3B3–SNRPA1 (0.999); SF3B3–SNRPD1 (0.998); SNRPA1–SNRPD1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06511.1 (PRMT5, SNRPA1, SNRPD1, SF3B3; 4/79); huMAP3_08980.1 (PRMT5, SNRPA1, SNRPD1, SF3B3; 4/97); huMAP3_09042.1 (NUP205, UNC45A; 2/26); huMAP3_06458.1 (ZW10, VAMP8; 2/41); huMAP3_08929.1 (ZW10, VAMP8; 2/44); huMAP3_10587.1 (ZW10, VAMP8; 2/45); huMAP3_04549.1 (SNRPD1, SF3B3; 2/52)

### Novelty

The module is not adequately described as a wholly new molecular complex. Several of its relationships are established in STRING, and the spliceosomal subset is represented repeatedly in hu.MAP. At the same time, the full cross-tissue co-abundance pattern appears broader than those known complexes: many module genes have no STRING partner or hu.MAP assignment in the supplied evidence, and the module combines several biological systems rather than matching one catalogued complex. The defensible conclusion is that the potentially novel finding is the liver-prostate co-abundance organization and its coordination of RNA processing, lipid metabolism, translation, trafficking and organelle biology, not the discovery of the individual protein interactions themselves. Absence from STRING or hu.MAP alone cannot establish novelty. Independent replication, tissue-cellular deconvolution, perturbation experiments and comparison with existing cross-tissue co-expression resources would be needed to claim a new biological mechanism.

**Hypothesis.** Hypothesis: this module represents a shared homeostatic state in liver and prostate cells in which RNA maturation and surveillance are coordinated with translation, lipid synthesis, protein folding, vesicle trafficking and mitochondrial maintenance. In this model, the spliceosomal and RNA-control genes form a regulatory layer that determines which transcripts are processed and translated; ACACA, ACSL3 and TECR provide a lipid-biosynthetic layer; EIF3C, CCT3 and DNAJB1 support production and folding of proteins; and ATP6V1A, VAMP8, SEC24C, DNM1L and TACO1 support organelle, vesicle and mitochondrial function. This is a mechanistic hypothesis, not an enrichment result. The apparent coordination could instead arise from shared cell-state composition, generalized biosynthetic demand, or technical and sampling effects.

### Important genes

#### GTF2I

- **Related proteins** (co-abundance neighbors): ABCF1 (0.94), ACACA (0.88), TECR (0.87), PPM1G (0.85), CTNND1 (0.85), DDX6 (0.85), ACSL3 (0.85), CCT3 (0.85), SNRPD1 (0.84), ZW10 (0.84), PRMT5 (0.84), UPF1 (0.83), DNAJB1 (0.83), TXLNA (0.82), SF3B3 (0.82), AP3B1 (0.82), EIF3C (0.81), FUS (0.81), SNRPA1 (0.80), ATP6V1A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: general transcription factor IIi. This gene encodes a phosphoprotein containing six characteristic repeat motifs. The encoded protein binds to the initiator element (Inr) and E-box element in promoters and functions as a regulator of transcription. This locus, along with several other neighboring genes, is deleted in Williams-Beuren syndrome. There are many closely related genes and pseudogenes for this gene on chromosome 7. This …
- **Diseases (Open Targets)**: neurodegenerative disease (0.548); type 2 diabetes mellitus (0.520); atrial fibrillation (0.519); hypertensive disorder (0.500); Abnormality of the skeletal system (0.495)
- **Europe PMC papers**: 2606
- **Why important**: GTF2I has the strongest network position in the supplied module and connects transcriptional regulation with genes involved in lipid metabolism, RNA control, translation and protein handling. It is detected in both liver and prostate, has low tissue and immune specificity, and has substantial literature support. Its association with several disease areas makes it biologically notable, although the supplied evidence does not assign it to a hu.MAP complex or a STRING interaction within this module.
- **Conclusion**: Established evidence supports GTF2I as a highly connected, broadly expressed transcriptional regulator that may coordinate multiple module neighborhoods. It is a strong network marker, but there is no direct evidence here that it drives the shared liver-prostate pattern. A causal coordinating role remains a hypothesis.

#### ACACA

- **Related proteins** (co-abundance neighbors): GTF2I (0.88), SNRPD1 (0.87), NUP205 (0.87), CLUH (0.85), ZW10 (0.85), PRMT5 (0.84), EIF3C (0.84), SF3B3 (0.83), CTNND1 (0.82), NIBAN2 (0.82), ATP6V1A (0.81); STRING partners: ACSL3 (0.797)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA carboxylase alpha. Acetyl-CoA carboxylase (ACC) is a complex multifunctional enzyme system. ACC is a biotin-containing enzyme which catalyzes the carboxylation of acetyl-CoA to malonyl-CoA, the rate-limiting step in fatty acid synthesis. There are two ACC forms, alpha and beta, encoded by two different genes. ACC-alpha is highly enriched in lipogenic tissues. The enzyme is under long term control at the transcriptio…
- **Diseases (Open Targets)**: neurodegenerative disease (0.550); Alzheimer disease (0.463); lysosomal storage disease (0.460); Parkinson disease (0.460); autoimmune disorder of central nervous system (0.383)
- **Europe PMC papers**: 6268
- **Why important**: ACACA is a central module gene connected to GTF2I, SNRPD1, NUP205, CLUH, ZW10, PRMT5, EIF3C and SF3B3. It catalyzes the rate-limiting step in fatty-acid synthesis and is described as highly enriched in lipogenic tissues. It is detected in both liver and prostate and has substantial literature and disease-association support. Its known STRING relationship with ACSL3 gives the lipid-related portion of the module direct interaction evidence.
- **Conclusion**: Established evidence supports ACACA as the clearest metabolic anchor of the module and as a plausible link between lipid biosynthesis and the broader intracellular network. The data do not establish that ACACA activity causes the RNA-processing or trafficking associations; that cross-process connection remains a hypothesis.

#### PRMT5

- **Related proteins** (co-abundance neighbors): ACACA (0.84), GTF2I (0.84), PAK2 (0.82), ACSL3 (0.82), PPM1G (0.81), SNRPD1 (0.81); STRING partners: SNRPD1 (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: protein arginine methyltransferase 5. This gene encodes an enzyme that belongs to the methyltransferase family. The encoded protein catalyzes the transfer of methyl groups to the amino acid arginine, in target proteins that include histones, transcriptional elongation factors and the tumor suppressor p53. This gene plays a role in several cellular processes, including transcriptional regulation, and the assembly of small nuclear ribon…
- **Diseases (Open Targets)**: neurodegenerative disease (0.207); breast cancer (0.140); neoplasm (0.119); hepatocellular carcinoma (0.117); colorectal carcinoma (0.116)
- **Europe PMC papers**: 6035
- **Why important**: PRMT5 is a well-studied methyltransferase with a substantial literature base and disease associations. It is connected in the module to ACACA, GTF2I, PAK2, ACSL3, PPM1G and SNRPD1. Its established role in small nuclear ribonucleoprotein assembly is directly supported by STRING interaction with SNRPD1 and by hu.MAP complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1).
- **Conclusion**: Established evidence supports PRMT5 as an important RNA-processing and post-translational regulatory anchor, especially for the spliceosomal portion of the module. Its position near metabolic and signaling genes suggests possible cross-talk, but the supplied co-abundance data do not demonstrate that PRMT5 enzymatic activity regulates those processes.

#### SNRPD1

- **Related proteins** (co-abundance neighbors): ATP6V1A (0.90), TECR (0.89), CCT3 (0.87), ACACA (0.87), SF3B3 (0.86), GTF2I (0.84), CTNND1 (0.83), ABCF1 (0.82), PRMT5 (0.81); STRING partners: PRMT5 (0.991), SF3B3 (0.998), SNRPA1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1, huMAP3_04549.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein D1 polypeptide. This gene encodes a small nuclear ribonucleoprotein that belongs to the SNRNP core protein family. The protein may act as a charged protein scaffold to promote SNRNP assembly or strengthen SNRNP-SNRNP interactions through nonspecific electrostatic contacts with RNA. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.483); dengue disease (0.370); liver disorder (0.116); breast cancer (0.097); breast carcinoma (0.097)
- **Europe PMC papers**: 636
- **Why important**: SNRPD1 is a core small nuclear ribonucleoprotein protein with known roles in spliceosomal assembly and messenger RNA splicing. It participates in the strongest STRING-supported interaction cluster with PRMT5, SF3B3 and SNRPA1, and occurs in hu.MAP complexes (hu.MAP huMAP3_06511.1), (hu.MAP huMAP3_08980.1) and (hu.MAP huMAP3_04549.1). It is detected in both liver and prostate and has direct links to RNA processing in its supplied annotation.
- **Conclusion**: Established evidence supports SNRPD1 as a core component of a genuine spliceosomal submodule within the co-abundance network. It is therefore an important mechanistic marker, but it cannot by itself explain the lipid, mitochondrial or vesicle-related genes.

#### FUS

- **Related proteins** (co-abundance neighbors): ABCF1 (0.93), PPM1G (0.91), AP3B1 (0.86), DDX6 (0.83), SNRPA1 (0.83), SF3B3 (0.83), DNAJB1 (0.82), TXLNA (0.81), GTF2I (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FUS RNA binding protein. This gene encodes a multifunctional protein component of the heterogeneous nuclear ribonucleoprotein (hnRNP) complex. The hnRNP complex is involved in pre-mRNA splicing and the export of fully processed mRNA to the cytoplasm. This protein belongs to the FET family of RNA-binding proteins which have been implicated in cellular processes that include regulation of gene expression, maintenance of gen…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.710); sporadic amyotrophic lateral sclerosis (0.683); frontotemporal dementia with motor neuron disease (0.667); essential tremor (0.557); juvenile amyotrophic lateral sclerosis (0.527)
- **Europe PMC papers**: 19869
- **Why important**: FUS is a highly studied RNA-binding protein with extensive literature and strong disease associations, particularly involving neurodegenerative disease. It connects ABCF1, PPM1G, AP3B1, DDX6, SNRPA1, SF3B3, DNAJB1 and TXLNA in the module. Its established functions include RNA splicing, messenger RNA stabilization, gene regulation and maintenance of genomic integrity, while its HPA profile is broadly expressed and detected in both tissues.
- **Conclusion**: Established evidence supports FUS as a multifunctional RNA-regulatory bridge linking splicing, RNA turnover and protein-homeostasis neighborhoods. Its network position makes it a plausible integrator, but the module does not show that FUS pathology or altered FUS activity is responsible for the liver-prostate co-abundance pattern.

#### VAMP8

- **Related proteins** (co-abundance neighbors): CCT3 (0.83), CTNND1 (0.82), EIF3C (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Plasma membrane; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_06458.1, huMAP3_08929.1, huMAP3_10587.1
- **Function (MyGene.info)**: vesicle associated membrane protein 8. This gene encodes an integral membrane protein that belongs to the synaptobrevin/vesicle-associated membrane protein subfamily of soluble N-ethylmaleimide-sensitive factor attachment protein receptors (SNAREs). The encoded protein is involved in the fusion of synaptic vesicles with the presynaptic membrane.[provided by RefSeq, Jun 2010].
- **Diseases (Open Targets)**: Moderate albuminuria (0.327); coronary artery disorder (0.326); prostate carcinoma (0.304); myocardial infarction (0.276); myocardial ischemia (0.204)
- **Europe PMC papers**: 2696
- **Why important**: VAMP8 is a vesicle-associated SNARE involved in vesicle fusion, vesicle-mediated transport, autophagy and autophagosome membrane docking. It connects CCT3, CTNND1 and EIF3C, is detected in both liver and prostate, and is represented with ZW10 in hu.MAP complexes (hu.MAP huMAP3_06458.1), (hu.MAP huMAP3_08929.1) and (hu.MAP huMAP3_10587.1). Its disease associations include prostate carcinoma and cardiovascular phenotypes, giving it relevance to the tissue pair and to cellular stress or trafficking states.
- **Conclusion**: Established evidence supports VAMP8 as a trafficking and membrane-fusion marker that extends the module beyond nuclear RNA processing. The evidence supports participation in a shared vesicle-related cellular state, but not a direct physical bridge from VAMP8 to the spliceosomal core.

## Module 3

**Tissue pair**: liver and prostate  
**Genes (5)**: ABCF3, LACTB2, NLN, SEC23A, USO1

### Function

The module does not have any GO or KEGG term passing global correction, so no pathway-level enrichment can be claimed from the globally significant GO/KEGG evidence. Its clearest biological signal is a small intracellular trafficking component: SEC23A is a COPII coat component involved in ER-to-Golgi transport, while USO1 supports COPII vesicle capture, Golgi transport and vesicle fusion. These genes form the only directly supported STRING relationship and are also co-members of hu.MAP complex (hu.MAP huMAP3_12394.1). The remaining genes have more disparate annotations: ABCF3 is an ABC-family protein with reported antiviral activity, LACTB2 is a mitochondrial RNA-processing enzyme, and NLN is a mitochondrial metallopeptidase involved in neurotensin processing and proteolysis. Thus, the most defensible interpretation is a weakly defined intracellular homeostasis module containing an ER-to-Golgi trafficking signal rather than a confidently established single biological pathway.

**Cell composition.** The module is not secreted and does not resemble a plasma-protein module. Most genes show low tissue specificity and low immune-cell specificity, although LACTB2 is liver-enhanced and USO1 is skeletal-muscle-enhanced. The single-cell annotations are heterogeneous, including germ-cell, tuft-cell, syncytiotrophoblast and myonuclear signals, rather than a coherent shared cell type. NLN is group-enriched in several monocyte populations, but the overall HPA profile is not blood-cell dominated. All module proteins are detected in prostate, and nearly all are detected in liver, so the co-abundance pattern could reflect broadly present intracellular proteins, shared cellular composition, or common sample-state effects rather than a liver-and-prostate-specific secretory program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports only the SEC23A–USO1 relationship among the module genes, and no STRING functional-enrichment result is available. This relationship is biologically coherent with the established COPII and ER-to-Golgi roles of both proteins. hu.MAP complex (hu.MAP huMAP3_12394.1) independently places SEC23A and USO1 in a large vesicle-trafficking and membrane-protein network that includes multiple coat, adaptor, vesicle and Golgi-associated proteins. Because only a small subset of that complex is represented in this module, (hu.MAP huMAP3_12394.1) supports a trafficking connection but does not establish that the whole module is a single physical complex. ABCF3, LACTB2 and NLN lack reported STRING partners and hu.MAP assignments in the supplied evidence, so their links to the trafficking signal are currently co-abundance associations rather than known molecular interactions.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: SEC23A–USO1 (0.704)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12394.1 (USO1, SEC23A; 2/98)

### Novelty

A new co-abundance pattern may be present, but the module cannot be called a new biological mechanism on the current evidence. The SEC23A–USO1 relationship is already represented in STRING and the same genes occur together in hu.MAP complex (hu.MAP huMAP3_12394.1), so its central trafficking connection is not novel as a molecular association. The possible novelty lies in the joint co-abundance of ABCF3, LACTB2 and NLN with that trafficking pair across liver and prostate. However, the absence of additional STRING or hu.MAP relationships is not proof of novelty, and the lack of globally significant GO or KEGG enrichment makes the biological interpretation provisional. Replication in independent cohorts, preservation of the gene correlations, cell-composition adjustment and experimental testing would be needed before claiming a new conserved module.

**Hypothesis.** Hypothesis: the module may capture coordinated intracellular stress or protein-homeostasis state in which ER-to-Golgi trafficking through SEC23A and USO1 covaries with mitochondrial RNA or proteolytic functions represented by LACTB2 and NLN, while ABCF3 marks a broader cytosolic or antiviral-response state. This is a network-level hypothesis, not an established pathway: the direct trafficking evidence is limited to SEC23A and USO1, and the links to ABCF3, LACTB2 and NLN are not supported by the supplied physical-interaction or complex evidence. A useful test would be whether the module tracks ER stress, secretory load, mitochondrial state or cellular composition after adjustment for tissue and cell-type effects.

### Important genes

#### ABCF3

- **Related proteins** (co-abundance neighbors): LACTB2 (0.89), SEC23A (0.83), NLN (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP binding cassette subfamily F member 3. This gene encodes a member of the ATP-binding cassette (ABC) transporter superfamily. ATP-binding cassette proteins transport various molecules across extra- and intracellular membranes. The protein encoded by this gene displays antiviral effect against flaviviruses. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2017].
- **Diseases (Open Targets)**: mathematical ability (0.369); hypertensive disorder (0.173); Familial prostate cancer (0.111); prostate cancer (0.111); cardiovascular disorder (0.095)
- **Europe PMC papers**: 290
- **Why important**: ABCF3 is the most connected and strongest-weighted node in the supplied co-abundance graph, linking the two trafficking-associated genes with LACTB2 and NLN. Its established annotation places it in the ABC transporter superfamily, and the fact sheet reports antiviral activity against flaviviruses. It has a comparatively substantial literature base and reported links to prostate cancer and familial prostate cancer, although those disease associations do not establish a role in this module.
- **Conclusion**: Established evidence supports ABCF3 as the module's network hub and as an ABC-family protein with reported antiviral activity. It is not established that ABCF3 physically interacts with the other module members or that it controls ER-to-Golgi transport. Its hub position makes it a strong candidate for testing as a coordinator or marker of the shared co-abundance state.

#### SEC23A

- **Related proteins** (co-abundance neighbors): ABCF3 (0.83), USO1 (0.81); STRING partners: USO1 (0.704)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A is a central connector between ABCF3 and USO1 and is one of the two genes with both STRING and hu.MAP support. Its established function is as a COPII component involved in ER-to-Golgi vesicle budding, cargo loading and intracellular protein transport. It has the largest reported literature volume among the module genes and disease associations including craniolenticulosutural dysplasia and male reproductive organ cancer.
- **Conclusion**: Established evidence strongly supports SEC23A as the principal trafficking-related gene in the module and supports its known relationship with USO1 through STRING and (hu.MAP huMAP3_12394.1). It is not established that SEC23A explains the co-abundance of the mitochondrial and ABC-family genes. SEC23A is therefore the leading mechanistic anchor for the module, but not proof of a unified pathway.

#### USO1

- **Related proteins** (co-abundance neighbors): SEC23A (0.81); STRING partners: SEC23A (0.704)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: USO1 vesicle transport factor. The protein encoded by this gene is a peripheral membrane protein which recycles between the cytosol and the Golgi apparatus during interphase. It is regulated by phosphorylation: dephosphorylated protein associates with the Golgi membrane and dissociates from the membrane upon phosphorylation. Ras-associated protein 1 recruits this protein to coat protein complex II (COPII) vesicles during buddin…
- **Diseases (Open Targets)**: psoriatic arthritis (0.184); bipolar disorder (0.150); retinitis pigmentosa (0.085); cone dystrophy (0.076); cone-rod dystrophy (0.076)
- **Europe PMC papers**: 546
- **Why important**: USO1 is directly connected to SEC23A in STRING and shares hu.MAP complex (hu.MAP huMAP3_12394.1) with SEC23A. Its established biology places it at the cytosol-Golgi interface, where it participates in COPII-vesicle recruitment, Golgi vesicle transport and vesicle fusion. Its tissue-enhanced skeletal-muscle annotation and myonuclear single-cell annotation may indicate context dependence, while its literature base is intermediate within this module.
- **Conclusion**: Established evidence supports USO1 as a genuine partner of the SEC23A trafficking signal. The module-specific association of USO1 with ABCF3, LACTB2 and NLN remains unproven and could reflect coordinated expression rather than physical interaction. USO1 is the best candidate for testing whether the module reflects altered ER-to-Golgi transport.

#### LACTB2

- **Related proteins** (co-abundance neighbors): ABCF3 (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lactamase beta 2. Enables endoribonuclease activity; single-stranded RNA binding activity; and zinc ion binding activity. Involved in RNA phosphodiester bond hydrolysis, endonucleolytic. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: alcohol drinking (0.346); Meniere disease (0.314); prolapse of female genital organ (0.308); Forceps delivery (0.296); Ventouse delivery (0.296)
- **Europe PMC papers**: 208
- **Why important**: LACTB2 is liver-enhanced, detected in both tissues, and is linked to the hub ABCF3 in the co-abundance graph. Its established annotation describes a mitochondrial matrix protein with endoribonuclease, single-stranded RNA-binding and zinc-binding activities involved in RNA phosphodiester-bond hydrolysis. Its germ-cell and tuft-cell annotations suggest that its abundance may be sensitive to cellular composition or differentiation state. The literature base is smaller than that of the principal trafficking genes.
- **Conclusion**: Established evidence supports LACTB2 as a mitochondrial RNA-processing enzyme and as a liver-enhanced module member. There is no supplied physical-interaction evidence connecting it to SEC23A, USO1 or NLN. Its inclusion supports a possible mitochondrial or cell-state component, but any role in coordinating trafficking is presently a hypothesis.

#### NLN

- **Related proteins** (co-abundance neighbors): ABCF3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Group enriched; location Mitochondria; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neurolysin. This gene encodes a member of the metallopeptidase M3 protein family that cleaves neurotensin at the Pro10-Tyr11 bond, leading to the formation of neurotensin(1-10) and neurotensin(11-13). The encoded protein is likely involved in the termination of the neurotensinergic signal in the central nervous system and in the gastrointestinal tract.[provided by RefSeq, Jun 2010].
- **Diseases (Open Targets)**: stroke disorder (0.388); occlusion precerebral artery (0.321); alcohol drinking (0.234); hypertensive disorder (0.221); Abnormal nasolacrimal system morphology (0.192)
- **Europe PMC papers**: 1159
- **Why important**: NLN is connected to the module hub ABCF3 and has a relatively substantial literature base. It is a mitochondrial metallopeptidase known to cleave neurotensin and is annotated for proteolysis and G-protein-coupled receptor signaling. Its HPA blood-cell annotation is enriched across monocyte and myeloid-dendritic-cell categories, although its overall immune-cell specificity is low and it is detected in both tissues. Reported disease associations include stroke-related and vascular phenotypes.
- **Conclusion**: Established evidence supports NLN as a mitochondrial peptidase with neurotensin-processing activity and possible relevance to vascular or neurological disease. The supplied data do not establish a physical or functional connection between NLN and the COPII trafficking genes. NLN may be a marker of mitochondrial, proteolytic or cellular-composition state within the module, but its causal importance requires direct testing.

## Module 4

**Tissue pair**: liver and prostate  
**Genes (5)**: ACSL1, CAT, ETFDH, DBT, TST

### Function

The module is most consistent with coordinated mitochondrial and redox metabolism, with links to fatty-acid oxidation, branched-chain amino-acid catabolism, electron transfer, sulfur metabolism, and peroxide detoxification. ETFDH is the network hub and connects ACSL1, DBT, CAT, and TST, providing a plausible bridge between mitochondrial electron transfer, lipid handling, branched-chain amino-acid breakdown, antioxidant defense, and sulfur-compound processing. This is an interpretation from the gene annotations and network structure, not a globally validated enrichment result. No GO/KEGG term passed global correction, so no GO/KEGG term is presented as significant. The absence of enriched terms does not invalidate the module.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and all module proteins were detected by immunohistochemistry in both liver and prostate. The composition is strongly liver-associated, with most genes tissue-enhanced in liver, while one gene has low tissue specificity. The HPA single-cell annotations include hepatocytes as well as several epithelial, muscle, and blood-lineage signals. Blood-cell associations occur for ACSL1, CAT, and TST, including neutrophil, eosinophil, myeloid dendritic-cell, and progenitor annotations. Therefore, the shared signal could reflect liver-associated metabolic programs and shared or contaminating cell populations rather than a prostate-specific mechanism. The evidence does not support calling this a broadly expressed housekeeping module, although the mitochondrial and antioxidant functions are biologically general.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the reported confidence threshold, and STRING functional enrichment was absent. No hu.MAP complex contained at least two module members. Thus, the four observed co-abundance edges are not corroborated by the supplied external protein-interaction or complex resources. This may indicate tissue-specific co-regulation, abundance-driven association, incomplete database coverage, or a technically fragile network rather than a physically established multiprotein complex. The strongest edge relationships should consequently be treated as co-abundance relationships, not proven direct interactions.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a tissue-pair-specific co-abundance observation, but it cannot be established as a new biological discovery from the fact sheet alone. Its novelty is supported only in the limited sense that the exact module lacks matching STRING and hu.MAP support. That absence does not prove novelty, because database coverage, confidence thresholds, tissue context, and the distinction between co-abundance and physical interaction can all explain the lack of matches. The strongest defensible claim is that this is an unvalidated candidate module linking several established metabolic and redox genes in a liver--prostate comparison.

**Hypothesis.** Hypothesis: in liver and prostate samples, a shared abundance program coordinates mitochondrial fuel utilization and protection from reactive metabolites. ETFDH may mark the central respiratory-electron-transfer state, while ACSL1 supplies activated fatty-acyl substrates, DBT represents branched-chain amino-acid oxidation, CAT limits hydrogen-peroxide stress, and TST contributes mitochondrial sulfur-compound handling and RNA import. The co-abundance pattern could therefore arise from coordinated metabolic state, cellular composition, or both. This hypothesis requires validation with independent cohorts, cell-composition adjustment, transcript or protein measurements, and targeted assays of mitochondrial respiration, fatty-acid oxidation, branched-chain amino-acid flux, and redox balance.

### Important genes

#### ETFDH

- **Related proteins** (co-abundance neighbors): ACSL1 (0.87), DBT (0.83), CAT (0.82), TST (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein dehydrogenase. This gene encodes a component of the electron-transfer system in mitochondria and is essential for electron transfer from a number of mitochondrial flavin-containing dehydrogenases to the main respiratory chain. Mutations in this gene are associated with glutaric acidemia. Alternatively spliced transcript variants that encode distinct isoforms have been observed. [provided by RefSeq, Aug 2013].
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.845); glutaric acidemia IIc (0.704); glutaric aciduria (0.670); hereditary disease (0.523); Abnormality of metabolism/homeostasis (0.407)
- **Europe PMC papers**: 1273
- **Why important**: ETFDH is the sole network hub, connected to every other module member, and is annotated as a component of the mitochondrial electron-transfer system serving multiple flavin-containing dehydrogenases. It provides the clearest structural and functional anchor for the module. Its disease associations with multiple acyl-CoA dehydrogenase deficiency and glutaric acidemia further support its importance to mitochondrial energy metabolism, while its literature volume indicates substantial prior study.
- **Conclusion**: Established evidence: ETFDH is the central co-abundance node and has a documented mitochondrial electron-transfer role. Hypothesis: its hub position reflects coordinated mitochondrial respiratory and fuel-oxidation state in the shared liver--prostate signal, but the network does not establish direct physical binding or causality.

#### ACSL1

- **Related proteins** (co-abundance neighbors): ETFDH (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 1. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. Several transcript variants enco…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.510); diabetes mellitus (0.501); diabetic neuropathy (0.404); neurodegenerative disease (0.368); menopause (0.334)
- **Europe PMC papers**: 4992
- **Why important**: ACSL1 is the module's fatty-acid entry point: it converts long-chain fatty acids into fatty acyl-CoA esters and participates in both lipid biosynthesis and fatty-acid degradation. Its HPA profile is enhanced in liver, adipose tissue, and skeletal muscle, with a neutrophil association, making it informative for both metabolic interpretation and possible cell-composition effects. Its diabetes-related disease associations and substantial literature volume add biological context.
- **Conclusion**: Established evidence: ACSL1 connects long-chain fatty-acid handling to the ETFDH-centered network and is strongly associated with metabolic tissues. Hypothesis: ACSL1 may couple lipid substrate availability to mitochondrial oxidation in this module, although the single observed network connection and blood-cell annotation require caution.

#### DBT

- **Related proteins** (co-abundance neighbors): ETFDH (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dihydrolipoamide branched chain transacylase E2. The branched-chain alpha-keto acid dehydrogenase complex (BCKD) is an inner-mitochondrial enzyme complex involved in the breakdown of the branched-chain amino acids isoleucine, leucine, and valine. The BCKD complex is thought to be composed of a core of 24 transacylase (E2) subunits, and associated decarboxylase (E1), dehydrogenase (E3), and regulatory subunits. This gene encodes the transacylase …
- **Diseases (Open Targets)**: maple syrup urine disease (0.710); maple syrup urine disease type 1A (0.695); maple syrup urine disease type 2 (0.659); intermittent maple syrup urine disease (0.370); classic maple syrup urine disease (0.370)
- **Europe PMC papers**: 15522
- **Why important**: DBT encodes the E2 transacylase component of the mitochondrial branched-chain alpha-keto acid dehydrogenase complex and is linked to breakdown of isoleucine, leucine, and valine. It is detected in both tissues and has a cell-type profile that includes prostatic glandular cells. Its established relationship to maple syrup urine disease and very large literature base make it a strong marker of branched-chain amino-acid catabolism.
- **Conclusion**: Established evidence: DBT represents mitochondrial branched-chain amino-acid degradation and is connected to ETFDH in the module. Hypothesis: its co-abundance may indicate coordinated use of amino-acid-derived reducing equivalents or carbon with other mitochondrial fuels, but no module-level enrichment or physical interaction demonstrates that mechanism.

#### CAT

- **Related proteins** (co-abundance neighbors): ETFDH (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Vesicles; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catalase. This gene encodes catalase, a key antioxidant enzyme in the bodies defense against oxidative stress. Catalase is a heme enzyme that is present in the peroxisome of nearly all aerobic cells. Catalase converts the reactive oxygen species hydrogen peroxide to water and oxygen and thereby mitigates the toxic effects of hydrogen peroxide. Oxidative stress is hypothesized to play a role in the developme…
- **Diseases (Open Targets)**: acatalasia (0.697); type 2 diabetes mellitus (0.354); COVID-19 (0.299); major depressive disorder (0.272); neurodegenerative disease (0.224)
- **Europe PMC papers**: 432201
- **Why important**: CAT encodes catalase, a major peroxide-detoxifying enzyme that converts hydrogen peroxide to water and oxygen. It is liver-enhanced, detected in both tissues, and annotated in erythroid, hepatocyte, and neutrophil-related cell types. Its acatalasia association and exceptionally extensive literature make it the key oxidative-stress component and an important indicator of possible blood or cell-composition effects.
- **Conclusion**: Established evidence: CAT supplies a well-established antioxidant function and is part of the ETFDH-centered co-abundance pattern. Hypothesis: CAT may buffer oxidative stress generated by increased mitochondrial fuel oxidation, but the module does not establish that oxidative stress drives the association.

#### TST

- **Related proteins** (co-abundance neighbors): ETFDH (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thiosulfate sulfurtransferase. This is one of two neighboring genes encoding similar proteins that each contain two rhodanese domains. The encoded protein is localized to the mitochondria and catalyzes the conversion of thiosulfate and cyanide to thiocyanate and sulfite. In addition, the protein interacts with 5S ribosomal RNA and facilitates its import into the mitochondria. Alternative splicing results in multiple transcript …
- **Diseases (Open Targets)**: neurodegenerative disease (0.356); atopic eczema (0.306); severe acute respiratory syndrome (0.287); COVID-19 (0.287); tuberculosis (0.105)
- **Europe PMC papers**: 14284
- **Why important**: TST is a mitochondrial sulfurtransferase that converts thiosulfate and cyanide to thiocyanate and sulfite and also participates in mitochondrial five-S ribosomal RNA import. It is liver-enhanced, detected in both tissues, and has a myeloid dendritic-cell association. Its disease and infection-related Open Targets associations and substantial literature provide context, while its connection to ETFDH adds a sulfur-metabolism dimension to the module.
- **Conclusion**: Established evidence: TST contributes mitochondrial sulfur-compound metabolism and RNA import and is co-abundant with the module hub. Hypothesis: TST may reflect a broader mitochondrial detoxification or stress-response state coordinated with respiratory metabolism, but this interpretation is not supported by a known complex or globally significant enrichment.

## Module 5

**Tissue pair**: liver and prostate  
**Genes (20)**: ACSL4, ANXA1, CASP3, CLIC1, DIAPH1, EFHD2, CPOX, IPO4, PKM, NAA15, PAFAH1B3, PCNA, PFDN6, PPIF, PFAS, ADSS2, TFRC, TMX1, TNPO1, TPD52L2

### Function

The module does not have a statistically supported GO or KEGG functional label: no GO or KEGG term passed global correction. Its gene-level annotations instead point to a mixed cellular program involving glycolysis through PKM, purine and nucleotide synthesis through PFAS and ADSS2, DNA replication and repair through PCNA, nuclear import through TNPO1 and IPO4, lipid metabolism through ACSL4, iron uptake through TFRC, heme synthesis through CPOX, protein folding and stress responses through TMX1 and PPIF, and cytoskeletal or membrane functions through DIAPH1, EFHD2, ANXA1 and CLIC1. The network has a connected core centered on TPD52L2, PCNA, NAA15, PFAS and TNPO1, with several smaller functional branches. Thus, the most defensible interpretation is a conserved cellular-maintenance and biosynthetic state rather than a single established pathway.

**Cell composition.** This is not predominantly a plasma or secreted-protein module. Only a minority of genes are annotated as secreted or secreted to blood, including TFRC and ANXA1, while TMX1 is annotated as intracellular and membrane-associated. Most genes have low tissue specificity, so the liver–prostate sharing is compatible with broadly expressed cellular biology rather than a liver-specific or prostate-specific program. HPA single-cell data show substantial enrichment or enhancement in blood-associated populations, especially neutrophil, platelet and erythrocyte-progenitor related populations, with additional signals in reproductive, epithelial and neural cell types. This pattern raises the possibility that part of the shared signal reflects blood contamination, vascular or stromal admixture, or shared cell populations in the samples. It does not establish that the module is blood-derived, because many members are intracellular housekeeping or biosynthetic proteins and the tissue-level evidence is mixed.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING functional enrichment is absent, so STRING provides no supplementary pathway-level support. At the specified interaction confidence, the only recorded STRING relationship within the module is IPO4 with TNPO1, supporting a known connection between nuclear import factors. hu.MAP provides two-member overlaps in C1 for PKM with EFHD2, and in C2 and C3 for ACSL4 with TNPO1. These overlaps are small relative to the listed complexes and therefore support compatibility with known molecular assemblies without demonstrating that the whole module is one physical complex. The module therefore appears to combine a small known nuclear-import relationship, limited complex overlaps, and co-abundance relationships that are not broadly represented as established protein interactions.

**STRING interactions (score >= 0.7)**: 1 of 190 gene pairs: IPO4–TNPO1 (0.74)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (PKM, EFHD2; 2/57); huMAP3_06247.1 (ACSL4, TNPO1; 2/65); huMAP3_09592.1 (ACSL4, TNPO1; 2/95)

### Novelty

The module may be a new co-abundance observation, but the available evidence does not justify calling it a newly discovered molecular complex or pathway. The strongest reason for possible novelty is that most module edges lack corresponding high-confidence STRING or hu.MAP support, while the module spans several biological processes. However, absence from those resources is not proof of novelty: co-abundance can arise from shared regulation, cell composition, compartmental activity, or indirect physiological coupling. The global absence of GO or KEGG enrichment also limits a claim of pathway-level discovery. A cautious conclusion is that this is a potentially novel conserved expression or abundance pattern requiring replication, cell-composition adjustment, and independent validation.

**Hypothesis.** Hypothesis: the conserved liver–prostate module reflects a shared cellular stress and biosynthetic state in which increased metabolic and proliferative demand coordinates glycolysis, purine production, lipid handling, iron uptake and heme-related activity with nuclear transport, protein maturation and cytoskeletal organization. The blood-cell and platelet-associated HPA signals suggest that this state may be partly influenced by circulating or infiltrating cells, or by shared vascular and stromal material. The proposed mechanism is not established by enrichment analysis; it should be tested by cell-type deconvolution, matched tissue validation, perturbation of the central genes, and measurement of the corresponding metabolic, transport and stress phenotypes.

### Important genes

#### TPD52L2

- **Related proteins** (co-abundance neighbors): IPO4 (0.88), PFAS (0.86), TNPO1 (0.82), PKM (0.81), PCNA (0.81), CLIC1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TPD52 like 2. This gene encodes a member of the tumor protein D52-like family. These proteins are characterized by an N-terminal coiled-coil motif that is used to form homo- and heteromeric complexes with other tumor protein D52-like proteins. Expression of this gene may be a marker for breast cancer and acute lymphoblastic leukemia. Alternatively spliced transcript variants encoding multiple isoforms have been…
- **Diseases (Open Targets)**: breast cancer (0.088); breast carcinoma (0.087); neoplasm (0.078); gastric cancer (0.078); posterior cortical atrophy (0.077)
- **Europe PMC papers**: 1316
- **Why important**: TPD52L2 is among the most connected nodes in the module and links the nuclear-import neighborhood with PFAS, PKM, PCNA and CLIC1. Its tumor-protein-D52-like coiled-coil biology provides a plausible scaffold or coordination role, while HPA detects it in both liver and prostate and places it in vesicles. Its disease and cancer associations and substantial literature make it a useful central candidate, although the fact sheet does not establish a direct physical interaction with its module neighbors.
- **Conclusion**: Established evidence: TPD52L2 is a highly connected, broadly expressed module member with coiled-coil and vesicular annotations and reported cancer-related associations. Conclusion: it is a strong network-prioritization candidate and possible coordinator of the module, but a mechanistic scaffolding role remains a hypothesis.

#### PCNA

- **Related proteins** (co-abundance neighbors): PFAS (0.85), TFRC (0.84), CASP3 (0.84), PFDN6 (0.82), TPD52L2 (0.81), ANXA1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proliferating cell nuclear antigen. The protein encoded by this gene is found in the nucleus and is a cofactor of DNA polymerase delta. The encoded protein acts as a homotrimer and helps increase the processivity of leading strand synthesis during DNA replication. In response to DNA damage, this protein is ubiquitinated and is involved in the RAD6-dependent DNA repair pathway. Two transcript variants encoding the same protein have b…
- **Diseases (Open Targets)**: ataxia-telangiectasia-like disorder (0.497); neurodegenerative disease (0.188); neoplasm (0.118); diabetes mellitus (0.116); hepatocellular carcinoma (0.113)
- **Europe PMC papers**: 61820
- **Why important**: PCNA is a highly connected node and connects the module to PFAS, TFRC, CASP3, PFDN6, TPD52L2 and ANXA1. Its established functions in DNA replication, repair and chromatin-related processes make it the clearest marker of a proliferative or genome-maintenance component. It is tissue-enhanced in bone marrow and cell-type enhanced in erythrocyte progenitors and germ-cell populations, while detected in prostate but not liver by the listed HPA protein evidence. Its extensive literature and disease associations provide strong external biological support.
- **Conclusion**: Established evidence: PCNA is a replication and repair factor with a central network position and strong literature support. Conclusion: it supports a cell-cycle or genome-maintenance interpretation, but its presence does not prove that proliferation drives the entire shared module.

#### TNPO1

- **Related proteins** (co-abundance neighbors): ADSS2 (0.92), NAA15 (0.87), IPO4 (0.87), TPD52L2 (0.82); STRING partners: IPO4 (0.74)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_06247.1, huMAP3_09592.1
- **Function (MyGene.info)**: transportin 1. This gene encodes the beta subunit of the karyopherin receptor complex which interacts with nuclear localization signals to target nuclear proteins to the nucleus. The karyopherin receptor complex is a heterodimer of an alpha subunit which recognizes the nuclear localization signal and a beta subunit which docks the complex at nucleoporins. Alternate splicing of this gene results in several transc…
- **Diseases (Open Targets)**: atrial fibrillation (0.415); neurodegenerative disease (0.370); hypothyroidism (0.320); injury (0.198); bladder calculus (0.183)
- **Europe PMC papers**: 822
- **Why important**: TNPO1 occupies a central position linking ADSS2, NAA15, IPO4 and TPD52L2. It is the sole partner in the recorded high-confidence STRING relationship, with IPO4, and it appears in two hu.MAP complexes together with ACSL4. Its established role in nuclear import provides a plausible route by which metabolic or stress-related changes could be coupled to nuclear regulation. It is detected in both liver and prostate and has documented disease associations and a substantial literature base.
- **Conclusion**: Established evidence: TNPO1 is a nuclear-import factor supported by a STRING relationship with IPO4 and by module connectivity. Conclusion: it is a credible organizing node for transport-related coordination, but the fact sheet does not show that it transports a specific module-associated cargo.

#### PFAS

- **Related proteins** (co-abundance neighbors): TPD52L2 (0.86), TMX1 (0.85), PCNA (0.85), PFDN6 (0.84), PKM (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoribosylformylglycinamidine synthase. Purines are necessary for many cellular processes, including DNA replication, transcription, and energy metabolism. Ten enzymatic steps are required to synthesize inosine monophosphate (IMP) in the de novo pathway of purine biosynthesis. The enzyme encoded by this gene catalyzes the fourth step of IMP biosynthesis. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: dyskeratosis congenita (0.520); Coats plus syndrome (0.455); neurodegenerative disease (0.187); hereditary disease (0.174); retinal disorder (0.118)
- **Europe PMC papers**: 3393
- **Why important**: PFAS is a highly connected metabolic node linking TPD52L2, TMX1, PCNA, PFDN6 and PKM. Its established enzymatic role in de novo purine biosynthesis connects the module to nucleotide supply needed for energy metabolism, replication and repair. HPA detects it in both liver and prostate, with enhancement in erythrocyte progenitors and immune-cell evidence involving neutrophils. Its disease associations and broad literature support make it more informative than a purely topological hub.
- **Conclusion**: Established evidence: PFAS is a purine-biosynthetic enzyme with a central co-abundance position and compatible tissue detection. Conclusion: it supports a nucleotide-demand component of the module, while the data do not demonstrate increased purine flux or direct coordination with PCNA or PKM.

#### TFRC

- **Related proteins** (co-abundance neighbors): ACSL4 (0.88), PAFAH1B3 (0.85), PCNA (0.84), CPOX (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes, Lysosomes; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transferrin receptor. This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: TFRC-related combined immunodeficiency (0.623); type 2 diabetes mellitus (0.518); mucopolysaccharidosis type 2 (0.490); diabetes mellitus (0.471); diabetic retinopathy (0.343)
- **Europe PMC papers**: 14164
- **Why important**: TFRC connects ACSL4, PAFAH1B3, PCNA and CPOX and is detected in both liver and prostate. Its established function in receptor-mediated iron uptake, together with its association with erythrocyte progenitors, monocytes and macrophages, provides a biologically meaningful link between cellular metabolism, iron handling and possible blood-cell contribution. It is annotated as secreted to blood, making it especially relevant to interpretation of tissue abundance data. Its extensive literature and disease associations further support prioritization.
- **Conclusion**: Established evidence: TFRC is an iron-uptake receptor with a connected position and blood-associated HPA pattern. Conclusion: it may report iron demand or blood-cell admixture in the module; distinguishing these explanations requires cell-resolved or tissue-localized validation.

## Module 6

**Tissue pair**: liver and prostate  
**Genes (5)**: AIFM1, LAP3, FH, ISG15, SDHA

### Function

The module is most consistent with a mitochondrial energy-metabolism and stress-response module, with a possible connection to proteolysis and interferon-related signaling. FH and SDHA provide the strongest functional anchor because both are mitochondrial metabolic enzymes and are linked by a high-confidence STRING relationship. SDHA also connects to AIFM1, which links respiratory-chain biology to mitochondrial apoptosis. LAP3 may represent a cytosolic proteolysis component, while ISG15 introduces an interferon-responsive and extracellular signaling-related component. However, no GO/KEGG term passed global correction, so this functional interpretation is gene- and network-based rather than enrichment-confirmed. The STRING tinnitus term is supplementary evidence only (STRING HPO Tinnitus; within-query FDR = 0.0169).

**Cell composition.** This does not appear to be a blood-cell-driven module: every gene has low immune-cell specificity in HPA. It is also not predominantly a secreted or plasma-protein module; ISG15 is secreted to blood, whereas the other proteins are intracellular or mitochondrial. The HPA profiles are heterogeneous, including liver, salivary gland, heart muscle, and skeletal muscle tissue enhancement, together with cell-type enhancement in hepatocytes, germ-cell populations, neural and glial populations, epithelial cells, and other cell types. Most proteins are detected in both liver and prostate, but ISG15 is not detected by IHC in either tissue. Thus, the shared signal is more compatible with broadly distributed cellular metabolism and stress biology, or with shared cell-state composition, than with a simple blood contamination explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING identifies a high-confidence FH–SDHA relationship, and the supplementary STRING tinnitus term includes FH, SDHA, and AIFM1 (STRING HPO Tinnitus; within-query FDR = 0.0169). The remaining module relationships are not represented by STRING partners at the stated confidence threshold. No hu.MAP complex contains multiple module members. The known FH–SDHA relationship supports a real mitochondrial metabolic core, but the absence of additional curated interactions means that the full co-abundance pattern should not be interpreted as an established physical complex. Co-abundance may instead reflect shared mitochondrial abundance, coordinated cellular stress, or indirect regulation.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: FH–SDHA (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: HPO Tinnitus (FDR = 0.0169, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a potentially interesting cross-tissue co-abundance pattern, but it cannot be called a newly discovered molecular complex or a definitively novel pathway. The FH–SDHA relationship is already established in STRING, and the functions of FH, SDHA, AIFM1, LAP3, and ISG15 are individually well documented. Conversely, the particular liver–prostate co-abundance arrangement has little direct support from the available STRING and hu.MAP records. That absence is compatible with a novel tissue-level association but does not prove novelty, because database coverage, assay context, indirect regulation, and co-abundance-specific relationships can all limit detection. Replication in independent liver and prostate cohorts, together with cell-composition adjustment and experimental validation, would be needed to establish novelty.

**Hypothesis.** Hypothesis: the module reflects coordinated mitochondrial metabolic capacity and mitochondrial stress handling in shared liver and prostate cellular states. In this model, FH and SDHA form the metabolic backbone, AIFM1 couples mitochondrial function to apoptotic or respiratory-chain stress responses, LAP3 reflects associated cytosolic proteolytic activity, and ISG15 marks an interferon-responsive or secreted signaling state that may modulate the module indirectly. This is a mechanistic hypothesis, not a demonstrated physical pathway; the lack of globally significant GO/KEGG enrichment and the sparse curated interaction evidence require cautious interpretation.

### Important genes

#### FH

- **Related proteins** (co-abundance neighbors): LAP3 (0.82), SDHA (0.81); STRING partners: SDHA (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fumarate hydratase. The protein encoded by this gene is an enzymatic component of the tricarboxylic acid (TCA) cycle, or Krebs cycle, and catalyzes the formation of L-malate from fumarate. It exists in both a cytosolic form and an N-terminal extended form, differing only in the translation start site used. The N-terminal extended form is targeted to the mitochondrion, where the removal of the extension generates the …
- **Diseases (Open Targets)**: hereditary leiomyomatosis and renal cell cancer (0.838); fumaric aciduria (0.820); hereditary neoplastic syndrome (0.580); Multiple cutaneous leiomyomas (0.575); neurodegenerative disease (0.482)
- **Europe PMC papers**: 42469
- **Why important**: FH is a high-connectivity bridge within the module and is directly linked to SDHA by a high-confidence STRING relationship. It is a mitochondrial and cytosolic fumarase involved in the TCA cycle, fumarate and malate metabolism, the urea and arginine pathways, and DNA-damage response. Its strong disease associations with hereditary leiomyomatosis and renal cell cancer, fumaric aciduria, and related neoplastic syndromes, together with extensive literature, make it the clearest metabolic and disease-relevant anchor.
- **Conclusion**: Established: FH is a central metabolic enzyme with a known relationship to SDHA and substantial disease evidence. Hypothesis: FH may help organize the shared cross-tissue metabolic state represented by this module.

#### SDHA

- **Related proteins** (co-abundance neighbors): FH (0.81), AIFM1 (0.80); STRING partners: FH (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate dehydrogenase complex flavoprotein subunit A. This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identi…
- **Diseases (Open Targets)**: mitochondrial complex II deficiency, nuclear type 1 (0.813); pheochromocytoma/paraganglioma syndrome 5 (0.790); dilated cardiomyopathy 1GG (0.768); neurodegeneration with ataxia and late-onset optic atrophy (0.761); gastrointestinal stromal tumor (0.743)
- **Europe PMC papers**: 12756
- **Why important**: SDHA occupies a central bridging position between FH and AIFM1. It encodes the catalytic flavoprotein subunit of mitochondrial complex II and participates in succinate metabolism, the TCA cycle, and respiratory electron transport. It has well-established associations with mitochondrial respiratory-chain deficiency, Leigh syndrome, paraganglioma-related disease, cardiomyopathy, and other mitochondrial disorders. Its strong STRING relationship with FH and broad literature support make it a key indicator of mitochondrial respiratory biology.
- **Conclusion**: Established: SDHA supports a mitochondrial respiratory and succinate-metabolism interpretation and is connected to FH in STRING. Hypothesis: coordinated SDHA abundance may be a major contributor to the conserved liver–prostate signal.

#### AIFM1

- **Related proteins** (co-abundance neighbors): SDHA (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apoptosis inducing factor mitochondria associated 1. This gene encodes a flavoprotein essential for nuclear disassembly in apoptotic cells, and it is found in the mitochondrial intermembrane space in healthy cells. Induction of apoptosis results in the translocation of this protein to the nucleus where it affects chromosome condensation and fragmentation. In addition, this gene product induces mitochondria to release the apoptogenic proteins cytochr…
- **Diseases (Open Targets)**: severe X-linked mitochondrial encephalomyopathy (0.813); X-linked hereditary sensory and autonomic neuropathy with hearing loss (0.798); Charcot-Marie-Tooth disease X-linked recessive 4 (0.761); spondyloepimetaphyseal dysplasia, Bieganski type (0.747); combined oxidative phosphorylation deficiency (0.615)
- **Europe PMC papers**: 1952
- **Why important**: AIFM1 links the SDHA-centered mitochondrial segment to apoptosis and stress responses. It is a mitochondrial intermembrane-space flavoprotein involved in respiratory-chain complex assembly and apoptotic nuclear changes, and it has established associations with severe X-linked mitochondrial encephalomyopathy, neuropathy, neurodevelopmental disease, and combined oxidative-phosphorylation deficiency. It also appears with FH and SDHA in the supplementary STRING tinnitus term (STRING HPO Tinnitus; within-query FDR = 0.0169).
- **Conclusion**: Established: AIFM1 connects mitochondrial respiration with apoptotic biology and has substantial disease evidence. Hypothesis: its co-abundance with SDHA may indicate mitochondrial stress or altered cell survival rather than a stable physical complex.

#### ISG15

- **Related proteins** (co-abundance neighbors): LAP3 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ISG15 ubiquitin like modifier. The protein encoded by this gene is a ubiquitin-like protein that is conjugated to intracellular target proteins upon activation by interferon-alpha and interferon-beta. Several functions have been ascribed to the encoded protein, including chemotactic activity towards neutrophils, direction of ligated target proteins to intermediate filaments, cell-to-cell signaling, and antiviral activity during…
- **Diseases (Open Targets)**: COVID-19 (0.470); bilateral striopallidodentate calcinosis (0.462); Orthomyxoviridae infectious disease (0.375); neoplasm (0.118); infection (0.118)
- **Europe PMC papers**: 17727
- **Why important**: ISG15 is the peripheral, low-connectivity component attached to LAP3. It is a ubiquitin-like modifier induced by interferon signaling and has reported roles in antiviral activity, immune regulation, chemotaxis, protein modification, and cell-to-cell signaling. It is the sole secreted-to-blood gene in the module and is not detected by IHC in liver or prostate, making it especially important for assessing whether the module reflects a transient inflammatory or secreted signal rather than a shared resident protein program. Its disease and infection associations and extensive literature further support its interpretive importance.
- **Conclusion**: Established: ISG15 is an interferon-responsive ubiquitin-like modifier with secreted signaling potential. Hypothesis: ISG15 may report an inflammatory or paracrine state that is associated with, but not necessarily mechanistically responsible for, the mitochondrial co-abundance pattern.

#### LAP3

- **Related proteins** (co-abundance neighbors): ISG15 (0.83), FH (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: leucine aminopeptidase 3. Predicted to enable peptidase activity. Predicted to be involved in proteolysis. Located in cytosol; midbody; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: upper respiratory tract disorder (0.283); preeclampsia (0.199); multinodular goiter (0.181); Alzheimer disease (0.165); acute myeloid leukemia (0.108)
- **Europe PMC papers**: 1293
- **Why important**: LAP3 is a network bridge connecting ISG15 with FH and is the only module member annotated primarily as a cytosolic proteolysis-related peptidase. Its position could link protein turnover to metabolic and stress-associated signals. It has less specific functional and disease support than FH, SDHA, or AIFM1, although its literature is substantial and its Open Targets associations include upper respiratory tract disorder, preeclampsia, multinodular goiter, Alzheimer disease, and acute myeloid leukemia.
- **Conclusion**: Established: LAP3 is a cytosolic peptidase-related protein positioned between the metabolic and ISG15 portions of the network. Hypothesis: LAP3 may reflect coordinated proteostasis accompanying mitochondrial or inflammatory stress.

## Module 7

**Tissue pair**: liver and prostate  
**Genes (39)**: AIMP1, AMPD2, CCAR1, CLPB, CPSF6, CYFIP1, ADAR, EPS8L2, EWSR1, GGCT, GNS, HDGF, HMGB3, HMOX2, LBR, LMNB2, MESD, NDUFS5, NRDC, NSUN2, NUP62, PPP6R3, PITRM1, PSMC6, PSMC4, PSMC2, PSMD13, PAICS, ADSL, RBM39, S100A13, SHTN1, SRP54, DARS2, TBL2, TCEA1, CCT5, TRIM25, XRN2

### Function

The strongest supported function is proteasome regulatory and accessory-complex activity, based on the globally corrected terms (GO:CC proteasome regulatory particle; q_global = 0.0159) and (GO:CC proteasome accessory complex; q_global = 0.0159). PSMC2, PSMC4, PSMC6 and PSMD13 form the clearly coherent proteasome-related core. The remaining genes suggest connected cellular processes involving RNA processing, RNA modification, translation and protein quality control, but these interpretations are not globally significant GO/KEGG enrichment results. The nucleic-acid-binding OB-fold signal (STRING InterPro Nucleic acid-binding, OB-fold; within-query FDR = 0.0216) is supplementary STRING evidence only and should not be treated as global enrichment. No additional GO/KEGG term passed global correction.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module: HPA classifies only a minority of its genes as secreted, and the prominent proteasome genes are intracellular. Most genes have low tissue specificity, and protein detection is broadly compatible with both liver and prostate. Thus, the shared signal is more consistent with a broadly expressed intracellular program than with a liver-specific or prostate-specific pathway. There is nevertheless a possible cellular-composition contribution. HPA shows enrichment patterns involving spermatogenic cells and several myeloid or neutrophil populations, while many genes are detected in both tissues. The module could therefore partly reflect shared cell types, immune-cell abundance, or general cellular stress and protein-turnover state rather than a process unique to hepatocytes and prostate epithelial cells. AIMP1 and HDGF are secreted to blood, and S100A13 is secreted in other tissues, but these genes do not define the main module signal.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC proteasome regulatory particle | 0.0159 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:CC proteasome accessory complex | 0.0159 | PSMC2, PSMC4, PSMC6, PSMD13 |

### STRING and hu.MAP

STRING supports a highly coherent proteasome subnetwork: PSMC2, PSMC4, PSMC6 and PSMD13 are connected by very strong known associations. STRING also records the ADSL–PAICS and ADSL–AMPD2 purine-metabolism relationships, the CCAR1–RBM39 relationship, the LBR–LMNB2 nuclear-envelope relationship, and the supplementary OB-fold association (STRING InterPro Nucleic acid-binding, OB-fold; within-query FDR = 0.0216). The hu.MAP results independently place the four proteasome genes together in several proteasome complexes (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1). hu.MAP also supports smaller assemblies involving TCEA1, HDGF and MESD (hu.MAP huMAP3_14982.1), GGCT and TRIM25 (hu.MAP huMAP3_04424.1), (hu.MAP huMAP3_08429.1) and (hu.MAP huMAP3_05804.1), TCEA1 and MESD (hu.MAP huMAP3_13998.1), and ADAR and NSUN2 (hu.MAP huMAP3_12301.1). These databases show that the proteasome core is established physical or complex-level biology, whereas many edges connecting the broader module are not established molecular interactions. Consequently, the co-abundance module is biologically structured but should not be interpreted as one physical complex.

**STRING interactions (score >= 0.7)**: 10 of 741 gene pairs: ADSL–AMPD2 (0.972); ADSL–PAICS (0.999); CCAR1–RBM39 (0.875); LBR–LMNB2 (0.998); PSMC2–PSMC4 (0.999); PSMC2–PSMC6 (0.999); PSMC2–PSMD13 (0.999); PSMC4–PSMC6 (0.999); PSMC4–PSMD13 (0.999); PSMC6–PSMD13 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: InterPro Nucleic acid-binding, OB-fold (FDR = 0.0216, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05064.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/31); huMAP3_09656.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/64); huMAP3_13725.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/69); huMAP3_14982.1 (TCEA1, HDGF, MESD; 3/28); huMAP3_04424.1 (GGCT, TRIM25; 2/3); huMAP3_08429.1 (GGCT, TRIM25; 2/5); huMAP3_05804.1 (GGCT, TRIM25; 2/6); huMAP3_13998.1 (TCEA1, MESD; 2/23); huMAP3_12301.1 (ADAR, NSUN2; 2/26)

### Novelty

The proteasome component is not a new biological discovery because its membership and interactions are already represented in STRING and hu.MAP. Likewise, several smaller relationships in the module are already known. The potentially novel observation is the shared liver–prostate co-abundance pattern that links this established proteasome core with RNA-processing, translation, nuclear-envelope, mitochondrial, purine-metabolism and stress-related genes. The available evidence does not establish that this exact cross-tissue module has been previously reported, but absence from STRING or hu.MAP alone cannot prove novelty. A defensible claim is therefore that the module may represent a novel systems-level co-abundance configuration built around a known proteasome program, requiring replication in independent cohorts and comparison with published tissue coexpression studies.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular proteostasis state in liver and prostate in which proteasome regulatory capacity is coordinated with RNA maturation, translation quality control, protein folding, mitochondrial quality control and stress responses. The proteasome genes may form the central functional anchor, while SRP54, NSUN2, CCT5, XRN2, CCAR1 and related genes represent coupled production, processing and disposal of cellular proteins. The spermatogenic and myeloid HPA patterns raise an alternative hypothesis that part of the signal arises from shared or variable cell populations in the sampled tissues. These alternatives can be distinguished by cell-resolved expression, histological composition measures, and perturbation of proteasome activity followed by measurement of RNA-processing and protein-quality-control responses.

### Important genes

#### PSMC2

- **Related proteins** (co-abundance neighbors): SRP54 (0.94), NSUN2 (0.92), PSMD13 (0.86), PSMC4 (0.85), PSMC6 (0.84), AIMP1 (0.84), TBL2 (0.82), ADSL (0.81), AMPD2 (0.80); STRING partners: PSMC4 (0.999), PSMC6 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is a high-connectivity module gene and belongs to the globally enriched proteasome regulatory-particle and accessory-complex terms (GO:CC proteasome regulatory particle; q_global = 0.0159) and (GO:CC proteasome accessory complex; q_global = 0.0159). It has strong STRING links to the other three proteasome-core module genes and occurs in the proteasome assemblies (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1). Its annotated role in ATP-dependent proteasomal protein catabolism, oxidative-stress response and ubiquitin-dependent degradation makes it a strong functional anchor. Its disease associations include plasma-cell and other neoplastic disorders, and it has substantial literature support.
- **Conclusion**: Established evidence supports PSMC2 as a central proteasome regulatory-particle component and a major marker of the module's proteostasis interpretation. It is not established that PSMC2 drives the liver–prostate co-abundance pattern; that causal interpretation remains a hypothesis.

#### PSMC4

- **Related proteins** (co-abundance neighbors): SRP54 (0.88), CCT5 (0.87), PSMD13 (0.87), PSMC2 (0.85), PAICS (0.85), XRN2 (0.82), PSMC6 (0.81); STRING partners: PSMC2 (0.999), PSMC6 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 4. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.603); mantle cell lymphoma (0.542); neoplasm (0.519); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1065
- **Why important**: PSMC4 is among the more highly connected genes and is included in (GO:CC proteasome regulatory particle; q_global = 0.0159), (GO:CC proteasome accessory complex; q_global = 0.0159) and the supplementary STRING term (STRING InterPro Nucleic acid-binding, OB-fold; within-query FDR = 0.0216). It has very strong STRING relationships with PSMC2, PSMC6 and PSMD13 and is present in (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1). Its known role in proteolysis, ubiquitin-dependent protein catabolism, oxidative-stress response and interferon response directly supports the module interpretation. It also has extensive literature and disease links involving hematologic malignancy, neoplasia, viral disease and amyloidosis.
- **Conclusion**: Established evidence identifies PSMC4 as a core proteasome ATPase and one of the most convincing biological representatives of this module. Its coordination with the RNA-related genes is a module-level association, not proof of a direct molecular mechanism.

#### PSMC6

- **Related proteins** (co-abundance neighbors): PSMC2 (0.84), SRP54 (0.82), PSMC4 (0.81), PSMD13 (0.80), CCAR1 (0.80); STRING partners: PSMC2 (0.999), PSMC4 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 6. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.606); mantle cell lymphoma (0.542); neoplasm (0.528); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 748
- **Why important**: PSMC6 is part of the globally significant proteasome terms (GO:CC proteasome regulatory particle; q_global = 0.0159) and (GO:CC proteasome accessory complex; q_global = 0.0159), has strong STRING links to the other proteasome members, and is found in (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1). Its annotation connects proteasomal degradation with oxidative stress, endoplasmic-reticulum-associated degradation and transcriptional regulation. It has disease associations involving plasma-cell myeloma, mantle-cell lymphoma, neoplasia, viral disease and amyloidosis, with a substantial literature base.
- **Conclusion**: Established evidence supports PSMC6 as a proteasome regulatory ATPase and a core module gene. Its possible role as a bridge between proteostasis and tissue-shared stress responses is plausible but remains untested in this module.

#### PSMD13

- **Related proteins** (co-abundance neighbors): PSMC4 (0.87), CCT5 (0.86), NSUN2 (0.86), PSMC2 (0.86), SRP54 (0.85), XRN2 (0.84), RBM39 (0.83), PAICS (0.82), PSMC6 (0.80); STRING partners: PSMC2 (0.999), PSMC4 (0.999), PSMC6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 is the non-ATPase proteasome member in the globally enriched terms (GO:CC proteasome regulatory particle; q_global = 0.0159) and (GO:CC proteasome accessory complex; q_global = 0.0159). It has strong STRING relationships with PSMC2, PSMC4 and PSMC6 and appears in (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1). Its localization in nuclear speckles and annotation in ubiquitin-dependent degradation, oxidative-stress response and type-I-interferon response make it especially relevant to a module that also contains RNA-processing genes. It has disease associations involving hematologic malignancy, neurodegeneration, neoplasia and viral disease.
- **Conclusion**: Established evidence supports PSMD13 as a proteasome regulatory-particle component and a plausible interface between nuclear RNA-related biology and protein degradation. The interface is a mechanistic hypothesis rather than a demonstrated direct interaction with the non-proteasome members.

#### NSUN2

- **Related proteins** (co-abundance neighbors): PSMC2 (0.92), SRP54 (0.90), CCT5 (0.87), PSMD13 (0.86), EWSR1 (0.85), PPP6R3 (0.84), XRN2 (0.83), HMOX2 (0.83), AIMP1 (0.82), EPS8L2 (0.81), NUP62 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_12301.1
- **Function (MyGene.info)**: NOP2/Sun RNA methyltransferase 2. This gene encodes a methyltransferase that catalyzes the methylation of cytosine to 5-methylcytosine (m5C) at position 34 of intron-containing tRNA(Leu)(CAA) precursors. This modification is necessary to stabilize the anticodon-codon pairing and correctly translate the mRNA. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Mar…
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.694); hereditary disease (0.518); Intellectual disability (0.489); phenylketonuria (0.470); neurodegenerative disease (0.462)
- **Europe PMC papers**: 2458
- **Why important**: NSUN2 is one of the most highly connected non-proteasome genes and links in the co-abundance graph to proteasome genes, SRP54, CCT5, EWSR1, XRN2, PPP6R3 and HMOX2. Its established function is RNA cytosine methylation, particularly tRNA modification, together with rRNA and mRNA processing. It has a hu.MAP association (hu.MAP huMAP3_12301.1) with ADAR, and it has extensive literature and disease associations involving intellectual disability and neurodegenerative disease. Its low tissue specificity and detection in both tissues support a broadly expressed cellular role.
- **Conclusion**: Established evidence supports NSUN2 as an RNA-modification and RNA-processing component that may explain why the module extends beyond proteasome biology. Its placement next to the proteasome genes demonstrates co-abundance, not a proven physical or regulatory interaction.

#### CCAR1

- **Related proteins** (co-abundance neighbors): RBM39 (0.86), XRN2 (0.85), SHTN1 (0.85), LMNB2 (0.85), MESD (0.85), NDUFS5 (0.83), EWSR1 (0.83), AIMP1 (0.81), CCT5 (0.80), PSMC6 (0.80); STRING partners: RBM39 (0.875)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell division cycle and apoptosis regulator 1. Enables RNA polymerase II cis-regulatory region sequence-specific DNA binding activity; nuclear receptor coactivator activity; and transcription corepressor activity. Involved in positive regulation of cell migration and positive regulation of cell population proliferation. Acts upstream of or within positive regulation of apoptotic process. Located in nuclear envelope lumen. [provided by Alliance…
- **Diseases (Open Targets)**: dengue disease (0.370); neurodegenerative disease (0.288); medulloblastoma (0.199); cancer (0.103); malignant pleural mesothelioma (0.093)
- **Europe PMC papers**: 733
- **Why important**: CCAR1 has high module connectivity and links RBM39, XRN2, SHTN1, LMNB2, MESD, NDUFS5, EWSR1 and AIMP1. It is annotated as a transcriptional coactivator and corepressor involved in transcription, proliferation, migration and apoptosis. The CCAR1–RBM39 relationship is supported by STRING, and RBM39 is a nuclear RNA-processing and splicing regulator, making this pair relevant to the non-proteasome portion of the module. CCAR1 has disease associations involving cancer and neurodegenerative disease, with meaningful literature support.
- **Conclusion**: Established evidence supports CCAR1 as a plausible nuclear regulatory connector within the module, especially between transcriptional regulation and RNA processing. A direct role in coordinating proteasome activity across liver and prostate is not established and remains hypothetical.

## Module 8

**Tissue pair**: liver and prostate  
**Genes (46)**: AIMP2, AP3D1, ATP1A1, ATP2A2, BLVRA, CAPZB, CD2AP, CLTC, COPS3, DAZAP1, DDX46, DYNC1H1, EML4, FLII, GGH, HACD3, HSP90AA1, LUC7L2, MAN2B1, MYBBP1A, NIF3L1, OSGEP, PRPF31, PRPF4, PTPA, PPAT, UQCRC2, RECQL, SEC63, U2SURP, STT3A, AARS1, CARS1, DARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, VARS1, YARS1, CCT7, TMOD3, SNRNP200, UFD1, VTA1

### Function

The primary interpretation is a conserved RNA and protein-biosynthesis module centered on cytosolic aminoacyl-tRNA charging. The strongest evidence is the globally corrected GO and KEGG enrichment for catalytic activity acting on a tRNA (GO:MF catalytic activity, acting on a tRNA; q_global = 5.06e-05), aminoacyl-tRNA ligase activity (GO:MF aminoacyl-tRNA ligase activity; q_global = 0.000123), tRNA aminoacylation for protein translation (GO:BP tRNA aminoacylation for protein translation; q_global = 0.000123), amino acid activation (GO:BP amino acid activation; q_global = 0.000123), tRNA metabolic process (GO:BP tRNA metabolic process; q_global = 0.00024), and aminoacyl-tRNA synthetase multienzyme complex (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.000298). The module also contains a coherent RNA-processing arm: globally significant terms identify nucleic-acid and RNA catalytic activity (GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.0006) (GO:MF catalytic activity, acting on RNA; q_global = 0.000709), RNA metabolism (GO:BP RNA metabolic process; q_global = 0.0306), and spliceosomal small nuclear ribonucleoprotein complexes (GO:CC small nuclear ribonucleoprotein complex; q_global = 0.0428) (GO:CC spliceosomal snRNP complex; q_global = 0.0428) (GO:CC Sm-like protein family complex; q_global = 0.0428). Thus, the module most plausibly reflects coordinated translational capacity together with RNA maturation and quality control, rather than a single narrowly specialized pathway. The nucleotide-binding terms (GO:MF ATP binding; q_global = 0.0228) (GO:MF adenyl ribonucleotide binding; q_global = 0.0245) are compatible with the ATP-dependent chemistry of aminoacyl-tRNA synthetases and other RNA enzymes, but are less specific.

**Cell composition.** This is not primarily a plasma or secreted-protein module: the HPA summary identifies only a small secreted component, and the listed proteins are predominantly intracellular, with cytosolic or nuclear locations. It is also not strongly blood-cell enriched overall, because most genes have low immune-cell specificity. The module is broadly expressed, with most genes showing low tissue specificity and protein detection in both liver and prostate. Some cell-type signals are present, particularly spermatogenic cells, muscle-related cells, neural or glial cells, epithelial cells, and selected myeloid populations, but these do not support a simple blood-contamination explanation. The shared liver–prostate signal therefore appears more consistent with a conserved housekeeping and biosynthetic program, potentially influenced by common proliferative or translational demand, than with a plasma-protein or blood-cell module. HPA detection is incomplete for a few individual proteins, so absence of detection in one tissue should not be treated as evidence that the module is absent there.

**GO/KEGG enrichment**: 18 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF catalytic activity, acting on a tRNA | 5.06e-05 | AARS1, CARS1, DARS1, EPRS1, IARS1, LARS1, MARS1, OSGEP, QARS1, VARS1, YARS1 |
| GO:MF aminoacyl-tRNA ligase activity | 0.000123 | AARS1, CARS1, DARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, VARS1, YARS1 |
| GO:BP tRNA aminoacylation for protein translation | 0.000123 | AARS1, CARS1, DARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, VARS1, YARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 0.000123 | AARS1, CARS1, DARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, VARS1, YARS1 |
| GO:BP amino acid activation | 0.000123 | AARS1, CARS1, DARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, VARS1, YARS1 |
| GO:BP tRNA aminoacylation | 0.000123 | AARS1, CARS1, DARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, VARS1, YARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 0.000123 | AARS1, CARS1, DARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, VARS1, YARS1 |
| GO:BP tRNA metabolic process | 0.00024 | AARS1, CARS1, DARS1, EPRS1, IARS1, LARS1, MARS1, OSGEP, QARS1, VARS1, YARS1 |
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 0.000298 | AIMP2, DARS1, EPRS1, IARS1, LARS1, MARS1, QARS1 |
| GO:MF catalytic activity, acting on a nucleic acid | 0.0006 | AARS1, CARS1, DARS1, DDX46, EPRS1, IARS1, LARS1, MARS1, OSGEP, QARS1, RECQL, SNRNP200, VARS1, YARS1 |
| GO:MF catalytic activity, acting on RNA | 0.000709 | AARS1, CARS1, DARS1, DDX46, EPRS1, IARS1, LARS1, MARS1, OSGEP, QARS1, SNRNP200, VARS1, YARS1 |
| GO:BP nucleic acid metabolic process | 0.00849 | AARS1, AP3D1, CARS1, CCT7, DARS1, DAZAP1, DDX46, EPRS1, HSP90AA1, IARS1, LARS1, LUC7L2, MARS1, MYBBP1A, NIF3L1, OSGEP, PRPF31, PRPF4, PTPA, QARS1, RECQL, SNRNP200, U2SURP, VARS1, YARS1 |
| GO:MF ATP binding | 0.0228 | AARS1, ATP1A1, ATP2A2, CARS1, CCT7, DARS1, DDX46, DYNC1H1, EPRS1, HSP90AA1, IARS1, LARS1, MARS1, PTPA, QARS1, RECQL, SNRNP200, VARS1, YARS1 |
| GO:MF adenyl ribonucleotide binding | 0.0245 | AARS1, ATP1A1, ATP2A2, CARS1, CCT7, DARS1, DDX46, DYNC1H1, EPRS1, HSP90AA1, IARS1, LARS1, MARS1, PTPA, QARS1, RECQL, SNRNP200, VARS1, YARS1 |
| GO:BP RNA metabolic process | 0.0306 | AARS1, AP3D1, CARS1, DARS1, DAZAP1, DDX46, EPRS1, IARS1, LARS1, LUC7L2, MARS1, MYBBP1A, NIF3L1, OSGEP, PRPF31, PRPF4, PTPA, QARS1, SNRNP200, U2SURP, VARS1, YARS1 |

### STRING and hu.MAP

STRING provides strong prior support for the aminoacyl-tRNA synthetase core. AARS1, CARS1, DARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, VARS1, and YARS1 form a densely interconnected group, with AIMP2 linked to several of them. The supplementary STRING enrichments (9 supplementary STRING terms; within-query FDR 1.92e-05–0.0021) independently point to cytosolic tRNA aminoacylation and the multisynthetase complex. STRING also supports a distinct spliceosomal group involving DDX46, SNRNP200, PRPF31, PRPF4, LUC7L2, and U2SURP, as well as smaller relationships involving chaperoning, membrane trafficking, and cellular structure. These STRING results indicate that much of the module recapitulates known molecular relationships rather than representing arbitrary co-abundance. hu.MAP independently identifies the multisynthetase complex (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1) and a spliceosomal complex (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_06511.1). Other hu.MAP complexes connect smaller subsets involving translation-associated proteins, actin or trafficking proteins, endoplasmic-reticulum proteins, and ATP-dependent transport proteins (hu.MAP huMAP3_06247.1) (hu.MAP huMAP3_10115.1) (hu.MAP huMAP3_09592.1) (hu.MAP huMAP3_07354.1) (hu.MAP huMAP3_06945.1) (hu.MAP huMAP3_10473.1) (hu.MAP huMAP3_12900.1) (hu.MAP huMAP3_14442.1). The partial membership of these complexes suggests that the module combines several biologically real substructures rather than corresponding to one physical complex in every sample.

**STRING interactions (score >= 0.7)**: 64 of 1035 gene pairs: AARS1–AIMP2 (0.888); AARS1–CARS1 (0.872); AARS1–DARS1 (0.743); AARS1–EPRS1 (0.976); AARS1–IARS1 (0.98); AARS1–LARS1 (0.968); AARS1–MARS1 (0.913); AARS1–QARS1 (0.964); AARS1–VARS1 (0.938); AARS1–YARS1 (0.996); AIMP2–DARS1 (0.999); AIMP2–EPRS1 (0.999); AIMP2–IARS1 (0.994); AIMP2–LARS1 (0.995); AIMP2–MARS1 (0.999); AIMP2–QARS1 (0.999); ATP1A1–ATP2A2 (0.82); CAPZB–CD2AP (0.896); CAPZB–DYNC1H1 (0.964); CARS1–EPRS1 (0.849); CARS1–IARS1 (0.905); CARS1–LARS1 (0.95); CARS1–MARS1 (0.89); CARS1–QARS1 (0.838); CARS1–VARS1 (0.872); CARS1–YARS1 (0.898); CCT7–HSP90AA1 (0.849); DARS1–EPRS1 (0.999); DARS1–IARS1 (0.996); DARS1–LARS1 (0.996); DARS1–MARS1 (0.999); DARS1–QARS1 (0.999); DARS1–YARS1 (0.859); DDX46–LUC7L2 (0.74); DDX46–SNRNP200 (0.874); DDX46–U2SURP (0.918); DYNC1H1–HSP90AA1 (0.909); EPRS1–HSP90AA1 (0.701); EPRS1–IARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–MARS1 (0.999); EPRS1–QARS1 (0.999); EPRS1–VARS1 (0.97); EPRS1–YARS1 (0.999); IARS1–LARS1 (0.999); IARS1–MARS1 (0.999); IARS1–QARS1 (0.999); IARS1–VARS1 (0.9); IARS1–YARS1 (0.966); LARS1–MARS1 (0.999); LARS1–QARS1 (0.999); LARS1–VARS1 (0.968); LARS1–YARS1 (0.98); MARS1–QARS1 (0.999); MARS1–VARS1 (0.902); MARS1–YARS1 (0.999); PRPF31–PRPF4 (0.999); PRPF31–SNRNP200 (0.999); PRPF4–SNRNP200 (0.999); QARS1–VARS1 (0.91); QARS1–YARS1 (0.959); SEC63–SNRNP200 (0.733); SEC63–STT3A (0.782); VARS1–YARS1 (0.956)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Cytosolic tRNA aminoacylation (FDR = 1.92e-05, 11 genes); NetworkNeighborAL tRNA Aminoacylation, and glutamyl-tRNA(Gln) amidotransferase complex (FDR = 9.94e-05, 11 genes); NetworkNeighborAL tRNA Aminoacylation (FDR = 9.94e-05, 10 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 0.0001, 10 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 0.00018, 10 genes); COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.0003, 8 genes); Function aminoacyl-tRNA ligase activity (FDR = 0.00043, 10 genes); Function Catalytic activity, acting on a nucleic acid (FDR = 0.00045, 13 genes); Function Catalytic activity, acting on RNA (FDR = 0.00052, 12 genes); Keyword Protein biosynthesis (FDR = 0.00091, 11 genes); Process tRNA metabolic process (FDR = 0.0018, 11 genes); Process tRNA aminoacylation for protein translation (FDR = 0.0018, 10 genes); InterPro Rossmann-like alpha/beta/alpha sandwich fold (FDR = 0.0018, 8 genes); Component aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.0021, 7 genes); Keyword ATP-binding (FDR = 0.0021, 19 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, DARS1, IARS1, QARS1, MARS1, AIMP2, LARS1; 7/14); huMAP3_13688.1 (EPRS1, DARS1, IARS1, QARS1, MARS1, AIMP2, LARS1; 7/14); huMAP3_06247.1 (ATP2A2, UQCRC2, STT3A, HACD3; 4/65); huMAP3_08980.1 (PRPF4, SNRNP200, DDX46, PRPF31; 4/97); huMAP3_10115.1 (RECQL, AARS1, YARS1; 3/14); huMAP3_06511.1 (PRPF4, DDX46, PRPF31; 3/79); huMAP3_09592.1 (ATP2A2, STT3A, HACD3; 3/95); huMAP3_07354.1 (FLII, TMOD3; 2/4); huMAP3_04783.1 (AARS1, YARS1; 2/4); huMAP3_06945.1 (VARS1, CARS1; 2/4); huMAP3_04189.1 (VARS1, CARS1; 2/6); huMAP3_10302.1 (AARS1, YARS1; 2/9); huMAP3_00469.1 (VARS1, CARS1; 2/12); huMAP3_12041.1 (VARS1, CARS1; 2/16); huMAP3_10473.1 (ATP1A1, ATP2A2; 2/24); huMAP3_07410.1 (STT3A, HACD3; 2/35); huMAP3_12900.1 (CAPZB, CD2AP; 2/50); huMAP3_14442.1 (AARS1, YARS1; 2/57)

### Novelty

The biological components are not new: aminoacyl-tRNA synthetase interactions, the multisynthetase complex, spliceosomal assemblies, and many of the associated disease links are already represented by STRING and hu.MAP. The finding can nevertheless be novel at the level of a conserved liver–prostate co-abundance program, because the fact sheet does not establish that this particular cross-tissue module, its relative coupling of translation and RNA splicing, or its tissue-pair conservation has previously been reported. That claim should remain provisional. Absence of a relationship from STRING or hu.MAP would not prove novelty, especially for co-regulation without direct physical interaction. The most defensible conclusion is that this is a potentially new systems-level observation built largely from established molecular machinery, requiring comparison with published tissue co-expression modules and independent cohorts before being called a new biological module.

**Hypothesis.** Hypothesis: the module represents a conserved intracellular RNA-production and translation-support program shared by hepatocytes and prostate cells. Coordinated abundance of multisynthetase components could maintain accurate aminoacyl-tRNA charging and translational throughput, while the linked spliceosomal proteins could support processing of the resulting transcript load. The connection may be strengthened by shared cellular stress, growth, differentiation, or protein-homeostasis demands. This is a mechanistic model inferred from co-abundance and existing annotations, not proof that these proteins form one physical supercomplex or that one member directly regulates another. Testing should assess whether module activity tracks translation rate, aminoacylation, splicing efficiency, and cell-state composition in independent liver and prostate datasets.

### Important genes

#### MARS1

- **Related proteins** (co-abundance neighbors): YARS1 (0.89), IARS1 (0.88), DDX46 (0.86), VARS1 (0.86), LUC7L2 (0.85), PRPF31 (0.84), MYBBP1A (0.84), PPAT (0.84), CARS1 (0.83), PRPF4 (0.83), QARS1 (0.83), RECQL (0.82), AARS1 (0.81), COPS3 (0.81), HSP90AA1 (0.80), SNRNP200 (0.80); STRING partners: AARS1 (0.913), AIMP2 (0.999), CARS1 (0.89), DARS1 (0.999), EPRS1 (0.999), IARS1 (0.999), LARS1 (0.999), QARS1 (0.999), VARS1 (0.902), YARS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: methionyl-tRNA synthetase 1. This gene encodes a member of the class I family of aminoacyl-tRNA synthetases. These enzymes play a critical role in protein biosynthesis by charging tRNAs with their cognate amino acids. The encoded protein is a component of the multi-tRNA synthetase complex and catalyzes the ligation of methionine to tRNA molecules. [provided by RefSeq, Jan 2011].
- **Diseases (Open Targets)**: severe early-onset pulmonary alveolar proteinosis due to MARS deficiency (0.745); Charcot-Marie-Tooth disease axonal type 2U (0.676); autosomal recessive spastic paraplegia type 70 (0.614); trichothiodystrophy 9, nonphotosensitive (0.428); pulmonary alveolar proteinosis (0.338)
- **Europe PMC papers**: 435
- **Why important**: MARS1 is the highest-positioned node among the listed genes in the module network and is embedded in the multisynthetase core. It is a methionyl-tRNA synthetase, appears across the primary GO and KEGG terms (15 globally significant GO/KEGG terms, q_global 5.06e-05–0.0306; see the table), is supported by the STRING aminoacylation terms (15 supplementary STRING terms; within-query FDR 1.92e-05–0.0021), and belongs to the hu.MAP multisynthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). Its disease associations include MARS deficiency and inherited neurological or multisystem disorders, while its substantial literature supports a well-established molecular function.
- **Conclusion**: Established evidence supports MARS1 as a central translational enzyme and a strong representative of the module's core function. Its network position and broad annotation make it an anchor gene for interpretation. It is a plausible marker of module activity, but the data do not establish that MARS1 drives the shared liver–prostate pattern.

#### EPRS1

- **Related proteins** (co-abundance neighbors): DDX46 (0.91), YARS1 (0.89), MYBBP1A (0.88), OSGEP (0.87), QARS1 (0.86), CCT7 (0.83), VARS1 (0.83), RECQL (0.82), LUC7L2 (0.82), IARS1 (0.81), AARS1 (0.81), DAZAP1 (0.80); STRING partners: AARS1 (0.976), AIMP2 (0.999), CARS1 (0.849), DARS1 (0.999), HSP90AA1 (0.701), IARS1 (0.999), LARS1 (0.999), MARS1 (0.999), QARS1 (0.999), VARS1 (0.97), YARS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is a multifunctional glutamyl-prolyl-tRNA synthetase, occupies a highly connected position, and is linked to nearly every aminoacylation component through STRING. It is present in the globally corrected aminoacylation, RNA-catalysis, ATP-binding, and RNA-metabolism terms (15 globally significant GO/KEGG terms, q_global 5.06e-05–0.0306; see the table), in the supplementary STRING aminoacylation results (15 supplementary STRING terms; within-query FDR 1.92e-05–0.0021), and in the hu.MAP multisynthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). Its disease associations include inherited leukodystrophy and developmental disorders, and it has substantial literature support.
- **Conclusion**: Established evidence identifies EPRS1 as a core enzymatic and structural component of the translational submodule. Because it connects the synthetase group to RNA-processing and chaperone-related proteins in the network, it is a useful candidate for linking translational demand to broader RNA homeostasis. A direct coordinating role remains a hypothesis.

#### DDX46

- **Related proteins** (co-abundance neighbors): LARS1 (0.93), SNRNP200 (0.91), EPRS1 (0.91), SEC63 (0.89), QARS1 (0.89), MARS1 (0.86), YARS1 (0.86), LUC7L2 (0.85), VTA1 (0.84), IARS1 (0.83), STT3A (0.83), CCT7 (0.82), AARS1 (0.82), EML4 (0.80); STRING partners: LUC7L2 (0.74), SNRNP200 (0.874), U2SURP (0.918)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_06511.1
- **Function (MyGene.info)**: DEAD-box helicase 46. This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribu…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); dengue disease (0.370); Hypercholesterolemia (0.203); lung adenocarcinoma (0.074); osteosarcoma (0.053)
- **Europe PMC papers**: 592
- **Why important**: DDX46 is among the most connected genes and provides a bridge from the aminoacylation-rich portion of the module to the spliceosomal portion. It is a DEAD-box RNA helicase associated with pre-mRNA splicing and prespliceosome assembly, and it appears in the globally corrected RNA-catalysis and spliceosomal terms (9 globally significant GO/KEGG terms, q_global 0.0006–0.0428; see the table). STRING connects it to SNRNP200, LUC7L2, and U2SURP, while hu.MAP supports spliceosomal complexes (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_06511.1). Its disease and neurological associations, together with substantial literature, make it a biologically informative bridge gene.
- **Conclusion**: Established evidence supports DDX46 as a component of RNA processing and spliceosome assembly, not as an aminoacyl-tRNA synthetase. Its position suggests that the module integrates translation with pre-mRNA processing. Whether this reflects coordinated regulation, shared cellular state, or indirect abundance effects is unresolved.

#### AIMP2

- **Related proteins** (co-abundance neighbors): COPS3 (0.85), OSGEP (0.81); STRING partners: AARS1 (0.888), DARS1 (0.999), EPRS1 (0.999), IARS1 (0.994), LARS1 (0.995), MARS1 (0.999), QARS1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: aminoacyl tRNA synthetase complex interacting multifunctional protein 2. The protein encoded by this gene is part of the aminoacyl-tRNA synthetase complex, which contains nine different aminoacyl-tRNA synthetases and three non-enzymatic factors. The encoded protein is one of the non-enzymatic factors and is required for assembly and stability of the complex. [provided by RefSeq, May 2016].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 17 (0.617); hereditary disease (0.494); Neurodevelopmental abnormality (0.111); Parkinson disease (0.107); neoplasm (0.106)
- **Europe PMC papers**: 605
- **Why important**: AIMP2 is a non-enzymatic component required for assembly and stability of the aminoacyl-tRNA synthetase complex. Although its direct module degree is modest, it has strong STRING links to the synthetase group and is included in the multisynthetase hu.MAP complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). It also contributes to the globally significant multienzyme-complex term (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.000298) and has disease associations involving leukodystrophy and neurodevelopmental phenotypes. Its literature supports a recognized structural role in the complex.
- **Conclusion**: Established evidence supports AIMP2 as an organizing component of the translational core rather than merely a catalytic enzyme. It may help explain why several synthetases co-vary as a unit. The co-abundance data do not demonstrate that changes in AIMP2 assemble or disassemble the complex in these tissues.

#### YARS1

- **Related proteins** (co-abundance neighbors): CCT7 (0.92), MARS1 (0.89), EPRS1 (0.89), LUC7L2 (0.87), AARS1 (0.87), SEC63 (0.87), IARS1 (0.86), VARS1 (0.86), DDX46 (0.86), COPS3 (0.84), SNRNP200 (0.84), HSP90AA1 (0.83), CLTC (0.82), RECQL (0.81); STRING partners: AARS1 (0.996), CARS1 (0.898), DARS1 (0.859), EPRS1 (0.999), IARS1 (0.966), LARS1 (0.98), MARS1 (0.999), QARS1 (0.959), VARS1 (0.956)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_10115.1, huMAP3_04783.1, huMAP3_10302.1, huMAP3_14442.1
- **Function (MyGene.info)**: tyrosyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Tyrosyl-tRNA synthetase belongs to the class I tRNA synthetase family. Cytokine activities have also been observ…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease dominant intermediate C (0.739); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset 2 (0.707); hereditary disease (0.509); Charcot-Marie-Tooth disease (0.418); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset (0.333)
- **Europe PMC papers**: 215
- **Why important**: YARS1 is highly connected to the synthetase group and is also linked in the network to RNA-processing and cellular quality-control proteins. It is a tyrosyl-tRNA synthetase represented across the primary aminoacylation and RNA-metabolism terms (15 globally significant GO/KEGG terms, q_global 5.06e-05–0.0306; see the table), the supplementary STRING terms (13 supplementary STRING terms; within-query FDR 1.92e-05–0.0021), and several hu.MAP complexes (hu.MAP huMAP3_10115.1) (hu.MAP huMAP3_04783.1) (hu.MAP huMAP3_10302.1) (hu.MAP huMAP3_14442.1). Its established disease associations include inherited neuropathic and multisystem developmental disorders, and its literature supports both canonical aminoacylation and additional reported cellular activities.
- **Conclusion**: Established evidence supports YARS1 as a core translational enzyme and a useful indicator of the synthetase-rich part of the module. Its additional network links make it a candidate interface between translation and other intracellular processes, but those links do not by themselves establish a noncanonical regulatory function in liver or prostate.

#### LARS1

- **Related proteins** (co-abundance neighbors): DDX46 (0.93), AP3D1 (0.87), MYBBP1A (0.86), SNRNP200 (0.82), DAZAP1 (0.82), COPS3 (0.82), LUC7L2 (0.81), IARS1 (0.80); STRING partners: AARS1 (0.968), AIMP2 (0.995), CARS1 (0.95), DARS1 (0.996), EPRS1 (0.999), IARS1 (0.999), MARS1 (0.999), QARS1 (0.999), VARS1 (0.968), YARS1 (0.98)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in liver, prostate
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: leucyl-tRNA synthetase 1. This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals w…
- **Diseases (Open Targets)**: infantile liver failure syndrome 1 (0.670); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.510); Global developmental delay (0.119); sensorineural hearing loss disorder (0.119); Generalized-onset seizure (0.118)
- **Europe PMC papers**: 267
- **Why important**: LARS1 is a cytosolic leucyl-tRNA synthetase with strong connectivity to the multisynthetase core and prominent representation across the primary aminoacylation terms (15 globally significant GO/KEGG terms, q_global 5.06e-05–0.0306; see the table). STRING and hu.MAP both support its association with the multisynthetase complex (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), and its annotated responses to amino-acid availability are relevant to interpreting a conserved biosynthetic module. Its disease associations include infantile liver failure and developmental or neurological phenotypes, with substantial literature support.
- **Conclusion**: Established evidence supports LARS1 as a central enzyme connecting amino-acid sensing and translational capacity. Its presence in a liver–prostate module is compatible with shared control of protein synthesis, but the co-abundance result does not show that amino-acid sensing is the cause of module conservation.

## Module 9

**Tissue pair**: liver and prostate  
**Genes (5)**: GFM1, IDE, OPA1, SYNJ2BP, VAPB

### Function

The module does not have a GO or KEGG term passing global correction. It also has no STRING functional enrichment. Its gene composition nevertheless points toward linked cellular maintenance processes: mitochondrial translation and respiratory-chain support through GFM1, mitochondrial organization and energy regulation through OPA1, mitochondrial outer-membrane and signaling roles through SYNJ2BP, endoplasmic-reticulum and vesicle-trafficking functions through VAPB, and intracellular peptide and insulin processing through IDE. The co-abundance pattern is therefore most consistent with a possible organelle homeostasis and protein or peptide-handling program, rather than a formally established pathway annotation.

**Cell composition.** All module genes have low tissue specificity in HPA, and protein detection is present in both liver and prostate for nearly the entire module. None is blood-cell enriched, and the module is not dominated by plasma proteins or secreted proteins. IDE is annotated as secreted in other tissues, but the other genes are intracellular or membrane-associated. The heterogeneous single-cell enhancements, including epicardial cells, neuronal cells, enterocytes, epididymal clear cells, gastric chief cells, and platelets, do not define a coherent liver- or prostate-specific cell population. Thus, the shared module is unlikely to be explained primarily by immune-cell contamination or a plasma-protein signature, although broad expression and shared cellular physiology remain plausible contributors.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No pair among the module genes reaches the supplied high-confidence STRING interaction threshold, and STRING reports no functional enrichment. No hu.MAP complex contains multiple module members. These results mean that the co-abundance edges are not supported by detected, well-established physical interactions or a recognized multiprotein complex in these resources. The individual annotations still provide biological context: VAPB is reported to interact with VAMP proteins and to form homo- and heteromeric assemblies with VAPA; GFM1 is a mitochondrial translation factor; OPA1 regulates mitochondrial inner-membrane organization; SYNJ2BP is an integral mitochondrial outer-membrane protein; and IDE is a peptide-degrading metallopeptidase. Those facts support related cellular themes but do not establish a direct five-gene molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact liver–prostate co-abundance module may represent a new observation because its member combination is not reproduced by the supplied STRING or hu.MAP evidence, and no globally enriched GO or KEGG term explains it. However, absence from these resources does not prove biological novelty: the genes have established individual functions, and co-abundance can arise from shared regulation, organelle content, cell composition, or technical structure without a direct physical interaction. The defensible conclusion is that the module is potentially novel as a cross-tissue co-abundance pattern, but its mechanistic novelty remains unvalidated.

**Hypothesis.** Hypothesis: the module reflects coordinated maintenance of organelle and proteostasis capacity across liver and prostate cells. GFM1 and OPA1 could represent mitochondrial translation and inner-membrane integrity, SYNJ2BP could connect mitochondrial outer-membrane signaling to cellular regulation, VAPB could couple endoplasmic-reticulum organization and vesicle or lipid handling, and IDE could link this state to intracellular peptide turnover and insulin-related signaling. The module may therefore mark a shared metabolic or stress-adaptation state rather than a stable physical complex. This hypothesis requires validation with independent cohorts, cell-resolved data, perturbation experiments, and measurements of mitochondrial, endoplasmic-reticulum, and peptide-processing activity.

### Important genes

#### GFM1

- **Related proteins** (co-abundance neighbors): OPA1 (0.84), SYNJ2BP (0.81), VAPB (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G elongation factor mitochondrial 1. Eukaryotes contain two protein translational systems, one in the cytoplasm and one in the mitochondria. Mitochondrial translation is crucial for maintaining mitochondrial function and mutations in this system lead to a breakdown in the respiratory chain-oxidative phosphorylation system and to impaired maintenance of mitochondrial DNA. This gene encodes one of the mitochondrial translation elongati…
- **Diseases (Open Targets)**: hepatoencephalopathy due to combined oxidative phosphorylation defect type 1 (0.822); neurodegenerative disease (0.463); combined oxidative phosphorylation deficiency (0.451); hereditary disease (0.341); Leigh syndrome (0.313)
- **Europe PMC papers**: 1380
- **Why important**: GFM1 is the strongest network-connected gene in the module, linking OPA1, SYNJ2BP, and VAPB. Its established role in mitochondrial translational elongation directly connects the module to production of proteins needed for mitochondrial function and oxidative phosphorylation. It has a substantial literature base and disease associations involving combined oxidative-phosphorylation defects and hepatoencephalopathy.
- **Conclusion**: Established evidence supports GFM1 as the central mitochondrial-translation component and the principal network hub. Hypothesis: its central position may indicate that variation in mitochondrial protein-synthesis capacity helps organize the broader co-abundance pattern.

#### VAPB

- **Related proteins** (co-abundance neighbors): GFM1 (0.80), IDE (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VAMP associated protein B and C. The protein encoded by this gene is a type IV membrane protein found in plasma and intracellular vesicle membranes. The encoded protein is found as a homodimer and as a heterodimer with VAPA. This protein also can interact with VAMP1 and VAMP2 and may be involved in vesicle trafficking. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis type 8 (0.729); amyotrophic lateral sclerosis (0.658); adult-onset proximal spinal muscular atrophy, autosomal dominant (0.654); neurodegenerative disease (0.468); amyotrophic lateral sclerosis, dominant (0.370)
- **Europe PMC papers**: 2845
- **Why important**: VAPB is the second network connector, linking GFM1 with IDE. It is an endoplasmic-reticulum and vesicle-membrane protein involved in vesicle trafficking, membrane organization, calcium homeostasis, and cholesterol transport. Its disease associations include amyotrophic lateral sclerosis and related motor-neuron disorders, and it has a substantial literature base.
- **Conclusion**: Established evidence supports VAPB as an endoplasmic-reticulum and membrane-trafficking component with important disease relevance. Hypothesis: VAPB may provide the organelle-contact or membrane-handling link between mitochondrial maintenance and IDE-associated peptide processing.

#### OPA1

- **Related proteins** (co-abundance neighbors): GFM1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OPA1 mitochondrial dynamin like GTPase. The protein encoded by this gene is a nuclear-encoded mitochondrial protein with similarity to dynamin-related GTPases. The encoded protein localizes to the inner mitochondrial membrane and helps regulate mitochondrial stability and energy output. This protein also sequesters cytochrome c. Mutations in this gene have been associated with optic atrophy type 1, which is a dominantly inherited optic …
- **Diseases (Open Targets)**: autosomal dominant optic atrophy, classic form (0.846); Behr syndrome (0.812); optic atrophy with or without deafness, ophthalmoplegia, myopathy, ataxia, and neuropathy (0.766); mitochondrial DNA depletion syndrome 14B (cardioencephalomyopathic type) (0.745); optic atrophy (0.653)
- **Europe PMC papers**: 12169
- **Why important**: OPA1 is directly connected to the module hub GFM1 and is a core regulator of mitochondrial inner-membrane organization, fusion, stability, and energy output. It also sequesters cytochrome c and has extensive literature and strong disease associations with dominant optic atrophy and related mitochondrial syndromes.
- **Conclusion**: Established evidence supports OPA1 as a mitochondrial-structure and energy-maintenance gene. Hypothesis: its co-abundance with GFM1 may reflect coordinated control of mitochondrial translation and mitochondrial architecture.

#### IDE

- **Related proteins** (co-abundance neighbors): VAPB (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin degrading enzyme. This gene encodes a zinc metallopeptidase that degrades intracellular insulin, and thereby terminates insulins activity, as well as participating in intercellular peptide signalling by degrading diverse peptides such as glucagon, amylin, bradykinin, and kallidin. The preferential affinity of this enzyme for insulin results in insulin-mediated inhibition of the degradation of other peptides such as…
- **Diseases (Open Targets)**: diabetes mellitus (0.307); type 2 diabetes mellitus (0.287); diabetic retinopathy (0.146); diabetic eye disease (0.144); brain cancer (0.142)
- **Europe PMC papers**: 19876
- **Why important**: IDE is connected to VAPB and contributes a distinct biochemical function: degradation of insulin and other peptides, including glucagon, amylin, bradykinin, and kallidin. It also participates in insulin-receptor signaling, proteolysis, and peptide-antigen processing. IDE has the largest literature base among the module genes and disease associations involving diabetes and related metabolic disorders.
- **Conclusion**: Established evidence supports IDE as an intracellular peptide-processing and metabolic-signaling enzyme. Hypothesis: IDE may indicate that the module couples organelle homeostasis to peptide turnover or insulin-related metabolic state, although the supplied data do not establish causality.

#### SYNJ2BP

- **Related proteins** (co-abundance neighbors): GFM1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: synaptojanin 2 binding protein. Predicted to enable type II activin receptor binding activity. Involved in several processes, including negative regulation of endothelial cell migration; negative regulation of sprouting angiogenesis; and regulation of signal transduction. Located in mitochondrion. Is integral component of mitochondrial outer membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Hypercholesterolemia (0.258); prostate carcinoma (0.178); response to statin (0.170); neoplasm (0.094); breast cancer (0.082)
- **Europe PMC papers**: 330
- **Why important**: SYNJ2BP is a mitochondrial outer-membrane protein and is connected to GFM1. Its annotations involve negative regulation of endothelial migration, angiogenesis, ERK signaling, and Notch signaling. It has a smaller literature base than the other selected genes, but its mitochondrial localization and links to vascular and prostate-cancer annotations make it a potentially informative tissue-context component.
- **Conclusion**: Established evidence supports SYNJ2BP as a mitochondrial membrane-associated regulator with signaling and angiogenesis-related annotations. Hypothesis: it may connect mitochondrial state to cell-signaling or vascular-regulatory programs in the shared module, but this interpretation is less established than the mitochondrial roles of GFM1 and OPA1.
