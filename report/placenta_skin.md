# Conserved co-abundance modules: placenta and skin

## Module 0

**Tissue pair**: placenta and skin  
**Genes (5)**: ANXA3, HSPB1, KRT18, KRT7, KRT8

### Function

The module is most consistent with a simple epithelial structural and stress-response program. KRT7, KRT8, and KRT18 form the central keratin-associated component: KRT8 and KRT18 are an established intermediate-filament pair, while KRT7 is linked to epithelial differentiation and intermediate-filament organization. HSPB1 adds a protein-folding and environmental-stress response component, and ANXA3 adds a membrane-associated signaling, migration, and defense-response component. The STRING supplementary results support an epithelial and intermediate-filament interpretation through the colonic cancer cell, squamous epithelium, mixed epithelial, and intermediate-filament annotations (STRING TISSUES Colonic cancer cell; within-query FDR = 0.008), (STRING TISSUES Squamous epithelium; within-query FDR = 0.0097), (STRING NetworkNeighborAL Mixed, incl. Signet ring cell adenocarcinoma, and Apical plasma membrane urothelial plaque; within-query FDR = 0.0498), (STRING SMART Intermediate filament protein; within-query FDR = 0.0499). No GO or KEGG term passed global correction, so there is no globally significant GO or KEGG enrichment to report. The absence of a globally enriched term does not invalidate the coherent gene-level and network-level interpretation.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the module genes are annotated as non-secreted, and all are detected at the protein level in both placenta and skin. The HPA evidence instead points toward cell-type composition and epithelial or trophoblast biology. Several genes are enhanced in epithelial, trophoblast, glandular, or lung-associated cell types. The recurrent migrating cytotrophoblast and extravillous trophoblast signals are especially compatible with placental epithelial-like or trophoblast populations, while the alveolar, esophageal, intestinal, and glandular signals indicate broader epithelial representation. ANXA3 has immune-cell enrichment in neutrophils, and KRT8, KRT18, and ANXA3 have additional blood-cell signals, but the module is not predominantly a blood-cell or immune module. Shared epithelial or trophoblast-related cell types, and possibly sample cellular composition, may therefore contribute to the conserved placenta-skin co-abundance pattern.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides strong support for a known keratin relationship between KRT8 and KRT18 and support for a KRT7-KRT8 relationship. The remaining co-abundance links, involving KRT7 with HSPB1 and ANXA3, are not represented as high-confidence STRING interactions in the supplied evidence. The supplementary STRING functional annotations are driven mainly by the three keratin genes, with HSPB1 and ANXA3 contributing to the colonic cancer cell annotation (STRING TISSUES Colonic cancer cell; within-query FDR = 0.008). No hu.MAP complex contains multiple members of this module. Thus, the module contains a well-established keratin subnetwork embedded in a broader co-abundance pattern, rather than corresponding to a previously catalogued multi-protein complex.

**STRING interactions (score >= 0.7)**: 2 of 10 gene pairs: KRT18–KRT8 (0.999); KRT7–KRT8 (0.746)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Colonic cancer cell (FDR = 0.008, 5 genes); TISSUES Squamous epithelium (FDR = 0.0097, 3 genes); NetworkNeighborAL Mixed, incl. Signet ring cell adenocarcinoma, and Apical plasma membrane urothelial plaque (FDR = 0.0498, 3 genes); SMART Intermediate filament protein (FDR = 0.0499, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The keratin biology itself is not a new finding: KRT8-KRT18 filament formation and epithelial expression are established, and KRT7 is a recognized epithelial keratin. The likely novel aspect is the conservation of this particular co-abundance arrangement across placenta and skin, especially its association with HSPB1 and ANXA3 in the same module. That conclusion should remain cautious because co-abundance can reflect shared cell types or tissue composition, and because the module is small. Its lack of a matching hu.MAP complex and the limited STRING representation of some links are compatible with a potentially new module-level observation, but absence from those resources alone does not prove novelty. Independent replication, cell-composition adjustment, and comparison with published placenta-skin co-expression modules would be needed to establish novelty.

**Hypothesis.** Hypothesis: the module reflects a conserved epithelial or trophoblast structural-stress state shared by placenta and skin. In this model, KRT7, KRT8, and KRT18 provide the intermediate-filament scaffold; HSPB1 helps maintain proteostasis and stress tolerance during differentiation or environmental stress; and ANXA3 links the structural state to membrane-associated signaling, migration, vascular or inflammatory interactions, and tissue repair. The shared signal may arise from epithelial-like cells present in both tissues rather than from a secreted systemic program. This is a mechanistic hypothesis, not a demonstrated causal pathway from the enrichment analysis.

### Important genes

#### KRT7

- **Related proteins** (co-abundance neighbors): KRT8 (0.92), HSPB1 (0.88), ANXA3 (0.84); STRING partners: KRT8 (0.746)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments, Cytosol; IHC detected in placenta, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 7. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the simple epithelia lining the cavities of the internal organs and in th…
- **Diseases (Open Targets)**: neoplasm (0.118); lung carcinoma (0.105); cancer (0.102); lung cancer (0.099); colorectal carcinoma (0.099)
- **Europe PMC papers**: 3815
- **Why important**: KRT7 is the most connected and strongest node in the module, linking the KRT8 keratin pair to HSPB1 and ANXA3. It is annotated in intermediate-filament organization and keratinization, is detected in both tissues, and has epithelial and trophoblast cell-type associations. It also has extensive literature covering epithelial differentiation and neoplasia.
- **Conclusion**: Established evidence supports KRT7 as the module's network bridge and as an epithelial intermediate-filament marker. It is plausible, but not demonstrated, that KRT7 coordinates the keratin scaffold with the stress and membrane-associated components.

#### KRT8

- **Related proteins** (co-abundance neighbors): KRT18 (0.96), KRT7 (0.92); STRING partners: KRT18 (0.999), KRT7 (0.746)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Intermediate filaments; IHC detected in placenta, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 8. This gene is a member of the type II keratin family clustered on the long arm of chromosome 12. Type I and type II keratins heteropolymerize to form intermediate-sized filaments in the cytoplasm of epithelial cells. The product of this gene typically dimerizes with keratin 18 to form an intermediate filament in simple single-layered epithelial cells. This protein plays a role in maintaining cellul…
- **Diseases (Open Targets)**: cirrhosis of liver (0.596); cirrhosis, familial (0.401); neurodegenerative disease (0.371); prostate carcinoma (0.314); Abnormality of the liver (0.306)
- **Europe PMC papers**: 5942
- **Why important**: KRT8 is a central keratin node connected to KRT7 and KRT18, with very strong STRING support for the KRT8-KRT18 relationship. Its annotations include intermediate-filament organization, epithelial development, cellular structural integrity, differentiation, and regulation of apoptosis. It is detected in both tissues, has trophoblast and epithelial cell-type associations, and has substantial disease and literature evidence.
- **Conclusion**: Established evidence identifies KRT8 as a core structural component of simple epithelial intermediate filaments and the principal connector between KRT7 and KRT18. Its role as a causal organizer of the entire conserved module remains a hypothesis.

#### KRT18

- **Related proteins** (co-abundance neighbors): KRT8 (0.96); STRING partners: KRT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in placenta, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 18. KRT18 encodes the type I intermediate filament chain keratin 18. Keratin 18, together with its filament partner keratin 8, are perhaps the most commonly found members of the intermediate filament gene family. They are expressed in single layer epithelial tissues of the body. Mutations in this gene have been linked to cryptogenic cirrhosis. Two transcript variants encoding the same protein have bee…
- **Diseases (Open Targets)**: cirrhosis of liver (0.623); cirrhosis, familial (0.396); prostate carcinoma (0.140); neoplasm (0.117); breast carcinoma (0.113)
- **Europe PMC papers**: 6539
- **Why important**: KRT18 is the direct partner of KRT8 and completes the best-supported filament relationship in the module. It is associated with intermediate-filament organization, cell-cell adhesion, protein transport, and regulation of apoptosis, is detected in placenta and skin, and has extensive literature and disease association, including cirrhosis.
- **Conclusion**: Established evidence supports KRT18 as the type one partner of KRT8 in epithelial intermediate filaments and as a major structural anchor of the module. The co-abundance data support shared regulation or shared cell origin, but do not establish that KRT18 drives the placenta-skin association.

#### HSPB1

- **Related proteins** (co-abundance neighbors): KRT7 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in placenta, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family B (small) member 1. This gene encodes a member of the small heat shock protein (HSP20) family of proteins. In response to environmental stress, the encoded protein translocates from the cytoplasm to the nucleus and functions as a molecular chaperone that promotes the correct folding of other proteins. This protein plays an important role in the differentiation of a wide variety of cell types. Expression of this gene …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2F (0.810); neuronopathy, distal hereditary motor, type 2B (0.808); Charcot-Marie-Tooth disease (0.540); hereditary disease (0.510); distal hereditary motor neuropathy type 2 (0.455)
- **Europe PMC papers**: 10348
- **Why important**: HSPB1 is connected to the module hub KRT7 and is the only member with the supplied STRING association specifically linked to the colonic cancer cell annotation without appearing in the keratin-focused supplementary terms (STRING TISSUES Colonic cancer cell; within-query FDR = 0.008). It is annotated as a small heat-shock chaperone involved in protein folding, unfolded-protein and heat responses, translational regulation, and differentiation. It has extensive literature and is detected in both tissues.
- **Conclusion**: Established evidence supports HSPB1 as a stress-proteostasis and differentiation component connected to the epithelial keratin program. Its inclusion suggests a stress-adapted epithelial state, but whether it mechanistically stabilizes the keratin network in these tissues is unproven.

#### ANXA3

- **Related proteins** (co-abundance neighbors): KRT7 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in placenta, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A3. This gene encodes a member of the annexin family.  Members of this calcium-dependent phospholipid-binding protein family play a role in the regulation of cellular growth and in signal transduction pathways.  This protein functions in the inhibition of phopholipase A2 and cleavage of inositol 1,2-cyclic phosphate to form inositol 1-phosphate. This protein may also play a role in anti-coagulation. […
- **Diseases (Open Targets)**: rheumatoid arthritis (0.318); Meniere disease (0.276); insomnia (0.255); hair color (0.209); refractive error (0.176)
- **Europe PMC papers**: 2243
- **Why important**: ANXA3 is connected to KRT7 and contributes a distinct membrane-associated biology to an otherwise keratin-centered module. Its annotations include phospholipid binding, signal transduction, phagocytosis, neutrophil degranulation, endothelial migration, angiogenesis, and bacterial defense. HPA links it to bone marrow, migrating cytotrophoblasts, alveolar cells, and neutrophils, and it is detected in both tissues.
- **Conclusion**: Established evidence supports ANXA3 as a membrane-associated signaling and defense protein with trophoblast, vascular, and myeloid relevance. Its connection to the epithelial structural core may reflect tissue repair, migration, or cellular composition; a direct mechanistic bridge to KRT7 is a hypothesis rather than an established interaction.
